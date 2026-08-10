# Betty SOP — Automated Whisper Transcription
**Version:** v4
**Date:** 2026-08-10
**Agent:** Betty
**Repo:** https://github.com/bbaggett2/joan-harris-pipeline/tree/main/betty-social-media-manager

---

## Purpose

Betty locates the final approved video in the **Ready to Publish** folder on Google Drive, transcribes it using Whisper via rclone on the Mac, applies mandatory name corrections, and uploads the RAW VTT back to the correct location — with no human involvement at any step.

**Trigger:** No `.vtt` transcript found for this video in Google Drive.
**Output:** `<VID_ID>_RAW.vtt` saved to Google Drive in the video's associated subfolder (see Output Location below).
**Escalate to Joan only if:** this SOP fails after one full retry.

> **Existing transcript in another format?** If a `.txt` or `.docx` already exists for this video, Betty does NOT run Whisper from scratch. See **Step 2 — Existing Transcript Conversion** below.

---

## Output Location

Betty uses this logic to determine where the VTT is saved, in order:

1. **Associated named subfolder** — search the Ready to Publish folder for a subfolder whose name contains the VID ID (e.g., `VID-0758 2026 car closed minded-approved`). If found, upload the VTT there.
2. **Ready to Publish root** — if no named subfolder exists for this VID ID, upload directly to the Ready to Publish folder root alongside the video file.

**Never create a new folder.** Upload only to an existing location.

**Ready to Publish folder ID (HU brand):** `1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv`

---

## Prerequisite — rclone

rclone must be configured on the Mac with a `gdrive:` remote. To verify:

```bash
rclone listremotes
```

Expected output includes `gdrive:`. If missing, rclone needs to be set up before this SOP can run — flag to Joan.

---

## Step 1 — Check for any existing transcript in Google Drive

Before downloading or running Whisper, search the Ready to Publish folder and the associated subfolder for any existing transcript file for this VID ID:

```
parentId = '1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv' and title contains '<VID_ID>'
```

Also search inside any associated subfolder if one was found. Look for files ending in `.vtt`, `.txt`, or `.docx`.

| Found | Action |
|---|---|
| `.vtt` file exists | **STOP — this SOP is not needed.** Pass the existing VTT `fileId` to the cleaning step. |
| `.txt` or `.docx` file exists | **Go to Step 2** — convert to VTT without running Whisper from scratch. |
| Nothing found | **Skip to Step 3** — run full Whisper transcription. |

---

## Step 2 — Convert existing .TXT or .DOCX to VTT *(only if found in Step 1)*

**Sub-step 2a — Download the existing transcript:**

Use `mcp__Google_Drive__download_file_content` to get the file content.

- For `.txt`: save the plain text to `/tmp/whisper_input/transcript.txt`.
- For `.docx`: download the file to `/tmp/whisper_input/transcript.docx`, then extract text on the Mac:

```bash
python3 -c "
import docx
doc = docx.Document('/tmp/whisper_input/transcript.docx')
text = '\n'.join([p.text for p in doc.paragraphs if p.text.strip()])
with open('/tmp/whisper_input/transcript.txt', 'w') as f:
    f.write(text)
print('Extracted', len(text), 'characters')
"
```

If `python-docx` is not installed: `pip install python-docx --break-system-packages`

**Sub-step 2b — Locate the video and download it (same as Step 3 below).**

Use `mcp__Google_Drive__search_files` to find the approved video and download via rclone (follow Step 3 exactly).

**Sub-step 2c — Run Whisper with the existing transcript as a prompt:**

Betty uses Whisper's `--initial_prompt` flag to align the existing text against the audio and produce properly timed VTT cues. This gives real timestamps from the audio while preserving the existing vocabulary and phrasing:

```bash
mkdir -p /tmp/whisper_output
whisper "/tmp/whisper_input/<FILENAME>.mp4" \
  --model medium \
  --language en \
  --output_format vtt \
  --output_dir /tmp/whisper_output/ \
  --initial_prompt "$(cat /tmp/whisper_input/transcript.txt)"
```

**Then continue from Step 7** (rename, correct, pre-upload check, upload). Skip Steps 4–6.

---

## Step 3 — Locate the approved final video in Google Drive

Use `mcp__Google_Drive__search_files` to find the approved final render:

```
parentId = '1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv' and title contains '<VID_ID>' and mimeType contains 'video/'
```

Select the file with `-approved` in the name and the highest version number. Record the `title` (exact filename) and `fileId`.

**If no approved video is found:** STOP. Flag to Joan with the VID ID. Do not proceed.

---

## Step 4 — Determine the VTT output folder

Use `mcp__Google_Drive__search_files` to look for an associated subfolder:

```
parentId = '1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv' and title contains '<VID_ID>' and mimeType = 'application/vnd.google-apps.folder'
```

- If a matching subfolder is found → record its `id` as the **upload target folder ID**.
- If no subfolder is found → use the Ready to Publish root folder ID (`1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv`) as the **upload target folder ID**.

---

## Step 5 — Download the video to the Mac via rclone

Use `Desktop_Commander__start_process` to download the video using the Ready to Publish folder as the rclone root:

```bash
mkdir -p /tmp/whisper_input
rclone copy \
  --drive-root-folder-id 1yRdzkR3wGdvDDPuR2NeLRrIC6pXLKQTv \
  "gdrive:<EXACT_FILENAME>.mp4" \
  /tmp/whisper_input/
```

