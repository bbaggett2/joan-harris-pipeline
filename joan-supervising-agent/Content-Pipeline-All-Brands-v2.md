# Content-Pipeline-All-Brands

## Purpose

This file is the governing instruction document for the n8n workflow
named **Content-Pipeline-All-Brands**.

The workflow turns raw content ideas into researched, brand-appropriate
content while preserving Bart Baggett's real expertise, opinions,
stories, voice, and professional boundaries.

The system must distinguish between:

1.  **Source facts** --- independently verifiable facts and research.
2.  **Bart knowledge** --- material Bart has authored or taught.
3.  **Bart perspective** --- Bart's documented opinions,
    interpretations, professional observations, stories, humor, and
    preferred framing.
4.  **AI synthesis** --- organization and drafting performed by AI.
5.  **Fresh Bart input** --- required when the existing library does not
    establish Bart's perspective strongly enough.

The AI may synthesize Bart's existing material. It must never invent a
Bart opinion, personal experience, case involvement, credential,
quotation, or professional conclusion.

------------------------------------------------------------------------

## Canonical Content Source

The starting point and master editorial queue for
**Content-Pipeline-All-Brands** is the designated Google Sheet:

-   **Spreadsheet ID:** `1lA4-OB3SM_lOssthD5XyJldwlJz10uJt`
-   **Starting tab GID:** `546834024`
-   **Role:** Content Control Center and system of record for content
    opportunities, routing, production status, approvals, and published
    outputs.

n8n must treat this Google Sheet as **Step 1 of the workflow and the
canonical production queue**.

GitHub is **not** the content queue. GitHub supplies the knowledge, Bart
voice, Bart perspective, source materials, governing rules, approved
examples, books, transcripts, case histories, and reusable intellectual
property required to process each spreadsheet row.

``` text
GOOGLE SHEET — CONTENT CONTROL CENTER / SOURCE QUEUE
        ↓
GITHUB — BART KNOWLEDGE + VOICE + PERSPECTIVE LIBRARY
        ↓
n8n — ORCHESTRATION + DECISION ENGINE
        ↓
AI — CLASSIFICATION + RESEARCH + DRAFTING + QA
        ↓
WORDPRESS / VIDEO / SOCIAL — OUTPUTS
        ↓
GOOGLE SHEET — STATUS + ASSET IDS + URLS + RESULTS
```

Unless a later approved configuration explicitly changes the source, n8n
begins with a selected/eligible row from this spreadsheet and writes
workflow state back to the same system of record.

------------------------------------------------------------------------

## 1. Workflow Input

The canonical Google Sheet identified above is the master editorial
queue and production system of record.

Each row should have a permanent `content_id`, such as:

-   `TR-001`
-   `TR-002`
-   `TR-047`

`TR` means **To Record**, preserving lineage from the original To Record
database.

Derivative assets should retain the parent ID:

-   `TR-047-ARTICLE`
-   `TR-047-VIDEO`
-   `TR-047-SHORT`
-   `TR-047-SOCIAL`

The spreadsheet should tell n8n:

-   topic
-   original note
-   source URL
-   primary lane
-   content vertical
-   voice mode
-   Bart authority level
-   whether Bart perspective exists
-   whether fresh Bart perspective is required
-   intended output
-   research/fact-check status
-   production status
-   publication destination
-   published URL

The spreadsheet is the **queue and status database**. GitHub is the
**knowledge, voice, perspective, rules, and source-content library**.

------------------------------------------------------------------------

## 2. GitHub Knowledge Repository

Use a predictable repository structure.

