# AIDCF-VAL-002 Expert Panel Content Validation Protocol

| Field | Value |
|---|---|
| Document ID | AIDCF-VAL-002 |
| Title | Expert Panel (Modified Delphi) Content Validation Protocol |
| Version | 1.0 |
| Date | 2026-10-11 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |

Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-11 | First issue. |

> **Status of the study.** This protocol and its kit are ready for use. No panel has been convened, no participant has been recruited and no ratings exist. Nothing in this repository should be read as a result of this protocol until signed round records and an analysis report are published under `validation/expert-panel/`.

---

## 1. Purpose and scope

### 1.1 Purpose

This protocol defines how a multidisciplinary panel of independent practitioners judges the **content validity** of a stratified sample of AIDCF controls and of all fifteen Critical Gates, using a modified Delphi method with anonymous ratings and controlled feedback.

It produces evidence for two research questions in the repository [README](../../README.md#research-questions):

| Research question | What this protocol contributes | What it cannot show |
|---|---|---|
| RQ3 Control-universe validity | Item-level judgements of whether sampled controls are relevant to AI data-centre assurance, clearly stated, testable as written, assigned the right claim type and the right gate role; free-text identification of padding, compression, overlap and omission | Whether the full 360-control catalogue is complete; only the sampled 48 are rated, and omission is detected only through free text |
| RQ8 Critical-gate effectiveness | Judgements of whether each gate is necessary, whether its criteria are adequate to detect the decisive weakness it targets, and whether its FAIL and UNKNOWN ceilings are proportionate | Whether gates prevent masking in real assessments; that requires pilot evidence and backtesting, not opinion |

### 1.2 Claim boundary

Content validity is expert judgement about what an instrument contains. A high content validity index means a qualified panel agreed that the content is relevant, clear and correctly framed. It does not demonstrate that AIDCF controls are effective, that assessments using them are reliable (RQ10) or that scores are valid (RQ9). Panel outcomes are not endorsement, accreditation or certification, and must not be presented as such.

### 1.3 Objects in scope

| Object | Source | Count |
|---|---|---|
| Control items | [`control-sample.csv`](control-sample.csv), drawn from `registries/controls/controls.csv` by `tools/build_sample.py` | 48 |
| Gate items | [`gate-sample.csv`](gate-sample.csv), all gates in `registries/gates/critical-gates.csv` with criteria from `registries/gates/critical-gate-criteria.csv` | 15 |

The item text rated by the panel is the generated [`round-1-item-booklet.md`](round-1-item-booklet.md) (AIDCF-VAL-002-B), which reproduces registry text verbatim. The registry release under study (release 3.1, registry version recorded in `controls.csv`) is frozen for the duration of the study; see EPV-REQ-004.

---

## 2. References

### 2.1 Repository references

| Reference | Use in this protocol |
|---|---|
| `README.md` (Research Questions; How to review AIDCF; Independent review needed) | RQ3 and RQ8; disposition vocabulary; disciplines sought |
| `CONTRIBUTING.md` sections 11 and 12 | Disposition values ACCEPT, PARTIAL, REJECT, DEFER; conflict-of-interest categories |
| `registries/vocabularies/claim-types.csv` | Claim types DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS, RESILIENCE |
| `registries/vocabularies/gate-results.csv` | Meaning of FAIL and UNKNOWN for a gate |
| `registries/controls/gate-mappings.csv` | CRITICAL and SUPPORTING gate roles |
| AIDCF-002, AIDCF-009 Part A, AIDCF-010 | Conceptual model, assessment methodology and gate doctrine that panellists may consult |

### 2.2 Methodological sources

Only sources the author is certain of are cited, at publication level.

- Lynn, M. R. (1986). Determination and quantification of content validity. *Nursing Research*, 35(6), 382–385.
- Polit, D. F., & Beck, C. T. (2006). The content validity index: are you sure you know what's being reported? Critique and recommendations. *Research in Nursing & Health*, 29(5), 489–497.
- Polit, D. F., Beck, C. T., & Owen, S. V. (2007). Is the CVI an acceptable indicator of content validity? Appraisal and recommendations. *Research in Nursing & Health*, 30(4), 459–467.
- Hasson, F., Keeney, S., & McKenna, H. (2000). Research guidelines for the Delphi survey technique. *Journal of Advanced Nursing*, 32(4), 1008–1015.

---

## 3. Terms

| Term | Meaning in this protocol |
|---|---|
| Item | One control or one gate presented for rating |
| Dimension | One rated property of an item (for example relevance) |
| Item-dimension | The unit of analysis: one dimension of one item |
| Valid rating | A rating of 1, 2, 3 or 4. `UNSURE`, `NA` and blank are recorded but excluded from N |
| I-CVI | Item-level content validity index: proportion of valid ratings that are 3 or 4 |
| Pc | Probability of chance agreement on the I-CVI, assuming each rating is equally likely to be agreeing or not |
| k\* | Modified kappa: I-CVI adjusted for chance agreement |
| S-CVI/Ave | Scale-level content validity index, averaging method: mean I-CVI across items for one dimension |
| S-CVI/UA | Scale-level index, universal agreement method: share of items with I-CVI = 1.00 |
| Facilitator | The person who runs rounds, holds the participant key and prepares feedback |
| Panellist code | Pseudonym (P01 to P12) assigned by the facilitator; the only identifier in response files |

---

## 4. Roles and independence

| Role | Responsibility | Independence requirement |
|---|---|---|
| Study sponsor | Approves the protocol, appoints the facilitator, owns data-protection and ethics obligations, signs off publication | Named organisation or individual; recorded in the study record |
| Facilitator | Recruits, issues invitations and consent, assigns panellist codes, distributes rounds, sends reminders, prepares controlled feedback, holds the participant key | Should not be the AIDCF author. If no other facilitator is available, the author may facilitate only with the analysis independently re-run (below) and the arrangement disclosed in the report |
| Independent analyst | Re-runs `tools/analyse_round.py` on the anonymised response files for every round and confirms the item results match | Must not be the AIDCF author or a panellist |
| AIDCF author | Answers factual questions about item meaning through the facilitator (answers circulated to all panellists); proposes dispositions after the final round | Does not see identified responses; does not contact panellists about their ratings |
| Panellists | Rate items independently, declare conflicts, keep round materials confidential until publication | At least two independent of the author (section 5.3) |

---

## 5. Panel composition and recruitment

### 5.1 Size

The panel has **8 to 12** panellists at the start of Round 1. Fewer than 8 consenting panellists means the study does not start. If retention falls below 6 valid ratings for an item, that item is reported as `LOW_N` and no consensus is claimed for it (section 8.4).

### 5.2 Disciplines

Each discipline below is covered by at least one panellist. One panellist may cover at most two disciplines and is counted against their primary discipline for recruitment.

| Code | Discipline | Typical roles |
|---|---|---|
| D1 | Electrical power | Electrical design or commissioning engineer; critical-power operations lead; protection and controls engineer |
| D2 | Mechanical and liquid cooling | Mechanical design engineer; liquid-cooling and CDU/TCS specialist; thermal commissioning lead |
| D3 | HPC and AI compute | HPC or AI cluster architect; accelerator platform reliability engineer |
| D4 | Storage | Storage architect or reliability engineer for AI training or inference data paths |
| D5 | Network fabric | Data-centre or AI back-end fabric architect (RDMA, lossless Ethernet, InfiniBand or equivalent) |
| D6 | Data-centre operations and reliability | Critical-facilities operations manager; site reliability or incident lead; maintenance and change authority |
| D7 | OT and ICS security | OT security engineer or architect for BMS, EPMS, PLC and SCADA environments |
| D8 | Assurance and audit | Internal or external auditor; assurance-methods lead; second-line risk practitioner with infrastructure scope |

Statistics and measurement review of the analysis (README, Independent review needed) is provided by the independent analyst, not by a panellist.

### 5.3 Independence

At least **two** panellists must be independent of the author: no current or prior employment relationship, reporting line, co-authorship of AIDCF material, commercial arrangement or personal relationship with the author, and no role in AIDCF's development. Recruitment should aim for a majority of independent panellists. The independence status of each panellist is recorded by the facilitator and reported only in aggregate (for example "9 of 11 independent").

### 5.4 Inclusion criteria

A candidate is eligible when all of the following hold:

1. At least **seven years** of professional practice in the discipline claimed, of which at least **three years** were on data-centre, HPC or comparable mission-critical infrastructure.
2. Current or recent (within the last three years) role with design, operational, security or assurance accountability in that discipline, not solely sales or marketing.
3. Able to read technical English and to commit to all rounds (estimated 3 to 4 hours for Round 1, 1 to 2 hours for each later round).
4. Willing to sign the consent form (`participant-information-and-consent.md`, AIDCF-VAL-002-C) and complete the conflict declaration.

Professional registration (for example chartered engineer status) or a recognised audit qualification is recorded where held but is not required, so that experienced practitioners in hyperscale operators, where such registration is uncommon, are not excluded.

### 5.5 Exclusion criteria

- Co-author or developer of AIDCF.
- A conflict that the facilitator and sponsor judge would prevent independent rating and that cannot be managed by disclosure (for example a commercial interest in AIDCF adoption).
- Unable to rate without disclosing confidential information about an identifiable site (section 12.6).

### 5.6 Conflict declaration

Before Round 1 each panellist completes the declaration in AIDCF-VAL-002-C, using the categories in `CONTRIBUTING.md` section 12: prior authorship or design involvement; employment or commercial interest; vendor relationships; assurance-provider role; pilot sponsor relationship; any other interest affecting impartiality. A declared conflict does not automatically exclude a panellist; it is recorded, considered against section 5.5, and reported in aggregate.

### 5.7 Recruitment route

Candidates are identified through professional networks, professional bodies and public expressions of interest in reviewing AIDCF. Invitations are sent individually by the facilitator. Recruitment records list the discipline, eligibility evidence summary, independence status and conflict outcome for each candidate; they are held by the facilitator and not published.

---

## 6. Item sample

### 6.1 Control sample

`tools/build_sample.py` selects 48 of the 360 candidate controls deterministically. No pseudo-random generator is used: every control is ranked by the SHA-256 digest of `AIDCF-VAL-002-2026-10-11:<controlId>`, lowest first, which gives the same order on every platform. Four rules are applied in sequence:

| Rule | Selection | Purpose |
|---|---|---|
| R1 Gate floor | For each of CG-01 to CG-10 and CG-13 to CG-15, add CRITICAL-mapped controls by rank until at least 2 CRITICAL controls for that gate are held | Every control-bearing gate is represented by controls that decide it |
| R2 Claim-type floor | For each claim type, add controls by rank until at least 4 are held, preferring domains below the cap of 4 | All five claim types are rated |
| R3 Domain floor | For each of the 15 domains, add controls by rank until at least 3 are held, preferring a claim type the domain does not yet have | Every domain is represented |
| R4 Critical-weighted fill | Fill to 48 from domains below the cap of 4, preferring the least-represented domain, then a CRITICAL mapping, then rank | Over-weight CRITICAL controls |

CG-11 (Evidence sufficiency) and CG-12 (Critical UNKNOWN) have no control mappings in `gate-mappings.csv`; they are evaluated from evidence and UNKNOWN records, so they appear as gate items only.

`build_sample.py --check` fails if the outputs on disk differ from a fresh generation, if any floor is not met, if the share of sampled controls holding a CRITICAL mapping does not exceed the population share, or if `controls.csv` and `gate-mappings.csv` disagree on CRITICAL roles. At issue, CRITICAL-holding controls are 29% of the population and 54% of the sample; each control's `selectionReason` records the rule that selected it.

R2 and R3 deliberately do not prefer CRITICAL controls, so that SUPPORTING-only and unmapped controls are present and the panel can say whether any of them should carry a CRITICAL role.

### 6.2 Gate sample

All 15 gates are rated. `gate-sample.csv` records each gate's name, criteria count and the number of CRITICAL controls in the registry and in the sample.

### 6.3 Changing the sample

The sample may be regenerated only before Round 1 is issued. Any change to the seed or rules is a protocol revision recorded in the revision history. Results from different samples are never pooled.

---

## 7. Method

### 7.1 Overview

| Stage | Activity | Output |
|---|---|---|
| Preparation | Freeze registry version; run `build_sample.py --check`; pre-test the questionnaire with one or two practitioners who are not panellists, for comprehension and time only (their ratings are discarded) | Frozen item set; timing estimate; wording fixes to instructions only |
| Recruitment | Invite, screen, obtain consent and conflict declarations, assign codes | Panel of 8 to 12 |
| Round 1 | All 63 items, all dimensions, free text | Round 1 responses; item results; collated comments |
| Feedback 1 | Controlled feedback pack per panellist (section 7.4) | Round 2 pack |
| Round 2 | Items without consensus, plus any variant items (section 7.5) | Round 2 responses and results |
| Round 3 (conditional) | Only if the stopping rule (section 8.5) is not met after Round 2 | Round 3 responses and results |
| Close | Final analysis, independent re-run, disposition proposals, anonymised report | Analysis report; disposition records |

Each round has a response window of 14 calendar days, with reminders on day 7 and day 12, followed by up to 14 days for analysis and feedback preparation.

### 7.2 Anonymity

The design is quasi-anonymous: the facilitator knows who the panellists are; panellists do not know each other's identities or individual ratings, and the author does not see identified responses. Response files carry only the panellist code. Free text is screened by the facilitator for identifying details before circulation (section 12.4).

### 7.3 Independence of ratings

Panellists rate alone and must not discuss items with other panellists during the study. Questions about meaning are sent to the facilitator; the facilitator obtains a factual answer from the author where needed and circulates the question and answer to all panellists without attribution.

### 7.4 Controlled feedback

After Rounds 1 and 2, each continuing panellist receives, for every item-dimension carried forward:

- group N, median, interquartile range and I-CVI from `tools/analyse_round.py`;
- the panellist's own previous rating (individualised pack; never other panellists' individual ratings);
- an anonymised, de-duplicated summary of the free-text reasons given, presented without attribution and without indication of discipline where that could identify a panellist;
- any factual clarification issued under section 7.3.

