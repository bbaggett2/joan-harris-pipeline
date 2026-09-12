# joan-harris-pipeline

Pipeline to manage agents for publishing and brand lanes.

**Last updated:** 2026-09-12

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

**The version goes IN the filename, the highest number is current, and EVERY change bumps it.**
`HU_Video_Publishing_Pipeline_V10.md` beats `..._V9.md`, always. A file with no number is older
than any numbered file of the same name.

> **Every change means every change.** Not "significant" changes, not "procedure" changes — any
> edit to the content produces the next number. There is no judgment call about what counts,
> which is the point: if the number moved, something is different, and you do not have to read
> both files to find out whether it mattered.
>
> ⚠️ **Bumping the number and leaving the old file live is the failure this prevents.** The new
> file and the deletion of the old one are the same action. Never two live. The version header
> inside the file moves with the filename, and the two must match.
>
> *Exemption — `README.md` only.* GitHub renders `README.md` by name on the repo and folder
> pages; a numbered README renders nowhere. READMEs therefore stay unnumbered and carry a
> **Last updated** date instead. This is safe because a README here is navigation: it points at
> the numbered files and states no rule that is not stated in one of them. Nothing authoritative
> escapes the numbering.

**Retire by deleting, or by moving to `_retired/YYYY-MM-DD/`.** Git history keeps the file either
way. A missing file throws a loud error; a stale file gets read and believed.

**Assets are pulled, not mirrored.** Images in the Handwriting University Drive library are fetched
on demand. Cite the Drive folder ID, never a local path.

## Layout

| Folder | Contents | Start here |
| :--- | :--- | :--- |
| `brands/` | Brand kits — voice, palette, typography, layout | the brand file for your lane |
| `joan-supervising-agent/` | Orchestration — pipelines, the review gate, pre-flight | the folder README |
| `salvatore-art-department/` | Graphics SOPs, thumbnail methods, build scripts, host photos | `Salvator_AI_Graphics_SOP_v1.md` |
| `peggy-olson-copywriting/` | Description and caption prompts, brand voice | the prompt for your lane |
| `betty-social-media-manager/` | Social and video execution SOPs | the folder README |

## Before you commit

- [ ] Does another file already state this? Link instead.
- [ ] Does this contradict anything written elsewhere? Search first.
- [ ] Did a filename change? Grep the repo for the old one.
- [ ] **Number bumped in the filename AND the header, and do they match?**
- [ ] **Is the file it replaces deleted in the same commit?** Never leave two live.
- [ ] Mac pulled since?
