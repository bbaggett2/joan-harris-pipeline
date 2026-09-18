# QDE Video Pipeline — 00 OVERVIEW
**V5 · 2026-09-18 · Lane: Handwriting Experts Inc. / QDE only · Supersedes `00_OVERVIEW_V4.md`**

This folder replaces the single pipeline document. **One file per step, one n8n node group per file.** When an outcome is consistently wrong, the file with that number is the only thing to edit. Each file versions in its own filename; bump the file you changed, nothing else.

## WHAT CHANGED IN V5 — YouTube upload moved off n8n Cloud entirely

**HARD RULE, confirmed by Bart 2026-09-18: YouTube video upload, thumbnail-set, and caption-insert never run inside n8n Cloud. They run locally, via the `yutu` CLI, on the Mac Studio — which must stay powered on for this pipeline to work.** This is not a preference; running an 870MB+ 4K video through n8n Cloud's Starter-plan memory allocation (320MB, per n8n's own published limits) crashed with out-of-memory errors on every attempt, regardless of file-size optimizations. The Mac has no such ceiling.

This supersedes the split done earlier the same day (V4's `Betty — QDE YouTube Publish v1` sub-workflow) — that sub-workflow still exists and is still what the main pipeline calls, but its *internal* mechanism changed:

**Old (V4, removed):** `Drive: download long` → `YouTube: upload` → `Wait for processing` → `Reattach PNG` → `YouTube: thumbnail` → `Reattach VTT` → `YouTube: captions`, all as HTTP Request nodes running inside n8n Cloud. These nodes are disabled and kept for history, not deleted.

**New (V5):** after `Share thumbnail`, the sub-workflow:
1. **`Build YouTube job`** — assembles a job description (vid_id, Drive file IDs for the video/thumbnail/VTT, title, description, and `$execution.resumeUrl`) and turns it into a small JSON file.
2. **`Write YouTube job`** — uploads that JSON file to a dedicated Drive folder: `youtube_upload_queue/` (id `1rm7hEFT0p9cd5H-bYMH--kNM-3PBk0Vn`), a subfolder of the QDE assets folder (`assets_folder_id`).
3. **`Wait for local YouTube worker`** — an n8n Wait node, `resume: webhook`. The execution pauses here — no timeout is currently configured, so a dead worker means a job waits indefinitely; see Action Items below.
4. A persistent process on the Mac Studio — launchd job **`com.betty.youtube-worker`**, script at `~/betty/youtube_worker/worker.py`, polling the queue folder every 30 seconds — picks up the job, downloads the video/thumbnail/VTT via `rclone`, uploads to YouTube via `yutu` (private, matching Gate 7), sets the thumbnail, deletes YouTube's auto-generated ASR caption track and inserts the real one, then **POSTs the result to the job's `resume_webhook_url`**, which resumes the waiting n8n execution.
5. **`Parse worker result`** → **`Worker succeeded?`** — on success, continues to `YT Result` exactly as before (same shape: `youtube_id`, `youtube_thumbnail_set`, `youtube_captions_set`). On failure, **`Slack: local upload failed`** / **`Notify: local upload failed`** fire instead, and the job file moves to `youtube_upload_queue/failed/`. Successful jobs move to `youtube_upload_queue/done/`.

**Known gotchas the worker script (`worker.py`) already handles, discovered the hard way on 2026-09-18 — do not re-debug these if they recur, just confirm the script still does this:**
- `yutu video insert` requires **base64-encoded** credentials in `YUTU_CREDENTIAL`/`YUTU_CACHE_TOKEN` — file paths fail with a misleading `illegal base64 data` error, even though every other `yutu` command accepts a file path fine. This looks like a real bug specific to that one subcommand in yutu v0.10.8.
- `yutu caption insert`/`delete` are themselves broken in this yutu version — both silently fail with `invalidMetadata` no matter what's passed. The worker calls the YouTube Data API directly instead (see the script's `insert_captions`/`delete_existing_captions` functions).
- YouTube auto-generates an ASR caption track in the same language immediately after upload. Inserting a real track in that same language conflicts with it — the existing track must be deleted first.
- The captions API's delete/update endpoints take the caption ID as a **query parameter** (`?id=...`), not a URL path segment. Path-segment delete calls return a bare 404 with no other explanation.
- Some VTT files use `MM:SS.mmm` timestamps with no hours field. Technically valid VTT, but not reliably accepted everywhere — the worker normalizes to `HH:MM:SS.mmm` before inserting.
- `YUTU_ROOT` (defaults to CWD) rejects absolute file paths that "escape" it — the worker always `cd`s into the job's working directory first and uses relative paths.

