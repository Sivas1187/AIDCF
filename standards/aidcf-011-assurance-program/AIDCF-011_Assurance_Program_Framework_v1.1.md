> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-011_Assurance_Program_Framework_v1.1.pdf](AIDCF-011_Assurance_Program_Framework_v1.1.pdf).

**AIDCF**

**AI Data Centre Facilities Assurance Framework**

**ASSURANCE PROGRAM FRAMEWORK**

**Version 1.1**

A non-certification programme standard for commissioning, governing, delivering, reviewing, sustaining and improving AIDCF assurance

Artifact ID: AIDCF-011  
Status: Draft for controlled review  
Author: Siva Sethumadhavan

**AIDCF defines the method. Users and assurance providers apply it. Accountable organisations own risks and decisions. This framework issues no certificate.**

# Document control

| **Field**         | **Value**                                                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------------------------------------|
| Title             | AIDCF-011 Assurance Program Framework                                                                                      |
| Artifact ID       | AIDCF-011 (requirement short code APF)                                                                                     |
| Version           | 1.1                                                                                                                        |
| Date              | 2026-10-10                                                                                                                 |
| Status            | Draft for controlled review                                                                                                |
| Author            | Siva Sethumadhavan                                                                                                         |
| Depends on        | AIDCF-006, AIDCF-007A, AIDCF-008, AIDCF-009 (Part A and Part B), AIDCF-010, AIDCF-012, AIDCF-014                           |
| Purpose           | Define repeatable AIDCF assurance programmes without establishing AIDCF as a certification or accreditation body.          |
| Users             | Organisations, customers, assurance providers, internal audit, investors and regulators using AIDCF for bounded decisions. |
| Inputs            | Controls, evidence, workpapers, Gate Results, scores, Findings, scenarios and decisions.                                   |
| Outputs           | Charter, plan, assessment package, bounded statement (AIDCF-012), action plan, reassessment, continuing-assurance and management-review records. |
| Non-certification | No AIDCF certificate, certification mark, accredited status or universal claim is created.                                 |
| Safety            | No programme authorises hazardous testing or replaces licensed professional judgment.                                      |

## Revision history

| **Version** | **Date**   | **Summary**                                                                                                                                                                                                                                                             |
|-------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | —          | Initial programme framework (published under the superseded identifier AIDCF-APF-001).                                                                                                                                                                                  |
| 1.1         | 2026-10-10 | Confirmed AL0–AL6 as the canonical Assurance Levels with claim-type mapping; removed duplicate statement templates in favour of AIDCF-012 AS-01–AS-05; made this document the single home of reviewer and release-gate tables; added the management-system loop (PDCA, programme internal audit, management review, corrective action, continual improvement) with ISO/IEC 42001 and ISO/IEC 27001 integration; consolidated boilerplate profiles and playbooks; aligned vocabularies and graph mappings; introduced APF-REQ requirement IDs with mapping annex. |

# Executive thesis

AIDCF-011 converts the AIDCF method into a usable, self-improving assurance programme while preserving the separation between framework ownership, assessment delivery, evidence review, management accountability and any separately regulated certification activity.

# 0 Introduction

## 0.1 Normative language

"Shall" and "shall not" state requirements; "should" and "should not" state recommendations; "may" states a permission; "can" states a capability (ISO/IEC Directives, Part 2 usage). Requirements carry identifiers APF-REQ-NNN.

## 0.2 Relationship to other AIDCF artifacts

| **Artifact** | **Relationship**                                                                                                              |
|--------------|-------------------------------------------------------------------------------------------------------------------------------|
| AIDCF-009    | Part A defines how each assessment in a programme is performed; Part B provides execution aids. AIDCF-011 governs the programme in which assessments run. |
| AIDCF-010    | Defines gate criteria, scoring, decision ceilings and decision-state rules applied in every programme evaluation.               |
| AIDCF-012    | Defines report classes, assurance statement templates AS-01–AS-05 and the authoritative controlled decision wording.           |
| AIDCF-008    | Defines evidence semantics, floors and confidence used by every programme.                                                    |

# Part I — Authority and boundaries

AIDCF-011 standardises programmes, not certification.

| **Element**            | **Programme rule**                                                                                                 |
|------------------------|------------------------------------------------------------------------------------------------------------------|
| Framework owner        | Maintains methodology, schemas and change control.                                                               |
| Programme sponsor      | Defines and authorises the decision need.                                                                        |
| Assessed organisation  | Owns capability, evidence access, risks and actions.                                                             |
| Assurance provider     | Performs work under its own professional and contractual authority.                                              |
| Decision authority     | Issues the bounded Assurance Decision or records that none is issued.                                            |
| Permitted wording      | "Assessed using AIDCF"; "AIDCF-aligned assessment"; "provider-issued AIDCF-aligned assurance statement".         |
| Prohibited wording     | "AIDCF Certified"; "AIDCF Accredited"; any universal safe, secure or resilient claim.                             |
| Separate certification | Any certification scheme is outside this framework and remains the responsibility of a separately governed body. |

**APF-REQ-001** No programme, provider or assessed organisation shall describe an AIDCF programme output as a certificate, accreditation, certification mark or endorsement by the framework owner.

# Part II — Programme principles

Programmes retain the AIDCF constitutional invariants (AIDCF-006).

| **Element**         | **Programme rule**                                                                                    |
|---------------------|-------------------------------------------------------------------------------------------------------|
| Capability first    | A defined Capability Instance and Service Outcomes.                                                   |
| Evidence gated      | Every material claim has evidence or an explicit UNKNOWN Record.                                      |
| UNKNOWN visible     | Missing, stale, inaccessible and conflicting evidence remains non-favourable.                         |
| Gate dominance      | Critical gates cannot be averaged away.                                                               |
| Claim distinction   | DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS and RESILIENCE claims remain distinct.               |
| Boundary visibility | External and excluded dependencies remain visible.                                                    |
| Safety              | Collection and testing are authorised and proportionate.                                              |
| Competence          | Collective technical and assurance competence.                                                        |
| Bounded conclusion  | Scope, operating states, time, evidence and limitations stated.                                       |
| Reassessment        | Material change can suspend prior reliance.                                                           |
| Improvement         | The programme itself is planned, checked and improved as a management system (Part XXI).             |

# Part III — Programme models

