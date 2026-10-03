# QDE Famous-Case Research Prompt — deep research, primary documents
**Version:** v4 · **Prepared:** 2026-10-03 · **Lane:** Handwriting Experts Inc. / QDE only
**Runs as:** the deep-research step of the n8n workflow *Peggy — Stories into Blog Rows* (and the *Deep fact re-check*
workflow), or a Claude task with web search when run by hand
**Feeds:** `QDE_Post_Queue` (Google Sheet `14pkeLjlH5SFf4X_DwafTCJlgdKRNOcY-p_AAbZjxfec`, tab gid 0) — **update that
spreadsheet; never create a new one** — plus one evidence folder per story in Google Drive (*QDE Evidence*)
**Then:** `Headline-QDE-Post.md` (headline rules) → `QDE_FamousCase_Story_Prompt_V5.md` (Peggy writes the copy)
**Also read:** `BART_FORENSIC_PERSPECTIVES.md` — Bart's own positions and stories, for the personal angle

**Supersedes v3.** v3 asked for "two sources" and stopped at news coverage. On 2026-10-02 Bart re-researched ten
stories by hand and found what the automated pass missed: the actual 8-page Michael Jackson will PDF, the federal
docket order barring forgery evidence (Branca v. Mann, filing 163), his own name in Randall Sullivan's source notes,
the Second Circuit *United States v. Amiel* opinion with the prison terms, and a Smithsonian object catalogued as
crime evidence. **v4 makes that hunt the job.** News stories are where the search starts, not where it ends.

v3's §4 line "nothing that names a living private person as a wrongdoer unless a court did" is replaced by Bart's
2026-10-02 rule: **accused is good enough** — write *accused* or *charged*, never *guilty*, and add a ⚠️ PENDING line.

---

## 1. What counts as a story (the five gates — unchanged in substance)

1. **A recognizable name** — a famous person or an institution every trial lawyer knows. Nationwide audience;
   international cases Americans know qualify.
2. **A document or handwriting is at the center** — a will, signature, letter, diary, contract, deed, manuscript,
   confession, print, autograph.
3. **Something gritty** — forgery, theft, fraud, a contested estate, a prison sentence, a family at war.
4. **A forensic tell or a court ruling on the paper** — an examiner, a lab, a jury or a judge decided the paper
   question. If nobody examined the document, the angle must be bigger (how courts handle the claim, why no examiner
   was ever named, undue influence vs. forgery).
5. **Public record.** Closed cases preferred. Active litigation only for public figures; living people accused are
   written as *accused*.

**Bart's name in the record is a feature, not a disqualifier.** A case where Bart was *retained and wrote a
confidential report* stays out. A case where a book, article or court paper *mentions* Bart is gold — see §3.

---

## 2. The document hunt — required for every story

The finished research must point a reader at the paper itself. Search each tier below. For every tier write either
what you found (with the direct URL) or "searched, nothing found".

| Tier | What to look for | Where |
| :--- | :--- | :--- |
| **A. The questioned document itself** | a scan or PDF of the will, letter, signature, check, print, autograph; which page shows what | law-firm blogs, The Smoking Gun, court exhibits, archive and museum scans, news PDF embeds |
| **B. Court records** | docket entries, orders, minute entries, verdicts, probate filings, appellate opinions, sentencing | CourtListener / RECAP, Justia Dockets and Justia Law, Casetext, FindLaw, Google Scholar case law, state appellate sites, Indian Kanoon, BAILII |
| **C. Government releases** | DOJ / US Attorney press releases, FBI artifact and case pages, postal inspector, police and prosecutor statements | justice.gov, fbi.gov, uspis.gov |
| **D. Institutions** | museum object records (look for "crime evidence"), library and archive catalog entries, university findings | si.edu, museum collection databases, library catalogs |
| **E. Books and long-form** | biographies and their **source notes / chapter notes**, long magazine features, academic papers | Google Books, archive.org, publisher pages, JSTOR abstracts, Vanity Fair, New Yorker, Smithsonian |
| **F. Testimony and transcripts** | deposition or trial transcripts, sworn declarations, expert designations, who the handwriting experts were and what they said | court record sites, Scribd uploads of filings, news quoting testimony |
| **G. Images for the post** | photos of the document, the exhibit, the seized items, the signatures side by side | the sources above; museum and government images first |

**Required searches** (in addition to the case itself):
- `"<case>" will PDF` · `"<case>" docket` · `"<case>" court opinion` · `"<case>" handwriting expert` ·
  `"<case>" forensic document examiner testified`