Feedback reports group statistics neutrally. It does not indicate a preferred answer and does not include the author's view of the item.

### 7.5 Carrying items forward and variant items

- An item-dimension that reached `CONSENSUS_ACCEPT` or `CONSENSUS_REJECT` (section 8.4) is not re-rated.
- An item-dimension with `NO_CONSENSUS` or `LOW_N` is re-rated in the next round.
- Where Round 1 comments converge on a specific wording, claim-type or gate-role change, the facilitator may present a **variant item** alongside the original in Round 2, with an identifier of the form `<controlId>-V1`. The variant is a proposal to the panel, not a registry change. Variant item rows use the same response layout and are analysed in the same way.
- The registry is not edited during the study (EPV-REQ-004).

### 7.6 Attrition

A panellist who does not respond within a round's window is treated as withdrawn from that round; they are invited to the next round only if they have not withdrawn from the study. Attrition by round is reported. Ratings already given by a panellist who withdraws are handled as set out in section 12.5.

---

## 8. Rating items and analysis

### 8.1 Control item dimensions

| Column | Question | Scale |
|---|---|---|
| `relevance` | Is this control relevant to assuring that an AI data-centre capability delivers its Service Outcomes? | 4-point (anchors in AIDCF-VAL-002-A) |
| `clarity` | Is the objective and requirement stated clearly and unambiguously enough that two competent assessors would read it the same way? | 4-point |
| `testability` | Can conformance with the requirement be assessed from evidence, with a clear pass or fail condition, as written? | 4-point |
| `claimTypeCorrect` | Is the assigned claim type the right one for what the requirement asks the assessor to establish? | 4-point agreement; alternative in `proposedClaimType` |
| `gateRoleAppropriate` | Is the control's gate role appropriate: CRITICAL where listed, SUPPORTING where listed, and no role where none is listed? | 4-point agreement; alternative in `proposedGateRole` |
| `comment` | Reasons, especially for ratings of 1 or 2; overlap, omission or padding observed | Free text |

