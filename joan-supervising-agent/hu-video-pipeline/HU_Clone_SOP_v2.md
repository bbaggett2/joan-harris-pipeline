# HU Video Publish — n8n Clone & Activation SOP

**v2 · 2026-09-19 (evening) · supersedes v1 of the same date**
**Goal:** fork the working QDE video lane into a Handwriting University lane that accepts *only* HU videos, and activate it.
**Source of truth:** `bbaggett2/joan-harris-pipeline` @ `main` · n8n Cloud `https://empresse.app.n8n.cloud`

> **Read §0 and §1 before touching anything.** v1 of this document was written before the live workflow graph had ever been opened. It has now been read node by node, and three defects that v1 listed as open have been found, fixed and proven on a live run. Several v1 claims were wrong and are retracted explicitly in §0.3 — do not carry them forward.

---

## 0. State of the world, verified 2026-09-19

### 0.1 What changed today

Three QDE defects were root-caused and fixed, each proven at the destination rather than by an exit code:

| Defect | Root cause | Status |
|---|---|---|
| Custom thumbnail never appeared on YouTube | `yutu thumbnail set` **silently refuses an absolute `--file` path** — prints its usage text to stdout, never calls the API, exits `0`. Compounded by `gpt-image-1` having no 16:9 size, so its `1536x1024` (3:2) output was rejected by YouTube even when it did upload. | **FIXED & PROVEN.** `cd` + basename, plus an ffmpeg centre-crop to 1280×720, plus a real check of the API response shape. Live run logged `thumbnail set (1280x720)`, `youtube_thumbnail_set: true`, and the thumbnail is visibly displaying. |
| Caption track always `status=failed / processingFailed` | `fix_vtt_hours()` in `worker.py` used `r'\b\d{2}:\d{2}\.\d{3}\b'`, which also matches the **tail** of a well-formed `HH:MM:SS.mmm` stamp. `00:00:00.216` became `00:00:00:00.216` — four colon-separated fields, invalid WebVTT. Descript always emits hours, so **every cue of every VTT this worker ever uploaded was corrupted in flight.** | **FIXED & PROVEN.** Lookbehind `(?<![\d:])` refuses a preceding digit or colon. Same video, same VTT, same production function: `status=serving` on the **first** attempt, no retries. |
| Pipeline reported ✅ Production Complete on videos with no thumbnail and no captions | `Worker succeeded?` tested only `worker_status === "OK"`, which the worker sets as soon as the **video** uploads. `youtube_thumbnail_set` / `youtube_captions_set` were parsed one node earlier and never gated on. | **FIXED & PUBLISHED.** A four-node non-blocking warning branch was added to `Betty — QDE YouTube Publish v1`. It fired correctly on the one run where captions genuinely failed. **This branch must be cloned to HU — see §4 C7.** |

**The caption "readiness race" hypothesis is dead.** v1 §0.4 and §3 B7.2 treated `processingFailed` as a timing problem and proposed longer waits. It was never timing — it was a malformed file, and no amount of retrying could ever have fixed it. The retry loop in `worker.py` is now a safety net, not the mechanism.

### 0.2 Verified facts about the live system

Everything in this table was read from the live n8n REST API or from the Mac this session. No `[assumed]` remains in this section.

