# joan-supervising-agent

Orchestration for the video publishing pipelines: the phase map, the review gate, ClickUp
handling, and the pre-flight checklist every job runs first.

**Last updated:** 2026-09-14

---

## Which file is current

**The version is in the filename, the highest number wins, and every change bumps it.**
Any edit to a numbered file's content produces the next number, and the file it replaces is
deleted in the same commit. Never two live.

The version header inside a file must match its filename. If they disagree, the filename is
right and the header needs fixing.

**Cross-references never name an exact version.** Anything written below as
`Something_V<n>.md` means *the highest-numbered `Something_V*.md` in that folder* — it might
be V5, V6 or V8. Always take the highest. This is why a bump in one file never makes another
file wrong.

**READMEs are exempt from numbering** and stay unnumbered, because GitHub renders them by
name. They carry a *Last updated* date instead. That is safe only because a README here
states no rule that is not stated in a numbered file — if you find one that does, that is
the bug.

---

## This folder states no rules of its own

Everything below is a pointer. If you find an operational rule written in this README, it is
a bug — the rule belongs in the pipeline file, and a second copy of it will be wrong within a
month. That is exactly what happened to the README this one replaces: it had become a full
duplicate of the HU pipeline and had already drifted out of sync with it.

| You need | Read (highest `n` wins) |
| :--- | :--- |
| The HU publishing procedure, end to end | `HU_Video_Publishing_Pipeline_V<n>.md` |
| The QDE publishing procedure, end to end | `QDE_Video_Publishing_Pipeline_V<n>.md` |
| The gate that runs **before** any pipeline job | `Joan_PreFlight_Pipeline_Checklist_V<n>.md` |
| Voice, palette, typography, banned terms | `brands/<brand>.md` — never a pipeline file |
| Thumbnail methods and build scripts | `salvatore-art-department/` |
| Description and caption prompts | `peggy-olson-copywriting/` |
| Social and video execution SOPs | `betty-social-media-manager/` |

---

## Start here, in this order

1. **Pre-flight checklist.** Resolve the brand from the Ready-to-Publish folder *first* —
   you cannot choose the pipeline file until you know the lane — then identify the SOP, read
   it end to end, and verify assets. A job that skips this is how the 2026-07-06 failure
   happened.
2. **The pipeline file for the resolved brand.** HU and QDE are separate documents on
   purpose — they have different voice rules, different thumbnail house styles, and
   different CTA policy. Never run one brand's pipeline against the other's content.
3. **The brand kit.** Every voice, palette and terminology question resolves there.

---

## The ten phases at a glance

Orientation only. Every rule, setting and exception lives in the pipeline file — go there
before doing any of this.

| Phase | What happens | Owner |
| :--- | :--- | :--- |
| **0** | Pre-flight: **brand resolved from the folder**, assets, ClickUp task, repo freshness | Joan |
| **1** | Generate captions, clean the VTT to ≤5 words per cue, fix name spellings | Betty |
| **2** | Six title options written from the cleaned transcript | Peggy |
| **3** | The description package — five platform outputs in one file | Peggy |
| **4** | Thumbnails: 16:9 for YouTube, 9:16 cover for the Reel | Salvatore |
| **5** | The vertical 9:16 cut, confirmed by ffprobe and never by filename | Betty |
| **6** | YouTube upload via the `yutu` CLI — **private**, title, description, thumbnail | Betty |
| **7** | Caption upload. Always last on YouTube, always after the thumbnail | Betty |
| **8** | Two media URLs, then four Metricool **drafts** — **two of them Facebook** — never scheduled | Betty |
| **9** | Verify everything, notify the reviewer, append the ledger | Joan |

**Phases 0–9 run agent-to-agent with no human step.** The work then stops and waits.

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

### The only two human touchpoints

1. **Someone puts the video in the Ready-to-Publish folder** — the approval to start, and
   also how the system learns the brand. *(That folder is the approval. Phase 0 does not
   check a spreadsheet for one.)*
2. **The reviewer makes the video public and schedules the drafts** — the approval to publish.

Anything else that halts a job is a **broken input, not an approval** — a missing VTT, no
ClickUp task, a missing asset, a prompt not on `main`, a brand that will not resolve, or
content in the wrong lane. A human fixes the input; nobody approves an output.

⚠️ **QDE has one addition:** the legal-accuracy check, which is part of touchpoint 2.
Statutes, jurisdictions, citations, credentials and timestamps are verified by a human before
the video goes public, and any `[TO VERIFY]` marker left in the copy is a blocker. See the
QDE pipeline, Gate 7.

---

## Four rules for anything committed here

**One spec, one home.** If a rule or number already exists in another file, link to it.
Restating is how two files come to disagree.

**Every change bumps the number in the filename** — and the file it replaces is deleted in
the same commit. Bumping and leaving the predecessor live recreates the ambiguity the rule
exists to prevent. **Never write an exact version into a cross-reference.**

**Retire by deleting, or by moving to `_retired/YYYY-MM-DD/`.** Git history keeps the file
either way. A missing file throws a loud error; a stale file gets read and believed.

**Assets are pulled, not mirrored.** Images in the Drive libraries are fetched on demand.
Cite the Drive folder ID, never a local path.

---

## Before you commit

- [ ] Does another file already state this? Link instead.
- [ ] Does this contradict anything written elsewhere? Search first.
- [ ] **Is the rule you are writing still current?** Check project memory and the newest
      ruling before copying from an existing document. A file written from a stale sibling
      inherits its errors — that is how the retired Facebook 90-second split survived into
      three files after it had been overturned.
- [ ] Number bumped in **both** the filename and the header, and do they match?
- [ ] **Is the file it replaces deleted in the same commit?** Never leave two live.
- [ ] Did you write an exact version into a reference? Use `_V<n>` instead.
- [ ] Mac pulled since?
