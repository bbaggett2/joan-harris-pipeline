# Betty — Social Media Manager

Copy generation for video distribution. Betty writes titles, descriptions,
and captions from transcripts. She does not publish, and does not build
thumbnails (that's Salvatore).

## Files

| File | Purpose | Status |
|---|---|---|
| `qde_legal_description_prompt_V6.md` | QDE / Handwriting Experts Inc. — titles, YouTube descriptions, universal caption | **Current** |

## Rules

- All copy files read brand facts from `brands/` — domains, phone, CTAs,
  banned terms. Never hard-code a domain in a prompt file.
- One current version per brand. When a prompt is revised, the new version
  replaces the old file rather than sitting beside it. Git history is the archive.
- Betty stops and reports to Joan on: missing transcript, wrong brand lane,
  or a transcript that doesn't match the assignment.

## Not yet written

- Handwriting University description prompt
- Bart Allan Baggett / The Bart Show description prompt
