# QDE Famous-Case Story Prompt — the copy step
**Version:** V3 · **Prepared:** 2026-09-15 · **Owner:** Peggy (copy) · **Lane:** Handwriting Experts Inc. / QDE only
**Voice:** `BART_BAGGETT_VOICE.MD` · **Credentials:** `brands/qde-brand.md`
**Stage A prompt:** `Headline-QDE-Post.md` — the RICK paste block lives there, not here.
**Runs on:** a row of `QDE_Post_Queue` (Google Sheet `14pkeLjlH5SFf4X_DwafTCJlgdKRNOcY-p_AAbZjxfec`, tab gid 0) that
already has a fact card in it. **Never create a new spreadsheet — update the existing row.**

**Supersedes V2 and v1.** V1 assumed one person did research and copy in a single sitting, so it never said what
passes between them; the first time the two were actually split — QDE-FC-16 … FC-21 on 2026-09-15 — six rows stalled
half-filled. V2 fixed the ownership problem but carried the RICK paste block inline, which put the same text in two
files as soon as the RICK prompt got its own document. **V3 changes no rules. It moves Stage A out to
`Headline-QDE-Post.md` and points here instead of repeating it.**

---

## Where this sits

```
QDE_FamousCase_Research_Prompt_v1.md   →   THIS FILE   →   Betty_n8n_QDE_Daily_Social_Post_SOP (v6)
Claude finds and verifies the case.        Stage A: RICK names it.        A human sets status READY.
Writes the fact card into the row.         Stage B: Peggy writes it.      Betty stages two Metricool drafts.
Status stays BLANK.                        Status stays BLANK.
```

Nothing here is research. If a fact is missing or a ⚠️ in `fact_status` needs resolving, that goes back to the
Research Prompt — do not fix it here, and never invent a fact to make a headline land.

---

## Column ownership — the table v1 was missing

V1 Step 5 and Research Prompt §6 both claimed all twenty columns. That overlap is what broke. This table governs.

| Col | Field | Written by | When |
| :--- | :--- | :--- | :--- |
| A | `post_id` | Research | fact card |
| B | `title` | Research | fact card |
| C | `status` | **A human** | left blank until a person flips it to `READY` |
| D | `headline` | **RICK** | Stage A — `Headline-QDE-Post.md` |
| E | `gold_word` | **RICK** | Stage A — `Headline-QDE-Post.md` |
| F | `subline` | **RICK** | Stage A — `Headline-QDE-Post.md` |
| G | `torn_note` | Research | fact card |
| H | `face_source` | Research | fact card — the full scene brief: who is in frame or why nobody is, plus period, setting and props |
| I | `photo_required` | — | retired; nothing reads it |
| J | `image_prompt` | **Peggy / Claude** | **Stage B — after the headline exists** |
| K | `image_url` | — | blank; Betty generates |
| L | `caption` | **Peggy / Claude** | Stage B |
| M | `facts_need_verify` | Research | fact card |
| N | `fact_status` | Research | fact card |
| O–T | Metricool ids, dates, notes | Betty | at staging |

**`image_prompt` is Stage B, not research** (Bart, 2026-09-15). The prompt quotes the headline and names the gold
word, so it cannot be written before the headline is chosen. The **retired** alternative was to pre-write the prompt
with `[[HEADLINE]]` placeholders at research time and find-and-replace later; rows 17–22 were built that way on
2026-09-15 and have been corrected. Do not reintroduce placeholders — a row that reaches Betty with brackets still in
it renders the brackets into the graphic.

---

## Stage A — RICK writes the headline, the gold word and the sub-line

**→ Use `Headline-QDE-Post.md`.** It holds the paste block, what to copy out of the row, and the six-point acceptance
test. Open a **new** RICK session every time: https://chatgpt.com/g/g-u9LaoH9J2-r-i-c-k

Stage A produces **D**, **E** and **F**, and nothing else. Do not write a headline in Claude's own voice — that is
RICK's job. Come back here when those three cells are filled and have passed the acceptance test.

---

## Stage B — Peggy writes the image prompt and the caption

### B1. `image_prompt` (column J)

Now that the headline exists, assemble the prompt. The scene is already decided in column H; this step wraps the
copy around it. House shape, per Betty's SOP v6:

