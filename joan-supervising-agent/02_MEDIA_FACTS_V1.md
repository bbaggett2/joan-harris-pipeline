# 02 — Media facts
**V1 · 2026-09-15 · Governs n8n nodes: `Drive: file metadata` · `Media facts` (Code)**

Replaces ffprobe. Drive already knows what the file is.

**`Drive: file metadata`** — Google Drive *Get* with `fields = id,name,size,videoMediaMetadata(width,height,durationMillis),mimeType`.

**`Media facts`** — Code, one item in, one out:
```js
const f = $input.first().json;
const m = f.videoMediaMetadata || {};
const out = {
  width: m.width, height: m.height,
  duration_s: Math.round((m.durationMillis||0)/1000),
  bytes: Number(f.size||0),
  aspect: (m.width && m.height) ? (m.height > m.width ? 'vertical' : 'landscape') : 'unknown',
  over_fb_cap: Number(f.size||0) > $('Config').first().json.facebook_cap_bytes,
  flags: []
};
if (out.aspect === 'unknown') out.flags.push('NO_VIDEO_METADATA');
return [{ json: { ...f, ...out } }];
```

## Routing table (the only routing that exists — no duration gates, ship full length always)
| Fact | Consequence |
|---|---|
| landscape | this file is the **long cut** → YouTube + Facebook POST. Vertical cut needed for TikTok / IG / FB REEL → file 08 |
| vertical | this file is the **short cut**. If no long cut exists, YouTube and FB POST get this file and `notes` gets `VERTICAL_ONLY` |
| `over_fb_cap` | Facebook POST cannot use it → file 08 `NEEDS_COMPRESS`. Compression is not trimming |
| `NO_VIDEO_METADATA` | Drive has not processed it yet → wait 10 min and re-read once, then flag and continue without the FB POST |

Writes `width height duration_s bytes` to the row.