| # | Fact | Evidence |
|---|---|---|
| **0.2.1** | The pipeline runs on **n8n Cloud**, not the Mac. | Worker job JSON carries `resume_webhook_url: https://empresse.app.n8n.cloud/webhook-waiting/...` |
| **0.2.2** | The self-hosted n8n on the Mac is **empty**. `localhost:5678` answers (401 on `/rest/login`) and the process is up since Sept 13, but **every** workflow table holds 0 rows — `workflow_entity`, `shared_workflow`, `workflow_history`, all of them. | `sqlite3 ~/.n8n/database.sqlite` against a copied db+WAL |
| **0.2.3** | **n8n Cloud uses draft/published versioning.** A `PATCH /rest/workflows/:id` updates the **draft only**. Production keeps running `activeVersionId` until you publish. | `GET /rest/workflows/:id` returns both `versionId` and `activeVersionId`; `GET /rest/workflows/:id/publication-status` returns `{status, liveVersionId, pendingVersionId, triggers[]}` |
| **0.2.4** | Publishing is `POST /rest/workflows/:id/activate` with body `{versionId, versionName, description}`. There is **no** `/publish` endpoint. | Found in the editor bundle; confirmed with a 200 and `liveVersionId` moving to match `versionId` |
| **0.2.5** | The QDE video lane is **four** workflows plus a shared helper, not two. | See §2.1 |
| **0.2.6** | `Next open slot` is **already brand-parameterised** — it declares `blogId` as a workflow input and the caller passes `metricool_blogId`. Safe to share. | Node JSON + `Metricool Drafts` caller params |
| **0.2.7** | Metricool: **one account** (`userId 4831552`), **two brands** — QDE `Handwriting Expert Inc` = blogId `6268508`; HU `thehandwritinguniversity` = blogId `6267975`. Both `America/Chicago`. | `getBrandSettings` |
| **0.2.8** | HU YouTube channel is `UCG-DLule9ZSStBdc5gSEoCw`; QDE is `UCrpyI5SkE075HJaFyxO_ozQ`. | Metricool brand records — **still not read back from the YouTube API. Confirm in A4.** |
| **0.2.9** | `worker.py` is **hardcoded to QDE credentials** and polls **one shared queue**. | `CRED_PATH`/`TOKEN_PATH` → `qde_client_secret.json` / `qde.token.json`; `QUEUE_REMOTE = "gdrive:youtube_upload_queue"` |
| **0.2.10** | The worker refuses to re-upload the same `vid_id\|drive_file_id` within **6 hours** unless the job sets `force_reupload`. The job builder never sets it. | `uploaded_ledger.json`, `DUPLICATE_WINDOW_S = 6*3600`; observed refusing a duplicate live |
| **0.2.11** | Worker runs under launchd as `com.betty.youtube-worker` and **respawns automatically** when killed. | `launchctl list`; killed PID 92331, respawned as 93582 on patched code |
| **0.2.12** | Two hard gates exist in the orchestrator and both work. `Video found?` stops an empty/missing filename; `Verify delivery file name (AM)` stops when column AM is blank or disagrees with the Drive filename. | Execution 322 died in 4.5s on `DELIVERY NAME CHECK FAILED — column AM is blank on the matched row` |
| **0.2.13** | The form trigger takes one field. When POSTing programmatically the key is **`field-0`**, not the display label. | Error text in `Video found?`; confirmed by a successful POST |
| **0.2.14** | Metricool drafts from the pipeline land with `draft: true` **and** `autoPublish: true`. They behave as drafts. `autoPublish` only takes effect if a human converts the draft to scheduled. | `getScheduledPosts` on the batch this run created |
| **0.2.15** | `Fetch title rules` and `Fetch caption rules` are **disabled** in the orchestrator. In n8n a disabled node passes its input through, which makes it *look* like it returned data. | Node JSON `disabled: true`; passthrough payload identical to the description prompt |

### 0.3 v1 claims now retracted — do not carry these forward

1. **"`Next open slot` has an open double-booking defect; do not clone or share it until read."** — Read. It is brand-parameterised and it chose the correct date on the live run. **Share it, do not clone it.** The v1 claim that runs 308/314 double-booked 2026-11-04 was not reproduced and should be treated as unverified.
2. **"The caption failure is a readiness race / root cause unknown."** — Root cause found (§0.1). Closed.
3. **"There is no HU pipeline document on `main`."** — v1 itself superseded this in its own §9. `HU_Video_Publishing_Pipeline_V15.md` exists and is authoritative for the *agent* process. `V14.md` is a misfiled QDE copy and should be retired.
4. **"Fix it twice."** — Wrong in the way that matters. `make_16x9()` and `fix_vtt_hours()` both live in `worker.py`, which serves **both** brands from one file. HU inherits both fixes for free. Only the n8n-side warning branch needs duplicating.

### 0.4 Not verified this session — inherited from v1, treat as unconfirmed

