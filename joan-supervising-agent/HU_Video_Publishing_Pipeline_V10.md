# HU VIDEO PUBLISHING PIPELINE — V10

**Brand:** Handwriting University (HU) ONLY
**Date:** 2026-09-12
**Location:** `joan-supervising-agent/` — cross-agent document, not Betty's
**Status:** AUTHORITATIVE for HU — supersedes V9, which has been deleted

> **Versioning:** the version lives in the filename, and the highest number is current.
> `..._V10.md` beats `..._V9.md`, always. The header version above must match the filename.
> A new revision becomes `..._V11.md`, and this file is deleted at the same time. Never two
> live — that is what produced the duplicate README this file also replaces.

---

## WHAT CHANGED IN V10

1. **YouTube upload is the `yutu` CLI**, from a local file path. V9 said YouTube Studio in
   Chrome and explicitly banned `yutu`, which contradicted
   `Joan_PreFlight_Pipeline_Checklist` Gate 4. Bart settled it 2026-09-11: `yutu` is
   correct. Phase 7 caption upload is a separate step and is **not** `yutu`.
2. **Metricool posts are created as DRAFTS.** Agents never schedule a post. The reviewer
   schedules it, and that act is the approval. V9's unconditional
   `autoPublish: true, draft: false` at creation is replaced by a two-stage rule.
3. **The Drive-URL ban is narrowed.** V9 said Google Drive URLs always fail as Metricool
   media. They fail when the file is owner-only to an editor's Google account. Metricool
   uploads Drive files itself when Google Drive is linked in the account. The FTP bridge
   is now a documented fallback, not the standard path.
4. **Four approval gates become one review.** V9 had Bart signing off on titles,
   descriptions, thumbnails and the finished package. V10 has a single review, done where
   the work already sits: the private YouTube video and the Metricool planner.
5. **"Bart" is replaced by the REVIEWER role.** Bart expects to hand review to a hired
   person. No individual is named in the operating procedure any more.
6. **Facebook page ID verification merged in** from the duplicate README copy, which had
   it and the named V9 file did not.
7. **Open questions are marked in place** rather than assumed — see OPEN FLAGS.

---

## AUTHORITY MODEL

**GitHub is authority. The Mac is where execution happens.**

Every SOP, prompt, and brand fact is committed to `bbaggett2/joan-harris-pipeline`.
Local copies under `joan foundation documents and SOP/`, `Ai Prompt Documents/`, installed
skills, and plugins are caches. They drift. **When any local file disagrees with `main`,
`main` wins.**

An uncommitted file is a blocked job, not a fallback. If a prompt or SOP an agent needs is
not on `main`, that agent stops and reports to Joan.

**Per-video artifacts are never committed.** VTT, description package, renders, and
thumbnails are working output on the Mac. When the video publishes, the job is over.

### Where brand facts live

| Need | File |
|---|---|
| Voice, banned terms, audience, domain, palette, typography, master image prompts, QA checklist | `brands/handwriting-university.md` |
| Host voice reference | `brands/BART_BAGGETT_VOICE.MD` |

⛔ **Never restate a brand fact in this file or in a prompt file.** Reference the brand kit.
A duplicated palette is a palette that will be wrong within a month.

---

## BRAND CONFIG — OPERATIONAL IDS ONLY

```
Metricool brand      : thehandwritinguniversity
Metricool blogId     : 6267975
Timezone             : America/Chicago
Publish time         : 06:00 America/Chicago   (reviewer sets it when scheduling)
YouTube channel ID   : UCG-DLule9ZSStBdc5gSEoCw
YouTube handle       : @handwritinguniversity
TikTok               : @handwritinguniversity
Instagram            : @thehandwritinguniversity
Facebook page ID     : 348215195822          (verified HU brand page, Bart 2026-08-18)
Networks             : YouTube · TikTok · Instagram · Facebook   (NO LinkedIn, NO X)
Ready-to-Publish     : Drive folder 1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv
                       ("3. Ready to Publish - HU brand") — direct children only
Description prompt   : peggy-olson-copywriting/hu_description_prompt_V2.md
Thumbnail SOP        : salvatore-art-department/  (see Phase 4)
Reference library    : Salvadore - art department/thumbnails May 2026/
Ledger               : betty/hu_syndication_ledger.json
ClickUp space        : Video Production
ClickUp statuses     : Open · in progress · Closed   (exact vocabulary)
```

Everything not in this block — voice, palette, fonts, banned words, audience, domain —
comes from `brands/handwriting-university.md`.

---

