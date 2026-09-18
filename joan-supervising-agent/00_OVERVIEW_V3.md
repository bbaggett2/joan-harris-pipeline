# QDE Video Pipeline — 00 OVERVIEW
**V3 · 2026-09-17 · Lane: Handwriting Experts Inc. / QDE only · Supersedes `00_OVERVIEW_V2.md`**

This folder replaces the single pipeline document. **One file per step, one n8n node group per file.** When an outcome is consistently wrong, the file with that number is the only thing to edit. Each file versions in its own filename; bump the file you changed, nothing else.

## WHAT CHANGED IN V3

**New hard rule: this pipeline never writes to column A (VID_ID) on the Workflow tab, and never creates a new row there, under any circumstance.** *(Bart/Joan, 2026-09-17.)* Previously `Create queue row` used `appendOrUpdate` — if a video's VID_ID didn't match an existing row, it silently created one. That is gone. A row must already exist, put there by a human, before this pipeline will touch a video at all.

**The verification gate runs second in the workflow — right after `Config`, before anything else:**

1. **`Create queue row`** (name kept unchanged so existing expression references still resolve) is now a **read-only** `Get Row(s)` lookup filtered on VID_ID, extracted from the Drive file name by regex. `alwaysOutputData: true` so a not-found result still passes one item through instead of silently dead-ending.
2. **`Row exists?`** (new IF node) checks whether the lookup returned a `VID_ID`.
   - **True** → continues into `Media facts` exactly as before. Nothing else in the pipeline changed.
   - **False** → **`Slack: no matching row`** (new node) notifies `#qde-celebrity-post-review` with the file name and the VID_ID candidate it tried to match, states plainly that this pipeline never creates rows, and asks a human to add one. **Nothing else runs** — no Media facts, no Descript import, no copy generation. The run stops before doing anything else, by design.

**Other write-boundary hardening done the same day, on top of V2's AO/AP-only rule:**

- **`Write copy to row`** now writes **nothing**. `Title`, `Transcript`, `Description+Title`, `Captions/VTT`, and `Status / Editing Notes` were all removed from its column map, and `VID_ID` was removed too (it remains only as the read-only `matchingColumns` lookup key — matching a row to update is not the same as writing to it, and is never written back). This node is effectively a no-op until the pipeline has a real `QDE_Video_Queue` to write per-video fields into.
- **`Update Metricool row`** now writes **only `Metricool Status` (col AO)**. `VID_ID`, `Instagram`, `TikTok`, and `Facebook` were all removed from its column map; `VID_ID` remains lookup-only, same as above.

⚠️ **STILL OPEN — NOT YET FIXED, flagging so it isn't mistaken for compliant:** three more Google Sheets nodes on this workflow still write outside the AO/AP boundary and have not been corrected yet:

| Node | Writes today (non-compliant) |
|---|---|
| `Mark STAGED` | `status`, `Title`, `Brand`, `Duration`, `Thumbnail`, `Captions/VTT`, `Description+Title`, `YouTube URL`, `YouTube Status`, `YT Publish Date`, `TikTok`, `Instagram`, `Facebook`, `Metricool Status`, `Status / Editing Notes` — nearly every curated column on the sheet, in one write |
| `Mark ERROR — Descript failed` | `status` (AP, fine) **+** `Status / Editing Notes` (AJ, no longer permitted) |
| `Mark ERROR — package incomplete` | `status` (AP, fine) **+** `Status / Editing Notes` (AJ, no longer permitted) |

All three need the same treatment as `Write copy to row` / `Update Metricool row` — strip every field except `Metricool Status` (AO) and `status` (AP) — before this pipeline is fully compliant with the rule below. Do not treat this pipeline as finished on the write-boundary work until these three are fixed too.

**The governing rule (from V2, unchanged and now extended to cover row creation):**

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
3. **Repair or flag, never block.** Every check either fixes the input or writes a flag to `notes` and the Slack notice. The only halts are broken inputs (file 11) — **and, as of V3, a missing sheet row (see WHAT CHANGED IN V3).**
4. **Two human touchpoints, unchanged from V14 — plus the row-must-exist gate added in V3:** (a) a human creates the video's row in the Workflow tab; (b) someone drops the file in the Ready-to-Publish folder; (c) the reviewer clears Gate 7, makes the YouTube video public and schedules the Metricool drafts. Nothing in between asks a human anything.
5. **GitHub is authority and n8n enforces it:** every prompt is fetched from `raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/...` at run time. No local copies exist to drift.
6. **Brand facts live in `brands/qde-brand.md` only.** No file in this folder restates a domain, phone, palette or credential.

## Row schema — `QDE_Video_Queue` / `videos`

`vid_id · brand · drive_file_id · drive_file_name · status · width · height · duration_s · bytes · long_url · vertical_url · vertical_file_id · title · description · tiktok_caption · ig_caption · fb_long · fb_short · thumbnail_url · thumbnail_prompt · youtube_id · yt_playlist · metricool_tt_id · metricool_ig_id · metricool_fb_post_id · metricool_fb_reel_id · publish_date · clickup_task_id · to_verify · notes · feedback_thumbnail · feedback_description · feedback_captions · staged_at`

Headers are the JSON keys n8n uses — **one word, no spaces, no parenthetical instructions in the header cell** (2026-09-14 lesson: a descriptive header made column S read as empty). Instructions go in cell notes.

## Which file governs which n8n node

| File | n8n node(s) in `Betty — QDE Video Publish` |
|---|---|
| 01 | `Drive trigger (QDE Ready)` · `Create queue row` (read-only lookup, V3) · `Row exists?` (V3) · `Slack: no matching row` (V3) · `ClickUp lookup` |
| 02 | `Drive: file metadata` · `Media facts` (Code) |
| 03 | `VTT: fetch` · `VTT: clean` (LLM) |
| 04 | `Copy: title` (LLM) |
| 05 | `Copy: description` (LLM) |
| 06 | `Copy: captions` (LLM) |
| 07 | `Thumbnail: prompt` · `OpenAI — thumbnail` · `Upload thumbnail` |
| 08 | `Needs ffmpeg?` (IF) · Mac worker (outside n8n) |
| 09 | `YouTube: upload` · `YouTube: thumbnail` · `YouTube: captions` |
| 10 | `Next open slot` (sub-workflow) · `Metricool ×4` · `Update Metricool row` (AO-only, V3) |
| 11 | `Preflight` (Code) |
| 12 | `Verify` · `Mark STAGED` ⚠️ still non-compliant, see WHAT CHANGED IN V3 · `Slack: reviewer` · `Ledger append` |
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
