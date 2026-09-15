# Headline — QDE Famous-Case Post
**The RICK prompt. Stage A of `QDE_FamousCase_Story_Prompt_V3.md`.** · Prepared 2026-09-15 · **Lane:** QDE only
**RICK:** https://chatgpt.com/g/g-u9LaoH9J2-r-i-c-k — **open a NEW session every time. Never continue an old one.**

This file produces three cells and nothing else: **D `headline`**, **E `gold_word`**, **F `subline`**.
Column J (image prompt) and column L (caption) come afterwards, written by Peggy/Claude — the image prompt is built
on the headline, so it cannot be written until RICK has picked one.

---

## Before you paste

1. Open the row in `QDE_Post_Queue` (sheet `14pkeLjlH5SFf4X_DwafTCJlgdKRNOcY-p_AAbZjxfec`, tab gid 0).
2. Copy **column N** (`fact_status`) — **but only the sourced narrative. Stop at the first ⚠️.** The warning lines are
   internal notes about what is unverified; RICK will treat them as material and write them into a headline.
3. Copy **column G** (`torn_note`) and **column H** (`face_source`).
4. Paste the block below with those three pieces dropped into the slots at the bottom.

---

## The paste block

```
I need a scroll stopping title for this composite LinkedIn graphic. It needs to capture attention, like a
headline of National Enquirer. There is always a good story here involving some alleged crime, forgery, theft,
or death of a famous person. Include the famous person in the headline. The audience is trial attorneys and
litigators who retain forensic document examiners; it posts on Bart Baggett's personal LinkedIn, so a broader
business and true-crime audience sees it too. We will also use this title on the graphic and must have space
for the celebrity image and documents, so it can't be super wordy.

Rules, all of them hard:
- Eight words maximum, all caps.
- The famous person is the SUBJECT of the crime, never its author. If the group name is more recognizable than
  the person's, use the group.
- No headline may state or imply that the famous person committed the crime.
- Give me ONE gold word: a single word, a crime verb or noun, that appears verbatim in the headline.
- Give me a sub-line: the second shock, one line, under twelve words. Not the forensic detail.
- The headline is the crime plus the famous name. The forensic tell is the last paragraph of a story, not a
  reason to stop scrolling.
- Use only the facts I give you below. Do not add a name, a date, a number or a claim of your own.

Return exactly three lines and nothing else:
HEADLINE:
GOLD WORD:
SUB-LINE:

Here is the case:
<<< paste column N, sourced narrative only, stop at the first warning symbol >>>

Torn note fragments:
<<< paste column G >>>

Who is in the frame:
<<< paste column H >>>
```

---

## Then check it before it touches the sheet

All six must pass:

1. Headline is **eight words or fewer**, all caps.
2. Gold word is **one word** and appears **verbatim in the headline**.
3. Sub-line is **under twelve words** and is not the microscope detail.
4. Nothing states or implies the famous person committed the crime.
5. Every proper noun, date and number traces to column N. **RICK invents confidently** — anything it added on its
   own goes back through `QDE_FamousCase_Research_Prompt_v1.md` before use.
6. No banned term: no "graphology" or "graphologist", no `HandwritingExpert.com` (it is
   **HandwritingExpertUSA.com**), no outcome language.

If a line fails, say which rule it broke and ask again **in the same session**. Do not fix it yourself — the
headline is RICK's job — and do not settle for a near miss because the third attempt is tiring.

Write the three values into **D**, **E** and **F**. Leave **C `status` blank**; a human flips it to READY.

---

## Worked example — the model post

Cosey, approved 2026-09-12:

```
HEADLINE: HE STOLE BEN FRANKLIN'S SIGNATURE
GOLD WORD: STOLE
SUB-LINE: The expert called it fake. So he became a forger.
```

Five words, gold word present in the headline, sub-line nine words. That is the standard.

⚠️ The live QDE-FC-5 row does **not** match this — it reads HE WAS AMERICA'S FIRST CONVICTED FORGER with gold word
LINCOLN, a word the headline does not contain. Use the block above, not the live row.

⚠️ Five other live rows have the same defect. **FC-8, FC-10, FC-14 and FC-15 have headlines that no longer contain
their gold word**, and **FC-2 (`HOWARD HUGHES`) and FC-15 (`SECRET DIARY`) have two-word gold words.** The graphic
gilds the gold word *from the headline*, so where the word is absent there is nothing to gild. Worth a cleanup pass.

---

## What happens next

Back to `QDE_FamousCase_Story_Prompt_V3.md`, Stage B: Peggy/Claude writes the image prompt around the headline you
just chose, then the caption. Then a human sets `status` to READY and Betty takes it.
