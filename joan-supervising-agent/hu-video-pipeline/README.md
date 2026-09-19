# HU Video Pipeline

The Handwriting University video publishing lane, one file per step.

**Start at `00_OVERVIEW_V1.md`.** It holds the runtime split, the hard rules, the config block, and the table of which file governs which n8n node.

## Files

| File | Step |
|---|---|
| `00_OVERVIEW_V1.md` | The model, hard rules, config, open flags |
| `01_PICKUP_AND_BRAND_V1.md` | Drive trigger, brand resolution, row + AM cross-check, ClickUp |
| `02_MEDIA_FACTS_V1.md` | Aspect, duration, byte size, `yt_format` |
| `03_VTT_CLEAN_V1.md` | Transcript fetch, cleaning, correction vocabulary, Shorts caption style |
| `04_TITLE_V1.md` | Title mechanics (no voice rules) |
| `05_DESCRIPTION_V1.md` | The copy JSON contract — five outputs |
| `06_CAPTIONS_V1.md` | Social caption mechanics (no voice rules) |
| `07_THUMBNAIL_V1.md` | HU thumbnail — Mac-side build, not an n8n node |
| `08_VERTICAL_CUT_V1.md` | The 9:16 cut and `vertical_url` registration — **live for HU** |
| `09_YOUTUBE_V1.md` | Upload, thumbnail set, caption insert, the Mac worker |
| `10_METRICOOL_DRAFTS_V1.md` | Four drafts, the slot picker, verification |
| `11_PREFLIGHT_V1.md` | Brand-lane and structural assertions |
| `12_VERIFY_NOTIFY_V1.md` | Destination reads, reviewer notice, daily sweep |
| `13_REGENERATE_V1.md` | The three regenerate forms |

## Versioning
The version lives in the filename; the highest number is current; every change bumps the file you changed and nothing else. **A new revision deletes the old file in the same commit — never two live.**

Cross-references never name an exact version: `Something_V<n>.md` means *the highest-numbered file of that name in that folder*.

## What this replaces
`joan-supervising-agent/HU_Video_Publishing_Pipeline_V15.md` and `..._V14.md`, both now pointer stubs. V15 described the HU lane as an agent-to-agent process and said itself that it did not include the n8n workflow. V14 was a misfiled copy of the QDE document.

## Where things live that are not here
- Voice, palette, typography, banned terms, master image prompts, QA checklist → `brands/handwriting-university.md`
- Host voice → `brands/BART_BAGGETT_VOICE.MD`
- What gets written (titles, descriptions, captions) → `peggy-olson-copywriting/hu_description_prompt_V<n>.md`

⛔ **Never restate a brand fact in this folder.** A duplicated palette is a palette that will be wrong within a month.

## Known blockers
1. `hu_description_prompt_V3.md` does not exist — the lane is blocked until it does (file 05).
2. The V15 thumbnail bans on "PIL hand-composite" and "red" contradict the brand kit (file 07).
3. HU assets folder and YouTube upload queue not yet created (files 00, 09).
4. No n8n Cloud API key exists on the Mac — needed to clone and patch the workflow with a diff and a rollback.

## Settled
- **Alerting shares the QDE channel and ntfy topic** (Bart, 2026-09-19). HU notices lead with `HU video STAGED` so the lane is obvious at a glance — see file 12.