- Existence and validity of `~/.config/betty/youtube/hu_client_secret.json` and `hu.token.json`
- The `yutu-handwriting-university` GCP project and its quota
- Contents of `brands/handwriting-university.md`, `HU_Video_Publishing_Pipeline_V15.md`, `hu_description_prompt_V2.md`
- Collegiate FLF font availability and licence
- Gemini reachability from the Mac
- Whether the n8n Drive credential can see the HU Ready-to-Publish folder

---

## 1. Process rules — learned the hard way, apply without exception

**R1 — A saved change is not a live change.** n8n Cloud keeps a draft and a published version. `PATCH` updates the draft; production keeps running the old code. Always finish with `POST /rest/workflows/:id/activate` and then **verify against `activeVersion`, not against the workflow object.** Reading back the draft and reporting success is the exact mistake made earlier today.

**R2 — A step that returns cleanly has not necessarily done anything.** Three separate no-ops this week: `yutu thumbnail set` printed usage and exited `0`; `worker.py` was edited without a restart; an n8n sub-workflow ran stale code. Confirm every external effect by reading it back from the destination — channel ID, caption status, thumbnail bytes, blogId — never from an exit code or a green tick.

**R3 — A credential that works is not a credential pointed at the right place.** Most credentials are shared between brands; most destinations are not. See §5.

**R4 — Back up before every write.** Workflows: duplicate to `BACKUP <reason> <date> — <name>` (inactive) via `POST /rest/workflows`, matching the existing `BACKUP pre-regex-fix …` convention. Files: `cp x x.bak-$(date +%Y%m%d-%H%M%S)-<reason>`.

**R5 — Diagnose from execution data, not from inference.** `GET /rest/executions/:id?includeData=true` returns **flatted** JSON: an array pool where a numeric string is an index into that pool. Resolve it recursively before reading. Twice today a plausible theory was wrong and the execution data settled it in one call.

**R6 — No API key is required.** All of the above was done through the browser session against `/rest/…` with the `browser-id` header from `localStorage.getItem('n8n-browserId')`. An n8n Cloud API key is still cleaner if Bart wants to mint one, but it is **no longer a blocker**.

---

## 2. The clone map

### 2.1 Workflows — verified IDs and node counts

| # | QDE workflow (live, Published) | ID | Nodes | HU clone |
|---|---|---|---|---|
| 1 | `Betty — QDE Video Publish v2` | `Heg8RaNTQxk3c2rz` | 86 | **`Betty — HU Video Publish v1`** |
| 2 | `Betty — QDE YouTube Publish v1` | `UW1eOY9bPaf8kBiw` | **31** (27 + the 4 new warning nodes) | **`Betty — HU YouTube Publish v1`** |
| 3 | `Betty — QDE Metricool Drafts v1` | `em4VP1LAYyE3BPbJ` | 12 | **`Betty — HU Metricool Drafts v1`** |
| 4 | `Betty — QDE Error Handler v1` | `eamKOlBW13KCipbQ` | 4 | **`Betty — HU Error Handler v1`** |
| 5 | `Next open slot (Mon–Fri, shared)` | `ibBwdX2a85z93M7E` | 3 | **SHARE — do not clone** |
| — | `Betty — QDE Daily Social Post v3` | `05ynfXtxJLa2oi1m` | 27 | **Out of scope.** Schedule-triggered, not part of the video lane |

**Wiring, verified:** `Video Publish v2` → `Call YouTube Publish` (`UW1eOY9bPaf8kBiw`) and `Call Metricool Drafts` (`em4VP1LAYyE3BPbJ`). `Metricool Drafts` → `Next open slot` (`ibBwdX2a85z93M7E`). `errorWorkflow: eamKOlBW13KCipbQ` is set on workflows 1, 2 and 3. `Next open slot` has no error workflow.

A rollback point already exists: **`BACKUP pre-warn-gate 2026-09-19 — QDE YouTube Publish v1`** (`OrZf3nausd7iSRqd`, 27 nodes, inactive).

### 2.2 Config node — read verbatim from the live `Config` node

