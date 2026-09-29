# Curt Baggett blog schema: handoff to Cameron (draft v1)

Status: DRAFT, NOT INSTALLED. Nothing has been changed on curtbaggett.com for schema. Cameron owns schema; review before use.

## What curtbaggett.com outputs today (audited on one published post, /7-can-a-handwriting-expert-be-wrong/)
- SEO plugin: AIOSEO. Single JSON-LD block (class aioseo-schema) with BlogPosting, BreadcrumbList, Organization, Person (Curt Baggett, /author/curtbaggett/#author), WebPage, WebSite.
- BlogPosting has no image and no speakable. No FAQPage anywhere.
- Posts do not contain QDE markers (qde-faq-start / qde-faq-end) or #speakable-summary.
- FAQ layout on that post: H2 "Frequently Asked Questions" followed by alternating <p> question / <p> answer pairs (questions end with ?). Other posts NOT checked; structure may differ.

## What the draft does
1. FAQPage JSON-LD built from the FAQ H2 section (no markers needed).
2. Adds id="speakable-summary" to the first FAQ answer paragraph.
3. Enriches AIOSEO's own BlogPosting (image, speakable) instead of printing a second one. Filter name aioseo_schema_output is a best estimate and is NOT verified. Please confirm against AIOSEO docs / live site.

## Open items for Cameron
- Verify the AIOSEO filter name and that the enrichment does not duplicate nodes.
- Confirm FAQ structure across all posts (drafts and scheduled too).
- Person node has no sameAs; Bart said no profile URLs to add. Do not invent any.
- Featured images on the next 13 scheduled posts are the 1200x675 editorial WebP (see salvatore-art-department/Curt_Baggett_Design_Template_v1.md); confirm og:image resolves to it.
- Firewall: Curt-only. No Bart Baggett, Handwriting Experts Inc., phone numbers, or QDE CTAs in any output.
- Tested only for PHP syntax and a dry run of the FAQ parser on sample markup. Not tested in WordPress.
