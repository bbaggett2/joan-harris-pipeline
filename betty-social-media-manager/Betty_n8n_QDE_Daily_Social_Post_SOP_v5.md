# Betty — n8n QDE Daily Social Post (Metricool drafts)
**Version:** v6 · **Prepared:** 2026-09-14 · v6: **image prompts are positive-only** — never list what should not appear (gpt-image-1 renders the words in a "no X" instruction; the QDE-FC-3 v2 render put swastikas on the diaries and leaked "Postwastikas no insignia" into the torn note); **no invented faces** — a named public figure is rendered, an unknown subject (Kujau, Hofmann, Cosey) gets a document-led composition with no person; status vocabulary stays at four values and the Regenerate button is the only regeneration path; OpenAI credential is the predefined n8n OpenAI credential, not Header Auth. v5: image engine is OpenAI `gpt-image-1`, not Gemini; one post per weekday via `publish_date`; captions clean, flags in `notes`; status vocabulary READY/STAGED/PUBLISHED/ERROR. v4: all pre-draft human stops removed — the reviewer's only touchpoint is the draft in Metricool; preflight repairs or flags, never blocks. v3: queue sheet ID set; v2: LinkedIn confirmed as Bart's personal profile · **Lane:** Handwriting Experts Inc. / QDE only
**Governing pipeline:** `joan-supervising-agent/QDE_Video_Publishing_Pipeline_V12.md` — HARD RULES apply unchanged. ⚠️ V12 lines 204 and 512 ("any `[TO VERIFY]` still present is a blocker") describe the gate *before publication*. In this workflow nothing is published; the reviewer is that gate. Bump V12 → V13 with one sentence: "For Betty's draft workflow, `[TO VERIFY]` blocks scheduling, not drafting."
**Files:** `preflight_checks_v4.js` (live Code node) · `QDE_Post_Queue_seed_v1.csv` (historical; the live sheet is the source of truth)

---

## The one rule this version exists for

**No human touches a post before it is a draft in Metricool.** The pipeline's job is to get every READY row into the reviewer's planner as two drafts, every morning, with every known problem written on the draft. The reviewer then does one of three things in Metricool: schedule it (approval), fix it and schedule it, or delete it. That is the entire human role. Anything in a prior version that said "BLOCKED — a human must do X first" is gone.

The only two things that stop a run: **the queue has no READY row**, or **an API call fails** (Sheets, Drive, OpenAI, Metricool). Both post one Slack notice. Neither asks a human to prepare anything.

---

## What it does

Every weekday at 7:00 AM Central, n8n:

1. Reads **QDE_Post_Queue** (first tab, gid 0) and takes the first row whose `status` is `READY`. (Rejected images are not re-staged by this workflow — they go through the Regenerate button, below, and the row stays `STAGED`.)
2. Runs **preflight** on the caption. Preflight has two outcomes per check — **repair** or **flag** — and no third. See the table below. It never sets `BLOCKED`.
3. Resolves the image, in this order, with no gap a human has to fill:
   - `image_url` filled → use it as-is (a hand-approved graphic).
   - `image_url` empty → send `image_prompt` to **OpenAI `gpt-image-1`** (`POST https://api.openai.com/v1/images/generations`, `size 1024x1536`, `quality high`, `moderation low`, `output_format png`), decode the base64, save the PNG to the Drive folder, share by link, use that URL. If the subject is a **famous public figure** the prompt names and describes them and the model renders the face with the headline, sub-line, torn note and document in one pass. If the subject is **not famous** (a forger nobody would recognise) the prompt contains **no person** — the document and the evidence carry the frame. `photo_required` and `FACE PENDING` are retired.
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
| `photo_required = YES` and `image_url` empty | BLOCK, human composites face | Retired in v5 — nothing reads `photo_required` |
| Caption empty | BLOCK | The only preflight condition that skips the row: set `status = ERROR`, note "empty caption", Slack, **take the next READY row** |

Flags are written two places: the `notes` column of the sheet (`REVIEW: … | Face source: … | Fact status: …`) and the Slack message. **They are never written into the caption** — the draft in Metricool is clean, and the reviewer checks the worksheet before scheduling (Bart, 2026-09-12).

---

## Image prompts — what produces the approved look