## HARD RULES — MEMORIZE BEFORE PHASE 0

```
✦ NEVER write a title, description, or caption without reading the cleaned VTT
  end to end. No VTT = STOP, flag to Joan.
✦ GitHub beats local. Always. No exceptions, no fallbacks.
✦ Brand facts come from brands/handwriting-university.md. Never from memory,
  never restated inline.
✦ ONE METRICOOL POST PER NETWORK. Never bundle providers into one post.
✦ AGENTS CREATE DRAFTS. draft:true, no publish time. An agent never schedules
  a post. The reviewer schedules it, and that is the approval.
✦ A SCHEDULED POST IS autoPublish:true + draft:false. autoPublish:false is
  banned outright — it is not a hold, it is a notification that silently dies.
✦ EVERY caption carries an explicit CTA and HandwritingUniversity.com written out.
✦ "LINK IN BIO" IS BANNED on every platform, Instagram included.
✦ Metricool takes a Google Drive URL. The FTP bridge is a FALLBACK for files
  that are owner-only to an editor's account (Phase 8).
✦ NEVER trust a filename. ffprobe the file before you choose REEL vs POST.
✦ NEVER upload captions before the thumbnail is set on YouTube.
✦ NEVER delete any file. The FTP bridge temp file is the sole exception, and
  only after Metricool holds its own copy.
✦ NEVER duplicate a file — search Drive first.
✦ NEVER post to the Joan Harris channel UCbDGkQdUKEgeDTDvqVEWoWA.
✦ NEVER invent timestamps, claims, credentials, or statistics. Mark [TO VERIFY].
✦ Betty publishes <VID_ID>_Description_Package_v1.md verbatim. She never edits copy.
✦ The REVIEWER is a role, not a person. Never name an individual in procedure.
✦ NOTHING PUBLISHES WITHOUT THE REVIEWER. Both surfaces hold by default.
```

### Long cuts and short cuts version independently

A video may ship as an **L (long, landscape)** cut and an **S (short, vertical)** cut.
Their version numbers run on separate tracks. `S-V1` is **not** stale because `L-V6`
exists — they are different deliverables.

Confirm with ffprobe, never by filename:

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height -show_entries format=duration \
  -of default=nw=1 "<file>"
```

- `1080x1920` → vertical → TikTok / Instagram Reel / Facebook Reel
- `1920x1080` → landscape → YouTube only. **Instagram rejects horizontal video outright**
  ("Media upload has failed: Fatal").

---

## THE REVIEW MODEL

V9 had four sign-offs. V10 has one review, and nothing publishes without it.

| Surface | How it holds | What approval looks like |
|---|---|---|
| **YouTube** | Video is PRIVATE. Nobody can see it. | The reviewer makes it public. |
| **Metricool** | All four posts are drafts. A draft is not scheduled and cannot fire. | The reviewer schedules them. |

The reviewer gets **one notice** when both are staged — the YouTube link and the Metricool
planner link — then a reminder every few days while anything is still unreviewed. There is
no approval form, no third tool, and no dashboard. Anyone with access to those two places
can do the whole job, which is what makes handing the role to a hired reviewer simple.

**The REVIEWER is a configured role.** One value holds the notification address and the
accounts whose action counts as approval. Replacing the reviewer is changing that value.

### What still blocks outright

These are exceptions, not approvals, and they stop the pipeline wherever they occur:

- A vertical cut longer than 3 minutes — the reviewer decides trim or full length.
- Any missing or failed asset, missing VTT, or prompt not present on `main`.

---

## AGENT ASSIGNMENTS

| Agent | Phases | Tools |
|---|---|---|
| **Joan** | 0, all ClickUp gates, 9 | MASTER sheet, ClickUp, Metricool read, memory |
| **Betty** | 1, 5, 6, 7, 8 | Drive, VTT cleaning, ffmpeg, rclone + `yutu` CLI, Metricool API, lftp (fallback only) |
| **Peggy** | 2 (titles), 3 (descriptions + captions) | VTT reading, brand kit, description prompt |
| **Salvatore** | 4 (all thumbnails) | Gemini via Mac (Desktop Commander), Drive |
| **Reviewer** | The single review | YouTube Studio, Metricool planner |

**Betty writes nothing. Peggy publishes nothing.** The handoff between them is one file:
`<VID_ID>_Description_Package_v1.md`.

---

## PHASE 0 — Pre-Flight (Joan)

- **Gate 1 — Brand.** Confirm HU. If QDE or Bart Show, use that brand's pipeline file.
- **Gate 2 — Client approval.** ⚠️ **UNRESOLVED — see OPEN FLAGS #1.** Until the real
  column is identified, this gate **fails closed**: hold the video and ask the reviewer.
  Do not guess a column, and do not proceed on a missing value.
- **Gate 3 — Assets, per video:**
  - [ ] Cleaned VTT in `particles/`
  - [ ] Vertical 9:16 cut confirmed by ffprobe, OR flagged for Phase 5
  - [ ] Thumbnails generated (approval now happens at the single review, not here)
- **Gate 4 — Platform settings.** Drafts only. See HARD RULES.
- **Gate 5 — ClickUp.** Find the task by VID_ID. No task = STOP, flag to Joan.
  **Joan never creates ClickUp tasks** — task creation is human-only.
- **Gate 6 — Repo freshness.** Confirm the description prompt and brand kit this job needs
  are present on `main`. Missing = blocked job, not a local fallback.

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

⛔ Peggy reads the cleaned VTT before writing a single title. Voice and banned terms come
from `brands/handwriting-university.md` §2 — read it first.

```
You are writing YouTube titles for Handwriting University, hosted by Bart Baggett.
Voice and banned terms: brands/handwriting-university.md §2. Read it before writing.

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

