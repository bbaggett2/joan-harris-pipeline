# 06 — Social captions (mechanics only)
**V1 · 2026-09-19 · Governs: the four caption fields of the copy contract in file 05**

## This file holds no voice rules
Same rule as file 04. Caption voice, length, hashtag policy and CTA wording live in `peggy-olson-copywriting/hu_description_prompt_V<n>.md` and `brands/handwriting-university.md`. Not here.

The QDE equivalent of this file became a competing authority — it specified caption counts, a hashtag count, and retired output keys, all contradicting the governing prompt, and had to be pulled out of the system prompt. **This file already made that mistake once** (see the correction below). Do not let it grow rules.

## Mechanics

Four caption fields, produced in the same LLM call as the title and description: `tiktok_caption`, `instagram_caption`, `fb_long`, `fb_short`. Each is written for its own platform. They are carried to file 10, which puts each on its own draft.

⛔ **Never bundle providers into one Metricool post.** Metricool exposes a single shared `text` field per post — only `tiktokData.title` and `facebookData.title` are per-network — so a bundled post forces one caption onto every platform. One call per draft. This is the prompt's own reasoning (V3 §1).

## ⚠️ Correction log, 2026-09-19

**The hashtag count was removed from this file.** V3 sets counts per platform — YouTube 12–18, Instagram 8–12, TikTok 4–6, Facebook REEL none needed. This file previously said "5–12", taken from the brand kit's general guidance, which contradicts the prompt for YouTube. **The prompt wins for copy.** Point at it; never copy the numbers here.

**The off-platform assertion was removed and then restored the same day.** It was briefly deleted on the reasoning that it was a QDE rule wrongly imported, because `hu_description_prompt_V2.md` §5 required the line `Full breakdown on YouTube` in the Instagram caption. Bart then ruled the other way: *"I don't want any copy pushing the user to another platform that is owned by a different company."* V3 deletes that line and states the rule generally. **The assertion below is HU policy in its own right, not an inheritance.**

## Assertions run by `Preflight` (file 11)

Every one is a named flag, never a silent fix.

| Assertion | Flag |
|---|---|
| The four captions are **distinct from each other** — no shared sentences | `CAPTIONS_NOT_DISTINCT` |
| **No destination we do not own.** No "full breakdown on YouTube", no "see the rest on TikTok", no naming another platform as somewhere to go. The only destination is `HandwritingUniversity.com` | `OFF_PLATFORM_DESTINATION` |
| No "link in bio" on any platform, Instagram included | `LINK_IN_BIO` |
| `HandwritingUniversity.com` present, written out, in **every** caption | `CTA_MISSING` |
| No "graphology" / "graphologist" anywhere in body copy | `BANNED_TERM_GRAPHOLOGY` |
| No QDE credential language — court testimony counts, judicial acceptance rate, expert-witness claims | `QDE_CREDENTIAL_IN_HU_COPY` |
| No outcome promise ("win your case" and relatives) | `OUTCOME_PROMISE` |
| No `HandwritingExpertUSA.com`, no `bartbaggett.com`, and **never** `HandwritingExpert.com` | `WRONG_DOMAIN` |
| No banned opener — "In this video…", "Today we'll explore…", "Have you ever wondered…" | `BANNED_OPENER` |
| No hype word — Amazing, Shocking, Incredible, Mind-blowing | `HYPE_WORD` |

⚠️ **`OFF_PLATFORM_DESTINATION` needs a real test, not just a word list.** "Full breakdown on YouTube" is the phrasing that existed; a model will find twenty others. Match on the platform *names* — YouTube, TikTok, Instagram, Facebook, Threads, X, Twitter — appearing as a place to go, rather than on any fixed phrase. A platform name inside a hashtag or in the transcript's own words is not a violation.

⚠️ **`CAPTIONS_NOT_DISTINCT` is the one to watch on the first HU run.** Per-platform captions shipped in the QDE lane on 2026-09-19 and no video in either lane has yet produced four genuinely different ones. The prompt has required it all along; nothing has yet proven the pipeline delivers it.

## Hashtags
Counts and required tags come from **V3 §4–§8**. `#graphology` is permitted **as a hashtag only** — never in body copy. QDE forensic/legal tags are banned on HU content. `#HandwritingUniversity` and `#BartBaggett` close the YouTube and Instagram sets.
