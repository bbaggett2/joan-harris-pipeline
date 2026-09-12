# Joan Pre-Flight Pipeline Checklist — V6

**Owner:** Joan Harris
**Version:** V6 — matches the filename. Highest number is current.
**Last updated:** 2026-09-12
**Status:** AUTHORITATIVE — supersedes V5
**Purpose:** Self-enforcing gate that runs BEFORE any pipeline or publishing job. Exists because Joan followed a skill's built-in instructions instead of the committed SOPs on 2026-07-06 and produced wrong outputs across all five steps.

> **Versioning:** the version lives in the filename and the highest number wins. A new
> revision becomes `..._V7.md` and this file is deleted in the same commit. Never two live.
>
> **Cross-references never name an exact version.** A file referred to below as
> `Something_V<n>.md` means *the highest-numbered `Something_V*.md` in that folder* — it
> might be V5, V6 or V8. Always take the highest. This is why a bump in one file never makes
> another file wrong.

**Rule:** If any item below is NOT checked, Joan stops and resolves it before touching any tool.

---

## WHAT CHANGED IN V6

1. **Gate 3 — client approval — is deleted.** It failed closed on every video, waiting on a
   spreadsheet column nobody could find. **The Ready-to-Publish folder is the approval.**
   The destination-channel check that sat under it survives and moves into Gate 2 — that is
   a correctness check, not an approval.
2. **The "under 3 minutes" line is deleted from Gate 2.** Standing rule: **ship full length,
   always.** Duration is still recorded, because Facebook splits REEL vs POST at 90 seconds.
   Nothing else depends on it.
3. **Instagram's 90-second ceiling is gone.** A long vertical cut now goes to Instagram.

Gates renumbered: 1 SOP identification, 2 asset verification, 3 platform settings.

⚠️ **Facebook's 90-second REEL-vs-POST rule is unchanged.** Separate constraint, separate
platform. Do not conflate them.

---

## Gate 1 — SOP identification (runs FIRST, before any other action)

- [ ] Name the task domain (video publishing / website edit / Metricool / caption / etc.)
- [ ] **Read the authoritative file on GitHub `main` first.** For video publishing that is
      `joan-supervising-agent/HU_Video_Publishing_Pipeline_V<n>.md` or
      `QDE_Video_Publishing_Pipeline_V<n>.md` — highest `n` in the folder.
- [ ] Then search the local cache for anything else relevant:

  ```bash
  export SOP_ROOT="$HOME/mnt/joan foundation documents and SOP"
  grep -rl "<domain keyword>" "$SOP_ROOT" --include="*.md"
  ```

- [ ] Read every matching SOP from start to finish — not skimmed, read
- [ ] If no SOP exists: **STOP. Tell the reviewer. Ask for the correct document.**
- [ ] **Authority order: GitHub `main` > local SOP > skills and plugins.** A local file that
      disagrees with `main` is stale, not a fallback. An uncommitted file is a blocked job.
      ⚠️ *Corrected in V4 — the older text said "local SOP wins," which the pipelines overturned.*

## Gate 2 — Asset verification (before writing any copy or touching any platform)

For video publishing jobs specifically:

- [ ] Is there a full, cleaned VTT transcript for each video? (No → generate it first;
      descriptions cannot be written without it)
- [ ] Is there a vertical 9:16 cut? **Confirm with `ffprobe`, never by filename.**
      If only a landscape master exists, it gets built in Phase 5.
- [ ] Record the duration from `ffprobe`. **It does not gate anything — ship full length,
      always.** It is recorded because Facebook still splits REEL vs POST at 90 seconds in
      Phase 8. *(V5 and earlier stopped here on anything over 3 minutes and asked the
      reviewer to choose trim or full length. That gate is deleted — Bart's standing rule,
      2026-09-12.)*
- [ ] Are thumbnails generated — real ones from the locked brand method, not placeholder art?
      *(Thumbnail approval no longer happens here. It happens at the single review, with
      the thumbnail already on the private video.)*
- [ ] Is the destination channel confirmed? QDE and HU never cross. Check the brand's
      pipeline file for the channel ID, not memory. *(Moved here from the deleted Gate 3.
      It is a correctness check, not an approval.)*

## Gate 3 — Platform settings (never assume defaults)

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
- [ ] One post per network. Never bundle providers.
- [ ] **Instagram takes video of any length.** *(Changed 2026-09-12 — the old 90-second cap
      is gone.)* Aspect ratio still applies: Instagram rejects horizontal video outright.
- [ ] **Facebook still splits on 90 seconds** — vertical and under 90s can be a REEL,
      otherwise POST. Decided by `ffprobe`, never by guess.
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

## What this checklist does NOT gate

Read this before adding a gate back. Each of these was removed deliberately, and the
reasoning is recorded so nobody restores one thinking it was lost by accident.