| **Model**               | **Programme rule**                                                                                    | **AIDCF-012 statement template** |
|-------------------------|-------------------------------------------------------------------------------------------------------|----------------------------------|
| First-party             | Organisation self-assessment for readiness and improvement.                                           | AS-01                            |
| Co-sourced              | Management and provider share work with an explicit responsibility split.                             | AS-02                            |
| Second-party            | Customer, investor or contracting party assesses a provider for a decision.                           | AS-03                            |
| Independent third-party | Provider performs the work and issues its own bounded statement.                                      | AS-04                            |
| Regulatory support      | Structures evidence and analysis; does not determine legal compliance unless separately authorised.   | AS-01–AS-04 per model, with R7 package |
| Diligence               | Bounded review for transaction, finance, capacity or outsourcing.                                     | AS-03 or AS-04                   |
| Internal audit          | May use AIDCF under its existing charter and professional standards.                                  | AS-01 (internal) or AS-04 where independence is established |
| Continuing assurance    | Claim-specific evidence refresh and event-driven reassessment, not universal continuous assurance.    | AS-05                            |

**APF-REQ-002** Every programme shall declare its model in the programme charter and shall use the AIDCF-012 statement template that corresponds to that model.

# Part IV — Assurance Levels (canonical)

Assurance Levels describe programme depth, not certification grades. AL0–AL6 are the canonical AIDCF Assurance Levels; other artifacts refer to them and do not redefine them.

| **Level** | **Name**                     | **Purpose**                                                              | **Claim types that may be concluded** | **Typical evidence profile tier (AIDCF-008)** | **Assurance Decision**                                                                                                  |
|-----------|------------------------------|--------------------------------------------------------------------------|---------------------------------------|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| AL0       | Discovery                    | Inventory of capability, controls, evidence and decision need.           | None                                  | —                                             | No Assurance Decision is issued; discovery report only.                                                                  |
| AL1       | Readiness                    | Scope, ownership, applicability and evidence readiness.                  | None (readiness Findings only)        | CP-1                                          | No Assurance Decision on Service Outcomes; readiness conclusion reported without a decision state.                      |
| AL2       | Design                       | Requirements, architecture and safeguard design.                         | DESIGN                                | CP-1, CP-2                                    | Decision states apply to design adequacy only.                                                                          |
| AL3       | Implementation               | Reconciliation to implemented or as-built state.                         | DESIGN, IMPLEMENTATION                | CP-2                                          | Decision states apply to design and implementation claims.                                                              |
| AL4       | Operational                  | Representative operation, monitoring, maintenance and incidents over a declared period. | DESIGN, IMPLEMENTATION, OPERATION | CP-3                                 | Decision states apply up to operation over the declared period.                                                         |
| AL5       | Effectiveness and resilience | Safeguard effectiveness, failure containment and recovery.               | All five claim types                  | CP-4, CP-5                                    | Decision states apply to all claims within tested and observed conditions.                                              |
| AL6       | Continuing                   | Refresh of approved claims, evidence, gates and triggers.                | The claim types previously concluded, for designated claims | As for the original level            | Continuing update (AIDCF-012 AS-05) of an existing decision; lifecycle may move to SUSPENDED, WITHDRAWN or SUPERSEDED. |

Each control in the AIDCF-007A registry has a "Required Assurance Level" (AL2–AL5) equal to the minimum level for its claim type (DESIGN AL2, IMPLEMENTATION AL3, OPERATION AL4, EFFECTIVENESS AL5, RESILIENCE AL5). Legacy registry values A2–A5 map one-to-one to AL2–AL5.

**APF-REQ-003** A programme statement shall not conclude on any claim type above those permitted for the programme's Assurance Level in Part IV.

**APF-REQ-004** Programmes and reports shall express programme depth only as AL0–AL6 as defined in Part IV.

# Part V — Assessment types

| **Type**           | **Programme rule**                                        | **Typical level** |
|--------------------|-----------------------------------------------------------|-------------------|
| Baseline           | Initial capability-wide understanding.                    | AL0–AL1           |
| Readiness          | Preparation for deployment or deeper assurance.           | AL1               |
| Design             | Pre-build or architecture decision support.               | AL2               |
| Implementation     | As-built, commissioning or handover.                      | AL3               |
| Operational        | Current operating effectiveness over a declared period.   | AL4               |
| Resilience         | Failure, degraded state, containment and recovery.        | AL5               |
| Major change       | Delta assessment after material change.                   | Level of the affected claims |
| Incident triggered | Impact on prior claims and residual state.                | Level of the affected claims |
| Periodic           | Planned reassessment of defined claims and gates.         | Level of the original decision |
| Continuing         | Evidence and trigger monitoring for approved assertions.  | AL6               |

# Part VI — Programme lifecycle

The programme lifecycle governs AIDCF-009 execution and maps onto the Plan-Do-Check-Act cycle of Part XXI.

| **Stage**             | **Programme rule**                                                  | **PDCA**   | **AIDCF-009 stage gate** |
|-----------------------|---------------------------------------------------------------------|------------|--------------------------|
| P0 Need               | Business decision, intended users and authority.                    | Plan       | SG0                      |
| P1 Charter            | Decision question, capability, outcomes and programme model.        | Plan       | SG0                      |
| P2 Scope/profile      | Boundary, level, controls, states, gates and exclusions.            | Plan       | SG1                      |
| P3 Provider           | Competence, independence, conflicts and rules of engagement.        | Plan       | SG2                      |
| P4 Plan               | Evidence, methods, samples, tests, safety and reviews.              | Plan       | SG2                      |
| P5 Execute            | AIDCF-009 fieldwork and workpapers.                                 | Do         | SG3                      |
| P6 Evaluate           | Findings, scenarios, Gate Results, UNKNOWN, scores and recommendation. | Do      | SG4                      |
| P7 Review             | Technical and independent challenge.                                | Check      | SG5                      |
| P8 Decide/report      | Accountable decision and bounded statement.                         | Do         | SG6                      |
| P9 Improve/sustain    | Actions, closure evidence, validity, monitoring, reassessment and programme improvement. | Check, Act | SG7 |

# Part VII — Governance roles

| **Role**             | **Programme rule**                                          |
|----------------------|-------------------------------------------------------------|
| Steering group       | Approves charter, scope, changes and unresolved conflicts; performs management review (Part XXI). |
| Capability owner     | Owns outcomes, risks and actions.                           |
| Programme lead       | Coordinates programme design, delivery and improvement.     |
| Lead assessor        | Directs assessment and integration.                         |
| Domain specialists   | Approve technical methods and conclusions.                  |
| Evidence lead        | Controls requirements, provenance and disclosure.           |
| Independent reviewer | Challenges method, evidence, gates and wording.             |
| Decision authority   | Issues the Assurance Decision or records that none is issued. |
| Action owners        | Deliver remediation and closure evidence.                   |
| Programme auditor    | Performs internal audit of the assurance programme (Part XXI); independent of the programme lead. |
| Tool owner           | Implements workflows without hidden authority.              |

