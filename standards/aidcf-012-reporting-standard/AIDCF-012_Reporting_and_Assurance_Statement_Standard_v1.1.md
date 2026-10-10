> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-012_Reporting_and_Assurance_Statement_Standard_v1.1.pdf](AIDCF-012_Reporting_and_Assurance_Statement_Standard_v1.1.pdf).

**AIDCF**

**AI Data Centre Facilities Assurance Framework**

**REPORTING AND ASSURANCE STATEMENT STANDARD**

**Version 1.1**

A normative standard for reports, bounded assurance statements, controlled decision wording, registers, dashboards and machine-readable reporting

Artifact ID: AIDCF-012  
Status: Draft for controlled review  
Author: Siva Sethumadhavan

**Reports communicate assurance. Reports do not create assurance.**

# Document control

| **Field**         | **Value**                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| Title             | AIDCF-012 Reporting and Assurance Statement Standard                                                             |
| Artifact ID       | AIDCF-012 (requirement short code RAS)                                                                           |
| Version           | 1.1                                                                                                              |
| Date              | 2026-10-10                                                                                                       |
| Status            | Draft for controlled review                                                                                      |
| Author            | Siva Sethumadhavan                                                                                               |
| Depends on        | AIDCF-006, AIDCF-008, AIDCF-009, AIDCF-010, AIDCF-011, AIDCF-014                                                 |
| Purpose           | Communicate scope, evidence, Findings, Gate Results, scores, UNKNOWN, decisions, limitations and validity consistently. |
| Inputs            | Approved AIDCF-009 assessment and AIDCF-010 decision snapshot under AIDCF-011 programme governance.               |
| Outputs           | Report classes R1–R10, assurance statements AS-01–AS-05, lifecycle notices AS-06–AS-08, registers and dashboards. |
| Non-certification | No report creates certification, accreditation, endorsement or guarantee.                                        |
| Security          | Sensitive infrastructure, identity, authority and dependency details require controlled disclosure.              |

## Revision history

| **Version** | **Date**   | **Summary**                                                                                                                                                                                                                                                  |
|-------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | —          | Initial reporting standard (published under the superseded identifier AIDCF-RAS-001).                                                                                                                                                                        |
| 1.1         | 2026-10-10 | Single authoritative controlled-wording table for the canonical decision states (Part V) referenced by AIDCF-010 and AIDCF-011; canonical gate, control-result, UNKNOWN-severity and finding vocabularies; gate-summary section without conditional gate states; differentiated AS-01–AS-05 templates and lifecycle notices; consolidated boilerplate annexes; canonical graph mappings; RAS-REQ requirement IDs with mapping annex; review and release table moved to AIDCF-011. |

# 0 Introduction

## 0.1 Normative language

"Shall" and "shall not" state requirements; "should" and "should not" state recommendations; "may" states a permission; "can" states a capability (ISO/IEC Directives, Part 2 usage). Requirements carry identifiers RAS-REQ-NNN.

## 0.2 Relationship to other AIDCF artifacts

AIDCF-010 decides which decision state is permitted; this standard decides how that state is worded and presented. AIDCF-011 decides which statement template a programme uses; this standard defines the templates. AIDCF-009 produces the assessment record that every report is drawn from.

# Part I — Reporting doctrine

Reporting is a controlled transformation of an approved assurance record.

| **Element**           | **Requirement**                                                          |
|-----------------------|--------------------------------------------------------------------------|
| Evidence authority    | Presentation cannot strengthen evidence.                                 |
| Single source         | All packages reference one authorised assessment and decision snapshot.  |
| Audience tailoring    | Detail may change; meaning and limitations may not.                      |
| No silent omission    | Material gate FAIL or UNKNOWN and limitations remain visible.            |
| Score restraint       | Scores are shown with coverage, band status, Gate Results and UNKNOWN.   |
| Management separation | Management response is separate from the assessor conclusion.            |
| No certification      | No certificate, mark, accreditation or universal claim.                  |
| Security              | Redaction protects detail but cannot hide decision limitations.          |
| Versioning            | Stable IDs, status, correction and supersession.                         |
| Human approval        | Automation drafts; accountable authorities approve.                      |

**RAS-REQ-001** Every report and statement shall identify, and be drawn only from, a single approved assessment and decision snapshot.

**RAS-REQ-002** No derivative report, summary or statement shall state or imply a stronger conclusion, wider scope or longer validity than the R2 Technical Assessment Report for the same snapshot.

# Part II — Mandatory report content

Every material report contains the same minimum assurance facts.

| **Element**   | **Requirement**                                                                                       |
|---------------|-------------------------------------------------------------------------------------------------------|
| Capability    | Capability Instance and Service Outcomes with tolerances.                                             |
| Question      | Decision question and prohibited interpretations.                                                     |
| Scope         | Physical, logical, organisational, provider and temporal boundaries.                                  |
| States/period | Assessed operating states (AIDCF-003 §45) and evidence period.                                        |
| Criteria      | AIDCF artifact, registry and capability-profile versions.                                             |
| Methods       | Assessment type, Assurance Level (AL0–AL6), claim types concluded and material procedures.            |
| Evidence      | Coverage, quality, sufficiency, conflict and restrictions.                                            |
| Gates         | Gate summary (Part VII) for all in-scope gates.                                                       |
| UNKNOWN       | Material UNKNOWN Records (US3–US5), ceilings and evidence to resolve.                                 |
| Scores        | Scores with coverage and band, or "Band withheld (coverage/UNKNOWN)" (AIDCF-010).                     |
| Decision      | Canonical decision state, lifecycle state and the Part V controlled wording.                          |
| Validity      | Conditions, validity end and Reassessment Triggers.                                                   |

# Part III — Report classes

