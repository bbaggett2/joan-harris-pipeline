# QDE BLOG PRODUCTION SOP v1 — celebrity & historical case articles on bartbaggett.com/blog

Owner: Cameron (blog production, WordPress and technical fixes). Created 2026-09-23.

This file says HOW the blog pipeline runs. It does not restate writing or image rules; it points to the files that own them.

## WHO OWNS WHAT

| Lane | Owner | File (GitHub, this repo) | Read by n8n every run? |
|---|---|---|---|
| Article writing rules, SEO/AEO fields, FAQ rules | Peggy | peggy-olson-copywriting/QDE_Celebrity_Historical_Article_Prompt_v4.md | Yes |
| Bart's voice (how every sentence sounds) | Peggy | peggy-olson-copywriting/BART_BAGGETT_VOICE.MD | Yes (attached to the article prompt) |
| Article ending: public FAQ heading and the linked closing line | Peggy | peggy-olson-copywriting/QDE_Celebrity_Historical_Article_Closing_v2.md | Yes |
| Image prompts | Salvatore | salvatore-art-department/QDE_Celebrity_Historical_Image_Prompts_v2.md | Yes |
| Image rules and image review checklist | Salvatore | salvatore-art-department/QDE_Celebrity_Historical_Articles_Image_SOP_v4.md | No (for people) |
| Pipeline, schedule, WordPress settings, notifications | Cameron | this file | No (for people) |

When any of these files gets a new version number, the matching URL in the n8n workflow's Config node must be changed the same day (prompt_url, voice_url, closing_url, image_prompts_url).

## THE PIPELINE (n8n, empresse.app.n8n.cloud)

1. **Source:** Google Sheet QDE_Post_Queue (one row per case: caption, headline, fact-check notes, column J image prompt).
2. **Daily scheduler:** workflow "Betty — QDE Blog Drafts DAILY x5 (bartbaggett.com)", every day 7:00 AM Central. Picks the next 5 rows (from row 3 down) that have a caption and no blog draft yet. A row that fails stays undrafted and is picked again the next day.
3. **Draft writer:** workflow "Betty — QDE Blog Draft v1 (bartbaggett.com)". Also has a manual form (post_id) for one-off drafts. For each case it:
   - reads the row, Peggy's article prompt and Bart's voice file, and writes the article with the AI (gpt-4.1), then runs an automatic fact-check against the source;
   - saves a Google Doc (flags, fact-check, TO VERIFY list, full article) in Drive folder "QDE Blog Drafts";
   - makes two images from Salvatore's prompts (featured widened to a crop-safe 1536 x 1024, main 1024 x 1024), saves them to Drive and uploads them to WordPress with alt, caption, title, description and clean filenames, and checks those fields saved;
   - creates a WordPress DRAFT: categories Forensic Document Examination (34) + articles (143), 3–5 tags, Yoast focus keyphrase / SEO title / meta description, the main image before the first section with its illustration caption, the public FAQ, the linked closing line last, and the hidden BlogPosting (speakable) + FAQPage schema;
   - writes the links and flags back to the sheet (blog_status, blog_doc_url, blog_wp_edit_url, blog_flags, image links).
4. **Notifications (Slack):** after each daily batch, Kristine S. gets a direct message listing each new draft (WordPress link, Google Doc link, flags) and the same message posts in #qde-celebrity-post-review. When fewer than 5 cases remain after a batch, or none remain, a "queue low / queue empty" note posts in #qde-celebrity-post-review.
5. **Publishing:** nothing is ever published automatically. Kristine edits, checks the TO VERIFY list and the image checklist (Salvatore's SOP), and publishes by hand.

## WORDPRESS SETTINGS THE PIPELINE DEPENDS ON

- REST user: application password stored only in n8n as credential "bartbaggett blog wordpress".
- Yoast fields writable over REST via the WPCode snippet "Yoast fields for n8n" (registers _yoast_wpseo_focuskw, _yoast_wpseo_metadesc, _yoast_wpseo_title). Do not deactivate it.
- Yoast uses the featured image as og:image; pages send max-image-preview:large (checked 2026-09-23).
- Blocksy blog cards crop featured images to about 1.15 : 1; that is why the featured image is widened (see Salvatore's SOP).
- Categories are set by ID inside the n8n workflow (34, 143), not from a file yet.

## KNOWN GAPS (as of 2026-09-23)

- Category IDs live in the n8n workflow, not in a GitHub file.
- WebP images not yet tested; JPEG in use.
- The public form URL for manual drafts is open to anyone who has the link.
- The repo is public; nothing secret may be committed here.
- Old test posts: Dreyfus #4934 (published, made before these rules) and #4927 (draft) need redoing or removing — Bart decides.