`proposedClaimType` takes one value from `registries/vocabularies/claim-types.csv`. `proposedGateRole` takes the form `CG-NN:CRITICAL`, `CG-NN:SUPPORTING` or `CG-NN:NONE`, semicolon-separated.

### 8.2 Gate item dimensions

| Column | Question | Scale |
|---|---|---|
| `gateNecessity` | Is a non-compensating gate for this condition necessary, so that a high aggregate score should not be able to offset its failure? | 4-point |
| `criteriaAdequacy` | Taken together, are the gate's criteria adequate to detect the decisive weakness the gate targets, with evidence and test methods that would expose it? | 4-point |
| `failCeilingAppropriate` | Is the FAIL ceiling proportionate: neither so weak that a decisive weakness is masked nor so broad that unaffected outcomes are penalised? | 4-point |
| `unknownCeilingAppropriate` | Is the UNKNOWN ceiling proportionate to the risk of acting without the gate evidence? | 4-point |
| `comment` | Reasons; missing criteria; criteria that belong elsewhere | Free text |

### 8.3 Item-level statistics

For each item-dimension, with N valid ratings of which A are 3 or 4:

```text
I-CVI = A / N
Pc    = C(N, A) × 0.5^N
k*    = (I-CVI − Pc) / (1 − Pc)
```

