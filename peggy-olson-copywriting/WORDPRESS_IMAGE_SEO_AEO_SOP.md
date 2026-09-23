# WordPress image publishing SOP: forensic articles

**Owner:** Bart Baggett / Questioned Document Examiner (QDE) editorial workflow  
**Applies to:** Claude Cowork writing and image preparation, n8n automation, WordPress publishing  
**Version:** 2026-09-23  
**Reference article:** https://bartbaggett.com/blog/dreyfus-bordereau-handwriting-experts-2/

## 1. Purpose and decision rules

Create fast, accessible, factually accurate images that help readers understand a case and give search systems appropriate context. Produce **two distinct image assets** for each article: a lightweight image actually displayed as the article's featured/hero image, and a larger editorial image in the body that may also serve as the article's social/Discover preview. A WordPress *featured media ID* does not automatically determine the file used in the visible hero, `og:image`, or JSON-LD: inspect the theme and SEO plugin output and explicitly map each role.

**Priority order:** factual integrity and legibility → accessibility → displayed-page speed → suitable preview imagery → optional metadata. File-size targets below are house budgets, **not Google ranking thresholds**. There is no special image size or metadata field required for “AEO.” Google Discover eligibility is not a guarantee of placement.

| Role | Output master | Target bytes | Review threshold | Placement |
| --- | --- | --- | --- | --- |
| Featured / visible hero / archive card | 800 × 450 WebP | 40–80 KB | >100 KB | WordPress featured image and visible article hero where theme uses it |
| Primary editorial / preview image | 1200 × 675 WebP, or 1280 × 720 when a useful composition needs it | 100–180 KB | >200 KB | Article body; `og:image` and `BlogPosting.image` when relevant and suitable |
| Supporting body image | Usually 800–1200 px wide, aspect ratio suited to evidence | Smallest legible file | Review >200 KB | Beside relevant explanation |

The editorial image must be **at least 1200 px wide** if intended for Google Discover's large-image preview. Google also recommends more than 300,000 pixels total, landscape framing near 16:9, `max-image-preview:large`, and a representative `og:image` or schema image. A 1200 × 675 image meets those numeric recommendations. The 800px featured asset alone does **not**. Some social platforms impose their own preview behavior; inspect the generated preview. See [Google Discover](https://developers.google.com/search/docs/appearance/google-discover).

**Exception:** If the theme/SEO plugin forces the featured media to be the only `og:image` or schema image, configure an explicit 1200px social image. If that is impossible, use a ≥1200px master as featured media and rely on verified responsive WordPress/CDN derivatives for the 800px visual display. Never sacrifice the large preview merely to keep the uploaded featured master at 800px. Conversely, a 1200px file downloaded at full size into every 400px card fails the speed goal. Verify actual network transfers.

## 2. What the supplied Dreyfus examples actually show

The provided image file `QDE-FC-13_blog-main_dreyfus-bordereau-handwriting-experts.jpg` is **1024 × 1024 JPEG, 99,955 bytes (~97.6 KiB)**. It contains a Dreyfus likeness, stylized torn handwritten pages, and substantial headline text. The screenshot `1024 X1024.png` shows a *separate Preview resize operation* estimating **190 KB** for a 1024 × 1024 output; do not confuse that estimate with the measured attached JPEG. WordPress screenshots show an alt field containing a headline-like phrase, and empty caption/title/description fields in the illustrated dialogs. A screenshot is not proof that every live attachment has the same metadata; verify each media ID. The prior assessment that the live article has a long tag list also requires confirmation in the publishing system before treating it as a current-site finding.

| Before: observed or supplied | After: production requirement |
| --- | --- |
| Square 1024 × 1024 image and a JPEG master | Compose landscape 16:9 versions; deliver WebP after visual inspection |
| Text-heavy image headed “1894: Dreyfus Was Accused of Treason” | Keep the readable headline in HTML; produce a less text-heavy preview with safe mobile cropping |
| Alt text reads like an article headline rather than a visual description | Describe the actual visible illustration, including that document imagery is reconstructed |
| Caption and other fields blank in the screenshots | Fill meaningful fields per role; omit captions when they add nothing |
| Internal prefix `QDE-FC-13_blog-main_...` in public filename | Use concise descriptive filename; keep campaign/job ID separately in workflow metadata |
| No demonstrated split between small displayed image and large preview | Explicitly assign visible hero, body image, `og:image`, and schema image; inspect published HTML |

The image depicts **an editorial reconstruction**. Do not label its simulated handwriting as an authenticated photograph of the original bordereau. Do not invent exact transcriptions, signatures, ink evidence, or a claim that Bart examined this historical case.

### Dreyfus AFTER example: metadata and placement

