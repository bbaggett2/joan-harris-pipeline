# 03 — Transcript via Descript API (SRT → VTT → clean)
**V3 · 2026-09-16 · Governs n8n nodes: `Descript: import` · `Descript: job done?` (Webhook or poll) · `Descript: export SRT` · `VTT: build + correct` (Code) · `VTT: save`**
**Replaces V1 (wrongly made the editor supply a .vtt) and V2 (unverified Descript REST guesses). V3 uses Descript's documented REST API — base `https://descriptapi.com/v1`, Bearer token, callable from n8n's HTTP Request node per Descript's own n8n guide. No Mac, no Whisper, no human.**

## Rule (V14 HARD RULE, unchanged)
Nothing downstream is written from a title alone. The transcript is produced by this step, from the video itself, before any copy node runs. Descript's timed SRT is the source because its per-cue timing is the same output that made the 5-word caption rule work (validated 2026-05).

## Credential
n8n → Credentials → New → **Header Auth**, name `Descript API`: header `Authorization`, value `Bearer <token>`. Token is created in Descript (help.descript.com/api-and-mcp/api → "How to create your API token") **by the account that owns the QDE drive** — each token is scoped to one Drive, and Descript says not to share tokens between people. A second `Content-Type: application/json` header goes on the import node.

## Nodes

**`Descript: import`** — HTTP `POST https://descriptapi.com/v1/jobs/import/project_media`
```json
{
  "project_name": "{{ vid_id }} — {{ drive_file_name }}",
  "folder_name": "QDE Pipeline/{{ $now.toFormat('yyyy-MM') }}",
  "team_access": "view",
  "add_media": { "{{ drive_file_name }}": { "url": "{{ long_url }}", "language": "en" } },
  "add_compositions": [ { "name": "main", "clips": [ { "media": "{{ drive_file_name }}" } ] } ],
  "callback_url": "{{ n8n Webhook URL }}?vid_id={{ vid_id }}"
}
```
`long_url` must be a share-by-link Drive URL (the trigger already shares the file; if not, a `Drive: share` node precedes this). Response is immediate: `job_id`, `project_id`, `project_url`. Write `descript_project_id` to the row. Importing consumes Descript media minutes; a **402** means the plan is out of minutes → row `ERROR`, `notes` `DESCRIPT_402_MINUTES`, Slack. A **429** → wait `Retry-After` and retry once.

**`Descript: job done?`** — the workflow ends here and resumes on the **Webhook** node when Descript POSTs the job result (payload = the `GET /jobs/{job_id}` shape). Fallback if the webhook never arrives (build item): a *Wait* + `GET https://descriptapi.com/v1/jobs/{{ job_id }}` loop every 30 s, max 40, until `status` is `completed`; `failed` → `ERROR`, `notes` `DESCRIPT_IMPORT_FAILED`.

**`Descript: export SRT`** — HTTP `POST https://descriptapi.com/v1/export/transcript`
```json
{ "project_id": "{{ descript_project_id }}", "format": "srt", "include_speaker_labels": "off" }
```
Sync: the response body **is** the SRT text (n8n: Response → *File* or *Text*; do not parse as JSON). Composition id comes back in the `X-Composition-Id` header — store it, the Regenerate buttons and the pinned captions job (file 08, later) will need it.

**`VTT: build + correct`** — Code node:
1. SRT → VTT: prepend `WEBVTT\n\n`, replace `,` with `.` in timestamps, drop the numeric cue indexes.
2. Mandatory name pass from the old Betty Whisper SOP (kept verbatim): `Bert Bagot`→`Bart Baggett`, `Bagot`→`Baggett`, `\bBert\b`→`Bart`. Spelling only — never a word of meaning changes.
3. Output two strings: `vtt_raw` (as exported, corrected) and `srt_raw`.

**`VTT: save`** — Drive upload `<vid_id>_RAW.vtt` (and `_RAW.srt`) to `assets_folder_id`, shared by link; file ids to the row; `notes` gets `VTT_SOURCE:descript`. Never deleted. This VTT is the caption track file 09 uploads to YouTube and the transcript files 04–06 write from.

## Stops (API failures only — never a missing input)
`ERROR` + Slack on: 402 (minutes), import `failed`, export non-200 after one retry. There is no "no VTT" branch any more; a video without a transcript is a Descript outage, and the daily sweep (file 12) resurfaces it.

## What this retires
`Betty_SOP_Whisper_Transcription_v4.md` (local Whisper + rclone via Desktop Commander) is superseded for the QDE lane. Whisper stays installed on the Mac Studio for emergencies only.

## Later (pinned): captions burned in
The same `project_id` can be handed to `POST /jobs/agent` (Underlord) with "add captions in the house style" and then `POST /jobs/publish` for a download URL — that is the automated version of the manual black-bars-plus-CapCut-text vertical. Not built in V3.

## Refinement hook
Transcript wrong words → the correction list in `VTT: build + correct`. Wrong file imported → the `long_url` / share step in file 01. Descript cost → `language`, `team_access`, or move to a cheaper engine here without touching any other file.