Median, first and third quartiles (inclusive method) and IQR are reported alongside. These follow the formulation in Polit, Beck and Owen (2007).

Acceptance thresholds:

| Statistic | Threshold | Basis |
|---|---|---|
| I-CVI, N ≤ 5 | 1.00 | Lynn (1986) |
| I-CVI, N ≥ 6 | ≥ 0.78, compared after rounding to two decimals | Lynn (1986); Polit, Beck and Owen (2007) |
| k\* | > 0.74 excellent; 0.60 to 0.74 good; 0.40 to 0.59 fair; < 0.40 poor | Polit, Beck and Owen (2007) |
| S-CVI/Ave | ≥ 0.90 | Polit and Beck (2006) |

Minimum agreeing panellists at the I-CVI threshold for the planned panel sizes (computed by the formulas above):

| Valid ratings N | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|
| Minimum A | 5 | 6 | 7 | 7 | 8 | 9 | 10 |
| I-CVI | 0.83 | 0.86 | 0.88 | 0.78 | 0.80 | 0.82 | 0.83 |
| k\* | 0.82 | 0.85 | 0.87 | 0.76 | 0.79 | 0.81 | 0.83 |

At every planned size, an I-CVI that meets the threshold also gives k\* in the excellent band.

### 8.4 Consensus definition

