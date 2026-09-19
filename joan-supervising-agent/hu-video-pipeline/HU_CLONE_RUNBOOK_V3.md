# HU Clone Runbook
**V3 · 2026-09-19 (evening) · Replaces `HU_Clone_SOP_v2.md`**

How to build and activate the HU lane, in order. **This file holds sequencing and the authorization register. Nothing else.**

⛔ **It does not restate the step files.** What each node does, what it asserts and why lives in `00_HU_OVERVIEW_V2.md` through `13_HU_REGENERATE_V1.md`. If a rule appears both here and there, there wins and the copy here is a bug.

> **Why V3.** V2 was written before this folder had been read, and restated files 00–13 at length. Four of its claims were wrong: it asked which Slack channel and ntfy topic to use (settled — share QDE's), asked Drive trigger versus form trigger (settled — Drive, file 01), said "four platforms, not five" (five copy outputs, four Metricool drafts), and listed retiring V14/V15 as outstanding (already done).

---

## Phase A — Access and safety net

- **A1.** No n8n API key needed. The `/rest/…` surface works through an authenticated browser session with the `browser-id` header from `localStorage.getItem('n8n-browserId')`. See file 00, flag 6.
- **A2.** Confirm the QDE source lane against the table in file 00 — four workflows plus the shared `Next open slot`, with the node counts listed there.
- **A3.** Back up all five. Export JSON to `n8n_backups/`, **and** duplicate each in n8n as an inactive `BACKUP <reason> <date> — <name>`, matching the existing convention. One such point already exists: `BACKUP pre-warn-gate 2026-09-19 — QDE YouTube Publish v1` (`OrZf3nausd7iSRqd`).
- **A4.** ⭐ **Read the HU channel ID back from YouTube.** `yutu_hu channel-list` must return `UCG-DLule9ZSStBdc5gSEoCw`. Anything else, or a 401, stop and re-mint. This one check prevents the entire wrong-channel failure class (file 09, B1).
- **A5.** Confirm `hu_client_secret.json` and `hu.token.json` exist and are readable by the worker's user.

## Phase B — HU infrastructure

- **B1.** Create the HU assets folder and the HU upload queue with `done/` and `failed/` (file 00 config, file 09). Record the IDs in file 00.
- **B2.** Confirm the n8n Drive credential can actually see `1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv`. Same account does not guarantee same sharing.
- **B3.** Patch `worker.py` for brand-aware credentials and the post-upload channel assertion (file 09, B1). Back up first. Restart and **confirm the new PID is running the new file** — launchd respawns automatically.
- **B4.** ⭐ **Prove the patch on a QDE job before any HU job exists.** No `brand` key, must still reach the QDE channel, new assertion must pass. If QDE breaks, stop.

## Phase C — Clone

- **C1.** `POST /rest/workflows` for each of the four, HU name, **`active: false`**. `Next open slot` is **shared, not cloned** (file 10).
- **C2.** Repoint every sub-workflow reference in the HU orchestrator at the new HU IDs. A missed one means the HU orchestrator silently calls the QDE sub-workflow — the same failure class as B1.
- **C3.** Set `Betty — HU Error Handler v1` as `settings.errorWorkflow` on the other three.
- **C4.** Replace the trigger per file 01 — Drive trigger on the HU Ready folder, matched on **folder ID**, direct children, mime `video/*`.
- **C5.** Fix `brand = "HU"` in the queue-row lookup. It is the trigger, not a lookup (file 01).
- **C6.** Keep both hard gates exactly as QDE has them — `Video found?` and the column AM cross-check. Both are proven working. Update the folder ID inside the `Video found?` error text.
- **C7.** ⭐ **Clone the ⚠️ incomplete-publish branch** (file 09). Four nodes off `YT Result`, non-blocking.
- **C8.** Remove the LinkedIn draft **and** the `linkedin` key from the LLM schema (file 10).

## Phase D — Config swap and publish

- **D1.** Apply the config block in file 00.
- **D2.** ⭐ **Grep the whole HU JSON for QDE leakage before publishing.** Config alone will not catch it — the ntfy URL, Slack channel, prompt paths and queue folder are hardcoded per node (file 00). Any hit is a bug:

  `132glSPY` · `1V-piQzAW` · `1rm7hEFT` · `6268508` · `UCrpyI5SkE` · `qde-pipeline-bhi` · `qde_legal_description` · `qde-brand.md` · `qde_client_secret` · `HandwritingExpertUSA` · `bartbaggett.com` · `Thumbnail_Brand_SOP_QDE` · `1-800-980-9030`

  ⚠️ `qde-celebrity-post-review` is **not** a leak — the Slack channel and ntfy topic are shared deliberately (file 12). Prefix, do not repoint.

- **D3.** n8n expression hygiene: one `}}` per expression, no consecutive braces, no apostrophes inside single-quoted strings. Validate as *n8n text*, not JavaScript.
- **D4.** ⭐ **Publish, then verify against `activeVersion`.** A PATCH updates the draft only. See file 00's hard rules — this is the mistake that was made on 2026-09-19.

## Phase E — Thumbnail lane

Per file 07. Delete the image-generation node, emit a build job, prove the Mac-side build standalone, wire the resume webhook. **Blocked on Bart's ruling** on the V15/brand-kit contradiction.

## Phase F — Copy lane

Per file 05. Repoint `Fetch description prompt` and `Fetch brand kit` at the HU files, rebuild the schema for five outputs minus LinkedIn, add the HU `Preflight` assertions from file 11. The Shorts gap is the one outstanding prompt-side item.

## Phase G — Dry run, workflow inactive

Manual execution against an HU video **already published**, so nothing new reaches YouTube. Assert node by node per file 11. Do not write a real Metricool draft — disconnect that leg or use a date you will delete.

## Phase H — One real video, end to end

One HU video into the HU Ready folder, **column AM filled first**. Trigger manually rather than waiting on the poll. Verify at the destination per file 12 — and note that caption `serving` and a confirmed thumbnail are now achievable, so anything less is a real failure rather than the known-broken baseline.

## Phase I — Activate

Sub-workflows first, then the orchestrator. Confirm from `publication-status` and a later execution's `workflowData` that the live code is the new code.

## Phase J — Document

Record the created folder IDs in file 00. Back up the four HU workflows. Close the flags this build resolves.

---

## 📌 PINNED — Authorization and destination binding: check EVERY stop

**Bart's standing instruction.** Most credentials are shared between the lanes; most destinations are not. A shared token pointed at an unchanged destination ID is how HU content lands on a QDE channel — and because everything stages private or draft, it would not be obvious.

| # | Stop | Credential | Destination binding | Risk if missed |
|---|---|---|---|---|
| 1 | YouTube upload / thumbnail / captions (Mac worker) | **DIFFERENT** — `hu_client_secret.json` + `hu.token.json` | Channel `UCG-DLule9ZSStBdc5gSEoCw` | **HU video on the QDE channel.** Still hardcoded — file 09, B1 |
| 2 | Metricool drafts | **SAME** token, **SAME** `userId 4831552` | **DIFFERENT** `blogId` — HU `6267975`, QDE `6268508`; different per-network connections | **HU posts on the QDE calendar.** The API call succeeds either way |
| 3 | Google Drive | likely SAME OAuth — unconfirmed | **DIFFERENT** folder IDs at four points: ready, assets, upload queue, done/failed | Files into QDE's assets; jobs into QDE's queue |
| 4 | Google Sheets | SAME | SAME sheet, **read-only** | A write corrupts dropdown-validated columns |
| 5 | rclone `gdrive:` | SAME token | **DIFFERENT** queue path | HU job claimed off the QDE queue |
| 6 | Gemini (thumbnail plate) | Mac `.env` — 403 from n8n Cloud and the sandbox | n/a | Silent thumbnail failure off-Mac |
| 7 | OpenAI (text) | SAME | **DIFFERENT prompt + brand file URLs** | HU video described in QDE legal voice, with QDE credentials in the copy |
| 8 | Slack | SAME workspace token | **SAME channel, deliberately** — lane named in the first line | A notice nobody can attribute to a lane |
| 9 | ntfy | none | **SAME topic, deliberately** — lane prefix in the body | Same, on mobile |
| 10 | GitHub raw | none | **DIFFERENT** prompt + brand paths | Wrong brand rules applied silently |
| 11 | Descript | SAME | n/a | — |

**Prove each destination by reading back from it, never by a successful call.** Two that are cheap and settle the two worst risks:

- `yutu_hu channel-list` → must be `UCG-DLule9ZSStBdc5gSEoCw`, before any upload is wired.
- Create one throwaway HU Metricool draft, confirm via `getScheduledPosts` that it is on `6267975` and **not** on `6268508`, then delete it.

---

## Acceptance criteria

HU is not done until every one of these is proven **at the destination**:

1. A file in the HU Ready folder starts the HU workflow and nothing else.
2. A file in the QDE folder does not start the HU workflow, and vice versa.
3. The video is on `UCG-DLule9ZSStBdc5gSEoCw`, **private**, never on `UCrpyI5SkE075HJaFyxO_ozQ`.
4. The attached thumbnail is 16:9, on-brand, with real trait handwriting from the library.
5. The caption track reads **`serving`** — not "inserted", not `syncing`.
6. Four Metricool drafts on blogId `6267975`, `draft: true`, four **distinct** captions.
7. Zero `graphology`/`graphologist` outside hashtags; zero QDE credentials; CTA to HandwritingUniversity.com only.
8. A deliberate failure reaches Slack and ntfy, prefixed `HU`, with the `Error to Correct:` line.
9. The ⚠️ incomplete-publish branch fires when thumbnail or captions do not land.
10. No write of any kind touches the master Workflow spreadsheet.

## Still needing Bart

| # | Question | Blocks |
|---|---|---|
| 1 | The V15 thumbnail bans on "PIL hand-composite" and "red" contradict the brand kit. | Phase E |
| 2 | `hu_description_prompt_V3.md` has no Shorts variant — what shape, and what length for a three-minute HU Short? | Phase F |
| 3 | Collegiate FLF commercial licence still `[TO VERIFY]`. | Not blocking; scales with this |
| 4 | Sequencing — clone now, or run two or three more QDE videos first to confirm today's fixes hold? | Start date |

## What this runbook does not claim

- HU-side credentials, fonts and brand-kit contents have **not** been verified this session.
- `UCG-DLule9ZSStBdc5gSEoCw` comes from the Metricool brand record, not a YouTube API read. A4 settles it.
- Per-platform caption distinctness has never been proven on any run, either lane.
- The QDE fixes of 2026-09-19 are proven on **one** live run. One run is evidence, not a track record.
