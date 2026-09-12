# joan-supervising-agent — V2

Orchestration for the video publishing pipelines: the phase map, the review gate, ClickUp
handling, and the pre-flight checklist every job runs first.

> ⚠️ **`README.md` in this folder is the old duplicate HU pipeline and should be deleted.**
> Under the repo's versioning rule this file (V2) supersedes it — but an unnumbered
> `README.md` is what GitHub renders on the folder page, so leaving it there is exactly the
> confusion the rule exists to prevent.

---

## Which file is current

**The version is in the filename, and the highest number wins.** `..._V10.md` beats
`..._V9.md`. A file with no number is older than any numbered file of the same name. When a
new version lands, the old one is deleted — never two live.

You may still find version headers *inside* files. Those must match the filename. If they
disagree, the filename is right and the header needs fixing.

---

## This folder states no rules of its own

Everything below is a pointer. If you find an operational rule written in this README, it is
a bug — the rule belongs in the pipeline file, and a second copy of it will be wrong within a
month. That is what happened to the file this one replaces.

| You need | Read |
| :--- | :--- |
| The HU publishing procedure, end to end | `HU_Video_Publishing_Pipeline_V10.md` |
| The QDE publishing procedure, end to end | `QDE_Video_Publishing_Pipeline_V10.md` |
| The gate that runs **before** any pipeline job | `Joan_PreFlight_Pipeline_Checklist_V4.md` |
| Voice, palette, typography, banned terms | `brands/<brand>.md` — never a pipeline file |
| Thumbnail methods and build scripts | `salvatore-art-department/` |
| Description and caption prompts | `peggy-olson-copywriting/` |
| Social and video execution SOPs | `betty-social-media-manager/` |

---

## Start here, in this order

1. **Pre-flight checklist.** Identify the SOP, read it end to end, verify assets. A job that
   skips this is how the 2026-07-06 failure happened.
2. **The pipeline file for the brand.** HU and QDE are separate documents on purpose — they
   have different voice rules, different thumbnail house styles, and different CTA policy.
   Never run one brand's pipeline against the other's content.
3. **The brand kit.** Every voice, palette and terminology question resolves there.

---

## The ten phases at a glance

Orientation only. Every rule, setting and exception lives in the pipeline file — go there
before doing any of this.

| Phase | What happens | Owner |
| :--- | :--- | :--- |
| **0** | Pre-flight: brand, client approval, assets, ClickUp task, repo freshness | Joan |
| **1** | Generate captions, clean the VTT to ≤5 words per cue, fix name spellings | Betty |
| **2** | Six title options written from the cleaned transcript | Peggy |
| **3** | The description package — five platform outputs in one file | Peggy |
| **4** | Thumbnails: 16:9 for YouTube, 9:16 cover for the Reel | Salvatore |
| **5** | The vertical 9:16 cut, confirmed by ffprobe and never by filename | Betty |
| **6** | YouTube upload via the `yutu` CLI — **private**, title, description, thumbnail | Betty |
| **7** | Caption upload. Always last on YouTube, always after the thumbnail | Betty |
| **8** | Media URL, then four Metricool **drafts** — one per network, never scheduled | Betty |
| **9** | Verify everything, notify the reviewer, append the ledger | Joan |

**Phases 1–9 run agent-to-agent with no human step.** The work then stops and waits.

---

## The review gate

Agents run unattended up to the point where the work is staged, and then everything holds.
The video sits PRIVATE on YouTube; the social posts sit as **drafts** in Metricool. Neither
can reach an audience. The reviewer gets one notice with both links, fixes anything wrong in
place, then makes the video public and schedules the drafts — and those two actions are the
approval. There is no approval form and no third tool.

**The reviewer is a configured role, not a named person.** One value holds the notification
address and the accounts whose action counts as approval, so handing review to a hired person
is a config change, not a rewrite.

⚠️ **QDE has one addition:** the legal-accuracy check. Statutes, jurisdictions, citations,
credentials and timestamps are verified by a human before the video goes public, and any
`[TO VERIFY]` marker left in the copy is a blocker. See the QDE pipeline, Gate 7.

---

## Four rules for anything committed here

**One spec, one home.** If a rule or number already exists in another file, link to it.
Restating is how two files come to disagree.

**Version in the filename, highest number current** — and **delete the old file when the new
one lands.** Bumping the number and leaving the predecessor live recreates the ambiguity the
rule exists to prevent.

**Retire by moving or deleting.** Superseded documents go to `_retired/YYYY-MM-DD/` or are
deleted outright; git history keeps them either way. A missing file throws a loud error; a
stale file gets read and believed.

**Assets are pulled, not mirrored.** Images in the Drive libraries are fetched on demand.
Cite the Drive folder ID, never a local path.

---

## Before you commit

- [ ] Does another file already state this? Link instead.
- [ ] Does this contradict anything written elsewhere? Search first.
- [ ] Did a filename change? Grep the repo for the old one.
- [ ] Version bumped in **both** the filename and the header, and do they match?
- [ ] **Is the superseded file deleted?** Never leave two live.
- [ ] Mac pulled since?
