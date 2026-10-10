> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-009_Part_B_Enhanced_Practitioner_Companion_v1.2.pdf](AIDCF-009_Part_B_Enhanced_Practitioner_Companion_v1.2.pdf).

**AIDCF**

**AI Data Centre Facilities Assurance Framework**

**ASSESSMENT METHODOLOGY PRACTITIONER HANDBOOK — PART B: ENHANCED COMPANION**

**Version 1.1**

Decision trees DT-01 to DT-20 • generic assessment protocol per claim type • index of control-specific procedures • inspection checklists by domain • evidence-collection playbooks • CG-01 to CG-15 gate workbooks • synthetic examples • assessor competence levels • graph-ingestion mappings • record schemas

Artifact ID: AIDCF-009 (Part B)  
Author: Siva Sethumadhavan  
Status: Draft for controlled review

# Document control

| **Field**        | **Value**                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Title            | AIDCF-009 Assessment Methodology Practitioner Handbook — Part B: Enhanced Companion                                                           |
| Artifact ID      | AIDCF-009 (requirement short code AMH)                                                                                                         |
| Part             | Part B — Enhanced Companion. Normative core: AIDCF-009 Part A — Core Handbook                                                                   |
| Version          | 1.2                                                                                                                                            |
| Date             | 2026-10-10                                                                                                                                     |
| Status           | Draft for controlled review                                                                                                                    |
| Author           | Siva Sethumadhavan                                                                                                                             |
| Depends on       | AIDCF-009 Part A; AIDCF-003; AIDCF-004; AIDCF-007A registry v1.1; AIDCF-008; AIDCF-010; AIDCF-011; AIDCF-012; AIDCF-014; AIDCF-018 domain guides |
| Control universe | 15 domains, 90 families and 360 controls (AIDCF-007A)                                                                                          |
| Safety           | No hazardous or disruptive testing without explicit authority and competent engineering governance                                             |
| Assurance        | UNKNOWN remains visible; gates are non-compensating; automation cannot approve material decisions                                              |

## Revision history

| **Version** | **Date**   | **Summary**                                                                                                                                                                                                                                                                                                                             |
|-------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.1 | — | Enhanced practitioner handbook, original issue (additive companion to v1.0). |
| 1.2 | 2026-10-10 | Designated as AIDCF-009 Part B (Enhanced Companion) with explicit relationship to Part A; replaced 360 lifecycle-titled boilerplate procedures with a generic per-claim-type assessment protocol and an index to control-specific procedures in the AIDCF-007A registry v1.1 and AIDCF-018 guides; rewrote decision trees DT-01–DT-20 (previously identical node structures) as distinct trees, with DT-15 and DT-19 implementing the AIDCF-010 roll-up rule and derivation order; made inspection checklists, evidence playbooks and gate workbooks domain-, class- and gate-specific; aligned vocabularies and graph mappings to canonical AIDCF sets; introduced AMH-REQ requirement IDs with mapping annex. |

# 0 Introduction

## 0.1 Purpose

Part B gives assessors structured decision support and execution detail for the method defined in Part A. It does not create authority, evidence, competence or certainty, and it does not relax any Part A requirement.

## 0.2 How Part A and Part B fit together

| **Aspect**        | **Part A — Core Handbook**                                                                                                                                 | **Part B — Enhanced Companion (this document)**                                                                                       |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Role              | Normative method for every AIDCF assessment.                                                                                                               | Execution aids and elaborations; selected elements are normative (§0.3).                                                               |
| Content           | Roles and independence, competence, stage gates SG0–SG7, procedures A1–A7, B1–B14, C1–C9, domain playbooks D-GOV to D-EVA, workpaper templates WP-01–WP-20, canonical status vocabulary (Annex A). | Decision trees, claim-type assessment protocol, control-procedure index, inspection checklists, evidence playbooks, gate workbooks, examples, competence levels, graph mappings, record schemas. |
| Precedence        | Prevails on conflict.                                                                                                                                      | Elaborates Part A; cannot relax it.                                                                                                    |
| Requirement IDs   | AMH-REQ-001 to AMH-REQ-064.                                                                                                                            | AMH-REQ-065 to AMH-REQ-086.                                                                                                   |
| Vocabulary        | Defines the canonical status vocabulary (Part A Annex A).                                                                                                  | Uses Part A Annex A without addition.                                                                                                  |

Part A references Part B at these points: procedure C1 step 4 (claim-type protocol, Part II), B11 (sampling parameters, §II.2), B10 (inspection checklists, Part III), A5 (competence levels, Part VII).

## 0.3 Normative status of Part B elements

| **Part B element**                                   | **Status**                                                                                         |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Part II Generic assessment protocol (§II.1–§II.8)    | Normative for every assessment, because Part A procedure C1 requires it.                           |
| Part II §II.9–§II.10 Control-procedure index         | Informative (the normative control content is in the AIDCF-007A registry).                         |
| Part I Decision trees                                | Normative when adopted; a tree aids judgment and never approves a decision autonomously.          |
| Part III Inspection checklists                       | Normative when adopted for an inspection.                                                          |
| Part IV Evidence-collection playbooks                | Normative when adopted; AIDCF-008 remains the authority on evidence semantics.                     |
| Part V Gate workbooks                                | Normative when adopted; AIDCF-010 remains the authority on gate criteria and ceilings.             |
| Part VI Synthetic examples                           | Informative.                                                                                       |
| Part VII Competence levels                           | Normative when adopted to evidence Part A procedure A5.                                            |
| Part VIII Graph-ingestion mappings                   | Normative when assessment records are exchanged as graph data.                                     |
| Part IX Record schemas                               | Normative when adopted; equivalent to the corresponding WP templates.                              |

**AMH-REQ-065** An assessment that adopts a Part B element shall declare it in the charter conformance claim (Part A WP-01 `conformanceClaim`) and shall then apply every "shall" statement in that element.

# Part I — Assessor decision trees

Twenty trees, DT-01 to DT-20, each covering one decision. Identifiers are unchanged from the previous edition (other artifacts, including AIDCF-010, cite them), but every tree now has its own tests and branches. At each node the assessor records the test outcome, the evidence relied on and the branch taken (Part IX "Decision Tree Instance"). Terminal outcomes are in **bold**. Trees support professional judgment; they do not approve decisions. Contrary evidence encountered while traversing a tree is retained.

**AMH-REQ-066** Every adopted decision-tree traversal that affects a control result, Gate Result or decision shall be recorded with the node outcomes, evidence references and the terminal outcome, and shall be reviewed by the technical reviewer for the domain.

**AMH-REQ-067** Trees DT-15 and DT-19 shall be applied exactly as the AIDCF-010 gate roll-up rule (Part VIII) and decision derivation order (Part XII) respectively; where the tree and AIDCF-010 differ, AIDCF-010 governs and the difference shall be reported to AIDCF-009 change control.

| **Tree** | **Decision**              | **Phase (Part A)** |
|----------|---------------------------|--------------------|
| DT-01    | Engagement acceptance     | A1, B1             |
| DT-02    | Capability definition     | B2                 |
| DT-03    | Boundary completeness     | B3                 |
| DT-04    | Control applicability     | B4                 |
| DT-05    | Evidence acceptance       | B6                 |
| DT-06    | Evidence freshness        | B6, C1             |
| DT-07    | Evidence conflict         | C1                 |
| DT-08    | Sampling                  | B11                |
| DT-09    | Interview corroboration   | B9                 |
| DT-10    | Site-inspection safety    | B10                |
| DT-11    | Testing authorisation     | B13, B14           |
| DT-12    | Control result            | C1                 |
| DT-13    | Failure path              | C2                 |
| DT-14    | Gate applicability        | B4, C3             |
| DT-15    | Gate result               | C3                 |
| DT-16    | Finding                   | C4                 |
| DT-17    | UNKNOWN severity          | C5                 |
| DT-18    | Independent review        | C6                 |
| DT-19    | Assurance decision        | C7                 |
| DT-20    | Reassessment              | C9                 |

## DT-01 Engagement acceptance

| **Node** | **Test**                                                                                      | **If yes**     | **If no**                                                      |
|----------|-----------------------------------------------------------------------------------------------|----------------|----------------------------------------------------------------|
| 1.1      | Is the decision question explicit, answerable and authorised by a named sponsor?               | 1.2            | **Rework**: return to sponsor.                                 |
| 1.2      | Is a decision authority named who is independent of the preparers?                             | 1.3            | **Rework**: appoint decision authority (Part A A4).            |
| 1.3      | Can the requested conclusion be supported at an achievable Assurance Level given access and testing authority? | 1.4 | **Rework**: reduce requested conclusion or obtain authority. |
| 1.4      | Is a competent team available for every in-scope domain without unmanaged conflicts?           | 1.5            | **Rework**, or **Stop** where competence cannot be obtained.  |
| 1.5      | Are safety, legal and confidentiality boundaries recorded?                                    | **Proceed** to Part A B1 and SG0. | **Rework**.                                 |

## DT-02 Capability definition

| **Node** | **Test**                                                                                   | **If yes** | **If no**                                                                 |
|----------|--------------------------------------------------------------------------------------------|------------|---------------------------------------------------------------------------|
| 2.1      | Is the Capability Instance identified with an accountable owner?                             | 2.2        | UNKNOWN US5 against CG-01; **Return to planning** (no outcome-level decision can be framed). |
| 2.2      | Does each Service Outcome have a measurable metric and tolerance?                            | 2.3        | UNKNOWN US5 for that outcome; **Escalate** to capability owner.            |
| 2.3      | Are the operating states in which each tolerance applies declared?                           | 2.4        | **Rework** profile (WP-02); outcome cannot support claims beyond NORMAL.   |
| 2.4      | Are demand and envelope parameters sourced and validated by a competent specialist?          | **Proceed** to boundary (DT-03). | **Rework**; record UNKNOWN (U6 or U8) against affected outcomes. |

## DT-03 Boundary completeness

| **Node** | **Test**                                                                                                    | **If yes** | **If no**                                                    |
|----------|-------------------------------------------------------------------------------------------------------------|------------|--------------------------------------------------------------|
| 3.1      | Are physical, logical, organisational and temporal boundaries recorded and approved?                         | 3.2        | UNKNOWN US5 against CG-02; **Rework**.                       |
| 3.2      | Is every boundary crossing (interface) assigned to an owning party?                                         | 3.3        | **Rework**; unowned crossings are CG-13 matters.             |
| 3.3      | Does any exclusion remove a material dependency of an in-scope Required Function?                           | 3.4        | **Proceed** to applicability (DT-04).                        |
| 3.4      | Is the exclusion's effect on the decision recorded and approved for disclosure?                              | **Proceed**, with a limitation (WP-17). | **Escalate** to sponsor; decision cannot exceed the ceiling for an undisclosed exclusion. |

## DT-04 Control applicability

| **Node** | **Test**                                                                                                     | **If yes** | **If no**                                                                                     |
|----------|--------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------------------------------------------------|
| 4.1      | Does any in-scope Required Function, dependency or operating state depend on the control's subject (registry `applicability`)? | 4.2 | 4.4 |
| 4.2      | Is the registry required Assurance Level for each relevant claim type ≤ the assessment AL?                    | **Applicable**; assign those claim types. | 4.3 |
| 4.3      | Is at least one claim type within the assessment AL?                                                          | **Applicable** for those claim types; record excluded claim types (Part A A3 step 6). | **Applicable but not concluded** at this AL; disclose. |
| 4.4      | Is the NOT_APPLICABLE rationale evidenced and approved by a person other than the preparer?                   | **NOT_APPLICABLE** | **NOT_ASSESSED** until the rationale is approved.                                   |

## DT-05 Evidence acceptance

