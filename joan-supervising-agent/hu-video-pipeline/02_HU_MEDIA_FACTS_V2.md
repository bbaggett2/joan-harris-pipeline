# 02 — HU Media facts
**V2 · 2026-09-19 (evening) · Governs n8n nodes: `Drive: file metadata` · `Media facts` (Code) · Replaces `02_MEDIA_FACTS_V1.md`**

## Rule
ffprobe-class facts tell you what a file **is** — aspect, duration, byte size. They never decide whether to trim anything, and they no longer decide a Facebook type. Confirm from the file, never from the filename.

## `Media facts` computes

| Field | How | Used by |
|---|---|---|
| `width`, `height` | file metadata / ffprobe on the Mac | routing, file 08, file 10 |
| `duration_ms` | `videoMediaMetadata.durationMillis`, **unrounded** | `yt_format` |
| `duration_s` | derived for display only — **never for a decision** | reporting |
| `bytes` | Drive metadata | `over_fb_cap` |
| `long_url` | `https://drive.google.com/uc?id=<id>` | file 09, file 10 FB POST |
| `yt_format` | see the boundary rule below | file 05 — decides which YouTube description shape is written |
| `over_fb_cap` | `bytes > 524288000` | file 10 — skips the FB POST with flag `FB_POST_OVER_CAP` |

`yt_format` exists because a 70-second vertical Short was getting the long-form description treatment. It is passed explicitly into the copy prompt; nothing downstream re-derives it.

## ⚠️ The Shorts boundary — fixed in V2, and why

V1 said: *vertical **and** `duration_s <= 180` → `short`*. With `duration_s` computed as `Math.round(durationMillis / 1000)`, that rounds **toward** the ceiling and lets a video that YouTube will reject from Shorts be classed as one.

**Observed on QDE VID-9946, 2026-09-19.** `durationMillis: 180499` → `Math.round` → `180` → classed `short`. YouTube measured the real 180.499 s, rejected it from Shorts by **499 milliseconds**, displayed it as `3:01`, and filed it under Videos. The copy step had already written a 303-character Shorts description, so a three-minute video shipped with Shorts-length copy and no chapters.

**Compare milliseconds, and leave a margin.**

```js
const _ms = Number(m.durationMillis || 0);
out.duration_ms = _ms;
out.yt_format = (out.aspect === 'vertical' && _ms > 0 && _ms <= 179000) ? 'short' : 'long';
if (out.aspect === 'vertical' && _ms === 0) out.flags.push('FORMAT_DEFAULTED_LONG');
```

179,000 ms, not 180,000: an encode that lands at 180.2 s is still a normal video to YouTube, and the cost of guessing wrong is a whole video's copy written to the wrong shape. Unknown aspect or duration → `long` with flag `FORMAT_DEFAULTED_LONG`.

⚠️ **A file between 179 s and 181 s is the danger zone.** If one appears, check what YouTube actually did before trusting `yt_format` — read the video back (file 12) and confirm which shelf it landed on.

## Routing facts

- `1080x1920` → vertical → TikTok · Instagram · Facebook REEL
- `1920x1080` → landscape → YouTube · Facebook POST
- **Instagram rejects horizontal video outright** — "Media upload has failed: Fatal"

⚠️ That same IG error is also thrown by **duration**; the real ceiling there is 3 minutes, not 90 seconds. Do not assume aspect when you see "Fatal."

## Ship full length, always
Duration is recorded for `yt_format` only. No platform has a duration gate. Compressing a file to clear Facebook's 500 MB cap is **not** trimming — the cut stays full length.

## Flags
`FORMAT_DEFAULTED_LONG` · `FB_POST_OVER_CAP`