| Key | QDE (verified today) | HU | Status |
|---|---|---|---|
| `qde_ready_folder_id` | `132glSPYurgEtU1ZkNqSlA5W6NOmK5Vx0` | `1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv` | ✅ rename the key for HU |
| `queue_sheet_id` | `1EO2ZdAEiVHJ9FVz5ZHY-9f0CjjngHkpMVa84nHCFpDA` | same sheet, **read-only** | ✅ |
| `assets_folder_id` | `1V-piQzAW8iOYn_AesxkDzK4lcWLXUYvY` | **must be created** | ⛔ B5 |
| `metricool_blogId` | `6268508` | `6267975` | ✅ verified both |
| `metricool_userId` | `4831552` | `4831552` | ✅ same account |
| `timezone` | `America/Chicago` | `America/Chicago` | ✅ verified both |
| `youtube_channel_id` | `UCrpyI5SkE075HJaFyxO_ozQ` | `UCG-DLule9ZSStBdc5gSEoCw` | ⚠️ read back in A4 |
| `slack_channel` | `#qde-celebrity-post-review` | **undecided** | ⛔ B6 |
| `prompt_base_url` | `https://raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/` | same | ✅ |
| `facebook_cap_bytes` | `524288000` | `524288000` | ✅ |

**Correction to v1:** there is **no `ntfy_topic` key in Config.** The ntfy URL `https://ntfy.sh/qde-pipeline-bhi-x7f2k9` is hardcoded in every `Notify: …` HTTP node. Same for the Slack channel name inside each Slack node, and for the prompt paths inside each `Fetch …` node. The §4 D2 grep is therefore **not optional** — config swapping alone will not catch these.

Also hardcoded outside Config:
- `Write YouTube job` folder: `1rm7hEFT0p9cd5H-bYMH--kNM-3PBk0Vn` (the QDE upload queue)
- `Fetch brand kit`: `brands/qde-brand.md`
- `Fetch description prompt`: `peggy-olson-copywriting/qde_legal_description_prompt_V9.md`
- `Video found?` code: the QDE folder ID appears again inside the error message
- `Next open slot` Metricool URL: `userId=4831552` hardcoded (fine — same account)

---

## 3. Blockers

### B1 ⛔ The Mac worker will upload HU videos to the QDE channel — still the highest risk

Unchanged from v1 and **still true**. `worker.py` hardcodes the QDE OAuth credential and polls one queue. An HU job dropped into `gdrive:youtube_upload_queue` today uploads to the QDE channel. Because uploads are private, nobody would notice.

**Fix — one worker, brand-aware:**

1. `Build YouTube job` adds `"brand": "HU"`, `"yutu_credential": "hu_client_secret.json"`, `"yutu_token": "hu.token.json"`, `"expected_channel_id": "UCG-DLule9ZSStBdc5gSEoCw"`.
2. In `worker.py`, replace the module-level constants with a per-job lookup defaulting to QDE **only when `brand` is absent**, so existing QDE jobs are untouched:
   ```python
   CREDS = {
     "QDE": ("qde_client_secret.json", "qde.token.json"),
     "HU":  ("hu_client_secret.json",  "hu.token.json"),
   }
   ```
3. **Hard assertion after upload:** read `channelId` back via `videos.list(part=snippet)` and compare to `expected_channel_id`. Mismatch → mark the job failed, alert loudly, delete nothing. A wrong-channel upload is a stop, never a warning. (This is R2 applied to identity.)
4. Give HU its own queue folder anyway (B5) — belt and braces.
5. Restart: killing the process is enough, launchd respawns it (0.2.11). Verify the new PID is running the new file.

### B2 ⛔ HU thumbnails are a different build and cannot run in n8n Cloud

Unchanged from v1 in substance. QDE generates with `gpt-image-1` inside n8n; HU requires a Gemini plate plus a deterministic PIL composite on the Mac, with real trait handwriting from the published library and Collegiate FLF type.

**What today's work changes:**

- The **16:9 crop is already solved in the shared layer.** `make_16x9()` in `worker.py` converts any non-16:9 thumbnail to 1280×720 before upload and logs the conversion. HU gets this free.
- The **silent-no-op bug is fixed in the shared layer too** — `cd` + basename. HU gets this free.
- So B2 is now only about **generating an on-brand HU image**, not about getting it onto YouTube. That materially shrinks the work item.
- Keep the dimension check, and make it **fatal** for HU rather than a warning.
- Naming: `<VID_ID>_thumb_v<n>.png` with `<n>` computed from existing files. Do not inherit QDE's hardcoded `_thumb_v1.png`.

