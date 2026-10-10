> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-009_Part_A_Core_Practitioner_Handbook_v1.1.pdf](AIDCF-009_Part_A_Core_Practitioner_Handbook_v1.1.pdf).

**AIDCF**

# ASSESSMENT METHODOLOGY PRACTITIONER HANDBOOK — PART A: CORE HANDBOOK

*AI Data Centre Facilities Assurance Framework*

Version 1.1

Normative assessment method: roles, independence, competence, stage gates, procedures from chartering to reassessment, domain playbooks, workpaper templates WP-01 to WP-20 and controlled status vocabulary

Artifact ID: AIDCF-009 (Part A)  
Status: Draft for controlled review  
Author: Siva Sethumadhavan

# Document control

| **Field**        | **Value**                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Title            | AIDCF-009 Assessment Methodology Practitioner Handbook — Part A: Core Handbook                                                       |
| Artifact ID      | AIDCF-009 (requirement short code AMH)                                                                                                |
| Part             | Part A — Core Handbook (normative). Companion: AIDCF-009 Part B — Enhanced Companion                                                  |
| Version          | 1.1                                                                                                                                   |
| Date             | 2026-10-10                                                                                                                            |
| Status           | Draft for controlled review                                                                                                           |
| Author           | Siva Sethumadhavan                                                                                                                    |
| Depends on       | AIDCF-001, AIDCF-002, AIDCF-003, AIDCF-004, AIDCF-006, AIDCF-007A, AIDCF-008, AIDCF-010, AIDCF-011, AIDCF-012, AIDCF-014, AIDCF-018   |
| Control universe | 15 domains, 90 families and 360 controls as defined in the AIDCF-007A Canonical Master Control Registry                               |
| Evidence basis   | AIDCF-008 evidence classes E1–E7, quality dimensions, quality bands Q0–Q5, sufficiency S0–S5, confidence CONF-0 to CONF-4 and UNKNOWN |
| Purpose          | Initiate, scope, plan, execute, review, decide, report and reassess AIDCF assessments                                                  |
| Safety           | No hazardous or disruptive testing without explicit authority and competent engineering governance                                    |

## Revision history

| **Version** | **Date**   | **Summary**                                                                                                                                                                                                                                                                 |
|-------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | —          | Initial practitioner handbook (published under the superseded identifier AIDCF-AM-001).                                                                                                                                                                                      |
| 1.1         | 2026-10-10 | Designated as AIDCF-009 Part A (normative core); added Part A/Part B relationship; renamed workpaper templates E1–E20 to WP-01–WP-20; replaced 90 boilerplate family procedures with 15 domain playbooks pointing to AIDCF-018 guides and the AIDCF-007A registry; aligned all vocabularies to the canonical AIDCF set; introduced AMH-REQ requirement IDs with mapping annex. |

# Executive thesis

An AIDCF assessment is a controlled chain from decision question to Capability Instance, Service Outcomes, boundary, dependencies, controls, failure paths, evidence, critical gates, independent review and a bounded Assurance Decision. The chain is never strengthened by presentation, averaging or automation.

# 0 Introduction

## 0.1 Purpose and scope

This Part A defines the normative method by which an AIDCF assessment is chartered, planned, executed, evaluated, reviewed, decided, reported and reassessed. It applies to every assessment type and Assurance Level defined in AIDCF-011, to every programme model (first-party, co-sourced, second-party and independent third-party) and to every domain of the AIDCF-007A control universe.

Part A does not define control content (that is the AIDCF-007A registry), evidence semantics (AIDCF-008), gate criteria, scoring and decision ceilings (AIDCF-010), programme governance (AIDCF-011) or report and statement content (AIDCF-012). Where Part A refers to those artifacts it applies them; it does not restate or modify them.

## 0.2 Normative language

"Shall" and "shall not" state requirements; "should" and "should not" state recommendations; "may" states a permission; "can" states a capability. This usage follows ISO/IEC Directives, Part 2. Every requirement in this Part carries a stable identifier of the form AMH-REQ-NNN.

## 0.3 How Part A and Part B fit together

AIDCF-009 is published as two documents with one artifact identifier.

| **Aspect**             | **Part A — Core Handbook (this document)**                                                                                                                                 | **Part B — Enhanced Companion**                                                                                                                                                                      |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Status                 | Normative. Conformance to AIDCF-009 requires conformance to Part A.                                                                                                        | Normative where a clause uses "shall" and the assessor has adopted that element (Part B §0.3); otherwise informative execution aid.                                                                  |
| Content                | Roles, independence, competence, stage gates SG0–SG7, procedures A1–A7, B1–B14, C1–C9, domain playbooks, workpaper templates WP-01–WP-20, controlled status vocabulary.     | Decision trees DT-01–DT-20, generic assessment protocol per claim type, index of control-specific procedures, inspection checklists, evidence-collection playbooks, gate workbooks, synthetic examples, assessor competence levels AC-0–AC-6, graph-ingestion mappings, record schemas. |
| Precedence             | Part A prevails over Part B on any conflict.                                                                                                                               | Part B elaborates Part A and cannot relax a Part A requirement.                                                                                                                                      |
| Requirement IDs        | AMH-REQ-001 to AMH-REQ-064.                                                                                                                                                | AMH-REQ-065 to AMH-REQ-086 (numbering continues from Part A so that every AIDCF-009 requirement ID is unique).                                                                                             |
| Typical use            | Every assessment.                                                                                                                                                          | Assessments that want structured decision support, deeper fieldwork aids or graph integration; mandatory protocol elements are referenced from Part A procedure C1.                                |

Cross-references between the Parts use the form "Part B §II.3" or "Part A procedure C1".

**AMH-REQ-001** An organisation or provider claiming that an assessment was performed in accordance with AIDCF-009 shall conform to every requirement of Part A that is applicable to the declared assessment type and Assurance Level, and shall state which Part B elements, if any, were adopted.

**AMH-REQ-002** Where Part B and Part A appear to conflict, the assessor shall apply Part A and shall record the conflict for the AIDCF-009 change-control process.

## 0.4 Where control-specific content lives

The 360 controls are distinct topics. Each control is assessed for one or more claim types (DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS, RESILIENCE). The control-specific objective, requirement, assessment criteria, assessment procedure, evidence profile, gate mappings and UNKNOWN rule are carried in the AIDCF-007A Canonical Master Control Registry v1.1 (fields `assessmentCriteria`, `assessmentProcedure`, `evidenceProfile`, `gateMappings`, `unknownRule`). Domain-specific engineering guidance is carried in the AIDCF-018 domain guides (AIDCF-018-GOV through AIDCF-018-EVA). The generic, claim-type assessment protocol that applies to every control is in Part B Part II.

## 0.5 Canonical chain and terms

The assessment chain follows the AIDCF assurance-case structure, which is based on ISO/IEC/IEEE 15026-2: Decision Question → Capability Instance → Service Outcome → Required Function → Architecture → Dependency and Fault Domain → Threat / Hazard / Failure Scenario → Safeguard → Control → Evidence Requirement → Evidence Object → Control Assessment → Finding / UNKNOWN Record → Gate Result → Score Snapshot and Decision Recommendation → Assurance Decision, with the Report and Reassessment Trigger closing the loop.

The top claim of every assessment has the form: "Capability Instance X can achieve Service Outcomes Y within tolerances T under declared operating states S, for decision question Q, as of date D."

A fact, dependency, condition, deficiency or UNKNOWN is **material** if, had it been known or resolved differently, a competent assessor would reasonably expect it to change a control result, a gate result, the decision state, or a condition, limitation or ceiling attached to the decision, for the declared Capability Instance, Service Outcomes and operating states.

## 0.6 Assessment lifecycle

Initiate → Profile → Scope → Tailor → Plan → Collect → Validate → Assess → Analyse → Gate → Find → Review → Decide → Report → Reassess

| **Lifecycle phase**        | **Part A procedures**   | **Stage gate exit** |
|----------------------------|-------------------------|---------------------|
| Initiate                   | A1–A5, B1               | SG0                 |
| Profile, Scope, Tailor     | B2, B3, B4              | SG1                 |
| Plan                       | B5, B14                 | SG2                 |
| Collect, Validate          | B6–B13                  | SG3                 |
| Assess, Analyse, Gate, Find| C1–C5                   | SG4                 |
| Review                     | C6                      | SG5                 |
| Decide, Report             | C7, C8                  | SG6, SG7            |
| Reassess                   | C9                      | Re-entry at SG0/SG1 |

## 0.7 Procedure conventions

Every procedure in sections A, B and C uses the same structure: purpose, entry criteria, a numbered step table, outputs, and escalation and stop criteria. The following apply to every procedure and are not repeated in each one.

| **Convention**           | **Rule applying to all procedures**                                                                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Common entry criteria    | An authorised assessment purpose and current scope exist (from B1 onwards, an approved charter WP-01); the preparer, technical reviewer and evidence sources are named.      |
| Records                  | Each step produces a workpaper record with the identifier shown in the "Record" column (WP-<procedure>-<step>), linked to the relevant WP-01–WP-20 template instance.       |
| Common outputs           | Completed workpaper with evidence references, review record, and any Finding, UNKNOWN Record or limitation raised.                                                          |
| Common quality checks    | No silent deletion or uncontrolled versioning; every material statement traces to evidence or to an UNKNOWN Record; method is proportionate and reproducible.               |
| Common stop criteria     | Pause or stop where authority, safety, evidence custody or competence is unresolved; stop any unsafe, unauthorised or uncontrolled activity; escalate critical missing evidence. |

**AMH-REQ-003** Every procedure step that contributes to a control result, Gate Result or Assurance Decision shall produce a retained workpaper record that identifies the preparer, the evidence relied on and the reviewer.

**AMH-REQ-004** Workpapers shall be version-controlled; a superseded or corrected workpaper shall be retained with its successor and shall not be deleted.

# A Foundations

## A1 Authority and conformance

Establish the authority under which the assessment is performed, the artifact versions applied and the conformance claim.

**Entry criteria (specific).** A request for assessment exists with an identified sponsor.

| **Step** | **Required action**                                                                                             | **Record** |
|----------|-----------------------------------------------------------------------------------------------------------------|------------|
| 1        | Confirm purpose, authority and intended users.                                                                  | WP-A1-01   |
| 2        | Declare applicable artifact versions (AIDCF-007A registry version, AIDCF-008, AIDCF-010, capability profile).  | WP-A1-02   |
| 3        | Record professional, legal, safety and confidentiality boundaries.                                              | WP-A1-03   |
| 4        | Define prohibited claims and exceptions (AIDCF-011 Part XIV).                                                   | WP-A1-04   |
| 5        | Approve version, repository and record controls.                                                                | WP-A1-05   |
| 6        | Declare the AIDCF-009 conformance claim: Part A in full, and any Part B elements adopted.                       | WP-A1-06   |
| 7        | Escalate any conflict with AIDCF constitutional invariants (AIDCF-006).                                         | WP-A1-07   |

**Outputs.** Authority record; artifact-version manifest; conformance claim.

**Escalation.** A conflict with AIDCF-006 invariants is escalated to the framework owner before fieldwork starts.

**AMH-REQ-005** The assessment shall declare, before fieldwork, the exact versions of AIDCF-007A, AIDCF-008, AIDCF-010 and any capability profile applied, and shall not change them during the assessment without a recorded change approved at the current stage gate.

## A2 Normative requirements for all assessment work

Establish the rules that every assessment applies regardless of type.

| **Step** | **Required action**                                                                                      | **Record** |
|----------|----------------------------------------------------------------------------------------------------------|------------|
| 1        | Identify Capability Instance and Service Outcomes.                                                       | WP-A2-01   |
| 2        | Declare boundary, operating states (AIDCF-003 §45), evidence period and evidence limits.                 | WP-A2-02   |
| 3        | Justify applicability and NOT_APPLICABLE decisions.                                                      | WP-A2-03   |
| 4        | Preserve UNKNOWN and conflicting evidence.                                                               | WP-A2-04   |
| 5        | Evaluate gates before scores.                                                                            | WP-A2-05   |
| 6        | Require independent review of material decisions.                                                        | WP-A2-06   |

**AMH-REQ-006** Every assessment shall identify the Capability Instance, the Service Outcomes with their tolerances, the operating states in scope and the decision question before any control is assessed.

**AMH-REQ-007** Missing, stale, inaccessible, unverifiable or conflicting evidence shall be recorded as an UNKNOWN Record and shall never be treated as favourable.

**AMH-REQ-008** Gate Results shall be determined before scores are computed, and no score, average or index shall override a Gate Result.

## A3 Assessment types, claim types and Assurance Levels

Select the assessment type, the target Assurance Level and the claim types to be assessed.

| **Step** | **Required action**                                                                                                     | **Record** |
|----------|-------------------------------------------------------------------------------------------------------------------------|------------|
| 1        | Define the primary decision question.                                                                                   | WP-A3-01   |
| 2        | Select the assessment type and target Assurance Level (AL0–AL6, AIDCF-011 Part IV).                                     | WP-A3-02   |
| 3        | Select the claim types to be assessed for each in-scope control and match evidence classes to claim type (AIDCF-008 §29). | WP-A3-03   |
| 4        | Identify mandatory gates and scenarios.                                                                                 | WP-A3-04   |
| 5        | Set method depth by consequence.                                                                                        | WP-A3-05   |
| 6        | Document excluded higher claim types and the reason.                                                                    | WP-A3-06   |

Claim types and the minimum Assurance Level at which each can be asserted:

| **Claim type**  | **What a CONFORMING result asserts**                                         | **Minimum Assurance Level** |
|-----------------|-------------------------------------------------------------------------------|-----------------------------|
| DESIGN          | The requirement and the approved design are adequate for the Service Outcome. | AL2                         |
| IMPLEMENTATION  | The as-built or configured state reconciles to the approved design.           | AL3                         |
| OPERATION       | The control operates as intended over a representative period and states.     | AL4                         |
| EFFECTIVENESS   | The control achieves its objective under tested or observed adverse conditions. | AL5                       |
| RESILIENCE      | The control contains failure and supports recovery within tolerance.          | AL5                         |

Assurance Levels are defined in AIDCF-011: AL0 Discovery, AL1 Readiness, AL2 Design, AL3 Implementation, AL4 Operational, AL5 Effectiveness and resilience, AL6 Continuing. The registry field "Required Assurance Level" uses AL2–AL5.

**AMH-REQ-009** A control result shall not be reported for a claim type whose minimum Assurance Level exceeds the Assurance Level of the assessment.

**AMH-REQ-010** Results for different claim types of the same control shall be recorded separately and shall not be merged into a single result.

## A4 Roles and independence