**No gate here.** The top-ranked title is carried forward automatically. It reaches the
reviewer sitting in the YouTube title field, where changing it takes seconds.

---

## PHASE 3 — Descriptions + Captions (Peggy)

⛔ Peggy must have the cleaned VTT open. Cannot find it → STOP, flag to Joan.

> **Authority is `peggy-olson-copywriting/hu_description_prompt_V2.md` on `main`.
> Nothing else.** Not a local `Ai Prompt Documents/` copy, not
> `skills_to_install/youtube-description/SKILL.md`, not a prior video's file.
> If that prompt is not on `main`, the job is blocked.

Peggy delivers **five** copy outputs in one pass — YouTube, Instagram, TikTok,
Facebook short, Facebook long — plus the title from Phase 2.

**Output file:** `particles/<VID_ID>_Description_Package_v1.md`

This file is the single handoff to Betty. Every field Betty needs must be present and
labeled by platform. A missing CTA, an unlabeled platform, or a placeholder is a failed
handoff — Betty stops rather than composing a substitute.

⛔ No markdown headings or backtick fences in the YouTube description body. YouTube
renders them literally.

**No gate here — which is why the checks above are strict.** No human reads this copy until
it is already in YouTube and the Metricool planner. The machine checks are doing the work a
sign-off used to do.

> ✅ ClickUp: mark **"Generate SEO title & description"**, then brief Salvatore.

---

## PHASE 4 — Thumbnails (Salvatore)

**Read first:** `brands/handwriting-university.md` §4–§8 (palette, typography, master image
prompts), then `salvatore-art-department/Salvator_AI_Graphics_SOP_v1.md`.

⛔ **Mandatory first step:** study 8–10 approved thumbnails in
`Salvadore - art department/thumbnails May 2026/` before writing any Gemini prompt. Output
must look like it belongs in that folder.

**Deliverable A — YouTube thumbnail, 16:9.** Run on Bart's Mac via Desktop Commander
(Gemini is 403-blocked in sandbox).

- Palette and typography: **`brands/handwriting-university.md` §3–§4.** Do not take them
  from this file or from a previous thumbnail.
- Headshots: real only. ⛔ Never `Bart_MG_1770_attorney_shot.png` — QDE lane only.
- Trait graphic: real handwriting from
  `betty/HU trait reference library (local copy)/rendered_hires/page-XX.png`.
  **Never AI-generated handwriting strokes.** Absolute rule.
- Plate must be dark and low-key — the host is the only lit element.
- BANNED: PIL hand-composite · AI handwriting · red
- ⛔ Must be 16:9. Never a file with `ig_reel` in the name.
- Generate 4 concepts (A/B/C/D), combine into a 2×2 grid, select the strongest.

**Deliverable B — Instagram Reel cover, 9:16, 1080×1920, 300 DPI, JPG 92%+.**
HU preferred: real video frame grab (Style 2 — LOCKED 2026-07-11). Two variations.

**No gate here.** A thumbnail the reviewer rejects re-runs this phase alone and swaps on the
live video. That is a redo, not a failure.

> ✅ ClickUp: mark **"Create thumbnail(s)"** and **"Archive final approved assets"**,
> then brief Betty.

---

## PHASE 5 — Vertical 9:16 Cut (Betty)

