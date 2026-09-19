# 05 — Copy contract
**V1 · 2026-09-19 · Governs n8n nodes: `Fetch description prompt` · `Copy: title+description+captions` (LLM) · `Parse copy`**

## Authority
**`peggy-olson-copywriting/hu_description_prompt_V<n>.md` on `main` — highest `n`, fetched at run time. Nothing else.** Not a local `Ai Prompt Documents/` copy, not an installed skill, not a previous video's package. If it is not on `main`, the job is blocked.

**Current: `hu_description_prompt_V3.md`.** V2 is a pointer stub.

⛔ **This file holds the JSON contract and nothing about voice.** See file 04. The prompt owns *what* gets written; this file owns *how* the pipeline carries it. That division is Bart's rule, 2026-09-19.

> ### ⚠️ Correction, 2026-09-19
>
> The first version of this file said the HU prompt "predates the five-output contract", had "no per-platform captions", and lacked "chapters-before-CTA", and concluded **the lane was blocked until a rewrite landed**. All three claims were wrong, and the conclusion with them.
>
> V2 §1 already read: *"Five outputs, every time, in one pass. Not four. Not 'and reuse that one for Facebook'"* — with the Metricool shared-`text` reasoning spelled out. §4 already required chapters *"before the CTA, never after it."* It also already banned graphology in body copy, banned "link in bio", banned markdown in the YouTube description, required exact VTT timestamps, and hard-stopped without a cleaned VTT.
>
> **The prompt was in good shape and needed one deletion, not a rewrite.** V3 exists because Bart banned off-platform destinations, not because V2 was behind. Read the file before characterising it.

## The contract — five copy outputs, four Metricool drafts

YouTube is not a Metricool draft (the video is already on the channel from file 09), which is why five outputs produce four drafts.

| Key | Prompt section | Shape |
|---|---|---|
| `title` | file 04 | |
| `description` | V3 §4 | Hook → Body → Chapters → CTA → Hashtags. Chapters **before** the CTA, first entry `0:00`, timestamps read off the VTT and never estimated |
| `instagram_caption` | V3 §5 | 80–150 words, hook opener that survives the "…more" truncation |
| `tiktok_caption` | V3 §6 | lead line under 150 characters |
| `fb_short` | V3 §7 | Facebook REEL — tight, Reels truncate hard |
| `fb_long` | V3 §8 | Facebook POST — narrative length, not the short one pasted |

⛔ **Per platform, always. Never one caption fanned out to four.** The prompt has required this all along; the QDE lane's file 10 still describes "one caption, four drafts", which is stale and must not be carried into HU.

⛔ **No markdown headings or backtick fences in the YouTube description body.** YouTube renders them literally.

### `mode` is not part of the HU contract

Removed 2026-09-19. It was copied from the QDE spec, where it selects attorney-facing versus consumer-facing framing. **HU has one audience** — curious adults 25–55, per V3 §3. A `mode` field here would have forced the model to invent a value with nothing to key it to.

### The one real gap

**There is no Shorts variant of the YouTube description.** V3 §4 defines a single long-form shape — 4–6 paragraphs, chapters, 12–18 hashtags. `Media facts` (file 02) computes `yt_format`, and a vertical HU clip under three minutes will get the long-form treatment, which is exactly the defect the QDE lane spent a day fixing.

Until the prompt gains a Shorts branch: pass `yt_format` into the system prompt anyway, and when it is `short`, instruct the model to skip chapters (V3 already says to skip them under ~2 minutes) and keep the description brief. **Flag `FORMAT_DEFAULTED_LONG` when this path is taken**, so it is visible rather than silent. The durable fix is a §4b in the prompt — Peggy's file, Bart's commit.

## Parsing

`Parse copy` reads the model's JSON and writes each field onto the payload.

- A `caption` key reappearing means something is on an old universal-caption spec → raise `CAPTION_LEGACY_SHAPE`.
- An empty caption set → `CAPTION_MISSING`.
- ⚠️ When extracting sections by regex, **do not use the `m` flag** — it makes `$` mean end-of-line and truncates every section to its first line. That bug cut a 1,643-character description to 350.

## Output file
`<VID_ID>_copy_package.md` in the assets folder, also saved to `particles/` as `<VID_ID>_Description_Package_v1.md` per V3 §1. It carries the **resolved brand as a field**; nothing downstream re-infers it.

## Flags
`COPY_PROMPT_MISSING` (hard stop) · `CAPTION_LEGACY_SHAPE` · `CAPTION_MISSING` · `FORMAT_DEFAULTED_LONG`
