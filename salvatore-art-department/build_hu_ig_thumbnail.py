"""
HU Instagram Reel Cover — parametric build (rev.4)

Corrections from Bart 2026-07-17:
  - The paper is NOT a fixed 0.415*H band. It sizes to whatever text
    lands inside it, on all four sides.
  - The white-line-above + navy-on-paper split is NOT a rule. Sometimes
    every word sits on the paper. The paper is often just a HIGHLIGHT on
    the punch. It depends on the length of the title.

So: paper geometry is derived from the text block. Pass line1=None to put
everything on the paper.

Tear: fractal value noise (variant B), all four edges, tapered to clean
corners, corners always inside the margin.
"""
import os, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H      = 1080, 1920
PARCHMENT = (245, 245, 220)
HU_NAVY   = (29, 53, 87)
WHITE     = (255, 255, 255)
BLACK     = (0, 0, 0)

MARGIN    = 70          # nothing crosses this
PAD_X     = 46          # base cream around the text, horizontally
PAD_Y     = 40          # base cream around the text, vertically
PAPER_GROW = 1.10       # Bart 2026-07-17: paper +10% so words breathe.
                        # Applied to the PAPER only - the text does not shrink.
AMP_H     = 70          # tear amplitude, top/bottom
AMP_V     = 42          # tear amplitude, sides
TAPER     = 60

FONT_HOOK = "/home/claude/fonts/Gelasio-Bold.ttf"
FONT_TOP  = "/home/claude/fonts/Anton-Regular.ttf"
LOGO_PATH = "/Users/joanharris/Documents/joan foundation documents and SOP/betty/HU logo new 2026 Watermark.png"   # used unaltered
LOGO_W    = 444          # 3x (was 148). PNG used unaltered, so ~2/3 of this is transparent padding.
LOGO_PAD  = (-64, -99)   # Bart: 1/3in left + down as far as the mark fits.
                         # 1in down (300px @300dpi) would clip the mark by 109px.


def value_noise(n, wl, rng):
    nc = max(2, int(n/wl) + 2)
    ctrl = [rng.uniform(-1, 1) for _ in range(nc)]
    out = []
    for i in range(n):
        p = i/wl; i0 = int(p) % nc; i1 = (i0+1) % nc
        t = p - int(p); t = t*t*(3-2*t)
        out.append(ctrl[i0]*(1-t) + ctrl[i1]*t)
    return out


def tear(n, amp, seed, wl):
    rng = random.Random(seed)
    o1 = value_noise(n, wl[0], rng)
    o2 = value_noise(n, wl[1], rng)
    o3 = value_noise(n, wl[2], rng)
    out = []
    for i in range(n):
        d = o1[i]*amp*0.55 + o2[i]*amp*0.38 + o3[i]*amp*0.10
        e = min(i, n-1-i) / TAPER
        d *= (e*e*(3-2*e)) if e < 1 else 1.0
        out.append(d)
    return out


