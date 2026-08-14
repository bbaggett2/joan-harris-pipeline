# HU AI-Generated Host Thumbnail — Instructions & Reusable Shell Template

**Brand:** Handwriting University (HU)
**Format:** YouTube thumbnail, 1280×720 (16:9)
**Method:** Gemini AI generates Bart's likeness from 5 approved reference photos — NO video screenshot required
**Style:** Torn cream parchment + HU Navy collegiate type (same palette as the Liar Liar approved build)
**Status:** Active — Joan dispatches, Salvadore/Betty executes, Bart approves
**Lives at:** `Salvadore - art department/HU_AI_GE_Thumbnail_instructions.MD`

---

## ⛔ MANDATORY — READ BEFORE STARTING EVERY THUMBNAIL

These two rules have caused failed builds. Both are non-negotiable and apply to every HU AI-GE thumbnail, every time.

### RULE 1 — HEADLINE: NEVER INVENT COPY

**Salvadore does NOT write thumbnail headlines. Ever.**

The thumbnail headline must come from one of these two sources only:
1. The video title provided by Joan or Bart, OR
2. A headline explicitly written and given to Salvadore in the task brief

If neither exists, **STOP. Ask Joan before proceeding.** Do not use the VTT transcript to guess a headline. Do not brainstorm options. Do not use the trait name as a headline. The copy is not Salvadore's job — it is Joan's and Bart's.

**The headline goes on the parchment exactly as written. No paraphrasing. No "improvements."**

### RULE 2 — LIKENESS: THE HOST MUST LOOK LIKE BART BAGGETT

Gemini sometimes generates a generic AI-looking man when likeness prompts are vague. If the output person does not closely match the reference photos, **regenerate before sending to Joan.**

Physical anchors to verify against the reference photos:
- **Hair:** Dark blonde going grey at the temples. Not fully grey. Not brown. Not bald.
- **Eyes:** Blue, direct, slightly deep-set
- **Face shape:** Defined jaw, prominent brow, strong cheekbones. Late 50s–early 60s appearance.
- **Build:** Solid, upright, broad-shouldered. Not slight or wiry.
- **Energy:** Confident, composed, authoritative — not generic "stock photo businessman"

**Auto-reject if the output shows:** a younger man (under 45-looking), a generic middle-aged white man with no distinguishing features, a man with dark eyes or dark/black hair, a man who looks like he was pulled from a corporate stock photo. Regenerate immediately.

---

## Why this file exists — and how it differs from the Screenshot Method

There are **two distinct HU thumbnail build paths:**

| | Screenshot Method | AI-GE Method (this file) |
|---|---|---|
| **Host image source** | Real frame grab from the actual video | Gemini synthesizes Bart's likeness from 5 reference photos |
| **When to use** | When a clean video frame exists with proper headroom | When no usable frame exists, or video isn't shot yet |
| **Governing SOP** | `SOP_HU_IG_Screenshot_Torn_Paper_v2.md` | This file |
| **Script flag** | `--headshot <frame>` (single primary image) | `--headshot <primary>` + `--reference` × 4 additional |
| **Background** | Extracted/padded from actual video footage | Gemini generates cinematic dark environment |
| **Person authenticity** | Real Bart from that video | AI-synthesized from approved reference pool |
| **Format scope** | 9:16 IG Reels / TikTok covers | 16:9 YouTube thumbnails |

**The parchment, colors, type rules, and composition structure are identical between the two methods.**
Everything in §2–§5 below matches the locked Liar Liar / vanity build standard exactly.

---

## 1. The Five Approved Reference Photos

These are the only photos Gemini is permitted to draw Bart's likeness from for this method.
They live in `skills_to_install/youtube-thumbnail/headshots/`.

| # | Filename | Character / Expression | Best used for |
|---|---|---|---|
| 1 | `Bart-serious-clear-bluesuit.png` | Authoritative, direct gaze, blue suit | Knowledge/credibility topics |
| 2 | `BartBaggett72whitebackgroundB16A5244blue_B.jpg` | Clean professional, neutral expression | General / flexible |
| 3 | `B16A5236_revised_bart_red_smile.jpg` | Warm confident smile | Positive/aspirational topics |
| 4 | `Bart_MG_1770_attorney_shot.png` | Attorney gravitas, composed | Legal / analysis topics |
| 5 | `bartbaggett_MG_1827-labcoat.jpg` | Expert / researcher, lab coat | Science / psychology topics |

**Rule:** Always pass ALL FIVE as references so Gemini has full likeness coverage.
Photo #1 (`Bart-serious-clear-bluesuit.png`) is always the `--headshot` (primary).
Photos #2–#5 go as `--reference` inputs alongside the HU logo.

