# HU Video Pipeline

The Handwriting University video publishing lane, one file per step.

**Start at `00_HU_OVERVIEW_V2.md`.** It holds the runtime split, the hard rules, the config block, and the table of which file governs which n8n node.

## ⚠️ Renamed 2026-09-19 — and the old files still need deleting

Every step file now carries `HU` in its name: `<NN>_HU_<NAME>_V<n>.md`. The bare names collided with the QDE step files one directory up, where a file opened by name alone could be the wrong brand's.

**The V1-named originals were not removed** — the tooling used to write the new ones cannot delete. Until these fourteen are deleted, the repo is in breach of its own "never two live" rule:

```
00_OVERVIEW_V1.md          07_THUMBNAIL_V1.md
01_PICKUP_AND_BRAND_V1.md  08_VERTICAL_CUT_V1.md
02_MEDIA_FACTS_V1.md       09_YOUTUBE_V1.md
03_VTT_CLEAN_V1.md         10_METRICOOL_DRAFTS_V1.md
04_TITLE_V1.md             11_PREFLIGHT_V1.md
05_DESCRIPTION_V1.md       12_VERIFY_NOTIFY_V1.md
06_CAPTIONS_V1.md          13_REGENERATE_V1.md
```

Also delete, both superseded:
- `HU_Clone_SOP_v2.md` — replaced by `HU_CLONE_RUNBOOK_V3.md`
- `hu_description_prompt_V2.md` — a duplicate; what gets written lives in `peggy-olson-copywriting/`

## Files

| File | Step |
|---|---|
| `00_HU_OVERVIEW_V2.md` | The model, hard rules, config, open flags, the QDE source lane |
| `01_HU_PICKUP_AND_BRAND_V1.md` | Drive trigger, brand resolution, row + AM cross-check, ClickUp |
| `02_HU_MEDIA_FACTS_V2.md` | Aspect, duration, byte size, `yt_format` |
| `03_HU_VTT_CLEAN_V2.md` | Transcript fetch, cleaning, correction vocabulary, Shorts caption style |
| `04_HU_TITLE_V1.md` | Title mechanics (no voice rules) |
| `05_HU_DESCRIPTION_V2.md` | The copy JSON contract — five outputs |
| `06_HU_CAPTIONS_V1.md` | Social caption mechanics (no voice rules) |
| `07_HU_THUMBNAIL_V2.md` | HU thumbnail — Mac-side build, not an n8n node |
| `08_HU_VERTICAL_CUT_V1.md` | The 9:16 cut and `vertical_url` registration — **live for HU** |
| `09_HU_YOUTUBE_V2.md` | Upload, thumbnail set, caption insert, the Mac worker, the ⚠️ branch |
| `10_HU_METRICOOL_DRAFTS_V2.md` | Four drafts, the slot picker, verification |
| `11_HU_PREFLIGHT_V2.md` | Brand-lane and structural assertions |
| `12_HU_VERIFY_NOTIFY_V1.md` | Destination reads, reviewer notice, daily sweep |
| `13_HU_REGENERATE_V1.md` | The three regenerate forms |
| `HU_CLONE_RUNBOOK_V3.md` | Sequencing and the authorization register for building the lane |

Files at V1 are byte-identical to their originals apart from the name and the H1. Files at V2 changed on 2026-09-19.

## What changed on 2026-09-19

The QDE lane had a working day and one video ran end to end. Three defects were root-caused and fixed:

1. **Thumbnails never landed** — `yutu` silently refuses an absolute `--file` path, prints its usage text and exits 0. Fixed, proven, thumbnail visibly displaying (file 09).
2. **Captions always failed** — `fix_vtt_hours()` corrupted every timestamp it touched, so YouTube was rejecting malformed WebVTT. It was never a readiness race. Fixed, `serving` on the first attempt (file 09).
3. **Success was reported on incomplete publishes** — a warning branch now fires when the thumbnail or captions do not land (file 09).

**Two of the three fixes are brand-agnostic.** `make_16x9()` and `fix_vtt_hours()` both live in the single `worker.py` that serves both brands, so HU inherits them. Only the warning branch has to be cloned.

## Versioning
The version lives in the filename; the highest number is current; every change bumps the file you changed and nothing else. **A new revision deletes the old file in the same commit — never two live.**

Cross-references never name an exact version: `Something_V<n>.md` means *the highest-numbered file of that name in that folder*. References by step number ("file 09") are stable across renames and are preferred.

## What this replaces
`joan-supervising-agent/HU_Video_Publishing_Pipeline_V15.md` and `..._V14.md`, both now pointer stubs. V15 described the HU lane as an agent-to-agent process and said itself that it did not include the n8n workflow. V14 was a misfiled copy of the QDE document.

## Where things live that are not here
- Voice, palette, typography, banned terms, master image prompts, QA checklist → `brands/handwriting-university.md`
- Host voice → `brands/BART_BAGGETT_VOICE.MD`
- What gets written (titles, descriptions, captions) → `peggy-olson-copywriting/hu_description_prompt_V<n>.md`

⛔ **Never restate a brand fact in this folder.** A duplicated palette is a palette that will be wrong within a month.

## Known blockers
1. `hu_description_prompt_V3.md` exists and the lane is **not** blocked on it. The one real gap is that it has no Shorts variant (file 05).
2. The V15 thumbnail bans on "PIL hand-composite" and "red" contradict the brand kit (file 07).
3. HU assets folder and YouTube upload queue not yet created (files 00, 09).
4. ~~No n8n Cloud API key exists on the Mac.~~ **Closed 2026-09-19** — not needed. The `/rest/…` surface works through an authenticated browser session, including backups, publish and rollback (file 00, flag 6).
5. `worker.py` is still hardcoded to the QDE credential and one shared queue. **This is the highest-risk open item** — an HU job in that queue uploads to the QDE channel (file 09, B1).

## Settled
- **Alerting shares the QDE channel and ntfy topic** (Bart, 2026-09-19). HU notices lead with `HU video STAGED` so the lane is obvious at a glance — see file 12.
- **`Next open slot` is shared, not cloned** (2026-09-19). It takes `blogId` as an input and is already brand-aware — see file 10.
- **`draft: true` with `autoPublish: true` is correct** and is what Bart wants — see file 10.
