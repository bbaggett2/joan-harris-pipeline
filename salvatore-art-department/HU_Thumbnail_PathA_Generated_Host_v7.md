# HU Thumbnail — Path A: Generated Host

**Version:** v7 — matches the filename. Highest number is current.
**Last updated:** 2026-09-12
**Status:** **THE CURRENT OPERATING DOCUMENT FOR HU THUMBNAILS**
**Brand:** Handwriting University
**Method:** Two-pass — Gemini generates host + environment, PIL layers the brand
**Executor:** Claude via Desktop Commander on Joan's Mac Studio. n8n-ready.
**Merged:** 2026-08-14, from `HU_AI_GE_Thumbnail_instructions.MD` (2026-08-10) and
`HU_Thumbnail_Creation_Process_v5.md` (2026-08-14 draft, never committed)

> **Versioning:** the version is in the filename and the highest number wins. A new revision
> becomes `..._v8.md` and this file is deleted in the same commit. Cross-references never name an
> exact version — `Something_v<n>.md` means the highest-numbered one in that folder.

**Companion files — read alongside, do not duplicate:**

| File | Scope |
| :--- | :--- |
| `HU_Thumbnail_Constants_v<n>.md` | **The 9:16 numbers.** Tear octaves, paper sizing, logo coordinates, fonts, asserts. **If a number appears there and here, that file wins.** |
| `HU_Thumbnail_16x9_Constants_v<n>.md` | **The 16:9 numbers.** Canvas, margins, keepouts, type sizes, asserts. Same precedence rule. |
| `brands/handwriting-university.md` §6 | The 16:9 layout spec |
| `HU_PathB_Frame_Acquisition_v<n>.md` | Path B — screengrab, opt-in only |
| `HU_Thumbnail_Step_Map_v<n>.md` | n8n step contracts |

---

## What changed in v7

1. **Five dead pointers fixed.** The companion table and §6 named files that have since been
   deleted or replaced. All now version-less.
2. **Two approval gates removed.** §8 ended "Human gate. Stop here"; §9 added a "second human
   gate." The publishing pipeline replaced four per-phase sign-offs with **one review**, done on
   the private YouTube video and the Metricool drafts. Salvatore now builds both deliverables and
   hands off once.
3. **A self-contradiction corrected.** §6 explains at length that `--format 16x9` never existed —
   and then §9 step 4 said to run Pass 2 with `--format 9x16`. Same fiction, same file. See §9.
4. **Header version now matches the filename.**

**Unchanged:** every Gemini prompt, asset path, trait-library rule, drift control and QA item — and
every place Bart appears as the person who *made* a ruling.

---

## 0. Merge record — what came from where

This file replaces two documents that described the same method differently.

| Source | What was kept | What was corrected |
| :--- | :--- | :--- |
| `HU_AI_GE_Thumbnail_instructions.MD` | The two-pass structure, input variables, CLI invocations, retry-on-drift rule, Drive upload, Slack delivery | Asset paths (§3 below); logo filename; logo no longer passed to Gemini; routing rule tightened |
| `HU_Thumbnail_Creation_Process_v5.md` | Path routing, likeness-drift controls, trait-library rules, composition specs, provenance discipline | Its claim that the screengrab was "retired entirely" — it is demoted to opt-in, not deleted |

**Both source files are retired.**

**Provenance.** The two-pass method and the "no typography in the Gemini prompt" rule are Bart's,
from the 2026-08-10 file. The likeness-drift controls in §7 are an agent draft implementing his
2026-08-14 verbal ruling and are **`[UNRATIFIED]`**.

---

## 1. Path routing — read before anything else

**Path A (this file) is the default. An agent never elects Path B.**

Absence of instruction means Path A. If you are unsure which path you are on, you are on Path A.

Path B — a real frame grabbed from the video — is used **only when Bart elects it for a specific
video, in writing.** The earlier criterion "use the screenshot method when a real expression is
critical" is **withdrawn**: it invited an agent to make an aesthetic judgment about Bart's own
likeness, which is not an agent's call.

> **Path B election stays with Bart, not the reviewer.** Choosing how the host is portrayed is a
> brand decision, not a quality check, so it did not move when the approval gates did.

