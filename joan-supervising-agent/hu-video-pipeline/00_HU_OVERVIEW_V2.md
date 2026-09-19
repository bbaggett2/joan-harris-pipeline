# HU Video Pipeline — 00 OVERVIEW
**V2 · 2026-09-19 (evening) · Lane: Handwriting University only · Replaces `00_OVERVIEW_V1.md`**

One file per step, one n8n node group per file. When an outcome is consistently wrong, the file with that number is the only thing to edit. Each file versions in its own filename; bump the file you changed, nothing else.

> **V2 exists because the QDE lane had a working day on 2026-09-19.** Three defects were root-caused and fixed and one live video ran end to end. Two of this file's open flags are now closed, one hard rule was wrong, and one new defect was found. Everything changed is marked.

> **Filenames carry `HU` as of 2026-09-19.** `01_PICKUP_AND_BRAND_V1.md` collided by name with the QDE step files one directory up; a file opened by name alone could be the wrong brand's. Every step file in this folder is now `<NN>_HU_<NAME>_V<n>.md`.

## Runtime split — this is the shape of the whole lane

**n8n Cloud** (`https://empresse.app.n8n.cloud`) orchestrates everything except the video-file-heavy steps. n8n Cloud has no Execute Command node, so it cannot run `ffmpeg`, `yutu` or `rclone` at all.

**The Mac Studio** runs the side-car workers. n8n writes a job file to a Google Drive queue; a launchd worker on the Mac claims it, does the work, and resumes the workflow through a wait-webhook. The Mac must be on and logged in.

⚠️ **The self-hosted n8n on the Mac (`localhost:5678`) is NOT where this runs.** It is up but holds zero workflows — `workflow_entity`, `shared_workflow`, `workflow_history`, every table, 0 rows. Re-verified 2026-09-19 against a copied db+WAL.

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
⛔ A SAVED n8n CHANGE IS NOT A LIVE CHANGE — and the mechanism is not what V1
   said. n8n Cloud keeps a DRAFT and a PUBLISHED version of every workflow.
     • PATCH /rest/workflows/:id updates the DRAFT only.
     • Production keeps running `activeVersionId` until you publish.
     • Publish with POST /rest/workflows/:id/activate  {versionId, versionName,
       description}. There is no /publish endpoint.
     • Verify with GET /rest/workflows/:id/publication-status — `liveVersionId`
       must equal the draft `versionId` — and read node counts off
       `activeVersion`, never off the workflow object.
   V1's "deactivate, reactivate" described a model this instance does not use.
   Following it leaves the change unpublished while everything reports success.
   This happened on 2026-09-19: a fix was PATCHed, verified against the draft,
   and reported live while production still ran the old 27-node version.
⛔ No HU copy names another company's platform as a destination. The only
   destination is HandwritingUniversity.com. (Bart, 2026-09-19. See file 06.)
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
                        ✅ both blogIds re-verified via getBrandSettings 2026-09-19:
                        HU 6267975, QDE 6268508, one account, both America/Chicago
timezone              : America/Chicago
publish_time          : 06:00 America/Chicago
                        ⚠️ QDE's live Assemble drafts uses 09:00 (read from the node,
                        2026-09-19). Bart's standing rule is 6:00 AM CST — it
                        protects first-24h views. 06:00 wins for HU.
youtube_channel_id    : UCG-DLule9ZSStBdc5gSEoCw   ("@handwritinguniversity")
                        ⚠️ from the Metricool brand record, NOT yet read back from
                        the YouTube API. Prove with `yutu_hu channel-list` before
                        the first upload — see file 09.
youtube_credential    : ~/.config/betty/youtube/hu_client_secret.json
                        + hu.token.json  (GCP project yutu-handwriting-university,
                        its own ~10k/day quota — HU never starves QDE)
facebook_page_id      : 348215195822   (verified HU brand page, Bart 2026-08-18)
networks              : YouTube · TikTok · Instagram · Facebook
                        ⛔ NO LinkedIn, NO X. X @handwritingu is suspended.
slack_channel         : #qde-celebrity-post-review
                        ⭐ SHARED WITH THE QDE LANE. Bart, 2026-09-19: "everyone
                        that needs to see it will see it." The channel's QDE-era
                        name is cosmetic — every HU notice leads with "HU video
                        STAGED" so the lane is unambiguous at a glance (file 12).
                        ⚠️ In the QDE workflows this is hardcoded inside each Slack
                        node, not held in Config. Same for ntfy. Swapping a Config
                        value will not change them.
ntfy_topic            : qde-pipeline-bhi-x7f2k9   (same topic, same reasoning)
ledger                : betty/hu_syndication_ledger.json
clickup_space         : Video Production   statuses: Open · in progress · Closed
prompt_base_url       : https://raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/
copy_prompt           : peggy-olson-copywriting/hu_description_prompt_V<n>.md
                        Current: V3. V2 is a pointer stub. Not a blocker — see
                        file 05 for the one remaining gap (no Shorts variant).
