# AIDCF-007A Control Catalogue — GOV Governance, Accountability and Assurance Direction

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-GOV](../../../aidcf-018-domain-guides/AIDCF-018-GOV_Governance_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-GOV-001](#mcf-gov-001) | Governance Charter | DIRECTIVE | DESIGN | AL2 | — | CG-13 |
| [MCF-GOV-002](#mcf-gov-002) | Decision Rights | PREVENTIVE | IMPLEMENTATION | AL3 | CG-13 | — |
| [MCF-GOV-003](#mcf-gov-003) | Committee Oversight | DETECTIVE | OPERATION | AL4 | — | CG-13 |
| [MCF-GOV-004](#mcf-gov-004) | Methodology Ownership | DIRECTIVE | IMPLEMENTATION | AL3 | — | — |
| [MCF-GOV-005](#mcf-gov-005) | RACI and Role Ownership | DIRECTIVE | IMPLEMENTATION | AL3 | CG-13 | — |
| [MCF-GOV-006](#mcf-gov-006) | Critical Function Accountability | DIRECTIVE | IMPLEMENTATION | AL3 | CG-13 | CG-03 |
| [MCF-GOV-007](#mcf-gov-007) | Risk Acceptance Authority | PREVENTIVE | OPERATION | AL4 | CG-13 | — |
| [MCF-GOV-008](#mcf-gov-008) | Evidence Custody | PREVENTIVE | OPERATION | AL4 | — | CG-13 |
| [MCF-GOV-009](#mcf-gov-009) | Policy Hierarchy | DIRECTIVE | DESIGN | AL2 | — | — |
| [MCF-GOV-010](#mcf-gov-010) | Technical Standard Baselines | DIRECTIVE | IMPLEMENTATION | AL3 | — | CG-14 |
| [MCF-GOV-011](#mcf-gov-011) | Exception Governance | PREVENTIVE | OPERATION | AL4 | — | CG-14, CG-13 |
| [MCF-GOV-012](#mcf-gov-012) | Document Lifecycle | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-14 |
| [MCF-GOV-013](#mcf-gov-013) | Assurance Plan | DIRECTIVE | DESIGN | AL2 | — | — |
| [MCF-GOV-014](#mcf-gov-014) | Risk Appetite Linkage | DIRECTIVE | DESIGN | AL2 | — | — |
| [MCF-GOV-015](#mcf-gov-015) | Critical Gate Governance | PREVENTIVE | OPERATION | AL4 | — | CG-13 |
| [MCF-GOV-016](#mcf-gov-016) | Independent Review | DETECTIVE | EFFECTIVENESS | AL5 | — | CG-13 |
| [MCF-GOV-017](#mcf-gov-017) | Stakeholder Obligations | DIRECTIVE | DESIGN | AL2 | — | CG-01 |
| [MCF-GOV-018](#mcf-gov-018) | Regulatory Monitoring | DETECTIVE | OPERATION | AL4 | — | CG-14 |
| [MCF-GOV-019](#mcf-gov-019) | Customer Commitments | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-01 |
| [MCF-GOV-020](#mcf-gov-020) | External Reporting | PREVENTIVE | OPERATION | AL4 | — | — |
| [MCF-GOV-021](#mcf-gov-021) | Conflict Management | PREVENTIVE | OPERATION | AL4 | — | — |
| [MCF-GOV-022](#mcf-gov-022) | Assessor Independence | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-13 |
| [MCF-GOV-023](#mcf-gov-023) | Competence Management | PREVENTIVE | OPERATION | AL4 | — | — |
| [MCF-GOV-024](#mcf-gov-024) | Appeal and Challenge | CORRECTIVE | OPERATION | AL4 | — | — |

## GOV-01 Governance architecture

### MCF-GOV-001

**Governance Charter** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Establish one approved charter that defines who directs, oversees and is accountable for assurance of each in-scope Capability Instance, which decision questions the programme serves, and the limits of reliance on AIDCF conclusions.

**Requirement.** The governing body shall approve an assurance governance charter that names the in-scope Capability Instances, the accountable executive, the assurance programme lead, the decision authority and the oversight committee; states the decision questions served and the intended users of conclusions; defines the programme model (self-assessment, co-sourced, second-party or independent provider); and states that AIDCF conclusions do not replace engineering, statutory or safety approval and are not certification. The accountable executive shall review the charter at no more than the governance charter review interval and after any change of ownership, organisation or programme model, and shall record the outcome of each review.

**Assessment criteria**

1. The charter in use is the approved version, and the approval was given by the governing body or by a body holding a documented delegation from it.
2. The charter names, by role and current incumbent, the accountable executive, assurance programme lead, decision authority and oversight committee.
3. Every Capability Instance recorded as in scope in the capability register (MCF-CAP-001) falls within the charter scope; no in-scope instance is uncovered.
4. The charter states the decision questions served, the intended users, the programme model and the non-substitution limits (no replacement of engineering, statutory or safety approval; no certification).
5. The charter defines the independence safeguards required before a material gate result or Assurance Decision is relied upon.
6. The most recent charter review is within the review interval and post-dates every charter trigger event (ownership, reorganisation, programme-model change).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Governance charter review interval | months | 12 | Capability-profile parameter set by the governing body; illustrative, shortened where the capability is changing rapidly |

**Minimum evidence**

- Approved governance charter with version identifier and effective date
- Governing-body resolution or minute recording approval of that charter version
- Delegation instrument where approval was given below the governing body
- Reconciliation of charter scope to a dated extract of the capability register
- Record of the most recent charter review and its outcome

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E6 |
| optionalClasses | E5 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Charter version in force at the assessment date and the preceding review cycle |
| independence | Approval evidence shall originate from the governing-body secretariat or equivalent, not from the charter author |
| mandatoryItems | Approved governance charter with version identifier and effective date; Governing-body resolution or minute recording approval of that charter version |
| acceptableAlternatives | Terms of reference of a board-delegated committee containing equivalent content, supported by the delegation instrument |
| unknownEffect | US3 Material: control result UNKNOWN; CG-13 gate-level evaluation records the gap; decision capped at CONDITIONALLY_ASSURED with a named condition to evidence charter approval |
| reassessmentTriggers | Change of accountable executive or decision authority; Organisational restructuring affecting assurance reporting lines; Change of programme model or assurance provider; Addition of a Capability Instance to scope |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY, RECONCILIATION

**Assessment procedure**

1. Obtain the charter in force and its approval record; confirm version identity and the authority of the approving body.
2. Reconcile the charter scope to a dated capability register extract and list any in-scope Capability Instance not covered.
3. Confirm the named roles against current appointment records.
4. Inspect the charter for decision questions, intended users, programme model, independence safeguards and non-substitution statements.
5. Interview the accountable executive to confirm their understanding of charter authority and the escalation route to the governing body.
6. Compare the last review date with the review interval and with trigger events since that review.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to every AIDCF assurance programme. For a single commissioned assessment, an engagement letter approved by the decision authority may satisfy the control if it contains the same content; full non-applicability is not permitted.

**Lifecycle stages.** PLAN, DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** No approved authority exists for issuing assurance conclusions; Charter scope omits a Capability Instance that is reported on; AIDCF conclusion is represented as engineering approval or certification; Charter remains in force after the accountable executive has left

**Testing safety.** Non-intrusive document review and interview only; no site or system testing. Governing-body papers can be commercially sensitive and are accessed through the evidence lead under the classification rules of AIDCF-008.

**UNKNOWN rule.** If the approval record cannot be produced, or the approving body's authority cannot be established, record a U1 or U6 UNKNOWN against the charter; approval shall not be inferred from the charter being in use.

**Ontology classes.** AssuranceProgram, CapabilityInstance, AssuranceDecision · **Related controls.** MCF-GOV-002, MCF-GOV-003, MCF-CAP-001, MCF-EVA-009

**Informative references.** ISO 37000 (governance of organizations); ISO/IEC 38500 (governance of IT for the organization); ISO/IEC/IEEE 15026-2 (assurance case); AIDCF-011 Assurance Program Framework

### MCF-GOV-002

**Decision Rights** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that every consequential decision affecting the AI capability and its assurance (risk acceptance, gate disposition, Assurance Decision, emergency load action, test authorisation, exception approval) has a defined, delegated decision right that is used as designed, including in emergency states.

**Requirement.** The accountable executive shall maintain a decision-rights matrix that, for each decision class affecting an in-scope Capability Instance, names the role holding the decision right, its financial or risk limits, the escalation route, the delegation and sub-delegation rules, and the emergency decision rights that apply when the normal holder is unavailable. The assurance programme lead shall ensure that workflow and approval systems enforce the matrix, and that every decision in the sample population was taken by a role holding the right at the time it was taken.

**Assessment criteria**

1. A decision-rights matrix exists, is approved by the accountable executive and covers at minimum: risk acceptance, gate disposition, Assurance Decision issue, exception approval, hazardous test authorisation, and emergency load curtailment or shutdown of AI workloads.
2. Each decision class names a single holding role, limits, escalation route and the emergency alternate.
3. Approval workflows (change, exception, risk and decision registers) are configured so that only roles holding the right can approve the corresponding record type.
4. In a sample of decisions taken during the assessment period, every approver held the decision right and was within limits on the date of the decision.
5. Emergency decision rights are defined for EMERGENCY and RECOVERY states and at least one exercised or rehearsed emergency decision shows the alternate route was usable.
6. No decision in the sample was taken by an assessor on behalf of management.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Decision sample size per decision class | records | 10 or the full population if smaller | Judgemental sample per AIDCF-008 sampling principles; illustrative, increased if exceptions are found |

**Minimum evidence**

- Approved decision-rights matrix with version and approval record
- Delegation and sub-delegation instruments in force during the period
- Export of approver role configuration from change, exception, risk and decision workflow tools
- Sampled decision records with approver identity, role and date
- Emergency decision-right definition and record of its exercise or rehearsal

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY; RECOVERY |
| periodCoverage | Current matrix plus decisions taken in the twelve months preceding the assessment, or since the last assessment if shorter |
| independence | Workflow configuration shall be extracted by the assessor or under assessor observation, not supplied as a screenshot by the approver population |
| mandatoryItems | Approved decision-rights matrix with version and approval record; Export of approver role configuration from change, exception, risk and decision workflow tools; Sampled decision records with approver identity, role and date |
| acceptableAlternatives | Where approvals are paper-based, a complete approval log reconciled to signed records replaces the workflow configuration export |
| unknownEffect | US4 Critical: CG-13 Gate Result UNKNOWN; decision capped at LIMITED until the decision-rights evidence is produced |
| reassessmentTriggers | Reorganisation or change in delegation limits; Introduction or replacement of an approval workflow tool; A decision found to have been taken outside its decision right; Change of emergency response arrangements |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, SAMPLING, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Obtain the decision-rights matrix and confirm it covers the minimum decision classes, including emergency classes.
2. Extract approver role configuration from each workflow tool and reconcile it to the matrix; list roles able to approve without holding the right.
3. Define the population of decisions per class for the period and select a sample using the stated sample size.
4. For each sampled decision, verify approver identity, role held on that date and limits, against appointment and delegation records.
5. Review the emergency decision-right record and interview the emergency alternate on how they would exercise it.
6. Expand the sample by the same size again for any class where a nonconforming decision is found, and record the result.

**Gate mappings.** CG-13 Responsibility and authority (CRITICAL)

**Applicability.** Applies to every in-scope Capability Instance. Decision classes that do not occur (for example no hazardous testing is permitted) may be marked NOT_APPLICABLE individually with rationale; the matrix as a whole is always applicable.

**Lifecycle stages.** PLAN, OPERATE, CHANGE · **Operating states.** NORMAL, EMERGENCY, RECOVERY

**Failure modes addressed.** Unauthorised risk acceptance; Gate disposition or Assurance Decision issued by a role without authority; No one able to authorise emergency curtailment of AI load when the normal holder is unavailable; Workflow tool allows any user to approve; Assessor makes a management decision

**Testing safety.** Read-only extraction of workflow configuration under the tool owner's supervision; no test approvals are submitted in production systems. Emergency decision rights are examined by walkthrough or tabletop, never by declaring a real emergency.

**UNKNOWN rule.** If a workflow tool configuration cannot be extracted, or decisions cannot be tied to the approver's role on the date taken, record a U2 or U6 UNKNOWN; the decision class is treated as uncontrolled for CG-13 until resolved.

**Ontology classes.** AssuranceDecision, Action, ReviewRecord · **Related controls.** MCF-GOV-001, MCF-GOV-005, MCF-GOV-007, MCF-EVA-019

**Informative references.** ISO 37000 (governance of organizations); COSO Internal Control - Integrated Framework; ISO/IEC 38500 (governance of IT for the organization)

### MCF-GOV-003

**Committee Oversight** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that a standing oversight committee actually receives, challenges and acts on assurance information about the AI capability, including gate failures, critical UNKNOWN Records and overdue actions, at a frequency matched to the rate of change.

**Requirement.** The governing body shall constitute an assurance oversight committee with written terms of reference, quorum and membership that includes at least one member independent of the operating line. The committee chair shall ensure that the committee meets at no more than the oversight meeting interval, receives at every meeting the current gate register, UNKNOWN register (US3 and above), findings register and overdue action list for each in-scope Capability Instance, records challenge and decisions in minutes, and tracks its own actions to closure.

**Assessment criteria**

1. Terms of reference define purpose, membership, quorum, frequency, independence of at least one member, and escalation to the governing body.
2. Meetings were held at intervals not exceeding the oversight meeting interval throughout the assessment period and each was quorate.
3. Every meeting pack in the sample contained the current gate register, UNKNOWN register (US3 and above), findings register and overdue action list.
4. Minutes record challenge or questions on at least each gate FAIL and each US4/US5 UNKNOWN Record presented, and the decision or action taken.
5. Committee actions are tracked and closed with evidence, and overdue committee actions are escalated to the governing body.
6. Any gate FAIL or US4/US5 UNKNOWN Record arising between meetings was notified to the chair within the out-of-cycle notification time.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Oversight meeting interval | months | 3 | Capability-profile parameter; illustrative, shortened during build, major change or after a gate FAIL |
| Out-of-cycle notification time for gate FAIL or US4/US5 UNKNOWN | working days | 5 | Capability-profile parameter; illustrative |

**Minimum evidence**

- Approved committee terms of reference
- Meeting calendar and attendance records for the period
- Sampled meeting packs with register extracts
- Approved minutes and committee action log
- Out-of-cycle notifications for gate FAIL or US4/US5 UNKNOWN events

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | At least four consecutive meeting cycles, or all meetings in the last twelve months |
| independence | Minutes shall be the approved record held by the committee secretary; drafts or summaries prepared by management are not sufficient |
| mandatoryItems | Approved committee terms of reference; Approved minutes and committee action log; Sampled meeting packs with register extracts |
| acceptableAlternatives | Recorded and transcribed meetings with approved action logs may replace minutes where the organisation's records policy permits |
| unknownEffect | US3 Material: control result UNKNOWN; decision capped at CONDITIONALLY_ASSURED with a condition that oversight operation is evidenced |
| reassessmentTriggers | Change of chair or loss of the independent member; Two consecutive missed or inquorate meetings; A gate FAIL not presented to the committee; Change to terms of reference |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Obtain terms of reference and confirm membership, quorum, independence and escalation provisions.
2. List all meetings in the period from the calendar and attendance records; test interval and quorum for each.
3. Select meeting packs and confirm the four mandatory registers were included and were current at the meeting date.
4. Reconcile gate FAIL and US4/US5 UNKNOWN Records in the gate and UNKNOWN registers to the minutes; identify any not presented or not challenged.
5. Trace committee actions to closure evidence and confirm escalation of overdue items.
6. Interview the chair and the independent member on how challenge is exercised and recorded.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to every programme where conclusions are relied upon beyond the immediate management team. For a single assessment with no continuing programme, review of the result by the decision authority may substitute, recorded as NOT_APPLICABLE with rationale.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** Gate FAIL or critical UNKNOWN never reaches oversight; Committee receives scores only and no gate or UNKNOWN information; Oversight meets too infrequently for the rate of capability change; Committee actions are not tracked

**Testing safety.** Document and interview review only. Observation of a live committee meeting requires the chair's prior consent and is confined to the agenda items concerning the in-scope capability.

**UNKNOWN rule.** If minutes for a meeting in the period are missing, record a U1 UNKNOWN for that meeting and do not count it as held; if more than one meeting in the period is affected, the criterion on meeting interval is not met.

**Ontology classes.** AssuranceProgram, GateResult, UnknownRecord, Action, ReviewRecord · **Related controls.** MCF-GOV-001, MCF-GOV-015, MCF-EVA-014, MCF-EVA-013

**Informative references.** ISO 37000 (governance of organizations); Institute of Internal Auditors Three Lines Model; AIDCF-012 Reporting and Assurance Statement Standard

### MCF-GOV-004

**Methodology Ownership** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that the assessment methodology actually applied (AIDCF artifact versions, capability profile, scoring version, any local tailoring) has a named owner, is version-controlled, and is identical to the version declared in reports.

**Requirement.** The assurance programme lead shall appoint a methodology owner who shall maintain a controlled methodology baseline listing the AIDCF artifact versions (including AIDCF-007A, AIDCF-008, AIDCF-009 and AIDCF-010), the capability profile, scoring version and every approved local tailoring, each with rationale and approval. The methodology owner shall ensure that assessment tools and templates are configured to that baseline and that every report declares the baseline version actually used.

**Assessment criteria**

1. A methodology owner is appointed in writing and holds competence in AIDCF and assurance methods.
2. A controlled methodology baseline exists listing artifact versions, capability profile version, scoring version and approved tailorings with rationale and approver.
3. No tailoring weakens a critical-gate rule, an evidence floor or the UNKNOWN treatment of AIDCF-008 and AIDCF-010.
4. The control registry, vocabularies and scoring logic configured in the assessment tool match the declared baseline version (hash or version comparison).
5. Every report in the sample declares a baseline version, and that version was the one in force on the assessment date.

**Minimum evidence**

- Methodology owner appointment record
- Methodology baseline record with versions, tailorings, rationale and approvals
- Tool configuration export showing registry, vocabulary and scoring versions
- Sampled reports with declared methodology baseline

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E7 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Methodology baseline in force and reports issued in the last twelve months |
| independence | Tool configuration comparison shall be performed by the assessor against published release manifests, not by the tool owner alone |
| mandatoryItems | Methodology baseline record with versions, tailorings, rationale and approvals; Tool configuration export showing registry, vocabulary and scoring versions |
| acceptableAlternatives | Where no tool is used, controlled template versions with checksums replace the tool configuration export |
| unknownEffect | US3 Material: affected control and gate results UNKNOWN where the methodology version cannot be established; decision capped at CONDITIONALLY_ASSURED |
| reassessmentTriggers | New AIDCF artifact release adopted; Approval of a new local tailoring; Assessment tool upgrade or replacement; Report found to declare an incorrect baseline |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INSPECTION, SAMPLING

**Assessment procedure**

1. Confirm the methodology owner appointment and competence record.
2. Review the methodology baseline and each tailoring; test each tailoring against gate rules, evidence floors and UNKNOWN treatment.
3. Extract registry, vocabulary and scoring versions from the assessment tool and compare them with the release manifest of the declared baseline.
4. Sample issued reports and compare the declared baseline with the baseline in force on each assessment date.
5. Record any divergence as a Finding and identify affected results.

**Gate mappings.** None

**Applicability.** Applies to every programme that issues AIDCF control, gate or decision results.

**Lifecycle stages.** PLAN, OPERATE, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** Results produced under an undeclared or superseded control registry; Local tailoring silently weakens a gate or evidence floor; Scoring version in tool differs from the version reported; No one accountable for methodology changes

**Testing safety.** Read-only inspection of tool configuration in a non-production or export copy; no change to scoring logic is made during assessment.

**UNKNOWN rule.** If the tool configuration cannot be compared with a release manifest, record a U8 (method uncertain) UNKNOWN against every result produced with that tool in the period.

**Ontology classes.** AssuranceProgram, ReleaseManifest, AssessmentProcedure, ScoreSnapshot · **Related controls.** MCF-GOV-012, MCF-GOV-013, MCF-EVA-001, MCF-EVA-020

**Informative references.** ISO/IEC/IEEE 15026-2 (assurance case); ISO 9001 (quality management systems) - control of documented information; AIDCF-014 End-to-End Traceability and Machine-Executable Data Standard

## GOV-02 Accountability and responsibility

### MCF-GOV-005

**RACI and Role Ownership** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that every role named in the assurance programme and in operation of the AI capability has a current incumbent, a defined RACI position for each process, and no unresolved overlap or gap between owner, operator and providers.

**Requirement.** The accountable executive shall maintain a RACI that assigns, for each in-scope process (capability management, assurance, evidence, change, incident, recovery, provider management), exactly one Accountable role and the Responsible, Consulted and Informed roles across owner, operator, tenants and providers. The assurance programme lead shall reconcile the RACI to current appointments and to contractual responsibility clauses at least at the RACI reconciliation interval and after every organisational or contract change.

**Assessment criteria**

1. The RACI covers every in-scope process and assigns exactly one Accountable role to each.
2. Every role in the RACI has a named current incumbent and a deputy.
3. RACI assignments for providers and tenants match the responsibility clauses of the corresponding contracts or service descriptions.
4. No process has a responsibility split between owner, operator and provider that leaves an activity with no Responsible role.
5. Reconciliation to appointments and contracts occurred within the reconciliation interval and after each trigger event.
6. Interviewed role holders describe their RACI position consistently with the document.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| RACI reconciliation interval | months | 6 | Capability-profile parameter; illustrative |

**Minimum evidence**

- Approved RACI with version
- Current appointment or HR role extract for named roles
- Responsibility clauses of operator, provider and tenant contracts
- RACI reconciliation record
- Interview notes from sampled role holders

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E6 |
| optionalClasses | E2; E7 |
| qualityFloor | P3 F3 C4 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | RACI in force and appointments current at the assessment date |
| independence | Interview evidence shall be obtained by the assessor directly from role holders, separately from the RACI author |
| mandatoryItems | Approved RACI with version; Responsibility clauses of operator, provider and tenant contracts; RACI reconciliation record |
| acceptableAlternatives | A responsibility matrix embedded in a service management system, exported with version metadata |
| unknownEffect | US4 Critical: CG-13 Gate Result UNKNOWN; decision capped at LIMITED |
| reassessmentTriggers | Organisational change; New, changed or terminated provider or tenant contract; Departure of an Accountable role holder; Incident in which responsibility was disputed |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INQUIRY, ANALYSIS

**Assessment procedure**

1. Obtain the RACI and confirm each in-scope process has exactly one Accountable role.
2. Reconcile named roles to current appointment records and identify vacancies or missing deputies.
3. Reconcile provider and tenant assignments to contractual responsibility clauses and list gaps or conflicts.
4. Analyse each process for activities with no Responsible role at owner/operator/provider interfaces.
5. Interview a sample of Accountable and Responsible role holders, including at least one provider role, and compare their description with the RACI.

**Gate mappings.** CG-13 Responsibility and authority (CRITICAL)

**Applicability.** Applies to every in-scope Capability Instance. Where the owner and operator are the same organisation, the owner/operator interface criteria are evaluated within the organisation.

**Lifecycle stages.** PLAN, BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Two parties each believe the other is responsible for an activity; Accountable role vacant; Provider contract assigns responsibility differently from the RACI; No deputy for an Accountable role during an emergency

**Testing safety.** Interview and document review only. Provider contract extracts may be commercially restricted; where access is limited, only responsibility clauses are disclosed under the evidence lead's restriction record.

**UNKNOWN rule.** If a provider or tenant contract cannot be accessed to confirm responsibility clauses, record a U2 UNKNOWN for that interface; it shall not be assumed that the provider is responsible.

**Ontology classes.** CapabilityInstance, RequiredFunction, Dependency, Action · **Related controls.** MCF-GOV-006, MCF-GOV-002, MCF-CAP-002

**Informative references.** ISO/IEC 20000-1 (service management system); ISO 37000 (governance of organizations); ISO/IEC 22237 series (data centre facilities and infrastructures) - management and operational information

### MCF-GOV-006

**Critical Function Accountability** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that every Required Function and material Dependency supporting an in-scope Service Outcome (power, cooling, compute, storage, network, control plane, external providers) has one accountable owner with authority to act, recorded in the assurance graph.

**Requirement.** The capability owner shall ensure that each Required Function and each material Dependency linked to an in-scope Service Outcome has exactly one accountable owner recorded in the assurance graph, that the owner holds the decision right to commit resources and to authorise degraded-state actions for that function, and that cross-organisational functions (for example utility supply, facility water, network carriers, cloud control planes) have both an internal accountable owner and a named counterparty contact. The assurance programme lead shall reconcile function ownership to the RACI and decision-rights matrix after every change to the Required Function or Dependency set.

**Assessment criteria**

1. Every Required Function and material Dependency in the assurance graph linked to an in-scope Service Outcome has exactly one accountable owner.
2. Each owner holds, in the decision-rights matrix, the right to commit resources and to authorise degraded-state actions for that function.
3. Each external or cross-organisational Dependency has an internal accountable owner and a named counterparty contact with a verified contact route.
4. Function ownership in the graph reconciles to the RACI and decision-rights matrix with no conflicts.
5. Ownership was reconciled after each addition, removal or change of a Required Function or Dependency in the period.

**Minimum evidence**

- Assurance graph extract of Required Functions and Dependencies with owner attributes
- RACI and decision-rights matrix extracts
- Counterparty contact register with last verification date
- Reconciliation record after each function or dependency change

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E7 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY |
| periodCoverage | Graph state at the assessment date and changes during the preceding twelve months |
| independence | The graph extract shall be produced by query executed or witnessed by the assessor |
| mandatoryItems | Assurance graph extract of Required Functions and Dependencies with owner attributes; RACI and decision-rights matrix extracts |
| acceptableAlternatives | Where no graph exists, a function and dependency register maintained under document control, with an explicit limitation recorded against traceability |
| unknownEffect | US4 Critical: CG-13 Gate Result UNKNOWN for each unowned critical function; decision capped at LIMITED |
| reassessmentTriggers | New Required Function or material Dependency identified; Change of provider for an external dependency; Owner departure; Incident revealing an unowned function |

**Assessment methods.** ANALYSIS, RECONCILIATION, DOCUMENT_REVIEW, INQUIRY

**Assessment procedure**

1. Query the assurance graph for all Required Functions and material Dependencies linked to in-scope Service Outcomes and their owner attributes.
2. Identify functions or dependencies with zero or more than one accountable owner.
3. Reconcile each owner to the decision-rights matrix for authority to commit resources and authorise degraded-state actions.
4. Test the counterparty contact route for a sample of external dependencies by confirming the last successful verification.
5. Interview a sample of owners, prioritising shared or external dependencies, on their authority and escalation in a degraded state.

**Gate mappings.** CG-13 Responsibility and authority (CRITICAL); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to every Required Function and material Dependency supporting an in-scope Service Outcome; dependencies assessed as non-material in the DEP domain are excluded with that rationale.

**Lifecycle stages.** DESIGN, BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY, RECOVERY

**Failure modes addressed.** Shared facility water loop has no single accountable owner across facility and IT teams; External carrier dependency has no internal owner; Owner lacks authority to authorise load shedding during a cooling degradation; Ownership not updated after a provider change

**Testing safety.** Graph queries are executed read-only. Contact-route verification uses existing records or a pre-agreed non-operational test message; it shall not simulate an incident to a provider.

**UNKNOWN rule.** Any Required Function or material Dependency whose owner cannot be established is recorded as a US4 UNKNOWN Record against CG-13; ownership shall not be presumed from organisational proximity.

**Ontology classes.** RequiredFunction, Dependency, ServiceOutcome, CapabilityInstance · **Related controls.** MCF-GOV-005, MCF-CAP-002, MCF-CAP-004, MCF-GOV-002

**Informative references.** ISO 22301 (business continuity management systems); ISO 55000 series (asset management); AIDCF-005 AIDCF-AI Trust Graph Integration Standard

### MCF-GOV-007

**Risk Acceptance Authority** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that residual risks, Findings left open and conditions attached to decisions are accepted only by a role holding risk-acceptance authority for that magnitude, with an expiry and review, and never by assessors.

**Requirement.** The accountable executive shall define risk-acceptance authority levels linked to the risk appetite (MCF-GOV-014) and impact tolerances (MCF-CAP-010). Each risk owner shall record every risk acceptance with the risk description, affected Service Outcomes and gates, residual consequence, compensating measures, acceptor, expiry date and review date. The assurance programme lead shall ensure that no acceptance of a risk that would cause a CRITICAL control or gate to be relied upon is recorded without the decision authority's approval, and that expired acceptances revert to open Findings.

**Assessment criteria**

1. Risk-acceptance authority levels are defined and linked to risk appetite and impact tolerance.
2. Every risk acceptance in the sample was made by a role holding authority for its magnitude on the date of acceptance.
3. Every acceptance records affected Service Outcomes and gates, residual consequence, compensating measures, expiry and review date.
4. No acceptance has passed its expiry date without renewal by an authorised acceptor or reversion to an open Finding.
5. No acceptance in the population was made or recommended for acceptance by an assessor.
6. No acceptance is used to convert a gate FAIL or US4/US5 UNKNOWN into PASS; such risks appear only as decision-level conditions.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum risk-acceptance validity | months | 12 | Capability-profile parameter; illustrative, shorter for acceptances touching gate-critical controls |

**Minimum evidence**

- Risk-acceptance authority schedule
- Risk register extract of acceptances in the period
- Sampled acceptance records with acceptor role and date
- Register of expired acceptances and their disposition

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | All acceptances active at any point in the twelve months preceding the assessment |
| independence | Assessor selects the sample from a full register extract; management selection of examples is not accepted |
| mandatoryItems | Risk-acceptance authority schedule; Risk register extract of acceptances in the period; Sampled acceptance records with acceptor role and date |
| acceptableAlternatives | Where risk acceptances are recorded in decision minutes rather than a register, a complete extraction from minutes reconciled to the action log |
| unknownEffect | US4 Critical: CG-13 Gate Result UNKNOWN; decision capped at LIMITED |
| reassessmentTriggers | Change of risk appetite or authority levels; Acceptance found to exceed authority; Expiry of acceptances touching gate-critical controls; Change of impact tolerance |

**Assessment methods.** SAMPLING, DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Obtain the authority schedule and confirm linkage to risk appetite and impact tolerance.
2. Extract the full population of acceptances active during the period and select a sample weighted to acceptances touching gate-critical controls.
3. For each sampled acceptance, verify acceptor authority on the date, completeness of required fields and expiry status.
4. Analyse the population for expired acceptances not renewed or reverted, and for acceptances used to clear a gate FAIL or US4/US5 UNKNOWN.
5. Confirm from engagement records that no assessor made or recommended an acceptance.

**Gate mappings.** CG-13 Responsibility and authority (CRITICAL)

**Applicability.** Applies whenever any residual risk, open Finding or decision condition is accepted for an in-scope Capability Instance.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Risk accepted by an operator below the authority threshold; Indefinite risk acceptance with no expiry; Gate FAIL hidden by a risk acceptance; Assessor accepts risk on management's behalf

**Testing safety.** Document and register review only; no operational activity.

**UNKNOWN rule.** If the acceptor's authority on the acceptance date cannot be established, record a U6 UNKNOWN and treat the acceptance as not made; the underlying Finding is reported as open.

**Ontology classes.** Finding, Action, AssuranceDecision, GateResult · **Related controls.** MCF-GOV-014, MCF-CAP-010, MCF-GOV-011, MCF-GOV-002

**Informative references.** ISO 31000 (risk management guidelines); COSO Enterprise Risk Management framework; ISO 37000 (governance of organizations)

### MCF-GOV-008

**Evidence Custody** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Assign accountable custody for assurance evidence so that every Evidence Object relied on by a decision has a custodian, an access policy and an unbroken custody record from collection to retention or destruction.

**Requirement.** The assurance programme lead shall appoint an evidence lead who shall assign a custodian role to each evidence repository and each Evidence Package, define who may read, add, alter, export, redact or destroy evidence, and ensure that every custody event defined in AIDCF-008 (transfer, access, export, alteration, redaction, retention action) is recorded. The evidence lead shall review custody records for Evidence Packages supporting gate results before each Assurance Decision is issued.

**Assessment criteria**

1. An evidence lead is appointed and each repository and Evidence Package supporting a gate or decision has a named custodian.
2. Access policies define permitted actions per role and are configured in the repository so that alteration and destruction are restricted to authorised roles.
3. For a sample of Evidence Objects supporting gate results, the custody log is complete from collection to current state with no unexplained gap.
4. Custody review of gate-supporting Evidence Packages was performed before each Assurance Decision in the period.
5. Transfers of evidence to or from providers are recorded with sender, receiver, method, time and integrity value.

**Minimum evidence**

- Evidence lead appointment and custodian register
- Repository access policy and role configuration export
- Custody logs for sampled Evidence Objects
- Pre-decision custody review records
- Provider evidence transfer records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E7 |
| qualityFloor | P4 F3 C4 R4 T3 I4 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Custody events for Evidence Objects supporting decisions issued in the last twelve months |
| independence | Custody logs shall be extracted from the repository system of record by the assessor, not compiled by the custodian |
| mandatoryItems | Repository access policy and role configuration export; Custody logs for sampled Evidence Objects; Pre-decision custody review records |
| acceptableAlternatives | For paper or physical evidence, a sealed-bag custody register with signatures and seal numbers |
| unknownEffect | US3 Material: affected gate evidence treated as integrity-uncertain (U7); dependent gate results may become UNKNOWN under CG-11 |
| reassessmentTriggers | Repository migration or platform change; Custodian change; Detected unauthorised access or alteration; New provider evidence exchange |

**Assessment methods.** INSPECTION, SAMPLING, RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Confirm evidence lead appointment and custodian assignment for each repository and gate-supporting package.
2. Extract role configuration and compare with the access policy; list roles able to alter or destroy evidence without authority.
3. Sample Evidence Objects supporting gate results and trace custody logs from collection to current state.
4. Verify pre-decision custody reviews for each decision in the period.
5. Trace a sample of provider evidence transfers and confirm integrity values were recorded and verified on receipt.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to all evidence relied on for control, gate or decision results. Operational records retained only in source systems are within scope when cited as evidence.

**Lifecycle stages.** PLAN, OPERATE, DECOMMISSION · **Operating states.** NORMAL

**Failure modes addressed.** Evidence altered after collection with no record; No custodian for provider-supplied test reports; Evidence destroyed before decision challenge period ends; Shared accounts used to upload evidence

**Testing safety.** Read-only inspection of repository configuration and logs. Any test of access restrictions uses a dedicated test account and test object approved by the evidence lead; production evidence is never altered.

**UNKNOWN rule.** If custody logs are absent for a period or object, record a U7 UNKNOWN against the affected Evidence Objects; they may not be used to support a gate result until integrity is re-established by re-collection or independent corroboration.

**Ontology classes.** EvidenceObject, EvidencePackage, DistributionControl · **Related controls.** MCF-EVA-002, MCF-EVA-006, MCF-EVA-004, MCF-EVA-003

**Informative references.** ISO/IEC 27037 (identification, collection, acquisition and preservation of digital evidence); ISO 15489-1 (records management); AIDCF-008 Evidence Model

## GOV-03 Policy and standards management

### MCF-GOV-009

**Policy Hierarchy** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure that policies, technical standards, procedures and runbooks governing the AI capability form a coherent hierarchy in which each lower document traces to a higher one and contradictions are identified and resolved.

**Requirement.** The policy owner shall maintain a policy hierarchy register that identifies, for each in-scope document, its level (policy, standard, procedure, runbook), parent document, owner, scope (sites, halls, clusters, systems) and approval status. The policy owner shall ensure that no procedure or runbook relies on a superseded or absent parent, and that identified contradictions between documents are recorded and resolved by the owner of the higher document.

**Assessment criteria**

1. A register exists listing each in-scope policy, standard, procedure and runbook with level, parent, owner, scope and approval status.
2. Every document below policy level traces to an approved, current parent.
3. Policy-level documents cover at minimum assurance, risk, change, incident, safety of work, information security, evidence and provider management for the in-scope capability.
4. Contradictions identified in the period (including those found by the assessor in a sample comparison) are recorded and resolved by the higher-document owner.
5. Scopes declared in documents cover all in-scope sites, halls and clusters without gaps.

**Minimum evidence**

- Policy hierarchy register
- Approved policy-level documents
- Sample of standards, procedures and runbooks with parent references
- Contradiction log and resolution records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1 |
| optionalClasses | E6; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Documents in force at the assessment date |
| independence | Contradiction comparison on a sample of document pairs shall be performed by the assessor |
| mandatoryItems | Policy hierarchy register; Approved policy-level documents |
| acceptableAlternatives | Document management system metadata export with parent-child links in place of a separate register |
| unknownEffect | US3 Material: control result UNKNOWN; reliance on procedures for affected controls is limited and recorded as a condition |
| reassessmentTriggers | New or withdrawn policy; New site, hall or cluster added to scope; Contradiction contributing to an incident |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION

**Assessment procedure**

1. Obtain the register and confirm completeness against the document management system.
2. Check that minimum policy topics are covered for the in-scope capability.
3. Trace a sample of procedures and runbooks, prioritising emergency and recovery runbooks, to approved current parents.
4. Compare a sample of document pairs at adjacent levels for contradictions in requirements, roles or limits.
5. Reconcile declared document scopes to the capability register and identify uncovered sites, halls or clusters.

**Gate mappings.** None

**Applicability.** Applies to every organisation operating or assuring an in-scope Capability Instance; for providers, applies to documents the provider makes available under contract.

**Lifecycle stages.** PLAN, DESIGN, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Runbook traces to a superseded standard; Contradictory limits in procedure and standard; No policy covering evidence or provider management; New cluster not covered by any operating procedure

**Testing safety.** Document review only; no runbook is exercised. Emergency runbooks are read in the document system, not at operational consoles.

**UNKNOWN rule.** If a document cited as parent cannot be produced, record a U1 UNKNOWN against the child document and treat the child as untraced.

**Ontology classes.** Control, ControlDomain, CapabilityInstance · **Related controls.** MCF-GOV-010, MCF-GOV-012, MCF-GOV-011

**Informative references.** ISO 9001 (quality management systems); ISO/IEC 27001 (information security management systems); ISO 37301 (compliance management systems)

### MCF-GOV-010

**Technical Standard Baselines** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that the engineering and technical standards baseline the capability is designed, built and operated against (electrical, mechanical, fire, OT security, accelerator platform, network and storage standards and vendor envelopes) is declared, versioned and actually applied to the as-built and as-configured state.

**Requirement.** The chief engineer for the capability shall declare a technical standards baseline listing each external standard family, internal engineering standard and OEM specification applied to in-scope infrastructure, with edition or version, scope of application and any declared deviation. The chief engineer shall ensure that design, commissioning and change records cite the baseline edition applied, and that adoption of a new edition is controlled through change control with impact assessment.

**Assessment criteria**

1. A technical standards baseline lists the standards, internal engineering standards and OEM specifications applied, with edition, scope and deviations.
2. The baseline covers each infrastructure domain in scope (power, thermal, physical, compute, storage, network, OT and control-plane security).
3. Design and commissioning records in a sample cite the baseline edition applied.
4. Each declared deviation has a rationale, a compensating measure and approval through exception governance (MCF-GOV-011).
5. Adoption of new editions or OEM specification revisions in the period was processed through change control with impact assessment.

**Minimum evidence**

- Technical standards baseline with editions and scope
- Sampled design and commissioning records citing the baseline
- Deviation register entries with approvals
- Change records for edition adoption

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Baseline in force and records produced since the last major design or commissioning event |
| independence | Domain specialists for each infrastructure domain shall confirm applicability of the listed standard families |
| mandatoryItems | Technical standards baseline with editions and scope; Deviation register entries with approvals |
| acceptableAlternatives | Design basis documents per domain that each list applied standards, consolidated by the assessor |
| unknownEffect | US3 Material: affected DESIGN claims in infrastructure domains may become UNKNOWN; decision condition recorded |
| reassessmentTriggers | New edition of an applied standard adopted; OEM specification revision for accelerators, CDUs or power equipment; New infrastructure domain or technology introduced (for example immersion cooling); Deviation approved |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, SAMPLING, INQUIRY

**Assessment procedure**

1. Obtain the baseline and confirm coverage of each in-scope infrastructure domain.
2. Ask each domain specialist to confirm that listed standard families are applicable and complete for their domain.
3. Sample design and commissioning records and verify citation of the baseline edition.
4. Trace deviations to approved exceptions and confirm compensating measures.
5. Trace edition adoptions in the period to change records with impact assessment.

**Gate mappings.** CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all in-scope infrastructure. Where a colocation provider owns the facility baseline, the provider's baseline is assessed through MCF-SUP controls and referenced here.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** Design built against an undeclared standard edition; OEM thermal or power envelope revision not reflected in design; Undocumented deviation from an applied standard; New technology deployed with no applicable standard declared

**Testing safety.** Document review only; no inspection of energised equipment is required for this control.

**UNKNOWN rule.** If the edition applied to a design cannot be determined, record a U8 UNKNOWN against the affected DESIGN claims in the relevant infrastructure domain.

**Ontology classes.** ArchitectureSnapshot, InfrastructureSystem, Control · **Related controls.** MCF-GOV-009, MCF-GOV-011, MCF-CAP-021

**Informative references.** ISO/IEC 22237 series (data centre facilities and infrastructures); EN 50600 series (data centre facilities and infrastructures); ASHRAE TC 9.9 thermal guidelines for data processing environments; IEC 62443 series (industrial automation and control systems security)

### MCF-GOV-011

**Exception Governance** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that every deviation from policy, technical baseline or control requirement is recorded, risk-assessed, approved by an authorised role, time-bound and visible in assurance reporting, so that exceptions do not silently accumulate into an unassessed configuration.

**Requirement.** The policy owner shall operate an exception process in which each exception records the requirement deviated from, affected Capability Instances, Service Outcomes, controls and gates, the risk assessment, compensating measures, approver, expiry and closure criteria. Exceptions affecting a gate-critical control shall be approved by the decision authority. The assurance programme lead shall ensure that the exception register is an input to every assessment and that expired exceptions are escalated to the oversight committee.

**Assessment criteria**

1. Every exception in the sample records the deviated requirement, affected scope, controls and gates, risk assessment, compensating measures, approver, expiry and closure criteria.
2. Exceptions affecting gate-critical controls were approved by the decision authority.
3. No exception in the register is past expiry without renewal or closure; expired exceptions were escalated to the oversight committee.
4. The exception register was used as an input to each assessment in the period and affected controls reference the relevant exceptions.
5. Configuration or practice found by the assessor to deviate from a requirement has a corresponding exception or is raised as a Finding.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum exception duration | months | 6 | Capability-profile parameter; illustrative, renewable once by the approver |

**Minimum evidence**

- Exception register extract for the period
- Sampled exception records with approvals
- Oversight committee records of expired-exception escalation
- Assessment planning records citing the exception register

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E2; E7 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | All exceptions active during the twelve months preceding the assessment |
| independence | Assessor compares observed configuration deviations with the register independently of the exception owner |
| mandatoryItems | Exception register extract for the period; Sampled exception records with approvals |
| acceptableAlternatives | Exception records held in a GRC tool, exported with full field history |
| unknownEffect | US3 Material: affected control results UNKNOWN where undeclared deviation cannot be excluded; decision condition recorded |
| reassessmentTriggers | Exception approved for a gate-critical control; Exceptions past expiry; Deviation discovered without an exception; Change in exception approval authority |

**Assessment methods.** SAMPLING, DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Extract the exception register for the period and analyse expiry status across the population.
2. Sample exceptions, weighting toward gate-critical controls, and test completeness and approver authority.
3. Confirm escalation of expired exceptions in oversight committee records.
4. Reconcile deviations observed in other domain assessments to the register and raise Findings for undeclared deviations.
5. Confirm that the assessment plan and affected control assessments reference active exceptions.

**Gate mappings.** CG-14 Change control (SUPPORTING); CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to every in-scope Capability Instance. If no exceptions exist, the control is still assessed by testing for undeclared deviations.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Temporary bypass of a protection or interlock left in place indefinitely; Exceptions approved by the requester; Exception register not used in assessment, so results ignore known deviations; Accumulated exceptions create an unassessed configuration

**Testing safety.** Register review only. Where the assessor verifies a deviation in a live system, it is by read-only inspection with the system owner present.

**UNKNOWN rule.** If the existence of undeclared deviations cannot be tested for a domain (for example configuration not accessible), record a U5 coverage-gap UNKNOWN for that domain against this control.

**Ontology classes.** Finding, Control, Action, ArchitectureSnapshot · **Related controls.** MCF-GOV-007, MCF-GOV-010, MCF-CAP-023

**Informative references.** ISO 37301 (compliance management systems); ISO/IEC 27001 (information security management systems); ISO 31000 (risk management guidelines)

### MCF-GOV-012

**Document Lifecycle** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that documents used to operate and assure the capability are controlled through creation, review, approval, publication, supersession and withdrawal, so that the version at the point of use is the approved current version.

**Requirement.** The policy owner shall define document lifecycle states, review intervals by document level and approval roles, and the document control administrator shall ensure that only approved current versions are published at points of use (control room, plant rooms, runbook systems, assessor workpaper templates), that superseded versions are withdrawn from points of use while retained in history, and that review dates are tracked.

**Assessment criteria**

1. Lifecycle states, review intervals by document level and approval roles are defined.
2. At a sample of points of use (including control room and runbook system), the version available is the approved current version.
3. Superseded documents are withdrawn from points of use and retained in history with supersession metadata.
4. No document in the sample is past its review date without a recorded extension.
5. Emergency and recovery runbooks are available at the point of use in a form usable during loss of the primary document system.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Runbook review interval | months | 12 | Capability-profile parameter; illustrative, shorter for emergency runbooks after change |

**Minimum evidence**

- Document control procedure
- Document management system version and status export
- Point-of-use inspection record
- Offline or alternate runbook availability record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F3 C3 R3 T4 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY |
| periodCoverage | Document versions current at the assessment date |
| independence | Point-of-use inspection shall be performed by the assessor |
| mandatoryItems | Document management system version and status export; Point-of-use inspection record |
| acceptableAlternatives | Controlled print register with issue and withdrawal signatures where points of use rely on printed documents |
| unknownEffect | US3 Material: affected OPERATION claims in operational domains may be qualified; decision condition recorded |
| reassessmentTriggers | Document management system replacement; Incident where an outdated document was used; Major change requiring runbook revision |

**Assessment methods.** INSPECTION, SAMPLING, RECONCILIATION

**Assessment procedure**

1. Obtain the document control procedure and confirm lifecycle states, review intervals and approval roles.
2. Select points of use, including the control room and runbook system, and compare available versions with the document management system.
3. Check that superseded versions are absent at points of use and present in history.
4. Test review dates on a sample of documents.
5. Inspect alternate availability of emergency and recovery runbooks for loss of the primary document system.

**Gate mappings.** CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all controlled documents used to operate or assure in-scope infrastructure.

**Lifecycle stages.** BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, EMERGENCY, RECOVERY

**Failure modes addressed.** Operator executes a superseded switching or cooling procedure; Emergency runbook unavailable when the document system is down; Assessor uses a superseded template; Review dates lapse unnoticed

**Testing safety.** Point-of-use inspection in control rooms and plant rooms is escorted, follows site induction and access rules, and does not involve touching operational equipment.

**UNKNOWN rule.** If the version at a point of use cannot be compared with the system of record, record a U6 UNKNOWN for that point of use.

**Ontology classes.** EvidenceObject, AssessmentProcedure, ReleaseManifest · **Related controls.** MCF-GOV-009, MCF-GOV-004, MCF-EVA-021

**Informative references.** ISO 9001 (quality management systems) - control of documented information; ISO 15489-1 (records management); ISO/IEC 20000-1 (service management system)

## GOV-04 Risk and assurance governance

### MCF-GOV-013

**Assurance Plan** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure that a risk-based assurance plan determines which Capability Instances, Service Outcomes, claim types and gates are assessed, at what Assurance Level, by whom and when, so that assurance effort follows consequence and change rather than convenience.

**Requirement.** The assurance programme lead shall prepare, and the oversight committee shall approve, an assurance plan for each planning period that, for each in-scope Capability Instance, states the decision questions, target Assurance Level (AL0-AL6), claim types and gates to be evaluated, assessment type, provider model, resourcing and schedule, and the rationale linking depth to criticality (MCF-CAP-009) and planned change (MCF-CAP-023). The programme lead shall record and approve deviations from the plan.

**Assessment criteria**

1. An approved assurance plan exists for the current period.
2. For each in-scope Capability Instance the plan states decision questions, target Assurance Level, claim types, gates, assessment type, provider model and schedule.
3. Planned depth is justified by criticality classification and planned material change; higher-criticality instances are not planned at a lower Assurance Level than lower-criticality instances without rationale.
4. Gates CG-01 to CG-15 are each planned for evaluation or recorded as APPROVED_NA with boundary rationale for each instance.
5. Deviations from the plan in the period are recorded and approved.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Assurance planning period | months | 12 | Programme parameter; illustrative |

**Minimum evidence**

- Approved assurance plan
- Criticality classification extract
- Planned change schedule used for planning
- Plan deviation records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Current planning period |
| independence | Approval by the oversight committee, separate from the programme lead who prepared the plan |
| mandatoryItems | Approved assurance plan; Criticality classification extract |
| acceptableAlternatives | Engagement-level plan for a single assessment, approved by the decision authority |
| unknownEffect | US3 Material: decision capped at CONDITIONALLY_ASSURED; condition requires an approved plan before reliance is extended |
| reassessmentTriggers | New Capability Instance; Change in criticality classification; Major change programme approved; Gate FAIL requiring unplanned assessment |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION

**Assessment procedure**

1. Obtain the approved plan and approval record.
2. Reconcile plan coverage to the capability register and criticality classification.
3. Analyse planned depth against criticality and planned change; identify inversions.
4. Confirm each gate is planned or recorded as APPROVED_NA with rationale.
5. Review plan deviations and their approvals.

**Gate mappings.** None

**Applicability.** Applies to continuing programmes. For a one-off assessment the engagement plan satisfies the control.

**Lifecycle stages.** PLAN, OPERATE, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** Low-consequence systems assessed deeply while critical ones are not; Gates omitted from plan without rationale; Planned change not reflected in assurance schedule; Plan never approved

**Testing safety.** Desk review of planning records only; draft plans for future periods are treated as confidential programme information.

**UNKNOWN rule.** If criticality classification is unavailable, record a U1 UNKNOWN against this control and the depth-justification criterion is not met.

**Ontology classes.** AssuranceProgram, Assessment, CriticalGate, CapabilityInstance · **Related controls.** MCF-GOV-014, MCF-CAP-009, MCF-EVA-010, MCF-GOV-015

**Informative references.** ISO 19011 (guidelines for auditing management systems); ISAE 3000 (assurance engagements other than audits or reviews of historical financial information); AIDCF-011 Assurance Program Framework

### MCF-GOV-014

**Risk Appetite Linkage** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure that the organisation's stated risk appetite is translated into measurable limits for the AI capability (for example tolerated outcome interruption, tolerated loss of training progress, tolerated degraded-state duration) that drive impact tolerances, risk acceptance and decision conditions.

**Requirement.** The governing body shall approve a risk appetite statement covering service continuity, safety, data integrity and dependency concentration for the AI capability. The accountable executive shall translate it into measurable appetite limits per Service Outcome class and shall demonstrate that impact tolerances (MCF-CAP-010), risk-acceptance authority (MCF-GOV-007) and decision condition rules reference those limits.

**Assessment criteria**

1. A risk appetite statement covering service continuity, safety, data integrity and concentration is approved by the governing body.
2. Appetite is expressed as measurable limits per Service Outcome class, with units.
3. Each impact tolerance in the capability profile is at or within the corresponding appetite limit, or the exceedance is approved by the governing body.
4. Risk-acceptance authority levels reference appetite limits.
5. Zero appetite for life-safety risk is stated and is not subject to risk acceptance below the governing body.

**Minimum evidence**

- Approved risk appetite statement
- Appetite limits schedule per Service Outcome class
- Reconciliation of impact tolerances to appetite limits
- Risk-acceptance authority schedule

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1 |
| optionalClasses | E6; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Appetite statement and tolerances in force at the assessment date |
| independence | Reconciliation performed by the assessor |
| mandatoryItems | Approved risk appetite statement; Reconciliation of impact tolerances to appetite limits |
| acceptableAlternatives | Enterprise risk appetite with capability-specific annex |
| unknownEffect | US3 Material: impact tolerances cannot be confirmed as governed; decision condition recorded |
| reassessmentTriggers | Revision of risk appetite; Change of impact tolerance; New Service Outcome class |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Obtain the approved risk appetite statement and confirm coverage of the four topics.
2. Confirm measurable limits with units per Service Outcome class.
3. Reconcile each impact tolerance to the appetite limit and identify unapproved exceedances.
4. Confirm risk-acceptance authority levels reference appetite limits and that life-safety risk is excluded from delegated acceptance.
5. Interview the accountable executive on how appetite is used in decision conditions.

**Gate mappings.** None

**Applicability.** Applies to every organisation that owns an in-scope Capability Instance. Providers are not required to share their own appetite.

**Lifecycle stages.** PLAN, DESIGN · **Operating states.** NORMAL

**Failure modes addressed.** Impact tolerances set without reference to governed appetite; Appetite expressed only qualitatively; Life-safety risk accepted operationally; Concentration risk absent from appetite

**Testing safety.** Desk review only. Risk appetite statements are board-confidential and are viewed in a read-only data room where the organisation requires it.

**UNKNOWN rule.** If appetite is stated only qualitatively, the measurable-limit criterion is not met (PARTIAL), not UNKNOWN; UNKNOWN is recorded only if the approved statement itself cannot be produced.

**Ontology classes.** ServiceOutcome, CapabilityInstance, AssuranceDecision · **Related controls.** MCF-GOV-007, MCF-CAP-010, MCF-CAP-011

**Informative references.** ISO 31000 (risk management guidelines); COSO Enterprise Risk Management framework; ISO 22301 (business continuity management systems)

### MCF-GOV-015

**Critical Gate Governance** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that critical gates are evaluated, disposed and reported under governance that prevents them from being averaged away, re-scoped or overridden, and that every FAIL or UNKNOWN Gate Result reaches the decision authority with its controlling effect.

**Requirement.** The decision authority shall maintain a gate register for each in-scope Capability Instance recording, for every gate CG-01 to CG-15, applicability, CRITICAL control results, evidence sufficiency against the gate floor, Gate Result, controlling effect on the decision and closure criteria. The assurance programme lead shall ensure that Gate Results are computed by the roll-up rule of AIDCF-010, that no Gate Result is changed except by reassessment, and that APPROVED_NA is granted only by the decision authority with a boundary rationale.

**Assessment criteria**

1. A gate register exists for each in-scope Capability Instance covering all fifteen gates.
2. In a sample of assessments, each recorded Gate Result reproduces when the AIDCF-010 roll-up rule is reapplied to the recorded CRITICAL control results and gate evidence.
3. Every APPROVED_NA was granted by the decision authority with a boundary rationale.
4. No Gate Result in the register history was changed without a corresponding reassessment record.
5. Every FAIL or UNKNOWN Gate Result appears with its controlling effect in the decision record and on the first page of the executive report.
6. No decision in the sample was issued at a state above the ceiling implied by its Gate Results.

**Minimum evidence**

- Gate register with history
- Assessment records with CRITICAL control results and gate evidence
- APPROVED_NA approvals
- Decision records and executive reports for sampled assessments

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3; E7 |
| optionalClasses | E5 |
| qualityFloor | P4 F4 C4 R4 T3 I4 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | All Assurance Decisions issued in the twelve months preceding the assessment |
| independence | Roll-up reperformance by the assessor or independent reviewer, separate from the team that produced the Gate Results |
| mandatoryItems | Gate register with history; Decision records and executive reports for sampled assessments |
| acceptableAlternatives | Machine-readable gate results exported from the assessment tool with full audit history |
| unknownEffect | US3 Material: decisions in the period may not be relied on above CONDITIONALLY_ASSURED until gate governance is evidenced |
| reassessmentTriggers | Change to AIDCF-010 roll-up rule or gate criteria; Gate Result altered outside reassessment; Decision issued above gate ceiling |

**Assessment methods.** REPERFORMANCE, SAMPLING, RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Obtain the gate register and confirm all fifteen gates are recorded per Capability Instance.
2. Select assessments and reapply the AIDCF-010 roll-up rule to the recorded CRITICAL control results and evidence sufficiency.
3. Compare reperformed Gate Results with recorded results and investigate differences.
4. Review APPROVED_NA approvals and register history for changes without reassessment.
5. Trace FAIL and UNKNOWN Gate Results to decision records and executive reports; test decision state against the gate ceiling.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to every programme issuing Assurance Decisions.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** Gate FAIL offset by a high domain score; Gate marked APPROVED_NA to avoid failure; Gate Result edited after review; Critical UNKNOWN omitted from executive report

**Testing safety.** Reperformance uses exported records; no change is made to the system of record.

**UNKNOWN rule.** If the CRITICAL control results underlying a Gate Result cannot be retrieved, record a U1 UNKNOWN against that Gate Result and treat the reperformance criterion as not met for that assessment.

**Ontology classes.** CriticalGate, GateResult, AssuranceDecision, AssuranceReport · **Related controls.** MCF-EVA-017, MCF-EVA-018, MCF-GOV-003, MCF-EVA-019

**Informative references.** ISO/IEC/IEEE 15026-2 (assurance case); AIDCF-010 Scoring and Decision Framework; AIDCF-012 Reporting and Assurance Statement Standard

### MCF-GOV-016

**Independent Review** · DETECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure that a competent reviewer independent of the assessment team challenges method, evidence, gates, UNKNOWN treatment and decision wording before material conclusions are relied upon, and that the review demonstrably detects errors.

**Requirement.** The assurance programme lead shall ensure that every Assurance Decision supporting a material decision question is subject, before issue, to independent review by a reviewer who did not prepare or perform the assessment, has no conflict under MCF-GOV-021 and holds the competence defined in MCF-GOV-023. The independent reviewer shall record challenges, responses and dispositions, and shall have authority to withhold their concurrence. The programme lead shall periodically test review effectiveness by reperformance or by seeded-defect review.

**Assessment criteria**

1. Every material Assurance Decision in the period has an independent review record dated before issue.
2. Each reviewer is independent of preparation and performance, conflict-free and competent for the domains reviewed.
3. Review records show challenge to method, evidence sufficiency, Gate Results, UNKNOWN treatment and decision wording, with dispositions.
4. No decision was issued over a withheld concurrence without escalation to the governing body or oversight committee.
5. Review effectiveness was tested in the period (reperformance of a completed review or seeded-defect exercise), and the test detected at least the defects the review was expected to detect, or the shortfall was addressed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Review effectiveness test frequency | tests per year | 1 | Programme parameter; illustrative |

**Minimum evidence**

- Independent review records for each material decision
- Reviewer independence and competence declarations
- Withheld-concurrence escalation records
- Review effectiveness test record with seeded defects and detection outcome

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E3; E4 |
| optionalClasses | E5; E6 |
| qualityFloor | P4 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | All material decisions in the last twelve months and at least one effectiveness test |
| independence | Effectiveness test designed and scored by a party other than the reviewers tested |
| mandatoryItems | Independent review records for each material decision; Review effectiveness test record with seeded defects and detection outcome |
| acceptableAlternatives | External quality assessment of the review function by a second-party or independent provider, if it includes reperformance |
| unknownEffect | US3 Material: decisions are treated as self-reviewed; decision capped at CONDITIONALLY_ASSURED for intended users beyond management |
| reassessmentTriggers | Change of reviewer pool; Decision issued without review; Missed defect discovered after issue; New domain requiring reviewer competence |

**Assessment methods.** DOCUMENT_REVIEW, REPERFORMANCE, TEST, INQUIRY

**Assessment procedure**

1. List material decisions in the period and match each to a review record dated before issue.
2. Verify reviewer independence and competence declarations against engagement records and the competence register.
3. Examine review records for challenge across the five topics and for dispositions.
4. Check for decisions issued over withheld concurrence and their escalation.
5. Examine the review effectiveness test design, seeded defects and detection results; where no test exists, reperform one completed review and compare findings.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to Assurance Decisions relied on for material decision questions or by intended users beyond the management team. Internal-only diagnostic assessments at AL0-AL1 are excluded.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Reviewer from the same team as the assessor; Review performed after issue; Review signs off without challenge; Reviewer lacks competence in the domain where the decisive gate sits

**Testing safety.** Seeded-defect tests use copies of closed engagements with synthetic defects clearly labelled; they are never introduced into live engagements or live reports.

**UNKNOWN rule.** If a review record exists but its date relative to issue cannot be established, record a U7 UNKNOWN and treat the decision as not independently reviewed for this control.

**Ontology classes.** ReviewRecord, AssuranceDecision, DecisionRecommendation · **Related controls.** MCF-GOV-021, MCF-GOV-022, MCF-GOV-023, MCF-EVA-019

**Informative references.** ISO 19011 (guidelines for auditing management systems); ISAE 3000 (assurance engagements other than audits or reviews of historical financial information); Institute of Internal Auditors Global Internal Audit Standards (quality assurance and improvement)

## GOV-05 Stakeholder and regulatory interface

### MCF-GOV-017

**Stakeholder Obligations** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure that obligations owed to stakeholders (customers, tenants, regulators, grid and water authorities, insurers, lenders, community) that constrain the AI capability are identified and translated into Service Outcomes, tolerances or constraints.

**Requirement.** The capability owner shall maintain a stakeholder obligation register identifying each obligation that constrains an in-scope Capability Instance (for example contracted availability, data residency, grid connection conditions, water abstraction limits, noise and emission permits, insurance warranties), its source document, owner and the Service Outcome, tolerance or operating constraint into which it is translated.

**Assessment criteria**

1. A stakeholder obligation register exists covering customers, tenants, regulators, utilities, insurers and financiers relevant to the instance.
2. Each obligation identifies its source document, owner and the Service Outcome, tolerance or constraint into which it is translated.
3. Grid connection and utility conditions that constrain load ramp rates, curtailment or on-site generation are captured.
4. A sample of source contracts and permits contains no constraining obligation absent from the register.
5. Obligations with conflicting requirements are identified and resolved by the capability owner.

**Minimum evidence**

- Stakeholder obligation register
- Sampled source contracts, permits and connection agreements
- Traceability from obligations to Service Outcomes and constraints

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1 |
| optionalClasses | E6; E7 |
| qualityFloor | P3 F4 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Obligations in force at the assessment date |
| independence | Sample of source documents selected by the assessor |
| mandatoryItems | Stakeholder obligation register; Traceability from obligations to Service Outcomes and constraints |
| acceptableAlternatives | Contract management system extract with obligation tagging |
| unknownEffect | US3 Material: affected Service Outcome definitions qualified; decision condition recorded |
| reassessmentTriggers | New or amended customer contract; New grid connection or permit condition; Insurance renewal with new warranties |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, RECONCILIATION

**Assessment procedure**

1. Obtain the register and confirm stakeholder classes covered.
2. Sample source documents and identify constraining obligations absent from the register.
3. Trace each sampled obligation to a Service Outcome, tolerance or constraint.
4. Confirm grid and utility constraints on ramp rate, curtailment and generation are captured.
5. Review conflict identification and resolution.

**Gate mappings.** CG-01 Capability and outcome definition (SUPPORTING)

**Applicability.** Applies to every in-scope Capability Instance.

**Lifecycle stages.** PLAN, DESIGN, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Grid connection ramp-rate limit unknown to operators of synchronous training workloads; Data residency obligation not reflected in recovery site selection; Insurance warranty breached by unrecorded configuration; Contracted availability exceeds designed capability

**Testing safety.** Document review only; contract access governed by the evidence lead's restriction record.

**UNKNOWN rule.** If a source contract or permit cannot be accessed, record a U2 UNKNOWN against the obligations it would contain.

**Ontology classes.** ServiceOutcome, CapabilityInstance, Dependency · **Related controls.** MCF-GOV-019, MCF-GOV-018, MCF-CAP-005, MCF-CAP-011

**Informative references.** ISO 37301 (compliance management systems); ISO 22301 (business continuity management systems)

### MCF-GOV-018

**Regulatory Monitoring** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that changes in law, regulation, permits and mandatory standards affecting the AI capability (energy, water, emissions, safety, data and critical-infrastructure regimes) are detected, assessed for impact and actioned in time.

**Requirement.** The compliance owner shall operate a regulatory monitoring process covering each jurisdiction in which in-scope infrastructure is located, record each relevant change with an impact assessment against Service Outcomes, controls and obligations, assign actions, and report material changes to the oversight committee. Changes affecting life safety, hazardous energy or reporting duties shall be escalated within the regulatory escalation time.

**Assessment criteria**

1. Monitoring covers each jurisdiction and regulatory topic relevant to in-scope infrastructure.
2. Each relevant change in the period has an impact assessment and assigned actions.
3. Material changes were reported to the oversight committee.
4. Changes affecting life safety, hazardous energy or reporting duties were escalated within the escalation time.
5. Actions arising from regulatory changes are tracked to closure or have approved exceptions.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Regulatory escalation time for safety or reporting-duty changes | working days | 10 | Programme parameter; illustrative |

**Minimum evidence**

- Regulatory monitoring scope by jurisdiction and topic
- Change log with impact assessments for the period
- Oversight committee reports
- Action tracking records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I2 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Twelve months preceding the assessment |
| independence | Assessor or legal specialist checks a sample of known changes against the log |
| mandatoryItems | Regulatory monitoring scope by jurisdiction and topic; Change log with impact assessments for the period |
| acceptableAlternatives | Subscription legal-update service records combined with internal impact assessments |
| unknownEffect | US3 Material: obligation completeness qualified; decision condition recorded |
| reassessmentTriggers | Entry into a new jurisdiction; Major regulatory change affecting energy, water or critical infrastructure; Regulatory enforcement event |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, INQUIRY

**Assessment procedure**

1. Confirm monitoring scope by jurisdiction and topic.
2. Sample changes from the log and test impact assessments and actions.
3. Check escalation timing for safety and reporting-duty changes.
4. Confirm committee reporting of material changes.
5. Interview the compliance owner on sources and coverage limits.

**Gate mappings.** CG-14 Change control (SUPPORTING)

**Applicability.** Applies to every organisation that owns or operates in-scope infrastructure. AIDCF does not determine legal compliance; this control assesses the monitoring process only.

**Lifecycle stages.** PLAN, OPERATE, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** New energy-reporting duty missed; Permit condition change not reflected in operating envelope; Safety regulation change not escalated; Jurisdiction omitted from monitoring

**Testing safety.** Desk review of the change log and impact assessments; no legal opinion is given or implied by the assessor.

**UNKNOWN rule.** If the monitoring scope cannot be confirmed for a jurisdiction, record a U5 coverage-gap UNKNOWN for that jurisdiction.

**Ontology classes.** Event, Action, ReassessmentTrigger · **Related controls.** MCF-GOV-017, MCF-GOV-020, MCF-EVA-022

**Informative references.** ISO 37301 (compliance management systems); ISO 31000 (risk management guidelines)

### MCF-GOV-019

**Customer Commitments** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that what is promised to customers and tenants (SLAs, SLOs, credits, capacity reservations, recovery commitments) reconciles to the approved Service Outcomes and to the capability actually provided, so that commitments do not exceed assured capability.

**Requirement.** The commercial owner shall ensure that each customer or tenant commitment concerning availability, performance, integrity, capacity or recovery of an in-scope Capability Instance is recorded with its metric definition, measurement method and exclusions, and is reconciled by the capability owner to the approved Service Outcomes and tolerances before signature and after every change to either. Commitments exceeding approved Service Outcomes shall be approved by the accountable executive with a recorded risk acceptance.

**Assessment criteria**

1. Each in-scope customer or tenant commitment is recorded with metric definition, measurement method and exclusions.
2. Each commitment is reconciled to an approved Service Outcome with the same metric definition and measurement window.
3. No commitment exceeds the approved Service Outcome tolerance without accountable-executive approval and risk acceptance.
4. Reconciliation was performed before signature for commitments made in the period.
5. Measurement of committed metrics uses the same data sources as Service Outcome measurement.

**Minimum evidence**

- Commitment register with metric definitions
- Reconciliation records to Service Outcomes
- Approvals and risk acceptances for exceedances
- Sampled contracts or service descriptions

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E7 |
| optionalClasses | E3 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Commitments in force at the assessment date |
| independence | Assessor selects contracts and reperforms reconciliation |
| mandatoryItems | Commitment register with metric definitions; Reconciliation records to Service Outcomes |
| acceptableAlternatives | Standard product terms plus a register of negotiated deviations |
| unknownEffect | US3 Material: decision condition recorded; Service Outcome adequacy for customer reliance qualified |
| reassessmentTriggers | New customer contract or renewal; Change in Service Outcome tolerance; SLA breach |

**Assessment methods.** RECONCILIATION, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Obtain the commitment register and confirm completeness against the contract system.
2. Sample contracts and reperform reconciliation of metric definitions, windows and exclusions to Service Outcomes.
3. Identify exceedances and verify approvals and risk acceptances.
4. Confirm reconciliation dates precede signature.
5. Compare data sources for commitment reporting with those for Service Outcome measurement.

**Gate mappings.** CG-01 Capability and outcome definition (SUPPORTING)

**Applicability.** Applies where in-scope capability is provided to external customers or internal tenants under defined commitments. Not applicable to purely internal research capability without commitments, with rationale.

**Lifecycle stages.** PLAN, OPERATE, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** SLA promises accelerator availability beyond designed redundancy; SLA measured with different exclusions from Service Outcome; Recovery commitment shorter than tested recovery time; Capacity reservation exceeds power or cooling envelope

**Testing safety.** Document review only; commercial terms are disclosed only to the extent needed and under restriction.

**UNKNOWN rule.** If a contract cannot be accessed, record a U2 UNKNOWN for that commitment; it shall not be assumed to match the Service Outcome.

**Ontology classes.** ServiceOutcome, CapabilityInstance, CapacityAssertion · **Related controls.** MCF-GOV-017, MCF-CAP-005, MCF-CAP-006, MCF-CAP-008

**Informative references.** ISO/IEC 20000-1 (service management system); ISO/IEC 19086 series (cloud computing service level agreement framework)

### MCF-GOV-020

**External Reporting** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that assurance conclusions communicated externally (customer statements, regulatory submissions, investor or public disclosures) are no stronger than the approved Assurance Decision, carry its limitations, and are approved before release.

**Requirement.** The decision authority shall approve every external communication that conveys an AIDCF assurance conclusion before release. The communications owner shall ensure that each such communication uses the controlled decision language of AIDCF-012, identifies the Capability Instance, scope, period and limitations, includes every gate FAIL and US4/US5 UNKNOWN relevant to the audience, contains no prohibited claim (certification, accreditation, universal safety or resilience), and is withdrawn or corrected when the underlying decision is suspended, withdrawn or superseded.

**Assessment criteria**

1. Every external communication in the period conveying an AIDCF conclusion was approved by the decision authority before release.
2. Each communication uses controlled decision language and states Capability Instance, scope, period and limitations.
3. No communication contains a prohibited claim.
4. No communication omits a gate FAIL or US4/US5 UNKNOWN material to its audience.
5. Communications based on decisions later suspended, withdrawn or superseded were corrected or withdrawn within the correction time.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| External correction time after decision suspension | working days | 10 | Programme parameter; illustrative |

**Minimum evidence**

- Register of external communications conveying conclusions
- Approval records
- Copies of the communications
- Correction and withdrawal records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E7 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Twelve months preceding the assessment |
| independence | Assessor compares each communication with the underlying decision record |
| mandatoryItems | Register of external communications conveying conclusions; Copies of the communications; Approval records |
| acceptableAlternatives | Communications archive search by assessor where no register exists, with a coverage limitation recorded |
| unknownEffect | US3 Material: decision condition recorded; continued external reliance is qualified |
| reassessmentTriggers | Decision suspended, withdrawn or superseded; New external audience; Change in AIDCF-012 controlled language |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, SAMPLING

**Assessment procedure**

1. Obtain the communications register and test completeness by searching published and submitted material.
2. Compare each communication with the underlying decision record for state, scope, period and limitations.
3. Screen for prohibited claims.
4. Check inclusion of material gate FAIL and US4/US5 UNKNOWN items.
5. Trace suspended or superseded decisions to correction or withdrawal of communications.

**Gate mappings.** None

**Applicability.** Applies whenever an AIDCF conclusion is communicated outside the organisation issuing it.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Marketing states the facility is 'AIDCF certified'; Customer statement omits a critical UNKNOWN; Communication remains published after decision suspension; Scope broadened in the summary beyond the assessed boundary

**Testing safety.** Desk review of published and submitted material only; the assessor does not contact external recipients of the communications.

**UNKNOWN rule.** If the completeness of the communications register cannot be tested, record a U5 coverage-gap UNKNOWN and limit the conclusion to communications identified.

**Ontology classes.** AssuranceStatement, AssuranceReport, DistributionControl, AssuranceDecision · **Related controls.** MCF-EVA-020, MCF-EVA-016, MCF-EVA-024, MCF-GOV-018

**Informative references.** AIDCF-012 Reporting and Assurance Statement Standard; ISAE 3000 (assurance engagements other than audits or reviews of historical financial information); ISO/IEC 17000 (conformity assessment vocabulary and general principles)

## GOV-06 Ethics, impartiality and competence

### MCF-GOV-021

**Conflict Management** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that conflicts of interest affecting assessors, reviewers, specialists and decision authorities (financial, self-review, familiarity, advocacy, intimidation) are declared, evaluated and safeguarded before work begins and throughout the engagement.

**Requirement.** The assurance programme lead shall require every assessor, reviewer, specialist and decision authority to declare interests before assignment and on any change, shall evaluate each declared or identified threat (self-review, self-interest, familiarity, advocacy, intimidation), and shall apply and record a safeguard or exclusion. The programme lead shall prohibit outcome-contingent fees for assurance conclusions and shall exclude from assessment any person who designed, built, operates or advised on the control under assessment within the cooling-off period.

**Assessment criteria**

1. Every person assigned to engagements in the period has a declaration dated before assignment.
2. Each declared or identified threat has a recorded evaluation and safeguard or exclusion.
3. No assessor assessed a control they designed, built, operated or advised on within the cooling-off period.
4. No engagement in the period used an outcome-contingent fee.
5. Changes in interests during engagements were declared and re-evaluated.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Self-review cooling-off period | months | 12 | Programme parameter; illustrative |

**Minimum evidence**

- Declarations of interest for engagement personnel
- Threat evaluations and safeguard records
- Engagement assignment records
- Fee arrangements for provider engagements

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Engagements active in the twelve months preceding the assessment |
| independence | Assessor cross-checks declarations against design, change and advisory records independently of the declarant |
| mandatoryItems | Declarations of interest for engagement personnel; Threat evaluations and safeguard records; Engagement assignment records |
| acceptableAlternatives | Provider's own conflict register, if the provider grants access to records for the engagement personnel |
| unknownEffect | US3 Material: affected results treated as not independently assessed; decision capped at CONDITIONALLY_ASSURED for external reliance |
| reassessmentTriggers | New provider engaged; Assessor previously involved in design or operation; Fee structure change; Undeclared conflict discovered |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, SAMPLING, INQUIRY

**Assessment procedure**

1. List engagement personnel and match each to a dated declaration.
2. Review threat evaluations and safeguards.
3. Cross-check assessors against design, change, operation and advisory records for the controls they assessed.
4. Inspect fee arrangements for outcome contingency.
5. Interview a sample of assessors on declaration practice.

**Gate mappings.** None

**Applicability.** Applies to all engagements producing Control Assessments, Gate Results or Assurance Decisions.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Assessor reviews a design they produced; Provider paid more for a favourable conclusion; Familiarity threat from long-standing operator relationship unaddressed; Decision authority holds a commercial interest in the outcome

**Testing safety.** Document review and interview only; personal declarations are handled as restricted personal data.

**UNKNOWN rule.** If a declaration is missing for a person who assessed a control, record a U1 UNKNOWN and treat that person's results as not independently assessed until a retrospective declaration is evaluated.

**Ontology classes.** Assessment, ReviewRecord, AssuranceProgram · **Related controls.** MCF-GOV-022, MCF-GOV-016, MCF-GOV-023

**Informative references.** ISO/IEC 17020 (requirements for bodies performing inspection) - impartiality; ISO/IEC 17021-1 (requirements for bodies providing audit and certification) - impartiality; ISO 19011 (guidelines for auditing management systems)

### MCF-GOV-022

**Assessor Independence** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that the organisational and reporting independence of the assessment function matches the reliance placed on its conclusions, so that preparation, performance, review and decision remain separable.

**Requirement.** The governing body shall define the independence level required for each class of intended reliance (management use, customer reliance, regulatory or financing reliance). The assurance programme lead shall ensure that for each engagement the assessment team's reporting line, provider model and separation of preparation, performance, review and decision meet the required level, and that the actual independence level is stated in the Assurance Statement.

**Assessment criteria**

1. Required independence levels are defined per reliance class.
2. For each engagement, the provider model and reporting line meet the required level for the stated intended users.
3. Preparation, performance, independent review and decision are assigned to separate persons or roles as required by the level.
4. The Assurance Statement states the actual independence level and provider model.
5. Assessors did not operate controls or accept risks for management during the engagement.

**Minimum evidence**

- Independence policy with levels per reliance class
- Engagement records with team composition, provider model and reporting line
- Assurance Statements for the period

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Engagements completed in the twelve months preceding the assessment |
| independence | Assessment of this control shall not be performed by the assessment function it concerns |
| mandatoryItems | Independence policy with levels per reliance class; Engagement records with team composition, provider model and reporting line |
| acceptableAlternatives | Engagement letters stating provider model and intended users |
| unknownEffect | US3 Material: intended use of affected decisions restricted to management; condition recorded |
| reassessmentTriggers | Change of provider model; Change of assessment function reporting line; New intended-user class |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Obtain the independence policy and levels.
2. For each engagement, compare provider model, reporting line and role separation with the required level.
3. Compare stated independence level in Assurance Statements with engagement records.
4. Interview management and assessors on any operation of controls or risk acceptance by assessors.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to all engagements; the required level may be management-only for AL0-AL1 diagnostic work.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Internal team reporting to the operations head issues customer-facing assurance; One person prepares, reviews and decides; Statement overstates independence; Assessor runs a failover test as operator

**Testing safety.** Document review and interview only.

**UNKNOWN rule.** If the reporting line of an assessment team cannot be established, record a U6 UNKNOWN and restrict intended use to management.

**Ontology classes.** Assessment, AssuranceStatement, AssuranceProgram · **Related controls.** MCF-GOV-021, MCF-GOV-016, MCF-EVA-019

**Informative references.** ISO/IEC 17020 (requirements for bodies performing inspection); Institute of Internal Auditors Three Lines Model; ISAE 3000 (assurance engagements other than audits or reviews of historical financial information)

### MCF-GOV-023

**Competence Management** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that assessors, specialists and reviewers are competent for the domains, technologies and test methods they apply (for example high-density liquid cooling, accelerator fabrics, protection studies, OT security), and that competence is current.

**Requirement.** The assurance programme lead shall maintain a competence framework for each role and domain (aligned to AIDCF-011 Part IX), a register recording each person's evidenced competence and its currency, and an assignment check confirming that every engagement assignment matches recorded competence. Where competence is not available internally, the lead shall engage a specialist under recorded reliance with scope and responsibility.

**Assessment criteria**

1. A competence framework defines required knowledge, experience and evidence per role and domain.
2. A register records each person's competence with evidence and currency date.
3. Every assignment in the period matches recorded, current competence for the domain and method.
4. Specialist reliance is recorded with scope, competence evidence and responsibility.
5. Competence gaps identified in the period have development actions or were filled by specialists.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Competence currency period | months | 24 | Programme parameter; illustrative, shorter for rapidly changing technologies |

**Minimum evidence**

- Competence framework
- Competence register with evidence
- Engagement assignment records
- Specialist reliance records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3; E6 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C4 R3 T3 I2 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Assignments in the twelve months preceding the assessment |
| independence | Assessor verifies a sample of competence evidence at source (certificates, prior work records) |
| mandatoryItems | Competence framework; Competence register with evidence; Engagement assignment records |
| acceptableAlternatives | Provider-held competence records made available for engagement personnel |
| unknownEffect | US3 Material: affected domain results carry a confidence ceiling of CONF-2 and a decision condition |
| reassessmentTriggers | New technology in scope; New assessor or provider; Finding attributed to competence gap |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Review the framework against AIDCF-011 competence expectations and the technologies in scope.
2. Sample register entries and verify evidence at source.
3. Reconcile assignments to recorded competence and currency.
4. Review specialist reliance records.
5. Interview a sample of assessors on their domain experience.

**Gate mappings.** None

**Applicability.** Applies to all engagement roles. AIDCF does not accredit people; this control assesses the programme's own competence management.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Mechanical assessor without liquid-cooling experience assesses CDU failover; Lapsed competence for protection-study review; Specialist used without recorded scope; Reviewer unfamiliar with accelerator fabric failure modes

**Testing safety.** Document review and interview only; personal data handled under minimisation.

**UNKNOWN rule.** If competence evidence for an assigned person cannot be verified, record a U6 UNKNOWN and apply a CONF-2 ceiling to results that person produced.

**Ontology classes.** Assessment, ReviewRecord, AssuranceProgram · **Related controls.** MCF-GOV-016, MCF-EVA-012, MCF-GOV-022

**Informative references.** ISO/IEC 17024 (requirements for bodies operating certification of persons); ISO 19011 (guidelines for auditing management systems) - competence of auditors; AIDCF-011 Assurance Program Framework

### MCF-GOV-024

**Appeal and Challenge** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that capability owners, operators and affected stakeholders can challenge a Finding, Gate Result or Assurance Decision through a defined, impartial process with recorded outcomes, without suppressing the original record.

**Requirement.** The decision authority shall maintain an appeal and challenge procedure that defines who may challenge, grounds, time limits, the impartial reviewer, evidence required, and possible outcomes. The decision authority shall ensure that every challenge is logged, decided by a person not involved in the challenged result, and that the original result, the challenge and the outcome are all preserved, with any change made only by reassessment.

**Assessment criteria**

1. A procedure defines eligible challengers, grounds, time limits, reviewer, evidence and outcomes.
2. Every challenge in the period is logged and was decided by a person not involved in the challenged result.
3. Original results, challenges and outcomes are preserved; no original record was deleted or overwritten.
4. Changed results arising from challenges were produced by reassessment with new or re-evaluated evidence.
5. Challenges were decided within the procedure time limits or the delay was recorded.

**Minimum evidence**

- Appeal and challenge procedure
- Challenge log for the period
- Sampled challenge files with decisions
- Record history for challenged results

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F3 C4 R3 T3 I4 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Challenges raised in the twelve months preceding the assessment |
| independence | Record history extracted by the assessor from the system of record |
| mandatoryItems | Appeal and challenge procedure; Challenge log for the period; Record history for challenged results |
| acceptableAlternatives | Where no challenges occurred, a walkthrough of the procedure with the decision authority, recorded as limited operating evidence |
| unknownEffect | US2 Moderate: confidence in contested results limited to CONF-2 |
| reassessmentTriggers | Challenge upheld; Change of decision authority; Repeated challenges on the same gate |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, INSPECTION

**Assessment procedure**

1. Review the procedure.
2. Sample challenges and verify reviewer non-involvement and timeliness.
3. Inspect record history for preservation of original results.
4. Trace changed results to reassessment records.

**Gate mappings.** None

**Applicability.** Applies to every programme issuing Findings, Gate Results or Assurance Decisions.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Finding deleted after management objection; Challenge decided by the original assessor; Result changed without new evidence; No route for operators to contest a Finding

**Testing safety.** Document and record inspection only.

**UNKNOWN rule.** If record history cannot demonstrate preservation of originals, record a U7 UNKNOWN against challenged results.

**Ontology classes.** Finding, GateResult, AssuranceDecision, ReviewRecord · **Related controls.** MCF-GOV-016, MCF-EVA-015, MCF-EVA-013

**Informative references.** ISO/IEC 17020 (requirements for bodies performing inspection) - complaints and appeals; ISO/IEC 17021-1 (requirements for bodies providing audit and certification) - appeals
