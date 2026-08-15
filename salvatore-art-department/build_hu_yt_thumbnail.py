#!/usr/bin/env python3
"""
build_hu_yt_thumbnail.py — HU YouTube thumbnail (16:9), Pass 2.

Composites the brand layer onto a Gemini host plate:
  trait graphic + red circle -> headline -> key word on tilted parchment -> logo

Canvas 1280x720. Constants in HU_Thumbnail_16x9_Constants_v1.md.
The 9:16 build is a different script (build_hu_ig_thumbnail.py) with different numbers.

Usage:
  python3 build_hu_yt_thumbnail.py \
      --plate  outputs/0814-raw-16x9.png \
      --trait  assets/no-trust-paper.png \
      --logo   HU_logo_new_2026_Watermark.png \
      --font   Gelasio-Bold.ttf \
      --headline "DOESN'T TRUST" \
      --keyword  "ANYONE" \
      --out    outputs/0814-yt_v1.jpg

Every geometry value is a named constant below. Nothing is eyeballed.
"""

import argparse
import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ---------------------------------------------------------------- constants
# 16:9 set. Measured 2026-08-14. See HU_Thumbnail_16x9_Constants_v1.md.

W, H = 1280, 720
MARGIN = 44                    # nothing crosses this
LEFT_COL_W = 540               # left ~42% carries headline + trait
RIGHT_KEEPOUT_X = 760          # host lives right of this; never composite over it

# Bottom-right must stay clear for the YouTube duration stamp.
TIMESTAMP_KEEPOUT = (1080, 630, 1280, 720)   # x0,y0,x1,y1

# Palette
HU_NAVY = (29, 53, 87)         # #1D3557
PARCHMENT = (245, 245, 220)    # #F5F5DC
WHITE = (255, 255, 255)
SILVER = (192, 192, 192)       # #C0C0C0 metallic edge
TEACHER_RED = (214, 40, 40)    # #D62828  -- 16:9 only
EMBOSS_TAN = (190, 182, 150)   # #BEB696

# Headline
HEAD_MAX_PT = 82
HEAD_MIN_PT = 44
HEAD_LINE_GAP = 8
HEAD_TOP = 40
HEAD_STROKE = 3                # silver edge width
HEAD_SHADOW = (4, 5)           # offset for legibility on busy plates

# Parchment key-word block
PARCH_TILT = -3.0              # degrees; slight, per brand kit
PARCH_PAD_X = 34
PARCH_PAD_Y = 20
PARCH_GROW = 1.10              # same 10% breathing room as the 9:16 build
PARCH_SHADOW_OFF = (10, 12)
PARCH_SHADOW_BLUR = 16
PARCH_SHADOW_ALPHA = 130
KEY_MAX_PT = 92
KEY_MIN_PT = 40
EMBOSS_OFF = (3, 4)

# Trait graphic
TRAIT_MAX_W = 430
TRAIT_MAX_H = 300
CIRCLE_MIN_RATIO = 0.62        # keep the pen circle from becoming a thin oval
TRAIT_GAP = 22                 # below the parchment block
TRAIT_LOGO_CLEAR = 104         # vertical room reserved for the logo below the trait
CIRCLE_W = 7                   # red pen stroke
CIRCLE_PAD = 22

# Logo — bottom-left. Scaled from the visible mark, never the padded box.
LOGO_MARK_W = 132              # visible mark width on a 1280x720 canvas
LOGO_LEFT = 44
LOGO_BOTTOM = 30

MAX_BYTES = 2 * 1024 * 1024


# ---------------------------------------------------------------- helpers
def fit_font(path, text, max_w, hi, lo):
    """Largest point size at or below `hi` whose rendered width fits max_w."""
    best = lo
    while lo <= hi:
        mid = (lo + hi) // 2
        f = ImageFont.truetype(path, mid)
        w = f.getbbox(text)[2] - f.getbbox(text)[0]
        if w <= max_w:
            best, lo = mid, mid + 1
        else:
            hi = mid - 1
    return best


def wrap(text, font_path, pt, max_w):
    f = ImageFont.truetype(font_path, pt)
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if f.getbbox(trial)[2] - f.getbbox(trial)[0] <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def visible_bbox(img):
    """Bounding box of non-transparent pixels. Logo placement uses this."""
    a = img.convert("RGBA").split()[-1]
    bb = a.getbbox()
    return bb if bb else (0, 0, img.width, img.height)


