# Betty — n8n QDE Daily Social Post (Metricool drafts)
**Version:** v5 · **Prepared:** 2026-09-13 · v5: **image engine is OpenAI `gpt-image-1`, not Gemini** — one pass renders the famous person, the headline type, the note and the document (the ChatGPT-made Aretha Franklin and Howard Hughes graphics are the approved standard; Gemini no-face graphics are not approved); one post per weekday via `publish_date`; captions clean, flags in `notes`; status vocabulary READY/STAGED/PUBLISHED/ERROR. v4: **all pre-draft human stops removed** — the reviewer's only touchpoint is the draft in Metricool; preflight now repairs or flags, it never blocks; `photo_required` no longer holds a row; `facts_need_verify` and `[TO VERIFY]` travel with the draft as flags. v3: queue sheet ID set; v2: LinkedIn confirmed as Bart's personal profile · **Lane:** Handwriting Experts Inc. / QDE only
**Governing pipeline:** `joan-supervising-agent/QDE_Video_Publishing_Pipeline_V12.md` — HARD RULES apply unchanged. ⚠️ V12 lines 204 and 512 ("any `[TO VERIFY]` still present is a blocker") describe the gate *before publication*. In this workflow nothing is published; the reviewer is that gate. Bump V12 → V13 with one sentence: "For Betty's draft workflow, `[TO VERIFY]` blocks scheduling, not drafting."
**Files:** `preflight_checks_v4.js` (live Code node) · `QDE_Post_Queue_seed_v1.csv` (historical; the live sheet is the source of truth)

---

## The one rule this version exists for

**No human touches a post before it is a draft in Metricool.** The pipeline's job is to get every READY row into the reviewer's planner as two drafts, every morning, with every known problem written on the draft. The reviewer then does one of three things in Metricool: schedule it (approval), fix it and schedule it, or delete it. That is the entire human role. Anything in a prior version that said "BLOCKED — a human must do X first" is gone.

The only two things that stop a run: **the queue has no READY row**, or **an API call fails** (Sheets, Drive, Gemini, Metricool). Both post one Slack notice. Neither asks a human to prepare anything.

---

## What it does

Every weekday at 7:00 AM Central, n8n:

1. Reads **QDE_Post_Queue** (first tab, gid 0) and takes the first row whose `status` is `READY`.
2. Runs **preflight** on the caption. Preflight has two outcomes per check — **repair** or **flag** — and no third. See the table below. It never sets `BLOCKED`.
3. Resolves the image, in this order, with no gap a human has to fill:
   - `image_url` filled → use it as-is (a hand-approved graphic).
   - `image_url` empty → send `image_prompt` to **OpenAI `gpt-image-1`** (`POST https://api.openai.com/v1/images/generations`, `size 1024x1536`, `quality high`, `moderation low`, `output_format png`), decode the base64, save the PNG to the Drive folder, share by link, use that URL. The prompt **names the famous person and describes them** (see "Image prompts" below); the model renders the face, the headline with its gold word, the sub-line, the torn note and the document in one pass. `photo_required` and `FACE PENDING` are retired — every row gets a face.
4. Picks the **publish slot**: the next weekday at 9:00 AM Central that no other QDE post already holds. Never the same day as another post — **posts are 24 hours apart, one per weekday**, whether the row ran on schedule or someone hit Execute three times in an evening. Rule: read the `publish_date` column of every `STAGED` and `PUBLISHED` row; take the latest; add one weekday (skip Sat/Sun); if that is in the past, use the next weekday from today. Write it to the row's `publish_date`.
5. Creates **two Metricool posts, both `draft: true`**, one Facebook, one LinkedIn, same caption, same image, at that slot. A draft cannot fire; the date is where it will land when the reviewer schedules it, so the reviewer only has to click, not re-date.
6. Marks the row `STAGED` with the Metricool ids, image URL, publish_date and the flag list, and posts one Slack message to `#qde-celebrity-post-review` with the planner links and the flags.

**The workflow never schedules and never publishes.** Scheduling in the planner is the approval.

---

## Preflight — repair or flag, never block

