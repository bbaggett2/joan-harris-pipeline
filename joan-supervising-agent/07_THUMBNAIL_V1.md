# 07 — Thumbnail
**V1 · 2026-09-15 · Governs n8n nodes: `Thumbnail: prompt` (Code) · `OpenAI — thumbnail` (HTTP) · `Base64 → PNG` · `Upload thumbnail` · `Share thumbnail`**

16:9 for YouTube (`1536x1024` from gpt-image-1; YouTube accepts it). Same engine and credential as the daily-post lane: predefined n8n **OpenAI** credential, `POST https://api.openai.com/v1/images/generations`, `{"model":"gpt-image-1","prompt":…,"size":"1536x1024","quality":"high","moderation":"low","output_format":"png","n":1}` → `data[0].b64_json` → PNG → Drive `assets_folder_id` `<vid_id>_thumb_v<n>.png`, shared by link → `thumbnail_url`.

## `Thumbnail: prompt` builds the prompt from the row
```
Cinematic editorial YouTube thumbnail, 16:9, photoreal. Deep navy ground (#10142E) with the texture of a document examiner's desk, film grain, one warm light source from the upper left. RIGHT third: a neutral dark silhouette placeholder of a seated man in a suit, no facial features, where a photograph will be composited. LEFT: the headline "{{ title_short }}" in white bold condensed sans-serif with only the word "{{ gold_words }}" in gold (#FFE455). CENTER-LOW: {{ prop }} under a round brass magnifier, a red CONTESTED rubber stamp, a stack of dark law books with plain spines. The only text in the image is the headline. Every surface not described is plain.
```
- `title_short` = the title cut to 6 words max (thumbnails are not YouTube titles).
- `gold_words` = 1–3 consecutive words from `title_short` carrying the crime or stake (rule changed 2026-09-14: no longer exactly one word; it is a graphic choice).
- `prop` chosen by keyword from the description: will → "a handwritten will on cream paper", signature → "two signatures laid side by side", forgery → "a brass magnifier over cracked ink", default → "a questioned document".

**Positive-only language. Never a "no …" instruction** — gpt-image-1 paints the noun. Hate symbols are never requested even when the case involves them; period props carry setting.

**Faces.** Bart's face is the house style but the model cannot place a real photo. Default: silhouette placeholder + `notes` gets `FACE_COMPOSITE_PENDING`; the reviewer swaps the composited version via the Regenerate-thumbnail button (file 13) by pasting a URL. When Bart approves rendered likeness for a given video, remove the placeholder sentence in this prompt.

## Refinement hook
Thumbnails consistently wrong → this file only.
