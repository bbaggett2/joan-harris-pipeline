# joan-harris-pipeline

Pipeline to manage agents for publishing and brand lanes.

---

## GitHub is the source of record. The Mac is a clone.

Every SOP, brand file, and script here has one authoritative copy: the one on `main`. The copy on
Joan's Mac Studio exists so scripts can run against local files. It is a `git pull` clone, nothing
more.

| Action | Where |
| :--- | :--- |
| Edit an SOP, brand file, or script | **GitHub only** |
| Get the current version onto the Mac | `cd $REPO_ROOT && git pull origin main` |
| Hand-edit a file in the local folder | **Never** |

A locally edited file gets overwritten or throws a conflict on the next pull. Both are fine — they
surface the problem. A quietly diverged copy does not.

## Four rules

**One spec, one home.** If a rule or number already exists in another file, link to it.
Restating is how two files come to disagree.

**The version goes IN the filename, and the highest number is current.**
`HU_Video_Publishing_Pipeline_V10.md` beats `..._V9.md`, always. A file with no number is older
than any numbered file of the same name. This is Bart's rule, set 2026-09-12, and it replaces the
earlier "version in the header, not the filename" rule — which is why you may still find files
whose headers say otherwise.

> ⚠️ **This rule only works if you delete the old file.** Bumping the number and leaving the
> predecessor live recreates the exact problem it exists to prevent — two live copies, and an
> agent that reads whichever one it happened to open. When a V10 lands, the V9 goes. Every time.
> The version header inside the file stays too, and must match the filename.

**Retire by moving or deleting — but do not leave it in place.** A superseded document either
goes to `_retired/YYYY-MM-DD/` or gets deleted outright, since git history keeps it either way.
A missing file throws a loud error; a stale file gets read and believed.

**Assets are pulled, not mirrored.** Images in the Handwriting University Drive library are fetched
on demand. Cite the Drive folder ID, never a local path.

## Layout

| Folder | Contents | Start here |
| :--- | :--- | :--- |
| `brands/` | Brand kits — voice, palette, typography, layout | the brand file for your lane |
| `joan-supervising-agent/` | Orchestration — pipelines, the review gate, pre-flight | `README_V2.md` |
| `salvatore-art-department/` | Graphics SOPs, thumbnail methods, build scripts, host photos | `Salvator_AI_Graphics_SOP_v1.md` |
| `peggy-olson-copywriting/` | Description and caption prompts, brand voice | the prompt for your lane |
| `betty-social-media-manager/` | Social and video execution SOPs | `README.md` |

## Before you commit

- [ ] Does another file already state this? Link instead.
- [ ] Does this contradict anything written elsewhere? Search first.
- [ ] Did a filename change? Grep the repo for the old one.
- [ ] Is the version number bumped in **both** the filename and the header?
- [ ] **Is the superseded file deleted or moved to `_retired/`?** Never leave two live.
- [ ] Mac pulled since?
