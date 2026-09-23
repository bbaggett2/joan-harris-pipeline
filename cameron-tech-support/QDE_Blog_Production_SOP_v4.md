# QDE BLOG PRODUCTION SOP v4 — celebrity & historical case articles on bartbaggett.com/blog

Owner: Cameron (blog production, WordPress and technical fixes). Created 2026-09-23. v2 (2026-09-23): blog notices moved to #qde-blog-post-project; Kristine's role is proofreading; n8n publish rule added. v3 (2026-09-23): errors and queue warnings go to #n8n-alerts (Bart); Kristine's channel only gets drafts to proofread. v4 (2026-09-23): n8n workflows renamed from "Betty" (social media) to "Cameron" (blog production).

## PEOPLE AND CHANNELS (two separate projects)

- **This project (QDE blog on bartbaggett.com):** Kristine S. proofreads and handles the WordPress blog posts. Drafts-to-proofread notices go to Slack **#qde-blog-post-project** (plus a direct message to Kristine). Kristine never gets error alerts. She is not a writer: she proofreads spelling, grammar, typos, both images and likeness, and notes fact problems for Bart instead of rewriting.
- **Errors and queue warnings:** Slack **#n8n-alerts** (Bart and Joan). Only Bart fixes n8n problems and adds new stories.
- **Not this project:** Katie handles video approval, Metricool, LinkedIn, etc. in #qde-celebrity-post-review, and still gets the video pipeline's errors there ("Betty — QDE Error Handler v1", unchanged). The blog pipeline must never post there.

This file says HOW the blog pipeline runs. It does not restate writing or image rules; it points to the files that own them.

## NAMING

The blog workflows carry Cameron's name because Cameron owns blog production; Peggy owns the words they write. "Betty" workflows are social media and are not part of this project. Older Peggy and Salvatore files may still say "Betty — QDE Blog Draft v1"; that is the same workflow under its old name.

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
2. **Daily scheduler:** workflow "Cameron — QDE Blog Drafts DAILY x5 — bartbaggett.com", every day 7:00 AM Central. Picks the next 5 rows (from row 3 down) that have a caption and no blog draft yet. A row that fails stays undrafted and is picked again the next day.
3. **Draft writer:** workflow "Cameron — QDE Blog Draft Writer (Peggy writes) — bartbaggett.com". Also has a manual form (post_id) for one-off drafts. For each case it:
   - reads the row, Peggy's article prompt and Bart's voice file, and writes the article with the AI (gpt-4.1), then runs an automatic fact-check against the source;
   - saves a Google Doc (flags, fact-check, TO VERIFY list, full article) in Drive folder "QDE Blog Drafts";
   - makes two images from Salvatore's prompts (featured widened to a crop-safe 1536 x 1024, main 1024 x 1024), saves them to Drive and uploads them to WordPress with alt, caption, title, description and clean filenames, and checks those fields saved;
   - creates a WordPress DRAFT: categories Forensic Document Examination (34) + articles (143), 3–5 tags, Yoast focus keyphrase / SEO title / meta description, the main image before the first section with its illustration caption, the public FAQ, the linked closing line last, and the hidden BlogPosting (speakable) + FAQPage schema;
   - writes the links and flags back to the sheet (blog_status, blog_doc_url, blog_wp_edit_url, blog_flags, image links).
4. **Notifications (Slack):** each draft posts a short note in #qde-blog-post-project; after each daily batch, Kristine S. gets a direct message listing the new drafts to proofread (WordPress link, Google Doc link, flags) and the same list posts in #qde-blog-post-project. When fewer than 5 cases remain after a batch, or none remain, a "queue low / queue empty" note posts in #n8n-alerts. Failures go to the blog error handler "Cameron — QDE Blog Error Handler v1 (#n8n-alerts)", which posts in #n8n-alerts.
5. **Publishing:** nothing is ever published automatically. Kristine proofreads (image checklist in Salvatore's SOP); fact questions from the TO VERIFY list go to Bart; a person publishes by hand.

## n8n RULE: SAVE IS NOT PUBLISH

n8n keeps a saved version and a published (active) version. The daily schedule and the form run the PUBLISHED version. After any edit to either blog workflow, publish it again, or the change does not reach the 7:00 AM run.

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
- The Dreyfus test post #4934 (made before these rules), if still on the site, should be redrafted with the current pipeline — Bart decides.
- Google Drive sometimes refuses requests for a minute (per-minute quota); the Google steps retry, and a case that still fails is picked again the next morning.