``` text
/bart-knowledge/

    /00_MASTER/
        BART_VOICE_AND_PERSPECTIVE_MASTER.md
        BART_BIO_CREDENTIALS.md
        CONTENT_LANE_RULES.md
        FACT_CHECKING_AND_CITATION_RULES.md

    /01_VOICE/
        BART_VOICE_GUIDE.md
        APPROVED_BART_WRITING.md
        BART_PHRASES_AND_PATTERNS.md
        ANTI_VOICE_EXAMPLES.md

    /02_QDE/
        QDE_BART_PERSPECTIVE.md
        QDE_BART_OPINIONS.md
        QDE_CASE_HISTORIES.md
        QDE_FAMOUS_CASE_COMMENTARY.md
        QDE_TERMINOLOGY.md

    /03_HANDWRITING_ANALYSIS/
        /books/
        HWA_BART_PERSPECTIVE.md
        HWA_UPDATED_POSITIONS.md

    /04_HAPPY_WEALTHY_MIND/
        /books/
        HWM_BART_PERSPECTIVES.md
        HWM_CORE_PRINCIPLES.md

    /05_STORIES/
        BART_PERSONAL_STORIES.md
        BUSINESS_STORIES.md
        MEDIA_STORIES.md

    /06_TRANSCRIPTS/
        /bart_show/
        /podcasts/
        /interviews/
        /seminars/
        /videos/

    /07_PUBLISHED_CONTENT/
        /articles/
        /newsletters/
        /social/

    /08_CONTENT_EXAMPLES/
        /approved/
        /rejected/

    /09_RESEARCH/
        /famous_cases/
        /studies/
        /source_material/
```

------------------------------------------------------------------------

## 3. Source Hierarchy

Before drafting, n8n should retrieve the smallest relevant set of files.

### Level 1 --- Governing files

Always load or retrieve relevant sections from:

-   `BART_VOICE_AND_PERSPECTIVE_MASTER.md`
-   `CONTENT_LANE_RULES.md`
-   `FACT_CHECKING_AND_CITATION_RULES.md`

Load `BART_BIO_CREDENTIALS.md` when biography, credentials, experience,
court qualification, media appearances, books, companies, or authority
claims are used.

### Level 2 --- Brand/vertical knowledge

Retrieve according to the row's `content_vertical` and `primary_lane`.

**QDE / forensic document examination** - `/02_QDE/`

**Handwriting analysis / graphology** - `/03_HANDWRITING_ANALYSIS/`

**Happy Wealthy Mind / psychology / personal development** -
`/04_HAPPY_WEALTHY_MIND/`

**Bart stories or autobiographical material** - `/05_STORIES/`

### Level 3 --- Voice evidence

When stronger voice matching is needed, retrieve from:

-   `/01_VOICE/`
-   `/06_TRANSCRIPTS/`
-   `/07_PUBLISHED_CONTENT/`
-   `/08_CONTENT_EXAMPLES/approved/`

Transcripts are especially useful for spoken scripts because they
preserve natural Bart phrasing, rhythm, humor, analogies, and
directness.

### Level 4 --- Research

Use `/09_RESEARCH/` as evidence and background only.

**Research files are not evidence of Bart's opinion.**

External research should also be performed when the topic requires
current facts, verification, legal developments, scientific claims,
statistics, dates, court decisions, or other information that may have
changed.

------------------------------------------------------------------------

## 4. Content Lanes

Every item must be classified before drafting.

Recommended `primary_lane` values:

-   `FORENSIC_AUTHORITY`
-   `FORENSIC_CASE_HISTORY`
-   `FORENSIC_NEWS`
-   `HWA_AUTHORITY`
-   `HWM_PSYCHOLOGY`
-   `BART_REACTS`
-   `BART_PHILOSOPHY`
-   `BUSINESS_BRANDING`
-   `BART_SHOW`
-   `HISTORICAL_STORY`
-   `SEARCH_AEO`
-   `EDITORIAL_RESEARCH`
-   `PROMOTIONAL`
-   `ARCHIVE`

The lane determines research requirements, source folders, voice
strength, output type, and whether fresh Bart input is likely to be
necessary.

------------------------------------------------------------------------

## 5. Bart Perspective Decision

Every row must be assigned:

`fresh_bart_perspective = NO | MAYBE | YES`

### NO

Use when existing Bart source material clearly establishes his relevant
perspective.

Proceed without interrupting Bart.

### MAYBE

Search the Bart knowledge library first.

If sufficiently relevant Bart material is found, proceed and record the
source files used.

If the available material does not establish the required position
confidently, change status to `YES`.

### YES

Do not invent the missing perspective.

Generate **one concise question** designed to obtain the missing
information from Bart in approximately 20--60 seconds.

Store it in:

`bart_pov_question`

Set workflow status to:

