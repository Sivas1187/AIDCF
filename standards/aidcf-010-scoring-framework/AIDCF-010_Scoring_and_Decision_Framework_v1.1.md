> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-010_Scoring_and_Decision_Framework_v1.1.pdf](AIDCF-010_Scoring_and_Decision_Framework_v1.1.pdf).

**AIDCF**

**AI Data Centre Facilities Assurance Framework**

**SCORING & DECISION FRAMEWORK**

**Version 1.1**

**A constitutional, evidence-aware and gate-controlled standard for synthesising assessment results and issuing bounded assurance decisions**

Artifact ID: AIDCF-010  
Requirement prefix: SDF  
Status: Draft for controlled review  
Author: Siva Sethumadhavan  
Depends on: AIDCF-006, AIDCF-007A, AIDCF-008 and AIDCF-009

**Evidence supports assurance. Scores summarise. Gates constrain. Accountable authority decides.**

# Document control

| **Field** | **Value** |
|---|---|
| Title | AIDCF Scoring and Decision Framework |
| Artifact ID | AIDCF-010 (requirement prefix SDF) |
| Version | 1.1 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Depends on | AIDCF-006 Assurance Principles; AIDCF-007A Canonical Master Control Registry; AIDCF-008 Evidence Model; AIDCF-009 Assessment Methodology |
| Downstream | AIDCF-011 Assurance Program Framework; AIDCF-012 Reporting and Assurance Statement Standard; AIDCF-014/AIDCF-016 machine-executable models; AIDCF-017 Capability Assurance Maturity Model |
| Purpose | Translate AIDCF-009 Control Assessments into transparent control, family, domain and capability scores; evaluate the fifteen critical gates; and derive the maximum permissible decision state for an accountable human Assurance Decision, without letting scores override evidence, UNKNOWN or gates. |
| Inputs | 360 controls, 90 families, 15 domains (AIDCF-007A); Evidence Assessments and UNKNOWN Records (AIDCF-008); Control Assessments, Findings and scenarios (AIDCF-009). |
| Outputs | Control results per claim type; scores with coverage and bands; Gate Results; UNKNOWN register with severity; Score Snapshot; Decision Recommendation (maximum permissible decision state with controlling reasons); input to the Assurance Decision. |
| Machine registers | registries/gates/critical-gates.csv; registries/gates/critical-gate-criteria.csv |
| Boundary | Not certification, guarantee, legal opinion, safety approval or engineering approval. |
| Safety | No score or gate may encourage unsafe testing, evidence suppression or uncontrolled operation. |

## Revision history

| **Version** | **Date** | **Summary** |
|---|---|---|
| 1.0 | — | Controlled-review draft. |
| 1.1 | 2026-10-10 | Method made executable: canonical result states and values; D1–D5 redefined as claim types with mandatory-claim-type rule; evidence multiplier removed (insufficient evidence → UNKNOWN); recalibrated bands with coverage and UNKNOWN withholding; EQI defined; fifteen distinct gate specifications with criteria, roll-up and ceilings; UNKNOWN severity; deterministic decision derivation; family profiles replaced by one rule and justified domain exceptions; consecutive SDF-REQ IDs; mapping annex. |

# Executive thesis

**AIDCF scoring supports synthesis, prioritisation, comparison and trend analysis. It never creates assurance. Every score remains bounded by capability, outcomes, scope, operating state, period, evidence, coverage, gates, UNKNOWN, Findings, scenarios, review and decision authority.**

The method is deterministic up to the point of human judgment. Given the same Control Assessments, Gate Results and UNKNOWN Records, any conforming implementation shall compute the same scores, the same bands or withholdings, the same Gate Results and the same maximum permissible decision state. The accountable decision owner then decides, at or below that state, and records why.

Normative keywords (shall, should, may, can) follow ISO/IEC Directives Part 2 usage. Terms follow the canonical assurance chain (AIDCF-002): this framework operates at steps 12 (Control Assessment), 13 (Finding / UNKNOWN Record), 14 (Gate Result), 15 (Score Snapshot and Decision Recommendation) and 16 (Assurance Decision).

# Part I - Constitutional doctrine

**Scoring is subordinate to AIDCF assurance principles (AIDCF-006 APS-036, APS-037, APS-045).**

| **Concept** | **Rule** |
|---|---|
| Score is not assurance | Numbers cannot issue or upgrade a decision. |
| Evidence first | Insufficient evidence produces UNKNOWN, never a reduced score. |
| Gate dominance | FAIL and UNKNOWN Gate Results constrain decisions regardless of scores. |
| Capability first | The primary subject is a defined Capability Instance and its Service Outcomes. |
| Claim-type separation | DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS and RESILIENCE results remain distinct and are never blended into one number. |
| No hidden imputation | UNKNOWN and NOT_ASSESSED are not zero, average or pass. |
| No double counting | A Finding changes the underlying result or a gate; there is no second deduction. |
| Human authority | Automation calculates and recommends; accountable authority decides. |
| Bounded use | Scope, period, state, profile, coverage and confidence are disclosed. |
| Versioning | Rules and input snapshots are immutable and superseded explicitly. |

**SDF-REQ-001** No score, band or index shall raise a Gate Result or the maximum permissible decision state; scores may only lower the ceiling through the band step of the decision derivation (Part XII).

**SDF-REQ-002** An implementation shall produce identical scores, bands, Gate Results and maximum permissible decision state from identical inputs and rule versions.

# Part II - Scoring objects

**Every score is a versioned object with lineage.**

| **Object** | **Rule** |
|---|---|
| ControlResult | One control, one claim type, one scope (and state where state-scoped): a canonical result code (Part III). |
| ControlScore | The score value of a ControlResult, or no value. |
| FamilyScore / DomainScore | Mean of scored ControlResults within the family or domain for one claim type, with coverage and band. |
| CapabilityAssuranceIndex (CAI) | Domain-weighted summary for one Capability Instance and one claim type (Part VI). |
| Supporting views | The same arithmetic over declared control subsets: Resilience view (RES domain plus all RESILIENCE claims); Dependency view (DEP domain); Digital authority view (SEC domain plus SUP-06); Operational readiness view (OPS domain); Resource view (ENV domain). |
| Evidence profile summary | Distribution of quality bands Q0–Q5, sufficiency S0–S5, UNKNOWN types and severities; not a numeric index. |
| GateResult | Independent non-compensating result for one gate (Part VIII). |
| DecisionRecommendation | Maximum permissible decision state with controlling reasons and prohibited higher states. |
| AssuranceDecision | Accountable bounded decision with lifecycle state. |
| ScoreSnapshot | Immutable inputs, rule versions, outputs and lineage. |

# Part III - Control result states and score values

**UNKNOWN is neither success nor failure.**

A control result is recorded per control, per claim type and per scope. The canonical result codes and score values are:

| **Code** | **Meaning** | **Score value** |
|---|---|---|
| CONFORMING | All assessment criteria met for the claim type, evidence at or above the Evidence Requirement Profile floors | 100 |
| PARTIAL | Some criteria met; each specific deficiency recorded as a Finding | 50 |
| NONCONFORMING | Criteria materially not met, or a safeguard demonstrated ineffective | 0 |
| UNKNOWN | Result cannot be determined (evidence below floor, conflict, inaccessible, stale, and similar) | No value; excluded from the mean; counted in coverage and in the UNKNOWN register |
| NOT_APPLICABLE | Approved non-applicability with rationale and approver | Excluded |
| NOT_ASSESSED | In scope but not yet assessed | Excluded from the mean; counted as a coverage gap |

**SDF-REQ-003** Every ControlResult shall carry exactly one canonical result code. A result of CONFORMING, PARTIAL or NONCONFORMING shall reference an EvidenceAssessment meeting the profile's sufficiency floor, except that NONCONFORMING may rest on evidence below the floor where that evidence affirmatively demonstrates a criterion is not met (AIDCF-008 §25).

**SDF-REQ-004** Where evidence is insufficient for a determination, the result shall be UNKNOWN with an UNKNOWN Record (type U1–U10, severity US1–US5); it shall not be recorded as PARTIAL or NONCONFORMING to obtain a score.

**SDF-REQ-005** A ControlAssessment whose reliance is suspended (change, expiry, incident) shall take lifecycle state SUSPENDED and its result shall revert to UNKNOWN until reassessed.

## Combining scopes and states

A control assessed over several scopes (sites, halls, clusters, population strata) or several operating states is combined for a parent scope by the least-favourable rule: NONCONFORMING if any part is NONCONFORMING; otherwise UNKNOWN if any part is UNKNOWN or NOT_ASSESSED; otherwise PARTIAL if any part is PARTIAL; otherwise CONFORMING. NOT_APPLICABLE parts are ignored. Per-scope results remain visible.

**SDF-REQ-006** Results for a parent scope shall be derived by the least-favourable rule and shall never be averaged across scopes or states.

## Implementation Maturity (diagnostic only)

Implementation Maturity describes how established a control's practice is. It is a diagnostic for improvement planning under AIDCF-017 and is never a control result, never scored here and never an input to a gate or decision.

| **Level** | **Name** | **Indicative description** |
|---|---|---|
| IM0 | Absent | No practice exists. |
| IM1 | Initial | Ad hoc, person-dependent practice. |
| IM2 | Defined | Documented and approved design. |
| IM3 | Implemented | Implemented as designed in the assessed scope. |
| IM4 | Operating | Operated consistently over a representative period. |
| IM5 | Optimised | Measured, reviewed and improved from evidence. |

**SDF-REQ-007** Implementation Maturity shall be reported separately from control results and shall not be converted into a result code or score.

## Legacy mapping (v1.0 states)

| **v1.0 state (v1.0 value)** | **v1.1 result code (value)** | **Note** |
|---|---|---|
| NOT IMPLEMENTED (0) | NONCONFORMING (0) | Indicative maturity IM0/IM1. |
| PARTIAL (25) | PARTIAL (50) | Value recalibrated; Findings mandatory. |
| IMPLEMENTED (60) | CONFORMING (100) | Valid only for DESIGN or IMPLEMENTATION claims; indicative maturity IM3. |
| OPERATING EFFECTIVELY (85) | CONFORMING (100) | For OPERATION or EFFECTIVENESS claims; indicative maturity IM4. |
| STRONGLY EFFECTIVE (100) | CONFORMING (100) | For OPERATION or EFFECTIVENESS claims; any "strength" beyond conformance is maturity (IM5), not a result. |
| INEFFECTIVE (0) | NONCONFORMING (0) | Finding and gate linkage retained. |
| N/A | NOT_APPLICABLE | Approved rationale required. |
| NOT ASSESSED | NOT_ASSESSED | Coverage gap. |
| UNKNOWN | UNKNOWN | UNKNOWN Record with type and severity now required. |
| SUSPENDED | Lifecycle state SUSPENDED; result UNKNOWN | Not a result code. |

# Part IV - Assurance dimensions D1–D5 as claim types

**A control is scored once per claim type it is assessed for.**

The five assurance dimensions are the five canonical claim types. A ControlResult always names one.

| **Dimension** | **Claim type** | **What the result asserts** | **Minimum Assurance Level** |
|---|---|---|---|
| D1 | DESIGN | The requirement and design are adequate. | AL2 |
| D2 | IMPLEMENTATION | The as-built or configured state reconciles to the approved design. | AL3 |
| D3 | OPERATION | The control operates as intended over a representative period and the declared operating states. | AL4 |
| D4 | EFFECTIVENESS | The control achieves its objective under tested or observed adverse conditions. | AL5 |
| D5 | RESILIENCE | The control contains failure and supports recovery within tolerance. | AL5 |

## Mandatory claim types for an assessment

The assessment plan declares a target Assurance Level T (AL2 to AL6; AIDCF-011). Each control record in the AIDCF-007A registry carries a requiredAssuranceLevel r (AL2 to AL5) and an evidenceProfile.claimType p consistent with r. The claim types mandatory for that control in that assessment are determined by L = min(T, r), with AL6 treated as AL5 for this purpose (AL6 adds continuing currency obligations under AIDCF-011, not deeper claim types):

| **L** | **Mandatory claim types** |
|---|---|
| AL2 | DESIGN |
| AL3 | DESIGN, IMPLEMENTATION |
| AL4 | DESIGN, IMPLEMENTATION, OPERATION |
| AL5 | DESIGN, IMPLEMENTATION, OPERATION and p (EFFECTIVENESS or RESILIENCE, whichever the profile names) |

Claim types above L are optional. An optional claim type that is assessed is scored and reported; one that is not assessed is out of scope and is not a coverage gap. A capability profile may raise r for named controls before results are known; it may not lower it. AL0 (Discovery) and AL1 (Readiness) engagements may produce ControlResults and scores for planning but do not run the decision derivation and issue no Assurance Decision.

Worked illustration: in an AL4 (operational) assessment, MCF-POW-011 Runtime and Derating with r = AL5 and p = EFFECTIVENESS is assessed for D1–D3; its EFFECTIVENESS claim is optional. In an AL5 assessment it is assessed for D1–D4, while MCF-RES-014 Recovery Sequencing with p = RESILIENCE is assessed for D1, D2, D3 and D5.

**SDF-REQ-008** The mandatory claim types of each in-scope control shall be determined from the target Assurance Level and the control's registry requiredAssuranceLevel and claimType using the table above, and shall be frozen in the assessment plan before results are recorded.

**SDF-REQ-009** Scores shall be computed and reported separately for each claim type; no rule shall combine results of different claim types into a single score.

**SDF-REQ-010** A Gate Result shall state the deepest claim type at which its CRITICAL controls were evaluated (for example "CG-05 PASS at OPERATION"), and the Assurance Decision shall not assert a claim deeper than the shallowest such depth among the gates it relies on.

# Part V - Evidence overlay and Evidence Quality Index

**Evidence quality remains visible and does not manufacture precision.**

Evidence is rated per AIDCF-008 on six dimensions, each 0–5: P Provenance, F Fitness (relevance), C Coverage, R Reliability, T Timeliness (currentness), I Integrity. Sufficiency is S0–S5 and quality bands Q0–Q5.

Evidence affects results in exactly one way: if the package for a claim does not meet the Evidence Requirement Profile's quality floor (per dimension), class requirements or sufficiency floor, the result is UNKNOWN. The v1.0 EvidenceConfidenceFactor (S2 = 0.50 … S5 = 1.00) and the "adjusted indicator" it produced are withdrawn: multiplying a score by an evidence factor blended two different questions (how good is the control, how well do we know) into one number and let a weak-evidence CONFORMING outscore a well-evidenced PARTIAL.

## Evidence Quality Index (EQI)

EQI is a single number per Evidence Object for a given use, defined as:

EQI = 100 × (0.20·P + 0.20·F + 0.15·C + 0.20·R + 0.15·T + 0.10·I) / 5

where each letter is the 0–5 rating for that use. The weights sum to 1.00.

| **Dimension** | **Weight** | **Rationale** |
|---|---|---|
| P Provenance | 0.20 | Without established origin an item cannot support any claim; weighted with F and R as the three dimensions that decide whether the item can bear on the claim at all. |
| F Fitness | 0.20 | Relevance to the precise criterion, claim type and state is the most common reason a well-sourced item fails to support a claim. |
| R Reliability | 0.20 | Method and corroboration determine whether the item would have detected a nonconforming condition. |
| C Coverage | 0.15 | Coverage is also tested at package level through sufficiency and state coverage, so it carries less weight per item. |
| T Timeliness | 0.15 | Currency is also enforced by change-based invalidation (AIDCF-008 §20), so it carries less weight per item. |
| I Integrity | 0.10 | Integrity has a hard floor (I0 forces Q0) and is largely a repository property applied uniformly; the residual variation between items is smaller. |

Example: an item rated E4-P4-F4-C3-R4-T4-I3 has EQI = 100 × (0.8 + 0.8 + 0.45 + 0.8 + 0.6 + 0.3) / 5 = 100 × 3.75 / 5 = 75.0.

**SDF-REQ-011** EQI shall be used only as a secondary sorting aid (for example to order evidence for review or to prioritise evidence remediation), consistent with AIDCF-008 §18. It shall never change a quality band, sufficiency level, ControlResult, Gate Result, band or decision, and shall always be displayed with the full quality vector.

**SDF-REQ-012** An Evidence Package that does not meet the profile's per-dimension quality floor, required classes or sufficiency floor shall yield an UNKNOWN result for the claim; no multiplier, discount or adjusted score shall be applied instead.

# Part VI - Scoring and aggregation

## Generic rule (applies to every family and domain)

The v1.0 framework repeated an identical scoring profile for each of the 90 families. They are replaced by this single rule; the genuine per-domain exceptions follow it.

