# 08 — Vertical cut and compression (the Mac step)
**V2 · 2026-09-19 · Operational authority: `betty/Betty_SOP_VideoSmimeo_IG_Resize_Normalize_v1.md`. No n8n node governs this lane.**

n8n Cloud cannot run ffmpeg. This work happens on Bart's Mac Studio, where ffmpeg, ffprobe and rclone are installed under `/opt/homebrew/bin`.

## What changed in V2 — the mechanism was described wrongly

V1 described a **launchd daemon** called `qde_ffmpeg_worker.sh` polling the sheet every 5 minutes for rows at `NEEDS_CUT` / `NEEDS_COMPRESS`, flipping them to `READY`, with a Schedule trigger in n8n resuming the run. V1 itself marked the resume trigger "not yet drawn in v1 JSON — build item."

None of that machinery exists, and none of it is how the work actually gets done:

| V1 claimed | Verified 2026-09-19 |
|---|---|
| launchd worker `qde_ffmpeg_worker.sh` | Not registered. The only betty launchd jobs are `com.betty.youtube-worker` and `com.betty.rick-worker` |
| `Needs ffmpeg?` IF node, `Hand to Mac worker` node | No such nodes in any of the three workflows. None mentions ffmpeg at all |
| Row statuses `NEEDS_CUT` / `NEEDS_COMPRESS` | Not referenced anywhere in the workflows |
| Schedule trigger resumes on `vertical_url not empty` | No such trigger. `vertical_url` is read in two places and written in none |

**What is real:** ffmpeg work on this Mac has been running since 2026-06-10 and is performed by **Video-Smimeo**, Betty's video publish/syndication sub-agent, invoked **through Desktop Commander** and following the SOP named above. Evidence on disk: `SAMPLE_spot-a-liar_vertical_blurfill_v1.mp4` (May), `Aggressiveness_GraphoDeck_V3_IG_9x16.mp4` (June), the `IG_Reencode/` set of `_src` → `_IG1080` pairs (June), `yt_work/batch4/` with `-land` → `-9x16` pairs (July), and `ffmpeg_0816_delivery.log` (August).

So this is an **agent-invoked SOP, not a daemon, and not an n8n step.** It runs out of band from the publish workflow, on demand, before or after a row moves.

## When it fires

A finished video cannot go to Instagram for one or more of three reasons — file size (IG's ~1 GB ceiling), aspect ratio (Reels reject horizontal with "Media upload failed: Fatal"), or duration. Fix only the one that applies.

**The standing lesson:** "too big for IG" almost always means the **shape**, not the bytes. A compress-only pass that keeps 1920×1080 looks identical and still gets rejected. Default to the vertical reframe for IG. (First run, VID-0871, 2026-06-10: 1.31 GB → 196 MB compress-only was rejected; the 1080×1920 blur-fill at 128 MB worked.)

Note also that "Fatal" on an IG upload is frequently **duration** — the real ceiling is 3 minutes, not 90 seconds.

## The two recipes

The commands live in the SOP and are not duplicated here, so there is one place to edit them:

- **Compress only**, native landscape — when size is the only problem, or it is a long feed video.
- **Vertical 9:16 blurred-fill** — pads to vertical with a blurred copy behind, so the whole frame stays visible. **The face is never cropped. Hard rule.**

Resolution policy: output at the highest resolution the source supports — 4K vertical at 2160×3840 when the master is 4K — and downscale to 1080 only where the platform requires it. **Never upscale.**

## How this squares with "publish native landscape"

They are not in conflict. The standing rule is that QDE and HU videos publish in their **native** aspect — there is no routine re-cut pipeline turning every landscape video into a vertical one. The blur-fill pad is an **Instagram-specific accommodation** applied when IG rejects a file, not a general re-cut step. File 02's `aspect` feeds `yt_format` (Short vs long-form description) and nothing else.

## What the publish workflow does today

Nothing routes to this lane. `Assemble drafts` builds all four Metricool drafts from `long_url` — the file the row actually has — because no node ever registered a vertical asset onto a row (file 10).

If vertical assets should feed the short-form drafts, the missing piece is **registration**, not encoding: something must write the finished `_IG_9x16` file's Drive URL onto the row. `short_media` in `Assemble drafts` is the single line that would switch back to it.

## Naming and guardrails

- Suffix outputs `_IG` or `_IG_9x16` so they are never confused with the editor's master.
- Version `v1` / `v2`; **never** "final".
- **Never delete** the source or any prior cut.
- Compression is not trimming. Full length unless a trim was explicitly agreed.

## Refinement hook

ffmpeg recipes, resolution policy, Reel-vs-Feed decision → **the Video-Smimeo SOP**, not this file.

Whether n8n should ever trigger or consume this lane → this file and file 10.