# Part VIII — Independence

| **Programme model / situation** | **Programme rule**                                               |
|---------------------------------|------------------------------------------------------------------|
| Self-assessment                 | Management review plus independent challenge for material gates. |
| Co-sourced                      | Separate preparation, testing, evaluation and review.            |
| Second-party                    | Disclose commissioner, purpose and access constraints.           |
| Independent provider            | Apply provider conflict, quality and liability rules.            |
| Prior advisory work             | Address self-review threat or restrict scope.                    |
| Outcome-contingent fees         | Prohibited for assurance conclusions.                            |
| Management decisions            | Assessors do not accept risk or operate controls for management. |
| Specialist reliance             | Record competence, scope and responsibility.                     |

**APF-REQ-005** Fees or other rewards for an assurance provider shall not be contingent on the decision state issued.

**APF-REQ-006** A person who designed, operated or advised on a subject within the previous assessment period shall not assess or independently review that subject unless the self-review threat is safeguarded and the safeguard is disclosed in the statement.

# Part IX — Competence

AIDCF states competence expectations but does not accredit people or firms. AIDCF-009 Part B Part VII provides competence levels AC-0 to AC-6 that programmes may adopt.

| **Discipline**        | **Competence expectation**                                     |
|-----------------------|----------------------------------------------------------------|
| Programme lead        | Programme governance, intended use, stakeholders and improvement. |
| Lead assessor         | AIDCF method, assurance, evidence, gates and decisions.        |
| Electrical            | Power architecture, protection, power quality and testing.     |
| Mechanical            | Cooling, thermal, fluid and recovery.                          |
| Compute               | AI/HPC architecture, firmware and recovery.                    |
| Storage/network       | Integrity, performance, fabrics, failover and restore.         |
| Operations/resilience | Reliability, incident, continuity and crisis.                  |
| OT/security           | Identity, authority, control plane and response.               |
| Evidence/data         | Provenance, integrity, analytics, privacy and custody.         |
| Independent reviewer  | Senior assurance competence and impartial challenge.           |
| Programme auditor     | Management-system audit competence and knowledge of AIDCF.     |

# Part X — Scoping

Ambiguous boundaries cannot support strong reliance.

| **Element**      | **Programme rule**                                                                                   |
|------------------|------------------------------------------------------------------------------------------------------|
| Capability       | Identity, owner, lifecycle and architecture baseline.                                                |
| Service outcomes | Function, tolerance, duration, operating state and consequence.                                      |
| Boundary         | Physical, logical, organisational, provider and temporal.                                            |
| Operating states | Declared from NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION, SHUTDOWN, FAILED (AIDCF-003 §45). |
| Controls         | Applicable AIDCF-007A controls and assigned claim types.                                             |
| Gates            | Applicable CG-01 to CG-15 and evidence floors.                                                       |
| Dependencies     | Internal, external, shared, common-mode and recovery.                                                |
| Exclusions       | Visible rationale and residual effect.                                                               |
| Intended users   | Named users and permitted reliance.                                                                  |
| Materiality      | Decision-specific, using the AIDCF definition of material.                                           |

# Part XI — Evidence and testing

Programmes apply AIDCF-008 and AIDCF-009 without changing source authority.

| **Element**         | **Programme rule**                                                    |
|---------------------|-----------------------------------------------------------------------|
| Evidence plan       | Assertion-specific classes, quality, sufficiency and timing.          |
| Intake              | Identity, source, collector, custodian, classification and integrity. |
| Conflict            | Retain supporting, challenging and qualifying evidence.               |
| Derived evidence    | Source lineage, transformation, assumptions and review.               |
| Sampling            | Population, strata, method, expansion and limitation.                 |
| Testing             | Authority, initial state, method, abort and restoration.              |
| Safety              | The safety authority can stop work.                                   |
| Restricted evidence | Alternative evidence or explicit UNKNOWN Record.                      |
| Retention           | Legal, contractual, audit and decision lineage.                       |
| Disclosure          | Minimum necessary information with protection and redaction.          |

# Part XII — Evaluation

AIDCF-010 supports synthesis while the decision authority retains the decision.

| **Element**     | **Programme rule**                                                                                                      |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Control results | CONFORMING, PARTIAL, NONCONFORMING, UNKNOWN, NOT_APPLICABLE, NOT_ASSESSED, recorded per control and claim type.        |
| Findings        | Condition, criterion, evidence, cause and consequence.                                                                  |
| Scenarios       | Propagation, safeguards, residual state and recovery.                                                                   |
| Gates           | PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED by the AIDCF-009 roll-up rule; no conditional gate result.            |
| UNKNOWN         | Type U1–U10, severity US1–US5 and decision effect.                                                                     |
| Scores          | Control, family and domain scores with coverage and band, or "Band withheld (coverage/UNKNOWN)" (AIDCF-010). Scores never override gates. |
| Recommendation  | Controlling reasons and prohibited higher states.                                                                       |
| Review          | Technical and independent challenge.                                                                                    |
| Decision        | REASONABLY_ASSURED, CONDITIONALLY_ASSURED, LIMITED, NOT_ASSURED or INCONCLUSIVE, derived in the AIDCF-010 order (gates → UNKNOWN severity → coverage → bands → conditions and confidence) and worded per AIDCF-012 Part V. |
| Conditions      | Named, owned, time-bound and evidence-based.                                                                            |

**APF-REQ-007** Every programme decision shall be expressed in the controlled decision wording of AIDCF-012 Part V, which is the single authoritative wording table for AIDCF decision states.

# Part XIII — Assurance statement

The programme output is a bounded statement, not a certificate. Statement content and templates are defined in AIDCF-012 (templates AS-01 to AS-05 and lifecycle notices AS-06 to AS-08); this framework does not define separate templates. The programme determines which template applies (Part III) and who may issue it:

| **Programme responsibility** | **Rule**                                                                                                   |
|------------------------------|------------------------------------------------------------------------------------------------------------|
| Issuer                       | The organisation or provider issuing under its own authority, named in the charter.                         |
| Users and use                | Named audience and decision, as chartered.                                                                  |
| Template                     | AS-01 first-party; AS-02 co-sourced; AS-03 second-party; AS-04 independent provider; AS-05 continuing update. |
| Authorisation                | Decision authority after independent review (AIDCF-009 SG5, SG6; PG-7, PG-8).                              |
| Non-certification            | Every statement carries the AIDCF-012 non-certification note.                                               |

**APF-REQ-008** Assurance statements issued within a programme shall use the AIDCF-012 template for the programme model and shall not be issued before the independent review and decision-authority approval have been recorded.