Each item-dimension is classified per round:

| Classification | Rule |
|---|---|
| `CONSENSUS_ACCEPT` | I-CVI meets the threshold for its N, k\* > 0.74, and IQR ≤ 1 |
| `CONSENSUS_REJECT` | I-CVI < 0.50 and IQR ≤ 1 (the panel agrees the item is deficient on that dimension) |
| `NO_CONSENSUS` | Any other result |
| `LOW_N` flag | N < 6; no consensus is claimed for the item-dimension, whatever its classification |

`UNSURE` is the correct response where an item falls outside the panellist's competence; it is excluded from N, not counted as disagreement. An item is rated by every panellist, so each item-dimension is expected to have enough valid ratings despite discipline spread; `LOW_N` items are reported separately.

### 8.5 Stopping rule

The study stops after the first round in which any of the following holds:

1. every item-dimension is `CONSENSUS_ACCEPT` or `CONSENSUS_REJECT`;
2. for every item-dimension still `NO_CONSENSUS`, the I-CVI changed by less than 0.15 from the previous round (stability: further rounds are unlikely to move opinion);
3. Round 3 has been completed.

Item-dimensions still `NO_CONSENSUS` at stop are reported as unresolved with their final statistics and comment themes; they are not forced into either category.

### 8.6 Scale-level statistics

