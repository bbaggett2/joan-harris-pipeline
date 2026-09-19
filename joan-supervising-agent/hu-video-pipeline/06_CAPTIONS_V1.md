# 06 — Social captions (mechanics only)
**V1 · 2026-09-19 · Governs: the four caption fields of the copy contract in file 05**

## This file holds no voice rules
Same rule as file 04. Caption voice, length, hashtag policy and CTA wording live in `peggy-olson-copywriting/hu_description_prompt_V<n>.md` and `brands/handwriting-university.md`. Not here.

The QDE equivalent of this file became a competing authority — it specified four per-platform captions, a hashtag count, and retired output keys, all contradicting the governing prompt, and had to be pulled out of the system prompt. Do not let this file grow rules.

## Mechanics

Four caption fields, produced in the same LLM call as the title and description: `tiktok_caption`, `instagram_caption`, `fb_long`, `fb_short`. Each is written for its own platform. They are carried to file 10, which puts each on its own draft.

⛔ **Never bundle providers into one Metricool post.** Metricool exposes a single shared `text` field per post — only `tiktokData.title` and `facebookData.title` are per-network — so a bundled post forces one caption onto every platform. One call per draft.

## Assertions run by `Preflight` (file 11)

Every one is a named flag, never a silent fix.

| Assertion | Flag |
|---|---|
| The four captions are **distinct from each other** — no shared sentences | `CAPTIONS_NOT_DISTINCT` |
| No "graphology" / "graphologist" anywhere in body copy | `BANNED_TERM_GRAPHOLOGY` |
| No QDE credential language — court testimony counts, judicial acceptance rate, expert-witness claims | `QDE_CREDENTIAL_IN_HU_COPY` |
| No outcome promise ("win your case" and relatives) | `OUTCOME_PROMISE` |
| `HandwritingUniversity.com` present, written out, with a CTA | `CTA_MISSING` |
| No `HandwritingExpertUSA.com`, no `bartbaggett.com`, and **never** `HandwritingExpert.com` | `WRONG_DOMAIN` |
| No "link in bio" on any platform, Instagram included | `LINK_IN_BIO` |
| No cross-platform pointer ("full breakdown on YouTube") | `CROSS_PLATFORM_POINTER` |

⚠️ **`CAPTIONS_NOT_DISTINCT` is the one to watch on the first HU run.** Per-platform captions shipped on 2026-09-19 and no video in either lane has yet produced four genuinely different ones.

## Hashtags
5–12 tags, HU core set from `brands/handwriting-university.md` §10. `#graphology` is permitted **as a hashtag only** — never in body copy. QDE forensic/legal tags are banned on HU content.
