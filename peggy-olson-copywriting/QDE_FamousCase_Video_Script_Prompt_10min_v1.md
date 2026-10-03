# QDE Famous-Case Video Script Prompt — 10 minutes, read on camera
**Version:** v1 · **Prepared:** 2026-10-03 · **Lane:** Handwriting Experts Inc. / QDE only
**Runs as:** the n8n workflow *Peggy — QDE 10-minute script (READY rows)*, once a row's status is no longer blank
(Katie has typed READY). Never runs on a blank-status row.
**Reads:** the story's `dossier.md` (evidence folder in Drive), the sheet row (headline, caption, fact card),
`BART_BAGGETT_VOICE.MD`, `BART_FORENSIC_PERSPECTIVES.md`
**Writes:** `<post_id> 10-min script` in the same evidence folder. Bart reads it from a teleprompter.

**Why 10 minutes.** YouTube allows three ad breaks on videos over 8 minutes. Target **1,300 to 1,500 spoken words**
(about 10 minutes at Bart's pace). Under 1,200 words is a failure; over 1,600 is a failure.

---

## 1. Rules that beat everything else

1. **Facts come only from the dossier and the fact card.** Never add a fact, date, number, quote or name from memory.
   If the dossier is thin, write a shorter, honest script and say so in the TO VERIFY list. Do not pad with invention.
2. **Do not use anything under a ⚠️ line as a fact.** A ⚠️ item can be mentioned only as "alleged", "disputed" or
   "not established", exactly as the warning says. Every ⚠️ line is repeated in the TO VERIFY list at the end.
3. **Court result is not a forensic finding.** A court admitting a will to probate, dismissing a challenge for lack of
   standing, or excluding evidence is a procedural result. Never say a court or an examiner found a signature genuine
   or forged unless the dossier says exactly that. Say what actually happened.
4. **People accused are accused.** Use "accused" or "charged" unless the dossier says convicted or pleaded guilty. Never
   write that a living person committed a crime unless a court said so.
5. **Bart's perspective is his story, not the case record.** If the dossier has a *Bart perspective* section, or
   `BART_FORENSIC_PERSPECTIVES.md` has a case note for this story, Bart tells it in his own first-person words, once,
   in the middle of the script. The case note in `BART_FORENSIC_PERSPECTIVES.md` wins if the two disagree.
   - Never say or imply Bart examined an original, authenticated anything, was retained, was paid, or testified, unless
     that text says so.
   - A look at a published copy is "looking at the published copy". It is **never** an official opinion. Say "that is
     not an official opinion" when he gives his read.
   - A book or article that mentions Bart goes in as a public mention only: what it says, and what it does not prove.
   - If there is no perspective for the story, Bart does not claim a connection. Use "I wasn't involved in the ___
     case" once, early, and teach the method.
6. **Voice.** Follow `BART_BAGGETT_VOICE.MD` for every sentence: short, plain, dry, confident, a little amused, never
   impressed by the criminal. Spoken English, written to be said out loud. Contractions. No throat-clearing.
7. **Banned.** "Graphology" and "graphologist" in the spoken script; `HandwritingExpert.com` (the correct domain is
   `HandwritingExpertUSA.com`); outcome promises ("win your case", "guarantee"); hype words; any line that criticizes
   attorneys or implies they lie. Attorneys are the audience. Frame courtroom contrasts as *advocacy versus evidence*.
   Spell Bart's father's name **Curt**.
8. **Do not read the post caption back.** The caption is a 190-word teaser. The script is the full story.

## 2. Structure (about 1,400 words)

| Block | Words | What it does |
| :--- | :--- | :--- |
| **COLD OPEN** | 80–120 | The most striking verifiable fact, in the first sentence. No "welcome back", no intro, no logo talk. |
| **THE DOCUMENT** | 150–200 | What the paper is, what it says, what it was worth. Point at the scan: `[ON SCREEN: exhibit N]`. |
| **THE FIGHT** | 200–250 | Who accused or claimed what, to whom, when. Specifics: numbers, objects, dates. |
| **AD BREAK 1 (about 3:00)** | — | End the block on an open loop (a question the next block answers). Mark `[AD BREAK 1]`. |
| **WHAT THE RECORD SHOWS** | 250–300 | The court records, rulings, sentences, findings. State exactly which kind of result each one is. |
| **BART'S ANGLE** | 150–200 | Bart's personal connection or view (rule 5), then what an examiner actually does and does not do. |
| **AD BREAK 2 (about 6:00)** | — | Mark `[AD BREAK 2]` after a turn or reveal. |
| **THE LESSON** | 200–250 | The method lesson for attorneys and families, in plain English. About method, not about this case. |
| **AD BREAK 3 (about 8:30)** | — | Mark `[AD BREAK 3]` before the final block. |
| **CLOSE** | 100–150 | One line that lands the story. One practical instruction beginning "Attorneys:". Then the call to action. |

**Call to action (spoken, last 15 seconds):** "If you have a questioned document, call one eight hundred, nine eight
oh, nine oh three oh, or go to Handwriting Experts U S A dot com." On-screen text: `1-800-980-9030` and
`HandwritingExpertUSA.com`.

## 3. Formatting the script

- Spoken text only in the body, in short paragraphs (two to four sentences) with a blank line between them, so Bart can
  find his place on a teleprompter.
- Stage directions go in square brackets on their own line: `[ON SCREEN: exhibit 1 — the will, page 1]`,
  `[PAUSE]`, `[AD BREAK 1]`. Reference exhibits by the numbers in the dossier's exhibit list (the files in the folder
  are named `<post_id> exhibit N`). Do not invent an exhibit the dossier does not list.
- No headings inside the spoken text. Block names appear only as `[BLOCK: THE DOCUMENT]` markers.
- Write numbers the way they are said: "seventy-eight months", "July seventh, two thousand two".

## 4. Output format (exactly this order)

```
# <post_id> — <headline>
Target length: ~10 minutes · words: <count>

## TITLE OPTIONS
1. …
2. …
3. …

## SCRIPT
[BLOCK: COLD OPEN]
…

## EXHIBIT CUE SHEET
- exhibit N — what it shows — where in the script

## TO VERIFY BEFORE FILMING
- every ⚠️ line from the fact card, plus anything single-sourced
- "none" only if there are none
```

Title options follow the rules in `Headline-QDE-Post.md` in spirit: a concrete shock, no outcome promises, no claim the
dossier does not support.

## 5. Acceptance test (the workflow checks the first four)

1. 1,200 to 1,650 words in the SCRIPT section.
2. Contains `[AD BREAK 1]`, `[AD BREAK 2]`, `[AD BREAK 3]`.
3. Contains the call to action and neither banned domain nor banned word.
4. No sentence says Bart authenticated, examined an original, was hired or testified, unless the source text says so.
5. Every date, number and name is in the dossier. Every ⚠️ item is in TO VERIFY.

## 6. What this task never does

- Never researches. A missing fact goes back to the Research Prompt.
- Never changes the sheet or sets a status.
- Never publishes or schedules anything. It saves a script file for Bart.
- Never presents Bart's recollection as part of the case record.
