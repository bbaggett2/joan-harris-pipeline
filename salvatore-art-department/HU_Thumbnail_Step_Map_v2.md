# HU Thumbnail — Step Map for n8n

**Version:** v2 — matches the filename. Highest number is current.
**Last updated:** 2026-09-12
**Purpose:** one row per callable step. Each row names its inputs, its output, and **the one
document it reads.** A step that has to read three files to know what to do is a step that will
drift.

> **Versioning:** the version is in the filename and the highest number wins. A new revision
> becomes `..._v3.md` and this file is deleted in the same commit. Cross-references never name
> an exact version — `Something_v<n>.md` means the highest-numbered one in that folder.

---

## What changed in v2

**The two mid-process approval gates are gone.** v1 stopped the chain twice to wait for Bart —
Step 6 for the 16:9 and Step 10 for the 9:16. The publishing pipeline replaced all four
per-phase sign-offs with **one review**, done once on the private YouTube video and the
Metricool drafts. Those two gates no longer exist, so Salvatore no longer waits at them.

**Every place Bart appears as the person who made a design ruling is unchanged** — his election
of Path B, the variants he tested and rejected, the defects he accepted. That is a record of who
decided what, not a workflow instruction.

---

## Document routing — read this first

| Document | Scope | Who reads it |
| :--- | :--- | :--- |
| `brands/handwriting-university.md` §6 | 16:9 layout | Steps 4, 6 |
| `HU_Thumbnail_Creation_Process_v<n>.md` | **Path A**, generated host | Steps 2, 3 |
| `HU_PathB_Frame_Acquisition_v<n>.md` | **Path B**, screengrab | Steps 2B, 3B |
| `HU_Thumbnail_Constants_v<n>.md` | **Both paths.** Numbers, geometry, logo, fonts, asserts | Steps 5, 7, 8, 9 |
| `HU_Brand_Thumbnail_v<n>_Screenshot_Torn_Parchment.md` | Path routing rules | Step 1 |

**Default is Path A.** Absence of instruction means Path A. An agent never elects Path B.

---

## The two invariants

**1. One video, one path.** The 16:9 and the 9:16 for a given video use the same host source. A
generated Bart on the thumbnail and a photographic Bart on the Reel cover will not match.

**2. The path is recorded, not remembered.** Step 1 writes `path` into the job record. Every
later step reads it from there. Never infer it, never re-decide it.

---

## Step contracts

### Step 1 — Resolve path

| | |
| :--- | :--- |
| **In** | video ID, transcript, Bart's election if any |
| **Out** | `path: "A" \| "B"` written to the job record |
| **Reads** | `HU_Brand_Thumbnail_v<n>_Screenshot_Torn_Parchment.md` |
| **Fails if** | anything other than an explicit written election tries to set `B` |

Default to `A`. This step exists so no later step has to decide.

> **Path B election stays with Bart.** It is a brand decision about how the host is portrayed,
> not a quality check, so it did not move to the reviewer. No agent elects Path B, and neither
> does the reviewer.

---

### Step 2 — Acquire host plate, 16:9

**2A — Path A**

| | |
| :--- | :--- |
| **In** | transcript, emotional register, reference image set |
| **Out** | 16:9 host plate — host and scene only, no text, no handwriting, no logo |
| **Reads** | the Path A creation process, §6 |
| **Fails if** | the plate contains handwriting, headline, parchment, or logo |

**2B — Path B**

| | |
| :--- | :--- |
| **In** | source video |
| **Out** | 16:9 frame, headroom verified |
| **Reads** | `HU_PathB_Frame_Acquisition_v<n>.md` §1 |
| **Fails if** | no frame has quiet dead space above the hair — reject early, do not proceed |

---

### Step 3 — Verify host

**3A — Path A: likeness recognition**

| | |
| :--- | :--- |
| **In** | new plate, last two published thumbnails |
| **Out** | pass / regenerate |
| **Reads** | the Path A creation process, §6.2 |
| **Note** | Salvatore compares side by side and asks **"is this the same man"** — not "is this a good image." No assert substitutes for that judgement. If it is not clearly the same man, regenerate; do not pass it on and hope. |

⚠️ **This is the step the single-review model costs something at.** v1 put a human eye here, and
now the only human eye lands later, at the review, with the thumbnail already on the private
video. A likeness that drifts still gets caught — but as a redo rather than a catch. If drift
starts happening, this is the step to put a person back on.

**3B — Path B: hair and face detection**

| | |
| :--- | :--- |
| **In** | frame |
| **Out** | `hair_y`, `face_y` |
| **Reads** | `HU_PathB_Frame_Acquisition_v<n>.md` §2 |
| **Fails if** | numbers are implausible for the frame — look at the image |

---

### Step 4 — Fetch trait card

| | |
| :--- | :--- |
| **In** | trait name from the video's claim |
| **Out** | cropped handwriting strokes, deck chrome removed |
| **Reads** | `brands/handwriting-university.md` §6 item 2 |
| **Source** | Google Drive `18lfO4P8oJRpcKc_buT7ehjCz0PM6ERx_` — `grapho deck individual cards` |
| **Fails if** | any attempt is made to generate handwriting. **Never generated. Both paths.** |

