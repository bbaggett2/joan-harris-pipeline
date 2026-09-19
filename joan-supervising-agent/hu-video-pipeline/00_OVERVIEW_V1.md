# HU Video Pipeline — 00 OVERVIEW
**V1 · 2026-09-19 · Lane: Handwriting University only · Replaces `HU_Video_Publishing_Pipeline_V15.md`**

One file per step, one n8n node group per file. When an outcome is consistently wrong, the file with that number is the only thing to edit. Each file versions in its own filename; bump the file you changed, nothing else.

> **Why this replaces V15.** V15 described the HU lane as an agent-to-agent process and said so itself: *"This document does not include the n8n workflow. This process will be rewritten asap."* The QDE lane has since been built in n8n with a Mac side-car worker, and Metricool now works a specific, proven way. This set is the HU lane rewritten on that reality. V15 and the misfiled `HU_Video_Publishing_Pipeline_V14.md` are both retired by this set and should be deleted.

## Runtime split — this is the shape of the whole lane

**n8n Cloud** (`https://empresse.app.n8n.cloud`) orchestrates everything except the video-file-heavy steps. n8n Cloud has no Execute Command node, so it cannot run `ffmpeg`, `yutu` or `rclone` at all.

**The Mac Studio** runs the side-car workers. n8n writes a job file to a Google Drive queue; a launchd worker on the Mac claims it, does the work, and resumes the workflow through a wait-webhook. The Mac must be on and logged in.

⚠️ **The self-hosted n8n on the Mac (`localhost:5678`) is NOT where this runs.** It is up but holds zero workflows. Anyone looking for a workflow there will find nothing. Verified 2026-09-19.

## Hard rules inherited from the QDE lane

```
⛔ n8n has NO write access to the master Workflow spreadsheet
   (1EO2ZdAEiVHJ9FVz5ZHY-9f0CjjngHkpMVa84nHCFpDA) — not the Workflow tab, not any
   other tab, nothing. Set by Bart/Joan 2026-09-19: "I don't want any accidental
   write overs." The only sheet operations are read-only VID_ID lookups.
   ⚠️ QDE's own file 10 still says "columns AM-AP are available for n8n to write
   to" — that is stale, superseded by QDE 00_OVERVIEW_V6. Do not re-add a sheet
   write to the HU lane on the strength of it.
⛔ A step that returns cleanly has not necessarily done anything. Confirm every
   external effect by reading it back from the destination — the channel id, the
   caption status, the thumbnail, the blogId. Never from an exit code, a node's
   executionStatus, or a green tick. Three separate steps failed this way in one
   week: an n8n sub-workflow running stale code, worker.py edited but not
   restarted, and `yutu thumbnail set` printing its usage text and exiting 0.
⛔ A saved n8n change is not a live change — sub-workflows included. Deactivate,
   reactivate, then prove it from a later execution's workflowData snapshot.
✦ GitHub is authority; the Mac is where execution happens. Every prompt is
   fetched from raw.githubusercontent.com at run time. An uncommitted file is a
   blocked job, never a local fallback.
✦ Brand facts come from brands/handwriting-university.md. Never restated here.
✦ NOTHING PUBLISHES WITHOUT THE REVIEWER. YouTube stays private; Metricool posts
   stay draft:true. The reviewer is a role, never a named person.
✦ NEVER delete any file. NEVER post to the Joan Harris channel
   UCbDGkQdUKEgeDTDvqVEWoWA.
```

## The model

1. **The Ready-to-Publish folder is the trigger, the approval to start, and the brand.** One trigger per brand folder. HU has its own workflow with its own trigger — it never shares one with QDE. (Bart, 2026-09-19.)
2. **Brand is resolved once, at pickup, and carried.** Never re-inferred from the video, title, copy, or a second folder read. An unresolvable brand is an error, not a guess.
3. **Repair or flag, never block.** The only halts are broken inputs and a missing sheet row, each with its own Slack + ntfy alert.
4. **Two human touchpoints.** Someone drops the file in the folder; the reviewer makes the video public and schedules the drafts. Everything between runs agent-to-agent.
5. **Status is not recorded anywhere durable by the pipeline.** Per the no-write rule, the only record of a run is the Slack/ntfy notification at the time. A human maintains the sheet by hand.

## Config — values, not rules

