# Work-Order-Content-Workflow

## Work Order

**Workflow:** `Content-Pipeline-All-Brands`

**Governing specification:** `Content-Pipeline-All-Brands-v2.md`

**Canonical source:** Google Sheet ID
`1lA4-OB3SM_lOssthD5XyJldwlJz10uJt`, starting tab GID `546834024`.

The Google Sheet is the **Content Control Center, editorial queue, and
production system of record**. GitHub is the **Bart knowledge, voice,
perspective, rules, books, transcripts, cases, and source-content
library**.

## Required Architecture

``` text
GOOGLE SHEET
eligible content row
    ↓
VALIDATE content_id + required fields
    ↓
CLASSIFY lane + vertical + voice + best output
    ↓
CHECK DUPLICATION / EXISTING CONTENT
    ↓
LOAD MASTER RULES FROM GITHUB
    ↓
RETRIEVE RELEVANT BART KNOWLEDGE + PERSPECTIVE
    ↓
BART POV SUFFICIENT?
    ├── YES → continue
    └── NO → create ONE 20–60 second Bart question
              → status WAITING_FOR_BART
              → stop that item
              → ingest Bart response
              → preserve response in GitHub perspective library
              → resume
    ↓
RESEARCH + FACT CHECK
    ↓
CREATE CONTENT BRIEF
    ↓
DRAFT PRIMARY ASSET
    ↓
FACT + VOICE + AUTHENTICITY QA
    ↓
CREATE DERIVATIVES
    ↓
WORDPRESS / VIDEO / SOCIAL DRAFT
    ↓
WRITE STATUS + ASSET IDS + URLS BACK TO GOOGLE SHEET
```

## Google Sheet Responsibilities

The Sheet determines **what enters production** and stores its state.
Preserve the original topic/note/source data.

Core fields should include:

`content_id`, `topic`, `original_note`, `source_url`, `primary_lane`,
`content_vertical`, `voice_mode`, `bart_authority_level`,
`bart_pov_source`, `fresh_bart_perspective`, `bart_pov_question`,
`fact_check_required`, `primary_output`, `seo_aeo_intent`,
`visual_asset_potential`, `workflow_status`, `article_status`,
`video_status`, `social_status`, `publishing_destination`,
`published_url`, `review_notes`.

Derivative IDs inherit the permanent parent ID:

``` text
TR-047-ARTICLE
TR-047-VIDEO
TR-047-SHORT
TR-047-SOCIAL
```

`TR` means **To Record**, preserving lineage from the original backlog.

## GitHub Responsibilities

Expected root:

`/bart-knowledge/`

Priority sources:

``` text
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
books/
HWA_BART_PERSPECTIVE.md
HWA_UPDATED_POSITIONS.md

/04_HAPPY_WEALTHY_MIND/
books/
HWM_BART_PERSPECTIVES.md
HWM_CORE_PRINCIPLES.md

/05_STORIES/
/06_TRANSCRIPTS/
/07_PUBLISHED_CONTENT/
/08_CONTENT_EXAMPLES/
/09_RESEARCH/
```

Do not fail the whole workflow because an optional future file is
missing. Log the missing resource and decide whether approved remaining
sources are sufficient.

## Retrieval Rules

Retrieve the **smallest relevant source set**, based on:

`topic + primary_lane + content_vertical + voice_mode + output_type`

Order:

1.  governing rules;
2.  relevant vertical knowledge;
3.  exact/related Bart perspective;
4.  approved Bart writing or transcripts;
5.  internal research;
6.  external/current research when required.

Record the Bart source files materially used in `bart_pov_source`.

Do not load the entire repository into every prompt.

## Bart Perspective Gate

Use:

`fresh_bart_perspective = NO | MAYBE | YES`

**NO:** Existing Bart material clearly establishes the relevant
position. Continue.

**MAYBE:** Search the Bart library first. If sufficient evidence exists,
continue. Otherwise change to `YES`.

**YES:** Do not invent Bart's view. Generate one concise question Bart
can normally answer in 20--60 seconds and set
`workflow_status = WAITING_FOR_BART`.

After Bart responds, preserve the raw response, extract the reusable
perspective, tag it, place it in the appropriate GitHub source, update
the Sheet, and resume.

## Editorial Lanes

Use these core lane values:

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

Primary outputs:

