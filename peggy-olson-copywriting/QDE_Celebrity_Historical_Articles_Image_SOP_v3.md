# QDE CELEBRITY & HISTORICAL CASE ARTICLES — IMAGE SOP v3

For bartbaggett.com/blog articles made by "Betty — QDE Blog Draft v1" from the QDE_Post_Queue sheet (Aretha Franklin, Howard Hughes, Hitler Diaries, Dreyfus, Zodiac, etc.).

Set by Bart, 2026-09-22. v2 (2026-09-23): featured image blog-card crop fix. v3 (2026-09-23): adds image SEO / accessibility rules adapted from an outside review (ChatGPT "WordPress image publishing SOP", reviewed by Claude; only the points that fit this site were adopted — see "Decisions" at the end).

Priority order for every image: factual honesty and legibility → accessibility → page speed → a good click/preview image. File-size targets are house budgets, not Google ranking rules. There is no special image field for "AEO".

## THIS IS NOT THE AEO QUESTION-ARTICLE SOP

AEO question articles ("How long does handwriting analysis take?", city-site Q&A posts) use a different rule set: no faces, 2–3 words, quiet mood scene. Those rules do NOT apply here. See "_OLD — AEO question-article image rules" only for that other article type.

## THE GOAL

Featured images are designed to get the click. The famous person's NAME and FACE (or the famous document, if there is no person) must be in both images. No "furniture catalog" images. (Bart's rule. Google advises against text-heavy preview images for Discover; we keep the name and a short headline anyway, but keep on-image text short: name + 2 headline lines, nothing else.)

## HONESTY RULES FOR AI IMAGES (NEW in v3)

- Every face and every document in these images is an AI-generated illustration, not a photograph and not the real document. Never present it as authentic.
- Handwriting on papers, envelopes, notebooks and book spines must be unreadable scribble texture. No readable names, dates or words on documents except the planned headline, name line and (main image only) the short torn-note bullets from column J. This prevents misspellings like "Surfoced", "erivelope" and wrong names like "Melvin DuMar".
- Never write text on an image that claims Bart examined the historical document.

## TWO IMAGES PER ARTICLE

### 1. FEATURED IMAGE (the click image: blog list cards, the social/Google preview, og:image)

**Artwork (the square "E" layout):**