| **Node** | **Test**                                                                                        | **If yes** | **If no**                                                    |
|----------|-------------------------------------------------------------------------------------------------|------------|--------------------------------------------------------------|
| 5.1      | Is the source identified and its authority to produce the evidence established?                   | 5.2        | **Restrict** use; UNKNOWN type U6 (source unverified).       |
| 5.2      | Is integrity and custody established (integrity reference, system-of-record extract, controlled copy)? | 5.3   | **Restrict**; UNKNOWN type U7 (integrity uncertain).         |
| 5.3      | Is the collection or test method defined well enough to interpret the result?                     | 5.4        | **Restrict**; UNKNOWN type U8 (method uncertain).            |
| 5.4      | Does the item address the subject, criterion, claim type and state of the assertion (F, fitness)? | **Accept** for rating; go to DT-06. | **Reject** for this assertion; record reason. |

## DT-06 Evidence freshness

| **Node** | **Test**                                                                                                     | **If yes** | **If no**                                                                 |
|----------|--------------------------------------------------------------------------------------------------------------|------------|---------------------------------------------------------------------------|
| 6.1      | Has any change, incident or maintenance since the evidence date altered the subject?                          | 6.2        | 6.3                                                                       |
| 6.2      | Does the change affect the attribute the evidence demonstrates?                                               | **Stale** for this claim; flag STALE; UNKNOWN U3; request current evidence. | 6.3 |
| 6.3      | Is the evidence within the evidence-profile `periodCoverage` and T (timeliness) floor?                        | 6.4        | **Stale**; UNKNOWN U3.                                                    |
| 6.4      | Does it represent the operating states the claim requires?                                                    | **Current**; rate quality. | **Accept for represented states**; UNKNOWN U5 for the rest. |

## DT-07 Evidence conflict

| **Node** | **Test**                                                                                          | **If yes**                              | **If no**                            |
|----------|---------------------------------------------------------------------------------------------------|-----------------------------------------|--------------------------------------|
| 7.1      | Do two accepted items support incompatible propositions about the same subject, state and time?     | Register both lineages; 7.2             | **No conflict**.                     |
| 7.2      | Is the conflict explained by a difference in scope, time or operating state?                       | **Resolved by scoping**; record both qualified assertions. | 7.3 |
| 7.3      | Can corroboration from an independent source or method resolve it?                                | **Resolved**; record resolution and reviewer. | 7.4                            |
| 7.4      | Is the conflict material (could it change a result, gate or condition)?                           | Flag CONFLICTING; UNKNOWN U4 with severity per DT-17; **Escalate** to technical reviewer. | Record; flag CONFLICTING; confidence ceiling applies. |

## DT-08 Sampling

| **Node** | **Test**                                                                                                       | **If yes** | **If no**                                                         |
|----------|----------------------------------------------------------------------------------------------------------------|------------|-------------------------------------------------------------------|
| 8.1      | Is the population complete and reconciled to a system of record?                                                | 8.2        | **Do not sample**; UNKNOWN U5; reconcile the population first.    |
| 8.2      | Is the population smaller than the derived sample size, or are the items CRITICAL-mapped to CG-04, CG-05 or CG-06? | **Test all items** (§II.2). | 8.3                                          |
| 8.3      | Has the sample size been derived from declared parameters (§II.2) and stratified?                               | 8.4        | **Rework** the sample design.                                     |
| 8.4      | Were more deviations found than expected?                                                                       | 8.5        | **Conclude** for the sampled population and strata.               |
| 8.5      | Has the sample been expanded, or the deviation cause established across the population?                         | **Conclude** with deviation rate and cause. | Criterion **undetermined** (UNKNOWN) or **not met**, per §II decision rules. |

## DT-09 Interview corroboration

| **Node** | **Test**                                                                                          | **If yes** | **If no**                                                                 |
|----------|---------------------------------------------------------------------------------------------------|------------|---------------------------------------------------------------------------|
| 9.1      | Is the statement decisive for a criterion?                                                         | 9.2        | **Use as context**.                                                       |
| 9.2      | Does the statement describe actual practice (not intended or documented practice)?                  | 9.3        | **Use as DESIGN or intent evidence only**.                                |
| 9.3      | Is the claim type DESIGN?                                                                          | **Use** with documentary support. | 9.4                                              |
| 9.4      | Is the statement corroborated by evidence of another class (E2, E3 or E4)?                          | **Use** as corroborated evidence. | Criterion **undetermined**; request corroborating evidence. |

## DT-10 Site-inspection safety

| **Node** | **Test**                                                                                          | **If yes** | **If no**                                    |
|----------|---------------------------------------------------------------------------------------------------|------------|----------------------------------------------|
| 10.1     | Are induction, permits, escort and the approved route complete?                                     | 10.2       | **Stop** until complete.                     |
| 10.2     | Does the inspection enter an area with energised equipment, hazardous fluids, battery or refrigerant hazards, or confined space? | 10.3 | **Proceed** (observation only). |
| 10.3     | Are the required PPE, approach boundaries and the area authority's approval in place?               | **Proceed** (observation only; no operation of equipment). | **Stop**; record inaccessible scope (UNKNOWN U2). |
| 10.4     | (During inspection) Has an unexpected alarm, unsafe condition or unplanned plant state occurred?    | **Withdraw** from the area; notify the safety authority; record in WP-08. | Continue. |

## DT-11 Testing authorisation

| **Node** | **Test**                                                                                                         | **If yes** | **If no**                                                       |
|----------|------------------------------------------------------------------------------------------------------------------|------------|-----------------------------------------------------------------|
| 11.1     | Can the proposition be established non-intrusively (DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS of existing E4 records)? | **Use non-intrusive method**. | 11.2                                          |
| 11.2     | Could the test affect power, cooling, fire and life-safety systems, control systems or production workloads?      | 11.3       | 11.4                                                            |
| 11.3     | Are capability-owner and safety-authority approvals, method statement, initial state, abort criteria and restoration plan in place? | 11.4 | **Stop**: do not test; record UNKNOWN (U5 or U8) or narrow the claim. |
| 11.4     | Will an authorised operator execute the test, with the assessor observing?                                       | **Proceed**. | **Stop**.                                                     |
| 11.5     | (During test) Is an abort criterion met, or has the plant deviated from the initial state?                        | **Abort**; restore; record in WP-11. | Continue to completion.               |

## DT-12 Control result

Apply per control, per claim type, per scope, after DT-05 to DT-07. Results feed the AIDCF-010 gate roll-up rule through the registry `gateMappings`; a result is recorded once and its effect is applied only through DT-15 and DT-19.

| **Node** | **Test**                                                                                               | **If yes**                  | **If no**  |
|----------|--------------------------------------------------------------------------------------------------------|-----------------------------|------------|
| 12.1     | Is the control applicable and assigned this claim type (DT-04)?                                         | 12.2                        | **NOT_APPLICABLE**, or not concluded for this claim type. |
| 12.2     | Has the assessment procedure been performed?                                                           | 12.3                        | **NOT_ASSESSED**. |
| 12.3     | Is any assessment criterion demonstrated materially not met, or a safeguard demonstrated ineffective?   | **NONCONFORMING**; raise Finding. | 12.4 |
| 12.4     | Is the prerequisite claim for the same control and scope NONCONFORMING (§II.1)?                          | **NONCONFORMING** for this claim; raise Finding. | 12.5 |
| 12.5     | Is evidence for every criterion at or above the evidence-profile quality and sufficiency floors?         | 12.6                        | 12.7 |
| 12.6     | Are all criteria met?                                                                                   | **CONFORMING**; assign confidence. | **PARTIAL**; raise a Finding for each unmet element. |
| 12.7     | Is any criterion evidenced as partly unmet?                                                            | **PARTIAL**; raise Finding, and UNKNOWN Record for the undetermined criteria. | **UNKNOWN**; raise UNKNOWN Record (severity per DT-17). |

Insufficient evidence produces UNKNOWN, never a reduced score (AIDCF-010: the evidence multiplier is removed).

## DT-13 Failure path

| **Node** | **Test**                                                                                                 | **If yes** | **If no**                                                                 |
|----------|----------------------------------------------------------------------------------------------------------|------------|---------------------------------------------------------------------------|
| 13.1     | Is each segment of the path (initiating condition, propagation, safeguard, residual state) evidenced?     | 13.2       | Record as **candidate path**; UNKNOWN for unevidenced segments. Connectivity alone does not establish reachability, authority or effect. |
| 13.2     | Do the safeguards on the path depend on a resource that the initiating condition also removes (common mode)? | Record **common-mode exposure**; raise Finding; evaluate CG-09. | 13.3 |
| 13.3     | Does the residual state stay within Service Outcome tolerance for the scenario?                          | 13.4       | Raise **Finding** (outcome breach); evaluate CG-09 and CG-10.             |
| 13.4     | Is recovery to the outcome tolerance evidenced end-to-end?                                               | **Scenario supported** within evidenced conditions. | UNKNOWN for recovery; evaluate CG-10. |

## DT-14 Gate applicability

| **Node** | **Test**                                                                                                 | **If yes** | **If no**                                                        |
|----------|----------------------------------------------------------------------------------------------------------|------------|------------------------------------------------------------------|
| 14.1     | Is the gate one of CG-11 or CG-12 (meta-gates)?                                                           | **In scope** for every assessment at AL2 or higher. | 14.2                     |
| 14.2     | Is any gate scope element (AIDCF-010 gate specification) present within the assessment boundary?          | **In scope**; collect mapped controls (DT-15). | 14.3                           |
| 14.3     | Does an approved boundary rationale meet the gate's APPROVED_NA conditions in AIDCF-010?                  | **APPROVED_NA**. | **In scope**; absence of the scope element is itself evidenced as part of the gate evaluation. |

## DT-15 Gate result

Apply per in-scope gate after all mapped controls have results. This tree is the AIDCF-010 Part VIII roll-up rule expressed as nodes.

| **Node** | **Test**                                                                                                         | **If yes**             | **If no** |
|----------|------------------------------------------------------------------------------------------------------------------|------------------------|-----------|
| 15.1     | Has the gate been evaluated?                                                                                     | 15.2                   | **NOT_ASSESSED** (UNKNOWN ceiling applies in DT-19 step 1). |
| 15.2     | Is any in-scope CRITICAL control NONCONFORMING or PARTIAL, or a gate criterion demonstrated not met?               | **FAIL**               | 15.3      |
| 15.3     | Is any in-scope CRITICAL control UNKNOWN or NOT_ASSESSED, gate evidence below the floor, or a US4 UNKNOWN attached? | **UNKNOWN**           | 15.4      |
| 15.4     | Are all CRITICAL controls CONFORMING at the required claim type and all gate criteria met with evidence at floor?   | 15.5                   | **UNKNOWN** (record which element is unestablished) |
| 15.5     | Does every NONCONFORMING SUPPORTING control have an approved gate-level evaluation concluding no defeat?          | **PASS**               | **UNKNOWN** until evaluated, or **FAIL** if the evaluation concludes defeat. |

There is no conditional gate result. PARTIAL never yields PASS.

## DT-16 Finding

| **Node** | **Test**                                                                                           | **If yes**                          | **If no**                          |
|----------|----------------------------------------------------------------------------------------------------|-------------------------------------|------------------------------------|
| 16.1     | Is there an evidenced variance from a stated criterion?                                             | 16.2                                | **Observation** or **Improvement opportunity** (AIDCF-012 Part IX); no result effect. |
| 16.2     | Does the variance cause a gate FAIL, or defeat a Service Outcome tolerance?                          | **Critical finding**                | 16.3                               |
| 16.3     | Is the control result NONCONFORMING, or does the variance affect a SUPPORTING-mapped control requiring gate-level evaluation? | **Significant weakness** | 16.4                          |
| 16.4     | Is the control result PARTIAL?                                                                      | **Weakness**                        | Re-check DT-12; a variance with a CONFORMING result is an Observation. |

## DT-17 UNKNOWN severity

Apply top-down; the first "yes" sets the severity (AIDCF-010 Part IX; AIDCF-008 §35A gives per-type guidance). The effect is applied once, in DT-19 step 2.

