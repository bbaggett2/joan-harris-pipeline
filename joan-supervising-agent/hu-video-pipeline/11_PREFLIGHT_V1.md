# 11 — Preflight
**V1 · 2026-09-19 · Governs n8n node: `Preflight` (Code)**

## Rule
Preflight **asserts and flags. It never repairs copy.** A silent fix hides the defect that produced it and the same wrong output ships next week.

It runs after the copy package is parsed (file 05) and before anything is uploaded or drafted.

## Brand-lane assertions — the ones that matter most for HU

| Assertion | Flag | Severity |
|---|---|---|
| No "graphology" / "graphologist" in any body copy, title, description or on-screen text | `BANNED_TERM_GRAPHOLOGY` | **hard stop** |
| No QDE credential language — court-testimony counts, judicial-acceptance rate, expert-witness or court-qualified claims | `QDE_CREDENTIAL_IN_HU_COPY` | **hard stop** |
| No outcome promise — "win your case" and relatives | `OUTCOME_PROMISE` | **hard stop** |
| No forensic/legal framing — forgery, will contest, questioned document, signature authentication | `LANE_STRADDLE` | **hard stop** |
| CTA present and points to `HandwritingUniversity.com` | `CTA_MISSING` | flag |
| No `HandwritingExpertUSA.com`, no `bartbaggett.com` | `WRONG_DOMAIN` | flag |
| **Never** `HandwritingExpert.com` — not an owned domain | `UNOWNED_DOMAIN` | **hard stop** |
| No "link in bio", any platform | `LINK_IN_BIO` | flag |
| The four captions are distinct from each other | `CAPTIONS_NOT_DISTINCT` | flag |
| Hashtags 5–12; `#graphology` only as a hashtag | `HASHTAG_COUNT` | flag |

The four hard stops exist because HU and QDE share a host and a subject. Copy that drifts between lanes is the failure this brand kit was written to prevent (`brands/handwriting-university.md` §1.2).

## Structural assertions

| Assertion | Flag |
|---|---|
| Title non-empty, no markdown, no wrapping quotes | `TITLE_MALFORMED` |
| Description matches the shape `yt_format` demands (file 02) | `FORMAT_MISMATCH` |
| No markdown headings or backtick fences in the YouTube description | `MARKDOWN_ARTIFACT` |
| Chapters present for long, absent under ~2 min, and **before** the CTA | `CHAPTER_PLACEMENT` |
| `mode` is one of the enum values, not prose | `MODE_NOT_ENUM` |
| No leaked prompt scaffolding — output labels, "OUTPUT 2:", section markers | `LABEL_STRIPPED` |
| A `caption` key reappeared → something is on the old universal-caption spec | `CAPTION_LEGACY_SHAPE` |

## Two regex traps that have already cost a run

⚠️ **Do not use the `m` flag when extracting sections.** It makes `$` mean end-of-line and truncates every section to its first line — this cut a 1,643-character description to 350.

⚠️ **Stripping markdown headings must not eat hashtags.** `/^#+\s?/gm` ate the first hashtag's `#`. The correct pattern is `/^#{1,6}[ \t]+(?=\S)/gm`.

## Output
`flags: []` on a clean run. Every flag is carried to file 12 and appears in the reviewer's Slack message. A hard stop halts before upload and alerts; it does not proceed with a warning.