The Aretha Franklin and Howard Hughes graphics were made in ChatGPT from a single descriptive prompt, and that is the standard. Gemini was told "no faces, empty photo zone" and produced graphics with a hole where the person belongs; those are not approved. Every `image_prompt` follows this shape:

- *Cinematic editorial poster, 4:5 portrait, photoreal.* Deep navy ground `#10142E`, film grain, one warm light source.
- **The subject — two cases, decide before writing:**
  - **Famous public figure** (Franklin, Hughes, Lincoln, Ben Franklin): name them and describe them — who, which decade, expression, clothing, where in the frame. "Aretha Franklin, warm and smiling, mid-2000s, chin on her hand." "Howard Hughes in his aviator years, leather flight jacket, monochrome." Expect a Hughes-type likeness rather than a photograph of Hughes; that is acceptable. The model cannot fetch or place a real photograph — if a specific public-domain photo is wanted (Library of Congress Hughes, the Gardner Lincoln), that is a Canva composite by a human, done *after* the draft exists, by pasting the finished file's URL into `image_url`.
  - **Not famous** (Kujau, Hofmann, Cosey — a forger nobody would recognise): **no person in the frame.** An invented face reads as a stock-photo stranger and, on grim material, sets the wrong tone (the QDE-FC-3 v2 render was a grinning man holding a Hitler diary). Lead with the document and the evidence: the stacked diaries, the cracked ink under the magnifier, the 1983 *Stern* cover, the pay warrant half-slipped into an overcoat pocket. Expression and mood come from light and composition, not a face.
- **The headline, quoted, with the gold word named**: `headline "…" in white with only the word "…" in gold (#FFE455)`, then the sub-line quoted.
- **The document at the center** with its detail (the smiley in the A, the CONTESTED stamp, the cracked ink under the magnifier).
- **The torn cream notepad** with the `torn_note` bullets quoted verbatim, and the count stated: *"the note lists exactly these four bullets."*
- **Law-book spines** with 3–4 words, optional.
- **Period and setting, described positively.** Hitler diaries: *1980s black cloth-bound diaries with gothic-script initials on the covers, a Stern magazine cover from April 1983, a Hamburg newsroom, a paper-fibre slide under a lab magnifier.* Hofmann: *1985 Salt Lake City, a rare-document dealer's desk, the Salt Lake Temple silhouette distant and unlit through the window.* Cosey: *the Library of Congress reading room, 1929, brass lamp light.*
- **Close with what the text is, not what it isn't:** *The only text in the image is the headline, the sub-line, and the note bullets. Every cover and spine is plain cloth unless a title is quoted above.*

**Never write a "no …" instruction.** gpt-image-1 does not process negation reliably — it sees the noun and paints it. "No swastikas" produced swastikas; "no other text" produced a fifth bullet reading "Postwastikas no insignia, no logos." State what every surface *is* and the model has nothing to add. This applies to `image_prompt` in the sheet and to reviewer feedback in column S: write *"plain black covers"*, not *"remove the symbols."*

Hate symbols are never requested, even when the story is about them. The subject is the forgery, not the regime; period props carry the setting.

Expect one bad letter in ten renders. Regeneration is the button below — nothing else.

## Regenerate image — the button

If the reviewer does not approve version 1 of a graphic, the procedure is two steps and no waiting:

1. In the sheet, type what should change into column **S `image_feedback`** on that row — *"Hughes looks too young; headline clipped on the right; plain black covers on the diaries."* Plain English, phrased as what the picture should show. This column is required whenever version 1 is not approved; a regenerate with it empty is refused.
2. Press **Regenerate image** — the button on the n8n form at `…/form/regenerate-image` (also linked as *Regenerate image →* in every Slack STAGED message, with the row pre-filled). The form asks only for the `post_id`; it reads the feedback from column S.

Do **not** clear `image_url` or set the row back to `READY` to get a new image — that hands the row to the daily workflow, which re-stages it and creates a second pair of Metricool drafts. The button updates the existing drafts in place.

What the button does (workflow **"Betty — Regenerate image (button)"**, Form Trigger, ~9 nodes, runs only when pressed):

