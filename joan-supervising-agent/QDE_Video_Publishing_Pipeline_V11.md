# QDE VIDEO PUBLISHING PIPELINE — V11

**Brand:** Handwriting Experts Inc. / QDE ONLY
**Date:** 2026-09-12
**Location:** `joan-supervising-agent/` — cross-agent document
**Status:** AUTHORITATIVE for QDE — supersedes V10

> **Versioning:** the version lives in the filename, the highest number is current, and
> every change bumps it. A new revision becomes `..._V12.md`, and this file is deleted in
> the same commit. Never two live.
>
> **Cross-references never name an exact version.** A file referred to below as
> `Something_V<n>.md` means *the highest-numbered `Something_V*.md` in that folder* — it
> might be V5, V6 or V8. Always take the highest.
>
> ⛔ **Keep V7 in git history** until this pipeline has run a live batch clean.

---

## WHAT CHANGED IN V11

**Cross-references no longer name an exact version.** V10 pointed at
`HU_Video_Publishing_Pipeline_V10.md` by name, which went stale the moment HU bumped. That
is the only change — every rule, phase, setting and open question is identical to V10.

<details>
<summary><strong>What changed in V10</strong> (kept as history)</summary>

Shared with the HU pipeline:

1. **YouTube upload is the `yutu` CLI**, from a local file path. V9 said YouTube Studio and
   explicitly banned `yutu`. Bart settled it 2026-09-11.
2. **Metricool posts are created as DRAFTS.** Agents never schedule.
3. **The Drive-URL ban was narrowed** to the editor-owner-only case; the FTP bridge became
   a fallback, not the procedure.
4. **Four sign-offs became one review.**
5. **"Bart" was replaced by the REVIEWER role.**

QDE-specific:

6. **Facebook page ID corrected** from `handwritingexpertsinc` (the handle) to
   `120481384817826`, read from the live Metricool account 2026-09-11.
7. **Network set filled in.** V9 left it `[TO VERIFY]`. Six networks are connected; the
   scope question was flagged, not assumed.
8. **YouTube channel filled in at Phase 6.**
9. **Gate 7 legal accuracy preserved and strengthened** as a non-skippable element of the
   single review.

</details>

---

## AUTHORITY MODEL

**GitHub is authority. The Mac is where execution happens.**

Every SOP, prompt, and brand fact is committed to `bbaggett2/joan-harris-pipeline`.
Local copies are caches. They drift. **When a local file disagrees with `main`, `main` wins.**
An uncommitted file is a blocked job, not a fallback.

**Per-video artifacts are never committed.** VTT, description package, renders, and
thumbnails are working output on the Mac.

### Where brand facts live

| Need | File |
|---|---|
| Domains, phone, credentials, banned terms, tone, palette, thumbnail house style, hashtags | `brands/qde-brand.md` |
| Host voice reference | `brands/BART_BAGGETT_VOICE.MD` |

⛔ **Never restate a brand fact here or in a prompt file.** A duplicated domain or palette
is one that will be wrong within a month — exactly what went wrong in V8.

---

## BRAND CONFIG — OPERATIONAL IDS ONLY

