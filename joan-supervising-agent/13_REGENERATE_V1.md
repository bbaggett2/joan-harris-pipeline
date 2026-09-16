# 13 — Regenerate buttons
**V1 · 2026-09-15 · Governs three n8n workflows: `QDE Video — Regenerate thumbnail` · `… — Regenerate description` · `… — Regenerate captions` (build items; pattern proven)**

Same pattern as `Betty — Regenerate image (button)`: a Form Trigger asking only for `vid_id`, reading feedback from a dedicated column, updating in place, ending on a **Show Text** page with the result and an *Open* button.

| Button | Reads column | Re-runs | Writes | Updates |
|---|---|---|---|---|
| Thumbnail | `feedback_thumbnail` | file 07 with feedback layered on the prompt (or, if the feedback is a URL, uses that image directly — the human-composited face path) | `thumbnail_url` (new file, v+1) | YouTube `thumbnails.set` |
| Description | `feedback_description` | file 05 | `description`, `to_verify` | YouTube `videos.update` (private stays private) |
| Captions | `feedback_captions` | file 06 + preflight | four caption fields | the four Metricool drafts via `updateScheduledPost` (re-read ids after — Metricool reissues them) |

Rules carried over: feedback empty → refuse with a message; feedback is phrased as what the output **should be**, never as a "no …"; each run appends `<field> v<n> (<time>): <feedback>` to `notes` and clears the feedback cell; status stays `STAGED` throughout; version 1 is never overwritten in Drive.

Completion page (Show Text, HTML): title, preview (thumbnail) or the new text, one button — *Open new thumbnail* / *Open in YouTube Studio* / *Open Metricool planner* — and the line "To go again, add new feedback to the column and press Regenerate."

## Refinement hook
A button that produces bad output → the step file it re-runs (07/05/06), not this one.
