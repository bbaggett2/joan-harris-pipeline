# CURT BAGGETT DESIGN TEMPLATE v1 — blog featured images for curtbaggett.com

**Owner:** Salvatore (art department). **Brand:** Curt Baggett / curtbaggett.com ONLY.
**Status:** LOCKED — approved by Bart 2026-09-28. Changes require a new version file (v2), never edits to this one.
**Companion file:** `salvatore-art-department/Curt_Baggett_Blog_Template_v1.html` (the production template that renders these designs).
**Metadata/upload rules:** follow `peggy-olson-copywriting/WORDPRESS_IMAGE_SEO_AEO_SOP.md` for sizes, WebP, alt text, and REST field verification.

## FIREWALL

This template belongs to the Curt Baggett brand. In any image, label, or filename produced from it:
- NEVER include Bart Baggett, Handwriting Experts Inc., HandwritingExpertUSA.com, any phone number, Handwriting University, The Bart Show, or any QDE/HU/Bart-brand CTA, domain, or credential.
- The only domain that may appear is CURTBAGGETT.COM. The only name that may appear is Curt Baggett (always spelled C-U-R-T).
- Do not point QDE image prompts or Bart-brand thumbnail SOPs at this template, or vice versa.

## DESIGN PHILOSOPHY — "Examined Evidence"

Every graphic is a questioned document under scrutiny: the visual language of the forensic bench (ruled baselines, exhibit stamps, examiner's red annotations, the loupe's magnified circle) elevated into composition. Each layout stages a dialogue between the organic (a handwritten stroke) and the analytic (grid, caliper ticks, clinical labels). Space is evidentiary — one dominant gesture, generous margins. Text is sparse: a kicker, the article title, the domain. Handwritten script appears only as specimen, never as voice. Drawn signature strokes are always ABSTRACT loops and curves — never a legible name or a reproduction of any real person's actual signature (the ghost "Curt Baggett" script in Style B is a font, not his real signature, and must stay that way).

## PALETTE (locked)

| Role | Hex | Use |
|---|---|---|
| Slate navy | #2B3542 | primary field (Style A), authority — matches curtbaggett.com |
| Deep navy | #222A35 | Style C left panel, loupe frame |
| Archival cream | #F4EFE6 | paper fields (Styles B, C right panel) |
| Cream ink (light strokes) | #E9E2D3 | specimen strokes on navy |
| Examiner red | #B0392E (#C4453A on navy) | annotations, kicker on cream, EXHIBIT stamp — one accent per board, never decorative |
| Brass | #A98B4F | instrumentation: scales, ticks, kicker on navy |
| Ink | #2F3A47 | title text on cream |
| Rule lines | #3A4655 on navy / #D8CFBC–#DDD4C1 on cream | ruled baselines and grids |

Maximum four color voices per board. No gradients, no drop shadows, no stock photos, no AI-generated imagery.

## TYPOGRAPHY (locked)

| Voice | Font | Use |
|---|---|---|
| Title serif (dark boards) | IBM Plex Serif Bold | Styles A & C titles, 41–44px, line-height ~1.22–1.24 |
| Title serif (cream board) | Lora Bold | Style B title, 56px |
| Clinical labels | IBM Plex Mono | kickers (14–15px, letter-spacing .4em), case numbers, scales, domain |
| Byline sans | Work Sans | Style B byline only |
| Specimen script | Nothing You Could Do | ghost signatures / "examined" artifacts only, 50–65% opacity |

All fonts are free Google Fonts (OFL). Title is always the post's H1, verbatim. If a title exceeds ~90 characters, reduce title font ~10% rather than truncating or rewriting.

## THE THREE LOCKED LAYOUTS

Rotate **A → B → C → A …** down the post queue so consecutive posts never share a layout.

**STYLE A — "Dark Exhibit"** (navy field)
Kicker top-left: `FORENSIC DOCUMENT EXAMINATION` (brass). Top-right case block: `SPECIMEN / Q-DOC` + `EXHIBIT NO. {n}` (n = post number in queue, zero-padded). Right half: abstract cream signature stroke crossing faint ruled baselines, two red annotation circles with leader lines labeled `Q-1` / `Q-2`, brass measurement scale beneath labeled `BASELINE ANALYSIS 0–144 mm`. Title lower-left (max width 600px), domain `CURTBAGGETT.COM` bottom-left.

**STYLE B — "Question Card"** (cream paper)
Red vertical margin rule at 60px; faint ruled lines lower half. Kicker top-left: `ASK THE DOCUMENT EXAMINER` (red). Rotated red `EXHIBIT A` stamp top-right (letter rotates B, C, D… down the queue). Title upper-left in Lora. Red accent bar, then byline `Curt Baggett · Forensic Handwriting Expert`. Ghost script signature lower-right at 50% opacity. Domain bottom-right.

**STYLE C — "The Loupe"** (split: deep navy left 560px / cream grid right)
Left: kicker `EXPERT ANALYSIS` (brass), title in Plex Serif, domain bottom. Right: large loupe (navy ring + inner brass ring + crosshair ticks + handle to lower-right) magnifying an abstract ink stroke; one red annotation circle with leader line labeled from the approved list; ghost script partially behind the lens; caliper scale bottom with caption `MAGNIFICATION 10× · STROKE DETAIL`.

**Approved annotation labels (only these):** Q-1, Q-2, K-1, K-2, TREMOR, PEN LIFT, BASELINE, RETOUCH, HESITATION, LETTERFORM. Never invent labels implying a real case, a real verdict, or a real person's writing.

## VARIATION RULES (what may change per post / what may not)

May vary: title text, exhibit number/letter, which approved annotation labels are used, the abstract stroke path (regenerate curves so no two boards are identical), scale end-value (e.g. 0–144 mm).
May NOT vary: palette, fonts, layout geometry, kicker wording, logo/domain treatment, number of accent colors, addition of photos/illustrations/gradients.

## OUTPUT SPEC (per the Image SEO/AEO SOP)

1. Render each board at 1200×675 (2× device scale) from the HTML template → export **WebP**, 100–180 KB target → article body / og:image / schema image.
2. Derive 800×450 WebP, 40–80 KB → WordPress featured image.
3. Filenames: `{post-slug}-editorial.webp` and `{post-slug}-featured.webp`.
4. Alt text describes the actual visual, marks it as an illustration (e.g. `Illustration of an examined signature stroke with forensic annotation marks`), never keyword-stuffed, never the headline verbatim.
5. Upload via REST with alt/title/caption/description; GET to verify fields saved.

## PRODUCTION

Rendered headlessly (Chromium/Playwright screenshot of the HTML template) — no manual design work per post. The batch script substitutes title, exhibit number, labels, and stroke path per post, cycling layouts A→B→C in queue order.