| **Node** | **Test**                                                                                          | **If yes**                                                                   | **If no** |
|----------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------|
| 17.1     | Does it concern the boundary, the Capability Instance, a Service Outcome or tolerance definition, or could its resolution change two or more gates? | **US5 Systemic**: decision ≤ INCONCLUSIVE for affected outcomes. | 17.2 |
| 17.2     | Does it concern a CRITICAL-mapped control at a mandatory claim type, or evidence for a gate criterion?  | **US4 Critical**: gate → UNKNOWN; decision ≤ LIMITED, or the gate's UNKNOWN ceiling if lower. | 17.3 |
| 17.3     | Could its resolution change any control result or a decision condition?                            | **US3 Material**: decision ≤ CONDITIONALLY_ASSURED; condition recorded.      | 17.4      |
| 17.4     | Could its resolution change the confidence recorded for a claim?                                   | **US2 Moderate**: confidence ceiling CONF-2 for affected claims.             | **US1 Low**: record only. |

## DT-18 Independent review

| **Node** | **Test**                                                                                                    | **If yes**   | **If no**                         |
|----------|-------------------------------------------------------------------------------------------------------------|--------------|-----------------------------------|
| 18.1     | Is the reviewer independent of every preparation role in the assessment and free of unmanaged conflicts?     | 18.2         | **Stop**; appoint another reviewer. |
| 18.2     | Do sampled material statements trace to Control Assessments, Gate Results, Findings, UNKNOWN Records and Evidence Objects (Part A A7)? | 18.3 | **Return** to lead assessor. |
| 18.3     | Are every FAIL or UNKNOWN gate and every US4/US5 UNKNOWN reviewed, including severity grading?               | 18.4         | **Return**.                       |
| 18.4     | Does the Decision Recommendation equal the maximum permissible state from the AIDCF-010 derivation (DT-19)?  | 18.5         | **Return** with recorded challenge. |
| 18.5     | Does the proposed wording match AIDCF-012 Part V for that state, with all mandatory disclosures?             | **Proceed** to decision authority. | **Return**.             |

## DT-19 Assurance decision

This tree is the AIDCF-010 Part XII derivation order (gates → UNKNOWN severity → coverage → bands → conditions and confidence), run per Service Outcome. Each step can only lower the ceiling. Ranking: REASONABLY_ASSURED > CONDITIONALLY_ASSURED > LIMITED > INCONCLUSIVE > NOT_ASSURED. Start each outcome at REASONABLY_ASSURED.

| **Step** | **Test**                                                                                          | **Effect on ceiling**                                                                                       |
|----------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| 19.0     | Is the assessment AL2 or higher, CG-01 evaluated and the in-scope gate set fixed?                  | If no: **no decision issued** (AIDCF-012 V.3); stop.                                                         |
| 19.1     | Gates: for each in-scope gate, is the result FAIL, UNKNOWN or NOT_ASSESSED?                        | FAIL → apply the gate's FAIL ceiling; UNKNOWN or NOT_ASSESSED → apply the gate's UNKNOWN ceiling (AIDCF-010 Part VIII). |
| 19.2     | UNKNOWN severity: is any US5, US4, US3 or US2 UNKNOWN affecting the outcome?                       | US5 → ≤ INCONCLUSIVE; US4 → ≤ LIMITED (or the gate ceiling if lower); US3 → ≤ CONDITIONALLY_ASSURED with condition; US2 → confidence ceiling CONF-2. |
| 19.3     | Coverage: is capability coverage of mandatory control results below 50%, below 80%, or is any relevant domain below 80%? | < 50% → ≤ INCONCLUSIVE; < 80% → ≤ LIMITED; relevant domain < 80% → ≤ CONDITIONALLY_ASSURED with coverage condition. |
| 19.4     | Bands: what is the lowest reported band for the outcome (CAI and relevant domains)?                 | B5, B4 → none; B3 → ≤ CONDITIONALLY_ASSURED; B2 → ≤ LIMITED; B1 → ≤ NOT_ASSURED. Withheld bands have already acted through 19.2 and 19.3. |
| 19.5     | Conditions and confidence: is any Significant weakness open, or decision confidence below CONF-3 or CONF-2? | Significant weakness → ≤ CONDITIONALLY_ASSURED with condition; confidence < CONF-3 → ≤ CONDITIONALLY_ASSURED; < CONF-2 → ≤ LIMITED. |
| 19.6     | Recommendation: what is the lowest ceiling across outcomes (unless the question is partitioned by outcome)? | **Decision Recommendation** at that state, with controlling reasons in step order, prohibited higher states and conditions. |
| 19.7     | After independent review (DT-18), does the decision authority select a state no higher than the recommendation? | **Decision APPROVED** at the selected state; rationale recorded if lower. | 

A request to exceed the recommendation is refused and recorded (AIDCF-010).

## DT-20 Reassessment

| **Node** | **Test**                                                                                                   | **If yes**                                          | **If no** |
|----------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|-----------|
| 20.1     | Has a material change, incident, evidence expiry, Gate Result change or Service Outcome change occurred?    | 20.2                                                | **Maintain** ACTIVE; record the review. |
| 20.2     | Does the trigger invalidate evidence for a decisive claim or a CRITICAL control?                            | Set lifecycle **SUSPENDED** for affected scope; 20.3 | 20.3     |
| 20.3     | Is the affected scope bounded to identified controls and gates?                                             | **Delta reassessment** of affected controls and gates. | **Full reassessment**. |
| 20.4     | After reassessment, does the decision state or a condition change?                                          | New decision that **SUPERSEDES** the prior one.     | **Reinstate** ACTIVE with recorded reassessment. |
| 20.5     | Is reliance no longer defensible and reassessment not possible within the validity period?                  | **WITHDRAWN**                                       | —         |
| 20.6     | Has the validity end passed without reassessment?                                                           | **EXPIRED**                                         | —         |

# Part II — Generic assessment protocol per claim type

## II.1 Principles

A control is a distinct topic: MCF-POW-010 (Battery Condition) and MCF-POW-011 (Runtime and Derating) are different controls with different criteria, not different lifecycle views of one topic. Each control is assessed for one or more **claim types** (DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS, RESILIENCE), and a result is recorded per control, per claim type, per scope. The protocol in this Part says, for each claim type, what the assessor does, what evidence is needed, how to sample and how to decide. The control-specific steps and criteria come from the AIDCF-007A registry (§II.9).

Claim prerequisites for the same control and scope:

| **Claim type**  | **Prerequisite claim** | **Rule**                                                                                                                                                             |
|-----------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DESIGN          | —                      | —                                                                                                                                                                     |
| IMPLEMENTATION  | DESIGN                 | Reconciliation needs an approved design baseline. If DESIGN is NONCONFORMING, IMPLEMENTATION cannot be CONFORMING.                                                    |
| OPERATION       | IMPLEMENTATION         | Operation is of the implemented control. If IMPLEMENTATION is NONCONFORMING, OPERATION cannot be CONFORMING.                                                          |
| EFFECTIVENESS   | IMPLEMENTATION         | The tested configuration must be the implemented one. OPERATION evidence is recommended but not a prerequisite (for example at commissioning).                         |
| RESILIENCE      | IMPLEMENTATION, and EFFECTIVENESS of the safeguards relied on in the scenario | Recovery claims rely on safeguards that work; where those safeguards' EFFECTIVENESS is UNKNOWN, RESILIENCE is at most UNKNOWN. |

Where a prerequisite is UNKNOWN or NOT_ASSESSED, the higher claim may still be determined if its own evidence independently establishes the prerequisite facts (for example, a witnessed test that records the configuration under test); otherwise the higher claim is UNKNOWN.

**AMH-REQ-068** Each control shall be assessed separately for each assigned claim type using the protocol for that claim type in §II.3–§II.7 together with the control's registry `assessmentProcedure` and `assessmentCriteria`; a single result shall not be recorded for several claim types.

**AMH-REQ-069** A claim shall not be recorded as CONFORMING where its prerequisite claim for the same control and scope is NONCONFORMING, and shall be UNKNOWN where the prerequisite is UNKNOWN or NOT_ASSESSED unless the claim's own evidence independently establishes the prerequisite facts.

## II.2 Common protocol steps and sampling

Steps applied for every control and claim type:

| **Step** | **Action**                                                                                                                                                      |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P1       | Retrieve the registry record: requirement, `assessmentCriteria`, `assessmentProcedure`, `evidenceProfile` for the claim type, `parameters`, `gateMappings`, `unknownRule`, `testingSafety`. |
| P2       | Bind scope: subject instances, boundary, operating states and period for this claim.                                                                            |
| P3       | Confirm the prerequisite claim status (§II.1).                                                                                                                  |
| P4       | Request evidence against the evidence profile (classes, quality floor, sufficiency floor, state coverage, period coverage, independence, mandatory items).        |
| P5       | Evaluate evidence (DT-05 to DT-07; AIDCF-008 quality and sufficiency). If a mandatory item is missing or below floor and no acceptable alternative exists, the affected criteria are undetermined. |
| P6       | Perform the registry `assessmentProcedure` steps using the claim-type protocol below and the methods in `assessmentMethods`.                                    |
| P7       | Conclude each `assessmentCriteria` item as met, not met or undetermined, with evidence references.                                                              |
| P8       | Apply the claim-type decision rules (DT-12); assign confidence; raise Findings and UNKNOWN Records (severity per DT-17); record gate effect from `gateMappings`.  |

**Sampling parameters.** Where a criterion is tested over a population (assets, configuration items, work orders, access events, alarms, changes), the sample plan (WP-09) declares: population and source; strata; confidence level *c*; tolerable deviation rate *p*; expected deviations. For acceptance sampling with zero expected deviations, the minimum sample size is

n = ⌈ ln(1 − c) / ln(1 − p) ⌉

which follows from the binomial probability of observing no deviations. Illustrative values (programme parameters; illustrative only): *c* = 0.95, *p* = 0.10 gives n = 29; *c* = 0.90, *p* = 0.10 gives n = 22; *c* = 0.95, *p* = 0.05 gives n = 59. For finite populations this is conservative. Where the population is smaller than n, the whole population is tested.

**AMH-REQ-070** Items that are the subject of a CRITICAL gate mapping for CG-04, CG-05 or CG-06 shall be tested in full (100%) unless the technical reviewer approves a documented engineering rationale for sampling.

**AMH-REQ-071** Where a sample yields more deviations than expected, the assessor shall either expand the sample or establish the deviation cause across the population before concluding; a criterion shall not be concluded as met on the basis of a sample containing an unexplained deviation in a CRITICAL-mapped population.

## II.3 DESIGN claims

**Asserts.** The requirement and the approved design are adequate for the Service Outcome in every declared operating state. Minimum Assurance Level AL2.

**What the assessor does.**

1. Identify the approved design artefacts for the control subject (for example single-line diagram, P&ID, fabric topology, policy, procedure, architecture decision) and confirm approval, version and currency.
2. Establish the design basis: the Service Outcome tolerances, demand and envelope parameters the design must satisfy (Part A WP-02), including DEGRADED and MAINTENANCE states.
3. Verify that the design addresses each `assessmentCriteria` item; for quantitative criteria, verify that a competent analysis (calculation, model, study) shows the design meets the parameter with its declared margin, using derated rather than nameplate capacities.
4. Check that assumptions, dependencies and exclusions are stated and consistent with the dependency baseline.
5. Check design governance: the design authority and the process for approving deviations.

**Evidence.** E1 design documentation plus E7 competent technical analysis; E5 independent design review where required by authority or consequence (AIDCF-008 §29). Typical profile tier CP-1 or CP-2; sufficiency floor per registry (commonly S2–S3).

**Sampling.** Decisive design artefacts are reviewed in full. Where a design is replicated (for example one rack or row design used across a hall), each distinct design type is reviewed and the replication is confirmed by IMPLEMENTATION assessment.

**Decision rules.**

