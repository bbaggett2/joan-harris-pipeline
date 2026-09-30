---
name: qde-dashboard-7day-watch
description: Daily review of the QDE Document Exam Case Summary dashboard (Google Sheet). Finds open cases that have just passed the 7-day time clock and posts a Slack alert tagging Bart Baggett and Kristine. Use for the daily scheduled "7-day clock" check, or when asked whether any case is past due, newly overdue, or at risk on the Client Dashboard. Reads and reports only; never edits the sheet or contacts clients.
---

# QDE Dashboard — 7-Day Clock Watch

## Purpose

First line of defense against past-due cases. Every day, review the Dashboard and tell Bart and Kristine, in Slack, which case has newly passed the 7-day clock so someone acts before it becomes a late case. (Pete's internal target is case-complete within 5 days of payment; 7 days is the alert line.)

## Source

- Google Sheet: **Dashboard Document Exam Case Summary**
  - Spreadsheet ID: `1xVjVNxxc7t_35jinI1oo4eXakwRILQSUpmNl0L-t7CY` (Client Dashboard link listed in `pete.md`)
  - Active tab gid: `798754215` (confirm the tab name on first run; there are several dated dashboard tabs — always use the current one)
- Read with the Google Drive connector (`read_file_content` / `search_files`). Read-only.

## Columns used (header row 1)

- A `Start Date`, B `Days Count down`, C `Client Name`, D `Person's name in question`, E `URGENT CASE NOTES`
- Checkbox stages: Documents Received, Documents Labeled?, Side by Side ordered?, Side by Side Created?, Lab Notes Written?, Received Signed Retainer Agreement, Verbal Opinion Rendered, Declaration Ordered?, and the declaration/final columns further right.
- **Finished-case columns: P and Q.** A checked/filled value in column P or Q means the case is finished. On first run, read the P and Q header names and record them here. Other columns can be located by header text.

## Procedure

1. **Read the sheet.** Skip the header, blank/empty checkbox-only rows, and section bands (e.g., the cyan "WAITING FOR PAYMENTS" row and anything below it is a separate list, not active cases).
2. **Compute days elapsed** for every row: `today − Start Date` (use the sheet's time zone). Do not trust column B blindly; if B disagrees with the computed value, use the computed value and mention the mismatch.
3. **Keep only open cases.** A case is finished, and must **never** be included in any alert count or list (newly past, still overdue, or approaching), if: column P or Q is checked/filled, **or** the row has a grey background (grey = complete). If the connector cannot return cell background colors, exclude by P/Q only and add this line to the Slack post: "Grey-row check unavailable this run — verify grey rows manually."
4. **Classify:**
   - **NEWLY PAST 7 DAYS:** open and days elapsed = **8** (first day past the 7-day clock).
   - **STILL OVERDUE:** open and days elapsed > 8. Count and list names only, oldest first, as context.
   - **APPROACHING:** open and days elapsed = 6 or 7 (optional one-line heads-up).
5. **For each NEWLY PAST case, add:** client name, start date, days elapsed, the **stage it is stuck at** (first unchecked stage in order: Documents Labeled → Side by Side → Lab Notes → Retainer → Verbal Opinion → Declaration → Final), and the `URGENT CASE NOTES` text if present.
6. **Post to Slack** (see below). If there are no NEWLY PAST cases, post nothing and tag no one (unless the owner later asks for a daily "all clear").

## Slack message

- **Post 1 — channel:** `#qde-cases-in-progress` (channel ID `C0C5RT6BA0J`), tagging all three recipients below.
- **Post 2 — direct message:** one group DM to the same three people (create with `slack_create_conversation` using their user IDs, then `slack_send_message`). If a group DM cannot be created, send individual DMs instead.
- Recipients (Slack user IDs, verified 2026-09-30):
  - Bart Baggett `<@U3KF4LQH0>`
  - Kristine S. `<@UMESJJYR0>`
  - Katie O'Connell `<@U0C1QDCRV6J>`
- Post only when there is at least one NEWLY PAST case. On days with none, post nothing, DM no one, and tag no one.
- Format (same text in the channel post and the DM):

```
7-day clock alert — <date> — <@U3KF4LQH0> <@UMESJJYR0> <@U0C1QDCRV6J>
NEWLY PAST 7 DAYS (action today):
1. <Client name> — started <date>, day <N>. Stuck at: <stage>. Notes: <notes or "none">
Still overdue (<count>): <names, oldest first>
Approaching (day 6–7): <names, or omit>
Dashboard: https://docs.google.com/spreadsheets/d/1xVjVNxxc7t_35jinI1oo4eXakwRILQSUpmNl0L-t7CY/edit
```

## Rules

- Read-only: never edit the dashboard, tick boxes, or change notes.
- Report only what the sheet says. Do not characterize the merits of a case, and never give or imply a forensic opinion.
- Include client names and case stage only; do not paste document contents or attorney strategy into Slack.
- Do not message clients. Do not assign work to Karla or Kristine in the alert; the alert surfaces the case, people decide.
- If the sheet cannot be read, the header row looks different than expected, or Slack posting fails: stop and send a push notification saying exactly what failed. Do not guess.
- If a run is missed, cases that crossed day 8 that day will not be flagged as "newly" past; they will appear under "Still overdue" the next day. Check the still-overdue list for anything that slipped through.

## Verification checklist (first run)

- Confirm the tab, the column headers, and the header names of columns P and Q.
- Confirm grey rows (e.g., finished cases) are excluded; if colors cannot be read, note it.
- Confirm a known open case's computed days match the sheet.
- Confirm the three tags and the group DM reach Bart, Kristine, and Katie.