text_model            : gpt-4.1
facebook_cap_bytes    : 524288000   (500 MB — a size cap, never a duration gate)
```

Everything not in this block — voice, palette, fonts, banned words, audience, domain — comes from `brands/handwriting-university.md`.

## The QDE source lane — verified 2026-09-19, for whoever does the clone

Read node by node from the live REST API. The video lane is **four** workflows plus a shared helper, not two.

| QDE workflow | ID | Nodes |
|---|---|---|
| `Betty — QDE Video Publish v2` (orchestrator) | `Heg8RaNTQxk3c2rz` | 86 |
| `Betty — QDE YouTube Publish v1` | `UW1eOY9bPaf8kBiw` | 31 |
| `Betty — QDE Metricool Drafts v1` | `em4VP1LAYyE3BPbJ` | 12 |
| `Betty — QDE Error Handler v1` | `eamKOlBW13KCipbQ` | 4 |
| `Next open slot (Mon–Fri, shared)` | `ibBwdX2a85z93M7E` | 3 — **share, do not clone** |
| `Betty — QDE Daily Social Post v3` | `05ynfXtxJLa2oi1m` | 27 — out of scope, schedule-triggered |

Wiring: the orchestrator calls YouTube Publish and Metricool Drafts; Metricool Drafts calls Next open slot. `errorWorkflow: eamKOlBW13KCipbQ` is set on the first three.

⚠️ **Values hardcoded outside the Config node** — a Config swap alone will not catch these. The ntfy URL and Slack channel in every notify node; `brands/qde-brand.md`; `peggy-olson-copywriting/qde_legal_description_prompt_V9.md`; the upload-queue folder `1rm7hEFT0p9cd5H-bYMH--kNM-3PBk0Vn`; and the QDE Ready folder ID repeated inside the `Video found?` error text. Grep the whole HU JSON before publishing.

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
| 09 | `Build YouTube job` · `Write YouTube job` · `Wait for worker` · `Parse worker result` · the ⚠️ incomplete-publish branch |
| 10 | `Next open slot` · `Assemble drafts` · `Metricool: create draft` · `Verify + collect` |
| 11 | `Preflight` |
| 12 | `Verify` · `Slack: reviewer` · `Daily sweep` |
| 13 | Regenerate forms |

## Where HU differs from QDE — read this before cloning

| | QDE | HU |
|---|---|---|
| Captions copy | per-platform | per-platform, **four** platforms not five |
| LinkedIn | in scope | **out** — no connection exists |
| Thumbnail | `gpt-image-1` inside n8n | **Gemini plate + build script on the Mac.** Gemini is 403-blocked from n8n Cloud and from the agent sandbox |
| Trait handwriting | generated is acceptable | **never generated.** Real strokes from the published library only |
| Vertical cut | retired (file 08 dead) | **live** — file 10's short drafts depend on it |
| Banned terms | legal-claim language | **"graphology"/"graphologist" banned from all body copy.** Hashtag only |
| CTA | HandwritingExpertUSA.com + bartbaggett.com | **HandwritingUniversity.com only** |
| Credentials | never in HU copy | court testimony counts, judicial acceptance, expert-witness claims are **QDE-only** |
| Slack / ntfy | `#qde-celebrity-post-review` | **the same channel and topic** — shared deliberately |
| Publish time | 09:00 (live node value) | **06:00** — Bart's standing rule |

**Two of the three QDE defects are fixed in the shared layer.** `make_16x9()` and `fix_vtt_hours()` both live in the single `worker.py` that serves both brands, so HU inherits the thumbnail and caption fixes without a second patch. Only the n8n-side ⚠️ incomplete-publish branch has to be duplicated (file 09).

## Open flags

1. **Thumbnail method conflict.** V15 Phase 4 banned "PIL hand-composite" and "red"; `brands/handwriting-university.md` §7 mandates a deterministic Python build and §3/§6 require Teacher Red on the 16:9. See file 07 — unresolved, needs Bart.
2. **No Shorts variant in the copy prompt.** ⚠️ **No longer hypothetical — it cost a real video on 2026-09-19.** VID-9946 was classed `short` and received a 303-character description; YouTube then filed it as a normal video, so a three-minute piece shipped with a Shorts-length description. Interim handling and the durable fix are in file 05.
3. ~~`Next open slot` double-booked a day.~~ **✅ CLOSED 2026-09-19.** The node was read: it declares `blogId` as a workflow input and the caller passes `metricool_blogId`. It is already brand-aware. On a live run it picked the correct next open weekday. The V1 claim that QDE runs 308 and 314 double-booked 2026-11-04 was not reproduced and should be treated as unverified. **Share it between lanes; do not clone it.**
4. **`Betty_SOP_VideoSmimeo_IG_Resize_Normalize_v<n>.md`** is named as file 08's governing doc and was never committed. By this repo's own rule that is a blocked job.
5. **Is Google Drive linked in the Metricool account?** If yes, nothing needs staging. Only checkable in Metricool's own settings.
6. ~~No n8n Cloud API key on the Mac.~~ **✅ CLOSED 2026-09-19.** Not needed. The whole `/rest/…` surface works through an authenticated browser session with the `browser-id` header from `localStorage.getItem('n8n-browserId')` — read workflows, PATCH, POST new ones, publish, and read execution data. A full workflow was backed up, patched, published and verified this way. An API key is still tidier if Bart wants one; it is not a blocker.
7. **The copy prompt still ends with a pre-paste sign-off line** that contradicts the two-touchpoint review model. Flagged in V3's own footer; needs Bart to either delete the line or restore the gate.
8. **NEW — `Media facts` misclassifies Shorts at the boundary.** See file 02. Deferred by Bart as rare; the one-line fix is recorded there.
9. **NEW — per-platform caption distinctness has still never been proven** on any run, either lane. File 06 carries the assertion; nothing has yet exercised it.

> ✅ **Closed 2026-09-19 — HU alerting.** Bart ruled: share the QDE Slack channel and ntfy topic.
> ✅ **Closed 2026-09-19 — the copy prompt.** The lane was never blocked on a rewrite; V2 already required five distinct per-platform outputs and chapters before the CTA. V3 adds the off-platform ban.
> ✅ **Closed 2026-09-19 — the caption failure.** Root cause found and fixed. It was never a readiness race. See file 09.
