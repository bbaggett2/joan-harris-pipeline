# SOP — HU Instagram Reel Cover: Screenshot + Torn Paper (v2)

**Owner:** Salvadore (art department)
**Status:** ACTIVE — locked by Bart 2026-07-17
**Applies to:** HU Instagram Reel covers, 1080×1920, built from real video frames

**Supersedes:**
- "LOCKED STYLE 2" in `Instagram_HU_Thumbnail_Cover_SOP_JULY2026.md`
- the sawtooth `tear_edge()` in `build_v17.py`
- the full-bleed 40% band geometry

**Reference build:** `vanity-nobody-likes-him/ig_v7.jpg`
**Reference script:** `build_hu_ig_thumbnail.py`

---

## 0. Why this file exists

The July SOP contradicts itself. It carries two locked styles, but its Typography,
Zone Layout and Trait Graphic sections describe **Style 1 only** — an agent building
Style 2 from it will produce gold text, a handwriting stroke, and a filename with
"final" in it. All three are wrong for this format.

This file governs the screenshot + torn paper style. Where the two disagree, **this
one wins.**

---

## 1. Known-bad guidance in the old SOP

| Old SOP says | Reality |
| --- | --- |
| Line 2 is Gold `#C9A84C` | Navy `#1D3557` on parchment |
| Parchment covers top 40%, full-bleed | Paper is inset and sized to its text |
| "no tearing on the left or right sides" | All four edges are torn |
| White Impact setup line always | Not a rule — judgment call per title |
| Output `ig_reel_A_final.jpg` | Violates the File Naming Rule. Never "final". |
| SOP lives in `betty/` | It's in `Salvadore - art department/` |
| Reference at `betty/thumbnails/batch/...` | That folder does not exist |

---

## 2. Choose the frame FIRST — it decides everything

No geometry rescues a bad grab.

- **Headroom is mandatory.** Bart must sit low enough that the paper has quiet dead
  space above his hair. A tight 16:9 close-up where his head fills the frame **cannot
  work** — filling a 9:16 canvas from it drives his forehead under the paper. This
  failed four times before a proper frame was used.
- **Prefer an already-vertical grab.** Reference: `IG_bart_leaning_in_to_camera_green_sweater_full.png`
  (639×1200, Bart in the lower two-thirds, dark headliner above).
- **Vertical crop is TOP-ANCHORED.** Centring eats the headroom you just gained.
- Quiet dead space — headliner, dark wall, sky. Engaged expression, mid-sentence.

### Measure hair and face separately

They are different limits:

- **Face is untouchable.** Never covered, never cropped.
- **Hair may be covered.** Bart approved this explicitly.

In the reference frame: hair tips at y=437, skin starts at y=635. That's ~198px of
hair the paper may eat. Detect both before building — don't eyeball:

```python
# hair: first row departing from the flat dark headliner
# face: first row with a real run of skin-tone pixels
skin = (R>95)&(G>40)&(B>20)&(R>G+15)&(G>B)&((R-B)>15)
```

**The check that matters:** the bottom tear reaches `PARCH_BOT + amp*1.2`. Test *that*
number against the forehead, not the paper edge. A deep tooth is what lands on his eyes.

---

## 3. The tear — the part everyone gets wrong

### Never use a sawtooth

`build_v17.py` walks a fixed step (`step = W/n`) and flips direction in groups of 2–4.
Every tooth is therefore the same width. **That reads as a saw blade, not a tear.**
Rejected repeatedly. Do not resurrect it.

### Use fractal value noise

Real torn paper **varies its frequency**. Three octaves of smoothed value noise, summed:

| Octave | Wavelength (horizontal edges) | Vertical edges | Weight |
| --- | --- | --- | --- |
| 1 — slow wander | 420 px | 240 px | 0.55 |
| 2 — bites | 90 px | 64 px | 0.38 |
| 3 — fibre | 11 px | 9 px | 0.10 |