S-CVI/Ave and S-CVI/UA are computed per dimension and item type (for example CONTROL relevance across the 48 control items). The headline content-validity statistic for RQ3 is CONTROL `relevance` S-CVI/Ave; for RQ8 it is GATE `gateNecessity` and `criteriaAdequacy` S-CVI/Ave. All scale results are reported, not only the headline ones.

### 8.7 Free text

Comments are coded by the facilitator and the independent analyst separately into the review categories in the README (TECH, ASSUR, SEM, SAFE, ED, IMPL, PILOT) and, for RQ3, into overlap, omission, padding and compression. Differences in coding are resolved by discussion and the number resolved is reported. Proposed claim types and gate roles are tabulated per item.

### 8.8 Tooling

`tools/analyse_round.py` implements sections 8.3 to 8.6 and validates response files (rejects values other than 1 to 4, `NA`, `UNSURE` or blank; rejects duplicate panellist-item rows; rejects mixed rounds). `--self-test` checks the arithmetic against hand-computed values on a fixture marked SYNTHETIC. The independent analyst re-runs the script and compares outputs byte for byte; any difference is investigated before results are circulated.

---

## 9. Requirements

| ID | Requirement |
|---|---|
| EPV-REQ-001 | The study shall not start with fewer than 8 consenting panellists, or without every discipline D1 to D8 covered, or with fewer than two panellists independent of the author. |
| EPV-REQ-002 | Every panellist shall have signed consent and a completed conflict declaration on file with the facilitator before receiving Round 1 materials. |
| EPV-REQ-003 | `tools/build_sample.py --check` shall pass, and its output files shall be identical to those issued, before Round 1 is issued. |
| EPV-REQ-004 | The registry files from which items were drawn shall not be changed for the purpose of the study between Round 1 issue and the final analysis; the registry version rated shall be recorded in the analysis report. |
| EPV-REQ-005 | Response files shall identify panellists only by panellist code; the key linking codes to identities shall be held only by the facilitator, separately from response files. |
| EPV-REQ-006 | Controlled feedback shall contain only group statistics, the recipient's own prior ratings, anonymised comment summaries and circulated clarifications. |
| EPV-REQ-007 | Each round's item results shall be re-run by the independent analyst and match before feedback is issued. |
| EPV-REQ-008 | Consensus, stopping and threshold rules shall be applied as written in section 8; any deviation shall be recorded with reason in the analysis report. |
| EPV-REQ-009 | Every flagged or `CONSENSUS_REJECT` item-dimension, and every converging proposal from free text, shall receive a disposition record (section 10). |
| EPV-REQ-010 | Published results shall contain no panellist identity, no individual rating set and no information identifying a site, organisation or customer (section 11). |
| EPV-REQ-011 | No result shall be described as endorsement, accreditation or certification of AIDCF. |

---

## 10. Disposition of results into AIDCF

### 10.1 From result to disposition

After the final round, the author proposes a disposition for each item-dimension requiring one (EPV-REQ-009), using the values in `CONTRIBUTING.md` section 11. Default proposals:

| Panel result | Default proposed disposition | Typical change |
|---|---|---|
| `CONSENSUS_REJECT` on relevance | ACCEPT the finding | Withdraw, merge or re-scope the control through an amendment |
| `CONSENSUS_REJECT` or flagged on clarity or testability | ACCEPT or PARTIAL | Reword requirement; add measurable condition or parameter |
| Flagged on claim type with a converging `proposedClaimType` | ACCEPT or PARTIAL | Change claim type and, where needed, required assurance level |
| Flagged on gate role with a converging `proposedGateRole` | ACCEPT, PARTIAL or DEFER | Amend `gate-mappings.csv`; DEFER where the change needs pilot or backtest evidence first |
| Gate necessity or criteria adequacy flagged | PARTIAL or DEFER | Add, split or tighten criteria; reconsider gate scope |
| FAIL or UNKNOWN ceiling flagged | PARTIAL or DEFER | Revise ceiling text in `critical-gates.csv`; DEFER where backtesting (RQ8) should decide |
| `NO_CONSENSUS` at stop | DEFER unless comments identify a clear defect | Carry to the next review cycle or pilot |
| Free-text omission theme | ACCEPT, PARTIAL, REJECT or DEFER | Candidate new control or criterion; assessed against RQ3 balance |

REJECT is used where the author disagrees with the panel; the rationale must engage with the panel's stated reasons and is published with the result.

### 10.2 Disposition record

Each record holds: disposition ID; item and dimension; round statistics (N, I-CVI, k\*, median, IQR, classification); comment theme summary; disposition value; rationale; resulting change (amendment ID and files changed) or reason for no change; closure evidence; disposition author; independent reviewer of the disposition. Author action does not equal independent reviewer acceptance (`CONTRIBUTING.md` section 11): a disposition is closed only when a reviewer who is not the author has checked that the change, or the rationale for no change, addresses the panel result.

Records are intended to sit in `validation/reviewer-dispositions/`, which is maintained separately from this kit.

### 10.3 Changes to the framework

Accepted changes follow the normal amendment and release process. Any changed control or gate is identified in the release notes as revised following expert-panel validation, citing the analysis report. Changed items have not been validated by the panel in their changed form; the report says so.

---

## 11. Publication of results

The analysis report, published under `validation/expert-panel/` after sponsor sign-off, contains:

- panel composition in aggregate (number per discipline, number independent, conflicts declared by category, attrition per round);
- item-level results for every item-dimension in every round (the `analyse_round.py` output without panellist codes);
- scale-level results;
- coded comment themes and tabulated proposals, with quotations only where screened and non-identifying;
- deviations from this protocol;
- disposition records or links to them;
- a statement of the claim boundary in section 1.2.

Individual response files are not published. Discipline-level breakdowns are published only where every cell has at least three panellists.

---

## 12. Ethics and data protection

### 12.1 Ethics review

The study collects professional opinion from adults about a technical framework and involves no vulnerable participants, no deception and no sensitive personal data by design. It still involves human participants and personal data. **If the study is run through or in association with a university or other research institution, institutional ethics approval may be required before recruitment begins**, and that institution's procedures then take precedence over this section wherever they are stricter. The sponsor records whether review was sought and the outcome.

### 12.2 Participant information and consent

Each candidate receives AIDCF-VAL-002-C before consenting. Consent is written and covers: purpose; what participation involves and time required; voluntary participation; anonymity arrangements; data held, by whom and for how long; publication; right to withdraw; prohibition on disclosing confidential site information; contacts. The template must be reviewed by the sponsor's legal adviser and data-protection adviser before use.

### 12.3 Personal data

Personal data is limited to: name, contact details, discipline, eligibility evidence summary, independence status, conflict declaration and the panellist-code key. These are held by the facilitator only, in access-controlled storage separate from response files. Response files and analysis outputs contain panellist codes only.

### 12.4 Anonymity in free text

The facilitator screens free text before circulation or publication and removes or generalises names, employers, sites, vendors where the reference would identify the panellist or a site, and distinctive incident details.

### 12.5 Right to withdraw