Do NOT use `bartbaggettB16A5236_red_background_smile2.png` as a reference — it is a raw
unretouched file (33 MB) that causes inconsistent color contamination in Gemini outputs.
`B16A5236_revised_bart_red_smile.jpg` is the corrected version and should be used instead.

**Mandatory likeness language in every prompt (copy verbatim):**
> "You are given 5 reference photos of the male host — study ALL FIVE carefully and synthesize a photorealistic version of THIS SPECIFIC MAN. Do not invent a generic person. Use his exact facial features: dark-blonde hair going grey at the temples, blue eyes, defined jaw, prominent brow, broad-shouldered, late 50s–early 60s in appearance, confident and composed bearing. If you cannot match this likeness from the references, do not generate a substitute — fail gracefully."

---

## 2. Color Palette (locked — matches Liar Liar build)

| Role | Color | Hex | Notes |
|---|---|---|---|
| Parchment fill | Cream | `#F5F5DC` | **Flat. No grain, no texture, no gradient.** The torn shape sells it. |
| Headline type | HU Navy | `#1D3557` | Exact. Non-negotiable. |
| Type emboss shadow | Warm tan | `#BEB696` | 3–4 px offset behind the navy — lifts letters off the cream. |
| Setup line (optional) | White | `#FFFFFF` | Above the parchment when used. Heavy black outline. |
| Paper drop shadow | Black @ 51% | — | Offset +16/+18, blur 26, beneath parchment. This sells the paper as physical. |
| Background | Dark cinematic | — | Gemini generates: darkened study/library, soft window or candle light, depth. Never flat color. |

---

## 3. Composition Rules (locked)

- **Bart on the RIGHT, ~40% of frame width.** Shoulders-up. His ENTIRE head visible — forehead, both ears, chin all in frame. Never cropped.
- **Torn parchment in the UPPER-LEFT**, carrying the headline. Sized to the text, then grown 10% outward.
- **Supporting visual (optional) on the LEFT** — a trait-letter card, a handwriting sample, a symbolic graphic. Max one element.
- **HU logo small**, bottom-left (or bottom-right), never dominant. Always the real PNG unaltered.
- **Maximum 3 distinct elements** (person + text/paper + one graphic). Bottom-right corner clear (YouTube timestamp zone).
- Text never overlaps the face.

### Three approved text layouts — choose by title length

| Layout | When to use | Reference |
|---|---|---|
| **A — all text on parchment, equal size** | Mid-length titles (3–5 words) | `ig_v6.jpg` "very very good" |
| **B — trait word LARGE, payoff below** | Trait + reaction titles | `ig_v7.jpg` "pretty darn good" |
| **C — stacked hero type, tall parchment** | Short punchy titles (1–2 words) | `liar-liar/ig_v2.jpg` "This is excellent" |

---

## 4. Typography

- **Parchment headline:** Georgia Bold (Mac) / Gelasio Bold (Linux substitute). Embossed: warm-tan offset shadow behind the navy.
- **Setup line above parchment (when used):** Impact (Mac) / Anton (Linux substitute). White with heavy black outline.
- Type is rendered by Gemini — do NOT hand-composite with Pillow/PIL. The style prompt drives the font rendering.
- Bart's explicit rule: **bold heavy white sans-serif for any text outside the parchment; navy collegiate serif ON the parchment.**

⛔ **HEADLINE SOURCE REMINDER (repeated here by design):** The words that go on the parchment come from Joan or Bart. Not from the VTT. Not from Salvadore's judgment. If you do not have the headline in writing, stop and ask.

---

## 5. The Torn Parchment — key rules for the Gemini prompt

The parchment appearance is specified in the prompt text. Gemini must understand:
- Shape is a **freeform torn rectangle**, not a straight-edged band and not a full-bleed strip.
- All four edges have organic tears — not a sawtooth, not a cut card.
- Fill is **flat cream `#F5F5DC`** — no grain, no parchment-texture aging effect.

---

## 6. Build Order Checklist

1. **Confirm headline is provided in writing by Joan or Bart.** If not — STOP. Ask.
2. Fill in the six `## CONFIGURE` variables in the shell script.
3. Confirm all five reference headshots are present in `headshots/` — run `ls` if unsure.
4. Confirm `GEMINI_API_KEY` is in `$ROOT/.env`.
5. Run the script. It generates Variant A then Variant B (minimum 2; up to 4 per Phase 4 brief).
6. Open all output PNGs. Run the QA gate (§9) before sending to Joan.
7. Send all variants to Joan. Joan sends to Bart. **Only Bart approves.**
8. Once Bart names a winner, Betty uploads via yutu CLI.
9. Log the result in `Salvadore - art department/youtube-thumbnail-log.md`.

---

## 7. Shell Script Template