**One video, one path.** The 16:9 and the 9:16 for a given video use the same host source. A
generated Bart on the thumbnail and a photographic Bart on the Reel cover do not match, and the
mismatch reads as sloppiness faster than either reads as good.

---

## 2. Input variables

Supplied in the trigger prompt, from Bart or from n8n.

| Variable | Description | Example |
|---|---|---|
| `VID_ID` | Video ID or slug number | `0812` |
| `SLUG` | Short descriptor for file naming | `fear-of-judgment` |
| `HEADLINE` | Main thumbnail text — **3–5 words** | `THEY CAN TELL` |
| `SUBHEAD` | Supporting line, optional | `from this one stroke` |
| `EXPRESSION` | Emotional register, **drawn from the transcript** | `intense, knowing, serious` |
| `BACKGROUND` | Environment | `dark collegiate study at dusk, dimly lit` |
| `TRAIT_CARD_PATH` | Local path to the published trait card | see §5 |

**`HEADLINE` and `SUBHEAD` are set exactly as Bart writes them.** Never tidy, normalise, correct,
or re-punctuate. If it looks like a typo, flag it and ship what he wrote.

---

## 3. Asset locations — CORRECTED

> The 2026-08-10 file described a folder tree (`assets/headshots/`, `assets/logos/`, `scripts/`)
> that **does not exist in the repository.** Everything is flat in `salvatore-art-department/`.
> Those paths are the reason a run fails at step one.

```
salvatore-art-department/
├── Bart-serious-clear-bluesuit.png                  ← PRIMARY headshot (--headshot)
├── BartBaggett72whitebackgroundB16A5244blue_B.jpg   ← clean isolate, default reference
├── B16A5236_revised_bart_red_smile.jpg              ← warm register
├── BartBaggett-serious-clear-bluesuit2.png          ← serious, alt angle
├── Bart_MG_1770_attorney_shot.png                   ← authoritative
├── Bartbaggett_MG_1881.jpg                          ← high-resolution reference
├── bartbaggett_MG_1827-labcoat.jpg                  ← QDE-leaning; use with care on HU
├── HU_logo_new_2026_Watermark.png                   ← logo. NOT passed to Gemini — see §4
└── build_hu_ig_thumbnail.py                         ← Pass 2, 9:16
```

**`generate_thumbnail.py` (Pass 1) is not in the repository.** It is referenced by the 2026-08-10
file and presumably exists on the Mac. **Verify before relying on this document.** See open items.

**Excluded permanently:** `bartbaggettB16A5236_red_background_smile2.png` (33MB) — causes colour
contamination in Gemini outputs. Never use it.

**Retired filename:** `HU_logo_navy_quill.png` does not exist. The logo is
`HU_logo_new_2026_Watermark.png`.

---

## 4. Pass 1 — Gemini generates host + environment ONLY

**Gemini's job is person and environment. Nothing else.**

Adding typography or brand elements to the Gemini call causes drift. This is Bart's own finding
and it is the reason the method is two-pass.

**The logo is NOT passed as a `--reference`.** The 2026-08-10 file did this, and it invites Gemini
to render a logo into the plate — which then has to be covered or discarded, and can produce two
logos in the final composite. The logo is a Pass 2 element only.

```bash
cd $REPO_ROOT

python3 scripts/generate_thumbnail.py \
  --headshot salvatore-art-department/Bart-serious-clear-bluesuit.png \
  --reference salvatore-art-department/BartBaggett72whitebackgroundB16A5244blue_B.jpg \
  --reference salvatore-art-department/B16A5236_revised_bart_red_smile.jpg \
  --prompt "$(cat /tmp/thumbnail_prompt.txt)" \
  --aspect 16:9 \
  --output outputs/$VID_ID-$SLUG-raw-16x9.png
```

### The prompt — brand kit §8.1, verbatim

Swap only the bracketed variable.

