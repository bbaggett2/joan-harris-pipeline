# Joan Pre-Flight Pipeline Checklist — V7

**Owner:** Joan Harris
**Version:** V7 — matches the filename. Highest number is current.
**Last updated:** 2026-09-14
**Status:** AUTHORITATIVE — supersedes V6
**Purpose:** Self-enforcing gate that runs BEFORE any pipeline or publishing job. Exists because Joan followed a skill's built-in instructions instead of the committed SOPs on 2026-07-06 and produced wrong outputs across all five steps.

> **Versioning:** the version lives in the filename and the highest number wins. A new
> revision becomes `..._V8.md` and this file is deleted in the same commit. Never two live.
>
> **Cross-references never name an exact version.** A file referred to below as
> `Something_V<n>.md` means *the highest-numbered `Something_V*.md` in that folder* — it
> might be V5, V6 or V8. Always take the highest.

**Rule:** If any item below is NOT checked, Joan stops and resolves it before touching any tool.

---

## WHAT CHANGED IN V7

1. **Brand resolution is the new Gate 1, and it runs before SOP identification.** This fixes
   a chicken-and-egg that has been here since V4: the old Gate 1 said "read the brand's
   pipeline file," but the brand was only confirmed by a gate *inside* that file. You cannot
   choose the document until you know the brand. Gates renumbered — SOP identification is
   now Gate 2, assets Gate 3, platform settings Gate 4.
2. **Facebook's 90-second split is gone.** *(Bart 2026-09-13.)* Facebook takes **two posts
   every time** — a full-length POST and a short vertical REEL — and the check is **byte size
   against the 500 MB cap**, not duration.
3. **Gate 3 now records the full-length cut's byte size.** The Facebook POST needs that file;
   V6 only ever accounted for the vertical one.

---

## Gate 1 — Brand resolution (runs FIRST, before anything else)

**The brand is decided by the Ready-to-Publish folder the video came out of.** A person put
it there; which folder they chose *is* the decision. Joan resolves it once, here, and writes
it down. Nothing downstream re-infers it.

- [ ] Read the **folder ID** the video was picked up from — not the folder's name.
      The name is the human-readable label and a fallback only; IDs survive a rename.

  | Folder | Brand |
  |---|---|
  | `1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv` — "3. Ready to Publish - HU brand" | **HU** |
  | ⛔ `[TO VERIFY]` — not yet identified | **QDE** |
  | *(none exists)* | Bart Show / BAB — cannot be resolved |

- [ ] **Write the resolved brand to the `PipelineState` row** for this VID_ID.
- [ ] Confirm it will reach Metricool: it must also land in
      `<VID_ID>_Description_Package_v1.md`, which is the only place Betty reads the lane from.
- [ ] ⛔ **No folder match, or content that straddles two brands → STOP and report.**
      An unresolvable brand is an error, not a guess. Never pick.

> ⛔ **QDE has no folder ID yet.** Until it is identified, record which staging location the
> video was taken from, so the substitution is visible rather than silent. Never reuse the HU
> folder ID for QDE.

**Everything brand-dependent hangs off this one value** — the Metricool `blogId` (HU `6267975`
/ QDE `6268508`), the YouTube channel, the Facebook page ID, the description prompt, the
thumbnail method, CTA policy and banned terms.

## Gate 2 — SOP identification

- [ ] Name the task domain (video publishing / website edit / Metricool / caption / etc.)
- [ ] **Read the authoritative file on GitHub `main` first.** For video publishing that is
      the pipeline for the brand resolved at Gate 1 —
      `joan-supervising-agent/HU_Video_Publishing_Pipeline_V<n>.md` or
      `QDE_Video_Publishing_Pipeline_V<n>.md`, highest `n` in the folder.
- [ ] Then search the local cache for anything else relevant:

  ```bash
  export SOP_ROOT="$HOME/mnt/joan foundation documents and SOP"
  grep -rl "<domain keyword>" "$SOP_ROOT" --include="*.md"
  ```