Read the card's own caption text to confirm it matches the video's claim before using it. Crop to
the strokes; drop the green border, banner, and pointer arrows — deck chrome is not brand.

---

### Step 5 — Composite 16:9

| | |
| :--- | :--- |
| **In** | plate, trait crop, headline, key word |
| **Out** | `yt_v1.jpg` — 1280×720, under 2 MB, readable at 168×94 |
| **Reads** | `brands/handwriting-university.md` §6 for layout; `HU_Thumbnail_Constants_v<n>.md` for logo, fonts, naming |
| **Fails if** | over 2 MB; more than 5 words; bottom-right not clear |

> **16:9 has no locked constant set.** Nobody has measured its margins, padding, or logo
> coordinates. This step is working from prose. See open items.

---

### Step 6 — Self-check the 16:9

**No gate. Step 7 proceeds.** Salvatore reads the 168×94 proof and confirms the headline is
legible at that size, the bottom-right is clear, and the file is under 2 MB. Then continue.

*v1 held here for Bart's approval. The pipeline's single review replaced it — the thumbnail is
seen once, on the private YouTube video, alongside the title, description and captions.*

---

### Step 7 — Acquire host plate, 9:16

**7A — Path A:** regenerate at 9:16 — same references, same wardrobe, same scene. **Do not
upscale, crop, or pad the 16:9.** Reads the Path A creation process, §0.5 Step 2.

**7B — Path B:** grab a 9:16-suitable frame, or pad a landscape frame. Reads
`HU_PathB_Frame_Acquisition_v<n>.md` §3. Sweep the scale and read the clearances — do not eyeball.

---

### Step 8 — Build 9:16

| | |
| :--- | :--- |
| **In** | plate, `hair_y`/`face_y`, headline lines, layout choice |
| **Out** | `ig_v1.jpg` — 1080×1920, JPG 92%+, 300 DPI, RGB |
| **Reads** | `HU_Thumbnail_Constants_v<n>.md` — **the whole file** |
| **Order** | size type → grow paper ×1.10 → tear four edges → taper corners → shadow → parchment → embossed type → logo |

---

### Step 9 — Asserts

| | |
| :--- | :--- |
| **Reads** | `HU_Thumbnail_Constants_v<n>.md` §4, §9 |
| **Checks** | paper on canvas; corners inside margin; `MARGIN > AMP_V`; **lowest tooth clears the forehead** |
| **Prints** | paper box, type sizes, bleed, `lowest tooth N vs forehead N -> CLEAR Npx` |

---

### Step 10 — Name and version the 9:16

**No gate.** Increment `v1` → `v2` → `v3`; **never overwrite**, and **never a status word in the
filename** — no `final`, no `approved`. A file is named for which attempt it is, not for what
someone thinks of it.

*v1 held here for Bart's approval and said only he could name a file approved. The naming rule
survives; the gate does not.*

---

### Step 11 — Close ClickUp

Status must be set to **`Closed`** — the Video Production lists carry only `Open`, `in progress`,
`Closed`. There is no "Done" or "Complete"; passing those strings fails. `Closed` is what releases
the next dependent step.

Task IDs are per-video: list `901818897770` is `_Sample Video JULY Temp`, the template source.
Resolve the task ID inside that video's cloned list. **Never write to the template.**

---

## Where the human actually is now

Salvatore hands off and stops. The thumbnails travel with the video into the publishing pipeline,
and a person sees them **once** — on the private YouTube video and in the Metricool drafts,
alongside everything else. Making the video public and scheduling the drafts is the approval.

A rejected thumbnail re-runs the relevant step alone and swaps on the live video. That is a redo,
not a failure, and it is the trade the single-review model makes deliberately.

**The reviewer is a role, not a person.** Never name an individual as the approver.

---

## Open items

1. **16:9 has no locked constants.** Margins, padding, and logo coordinates for 1280×720 have
   never been measured the way the 9:16 set was. Step 5 is the weakest link in this chain.
2. **Add an explicit path flag to `build_hu_ig_thumbnail.py`** so Step 8 cannot silently run
   Path B logic on a Path A job, or vice versa.
3. **Likeness drift is now caught later, not sooner.** v1 put a human at Step 3A specifically
   because no assert catches an AI-generated host that has stopped looking like Bart. Under the
   single review that judgement happens on the private video instead. Watch for drift over the
   first few batches; if it appears, put a person back on Step 3A rather than weakening the
   single-review model elsewhere.
4. **Retire `SOP_HU_IG_Screenshot_Torn_Paper_v2.md`** once its split is verified, or it becomes a
   third stale source.
5. **`HU_Thumbnail_Constants_v<n>.md` and `HU_Brand_Thumbnail_v<n>_Screenshot_Torn_Parchment.md`
   still say "only Bart names anything approved."** The naming instruction they carry is still
   correct — never a status word in a filename — but the attribution is stale. Fix at their next
   revision rather than spending a version number on one sentence.
