# QDE CELEBRITY & HISTORICAL CASE ARTICLES — IMAGE SOP v2

For bartbaggett.com/blog articles made by "Betty — QDE Blog Draft v1" from the QDE_Post_Queue sheet (Aretha Franklin, Howard Hughes, Hitler Diaries, Dreyfus, Zodiac, etc.).

Set by Bart, 2026-09-22. Revised 2026-09-23 (v2): featured image blog-card crop fix.

## THIS IS NOT THE AEO QUESTION-ARTICLE SOP

AEO question articles ("How long does handwriting analysis take?", city-site Q&A posts) use a different rule set: no faces, 2–3 words, quiet mood scene. Those rules do NOT apply here. See "_OLD — AEO question-article image rules" only for that other article type.

## THE GOAL

Featured images are designed to get the click. The famous person's NAME and FACE (or the famous document, if there is no person) must be in both images. No "furniture catalog" images.

## TWO IMAGES PER ARTICLE

### 1. FEATURED IMAGE (the thumbnail people click from the blog list, search and social previews)

**Artwork (the square "E" layout):**

- Very large 2-line headline that includes the famous name (e.g. ARETHA'S WILL / WAS IN THE COUCH), one word in gold (#FFE455).
- Left half: the famous person's portrait (description taken from the sheet's column J image_prompt).
- Right half: one scene from the case (the couch notebook, the torn bordereau, etc.).
- Deep navy (#10142E), moody light, film grain. No other text.

**Final file: the square artwork centered on a wide canvas (NEW in v2 — required):**

The bartbaggett.com blog list (Blocksy theme) crops every featured image to fill its card, roughly 266 x 232 px on desktop (about 1.15 : 1) and narrower on phones. A plain square image loses its top and bottom; a wide AI-generated image loses its sides, and words get cut off ("VAS IN THE COUCH").

Asking the AI image generator to "keep text in the center safe area" does NOT work. It ignored that instruction in two tests (v2 and v3 of the Aretha image, 2026-09-23). So the safe area is built in code, not in the prompt:

1. Generate or approve the square 1:1 featured artwork as above.
2. Make a wide canvas 1536 x 1024.
3. Fill the canvas with the same square image stretched, heavily blurred (radius about 40) and darkened to about 45% brightness, so the edges are only soft background.
4. Resize the square artwork to 860 x 860 and paste it in the exact center (338 px margin left and right, 82 px top and bottom).
5. Save as JPEG, quality stepped down until under 125 KB (Aretha result: 108 KB).

Result: all headline words and the face sit in the middle 56% of the width. The desktop card shows the middle ~64% and a phone card (0.9 : 1) about 60%, so nothing is cut off in either. Search and social previews (wide 1.91 : 1) also show the whole square.

- Set the wide composite (not the plain square) as the WordPress Featured Image.
- Approved example: Aretha Franklin post #4924, media aretha-franklin-couch-will-featured-1.jpg (2026-09-23).

### 2. MAIN IMAGE (inside the article)

- The sheet's column J image_prompt poster, squared to 1:1, with a small name line added above the headline (e.g. ALFRED DREYFUS).
- Keeps the column J details: headline with gold word, sub-line, torn-note bullets, magnifier, book spines.
- Placed in the article just before the first section heading.
- Stays 1024 x 1024; it is not cropped inside the article, so it needs no wide canvas.

## SOURCE OF TRUTH

- Column J (image_prompt) of QDE_Post_Queue is the master art direction for each case. Improve the image by editing column J, not the workflow.
- Column D (headline) and E (gold_word) guide the headline wording. Fix typos there (e.g. D2 reads "ARETHA'S FRANKLIN'S").

## SIZE

- Main image: 1024 x 1024 JPEG, compressed by the image generator. Target 85–110 KB.
- Featured image: 1536 x 1024 JPEG composite. Target 90–125 KB.
- Hard limit 130 KB for both; the workflow flags anything larger in the sheet (blog_flags) and in Slack.

## REVIEW CHECKLIST (Kristine, before publishing)

1. Spelling: read every word on BOTH images. AI images sometimes misspell small text (seen: "torn in preces", gibberish book spines). If wrong, regenerate or fix.
2. Crop check: open bartbaggett.com/blog (hard refresh) and confirm every headline word and the face show fully in the post's card. If anything is clipped, the featured image was not put on the wide canvas.
3. Likeness: does the face look like the real person? If not, regenerate.
4. Rights: the sheet's face_source column says "Editorial license required (Getty/AP)". These are AI-generated likenesses, not licensed photos. Bart decides whether that is acceptable per case.
5. Facts on the image (dates, names, bullets) must match the article's verified facts.
6. Alt text, caption and description are set automatically. Check they read sensibly.

## WHERE FILES LIVE

- Both images are saved in the "QDE Blog Drafts" Drive folder as `POSTID_blog-featured_SLUG.jpg` and `POSTID_blog-main_SLUG.jpg` (e.g. `QDE-FC-1_blog-featured_aretha-franklin-couch-will.jpg`), and linked in the sheet columns blog_image_url and blog_main_image_url.

## WORKFLOW STATUS (as of 2026-09-23)

- The Aretha featured image was fixed by hand with this method.
- The n8n workflow still uploads the plain square featured image. The wide-canvas step still has to be added to it before the workflow goes live for Kristine.