1. Unit. The unit of scoring is the ControlResult for one control, one mandatory (or assessed optional) claim type and one scope.
2. Control score. The score is the value in Part III: CONFORMING 100, PARTIAL 50, NONCONFORMING 0; UNKNOWN, NOT_ASSESSED and NOT_APPLICABLE have no value.
3. Family and domain score. For a scope S and claim type c, the score is the arithmetic mean of the values of the scored ControlResults (CONFORMING, PARTIAL, NONCONFORMING) for controls in S, computed directly over controls (a domain score is not a mean of family means). Control weights are equal unless an approved capability profile weights named controls before results are recorded.
4. Coverage. Coverage % = 100 × scored / (in-scope − NOT_APPLICABLE), where in-scope counts the ControlResults required for claim type c in S. UNKNOWN and NOT_ASSESSED stay in the denominator.
5. Band. Bands are: B5 Strong ≥ 90; B4 Substantial 75–89.99; B3 Moderate 50–74.99; B2 Weak 25–49.99; B1 Very weak < 25.
6. Withholding. A band is reported for S and c only if coverage ≥ 80% and no US4 or US5 UNKNOWN is attached to any ControlResult or gate criterion in S. Otherwise the output is "Band withheld (coverage)", "Band withheld (UNKNOWN)" or "Band withheld (coverage/UNKNOWN)". The numeric mean may be shown only next to the withholding label, its coverage and its UNKNOWN count.
7. Disclosure. Every score is shown with: claim type, coverage %, counts of CONFORMING, PARTIAL, NONCONFORMING, UNKNOWN (by severity), NOT_ASSESSED and NOT_APPLICABLE, the mapped Gate Results, and the rule version.
8. Gates. Scores never override gates. A family or domain score is never shown without the Gate Results of the gates to which its controls are mapped.

**SDF-REQ-013** Family, domain and capability scores shall be computed by the generic rule; no family-specific formula shall be used unless listed in the domain exception table below.

**SDF-REQ-014** A band shall be withheld where coverage is below 80% or any US4 or US5 UNKNOWN is attached within the scope; the withholding reason shall be stated.

**SDF-REQ-015** Control weights, the CAI domain weights and any capability-profile variations shall be approved and frozen before the first ControlResult is recorded; a later change creates a new score series.

## Capability Assurance Index (CAI)

CAI for claim type c = Σ (wd × DomainScore d,c) / Σ wd, over the domains d included for c that have at least one scored ControlResult. CAI coverage is computed over all included domains' ControlResults by the generic rule, and the CAI band is withheld on the same conditions at capability scope. CAI is a summary for one Capability Instance; it is not a facility rating.

Default domain weights (provisional; they reflect the relative contribution of each domain to typical AI training and inference Service Outcomes and are subject to the calibration review in the release gates):

| **Domain** | **Default weight** | **Domain** | **Default weight** |
|---|---|---|---|
| GOV | 5 | CMP | 9 |
| CAP | 5 | STO | 9 |
| DEP | 7 | NET | 9 |
| PHY | 5 | OPS | 7 |
| POW | 10 | RES | 9 |
| THM | 10 | SUP | 4 |
| ENV | 4 | SEC | 5 |
| EVA | 2 (excluded by default; see exceptions) | | |

## Domain exceptions (only where justified)

| **Domain / scope** | **Exception** | **Justification** |
|---|---|---|
| EVA (all families) | EVA scores are computed and reported but EVA is excluded from CAI by default (CAI normalises by the weights of included domains). | EVA controls assess the assurance process itself; their decision effect is already carried by meta-gates CG-11 and CG-12. Including them in CAI would count the same deficiency twice. |
| GOV, EVA | For OPERATION claims, records of the governance or assessment process operating (decisions taken, reviews held, appeals handled over the period) satisfy the E3 class. | Governance controls have no telemetry; without this interpretation every GOV/EVA OPERATION claim would be UNKNOWN by construction. |
| CMP, STO, NET (fleet-scale controls) | Controls applied to large homogeneous populations (nodes, accelerators, links, drives) are assessed per declared population stratum (for example per accelerator model and firmware baseline, or per cluster), each stratum a scope; results combine by the least-favourable rule. A stratum's sampled exception rate above the profile's declared tolerance parameter makes it PARTIAL or NONCONFORMING as the profile states. | Fleets of thousands of identical items are evidenced by sampling (AIDCF-008 §23); treating each item as a control result would swamp the scores, and treating the fleet as one undivided item would hide a bad stratum. |
| POW, THM | OPERATION, EFFECTIVENESS and RESILIENCE claims are state-scoped: results are recorded per operating state in the profile's stateCoverage (at least NORMAL and MAINTENANCE for concurrently maintainable designs) and combined by the least-favourable rule. | A path that is redundant in NORMAL can be single-threaded in MAINTENANCE; averaging across states would hide exactly the condition that defeats the outcome. |
| DEP | Alongside control coverage, dependency coverage = evidenced material dependency paths / identified material dependency paths is reported. The DEP band is also withheld if dependency coverage < 80%. | DEP controls can be CONFORMING against an incomplete dependency inventory; dependency coverage exposes the population the results do not reach. |
| ENV-02 to ENV-04 | Results concern measurement and reporting integrity of energy, water and carbon metrics. They contribute to CAI and the Resource view but are relevant to the decision derivation band step only where the decision question includes an environmental Service Outcome. | Environmental reporting weaknesses do not by themselves bear on availability or performance outcomes. |
| RES-05 (testing and exercising) | An exercise that reveals a defect supports CONFORMING for the testing control if it was planned, executed and analysed as required; the defect is recorded against the control under test. | Prevents a disincentive to test and double counting of one defect. |
| SEC, SUP-06 | Control-level results are classified RESTRICTED by default in reports (AIDCF-012); domain bands and Gate Results may be published while control-level detail is withheld. | Control-level security results describe exploitable weaknesses. |

# Part VII - Worked numeric examples

Synthetic, for method validation only; not real assessments.

## Example 1 - Band reported (POW, OPERATION)

The assessment has target AL4 or higher, so OPERATION is mandatory for 22 of the 24 POW controls (two have requiredAssuranceLevel AL3). One is approved NOT_APPLICABLE with rationale.

| **Result** | **Count** | **Value** | **Contribution** |
|---|---|---|---|
| CONFORMING | 15 | 100 | 1500 |
| PARTIAL | 3 | 50 | 150 |
| NONCONFORMING | 1 | 0 | 0 |
| UNKNOWN (US3) | 1 | — | — |
| NOT_ASSESSED | 1 | — | — |
| NOT_APPLICABLE | 1 | excluded | — |

- Scored = 15 + 3 + 1 = 19. Denominator = 22 − 1 = 21. Coverage = 19 / 21 = 90.5%.
- Mean = 1650 / 19 = 86.84.
- Coverage ≥ 80% and no US4/US5 UNKNOWN: band reported. Output: "POW · OPERATION · 86.8 · B4 Substantial · coverage 90.5% · 15 C / 3 P / 1 NC / 1 UNKNOWN (US3) / 1 NOT_ASSESSED / 1 NA · CG-05 PASS".
- Had the UNKNOWN been encoded as 0 (prohibited), the mean would have been 1650 / 20 = 82.5; had it been imputed as the average, the gap would have disappeared from view. Neither is permitted.
- The NONCONFORMING control holds only a SUPPORTING mapping to CG-05, so the gate is not failed automatically; CG-05 PASS requires a documented gate-level evaluation concluding the deficiency does not defeat the gate. That evaluation and the Finding feed the decision's condition step.

## Example 2 - Band withheld for coverage (THM, EFFECTIVENESS, AL5 assessment)

EFFECTIVENESS is mandatory for 18 THM controls; none is NOT_APPLICABLE. Three failover tests were not produced (U1), each graded US3 because the controls concerned hold no CRITICAL gate mapping and no gate criterion depends on them.

| **Result** | **Count** | **Contribution** |
|---|---|---|
| CONFORMING | 12 | 1200 |
| PARTIAL | 2 | 100 |
| NONCONFORMING | 0 | 0 |
| UNKNOWN (US3) | 3 | — |
| NOT_ASSESSED | 1 | — |

- Scored = 14. Coverage = 14 / 18 = 77.8% (< 80%).
- Mean = 1300 / 14 = 92.86, which would be B5.
- Output: "THM · EFFECTIVENESS · Band withheld (coverage) · mean 92.9 on 77.8% coverage · 3 UNKNOWN (US3) · 1 NOT_ASSESSED". A narrow, high mean is not published as "Strong".
- Decision effect: the US3 UNKNOWNs cap affected outcomes at CONDITIONALLY_ASSURED with conditions to produce the tests, and the domain coverage below 80% does the same at the coverage step.

## Example 3 - Band withheld for a critical UNKNOWN (NET, OPERATION)

All 24 NET controls are in scope for OPERATION; one is NOT_APPLICABLE. For MCF-NET-002 Path Diversity, cross-connect records contradict the topology export on whether two spine uplinks share a tray (U4 Conflicting). The control holds a CRITICAL mapping to CG-08, so the UNKNOWN is US4.

| **Result** | **Count** | **Contribution** |
|---|---|---|
| CONFORMING | 20 | 2000 |
| PARTIAL | 1 | 50 |
| UNKNOWN (US4) | 1 | — |
| NOT_ASSESSED | 1 | — |
| NOT_APPLICABLE | 1 | — |

- Scored = 21. Coverage = 21 / 23 = 91.3%.
- Mean = 2050 / 21 = 97.62, which would be B5.
- Output: "NET · OPERATION · Band withheld (UNKNOWN) · mean 97.6 · coverage 91.3% · 1 UNKNOWN (US4, MCF-NET-002) · CG-08 UNKNOWN".
- Gate effect: under the roll-up rule, a CRITICAL control that is UNKNOWN makes CG-08 UNKNOWN; the CG-08 UNKNOWN ceiling caps the Service Outcomes delivered by that fabric at LIMITED, whatever the mean.

## Example 4 - Decision derivation (combining Examples 1 to 3)

Decision question: "Can training cluster TC-1 in hall H2 deliver O1 (sustained training throughput within the declared performance tolerance) and O2 (power and heat removal at the rack interface within tolerance) under NORMAL and MAINTENANCE states, as of the assessment date?" Target AL5, so Examples 1 to 3 are all mandatory results of this assessment. All gates other than CG-08 are PASS; CG-08 UNKNOWN (Example 3). Capability coverage across mandatory ControlResults is 88%. Capability OPERATION CAI is 87.5 (B4) with the NET band withheld. One Significant weakness Finding exists (the POW NONCONFORMING control, Example 1).

| **Step** | **O1 (throughput)** | **O2 (rack power and heat removal)** |
|---|---|---|
| Start | REASONABLY_ASSURED | REASONABLY_ASSURED |
| 1 Gates | CG-08 UNKNOWN → ≤ LIMITED | Not affected by CG-08 |
| 2 UNKNOWN severity | US4 already applied via CG-08; THM US3 not relevant to O1 | THM US3 (Example 2) → ≤ CONDITIONALLY_ASSURED |
| 3 Coverage | Capability 88%; NET 91.3% → no cap | THM EFFECTIVENESS coverage 77.8% < 80% → ≤ CONDITIONALLY_ASSURED (coverage condition) |
| 4 Bands | CAI B4 → no cap | POW B4, THM OPERATION B4 → no cap |
| 5 Conditions | — | POW Significant weakness → ≤ CONDITIONALLY_ASSURED, condition recorded |
| Maximum permissible | LIMITED | CONDITIONALLY_ASSURED |

The Decision Recommendation for the whole question is LIMITED (the lower of the two, since the question asks for both), with a per-outcome breakdown. Controlling reasons: CG-08 UNKNOWN from US4 on MCF-NET-002; for O2, the THM US3 UNKNOWNs, the THM coverage gap and the POW Finding as named, owned, time-bound conditions. Prohibited higher states: REASONABLY_ASSURED and CONDITIONALLY_ASSURED for the question as a whole. The decision owner may approve LIMITED, issue per-outcome decisions (O1 LIMITED, O2 CONDITIONALLY_ASSURED) if the decision question permits partition, or select a lower state with rationale. The owner may not select CONDITIONALLY_ASSURED for O1.

# Part VIII - Critical gates

**Critical gates are evaluated before and outside numeric aggregation.**

## Gate results

| **Gate result** | **Meaning** |
|---|---|
| PASS | All CRITICAL controls CONFORMING at their mandatory claim types, all gate criteria met with evidence at or above the floor, and every NONCONFORMING SUPPORTING control has a gate-level evaluation concluding no defeat. No ceiling from this gate. |
| FAIL | An in-scope CRITICAL control is NONCONFORMING or PARTIAL, or a gate criterion is demonstrated not met. The gate's FAIL ceiling applies. |
| UNKNOWN | Not FAIL, and any in-scope CRITICAL control is UNKNOWN or NOT_ASSESSED, gate evidence is below the floor, or a US4 UNKNOWN is attached. The gate's UNKNOWN ceiling applies. |
| APPROVED_NA | Approved boundary rationale meeting the gate's APPROVED_NA conditions. No ceiling. |
| NOT_ASSESSED | Applicable but not evaluated. Treated as UNKNOWN for the decision derivation. |

There is no conditional gate state. Conditions exist only at decision level.

## Roll-up rule (canonical)

For a gate in scope, evaluated in this order:

1. FAIL if any in-scope CRITICAL control is NONCONFORMING or PARTIAL at a mandatory claim type, or any gate criterion is demonstrated not met.
2. Else UNKNOWN if any in-scope CRITICAL control is UNKNOWN or NOT_ASSESSED at a mandatory claim type, or the gate evidence package is below the gate's effective floor, or a US4 UNKNOWN is attached to the gate or one of its criteria.
3. Else PASS if every CRITICAL control is CONFORMING at its mandatory claim types, every gate criterion is met with evidence at or above the floor, and every SUPPORTING control that is NONCONFORMING has a documented gate-level evaluation concluding no defeat of the gate scope. A NONCONFORMING SUPPORTING control without that evaluation leaves the gate UNKNOWN.
4. APPROVED_NA only with an approved boundary rationale meeting the gate's APPROVED_NA conditions.

PARTIAL never yields PASS. A SUPPORTING control's PARTIAL or UNKNOWN does not by itself change the Gate Result but is listed among the gate's controlling facts.

CRITICAL and SUPPORTING roles are carried per control in the AIDCF-007A registry (gateMappings). A CRITICAL mapping means the gate cannot PASS unless the control is CONFORMING; SUPPORTING means the control informs the gate and a NONCONFORMING result requires gate-level evaluation. The control lists in the specifications below are generated from the AIDCF-007A registry v1.1 gate-mappings; if they ever differ, the registry governs. CG-11 and CG-12 are meta-gates evaluated across all controls and are not mapped per control.

Effective evidence floor. The gate floor (S3–S5) applies to evidence for claims at OPERATION depth or deeper. Where the deepest mandatory claim type of the gate's CRITICAL controls is DESIGN or IMPLEMENTATION, the effective floor is the lower of the gate floor and S3; the Gate Result then states that depth (SDF requirement on claim depth, Part IV).

Gate ceilings are expressed against decision states ordered REASONABLY_ASSURED > CONDITIONALLY_ASSURED > LIMITED > INCONCLUSIVE > NOT_ASSURED, and apply to the Service Outcomes and claims stated; where a ceiling names "the decision as a whole", it applies to every outcome in the decision question.

**SDF-REQ-016** Each in-scope gate shall be evaluated using the roll-up rule and its gate criteria, independently of any score, before the decision derivation is run.

**SDF-REQ-017** Every Gate Result shall record: gate, scope, claim depth, result, the CRITICAL and SUPPORTING control results relied on, each criterion's status with evidence references, attached UNKNOWN Records, gate-level evaluations of NONCONFORMING SUPPORTING controls, the ceiling applied, reviewer and date.

**SDF-REQ-018** APPROVED_NA shall be recorded only where the gate's APPROVED_NA conditions are met, with rationale and approver; CG-01, CG-02, CG-03, CG-09, CG-11, CG-12, CG-13 and CG-14 shall never be APPROVED_NA.

**SDF-REQ-019** A gate override that raises FAIL or UNKNOWN to PASS shall not be permitted; a Gate Result changes only through new evidence, a corrected ControlResult or an approved boundary change, each recorded.

## Gate summary

| **Gate** | **Name** | **Floor** | **Classes** | **Criteria** | **APPROVED_NA possible** |
|---|---|---|---|---|---|
| CG-01 | Capability and outcome definition | S3 | E1+E7 | GC-01-1 to GC-01-6 | No |
| CG-02 | Boundary and architecture integrity | S3 | E1+E2+E6 | GC-02-1 to GC-02-6 | No |
| CG-03 | Critical dependency visibility | S4 | E1+E2+E7 | GC-03-1 to GC-03-7 | No |
| CG-04 | Life safety and hazardous energy | S4 | E1+E4+E5 | GC-04-1 to GC-04-8 | Restricted |
| CG-05 | Resilient electrical supply | S5 | E1+E2+E3+E4 | GC-05-1 to GC-05-8 | Restricted |
| CG-06 | Thermal continuity | S5 | E1+E2+E3+E4 | GC-06-1 to GC-06-8 | Restricted |
| CG-07 | Critical control-system integrity | S4 | E1+E2+E3+E4 | GC-07-1 to GC-07-7 | Restricted |
| CG-08 | Compute, storage and network functional integrity | S4 | E2+E3+E4 | GC-08-1 to GC-08-7 | Restricted |
| CG-09 | Failure containment | S4 | E1+E2+E4+E7 | GC-09-1 to GC-09-6 | No |
| CG-10 | Recovery readiness | S5 | E1+E2+E3+E4 | GC-10-1 to GC-10-7 | Restricted |
| CG-11 | Evidence sufficiency | S4 | E1+E7 | GC-11-1 to GC-11-6 | No |
| CG-12 | Critical UNKNOWN | S3 | E1+E7 | GC-12-1 to GC-12-5 | No |
| CG-13 | Responsibility and authority | S3 | E1+E6 | GC-13-1 to GC-13-6 | No |
| CG-14 | Change control | S4 | E1+E2+E3+E4 | GC-14-1 to GC-14-7 | No |
| CG-15 | Integrated digital authority over infrastructure | S4 | E2+E3+E4+E7 | GC-15-1 to GC-15-7 | Restricted |

