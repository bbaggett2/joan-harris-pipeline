# Prompt — fill Copy-LanePryce_V3

August 3, 2026

**Before you paste this:** re-upload `publishing-audit` in Settings → Customize →
Skills (delete, then Add the zip from `~/Downloads/publishing-audit.zip`). The
version in the Skills library is dated 7/25 and does not contain any of the rules
below. Start a NEW chat after uploading — an open chat keeps the old copy.

Run on **Joan's Mac Studio in Claude Desktop**, not the web app. Desktop Commander
and the `yutu_*` connectors are required.

---

Run the publishing-audit skill. You are Lane Pryce. Report-only for platforms —
publish, delete, close, create and assign nothing.

**Your one job this session: fill columns AC, AD and AE (Instagram, TikTok,
Facebook) for every row on the Workflow tab, plus AA and AB (YouTube Status, YT
Publish Date) where they are blank or wrong.**

## Where to write

Read `Video Production MASTER (Workflow) Copy-LanePryce_V3`
`1EO2ZdAEiVHJ9FVz5ZHY-9f0CjjngHkpMVa84nHCFpDA` — already created, a clean copy of
V2, untouched. Write your corrections into it directly this once; it is this
session's copy and V2 is the backup. Do NOT touch V2 or the base master. Do NOT
edit the AEO sheet — read-only, always.

Header is row 1; data starts row 2. Confirm the row for every VID_ID by reading
column A rather than trusting a row number from any report, including this one.

## Sources, in this order

1. **YouTube API** via `yutu_hu`, `yutu_qde`, `yutu_bartshow` — authoritative for
   privacy. Always check privacy; never take a status word from a sheet.
2. **Metricool** — HU `6267975`, QDE `6268508`. Covers 2026-05-18 forward only.
   QDE from **May 19 to Aug 7 has never been read** — that is the biggest gap.
3. **AEO Video Publishing Master Worksheet** `152bwCLMRRQlewuIIHj12XO64GLbLdsBzefRxuRaHX30`,
   tabs **ALL WIP** and **HU AEO** — READ ONLY. Carries per-platform dates back to
   February, covering the pre-Metricool window. A date there is truth. Its status
   text is not.

## Vocabulary — use exactly

UPLOADED = on YouTube, private. PUBLIC = visibility public. PUBLISHED = the whole
chain done: uploaded, thumbnail, description, captions, public, syndicated.
Unlisted is its own state. Never write "published" for a private video.

`private` is a CURRENT state, not a history — a video can be public and later
pulled. Never write "never published" from `private` alone.

## Cell values

- a date — verified
- `No Data` — inspected, nothing published, nothing could be (Bart Allan Baggett
  rows only: no TikTok, no Instagram, brand unlaunched)
- `UNVERIFIED — no connector` — The Bart Show rows; IG `thebartshowpodcast` is
  live but unreadable, and its YouTube channel has no connector
- `UNVERIFIED — pre-Metricool` — only if the AEO sheet is also silent
- never leave a cell blank after this run

`No Data` asserts an inspection. Never write it for something you could not read.

## Already verified 2026-08-06 — carry in, do not re-derive

VID-0111 `_TH7EpCpZlo` public · YT 7/14 · IG 7/17 · TT 7/17
VID-0787 `TPJ4vXCZ0ig` public · YT 7/10 · IG 7/16 · TT 7/16
VID-0790 `XObJ_DAgv5g` public · YT 7/9 · IG+TT 6/5, 7/15, 7/29 (three runs)
VID-0795 `CdlbWG8FtYw` public · YT 7/21 · IG 7/21 · TT 7/21 — AA currently says
  Unlisted, wrong
VID-0106 Vanity IG+TT **7/22** — the 7/29 now in those cells belongs to VID-0790
VID-0741 Pain Dots IG 7/14 · TT 7/14 · FB 7/14 · public twice on YouTube
  (`S-9muVkzEfw` 7/14, `3CJGAoX3euw` mid-May — sheet says 5/22, Bart says 5/19),
  both private today
VID-0816 IG 7/1 · TT 7/1
VID-0822 Ambivert IG 7/6 · TT 7/6 · never uploaded to YouTube
VID-0764 TT 7/24
VID-0759 `X80r5ThmKUI` public · YT 6/16 · TT 6/16
VID-0757 Aggressiveness IG+TT 6/8 and 7/18 · approved V3 never uploaded; only
  superseded V2 `ebwqBOnl7G0` sits unlisted
VID-0792-MA Defiance IG+FB+TT 8/6 · YouTube public 8/6, TWO copies
  (`CjZas204gP0`, `4eRpCrdqmoo`) plus a third from 6/8 (`-zFKLqhKDaA`)
VID-2601 YT 3/31 · IG 5/1 · TT 5/1
VID-2602 YT 3/31 · IG 5/2 · TT 5/2
VID-2603 YT 3/26 · IG 5/3 · TT 5/3
VID-2604 `GgjGnMXvSS0` public · YT 3/31 · IG 5/4 · TT 5/4
VID-2605 `_su-6r07C3o` public · YT 4/2 · IG 5/5 · TT 5/5
VID-0871 Emotional Regulation `VreBJnXrytk` **private** — AA says Public and AB
  says 06/10, both wrong; social = `No Data — brand not launched`

Rows needing creation: **VID-0827 Concentration** (`uzvJqPRIWD0` public, YT 7/10,
IG 7/28, TikTok deliberately pulled per VID-0109) and **VID-GD03 Talkative**
(`rC41ky23Ky0` private, IG 7/10, TT 7/10).

## Ask Bart, do not guess

- `WfY9D0Md7Ko` Small Handwriting and `qDXZZaD9P_c` Pathological Liar are private
  but carry dates — pulled after going public, or never public?
- `VID-0795VB` vs `VID-0795b` — same Mo cut? One is marked DO NOT PUBLISH.
- VID-0757a / 0757b / 0759 all claim clip 0757; the folder file named `0757b`
  contains Aggressiveness while the legend says 0757b is Self-Control.
- VID-0107 has two rows.
- Three Go-to-Hell K videos are public simultaneously.

## Output

Post the exception report in the skill's format, then a line-by-line log of every
cell you wrote (`row · VID · column · old → new · source`). Update
`state/ledger.csv` and append a dated file to `state/runs/` — the 2026-07-30 run
claimed both and wrote neither, which is why nothing carried forward.