`WAITING_FOR_BART`

After Bart responds:

1.  preserve the raw response/transcript;
2.  convert it into a clean perspective entry;
3.  identify appropriate topic tags;
4.  add the approved perspective to the appropriate GitHub perspective
    file or source document;
5.  update the spreadsheet;
6.  resume content production.

Bart should only be interrupted when his contribution materially
improves authenticity, expertise, opinion, story, interpretation, humor,
or authority.

------------------------------------------------------------------------

## 6. Retrieval Rules

Do not dump the entire repository into every prompt.

Retrieve based on:

`topic + primary_lane + content_vertical + voice_mode + output_type`

Prefer:

1.  exact topic matches;
2.  closely related Bart perspectives;
3.  approved Bart examples;
4.  relevant book passages;
5.  relevant transcripts;
6.  related published content;
7.  external research.

Record which Bart source files materially influenced the draft.

Suggested spreadsheet field:

`bart_pov_source`

Example:

``` text
QDE_BART_OPINIONS.md; QDE_CASE_HISTORIES.md#CASE-014
```

------------------------------------------------------------------------

## 7. Voice Modes

The system should not use one generic "Bart voice."

Recommended `voice_mode` values include:

### `BART_FORENSIC_EXPERT`

Precise, authoritative, evidence-driven, understandable to attorneys and
educated consumers. Avoid sensational claims. Separate observation,
inference, and conclusion.

### `BART_EDUCATOR`

Clear explanations, analogies, practical examples, direct language,
occasional humor.

### `BART_HWM`

Psychology, happiness, responsibility, money, relationships, behavior,
NLP, and life design. Logical and practical rather than generic
motivational language.

### `BART_REACTS`

Stronger personal perspective. Conversational, direct, willing to
challenge weak assumptions. Requires documented Bart perspective.

### `BART_STORYTELLER`

Narrative-first. Strong hook, tension, human detail, reveal, lesson.

### `BART_SHOW`

Conversational host/commentator voice suitable for direct-to-camera or
entertainment content.

### `NEUTRAL_RESEARCH`

Primarily factual. Bart perspective may appear separately if supported.

### `FACELESS_NARRATOR`

Efficient visual storytelling. Do not pretend the narrator is Bart
unless the script is explicitly designed as Bart narration and is
grounded in Bart material.

------------------------------------------------------------------------

## 8. QDE Special Rules

QDE must remain distinct from handwriting personality analysis.

For forensic/document topics, retrieve from `/02_QDE/`.

Never imply Bart personally worked a famous case unless
`QDE_CASE_HISTORIES.md` or another approved source explicitly confirms
involvement.

For famous cases, separate:

1.  verified case facts;
2.  findings of the actual examiners/courts;
3.  Bart's later professional commentary;
4.  general forensic lesson.

Do not turn Bart's retrospective commentary into evidence from the
original case.

Important QDE subjects to build into the perspective library include:

-   natural variation
-   simulation
-   tracing
-   disguise
-   questioned signatures
-   known exemplars
-   original versus copy
-   reproduction limitations
-   line quality
-   tremor
-   writing speed
-   elderly writers
-   illness/injury considerations
-   document alteration
-   anonymous writing
-   standards of conclusion
-   limitations of examination
-   attorney/client misconceptions
-   appropriate evidence submission
-   AI and automated signature analysis

------------------------------------------------------------------------

## 9. Handwriting Analysis Rules

Handwriting analysis/graphology and QDE are different disciplines.

Do not use graphology claims as forensic authorship conclusions.

Use Bart's handwriting-analysis books as primary Bart knowledge sources,
supplemented by:

-   `HWA_BART_PERSPECTIVE.md`
-   `HWA_UPDATED_POSITIONS.md`

If an older book position conflicts with a documented newer Bart
position, the newer approved position controls.

------------------------------------------------------------------------

## 10. Happy Wealthy Mind Rules

For HWM topics, retrieve from:

-   HWM books
-   `HWM_BART_PERSPECTIVES.md`
-   `HWM_CORE_PRINCIPLES.md`
-   relevant transcripts
-   approved published content

Distinguish:

-   published research;
-   Bart's interpretation of research;
-   Bart's personal philosophy;
-   personal stories;
-   NLP concepts;
-   clinical or medical claims.

