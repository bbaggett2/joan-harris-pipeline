# HU Thumbnail Methods — Generated Host + Torn Parchment

**Version:** 5
**Brand:** Handwriting University (HU)
**Supersedes:** v4, *HU Brand Thumbnail — The Screenshot + Torn Parchment Method*
**Covers:** both HU thumbnail deliverables, in build order — YouTube 16:9 first, vertical 9:16 second
**Status:** rewritten 2026-08-14 on Bart's ruling. **§6 and §12 are new and require Bart's ratification.**
**Lives at:** `salvatore-art-department/HU_Thumbnail_Creation_Process_gemini_v5.md`
**Referenced by:** `/brands/handwriting-university.md` §7

---

## What changed in v5, and what is now retired

Bart ruled on 2026-08-14: **the host is an AI-generated likeness of Bart, on both deliverables.**
The real photographs are overused and are retired as output. They become reference input.

**Retired. Do not follow these anywhere:**

| Retired rule | Where it came from | Why |
| :--- | :--- | :--- |
| "Pull the frame from the actual video" | v4 §6, v4 §8 step 1 | Screengrab method is retired entirely. See §6. |
| "Headshots — real only" | `HU_Video_Publishing_Pipeline_V7` Phase 4 | Superseded. The host is generated from a reference set. |
| "Do not produce generated-host covers until Bart documents one" | v4 §10.3 | Bart has now documented one. This file is that documentation. |
| Hairline/forehead *detection* on a found frame | v4 §6 | Headroom is now specified in the prompt, not discovered. The clearance *check* survives — see §6.4. |
| Landscape padding / headliner extension | v4 §6 | Was a rescue for bad 16:9 grabs. Generate at the target ratio instead. |
| "Screenshot" in the document title | v4 header, v4 §1 | No longer describes either deliverable. |

**Unchanged and still Bart's, transcribed from v4:** §1 (what the style is), §2 (palette),
§3 (lettering), §4 (the torn edge), §5 (the parchment serves the words), §7 (the logo).
The parchment craft is unaffected by where the host image comes from.

> **Provenance.** §1–§5 and §7 are Bart's, carried forward. §6 and §12 were drafted by an
> agent on 2026-08-14 to implement Bart's ruling, and are **`[UNRATIFIED DRAFT]`** until he
> reviews them. §0, §0.5, §8, §9, §10 and §11 are reconciliation and ordering, not craft.

---

## 0. Repository contents

**Required to execute:**

| File | Why |
| :--- | :--- |
| `HU_Thumbnail_Creation_Process_v5.md` | This file. |
| `SOP_HU_IG_Screenshot_Torn_Paper_v2.md` | The 9:16 build SOP. **Name is now misleading** — see §10.1. |
| `build_hu_ig_thumbnail.py` | The 9:16 build. **The method is this script — not a prompt.** |
| `HU_logo_new_2026_Watermark.png` | The logo, used unaltered. See §7. |

**Host reference set — input to generation, never output. See §6.2:**

| File | Use |
| :--- | :--- |
| `B16A5236_revised_bart_red_smile.jpg` | warm / approachable |
| `Bart-serious-clear-bluesuit.png` | serious, blue suit |
| `BartBaggett-serious-clear-bluesuit2.png` | serious, blue suit, alt angle |
| `BartBaggett72whitebackgroundB16A5244blue_B.jpg` | clean isolate, good for reference |
| `Bart_MG_1770_attorney_shot.png` | authoritative |
| `Bartbaggett_MG_1881.jpg` | high-resolution reference |
| `bartbaggett_MG_1827-labcoat.jpg` | lab coat — QDE-leaning, use with care on HU |

**Reference builds (read-only comparison targets):**

| File | Layout |
| :--- | :--- |
| `liar-liar/ig_v2.jpg` | C — stacked hero |
| `true-optimists-write-like-this/ig_v6.jpg` | A — all text on paper |
| `vanity-nobody-likes-him/ig_v7.jpg` | B — trait emphasised |
| `thumbnail_IQtest_ig_approved.jpg` | **generated-host precedent.** Formerly banned as undocumented; v5 documents the method, so this becomes a legitimate reference. |

**URL forms.** A `blob/` URL returns an HTML page, not an image. To *see* a reference, use raw:

```
view →  https://github.com/bbaggett2/joan-harris-pipeline/blob/main/salvatore-art-department/<FILE>
load →  https://raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/salvatore-art-department/<FILE>
```

---

