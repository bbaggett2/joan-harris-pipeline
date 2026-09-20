# HU Description Prompt — V4

**Brand:** Handwriting University (HU) ONLY
**Owner:** Peggy Olson — she writes this package. Betty executes it, unchanged.
**Status:** Current
**Supersedes:** V3
**Companion:** `joan-supervising-agent/hu-video-pipeline/` — start at `00_OVERVIEW_V1.md`

> **What changed in V4 (2026-09-20):**
>
> 1. **All five outputs are now written in first person, as Bart — no exceptions.**
>    Bart: *"It seems the HU is outputting third-person summaries... this is not ideal.
>    I want to change it to first person for all platforms."* V3 implied this through
>    the "Write like Bart" voice note in §3 but never said it outright, and outputs were
>    drifting into third-person, editorial-style summaries (`Bart explains why...`,
>    `he shares three principles...`). **That drift ends here.** §3 now states the
>    point-of-view rule explicitly, with a banned/required example pair, and every
>    output section below (§4–§8) calls it out again at the point where it's easiest
>    to violate.
> 2. **Rationale, for the record:** research on narrative perspective and persuasion is
>    mixed rather than conclusive — first-person narration shows a real engagement
>    advantage in some studies (Cognition & Emotion, 2021) but not others (a 2026
>    study found no significant effect on empathy/identification). The clearer, more
>    consistently-replicated finding is that first-person self-referencing statements
>    ("I") tend to out-persuade second-person "you" statements, because "you" can read
>    as being told what to think or feel. This matches how comparable creator-led
>    personal-development channels (Mel Robbins, Mark Manson, Diary of a CEO) actually
>    write their descriptions — first person, as the creator, not as a summarizing
>    narrator. Bart made the call on 2026-09-20; this is not being sold as proven science.
>
> Every other copy rule is unchanged from V3.

> ⛔ **This file is HU only.** Do not use it for QDE / Handwriting Experts Inc.
> (use `qde_legal_description_prompt_V<n>.md`) or for The Bart Show / Bart Allan
> Baggett (no prompt written yet — STOP and flag to Joan).
> If the video is forensic, attorney-facing, or about document examination,
> you are in the wrong lane. Stop.

> **Brand facts — voice, banned terms, palette, domain — are governed by
> `brands/handwriting-university.md`.** §3 below summarizes the copy-relevant parts for
> convenience. Where the two disagree, the brand kit wins.

> **Name spellings are governed by `Peggy_Copy_Names_and_Spelling_v1.md`.** Do not
> restate its rules here; point at it.

---

## 0. HARD STOP BEFORE YOU WRITE ANYTHING

- [ ] The **cleaned VTT** (non-RAW) is open in front of you and read **end to end**.
- [ ] If no cleaned VTT exists → **STOP. Flag to Joan.** Do not write from the title,
      the filename, or the thumbnail. There is no exception to this.
- [ ] Name correction pass applied to the transcript per
      **`Peggy_Copy_Names_and_Spelling_v1.md` §1**. Both halves of the host's name are
      wrong independently — `Bert` / `Barb` / `Mark` on the given name, `Bagot` /
      `Bagget` / `Baget` / `Bagott` on the surname. ⚠️ `Bert` and bare `Barb` are
      **review flags, not automatic swaps** — a guest genuinely named Bert exists, and
      renaming him is the worse failure.

Every claim, chapter, name, story, and number in your output must trace to a line
in that transcript. If you cannot point at the line, it does not go in.

---

## 1. WHAT YOU DELIVER

**Five outputs, every time, in one pass.** Not four. Not "and reuse that one for
Facebook."

| # | Output | Goes to |
|---|---|---|
| 1 | YouTube description | YouTube |
| 2 | Instagram caption | Instagram Reel |
| 3 | TikTok caption | TikTok |
| 4 | Facebook caption — short | Facebook REEL |
| 5 | Facebook caption — long | Facebook POST |

⛔ **Never write one caption and spread it across platforms.** Metricool has a
single shared `text` field per post, so a bundled post silently forces one caption
onto every network. Each platform gets its own post and its own copy. See
`hu-video-pipeline/10_METRICOOL_DRAFTS_V<n>.md`.

Save all five to the video's `particles/` folder as
`<VID_ID>_Description_Package_v1.md` before the Metricool step begins.

**This file is the handoff.** Betty publishes from it verbatim and composes nothing.
Label every output by platform. A missing CTA, an unlabeled platform, third-person
narration, or a placeholder is a failed handoff — Betty will stop rather than fill
the gap or fix the voice.

---

## 2. THE CTA — REQUIRED ON ALL FIVE OUTPUTS

