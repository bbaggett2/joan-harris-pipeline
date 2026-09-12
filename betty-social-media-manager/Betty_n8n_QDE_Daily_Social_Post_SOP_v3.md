# Betty — n8n QDE Daily Social Post (Metricool drafts)
**Version:** v3 · **Prepared:** 2026-09-12 · v3: queue sheet ID set (`14pkeLjlH5SFf4X_DwafTCJlgdKRNOcY-p_AAbZjxfec`, first tab, gid 0); v2: LinkedIn confirmed as Bart's personal profile; Metricool userId filled in · **Lane:** Handwriting Experts Inc. / QDE only
**Governing pipeline:** `joan-supervising-agent/QDE_Video_Publishing_Pipeline_V11.md` (HARD RULES and Phase 8 apply here unchanged — this SOP restates nothing, it links)
**Files:** `Betty_n8n_QDE_Daily_Social_Post_v3.json` (import into n8n) · `QDE_Post_Queue_seed_v1.csv` (first five rows for the Google Sheet)

---

## What it does

Every weekday at 7:00 AM Central, n8n:

1. Reads the **QDE_Post_Queue** Google Sheet and takes the first row whose `status` is `READY`.
2. Runs Betty's preflight on the caption — phone number present, `HandwritingExpertUSA.com` present, `HandwritingExpert.com` absent, no "link in bio," no "graphology," no `[TO VERIFY]` or `****` marker, no outcome language, `facts_need_verify` is `NO`. Any failure → row marked `BLOCKED`, reviewer pinged on Slack, nothing sent.
3. If the row has an `image_url`, uses it. If not, sends `image_prompt` to Gemini, saves the PNG to a Drive folder, shares it by link, and uses that URL.
4. Creates **two Metricool posts, both `draft: true`, one for Facebook, one for LinkedIn**, each with the same caption and the image. No publish time of any consequence: a placeholder date is sent because Metricool requires one, and a draft cannot fire.
5. Marks the row `STAGED` with the Metricool ids and image URL, and posts the planner links to the reviewer's Slack channel.

The reviewer approves by scheduling the drafts in the Metricool planner. That is the approval — same gate as the video pipeline. **The workflow never schedules and never publishes.**

Empty queue → one Slack notice, no action.

---

## Why faces are a human step

A fully automated run **cannot** composite a licensed photograph of a real person into a Gemini design, and Gemini will generally refuse to generate a real person's likeness. So the queue carries a `photo_required` column:

| `photo_required` | `image_url` | What happens |
| :--- | :--- | :--- |
| `YES` | empty | **BLOCKED.** Salvatore builds the face composite by hand, uploads it, pastes the URL into `image_url`, sets `status` back to `READY`. |
| `YES` | filled | Uses the pre-built image. |
| `NO` | empty | Gemini generates the no-face document-and-prop version from `image_prompt`. |
| `NO` | filled | Uses the pre-built image. |

All five famous-case posts in the seed CSV are `photo_required = YES`, so the first run of each is a hand-built graphic. The "What I Look For" and attorney-education series can run `NO` and be fully automatic.

---

## Google Sheet — `QDE_Post_Queue`

Live at `https://docs.google.com/spreadsheets/d/14pkeLjlH5SFf4X_DwafTCJlgdKRNOcY-p_AAbZjxfec` — the workflow reads the **first tab (gid 0)** by id, so the tab can be named anything.

Columns, in this order (the seed CSV has them):

`post_id · title · status · headline · gold_word · subline · torn_note · face_source · photo_required · image_prompt · image_url · caption · facts_need_verify · fact_status · metricool_fb_id · metricool_li_id · date_staged · notes`

`status` values: `HOLD` (not ready — facts unverified or copy not final) · `READY` (Betty may take it) · `STAGED` (drafts exist in Metricool) · `BLOCKED` (preflight failed, see `notes`) · `PUBLISHED` (reviewer sets this after scheduling; optional).

Only `READY` rows are ever touched. Order in the sheet is the posting order — the workflow takes the first `READY` row it finds.

The seed CSV loads Post 1 (Franklin) as `READY` and Posts 2–5 as `HOLD` because their fact-status lines still carry ⚠️ items. Flip each to `READY` after the ⚠️ items are cleared **and** the face composite URL is in `image_url`.

---

## Credentials to set in n8n (four)

