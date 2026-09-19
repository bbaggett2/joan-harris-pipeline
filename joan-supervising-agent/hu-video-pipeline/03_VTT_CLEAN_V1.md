# 03 — VTT fetch and clean
**V1 · 2026-09-19 · Governs n8n nodes: `VTT: fetch` · `VTT: clean` · `VTT: build + correct` · `VTT: save` · `Merge VTT ref` · `VTT: to text`**

## Rule
⛔ **No title, description or caption is written without the cleaned VTT.** No VTT is a hard stop, not a "write it from the title." This is the single most-broken rule in the brand kit (`brands/handwriting-university.md` §2.2) and it is enforced here, upstream of every copy step.

## Source
A fresh transcript comes from Descript. An existing `<VID_ID>_RAW.vtt` in the assets folder is reused.

⚠️ **Descript's API cannot produce VTT.** `POST /v1/export/transcript` takes `format` from `txt|markdown|html|rtf|docx|srt` — **no vtt**, no word-level timestamps, no max-characters-per-line, no max-lines-per-card. Those four toggles are desktop-app only. Confirmed against the full 17-endpoint spec. So the lane exports **SRT** and converts. Do not re-litigate this.

⚠️ **`Merge VTT ref` must not be left at `{"mode":"combine","options":{}}`** — that configuration throws a "Fields to Match" error and blocks any video needing a fresh transcript.

## Correction rules
Authority is `betty-social-media-manager/HU_QDE_Transcription_Custom_Vocabulary_v<n>.md` on `main`, fetched at run time.

⚠️ **Known gap carried from the QDE lane:** the n8n node hardcodes 4 of the 13 correction rules and still runs the unsafe blind `Bert → Bart` swap that v2 §2b downgrades to a review flag. Until the node fetches §2c from GitHub, the list drifts. Fix this in the HU build rather than copying it forward.

Name corrections are mandatory on every file: `Bagot` / `Bagget` / `Baget` / `Bagott` → `Baggett`; `Bert Bagot` / `Mark Baggett` → `Bart Baggett`. **Bart's father is Curt — C-U-R-T, never "Kurt"** — in every document and record.

## Shorts caption style — 24 chars / 1 line
Applied **on Shorts only** (`yt_format === 'short'`), because Descript's API cannot do it. Each run records `captions_style` as `shorts-24ch-1line` or `descript-default`.

⚠️ **The split timings are interpolated, not measured.** The SRT carries no word-level timing, so each card's start is derived from character position within its parent cue. Every original cue's start and end are preserved exactly, so no drift accumulates, but the internal boundaries are estimates. Whisper (already on the Mac) is the upgrade path if it ever reads wrong on screen.

## Output
Two files kept in the assets folder: `<VID_ID>_RAW.vtt` and the cleaned file **without** `RAW` in the name. Both retained.

⛔ Captions are not uploaded here. That is file 09, and it happens **after** the thumbnail is set.

## Flags
`NO_VTT` (hard stop) · `VTT_MERGE_ERROR` · `VOCAB_RULES_PARTIAL`