## CG-01 Capability and outcome definition

**Purpose and scope.** Protects the subject of the top claim. Without an approved Capability Instance, measurable Service Outcomes with tolerances, a declared operating envelope and a decision question, no evidence can be judged relevant (F) or sufficient, and no decision can be bounded. The gate is evaluated first and is always applicable. Scope: Capability Instance, Service Outcomes, tolerances, criticality and decision question are defined, owned and approved.

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S3; E1+E7 (AIDCF-008 Part XIII). |
| Mandatory evidence | Capability register extract with owner and lifecycle status; approved Service Outcome specification (metric, measurement point, tolerance, applicable operating states); criticality and impact-tolerance analysis; operating-envelope declaration; outcome-to-function-to-architecture traceability matrix; decision-question record. |
| CRITICAL mappings (AIDCF-007A registry v1.1, 7) | MCF-CAP-001 Capability Register; MCF-CAP-005 Availability Outcomes; MCF-CAP-006 Performance Outcomes; MCF-CAP-007 Integrity Outcomes; MCF-CAP-008 Recovery Outcomes; MCF-CAP-010 Impact Tolerance; MCF-EVA-009 Decision Question |
| SUPPORTING mappings (AIDCF-007A registry v1.1, 16) | MCF-GOV-017; MCF-GOV-019; MCF-CAP-002; MCF-CAP-003; MCF-CAP-004; MCF-CAP-009; MCF-CAP-011; MCF-CAP-023; MCF-THM-001; MCF-ENV-024; MCF-CMP-001; MCF-CMP-009; MCF-STO-001; MCF-RES-001; MCF-RES-009; MCF-RES-012 |
| Roll-up | Canonical roll-up rule (above). Gate criteria are definitional, so CRITICAL controls are evaluated at DESIGN (and IMPLEMENTATION where mandatory) whatever the assessment's target Assurance Level. An outcome omitted from the specification is excluded from the decision question, not treated as defined. |
| FAIL ceiling | INCONCLUSIVE for the whole decision: the top claim cannot be framed. The assessment returns to planning (AIDCF-009 DT-02) and no outcome-level decision is issued. |
| UNKNOWN ceiling | INCONCLUSIVE for each Service Outcome whose definition or tolerance is UNKNOWN (US5); the remaining outcomes are capped at LIMITED. |
| APPROVED_NA conditions | Never. Every assessment has a Capability Instance and decision question. |
| Reassessment triggers | Change to the capability register entry, owner or lifecycle status; Change to any Service Outcome, tolerance or criticality; Envelope change such as a new accelerator generation or a rack-density increase; Change of decision question or intended use. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-01-1 | The Capability Instance is recorded in the capability register with a unique identifier, accountable owner and lifecycle status, and the record is approved by the named authority. | Capability register extract; approval record | DOCUMENT_REVIEW; INQUIRY: confirm register entry, owner and approval against delegation of authority |
| GC-01-2 | Each Service Outcome in the decision question has a measurable definition: metric, measurement point, tolerance and the operating states in which it applies. | Approved Service Outcome specification | DOCUMENT_REVIEW; ANALYSIS: check each outcome for metric, measurement point, tolerance and states; any missing element fails the criterion |
| GC-01-3 | Criticality and impact tolerance are defined and approved per outcome, with the consequence basis recorded. | Criticality and impact-tolerance analysis; approval record | DOCUMENT_REVIEW; INQUIRY: trace each tolerance to an approved consequence analysis |
| GC-01-4 | The operating envelope (load, environmental, duration and state-specific limits) for which outcomes are claimed is declared with parameter values. | Operating-envelope declaration | DOCUMENT_REVIEW; ANALYSIS: confirm each envelope parameter has a value, unit and basis |
| GC-01-5 | Every Service Outcome traces to at least one Required Function and to the architecture elements that implement it. | Outcome-function-architecture traceability matrix | RECONCILIATION: trace a sample of outcomes forward to architecture and architecture elements back to outcomes; untraced elements are recorded |
| GC-01-6 | The decision question states the decision to be supported, the accountable decision owner, the intended use and the as-of date or period. | Decision-question record in the assessment plan | DOCUMENT_REVIEW: confirm all four elements are present and approved by the decision owner |

**Typical failure patterns**

- Outcomes expressed as design labels (for example a tier rating or "N+1") rather than measurable service tolerances.

- Tolerances absent or qualitative ("high availability") so nothing can be tested against them.

- Capability defined by product or SKU instead of the service delivered to the consumer.

- Envelope declared at nameplate rack density rather than the contracted or forecast density and accelerator transient behaviour.

- Training and inference outcomes conflated although their interruption and recovery tolerances differ.

- Evidence collected before a decision question exists, so its fitness cannot be judged.

## CG-02 Boundary and architecture integrity

**Purpose and scope.** Protects the correspondence between the evidence and the real system. Evidence about an architecture that is not the one built, or a boundary that silently excludes something the outcomes depend on, cannot support any claim about the Capability Instance. Scope: Assessment boundary, current architecture, as-built reconciliation and exclusions.

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S3; E1+E2+E6 (AIDCF-008 Part XIII). |
| Mandatory evidence | Approved assessment boundary with exclusions and rationale; provider/tenant demarcation records; current, versioned architecture records (single-line diagrams, P&IDs, network and cluster topology); as-built/as-configured reconciliation records with discrepancy log; boundary-interface register. |
| CRITICAL mappings (AIDCF-007A registry v1.1, 3) | MCF-CAP-004 Architecture Linkage; MCF-DEP-017 Assessment Boundary; MCF-EVA-010 Scope and Criteria |
| SUPPORTING mappings (AIDCF-007A registry v1.1, 16) | MCF-CAP-021; MCF-CAP-022; MCF-CAP-024; MCF-DEP-001; MCF-PHY-001; MCF-PHY-005; MCF-PHY-012; MCF-POW-009; MCF-THM-002; MCF-CMP-004; MCF-CMP-005; MCF-CMP-024; MCF-NET-001; MCF-NET-020; MCF-OPS-017; MCF-RES-005 |
| Roll-up | Canonical roll-up rule (above). Reconciliation discrepancies are dispositioned individually: a discrepancy that changes capacity, redundancy, protection or a fault domain makes GC-02-4 not met (FAIL); an undispositioned discrepancy whose effect is not yet known makes the gate UNKNOWN. |
| FAIL ceiling | If the boundary itself cannot be established: INCONCLUSIVE for the whole decision. If reconciliation demonstrates material divergence in part of the architecture: NOT_ASSURED for claims about the unreconciled systems and LIMITED for the decision as a whole. |
| UNKNOWN ceiling | LIMITED. Claims about systems whose reconciliation is incomplete are restricted to the DESIGN claim type. |
| APPROVED_NA conditions | Never. |
| Reassessment triggers | Boundary change or new exclusion; Expansion, new hall or major refurbishment; Provider or demarcation change; A reconciliation discrepancy discovered in operation or by another assessment. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-02-1 | The assessment boundary is documented and approved, listing included systems, locations and interfaces, and every exclusion with its rationale. | Approved boundary statement | DOCUMENT_REVIEW; INQUIRY: confirm approval and that each exclusion has rationale |
| GC-02-2 | Provider and tenant responsibility boundaries are documented at each demarcation point and agreed by both parties. | Demarcation schedule; contract extracts; signed RACI | DOCUMENT_REVIEW; INSPECTION: verify demarcation points on site against the schedule |
| GC-02-3 | Current architecture records exist for every in-boundary system, each with version, date and approver. | Single-line diagrams, P&IDs, network and cluster topology records | DOCUMENT_REVIEW: check presence, version and approval for each in-boundary system |
| GC-02-4 | As-built or as-configured reconciliation has been performed for each in-boundary system, and each discrepancy is recorded and dispositioned. | Reconciliation records; discrepancy log; configuration exports | RECONCILIATION; SAMPLING; INSPECTION: compare a risk-based sample of physical and configured state with the architecture records |
| GC-02-5 | No component on which a Required Function depends lies outside the boundary unless it is recorded as an external dependency for evaluation under CG-03. | Dependency model; boundary statement | ANALYSIS: trace Required Functions to components and compare with the boundary and external dependency list |
| GC-02-6 | Every interface crossing the boundary (power, water, network, management access) is enumerated with an owner on each side. | Boundary-interface register | DOCUMENT_REVIEW; INSPECTION: sample interfaces on site and confirm both owners |

**Typical failure patterns**

- Boundary drawn around the data hall while the switchgear, chilled-water plant or heat rejection it depends on sits in a shared plant outside it, unrecorded.

- "As-built" drawings that are the issued-for-construction set.

- Provider/tenant demarcation ambiguous at the CDU secondary loop, the rack PDU or the cross-connect.

- Temporary equipment (load banks, temporary chillers, temporary feeds) present but absent from the architecture.

- Network topology export from the controller that does not match the physical cabling records.

## CG-03 Critical dependency visibility

**Purpose and scope.** Protects every redundancy, independence and recovery claim. A redundant design is only as independent as its least visible shared element: a common source, controller, route, person or provider can defeat the redundancy that all other gates assume. Scope: Material internal and external dependencies, common-mode exposure and concentration are identified and owned.

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S4; E1+E2+E7 (AIDCF-008 Part XIII). |
| Mandatory evidence | Dependency graph from Required Functions to assets, upstream sources and external providers; common-mode analysis for each redundancy claim (shared source, controller, route, human); external provider register with service terms and evidence rights; concentration and substitution analysis; owner assignments; evidence that the model is reconciled to configuration and route data. |
| CRITICAL mappings (AIDCF-007A registry v1.1, 9) | MCF-DEP-001 Asset-to-Function Mapping; MCF-DEP-002 Upstream Dependency Mapping; MCF-DEP-005 Shared Source Analysis; MCF-DEP-007 Shared Route Analysis; MCF-DEP-009 Utility Dependency; MCF-DEP-010 Telecom Dependency; MCF-DEP-012 Cloud and Service Dependency; MCF-DEP-017 Assessment Boundary; MCF-SUP-004 Sub-Tier Visibility |
| SUPPORTING mappings (AIDCF-007A registry v1.1, 50) | MCF-GOV-006; MCF-CAP-004; MCF-DEP-003; MCF-DEP-004; MCF-DEP-006; MCF-DEP-008; MCF-DEP-011; MCF-DEP-013; MCF-DEP-014; MCF-DEP-016; MCF-DEP-018; MCF-DEP-021; MCF-DEP-023; MCF-DEP-024; MCF-PHY-001; MCF-PHY-002; MCF-PHY-004; MCF-POW-001; MCF-POW-003; MCF-POW-008; MCF-POW-020; MCF-THM-004; MCF-THM-015; MCF-THM-016; MCF-ENV-011; MCF-ENV-022; MCF-ENV-024; MCF-CMP-008; MCF-CMP-022; MCF-STO-014; MCF-NET-002; MCF-NET-004; MCF-NET-015; MCF-NET-018; MCF-NET-020; MCF-NET-024; MCF-OPS-018; MCF-RES-003; MCF-RES-005; MCF-RES-007; MCF-RES-010; MCF-RES-011; MCF-RES-013; MCF-SUP-001; MCF-SUP-002; MCF-SUP-006; MCF-SUP-007; MCF-SUP-012; MCF-SUP-018; MCF-SUP-020 |
| Roll-up | Canonical roll-up rule (above). The gate is evaluated per redundancy claim relied on by a Service Outcome. A demonstrated, unaddressed common mode across paths relied on as independent makes GC-03-3 not met (FAIL) for the outcomes relying on that claim. A dependency that cannot be established (U10) is graded US4, or US5 if it could span two or more gates. |
| FAIL ceiling | NOT_ASSURED for every Service Outcome whose redundancy or independence claim is defeated by the identified common mode; LIMITED for the decision as a whole. |
| UNKNOWN ceiling | LIMITED. RESILIENCE claims for the affected outcomes are INCONCLUSIVE. |
| APPROVED_NA conditions | Never. |
| Reassessment triggers | New or changed external provider or contract; Route, feed or controller change; Consolidation of control or management systems; Staffing or support-model change; Supplier merger, insolvency or sanction; An incident revealing an unrecorded dependency. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-03-1 | Every Required Function is mapped to the assets and systems that implement it, with upstream dependencies traced to the boundary or to a named external provider. | Dependency graph; asset-to-function map | ANALYSIS; RECONCILIATION: trace a sample of functions end to end and confirm each path terminates at the boundary or a named provider |
| GC-03-2 | Recovery dependencies (services, data, tools, spares, people and providers needed to restore each function) are mapped. | Recovery dependency map | DOCUMENT_REVIEW; ANALYSIS: compare with recovery procedures and confirm each prerequisite is mapped |
| GC-03-3 | Shared source, common controller, shared route and shared human dependencies are analysed for every redundancy claim used by a Service Outcome, and each common mode is recorded with consequence and disposition. | Common-mode analysis per redundancy claim | ANALYSIS; INSPECTION: test a sample of claimed-independent paths for shared elements on drawings, configuration and site |
| GC-03-4 | Each external dependency has a documented provider, service terms, incident-notification obligations and evidence rights. | Provider register; contract extracts | DOCUMENT_REVIEW: verify terms and evidence rights for each material provider |
| GC-03-5 | Capacity, supplier and knowledge concentration is assessed, with substitution readiness recorded for each critical concentration. | Concentration and substitution analysis | ANALYSIS; INQUIRY: confirm substitution options and lead times for each critical concentration |
| GC-03-6 | Every material dependency has a named accountable owner. | Dependency register with owners | DOCUMENT_REVIEW; INQUIRY: confirm with a sample of named owners |
| GC-03-7 | The dependency model is reconciled with configuration, topology and route evidence and is current against change records. | Configuration and topology exports; change records; reconciliation record | RECONCILIATION: compare the model with exports and changes since the model date |

**Typical failure patterns**

- Two utility feeds described as diverse that originate from the same upstream substation or circuit.

- "Diverse" fibre routes that share a duct, bridge or building entry.

- Both A and B cooling or power trains supervised by a single PLC, BMS server or controller network.

- A single specialist or vendor engineer on whom all recovery actions depend.

- DNS, time, identity or provisioning services needed for recovery hosted inside the failure domain they must recover.

- A single OEM for accelerators, firmware and RMA with no substitution path.

## CG-04 Life safety and hazardous energy

