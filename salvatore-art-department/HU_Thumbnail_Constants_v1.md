# HU Thumbnail — Constants & Geometry (shared)

**Version:** 1
**Status:** **PATH-AGNOSTIC.** Applies to Path A (generated host) and Path B (screengrab) identically.
**Extracted from:** `SOP_HU_IG_Screenshot_Torn_Paper_v2.md`, 2026-08-14. Values unchanged.
**Lives at:** `salvatore-art-department/HU_Thumbnail_Constants_v1.md`

> **This file is the numbers.** The narrative files describe intent; this one is what the build
> reads. If a number appears in both, **this file wins** — and the narrative should be corrected
> rather than the number.
>
> Nothing here depends on where the host image came from. Do not fork it per path.

---

## 1. Locked settings — 9:16 (as shipped in `ig_v7`)

```
CANVAS      1080 x 1920
PARCHMENT   #F5F5DC   flat. No grain, no texture, no gradient.  (headline block ONLY - see note)
HU_NAVY     #1D3557   exact
MARGIN      70        # nothing crosses; MUST exceed AMP_V
PAD_X       46        # base, before x1.10
PAD_Y       40        # base, before x1.10
PAPER_GROW  1.10
AMP_H       70        # top; bottom = x1.2
AMP_V       42        # sides
TAPER       60
top_air     70        # 20 when headroom is tight
shadow      offset +16/+18, alpha 130, blur 26
mask blur   0.8
emboss      navy text: (190,182,150) at +3/+4 behind
LOGO_W      444       # 3x
LOGO_PAD    (-64, -99)
```

> **Scope of the flat-fill rule.** "No grain, no texture, no gradient" governs the **headline
> parchment block** that the build draws. It does **not** govern trait graphics. Approved trait
> samples from the published library — including the pre-composited Y-chart PNGs such as
> `no-trust-paper.png` — are set on real aged paper and are visibly textured. That is correct and
> approved. **Do not reject a library asset for having paper texture, and do not flatten it.**

### Machine-readable

```json
{
  "canvas": { "w": 1080, "h": 1920 },
  "color": { "parchment": "#F5F5DC", "hu_navy": "#1D3557", "emboss_rgb": [190, 182, 150] },
  "margin": 70,
  "pad": { "x": 46, "y": 40 },
  "paper_grow": 1.10,
  "amp": { "h_top": 70, "h_bottom_mult": 1.2, "v_sides": 42 },
  "taper": 60,
  "top_air": { "default": 70, "tight": 20 },
  "shadow": { "offset": [16, 18], "alpha": 130, "blur": 26, "mask_blur": 0.8 },
  "emboss_offset": [3, 4],
  "logo": { "w": 444, "pad": [-64, -99] }
}
```

---

## 2. The tear — fractal value noise, three octaves

**Never a sawtooth.** A fixed step (`step = W/n`) makes every tooth the same width and reads as a
saw blade. Rejected repeatedly. Do not resurrect it.

| Octave | Horizontal edges | **Vertical edges** | Weight |
| --- | --- | --- | --- |
| 1 — slow wander | 420 px | **240 px** | 0.55 |
| 2 — bites | 90 px | **64 px** | 0.38 |
| 3 — fibre | 11 px | **9 px** | 0.10 |

**Vertical edges are shorter, so their wavelengths are tightened.** Reusing the horizontal
numbers on the sides produces stretched teeth. This is the single most commonly dropped detail
in the narrative files.

Amplitude: **70px top, ×1.2 bottom, 42px sides.**

Bart tested four variants and rejected deep gaussian bites and fibre fringe. **Plain
three-octave noise is the approved look. Do not embellish it.**

**All four edges torn.** An inset paper with straight sides reads as a cut rectangle.

**Corners:** taper the noise to zero over ~60px at each end of every edge. Untapered noise
wanders the corner off its mark.

**Assert `MARGIN > AMP_V`** (70 > 42) or the side tear pushes the paper off-canvas.

---

## 3. Paper sizing — the paper serves the text

`PARCH_BOT = 0.415 * H` is **dead.** It left two-thirds of the paper as empty cream on short titles.

```
paper half-width  = (text_block_width  / 2 + PAD_X) × 1.10
paper half-height = (text_block_height / 2 + PAD_Y) × 1.10
```

