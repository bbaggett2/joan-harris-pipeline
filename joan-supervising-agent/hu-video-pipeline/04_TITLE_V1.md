# 04 — Title (mechanics only)
**V1 · 2026-09-19 · Governs: the title field of the copy contract in file 05**

## This file holds no voice rules
**Bart's rule, 2026-09-19: Peggy's folder (`peggy-olson-copywriting/`) owns WHAT gets written; Joan's folder owns HOW the pipeline carries it.** Title strategy, length, phrasing and banned words live in `peggy-olson-copywriting/hu_description_prompt_V<n>.md` and `brands/handwriting-university.md` §2. They are not restated here and must not be.

This exists because `04_TITLE_V1.md` in the QDE lane became a competing authority — it contradicted the governing prompt on title length and on strategy, and had to be pulled out of the system prompt. Do not let this file grow rules.

## Mechanics

- The title is produced in the **same LLM call** as the description and captions (file 05), not a separate one. One call, one JSON object, one contract.
- It is carried on the payload to file 09, which sets it on the YouTube video verbatim.
- **No gate here.** The title reaches the reviewer sitting in the YouTube title field, where changing it takes seconds.

## Assertions run by `Preflight` (file 11)
- non-empty
- no markdown artifacts, no surrounding quotes
- no banned term from `brands/handwriting-university.md` §2.3 — in particular **"graphology" / "graphologist"**, which are banned in titles outright and permitted only as a hashtag
- no QDE credential language, no outcome promise

A failed assertion is a named flag, never a silent rewrite. The pipeline does not repair copy.
