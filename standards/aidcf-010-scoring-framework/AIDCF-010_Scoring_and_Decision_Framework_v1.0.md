> Markdown edition. Source: [AIDCF-010_Scoring_and_Decision_Framework_v1.0.docx](AIDCF-010_Scoring_and_Decision_Framework_v1.0.docx) · PDF: [AIDCF-010_Scoring_and_Decision_Framework_v1.0.pdf](AIDCF-010_Scoring_and_Decision_Framework_v1.0.pdf)

**AIDCF**

**AI Data Centre Facilities Assurance Framework**

**SCORING & DECISION FRAMEWORK**

**Version 1.0**

**  
A constitutional, evidence-aware and gate-controlled standard for synthesising assessment results and issuing bounded assurance decisions**

Artifact ID: AIDCF-SDF-001  
Status: Draft for controlled review  
Author: Siva Sethumadhavan  
Depends on: AIDCF-006, AIDCF-007, AIDCF-008 and AIDCF-009

**  
Evidence supports assurance. Scores summarise. Gates constrain. Accountable authority decides.**

# Document control

| **Field** | **Value**                                                                                                                                                                                |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Purpose   | Translate AIDCF-009 assessment outputs into transparent control, family, domain and capability indicators without overriding evidence, UNKNOWN, critical gates or professional judgment. |
| Inputs    | 360 controls, 90 families, 15 domains, Evidence Assessments, findings, scenarios, gates and reviews.                                                                                     |
| Outputs   | Raw and adjusted indicators, coverage, confidence, CAI, supporting indices, gate overlay, recommendation and accountable decision.                                                       |
| Boundary  | Not certification, guarantee, legal opinion, safety approval or engineering approval.                                                                                                    |
| Safety    | No score may encourage unsafe testing, evidence suppression or uncontrolled operation.                                                                                                   |

# Executive thesis

**AIDCF scoring supports synthesis, prioritisation, comparison and trend analysis. It never creates assurance. Every score remains bounded by capability, outcomes, scope, state, period, evidence, coverage, gates, UNKNOWN, findings, scenarios, review and decision authority.**

# Part I - Constitutional doctrine

**Scoring is subordinate to AIDCF assurance principles.**

| **Concept**            | **Rule**                                                                         |
|------------------------|----------------------------------------------------------------------------------|
| Score is not assurance | Numbers cannot issue or upgrade a decision.                                      |
| Evidence first         | No positive numeric treatment for unevidenced results.                           |
| Gate dominance         | FAIL and critical UNKNOWN constrain decisions regardless of average.             |
| Capability first       | Primary subject is a defined Capability Instance and outcomes.                   |
| State separation       | Design, implementation, operation, effectiveness and resilience remain distinct. |
| No hidden imputation   | UNKNOWN/not assessed are not zero, average or pass.                              |
| No double counting     | Findings change underlying results or gates; no undeclared second deduction.     |
| Human authority        | Automation calculates and recommends; authority decides.                         |
| Bounded use            | Scope, period, state, profile, coverage and confidence are disclosed.            |
| Versioning             | Rules and input snapshots are immutable and superseded explicitly.               |

# Part II - Scoring objects

**Every score is a versioned object with lineage.**

| **Concept**              | **Rule**                                                    |
|--------------------------|-------------------------------------------------------------|
| ControlIndicator         | One control, subject, assurance dimension and state/period. |
| FamilyIndicator          | Aggregation within one family.                              |
| DomainIndicator          | Aggregation across the domain.                              |
| CapabilityAssuranceIndex | Cross-domain summary for one capability.                    |
| EvidenceAssuranceIndex   | Evidence quality, sufficiency and coverage.                 |
| ResilienceAssuranceIndex | Failure, containment and recovery view.                     |
| DependencyAssuranceIndex | Dependency visibility, concentration and common mode.       |
| GateResult               | Independent non-compensating result.                        |
| DecisionRecommendation   | Engine output before review.                                |
| AssuranceDecision        | Accountable bounded decision.                               |
| ScoreSnapshot            | Immutable inputs, rules, outputs and lineage.               |

# Part III - Result state encoding

**UNKNOWN is neither success nor failure.**

| **Concept**           | **Rule**                                         |
|-----------------------|--------------------------------------------------|
| NOT ASSESSED          | No value; retained in coverage and ceiling.      |
| UNKNOWN               | No value; explicit unknown population.           |
| N/A                   | No value; excluded only with approved rationale. |
| NOT IMPLEMENTED       | 0                                                |
| PARTIAL               | 25                                               |
| IMPLEMENTED           | 60                                               |
| OPERATING EFFECTIVELY | 85                                               |
| STRONGLY EFFECTIVE    | 100; optional controlled state.                  |
| INEFFECTIVE           | 0 and finding/gate linkage.                      |
| SUSPENDED             | No current reliance; retain history.             |

# Part IV - Assurance dimensions

**Controls are represented across distinct claim depths.**

| **Concept**       | **Rule**                                                 |
|-------------------|----------------------------------------------------------|
| D1 Design         | Is the safeguard appropriately defined?                  |
| D2 Implementation | Is the design implemented?                               |
| D3 Operation      | Does it operate over the represented period/state?       |
| D4 Effectiveness  | Does it achieve the objective under relevant conditions? |
| D5 Resilience     | Does it contain, continue or recover under adversity?    |

