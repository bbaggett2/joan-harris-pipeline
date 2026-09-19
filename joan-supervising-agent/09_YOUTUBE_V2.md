# QDE Video Pipeline — 09 YOUTUBE
**V2 · 2026-09-18 · Lane: Handwriting Experts Inc. / QDE only · Supersedes `09_YOUTUBE_V1.md`**

Governs: `Thumbnail: prompt` (fetch + LLM) · `OpenAI — thumbnail` · `Upload thumbnail` · `Share thumbnail` · `Build YouTube job` · `Write YouTube job` · `Wait for local YouTube worker` · `Parse worker result` · `Worker succeeded?` · `YT Result` — all in `Betty — QDE Video Publish v1` and `Betty — QDE YouTube Publish v1`. Companion doc: `00_OVERVIEW_V5.md` (the whole-pipeline picture); this file is the deep dive on this one step.

## What changed in V2

Two separate rebuilds, both same day:

1. **The upload itself moved off n8n Cloud** (already covered in `00_OVERVIEW_V5.md` — this file doesn't repeat that, see it for the full local-worker architecture, the Drive job queue, and the resume-webhook design).
2. **The thumbnail prompt stopped being a hardcoded guess and started being SOP-driven.** This is the part V1 never had and V2 exists to document.

## The old V1 problem

`Thumbnail: prompt` was a Code node with a hand-written regex formula baked directly into it — no file fetch, no brand reference, nothing. It picked a "gold word" via regex against the title and stitched together a generic navy/gold prompt. It explicitly generated a **placeholder silhouette with no facial features**, flagged the output `FACE_COMPOSITE_PENDING` — implying a real-photo compositing step was supposed to follow — but nothing downstream ever did that compositing. The raw placeholder just got used as the final thumbnail. This is why thumbnails looked generic and off-brand: the pipeline was never reading anything Salvatore (the actual owner of QDE thumbnail brand, per `org-ai-chain-of-command`) had written.

## The V2 fix

`Thumbnail: prompt` is now three nodes:

1. **`Fetch QDE thumbnail SOP`** — HTTP GET of `Thumbnail_Brand_SOP_QDE_v2.md` from `salvatore-art-department/` on GitHub (mirrored from the real Drive doc the same day — Drive is Salvatore's working copy, GitHub is what the pipeline actually reads, same authority pattern as every other prompt file in this repo).
2. **`Thumbnail: prompt (LLM)`** — an OpenAI chat/completions call (same raw-HTTP pattern as `Copy: title+description+captions`, not a special node type) that receives the full SOP text plus this video's title and description, and returns a single JSON field `thumbnail_prompt`. The system prompt makes it follow the SOP's actual rules: exact hex palette (`#10142E` navy / `#FFE455` gold / `#B00708` red), Anton-style bold condensed sans-serif, one of the three named layout patterns with a stated diagonal-slant panel if using pattern A, real forensic props from the SOP's list, question-format headline in second person that hides the answer, no episode numbers, no "FDE" jargon, no credentials, never "graphology"/"graphologist", explicit no-logo/no-watermark instruction.
3. **`Thumbnail: prompt`** (renamed back to this so nothing downstream needs to change) — a small Code node that parses the LLM's JSON response and shapes it into the same `thumbnail_prompt` field the rest of the workflow already expects.

**Deliberately does NOT include Bart's face.** No real photo reference is available to this automated path (Salvatore's real process uses a headshot library at `skills_to_install/youtube-thumbnail/headshots/` that this pipeline has no access to), so the LLM is instructed to default to Layout B (full-bleed photo + overlay) or C (document hero) — patterns the SOP itself says don't require Bart — rather than attempt a face it has no reference for. This avoids recreating the old placeholder-silhouette problem in a new form.

**This is an approximation, not a replacement for Salvatore's process — the SOP says so explicitly** (see its own note added under Production Step 2 when it was mirrored to GitHub). It cannot run Salvatore's actual Gemini script (`Generate_QDE_Forensic_Thumbnails_v3.sh` — Mac-only, Desktop Commander), cannot review the approved reference-library folder the SOP calls a mandatory step, and cannot composite a real Bart photo. Treat automated thumbnails as a reasonable draft, not a finished, on-brand asset — the SOP's own pre-publish checklist still applies before anything goes live.

**Dependency, not yet satisfied as of this writing:** the SOP file needs to actually exist at that GitHub path for the fetch to succeed. If `Fetch QDE thumbnail SOP` errors with a 404, that's why — push `Thumbnail_Brand_SOP_QDE_v2.md` to `salvatore-art-department/` first.

## The upload chain itself — gotchas already fixed, don't re-debug these

All discovered and fixed 2026-09-18, in this order, each one masking the next:

1. **VID_ID regex never captured suffixes.** `Create queue row` and `Media facts` both used `/VID-?\d{3,4}/i`, which drops any trailing `-S`/`-L`/`-V3`/`-A`/`-IG`. A file named `VID-0778-S...` matched the sheet row and copy package for base `VID-0778` instead of its own row — silently wrong data, not a crash. Fixed to `/VID-?\d{3,4}(-(?:S|L|A|IG|V\d+))?/i` in both nodes plus the two Slack/ntfy messages that also display the candidate ID.
2. **Local error handlers could mask real failures as success.** Nodes set to `onError: continueErrorOutput` (added the same night, to get the video number into error notifications) would notify correctly but then let the workflow end normally — n8n counts that as a successful execution. Fixed by adding a `Re-throw as real failure` node after the notification chain in both the YouTube and Metricool sub-workflows, so a caught error still fails the execution for real.
3. **`Write YouTube job` had the wrong credential.** A Drive node was accidentally given the Google **Sheets** credential's ID (`DTK7DwpcCWRxP6lW`) instead of the real Drive credential (`ggJqGY6WsbOSx1sq`, "Google Drive baggett.bart"). Fails with `Credential with ID ... does not exist for type "googleDriveOAuth2Api"`.
4. **The local worker was polling the wrong Drive path.** The `youtube_upload_queue` folder was created scoped to a specific root folder ID (`1V-piQzAW8iOYn_AesxkDzK4lcWLXUYvY`, the QDE assets folder) via `rclone --drive-root-folder-id ...`, but `worker.py`'s own rclone calls (`lsf`, `copyto`, `moveto`) didn't include that flag — so it was checking a `youtube_upload_queue` folder under default `My Drive` root, which doesn't exist. Silent, permanent miss; nothing ever got picked up. Fixed by adding `RCLONE_ROOT_FLAG` and applying it to every queue-folder rclone call in `worker.py`.
5. **launchd's PATH doesn't include Homebrew.** `com.betty.youtube-worker`'s default environment is `/usr/bin:/bin:/usr/sbin:/sbin` — no `/opt/homebrew/bin`, where both `rclone` and `yutu` live. Every subprocess call to either was silently failing with "command not found," and the polling loop didn't check the return code, so nothing was ever logged. Fixed by adding an explicit `EnvironmentVariables` / `PATH` key to the plist.
6. **Direct caption API calls didn't refresh the access token.** `yutu` commands auto-refresh internally; the worker's own direct `urllib` calls to the captions endpoints (needed because `yutu caption insert`/`delete` are themselves broken in this yutu version — see `00_OVERVIEW_V5.md`) just read the cached `access_token` from the token file, which is often stale by the time the worker gets to that step. Fails with a 401. Fixed: `get_access_token()` now does a real refresh-token exchange against `https://oauth2.googleapis.com/token` every time it's called, and writes the fresh token back to the file.

**First real end-to-end automated success, after all six fixes:** `VID-0778-S` → YouTube id `Vvd8ajIZZUw`, real title/description/thumbnail/captions, all independently verified.

## Known open gaps — not yet fixed

- **No timeout on `Wait for local YouTube worker`.** If the Mac is off or the worker process is dead, a job waits indefinitely with no alert. Needs a time-limit branch (the Wait node supports combining webhook-resume with a fallback duration) that pages Slack/ntfy if nothing arrives within, say, 30 minutes.
- **No dead-man's-switch on the worker itself.** `launchd`'s `KeepAlive: true` restarts the *process* if it dies, but nothing currently notices if the Mac itself is off or asleep for an extended stretch. A daily heartbeat job (a scheduled dummy job the worker is expected to pick up promptly) would close this.
- **Facebook Post needs a landscape file under 500MB; TikTok/Instagram/FB Reel need a vertical file.** Neither is automatic yet — tonight this meant manually compressing an oversized file (`VID-0773-L`, 912MB → 269MB via `ffmpeg`/`h264_videotoolbox`) and manually skipping formats with no source file available (`over_fb_cap: true`, empty `vertical_url`). Worth deciding whether the worker should auto-compress/auto-flag rather than requiring a human (or Claude) to notice and do it by hand each time.

## Operational commands

```bash
# Check the worker is running
launchctl list | grep betty

# Restart after editing worker.py or the plist
launchctl unload ~/Library/LaunchAgents/com.betty.youtube-worker.plist
launchctl load ~/Library/LaunchAgents/com.betty.youtube-worker.plist

# Watch it work
tail -f ~/betty/youtube_worker/worker.log

# Confirm the queue folder it's actually checking
rclone --drive-root-folder-id 1V-piQzAW8iOYn_AesxkDzK4lcWLXUYvY lsf gdrive:youtube_upload_queue --files-only
```

## Gate 7 is still human

Nothing in this file changes that. Real thumbnails, real captions, real descriptions all still need the reviewer's eyes before a video goes public — more so now that thumbnail generation is a best-effort automated approximation of Salvatore's brand, not his actual reviewed work.