Use the exact alt wording only if the final generated/cropped image actually depicts the named elements. Otherwise rewrite it after inspecting the final pixels.

| WordPress / page field | Featured asset: visible hero | Primary body asset: large preview |
| --- | --- | --- |
| Filename | `alfred-dreyfus-bordereau-featured.webp` | `dreyfus-affair-bordereau-editorial.webp` |
| Alt text | `Editorial illustration of Alfred Dreyfus beside reconstructed bordereau pages` | `Editorial reconstruction of Alfred Dreyfus and the torn handwritten bordereau` |
| Media title | `Alfred Dreyfus and the bordereau` | `Dreyfus Affair: bordereau editorial illustration` |
| Caption | Empty if the theme displays no informative caption | `Editorial reconstruction of Dreyfus and the bordereau; the pictured handwriting is illustrative, not a reproduction of the original document.` |
| Media description | `Landscape editorial illustration for the Dreyfus Affair article; document imagery is reconstructed.` | `Landscape editorial illustration of Alfred Dreyfus and reconstructed handwritten bordereau pages for an article about disputed handwriting evidence.` |
| Alt in published HTML | Check the visible `<img alt="...">` | Check the body `<img alt="...">` |
| Page use | WordPress `featured_media`, visual hero/cards | Body `<figure>` and preferred `og:image` / schema `image` if representative |

**Before alt shown in the screenshot:** `ALFRED DREYFUS: The Dreyfus Affair: How Handwriting Experts Split Over the Bordereau`. **After:** a description of the rendered visual above. Keep the story's headline as the page heading, not as a substitute for alt text. A body caption is optional in general, but is useful here to make the reconstruction explicit.

**Artwork instruction:** Recompose from original sources or generate a 16:9 landscape editorial artwork. Preserve meaningful subject matter and legible faces; use a deliberately styled reconstruction of the papers. Remove or greatly reduce baked-in headline text because the page H1 already supplies it and Google advises avoiding text-heavy preferred previews. Do not stretch a square to 16:9. If cropping the existing square, verify nothing important is cut off; a genuinely redesigned landscape image will usually work better. Preserve a record of any real source photograph/document and rights or credit requirements.

## 3. Asset creation and compression

1. Establish the story's subject, evidence, visual source, usage rights, and whether the document is genuine, a photograph, a replica, or an AI illustration. Keep those distinctions in the prompt and caption.
2. Compose or crop a landscape master; inspect at full size and at a small mobile/card size. Keep faces and evidence away from crop edges. Avoid illegible fake text and unsupported words in generated documents.
3. Export separate 800 × 450 and ≥1200 × 675 files as WebP; resize proportionally, never warp. Use a better quality setting for evidence whose visible detail matters. For a detailed document, a portrait crop or zoomable supplemental image can coexist with the 16:9 preview.
4. Compare real encoded byte counts (decimal KB and/or KiB consistently), not an editor's estimated export size. Compress until within targets without ruining relevant visual evidence. If the file exceeds the review threshold, record a justified exception.
5. Check the MIME signature really is `image/webp`, extension `.webp`, target pixel dimensions, color appearance, sharpness, and spelling. Do not turn an unreadable 1200px graphic into a smaller unreadable 800px graphic.
6. Keep originals and license/credit details in the internal asset record. Never expose production IDs or unverifiable provenance as search metadata.

WebP is the default workflow format; AVIF can be used if the site's delivery stack correctly handles it. JPEG is acceptable when WebP upload or delivery fails, provided the image remains optimized. DPI/PPI metadata is irrelevant to web display. WordPress thumbnails, responsive `srcset`, and CDN conversions must be *verified* in rendered HTML and network requests; uploading a master does not prove the visitor received an appropriately sized derivative.

## 4. Editorial metadata rules

| Field | Rule | Why |
| --- | --- | --- |
| Filename | Short, lowercase, hyphen separated, specific to depicted subject; append `-featured` or `-editorial` to distinguish roles | Mild contextual clue; stable asset identity |
| Alt text | One concise sentence fragment describing what is visually present and its relevant function; mark reconstructions as such | Accessibility and image understanding |
| Media title | Plain human-readable name; use only verified facts | Library organization and possible visible contexts |
| Caption | Include when it supplies evidence context, date, attribution, or reconstruction disclosure; can be empty for a redundant featured hero | Reader context; potentially useful to search systems |
| Description | One or two factual sentences for internal asset management; do not treat as a ranking field | Editorial traceability |
| Article H1 / nearby prose | Clearly identify the case, the document, dispute, findings, and uncertainty | Page meaning is more important than repeating terms in image fields |