# Part V - Evidence overlay

**Evidence quality remains visible and does not manufacture precision.**

| **Concept**    | **Rule**                                                                                  |
|----------------|-------------------------------------------------------------------------------------------|
| P Provenance   | P0-P5; origin and collection lineage.                                                     |
| F Freshness    | F0-F5; current representation.                                                            |
| C Coverage     | C0-C5; population, period, state and scenario.                                            |
| R Reliability  | R0-R5; method and corroboration.                                                          |
| T Traceability | T0-T5; end-to-end linkage.                                                                |
| I Integrity    | I0-I5; alteration and custody control.                                                    |
| EQI            | 100 × weighted mean of normalised P/F/C/R/T/I; vector remains visible.                    |
| Sufficiency    | S0 none; S1 insufficient; S2 descriptive; S3 reasonable; S4 strong; S5 highly defensible. |

# Part VI - Control indicator

**Raw and evidence-adjusted indicators are separate outputs.**

| **Concept**              | **Rule**                                                     |
|--------------------------|--------------------------------------------------------------|
| DimensionValue           | Ordinal value for numeric controlled state.                  |
| RawControlIndicator      | Σ(wd×vd)/Σ(wd) for numeric applicable dimensions.            |
| EvidenceConfidenceFactor | S2=.50; S3=.75; S4=.90; S5=1.00; S0/S1 no adjusted positive. |
| AdjustedIndicator        | Raw × factor; optional secondary view.                       |
| Coverage                 | Numeric assessed, UNKNOWN, not assessed and N/A displayed.   |
| GateLinks                | Applicable gate status remains separate.                     |
| DecisionCeiling          | Highest permitted recommendation after gates/UNKNOWN.        |
| Confidence               | Controlled state plus rationale.                             |

# Part VII - Aggregation

**Aggregation never hides the composition or missing population.**

| **Concept**  | **Rule**                                                               |
|--------------|------------------------------------------------------------------------|
| Family       | Weighted mean of applicable control indicators; equal default weights. |
| Domain       | Weighted mean of applicable family indicators.                         |
| Capability   | Weighted mean of applicable domain indicators.                         |
| Coverage     | Show assessed, UNKNOWN, not assessed and N/A separately.               |
| Confidence   | Lowest material confidence or reviewed synthesis.                      |
| Gate overlay | All mapped gates displayed independently.                              |
| Status       | Qualitative state after evidence/gate/UNKNOWN review.                  |

# Part VIII - Capability indices

**CAI is a summary for one Capability Instance, not a universal facility rating.**

| **Concept**                 | **Rule**                                                                 |
|-----------------------------|--------------------------------------------------------------------------|
| CAI                         | Cross-domain capability summary.                                         |
| EAI                         | Evidence quality, sufficiency, currency, conflict and coverage.          |
| RAI                         | Cross-domain failure, containment and recovery.                          |
| DAI                         | Dependency visibility, concentration, common mode and recovery reliance. |
| Security Authority Index    | Identity, control plane and consequential authority.                     |
| Operational Readiness Index | Staffing, work control, incidents, change and authority.                 |
| Resource Index              | Environmental performance and resource continuity.                       |

# Part IX - Gate engine

**Critical gates are evaluated before and outside numeric aggregation.**

| **Concept**  | **Rule**                                                            |
|--------------|---------------------------------------------------------------------|
| PASS         | No ceiling from that gate.                                          |
| FAIL         | Apply adverse gate-specific decision rule.                          |
| UNKNOWN      | Apply gate-specific ceiling; generally prevents Reasonably Assured. |
| APPROVED N/A | Exclude only with evidence and review.                              |
| NOT ASSESSED | No positive decision when applicable.                               |

# Part X - UNKNOWN engine

**UNKNOWN is treated by materiality, not a points deduction.**

| **Concept** | **Rule**                                              |
|-------------|-------------------------------------------------------|
| Low         | Bounded non-material limitation.                      |
| Moderate    | Conditionally Assured ceiling.                        |
| Material    | Limited ceiling.                                      |
| Critical    | Unknown, Adverse or Withheld according to evidence.   |
| Systemic    | Assessment cannot support decision; Unknown/Withheld. |

# Part XI - Findings and scenarios

**Do not deduct twice for the same condition.**

| **Concept**          | **Rule**                                  |
|----------------------|-------------------------------------------|
| Observation          | No automatic score effect.                |
| Improvement          | No effect unless control result changes.  |
| Weakness             | Reflected in control result.              |
| Significant weakness | Control/domain effect and gate review.    |
| Critical finding     | Mandatory gate and decision review.       |
| Accepted risk        | Does not change nonconformance to pass.   |
| Effective scenario   | Supports D4/D5 within tested conditions.  |
| Uncontained scenario | Triggers CG-09 and outcome review.        |
| Recovery unknown     | CG-10 UNKNOWN/FAIL according to evidence. |

# Part XII - Confidence and coverage

**Confidence is professional judgment, not statistical probability.**