Do not upgrade personal-development concepts into medical or scientific
conclusions.

------------------------------------------------------------------------

## 11. Research and Fact Checking

Fact-check before drafting whenever content contains:

-   historical events
-   crime
-   famous cases
-   court rulings
-   scientific studies
-   psychological research
-   statistics
-   medical claims
-   current events
-   laws
-   quotations
-   dates
-   attributed statements
-   auction values
-   biographies

Do not rely on a viral article or social post as the sole source when
primary or authoritative sources can be found.

Keep factual research separate from Bart perspective.

The workflow should be able to say internally:

``` text
FACT: Supported by source.
BART VIEW: Supported by Bart library.
SYNTHESIS: AI-created explanation based on those sources.
```

------------------------------------------------------------------------

## 12. Drafting Decision

Before generating content, determine the best primary output.

Recommended values:

-   `ARTICLE`
-   `FACELESS_VIDEO`
-   `BART_VIDEO`
-   `ARTICLE_AND_FACELESS_VIDEO`
-   `ARTICLE_AND_BART_VIDEO`
-   `SOCIAL_ONLY`
-   `RESEARCH_ONLY`
-   `ARCHIVE`

Do not automatically turn every idea into an article.

Choose based on:

-   search/AEO opportunity
-   Bart authority
-   visual potential
-   timeliness
-   originality
-   strength of Bart perspective
-   usefulness to target audience
-   duplication with existing content
-   potential for derivative assets

------------------------------------------------------------------------

## 13. Article Production

For an approved article:

1.  classify search intent;
2.  identify target query/topic;
3.  research and fact-check;
4.  retrieve Bart knowledge and perspective;
5.  identify the unique Bart angle;
6.  draft;
7.  validate factual claims;
8.  validate voice;
9.  create title/meta description;
10. identify internal-link opportunities;
11. create image brief and metadata;
12. create WordPress draft;
13. record URL/status in spreadsheet.

Avoid generic length targets. Use the shortest article that completely
answers the user's likely question while adding meaningful Bart
authority.

------------------------------------------------------------------------

## 14. Faceless Video Production

Faceless video is appropriate when the value primarily comes from:

-   story
-   documents
-   historical images
-   signatures
-   handwriting
-   visual evidence
-   timelines
-   public figures
-   locations
-   diagrams
-   research findings

The workflow should generate:

-   hook
-   concise script
-   scene/shot list
-   visual-source requirements
-   narration
-   on-screen text
-   caption
-   source list
-   CTA when appropriate

A faceless video may use Bart's perspective without Bart appearing on
camera only when that perspective is documented.

Do not create fake quotations or make synthetic narration imply Bart
personally said words he has not approved if presented as a direct
quote.

------------------------------------------------------------------------

## 15. Bart Video Production

Reserve Bart-recorded video for topics where Bart himself is the
product:

-   strong personal opinion
-   personal story
-   humor
-   reaction
-   controversial interpretation
-   professional nuance difficult to synthesize
-   brand-defining philosophy
-   direct audience relationship

Automation should minimize Bart's workload by preparing:

-   hook
-   three key points
-   supporting facts
-   optional punch line/analogy
-   CTA

Do not require Bart to record information that can be communicated just
as effectively through an article or faceless asset.

------------------------------------------------------------------------

## 16. Perspective Library Expansion Loop

The pipeline should continuously improve the repository.

When Bart provides a new answer:

``` text
RAW BART INPUT
        ↓
TRANSCRIBE
        ↓
EXTRACT POSITION / STORY / ANALOGY
        ↓
TAG TOPICS
        ↓
HUMAN APPROVAL WHEN REQUIRED
        ↓
SAVE TO CORRECT GITHUB FILE
        ↓
AVAILABLE TO FUTURE CONTENT
```

One Bart answer should become reusable intellectual property rather than
being consumed by one article.

------------------------------------------------------------------------

## 17. Required Assets to Assemble

### Critical

