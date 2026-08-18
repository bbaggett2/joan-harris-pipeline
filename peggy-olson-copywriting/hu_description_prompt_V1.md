# HU Description Prompt — V1

**Brand:** Handwriting University (HU) ONLY
**Status:** Current
**Supersedes:** `Ai Prompt Documents/handwriting_university_description_promptv3.md` (local, retired)
**Companion:** `HU_Video_Publishing_Pipeline_V8.md`

> ⛔ **This file is HU only.** Do not use it for QDE / Handwriting Experts Inc.
> (use `qde_legal_description_prompt_V6.md`) or for The Bart Show / Bart Allan
> Baggett (no prompt written yet — STOP and flag to Joan).
> If the video is forensic, attorney-facing, or about document examination,
> you are in the wrong lane. Stop.

---

## 0. HARD STOP BEFORE YOU WRITE ANYTHING

- [ ] The **cleaned VTT** (non-RAW) is open in front of you and read **end to end**.
- [ ] If no cleaned VTT exists → **STOP. Flag to Joan.** Do not write from the title,
      the filename, or the thumbnail. There is no exception to this.
- [ ] "Baggett" correction pass applied to the transcript (`Bagot`, `Bagget`,
      `Baget`, `Bagott`, `Bert`, `Mark Baggett` → `Bart Baggett`).

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
`HU_Video_Publishing_Pipeline_V8.md` Phase 8.

Save all five to the video's `particles/` folder as
`<VID_ID>_Description_Package_v1.md` before Phase 8 begins.

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
First entry must be `0:00` or YouTube will not build the chapter bar. Format:

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
- Then: `Full breakdown on YouTube` followed by the §2 CTA
- ⛔ Never "link in bio"
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

Correct obvious transcription errors of **names** silently. Everything else gets
flagged for Bart, not fixed by you.

---

## 10. SELF-CHECK — RUN BEFORE HANDOFF

- [ ] Cleaned VTT was read end to end
- [ ] All **five** outputs written, each distinct copy
- [ ] `HandwritingUniversity.com` appears in all five
- [ ] "Link in bio" appears in **none**
- [ ] Zero markdown artifacts in the YouTube description (no `###`, no backticks)
- [ ] Chapters start at `0:00` and every timestamp exists in the VTT
- [ ] `graphology` / `graphologist` absent from all body copy
- [ ] "Bart Baggett" spelled correctly everywhere
- [ ] No banned openers, no hype words
- [ ] `⚠️ TO VERIFY` list attached (or explicitly "none")
- [ ] Package saved to `particles/` as `<VID_ID>_Description_Package_v1.md`

Peggy reviews for voice. Joan takes it to Bart for sign-off. Nothing is pasted into
YouTube or Metricool before that sign-off.
