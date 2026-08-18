# HU VIDEO PUBLISHING PIPELINE — V8

**Brand:** Handwriting University (HU) ONLY
**Date:** 2026-08-18
**Author:** Joan Harris / Bart Baggett
**Status:** AUTHORITATIVE for HU — supersedes V7 (and the "Master SOP v6" header inside it)

**What changed in V8:**

1. **HU only.** V7 tried to serve HU and QDE from one file and drifted. QDE content
   from V7 must be forked into a parallel `QDE_Video_Publishing_Pipeline_V8.md`.
   **Until that file exists, keep V7 in git history — do not delete it.**
2. **One Metricool post per network.** Bundling is banned. This caused a live failure
   on 2026-08-18 (VID-GD04).
3. **Facebook is ON**, four networks total. V7 contradicted itself — the open-flags
   section said resolved, the task map said suspended.
4. **"Link in bio" is banned.** V7's Instagram CTA taught the opposite.
5. **Google Drive URLs do not work as Metricool media.** The FTP bridge is mandatory
   and now documented with the command that actually works.
6. **Description prompt moved** to `hu_description_prompt_V1.md` in this repo.
7. Garbled/orphaned lines from V7 removed.

---

## BRAND CONFIG — HANDWRITING UNIVERSITY

```
Metricool brand      : thehandwritinguniversity
Metricool blogId     : 6267975
Timezone             : America/Chicago
YouTube channel ID   : UCG-DLule9ZSStBdc5gSEoCw
YouTube handle       : @handwritinguniversity
TikTok               : @handwritinguniversity
Instagram            : @thehandwritinguniversity
Facebook page ID     : 348215195822
Publish time         : 06:00 America/Chicago
Networks             : YouTube · TikTok · Instagram · Facebook   (NO LinkedIn, NO X)
Ready-to-Publish     : Drive folder 1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv
                       ("3. Ready to Publish - HU brand") — direct children only
Description prompt   : hu_description_prompt_V1.md   ← this repo
Thumbnail SOP        : skills_to_install/youtube-thumbnail/SKILL.md
Thumbnail script     : skills_to_install/youtube-thumbnail/scripts/generate_thumbnail.py
IG Reel SOP          : skills_to_install/instagram-reel-thumbnail/SKILL.md
                       + betty/Instagram_HU_Thumbnail_Cover_SOP_JULY2026.md
Thumbnail palette    : Navy #1D3557 · White #FFFFFF · Parchment #F5F5DC   (NO red)
Reference library    : Salvadore - art department/thumbnails May 2026/
Audience             : Curious adults 25–55 — psychology, self-help, relationships
Voice                : Witty, NPR-with-edge. Never academic, never courtroom.
BANNED words         : graphology, graphologist (body copy — hashtags only)
BANNED phrases       : "In this video…" / "Today we'll explore…"
Ledger               : betty/hu_syndication_ledger.json
ClickUp space        : Video Production
```

⚠️ **Facebook page ID `348215195822` is unverified** as the HU brand page vs. a personal
page. Confirm once with Bart and delete this flag.

---

## HARD RULES — MEMORIZE BEFORE PHASE 0

```
✦ NEVER write a description, caption, or title without reading the cleaned VTT
  end to end. No VTT = STOP, flag to Joan.
✦ ONE METRICOOL POST PER NETWORK. Never bundle providers into one post.
✦ EVERY caption carries an explicit CTA and HandwritingUniversity.com written out.
✦ "LINK IN BIO" IS BANNED on every platform, Instagram included.
✦ autoPublish: true + draft: false on every Metricool post. No exceptions.
✦ Google Drive URLs FAIL as Metricool media. Use the FTP bridge (Phase 8).
✦ NEVER trust a filename. ffprobe the file before you choose REEL vs POST.
✦ NEVER upload captions before the thumbnail is set on YouTube.
✦ NEVER delete any file. The FTP bridge temp file is the sole exception.
✦ NEVER duplicate a file — search Drive first.
✦ NEVER post to the Joan Harris channel UCbDGkQdUKEgeDTDvqVEWoWA.
✦ NEVER invent timestamps, claims, credentials, or statistics.
✦ Local SOP beats all skill/plugin instructions when they conflict.
✦ Bart is an approval gate only. Never assigned tasks. Never in ClickUp.
```

