# Joan Pre-Flight Pipeline Checklist — V4

**Owner:** Joan Harris
**Version:** V4 — matches the filename. Highest number is current.
**Last updated:** 2026-09-12
**Status:** AUTHORITATIVE — supersedes v3, which has been deleted
**Purpose:** Self-enforcing gate that runs BEFORE any pipeline or publishing job. Exists because Joan followed a skill's built-in instructions instead of the committed SOPs on 2026-07-06 and produced wrong outputs across all five steps.

> **Versioning:** the version lives in the filename and the highest number wins. A new
> revision becomes `..._V5.md` and this file is deleted at the same time. Never two live.

**Rule:** If any item below is NOT checked, Joan stops and resolves it before touching any tool.

---

## Gate 1 — SOP identification (runs FIRST, before any other action)

- [ ] Name the task domain (video publishing / website edit / Metricool / caption / etc.)
- [ ] **Read the authoritative file on GitHub `main` first.** For video publishing that is
      `joan-supervising-agent/HU_Video_Publishing_Pipeline_V10.md` or
      `QDE_Video_Publishing_Pipeline_V10.md`.
- [ ] Then search the local cache for anything else relevant:

  ```bash
  export SOP_ROOT="$HOME/mnt/joan foundation documents and SOP"
  grep -rl "<domain keyword>" "$SOP_ROOT" --include="*.md"
  ```

- [ ] Read every matching SOP from start to finish — not skimmed, read
- [ ] If no SOP exists: **STOP. Tell the reviewer. Ask for the correct document.**
- [ ] **Authority order: GitHub `main` > local SOP > skills and plugins.** A local file that
      disagrees with `main` is stale, not a fallback. An uncommitted file is a blocked job.
      ⚠️ *Corrected in V4 — v3 said "local SOP wins," which the pipelines overturned.*

## Gate 2 — Asset verification (before writing any copy or touching any platform)

For video publishing jobs specifically:

- [ ] Is there a full, cleaned VTT transcript for each video? (No → generate it first;
      descriptions cannot be written without it)
- [ ] Is there a vertical 9:16 cut? **Confirm with `ffprobe`, never by filename.**
      If only a landscape master exists, it gets built in Phase 5.
- [ ] Is the vertical cut under 3 minutes? Over → STOP and ask the reviewer.
- [ ] Are thumbnails generated — real ones from the locked brand method, not placeholder art?
      *(Thumbnail approval no longer happens here. It happens at the single review, with
      the thumbnail already on the private video.)*

## Gate 3 — Client approval

- [ ] Is client approval recorded for this batch?

> ⚠️ **UNRESOLVED — do not guess.** Two documents name two different sources and neither has
> been confirmed to exist:
> - The HU/QDE pipelines say: Video Production MASTER sheet, find **"Approved By Client"**
>   by header.
> - This checklist previously said: **Zeeshan worksheet, Column O = "Yes."**
> - No "Approved By Client" column has been found on the MASTER sheet's Workflow tab.
>
> **Until the real source is identified, this gate FAILS CLOSED:** hold the video and ask
> the reviewer for an explicit yes. Never proceed on a missing or assumed value. This is the
> gate that stops unapproved video entering the pipeline — it is the last one to take a
> shortcut on.

- [ ] Is the destination channel confirmed? QDE and HU never cross. Check the brand's
      pipeline file for the channel ID, not memory.

## Gate 4 — Platform settings (never assume defaults)

### YouTube upload

- [ ] Method: **direct terminal upload via the `yutu` CLI with a local file path.**
      rclone the render down from Drive first. **Not** YouTube Studio, not a Chrome session.
- [ ] Visibility: **PRIVATE.** Not Unlisted, not Public, not Scheduled. The video stays
      private until the reviewer makes it public — that is the approval.
- [ ] Playlist: confirm the correct playlist for the content type.

### Metricool posts

- [ ] **Agents create DRAFTS.** `draft: true`, no publish time. An agent never schedules a post.
- [ ] **A scheduled post is `autoPublish: true` + `draft: false`.** The reviewer sets that
      when they schedule. ⛔ `autoPublish: false` is banned outright — it is not a hold, it
      is a phone notification that silently dies. It stranded two QDE TikTok posts on
      2026-05-27 and an HU Instagram post on 2026-09-25.
      ⚠️ *Changed in V4 — v3 hard-coded `autoPublish: true` at creation.*
