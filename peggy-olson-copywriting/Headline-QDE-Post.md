# Headline — QDE Famous-Case Post
**The RICK prompt. Stage A of `QDE_FamousCase_Story_Prompt_V4.md`.** · Prepared 2026-09-15 · **Lane:** QDE only
**RICK:** https://chatgpt.com/g/g-u9LaoH9J2-r-i-c-k — **open a NEW session every time. Never continue an old one.**

> ⚠️ **RICK is run by a human, always.** Custom GPTs have no API endpoint — RICK cannot be
> called from n8n, a script, or any agent. A person pastes this and pastes the result back.

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
- Eight words maximum, all caps. Six is the target — the approved set averages six.
- The famous person is the SUBJECT of the crime, never its author. If the group name is more recognizable than
  the person's, use the group.
- No headline may state or imply that the famous person committed the crime.
- Give me ONE gold word: a single word, a crime verb or noun, that appears verbatim in the headline.
- Give me a sub-line: the second shock, one line, under twelve words. Not the forensic detail.
- The headline is the crime plus the famous name. The forensic tell is the last paragraph of a story, not a
  reason to stop scrolling.
- Use only the facts I give you below. Do not add a name, a date, a number or a claim of your own.

Here are eight approved headlines from this same series. Match their length and their punch:

ARETHA'S FRANKLIN'S WILL WAS IN THE COUCH / COUCH / A Michigan jury took less than an hour.
THE FAKE HITLER DIARIES / WEEKS / The handwriting was close. The paper wasn't.
THE MORMON FORGERY THAT ENDED IN MURDER / MURDER / He fooled the collectors, the church, and the FBI.
HE WAS AMERICA'S FIRST CONVICTED FORGER / LINCOLN / For twenty years. Auction houses still sell his work.
TRUE STORY BEHIND THE JONBENET RANSOM NOTE / RANSOM / Two and a half pages. Thirty years. No identification.
THE LINDBERGH KIDNAPPING / KIDNAPPING / Eight examiners agreed. The exemplars were dictated to him.
HOWARD HUGHES FAKE AUTOBIOGRAPHY / FORGED / The experts called the writing unanswerable. It was invented.
THE ZODIAC KILLER'S NOTES STILL UNSOLVED? / KILLER / California's top examiner excluded him. DNA later agreed.

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

> **Why eight and not nine:** FC-2 is deliberately absent from the exemplars. It carries two
> of the defects listed below — the HUGES misspelling and a two-word gold word — so it is not
> something to imitate. The paste block used to say "nine"; the count was the error.

---

## Approved headlines — QDE-FC-1 through QDE-FC-9

**Bart approved these on 2026-09-15: learn from the length and the punchy content.** Pulled live from the sheet.

| # | Case (col B) | Headline (col D) | Gold (col E) | Sub-line (col F) |
| :--- | :--- | :--- | :--- | :--- |
| FC-1 | Aretha Franklin | ARETHA'S FRANKLIN'S WILL WAS IN THE COUCH | COUCH | A Michigan jury took less than an hour. |
| FC-2 | Howard Hughes and the "Mormon Will" | HOWARD HUGES FAKE WILL SCAM | HOWARD HUGHES | It showed up on a church desk. A Las Vegas jury called it a forgery. |
| FC-3 | The Hitler Diaries | THE FAKE HITLER DIARIES | WEEKS | The handwriting was close. The paper wasn't. |
| FC-4 | Mark Hofmann and the Salamander Letter | THE MORMON FORGERY THAT ENDED IN MURDER | MURDER | He fooled the collectors, the church, and the FBI. Then he built the bombs. |
| FC-5 | Joseph Cosey and the Lincoln Forgeries | HE WAS AMERICA'S FIRST CONVICTED FORGER | LINCOLN | For twenty years. Auction houses still sell his work — labeled. |
| FC-6 | The JonBenét Ramsey Ransom Note | TRUE STORY BEHIND THE JOHN BENET RANSOM NOTE | RANSOM | Two and a half pages. Thirty years. No identification. |
| FC-7 | The Lindbergh Ransom Notes and Bruno Hauptmann | THE LINDBERGH KIDNAPPING: NEW EVIDENCE INVOLVES NAZIES | KIDNAPPING | Eight examiners agreed. The exemplars were dictated to him. |
| FC-8 | Clifford Irving's Fake Howard Hughes Autobiography | HOWARD HUGHES FAKE AUTOBIOGRAPHY | FORGED | The experts called the writing unanswerable. It was invented. |
| FC-9 | The Zodiac Letters and Sherwood Morrill | THE ZODIAC KILLER'S NOTES STILL UNSOLVED? | KILLER | California's top examiner excluded him. DNA later agreed. |