-   `ARTICLE`
-   `FACELESS_VIDEO`
-   `BART_VIDEO`
-   `ARTICLE_AND_FACELESS_VIDEO`
-   `ARTICLE_AND_BART_VIDEO`
-   `SOCIAL_ONLY`
-   `RESEARCH_ONLY`
-   `ARCHIVE`

Do not assume every row deserves an article or video.

## Research Gate

Fact-check before final drafting for historical events, crime, famous
cases, court rulings, laws, scientific studies, psychological research,
statistics, medical claims, quotations, dates, biographies, auction
values, or current events.

Keep separate:

``` text
FACT = independently supported
BART VIEW = documented in Bart library
AI SYNTHESIS = AI organization/explanation
```

## QDE Boundary

QDE and handwriting personality analysis are separate disciplines.

For QDE, use `/02_QDE/`. Never infer Bart worked a famous case. Separate
the original examiner/court findings from Bart's later commentary. Never
convert graphology claims into forensic authorship conclusions.

## Production Requirements

**ARTICLE:** research brief, search/AEO question, unique Bart angle,
draft, title, meta description, internal links, image brief/metadata,
sources, QA result, WordPress draft/status.

**FACELESS VIDEO:** hook, concise narration, shot list, visual-source
requirements, on-screen text, caption, sources, CTA when appropriate.

**BART VIDEO:** low-friction recording brief containing hook, three
talking points, essential facts, optional analogy/punch line, and CTA.
Do not create a new long-form recording bottleneck.

## Quality Gate

Before READY_FOR_REVIEW, verify:

-   no invented Bart opinion, quote, story, experience, or case
    involvement;
-   QDE and graphology remain distinct;
-   important factual claims are supported;
-   opinion is distinguishable from fact;
-   current information is checked where required;
-   selected voice matches the lane;
-   content adds genuine Bart expertise rather than generic AI prose;
-   meaningful duplication has been checked;
-   output fits its destination.

Uncertainty routes to human review, not automatic publication.

## Workflow Status Values

``` text
NEW
TRIAGE
RESEARCH_REQUIRED
RETRIEVING_BART_POV
WAITING_FOR_BART
READY_FOR_BRIEF
DRAFTING
QA
NEEDS_REVISION
READY_FOR_REVIEW
APPROVED
SCHEDULED
PUBLISHED
ARCHIVED
ERROR
```

Every execution must leave the Sheet with a meaningful status, including
failures.

## Idempotency and Logging

Use `content_id + derivative_type` as the durable asset key. Before
creating an external asset, check whether it already exists.

Log:

-   `content_id`
-   execution timestamp
-   lane
-   vertical
-   voice mode
-   primary output
-   Bart source files used
-   research sources used
-   Bart POV decision
-   generated asset IDs
-   destination URLs
-   QA result
-   error/review notes

A rerun must not create duplicate articles, videos, or social assets.

## Build Order

**Phase 1 --- Editorial Intelligence:** Sheet intake → validation →
classification → GitHub retrieval → Bart POV gate → research brief →
Sheet update. No auto-publishing.

**Phase 2 --- Article Production:** SEO/AEO brief → article → fact/voice
QA → WordPress draft → Sheet update.

**Phase 3 --- Video Production:** faceless-video scripts/shot lists +
Bart-video recording briefs.

**Phase 4 --- Derivatives:** social, Shorts/Reels, newsletters,
cross-platform reuse.

**Phase 5 --- Perspective Learning Loop:** ingest new Bart responses →
extract reusable perspective → approved GitHub update → reuse in future
content.

## Definition of Done --- Initial Build

The initial workflow is production-ready when it can:

1.  read an eligible row from the canonical Google Sheet;
2.  preserve its permanent `content_id`;
3.  classify lane, vertical, voice, and best output;
4.  retrieve appropriate GitHub instructions and Bart material;
5.  determine whether fresh Bart POV is required;
6.  stop and generate one Bart question when necessary;
7.  research/fact-check when appropriate;
8.  produce a structured content brief;
9.  write decisions and status back to the same Sheet;
10. avoid duplicate processing;
11. log errors without corrupting source data.

Only after this works reliably should downstream automatic publishing be
enabled.

## Governing Principle

**The Google Sheet decides what enters production. GitHub supplies
Bart's intellectual property. n8n coordinates the work. AI assists with
research and creation. Bart is interrupted only when Bart is genuinely
the missing ingredient.**
