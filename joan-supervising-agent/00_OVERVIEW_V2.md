# QDE Video Pipeline — 00 OVERVIEW
**V2 · 2026-09-17 · Lane: Handwriting Experts Inc. / QDE only · Supersedes `00_OVERVIEW_V1.md`**

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
                        ⛔ MUST NOT be 1EO2ZdAEiVHJ9FVz5ZHY-9f0CjjngHkpMVa84nHCFpDA (the
                        Workflow master sheet) — that value was found live in the Config
                        node 2026-09-17 and is the root cause of the V/W corruption below.
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

## WHAT CHANGED IN V2

**The Video Production MASTER sheet's `Workflow` tab is off-limits to this pipeline.** *(Joan/Bart, 2026-09-17.)* A live n8n node was found writing generated Description+Title and Captions/VTT text into columns **W** and **V** of the `Workflow` tab — both are dropdown / data-validation cells, not free text, and the write corrupted them.

**Root cause:** the `Get sheet row` node's `Document` field read `{{ $('Config').first().json.queue_sheet_id }}` — and `Config.queue_sheet_id` was set to the live master spreadsheet ID (`1EO2ZdAEiVHJ9FVz5ZHY-9f0CjjngHkpMVa84nHCFpDA`) with `Sheet: Workflow`, because the `QDE_Video_Queue` sheet documented above was never actually created. The pipeline had nowhere compliant to write, so it wrote into the master sheet instead.

**New hard rule (supersedes any per-file note, including the one previously added to file 10):**

⛔ NO node in this pipeline writes to the Workflow tab of the master spreadsheet (`1EO2ZdAEiVHJ9FVz5ZHY-9f0CjjngHkpMVa84nHCFpDA`), columns A through AL. That range is curated, dropdown-driven content owned by humans/editors — Video Status, Stage, Captions/VTT, Description+Title, Brand, YouTube URL, platform dates, etc. Several of those columns are dropdown/data-validation cells; writing free text into them corrupts the cell.

✦ The ONLY columns on that tab this pipeline may write are the two status columns appended after the original 40: **AO** ("Metricool Status") and **AP** ("status", lowercase).

✦ Every per-video field this pipeline generates — title, description, captions, VTT link, thumbnail URL, etc. — belongs in `QDE_Video_Queue` once it exists. It is never back-filled into the Workflow tab's named columns, no matter how convenient that seems mid-build.

**Action item, still open:** `queue_sheet_id` in the Config node must be corrected to point at an actual `QDE_Video_Queue` sheet — see the flagged line in the Config block above.
