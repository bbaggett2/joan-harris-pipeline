# HU VIDEO PUBLISHING PIPELINE — V15 (SUPERSEDED)

**Superseded 2026-09-19 by the step files in `joan-supervising-agent/hu-video-pipeline/` — start at `00_OVERVIEW_V1.md`.**

The single-document pipeline is retired in favour of one file per step, so each step can be refined independently. This mirrors what the QDE lane did on 2026-09-15.

**Why it was rewritten rather than bumped.** V15 described the HU lane as an agent-to-agent process and said so itself: *"This document does not include the n8n workflow. This process will be rewritten asap."* The lane now runs on n8n Cloud with a Mac side-car worker, and Metricool works a specific, proven way. The step files are the HU lane rewritten on that reality.

**Rules that survive unchanged** are restated in the step files that own them: the Ready-to-Publish folder is the approval *and* the brand signal; brand is resolved once and carried, never re-inferred; `draft: true` always; ship full length; nothing publishes without the reviewer; GitHub is authority.

**What changed from V15, and why** — each is argued in the step file named:

- **Four Metricool drafts, not five.** V15 said "five" in two places and "four" in its own table. Peggy produces five *copy outputs*; YouTube is not a Metricool draft. See `05` and `10`.
- **Short-form drafts take the vertical cut.** File `08` is live for HU and registers `vertical_url` — the wiring the QDE lane never had, which silently skipped three of its four drafts. See `08` and `10`.
- **Publish time is 06:00 America/Chicago**, per Bart's standing rule. See `10`.
- **No sheet writes at all**, per QDE `00_OVERVIEW_V6`. See `00` and `12`.
- **Thumbnails build on the Mac.** Gemini is unreachable from n8n Cloud. See `07`.

⚠️ **Two Phase 4 bans in this document are unresolved against the brand kit** and are carried forward as an open flag in `07`, not silently dropped: `BANNED: PIL hand-composite` contradicts `brands/handwriting-university.md` §7, which mandates a deterministic Python build; `BANNED: red` contradicts §3 and §6, where Teacher Red is required on the 16:9 and excluded only from the 9:16. **Bart's ruling needed.**

This file is kept as history only; nothing reads it.
