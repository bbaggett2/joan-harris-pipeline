# QDE Video Pipeline — 00 OVERVIEW
**V6 · 2026-09-19 · Lane: Handwriting Experts Inc. / QDE only · Supersedes `00_OVERVIEW_V5.md`**

This folder replaces the single pipeline document. **One file per step, one n8n node group per file.** When an outcome is consistently wrong, the file with that number is the only thing to edit. Each file versions in its own filename; bump the file you changed, nothing else.

## WHAT CHANGED IN V6 — n8n never writes to the master worksheet, period

**HARD RULE, set by Bart/Joan 2026-09-19: n8n has NO write access to the master Workflow spreadsheet at all — not the Workflow tab, not any other tab in that file, nothing.** This replaces and is stricter than the V2–V5 rule, which still allowed two columns (AO "Metricool Status", AP "status"). That carve-out is gone. The reason: "I don't want any accidental write overs" — even a two-column exception was more surface area than wanted.

**What this actually changed, node by node (all in `Betty — QDE Video Publish v1`):**

| Node | Was | Now |
|---|---|---|
| `Mark STAGED` | Wrote AO/AP on success | **Disabled.** `Verify + collect` → `Slack: reviewer` directly. |
| `Mark ERROR — Descript failed` | Wrote AP = ERROR | **Disabled.** `Descript: job done?` (both error outputs) → `Slack: Descript failed` / `Notify: Descript failed` directly. |
| `Mark ERROR — package incomplete` | Wrote AP = ERROR | **Disabled.** `Package complete?` (error output) → `Slack: package incomplete` / `Notify: package incomplete` directly. |
| `Update Metricool row` | Wrote AO = Metricool Status | **Disabled.** `Build Metricool row update` now has no downstream node — its output is simply not used for a sheet write anymore. |
| `Write copy to row` | Wrote V/W (already disabled since V2) | Unchanged — still disabled. |
| `Ledger append` | Appended a row to a separate **"n8n ledger" tab** in the same spreadsheet file | **Disabled, then the tab itself was deleted 2026-09-19** ("never really worked as planned"). `Slack: reviewer` → `Slack: Production Complete` / `Notify: Production Complete` directly. |
| `Ledger: Metricool success` | Appended to the same "n8n ledger" tab | **Disabled** along with the tab. `Update Metricool row`'s old connection to it removed entirely. |

**What's left with any relationship to this spreadsheet — both read-only, both unchanged:** `Create queue row` (VID_ID lookup, filtersUI-based, no write operation available to it) and `Get sheet row (Metricool)` (same). Verified directly against every node in all four workflows (`Betty — QDE Video Publish v1`, `Betty — QDE YouTube Publish v1`, `Betty — QDE Metricool Drafts v1`, `Betty — QDE Error Handler v1`) — zero nodes with a live `update`/`append`/`appendOrUpdate`/`delete`/`clear` operation against this document remain enabled anywhere in the pipeline.

**What this means in practice:** the pipeline no longer records STAGED/ERROR status, Metricool status, or a run ledger anywhere durable on its own. The only record of a run's outcome is now the Slack/ntfy notifications at the time it happens — there is no queryable "what happened to VID-XXXX" state left in a spreadsheet or ledger. If that's ever needed again, it has to be a deliberate new decision, not a default assumption — don't quietly re-add a sheet write to "fix" this without checking first, since removing that surface area was the explicit point.

**No action needed on the tab deletion itself** — every node that used to write to "n8n ledger" was already fully disconnected before the tab was deleted, so nothing in the pipeline references it and nothing broke.

## History — kept for context

**V5 (2026-09-18):** YouTube video upload, thumbnail-set, and caption-insert moved off n8n Cloud entirely to a local `yutu`-based worker on the Mac Studio (`com.betty.youtube-worker`). See `00_OVERVIEW_V5.md` for the full local-worker architecture (Drive job queue, resume-webhook design) — unchanged and unaffected by V6; the worker never touched the master sheet in the first place.

**V4 (2026-09-18):** `Mark STAGED` and both `Mark ERROR` nodes stripped to AO/AP-only writes, closing out the write-boundary work started in V2/V3. **Superseded by V6** — those same nodes are now disabled entirely rather than restricted.

**V3 (2026-09-17):** row-must-exist gate added — `Create queue row` converted to a read-only lookup, `Row exists?` stops the pipeline before anything else if no matching sheet row exists. Still in force, unaffected by V6.

**V2 (2026-09-17):** root cause identified — a write node was corrupting dropdown-validated `Captions/VTT` (col V) and `Description+Title` (col W) on the master sheet. Established the original AO/AP-only write rule. **Superseded by V6.**

**The governing sheet-write rule, current as of V6:**

```
⛔ n8n has NO write access to the master Workflow spreadsheet
  (1EO2ZdAEiVHJ9FVz5ZHY-9f0CjjngHkpMVa84nHCFpDA) — not the Workflow tab, not any
  other tab, nothing. Every former write node (Mark STAGED, both Mark ERROR
  nodes, Update Metricool row, Write copy to row, both Ledger nodes) is disabled
  and disconnected. The "n8n ledger" tab this file used to write to no longer
  exists.
✦ The ONLY sheet operations this pipeline performs are read-only lookups:
  Create queue row (VID_ID match) and Get sheet row (Metricool). Neither has
  any write capability configured.
✦ A human maintains every column in this sheet by hand now, including what
  V2–V5 called the AO/AP columns. The pipeline reports outcomes via Slack/ntfy
  only — there is no automated record in the sheet of what the pipeline did.
```