Staff the engagement with appropriate authority, competence and separation.

| **Step** | **Required action**                                    | **Record** |
|----------|--------------------------------------------------------|------------|
| 1        | Appoint sponsor and decision authority.                | WP-A4-01   |
| 2        | Assign lead assessor and domain specialists.           | WP-A4-02   |
| 3        | Assign evidence lead, quality and safety roles.        | WP-A4-03   |
| 4        | Declare conflicts of interest and safeguards.          | WP-A4-04   |
| 5        | Separate preparation, technical approval and decision. | WP-A4-05   |
| 6        | Record external specialist reliance.                   | WP-A4-06   |

Assessment roles:

| **Role**                | **Accountability in the assessment**                                                                                               | **May not also be**                                       |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Sponsor                 | Authorises the decision question, scope, resources and access.                                                                     | Independent reviewer                                      |
| Decision authority      | Issues the Assurance Decision after independent review, or declines to issue one.                                                   | Preparer of the workpapers on which the decision rests    |
| Lead assessor           | Directs the assessment, integrates domain results, drafts gate evaluations and the Decision Recommendation.                       | Independent reviewer; decision authority                  |
| Domain assessor / specialist | Performs and concludes domain procedures within demonstrated competence.                                                     | Technical reviewer of their own work                      |
| Evidence lead           | Controls evidence requests, intake, custody, classification and the evidence manifest.                                             | —                                                         |
| Technical reviewer      | Approves domain methods and technical conclusions before gate evaluation.                                                         | Preparer of the reviewed workpaper                        |
| Independent reviewer    | Challenges evidence, gate logic, decision recommendation and wording (procedure C6).                                               | Any preparation role in the same assessment               |
| Safety authority        | Approves, stops or suspends any intrusive inspection or test.                                                                      | —                                                         |
| Capability owner        | Owns outcomes, risks, management responses and actions.                                                                            | Assessor or reviewer for the same Capability Instance     |

Programme-level independence safeguards by programme model, and the single authoritative table of reviewer and release-gate roles, are defined in AIDCF-011 (Part VIII and Part XXII). Part A applies them at assessment level.

**AMH-REQ-011** The preparation of a workpaper, its technical approval, the independent review of the decision package and the Assurance Decision shall be performed by different persons.

**AMH-REQ-012** Every assessor and reviewer shall declare conflicts of interest before appointment; a declared self-review threat (for example prior design, operation or advisory work on the same subject) shall be safeguarded or the person shall be excluded from the affected scope.

**AMH-REQ-013** Assessors shall not operate controls, accept risk or make management decisions for the assessed organisation within the scope they assess.

## A5 Competency management

Demonstrate collective competence for the assessed domains.

| **Step** | **Required action**                                                       | **Record** |
|----------|---------------------------------------------------------------------------|------------|
| 1        | Map scope to required disciplines (per domain playbook, section D).       | WP-A5-01   |
| 2        | Assess qualifications and current experience.                             | WP-A5-02   |
| 3        | Assign licensed or authorised judgments to appropriately authorised persons. | WP-A5-03 |
| 4        | Brief team on AIDCF method and evidence rules.                            | WP-A5-04   |
| 5        | Track competence gaps and supervision.                                    | WP-A5-05   |
| 6        | Restrict conclusions where competence is absent.                          | WP-A5-06   |

Part B Part VII defines assessor competence levels AC-0 (observer) to AC-6 (decision authority) that may be used to evidence this procedure.

**AMH-REQ-014** No control result, Gate Result or technical conclusion shall be issued by a person who lacks demonstrated competence in the discipline concerned; where competence is absent the affected result shall be NOT_ASSESSED or UNKNOWN and the limitation shall be disclosed.

**AMH-REQ-015** Judgments that require a licensed or legally authorised professional (for example electrical protection settings, structural capacity or fire-engineering conclusions where regulation requires it) shall be relied on only from such a professional, with the reliance recorded.

## A6 Lifecycle stage gates

Control progression of the assessment from authorisation to archive. Stage gates SG0–SG7 govern the assessment process; they are distinct from the critical gates CG-01–CG-15, which govern the assurance conclusion.

| **Step** | **Required action**                                | **Record** |
|----------|----------------------------------------------------|------------|
| 1        | Approve SG0 purpose and authority.                 | WP-A6-01   |
| 2        | Approve SG1 capability and scope.                  | WP-A6-02   |
| 3        | Approve SG2 plan, safety and evidence.             | WP-A6-03   |
| 4        | Confirm SG3 fieldwork completeness or limitations. | WP-A6-04   |
| 5        | Complete SG4 technical and SG5 independent review. | WP-A6-05   |
| 6        | Approve SG6 decision and SG7 archive.              | WP-A6-06   |

| **Stage gate** | **Exit criteria**                                                                                                         | **Approver**         | **AIDCF-011 programme gate** |
|----------------|---------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------|
| SG0 Authorise  | Purpose, sponsor, decision authority, intended users, conformance claim and artifact versions recorded (A1, B1).          | Sponsor              | PG-0, PG-1                   |
| SG1 Scope      | Capability profile, boundary, dependency baseline, applicability matrix and target Assurance Level approved (B2–B4).      | Sponsor, lead assessor | PG-2                       |
| SG2 Plan       | Assessment plan, rules of engagement, safety approvals, evidence requests and team competence approved (A4, A5, B5, B14). | Lead assessor, safety authority | PG-3, PG-4          |
| SG3 Fieldwork  | All planned procedures complete, or each incomplete item recorded as NOT_ASSESSED or UNKNOWN with effect.                  | Lead assessor        | PG-5                         |
| SG4 Technical review | Control results, scenarios, Findings and Gate Results technically approved (C1–C5).                                 | Technical reviewers  | PG-6                         |
| SG5 Independent review | Decision package challenged and dispositioned (C6).                                                               | Independent reviewer | PG-7                         |
| SG6 Decide     | Assurance Decision issued, or a recorded decision not to issue one; report and statement authorised (C7, C8).                                          | Decision authority   | PG-8                         |
| SG7 Archive    | Package immutable, actions and Reassessment Triggers active, evidence custody confirmed.                                   | Lead assessor        | PG-9                         |

A stage gate has one of three outcomes: PROCEED, RETURN (rework before re-submission) or STOP. There is no conditional stage-gate outcome; a limitation that remains at a stage gate is carried forward as an UNKNOWN Record or NOT_ASSESSED result whose effect is evaluated at decision level.

**AMH-REQ-016** The assessment shall not progress past a stage gate until its exit criteria are met and the approver has recorded PROCEED; unresolved items shall be carried as UNKNOWN Records or NOT_ASSESSED results, not as conditional approvals.

## A7 Quality management

Make assessments reproducible, reviewable and resistant to unsupported claims.

| **Step** | **Required action**                                  | **Record** |
|----------|------------------------------------------------------|------------|
| 1        | Define workpaper identifiers and review conventions. | WP-A7-01   |
| 2        | Track open points, conflicts and deviations.         | WP-A7-02   |
| 3        | Perform evidence-to-assertion traces.                | WP-A7-03   |
| 4        | Perform finding-to-decision traces.                  | WP-A7-04   |
| 5        | Retain review comments and resolutions.              | WP-A7-05   |
| 6        | Issue the assessment conformance record.             | WP-A7-06   |

**AMH-REQ-017** Before SG5, the lead assessor shall complete a trace from every material statement in the Decision Recommendation to its Control Assessments, Gate Results, Findings, UNKNOWN Records and Evidence Objects, and shall resolve or disclose any break in the trace.

# B Planning and fieldwork

## B1 Initiation and chartering

Convert the request into a bounded assessment charter (template WP-01).

| **Step** | **Required action**                                                    | **Record** |
|----------|------------------------------------------------------------------------|------------|
| 1        | Record trigger and requested conclusion.                               | WP-B1-01   |
| 2        | Identify sponsor, decision owner and intended users.                   | WP-B1-02   |
| 3        | Define preliminary Capability Instance and Service Outcomes.           | WP-B1-03   |
| 4        | Set assessment type, target Assurance Level and exclusions.            | WP-B1-04   |
| 5        | Record constraints and approvals.                                      | WP-B1-05   |
| 6        | Freeze the charter baseline.                                           | WP-B1-06   |

**Outputs.** Approved charter WP-01 (SG0 exit).

**Escalation.** A requested conclusion that exceeds the achievable Assurance Level (for example a resilience conclusion with no authority to test or to obtain test evidence) is returned to the sponsor before SG0.

**AMH-REQ-018** Every assessment shall have an approved charter (WP-01) stating the decision question, Capability Instance, intended users, assessment type, target Assurance Level, exclusions and decision authority before any evidence is requested.

## B2 Capability profiling

Build the capability, outcome and operating-envelope model (template WP-02).

| **Step** | **Required action**                                                   | **Record** |
|----------|-----------------------------------------------------------------------|------------|
| 1        | Identify owner, lifecycle stage and architecture baseline.            | WP-B2-01   |
| 2        | Define Service Outcome tolerances and criticality.                    | WP-B2-02   |
| 3        | Map Required Functions and demand.                                    | WP-B2-03   |
| 4        | Record peak, transient and forecast demand.                           | WP-B2-04   |
| 5        | Define operating states and operating envelope.                       | WP-B2-05   |
| 6        | Validate the profile with competent specialists.                      | WP-B2-06   |

**Outputs.** Capability profile WP-02. An undefined or unowned Capability Instance or Service Outcome is a CG-01 matter and is recorded as an UNKNOWN Record with severity US5 (Systemic).

**AMH-REQ-019** Service Outcomes shall be stated with measurable tolerances and the operating states in which they apply; an outcome without a tolerance shall not support any CONFORMING result for a control whose objective depends on it.

## B3 Boundary and dependency discovery

Set the assessment boundary and map dependencies (template WP-03).

| **Step** | **Required action**                                            | **Record** |
|----------|----------------------------------------------------------------|------------|
| 1        | Set physical, logical, organisational and temporal boundaries. | WP-B3-01   |
| 2        | Identify boundary crossings and interfaces.                    | WP-B3-02   |
| 3        | Map upstream, downstream and recovery dependencies.            | WP-B3-03   |
| 4        | Identify shared, common-mode and concentration dependencies.   | WP-B3-04   |
| 5        | Record exclusions and evidence-access constraints.             | WP-B3-05   |
| 6        | Approve scope and dependency baseline.                         | WP-B3-06   |

**AMH-REQ-020** Every exclusion from the boundary shall state its rationale, the Service Outcomes it can affect and its effect on the decision; an exclusion that removes a material dependency shall be disclosed in the Assurance Decision and in every report class issued.

## B4 Applicability and tailoring

Determine which controls and claim types apply (template WP-04).

| **Step** | **Required action**                                                                                  | **Record** |
|----------|------------------------------------------------------------------------------------------------------|------------|
| 1        | Map entities and Required Functions to the 15 domains.                                               | WP-B4-01   |
| 2        | Determine applicability for each of the 360 controls using the registry `applicability` field.       | WP-B4-02   |
| 3        | Assign claim types per control, consistent with the registry required Assurance Level and the assessment AL. | WP-B4-03 |
| 4        | Select in-scope gates and confirm control-to-gate mappings (CRITICAL / SUPPORTING) from the registry. | WP-B4-04  |
| 5        | Approve NOT_APPLICABLE rationale.                                                                    | WP-B4-05   |
| 6        | Add capability-profile controls or stronger evidence floors without weakening the baseline.          | WP-B4-06   |

**AMH-REQ-021** A control shall be NOT_APPLICABLE only with a recorded rationale, an approver independent of the preparer, and confirmation that no in-scope Required Function depends on the control's subject; a blank or missing applicability decision shall be treated as NOT_ASSESSED.

**AMH-REQ-022** Tailoring shall not lower an evidence floor, a gate mapping role or a required claim type below the AIDCF-007A registry value.

## B5 Assessment planning

Produce the assessment plan (template WP-05).

| **Step** | **Required action**                                                                                  | **Record** |
|----------|------------------------------------------------------------------------------------------------------|------------|
| 1        | Assign domain leads and technical reviewers.                                                         | WP-B5-01   |
| 2        | Map each control and claim type to assessment methods (INQUIRY, DOCUMENT_REVIEW, INSPECTION, OBSERVATION, RECONCILIATION, ANALYSIS, SAMPLING, TEST, REPERFORMANCE, SCENARIO_EXERCISE) and evidence requirements. | WP-B5-02 |
| 3        | Design interviews, site visits, samples and tests.                                                   | WP-B5-03   |
| 4        | Set safety rules and access.                                                                         | WP-B5-04   |
| 5        | Define checkpoints and cross-domain dependencies in the work plan.                                   | WP-B5-05   |
| 6        | Approve plan and workpaper index.                                                                    | WP-B5-06   |

**AMH-REQ-023** The plan shall assign to each in-scope control and claim type at least one assessment method from the canonical method set, and INQUIRY shall not be the sole method for any claim type other than DESIGN of a purely directive control.

## B6 Evidence request and intake

Request and receive evidence under control (template WP-06).

| **Step** | **Required action**                                                                         | **Record** |
|----------|---------------------------------------------------------------------------------------------|------------|
| 1        | Issue claim-specific requests.                                                              | WP-B6-01   |
| 2        | Record evidence class (E1–E7), period, operating state, quality floor and sufficiency floor. | WP-B6-02  |
| 3        | Receive into the controlled repository.                                                     | WP-B6-03   |
| 4        | Assign evidence ID, classification and custody.                                             | WP-B6-04   |
| 5        | Validate provenance, integrity and readability.                                             | WP-B6-05   |
| 6        | Record missing, stale, restricted or substituted evidence as UNKNOWN Records (types U1–U10). | WP-B6-06  |

**AMH-REQ-024** Evidence relied on for a control result shall be held in a controlled repository with an evidence ID, source, collector, custodian, classification and integrity reference as required by AIDCF-008.

## B7 Document review (DOCUMENT_REVIEW)

| **Step** | **Required action**                                    | **Record** |
|----------|--------------------------------------------------------|------------|
| 1        | Restate the assertion under test.                      | WP-B7-01   |
| 2        | Verify ownership, approval, version and applicability. | WP-B7-02   |
| 3        | Extract criteria and assumptions.                      | WP-B7-03   |
| 4        | Compare conflicting documents.                         | WP-B7-04   |
| 5        | Link to architecture and controls.                     | WP-B7-05   |
| 6        | Record support, challenge and limits.                  | WP-B7-06   |

**Limit.** Documentary evidence (E1) supports DESIGN claims and the intent element of other claims; on its own it does not support IMPLEMENTATION, OPERATION, EFFECTIVENESS or RESILIENCE results.