-   `BART_VOICE_AND_PERSPECTIVE_MASTER.md`
-   `BART_VOICE_GUIDE.md`
-   `CONTENT_LANE_RULES.md`
-   `FACT_CHECKING_AND_CITATION_RULES.md`
-   `BART_BIO_CREDENTIALS.md`
-   `QDE_BART_PERSPECTIVE.md`
-   `QDE_BART_OPINIONS.md`
-   `QDE_CASE_HISTORIES.md`
-   approved Bart writing examples

### High priority

-   QDE famous-case commentary
-   handwriting-analysis books
-   HWA perspective/update file
-   Happy Wealthy Mind books
-   HWM perspective file
-   Bart Show transcripts
-   best podcast/interview transcripts
-   published Bart articles
-   newsletters
-   personal story library

### Useful expansion

-   seminar transcripts
-   media appearances
-   direct-to-camera transcripts
-   social posts
-   business stories
-   comedy/storytelling examples
-   rejected AI examples showing what does not sound like Bart

------------------------------------------------------------------------

## 18. File Creation Standard

Markdown is preferred for the working knowledge repository.

Each perspective entry should ideally include metadata such as:

``` yaml
---
id: QDE-PERSPECTIVE-001
topic: natural variation
brand: Bart Baggett / QDE
source_type: book|transcript|bart_response|article|case
source_reference: filename or URL
confidence: high
approved: true
updated: 2026-09-23
---
```

Then:

``` markdown
## Position

Bart's documented position in clean prose.

## Supporting Experience

Relevant professional or personal context.

## Useful Language

Approved analogies, phrases, examples, or explanations.

## Boundaries

What this position does NOT establish.

## Source Notes

Where the position came from.
```

Do not mark inferred AI content as `approved: true`.

------------------------------------------------------------------------

## 19. Content Safety / Authenticity Gate

Before publishing, ask:

-   Did we invent anything Bart supposedly believes?
-   Did we imply Bart worked a case he did not work?
-   Did we confuse QDE with graphology?
-   Did we present an opinion as fact?
-   Did we present correlation as causation?
-   Did we use an outdated Bart position when a newer one exists?
-   Are important factual claims supported?
-   Does this actually add Bart's expertise or merely attach his name to
    generic AI writing?
-   Is the content useful enough to deserve publication?

If any answer creates uncertainty, route to review rather than publish
automatically.

------------------------------------------------------------------------

## 20. Core n8n Logic

``` text
NEW / SELECTED SPREADSHEET ROW
        ↓
VALIDATE CONTENT ID
        ↓
CLASSIFY LANE + VERTICAL
        ↓
CHECK DUPLICATION / EXISTING CONTENT
        ↓
DETERMINE BEST OUTPUT
        ↓
LOAD MASTER RULES
        ↓
RETRIEVE RELEVANT BRAND KNOWLEDGE
        ↓
RETRIEVE BART PERSPECTIVE
        ↓
IS BART PERSPECTIVE SUFFICIENT?
        │
        ├── YES → CONTINUE
        │
        └── NO → CREATE ONE BART QUESTION
                    ↓
              WAITING_FOR_BART
                    ↓
              INGEST RESPONSE
                    ↓
              UPDATE PERSPECTIVE LIBRARY
                    ↓
                  CONTINUE
        ↓
RESEARCH / FACT CHECK
        ↓
CREATE CONTENT BRIEF
        ↓
DRAFT PRIMARY ASSET
        ↓
FACT + VOICE + AUTHENTICITY QA
        ↓
CREATE DERIVATIVE ASSETS
        ↓
CREATE CMS / VIDEO / SOCIAL DRAFTS
        ↓
UPDATE MASTER SPREADSHEET
        ↓
HUMAN APPROVAL OR PUBLISHING WORKFLOW
```

------------------------------------------------------------------------

## 21. Governing Principle

The goal of **Content-Pipeline-All-Brands** is not to automate Bart.

It is to automate everything around Bart that does not require Bart.

Research, classification, retrieval, drafting, formatting, repurposing,
metadata, imagery planning, SEO/AEO preparation, and publishing
administration can be automated.

Bart should be brought into the workflow when his real experience,
judgment, opinion, story, humor, or interpretation is the scarce
ingredient.

Every time Bart supplies that ingredient, preserve it in the GitHub
perspective library so the pipeline becomes more capable without
becoming less authentic.
