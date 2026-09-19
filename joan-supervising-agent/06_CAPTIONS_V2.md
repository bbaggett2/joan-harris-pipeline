# 06 — Caption (one universal, all short-form platforms)
**V2 · 2026-09-19 · Governs n8n node: `Copy: title+description+captions` (caption section) and the fan-out in `Parse copy`**

Authority for caption text is **`peggy-olson-copywriting/qde_legal_description_prompt_V<n>.md`, highest n on main** — the same file that governs the title and the description. n8n fetches it from raw GitHub at run time and passes it inside the system prompt; the cleaned VTT (file 03) is user content. This file holds the wiring only.

## What changed in V2

V1 specified **four** captions — `tiktok`, `instagram`, `fb_long`, `fb_short` — with per-platform lengths and exactly five hashtags, and carried those rules verbatim into the system prompt. V7 Output 3 requires the opposite:

> One caption, posted identically to TikTok, Instagram, Facebook, and Threads. […] There is no reason to write four variants of the same caption, and doing so introduces drift.

V1 also named output keys that no longer exist in the schema. The rules block is gone, `Fetch caption rules` no longer feeds the system prompt (the node remains in the graph feeding nothing, so it reverts in one edit), and the model is now asked for **one** caption.

**Peggy's folder owns what gets written; this folder owns how the pipeline carries it.** File 05 has always worked this way.

## n8n behaviour

The model returns the caption in a single key:

```json
{"caption": "...", "tiktok_hook": "..."}
```

- `caption` — V7 Output 3. 75–150 words, 3–5 hashtags, hard ceiling 1,000 characters including hashtags. Written **once**. The system prompt says explicitly: *do NOT produce per-platform caption variants.*
- `tiktok_hook` — the on-screen text overlay for the first three seconds. Separate from the caption; it is not a caption variant.

`Parse copy` then **fans the single caption out** to the four per-platform fields the copy package and the Metricool drafts still expect:

```js
const _cap = c.caption || c.tiktok || c.instagram || c.fb_long || '';
c.tiktok = _cap; c.instagram = _cap; c.fb_long = _cap; c.fb_short = _cap;
```

The fallback chain is deliberate: if an older prompt version is ever restored and returns the legacy per-platform keys, the pipeline still works and raises `CAPTION_LEGACY_SHAPE` so the drift is visible instead of silent. An empty caption raises `CAPTION_MISSING`.

| Flag | Meaning |
|---|---|
| `CAPTION_LEGACY_SHAPE` | Model returned per-platform keys instead of `caption` — prompt version drift |
| `CAPTION_MISSING` | No caption in any key. Preflight halts the row (`EMPTY_CAPTION`) |

## Storage shape, not a writing instruction

The copy package still carries four sections — `## TikTok caption`, `## Instagram caption`, `## Facebook (long cut)`, `## Facebook (vertical / reel)` — and after the fan-out they hold identical text. That is storage redundancy in a file, not four separate acts of writing, so it does not re-introduce the drift V7 is guarding against. Collapsing the package to a single `## Universal caption` section is a separate change touching `Build copy package` and both parsers; it has not been made.

## Preflight

File 11 applies the CTA repair to each of the four fields after the fan-out, so all four stay identical. Length caps live in V7, not in Preflight.

## Refinement hook

Caption voice, length, hashtag count, CTA wording → **edit the Peggy prompt file**, not this one.

The fan-out, the flags, or which networks receive which field → this file, the `Parse copy` node, and file 10.
