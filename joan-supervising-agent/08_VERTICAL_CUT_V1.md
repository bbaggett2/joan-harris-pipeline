# 08 — Vertical cut and compression (the only Mac step)
**V1 · 2026-09-15 · Governs n8n node: `Needs ffmpeg?` (IF) · `Hand to Mac worker` and the Mac Studio worker `qde_ffmpeg_worker.sh`**

n8n Cloud cannot run ffmpeg. This is the single hand-off to the Mac, and it goes through the sheet, not through a person.

## n8n side
`Needs ffmpeg?` IF:
- landscape AND no `vertical_url` on the row → status `NEEDS_CUT`
- `over_fb_cap` → status `NEEDS_COMPRESS`
- both → `NEEDS_CUT` (the worker does both when it sees a landscape file over cap)
Row is written and **the run ends.** The worker flips it back to `READY`; a sibling *Schedule* trigger (every 15 min, `status = READY AND youtube_id empty AND vertical_url not empty`) resumes it from `VTT: fetch`. Nothing waits. *(Resume trigger not yet drawn in v1 JSON — build item.)*

## Mac worker — `qde_ffmpeg_worker.sh` (launchd, every 5 min)
1. Read `videos` rows where `status IN (NEEDS_CUT, NEEDS_COMPRESS)` (Sheets API via a tiny Python script).
2. Download the file by `drive_file_id` (rclone).
3. `NEEDS_CUT`: build the blurred-fill vertical — never crop the face:
```bash
ffmpeg -y -i in.mp4 -vf "split[a][b];[b]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:6[bg];[a]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1" -c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 128k <vid_id>_IG_9x16_v1.mp4
```
4. `NEEDS_COMPRESS`: `ffmpeg -y -i in.mp4 -c:v libx264 -preset medium -crf 20 -c:a aac -b:a 128k <vid_id>_L_compressed.mp4` — full length, always. Compression is not trimming.
5. Upload to `assets_folder_id`, share by link, write `vertical_url` / `vertical_file_id` (and `long_url` if compressed), set `status = READY`.
6. Never delete anything. v1/v2/v3 filenames, never "final".

## If the worker is down
Rows sit at `NEEDS_*`. File 12's daily sweep posts to Slack: "n rows waiting on the Mac worker for > 2 h."

## Refinement hook
ffmpeg recipes → here. Whether a vertical cut is required at all → file 02 routing table.