### What the approved set actually does — measured, not asserted

- **Length: 4 to 8 words, median 6.** FC-3 and FC-8 are four words; FC-6 is the only eight. **Eight is the ceiling,
  six is the target.** A headline that needs seven words to land is fine; one that needs nine is the wrong headline.
- **The verb is plain.** WAS IN THE COUCH. ENDED IN MURDER. No headline reaches for a clever verb.
- **The sub-line is two short sentences, and the second one turns.** *"The handwriting was close. The paper wasn't."*
  *"California's top examiner excluded him. DNA later agreed."* Setup, then the snap. That two-beat structure is the
  single most repeatable thing in the set.
- **Sub-lines run 7 to 11 words**, except FC-2 (15) and FC-4 (14). Treat those two as the outer edge, not the model —
  the twelve-word rule above still governs.
- **The concrete noun beats the forensic term.** COUCH is the best gold word in the set because a jury deliberating
  over a will found in a sofa is a picture. FORGERY is a category; a couch is an image.
- **Four of the nine ask or imply a question** (STILL UNSOLVED?, TRUE STORY BEHIND). Used sparingly it pulls; used
  every time it reads as clickbait to a litigator.

### ⚠️ Copy the style, not these five defects

These are live-cell errors, not house style. They are listed so nobody learns them by imitation:

- **FC-2 headline misspells HUGHES as "HUGES"**, and its gold word is **two words** (`HOWARD HUGHES`).
- **FC-6 spells the name "JOHN BENET"** — it is **JonBenét**.
- **FC-7 spells "NAZIES"** — it is **NAZIS**. The headline also runs a colon and a second clause, which no other
  approved headline does.
- **FC-9 has a trailing space** in the cell.
- **FC-3, FC-5 and FC-8 have gold words that do not appear in their headline** (WEEKS, LINCOLN, FORGED). The graphic
  gilds the gold word *from the headline*, so on those three there is nothing to gild. FC-2's `HOWARD HUGHES` fails
  too, because the headline spells it HUGES.
- **FC-5's sub-line carries Mac-Roman mojibake** (`‚Äî` where an em-dash belongs).

Worth a cleanup pass on the sheet before any of these renders again.

---

## Then check what RICK returns

All six must pass:

1. Headline is **eight words or fewer**, all caps. Six is the target.
2. Gold word is **one word** and appears **verbatim in the headline**.
3. Sub-line is **under twelve words** and is not the microscope detail.
4. Nothing states or implies the famous person committed the crime.
5. Every proper noun, date and number traces to column N. **RICK invents confidently** — anything it added on its
   own goes back through `QDE_FamousCase_Research_Prompt_v2.md` before use.
6. No banned term: no "graphology" or "graphologist", no `HandwritingExpert.com` (it is
   **HandwritingExpertUSA.com**), no outcome language. ⚠️ `handwritingexperts.com` — plural — **is** a real owned
   property; never "correct" it to the singular. Spell-check the proper nouns — see the defect list above, and
   `Peggy_Copy_Names_and_Spelling_v1.md` for the house names.

If a line fails, say which rule it broke and ask again **in the same session**. Do not fix it yourself — the
headline is RICK's job — and do not settle for a near miss because the third attempt is tiring.

Write the three values into **D**, **E** and **F**. Leave **C `status` blank**; a human flips it to READY.

---

## What happens next

Back to `QDE_FamousCase_Story_Prompt_V4.md`, Stage B: Peggy/Claude writes the image prompt around the headline you
just chose, then the caption. Then a human sets `status` to READY and Betty takes it.
