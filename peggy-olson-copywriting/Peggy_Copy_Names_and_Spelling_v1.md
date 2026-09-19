# Peggy — Names & Spelling in Published Copy — v1

**Version:** v1 · September 19, 2026
**Repo location:** `peggy-olson-copywriting/Peggy_Copy_Names_and_Spelling_v1.md`
**Applies to:** every word Peggy publishes — titles, descriptions, captions, posts, on every surface and every brand lane.

---

## What this file is for

A name spelled wrong in published copy is worse than a name spelled wrong in a transcript. The transcript is working material; the copy is what a trial attorney reads before deciding whether to hire an expert witness. "Bart Bagot, forensic document examiner" undoes the credibility the sentence is trying to build.

This file is the standard for **what correct looks like**. Betty's `betty-social-media-manager/HU_QDE_Transcription_Custom_Vocabulary_v2.md` §2 is the machine-side enforcement of the same facts on transcripts. They are two application points for one set of truths — not two lists.

## What this file does NOT own

Per Peggy's README: *"Prompt files read brand facts from `brands/`. Never hard-code a domain, palette, or banned-terms list into a prompt."*

That rule applies here too. This file covers **names and spellings only**. It does not restate:

| Fact | Lives in |
|---|---|
| Domains, CTAs, phone number | `brands/qde-brand.md`, `brands/handwriting-university.md`, `brands/bartallanbaggett-brand.md` |
| Banned terms (graphology in body copy, "link in bio", outcome promises) | `brands/` and the README's non-negotiables |
| Voice and tone | `brands/BART_BAGGETT_VOICE.MD` |
| Transcript correction regexes | Betty's vocabulary v2 §2c |

Duplicating a list is how the transcription dictionary ended up with 4 of its 13 rules deployed. Point, don't copy.

---

## 1. People

### Bart Baggett — the host

**Correct: `Bart Baggett`.** Both halves are wrong often, and independently.

| Wrong given name | Wrong surname |
|---|---|
| Bert · Barb · Mark | Bagot · Bagget · Baget · Bagott |

Any combination of those appears in raw transcripts. **All of them are the host.** Correct silently — never ship one, never flag one for Bart to fix.

> **Barb** and **Mark** were both observed in 2026. If you see a new variant, correct it and add it to Betty's v2 §2a so the transcript layer catches it next time.

### Curt Baggett — Bart's father

**Correct: `Curt Baggett`. C-U-R-T.** Never "Kurt." This is a standing instruction from Bart and it applies to every document and record, not just copy.

⚠️ **Curt is a different person.** He is not a misspelling of Bart and must never be corrected toward Bart. If the source says Curt, the copy says Curt.

### Team

`Zeeshan` · `Kristine` · `Zakir` · `Dr. Walker`

---

## 2. Entities and products

| Correct | Seen wrong as |
|---|---|
| `Handwriting Experts Inc.` | Handbring Experts |
| `Handwriting University` | — |
| `International School of Forensic Document Examination` | International School of Forensic **Talking** Examination |
| `Grapho-Deck` / `GraphoDeck` | graph deck · Grafodet |
| `Silver Class` | — |
| `Level 100` | — |

---

## 3. Terms of art — capitalisation

These are correct spellings, not banned terms. Write them this way:

`T-bar` (not "tea bar") · `questioned document examiner` · `forensic document examination` (not "forensic doc examining") · `decedent` (not "deedent") · `holographic will` · `known exemplar` · `line quality` · `pen lift` · `personal pronoun I`

---

## 4. Domains — the one rule that belongs here

Full domain policy is in `brands/`. Only the spelling hazard is recorded here, because it is a spelling hazard:

- **`HandwritingExpertUSA.com`** — the QDE service domain. Written with that exact casing.
- **`HandwritingExpert.com`** — **not owned. Never write it in any copy, CTA, caption or on-screen text.** Valid only as the hashtag `#HandwritingExpert`.
- **`handwritingexperts.com`** — plural, and a **real owned property**. Never "correct" it to the singular.

---

## 5. When the source is wrong

Peggy's README already sets the principle: *"Name transcription errors are corrected silently; everything else is flagged for Bart."* Applied:

| Situation | Action |
|---|---|
| Any Bart / Baggett variant in §1 | Correct silently |
| Curt vs Kurt | Correct silently to Curt |
| Entity or product name in §2 | Correct silently |
| Term of art in §3 | Correct silently |
| A name not on this page | ⚠️ `TO VERIFY` — do not guess |
| A **guest** genuinely named Bert or Barb | Leave it. Flag for Bart if the transcript is ambiguous. |

The last row is the reason `Bert` and bare `Barb` are review flags rather than automatic swaps in Betty's v2 §2b. A guest named Bert exists; renaming him is a worse failure than leaving the host misspelled once, because it is invisible.

---

## 6. Keeping this in step

- A new misspelling goes into **Betty's v2 §2a** (machine enforcement) **and** §1 here if it is a new name.
- Bump the version in the filename on every change — repo rule, highest number wins.
- If this file and `brands/` ever disagree on a domain, **`brands/` wins** and this file gets fixed.
