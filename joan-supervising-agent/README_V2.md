# joan-supervising-agent

Orchestration for the video publishing pipelines: phase maps, the review gate, ClickUp
handling, and the pre-flight checklist every job runs first.

> ⚠️ **This file is not yet canonical.** The live `README.md` in this folder is a full
> second copy of the HU pipeline, and it has already drifted from the named pipeline file.
> On approval: move that README to `_retired/2026-09-12/` and rename this file to
> `README.md`.

---

## This folder states no rules of its own

Everything here is a pointer. If you find an operational rule written in this README,
it is a bug — the rule belongs in the pipeline file, and a second copy of it will be wrong
within a month. That is what happened to the file this one replaces.

| You need | Read |
| :--- | :--- |
| The HU publishing procedure, end to end | `HU_Video_Publishing_Pipeline_V10.md` |
| The QDE publishing procedure, end to end | `QDE_Video_Publishing_Pipeline_V10.md` |
| The gate that runs **before** any pipeline job | `Joan_PreFlight_Pipeline_Checklist_V4.md` |
| Voice, palette, typography, banned terms | `brands/<brand>.md` — never a pipeline file |
| Thumbnail methods and build scripts | `salvatore-art-department/` |
| Social and video execution SOPs | `betty-social-media-manager/` |

---

## Start here, in this order

1. **Pre-flight checklist.** Identify the SOP, read it end to end, verify assets. A job
   that skips this is how the 2026-07-06 failure happened.
2. **The pipeline file for the brand.** HU and QDE are separate documents on purpose —
   they have different voice rules, different thumbnail house styles, and different CTA
   policy. Never run one brand's pipeline against the other's content.
3. **The brand kit.** Every voice, palette and terminology question resolves there.

---

## The review model, in one paragraph

Agents run the pipeline unattended up to the point where the work is staged, and then
everything holds. The video sits PRIVATE on YouTube; the social posts sit as **drafts** in
Metricool. Neither can reach an audience. The reviewer gets one notice with both links,
fixes anything that is wrong in place, then makes the video public and schedules the
drafts — and those two actions are the approval. There is no approval form and no third
tool. **The reviewer is a configured role, not a named person.**

---

## Four rules for anything committed here

**One spec, one home.** If a rule or number already exists in another file, link to it.
Restating is how two files come to disagree.

**Version numbers go in the file header, not the filename.** Versioned filenames produce
several live copies and no way to know which one an agent read. Files currently carrying
`V10`, `V2` or `V4` in their names are under review and lose the suffix on approval.

**Retire by moving, not deleting.** Superseded documents go to `_retired/YYYY-MM-DD/`.
A missing file throws a loud error; a stale file gets read and believed.

**Assets are pulled, not mirrored.** Images in the Drive libraries are fetched on demand.
Cite the Drive folder ID, never a local path.

---

## Before you commit

- [ ] Does another file already state this? Link instead.
- [ ] Does this contradict anything written elsewhere? Search first.
- [ ] Did a filename change? Grep the repo for the old one.
- [ ] Header version updated, filename left alone?
- [ ] Anything superseded moved to `_retired/`?
- [ ] Mac pulled since?
