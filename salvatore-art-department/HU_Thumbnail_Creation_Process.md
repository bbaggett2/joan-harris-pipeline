# HU Brand Thumbnail — The Screenshot + Torn Parchment Method

**Brand:** Handwriting University (HU)
**Format:** Instagram Reel / TikTok cover, 1080×1920 (9:16) — **this method is 9:16 only.**
**Style:** real screenshot of the host + torn cream parchment + collegiate lettering
**Status:** locked by Bart, 2026-07-17 → 2026-08-09
**Lives at:** `salvatore-art-department/HU_Thumbnail_Creation_Process.md`
**Referenced by:** `/brands/handwriting-university.md` §7

**Ruling files:**
- SOP → `Salvadore - art department/SOP_HU_IG_Screenshot_Torn_Paper_v2.md`
- Build → `Salvadore - art department/build_hu_ig_thumbnail.py`

Reference builds Bart signed off on:
- `true-optimists-write-like-this/ig_v6.jpg` — *"very very good"*
- `vanity-nobody-likes-him/ig_v7.jpg` — *"pretty darn good"*
- `liar-liar/ig_v2.jpg` — *"This is excellent."*

> **Everything in §1–§9 below is Bart's, transcribed unaltered.** No procedure in this
> document was authored by an agent. §10 and §11 are reconciliation notes only — they
> record path and filename facts, and they contain no build instructions.

---

## 0. Repository contents — what must be in this folder

An agent can only follow this method if the assets are present. Upload manifest in §11.

**Required:**

| File | Why |
| :--- | :--- |
| `HU_Thumbnail_Creation_Process.md` | This file. The narrative method. |
| `SOP_HU_IG_Screenshot_Torn_Paper_v2.md` | The ruling SOP named above. |
| `build_hu_ig_thumbnail.py` | The build. **The method is this script — not a prompt.** |
| `HU logo new 2026 Watermark.png` | The logo, used unaltered. See §7. |

**Reference builds (read-only comparison targets):**

| File | Layout |
| :--- | :--- |
| `liar-liar/ig_v2.jpg` | C — stacked hero |
| `true-optimists-write-like-this/ig_v6.jpg` | A — all text on paper |
| `vanity-nobody-likes-him/ig_v7.jpg` | B — trait emphasised |
| `Thumbnail.HU_hates-all-men-host-photo-sample.png` | host screengrab sample |
| `thumbnail_IQtest_ig_approved.jpg` | generated-host sample — see §10.3 |

**URL forms.** A `blob/` URL returns an HTML page, not an image. Any agent or model that
needs to *see* a reference must use the raw form:

```
view →  https://github.com/bbaggett2/joan-harris-pipeline/blob/main/salvatore-art-department/<FILE>
load →  https://raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/salvatore-art-department/<FILE>
```

---

## 1. What this style is, in one sentence

A real frame of Bart from the actual video, with a piece of torn cream parchment laid
over the quiet space above his head, carrying the title in HU-navy collegiate type, with
the HU feather-and-letters mark in the corner.

Three things make it work. Everything else is detail.

1. **The parchment must precisely torn at the edges. It must resemble old paper.**
2. **The parchment must never cover his face.**
3. **The parchment sizes itself to the key words in the headline — not the other way round.**

---

## 2. The color palette

| Role | Color | Hex | Notes |
| --- | --- | --- | --- |
| Parchment | Cream | `#F5F5DC` | **Flat fill. No grain, no texture, no gradient.** The torn *shape* is what reads as paper — texture makes it look fake, not real. |
| Headline type | HU Navy | `#1D3557` | Exact. The one non-negotiable brand color. |
| Type emboss | Warm tan | `#BEB696` (190,182,150) | A 3px/4px offset shadow behind the navy, so the letters lift off the cream. |
| Setup line (optional) | White | `#FFFFFF` | Only when a white line sits above the parchment. Heavy black outline. |
| Paper shadow | Black @ 51% | — | Offset +16/+18, blur 26, *under* the parchment. This is most of what sells the paper as physical. |

The parchment/navy pairing is the brand's native combination — navy collegiate letters on
cream is exactly the HU logo's own palette, which is why the logo fits nicely on the thumbnail and expresses university educational Ivy League status..

---

## 3. The lettering

