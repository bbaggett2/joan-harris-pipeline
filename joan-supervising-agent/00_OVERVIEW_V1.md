# QDE Video Pipeline — 00 OVERVIEW

This version is outdated. find OVERVIEW_V2.md
**V1 · 2026-09-15 · Lane: Handwriting Experts Inc. / QDE only · Supersedes `QDE_Video_Publishing_Pipeline_V14.md`**

This folder replaces the single pipeline document. **One file per step, one n8n node group per file.** When an outcome is consistently wrong, the file with that number is the only thing to edit. Each file versions in its own filename; bump the file you changed, nothing else.

## The model (carried from the QDE daily-post workflow, proven 2026-09-12 → 14)

1. **A sheet row is the state machine.** `QDE_Video_Queue` (tab `videos`) — one row per video. n8n reads it, agents never do.
2. **Four statuses, uppercase, case-sensitive filter:** `READY` · `STAGED` · `PUBLISHED` · `ERROR`. Plus two worker states only the Mac touches: `NEEDS_CUT` · `NEEDS_COMPRESS`. Nothing else. `HOLD` is a human note in `notes`, not a status.
3. **Repair or flag, never block.** Every check either fixes the input or writes a flag to `notes` and the Slack notice. The only halts are broken inputs (file 11).
4. **Two human touchpoints, unchanged from V14:** (a) someone drops the file in the Ready-to-Publish folder; (b) the reviewer clears Gate 7, makes the YouTube video public and schedules the Metricool drafts. Nothing in between asks a human anything.
5. **GitHub is authority and n8n enforces it:** every prompt is fetched from `raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/...` at run time. No local copies exist to drift.
6. **Brand facts live in `brands/qde-brand.md` only.** No file in this folder restates a domain, phone, palette or credential.

## Row schema — `QDE_Video_Queue` / `videos`

`vid_id · brand · drive_file_id · drive_file_name · status · width · height · duration_s · bytes · long_url · vertical_url · vertical_file_id · title · description · tiktok_caption · ig_caption · fb_long · fb_short · thumbnail_url · thumbnail_prompt · youtube_id · yt_playlist · metricool_tt_id · metricool_ig_id · metricool_fb_post_id · metricool_fb_reel_id · publish_date · clickup_task_id · to_verify · notes · feedback_thumbnail · feedback_description · feedback_captions · staged_at`

Headers are the JSON keys n8n uses — **one word, no spaces, no parenthetical instructions in the header cell** (2026-09-14 lesson: a descriptive header made column S read as empty). Instructions go in cell notes.

## Which file governs which n8n node

| File | n8n node(s) in `Betty — QDE Video Publish` |
|---|---|
| 01 | `Drive trigger (QDE Ready)` · `Create queue row` · `ClickUp lookup` |
| 02 | `Drive: file metadata` · `Media facts` (Code) |
| 03 | `VTT: fetch` · `VTT: clean` (LLM) |
| 04 | `Copy: title` (LLM) |
| 05 | `Copy: description` (LLM) |
| 06 | `Copy: captions` (LLM) |
| 07 | `Thumbnail: prompt` · `OpenAI — thumbnail` · `Upload thumbnail` |
| 08 | `Needs ffmpeg?` (IF) · Mac worker (outside n8n) |
| 09 | `YouTube: upload` · `YouTube: thumbnail` · `YouTube: captions` |
| 10 | `Next open slot` (sub-workflow) · `Metricool ×4` |
| 11 | `Preflight` (Code) |
| 12 | `Verify` · `Mark STAGED` · `Slack: reviewer` · `Ledger append` |
| 13 | Three form-trigger workflows |

## Runtime split

**n8n Cloud runs everything except ffmpeg.** The Mac Studio runs one poller (file 08) that watches for `NEEDS_CUT` / `NEEDS_COMPRESS` rows, does the ffmpeg job, drops the file in Drive and sets the row back to `READY`. No yutu, no rclone, no lftp, no Desktop Commander in the main path.

## Config node (values, not rules)

```
qde_ready_folder_id   : 132glSPYurgEtU1ZkNqSlA5W6NOmK5Vx0   ("4 Ready to Publish QDE Brand", verified 2026-09-15)
hu_ready_folder_id    : 1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv   (never used by this lane; listed so no one confuses them)
queue_sheet_id        : [TO CREATE] — new sheet QDE_Video_Queue, tab `videos`, gid 0
assets_folder_id      : [TO CREATE] — Drive folder for thumbnails / vertical cuts
metricool_blogId      : 6268508      metricool_userId : 4831552     timezone : America/Chicago
youtube_channel_id    : UCrpyI5SkE075HJaFyxO_ozQ     yt_playlist_id : [TO VERIFY]
slack_channel         : qde-video-review
prompt_base_url       : https://raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/
image_model           : gpt-image-1     text_model : gpt-4.1 (first pass; swap in the HTTP node)
facebook_cap_bytes    : 524288000
```

## Gate 7 is still human

Legal accuracy is checked by the reviewer before making the video public. n8n surfaces every `[TO VERIFY]` as the first line of the Slack notice (file 12). No machine clears it.