```text
A photoreal 16:9 image for a psychology and handwriting analysis channel.
SUBJECT: The male host on the right side (approximately 40% of the width), waist-up, entire head
fully visible and never cropped, looking directly into the camera. Expression and body language:
[EXPRESSION].
BACKGROUND: Dark cinematic collegiate setting at dusk — study, library, or Ivy League campus —
soft lighting, high contrast, genuine photographic depth, non-distracting.
COMPOSITION: Leave the left ~40% of the frame quiet and uncluttered. Leave clear space in the
upper left. No text anywhere in the image.
NO TEXT. NO HANDWRITING. NO LOGO. NO GRAPHIC OVERLAYS. No brown dominant tones.
```

**Reject and regenerate** if the plate contains text, handwriting, a parchment block, or a logo.
Do not paint over them.

**Composition for 9:16** (later, at §9): host positioned low in frame, top third quiet dead space
for the parchment.

---

## 5. The trait card — never generated

The magnified handwriting **always** comes from published material in Bart's library. Brand kit §6
item 2. No exceptions, both paths.

**Library:** `https://drive.google.com/drive/folders/1_ZzlXw1Zr2hoT-2aW8NK1cbWq8L2j-gH`

| Folder | ID |
| :--- | :--- |
| **`grapho deck individual cards`** — 53 single-trait PNGs, the primary source | `18lfO4P8oJRpcKc_buT7ehjCz0PM6ERx_` |
| `graphodeck - all cards high rez` | `1Qkgk0pXR1_qEjeBiFGolzysX8YjtDID3` |
| `handwriting analysis graphics general folder` | `1kcsuW_t3K0iY0mh9eSkBCq1vGBYwYC14` |
| `graphodeck high rez images` | `1iTPj6mNUvIjn1eLiaOE1INkfd1EKYCbL` |

Cards are named `NNN_traitname.png`. **Read the card's own caption text** to confirm it matches the
video's claim before using it — select by trait, not by guesswork.

### Approved: pre-composited samples in the Y-chart folder

`Y chart handwriting samples for videos` — `1BV4U4uIMAxvZfu9w_NpFtTMaIzmBlTf9`

Bart approved these for thumbnail use, 2026-08-14. They are single traits already set on aged
paper, with no deck chrome to strip:

| File | Trait |
| :--- | :--- |
| `no-trust-paper.png` | retraced lower-loop *y* — does not trust anyone |
| `healthy-y-loop-paper.png` | full, healthy lower loop |
| `y-chart3-lowerzones.png` | lower-zone comparison |
| `y- hook-paper.png` | hooked lower loop |
| `y-triangles-paper.png` | triangle lower loop |

**Finished PNG and JPG files only.** That folder also holds `.psd`, `.tif`, `.mp4` cursive
animations, a folded-paper texture pack, and `.DS_Store`. Those are editor working files — never
thumbnail assets.

**Check the aspect before choosing.** `no-trust-paper.png` is 1500 × 326, a 4.6:1 strip. The
16:9 left-hand trait zone is roughly 512 × 720, portrait. Either crop tighter around the
letterform or run the sample as a horizontal band — do not stretch it. At 326px tall it also needs
roughly 2× upscale to fill that zone, where a GraphoDeck individual card supplies about 800px of
stroke height natively. **Match beats resolution when the trait is unambiguous; otherwise use the
deck card.**

> **Textured paper here is correct and is not a rule violation.** The "flat fill, no grain, no
> texture" rule in the constants file governs the **headline parchment block** only. A trait
> sample photographed or composited on real aged paper is approved and should not be rejected for
> having texture.

**Crop off the deck chrome.** Cards ship with a green border, a green trait banner, caption text,
and green pointer arrows. Crop to the handwriting strokes only; the teacher-red circle comes from
the build, not from the card. Green is not an HU brand colour.

---

## 6. Pass 2 — PIL layers the brand

**16:9 and 9:16 use two different scripts. They are not one script with a flag.**

| Deliverable | Script | Constants |
| :--- | :--- | :--- |
| YouTube 16:9, 1280×720 | `build_hu_yt_thumbnail.py` | `HU_Thumbnail_16x9_Constants_v<n>.md` |
| Vertical 9:16, 1080×1920 | `build_hu_ig_thumbnail.py` | `HU_Thumbnail_Constants_v<n>.md` |

