# 11 — Preflight (repair or flag, never block)
**V2 · 2026-09-19 · Governs n8n node: `Preflight` (Code) — runs after files 04–06, before 07/09**

The Gate 7 checklist as code. Every check either **repairs** the text or **flags** it. Flags go to `notes` and the Slack notice — never into any caption.

## What changed in V2

**1. The markdown strip was eating hashtags.** V1's rule was `/^#+\s?/gm`. Under `/m`, `^` matches the start of *every line*, and `\s?` makes the space optional — so the pattern also matched the leading `#` of the first hashtag on the tag line. Every description shipped as `ForgeryDetection #HandwritingExpert …` with the first tag de-hashed, and `MARKDOWN_STRIPPED` was raised on runs where no markdown existed.

The rule is now `/^#{1,6}[ \t]+(?=\S)/gm` — CommonMark requires whitespace after the `#`, so a heading still strips and a hashtag never does. Verified against a real payload: the old pattern fired 4 times and lost 2 hashtags; the new one fires only on the 2 genuine headings and keeps all 6 tags.

**2. One caption, four fields.** V1 described "four caption fields instead of one." That is now inverted: the model writes **one** caption (file 06) and `Parse copy` fans it out to the four per-platform fields before Preflight runs. Preflight still caps each of the four, so they stay identical.

**3. `to_verify` no longer implies a publication block.** See below.

## The checks

| Check | Action |
|---|---|
| `HandwritingExpert.com` (no USA) in any field | **Repair** → `HandwritingExpertUSA.com`; flag `DOMAIN_REPAIRED` |
| Phone or either owned domain missing from a caption | **Repair** → append the CTA block; flag `CTA_APPENDED` |
| "link in bio", "full breakdown on YouTube", any cross-platform pointer | **Repair** → delete sentence; flag `POINTER_REMOVED` |
| Markdown **heading** (`#`–`######` followed by whitespace) or ``` fence in description | **Repair** → strip; flag `MARKDOWN_STRIPPED`. Hashtags are never touched |
| Third person "Bart Baggett examined" | **Flag** `THIRD_PERSON` (never rewrite Peggy's meaning) |
| "graphology"/"graphologist" outside a hashtag | **Flag** `BANNED_TERM` |
| "win your case", "guarantee", "will prove" | **Flag** `OUTCOME_LANGUAGE` |
| Any `$` amount or the words price/fee/retainer | **Flag** `PRICING` (nothing publishes with pricing) |
| `to_verify` non-empty | **Flag** `TO_VERIFY:n` — informational only, see below |
| Personality / HU framing keywords ("personality", "what your handwriting says") | **Flag** `HU_FRAMING` — the one flag the reviewer must treat as a stop |
| Caption empty | **Halt this row** → `ERROR`, `notes` `EMPTY_CAPTION`, Slack, next row |

Output: repaired fields + `flags[]` + `preflight_ok` (false only for empty caption). Mojibake (`‚Äî`, `‚Äô`, `‚Äú`, `¬∑`) is normalised on the way through.

## `TO_VERIFY` is a note, not a gate

**Bart, 2026-09-19: when the content comes from a video Bart was in, the claims are taken as valid. There is no reason to question the source or delete content on that basis.**

So `TO_VERIFY:n` records what the copy spec flagged and nothing more. It does not hold a row, does not block publication, and nothing downstream should be built to make it do so.

⚠️ **Unreconciled:** `05_DESCRIPTION_V1.md` still states *"Any item present blocks publication (Gate 7) but never blocks staging."* That contradicts the rule above. File 05 needs a V2 deciding which stands — this file assumes the 2026-09-19 rule.

## Where the code lives

Inline in the `Preflight` node of the workflow JSON. Originally forked from `betty-social-media-manager/preflight_checks_v4.js`; the fork has diverged and the n8n node is authoritative.

## Refinement hook

A check that fires wrongly → edit the regex, and test it against a real payload before trusting it. A check that should block instead of flag → move it to the halt row, deliberately.