Panellists may withdraw at any time without giving a reason. On withdrawal, the panellist chooses whether ratings already given are retained or deleted. Deletion is possible until the analysis of the round concerned has been circulated as feedback; after that point, ratings already aggregated into circulated or published statistics cannot be separated, and this is stated in the participant information.

### 12.6 No confidential site information

Panellists are asked to rate on the basis of professional judgement and must not provide confidential information about any identifiable site, organisation, customer or incident. The facilitator deletes any such content received and informs the panellist.

### 12.7 Data retention

| Data | Holder | Retention |
|---|---|---|
| Participant key and contact details | Facilitator | Until the final analysis report is published, then destroyed, unless the panellist consents to be contacted for a later review cycle |
| Consent forms and conflict declarations | Sponsor | For the period set by the sponsor's records policy, as advised by its data-protection adviser |
| Anonymised response files | Sponsor | For the period set by the sponsor, sufficient to allow re-analysis and audit of published results |
| Published anonymised results | Repository | Indefinitely, as part of the repository record |

Retention periods must be confirmed by the sponsor's data-protection adviser and stated in the participant information before recruitment.

---

## 13. Threats to validity

| Threat | Description | Mitigation |
|---|---|---|
| Selection bias | Panellists recruited through the author's network may share the author's assumptions | At least two, aiming for a majority, independent panellists; public call for expressions of interest; independence reported |
| Acquiescence and authority bias | Panellists may rate favourably out of courtesy to the author or because AIDCF appears authoritative | Facilitator not the author where possible; instructions state the panel's role is to challenge; anonymity |
| Conformity pressure | Controlled feedback may pull ratings towards the median without new reasoning | Feedback carries reasons, not only statistics; panellists may hold their rating; stability criterion stops rounds rather than pursuing consensus |
| Competence mismatch | Panellists rate items outside their discipline | `UNSURE` option excluded from N; `LOW_N` flag; discipline coverage requirement |
| Sample representativeness | 48 of 360 controls; the sample over-weights CRITICAL controls | Documented, deterministic rules; selection reasons published; results generalised to the catalogue only with that caveat |
| Item-order and fatigue effects | About 300 ratings in Round 1; later items may be rated less carefully | Pre-test timing; completion over multiple sittings allowed; fatigue checked by comparing comment rates across the booklet |
| Dimension confounding | Clarity problems depress relevance and testability ratings | Separate dimensions; comments coded to identify the driver |
| Chance agreement | High I-CVI with small N | Modified kappa reported; N-dependent thresholds |
| Attrition bias | Dissenting panellists may drop out | Attrition reported per round with the earlier ratings of those who left, in aggregate |
| Construct limits | Content validity is not effectiveness | Claim boundary in section 1.2; RQ8 effectiveness addressed by pilots and backtesting |
| Analyst error | Script or data-handling error | Self-test; independent re-run; response-file validation |
| Author control of dispositions | The author decides what changes | Independent review of dispositions; REJECT rationale published |

---

## 14. Kit contents

| File | Document ID | Purpose |
|---|---|---|
| `AIDCF-VAL-002_Expert_Panel_Content_Validation_Protocol_v1.0.md` | AIDCF-VAL-002 | This protocol |
| `round-1-questionnaire.md` | AIDCF-VAL-002-A | Instructions, scales and anchors, item layout |
| `round-1-item-booklet.md` | AIDCF-VAL-002-B | Generated item text |
| `participant-information-and-consent.md` | AIDCF-VAL-002-C | Participant information sheet, consent form and conflict declaration template |
| `control-sample.csv`, `gate-sample.csv` | n/a | Generated item sample |
| `round-1-response-template.csv` | n/a | Generated response file, one row per item |
| `tools/build_sample.py` | n/a | Sample, template and booklet generator (`--check`) |
| `tools/analyse_round.py` | n/a | Round analysis (`--self-test`) |
| `tools/test-fixtures/SYNTHETIC_round-1-responses.csv` | n/a | Synthetic self-test data; not panel data |