| Not gated | Why |
| :--- | :--- |
| **Client approval** | The Ready-to-Publish folder is the approval. A video is in it because a person put it there. The old gate read the MASTER sheet for an "Approved By Client" column that was never found, so it failed closed on every video. |
| **Duration / trimming** | Ship full length, always. Duration is recorded for Facebook's REEL/POST split and nothing else. |
| **Title, description, caption copy** | No human reads it until it is staged. That is why Peggy's marking discipline is absolute and why every `[TO VERIFY]` is a blocker at Phase 9. |
| **Thumbnail choice** | Reviewed on the private video. A rejected thumbnail re-runs Phase 4 and swaps on the live video — a redo, not a failure. |

**There are exactly two human touchpoints in the whole pipeline:** someone puts the video in
the Ready-to-Publish folder, and the reviewer makes the video public and schedules the
drafts. *(In the QDE lane the second one includes the legal-accuracy check, which is never
skipped and never automated.)*

**What still stops a job is an error, not an approval:** a missing or unreadable VTT, no
ClickUp task for the VID_ID, a missing or failed asset, a prompt or brand kit not present on
`main`, or content that belongs to a different brand. A human fixes the input. Nobody
approves an output.

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

> **Three rows above have since been overturned, and that is worth understanding rather than
> editing away.** The upload method is now the `yutu` CLI from local disk; Metricool posts
> are now created as drafts on purpose; and the right-hand column of row 4 is itself now
> wrong, since `autoPublish: false` is banned but an agent never schedules at all. Every
> reversal was a deliberate decision with reasons recorded in the pipeline files.
>
> **The lesson of 2026-07-06 was never the specific settings — it was acting without
> reading the current SOP.** That lesson is unchanged, and these reversals are the proof of
> it: an agent working from memory of this table would now get three of six wrong.

---

## Referenced SOP files

⚠️ **Most of the `betty/` paths below are not on GitHub `main`.** Under the repo's own rule
an uncommitted file is a blocked job, not an input — so an agent told to "read all of
these" will correctly stop. Before relying on any of them, check `main`:

- `betty/Betty_SOP_YouTube_Publishing_QDE.md` — ⚠️ not on `main`
- `betty/Betty_SOP_Metricool_Syndication_QDE_v1.md` — ⚠️ not on `main`; the local copy is
  dated 2026-05-31 and covers TikTok + Instagram only, with no Facebook
- `betty/Betty_SOP_VideoSmimeo_IG_Resize_Normalize_v1.md` — ⚠️ not on `main`, though the
  pipelines name it as the Phase 5 governing doc
- `betty/Video_Publishing_Workflow_HU_and_QDE_v1.md` — ⚠️ not on `main`
- `betty/Publishing_Kickoff_and_Intake_Form_v1.md` — ⚠️ not on `main`

**On `main` and authoritative** (highest-numbered file of each name):

- `joan-supervising-agent/HU_Video_Publishing_Pipeline_V<n>.md`
- `joan-supervising-agent/QDE_Video_Publishing_Pipeline_V<n>.md`
- `peggy-olson-copywriting/hu_description_prompt_V<n>.md`
- `peggy-olson-copywriting/qde_legal_description_prompt_V<n>.md`
- `brands/handwriting-university.md` · `brands/qde-brand.md`

---

## Changelog

| Date | Version | Change |
| :--- | :--- | :--- |
| 2026-07-06 | v2 | Created after confirmed procedure failure across all five pipeline steps. |
| 2026-09-05 | v2.1 | Gate 4 YouTube upload method corrected to `yutu` CLI local-file upload. Gate 1 `find` placeholder replaced with a runnable `grep -rl`. Caption limit tightened from ≤6 to ≤5 words per cue. |
| 2026-09-12 | V4 | Header version corrected — the previous file's header said "v2.1" while its filename said v3. Gate 4 Metricool rewritten to the two-stage draft rule. Gate 4 media line now points at Phase 8 instead of restating it. Gate 3 approval source marked unconfirmed and set to fail closed. Authority corrected to GitHub-beats-local. Referenced SOP list flagged against `main`. Failure table annotated rather than edited. |
| 2026-09-12 | V5 | Cross-references no longer name an exact version — they use `_V<n>` and instruct the reader to take the highest. Ends the cascade where bumping one file made every file pointing at it wrong. No procedural change. |
| 2026-09-12 | V6 | Client-approval gate deleted (the Ready-to-Publish folder is the approval); its destination-channel check moved into Gate 2. The 3-minute duration gate deleted — ship full length, always. Instagram's 90-second ceiling noted as gone; Facebook's 90-second REEL/POST split explicitly unchanged. Gates renumbered 1–3. New "What this checklist does NOT gate" section. |

*Update this file whenever a new failure adds a lesson. **Bump the number in the filename and in the header together, and delete the file it replaces.** Never leave two live.*