Do not stuff `forgery`, `handwriting expert`, `forensic document examiner`, or Bart's name into every field. Avoid identical alt strings for visually different files. Don't make factual claims based on AI-rendered handwritten text. For an image that is truly decorative and redundant, use empty `alt=""` in the actual page markup; do not omit the `alt` attribute. For linked image cards, alt may need to convey the link's destination in context. For text shown *only* inside a graphic, alt must carry the meaningful text or the same information must appear in adjacent HTML.

**Taxonomy:** Use only relevant WordPress categories/tags from the existing taxonomy. Proposed Dreyfus tags: `Dreyfus Affair`, `Alfred Dreyfus`, `bordereau`, `questioned documents`—only if the corresponding tags exist or meet the site's taxonomy rules. Do not create dozens of generic tags, and do not equate tags with Google meta keywords. Confirm live output before removing any existing tag system.

## 5. Claude Cowork → n8n → WordPress contract

Claude should deliver **structured data and image files**, not only prose. n8n validates, uploads, maps IDs, saves a draft, and checks the rendered result. The following JSON is an illustrative contract; replace URLs and IDs with actual response values.

```json
{
  "article_slug": "dreyfus-bordereau-handwriting-experts",
  "h1": "The Dreyfus Affair: How Handwriting Experts Split Over the Bordereau",
  "image_claims_checked": true,
  "assets": [
    {
      "role": "featured_visible",
      "filename": "alfred-dreyfus-bordereau-featured.webp",
      "width": 800,
      "height": 450,
      "mime_type": "image/webp",
      "max_review_bytes": 100000,
      "alt_text": "Editorial illustration of Alfred Dreyfus beside reconstructed bordereau pages",
      "title": "Alfred Dreyfus and the bordereau",
      "caption": "",
      "description": "Landscape editorial illustration for the Dreyfus Affair article; document imagery is reconstructed."
    },
    {
      "role": "editorial_preview",
      "filename": "dreyfus-affair-bordereau-editorial.webp",
      "width": 1200,
      "height": 675,
      "mime_type": "image/webp",
      "max_review_bytes": 200000,
      "alt_text": "Editorial reconstruction of Alfred Dreyfus and the torn handwritten bordereau",
      "title": "Dreyfus Affair: bordereau editorial illustration",
      "caption": "Editorial reconstruction of Dreyfus and the bordereau; the pictured handwriting is illustrative, not a reproduction of the original document.",
      "description": "Landscape editorial illustration of Alfred Dreyfus and reconstructed handwritten bordereau pages for an article about disputed handwriting evidence."
    }
  ],
  "preferred_preview_role": "editorial_preview",
  "article_tags_proposed": ["Dreyfus Affair", "Alfred Dreyfus", "bordereau", "questioned documents"]
}
```

### n8n sequence and field mapping

1. **Validate input:** Verify binaries independently of model-supplied dimensions and MIME; reject absent assets, distorted ratios, invalid/empty meaningful alt text, unreviewed historical claims, or unapproved oversize images. Treat the byte values above as review thresholds, with a logged exception path. Keep draft status on failure.
2. **Upload each binary:** `POST /wp-json/wp/v2/media` with the image bytes, appropriate authentication, `Content-Disposition: attachment; filename="...webp"`, and `Content-Type: image/webp`. Record each returned attachment ID and `source_url`. Do not assume an upload succeeded based solely on the HTTP call initiating.
3. **Update attachment fields:** Send `POST /wp-json/wp/v2/media/{id}` with `alt_text`, `title`, `caption`, `description` as appropriate. WordPress REST supports these fields; title/caption/description may be accepted as strings and returned as rendered objects. GET each record and confirm persisted values. Escape caption text safely in HTML if the system accepts HTML.
4. **Create/update a WordPress draft:** `POST /wp-json/wp/v2/posts` or update its ID with `status: "draft"`, correct title/content, `featured_media: <featured ID>`, and validated category/tag IDs. Put the main body image in a WordPress image block or `<figure><img ...></figure>` with its returned URL and correct alt; never embed a local path. Prefer native image blocks where possible to retain responsive attachment behavior.
5. **Set preferred preview:** Configure the site's SEO plugin/social image to use the ≥1200px editorial URL/ID for `og:image`; ensure JSON-LD `BlogPosting.image` (or equivalent page image) points to the same representative large image. The exact API/meta field depends on installed plugin and which custom meta fields it exposes to REST. Inspect configuration; do not invent an `og_image` parameter on the core posts endpoint. If the plugin automatically uses featured media, implement the exception in §1.
6. **Verify the draft in its rendered template:** Check the hero, article image, actual WordPress media IDs, captions, responsive `srcset`/`sizes`, and `width`/`height`; inspect page source for `og:image`, article schema, and `max-image-preview:large` (and absence of conflicting restrictive preview directives). Confirm the large preview URL actually returns the expected image, is crawlable and publicly accessible after publication.
7. **Publish only after editorial approval in the established publishing process.** Recheck the published page; log the URL, attachment IDs, actual bytes and dimensions, preview URL, and validation results. On failure, leave draft and report the exact field/asset that needs repair.