| **Class** | **Report**                      | **Audience**                                    | **Typical programme use (AIDCF-011)** |
|-----------|---------------------------------|-------------------------------------------------|----------------------------------------|
| R1        | Executive Assurance Report      | Board, executive committee and accountable executives | All models                       |
| R2        | Technical Assessment Report     | Engineering, operations, security and assurance | All models (master record)             |
| R3        | Domain Report                   | Domain owner and specialist                     | All models                             |
| R4        | Evidence Package                | Evidence custodians and reviewers               | All models                             |
| R5        | Gate and Decision Package       | Independent reviewer and decision authority     | All models                             |
| R6        | Customer/Second-Party Statement | Named relying party                             | Second-party, diligence                |
| R7        | Regulatory Support Package      | Authorised regulator engagement                 | Regulatory support                     |
| R8        | Public Summary                  | Controlled external disclosure                  | Optional                               |
| R9        | Continuing-Assurance Report     | Monitored assertions and trigger state          | Continuing assurance (AL6)             |
| R10       | Remediation/Closure Report      | Action owners and reviewers                     | All models                             |

**RAS-REQ-003** An R2 Technical Assessment Report shall exist for every assessment from which any other report class or statement is issued.

# Part IV — Mandatory metadata

A report without identity, lineage and intended use is non-conformant. All fields below are mandatory.

| **Field**       | **Content**                                                                  |
|-----------------|------------------------------------------------------------------------------|
| reportId        | Stable report identifier.                                                    |
| version         | Report version.                                                              |
| status          | Report status (DRAFT, IN_REVIEW, ISSUED, CORRECTED, SUPERSEDED, WITHDRAWN).  |
| reportClass     | R1–R10.                                                                      |
| programmeId     | AIDCF-011 programme.                                                         |
| assessmentId    | AIDCF-009 assessment.                                                        |
| decisionId      | Assurance Decision reported.                                                 |
| issuer          | Issuing organisation and authority.                                          |
| preparer        | Preparer.                                                                    |
| reviewers       | Technical and independent reviewers.                                         |
| intendedUsers   | Named users.                                                                 |
| intendedUse     | Decision the report supports.                                                |
| capabilityId    | Capability Instance.                                                         |
| serviceOutcomes | Service Outcomes and tolerances.                                             |
| scope           | Boundary and exclusions.                                                     |
| profile         | Capability profile and registry versions.                                    |
| period          | Evidence period and assessment date.                                         |
| classification  | Part XIII classification.                                                    |
| validity        | Validity end and triggers.                                                   |
| supersedes      | Prior report superseded, or "none".                                          |

# Part V — Controlled decision language (authoritative)

This Part is the single authoritative source of controlled wording for AIDCF decision states. AIDCF-009, AIDCF-010 and AIDCF-011 refer to it and do not define alternative wording. AIDCF-010 determines which state is permitted; this Part determines how it is expressed. The meanings below summarise the AIDCF-010 Part XII definitions; the maximum permissible state is derived in the AIDCF-010 order gates → UNKNOWN severity → coverage → bands → conditions and confidence, with ceilings ranked REASONABLY_ASSURED > CONDITIONALLY_ASSURED > LIMITED > INCONCLUSIVE > NOT_ASSURED.

## V.1 Decision states

Bracketed items are completed from the approved decision record. The core sentence shall be used verbatim apart from the bracketed items; additional explanatory text may follow it but may not qualify it upwards.

| **Decision state**    | **Meaning (entry conditions per AIDCF-010)**                                                                                       | **Controlled core wording**                                                                                                                                                                                                                                                                                         | **Mandatory accompanying disclosures**                                                                     | **Prohibited**                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| REASONABLY_ASSURED    | All in-scope gates PASS or APPROVED_NA; no US3–US5 UNKNOWN affecting the outcomes; coverage and bands meet the AIDCF-010 thresholds; no Significant weakness open; decision confidence CONF-3 or higher. | "Based on the work performed and the evidence obtained, [issuer] concludes with reasonable assurance that [Capability Instance] can achieve [Service Outcomes] within [tolerances] under [operating states], for [decision question], as of [date], within the scope and limitations stated in this [report/statement]." | Scope, states, period, Assurance Level and claim types concluded; gate summary; limitations; validity end and triggers; non-certification note. | "Certified", "guaranteed", "fully compliant", "safe", "secure" or "resilient" without qualification; omission of any limitation. |
| CONDITIONALLY_ASSURED | Core claim supported subject to named, owned, time-bound conditions (US3 UNKNOWN Records, Significant weaknesses, domain coverage gaps, band B3); no gate FAIL or UNKNOWN affecting the outcomes; decision confidence CONF-2 or higher. | "Based on the work performed and the evidence obtained, [issuer] concludes that [Capability Instance] can achieve [Service Outcomes] within [tolerances] under [operating states], for [decision question], as of [date], subject to the conditions listed below. If a condition is not met by its stated date, this conclusion ceases to apply to [affected scope]." | Each condition with owner, due date or event, evidence required and effect if unmet; all items required for REASONABLY_ASSURED. | Presenting the conclusion without its conditions; describing conditions as recommendations; "conditional pass" of any gate. |
| LIMITED               | Material scope, evidence, coverage (capability coverage below 80%), gate UNKNOWN, US4 UNKNOWN, band B2 or weakness prevents a stronger conclusion; what is supported is stated with its limits. | "Based on the work performed, [issuer] has obtained evidence that supports only the following limited conclusions: [supported claims]. [Issuer] does not conclude that [Capability Instance] can achieve [Service Outcomes] within [tolerances] under [operating states], because [controlling Gate Results, UNKNOWN Records or limitations]." | Supported claims; controlling Gate Results and UNKNOWN Records; evidence needed to resolve; validity and triggers. | Wording that implies the unsupported claims are met; "substantially assured"; leading with supported claims while omitting controlling items. |
| NOT_ASSURED           | Evidence demonstrates that the claim does not hold for the affected outcomes: a gate FAIL with a NOT_ASSURED ceiling, or band B1. | "Based on the work performed and the evidence obtained, [issuer] concludes that [Capability Instance] is not assured to achieve [Service Outcomes] within [tolerances] under [operating states], for [decision question], as of [date], because [controlling FAIL Gate Results or demonstrated deficiencies]." | Controlling Gate Results and Findings; consequence for Service Outcomes; required actions; reassessment route. | Softening terms ("opportunity", "minor"); presenting scores or partial strengths before the controlling reasons. |
| INCONCLUSIVE          | Evidence, method or boundary cannot support a determination: US5 UNKNOWN, CG-01, CG-11 or CG-12 FAIL, or capability coverage below 50%. | "[Issuer] is unable to conclude whether [Capability Instance] can achieve [Service Outcomes] within [tolerances] under [operating states], for [decision question], because [US5 UNKNOWN Records, boundary or evidence limitations]. This is neither a positive nor a negative conclusion." | The UNKNOWN Records or limitations that prevent a conclusion; evidence or scope changes needed; whether reassessment is planned. | Presenting INCONCLUSIVE as favourable or as "pending assurance"; implying a positive result is expected. |