*Best estimate, not a commitment:* still the largest single item, on the order of a day to build and prove.

### B3 ⛔ `hu_description_prompt_V2.md` predates the V9 output contract

The QDE prompt is `peggy-olson-copywriting/qde_legal_description_prompt_V9.md`, **17,102 bytes**, and its structure is now known precisely. It defines six outputs:

| Output | Surface | Spec |
|---|---|---|
| 1 | Long-form YouTube description | 200–400 words + chapters, 12–18 hashtags |
| 2 | **YouTube Shorts description** | **150–300 characters, 3–5 hashtags, no chapters, no timestamps** |
| 3–4 | TikTok / Instagram captions | per-platform, never reused |
| 5 | Facebook Reel caption | 75–150 words, 3 hashtags |
| 6 | Facebook feed POST | full-length cut |

Plus: title under 10 words, written first from the transcript; chapters **before** the CTA, skipped under ~2 minutes; `chapters: []` for a Short; `tiktok_hook` as an **array** of 2–3 strings; a `mode` enum of `attorney` / `consumer`.

**Write `hu_description_prompt_V3.md` before the first HU run.** It must carry the V9 *output contract* minus LinkedIn, and:

- **Four platforms**, not five: YouTube (long or Short by `yt_format`), TikTok, Instagram, Facebook.
- **`graphology` / `graphologist` banned** from all body copy, titles, descriptions and on-screen text — hashtag only. Enforce as a rejected-token check in `Preflight`, not only in prose.
- **No QDE credentials anywhere** — no court-testimony counts, no judicial-acceptance rate, no expert-witness claims, no outcome promises.
- **CTA to HandwritingUniversity.com only.** Never HandwritingExpertUSA.com, never bartbaggett.com, and **never `HandwritingExpert.com` in any copy at all.**
- First person, second-person address; body built from the actual transcript, never from the title.
- Bart's own copy reproduced exactly as written, never tidied.

Peggy's folder owns *what* gets written; Joan's folder owns *how* the pipeline carries it. Joan's step files must not restate voice rules.

### B4 ✅ LinkedIn — decided, remove it

HU's Metricool brand connects Facebook, Instagram, TikTok, YouTube only. Drop the LinkedIn destination from `Assemble drafts`, drop Output 4 from the schema.

**Note:** in the QDE `Assemble drafts`, LinkedIn is already conditional — `if (r.linkedin) out.push(...)`. So an empty `linkedin` field would skip it naturally. But the LLM JSON schema lists `linkedin` in `required`, so the model will still produce it. Remove it from the schema properly rather than relying on the conditional.

### B5 ⛔ HU Drive infrastructure does not exist

- `5 HU Pipeline Assets` — parallel to `1V-piQzAW8iOYn_AesxkDzK4lcWLXUYvY`
- `hu_youtube_upload_queue` inside it, with `done/` and `failed/` subfolders
- Confirm the n8n Drive credential can actually see `1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv`

### B6 ⛔ HU alerting is undecided

Needs Bart: which Slack channel (suggest a new `#hu-video-review`), and a fresh ntfy topic. Remember these are **hardcoded per node**, not in Config.

Alert text must carry the plain-language `Error to Correct:` line ending in `Please have human investigate`.

### B7 ⚠️ QDE defects the clone would inherit — updated

1. ~~Thumbnail aspect ratio~~ — **CLOSED.** Fixed in the shared layer.
2. ~~Captions `processingFailed`~~ — **CLOSED.** Root-caused and fixed in the shared layer.
3. **Per-platform captions still unproven.** No run has yet been checked for five genuinely distinct captions. HU's first run is a chance to prove it, with the extra check that no caption contains "graphology".
4. **NEW — `Media facts` misclassifies Shorts at the boundary.** `duration_s: Math.round(durationMillis/1000)` turned `180499` ms into `180`, and the rule `_dur <= 180` said "short". YouTube measured the true 180.499 s, rejected it from Shorts by 499 ms, and filed it as a regular video — which then received a 303-character Shorts description instead of the long-form one. Bart has deferred this as rare. One-line fix when wanted:
   ```js
   const _ms = Number(m.durationMillis || 0);
   out.yt_format = (out.aspect === 'vertical' && _ms > 0 && _ms <= 179000) ? 'short' : 'long';
   ```