| **Concept**   | **Rule**                                                         |
|---------------|------------------------------------------------------------------|
| UNKNOWN       | No defensible confidence.                                        |
| LOW           | Weak/limited support.                                            |
| MODERATE      | Reasonable support with limitations.                             |
| HIGH          | Strong support; no unresolved material conflict.                 |
| VERY HIGH     | Highly defensible, representative and appropriately independent. |
| Coverage %    | Numeric assessed/applicable ×100.                                |
| Unknown %     | UNKNOWN/applicable ×100.                                         |
| Gate coverage | Assessed applicable gates/applicable gates.                      |

# Part XIII - Decision model

**The engine recommends; accountable authority decides after independent review.**

| **Concept**            | **Rule**                                                                                   |
|------------------------|--------------------------------------------------------------------------------------------|
| REASONABLY ASSURED     | Sufficient evidence, required states, no gate FAIL, no critical UNKNOWN, High+ confidence. |
| CONDITIONALLY ASSURED  | Core claim supported with named time-bound conditions; no controlling gate FAIL.           |
| LIMITED                | Material scope/evidence weakness or material UNKNOWN.                                      |
| ADVERSE / NOT ASSURED  | Evidence demonstrates material failure or controlling gate FAIL.                           |
| UNKNOWN / INCONCLUSIVE | Evidence, method or boundary cannot support determination.                                 |
| SUSPENDED              | Prior decision invalidated by change, incident, expiry or gate.                            |
| WITHDRAWN              | Decision removed due to material integrity/governance issue.                               |
| SUPERSEDED             | New approved snapshot replaces prior.                                                      |

# Part XIV - Benchmarking and trends

**Comparisons require equivalent profile, scope, depth, state and version.**

| **Concept**            | **Rule**                                                       |
|------------------------|----------------------------------------------------------------|
| Cohort comparability   | Same profile/version, capability type, scope, depth and state. |
| Coverage floor         | Declared minimum cohort coverage.                              |
| Gate comparison        | Gates compared separately from scores.                         |
| No unsupported ranking | No “best/top” without approved complete cohort.                |
| Trend break            | Scope, weights or formula change creates a new series.         |
| Evidence trend         | Raw score may remain while confidence/adjusted changes.        |
| Incident marker        | Decision suspension and reassessment shown.                    |

# Part XV - Anti-gaming

**Controls prevent score optimisation from replacing assurance.**

| **Concept**              | **Rule**                                                       |
|--------------------------|----------------------------------------------------------------|
| N/A inflation            | Independent review of exclusions.                              |
| Cherry picking           | Population and sample rationale required.                      |
| Easy-control weighting   | Weights frozen before results.                                 |
| Evidence duplication     | Deduplicate common lineage.                                    |
| Finding double counting  | No undeclared second deduction.                                |
| Score shopping           | Formula/version frozen.                                        |
| Override abuse           | Named authority, rationale and expiry; never Fail-to-Pass.     |
| Dashboard simplification | Score, coverage, confidence, gates and UNKNOWN shown together. |

# Default assurance-dimension profiles

**The selected assessment purpose determines applicable weights.**

| **Purpose**    | **D1** | **D2** | **D3** | **D4** | **D5** |
|----------------|--------|--------|--------|--------|--------|
| Design         | 100%   | N/A    | N/A    | N/A    | N/A    |
| Implementation | 30%    | 70%    | N/A    | N/A    | N/A    |
| Operating      | 15%    | 25%    | 60%    | N/A    | N/A    |
| Effectiveness  | 10%    | 20%    | 30%    | 40%    | N/A    |
| Resilience     | 10%    | 15%    | 20%    | 25%    | 30%    |

- Profile is approved before scoring.

- An unassessed higher dimension is not assumed.

# Default CAI domain weights

**Baseline weights total 100; an industry/deployment profile may change them only before results.**

| **Domain** | **Weight** |
|------------|------------|
| GOV        | 5          |
| CAP        | 5          |
| DEP        | 7          |
| PHY        | 5          |
| POW        | 10         |
| THM        | 10         |
| ENV        | 4          |
| CMP        | 9          |
| STO        | 9          |
| NET        | 9          |
| OPS        | 7          |
| RES        | 9          |
| SUP        | 4          |
| SEC        | 5          |
| EVA        | 2          |

# Presentation bands

**Bands are descriptive, not certifications or decision states.**

| **Band** | **Indicator** | **Label**                      |
|----------|---------------|--------------------------------|
| B5       | 90-100        | Strong                         |
| B4       | 80-89         | Established                    |
| B3       | 65-79         | Developing                     |
| B2       | 45-64         | Weak                           |
| B1       | 0-44          | Critical weakness              |
| BN       | None          | UNKNOWN/not assessed/suspended |

- Never publish a band without coverage, confidence, gate and UNKNOWN status.

# CG-01 Decision Card - Capability/outcome definition

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-02 Decision Card - Boundary/architecture integrity

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-03 Decision Card - Critical dependency visibility

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-04 Decision Card - Life safety/hazardous energy

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-05 Decision Card - Electrical continuity

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-06 Decision Card - Thermal continuity

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-07 Decision Card - Critical control-system integrity

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-08 Decision Card - Compute/storage/network integrity

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-09 Decision Card - Failure containment

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-10 Decision Card - Recovery readiness

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-11 Decision Card - Evidence sufficiency

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-12 Decision Card - Critical UNKNOWN

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-13 Decision Card - Responsibility/authority

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-14 Decision Card - Change control

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# CG-15 Decision Card - Integrated digital authority

