# 11 — Preflight (repair or flag, never block)
**V1 · 2026-09-15 · Governs n8n node: `Preflight` (Code) — runs after files 04–06, before 07/09**

The Gate 7 checklist as code. Every check either **repairs** the text or **flags** it. Flags go to `notes` and the Slack notice — never into any caption.

| Check | Action |
|---|---|
| `HandwritingExpert.com` (no USA) in any field | **Repair** → `HandwritingExpertUSA.com`; flag `DOMAIN_REPAIRED` |
| Phone or either owned domain missing from a caption | **Repair** → append the CTA block; flag `CTA_APPENDED` |
| "link in bio", "full breakdown on YouTube", any cross-platform pointer | **Repair** → delete sentence; flag `POINTER_REMOVED` |
| Markdown `#`, ``` in description | **Repair** → strip; flag `MARKDOWN_STRIPPED` |
| Third person "Bart Baggett examined" | **Flag** `THIRD_PERSON` (never rewrite Peggy's meaning) |
| "graphology"/"graphologist" outside a hashtag | **Flag** `BANNED_TERM` |
| "win your case", "guarantee", "will prove" | **Flag** `OUTCOME_LANGUAGE` |
| Any `$` amount or the words price/fee/retainer | **Flag** `PRICING` (nothing publishes with pricing) |
| `to_verify` non-empty | **Flag** `TO_VERIFY:n` — first line of the reviewer notice |
| Personality / HU framing keywords ("personality", "what your handwriting says") | **Flag** `HU_FRAMING` — the one flag the reviewer must treat as a stop |
| Caption empty | **Halt this row** → `ERROR`, `notes` `EMPTY_CAPTION`, Slack, next row |

Output: repaired fields + `flags[]` + `preflight_ok` (false only for empty caption). Mojibake (`‚Äî` etc.) is normalised on the way through. The code lives inline in the `Preflight` node of the workflow JSON (a fork of `betty-social-media-manager/preflight_checks_v4.js`, four caption fields instead of one).

## Refinement hook
A check that fires wrongly → edit the regex. A check that should block instead of flag → move it to the halt row, deliberately.