**Order matters.** Size the type *first* against base padding, **then** grow the paper around it
and re-centre the text. If the growth feeds back into the font fit, the headline shrinks instead
of gaining breathing room — the opposite of the intent.

### Per-line emphasis

Lines may be sized independently — `("VANITY", 3.0)` sets the trait word at 3×.

- Base size = largest that fits **every unemphasised line**, so emphasis doesn't drag the others down.
- Guard: an emphasised line must never overflow the paper width. Shrink it if it does.

### Type width ceiling

At `MARGIN 70 + AMP_V 42 + PAD_X 46` per side, only **764px** is available for type. A
5-character word tops out near **230pt**. Asking for "3×" on a short word is usually impossible —
the letters hit the margin first. **Do not narrow the margin to chase it**; that breaks the
corner rule.

**The paper follows the type.** Doubling the type roughly triples the paper. Paper height and
type size cannot be specified independently.

---

## 4. Clearance — the formula that matters

The bottom tear reaches:

```
lowest_tooth = PARCH_BOT + (AMP_H * 1.2)
```

**Test that number against the forehead — not the paper edge, and not the hairline.** A deep
tooth is what lands on his eyes.

- **Face is untouchable.** Never covered, never cropped.
- **Hair may be covered.** Bart approved this explicitly.

*How hair and face positions are obtained differs by path: Path A specifies composition, Path B
detects it. The clearance test itself is identical on both.*

---

## 5. Measured evidence — why the rules are the rules

Keep these. They are the proof, and without them the rules read as arbitrary and get "improved."

### The white setup line COSTS headroom

Measured on *"Vanity / Nobody Likes Him, Everyone Respects Him"*:

```
VANITY white + 2 on paper, air 70   -> HITS HAIR 115px
all 3 on paper, air 70              -> HITS HAIR  25px
VANITY white + 2 on paper, air 20   -> HITS HAIR  65px
all 3 on paper, air 20              -> CLEAR      25px   <- shipped
```

The white line spends ~200px before the paper even starts. On a 437px band that is fatal.
**Long titles can least afford the setup line.** Test before choosing.

---

## 6. Text distribution — judgment, not rule

There is **no rule** that line 1 is white above and line 2 is navy on the paper. Bart was explicit.

**Three approved layouts. Choose by title length. None is the default.**

| Option | Reference | Use | Type | Paper |
| :--- | :--- | :--- | :--- | :--- |
| **A** — all text on paper, equal weight | `true-optimists-write-like-this/ig_v6.jpg` — *"very very good"* | Mid-length titles | ~78pt | ~258px |
| **B** — trait word emphasised | `vanity-nobody-likes-him/ig_v7.jpg` — *"pretty darn good"* | Title = trait label + payoff | `[156, 52, 52]pt` | ~379px |
| **C** — stacked hero type | `liar-liar/ig_v2.jpg` — *"This is excellent."* | Very short, punchy titles | `[230, 230]pt` | **590px** |

**When splitting, the paper carries the PUNCH** — not merely the back half of the sentence.
*"STUBBORN. The Fear of Being Wrong."* → setup `THE FEAR OF BEING WRONG`, paper `STUBBORN`.
Reorder if the payoff should land last.

Option C example call:

```python
build(PHOTO, out, ["LIAR !", "LIAR!"], line1=None,
      top_air=70, face_cx_src=759, manual_scale=1.30)
```

---

## 7. The HU logo — locked position (Bart, 2026-07-17)

| Property | Locked value |
| --- | --- |
| File | `HU_logo_new_2026_Watermark.png` — **used unaltered** *(underscores; renamed 2026-08-10)* |
| Scale | 3× the old 148px spec → paste box **444px wide** |
| Visible mark | **~292px wide**, ~202px tall |
| Position | **Bottom-left.** Mark occupies **x 21–313, y 1672–1874** |
| Margins | **21px from left, 46px from bottom** |
| Paste box | `(-64, -99)` from bottom-left, i.e. box origin (-64, 1575) |

**Record the MARK position, not the box.** Box coordinates are only meaningful while the PNG
carries its transparent padding. The mark position survives a re-export.

### Why the box hangs off-canvas

The PNG is a 720×720 canvas with the mark occupying only 475×328. At 3× that is **85px padding
left, 97px top, 66px right, 144px bottom**. The padding, not the mark, hits the canvas edge
first. To move the mark down at all, the box must overhang.