## V.2 Decision lifecycle notices

| **Lifecycle state** | **Controlled core wording**                                                                                                                                                       | **Template** |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| SUSPENDED           | "The Assurance Decision [decisionId] dated [date] is suspended with effect from [date] for [affected scope] because [trigger]. It should not be relied on for that scope until reassessment is complete." | AS-06        |
| WITHDRAWN           | "The Assurance Decision [decisionId] dated [date] is withdrawn with effect from [date] because [reason]. It shall not be relied on."                                             | AS-07        |
| SUPERSEDED          | "The Assurance Decision [decisionId] dated [date] is superseded by [new decisionId] dated [date]. Reliance should be placed on the superseding decision."                         | AS-08        |
| EXPIRED             | "The Assurance Decision [decisionId] expired on [date] and has not been reassessed. It shall not be relied on after that date."                                                   | AS-06 (expiry variant) |

DRAFT and RECOMMENDED decisions shall not be reported outside the assessment team and decision authority. APPROVED and ACTIVE decisions are reported using V.1.

## V.3 No decision issued

Where no Assurance Decision is issued (AL0 discovery, AL1 readiness, or an assessment stopped before decision), the report shall state: "No Assurance Decision has been issued for [Capability Instance]. This report records [discovery/readiness/partial assessment] results only." "Not assessed" is not a decision state.

## V.4 Legacy terms

| **Legacy term**                                                     | **Canonical state**                                 |
|---------------------------------------------------------------------|-----------------------------------------------------|
| ADVERSE; ADVERSE_NOT_ASSURED; "Adverse / Not assured"                | NOT_ASSURED                                         |
| UNKNOWN; UNKNOWN_INCONCLUSIVE; UNKNOWN_OR_INCONCLUSIVE; "Withheld"   | INCONCLUSIVE                                        |
| CONDITIONAL                                                         | CONDITIONALLY_ASSURED                               |
| "NOT ASSESSED"                                                      | Not a decision state; use V.3                       |
| SUSPENDED, WITHDRAWN, SUPERSEDED (as decision states)               | Lifecycle states; use V.2                           |

**RAS-REQ-004** Every report and statement shall express the decision using exactly one canonical decision state from V.1, the corresponding controlled core wording, and all mandatory accompanying disclosures for that state.

**RAS-REQ-005** Legacy decision terms listed in V.4 shall not appear in issued reports or statements except in a mapping or history section.

**RAS-REQ-006** A change of decision lifecycle state to SUSPENDED, WITHDRAWN, SUPERSEDED or EXPIRED shall be communicated to known recipients of the affected decision using the V.2 wording and the corresponding template.

# Part VI — Evidence reporting

| **Element**      | **Requirement**                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------|
| Manifest         | Stable evidence snapshot ID.                                                                          |
| Coverage         | Counts of in-scope controls by result: CONFORMING, PARTIAL, NONCONFORMING, UNKNOWN, NOT_ASSESSED, NOT_APPLICABLE; coverage % as defined in AIDCF-010. |
| Quality          | Quality dimensions (AIDCF-008 v1.1): P Provenance, F Fitness (relevance), C Coverage, R Reliability, T Timeliness (currentness), I Integrity, each 0–5; quality band Q0–Q5. |
| Traceability     | Reported as the AIDCF-008 §17A linkage requirement (each item linked to the assertions it supports, challenges or qualifies), not as a quality dimension. |
| Sufficiency      | Claim-specific S0–S5. Insufficient evidence is reported as UNKNOWN results; no evidence-adjusted or multiplied score is reported (AIDCF-010 removes the evidence multiplier). |
| Conflict         | Supporting, challenging and qualifying evidence; CONFLICTING flags.                                   |
| Restrictions     | Inaccessible, redacted, classified or third-party-controlled evidence.                               |
| Derived evidence | Sources and transformation.                                                                           |
| Sampling/testing | Population, sample, conditions and limitations.                                                       |
| Disclosure       | No credentials, secrets or sensitive paths without authority.                                         |

# Part VII — Critical-gate reporting and gate summary

## VII.1 Gate summary section

Every R1, R2, R5 and AS-series output contains a gate summary in this form:

| **Gate** | **Name** | **Result** | **Controlling items** | **Decision ceiling (AIDCF-010)** | **Closure required** |
|----------|----------|------------|-----------------------|----------------------------------|----------------------|
| CG-nn    | Canonical gate name | PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED | CRITICAL controls not CONFORMING; US4 UNKNOWN Records; unmet criteria | Ceiling imposed, or "none" | Owner, evidence, retest, trigger |

Gate results are reported only as PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED. There is no conditional gate result: wording such as "conditional pass", "pass with observations" or "provisional pass" is prohibited. Conditions are expressed only at decision level (Part V).

## VII.2 Gate reporting rules

| **Element**     | **Requirement**                                                       |
|-----------------|-----------------------------------------------------------------------|
| Applicability   | In scope, APPROVED_NA (with rationale) or NOT_ASSESSED.               |
| Basis           | Evidence and Control Assessment references.                           |
| Decision effect | Ceiling, condition or suspension as determined under AIDCF-010.       |
| Related items   | Findings, UNKNOWN Records and scenarios.                              |
| Closure         | Owner, evidence, retest and trigger.                                  |
| Prominence      | FAIL and UNKNOWN Gate Results on the first page of R1 and in every statement. |
| Visual rule     | No score colour may neutralise a Gate Result.                         |