Vertical edges are shorter, so tighten the wavelengths or the teeth look stretched.

Amplitude: **70px top, ×1.2 bottom, 42px sides.**

Bart tested four variants and rejected the ones adding deep gaussian bites and fibre
fringe. **Plain three-octave noise is the approved look. Do not embellish it.**

### All four edges are torn

North, south, **east and west**. An inset paper with straight sides reads as a cut
rectangle, not torn paper.

### Corners must be exact and inside the margin

**Taper the noise to zero** over ~60px at each end of every edge. Untapered noise
wanders the corner off its mark and produces a ragged corner.

**MARGIN must exceed AMP_V** (70 > 42) or the side tear pushes the paper off-canvas.
Assert it. Do not eyeball it.

### Shadow is not optional

It is most of what sells the paper. Polygon offset `+16,+18`, black alpha 130,
gaussian blur 26, composited *under* the parchment. Mask blurred 0.8 to anti-alias.

---

## 4. The paper serves the text — not the reverse

### There is no fixed paper height

`PARCH_BOT = 0.415 * H` is **dead**. It left two-thirds of the paper as empty cream on
short titles.

```
paper half-width  = (text_block_width  / 2 + PAD_X) × 1.10
paper half-height = (text_block_height / 2 + PAD_Y) × 1.10
```

Base padding `PAD_X = 46`, `PAD_Y = 40`. The **×1.10** is Bart's — words were crowding
the tear.

**Order matters.** Size the type *first*, against base padding, **then** grow the paper
around it and re-centre the text. If the growth feeds back into the font fit, the
headline shrinks instead of gaining breathing room — the opposite of the intent.

### Text distribution is a judgment call, NOT a rule

There is **no rule** that line 1 is white above and line 2 is navy on the paper. Bart
was explicit. Options:

- **All text on the paper** — used in both approved builds.
- **White Impact setup line above, paper on the punch** — for shorter titles.
- **Paper as a small highlight** on one or two punch words.

**It depends on the length of the title.**

### The white setup line COSTS headroom — the counter-intuitive finding

The old SOP implies long titles want a setup line. **The opposite is true.** The white
line spends ~200px before the paper even starts. On a 437px band that is fatal.

Measured, "Vanity / Nobody Likes Him, Everyone Respects Him":

```
VANITY white + 2 on paper, air 70   -> HITS HAIR 115px
all 3 on paper, air 70              -> HITS HAIR  25px
VANITY white + 2 on paper, air 20   -> HITS HAIR  65px
all 3 on paper, air 20              -> CLEAR      25px   <- shipped
```

**Long titles can least afford the setup line.** Test before choosing.

### When splitting, the paper carries the PUNCH

Not merely the back half of the sentence. From Bart's own splits:
*"STUBBORN. The Fear of Being Wrong."* → setup `THE FEAR OF BEING WRONG`, paper
`STUBBORN`. Reorder if the payoff should land last.

### Per-line emphasis

Lines may be sized independently — `("VANITY", 3.0)` sets the trait word at 3×.

- Base size = largest that fits **every unemphasised line**, so emphasis doesn't drag
  the others down.
- Guard: an emphasised line must never overflow the paper width. Shrink it if it does.

---

## 5. HU LOGO — LOCKED POSITION (Bart, 2026-07-17)

**Locked for all IG Reel covers in this format.**

| Property | Locked value |
| --- | --- |
| File | `betty/HU logo new 2026 Watermark.png` — **used unaltered** |
| Scale | 3× the old 148px spec → paste box **444px wide** |
| Visible mark | **~292px wide**, ~202px tall |
| Position | **Bottom-left.** Mark occupies **x 21–313, y 1672–1874** |
| Margins | **21px from left, 46px from bottom** |
| Paste box | `(-64, -99)` from bottom-left, i.e. box origin (-64, 1575) |

**Record the MARK position, not the box.** The box coordinates are only meaningful
while the PNG carries its transparent padding. The mark position survives a re-export.