- Very large 2-line headline that includes the famous name (e.g. ARETHA'S WILL / WAS IN THE COUCH), one word in gold (#FFE455).
- Left half: the famous person's portrait (description taken from the sheet's column J image_prompt).
- Right half: one scene from the case (the couch notebook, the torn bordereau, etc.).
- Deep navy (#10142E), moody light, film grain. No other text.

**Final file: the square artwork centered on a wide canvas (required):**

The bartbaggett.com blog list (Blocksy theme) crops every featured image to fill its card, roughly 266 x 232 px on desktop (about 1.15 : 1) and narrower on phones. A plain square image loses its top and bottom; a wide AI-generated image loses its sides, and words get cut off ("VAS IN THE COUCH"). Asking the AI image generator to "keep text in the center safe area" does NOT work (it ignored that instruction twice, 2026-09-23). So the safe area is built in code:

1. Generate or approve the square 1:1 featured artwork as above.
2. Center it on a wide canvas: square resized to 860 x 860, canvas 1536 x 1024, navy (#10142E) or blurred-and-darkened copy of the art around it. Never stretch or warp the square.
3. Save under the size limit below.

Result: all headline words and the face sit in the middle 56% of the width, so the desktop card (~64% visible) and a phone card (~60% visible) never cut them off.

**Why the featured file stays large (at least 1200 px wide):** Yoast uses the featured image as the page's og:image (social and Google preview). Google Discover's large preview wants an image at least 1200 px wide, over 300,000 pixels, landscape. Our 1536 x 1024 composite meets all three (checked on the Aretha page 2026-09-23, and the page already sends max-image-preview:large). WordPress automatically makes smaller copies (srcset) for the small blog cards — the blog list loads the 768 x 512 copy, not the full file.

- Set the wide composite (not the plain square) as the WordPress Featured Image.
- Approved example: Aretha Franklin post #4924, aretha-franklin-couch-will-featured-1.jpg (1536 x 1024, 108 KB).

### 2. MAIN IMAGE (inside the article)

- The sheet's column J image_prompt poster, squared to 1:1, with a small name line added above the headline (e.g. ALFRED DREYFUS).
- Keeps the column J details: headline with gold word, sub-line, short torn-note bullets, magnifier. Any other handwriting, envelope text or book spines stay unreadable texture.
- Placed in the article just before the first section heading.
- Stays square (1024 x 1024). It is not the preview image, so it does not need to be landscape.
- Gets a caption that says it is an illustration (see the text rules below).

## SIZE AND FORMAT

| Image | Dimensions | Target | Hard limit |
|---|---|---|---|
| Featured (click / preview) | 1536 x 1024 composite (at least 1200 px wide) | 90–125 KB | 130 KB |
| Main (in article) | 1024 x 1024 | 85–110 KB | 130 KB |

- Measure the real file size, not an editor's estimate. The workflow flags anything over 130 KB in the sheet (blog_flags) and in Slack.
- Format: JPEG today. WebP is the preferred future format (smaller at the same quality) once the workflow is tested to upload WebP correctly; until then JPEG stays. DPI/PPI settings do not matter on the web.
- Never stretch an image to change its shape; pad or recompose instead.

## IMAGE TEXT FIELDS (alt, caption, title, description, filename) (NEW in v3)

The article prompt (QDE_Celebrity_Historical_Article_Prompt_v3.md) tells the AI to write these; these are the rules.

- **Alt text:** describe what is actually visible, in one short phrase, and say it is an illustration. Example: "Illustration of Aretha Franklin beside a spiral notebook will under a couch cushion". Not the article headline. Under 125 characters. Each image gets a different alt.
- **Caption (main image):** one sentence that makes clear it is an AI illustration, not the real document or a photo. Example: "Illustration: Aretha Franklin and the 2014 notebook will found in her couch. Not a reproduction of the original document." Featured image: no caption needed.
- **Title:** plain name, e.g. "Aretha Franklin couch will illustration".
- **Description:** one or two factual sentences for the media library. Not a place for keywords.
- **Public filename:** short, lowercase, hyphens, the article slug plus the role, e.g. `aretha-franklin-couch-will-featured.jpg` and `aretha-franklin-couch-will-main.jpg`. Do not put internal IDs like "QDE-FC-1_blog-" in the public WordPress filename; the Drive copy keeps the ID.
- Do not stuff "forgery", "handwriting expert", "forensic document examiner" or Bart's name into every field.

## TAGS

- 3–5 tags per article, specific to the case: the famous name, the case or document name, the document type. Reuse existing tags when they match; create a new one only for a new case name. No long generic tag lists.

## SOURCE OF TRUTH

- Column J (image_prompt) of QDE_Post_Queue is the master art direction for each case. Improve the image by editing column J, not the workflow.
- Column D (headline) and E (gold_word) guide the headline wording. Fix typos there (e.g. D2 "ARETHA'S FRANKLIN'S", D3 "HOWARD HUGES").

## REVIEW CHECKLIST (Kristine, before publishing)

1. Spelling: read every word on BOTH images. If wrong, regenerate or fix.
2. Honesty: no readable fake names or claims on documents; the main image caption says it is an illustration.
3. Crop check: open bartbaggett.com/blog (hard refresh) and confirm every headline word and the face show fully in the post's card.
4. Likeness: does the face look like the real person? If not, regenerate.
5. Rights: the sheet's face_source column says "Editorial license required (Getty/AP)". These are AI-generated likenesses, not licensed photos. Bart decides whether that is acceptable per case.
6. Facts on the image (dates, names, bullets) must match the article's verified facts.
7. Alt text describes what is in the picture (not the headline); caption, title and description read sensibly.
8. First time on a new theme or plugin setup only: check the page source for og:image (should be the featured image, 1200+ px wide) and max-image-preview:large, and run PageSpeed Insights on one article.

## WHERE FILES LIVE

- Drive ("QDE Blog Drafts" folder): `POSTID_blog-featured_SLUG.jpg` and `POSTID_blog-main_SLUG.jpg`, linked in the sheet columns blog_image_url and blog_main_image_url.

## WORKFLOW STATUS (as of 2026-09-23)

Done in n8n:
- Featured square automatically centered on a 1536 x 1024 navy canvas ("Widen featured (crop-safe)", JPEG quality 68; Howard Hughes test 118 KB).
- Daily scheduler drafts the next 5 undrafted cases at 7:00 AM Central, starting at sheet row 3. Drafts only.
- Image prompts and article text rules are read from GitHub every run.

Still to build in n8n (approved rules above, not yet automated):
- The in-article image tag uses the AI's descriptive main_alt (today it uses "NAME: article title"), and shows the illustration caption under it.
- Public WordPress filenames without the "QDE-FC-x_blog-" prefix.
- After upload, read back each image's alt/caption/title/description to confirm they saved.
- WebP output, after a test upload.

## DECISIONS ON THE OUTSIDE REVIEW (2026-09-23)

Adopted: describe-the-picture alt text; illustration disclosure in captions; no readable fake document text; clean public filenames; no keyword stuffing; 3–5 specific tags; never stretch images; measure real bytes; verify saved fields; WebP as the target format after testing; check og:image and max-image-preview once.

Not adopted, and why:
- 800 x 450 featured image: Yoast uses the featured image as og:image, so an 800 px featured would drop below Google Discover's 1200 px minimum. WordPress already serves small copies to cards.
- 16:9 featured shape: the blog cards crop to about 1.15 : 1, so a 16:9 image loses its sides; the centered-square composite is the tested fix.
- Removing the headline text from images: conflicts with Bart's rule (name and a click headline on both images). Kept, but short.
- Landscape main image: it is not the preview image, so the square column J poster stays.
- The JSON "contract" from Claude to n8n: n8n generates the images itself; no hand-off file is needed.