| Check | Old (v3) | New (v4) |
| :--- | :--- | :--- |
| `HandwritingExpert.com` in caption | BLOCK | **Repair** → replace with `HandwritingExpertUSA.com` |
| Phone `1-800-980-9030` missing | BLOCK | **Repair** → append the standard CTA block (phone + both owned domains) |
| `HandwritingExpertUSA.com` missing | BLOCK | **Repair** → same CTA append |
| "link in bio" / cross-platform pointer | BLOCK | **Repair** → delete the sentence; **flag** `POINTER REMOVED` |
| "graphology" / "graphologist" | BLOCK | **Flag** `BANNED TERM` (reviewer edits in Metricool — an agent never rewrites Peggy's copy) |
| `[TO VERIFY]` or `****` marker in caption | BLOCK | **Flag** `TO VERIFY IN COPY` — marker left in place so the reviewer sees exactly where |
| Outcome language ("win your case", "guarantee") | BLOCK | **Flag** `OUTCOME LANGUAGE` |
| `facts_need_verify = YES` | BLOCK | **Flag** `FACTS UNVERIFIED` and copy `fact_status` into the Slack message |
| `photo_required = YES` and `image_url` empty | BLOCK, human composites face | **Generate** no-face graphic; **flag** `FACE PENDING` with `face_source` in the Slack message |
| Caption empty | BLOCK | The only preflight condition that skips the row: set `status = ERROR`, note "empty caption", Slack, **take the next READY row** |

Flags are written two places: the `notes` column of the sheet (`REVIEW: … | Face source: … | Fact status: …`) and the Slack message. **They are never written into the caption** — the draft in Metricool is clean, and the reviewer checks the worksheet before scheduling (Bart, 2026-09-12).

---

## Image prompts — what produces the approved look

The Aretha Franklin and Howard Hughes graphics were made in ChatGPT from a single descriptive prompt, and that is the standard. Gemini was told "no faces, empty photo zone" and produced graphics with a hole where the person belongs; those are not approved. Every `image_prompt` follows this shape (the five in the sheet were rewritten to it on 2026-09-13):

- *Cinematic editorial poster, 4:5 portrait, photoreal.* Deep navy ground `#10142E`, film grain, one warm light source.
- **The person, named and described**: who, which decade, expression, clothing, where in the frame. "Aretha Franklin, warm and smiling, mid-2000s, chin on her hand." "Howard Hughes in his aviator years, leather flight jacket, monochrome." For a face nobody knows (Kujau, Hofmann) describe the man — the model does not need the name to be right, it needs the description to be specific.
- **The headline, quoted, with the gold word named**: `headline "…" in white with only the word "…" in gold (#FFE455)`, then the sub-line quoted.
- **The document at the center** with its detail (the smiley in the A, the CONTESTED stamp, the cracked ink under the magnifier).
- **The torn cream notepad** with the `torn_note` bullets quoted verbatim.
- **Law-book spines** with 3–4 words, optional.
- Close with: *No logos, no other text.* For Hitler-diaries material add *No swastikas, no insignia.* For Hofmann add *No explosions, no religious symbols.*

Expect a Hughes-type face rather than a photograph of Hughes; that is acceptable. Expect one bad letter in ten renders; the reviewer regenerates by clearing `image_url` and setting the row back to `READY`.

## Regenerate image — the button

If the reviewer does not approve version 1 of a graphic, the procedure is two steps and no waiting:

1. In the sheet, type what should change into column **S `image_feedback`** on that row — *"Hughes looks too young; headline clipped on the right; lose the fountain pen."* Plain English. This column is required whenever version 1 is not approved; a regenerate with it empty is refused.
2. Press **Regenerate image** — the button on the n8n form at `…/form/regenerate-image` (also linked as *Regenerate image →* in every Slack STAGED message, with the row pre-filled). The form asks only for the `post_id`; it reads the feedback from column S.

What the button does (workflow **"Betty — Regenerate image"**, Form Trigger, ~9 nodes, runs only when pressed):

- reads the row by `post_id`; stops with a message if `image_feedback` is empty;
- builds the revision prompt: the row's `image_prompt` + *"Revision notes from the reviewer (apply these, keep everything else): …S…"*;
- renders with `gpt-image-1` (same call as the daily workflow), saves the PNG to Drive, shares by link;
- **updates both existing Metricool drafts in place** (`metricool_fb_id`, `metricool_li_id`) with the new image — never creates new drafts;
- writes the new `image_url`, bumps an image version counter in `notes` (*"image v2 — <feedback>"*, so the history stays on the row), clears column S;
- posts *"QDE-FC-4 image regenerated (v2) — FB: link · LI: link — Regenerate again →"* to `#qde-celebrity-post-review`;
- ends the form page with the new image on it and a *Regenerate again* link.

The reviewer approves by scheduling the draft in Metricool. Version 1 is never overwritten in Drive — each render is a new file, so an earlier version can be put back by pasting its URL into `image_url`. Status is untouched by the button: the row stays `STAGED` throughout.

## Why faces no longer hold a row

v3 stopped on `photo_required = YES` because Gemini would not render a real person. v4 shipped a no-face graphic and asked a human to add the face later. v5 removes the problem: `gpt-image-1` renders the person in the same pass as the rest of the graphic, so nothing waits on anyone.

| `image_url` | v5 behaviour |
| :--- | :--- |
| empty | `gpt-image-1` renders the full graphic from `image_prompt`, person included |
| filled | Use the image as-is (reviewer-approved or hand-built) |

`photo_required` stays in the sheet for history but nothing reads it.

---

## Google Sheet — `QDE_Post_Queue`

Live at `https://docs.google.com/spreadsheets/d/14pkeLjlH5SFf4X_DwafTCJlgdKRNOcY-p_AAbZjxfec`, first tab (gid 0), read by id.

Columns (A–T): `post_id · title · status · headline · gold_word · subline · torn_note · face_source · photo_required · image_prompt · image_url · caption · facts_need_verify · fact_status · metricool_fb_id · metricool_li_id · date_staged · notes · image_feedback · publish_date`. Column **S `image_feedback`** (header: *IMAGE FEEDBACK — required if version 1 is not approved*) is the reviewer's instruction to the regenerate button. Column **T `publish_date`** (`YYYY-MM-DD`) is the slot Betty gave the drafts; it is how the next run knows where the calendar ends. Both added 2026-09-13.

`status` values — exactly four, uppercase, the filter is case-sensitive: `READY` (Betty takes it) · `STAGED` (drafts exist in Metricool) · `PUBLISHED` (reviewer sets after scheduling) · `ERROR` (an API call or empty caption failed; see `notes`; fix and set back to `READY`). A blank cell means Peggy is still writing.

**`BLOCKED` is retired.** Any row currently `BLOCKED` should be set back to `READY`; v4 will stage it with flags.

Only `READY` rows are touched. Sheet order is posting order. **Do not set rows to `HOLD` to wait for a face or a fact check** — set them `READY` and let the flags carry the work to the draft.

---

## n8n workflow changes from v3 (what to edit on import, or what the v4 JSON contains)

1. **"Read queue (READY rows)"** — Resource *Sheet Within Document*, Operation *Get Row(s)*, Document by ID, Sheet by ID `0`, filter `status = READY`, *Return only First Matching Row* on. (v3's live instance had drifted to Document → Create, which created an empty spreadsheet every run and staged nothing.)
2. **"Preflight checks"** (Code node, *Run Once for All Items*) — `preflight_checks_v4.js` in this folder is the live code. Repair-and-flag: returns the repaired, mojibake-fixed `caption`, `flags[]`, `preflight_problems`, `face_pending`, and `preflight_ok` (false only for an empty caption).
3. **"Preflight passed?"** (IF) — `{{ $json.preflight_ok }}` is true, with *Convert types where required* ON (without it the IF throws a type error). Only an empty caption goes to the ERROR branch.
4. **"Has image already?"** (IF) — unchanged; its false branch is reached for every empty `image_url`.
4a. **"Gemini — generate graphic"** → rename **"OpenAI — generate graphic"**: HTTP POST `https://api.openai.com/v1/images/generations`, Header Auth credential "OpenAI Images" (`Authorization: Bearer …`), JSON body `{"model":"gpt-image-1","prompt":{{ $json.image_prompt }},"size":"1024x1536","quality":"high","moderation":"low","output_format":"png","n":1}`. The response's `data[0].b64_json` feeds the existing "Base64 → PNG" node (change its source path from Gemini's `candidates[0].content.parts[…].inlineData.data` to `data[0].b64_json`). Everything after is unchanged.
5. **"Mark row BLOCKED" / "Blocked — tell reviewer"** — renamed **"Mark row ERROR" / "Error — tell reviewer"** and reached only from API failures (set *On Error → Continue (error output)* on the Gemini, Drive, and both Metricool HTTP nodes and wire their error outputs here) and the empty-caption case.
6. **"Assemble post"** — computes the publish slot (item 4 above) from the sheet's `publish_date` column: the Read-queue node's sibling **"Read scheduled dates"** (Get Row(s), filter `status = STAGED` or `PUBLISHED`, no first-row limit) feeds it; Assemble post takes `max(publish_date) + 1 weekday`, falling back to the next weekday from today at 09:00 America/Chicago, and puts it in both bodies' `publicationDate`. **The v3 code set every draft to the same next-weekday 09:00, which is why a batch of manual runs stacked six drafts on one morning.** Uses the clean `caption`; body includes `saveExternalMediaFiles: true` so Metricool ingests the Drive image instead of storing a dead link. Wiring: Assemble post → Facebook DRAFT → LinkedIn DRAFT → Mark row STAGED (serial, so `$('Metricool — Facebook DRAFT')` is on the path). "Mark row STAGED" writes the flag summary into `notes`.
7. **"Staged — tell reviewer"** — message format: `QDE daily post STAGED — <post_id> (<headline>). FB: <link> · LI: <link>. Flags: <list or "none">. Fact status: <fact_status if FACTS UNVERIFIED>. Regenerate image → <form URL>?post_id=<post_id>`.
8. **New workflow "Betty — Regenerate image"** — see "Regenerate image — the button" above.

---

## Credentials (unchanged from v3)

Google Sheets OAuth2 · Google Drive OAuth2 (same account) · OpenAI `Authorization: Bearer <key>` header (Header Auth credential "OpenAI Images") · Metricool `X-Mc-Auth` header · Slack OAuth2. Config node: sheet id, gid `0`, Drive folder `12vSyv-55AgDEz1YNuf8SJPStcKUF-_4w`, Slack channel `qde-celebrity-post-review`, `blogId 6268508`, `userId 4831552`, model `gpt-image-1` (the Gemini credential and `gemini_image_model` config stay for HU thumbnails only).

---

## [TO VERIFY] before relying on v4

1. Metricool `draft: true` lands in the planner as a draft (pipeline OPEN FLAG #3) — confirmed in principle by the v3 test on 2026-09-12 reaching the Metricool nodes; confirm the drafts are visible in the planner.
2. Google Drive linked in Metricool (OPEN FLAG #2) — if `Failed to normalize media`, the FTP bridge replaces "Upload PNG to Drive".
3. `gpt-image-1` via the API renders named public figures as freely as the ChatGPT app does — confirmed for nobody yet; the first v5 run on QDE-FC-4 is the test. If it refuses, drop the name and keep the description (Kujau/Hofmann prompts already work that way).
4. V12 → V13 one-line amendment described in the header.

---

## What this workflow deliberately does not do

- It does not write or rewrite copy. Repairs are limited to the mechanical fixes in the preflight table (domain swap, CTA append, pointer deletion). Everything else is a flag.
- It does not call Claude at run time.
- It does not wait for a human. Ever. If it cannot finish a row, it says so in Slack and moves on.
- It does not schedule, publish, or delete.
- It does not run for Handwriting University or Bart Allan Baggett.

---

## Runbook

**Go live:** set every `BLOCKED` row to `READY`, activate the workflow. Next morning: two drafts for the top row, dated to the next open weekday slot (one post per weekday, 24 hours apart), one Slack message with flags. Review in Metricool only.

**Stop it:** deactivate in n8n. Existing drafts stay drafts.

**Change the time:** edit the cron in "Daily 7:00 CT" (`0 7 * * 1-5`, Central).