## B8 Configuration review (RECONCILIATION)

| **Step** | **Required action**                                         | **Record** |
|----------|-------------------------------------------------------------|------------|
| 1        | Define target configuration and subject.                    | WP-B8-01   |
| 2        | Capture authorised source and extraction context.           | WP-B8-02   |
| 3        | Compare approved baseline, as-built and observed state.     | WP-B8-03   |
| 4        | Trace exceptions and unauthorised drift.                    | WP-B8-04   |
| 5        | Assess dependency and operating-state impact.               | WP-B8-05   |
| 6        | Record evidence and follow-up.                              | WP-B8-06   |

**Limit.** Configuration extracts are E2 evidence of state at extraction time. The extraction method, privilege used and timestamp shall be recorded; an extract supplied without that context is treated as E1 (declarative) until corroborated.

## B9 Interview method (INQUIRY)

| **Step** | **Required action**                                    | **Record** |
|----------|--------------------------------------------------------|------------|
| 1        | Define role-specific objectives.                       | WP-B9-01   |
| 2        | Prepare open, scenario and evidence-seeking questions. | WP-B9-02   |
| 3        | Explain handling and recording.                        | WP-B9-03   |
| 4        | Distinguish personal practice from approved process.   | WP-B9-04   |
| 5        | Capture contradictions and evidence references.        | WP-B9-05   |
| 6        | Confirm notes and follow-ups (template WP-07).         | WP-B9-06   |

**AMH-REQ-025** Interview statements (E6) that are decisive for a control result other than DESIGN shall be corroborated by evidence of another class before the result is recorded as CONFORMING.

The structured prompts in B9.1–B9.4 shall be adapted to the scope and corroborated. The common outputs are a confirmed interview record and a list of contradictions and evidence follow-ups. Concealment, unsafe practice or unsupported critical claims are escalated to the lead assessor.

### B9.1 Executive interviews

| **Step** | **Ask and evidence**                                    | **Record**  |
|----------|---------------------------------------------------------|-------------|
| 1        | What decision must the capability support?              | WP-B9.1-01  |
| 2        | Which Service Outcomes and tolerances are non-negotiable? | WP-B9.1-02 |
| 3        | Which assumptions depend on external parties?           | WP-B9.1-03  |
| 4        | Which changes or incidents reduced confidence?          | WP-B9.1-04  |
| 5        | Who can accept residual exposure, and under what authority? | WP-B9.1-05 |
| 6        | What events would suspend reliance on a prior decision? | WP-B9.1-06  |

### B9.2 Engineering interviews (power, thermal, physical)

| **Step** | **Ask and evidence**                                                      | **Record**  |
|----------|---------------------------------------------------------------------------|-------------|
| 1        | Which conditions and deratings govern usable capacity?                    | WP-B9.2-01  |
| 2        | Which shared dependencies remain after redundancy?                        | WP-B9.2-02  |
| 3        | How are maintenance and degraded states controlled and for how long?      | WP-B9.2-03  |
| 4        | Which tests demonstrate transfer and recovery, and at what load?          | WP-B9.2-04  |
| 5        | Where does the as-built state differ from design?                         | WP-B9.2-05  |
| 6        | Which evidence is disputed?                                               | WP-B9.2-06  |

### B9.3 Technology interviews (compute, storage, network)

| **Step** | **Ask and evidence**                                                     | **Record**  |
|----------|--------------------------------------------------------------------------|-------------|
| 1        | What topology and compatibility baseline applies?                        | WP-B9.3-01  |
| 2        | What limits usable accelerator, storage and fabric capacity?             | WP-B9.3-02  |
| 3        | Which failures cross compute, fabric and storage?                        | WP-B9.3-03  |
| 4        | How are checkpoints and restart validated?                               | WP-B9.3-04  |
| 5        | Which changes alter firmware or scheduling behaviour?                    | WP-B9.3-05  |
| 6        | Which telemetry blind spots remain?                                      | WP-B9.3-06  |

### B9.4 Operations and provider interviews

| **Step** | **Ask and evidence**                                                       | **Record**  |
|----------|----------------------------------------------------------------------------|-------------|
| 1        | Who can operate and command critical systems?                              | WP-B9.4-01  |
| 2        | How are alarms and emergency access controlled?                            | WP-B9.4-02  |
| 3        | Which provider identities and services are essential?                      | WP-B9.4-03  |
| 4        | How are incidents and their evidence preserved?                            | WP-B9.4-04  |
| 5        | Which recovery steps rely on external support?                             | WP-B9.4-05  |
| 6        | Which contractual boundaries limit evidence rights or assurance?           | WP-B9.4-06  |

## B10 Site inspection (INSPECTION, OBSERVATION)

| **Step** | **Required action**                                     | **Record** |
|----------|---------------------------------------------------------|------------|
| 1        | Complete induction and pre-brief.                       | WP-B10-01  |
| 2        | Follow approved route and access.                       | WP-B10-02  |
| 3        | Verify sampled assets and zones against the approved record. | WP-B10-03 |
| 4        | Observe condition, labels, alarms and maintenance state. | WP-B10-04 |
| 5        | Record deviations and inaccessible areas (template WP-08). | WP-B10-05 |
| 6        | Debrief immediate safety or integrity concerns.         | WP-B10-06  |

Domain-specific inspection checklists are in Part B Part III.

**AMH-REQ-026** Assessors shall not operate, switch, isolate, open or adjust any equipment during inspection unless the action is part of an approved test (B13) executed by an authorised operator.

## B11 Sampling method (SAMPLING)

| **Step** | **Required action**                                         | **Record** |
|----------|-------------------------------------------------------------|------------|
| 1        | Define the population and confirm its completeness.         | WP-B11-01  |
| 2        | Stratify by risk, site, operating state, age or topology.   | WP-B11-02  |
| 3        | Select a random, systematic, judgmental or scenario sample. | WP-B11-03  |
| 4        | Record rationale and the inference intended (template WP-09). | WP-B11-04 |
| 5        | Expand the sample after exceptions.                         | WP-B11-05  |
| 6        | State coverage and extrapolation limits.                    | WP-B11-06  |

Sampling parameters and decision rules per claim type are in Part B §II.2.

**AMH-REQ-027** A sample-based conclusion shall not be extrapolated beyond the population, strata, operating states and period from which the sample was drawn, and the population source shall itself be reconciled for completeness.

## B12 Data and telemetry analysis (ANALYSIS)

| **Step** | **Required action**                                          | **Record** |
|----------|--------------------------------------------------------------|------------|
| 1        | Define metric, source, period and resolution.                | WP-B12-01  |
| 2        | Verify clock synchronisation, gaps and collection health.    | WP-B12-02  |
| 3        | Baseline normal, peak and degraded states.                   | WP-B12-03  |
| 4        | Correlate events without premature causality.                | WP-B12-04  |
| 5        | Investigate anomalies and counter-evidence.                  | WP-B12-05  |
| 6        | Retain query, lineage and limitations.                       | WP-B12-06  |

**AMH-REQ-028** Derived evidence (E7) shall retain its source datasets, query or model version, transformation and assumptions, and shall not be rated above the quality of its weakest decisive source.

## B13 Testing and exercises (TEST, REPERFORMANCE, SCENARIO_EXERCISE)

| **Step** | **Required action**                                               | **Record** |
|----------|-------------------------------------------------------------------|------------|
| 1        | Define proposition, initial state and expected result (template WP-10). | WP-B13-01 |
| 2        | Assess safety and operational risk.                               | WP-B13-02  |
| 3        | Approve procedure, instrumentation and abort criteria.            | WP-B13-03  |
| 4        | Execute or observe the authorised test.                           | WP-B13-04  |
| 5        | Record anomalies, post-test state and restoration (template WP-11). | WP-B13-05 |
| 6        | Issue evidence and retest needs.                                  | WP-B13-06  |

**AMH-REQ-029** No test that can affect power, cooling, fire and life-safety systems, control systems or production AI workloads shall start without written approval from the capability owner and the safety authority, a defined initial state, abort criteria and a restoration plan.

**AMH-REQ-030** A test result shall support EFFECTIVENESS or RESILIENCE claims only for the load, duration, operating states and failure conditions actually tested; untested conditions within the claim scope shall be recorded as UNKNOWN Records (type U5, coverage gap).

## B14 Rules of engagement

| **Step** | **Required action**                                     | **Record** |
|----------|---------------------------------------------------------|------------|
| 1        | Classify method risk and required permits.              | WP-B14-01  |
| 2        | Name change, safety and stop authorities.               | WP-B14-02  |
| 3        | Define communications, monitoring and rollback.         | WP-B14-03  |
| 4        | Protect credentials and sensitive infrastructure paths. | WP-B14-04  |
| 5        | Record deviations, incidents and near misses.           | WP-B14-05  |
| 6        | Close access and restore the environment.               | WP-B14-06  |

**AMH-REQ-031** The rules of engagement shall give the safety authority and the capability owner the right to stop any assessment activity at any time, and a stop shall be recorded with its effect on the affected results.

# C Evaluation, decision and reassessment

## C1 Control assessment

Evaluate each applicable control for each assigned claim type.

| **Step** | **Required action**                                                                                    | **Record** |
|----------|--------------------------------------------------------------------------------------------------------|------------|
| 1        | Restate the control requirement and the claim type being assessed.                                     | WP-C1-01   |
| 2        | Confirm subject, operating states, period and boundary.                                                | WP-C1-02   |
| 3        | Review evidence quality and sufficiency against the registry `evidenceProfile`.                        | WP-C1-03   |
| 4        | Perform the registry `assessmentProcedure` using the generic claim-type protocol (Part B §II.3–II.7).  | WP-C1-04   |
| 5        | Record supporting, challenging and qualifying evidence, exceptions and UNKNOWN.                        | WP-C1-05   |
| 6        | Assign the control result against each `assessmentCriteria` item, with rationale and confidence (template WP-12). | WP-C1-06 |

Control results (canonical, per control, per claim type, per scope):

| **Result**      | **Meaning**                                                                                         | **Score value**                                              |
|-----------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| CONFORMING      | All assessment criteria met for the claim type, with evidence at or above the evidence-profile floor. | 100                                                        |
| PARTIAL         | Some criteria met; specific deficiencies recorded as Findings.                                       | 50                                                           |
| NONCONFORMING   | Criteria materially not met, or a safeguard demonstrated ineffective.                                | 0                                                            |
| UNKNOWN         | Result cannot be determined (evidence below floor, conflict, inaccessible and similar).             | No value; excluded from the mean; counted in coverage and the UNKNOWN register |
| NOT_APPLICABLE  | Approved non-applicability with rationale and approver.                                             | Excluded                                                     |
| NOT_ASSESSED    | In scope but not yet assessed.                                                                       | Excluded; counted as a coverage gap                          |

**AMH-REQ-032** A control result shall be determined against the control's `assessmentCriteria` in the AIDCF-007A registry; CONFORMING requires every criterion to be met for the claim type with evidence at or above the `evidenceProfile` quality and sufficiency floors.

**AMH-REQ-033** Where evidence is below the evidence-profile floor and no criterion is demonstrated unmet, the result shall be UNKNOWN, not PARTIAL or CONFORMING; insufficient evidence shall never be converted into a reduced score.

**AMH-REQ-034** Where evidence demonstrates that a criterion is materially not met, or a safeguard has been shown ineffective, the result shall be NONCONFORMING regardless of the quality of evidence for other criteria.

## C2 Failure scenario analysis

Trace credible adversity to capability consequence (template WP-13).

| **Step** | **Required action**                                                          | **Record** |
|----------|------------------------------------------------------------------------------|------------|
| 1        | Select bottom-up, top-down, path, state or capability method.                | WP-C2-01   |
| 2        | Separate threat or hazard, initiating event, cause, failure mode, effect and consequence (AIDCF-004). | WP-C2-02 |
| 3        | Trace dependencies and fault domains.                                        | WP-C2-03   |
| 4        | Evaluate safeguards and the dependencies of the safeguards themselves.       | WP-C2-04   |
| 5        | Determine residual state and recovery path.                                  | WP-C2-05   |
| 6        | Record evidence, UNKNOWN and gate effects.                                   | WP-C2-06   |

**AMH-REQ-035** Every in-scope Service Outcome shall be traced through at least one failure scenario per material fault domain, including scenarios that start in another domain and propagate across the power, thermal, control-system, compute, storage and network boundaries where those dependencies exist.

## C3 Critical gate evaluation

Apply non-compensating gate logic (template WP-14).

| **Step** | **Required action**                                                                                     | **Record** |
|----------|---------------------------------------------------------------------------------------------------------|------------|
| 1        | Confirm gate applicability and the gate criteria (AIDCF-010).                                           | WP-C3-01   |
| 2        | Collect the results of every in-scope CRITICAL and SUPPORTING control mapped to the gate.               | WP-C3-02   |
| 3        | Verify mandatory evidence classes and the gate evidence floor (AIDCF-008 Part XIII).                    | WP-C3-03   |
| 4        | Evaluate all relevant operating states and scenarios.                                                   | WP-C3-04   |
| 5        | Apply the gate roll-up rule and assign PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED.                | WP-C3-05   |
| 6        | Determine the decision ceiling (AIDCF-010) and closure requirements.                                    | WP-C3-06   |
| 7        | Obtain technical and independent review.                                                                | WP-C3-07   |

Gate roll-up rule (canonical; specified in AIDCF-010 Part VIII and expressed as Part B DT-15). For a gate in scope:

1. **FAIL** if any in-scope CRITICAL control is NONCONFORMING or PARTIAL, or a gate criterion is demonstrated not met;
2. else **UNKNOWN** if any in-scope CRITICAL control is UNKNOWN or NOT_ASSESSED, or gate evidence is below the floor, or a US4 UNKNOWN Record is attached;
3. else **PASS** if all CRITICAL controls are CONFORMING at the required claim type, all gate criteria are met with evidence at or above the floor, and every SUPPORTING control that is NONCONFORMING has a documented gate-level evaluation concluding no defeat.

APPROVED_NA is used only with an approved boundary rationale. NOT_ASSESSED is used where the gate is in scope but has not been evaluated. PARTIAL never yields PASS. There is no conditional gate result; conditions are expressed only at decision level. Gates CG-11 (Evidence sufficiency) and CG-12 (Critical UNKNOWN) are evaluated across all controls and are not mapped per control.

**AMH-REQ-036** Gate Results shall be determined only by the canonical roll-up rule and the gate criteria in AIDCF-010, using the control-to-gate mappings in the AIDCF-007A registry; a gate shall not be assigned any result other than PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED.