- `"<case>" sentenced` / `convicted` / `pleaded guilty` — and the names of anyone charged
- **`"Bart Baggett" "<famous name>"`** and **`"Baggett" "<famous name>" handwriting`** — every story, every time
- one search for an **adjacent, stronger case**: the same scheme with a conviction, the same document type with a
  ruling (see §4)

**Court ruling vs. forensic finding.** Never write that a court "found the signature genuine" unless a court said so.
Admitting a will to probate, dismissing a challenge for lack of standing, or excluding forgery evidence in a motion in
limine are procedural results, not forensic findings. Say exactly which one happened.

**Open the page.** Cite only URLs you actually opened in this session. Wikipedia is a map to sources, never a source.
A pirated book mirror can be cited as "text of <book>, ch. N" but name the book, author and year.

---

## 3. The Bart connection

Report every public mention of Bart Baggett tied to the case: where (book, chapter, page or note), the exact words,
and what it does and does not establish. Example from 2026-10-02: Sullivan, *Untouchable* (2012), source notes for
the Jackson will chapter — "Handwriting expert (Bart Baggett): witnessed Sanders and Mann discussing it." It
establishes that Bart's name was discussed; it does **not** establish that he was hired, examined the will, or wrote a
report. Bart's own account of what happened belongs to `BART_FORENSIC_PERSPECTIVES.md` and the story file's
**BART PERSPECTIVE** section — never invent it.

---

## 4. Upgrade the story

If a stronger, sourced angle sits next to the pitch, say so and lay it out. 2026-10-02 example: "Dalí signed blank
sheets and the market collapsed" became "three members of the Amiel family went to federal prison for 78, 46 and 33
months" with the Second Circuit opinion and a Smithsonian object catalogued as crime evidence. Keep the story Bart
pitched unless the upgrade is plainly better and on the same case; never swap in a different case silently.

---

## 5. The fact card (column N `fact_status`) and the dossier

**Fact card** — short, for a busy human, max ~2,500 characters:

```
CASE: <person/institution> — <one-line what happened>
WHEN/WHERE:
THE DOCUMENT: what it was, what it claimed, what it was worth — and where the scan is
THE CRIME / THE DISPUTE: who did or alleged what, to whom, for how much
THE TELL: what the examination or ruling found, who, how — or "no examiner's finding is public"
THE OUTCOME: verdict, sentence, ruling, settlement, what happened to the document
THE DETAILS THAT MAKE IT A STORY: 3–5 specifics with numbers
BART CONNECTION: the public mention, or "none found"
SOURCES: url — what it supports (primary records first)
⚠️ anything single-sourced, disputed, or about Bart's own role
```

**Dossier** — long, saved as `dossier.md` in the story's evidence folder in Drive: everything found in the §2 tiers,
the exhibit list (direct URL, type, which page shows what), quotes worth using with their source, the §3 Bart
connection, the §4 upgrade, open questions, and a "best visuals" list. The blog writer reads the dossier.

**Exhibits** — every direct link to a PDF or image of the document, the court record, the evidence, or the people.
The workflow downloads these into the evidence folder, so give the direct file URL when one exists.

Rules: two independent sources for any number, date or sentence, or it goes under ⚠️. Never write a fact from memory.
Victims named once, factually. Living people not convicted: *accused* or *charged* and a ⚠️ PENDING line.

**SCENE** (column H `face_source`) is the whole visual brief: who is in frame and how to describe them (decade,
expression, clothing, mood) or why nobody is, plus period, setting and props — and the real document or exhibit if a
scan exists. Positive statements only.

---

## 6. Hand off and write the row

Stage 2 headline rules: `Headline-QDE-Post.md` (in the automated run the headline is Bart's/RICK's title, verbatim).
Stage 3 copy: `QDE_FamousCase_Story_Prompt_V5.md`. Research fills A `post_id`, B `title`, G `torn_note`,
H `face_source`, M `facts_need_verify`, N `fact_status`; the evidence-folder link goes in the notes column.
**Status on arrival: blank.** Katie types READY in column C after review. The column ownership table in the story
prompt governs.

---

## 7. What this task never does

- Never sets `READY`.
- Never creates a spreadsheet, a tab, or a copy of the sheet.
- Never writes a headline, caption or image prompt.
- Never presents Bart's personal account, or a book's mention of Bart, as proof that he examined a document.
- Never states a court authenticated a signature unless it did (see §2).
- Never rejects quietly: a rejection says which gate and why, on Slack, so a good story is never lost.
