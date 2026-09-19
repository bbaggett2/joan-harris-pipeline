# QDE Video Title + Description — The RICK Prompt
**Stage A (title) and Stage B (description), one continuous RICK session.** · Prepared 2026-09-19 · **Lane:** QDE only
**RICK:** https://chatgpt.com/g/g-u9LaoH9J2-r-i-c-k — **open a NEW session every time. Never continue an old one.**

This file exists because two real things were true at once and needed reconciling: (1) `How_to_get_the_perfect_Title_and_Description_SOP.docx` documents the actual, human-run process — paste transcript, get a title, same session, ask for a description — and (2) `qde_legal_description_prompt_V6.md` is the actual, current QDE brand rulebook (audience modes, hard rules, banned terms, TO VERIFY flagging) that RICK has never been shown. This file merges them: RICK's real two-stage process, carrying V6's real rules instead of the thinner rules the old docx alone would produce. It supersedes nothing — the docx's *process* stays the process; this is what actually goes in the paste.

---

## Before you paste

1. Get the cleaned VTT transcript for the video (file 03 in the pipeline; if working by hand, the editor-supplied `.vtt`).
2. Have `BART_BAGGETT_VOICE.MD` and `brands/qde-brand.md` open — paste their content in below the transcript. RICK has no file access; it only knows what's in the message.
3. Know the video's likely audience mode before you start (attorney vs. consumer) — see the rule below. If genuinely unsure, paste the transcript and ask RICK to state which it detects before writing anything.

---

## Stage A — Title

```
I need a scroll-stopping title for this YouTube video, for Bart Baggett's forensic
document examination channel (Handwriting Experts Inc. — signature forgery,
disputed wills and contracts, expert witness testimony). We will also use this
title on the YouTube thumbnail, so it can't be wordy.

Read the transcript below end to end before writing anything.

Rules, all of them hard:
- Hide the answer. Name the category of thing at stake (a signature, a will, a
  prenup, a lease, a piece of evidence) — never the specific fact or twist the
  video reveals. Someone should need to watch to find out the answer, not be
  able to answer just by reading the title.
- Lead with what a stranger recognizes — the document, the crime, the famous
  name, the amount of money, the courthouse — never the forensic method itself.
- Second person when the video's real subject is a risk any viewer could face
  ("Is Your Signature Real?"). Third person when it's really about a specific
  named case or public figure — don't force "you" onto someone else's story.
- Under 10 words. No colon-subtitles. No em dashes. Plain, specific, serious —
  curiosity yes, hype no.
- Never promise or imply a case outcome. Never make a famous person the author
  of a crime they were the victim of.
- No "Shocking / Secret / Unbelievable / You Won't Believe." "Exposed" only
  when literally true to the case.
- No jargon a stranger wouldn't know ("FDE," "questioned document examination").
  Never "graphology" or "graphologist" — that's a different brand's territory.
- No credentials or taglines in the title itself, no episode numbers or
  internal codes.

Give me your best single title, and tell me whether this video reads as
ATTORNEY mode (peer-to-peer, litigators and trial attorneys) or CONSUMER mode
(a scared layperson with a real legal problem) — say which and why in one
sentence.

Here is the transcript:
<<< paste the cleaned VTT here >>>
```

Read the result. If it states or implies the answer, restates a specific fact from the transcript, uses a banned word, or runs long, say which rule it broke and ask again **in the same session** — same discipline as the headline prompt. Don't fix it yourself.

---

## Stage B — Description (same session, after a title is settled)

```
Good. Now write the YouTube description for this video, using the transcript
for the facts and the title we just settled on.

Voice — read this before writing a word:
<<< paste the full contents of BART_BAGGETT_VOICE.MD here >>>

Brand facts — domains, banned terms, credentials, hard rules. Use only what's
here; invent nothing:
<<< paste the full contents of brands/qde-brand.md here >>>

Audience mode: <<< ATTORNEY or CONSUMER, from Stage A >>>. If attorney, write
peer-to-peer — validate them, don't lecture. If consumer, calm and plain —
they're scared; explain options and next steps, not just the forensic detail.
If the video genuinely straddles both, lead consumer and add one paragraph
signalling to attorneys that this is the kind of work Bart does.

Structure:
- Open with 1-2 sentences that hook without giving away the answer the title
  already protects.
- 2-4 short paragraphs (this is spoken, not written — Bart never sounds
  impressed with himself, explains why before how, avoids absolutes).
- Chapters/timestamps ONLY if you can point to the exact moment in the
  transcript — never estimate a time. If you can't tie a moment to a real
  timestamp, skip chapters entirely rather than guess.
- End with the CTA and both domains from the brand facts above, plus the
  phone number, exactly as written there — do not alter, shorten, or invent a
  domain.
- Close with hashtags, count and mix per the brand facts.

Flag anything you're not fully certain of — a claim, a date, a legal fact, an
outcome implied on camera but not stated in the copy — under a heading called
TO VERIFY, one line each, so a human checks before this goes live. Don't just
omit an uncertain claim silently; flag it.

It must contain "Bart Baggett" by name at least once. It must never promise or
imply how the case turns out, even if the transcript itself does.
```

---

## Then check what RICK returns

All of these must pass before this goes anywhere near the pipeline:

1. Title hides the answer, matches Stage A's rules, under 10 words.
2. Description names Bart Baggett, ends with the CTA and domains exactly as given in the brand facts pasted above — not a domain RICK invented or half-remembered.
3. No outcome promise anywhere, even if the transcript's own audio states one.
4. Every proper noun, date, and number traces to the transcript. **RICK invents confidently when it runs out of real material** — anything that isn't in the transcript goes in TO VERIFY, or gets cut.
5. No banned term: no "graphology"/"graphologist," no `HandwritingExpert.com` (it's `HandwritingExpertUSA.com`), no FDE jargon, no unverified credential from the brand kit's own "not yet confirmed" list.
6. A TO VERIFY section exists whenever there's anything short of fully certain — if RICK returns none, ask directly whether it's confident on every fact, don't assume silence means clean.

If a line fails, say which rule it broke and ask again in the same session. Don't fix it yourself — same rule as the headline prompt: this is RICK's job, not the human's or Claude's.

---

## What happens next

Once both stages pass, this is the same handoff the old docx already describes: upload the final title + description into a Google Doc in the video's project folder — or, if this is feeding the automated pipeline, this is what should replace the current `Copy: title+description+captions` node's own gpt-4.1 approximation for the title/description portion (captions can stay as-is, or get the same treatment later — this file doesn't cover captions).

**Known gap, stated plainly:** this file has not yet been tested end-to-end with a real transcript. The paste blocks above are built from real source material (the docx's actual process, V6's actual rules, the brand kit's actual facts) rather than a guess, but "built correctly" and "tested and working" are different claims. Run it once against a real VTT before trusting it in production.