**Complete independently from score aggregation.**

| **Field**         | **Requirement**                                            |
|-------------------|------------------------------------------------------------|
| Applicability     | Capability, outcome, boundary and rationale.               |
| Evidence          | Mandatory evidence profile and IDs.                        |
| States/scenarios  | Relevant operating states and credible adversity.          |
| Status            | PASS, FAIL, UNKNOWN or approved N/A.                       |
| Controlling facts | Findings, evidence conflicts and UNKNOWN.                  |
| Score treatment   | Remain separate; never compensate through averages.        |
| Decision effect   | Apply gate-specific ceiling, adverse result or suspension. |
| Closure           | Action, owner, evidence, retest and trigger.               |
| Review            | Technical and independent approval.                        |

# GOV Domain Scoring Profile - Governance, Accountability and Assurance Direction

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 5%                                                                           |
| Mapped gates   | CG-13; CG-14                                                                 |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# GOV-01 Family Scoring Profile - Governance architecture

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-GOV-001 to MCF-GOV-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-13; CG-14                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# GOV-02 Family Scoring Profile - Accountability and responsibility

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-GOV-005 to MCF-GOV-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-13; CG-14                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# GOV-03 Family Scoring Profile - Policy and standards management

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-GOV-009 to MCF-GOV-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-13; CG-14                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# GOV-04 Family Scoring Profile - Risk and assurance governance

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-GOV-013 to MCF-GOV-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-13; CG-14                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# GOV-05 Family Scoring Profile - Stakeholder and regulatory interface

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-GOV-017 to MCF-GOV-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-13; CG-14                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# GOV-06 Family Scoring Profile - Ethics, impartiality and competence

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-GOV-021 to MCF-GOV-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-13; CG-14                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# CAP Domain Scoring Profile - AI Capability, Service Outcome and Demand Management

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 5%                                                                           |
| Mapped gates   | CG-01; CG-02                                                                 |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# CAP-01 Family Scoring Profile - Capability inventory

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-CAP-001 to MCF-CAP-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-01; CG-02                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# CAP-02 Family Scoring Profile - Service outcome definition

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-CAP-005 to MCF-CAP-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-01; CG-02                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# CAP-03 Family Scoring Profile - Criticality and materiality

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-CAP-009 to MCF-CAP-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-01; CG-02                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# CAP-04 Family Scoring Profile - Demand and growth modelling

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-CAP-013 to MCF-CAP-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-01; CG-02                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# CAP-05 Family Scoring Profile - Operating envelope

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-CAP-017 to MCF-CAP-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-01; CG-02                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# CAP-06 Family Scoring Profile - Capability lifecycle and change

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-CAP-021 to MCF-CAP-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-01; CG-02                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# DEP Domain Scoring Profile - Dependency, Concentration and External Reliance Management

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 7%                                                                           |
| Mapped gates   | CG-03; CG-12                                                                 |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# DEP-01 Family Scoring Profile - Dependency discovery

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-DEP-001 to MCF-DEP-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-03; CG-12                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# DEP-02 Family Scoring Profile - Shared and common-mode dependencies

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-DEP-005 to MCF-DEP-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-03; CG-12                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# DEP-03 Family Scoring Profile - External providers and utilities

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-DEP-009 to MCF-DEP-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-03; CG-12                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# DEP-04 Family Scoring Profile - Concentration and substitutability

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-DEP-013 to MCF-DEP-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-03; CG-12                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# DEP-05 Family Scoring Profile - Boundary and interface control

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-DEP-017 to MCF-DEP-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-03; CG-12                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# DEP-06 Family Scoring Profile - Dependency monitoring and review

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-DEP-021 to MCF-DEP-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-03; CG-12                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# PHY Domain Scoring Profile - Physical Site, Building and Security Infrastructure

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 5%                                                                           |
| Mapped gates   | CG-02; CG-04                                                                 |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# PHY-01 Family Scoring Profile - Site and location resilience

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-PHY-001 to MCF-PHY-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-02; CG-04                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# PHY-02 Family Scoring Profile - Building and structural integrity

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-PHY-005 to MCF-PHY-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-02; CG-04                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# PHY-03 Family Scoring Profile - Physical zoning and segregation

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-PHY-009 to MCF-PHY-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-02; CG-04                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# PHY-04 Family Scoring Profile - Access and surveillance

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-PHY-013 to MCF-PHY-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-02; CG-04                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# PHY-05 Family Scoring Profile - Asset movement and custody

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-PHY-017 to MCF-PHY-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-02; CG-04                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# PHY-06 Family Scoring Profile - Fire, life safety and emergency interfaces

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-PHY-021 to MCF-PHY-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-02; CG-04                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# POW Domain Scoring Profile - Electrical Power Infrastructure and Energy Continuity

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 10%                                                                          |
| Mapped gates   | CG-05                                                                        |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# POW-01 Family Scoring Profile - Utility and grid interface

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-POW-001 to MCF-POW-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-05                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# POW-02 Family Scoring Profile - Generation and fuel

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-POW-005 to MCF-POW-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-05                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# POW-03 Family Scoring Profile - UPS and energy storage

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-POW-009 to MCF-POW-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-05                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# POW-04 Family Scoring Profile - Distribution and protection

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-POW-013 to MCF-POW-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-05                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# POW-05 Family Scoring Profile - Power quality and transient response

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-POW-017 to MCF-POW-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-05                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# POW-06 Family Scoring Profile - Electrical monitoring, maintenance and recovery

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-POW-021 to MCF-POW-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-05                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# THM Domain Scoring Profile - Cooling, Thermal and Fluid Infrastructure

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 10%                                                                          |
| Mapped gates   | CG-06                                                                        |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# THM-01 Family Scoring Profile - Thermal architecture and capacity

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-THM-001 to MCF-THM-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-06                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# THM-02 Family Scoring Profile - Air cooling systems

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-THM-005 to MCF-THM-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-06                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# THM-03 Family Scoring Profile - Liquid cooling systems

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-THM-009 to MCF-THM-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-06                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# THM-04 Family Scoring Profile - Heat rejection and water systems

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-THM-013 to MCF-THM-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-06                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# THM-05 Family Scoring Profile - Fluid quality and leak management

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-THM-017 to MCF-THM-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-06                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# THM-06 Family Scoring Profile - Thermal control, maintenance and recovery

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-THM-021 to MCF-THM-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-06                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# ENV Domain Scoring Profile - Environmental and Resource Performance

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 4%                                                                           |
| Mapped gates   | CG-02; CG-04                                                                 |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# ENV-01 Family Scoring Profile - Environmental operating conditions

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-ENV-001 to MCF-ENV-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-02; CG-04                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# ENV-02 Family Scoring Profile - Energy performance

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-ENV-005 to MCF-ENV-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-02; CG-04                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# ENV-03 Family Scoring Profile - Water performance

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-ENV-009 to MCF-ENV-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-02; CG-04                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# ENV-04 Family Scoring Profile - Carbon and resource reporting

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-ENV-013 to MCF-ENV-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-02; CG-04                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# ENV-05 Family Scoring Profile - Hazardous materials and waste

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-ENV-017 to MCF-ENV-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-02; CG-04                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# ENV-06 Family Scoring Profile - Climate adaptation and resource continuity

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-ENV-021 to MCF-ENV-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-02; CG-04                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# CMP Domain Scoring Profile - AI Compute Infrastructure

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 9%                                                                           |
| Mapped gates   | CG-08                                                                        |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# CMP-01 Family Scoring Profile - Compute architecture and configuration

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-CMP-001 to MCF-CMP-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# CMP-02 Family Scoring Profile - Cluster and scale-up domains

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-CMP-005 to MCF-CMP-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# CMP-03 Family Scoring Profile - Capacity, scheduling and utilisation

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-CMP-009 to MCF-CMP-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# CMP-04 Family Scoring Profile - Firmware, driver and compatibility

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-CMP-013 to MCF-CMP-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# CMP-05 Family Scoring Profile - Compute health and observability

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-CMP-017 to MCF-CMP-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# CMP-06 Family Scoring Profile - Compute lifecycle and recovery

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-CMP-021 to MCF-CMP-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# STO Domain Scoring Profile - AI Storage and Data Infrastructure

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 9%                                                                           |
| Mapped gates   | CG-08; CG-10                                                                 |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# STO-01 Family Scoring Profile - Storage architecture and tiering

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-STO-001 to MCF-STO-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08; CG-10                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# STO-02 Family Scoring Profile - Performance and capacity

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-STO-005 to MCF-STO-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08; CG-10                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# STO-03 Family Scoring Profile - Integrity and consistency

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-STO-009 to MCF-STO-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08; CG-10                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# STO-04 Family Scoring Profile - Protection and replication

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-STO-013 to MCF-STO-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08; CG-10                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# STO-05 Family Scoring Profile - Checkpoint and recovery services

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-STO-017 to MCF-STO-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08; CG-10                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# STO-06 Family Scoring Profile - Storage monitoring and lifecycle

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-STO-021 to MCF-STO-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08; CG-10                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# NET Domain Scoring Profile - AI Network and Interconnect Architecture

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 9%                                                                           |
| Mapped gates   | CG-08                                                                        |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# NET-01 Family Scoring Profile - Scale-up and scale-out fabrics

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-NET-001 to MCF-NET-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# NET-02 Family Scoring Profile - Performance and congestion control

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-NET-005 to MCF-NET-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# NET-03 Family Scoring Profile - Storage and service networks

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-NET-009 to MCF-NET-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# NET-04 Family Scoring Profile - Management and out-of-band networks

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-NET-013 to MCF-NET-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# NET-05 Family Scoring Profile - Physical connectivity and optics

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-NET-017 to MCF-NET-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# NET-06 Family Scoring Profile - Network control and observability

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-NET-021 to MCF-NET-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-08                                                                                           |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# OPS Domain Scoring Profile - Building Operations and Service Management

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 7%                                                                           |
| Mapped gates   | CG-07; CG-13; CG-14                                                          |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# OPS-01 Family Scoring Profile - Operating model and staffing

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-OPS-001 to MCF-OPS-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-07; CG-13; CG-14                                                                             |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# OPS-02 Family Scoring Profile - Procedure and work control

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-OPS-005 to MCF-OPS-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-07; CG-13; CG-14                                                                             |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# OPS-03 Family Scoring Profile - Maintenance and reliability

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-OPS-009 to MCF-OPS-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-07; CG-13; CG-14                                                                             |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# OPS-04 Family Scoring Profile - Alarm, incident and problem management

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-OPS-013 to MCF-OPS-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-07; CG-13; CG-14                                                                             |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# OPS-05 Family Scoring Profile - Change and configuration management

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-OPS-017 to MCF-OPS-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-07; CG-13; CG-14                                                                             |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# OPS-06 Family Scoring Profile - Capacity and service operations

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-OPS-021 to MCF-OPS-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-07; CG-13; CG-14                                                                             |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# RES Domain Scoring Profile - Resilience, Continuity and Recovery

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 9%                                                                           |
| Mapped gates   | CG-09; CG-10                                                                 |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# RES-01 Family Scoring Profile - Resilience strategy

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-RES-001 to MCF-RES-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-09; CG-10                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# RES-02 Family Scoring Profile - Fault-domain and containment design

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-RES-005 to MCF-RES-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-09; CG-10                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# RES-03 Family Scoring Profile - Continuity planning

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-RES-009 to MCF-RES-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-09; CG-10                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# RES-04 Family Scoring Profile - Recovery planning

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-RES-013 to MCF-RES-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-09; CG-10                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# RES-05 Family Scoring Profile - Testing and exercising

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-RES-017 to MCF-RES-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-09; CG-10                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# RES-06 Family Scoring Profile - Crisis and adaptive response

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-RES-021 to MCF-RES-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-09; CG-10                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# SUP Domain Scoring Profile - Supply Chain, OEM and Ecosystem Assurance

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 4%                                                                           |
| Mapped gates   | CG-03; CG-13                                                                 |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# SUP-01 Family Scoring Profile - Supplier due diligence

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-SUP-001 to MCF-SUP-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-03; CG-13                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# SUP-02 Family Scoring Profile - Contract and service obligations

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-SUP-005 to MCF-SUP-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-03; CG-13                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# SUP-03 Family Scoring Profile - Hardware and component provenance

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-SUP-009 to MCF-SUP-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-03; CG-13                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# SUP-04 Family Scoring Profile - Software, firmware and update supply

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-SUP-013 to MCF-SUP-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-03; CG-13                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# SUP-05 Family Scoring Profile - Spares, logistics and obsolescence

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-SUP-017 to MCF-SUP-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-03; CG-13                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# SUP-06 Family Scoring Profile - Remote support and third-party access

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-SUP-021 to MCF-SUP-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-03; CG-13                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# SEC Domain Scoring Profile - Digital, OT and Control-Plane Security

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 5%                                                                           |
| Mapped gates   | CG-07; CG-15                                                                 |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# SEC-01 Family Scoring Profile - Identity and privileged access

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-SEC-001 to MCF-SEC-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-07; CG-15                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# SEC-02 Family Scoring Profile - Control-plane protection

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-SEC-005 to MCF-SEC-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-07; CG-15                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# SEC-03 Family Scoring Profile - Network security and segmentation

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-SEC-009 to MCF-SEC-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-07; CG-15                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# SEC-04 Family Scoring Profile - Configuration, vulnerability and patching

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-SEC-013 to MCF-SEC-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-07; CG-15                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# SEC-05 Family Scoring Profile - Detection and response

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-SEC-017 to MCF-SEC-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-07; CG-15                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# SEC-06 Family Scoring Profile - AI-enabled and automated action

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-SEC-021 to MCF-SEC-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-07; CG-15                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# EVA Domain Scoring Profile - Evidence, Assessment and Assurance Management