**Default (current):**

```
🔗 Free handwriting Level 100 course. Join our weekly live zoom class.
HandwritingUniversity.com
```

**Approved alternate** (longer, for YouTube body when the description has room):

```
🔗 Free handwriting resources, live classes, courses, and personality tools: HandwritingUniversity.com
```

Rules, no exceptions:

- ⛔ **"Link in bio" is BANNED on every platform, including Instagram.**
  Write the domain out.
- ⛔ **No copy sends the viewer to another company's platform.**
  Do not tell a reader to go watch, read, or continue somewhere we do not own — no
  "full breakdown on YouTube," no "see the rest on TikTok," no "link in our Facebook
  group," no naming another platform as the destination at all. Every platform's copy
  stands on its own and sends the reader to **HandwritingUniversity.com** and nowhere
  else. The audience we move is the one that lands on our own site; sending a Meta
  viewer to Google is unpaid work for someone else.
- The literal string `HandwritingUniversity.com` appears in every one of the five outputs.
- YouTube and Facebook POST also carry the bare URL `https://handwritinguniversity.com`
  on its own line so it renders clickable.
- A caption with no CTA is not finished copy. Do not hand it off.

---

## 3. BRAND VOICE

**Audience:** curious adults 25–55. Psychology, self-help, relationships. They want
to understand people, not become certified analysts.

**Voice:** witty, NPR-with-edge, psychology-forward. Confident and specific. Slightly
irreverent. Never academic, never courtroom, never motivational-poster.

**Write like:** Bart noticed something about a person and can't help telling you.

### 3.1 POINT OF VIEW — FIRST PERSON, ALWAYS (New in V4)

**Every one of the five outputs is written as Bart, in first person, using "I."**
Not a hired editor summarizing the video. Not a narrator describing what "Bart"
does in the third person. Bart, talking.

**Banned — third-person / editorial summary voice:**
> Bart explains why most people misunderstand confidence and shares three
> psychological principles he's learned from decades of studying human behavior.

**Required — first-person / Bart voice:**
> I spent most of my life thinking confident people were born different. I was
> wrong. After decades studying psychology, NLP, and human behavior, I've learned
> that confidence is something you can build — and most people are doing it
> backwards.

Working pattern for the opening lines of any output: **I → principle → you.**
State what Bart lived or discovered in first person, generalize it into the
principle, then bring it to the viewer. Do not skip the "I" step and start from
the principle — that's the third-person-summary failure mode this rule exists to
kill.

This applies to the **body copy** of every output. It does not ban second person
("you") or third-person references to other people mentioned in the video (a
guest, a historical figure, a client story) — it bans narrating **Bart himself**
from the outside. If you catch yourself writing "Bart," "he," or "the host" to
describe what the video's host says or does, stop and rewrite it as "I."

**Banned words in body copy:** `graphology`, `graphologist` (hashtags only).

**Banned openers:** "In this video…" · "Today we'll explore…" · "Have you ever wondered…"

**Banned generally:** hype words (Amazing, Shocking, Incredible, Mind-blowing) ·
em-dash pileups · AI-coded phrasing ("delve", "in today's fast-paced world",
"unlock the secrets") · outcome guarantees · diagnostic claims.

**Frame handwriting as a pattern-recognition tool, never a diagnosis.** If the
transcript makes a medical or clinical claim, keep Bart's framing attributed to him
("Bart's read is…" becomes, in first person, "My read is…" or "I read this as…")
rather than stating it as fact.

---

## 4. OUTPUT 1 — YOUTUBE DESCRIPTION

**Structure:** Hook → Body → Chapters → CTA → Hashtags

**Point of view:** first person throughout, per §3.1. The hook and body are Bart
talking, not a synopsis of Bart.