| **Result**     | **Condition**                                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| CONFORMING     | Approved, current design addresses every criterion for every in-scope state, with competent analysis demonstrating each quantitative parameter is met.    |
| PARTIAL        | Design addresses some criteria or states; each gap is a Finding (for example maintenance state not designed for).                                         |
| NONCONFORMING  | Design demonstrably cannot meet a criterion (for example calculated capacity below required demand at design condition), or no design exists where one is required. |
| UNKNOWN        | Design exists but approval, currency or analysis cannot be established, or design versions conflict.                                                     |

**Common defects.** Design to nameplate rather than derated capacity; ambient design conditions not stated; maintenance or degraded states not addressed; single-point dependencies introduced by shared controllers or routes; design assumptions unowned.

## II.4 IMPLEMENTATION claims

**Asserts.** The as-built or configured state reconciles to the approved design. Minimum Assurance Level AL3.

**What the assessor does.**

1. Define the reconciliation set: design attributes that must be observable in the implemented state (topology, ratings, settings, versions, labels, segregation).
2. Obtain the implemented state from authorised sources (configuration extracts with extraction context, as-built records, inspection) — Part A B8 and B10.
3. Reconcile design to implemented state item by item; classify each difference as approved deviation, temporary configuration within validity, or unapproved deviation.
4. For unapproved deviations, evaluate the effect on the design intent and the Service Outcome.
5. Verify that commissioning or acceptance evidence relates to the current implemented state, not an earlier configuration.

**Evidence.** E2 configuration or as-built evidence plus E3 or E6 observation, reconciled to design (AIDCF-008 §29). Typical tier CP-2; sufficiency commonly S3.

**Sampling.** Population = implemented instances of the design attributes. Where configuration can be extracted automatically, reconcile 100%. Otherwise sample per §II.2, stratified by hall, system, age and change history; include all items changed since the last baseline.

**Decision rules.**

| **Result**     | **Condition**                                                                                                                         |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| CONFORMING     | No unapproved deviation in the reconciled population (or sample, with no unexplained deviation), and temporary configurations are within validity. |
| PARTIAL        | Unapproved deviations exist that do not defeat the design intent; each is a Finding.                                                    |
| NONCONFORMING  | A deviation defeats the design intent (for example a designed dual path implemented as a single path; a protection setting outside the approved coordination study), or the deviation rate exceeds the tolerable rate. |
| UNKNOWN        | Implemented state cannot be obtained, extraction context is unknown, or the population cannot be reconciled for completeness.            |

**Common defects.** As-built records not updated after change; temporary bypasses left in place; configuration drift between nominally identical systems; labels not matching drawings.

## II.5 OPERATION claims

**Asserts.** The control operates as intended over a representative period and in the declared operating states. Minimum Assurance Level AL4.

**What the assessor does.**

1. Define the operating period and the occurrences that demonstrate operation (for example alarms raised and handled, maintenance completed, access reviews performed, changes approved, telemetry within limits).
2. Confirm monitoring and record-source health over the period (Part A B12): gaps, clock integrity, data loss.
3. Sample occurrences (§II.2) and verify each was performed as designed, by an authorised person, within the required time.
4. Review exceptions, incidents and near misses in the period and how the control responded.
5. Confirm that the period includes the in-scope operating states (for example at least one MAINTENANCE occurrence where MAINTENANCE is in scope).

**Evidence.** E3 operational evidence over the representative period, plus current E2 and exception and incident review (AIDCF-008 §29). Typical tier CP-3; sufficiency commonly S3–S4.

