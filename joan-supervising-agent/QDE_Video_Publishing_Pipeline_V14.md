# QDE VIDEO PUBLISHING PIPELINE — V14

**Brand:** Handwriting Experts Inc. / QDE ONLY
**Date:** 2026-09-14
**Location:** `joan-supervising-agent/` — cross-agent document
**Status:** AUTHORITATIVE for QDE — supersedes V13

> **Versioning:** the version lives in the filename, the highest number is current, and
> every change bumps it. A new revision becomes `..._V15.md`, and this file is deleted in
> the same commit. Never two live.
>
> **Cross-references never name an exact version.** A file referred to below as
> `Something_V<n>.md` means *the highest-numbered `Something_V*.md` in that folder* — it
> might be V5, V6 or V8. Always take the highest.

---

## WHAT CHANGED IN V14

Same two corrections as HU V14, applied to this lane.

**1. Facebook's 90-second split is retired.** *(Bart, 2026-09-13.)* Facebook gets **two posts
every time** — a **POST carrying the full-length cut** and a **REEL carrying the short
vertical cut**. No duration test decides either. Reels and the feed are separate surfaces with
separate audiences; publishing one leaves the other empty.

Consequence V13 missed: **two Facebook posts need two different media files.** V13 staged only
the vertical cut. Phase 8 Step 1 now stages both, and the full-length file is where the hard
**500 MB** Metricool cap actually bites — checked by byte size, compressed first if over.
**Compressing to clear a size cap is not trimming;** the cut stays full length.

**2. Brand is resolved once, at pickup, and carried.** *(Bart, 2026-09-14.)* The
Ready-to-Publish folder the video came out of determines the brand, and that value travels
with the job to Metricool, where it selects the `blogId`. Nothing downstream re-infers it.

⛔ **This lane cannot satisfy that rule yet.** QDE's Ready-to-Publish folder ID has never been
identified, so there is nothing to resolve against — and that gap is now load-bearing, because
both the human approval *and* brand resolution depend on that folder. See OPEN FLAGS #1. Do
not reuse the HU folder ID.

⚠️ **Gate 7 — legal accuracy — is untouched.** Neither correction goes near it. It remains
part of the single review and is the reason this lane cannot run fully unattended.

⚠️ **ffprobe's job changed.** It tells you what a file **is** — aspect, duration, byte size.
It no longer decides whether to trim anything or which Facebook type to use.

<details>
<summary><strong>Earlier changes</strong> (kept as history)</summary>

**V13** — Gate 2 (client approval) deleted, the Ready-to-Publish folder became the approval;
the 3-minute duration gate deleted (ship full length, always); Instagram's 90-second ceiling
removed.

**V12** — LinkedIn URN corrected to `urn:li:person:nFfhG_fIiZ` (Bart's PERSONAL profile, not
the company page), read from the live Metricool account. Metricool `userId` recorded.

**V11** — cross-references stopped naming exact versions.

**V10** — shared with the HU pipeline: `yutu` CLI replaced YouTube Studio; Metricool posts
became drafts; the Drive-URL ban narrowed to the editor-owner-only case; four sign-offs
became one review; "Bart" became the REVIEWER role. QDE-specific: Facebook page ID corrected
to `120481384817826`, network set filled in, YouTube channel filled in, and Gate 7 legal
accuracy strengthened.

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

## BRAND RESOLUTION — HOW THE SYSTEM KNOWS WHICH LANE IT IS IN

**Resolved once, at pickup. Carried everywhere. Never re-inferred.**

The Ready-to-Publish folder a video is picked up from **is** the brand signal — a person put
it there, and which folder they chose is the decision.

| Folder | Brand |
|---|---|
| `1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv` — "3. Ready to Publish - HU brand" | HU |
| ⛔ **`[TO VERIFY]` — not yet identified** | **QDE** |
| *(none exists)* | Bart Show / BAB |

⛔ **Match on folder ID, not on the folder's name.** The name is the human-readable label and
a fallback only. IDs survive a rename; names do not.