### Why the box hangs off-canvas

The PNG is a 720×720 canvas with the mark occupying only 475×328 inside it. At 3× that's
**85px of padding left, 97px top, 66px right, 144px bottom**. The padding, not the mark,
hits the canvas edge first. To move the mark down at all, the box must overhang.

**Consequence:** "move it down 1 inch" (300px @ 300dpi) is **impossible** — the mark has
only 191px of travel before the quill is amputated. Max is ~0.48in. If more is ever
needed, the padding must be cropped, which means altering the asset.

### Two known asset defects — accepted by Bart, not fixed

1. **The counters are opaque white.** Transparency covers only the outer background.
   The enclosed space inside the U and the gaps in the H are **solid white** — 22.6% of
   the mark is opaque white; inside the U bowl alone, 6,275 white pixels. On dark
   clothing these read as white patches. **Bart: "It is acceptable."** Do not "fix" it
   without asking.
2. **`hu_brand_logo.jpg` is worse** — flattened, entire background opaque white. It is
   the fallback only. **Neither logo file is genuinely transparent.**

### Contrast — measure it

On the reference frame the logo is invisible on the sweater:

```
logo ink luminance   111.8
backdrop luminance   112.1     <- a gap of 0.3
```

Navy-and-grey mark on a mid grey-green sweater of identical brightness. **No file swap
fixes this** — it is a contrast problem, not a format problem. Bart accepted it here.
If a future frame makes it unreadable, the fixes are a torn parchment chip behind the
mark, a soft dark halo, or a white knockout — **ask, don't choose.**

---

## 6. Locked settings (as shipped in ig_v7)

```
CANVAS      1080 x 1920
PARCHMENT   #F5F5DC  flat. No grain, no texture, no gradient.
HU_NAVY     #1D3557  exact
MARGIN      70        # nothing crosses; must exceed AMP_V
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

---

## 7. Fonts

Georgia Bold and Impact are proprietary. **On the Mac use the real ones:**
`/System/Library/Fonts/Supplemental/Georgia Bold.ttf` and `.../Impact.ttf`

In a Linux container they don't exist. Metric-holding substitutes:

- **Gelasio Bold** → metric-compatible Georgia Bold
  `https://raw.githubusercontent.com/SorkinType/Gelasio/master/fonts/ttf/Gelasio-Bold.ttf`
- **Anton** → closest open Impact
  `https://raw.githubusercontent.com/google/fonts/main/ofl/anton/Anton-Regular.ttf`

**The approved builds used the substitutes.** Rebuilding on the Mac with the real fonts
**will shift the type** — expect it and re-check the fit.

---

## 8. Build checks — assert, don't eyeball

```python
assert min(xs) > 0 and max(xs) < W          # paper never leaves the canvas
assert min(ys) > 0 and max(ys) < H
assert X0 >= MARGIN and X1 <= W - MARGIN    # corners inside margin
```

Print every build:

```
paper x 70-1009  y 90-469 (h=379)  sizes [156, 52, 52]pt  bleed L67 R56
lowest tooth 518  vs forehead 635  -> CLEAR 117px
```

---

## 9. Order of operations

1. Pull the frame from the **actual video**. Check headroom. **Reject bad frames early.**
2. Detect hairline and forehead. Both.
3. Decide the split by title length. **Test it — don't assume the setup line helps.**
4. Size type → build paper around it → grow 10%.
5. Tear all four edges, fractal noise, tapered corners.
6. Shadow → parchment → text → logo.
7. Run the asserts. Check the lowest tooth against the **forehead**.
8. Save `ig_v1.jpg` in the slug folder. Increment, never overwrite, never "final".
9. **Bart approves. Nothing else does.**

---

## 10. LANDSCAPE FRAMES — pad, don't reject (added 2026-07-17)