5. **NEW — thumbnail crop quality.** `make_16x9()` centre-crops. When a headline sits near the top or bottom it will clip. Correctness is fixed; composition is not. Deferred by Bart.

---

## 4. Execution

### Phase A — Access and safety net

- **A1.** No API key needed (R6). If Bart prefers one, Settings → n8n API, save to `~/.config/betty/n8n/api_key`, `chmod 600`.
- **A2.** Confirm the five workflows and their node counts against §2.1.
- **A3.** **Export all five to JSON** into `n8n_backups/` as `20260919-<WorkflowName>-PRE-HU-CLONE.json`. Also duplicate each in n8n as an inactive `BACKUP …` workflow (R4).
- **A4.** **Read the HU channel ID back from YouTube** — `yutu_hu channel-list` must return `UCG-DLule9ZSStBdc5gSEoCw`. Anything else, or a 401, stop and re-mint. This single check prevents the entire B1 failure class.
- **A5.** Confirm `hu_client_secret.json` and `hu.token.json` exist and are readable by the worker's user.

### Phase B — HU infrastructure

- **B1.** Create the Drive folders (B5). Record IDs here.
- **B2.** Generate the HU ntfy topic; get Bart's Slack channel (B6).
- **B3.** Patch `worker.py` for brand-aware credentials + the post-upload channel assertion. Back up first. Restart and confirm the new PID.
- **B4.** **Prove the worker patch on QDE before HU exists.** Run one QDE job with no `brand` key. It must still reach the QDE channel and the new assertion must pass. If QDE breaks, stop.

### Phase C — Clone

- **C1.** For each of the four workflows: `POST /rest/workflows` with the exported nodes/connections/settings, HU name, **`active: false`**.
- **C2.** Repoint every sub-workflow reference in the HU orchestrator at the new HU IDs. A missed reference means the HU orchestrator silently calls the QDE sub-workflow — same failure class as B1.
- **C3.** Set `Betty — HU Error Handler v1` as `settings.errorWorkflow` on the other three.
- **C4.** Replace the trigger. v1 specified a Drive trigger on the HU Ready folder; the live QDE lane uses a **form trigger** (`Run QDE video`, one field, key `field-0`). Pick one deliberately — a Drive trigger gives Bart's "folder is the brand" rule automatically; a form keeps parity with QDE. **Needs a decision (§7 item 7).**
- **C5.** Fix `brand = "HU"` in the queue-row lookup. Not inferred, not looked up.
- **C6.** Keep `Video found?` and `Verify delivery file name (AM)` exactly as QDE has them — both are proven working hard stops (0.2.12). Update the folder ID inside the `Video found?` error text.
- **C7. Clone the warning branch.** The four new nodes in `QDE YouTube Publish v1` must exist in the HU clone: an IF on `youtube_thumbnail_set && youtube_captions_set` hanging off `YT Result` (so it runs alongside the success path and blocks nothing), feeding a Code node that names what missed, into HU's Slack and ntfy nodes.

### Phase D — Config swap

- **D1.** Apply every row of §2.2.
- **D2.** **Grep the whole HU JSON for QDE leakage before publishing.** This is the single highest-value check, and §2.2 explains why config alone is insufficient. Any hit is a bug:
  `132glSPY` · `1V-piQzAW` · `1rm7hEFT` · `6268508` · `UCrpyI5SkE` · `qde-pipeline-bhi` · `qde_legal_description` · `qde-brand.md` · `qde_client_secret` · `HandwritingExpertUSA` · `bartbaggett.com` · `qde-celebrity-post-review` · `Thumbnail_Brand_SOP_QDE` · `1-800-980-9030`
- **D3.** n8n expression hygiene: one `}}` per expression, no consecutive braces; no apostrophes inside single-quoted strings; validate as *n8n text*, not JavaScript.
- **D4. Publish, then verify against `activeVersion`** (R1). `POST /rest/workflows/:id/activate` with the draft `versionId`, then confirm `publication-status.liveVersionId` matches and the node count is what you expect.

