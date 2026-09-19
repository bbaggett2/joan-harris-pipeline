# 05 — Copy contract
**V1 · 2026-09-19 · Governs n8n nodes: `Fetch description prompt` · `Copy: title+description+captions` (LLM) · `Parse copy`**

## Authority
**`peggy-olson-copywriting/hu_description_prompt_V<n>.md` on `main` — highest `n`, fetched at run time. Nothing else.** Not a local `Ai Prompt Documents/` copy, not an installed skill, not a previous video's package. If it is not on `main`, the job is blocked.

⛔ **This file holds the JSON contract and nothing about voice.** See file 04.

⚠️ **The file on `main` is `hu_description_prompt_V2.md` and it predates this contract.** It has no five-output shape, no `mode` enum, and none of the 2026-09-19 rulings. **The HU lane is blocked until `V3` lands.** Writing `V3` is Peggy's job; Bart commits it.

## The contract — five copy outputs, four Metricool drafts

YouTube is not a Metricool draft (the video is already on the channel from file 09), which is why five outputs produce four drafts. V15 said "five drafts" in two places and "four" in its own table; four is correct.

| Key | Shape |
|---|---|
| `title` | file 04 |
| `description` | **one of two shapes, chosen by `yt_format` from file 02.** `long` → long-form YouTube body + chapters. `short` → Shorts description, short, 3–5 hashtags, **no chapters** |
| `tiktok_caption` | its own words |
| `instagram_caption` | its own words |
| `fb_long` | Facebook POST, its own words |
| `fb_short` | Facebook REEL, its own words |
| `mode` | hard **enum**, not prose. A prose field here returned a sentence instead of a value |

⛔ **Per platform, always. Never one caption fanned out to four.** Bart reversed the universal-caption design on 2026-09-19. The QDE lane's file 10 still describes "one caption, four drafts" — that is stale; do not carry it into HU.

⛔ **Chapters go BEFORE the CTA**, not appended after it. Skip chapters entirely under ~2 minutes.

⛔ **No markdown headings or backtick fences in the YouTube description body.** YouTube renders them literally.

## Parsing

`Parse copy` reads the model's JSON and writes each field onto the payload.

- A `caption` key reappearing means something is still on the old universal-caption spec → raise `CAPTION_LEGACY_SHAPE`.
- An empty caption set → `CAPTION_MISSING`.
- ⚠️ When extracting sections by regex, **do not use the `m` flag** — it makes `$` mean end-of-line and truncates every section to its first line. That bug cut a 1,643-character description to 350.

## Output file
`<VID_ID>_copy_package.md` in the assets folder. It carries the **resolved brand as a field**; nothing downstream re-infers it.

## Flags
`COPY_PROMPT_MISSING` (hard stop) · `CAPTION_LEGACY_SHAPE` · `CAPTION_MISSING` · `FORMAT_DEFAULTED_LONG`
