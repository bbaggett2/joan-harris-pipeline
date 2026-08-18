# QDE VIDEO PUBLISHING PIPELINE — V9

**Brand:** Handwriting Experts Inc. / QDE ONLY
**Date:** 2026-08-18
**Location:** `joan-supervising-agent/` — this is a cross-agent document
**Status:** AUTHORITATIVE for QDE — forks the QDE half out of the retired dual-brand V7

> ⛔ **V7 stays in git history until this file is confirmed working on a live batch.**
> Do not delete it yet.

---

## ⚠️ READ THIS BEFORE THE FIRST RUN

This file was built from V9's structure with QDE brand facts from
`brands/qde-brand.md`. It was **not** copied from the local QDE pipeline on the hard
drive, deliberately: that file last ran cleanly in May -JULY 2026, which is *before*
every failure the current procedure exists to prevent — bundled Metricool posts, the
"link in bio" ban, Drive URLs failing as Metricool media, and ffprobe-before-REEL. A
May-era pipeline would reintroduce all four.

**The operational IDs below are incomplete.** Fields marked `[TO VERIFY]` are unknown.
Fields marked `[BEST ESTIMATE]` are carried from prior sessions and have **not** been
confirmed against Metricool or YouTube. **Confirm every one before the first batch runs.**

---

## WHAT THIS FORK CHANGED FROM THE HU PIPELINE

1. **Brand facts point at `brands/qde-brand.md`**, not the HU kit.
2. **Copy prompt is `qde_legal_description_prompt_V6.md`.**
3. **No cross-platform pointers.** QDE bans "full breakdown on YouTube" — HU requires it.
   Every QDE CTA resolves to the phone number and the two owned domains.
4. **Thumbnail house style differs entirely** — navy ground, exactly one gold word,
   red stamps only. Produced by a script, not the HU generator.
5. **Outcome claims are banned**, and credibility markers are used only when the video is
   actually about credibility.

---

## AUTHORITY MODEL

**GitHub is authority. The Mac is where execution happens.**

Every SOP, pipeline, prompt, and brand fact is committed to
`bbaggett2/joan-harris-pipeline`. Local copies are caches. They drift. **When a local
file disagrees with `main`, `main` wins.** An uncommitted file is a blocked job, not a
fallback.

**Per-video artifacts are never committed.** VTT, description package, renders, and
thumbnails are working output on the Mac. When the video publishes, the job is over.

### Where brand facts live

| Need | File |
|---|---|
| Domains, phone, credentials, banned terms, tone, palette, thumbnail house style, hashtags | `brands/qde-brand.md` |
| Host voice reference | `brands/BART_BAGGETT_VOICE.MD` |

⛔ **Never restate a brand fact in this file or in a prompt file.** A duplicated domain or
palette is one that will be wrong within a month — this is exactly what went wrong in V8.

---

## BRAND CONFIG — OPERATIONAL IDS ONLY

```
Metricool brand      : Handwriting Expert Inc
Metricool blogId     : 6268508   
Timezone             : America/Chicago
Publish time         : [TO VERIFY]
YouTube channel ID   : UCrpyI5SkE075HJaFyxO_ozQ 
YouTube handle       : @thehandwritingexpert
TikTok               : @handwritingexpertsinc
Instagram            : forensichandwritingexpert
Facebook page ID     : handwritingexpertsinc
Networks             : [TO VERIFY — HU runs YT/TikTok/IG/FB. Confirm QDE's set.]
Ready-to-Publish     : [TO VERIFY — Drive folder ID]
Description prompt   : peggy-olson-copywriting/qde_legal_description_prompt_V6.md
Thumbnail script     : Generate_QDE_Forensic_Thumbnails_v3.sh  (Salvatore's folder, Mac)
Ledger               : [TO VERIFY]
ClickUp space        : [TO VERIFY — HU uses "Video Production"]
ClickUp statuses     : Open · in progress · Closed   (exact vocabulary)
```

Everything not in this block — domains, phone, credentials, palette, banned terms, tone —
comes from `brands/qde-brand.md`.

---

## HARD RULES — MEMORIZE BEFORE PHASE 0