**Action items, still open:**
- The Wait node has no timeout configured. If the Mac is off or the worker is down, a job waits forever with no alert. Add a time-limit branch (Wait node supports combining webhook-resume with a fallback time limit) that fires a Slack/ntfy alert if no callback arrives within, say, 30 minutes.
- No dead-man's-switch on the worker itself. `launchd` will restart it if the *process* dies (`KeepAlive: true`), but nothing currently alerts if the Mac itself is powered off or asleep for an extended period. Consider a daily "worker heartbeat" check from n8n (a scheduled ping to a job the worker is expected to pick up promptly).
- The queue is a flat Drive folder scanned by filename pattern (`*.json`). Fine at current volume; would need real locking/claiming if two runs could ever race for the same job (they can't currently, since VID_ID is unique per job file).

## History — kept for context

**V4 (2026-09-18):** `Mark STAGED` and both `Mark ERROR` nodes stripped to AO/AP-only, closing out the write-boundary work started in V2/V3.

**V3 (2026-09-17):** row-must-exist gate added — `Create queue row` converted to a read-only lookup, `Row exists?` stops the pipeline before anything else if no matching sheet row exists.

**V2 (2026-09-17):** root cause identified — a write node was corrupting dropdown-validated `Captions/VTT` (col V) and `Description+Title` (col W) on the master sheet. Established the AO/AP-only write rule, still in force and unaffected by this V5 change (the YouTube worker never touches the master sheet at all — it only reads/writes Drive files and calls the resume webhook).

**The governing sheet-write rule (unchanged since V2):**

```
⛔ NO node in this pipeline writes to the Workflow tab of the master spreadsheet
  (1EO2ZdAEiVHJ9FVz5ZHY-9f0CjjngHkpMVa84nHCFpDA), columns A through AL, and NO node
  ever creates a new row there. A human starts every row; this pipeline never does.
✦ The ONLY columns on that tab this pipeline may write are AO ("Metricool Status")
  and AP ("status", lowercase). VID_ID is read-only everywhere — a matchingColumns
  lookup key only, never written back, never used to create a row.
```

## The model (carried from the QDE daily-post workflow, proven 2026-09-12 → 14)

1. **A sheet row is the state machine.** `QDE_Video_Queue` (tab `videos`) — one row per video. n8n reads it, agents never do. *(Still not created — see the Config block below; the pipeline currently reads/writes the master Workflow tab under the AO/AP-only rule instead.)*
2. **Four statuses, uppercase, case-sensitive filter:** `READY` · `STAGED` · `PUBLISHED` · `ERROR`. `HOLD` is a human note in `notes`, not a status.
3. **Repair or flag, never block.** The only halts are broken inputs, a missing sheet row (V3), and now a failed local YouTube upload (V5) — each with its own Slack + ntfy alert.
4. **Human touchpoints:** (a) a human creates the video's row in the Workflow tab; (b) someone drops the file in the Ready-to-Publish folder; (c) the reviewer clears Gate 7, makes the YouTube video public, and schedules the Metricool drafts. Nothing in between asks a human anything — except that **the Mac Studio must be on and the youtube-worker launchd job running**, or nothing ever finishes.
5. **GitHub is authority and n8n enforces it:** every prompt is fetched from `raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/...` at run time.
6. **Brand facts live in `peggy-olson-copywriting/BART_BAGGETT_VOICE.MD` and the description prompt files.** No file in this folder restates a domain, phone, palette, or credential.

## Row schema — `QDE_Video_Queue` / `videos` (aspirational — sheet not yet created)

`vid_id · brand · drive_file_id · drive_file_name · status · width · height · duration_s · bytes · long_url · vertical_url · vertical_file_id · title · description · tiktok_caption · ig_caption · fb_long · fb_short · thumbnail_url · thumbnail_prompt · youtube_id · yt_playlist · metricool_tt_id · metricool_ig_id · metricool_fb_post_id · metricool_fb_reel_id · publish_date · clickup_task_id · to_verify · notes · feedback_thumbnail · feedback_description · feedback_captions · staged_at`

## Which file governs which n8n node

| File | n8n node(s) in `Betty — QDE Video Publish` |
|---|---|
| 01 | `Drive trigger (QDE Ready)` · `Create queue row` (read-only lookup) · `Row exists?` · `Slack: no matching row` · `ClickUp lookup` |
| 02 | `Drive: file metadata` · `Media facts` (Code) |
| 03 | `VTT: fetch` · `VTT: clean` (LLM) |
| 04 | `Copy: title` (LLM) |
| 05 | `Copy: description` (LLM) |
| 06 | `Copy: captions` (LLM) |
| 07 | `Thumbnail: prompt` · `OpenAI — thumbnail` · `Upload thumbnail` · **`Build YouTube job` · `Write YouTube job` · `Wait for local YouTube worker` · `Parse worker result` (V5, local yutu upload — see WHAT CHANGED IN V5)** |
| 08 | *(retired — ffmpeg/vertical-cut worker; the YouTube-upload worker introduced in V5 is a separate, newer Mac process, `com.betty.youtube-worker`, not this one)* |
| 09 | *(superseded by V5's local worker — see file 07 row)* |
| 10 | `Next open slot` (sub-workflow) · `Metricool ×4` · `Update Metricool row` (AO-only) |
| 11 | `Preflight` (Code) |
| 12 | `Verify` · `Mark STAGED` (AO/AP-only) · `Slack: reviewer` · `Ledger append` · `Slack: Production Complete` |
| 13 | Three form-trigger workflows |

## Runtime split

**n8n Cloud runs everything except the final video-file-heavy steps.** The Mac Studio runs **two** persistent processes now: the original ffmpeg/vertical-cut poller (file 08, if still in use) and, as of V5, `com.betty.youtube-worker` — the YouTube upload/thumbnail/caption worker described above. Both require the Mac to be on.

## Config node (values, not rules)

```
qde_ready_folder_id   : 132glSPYurgEtU1ZkNqSlA5W6NOmK5Vx0   ("4 Ready to Publish QDE Brand")
assets_folder_id      : 1V-piQzAW8iOYn_AesxkDzK4lcWLXUYvY   ("5 QDE Pipeline Assets" — confirmed live value;
                        the folder VID copy packages, thumbnails, and VTTs already live in)
youtube_upload_queue  : 1rm7hEFT0p9cd5H-bYMH--kNM-3PBk0Vn   (subfolder of assets_folder_id, added V5;
                        subfolders done/ and failed/ exist for processed jobs)
queue_sheet_id        : 1EO2ZdAEiVHJ9FVz5ZHY-9f0CjjngHkpMVa84nHCFpDA (the master Workflow sheet;
                        read for VID_ID lookups, written only on AO/AP — see the governing rule above.
                        A dedicated QDE_Video_Queue sheet is still not created.)
metricool_blogId      : 6268508      metricool_userId : 4831552     timezone : America/Chicago
youtube_channel_id    : UCrpyI5SkE075HJaFyxO_ozQ   ("@TheHandwritingExpert" — verify the QDE youtube
                        account credential is authorized against THIS channel, not another Baggett
                        brand; this credential was found mis-authorized once, 2026-09-18)
slack_channel         : #qde-celebrity-post-review
prompt_base_url       : https://raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/
image_model           : gpt-image-1     text_model : gpt-4.1
facebook_cap_bytes    : 524288000
ntfy_topic            : qde-pipeline-bhi-x7f2k9   (desktop-popup notifications, added 2026-09-18;
                        see qde-pipeline-status.html — not in this repo, distributed separately)
```

## The local YouTube worker — operational notes

**Location:** `~/betty/youtube_worker/worker.py` on the Mac Studio. **Launchd job:** `com.betty.youtube-worker`, plist at `~/Library/LaunchAgents/com.betty.youtube-worker.plist`, `KeepAlive: true` (restarts on crash), `RunAtLoad: true` (starts on login/reboot). **Logs:** `~/betty/youtube_worker/worker.log` (structured `OK:`/`FAIL:` lines per job, matching the Desktop Commander long-job convention), plus raw `stdout.log`/`stderr.log`.

**To check it's running:** `launchctl list | grep betty`. **To restart after editing the script:** `launchctl unload` then `launchctl load` the plist. **If the Mac restarts,** the job starts itself automatically (`RunAtLoad`) — no manual step needed, but the Mac itself must be powered on.

## Gate 7 is still human

Legal accuracy is checked by the reviewer before making the video public. n8n surfaces every `[TO VERIFY]` as the first line of the Slack notice (file 12). No machine clears it.
