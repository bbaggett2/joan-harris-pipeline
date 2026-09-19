# QDE Forensic Brand — YouTube Thumbnail SOP

**Version 3 · 2026-07-13 · Brand: QDE / @TheHandwritingExpert**
**Supersedes:** v1 and v2 (2026-05-22)
**Changes in v3:** Reference library moved from Betty to Salvatore. QDE-specific generation script added. Mandatory reference review step added before Gemini generation. Ownership transferred to Salvatore.

This SOP defines the thumbnail look for the **QDE forensic brand only**. It is deliberately separate from the Handwriting University (HU), Bart Allan Baggett, and Bart Show brands so the four channels never blur together. When you make a QDE thumbnail, follow this document — not the HU style guide.

---

## 1. What the QDE brand is

QDE = **Questioned Document Examination** — the forensic side of the business: signature forgery, disputed wills and contracts, document examination, and expert-witness testimony in court. The viewer is usually someone with a real legal problem (a forged signature, a fake lease, a contested estate) or an attorney serving that person. The corporate entity is called Handwriting Experts Inc and handles $400,000 per year in legal related consulting contracts.

A QDE thumbnail should feel like an **investigative news segment** — serious, credible, forensic. It must never feel like a personality quiz. The HU channel covers personality and "what your handwriting says about you"; QDE never uses that framing, and never uses the words "graphology" or "graphologist." When clients are investing $100,000 to win a lawsuit and $10,000 of that is for the most credible expert witness, the expert's public persona is an important factor in the hiring decision.

---

## 2. Visual identity

### Color palette

| Role | Color | Use |
|---|---|---|
| Deep navy panel | `#10142E` (near-black navy; range `#0E1228`–`#1E2240`) | The signature QDE headline block / background |
| White | `#FFFFFF` | Primary headline text |
| Accent gold | `#FFE455` | Highlights the 1–2 key words of the headline |
| Alarm red | `#B00708` | Sparingly — stamps and alarm words only ("FAKE", "FORGED") |

*(Colors sampled directly from the approved reference thumbnails.)*

### Typography

Heavy, bold, slightly condensed sans-serif. Title Case for the headline (one alarm word may be ALL CAPS). White base text, with the 1–2 most emotional words set in gold; red only for a stamp or alarm word. Apply a subtle dark drop shadow or outline so text stays legible over photography. Type is large — the headline fills its panel and is readable on a phone at a glance.

| Font | Size | Role |
|---|---|---|
| `Anton` | 75–120pt | Primary thumbnail headline |

### Layout — pick one pattern

A. **Navy panel + photo split** — a solid deep-navy block on one side holds the headline; a forensic photo fills the other side. This is the most common and most on-brand pattern. **The dividing edge of the navy panel must be cut on a diagonal slant** (a clear, noticeable tilt — roughly 75° or 100°, never 90°). Never a straight vertical or horizontal block edge.

B. **Full-bleed photo + overlay** — a darkened forensic photo with the headline overlaid directly, key words in gold, optional small navy bar for a subtitle line.

C. **Document hero** — a close-up of a signature, contract, or piece of evidence is the star, with a navy headline panel beside it. Bart optional.

### Imagery

Forensic props carry the brand: signatures, police crime scenes, forensic crime labs, ESDA machines, UV light on documents, contracts, wills, magnifying glass, microscope, "FAKE"/"FORGED" stamps, courtrooms, evidence. Use real photographs, high contrast, darkened wherever text sits. Bart is **optional** — many of the strongest QDE thumbnails have no Bart at all. When he appears, he is professional (suit or business casual, serious or confident) and reads as the expert, not the subject; show his full head and never crop the face. **His facial expression must always be engaged — determined, intense, angry, or inquisitive — and never bored, blank, or flat.** When possible use a frame from the video so that the journey from click to the talking head video is congruent with the thumbnail. This is more effective if Bart is wearing a suit in the video.

### Logo

**No channel logo and no watermark on QDE thumbnails.** Keep them clean. (Confirmed by Bart, May 2026.)

---

## 3. Headline rules

- **Ask a question.** Curiosity-gap headlines win — "Did They Forge Your Lease?", "How Long Does It Take?"
- **Second person.** Speak to the viewer's problem: "your signature", "your lease", "your contract".
- **Highlight 1–2 key words in gold** — the emotional hooks ("Signature", "Forged").
- **Short** — 3 to 8 words, readable in under two seconds on a phone.
- **Hide the answer.** Pose the question; never give away the payoff.
- **No episode numbers or internal codes** ("20.", "Q36", "0764") — those are internal reference only.
- **No insider jargon.** Spell it out — "Handwriting Expert" or "Document Examiner", never "FDE". Don't assume the viewer knows forensic acronyms.
- **No credentials or taglines.** A thumbnail provokes a question; it is not a business card. No "Certified", no "30 years", no "hire me" energy.
- **Never "graphology" / "graphologist."** That is HU/personality territory and is off-brand for QDE.