## The model (carried from the QDE daily-post workflow, proven 2026-09-12 → 14)

1. **A sheet row is the state machine, read-only.** `QDE_Video_Queue` (tab `videos`) was the original aspiration — never created. The pipeline currently reads the master Workflow tab for VID_ID lookups only, per the rule above; it does not write status back anywhere.
2. **Four statuses, uppercase, case-sensitive filter:** `READY` · `STAGED` · `PUBLISHED` · `ERROR` — these remain the conceptual states a human tracks by hand; the pipeline no longer sets any of them.
3. **Repair or flag, never block.** The only halts are broken inputs and a missing sheet row — each with its own Slack + ntfy alert, same as before. Alerting is unaffected by the write-removal; only the sheet-write side-effect is gone.
4. **Human touchpoints:** (a) a human creates the video's row in the Workflow tab; (b) someone drops the file in the Ready-to-Publish folder; (c) the reviewer clears Gate 7, makes the YouTube video public, and schedules the Metricool drafts. As of V6, a human must also now manually update the Workflow tab's status columns after each run, since the pipeline no longer does it. The Mac Studio must still be on and the youtube-worker launchd job running, per V5.
5. **GitHub is authority and n8n enforces it:** every prompt is fetched from `raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/...` at run time.
6. **Brand facts live in `peggy-olson-copywriting/BART_BAGGETT_VOICE.MD`, the description prompt files, and now `salvatore-art-department/Thumbnail_Brand_SOP_QDE_v2.md`.** No file in this folder restates a domain, phone, palette, or credential.

## Row schema — `QDE_Video_Queue` / `videos` (aspirational — sheet not yet created, and per V6 would be human-maintained even if it existed)

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
| 07 | `Thumbnail: prompt` (fetch SOP + LLM, rebuilt V2 of file 09) · `OpenAI — thumbnail` · `Upload thumbnail` · `Build YouTube job` · `Write YouTube job` · `Wait for local YouTube worker` · `Parse worker result` |
| 08 | *(retired — ffmpeg/vertical-cut worker, separate from the V5 YouTube worker)* |
| 09 | See `09_YOUTUBE_V2.md` — the deep dive on the thumbnail rebuild and every upload-chain gotcha found and fixed 2026-09-18 |
| 10 | `Next open slot` (sub-workflow) · `Metricool ×4` · `Update Metricool row` (⛔ disabled V6 — see above) |
| 11 | `Preflight` (Code) |
| 12 | `Verify` · `Mark STAGED` (⛔ disabled V6) · `Slack: reviewer` · ~~`Ledger append`~~ (⛔ disabled + tab deleted V6) · `Slack: Production Complete` |
| 13 | Three form-trigger workflows |

## Runtime split

**n8n Cloud runs everything except the final video-file-heavy steps.** The Mac Studio runs `com.betty.youtube-worker` (V5) and, if still in use, the older ffmpeg/vertical-cut poller (file 08). Both require the Mac to be on. Unaffected by V6.

## Config node (values, not rules)

```
qde_ready_folder_id   : 132glSPYurgEtU1ZkNqSlA5W6NOmK5Vx0   ("4 Ready to Publish QDE Brand")
assets_folder_id      : 1V-piQzAW8iOYn_AesxkDzK4lcWLXUYvY   ("5 QDE Pipeline Assets")
youtube_upload_queue  : 1rm7hEFT0p9cd5H-bYMH--kNM-3PBk0Vn   (subfolder of assets_folder_id;
                        subfolders done/ and failed/ exist for processed jobs)
queue_sheet_id        : 1EO2ZdAEiVHJ9FVz5ZHY-9f0CjjngHkpMVa84nHCFpDA (the master Workflow sheet;
                        READ-ONLY as of V6 — see the governing rule above. The "n8n ledger" tab
                        this file's Config once referenced no longer exists; do not re-add a
                        reference to it.)
metricool_blogId      : 6268508      metricool_userId : 4831552     timezone : America/Chicago
youtube_channel_id    : UCrpyI5SkE075HJaFyxO_ozQ   ("@TheHandwritingExpert")
slack_channel         : #qde-celebrity-post-review
prompt_base_url       : https://raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/
image_model           : gpt-image-1     text_model : gpt-4.1
facebook_cap_bytes    : 524288000
ntfy_topic            : qde-pipeline-bhi-x7f2k9
```

## The local YouTube worker — operational notes

Unchanged from V5 — see that file (or `09_YOUTUBE_V2.md` for the deeper gotcha list) for `worker.py` location, the launchd job, logs, and restart commands. V6 makes no changes to the worker; it never had sheet-write access to begin with.

## Gate 7 is still human

Legal accuracy is checked by the reviewer before making the video public. As of V6, the reviewer is also the only remaining record-keeper for the Workflow tab's status columns — the pipeline will not update them.
