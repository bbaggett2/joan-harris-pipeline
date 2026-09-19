# 09 — HU YouTube upload, thumbnail, captions
**V2 · 2026-09-19 (evening) · Governs n8n nodes: `Build YouTube job` · `Write YouTube job` · `Wait for local YouTube worker` · `Parse worker result` · the ⚠️ incomplete-publish branch · and `worker.py` on the Mac · Replaces `09_YOUTUBE_V1.md`**

## Architecture
n8n Cloud cannot run `yutu`, `rclone` or `ffmpeg` — no Execute Command node. So n8n writes a **job JSON** into a Google Drive queue; the launchd worker `com.betty.youtube-worker` on the Mac claims it, downloads the media, uploads to YouTube, sets the thumbnail, inserts captions, and resumes the workflow through the wait-webhook.

The Mac must be on and logged in. **launchd respawns the worker automatically when the process dies** — verified 2026-09-19, killed PID 92331 and it came back as 93582 on the patched file. `launchctl kickstart -k gui/$(id -u)/com.betty.youtube-worker` also works. Either way, **confirm the new PID is running the new file**; an edit without a restart is the classic silent no-op.

## ⛔ B1 — the brand-safety requirement, before anything else

`worker.py` as built hardcodes the **QDE** credential and one shared queue:

```
CRED_PATH    = ~/.config/betty/youtube/qde_client_secret.json
TOKEN_PATH   = ~/.config/betty/youtube/qde.token.json
QUEUE_REMOTE = "gdrive:youtube_upload_queue"
```

**An HU job dropped into that queue as-is uploads to the QDE channel.** The upload is private, so nobody would notice until someone went looking. This is the highest-risk item in the HU build and it is still open.

Required before the first HU run:

1. **Its own queue folder.** HU never shares `youtube_upload_queue`.
2. **The job carries its own identity:** `brand: "HU"`, `yutu_credential: "hu_client_secret.json"`, `yutu_token: "hu.token.json"`, `expected_channel_id: "UCG-DLule9ZSStBdc5gSEoCw"`.
3. **A per-job credential lookup** in the worker, defaulting to QDE only when `brand` is absent, so existing QDE jobs are untouched.
4. **A hard assertion after upload:** read `channelId` back with `videos.list(part=snippet)` and compare to `expected_channel_id`. A mismatch stops the job loudly. **Never a warning.**
5. **Prove the patch on a QDE job first**, before any HU job exists. If the QDE lane breaks, stop.
6. **Prove the credential points where you think it does** — `yutu_hu channel-list` must return `UCG-DLule9ZSStBdc5gSEoCw`. The channel ID in file 00 came from the Metricool brand record, not from YouTube. One read settles it.

HU has its own GCP project (`yutu-handwriting-university`) with its own ~10k/day quota, so HU traffic never starves QDE. A `403 quotaExceeded` on HU means genuine HU volume.

## Upload
Via the `yutu` CLI from a local path — never YouTube Studio, never a Chrome session. rclone the render down first; `yutu` needs a real local file.

- Channel: `UCG-DLule9ZSStBdc5gSEoCw` (`@handwritinguniversity`)
- Visibility: **PRIVATE**. Never Unlisted, Public, or Scheduled at upload time.
- Title and description set **verbatim** from the copy package. Check for markdown artifacts first.
- ⛔ **Never post to the Joan Harris channel `UCbDGkQdUKEgeDTDvqVEWoWA`.**

**The duplicate guard works, and its key is `vid_id|drive_file_id` with a 6-hour window.** Observed refusing a genuine duplicate on 2026-09-19. **A rename defeats it**: the same physical file under a new VID_ID uploads twice — this happened (`DUeiBACO-Xc` then `1gHpJXJLDf0`, same Drive ID). Add a secondary check on `drive_file_id` alone that warns when the same bytes were already uploaded under a different VID_ID. Note also that nothing in the job builder ever sets `force_reupload`, so a legitimate re-run inside six hours is silently skipped — that skip is reported as a normal completion.

## Thumbnail — two faults, both fixed and both proven 2026-09-19

**Fault 1 — `yutu` silently refuses an absolute `--file` path.** It resolves `--file` against `YUTU_ROOT` (default: cwd), prints its usage text to stdout, **never calls the API, and still exits 0**. This, not the aspect ratio, is why no custom thumbnail had ever reached YouTube.

```
✅  cd {job_dir} && yutu thumbnail set --videoId {id} --file {basename} --yes --output json
⛔  yutu thumbnail set --videoId {id} --file /absolute/path.png ...
```

