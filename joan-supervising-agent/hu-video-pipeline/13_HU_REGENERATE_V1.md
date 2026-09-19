# 13 — HU Regenerate
**V1 · 2026-09-19 · Governs: three form-trigger workflows**

## Rule
A reviewer who does not like a thumbnail, a description, or the captions re-runs **that phase alone** against the already-uploaded private video. That is a redo, not a failure, and it never re-uploads the video.

## The three forms
Each is its own n8n form-trigger workflow, linked from the reviewer's Slack message (file 12).

| Form | Re-runs | Replaces on the live video |
|---|---|---|
| Regenerate thumbnail | file 07 | the thumbnail only |
| Regenerate description | files 05 + 11 | title and description only |
| Regenerate captions | files 03 + 09 caption step | the caption track only |

## Mechanics

⚠️ **The n8n form trigger's field name is `field-0`, not the display label.** A POST with the wrong key yields `null` — and the run still reports **success** after doing nothing. This is the same class of silent pass as the `yutu` absolute-path bug; assert the field is non-empty before acting on it. Confirmed again on a live QDE run, 2026-09-19.

- Input is the `vid_id`. Resolve the current YouTube ID from the ledger, **not** from channel recency — Bart deletes and re-uploads, so the newest video on the channel is not reliably the one you want.
- ⛔ **Never re-upload the video.** These forms touch metadata and assets only.
- ⛔ **Never create new Metricool drafts** from a regenerate run. If the copy changed and drafts already exist, update them — and remember `updateScheduledPost` reissues the post id (file 10), so re-read afterwards and never reuse the pre-update id.
- Thumbnail regeneration writes `<VID_ID>_thumb_v<n>.png` with the **next** `n`. Never another `v1`. Bart reviews variations side by side, so the numbering is the point.
- Every regenerate run reports back through file 12's notification, with the same destination reads. A regenerated thumbnail that did not actually land is exactly the failure mode this pipeline already had.

## Duplicate-upload guard
⛔ **Never auto-upload a cut that is already published.** Re-resolve the current video ID before acting. The upload ledger's key is `VID_ID|drive_file_id`, which a rename defeats — see file 09.
