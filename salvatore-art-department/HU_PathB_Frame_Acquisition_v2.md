# HU Thumbnail — Path B: Frame Acquisition (screengrab)

**Version:** v2 — matches the filename. Highest number is current.
**Last updated:** 2026-09-12
**Status:** **PATH B ONLY. NOT THE DEFAULT.** Opt-in, by Bart's explicit election per video.
**Default path:** Path A, generated host — `HU_Thumbnail_PathA_Generated_Host_v<n>.md`
**Shared constants:** `HU_Thumbnail_Constants_v<n>.md` — applies to both paths, do not fork
**Extracted from:** `SOP_HU_IG_Screenshot_Torn_Paper_v2.md` §2 and §10, 2026-08-14. Values unchanged.

> **Scope.** This file covers **only** how a real video frame becomes a usable host plate.
> Everything after that — tear, paper sizing, type, logo, asserts — is in
> `HU_Thumbnail_Constants_v<n>.md` and is identical on both paths.
>
> **An agent never elects Path B.** Absence of instruction means Path A.
>
> **Versioning:** the version is in the filename and the highest number wins. A new revision
> becomes `..._v3.md` and this file is deleted in the same commit. Cross-references never name an
> exact version — `Something_v<n>.md` means the highest-numbered one in that folder.
>
> **What changed in v2:** two dead pointers only. v1 routed to
> `HU_Thumbnail_Creation_Process_v5.md`, which is retired, and to
> `HU_Thumbnail_Constants_v1.md`, which has been replaced. Every measurement below is unchanged.

---

## 1. Choose the frame FIRST — it decides everything

No geometry rescues a bad grab.

**Headroom is mandatory.** Bart must sit low enough that the paper has quiet dead space above his
hair. A tight 16:9 close-up where his head fills the frame **cannot work** — filling a 9:16 canvas
from it drives his forehead under the paper. This failed four times before a proper frame was used.

**Prefer an already-vertical grab.** Reference:
`IG_bart_leaning_in_to_camera_green_sweater_full.png` (639×1200, Bart in the lower two-thirds,
dark headliner above).

**Vertical crop is TOP-ANCHORED.** Centring eats the headroom you just gained.

Quiet dead space — headliner, dark wall, sky. Engaged expression, mid-sentence.

**Reject early.** A bad grab discovered at compositing time has already cost the build.

---

## 2. Detect hair and face separately — don't eyeball

They are different limits:

- **Face is untouchable.** Never covered, never cropped.
- **Hair may be covered.** Bart approved this explicitly.

In the reference frame: hair tips at **y=437**, skin starts at **y=635**. That is ~198px of hair
the paper may eat.

```python
# hair: first row departing from the flat dark headliner
# face: first row with a real run of skin-tone pixels
skin = (R>95)&(G>40)&(B>20)&(R>G+15)&(G>B)&((R-B)>15)
```

Then apply the clearance test from `HU_Thumbnail_Constants_v<n>.md` §4 — lowest tooth versus
**forehead**, not paper edge, not hairline.

> **This detection step is the difference between the paths.** Path A specifies composition in the
> prompt and the build merely verifies it. Path B has to find it in a frame nobody designed.
> Treat a detection result as a measurement to be checked: if the numbers look implausible for the
> frame, they are wrong — look at the image.

---

## 3. Landscape frames — pad, don't reject

**This amends §1.** A 16:9 frame is not an automatic reject. Scale-to-fill is what fails, not the
frame — it drives Bart's head under the paper.

**Reference build:** `liar-liar/ig_v2.jpg` — Bart: *"This is excellent."*

### Method (`manual_scale` in `build_hu_ig_thumbnail.py`)

1. Scale the frame by a **chosen factor** — *not* `max(W/bw, H/bh)`.
2. Crop horizontally on the face (`face_cx_src`).
3. **Bottom-align**, so his body reaches the canvas edge.
4. Fill the gap above by extending the top of the frame upward.

