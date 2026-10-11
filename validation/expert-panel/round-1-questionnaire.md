# AIDCF Expert Panel Round 1 Questionnaire

| Field | Value |
|---|---|
| Document ID | AIDCF-VAL-002-A |
| Title | AIDCF Expert Panel Round 1 Questionnaire |
| Version | 1.0 |
| Date | 2026-10-11 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |

Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-11 | First issue. |

This questionnaire implements section 8 of the protocol [AIDCF-VAL-002](AIDCF-VAL-002_Expert_Panel_Content_Validation_Protocol_v1.0.md). It is issued with three other files:

| File | What it is |
|---|---|
| `round-1-item-booklet.md` (AIDCF-VAL-002-B) | The 48 control items and 15 gate items you are asked to rate, reproduced from the AIDCF registries |
| `round-1-response-template.csv` | Your response file: one row per item |
| `participant-information-and-consent.md` (AIDCF-VAL-002-C) | Already signed before you receive this pack |

---

## 1. Instructions for panellists

1. **Your role is to challenge.** The panel exists to find controls and gates that are irrelevant, unclear, untestable or wrongly framed. A low rating with a reason is as useful as a high one. Please do not rate favourably out of courtesy.
2. **Rate alone.** Do not discuss items with other panellists or colleagues during the study. Questions about what an item means go to the facilitator; the question and answer will be shared with all panellists without your name.
3. **Rate the text as written.** Judge the objective, requirement, criteria and ceilings exactly as printed in the booklet, not what you think the author intended. If the text needs interpretation, that is a clarity issue: say so.
4. **Use `UNSURE` outside your competence.** If an item is outside your discipline and you cannot form a professional judgement, enter `UNSURE`. It is excluded from the statistics and is not counted as disagreement. Please still rate clarity where you can.
5. **Give reasons for low ratings.** For any rating of 1 or 2, write a short reason in `comment`. Where you think a claim type or gate role is wrong, enter your alternative in `proposedClaimType` or `proposedGateRole`.
6. **No confidential information.** Do not name or describe any identifiable site, organisation, customer, vendor contract or incident. Write from general professional experience. Content of this kind will be deleted.
7. **Time.** Round 1 is expected to take 3 to 4 hours. You may complete it over several sittings within the 14-day window. Save the file as `R1_<your panellist code>.csv` and return it to the facilitator only.
8. **Context documents.** You may consult the AIDCF repository, particularly AIDCF-002 (conceptual model), AIDCF-009 Part A (assessment methodology) and AIDCF-010 (critical gates), and the vocabularies in `registries/vocabularies/`. You are not expected to read them in full.

### Key AIDCF terms

| Term | Meaning |
|---|---|
| Claim type | What a control's conformance establishes. DESIGN: requirement and design are adequate. IMPLEMENTATION: as-built or configured state reconciles to approved design. OPERATION: operates as intended over a representative period and states. EFFECTIVENESS: achieves its objective under tested or observed adverse conditions. RESILIENCE: contains failure and supports recovery within tolerance. |
| Critical Gate | A non-compensating condition. If a gate FAILs or is UNKNOWN, the assurance decision is capped regardless of aggregate scores. |
| CRITICAL role | The control decides the gate: if it is NONCONFORMING or PARTIAL, the gate FAILs; if UNKNOWN or not assessed, the gate is UNKNOWN. |
| SUPPORTING role | The control contributes evidence to the gate; a NONCONFORMING SUPPORTING control requires a documented gate-level evaluation but does not by itself fail the gate. |
| FAIL ceiling | The best decision that may be issued for affected outcomes when the gate FAILs. |
| UNKNOWN ceiling | The best decision that may be issued when the gate's evidence is insufficient or a critical control's state is unknown. |
| Decision states | REASONABLY_ASSURED, CONDITIONALLY_ASSURED, LIMITED, NOT_ASSURED, INCONCLUSIVE (`registries/vocabularies/decision-states.csv`), as used in the ceilings. |

---

## 2. Rating scales and anchors

All rated columns take `1`, `2`, `3`, `4` or `UNSURE`. Cells pre-filled `NA` do not apply to that item; leave them as they are. Ratings of 3 and 4 count as agreement in the analysis, so choose between 2 and 3 deliberately.

### 2.1 Control items

**`relevance`**: Is this control relevant to assuring that an AI data-centre capability delivers its Service Outcomes?

| Rating | Anchor |
|---|---|
| 1 | Not relevant. The control does not bear on the capability's Service Outcomes or belongs in another discipline's framework. |
| 2 | Somewhat relevant. Related to the capability but marginal, duplicated elsewhere or too generic to add assurance value. |
| 3 | Quite relevant. Bears directly on the capability; minor scoping changes would improve it. |
| 4 | Highly relevant. An assessment of this capability would be materially incomplete without it. |

**`clarity`**: Is the objective and requirement stated clearly enough that two competent assessors would read it the same way?

| Rating | Anchor |
|---|---|
| 1 | Not clear. Key terms, scope or the required condition cannot be determined. |
| 2 | Somewhat clear. Intent is discernible but assessors would likely differ on scope or on what satisfies it. |
| 3 | Quite clear. Minor ambiguities that would not change an assessment outcome. |
| 4 | Very clear. Unambiguous scope, responsible role and required condition. |

**`testability`**: Can conformance be assessed from evidence, with a clear pass or fail condition, as written?

| Rating | Anchor |
|---|---|
| 1 | Not testable. No evidence could establish conformance, or there is no condition to test against. |
| 2 | Somewhat testable. Evidence exists in principle but the pass condition is vague, unbounded or needs a missing parameter. |
| 3 | Quite testable. A competent assessor could define the test with minor assumptions. |
| 4 | Highly testable. Evidence, sample population and pass condition follow directly from the text. |

