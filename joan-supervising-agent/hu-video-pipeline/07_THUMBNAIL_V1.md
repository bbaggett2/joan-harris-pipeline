# 07 — Thumbnails
**V1 · 2026-09-19 · Governs n8n nodes: `Thumbnail: job` · `Write thumbnail job` · `Wait for thumbnail worker` · `Parse thumbnail result` · and the HU thumbnail worker on the Mac**

## This is the largest structural difference between the HU and QDE lanes

**HU thumbnails cannot be built inside n8n.** QDE generates its thumbnail with `gpt-image-1` in an n8n node. HU cannot:

- **Gemini is unreachable from n8n Cloud and from the agent sandbox** (proxy returns 403). It runs on the Mac only.
- **HU handwriting must be real.** `brands/handwriting-university.md` §6 item 2: the trait visual comes from Bart's published trait library. **Never AI-generated handwriting strokes. Absolute rule.**
- **The typeface is named and closed.** `CollegiateFLF` + `CollegiateOutlineFLF`, both faces over each other, no substitutes. If the fonts are missing the build **stops**; it does not pick something close.

So the HU thumbnail follows the same side-car pattern as file 09: n8n emits a **job**, the Mac builds the image, the workflow resumes by webhook. **Do not add an image-generation node to the HU workflow.**

## ⚠️ UNRESOLVED — needs Bart before this can be built

`HU_Video_Publishing_Pipeline_V15.md` Phase 4 listed `BANNED: PIL hand-composite · AI handwriting · red`. Two of those contradict the brand kit:

| V15 says | The brand kit says |
|---|---|
| PIL hand-composite banned | §7: the 9:16 build **is** a deterministic Python script (`build_hu_ig_thumbnail.py`), explicitly *"not a prompt — do not hand it to an image model."* The standing thumbnail note also says to composite the HU logo in PIL rather than rely on Gemini |
| red banned | §3 defines **Teacher Red `#D62828`** for magnification circles; §6 item 2 requires the trait letter *"circled or highlighted in bright teacher-red pen."* §3's real rule is narrower: **no red on 9:16, red permitted on 16:9** |

"AI handwriting banned" is not in conflict — both sources agree, absolutely.

**Until Bart rules, build to the brand kit** (it is the named single source of truth for artwork) and flag the divergence. Do not silently pick.

## Deliverable A — YouTube 16:9

Canvas **1280×720**. Maximum three visual focus elements.

1. **Presenter, right ~40%** — waist-up, entire head visible, never cropped, looking into camera. Expression drawn from the transcript.
2. **Trait visual, left ~40%** — one magnified real handwritten letter or word from the published library, circled. Crop the library card to the strokes only; its green border, banner and arrows are deck design, not HU brand.
3. **Headline, upper left** — 3–5 words max, ALL CAPS, `CollegiateFLF` filled white with `CollegiateOutlineFLF` over it in HU Navy, inside a slightly tilted parchment rectangle.
4. **Logo** — `HU_logo_new_2026_Watermark.png` (underscores), small, bottom-left or top-right. **Bottom-right stays clear** for the YouTube timestamp. Used unaltered.
5. **Background** — dark cinematic study at dusk. Generated as its own separate Gemini step; asking one prompt to assemble background, text and handwriting together is what causes drift.

Must be readable at 168×94px.

**Path A — generated host — is the default. An agent never elects Path B.** Absence of instruction means Path A. One video, one path: the 16:9 and the 9:16 must use the same host source or the pair will not match.

## Deliverable B — Instagram Reel cover, 9:16
1080×1920. Style locked 2026-07-11. **No red on 9:16.** Two variations.

## Hard requirements carried from today's QDE fixes

⛔ **Output must be 16:9.** The QDE generator defaulted to 1536×1024 and YouTube silently kept its own auto-frame on every upload. `gpt-image-1` has **no 16:9 size** — only 1024×1024, 1536×1024, 1024×1536 — which is why "just set the generator to 1280×720" is not achievable there. HU's build script sets the canvas directly, so it has no excuse.

⛔ **Filenames are sequential: `<VID_ID>_thumb_v<n>.png`**, `n` computed from existing files. The QDE nodes hardcode `_thumb_v1.png`, so every run writes another "v1" and Drive allows the duplicate name. Bart wants variations numbered so humans can review them — do not inherit the hardcode.

⛔ **The upload step must prove it.** See file 09: `yutu` refuses an absolute `--file` path, prints its usage text, and exits 0 without calling the API.

## Flags
`THUMB_NOT_16X9` (hard stop) · `THUMB_FONTS_MISSING` (hard stop) · `THUMB_TRAIT_NOT_FROM_LIBRARY` (hard stop) · `THUMB_WORKER_TIMEOUT`