### Long cuts and short cuts version independently

A video may ship as an **L (long, landscape)** cut and an **S (short, vertical)** cut.
Their version numbers run on separate tracks. `S-V1` is **not** stale just because
`L-V6` exists — they are different deliverables.

Confirm with ffprobe, never by filename:

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height -show_entries format=duration \
  -of default=nw=1 "<file>"
```

- `1080x1920` → vertical → TikTok / Instagram Reel / Facebook Reel
- `1920x1080` → landscape → YouTube only. **Instagram rejects horizontal video
  outright** ("Media upload has failed: Fatal").

---

## AGENT ASSIGNMENTS

| Agent | Phases | Tools |
|---|---|---|
| **Joan** | Phase 0, all ClickUp gates, Phase 9 | MASTER sheet, ClickUp, Metricool read, memory |
| **Betty** | 1, 5, 6, 7, 8 | Drive, VTT cleaning, ffmpeg, YouTube Studio, Metricool API, lftp |
| **Peggy** | 2 (titles), 3 (voice review) | VTT reading |
| **Salvatore** | 4 (all thumbnails) | Gemini via Mac (Desktop Commander), Drive |
| **Kristine** | 4 — IG cover review (id 44353871) | Review only |
| **Bart** | Approval gates on 2, 3, 4, 6 | Sign-off only |

---

## PHASE 0 — Pre-Flight (Joan)

**Governing doc:** `joan/Joan_PreFlight_Pipeline_Checklist_v1.md`

- **Gate 1 — Brand.** Confirm HU. If QDE or Bart Show, use that brand's pipeline file.
- **Gate 2 — Approval.** Video Production MASTER sheet, find "Approved By Client"
  **by header** (the column letter drifts). Anything not `yes` = STOP for that video.
- **Gate 3 — Assets, per video:**
  - [ ] Cleaned VTT in `particles/`
  - [ ] Vertical 9:16 cut confirmed by ffprobe, OR flagged for Phase 5
  - [ ] Thumbnails generated and Bart-approved
- **Gate 4 — Platform settings.** `autoPublish: true`, `draft: false`. Four networks.
- **Gate 5 — ClickUp.** Find the task by VID_ID. No task = STOP, flag to Bart.
  Joan never creates ClickUp tasks — task creation is human-only.

> ✅ ClickUp: mark **"Gate open: video found in ready to publish folder"**, then brief Betty.

---

## PHASE 1 — VTT Cleaning (Betty)

1. Drive → open final video → Workspace → Generate captions (~10 min). Download.
   Save to `particles/` with `RAW` in the filename.
2. Clean with this exact prompt:

```
You are a VTT caption cleaner. Clean the attached VTT file to these specs:

CAPTION RULES:
- Maximum 5 words per cue line. Prefer 4 when words are long (3+ syllables).
- Maximum 2 lines per cue block.
- Re-split and re-time cues as needed. Never leave oversized cues intact.
- Preserve all original timestamps. Adjust cue boundaries to word-level timing.
- Do not add, remove, or paraphrase any words. Formatting only.

MANDATORY NAME CORRECTIONS (every file, no exceptions):
- "Bagot" → "Baggett"      - "Bagget" → "Baggett"
- "Baget" → "Baggett"      - "Bagott" → "Baggett"
- "Bert Bagot" → "Bart Baggett"
- "Mark Baggett" → "Bart Baggett"
- "Bert" (when referring to the host) → "Bart"