**Fault 2 — aspect ratio.** YouTube silently keeps its auto-generated frame when a custom thumbnail is not 16:9. `make_16x9()` centre-crops and scales to 1280×720 with ffmpeg before upload.

**Both proven on a live run:** `thumbnail converted 1536x1024 -> 1280x720`, then `thumbnail set (1280x720)` with no warning — meaning the API acknowledged it *and* the aspect check passed — and the thumbnail visibly displaying on `S6JgRfTbdjY`.

**Confirm it landed by reading it back.** `thumbnails.maxres` present at 1280×720 on `videos.list` is the proof. `rc == 0` is not.

## Captions — LAST YouTube step, after the thumbnail

⛔ Never upload captions before the thumbnail is set.

### ⭐ SOLVED 2026-09-19 — and V1 of this file had it wrong

Every caption insert in both lanes returned `status: failed / failureReason: processingFailed`, for as long as the lane has existed. **V1 concluded it was a readiness race and prescribed 8 retries 60 seconds apart. That was wrong, and no number of retries could ever have worked.**

**Root cause: `fix_vtt_hours()` in `worker.py`.** It exists to add a missing hours field to `MM:SS.mmm` timestamps. Its pattern `\b\d{2}:\d{2}\.\d{3}\b` also matches the **tail** of a well-formed `HH:MM:SS.mmm` stamp, so it prepended another `00:`:

```
IN : 00:00:00.216 --> 00:00:01.319
OUT: 00:00:00:00.216 --> 00:00:00:01.319     ← four fields, invalid WebVTT
```

Descript **always** emits hours. So every cue of every VTT this worker ever uploaded was corrupted between download and upload. YouTube was correctly rejecting a malformed file. The VTT saved by file 03 was fine all along.

**The fix** — a lookbehind that refuses a preceding digit or colon:

```python
fixed = re.sub(r'(?<![\d:])(\d{2}:\d{2}\.\d{3})', lambda m: '00:' + m.group(1), content)
```

Verified against `00:00:00.216`, `00:12.500`, `01:02:03.456` and `10:59:59.999` — correct stamps untouched, the `MM:SS.mmm` case still fixed. Then proven end to end: the same VTT, the same video, the same production function → **`status: serving` on the first attempt, no retries.**

**What this retires.** The readiness-race theory. The "~90 minutes later the same VTT served fine" anecdote — that file had not been through this function. And any plan to lengthen the retry window, which would only have re-uploaded a broken file more patiently.

### The retry loop stays, as a safety net

Delete the existing track, re-insert, poll; on `processingFailed`, wait and repeat — 8 attempts, 60s apart. `syncing` does **not** count as success; only `serving` does. It should now succeed on attempt 1. If it ever needs a second attempt, that is a signal worth investigating, not a normal outcome.

Verify `trackKind: standard`, not `asr`. A newly uploaded video gets an auto-generated ASR track in the same language which must be deleted before inserting the real one, or the insert fails on a same-language conflict.

## ⚠️ The incomplete-publish branch — clone this to HU

The worker sets `status: "OK"` as soon as the **video** uploads, whether or not the thumbnail and captions landed. The QDE `Worker succeeded?` node tested only `worker_status === "OK"`, so four videos reported ✅ Production Complete with neither a thumbnail nor captions. The flags were parsed one node earlier and never gated on.

A four-node branch was added to `Betty — QDE YouTube Publish v1` on 2026-09-19 and it fired correctly on the one run where captions genuinely failed. **The HU clone needs the same thing:**

- An IF on `youtube_thumbnail_set && youtube_captions_set`, hanging off `YT Result` so it runs **alongside** the success path and blocks nothing.
- False → a Code node that names exactly what is missing → Slack + ntfy.
- The message leads with `⚠️ HU published INCOMPLETE`, names the missing piece, and says not to make the video public until it is fixed.

⛔ **Do not tighten `Worker succeeded?` itself.** `status: OK` means the video uploaded, which is true. Warn loudly and keep going; a slow caption should not fail-stop a whole run.

## Resume
The worker POSTs back to the wait-webhook with `vid_id`, `youtube_id`, `youtube_thumbnail_set`, `youtube_captions_set`, `status`. Each of those booleans must come from a destination read, not from an exit code.

## Flags
`WRONG_CHANNEL` (hard stop) · `DUPLICATE_UPLOAD` · `THUMB_NOT_CONFIRMED` · `CAPTIONS_NOT_SERVING` · `WORKER_TIMEOUT`
