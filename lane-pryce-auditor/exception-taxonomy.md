# Exception taxonomy

Every disagreement lands in exactly one bucket. Rows where all four sources agree
are **never mentioned** — silence is the reward for a healthy row, and it is what
keeps the report short enough to read.

An item that fits no bucket is reported as `UNCLASSIFIED`. Do not force it. A new
failure mode is a finding.

---

## 1. `ALREADY_LIVE` — published, never recorded

**Test:** platform read returns a live post; the canonical sheet does not record
a publish date for that platform.
**Means:** zero work outstanding. Pure bookkeeping.
**Action:** write the cell update into this session's new versioned copy
(`Copy-LanePryce_V#`). No video work.
**Example:** VID-0812 — live on YouTube 4/30, Instagram 5/1, TikTok 4/30,
Facebook 5/8, LinkedIn 5/8, X 5/9, while the workflow sheet read
"Approved - Move to Publish" and ClickUp held nine open tasks.

Expect this bucket to dominate the first run. That is good news, and you should
say so plainly in the report — it means the backlog is smaller than it looks.

---

## 2. `PHANTOM_PUBLISH` — recorded, not actually live

**Test:** sheet records a publish date; platform read finds nothing, or finds it
private/unlisted.
**Means:** someone believed they published and did not, or it was pulled.
**Action:** flag for republish. This is real work.
**Example:** the AEO sheet's own note on Q46 — *"She scheduled the old version…
I stopped it from being published, set to private."* The date stayed in the sheet.

Distinguish carefully from `unverified`. If the connector was down, this is not a
phantom publish — it is an unread platform.

---

## 3. `SYNDICATION_GAP` — live on YouTube, absent elsewhere

**Test:** YouTube live; one or more of TikTok / Instagram / Facebook / LinkedIn
has no post and no scheduled draft.
**Means:** the actual backlog. As of July 2026 the AEO sheet's YouTube column was
nearly complete while the social columns were overwhelmingly blank.
**Action:** queue for the `video-distribution` skill. Name the missing platforms
explicitly — "missing TikTok + Instagram" not "incomplete".

This is the bucket that answers Bart's observation that the counts differ across
platforms. Report it as a per-platform count, every week:

```
YouTube 58 · TikTok 31 · Instagram 27 · Facebook 12 · LinkedIn 4
```

---

## 4. `ORPHAN_FILE` — file present, no record

**Test:** a video file sits in a ready-to-publish folder; its VID ID has no row
in either canonical sheet.
**Means:** work arrived and entered no system.
**Action:** flag for a sheet row. Do not create one yourself.

---

## 5. `MISSING_ASSET` — record present, no file

**Test:** a canonical sheet row is marked approved or ready; no matching file in
Drive and no live post.
**Means:** the deliverable was lost, renamed, or never arrived.
**Action:** flag to the editor. Include the sheet's `Delivery File Name` value —
it is often the clue.

---

## 6. `STALLED_TASK` — ClickUp work open past threshold

**Test:** an open ClickUp task in the Active Video Projects folder whose video is
either fully reconciled (so the task is stale) or untouched for more than 21 days.
**Means:** either bookkeeping debt or genuinely dropped work. Sub-label which:
- `STALLED_TASK/stale` — the video is live; the task should be closed by a human.
- `STALLED_TASK/dropped` — the video is not live and nothing has moved.

**Action:** for `/dropped`, re-open and comment (only in `MODE=reassign`). For
`/stale`, report only — **you never close a task.**

Ignore the template list `901818897770` entirely. Ignore the "Weekly Metricool
analytics review (recurring weekly)" task, which is duplicated onto every video
list and is pure noise.

---

## 7. `AMBIGUOUS` — cannot be resolved without a human

Sub-labels:
- `/quarantine` — filename will not parse (see vid-id-grammar.md).
- `/collision` — one ID matches two lists or two sheet rows.
- `/version` — two versions in ready-to-publish with no current marker.
- `/sheet-conflict` — the two canonical sheets disagree.
- `/blocked` — the record explicitly says hold. Respect it, count the days.
  Examples: VID-0795b "DO NOT PUBLISH", VID-0764 "Zee's version better — DO NOT
  PUBLISH", VID-0109 pulled from TikTok for revisions 2026-06-30.

**Action:** one line each, addressed to Bart, stating the decision needed.
Never resolve these yourself.

---

## Report shape

```
WEEK OF <date> · <N> open exceptions (<prev> last week)

Platform counts   YouTube 58 · TikTok 31 · Instagram 27 · Facebook 12 · LinkedIn 4
Filename gate     17/20 passed

BOOKKEEPING ONLY — no video work (<n>)
  ALREADY_LIVE    VID-0812, VID-0838, VID-0813, VID-0774

REAL WORK (<n>)
  SYNDICATION_GAP VID-0827 missing TikTok + Instagram
  PHANTOM_PUBLISH VID-Q46 sheet says 3/24, YouTube shows private
  MISSING_ASSET   VID-0793 no file; sheet expects VIF_0793

NEEDS BART (<n>)
  AMBIGUOUS/collision  VID-0827 matches two ClickUp lists
  AMBIGUOUS/blocked    VID-0109 held 25 days

UNVERIFIED THIS RUN
  yutu_qde connector unavailable — 14 YouTube cells unread
```

If the report regularly exceeds roughly twenty lines, the buckets are too loose.
Tighten them. A report nobody reads is worse than no report.