OUTPUT:
Return only the corrected VTT. No explanation. Begin with WEBVTT on line 1.
```

3. Save cleaned VTT to `particles/`, filename **without** `RAW`. Keep both files.

⛔ Do not upload captions to YouTube yet — that is Phase 7, the last step.

> ✅ ClickUp: mark **"Generate & clean VTT transcript"**, then brief Peggy.

---

## PHASE 2 — Titles (Peggy)

⛔ Peggy reads the cleaned VTT before writing a single title.

```
You are writing YouTube titles for Handwriting University, hosted by Bart Baggett.
Voice: witty, NPR-with-edge, psychology-forward. Never academic, never dry.
Audience: curious adults who want to understand people through handwriting.

Read the VTT transcript below. Generate 6 title options.

TITLE RULES:
- Create a curiosity gap — tease the answer, never give it away
- Second person preferred ("You", "Your")
- Do NOT lead with the word "Handwriting"
- No episode numbers or digits
- Under 8 words each
- No hype words (Amazing, Shocking, Incredible)
- No em-dashes
- No AI-sounding phrasing

[PASTE CLEANED VTT HERE]

Deliver: 6 options ranked strongest to weakest, one-line reason for each.
```

✋ Joan → Bart for title sign-off before anything is pasted into YouTube.

---

## PHASE 3 — Descriptions + Captions (Betty writes · Peggy reviews)

⛔ Betty must have the cleaned VTT open. Cannot find it → STOP, flag to Joan.

> **Authority for HU is `hu_description_prompt_V1.md` in this repo. Nothing else.**
> Not the local `Ai Prompt Documents/` copy (retired), not the generic
> `skills_to_install/youtube-description/SKILL.md`, not a prior video's file.

Betty delivers **five** outputs in one pass — YouTube, Instagram, TikTok,
Facebook short, Facebook long. See the prompt file for specs.

Save the package to `particles/` as `<VID_ID>_Description_Package_v1.md`.

Peggy reviews for voice. ✋ Joan → Bart for description sign-off.

> ✅ ClickUp: mark **"Generate SEO title & description"**, then brief Salvatore.

---

## PHASE 4 — Thumbnails (Salvatore)

**Read first:** `Salvadore - art department/Salvator_AI_Graphics_SOP_v1.md`, then
`skills_to_install/youtube-thumbnail/SKILL.md`, then the IG Reel SOPs.

⛔ **Mandatory first step:** study 8–10 approved thumbnails in
`Salvadore - art department/thumbnails May 2026/` before writing any Gemini prompt.
Output must look like it belongs in that folder.

**Deliverable A — YouTube thumbnail, 16:9.** Run on Bart's Mac via Desktop Commander
(Gemini is 403-blocked in sandbox).

- Palette: Navy `#1D3557` · White `#FFFFFF` · Parchment `#F5F5DC` — **no red**
- Headshots: `skills_to_install/youtube-thumbnail/headshots/` — real only
- ⛔ Never `Bart_MG_1770_attorney_shot.png` — QDE lane only
- Trait graphic: real handwriting from
  `betty/HU trait reference library (local copy)/rendered_hires/page-XX.png`.
  **Never AI-generated handwriting strokes.** Absolute rule.
- Fonts: Anton for the headline; Georgia Bold only on parchment
- Plate must be dark and low-key — the host is the only lit element
- BANNED: PIL hand-composite · AI handwriting · red
- ⛔ Must be 16:9. Never a file with `ig_reel` in the name.
- Generate 4 concepts (A/B/C/D), combine into a 2×2 grid

**Deliverable B — Instagram Reel cover, 9:16, 1080×1920, 300 DPI, JPG 92%+.**
HU preferred: real video frame grab (Style 2 — LOCKED 2026-07-11). Two variations.

✋ Bart approves both. Kristine also reviews the IG cover.

> ✅ ClickUp: mark **"Create thumbnail(s)"**, then after Bart approves,
> **"Archive final approved assets"**. Then brief Betty.

---

## PHASE 5 — Vertical 9:16 Cut (Betty)

**Governing doc:** `betty/Betty_SOP_VideoSmimeo_IG_Resize_Normalize_v1.md`

