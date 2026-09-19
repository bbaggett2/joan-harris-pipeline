# 01 — HU Pickup and brand
**V1 · 2026-09-19 · Governs n8n nodes: `Drive trigger (HU Ready)` · `Create queue row` · `Row exists?` · `Slack: no matching row` · `ClickUp lookup`**

## Rule
The folder a video is dropped into **is** the brand and **is** the approval to start. Resolved once, here, carried on the payload, never re-inferred.

## Nodes

**`Drive trigger (HU Ready)`** — Google Drive Trigger, event *File Created*, folder `1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv` ("3. Ready to Publish - HU brand"), poll every 5 min, **direct children only**. Filter mime `video/*`.

⛔ **Match on the folder ID, never the folder name.** IDs survive a rename; names do not.

A file in this folder is HU by definition. This trigger belongs to the HU workflow alone — it is never added to the QDE workflow, and the QDE folder is never added here. One trigger per brand folder is the whole brand-safety design (Bart, 2026-09-19).

**`Create queue row`** — Google Sheets *Get rows*, *read-only*. Look up the VID_ID on the master Workflow tab.

- `vid_id` = `{{ $json.name.match(/VID-\d{4}/)?.[0] || 'VID-' + $now.toFormat('yyMMddHHmm') }}` — from the filename if present, else a timestamp id with flag `NO_VID_ID`
- `brand` = `HU` — **fixed. It is the trigger, not a lookup.**
- `drive_file_id`, `drive_file_name`
- `long_url` = `https://drive.google.com/uc?id={{ id }}`

⛔ This node has no write operation configured and must never gain one. See file 00.

**`Row exists?`** — no matching row on the Workflow tab → **hard stop**, `Slack: no matching row`. A human creates the row; the pipeline never invents one.

**Column AM cross-check.** Human staff fill column AM ("Delivery File Name (Bart)") with the exact upload filename before every run. AM is a **cross-check, not the lookup key** — the VID_ID lookup stays primary, and AM is asserted against the Drive filename on the matched row. Comparison is trim + case-insensitive. A blank AM, a mismatch, or a VID_ID appearing on more than one row is a **hard stop**, not a warning. (Bart, 2026-09-19.)

**`ClickUp lookup`** — *Get tasks*, space `Video Production`, search by `vid_id`. Found → `clickup_task_id` on the payload. Not found → flag `NO_CLICKUP_TASK` and **continue**; the reviewer sees the flag in Slack. Task creation stays human-only.

## Stops
- File is not a video → ignore silently.
- No matching sheet row → hard stop, Slack.
- AM blank, mismatched, or VID_ID duplicated → hard stop, Slack.
- Brand will not resolve, or content straddles two brands → hard stop. **Never pick.**

## Flags
`NO_VID_ID` · `NO_CLICKUP_TASK`
