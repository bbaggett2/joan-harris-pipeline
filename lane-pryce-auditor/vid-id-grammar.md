# VID ID grammar

The VID ID is the join key across Drive, the sheets, ClickUp, and the platforms.
It is a convention that lives in editors' heads, so it degrades. Roughly 12 of 20
files in the July 2026 audit matched a strict `VID-\d+`. A tolerant parser gets
to about 17. The remaining three must be quarantined, never guessed.

## The parser

Apply in order. Stop at the first match.

1. **Normalize the string.** Uppercase. Replace any run of whitespace or
   underscore between `VID` and the number with a single hyphen. Strip a leading
   `GD-` or other prefix only if `VID` appears later in the token.
2. **Match** `VID-([0-9]{2,4})([A-Za-z]{0,2})` — digits, then an optional short
   alpha suffix.
3. **Match the alphanumeric series** `VID-(GD[0-9]{2}|Q[0-9]{1,2}[a-z]?|[0-9]{4}-[A-Z]{2})`.
4. **Zero-pad** a 3-digit numeric ID to 4 digits **only if** the padded form
   exists in a canonical sheet and the unpadded form does not.
5. If nothing matches, or if step 4 finds both forms, **quarantine**.

## Real failures observed (use these as your test set)

| Filename as delivered | Strict match | Correct ID | Why it fails |
|---|---|---|---|
| `VID-0740_TT_metricool.mp4` | ✅ | VID-0740 | — |
| `VID 0790 Blunt V3-ZU-approved.mp4` | ❌ | VID-0790 | space, not hyphen |
| `VID 0795VB -trigger neuropathways...` | ❌ | VID-0795b | space + uppercase suffix; sheet uses `0795b` |
| `Vid-106-Vanity-Short-V1-Zu-approved` | ❌ | VID-0106 | lowercase; 3-digit vs sheet's 4-digit |
| `VID-GD04-Socially Selective-ZU-V4.mp4` | ❌ | VID-GD04 | alphanumeric series |
| `GD-GD03-Talkative-V2-ZU-mobile short.mp4` | ❌ | **quarantine** | no `VID` token at all |
| `VID-40V7forensicreport hold up in courtz-V2-approved.mp4` | partial | VID-Q40 V7 | strict regex captures `VID-40`, which is wrong; sheet row is `VID-Q40 V7` |
| `VID-0771 Screw your wife...approvedmp4` | ✅ | VID-0771a | sheet row and ClickUp list are `0771a`; also missing the `.` before `mp4` |

## Known collisions — escalate, never resolve

These are real and cannot be fixed by parsing. Report them; Bart decides.

- **VID-0827** matches **two** ClickUp lists: "Concentration" and
  "Concentration (HU)".
- **VID-0816** — the file `VID-0816 GOTTMAN Study V2-ZU.mp4` is actually
  **VID-0215** per the workflow sheet's own note, and collides with the genuine
  VID-0816 ("Socially Selective Listener"). A separate list, VID-0758, is the
  real "closed minded" video.
- **VID-0739 / VID-0740** exist twice in the workflow sheet — once hyphenated,
  once as `VID_0739` / `VID_0740` with underscores, with different stages.
- **VID-0757** appears twice in the HU folder as two different cuts, and the
  sheet notes the same source clip is also `VID-0765a`.
- **VID-GD04** has both a `V3` and a `V4` file sitting in ready-to-publish with
  no current-version marker.

The sheet itself carries pending renames: `VIF_0793` → `VID-0793`,
`VD 0764` → `VID-0764`, `VID-0802 How to Spot liar` → `VID-0107`. Until those
files are renamed, match on the sheet's `Delivery File Name` column as a fallback
before quarantining.

## The quarantine rule

On a parse failure or an ambiguous match:

1. Move the file to a `_needs-VID` subfolder in the same brand folder. **Move
   only — never rename, never delete.**
2. Post one Slack line naming the file and the reason.
3. Record `QUARANTINE` in the ledger with the original filename verbatim.

Never route a file to a list you are not certain of. A wrong route publishes the
wrong video under the wrong title on the wrong brand's channel, and for the QDE
forensic brand that is an expert-witness credibility problem, not a content
problem.

## The upstream fix

Track filename gate pass rate weekly. If it stays below roughly 90%, the answer
is not a cleverer parser — it is one line in the editor ticket template:

> The delivered filename must begin `VID-####` exactly: uppercase VID, one
> hyphen, four digits, then anything you like. Example:
> `VID-0827 Concentration V3-ZU-approved.mp4`
