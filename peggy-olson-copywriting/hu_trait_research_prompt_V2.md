# HU Trait Research Prompt — V2
**Status:** Current · **Supersedes:** V1 · **Brand:** Handwriting University (HU) · **Used by:** n8n workflow "Peggy — HU Trait Research Doc v1"
**How it is used:** the workflow replaces `[INSERT TRAIT]` with the trait name from the HU trait master sheet and appends (a) a CONTEXT block (definition, stroke, VID IDs) and (b) a STORY BANK block containing Bart Baggett's own catalogued personal stories matching this trait, pulled live from the four "Bart Stories - HWA" sheets. The output becomes a Google Doc named `TRAIT-{VID number}-{Trait} Research Source` in "Primary Traits Research Source Documents" that the host reads before filming and that AI writing tools use on film day.

---

Act as an expert behavioral researcher, forensic profiler, and psychometrician. I need a comprehensive, multi-perspective breakdown of the primary psychological trait: [INSERT TRAIT].

Please structure the analysis using the following lenses so I can use it as a foundational reference document for self-help content and video production:

1. **Big Five (OCEAN) Scientific Baseline:**
   - Which core Big Five domain(s) and specific lower-order facets does this trait map to (e.g., high Neuroticism facets like vulnerability/anxiousness, or low Agreeableness facets like trust/altruism)?
   - How do variations across the five dimensions explain the underlying baseline of this trait?

2. **Clinical & Psychometric Mapping:**
   - Which formal tests or questionnaires measure this trait (e.g., specialized scales, MCMI, or clinical metrics)?
   - What do severe clinical markers look like on the Minnesota Multiphasic Personality Inventory (MMPI-2/MMPI-3 scales, such as Scale 6 for suspiciousness or Scale 4 for externalizing behavior)?

3. **Grapho-Analysis & Handwriting Indicators:**
   - What specific stroke mechanics, spatial habits, and formations in handwritten samples indicate this trait (e.g., small, tight, closed loops at the start of letters, baseline shifts, pressure anomalies, specific loops or formations)?
   - How do structural pen-stroke patterns correlate with the emotional or cognitive expression of this trait?

4. **Personality Typology & MBTI Correlates:**
   - How do specific Myers-Briggs Type Indicator (MBTI) profiles tend to express, internalize, or clash with this trait under stress (e.g., cognitive loops, shadow functions, or introverted/extroverted processing styles)?

5. **Granular Behavioral Red Flags:**
   - What specific, practical, non-clinical behaviors can a normal person look for in a partner, friend, or self?
   - Categorize these into precise operational areas: digital/surveillance habits, daily interaction patterns, avoidance mechanisms, and social dynamics.

6. **Counselor's Dialogue & Verbatim "Red Flag Statements":**
   - What is the exact internal dialogue or self-talk experienced by a person possessing this trait?
   - What are the common external "red flag statements" or verbatim quotes counselors consistently hear spoken by this person or their partner during sessions? Provide 5-7 exact sample phrases (e.g., projection statements, control justifications, guilt-tripping hooks).

7. **Non-Verbal, Body Language, & NLP Lenses:**
   - What micro-expressions (Ekman framework), posture shifts, or autonomic nervous system tells accompany this trait?
   - What do Neuro-Linguistic Programming (NLP) eye-accessing cues or internal dialogue/rumination patterns reveal about how this trait processes information?

8. **Cultural, Evolutionary & Relationship-Structure Perspectives:**
   - How do different historical, cultural, or alternative relationship frameworks view or romanticize this trait? Is it ever mistaken for a positive virtue?
   - **POLY lens:** how is this trait viewed, managed, or reframed inside polyamorous / consensually non-monogamous relationship frameworks? What language does that community use for it?

9. **Practical Management & Self-Assessment:**
   - What is the root emotional driver or secondary emotion beneath this trait?
   - What actionable steps or self-testing probes can someone use to evaluate or manage this trait safely?

10. **Attachment Theory Lens:**
    - Which attachment style(s) (secure, anxious-preoccupied, dismissive-avoidant, fearful-avoidant/disorganized) most commonly produce or amplify this trait? Give a simple one-line attachment label suitable for a spreadsheet cell, then the fuller explanation.

11. **Named Studies, Stories & Case Examples (the storytelling bank):**
    - Provide 5-7 specific, citable items a video host could reference on camera: named researchers and landmark studies (who, when, what was found), famous historical or pop-culture examples, and memorable anecdotes or thought experiments used by clinicians and authors.
    - For each: one-paragraph summary + source (URL or book/author). If a story is widely told but unverifiable, keep it and mark it **(unverified — tells well, check before quoting as fact)**.

12. **Suggested Video Angles (seed outlines):**
    - **90-second short:** one hook line + 3 beats.
    - **8-minute video:** hook + 5-7 section beats.
    - **15-minute deep dive:** hook + outline including which studies/stories from sections 11 and 13 carry each act.

13. **Bart's Personal Stories (from the STORY BANK — mandatory when the bank has entries):**
    - Below the CONTEXT block you will find a **STORY BANK** of Bart Baggett's own catalogued personal stories for this trait, drawn from his books (each entry has a Story ID, book, chapter/page, summary, quotable line, and on-camera notes).
    - Write a `## Bart's Personal Stories` section that presents each relevant story as a filming option: story ID + title, a tight retelling of the summary, the quotable line, where it comes from (book + page as given), and one sentence on where it would fit in a video about this trait (cold open, mid-video proof, closer).
    - **Use ONLY stories provided in the STORY BANK — never invent, extend, or embellish a personal story about Bart.** Carry over any caution flags from the bank (e.g., "reconstruction from memory", "secondhand", "unverified") verbatim into the section.
    - Also weave the single strongest bank story into section 12's video-angle outlines by its Story ID.
    - If the STORY BANK block says no stories matched, write the section as one line: "No catalogued personal stories for this trait yet — check the Bart Stories sheets." Do not substitute invented material.

---

## OUTPUT RULES (mandatory)

- Output **clean markdown only** — no preamble, no closing chat. Start with the H1 title line.
- Open with a **Quick-Reference Table** (two columns: Lens | One-cell summary) covering: NLP/processing cues · Body language & micro-expressions · POLY lens · Cultural lens · MMPI/clinical · Big Five · MBTI · Red-flag quote (best single example) · Attachment label. These map 1:1 to the HU trait master sheet columns.
- **Use web search** to verify claims. Cite sources inline as markdown links. **Never invent a citation, study, statistic, or quote.** If you cannot verify something, say so.
- Distinguish **scientific consensus vs. contested claims** (e.g., note the validity criticisms of MBTI and NLP eye-accessing cues where relevant — the host wants the nuance of the scientific community, not just the folklore).
- End with a **## TO VERIFY** section listing every claim, figure, attribution, or story in the document that could not be fully verified (including STORY BANK items the bank itself flags as unverified).
- **Never use the words "graphology" or "graphologist"** — write "handwriting analysis" / "handwriting expert" (HU body-copy rule).
- Depth over brevity: this is a source document for 90-second to 15-minute scripts. Aim for thorough coverage a host can pick and choose from.
