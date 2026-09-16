# 12 — Verify, mark STAGED, notify, ledger
**V1 · 2026-09-15 · Governs n8n nodes: `Verify + collect` · `Mark STAGED` · `Slack: reviewer` · `Ledger append` · `Daily sweep` (schedule, build item)**

## `Verify + collect` — asserts, does not fix
YouTube: `videos.list` shows `privacyStatus = private`, title/description equal the row, thumbnail present, caption track `standard`. Metricool: file 10's verify result. Any failed assertion → flag `VERIFY_<what>`; the row still goes to STAGED so the reviewer can see it.

## `Mark STAGED`
Sheets *Update* by `vid_id`: `status = STAGED`, `staged_at`, `youtube_id`, the four Metricool ids, `publish_date`, `notes = flags joined ' | '`.

## `Slack: reviewer` — one message to `qde-video-review`
```
QDE video STAGED — <vid_id> · <title>
⚠️ TO VERIFY (<n>): <items>            ← first line whenever n > 0
YouTube (private): https://studio.youtube.com/video/<id>/edit
Metricool drafts (<publish_date>): TikTok · Instagram · FB POST · FB REEL — <planner link>
Flags: <list or none>
Gate 7 before going public: statutes/jurisdictions · credentials · timestamps vs VTT · no outcome claims · no HU framing · no HandwritingExpert.com · no pricing
Regenerate: thumbnail <form> · description <form> · captions <form>
```
Then the reviewer makes it public and schedules the drafts. **That is the approval.**

## `Ledger append`
Tab `ledger`: `{vid_id, brand, drive_file_id, title, youtube_id, staged_at, platforms, clickup_task_id, publish_date}`. Append only. Never deleted.

## `Daily sweep` (schedule 08:00 CT)
Reads the sheet and posts one Slack digest: rows STAGED > 3 days and still private/unscheduled (reminder), rows at `NEEDS_*` > 2 h (Mac worker down?), rows at `ERROR`. Reads only; changes nothing.

## Refinement hook
Notice wording → here. What counts as verified → the assertions list.