- [ ] Read every matching SOP from start to finish — not skimmed, read
- [ ] If no SOP exists: **STOP. Tell the reviewer. Ask for the correct document.**
- [ ] **Authority order: GitHub `main` > local SOP > skills and plugins.** A local file that
      disagrees with `main` is stale, not a fallback. An uncommitted file is a blocked job.

## Gate 3 — Asset verification (before writing any copy or touching any platform)

For video publishing jobs specifically:

- [ ] Is there a full, cleaned VTT transcript for each video? (No → generate it first;
      descriptions cannot be written without it)
- [ ] Is there a vertical 9:16 cut? **Confirm with `ffprobe`, never by filename.**
      If only a landscape master exists, it gets built in Phase 5.
- [ ] Is the **full-length cut** located, and its **byte size recorded**? The Facebook POST
      carries this file, and 500 MB is the cap that will actually block it.
- [ ] Duration: record it, but **it gates nothing. Ship full length, always.**
      *(V5 and earlier stopped on anything over 3 minutes; deleted 2026-09-12.)*
- [ ] Are thumbnails generated — real ones from the locked brand method, not placeholder art?
      *(Thumbnail approval no longer happens here. It happens at the single review, with
      the thumbnail already on the private video.)*
- [ ] Is the destination channel confirmed **against the brand resolved at Gate 1**? QDE and
      HU never cross. Read the channel ID from that brand's pipeline file, not from memory.

## Gate 4 — Platform settings (never assume defaults)

### YouTube upload

- [ ] Method: **direct terminal upload via the `yutu` CLI with a local file path.**
      rclone the render down from Drive first. **Not** YouTube Studio, not a Chrome session.
- [ ] Visibility: **PRIVATE.** Not Unlisted, not Public, not Scheduled. The video stays
      private until the reviewer makes it public — that is the approval.
- [ ] Playlist: confirm the correct playlist for the content type.

### Metricool posts

- [ ] **`blogId` comes from the brand resolved at Gate 1** — HU `6267975`, QDE `6268508`.
      Never typed from memory, never inferred at this step.
- [ ] **Agents create DRAFTS.** `draft: true`, no publish time. An agent never schedules a post.
- [ ] **A scheduled post is `autoPublish: true` + `draft: false`.** The reviewer sets that
      when they schedule. ⛔ `autoPublish: false` is banned outright — it is not a hold, it
      is a phone notification that silently dies. It stranded two QDE TikTok posts on
      2026-05-27 and an HU Instagram post on 2026-09-25.
- [ ] One post per network — **except Facebook, which always gets two.**
- [ ] **Facebook: a POST carrying the full-length cut AND a REEL carrying the short vertical
      cut, every time.** *(Bart 2026-09-13 — the old 90-second split is retired.)* Reels and
      the feed are separate surfaces; publishing one leaves the other empty. **No duration
      test decides either type.**
- [ ] **Facebook POST media under 500 MB?** This is the real constraint. Over it → compress
      first. Compressing for a size cap is **not** trimming; the cut stays full length.
- [ ] If no short vertical cut exists, the Facebook REEL is simply not created. ⛔ Never
      substitute a landscape master into a Reel.
- [ ] **Instagram takes video of any length.** *(Changed 2026-09-12.)* Aspect ratio still
      applies: Instagram rejects horizontal video outright.
- [ ] Media: see Phase 8 of the brand's pipeline file. *(Short version: hand Metricool the
      Google Drive URL; the FTP bridge is a fallback for files owner-only to an editor's
      account. Not restated here — one spec, one home.)*
- [ ] The YouTube video is already live from the pipeline, so **do not** create a YouTube
      Metricool post — it would duplicate.
- [ ] ⚠️ A failed `createScheduledPost` leaves **nothing** in the planner. If a whole network
      set fails at once, suspect the media file.
- [ ] ⚠️ `updateScheduledPost` **reissues the post id.** Re-read after any update; never
      reuse the pre-update id.

