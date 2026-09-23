# QDE CELEBRITY & HISTORICAL CASE ARTICLES — ARTICLE ENDING, FAQ & SCHEMA v2

Approved by Bart 2026-09-23 on the Aretha Franklin post (bartbaggett.com/blog/aretha-franklin-couch-will/).

The n8n workflow "Betty — QDE Blog Draft v1" reads THIS GitHub file every time it runs (bbaggett2/joan-harris-pipeline, peggy-olson-copywriting/QDE_Celebrity_Historical_Article_Closing_v2.md). Owner: Peggy. Every edit bumps the version number; change the n8n Config closing_url to match. Edit the text inside the ```text and ```html boxes to change every future draft. Keep the headings (## FAQ_HEADING, ## CTA_HTML) exactly as they are. If the file can't be read, the workflow uses its built-in copy and flags it in Slack.

## HOW EVERY ARTICLE ENDS (locked order)

1. The article body, ending with the "what this means for you" section.
2. A public FAQ section: the FAQ_HEADING below as an H2, then each question as an H3 with its answer as a normal paragraph.
3. The closing call-to-action paragraph (CTA_HTML below) as the very last paragraph. Same text style as the article, not bold, not boxed, not a button. Nothing that looks like an ad.
4. Hidden (not visible): the AEO schema block (BlogPosting with speakable pointing at the #speakable-summary paragraph, plus FAQPage). The FAQPage schema always uses exactly the same questions and answers as the public FAQ.

The AI's own version of the closing line is removed automatically and replaced with CTA_HTML, so the wording and links are always identical.

## FAQ RULES (set in the article prompt, QDE_Celebrity_Historical_Article_Prompt_v4.md)

- 5 to 7 questions. The first four are required, in this order, each naming the person or case:
  1. What happened in the [case]?
  2. When did it happen?
  3. What was the outcome?
  4. Was the handwriting or document ever questioned, and what role did document examination play?
- Then 1 to 3 more, such as how a document examiner would check this kind of document, or what to do if you face a similar document today.
- Answers are 1 to 3 plain sentences, use only source facts or general method, and stand alone when quoted by an AI.

## FAQ_HEADING

```text
Frequently Asked Questions
```

## CTA_HTML
The website and the phone number must both stay linked (the phone link dials on a phone).

```html
<p>If you’re dealing with a questioned will, signature, or document, Handwriting Experts Inc. can help. Visit <a href="https://handwritingexpertusa.com/">HandwritingExpertUSA.com</a> or call <a href="tel:+18009809030">1-800-980-9030</a>.</p>
```