```bash
python3 salvatore-art-department/build_hu_yt_thumbnail.py \
  --plate              outputs/$VID_ID-$SLUG-raw-16x9.png \
  --trait              <cropped trait from the approved library> \
  --logo               salvatore-art-department/HU_logo_new_2026_Watermark.png \
  --headline-font      ~/Library/Fonts/CollegiateOutlineFLF.ttf \
  --headline-fill-font ~/Library/Fonts/CollegiateFLF.ttf \
  --keyword-font       ~/Library/Fonts/CollegiateFLF.ttf \
  --logo-pos           top-right \
  --headline           "$HEADLINE" \
  --keyword            "$KEY_WORD" \
  --out                outputs/$VID_ID-$SLUG-yt_v1.jpg
```

**The two Collegiate faces are mandatory and enforced** — the build exits if anything else is
passed. Brand kit §4. `--headline-fill-font` is not optional: the outline face alone renders
hollow letters that fail at 168×94.

Run `--help` before invoking. **Do not copy a command line out of a document without checking it
against the script** — see the correction below.

PIL handles the parchment block, navy collegiate typography, the teacher-red trait circle, the HU
logo at its measured position, and drop shadows. All geometry lives in the constants files and is
not restated here.

Every run writes a **168 × 94 proof image** beside the output. Read it before handing off.

> ### Correction, 2026-08-14 — a command line in earlier versions was fiction
>
> v6 as first written, and `HU_AI_GE_Thumbnail_instructions.MD` before it, printed a Pass 2
> invocation of `build_hu_ig_thumbnail.py` with `--input`, `--headline`, `--subhead`, and
> `--format 16x9`. **None of those flags exist.** That script hardcodes `W, H = 1080, 1920`, has
> no `argparse` and no `__main__`, and `build()` is a Python function only. There was no 16:9
> build path at all — not a broken one, none. The command was transcribed from document to
> document and never run.
>
> `build_hu_yt_thumbnail.py` was written on 2026-08-14 to close that gap, and tested against a
> real Gemini plate before being documented. Its constants are **provisional** — derived in one
> session, not measured against a body of approved work.

> **PIL is the method, not a violation.** Older pipeline docs said "BANNED: PIL hand-composite"
> without defining the term, and agents have read it as "PIL is banned." **Hand-compositing** —
> eyeballing coordinates in a throwaway script — is banned. A committed, versioned build script
> that happens to use PIL is required. If you find yourself picking an x/y by eye, stop.

---

## 7. Likeness drift — the thing that breaks first `[UNRATIFIED]`

A generated likeness varies run to run. Nobody notices across one thumbnail. Everybody notices
across thirty, and by then the channel has quietly stopped looking like one person.

**Three controls, all required:**

1. **Fixed reference set.** Same references every time. Default: the clean isolate
   (`BartBaggett72whitebackgroundB16A5244blue_B.jpg`) plus one expression match. Do not swap
   references between videos in a batch.
2. **Locked descriptors.** Age, build, hair, and eye colour are fixed prompt text, never re-worded
   per video. Only wardrobe and scene change.
3. **Recognition check.** Put the new plate beside the last two published thumbnails. The question
   is **"is this the same man,"** not "is this a good image."