**Purpose and scope.** Protects people and governs whether the assessment itself may proceed safely. It is the only gate whose result also controls assessment activity: no hazardous test may be authorised in an area where this gate is not PASS. It never trades against service outcomes. Scope: Fire, electrical arc-flash and shock, hazardous fluids and chemicals, confined space, refrigerants, battery thermal runaway and safe work.

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S4; E1+E4+E5 (AIDCF-008 Part XIII). |
| Mandatory evidence | Current fire strategy, detection and suppression inspection and test records by competent persons, with approvals from the authority having jurisdiction where required; current arc-flash and shock risk assessment for the installed configuration and labelling records; permit-to-work, lockout/tagout and method-statement records in use; battery hazard assessment for the installed chemistry; inventory and safety data for refrigerants, coolants, fuels and suppressants; EPO and suppression-interface governance; register of open life-safety Findings; authorisations for any hazardous test. |
| CRITICAL mappings (AIDCF-007A registry v1.1, 13) | MCF-PHY-021 Fire Detection; MCF-PHY-022 Suppression Interfaces; MCF-PHY-023 Egress and Emergency Access; MCF-PHY-024 Emergency Shutdown Governance; MCF-POW-010 Battery Condition; MCF-POW-013 Switchgear Integrity; MCF-POW-016 Earthing and Bonding; MCF-POW-023 Switching Procedures; MCF-THM-018 Water Quality; MCF-ENV-018 Refrigerants and Coolants; MCF-OPS-004 Competence and Authorisation; MCF-OPS-007 Permit to Work; MCF-OPS-008 Lockout and Tagout |
| SUPPORTING mappings (AIDCF-007A registry v1.1, 24) | MCF-CAP-024; MCF-PHY-001; MCF-PHY-005; MCF-PHY-006; MCF-PHY-010; MCF-PHY-011; MCF-PHY-018; MCF-THM-006; MCF-THM-012; MCF-THM-013; MCF-THM-017; MCF-THM-019; MCF-THM-020; MCF-THM-023; MCF-ENV-009; MCF-ENV-017; MCF-ENV-019; MCF-OPS-003; MCF-OPS-006; MCF-OPS-019; MCF-RES-008; MCF-SUP-009; MCF-SUP-010; MCF-EVA-011 |
| Roll-up | Canonical roll-up rule (above). The gate is evaluated per area (room, hall or plant space). Statutory approvals and third-party inspections are evidence (E5), not automatic PASS (non-inheritance). An open imminent-hazard Finding without interim protection makes GC-04-7 not met (FAIL) regardless of control results. Life-safety evidence is not substituted by design documents alone: E4 inspection or test evidence is mandatory. |
| FAIL ceiling | NOT_ASSURED for any claim relying on the affected area; all hazardous testing in the affected area is suspended; the duty holder is notified immediately (outside the decision process); LIMITED for the decision as a whole. |
| UNKNOWN ceiling | LIMITED for outcomes depending on the affected area. No hazardous test is authorised there until the gate is resolved, so EFFECTIVENESS and RESILIENCE claims that need such tests remain UNKNOWN. |
| APPROVED_NA conditions | Only when no physical infrastructure and no site activity lies within the boundary (for example a desk-based review of a logical platform whose facility is an external dependency under CG-03); approved by the decision owner with rationale. |
| Reassessment triggers | Change of battery chemistry or energy-storage capacity; Protection-setting or distribution change; Introduction of a new coolant, refrigerant or suppressant; Change to the fire strategy or zoning; Incident or near miss; Adverse regulatory or insurer inspection. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-04-1 | Fire detection and suppression cover all in-boundary spaces, including battery rooms, generator and fuel areas and liquid-cooled halls, with current inspection and test records by a competent person and jurisdictional approvals where required. | Fire strategy; detection and suppression inspection/test records; approvals | DOCUMENT_REVIEW; INSPECTION: walk down each space against the fire strategy and verify current test records |
| GC-04-2 | An arc-flash and shock risk assessment is current for the installed configuration, the protective-device settings it assumes match the installed settings, and equipment is labelled accordingly (assessed against the applicable regime, for example NFPA 70E with IEEE 1584 or national equivalents). | Arc-flash study; extracted device settings; labelling survey | RECONCILIATION; INSPECTION: compare study assumptions with extracted settings and sample labels |
| GC-04-3 | Permit-to-work, lockout/tagout, method statements and competence authorisation are defined and evidenced in use for energised, hazardous-fluid and confined-space work. | Permits, LOTO records and method statements for a sample of completed work; competence register | SAMPLING; DOCUMENT_REVIEW; OBSERVATION: trace a sample of hazardous work orders to permits, isolations and authorised persons |
| GC-04-4 | Battery thermal-runaway hazards are addressed for the installed chemistry: detection, ventilation or off-gas management, segregation and suppression, consistent with the applicable standard family (for example NFPA 855 or national equivalents). | Battery hazard assessment; room design; inspection records | DOCUMENT_REVIEW; INSPECTION: verify measures in place against the hazard assessment |
| GC-04-5 | Refrigerants, coolants, fuels and suppressants are inventoried with safety data, leak detection where the hazard warrants, and handling and emergency procedures. | Hazardous-substance inventory; safety data; leak-detection records; procedures | DOCUMENT_REVIEW; INSPECTION: sample inventory items on site and confirm detection and procedures |
| GC-04-6 | Egress and emergency access are unobstructed, and EPO and suppression interfaces cannot be actuated or inhibited without authority and record. | EPO and suppression-interface governance; inhibit logs; inspection | INSPECTION; DOCUMENT_REVIEW: inspect EPO guarding and review inhibit/restore records |
| GC-04-7 | No open life-safety Finding classified as an imminent hazard exists without interim protection and duty-holder acceptance. | Life-safety Finding register | DOCUMENT_REVIEW; INQUIRY: review open items with the duty holder |
| GC-04-8 | Every hazardous test proposed by the assessment has written authorisation, method statement, abort criteria and competent supervision before execution. | Test authorisations and method statements | DOCUMENT_REVIEW: verify before any test is executed; an unauthorised test is a Critical evidence nonconformance (AIDCF-008 §47) |

**Typical failure patterns**

- Arc-flash study predates UPS, busway or protection-setting changes, so labels understate incident energy.

- Lockout/tagout procedure exists but there is no evidence of its use for busway tap-off or PDU work.

- Lithium-ion UPS batteries retrofitted into rooms designed for valve-regulated lead-acid without a revised hazard assessment.

- Liquid-cooled halls with no handling or spill procedure for the glycol or dielectric fluid in use.

- Emergency power-off unguarded or able to be inhibited without authority or record.

- Suppression inhibited for maintenance with no restoration record.

- No refrigerant leak detection in chiller or machine rooms where the refrigerant class warrants it.

## CG-05 Resilient electrical supply

**Purpose and scope.** Protects continuity of electrical supply to IT and cooling loads at the declared redundancy, through utility loss, maintenance and accelerator-driven load transients. AI training loads change the classic sizing problem: synchronous load steps across thousands of accelerators stress UPS rectifiers, generators and protection in ways steady-state sizing does not reveal. Scope: Utility, distribution, UPS/BESS, generation, fuel, protection and power quality sufficient for the Service Outcomes across operating states.

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S5; E1+E2+E3+E4 (AIDCF-008 Part XIII). |
| Mandatory evidence | Single-line diagrams; capacity and load study including transient demand; protection coordination study and extracted settings; UPS/BESS runtime and battery state-of-health records; generator start, transfer and load test records; fuel autonomy calculation and replenishment contracts; power-quality measurements; EPMS coverage and alarm records; preventive-maintenance and deferred-work records; incident records. |
| CRITICAL mappings (AIDCF-007A registry v1.1, 8) | MCF-POW-001 Utility Capacity; MCF-POW-005 Generator Capacity; MCF-POW-006 Start Reliability; MCF-POW-007 Fuel Autonomy; MCF-POW-009 UPS Topology; MCF-POW-011 Runtime and Derating; MCF-POW-019 Transient Ride-Through; MCF-POW-020 Load-Step Response |
| SUPPORTING mappings (AIDCF-007A registry v1.1, 39) | MCF-CAP-012; MCF-CAP-013; MCF-CAP-014; MCF-CAP-016; MCF-CAP-017; MCF-CAP-019; MCF-DEP-005; MCF-DEP-009; MCF-POW-002; MCF-POW-003; MCF-POW-004; MCF-POW-008; MCF-POW-010; MCF-POW-012; MCF-POW-013; MCF-POW-014; MCF-POW-015; MCF-POW-016; MCF-POW-017; MCF-POW-018; MCF-POW-021; MCF-POW-022; MCF-POW-024; MCF-THM-003; MCF-ENV-008; MCF-ENV-021; MCF-CMP-003; MCF-OPS-009; MCF-OPS-010; MCF-OPS-012; MCF-OPS-013; MCF-OPS-021; MCF-OPS-023; MCF-RES-014; MCF-RES-017; MCF-RES-018; MCF-SUP-017; MCF-SUP-019; MCF-SEC-005 |
| Roll-up | Canonical roll-up rule (above). The gate is evaluated per power path serving the declared outcomes and in each operating state in the CRITICAL controls' stateCoverage (at least NORMAL and MAINTENANCE for concurrently maintainable designs). A path that is CONFORMING in NORMAL but UNKNOWN in MAINTENANCE leaves the gate UNKNOWN for outcomes relying on concurrent maintainability. |
| FAIL ceiling | NOT_ASSURED for every Service Outcome depending on the affected electrical path; LIMITED for the decision as a whole where unaffected paths remain. |
| UNKNOWN ceiling | LIMITED for outcomes depending on electrical continuity; RESILIENCE claims depending on the affected path are INCONCLUSIVE. |
| APPROVED_NA conditions | Only when the entire electrical supply up to and including the rack power interface is outside the boundary and provided under a contract evaluated as an external dependency under CG-03 with evidence rights (for example a colocation tenant assessing its compute only). CG-03 shall then be PASS for that dependency. |
| Reassessment triggers | IT load increase or new accelerator generation; Protection-setting change; Battery replacement or chemistry change; UPS, generator or switchgear firmware change; Utility connection change; Failed or anomalous test; Electrical incident. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-05-1 | For each power path, design and measured peak demand, including declared accelerator transient demand, are within the derated rating of utility connection, transformers, UPS, generation and distribution at the declared redundancy. | Capacity and load study; EPMS demand data; equipment ratings | ANALYSIS; RECONCILIATION: compare measured peaks and declared transients with derated ratings per component |
| GC-05-2 | The declared redundancy is realised as built and preserved in MAINTENANCE states, and single points of failure are listed with disposition. | Single-line diagrams; switching procedures; SPOF register | INSPECTION; ANALYSIS: walk each maintenance switching state on the SLD and confirm redundancy is preserved |
| GC-05-3 | A protection coordination study exists for the as-built configuration, installed settings match it, and selectivity is demonstrated for faults that would otherwise disconnect more than one redundant path. | Coordination study; settings extracted from relays and trip units | RECONCILIATION; SAMPLING: compare extracted settings with the study for a risk-based sample of devices |
| GC-05-4 | UPS/BESS runtime at actual load and current battery state of health exceeds generator start-and-transfer time with the margin declared in the capability profile, demonstrated by test. | Runtime test records; battery state-of-health data; transfer timing records | TEST; ANALYSIS: compare tested runtime at representative load with measured transfer time |
| GC-05-5 | On-site fuel autonomy at declared load meets the outcome's duration requirement, and replenishment arrangements (contracts, priority and access) are evidenced. | Fuel autonomy calculation; tank level records; replenishment contracts | ANALYSIS; DOCUMENT_REVIEW: recompute autonomy from consumption data and verify contract terms |
| GC-05-6 | Voltage, harmonics and transient behaviour at IT and cooling loads are within equipment tolerance under measured operation, including load steps. | Power-quality measurements; load-step test records | ANALYSIS; TEST: review measurements over a representative period and at least one load-step test |
| GC-05-7 | Generator start, transfer, retransfer and restoration sequences have been tested at representative load within the evidence currency window, with anomalies closed. | Transfer and restoration test records; anomaly closure records | DOCUMENT_REVIEW; REPERFORMANCE where authorised: review test records and anomaly closure |
| GC-05-8 | EPMS covers the critical electrical path with alarms reaching the operator, and preventive maintenance of that path is current with no deferred safety- or reliability-critical task. | EPMS point list and alarm records; maintenance and deferral records | RECONCILIATION; SAMPLING: compare EPMS points with the SLD and sample maintenance records |

**Typical failure patterns**

- UPS and generators sized on steady-state IT load without the synchronous load steps of large training jobs.

- Static bypass of a redundant UPS fed from a shared upstream bus, defeating the redundancy in bypass.

- Battery state of health degraded so that runtime at actual load is shorter than generator start and transfer.

- Generator tests on load banks only, never on the building load with its rectifier characteristics.

- Protection coordination study based on settings that have since changed.

- Rectifier harmonics or load steps causing generator instability that only appears on transfer.

- Fuel supply contract without priority or access provisions for a regional emergency.

## CG-06 Thermal continuity

**Purpose and scope.** Protects removal of heat from accelerators within the equipment envelope through every stage of the heat-removal path. Direct liquid cooling shortens the time between a cooling interruption and accelerator throttling or shutdown compared with air cooling, so ride-through and failover of pumps and CDUs, not only capacity, decide the gate. Scope: Heat-removal path (air, liquid, facility water, heat rejection) sufficient across operating states including transients.

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S5; E1+E2+E3+E4 (AIDCF-008 Part XIII). |
| Mandatory evidence | Heat-load model; thermal design and P&ID; capacity and resilient-capacity calculations at design ambient with seasonal derating; CDU, loop and facility-water telemetry (supply temperature, flow, differential pressure); failover, ride-through and leak-response test records; water-continuity evidence; leak detection and isolation records; coolant quality records; sensor calibration and control-stability records; maintenance-state capacity analysis. |
| CRITICAL mappings (AIDCF-007A registry v1.1, 7) | MCF-THM-002 Design Capacity; MCF-THM-003 Resilient Capacity; MCF-THM-004 Seasonal Derating; MCF-THM-010 CDU Capacity; MCF-THM-011 Secondary Loop Integrity; MCF-THM-013 Chiller Capacity; MCF-THM-015 Water Continuity |
| SUPPORTING mappings (AIDCF-007A registry v1.1, 46) | MCF-CAP-012; MCF-CAP-013; MCF-CAP-014; MCF-CAP-017; MCF-CAP-018; MCF-CAP-019; MCF-DEP-005; MCF-PHY-008; MCF-PHY-022; MCF-POW-019; MCF-THM-001; MCF-THM-005; MCF-THM-006; MCF-THM-007; MCF-THM-008; MCF-THM-009; MCF-THM-012; MCF-THM-014; MCF-THM-016; MCF-THM-017; MCF-THM-018; MCF-THM-019; MCF-THM-020; MCF-THM-021; MCF-THM-022; MCF-THM-023; MCF-THM-024; MCF-ENV-001; MCF-ENV-002; MCF-ENV-008; MCF-ENV-009; MCF-ENV-011; MCF-ENV-021; MCF-CMP-003; MCF-CMP-017; MCF-OPS-009; MCF-OPS-010; MCF-OPS-012; MCF-OPS-013; MCF-OPS-021; MCF-OPS-023; MCF-RES-014; MCF-RES-017; MCF-RES-018; MCF-SUP-017; MCF-SEC-005 |
| Roll-up | Canonical roll-up rule (above). The gate is evaluated per heat-removal path and per operating state, at the declared envelope (including design ambient). Evidence at steady low load does not support claims at full transient load. Where only states beyond the demonstrated envelope are UNKNOWN, the only route to a higher decision is an approved narrowing of the declared envelope (a boundary change, reassessed), never a conditional gate. |
| FAIL ceiling | NOT_ASSURED for Service Outcomes served by the affected heat-removal path at the declared load. |
| UNKNOWN ceiling | LIMITED for outcomes depending on the affected heat-removal path. |
| APPROVED_NA conditions | Only when the entire heat-removal path, including any in-rack and CDU elements, is outside the boundary and evaluated as an external dependency under CG-03 (for example an air-cooled tenant in a provider-managed facility). |
| Reassessment triggers | Rack-density or accelerator change; Cooling topology or controller change; Coolant or water-treatment change; Seasonal extreme beyond previously evidenced conditions; Failed failover or leak test; Thermal incident or throttling event. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-06-1 | The heat-load model reflects the declared envelope, including per-rack density and accelerator transient power, and allocates heat between air and liquid paths. | Heat-load model; envelope declaration | ANALYSIS; RECONCILIATION: compare model inputs with the envelope and with measured rack power |
| GC-06-2 | Design and resilient capacity of each heat-removal stage at the declared redundancy and design ambient, after seasonal derating, exceeds the modelled load. | Capacity calculations; equipment data; derating basis | ANALYSIS: recompute capacity per stage at design ambient with one unit (or the declared redundancy) out of service |
| GC-06-3 | Secondary-loop supply temperature, flow and differential pressure at the cold plates remain within the equipment manufacturer's specified envelope across measured operation, including at peak load. | CDU and loop telemetry over a representative period; manufacturer specification | ANALYSIS; SAMPLING: review telemetry against the specification at recorded peak loads |
| GC-06-4 | Loss of a CDU, pump, chiller or power feed to cooling has been tested, or analysed where testing is unsafe, showing supply temperature stays within the envelope until redundant capacity or controlled throttling takes over, including cooling ride-through on power interruption. | Failover and ride-through test records or competent analysis | TEST; SCENARIO_EXERCISE; ANALYSIS: review timed test results against the envelope |
| GC-06-5 | Water continuity for heat rejection and make-up water is evidenced for the outcome duration, including dependence on external water supply. | Water supply agreements; storage capacity and consumption data | ANALYSIS; DOCUMENT_REVIEW: recompute autonomy from consumption data |
| GC-06-6 | Leak detection and isolation cover liquid-cooled racks, manifolds and quick disconnects, and isolation has been demonstrated. | Detection coverage drawings; leak-response test records | INSPECTION; TEST: sample detection points and review isolation tests |
| GC-06-7 | Coolant chemistry, filtration and wetted-material compatibility are monitored against specification. | Coolant analysis records; specification | DOCUMENT_REVIEW; ANALYSIS: review sample results against limits and actions taken |
| GC-06-8 | Thermal control is stable, critical sensors are calibrated or plausibility-checked, and maintenance states preserve the capacity claimed. | Control-trend records; calibration records; maintenance-state analysis | ANALYSIS; SAMPLING: review control trends for oscillation and sample sensor calibrations |

**Typical failure patterns**

- CDUs sized at average rather than peak rack heat load.

- Secondary-loop pumps or CDU controls not on UPS, so a utility-to-generator transfer causes a thermal excursion before generation is online.