- reads the row by `post_id`; stops with a message if `image_feedback` is empty;
- builds the revision prompt: the row's `image_prompt` + *"Revision notes from the reviewer (apply these, keep everything else): …S…"*;
- renders with `gpt-image-1` (same call as the daily workflow), saves the PNG to Drive, shares by link;
- **updates both existing Metricool drafts in place** (`metricool_fb_id`, `metricool_li_id`) with the new image — never creates new drafts;
- writes the new `image_url`, bumps an image version counter in `notes` (*"image v2 — <feedback>"*, so the history stays on the row), clears column S;
- posts *"QDE-FC-4 image regenerated (v2) — FB: link · LI: link — Regenerate again →"* to `#qde-celebrity-post-review`;
- ends the form page with the new image on it and a *Regenerate again* link.

Because the button layers column S on top of the row's `image_prompt`, a bad base prompt produces a bad v2, v3 and v4. If the feedback is really "the whole concept is wrong," fix column **J `image_prompt`** first, then press the button.

The reviewer approves by scheduling the draft in Metricool. Version 1 is never overwritten in Drive — each render is a new file, so an earlier version can be put back by pasting its URL into `image_url`. Status is untouched by the button: the row stays `STAGED` throughout.

## Why faces no longer hold a row

v3 stopped on `photo_required = YES` because Gemini would not render a real person. v4 shipped a no-face graphic and asked a human to add the face later. v5 removed the wait: `gpt-image-1` renders a famous person in the same pass as the rest of the graphic. v6 keeps that and adds the rule for the other case: an unknown subject gets no face at all, by design, not as a gap.

| `image_url` | Subject | v6 behaviour |
| :--- | :--- | :--- |
| empty | famous public figure | `gpt-image-1` renders the full graphic from `image_prompt`, person included |
| empty | not famous | `gpt-image-1` renders the full graphic from `image_prompt`, document-led, no person |
| filled | any | Use the image as-is (reviewer-approved or hand-built) |

`photo_required` stays in the sheet for history but nothing reads it.

---

## Google Sheet — `QDE_Post_Queue`

Live at `https://docs.google.com/spreadsheets/d/14pkeLjlH5SFf4X_DwafTCJlgdKRNOcY-p_AAbZjxfec`, first tab (gid 0), read by id.

Columns (A–T): `post_id · title · status · headline · gold_word · subline · torn_note · face_source · photo_required · image_prompt · image_url · caption · facts_need_verify · fact_status · metricool_fb_id · metricool_li_id · date_staged · notes · image_feedback · publish_date`. Column **S** header is exactly `image_feedback` — n8n uses the row-1 header text as the JSON key, so the header must match the expression `$json.image_feedback` character for character; instructions for the reviewer go in a cell note, never in the header (2026-09-14: a long descriptive header made the Regenerate button read column S as empty). Column **T `publish_date`** (`YYYY-MM-DD`) is the slot Betty gave the drafts; it is how the next run knows where the calendar ends. Both added 2026-09-13.

`status` values — exactly four, uppercase, the filter is case-sensitive: `READY` (Betty takes it) · `STAGED` (drafts exist in Metricool; also the state during and after every regenerate) · `PUBLISHED` (reviewer sets after scheduling) · `ERROR` (an API call or empty caption failed; see `notes`; fix and set back to `READY`). A blank cell means Peggy is still writing.

**`BLOCKED` is retired.** Any row currently `BLOCKED` should be set back to `READY`; v4 will stage it with flags.

Only `READY` rows are touched by the daily run. Sheet order is posting order. **Do not set rows to `HOLD` to wait for a face or a fact check** — set them `READY` and let the flags carry the work to the draft.

---

## n8n workflow changes from v3 (what to edit on import, or what the v4 JSON contains)

