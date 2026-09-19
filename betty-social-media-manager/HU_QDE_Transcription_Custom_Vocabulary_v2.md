# Transcription Custom Vocabulary + Correction Dictionary — v2

**Version:** v2 · September 19, 2026
**Repo location:** `betty-social-media-manager/HU_QDE_Transcription_Custom_Vocabulary_v2.md`
**Supersedes:** v1 (2026-08-19), which existed only on the Mac and was never committed.
**Scope:** HU, QDE and Bart Show video transcription — Descript, Whisper, Gemini, YouTube ASR.

**Why v2 exists.** v1 was a good list in a place nothing could reach. It lived on one Mac, was never committed, and split its corrections across three subsections with different confidence levels. The result: the live n8n node `VTT: build + correct` implemented **four** of its rules and silently missed the rest — including `Bagget`, the second most common misspelling of the surname, which appears 8 times in the source corpus. This version is one ordered list, machine-readable, with its deployment status recorded.

**Source of truth:** this file, on `main`. Any copy on any Mac is a cache.

---

## 1. CUSTOM VOCABULARY — 78 terms

Fed to the transcriber as `custom_vocabulary` where the engine supports it. Improves the words at capture time. Section 2 is still required afterwards.

> ⚠️ Google rejects `custom_vocabulary` combined with word-level timestamps or diarization. Descript's API exposes no vocabulary parameter at all. **Section 2 is the only correction layer that runs on every path.**

### People
```
Bart Baggett
Curt Baggett
Baggett
Dr. Walker
Zeeshan
Kristine
Zakir
```

### Brands, domains and products
```
Handwriting University
HandwritingUniversity.com
Handwriting Experts Inc.
HandwritingExpertUSA.com
handwritingexperts.com
Grapho-Deck
GraphoDeck
Silver Class
Level 100
International School of Forensic Document Examination
```

### Handwriting-analysis vocabulary
```
handwriting analysis
handwriting analyst
graphology
graphologist
graphotherapy
graphotherapist
T-bar
t-bar
crossed t-bar
personal pronoun I
capital I
baseline
upper zone
middle zone
lower zone
lower loop
upper loop
felon's claw
stinger
loop
stroke
slant
pen pressure
letter formation
trait
self-esteem
self-image
```

### Forensic / QDE vocabulary
```
questioned document
questioned document examination
questioned document examiner
forensic document examination
forensic document examiner
decedent
holographic will
will contest
exemplar
known exemplar
signature authentication
forgery
simulated forgery
traced forgery
disguised writing
line quality
pen lift
expert witness
deposition
subpoena
affidavit
notary
probate
```

### Psychology vocabulary
```
narcissism
narcissist
narcissistic
Freudian
ego
ambivert
introvert
extrovert
emotional responsiveness
self-conscious
self-reliance
sensitive to criticism
selective listener
```

---

## 2. CORRECTION DICTIONARY

Deterministic find-and-replace, run on the transcript from **any** tool.

### ⚠️ ORDER IS NOT OPTIONAL

Rules run top to bottom. Multi-word rules must run before the single-word rules they contain, or you get wrong results:

- `Mark Bagot` → surname rule first gives `Mark Baggett` → then the given-name rule gives `Bart Baggett`. Correct.
- Reverse the order and `Mark Bagot` never matches `Mark Baggett`, so it ships as `Mark Bagot`.

### 2a. AUTO-REPLACE — apply without asking

| # | Pattern (JS regex) | Replace with | Why |
|---|---|---|---|
| 1 | `/\bBag(?:ot\|ott\|get\|et)\b/gi` | `Baggett` | Covers Bagot (14), Bagget (8), Baget (2), Bagott. Does **not** match the correct `Baggett`. |
| 2 | `/\bBart Bagg?ett?\b/gi` | `Bart Baggett` | Normalises casing after rule 1. |
| 3 | `/\bMark Baggett\b/g` | `Bart Baggett` | Documented 2026-05-19. Runs after rule 1. |
| 4 | `/\bBarb Baggett\b/gi` | `Bart Baggett` | **New in v2**, observed by Bart 2026-09-19. Safe because the surname disambiguates. |
| 5 | `/\btea bar\b/gi` | `T-bar` | 4 occurrences |
| 6 | `/\bdeedent\b/gi` | `decedent` | 3 occurrences |
| 7 | `/\bgraph deck\b/gi` | `Grapho-Deck` | 2 occurrences |
| 8 | `/\bGrafodet\b/gi` | `Grapho-Deck` | VID-0110 |
| 9 | `/forensic doc examin(?:ing\|ation)\b/gi` | `forensic document examination` | 3 occurrences combined |
| 10 | `/\bHandbring Experts\b/gi` | `Handwriting Experts Inc.` | Documented 2026-05-19 |
| 11 | `/International School of Forensic Talking Examination/gi` | `International School of Forensic Document Examination` | Documented 2026-05-19 |
| 12 | `/\bhandwritingexpertsusa\.com\b/gi` | `HandwritingExpertUSA.com` | 1 occurrence |
| 13 | `/\bHandwritingExpert\.com\b/gi` | `HandwritingExpertUSA.com` | Domain is not owned and must never ship |