**Domain indicator remains separate from mapped gates.**

| **Field**      | **Rule**                                                                     |
|----------------|------------------------------------------------------------------------------|
| CAI weight     | 2%                                                                           |
| Mapped gates   | CG-11; CG-12                                                                 |
| Family weights | Equal default; approved profile may vary before scoring.                     |
| Outputs        | Raw, adjusted if permitted, coverage, confidence, gates, UNKNOWN and status. |
| Decision       | Numeric strength cannot compensate for gate failure or critical UNKNOWN.     |

# EVA-01 Family Scoring Profile - Evidence architecture

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-EVA-001 to MCF-EVA-004                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-11; CG-12                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# EVA-02 Family Scoring Profile - Evidence provenance and quality

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-EVA-005 to MCF-EVA-008                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-11; CG-12                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# EVA-03 Family Scoring Profile - Assessment planning and execution

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-EVA-009 to MCF-EVA-012                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-11; CG-12                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# EVA-04 Family Scoring Profile - Findings, UNKNOWN and limitations

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-EVA-013 to MCF-EVA-016                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-11; CG-12                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# EVA-05 Family Scoring Profile - Critical gates and decisions

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-EVA-017 to MCF-EVA-020                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-11; CG-12                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# EVA-06 Family Scoring Profile - Reassessment and continuing assurance