```
hu_ready_folder_id    : 1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv
                        ("3. Ready to Publish - HU brand") — direct children only
                        ⭐ the trigger, the approval, and the brand signal
                        ⛔ match on folder ID, never the folder name
assets_folder_id      : [TO CREATE — "5 HU Pipeline Assets"]
youtube_upload_queue  : [TO CREATE — own queue, NOT QDE's. See file 09.]
queue_sheet_id        : 1EO2ZdAEiVHJ9FVz5ZHY-9f0CjjngHkpMVa84nHCFpDA  (READ-ONLY)
metricool_blogId      : 6267975        metricool_userId : 4831552
metricool_brand       : thehandwritinguniversity
timezone              : America/Chicago
publish_time          : 06:00 America/Chicago
                        ⚠️ QDE file 10 says 09:00. Bart's standing rule is 6:00 AM
                        CST — it protects first-24h views. 06:00 wins for HU.
youtube_channel_id    : UCG-DLule9ZSStBdc5gSEoCw   ("@handwritinguniversity")
youtube_credential    : ~/.config/betty/youtube/hu_client_secret.json
                        + hu.token.json  (GCP project yutu-handwriting-university,
                        its own ~10k/day quota — HU never starves QDE)
facebook_page_id      : 348215195822   (verified HU brand page, Bart 2026-08-18)
networks              : YouTube · TikTok · Instagram · Facebook
                        ⛔ NO LinkedIn, NO X. X @handwritingu is suspended.
slack_channel         : [TO VERIFY — needs Bart. QDE uses #qde-celebrity-post-review;
                        HU must not share it or HU failures vanish into QDE's stream.]
ntfy_topic            : [TO CREATE — must be distinct from qde-pipeline-bhi-x7f2k9]
ledger                : betty/hu_syndication_ledger.json
clickup_space         : Video Production   statuses: Open · in progress · Closed
prompt_base_url       : https://raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/
copy_prompt           : peggy-olson-copywriting/hu_description_prompt_V<n>.md
                        ⚠️ the file on main is V2 and predates the five-output
                        contract in file 05. Blocked until V3 lands.
text_model            : gpt-4.1
facebook_cap_bytes    : 524288000   (500 MB — a size cap, never a duration gate)
```

Everything not in this block — voice, palette, fonts, banned words, audience, domain — comes from `brands/handwriting-university.md`.

## Which file governs which n8n node

| File | Scope |
|---|---|
| 01 | `Drive trigger (HU Ready)` · `Create queue row` (read-only) · `Row exists?` · `ClickUp lookup` |
| 02 | `Drive: file metadata` · `Media facts` |
| 03 | `VTT: fetch` · `VTT: clean` |
| 04 | Title mechanics (content authority is Peggy's prompt) |
| 05 | Copy JSON contract |
| 06 | Caption mechanics (content authority is Peggy's prompt) |
| 07 | `Thumbnail: job` · HU thumbnail worker on the Mac |
| 08 | **Vertical 9:16 cut — LIVE for HU.** QDE retired this; HU needs it |
| 09 | `Build YouTube job` · `Write YouTube job` · `Wait for worker` · `Parse worker result` |
| 10 | `Next open slot` · `Assemble drafts` · `Metricool: create draft` · `Verify + collect` |
| 11 | `Preflight` |
| 12 | `Verify` · `Slack: reviewer` · `Daily sweep` |
| 13 | Regenerate forms |

## Where HU differs from QDE — read this before cloning

| | QDE | HU |
|---|---|---|
| Captions copy | per-platform (V9) | per-platform, **four** platforms not five |
| LinkedIn | in scope | **out** — no connection exists |
| Thumbnail | `gpt-image-1` inside n8n | **Gemini plate + build script on the Mac.** Gemini is 403-blocked from n8n Cloud and from the agent sandbox |
| Trait handwriting | generated is acceptable | **never generated.** Real strokes from the published library only |
| Vertical cut | retired (file 08 dead) | **live** — file 10's short drafts depend on it |
| Banned terms | legal-claim language | **"graphology"/"graphologist" banned from all body copy.** Hashtag only |
| CTA | HandwritingExpertUSA.com + bartbaggett.com | **HandwritingUniversity.com only** |
| Credentials | never in HU copy | court testimony counts, judicial acceptance, expert-witness claims are **QDE-only** |

## Open flags

1. **Slack channel and ntfy topic for HU** — needs Bart.
2. **`hu_description_prompt_V3.md`** does not exist. The lane is blocked until it does.
3. **Thumbnail method conflict.** V15 Phase 4 banned "PIL hand-composite" and "red"; `brands/handwriting-university.md` §7 mandates a deterministic Python build and §3/§6 require Teacher Red on the 16:9. See file 07 — unresolved, needs Bart.
4. **`Next open slot` double-booked a day** (QDE runs 308 and 314 both landed on 2026-11-04). Do not share it between lanes until it is read and made brand-aware.
5. **`Betty_SOP_VideoSmimeo_IG_Resize_Normalize_v<n>.md`** is named as file 08's governing doc and was never committed. By this repo's own rule that is a blocked job.
6. **Is Google Drive linked in the Metricool account?** If yes, nothing needs staging. Only checkable in Metricool's own settings.