**This amends section 2.** A 16:9 frame is no longer an automatic reject. Scale-to-fill
is what fails, not the frame — it drives Bart's head under the paper. The fix is to
scale him to a chosen size, bottom-align, and **extend the headliner upward** to
manufacture headroom.

**Reference build:** `liar-liar/ig_v2.jpg` — Bart: *"This is excellent."*

### Method (`manual_scale` in `build_hu_ig_thumbnail.py`)

1. Scale the frame by a chosen factor — **not** `max(W/bw, H/bh)`.
2. Crop horizontally on the face (`face_cx_src`).
3. **Bottom-align**, so his body reaches the canvas edge.
4. Fill the gap above by extending the top of the frame upward.

### The fill must not be a flat block

Sample the **top 6 rows**, then walk a darkening gradient (78% → 100%) with light grain.
Headliner darkens away from the glass; a flat fill bands visibly.

```python
band = np.array(crop.crop((0, 0, W, 6))).astype(float).mean(axis=0)
for r in range(pad):
    k = 0.78 + 0.22 * (r / pad)
    row = band * k + rng.normal(0, 1.6, band.shape)
```

### Only works on quiet dead space — CHECK FIRST

Measure the std of the top rows of the **cropped** region before trusting it. The
reference frame gave mean RGB 18/29/35 with **std ≈5** — near-uniform, so the extension
is invisible. On a busy top edge it will look obviously faked. **If std is high, reject
the frame.**

### Scale is a clearance decision, not an aesthetic one

Bigger scale = bigger Bart = less headroom. Measured on `bart_green_sweater_serious.png`
with the stacked LIAR type:

```
scale 1.50 -> tooth 779, face 734  -> ON FACE by 45px
scale 1.40 -> covers hair 85px, face clear only 33px
scale 1.30 -> fully clear, 4px above hair          <- shipped
scale 1.25 -> fully clear, 47px above hair
```

**Sweep the scale and read the clearances. Do not eyeball it.** Pick the largest scale
that still clears the forehead with margin.

---

## 11. LAYOUT OPTIONS — the approved set

Three layouts are now locked. **Choose by title length.** None is the default.

### Option A — all text on the paper, normal weight
`true-optimists-write-like-this/ig_v6.jpg` — Bart: *"very very good"*

Two lines, equal size, on one paper. For mid-length titles.
Type ~78pt. Paper ~258px.

### Option B — trait word emphasised
`vanity-nobody-likes-him/ig_v7.jpg` — Bart: *"pretty darn good"*

Three lines, first at **3x** via `("VANITY", 3.0)`. For a title that is a trait label
plus a payoff line. Type `[156, 52, 52]pt`. Paper ~379px.
Use when the title names a trait — the trait word carries the thumbnail.

### Option C — STACKED HERO TYPE (added 2026-07-17)
`liar-liar/ig_v2.jpg` — Bart: *"This is excellent."*

**For very short, punchy titles.** Two or three words stacked, set as large as the paper
allows, on a tall paper. Type `[230, 230]pt`. Paper **590px** — nearly a third of the
canvas.

```python
build(PHOTO, out, ["LIAR !", "LIAR!"], line1=None,
      top_air=70, face_cx_src=759, manual_scale=1.30)
```

**Width is the ceiling, not height.** At `MARGIN 70 + AMP_V 42 + PAD_X 46` per side,
only **764px** is available for type. A 5-character word tops out near **230pt**. Asking
for "3x" on a short word is usually impossible — the letters hit the margin first.
Do not narrow the margin to chase it; that breaks the corner rule.

**The paper follows the type.** Doubling the type roughly triples the paper. You cannot
specify paper height and type size independently — the paper is not free to obey.

---

## 12. Copy is set EXACTLY as Bart writes it

The reference build reads `LIAR !` on line one (space before the bang) and `LIAR!` on
line two. **That is how he typed it.** It was flagged to him and left alone.

Never tidy, normalise, correct, or re-punctuate Bart's headline copy. Flag it and ship
what he wrote.
