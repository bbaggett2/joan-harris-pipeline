# 10 — Metricool drafts
**V1 · 2026-09-19 · Governs n8n nodes: `Restore payload for Metricool` · `Call Metricool Drafts` → HU sub-workflow: `Next open slot` · `Assemble drafts` · `Metricool: create draft` · `Verify + collect`**

## The call

```
POST https://app.metricool.com/api/v2/scheduler/posts?blogId=6267975&userId=4831552
Header Auth: Metricool X-Mc-Auth
body: saveExternalMediaFiles: true, draft: true   ← always
```

⚠️ **Same API token as QDE, different `blogId`.** The call succeeds either way — a 200 proves nothing about which brand received the post. HU is `6267975`; QDE is `6268508`. This is the single most likely way HU content lands on the QDE calendar. Confirm the `blogId` by reading the draft back, never by a successful POST.

⛔ **One `createScheduledPost` call per draft.** Never bundle providers: Metricool exposes a single shared `text` field per post — only `tiktokData.title` and `facebookData.title` are per-network — so a bundled post forces one caption onto every platform.

⛔ **Never schedule. `draft: true`, no publish time.** The reviewer schedules, and that is the approval. `autoPublish: false` is banned outright — it is not a hold, it is a notification that silently dies.

## `Restore payload for Metricool` is mandatory

`Call Metricool Drafts` must be fed from this node, **never directly from `Call YouTube Publish`**. The YouTube sub-workflow's last node on the success path is an ntfy HTTP call, so feeding Metricool from it delivers ntfy's reply (`id, time, expires, event, topic, message`) instead of the pipeline payload — every copy field arrives empty and Metricool answers `text: must not be null`.

## The four drafts

| Draft | providers | networkData | media | text |
|---|---|---|---|---|
| TikTok | `tiktok` | `{title: <hook>, privacyOption: "PUBLIC_TO_EVERYONE"}` | `vertical_url` | `tiktok_caption` |
| Instagram | `instagram` | `{type: "REEL", showReelOnFeed: true}` | `vertical_url` | `instagram_caption` |
| FB POST | `facebook` | `{type: "POST", title: <title>}` | `long_url` — skipped if `over_fb_cap`, flag `FB_POST_OVER_CAP` | `fb_long` |
| FB REEL | `facebook` | `{type: "REEL", title: <title>}` | `vertical_url` | `fb_short` |

**Two differences from the QDE lane — both deliberate, both Bart's ruling 2026-09-19:**

1. **`short_media` is `vertical_url`, not `long_url`.** QDE currently sends the long file to all four because nothing ever registered a vertical cut. File 08 builds that wiring for HU. `Assemble drafts` is the single point of control — if the vertical registration is ever removed, this is the one line that changes.
2. **Each draft carries its own caption.** QDE's file 10 still describes "one caption, four drafts"; that is stale. Per-platform copy is the rule.

**Facebook always gets both.** Reels and the feed are separate surfaces with separate audiences; publishing one leaves the other empty. No duration test decides either type — the POST always takes the full-length cut, the REEL always the vertical.

**No YouTube draft.** The video is already on the channel from file 09; a Metricool YouTube draft would duplicate it.

⛔ **No LinkedIn, no X.** Neither is connected to the HU brand, and X `@handwritingu` is suspended. Not "skipped pending a decision" — absent.

**`videoThumbnailUrl` is omitted.** Sent speculatively it rejects the entire request with `VIDEO_THUMBNAIL_NOT_APPLICABLE`.

## `Next open slot`

Input `blogId`, output `publish_date`.

1. `GET …/scheduler/posts?blogId=…&userId=…&start=<today>&end=<today+45d>&timezone=America/Chicago` — every scheduled **and draft** post.
2. Collect the dates that already hold an HU post.
3. Starting tomorrow, walk forward **Mon–Fri only**; return the first date not in the set.
4. That date goes in the Slack message so a human can find the posts quickly.

**Posts go at 06:00 America/Chicago.** ⚠️ QDE's file 10 says 09:00. Bart's standing rule is 6:00 AM CST — it protects first-24h views and consistency. **06:00 wins for HU.**

⚠️ **Known defect — do not share this sub-workflow between lanes until it is fixed.** QDE runs 308 and 314 both landed on 2026-11-04 09:00, leaving nine drafts on one day: it did not skip a date that already held drafts. Give HU its own instance, or make the existing one brand-aware, and prove the skip works before relying on it.

## `Verify + collect`

`getScheduledPosts` for the date. Assert, for each of the four: it exists, `draft: true`, the correct `type`, **`blogId 6267975`**, its own distinct caption, `HandwritingUniversity.com` present, no "link in bio", and `media` now a `static.metricool.com` URL.

⛔ **Never accept the node's own `executionStatus` as proof.** `Metricool: create draft` continues on error, so it reports success while the API returned 400 and created nothing. Confirm at Metricool's API or not at all.

⚠️ **A failed `createScheduledPost` leaves nothing behind** — there is no partial draft in the planner. If a whole network set fails at once, suspect the media file: a landscape master breaks Instagram (aspect), Facebook (500 MB) and TikTok at the same time.

⚠️ **`updateScheduledPost` reissues the post id.** Same uuid, new id, old id gone. Re-read after any update; never reuse the pre-update id.

## Media
**Hand Metricool the Google Drive URL.** It uploads Drive files into its own storage, provided Drive is linked in the Metricool account (open flag in file 00). A `Failed to normalize media` error means the file is owner-only to an editor's account and Metricool's fetch got Google's HTML interstitial — **fix the Drive sharing.** The FTP bridge is retired from this lane.

## Dedup
For scheduling decisions, dedup against the **live calendar** (`getScheduledPosts`), not the MASTER sheet's columns — the sheet lags.

## Master sheet
⛔ **No writes.** See file 00. QDE's file 10 still says columns AM–AP are available to n8n; that is stale and superseded.

## Flags
`FB_POST_OVER_CAP` · `NO_VERTICAL` · `MEDIA_NOT_NORMALIZED` · `WRONG_BLOGID` (hard stop) · `DRAFT_NOT_CREATED`