### Phase E — Thumbnail lane (B2)

- **E1.** Delete `OpenAI — thumbnail` from the HU clone.
- **E2.** Rewrite `Thumbnail: prompt` to fetch the HU brand file + constants and emit a **build job**, not an image.
- **E3.** Build and prove the Mac-side HU thumbnail worker standalone — 1280×720, fonts present, trait card from the library, logo bottom-right clear, legible at 168×94.
- **E4.** Wire the resume webhook. Keep the dimension check, fatal for HU.

### Phase F — Copy lane (B3)

- **F1.** Write `hu_description_prompt_V3.md`; Bart commits it (the Mac has no GitHub write credentials).
- **F2.** Repoint `Fetch description prompt` at its raw URL, and `Fetch brand kit` at the HU brand file.
- **F3.** Rebuild the LLM JSON schema for four platforms, no LinkedIn.
- **F4.** Add HU `Preflight` assertions: reject `graphology`/`graphologist` outside hashtags; reject any QDE credential string, court-testimony count or judicial-acceptance figure; reject `HandwritingExpert.com`; require the HandwritingUniversity.com CTA. Each rejection a named flag, never a silent fix.

### Phase G — Dry run, workflow inactive

- **G1.** Manual execution against an HU video **already published**, so nothing new reaches YouTube.
- **G2.** Assert node by node: brand `HU`; four captions distinct; no banned term; Metricool payload carries `6267975`; the YouTube job carries the HU credential and `expected_channel_id`; thumbnail 16:9.
- **G3.** Do not let it write a real Metricool draft — disconnect the Metricool leg, or point it at a future date you will delete.

### Phase H — One real video, end to end

- **H1.** One HU video into the HU Ready folder, with its Workflow-tab row and **column AM filled first** — a blank AM is a hard stop (0.2.12).
- **H2.** Trigger manually rather than waiting on a poll.
- **H3.** Verify **at the destination** (R2): `videos.list` shows it on `UCG-DLule9ZSStBdc5gSEoCw`, private, with the custom 16:9 thumbnail actually attached; caption track reads `serving`; `getScheduledPosts` shows four drafts on blogId `6267975` and **none** on `6268508`.
- **H4.** Read all captions and the description end to end against the HU QA checklist before anything goes public.

### Phase I — Activate

- **I1.** Activate the three sub-workflows first, then the orchestrator. Then **confirm from `publication-status` and a later execution's `workflowData` that the live code is the new code** (R1).
- **I2.** Confirm the Mac worker is running the patched file.

### Phase J — Document

- **J1.** Write `joan-supervising-agent/HU_Video_Publishing_Pipeline_V1.md`; retire or correct `V14.md` (a misfiled QDE copy).
- **J2.** Add an HU column to the `00_OVERVIEW` Config block, or split an `hu-video-pipeline/` step folder.
- **J3.** Back up all four HU workflows as JSON.
- **J4.** Correct the standing note that n8n Cloud is unused — it is the production host (0.2.1/0.2.2).
- **J5.** Record the three fixes of 2026-09-19 and their root causes, so nobody re-opens them as "readiness" or "aspect ratio" problems.

---

## 5. 📌 PINNED — Authorization & channel binding: check EVERY stop

**Bart's standing instruction.** Most credentials are shared; most destinations are not. A shared token pointed at an unchanged destination ID is how HU content lands on a QDE channel — and because everything stages private or draft, it would not be obvious.

