# QDE Video Pipeline — 00 OVERVIEW
**V4 · 2026-09-17 · Lane: Handwriting Experts Inc. / QDE only · Supersedes `00_OVERVIEW_V3.md`**

This folder replaces the single pipeline document. **One file per step, one n8n node group per file.** When an outcome is consistently wrong, the file with that number is the only thing to edit. Each file versions in its own filename; bump the file you changed, nothing else.

## WHAT CHANGED IN V4

**Every Google Sheets write node on this workflow is now fully compliant with the AO/AP-only rule.** *(2026-09-17, same day as V3.)* The three nodes V3 flagged as still open are fixed:

| Node | Before | Now |
|---|---|---|
| `Mark STAGED` | Wrote `status`, `Title`, `Brand`, `Duration`, `Thumbnail`, `Captions/VTT`, `Description+Title`, `YouTube URL`, `YouTube Status`, `YT Publish Date`, `TikTok`, `Instagram`, `Facebook`, `Metricool Status`, `Status / Editing Notes` — nearly every curated column | Writes only `status` (AP) and `Metricool Status` (AO) |
| `Mark ERROR — Descript failed` | Wrote `status` (AP) + `Status / Editing Notes` (AJ) | Writes only `status: "ERROR"` (AP) |
| `Mark ERROR — package incomplete` | Wrote `status` (AP) + `Status / Editing Notes` (AJ) | Writes only `status: "ERROR"` (AP) |

All three also had `VID_ID` removed from their value maps — it remains a `matchingColumns` lookup key only, used to find the row, never written back. The failure detail that used to go into `Status / Editing Notes` on the two error nodes is still communicated — it's in the Slack message each error branch sends, just no longer written to the sheet.

**Status as of V4: every write this pipeline makes to the Workflow tab of the master spreadsheet is limited to columns AO (`Metricool Status`) and AP (`status`). Nothing else on that sheet is touched by any node, and no node creates a row.** The write-boundary work started in V2 and extended in V3 is complete.

## History — kept for context

**V3 (2026-09-17):** added the row-must-exist gate. `Create queue row` converted from `appendOrUpdate` (which silently created new rows) to a read-only `Get Row(s)` lookup on VID_ID. New `Row exists?` IF node added right after it — true continues to `Media facts` unchanged; false routes to new `Slack: no matching row`, which notifies a human and stops the run before anything else executes. `Write copy to row` reduced to writing nothing; `Update Metricool row` reduced to writing only `Metricool Status`.

**V2 (2026-09-17):** root cause identified — `Config.queue_sheet_id` pointed at the live master spreadsheet (Workflow tab) instead of a dedicated `QDE_Video_Queue` sheet that was never created, and a write node was corrupting the dropdown-validated `Captions/VTT` (col V) and `Description+Title` (col W) cells as a result. Established the governing rule: only AO and AP are writable on that sheet.

**The governing rule (unchanged since V2, now fully enforced as of V4):**

```
⛔ NO node in this pipeline writes to the Workflow tab of the master spreadsheet
  (1EO2ZdAEiVHJ9FVz5ZHY-9f0CjjngHkpMVa84nHCFpDA), columns A through AL, and NO node
  ever creates a new row there. That range — including column A, VID_ID — is curated
  content owned by humans/editors. A human starts every row; this pipeline never does.
✦ The ONLY columns on that tab this pipeline may write are the two status columns
  appended after the original 40: AO ("Metricool Status") and AP ("status", lowercase).
✦ VID_ID / column A is read-only everywhere in this pipeline — used only as a
  matchingColumns lookup key to find an existing row, never written back, never
  used to create one.
✦ If no row exists for a video, the pipeline stops immediately (the Row exists?
  gate, step 2) and notifies a human. It does not proceed to any other step.
✦ Every per-video field this pipeline generates — title, description, captions,
  VTT link, thumbnail URL, etc. — belongs in QDE_Video_Queue once it exists. It is
  never back-filled into the Workflow tab's named columns, no matter how convenient
  that seems mid-build.
```