- Chiller or dry-cooler capacity at summer design ambient below the resilient requirement once derated.

- A single facility-water header or valve whose maintenance removes redundancy for a whole hall.

- Leak detection at floor level only, not at manifolds and quick disconnects.

- Sensor drift masking approach-temperature or flow degradation.

- Incompatible fluids or wetted materials introduced during expansion.

## CG-07 Critical control-system integrity

**Purpose and scope.** Protects the automated functions that change power, cooling or life-safety state. A control system can defeat a physically redundant plant: a single controller, a fail-to-stop default or an unrecorded setpoint change acts on both trains at once. Scope: BMS, EPMS, CDU, PLC/SCADA and automation function safely, fail safe, and are configured and governed.

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S4; E1+E2+E3+E4 (AIDCF-008 Part XIII). |
| Mandatory evidence | Control-system inventory and architecture identifying every automated function that can change power, cooling or life-safety state; logic and setpoint baselines with running-configuration comparisons; fail-safe test, factory or site acceptance test records; controller redundancy analysis; command-authority and access configuration with logs; alarm rationalisation and response records; manual-operation procedures and exercise records. |
| CRITICAL mappings (AIDCF-007A registry v1.1, 6) | MCF-POW-021 EPMS Coverage; MCF-THM-021 Control Stability; MCF-OPS-013 Alarm Rationalisation; MCF-SEC-005 BMS and EPMS Security; MCF-SEC-009 Security Zoning; MCF-SEC-023 Command Allowlisting |
| SUPPORTING mappings (AIDCF-007A registry v1.1, 26) | MCF-DEP-006; MCF-PHY-022; MCF-PHY-024; MCF-POW-006; MCF-POW-023; MCF-POW-024; MCF-THM-010; MCF-THM-022; MCF-OPS-011; MCF-OPS-017; MCF-OPS-019; MCF-RES-015; MCF-SEC-001; MCF-SEC-003; MCF-SEC-010; MCF-SEC-011; MCF-SEC-012; MCF-SEC-013; MCF-SEC-014; MCF-SEC-015; MCF-SEC-016; MCF-SEC-017; MCF-SEC-018; MCF-SEC-019; MCF-SEC-021; MCF-SEC-024 |
| Roll-up | Canonical roll-up rule (above). The gate is evaluated per automated function that can change the state of an in-scope power, cooling or life-safety system. Command authority (GC-07-5) shares evidence with CG-15; a defect found there is evaluated in both gates but counted once per control result (no double counting). |
| FAIL ceiling | NOT_ASSURED for Service Outcomes depending on the affected automated function. Claims based on demonstrated manual operation may be assessed separately and support at most LIMITED. |
| UNKNOWN ceiling | LIMITED for outcomes depending on the affected automation. |
| APPROVED_NA conditions | Only if no automated control system within the boundary can change the state of in-scope power, cooling or life-safety systems, demonstrated as a negative claim (AIDCF-008 §29). |
| Reassessment triggers | Controller logic, firmware or setpoint change; Control network change; New automated function or integration; Control-system incident or nuisance trip; Alarm philosophy change. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-07-1 | An inventory and architecture of BMS, EPMS, CDU controllers, PLC/SCADA and their networks exists and identifies every automated function that can change power, cooling or life-safety state. | Control-system inventory; architecture; function list | DOCUMENT_REVIEW; INSPECTION: sample field controllers and confirm they are in the inventory |
| GC-07-2 | Controller logic and setpoints are under configuration control with a current baseline, and running configuration matches the baseline on sampled controllers. | Logic and setpoint baselines; running-configuration exports | RECONCILIATION; SAMPLING: compare running configuration with baseline for a risk-based sample |
| GC-07-3 | On loss of controller, network or power, each critical automated function goes to its declared safe state, demonstrated by test or acceptance-test records. | Fail-safe test records; FAT/SAT records | TEST where authorised; DOCUMENT_REVIEW: review test evidence per function |
| GC-07-4 | No single controller, server or control network failure affects both redundant power or cooling paths. | Controller redundancy and common-controller analysis | ANALYSIS; INSPECTION: trace both trains to their controllers and networks |
| GC-07-5 | Write and command authority to controllers is limited to authorised identities and logged; engineering workstations and remote access are controlled (evaluated with CG-15). | Access configuration; command logs; remote-access records | RECONCILIATION; SAMPLING: compare accounts with authorised list and sample command logs |
| GC-07-6 | Critical alarms are rationalised, reach the operator and have a defined response. | Alarm rationalisation records; alarm logs; response procedures | ANALYSIS; OBSERVATION: review alarm rates and trace a sample of critical alarms to response |
| GC-07-7 | Manual operation procedures for loss of automation exist and have been exercised. | Manual-operation procedures; exercise records | DOCUMENT_REVIEW; SCENARIO_EXERCISE: review records or observe a walkthrough |

**Typical failure patterns**

- A single BMS server or controller network supervising both A and B chiller or CDU trains.

- CDU PLC that defaults to pump stop on loss of communication.

- Vendor default credentials on controllers or engineering workstations.

- Setpoints changed at the HMI without a change record.

- Alarm floods that bury critical alarms (contrary to ISA-18.2-style alarm management).

- Undocumented controller firmware or logic versions.

## CG-08 Compute, storage and network functional integrity

**Purpose and scope.** Protects the AI Service Outcomes themselves: usable accelerator capacity, fabric performance for collective communication, storage throughput for data and checkpoints, and data integrity. Facility outcomes can be fully met while the capability fails because the fabric is degraded or data is silently corrupted. Scope: Accelerators, storage and fabrics deliver the required function, performance and integrity.

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S4; E2+E3+E4 (AIDCF-008 Part XIII). |
| Mandatory evidence | Approved compute, firmware and driver baseline and fleet-conformance data; usable-capacity telemetry net of drained and failed nodes; fabric topology exports, path-diversity analysis and collective-communication performance on representative workloads; storage throughput, metadata and capacity telemetry; integrity checks and scrubbing records; error and degradation detection records with drain/repair actions; node, link and storage failure test records. |
| CRITICAL mappings (AIDCF-007A registry v1.1, 12) | MCF-CMP-006 Scale-Up Domain Integrity; MCF-CMP-009 Usable Accelerator Capacity; MCF-CMP-013 Firmware Baseline; MCF-CMP-019 Error and Degradation Detection; MCF-STO-005 Throughput and IOPS; MCF-STO-009 Data Integrity; MCF-STO-010 Metadata Integrity; MCF-STO-017 Checkpoint Durability; MCF-NET-001 Fabric Topology; MCF-NET-007 Congestion Control; MCF-NET-008 Collective Communication Performance; MCF-NET-009 Storage Fabric |
| SUPPORTING mappings (AIDCF-007A registry v1.1, 63) | MCF-CAP-006; MCF-CAP-007; MCF-CAP-022; MCF-ENV-001; MCF-ENV-003; MCF-ENV-004; MCF-CMP-001; MCF-CMP-002; MCF-CMP-003; MCF-CMP-004; MCF-CMP-005; MCF-CMP-008; MCF-CMP-010; MCF-CMP-011; MCF-CMP-012; MCF-CMP-014; MCF-CMP-015; MCF-CMP-017; MCF-CMP-018; MCF-CMP-020; MCF-CMP-021; MCF-CMP-023; MCF-STO-001; MCF-STO-002; MCF-STO-003; MCF-STO-006; MCF-STO-007; MCF-STO-008; MCF-STO-011; MCF-STO-012; MCF-STO-015; MCF-STO-021; MCF-STO-022; MCF-STO-023; MCF-NET-002; MCF-NET-003; MCF-NET-004; MCF-NET-005; MCF-NET-006; MCF-NET-010; MCF-NET-011; MCF-NET-012; MCF-NET-013; MCF-NET-017; MCF-NET-018; MCF-NET-019; MCF-NET-021; MCF-NET-022; MCF-NET-023; MCF-NET-024; MCF-RES-016; MCF-SUP-003; MCF-SUP-009; MCF-SUP-010; MCF-SUP-011; MCF-SUP-012; MCF-SUP-014; MCF-SUP-015; MCF-SEC-002; MCF-SEC-006; MCF-SEC-007; MCF-SEC-008; MCF-SEC-013 |
| Roll-up | Canonical roll-up rule (above). The gate is evaluated per cluster, fabric and storage tier delivering a Service Outcome. Fleet-scale controls are assessed per homogeneous population stratum (Part VI exceptions); a stratum outside tolerance makes the corresponding criterion not met for the outcomes it serves. |
| FAIL ceiling | NOT_ASSURED for Service Outcomes delivered by the affected cluster, fabric or storage tier. Facility outcomes defined at the rack interface are unaffected. |
| UNKNOWN ceiling | LIMITED for the Service Outcomes delivered by the affected cluster, fabric or storage tier. |
| APPROVED_NA conditions | Only for facility-only assessments in which Service Outcomes are defined at the facility interface (power and heat removal delivered to the rack) and no compute, storage or network is within the boundary. |
| Reassessment triggers | Firmware, driver or fabric software change; Cluster expansion or topology change; Storage tier or filesystem change; Rising error or drain rates; Performance regression against baseline. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-08-1 | An approved baseline for accelerators, nodes, firmware, drivers and rack-scale composition exists, and fleet conformance to it is measured. | Baseline record; fleet inventory and conformance report | RECONCILIATION; SAMPLING: compare fleet inventory with baseline per stratum |
| GC-08-2 | Usable accelerator capacity, net of failed, drained and reserved nodes, meets the capacity outcome over the assessment period. | Scheduler and health telemetry; capacity outcome | ANALYSIS: compute usable capacity over the period against the outcome |
| GC-08-3 | As-configured fabric topology matches design, and path diversity, oversubscription and collective-communication performance meet the performance outcome on representative workloads. | Topology exports; path analysis; benchmark and production telemetry | RECONCILIATION; TEST; ANALYSIS: compare exports with design and review representative benchmarks |
| GC-08-4 | Storage throughput, metadata performance and capacity headroom meet the data and checkpoint outcome, measured. | Storage telemetry; checkpoint timing records | ANALYSIS; TEST: review measured throughput and checkpoint duration at representative scale |
| GC-08-5 | Data and metadata integrity mechanisms (checksums, scrubbing) operate, and integrity errors are detected and handled. | Scrub and integrity-check records; error-handling records | DOCUMENT_REVIEW; SAMPLING: confirm mechanisms enabled and sample error handling |
| GC-08-6 | Error and degradation detection for accelerators, links and storage media operates with defined drain and repair actions. | Error-detection configuration; drain and repair records | RECONCILIATION; SAMPLING: trace a sample of detected errors to actions |
| GC-08-7 | Failure of a node, link or switch, or storage server within the declared fault domain has been tested and degrades performance within tolerance. | Failure-injection or incident records | TEST; SCENARIO_EXERCISE: review timed results against the performance tolerance |

**Typical failure patterns**

- Mixed firmware or driver versions within a scale-up domain.

- Fabric running with failed links masked by adaptive routing until a large collective job exposes the loss.

- Metadata servers that bottleneck synchronous checkpoint writes.

- Silent data corruption not detected because checksums or scrubbing are disabled for performance.

- Usable capacity reported as installed capacity, ignoring drained, failed or reserved nodes.

## CG-09 Failure containment

**Purpose and scope.** Protects the assumption, implicit in every tolerance, that a failure stays where it starts. AI facilities couple domains tightly: an electrical event can trip cooling pumps, which throttles accelerators, which fails synchronous jobs across a whole cluster. Containment must be demonstrated across domains, not only within each. Scope: Fault domains, isolation and blast-radius limits prevent propagation beyond tolerance.

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S4; E1+E2+E4+E7 (AIDCF-008 Part XIII). |
| Mandatory evidence | Fault-domain model for power, cooling, compute, network, storage and control plane with outcome impact per domain; containment design (selectivity, isolation valves, partitioning, failure domains, segmentation) and as-built evidence; blast-radius analysis for credible single failures and identified common modes; isolation tests, incident evidence or competent analysis; cross-domain propagation analysis for relevant compound scenarios (AIDCF-004); workload and tenant segregation evidence. |
| CRITICAL mappings (AIDCF-007A registry v1.1, 9) | MCF-PHY-010 Fire Zones; MCF-POW-014 Selective Coordination; MCF-THM-020 Isolation and Drainage; MCF-CMP-008 Fault-Domain Design; MCF-STO-015 Erasure Coding; MCF-NET-004 Fabric Fault-Domain Design; MCF-RES-005 Fault-Domain Definition; MCF-RES-007 Blast Radius; MCF-RES-008 Isolation Validation |
| SUPPORTING mappings (AIDCF-007A registry v1.1, 42) | MCF-CAP-020; MCF-DEP-003; MCF-DEP-005; MCF-DEP-006; MCF-DEP-007; MCF-DEP-013; MCF-DEP-019; MCF-DEP-020; MCF-PHY-002; MCF-PHY-007; MCF-PHY-009; MCF-PHY-011; MCF-PHY-021; MCF-PHY-024; MCF-POW-003; MCF-POW-009; MCF-POW-012; MCF-THM-003; MCF-THM-011; MCF-THM-016; MCF-THM-019; MCF-ENV-023; MCF-CMP-006; MCF-CMP-007; MCF-CMP-015; MCF-STO-008; MCF-STO-014; MCF-STO-019; MCF-NET-002; MCF-NET-007; MCF-NET-012; MCF-NET-021; MCF-OPS-015; MCF-OPS-023; MCF-RES-001; MCF-RES-002; MCF-RES-003; MCF-RES-006; MCF-RES-018; MCF-SUP-015; MCF-SEC-009; MCF-SEC-019 |
| Roll-up | Canonical roll-up rule (above). The gate is evaluated per fault domain and per compound scenario in scope. Where testing a boundary is unsafe, competent analysis (E7) with stated limitations may meet GC-09-4 only for DESIGN and IMPLEMENTATION claims; EFFECTIVENESS and RESILIENCE claims then remain UNKNOWN. |
| FAIL ceiling | NOT_ASSURED for RESILIENCE claims, and for any Service Outcome whose tolerance assumes the defeated containment; LIMITED for the decision as a whole. |
| UNKNOWN ceiling | INCONCLUSIVE for RESILIENCE claims of the affected outcomes; LIMITED for the decision as a whole. |
| APPROVED_NA conditions | Never. |
| Reassessment triggers | Fault-domain or topology redesign; Expansion that alters zoning or loop allocation; An incident whose impact exceeded its expected domain; New compound scenario identified in AIDCF-004 analysis. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-09-1 | Fault domains are defined for power, cooling, compute, network, storage and control plane, with the outcome impact of losing each stated. | Fault-domain model | DOCUMENT_REVIEW; ANALYSIS: confirm every domain type is defined with outcome impact |
| GC-09-2 | Containment boundaries are implemented as designed (electrical selectivity, cooling isolation, fabric partitioning, storage failure domains, control-plane segmentation). | Containment design; as-built and configuration evidence | RECONCILIATION; INSPECTION: sample boundaries and compare with design |
| GC-09-3 | The blast radius of each credible single failure and each identified common mode is within the impact tolerance of the affected outcomes. | Blast-radius analysis; impact tolerances | ANALYSIS: compare computed impact with tolerance per scenario |
| GC-09-4 | Isolation is validated by test, by documented incident evidence or, where testing is unsafe, by competent analysis with stated limitations. | Isolation test records; incident records; analysis | TEST; DOCUMENT_REVIEW; ANALYSIS: review validation per boundary |
| GC-09-5 | Cross-domain propagation paths are analysed for the compound scenarios relevant to the capability. | Propagation analysis; scenario set | ANALYSIS; SCENARIO_EXERCISE: trace each relevant scenario across domains |
| GC-09-6 | Workload and tenant segregation prevents a fault or contention in one partition from breaching another partition's tolerance. | Partitioning and isolation configuration; contention telemetry | RECONCILIATION; ANALYSIS: review configuration and contention evidence |

**Typical failure patterns**

- A fire or water zone that contains both power paths or both cooling trains.

- A single cooling loop serving racks in different compute fault domains.

- A scale-up domain spanning racks fed from the same PDU or CDU.

- Storage erasure-coding failure domain set at node level although rack-level failures are credible.

- A flat management network through which a fault or compromise can reach all controllers.

## CG-10 Recovery readiness