## 0.5 Deliverable order and platform specs

**Two deliverables, in this order. Do not reverse them.**

### Step 1 — YouTube thumbnail (16:9). Build this first.

| Spec | Value |
| :--- | :--- |
| Canvas | **1280 × 720 px** |
| Aspect ratio | **16:9** |
| Minimum width | 640 px |
| Formats | JPG, PNG, GIF |
| File size | **Under 2 MB** |
| Legibility floor | Must read at 168 × 94 px |

**Layout is not specified here.** It lives in `/brands/handwriting-university.md` §6 — one
spec, one home. Restating it across two files is how §6 and §8.1 drifted apart.

Get this approved before touching Step 2.

### Step 2 — Vertical cover (9:16).

| Spec | Value |
| :--- | :--- |
| Canvas | **1080 × 1920 px** |
| Aspect ratio | **9:16** |
| Output | JPG, 92%+ quality, 300 DPI, RGB |
| Platforms | Instagram Reels, TikTok, YouTube Shorts |

**"Derived from Step 1" means same host, not same pixels.** Regenerate the plate at 9:16
using the identical reference set, wardrobe, and scene descriptors — do not upscale, crop,
or pad the 16:9. Padding a landscape plate into a vertical canvas was a v4 rescue for bad
screengrabs and is retired with them.

> **YouTube Shorts caveat — unresolved.** A Short is 1080 × 1920, but YouTube crops the cover
> differently depending on where it surfaces — Shorts feed, channel grid, search, watch page.
> §7's safe zones were measured against **Instagram Reels and TikTok only** and have not been
> validated against YouTube's crops. Check on a phone before publishing. See §12 item 3.

---

## 1. What this style is, in one sentence

A photoreal image of Bart in a collegiate setting, with a piece of torn cream parchment laid
over the quiet space above his head, carrying the title in HU-navy collegiate type, with the
HU feather-and-letters mark in the corner.

Three things make it work. Everything else is detail.

1. **The parchment must be precisely torn at all four edges.** It must read as a sheet of old
   paper someone tore by hand — never as a cut card. The torn *shape* does that work. Do not
   reach for grain, texture, or a gradient to age it; see §2 and §9 rule 1.
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
| Trait circle — **16:9 only** | Teacher Red | `#D62828` | Circles or highlights the trait letterform. **Not used on 9:16.** |

The parchment/navy pairing is the brand's native combination — navy collegiate letters on
cream is exactly the HU logo's own palette, which is why the logo fits nicely on the thumbnail
and expresses university educational Ivy League status.

---

## 3. The lettering

