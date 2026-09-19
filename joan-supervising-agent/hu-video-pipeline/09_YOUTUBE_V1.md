# 09 — YouTube upload, thumbnail, captions
**V1 · 2026-09-19 · Governs n8n nodes: `Build YouTube job` · `Write YouTube job` · `Wait for local YouTube worker` · `Parse worker result` · and `worker.py` on the Mac**

## Architecture
n8n Cloud cannot run `yutu`, `rclone` or `ffmpeg` — no Execute Command node. So n8n writes a **job JSON** into a Google Drive queue; the launchd worker `com.betty.youtube-worker` on the Mac claims it, downloads the media, uploads to YouTube, sets the thumbnail, inserts captions, and resumes the workflow through the wait-webhook.

The Mac must be on and logged in. `launchctl kickstart -k gui/$(id -u)/com.betty.youtube-worker` restarts it.

## ⛔ B1 — the brand-safety requirement, before anything else

`worker.py` as built hardcodes the **QDE** credential and one shared queue:

```
CRED_PATH    = ~/.config/betty/youtube/qde_client_secret.json
TOKEN_PATH   = ~/.config/betty/youtube/qde.token.json
QUEUE_REMOTE = "gdrive:youtube_upload_queue"
```

**An HU job dropped into that queue as-is uploads to the QDE channel.** The upload is private, so nobody would notice until someone went looking. This is the highest-risk item in the HU build.

Required before the first HU run:

1. **Its own queue folder.** HU never shares `youtube_upload_queue`.
2. **The job carries its own identity:** `brand: "HU"`, `yutu_credential: "hu_client_secret.json"`, `yutu_token: "hu.token.json"`, `expected_channel_id: "UCG-DLule9ZSStBdc5gSEoCw"`.
3. **A per-job credential lookup** in the worker, defaulting to QDE only when `brand` is absent, so existing QDE jobs are untouched.
4. **A hard assertion after upload:** read `channelId` back with `videos.list(part=snippet)` and compare to `expected_channel_id`. A mismatch stops the job loudly. **Never a warning.**
5. **Prove the patch on a QDE job first**, before any HU job exists. If the QDE lane breaks, stop.

HU has its own GCP project (`yutu-handwriting-university`) with its own ~10k/day quota, so HU traffic never starves QDE. A `403 quotaExceeded` on HU means genuine HU volume.

## Upload
Via the `yutu` CLI from a local path — never YouTube Studio, never a Chrome session. rclone the render down first; `yutu` needs a real local file.

- Channel: `UCG-DLule9ZSStBdc5gSEoCw` (`@handwritinguniversity`)
- Visibility: **PRIVATE**. Never Unlisted, Public, or Scheduled at upload time.
- Title and description set **verbatim** from the copy package. Check for markdown artifacts first.
- ⛔ **Never post to the Joan Harris channel `UCbDGkQdUKEgeDTDvqVEWoWA`.**

**The upload ledger is defeated by a rename.** Its key is `VID_ID|drive_file_id`, so the same physical file renamed to a new VID_ID uploads twice — this happened on 2026-09-19 (`DUeiBACO-Xc` then `1gHpJXJLDf0`, same bytes, same Drive ID). Add a secondary check on `drive_file_id` alone that warns when the same bytes were already uploaded under a different VID_ID.

## Thumbnail — two faults, both fixed 2026-09-19, both must carry into HU

**Fault 1 — `yutu` silently refuses an absolute `--file` path.** It resolves `--file` against `YUTU_ROOT` (default: cwd), prints its usage text to stdout, **never calls the API, and still exits 0**. This, not the aspect ratio, is why no custom thumbnail had ever reached YouTube. Proven by hand on `liXYA9k_HMo`: absolute path → usage text; `cd <dir>` + basename → `youtube#thumbnailSetResponse`, thumbnail live.

```
✅  cd {job_dir} && yutu thumbnail set --videoId {id} --file {basename} --yes --output json
⛔  yutu thumbnail set --videoId {id} --file /absolute/path.png ...
```

**Fault 2 — aspect ratio.** YouTube silently keeps its auto-generated frame when a custom thumbnail is not 16:9. The worker now centre-crops to 16:9 and scales to 1280×720 with ffmpeg before upload. For HU this should rarely fire — file 07's build script sets the canvas directly — but it stays as a safety net.

**Confirm it landed by reading it back.** `thumbnails.maxres` present at 1280×720 on `videos.list` is the proof. `rc == 0` is not.

## Captions — LAST YouTube step, after the thumbnail

⛔ Never upload captions before the thumbnail is set.

**The failure and its cause.** Every caption insert returned `status: failed / processingFailed`. Three explanations were tested and two were eliminated:

- **Transport is not the cause.** Four upload methods — curl form-data (what the worker uses), multipart/related, related+SRT, and resumable PUT — all returned `serving`.
- **VTT content is not the cause.** The real pipeline VTT for VID-4522 (58 cues, no overlaps, no zero-length cues, last end 62.795s inside a 64s video) served fine.
- **It is a readiness race, and `processingStatus` is not the signal.** VID-4522 waited 40s for `processingStatus: succeeded`, inserted, and failed. ~90 minutes later the same VTT, same call, same video returned `serving` on the first try.

**The fix: retry until the track serves.** Delete the existing track, re-insert, poll; on `processingFailed`, wait and repeat — 8 attempts, 60s apart. `syncing` does **not** count as success; only `serving` does.

Verify `trackKind: standard`, not `asr`.

## Resume
The worker POSTs back to the wait-webhook with `vid_id`, `youtube_id`, `youtube_thumbnail_set`, `youtube_captions_set`, `status`. Each of those booleans must come from a destination read, not from an exit code.

## Flags
`WRONG_CHANNEL` (hard stop) · `DUPLICATE_UPLOAD` · `THUMB_NOT_CONFIRMED` · `CAPTIONS_NOT_SERVING` · `WORKER_TIMEOUT`
