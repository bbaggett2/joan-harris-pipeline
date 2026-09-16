# 10 — Metricool drafts
**V1 · 2026-09-15 · Governs n8n nodes: `Next open slot` (sub-workflow) · `Assemble drafts` · `Metricool: create draft` · `Verify + collect`**

Proven nodes from `Betty — QDE Daily Social Post`, reused. `POST https://app.metricool.com/api/v2/scheduler/posts?blogId=6268508&userId=4831552`, Header Auth `Metricool X-Mc-Auth`, body `saveExternalMediaFiles: true`, **`draft: true`, always**. One call per draft. Betty never schedules.

## `Next open slot` — the shared sub-workflow (fixes the 2026-09-14 stacking bug)
Input: `blogId`. Output: `publish_date` (`yyyy-MM-dd`; posts go at 09:00 America/Chicago).
1. `GET …/scheduler/posts?blogId=…&userId=…&start=<today>&end=<today+45d>&timezone=America/Chicago` — every scheduled *and draft* post.
2. Collect the set of dates that already hold a QDE post.
3. Starting tomorrow, walk forward Mon–Fri only; return the first date not in the set.
Both the post lane and this lane call it, so the two never stack on each other. `n8n/Next_Open_Slot_subworkflow_v1.json`.

## The four drafts
| Draft | providers | networkData | media | text |
|---|---|---|---|---|
| TikTok | `tiktok` | `{title: tiktok_hook, privacyOption: "PUBLIC_TO_EVERYONE"}` | `vertical_url` | `tiktok_caption` |
| Instagram | `instagram` | `{type: "REEL", showReelOnFeed: true}` | `vertical_url` | `ig_caption` |
| FB POST | `facebook` | `{type: "POST", title: title}` | `long_url` (< 500 MB, else skipped + flag `FB_POST_OVER_CAP`) | `fb_long` |
| FB REEL | `facebook` | `{type: "REEL", title: title}` | `vertical_url` (missing → not created, flag `NO_VERTICAL`) | `fb_short` |

All four carry the same `publish_date` from the sub-workflow. `videoThumbnailUrl` is omitted. LinkedIn and GBP are not created by this workflow until "network scope" is decided (file 00).

## `Verify + collect`
`getScheduledPosts` for the date; assert each draft exists with `draft: true`, correct `type`, `blogId 6268508`, `media` now a `static.metricool.com` URL. Ids → row. A draft that fails to normalize media → flag `MEDIA_NOT_NORMALIZED` (Drive sharing is the usual cause; the FTP bridge is retired from this lane — fix sharing instead).

## Refinement hook
Which networks / captions map where → the table above. Slot rule → the sub-workflow. Copy → file 06.