- **Headline:** Georgia Bold — a collegiate serif. On the Mac use the real
  `/System/Library/Fonts/Supplemental/Georgia Bold.ttf`. In a Linux container Georgia is
  absent (it's proprietary); **Gelasio Bold** is a metric-compatible substitute.
- **Setup line (when used):** Impact. Substitute: **Anton**.
- Rebuilding on the Mac with the real fonts shifts the metrics slightly — always re-check
  the fit after switching.

Type is **embossed**, not flat: a warm-tan copy offset behind the navy. On cream, flat navy
looks printed; the emboss makes it look stamped.

---

## 4. The torn edge — the hardest part, and where every early attempt failed

### What does NOT work: a sawtooth

The first builds walked a **fixed step** and flipped direction in tidy groups. Every tooth
came out the same width. That reads as a **saw blade**, not torn paper. It was rejected
over and over until the cause was named: a fixed step *cannot* look torn, because real
torn paper never tears at a constant frequency.

### What works: fractal value noise

Real torn paper **varies its frequency** — long slow wander, occasional bites, fine fibre,
all at once. So the edge is three octaves of smoothed value noise, summed:

| Octave | Does | Wavelength (long edges) | Weight |
| --- | --- | --- | --- |
| 1 | slow wander | 420 px | 0.55 |
| 2 | bites | 90 px | 0.38 |
| 3 | fibre | 11 px | 0.10 |

Bart tested four candidates — plain noise, noise + deep gouges, noise + fibre fringe — and
chose **plain three-octave noise.** Do not embellish it.

### All four edges are torn

North, south, **and east/west.** An early rule said "no tearing on the left or right" — but
that was written for a full-bleed band that ran off the sides. Once the paper became an
inset rectangle with four visible corners, straight sides read as a **cut card**. So every
edge is torn now.

### Clean corners

All four corners must land **inside the margin** and be exact. The trick: **taper the noise
to zero** over ~60px at each end of every edge. Without the taper the noise wanders the
corner off its mark. And the side margin must be **larger than the side tear amplitude**, or
a tear tooth pushes the paper off-canvas. The build *asserts* this rather than trusting the eye.

---

## 5. The parchment serves the words

### There is no fixed paper size

An early version pinned the paper to 41.5% of the canvas height. On short titles that left
two-thirds of it as empty cream. **Dead.** Now:

```
paper half-width  = (text_width  / 2 + horizontal_padding) × 1.10
paper half-height = (text_height / 2 + vertical_padding)  × 1.10
```

The **×1.10** is Bart's own note — words were crowding the tear, so the paper grows 10%
around them.

**Order matters:** size the type first, *then* grow the paper around it. If the growth feeds
back into the font-sizing, the headline shrinks instead of gaining breathing room — the
exact opposite of the intent.

### Where the words go is a judgment call, NOT a rule

There is **no rule** that one line goes white-above and the rest goes navy-on-paper. Bart
was explicit. Three approved layouts, chosen by title:

- **A — all text on the paper**, equal size. Mid-length titles. *(ig_v6, "very very good")*
- **B — trait word emphasised**, e.g. the trait at 3× above two normal lines. For
  trait-plus-payoff titles. *(ig_v7, "pretty darn good")*
- **C — stacked hero type**, two or three short words set as large as the paper allows, on a
  tall paper. For very short, punchy titles. *(ig_v2 Liar Liar, "This is excellent")*

### A counter-intuitive lesson: the white setup line COSTS headroom

It seems like long titles want a white line up top. The opposite is true. A white line
spends ~200px before the parchment even begins — on a shallow band, that's fatal. **Long
titles can least afford it.** Always test placement against the hairline before choosing.If the headline is long, part of the the headline is a bold font and only the most compelling key word or phrase lands on the parchment. 

### When you split, the paper carries the PUNCH

Not the back half of the sentence. *"STUBBORN. The Fear of Being Wrong."* → the paper
carries **STUBBORN**, the trait, because that's the payoff. Reorder if the punch should land
last.

---

## 6. The frame decides everything — choose it first

No geometry rescues a bad grab.

- **Headroom is mandatory.** Bart must sit low enough that the parchment has quiet dead
  space above his hair. A tight 16:9 close-up where his head fills the frame **cannot
  work** — filling a vertical canvas from it drives his forehead under the paper. This
  failed four times before a proper frame fixed it in one.
- **Face is untouchable. Hair may be covered.** These are different limits — measure both.
  In the reference frame, hair tips began at y≈437 and skin at y≈635, giving ~200px of hair
  the paper could use. The check that matters: the *lowest tear tooth* (deeper than the
  paper edge) must clear the **forehead**, not just the hairline.

### Landscape frames: pad, don't reject

A 16:9 frame is no longer an automatic reject. Scale it to a chosen size, crop on the face,
**bottom-align**, and **extend the headliner upward** to manufacture headroom. The fill
can't be a flat block — sample the top few rows and walk a gentle darkening gradient with a
little grain, because a car headliner darkens away from the glass. This only works on quiet,
uniform dead space (check that the top rows are low-variance first). This is exactly how the
"Liar Liar" cover was built from a wide frame.

---

## 7. The HU logo

- File: **`HU logo new 2026 Watermark.png`**, used **unaltered**, bottom-left.
- It's a padded PNG — the visible feather-and-letters mark occupies only part of the
  canvas, so placement is measured against the **visible mark**, not the file box.
- **Locked scale:** 3× the original spec.
- **Two accepted asset quirks:** the letter counters are opaque white (they can show as
  white patches on dark clothing), and the mark's navy can match a grey-green sweater in
  brightness and vanish. Bart reviewed both and accepted them — *"It is acceptable."* Do
  not "fix" the asset without asking.

### Platform safe zones (2026-08-09)

Instagram Reels and TikTok overlay their own UI on the frame: captions and an action rail
across the **bottom**, a button rail up the **right**, and IG crops the *profile-grid tile*
to a centred 4:5 slice (trimming top and bottom). The logo used to pin to the true corner —
dead inside the danger zone. It's now **lifted above the reserved bottom band** so it
survives the overlay and the grid crop. The build reports when the paper or a tear tooth
crosses a safe zone, so hero-type layouts get a warning rather than a silent clip.

---

## 8. Build order (the checklist)

1. Pull the frame from the **actual video**. Check headroom. Reject bad frames early; pad
   landscape frames.
2. Detect the hairline **and** the forehead.
3. Choose the layout by title length. **Test the split against the hairline — don't assume.**
4. Size the type → build the paper around it → grow 10%.
5. Tear all four edges with fractal noise; taper the corners.
6. Shadow → parchment → embossed type → logo (lifted clear of the safe zone).
7. Run the asserts. Check the lowest tooth against the **forehead**, and the safe-zone report.
8. Save `ig_v1.jpg` in the video's slug folder. Increment — never overwrite, never a status
   word in the filename.
9. **Bart approves. Nothing else does.**

---

## 9. The rules that came out of this, in one place

1. Parchment is flat cream `#F5F5DC` — the torn shape sells it, never texture.
2. Type is HU Navy `#1D3557`, collegiate serif (Georgia Bold), embossed.
3. The tear is fractal noise, all four edges, corners tapered — never a fixed-step sawtooth.
4. The paper sizes to the text, then grows 10%. No fixed height.
5. Text distribution is judged per title. The white setup line is optional and costs
   headroom.
6. The frame is chosen first; the face is never covered; landscape frames get padded.
7. The logo is the unaltered PNG, 3×, bottom-left, lifted clear of platform UI.
8. Filenames are `v1`, `v2`, `v3` — only Bart approves, so only Bart names anything approved.

---

## 10. Reconciliation notes

These record facts about paths and filenames. **They add no procedure.**

### 10.1 `Salvadore` vs `salvatore`

Both spellings are live and they point at two different places:

| Context | Spelling | Path |
| :--- | :--- | :--- |
| Local Mac Studio (Joan's machine) | `Salvadore` | `Salvadore - art department/` |
| GitHub repo | `salvatore` | `salvatore-art-department/` |

The ruling-file paths in the header are **local Mac paths** and stay as written. GitHub URLs
use the lowercase hyphenated form. *This is a reconciliation of two observed spellings, not a
ruling — if you want one canonical spelling, say which and both get updated.*

### 10.2 Liar Liar — `ig_v2` vs `ig_v3`

§5 cites `liar-liar/ig_v2.jpg` as the Layout C reference carrying Bart's *"This is
excellent."* The file separately supplied is named `LiarLiar_thumbnail_approved_ig_v3.jpg`.
These are two different filenames and it is not established that they are the same image.

Also note: that filename contains the status word **"approved"**, which §8 step 8 and §9
rule 8 forbid. **Unresolved — Bart to confirm which file is canonical and whether the
GitHub copy should be renamed to conform.**

### 10.3 The generated-host sample

`thumbnail_IQtest_ig_approved.jpg` was supplied as a generated-host example rather than a
screengrab. **There is no written process for it.** It is listed in §0 as a reference image
only. Do not infer a method from it, and do not produce generated-host covers until Bart
documents one.

### 10.4 Scope

This method is **9:16 only**, per the header. The 16:9 YouTube thumbnail layout is
unaffected and remains as specified in `/brands/handwriting-university.md` §6.

---

## 11. Upload manifest

Target: `salvatore-art-department/` on `bbaggett2/joan-harris-pipeline`, branch `main`.

**Already present (per the URLs Bart supplied):**
- [x] `Thumbnail.HU_hates-all-men-host-photo-sample.png`
- [x] `thumbnail_IQtest_ig_approved.jpg`

**To upload — blocking. Without these an agent cannot execute the method:**
- [ ] `HU_Thumbnail_Creation_Process.md` ← this file
- [ ] `SOP_HU_IG_Screenshot_Torn_Paper_v2.md` ← copy from `Salvadore - art department/`
- [ ] `build_hu_ig_thumbnail.py` ← copy from `Salvadore - art department/`
- [ ] `HU logo new 2026 Watermark.png` ← the padded PNG, unaltered, do not re-export

**To upload — reference builds. Keep the slug-folder structure:**
- [ ] `liar-liar/ig_v2.jpg`
- [ ] `true-optimists-write-like-this/ig_v6.jpg`
- [ ] `vanity-nobody-likes-him/ig_v7.jpg`

**To upload — fonts, if the build runs anywhere other than the Mac:**
- [ ] `Gelasio-Bold.ttf` — Georgia substitute; Georgia is proprietary and absent on Linux
- [ ] `Anton-Regular.ttf` — Impact substitute, only if setup lines are used

**Do not upload:** Georgia Bold or Impact (proprietary, do not redistribute); any file with
a status word in its name other than the two already present; re-exported or "cleaned"
versions of the logo.

**After uploading**, confirm each raw URL resolves:
`https://raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/salvatore-art-department/<FILE>`