```
✦ NEVER write a title, description, or caption without reading the cleaned VTT
  end to end. No VTT = STOP, flag to Joan.
✦ GitHub beats local. Always. No exceptions, no fallbacks.
✦ Brand facts come from brands/qde-brand.md. Never from memory, never restated inline.
✦ NEVER promise or imply a case outcome. No "win your case," no "guarantee."
✦ FIRST PERSON always. "I examined the signature," never "Bart Baggett examined."
✦ HandwritingExpertUSA.com and bartbaggett.com are BOTH this lane. Do not "correct"
  bartbaggett.com out of QDE copy.
✦ HandwritingExpert.com is BANNED — Bart does not own it. Hashtag use only.
✦ NO cross-platform pointers. No "link in bio," no "full breakdown on YouTube."
  Every CTA resolves to the phone number and the two owned domains.
✦ ONE METRICOOL POST PER NETWORK. Never bundle providers into one post.
✦ autoPublish: true + draft: false on every Metricool post. No exceptions.
✦ Google Drive URLs FAIL as Metricool media. Use the FTP bridge (Phase 8).
✦ NEVER trust a filename. ffprobe the file before you choose REEL vs POST.
✦ NEVER upload captions before the thumbnail is set on YouTube.
✦ NEVER delete any file. The FTP bridge temp file is the sole exception.
✦ NEVER post to the Joan Harris channel UCbDGkQdUKEgeDTDvqVEWoWA.
✦ NEVER invent a credential, statistic, statute, jurisdiction, or case detail.
  Mark [TO VERIFY].
✦ NEVER apply HU personality/graphology framing to this lane. If content straddles,
  STOP and report to Joan.
✦ Betty publishes <VID_ID>_Description_Package_v1.md verbatim. She never edits copy.
✦ Bart is an approval gate only. Never assigned tasks. Never in ClickUp.
```

### Long cuts and short cuts version independently

`S-V1` is **not** stale because `L-V6` exists — they are different deliverables. Confirm
format with ffprobe, never by filename:

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height -show_entries format=duration \
  -of default=nw=1 "<file>"
```

- `1080x1920` → vertical → TikTok / Instagram Reel / Facebook Reel
- `1920x1080` → landscape → YouTube only. **Instagram rejects horizontal video outright.**

---

## AGENT ASSIGNMENTS

| Agent | Phases | Tools |
|---|---|---|
| **Joan** | 0, all ClickUp gates, 9 | MASTER sheet, ClickUp, Metricool read, memory |
| **Betty** | 1, 5, 6, 7, 8 | Drive, VTT cleaning, ffmpeg, YouTube Studio, Metricool API, lftp |
| **Peggy** | 2 (titles), 3 (descriptions + captions) | VTT reading, brand kit, description prompt |
| **Salvatore** | 4 (all thumbnails) | Gemini via Mac (Desktop Commander), Drive |
| **Bart** | Approval gates on 2, 3, 4, 6 | Sign-off only |

**Betty writes nothing. Peggy publishes nothing.** The handoff is one file:
`<VID_ID>_Description_Package_v1.md`.

Bart's four sign-offs are the only human touchpoints. Everything between them runs
agent-to-agent with no manual step.

⚠️ `brands/qde-brand.md` v1.0 still lists Betty as writing descriptions and captions and
Peggy as doing blog/AEO. That is the retired model. **This file governs.** Correct the
brand kit's "Read by" line at the next revision.

---

## PHASE 0 — Pre-Flight (Joan)

- **Gate 1 — Brand.** Confirm QDE. Forensic, attorney-facing, questioned documents, will
  contests, expert witness. If the content is handwriting *psychology* or personality,
  it is HU — use that pipeline. If it straddles, STOP.
- **Gate 2 — Approval.** MASTER sheet, find "Approved By Client" **by header** — the
  column letter drifts. Anything not `yes` = STOP for that video.
- **Gate 3 — Assets, per video:**
  - [ ] Cleaned VTT in `particles/`
  - [ ] Vertical 9:16 cut confirmed by ffprobe, OR flagged for Phase 5
  - [ ] Thumbnails generated and Bart-approved
- **Gate 4 — Platform settings.** `autoPublish: true`, `draft: false`.
- **Gate 5 — ClickUp.** Find the task by VID_ID. No task = STOP, flag to Bart.
  **Joan never creates ClickUp tasks** — task creation is human-only.
- **Gate 6 — Repo freshness.** The prompt and brand kit this job needs are on `main`.
- **Gate 7 — Legal accuracy.** ⚠️ QDE only. Any statute, jurisdiction, case citation, or
  credential in the copy is checked before publish. This is the one stage that always
  requires human review.

---

## PHASE 1 — VTT Cleaning (Betty)

Identical to the HU pipeline. See
`joan-supervising-agent/HU_Video_Publishing_Pipeline_V9.md` Phase 1 for the cleaner
prompt — the caption rules and the "Baggett" correction list are brand-neutral.

Save cleaned VTT to `particles/`, filename **without** `RAW`. Keep both files.

⛔ Do not upload captions to YouTube yet — that is Phase 7.

---

## PHASE 2 — Titles (Peggy)

⛔ Peggy reads the cleaned VTT before writing a single title. Tone and banned terms come
from `brands/qde-brand.md` — read it first.

```
You are writing YouTube titles for Handwriting Experts Inc., the forensic document
examination practice of Bart Baggett, questioned document examiner and expert witness.

