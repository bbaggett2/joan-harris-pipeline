# 05 — Description
**V1 · 2026-09-15 · Governs n8n node: `Copy: title+description+captions` (description section)**

Authority for the description text is unchanged: **`peggy-olson-copywriting/qde_legal_description_prompt_V<n>.md`, highest n on main.** n8n fetches it from raw GitHub at run time and passes it inside the system prompt; the cleaned VTT is user content.

The model returns JSON only; the description-related keys are:
```json
{"mode":"attorney|consumer","description":"...","chapters":[{"t":"00:00","label":"..."}],"to_verify":["..."]}
```

## n8n behaviour
- `description` → row. No markdown headings, no backtick fences (the prompt says so; preflight strips any that leak — file 11).
- `to_verify[]` → row `to_verify`, joined with ` | `. Every item becomes the first line of the reviewer's Slack notice. **Any item present blocks publication (Gate 7) but never blocks staging.**
- Chapters are appended to the description as `mm:ss Label` lines only if every `t` appears verbatim in the VTT; a chapter whose timestamp is not in the VTT is dropped and `notes` gets `CHAPTER_TS_NOT_IN_VTT`. Timestamps are read, never estimated.

## Refinement hook
Description quality → edit the Peggy prompt file. JSON shape or chapter handling → edit this file and the `Parse copy` node.
