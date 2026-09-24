# QDE Famous-Case Research Prompt — one new story a day
**Version:** v2 · **Prepared:** 2026-09-15 · **Runs as:** a Claude task with web search and the Google Sheets connection (scheduled, or "find the next story" in chat) · **Lane:** Handwriting Experts Inc. / QDE only
**Feeds:** one new row in `QDE_Post_Queue` (Google Sheet `14pkeLjlH5SFf4X_DwafTCJlgdKRNOcY-p_AAbZjxfec`, tab gid 0) — **update that spreadsheet; never create a new one**
**Then:** `Headline-QDE-Post.md` (RICK writes the headline) → `QDE_FamousCase_Story_Prompt_V4.md` (Peggy writes the image prompt and the caption)

**Supersedes v1**, which pointed at `QDE_FamousCase_Story_Prompt_v1.md` in three places. That file was deleted on
2026-09-15 along with V2 and V3; the live copy step is **V4**.

Division of labor, fixed — **three stages, one owner each:**

| Stage | Who | Produces |
| :--- | :--- | :--- |
| 1. Find and verify the story | **Claude** — this file | the fact card, written into the row |
| 2. Name it | **RICK** — `Headline-QDE-Post.md` | `headline`, `gold_word`, `subline` |
| 3. Write it | **Peggy / Claude** — `QDE_FamousCase_Story_Prompt_V4.md` | `image_prompt`, `caption` |

**Claude does not write the headline. RICK does not do the research.** v1 blurred this by asking RICK for case facts
first; see §5.

---

## 1. What counts as a story

Every candidate must clear all five:

1. **A recognizable name.** A famous person, or an institution everyone knows (the FBI, the Library of Congress, the LDS Church, Sotheby's, Stern, the Vatican). Test: would a trial lawyer anywhere in the United States know the name without a Wikipedia link. The audience is nationwide — cases from any state, or international cases Americans know (the Hitler Diaries, the Vatican's forged letters), all qualify; nothing is weighted toward Texas.
2. **A document or handwriting is at the center.** A will, a signature, a letter, a diary, a contract, a deed, a manuscript, a confession. The crime is *on paper* — that's what makes it Bart's beat and not generic true crime.
3. **Something gritty or salacious.** Forgery, theft, fraud, a contested estate, a fake death, a bomb, a prison sentence, a family at war over a couch will. Polite academic disputes don't qualify. Any public figure or elected official is juicy good content.
4. **A forensic tell.** Somewhere in the record an examiner, a lab, or a jury decided the paper question — ink, paper, letterforms, pressure, a countersignature, a thumbprint. If nobody ever examined the document, it can still be a post, but the angle has to be bigger than forensic document examination. Example... the decline of cursive handwriting or the procedure courts allow expert testimony. 
5. **Public record, closed case.** Convictions, verdicts, published findings, deaths more than a few years back. No active litigation unless it involves politicians or celebrities. Avoid living private individuals accused of anything that is not in the media.

**Gate 4 is a factual test, not an editorial one.** On 2026-09-15 it disqualified four of ten candidates: the Boston
Strangler (no questioned-document examination exists anywhere in the case), Son of Sam (no named examiner; a parking
ticket broke it), the Black Dahlia (only an unnamed comparison, and the case is still open, so it fails gate 5 too),
and a Napoleon pitch with no case behind it at all. A famous name and a good story are not enough.

Beats to rotate through, so the feed doesn't become five forgers in a row: celebrity wills and estates · literary and historical manuscript forgery · art-world document fraud · signed-memorabilia and autograph rings · political and diplomatic forgeries · religious relics and letters · financial forgeries (checks, bonds, deeds) · impostors and fake credentials · a "the expert got it wrong" case.

---

## 2. Search

Run at least six searches before choosing. Mix these shapes, changing the noun each day:

- `[celebrity] will contested handwriting`  ·  `holographic will jury forgery`
- `forged [Lincoln|Washington|Twain|Hemingway] letters dealer arrested`
- `document examiner testimony famous forgery case`
- `autograph forgery ring FBI [Operation name]`
- `[institution] archive theft manuscript convicted`
- `forensic ink analysis proved forgery` · `paper analysis exposed fake`
- `"questioned document" famous case` · `celebrity estate signature dispute verdict`

Read past the first result. The best material is in a long feature (New Yorker, Smithsonian, Vanity Fair, a court opinion, a university archive page), not a listicle. Note every source URL as you go.

**Dedupe.** Before committing, read column B (`title`) of the sheet and the `post_id` list. Skip anything already there, and skip anything within two weeks of the same beat (two wills in a row is fine; two Lincoln forgers is not).

---

## 3. Pick one

