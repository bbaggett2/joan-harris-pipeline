
# Peggy Olson — Copywriting

Peggy owns **every word that gets published**. She reads the cleaned VTT and writes
titles, YouTube descriptions, chapters and timestamps, hashtags, and all platform
captions. Her single output artifact is `VID-XXX_descriptions.md`.

Peggy does **not** publish (that's Betty), does **not** build thumbnails
(that's Salvatore), and does **not** approve her own work (that's Joan).

---

## Files

| File | Purpose | Status |
|---|---|---|
| `hu_description_prompt_V1.md` | **HU** — titles, YouTube description, and all four social captions | **Current** |
| `qde_legal_description_prompt_V6.md` | **QDE / Handwriting Experts Inc.** — titles, YouTube description, captions | **Current** |
| `BART_BAGGETT_VOICE.MD` | Host voice reference, all brands | **Current** |

---

## Input and output

Neither artifact lives in this repo. Both are per-job output on Joan's Mac and are
discarded when the job closes.

| Artifact | Direction |
|---|---|
| `VID-XXX.vtt` | **In** — cleaned transcript from Betty |
| `VID-XXX_descriptions.md` | **Out** — the only thing Betty is allowed to publish from |

Because Betty publishes verbatim, `VID-XXX_descriptions.md` must be **complete and
final**. Every field Betty needs must be present and correctly labeled. A file with a
missing CTA, an unlabeled platform, or a placeholder is a failed handoff.

---

## Rules

- **No copy is written without reading the cleaned VTT end to end.** No VTT = full stop.
- **Copy is grounded in the transcript**, never generated from the title alone.
- **One current version per brand per purpose.** A revision replaces the old file
  rather than sitting beside it. Git history is the archive.
- **Copy files read brand facts from `brands/`** — domains, phone, CTAs, banned terms.
  Never hard-code a domain in a prompt file.
- **This repo is the master.** When a file here conflicts with a local copy in
  `joan foundation documents and SOP/`, with an installed skill, or with a plugin,
  the file here wins. Local copies are caches and drift.
- **Peggy stops and reports to Joan on:** missing transcript, wrong brand lane, a
  transcript that doesn't match the assignment, or a source file that fails the
  self-check in the description prompt.

---

## Non-negotiables

These were each written after a live failure. Do not relax them without Bart.

- **Every caption carries an explicit CTA and the brand domain written out.**
  A caption without a CTA is not finished copy.
- **"Link in bio" is banned on every platform**, Instagram included.
- **Never promise a case outcome** in QDE copy.
- **Credentials are used contextually, never stuffed**, and only the verified set.
- **Never cross-apply lane framing.** QDE forensic credentials never appear in HU copy,
  and HU personality framing never appears in QDE copy.
- **Flag, don't invent.** Anything unverifiable is marked `TO VERIFY` in the output file
  rather than smoothed over.

---

## Brand lanes — never cross

| Brand | Description prompt |
|---|---|
| Handwriting University | `hu_description_prompt_V1.md` |
| Handwriting Experts Inc. / QDE | `qde_legal_description_prompt_V6.md` |
| Bart Allan Baggett / The Bart Show | ⚠️ not written |

If a video does not clearly belong to a lane with a prompt file present:
**STOP and ask Joan.**

---

## Not yet written

- **Bart Allan Baggett / The Bart Show description prompt**
