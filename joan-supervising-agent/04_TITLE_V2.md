# 04 — Title
**V2 · 2026-09-19 · Governs n8n node: `Copy: title+description+captions` (title section)**

Authority for title text is **`peggy-olson-copywriting/qde_legal_description_prompt_V<n>.md`, highest n on main** — the same file that governs the description and the universal caption. n8n fetches it from raw GitHub at run time and passes it inside the system prompt; the cleaned VTT (file 03) is user content. This file holds the wiring only.

Input: cleaned VTT (file 03) + `brands/qde-brand.md` (fetched). Output: `title` and `mode` on the row.

## What changed in V2

V1 carried its own TITLE RULES block, fetched verbatim into the system prompt alongside the Peggy file. The two disagreed — V1 said titles under 10 words, V7 says under 8 — and the model was handed both at once. Whichever it followed, a rule lost.

The rules block is gone. `Fetch title rules` no longer feeds the system prompt; the node remains in the graph feeding nothing, so the change reverts in one edit. **Peggy's folder owns what gets written; this folder owns how the pipeline carries it.** File 05 has always worked this way — V2 brings this file into line with it.

## n8n behaviour

- **No title is ever supplied upstream.** The transcript is the only source, and V7 requires the title be written *first*, before any description copy, because that is what forces the model to find what the video is actually about.
- `title` → row → the YouTube title field, and the `## Title` section of the copy package (file 05).
- `mode` (`attorney` | `consumer`) → row. Detected from the transcript. It is not cosmetic: it selects which CTA block the description carries.
- Both keys arrive in the single JSON object returned by `Copy: title+description+captions`. There is no separate title call.
- Length, register, question patterns and the banned-word list all live in V7. Preflight (file 11) performs no title checks.

## No human gate

The reviewer sees the title in the YouTube title field on the private upload. Nothing blocks on it.

## Held for merge into V7 — do not drop

V1 carried one instruction sharper than anything currently in V7's title section. It is recorded here so it survives this file ceasing to be an authority. **Fold it into V7's "THE TITLE" section, then delete this block:**

> Lead with the crime, the document or the famous name — the thing a stranger recognises — not the forensic method.
>
> Never make a famous person the author of a crime they were the victim of.

Headline register is the output Bart edits most (2026-09-14: name-first, plain crime word, question allowed, stake or date). That makes it the thing most worth getting right in V7 rather than losing here.

## Refinement hook

Title quality, length, register, banned words → **edit the Peggy prompt file**, not this one.

JSON shape, which node emits the title, or how `mode` is routed → this file and the `Parse copy` node.