**`claimTypeCorrect`**: Is the assigned claim type the right one for what the requirement asks the assessor to establish?

| Rating | Anchor |
|---|---|
| 1 | Strongly disagree. The requirement establishes a different claim type. Give your alternative in `proposedClaimType`. |
| 2 | Disagree. The claim type is arguable but another fits better. Give your alternative. |
| 3 | Agree. The claim type fits, with minor reservations. |
| 4 | Strongly agree. The claim type is clearly correct. |

**`gateRoleAppropriate`**: Is the gate role appropriate (CRITICAL where listed, SUPPORTING where listed, and no role where none is listed)?

| Rating | Anchor |
|---|---|
| 1 | Strongly disagree. The role is wrong in a way that would let a decisive weakness pass, or fail a gate on a non-decisive one. Give the alternative in `proposedGateRole`. |
| 2 | Disagree. At least one role should be changed, added or removed. Give the alternative. |
| 3 | Agree. The roles are appropriate, with minor reservations. |
| 4 | Strongly agree. The roles are clearly appropriate. |

### 2.2 Gate items

**`gateNecessity`**: Is a non-compensating gate for this condition necessary, so that a high aggregate score should not be able to offset its failure?

| Rating | Anchor |
|---|---|
| 1 | Not necessary. Ordinary scoring is sufficient; a gate would over-penalise. |
| 2 | Somewhat necessary. The condition matters but could be handled by a lower-weight mechanism or merged with another gate. |
| 3 | Quite necessary. Failure would usually be decisive. |
| 4 | Essential. A decision that ignored this condition would be unsafe or misleading. |

**`criteriaAdequacy`**: Are the gate's criteria, evidence and test methods adequate, together, to detect the decisive weakness the gate targets?

| Rating | Anchor |
|---|---|
| 1 | Inadequate. Material failure conditions would not be detected, or criteria test the wrong thing. |
| 2 | Partly adequate. At least one material condition is missing, or a criterion is not testable as written. |
| 3 | Adequate. Minor gaps or wording issues only. |
| 4 | Fully adequate. A competent assessor applying these criteria would detect the decisive weakness. |

**`failCeilingAppropriate`** and **`unknownCeilingAppropriate`**: Is the ceiling proportionate?

| Rating | Anchor |
|---|---|
| 1 | Not proportionate. The ceiling would mask a decisive weakness, or would penalise outcomes the gate does not affect. |
| 2 | Somewhat proportionate. Direction is right but scope or severity should change. |
| 3 | Proportionate, with minor reservations. |
| 4 | Fully proportionate. |

### 2.3 Free-text columns

| Column | Content |
|---|---|
| `proposedClaimType` | One of DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS, RESILIENCE; blank if no change |
| `proposedGateRole` | Semicolon-separated `CG-NN:CRITICAL`, `CG-NN:SUPPORTING` or `CG-NN:NONE` (remove a role); blank if no change |
| `comment` | Reasons, especially for ratings of 1 or 2; overlaps with other controls; conditions you think are missing from the catalogue or from a gate. Avoid commas only if your spreadsheet tool does not quote fields; the file is standard CSV. |

---

## 3. Item layout

### 3.1 Booklet

Each control item in the booklet shows: item number (A01 to A48) and control ID; domain and family; claim type and required assurance level; control type, profile tier and sufficiency floor; CRITICAL and SUPPORTING gates; objective; requirement.

Each gate item shows: gate ID and name; scope; evidence floor and required evidence classes; FAIL ceiling; UNKNOWN ceiling; approved not-applicable conditions; and a table of criteria with evidence and test method.

### 3.2 Response file

`round-1-response-template.csv` has 63 rows: 48 `CONTROL` rows in booklet order, then 15 `GATE` rows. Columns:

| Column | Filled by | CONTROL rows | GATE rows |
|---|---|---|---|
| `panelistCode` | You, from your invitation (for example P07) | Required | Required |
| `round` | Pre-filled | 1 | 1 |
| `itemType` | Pre-filled | CONTROL | GATE |
| `itemId` | Pre-filled | Control ID, matching the booklet heading | Gate ID |
| `itemTitle` | Pre-filled | Control title | Gate name |
| `relevance`, `clarity`, `testability`, `claimTypeCorrect`, `gateRoleAppropriate` | You | 1 to 4 or UNSURE | NA |
| `gateNecessity`, `criteriaAdequacy`, `failCeilingAppropriate`, `unknownCeilingAppropriate` | You | NA | 1 to 4 or UNSURE |
| `proposedClaimType`, `proposedGateRole` | You, optional | Optional | NA |
| `comment` | You, optional | Optional | Optional |

Do not add, delete, reorder or rename columns or rows, and do not change pre-filled cells. Save as UTF-8 CSV. If you use a spreadsheet application, check that it has not converted ratings to dates or added rows.

### 3.3 Worked example (illustrative only, not a real response)

```csv
panelistCode,round,itemType,itemId,itemTitle,relevance,clarity,testability,claimTypeCorrect,gateRoleAppropriate,gateNecessity,criteriaAdequacy,failCeilingAppropriate,unknownCeilingAppropriate,proposedClaimType,proposedGateRole,comment
P00,1,CONTROL,MCF-GOV-002,Decision Rights,4,3,2,3,4,NA,NA,NA,NA,,,"Testability: ""every decision in the sample population"" needs a defined sampling basis."
```

---

## 4. Before you return the file

- Every applicable rating cell holds 1, 2, 3, 4 or UNSURE.
- Every rating of 1 or 2 has a reason in `comment`.
- No comment identifies a site, organisation, customer, vendor or incident.
- `panelistCode` is filled on every row.
- File saved as `R1_<panellist code>.csv` and sent to the facilitator only.
