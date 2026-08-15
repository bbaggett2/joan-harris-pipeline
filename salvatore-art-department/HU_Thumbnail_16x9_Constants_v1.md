# HU Thumbnail — 16:9 Constants & Build (YouTube)

**Version:** 1
**Scope:** YouTube thumbnail, 1280 × 720. **16:9 only.**
**Build:** `salvatore-art-department/build_hu_yt_thumbnail.py`
**Companion:** `HU_Thumbnail_Constants_v1.md` is the **9:16** set. Different canvas, different
numbers. Do not mix them.
**Layout authority:** `brands/handwriting-university.md` §6.

---

## 0. Why this file exists

Until 2026-08-14 there was **no 16:9 build path.** `build_hu_ig_thumbnail.py` hardcodes
`W, H = 1080, 1920` at line 21, has no `argparse`, no `__main__`, and no `--format` flag. The
Pass 2 command line printed in earlier SOPs — `--input / --headline / --subhead / --format 16x9` —
described an interface that did not exist. It was carried forward from document to document
without ever being run.

`build_hu_yt_thumbnail.py` is a **new, separate script** for 16:9. The 9:16 script is untouched.

**Provenance of the numbers below.** The 9:16 constants were measured against approved builds over
weeks. These were derived on 2026-08-14 from the §6 layout spec plus the 168×94 legibility floor,
then tuned across seven test renders against a real Gemini plate. They are **working values, not
battle-tested ones.** Expect to adjust after the first few approved thumbnails, and update this
file when you do.

---

## 1. Locked settings

```
CANVAS            1280 x 720
MARGIN            44        # nothing crosses
LEFT_COL_W        540       # headline + key word + trait live here
RIGHT_KEEPOUT_X   760       # host zone; never composite left-column art past this
TIMESTAMP_KEEPOUT (1080, 630, 1280, 720)   # YouTube duration stamp

HEAD_MAX_PT       82        # auto-fits down to HEAD_MIN_PT
HEAD_MIN_PT       44
HEAD_TOP          40
HEAD_LINE_GAP     8
HEAD_STROKE       3         # silver edge
HEAD_SHADOW       (4, 5)    # black 150 alpha, for busy plates

KEY_MAX_PT        92
KEY_MIN_PT        40
PARCH_TILT        -3.0 deg
PARCH_PAD_X       34
PARCH_PAD_Y       20
PARCH_GROW        1.10      # same 10% breathing room as the 9:16 build
PARCH_SHADOW      offset (10,12), blur 16, alpha 130
EMBOSS_OFF        (3, 4)

TRAIT_MAX_W       430
TRAIT_MAX_H       300
TRAIT_GAP         22        # below the parchment block
TRAIT_LOGO_CLEAR  104       # vertical room reserved for the logo
CIRCLE_W          7
CIRCLE_PAD        22
CIRCLE_MIN_RATIO  0.62      # keeps a narrow letterform from getting a thin oval

LOGO_MARK_W       132       # VISIBLE mark width, not the padded box
LOGO_LEFT         44
LOGO_BOTTOM       30

MAX_BYTES         2 MB
```

### Palette

| Role | Hex |
| :--- | :--- |
| Headline | White `#FFFFFF`, silver `#C0C0C0` edge |
| Key word | HU Navy `#1D3557` on parchment `#F5F5DC` |
| Emboss | Warm tan `#BEB696` |
| Trait circle | Teacher Red `#D62828` — **16:9 only. No red on 9:16.** |

---

## 2. Layout

Left column carries headline → key word on tilted parchment → trait graphic → logo, stacked.
Host occupies the right ~40% and comes from the plate; nothing is composited over it.

```
 x=44                          x=540      x=760 ────────────── host zone
 ┌────────────────────────────────┐        │
 │ HEADLINE            (white)    │        │
 │ ▔▔▔▔▔▔▔▔▔▔                     │        │
 │ ┌──────────────────┐           │        │      (Gemini plate)
 │ │ KEY WORD (navy)  │  tilted   │        │
 │ └──────────────────┘  parchment│        │
 │   ⭘ trait, red circle          │        │
 │  [HU]                          │        │  ← bottom-right stays
 └────────────────────────────────┘        │     clear: timestamp
```

**Vertical budget is finite.** Headline, key word, trait, and logo compete for 720px. A long
headline starves the trait. The script fits the trait to whatever space remains and **exits with
an error** if under 90px is left — that is a signal to shorten the headline, not to shrink the
margins.

---

## 3. Two failure modes found during the build

**Parchment must be measured by its visible alpha, not its canvas.** The block is drawn on a
padded transparent surface and then rotated, which expands it further. Measuring the canvas puts
the trait ~60px too high, overlapping the key word. Use the alpha bounding box.

**Auto-trim is opt-in and unreliable on photographed paper.** `--trim` crops a trait graphic to
its densest ink cluster. That works on clean-background GraphoDeck cards. It **fails** on samples
photographed on real paper: `no-trust-paper.png` has a fold crease running its full height that
out-densities the letterform, so the crop lands on the crease. Verified 2026-08-14. Crop those by
hand and pass the result without `--trim`.

---

## 4. Asserts — the build refuses rather than ships

```
logo mark inside the left margin and on canvas
trait circle stays left of RIGHT_KEEPOUT_X (host zone)
trait circle does not overlap the parchment block
trait circle does not collide with the logo mark
logo does not intrude on the timestamp keepout
headline wraps to at most 3 lines
headline + key word is at most 5 words total
output under 2 MB
```

Every run also writes a **168 × 94 proof image** beside the output. Read it before approving —
that is the size the thumbnail is actually judged at.

---

## 5. Usage

```bash
python3 build_hu_yt_thumbnail.py \
  --plate    outputs/0814-raw-16x9.png \
  --trait    assets/y-no-trust-cropped.png \
  --logo     HU_logo_new_2026_Watermark.png \
  --font     Gelasio-Bold.ttf \
  --headline "DOESN'T TRUST" \
  --keyword  "ANYONE" \
  --out      outputs/0814-yt_v1.jpg
```

| Flag | Notes |
| :--- | :--- |
| `--plate` | Pass 1 Gemini output. Host and scene only. Scale-to-fill, centre-crop. |
| `--trait` | From the approved library. **Never generated.** |
| `--font` | `/System/Library/Fonts/Supplemental/Georgia Bold.ttf` on the Mac; `Gelasio-Bold.ttf` off-Mac. Metrics shift between them — re-check the fit. |
| `--edge` | `cut` (default) or `torn`. §6 permits either on 16:9, by the space the text needs. 9:16 is always torn. |
| `--trim` | Opt-in. See §3. |

Filenames: `yt_v1.jpg`, `yt_v2.jpg` — never a status word. Only Bart names anything approved.

---

## 6. Open items

1. **These constants are provisional.** Derived and tuned in one session, not measured against a
   body of approved work. Revisit after the first few approvals.
2. **No approved 16:9 reference build exists in the repo.** There is nothing to compare output
   against. The first approved thumbnail should be committed as the reference.
3. **The silver edge is a stroke, not a gradient.** §4 of the brand kit calls for a "metallic-silver
   edge"; this is a flat `#C0C0C0` outline. Good enough at 168×94, arguably not at full size.
4. **`generate_thumbnail.py` (Pass 1) is Mac-only**, at `skills_to_install/youtube-thumbnail/scripts/`.
   Not in the repo, so a clean clone cannot run Pass 1.