**Purpose and scope.** Protects the ability to restore Service Outcomes within recovery tolerances after a disruption. Recovery is cross-domain and ordered: cooling before compute, network and identity before provisioning, storage before job restart. A plan that has not been exercised at representative scale supports DESIGN only. Scope: Restoration of outcomes (power, cooling, compute, data and checkpoint, network, control plane) within tolerance is planned and tested.

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S5; E1+E2+E3+E4 (AIDCF-008 Part XIII). |
| Mandatory evidence | Recovery outcomes and minimum service outcome; recovery dependency and sequencing plans for power, cooling, compute, storage, network and control plane; configuration-restoration sources with integrity protection; checkpoint durability and immutable recovery copy; component and integrated scenario test records with measured times; defect and retest records; spares, support and staffing evidence. |
| CRITICAL mappings (AIDCF-007A registry v1.1, 11) | MCF-POW-024 Black-Start and Restoration; MCF-THM-024 Thermal Recovery; MCF-CMP-023 Node Rebuild; MCF-STO-016 Immutable Recovery Copy; MCF-STO-018 Restart Readiness; MCF-STO-020 Recovery Validation; MCF-NET-015 OOB Resilience; MCF-RES-013 Recovery Dependencies; MCF-RES-014 Recovery Sequencing; MCF-RES-016 Data and Checkpoint Recovery; MCF-RES-018 Integrated Scenario Tests |
| SUPPORTING mappings (AIDCF-007A registry v1.1, 56) | MCF-CAP-008; MCF-CAP-016; MCF-CAP-019; MCF-CAP-020; MCF-DEP-004; MCF-DEP-010; MCF-DEP-011; MCF-DEP-012; MCF-DEP-015; MCF-DEP-016; MCF-PHY-003; MCF-POW-004; MCF-POW-008; MCF-CMP-011; MCF-CMP-016; MCF-CMP-022; MCF-STO-002; MCF-STO-003; MCF-STO-004; MCF-STO-010; MCF-STO-013; MCF-STO-014; MCF-STO-017; MCF-STO-019; MCF-NET-009; MCF-NET-014; MCF-NET-016; MCF-NET-020; MCF-NET-021; MCF-NET-022; MCF-NET-024; MCF-OPS-001; MCF-OPS-005; MCF-OPS-014; MCF-OPS-020; MCF-RES-001; MCF-RES-002; MCF-RES-003; MCF-RES-009; MCF-RES-010; MCF-RES-011; MCF-RES-012; MCF-RES-015; MCF-RES-017; MCF-RES-019; MCF-RES-020; MCF-RES-021; MCF-SUP-005; MCF-SUP-008; MCF-SUP-017; MCF-SUP-018; MCF-SUP-019; MCF-SEC-004; MCF-SEC-008; MCF-SEC-019; MCF-SEC-024 |
| Roll-up | Canonical roll-up rule (above). Recovery evidence is evaluated against the recovery tolerances in CG-01. A recovery plan with only component tests meets GC-10-5 only if no cross-domain dependency exists for the outcome; otherwise an integrated exercise is required. |
| FAIL ceiling | NOT_ASSURED for recovery outcomes and for RESILIENCE claims of the affected outcomes; LIMITED for the decision as a whole. |
| UNKNOWN ceiling | LIMITED; recovery outcomes are INCONCLUSIVE. DESIGN claims about recovery may still be reported. |
| APPROVED_NA conditions | Not permitted where any Service Outcome in the decision question declares a recovery tolerance or the target Assurance Level is AL4 or higher; otherwise only with approved rationale. |
| Reassessment triggers | Change to recovery architecture, tooling or dependencies; Failed or partially successful exercise; Real recovery event; Scale change of the cluster or storage; Expiry of the exercise currency window. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-10-1 | Recovery outcomes (recovery-time and recovery-point tolerances and minimum service outcome) exist for each Service Outcome in scope. | Recovery outcome specification | DOCUMENT_REVIEW: confirm tolerances per outcome |
| GC-10-2 | Recovery dependencies and sequencing for power, cooling, compute, storage, network and control plane are documented and mutually consistent. | Recovery plans; dependency and sequence maps | ANALYSIS: check sequences for circular or missing prerequisites across domains |
| GC-10-3 | Configuration-restoration sources are current, integrity protected and restorable independently of the failed environment. | Backup and image inventory; integrity records; restore tests | RECONCILIATION; TEST: compare backups with current configuration and review independent restore |
| GC-10-4 | Checkpoint durability and an immutable recovery copy exist, and restore to a usable training state has been demonstrated. | Checkpoint and immutable-copy configuration; restore test records | TEST; DOCUMENT_REVIEW: review restore to a resumed job at representative scale |
| GC-10-5 | Recovery has been exercised through component tests and at least one integrated cross-domain scenario at representative scale within the evidence currency window, with measured times compared against tolerance. | Exercise records with timings | SCENARIO_EXERCISE; DOCUMENT_REVIEW: compare measured times with tolerances |
| GC-10-6 | Defects from exercises are tracked to closure with retest. | Defect register; retest records | SAMPLING: trace a sample of defects to closure and retest |
| GC-10-7 | Spares, vendor support and staff required for recovery are available within the recovery time. | Spares inventory; support contracts; staffing rota | DOCUMENT_REVIEW; INQUIRY: compare availability with recovery-time assumptions |

**Typical failure patterns**

- Recovery tested per component but never as an integrated, ordered sequence.

- Restoration depends on identity, DNS or provisioning services hosted in the failed domain.

- Checkpoint restore tested on a small job only, not at the scale of the outcome.

- Black-start sequence depends on a BMS or EPMS that itself needs restored power.

- Golden images and configuration backups stored only on the cluster storage they are needed to rebuild.

## CG-11 Evidence sufficiency

**Purpose and scope.** Protects the integrity of the evidence base behind the decision. It does not re-score individual controls: a decisive claim honestly recorded as UNKNOWN because its evidence is below floor is handled by that control's gate. CG-11 fails when evidence is misrepresented, misclassified as meeting a floor it does not meet, or compromised. Scope: Evidence for decisive claims meets the AIDCF-008 floors (meta-gate across all controls).

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S4; E1+E7 (AIDCF-008 Part XIII). |
| Mandatory evidence | Evidence Requirement Profiles applied (AIDCF-007A registry version); EvidenceAssessments for decisive claims; evidence manifest for the decision snapshot; record of substitutions and approvals; lineage and deduplication analysis; evidence nonconformance register (AIDCF-008 §47). |
| Control mappings | None: meta-gate evaluated across all controls and gate criteria. |
| Roll-up | Meta-gate evaluated across all controls; not mapped per control. A decisive claim is any mandatory claim type of a control with a CRITICAL mapping to an in-scope gate, and any gate criterion. FAIL if GC-11-2, GC-11-4 or GC-11-5 is demonstrated not met; UNKNOWN if GC-11-1, GC-11-3 or GC-11-6 is incomplete, or a U7 integrity UNKNOWN on decisive evidence is unresolved; PASS otherwise. |
| FAIL ceiling | INCONCLUSIVE for the whole decision. Any previously issued decision relying on the affected evidence is SUSPENDED, and the matter is escalated as an evidence nonconformance (AIDCF-008 §47). |
| UNKNOWN ceiling | LIMITED. |
| APPROVED_NA conditions | Never. |
| Reassessment triggers | Discovery of an evidence nonconformance; Change of Evidence Requirement Profile version; Evidence repository or tooling change; Challenge or appeal to a decisive claim. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-11-1 | Every decisive claim has a recorded EvidenceAssessment with quality vector, sufficiency against the profile floor and reviewer. | EvidenceAssessments; list of decisive claims | RECONCILIATION: compare the decisive-claim list with recorded assessments |
| GC-11-2 | No decisive claim is recorded CONFORMING or PARTIAL on a package below its sufficiency floor or with a mandatory item below its quality floor. | EvidenceAssessments; profiles | ANALYSIS; SAMPLING: re-evaluate a risk-based sample of decisive claims against their floors |
| GC-11-3 | Mandatory items are present, or substituted only by a listed acceptable alternative with approval rationale. | Evidence manifests; substitution approvals | RECONCILIATION: compare manifests with profile mandatory items |
| GC-11-4 | Duplicate lineage is not counted as corroboration, and AI-generated or derived content is not used as independent corroboration of its own sources. | Lineage records; derived-evidence records | ANALYSIS: trace lineage of corroborating items for a sample of decisive claims |
| GC-11-5 | No Critical evidence nonconformance (fabrication, falsification, concealed conflict, custody breach affecting a critical claim) exists. | Evidence nonconformance register; custody records | DOCUMENT_REVIEW; INQUIRY; ANALYSIS of custody events for decisive evidence |
| GC-11-6 | An immutable EvidenceManifest exists for the decision snapshot and references all evidence underlying decisive claims. | EvidenceManifest with integrity protection | RECONCILIATION: verify manifest integrity and completeness against decisive claims |

**Typical failure patterns**

- OPERATION claims marked CONFORMING with only policies and procedures (E1) as evidence.

- The same telemetry export cited twice as independent corroboration.

- A vendor attestation accepted as independent evidence (E5) without scope, method or exclusions.

- AI-generated summaries of logs used as evidence that the logs were reviewed.

- Evidence manifests that can be edited after the decision snapshot.

## CG-12 Critical UNKNOWN

**Purpose and scope.** Protects visibility and governance of the uncertainties that could change a gate or the decision. A PASS confirms that every US4 and US5 UNKNOWN is registered, correctly graded and dispositioned; it does not lift the ceilings those UNKNOWNs impose. Scope: No unresolved US4 or US5 UNKNOWN without disposition (meta-gate across all controls).

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S3; E1+E7 (AIDCF-008 Part XIII). |
| Mandatory evidence | UNKNOWN register with type, severity, determining test, owner, evidence request, target date and disposition; independent review records of severity assignments; severity history; decision record and draft assurance statement showing UNKNOWN disclosure. |
| Control mappings | None: meta-gate evaluated across all controls and gate criteria. |
| Roll-up | Meta-gate evaluated across all controls and gate criteria; not mapped per control. Disposition means one of: (a) resolved with evidence; (b) removed from scope by an approved boundary change disclosed as a limitation; (c) carried with a named owner, evidence request, target date and the applicable decision ceiling recorded on the decision. FAIL if GC-12-2 or GC-12-4 is demonstrated not met, or a US4/US5 UNKNOWN is omitted from the register or report; UNKNOWN if any US4/US5 UNKNOWN lacks disposition or severity review is incomplete; PASS otherwise. |
| FAIL ceiling | INCONCLUSIVE for the whole decision; escalated as an evidence nonconformance (concealed UNKNOWN, AIDCF-008 §47). |
| UNKNOWN ceiling | LIMITED; INCONCLUSIVE if any undispositioned UNKNOWN is US5. |
| APPROVED_NA conditions | Never. |
| Reassessment triggers | New US4/US5 UNKNOWN raised; Severity change; Target date for a carried UNKNOWN passed; Boundary change used as a disposition. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-12-1 | Every UNKNOWN result, gate UNKNOWN and evidence gap has an UNKNOWN Record with type, severity and the determining test. | UNKNOWN register; control and gate results | RECONCILIATION: compare UNKNOWN results and gaps with register entries |
| GC-12-2 | Every US3, US4 and US5 severity has been reviewed by the independent reviewer, and no severity has been downgraded without new evidence or an approved boundary change. | Review records; severity history | DOCUMENT_REVIEW: verify review and justification for each downgrade |
| GC-12-3 | Every US4 and US5 UNKNOWN has a disposition (resolved, approved boundary change, or carried with owner, evidence request, target date and ceiling). | UNKNOWN register dispositions | DOCUMENT_REVIEW: confirm disposition fields complete for each US4/US5 |
| GC-12-4 | No UNKNOWN is encoded as pass, zero, NOT_APPLICABLE or accepted risk in results, scores or reports. | Results; score snapshot; reports | ANALYSIS: automated and sampled checks of encodings |
| GC-12-5 | US4 and US5 UNKNOWNs are reported in the decision record and assurance statement with their effect. | Decision record; draft assurance statement | RECONCILIATION: compare register with decision record and statement |

**Typical failure patterns**

- UNKNOWN recoded as PARTIAL so that a score can be produced.

- Provider evidence that was refused recorded as NOT_APPLICABLE.

- Severity set to US2 on the evidence holder's assurance alone.

- UNKNOWNs present in workpapers but missing from the executive report and assurance statement.

## CG-13 Responsibility and authority

**Purpose and scope.** Protects accountable action at the moments that matter: state transitions, emergencies, risk acceptance and the Assurance Decision itself. Evidence of capability is of little value if nobody holds the authority to act on it, or if authority sits informally with a vendor. Scope: Every critical function and dependency has an accountable owner and decision authority.

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S3; E1+E6 (AIDCF-008 Part XIII). |
| Mandatory evidence | RACI for Required Functions and material dependencies; provider/operator/tenant responsibility clauses including incident and maintenance periods; decision-rights register for operating-state transitions; risk-acceptance delegations and signed acceptances; 24x7 escalation paths and test records; designation of the accountable decision owner and evidence of independence from the assessment team. |
| CRITICAL mappings (AIDCF-007A registry v1.1, 7) | MCF-GOV-002 Decision Rights; MCF-GOV-005 RACI and Role Ownership; MCF-GOV-006 Critical Function Accountability; MCF-GOV-007 Risk Acceptance Authority; MCF-CAP-002 Capability Ownership; MCF-DEP-018 Provider Boundary; MCF-OPS-002 Role Clarity |
| SUPPORTING mappings (AIDCF-007A registry v1.1, 28) | MCF-GOV-001; MCF-GOV-003; MCF-GOV-008; MCF-GOV-011; MCF-GOV-015; MCF-GOV-016; MCF-GOV-022; MCF-DEP-008; MCF-DEP-015; MCF-DEP-019; MCF-DEP-022; MCF-PHY-012; MCF-OPS-001; MCF-OPS-004; MCF-OPS-005; MCF-OPS-012; MCF-OPS-014; MCF-OPS-024; MCF-RES-004; MCF-RES-019; MCF-RES-021; MCF-RES-022; MCF-SUP-005; MCF-SUP-021; MCF-SUP-024; MCF-SEC-001; MCF-EVA-002; MCF-EVA-019 |
| Roll-up | Canonical roll-up rule (above). Ownership is evaluated per Required Function and per material dependency in the CG-03 model. Interview evidence (E6) shall corroborate documentary allocation for state-transition authority. |
| FAIL ceiling | NOT_ASSURED for OPERATION, EFFECTIVENESS and RESILIENCE claims about the unowned function or dependency; LIMITED for the decision as a whole. If GC-13-6 is not met, no decision advances beyond the RECOMMENDED lifecycle state. |
| UNKNOWN ceiling | LIMITED. |
| APPROVED_NA conditions | Never. |
| Reassessment triggers | Organisational change; Provider or operator change; Change of decision owner; Incident revealing unclear authority. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-13-1 | Every Required Function and every material dependency has a named accountable owner (role and individual). | RACI; dependency register | RECONCILIATION: compare functions and dependencies with owner assignments |
| GC-13-2 | Provider, tenant and operator responsibilities at each boundary interface are allocated in contract or agreed RACI, including during incidents and maintenance. | Contracts; agreed RACI | DOCUMENT_REVIEW: verify allocation per interface and state |
| GC-13-3 | Decision rights for operating-state transitions (generator transfer, emergency shutdown, workload throttling, load shedding) are assigned and known to operations staff. | Decision-rights register; interviews | DOCUMENT_REVIEW; INQUIRY: corroborate with a sample of shift staff |
| GC-13-4 | Risk-acceptance authority is defined with limits, and every accepted risk is signed by a holder of that authority. | Delegations; risk acceptances | SAMPLING: compare signatories of accepted risks with delegations |
| GC-13-5 | 24x7 escalation paths are defined and have been tested. | Escalation procedure; test or exercise records | DOCUMENT_REVIEW; SCENARIO_EXERCISE: review escalation tests |
| GC-13-6 | The Assurance Decision has a named accountable decision owner with authority for the decision question who is independent of the assessment team. | Decision-owner designation; independence declaration | DOCUMENT_REVIEW; INQUIRY: confirm authority and independence |

**Typical failure patterns**

- CDU and secondary-loop ownership ambiguous between facility and IT teams.

- Out-of-band management network owned by nobody.

- A vendor holding de facto authority over a critical system without a contractual basis.

- Risks accepted by a project manager without delegated authority.

- Emergency shutdown authority unclear outside business hours.

## CG-14 Change control