```
Metricool brand      : Handwriting Expert Inc
Metricool blogId     : 6268508                      (verified 2026-09-11)
Timezone             : America/Chicago              (verified 2026-09-11)
Publish time         : [TO VERIFY]  — no standing slot recorded
YouTube channel ID   : UCrpyI5SkE075HJaFyxO_ozQ     (verified 2026-09-11)
YouTube handle       : @thehandwritingexpert
TikTok               : handwritingexpertsinc        (verified 2026-09-11)
Instagram            : forensichandwritingexpert    (verified 2026-09-11)
Facebook page ID     : 120481384817826              (verified 2026-09-11 — V9 had the handle)
LinkedIn             : urn:li:organization:91412902 (connected; scope unconfirmed)
Google Business Prof.: accounts/109050590039336744861/locations/8211063081556039950
                       (connected; scope unconfirmed)
Networks             : Connected — YouTube · TikTok · Instagram · Facebook · LinkedIn · GBP
                       ⚠️ Confirm which of these receive VIDEO posts before the first batch.
                       HU runs four and skips LinkedIn; QDE is attorney-facing, so LinkedIn
                       may genuinely belong here. Do not assume either way.
Ready-to-Publish     : [TO VERIFY] — Drive folder ID
Description prompt   : peggy-olson-copywriting/qde_legal_description_prompt_V<n>.md
Thumbnail script     : Generate_QDE_Forensic_Thumbnails_v3.sh  (Salvatore's folder, Mac)
Ledger               : [TO VERIFY]
ClickUp space        : [TO VERIFY] — HU uses "Video Production"
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
✦ AGENTS CREATE DRAFTS. draft:true, no publish time. An agent never schedules.
  The reviewer schedules, and that is the approval.
✦ A SCHEDULED POST IS autoPublish:true + draft:false. autoPublish:false is
  banned outright — it is not a hold, it is a notification that silently dies.
✦ Metricool takes a Google Drive URL. The FTP bridge is a FALLBACK for files
  that are owner-only to an editor's account (Phase 8).
✦ NEVER trust a filename. ffprobe the file before you choose REEL vs POST.
✦ NEVER upload captions before the thumbnail is set on YouTube.
✦ NEVER delete any file. The FTP bridge temp file is the sole exception, and
  only after Metricool holds its own copy.
✦ NEVER post to the Joan Harris channel UCbDGkQdUKEgeDTDvqVEWoWA.
✦ NEVER invent a credential, statistic, statute, jurisdiction, or case detail.
  Mark [TO VERIFY]. EVERY TIMESTAMP IS READ OFF THE VTT, never estimated.
✦ NEVER apply HU personality/graphology framing to this lane. If content straddles,
  STOP and report to Joan.
✦ Betty publishes <VID_ID>_Description_Package_v1.md verbatim. She never edits copy.
✦ The REVIEWER is a role, not a person. Never name an individual in procedure.
✦ NOTHING PUBLISHES WITHOUT THE REVIEWER, and in this lane the review includes
  the legal-accuracy check. That check is never skipped and never automated.
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

## THE REVIEW MODEL

V9 had four sign-offs. There is now one review, and nothing publishes without it.

| Surface | How it holds | What approval looks like |
|---|---|---|
| **YouTube** | Video is PRIVATE. Nobody can see it. | The reviewer makes it public. |
| **Metricool** | All posts are drafts. A draft is not scheduled and cannot fire. | The reviewer schedules them. |

The reviewer gets **one notice** when both are staged, then a reminder every few days while
anything is still unreviewed. No approval form, no third tool.

**The REVIEWER is a configured role.** One value holds the notification address and the
accounts whose action counts as approval. Replacing the reviewer is changing that value.

### ⚠️ Gate 7 — legal accuracy is part of this review, and it is not optional

This is the one place QDE differs from HU, and it is the reason this lane cannot run
fully unattended. **Before making the video public, the reviewer confirms:**

- [ ] Every statute, jurisdiction, and case citation in the copy is accurate
- [ ] Every credential claim is accurate and current
- [ ] Every timestamp matches the VTT — not estimated, not inferred
- [ ] No outcome is promised or implied anywhere
- [ ] No HU personality/graphology framing has leaked into the copy
- [ ] `HandwritingExpert.com` appears nowhere
- [ ] No pricing appears anywhere (see OPEN FLAGS)

**No machine check clears this.** Peggy marks anything uncertain `[TO VERIFY]`, and any
`[TO VERIFY]` still present is a blocker, not a note. Copy in this lane gets quoted in
legal contexts; the cost of a wrong statute is not a bad post.

### What still blocks outright

- A vertical cut longer than 3 minutes — the reviewer decides trim or full length.
- Any missing or failed asset, missing VTT, or prompt not present on `main`.
- Content that straddles QDE and HU — STOP and report, never choose.

---

## AGENT ASSIGNMENTS

| Agent | Phases | Tools |
|---|---|---|
| **Joan** | 0, all ClickUp gates, 9 | MASTER sheet, ClickUp, Metricool read, memory |
| **Betty** | 1, 5, 6, 7, 8 | Drive, VTT cleaning, ffmpeg, rclone + `yutu` CLI, Metricool API, lftp (fallback only) |
| **Peggy** | 2 (titles), 3 (descriptions + captions) | VTT reading, brand kit, description prompt |
| **Salvatore** | 4 (all thumbnails) | Gemini via Mac (Desktop Commander), Drive |
| **Reviewer** | The single review, including Gate 7 | YouTube Studio, Metricool planner |

**Betty writes nothing. Peggy publishes nothing.** The handoff is one file:
`<VID_ID>_Description_Package_v1.md`.

⚠️ `brands/qde-brand.md` v1.0 still lists Betty as writing descriptions and captions and
Peggy as doing blog/AEO. That is the retired model. **This file governs.** Correct the
brand kit's "Read by" line at the next revision.

---

## PHASE 0 — Pre-Flight (Joan)

- **Gate 1 — Brand.** Confirm QDE. Forensic, attorney-facing, questioned documents, will
  contests, expert witness. If the content is handwriting *psychology* or personality, it
  is HU — use that pipeline. If it straddles, STOP.
- **Gate 2 — Client approval.** ⚠️ **UNRESOLVED — see OPEN FLAGS #1.** Until the real
  column is identified this gate **fails closed**: hold the video and ask the reviewer.
  Do not guess a column and do not proceed on a missing value.
- **Gate 3 — Assets, per video:**
  - [ ] Cleaned VTT in `particles/`
  - [ ] Vertical 9:16 cut confirmed by ffprobe, OR flagged for Phase 5
  - [ ] Thumbnails generated (approval happens at the single review)
- **Gate 4 — Platform settings.** Drafts only. See HARD RULES.
- **Gate 5 — ClickUp.** Find the task by VID_ID. No task = STOP, flag to Joan.
  **Joan never creates ClickUp tasks** — task creation is human-only.
- **Gate 6 — Repo freshness.** The prompt and brand kit this job needs are on `main`.
- **Gate 7 — Legal accuracy.** Carried out at the single review, not here. Phase 0's job is
  to confirm the *inputs* exist so the reviewer can do it: a VTT to check timestamps
  against, and copy with every uncertainty explicitly marked.

---

## PHASE 1 — VTT Cleaning (Betty)

Identical to the HU pipeline. See `HU_Video_Publishing_Pipeline_V<n>.md` Phase 1 for the
cleaner prompt — the caption rules and the "Baggett" correction list are brand-neutral.

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

**No gate here.** The top-ranked title is carried forward. It reaches the reviewer sitting
in the YouTube title field, where changing it takes seconds.

---

## PHASE 3 — Descriptions + Captions (Peggy)

⛔ Peggy must have the cleaned VTT open. Cannot find it → STOP, flag to Joan.

> **Authority is `peggy-olson-copywriting/qde_legal_description_prompt_V<n>.md` on `main` —
> highest `n` in that folder. Nothing else.** If it is not on `main`, the job is blocked.

**Output file:** `particles/<VID_ID>_Description_Package_v1.md`

This is the single handoff to Betty. Every output labeled by platform. A missing CTA, an
unlabeled platform, or a placeholder is a failed handoff — Betty stops rather than
composing a substitute.

⛔ No markdown headings or backtick fences in the YouTube description body.

⚠️ **Every timestamp is read off the VTT. Never estimated.** This lane is quoted in legal
contexts; an invented timestamp is worse here than anywhere else.

⚠️ **Mark every uncertainty `[TO VERIFY]`** — a statute, a jurisdiction, a credential, a
case detail, a statistic. Peggy never resolves these by guessing. They are what the
reviewer's Gate 7 check exists to clear, and any left unresolved block publication.

**No gate here — which is why the marking discipline above is absolute.** No human reads
this copy until it is already staged.

---

## PHASE 4 — Thumbnails (Salvatore)

**Read first:** `brands/qde-brand.md` — palette, thumbnail house style, prop vocabulary.

**Production:** `Generate_QDE_Forensic_Thumbnails_v3.sh` via the Gemini pipeline on the Mac
Studio (Gemini is 403-blocked in sandbox).

The house style is what makes the set read as a set:

1. Ground: deep navy, or a document/desk photograph darkened toward navy.
2. Headline: white, large, aligned opposite the subject.
3. **Exactly one word in gold.** Never two, never a gold sentence. This is the discipline
   that carries the brand.
4. Subject: Bart's face, serious, on one side — or a forensic prop where no face is used.
5. Props: magnifying glass, questioned document, signature close-up, gavel, evidence stamp,
   lab setting.
6. Red stamps sparingly (CONTESTED, FORGERY DETECTED). Never red headline text.

⛔ Never: neon, playful type, comedy framing, self-help imagery, personality-analysis
visuals, more than one gold emphasis.
⛔ Must be 16:9 for YouTube.

⚠️ **Palette hex values in the brand kit are flagged as unverified.** The authoritative
source is the generation script. Read the script, then correct the brand kit.

**No gate here.** A thumbnail the reviewer rejects re-runs this phase alone and swaps on the
live video — a redo, not a failure.

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

**Duration over 3 min → STOP and ask the reviewer.**

---

## PHASE 6 — YouTube Upload (Betty)

⛔ Title ✓ + `<VID_ID>_Description_Package_v1.md` ✓ + 16:9 thumbnail ✓ in hand, or STOP.

1. **Direct terminal upload with the `yutu` CLI, from a local file path.** Not YouTube
   Studio, not a Chrome session. rclone the final render down from Drive first — `yutu`
   needs a real local path.
2. Upload to channel `UCrpyI5SkE075HJaFyxO_ozQ` (`@thehandwritingexpert`).
   ⛔ Never the HU channel, never the Joan Harris channel.
3. Visibility: **PRIVATE**. Never Unlisted, Public, or Scheduled at this stage.
4. Add to the correct playlist. Wait for HD processing.
5. Set the title and description **verbatim** from the package.
   ⛔ Check for markdown artifacts before saving.
6. Set the 16:9 thumbnail.
7. **Leave PRIVATE.** The reviewer making it public — after the Gate 7 legal check — is the
   approval. Betty never changes visibility.

⛔ Do not upload captions yet.

---

## PHASE 7 — Caption Upload (Betty · LAST YOUTUBE STEP)

Runs after the description is set ✓ and the thumbnail is set ✓. It does not wait on the
reviewer — captions on a private video harm nothing.

1. Use the cleaned VTT from Phase 1 (the non-`RAW` file).
2. Upload as the English track, **with timing**. ⛔ Not `yutu` — caption upload is a
   separate tool from video upload.
3. Spot-check the opening and 3–4 random points.
4. Verify the track lists as `trackKind: standard` (not `asr`).

---

## PHASE 8 — Media + Metricool Drafts (Betty)

### Step 1 — The media URL

**Default path: hand Metricool the Google Drive URL of the vertical 9:16 cut.** Metricool
uploads Drive files into its own storage automatically, provided Google Drive is linked in
the Metricool account (⚠️ OPEN FLAGS #2). Nothing is staged, copied, or deleted.

**Fallback — the FTP bridge.** Use *only* when the Drive URL fails with
`Failed to normalize media`, which happens when the file is **owner-only to an editor's
Google account** and Metricool's fetch gets Google's HTML interstitial instead of the mp4.

On the Mac via Desktop Commander:

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

### Step 2 — One draft per network

⛔ **One `createScheduledPost` call per network, every one `draft: true`.** Bundling forces
one caption onto every platform, because Metricool exposes a single shared `text` field per
post — only `tiktokData.title` and `facebookData.title` are per-network.

⛔ **Betty sets no publish time and never schedules.** The reviewer does that.

⚠️ **Confirm the network scope before the first batch.** Six are connected; HU runs four and
skips LinkedIn. QDE is attorney-facing, so LinkedIn may genuinely belong — and Google
Business Profile behaves differently from the rest (a "publication" is text, a "photo" is
media and carries no text of its own). Do not send video to GBP without deciding that
deliberately.

**Facebook REEL vs POST** — decide by ffprobe, never by guess:
- Vertical **and** under 90 seconds → REEL is valid
- Landscape or over 90 seconds → POST only

**Video covers:** omit `videoThumbnailUrl` unless you have a public URL and the post meets
Metricool's conditions. Sent speculatively, it rejects the whole request with
`VIDEO_THUMBNAIL_NOT_APPLICABLE`.

### Step 3 — Verify, then clean up

Run `getScheduledPosts` and confirm, per draft: it exists, `draft: true`, correct `type`,
its own distinct caption, the phone number and `HandwritingExpertUSA.com` present,
`HandwritingExpert.com` absent, no "link in bio", no "full breakdown on YouTube", no
outcome claim, and `media` now a `static.metricool.com` URL.

**Only if the bridge was used**, and only once `media` shows `static.metricool.com`:

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

---

## PHASE 9 — Verify, Notify, Log (Joan)

Run the full check **before** the reviewer is notified.

**YouTube — private:**
- [ ] Title and description match the package verbatim, no markdown artifacts
- [ ] Thumbnail set, 16:9, exactly one gold word
- [ ] Captions uploaded, `trackKind: standard`, spot-checked
- [ ] Correct playlist · correct channel · **still PRIVATE**

**Metricool — every draft:**
- [ ] Exists, `draft: true`, none scheduled
- [ ] Correct type per network, decided by ffprobe
- [ ] Each has its own distinct caption
- [ ] Every caption carries the phone number and `HandwritingExpertUSA.com`
- [ ] `HandwritingExpert.com` appears **nowhere**
- [ ] No "link in bio", no "full breakdown on YouTube"
- [ ] No outcome claim anywhere
- [ ] No pricing anywhere
- [ ] `media` is a `static.metricool.com` URL

**Any `[TO VERIFY]` still in the copy is a blocker.** Do not notify the reviewer with
unresolved markers as though the package were finished — surface them as the first line of
the notice.

**Notify the reviewer — one message:** the YouTube link, the Metricool planner link, the
Gate 7 checklist, every `[TO VERIFY]`, and any flags. Then remind every few days until the
video is public and the drafts are scheduled.

**Ledger:** append `{driveFileId, vid, title, stagedAt, platforms, clickupTaskId, runDate}`.
Never delete entries.

---

## OPEN FLAGS

1. **Client approval has no confirmed data source.** V9 said find "Approved By Client" by
   header in the MASTER sheet; the pre-flight checklist said Zeeshan worksheet Column O;
   no such column has been found on the Workflow tab. **Gate 2 fails closed until settled.**
2. **Is Google Drive linked in the Metricool account?** Metricool's documentation says
   Drive files upload automatically when it is. Only checkable in Metricool's own settings.
   If linked, the FTP bridge can come out of Phase 8 entirely.
3. **Does a hand-scheduled draft land at `autoPublish: true`?** If the planner defaults it
   to manual-publish, the review gate silently reintroduces the failure it was built to
   prevent. **Test once before any video runs this path.**
4. **Network scope.** Six connected; which receive video posts is undecided. GBP in
   particular needs a deliberate call.
5. **Remaining `[TO VERIFY]` config:** publish time, Ready-to-Publish Drive folder ID,
   ledger path, ClickUp space. None are exposed by any connected API.
6. **Palette unverified.** Hex values in `brands/qde-brand.md` are best estimates. The
   authoritative source is `Generate_QDE_Forensic_Thumbnails_v3.sh` on the Mac. Read the
   script, correct the brand kit, remove the warning.
7. **`brands/qde-brand.md` has broken cross-references** — it points at `brands/hu.md` and
   `brands/bartallan.md`. The real filenames are `handwriting-university.md` and
   `bartallanbaggett-brand.md`.
8. **`brands/qde-brand.md` "Read by" line is stale** — it assigns descriptions and captions
   to Betty. Peggy writes.
9. **Pricing unresolved.** The brand kit flags a conflict between a tiered model and a
   $5,000 flat rate. **No pricing appears in any public copy until it is resolved.**
10. **"Free initial case review"** — confirm the offer is current before it appears in a
    consumer CTA.