**Retry rule (Bart's, from 2026-08-10):** if face drift is detected, do **not** send. Re-run Pass 1
with the same headshot and a prompt emphasising likeness. **Up to 2 retries, then flag.**

⚠️ **This control now carries more weight than it did.** Under the single review, the human eye
that catches drift lands later — on the private YouTube video rather than on the plate. These
three controls are what stands between a drifting likeness and a redo. Do not treat the
recognition check as a formality.

---

## 8. QA — 16:9

Run this before building the 9:16, and again before handing off.

- [ ] Bart's face is recognisable — not a generic AI face
- [ ] Full head visible, not cropped; waist-up; looking into camera
- [ ] Expression matches the transcript's register
- [ ] Headline readable at 168×94px; 3–5 words
- [ ] Parchment is cream `#F5F5DC`, not grey or white; flat fill, no texture
- [ ] Trait handwriting came from the published library
- [ ] HU logo present, not dominant; **bottom-right clear** for the YouTube timestamp
- [ ] Under 2 MB; minimum width 640px; JPG, PNG or GIF
- [ ] Filename has no status word — `v1`, `v2`, never `final` or `approved`

**No gate here.** *v6 ended this section with "Human gate. Stop here. Do not build the 9:16 on an
unapproved host." The single review replaced it — build both, hand off once.*

---

## 9. Build the vertical, then hand off

1. Regenerate the plate at **9:16**, using the **identical reference set, wardrobe, and scene**.
   **Do not upscale, crop, or pad the 16:9.** Padding a landscape plate is a Path B rescue and is
   forbidden here.
2. Build with `build_hu_ig_thumbnail.py`. ⚠️ **That script has no CLI** — no `argparse`, no
   `__main__`, and **no `--format` flag**. Call `build()` directly, as the constants file's §6
   example shows. *v6 said "run Pass 2 with `--format 9x16`" four sections after explaining that
   exact flag was fiction. See open items.*
3. Run the asserts in `HU_Thumbnail_Constants_v<n>.md` §9 — particularly **lowest tooth clears the
   forehead**, not the hairline.
4. Upload both deliverables to
   `Handwriting University / Thumbnails / $VID_ID-$SLUG/`.
5. Post the handoff notice to Slack and stop.

```
🎬 *Thumbnails built — $VID_ID: $SLUG*

Headline: "$HEADLINE"
$SUBHEAD (if present)

16:9 YouTube: [link]
9:16 vertical: [link]

Both go with the video into the publishing pipeline. They are reviewed once,
on the private YouTube video and the Metricool drafts — no approval needed here.
```

**9:16 differs from 16:9 on three points:** parchment edges always torn on all four sides;
**no red**; canvas 1080×1920, JPG 92%+, 300 DPI.

> **YouTube Shorts safe zones are unmeasured.** The reserved bands in the constants file came from
> Instagram and TikTok. YouTube crops Shorts covers differently across feed, channel grid, search,
> and watch page. Check on a phone before publishing.

**Where the human is now:** the reviewer sees both thumbnails once, on the private YouTube video
and in the Metricool drafts. Making the video public and scheduling the drafts is the approval. A
rejected thumbnail re-runs its step alone and swaps on the live video — a redo, not a failure.
**The reviewer is a role, not a person.**

---

## 10. ClickUp closure

Status must be set to **`Closed`**. The Video Production lists carry only `Open`, `in progress`,
`Closed`. There is no "Done" or "Complete" — passing those strings fails. `Closed` releases the
next dependent step.

Task IDs are per-video. List `901818897770` is `_Sample Video JULY Temp`, the **template source**.
Resolve the task ID inside that video's cloned list. **Never write to the template.**

---

## 11. Open items

1. **`generate_thumbnail.py` is not in the repository.** Pass 1 cannot run from a clean clone.
   Commit it, or document that it is Mac-only and why.
2. ✅ **CLOSED 2026-08-14.** `--format 16x9` did not exist and neither did any 16:9 build path.
   Resolved by `build_hu_yt_thumbnail.py` + `HU_Thumbnail_16x9_Constants_v<n>.md`. Those constants
   are provisional and should be revisited after the first few approved thumbnails.
3. **Give `build_hu_ig_thumbnail.py` a CLI.** It is the only build in the chain that cannot be
   invoked from a command line, which is why fictional flags for it kept getting written down.
   An `argparse` front end with an explicit `--path` flag would close open item 4 at the same time.
4. **Gate the Path B code.** Frame-grab, skin detection, and `manual_scale` padding in
   `build_hu_ig_thumbnail.py` are live Path B logic — gate behind an explicit path flag, do not
   delete. Record the path in the output.
5. **`youtube-thumbnail-log.md` does not exist** in the repo. Create it or drop the reference.
6. **Ratify §7.** Agent draft implementing a verbal ruling — and now load-bearing, since the human
   eye on likeness moved later.
7. **Synthetic-media disclosure.** Path A generates a likeness of a real person — Bart, with his own
   consent, the straightforward case. Confirm current YouTube policy before this scales.
   **Flagged, not researched.**
8. **Reference builds missing:** `liar-liar/ig_v2.jpg`, `true-optimists-write-like-this/ig_v6.jpg`,
   `vanity-nobody-likes-him/ig_v7.jpg`. All are Path B outputs and the only visual record of the
   approved layouts.