- *Cinematic editorial poster, 4:5 portrait, photoreal.* Deep navy ground `#10142E`, film grain, one warm light source.
- **The subject, from column H.** A famous public figure is named and described — who, which decade, expression,
  clothing, where in the frame. An unrecognizable subject gets **no person**: the document and the evidence carry the
  frame, and mood comes from light and composition. An invented face reads as a stock-photo stranger.
- **The headline, quoted, with the gold word named**: `headline "…" in white with only the word "…" in gold (#FFE455)`,
  then the sub-line quoted.
- **The document at the centre** with its specific detail, and the period props from column H.
- **The torn cream notepad** with column G's fragments quoted verbatim, and the count stated: *"the note lists exactly
  these four bullets."*
- **Close with what the text is, not what it isn't:** *The only text in the image is the headline, the sub-line, and
  the note bullets. Every cover and spine is plain cloth unless a title is quoted above.*

**Never write a "no …" instruction.** `gpt-image-1` does not process negation — it sees the noun and paints it.
"No swastikas" produced swastikas; "no other text" produced a fifth bullet reading the instruction back. State what
every surface *is*. This applies to column S feedback too: write *"plain black covers"*, not *"remove the symbols."*
Hate symbols are never requested even when the story is about the regime; period props carry the setting.

### B2. `caption` (column L)

**Under 200 words before the CTA block.** Five parts, in this order, no headers:

1. **Crime and famous name in the first two lines.** A date, a place, a person, and the act.
2. **The turn.** The single fact that makes it a story, in its own short paragraph. Give it room.
3. **What happened next.** One paragraph. Specifics over summary — numbers and objects, not adjectives.
4. **Bart's paragraph.** Opens *"I wasn't involved in the ___ case."* — stated, every time. Then the forensic lesson
   in plain English, and it must be a lesson about *method*, not about the case: *"The famous signature draws your
   eye. The obscure handwriting solves the case."* This is the only paragraph in the first person.
5. **One line for attorneys.** Starts *"Attorneys:"*. A practical instruction that follows from paragraph 4. Then the
   CTA block exactly:
   ```
   1-800-980-9030
   HandwritingExpertUSA.com · bartbaggett.com
   ```
   followed by five hashtags on one line.

**Sentence rules.** Short. One idea per sentence. Cut every sentence that explains a previous one. No "here's the part
that matters," no "now," no throat-clearing. Dry, confident, a little amused — never impressed by the criminal.

**Banned.** Outcome language ("win your case", "guarantee"), hype words, exclamation marks, "graphology",
`HandwritingExpert.com`, any sentence that makes the famous person the criminal, any claim not in `fact_status`.
One em-dash per paragraph at most.

### Acceptance test before the row is done

- Caption is **under 200 words** before the CTA block, and has all five parts in order.
- *"I wasn't involved in the ___ case."* is present, verbatim in shape.
- CTA block is exact. **Exactly five** hashtags.
- `image_prompt` contains the headline and the gold word **as written in D and E**, quotes column G's fragments
  verbatim, states the bullet count, and **contains no negation** — search it for "no ", "not ", "without", "remove".
- **No `[[…]]` placeholder survives anywhere in the row.**
- Every specific in the caption traces to `fact_status`.

---

## What this step never does

- Never researches. A missing fact goes back to the Research Prompt.
- Never sets `status`. A human does that, and it is the one glance the pipeline keeps at the front — a new case is a
  brand decision (does Bart want a dictator's face on his feed?), and it costs five seconds.
- Never writes a headline in Claude's own voice. That is Stage A, and it is RICK's.
- Never touches a case Bart worked, an open case, or a living private person — the Research Prompt's gates already
  excluded those, and nothing here reopens them.

---

## The model post

Cosey, approved 2026-09-12 — headline HE STOLE BEN FRANKLIN'S SIGNATURE, gold STOLE, sub-line *The expert called it
fake. So he became a forger.*, 197 words. When in doubt, count its sentences and match them.

⚠️ **Known conflict, unresolved:** the SOP names row QDE-FC-5 as this model post, but the live row reads HE WAS
AMERICA'S FIRST CONVICTED FORGER, gold LINCOLN, and runs long. Two different posts. The Cosey text above is the
standard; the live row is not.
