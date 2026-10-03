# Mobile Template: Master Architecture (v2.2)
**QDE / Bart Baggett Forensic Landing Pages** · v1 locked 2026-10-02 · v2 (merged look "C") approved 2026-10-02 · v2.1 (light grey headline) approved 2026-10-02 · v2.2 (rolled out live; blue bar everywhere; grey menu; local numbers) 2026-10-02
Reference page: `bartbaggett.com/usa/florida/documentexaminer_mobile.html`
Template file (same folder): `QDE_MOBILE_TEMPLATE_documentexaminer_mobile.template.html`

> Evidence labels: **[Verified]** = measured or read directly from code/data. **[Best estimate]** = inference or approximate. **[Unverified]** = user recollection, not confirmed by data.

---

## 1. Decision
Use the Florida mobile page layout as the master mobile template for all city landing pages, with the approved v2.2 look:
- **Light grey menu bar** (#e7e7e7, dark text). The old green menu was removed from all mobile pages.
- **Blue sticky click-to-call bar (#344279) on every mobile page.** Click-to-call is essential on mobile.
- Source Sans Pro for all text, bold headline.
- Tightened headline box in the **light grey #D6D6D6**.
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
- [Verified] The responsive /usa/1/ pages (non-`_mobile`) have no `mobile-callbar`. The `_mobile` pages already had it.
- [Verified] The media logo strip (CNN, Court TV, GMA, WSJ, Today, USA Today, NY Daily News) is part of the header image, so proof shows above the fold on phone.

### 2.5 Consistency audit of the 48 live mobile pages (2026-10-02)
- [Verified] Two looks existed: **A** = Source Sans Pro + lighter grey headline (#D6D6D6), 20 pages; **B** = Times + darker grey headline (#B9B9B9), 21 pages. Bart approved a merge ("C") and the lighter grey #D6D6D6.
- [Verified] v2.2 state: look "C" rolled out to the live mobile pages (41 pages). Menu green #1a7f2e replaced on 20 pages (menu now light grey, call bar blue). Blue call bar added to the 7 mobile pages that lacked it (Nevada June 2016 x4 at 702-996-0911, New Mexico ZH at 505-591-7909, Florida SanFran at 1-415-324-8780). All 48 verified to have a blue bar.
- [Verified] 38 mobile pages had no charset declaration and showed "â€™" for curly apostrophes; `<meta charset="utf-8">` was added right after `<head>`. Test/draft pages (Zakir x2, joanv3-5, _v2) were left alone. **Always keep `<meta charset="utf-8">` as the first element in `<head>`.**

## 3. Template architecture (top to bottom, phone)
1. **Credibility header image**: name, "Forensic Handwriting Expert & Court Qualified Expert Witness", portrait, media logo strip. Use `/usa/images/2026QDEexpert_credibility_header_clean.jpg` (the original had a baked-in dark column on the left edge, now removed; 124 pages updated).
2. **Menu bar** (light grey, collapsed "Menu"; links behind a tap).
3. **Headline box** (light grey #D6D6D6): 2-line bold H1 + phone number as its own H1 line. Tightened padding (see 4.2).
4. **Authority paragraph**: "seen on CNN, CBS, FOX, NBC... over 135 court qualifications and testimonies" (confirm the figure before reuse: the brand profile states about 138 testimonies, 100% judicial acceptance).
5. **Yellow-highlight CTA line**: "Call Today to Talk About Your Case".
6. **Celebrity/media photos** visible on first scroll. The second CNN photo is replaced by `https://bartbaggett.com/images/2013bart_testmonials_red.jpg` (no duplicate photos).
7. **Attorney testimonial near the top** (Florida: Scott image `Scott-testimonial-baggett-2026.jpg`), body copy, Riordan image (`riordan_testiml_small.jpg`) in the mid-page, text testimonials.
8. **Alex (ARose-testimonial.jpg) at the bottom**, once. Never duplicate a testimonial image on a page.
9. **Sticky bottom call bar** on every screen.
Brand rule: the "TEXAS JUSTICE" film strip (`/usa/images/35mmTexasJusticefilm.jpg`) belongs on Texas pages only (the show has been off the air for about 20 years, per Bart). Other pages use the Larry King banner hosted at `/images/2006larryking_banner2_hwexpertusa.jpg` / `/usa/images/2006larryking_banner2_hwexpertusa.jpg` (same domain, no cross-domain reach).

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
Required on every `_mobile` page. Use the city's local number, never the 1-800 number, on city pages.

### 4.2 Tight headline (reclaims about 64px; measured 208px -> 144px box at 390px wide)
```html
<style id="tight-headline">
#headline{padding:6px 12px !important}
#headline header,#headline center{margin:0 !important;padding:0 !important}
#headline h1{margin:4px 0 !important}
</style>
```
Cause of the wasted space: shared `salesletter.css` `#headline{padding:20px}` plus default H1 margins. Inject before `</head>`.

### 4.3 Typography and headline color
```html
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600;700&display=swap" rel="stylesheet">
<style id="bb-sans-merge">
body,p,li,td,h1,h2,h3,h4,h5,.testimonial2,#blurb,#section2,#nextstep,footer{font-family:"Source Sans Pro",Arial,Helvetica,sans-serif !important}
#headline h1,#headline h1 span{font-weight:700 !important}
h2{font-weight:700}
#headline{background:#D6D6D6 !important;color:#000 !important}
</style>
```

### 4.4 Grey menu (v2.2)
```html
<style id="bb-menu-grey">html body .menu_container .mobile_collapser,html body #menu1 .mobile_collapser,html body label.mobile_collapser{background:#e7e7e7 !important;color:#222 !important}</style>
```
Also replace any hard-coded green `#1a7f2e` with `#344279`.

### 4.5 Other mobile rules in the reference page
`h1{font-size:24px!important}`, `h2{font-size:20px!important}`, single-column override (`#section1{display:none}`), images `max-width:100%`, container max 800px.

## 5. Per-city values
| City | `{{PHONE_DISPLAY}}` | `{{PHONE_TEL}}` | `{{PHONE_CHAT}}` |
|---|---|---|---|
| Florida | 1-305-459-1544 | +13054591544 | 305-459-1544 |
| San Francisco | 1-415-324-8780 | +14153248780 | 415-324-8780 |
| Dallas | 1-214-614-8122 | +12146148122 | 214-614-8122 |
| Los Angeles | 1-323-544-9277 | +13235449277 | 323-544-9277 |
| Nevada (June 2016 pages) | 1-702-996-0911 | +17029960911 | 702-996-0911 |
| New Mexico (ZH page) | 1-505-591-7909 | +15055917909 | 505-591-7909 |
| National (/usa/1/) | 1-800-980-9030 (CST) | +18009809030 | 800-980-9030 |
Nevada and New Mexico numbers were taken from the pages themselves [Best estimate: confirm with Bart]. The Florida-named SanFran page now uses the San Francisco number everywhere (the Miami international line for Bahamas callers was also changed to it by Bart's go-ahead).

`{{PHONE_CHAT}}` fills the chat widget `support-contact` attribute. `{{name}}` inside the widget is a GoHighLevel token: leave it alone.
Also edit city-specific strings after filling the placeholders (testimonial comment; footer "Serving Clients in Florida, Texas and Worldwide").
Copy rules: phone-first. Never use "text us" wording with the office numbers (the PR line "Call or Text our PR team at 310-779-7224" is the one approved exception). Domain: always **HandwritingExpertUSA.com**, never HandwritingExpert.com. Media/press-kit menus carry no sales number; the footer 1-800 number on /usa/presskit stays.

## 6. Rollout and deploy
- Archive the original on the server before overwriting: `<stem>_Joan_<YYYY-MM-DD>[b..z].html`, then put the new file.
- Verify live: fix present, `mobile-callbar` present and blue, tel number correct per city, Source Sans Pro loading, `document.characterSet` = UTF-8.
- Done (2026-10-02): tight headline, look "C" with light grey headline, grey menu, blue call bar on all 48 mobile pages, charset fix on 38 pages, local city numbers, clean header image on 124 pages.
- Still open: the responsive /usa/1/ pages (non-`_mobile`) have no call bar; per-city mobile templates for the other cities still need their per-city edits.

## 6b. Desktop (not the mobile template; recorded for consistency)
Sub pages (rates, CV, FAQ, press kit, reviews, contact) on 26 pages use a thin blue-grey band `#D6E0E1` (band color picked by eye: [Best estimate]) with a black title in place of the red H1, thin 25%-black frame lines on both sides of the 800px column, and a white column background. Style id `bb-headline-band`; pages with a padded wrapper also carry `bb-band-edge` so the band runs edge to edge. Source: `html body #headline h1{color:#AD1C17 !important}` in `bb-conversion.css` caused the red title.

## 7. Open items and caveats
- After rollout, test mobile cost per phone-click conversion on `_mobile` pages against the $63-91 baseline (phone-click conversions only).
- Confirm the testimonial count claim (135 vs about 138) before reuse.
- Nov 2025-Mar 2026 call data is compromised (OneBox dropped about 30%); do not use it as the baseline.
- Whether the media images were moved above the fold in 2025 because of research is **[Unverified]**.
- Headline color and grey shade are untested; consider an A/B test now that the call bar is live everywhere.
- Test/draft pages (Zakir x2, joanv3-5, _v2) still have the encoding problem and were not changed.