**Governing doc:** `betty-social-media-manager/Betty_SOP_VideoSmimeo_IG_Resize_Normalize_v1.md`
⚠️ Not committed — see OPEN FLAGS #4. Until it is, Phase 5 runs on the recipe below alone.

1. Check for an editor-made vertical cut (filename contains `TIKTOK`, `Vertical`, `9x16`).
   **ffprobe it** — confirm 1080×1920. If good → skip to Phase 6.
2. If only a landscape master exists, build the blurred fill:

```bash
ffmpeg -y -i <land>.mp4 -vf "split[a][b];\
[b]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:6[bg];\
[a]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1" \
-c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 128k <vid>-9x16.mp4
```

   Never crop the face. Output `<base>_IG_9x16_v1.mp4` — v1/v2/v3, never "final".
   Verify with ffprobe (a "moov atom not found" error means an incomplete download — re-run).
3. **Duration over 3 min → STOP and ask the reviewer.** Trim or full length is their call.

> ✅ ClickUp: mark **"Assemble Essential Asset Bucket"**, then proceed to Phase 6.

---

## PHASE 6 — YouTube Upload (Betty)

⛔ Title ✓ + `<VID_ID>_Description_Package_v1.md` ✓ + 16:9 thumbnail ✓ all in hand, or STOP.

1. **Direct terminal upload with the `yutu` CLI, from a local file path.** Not YouTube
   Studio, not a Chrome session. rclone the final render down from Drive first — `yutu`
   needs a real local path.
2. Upload to channel `UCG-DLule9ZSStBdc5gSEoCw` (`@handwritinguniversity`).
3. Visibility: **PRIVATE**. Never Unlisted, Public, or Scheduled at this stage.
4. Add to the correct playlist. Wait for HD processing.
5. Set the title and the YouTube description **verbatim from
   `<VID_ID>_Description_Package_v1.md`.** Betty does not trim, rewrite, or re-order.
   ⛔ Check for markdown artifacts before saving — no `###`, no backtick fences.
6. Set the 16:9 thumbnail.
7. **Leave PRIVATE.** The reviewer making it public is the approval. Betty never changes
   visibility.

⛔ Do not upload captions yet.

> ✅ ClickUp: mark **"Handoff to Betty"**, then proceed to Phase 7.

---

## PHASE 7 — Caption Upload (Betty · LAST YOUTUBE STEP)

Runs after the description is set ✓ and the thumbnail is set ✓. It does not wait on the
reviewer — captions on a private video harm nothing, and doing it now means the reviewer
sees the finished article.

1. Use the cleaned VTT from Phase 1 (the non-`RAW` file).
2. Upload as the English track, **with timing**. ⛔ This step is **not** `yutu` — see
   the caption-upload procedure, which is a separate tool.
3. Spot-check the opening hook and 3–4 random points.
4. Verify the track lists as `trackKind: standard` (not `asr`).
5. Privacy is not changed by this step.

---

## PHASE 8 — Media + Metricool Drafts (Betty)

⛔ Confirm all five caption outputs are present in `<VID_ID>_Description_Package_v1.md`.

### Step 1 — The media URL

