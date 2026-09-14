# QDE Famous-Case Story Prompt
**Version:** v1 · **Prepared:** 2026-09-12 · **Owner:** Peggy (copy) · **Lane:** Handwriting Experts Inc. / QDE only
**Voice:** `brands/BART_BAGGETT_VOICE.MD` · **Facts:** `brands/qde-brand.md` (credentials) + the RICK research session (case facts)
**Output goes to:** one row of `QDE_Post_Queue` (Google Sheet `14pkeLjlH5SFf4X_DwafTCJlgdKRNOcY-p_AAbZjxfec`, tab gid 0). Betty's n8n workflow takes it from there. **Never create a new spreadsheet — update the existing row.**

**Where this lives in the pipeline.** Everything in this file happens *before* a row is set to READY. Betty's n8n workflow (`Betty_n8n_QDE_Daily_Social_Post_SOP_v4.md`) starts at READY and never writes copy, so nothing here belongs in n8n. This is a writing procedure; it runs in a chat (Bart, or an agent with a browser), and its only deliverable is a filled-in row.

---

## Step 1 — Research and headline in RICK (required, not optional)

Open a **new** session of the R.I.C.K. custom GPT: https://chatgpt.com/g/g-u9LaoH9J2-r-i-c-k — never continue an old one.

**1a. Facts.** Paste the case name (and any draft you already have) with: *"Tell me more about this story."* RICK returns the version with the details that make it a story — the $10 sale, the two hours at the visitor book, the young man's signature on an old man's documents. Those specifics are the raw material. Keep RICK's sources (New Yorker 1956, Raab Collection, Indiana University) in your notes; they go in `fact_status`.

**1b. Headline.** In the same session, paste this, then the story:

> I need a scroll stopping title for this composite LinkedIn graphic. It needs to capture attention, like a headline of National Enquirer. There is always a good story here involving some alleged crime, forgery, theft, or death of a famous person. Include the famous person in the headline. The audience is trial attorneys and litigators who retain forensic document examiners; it posts on Bart Baggett's personal LinkedIn, so a broader business and true-crime audience sees it too. The working title is this, but please make it shorter and better for the highest click through rate. We will also use this title on the graphic and must have space for the celebrity image and documents, so it can't be super wordy. No headline may state or imply that the famous person committed the crime.

Take RICK's pick unless it breaks a rule below. Then ask RICK to tighten any historical claim it made ("America's first professional forger" became "the forger who stole Ben Franklin" this way).

---

## Step 2 — Headline, gold word, sub-line

- **Headline = the crime + the famous name.** Not the forensic tell. THE INK CRACKED is the last paragraph of a story, not a reason to stop scrolling. HE STOLE BEN FRANKLIN'S SIGNATURE and THE MORMON FORGERY THAT ENDED IN MURDER are.
- **Eight words maximum**, all caps. It shares the frame with a face and a document.
- **The famous person is the subject of the crime, never its author.** JOSEPH SMITH THE FORGER is wrong; THE MORMON FORGERY is right. If the group name is more recognizable than the person's, use it (MORMON beat JOSEPH SMITH).
- **Gold word = the crime verb or noun**: STOLE, MURDER, FORGERY. One word only (house rule from `QDE_Video_Publishing_Pipeline_V12.md`). Write it in `gold_word` and also replace the headline text inside `image_prompt`, or Gemini prints the old one.
- **Sub-line = the second shock, one line, under twelve words.** *"The expert called it fake. So he became a forger."* *"He fooled the collectors, the church, and the FBI. Then he built the bombs."* The microscope detail is never the sub-line.

---

## Step 3 — The caption

**Under 200 words before the CTA block.** The v2 pack ran 300–430 and was too long; the approved Cosey rewrite is the length.

Five parts, in this order, no headers:

1. **Crime and famous name in the first two lines.** A date, a place, a person, and the act. *"In 1929 Martin Coneely signed the visitor book at the Library of Congress … and walked out with a 1786 pay warrant signed by Benjamin Franklin in his pocket. Nobody noticed."*
2. **The turn.** The single fact that makes it a story, in its own short paragraph. *"The dealer called it a fake."* Give it room.
3. **What he did with it.** One paragraph. Specifics over summary: the $10, the rusted iron filings, the 78 documents at the NYPL. Numbers and objects, not adjectives.
4. **Bart's paragraph.** Opens with *"I wasn't involved in the ___ case."* — stated, every time. Then the forensic lesson in plain English, and it must be a lesson about *method*, not about the case: *"The famous signature draws your eye. The obscure handwriting solves the case."* This is the only paragraph in the first person.
5. **One line for attorneys.** Starts *"Attorneys:"*. A practical instruction that follows from paragraph 4. Then the CTA block exactly:
   ```
   1-800-980-9030
   HandwritingExpertUSA.com · bartbaggett.com
   ```
   followed by five hashtags on one line.

**Sentence rules.** Short. One idea per sentence. Cut every sentence that explains a previous one. No "here's the part that matters," no "now," no throat-clearing before a paragraph. Dry, confident, a little amused — never impressed by the criminal.

**Banned.** Outcome language ("win your case"), hype words, exclamation marks, "graphology," "HandwritingExpert.com" (the domain is HandwritingExpertUSA.com), any sentence that makes the famous person the criminal, any claim you can't source (see Step 4). No em-dash pile-ups; one per paragraph at most.

---

## Step 4 — Fact discipline (fills `facts_need_verify`, `fact_status`, `notes`)

- Every specific — a dollar figure, a count, a year, a sentence length — is either sourced in `fact_status` or cut. RICK's relay of a source is a lead, not a source: write *"$10 sale — 1956 New Yorker via RICK, verify."*
- When sources disagree (Cosey's sentence: three years / served under one, per IU), say less: *"arrested in 1937, out in a year."*
- Anything about Bart's own life ("I was in high school," "he died before I was born") is either confirmed by Bart or cut. Default: cut.
- Two homicides or a living private person in the story: name victims once, factually; never name private individuals who weren't charged.
- `facts_need_verify = YES` if any ⚠️ remains in `fact_status`. Betty stages the draft anyway and writes the flags to `notes`; the reviewer clears them in the sheet before scheduling. The flags are never in the caption.

---

## Step 5 — Fill the row

| column | what goes in it |
| :--- | :--- |
| `title` | case name, for humans |
| `status` | `READY` when Steps 1–4 are done. The only four values the system uses: `READY` (Betty takes it) · `STAGED` (drafts exist in Metricool) · `PUBLISHED` (reviewer sets after scheduling) · `ERROR` (an API call failed; see `notes`, fix, set back to `READY`). Uppercase, exact — the filter is case-sensitive. Leave the cell blank while writing. |
| `headline` / `gold_word` / `subline` | from Step 2 |
| `torn_note` | 3–4 fragments, · separated, for the notepad callout |
| `face_source` | who the face is and how to describe them (decade, expression, clothing) — this feeds `image_prompt` |
| `image_prompt` | the house-style prompt from the SOP's "Image prompts" section: names and describes the person, quotes the headline with its gold word, the sub-line, the document, the `torn_note` bullets. Rendered by `gpt-image-1`, person included — never "no faces" |
| `image_url` | blank (Betty generates) — or the URL of a hand-approved graphic |
| `caption` | Step 3, plain text, real line breaks |
| `facts_need_verify` / `fact_status` | Step 4 |
| `publish_date` | leave blank — Betty fills it with the next open weekday slot (one post per weekday, 24 hours apart) |
| `notes` | leave for Betty |
| `image_feedback` (col S) | leave blank — the reviewer fills it only when version 1 of the graphic is not approved, then presses Regenerate |

Type straight into the sheet or update via API. UTF-8 only — the v1 seed CSV was imported as Mac-Roman and every dash became `‚Äî`; Betty repairs it on the way out, but the sheet is the source of truth.

---

## The model post

Cosey, approved 2026-09-12 — headline HE STOLE BEN FRANKLIN'S SIGNATURE, gold STOLE, sub-line *The expert called it fake. So he became a forger.*, 197 words. It is in row QDE-FC-5 of the sheet. When in doubt, count its sentences and match them.