```zsh
#!/bin/zsh
ROOT="/Users/joanharris/Documents/joan foundation documents and SOP"
SKILL="$ROOT/skills_to_install/youtube-thumbnail"
GEN="$SKILL/scripts/generate_thumbnail.py"
LOGO="$ROOT/betty/HU logo new 2026 Watermark.png"
HS_PRIMARY="$SKILL/headshots/Bart-serious-clear-bluesuit.png"
HS_REF2="$SKILL/headshots/BartBaggett72whitebackgroundB16A5244blue_B.jpg"
HS_REF3="$SKILL/headshots/B16A5236_revised_bart_red_smile.jpg"
HS_REF4="$SKILL/headshots/Bart_MG_1770_attorney_shot.png"
HS_REF5="$SKILL/headshots/bartbaggett_MG_1827-labcoat.jpg"

## CONFIGURE (fill these in per video — get headline from Joan/Bart, never invent)
VID_ID="VID-XXXX"
SLUG="short-slug"
HEADLINE_A="HEADLINE FROM JOAN OR BART — VERBATIM"
HEADLINE_B="ALTERNATE HEADLINE FROM JOAN OR BART — VERBATIM"
TRAIT="path/to/trait/card.png"
EXPRESSION_A="walled off and wary — eyes direct, slightly narrowed, flat closed lips"
EXPRESSION_B="quietly wounded — tightness around eyes, knowing look"
BACKGROUND_A="dark moody private library, warm amber candlelight"
BACKGROUND_B="dark psychology office, cool blue-grey window light"
VISUAL_LEFT_A="narrow lower-loop Y and G strokes as clinical specimen on cream paper"
VISUAL_LEFT_B="prominent narrow lower-loop stroke, large, left 50% of frame"
OUT="$ROOT/Salvadore - art department/thumbnails work folder from recent sessions/${VID_ID}-${SLUG}"

export GEMINI_API_KEY="$(grep -E '^GEMINI_API_KEY=' "$ROOT/.env" | head -1 | cut -d= -f2- | tr -d '\r\n "')"
mkdir -p "$OUT"

python3 "$GEN" \
  --headshot "$HS_PRIMARY" \
  --reference "$HS_REF2" "$HS_REF3" "$HS_REF4" "$HS_REF5" "$LOGO" "$TRAIT" \
  --output "$OUT/${VID_ID}-A-$(echo "$SLUG" | cut -c1-12).png" \
  --prompt "$(cat <<PROMPT_A
A professional 16:9 YouTube thumbnail for a psychology and handwriting channel.
You are given 5 reference photos of the male host — study ALL FIVE carefully and synthesize
a photorealistic version of THIS SPECIFIC MAN. Do not invent a generic person. Use his exact
facial features: dark-blonde hair going grey at the temples, blue eyes, defined jaw, prominent
brow, broad-shouldered, late 50s–early 60s in appearance, confident and composed bearing.
The 6th image is the HU logo — place it SMALL in the bottom-left corner, never dominant.
The 7th image is the handwriting trait card — extract ONLY the ink strokes (see §13 rule).

PERSON: Place the synthesized host on the RIGHT, ~40% of the frame width. Shoulders-up.
His ENTIRE head must be fully visible — forehead, both ears, chin all in frame. Never cropped.
Expression: ${EXPRESSION_A}. Dramatic cinematic side lighting from the left.

BACKGROUND: ${BACKGROUND_A}. Photographic depth of field, never a flat color.

VISUAL (left side): ${VISUAL_LEFT_A}. Occupies the left ~45% of the frame.

TEXT: "${HEADLINE_A}" rendered in a heavy collegiate block-serif font, ALL CAPS, in HU Navy
(#1D3557), on a piece of torn cream parchment (#F5F5DC flat fill — no grain, no texture,
no aging effect). Freeform torn shape — all four edges have organic irregular tears. Sized to
the words, with a slight drop shadow underneath. A warm tan emboss shadow 3-4px behind the
navy letters. Parchment in the upper-left area, clear of the host's face.

STYLE: High-contrast, clean, cinematic. Maximum 3 elements total. Bottom-right corner clear.
No text overlaps the face.
PROMPT_A
)"
```

---

## 8. Prompt Formula — the anatomy of every AI-GE prompt

Every prompt in this method must contain these six sections, in this order:

1. **Likeness instruction** — Explicitly tells Gemini to synthesize the host from the provided references. Include the physical description anchor verbatim from §1.
2. **Logo instruction** — One sentence: place it small in a specific corner, never dominant.
3. **Person block** — Position (right ~40%), crop rule (entire head visible), expression, lighting direction.
4. **Background block** — Describe a real cinematic environment. Never flat color. Dark and moody.
5. **Visual block** — The left-side graphic element. Specific. Single element.
6. **Text + parchment block** — The headline text verbatim in quotes (from Joan/Bart), the font spec, the parchment spec, and its position.