**RAS-REQ-007** Gate Results shall be reported only in the canonical states PASS, FAIL, UNKNOWN, APPROVED_NA and NOT_ASSESSED, and no report shall describe a gate as conditionally or provisionally passed.

**RAS-REQ-008** Every FAIL or UNKNOWN Gate Result shall appear on the first page of the R1 report and in the gate summary of every statement.

# Part VIII — Score reporting

| **Element**         | **Requirement**                                                                                                          |
|---------------------|--------------------------------------------------------------------------------------------------------------------------|
| Score basis         | Control score = result value (CONFORMING 100, PARTIAL 50, NONCONFORMING 0); family and domain scores = mean of scored controls (AIDCF-010). |
| Coverage            | Coverage % adjacent to every family, domain or capability score.                                                         |
| Decision effect     | Lowest reported band for an outcome: B3 → decision ≤ CONDITIONALLY_ASSURED; B2 → ≤ LIMITED; B1 → ≤ NOT_ASSURED (AIDCF-010). Capability coverage below 50% → ≤ INCONCLUSIVE; below 80% → ≤ LIMITED. |
| No adjusted indicator | Only result-value scores are reported; there is no evidence-adjusted indicator. |
| Band                | B5 Strong, B4 Substantial, B3 Moderate, B2 Weak, B1 Very weak, or "Band withheld (coverage/UNKNOWN)" where coverage is below the AIDCF-010 threshold or a US4/US5 UNKNOWN is in scope. |
| Gate overlay        | Gate summary adjacent to domain and capability scores.                                                                   |
| UNKNOWN             | Count of UNKNOWN results and UNKNOWN Records by severity.                                                                |
| Profile/version     | Any capability-profile weighting and the scoring version.                                                                |
| Trend               | Separate condition change from evidence, scope or method change.                                                         |
| Bands               | Descriptive, never certification tiers.                                                                                  |
| Benchmark           | Cohort comparability and privacy disclosed.                                                                              |

**RAS-REQ-009** A numeric score shall not be presented without its coverage, its band or band-withheld status, and the gate summary for the same scope.

# Part IX — Findings reporting

## IX.1 Finding classification

| **Classification**      | **Meaning**                                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------------------|
| Observation             | Condition noted without a criterion being unmet; no result effect.                                                    |
| Improvement opportunity | Criteria met; a practice could be strengthened.                                                                       |
| Weakness                | A criterion partly unmet (control result PARTIAL) without gate effect.                                                |
| Significant weakness    | Control result NONCONFORMING, or a deficiency in a SUPPORTING-mapped control requiring gate-level evaluation.         |
| Critical finding        | Deficiency that causes a gate FAIL or defeats a Service Outcome tolerance.                                            |

Finding status: OPEN, ACTION_AGREED, CLOSURE_SUBMITTED, CLOSED, SUPERSEDED. Closure requires evidence and reviewer validation.

## IX.2 Finding content

| **Element**         | **Requirement**                                         |
|---------------------|---------------------------------------------------------|
| Identity            | Stable ID and concise title.                            |
| Criterion/condition | Requirement and evidenced state.                        |
| Evidence            | Supporting and challenging references.                  |
| Cause               | Only if evidenced, or labelled as analysis.             |
| Consequence         | Affected Service Outcomes, dependencies and states.     |
| Classification      | IX.1.                                                   |
| Gate/score effect   | Explicit.                                               |
| Management response | Separate from assessor conclusion (Part XI).            |
| Closure             | Evidence and reassessment criteria.                     |
| Status              | IX.1 status.                                            |

# Part X — UNKNOWN reporting

| **Element**      | **Requirement**                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------|
| Identity/subject | Stable ID and affected object.                                                                    |
| Missing item     | Attribute, evidence, state, provider or method.                                                   |
| Type             | U1–U10 (AIDCF-008 §35).                                                                           |
| Severity         | US1 Low, US2 Moderate, US3 Material, US4 Critical, US5 Systemic (AIDCF-009 Part A C5).             |
| Decision effect  | Gate UNKNOWN, decision ceiling, condition or confidence ceiling.                                  |
| Resolution       | Evidence or method required, owner and trigger.                                                   |
| No euphemism     | A US4 or US5 UNKNOWN is never described as an improvement opportunity.                            |

**RAS-REQ-010** Every US3, US4 and US5 UNKNOWN Record shall be reported with its type, severity and decision effect in R1, R2 and every statement; US4 and US5 Records shall not be summarised away in any derivative report.

# Part XI — Management response

| **Element**      | **Requirement**                                    |
|------------------|----------------------------------------------------|
| Position         | Agree, partly agree, disagree or reviewing.        |
| Rationale        | Management view and evidence.                      |
| Action/owner     | Specific action and accountable owner.             |
| Target/trigger   | Approved target or event.                          |
| Risk decision    | Management authority and rationale.                |
| Interim control  | Temporary safeguard and validity.                  |
| Closure evidence | Required proof and independent validation.         |
| Separation       | Distinct styling and data object.                  |

**RAS-REQ-011** Management responses shall be presented as a separate, attributed section or object and shall not alter the assessor's Findings, Gate Results or decision wording.

# Part XII — Validity and supersession

| **Element**  | **Requirement**                                                          |
|--------------|--------------------------------------------------------------------------|
| Validity     | Point in time or period, conditions and validity end.                    |
| Triggers     | Change, incident, expiry, source outage, Gate Result or Finding change.  |
| Correction   | Version, reason and approval; status CORRECTED.                          |
| Suspension   | Affected claims and AS-06 notice.                                        |
| Withdrawal   | Issuer, reason and effective date; AS-07 notice.                         |
| Supersession | New package references prior; AS-08 notice.                              |
| Recall       | Known recipients notified of material change.                            |
| Archive      | Issued and superseded versions retained.                                 |

# Part XIII — Classification