**Core WP REST mapping:** `media.alt_text` → attachment alt; `media.title`, `.caption`, `.description` → attachment metadata; `posts.featured_media` → attachment ID. Media descriptions and titles are not substitutes for the actual `<img alt>` value. Depending on the editor/theme, the image block may store its own alt; explicitly confirm rendered HTML. Do not assume the featured-media relationship creates an article-body image or caption.

### Optional rendered markup pattern

```html
<figure>
  <img src="https://EXAMPLE/wp-content/uploads/dreyfus-affair-bordereau-editorial.webp"
       alt="Editorial reconstruction of Alfred Dreyfus and the torn handwritten bordereau"
       width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Editorial reconstruction of Dreyfus and the bordereau; the pictured handwriting is illustrative, not a reproduction of the original document.</figcaption>
</figure>
```

This `loading="lazy"` example is for an image **below the first viewport**. If the body image is the page's LCP/first-viewport image, remove lazy loading; consider `fetchpriority="high"` for the actual LCP image after measurement. Never set high fetch priority on both images by rote. Add responsive `srcset`/`sizes` via WordPress rather than copying this illustrative `src`-only snippet verbatim into production.

## 6. Acceptance checks for every article

### Mandatory automation checks

- [ ] Featured and editorial assets are different intended outputs or a documented responsive-master exception; image dimensions, MIME signature, byte counts, and aspect ratios verified from actual files.
- [ ] Editorial preview image is ≥1200px wide, >300,000 pixels total, representative, and legible at mobile preview sizes.
- [ ] No evidence or person is fabricated as authentic; reconstructions are labeled; visual claims and rights/credits reviewed.
- [ ] Filenames are concise and unique; alt text matches final rendered pixels; captions/descriptions reflect the image and are present when useful.
- [ ] Both media uploads return IDs; GET confirms saved alt/title/caption/description; post has expected `featured_media` ID and body image URL.
- [ ] HTML uses an ordinary `<img src>` (or `<picture>` with `<img src>` fallback), useful `srcset`/`sizes`, and intrinsic width/height.
- [ ] Actual hero/LCP image is not lazy loaded; below-fold images may be; downloaded card image is appropriately small.
- [ ] `og:image` and structured article image, where present, resolve to the ≥1200px representative image; `max-image-preview:large` is allowed.
- [ ] H1, intro, nearby image context, and article-specific tags accurately describe the case; no irrelevant bulk taxonomy.
- [ ] Post stays draft when a hard validation check fails; log exceptions to soft byte targets.

### First deployment / periodic manual checks

- [ ] Check the real published template on mobile and desktop, including article hero, homepage cards, related-post cards, social preview, and cropped Discover-like preview.
- [ ] Inspect network transfer size and selected `currentSrc`; ensure theme/CDN does not load a 1200px original unnecessarily into small cards.
- [ ] Run [PageSpeed Insights](https://pagespeed.web.dev/) on representative pages. Use observed LCP and layout shift to change sizing or image priority; do not treat a single KB target as a performance guarantee.
- [ ] Confirm image URLs are accessible to crawlers and not excluded by a CDN, `robots.txt`, or authentication; inspect Search Console for indexing/discovery rather than promising inclusion.

## 7. Sources and scope of authority

The **1200px Discover recommendation**, resolution and landscape guidance, `max-image-preview:large`, preferred image signals, and avoidance of text-heavy previews come from [Google Search Central: Discover](https://developers.google.com/search/docs/appearance/google-discover). Google [Image SEO Best Practices](https://developers.google.com/search/docs/appearance/google-images) supports standard `<img>` elements, responsive images, optimization, relevant captions/context, concise filenames, and useful alt text. [WordPress media](https://developer.wordpress.org/rest-api/reference/media/) and [posts](https://developer.wordpress.org/rest-api/reference/posts/) document the REST fields. [web.dev image performance](https://web.dev/learn/images/performance-issues) explains LCP prioritization and avoiding lazy loading of above-the-fold images. **The pixel choices for the 800px featured asset and all KB budgets are this site's editorial defaults, not published Google standards.**

Review this SOP when the site's theme, SEO plugin, CDN, WordPress configuration, or Google documentation changes. Record actual site behavior before automating a plugin-specific field.
