# 01 — Pickup and brand
**V1 · 2026-09-15 · Governs n8n nodes: `Drive trigger (QDE Ready)` · `Create queue row` · `ClickUp lookup`**

## Rule
The folder a video is dropped into **is** the brand and **is** the approval to start. Resolved once, here, written to the row, never re-inferred.

## Nodes

**`Drive trigger (QDE Ready)`** — Google Drive Trigger, event *File Created*, folder `132glSPYurgEtU1ZkNqSlA5W6NOmK5Vx0`, poll every 5 min. Filter mime `video/*`. One trigger per brand folder; the HU lane has its own workflow with its own trigger. A file in this folder is QDE by definition.

**`Create queue row`** — Google Sheets *Append*, sheet `QDE_Video_Queue` / `videos`:
- `vid_id` = `{{ $json.name.match(/VID-\d{4}/)?.[0] || 'VID-' + $now.toFormat('yyMMddHHmm') }}` — the VID_ID from the filename if present, else a timestamp id (flag `NO_VID_ID` in `notes`)
- `brand` = `QDE` (fixed — it is the trigger, not a lookup)
- `drive_file_id`, `drive_file_name`
- `status` = `READY`
- `long_url` = `https://drive.google.com/uc?id={{ id }}`

Idempotence: before appending, *Get rows* filtered `drive_file_id = {{ id }}`; if found, stop. Re-dropping a file never creates a second row.

**`ClickUp lookup`** — ClickUp node *Get tasks*, list `[TO VERIFY — QDE space]`, search by `vid_id`. Found → `clickup_task_id` on the row. Not found → flag `NO_CLICKUP_TASK` in `notes` and **continue**. (V14 stopped here. n8n does not: the reviewer sees the flag in Slack. Task creation stays human-only.)

## Stops (broken input, not approval)
- File is not a video → ignore silently.
- Sheet append fails → `ERROR` path, Slack.

## Flags this file can write
`NO_VID_ID` · `NO_CLICKUP_TASK`