**Purpose and scope.** Protects the currency of everything else: evidence describes a state, and an uncontrolled change silently invalidates it. In AI facilities, fleet-wide firmware pushes, rack-density increases and protection-setting changes are frequent and consequential. Scope: Material changes are controlled, impact-assessed and validated.

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S4; E1+E2+E3+E4 (AIDCF-008 Part XIII). |
| Mandatory evidence | Configuration baselines; change records reconciled with configuration and telemetry; impact assessments; approvals; test, rollback and post-change validation records; temporary-configuration register; emergency-change reviews; records of evidence invalidated by change. |
| CRITICAL mappings (AIDCF-007A registry v1.1, 7) | MCF-CAP-023 Material Change Impact; MCF-CMP-015 Upgrade Testing; MCF-NET-022 Configuration Management; MCF-OPS-006 Method Statements; MCF-OPS-017 Configuration Baseline; MCF-OPS-018 Change Assessment; MCF-OPS-020 Rollback and Validation |
| SUPPORTING mappings (AIDCF-007A registry v1.1, 35) | MCF-GOV-010; MCF-GOV-011; MCF-GOV-012; MCF-GOV-018; MCF-CAP-003; MCF-CAP-022; MCF-CAP-024; MCF-DEP-023; MCF-PHY-006; MCF-POW-015; MCF-POW-023; MCF-THM-012; MCF-THM-023; MCF-ENV-008; MCF-CMP-004; MCF-CMP-013; MCF-CMP-016; MCF-CMP-021; MCF-STO-012; MCF-NET-019; MCF-OPS-002; MCF-OPS-003; MCF-OPS-005; MCF-OPS-016; MCF-OPS-019; MCF-RES-015; MCF-RES-020; MCF-RES-023; MCF-RES-024; MCF-SUP-013; MCF-SUP-015; MCF-SUP-022; MCF-SEC-015; MCF-SEC-022; MCF-EVA-022 |
| Roll-up | Canonical roll-up rule (above). Changes are evaluated for the period between the earliest evidence observation date relied on and the decision date. At AL2 the gate is evaluated against control of the design baseline. |
| FAIL ceiling | Affected evidence is invalidated (STALE, U3) and claims relying on the post-change state become UNKNOWN; any prior decision covering the affected scope is SUSPENDED; LIMITED for the decision as a whole, or NOT_ASSURED where the uncontrolled change is demonstrated to have defeated a safeguard. |
| UNKNOWN ceiling | LIMITED. |
| APPROVED_NA conditions | Never. |
| Reassessment triggers | Any material change after the evidence observation date; Discovery of unrecorded configuration drift; Emergency change; Change-process tooling change. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-14-1 | Configuration baselines exist for in-scope facility and IT systems. | Baselines | DOCUMENT_REVIEW: confirm baseline per system with version and date |
| GC-14-2 | Material changes since the evidence observation dates are identified by reconciling change records with configuration and telemetry evidence. | Change records; configuration and telemetry evidence | RECONCILIATION: detect unrecorded changes by comparing configuration over time |
| GC-14-3 | Each material change has an impact assessment covering capacity, redundancy, protection, fault domain and recovery effects, and approval by the authorised party. | Impact assessments; approvals | SAMPLING: review a risk-based sample of material changes |
| GC-14-4 | Changes were tested, with a rollback plan and recorded post-change validation. | Test, rollback and validation records | SAMPLING; DOCUMENT_REVIEW: trace sampled changes to validation |
| GC-14-5 | Temporary configurations are registered, time-bound, and removed or converted under change control. | Temporary-configuration register; inspection | INSPECTION; RECONCILIATION: compare site state with the register |
| GC-14-6 | Emergency changes are retrospectively reviewed and approved. | Emergency-change records and reviews | DOCUMENT_REVIEW: confirm reviews for all emergency changes in the period |
| GC-14-7 | Evidence affected by a material change is marked STALE and dependent Control Assessments are reopened. | Evidence lifecycle records; assessment reopen records | RECONCILIATION: compare changes with evidence status |

**Typical failure patterns**

- Firmware rolled fleet-wide by automation without change approval.

- Protection settings changed during commissioning and not reflected in the baseline or study.

- UPS left in bypass after maintenance.

- Rack-density increases treated as routine operations rather than material change.

- Temporary chillers or feeds that become permanent without design review.

## CG-15 Integrated digital authority over infrastructure

**Purpose and scope.** Protects against consequential action by any identity, human, vendor, service or automated agent, reaching facility or AI infrastructure through a digital path. One identity plane often spans BMS, EPMS, cluster managers and out-of-band management; an unbounded path is a common mode across every physical gate. Scope: Identity, privilege, remote access and control-plane reach over facility and AI infrastructure are bounded, monitored and recoverable.

| **Field** | **Specification** |
|---|---|
| Evidence floor and classes | S4; E2+E3+E4+E7 (AIDCF-008 Part XIII). |
| Mandatory evidence | Inventory of identities able to issue consequential commands; privileged and break-glass access configuration and logs; segmentation design and reachability analysis; remote and third-party access activation, session and revocation records; automation and agent authority configuration with allowlists and approval controls; detection coverage and response records; identity and control-plane recovery tests. |
| CRITICAL mappings (AIDCF-007A registry v1.1, 7) | MCF-SUP-021 Support Identity; MCF-SUP-022 Activation and Approval; MCF-SEC-003 Privileged Access; MCF-SEC-006 Cluster Manager Security; MCF-SEC-010 Management-Plane Segmentation; MCF-SEC-012 Remote Access; MCF-SEC-021 Agent or Automation Authority |
| SUPPORTING mappings (AIDCF-007A registry v1.1, 42) | MCF-DEP-002; MCF-DEP-012; MCF-DEP-020; MCF-PHY-009; MCF-PHY-013; MCF-POW-021; MCF-THM-021; MCF-CMP-002; MCF-CMP-007; MCF-CMP-010; MCF-CMP-013; MCF-STO-016; MCF-NET-012; MCF-NET-013; MCF-NET-014; MCF-NET-015; MCF-NET-016; MCF-SUP-003; MCF-SUP-007; MCF-SUP-013; MCF-SUP-014; MCF-SUP-016; MCF-SUP-023; MCF-SUP-024; MCF-SEC-001; MCF-SEC-002; MCF-SEC-004; MCF-SEC-005; MCF-SEC-007; MCF-SEC-008; MCF-SEC-009; MCF-SEC-011; MCF-SEC-013; MCF-SEC-014; MCF-SEC-016; MCF-SEC-017; MCF-SEC-018; MCF-SEC-019; MCF-SEC-020; MCF-SEC-022; MCF-SEC-023; MCF-SEC-024 |
| Roll-up | Canonical roll-up rule (above). Evaluated per authority path from an identity to a consequential control function, using AIDCF-005 integrated authority semantics. Reachability (E7) alone does not demonstrate authority; E2 configuration and E3 logs are required for each path relied on. Where an unverified path reaches the scope of two or more other gates, the UNKNOWN is US5. |
| FAIL ceiling | NOT_ASSURED for every Service Outcome reachable through the unbounded authority path; LIMITED for the decision as a whole. |
| UNKNOWN ceiling | LIMITED; INCONCLUSIVE where the unverified authority reaches the scope of two or more other gates (US5). |
| APPROVED_NA conditions | Only if discovery demonstrates that no digital path (network, remote access, out-of-band, removable media or vendor tool) exists from any identity to in-scope control functions, recorded as a negative claim (AIDCF-008 §29). |
| Reassessment triggers | New remote-access path or provider; Identity-platform change; New automation or agent with infrastructure authority; Security incident or credential compromise; Segmentation change. |

**Gate criteria**

| **ID** | **Criterion** | **Evidence** | **Test method** |
|---|---|---|---|
| GC-15-1 | Identities (human, machine, vendor and automation) able to issue consequential commands to facility control systems, cluster managers, fabric or storage controllers and out-of-band management are inventoried. | Identity and entitlement exports | RECONCILIATION: compare entitlements on target systems with the inventory |
| GC-15-2 | Privileged and break-glass access is least-privilege, approved, time-bound and logged. | Privileged-access configuration; approvals; logs | SAMPLING: trace a sample of privileged sessions to approvals |
| GC-15-3 | Management and control planes are segmented from tenant and corporate networks, and reachability analysis shows no unapproved path to consequential control functions. | Segmentation design; firewall and routing configuration; reachability analysis | ANALYSIS; TEST where authorised: verify reachability against approved paths |
| GC-15-4 | Remote and third-party access requires activation, approval, session monitoring and timely revocation. | Remote-access records; session recordings or logs; revocation records | SAMPLING: trace a sample of vendor sessions end to end |
| GC-15-5 | Automated and AI-enabled actions on infrastructure are bounded by allowlists, approval controls and safe rollback. | Automation authority configuration; approval records; rollback tests | RECONCILIATION; TEST: compare permitted actions with allowlists and review rollback tests |
| GC-15-6 | Authentication and command activity on control planes is monitored, with defined response. | Detection coverage map; alert and response records | ANALYSIS; SAMPLING: confirm coverage and sample responses |
| GC-15-7 | Recovery of identity and control-plane authority after loss of the identity provider or credential compromise is planned and tested. | Recovery procedures; test records | SCENARIO_EXERCISE; DOCUMENT_REVIEW: review exercise results |

**Typical failure patterns**

- The same directory forest used for corporate IT and the BMS/EPMS.

- Persistent vendor VPN with standing access to controllers.

- Out-of-band console servers with shared passwords.

- A cluster automation service account with power control over every node's baseboard management controller.

- An AI operations agent with write access to cooling setpoints and no allowlist or approval step.


# Part IX - UNKNOWN severity and its decision effects

**UNKNOWN is treated by consequence, not by a points deduction.**

Every UNKNOWN Record carries a type (U1–U10, AIDCF-008 §35) and a severity determined by the first test that applies, top-down (AIDCF-008 §35A gives per-type grading guidance):

| **Code** | **Name** | **Test (first that applies, top-down)** | **Decision effect** |
|---|---|---|---|
| US5 | Systemic | Affects the boundary, a Capability Instance or Service Outcome definition, or two or more gates. | Decision ≤ INCONCLUSIVE (for the affected outcomes, or the decision as a whole where the boundary or Capability Instance is affected). |
| US4 | Critical | Affects a gate-critical control or a gate criterion (CG-12 trigger). | Gate → UNKNOWN; decision ≤ LIMITED or INCONCLUSIVE per that gate's UNKNOWN ceiling. |
| US3 | Material | Could change a control result or a decision condition but affects no gate. | Decision ≤ CONDITIONALLY_ASSURED for affected outcomes; a condition is recorded. |
| US2 | Moderate | Affects confidence but could not change any result. | Confidence ceiling CONF-2 for affected claims. |
| US1 | Low | No plausible effect on any result or condition. | Record only. |

Test questions in order, as an assessor applies them:

1. Does the UNKNOWN concern the boundary, the Capability Instance, a Service Outcome or tolerance definition, or could its resolution change the result of two or more gates? If yes, US5.
2. Does it concern a control holding a CRITICAL mapping to an in-scope gate (at a mandatory claim type), or evidence for a gate criterion? If yes, US4.
3. Could its resolution change any ControlResult, or a condition attached to the decision? If yes, US3.
4. Could its resolution change the confidence recorded for a claim? If yes, US2.
5. Otherwise US1.

**SDF-REQ-020** Every UNKNOWN Record shall carry a severity determined by the top-down test, with the determining question recorded; US3, US4 and US5 severities shall be reviewed by the independent reviewer.

**SDF-REQ-021** The effect of an UNKNOWN shall be applied once, through the decision derivation; an UNKNOWN shall not also be converted into a score deduction.

# Part X - Findings and scenarios

**Do not deduct twice for the same condition.**

| **Finding or scenario** | **Rule** |
|---|---|
| Observation | No result effect. |
| Improvement | No effect unless the control result changes. |
| Weakness | Reflected in the control result (PARTIAL or NONCONFORMING on a non-critical control); listed in the decision record; no ceiling of its own. |
| Significant weakness | A NONCONFORMING result on a control relevant to a Service Outcome, or a SUPPORTING-control deficiency that required gate-level evaluation. Decision ≤ CONDITIONALLY_ASSURED for affected outcomes with a named, owned, time-bound condition. |
| Critical finding | A deficiency on a CRITICAL control or gate criterion: produces gate FAIL through the roll-up rule. |
| Accepted risk | Does not change a result or Gate Result; recorded with the authority that accepted it (CG-13). |
| Effective scenario | Supports EFFECTIVENESS/RESILIENCE claims within the tested conditions only. |
| Uncontained scenario | Evaluated under CG-09; affected outcomes reviewed. |
| Recovery unknown | CG-10 UNKNOWN or FAIL according to evidence. |

**SDF-REQ-022** Each Finding shall be classified using the table above, and its decision effect shall arise only through the control result, the gate roll-up or the condition step of the decision derivation.

# Part XI - Confidence and coverage

**Confidence is recorded professional judgment, not statistical probability.**

Confidence uses the canonical levels of AIDCF-008 §27: CONF-0 UNKNOWN, CONF-1 LOW, CONF-2 MODERATE, CONF-3 HIGH, CONF-4 VERY_HIGH, with flags CONFLICTING and STALE. Decision confidence is the reviewed confidence in the top claim, not exceeding the lowest confidence recorded for any decisive claim (a mandatory claim of a CRITICAL control or a gate criterion) unless the reviewer records why that claim does not bear on the outcome.

| **Measure** | **Definition** |
|---|---|
| Coverage % | Scored / (in-scope − NOT_APPLICABLE) × 100, per scope and claim type (Part VI). |
| UNKNOWN % | UNKNOWN / (in-scope − NOT_APPLICABLE) × 100, with counts by severity. |
| NOT_ASSESSED % | NOT_ASSESSED / (in-scope − NOT_APPLICABLE) × 100. |
| Gate coverage | Gates with a result other than NOT_ASSESSED / applicable gates. |
| Dependency coverage | DEP exception (Part VI). |

**SDF-REQ-023** Every reported score shall be accompanied by its coverage %, UNKNOWN counts by severity and the decision confidence level; confidence shall respect the ceilings in AIDCF-008 §27.

# Part XII - Decision model

**The engine derives the maximum permissible decision state; accountable authority decides.**

## Decision states

| **Decision state** | **Definition** |
|---|---|
| REASONABLY_ASSURED | The top claim is supported for the declared outcomes, states and period: all in-scope gates PASS or APPROVED_NA, no US3–US5 UNKNOWN affecting the outcomes, coverage and bands meet the thresholds, no Significant weakness open, decision confidence CONF-3 or higher. |
| CONDITIONALLY_ASSURED | The core claim is supported, subject to named, owned and time-bound conditions (US3 UNKNOWNs, Significant weaknesses, domain coverage gaps); no gate FAIL or UNKNOWN affecting the outcomes; decision confidence CONF-2 or higher. |
| LIMITED | Material scope, evidence, coverage, gate UNKNOWN or weakness prevents a stronger conclusion; what is supported is stated with its limits. |
| NOT_ASSURED | Evidence demonstrates that the claim does not hold for the affected outcomes (gate FAIL with a NOT_ASSURED ceiling, or B1 band). |
| INCONCLUSIVE | Evidence, method or boundary cannot support a determination (US5, CG-01/CG-11/CG-12 FAIL, coverage below 50%). |

Aliases (legacy → canonical): ADVERSE, ADVERSE_NOT_ASSURED, "Adverse / Not assured" → NOT_ASSURED; UNKNOWN, UNKNOWN_INCONCLUSIVE, UNKNOWN_OR_INCONCLUSIVE, "Withheld" → INCONCLUSIVE; CONDITIONAL → CONDITIONALLY_ASSURED. "NOT ASSESSED" is not a decision state: no decision is issued.

Decision lifecycle: DRAFT (being derived) → RECOMMENDED (Decision Recommendation issued with maximum permissible state) → APPROVED (decision owner has decided after independent review) → ACTIVE (published, within validity) → SUSPENDED (reliance paused by change, incident, expiry of evidence or gate change) / WITHDRAWN (removed for integrity or governance reasons) / SUPERSEDED (replaced by a later approved decision) / EXPIRED (validity period ended). SUSPENDED, WITHDRAWN, SUPERSEDED and EXPIRED are lifecycle states, not decision states.

## Derivation order

Precedence is fixed: gates → UNKNOWN severity → coverage → bands → conditions. Each step can only lower the ceiling. The derivation runs per Service Outcome in the decision question; the recommendation for the question is the lowest outcome ceiling unless the decision question is explicitly partitioned by outcome.