# Part XIV — Prohibited claims

| **Claim**                         | **Programme rule**                                                       |
|-----------------------------------|--------------------------------------------------------------------------|
| AIDCF Certified                   | Prohibited.                                                              |
| AIDCF Accredited                  | Prohibited.                                                              |
| Compliant with all laws           | Prohibited unless separately authorised and evidenced.                   |
| Safe/secure/resilient universally | Prohibited guarantee.                                                    |
| Continuous assurance universally  | Prohibited unless specific monitored claims and blind spots are defined. |
| Pass based on score               | Prohibited when gates or UNKNOWN control.                                |
| Engineering approval              | AIDCF does not replace it.                                               |
| Framework-owner endorsement       | Not implied by use.                                                      |
| Public ranking                    | Requires a separate approved cohort method.                              |
| Transfer of assurance             | Requires applicability across capability, boundary, state and time.      |

# Part XV — Reporting

Different reports use the same underlying evidence and decision. Report classes are defined in AIDCF-012 Part III.

| **Programme need**  | **AIDCF-012 report class**                               |
|---------------------|----------------------------------------------------------|
| Executive reporting | R1 Executive Assurance Report                            |
| Technical record    | R2 Technical Assessment Report; R3 Domain Report         |
| Evidence            | R4 Evidence Package                                      |
| Gates and decision  | R5 Gate and Decision Package                             |
| Relying party       | R6 Customer/Second-Party Statement                       |
| Regulator           | R7 Regulatory Support Package                            |
| Public              | R8 Public Summary (never stronger than the full report)  |
| Continuing          | R9 Continuing-Assurance Report                           |
| Remediation         | R10 Remediation/Closure Report                           |

Management responses remain separate from assessor conclusions (AIDCF-012 Part XI).

# Part XVI — Validity and reassessment

No conclusion remains valid indefinitely by default.

| **Element**     | **Programme rule**                                                             |
|-----------------|--------------------------------------------------------------------------------|
| Validity        | Point in time or period, conditions and evidence basis; lifecycle EXPIRED at end of validity. |
| Evidence expiry | Mandatory evidence expiry triggers review.                                     |
| Material change | Architecture, capacity, configuration, supplier or ownership.                  |
| Incident        | May set affected decisions to SUSPENDED.                                       |
| Gate change     | A Gate Result change to FAIL or UNKNOWN, or a new US4/US5 UNKNOWN, triggers review. |
| Closure         | Requires evidence and reassessment.                                            |
| Periodic review | Set by risk, freshness and reliance.                                           |
| Supersession    | New decision SUPERSEDES the prior; history preserved.                          |
| Withdrawal      | Issuer sets WITHDRAWN when reliance is no longer defensible.                   |

**APF-REQ-009** Every ACTIVE Assurance Decision issued within a programme shall have a stated validity end date or triggering event after which its lifecycle state becomes EXPIRED unless reassessed.

# Part XVII — Continuing assurance

Continuing assurance (AL6) is claim-specific monitoring plus human decision.

| **Element**      | **Programme rule**                                                    |
|------------------|-----------------------------------------------------------------------|
| Baseline         | Initial defensible assessment and ACTIVE decision.                    |
| Source register  | Authoritative sources, owners and health.                             |
| Monitored claims | Explicit propositions, operating states and dependencies.             |
| Refresh          | Evidence validation cadence.                                          |
| Triggers         | Change, incident, threshold, missing data, conflict and gate event.   |
| Blind spots      | Source outage and uncovered states visible.                           |
| Human review     | Automation proposes; the decision authority approves material status. |
| Decision effect  | Maintain ACTIVE, add or change conditions (new decision), SUSPENDED, WITHDRAWN, or reassess. |
| Snapshot         | Immutable evidence, rules and lineage.                                |

**APF-REQ-010** Continuing assurance shall be limited to explicitly designated claims with defined sources, refresh cadence, triggers and blind spots, and shall not be described as continuous assurance of the whole Capability Instance.

# Part XVIII — Quality and challenge

| **Element**        | **Programme rule**                                     |
|--------------------|--------------------------------------------------------|
| Quality plan       | Review points and technical approvals.                 |
| Hot review         | Before material conclusion.                            |
| Cold review        | Post-issuance sample.                                  |
| Consultation       | Resolve specialist disagreement.                       |
| Evidence challenge | Assertion-to-evidence trace and contrary evidence.     |
| Appeal             | Challenge facts or method, not negotiate outcome.      |
| Complaint          | Conduct, confidentiality and process concerns.         |
| Correction         | Material error triggers corrected or superseding report. |
| Conflict register  | Commercial, management and reviewer conflicts.         |

**APF-REQ-011** The programme shall perform cold reviews of a sample of issued decisions in each management-review period and shall feed the results into corrective action (Part XXI).

# Part XIX — Data and graph

Assurance does not justify overcollection or exposure of infrastructure paths.

| **Element**        | **Programme rule**                                               |
|--------------------|------------------------------------------------------------------|
| Minimisation       | Collect only for precise assertions.                             |
| Authorisation      | Source-owner approval.                                           |
| Classification     | Protect architecture, credentials, controls and dependencies.    |
| Segregation        | Separate client, provider and public packages.                   |
| Redaction          | Preserve limitations when details are withheld from disclosure.  |
| Retention/deletion | Preserve obligations and lineage.                                |
| Graph security     | Restrict sensitive paths and exports.                            |
| AI use             | AI-derived material is candidate, lineage-linked and reviewed.   |
| Native conclusions | AIDCF and AITG decisions remain separate.                        |

# Part XX — Commercial deployment

AIDCF supports services and products without certification claims.

| **Offering**          | **Programme rule**                                       |
|-----------------------|----------------------------------------------------------|
| Readiness review      | Profile, evidence gaps and roadmap.                      |
| Design assurance      | Architecture and safeguard design.                       |
| Deployment assurance  | Implementation, commissioning and handover.              |
| Operational assurance | Representative operating evidence and gates.             |
| Resilience assurance  | Scenario, containment, recovery and exercise.            |
| Continuing assurance  | Subscription or cadence for approved monitored claims.   |
| Second-party review   | Supplier or customer decision support.                   |
| Platform subscription | Workflow, evidence and graph; human authority remains.   |
| Benchmarking          | Comparable cohort analytics.                             |
| Method licence        | Use under terms; no implied endorsement.                 |

# Part XXI — Management-system integration and continual improvement

An AIDCF assurance programme is operated as a management system: it is planned, performed, checked and improved, and it can be integrated with an organisation's existing management systems. In particular, it is designed to sit within or alongside an AI management system conforming to ISO/IEC 42001 and an information security management system conforming to ISO/IEC 27001. Both standards follow the ISO harmonized structure for management system standards; AIDCF does not reproduce their requirements and conformance to AIDCF-011 does not imply conformance to either standard.

