**AIDCF**

# CAPABILITY ASSURANCE MATURITY MODEL

*AI Data Centre Facilities Assurance Framework*

Version 1.0

A diagnostic model of how well an organisation is equipped to produce, sustain and act on capability-centred AI infrastructure assurance

Artifact ID: AIDCF-017  
Short code: CMM  
Artifact type: Normative standard (diagnostic)  
Status: Draft for controlled review  
Author: Siva Sethumadhavan

# Document control

| **Field** | **Value** |
|---|---|
| Title | AIDCF Capability Assurance Maturity Model |
| Public ID | AIDCF-017 |
| Short code (requirement IDs) | CMM |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Depends on | AIDCF-001 (§25, §55, §71 commitment 8); AIDCF-002 (vocabularies, IM codes, interpretation rules); AIDCF-006 (APS-046 maturity separation); AIDCF-008; AIDCF-011 (Assurance Levels AL0–AL6) |
| Downstream users | Programme sponsors and planners (AIDCF-011); assessors (AIDCF-009); reporting (AIDCF-012); tooling (AIDCF-014, AIDCF-016) |
| Normative language | As defined in AIDCF-002 Section 4 |

## Revision history

| **Version** | **Date** | **Summary** |
|---|---|---|
| 1.0 | 2026-10-10 | First issue: IM0–IM5 levels, ten maturity dimensions with observable indicators, rating method, link to AIDCF-011 programme planning, maturity-to-AL recommendation, anti-gaming rules, self-assessment questionnaire and record schema. |

# Part I – Purpose, status and doctrine

## 1. Purpose

AIDCF-001 §55 commits AIDCF to a maturity model that defines levels and criteria while ensuring that maturity "does not override critical gates, replace engineering analysis, prove resilience, demonstrate compliance or convert UNKNOWN into confidence". This document fulfils that commitment.

The model answers one question: **how well is this organisation equipped to generate, maintain and act on AIDCF assurance for a declared Capability Instance?** It does not answer whether the infrastructure is adequate. An organisation can be highly mature and operate a facility whose Assurance Decision is NOT_ASSURED (for example, because a well-run assurance practice has correctly identified that the utility supply cannot support the declared tolerance). An immature organisation can operate a facility whose safeguards are, in fact, sound; it simply cannot yet demonstrate it.

Maturity is useful for three purposes:

1. **Programme planning.** Choosing the Assurance Level (AIDCF-011) that a programme can realistically reach, and the readiness work needed first.
2. **Improvement.** Identifying which assurance practices are weakest and most likely to produce UNKNOWN-heavy or unreliable results.
3. **Diagnosis of results.** Explaining why an assessment produced many UNKNOWN Records, stale evidence or unowned dependencies.

## 2. Scope

The model rates ten **maturity dimensions** (Part III) of the assurance practice surrounding a declared scope: an organisation, or part of one, responsible for one or more Capability Instances. It applies to owners, operators, colocation providers, tenants with infrastructure responsibilities and assurance providers assessing their own practice.

It does not rate equipment, sites, designs or individual controls' effectiveness; those are the subject of Control Assessments (AIDCF-009), Gate Results and Assurance Decisions (AIDCF-010).

## 3. Doctrine: maturity is diagnostic

> **CMM-REQ-001 Diagnostic status.** A maturity rating shall be treated as diagnostic information only. It shall not be used as, converted into, or substituted for a control result, a Gate Result, a decision state, a confidence level, an evidence sufficiency level or a score.
>
> **CMM-REQ-002 No decision effect.** No maturity rating shall raise or lower a control result, change a Gate Result, change a decision ceiling, waive an evidence floor or close an UNKNOWN Record.
>
> **CMM-REQ-003 Separate presentation.** Where a maturity profile appears in an AIDCF report, it shall be presented in a section separate from Control Assessment results, Gate Results and the Assurance Decision, and shall carry the statement: "Maturity describes the institutionalisation of assurance practice; it is not a measure of infrastructure adequacy and does not form part of the Assurance Decision."

The reverse is also true: a favourable Assurance Decision does not establish maturity. A single well-evidenced assessment can be produced by heroic effort in an organisation whose practice is IM1.

## 4. Two uses of the IM scale

AIDCF-002 defines one scale, **Implementation Maturity IM0–IM5**, used in two places:

| **Use** | **Subject** | **Recorded on** | **Owner** |
|---|---|---|---|
| Control-level IM | The practice required by a single control, in a single scope | ControlAssessment, as a diagnostic attribute beside the control result | AIDCF-009 (assessor records) |
| Dimension-level IM | One of the ten maturity dimensions of an organisation's assurance practice | Maturity Assessment record (Part VIII) | This document |

The level meanings are the same in both uses. Control-level IM is never the control result: a control can be IM4 (the practice has operated consistently for a year) and NONCONFORMING (because the practice, though consistent, does not meet the control's criteria, for example a rigorously followed maintenance regime on a UPS whose battery runtime no longer meets the declared autonomy).

# Part II – Maturity levels

## 5. Level definitions

| **Level** | **Name** | **Definition** | **Typical evidence** |
|---|---|---|---|
| IM0 | Absent | The practice is not performed, or there is no evidence that it is. | — |
| IM1 | Initial | Performed ad hoc or reactively; depends on specific individuals; inconsistent across the scope; little or no documentation. | E6 interviews; isolated E1 or E3 records |
| IM2 | Defined | Documented, approved and owned; scope and responsibilities stated; not yet consistently implemented across the declared scope. | E1 approved procedures, RACI, standards |
| IM3 | Implemented | Implemented across the declared scope; records exist and reconcile to the definition; gaps are known and tracked. | E1 + E2 configuration/records + E3 sampled records |
| IM4 | Operating | Operates consistently over a representative period, across operating states where relevant; measured; exceptions detected and handled; survives staff changes. | E3 over a representative period; exception and metric records; E6 corroborated |
| IM5 | Optimised | Measured against objectives; improved through incidents, tests, exercises and independent challenge; improvements demonstrated in later cycles; practice anticipates change (density, technology, supplier). | E4 exercise/test lessons; E5 independent review; trend records showing improvement |

## 6. Level rules

1. **Cumulative.** A level is achieved only when the indicators for that level and every lower level are met.
2. **Scope-bound.** A level applies to the declared scope (organisation unit, sites, Capability Instances). A practice that is IM4 in one hall and IM2 in another is IM2 for a scope that includes both, with the variation recorded.
3. **Evidence-bound.** A level is rated only on evidence meeting the minimum pattern in Section 5; an indicator whose evidence is missing is not met (it is not assumed met).
4. **Time-bound.** A rating is as of a date. IM4 and IM5 require evidence over a period; the period is stated. A rating older than the programme's reassessment interval, or predating a material organisational change, is stale.
5. **No rounding up.** Partial achievement of a level is reported as the lower level with the met indicators of the higher level listed.

> **CMM-REQ-004 Cumulative rating.** A dimension shall be rated at the highest level for which all indicators of that level and every lower level are met for the whole declared scope, on evidence meeting the level's minimum pattern.
>
> **CMM-REQ-005 Rating metadata.** Every rating shall record the scope, as-of date, evidence period, evidence references, rater, reviewer and any indicators of the next level already met.

# Part III – Maturity dimensions and observable indicators

## 7. The ten dimensions

| **Code** | **Dimension** | **Question** | **Principal AIDCF links** |
|---|---|---|---|
| MD-01 | Governance | Is assurance directed, owned and resourced? | GOV domain; AIDCF-006; CG-13 |
| MD-02 | Capability definition | Are Capability Instances, Service Outcomes and tolerances defined and maintained? | CAP domain; CG-01 |
| MD-03 | Dependency visibility | Are dependencies, fault domains and concentration known, owned and current? | DEP, RES-02; CG-02, CG-03, CG-09 |
| MD-04 | Evidence management | Is evidence collected, protected, graded and retained to AIDCF-008? | EVA-01, EVA-02; CG-11 |
| MD-05 | Assessment practice | Are assessments planned, executed and reviewed to AIDCF-009? | EVA-03, EVA-04 |
| MD-06 | Gate discipline | Are Critical Gates applied without compensation, and UNKNOWN preserved? | EVA-05, GOV-04; CG-11, CG-12 |
| MD-07 | Change and reassessment | Do changes and events trigger impact analysis and reassessment? | OPS-05, CAP-06, EVA-06; CG-14 |
| MD-08 | Machine traceability | Are assurance records held as AIDCF-014 objects with lineage? | AIDCF-014, AIDCF-016 |
| MD-09 | Independence and review | Are conclusions challenged by competent, independent reviewers? | GOV-06, GOV-04; AIDCF-011 |
| MD-10 | Resilience practice | Are failure, containment and recovery tested and learned from? | RES, OPS-04; CG-09, CG-10 |

## 8. Indicators by dimension

Indicators are observable: each can be checked by inspecting a record, a configuration or an activity. Each row lists what is newly true at that level; lower-level indicators remain required.

### 8.1 MD-01 Governance

| **Level** | **Observable indicators** |
|---|---|
| IM0 | No assigned accountability for infrastructure assurance; no decision owner for reliance on facilities. |
| IM1 | Individuals commission reviews when prompted (incident, customer request); no charter; findings tracked informally. |
| IM2 | Approved assurance charter or policy; named sponsor and decision authorities; RACI for capability, dependency and evidence ownership; risk-acceptance authority defined. |
| IM3 | Charter applied to all in-scope Capability Instances; every critical function and dependency has a recorded owner; assurance plan exists and is resourced; risk acceptances recorded with authority and expiry. |
| IM4 | Governance forum meets on a defined cadence with minutes showing decisions on findings, UNKNOWNs and gate outcomes; overdue actions escalated; ownership survives staff turnover. |
| IM5 | Governance effectiveness reviewed against objectives; assurance priorities adjusted from incidents, near misses and changes in AI density and technology; independent challenge of governance recorded and acted on. |

### 8.2 MD-02 Capability definition

| **Level** | **Observable indicators** |
|---|---|
| IM0 | Infrastructure described only as sites, halls and equipment; no Capability Instance or Service Outcome records. |
| IM1 | Capabilities named informally (for example in sales or capacity documents); outcomes implied by SLAs; tolerances absent. |
| IM2 | Capability register template and outcome taxonomy approved; definitions of Capability Instance, Service Outcome and tolerance adopted per AIDCF-002. |
| IM3 | Every in-scope Capability Instance has owner, boundary, architecture baseline, Service Outcomes with metrics and tolerances, criticality rationale and declared operating states; Decision Questions recorded for programmes. |
| IM4 | Register maintained through lifecycle events (expansion, densification, workload changes); outcome measurements collected against tolerances over a representative period; stale records detected. |
| IM5 | Tolerances revisited with decision owners using operational and incident data; graceful-degradation priorities tested; capability definitions anticipate planned technology transitions (for example air-to-liquid cooling, new accelerator generations). |

### 8.3 MD-03 Dependency visibility

| **Level** | **Observable indicators** |
|---|---|
| IM0 | Dependencies not recorded beyond equipment single-line and schematic drawings. |
| IM1 | Dependencies known by experienced staff; partial lists exist for some systems; external dependencies (utility, fuel, carriers, OEMs) not linked to functions. |
| IM2 | Dependency record schema (AIDCF-003) adopted; method for discovery, common-mode and fault-domain analysis defined; boundary-crossing dependencies required to be recorded. |
| IM3 | Dependency graph for each in-scope Capability Instance covers electrical, thermal, hydraulic, network, control-system, timing, human, supplier and recovery dependencies; fault domains and shared providers recorded; owners assigned; discovery coverage stated. |
| IM4 | Graph reconciled to as-built and observed state on a defined cadence and after changes; drift detected; concentration and substitutability reviewed; dependency health indicators monitored. |
| IM5 | Hidden dependencies found through incidents, exercises and independent review are fed back into method; common-mode analysis extends to firmware baselines, configuration sources, support personnel and sub-tier suppliers; reduction of concentration measured. |

### 8.4 MD-04 Evidence management

| **Level** | **Observable indicators** |
|---|---|
| IM0 | Evidence produced only when requested, from wherever it can be found. |
| IM1 | Documents and records exist in multiple uncontrolled locations; provenance and dates often unclear; commissioning records partly missing. |
| IM2 | Evidence ownership, repository, classification and retention defined; AIDCF-008 classes and metadata adopted; evidence-system conformance target set (EC level). |
| IM3 | Mandatory metadata recorded for evidence in scope; integrity at least I2 for gate-relevant evidence; evidence linked to assertions; manifests maintained for Evidence Packages; achieves EC3. |
| IM4 | Evidence currency monitored against freshness rules; stale and expiring evidence flagged before reliance; conflicts recorded and worked through the AIDCF-008 conflict workflow; achieves EC4. |
| IM5 | Evidence produced as a by-product of operation (telemetry, configuration export, test automation) with I3+ integrity; quality vectors trended; recurring U1–U3 UNKNOWN causes eliminated; achieves EC5. |

### 8.5 MD-05 Assessment practice

| **Level** | **Observable indicators** |
|---|---|
| IM0 | No assessments against defined criteria. |
| IM1 | Checklist audits or vendor reviews, not tied to capability outcomes or claim types. |
| IM2 | AIDCF-009 procedures adopted; claim types and Assurance Levels used to plan; sampling rules defined; assessor competence (AC levels) defined. |
| IM3 | Assessments record one result per control, claim type and scope; samples documented and reproducible; Findings carry criterion, condition, cause, consequence; workpapers reviewed. |
| IM4 | Assessment results consistent across assessors (sampled re-performance); specialist involvement (electrical, mechanical, OT, HPC) planned and evidenced; safe-testing authorisations obtained before intrusive validation. |
| IM5 | Calibration exercises between assessors; methods improved from review findings and appeals; assessment results predict subsequent incidents or test failures (backward review). |

### 8.6 MD-06 Gate discipline

| **Level** | **Observable indicators** |
|---|---|
| IM0 | Overall ratings or averages are the only conclusion. |
| IM1 | Some "showstopper" issues recognised informally; UNKNOWNs often resolved by assumption. |
| IM2 | Critical Gate catalogue, roll-up rule and UNKNOWN severity tests adopted; prohibition on compensation documented. |
| IM3 | Every assessment records Gate Results for all applicable gates with evidence references; UNKNOWN Records carry type and severity; decision ceilings applied; no conditional gate states used. |
| IM4 | Gate outcomes reviewed by a party independent of fieldwork; overrides (downward only) recorded with authority; no instance found in sampled history of UNKNOWN converted to pass or of a gate FAIL averaged away. |
| IM5 | Gate criteria and floors calibrated from incidents and exercises; gate evaluation partly automated with human approval; trend of US4/US5 UNKNOWNs reported to governance and reducing. |

### 8.7 MD-07 Change and reassessment

| **Level** | **Observable indicators** |
|---|---|
| IM0 | Changes made without assurance impact consideration. |
| IM1 | Major projects reviewed; routine changes (firmware, set-points, topology, suppliers) not assessed for assurance impact. |
| IM2 | Change process requires assurance impact assessment; Reassessment Triggers defined for decisions; temporary configurations required to be recorded as states. |
| IM3 | Every change record in scope references affected Capability Instances, dependencies and claims; triggers recorded on every active decision; decision lifecycle states (SUSPENDED, EXPIRED) used. |
| IM4 | Triggers fire from events (incidents, change records, evidence expiry) within a defined latency; suspended decisions are not relied upon; post-change validation evidence collected. |
| IM5 | Change-impact analysis uses the dependency graph to identify affected claims automatically for human review; reassessment effort targeted by impact; lessons from change-induced incidents incorporated. |

### 8.8 MD-08 Machine traceability

| **Level** | **Observable indicators** |
|---|---|
| IM0 | Assurance held in narrative documents and spreadsheets without stable identifiers. |
| IM1 | Some registers with local identifiers; links between controls, evidence and decisions held in prose. |
| IM2 | AIDCF-014 classes, identifiers and canonical vocabularies adopted; target conformance level (TDS-T level) set. |
| IM3 | Records for the full chain (Capability Instance to Assurance Decision) held as AIDCF-014 objects and relationships; canonical codes used; reaches TDS-T2 traceability. |
| IM4 | Validation (schema and shape) run on every release; reverse traceability queries (decision to evidence) answered without manual reconstruction; snapshots immutable; reaches TDS-T5. |
| IM5 | Event-driven impact analysis and continuing-assurance feeds operational (TDS-T6); conformance test suite passed (TDS-T7); exchange with AI Trust Graph through governed handoffs. |

### 8.9 MD-09 Independence and review

| **Level** | **Observable indicators** |
|---|---|
| IM0 | Conclusions issued by those who performed or own the work, without review. |
| IM1 | Peer review on request; conflicts of interest not recorded. |
| IM2 | Independence and competence requirements defined (AIDCF-011, AIDCF-009 AC levels); conflict declarations required; appeal and challenge route defined. |
| IM3 | Technical review and independent review recorded for every decision; reviewer competence matches the domains assessed; conflicts declared and managed. |
| IM4 | Reviews demonstrably change outcomes when warranted (review records show challenges raised and resolved); dissent preserved; commercial pressure on conclusions escalated and recorded. |
| IM5 | Periodic external review of the assurance practice; reviewer rotation; review quality itself sampled and improved. |

### 8.10 MD-10 Resilience practice

| **Level** | **Observable indicators** |
|---|---|
| IM0 | Failure, containment and recovery not analysed or tested beyond equipment commissioning. |
| IM1 | Some component tests (generator runs, UPS transfers) performed; integrated or recovery scenarios not exercised; results not linked to outcomes. |
| IM2 | Resilience scenarios, test programme and safe-testing authorisation process defined (AIDCF-004 scenarios; V-level selection); recovery plans exist for power, cooling, compute, storage, network and control plane. |
| IM3 | Scenario library covers maintenance-induced, recovery-induced and cross-domain paths for each in-scope capability; component and integrated tests performed to plan; results linked to safeguards and outcomes. |
| IM4 | Integrated tests and exercises repeated on a defined cadence across declared states; recovery times measured against tolerances; defects tracked to closure and retested. |
| IM5 | Exercise scope grows with risk (compound and cross-boundary scenarios); results calibrate tolerances, gate criteria and design standards; near misses analysed with the same rigour as incidents. |

> **CMM-REQ-006 Indicator basis.** Ratings shall be made against the observable indicators in Section 8, or against an approved profile extension that preserves their meaning; an indicator shall be treated as met only where evidence demonstrates it for the whole declared scope.

# Part IV – Rating method

## 9. Procedure

1. **Declare scope.** Organisation unit, sites, Capability Instances, as-of date and evidence period.
2. **Collect evidence.** Use AIDCF-008 classes and metadata. The minimum evidence pattern rises with the level (Section 5): an IM4 rating without E3 records across a representative period is not supportable.
3. **Rate each dimension.** Apply the cumulative rule (Section 6). Record met indicators of the next level.
4. **Record UNKNOWN.** Where evidence for an indicator cannot be obtained, record a maturity UNKNOWN (type U1–U10) and rate the dimension at the highest level fully evidenced. Maturity UNKNOWNs do not receive US severities and have no decision effect; they are not entered in the assessment's UNKNOWN register unless the same missing information also affects a control result or gate, in which case the UNKNOWN Record is raised in the assessment in its own right.
5. **Review.** A reviewer who did not perform the rating confirms it (MD-09 practice applies to maturity ratings as well).
6. **Present the profile.** Show all ten dimensions with level, as-of date and evidence period.

## 10. Profile, not a number

The output is a ten-dimension profile, for example:

| **Dimension** | MD-01 | MD-02 | MD-03 | MD-04 | MD-05 | MD-06 | MD-07 | MD-08 | MD-09 | MD-10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Level (illustrative)** | IM3 | IM3 | IM2 | IM2 | IM3 | IM2 | IM1 | IM1 | IM3 | IM2 |

> **CMM-REQ-007 Profile presentation.** Maturity shall be presented as a profile of all rated dimensions. If a single summary level is shown, it shall be the minimum across dimensions and shall be displayed with the full profile; averages, weighted sums and percentages of maturity shall not be published.
>
> **CMM-REQ-008 Evidence for maturity.** A maturity rating at IM3 or above shall be supported by E2 or E3 evidence; IM4 by E3 evidence over a stated representative period; IM5 by E4 or E5 evidence of improvement cycles in addition. E6 (interview) evidence alone shall support no rating above IM1.

# Part V – Maturity and programme planning

## 11. How maturity informs AIDCF-011 programmes

Assurance Levels (AIDCF-011) describe the depth of a programme: AL0 Discovery, AL1 Readiness, AL2 Design, AL3 Implementation, AL4 Operational, AL5 Effectiveness and resilience, AL6 Continuing. Maturity predicts whether a programme at a given level will produce defensible results or a decision dominated by UNKNOWN Records. The relationship is advisory: maturity never forbids or permits an Assurance Level, and a programme at any level is governed only by AIDCF-011 entry criteria and the evidence floors of AIDCF-008.

Maturity informs planning in five ways:

| **Planning decision** | **Maturity signal** |
|---|---|
| Recommended next Assurance Level | Section 12 thresholds |
| Readiness work before fieldwork | Dimensions below threshold become AL1 readiness actions |
| Evidence request lead time and sampling depth | Low MD-04 predicts U1/U3 UNKNOWNs; plan longer evidence lead times and larger exception sampling |
| Specialist and independence resourcing | Low MD-09 calls for an external reviewer; low MD-05 calls for a lead assessor at AC-3 or above |
| Reassessment interval | Low MD-07 calls for shorter validity periods and more triggers on decisions |

## 12. Recommended next Assurance Level

A programme **should** plan the highest Assurance Level for which all thresholds below are met, and treat unmet thresholds as AL1 readiness actions. Thresholds are cumulative: AL4 requires the AL2 and AL3 thresholds too.

| **Target level** | **Recommended minimum dimension levels (in addition to lower targets)** | **Rationale** |
|---|---|---|
| AL0 Discovery | None | Discovery is how maturity gaps are found. |
| AL1 Readiness | MD-01 ≥ IM1; MD-02 ≥ IM1 | A sponsor and a named capability are needed to scope readiness. |
| AL2 Design | MD-01 ≥ IM2; MD-02 ≥ IM2; MD-03 ≥ IM2; MD-04 ≥ IM2 | Design claims need defined outcomes and tolerances (CG-01), a dependency method (CG-03) and controlled design evidence. |
| AL3 Implementation | MD-02 ≥ IM3; MD-03 ≥ IM3; MD-04 ≥ IM3; MD-05 ≥ IM2; MD-07 ≥ IM2 | As-built reconciliation needs implemented registers, a dependency graph and evidence metadata; changes during reconciliation must be visible. |
| AL4 Operational | MD-04 ≥ IM4; MD-05 ≥ IM3; MD-06 ≥ IM3; MD-07 ≥ IM3; MD-09 ≥ IM3 | Operation claims need period evidence with currency control, consistent assessment, gate discipline and independent review. |
| AL5 Effectiveness and resilience | MD-03 ≥ IM4; MD-06 ≥ IM4; MD-10 ≥ IM3 | Effectiveness and resilience claims depend on current dependency graphs, independently reviewed gates and an executed scenario test programme. |
| AL6 Continuing | MD-07 ≥ IM4; MD-08 ≥ IM3; MD-04 ≥ IM4 | Continuing assurance needs trigger-driven reassessment and machine-held lineage, otherwise evidence refresh cannot be targeted. |

**Example (illustrative).** For the profile in Section 10, every AL1 and AL2 threshold is met (MD-01 IM3, MD-02 IM3, MD-03 IM2, MD-04 IM2). AL3 is not: MD-03 and MD-04 are IM2 against a threshold of IM3, and MD-07 is IM1 against IM2. The recommendation is an AL2 Design programme, with AL1 readiness actions to complete the dependency graph, implement evidence metadata and introduce change-impact assessment before an AL3 programme is planned.

> **CMM-REQ-009 Planning use.** Programme plans under AIDCF-011 should record the current maturity profile, the recommended next Assurance Level from Section 12, and the readiness actions for any dimension below threshold. Where a programme proceeds at a level above the recommendation, the plan shall record the rationale and the expected effect on UNKNOWN Records.
>
> **CMM-REQ-010 Level independence.** A maturity profile shall not be used to grant entry to an Assurance Level, to waive AIDCF-011 entry criteria, or to infer that claims at that level are supported.

# Part VI – Anti-gaming rules

Maturity models are easily turned into targets. The following rules prevent maturity ratings from substituting for assurance or from being optimised at the expense of it.

| **ID** | **Rule** |
|---|---|
| AG-01 | **No decision use.** Maturity is excluded from scores, gate evaluation, decision ceilings and confidence (Section 3). |
| AG-02 | **No inherited maturity.** A rating for one organisation unit, site or capability shall not be applied to another. Corporate policy maturity is not site practice maturity. |
| AG-03 | **No paper levels.** IM3 and above require evidence of implementation and operation, not documents (Section 10). A policy library alone supports at most IM2. |
| AG-04 | **No level skipping.** Indicators of a higher level do not compensate for unmet lower-level indicators. |
| AG-05 | **No averaging.** No mean, weighted or percentage maturity score is published (Section 10). |
| AG-06 | **No self-certification beyond IM3.** Ratings of IM4 and IM5 shall be confirmed by a reviewer independent of the practice rated. |
| AG-07 | **No target-only scope.** The declared scope shall not be narrowed after rating to exclude weak halls, sites or teams; scope changes create a new rating. |
| AG-08 | **No marketing claims.** Maturity shall not be described as certification, accreditation or an AIDCF "rating" of a facility. Permitted wording: "AIDCF-017 maturity profile, self-assessed (or independently reviewed), as of [date], for [scope]". |
| AG-09 | **Staleness.** A rating predating a material organisational change (ownership, operator, outsourcing, major staff turnover, merger of operations teams) or older than the programme's reassessment interval shall be marked stale and not used for planning. |
| AG-10 | **Contradiction check.** Where assessment results contradict a maturity rating (for example MD-04 rated IM4 while the assessment raises many U1 Missing or U3 Stale UNKNOWNs on gate evidence), the rating shall be reviewed and the outcome recorded. |

> **CMM-REQ-011 Anti-gaming.** Rules AG-01 to AG-10 shall be applied to every maturity rating; a rating that breaches any of them shall be withdrawn.

# Part VII – Self-assessment questionnaire

Each question has an indicative answer scale. The answer suggests a level; the rating itself is made against the indicators in Section 8 with evidence. "Evidence to have ready" lists what a reviewer will ask for.

| **Ref** | **Dimension** | **Question** | **Answer indicates** | **Evidence to have ready** |
|---|---|---|---|---|
| SQ-01 | MD-01 | Is there an approved charter naming the sponsor and the decision authority for reliance on AI infrastructure? | No → IM0–1; approved → IM2; applied to all in-scope capabilities → IM3 | Charter; RACI; delegation records |
| SQ-02 | MD-01 | Do governance minutes from the last representative period show decisions on findings, UNKNOWNs and gate outcomes? | None → ≤ IM2; yes → IM4 indicator | Minutes; action log |
| SQ-03 | MD-01 | Are risk acceptances recorded with authority, scope and expiry? | No → ≤ IM1; yes → IM3 indicator | Risk-acceptance register |
| SQ-04 | MD-02 | For each in-scope Capability Instance, are Service Outcomes stated with metrics and tolerances approved by the decision owner? | None → IM0–1; template only → IM2; all instances → IM3 | Capability register; outcome records |
| SQ-05 | MD-02 | Are outcome measurements collected against tolerances over time? | No → ≤ IM3; yes → IM4 indicator | Outcome trend data |
| SQ-06 | MD-03 | Does a dependency graph exist covering electrical, thermal, hydraulic, network, control, human, supplier and recovery dependencies for each capability? | Partial lists → IM1; method only → IM2; full graph → IM3 | Graph export; discovery-coverage statement |
| SQ-07 | MD-03 | When was the graph last reconciled to as-built and observed state, and was drift recorded? | Never → ≤ IM3; on cadence and after changes → IM4 indicator | Reconciliation records |
| SQ-08 | MD-03 | Have common-mode reviews covered firmware baselines, configuration sources, support personnel and sub-tier suppliers? | No → ≤ IM4; yes, with findings acted on → IM5 indicator | Common-mode analysis; actions |
| SQ-09 | MD-04 | Can gate-relevant evidence be produced with source, collection time, custodian and integrity level within the agreed request window? | Rarely → IM1; defined but inconsistent → IM2; yes → IM3 | Sample of Evidence Objects with metadata |
| SQ-10 | MD-04 | Is evidence expiry monitored so that stale evidence is flagged before reliance? | No → ≤ IM3; yes → IM4 indicator | Freshness reports |
| SQ-11 | MD-05 | Do assessment records give one result per control, claim type and scope, with documented samples? | No → ≤ IM2; yes → IM3 | Workpapers; sampling plans |
| SQ-12 | MD-05 | Has re-performance by a second assessor been sampled, and were differences resolved? | No → ≤ IM3; yes → IM4 indicator | Re-performance records |
| SQ-13 | MD-06 | Are Gate Results recorded for all applicable gates in every assessment, using only PASS, FAIL, UNKNOWN, APPROVED_NA, NOT_ASSESSED? | No → ≤ IM2; yes → IM3 | Gate Result records |
| SQ-14 | MD-06 | In the sampled history, has any UNKNOWN been resolved by assumption or any gate FAIL offset by a high score? | Yes → ≤ IM2 (and raise a governance finding); no, independently checked → IM4 indicator | Decision history; review records |
| SQ-15 | MD-07 | Do change records reference affected capabilities, dependencies and claims? | No → ≤ IM2; yes → IM3 | Change records |
| SQ-16 | MD-07 | When a Reassessment Trigger last fired, how long did it take to suspend reliance and start reassessment? | No triggers defined → ≤ IM1; triggers defined → IM2; fired and acted on within defined latency → IM4 indicator | Event and decision-lifecycle records |
| SQ-17 | MD-08 | Are assurance records held as AIDCF-014 objects with canonical codes and stable identifiers? | No → IM0–1; adopted → IM2; full chain → IM3 | Data export; validation report |
| SQ-18 | MD-08 | Can the question "which evidence supports this decision?" be answered by query? | No → ≤ IM3; yes → IM4 indicator | Query output |
| SQ-19 | MD-09 | Is every decision reviewed by someone independent of fieldwork with competence in the domains assessed? | No → ≤ IM1; required → IM2; recorded every time → IM3 | Review records; competence records |
| SQ-20 | MD-09 | Do review records show challenges that changed outcomes? | No evidence → ≤ IM3; yes → IM4 indicator | Review records |
| SQ-21 | MD-10 | Is there a scenario library covering maintenance-induced, recovery-induced and cross-domain failures for each capability? | No → IM0–1; defined → IM2; covering each capability → IM3 | Scenario library |
| SQ-22 | MD-10 | Have integrated tests or exercises been repeated across declared states, with recovery times compared to tolerances? | Component tests only → IM1; planned → IM2–3; repeated and measured → IM4 | Test and exercise reports |
| SQ-23 | MD-10 | Have test and exercise results changed tolerances, gate criteria or design standards? | No → ≤ IM4; yes → IM5 indicator | Change records; revised standards |

# Part VIII – Maturity record

## 13. Record schema

AIDCF-014 v1.0 has no dedicated maturity class. Until AIDCF-016 introduces one, a maturity rating is carried as an `Assessment` whose profile is `AIDCF-017`, with one rating entry per dimension.

| **Field** | **Content** |
|---|---|
| maturityAssessmentId | Stable identifier |
| modelVersion | AIDCF-017 version |
| scope | Organisation unit, sites, Capability Instances |
| asOfDate; evidencePeriod | Dates |
| ratings[] | {dimension MD-01..MD-10, level IM0..IM5, indicatorsMet[], nextLevelIndicatorsMet[], evidenceRefs[], unknowns[]} |
| rater; reviewer; independence | Roles and independence statement |
| status | DRAFT, REVIEWED, APPROVED, SUPERSEDED, STALE |
| recommendedNextAL | Output of Section 12 |
| readinessActions[] | Actions for dimensions below threshold |

> **CMM-REQ-012 Record separation.** Maturity records shall be stored and exchanged separately from ControlAssessment results, GateResults and AssuranceDecisions, and no relationship of type RESULTS_IN, EVALUATES_GATE, CONSTRAINS or RECOMMENDS shall originate from a maturity record.

# Part IX – Conformance requirements index

| **ID** | **Title** | **Section** |
|---|---|---|
| CMM-REQ-001 | Diagnostic status | 3 |
| CMM-REQ-002 | No decision effect | 3 |
| CMM-REQ-003 | Separate presentation | 3 |
| CMM-REQ-004 | Cumulative rating | 6 |
| CMM-REQ-005 | Rating metadata | 6 |
| CMM-REQ-006 | Indicator basis | 8 |
| CMM-REQ-007 | Profile presentation | 10 |
| CMM-REQ-008 | Evidence for maturity | 10 |
| CMM-REQ-009 | Planning use | 12 |
| CMM-REQ-010 | Level independence | 12 |
| CMM-REQ-011 | Anti-gaming | Part VI |
| CMM-REQ-012 | Record separation | 13 |

The series runs consecutively from CMM-REQ-001 to CMM-REQ-012.

*Final doctrine.* Maturity tells an organisation how ready it is to know. It never tells anyone what is known.