| **Level**            | **Requirement**                                                  |
|----------------------|------------------------------------------------------------------|
| Public               | High-level decision and limitations only.                        |
| Client restricted    | Named users and contractual handling.                            |
| Confidential         | Detailed Findings and technical content.                         |
| Highly restricted    | Sensitive paths, configurations, identities and vulnerabilities. |
| Redaction            | Reason recorded; controlled master retained.                     |
| Third-party evidence | Redistribution restrictions observed.                            |
| Privacy              | Personal data minimised.                                         |
| Export               | Controlled release record.                                       |

**RAS-REQ-012** Redaction shall not remove the decision state, controlling Gate Results, US4 or US5 UNKNOWN Records or material limitations from any report class.

# Part XIV — Visual and accessibility

| **Element**          | **Requirement**                                           |
|----------------------|-----------------------------------------------------------|
| Hierarchy            | Decision, Gate Results, UNKNOWN and actions prominent.    |
| Colour               | Supplemental to text, icon or status label.               |
| Charts               | Denominator, coverage, version and units.                 |
| Tables               | Headers repeat; critical rows not split.                  |
| Language             | Plain executive language; precise technical meaning.      |
| Accessibility        | Structured headings, contrast, readable fonts and labels. |
| No misleading gauges | No false precision or certification cue.                  |
| Page control         | Classification, report ID, version and page number.       |

# Part XV — Quality review

| **Element**        | **Requirement**                                        |
|--------------------|--------------------------------------------------------|
| Reconciliation     | All claims trace to the approved snapshot.             |
| Consistency        | All derivative reports agree.                          |
| Gate/UNKNOWN       | All material items visible.                            |
| Score              | Coverage, band status and version correct.             |
| Claim              | No certification, guarantee or unsupported compliance. |
| Security           | Sensitive disclosure controlled.                       |
| Technical review   | Domain conclusions approved.                           |
| Independent review | Decision and statement challenged.                     |
| Authorisation      | Named issuer approves release.                         |

# Report templates

## R1 Executive Assurance Report

| **Section** | **Required content**                                  |
|-------------|-------------------------------------------------------|
| 1           | Report control (Part IV metadata)                     |
| 2           | Executive decision statement (Part V wording)         |
| 3           | Capability Instance and Service Outcomes              |
| 4           | Scope, operating states and period                    |
| 5           | Gate summary (Part VII)                               |
| 6           | Material Findings and UNKNOWN Records                 |
| 7           | Capability Assurance Index (CAI) and domain scores with coverage and bands |
| 8           | Failure and dependency pathways                       |
| 9           | Management actions and decisions required             |
| 10          | Validity and non-certification note                   |

## R2 Technical Assessment Report

| **Section** | **Required content**                              |
|-------------|---------------------------------------------------|
| 1           | Control and approval                              |
| 2           | Decision question and criteria                    |
| 3           | Capability architecture and boundary              |
| 4           | Profile, Assurance Level, claim types and methods |
| 5           | Evidence, sampling and testing                    |
| 6           | Control results by claim type; family and domain results |
| 7           | Failure scenarios                                 |
| 8           | Gate summary and gate workbooks                   |
| 9           | Findings and UNKNOWN Records                      |
| 10          | Scores, coverage and confidence                   |
| 11          | Technical conclusions                             |
| 12          | Independent review                                |
| 13          | Management response                               |
| 14          | Validity and reassessment                         |
| 15          | Appendices and schemas                            |

## R3 Domain Report

| **Section** | **Required content**                  |
|-------------|---------------------------------------|
| 1           | Domain scope                          |
| 2           | Required Functions and outcomes       |
| 3           | Control and family results            |
| 4           | Evidence                              |
| 5           | Inspection and testing                |
| 6           | Gates affected by domain controls     |
| 7           | Findings and UNKNOWN Records          |
| 8           | Domain score, coverage and band       |
| 9           | Domain conclusion                     |
| 10          | Actions and triggers                  |

## R4 Evidence Package

| **Section** | **Required content** |
|-------------|----------------------|
| 1           | Manifest             |
| 2           | Requirements matrix  |
| 3           | Evidence register    |
| 4           | Quality and sufficiency |
| 5           | Conflict register    |
| 6           | Sampling             |
| 7           | Testing              |
| 8           | Restrictions         |
| 9           | Derived lineage      |
| 10          | Custody and retention |

## R5 Gate and Decision Package

| **Section** | **Required content**          |
|-------------|-------------------------------|
| 1           | Question and scope            |
| 2           | Gate summary                  |
| 3           | Gate workbooks                |
| 4           | US4 and US5 UNKNOWN Records   |
| 5           | Material Findings and scenarios |
| 6           | Scores and coverage           |
| 7           | Decision Recommendation       |
| 8           | Independent challenge         |
| 9           | Decision-authority decision   |
| 10          | Conditions and validity       |

## R6 Customer/Second-Party Statement

| **Section** | **Required content** |
|-------------|----------------------|
| 1           | Issuer, user and use |
| 2           | Capability and scope |
| 3           | Criteria and level   |
| 4           | Responsibilities     |
| 5           | Methods and evidence |
| 6           | Gate summary         |
| 7           | Conclusion (Part V)  |
| 8           | Limitations          |
| 9           | Validity             |
| 10          | Restrictions on use  |
| 11          | Non-certification note |

## R7 Regulatory Support Package

| **Section** | **Required content** |
|-------------|----------------------|
| 1           | Authority and cover  |
| 2           | Regulatory mapping   |
| 3           | Capability and scope |
| 4           | Control mapping      |
| 5           | Evidence index       |
| 6           | Gate and decision trace |
| 7           | Findings and response |
| 8           | Scores if relevant   |
| 9           | Limitations          |
| 10          | Submission record    |

## R8 Public Summary

| **Section** | **Required content**        |
|-------------|-----------------------------|
| 1           | Issuer                      |
| 2           | High-level subject and scope |
| 3           | Assessment basis            |
| 4           | Decision (Part V wording)   |
| 5           | Limitations                 |
| 6           | Validity                    |
| 7           | Contact and reference       |
| 8           | Non-certification note      |