def trim_to_ink(img, pad=16):
    """Crop a trait graphic to the dense cluster of strokes. OPT-IN, not default.

    Reliable on clean-background art such as the GraphoDeck individual cards.
    NOT reliable on samples photographed on real paper: a fold crease runs the
    full height of the image and out-densities the letterform, so the crop lands
    on the crease. Verified failure on no-trust-paper.png, 2026-08-14. Crop those
    by hand and pass the result without --trim.

    A plain threshold does not work: library samples are photographed on real
    paper, and fold creases, edge shadows, and grain all read as "dark". Those
    are sparse and spread out; the letterform is a dense localised cluster. So
    profile ink-per-column and ink-per-row, then keep the span above a fraction
    of the peak. Falls back to the original image if nothing dominant is found.
    """
    import numpy as np
    g = np.array(img.convert("L")).astype(float)
    ink = (g < 110).astype(float)
    if ink.sum() < 50:
        return img

    def span(profile, frac=0.14):
        pk = profile.max()
        if pk <= 0:
            return None
        hits = np.where(profile >= pk * frac)[0]
        if hits.size == 0:
            return None
        # keep the contiguous run containing the peak
        peak = int(profile.argmax())
        lo = hi = peak
        hitset = set(hits.tolist())
        while lo - 1 in hitset:
            lo -= 1
        while hi + 1 in hitset:
            hi += 1
        return lo, hi

    cs = span(ink.sum(axis=0))
    rs = span(ink.sum(axis=1))
    if not cs or not rs:
        return img
    x0 = max(0, cs[0] - pad)
    x1 = min(img.width, cs[1] + pad)
    y0 = max(0, rs[0] - pad)
    y1 = min(img.height, rs[1] + pad)
    if (x1 - x0) < 24 or (y1 - y0) < 24:
        return img
    return img.crop((x0, y0, x1, y1))


def cover(img, w, h):
    """Scale-to-fill and centre-crop, preserving aspect."""
    s = max(w / img.width, h / img.height)
    r = img.resize((max(1, int(img.width * s)), max(1, int(img.height * s))),
                   Image.LANCZOS)
    x = (r.width - w) // 2
    y = (r.height - h) // 2
    return r.crop((x, y, x + w, y + h))