⛔ **Until QDE's folder is identified, this lane has no brand anchor.** Joan records which
staging location each video was taken from, so the substitution is visible rather than silent,
and she never assumes QDE because a video "looks forensic."

**Where the resolved value lives, so it is still there at Metricool:**

1. **`PipelineState` row for the VID_ID**, in the master spreadsheet.
2. **`<VID_ID>_Description_Package_v1.md`** — the one file Betty reads. She takes the lane
   from the package and is forbidden from inferring it.

**Everything brand-dependent hangs off that one value** — the Metricool `blogId`, the YouTube
channel, the Facebook page ID, the LinkedIn URN, the description prompt, the thumbnail script,
CTA policy and banned terms.

⛔ **An unresolvable brand is an error, not a guess.** No folder match, or content that
straddles QDE and HU → STOP and report. Never pick. In this lane that rule is doubly strict:
HU framing in QDE copy is a Gate 7 failure.

---

## BRAND CONFIG — OPERATIONAL IDS ONLY

```
Metricool brand      : Handwriting Expert Inc
Metricool blogId     : 6268508                      ← selected by the resolved brand value
                       (HU is 6267975 — never type one from memory)
Metricool userId     : 4831552                      (verified 2026-09-12)
Timezone             : America/Chicago              (verified 2026-09-11)
Publish time         : [TO VERIFY]  — no standing slot recorded
YouTube channel ID   : UCrpyI5SkE075HJaFyxO_ozQ     (verified 2026-09-11)
YouTube handle       : @thehandwritingexpert
TikTok               : handwritingexpertsinc        (verified 2026-09-11)
Instagram            : forensichandwritingexpert    (verified 2026-09-11)
Facebook page ID     : 120481384817826              (verified 2026-09-11 — V9 had the handle)
LinkedIn             : urn:li:person:nFfhG_fIiZ     (verified 2026-09-12 — PERSONAL profile,
                       not the company page; V11 had the organization URN)
Google Business Prof.: accounts/109050590039336744861/locations/8211063081556039950
                       (connected; scope unconfirmed)
Networks             : Connected — YouTube · TikTok · Instagram · Facebook · LinkedIn · GBP
                       ⚠️ Confirm which of these receive VIDEO posts before the first batch.
                       HU runs four and skips LinkedIn; QDE is attorney-facing, so LinkedIn
                       may genuinely belong here. Do not assume either way.
Ready-to-Publish     : [TO VERIFY] — Drive folder ID not yet identified for this brand
                       ⭐ WHEN IDENTIFIED, THAT FOLDER IS BOTH THE HUMAN APPROVAL AND THE
                       BRAND SIGNAL. HU's is 1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv — do not
                       reuse it; that folder is the HU brand's.
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
✦ BRAND IS RESOLVED ONCE, FROM THE FOLDER, AND CARRIED. Never re-infer it from
  the video, the title, the copy, or the folder a second time. Unresolvable
  brand = STOP, never a guess.
✦ NEVER promise or imply a case outcome. No "win your case," no "guarantee."
✦ FIRST PERSON always. "I examined the signature," never "Bart Baggett examined."
✦ HandwritingExpertUSA.com and bartbaggett.com are BOTH this lane. Do not "correct"
  bartbaggett.com out of QDE copy.
✦ HandwritingExpert.com is BANNED — Bart does not own it. Hashtag use only.
✦ NO cross-platform pointers. No "link in bio," no "full breakdown on YouTube."
  Every CTA resolves to the phone number and the two owned domains.
✦ ONE METRICOOL POST PER NETWORK — except Facebook, which always gets TWO
  (full-length POST + short vertical REEL). Never bundle providers into one post.
✦ AGENTS CREATE DRAFTS. draft:true, no publish time. An agent never schedules.
  The reviewer schedules, and that is the approval.
✦ A SCHEDULED POST IS autoPublish:true + draft:false. autoPublish:false is
  banned outright — it is not a hold, it is a notification that silently dies.
✦ Metricool takes a Google Drive URL. The FTP bridge is a FALLBACK for files
  that are owner-only to an editor's account (Phase 8).
✦ ffprobe TELLS YOU WHAT A FILE IS — aspect, duration, byte size. It never
  decides whether to trim, and it no longer decides a Facebook type.
✦ FACEBOOK'S LIMIT IS 500 MB, NOT A DURATION. Check byte size before the POST.
✦ NEVER upload captions before the thumbnail is set on YouTube.
✦ NEVER delete any file. The FTP bridge temp file is the sole exception, and
  only after Metricool holds its own copy.
✦ NEVER post to the Joan Harris channel UCbDGkQdUKEgeDTDvqVEWoWA.
✦ NEVER invent a credential, statistic, statute, jurisdiction, or case detail.
  Mark [TO VERIFY]. EVERY TIMESTAMP IS READ OFF THE VTT, never estimated.
✦ SHIP FULL LENGTH, ALWAYS. Never trim a cut to fit a platform.
✦ NEVER apply HU personality/graphology framing to this lane. If content straddles,
  STOP and report to Joan.
✦ Betty publishes <VID_ID>_Description_Package_v1.md verbatim. She never edits copy.
✦ The REVIEWER is a role, not a person. Never name an individual in procedure.
✦ NOTHING PUBLISHES WITHOUT THE REVIEWER, and in this lane the review includes
  the legal-accuracy check. That check is never skipped and never automated.
```