## XXI.1 Plan-Do-Check-Act loop

| **PDCA phase** | **AIDCF programme activity**                                                                                                                         | **Records**                                     |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Plan           | Establish programme scope, objectives (for example coverage of critical Capability Instances, timeliness of reassessment), risks to the programme, resources, competence and the programme plan (P0–P4). | Programme charter, profile, plan, objectives    |
| Do             | Execute assessments under AIDCF-009, evaluate under AIDCF-010, decide and report under AIDCF-012 (P5–P8).                                            | Assessment packages, decisions, statements      |
| Check          | Monitor programme performance indicators; perform internal audit of the assurance programme; perform cold reviews; hold management review.         | Indicator reports, audit reports, review minutes |
| Act            | Address nonconformities with corrective action; implement improvements to method application, competence, tooling and evidence architecture.       | Corrective-action and improvement registers     |

## XXI.2 Programme objectives and performance indicators

The programme sets measurable objectives and monitors them. Indicators are programme parameters chosen by the steering group; examples: proportion of in-scope Capability Instances with an ACTIVE decision; proportion of decisions reassessed before EXPIRED; number and age of open US4/US5 UNKNOWN Records; proportion of conditions closed by their due date; cold-review exceptions; corrective actions overdue.

**APF-REQ-012** The programme shall define measurable objectives and performance indicators, review them at each management review and record the action taken where an objective is not met.

## XXI.3 Internal audit of the assurance programme

Internal audit of the programme examines whether the programme conforms to AIDCF-011 and to the organisation's own programme requirements, and whether it is effectively implemented. It is distinct from AIDCF assessments of Capability Instances: it audits how assurance is done, not the infrastructure.

| **Audit topic**             | **Examples of audit evidence**                                                                                      |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------|
| Method conformance          | Sampled assessment packages traced against AIDCF-009 Part A requirements and stage gates.                           |
| Independence and competence | Conflict declarations, AC-level records, reviewer separation.                                                       |
| Evidence integrity          | Evidence manifests, custody and integrity references.                                                               |
| Decision integrity          | Decision states versus Gate Results, UNKNOWN severities and AIDCF-010 ceilings; controlled wording per AIDCF-012.   |
| Validity and reassessment   | Triggers fired versus reassessments performed; expired decisions still relied on.                                   |
| Prohibited claims           | Published material checked against Part XIV.                                                                        |

**APF-REQ-013** The programme shall be internally audited at planned intervals, set by the steering group in proportion to reliance, by an auditor independent of the programme lead and of the assessments sampled; audit results shall be reported to management review.

## XXI.4 Management review

| **Inputs**                                                                                                                | **Outputs**                                                             |
|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Status of actions from previous reviews; changes in context (new AI infrastructure, providers, regulation, AIDCF artifact versions); performance indicators; internal-audit and cold-review results; nonconformities and corrective actions; appeals and complaints; open US4/US5 UNKNOWN Records across the portfolio; resource and competence adequacy; interfaces with ISO/IEC 42001 and ISO/IEC 27001 management reviews. | Decisions on improvement, resources, programme scope and objectives; changes to the programme plan; escalation of portfolio-level risks to the organisation's governance. |

**APF-REQ-014** The steering group shall conduct a management review of the programme at planned intervals, using at least the inputs listed in XXI.4, and shall record its decisions and actions.

## XXI.5 Nonconformity and corrective action

A programme nonconformity is a failure of the programme to meet AIDCF-011, AIDCF-009 or its own requirements (for example a decision issued without independent review, a decision above its gate ceiling, a reassessment trigger not acted on). It is distinct from a Finding about the assessed infrastructure.

**APF-REQ-015** For each programme nonconformity the programme shall correct it, evaluate whether issued decisions are affected (and, where they are, correct, suspend or supersede them under AIDCF-012), determine its cause, implement corrective action to prevent recurrence and review the effectiveness of that action.

## XXI.6 Continual improvement

Improvement sources include corrective actions, audit and cold-review results, assessor feedback on AIDCF-009 procedures, recurring UNKNOWN causes (for example systematic evidence-access limits) and changes to the AIDCF artifacts. Proposed changes to AIDCF artifacts are submitted to the framework owner's change control.

**APF-REQ-016** The programme shall maintain an improvement register and shall record, for each improvement, its source, owner, status and effect on programme objectives.

## XXI.7 Integration with ISO/IEC 42001 and ISO/IEC 27001 management systems

| **Management-system topic (harmonized structure)** | **AIDCF programme contribution**                                                                                                     | **Integration note**                                                                                                     |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Context of the organisation                        | Capability Instances, Service Outcomes, dependency and boundary records (AIDCF-009 B2, B3).                                          | AI infrastructure dependencies inform the AI management system's context and the ISMS scope.                             |
| Leadership                                         | Steering group, decision authority and accountability (Part VII; CG-13).                                                             | Align decision authorities with roles assigned in the existing management systems.                                       |
| Planning (risks, opportunities, objectives)        | Programme objectives (XXI.2); gate-based risk view (CG-01–CG-15); UNKNOWN portfolio.                                                 | AIDCF Findings and UNKNOWN Records can be inputs to AI-system and information-security risk assessment and treatment.    |
| Support (resources, competence, documented information) | Competence (Part IX; AC levels), evidence architecture (AIDCF-008), records retention.                                           | Reuse existing document-control and competence processes where they meet AIDCF-008 provenance and custody requirements.  |
| Operation                                          | Assessments under AIDCF-009, change control (CG-14), digital authority (CG-15).                                                     | ISMS operational controls for identity, access and supplier security provide evidence for SEC and SUP controls.          |
| Performance evaluation                             | Indicators, internal audit of the programme, management review (XXI.2–XXI.4).                                                       | Programme internal audit and management review may be combined with those of the existing systems if AIDCF inputs are covered explicitly. |
| Improvement                                        | Nonconformity, corrective action and improvement register (XXI.5–XXI.6).                                                            | Use a common corrective-action process with AIDCF-specific classification of programme nonconformities.                 |

**APF-REQ-017** Where the organisation operates an ISO/IEC 42001 or ISO/IEC 27001 management system, the programme charter shall state how programme planning, internal audit, management review and corrective action are integrated with or kept separate from that system, and evidence drawn from it shall still meet AIDCF-008 requirements.

# Part XXII — Review and release gates (single authoritative table)

This table is the single authoritative list of reviewer roles and release-gate states for AIDCF-009 (Part A and Part B), AIDCF-011 and AIDCF-012. Those documents refer to it and do not maintain their own tables.

