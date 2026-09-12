# HU Thumbnail — 16:9 Constants & Build (YouTube)

**Version:** v2 — matches the filename. Highest number is current.
**Last updated:** 2026-09-12
**Scope:** YouTube thumbnail, 1280 × 720. **16:9 only.**
**Build:** `salvatore-art-department/build_hu_yt_thumbnail.py`
**Companion:** `HU_Thumbnail_Constants_v<n>.md` is the **9:16** set. Different canvas, different
numbers. Do not mix them.
**Layout authority:** `brands/handwriting-university.md` §6.

> **Versioning:** the version is in the filename and the highest number wins. A new revision
> becomes `..._v3.md` and this file is deleted in the same commit. Cross-references never name an
> exact version — `Something_v<n>.md` means the highest-numbered one in that folder.
>
> **What changed in v2:** the filename said `v1` while the header said `1.1`; the companion
> pointer named a file that is being deleted; and §5 attributed approval to a named person. **No
> constant, assert, flag or measurement changed.** The 1.1 content — fonts named and enforced in
> §1, the corrected assert list in §4, §5 rewritten against the shipped CLI — is all still here.

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

> ⚠️ **This file contradicts two others, and this file is right.** The 9:16 constants §12 and the
> thumbnail step map both say *"16:9 has no equivalent locked constant set — nobody has measured
> its margins, padding, or logo coordinates."* That was true before 2026-08-14 and is not true
> now: the set is below. What is accurate is that these numbers are **provisional** — tuned in one
> session rather than proven across approved work. Correct those two files at their next revision.

---

## 1. Locked settings

```
CANVAS            1280 x 720
MARGIN            44        # nothing crosses
LEFT_COL_W        540       # headline + key word + trait live here
RIGHT_KEEPOUT_X   760       # host zone; never composite left-column art past this
TIMESTAMP_KEEPOUT (1080, 630, 1280, 720)   # YouTube duration stamp

FONT_HEAD_FILL    CollegiateFLF.ttf          # drawn first, filled white
FONT_HEAD_OUTLINE CollegiateOutlineFLF.ttf   # laid over it, HU Navy
FONT_KEY          CollegiateFLF.ttf          # navy, on the parchment
                  # ~/Library/Fonts/. NO SUBSTITUTES -- the build refuses.
                  # Impact / Anton / Georgia / Gelasio are retired. Brand kit 4.

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
FONT  headline / fill / key-word faces are CollegiateFLF or CollegiateOutlineFLF
      -- checked before any file is opened; refuses by name and says which face
      is retired. Section 1.

LOGO  bottom-left: mark inside the left margin
      top-right:   mark inside the right and top margins
      either:      mark on canvas
      does not intersect the TIMESTAMP_KEEPOUT rectangle

TRAIT circle stays left of RIGHT_KEEPOUT_X (host zone)
      circle does not overhang the left margin, and is on canvas
      circle does not cross the bottom margin
      circle does not overlap the parchment block
      circle does not collide with the logo mark  (bottom-left only)
      at least 90px of vertical budget remains -- otherwise the build exits and
      tells you to shorten the headline. Do NOT respond by shrinking margins.

TEXT  headline wraps to at most 3 lines
      headline + key word is at most 5 words TOTAL, counted by whitespace
      (so "THIS Y-LOOP REVEALS" + "TRUST ISSUES" = 5, and passes)

FILE  output under 2 MB
```

> **Three assert bugs were found and fixed on 2026-08-15.** The timestamp check compared x only
> and used `mark[1] > H`, which can never be true — so any logo past x=1080 tripped a keepout that
> lives at the *bottom* right, and a legal top-right logo was rejected. It is now a real rectangle
> intersection. The logo-margin assert assumed bottom-left. And there was no left-margin assert on
> the trait circle at all. If you are reading an older copy of this file, it lists none of these.

Every run also writes a **168 × 94 proof image** beside the output. **Read it before handing
off** — that is the size the thumbnail is actually judged at.

---

## 5. Usage

```bash
python3 build_hu_yt_thumbnail.py \
  --plate     outputs/0814-raw-16x9-dark.png \
  --trait     assets/y-no-trust-cropped.png \
  --logo      HU_logo_new_2026_Watermark.png \
  --headline  "THIS Y-LOOP REVEALS" \
  --keyword   "TRUST ISSUES" \
  --logo-pos  top-right \
  --tilt      0 \
  --parch-pad-x 30 --parch-pad-y 26 --key-max-pt 62 \
  --out       outputs/0814-yt_v1.jpg
```

**The three font flags are not in that command on purpose** — they now default to the approved
Collegiate faces, so a bare invocation is already compliant. Pass them only to be explicit.

| Flag | Notes |
| :--- | :--- |
| `--plate` | Pass 1 Gemini output. Host and scene only. Scale-to-fill, centre-crop. |
| `--trait` | From the approved library. **Never generated.** |
| `--headline-font` | `~/Library/Fonts/CollegiateOutlineFLF.ttf`. **Enforced** — the build exits if it is anything else. |
| `--headline-fill-font` | `~/Library/Fonts/CollegiateFLF.ttf`. Drawn white beneath the outline so the letters have a body. Omit it and the headline is hollow and illegible at 168×94. |
| `--keyword-font` | `~/Library/Fonts/CollegiateFLF.ttf`. **Enforced.** |
| `--logo-pos` | `bottom-left` or `top-right`. Top-right returns ~104px of vertical budget to the trait graphic. |
| `--font` | Legacy fallback only. Nothing in an HU build should rely on it. |
| `--headline-outline-color` | `navy` (default), `silver`, or `black`. Navy on a near-black plate is dark-on-dark — `silver` lifts it if the outline softens on a phone. |
| `--tilt` | Parchment tilt in degrees. Default `-3.0`. **The approved reference builds are untilted — pass `0`.** |
| `--parch-pad-x` / `--parch-pad-y` | Parchment padding. Defaults 34 / 20. **Collegiate needs more vertical padding than Georgia — use ~26 for `pad-y`** or the glyph bottoms spill past the cream and vanish against a dark plate. |
| `--key-max-pt` | Caps the key-word size. Default 92. The parchment sizes to the type and the trait gets what is left, so a large key word starves the trait. ~62 is a good balance on a 3-line headline. |
| `--edge` | `cut` (default) or `torn`. §6 permits either on 16:9, by the space the text needs. 9:16 is always torn. |
| `--trim` | Opt-in. See §3. |

Filenames: `yt_v1.jpg`, `yt_v2.jpg` — incrementing, **never a status word**. A file is named for
which attempt it is, not for what anyone thinks of it.

*v1 said "only Bart names anything approved." The approver is now a role rather than a person, and
under the single review nothing is marked approved in a filename at all — approval is the reviewer
making the YouTube video public and scheduling the Metricool drafts.*

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
5. **Two files still say 16:9 has no constants.** The 9:16 constants §12 and the thumbnail step
   map (§5 note and open item 1) both claim nobody has measured 16:9 margins, padding or logo
   coordinates. This file is that measurement. Correct both at their next revision — the accurate
   statement is "provisional, not unmeasured."