### Long cuts and short cuts version independently

`S-V1` is **not** stale because `L-V6` exists — they are different deliverables, and **both
are used**: the long cut carries YouTube and the Facebook POST, the short vertical cut carries
TikTok, Instagram and the Facebook REEL.

**No platform has a duration gate any more.** Instagram's 90-second ceiling went on
2026-09-12 and Facebook's REEL/POST split on 2026-09-13. **What still routes is aspect ratio,
and for Facebook, file size.** Confirm with ffprobe, never by filename:

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height -show_entries format=duration \
  -of default=nw=1 "<file>"
ls -l "<file>"        # byte size — the Facebook POST constraint
```

- `1080x1920` → vertical → TikTok / Instagram Reel / Facebook **REEL**
- `1920x1080` → landscape → YouTube / Facebook **POST**.
  **Instagram rejects horizontal video outright.**

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

### The only two human touchpoints

1. **Someone puts the video in the Ready-to-Publish folder.** That is the approval to start,
   and it is also how the system learns the brand.
2. **The reviewer makes the video public and schedules the drafts** — after clearing the
   Gate 7 legal check below. That is the approval to publish.

**Nothing else asks a human for a decision.** Phases 0 through 9 run agent-to-agent.

### ⚠️ Gate 7 — legal accuracy is part of the second touchpoint, and it is not optional

This is the one place QDE differs from HU. **Before making the video public, the reviewer
confirms:**

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

### What still stops the pipeline — errors, not approvals

These halt because an input is broken or genuinely ambiguous. A human fixes the input;
nobody approves an output.

- Missing or unreadable cleaned VTT
- No ClickUp task for the VID_ID
- A missing or failed asset
- A prompt or brand kit not present on `main`
- **A brand that will not resolve**, or content that straddles QDE and HU
- An unresolved `[TO VERIFY]` in the copy at Phase 9

⛔ **Length is not on this list.** Ship full length, always.

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

**Fully automatic.** No gate here asks a human for a decision — each one either passes or
reports a broken input.

- **Gate 1 — Brand.** Resolve the brand from the Ready-to-Publish folder ID the video came
  from (see BRAND RESOLUTION above) and **write it to the `PipelineState` row**. Confirm it
  is QDE: forensic, attorney-facing, questioned documents, will contests, expert witness. If
  the content is handwriting *psychology* or personality, it is HU — use that pipeline. If it
  straddles, or will not resolve, STOP.
  ⛔ QDE's folder is not yet identified — record the staging location used.
- **Gate 2 — Assets, per video:**
  - [ ] Cleaned VTT in `particles/`
  - [ ] Vertical 9:16 cut confirmed by ffprobe, OR flagged for Phase 5
  - [ ] Full-length cut located and its **byte size recorded** — the Facebook POST needs it
  - [ ] Thumbnails generated (approval happens at the single review)
- **Gate 3 — Platform settings.** Drafts only. See HARD RULES.
- **Gate 4 — ClickUp.** Find the task by VID_ID. No task = STOP, flag to Joan.
  **Joan never creates ClickUp tasks** — task creation is human-only.
- **Gate 5 — Repo freshness.** The prompt and brand kit this job needs are on `main`.
- **Gate 6 — Legal-accuracy inputs.** Carried out at the single review, not here. Phase 0's
  job is to confirm the *inputs* exist so the reviewer can do it: a VTT to check timestamps
  against, and copy with every uncertainty explicitly marked.

> **Client approval is not checked here, and that is deliberate.** *(V12 and earlier had a
> Gate 2 that read the MASTER sheet for an "Approved By Client" column, failed closed
> because no such column was ever found, and stopped every video.)* **The Ready-to-Publish
> folder is the approval** — a video is in it because a person put it there. Do not
> reintroduce a spreadsheet check for a decision the folder already records.

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

⭐ **The package carries the resolved brand as a field.** Betty reads the lane from here and
nowhere else.

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

**Ship full length, always.** *(V12 and earlier stopped here and asked the reviewer to
choose trim or full length on anything over 3 minutes. That gate is deleted — Bart's
standing rule, 2026-09-12.)*

**Record the byte size of the full-length cut.** *(New in V14.)* It is not a routing
decision — it is the one thing that can block the Facebook POST at Phase 8.

> **If no short vertical cut exists and none can be built, the Facebook REEL is simply not
> created.** ⛔ Never substitute a landscape master into a Reel.

---

## PHASE 6 — YouTube Upload (Betty)

⛔ Title ✓ + `<VID_ID>_Description_Package_v1.md` ✓ + 16:9 thumbnail ✓ in hand, or STOP.

1. **Direct terminal upload with the `yutu` CLI, from a local file path.** Not YouTube
   Studio, not a Chrome session. rclone the final render down from Drive first — `yutu`
   needs a real local path.
2. Upload to the channel named by the **resolved brand** — for QDE,
   `UCrpyI5SkE075HJaFyxO_ozQ` (`@thehandwritingexpert`).
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

⛔ Read the **resolved brand** from the description package. It selects the `blogId` — QDE is
`6268508`, HU is `6267975`. Never type a `blogId` from memory and never infer the brand here.

### Step 1 — The media URLs — **two of them**

*(New in V14. V13 staged only the vertical cut, which is not enough once the Facebook POST
carries the full-length file.)*

| Media | Used by |
|---|---|
| **Vertical 9:16 cut** | TikTok · Instagram · Facebook **REEL** |
| **Full-length cut** | Facebook **POST** |

**Default path: hand Metricool the Google Drive URL of each.** Metricool uploads Drive files
into its own storage automatically, provided Google Drive is linked in the Metricool account
(⚠️ OPEN FLAGS #3). Nothing is staged, copied, or deleted.

⚠️ **Check the full-length file's byte size before creating the Facebook POST.** Metricool's
cap is **500 MB**, and this is the constraint that will actually break a job. Over it →
compress first (ffmpeg CRF 20 took 543 MB → 170 MB in a known case; VID-0771-L at 694 MB and
VID-0740 at 723 MB both needed it). **Compressing for a size cap is not trimming** — the cut
stays full length.

**Fallback — the FTP bridge.** Use *only* when a Drive URL fails with
`Failed to normalize media`, which happens when the file is **owner-only to an editor's
Google account** and Metricool's fetch gets Google's HTML interstitial instead of the mp4.

On the Mac via Desktop Commander:

```bash
SRC="<path to the file>"
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