| # | Stop | Credential | Destination binding | Risk if missed |
|---|---|---|---|---|
| 1 | YouTube upload / thumbnail / captions (Mac worker) | **DIFFERENT** — `hu_client_secret.json` + `hu.token.json` | Channel `UCG-DLule9ZSStBdc5gSEoCw` | **HU video on the QDE channel.** Hardcoded today — B1 |
| 2 | Metricool drafts | **SAME** token, **SAME** `userId 4831552` | **DIFFERENT** `blogId` — HU `6267975`, QDE `6268508`; different per-network connections (FB `348215195822`, IG `@thehandwritinguniversity`, TikTok `@handwritinguniversity`) | **HU posts on the QDE calendar.** The API call succeeds either way |
| 3 | Google Drive | likely SAME OAuth — unconfirmed | **DIFFERENT** folder IDs at four points: ready, assets, upload queue, done/failed | Files into QDE's assets; jobs into QDE's queue |
| 4 | Google Sheets | SAME | SAME sheet, **read-only** | A write corrupts dropdown-validated columns |
| 5 | rclone `gdrive:` | SAME token | **DIFFERENT** queue path | HU job claimed off the QDE queue |
| 6 | Gemini (HU thumbnail plate) | Mac `.env` — unreachable from n8n Cloud | n/a | Silent thumbnail failure off-Mac |
| 7 | OpenAI (text) | SAME | **DIFFERENT prompt + brand file URLs** | HU video described in QDE legal voice, with QDE credentials in the copy |
| 8 | Slack | SAME workspace token | **DIFFERENT** channel — hardcoded per node | HU failures in the QDE reviewer's stream |
| 9 | ntfy | none | **DIFFERENT** topic — hardcoded per node | Same, on mobile |
| 10 | GitHub raw | none | **DIFFERENT** prompt + brand paths | Wrong brand rules applied silently |
| 11 | Descript | SAME | n/a | — |

**Prove each destination by reading back from it**, never by a successful call. Specifically: `yutu_hu channel-list` before wiring YouTube; create one throwaway HU Metricool draft and confirm via `getScheduledPosts` that it is on `6267975` and **not** on `6268508`, then delete it.

---

## 6. Acceptance criteria

HU is not done until every one of these is proven **at the destination**:

1. A file in the HU Ready folder starts the HU workflow and nothing else.
2. A file in the QDE folder does not start the HU workflow, and vice versa.
3. The video is on `UCG-DLule9ZSStBdc5gSEoCw`, **private**, never on `UCrpyI5SkE075HJaFyxO_ozQ`.
4. The attached thumbnail is 16:9, on-brand, with real trait handwriting from the library.
5. The caption track reads **`serving`** — not merely "inserted".
6. Four Metricool drafts on blogId `6267975`, `draft: true`, four **distinct** captions.
7. Zero `graphology`/`graphologist` outside hashtags; zero QDE credentials; CTA to HandwritingUniversity.com only.
8. A deliberate failure reaches the HU Slack channel and HU ntfy topic with the `Error to Correct:` line.
9. The ⚠️ incomplete-publish branch fires when thumbnail or captions do not land.
10. No write of any kind touches the master Workflow spreadsheet.

---

## 7. Open items needing Bart

| # | Question | Blocks |
|---|---|---|
| 1 | **HU Slack channel** — new `#hu-video-review`, or existing? | B6, Phase B2 |
| 2 | **HU ntfy topic** — generate a fresh random-suffixed one? | B6 |
| 3 | **`hu_description_prompt_V3.md`** — I draft, you commit. Confirm four-platform scope, V9 shape minus LinkedIn. | F1 |
| 4 | **V15 contradictions** carried from v1 §9: `BANNED: PIL hand-composite` contradicts the brand kit's mandated deterministic script; `BANNED: red` contradicts Teacher Red `#D62828` on 16:9. Both need a ruling. | E-phase |
| 5 | **Collegiate FLF commercial licence** still `[TO VERIFY]`. | Not blocking; scales with this |
| 6 | **Sequencing** — QDE is now materially healthier than this morning. Clone immediately, or run two or three more QDE videos first to confirm the fixes hold? | Start date |
| 7 | **Trigger type (C4)** — Drive trigger on the HU Ready folder (folder-is-the-brand, automatic) or a form trigger matching QDE's current design? | C4 |

---

## 8. What this document does not claim

- HU-side credentials, fonts, brand-kit contents and V15 details are **inherited from v1 and not re-verified** (§0.4).
- `UCG-DLule9ZSStBdc5gSEoCw` comes from the Metricool record, not a YouTube API read. A4 settles it.
- Effort estimates are best estimates, not commitments.
- Per-platform caption distinctness has **never** been proven on any run, either brand.
- The QDE fixes of 2026-09-19 are proven on **one** live run (VID-9946 → `S6JgRfTbdjY`). One run is evidence, not a track record.