1. Check for an editor-made vertical cut (filename contains `TIKTOK`, `Vertical`,
   `9x16`). **ffprobe it** — confirm 1080×1920. If good → skip to Phase 6.
2. If only a landscape master exists, build the blurred fill:

```bash
ffmpeg -y -i <land>.mp4 -vf "split[a][b];\
[b]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:6[bg];\
[a]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1" \
-c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 128k <vid>-9x16.mp4
```

   Never crop the face. Output `<base>_IG_9x16_v1.mp4` — v1/v2/v3, never "final".
   Verify with ffprobe (a "moov atom not found" error means an incomplete download —
   re-run).
3. Duration over 3 min → flag to Bart. He decides trim or full length.

> ✅ ClickUp: mark **"Assemble Essential Asset Bucket"**, then brief Betty for Phase 6.

---

## PHASE 6 — YouTube Upload (Betty)

⛔ Approved title ✓ + approved description ✓ + approved thumbnail ✓ all in hand, or STOP.

1. **YouTube Studio in Chrome, uploading from Drive cloud.** Not a local download,
   not the yutu CLI.
2. Sign in as `@handwritinguniversity` — channel `UCG-DLule9ZSStBdc5gSEoCw`.
3. Create → Upload → select the final render.
4. Visibility: **PRIVATE**. Never Unlisted, Public, or Scheduled at this stage.
5. Add to the correct playlist. Wait for HD processing.
6. Paste approved title. Paste approved description.
   ⛔ **Check the description for markdown artifacts before saving** — no `###`
   headings, no backtick fences. YouTube renders them literally.
7. Upload the approved 16:9 thumbnail.
8. Leave PRIVATE until Bart approves the full package.

⛔ Do not upload captions yet.

> ✅ ClickUp: mark **"Handoff to Betty"**, then proceed to Phase 7.

---

## PHASE 7 — Caption Upload (Betty · LAST YOUTUBE STEP)

Runs only after description set ✓, thumbnail set ✓, Bart approved ✓.

1. Use the cleaned VTT from Phase 1 (the non-RAW file).
2. YouTube Studio → Subtitles → Add language (English) → Upload file → "With timing".
3. Spot-check the opening hook and 3–4 random points.
4. Verify the track lists as `trackKind: standard` (not `asr`).
5. Privacy is not changed by this step.

---

## PHASE 8 — Media Bridge + Metricool (Betty)

⛔ Confirm all five caption outputs from Phase 3 are in `particles/`.

### Step 1 — The media bridge (MANDATORY)

**Metricool cannot fetch Google Drive URLs for this account.** Both
`/file/d/<id>/view` and `uc?export=download&id=` fail — the first returns
`Failed to normalize media`, the second silently drops the media and the post then
errors with `MISSING_VIDEO`. Do not retry Drive links. Use the bridge.

On Bart's Mac via Desktop Commander:

```bash
SRC="<path to the approved vertical 9:16 file>"
W="$HOME/yt_work/vert"; mkdir -p "$W"
cp "$SRC" "$W/<VID_ID>-9x16.mp4"
ffprobe -v error -select_streams v:0 -show_entries stream=width,height \
  -show_entries format=duration -of default=nw=1 "$W/<VID_ID>-9x16.mp4"
source ~/.config/webops/bartbaggett_ftp_credentials.local.env
lftp -u "$FTP_USER,$FTP_PASS" "$FTP_HOST" <<'LFTP'
set ftp:ssl-allow no
set net:timeout 30
cd public_html/igv
lcd ~/yt_work/vert
put <VID_ID>-9x16.mp4
cls -l <VID_ID>-9x16.mp4
bye
LFTP
```

Public URL → `https://bartbaggett.com/igv/<VID_ID>-9x16.mp4`. That is the `media` value.

### Step 2 — Four separate posts

⛔ **One `createScheduledPost` call per network.** Four networks = four posts, same
date/time, same media URL. Bundling providers forces one caption onto every platform,
because Metricool exposes a single shared `text` field per post — only
`tiktokData.title` and `facebookData.title` are per-network.