1. **"Read queue (READY rows)"** — Resource *Sheet Within Document*, Operation *Get Row(s)*, Document by ID, Sheet by ID `0`, filter `status = READY`, *Return only First Matching Row* on. (v3's live instance had drifted to Document → Create, which created an empty spreadsheet every run and staged nothing.)
2. **"Preflight checks"** (Code node, *Run Once for All Items*) — `preflight_checks_v4.js` in this folder is the live code. Repair-and-flag: returns the repaired, mojibake-fixed `caption`, `flags[]`, `preflight_problems`, `face_pending`, and `preflight_ok` (false only for an empty caption).
3. **"Preflight passed?"** (IF) — `{{ $json.preflight_ok }}` is true, with *Convert types where required* ON (without it the IF throws a type error). Only an empty caption goes to the ERROR branch.
4. **"Has image already?"** (IF) — unchanged; its false branch is reached for every empty `image_url`.
4a. **"Gemini — generate graphic"** → rename **"OpenAI — generate graphic"**: HTTP POST `https://api.openai.com/v1/images/generations`, Authentication *Predefined Credential Type* → *OpenAI* → credential **"OpenAI account"** (2026-09-14: the node had been left on Header Auth pointing at the Metricool `X-Mc-Auth` credential, which OpenAI rejected as "Missing bearer or basic authentication"). JSON body `{"model":"gpt-image-1","prompt":{{ $json.image_prompt }},"size":"1024x1536","quality":"high","moderation":"low","output_format":"png","n":1}`. The response's `data[0].b64_json` feeds the existing "Base64 → PNG" node (change its source path from Gemini's `candidates[0].content.parts[…].inlineData.data` to `data[0].b64_json`). Everything after is unchanged. The same credential setting applies to the OpenAI node in "Betty — Regenerate image (button)".
5. **"Mark row BLOCKED" / "Blocked — tell reviewer"** — renamed **"Mark row ERROR" / "Error — tell reviewer"** and reached only from API failures (set *On Error → Continue (error output)* on the OpenAI, Drive, and both Metricool HTTP nodes and wire their error outputs here) and the empty-caption case.
6. **"Assemble post"** — computes the publish slot (item 4 above) from the sheet's `publish_date` column: the Read-queue node's sibling **"Read scheduled dates"** (Get Row(s), filter `status = STAGED` or `PUBLISHED`, no first-row limit) feeds it; Assemble post takes `max(publish_date) + 1 weekday`, falling back to the next weekday from today at 09:00 America/Chicago, and puts it in both bodies' `publicationDate`. **The v3 code set every draft to the same next-weekday 09:00, which is why a batch of manual runs stacked six drafts on one morning.** Uses the clean `caption`; body includes `saveExternalMediaFiles: true` so Metricool ingests the Drive image instead of storing a dead link. Wiring: Assemble post → Facebook DRAFT → LinkedIn DRAFT → Mark row STAGED (serial, so `$('Metricool — Facebook DRAFT')` is on the path). "Mark row STAGED" writes the flag summary into `notes`.
7. **"Staged — tell reviewer"** — message format: `QDE daily post STAGED — <post_id> (<headline>). FB: <link> · LI: <link>. Flags: <list or "none">. Fact status: <fact_status if FACTS UNVERIFIED>. Regenerate image → <form URL>?post_id=<post_id>`.
8. **Workflow "Betty — Regenerate image (button)"** — see "Regenerate image — the button" above. Its "Feedback in column S?" IF node tests `{{ String($json.image_feedback || '').trim() }}` *is not empty*; this only works while the sheet's column S header is exactly `image_feedback`.

---

## Credentials

Google Sheets OAuth2 · Google Drive OAuth2 (same account) · OpenAI — n8n predefined **OpenAI** credential named **"OpenAI account"** (API key from platform.openai.com; used by the HTTP node via *Predefined Credential Type*, not Header Auth) · Metricool `X-Mc-Auth` header · Slack OAuth2. Config node: sheet id, gid `0`, Drive folder `12vSyv-55AgDEz1YNuf8SJPStcKUF-_4w`, Slack channel `qde-celebrity-post-review`, `blogId 6268508`, `userId 4831552`, model `gpt-image-1` (the Gemini credential and `gemini_image_model` config stay for HU thumbnails only).

---

## [TO VERIFY] before relying on v6

1. Metricool `draft: true` lands in the planner as a draft (pipeline OPEN FLAG #3) — confirmed in principle by the v3 test on 2026-09-12 reaching the Metricool nodes; confirm the drafts are visible in the planner.
2. Google Drive linked in Metricool (OPEN FLAG #2) — if `Failed to normalize media`, the FTP bridge replaces "Upload PNG to Drive".
3. `gpt-image-1` via the API renders named public figures as freely as the ChatGPT app does — confirmed for nobody yet; the first run on QDE-FC-4 or QDE-FC-5 is the test. If it refuses, drop the name and keep the description.
4. V12 → V13 one-line amendment described in the header.
5. The five `image_prompt` cells in the sheet still carry the v5 closing tail ("No logos, no other text" / "No swastikas, no insignia" / "No explosions, no religious symbols") and, for QDE-FC-3, an invented forger's face. Rewrite each to the v6 shape before its row runs.

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
