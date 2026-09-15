# QDE Famous-Case Story Prompt — the copy step
**Version:** V4 · **Prepared:** 2026-09-15 · **Owner:** Peggy (copy) · **Lane:** Handwriting Experts Inc. / QDE only
**Voice:** `BART_BAGGETT_VOICE.MD` · **Credentials:** `brands/qde-brand.md`
**Stage A prompt:** `Headline-QDE-Post.md` — the RICK paste block and the approved headline library live there.
**Runs on:** a row of `QDE_Post_Queue` (Google Sheet `14pkeLjlH5SFf4X_DwafTCJlgdKRNOcY-p_AAbZjxfec`, tab gid 0) that
already has a fact card in it. **Never create a new spreadsheet — update the existing row.**

**Supersedes V3, V2 and v1.** V4 adds the completeness gate and the render-approval loop; **no copy rules changed
from V3.** The gate exists because V3 said column J is written at Stage B but never said a row must not reach
`READY` with it blank — and Betty sends column J straight to `gpt-image-1`.

---

## Where this sits

```
QDE_FamousCase_Research_Prompt_v1.md   →   THIS FILE   →   Betty_n8n_QDE_Daily_Social_Post_SOP (v6)
Claude finds and verifies the case.        Stage A: RICK names it.        A human sets status READY.
Writes the fact card into the row.         Stage B: Peggy writes it.      Betty stages two Metricool drafts.
Status stays BLANK.                        Status stays BLANK.            The reviewer judges the graphic.
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
2026-09-15 and were corrected the same day. Do not reintroduce placeholders.

---

## THE COMPLETENESS GATE — read this before setting any row READY

**A row never goes `READY` with any of these blank: D, E, F, G, H, J, L.** Betty does not write copy and does not
write prompts. Whatever is missing when the row is taken stays missing all the way to the planner.

| Must be FILLED before READY | Must be BLANK at READY |
| :--- | :--- |
| D `headline`, E `gold_word`, F `subline` | C `status` — until the human flips it |
| G `torn_note` — 3 to 4 fragments | K `image_url` — Betty generates it |
| H `face_source` — the scene brief | O–T — Betty's ids, dates and notes |
| **J `image_prompt`** | S `image_feedback` — reviewer fills it only on a reject |
| L `caption` | |
| M `facts_need_verify`, N `fact_status` | |

**Blank J is the one that bites.** Betty resolves the image in this order: `image_url` filled → use it as-is;
`image_url` empty → send `image_prompt` to `gpt-image-1`. There is no third branch and no human stop. An empty
`image_prompt` means an empty API call, and the row still becomes two Metricool drafts — with nothing usable in the
frame. The workflow will not catch it: preflight checks the **caption**, and the only condition that skips a row is
an empty caption.

Also check, every time:
- **No `[[…]]` placeholder anywhere in the row.** Brackets left in column J render as brackets in the graphic.
- **The headline and gold word inside J match D and E character for character.** See the drift warning below.
- **J contains no negation** — search it for "no ", "not ", "without", "remove". `gpt-image-1` paints the noun in a
  "no X" instruction. This does not apply to text inside quotation marks, which is copy to be rendered, not an
  instruction: a sub-line reading *"The courts said no. Then DNA ended it."* is fine.

### ⚠️ Editing a headline later orphans column J

Column J quotes the headline. Change D without rewriting J and the graphic still renders the **old** headline, and
the gold word named in J may no longer exist in the new one. **This has already happened on four of the five
published rows** — FC-1, FC-2, FC-3 and FC-5 all have a column D that does not match the headline inside their
column J, because the headlines were hand-edited after the prompt was written. Only FC-4 matches.

**So: any edit to D or E is an edit to J.** Do both, or the graphic is wrong.

---

## Stage A — RICK writes the headline, the gold word and the sub-line

**→ Use `Headline-QDE-Post.md`.** It holds the paste block, the approved headline library for QDE-FC-1 through FC-9,
and the six-point acceptance test. Open a **new** RICK session every time:
https://chatgpt.com/g/g-u9LaoH9J2-r-i-c-k

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

**Banned.** Outcome language ("win your case", "guarantee"), hype words, exclamation marks, **"graphology" and
"graphologist"** (acceptable as hashtags only — so an examiner whose real title is *judicial graphologist* is
described in body copy as a court-qualified handwriting examiner, with the actual title kept in `fact_status`),
`HandwritingExpert.com`, any sentence that makes the famous person the criminal, any claim not in `fact_status`.
One em-dash per paragraph at most.

### Acceptance test before the row is done

- Caption is **under 200 words** before the CTA block, and has all five parts in order.
- *"I wasn't involved in the ___ case."* is present, verbatim in shape.
- CTA block is exact. **Exactly five** hashtags.
- `image_prompt` quotes the headline and gold word **as written in D and E**, quotes column G's fragments verbatim,
  states the bullet count, and contains no negation outside quotation marks.
- **Run the completeness gate above.** Nothing in D, E, F, G, H, J, L is blank.

---

## After the graphic renders — judging version 1

The prompt is not finished when it is written. It is finished when someone looks at the picture. **Expect about one
bad render in ten.**

- **Approved?** The reviewer schedules the draft in Metricool. Scheduling *is* the approval.
- **Not approved?** Type what the picture should show into column **S `image_feedback`** — plain English, phrased
  positively: *"Hughes looks too young; headline clipped on the right; plain black covers on the diaries."* Then press
  **Regenerate image** on the n8n form (linked in every Slack STAGED message). The button updates the two existing
  drafts in place. Column S is required; a regenerate with it empty is refused.
- **Is the whole concept wrong?** **Fix column J first, then press the button.** The button layers column S on top of
  the row's `image_prompt`, so a bad base prompt produces a bad v2, v3 and v4. Rewriting S over and over will not
  rescue a prompt that describes the wrong scene.
- **Never** clear `image_url` or set the row back to `READY` to get a new image. That hands the row to the daily
  workflow, which re-stages it and creates a second pair of Metricool drafts. The row stays `STAGED` throughout.
- Version 1 is never overwritten in Drive. Each render is a new file, so an earlier version can be restored by
  pasting its URL into `image_url`.

**What a reject teaches.** If the same problem shows up on more than one case — text clipping, a face reading too
young, the note bullets miscounted — that is a fault in the house shape in B1, not in one row. Fix it here and bump
the version, so the next batch starts from the corrected prompt.

---

## What this step never does

- Never researches. A missing fact goes back to the Research Prompt.
- Never sets `status`. A human does that, and it is the one glance the pipeline keeps at the front — a new case is a
  brand decision (does Bart want a dictator's face on his feed?), and it costs five seconds.
- Never writes a headline in Claude's own voice. That is Stage A, and it is RICK's.
- Never leaves column J blank. See the completeness gate.
- Never touches a case Bart worked, an open case, or a living private person — the Research Prompt's gates already
  excluded those, and nothing here reopens them.

---

## The model post

Cosey, approved 2026-09-12 — headline HE STOLE BEN FRANKLIN'S SIGNATURE, gold STOLE, sub-line *The expert called it
fake. So he became a forger.*, 197 words. When in doubt, count its sentences and match them.

⚠️ **Known conflict, unresolved:** the SOP names row QDE-FC-5 as this model post, but the live row reads HE WAS
AMERICA'S FIRST CONVICTED FORGER, gold LINCOLN, and runs long. Two different posts. The Cosey text above is the
standard; the live row is not.