## R9 Continuing-Assurance Report

| **Section** | **Required content**  |
|-------------|-----------------------|
| 1           | Baseline decision     |
| 2           | Monitored assertions  |
| 3           | Source health         |
| 4           | Evidence refresh      |
| 5           | Gate Result changes   |
| 6           | Drift and triggers    |
| 7           | Findings and UNKNOWN  |
| 8           | Current decision and lifecycle state |
| 9           | Human review          |
| 10          | Validity              |

## R10 Remediation/Closure Report

| **Section** | **Required content**  |
|-------------|-----------------------|
| 1           | Original item         |
| 2           | Action                |
| 3           | Interim safeguards    |
| 4           | Closure evidence      |
| 5           | Retest or reassessment |
| 6           | Gate and score impact |
| 7           | Reviewer disposition  |
| 8           | Decision update       |
| 9           | Supersession          |

# Assurance statement templates AS-01 to AS-05

AS-01 to AS-05 are the only AIDCF assurance statement templates; AIDCF-011 selects the template by programme model and does not define its own. Each statement is a bounded AIDCF-aligned statement, never a certificate.

## Common statement elements (AS-01 to AS-05)

| **Element**                                | **Content**                                                                 |
|--------------------------------------------|-----------------------------------------------------------------------------|
| statementId / version / status             | Stable ID, version, status.                                                 |
| issuer / authority                         | Issuing organisation and the authority under which it issues.               |
| intended users / use                       | Named users and the decision supported; restrictions on use.               |
| responsibilities                           | Assessed organisation, assessor, reviewer and decision authority.          |
| capability / outcomes                      | Capability Instance, Service Outcomes and tolerances.                       |
| scope / states / period                    | Boundary, exclusions, operating states and evidence period.                 |
| criteria / profile                         | AIDCF artifact, registry and capability-profile versions.                   |
| Assurance Level / assessment type / claim types | AL0–AL6, AIDCF-011 type, claim types concluded.                        |
| methods                                    | Material methods, sampling and tests.                                       |
| evidence                                   | Coverage, sufficiency and confidence; restrictions.                         |
| gate summary                               | Part VII.1.                                                                 |
| scores with context                        | Part VIII (optional in AS-01 and AS-03; mandatory where scores are shown).  |
| conclusion                                 | Part V.1 core wording and mandatory disclosures.                            |
| conditions                                 | For CONDITIONALLY_ASSURED.                                                  |
| UNKNOWN / limitations                      | US3–US5 UNKNOWN Records and limitations.                                    |
| validity / triggers                        | Validity end and Reassessment Triggers.                                     |
| classification / distribution              | Part XIII.                                                                  |
| non-certification note                     | "This statement is issued by [issuer] under its own authority using the AIDCF method. It is not a certificate, accreditation or endorsement by the AIDCF framework owner." |
| approvals                                  | Independent reviewer and decision authority, with dates.                    |

## Template-specific elements

| **Template** | **Programme model**       | **Additional mandatory elements**                                                                                                                                                         |
|--------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AS-01        | First-party conclusion     | Statement that the conclusion is management's own; the independent challenge performed for material gates and who performed it; known self-review threats and safeguards.              |
| AS-02        | Co-sourced statement       | Responsibility split between management and provider by activity (preparation, testing, evaluation, review); which party issues the conclusion; any work the provider relied on without re-performance. |
| AS-03        | Second-party statement     | Commissioning party and its relationship to the assessed organisation; purpose; access and evidence-rights constraints; statement that the conclusion is for the commissioning party's decision. |
| AS-04        | Independent-provider statement | Provider independence declaration and safeguards; professional standards or quality framework applied by the provider; provider liability and reliance terms; specialists relied on. |
| AS-05        | Continuing-assurance update | Reference to the baseline decision and statement; designated monitored claims; source health and blind spots for the period; triggers fired and their disposition; current decision and lifecycle state. |

**RAS-REQ-013** Every assurance statement shall contain all common statement elements and the additional elements for its template; a statement missing a mandatory element shall not be issued.

## Lifecycle notices AS-06 to AS-08

| **Template** | **Notice**          | **Mandatory elements**                                                                                          |
|--------------|---------------------|-----------------------------------------------------------------------------------------------------------------|
| AS-06        | Suspension notice (and expiry variant) | Affected decision and statement IDs; affected scope; trigger; effective date; V.2 wording; expected reassessment route; issuer approval. |
| AS-07        | Withdrawal notice   | Affected decision and statement IDs; reason; effective date; V.2 wording; recipients notified; issuer approval. |
| AS-08        | Supersession notice | Superseded and superseding decision and statement IDs; summary of changes in decision state, conditions or scope; effective date; V.2 wording. |

# Registers

## Evidence register

| **Field**    | **Content**                                                 |
|--------------|-------------------------------------------------------------|
| evidenceId   | Evidence Object ID.                                         |
| assertion    | Assertions supported, challenged or qualified.              |
| class        | E1–E7.                                                      |
| source       | Source system or party.                                     |
| scope        | Subject and boundary.                                       |
| period       | Period covered.                                             |
| state        | Operating states represented.                               |
| integrity    | Integrity reference.                                        |
| quality      | P F C R T I ratings (AIDCF-008 v1.1 meanings) and band Q0–Q5. |
| sufficiency  | S0–S5 for the claim.                                        |
| restrictions | Access or redistribution restrictions.                      |
| status       | AIDCF-008 lifecycle state.                                  |
| review       | Reviewer and acceptance.                                    |

## Findings register

| **Field**      | **Content**                                        |
|----------------|----------------------------------------------------|
| findingId      | Stable ID.                                         |
| criterion      | Requirement or assessment criterion.               |
| condition      | Evidenced state.                                   |
| evidence       | Evidence references.                               |
| cause          | Evidenced cause or labelled analysis.              |
| consequence    | Outcome effect.                                    |
| classification | IX.1 classification.                               |
| gateEffect     | Gates affected.                                    |
| scoreEffect    | Control result affected.                           |
| owner          | Action owner.                                      |
| action         | Required action.                                   |
| target         | Due date or trigger.                               |
| closure        | Closure evidence.                                  |
| status         | IX.1 status.                                       |