### The fill must not be a flat block

Sample the **top 6 rows**, then walk a darkening gradient (78% → 100%) with light grain. A
headliner darkens away from the glass; a flat fill bands visibly.

```python
band = np.array(crop.crop((0, 0, W, 6))).astype(float).mean(axis=0)
for r in range(pad):
    k = 0.78 + 0.22 * (r / pad)
    row = band * k + rng.normal(0, 1.6, band.shape)
```

### Only works on quiet dead space — CHECK FIRST

Measure the std of the top rows of the **cropped** region before trusting it. The reference frame
gave mean RGB 18/29/35 with **std ≈5** — near-uniform, so the extension is invisible. On a busy
top edge it will look obviously faked. **If std is high, reject the frame.**

### Scale is a clearance decision, not an aesthetic one

Bigger scale = bigger Bart = less headroom. Measured on `bart_green_sweater_serious.png` with the
stacked LIAR type:

```
scale 1.50 -> tooth 779, face 734  -> ON FACE by 45px
scale 1.40 -> covers hair 85px, face clear only 33px
scale 1.30 -> fully clear, 4px above hair          <- shipped
scale 1.25 -> fully clear, 47px above hair
```

**Sweep the scale and read the clearances. Do not eyeball it.** Pick the largest scale that still
clears the forehead with margin.

> **Path B only.** This technique exists because a screengrab is the only frame available. On
> Path A, generate at the target aspect ratio instead — the Path A creation process §0.5 Step 2
> forbids padding a landscape plate into a vertical canvas.

---

## 4. Known-bad guidance in the retired July SOP

Carried forward so nobody reintroduces it from an old copy.

| Old SOP says | Reality |
| --- | --- |
| Line 2 is Gold `#C9A84C` | Navy `#1D3557` on parchment |
| Parchment covers top 40%, full-bleed | Paper is inset and sized to its text |
| "no tearing on the left or right sides" | All four edges are torn |
| White Impact setup line always | Not a rule — judgment call per title |
| Output `ig_reel_A_final.jpg` | Violates the File Naming Rule. Never "final". |
| SOP lives in `betty/` | It's in the art department folder |
| Reference at `betty/thumbnails/batch/...` | That folder does not exist |
| Logo at `betty/HU logo new 2026 Watermark.png` | `salvatore-art-department/HU_logo_new_2026_Watermark.png` — underscores |

---

## 5. What Path B does NOT change

For the avoidance of doubt, these are identical on both paths and are **not** restated here:

- Every constant in `HU_Thumbnail_Constants_v<n>.md` §1
- The tear — octaves, wavelengths, amplitudes, taper
- Paper sizing, the ×1.10 grow, the three layouts, per-line emphasis
- Type width ceiling, fonts and substitutes
- Logo position, scale, the two accepted asset defects, safe zones
- The clearance formula and the build asserts
- Copy set exactly as Bart writes it
- File naming
- **Trait handwriting is never generated** — published library only, brand kit §6 item 2

---

## 6. Open items

1. **Gate the code, don't delete it.** `build_hu_ig_thumbnail.py` contains frame-grab, skin
   detection, and `manual_scale` padding. Under two live paths this is **Path B code, not dead
   code.** Earlier guidance said to strip it — that was wrong. Gate it behind an explicit path
   flag.
2. **`IG_bart_leaning_in_to_camera_green_sweater_full.png` and `bart_green_sweater_serious.png`
   are cited here but are not in the repo.** They are the reference frames behind the measured
   numbers in §2 and §3. Without them those numbers can't be reproduced.
3. **Retire `SOP_HU_IG_Screenshot_Torn_Paper_v2.md`.** Its content is now split between
   `HU_Thumbnail_Constants_v<n>.md` (most of it) and this file (§2, §10). Leaving the original in
   place gives agents a third, stale source.
