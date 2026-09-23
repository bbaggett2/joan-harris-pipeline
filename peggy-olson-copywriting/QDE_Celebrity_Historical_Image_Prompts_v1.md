# QDE CELEBRITY & HISTORICAL CASE ARTICLES — IMAGE PROMPTS v1

The n8n workflow "Betty — QDE Blog Draft v1" reads THIS GitHub file every time it runs (bbaggett2/joan-harris-pipeline, peggy-olson-copywriting/QDE_Celebrity_Historical_Image_Prompts_v1.md). Edit the text inside the three ```text boxes below to change every future image. Rules and review steps are in QDE_Celebrity_Historical_Articles_Image_SOP_v2.md.

HOW TO EDIT SAFELY
- Only change text INSIDE the ```text boxes. Keep the three headings (## FEATURED_PROMPT, ## MAIN_PROMPT_ADDON, ## MAIN_PROMPT_FALLBACK) exactly as they are, or the workflow cannot find the prompts.
- Words in curly braces are filled in automatically for each article. Keep the braces:
  - {SUBJECT} = the famous person's portrait description (from the sheet's column J)
  - {SCENE} = one scene from the case (e.g. a spiral notebook under a couch cushion)
  - {LINE1} and {LINE2} = the two headline lines, in capitals
  - {GOLD} = the one headline word shown in gold
  - {NAME} = the famous name line, e.g. ARETHA FRANKLIN
  - {COLUMN_J} = the full image_prompt from the sheet's column J (main image only)
- If you break the file, the workflow falls back to the built-in copy of v1 and flags it in Slack.

## FEATURED_PROMPT
The click image (square "E" layout). After it is made, the workflow centers it on a wide 1536 x 1024 canvas so the blog card never cuts off words (see SOP v2).

```text
Cinematic editorial blog featured image, 1:1 square, photoreal, designed to earn a click at small thumbnail size. Deep navy background (#10142E), moody light from upper left, film grain. LEFT HALF: {SUBJECT}, looking into camera. RIGHT HALF: {SCENE}, lit by warm gold light. TOP: very large bold condensed white headline on two lines "{LINE1}" / "{LINE2}" with only the word "{GOLD}" in gold (#FFE455). No other text anywhere. Spell every word exactly. Leave generous contrast so the headline reads on a phone.
```

## MAIN_PROMPT_ADDON
The in-article image. The workflow takes the sheet's column J prompt ({COLUMN_J}), changes any 4:5 portrait wording to 1:1 square, and uses the text below as the full prompt.

```text
{COLUMN_J} Add a small white condensed all-caps name line "{NAME}" with a thin gold rule directly above the headline. The name line is the only text added; keep all other text exactly as described above. Spell every word exactly.
```

## MAIN_PROMPT_FALLBACK
Used only when column J is empty or very short (under 200 characters).

```text
Cinematic editorial blog image, 1:1 square, photoreal, rich editorial detail for display inside the article. Deep navy background (#10142E), moody light from upper left, film grain. LEFT HALF: {SUBJECT}, looking into camera. RIGHT HALF: {SCENE}, lit by warm gold light. TOP: very large bold condensed white headline on two lines "{LINE1}" / "{LINE2}" with only the word "{GOLD}" in gold (#FFE455). Add a small white condensed all-caps name line "{NAME}" with a thin gold rule above the headline. No other text anywhere. Spell every word exactly.
```
