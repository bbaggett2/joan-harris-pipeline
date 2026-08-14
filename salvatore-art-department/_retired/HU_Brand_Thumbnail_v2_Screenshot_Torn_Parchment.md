# HU Brand Thumbnail v2 — The Screenshot + Torn Parchment Method

**Version:** 2
**Brand:** Handwriting University (HU)
**Status:** **ALTERNATE PATH — NOT THE DEFAULT.** Opt-in, by Bart's explicit election only.
**Default path:** `HU_Thumbnail_Creation_Process_v5.md` — generated host. Use that unless told otherwise.
**Lives at:** `salvatore-art-department/HU_Brand_Thumbnail_v2_Screenshot_Torn_Parchment.md`
**Rewritten:** 2026-08-14

---

## READ THIS BEFORE ANYTHING ELSE

There are two host-image paths. They do not mix.

| | Path A — **DEFAULT** | Path B — this file |
| :--- | :--- | :--- |
| Host image | AI-generated likeness of Bart | Real frame grabbed from the actual video |
| Governing file | `HU_Thumbnail_Creation_Process_v5.md` | This file, plus v5 for everything shared |
| When | **Always, unless Bart says otherwise** | Only when Bart elects it for a specific video |
| Who decides | Nobody — it's the default | **Bart, per video, in writing** |

**An agent never chooses Path B.** Absence of instruction means Path A. If you are unsure which
path you are on, you are on Path A.

### The one rule that matters most

**One video, one path. Never both.**

The YouTube 16:9 and the vertical 9:16 for the same video must come from the same host source.
A generated Bart on the thumbnail and a photographic Bart on the Reel cover will not match —
different skin rendering, different lighting logic, a subtly different face — and side by side in
a feed that mismatch reads as sloppiness faster than either version alone reads as good.

If Bart elects Path B for a video, **both** deliverables for that video use Path B.

---

## What this file does and does not contain

This document is an **override**, not a second SOP. It replaces exactly one section of v5 and
inherits the rest.

| Topic | Where it lives |
| :--- | :--- |
| **Host image sourcing** | **This file, §1–§5. Replaces v5 §6 entirely.** |
| Deliverable order, canvas sizes, platform specs | v5 §0.5 — unchanged |
| Colour palette | v5 §2 — unchanged |
| Lettering, fonts, emboss | v5 §3 — unchanged |
| The torn edge — fractal noise, octaves, corner taper | v5 §4 — unchanged |
| Parchment sizing, the three layouts, where words go | v5 §5 — unchanged |
| The HU logo, placement, safe zones | v5 §7 — unchanged |
| Trait handwriting — published library, never generated | brand kit §6 item 2 — unchanged, **applies on both paths** |
| Build checklist | v5 §8, with steps 2–3 and 9 swapped for §5 below |

**Nothing above is restated here.** Duplicating craft rules across two files is how they drift
apart. If you need the tear algorithm, open v5 §4. Do not work from memory of it.

---

## 1. When Path B is the right call

Bart elects this path. These are the situations that tend to justify it — they are context for
his decision, not criteria an agent applies.

- The video contains a **moment** worth showing — a specific reaction, gesture, or expression that
  happened on camera and would be diminished by being described to a model.
- The footage is unusually good, well-lit, and well-framed.
- The video's credibility depends on it being visibly the real recording.
- Bart simply wants the the user to click and see the same host clothes, background, and consistency from click to watching the video for this one.

If none of these is stated, Path A applies.

---

## 2. The frame decides everything — choose it first

No geometry rescues a bad grab. This is the whole reason Path B is harder than Path A: on Path A
you specify the composition, here you have to find it.

**Headroom is mandatory.** Bart must sit low enough in frame that the parchment has quiet dead
space above his hair. A tight close-up where his head fills the frame **cannot work** — filling a
vertical canvas from it drives his forehead under the paper. This failed four times before a
proper frame fixed it in one.

**Face is untouchable. Hair may be covered.** These are different limits — measure both. In the
original reference frame, hair tips began at y≈437 and skin at y≈635, giving ~200px of hair the
paper could use. The check that matters: the *lowest tear tooth*, which cuts deeper than the paper
edge, must clear the **forehead** — not merely the hairline.

**Reject early.** A bad grab discovered at compositing time has already cost you the build. Judge
headroom and expression before anything else happens.

---

## 3. Detection, not specification

