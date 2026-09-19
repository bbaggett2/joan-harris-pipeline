# 08 — HU Vertical 9:16 cut
**V1 · 2026-09-19 · Governs: the vertical-cut worker on the Mac and the `vertical_url` field**
**Status: LIVE for HU.** The QDE lane retired this file. HU needs it — see the rule below.

## Why this file is alive for HU and dead for QDE

QDE's `10_METRICOOL_DRAFTS_V3.md` sends `long_url` to **all four** drafts. That was a deliberate wiring fix, not a design choice: three drafts read a `vertical_url` field that **no node in any of the three workflows ever assigned**, so TikTok, Instagram and the Facebook REEL were silently skipped on every run since the workflow was built.

Bart's ruling for HU, 2026-09-19: **build the missing wiring.** HU's short-form drafts take the vertical cut, and this file is the node group that produces and registers it.

⛔ **Instagram rejects horizontal video outright.** Sending `long_url` to the IG draft does not degrade the post — it fails it. That is the concrete cost of copying QDE's current wiring.

## Governing doc
`betty-social-media-manager/Betty_SOP_VideoSmimeo_IG_Resize_Normalize_v<n>.md`
⚠️ **Named as authority but never committed to `main`.** By this repo's own rule that is a blocked job. Until it lands, this file's recipe is the whole spec.

## Steps

1. **Look for an editor-made vertical cut first** — filename contains `TIKTOK`, `Vertical`, or `9x16`. **ffprobe it**, never trust the name. Confirmed 1080×1920 → use it, skip to step 3.

2. **Otherwise build the blurred-fill cut** on the Mac:

```bash
ffmpeg -y -i <land>.mp4 -vf "split[a][b];\
[b]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:6[bg];\
[a]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1" \
-c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 128k <VID_ID>_IG_9x16_v1.mp4
```

Never crop the face. Version `v1`/`v2`/`v3` — **never "final"**. Verify with ffprobe; a "moov atom not found" error means an incomplete download, so re-run.

3. **⭐ Register it on the payload as `vertical_url`.** This is the step QDE never had, and the whole reason this file exists. Upload the cut to the HU assets folder, then set `vertical_url` to its Drive download URL. File 10's `short_media` reads this field and nothing else.

4. **Record the full-length cut's byte size.** Not a routing decision — it is the one thing that can block the Facebook POST at file 10. Over 500 MB → compress (CRF 20 took 543 MB → 170 MB in a known case). **Compressing for a size cap is not trimming.** The cut stays full length.

## Long and short cuts version independently
`S-V1` is **not** stale because `L-V6` exists — they are different deliverables. The long cut carries YouTube and the Facebook POST; the short vertical cut carries TikTok, Instagram and the Facebook REEL. Both are used.

## Stops
- No vertical cut exists and none can be built → **the three short-form drafts are not created**, flag `NO_VERTICAL`. ⛔ Never substitute a landscape master into a Reel or an IG post. The Facebook POST still goes.

## Flags
`NO_VERTICAL` · `VERTICAL_ASPECT_WRONG` · `FB_POST_OVER_CAP`