def build(photo, out_path, hook_lines, line1=None, face_cx_src=None, top_air=20,
          manual_scale=None):
    """top_air: px of photo above the paper's tear.

    manual_scale: use when the frame is LANDSCAPE and scale-to-fill would drive
    Bart's head under the paper. The photo is scaled by this factor, cropped on
    the face, BOTTOM-aligned, and the gap above is filled by extending the
    headliner upward. Only works when the top of the frame is quiet, uniform
    dead space - check std before trusting it. See SOP section 2.
    """
    bg = Image.open(photo).convert("RGB")
    bw, bh = bg.size

    if manual_scale is None:
        s = max(W/bw, H/bh)
        bg = bg.resize((int(bw*s)+2, int(bh*s)+2), Image.LANCZOS)
        if face_cx_src is None:
            lf = max(0, (bg.width - W)//2)
        else:
            lf = max(0, min(bg.width - W, int(face_cx_src*s) - W//2))
        canvas = bg.crop((lf, 0, lf+W, H)).copy()   # top-anchored
    else:
        s = manual_scale
        bg = bg.resize((int(bw*s), int(bh*s)), Image.LANCZOS)
        cx = int((face_cx_src or bw/2) * s)
        lf = max(0, min(bg.width - W, cx - W//2))
        crop = bg.crop((lf, 0, lf+W, min(bg.height, H)))
        pad = H - crop.height
        canvas = Image.new("RGB", (W, H))
        if pad > 0:
            band = np.array(crop.crop((0, 0, W, 6))).astype(float).mean(axis=0)
            fill = np.zeros((pad, W, 3), dtype=np.uint8)
            rng = np.random.default_rng(4)
            for r in range(pad):
                k = 0.78 + 0.22 * (r / pad)          # darker further from the glass
                row = band * k + rng.normal(0, 1.6, band.shape)
                fill[r] = np.clip(row, 0, 255).astype(np.uint8)
            canvas.paste(Image.fromarray(fill), (0, 0))
        canvas.paste(crop, (0, max(0, pad)))
    d0 = ImageDraw.Draw(canvas.copy())

    def fit(path, text, max_w, start=250, stop=24):
        sz = start
        while sz > stop:
            f = ImageFont.truetype(path, sz)
            bb = d0.textbbox((0, 0), text, font=f)
            if bb[2]-bb[0] <= max_w:
                return f
            sz -= 2
        return ImageFont.truetype(path, stop)

    # ---- optional white setup line
    y_cursor = top_air
    f_l1 = None
    if line1:
        f_l1 = fit(FONT_TOP, line1, W - 40, start=112, stop=50)
        y_cursor = top_air + d0.textbbox((0, 0), line1, font=f_l1)[3] + 18

    # ---- hook block: the paper is sized around THIS
    # hook_lines entries: "TEXT" or ("TEXT", scale). scale emphasises one
    # line relative to the base size (e.g. a trait word set 3x).
    lines  = [l[0] if isinstance(l, tuple) else l for l in hook_lines]
    scales = [l[1] if isinstance(l, tuple) else 1.0 for l in hook_lines]

    avail_w = W - 2*(MARGIN + AMP_V + PAD_X)
    # base size = largest that fits every UNEMPHASISED line
    base_cands = [fit(FONT_HOOK, ln, avail_w).size
                  for ln, sc in zip(lines, scales) if sc == 1.0] or [78]
    sz = min(base_cands)
    fonts = []
    for ln, sc in zip(lines, scales):
        f = ImageFont.truetype(FONT_HOOK, int(sz*sc))
        while d0.textbbox((0,0), ln, font=f)[2] > avail_w and f.size > 24:
            f = ImageFont.truetype(FONT_HOOK, f.size - 2)   # emphasis never overflows
        fonts.append(f)
    widths  = [d0.textbbox((0, 0), ln, font=f)[2] for ln, f in zip(lines, fonts)]
    heights = [d0.textbbox((0, 0), ln, font=f)[3] for ln, f in zip(lines, fonts)]
    gap = int(sz * 0.10)
    block_w = max(widths)
    block_h = sum(heights) + gap * (len(hook_lines) - 1)

    # ---- paper hugs the block, then grows PAPER_GROW around it
    half_w = (block_w/2 + PAD_X) * PAPER_GROW
    half_h = (block_h/2 + PAD_Y) * PAPER_GROW
    cx = W//2
    X0 = int(max(MARGIN, cx - half_w))
    X1 = int(min(W - MARGIN, cx + half_w))
    Y0 = int(y_cursor + AMP_H)
    Y1 = int(Y0 + 2*half_h)
    text_top = int(Y0 + half_h - block_h/2)        # text re-centred in the bigger paper
    nx, ny = X1-X0, Y1-Y0

    td = tear(nx, AMP_H, 33, (420, 90, 11))
    bd = tear(nx, AMP_H*1.2, 88, (420, 90, 11))
    rd = tear(ny, AMP_V, 51, (240, 64, 9))
    ld = tear(ny, AMP_V, 17, (240, 64, 9))

    poly = ([(X0, Y0)] + [(int(X0+i), int(Y0+td[i])) for i in range(nx)] +
            [(X1, Y0)] + [(int(X1+rd[j]), int(Y0+j)) for j in range(ny)] +
            [(X1, Y1)] + [(int(X0+i), int(Y1+bd[i])) for i in reversed(range(nx))] +
            [(X0, Y1)] + [(int(X0+ld[j]), int(Y0+j)) for j in reversed(range(ny))])

    # ---- shadow + paper
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).polygon([(min(W-1, x+16), min(H-1, y+18)) for x, y in poly],
                               fill=(0, 0, 0, 130))
    sh = sh.filter(ImageFilter.GaussianBlur(26))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), sh).convert("RGB")

    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).polygon(poly, fill=255)
    m = m.filter(ImageFilter.GaussianBlur(0.8))
    canvas.paste(Image.new("RGB", (W, H), PARCHMENT), (0, 0), m)

    dr = ImageDraw.Draw(canvas)

    if line1:
        bb = dr.textbbox((0, 0), line1, font=f_l1)
        x = (W - (bb[2]-bb[0]))//2
        for dx in range(-9, 10, 2):
            for dy in range(-9, 10, 2):
                if dx*dx + dy*dy <= 90:
                    dr.text((x+dx, top_air+dy), line1, font=f_l1, fill=BLACK)
        dr.text((x, top_air), line1, font=f_l1, fill=WHITE)

    y = text_top
    for ln, f, hgt in zip(lines, fonts, heights):
        bb = dr.textbbox((0, 0), ln, font=f)
        x = (W - (bb[2]-bb[0]))//2
        dr.text((x+3, y+4), ln, font=f, fill=(190, 182, 150))
        dr.text((x, y),     ln, font=f, fill=HU_NAVY)
        y += hgt + gap

    # ---- logo, bottom-left
    if LOGO_PATH and os.path.exists(LOGO_PATH):
        lg = Image.open(LOGO_PATH).convert("RGBA")
        lh = int(lg.height * LOGO_W / lg.width)
        lg = lg.resize((LOGO_W, lh), Image.LANCZOS)
        canvas.paste(lg, (LOGO_PAD[0], H - lh - LOGO_PAD[1]), lg)

    xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
    assert min(xs) > 0 and max(xs) < W and min(ys) > 0 and max(ys) < H
    print(f"{os.path.basename(out_path):28s} paper x {X0}-{X1}  y {Y0}-{Y1} "
          f"(h={Y1-Y0})  sizes {[f.size for f in fonts]}pt  bleed L{min(xs)} R{W-max(xs)}")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    canvas.save(out_path, "JPEG", quality=94)
    return {"X0": X0, "X1": X1, "Y0": Y0, "Y1": Y1,
            "lowest_tooth": int(max(ys)), "hook_pt": sz, "sizes": [f.size for f in fonts]}


# ---------------------------------------------------------------------
# Reference build — the settings Bart signed off on (ig_v6).
#   build(photo, out_path, hook_lines, line1=None, top_air=70)
#
#   hook_lines : list of lines to set in navy ON the paper
#   line1      : white Impact setup line ABOVE the paper, or None to put
#                every word on the paper. NOT a rule - judge per title.
#                See SOP_HU_IG_Screenshot_Torn_Paper_Thumbnail.md section 5.
#   top_air    : px of photo above the paper's tear. 70 = approved.
#
# On a Mac, point FONT_HOOK/FONT_TOP at the real fonts:
#   /System/Library/Fonts/Supplemental/Georgia Bold.ttf
#   /System/Library/Fonts/Supplemental/Impact.ttf
# and re-check the fit - the metrics shift slightly off the substitutes.
# ---------------------------------------------------------------------
if False:
    PHOTO = "/mnt/user-data/uploads/IG_bart_leaning_in_to_camera_green_sweater_full.png"
    OUT   = "/mnt/user-data/outputs/true-optimists-write-like-this"
    build(PHOTO, f"{OUT}/ig_v6.jpg", ["TRUE OPTIMISTS", "WRITE LIKE THIS"],
          line1=None, top_air=70)