**Action item, still open:** `queue_sheet_id` in the Config node must eventually point at a real `QDE_Video_Queue` sheet — see the flagged line in the Config block below. Until it does, the Workflow tab is read for VID_ID lookups and written only on AO/AP, per the rule above.

## The model (carried from the QDE daily-post workflow, proven 2026-09-12 → 14)

1. **A sheet row is the state machine.** `QDE_Video_Queue` (tab `videos`) — one row per video. n8n reads it, agents never do.
2. **Four statuses, uppercase, case-sensitive filter:** `READY` · `STAGED` · `PUBLISHED` · `ERROR`. Plus two worker states only the Mac touches: `NEEDS_CUT` · `NEEDS_COMPRESS`. Nothing else. `HOLD` is a human note in `notes`, not a status.
3. **Repair or flag, never block.** Every check either fixes the input or writes a flag to `notes` and the Slack notice. The only halts are broken inputs (file 11) — and a missing sheet row (see V3 history above).
4. **Two human touchpoints, unchanged from V14 — plus the row-must-exist gate added in V3:** (a) a human creates the video's row in the Workflow tab; (b) someone drops the file in the Ready-to-Publish folder; (c) the reviewer clears Gate 7, makes the YouTube video public and schedules the Metricool drafts. Nothing in between asks a human anything.
5. **GitHub is authority and n8n enforces it:** every prompt is fetched from `raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/...` at run time. No local copies exist to drift.
6. **Brand facts live in `brands/qde-brand.md` only.** No file in this folder restates a domain, phone, palette or credential.

## Row schema — `QDE_Video_Queue` / `videos`

`vid_id · brand · drive_file_id · drive_file_name · status · width · height · duration_s · bytes · long_url · vertical_url · vertical_file_id · title · description · tiktok_caption · ig_caption · fb_long · fb_short · thumbnail_url · thumbnail_prompt · youtube_id · yt_playlist · metricool_tt_id · metricool_ig_id · metricool_fb_post_id · metricool_fb_reel_id · publish_date · clickup_task_id · to_verify · notes · feedback_thumbnail · feedback_description · feedback_captions · staged_at`

Headers are the JSON keys n8n uses — **one word, no spaces, no parenthetical instructions in the header cell** (2026-09-14 lesson: a descriptive header made column S read as empty). Instructions go in cell notes.

## Which file governs which n8n node

| File | n8n node(s) in `Betty — QDE Video Publish` |
|---|---|
| 01 | `Drive trigger (QDE Ready)` · `Create queue row` (read-only lookup) · `Row exists?` · `Slack: no matching row` · `ClickUp lookup` |
| 02 | `Drive: file metadata` · `Media facts` (Code) |
| 03 | `VTT: fetch` · `VTT: clean` (LLM) |
| 04 | `Copy: title` (LLM) |
| 05 | `Copy: description` (LLM) |
| 06 | `Copy: captions` (LLM) |
| 07 | `Thumbnail: prompt` · `OpenAI — thumbnail` · `Upload thumbnail` |
| 08 | `Needs ffmpeg?` (IF) · Mac worker (outside n8n) |
| 09 | `YouTube: upload` · `YouTube: thumbnail` · `YouTube: captions` |
| 10 | `Next open slot` (sub-workflow) · `Metricool ×4` · `Update Metricool row` (AO-only) |
| 11 | `Preflight` (Code) |
| 12 | `Verify` · `Mark STAGED` (AO/AP-only) · `Slack: reviewer` · `Ledger append` |
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
                        node 2026-09-17 and is the root cause of the V/W corruption fixed
                        in V2. It currently still points there for VID_ID lookups and the
                        AO/AP status writes described above — that is the accepted interim
                        state, not an error, as long as nothing else on that sheet is touched.
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
