# HU Thumbnail — Step Map for n8n

**Version:** 1
**Purpose:** one row per callable step. Each row names its inputs, its output, and **the one
document it reads.** A step that has to read three files to know what to do is a step that will
drift.
**Lives at:** `salvatore-art-department/HU_Thumbnail_Step_Map_v1.md`

---

## Document routing — read this first

| Document | Scope | Who reads it |
| :--- | :--- | :--- |
| `brands/handwriting-university.md` §6 | 16:9 layout | Steps 4, 6 |
| `HU_Thumbnail_Creation_Process_v5.md` | **Path A**, generated host | Steps 2, 3 |
| `HU_PathB_Frame_Acquisition_v1.md` | **Path B**, screengrab | Steps 2B, 3B |
| `HU_Thumbnail_Constants_v1.md` | **Both paths.** Numbers, geometry, logo, fonts, asserts | Steps 5, 7, 8, 9 |
| `HU_Brand_Thumbnail_v2_Screenshot_Torn_Parchment.md` | Path routing rules | Step 1 |

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
| **Reads** | `HU_Brand_Thumbnail_v2_Screenshot_Torn_Parchment.md` |
| **Fails if** | anything other than an explicit written election tries to set `B` |

Default to `A`. This step exists so no later step has to decide.

---

### Step 2 — Acquire host plate, 16:9

**2A — Path A**

| | |
| :--- | :--- |
| **In** | transcript, emotional register, reference image set |
| **Out** | 16:9 host plate — host and scene only, no text, no handwriting, no logo |
| **Reads** | v5 §6 |
| **Fails if** | the plate contains handwriting, headline, parchment, or logo |

**2B — Path B**

| | |
| :--- | :--- |
| **In** | source video |
| **Out** | 16:9 frame, headroom verified |
| **Reads** | `HU_PathB_Frame_Acquisition_v1.md` §1 |
| **Fails if** | no frame has quiet dead space above the hair — reject early, do not proceed |

---

### Step 3 — Verify host

**3A — Path A: likeness recognition**

| | |
| :--- | :--- |
| **In** | new plate, last two approved thumbnails |
| **Out** | pass / regenerate |
| **Reads** | v5 §6.2 |
| **Note** | **Human step. Bart's eye.** The question is "is this the same man," not "is this a good image." No assert substitutes for it. |

**3B — Path B: hair and face detection**

| | |
| :--- | :--- |
| **In** | frame |
| **Out** | `hair_y`, `face_y` |
| **Reads** | `HU_PathB_Frame_Acquisition_v1.md` §2 |
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
| **Reads** | `brands/handwriting-university.md` §6 for layout; `HU_Thumbnail_Constants_v1.md` for logo, fonts, naming |
| **Fails if** | over 2 MB; more than 5 words; bottom-right not clear |

> **16:9 has no locked constant set.** Nobody has measured its margins, padding, or logo
> coordinates. This step is working from prose. See open items.

---

### Step 6 — Bart approves 16:9

**Human gate. Nothing proceeds without it.** Step 7 does not start.

---

### Step 7 — Acquire host plate, 9:16

**7A — Path A:** regenerate at 9:16 — same references, same wardrobe, same scene. **Do not
upscale, crop, or pad the 16:9.** Reads v5 §0.5 Step 2.

**7B — Path B:** grab a 9:16-suitable frame, or pad a landscape frame. Reads
`HU_PathB_Frame_Acquisition_v1.md` §3. Sweep the scale and read the clearances — do not eyeball.

---

### Step 8 — Build 9:16

| | |
| :--- | :--- |
| **In** | plate, `hair_y`/`face_y`, headline lines, layout choice |
| **Out** | `ig_v1.jpg` — 1080×1920, JPG 92%+, 300 DPI, RGB |
| **Reads** | `HU_Thumbnail_Constants_v1.md` — **the whole file** |
| **Order** | size type → grow paper ×1.10 → tear four edges → taper corners → shadow → parchment → embossed type → logo |

---

### Step 9 — Asserts

| | |
| :--- | :--- |
| **Reads** | `HU_Thumbnail_Constants_v1.md` §4, §9 |
| **Checks** | paper on canvas; corners inside margin; `MARGIN > AMP_V`; **lowest tooth clears the forehead** |
| **Prints** | paper box, type sizes, bleed, `lowest tooth N vs forehead N -> CLEAR Npx` |

---

### Step 10 — Bart approves 9:16

**Human gate.** Only Bart names anything approved. Increment `v1` → `v2`; never overwrite, never a
status word in the filename.

---

### Step 11 — Close ClickUp

Status must be set to **`Closed`** — the Video Production lists carry only `Open`, `in progress`,
`Closed`. There is no "Done" or "Complete"; passing those strings fails. `Closed` is what releases
the next dependent step.

Task IDs are per-video: list `901818897770` is `_Sample Video JULY Temp`, the template source.
Resolve the task ID inside that video's cloned list. **Never write to the template.**

---

## Open items

1. **16:9 has no locked constants.** Margins, padding, and logo coordinates for 1280×720 have
   never been measured the way the 9:16 set was. Step 5 is the weakest link in this chain.
2. **Add an explicit path flag to `build_hu_ig_thumbnail.py`** so Step 8 cannot silently run
   Path B logic on a Path A job, or vice versa.
3. **Steps 3A, 6 and 10 are human.** n8n should hold, not poll — an automated approval defeats
   the only check that catches likeness drift.
4. **Retire `SOP_HU_IG_Screenshot_Torn_Paper_v2.md`** once its split is verified, or it becomes a
   third stale source.
