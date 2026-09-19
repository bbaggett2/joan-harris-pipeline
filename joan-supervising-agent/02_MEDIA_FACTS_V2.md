# 02 — Media facts
**V2 · 2026-09-19 · Governs n8n nodes: `Drive: file metadata` · `Find video` · `Media facts` (Code)**

Replaces ffprobe. Drive already knows what the file is.

**`Drive: file metadata`** — Google Drive *Get* with `fields = id,name,size,videoMediaMetadata(width,height,durationMillis),mimeType`.

## What changed in V2

**1. `yt_format` added.** V7 defines two different YouTube descriptions — Output 1 long-form (200–400 words, 12–18 hashtags, chapters) and Output 2 Shorts (150–300 **characters**, 3–5 hashtags, no chapters) — and says the choice is *"decided upstream, not by you."* Nothing upstream ever decided it. VID-4520 is vertical and 70 seconds, so a Short, and it received a 1,643-character long-form description with 17 hashtags and six chapters. `Media facts` now makes that call and file 04's node is told the answer explicitly.

**2. The V1 code sample was already well out of date** — it predated `vid_id` parsing, `long_url`, the multi-source file pick and the suffixed-ID regex. The block below is the live node.

**3. The routing table no longer sends anything to a vertical cut.** See file 08.

## `Media facts` — live code

```js
const pick = (n) => { try { return $(n).first().json; } catch (e) { return null; } };
const meta = pick('Drive: file metadata');
const found = pick('Find video');
const f = (meta && meta.id) ? meta : (found && found.id) ? found : $input.first().json;
const row = pick('Create queue row') || {};
const cfg = $('Config').first().json;
const m = f.videoMediaMetadata || {};
const bytes = Number(f.size||0);
const name = f.name || f.title || '';
const vid_id = row.VID_ID || row.vid_id || ((name.match(/VID-?\d{3,4}(-(?:IG|ZEE|MA|V\d+|S|L|A)\b)?/i)||[])[0]||'').toUpperCase().replace(/^VID-?/,'VID-') || ('VID-' + $now.toFormat('yyMMddHHmm'));
const out = { ...row, vid_id, drive_file_id: f.id, drive_file_name: name,
  long_url: 'https://drive.usercontent.google.com/download?id=' + f.id + '&export=download&confirm=t',
  width: m.width, height: m.height, duration_s: Math.round((m.durationMillis||0)/1000), bytes,
  aspect: (m.width&&m.height)?(m.height>m.width?'vertical':'landscape'):'unknown',
  over_fb_cap: bytes > cfg.facebook_cap_bytes, flags: [] };
if (!f.id) throw new Error('Media facts: no Drive file id found (checked Drive: file metadata, Find video, input)');
if (out.aspect==='unknown') out.flags.push('NO_VIDEO_METADATA');

// V7 decides the YouTube output shape upstream: vertical AND under ~3 minutes is a Short
// (V7 Output 2); everything else is long-form (Output 1).
const _dur = Number(out.duration_s) || 0;
out.yt_format = (out.aspect === 'vertical' && _dur > 0 && _dur <= 180) ? 'short' : 'long';
if (out.aspect === 'vertical' && _dur === 0) out.flags.push('FORMAT_DEFAULTED_LONG');
return [{json: out}];
```

## The VID_ID regex — do not loosen it

`/VID-?\d{3,4}(-(?:IG|ZEE|MA|V\d+|S|L|A)\b)?/i` — the suffix list is **deliberately closed**. A first attempt using `(-[A-Z0-9]+)?` over-captured `VID-4520-vertical-raw.MOV` as `VID-4520-VERTICAL` and matched no sheet row. Before this regex existed, the pattern dropped the suffix entirely, so `VID-0778-S` silently resolved to the `VID-0778` row — a different video with a different title — and reported success.

## `yt_format` truth table

| aspect | duration | `yt_format` | flags |
|---|---|---|---|
| vertical | 1–180 s | `short` | — |
| vertical | > 180 s | `long` | — |
| vertical | unknown (0) | `long` | `FORMAT_DEFAULTED_LONG` |
| landscape | any | `long` | — |
| unknown | any | `long` | `NO_VIDEO_METADATA` |

Defaulting to `long` is intentional: a long-form description on a Short is verbose, a 200-character description on a long-form upload is a hole.

## Rotation gotcha — Drive and YouTube disagree

iPhone `.MOV` files shot vertically are stored as a landscape frame plus a rotation flag. **Drive's `videoMediaMetadata` applies that rotation**, so `height > width` is correct and `aspect` comes out `vertical`. YouTube's `fileDetails` does **not** — it reports the raw stream (e.g. 3840×2160 with `rotation: clockwise`) and an `aspectRatio` of 1.777 for a video it then transcodes and serves as 9:16. Never judge orientation from YouTube's `fileDetails`; trust Drive, or the rendered player.

## Routing table

| Fact | Consequence |
|---|---|
| `aspect` | Feeds `yt_format`. For the vertical-cut lane see file 08 — note that as of 2026-09-19 no n8n node reads or writes `vertical_url`, so nothing in *this workflow* routes to it |
| `yt_format = short` | `Copy: title+description+captions` is instructed to write V7 Output 2 and return an empty `chapters` array |
| `yt_format = long` | V7 Output 1 with 4–6 chapters at exact VTT timestamps |
| `over_fb_cap` | Facebook POST is skipped, flag `FB_POST_OVER_CAP` (file 10). There is no compression step |
| `NO_VIDEO_METADATA` | Drive has not processed it yet → wait 10 min and re-read once, then flag and continue |

Writes `width height duration_s bytes` to the row.

## Refinement hook

The Short/long-form threshold or the default → this file and the `Media facts` node. What the model does with `yt_format` → the system prompt in file 04's node. How a Short's description should read → the Peggy prompt file.