# ---------------------------------------------------------------- build
def build(plate_path, trait_path, logo_path, font_path,
          headline, keyword, out_path, edge="cut", trim=False, quiet=False):

    def log(m):
        if not quiet:
            print(m)

    canvas = cover(Image.open(plate_path).convert("RGB"), W, H)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    text_w = LEFT_COL_W - MARGIN

    # ---- headline: white, silver edge, drop shadow -----------------------
    pt = fit_font(font_path, max(headline.split(), key=len),
                  text_w, HEAD_MAX_PT, HEAD_MIN_PT)
    lines = wrap(headline, font_path, pt, text_w)
    while len(lines) > 3 and pt > HEAD_MIN_PT:
        pt -= 4
        lines = wrap(headline, font_path, pt, text_w)
    hf = ImageFont.truetype(font_path, pt)

    y = HEAD_TOP
    for ln in lines:
        draw.text((MARGIN + HEAD_SHADOW[0], y + HEAD_SHADOW[1]), ln,
                  font=hf, fill=(0, 0, 0, 150))
        draw.text((MARGIN, y), ln, font=hf, fill=WHITE + (255,),
                  stroke_width=HEAD_STROKE, stroke_fill=SILVER + (255,))
        y += (hf.getbbox(ln)[3] - hf.getbbox(ln)[1]) + HEAD_LINE_GAP
    head_bottom = y
    log(f"headline  {pt}pt  {len(lines)} line(s)  bottom y={head_bottom}")

    # ---- key word on tilted parchment ------------------------------------
    parch_bottom = head_bottom
    if keyword:
        kpt = fit_font(font_path, keyword, text_w - 2 * PARCH_PAD_X,
                       KEY_MAX_PT, KEY_MIN_PT)
        kf = ImageFont.truetype(font_path, kpt)
        bb = kf.getbbox(keyword)
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        pw = int((tw / 2 + PARCH_PAD_X) * PARCH_GROW * 2)
        ph = int((th / 2 + PARCH_PAD_Y) * PARCH_GROW * 2)

        pad = 60
        block = Image.new("RGBA", (pw + pad * 2, ph + pad * 2), (0, 0, 0, 0))
        bd = ImageDraw.Draw(block)
        rect = [pad, pad, pad + pw, pad + ph]

        if edge == "torn":
            import random
            rnd = random.Random(7)
            pts, amp, step = [], 6, 14
            for x in range(rect[0], rect[2], step):
                pts.append((x, rect[1] + rnd.randint(-amp, amp)))
            for yy in range(rect[1], rect[3], step):
                pts.append((rect[2] + rnd.randint(-amp, amp), yy))
            for x in range(rect[2], rect[0], -step):
                pts.append((x, rect[3] + rnd.randint(-amp, amp)))
            for yy in range(rect[3], rect[1], -step):
                pts.append((rect[0] + rnd.randint(-amp, amp), yy))
            bd.polygon(pts, fill=PARCHMENT + (255,))
        else:
            bd.rectangle(rect, fill=PARCHMENT + (255,))

        bd.text((pad + PARCH_PAD_X + EMBOSS_OFF[0] - bb[0],
                 pad + PARCH_PAD_Y + EMBOSS_OFF[1] - bb[1]),
                keyword, font=kf, fill=EMBOSS_TAN + (255,))
        bd.text((pad + PARCH_PAD_X - bb[0], pad + PARCH_PAD_Y - bb[1]),
                keyword, font=kf, fill=HU_NAVY + (255,))

        block = block.rotate(PARCH_TILT, resample=Image.BICUBIC, expand=True)

        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sm = Image.new("L", block.size, 0)
        ImageDraw.Draw(sm).bitmap((0, 0), block.split()[-1], fill=PARCH_SHADOW_ALPHA)
        px, py = MARGIN - pad, head_bottom + 14 - pad
        sh.paste(Image.new("RGBA", block.size, (0, 0, 0, PARCH_SHADOW_ALPHA)),
                 (px + PARCH_SHADOW_OFF[0], py + PARCH_SHADOW_OFF[1]),
                 block.split()[-1])
        layer = Image.alpha_composite(layer, sh.filter(
            ImageFilter.GaussianBlur(PARCH_SHADOW_BLUR)))

        layer.paste(block, (px, py), block)
        draw = ImageDraw.Draw(layer)
        # The block carries 60px of transparent padding plus rotation expansion.
        # Measure the visible parchment, or the trait below it starts too high
        # and overlaps the key word.
        vb = visible_bbox(block)
        parch_bottom = py + vb[3]
        log(f"parchment {kpt}pt  {pw}x{ph}  tilt {PARCH_TILT}  edge={edge}")

    # ---- trait graphic + red circle --------------------------------------
    avail_top = parch_bottom + TRAIT_GAP
    avail_h = (H - MARGIN - TRAIT_LOGO_CLEAR) - avail_top
    if avail_h < 90:
        sys.exit(f"ASSERT FAILED: only {avail_h}px left for the trait graphic. "
                 f"Shorten the headline or the key word.")

    trait = Image.open(trait_path).convert("RGBA")
    if trim:
        before = trait.size
        trait = trim_to_ink(trait)
        log(f"trait     trimmed {before[0]}x{before[1]} -> {trait.width}x{trait.height}")
    s = min(TRAIT_MAX_W / trait.width, min(TRAIT_MAX_H, avail_h) / trait.height)
    trait = trait.resize((max(1, int(trait.width * s)), max(1, int(trait.height * s))),
                         Image.LANCZOS)
    tx = MARGIN
    ty = avail_top
    layer.paste(trait, (tx, ty), trait)

    # A single narrow letterform would otherwise get a thin vertical oval. Widen
    # the circle until it reads as a hand-drawn pen ring.
    cw = trait.width + CIRCLE_PAD * 2
    ch = trait.height + CIRCLE_PAD
    if cw / ch < CIRCLE_MIN_RATIO:
        cw = int(ch * CIRCLE_MIN_RATIO)
    cx = tx + trait.width / 2
    cb = [int(cx - cw / 2), ty - CIRCLE_PAD // 2,
          int(cx + cw / 2), ty + trait.height + CIRCLE_PAD // 2]
    if cb[0] < MARGIN - 10:
        shift = (MARGIN - 10) - cb[0]
        cb[0] += shift; cb[2] += shift
        layer.paste(Image.new("RGBA", (0, 0)), (0, 0)) if False else None
    ImageDraw.Draw(layer).ellipse(cb, outline=TEACHER_RED + (255,), width=CIRCLE_W)
    log(f"trait     {trait.width}x{trait.height} at ({tx},{ty})  circle {cb}")

    # ---- logo, bottom-left, measured on the visible mark -----------------
    logo = Image.open(logo_path).convert("RGBA")
    bb = visible_bbox(logo)
    scale = LOGO_MARK_W / (bb[2] - bb[0])
    logo = logo.resize((int(logo.width * scale), int(logo.height * scale)), Image.LANCZOS)
    nb = visible_bbox(logo)
    lx = LOGO_LEFT - nb[0]
    ly = H - LOGO_BOTTOM - nb[3]
    layer.paste(logo, (lx, ly), logo)
    mark = (LOGO_LEFT, ly + nb[1], LOGO_LEFT + (nb[2] - nb[0]), ly + nb[3])
    log(f"logo      mark {mark}")

    out = Image.alpha_composite(canvas.convert("RGBA"), layer).convert("RGB")

    # ---- asserts: fail loudly, never silently ship -----------------------
    assert mark[0] >= MARGIN - 4, "logo mark crosses the left margin"
    assert mark[3] <= H - 4, "logo mark falls off the canvas"
    assert cb[2] < RIGHT_KEEPOUT_X, \
        f"trait circle reaches x={cb[2]}, into the host zone at {RIGHT_KEEPOUT_X}"
    assert cb[3] < H - MARGIN + CIRCLE_PAD, "trait circle crosses the bottom margin"
    assert cb[1] >= parch_bottom, \
        f"trait circle (top {cb[1]}) overlaps the parchment block (bottom {parch_bottom})"
    assert cb[3] < mark[1] - 6, \
        f"trait circle (bottom {cb[3]}) collides with the logo mark (top {mark[1]})"
    tsx0, tsy0, _, _ = TIMESTAMP_KEEPOUT
    assert mark[2] < tsx0 or mark[1] > H, "logo intrudes on the timestamp keepout"
    assert len(lines) <= 3, f"headline wrapped to {len(lines)} lines; shorten it"
    assert len(headline.split()) + len(keyword.split()) <= 5, \
        "more than 5 words total; the 168x94 legibility floor will fail"

    # ---- write under the 2 MB ceiling ------------------------------------
    q = 92
    while q >= 70:
        out.save(out_path, "JPEG", quality=q, optimize=True)
        if os.path.getsize(out_path) <= MAX_BYTES:
            break
        q -= 4
    size = os.path.getsize(out_path)
    assert size <= MAX_BYTES, f"{size} bytes exceeds the 2 MB YouTube ceiling"
    log(f"wrote     {out_path}  {W}x{H}  q{q}  {size/1024:.0f} KB")

    # ---- legibility proof ------------------------------------------------
    prev = out_path.rsplit(".", 1)[0] + "_168x94.png"
    out.resize((168, 94), Image.LANCZOS).save(prev)
    log(f"proof     {prev}  <- read this before approving")
    return out_path


def main():
    p = argparse.ArgumentParser(description="HU YouTube thumbnail (16:9) Pass 2")
    p.add_argument("--plate", required=True, help="Gemini host plate, Pass 1 output")
    p.add_argument("--trait", required=True, help="trait graphic from the approved library")
    p.add_argument("--logo", required=True)
    p.add_argument("--font", required=True, help="Georgia Bold, or Gelasio Bold off-Mac")
    p.add_argument("--headline", required=True)
    p.add_argument("--keyword", default="", help="word that lands on the parchment")
    p.add_argument("--out", required=True)
    p.add_argument("--edge", choices=["cut", "torn"], default="cut",
                   help="parchment edge; 16:9 allows either, per brand kit 6")
    p.add_argument("--trim", action="store_true",
                   help="auto-crop to ink. Works on clean-background deck cards. "
                        "Do NOT use on photographed paper with fold creases or "
                        "heavy edge shadow -- it will crop the crease, not the "
                        "letter. Crop those by hand first.")
    p.add_argument("--quiet", action="store_true")
    a = p.parse_args()

    for f in (a.plate, a.trait, a.logo, a.font):
        if not os.path.exists(f):
            sys.exit(f"missing input: {f}")

    try:
        build(a.plate, a.trait, a.logo, a.font, a.headline, a.keyword,
              a.out, a.edge, a.trim, a.quiet)
    except AssertionError as e:
        sys.exit(f"ASSERT FAILED: {e}")


if __name__ == "__main__":
    main()