| **Reviewer role / pilot**             | **Applies to**                    | **Review focus**                                                                       | **Status** |
|---------------------------------------|-----------------------------------|----------------------------------------------------------------------------------------|------------|
| Methodology author                    | 009A, 009B, 011, 012              | Coherence with AIDCF-006 invariants and the canonical vocabularies.                    | Pending    |
| Lead assessor peer                    | 009A, 009B                        | Practical execution of procedures, decision trees and templates.                       | Pending    |
| Assurance and reporting specialist    | 011, 012                          | Programme models, statements and controlled decision wording.                          | Pending    |
| Electrical engineering reviewer       | 009A, 009B                        | Power playbook, inspection points, CG-05 and CG-04 workbooks.                          | Pending    |
| Mechanical engineering reviewer       | 009A, 009B                        | Thermal playbook, inspection points, CG-06 workbook.                                   | Pending    |
| Compute / HPC reviewer                | 009A, 009B, 012                   | Compute procedures, CG-08 workbook, technical reporting.                               | Pending    |
| Storage and network reviewer          | 009A, 009B                        | Storage and network procedures, CG-08 and CG-10 workbooks.                             | Pending    |
| Operations and reliability reviewer   | 009A, 009B                        | Fieldwork, operations and recovery procedures.                                         | Pending    |
| OT and security reviewer              | 009A, 009B, 011                   | Control-plane procedures, CG-07 and CG-15 workbooks, graph security.                   | Pending    |
| Evidence specialist                   | 009A, 009B, 012                   | Alignment with AIDCF-008; evidence playbooks and evidence reporting.                   | Pending    |
| Safety, legal and privacy reviewer    | 009A, 009B, 011, 012              | Testing boundaries, disclosure, classification and liability.                          | Pending    |
| Independent provider reviewer         | 011, 012                          | Independence safeguards and statement usability.                                       | Pending    |
| Internal audit reviewer               | 011                               | Programme internal audit and management-system integration.                            | Pending    |
| Second-party / customer reviewer      | 011, 012                          | Relying-party needs and AS-03 statement.                                               | Pending    |
| Regulatory liaison                    | 012                               | R7 package.                                                                            | Pending    |
| Board reader                          | 012                               | R1 executive report comprehension.                                                     | Pending    |
| Accessibility and design reviewer     | 012                               | Part XIV visual and accessibility rules.                                               | Pending    |
| Ontology, schema and AITG reviewer    | 009B, 011, 012                    | Graph mappings and machine-readable packages against AIDCF-014.                        | Pending    |
| Practitioner pilot (assessment)       | 009A, 009B                        | Reproducibility of results by an independent practitioner on a synthetic dataset.      | Pending    |
| Programme pilots (first-party, co-sourced, third-party, continuing) | 011     | Programme operation across models.                                                     | Pending    |
| Reporting pilots (executive, technical, statement, dashboard) | 012            | Report classes and templates.                                                          | Pending    |
| Public release                        | 009A, 009B, 011, 012              | All gates above.                                                                       | Not approved |

**APF-REQ-018** AIDCF-009, AIDCF-011 and AIDCF-012 shall not be released for public use until every reviewer role applicable to the document in Part XXII has recorded its review and the public-release gate has been passed through the framework owner's change control.

# Programme stage gates

Advance only when exit criteria are met; limitations remain explicit as UNKNOWN Records rather than as conditional approvals. A programme stage gate has the outcomes PROCEED, RETURN or STOP.

| **Gate**                | **Exit criteria**                                | **AIDCF-009 stage gate** |
|-------------------------|--------------------------------------------------|--------------------------|
| PG-0 Authorise          | Need, sponsor, users and authority.              | SG0                      |
| PG-1 Charter            | Question, capability, outcomes and model.        | SG0                      |
| PG-2 Scope              | Boundary, profile, level, gates and exclusions.  | SG1                      |
| PG-3 Provider           | Competence, independence and rules.             | SG2                      |
| PG-4 Plan               | Evidence, methods, safety and reviews.           | SG2                      |
| PG-5 Complete           | Fieldwork complete or UNKNOWN visible.           | SG3                      |
| PG-6 Technical review   | Domain conclusions and Gate Results approved.    | SG4                      |
| PG-7 Independent review | Package and wording challenged.                  | SG5                      |
| PG-8 Issue              | Decision and statement authorised.               | SG6                      |
| PG-9 Sustain            | Actions, evidence custody and triggers active; programme indicators updated. | SG7    |

# Domain programme coverage

Programme coverage applies the same rules in every domain: decisions link to the Capability Instance and Service Outcomes; scope covers assets, functions, providers, interfaces, operating states and dependencies; depth is set by AL0–AL6; methods are those of AIDCF-009; evidence follows AIDCF-008; outputs are results, Findings, UNKNOWN Records, Gate Results and a domain conclusion; material conclusions receive competent specialist and independent review; reassessment follows architecture, capacity, provider, incident and evidence triggers. The domain-specific elements are:

| **Domain** | **Programme coverage focus**                                         | **Principal gates informed (see AIDCF-007A registry v1.1 for control-level mappings)** | **Domain guide** |
|------------|-----------------------------------------------------------------------|----------------------------------|------------------|
| GOV        | Authority, decisions, policy and impartiality.                        | CG-13, CG-14                     | AIDCF-018-GOV    |
| CAP        | Capability, outcomes, demand and envelope.                            | CG-01, CG-02                     | AIDCF-018-CAP    |
| DEP        | Dependencies, concentration, providers and boundary.                  | CG-03, CG-02, CG-09              | AIDCF-018-DEP    |
| PHY        | Site, structure, zoning, access, custody and life safety.             | CG-04, CG-02                     | AIDCF-018-PHY    |
| POW        | Supply, generation, storage, distribution, quality and recovery.      | CG-05, CG-04, CG-07, CG-10       | AIDCF-018-POW    |
| THM        | Air and liquid cooling, heat rejection, fluids and thermal recovery.  | CG-06, CG-04, CG-07, CG-10       | AIDCF-018-THM    |
| ENV        | Environmental conditions, energy, water, carbon, hazards and climate. | CG-04, CG-02                     | AIDCF-018-ENV    |
| CMP        | Accelerator architecture, capacity, firmware, health and recovery.    | CG-08, CG-09, CG-10              | AIDCF-018-CMP    |
| STO        | Tiers, performance, integrity, protection and checkpoint recovery.    | CG-08, CG-10                     | AIDCF-018-STO    |
| NET        | Fabrics, congestion, service and management networks, optics, control.| CG-08, CG-09, CG-10              | AIDCF-018-NET    |
| OPS        | Staffing, work control, maintenance, alarms, change and capacity.     | CG-07, CG-13, CG-14              | AIDCF-018-OPS    |
| RES        | Strategy, containment, continuity, recovery, exercising and crisis.   | CG-09, CG-10                     | AIDCF-018-RES    |
| SUP        | Suppliers, contracts, provenance, updates, spares and remote support. | CG-03, CG-13, CG-15              | AIDCF-018-SUP    |
| SEC        | Identity, control planes, segmentation, patching, detection, automation. | CG-07, CG-15                  | AIDCF-018-SEC    |
| EVA        | Evidence, execution, Findings, gates and reassessment.                | None per control; supports meta-gates CG-11, CG-12 (evaluated across all controls) | AIDCF-018-EVA    |

