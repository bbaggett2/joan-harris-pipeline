# 02 — Media facts
**V1 · 2026-09-19 · Governs n8n nodes: `Drive: file metadata` · `Media facts` (Code)**

## Rule
ffprobe-class facts tell you what a file **is** — aspect, duration, byte size. They never decide whether to trim anything, and they no longer decide a Facebook type. Confirm from the file, never from the filename.

## `Media facts` computes

| Field | How | Used by |
|---|---|---|
| `width`, `height` | file metadata / ffprobe on the Mac | routing, file 08, file 10 |
| `duration_s` | same | `yt_format` |
| `bytes` | Drive metadata | `over_fb_cap` |
| `long_url` | `https://drive.google.com/uc?id=<id>` | file 09, file 10 FB POST |
| `yt_format` | vertical **and** `duration_s <= 180` → `short`, else `long`. Unknown aspect or duration → `long` with flag `FORMAT_DEFAULTED_LONG` | file 05 — decides which YouTube description shape is written |
| `over_fb_cap` | `bytes > 524288000` | file 10 — skips the FB POST with flag `FB_POST_OVER_CAP` |

`yt_format` exists because a 70-second vertical Short was getting the long-form description treatment. It is passed explicitly into the copy prompt; nothing downstream re-derives it.

## Routing facts

- `1080x1920` → vertical → TikTok · Instagram · Facebook REEL
- `1920x1080` → landscape → YouTube · Facebook POST
- **Instagram rejects horizontal video outright** — "Media upload has failed: Fatal"

⚠️ That same IG error is also thrown by **duration**; the real ceiling there is 3 minutes, not 90 seconds. Do not assume aspect when you see "Fatal."

## Ship full length, always
Duration is recorded for `yt_format` only. No platform has a duration gate. Compressing a file to clear Facebook's 500 MB cap is **not** trimming — the cut stays full length.

## Flags
`FORMAT_DEFAULTED_LONG` · `FB_POST_OVER_CAP`