## UNKNOWN register

| **Field**      | **Content**                                    |
|----------------|------------------------------------------------|
| unknownId      | Stable ID.                                     |
| subject        | Affected object.                               |
| missingItem    | What is not known.                             |
| type           | U1–U10.                                        |
| severity       | US1–US5.                                       |
| decisionEffect | Gate, ceiling, condition or confidence effect. |
| evidenceNeeded | Evidence or method to resolve.                 |
| owner          | Resolution owner.                              |
| trigger        | Review trigger.                                |
| status         | OPEN, RESOLVED, ACCEPTED_AS_LIMITATION, SUPERSEDED. |

## Gate register

| **Field**      | **Content**                                              |
|----------------|----------------------------------------------------------|
| gateId         | CG-01 to CG-15.                                          |
| applicability  | In scope, APPROVED_NA or NOT_ASSESSED.                   |
| criticalControls | CRITICAL controls and results.                         |
| evidence       | Evidence floor and achieved sufficiency.                 |
| states         | Operating states evaluated.                              |
| scenarios      | Scenarios evaluated.                                     |
| result         | PASS, FAIL, UNKNOWN, APPROVED_NA, NOT_ASSESSED.          |
| findings       | Linked Findings.                                         |
| unknown        | Linked UNKNOWN Records.                                  |
| decisionEffect | Ceiling under AIDCF-010.                                 |
| closure        | Closure requirements.                                    |
| review         | Technical and independent review.                        |

## Decision register

| **Field**      | **Content**                                                    |
|----------------|----------------------------------------------------------------|
| decisionId     | Stable ID.                                                     |
| question       | Decision question.                                             |
| subject        | Capability Instance and Service Outcomes.                      |
| scope          | Boundary, states and period.                                   |
| recommendation | Recommended decision state.                                    |
| gates          | Gate summary reference.                                        |
| unknown        | Controlling UNKNOWN Records.                                   |
| scores         | Score Snapshot reference.                                      |
| conditions     | Conditions.                                                    |
| decision       | Canonical decision state.                                      |
| lifecycle      | DRAFT, RECOMMENDED, APPROVED, ACTIVE, SUSPENDED, WITHDRAWN, SUPERSEDED, EXPIRED. |
| authority      | Decision authority.                                            |
| validity       | Validity end and triggers.                                     |
| supersession   | Superseded and superseding IDs.                                |

## Action register

| **Field**       | **Content**                              |
|-----------------|------------------------------------------|
| actionId        | Stable ID.                               |
| source          | Finding, UNKNOWN Record or condition.    |
| action          | Action description.                      |
| owner           | Accountable owner.                       |
| priority        | Priority.                                |
| dependency      | Dependencies.                            |
| target          | Due date or event.                       |
| interimControl  | Interim safeguard.                       |
| closureEvidence | Required closure evidence.               |
| validation      | Reviewer validation.                     |
| status          | Open, in progress, closure submitted, closed. |

## Continuing dashboard

| **Field**       | **Content**                                     |
|-----------------|-------------------------------------------------|
| decision        | Current decision state and lifecycle state.     |
| gates           | Current Gate Results.                           |
| evidenceHealth  | Evidence freshness and STALE flags.             |
| coverage        | Coverage of monitored claims.                   |
| sourceOutage    | Sources unavailable and duration.               |
| controlDrift    | Configuration or performance drift detected.    |
| dependencyDrift | Dependency changes detected.                    |
| triggers        | Triggers fired and status.                      |
| findings        | Open Findings.                                  |
| criticalUnknown | Open US4 and US5 UNKNOWN Records.               |
| actions         | Overdue actions.                                |
| validity        | Validity end.                                   |

# Domain reporting annexes

Every R3 Domain Report and every domain section of R2 contains: purpose and Required Functions; scope, interfaces, providers and operating states; control and family results by claim type; evidence quality and sufficiency; scenarios and dependencies; gates affected (from registry `gateMappings`); domain score, coverage and band; Findings and UNKNOWN Records; bounded domain conclusion; sensitive-disclosure controls; Reassessment Triggers. The domain-specific reporting emphasis and the items that normally require "Highly restricted" classification are:

| **Domain** | **Reporting emphasis**                                                           | **Normally highly restricted**                                         |
|------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| GOV        | Decision rights in emergency states; exceptions and risk acceptances.             | Personal data in delegation records.                                   |
| CAP        | Outcome tolerances; usable versus installed capacity; envelope limits.            | Customer-specific capacity commitments.                                |
| DEP        | Material and common-mode dependencies; concentration; provider boundaries.        | Physical route details of diverse feeds.                               |
| PHY        | Life-safety status; structural limits; access-control weaknesses.                 | Security system layouts and weaknesses.                                |
| POW        | Capacity with one path out; transient response; tested load and duration.        | Detailed single-line diagrams and protection settings.                 |
| THM        | Capacity at design ambient; ride-through versus restoration time; leak isolation. | Detailed P&IDs and control setpoints.                                  |
| ENV        | Metric boundaries and calibration; hazardous-material controls.                   | —                                                                      |
| CMP        | Usable accelerator capacity; firmware baseline conformity; error trends.          | Cluster management interfaces and credentials.                         |
| STO        | Checkpoint restore results versus tolerance; recovery-copy separation.            | Storage administrative paths.                                          |
| NET        | Fabric fault domains; management and out-of-band independence.                   | Network topology details and management addresses.                     |
| OPS        | Staffing, permits, alarm load and change control.                                 | —                                                                      |
| RES        | Exercised scenarios and measured recovery; untested scenarios.                    | Detailed recovery runbooks.                                            |
| SUP        | Evidence rights; provenance; remote-support controls.                             | Supplier commercial terms.                                             |
| SEC        | Authority over infrastructure; automation limits; detection coverage.             | Vulnerabilities, identities, privileged paths and allowlists.          |
| EVA        | Evidence integrity; UNKNOWN handling; reassessment timeliness.                    | —                                                                      |