| Credential | Type | Value |
| :--- | :--- | :--- |
| Google Sheets — Baggett | Google OAuth2 | an account with edit access to the queue sheet (⚠️ the Drive connector in this chat could not open it — check which Google account owns it and use that one in n8n) |
| Google Drive — Baggett | Google OAuth2 | same account; write access to the graphics folder |
| Gemini API key | Header Auth | header name `x-goog-api-key`, value = the key |
| Metricool | Header Auth | header name `X-Mc-Auth`, value = the API token from Metricool Settings → API |
| Slack — Baggett | Slack OAuth2 | posts to the reviewer channel |

Then fill the **Config** node: Drive folder id and reviewer Slack channel (sheet id is already set). `blogId` `6268508` and `userId` `4831552` are already set (read from the live Metricool account 2026-09-12).

---

## [TO VERIFY] before the first live run

1. **Metricool REST endpoint.** The workflow calls `POST https://app.metricool.com/api/v2/scheduler/posts?blogId=…&userId=…` with header `X-Mc-Auth`. That is Metricool's documented public API pattern as I understand it, and the request body matches the `createScheduledPost` schema Betty already uses through the MCP connector (`draft`, `providers`, `facebookData`, `linkedinData`, `publicationDate`, `media`). Confirm the URL against Metricool's API docs for the account. If the response shape differs, the only nodes that read it are "Mark row STAGED" and "Staged — tell reviewer" (they look for `data.id` and `data.plannerUrl`).
2. **Does a `draft: true` post land as a draft in the planner** (pipeline OPEN FLAG #3 applies here too). Run once with a test caption and check before enabling the schedule.
3. **Is Google Drive linked in the Metricool account** (pipeline OPEN FLAG #2). If not, the Drive URL fails with `Failed to normalize media` and the FTP bridge from Phase 8 has to replace the "Upload PNG to Drive" step.
4. **LinkedIn — resolved.** Read from the live Metricool account 2026-09-12: the QDE brand's LinkedIn connection is now `urn:li:person:nFfhG_fIiZ`, i.e. **Bart's personal profile**, not the company page. The LinkedIn draft this workflow creates therefore lands on Bart's profile, which is exactly where this series belongs. Two consequences: (a) the company page (`urn:li:organization:91412902`) is no longer connected to this brand, so the company reshare is a manual step in LinkedIn or needs a second Metricool brand; (b) `QDE_Video_Publishing_Pipeline_V11.md` line 88 still says the organization URN — bump it to V12 and correct the value.
5. **Gemini image model name.** Config uses `gemini-2.5-flash-image`. Confirm the current model id in the Gemini docs; the request body (`responseModalities: ["IMAGE"]`) is the same either way.
6. **Palette conflict.** `brands/qde-brand.md` says navy `#10142E` / gold `#FFE455` (flagged unverified). `salvatore-art-department/Salvator_AI_Graphics_SOP_v1.md` §3A says navy `#1B2A4A` / gold `#C9A84C`. The image prompts in the seed use the brand file's values. Pick one and fix the other file — never two live.
7. **Two nodes never ran in this environment.** The JSON was written by hand, not exported from a working n8n. Expect to open each node once on import and confirm the field mappings render; the Google Sheets and Drive nodes in particular change parameter shapes between n8n versions.

---

## What this workflow deliberately does not do

- It does not write copy. Every word comes from the sheet, which comes from the approved pack. If copy needs a change, change the sheet.
- It does not call Claude. There is nothing for a model to decide at run time; adding one would be adding a place for the copy to drift.
- It does not touch Instagram, TikTok, YouTube, or GBP. Two providers, two calls.
- It does not delete anything.
- It does not run for Handwriting University or Bart Allan Baggett. Wrong lane = don't import it there.

---

## Runbook

**First run (manual):** Import JSON → set credentials → fill Config → put one `READY` test row in the sheet with `photo_required = NO` and a harmless caption that still passes preflight → click "Test workflow" → confirm two drafts appear in the Metricool planner and the sheet row reads `STAGED` → delete the test drafts in Metricool → set the row to `HOLD`.

**Go live:** Activate the workflow. Keep at least one `READY` row ahead of it or you get the empty-queue Slack notice every morning.

**Change the time:** edit the cron in "Daily 7:00 CT" (`0 7 * * 1-5`, Central).

**Stop it:** deactivate the workflow in n8n. Drafts already created stay drafts.