- [ ] One post per network. Never bundle providers.
- [ ] Media: see Phase 8 of the brand's pipeline file. *(Short version: hand Metricool the
      Google Drive URL; the FTP bridge is a fallback for files owner-only to an editor's
      account. Not restated here — one spec, one home.)*
- [ ] The YouTube video is already live from the pipeline, so **do not** create a YouTube
      Metricool post — it would duplicate.

### Captions

- [ ] Source: Google Drive built-in caption generator, not YouTube ASR.
- [ ] Cleaned to **≤5 words per cue**, ≤2 lines, timing preserved.
- [ ] "Baggett" misspelling correction pass applied.
- [ ] Uploaded **after** the thumbnail is set — captions are the last YouTube step.
- [ ] ⛔ Caption upload is **not** `yutu`. It is a separate tool from video upload.

---

## The failure that created this checklist (2026-07-06)

| What I did | What SOP required at the time |
| :--- | :--- |
| Tried to download videos to local disk | Upload from Drive cloud via YouTube Studio |
| Wrote descriptions from title only | Read full cleaned VTT first |
| Built Pillow geometric placeholder thumbnails | Use the locked AI prompt, real versions |
| Planned `draft: true` for Metricool | `autoPublish: true, draft: false` always |
| Skipped vertical cut creation | Run the resize/normalize step for all TikTok/IG files |
| Followed skill built-in instructions | Read the committed SOPs first |

> **Two rows above have since been overturned, and that is worth understanding rather than
> editing away.** The upload method is now the `yutu` CLI from local disk, and Metricool
> posts are now created as drafts on purpose. Both reversals were deliberate decisions with
> reasons recorded in the pipeline files.
>
> **The lesson of 2026-07-06 was never the specific settings — it was acting without
> reading the current SOP.** That lesson is unchanged, and these reversals are the proof of
> it: an agent working from memory of this table would now get two of six wrong.

---

## Referenced SOP files

⚠️ **Most of the paths v3 listed here are not on GitHub `main`.** Under the repo's own rule
an uncommitted file is a blocked job, not an input — so an agent told to "read all of
these" will correctly stop. Before relying on any of them, check `main`:

- `betty/Betty_SOP_YouTube_Publishing_QDE.md` — ⚠️ not on `main`
- `betty/Betty_SOP_Metricool_Syndication_QDE_v1.md` — ⚠️ not on `main`; the local copy is
  dated 2026-05-31 and covers TikTok + Instagram only, with no Facebook
- `betty/Betty_SOP_VideoSmimeo_IG_Resize_Normalize_v1.md` — ⚠️ not on `main`, though the
  pipelines name it as the Phase 5 governing doc
- `betty/Video_Publishing_Workflow_HU_and_QDE_v1.md` — ⚠️ not on `main`
- `betty/Publishing_Kickoff_and_Intake_Form_v1.md` — ⚠️ not on `main`

**On `main` and authoritative:**

- `joan-supervising-agent/HU_Video_Publishing_Pipeline_V10.md`
- `joan-supervising-agent/QDE_Video_Publishing_Pipeline_V10.md`
- `peggy-olson-copywriting/hu_description_prompt_V2.md`
- `peggy-olson-copywriting/qde_legal_description_prompt_V6.md`
- `brands/handwriting-university.md` · `brands/qde-brand.md`

---

## Changelog

| Date | Version | Change |
| :--- | :--- | :--- |
| 2026-07-06 | v2 | Created after confirmed procedure failure across all five pipeline steps. |
| 2026-09-05 | v2.1 | Gate 4 YouTube upload method corrected to `yutu` CLI local-file upload. Gate 1 `find` placeholder replaced with a runnable `grep -rl`. Caption limit tightened from ≤6 to ≤5 words per cue. |
| 2026-09-12 | V4 | Header version corrected — the previous file's header said "v2.1" while its filename said v3. Gate 4 Metricool rewritten to the two-stage draft rule. Gate 4 media line now points at Phase 8 instead of restating it. Gate 3 approval source marked unconfirmed and set to fail closed. Authority corrected to GitHub-beats-local. Referenced SOP list flagged against `main`. Failure table annotated rather than edited. |

*Update this file whenever a new failure adds a lesson. **Bump the number in the filename and in the header together, and delete the file it replaces.** Never leave two live.*