**Hook** — 2–3 sentences, first person. Curiosity gap. Tease the mechanism, never
resolve it. ("I used to think X. I was wrong." / "I spent years doing X before I
figured out why it wasn't working.")

**Body** — 4–6 paragraphs, drawn only from the transcript, written as Bart. Concrete
over abstract: name the letter, the stroke, the zone, the example Bart actually used.
Where Bart tells a story, keep the story in first person — the specificity is the
brand. End on the "so what": what the viewer does with this tomorrow.

**Chapters** — exact timestamps read off the VTT. Never estimated, never invented.
First entry must be `0:00` or YouTube will not build the chapter bar. Chapters go
**before** the CTA, never after it. Chapter labels are plain navigation labels, not
first- or third-person sentences — that rule doesn't apply to them. Format:

```
Chapters:

0:00 — <label>
0:28 — <label>
```

⛔ **Plain text only. No markdown.** No `###` headings, no backtick fences, no `**bold**`.
YouTube renders them literally and viewers see the hash marks. This has shipped
broken before — check it.

**CTA** — from §2. Place once mid-body (after the setup paragraphs) and once at the end.

**Hashtags** — 12–18. Always include `#HandwritingUniversity` and `#BartBaggett`.

---

## 5. OUTPUT 2 — INSTAGRAM CAPTION

- 80–150 words, first person throughout (§3.1)
- Hook opener — first line has to survive the "…more" truncation
- 2–3 punchy lines pulled from the transcript, written as Bart, short paragraphs,
  line breaks between
- Then the §2 CTA
- ⛔ Never "link in bio"
- ⛔ **Never point the reader to YouTube or any other platform.** The caption has to
  land on its own. If the clip needs the long video to make sense, that is a copy
  problem, not a reason to hand the viewer to another company.
- 8–12 hashtags, ending `#HandwritingUniversity #BartBaggett`

---

## 6. OUTPUT 3 — TIKTOK CAPTION

- Lead line under 150 characters, first person — one sharp claim, the whole hook
- Then the §2 CTA on its own lines
- 4–6 hashtags
- Native, declarative, no "watch to find out"

---

## 7. OUTPUT 4 — FACEBOOK SHORT (for the REEL)

- Hook line, first person — usually a first-person version of the video title
- Then the §2 CTA
- Then `https://handwritinguniversity.com`
- No hashtags needed. Keep it tight — Reels truncate hard.

---

## 8. OUTPUT 5 — FACEBOOK LONG (for the POST)

- Same shape as the YouTube description body, minus the chapters — first person
  throughout, per §3.1
- Facebook rewards longer narrative copy in-feed — do not just paste the short version
- CTA mid-body and again at the end, plus the bare URL
- First person throughout. Facebook reads as Bart talking, not as a page describing him.

---

## 9. FLAG, DON'T GUESS

Mark anything you cannot verify with `⚠️ TO VERIFY` and list it at the bottom of the
package. Real examples from past batches:

- A date or historical case that does not check out (the "1912 London Ripper" —
  the Ripper murders were 1888)
- A statistic or research consensus Bart asserts that you have not confirmed
- A book title or product you cannot confirm is still available
- A proper noun the transcriber may have mangled (Whisper turned "Nicole Kidman"
  into "Nico Kidman")

Correct obvious transcription errors of **names** silently, per
`Peggy_Copy_Names_and_Spelling_v1.md` §5. Everything else gets flagged for Bart,
not fixed by you.

---

## 10. SELF-CHECK — RUN BEFORE HANDOFF

- [ ] Cleaned VTT was read end to end
- [ ] All **five** outputs written, each distinct copy
- [ ] Each output labeled by platform
- [ ] **Every output is written in first person, as Bart** — no "Bart explains…",
      "he shares…", "the host discusses…", or any other third-person narration of
      Bart himself (§3.1)
- [ ] `HandwritingUniversity.com` appears in all five
- [ ] "Link in bio" appears in **none**
- [ ] **No output names another platform as a destination** — no "full breakdown on
      YouTube", no "see the rest on…", nothing sending the reader off our own site
- [ ] Zero markdown artifacts in the YouTube description (no `###`, no backticks)
- [ ] Chapters start at `0:00`, every timestamp exists in the VTT, and they sit
      **before** the CTA
- [ ] `graphology` / `graphologist` absent from all body copy
- [ ] Names spelled per `Peggy_Copy_Names_and_Spelling_v1.md` — "Bart Baggett"
      everywhere, and "Curt" is C-U-R-T if the father is mentioned
- [ ] No banned openers, no hype words
- [ ] `⚠️ TO VERIFY` list attached (or explicitly "none")
- [ ] Package saved to `particles/` as `<VID_ID>_Description_Package_v1.md`

---

## ⚠️ OPEN — needs Bart's confirmation

V2 ended: *"Joan takes the package to Bart for sign-off. Nothing is pasted into
YouTube or Metricool before that sign-off."* That was carried forward into V3
unchanged because changing an approval gate is not Peggy's call — **but it
contradicts the current pipeline.** The lane now has two human touchpoints: someone
drops the video in the Ready-to-Publish folder, and the reviewer makes the YouTube
video public and schedules the Metricool drafts. There is no pre-paste copy
sign-off; copy reaches Bart sitting in the private video and the draft planner.

**Either this line goes, or the pipeline gets a gate back.** It should not stay
ambiguous. Flagged 2026-09-19, still open at V4.