### Captions

- [ ] Source: Google Drive built-in caption generator, not YouTube ASR.
- [ ] Cleaned to **≤5 words per cue**, ≤2 lines, timing preserved.
- [ ] "Baggett" misspelling correction pass applied.
- [ ] Uploaded **after** the thumbnail is set — captions are the last YouTube step.
- [ ] ⛔ Caption upload is **not** `yutu`. It is a separate tool from video upload.

---

## What this checklist does NOT gate

Read this before adding a gate back. Each was removed deliberately, and the reasoning is
recorded so nobody restores one thinking it was lost by accident.

| Not gated | Why |
| :--- | :--- |
| **Client approval** | The Ready-to-Publish folder is the approval. A video is in it because a person put it there. The old gate read the MASTER sheet for an "Approved By Client" column that was never found, so it failed closed on every video. |
| **Brand** | Brand is **resolved, not approved.** A human chose it by picking the folder. Gate 1 reads that decision and records it; nobody is asked to confirm it. |
| **Duration / trimming** | Ship full length, always. No platform has a duration gate any more — Instagram's went 2026-09-12, Facebook's 2026-09-13. |
| **Title, description, caption copy** | No human reads it until it is staged. That is why Peggy's marking discipline is absolute and why every `[TO VERIFY]` is a blocker at Phase 9. |
| **Thumbnail choice** | Reviewed on the private video. A rejected thumbnail re-runs Phase 4 and swaps on the live video — a redo, not a failure. |

**There are exactly two human touchpoints in the whole pipeline:** someone puts the video in
the Ready-to-Publish folder, and the reviewer makes the video public and schedules the
drafts. *(In the QDE lane the second one includes the legal-accuracy check, which is never
skipped and never automated.)*

**What still stops a job is an error, not an approval:** a missing or unreadable VTT, no
ClickUp task for the VID_ID, a missing or failed asset, a prompt or brand kit not present on
`main`, a brand that will not resolve, or content that belongs to a different brand. A human
fixes the input. Nobody approves an output.

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
> wrong, since `autoPublish: false` is banned but an agent never schedules at all.
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
| 2026-09-12 | V4 | Header version corrected. Gate 4 Metricool rewritten to the two-stage draft rule. Gate 4 media line now points at Phase 8 instead of restating it. Gate 3 approval source marked unconfirmed and set to fail closed. Authority corrected to GitHub-beats-local. Referenced SOP list flagged against `main`. Failure table annotated rather than edited. |
| 2026-09-12 | V5 | Cross-references no longer name an exact version — they use `_V<n>` and instruct the reader to take the highest. No procedural change. |
| 2026-09-12 | V6 | Client-approval gate deleted (the Ready-to-Publish folder is the approval); its destination-channel check moved into Gate 2. The 3-minute duration gate deleted — ship full length, always. Instagram's 90-second ceiling noted as gone. Gates renumbered 1–3. New "What this checklist does NOT gate" section. |
| 2026-09-14 | V7 | Brand resolution added as Gate 1 and moved ahead of SOP identification, ending the chicken-and-egg where you had to read the brand's pipeline to learn the brand. Gates renumbered 1–4. Facebook's 90-second split removed — two posts every time, and the check is byte size against 500 MB. Gate 3 now records the full-length cut's byte size. |

> ⚠️ **V6 shipped carrying a rule that had already been overturned.** It was written on
> 2026-09-12 and stated that Facebook "still splits on 90 seconds" — a rule Bart had retired
> on 2026-09-13 — because it was written from the pipeline files without re-checking the
> newer ruling first. **That is precisely the failure this checklist exists to prevent**, so
> it is recorded here rather than quietly corrected. Gate 2 says read the authoritative
> source *first*. It applies to whoever is editing these documents, not only to whoever is
> running a job.

*Update this file whenever a new failure adds a lesson. **Bump the number in the filename and in the header together, and delete the file it replaces.** Never leave two live.*