**AMH-REQ-037** Where a SUPPORTING control mapped to a gate is NONCONFORMING, the lead assessor shall record a gate-level evaluation stating whether the deficiency defeats the gate scope, and the gate shall not be PASS until that evaluation is technically approved.

## C4 Findings and causes

Write evidence-linked and outcome-focused Findings (template WP-15).

| **Step** | **Required action**                                       | **Record** |
|----------|-----------------------------------------------------------|------------|
| 1        | State the factual condition and evidence.                 | WP-C4-01   |
| 2        | Map the criterion and affected Service Outcome.           | WP-C4-02   |
| 3        | Identify immediate and systemic causes where evidenced.   | WP-C4-03   |
| 4        | Describe consequence and residual exposure.               | WP-C4-04   |
| 5        | Classify the Finding (AIDCF-012 Part IX) and record confidence. | WP-C4-05 |
| 6        | Define action and validation requirement.                 | WP-C4-06   |

**AMH-REQ-038** Every PARTIAL or NONCONFORMING control result shall be supported by at least one Finding that states criterion, condition, evidence, consequence for the affected Service Outcome and closure evidence required; a cause shall be stated only where evidenced or explicitly labelled as analysis.

## C5 UNKNOWN and limitations

Record, classify and apply the effect of every UNKNOWN (templates WP-16 and WP-17).

| **Step** | **Required action**                                                                     | **Record** |
|----------|-----------------------------------------------------------------------------------------|------------|
| 1        | Classify the UNKNOWN type (U1–U10, AIDCF-008 §35).                                      | WP-C5-01   |
| 2        | Identify subject and missing attribute.                                                 | WP-C5-02   |
| 3        | Classify severity US1–US5 using the top-down test below.                                | WP-C5-03   |
| 4        | Define evidence needed to resolve and owner.                                            | WP-C5-04   |
| 5        | Apply the decision effect (gate result, ceiling, condition or confidence ceiling).      | WP-C5-05   |
| 6        | Track resolution and history.                                                           | WP-C5-06   |

UNKNOWN severity (apply the first test that is satisfied, from top to bottom):

| **Code** | **Name**  | **Test**                                                                                  | **Decision effect**                                                          |
|----------|-----------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| US5      | Systemic  | Affects the boundary, a Capability Instance or Service Outcome definition, or two or more gates. | Decision no higher than INCONCLUSIVE.                                  |
| US4      | Critical  | Affects a gate-critical control or a gate criterion (CG-12 trigger).                      | Gate result UNKNOWN; decision no higher than LIMITED, or the gate's UNKNOWN ceiling in AIDCF-010 if lower. |
| US3      | Material  | Could change a control result or a decision condition but affects no gate.                | Decision no higher than CONDITIONALLY_ASSURED; condition recorded.           |
| US2      | Moderate  | Affects confidence but not any result.                                                    | Confidence ceiling CONF-2 for the affected claims.                           |
| US1      | Low       | No plausible effect on any result or condition.                                           | Record only.                                                                 |

**AMH-REQ-039** Every UNKNOWN Record shall carry a type (U1–U10), a severity (US1–US5) determined by the top-down test, the evidence needed to resolve it, an owner and its decision effect; severity shall not be lowered without new evidence and technical review.

**AMH-REQ-040** A limitation (template WP-17) that restricts scope, method or evidence access shall be linked to every result and gate it affects and shall be disclosed in the Assurance Decision.

## C6 Independent review

Challenge the decision package before decision (template WP-18).

| **Step** | **Required action**                                                  | **Record** |
|----------|----------------------------------------------------------------------|------------|
| 1        | Verify scope, criteria and artifact versions.                        | WP-C6-01   |
| 2        | Sample assertions back to evidence.                                  | WP-C6-02   |
| 3        | Challenge omitted and contradictory evidence.                        | WP-C6-03   |
| 4        | Review scenario and gate completeness and the roll-up applied.       | WP-C6-04   |
| 5        | Test the proposed wording against the decision state and AIDCF-012 controlled wording. | WP-C6-05 |
| 6        | Record resolution and either approval to proceed or return.          | WP-C6-06   |

**AMH-REQ-041** Every Assurance Decision other than one issued at AL0 shall be preceded by an independent review that covers, at minimum, every gate that is FAIL or UNKNOWN, every US4 and US5 UNKNOWN Record and the proposed decision wording.

## C7 Assurance decision

Select and record the decision state (template WP-19).

| **Step** | **Required action**                                                                  | **Record** |
|----------|--------------------------------------------------------------------------------------|------------|
| 1        | Restate the decision question and subject.                                           | WP-C7-01   |
| 2        | Summarise evidence, coverage and limitations.                                        | WP-C7-02   |
| 3        | Derive the ceiling per Service Outcome in AIDCF-010 order: gates, UNKNOWN severity, coverage, bands, conditions and confidence. | WP-C7-03   |
| 4        | Select the decision state.                                                           | WP-C7-04   |
| 5        | Set conditions, validity period and Reassessment Triggers.                           | WP-C7-05   |
| 6        | Approve the immutable decision package and set the decision lifecycle state.         | WP-C7-06   |

The decision is derived per Service Outcome in the fixed AIDCF-010 precedence order — gates → UNKNOWN severity → coverage → bands → conditions and confidence — each step only lowering the ceiling (Part B DT-19). Ceilings are ranked REASONABLY_ASSURED > CONDITIONALLY_ASSURED > LIMITED > INCONCLUSIVE > NOT_ASSURED. In summary: gate FAIL and UNKNOWN ceilings are gate-specific (AIDCF-010 Part VIII); US5 → ≤ INCONCLUSIVE, US4 → ≤ LIMITED, US3 → ≤ CONDITIONALLY_ASSURED; capability coverage below 50% → ≤ INCONCLUSIVE and below 80% → ≤ LIMITED; lowest reported band B3 → ≤ CONDITIONALLY_ASSURED, B2 → ≤ LIMITED, B1 → ≤ NOT_ASSURED; an open Significant weakness or decision confidence below CONF-3 → ≤ CONDITIONALLY_ASSURED, and confidence below CONF-2 → ≤ LIMITED. The decision authority may select a state lower than the recommendation (with rationale) but never higher.

Decision states (canonical): REASONABLY_ASSURED, CONDITIONALLY_ASSURED, LIMITED, NOT_ASSURED, INCONCLUSIVE. Decision lifecycle: DRAFT, RECOMMENDED, APPROVED, ACTIVE, SUSPENDED, WITHDRAWN, SUPERSEDED, EXPIRED. Where no decision is issued (for example an AL0 discovery engagement, or an assessment stopped before SG6) no decision state is recorded; "not assessed" is not a decision state. The decision ceiling rules are in AIDCF-010; the authoritative controlled wording for each decision state is in AIDCF-012 Part V.

**AMH-REQ-042** The Assurance Decision shall use exactly one canonical decision state, shall not exceed the lowest ceiling imposed by any Gate Result or UNKNOWN Record under AIDCF-010, and shall be expressed using the controlled wording in AIDCF-012 Part V.

**AMH-REQ-043** Every CONDITIONALLY_ASSURED decision shall list each condition with an owner, a due date or triggering event, the evidence that will demonstrate it and the effect if it is not met.

## C8 Reporting and closeout

| **Step** | **Required action**                                                                   | **Record** |
|----------|---------------------------------------------------------------------------------------|------------|
| 1        | Prepare the report classes required by the charter (AIDCF-012 Part III).              | WP-C8-01   |
| 2        | Place scope, coverage, Gate Results and UNKNOWN beside outcomes.                      | WP-C8-02   |
| 3        | Protect sensitive evidence and infrastructure detail.                                 | WP-C8-03   |
| 4        | Reconcile references and versions to the approved decision snapshot.                  | WP-C8-04   |
| 5        | Assign actions and validation.                                                        | WP-C8-05   |
| 6        | Archive and close (SG7).                                                              | WP-C8-06   |

**AMH-REQ-044** Reports and assurance statements shall be prepared only from the approved decision snapshot and shall conform to AIDCF-012.

## C9 Reassessment

| **Step** | **Required action**                                                          | **Record** |
|----------|------------------------------------------------------------------------------|------------|
| 1        | Monitor changes, incidents, evidence expiry and Gate Result changes.         | WP-C9-01   |
| 2        | Map each trigger to affected assertions, controls and gates.                 | WP-C9-02   |
| 3        | Suspend invalidated claims (decision lifecycle SUSPENDED where material).    | WP-C9-03   |
| 4        | Perform delta or full reassessment.                                          | WP-C9-04   |
| 5        | Independently review material updates.                                       | WP-C9-05   |
| 6        | Supersede without erasing history (template WP-20).                          | WP-C9-06   |

**AMH-REQ-045** Every ACTIVE Assurance Decision shall carry Reassessment Triggers derived from the `reassessmentTriggers` of the decisive controls' evidence profiles; when a trigger fires, the affected claims shall be re-evaluated and, where the trigger is material, the decision shall be set to SUSPENDED until re-evaluation is complete.

**AMH-REQ-046** A reassessment shall produce a new decision record that SUPERSEDES the prior one; the prior record shall be retained unchanged.

# D Domain playbooks

Each domain playbook gives the assessment focus, the families and controls in the domain, baseline evidence, domain-specific emphasis and the specialist competence required. Control-specific objectives, criteria, procedures and evidence profiles are carried in the AIDCF-007A registry v1.1; engineering guidance is in the domain guide named in each playbook. The principal gates informed by each domain are indicative only; gates are mapped control by control, and the authoritative control-to-gate mapping (CRITICAL or SUPPORTING) is the `gateMappings` field of each control in the registry.

The following planning dimensions apply to every domain playbook:

| **Planning dimension** | **Requirement**                                                                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Subject                | Map in-scope controls to the Capability Instance, Service Outcomes and Required Functions.                               |
| Boundary               | Identify assets, interfaces, providers and exclusions within the domain.                                                 |
| States                 | Assess NORMAL and the material MAINTENANCE, DEGRADED, EMERGENCY, RECOVERY and TRANSITION states for each claim type.     |
| Claim types            | Assess each control for the claim types assigned in B4; record results per claim type.                                   |
| Methods                | Use the methods named in the registry `assessmentMethods`; apply safe-testing rules (B13, B14).                          |
| Scenarios              | Trace local, cross-domain, common-mode and recovery paths (C2).                                                          |
| Decision               | Preserve UNKNOWN; apply the gate roll-up rule and non-compensation.                                                      |

**AMH-REQ-047** Every domain conclusion shall be technically reviewed by a person with the specialist competence stated in the domain playbook, and the family-level results shall be reported with coverage as defined in AIDCF-010.

## D-GOV Governance, Accountability and Assurance Direction