### Step 2 — One draft per network, **two for Facebook**

⛔ **One `createScheduledPost` call per draft, every one `draft: true`.** Bundling forces
one caption onto every platform, because Metricool exposes a single shared `text` field per
post — only `tiktokData.title` and `facebookData.title` are per-network.

⛔ **Betty sets no publish time and never schedules.** The reviewer does that.

| Draft | Providers | networkData | Media | Copy |
|---|---|---|---|---|
| 1 | `tiktok` | `{title: <hook>, privacyOption: "PUBLIC_TO_EVERYONE"}` | vertical | TikTok caption |
| 2 | `instagram` | `{type: "REEL", showReelOnFeed: true}` | vertical | Instagram caption |
| 3 | `facebook` | `{type: "POST", title: <video title>}` | **full-length** | Facebook **long** |
| 4 | `facebook` | `{type: "REEL", title: <video title>}` | **vertical** | Facebook **short** |

**Facebook always gets both.** *(Bart 2026-09-13.)* Reels and the feed are separate surfaces
with separate audiences — publishing one leaves the other empty. This is two placements, not
duplicate content. **No duration test decides either type.**

**Instagram: no duration limit.** *(Changed 2026-09-12.)* A vertical cut goes to Instagram
whatever its length. **Aspect ratio still applies** — Instagram rejects horizontal video.