---

## 4. Do / Don't

**Do:** navy + gold palette; question headlines in the viewer's POV; forensic props; clean and uncluttered (about three elements maximum); match the reference library.

**Don't:** use the HU look — cinematic study background, a single magnified letter inside a red teacher's circle, antique-parchment highlight block, collegiate serif type — that is the Handwriting University brand. Also avoid episode numbers, credentials, graphology language, cropped faces, and flat colorless backgrounds.

---

## 5. Production

### Step 1 — Review the reference library BEFORE writing any Gemini prompt

⛔ **This step is mandatory. Do not open Gemini or write a generation prompt until it is complete.**

Open and study the approved thumbnail reference library:
- **Folder:** `Salvadore - art department/4-2026 best thumbnails QDE samples approved/`
- **PDF summary:** `Salvadore - art department/4-2026 approved thumbnails QDE – YouTube Thumbnail.pdf`

Review at minimum 8–10 approved thumbnails. Before proceeding, confirm you can answer:
- Which layout pattern (A, B, or C) is most common in the approved set?
- Where does the diagonal slant typically fall?
- How much of the frame does the navy panel occupy?
- How large is the headline text relative to the image?
- What types of forensic props appear most frequently?

Your Gemini prompt must produce a result that **looks like it belongs in that folder**. If you cannot say that confidently after generation, discard and regenerate.

### Step 2 — Generate using the QDE-specific script

- **QDE generation script:** `Salvadore - art department/Generate_QDE_Forensic_Thumbnails_v3.sh`
- Run on Bart's Mac via Desktop Commander (Gemini blocked in sandbox — 403 error)
- Use `--aspect 16:9`
- Headshot reference (when Bart is included): `skills_to_install/youtube-thumbnail/headshots/`
- Pass **no logo** reference image

> Do NOT use `skills_to_install/youtube-thumbnail/scripts/generate_thumbnail.py` for QDE thumbnails. That is the HU script. The QDE script is `Generate_QDE_Forensic_Thumbnails_v3.sh`.

### Step 3 — Prompt skeleton

Build your Gemini prompt using this structure:
1. Navy panel + forensic photo split (diagonal slant edge — never 90°)
2. Question headline, 3–8 words, Anton font, white base + 1–2 gold key words
3. One clear forensic prop (signature, contract, stamp, courtroom, evidence)
4. Bart optional — if included: full head, professional, expression engaged, natural skin tone
5. Explicitly state: "no logo, no watermark, no channel branding"
6. Confirm output matches the reference library before accepting

### Step 4 — Naming, versions, and filing

- Every QDE video has a permanent starts with a Q or a  VID from the master worksheet
- Thumbnail filename **must lead with the VID-number** — e.g. `VID-Q40-hold-up-in-court-v1.png`
- Q-number is in the filename only — **never visibly on the thumbnail image**
- Version as `v1`/`v2`/`v3` — **never use "final" in a filename**
- Once Bart approves: add a copy to `Salvadore - art department/4-2026 best thumbnails QDE samples approved/` so the reference library grows

### Step 5 — Tracking

Master worksheet: **AEO Video Publishing Master Worksheet**, tab **"ALL WIP Sheet"**

| Column | Field | Action |
|---|---|---|
| A | Q-number | Reference only |
| B | Title | Reference only |
| P | Thumbnail Uploaded? | Update when thumbnail goes live on YouTube |
| Q | Description Uploaded? | Update when description is live |
| S | YouTube publish date | Update when video goes public |

---

## 6. Pre-publish checklist

- [ ] Reference library reviewed (minimum 8–10 approved thumbnails studied before prompting)
- [ ] 16:9, at least 1280×720, under 2 MB
- [ ] Navy + gold palette — reads as QDE, not HU
- [ ] Headline is a question, second person, 1–2 gold key words, 8 words or fewer
- [ ] Anton font, large enough to read on a phone at a glance
- [ ] No episode number, no FDE jargon, no credentials, no "graphology"
- [ ] No logo and no watermark
- [ ] Navy panel edge is cut on a diagonal slant — never a straight 90° block
- [ ] If Bart is shown: full head visible, natural skin tone, professional wardrobe, expression engaged (never bored)
- [ ] Filename leads with Q-number (e.g. `Q40-title-v1.png`) — Q-number not visible on image
- [ ] Approved copy added to reference library folder
- [ ] Master worksheet column P updated
- [ ] Sits comfortably alongside the reference library

---

*Maintained by Salvatore (Art Department). Update as `v3`, `v4`… when the brand evolves.*
*Companion docs: `Salvator_AI_Graphics_SOP_v1.md` · `Video_Publishing_Workflow_HU_and_QDE_v1.md` · `Betty_SOP_YouTube_Publishing_QDE.md`*