**Period.** Defined by the evidence profile `periodCoverage`. Where the profile does not state one, the capability profile sets it as a parameter (illustrative default: the longer of 90 days and one full cycle of the control's periodic activity).

**Decision rules.**

| **Result**     | **Condition**                                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------------------------------------|
| CONFORMING     | Sampled occurrences performed as designed; exceptions handled; monitoring gaps immaterial; in-scope states represented.            |
| PARTIAL        | Occurrences generally performed but with deviations that did not defeat the objective (for example late reviews); each is a Finding. |
| NONCONFORMING  | The control did not operate when required (for example alarms unacknowledged during an event, maintenance not performed, unauthorised access not detected), or the deviation rate exceeds the tolerable rate. |
| UNKNOWN        | Record sources incomplete for the period, an in-scope state not represented (UNKNOWN type U5), or the population of occurrences cannot be established. |

**Common defects.** Monitoring blind spots during maintenance; records of activity without evidence of outcome; operation demonstrated only in NORMAL state; exceptions closed without root cause.

## II.6 EFFECTIVENESS claims

**Asserts.** The control achieves its objective under tested or observed adverse conditions. Minimum Assurance Level AL5.

**What the assessor does.**

1. State the proposition as a measurable acceptance criterion from the control's `parameters` (for example transfer completes within the declared time at the declared load; leak detected and isolated before a declared volume; alert raised within a declared time of a fault).
2. Select evidence: an authorised test (Part A B13) or an observed real event with instrumentation sufficient to measure the criterion.
3. Confirm that the configuration under test is the implemented one (prerequisite, §II.1).
4. Execute or observe; record initial state, conditions achieved, measurements, anomalies and post-state (WP-10, WP-11).
5. Compare achieved conditions with the claimed conditions (load, duration, states, failure modes); untested claimed conditions are coverage gaps.

**Evidence.** E4 representative validation plus E2 and E3 supporting state and operating evidence (AIDCF-008 §29). Typical tier CP-4; sufficiency commonly S4.

**Sampling.** Tests are selected by failure mode and condition rather than statistically; each claimed failure mode and condition needs at least one representative test or instrumented observed event. Repeated identical units may be represented by a sample where implementation reconciliation (§II.4) shows they are identical.

**Decision rules.**

| **Result**     | **Condition**                                                                                                                                       |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| CONFORMING     | The acceptance criterion was met for every claimed condition, or the claim scope has been formally narrowed to the tested conditions and the narrowing disclosed. |
| PARTIAL        | Criterion met with deviations that did not defeat the objective (for example alarm raised but routed to the wrong team); each is a Finding.             |
| NONCONFORMING  | The acceptance criterion was not met under a claimed condition.                                                                                       |
| UNKNOWN        | No representative test or observed event exists for a claimed condition, instrumentation was insufficient, or the configuration under test cannot be shown to be the implemented one. |

A retest after remediation produces a new result; the original result is retained in history.

**Common defects.** Tests at partial load extrapolated to full load; tests that bypass the control under test; success declared without measured timing; tests performed on a configuration since changed.

## II.7 RESILIENCE claims

**Asserts.** The control contains failure and supports recovery of the Service Outcome within tolerance. Minimum Assurance Level AL5.

**What the assessor does.**

1. Select the failure scenarios the control is claimed to contain or recover from (Part A C2; AIDCF-004), including cross-domain and common-mode scenarios.
2. For containment, verify that the fault does not propagate beyond the declared fault domain: the isolation mechanism, its dependencies and evidence that it acts.
3. For recovery, measure end-to-end restoration of the Service Outcome (not only of the component), including recovery dependencies (power, cooling, control plane, identity, time, storage, spares, people).
4. Use integrated scenario tests or exercises (SCENARIO_EXERCISE), instrumented incidents, or reperformance of recovery steps; tabletop exercises support DESIGN of recovery, not RESILIENCE results.
5. Compare achieved recovery time and recovery point with the Service Outcome tolerances for each scenario.

**Evidence.** E4 scenario or recovery evidence plus cross-domain E2 and E3 and dependency coverage (AIDCF-008 §29). Typical tier CP-5; sufficiency commonly S5.

**Decision rules.**

| **Result**     | **Condition**                                                                                                                                  |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| CONFORMING     | For every claimed scenario, containment held within the declared fault domain and the Service Outcome was restored within tolerance with recovery dependencies available. |
| PARTIAL        | Containment and recovery within tolerance, but reliant on undocumented steps, unavailable-by-design resources or individual knowledge; each is a Finding. |
| NONCONFORMING  | Propagation beyond the fault domain, or recovery outside tolerance, for a claimed scenario.                                                      |
| UNKNOWN        | A claimed scenario not exercised end-to-end, recovery dependencies unverified, or safeguards relied on have UNKNOWN EFFECTIVENESS.               |

**Common defects.** Component restored but outcome not (for example power restored but job restart blocked by unavailable identity or storage metadata services); recovery sequencing untested across domains; recovery depending on the failed fault domain.

## II.8 Recording, confidence and gate effect

**AMH-REQ-072** Each `assessmentCriteria` item shall be concluded individually as met, not met or undetermined, with evidence references, before the control result is assigned.

**AMH-REQ-073** Confidence shall be assigned to every CONFORMING, PARTIAL and NONCONFORMING result using the AIDCF-008 confidence states, shall not exceed the ceiling set by any US2 or higher UNKNOWN Record affecting the claim, and shall be CONF-0 for an UNKNOWN result.

**AMH-REQ-074** The gate effect of each result shall be taken from the registry `gateMappings` (CRITICAL or SUPPORTING) and recorded on the Control Assessment; the assessor shall not infer gate mappings from the domain of the control.

**AMH-REQ-075** Where a claim scope is narrowed to the conditions actually evidenced, the narrowing shall be approved by the technical reviewer, recorded as a limitation (WP-17) and disclosed in the Assurance Decision.

## II.9 Where control-specific procedures, criteria and evidence profiles are carried

Control-specific assessment content is not reproduced in AIDCF-009. It is carried in two places:

| **Source**                                    | **Content**                                                                                                                                                         |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AIDCF-007A Canonical Master Control Registry v1.1 (standards/aidcf-007a/registry/) | Per control: `objective`, `requirement`, `assessmentCriteria` (3–7 independently testable criteria), `assessmentProcedure` (3–8 ordered control-specific steps), `assessmentMethods`, `parameters`, `minimumEvidence`, `evidenceProfile` (claimType, profileTier, requiredClasses, optionalClasses, qualityFloor, sufficiencyFloor, stateCoverage, periodCoverage, independence, mandatoryItems, acceptableAlternatives, unknownEffect, reassessmentTriggers), `requiredAssuranceLevel`, `gateMappings`, `failureModes`, `testingSafety`, `unknownRule`, `applicability`. |
| AIDCF-018 domain guides (standards/aidcf-018-domain-guides/), one per domain: AIDCF-018-<DOM> | Engineering context, typical architectures and failure modes, interpretation of criteria, worked evidence examples and testing practice for the domain.               |

**AMH-REQ-076** The assessor shall use the registry version declared in the charter as the sole source of control-specific criteria, procedures and evidence profiles; a domain guide may elaborate but shall not add or remove criteria.

## II.10 Index of families, registry ranges and domain guides

| **Family** | **Title** | **Registry controls** | **Domain guide** |
|------------|-----------|-----------------------|------------------|
| GOV-01 | Governance architecture | MCF-GOV-001 to MCF-GOV-004 | AIDCF-018-GOV |
| GOV-02 | Accountability and responsibility | MCF-GOV-005 to MCF-GOV-008 | AIDCF-018-GOV |
| GOV-03 | Policy and standards management | MCF-GOV-009 to MCF-GOV-012 | AIDCF-018-GOV |
| GOV-04 | Risk and assurance governance | MCF-GOV-013 to MCF-GOV-016 | AIDCF-018-GOV |
| GOV-05 | Stakeholder and regulatory interface | MCF-GOV-017 to MCF-GOV-020 | AIDCF-018-GOV |
| GOV-06 | Ethics, impartiality and competence | MCF-GOV-021 to MCF-GOV-024 | AIDCF-018-GOV |
| CAP-01 | Capability inventory | MCF-CAP-001 to MCF-CAP-004 | AIDCF-018-CAP |
| CAP-02 | Service outcome definition | MCF-CAP-005 to MCF-CAP-008 | AIDCF-018-CAP |
| CAP-03 | Criticality and materiality | MCF-CAP-009 to MCF-CAP-012 | AIDCF-018-CAP |
| CAP-04 | Demand and growth modelling | MCF-CAP-013 to MCF-CAP-016 | AIDCF-018-CAP |
| CAP-05 | Operating envelope | MCF-CAP-017 to MCF-CAP-020 | AIDCF-018-CAP |
| CAP-06 | Capability lifecycle and change | MCF-CAP-021 to MCF-CAP-024 | AIDCF-018-CAP |
| DEP-01 | Dependency discovery | MCF-DEP-001 to MCF-DEP-004 | AIDCF-018-DEP |
| DEP-02 | Shared and common-mode dependencies | MCF-DEP-005 to MCF-DEP-008 | AIDCF-018-DEP |
| DEP-03 | External providers and utilities | MCF-DEP-009 to MCF-DEP-012 | AIDCF-018-DEP |
| DEP-04 | Concentration and substitutability | MCF-DEP-013 to MCF-DEP-016 | AIDCF-018-DEP |
| DEP-05 | Boundary and interface control | MCF-DEP-017 to MCF-DEP-020 | AIDCF-018-DEP |
| DEP-06 | Dependency monitoring and review | MCF-DEP-021 to MCF-DEP-024 | AIDCF-018-DEP |
| PHY-01 | Site and location resilience | MCF-PHY-001 to MCF-PHY-004 | AIDCF-018-PHY |
| PHY-02 | Building and structural integrity | MCF-PHY-005 to MCF-PHY-008 | AIDCF-018-PHY |
| PHY-03 | Physical zoning and segregation | MCF-PHY-009 to MCF-PHY-012 | AIDCF-018-PHY |
| PHY-04 | Access and surveillance | MCF-PHY-013 to MCF-PHY-016 | AIDCF-018-PHY |
| PHY-05 | Asset movement and custody | MCF-PHY-017 to MCF-PHY-020 | AIDCF-018-PHY |
| PHY-06 | Fire, life safety and emergency interfaces | MCF-PHY-021 to MCF-PHY-024 | AIDCF-018-PHY |
| POW-01 | Utility and grid interface | MCF-POW-001 to MCF-POW-004 | AIDCF-018-POW |
| POW-02 | Generation and fuel | MCF-POW-005 to MCF-POW-008 | AIDCF-018-POW |
| POW-03 | UPS and energy storage | MCF-POW-009 to MCF-POW-012 | AIDCF-018-POW |
| POW-04 | Distribution and protection | MCF-POW-013 to MCF-POW-016 | AIDCF-018-POW |
| POW-05 | Power quality and transient response | MCF-POW-017 to MCF-POW-020 | AIDCF-018-POW |
| POW-06 | Electrical monitoring, maintenance and recovery | MCF-POW-021 to MCF-POW-024 | AIDCF-018-POW |
| THM-01 | Thermal architecture and capacity | MCF-THM-001 to MCF-THM-004 | AIDCF-018-THM |
| THM-02 | Air cooling systems | MCF-THM-005 to MCF-THM-008 | AIDCF-018-THM |
| THM-03 | Liquid cooling systems | MCF-THM-009 to MCF-THM-012 | AIDCF-018-THM |
| THM-04 | Heat rejection and water systems | MCF-THM-013 to MCF-THM-016 | AIDCF-018-THM |
| THM-05 | Fluid quality and leak management | MCF-THM-017 to MCF-THM-020 | AIDCF-018-THM |
| THM-06 | Thermal control, maintenance and recovery | MCF-THM-021 to MCF-THM-024 | AIDCF-018-THM |
| ENV-01 | Environmental operating conditions | MCF-ENV-001 to MCF-ENV-004 | AIDCF-018-ENV |
| ENV-02 | Energy performance | MCF-ENV-005 to MCF-ENV-008 | AIDCF-018-ENV |
| ENV-03 | Water performance | MCF-ENV-009 to MCF-ENV-012 | AIDCF-018-ENV |
| ENV-04 | Carbon and resource reporting | MCF-ENV-013 to MCF-ENV-016 | AIDCF-018-ENV |
| ENV-05 | Hazardous materials and waste | MCF-ENV-017 to MCF-ENV-020 | AIDCF-018-ENV |
| ENV-06 | Climate adaptation and resource continuity | MCF-ENV-021 to MCF-ENV-024 | AIDCF-018-ENV |
| CMP-01 | Compute architecture and configuration | MCF-CMP-001 to MCF-CMP-004 | AIDCF-018-CMP |
| CMP-02 | Cluster and scale-up domains | MCF-CMP-005 to MCF-CMP-008 | AIDCF-018-CMP |
| CMP-03 | Capacity, scheduling and utilisation | MCF-CMP-009 to MCF-CMP-012 | AIDCF-018-CMP |
| CMP-04 | Firmware, driver and compatibility | MCF-CMP-013 to MCF-CMP-016 | AIDCF-018-CMP |
| CMP-05 | Compute health and observability | MCF-CMP-017 to MCF-CMP-020 | AIDCF-018-CMP |
| CMP-06 | Compute lifecycle and recovery | MCF-CMP-021 to MCF-CMP-024 | AIDCF-018-CMP |
| STO-01 | Storage architecture and tiering | MCF-STO-001 to MCF-STO-004 | AIDCF-018-STO |
| STO-02 | Performance and capacity | MCF-STO-005 to MCF-STO-008 | AIDCF-018-STO |
| STO-03 | Integrity and consistency | MCF-STO-009 to MCF-STO-012 | AIDCF-018-STO |
| STO-04 | Protection and replication | MCF-STO-013 to MCF-STO-016 | AIDCF-018-STO |
| STO-05 | Checkpoint and recovery services | MCF-STO-017 to MCF-STO-020 | AIDCF-018-STO |
| STO-06 | Storage monitoring and lifecycle | MCF-STO-021 to MCF-STO-024 | AIDCF-018-STO |
| NET-01 | Scale-up and scale-out fabrics | MCF-NET-001 to MCF-NET-004 | AIDCF-018-NET |
| NET-02 | Performance and congestion control | MCF-NET-005 to MCF-NET-008 | AIDCF-018-NET |
| NET-03 | Storage and service networks | MCF-NET-009 to MCF-NET-012 | AIDCF-018-NET |
| NET-04 | Management and out-of-band networks | MCF-NET-013 to MCF-NET-016 | AIDCF-018-NET |
| NET-05 | Physical connectivity and optics | MCF-NET-017 to MCF-NET-020 | AIDCF-018-NET |
| NET-06 | Network control and observability | MCF-NET-021 to MCF-NET-024 | AIDCF-018-NET |
| OPS-01 | Operating model and staffing | MCF-OPS-001 to MCF-OPS-004 | AIDCF-018-OPS |
| OPS-02 | Procedure and work control | MCF-OPS-005 to MCF-OPS-008 | AIDCF-018-OPS |
| OPS-03 | Maintenance and reliability | MCF-OPS-009 to MCF-OPS-012 | AIDCF-018-OPS |
| OPS-04 | Alarm, incident and problem management | MCF-OPS-013 to MCF-OPS-016 | AIDCF-018-OPS |
| OPS-05 | Change and configuration management | MCF-OPS-017 to MCF-OPS-020 | AIDCF-018-OPS |
| OPS-06 | Capacity and service operations | MCF-OPS-021 to MCF-OPS-024 | AIDCF-018-OPS |
| RES-01 | Resilience strategy | MCF-RES-001 to MCF-RES-004 | AIDCF-018-RES |
| RES-02 | Fault-domain and containment design | MCF-RES-005 to MCF-RES-008 | AIDCF-018-RES |
| RES-03 | Continuity planning | MCF-RES-009 to MCF-RES-012 | AIDCF-018-RES |
| RES-04 | Recovery planning | MCF-RES-013 to MCF-RES-016 | AIDCF-018-RES |
| RES-05 | Testing and exercising | MCF-RES-017 to MCF-RES-020 | AIDCF-018-RES |
| RES-06 | Crisis and adaptive response | MCF-RES-021 to MCF-RES-024 | AIDCF-018-RES |
| SUP-01 | Supplier due diligence | MCF-SUP-001 to MCF-SUP-004 | AIDCF-018-SUP |
| SUP-02 | Contract and service obligations | MCF-SUP-005 to MCF-SUP-008 | AIDCF-018-SUP |
| SUP-03 | Hardware and component provenance | MCF-SUP-009 to MCF-SUP-012 | AIDCF-018-SUP |
| SUP-04 | Software, firmware and update supply | MCF-SUP-013 to MCF-SUP-016 | AIDCF-018-SUP |
| SUP-05 | Spares, logistics and obsolescence | MCF-SUP-017 to MCF-SUP-020 | AIDCF-018-SUP |
| SUP-06 | Remote support and third-party access | MCF-SUP-021 to MCF-SUP-024 | AIDCF-018-SUP |
| SEC-01 | Identity and privileged access | MCF-SEC-001 to MCF-SEC-004 | AIDCF-018-SEC |
| SEC-02 | Control-plane protection | MCF-SEC-005 to MCF-SEC-008 | AIDCF-018-SEC |
| SEC-03 | Network security and segmentation | MCF-SEC-009 to MCF-SEC-012 | AIDCF-018-SEC |
| SEC-04 | Configuration, vulnerability and patching | MCF-SEC-013 to MCF-SEC-016 | AIDCF-018-SEC |
| SEC-05 | Detection and response | MCF-SEC-017 to MCF-SEC-020 | AIDCF-018-SEC |
| SEC-06 | AI-enabled and automated action | MCF-SEC-021 to MCF-SEC-024 | AIDCF-018-SEC |
| EVA-01 | Evidence architecture | MCF-EVA-001 to MCF-EVA-004 | AIDCF-018-EVA |
| EVA-02 | Evidence provenance and quality | MCF-EVA-005 to MCF-EVA-008 | AIDCF-018-EVA |
| EVA-03 | Assessment planning and execution | MCF-EVA-009 to MCF-EVA-012 | AIDCF-018-EVA |
| EVA-04 | Findings, UNKNOWN and limitations | MCF-EVA-013 to MCF-EVA-016 | AIDCF-018-EVA |
| EVA-05 | Critical gates and decisions | MCF-EVA-017 to MCF-EVA-020 | AIDCF-018-EVA |
| EVA-06 | Reassessment and continuing assurance | MCF-EVA-021 to MCF-EVA-024 | AIDCF-018-EVA |

## II.11 Mapping from the previous Part II

The previous edition of this Part contained 360 procedures titled by lifecycle stage ("Design and governance", "Implementation and configuration", "Operation and monitoring", "Effectiveness, failure and recovery") with identical bodies within each family. Those titles did not match the control titles in the registry (for example MCF-POW-009 is "UPS Topology", not "Design and governance"). They are withdrawn. Each previous procedure ID MCF-<DOM>-NNN now resolves to the registry record for the same control ID, assessed per claim type using §II.3–§II.7.

# Part III — Site-inspection checklists by domain

## III.0 Common inspection protocol (applies to every checklist)

| **ID**   | **Inspection action**                                                                                      |
|----------|------------------------------------------------------------------------------------------------------------|
| INS-0-01 | Complete site induction; confirm the approved route, escort and stop authority (Part A B10, B14).           |
| INS-0-02 | Record location, subject, operating state at time of inspection and the boundary of what was inspected.     |
| INS-0-03 | Reconcile sampled assets and zones to the approved record (drawing, register or configuration).             |
| INS-0-04 | Record inaccessible scope, deviations, evidence IDs (photographs only where permitted) and follow-ups.       |
| INS-0-05 | Do not operate, open, switch, isolate or adjust equipment; observe authorised operators only.               |

Every domain item is recorded in WP-08 with: location; subject; operating state; observation; evidence ID; variance from record; follow-up action.

**AMH-REQ-077** Every adopted inspection checklist shall be applied together with the common protocol INS-0-01 to INS-0-05, and inaccessible scope shall be recorded as an UNKNOWN Record (type U2) linked to the affected controls.

## INS-GOV Governance, Accountability and Assurance Direction

| **ID**     | **Inspection point**                                                                                                    |
|------------|-------------------------------------------------------------------------------------------------------------------------|
| INS-GOV-01 | Control room and operations desk: escalation and delegation charts displayed match the approved delegation of authority. |
| INS-GOV-02 | Named duty manager and emergency decision authority can be identified for the current shift.                             |
| INS-GOV-03 | Controlled copies of policies and standards at point of use are the current approved versions.                           |
| INS-GOV-04 | Active exceptions or risk acceptances visible at site (temporary arrangements, signage) are on the exception register and within validity. |
| INS-GOV-05 | Evidence repositories referenced by governance records are accessible to the assessment under the agreed access rights.  |

## INS-CAP AI Capability, Service Outcome and Demand Management

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-CAP-01 | Installed racks, rows and halls in the Capability Instance match the capability register and architecture baseline.             |
| INS-CAP-02 | Rack nameplate and branch-circuit ratings at sampled positions are consistent with the demand model used for capacity.          |
| INS-CAP-03 | Live power and thermal dashboards show current load against the declared operating envelope and alarm limits.                  |
| INS-CAP-04 | Capacity reserved for maintenance or redundancy is not occupied by deployed load (no stranded or borrowed redundancy).         |
| INS-CAP-05 | Equipment staged for deployment is recorded as pending change, not counted as installed capacity.                              |

## INS-DEP Dependency, Concentration and External Reliance Management

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-DEP-01 | Utility, telecom and water points of entry: physical separation of nominally diverse feeds and routes matches the dependency baseline. |
| INS-DEP-02 | Demarcation points with providers are labelled and match the contracted responsibility split.                                   |
| INS-DEP-03 | Shared infrastructure items (common duct banks, shared risers, shared controller panels) are identified on the dependency record. |
| INS-DEP-04 | Third-party equipment on site (provider racks, metering, telemetry gateways) is registered with owner and access arrangements. |
| INS-DEP-05 | Alternative supply arrangements (fuel delivery access, alternative routes) are physically available as described.               |

## INS-PHY Physical Site, Building and Security Infrastructure

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-PHY-01 | Perimeter, vehicle access and loading areas match the site security design; observed weaknesses recorded without testing them. |
| INS-PHY-02 | Floor loading signage, raised-floor or slab condition and rack anchorage at sampled high-density positions match structural records. |
| INS-PHY-03 | Security, fire and water zone boundaries (doors, fire-stopping, bunds, drainage) are intact; penetrations sealed.                 |
| INS-PHY-04 | Access readers, surveillance coverage and alarm response points at critical rooms (electrical, battery, meet-me, control) are as designed. |
| INS-PHY-05 | Fire detection and suppression devices are unobstructed, in date for inspection, and cause-and-effect documentation is available at the panel. |
| INS-PHY-06 | Egress routes and emergency equipment are unobstructed, including in white space with liquid-cooling manifolds and overhead busway.     |

## INS-POW Electrical Power Infrastructure and Energy Continuity

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-POW-01 | Switchgear, transformer and distribution labelling matches the current single-line diagram; mimic diagrams are current.         |
| INS-POW-02 | Breaker positions and any bypass or tie arrangements observed match the declared operating state; temporary arrangements are tagged and recorded. |
| INS-POW-03 | Arc-flash labels and approach boundaries are present and consistent with the current study; PPE and access controls at energised equipment are in place. |
| INS-POW-04 | UPS and battery or BESS rooms: environmental conditions, ventilation, spill and thermal-runaway provisions and monitoring are as designed. |
| INS-POW-05 | Generators and fuel systems: fuel level indication, day-tank and transfer arrangements, and the generator control panel state are as recorded. |
| INS-POW-06 | EPMS displays at sampled points agree with local meter readings; communication-loss indicators are absent or recorded.          |

## INS-THM Cooling, Thermal and Fluid Infrastructure

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-THM-01 | Chillers, dry coolers or cooling towers: units in service match the declared state; units in maintenance are isolated and recorded. |
| INS-THM-02 | CDUs and secondary loops: pump status, filter differential pressure and supply/return temperatures are within declared limits; valve positions match P&ID. |
| INS-THM-03 | Quick-disconnects, manifolds and hoses at sampled racks show no signs of leakage, strain or damage; drip trays and leak sensors are in place. |
| INS-THM-04 | Air-side containment is intact (doors, blanking panels, cable brush seals); hot spots visible on dashboards are investigated.     |
| INS-THM-05 | Leak-detection zones and isolation valves are as shown on the leak management layout; isolation valves are accessible.         |
| INS-THM-06 | Water treatment and makeup arrangements (where present) are operating and recorded.                                            |

## INS-ENV Environmental and Resource Performance

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-ENV-01 | Temperature and humidity sensors at sampled inlet positions are placed as designed and readings agree with portable reference measurements where permitted. |
| INS-ENV-02 | Energy and water meters in the efficiency-metric boundary are installed, labelled and within calibration.                        |
| INS-ENV-03 | Hazardous material stores (batteries, refrigerants, coolants, fuel, suppressants) are labelled, segregated and have spill provisions. |
| INS-ENV-04 | Waste and decommissioned hardware or media awaiting disposal are in controlled, recorded storage.                               |
| INS-ENV-05 | Climate-adaptation provisions recorded in the risk assessment (flood barriers, elevated plant, heat-wave measures) are present. |

## INS-CMP AI Compute Infrastructure

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-CMP-01 | Sampled racks: node count, model and position match the asset register and cluster inventory.                                  |
| INS-CMP-02 | Rack-scale systems: power shelves, liquid connections and scale-up interconnect cabling match the approved rack configuration.   |
| INS-CMP-03 | Nodes flagged as failed, drained or awaiting RMA are physically identified and match the scheduler's unavailable set.            |
| INS-CMP-04 | Cluster management console shows firmware and driver versions for sampled nodes consistent with the approved baseline (observed, not extracted by the assessor). |
| INS-CMP-05 | Spares stock for accelerators, nodes and critical modules matches the spares register.                                         |

## INS-STO AI Storage and Data Infrastructure

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-STO-01 | Storage systems and tiers on site match the storage architecture (training data, checkpoint, model and artifact, archive).     |
| INS-STO-02 | Storage management console shows health, degraded components and rebuild status consistent with incident records.              |
| INS-STO-03 | Physical placement of replicas or immutable copies is in the declared separate fault domain (hall, power path, site).           |
| INS-STO-04 | Media awaiting sanitisation or destruction is in controlled custody with records.                                               |
| INS-STO-05 | Metadata servers and their power and network connections are on the paths declared in the design.                               |

## INS-NET AI Network and Interconnect Architecture

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-NET-01 | Sampled leaf, spine and rail connections match the fabric topology and cabling records.                                       |
| INS-NET-02 | Cable routing for nominally diverse paths uses physically separate trays or routes as designed.                                 |
| INS-NET-03 | Optics in sampled ports are of approved types; spare optics stock matches the register.                                       |
| INS-NET-04 | Management and out-of-band network equipment is powered from the declared paths and physically separate from production fabric equipment where designed. |
| INS-NET-05 | Cross-connects and meet-me room patching are labelled and match the cross-connect register.                                     |
| INS-NET-06 | Time-source equipment (for example GNSS receivers and grandmaster clocks, where used) is installed and monitored as designed.  |

## INS-OPS Building Operations and Service Management

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-OPS-01 | Shift staffing on site matches the roster and the minimum staffing in the operating model.                                     |
| INS-OPS-02 | Active permits to work and lockout/tagout points match the permit register; isolations are as recorded.                         |
| INS-OPS-03 | Alarm panel or console: standing alarms are known, recorded and within the rationalised alarm philosophy.                       |
| INS-OPS-04 | Shift handover record for the current shift is complete and reflects the observed plant state.                                  |
| INS-OPS-05 | Maintenance tags and calibration labels on sampled equipment match the maintenance system.                                     |
| INS-OPS-06 | Emergency operating procedures are available at point of use and are the current versions.                                     |

## INS-RES Resilience, Continuity and Recovery

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-RES-01 | Fault-domain boundaries declared in the resilience design (halls, power paths, cooling loops, fabric pods) are physically recognisable and labelled. |
| INS-RES-02 | Recovery resources (spares, tools, recovery media, printed recovery runbooks for loss-of-IT scenarios) are present where the recovery plan says. |
| INS-RES-03 | Crisis command location and alternative location are available and equipped as planned.                                       |
| INS-RES-04 | Evidence from the most recent exercise (logs, timings) is retained and accessible on site or in the repository.                 |
| INS-RES-05 | Alternative capacity relied on by the continuity plan exists and is in the state the plan assumes.                              |

## INS-SUP Supply Chain, OEM and Ecosystem Assurance

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-SUP-01 | Goods-in area: receipt inspection, quarantine of unverified components and chain-of-custody records are in operation.         |
| INS-SUP-02 | Sampled installed components carry identifiers traceable to approved sourcing records.                                         |
| INS-SUP-03 | Critical spares held by or for suppliers are at the declared locations and quantities.                                         |
| INS-SUP-04 | Remote-support equipment (vendor gateways, modems, cellular routers) on site is registered and in the declared activation state. |
| INS-SUP-05 | Vendor engineers on site are escorted and authorised in line with the support contract and access policy.                      |

## INS-SEC Digital, OT and Control-Plane Security

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-SEC-01 | BMS, EPMS, CDU and PLC engineering workstations: physical location, access control and logged-in sessions are as policy requires. |
| INS-SEC-02 | Network cabinets for OT and management networks are locked; no unregistered devices are connected at sampled ports.          |
| INS-SEC-03 | Break-glass credentials are held in the declared custody arrangement with access records.                                     |
| INS-SEC-04 | Remote-access gateways are physically present as designed and their status matches the access register.                       |
| INS-SEC-05 | Consoles that can issue commands to infrastructure display the operator identity and are not shared or unlocked when unattended. |
| INS-SEC-06 | Automation or agent control interfaces that can change infrastructure state are identified and their approval mechanisms observable. |

## INS-EVA Evidence, Assessment and Assurance Management

| **ID**     | **Inspection point**                                                                                                          |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| INS-EVA-01 | Evidence repository: access controls, integrity mechanisms and retention settings match the evidence management procedure.     |
| INS-EVA-02 | Sampled evidence manifests resolve to stored Evidence Objects with matching integrity references.                               |
| INS-EVA-03 | Finding, UNKNOWN and gate registers are current and show history for closed and superseded items.                               |
| INS-EVA-04 | Monitoring sources used for continuing assurance are operating and their health is recorded.                                   |
| INS-EVA-05 | Superseded decisions and reports are retained and marked as superseded.                                                        |

# Part IV — Evidence-collection playbooks linked to AIDCF-008

## IV.0 Fields common to all evidence classes

| **Field**        | **Requirement (all classes)**                                                                 |
|------------------|-----------------------------------------------------------------------------------------------|
| Evidence request | Assertion, subject, boundary, period, operating state, quality floor and sufficiency floor.   |
| Metadata         | Evidence ID, source, collector, custodian, classification, location, version, integrity reference. |
| Quality          | Rate P (provenance), F (fitness/relevance), C (coverage), R (reliability), T (timeliness), I (integrity) 0–5; derive quality band Q0–Q5. |
| Conflict         | Retain SUPPORTS, CHALLENGES and QUALIFIES links separately.                                   |
| UNKNOWN          | Create an UNKNOWN Record (U1–U10) when a mandatory item, source, integrity, coverage or method is unresolved. |
| Review           | Collector, assessor, technical reviewer and acceptance state.                                 |

**AMH-REQ-078** Each Evidence Object shall be used only within the claim-type boundary of its class shown in the playbooks below, unless corroborated by evidence of a class that supports the higher claim.

## IV.1 E1 Documentary and declarative

| **Field**        | **Class-specific requirement**                                                                          |
|------------------|---------------------------------------------------------------------------------------------------------|
| Examples         | Policies, standards, procedures, drawings, design studies, contracts, inventories, registers.          |
| Collection       | Confirm authority, approval, version, scope, effective date and supersession; obtain from the document-control system of record. |
| Use boundary     | Supports DESIGN claims and the intent element of other claims; does not on its own support IMPLEMENTATION, OPERATION, EFFECTIVENESS or RESILIENCE. |
| Typical defects  | Unapproved drafts; superseded versions in use; drawings not updated after change.                        |

## IV.2 E2 Configuration and technical state

| **Field**        | **Class-specific requirement**                                                                          |
|------------------|---------------------------------------------------------------------------------------------------------|
| Examples         | Device and controller configurations, protection settings, firmware and driver versions, topology exports, access-policy exports, manifests. |
| Collection       | Record authorised source, extraction method, extraction time, privilege used and baseline compared; prefer system-generated exports with integrity references. |
| Use boundary     | Supports IMPLEMENTATION (current state); contributes to OPERATION and EFFECTIVENESS as supporting state evidence. |
| Typical defects  | Extracts without context; partial exports; configuration of a lab or standby system supplied in place of production. |

## IV.3 E3 Operational and observational

| **Field**        | **Class-specific requirement**                                                                          |
|------------------|---------------------------------------------------------------------------------------------------------|
| Examples         | Telemetry, logs, alarm histories, work orders, incident records, access events, assessor observation.  |
| Collection       | Verify source health, clock synchronisation, period covered, gaps, filters and operating-state coverage. |
| Use boundary     | Supports OPERATION over the represented period and states; supports EFFECTIVENESS where an observed event is adequately instrumented. |
| Typical defects  | Gaps during incidents; filtered exports; time-zone or clock drift; aggregated data hiding transients.   |

## IV.4 E4 Validation and test

| **Field**        | **Class-specific requirement**                                                                          |
|------------------|---------------------------------------------------------------------------------------------------------|
| Examples         | Commissioning and integrated systems tests, functional tests, load-bank tests, failover tests, restore tests, exercises. |
| Collection       | Record authority, initial state, method, instrumentation, acceptance and abort criteria, results and restoration (WP-10, WP-11). |
| Use boundary     | Supports EFFECTIVENESS and RESILIENCE within the tested conditions only.                               |
| Typical defects  | Tests at reduced load; tests of a configuration since changed; pass recorded without measured values.  |

## IV.5 E5 Independent and third-party

| **Field**        | **Class-specific requirement**                                                                          |
|------------------|---------------------------------------------------------------------------------------------------------|
| Examples         | Independent audit and inspection reports, specialist reviews, witness statements, provider assurance reports. |
| Collection       | Confirm issuer competence, independence, scope, method, exclusions and currency; obtain the full report, not a summary. |
| Use boundary     | Corroboration within the issuer's scope; no inherited assurance beyond that scope and period.          |
| Typical defects  | Scope narrower than the claim; report period not covering the assessment period; carve-outs of the relevant subservice. |

## IV.6 E6 Human and experiential

| **Field**        | **Class-specific requirement**                                                                          |
|------------------|---------------------------------------------------------------------------------------------------------|
| Examples         | Interviews, walkthroughs, demonstrations, expert judgment.                                             |
| Collection       | Record role, objective, statements, handling, corroboration and contradictions (WP-07).                |
| Use boundary     | Context and practice; decisive statements require corroboration by another class for claims other than DESIGN. |
| Typical defects  | Description of intended practice reported as actual; single-person knowledge.                          |

## IV.7 E7 Derived and analytical

| **Field**        | **Class-specific requirement**                                                                          |
|------------------|---------------------------------------------------------------------------------------------------------|
| Examples         | Trend analyses, capacity and thermal models, query results, failure and dependency analyses.           |
| Collection       | Record sources, transformation, query or model version, assumptions and reviewer.                      |
| Use boundary     | Synthesis; cannot exceed the quality of its decisive sources; model outputs support DESIGN unless validated against measured data. |
| Typical defects  | Unvalidated models; undocumented assumptions; source data not retained.                                 |

# Part V — CG-01 to CG-15 gate evaluation workbooks

## V.0 Workbook structure (applies to every gate)

Each workbook is completed in WP-14 and contains: applicability (or APPROVED_NA rationale); the in-scope CRITICAL and SUPPORTING controls from the registry `gateMappings`; the AIDCF-010 gate criteria; mandatory evidence, classes and floor (AIDCF-008 Part XIII); operating states and scenarios evaluated; Findings and UNKNOWN Records; the Gate Result from the AIDCF-010 roll-up rule (DT-15) in canonical states PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED; the decision ceiling under AIDCF-010; closure requirements; technical and independent review. There is no conditional gate result.

**AMH-REQ-079** An adopted gate workbook shall record, for the gate, every in-scope CRITICAL control result at its required claim type, the gate-level evaluation of every NONCONFORMING SUPPORTING control, the evidence floor achieved and the operating states and scenarios evaluated.

Gate-specific content:

| **Gate** | **Scope protected**                                                                                                           | **Mandatory evidence (AIDCF-008)** | **Floor** | **Gate-specific evaluation questions**                                                                                                                                                              |
|----------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CG-01    | Capability Instance, Service Outcomes, tolerances, criticality and decision question defined, owned and approved.             | E1+E7                               | S3        | Is every outcome measurable with a tolerance and states? Is the owner accountable and the approval current? Is the decision question the one the outcomes answer?                                    |
| CG-02    | Assessment boundary, current architecture, as-built reconciliation, exclusions.                                                | E1+E2+E6                            | S3        | Does the architecture snapshot reconcile to as-built for decisive systems? Does any exclusion remove a material dependency? Are tenant and provider boundaries explicit?                              |
| CG-03    | Material internal and external dependencies, common mode and concentration identified and owned.                              | E1+E2+E7                            | S4        | Are recovery dependencies included? Are shared routes, controllers, firmware images and people identified? Does every material dependency have an owner and monitoring?                              |
| CG-04    | Fire, arc-flash and shock, hazardous fluids and chemicals, confined space, refrigerants, battery thermal runaway, safe work.    | E1+E4+E5                            | S4        | Are hazard studies current for the as-built state (for example arc-flash after protection changes)? Are battery and refrigerant hazards controlled? Are permits and isolation practices operating?       |
| CG-05    | Utility, distribution, UPS/BESS, generation, fuel, protection and power quality sufficient for the outcome across states.      | E1+E2+E3+E4                         | S5        | Is capacity sufficient with one path or unit unavailable? Do UPS, generation and protection tolerate AI load transients? Is fuel autonomy and replenishment evidenced for the declared duration?        |
| CG-06    | Heat-removal path (air, liquid, facility water, heat rejection) sufficient across states including transients.                 | E1+E2+E3+E4                         | S5        | Is capacity sufficient at design ambient with one unit out? Is thermal ride-through longer than restoration time after power or pump loss? Are leak detection and isolation effective?                   |
| CG-07    | BMS, EPMS, CDU, PLC and SCADA function safely, fail safe, are configured and governed.                                         | E1+E2+E3+E4                         | S4        | Do controllers fail to a safe state on loss of communication or power? Are setpoints and logic under change control? Are sensor failures detected rather than acted on?                                 |
| CG-08    | Accelerators, storage and fabrics deliver required function, performance and integrity.                                        | E2+E3+E4                            | S4        | Is usable capacity (not installed) sufficient for the outcome? Are performance baselines met under representative jobs? Are integrity errors detected and contained?                                    |
| CG-09    | Fault domains, isolation and blast-radius limits prevent propagation beyond tolerance.                                         | E1+E2+E4+E7                         | S4        | Are fault domains aligned across power, cooling, fabric and storage? Has isolation been demonstrated? Do any common-mode dependencies span fault domains?                                                |
| CG-10    | Restoration of outcome (power, cooling, compute, data/checkpoint, network, control plane) within tolerance planned and tested.  | E1+E2+E3+E4                         | S5        | Has end-to-end recovery been exercised to outcome restoration? Are recovery dependencies available when the primary fault domain is lost? Are recovery-time results within tolerance?                   |
| CG-11    | Evidence for decisive claims meets floors (meta-gate; evaluated across all controls).                                          | E1+E7                               | S4        | Do all decisive claims meet their evidence-profile floors? Have substitutions been approved? Are conflicts resolved or bounded?                                                                        |
| CG-12    | No unresolved US4/US5 UNKNOWN without disposition (meta-gate; evaluated across all controls).                                  | E1+E7                               | S3        | Is every US4 and US5 UNKNOWN dispositioned with owner, evidence needed and decision effect? Has any severity been lowered without new evidence?                                                         |
| CG-13    | Every critical function and dependency has an accountable owner and decision authority.                                       | E1+E6                               | S3        | Is there a named owner for each Required Function and material dependency? Can the owner act in EMERGENCY state? Are provider responsibilities contractually assigned?                                 |
| CG-14    | Material changes controlled, impact-assessed, validated.                                                                      | E1+E2+E3+E4                         | S4        | Do sampled material changes have impact assessment, approval, rollback and post-change validation? Are emergency changes reviewed after the event? Is drift detected?                                   |
| CG-15    | Identity, privilege, remote access and control-plane reach over facility and AI infrastructure bounded, monitored, recoverable. | E2+E3+E4+E7                         | S4        | Which identities can change infrastructure state, from where, with what approval? Are automation and agent actions allowlisted and reversible? Can authority be recovered if identity services fail?    |

# Part VI — Synthetic completed examples

The examples are synthetic training material. They describe no real facility, organisation or assessment, and are kept segregated from real assessment records.

## EX-01 Synthetic AI training cluster — checkpoint recovery not evidenced

| **Record**          | **Completed entry**                                                                                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Charter             | Synthetic Capability Instance: one training cluster; outcome includes recovery from node or storage failure within a declared recovery-time tolerance; AL5 requested.    |
| Evidence            | Current architecture, configuration and telemetry support OPERATION; checkpoint restore has only been tested for single files.                                          |
| Control results     | STO checkpoint durability: OPERATION CONFORMING. STO restart readiness: RESILIENCE UNKNOWN (no end-to-end restore at representative scale). Results recorded per claim type. |
| Failure path        | Storage metadata service loss → job stall → restart requires checkpoint read at scale; recovery time not evidenced.                                                     |
| Gates               | CG-08 PASS within observed states. CG-10 UNKNOWN (CRITICAL control UNKNOWN).                                                                                             |
| UNKNOWN             | US4 Critical (affects a CG-10 CRITICAL control); evidence needed: instrumented restore exercise at representative scale.                                                 |
| Review              | Independent reviewer challenged the use of single-file restore evidence for a RESILIENCE claim; challenge upheld.                                                       |
| Decision            | DT-19: CG-10 UNKNOWN ceiling (AIDCF-010) caps the recovery outcome at INCONCLUSIVE and the other outcomes at LIMITED; the question is not partitioned by outcome, so the recommendation is INCONCLUSIVE, worded per AIDCF-012 Part V; action: representative restore exercise. |
| Reassessment        | Trigger: completion of the restore exercise; delta reassessment of CG-10 controls.                                                                                       |

## EX-02 Synthetic power continuity — partial-load transfer evidence

| **Record**          | **Completed entry**                                                                                                                                                       |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Charter             | Synthetic Capability Instance: one data hall; outcome includes continuity through utility loss for a declared autonomy duration.                                        |
| Evidence            | Design, telemetry and maintenance current; generator transfer tested only at partial load; fuel replenishment contract exists but delivery has not been evidenced.        |
| Control results     | Generator start reliability: EFFECTIVENESS — claim scope narrowed to the tested load with technical-reviewer approval; CONFORMING for the narrowed scope; full-load condition recorded as UNKNOWN (U5). Fuel replenishment: OPERATION UNKNOWN (U10 dependency). |
| Gates               | CG-05 UNKNOWN; CG-03 UNKNOWN.                                                                                                                                             |
| UNKNOWN             | US5 Systemic (two gates affected).                                                                                                                                        |
| Decision            | DT-19: step 1 gate ceilings (CG-05 and CG-03 UNKNOWN → LIMITED, RESILIENCE claims INCONCLUSIVE); step 2 US5 → INCONCLUSIVE. Recommendation INCONCLUSIVE; no resilience conclusion beyond tested load and duration; actions: full-load transfer test and evidenced fuel delivery. |
| Reassessment        | Trigger: test and delivery evidence; delta reassessment of CG-03 and CG-05.                                                                                               |

## EX-03 Synthetic remote support authority — permission scope incomplete

| **Record**          | **Completed entry**                                                                                                                                       |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Charter             | Synthetic Capability Instance: cooling control system for a liquid-cooled hall, with OEM remote support.                                                  |
| Evidence            | Identity and network route evidence exist; permission scope and command limits for the OEM role are incomplete.                                           |
| Control results     | Remote support activation and approval: IMPLEMENTATION CONFORMING. Support identity permission scope: IMPLEMENTATION UNKNOWN.                            |
| Failure path        | Candidate authority path from OEM gateway to CDU setpoints; network connectivity alone does not establish authority or effect (DT-13 node 13.1).            |
| Gates               | CG-15 UNKNOWN. CG-06 not affected by connectivity alone; evaluated on its own CRITICAL controls (PASS).                                                    |
| UNKNOWN             | US4 Critical (CG-15 CRITICAL control).                                                                                                                    |
| Decision            | DT-19: CG-15 UNKNOWN ceiling → LIMITED (the authority path reaches only CG-06 scope, so not US5); recommendation LIMITED; actions: permission export for the OEM role and an authorised command-limit test in a maintenance window.                        |
| Reassessment        | Trigger: permission evidence and test; delta reassessment of CG-15.                                                                                       |

# Part VII — Assessor competence and accreditation criteria

AIDCF does not accredit people or firms (AIDCF-011 Part IX). The levels below let an organisation or provider evidence Part A procedure A5 consistently.

| **Level** | **Role**             | **Minimum evidence**                                                                                       | **May sign**                                    |
|-----------|----------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| AC-0      | Observer             | Induction, confidentiality, safety and method orientation.                                                  | Nothing                                         |
| AC-1      | Associate assessor   | Supervised evidence intake and accepted workpapers.                                                         | Workpapers as preparer, under supervision       |
| AC-2      | Domain assessor      | Domain competence, witnessed fieldwork, evidence judgment and accepted reviews.                             | Control results in the competent domain         |
| AC-3      | Lead assessor        | Cross-domain scope, integration, gates, Findings and decision drafting on prior assessments.                | Gate evaluations and Decision Recommendation    |
| AC-4      | Technical reviewer   | Recognised technical authority in the domain and current review experience.                                 | Technical approval (SG4)                        |
| AC-5      | Independent reviewer | Impartial senior assurance competence and gate and decision challenge experience.                          | Independent review (SG5)                        |
| AC-6      | Decision authority   | Governance appointment, independence and recorded delegation.                                               | Assurance Decision (SG6)                        |

Competence portfolio content: AIDCF method and evidence discipline; assurance, sampling, Findings and bounded decisions; applicable engineering and technical domains; safety and authorised testing; professional scepticism, impartiality and confidentiality; graph lineage and candidate-assertion handling; witnessed assessments and accepted workpapers; the scope, methods, Assurance Levels and roles for which the person is recognised; suspension and reinstatement criteria.

**AMH-REQ-080** Where Part VII is adopted, each person's level shall be recorded per domain and per engagement, and a person shall not sign a record listed for a higher level than the one recorded for that domain.

# Part VIII — Graph-ingestion mappings

Assessment records exchanged as graph data use the canonical AIDCF-014 object classes and relationship types. AIDCF and AI Trust Graph (AITG) decisions remain separate native objects (AIDCF-005).

| **AIDCF record**         | **AIDCF-014 class**       | **Minimum properties**                                                        |
|--------------------------|---------------------------|-------------------------------------------------------------------------------|
| Assessment               | Assessment                | ID; decision question; scope; version; status; owner                          |
| Capability profile       | CapabilityInstance        | ID; owner; lifecycle stage; architecture baseline                            |
| Service Outcome          | ServiceOutcome            | ID; metric; tolerance; criticality; operating states                          |
| Control result           | ControlAssessment         | control; claim type; subject; states; methods; result; confidence; review    |
| Evidence                 | EvidenceObject / EvidencePackage | ID; class; source; time; scope; integrity; status                      |
| Assertion                | Carried on ControlAssessment and EvidenceRequirement (no separate class) | proposition; conditions; candidate or reviewed state |
| Finding                  | Finding                   | ID; criterion; condition; cause; consequence; classification; status         |
| UNKNOWN                  | UnknownRecord             | ID; subject; missing attribute; type; severity; decision effect               |
| Scenario                 | FailureScenario           | ID; state; initiating condition; path; safeguards; residual; recovery         |
| Gate                     | GateResult                | ID; gate; applicability; evidence; result; decision ceiling; review           |
| Recommendation           | DecisionRecommendation    | ID; recommended state; controlling factors                                    |
| Decision                 | AssuranceDecision         | ID; subject; scope; state; lifecycle state; conditions; validity; authority   |
| Review                   | ReviewRecord              | ID; reviewer; independence; comments; disposition                             |
| Reassessment trigger     | ReassessmentTrigger       | ID; condition; affected objects                                               |

| **Previous relationship** | **Canonical relationship (AIDCF-014 §9)**                                                 |
|---------------------------|-------------------------------------------------------------------------------------------|
| ASSESSES                  | ASSESSED_BY (inverse: Control ASSESSED_BY ControlAssessment)                              |
| SUPPORTS / CHALLENGES / QUALIFIES | Unchanged                                                                         |
| EVALUATES                 | ASSESSED_BY (inverse)                                                                     |
| AFFECTS                   | HAS_FINDING (subject to Finding) and PROPAGATES_TO (scenario step to next step or outcome) |
| DEPENDS_ON                | Unchanged                                                                                 |
| PROPAGATES_TO             | Unchanged                                                                                 |
| PROTECTED_BY              | Unchanged                                                                                 |
| EVIDENCES_GATE            | GateResult EVIDENCED_BY EvidencePackage; ControlAssessment EVALUATES_GATE GateResult       |
| LIMITS                    | CONSTRAINS                                                                                |
| REVIEWED_BY               | Unchanged                                                                                 |
| GENERATED_FROM            | Carried in the provenance envelope of the derived object (AIDCF-014 §26), not as a relationship |
| SUPERSEDES                | Unchanged                                                                                 |
| INTEGRATION_HANDOFF       | Unchanged                                                                                 |

Ingestion validation rules:

**AMH-REQ-081** Every ingested object shall carry a stable ID, source, version and lifecycle state.

**AMH-REQ-082** Every ingested assertion shall be linked to supporting, challenging or qualifying evidence, or to an UNKNOWN Record.

**AMH-REQ-083** A candidate inference produced by automated or AI-assisted analysis shall not become a reviewed fact, and shall not change a result, Gate Result or decision, without review by a competent person.

**AMH-REQ-084** Network connectivity in the graph shall not be interpreted as reachability, authority, causality or realised effect without evidence for each.

**AMH-REQ-085** AIDCF and AITG decisions shall remain separate objects linked by INTEGRATION_HANDOFF.

**AMH-REQ-086** Sensitive infrastructure paths shall carry classification and be subject to a controlled query policy; supersession shall preserve prior snapshots and lineage.

# Part IX — Record schemas

All Part IX records carry the Part A common header (Part A §E.0: workpaperId, assessmentId, capabilityId, version, workpaperStatus, preparer, reviewer, relatedRecords, classification). Record-specific mandatory fields:

| **Record**                  | **Record-specific mandatory fields**                                                                                                   | **Equivalent Part A template** |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| Control Procedure           | controlId; registryVersion; claimType; scope (subject, states, period); stepsPerformed (P1–P8); criteriaConclusions; result; confidence | WP-12                          |
| Decision Tree Instance      | treeId (DT-01–DT-20); subject; nodeOutcomes (node, test outcome, evidence, branch); terminalOutcome; reviewer                           | —                              |
| Inspection Record           | checklistId (INS-<DOM>); itemsApplied; location; operatingState; observations; deviations; inaccessibleScope; safetyStatus            | WP-08                          |
| Evidence Collection         | evidenceId; class (E1–E7); playbook (IV.1–IV.7); collectionContext; qualityRatings (P F C R T I); qualityBand; acceptanceState         | WP-06                          |
| Gate Workbook               | gateId; applicability; criticalControls; supportingEvaluations; criteria; evidenceFloorAchieved; statesAndScenarios; gateResult; ceiling | WP-14                        |
| Competence Record           | person; domain; level (AC-0–AC-6); evidence; engagement; validity; supervisor                                                           | —                              |
| Graph Ingestion Manifest    | manifestId; sourceSystem; objectCounts by class; relationshipCounts by type; validationResults; reviewState                            | —                              |

# Appendix A — Conformance and requirement mapping

## A.1 Mapping from previous validation identifiers

| **Previous ID** | **Previous validation**                                                         | **Now**                                                                 |
|-----------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| AM11-VAL-01     | Every applicable control has an individual procedure record.                    | AMH-REQ-068 (per control and claim type)                            |
| AM11-VAL-02     | Every used decision tree retains the selected branch and rationale.             | AMH-REQ-066                                                           |
| AM11-VAL-03     | Every inspection records inaccessible scope and safety status.                  | AMH-REQ-077                                                           |
| AM11-VAL-04     | Every Evidence Object follows an applicable collection playbook.                | AMH-REQ-078                                                            |
| AM11-VAL-05     | Every applicable critical gate has a completed workbook and independent review. | AMH-REQ-079; Part A C3 and C6                                       |
| AM11-VAL-06     | Synthetic examples remain segregated from real assessments.                     | Part VI introduction (informative)                                       |
| AM11-VAL-07     | Every assessor role has an engagement-specific competence decision.             | AMH-REQ-080                                                          |
| AM11-VAL-08     | Every graph object preserves source, version and review state.                  | AMH-REQ-081                                                         |
| AM11-VAL-09     | No graph inference automatically changes a gate or decision.                    | AMH-REQ-083                                                        |
| AM11-VAL-10     | UNKNOWN, conflict, safety and non-compensation remain visible.                  | Part A requirements on UNKNOWN, gates and safety                         |

## A.2 Other identifier changes

| **Previous**                                                    | **Now**                                                           |
|-----------------------------------------------------------------|-------------------------------------------------------------------|
| Artifact ID AIDCF-AM-001; "Basis: Existing AIDCF-009 v1.0 only" | AIDCF-009 (Part B), companion to AIDCF-009 Part A                 |
| DT-01–DT-20 with identical node structure                       | DT-01–DT-20 rewritten as distinct trees (same IDs and topics)     |
| Part II 360 lifecycle-titled procedures                         | §II.3–§II.7 protocol + AIDCF-007A registry v1.1 (§II.9–§II.11)    |
| Evidence playbook headings "E1 Documentary E1 Documentary" …    | IV.1–IV.7 by AIDCF-008 class name                                 |
| Gate status "approved N/A"                                      | APPROVED_NA                                                       |
| Release review table                                            | AIDCF-011 Part XXII                                               |

# Appendix B — Review and release

The authoritative list of reviewer roles and release-gate states is in AIDCF-011 Part XXII and is not repeated here. Review of this document by the reviewer roles assigned to AIDCF-009 in that table is pending; this document has not been released.

**Final doctrine.** Additional procedural detail improves execution but cannot create authority, evidence, competence or certainty. Where the chain is incomplete, the assessor reduces, conditions or suspends assurance, or the decision is INCONCLUSIVE.
