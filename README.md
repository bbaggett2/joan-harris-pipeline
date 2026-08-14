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

**One spec, one home.** If a rule or number already exists in another file, link to it. Restating
is how two files come to disagree.

**Version numbers go in the file header, not the filename.** Versioned filenames produce several
live copies and no way to know which one an agent read.

**Retire by moving, not deleting.** Superseded documents go to `_retired/YYYY-MM-DD/`. A missing
file throws a loud error; a stale file gets read and believed.

**Assets are pulled, not mirrored.** Images in the Handwriting University Drive library are fetched
on demand. Cite the Drive folder ID, never a local path.

## Layout

| Folder | Contents | Start here |
| :--- | :--- | :--- |
| `brands/` | Brand kits — voice, palette, typography, layout | the brand file for your lane |
| `salvatore-art-department/` | Graphics SOPs, thumbnail methods, build scripts, host photos | `Salvator_AI_Graphics_SOP_v1.md` |
| `joan-supervising-agent/` | Orchestration — step maps, human gates, ClickUp | `HU_Thumbnail_Step_Map_v1.md` |
| `betty-social-media-manager/` | Social and video SOPs | `README.md` |

## Before you commit

- [ ] Does another file already state this? Link instead.
- [ ] Does this contradict anything written elsewhere? Search first.
- [ ] Did a filename change? Grep the repo for the old one.
- [ ] Header version updated, filename left alone?
- [ ] Anything superseded moved to `_retired/`?
- [ ] Mac pulled since?