# Machine-readable reporting package

Schemas support reporting tools without delegating authority.

| **Artifact**                     | **Purpose**                                                              |
|----------------------------------|--------------------------------------------------------------------------|
| report-metadata.schema.json      | Part IV metadata.                                                        |
| executive-report.schema.json     | R1 structure.                                                            |
| technical-report.schema.json     | R2 structure.                                                            |
| assurance-statement.schema.json  | AS-01 to AS-08.                                                          |
| decision-wording.json            | Part V controlled wording, keyed by canonical decision and lifecycle state. |
| evidence-register.schema.json    | Evidence disclosures.                                                    |
| finding-register.schema.json     | Findings and management response.                                        |
| unknown-register.schema.json     | UNKNOWN Records.                                                         |
| gate-register.schema.json        | Gate Results and effects.                                                |
| decision-register.schema.json    | Recommendation, decision and validity.                                   |
| continuing-dashboard.schema.json | Monitored claims, source health, drift and triggers.                     |
| public-summary.schema.json       | Permitted external disclosure.                                           |
| conformance-tests                | Consistency, non-certification, security and supersession.              |

Ontology and validation shapes are published under AIDCF-014 and AIDCF-016.

# Graph mappings

Reporting objects use the canonical AIDCF-014 classes and relationships and preserve source lineage.

| **Reporting object** | **AIDCF-014 class or relationship**                                        |
|----------------------|----------------------------------------------------------------------------|
| Report               | AssuranceReport                                                            |
| Statement            | AssuranceStatement                                                         |
| Decision             | AssuranceDecision; AssuranceDecision REPORTED_IN AssuranceReport / AssuranceStatement |
| Evidence register    | EvidencePackage                                                            |
| Finding              | Finding                                                                    |
| UNKNOWN              | UnknownRecord                                                              |
| Gate                 | GateResult                                                                 |
| Distribution         | DistributionControl                                                        |
| Action               | Action; REQUIRES_ACTION, CLOSED_BY                                         |
| Correction           | New AssuranceReport version SUPERSEDES the corrected version (correction reason recorded) |
| Supersession         | SUPERSEDES                                                                 |

Report sections, disclosure profiles, management responses and validity conditions are carried as properties of AssuranceReport and AssuranceStatement. Previous non-canonical names CORRECTS, REPORTS and the classes ReportSection, DisclosureProfile, EvidenceManifest, FindingRegister, UnknownRegister, GateRegister, ManagementResponse and ValidityCondition are replaced as shown. A report reports a decision; it never creates one.

# Annex A — Conformance validation and requirement mapping

The following requirements are validation rules applied to every reporting package.

**RAS-REQ-014** Capability Instance, Service Outcomes, scope, operating states and period shall be explicit in every report and statement.

**RAS-REQ-015** Criteria and artifact versions shall be identified.

**RAS-REQ-016** Intended users and use shall be stated.

**RAS-REQ-017** Management responses shall be separate from the assessor conclusion.

**RAS-REQ-018** No report shall claim certification, accreditation, guarantee or universal compliance.

**RAS-REQ-019** Sensitive infrastructure paths shall be disclosed only under Part XIII controls.

**RAS-REQ-020** Every Finding and decision claim shall be traceable to the approved snapshot.

**RAS-REQ-021** Validity, conditions and triggers shall be present.

**RAS-REQ-022** Correction and supersession shall preserve history.

**RAS-REQ-023** Continuing-assurance reports shall name the monitored claims and blind spots.

**RAS-REQ-024** Automation shall not approve conclusions or release reports.

**RAS-REQ-025** A cross-report consistency check shall be completed before release.

**RAS-REQ-026** Technical and independent approvals shall be recorded before release.

| **v1.0 validation** | **v1.1 requirement**          |
|---------------------|-------------------------------|
| RAS-VAL-001         | RAS-REQ-001            |
| RAS-VAL-002         | RAS-REQ-014                   |
| RAS-VAL-003         | RAS-REQ-015                   |
| RAS-VAL-004         | RAS-REQ-016                   |
| RAS-VAL-005         | RAS-REQ-008         |
| RAS-VAL-006         | RAS-REQ-010             |
| RAS-VAL-007         | RAS-REQ-009           |
| RAS-VAL-008         | RAS-REQ-017                   |
| RAS-VAL-009         | RAS-REQ-018                   |
| RAS-VAL-010         | RAS-REQ-002          |
| RAS-VAL-011         | RAS-REQ-019                   |
| RAS-VAL-012         | RAS-REQ-020                   |
| RAS-VAL-013         | RAS-REQ-021                   |
| RAS-VAL-014         | RAS-REQ-022                   |
| RAS-VAL-015         | RAS-REQ-023                   |
| RAS-VAL-016         | RAS-REQ-024                   |
| RAS-VAL-017         | RAS-REQ-025                   |
| RAS-VAL-018         | RAS-REQ-026                   |

Other identifier changes: artifact ID AIDCF-RAS-001 → AIDCF-012; the six "Controlled Wording" sections → Part V; decision labels "ADVERSE / NOT ASSURED" and "UNKNOWN / INCONCLUSIVE" → NOT_ASSURED and INCONCLUSIVE; SUSPENDED → lifecycle notice (V.2, AS-06); fifteen identical domain reporting annexes → one domain reporting table; "Review and Release Gates" → AIDCF-011 Part XXII.

# Annex B — Review and release

The authoritative list of reviewer roles and release-gate states is in AIDCF-011 Part XXII and is not repeated here. Review of this document by the reviewer roles assigned to AIDCF-012 in that table is pending; this document has not been released.

## Final doctrine

AIDCF reports and statements communicate an approved assurance record. They do not create evidence, improve a score, neutralise UNKNOWN, override a critical gate, transfer assurance or establish certification. Every package remains bounded, traceable, appropriately protected, consistent with the technical record and authorised by a competent issuer.