- **Headline:** Georgia Bold — a collegiate serif. On the Mac use the real
  `/System/Library/Fonts/Supplemental/Georgia Bold.ttf`. In a Linux container Georgia is
  absent (it's proprietary); **Gelasio Bold** is a metric-compatible substitute.
- **Setup line (when used):** Impact. Substitute: **Anton**.
- Rebuilding on the Mac with the real fonts shifts the metrics slightly — always re-check the
  fit after switching.

Type is **embossed**, not flat: a warm-tan copy offset behind the navy. On cream, flat navy
looks printed; the emboss makes it look stamped.

---

## 4. The torn edge — the hardest part, and where every early attempt failed

### What does NOT work: a sawtooth

The first builds walked a **fixed step** and flipped direction in tidy groups. Every tooth came
out the same width. That reads as a **saw blade**, not torn paper. It was rejected over and over
until the cause was named: a fixed step *cannot* look torn, because real torn paper never tears
at a constant frequency.

### What works: fractal value noise

Real torn paper **varies its frequency** — long slow wander, occasional bites, fine fibre, all at
once. So the edge is three octaves of smoothed value noise, summed:

| Octave | Does | Wavelength (long edges) | Weight |
| --- | --- | --- | --- |
| 1 | slow wander | 420 px | 0.55 |
| 2 | bites | 90 px | 0.38 |
| 3 | fibre | 11 px | 0.10 |

Bart tested four candidates — plain noise, noise + deep gouges, noise + fibre fringe — and chose
**plain three-octave noise.** Do not embellish it.

### All four edges are torn

North, south, **and east/west.** An early rule said "no tearing on the left or right" — but that
was written for a full-bleed band that ran off the sides. Once the paper became an inset rectangle
with four visible corners, straight sides read as a **cut card**. So every edge is torn now.

*(16:9 differs — brand kit §6 allows scissor-cut edges there. See §10.4.)*

### Clean corners

All four corners must land **inside the margin** and be exact. The trick: **taper the noise to
zero** over ~60px at each end of every edge. Without the taper the noise wanders the corner off
its mark. And the side margin must be **larger than the side tear amplitude**, or a tear tooth
pushes the paper off-canvas. The build *asserts* this rather than trusting the eye.

---

## 5. The parchment serves the words

### There is no fixed paper size

An early version pinned the paper to 41.5% of the canvas height. On short titles that left
two-thirds of it as empty cream. **Dead.** Now:

```
paper half-width  = (text_width  / 2 + horizontal_padding) × 1.10
paper half-height = (text_height / 2 + vertical_padding)  × 1.10
```

The **×1.10** is Bart's own note — words were crowding the tear, so the paper grows 10% around them.

**Order matters:** size the type first, *then* grow the paper around it. If the growth feeds back
into the font-sizing, the headline shrinks instead of gaining breathing room — the exact opposite
of the intent.

### Where the words go is a judgment call, NOT a rule

There is **no rule** that one line goes white-above and the rest goes navy-on-paper. Bart was
explicit. Three approved layouts, chosen by title:

- **A — all text on the paper**, equal size. Mid-length titles. *(ig_v6, "very very good")*
- **B — trait word emphasised**, e.g. the trait at 3× above two normal lines. For
  trait-plus-payoff titles. *(ig_v7, "pretty darn good")*
- **C — stacked hero type**, two or three short words set as large as the paper allows, on a tall
  paper. For very short, punchy titles. *(ig_v2 Liar Liar, "This is excellent")*

### A counter-intuitive lesson: the white setup line COSTS headroom

It seems like long titles want a white line up top. The opposite is true. A white line spends
~200px before the parchment even begins — on a shallow band, that's fatal. **Long titles can
least afford it.** Always test placement against the hairline before choosing.

**Default for long headlines.** Set part of the headline in a bold font off the paper, and land
only the most compelling key word or phrase on the parchment. This is the starting point, not a
rule — the section above still governs, and the split is judged per title.

### When you split, the paper carries the PUNCH

Not the back half of the sentence. *"STUBBORN. The Fear of Being Wrong."* → the paper carries
**STUBBORN**, the trait, because that's the payoff. Reorder if the punch should land last.

---

## 6. The host plate — generated, not grabbed `[UNRATIFIED DRAFT]`

> Replaces v4 §6 entirely. Drafted 2026-08-14 to implement Bart's ruling. Needs his sign-off.

### 6.1 What is generated and what is not

| Element | Source |
| :--- | :--- |
| Scene — collegiate desk, library, Ivy League campus | **Gemini, generated fresh each time.** No source material. |
| Host — Bart | **Gemini, generated likeness**, guided by the reference set in §6.2. |
| Trait handwriting | **Never generated.** Published library card. Brand kit §6 item 2. |
| Headline, parchment, logo | **Never generated.** Composited by the build script. |

The plate carries **host and scene only.** Everything else is overlay. Asking one prompt to
assemble background, handwriting, and words is what produces drift — brand kit §6 item 5.

### 6.2 Likeness consistency — the thing that will break first

A generated likeness varies run to run. Nobody notices across one thumbnail. Everybody notices
across thirty, and by then the channel has quietly stopped looking like one person.

**Controls, all three required:**

1. **Fixed reference set.** Pass the same reference images every time. Default pair:
   `BartBaggett72whitebackgroundB16A5244blue_B.jpg` (clean isolate) plus one expression match
   from §0. Do not swap references between videos in a batch.
2. **Locked descriptors.** Age, build, hair, and eye colour are written into the prompt as fixed
   text and never re-worded per video. Only wardrobe and scene change.
3. **Recognition check at approval.** Put the new plate beside the last two approved thumbnails.
   The question is not "is this a good image" but **"is this the same man."** This is Bart's
   check. No assert can do it.

### 6.3 Expression comes from the transcript

Brand kit §6 item 1: emotion and body language are drawn from the content of the video, not
chosen arbitrarily. Read the transcript, name the emotional register in one word, then write it
into the prompt. Host always looking directly into camera.

This is the one place the generated approach is strictly better than the screengrab: the
expression is specified rather than hunted for, so a near-miss is a prompt edit, not a rescan.

### 6.4 Composition — specify headroom, don't discover it

v4 hunted for a frame with quiet space above the head. Now it is requested.

- **9:16 plate:** host positioned low in frame, with quiet, low-variance dead space across the
  top third for the parchment. Request it explicitly.
- **16:9 plate:** host waist-up, right ~40%, entire head visible and never cropped, left ~40%
  left quiet for the trait image. Brand kit §6.
- **The face is untouchable. Hair may be covered.** Unchanged from v4 and still absolute.
- **The clearance assert survives.** The build still measures where hair and skin begin and
  confirms the lowest tear tooth clears the **forehead**, not merely the hairline. Detection on
  a found frame is retired; verification on a generated plate is not.

### 6.5 Rejecting a plate

Regenerate — do not rescue. A wrong expression, a covered face, or insufficient headroom is a
prompt problem now, and prompt problems are cheap. The v4 padding and headliner-extension tricks
existed because a screengrab was the only frame available. That constraint is gone.

---

## 7. The HU logo

- File: **`HU_logo_new_2026_Watermark.png`**, used **unaltered**, bottom-left.
- It's a padded PNG — the visible feather-and-letters mark occupies only part of the canvas, so
  placement is measured against the **visible mark**, not the file box.
- **Locked scale:** 3× the original spec.
- **Two accepted asset quirks:** the letter counters are opaque white (they can show as white
  patches on dark clothing), and the mark's navy can match a grey-green sweater in brightness and
  vanish. Bart reviewed both and accepted them — *"It is acceptable."* Do not "fix" the asset
  without asking.

### Platform safe zones (2026-08-09)

Instagram Reels and TikTok overlay their own UI: captions and an action rail across the
**bottom**, a button rail up the **right**, and IG crops the *profile-grid tile* to a centred 4:5
slice. The logo used to pin to the true corner — dead inside the danger zone. It is now **lifted
above the reserved bottom band**. The build reports when the paper or a tear tooth crosses a safe
zone, so hero-type layouts get a warning rather than a silent clip.

**Not yet measured for YouTube Shorts.** See §0.5 Step 2 and §12 item 3.

---

## 8. Build order (the checklist)

**Step 1 — YouTube 16:9**

1. Read the transcript. Name the emotional register (§6.3).
2. Generate the host plate: Gemini, solo step, host and scene only (§6.1, §6.4).
3. Recognition check against the last two approved thumbnails (§6.2). Regenerate if it drifts.
4. Pull the trait card from the published library; crop to the strokes, drop the deck chrome.
5. Composite by script: trait image + red circle → headline + parchment key word → logo.
6. Confirm ≤5 words, readable at 168×94, bottom-right clear, under 2 MB.
7. Save `yt_v1.jpg` in the video's slug folder. Increment — never overwrite, never a status word.
8. **Bart approves.** Nothing proceeds without it.

**Step 2 — Vertical 9:16**

9. Regenerate the plate at 9:16 — same references, same wardrobe, same scene (§0.5 Step 2).
10. Choose the layout by title length (§5). Test the split against the hairline — don't assume.
11. Size the type → build the paper around it → grow 10%.
12. Tear all four edges with fractal noise; taper the corners.
13. Shadow → parchment → embossed type → logo (lifted clear of the safe zone).
14. Run the asserts. Lowest tooth clears the **forehead**; check the safe-zone report.
15. Save `ig_v1.jpg` in the slug folder. Increment.
16. **Bart approves. Nothing else does.**

---

## 9. The rules that came out of this, in one place

1. Parchment is flat cream `#F5F5DC` — the torn shape sells it, never texture.
2. Type is HU Navy `#1D3557`, collegiate serif (Georgia Bold), embossed.
3. The tear is fractal noise, all four edges, corners tapered — never a fixed-step sawtooth.
4. The paper sizes to the text, then grows 10%. No fixed height.
5. Text distribution is judged per title. The white setup line is optional and costs headroom.
6. **The host is generated from the fixed reference set. The face is never covered.**
7. **The trait handwriting is never generated. Published library only.**
8. The logo is the unaltered PNG, 3×, bottom-left, lifted clear of platform UI.
9. Filenames are `v1`, `v2`, `v3` — only Bart approves, so only Bart names anything approved.

---

## 10. Reconciliation notes

### 10.1 Filenames that no longer describe their contents

| File | Problem |
| :--- | :--- |
| `SOP_HU_IG_Screenshot_Torn_Paper_v2.md` | Says "Screenshot." The screengrab method is retired. Contents need auditing against §6 and the file renaming. **Not yet done.** See §12 item 1. |
| `build_hu_ig_thumbnail.py` | If it contains frame-grab or headliner-padding logic, that code is now dead. Needs a read. See §12 item 2. |

### 10.2 `Salvadore` vs `salvatore`

| Context | Spelling | Path |
| :--- | :--- | :--- |
| Local Mac Studio (Joan's machine) | `Salvadore` | `Salvadore - art department/` |
| GitHub repo | `salvatore` | `salvatore-art-department/` |

Both are live. GitHub URLs use the lowercase hyphenated form.

### 10.3 Liar Liar — `ig_v2` vs `ig_v3`

§5 cites `liar-liar/ig_v2.jpg`. The file separately supplied is
`LiarLiar_thumbnail_approved_ig_v3.jpg` — a different name, containing the status word
"approved" that §9 rule 9 forbids. **Unresolved.**

### 10.4 The two specs disagree about parchment edges, deliberately

| | 9:16 (this file) | 16:9 (brand kit §6) |
| :--- | :--- | :--- |
| Parchment edges | Always torn, all four | Torn **or** scissor-cut, per the space the text needs |
| Red | None | Teacher Red `#D62828` for the trait circle |
| Host plate | Generated, 9:16 native | Generated, 16:9 native |

Check the aspect ratio first, then pick the rule. Do not reconcile these.

### 10.5 Documents that contradict v5 and must be updated

| Document | Stale text |
| :--- | :--- |
| `brands/handwriting-university.md` §5 | Cites the logo as `HU logo new 2026 Watermark.png` — spaced name, retired 2026-08-10 |
| `brands/handwriting-university.md` §7 | Points at `HU_Thumbnail_Creation_Process.md` and calls the 9:16 method a screenshot build |
| `brands/handwriting-university.md` §8.1 | Still asks Gemini for a one-pass assembly including handwriting and headline |
| `brands/handwriting-university.md` §12 item 7 | "Approved presenter photo library" — now answered by §0 and §6.2 |
| `HU_Video_Publishing_Pipeline_V7` Phase 4 | "Headshots — real only"; "PIL hand-composite banned" without a definition |

---

## 11. Asset manifest — verified against `main`, 2026-08-14

**Present:**

- [x] `SOP_HU_IG_Screenshot_Torn_Paper_v2.md` *(name misleading — §10.1)*
- [x] `build_hu_ig_thumbnail.py`
- [x] `HU_logo_new_2026_Watermark.png` — **underscores.** Renamed 2026-08-10; the spaced name no longer resolves.
- [x] All seven host reference images listed in §0
- [x] `thumbnail_IQtest_ig_approved.jpg`
- [x] `Thumbnail.HU_hates-all-men-host-photo-sample.png` *(screengrab sample — now historical only)*

**Missing — reference builds:**

- [ ] `liar-liar/ig_v2.jpg`
- [ ] `true-optimists-write-like-this/ig_v6.jpg`
- [ ] `vanity-nobody-likes-him/ig_v7.jpg`

Not blocking a build; blocking a *review*.

**Missing — fonts, only if the build runs off-Mac:**

- [ ] `Gelasio-Bold.ttf` — Georgia substitute
- [ ] `Anton-Regular.ttf` — Impact substitute, only if setup lines are used

**Do not upload:** Georgia Bold or Impact (proprietary); files with status words in the name;
re-exported or "cleaned" versions of the logo.

---

## 12. Open items

1. **Audit `SOP_HU_IG_Screenshot_Torn_Paper_v2.md` against v5.** It is named for and probably
   written around the retired screengrab method. Read it, strip the dead procedure, rename.
2. **Audit `build_hu_ig_thumbnail.py`.** Frame-grab handling, hairline detection on found frames,
   and headliner padding are now dead code paths. The clearance assert (§6.4) must stay.
3. **YouTube Shorts safe zones are unmeasured.** §7's bands came from Instagram and TikTok.
   Measure YouTube's crops across feed, channel grid, search, and watch page.
4. **Synthetic-media disclosure — verify, do not assume.** YouTube has required disclosure for
   realistic altered or synthetic depictions of real people in some contexts. This is Bart's own
   likeness used with his own consent, which is the straightforward case, but the current policy
   should be checked directly before this scales. **Flagged, not researched.**
5. **Ratify §6.** It is an agent draft implementing Bart's verbal ruling. Nothing in it is
   Bart's own wording.
6. **Update the five stale documents in §10.5.**
7. **Liar Liar filename** — `ig_v2` vs `ig_v3`, and the banned status word. See §10.3.
