# 10 — Metricool drafts

**V2 · 2026-09-19 · Governs n8n nodes: `Restore payload for Metricool` · `Call Metricool Drafts` → sub-workflow `Betty — QDE Metricool Drafts v1` (`em4VP1LAYyE3BPbJ`): `Next open slot` · `Assemble drafts` · `Metricool: create draft` · `Verify + collect`**

`POST https://app.metricool.com/api/v2/scheduler/posts?blogId=6268508&userId=4831552`, Header Auth `Metricool X-Mc-Auth`, body `saveExternalMediaFiles: true`, **`draft: true`, always**. One call per draft. Betty never schedules.

## What changed in V2

**1\. The `vertical_url` gate is gone.** V1 gated TikTok, Instagram and FB REEL on a `vertical_url` field. No node in any of the three workflows ever assigned that field — it was only ever read. The result was that three of the four drafts were skipped on **every** run since the workflow was built, and only the Facebook POST was created. This was not a per-row data gap; it could not succeed for any row.

All four drafts now take `long_url`, the Drive download URL that `Media facts` builds, so the drafts build from the file the row actually has.

This is a wiring fix, not a decision about vertical cuts. Vertical cuts are produced on the Mac (file 08\) and land in Drive; what was missing is any node that registers one onto the row as `vertical_url`. If that registration is added later, this table is where the three short-form drafts switch back to it — change the `short_media` line in `Assemble drafts`, which is the single point of control.

**2\. One caption, four drafts.** All four drafts carry the same `caption` text (file 06). The per-platform fields still exist on the row after the fan-out; they hold identical text.

**3\. `Restore payload for Metricool` is mandatory.** `Call Metricool Drafts` must be fed from this node, never directly from `Call YouTube Publish`. The YouTube sub-workflow's last node on the success path is an ntfy HTTP call, so feeding Metricool from it delivers ntfy's reply (`id, time, expires, event, topic, message`) instead of the pipeline payload — every copy field arrives empty and Metricool answers `text: must not be null`. The restore node pulls the real payload from `Prepare distribution payload` and carries the YouTube ID forward.

## `Next open slot` — the shared sub-workflow (fixes the 2026-09-14 stacking bug)

Input: `blogId`. Output: `publish_date` (`yyyy-MM-dd`; posts go at 09:00 America/Chicago).

1. `GET …/scheduler/posts?blogId=…&userId=…&start=<today>&end=<today+45d>&timezone=America/Chicago` — every scheduled *and draft* post.  
2. Collect the set of dates that already hold a QDE post.  
3. Starting tomorrow, walk forward Mon–Fri only; return the first date not in the set.  
4. Remember the date you choose. That date must be included in the slack message  upon confirmation for a human to find the posts quickly during their human review. 

Both the post lane and this lane call it, so the two never stack on each other. `n8n/Next_Open_Slot_subworkflow_v1.json`.

## The four drafts

| Draft | providers | networkData | media | text |
| :---- | :---- | :---- | :---- | :---- |
| TikTok | `tiktok` | `{title: tiktok_hook, privacyOption: "PUBLIC_TO_EVERYONE"}` | `long_url` | `caption` |
| Instagram | `instagram` | `{type: "REEL", showReelOnFeed: true}` | `long_url` | `caption` |
| FB POST | `facebook` | `{type: "POST", title: title}` | `long_url` — skipped if `over_fb_cap`, flag `FB_POST_OVER_CAP` | `caption` |
| FB REEL | `facebook` | `{type: "REEL", title: title}` | `long_url` | `caption` |

All four carry the same `publish_date` from the sub-workflow. `videoThumbnailUrl` is omitted. LinkedIn and GBP are not created by this workflow until "network scope" is decided (file 00).

Retired flags: `NO_VERTICAL` no longer exists — nothing gates on a vertical asset.

## `Verify + collect`

`getScheduledPosts` for the date; assert each draft exists with `draft: true`, correct `type`, `blogId 6268508`, `media` now a `static.metricool.com` URL. Ids → row. A draft that fails to normalize media → flag `MEDIA_NOT_NORMALIZED` (Drive sharing is the usual cause; the FTP bridge is retired from this lane — fix sharing instead).

**Never accept the node's own `executionStatus` as proof.** `Metricool: create draft` continues on error, so it reports `success` while the API returned 400 and created nothing. Confirm at Metricool's API or not at all.

## Dedup

For scheduling decisions, dedup against the **live calendar** (`getScheduledPosts`), not the MASTER sheet's T/V columns — the sheet lags.

## Updating the master sheet

Never write into columns A–Y. That contains content you do not touch. Only columns AM–AP are available for n8n to write to at this time.

## Refinement hook

Which networks / captions map where → the table above. Slot rule → the sub-workflow. Copy → file 06\. Media URL construction → file 02\.  