**Domain guide:** AIDCF-018-GOV (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-13, CG-14.

**Assessment focus.** Whether accountable authority, decision rights, policy baselines and assurance direction exist and operate for the Capability Instance, so that every critical function and dependency has an owner who can act and accept risk.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| GOV-01 | Governance architecture | MCF-GOV-001 to MCF-GOV-004 | Governance Charter; Decision Rights; Committee Oversight; Methodology Ownership |
| GOV-02 | Accountability and responsibility | MCF-GOV-005 to MCF-GOV-008 | RACI and Role Ownership; Critical Function Accountability; Risk Acceptance Authority; Evidence Custody |
| GOV-03 | Policy and standards management | MCF-GOV-009 to MCF-GOV-012 | Policy Hierarchy; Technical Standard Baselines; Exception Governance; Document Lifecycle |
| GOV-04 | Risk and assurance governance | MCF-GOV-013 to MCF-GOV-016 | Assurance Plan; Risk Appetite Linkage; Critical Gate Governance; Independent Review |
| GOV-05 | Stakeholder and regulatory interface | MCF-GOV-017 to MCF-GOV-020 | Stakeholder Obligations; Regulatory Monitoring; Customer Commitments; External Reporting |
| GOV-06 | Ethics, impartiality and competence | MCF-GOV-021 to MCF-GOV-024 | Conflict Management; Assessor Independence; Competence Management; Appeal and Challenge |

**Baseline evidence.** Governance charters, terms of reference, delegations of authority, RACI, policy and standards registers, exception registers, committee minutes, risk-acceptance records, independent review records.

**Domain-specific emphasis.**

- Test that decision rights operate in EMERGENCY and RECOVERY states (who can authorise load shedding, emergency change or customer communication out of hours), not only in NORMAL governance cycles.

- Reconcile the RACI to named people and to the dependency baseline from B3: an owner per critical function and per external dependency.

- Sample exceptions and risk acceptances for authority, expiry and compensating safeguards; expired exceptions still in force are Findings.

- For assessor independence (GOV-06) apply AIDCF-011 Part VIII; the assessed organisation cannot certify its own independence safeguards.

**Specialist competence.** Governance, risk and assurance; knowledge of the assessed organisation's legal and contractual obligations.

## D-CAP AI Capability, Service Outcome and Demand Management

**Domain guide:** AIDCF-018-CAP (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-01, CG-02.

**Assessment focus.** Whether the Capability Instance, its Service Outcomes, tolerances, criticality, demand and operating envelope are defined, owned, current and linked to the architecture, so that every other domain has a stable assessment target.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| CAP-01 | Capability inventory | MCF-CAP-001 to MCF-CAP-004 | Capability Register; Capability Ownership; Lifecycle Status; Architecture Linkage |
| CAP-02 | Service outcome definition | MCF-CAP-005 to MCF-CAP-008 | Availability Outcomes; Performance Outcomes; Integrity Outcomes; Recovery Outcomes |
| CAP-03 | Criticality and materiality | MCF-CAP-009 to MCF-CAP-012 | Criticality Criteria; Impact Tolerance; Stakeholder Consequence; Priority Classification |
| CAP-04 | Demand and growth modelling | MCF-CAP-013 to MCF-CAP-016 | Current Demand Baseline; Peak and Transient Demand; Growth Forecast; Scenario Demand |
| CAP-05 | Operating envelope | MCF-CAP-017 to MCF-CAP-020 | Load Envelope; Environmental Envelope; Duration Limits; State-Specific Limits |
| CAP-06 | Capability lifecycle and change | MCF-CAP-021 to MCF-CAP-024 | Design-to-Operation Traceability; Commissioning Acceptance; Material Change Impact; Retirement Control |

**Baseline evidence.** Capability register, service outcome definitions and tolerances, criticality and impact-tolerance analysis, demand baselines and forecasts, operating-envelope records, commissioning acceptance records, change-impact assessments.

**Domain-specific emphasis.**

- Express each Service Outcome with a measurable tolerance (for example availability, sustained accelerator throughput, checkpoint recovery point and recovery time) and the operating states in which it applies.

- Reconcile demand to measured load: rack and row power at peak training load, transient load steps from synchronised accelerator phases, and the liquid/air heat split.

- Check that the operating envelope records duration limits for DEGRADED and MAINTENANCE states rather than only NORMAL capacity.

- An undefined or unowned outcome is a US5 UNKNOWN and caps the decision at INCONCLUSIVE (CG-01).

**Specialist competence.** Capacity planning for AI/HPC; service management; ability to read power, thermal and compute capacity models.

## D-DEP Dependency, Concentration and External Reliance Management

**Domain guide:** AIDCF-018-DEP (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-03, CG-02, CG-09.

**Assessment focus.** Whether internal, external, shared and common-mode dependencies of the Required Functions are identified, owned, monitored and bounded, including recovery dependencies and concentration on single providers, routes, controllers or people.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| DEP-01 | Dependency discovery | MCF-DEP-001 to MCF-DEP-004 | Asset-to-Function Mapping; Upstream Dependency Mapping; Downstream Consequence Mapping; Recovery Dependency Mapping |
| DEP-02 | Shared and common-mode dependencies | MCF-DEP-005 to MCF-DEP-008 | Shared Source Analysis; Common Controller Analysis; Shared Route Analysis; Shared Human Dependency Analysis |
| DEP-03 | External providers and utilities | MCF-DEP-009 to MCF-DEP-012 | Utility Dependency; Telecom Dependency; OEM Dependency; Cloud and Service Dependency |
| DEP-04 | Concentration and substitutability | MCF-DEP-013 to MCF-DEP-016 | Capacity Concentration; Supplier Concentration; Knowledge Concentration; Substitution Readiness |
| DEP-05 | Boundary and interface control | MCF-DEP-017 to MCF-DEP-020 | Assessment Boundary; Provider Boundary; Tenant Boundary; Cross-Boundary Enforcement |
| DEP-06 | Dependency monitoring and review | MCF-DEP-021 to MCF-DEP-024 | Dependency Health Indicators; Provider Performance; Change Detection; Periodic Revalidation |

**Baseline evidence.** Dependency graphs, asset-to-function mappings, utility and telecom agreements, route diagrams, OEM and cloud service dependencies, concentration analyses, boundary and interface records, provider performance records.

**Domain-specific emphasis.**

- Trace each Required Function to its upstream sources and to its recovery dependencies (for example generator fuel contracts, OEM field service, DNS, time, identity and licence servers needed to restart).

- Look for common-mode dependencies hidden by nominal redundancy: shared controller, shared conduit or duct bank, shared firmware image, shared single person with authority.

- Validate the boundary against contracts: which party operates which interface and who holds evidence rights.

- A material dependency that cannot be evidenced is a U10 UNKNOWN; its severity is US4 where it touches a gate-critical control.

**Specialist competence.** Systems and dependency analysis; contract and provider management; telecom and utility interfaces.

## D-PHY Physical Site, Building and Security Infrastructure

**Domain guide:** AIDCF-018-PHY (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-04, CG-02.

**Assessment focus.** Whether the site, building, structure, zoning, access control, asset custody and fire and life-safety interfaces protect the Required Functions and people across operating states.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| PHY-01 | Site and location resilience | MCF-PHY-001 to MCF-PHY-004 | Site Hazard Assessment; External Exposure; Access and Logistics; Adjacent Risk |
| PHY-02 | Building and structural integrity | MCF-PHY-005 to MCF-PHY-008 | Structural Capacity; Rack Loading; Anchorage and Vibration; Building Envelope |
| PHY-03 | Physical zoning and segregation | MCF-PHY-009 to MCF-PHY-012 | Security Zones; Fire Zones; Water Zones; Tenant Segregation |
| PHY-04 | Access and surveillance | MCF-PHY-013 to MCF-PHY-016 | Identity-Based Access; Visitor Control; Surveillance Coverage; Alarm Response |
| PHY-05 | Asset movement and custody | MCF-PHY-017 to MCF-PHY-020 | Delivery Controls; Equipment Movement; Media Custody; Decommissioning Custody |
| PHY-06 | Fire, life safety and emergency interfaces | MCF-PHY-021 to MCF-PHY-024 | Fire Detection; Suppression Interfaces; Egress and Emergency Access; Emergency Shutdown Governance |

**Baseline evidence.** Site hazard studies, structural and floor-loading calculations, drawings, zoning plans, access-control configurations and logs, surveillance coverage plans, custody records, fire-strategy documents, fire-system inspection and test records.

**Domain-specific emphasis.**

- Verify floor and rack loading for high-density AI racks, including liquid-filled manifolds and coolant distribution units, against structural calculations by a competent structural engineer.

- Sample access events for critical spaces (electrical rooms, battery rooms, meet-me rooms, control rooms) and reconcile against authorised lists.

- Check interfaces between fire detection/suppression and the power, thermal and control systems (for example cause-and-effect matrices, emergency power off, damper and pump interlocks).

- Fire and life-safety tests are witnessed or reviewed from authorised records; assessors never initiate them.

**Specialist competence.** Physical security; structural engineering (licensed where required); fire engineering and life safety.

## D-POW Electrical Power Infrastructure and Energy Continuity

**Domain guide:** AIDCF-018-POW (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-05, CG-04, CG-07, CG-10.

**Assessment focus.** Whether utility supply, generation, UPS and energy storage, distribution, protection, power quality and electrical recovery deliver the power-related Service Outcomes across all declared operating states, including AI load transients.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| POW-01 | Utility and grid interface | MCF-POW-001 to MCF-POW-004 | Utility Capacity; Grid Quality; Connection Reliability; Utility Contingency |
| POW-02 | Generation and fuel | MCF-POW-005 to MCF-POW-008 | Generator Capacity; Start Reliability; Fuel Autonomy; Fuel Replenishment |
| POW-03 | UPS and energy storage | MCF-POW-009 to MCF-POW-012 | UPS Topology; Battery Condition; Runtime and Derating; Bypass Exposure |
| POW-04 | Distribution and protection | MCF-POW-013 to MCF-POW-016 | Switchgear Integrity; Selective Coordination; Busway and PDU Capacity; Earthing and Bonding |
| POW-05 | Power quality and transient response | MCF-POW-017 to MCF-POW-020 | Voltage Quality; Harmonics; Transient Ride-Through; Load-Step Response |
| POW-06 | Electrical monitoring, maintenance and recovery | MCF-POW-021 to MCF-POW-024 | EPMS Coverage; Preventive Maintenance; Switching Procedures; Black-Start and Restoration |

**Baseline evidence.** Single-line diagrams, short-circuit, protection-coordination and arc-flash studies, protection relay settings, UPS and BESS records, generator and fuel records, EPMS telemetry, power-quality recordings, maintenance and switching procedures, integrated systems test records.

**Domain-specific emphasis.**

- Reconcile the single-line diagram to the as-built installation and to EPMS points; unreconciled breakers or bypass paths are IMPLEMENTATION Findings.

- Evaluate behaviour under synchronised accelerator load steps and power swings: UPS and generator transient response, protection nuisance-trip margins and any rack-level energy buffering.

- Assess concurrent-maintenance states: the residual topology when one path or one generator is out of service, and the duration it is tolerated.

- Electrical tests (transfer, load-bank, black-start) are executed only by authorised persons under switching programmes; arc-flash and shock exposure is a CG-04 matter.

**Specialist competence.** Electrical power engineering for critical facilities; protection; power quality; authorised-person competence for switching where witnessed.

## D-THM Cooling, Thermal and Fluid Infrastructure

**Domain guide:** AIDCF-018-THM (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-06, CG-04, CG-07, CG-10.

**Assessment focus.** Whether air and liquid heat-removal paths, heat rejection, water supply, fluid quality, leak management and thermal controls remove the declared heat load across operating states, including transients and partial failures.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| THM-01 | Thermal architecture and capacity | MCF-THM-001 to MCF-THM-004 | Heat-Load Model; Design Capacity; Resilient Capacity; Seasonal Derating |
| THM-02 | Air cooling systems | MCF-THM-005 to MCF-THM-008 | Airflow Management; Containment; CRAH and In-Row Capacity; Air-Side Monitoring |
| THM-03 | Liquid cooling systems | MCF-THM-009 to MCF-THM-012 | Direct-to-Chip Architecture; CDU Capacity; Secondary Loop Integrity; Quick-Disconnect Management |
| THM-04 | Heat rejection and water systems | MCF-THM-013 to MCF-THM-016 | Chiller Capacity; Cooling Tower or Dry Cooler; Water Continuity; Heat-Rejection Dependency |
| THM-05 | Fluid quality and leak management | MCF-THM-017 to MCF-THM-020 | Coolant Compatibility; Water Quality; Leak Detection; Isolation and Drainage |
| THM-06 | Thermal control, maintenance and recovery | MCF-THM-021 to MCF-THM-024 | Control Stability; Sensor Trust; Maintenance States; Thermal Recovery |

**Baseline evidence.** Heat-load models, P&IDs, CDU and secondary-loop design records, chiller and heat-rejection capacity data, BMS trends, flow, pressure and temperature telemetry, coolant chemistry records, leak-detection layouts and tests, failover and recovery test records.

**Domain-specific emphasis.**

- Separate the liquid-cooled and air-cooled heat fractions and test each path's capacity at the design ambient condition and with one unit out of service.

- Examine thermal ride-through: the time from loss of cooling (or loss of power to pumps) to accelerator throttling or shutdown, against the time to restore flow.

- Check fluid quality and compatibility for the secondary loop (wetted materials, filtration, inhibitor and biological control) and quick-disconnect handling.

- Leak and pressure tests and pump or valve failover are executed only under authorised method statements.

**Specialist competence.** Mechanical engineering for data-centre cooling; liquid cooling and fluid chemistry; controls engineering.

## D-ENV Environmental and Resource Performance

**Domain guide:** AIDCF-018-ENV (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-04, CG-02.

**Assessment focus.** Whether environmental operating conditions, energy, water and carbon performance, hazardous materials and climate adaptation are measured, controlled and reported accurately for the Capability Instance.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| ENV-01 | Environmental operating conditions | MCF-ENV-001 to MCF-ENV-004 | Temperature Control; Humidity Control; Particulate and Corrosion; Vibration and Acoustic Conditions |
| ENV-02 | Energy performance | MCF-ENV-005 to MCF-ENV-008 | PUE Measurement; Energy Allocation; Efficiency Under Load; Resilience-Efficiency Trade-Off |
| ENV-03 | Water performance | MCF-ENV-009 to MCF-ENV-012 | Water Source and Quality; WUE Measurement; Water Scarcity Response; Discharge Control |
| ENV-04 | Carbon and resource reporting | MCF-ENV-013 to MCF-ENV-016 | Carbon Accounting Boundary; Energy Attribute Evidence; Embodied Resource Data; Reporting Traceability |
| ENV-05 | Hazardous materials and waste | MCF-ENV-017 to MCF-ENV-020 | Battery Materials; Refrigerants and Coolants; Fuel and Suppressant Handling; Hardware and Media Waste |
| ENV-06 | Climate adaptation and resource continuity | MCF-ENV-021 to MCF-ENV-024 | Heatwave Readiness; Drought Readiness; Flood Adaptation; Long-Term Resource Constraints |

**Baseline evidence.** Environmental telemetry, metering hierarchies and calibration records, energy and water accounting, carbon accounting boundary statements, hazardous-material inventories, permits, climate-risk assessments.

**Domain-specific emphasis.**

- Check that environmental envelopes are taken from an attributed source (for example the ASHRAE TC 9.9 thermal guidelines or the equipment manufacturer's specification) and stated as capability-profile parameters.

- Verify metering boundaries for efficiency metrics (for example PUE and WUE as defined in ISO/IEC 30134) before relying on reported values.

- Battery, refrigerant, coolant, fuel and suppressant hazards link to CG-04 and are assessed with PHY, POW and THM controls.

- Resource-efficiency changes are evaluated for their effect on resilience (ENV-02 resilience-efficiency trade-off).

**Specialist competence.** Environmental and energy management; metering; hazardous materials; climate risk.

## D-CMP AI Compute Infrastructure

**Domain guide:** AIDCF-018-CMP (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-08, CG-09, CG-10.

**Assessment focus.** Whether accelerator compute is architected, configured, scheduled, observed and recovered so that usable capacity and functional integrity meet the Service Outcomes, including behaviour of scale-up domains under component failure.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| CMP-01 | Compute architecture and configuration | MCF-CMP-001 to MCF-CMP-004 | Accelerator Architecture; Node Configuration; Rack-Scale Composition; Approved Baseline |
| CMP-02 | Cluster and scale-up domains | MCF-CMP-005 to MCF-CMP-008 | Cluster Topology; Scale-Up Domain Integrity; Partitioning; Fault-Domain Design |
| CMP-03 | Capacity, scheduling and utilisation | MCF-CMP-009 to MCF-CMP-012 | Usable Accelerator Capacity; Scheduler Controls; Resource Reservation; Contention Management |
| CMP-04 | Firmware, driver and compatibility | MCF-CMP-013 to MCF-CMP-016 | Firmware Baseline; Driver Compatibility; Upgrade Testing; Rollback Readiness |
| CMP-05 | Compute health and observability | MCF-CMP-017 to MCF-CMP-020 | GPU Telemetry; Node Health; Error and Degradation Detection; Performance Baselines |
| CMP-06 | Compute lifecycle and recovery | MCF-CMP-021 to MCF-CMP-024 | Provisioning; Spares and RMA; Node Rebuild; Secure Retirement |

**Baseline evidence.** Cluster and rack-scale architecture records, node and firmware baselines, scheduler configuration, accelerator and node telemetry, error and degradation logs, burn-in and acceptance results, spares and RMA records, rebuild procedures.

**Domain-specific emphasis.**

- Distinguish installed from usable accelerator capacity: nodes drained, quarantined, failed or awaiting RMA, and the effect of a single failure on a scale-up domain.

- Reconcile firmware and driver versions across the fleet to the approved baseline; mixed baselines inside one job domain are a functional-integrity risk.

- Use error telemetry (for example correctable and uncorrectable memory errors, link errors, thermal throttling events) as OPERATION evidence over a representative period.

- Node rebuild and job restart tests are performed on non-production or drained capacity unless the owner authorises otherwise.

**Specialist competence.** AI/HPC systems architecture; accelerator platforms; cluster scheduling; firmware lifecycle.

## D-STO AI Storage and Data Infrastructure

**Domain guide:** AIDCF-018-STO (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-08, CG-10.

**Assessment focus.** Whether storage tiers for training data, checkpoints, models and archives provide the performance, capacity, integrity, protection and recovery the Service Outcomes require.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| STO-01 | Storage architecture and tiering | MCF-STO-001 to MCF-STO-004 | Training Data Tier; Checkpoint Tier; Model and Artifact Tier; Archive Tier |
| STO-02 | Performance and capacity | MCF-STO-005 to MCF-STO-008 | Throughput and IOPS; Metadata Performance; Capacity Headroom; Burst Handling |
| STO-03 | Integrity and consistency | MCF-STO-009 to MCF-STO-012 | Data Integrity; Metadata Integrity; Checksum and Scrubbing; Configuration Consistency |
| STO-04 | Protection and replication | MCF-STO-013 to MCF-STO-016 | Snapshot Protection; Replication; Erasure Coding; Immutable Recovery Copy |
| STO-05 | Checkpoint and recovery services | MCF-STO-017 to MCF-STO-020 | Checkpoint Durability; Restart Readiness; Storage Recovery Sequencing; Recovery Validation |
| STO-06 | Storage monitoring and lifecycle | MCF-STO-021 to MCF-STO-024 | Storage Telemetry; Capacity Forecasting; Media Health; Secure Sanitisation |

**Baseline evidence.** Storage architecture and tiering records, performance baselines, capacity forecasts, integrity and scrubbing reports, snapshot and replication configurations, immutable-copy records, checkpoint and restore test records, media-sanitisation records.

**Domain-specific emphasis.**

- Test checkpoint write and restore against the recovery-point and recovery-time tolerances at representative scale, not single-file restores.

- Verify that at least one recovery copy is protected from the same administrative credentials and failure domain as production.

- Check metadata-service capacity and failover separately from data throughput.

- Restore tests run into isolated targets; overwriting production data is never part of an assessment test.

**Specialist competence.** Storage systems for AI/HPC; data protection; parallel and object file systems.

## D-NET AI Network and Interconnect Architecture

**Domain guide:** AIDCF-018-NET (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-08, CG-09, CG-10.

**Assessment focus.** Whether scale-up and scale-out fabrics, storage and front-end networks, management and out-of-band networks, physical connectivity and network control deliver the required performance, isolation and recovery.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| NET-01 | Scale-up and scale-out fabrics | MCF-NET-001 to MCF-NET-004 | Fabric Topology; Path Diversity; Oversubscription; Fabric Fault-Domain Design |
| NET-02 | Performance and congestion control | MCF-NET-005 to MCF-NET-008 | Latency Baseline; Loss and Retransmission; Congestion Control; Collective Communication Performance |
| NET-03 | Storage and service networks | MCF-NET-009 to MCF-NET-012 | Storage Fabric; Frontend Network; Service Gateways; Traffic Isolation |
| NET-04 | Management and out-of-band networks | MCF-NET-013 to MCF-NET-016 | Management Separation; Console Access; OOB Resilience; Break-Glass Access |
| NET-05 | Physical connectivity and optics | MCF-NET-017 to MCF-NET-020 | Cabling Standards; Optics Compatibility; Cross-Connect Control; Path Documentation |
| NET-06 | Network control and observability | MCF-NET-021 to MCF-NET-024 | Controller Resilience; Configuration Management; Flow Telemetry; Time and Core Services |

**Baseline evidence.** Fabric topology and design records, path-diversity analysis, oversubscription calculations, congestion-control configuration, latency and loss baselines, collective-communication benchmarks, cabling and optics records, controller and core-service configurations.

**Domain-specific emphasis.**

- Verify fabric fault domains: the effect of a leaf, spine or optical link failure on collective-communication performance and on job completion.

- Check that the management and out-of-band networks remain available when the production fabric, identity services or power to one hall fail.

- Confirm time, DNS and other core services needed to restart the fabric are not dependent on the fabric they restart.

- Link and switch failover tests are performed only in maintenance windows approved by the network owner.

**Specialist competence.** Data-centre and HPC networking; RDMA fabrics; optical transport; network operations.

## D-OPS Building Operations and Service Management

**Domain guide:** AIDCF-018-OPS (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-07, CG-13, CG-14.

**Assessment focus.** Whether the operating model, procedures, work control, maintenance, alarm and incident management, change and capacity operations keep the facility and AI infrastructure within the declared envelope.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| OPS-01 | Operating model and staffing | MCF-OPS-001 to MCF-OPS-004 | 24x7 Coverage; Role Clarity; Shift Handover; Competence and Authorisation |
| OPS-02 | Procedure and work control | MCF-OPS-005 to MCF-OPS-008 | Standard Operating Procedures; Method Statements; Permit to Work; Lockout and Tagout |
| OPS-03 | Maintenance and reliability | MCF-OPS-009 to MCF-OPS-012 | Maintenance Strategy; Condition Monitoring; Calibration; Deferred Maintenance |
| OPS-04 | Alarm, incident and problem management | MCF-OPS-013 to MCF-OPS-016 | Alarm Rationalisation; Incident Response; Root Cause Analysis; Problem Elimination |
| OPS-05 | Change and configuration management | MCF-OPS-017 to MCF-OPS-020 | Configuration Baseline; Change Assessment; Temporary Configuration; Rollback and Validation |
| OPS-06 | Capacity and service operations | MCF-OPS-021 to MCF-OPS-024 | Capacity Review; Service Level Monitoring; Resource Balancing; Operational Reporting |

**Baseline evidence.** Staffing rosters, competence and authorisation records, SOPs, method statements, permits to work, lockout/tagout records, maintenance plans and work orders, alarm logs and rationalisation records, incident and problem records, change records.

**Domain-specific emphasis.**

- Sample work orders and permits for high-risk tasks and reconcile with method statements, isolation records and post-work validation.

- Assess alarm load and rationalisation: alarm floods during events reduce operator effectiveness and are an OPERATION concern.

- Check deferred maintenance against the residual-risk acceptance and its expiry.

- Observe shift handover and emergency response drills rather than relying only on procedure documents.

**Specialist competence.** Critical-facility operations; maintenance and reliability engineering; incident and change management.

## D-RES Resilience, Continuity and Recovery

**Domain guide:** AIDCF-018-RES (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-09, CG-10.

**Assessment focus.** Whether resilience strategy, fault-domain design, continuity and recovery plans, testing and crisis response together contain failures and restore Service Outcomes within tolerance.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| RES-01 | Resilience strategy | MCF-RES-001 to MCF-RES-004 | Minimum Service Outcome; Graceful Degradation; Resilience Scenarios; Resilience Ownership |
| RES-02 | Fault-domain and containment design | MCF-RES-005 to MCF-RES-008 | Fault-Domain Definition; Containment Boundaries; Blast Radius; Isolation Validation |
| RES-03 | Continuity planning | MCF-RES-009 to MCF-RES-012 | Continuity Strategy; Alternative Capacity; Site and Provider Continuity; Crisis Priorities |
| RES-04 | Recovery planning | MCF-RES-013 to MCF-RES-016 | Recovery Dependencies; Recovery Sequencing; Configuration Restoration; Data and Checkpoint Recovery |
| RES-05 | Testing and exercising | MCF-RES-017 to MCF-RES-020 | Component Tests; Integrated Scenario Tests; Tabletop Exercises; Lessons and Retest |
| RES-06 | Crisis and adaptive response | MCF-RES-021 to MCF-RES-024 | Crisis Command; Stakeholder Communications; Emergency Change; Post-Event Adaptation |

**Baseline evidence.** Resilience strategy and minimum service outcome definitions, fault-domain and blast-radius analyses, continuity and recovery plans, recovery sequencing and dependency records, test and exercise reports, lessons-learned and retest records.

**Domain-specific emphasis.**

- Validate recovery sequencing across domains: power before cooling before compute, and the control-plane, identity and storage services each needs.

- Prefer integrated scenario evidence (RES-05) over component tests for RESILIENCE claims, and record which states and loads were exercised.

- Check that lessons from exercises and incidents produced retested changes, not only recorded actions.

- Integrated tests require a joint authorisation by the power, thermal, IT and safety authorities.

**Specialist competence.** Resilience engineering; business continuity; crisis management; cross-domain systems analysis.

## D-SUP Supply Chain, OEM and Ecosystem Assurance

**Domain guide:** AIDCF-018-SUP (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-03, CG-13, CG-15.

**Assessment focus.** Whether suppliers, OEMs and service providers are assured for capability, resilience, provenance, update integrity, spares and remote access in proportion to their effect on Service Outcomes.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| SUP-01 | Supplier due diligence | MCF-SUP-001 to MCF-SUP-004 | Supplier Capability; Financial and Operational Resilience; Security and Quality Posture; Sub-Tier Visibility |
| SUP-02 | Contract and service obligations | MCF-SUP-005 to MCF-SUP-008 | Service Levels; Evidence Rights; Incident Notification; Exit and Transition Rights |
| SUP-03 | Hardware and component provenance | MCF-SUP-009 to MCF-SUP-012 | Approved Sourcing; Counterfeit Prevention; Chain of Custody; Component Traceability |
| SUP-04 | Software, firmware and update supply | MCF-SUP-013 to MCF-SUP-016 | Release Provenance; Signature Validation; Compatibility Assurance; Vulnerability Response |
| SUP-05 | Spares, logistics and obsolescence | MCF-SUP-017 to MCF-SUP-020 | Critical Spares; Lead Times; Logistics Continuity; End-of-Life Planning |
| SUP-06 | Remote support and third-party access | MCF-SUP-021 to MCF-SUP-024 | Support Identity; Activation and Approval; Session Monitoring; Revocation and Review |

**Baseline evidence.** Supplier due-diligence records, contracts and service schedules, evidence-rights clauses, provenance and chain-of-custody records, firmware release and signature records, spares inventories and lead times, remote-support access logs.

**Domain-specific emphasis.**

- Verify that contracts grant the evidence and audit rights the assessment depends on; missing rights are limitations, not favourable assumptions.

- Check firmware and software update provenance and signature validation for facility controllers, accelerators, network and storage platforms.

- Reconcile critical spares to failure-mode and lead-time analysis for long-lead items (for example transformers, switchgear, CDUs, optics).

- Remote OEM access is assessed with SEC controls for identity, activation, session monitoring and revocation.

**Specialist competence.** Supply-chain assurance; procurement and contract; hardware provenance; OEM support models.

## D-SEC Digital, OT and Control-Plane Security

**Domain guide:** AIDCF-018-SEC (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): CG-07, CG-15.

**Assessment focus.** Whether identity, privilege, segmentation, configuration, detection and response, and automated or AI-enabled action bound the digital authority that can affect facility and AI infrastructure.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| SEC-01 | Identity and privileged access | MCF-SEC-001 to MCF-SEC-004 | Human Identity; Machine Identity; Privileged Access; Break-Glass Governance |
| SEC-02 | Control-plane protection | MCF-SEC-005 to MCF-SEC-008 | BMS and EPMS Security; Cluster Manager Security; Fabric Controller Security; Storage Controller Security |
| SEC-03 | Network security and segmentation | MCF-SEC-009 to MCF-SEC-012 | Security Zoning; Management-Plane Segmentation; Filtering and Gateways; Remote Access |
| SEC-04 | Configuration, vulnerability and patching | MCF-SEC-013 to MCF-SEC-016 | Secure Baseline; Vulnerability Management; Patch Governance; Exception and Compensating Control |
| SEC-05 | Detection and response | MCF-SEC-017 to MCF-SEC-020 | Security Telemetry; Behaviour Detection; Incident Containment; Forensic Readiness |
| SEC-06 | AI-enabled and automated action | MCF-SEC-021 to MCF-SEC-024 | Agent or Automation Authority; Approval Controls; Command Allowlisting; Safe Rollback |

**Baseline evidence.** Identity and privilege inventories, privileged-session logs, segmentation designs and firewall rule sets, control-plane configurations (BMS, EPMS, CDU, cluster, fabric and storage managers), vulnerability and patch records, detection and response records, automation authority and allowlists.

**Domain-specific emphasis.**

- Map who and what can issue commands to BMS, EPMS, CDU, PLC and cluster managers, from which networks, and with what approval; reachability alone is not authority, and authority without reachability is not exposure.

- Check break-glass accounts for custody, monitoring and post-use review.

- Evaluate automation and AI agents that can change infrastructure state for command allowlisting, approval and safe rollback.

- Security testing of operational technology is performed only with explicit owner approval and vendor-supported methods; active scanning of controllers is excluded unless authorised.

**Specialist competence.** OT and industrial control-system security; identity and privileged access; infrastructure security operations.

## D-EVA Evidence, Assessment and Assurance Management

**Domain guide:** AIDCF-018-EVA (standards/aidcf-018-domain-guides/). **Principal gates informed** (see AIDCF-007A registry v1.1 for control-level mappings): none mapped per control; EVA controls support evaluation of the meta-gates CG-11 and CG-12, which are evaluated across all controls.

**Assessment focus.** Whether evidence architecture, provenance, assessment planning, Findings and UNKNOWN handling, gates and decisions, and reassessment are managed so that assurance conclusions are traceable and current.

| **Family** | **Title** | **Controls** | **Control topics** |
|------------|-----------|--------------|--------------------|
| EVA-01 | Evidence architecture | MCF-EVA-001 to MCF-EVA-004 | Evidence Taxonomy; Evidence Ownership; Evidence Repository; Retention and Protection |
| EVA-02 | Evidence provenance and quality | MCF-EVA-005 to MCF-EVA-008 | Source Provenance; Integrity and Custody; Relevance and Reliability; Currency and Coverage |
| EVA-03 | Assessment planning and execution | MCF-EVA-009 to MCF-EVA-012 | Decision Question; Scope and Criteria; Sampling and Testing; Specialist Involvement |
| EVA-04 | Findings, UNKNOWN and limitations | MCF-EVA-013 to MCF-EVA-016 | Finding Traceability; UNKNOWN Preservation; Conflict Handling; Limitation Disclosure |
| EVA-05 | Critical gates and decisions | MCF-EVA-017 to MCF-EVA-020 | Gate Applicability; Gate Evidence; Independent Decision; Claim Language |
| EVA-06 | Reassessment and continuing assurance | MCF-EVA-021 to MCF-EVA-024 | Evidence Expiry; Change Triggers; Monitoring Coverage; Decision Suspension and Supersession |

**Baseline evidence.** Evidence manifests and repositories, custody and integrity records, assessment plans and workpapers, Finding and UNKNOWN registers, Gate Result and decision records, reassessment and supersession records.

**Domain-specific emphasis.**

- Sample decisive assertions and trace them to Evidence Objects with provenance and integrity records.

- Check that UNKNOWN Records have severity, owner and decision effect, and that none have been silently closed.

- CG-11 and CG-12 are evaluated across all controls; EVA controls provide the management-system evidence that these meta-gates can be evaluated reliably.

- For continuing assurance (AL6), verify monitoring coverage and source health for every monitored claim.

**Specialist competence.** Assurance methodology; evidence management; data governance.

# E Workpaper templates WP-01 to WP-20

Workpaper templates are numbered WP-01 to WP-20. (In version 1.0 they were numbered E1–E20; they were renumbered to avoid confusion with the AIDCF-008 evidence classes E1–E7. Annex E gives the mapping.) Each template consists of the common header below plus the template-specific fields. Blank fields are not evidence of NOT_APPLICABLE; a field that does not apply is marked "n/a" with a reason.

## E.0 Common header and quality review (all templates)

| **Field**        | **Entry**                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------|
| workpaperId      | Stable identifier (template ID, assessment ID, sequence), for example WP-12/ASM-0042/0137.    |
| assessmentId     | Assessment to which the record belongs.                                                       |
| capabilityId     | Capability Instance identifier.                                                               |
| version          | Workpaper version; prior versions retained.                                                   |
| workpaperStatus  | DRAFT, IN_REVIEW, REVIEWED, RETURNED, SUPERSEDED.                                             |
| preparer         | Name, role and competence reference.                                                          |
| reviewer         | Name, role, independence basis and review date.                                               |
| relatedRecords   | Links to other WP records, Evidence Objects, Findings and UNKNOWN Records.                    |
| classification   | Disclosure classification (AIDCF-012 Part XIII).                                              |

| **Quality review check (all templates)**           | **Yes/No** | **Reviewer note** |
|----------------------------------------------------|------------|-------------------|
| Scope, operating states and period explicit        |            |                   |
| Evidence traceable to Evidence Objects             |            |                   |
| UNKNOWN and conflicts visible                      |            |                   |
| Result, gate and decision effect correctly applied |            |                   |
| Wording within the decision ceiling                |            |                   |

**AMH-REQ-048** Workpapers shall contain at least the common header fields and the template-specific fields marked as mandatory for the record type; an equivalent tool-based record is acceptable where it carries the same fields with the same controlled values.

## WP-01 Assessment Charter

| **Field**             | **Entry**                                                                     |
|-----------------------|-------------------------------------------------------------------------------|
| trigger               | Event or need that initiated the assessment.                                  |
| decisionQuestion      | The question the Assurance Decision will answer.                              |
| sponsor               | Name and authority.                                                           |
| decisionAuthority     | Name and authority to issue the Assurance Decision.                           |
| intendedUsers         | Named users and permitted reliance.                                           |
| programmeModel        | First-party, co-sourced, second-party or independent third-party (AIDCF-011). |
| assessmentType        | AIDCF-011 Part V type.                                                        |
| targetAssuranceLevel  | AL0–AL6.                                                                      |
| preliminaryCapability | Capability Instance and Service Outcomes (preliminary).                       |
| exclusions            | Excluded scope and rationale.                                                 |
| constraints           | Access, time, safety, legal and confidentiality constraints.                  |
| artifactVersions      | AIDCF artifact and capability-profile versions applied (A1).                  |
| conformanceClaim      | Part A in full; Part B elements adopted.                                      |

## WP-02 Capability Profile

| **Field**            | **Entry**                                                                   |
|----------------------|-----------------------------------------------------------------------------|
| capabilityOwner      | Accountable owner.                                                          |
| lifecycleStage       | PLAN, DESIGN, BUILD, COMMISSION, OPERATE, CHANGE or DECOMMISSION.           |
| serviceOutcomes      | Each outcome with metric, tolerance, measurement method and criticality.    |
| requiredFunctions    | Required Functions per outcome.                                             |
| demandProfile        | Current, peak, transient and forecast demand with sources.                  |
| operatingStates      | In-scope states (NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION, SHUTDOWN, FAILED, UNKNOWN). |
| operatingEnvelope    | Envelope parameters with units and basis (illustrative defaults labelled).  |
| architectureBaseline | Architecture snapshot reference.                                            |
| specialistValidation | Specialists who validated the profile.                                      |

## WP-03 Scope and Boundary

| **Field**             | **Entry**                                                                |
|-----------------------|--------------------------------------------------------------------------|
| physicalBoundary      | Sites, buildings, halls, plant areas.                                    |
| logicalBoundary       | Systems, networks, control planes, tenants.                              |
| organisationalBoundary| Owner, operator, providers and their responsibilities.                   |
| temporalBoundary      | Point in time or evidence period.                                        |
| interfaces            | Boundary crossings with owning party.                                    |
| dependencyBaseline    | Upstream, downstream, shared, common-mode and recovery dependencies.     |
| exclusions            | Each exclusion with rationale, affected outcomes and decision effect.    |
| accessConstraints     | Evidence that cannot be accessed and why.                                |

## WP-04 Applicability Matrix

| **Field**          | **Entry**                                                                     |
|--------------------|-------------------------------------------------------------------------------|
| controlId          | MCF-<DOM>-NNN.                                                                |
| applicability      | Applicable or NOT_APPLICABLE.                                                 |
| naRationale        | Rationale and approver (mandatory where NOT_APPLICABLE).                      |
| claimTypes         | Claim types assigned (DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS, RESILIENCE). |
| requiredLevel      | Registry required Assurance Level (AL2–AL5).                                  |
| gateMappings       | Gate IDs with role CRITICAL or SUPPORTING (from registry).                    |
| profileStrengthening | Any capability-profile strengthening of evidence floors.                    |

## WP-05 Assessment Plan

| **Field**          | **Entry**                                                                  |
|--------------------|----------------------------------------------------------------------------|
| workstreams        | Domain workstreams, leads and technical reviewers.                         |
| methodMap          | Per control and claim type: methods and evidence requirements.             |
| fieldworkSchedule  | Interviews, inspections, samples, tests with dates and dependencies.       |
| safetyPlan         | Rules of engagement reference, permits and stop authorities.               |
| reviewPoints       | Stage gates and review checkpoints.                                        |
| workpaperIndex     | Planned WP records.                                                        |

## WP-06 Evidence Request

| **Field**          | **Entry**                                                                   |
|--------------------|-----------------------------------------------------------------------------|
| requestId          | Stable request identifier.                                                  |
| assertion          | Claim the evidence must support or challenge.                               |
| controlsAndClaims  | Controls and claim types served.                                            |
| evidenceClass      | E1–E7 required; acceptable alternatives.                                    |
| periodAndStates    | Evidence period and operating states to be represented.                     |
| floors             | Quality floor (P F C R T I) and sufficiency floor (S0–S5).                  |
| custodian          | Source owner and custodian.                                                 |
| dueDate            | Date required.                                                              |
| receiptStatus      | Received, partial, refused, inaccessible, substituted; UNKNOWN Record link. |

## WP-07 Interview Record

| **Field**          | **Entry**                                                       |
|--------------------|-----------------------------------------------------------------|
| interviewee        | Role (and name where permitted).                                |
| objective          | Assertions explored.                                            |
| promptsUsed        | B9.1–B9.4 prompts and additions.                                |
| statements         | Summary of statements, distinguishing practice from procedure.  |
| evidenceReferences | Evidence offered or requested.                                  |
| contradictions     | Conflicts with other evidence.                                  |
| confirmation       | Interviewee confirmation of notes.                              |

## WP-08 Site Inspection Record

| **Field**          | **Entry**                                                          |
|--------------------|--------------------------------------------------------------------|
| location           | Site, room, zone, row or plant item.                               |
| route              | Approved route and escort.                                         |
| inspectionItems    | Part B Part III checklist items applied.                           |
| sampledAssets      | Assets and zones verified against record.                          |
| observations       | Condition, labels, alarms, temporary arrangements.                 |
| operatingState     | State observed at time of inspection.                              |
| deviations         | Deviations from the approved record.                               |
| inaccessibleScope  | Areas not inspected and why.                                       |
| safetyStatus       | Safety events or stops.                                            |

## WP-09 Sampling Plan

| **Field**          | **Entry**                                                                  |
|--------------------|----------------------------------------------------------------------------|
| population         | Population definition and source; completeness reconciliation.             |
| strata             | Stratification basis.                                                      |
| method             | Random, systematic, judgmental or scenario.                                |
| parameters         | Confidence, tolerable deviation rate, expected deviations (Part B §II.2). |
| sampleSize         | Size and derivation.                                                       |
| exceptions         | Exceptions found and expansion performed.                                  |
| inference          | Conclusion supported and its limits.                                       |

## WP-10 Test Plan

| **Field**          | **Entry**                                                                    |
|--------------------|------------------------------------------------------------------------------|
| proposition        | Claim under test and claim type.                                             |
| initialState       | Required initial operating state and load.                                   |
| procedure          | Steps, operator and method statement reference.                              |
| instrumentation    | Measurement points, accuracy and time synchronisation.                       |
| acceptanceCriteria | Expected result linked to assessmentCriteria.                                |
| abortCriteria      | Conditions that stop the test.                                               |
| authorisations     | Capability owner, safety authority and change approval.                      |
| restorationPlan    | Return-to-service steps and verification.                                    |

## WP-11 Test Result

| **Field**           | **Entry**                                                                 |
|---------------------|---------------------------------------------------------------------------|
| testPlanRef         | WP-10 reference.                                                          |
| conditionsAchieved  | Actual load, duration, states and failure conditions.                    |
| measurements        | Results against acceptance criteria.                                      |
| anomalies           | Deviations, aborts and near misses.                                       |
| postState           | Post-test state and restoration verification.                             |
| coverageGaps        | Untested conditions within claim scope (UNKNOWN type U5).                 |
| retestNeeds         | Retest requirements.                                                      |

## WP-12 Control Result

| **Field**           | **Entry**                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------|
| controlId           | MCF-<DOM>-NNN and registry version.                                                         |
| claimType           | DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS or RESILIENCE.                             |
| subjectAndScope     | Subject, boundary, operating states and period.                                             |
| criteriaResults     | Each assessmentCriteria item: met, not met, undetermined, with evidence.                    |
| methodsPerformed    | Canonical methods used.                                                                     |
| evidenceAssessment  | Quality band, sufficiency level, conflicts.                                                 |
| result              | CONFORMING, PARTIAL, NONCONFORMING, UNKNOWN, NOT_APPLICABLE, NOT_ASSESSED.                  |
| confidence          | CONF-0 to CONF-4, with CONFLICTING or STALE flags.                                          |
| findingsAndUnknowns | Linked Findings and UNKNOWN Records.                                                        |
| gateEffect          | Gates affected and role (CRITICAL or SUPPORTING).                                           |
| implementationMaturity | Optional diagnostic IM0–IM5 (never a result).                                            |

## WP-13 Scenario Record

| **Field**          | **Entry**                                                                  |
|--------------------|----------------------------------------------------------------------------|
| scenarioId         | Stable identifier and AIDCF-004 scenario reference.                        |
| initiatingCondition| Threat, hazard or initiating event and operating state.                    |
| propagationPath    | Ordered path across systems and fault domains.                             |
| safeguards         | Safeguards on the path and their own dependencies.                         |
| residualState      | State after safeguards act.                                                |
| recoveryPath       | Recovery sequence and time.                                                |
| outcomeEffect      | Effect on Service Outcomes versus tolerance.                               |
| evidenceAndUnknown | Evidence relied on and UNKNOWN Records.                                    |

## WP-14 Critical Gate Result

| **Field**              | **Entry**                                                                            |
|------------------------|--------------------------------------------------------------------------------------|
| gateId                 | CG-01 to CG-15.                                                                      |
| applicability          | In scope, or APPROVED_NA with boundary rationale and approver.                      |
| criticalControls       | In-scope CRITICAL controls and their results at the required claim type.             |
| supportingControls     | SUPPORTING controls; gate-level evaluation for any NONCONFORMING.                    |
| gateCriteria           | AIDCF-010 gate criteria and whether met.                                             |
| evidenceFloor          | Required floor and achieved sufficiency.                                             |
| attachedUnknowns       | US4/US5 UNKNOWN Records attached.                                                    |
| gateResult             | PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED.                                    |
| decisionCeiling        | Ceiling imposed under AIDCF-010.                                                     |
| closure                | Actions, evidence and retest required to change the result.                          |

## WP-15 Finding Record

| **Field**          | **Entry**                                                                   |
|--------------------|-----------------------------------------------------------------------------|
| findingId          | Stable identifier and title.                                                |
| criterion          | Control requirement or assessment criterion.                                |
| condition          | Evidenced state.                                                            |
| evidence           | Supporting and challenging Evidence Objects.                                |
| cause              | Evidenced cause or labelled analysis.                                       |
| consequence        | Affected Service Outcomes, dependencies and states.                         |
| classification     | AIDCF-012 Part IX classification.                                           |
| resultAndGateEffect| Control result and gate effect.                                             |
| action             | Required action, owner and closure evidence.                                |

## WP-16 UNKNOWN Record

| **Field**          | **Entry**                                                               |
|--------------------|-------------------------------------------------------------------------|
| unknownId          | Stable identifier.                                                      |
| subject            | Affected object (control, gate, outcome, dependency, boundary).         |
| missingAttribute   | What is not known.                                                      |
| type               | U1–U10 (AIDCF-008 §35).                                                 |
| severity           | US1–US5 with the test applied.                                          |
| decisionEffect     | Gate result, ceiling, condition or confidence ceiling.                  |
| evidenceNeeded     | Evidence or method required to resolve.                                 |
| owner              | Resolution owner.                                                       |
| resolutionStatus   | OPEN, RESOLVED (with resulting result), ACCEPTED_AS_LIMITATION, SUPERSEDED. |

## WP-17 Limitation Record

| **Field**          | **Entry**                                                              |
|--------------------|------------------------------------------------------------------------|
| limitationId       | Stable identifier.                                                     |
| nature             | Scope, method, access, time or competence limitation.                  |
| cause              | Why the limitation exists.                                             |
| affectedItems      | Results, gates and claims affected.                                    |
| decisionEffect     | Effect on decision state and wording.                                  |
| disclosure         | Where it is disclosed (decision, report classes).                      |

## WP-18 Independent Review

| **Field**          | **Entry**                                                                 |
|--------------------|---------------------------------------------------------------------------|
| reviewer           | Name, independence basis and competence.                                  |
| packageReviewed    | Decision snapshot ID.                                                     |
| samplesTraced      | Assertions traced to evidence.                                            |
| challenges         | Challenges raised, by gate, UNKNOWN and wording.                          |
| dispositions       | Resolution of each challenge.                                             |
| conclusion         | PROCEED to decision or RETURN.                                            |

## WP-19 Assurance Decision

| **Field**             | **Entry**                                                                          |
|-----------------------|------------------------------------------------------------------------------------|
| decisionQuestion      | As chartered.                                                                      |
| topClaim              | Capability Instance, Service Outcomes, tolerances, states, question and date.     |
| gateSummary           | Gate Results CG-01 to CG-15 in canonical states.                                   |
| controllingFactors    | Gate Results and UNKNOWN Records that set the ceiling.                             |
| scoreSnapshot         | Score Snapshot reference with coverage and bands (AIDCF-010).                      |
| decisionState         | REASONABLY_ASSURED, CONDITIONALLY_ASSURED, LIMITED, NOT_ASSURED or INCONCLUSIVE.   |
| conditions            | Conditions with owner, due date or event, evidence and failure effect.             |
| limitations           | Linked WP-17 records.                                                              |
| validity              | Validity period and Reassessment Triggers.                                         |
| lifecycleState        | DRAFT, RECOMMENDED, APPROVED, ACTIVE, SUSPENDED, WITHDRAWN, SUPERSEDED, EXPIRED.   |
| controlledWording     | AIDCF-012 Part V wording used.                                                     |

## WP-20 Reassessment Record

| **Field**             | **Entry**                                                                |
|-----------------------|--------------------------------------------------------------------------|
| trigger               | Change, incident, evidence expiry, gate change or outcome change.        |
| affectedClaims        | Assertions, controls, gates and decisions affected.                      |
| interimState          | Decision lifecycle state while reassessing (for example SUSPENDED).      |
| reassessmentScope     | Delta or full; procedures re-performed.                                  |
| newResults            | Updated results and Gate Results.                                        |
| newDecision           | New decision record reference.                                           |
| supersession          | Prior decision ID superseded; prior record retained.                     |

# Annex A Controlled status vocabulary (canonical)

The vocabularies below are the canonical AIDCF vocabularies. Part A uses no other status values.

## A.1 Control result

| **Code**       | **Meaning**                                                                                  | **Score value**                                   |
|----------------|----------------------------------------------------------------------------------------------|---------------------------------------------------|
| CONFORMING     | All assessment criteria met for the claim type, evidence at or above the profile floor.      | 100                                               |
| PARTIAL        | Some criteria met; specific deficiencies recorded as Findings.                               | 50                                                |
| NONCONFORMING  | Criteria materially not met, or a safeguard demonstrated ineffective.                        | 0                                                 |
| UNKNOWN        | Result cannot be determined.                                                                 | No value; excluded from mean; counted in coverage and UNKNOWN register |
| NOT_APPLICABLE | Approved non-applicability with rationale and approver.                                      | Excluded                                          |
| NOT_ASSESSED   | In scope but not yet assessed.                                                               | Excluded; counted as coverage gap                 |

Legacy control-status mapping (version 1.0 values):

| **Legacy value (v1.0)**                    | **Canonical value**                                                                                   |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------|
| NOT IMPLEMENTED                            | NONCONFORMING                                                                                         |
| INEFFECTIVE                                | NONCONFORMING                                                                                         |
| IMPLEMENTED                                | CONFORMING (valid only for DESIGN and IMPLEMENTATION claims)                                          |
| OPERATING EFFECTIVELY / STRONGLY EFFECTIVE | CONFORMING (for OPERATION and EFFECTIVENESS claims)                                                   |
| N/A                                        | NOT_APPLICABLE                                                                                        |
| SUSPENDED                                  | Lifecycle state SUSPENDED on the Control Assessment record; the result reverts to UNKNOWN             |
| NOT ASSESSED                               | NOT_ASSESSED                                                                                          |
| PARTIAL, UNKNOWN                           | Unchanged                                                                                             |

Implementation Maturity IM0 Absent, IM1 Initial, IM2 Defined, IM3 Implemented, IM4 Operating and IM5 Optimised (AIDCF-017) is a diagnostic attribute only and is never a control result.

## A.2 Gate result

PASS, FAIL, UNKNOWN, APPROVED_NA, NOT_ASSESSED. There is no conditional gate result. (Version 1.0 "approved N/A" maps to APPROVED_NA.)

## A.3 Decision state, decision lifecycle and aliases

Decision states: REASONABLY_ASSURED, CONDITIONALLY_ASSURED, LIMITED, NOT_ASSURED, INCONCLUSIVE.

Decision lifecycle: DRAFT, RECOMMENDED, APPROVED, ACTIVE, SUSPENDED, WITHDRAWN, SUPERSEDED, EXPIRED.

Ranking for ceilings (AIDCF-010): REASONABLY_ASSURED > CONDITIONALLY_ASSURED > LIMITED > INCONCLUSIVE > NOT_ASSURED.

| **Legacy value**                                                        | **Canonical value**                                              |
|-------------------------------------------------------------------------|------------------------------------------------------------------|
| ADVERSE; ADVERSE_NOT_ASSURED; "Adverse / Not assured"                   | NOT_ASSURED                                                      |
| UNKNOWN (as decision); UNKNOWN_INCONCLUSIVE; UNKNOWN_OR_INCONCLUSIVE; Withheld | INCONCLUSIVE                                              |
| CONDITIONAL                                                             | CONDITIONALLY_ASSURED                                            |
| REASONABLY ASSURED (with space)                                         | REASONABLY_ASSURED                                               |
| NOT ASSESSED (as decision)                                              | Not a decision state; no decision is issued                      |
| SUSPENDED, WITHDRAWN, SUPERSEDED (as decision)                          | Decision lifecycle states, not decision states                   |

## A.4 Finding classification

Observation, Improvement opportunity, Weakness, Significant weakness, Critical finding, as defined in AIDCF-012 Part IX. A Finding classification is not a control result; the control result is recorded separately in WP-12.

## A.5 Confidence

CONF-0 UNKNOWN, CONF-1 LOW, CONF-2 MODERATE, CONF-3 HIGH, CONF-4 VERY_HIGH, with the flags CONFLICTING and STALE (AIDCF-008 §27).

## A.6 UNKNOWN type and severity

Type U1 Missing, U2 Inaccessible, U3 Stale, U4 Conflicting, U5 Coverage gap, U6 Source unverified, U7 Integrity uncertain, U8 Method uncertain, U9 Interpretation unresolved, U10 Dependency unknown (AIDCF-008 §35). Severity US1 Low, US2 Moderate, US3 Material, US4 Critical, US5 Systemic (procedure C5).

## A.7 Claim types and Assurance Levels

Claim types DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS, RESILIENCE (procedure A3). Assurance Levels AL0 Discovery, AL1 Readiness, AL2 Design, AL3 Implementation, AL4 Operational, AL5 Effectiveness and resilience, AL6 Continuing (AIDCF-011). Version 1.0 references to "A0–A5" map to AL0–AL5; registry values A2–A5 map to AL2–AL5.

## A.8 Assessment methods

INQUIRY, DOCUMENT_REVIEW, INSPECTION, OBSERVATION, RECONCILIATION, ANALYSIS, SAMPLING, TEST, REPERFORMANCE, SCENARIO_EXERCISE.

## A.9 Operating states

NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION, SHUTDOWN, FAILED, UNKNOWN (AIDCF-003 §45).

## A.10 Stage-gate outcome and workpaper status

Stage-gate outcome: PROCEED, RETURN, STOP. Workpaper status: DRAFT, IN_REVIEW, REVIEWED, RETURNED, SUPERSEDED.

**AMH-REQ-049** Assessment records shall use only the canonical values in Annex A; legacy values received from earlier records shall be converted using the mappings in A.1 and A.3 and the original value retained in the record history.

# Annex B Machine-readable package

| **Artifact**                        | **Purpose**                                            |
|-------------------------------------|--------------------------------------------------------|
| assessment-charter.schema.json      | WP-01 charter and authority                            |
| capability-profile.schema.json      | WP-02 capability, outcomes and envelope                |
| assessment-plan.schema.json         | WP-05 plan and method map                              |
| control-assessment.schema.json      | WP-12 control results per claim type                   |
| scenario-record.schema.json         | WP-13 failure scenarios                                |
| gate-result.schema.json             | WP-14 Gate Results                                     |
| finding.schema.json                 | WP-15 Findings                                         |
| unknown-record.schema.json          | WP-16 UNKNOWN Records                                  |
| assurance-decision.schema.json      | WP-19 decision                                         |
| reassessment-record.schema.json     | WP-20 reassessment and supersession                    |

Object classes and relationships used by these schemas are the canonical AIDCF-014 classes (for example Assessment, ControlAssessment, GateResult, UnknownRecord, AssuranceDecision) and relationship types (for example ASSESSED_BY, EVIDENCED_BY, HAS_FINDING, HAS_UNKNOWN, EVALUATES_GATE, CONSTRAINS, SUPERSEDES). Ontology and validation shapes are published under AIDCF-014 and AIDCF-016; AIDCF-009 does not publish a separate ontology.

# Annex C Validation rules

The following requirements are validation rules applied to every assessment package; they are checked at SG5 and are suitable for automated validation.

**AMH-REQ-050** An assessment record shall have a decision question, a Capability Instance and at least one Service Outcome.

**AMH-REQ-051** Every in-scope control shall have an applicability decision, assigned claim types, methods, evidence references and a result per claim type.

**AMH-REQ-052** Every assertion relied on shall have supporting evidence or a linked UNKNOWN Record.

**AMH-REQ-053** Every test record shall have authorisation, initial state, abort criteria and restoration verification.

**AMH-REQ-054** Every in-scope gate shall have a Gate Result, evidence references and technical and independent review.

**AMH-REQ-055** No Decision Recommendation or Assurance Decision shall exceed a ceiling imposed by a FAIL or UNKNOWN gate.

**AMH-REQ-056** Every Finding shall map evidence, criterion, cause (or labelled analysis) and outcome consequence.

**AMH-REQ-057** Every Assurance Decision shall state scope, operating states, period, conditions, validity and decision authority.

**AMH-REQ-058** Every automated or AI-assisted inference shall remain a candidate until reviewed by a competent person, and shall not change a result, Gate Result or decision automatically.

**AMH-REQ-059** Every superseded decision shall remain retrievable and linked by SUPERSEDES to its successor.

**AMH-REQ-060** Every external dependency in the dependency baseline shall remain visible in the decision package, including where excluded.

**AMH-REQ-061** Every NOT_APPLICABLE result and APPROVED_NA Gate Result shall have an approved rationale.

**AMH-REQ-062** Every US3, US4 and US5 UNKNOWN Record shall have a recorded decision effect.

**AMH-REQ-063** Every record containing sensitive infrastructure detail shall carry a classification.

**AMH-REQ-064** Every material change recorded in the change baseline shall be mapped to the decisions it affects.

# Annex D Review and release

The authoritative list of reviewer roles and release-gate states for AIDCF-009, AIDCF-011 and AIDCF-012 is maintained in one place: AIDCF-011 Part XXII. This Part does not repeat it. Review of this document by the reviewer roles assigned to AIDCF-009 in that table is pending; this document has not been released.

# Annex E Mapping from version 1.0 identifiers

## E.1 Workpaper templates

| **v1.0 template** | **v1.1 template** | **Title**              |
|-------------------|-------------------|------------------------|
| E1                | WP-01             | Assessment Charter     |
| E2                | WP-02             | Capability Profile     |
| E3                | WP-03             | Scope and Boundary     |
| E4                | WP-04             | Applicability Matrix   |
| E5                | WP-05             | Assessment Plan        |
| E6                | WP-06             | Evidence Request       |
| E7                | WP-07             | Interview Record       |
| E8                | WP-08             | Site Inspection Record |
| E9                | WP-09             | Sampling Plan          |
| E10               | WP-10             | Test Plan              |
| E11               | WP-11             | Test Result            |
| E12               | WP-12             | Control Result         |
| E13               | WP-13             | Scenario Record        |
| E14               | WP-14             | Critical Gate Result   |
| E15               | WP-15             | Finding Record         |
| E16               | WP-16             | UNKNOWN Record         |
| E17               | WP-17             | Limitation Record      |
| E18               | WP-18             | Independent Review     |
| E19               | WP-19             | Assurance Decision     |
| E20               | WP-20             | Reassessment Record    |

## E.2 Validation rules and requirements

| **v1.0 rule** | **v1.1 requirement** |
|---|---|
| AM-VAL-001 | AMH-REQ-050 |
| AM-VAL-002 | AMH-REQ-051 |
| AM-VAL-003 | AMH-REQ-052 |
| AM-VAL-004 | AMH-REQ-053 |
| AM-VAL-005 | AMH-REQ-054 |
| AM-VAL-006 | AMH-REQ-055 |
| AM-VAL-007 | AMH-REQ-056 |
| AM-VAL-008 | AMH-REQ-057 |
| AM-VAL-009 | AMH-REQ-058 |
| AM-VAL-010 | AMH-REQ-059 |
| AM-VAL-011 | AMH-REQ-060 |
| AM-VAL-012 | AMH-REQ-061 |
| AM-VAL-013 | AMH-REQ-062 |
| AM-VAL-014 | AMH-REQ-063 |
| AM-VAL-015 | AMH-REQ-064 |

Requirements AMH-REQ-001 to AMH-REQ-064 are new in version 1.1 except those mapped above; version 1.0 contained no numbered requirements.

## E.3 Other identifier changes

| **v1.0**                                        | **v1.1**                                                                                 |
|-------------------------------------------------|------------------------------------------------------------------------------------------|
| Artifact ID AIDCF-AM-001                        | AIDCF-009 (Part A)                                                                       |
| "AM0–AM5 conformance"                           | Conformance claim: Part A in full plus declared Part B elements (A1 step 6, AMH-REQ-001) |
| "A0–A5 assurance ceiling"                       | Target Assurance Level AL0–AL6 and claim types (A3)                                      |
| 90 family procedures (GOV-01 … EVA-06), each with four lens steps "control 001 design, 002 implemented, 003 operation, 004 failure" | Replaced by 15 domain playbooks (section D); each control is a distinct topic assessed per claim type, with control-specific procedures in the AIDCF-007A registry v1.1 and AIDCF-018 domain guides |
| Domain playbook IDs DGOV … DEVA                 | D-GOV … D-EVA                                                                            |
| aidcf-am-v1.0.owl / ttl; aidcf-am-shapes-v1.0.ttl | Ontology and shapes published under AIDCF-014 / AIDCF-016                              |
| Appendix D review and release table             | AIDCF-011 Part XXII                                                                      |

## Final doctrine

An AIDCF assessment is complete only when decision question, Capability Instance, Service Outcomes, boundary, dependencies, controls, failure paths, safeguards, evidence, UNKNOWN, gates, review and validity are traceably connected. Otherwise the practitioner reduces, conditions or suspends assurance, or declines to issue a decision, using the canonical decision states and lifecycle.
