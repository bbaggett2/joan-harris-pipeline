# 12 — Verify, notify, ledger
**V1 · 2026-09-19 · Governs n8n nodes: `Verify + collect` · `Slack: reviewer` · `Slack: Production Complete` · `Daily sweep`**

## `Verify + collect` — asserts, does not fix

Every assertion is a **read from the destination**. Not an exit code, not a node's `executionStatus`, not a green tick.

**YouTube** (`videos.list`):
- `privacyStatus = private`
- title and description equal the copy package
- **`thumbnails.maxres` present at 1280×720** — this is the proof the custom thumbnail landed, and the thing that was silently false on every run before 2026-09-19
- **`channelId == UCG-DLule9ZSStBdc5gSEoCw`** — wrong channel is a hard stop, never a flag
- caption track `trackKind: standard`, **`status: serving`** (not `syncing`, not `failed`)

**Metricool:** file 10's verify result — four drafts, `draft: true`, `blogId 6267975`, distinct captions, `media` a `static.metricool.com` URL.

Any failed assertion → flag `VERIFY_<what>`. The run still reaches the reviewer so they can see it, except for the two hard stops (wrong channel, banned-term hard stops from file 11), which halt.

## ⛔ No sheet write, no ledger tab

The pipeline records **nothing** durable on its own. Per file 00, n8n has no write access to the master spreadsheet — not the Workflow tab, not any other tab. QDE's `Mark STAGED`, `Update Metricool row` and both `Ledger append` nodes are disabled and its "n8n ledger" tab was deleted. **Do not build HU with a sheet write "because QDE's file 12 describes one."** That file is stale.

The only record of a run is the notification at the time it happens. A human maintains the sheet by hand.

**File ledger:** append to `betty/hu_syndication_ledger.json` — `{driveFileId, vid_id, brand, title, stagedAt, platforms, clickupTaskId, publish_date, youtube_id}`. Append only, never deleted. This is a file on the Mac, not a spreadsheet tab.

## `Slack: reviewer` — one message

**Channel: `#qde-celebrity-post-review` — shared with the QDE lane.** Bart, 2026-09-19: *"everyone that needs to see it will see it."*

⭐ **Because the channel is shared, the first line must name the lane.** Every HU notice opens `HU video STAGED`; QDE's opens `QDE video STAGED`. A reader scanning the channel should never have to open a message to know which brand it belongs to. The same applies to error alerts and to the daily sweep, which reports both lanes and must label each row.

```
HU video STAGED — <vid_id> · <title>
⚠️ TO VERIFY (<n>): <items>            ← first line whenever n > 0
YouTube (private): https://studio.youtube.com/video/<id>/edit
Metricool drafts (<publish_date>): TikTok · Instagram · FB POST · FB REEL — <planner link>
Flags: <list or none>
Before going public: brand lane (no forensic framing) · no "graphology" in copy ·
  CTA to HandwritingUniversity.com · thumbnail trait is real handwriting ·
  captions spot-checked · no unverified claims
Regenerate: thumbnail <form> · description <form> · captions <form>
```

The reviewer then makes the video public and schedules the drafts. **That is the approval.**

**Error alerts carry a plain-language line.** Bart's standing rule: every failure notice ends with an `Error to Correct:` line finishing `Please have human investigate`. The raw n8n error alone is not actionable.

**ntfy:** topic `qde-pipeline-bhi-x7f2k9`, shared with QDE for the same reason. The message body carries the lane prefix.

## `Daily sweep` — 08:00 CT
Reads and reports; changes nothing. One digest covering **both lanes, each row labelled HU or QDE**: runs staged more than 3 days and still private or unscheduled; anything waiting on the Mac worker more than 2 hours (worker down?); anything at `ERROR`.

## Reminder cadence
One notice when both surfaces are staged, then a reminder every few days while anything is still unreviewed. No approval form, no third tool, no dashboard.