Score the top three candidates 1–5 on each of: name recognition · how bad the crime is · how clean the forensic tell is · how much verifiable detail exists. Highest total wins. Ties go to the more recent case. Write the other two into the day's Slack note so tomorrow starts with a shortlist.

---

## 4. Verify and write the fact card

For the chosen case, build a fact card. Every line is a fact with a source, or a ⚠️.

```
CASE: <person/institution> — <one-line what happened>
WHEN/WHERE:
THE DOCUMENT: what it was, what it claimed, what it was worth
THE CRIME: who did what, to whom, for how much
THE TELL: what the examination found, who found it, how (ink/paper/letterforms/countersignature/print)
THE OUTCOME: verdict, sentence, what happened to the document
THE DETAILS THAT MAKE IT A STORY: 3–5 specifics (a $10 sale, two hours at a visitor book, a thumbprint on an envelope)
SOURCES: url — what it supports
⚠️ UNVERIFIED: anything from one weak source, anything sources disagree on, anything about Bart
SCENE: the full brief for the graphic — who should be in the frame and how to describe them (decade, expression,
       clothing, mood), or why nobody is; plus period, setting and props. This becomes column H.
```

Rules: two independent sources for any number, date, or sentence length, or it goes under ⚠️. Wikipedia is a map to sources, not a source. Never write a fact from memory. Victims are named once, factually. Nothing that names a living private person as a wrongdoer unless a court did.

**The SCENE field is the whole visual brief, and it is where the visual work stops.** The image prompt is written
later, at Stage 3, because it quotes the headline and the headline does not exist yet. Do not pre-write column J,
and never with `[[HEADLINE]]`-style placeholders — that was tried on 2026-09-15 and rejected.

**Write the ⚠️ lines so a human reads them, not RICK.** They stay in `fact_status` and are stripped before anything
is pasted into RICK, which will otherwise treat a warning as material and put it in a headline.

---

## 5. Hand off

**Stage 2 — RICK names it.** Open a **new** R.I.C.K. session and follow `Headline-QDE-Post.md`. It specifies exactly
what to paste (the sourced narrative from column N, stopping at the first ⚠️, plus columns G and H), the approved
headline library, and the six-point acceptance test on what comes back.

⚠️ **v1 also asked RICK for the case facts first — *"tell me more about this story"* — and that step is removed.**
It contradicted §4 of this very file: RICK's relay of a source is a lead, not a source. Running it is how unverified
claims reached finished copy. **RICK receives a finished fact card and writes only the headline, the gold word and
the sub-line.**

**Stage 3 — Peggy writes it.** `QDE_FamousCase_Story_Prompt_V4.md` covers the image prompt and the caption, and
carries the completeness gate that must pass before the row goes READY.

---

## 6. Write the row

Append one row to `QDE_Post_Queue` with the next `post_id` in sequence. **This task fills only its own columns:**

| Col | Field |
| :--- | :--- |
| A | `post_id` |
| B | `title` — case name, for humans |
| G | `torn_note` — 3 to 4 fragments, `·` separated |
| H | `face_source` — the SCENE field from the fact card |
| M | `facts_need_verify` — `YES` if any ⚠️ remains |
| N | `fact_status` — the sourced narrative, then every ⚠️ |

**Everything else belongs to a later stage. The full ownership table is in `QDE_FamousCase_Story_Prompt_V4.md` and it
governs.** v1 listed all twenty columns here and so did the old story prompt; two files claiming the same fields is
what left QDE-FC-16 through FC-21 stalled half-filled on 2026-09-15.

Write clean UTF-8 — the v1 seed CSV was imported as Mac-Roman and every dash became `‚Äî`; rows 2–6 still carry it.

**Status on arrival: blank.** A person flips it to `READY`. That is the one glance the pipeline keeps at the front — a new case is a brand decision (does Bart want a dictator's face on his feed?), and it costs five seconds. **A row is not ready for that glance until Stages 2 and 3 are done and V4's completeness gate passes.**

Post one line to `#qde-celebrity-post-review`: *"New case queued: QDE-FC-## — <title>. Runners-up: <two>. Needs headline and copy."*

---

## 7. What this task never does

- Never sets `READY` itself.
- Never creates a spreadsheet, a tab, or a copy of the sheet.
- Never writes a headline, a caption, or an image prompt. Those are Stages 2 and 3.
- Never asks RICK for facts.
- Never uses a case Bart worked, an open case, or a living private non-public figure whose case is not already in the news cycle or was in the news cycle. 
- Never runs the same beat two days running.

## 8. What happens in the gate fails.
- Don't reject something quietly and never notify anyone
- Notify through Slack and claude.
- We don't want to lose good stories because you did't reach out to a human and explain whey you rejected and article.
