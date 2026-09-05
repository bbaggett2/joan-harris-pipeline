# Joan Pre-Flight Pipeline Checklist

**Owner:** Joan Harris
**Version:** v2.1
**Last updated:** 2026-09-05
**Purpose:** Self-enforcing gate that runs BEFORE any pipeline or publishing job. Exists because Joan followed a skill's built-in instructions instead of Betty's SOPs on 2026-07-06 and produced wrong outputs across all five steps. This checklist prevents that from happening again.

**Rule:** If any item below is NOT checked, Joan stops and resolves it before touching any tool.

---

## Gate 1 — SOP identification (runs FIRST, before any other action)

- [ ] List the task domain (video publishing / website edit / Metricool / caption / etc.)
- [ ] Find all relevant SOP files:

  ```bash
  grep -rl "<domain keyword>" "$SOP_ROOT" --include="*.md"
  ```

  where `SOP_ROOT` is the connected "joan foundation documents and SOP" folder. In a Cowork device session that is:

  ```bash
  export SOP_ROOT="$HOME/mnt/joan foundation documents and SOP"
  ```

- [ ] Read every matching SOP from start to finish — not skimmed, read
- [ ] If no SOP exists: **STOP. Tell Bart. Ask for the correct document or instruction.**
- [ ] If a loaded skill conflicts with the SOP: **local SOP wins. Flag conflict to Bart.**

## Gate 2 — Asset verification (before writing any copy or touching any platform)

For video publishing jobs specifically:

- [ ] Is there a full, cleaned VTT transcript for each video? (If no → generate from Google Drive built-in caption generator first; descriptions cannot be written without it)
- [ ] Is the YouTube video already uploaded? (Metricool step requires a live YouTube video ID — do not create Metricool posts before YouTube upload)
- [ ] Is there a vertical 9:16 cut for each video? (TikTok/IG require this — if only horizontal exists, run Video-Smimeo rclone+ffmpeg on Mac first)
- [ ] Is there a Bart-approved thumbnail (3 versions generated via locked AI prompt, not placeholder art)?

## Gate 3 — Approval gate check

- [ ] Is Bart's approval recorded for this batch? (Zeeshan worksheet Column O = "Yes", or explicit Bart message)
- [ ] Is the destination channel confirmed? (QDE = `@TheHandwritingExpert` only; never cross-brand)
- [ ] Has Bart or Joan approved title + description + thumbnail before they go live or public?

## Gate 4 — Platform-specific settings (never assume defaults)

### YouTube upload

- [ ] Upload method: **local file upload from the terminal using the `yutu` CLI with a local file path.** The video file must already be on local disk (sync it from Drive with rclone first if needed). Do not upload through the YouTube Studio web UI.
- [ ] Visibility: **PRIVATE** (not Unlisted, not Public, not Scheduled — those come after human review)
- [ ] Playlist: confirm correct playlist for content type

### Metricool posts

- [ ] `autoPublish: true` — hard-coded, no exceptions
- [ ] `draft: false` — hard-coded, no exceptions
- [ ] `providers` and `<network>Data` blocks must match exactly
- [ ] Media URL is the Drive `viewUrl` of the **vertical 9:16 cut**, not the horizontal master
- [ ] YouTube video ID is live before creating Metricool posts

### Captions

- [ ] Source: Google Drive built-in caption generator (not YouTube ASR as primary)
- [ ] Cleaned to **≤5 words per cue**, ≤2 lines, timing preserved (matches the `caption-shortener` skill; word-level timestamps required)
- [ ] "Baggett" misspelling correction pass applied
- [ ] Uploaded as English track via `caption-insert` after thumbnail is set (captions are the LAST step)

---

## The failure that created this checklist (2026-07-06)

| What I did | What SOP required at the time |
|---|---|
| Tried to download videos to local disk | Upload from Drive cloud via YouTube Studio |
| Wrote descriptions from title only | Read full cleaned VTT first |
| Built Pillow geometric placeholder thumbnails | Use locked AI prompt via Grok/NotebookLM, 3 versions |
| Planned `draft: true` for Metricool | `autoPublish: true, draft: false` always |
| Skipped vertical cut creation | Run Video-Smimeo (rclone+ffmpeg) for all TikTok/IG files |
| Followed skill built-in instructions | Read Betty SOPs first; local always wins |

> **Superseded (2026-09-05):** Row 1 above reflects the July 2026 standard. The YouTube upload method has since changed to a local file upload via the `yutu` CLI (see Gate 4). The lesson from that row still stands — the failure was acting without reading the SOP, not the upload path itself.

---

## Relevant SOP files — read ALL of these for any QDE video job

- `betty/Betty_SOP_YouTube_Publishing_QDE.md`
- `betty/Betty_SOP_Metricool_Syndication_QDE_v1.md`
- `betty/Betty_SOP_VideoSmimeo_IG_Resize_Normalize_v1.md`
- `betty/Video_Publishing_Workflow_HU_and_QDE_v1.md`
- `betty/Publishing_Kickoff_and_Intake_Form_v1.md`
- `Ai Prompt Documents/qde_legal_description_prompt.md`

---

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-07-06 | v2 | Created after confirmed procedure failure across all five pipeline steps. |
| 2026-09-05 | v2.1 | Gate 4 YouTube upload method corrected to `yutu` CLI local-file upload; resolved contradiction with the failure table. Gate 1 `find` placeholder replaced with a runnable `grep -rl` using `$SOP_ROOT`. Caption limit tightened from ≤6 to ≤5 words per cue to match the `caption-shortener` skill. Added version header and this changelog. |

*Update this file whenever a new failure adds a lesson. Bump the version and add a changelog row.*