**Four underlying controls are scored across applicable assurance dimensions.**

| **Field**          | **Rule**                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Controls           | MCF-EVA-021 to MCF-EVA-024                                                                      |
| Dimensions         | D1-D5 as applicable to assessment purpose.                                                      |
| Raw indicator      | Weighted mean of numeric applicable results.                                                    |
| Evidence overlay   | EQI, sufficiency, confidence and optional adjusted indicator.                                   |
| Coverage           | Applicable, numeric assessed, UNKNOWN, not assessed and N/A.                                    |
| Gate overlay       | CG-11; CG-12                                                                                    |
| Findings/scenarios | Underlying result plus separate critical effect.                                                |
| Status             | Reviewed qualitative family status.                                                             |
| Reassessment       | Material architecture, capacity, configuration, provider, incident, evidence or outcome change. |

# Machine-executable publication package

**The engine implements declared rules and has no hidden authority.**

| **File**                            | **Purpose**                                                            |
|-------------------------------------|------------------------------------------------------------------------|
| aidcf-sdf-v1.0.json                 | Normative configuration.                                               |
| control-indicator.schema.json       | Control results and evidence.                                          |
| family-domain.schema.json           | Aggregation and coverage.                                              |
| capability-index.schema.json        | CAI and supporting indices.                                            |
| gate-engine.schema.json             | Gate states and decision effects.                                      |
| unknown-ceiling.schema.json         | UNKNOWN classification and ceiling.                                    |
| decision-recommendation.schema.json | Recommendation and controlling reasons.                                |
| score-snapshot.schema.json          | Immutable lineage.                                                     |
| aidcf-score.owl / ttl               | Graph vocabulary.                                                      |
| aidcf-score-shapes.ttl              | Validation shapes.                                                     |
| conformance-tests                   | Positive, negative, gate, UNKNOWN, migration and anti-gaming fixtures. |