On Path A the build *verifies* clearance on a plate whose composition was requested. Here the
build must first **find** the hairline and the forehead in a frame nobody designed, then verify
against them. Both steps are required, and the detection step is where this path fails.

Treat a detection result as a measurement to be checked, not a fact. If the numbers look
implausible for the frame, they are wrong — look at the image.

---

## 4. Landscape frames: pad, don't reject

A 16:9 frame is not an automatic reject for the 9:16 deliverable. Scale it to a chosen size, crop
on the face, **bottom-align**, and **extend the headliner upward** to manufacture headroom.

The fill cannot be a flat block. Sample the top few rows and walk a gentle darkening gradient with
a little grain — a real headliner darkens away from the glass, and a flat fill reads instantly as
fake. This only works on quiet, uniform dead space, so check that the top rows are low-variance
before attempting it.

This is exactly how the "Liar Liar" cover was built from a wide frame.

> **This technique is Path B only.** It exists because a screengrab is the only frame available.
> On Path A, generate at the target aspect ratio instead — v5 §0.5 Step 2 forbids padding a
> landscape plate into a vertical canvas.

---

## 5. Build steps that differ from v5 §8

Run v5 §8 as written, with these substitutions:

**Step 1 — YouTube 16:9**

- *v5 steps 2–3 (generate plate, recognition check)* → **replaced by:** grab the frame from the
  actual video per §2 above; reject bad frames early.
- Everything else in v5 §8 Step 1 is unchanged, including the trait card, the composite order,
  the 2 MB ceiling, and Bart's approval gate.

**Step 2 — Vertical 9:16**

- *v5 step 9 (regenerate plate at 9:16)* → **replaced by:** grab a 9:16-suitable frame, or pad a
  landscape frame per §4.
- *v5 step 10* onward is unchanged — layout by title length, type sizing, tear, composite,
  asserts, `ig_v1.jpg`, Bart approves.

Filenames are identical on both paths: `yt_v1.jpg`, `ig_v1.jpg`, incrementing, never a status
word, only Bart names anything approved.

---

## 6. Provenance and reconciliation

### 6.1 Where this content came from

§2, §3, and §4 are Bart's, carried forward verbatim in substance from
*HU Brand Thumbnail — The Screenshot + Torn Parchment Method* (v4) §6, which v5 retired. Nothing
in them is new. §0, §1, and §5 are routing and ordering, drafted by an agent on 2026-08-14 to
implement Bart's ruling that the screengrab method be preserved as an opt-in alternate rather than
deleted.

### 6.2 This partially un-retires a v5 retirement

v5's retirement table lists "Pull the frame from the actual video" as retired, and says the
screengrab method is retired *entirely*. That is now too strong. **v5's retirement table needs
one line amended** to read that the screengrab method is demoted to an opt-in alternate path
governed by this file — not deleted. Until that edit is made, v5 and this file disagree.

Two v5 retirements are **unaffected** and still stand on both paths:

- **"Headshots — real only" is still retired.** It was a rule about generated hosts being
  forbidden. Path B uses real frames by nature, so the rule is moot here, not revived.
- **The trait handwriting is still never generated.** Published library only, both paths.

### 6.3 Files whose names now mislead

`SOP_HU_IG_Screenshot_Torn_Paper_v2.md` and `build_hu_ig_thumbnail.py` were both written when the
screengrab was the only method. With two live paths, their frame-handling code and procedure are
Path B material, not dead code as v5 §12 item 2 assumed. **v5 §12 item 2 needs amending** — the
frame-grab and headliner-padding logic must be *preserved and gated*, not stripped.

---

## 7. Open items

1. **Amend v5's retirement table** so it describes the screengrab as demoted, not deleted. See §6.2.
2. **Amend v5 §12 item 2.** Frame-grab, hairline detection, and headliner padding in
   `build_hu_ig_thumbnail.py` are live Path B code. Gate them behind a path flag; do not delete.
3. **Add a path flag to the build.** The script should take the path as an explicit argument and
   record it in the output, so an agent cannot silently mix paths within one video.
4. **Record the elected path in ClickUp** on any video where Bart chooses Path B, so the 9:16
   build later in the week does not default back to Path A and mismatch the pair.
5. **Reference builds still missing from the repo** — `liar-liar/ig_v2.jpg`,
   `true-optimists-write-like-this/ig_v6.jpg`, `vanity-nobody-likes-him/ig_v7.jpg`. All three are
   Path B outputs and are the only visual record of what this path produces when it works.