The authoritative control-to-gate mapping is per control in the AIDCF-007A registry (`gateMappings`, roles CRITICAL or SUPPORTING).

# Programme playbooks

Every playbook follows the common sequence: (1) define decision and intended users; (2) define capability, outcomes, scope, operating states and profile; (3) select Assurance Level, gates and evidence depth; (4) appoint provider and team and assess competence and independence; (5) approve evidence, methods, sampling, safety and review plan; (6) execute AIDCF-009, preserving UNKNOWN and conflict; (7) apply AIDCF-010; (8) complete technical and independent review; (9) issue the AIDCF-012 statement without certification language; (10) activate actions, triggers and reassessment. The distinctive elements of each playbook are:

| **Playbook**          | **Trigger / decision**                                         | **Level** | **Distinctive steps**                                                                                                                       | **Statement**   |
|-----------------------|----------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Readiness             | Preparing for deployment or deeper assurance.                  | AL1       | Evidence-availability survey per control; gap roadmap; no decision state issued.                                                              | Readiness report (R1/R2) |
| Design assurance      | Pre-build or major design decision.                            | AL2       | Design-basis confirmation with capability owner; independent design review (E5) for gate-critical systems; DESIGN claims only.               | AS per model    |
| Deployment assurance  | Commissioning, handover or go-live.                            | AL3–AL5   | Witness integrated systems tests; reconcile as-built to design; capture commissioning evidence as E4 tied to the implemented configuration.   | AS per model    |
| Operational assurance | Reliance on current operation.                                 | AL4       | Define representative period and states; sample occurrences; review incidents and exceptions in period.                                     | AS per model    |
| Resilience assurance  | Reliance on containment and recovery.                          | AL5       | Select cross-domain scenarios; authorise integrated exercises; measure end-to-end outcome recovery.                                         | AS per model    |
| Major change          | Material change to architecture, capacity, provider or control plane. | Affected claims | Change-impact mapping to controls and gates; delta reassessment; supersede prior decision.                                       | AS per model; AS-08 where superseded |
| Incident-triggered    | Incident affecting relied-on claims.                           | Affected claims | Set affected decisions SUSPENDED where material; preserve incident evidence; reassess affected gates.                                  | AS-06, then AS per model or AS-07 |
| Second-party          | Customer, investor or contracting-party decision.              | As chartered | Disclose commissioner and access limits; agree evidence rights in advance.                                                              | AS-03           |
| Independent-provider  | Third-party reliance.                                          | As chartered | Provider conflict check, engagement terms, provider quality review.                                                                      | AS-04           |
| Continuing assurance  | Ongoing reliance on designated claims.                         | AL6       | Source register; refresh cadence; trigger monitoring; human review of material status changes.                                              | AS-05           |

# Machine-readable publication package

Tools implement declared workflow and never hidden authority.

| **Artifact**                     | **Purpose**                                         |
|----------------------------------|-----------------------------------------------------|
| aidcf-apf-config.json            | Programme configuration.                            |
| programme-charter.schema.json    | Decision, subject, users, model and authority.      |
| programme-profile.schema.json    | Level, type, controls, gates and evidence.          |
| provider-role.schema.json        | Competence and independence.                        |
| programme-plan.schema.json       | Methods, safety and reviews.                        |
| validity-trigger.schema.json     | Monitoring and reassessment.                        |
| quality-review.schema.json       | Review, appeal and correction.                      |
| programme-audit.schema.json      | Internal audit, management review and corrective action. |
| conformance-tests                | Non-certification, safety and lineage fixtures.     |

Assurance statements use the AIDCF-012 assurance-statement schema. Ontology and validation shapes are published under AIDCF-014 and AIDCF-016.

# AITG and graph mappings

Programme records are native AIDCF objects using AIDCF-014 classes and relationships.

| **Programme record** | **AIDCF-014 class**    | **Relationship (AIDCF-014 §9)**                                       |
|----------------------|------------------------|-----------------------------------------------------------------------|
| Programme            | AssuranceProgram       | GOVERNED_BY (Assessment GOVERNED_BY AssuranceProgram)                 |
| Charter, profile     | Properties of AssuranceProgram | —                                                             |
| Provider, roles      | Properties of Assessment and ReviewRecord | REVIEWED_BY, APPROVED_BY                           |
| Capability           | CapabilityInstance     | ASSESSED_BY (CapabilityInstance ASSESSED_BY Assessment)               |
| Evidence             | EvidencePackage        | SUPPORTS, CHALLENGES, QUALIFIES                                       |
| Gate                 | GateResult             | CONSTRAINS (GateResult CONSTRAINS AssuranceDecision)                  |
| Decision             | AssuranceDecision      | APPROVED_BY                                                           |
| Statement            | AssuranceStatement     | REPORTED_IN (AssuranceDecision REPORTED_IN AssuranceStatement)        |
| Action               | Action                 | REQUIRES_ACTION, CLOSED_BY                                            |
| Trigger              | ReassessmentTrigger    | TRIGGERS_REASSESSMENT                                                 |
| Supersession         | —                      | SUPERSEDES                                                            |

Previous non-canonical relationships ASSIGNED_TO, ASSURES, EXECUTES, ISSUED_BY, REPORTS, REMEDIATES and REQUIRES_REVIEW are replaced as shown.

# Templates

Assurance statements use AIDCF-012 templates AS-01 to AS-05; this framework provides programme templates only.

## Template — Programme Charter