Replace `<EXACT_FILENAME>` with the exact `title` from Step 3.

Verify the download completed:

```bash
ls -lh /tmp/whisper_input/
```

If the file is missing or 0 bytes: retry once. If it fails again: STOP and flag to Joan.

---

## Step 6 — Run Whisper *(full transcription — no existing transcript)*

Use `Desktop_Commander__start_process` to transcribe the video:

```bash
mkdir -p /tmp/whisper_output
whisper "/tmp/whisper_input/<FILENAME>.mp4" \
  --model medium \
  --language en \
  --output_format vtt \
  --output_dir /tmp/whisper_output/
```

**Model guidance:**

| Model | When to use |
|---|---|
| `medium` | Default — all standard videos |
| `large` | Only if `medium` produces garbled output (heavy accent, dense technical content) |
| `tiny` / `base` | Never — accuracy is insufficient for publishing |

Whisper outputs `<filename>.vtt` into `/tmp/whisper_output/`.

---

## Step 7 — Rename to RAW convention

```bash
mv "/tmp/whisper_output/<filename>.vtt" "/tmp/whisper_output/<VID_ID>_RAW.vtt"
```

The `RAW` suffix is mandatory. It distinguishes the unedited Whisper output from the cleaned version. Both files must be kept in Drive — never delete the RAW.

---

## Step 8 — Run mandatory name correction pass

Run before uploading. Catches the known Baggett misspelling that Whisper consistently produces:

```bash
python3 -c "
import re
path = '/tmp/whisper_output/<VID_ID>_RAW.vtt'
with open(path, 'r') as f:
    text = f.read()
corrections = [
    (r'Bert Bagot', 'Bart Baggett'),
    (r'Bagot', 'Baggett'),
    (r'\bBert\b', 'Bart'),
]
for pattern, replacement in corrections:
    text = re.sub(pattern, replacement, text)
with open(path, 'w') as f:
    f.write(text)
print('Name correction pass complete.')
"
```

---

## Step 9 — Pre-upload duplicate check *(mandatory — prevents repeat uploads)*

**Before calling `create_file`, search the upload target folder for an existing file with the same name:**

```
parentId = '<upload target folder ID from Step 4>' and title = '<VID_ID>_RAW.vtt'
```

| Result | Action |
|---|---|
| File already exists | **STOP. Do not upload.** Record the existing `fileId` and pass it to the cleaning step. Log: "RAW VTT already present in Drive — skipping upload." |
| No file found | Proceed to Step 10. |

> **Why this step exists:** A context interruption or session resume can cause the upload to be attempted more than once. This check is the single gate that prevents duplicates. It must run every time, even if the agent believes the upload has not yet occurred.

---

## Step 10 — Upload RAW VTT to Google Drive *(only if Step 9 found no existing file)*

Use `mcp__Google_Drive__create_file` **exactly once**:

```
name:     <VID_ID>_RAW.vtt
mimeType: text/vtt
parent:   <upload target folder ID from Step 4>
content:  [contents of /tmp/whisper_output/<VID_ID>_RAW.vtt]
```

Confirm upload success and record the Drive `fileId`. **Do not call `create_file` again for this VID ID, regardless of any context interruption or session resume.**

---

## Step 11 — Clean up temp files

```bash
rm -rf /tmp/whisper_input /tmp/whisper_output
```

---

## Step 12 — Report complete

Betty reports the RAW VTT Drive `fileId` and its location to the next step. No human confirmation needed before proceeding.

---

## Decision Flow Summary

```
START
  │
  ▼
Step 1: Search Drive for existing transcript (.vtt / .txt / .docx)
  │
  ├─ .vtt found ──────────────────────────────► STOP. Pass fileId to cleaning step.
  │
  ├─ .txt or .docx found ────► Step 2 (convert) ──► Steps 7–12
  │
  └─ nothing found ──────────► Steps 3–12 (full Whisper transcription)
                                         │
                                         ▼
                               Step 9: Pre-upload duplicate check
                                         │
                               ├─ file exists ──► STOP. Use existing fileId.
                               └─ no file ──────► Step 10: Upload (once only)
```

---

## Hard Rules

| Rule | Detail |
|---|---|
| Never create a new Drive folder | Upload only to existing locations |
| Never delete the RAW VTT | Keep both RAW and cleaned versions in Drive |
| Never upload to YouTube at this step | Captions go to YouTube only in the caption upload phase |
| Never edit transcript content | Name/spelling corrections only — no paraphrasing |
| Baggett correction is mandatory | Run Step 8 on every file, every time |
| Duplicate check is mandatory | Run Step 9 before every upload — no exceptions, even on resume |
| One upload only | Call `create_file` exactly once per VID ID. If a fileId was already returned for this VID ID in this session, STOP — do not call again. |
| Escalate to Joan only on retry failure | One retry before flagging |

---

## Related files in this repo

- Voice profile: [BART_BAGGETT_VOICE.MD](https://github.com/bbaggett2/joan-harris-pipeline/blob/main/betty-social-media-manager/BART_BAGGETT_VOICE.MD)
- QDE description prompt: [qde_legal_description_prompt_V6.md](https://github.com/bbaggett2/joan-harris-pipeline/blob/main/betty-social-media-manager/qde_legal_description_prompt_V6.md)
- Repo root: [betty-social-media-manager](https://github.com/bbaggett2/joan-harris-pipeline/tree/main/betty-social-media-manager)