Closing every prompt with: `STYLE: High-contrast, clean, cinematic. Maximum 3 elements total. Bottom-right corner clear (YouTube timestamp zone). No text overlaps the face.`

---

## 9. QA Gate — check before sending to Joan

All items must pass or the thumbnail is regenerated, not sent.

| Check | Pass condition |
|---|---|
| ⛔ **Headline came from Joan or Bart** | Written in the task brief — not invented by Salvadore |
| ⛔ **Host likeness matches reference photos** | Dark-blonde greying hair, blue eyes, defined jaw, late 50s–early 60s. Reject generic AI-man. |
| Bart's full head visible | Forehead, both ears, chin — nothing cropped |
| Face not covered by parchment | Parchment is in upper-left, above or beside the face |
| Parchment reads as torn paper | Irregular edges on all four sides; not a cut card or rectangle |
| Parchment is flat cream | No grain, no texture, no aged-paper look |
| Navy type on parchment | Exactly `#1D3557` — not gold, not white, not any other color |
| Logo is present and small | Visible in corner but never a dominant element |
| Background is cinematic/dark | Actual environment with depth — not a solid void or flat color |
| Maximum 3 elements | Person + parchment/text + one left-side visual; nothing more |
| Bottom-right clear | No text or graphic in the YouTube timestamp zone |
| Not 100% AI-looking | Image should feel editorial-quality, not stock AI illustration |
| Looks expensive | Brand feel: premium psychology channel, not hobbyist content |

---

## 10. Variant Naming Convention

```
{VID_ID}-A-{slug-12chars}.png    ← Variant A
{VID_ID}-B-{slug-12chars}.png    ← Variant B
{VID_ID}-C-{slug-12chars}.png    ← Variant C (if 4-concept run)
{VID_ID}-D-{slug-12chars}.png    ← Variant D (if 4-concept run)
{VID_ID}-GRID-2x2.jpg            ← Comparison grid
```

**Never use status words in filenames** (`final`, `approved`, `winner`, `done`).
Only Bart approves. File names increment: v1, v2, v3 if regenerated.

---

## 11. When to Use This Method vs. the Screenshot Method

Use **AI-GE (this file)** when:
- No video has been shot yet but a thumbnail is needed for pre-scheduling
- The video exists but no frame has good headroom
- Bart requests a "concept thumbnail" for a pitch or planning deck

Use **Screenshot Method** (`SOP_HU_IG_Screenshot_Torn_Paper_v2.md`) when:
- A real video frame with proper headroom is available
- The video has already been reviewed and a specific emotional beat should be captured

When in doubt: **Screenshot Method is preferred** because Bart is a real person and real footage is always more authentic.

---

## 12. Related Files

| File | Purpose |
|---|---|
| `SOP_HU_IG_Screenshot_Torn_Paper_v2.md` | Screenshot method (9:16 IG/TikTok) |
| `HU_Thumbnail_Creation_Process.md` | Master narrative of the torn-paper style |
| `skills_to_install/youtube-thumbnail/SKILL.md` | Full skill definition including viewer psychology framework |
| `youtube-thumbnail-log.md` | Log every generated+applied thumbnail here |
| `betty/HU logo new 2026 Watermark.png` | The HU logo — use unaltered |
| `skills_to_install/youtube-thumbnail/scripts/generate_thumbnail.py` | Generation script |
| `skills_to_install/youtube-thumbnail/headshots/` | Five approved reference photos |

---

## 13. Trait Graphic Rule — Handwriting Stroke Only (added 2026-08-13)

**Rule:** When passing a grapho-deck card or trait library image as a `--reference`, the prompt MUST instruct Gemini to extract ONLY the handwriting ink marks — never the full card.

**What to NEVER show in the thumbnail:**
- The green card background/strip
- Any text descriptions, labels, or trait names printed on the card
- Card borders, badge graphics, or framing elements

**What to show:**
- Only the raw handwriting strokes — the ink marks on a clean cream/white paper background
- The stroke should appear as a clinical specimen: ink on paper, possibly with a red circle or annotation arrow pointing to the specific trait stroke

**Mandatory language in every prompt (copy verbatim):**
> "From the handwriting reference image, extract and show ONLY the handwriting ink strokes themselves — do NOT reproduce the green card background, text descriptions, labels, badge, or any card framing. Show only the raw ink marks as if isolated on clean cream paper, displayed as a clinical handwriting specimen."

---

*Last updated: 2026-08-14 — Added §⛔ MANDATORY rules block, strengthened likeness anchor in §1, added headline source rule in §4, added two ⛔ rows at top of QA Gate in §9.*