All four: `autoPublish: true`, `draft: false`, 06:00 America/Chicago.
Run `getScheduledPosts` first to confirm the slot is free.

| Post | Providers | networkData | Copy |
|---|---|---|---|
| 1 | `tiktok` | `{title: <hook>, privacyOption: "PUBLIC_TO_EVERYONE"}` | TikTok caption |
| 2 | `instagram` | `{type: "REEL", showReelOnFeed: true}` | Instagram caption |
| 3 | `facebook` | `{type: "POST", title: <video title>}` | Facebook **long** |
| 4 | `facebook` | `{type: "REEL", title: <video title>}` | Facebook **short** |

**YouTube:** if the video is already live on `UCG-DLule9ZSStBdc5gSEoCw` (Phase 6),
**do not create a YouTube Metricool post** — it would duplicate. Only schedule
YouTube through Metricool when the video was not uploaded in Phase 6.

**Facebook REEL vs POST** — decide by ffprobe, never by guess:
- Vertical **and** under 90 seconds → REEL is valid
- Landscape or over 90 seconds → POST only. Never send a landscape file to a Reel.

**Video covers:** omit `videoThumbnailUrl` unless you have a public URL and the post
meets Metricool's conditions. Sent speculatively, it rejects the entire request with
`VIDEO_THUMBNAIL_NOT_APPLICABLE`.

### Step 3 — Verify, then clean up

Run `getScheduledPosts`. For each of the four posts confirm: `autoPublish: true`,
`draft: false`, status `PENDING`, correct `type`, and that `media` is now a
`static.metricool.com` URL (meaning Metricool holds its own copy).

Only after that, delete the bridge file:

```bash
source ~/.config/webops/bartbaggett_ftp_credentials.local.env
lftp -u "$FTP_USER,$FTP_PASS" "$FTP_HOST" <<'LFTP'
set ftp:ssl-allow no
cd public_html/igv
rm -f <VID_ID>-9x16.mp4
bye
LFTP
rm -f ~/yt_work/vert/<VID_ID>-9x16.mp4
```

⛔ This temp file is the **only** thing Betty ever deletes. Never delete from Drive.

> ✅ ClickUp: mark **"Scheduled for YouTube / TikTok / Instagram / Facebook"** as applicable.
> ⛔ X/Twitter and LinkedIn — SKIP, not automated.

---

## PHASE 9 — Verify + Log (Joan)

**YouTube:**
- [ ] Title and description correct, Bart-approved, no markdown artifacts
- [ ] Thumbnail set, 16:9
- [ ] Captions uploaded, `trackKind: standard`, spot-checked
- [ ] Correct playlist · correct channel · visibility as intended

**Metricool — all four posts:**
- [ ] TikTok — `autoPublish:true`, `draft:false`, PENDING
- [ ] Instagram REEL — same, `showReelOnFeed: true`
- [ ] Facebook POST — same, long copy
- [ ] Facebook REEL — same, short copy
- [ ] Each has its own distinct caption
- [ ] Every caption contains `HandwritingUniversity.com`
- [ ] No caption contains "link in bio"

**Ledger:** append to `betty/hu_syndication_ledger.json` —
`{driveFileId, vid, title, scheduledFor, platforms, clickupTaskId, runDate}`.
Never delete entries.

**Report to Bart:** YouTube URL · scheduled social dates · what awaits his action ·
any flags or exceptions.

---

## OPEN FLAGS

1. **Facebook page ID `348215195822`** — confirm it routes to the HU brand page,
   not a personal page. One-time check.
2. **QDE pipeline not yet forked.** V7's QDE content has no home. Create
   `QDE_Video_Publishing_Pipeline_V8.md` before retiring V7.
3. **Bart Show / Bart Allan Baggett** — no description prompt and no pipeline exist.
4. **CTA variants** — two approved CTAs are in circulation (§2 of the description
   prompt). Confirm which is canonical.