| **Step** | **Input** | **Rule** |
|---|---|---|
| 0 Preconditions | Plan, target AL, decision owner | Target AL is AL2 or higher; CG-01 evaluated; the gate set in scope is fixed (all fifteen unless APPROVED_NA). |
| 1 Gates | Gate Results | For each gate: FAIL → apply the gate's FAIL ceiling to the outcomes and claims it names; UNKNOWN or NOT_ASSESSED → apply the UNKNOWN ceiling; PASS or APPROVED_NA → no effect. |
| 2 UNKNOWN severity | UNKNOWN register | US5 → ≤ INCONCLUSIVE for affected outcomes (whole decision if boundary or Capability Instance); US4 → ≤ LIMITED for affected outcomes (or the gate's UNKNOWN ceiling if lower); US3 → ≤ CONDITIONALLY_ASSURED and a condition; US2 → confidence ceiling CONF-2; US1 → none. |
| 3 Coverage | Coverage of mandatory ControlResults | Capability coverage < 50% → ≤ INCONCLUSIVE; < 80% → ≤ LIMITED. Any domain relevant to the outcome with coverage < 80% for a mandatory claim type → ≤ CONDITIONALLY_ASSURED with a coverage condition. |
| 4 Bands | Reported bands for mandatory claim types | Lowest reported band among CAI and domains relevant to the outcome: B5 or B4 → none; B3 → ≤ CONDITIONALLY_ASSURED; B2 → ≤ LIMITED; B1 → ≤ NOT_ASSURED. Withheld bands have already acted through steps 2 and 3. |
| 5 Conditions and confidence | Findings; decision confidence | Open Significant weakness → ≤ CONDITIONALLY_ASSURED with condition; decision confidence < CONF-3 → ≤ CONDITIONALLY_ASSURED; < CONF-2 → ≤ LIMITED. |
| 6 Recommendation | Ceilings and reasons | Maximum permissible state per outcome and for the question; controlling reasons in step order; prohibited higher states; conditions with owner and due date. |

A domain is relevant to an outcome if at least one of its in-scope controls is traced to a Required Function of that outcome in the CG-01/CG-03 models.

## Pseudocode

```
ORDER = [NOT_ASSURED, INCONCLUSIVE, LIMITED, CONDITIONALLY_ASSURED, REASONABLY_ASSURED]
def cap(cur, new): return min(cur, new, key=ORDER.index)

def derive(question, gates, unknowns, scores, findings, confidence):
    assert question.target_al >= "AL2" and gates["CG-01"].result != "NOT_ASSESSED"
    rec = {}
    for o in question.outcomes:
        c, reasons, conditions = REASONABLY_ASSURED, [], []
        # 1 Gates
        for g in gates.in_scope():
            if g.result == "FAIL":
                c = cap(c, g.fail_ceiling(o));    reasons.append((1, g.id, "FAIL"))
            elif g.result in ("UNKNOWN", "NOT_ASSESSED"):
                c = cap(c, g.unknown_ceiling(o)); reasons.append((1, g.id, g.result))
        # 2 UNKNOWN severity
        for u in unknowns.affecting(o):
            if u.severity == "US5": c = cap(c, INCONCLUSIVE)
            elif u.severity == "US4": c = cap(c, LIMITED)
            elif u.severity == "US3":
                c = cap(c, CONDITIONALLY_ASSURED); conditions.append(u.as_condition())
            elif u.severity == "US2": confidence.ceiling(u.claims, "CONF-2")
            if u.severity >= "US3": reasons.append((2, u.id, u.severity))
        # 3 Coverage
        cov = scores.capability_coverage(mandatory_only=True)
        if cov < 50: c = cap(c, INCONCLUSIVE)
        elif cov < 80: c = cap(c, LIMITED)
        for d in scores.domains_relevant_to(o):
            if d.coverage < 80:
                c = cap(c, CONDITIONALLY_ASSURED); conditions.append(d.coverage_condition())
        # 4 Bands (reported bands only)
        b = scores.lowest_reported_band(o, mandatory_only=True)
        c = cap(c, {"B5": c, "B4": c, "B3": CONDITIONALLY_ASSURED,
                    "B2": LIMITED, "B1": NOT_ASSURED}.get(b, c))
        # 5 Conditions and confidence
        for f in findings.open(o, kind="SIGNIFICANT_WEAKNESS"):
            c = cap(c, CONDITIONALLY_ASSURED); conditions.append(f.as_condition())
        conf = confidence.decision_level(o)
        if conf < "CONF-2": c = cap(c, LIMITED)
        elif conf < "CONF-3": c = cap(c, CONDITIONALLY_ASSURED)
        rec[o] = (c, reasons, conditions)
    overall = min((v[0] for v in rec.values()), key=ORDER.index)
    return Recommendation(overall, rec, prohibited=ORDER[ORDER.index(overall)+1:])
```

## Human accountable decision

The Decision Recommendation is not the decision. The accountable decision owner (CG-13, GC-13-6), after independent review (AIDCF-009 DT-18 and DT-19), selects the decision state.

**SDF-REQ-024** The approved decision state shall not exceed the maximum permissible decision state derived for the same Score Snapshot; any request to exceed it shall be refused and recorded.

**SDF-REQ-025** Where the approved decision state is lower than the maximum permissible state, the decision owner shall record the rationale.

**SDF-REQ-026** Every Assurance Decision shall state the Capability Instance, Service Outcomes, tolerances, operating states, decision question, as-of date, claim depth, decision state, conditions with owners and due dates, controlling reasons, Gate Results, UNKNOWN Records of severity US3 and above, and validity and reassessment triggers.

**SDF-REQ-027** A decision shall move to SUSPENDED when a reassessment trigger of a gate it relies on occurs, when relied-on evidence becomes STALE through material change, or when CG-11 or CG-12 FAIL is found after approval.

# Part XIII - Benchmarking and trends

**Comparisons require equivalent profile, scope, depth, state and rule version.**

| **Concept** | **Rule** |
|---|---|
| Cohort comparability | Same profile and rule version, capability type, scope, target AL, claim type and states. |
| Coverage floor | Only reported bands (coverage ≥ 80%, no US4/US5) enter a cohort. |
| Gate comparison | Gates compared separately from scores. |
| No unsupported ranking | No "best/top" claim without an approved complete cohort. |
| Trend break | A change of scope, weights, formula, band thresholds or result values creates a new series; v1.0 and v1.1 scores are not comparable. |
| Evidence trend | Changes in evidence quality are shown through the evidence profile summary, never as a score change. |
| Incident marker | Decision suspension and reassessment shown on the series. |

# Part XIV - Anti-gaming

**Controls prevent score optimisation from replacing assurance.**

| **Concept** | **Rule** |
|---|---|
| NOT_APPLICABLE inflation | Independent review of exclusions; NOT_APPLICABLE count shown with every score. |
| UNKNOWN laundering | UNKNOWN recoded as PARTIAL or NOT_APPLICABLE is a CG-12 FAIL condition. |
| Cherry picking | Population, strata and sample rationale required. |
| Easy-control weighting | Weights frozen before results. |
| Evidence duplication | Deduplicate common lineage (CG-11). |
| Finding double counting | No second deduction. |
| Score shopping | Formula and rule version frozen. |
| Override abuse | No override above the maximum permissible state; never FAIL-to-PASS. |
| Scope narrowing to pass a gate | A boundary change used to dispose of an UNKNOWN is disclosed as a limitation in the decision and the assurance statement. |
| Dashboard simplification | Score, coverage, confidence, gates and UNKNOWN shown together. |

# Part XV - Machine-executable publication package

**The engine implements declared rules and has no hidden authority.**

| **File** | **Purpose** |
|---|---|
| registries/gates/critical-gates.csv | Gate register: gateId, name, scope, evidenceFloor, requiredClasses, failCeiling, unknownCeiling, approvedNaConditions, ownerArtifact. |
| registries/gates/critical-gate-criteria.csv | Gate criteria: criterionId, gateId, criterion, evidence, testMethod. |
| aidcf-sdf-v1.1.json | Normative configuration: result values, band thresholds, withholding rule, CAI default weights, EQI weights, decision order. |
| control-result.schema.json | ControlResult per control, claim type and scope. |
| family-domain.schema.json | Scores, coverage, bands and withholding. |
| capability-index.schema.json | CAI and supporting views. |
| gate-engine.schema.json | Gate Results, criteria status and ceilings. |
| unknown-severity.schema.json | UNKNOWN type, severity, test and disposition. |
| decision-recommendation.schema.json | Maximum permissible state, controlling reasons and conditions. |
| score-snapshot.schema.json | Immutable lineage. |
| aidcf-score.owl / ttl | Graph vocabulary (namespace https://w3id.org/aidcf/ontology#; w3id registration pending). |
| aidcf-score-shapes.ttl | Validation shapes. |
| conformance-tests | Positive, negative, gate, UNKNOWN, withholding, migration and anti-gaming fixtures, including Examples 1 to 4. |

## Engine execution order

| **Order** | **Action** |
|---|---|
| 1 | Load the approved assessment snapshot, rule version, capability profile and registry version. |
| 2 | Validate IDs, applicability, mandatory claim types, evidence-floor outcomes and UNKNOWN Records (type and severity). |
| 3 | Compute ControlResults per scope, combining scopes and states by the least-favourable rule. |
| 4 | Compute family, domain, CAI and supporting-view scores, coverage and bands with withholding. |
| 5 | Evaluate gates by the roll-up rule and gate criteria. |
| 6 | Run the decision derivation (gates → UNKNOWN severity → coverage → bands → conditions). |
| 7 | Generate the Decision Recommendation with controlling reasons and prohibited states. |
| 8 | Independent review and accountable decision. |
| 9 | Publish the immutable Score Snapshot, decision, validity and reassessment triggers. |

# Part XVI - Synthetic worked cases

Method validation cases, not real assessments.

| **Case** | **Input** | **Treatment** |
|---|---|---|
| High score, electrical gate FAIL | CAI (OPERATION) 88, B4; CG-05 FAIL because MCF-POW-011 Runtime and Derating is PARTIAL (runtime at current battery state of health below transfer time plus margin). | Step 1: NOT_ASSURED for every outcome depending on that power path; LIMITED for the rest. The score remains descriptive; no override. |
| Good operation, recovery UNKNOWN | OPERATION bands B5 across domains; CG-10 UNKNOWN because only a recovery plan exists (no integrated exercise). | Step 1: LIMITED; recovery outcomes INCONCLUSIVE; DESIGN claims about recovery may be reported. |
| Low score, strong evidence | Domain mean 42 (B2), all results at S5 with CONF-3. | Step 4: ≤ LIMITED for outcomes relevant to that domain. Strong evidence makes the weak result highly defensible; it does not raise the score. |
| Narrow high score | Mean 92 on 35% coverage with 50% UNKNOWN. | Band withheld (coverage); step 3: capability coverage < 50% → INCONCLUSIVE. |
| Accepted risk | Non-critical control NONCONFORMING; risk accepted by the authorised holder. | Result stays NONCONFORMING (score 0); Significant weakness → ≤ CONDITIONALLY_ASSURED with condition; acceptance recorded under CG-13. |

# Part XVII - Record templates

## ControlResult

| **Field** | **Entry** |
|---|---|
| controlId / claimType / scope / state | |
| result code / score value | |
| EvidenceAssessment reference (quality vector, EQI for sorting, sufficiency vs floor) | |
| UNKNOWN Record (type, severity) | |
| Findings | |
| gate mappings and roles | |
| confidence (level, flags) | |
| lifecycle state / reviewer / date | |

## Family / Domain / Capability score

| **Field** | **Entry** |
|---|---|
| scope / claim type / rule version | |
| members and weights | |
| mean / band or withholding reason | |
| coverage % and result counts | |
| UNKNOWN counts by severity | |
| mapped Gate Results | |
| confidence | |

## Gate Result

| **Field** | **Entry** |
|---|---|
| gateId / scope / claim depth | |
| CRITICAL control results / SUPPORTING control results | |
| criteria status (GC-xx-n) with evidence references | |
| gate-level evaluations of NONCONFORMING SUPPORTING controls | |
| attached UNKNOWN Records | |
| result / ceiling applied | |
| closure actions / reassessment triggers | |
| reviewer / date | |

## Decision Recommendation

| **Field** | **Entry** |
|---|---|
| decision question / Capability Instance / outcomes / states / as-of date | |
| target AL / claim depth | |
| per-outcome maximum permissible state | |
| controlling reasons in step order | |
| prohibited higher states | |
| conditions (owner, due date, closure evidence) | |
| scores, coverage and bands | |
| Gate Results / UNKNOWN US3–US5 | |
| decision confidence | |

## Score Snapshot

| **Field** | **Entry** |
|---|---|
| snapshotId | |
| assessment / registry version / rule version / capability profile | |
| evidence manifest | |
| inputs / outputs | |
| review | |
| supersession | |

# Part XVIII - Conformance validation

**A conformant implementation shall pass positive and negative tests.**

| **ID** | **Validation** |
|---|---|
| SDF-VAL-001 | UNKNOWN is never encoded as zero, pass or average. |
| SDF-VAL-002 | NOT_APPLICABLE has approved rationale and approver. |
| SDF-VAL-003 | Every score shows claim type, coverage, UNKNOWN counts by severity and confidence. |
| SDF-VAL-004 | No adjusted or evidence-multiplied score is produced. |
| SDF-VAL-005 | Evidence below the profile floor produces UNKNOWN, never a reduced score. |
| SDF-VAL-006 | Weights sum correctly and are frozen before results. |
| SDF-VAL-007 | Gate Results follow the roll-up rule and gate ceilings are applied. |
| SDF-VAL-008 | Findings are not double counted. |
| SDF-VAL-009 | A portfolio or capability average does not hide a failed gate. |
| SDF-VAL-010 | The recommendation lists controlling reasons in derivation order. |
| SDF-VAL-011 | The decision has independent review and accountable authority. |
| SDF-VAL-012 | The snapshot is immutable and versioned. |
| SDF-VAL-013 | Material change suspends affected results and decisions. |
| SDF-VAL-014 | Benchmarks use comparable cohorts and reported bands only. |
| SDF-VAL-015 | Graph inference cannot alter a result, score or gate automatically. |
| SDF-VAL-016 | Bands are withheld when coverage < 80% or a US4/US5 UNKNOWN is attached. |
| SDF-VAL-017 | Results of different claim types are never combined into one score. |
| SDF-VAL-018 | EQI never changes a result, band, gate or decision. |
| SDF-VAL-019 | The approved decision state never exceeds the maximum permissible state. |
| SDF-VAL-020 | Examples 1 to 4 reproduce exactly. |

# Part XIX - Review and release gates

**The framework remains draft until calibration and multidisciplinary review are closed.**

| **Reviewer** | **Status** |
|---|---|
| Methodology author | Draft completed |
| Assurance/scoring specialist | Pending |
| Electrical SME (CG-04, CG-05) | Pending |
| Mechanical/thermal SME (CG-06) | Pending |
| Compute/HPC SME (CG-08) | Pending |
| Storage/network SME (CG-08, CG-10) | Pending |
| Operations/resilience SME (CG-09, CG-10, CG-14) | Pending |
| OT/security SME (CG-07, CG-15) | Pending |
| Evidence specialist (CG-11, CG-12) | Pending |
| Measurement/statistics reviewer (bands, EQI weights, CAI weights) | Pending |
| Legal/privacy/ethics reviewer | Pending |
| AITG/tooling reviewer | Pending |
| Independent practitioner trial | Pending |
| Calibration cohort | Pending |
| Public release | Not approved |

# Annex A - Mapping from v1.0

v1.0 contained no SDF-REQ identifiers; SDF-REQ-001 to SDF-REQ-027 are new and consecutive. SDF-VAL-001 to SDF-VAL-015 are retained with SDF-VAL-004 and SDF-VAL-005 rewritten for the removal of the evidence multiplier; SDF-VAL-016 to SDF-VAL-020 are new.

| **v1.0 content** | **v1.1 treatment** |
|---|---|
| Part III result encoding (0/25/60/85/100) | Part III canonical result codes (0/50/100) and legacy mapping; maturity moved to Implementation Maturity (AIDCF-017). |
| Part IV D1–D5 assurance dimensions | Part IV: D1–D5 are the claim types; mandatory-claim-type rule. |
| Part V evidence overlay and EQI ("weighted mean") | Part V: EQI weights defined; secondary sorting only. |
| Part VI EvidenceConfidenceFactor and AdjustedIndicator | Withdrawn; insufficient evidence → UNKNOWN. |
| Part VII aggregation (weighted means of family indicators) | Part VI generic rule: direct mean over controls, coverage, withholding. |
| Part VIII capability indices (CAI, EAI, RAI, DAI and others) | CAI retained; RAI, DAI and others become supporting views with the same arithmetic; EAI replaced by the evidence profile summary. |
| Part IX gate engine | Part VIII: roll-up rule, CRITICAL/SUPPORTING roles, effective floor, fifteen gate specifications. |
| Part X UNKNOWN engine (Low/Moderate/Material/Critical/Systemic with differing effects) | Part IX: US1–US5 with canonical tests and effects. |
| Part XIII decision model | Part XII: canonical decision states, aliases, lifecycle, deterministic derivation, human decision. |
| Default assurance-dimension profiles (purpose weights blending D1–D5) | Withdrawn; replaced by per-claim-type scores and the mandatory-claim-type rule. |
| Presentation bands (B5 90–100, B4 80–89, B3 65–79, B2 45–64, B1 0–44, BN) | Recalibrated bands B5 ≥ 90, B4 75–89.99, B3 50–74.99, B2 25–49.99, B1 < 25; BN replaced by explicit withholding labels. |
| CG-01 to CG-15 decision cards (identical text) | Distinct gate specifications in Part VIII and registries/gates/*.csv. |
| 15 domain and 90 family scoring profiles (identical text) | Generic rule and domain exception table (Part VI). |
| Synthetic worked examples (descriptive) | Part VII numeric Examples 1 to 4 and Part XVI cases. |
| Decision states ADVERSE / NOT ASSURED, UNKNOWN / INCONCLUSIVE, SUSPENDED, WITHDRAWN, SUPERSEDED | NOT_ASSURED, INCONCLUSIVE; SUSPENDED, WITHDRAWN and SUPERSEDED become lifecycle states. |

## Final doctrine

**AIDCF scores summarise assessed conditions. They do not create assurance, certify a facility or neutralise uncertainty. UNKNOWN remains visible and graded. Critical gates control decisions. Material change may suspend reliance. Only competent and impartial review followed by accountable authority can issue a bounded Assurance Decision, and never above the state the evidence permits.**