⚠️ **Confirm the network scope before the first batch.** Six are connected; HU runs four and
skips LinkedIn. QDE is attorney-facing, so LinkedIn may genuinely belong — and Google
Business Profile behaves differently from the rest (a "publication" is text, a "photo" is
media and carries no text of its own). Do not send video to GBP without deciding that
deliberately.

**Video covers:** omit `videoThumbnailUrl` unless you have a public URL and the post meets
Metricool's conditions. Sent speculatively, it rejects the whole request with
`VIDEO_THUMBNAIL_NOT_APPLICABLE`.

⚠️ **A failed `createScheduledPost` leaves nothing behind.** There is no partial draft in the
planner. If a whole network set fails at once, suspect the media file — a landscape master
breaks Instagram (aspect), Facebook (500 MB) and TikTok simultaneously.

⚠️ **`updateScheduledPost` reissues the post id.** Same uuid, new id, old id gone. Re-read
the post after any update and never reuse the pre-update id.

### Step 3 — Verify, then clean up

Run `getScheduledPosts` and confirm, per draft: it exists, `draft: true`, correct `type`,
the right `blogId` for the resolved brand, its own distinct caption, the phone number and
`HandwritingExpertUSA.com` present, `HandwritingExpert.com` absent, no "link in bio", no
"full breakdown on YouTube", no outcome claim, and `media` now a `static.metricool.com` URL.

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
- [ ] Correct playlist · correct channel for the resolved brand · **still PRIVATE**

**Metricool — every draft:**
- [ ] Exists, `draft: true`, none scheduled
- [ ] All on the `blogId` for the resolved brand
- [ ] **Two Facebook drafts** — a POST on the full-length cut and a REEL on the vertical cut
- [ ] The Facebook POST's media is under 500 MB
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

**Ledger:** append
`{driveFileId, vid, brand, title, stagedAt, platforms, clickupTaskId, runDate}`.
Never delete entries.

---

## OPEN FLAGS

1. **QDE's Ready-to-Publish Drive folder ID is unknown — and it is now load-bearing twice
   over.** That folder is both the human approval *and* the brand signal, so until it is
   identified this lane can satisfy neither rule. HU's is
   `1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv`; QDE needs its own. Joan records which staging
   location each video came from in the meantime.
2. **Network scope.** Six connected; which receive video posts is undecided. GBP in
   particular needs a deliberate call.
3. **Is Google Drive linked in the Metricool account?** Metricool's documentation says
   Drive files upload automatically when it is. Only checkable in Metricool's own settings.
   If linked, the FTP bridge can come out of Phase 8 entirely.
4. **Does a hand-scheduled draft land at `autoPublish: true`?** If the planner defaults it
   to manual-publish, the review gate silently reintroduces the failure it was built to
   prevent. **Test once before any video runs this path.**
5. **Remaining `[TO VERIFY]` config:** publish time, ledger path, ClickUp space. None are
   exposed by any connected API.
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

> ✅ **Closed 2026-09-12 — client approval data source.** The old flag tracked the missing
> "Approved By Client" column. It is closed because the check itself is gone: the
> Ready-to-Publish folder is the approval.