# Engine execution order

**Ordered constraints protect the decision from score dominance.**

| **Order** | **Action**                                                    |
|-----------|---------------------------------------------------------------|
| 1         | Load approved assessment snapshot and profile.                |
| 2         | Validate IDs, applicability, evidence and coverage.           |
| 3         | Calculate dimension and raw control indicators.               |
| 4         | Calculate optional adjusted indicators without replacing raw. |
| 5         | Aggregate family/domain/CAI and supporting indices.           |
| 6         | Evaluate gates independently.                                 |
| 7         | Apply UNKNOWN ceilings.                                       |
| 8         | Review findings and scenarios.                                |
| 9         | Generate recommendation and prohibited higher states.         |
| 10        | Complete independent review and accountable decision.         |
| 11        | Publish immutable snapshot, validity and triggers.            |

# Synthetic worked example - High score, electrical gate FAIL

**Method validation example, not a real assessment.**

| **Field**    | **Completed treatment**                                                             |
|--------------|-------------------------------------------------------------------------------------|
| Input        | CAI 88; CG-05 FAIL.                                                                 |
| Calculation  | Compute permitted raw/adjusted indicators and disclose coverage.                    |
| Gate/UNKNOWN | Adverse/Not Assured for resilience; score remains descriptive only.                 |
| Review       | Confirm no override, imputation or double counting.                                 |
| Output       | Score, coverage, confidence, gates, controlling reasons and bounded recommendation. |

# Synthetic worked example - Good operation, recovery UNKNOWN

**Method validation example, not a real assessment.**

| **Field**    | **Completed treatment**                                                             |
|--------------|-------------------------------------------------------------------------------------|
| Input        | High operating indicator; CG-10 UNKNOWN.                                            |
| Calculation  | Compute permitted raw/adjusted indicators and disclose coverage.                    |
| Gate/UNKNOWN | Limited/conditional; no recoverability claim.                                       |
| Review       | Confirm no override, imputation or double counting.                                 |
| Output       | Score, coverage, confidence, gates, controlling reasons and bounded recommendation. |

# Synthetic worked example - Low score, strong evidence

**Method validation example, not a real assessment.**

| **Field**    | **Completed treatment**                                                             |
|--------------|-------------------------------------------------------------------------------------|
| Input        | Domain 42; S5 evidence; High confidence.                                            |
| Calculation  | Compute permitted raw/adjusted indicators and disclose coverage.                    |
| Gate/UNKNOWN | Weak condition is highly defensible; strong evidence does not raise score.          |
| Review       | Confirm no override, imputation or double counting.                                 |
| Output       | Score, coverage, confidence, gates, controlling reasons and bounded recommendation. |

# Synthetic worked example - Narrow high score

**Method validation example, not a real assessment.**

| **Field**    | **Completed treatment**                                                             |
|--------------|-------------------------------------------------------------------------------------|
| Input        | Indicator 92; 35% coverage; 50% UNKNOWN.                                            |
| Calculation  | Compute permitted raw/adjusted indicators and disclose coverage.                    |
| Gate/UNKNOWN | Do not publish 92 alone; Unknown/Limited recommendation.                            |
| Review       | Confirm no override, imputation or double counting.                                 |
| Output       | Score, coverage, confidence, gates, controlling reasons and bounded recommendation. |

