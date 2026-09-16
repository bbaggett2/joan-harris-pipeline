# 06 — Captions (TikTok · Instagram · Facebook long · Facebook short)
**V1 · 2026-09-15 · Governs n8n node: `Copy: title+description+captions` (caption section)**

Four captions, four fields, one call. Output keys: `tiktok, tiktok_hook, instagram, fb_long, fb_short`.

## CAPTION RULES (fetched verbatim into the system prompt)
```
Write four captions for the same forensic-document video. Every caption is grounded in the transcript — never from the title alone. First person ("I examined"), never third person. Never promise or imply an outcome.

tiktok: under 1,000 characters. Open with the strongest sentence of the video as a hook. Also return tiktok_hook: 6 words max for the on-screen title.
instagram: under 1,000 characters. Same story, different first line.
fb_long: 120–200 words. Carries the full-length cut. May tell the whole case.
fb_short: 40–80 words. Carries the vertical cut. One idea.

Every caption ends with exactly:
1-800-980-9030
HandwritingExpertUSA.com · bartbaggett.com
then five hashtags on one line.

Banned everywhere: "link in bio", "full breakdown on YouTube", any cross-platform pointer, "graphology" outside hashtags, HandwritingExpert.com, pricing of any kind.
```

Fields → row. Preflight (file 11) repairs the CTA block if the model drops it.

## Refinement hook
Caption voice → this file. Length caps → this file. Which networks receive which caption → file 10.
