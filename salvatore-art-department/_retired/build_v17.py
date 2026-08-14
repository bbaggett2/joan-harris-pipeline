"""
HU Screenshot IG Reel — v17
Back to full-width band — matches approved OPTIMIST IG Reel reference.
Top + bottom torn edges only (straight sides = clean shape, not blob).
Larger tear amplitude. Text fills width to be as big as possible.
"""
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE      = "/Users/joanharris/Documents/joan foundation documents and SOP/Salvadore - art department/thumbnails May 2026/batch/she-hates-all-men"
PHOTO     = f"{BASE}/hurst7-bart-car.png"
LOGO_PATH = "/Users/joanharris/Documents/joan foundation documents and SOP/betty/HU logo new 2026 Watermark.png"
OUTPUT    = f"{BASE}/ig_v17.jpg"
FONT_HOOK = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
FONT_TOP  = "/System/Library/Fonts/Supplemental/Impact.ttf"

W, H      = 1080, 1920
PARCHMENT = (245, 245, 220)
HU_NAVY   = (29, 53, 87)
WHITE     = (255, 255, 255)
BLACK     = (0, 0, 0)

# ── 1. Background photo ─────────────────────────────────────────────
bg = Image.open(PHOTO).convert("RGB")
bw, bh = bg.size
scale = max(W/bw, H/bh)
bg = bg.resize((int(bw*scale)+2, int(bh*scale)+2), Image.LANCZOS)
nw, _ = bg.size
canvas = bg.crop(((nw-W)//2, 0, (nw-W)//2+W, H)).copy()

# ── 2. Tear edge (top/bottom only) ───────────────────────────────────
def tear_edge(y_base, n, amp, flip_dir, seed):
    """
    Returns list from (0,y_base)→ torn teeth → (W,y_base).
    Groups of 2-4 teeth in same direction, occasional deep spike.
    flip_dir=-1 → teeth UP, +1 → teeth DOWN.
    """
    rng = random.Random(seed)
    pts = [(0, y_base)]
    step = W / n
    direction = 1
    group = rng.randint(2, 4); count = 0
    x = 0.0
    while x < W - step * 0.4:
        x = min(x + step, float(W))
        # ~12% chance of a deep spike, otherwise small tooth
        if rng.random() < 0.12:
            mag = rng.randint(int(amp * 0.7), int(amp * 1.4))
        else:
            mag = rng.randint(int(amp * 0.08), int(amp * 0.45))
        pts.append((int(x), int(y_base + flip_dir * direction * mag)))
        count += 1
        if count >= group:
            direction *= -1; group = rng.randint(2, 4); count = 0
    pts.append((W, y_base))
    return pts

# Font helper
_tmp = ImageDraw.Draw(canvas.copy())
def fit_font(path, text, max_w, start=240, stop=20):
    sz = start
    while sz > stop:
        f  = ImageFont.truetype(path, sz)
        bb = _tmp.textbbox((0,0), text, font=f)
        if bb[2]-bb[0] <= max_w: return f, sz
        sz -= 4
    return ImageFont.truetype(path, stop), stop

LINE1 = "IF SHE HATES ALL MEN,"
f_l1, _ = fit_font(FONT_TOP, LINE1, W-20, start=110, stop=50)
h_l1 = _tmp.textbbox((0,0), LINE1, font=f_l1)[3]

Y_LINE1   = 20
PARCH_TOP = Y_LINE1 + h_l1 + 18
PARCH_BOT = int(H * 0.415)

top_pts = tear_edge(PARCH_TOP, n=45, amp=75, flip_dir=-1, seed=33)
bot_pts = tear_edge(PARCH_BOT, n=52, amp=90, flip_dir=+1, seed=88)

# Full-width band polygon
poly = top_pts + [(W, PARCH_BOT)] + list(reversed(bot_pts))

# ── 3. Shadow + parchment ────────────────────────────────────────────
shad = Image.new("RGBA", (W, H), (0,0,0,0))
spoly = [(min(W-1,x+16), min(H-1,y+18)) for x,y in poly]
ImageDraw.Draw(shad).polygon(spoly, fill=(0,0,0,130))
shad = shad.filter(ImageFilter.GaussianBlur(26))
canvas = Image.alpha_composite(canvas.convert("RGBA"), shad).convert("RGB")

mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask).polygon(poly, fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(0.8))
canvas.paste(Image.new("RGB", (W, H), PARCHMENT), (0,0), mask)

draw = ImageDraw.Draw(canvas)

# ── 4. White setup line ─────────────────────────────────────────────
def ctr(text, font):
    bb = draw.textbbox((0,0), text, font=font)
    return (W-(bb[2]-bb[0]))//2

def outlined(pos, text, font, fill=WHITE, ow=9):
    x,y = pos
    for dx in range(-ow, ow+1, 2):
        for dy in range(-ow, ow+1, 2):
            if dx*dx+dy*dy <= ow*ow+ow:
                draw.text((x+dx,y+dy), text, font=font, fill=BLACK)
    draw.text(pos, text, font=font, fill=fill)

outlined((ctr(LINE1, f_l1), Y_LINE1), LINE1, f_l1)

# ── 5. Hook text — as large as possible, fills parchment width ───────
HOOK_A = "SHE'LL HAVE THIS"
HOOK_B = "IN HER HANDWRITING"
# Leave 30px margin each side inside parchment
f_a, _ = fit_font(FONT_HOOK, HOOK_A, W - 60, start=240, stop=30)
f_b, _ = fit_font(FONT_HOOK, HOOK_B, W - 60, start=240, stop=30)
ha = draw.textbbox((0,0), HOOK_A, font=f_a)[3]
hb = draw.textbbox((0,0), HOOK_B, font=f_b)[3]
total = ha + 10 + hb
mid   = (PARCH_TOP + PARCH_BOT)//2 + 12
ya    = mid - total//2
yb    = ya + ha + 10

def navy_block(pos, text, font):
    x,y = pos
    draw.text((x+3, y+4), text, font=font, fill=(190,182,150))
    draw.text(pos, text, font=font, fill=HU_NAVY)

navy_block((ctr(HOOK_A, f_a), ya), HOOK_A, f_a)
navy_block((ctr(HOOK_B, f_b), yb), HOOK_B, f_b)

# ── 6. Logo ─────────────────────────────────────────────────────────
logo = Image.open(LOGO_PATH).convert("RGBA")
lw = 148; lh = int(logo.height*lw/logo.width)
logo = logo.resize((lw, lh), Image.LANCZOS)
canvas.paste(logo, (36, H-lh-46), logo)

canvas.save(OUTPUT, "JPEG", quality=94)
print(f"Done → {OUTPUT}")
