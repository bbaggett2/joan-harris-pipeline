# Mobile Template: Master Architecture
**QDE / Bart Baggett Forensic Landing Pages** · Locked 2026-10-02
Reference page: `bartbaggett.com/usa/florida/documentexaminer_mobile.html`
Template file: `template/mobile/documentexaminer_mobile.template.html`

> Evidence labels: **[Verified]** = measured or read directly from code/data. **[Best estimate]** = inference or approximate. **[Unverified]** = user recollection, not confirmed by data.

---

## 1. Decision
Use the Florida mobile page layout as the master mobile template for all city landing pages.
Phone-first, proof above the fold, one persistent call action.

## 2. Why (findings)

### 2.1 Ad data (Google Ads "Bart Baggett QDE ExpertUSA", Oct 2015-Sep 2026; SoCal #1, SoCal #2, CPA National; Display excluded)
- [Verified] Best-performing pages by bartbaggett.com conversions: `/usa/1/handwritinganalysis.html` and `/usa/1/handwritingexpert.html` (desktop).
- [Verified] Mobile variants (`_mobile`) cost far more per conversion than desktop: about $63-91 vs $29-33 per conversion on the handwritingexpert page. This is the gap the template targets.
- [Verified] "Conversions" on the California domain are inflated (sitelink/preview clicks fire the tag). Only phone-click conversions are trustworthy, and they are sparse.
- [Best estimate] About 70% of traffic is mobile now.

### 2.2 Historical page evidence (archived FTP copies 2016-2026)
- [Verified] The headline and phone-led CTA (no forms) persisted across the decade on handwritinganalysis and signatureexpert; documentexaminer's headline changed Feb 2024.
- [Verified] Phone-first, call-driven conversion is the constant. Forms were never the mechanism.
- [Unverified] Grey headline bar vs. red headline text: the date of the grey override is unknown (all CSS stamped Feb 26 2020). Bart recalls red as the standard since 2003.

### 2.3 2014 Crazy Egg (handwritingexpertusa.com/index.html; 689 visits, 496 clicks)
- [Verified] Headline text and top banner drew the most clicks; nav links were about 10% of clicks; readers spent 1-4 minutes before acting.
- [Caveat] One page, different domain, small sample, about 89% desktop. Directional only.

### 2.4 Live fold measurements (2026-10-02, real Chrome, bartbaggett.com)
| Page | Viewport | Result |
|---|---|---|
| /usa/1/handwritinganalysis | 390x844 | Header image + tall H1 (about 360px); H3 starts about 700px; **no call bar, no tel link, no nav links in view**; page about 10,800px |
| /usa/1/handwritingexpert | 390x844 | Same pattern |
| /usa/1/ pages | 1280x800 | Nav and 1-800 number visible; CNN image starts about 785px (barely above fold) |
| /usa/florida/documentexaminer_mobile | phone | Short 2-line headline + phone number, logo strip in header, CNN photo visible, **sticky Call Now bar** |
- [Verified] The /usa/1/ pages have no `mobile-callbar` (searched live HTML).
- [Verified] The media logo strip (CNN, Court TV, GMA, WSJ, Today, USA Today, NY Daily News) is part of the header image, so proof shows above the fold on phone.

## 3. Template architecture (top to bottom, phone)
1. **Credibility header image**: name, "Forensic Handwriting Expert & Court Qualified Expert Witness", portrait, media logo strip.
2. **Menu bar** (collapsed "Menu"; links behind a tap).
3. **Headline box** (grey): 2-line H1 + phone number as its own H1 line. Tightened padding (see 4.2).
4. **Authority paragraph**: "seen on CNN, CBS, FOX, NBC... over 135 court qualifications and testimonies" (confirm the figure before reuse: the brand profile states about 138 testimonies, 100% judicial acceptance).
5. **Yellow-highlight CTA line**: "Call Today to Talk About Your Case".
6. **Celebrity/media photo (CNN)** visible on first scroll.
7. Body copy, testimonials, credentials (existing salesletter content).
8. **Sticky bottom call bar** on every screen.

## 4. Code spec

### 4.1 Sticky call bar
```css
body { padding-bottom: 64px; }
#mobile-callbar { display:block; position:fixed; left:0; right:0; bottom:0; z-index:9999;
  background:#344279; text-align:center; padding:14px 0; box-shadow:0 -2px 8px rgba(0,0,0,.3); }
#mobile-callbar a { color:#fff; font-weight:700; font-size:21px; text-decoration:none; letter-spacing:.3px; }
```
```html
<div id="mobile-callbar"><a href="tel:{{PHONE_TEL}}">📞 Call Now: {{PHONE_DISPLAY}}</a></div>
```

### 4.2 Tight headline (reclaims about 64px; measured 208px -> 144px box at 390px wide)
```html
<style id="tight-headline">
#headline{padding:6px 12px !important}
#headline header,#headline center{margin:0 !important;padding:0 !important}
#headline h1{margin:4px 0 !important}
</style>
```
Cause of the wasted space: shared `salesletter.css` `#headline{padding:20px}` plus default H1 margins. Inject before `</head>`.

### 4.3 Other mobile rules in the reference page
`h1{font-size:24px!important}`, `h2{font-size:20px!important}`, single-column override (`#section1{display:none}`), images `max-width:100%`, container max 800px.

## 5. Per-city values
| City | `{{PHONE_DISPLAY}}` | `{{PHONE_TEL}}` |
|---|---|---|
| Florida | 1-305-459-1544 | +13054591544 |
| Dallas | 1-214-614-8122 | +12146148122 |
| Los Angeles | 1-323-544-9277 | +13235449277 |
| National (/usa/1/) | 1-800-980-9030 (CST) | +18009809030 |

Also edit city-specific strings after filling the placeholders (Florida testimonial comment; footer "Serving Clients in Florida, Texas and Worldwide").
Domain rule: always **HandwritingExpertUSA.com**, never HandwritingExpert.com.

## 6. Rollout and deploy
- Archive the original on the server before overwriting: `<stem>_Joan_<YYYY-MM-DD>[b..j].html`, then put the new file (see `webops/tight_2026-10-02/go.py`).
- Verify live: fix present, `mobile-callbar` present, tel number correct per city.
- Done so far: Florida `documentexaminer_mobile.html` live with the tight headline (archive: `documentexaminer_mobile_Joan_2026-10-02.html`).
- Next (pending Bart's choice): /usa/1/ ad landing pages first (highest ad traffic, no call bar today), then Dallas, Los Angeles and the remaining city folders.

## 7. Open items and caveats
- After rollout, test mobile cost per phone-click conversion on `_mobile` pages against the $63-91 baseline (phone-click conversions only).
- Confirm the testimonial count claim (135 vs about 138) before reuse.
- Nov 2025-Mar 2026 call data is compromised (OneBox dropped about 30%); do not use it as the baseline.
- Whether the media images were moved above the fold in 2025 because of research is **[Unverified]**.
- Headline color (red vs grey/black) is untested; consider an A/B test once the call bar is live.