**Consequence:** "move it down 1 inch" (300px @ 300dpi) is **impossible** — the mark has only
191px of travel before the quill is amputated. Max is ~0.48in. More would require cropping the
padding, which means altering the asset.

### Two known asset defects — accepted by Bart, not fixed

1. **The counters are opaque white.** Transparency covers only the outer background. The enclosed
   space inside the U and the gaps in the H are **solid white** — 22.6% of the mark is opaque
   white; inside the U bowl alone, 6,275 white pixels. On dark clothing these read as white
   patches. **Bart: "It is acceptable."** Do not "fix" it without asking.
2. **`hu_brand_logo.jpg` is worse** — flattened, entire background opaque white. Fallback only.
   **Neither logo file is genuinely transparent.**

### Contrast — measure it

On the reference frame the logo is invisible on the sweater:

```
logo ink luminance   111.8
backdrop luminance   112.1     <- a gap of 0.3
```

**No file swap fixes this** — it is a contrast problem, not a format problem. Bart accepted it
there. If a future plate makes it unreadable, the options are a torn parchment chip behind the
mark, a soft dark halo, or a white knockout — **ask, don't choose.**

### Platform safe zones (2026-08-09)

Instagram Reels and TikTok overlay captions and an action rail across the **bottom**, a button
rail up the **right**, and IG crops the profile-grid tile to a centred 4:5 slice. The logo is
**lifted above the reserved bottom band**. The build reports when the paper or a tear tooth
crosses a safe zone.

**Not measured for YouTube Shorts.** Verify on a phone before publishing.

---

## 8. Fonts

Georgia Bold and Impact are proprietary. **On the Mac use the real ones:**
`/System/Library/Fonts/Supplemental/Georgia Bold.ttf` and `.../Impact.ttf`

In a Linux container they don't exist. Metric-holding substitutes:

- **Gelasio Bold** → metric-compatible Georgia Bold
  `https://raw.githubusercontent.com/SorkinType/Gelasio/master/fonts/ttf/Gelasio-Bold.ttf`
- **Anton** → closest open Impact
  `https://raw.githubusercontent.com/google/fonts/main/ofl/anton/Anton-Regular.ttf`

**The approved builds used the substitutes.** Rebuilding on the Mac with the real fonts **will
shift the type** — expect it and re-check the fit.

---

## 9. Build asserts — assert, don't eyeball

```python
assert min(xs) > 0 and max(xs) < W          # paper never leaves the canvas
assert min(ys) > 0 and max(ys) < H
assert X0 >= MARGIN and X1 <= W - MARGIN    # corners inside margin
assert MARGIN > AMP_V                       # side tear stays on canvas
```

Print every build:

```
paper x 70-1009  y 90-469 (h=379)  sizes [156, 52, 52]pt  bleed L67 R56
lowest tooth 518  vs forehead 635  -> CLEAR 117px
```

---

## 10. Copy is set EXACTLY as Bart writes it

The reference build reads `LIAR !` on line one (space before the bang) and `LIAR!` on line two.
**That is how he typed it.** It was flagged to him and left alone.

**Never tidy, normalise, correct, or re-punctuate Bart's headline copy.** Flag it and ship what
he wrote.

> This rule is not thumbnail-specific and should arguably live in the brand kit. Flagged.

---

## 11. File naming

`ig_v1.jpg`, `ig_v2.jpg`, `yt_v1.jpg` — in the video's slug folder. Increment, never overwrite,
**never a status word** (`final`, `approved`). Only Bart approves, so only Bart names anything
approved.

---

## 12. 16:9 differences

These constants are the 9:16 build. The 16:9 YouTube thumbnail differs on three points, per
`/brands/handwriting-university.md` §6:

| | 9:16 (this file) | 16:9 |
| :--- | :--- | :--- |
| Canvas | 1080 × 1920 | 1280 × 720, under 2 MB |
| Parchment edges | Always torn, all four | Torn **or** scissor-cut, per the space the text needs |
| Red | None | Teacher Red `#D62828` for the trait circle |

**16:9 has no equivalent locked constant set.** Nobody has measured its margins, padding, or
logo coordinates. Until someone does, 16:9 builds are working from prose. Flagged as an open item.
