# Sources of truth

Read this every run. The single most damaging mistake available to you is
treating a record as reality.

## The authority order

| Fact | Authoritative source | Never trust for this |
|---|---|---|
| Is it live on a platform? | The platform itself (Metricool / YouTube connector) | Any spreadsheet, ClickUp |
| Does a finished file exist? | Google Drive folder listing | Spreadsheet "Finished Video Folder" column |
| What is this video called / what is it about? | Master spreadsheet | Filename (frequently wrong — see vid-id-grammar.md) |
| Was it approved? | Master spreadsheet + `-approved` in filename | ClickUp task status |
| What work remains? | The ledger, after reconciliation | ClickUp (least accurate system) |

**ClickUp is the least accurate of the four.** In the July 2026 audit it showed
nine open tasks against VID-0812, a video that had published to all six platforms
three months earlier. Treat ClickUp as a work board that has drifted, not as a
record of state.

## Canonical spreadsheets

Five files have "MASTER" in the name. Only two are canonical. If you find
yourself reading either of the others for status, stop.

| Sheet | ID | Role |
|---|---|---|
| AEO Video Publishing Master Worksheet — MASTER | `152bwCLMRRQlewuIIHj12XO64GLbLdsBzefRxuRaHX30` | **Canonical for the QDE / AEO question series (Q1–Q59).** Has per-platform published columns. |
| Video Production MASTER (Workflow) Bart Baggett_V4 most current | `1EO2ZdAEiVHJ9FVz5ZHY-9f0CjjngHkpMVa84nHCFpDA` | **Canonical for HU as of 2026-09-20 — confirmed by Bart directly.** Workflow tab `gid=2134111827`. This is a separate lineage from Copy-LanePryce (Bart edits it himself); do not assume a `Copy-LanePryce_V#` bump supersedes it going forward — check modified time against both before choosing which to read. |
| Video Production MASTER (Workflow) | `1KwNrq2H9uJbRKy9-OfyBEjYWYI1EjTMGu5mtAW458f4` | Origin of the HU lineage. **Frozen history — do not read for status.** |
| Video Production MASTER (Workflow) Copy-LanePryce_V2_ / _V3 | `121Im_ock0A-GfE_qjp1j0tu5utosgBYiyVjvB1HvLbs` / `1ap7cNS3ozzuzxE-3snq2G4jY-keDOGLBChcGoIh4vks` | **Superseded 2026-09-20 by Bart Baggett_V4 above.** Last confirmed live 2026-08-09. Do not read for status unless Bart says the V4 sheet is stale. |
| Zeeshan Video Publishing Master | `1mUn5jNXUu8pUSsPoS_zly8LicpVRiNOlLcL9Hj4Bc6k` | Superseded. Read-only. |
| Video_Production_MASTER__for_approval__v1 | `1Ld--_76Rtwrg4N7qBYMO4AVnWD2mgxvfeTp0lcWeguI` | Abandoned draft. Ignore. |
| QDE_Metricool_Mobile_Inventory_v1 | `1NYLqygb8cHzvTv-aXjkMb-Nguo1l5xm6Ja5jHzOT5Oc` | Point-in-time inventory. Not a tracker. |

**Known cross-sheet conflict:** the two canonical sheets disagree on VID-0814 —
the AEO sheet says "STILL TO BE PUBLISHED APRIL 17 2026", the workflow sheet says
"Published / Syndicated". Where they conflict, neither wins: read the platform
and report `SHEET_CONFLICT`.

## Google Drive folders

| Folder | ID | What it actually contains |
|---|---|---|
| HU ready-to-publish | `1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv` | 15 video files + 1 subfolder. Live queue. |
| QDE / HEI ready-to-publish | `132glSPYurgEtU1ZkNqSlA5W6NOmK5Vx0` | 5 video files. Live queue. |
| "Videos ready to be published are here" | `1U6oCZlMrsU-NVWcvps6xZ-sZ8lCwso6f` | **Misnamed.** Holds ~45 Q-series project folders from February, mostly already published. Treat as an archive, not a queue. |
| AEO master folder | `1sgniGfuuhy0iyNu11mgKVMOvXLkx1jsS` | Project root. |
| Locked folder | `1fWeycr3OE5CXvdbGchrmFJrAqL2wgfEw` | Do not write. |
| VID-0827 project folder | `1-fVm_59JbmFlwslKaY_9qa36fKz8anHJ` | Empty because its approved cut moved to ready-to-publish 2026-07-07. Emptiness here means "moved", not "approved". |

A folder named with a status message (e.g. "Kristine passed Waiting on Barts
approval Folder empty JULY 6") is a symptom, not a source. Record it as
`STATE_IN_FILENAME` and do not parse meaning from it.

## Platform reads

**Metricool** is the verification path for TikTok, Instagram, Facebook and
LinkedIn. Do not attempt to scrape those sites directly — it is unreliable and
not permitted.

| Brand | Metricool blogId | YouTube channel | TikTok | Instagram |
|---|---|---|---|---|
| Handwriting University (HU) | `6267975` | `UCG-DLule9ZSStBdc5gSEoCw` | `handwritinguniversity` | `thehandwritinguniversity` |
| Handwriting Experts Inc / QDE | `6268508` | `UCrpyI5SkE075HJaFyxO_ozQ` | `handwritingexpertsinc` | `forensichandwritingexpert` |

Timezone for both: `America/Chicago`.

**YouTube** is read through the `yutu_*` MCP connectors — `yutu_hu`,
`yutu_qde`, `yutu_bartshow`. Confirm which channel a connector points at with
`channel-list` before trusting it; the naming has not always matched. These
connectors drop intermittently and have historically required a full Claude
Desktop restart. **If a connector is unavailable, every YouTube cell that run is
`unverified` — never `no`.** Report the outage as its own line item.

## ClickUp

| Thing | ID |
|---|---|
| Active Video Projects folder | `901814480010` |
| `_Sample Video JULY Temp` (template list — never audit as real work) | `901818897770` |

Each video has its own list inside the Active Video Projects folder. Status
vocabulary is inconsistent across lists (`Open`, `to do`, `in progress`) and some
newer lists carry no due dates at all, so no single filter finds stalled work.
Normalize before comparing.

## The rule that generates most findings

> Whoever did the work does not get to mark it done.

Every "published" claim in a spreadsheet was written by the person or agent who
believed they published it. That belief is exactly what failed for seven weeks.
Read the platform.