Tone, banned terms, and audience modes: brands/qde-brand.md. Read it before writing.

Read the VTT transcript below. Generate 6 title options.

TITLE RULES:
- Serious, plain English. Credibility through specificity, not adjectives.
- Question form works well for this lane ("Can a Handwriting Expert Work Off a
  Photocopy?"). Curiosity is fine; hype is not.
- NEVER promise or imply a case outcome
- No hype words (Shocking, Unbelievable, Secret, You Won't Believe)
- "Exposed" only when literally accurate to the case
- No em-dashes
- Under 10 words each
- Identify whether the video is attorney mode or consumer mode, and say which

[PASTE CLEANED VTT HERE]

Deliver: 6 options ranked strongest to weakest, one-line reason for each.
```

✋ Joan → Bart for title sign-off.

---

## PHASE 3 — Descriptions + Captions (Peggy)

⛔ Peggy must have the cleaned VTT open. Cannot find it → STOP, flag to Joan.

> **Authority is `peggy-olson-copywriting/qde_legal_description_prompt_V6.md` on `main`.
> Nothing else.** If it is not on `main`, the job is blocked.

**Output file:** `particles/<VID_ID>_Description_Package_v1.md`

This is the single handoff to Betty. Every output labeled by platform. A missing CTA, an
unlabeled platform, or a placeholder is a failed handoff — Betty stops rather than
composing a substitute.

⛔ No markdown headings or backtick fences in the YouTube description body. YouTube
renders them literally.

⚠️ **Every timestamp must be read off the VTT.** Never estimated. This lane is quoted in
legal contexts; an invented timestamp is worse here than anywhere else.

✋ Joan → Bart for description sign-off, **plus the Gate 7 legal-accuracy check.**

---

## PHASE 4 — Thumbnails (Salvatore)

**Read first:** `brands/qde-brand.md` — palette, thumbnail house style, prop vocabulary.

**Production:** `Generate_QDE_Forensic_Thumbnails_v3.sh` via the Gemini pipeline on Joan's
Mac Studio (Gemini is 403-blocked in sandbox).

The house style is what makes the set read as a set:

1. Ground: deep navy, or a document/desk photograph darkened toward navy.
2. Headline: white, large, aligned opposite the subject.
3. **Exactly one word in gold.** Never two, never a gold sentence. This is the discipline
   that carries the brand.
4. Subject: Bart's face, serious, on one side — or a forensic prop where no face is used.
5. Props: magnifying glass, questioned document, signature close-up, gavel, evidence
   stamp, lab setting.
6. Red stamps sparingly (CONTESTED, FORGERY DETECTED). Never red headline text.

⛔ Never: neon, playful type, comedy framing, self-help imagery, personality-analysis
visuals, more than one gold emphasis.
⛔ Must be 16:9 for YouTube.

⚠️ **Palette hex values in the brand kit are flagged as unverified.** The authoritative
source is the generation script. Read the script, then correct the brand kit.

✋ Bart approves. Thumbnails are never decided alone.

---

## PHASE 5 — Vertical 9:16 Cut (Betty)

Identical to HU. Check for an editor-made vertical cut, **ffprobe it** to confirm
1080×1920. If only a landscape master exists, build the blurred fill:

```bash
ffmpeg -y -i <land>.mp4 -vf "split[a][b];\
[b]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:6[bg];\
[a]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1" \
-c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 128k <vid>-9x16.mp4
```

Never crop the face. Output `<base>_IG_9x16_v1.mp4` — v1/v2/v3, never "final".

---

## PHASE 6 — YouTube Upload (Betty)

⛔ Approved title ✓ + approved package ✓ + approved thumbnail ✓ + Gate 7 legal check ✓,
or STOP.

1. **YouTube Studio in Chrome, uploading from Drive cloud.** Not a local download,
   **not the yutu CLI.**
2. Sign in to the QDE channel — `[TO VERIFY]`.
3. Create → Upload → select the final render.
4. Visibility: **PRIVATE**. Never Unlisted, Public, or Scheduled at this stage.
5. Add to the correct playlist. Wait for HD processing.
6. Paste the approved title and description **verbatim** from the package.
   ⛔ Check for markdown artifacts before saving.
7. Upload the approved 16:9 thumbnail.
8. Leave PRIVATE until Bart approves.

⛔ Do not upload captions yet.

---

## PHASE 7 — Caption Upload (Betty · LAST YOUTUBE STEP)

Runs only after description set ✓, thumbnail set ✓, Bart approved ✓.

1. Use the cleaned VTT from Phase 1 (the non-`RAW` file).
2. YouTube Studio → Subtitles → Add language (English) → Upload file → "With timing".
3. Spot-check the opening and 3–4 random points.
4. Verify the track lists as `trackKind: standard` (not `asr`).

---

## PHASE 8 — Media Bridge + Metricool (Betty)

### Step 1 — The media bridge (MANDATORY)

**Metricool cannot fetch Google Drive URLs for this account.** Both `/file/d/<id>/view`
and `uc?export=download&id=` fail — the first returns `Failed to normalize media`, the
second silently drops the media and the post errors with `MISSING_VIDEO`. Do not retry
Drive links.

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

### Step 2 — One post per network

⛔ **One `createScheduledPost` call per network.** Bundling forces one caption onto every
platform, because Metricool exposes a single shared `text` field per post — only
`tiktokData.title` and `facebookData.title` are per-network.

All posts: `autoPublish: true`, `draft: false`. Run `getScheduledPosts` first to confirm
the slot is free.

⚠️ **The network set for QDE is `[TO VERIFY]`.** HU runs four. Confirm which platforms
QDE publishes to before the first batch, and record it in the config block above.

**Facebook REEL vs POST** — decide by ffprobe, never by guess:
- Vertical **and** under 90 seconds → REEL is valid
- Landscape or over 90 seconds → POST only

**Video covers:** omit `videoThumbnailUrl` unless you have a public URL and the post meets
Metricool's conditions. Sent speculatively, it rejects the whole request with
`VIDEO_THUMBNAIL_NOT_APPLICABLE`.

### Step 3 — Verify, then clean up

Run `getScheduledPosts`. Per post confirm `autoPublish: true`, `draft: false`, status
`PENDING`, correct `type`, and `media` now a `static.metricool.com` URL.

Only then delete the bridge file:

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

---

## PHASE 9 — Verify + Log (Joan)

**YouTube:**
- [ ] Title and description correct, Bart-approved, no markdown artifacts
- [ ] Description matches the package verbatim
- [ ] Thumbnail set, 16:9, one gold word
- [ ] Captions uploaded, `trackKind: standard`, spot-checked
- [ ] Correct playlist · correct channel · visibility as intended

**Metricool — every post:**
- [ ] `autoPublish: true`, `draft: false`, PENDING
- [ ] Each has its own distinct caption
- [ ] Every caption carries the phone number and `HandwritingExpertUSA.com`
- [ ] `HandwritingExpert.com` appears **nowhere**
- [ ] No caption contains "link in bio" or "full breakdown on YouTube"
- [ ] No outcome claim anywhere in the copy

**Ledger:** append — `{driveFileId, vid, title, scheduledFor, platforms, clickupTaskId,
runDate}`. Never delete entries.

**Report to Bart:** YouTube URL · scheduled dates · what awaits his action · flags.

---

## OPEN FLAGS

1. **⛔ BLOCKING — operational IDs incomplete.** Every `[TO VERIFY]` and
   `[BEST ESTIMATE]` in the config block must be confirmed before the first batch runs.
   The two best estimates came from prior sessions, not from Metricool or YouTube.
2. **Network set unknown.** Confirm which platforms QDE publishes to.
3. **Palette unverified.** Hex values in `brands/qde-brand.md` are best estimates. The
   authoritative source is `Generate_QDE_Forensic_Thumbnails_v3.sh` on the Mac. Read the
   script, correct the brand kit, remove that warning.
4. **`brands/qde-brand.md` has broken cross-references** — it points at `brands/hu.md`
   and `brands/bartallan.md`. The real filenames are `handwriting-university.md` and
   `bartallanbaggett-brand.md`.
5. **`brands/qde-brand.md` "Read by" line is stale** — it assigns descriptions and
   captions to Betty. Peggy writes.
6. **Pricing unresolved.** The brand kit flags a conflict between a tiered model and a
   $5,000 flat rate. **No pricing appears in any public copy until Bart resolves it.**
7. **"Free initial case review"** — confirm this offer is current before it appears in a
   consumer CTA.
8. **V7 retirement.** Keep it in git history until this file has run a live batch clean.
