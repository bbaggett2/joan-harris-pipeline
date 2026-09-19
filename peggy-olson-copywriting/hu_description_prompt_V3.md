# HU Description Prompt — V3

**Brand:** Handwriting University (HU) ONLY
**Owner:** Peggy Olson — she writes this package. Betty executes it, unchanged.
**Status:** Current
**Supersedes:** V2
**Companion:** `joan-supervising-agent/hu-video-pipeline/` — start at `00_OVERVIEW_V1.md`

> **What changed in V3 (2026-09-19):**
>
> 1. **No copy sends the viewer to another company's platform.** Bart: *"I don't want any copy pushing the user to another platform that is owned by a different company."* V2 §5 told the Instagram caption to carry the line `Full breakdown on YouTube`. **That line is deleted.** The rule is now stated generally in §2 so it cannot reappear on a different platform.
> 2. **Companion pointer corrected.** V2 named `HU_Video_Publishing_Pipeline_V9.md`, which no longer exists. The lane is now the step files in `joan-supervising-agent/hu-video-pipeline/`.
>
> Every other copy rule is unchanged from V2.

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
Label every output by platform. A missing CTA, an unlabeled platform, or a placeholder
is a failed handoff — Betty will stop rather than fill the gap.

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
- ⛔ **No copy sends the viewer to another company's platform.** *(New in V3, Bart 2026-09-19.)*
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

**Banned words in body copy:** `graphology`, `graphologist` (hashtags only).

**Banned openers:** "In this video…" · "Today we'll explore…" · "Have you ever wondered…"

**Banned generally:** hype words (Amazing, Shocking, Incredible, Mind-blowing) ·
em-dash pileups · AI-coded phrasing ("delve", "in today's fast-paced world",
"unlock the secrets") · outcome guarantees · diagnostic claims.

**Frame handwriting as a pattern-recognition tool, never a diagnosis.** If the
transcript makes a medical or clinical claim, keep Bart's framing attributed to him
("Bart's read is…") rather than stating it as fact.

---

## 4. OUTPUT 1 — YOUTUBE DESCRIPTION

**Structure:** Hook → Body → Chapters → CTA → Hashtags

**Hook** — 2–3 sentences. Curiosity gap. Tease the mechanism, never resolve it.
Second person where natural.

**Body** — 4–6 paragraphs, drawn only from the transcript. Concrete over abstract:
name the letter, the stroke, the zone, the example Bart actually used. Where Bart
tells a story, keep the story — the specificity is the brand. End on the "so what":
what the viewer does with this tomorrow.

**Chapters** — exact timestamps read off the VTT. Never estimated, never invented.
First entry must be `0:00` or YouTube will not build the chapter bar. Chapters go
**before** the CTA, never after it. Format:

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

- 80–150 words
- Hook opener — first line has to survive the "…more" truncation
- 2–3 punchy lines pulled from the transcript, short paragraphs, line breaks between
- Then the §2 CTA
- ⛔ Never "link in bio"
- ⛔ **Never point the reader to YouTube or any other platform.** *(V2 carried the line
  `Full breakdown on YouTube` here. Deleted in V3 — see §2.)* The caption has to land
  on its own. If the clip needs the long video to make sense, that is a copy problem,
  not a reason to hand the viewer to another company.
- 8–12 hashtags, ending `#HandwritingUniversity #BartBaggett`

---

## 6. OUTPUT 3 — TIKTOK CAPTION

- Lead line under 150 characters — one sharp claim, the whole hook
- Then the §2 CTA on its own lines
- 4–6 hashtags
- Native, declarative, no "watch to find out"

---

## 7. OUTPUT 4 — FACEBOOK SHORT (for the REEL)

- Hook line — usually the video title, plain
- Then the §2 CTA
- Then `https://handwritinguniversity.com`
- No hashtags needed. Keep it tight — Reels truncate hard.

---

## 8. OUTPUT 5 — FACEBOOK LONG (for the POST)

- Same shape as the YouTube description body, minus the chapters
- Facebook rewards longer narrative copy in-feed — do not just paste the short version
- CTA mid-body and again at the end, plus the bare URL
- First person where the transcript is first person. Facebook reads as Bart talking.

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
YouTube or Metricool before that sign-off."* That is carried forward here unchanged
because changing an approval gate is not Peggy's call — **but it contradicts the
current pipeline.** The lane now has two human touchpoints: someone drops the video in
the Ready-to-Publish folder, and the reviewer makes the YouTube video public and
schedules the Metricool drafts. There is no pre-paste copy sign-off; copy reaches Bart
sitting in the private video and the draft planner.

**Either this line goes, or the pipeline gets a gate back.** It should not stay
ambiguous. Flagged 2026-09-19.
