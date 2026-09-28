# TEXAS COURTHOUSE CHANNEL — RESEARCH PHASE SOP v1
**Scope:** the research-building phase only (master list → research docs → queue rows). Modeled on "Peggy — HU Trait Research Doc v1" (n8n). Article writing, video production, and publishing get their own SOPs.
**Owner:** Bart (n8n + errors). Operator: Christine (video production, later phase). Public face: Curt Baggett — this brand is firewalled from all Bart-brand assets (see voice file, section 5).

---

## Phase 0 — Build the Master List (one-time, human + Claude)

1. Source the candidate list from the Texas Historical Commission's Texas Historic Courthouse Preservation Program (THCPP) — the restored/partially-restored courthouses, plus notable non-THCPP restorations. Texas has 254 counties; the working list is every courthouse with (a) a completed or substantial restoration and (b) photogenic architecture.
2. Each courthouse becomes ONE row in the master sheet (structure below), status `NEW`, with only identity fields filled: `post_id`, `county`, `town`, `courthouse_name`, `region`.
3. Priority order: story strength first (pilot ranking), then geographic spread so consecutive posts don't cluster in one region.

## Master Sheet Structure (new Google Sheet — never reuse a QDE/HU sheet)

| Column | Meaning | Written by |
|---|---|---|
| post_id | CH-001, CH-002 … (anchor ID, never reused) | Phase 0 |
| county / town / courthouse_name / region | identity | Phase 0 |
| status | NEW → RESEARCHED → READY → DRAFTED → PUBLISHED (+ ERROR) | automation/human |
| research_doc_url | Google Doc link written back by the research workflow | n8n |
| story_headline | the one-line best story, from the research doc | n8n |
| ready | human types READY after reviewing the research doc | human |
| blog_doc_url / blog_wp_edit_url / blog_flags | filled by the draft-writer workflow (later phase) | n8n |
| video_status / video_url | filled by the video workflow (later phase) | n8n/Christine |
| notes | anything a human wants the next stage to know | human |

## Daily Research Workflow (n8n — clone of "Peggy — HU Trait Research Doc v1")

Config node values (all retargeting lives here):
- `sheet_id`: the new master sheet (never a QDE/HU sheet ID) — "Historic Courthouses — Master Post Queue", ID 1Ve8zxD3b1jqRrIrEXy2GK-E54apOJrfptfmbFca0wWk
- `research_folder_id`: new Drive folder `/Historic Courthouses/Research Docs/`
- `prompt_url`: https://raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/historic-courthouses/copywriting/TX_Courthouse_Research_Prompt_v1.md
- `voice_url`: https://raw.githubusercontent.com/bbaggett2/joan-harris-pipeline/main/historic-courthouses/copywriting/SHERIFF_ROSCOE_VOICE.md
- `model`: claude-sonnet-4-5 with web search, `max_web_searches`: 8
- `slack_channel`: #historic-courthouses (ID C0C50HMPMU2) — never a QDE channel

Steps per run (daily, early morning):
1. Read master sheet → pick the first row where `research_doc_url` is empty (status NEW), claim it.
2. Fetch the research prompt from GitHub; substitute `[INSERT COURTHOUSE]` with `courthouse_name — town, TX`; append row context (county, region, any notes).
3. Call Claude with web search → full research document per the prompt (verified facts, ranked stories, TO VERIFY section).
4. Assemble and save the Google Doc in the research folder, named `CH-XXX — [County] County Courthouse — Research v1`.
5. Write back to the row: `research_doc_url`, `story_headline`, status `RESEARCHED`.
6. Slack the review channel: post_id, county, headline, doc link, and the TO VERIFY count.
7. No rows left → "queue empty" notice. Any failure → ERROR status + alert to Bart (only Bart fixes n8n).

## Human Review Gate (the READY step)

A human (Bart or delegate) opens each research doc and checks: the TO VERIFY list, the crime-story dignity rule, and that the ★ story is actually the best hook. Then types READY in the sheet. **Nothing advances to article drafting without READY.** Docs with unresolved TO VERIFY items that affect the main story stay un-READY until resolved.

## Standing Rules

- Firewall: no Bart-brand names, domains, credentials, or CTAs anywhere in this pipeline's prompts, sheets, or copy. Attribution: Curt Baggett (C-U-R-T); links only to curtbaggett.com.
- Never invent facts; TO VERIFY is the pressure valve.
- Superseded Drive files are never trashed — replaced files keep the old version alongside (versioned names).
- All prompts/SOPs this pipeline reads live in GitHub (raw URLs), not only in Drive.
- This SOP covers research only. The article-writer clone (Cameron pattern), image style, schema, and video SOP (Syllaby/HeyGen voice and template casting per the voice file sections 7–8) are separate documents, written when those phases start.
