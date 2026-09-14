# QDE Famous-Case Research Prompt — one new story a day
**Version:** v1 · **Prepared:** 2026-09-12 · **Runs as:** a Claude task with web search and the Google Sheets connection (scheduled, or "find the next story" in chat) · **Lane:** Handwriting Experts Inc. / QDE only
**Feeds:** one new row in `QDE_Post_Queue` (Google Sheet `14pkeLjlH5SFf4X_DwafTCJlgdKRNOcY-p_AAbZjxfec`, tab gid 0) — **update that spreadsheet; never create a new one**
**Then:** `QDE_FamousCase_Story_Prompt_v1.md` (RICK for headline and copy; Claude for the rest)

Division of labor, fixed: **Claude finds and verifies the story. RICK names it and writes it snappy.** Claude does not write the headline. RICK does not do the research.

---

## 1. What counts as a story

Every candidate must clear all five:

1. **A recognizable name.** A famous person, or an institution everyone knows (the FBI, the Library of Congress, the LDS Church, Sotheby's, Stern, the Vatican). Test: would a trial lawyer anywhere in the United States know the name without a Wikipedia link. The audience is nationwide — cases from any state, or international cases Americans know (the Hitler Diaries, the Vatican's forged letters), all qualify; nothing is weighted toward Texas.
2. **A document at the center.** A will, a signature, a letter, a diary, a contract, a deed, a manuscript, a confession. The crime is *on paper* — that's what makes it Bart's beat and not generic true crime.
3. **Something gritty or salacious.** Forgery, theft, fraud, a contested estate, a fake death, a bomb, a prison sentence, a family at war over a couch will. Polite academic disputes don't qualify.
4. **A forensic tell.** Somewhere in the record an examiner, a lab, or a jury decided the paper question — ink, paper, letterforms, pressure, a countersignature, a thumbprint. If nobody ever examined the document, it's not a post.
5. **Public record, closed case.** Convictions, verdicts, published findings, deaths more than a few years back. No active litigation, no living private individuals accused of anything, nothing Bart himself worked on (those are a different series).

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
FACE: who should be in the frame and how to describe them for the image model (decade, expression, clothing, mood) — the graphic is rendered, not licensed
```

Rules: two independent sources for any number, date, or sentence length, or it goes under ⚠️. Wikipedia is a map to sources, not a source. Never write a fact from memory. Victims are named once, factually. Nothing that names a living private person as a wrongdoer unless a court did.

---

## 5. Hand off to RICK (headline + copy)

Open a **new** R.I.C.K. session (https://chatgpt.com/g/g-u9LaoH9J2-r-i-c-k). Paste the fact card. Then run the two prompts in `QDE_FamousCase_Story_Prompt_v1.md`: *"tell me more about this story"* (RICK will add color — anything new it adds goes back through step 4 before it's used), then the headline prompt. Take the pick. Then ask RICK for the caption under the Step 3 rules (under 200 words, five parts, "I wasn't involved," attorneys line) and paste the result back into Claude for the fact check and the banned-word pass.

---

## 6. Write the row

Append one row to `QDE_Post_Queue` with the next `post_id` (QDE-FC-6, 7, …), every column from the story prompt's Step 5 table, `image_url` and `publish_date` blank (Betty dates it: one post per weekday, 24 hours apart), the fact card's ⚠️ lines in `fact_status`, and `facts_need_verify` set accordingly.

**Status on arrival: blank.** A person flips it to `READY`. That is the one glance the pipeline keeps at the front — a new case is a brand decision (does Bart want a dictator's face on his feed?), and it costs five seconds. Once it's `READY`, Betty does the rest with no one in the loop.

Post one line to `#qde-celebrity-post-review`: *"New case queued: QDE-FC-6 — <headline>. Runners-up: <two>. Set READY to schedule."*

---

## 7. What this task never does

- Never sets `READY` itself.
- Never creates a spreadsheet, a tab, or a copy of the sheet.
- Never writes a headline or a caption in its own voice — that's RICK's job and then Peggy's rules.
- Never uses a case Bart worked, an open case, or a living private person.
- Never runs the same beat two days running.
