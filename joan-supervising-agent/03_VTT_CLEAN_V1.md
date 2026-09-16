# 03 — VTT clean
**V1 · 2026-09-15 · Governs n8n nodes: `VTT: fetch` · `VTT: clean` (LLM)**

## Where the VTT comes from
The editor drops `<same basename>.vtt` in the Ready folder alongside the mp4, **or** the Drive trigger finds it in `assets_folder_id/vtt/`. `VTT: fetch` searches Drive for `name contains '<basename>' and mimeType != video`.

**No VTT = the one hard stop in the copy chain.** Row → `ERROR`, `notes` = `NO_VTT`, Slack. Nothing downstream is written from a title alone (HARD RULE, unchanged).

## `VTT: clean`
LLM node. System prompt fetched at run time from `prompt_base_url + peggy-olson-copywriting/vtt_cleaner_prompt_V<n>.md` (the HU cleaner — brand-neutral). User content = raw VTT.

Rules the prompt must keep: preserve every timestamp exactly; fix the "Baggett" mis-hearings list; no rewording of meaning; output is valid WebVTT only.

Output saved to Drive `assets_folder_id/vtt/<vid_id>_clean.vtt` and its file id stored on the row (`notes` gets `VTT_CLEAN_OK`). Kept as the caption track for file 09. Raw file never deleted.

## v1 shortcut
The first-pass workflow JSON skips the clean step and uses the raw VTT as-is for both the copy prompts and the caption upload. Add the LLM clean node when the raw captions prove too dirty — that is the refinement hook.