| **Field**        | **Entry**                                                         |
|------------------|-------------------------------------------------------------------|
| programmeId      | Stable programme identifier.                                      |
| decisionQuestion | Decision the programme supports.                                  |
| intendedUsers    | Named users and permitted reliance.                               |
| capability       | Capability Instances in scope.                                    |
| outcomes         | Service Outcomes and tolerances.                                  |
| model            | Programme model (Part III).                                       |
| type             | Assessment type (Part V).                                         |
| level            | Assurance Level AL0–AL6.                                          |
| statementTemplate| AIDCF-012 template (AS-01–AS-05).                                 |
| authority        | Sponsor and decision authority.                                   |
| managementSystem | Integration with ISO/IEC 42001 or ISO/IEC 27001 systems (XXI.7).  |
| constraints      | Access, safety, legal and confidentiality constraints.            |
| approvals        | Charter approvals.                                                |

## Template — Programme Profile

| **Field**     | **Entry**                                                     |
|---------------|---------------------------------------------------------------|
| scope         | Capability Instances and boundary.                            |
| states        | Operating states in scope.                                    |
| controls      | Applicable controls and claim types.                          |
| gates         | Applicable gates.                                             |
| evidenceDepth | Profile tiers and sufficiency floors.                         |
| methods       | AIDCF-009 methods and Part B elements adopted.                |
| outputs       | AIDCF-012 report classes.                                     |
| validity      | Validity period and triggers.                                 |

## Template — Provider Record

| **Field**        | **Entry**                                             |
|------------------|-------------------------------------------------------|
| provider         | Organisation.                                         |
| roles            | Roles assigned.                                       |
| competence       | Competence evidence (AC levels where adopted).        |
| conflicts        | Declared conflicts.                                   |
| safeguards       | Independence safeguards.                              |
| responsibilities | Responsibility split with management.                 |
| authority        | Professional and contractual authority.               |

## Template — Programme Plan

| **Field**   | **Entry**                                    |
|-------------|----------------------------------------------|
| workstreams | Domain workstreams and leads.                |
| evidence    | Evidence requests and access.                |
| interviews  | Interview plan.                              |
| inspections | Inspection plan.                             |
| samples     | Sampling plans.                              |
| tests       | Test plans and authorisations.               |
| safety      | Rules of engagement.                         |
| reviews     | Technical and independent reviews.           |
| stageGates  | PG-0 to PG-9 dates and approvers.            |

## Template — Continuing Assurance

| **Field**       | **Entry**                                       |
|-----------------|-------------------------------------------------|
| claims          | Designated monitored claims.                    |
| sources         | Source register and owners.                     |
| thresholds      | Trigger thresholds.                             |
| refresh         | Refresh cadence.                                |
| blindSpots      | Uncovered states and source outages.            |
| triggers        | Reassessment Triggers.                          |
| review          | Human review arrangements.                      |
| decisionState   | Current decision state and lifecycle state.     |
| snapshot        | Snapshot reference.                             |

## Template — Quality Review

| **Field**          | **Entry**                                    |
|--------------------|----------------------------------------------|
| reviewId           | Stable identifier.                           |
| reviewType         | Hot review, cold review or consultation.     |
| scope              | Decisions and packages reviewed.             |
| samples            | Items sampled.                               |
| technicalApprovals | Approvals verified.                          |
| challenges         | Challenges raised.                           |
| dispositions       | Resolution of challenges.                    |
| appeals            | Appeals received and outcome.                |
| corrections        | Corrections or supersessions issued.         |
| release            | Release decision.                            |

## Template — Programme Audit and Management Review

| **Field**            | **Entry**                                                        |
|----------------------|------------------------------------------------------------------|
| auditId              | Stable identifier.                                               |
| auditor              | Auditor and independence basis.                                  |
| auditScope           | Topics and assessments sampled (XXI.3).                          |
| nonconformities      | Programme nonconformities and classification.                    |
| correctiveActions    | Actions, owners, due dates and effectiveness review.             |
| managementReviewRef  | Management review at which results were considered.              |
| decisions            | Management-review decisions and improvement-register entries.    |

# Annex A — Conformance validation and requirement mapping

The following requirements are validation rules applied to every programme.

**APF-REQ-019** The programme charter shall state the decision question, intended users, Capability Instances and Service Outcomes.

**APF-REQ-020** The programme model, assessment type and Assurance Level shall be approved at PG-1 or PG-2.

**APF-REQ-021** Scope, operating states, dependencies and exclusions shall be visible in the programme profile.

**APF-REQ-022** Applicable controls, claim types and gates shall be defined in the programme profile.

**APF-REQ-023** Evidence depth shall match the claim types concluded (Part IV).

**APF-REQ-024** Competence and independence of every assessor and reviewer shall be assessed and recorded before PG-3.

**APF-REQ-025** Management and assessor responsibilities shall be recorded separately.

**APF-REQ-026** Safety and stop criteria shall be documented in the programme plan.

**APF-REQ-027** UNKNOWN Records and conflicts shall remain visible in every programme output.

**APF-REQ-028** Scores shall not override Gate Results.

**APF-REQ-029** Tooling shall not approve results, Gate Results or decisions automatically.

**APF-REQ-030** Corrections and supersessions shall preserve history.

**APF-REQ-031** A public summary shall not be stronger than the full report.

| **v1.0 validation** | **v1.1 requirement**        |
|---------------------|-----------------------------|
| APF-VAL-001         | APF-REQ-001           |
| APF-VAL-002         | APF-REQ-019                 |
| APF-VAL-003         | APF-REQ-020                 |
| APF-VAL-004         | APF-REQ-021                 |
| APF-VAL-005         | APF-REQ-022                 |
| APF-VAL-006         | APF-REQ-023                 |
| APF-VAL-007         | APF-REQ-024                 |
| APF-VAL-008         | APF-REQ-025                 |
| APF-VAL-009         | APF-REQ-026                 |
| APF-VAL-010         | APF-REQ-027                 |
| APF-VAL-011         | APF-REQ-028                 |
| APF-VAL-012         | APF-REQ-007          |
| APF-VAL-013         | APF-REQ-009            |
| APF-VAL-014         | APF-REQ-010           |
| APF-VAL-015         | APF-REQ-029                 |
| APF-VAL-016         | APF-REQ-030                 |
| APF-VAL-017         | APF-REQ-031                 |

Other identifier changes: artifact ID AIDCF-APF-001 → AIDCF-011; the five "Statement Template" sections → AIDCF-012 AS-01–AS-05; the "Template — Assurance Statement" → AIDCF-012 AS templates; the AL0–AL6 profile sections → Part IV table; the fifteen domain programme profiles → "Domain programme coverage" table; the ten programme playbooks → "Programme playbooks" table; the "Review and release gates" table → Part XXII.

## Final doctrine

AIDCF-011 enables disciplined, self-improving assurance programmes without presenting AIDCF as a certifying or accrediting body. The issuer remains responsible for competence, independence, professional obligations and the bounded statement issued. The assessed organisation remains responsible for the capability, risks, controls, actions and decisions.