# Synthetic worked example - Accepted risk

**Method validation example, not a real assessment.**

| **Field**    | **Completed treatment**                                                             |
|--------------|-------------------------------------------------------------------------------------|
| Input        | Control nonconforming; risk accepted.                                               |
| Calculation  | Compute permitted raw/adjusted indicators and disclose coverage.                    |
| Gate/UNKNOWN | Acceptance is separate and does not change control to pass.                         |
| Review       | Confirm no override, imputation or double counting.                                 |
| Output       | Score, coverage, confidence, gates, controlling reasons and bounded recommendation. |

# Template - Control Indicator

**Complete all mandatory attributes.**

| **Field**       | **Entry** |
|-----------------|-----------|
| controlId       |           |
| dimensions      |           |
| raw             |           |
| evidence vector |           |
| sufficiency     |           |
| adjusted        |           |
| coverage        |           |
| gates           |           |
| UNKNOWN         |           |
| confidence      |           |
| review          |           |

# Template - Family/Domain Indicator

**Complete all mandatory attributes.**

| **Field**  | **Entry** |
|------------|-----------|
| members    |           |
| weights    |           |
| raw        |           |
| adjusted   |           |
| coverage   |           |
| confidence |           |
| gates      |           |
| UNKNOWN    |           |
| status     |           |

# Template - Capability Index

**Complete all mandatory attributes.**

| **Field**          | **Entry** |
|--------------------|-----------|
| profile            |           |
| domain indicators  |           |
| weights            |           |
| CAI                |           |
| supporting indices |           |
| coverage           |           |
| gates              |           |
| recommendation     |           |

# Template - Gate Result

**Complete all mandatory attributes.**

| **Field**     | **Entry** |
|---------------|-----------|
| gateId        |           |
| applicability |           |
| evidence      |           |
| status        |           |
| findings      |           |
| UNKNOWN       |           |
| effect        |           |
| closure       |           |
| review        |           |

# Template - Decision Recommendation

**Complete all mandatory attributes.**

| **Field**                 | **Entry** |
|---------------------------|-----------|
| question                  |           |
| subject                   |           |
| scope                     |           |
| scores                    |           |
| coverage                  |           |
| confidence                |           |
| gates                     |           |
| UNKNOWN                   |           |
| findings                  |           |
| scenarios                 |           |
| allowed/prohibited states |           |
| reasons                   |           |

# Template - Score Snapshot

**Complete all mandatory attributes.**

| **Field**                | **Entry** |
|--------------------------|-----------|
| snapshotId               |           |
| assessment               |           |
| evidence manifest        |           |
| profile/formula versions |           |
| inputs                   |           |
| outputs                  |           |
| review                   |           |
| supersession             |           |

# Conformance validation

**A conformant implementation must pass positive and negative tests.**

| **ID**      | **Validation**                                           |
|-------------|----------------------------------------------------------|
| SDF-VAL-001 | UNKNOWN never encoded as zero, pass or average.          |
| SDF-VAL-002 | N/A has approved rationale.                              |
| SDF-VAL-003 | Every score shows coverage and confidence.               |
| SDF-VAL-004 | Raw and adjusted indicators are both retained.           |
| SDF-VAL-005 | Evidence factor does not override sufficiency/gates.     |
| SDF-VAL-006 | Weights sum correctly and are frozen before results.     |
| SDF-VAL-007 | Gate effects are applied.                                |
| SDF-VAL-008 | Findings are not double counted.                         |
| SDF-VAL-009 | Portfolio average does not hide failed capability gates. |
| SDF-VAL-010 | Recommendation lists controlling reasons.                |
| SDF-VAL-011 | Decision has independent review and authority.           |
| SDF-VAL-012 | Snapshot is immutable and versioned.                     |
| SDF-VAL-013 | Material change suspends affected score.                 |
| SDF-VAL-014 | Benchmarks use comparable cohorts.                       |
| SDF-VAL-015 | Graph inference cannot alter score automatically.        |

# Review and release gates

**The framework remains draft until calibration and multidisciplinary review are closed.**

| **Reviewer**                    | **Status** |
|---------------------------------|------------|
| Methodology author              | Pending    |
| Assurance/scoring specialist    | Pending    |
| Electrical SME                  | Pending    |
| Mechanical/thermal SME          | Pending    |
| Compute/HPC SME                 | Pending    |
| Storage/network SME             | Pending    |
| Operations/resilience SME       | Pending    |
| OT/security SME                 | Pending    |
| Evidence specialist             | Pending    |
| Measurement/statistics reviewer | Pending    |
| Legal/privacy/ethics reviewer   | Pending    |
| AITG/tooling reviewer           | Pending    |
| Independent practitioner pilot  | Pending    |
| Calibration cohort              | Pending    |
| Public release                  | Pending    |

## Final doctrine

**AIDCF scores summarise assessed conditions. They do not create assurance, certify a facility or neutralise uncertainty. UNKNOWN remains visible. Critical gates control decisions. Material change may suspend reliance. Only competent and impartial review followed by accountable authority can issue a bounded assurance decision.**