**Rule 13 cannot eat the plural.** `handwritingexperts.com` has an `s` before `.com`, so the pattern cannot match it. That domain is a real owned property — see §3.2.

### 2b. REVIEW FLAGS — do NOT auto-replace

These are wrong only *sometimes*. Replacing them blindly breaks real names. Raise a flag on the run and let a human decide.

| Pattern | Likely intended | Why it is not auto-replaced |
|---|---|---|
| `/\bBert\b/gi` | `Bart` | A guest genuinely named Bert would be renamed. 2 occurrences in corpus. |
| `/\bBarb\b/gi` *(bare, no surname)* | `Bart` | Barb is a common name. Only auto-replace when followed by the surname — rule 4. |
| `pride` *(VID-0110 @ 1:36)* | `presence` | Unresolved — Descript and Whisper disagree. Needs the audio. |
| `j'ai` | `je` (FR) or `yo` (ES) | Language-dependent; cannot be resolved by pattern. |

> **v1 said this and the code did the opposite.** v1 §3 warned that a blind `Bert` → `Bart` swap was unsafe. The deployed n8n node ran `/\bBert\b/g → Bart` unconditionally anyway. Flag, do not swap.

### 2c. Machine-readable

Tools should consume this block rather than hardcoding a subset. Order is preserved.

```json
{
  "version": 2,
  "auto_replace": [
    {"pattern": "\\bBag(?:ot|ott|get|et)\\b", "flags": "gi", "replace": "Baggett"},
    {"pattern": "\\bBart Bagg?ett?\\b", "flags": "gi", "replace": "Bart Baggett"},
    {"pattern": "\\bMark Baggett\\b", "flags": "g", "replace": "Bart Baggett"},
    {"pattern": "\\bBarb Baggett\\b", "flags": "gi", "replace": "Bart Baggett"},
    {"pattern": "\\btea bar\\b", "flags": "gi", "replace": "T-bar"},
    {"pattern": "\\bdeedent\\b", "flags": "gi", "replace": "decedent"},
    {"pattern": "\\bgraph deck\\b", "flags": "gi", "replace": "Grapho-Deck"},
    {"pattern": "\\bGrafodet\\b", "flags": "gi", "replace": "Grapho-Deck"},
    {"pattern": "forensic doc examin(?:ing|ation)\\b", "flags": "gi", "replace": "forensic document examination"},
    {"pattern": "\\bHandbring Experts\\b", "flags": "gi", "replace": "Handwriting Experts Inc."},
    {"pattern": "International School of Forensic Talking Examination", "flags": "gi", "replace": "International School of Forensic Document Examination"},
    {"pattern": "\\bhandwritingexpertsusa\\.com\\b", "flags": "gi", "replace": "HandwritingExpertUSA.com"},
    {"pattern": "\\bHandwritingExpert\\.com\\b", "flags": "gi", "replace": "HandwritingExpertUSA.com"}
  ],
  "review_flags": [
    {"pattern": "\\bBert\\b", "flags": "gi", "suggest": "Bart", "flag": "NAME_BERT_REVIEW"},
    {"pattern": "\\bBarb\\b(?! Baggett)", "flags": "gi", "suggest": "Bart", "flag": "NAME_BARB_REVIEW"}
  ]
}
```

---

## 3. Notes and cautions

1. **`Bert` and bare `Barb` are flags, not swaps.** See §2b.
2. **`handwritingexperts.com` (plural) is a real owned property** and must never be "corrected" to the singular. `HandwritingExpert.com` is not owned and must never appear in any output.
3. **`graphology` / `graphologist` are correct transcriptions.** They are banned in HU *body copy*, not in transcripts. Do not strip them at the transcript stage.
4. **The corpus is HU-weighted.** Only a handful of QDE transcripts sit in the original 67-file sweep, so the forensic terms in §1 are drawn from the SOPs rather than measured error counts. Best estimate, not verified frequency.
5. **The surname is the highest-value rule on this page.** In the source corpus "Baggett" was wrong 24 times out of 50 — misspelled almost half the time.
6. **This list is a floor, not a ceiling.** Sweep each new batch the same way and extend it. Bump the version in the filename on every change.

---

## 4. Deployment status — what is actually live

v1's failure was that nobody could tell which rules were running. Record it here and update it with every change.

| Consumer | Location | Status as of 2026-09-19 |
|---|---|---|
| n8n `VTT: build + correct` | `Betty — QDE Video Publish v2` (`Heg8RaNTQxk3c2rz`) | **Partial — 4 of 13 auto-replace rules**, and it runs the unsafe blind `Bert` swap. Needs updating to §2c. |
| Whisper SOP | `betty-social-media-manager/Betty_SOP_Whisper_Transcription_v4.md` | Not yet cross-referenced |
| Descript | API exposes no vocabulary parameter | §2 is the only correction layer on this path |

**Known gap:** the n8n node hardcodes its rules. Until it fetches §2c from this file the way `Fetch description prompt` fetches the copy spec, this document and the running code will drift again.