**Default path: hand Metricool the Google Drive URL of the vertical 9:16 cut.** Metricool
uploads Drive files into its own storage automatically, provided Google Drive is linked in
the Metricool account (⚠️ OPEN FLAGS #2). Nothing is staged, copied, or deleted.

**Fallback — the FTP bridge.** Use this *only* when the Drive URL fails with
`Failed to normalize media`, which happens when the file is **owner-only to an editor's
Google account** and Metricool's fetch gets Google's HTML interstitial instead of the mp4.
Never retry the Drive link in that case; bridge it.

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

### Step 2 — Four separate drafts

⛔ **One `createScheduledPost` call per network, every one `draft: true`.** Four networks =
four drafts, same media URL. Bundling forces one caption onto every platform, because
Metricool exposes a single shared `text` field per post — only `tiktokData.title` and
`facebookData.title` are per-network.

⛔ **Betty sets no publish time and never schedules.** The reviewer does that.

| Draft | Providers | networkData | Copy (verbatim from `<VID_ID>_Description_Package_v1.md`) |
|---|---|---|---|
| 1 | `tiktok` | `{title: <hook>, privacyOption: "PUBLIC_TO_EVERYONE"}` | TikTok caption |
| 2 | `instagram` | `{type: "REEL", showReelOnFeed: true}` | Instagram caption |
| 3 | `facebook` | `{type: "POST", title: <video title>}` | Facebook **long** |
| 4 | `facebook` | `{type: "REEL", title: <video title>}` | Facebook **short** |

**YouTube:** the video is already on the channel from Phase 6, so **do not create a YouTube
Metricool draft** — it would duplicate.

**Facebook REEL vs POST** — decide by ffprobe, never by guess:
- Vertical **and** under 90 seconds → REEL is valid
- Landscape or over 90 seconds → POST only. Never send a landscape file to a Reel.

**Video covers:** omit `videoThumbnailUrl` unless you have a public URL and the post meets
Metricool's conditions. Sent speculatively, it rejects the entire request with
`VIDEO_THUMBNAIL_NOT_APPLICABLE`.

### Step 3 — Verify, then clean up

Run `getScheduledPosts` and confirm, for each of the four: it exists, `draft: true`, the
correct `type`, its own distinct caption, `HandwritingUniversity.com` present, no "link in
bio", and `media` now a `static.metricool.com` URL.

**Only if the bridge was used**, and only once `media` shows `static.metricool.com`, delete
the temp file:

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

⛔ Deleting before Metricool holds its own copy empties the draft before anyone schedules
it. ⛔ This temp file is the **only** thing Betty ever deletes. Never delete from Drive.

> ✅ ClickUp: mark **"Drafted for TikTok / Instagram / Facebook"**.
> ⛔ X/Twitter and LinkedIn — SKIP, not in the HU network set.

---

## PHASE 9 — Verify, Notify, Log (Joan)

Run the full check **before** the reviewer is notified. Nothing reaches them half-staged.

**YouTube — private:**
- [ ] Title and description match `<VID_ID>_Description_Package_v1.md` verbatim
- [ ] No markdown artifacts
- [ ] Thumbnail set, 16:9
- [ ] Captions uploaded, `trackKind: standard`, spot-checked
- [ ] Correct playlist · correct channel · **still PRIVATE**

**Metricool — all four drafts:**
- [ ] Four drafts exist, `draft: true`, none scheduled
- [ ] Correct type per network, decided by ffprobe
- [ ] Each has its own distinct caption
- [ ] Every caption contains `HandwritingUniversity.com` and a CTA
- [ ] No caption contains "link in bio"
- [ ] `media` is a `static.metricool.com` URL

**Notify the reviewer — one message:** the YouTube link, the Metricool planner link, what
is waiting on them, and any flags or exceptions. Then remind every few days until the video
is public and the drafts are scheduled.

**Ledger:** append to `betty/hu_syndication_ledger.json` —
`{driveFileId, vid, title, stagedAt, platforms, clickupTaskId, runDate}`.
Never delete entries.

---

## OPEN FLAGS

1. **Client approval has no confirmed data source.** V9 Phase 0 Gate 2 said find
   "Approved By Client" by header in the Video Production MASTER sheet. The Pre-Flight
   checklist says Zeeshan worksheet, Column O. Neither has been confirmed to exist, and no
   "Approved By Client" column has been found on the Workflow tab. **Until this is
   settled, Gate 2 fails closed.** This is the single most consequential open item in the
   pipeline.
2. **Is Google Drive linked in the Metricool account?** Metricool's documentation says
   Drive files upload automatically when it is. `getBrandSettings` exposes only the
   connected social accounts, so this can only be checked in Metricool's own settings. If
   it is linked, the FTP bridge can be deleted from Phase 8 entirely.
3. **Does a hand-scheduled draft land at `autoPublish: true`?** If the Metricool web
   planner defaults a scheduled draft to manual-publish, the review gate silently
   reintroduces the failure it was built to prevent, at the last possible step. **Test
   once before any video runs this path:** schedule one draft by hand, then read it back
   with `getScheduledPosts`.
4. **`Betty_SOP_VideoSmimeo_IG_Resize_Normalize_v1.md` is named as the Phase 5 governing
   doc but was never committed.** Under this repo's own rule that is a blocked job.
5. **`joan-supervising-agent/README.md` is still live and is a duplicate of this pipeline.**
   It predates V10, still carries the withdrawn YouTube Studio instruction, and is what
   GitHub renders on the folder page. Delete it — `README_V2.md` replaces it.
6. **CTA variants** — two approved CTAs in circulation. Confirm which is canonical.
7. **`BART_BAGGETT_VOICE.MD` is committed three times** — `brands/`, `betty/`, `peggy/`,
   all identical. Keep `brands/`. Delete the other two.
8. **Bart Show / BAB** — `brands/bartallanbaggett-brand.md` exists, but no description
   prompt and no pipeline do.
