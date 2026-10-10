> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-006_Assurance_Principles_Standard_v1.1.pdf](AIDCF-006_Assurance_Principles_Standard_v1.1.pdf).

**AIDCF**

# ASSURANCE PRINCIPLES STANDARD

*AI Data Centre Facilities Assurance Framework*

Version 1.1

The constitutional rules governing claims, evidence, uncertainty, critical gates, decisions, independence and responsible use

Artifact ID: AIDCF-006 (short code APS)  
Artifact type: Normative constitutional standard  
Status: Draft for controlled review  
Date: 2026-10-10  
Author: Siva Sethumadhavan  
Release 1: Foundational Methodology

Assurance is bounded confidence supported by evidence, not confidence created by presentation.

# Document control

| **Field**            | **Value**                                                                                                                                                                            |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Title                | AIDCF Assurance Principles Standard                                                                                                                                                  |
| Artifact ID          | AIDCF-006 (short code APS)                                                                                                                                                           |
| Version              | 1.1                                                                                                                                                                                  |
| Date                 | 2026-10-10                                                                                                                                                                           |
| Artifact type        | Normative constitutional standard                                                                                                                                                    |
| Status               | Draft for controlled review                                                                                                                                                          |
| Author               | Siva Sethumadhavan                                                                                                                                                                   |
| Depends on           | AIDCF-001 AIDCF Manifesto; AIDCF-002 Core Conceptual Model; AIDCF-003; AIDCF-004; AIDCF-005                                                                                          |
| Authority            | Governs downstream controls (AIDCF-007A), evidence (AIDCF-008), assessment (AIDCF-009), scoring and decisions (AIDCF-010), programmes (AIDCF-011), maturity (AIDCF-017), reporting (AIDCF-012) and tooling. |
| Publication boundary | Independent methodology; not law, licensed engineering, safety approval, accredited certification or authorisation for hazardous testing. AIDCF does not certify.                  |

## Revision history

| **Version** | **Date**   | **Summary**                                                                                                                                                                                                                                                                                                                         |
|-------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | —          | Controlled-review baseline for downstream artifacts.                                                                                                                                                                                                                                                                                |
| 1.1         | 2026-10-10 | Removed certification authority claims; adopted the canonical 16-step chain; aligned assurance levels (AL0–AL6), claim types, decision states and lifecycle, gate results (with NOT_ASSESSED), confidence, evidence quality bands and UNKNOWN severity to AIDCF-002; canonical gate catalogue with scope and evidence floors; defined MATERIAL; public artifact IDs; principle IDs in APS-REQ form; conformance levels renamed APS-CL0–APS-CL5. |

## Relationship to AIDCF-002

AIDCF-002 Core Conceptual Model states what assurance concepts mean; this standard states the non-negotiable rules for using them. The canonical chain (AIDCF-002 §9), the definition of MATERIAL (AIDCF-002 §22), the control model (AIDCF-002 §23) and the controlled vocabularies (AIDCF-002 Part VI) are used here without redefinition, and every principle in Parts III to XIV constrains one or more steps of that chain. Where a principle and an AIDCF-002 definition appear to differ, the definition governs meaning and the principle governs obligation; the conflict is resolved through methodology governance. Detailed operational rules (gate criteria, roll-up and decision ceilings) belong to AIDCF-010 and evidence floors to AIDCF-008.

# Executive thesis

AIDCF assurance is a bounded, evidence-supported and accountable conclusion about whether the facilities and infrastructure supporting a defined AI Capability Instance can be reasonably relied upon to achieve required Service Outcomes within declared boundaries, states, operating conditions and time. It is not a guarantee, a generic quality label, a score, a maturity level or an inherited certificate.

## Constitutional reasoning chain

This standard uses the canonical AIDCF assurance chain of AIDCF-002 §9:

1 Decision Question → 2 Capability Instance → 3 Service Outcome → 4 Required Function → 5 Architecture (InfrastructureSystem/Asset/Interface) → 6 Dependency and Fault Domain → 7 Threat / Hazard / Failure Scenario → 8 Safeguard → 9 Control → 10 Evidence Requirement → 11 Evidence Object → 12 Control Assessment (result) → 13 Finding / UNKNOWN Record → 14 Gate Result → 15 Score Snapshot and Decision Recommendation → 16 Assurance Decision → (Assurance Report and Reassessment Trigger close the loop back to 2).

Boundary, operating envelope and operating states are context for every step. Independent review (APS-REQ-049, APS-REQ-051) takes place between the Decision Recommendation (step 15) and the Assurance Decision (step 16), and no decision is approved without it.

# Contents

1\. Authority, scope and constitutional status

2\. Assurance architecture and terminology

3\. Capability and outcome principles

4\. Scope, boundary and state principles

5\. Dependency and concentration principles

6\. Failure, resilience and recovery principles

7\. Safeguard and validation principles

8\. Evidence and confidence principles

9\. UNKNOWN and limitation principles

10\. Critical-gate principles

11\. Cross-domain and graph-native principles

12\. Decision, scoring, maturity and reporting principles

13\. Independence, competence and ethics

14\. Lifecycle and continuing assurance

15\. Claim language and decision model

16\. Conformance and enforcement

17\. Machine-readable profile

18\. Worked applications and anti-patterns

19\. Appendices

# Part I - Authority, scope and constitutional status

## 1. Purpose

This standard establishes the non-negotiable principles that constrain how AIDCF requirements are designed, assessments are performed, evidence is interpreted and conclusions are issued. Downstream artifacts may operationalise these principles but shall not weaken, bypass or silently reinterpret them.

Its scope is AIDCF assessments and the Assurance Decisions, Assurance Statements and Assurance Reports issued from them. AIDCF does not certify, and this standard neither establishes, operates nor endorses a certification scheme. An organisation that operates a conformity-assessment or certification scheme using AIDCF artifacts does so under its own accreditation and authority; such use does not make AIDCF a certifying body, and the scheme's certificates are not AIDCF conclusions.

## 2. Artifact precedence

| **Layer**                           | **Authority**                                               |
|-------------------------------------|-------------------------------------------------------------|
| AIDCF-001 Manifesto                 | Purpose, identity and public commitments.                   |
| AIDCF-002 Core Conceptual Model     | Canonical meanings, chain, MATERIAL and vocabularies.       |
| AIDCF-003 to AIDCF-005              | Ontology, failure semantics and graph integration.          |
| AIDCF-006 (this standard)           | Constitutional assurance rules.                             |
| AIDCF-007A to AIDCF-019             | Operational controls, evidence, methods, scores, programmes, reports and guides. |
| Tooling                             | Declared implementation only, never hidden authority.       |

## 3. Constitutional invariants

| **ID** | **Invariant**                                                                  |
|--------|--------------------------------------------------------------------------------|
| CI-01  | Capability and Service Outcome are the primary assurance object.               |
| CI-02  | Assertions do not become facts without evidence and review.                    |
| CI-03  | UNKNOWN remains visible and non-favourable.                                    |
| CI-04  | Critical gates cannot be averaged away.                                        |
| CI-05  | Cross-boundary dependencies remain visible.                                    |
| CI-06  | Designed, installed, commissioned, observed and tested states remain distinct. |
| CI-07  | Conclusions stay bounded by scope, state, time and evidence.                   |
| CI-08  | Material change can invalidate a prior conclusion.                             |
| CI-09  | Automation proposes; accountable authority approves.                           |
| CI-10  | AIDCF and AI Trust Graph retain separate native conclusions.                   |

## 4. Non-substitution

- Does not replace licensed engineering or statutory approval.

- Does not determine legal compliance unless separately authorised.

- Does not authorise intrusive or hazardous testing.

- Does not transfer operational accountability from owners to assessors.

- Does not certify, and does not authorise any party to describe an AIDCF assessment or decision as a certification.

# Part II - Assurance architecture and terminology

## 5. Definition of assurance

Assurance is a reasoned and reviewable level of confidence, for a defined decision, that specified claims about a Capability Instance and supporting infrastructure are supported by sufficient appropriate evidence within a declared scope, state, period and set of limitations.

## 6. Claim types and assurance levels

What a conclusion may assert depends on the claim type it is made for (AIDCF-002 §24) and on the depth of the assurance programme that produced it (Assurance Levels, AIDCF-011; AIDCF-002 §25). A claim type cannot be concluded by a programme below its minimum level.

| **Claim type**  | **What a CONFORMING result asserts**                                         | **Minimum Assurance Level** |
|-----------------|-----------------------------------------------------------------------------|-----------------------------|
| DESIGN          | Requirement and design are adequate.                                        | AL2                         |
| IMPLEMENTATION  | As-built and configured state reconciles to the approved design.            | AL3                         |
| OPERATION       | Operates as intended over a representative period and states.               | AL4                         |
| EFFECTIVENESS   | Achieves its objective under tested or observed adverse conditions.        | AL5                         |
| RESILIENCE      | Contains failure and supports recovery within tolerance.                    | AL5                         |

| **Assurance Level**               | **Permitted conclusion**                                                       | **Minimum basis**                                    |
|-----------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------|
| AL0 Discovery                     | No positive conclusion; inventory and decision discovery only.                 | Traceable inventory and decision question.           |
| AL1 Readiness                     | Known state described; scope, ownership, applicability and evidence readiness. | Traceable inventory, observations and scope record.  |
| AL2 Design                        | DESIGN claims.                                                                 | Approved design evidence and competent review.       |
| AL3 Implementation                | IMPLEMENTATION claims in observed scope.                                       | Corroborated technical and as-built evidence.        |
| AL4 Operational                   | OPERATION claims for representative period and states.                         | Representative operating and monitoring evidence.    |
| AL5 Effectiveness and resilience  | EFFECTIVENESS and RESILIENCE claims for defined scenarios.                     | Cross-domain scenario, test, gate and recovery evidence. |
| AL6 Continuing                    | Refresh of previously approved claims within monitored scope.                  | Monitoring design and operation (APS-REQ-058), evidence refresh and trigger handling. |

v1.0 used levels A0 to A5. A2 to A5 map one to one to AL2 to AL5; A0 and A1 correspond to AL0 and AL1. Assurance Levels are not certification grades.

## 7. Mandatory distinctions

| **Do not collapse**         | **Reason**                                                      |
|-----------------------------|-----------------------------------------------------------------|
| Assurance / guarantee       | Assurance is bounded confidence, not certainty.                 |
| Evidence quality / confidence | Support strength (quality band, sufficiency) differs from assessor confidence (CONF-0 to CONF-4). |
| Control / safeguard         | Requirement differs from real-world mechanism.                  |
| Maturity / effectiveness    | Institutionalisation differs from performance.                  |
| Score / decision            | Number cannot replace reasoning and gates.                      |
| UNKNOWN / failure           | Missing knowledge differs from demonstrated adverse state.      |
| NOT_APPLICABLE / NOT_ASSESSED | Approved irrelevance differs from missing activity.           |
| Control result / decision state | CONFORMING … NOT_ASSESSED describe one control; REASONABLY_ASSURED … INCONCLUSIVE describe a decision. |
| Gate result / condition       | A gate is PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED; conditions exist only at decision level. |
| Failover / recovery         | Transfer differs from restoration.                              |
| Redundancy / resilience     | Duplication does not prove outcome continuity.                  |
| Connection / authority      | Reachability does not prove permission or consequential action. |

# Part III - Capability and outcome principles

## APS-REQ-001 Capability-first assurance

The primary object of AIDCF assurance shall be a defined Capability Instance and required Service Outcomes.

Assets and controls matter because of the functions and outcomes they support.

| **Dimension**             | **Requirement**                                                                             |
|---------------------------|---------------------------------------------------------------------------------------------|
| Application               | Define capability, owner, architecture baseline, lifecycle stage, outcomes and criticality. |
| Prohibited interpretation | Generic facility assurance without a Capability Instance.                                   |
| Minimum evidence          | Capability record, outcome requirements and architecture.                                   |
| Decision effect           | Missing capability or outcome blocks positive capability assurance.                         |

## APS-REQ-002 Outcome alignment

Every material test, control, finding and recommendation shall identify the Service Outcome or decision it protects.

Outcome alignment prevents checklist completion from becoming the objective.

| **Dimension**             | **Requirement**                                                       |
|---------------------------|-----------------------------------------------------------------------|
| Application               | Record affected outcome, tolerance, time sensitivity and consequence. |
| Prohibited interpretation | Control activity justified only because it is customary.              |
| Minimum evidence          | Service requirements and impact analysis.                             |
| Decision effect           | Unlinked activity cannot determine capability assurance.              |

## APS-REQ-003 Function before product

Required functions shall be defined independently from products implementing them.

This preserves vendor neutrality and enables substitution and failure analysis.

| **Dimension**             | **Requirement**                                                   |
|---------------------------|-------------------------------------------------------------------|
| Application               | Define function, demand, duration, state and implementing assets. |
| Prohibited interpretation | Using a vendor product name as the control objective.             |
| Minimum evidence          | Functional requirements and observed implementation.              |
| Decision effect           | Unclear function limits design and effectiveness conclusions.     |

## APS-REQ-004 Outcome-centric materiality

Materiality shall be based on plausible effect on outcomes, safety, stakeholders and obligations, and shall be decided with the AIDCF-002 §22 test: a fact, dependency, condition, deficiency or UNKNOWN is **MATERIAL** if, had it been known or resolved differently, a competent assessor would reasonably expect it to change (a) a control result, (b) a gate result, (c) the decision state, or (d) a condition, limitation or ceiling attached to the decision, for the declared Capability Instance, Service Outcomes and operating states.

Issue count, novelty and cost alone do not establish materiality.

| **Dimension**             | **Requirement**                                                                   |
|---------------------------|-----------------------------------------------------------------------------------|
| Application               | Assess magnitude, duration, concentration, recoverability and stakeholder effect. |
| Prohibited interpretation | Averaging catastrophic and trivial effects.                                       |
| Minimum evidence          | Capability impact analysis and accountable criteria.                              |
| Decision effect           | Materiality determines depth, gate relevance, UNKNOWN severity and escalation.   |

# Part IV - Scope, boundary and state principles

## APS-REQ-005 Explicit boundary

Every conclusion shall declare included systems, locations, organisations, states and time.

A boundary makes claims interpretable.

| **Dimension**             | **Requirement**                                                   |
|---------------------------|-------------------------------------------------------------------|
| Application               | Record inclusions, exclusions and boundary-crossing dependencies. |
| Prohibited interpretation | Treating out-of-scope as non-existent.                            |
| Minimum evidence          | Approved scope, architecture and dependency record.               |
| Decision effect           | Unclear boundary blocks final assurance wording.                  |

## APS-REQ-006 Operating-envelope discipline

Assurance applies only within defined load, environmental, capacity, duration and state conditions.

Evidence in one condition cannot automatically support another.

| **Dimension**             | **Requirement**                                                 |
|---------------------------|-----------------------------------------------------------------|
| Application               | State demand, headroom, limits, duration and applicable states. |
| Prohibited interpretation | Generalising low-load tests to peak AI load.                    |
| Minimum evidence          | Operating envelope, telemetry and test conditions.              |
| Decision effect           | Claims outside the envelope remain unassured.                   |

## APS-REQ-007 State-specific assurance

Normal, degraded, maintenance, emergency, recovery and transition states (NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION, with SHUTDOWN, FAILED and UNKNOWN as further codes) shall be considered separately where material.

Normal operation can hide maintenance or recovery fragility.

| **Dimension**             | **Requirement**                                       |
|---------------------------|-------------------------------------------------------|
| Application               | Identify state coverage for each claim and safeguard. |
| Prohibited interpretation | Assuming normal-state evidence proves all states.     |
| Minimum evidence          | State model, work controls, incidents and tests.      |
| Decision effect           | Uncovered critical states cap resilience assurance.   |

## APS-REQ-008 Reality over intent

Observed and tested reality shall take precedence over intended design where they conflict.

Intent cannot prove current implementation.

| **Dimension**             | **Requirement**                                                                  |
|---------------------------|----------------------------------------------------------------------------------|
| Application               | Separate intended, designed, installed, commissioned, observed and tested state. |
| Prohibited interpretation | Silently reconciling records to match design.                                    |
| Minimum evidence          | Current configuration, observation and test evidence.                            |
| Decision effect           | Conflict is disclosed and evaluated.                                             |

## APS-REQ-009 Proportionate depth

Assessment depth shall match consequence, complexity, change, uncertainty and decision need.

Proportionality prevents both superficiality and unsafe overtesting.

| **Dimension**             | **Requirement**                                    |
|---------------------------|----------------------------------------------------|
| Application               | Document depth, sampling and escalation rationale. |
| Prohibited interpretation | One fixed checklist depth for all capabilities.    |
| Minimum evidence          | Scoping, criticality and test authorisation.       |
| Decision effect           | Insufficient depth limits the conclusion.          |

# Part V - Dependency and concentration principles

## APS-REQ-010 Dependency visibility

Material dependencies shall be explicit, typed, directional and state-aware.

Hidden dependencies undermine redundancy and recovery claims.

| **Dimension**             | **Requirement**                                                                       |
|---------------------------|---------------------------------------------------------------------------------------|
| Application               | Map upstream, downstream, shared, external, human, control and recovery dependencies. |
| Prohibited interpretation | Omitting outsourced dependencies.                                                     |
| Minimum evidence          | Dependency graph, architecture, contracts and observed paths.                         |
| Decision effect           | Critical hidden dependency may trigger a gate.                                        |

## APS-REQ-011 External dependency continuity

External providers remain part of capability reasoning even when outside direct assessment.

Exclusion does not remove consequence.

| **Dimension**             | **Requirement**                                                                       |
|---------------------------|---------------------------------------------------------------------------------------|
| Application               | Identify provider, service, capacity, evidence access, failure effect and escalation. |
| Prohibited interpretation | Assuming an SLA proves continuity.                                                    |
| Minimum evidence          | Contracts, provider evidence and scenario analysis.                                   |
| Decision effect           | Weakly evidenced critical external dependency caps assurance.                         |

## APS-REQ-012 Shared-dependency scrutiny

Nominal alternatives shall be examined for common causes, routes, controllers, identities, teams and providers.

Duplication does not establish independence.

| **Dimension**             | **Requirement**                                                  |
|---------------------------|------------------------------------------------------------------|
| Application               | Map shared fault domains and common-mode events.                 |
| Prohibited interpretation | Calling dual paths resilient without shared-dependency analysis. |
| Minimum evidence          | Topology, configuration and test evidence.                       |
| Decision effect           | Unresolved common mode prevents independence claims.             |

## APS-REQ-013 Concentration awareness

Capability, capacity, authority, supplier and knowledge concentration shall be explicit.

Concentration magnifies consequence.

| **Dimension**             | **Requirement**                                                 |
|---------------------------|-----------------------------------------------------------------|
| Application               | Identify aggregation points, blast radius and recovery options. |
| Prohibited interpretation | Dismissing concentration using component reliability alone.     |
| Minimum evidence          | Capacity, topology, role and provider data.                     |
| Decision effect           | Critical concentration increases scenario priority.             |

## APS-REQ-014 Dependency ownership

Every material dependency shall have an owner or explicit UNKNOWN owner.

Responsibility is required for evidence, treatment and recovery.

| **Dimension**             | **Requirement**                                              |
|---------------------------|--------------------------------------------------------------|
| Application               | Assign owner, operator, provider, maintainer and escalation. |
| Prohibited interpretation | Treating contract assignment as proof of control.            |
| Minimum evidence          | Responsibility model and operating procedure.                |
| Decision effect           | Unowned critical dependency is a responsibility gap.         |

# Part VI - Failure, resilience and recovery principles

## APS-REQ-015 Failure-chain analysis

Material failures shall be analysed from initiating condition through mode, effect, propagation, consequence, safeguard and recovery.

Stopping at component failure misses capability impact.

| **Dimension**             | **Requirement**                                       |
|---------------------------|-------------------------------------------------------|
| Application               | Apply AIDCF-004 distinctions and dependency paths.    |
| Prohibited interpretation | Collapsing cause, mode, effect and consequence.       |
| Minimum evidence          | Scenario records and failure analysis.                |
| Decision effect           | Incomplete chain limits resilience conclusions.       |

## APS-REQ-016 Cross-domain propagation

Failure analysis shall cross domain boundaries wherever dependencies transmit effect.

Resilience emerges from interactions.

| **Dimension**             | **Requirement**                                                         |
|---------------------------|-------------------------------------------------------------------------|
| Application               | Trace power, cooling, compute, storage, network and operations effects. |
| Prohibited interpretation | Siloed domain assessment as end-to-end assurance.                       |
| Minimum evidence          | Cross-domain graph, telemetry and tests.                                |
| Decision effect           | Unexamined material path is recorded as an UNKNOWN Record.              |

## APS-REQ-017 Compound conditions

Credible combinations of failure, maintenance, demand, threat and recovery shall be considered.

Systemic failures often require multiple conditions.

| **Dimension**             | **Requirement**                                                  |
|---------------------------|------------------------------------------------------------------|
| Application               | Analyse latent, sequential, compound and common-cause scenarios. |
| Prohibited interpretation | Dismissing combinations solely on individual rarity.             |
| Minimum evidence          | Scenario basis, incident data and stress analysis.               |
| Decision effect           | Catastrophic credible scenario may become a gate.                |

## APS-REQ-018 Resilience lifecycle

Resilience shall cover anticipate, prevent, detect, decide, respond, contain, withstand, degrade, recover and adapt as applicable.

Prevention alone is not resilience.

| **Dimension**             | **Requirement**                                                     |
|---------------------------|---------------------------------------------------------------------|
| Application               | Map safeguards and gaps across the lifecycle.                       |
| Prohibited interpretation | Equating monitoring or redundancy with resilience.                  |
| Minimum evidence          | Safeguard model, exercises and recovery records.                    |
| Decision effect           | Missing essential lifecycle capability limits resilience assurance. |

## APS-REQ-019 Recovery evidence

Recovery claims shall identify prerequisites, sequence, authority, resources and validation.

A plan does not prove recoverability.

| **Dimension**             | **Requirement**                                           |
|---------------------------|-----------------------------------------------------------|
| Application               | Validate critical recovery steps and dependencies safely. |
| Prohibited interpretation | Assuming failover equals recovery.                        |
| Minimum evidence          | Recovery tests, incidents and baselines.                  |
| Decision effect           | Untested critical recovery remains design intent.         |

## APS-REQ-020 Safe validation

Validation shall be authorised, competent, proportionate and non-destructive by default.

Assurance does not justify new unmanaged risk.

| **Dimension**             | **Requirement**                                                                |
|---------------------------|--------------------------------------------------------------------------------|
| Application               | Use least intrusive sufficient method, rules of engagement and abort criteria. |
| Prohibited interpretation | Hazardous live testing without explicit authority.                             |
| Minimum evidence          | Authorisation, risk assessment, test plan and results.                         |
| Decision effect           | Unsafe evidence is not accepted and is escalated.                              |

# Part VII - Safeguard and validation principles

## APS-REQ-021 Safeguard reality

A control requirement and real-world safeguard shall remain distinct.

A policy cannot substitute for implemented protection.

| **Dimension**             | **Requirement**                                            |
|---------------------------|------------------------------------------------------------|
| Application               | Identify mechanism, owner, scope, states and dependencies. |
| Prohibited interpretation | Counting a control statement as an operating safeguard.    |
| Minimum evidence          | Configuration and observation evidence.                    |
| Decision effect           | Absent implementation supports intent only.                |

## APS-REQ-022 Effectiveness by condition

Safeguard effectiveness shall be concluded only for validated scope, conditions and period.

Effectiveness is contextual.

| **Dimension**             | **Requirement**                                            |
|---------------------------|------------------------------------------------------------|
| Application               | Define trigger, capacity, timing, state and failure modes. |
| Prohibited interpretation | Generalising one successful test to all conditions.        |
| Minimum evidence          | Representative test and operating evidence.                |
| Decision effect           | Outside tested conditions remains unproven.                |

## APS-REQ-023 Safeguard dependency

Safeguards shall be assessed for power, sensing, control, identity, operator and supplier dependencies.

A safeguard can fail through the same cause it manages.

| **Dimension**             | **Requirement**                                 |
|---------------------------|-------------------------------------------------|
| Application               | Model dependencies and common mode.             |
| Prohibited interpretation | Assuming safeguards are independent.            |
| Minimum evidence          | Architecture, configuration and failure tests.  |
| Decision effect           | Shared dependency may invalidate barrier claim. |

## APS-REQ-024 Defence diversity

Multiple safeguards strengthen assurance only when mechanisms and dependencies are meaningfully diverse.

Layer count is not defence depth.

| **Dimension**             | **Requirement**                                    |
|---------------------------|----------------------------------------------------|
| Application               | Define diversity and correlated bypass.            |
| Prohibited interpretation | Counting duplicate policies as independent layers. |
| Minimum evidence          | Design and scenario evidence.                      |
| Decision effect           | No independence claim without evidence.            |

## APS-REQ-025 Residual-path disclosure

Material paths remaining after safeguards shall be disclosed.

Remediation existence does not prove closure.

| **Dimension**             | **Requirement**                                     |
|---------------------------|-----------------------------------------------------|
| Application               | Reanalyse alternate and residual paths.             |
| Prohibited interpretation | Reporting only planned control.                     |
| Minimum evidence          | Post-control analysis and retest.                   |
| Decision effect           | Residual exposure informs conditions and follow-up. |

# Part VIII - Evidence and confidence principles

## APS-REQ-026 Evidence before conclusion

Every material conclusion shall be supported by evidence appropriate to claim type.

Evidence is the basis, not an appendix.

| **Dimension**             | **Requirement**                                                                  |
|---------------------------|----------------------------------------------------------------------------------|
| Application               | Match design, implementation and effectiveness claims to corresponding evidence. |
| Prohibited interpretation | Policy alone for operating effectiveness.                                        |
| Minimum evidence          | Assertion-specific evidence bundle.                                              |
| Decision effect           | Unsupported claim remains UNKNOWN or intent.                                     |

## APS-REQ-027 Evidence provenance

Evidence shall retain source, collection, time, scope, integrity and transformation.

Without provenance evidence cannot be reviewed.

| **Dimension**             | **Requirement**                         |
|---------------------------|-----------------------------------------|
| Application               | Use stable IDs and custody records.     |
| Prohibited interpretation | Detached screenshots without context.   |
| Minimum evidence          | Evidence manifest and provenance chain. |
| Decision effect           | Material provenance gap limits use.     |

## APS-REQ-028 Evidence sufficiency

Sufficiency depends on relevance, reliability, currency, coverage, corroboration and representativeness, rated under AIDCF-008 as quality dimensions, quality bands Q0–Q5 and sufficiency S0–S5 against the control's evidence floor.

Quantity alone does not create assurance.

| **Dimension**             | **Requirement**                                     |
|---------------------------|-----------------------------------------------------|
| Application               | Review each assertion and common-source dependence. |
| Prohibited interpretation | Averaging evidence quality across assertions.       |
| Minimum evidence          | Sufficiency rationale.                              |
| Decision effect           | Evidence below floor makes the control result UNKNOWN; it never reduces a score in place of the result. |

## APS-REQ-029 Evidence currency

Evidence remains valid only while representative of the assessed state.

Time and change can invalidate evidence.

| **Dimension**             | **Requirement**                                     |
|---------------------------|-----------------------------------------------------|
| Application               | Define expiry and change triggers.                  |
| Prohibited interpretation | Universal fixed validity without change review.     |
| Minimum evidence          | Timestamp, configuration and change records.        |
| Decision effect           | Stale evidence triggers limitation or reassessment. |

## APS-REQ-030 Assertion-specific confidence

Confidence shall attach to a precise assertion, not a whole report, and shall be expressed on the CONF-0 to CONF-4 scale with CONFLICTING and STALE flags (AIDCF-008).

Claims in one document may have unequal support.

| **Dimension**             | **Requirement**                                          |
|---------------------------|----------------------------------------------------------|
| Application               | State rationale and unresolved conditions per assertion. |
| Prohibited interpretation | One overall confidence label hiding weak claims.         |
| Minimum evidence          | Assertion register and review.                           |
| Decision effect           | Confidence shapes wording, never replaces evidence.      |

## APS-REQ-031 Conflict retention

Conflicting evidence shall remain visible until resolved or bounded.

Deleting conflict creates false certainty.

| **Dimension**             | **Requirement**                              |
|---------------------------|----------------------------------------------|
| Application               | Record each source and resolution rationale. |
| Prohibited interpretation | Selecting favourable evidence silently.      |
| Minimum evidence          | Conflict and supersession record.            |
| Decision effect           | Unresolved conflict limits assurance.        |

# Part IX - UNKNOWN and limitation principles

## APS-REQ-032 UNKNOWN preservation

UNKNOWN shall remain a first-class state.

Transparency is safer than fabricated completeness.

| **Dimension**             | **Requirement**                                                 |
|---------------------------|-----------------------------------------------------------------|
| Application               | Record an UNKNOWN Record with type (U1–U10), severity (US1–US5), owner and resolution path. |
| Prohibited interpretation | Encoding UNKNOWN as zero, PASS, NONCONFORMING or NOT_APPLICABLE. |
| Minimum evidence          | Unknown register.                                               |
| Decision effect           | US3 to US5 UNKNOWNs cap the decision by severity (Appendix C).  |

## APS-REQ-033 No assumed favourable state

Absence of adverse evidence shall not prove effectiveness or resilience.

Not finding is not proving.

| **Dimension**             | **Requirement**                                             |
|---------------------------|-------------------------------------------------------------|
| Application               | Distinguish NOT_ASSESSED, UNKNOWN, NOT_APPLICABLE and an INCONCLUSIVE decision. |
| Prohibited interpretation | Assumed pass where evidence is unavailable.                 |
| Minimum evidence          | Coverage and state records.                                 |
| Decision effect           | No positive claim without affirmative support.              |

## APS-REQ-034 Limitation transparency

Material exclusions, sampling, stale evidence and access constraints shall be prominent.

Decision makers need to know what is not covered.

| **Dimension**             | **Requirement**                                      |
|---------------------------|------------------------------------------------------|
| Application               | State limitations beside conclusions and in exports. |
| Prohibited interpretation | Burying critical limits in appendices.               |
| Minimum evidence          | Limitation register.                                 |
| Decision effect           | Limitations shape wording and validity.              |

## APS-REQ-035 Not-applicable discipline

NOT_APPLICABLE requires approved rationale that no relevant subject or outcome exists.

NOT_APPLICABLE must not remove hard or untested requirements.

| **Dimension**             | **Requirement**                            |
|---------------------------|--------------------------------------------|
| Application               | Name criterion, rationale and approver.    |
| Prohibited interpretation | Using NOT_APPLICABLE because evidence is unavailable. |
| Minimum evidence          | Applicability decision.                    |
| Decision effect           | Improper NOT_APPLICABLE reverts to NOT_ASSESSED or UNKNOWN. |

# Part X - Critical-gate principles

## APS-REQ-036 Critical-gate protection

Critical prerequisites shall be evaluated separately from scores and maturity.

Some conditions are indispensable.

| **Dimension**             | **Requirement**                                                        |
|---------------------------|------------------------------------------------------------------------|
| Application               | Define gate, failure/unknown criteria, evidence floor and consequence. |
| Prohibited interpretation | Averaging a failed gate into a good score.                             |
| Minimum evidence          | Gate record and evidence.                                              |
| Decision effect           | A gate result of FAIL or UNKNOWN caps the decision state as specified in AIDCF-010. |

## APS-REQ-037 Non-compensation

Strong performance in one area shall not compensate for a failed prerequisite or catastrophic scenario.

Substitution hides fragility.

| **Dimension**             | **Requirement**                                                                        |
|---------------------------|----------------------------------------------------------------------------------------|
| Application               | Use non-compensating logic for safety, continuity, containment, recovery and evidence. |
| Prohibited interpretation | Points trading across unrelated domains.                                               |
| Minimum evidence          | Gate and outcome analysis.                                                             |
| Decision effect           | Decision follows the most restrictive applicable condition.                            |

## APS-REQ-038 Gate proportionality

Critical gates shall be applied through the capability profile: the set of fifteen gates (CG-01 to CG-15, Appendix B) is canonical, but applicability and criterion parameters shall derive from the Capability Instance, outcomes, dependencies and scenarios.

Different profiles have different indispensable conditions; a gate is set aside only as APPROVED_NA with approved boundary rationale.

| **Dimension**             | **Requirement**                                           |
|---------------------------|-----------------------------------------------------------|
| Application               | Derive gates from outcomes, dependencies and scenarios.   |
| Prohibited interpretation | Declaring every control gate-critical, or omitting a gate without APPROVED_NA. |
| Minimum evidence          | Capability profile and rationale.                         |
| Decision effect           | Improper gate applicability invalidates the decision basis. |

## APS-REQ-039 Gate closure

A critical gate closes only with corrective evidence and required independent review.

Planned action is not closure.

| **Dimension**             | **Requirement**                      |
|---------------------------|--------------------------------------|
| Application               | Retest condition and residual paths. |
| Prohibited interpretation | Closure by management promise.       |
| Minimum evidence          | Remediation and retest evidence.     |
| Decision effect           | Open gate remains visible in claims. |

# Part XI - Cross-domain and graph-native principles

## APS-REQ-040 System-of-systems assurance

AIDCF shall reason across all material domains as one capability-supporting system.

Local conformance does not prove end-to-end outcome.

| **Dimension**             | **Requirement**                                  |
|---------------------------|--------------------------------------------------|
| Application               | Use integrated dependency and scenario views.    |
| Prohibited interpretation | End-to-end decision from siloed checklists only. |
| Minimum evidence          | Cross-domain graph and scenarios.                |
| Decision effect           | Missing interaction limits system assurance.     |

## APS-REQ-041 Graph-native traceability

Material entities, relations, assertions, paths and decisions should be versioned graph objects.

Graph form makes lineage and propagation explicit.

| **Dimension**             | **Requirement**                                      |
|---------------------------|------------------------------------------------------|
| Application               | Use canonical IDs, evidence and snapshots.           |
| Prohibited interpretation | Treating graph connection as causality or authority. |
| Minimum evidence          | Conformant exchange records.                         |
| Decision effect           | Graph supports reasoning but proves nothing alone.   |

## APS-REQ-042 Federated assurance

AIDCF and AI Trust Graph conclusions shall remain native while contributing to an integrated decision package.

Integration must not collapse semantics.

| **Dimension**             | **Requirement**                                         |
|---------------------------|---------------------------------------------------------|
| Application               | Use approved bridge assertions and native snapshots.    |
| Prohibited interpretation | Merging distinct findings into one unsupported verdict. |
| Minimum evidence          | AIDCF-005 integrated decision package.                  |
| Decision effect           | Integrated decision states separate limitations.        |

## APS-REQ-043 Human approval of inference

Automation may propose content; material facts and decisions require accountable review.

Model confidence cannot confer authority.

| **Dimension**             | **Requirement**                                      |
|---------------------------|------------------------------------------------------|
| Application               | Store candidate state, source and reviewer outcome.  |
| Prohibited interpretation | Automatic conversion of inference to fact.           |
| Minimum evidence          | Inference and review log.                            |
| Decision effect           | Unreviewed inference cannot support final assurance. |

# Part XII - Decision, scoring, maturity and reporting principles

## APS-REQ-044 Bounded decision

Every decision shall state subject, question, scope, criteria, evidence, states, period, limitations and owner.

Bounds prevent misleading transfer.

| **Dimension**             | **Requirement**                                      |
|---------------------------|------------------------------------------------------|
| Application               | Use canonical decision record.                       |
| Prohibited interpretation | Unqualified statements such as fully assured, or any state outside the five canonical decision states. |
| Minimum evidence          | Complete decision package.                           |
| Decision effect           | Missing bounds make decision provisional or invalid. |

## APS-REQ-045 Scoring restraint

Scores may aid prioritisation but shall not create facts, hide uncertainty or override gates.

Numbers can overstate support.

| **Dimension**             | **Requirement**                                    |
|---------------------------|----------------------------------------------------|
| Application               | Publish formula, inputs, coverage and sensitivity. |
| Prohibited interpretation | Opaque overall score.                              |
| Minimum evidence          | Transparent scoring and gate record.               |
| Decision effect           | Evidence and gates govern wording.                 |

## APS-REQ-046 Maturity separation

Maturity shall remain distinct from effectiveness, evidence, risk and assurance.

Mature process can still fail a specific outcome.

| **Dimension**             | **Requirement**                             |
|---------------------------|---------------------------------------------|
| Application               | Use cumulative criteria and separate gates. |
| Prohibited interpretation | Inferring resilience from maturity.         |
| Minimum evidence          | Maturity evidence and rule-based decision.  |
| Decision effect           | Maturity contextualises, not overrides.     |

## APS-REQ-047 Reporting integrity

Reports shall give findings, limits, UNKNOWN, conflict, coverage and gate status appropriate prominence.

Selective presentation harms decisions.

| **Dimension**             | **Requirement**                               |
|---------------------------|-----------------------------------------------|
| Application               | Provide executive and technical traceability. |
| Prohibited interpretation | Green dashboards hiding critical limits.      |
| Minimum evidence          | Release and traceability review.              |
| Decision effect           | Misleading presentation is nonconformance.    |

## APS-REQ-048 No inherited assurance

External certification or vendor validation may be evidence but shall not automatically transfer.

Scope, conditions and time differ.

| **Dimension**             | **Requirement**                                |
|---------------------------|------------------------------------------------|
| Application               | Assess relevance, currency and coverage.       |
| Prohibited interpretation | Automatic pass by certification inheritance.   |
| Minimum evidence          | Third-party report and applicability analysis. |
| Decision effect           | Unsupported inheritance remains a limitation.  |

# Part XIII - Independence, competence and ethics

## APS-REQ-049 Impartiality

Conclusions shall be protected from commercial, managerial, political and vendor pressure.

Credibility depends on objective interpretation.

| **Dimension**             | **Requirement**                                                                |
|---------------------------|--------------------------------------------------------------------------------|
| Application               | Declare conflicts and separate evaluation, review and decision where required. |
| Prohibited interpretation | Outcome-contingent conclusion.                                                 |
| Minimum evidence          | Conflict register and independent review.                                      |
| Decision effect           | Unmanageable conflict blocks decision.                                         |

## APS-REQ-050 Competence

Assessment shall use collectively competent engineering, AI infrastructure, operations, security and assurance professionals.

No single discipline covers AIDCF.

| **Dimension**             | **Requirement**                                                |
|---------------------------|----------------------------------------------------------------|
| Application               | Define competence by scope and use specialists.                |
| Prohibited interpretation | General audit competence for licensed engineering conclusions. |
| Minimum evidence          | Competence matrix and assignments.                             |
| Decision effect           | Gap limits scope or requires specialist review.                |

## APS-REQ-051 Professional scepticism

Assessors shall test whether evidence supports claims and consider alternatives.

Assurance is challenge, not confirmation.

| **Dimension**             | **Requirement**                                            |
|---------------------------|------------------------------------------------------------|
| Application               | Seek corroboration, exceptions and failed cases.           |
| Prohibited interpretation | Assuming title equals evidence.                            |
| Minimum evidence          | Review notes and samples.                                  |
| Decision effect           | Unchallenged material claim cannot support high assurance. |

## APS-REQ-052 Confidentiality and minimisation

Collection and reporting shall be authorised, necessary, proportionate and protected.

Assurance does not justify overcollection.

| **Dimension**             | **Requirement**                                              |
|---------------------------|--------------------------------------------------------------|
| Application               | Apply classification, access, retention and lawful handling. |
| Prohibited interpretation | Publishing live sensitive paths.                             |
| Minimum evidence          | Authorisation and evidence inventory.                        |
| Decision effect           | Improper material is escalated and may be excluded.          |

## APS-REQ-053 Accountability

Owners retain operational responsibility; assessors retain method and conclusion responsibility.

Assurance informs but does not transfer accountability.

| **Dimension**             | **Requirement**                                    |
|---------------------------|----------------------------------------------------|
| Application               | Name owner, assessor, reviewer and decision owner. |
| Prohibited interpretation | Using assessor opinion to avoid owner decision.    |
| Minimum evidence          | Signed role and decision record.                   |
| Decision effect           | Unclear authority prevents final disposition.      |

## APS-REQ-054 Appeal and challenge

Material findings and decisions shall permit controlled challenge.

Fair challenge improves quality.

| **Dimension**             | **Requirement**                                              |
|---------------------------|--------------------------------------------------------------|
| Application               | Record grounds, evidence, reviewer independence and outcome. |
| Prohibited interpretation | Informal deletion of disputed findings.                      |
| Minimum evidence          | Appeal record.                                               |
| Decision effect           | Decision status remains explicit until resolved.             |

# Part XIV - Lifecycle and continuing assurance

## APS-REQ-055 Temporal validity

Assurance remains valid only for declared snapshot, period and conditions.

Systems, evidence and dependencies change.

| **Dimension**             | **Requirement**                                          |
|---------------------------|----------------------------------------------------------|
| Application               | State effective and expiry conditions; preserve history. |
| Prohibited interpretation | Perpetual validity claim.                                |
| Minimum evidence          | Snapshot and validity metadata.                          |
| Decision effect           | Expired conclusion cannot be current.                    |

## APS-REQ-056 Material-change reassessment

Changes affecting outcomes, dependencies, capacity, state, safeguards or evidence shall trigger impact review.

Prior decisions cannot survive unexamined change.

| **Dimension**             | **Requirement**                                               |
|---------------------------|---------------------------------------------------------------|
| Application               | Define triggers and affected assertions.                      |
| Prohibited interpretation | Updating report date without reassessment.                    |
| Minimum evidence          | Change and impact record.                                     |
| Decision effect           | Affected conclusions become limited, suspended or superseded. |

## APS-REQ-057 Incident learning

Incidents, tests and near misses shall feed back into scenarios, controls and methods.

Observed outcomes test assumptions.

| **Dimension**             | **Requirement**                                |
|---------------------------|------------------------------------------------|
| Application               | Compare event to model and update records.     |
| Prohibited interpretation | Closing incident without methodology feedback. |
| Minimum evidence          | Incident and change record.                    |
| Decision effect           | Recurring weakness may trigger broader review. |

## APS-REQ-058 Continuing-assurance restraint

Continuous assurance may be claimed only for monitored scope, signals, freshness and decision logic actually implemented.

Telemetry does not create universal assurance.

| **Dimension**             | **Requirement**                                                 |
|---------------------------|-----------------------------------------------------------------|
| Application               | State monitored objects, blind spots, cadence and human review. |
| Prohibited interpretation | Calling periodic collection continuous assurance.               |
| Minimum evidence          | Monitoring design and operation.                                |
| Decision effect           | Unmonitored conditions remain point-in-time or UNKNOWN.         |

# Part XV - Claim language and assurance decision model

## 8. Decision states and decision lifecycle

An Assurance Decision has exactly one decision state and one lifecycle state (AIDCF-002 §28; criteria and ceilings in AIDCF-010).

| **Decision state**    | **Meaning**                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------------|
| REASONABLY_ASSURED    | Sufficient appropriate evidence supports the bounded top claim; all applicable gates PASS or APPROVED_NA; no undisposed US3–US5 UNKNOWN. |
| CONDITIONALLY_ASSURED | The bounded claim is supported subject to named, owned and time-bound conditions recorded on the decision.  |
| LIMITED               | Some claims are supported, with material limitations or a gate ceiling that prevents a higher state.        |
| NOT_ASSURED           | Evidence demonstrates a material unmet condition, such as a failed gate or a demonstrated ineffective safeguard. |
| INCONCLUSIVE          | Assessment occurred but cannot support a determination, for example because of a US5 UNKNOWN or an unresolved boundary or outcome definition. |

| **Lifecycle state** | **Meaning**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| DRAFT               | Being prepared; no reliance.                                                |
| RECOMMENDED         | Decision Recommendation submitted for independent review and approval.      |
| APPROVED            | Approved by the named decision authority.                                   |
| ACTIVE              | Approved and within validity; may be relied on within its bounds.           |
| SUSPENDED           | Material change, gate failure or evidence expiry prevents reliance pending reassessment. |
| WITHDRAWN           | Decision authority removed the conclusion.                                  |
| SUPERSEDED          | A newer decision replaces this one; history retained.                       |
| EXPIRED             | Validity period ended without renewal.                                      |

"NOT ASSESSED" is not a decision state: where no relevant activity has occurred, no decision is issued. Legacy v1.0 statuses map as follows: UNKNOWN → INCONCLUSIVE; ADVERSE → NOT_ASSURED; CONDITIONAL → CONDITIONALLY_ASSURED; REASONABLY ASSURED → REASONABLY_ASSURED; SUSPENDED, WITHDRAWN and SUPERSEDED move to the lifecycle.

## 9. Assurance decision record

| **Field**                 | **Required content**                            |
|---------------------------|-------------------------------------------------|
| decisionId                | Stable, versioned identifier.                   |
| decisionQuestion          | Exact decision supported.                       |
| subject/outcomes          | Capability Instance and Service Outcomes.       |
| scope/boundary            | Inclusions, exclusions, states and period.      |
| criteria/methods          | Artifacts, profiles, tests and samples.         |
| evidence/coverage         | Manifest, sufficiency and coverage.             |
| unknowns/conflicts        | MATERIAL UNKNOWN Records (type, severity) and conflicts. |
| gateResults               | Gate Result for each of CG-01 to CG-15 (PASS, FAIL, UNKNOWN, APPROVED_NA, NOT_ASSESSED). |
| findings/residualExposure | Material results and remaining paths.           |
| state/limitations         | Decision state, lifecycle state, conditions, limitations and ceilings applied. |
| validity/triggers         | Expiry and reassessment.                        |
| roles                     | Assessor, reviewer and decision owner.          |
| snapshot                  | Machine-readable reference where applicable.    |

## 10. Claim language

| **Avoid**                   | **Use instead**                                                                                              |
|-----------------------------|--------------------------------------------------------------------------------------------------------------|
| Fully compliant             | Assessed against named criteria within stated scope; compliance not determined unless separately authorised. |
| Zero risk                   | No material adverse condition identified within tested scope; residual and UNKNOWN remain.                   |
| Fail-proof                  | Validated for specified scenario and conditions.                                                             |
| Certified by AIDCF          | Assessed against named AIDCF artifacts and capability profile; AIDCF does not certify.                     |
| Assured (unqualified)       | The named decision state, with Capability Instance, Service Outcomes, operating states, scope and date.     |
| Continuously assured        | Monitored for named signals, scope, cadence and review process.                                              |
| All dependencies identified | No additional material dependency identified within documented discovery coverage.                           |
| Control effective           | Evidence supports effectiveness for tested scope, period and conditions.                                     |
| Redundant                   | Alternative exists; independence and common-mode status stated separately.                                   |

## 11. Assurance ceilings

The ceilings below summarise how constraints limit a conclusion. The exact gate ceilings and roll-up are specified in AIDCF-010; UNKNOWN severity effects follow AIDCF-002 §31.2.

| **Constraint**                                       | **Ceiling**                                                                                                  |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| No defined Capability Instance or Service Outcome    | No decision above INCONCLUSIVE (US5; CG-01 not PASS).                                                         |
| No current boundary or architecture                  | No decision above INCONCLUSIVE (US5; CG-02 not PASS); descriptive output only.                               |
| Evidence below the control's floor (for example Q0–Q1 for a material claim) | Control result UNKNOWN; the assertion remains candidate.                                 |
| Documentary evidence only                            | DESIGN claims at most.                                                                                       |
| No representative operating or test evidence         | No OPERATION, EFFECTIVENESS or RESILIENCE claim.                                                             |
| US5 UNKNOWN                                          | Decision ≤ INCONCLUSIVE.                                                                                     |
| US4 UNKNOWN                                          | Affected gate UNKNOWN; decision ≤ LIMITED or INCONCLUSIVE per gate ceiling.                                  |
| US3 UNKNOWN                                          | Decision ≤ CONDITIONALLY_ASSURED, with a recorded condition.                                                 |
| US2 UNKNOWN                                          | Confidence ceiling CONF-2 for affected claims.                                                               |
| Gate FAIL                                            | Decision capped per gate ceiling in AIDCF-010 (NOT_ASSURED or LIMITED); scores cannot raise it.              |
| Unassessed degraded or recovery state                | No RESILIENCE claim for that state; gates whose scope includes the state are UNKNOWN.                         |
| Material change or stale evidence                    | Reassessment Trigger; affected results revert to UNKNOWN and the decision may be SUSPENDED.                  |

# Part XVI - Conformance and enforcement

## 12. Conformance levels

| **Level** | **Name**              | **Expectation**                                                        |
|-----------|-----------------------|------------------------------------------------------------------------|
| APS-CL0   | Aware                 | Uses vocabulary without formal claim.                                  |
| APS-CL1   | Declared              | Identifies applicable principles and deviations.                       |
| APS-CL2   | Assessment conformant | Applies evidence, UNKNOWN, gate, independence and decision rules.      |
| APS-CL3   | Artifact conformant   | Maps downstream requirements to APS principles.                        |
| APS-CL4   | Tool conformant       | Preserves semantics, validation, audit and human approval.             |
| APS-CL5   | Programme conformant  | A continuing-assurance programme under AIDCF-011 demonstrates impartiality, independent review, surveillance of validity and controlled claims. |

The levels were labelled P0 to P5 in v1.0; they are renamed because P0 to P5 is the AIDCF-008 provenance quality rating. APS-CL5 is a statement about how an assurance programme is run; it is not a certification and confers no right to certify.

## 13. Nonconformance

| **Class**   | **Examples**                                                                                        | **Response**                                                      |
|-------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Critical    | Fabricated evidence, hidden gate failure, unsafe test, suppressed conflict, a claim that AIDCF has certified. | Stop claim, preserve evidence, escalate and independently review. |
| Major       | Unsupported effectiveness, UNKNOWN converted to CONFORMING or PASS, boundary omission, unmanaged conflict. | Withdraw/limit and remediate before release.               |
| Minor       | Non-material metadata or traceability defect.                                                       | Correct under quality review.                                     |
| Observation | Improvement opportunity without breach.                                                             | Track improvement.                                                |

## 14. Exception rule

No exception may waive a constitutional invariant. An alternative may vary implementation only where it demonstrably preserves principle intent and does not weaken safety, evidence, transparency, independence or decision integrity.

| **Exception field** | **Requirement**                         |
|---------------------|-----------------------------------------|
| principle/rule      | Exact item affected.                    |
| reason              | Why standard approach is impracticable. |
| alternative         | How intent remains satisfied.           |
| impact              | Evidence and decision effect.           |
| owner/approver      | Authorised and independent roles.       |
| duration            | Time-bounded validity.                  |
| monitoring          | Conditions and reassessment.            |
| disclosure          | Report and machine-readable placement.  |
| closure             | Evidence of end state.                  |

# Part XVII - Machine-readable constitutional profile

## 15. Entities and relationships

| **Entity**          | **Purpose**                        |
|---------------------|------------------------------------|
| AssurancePrinciple  | Canonical constitutional rule.     |
| PrincipleObligation | Required application.              |
| Prohibition         | Disallowed practice.               |
| AssuranceClaim      | Precise proposition.               |
| CriticalGate        | Non-compensating prerequisite.     |
| EvidenceRequirement | Minimum support.                   |
| UnknownRecord       | Unresolved information and effect. |
| Limitation          | Restriction on interpretation.     |
| AssuranceDecision   | Bounded authorised conclusion.     |
| ExceptionRecord     | Approved equivalent treatment.     |
| Nonconformance      | Principle breach.                  |
| ReassessmentTrigger | Condition requiring review.        |

| **Relationship**         | **Meaning**                                      | **AIDCF-014 exchange type**                     |
|--------------------------|--------------------------------------------------|-------------------------------------------------|
| GOVERNS                  | Principle constrains artifact, claim or process. | GOVERNED_BY (inverse)                           |
| REQUIRES                 | Principle mandates obligation.                   | Constitutional profile only                     |
| PROHIBITS                | Principle disallows practice.                    | Constitutional profile only                     |
| SUPPORTED_BY             | Claim/decision linked to evidence.               | EVIDENCED_BY; SUPPORTS from the evidence        |
| LIMITED_BY               | Claim constrained by limitation/UNKNOWN.         | CONSTRAINS (inverse)                            |
| BLOCKED_BY               | Gate result caps the conclusion.                 | CONSTRAINS (inverse, from the GateResult)       |
| REVIEWED_BY              | Accountable review.                              | REVIEWED_BY                                     |
| SUPERSEDES               | New version replaces without erasing history.    | SUPERSEDES                                      |
| TRIGGERS_REASSESSMENT_OF | Change affects prior decision.                   | TRIGGERS_REASSESSMENT                           |
| CONFORMS_TO              | Artifact/tool declares tested conformance.       | Constitutional profile only                     |

CriticalGate, EvidenceRequirement, UnknownRecord, AssuranceDecision and ReassessmentTrigger are the classes of AIDCF-003 Part XV and AIDCF-014 §7; AssuranceClaim corresponds to aidcf:Assertion.

## 16. Publication package

| **File**                      | **Purpose**                              |
|-------------------------------|------------------------------------------|
| aidcf-aps-v1.0.owl            | Formal constitutional ontology.          |
| aidcf-aps-v1.0.ttl            | RDF/Turtle serialisation.                |
| aidcf-aps-context-v1.0.jsonld | JSON-LD context.                         |
| aidcf-aps-schema-v1.0.json    | Decision, gate and exception schemas.    |
| aidcf-aps-shapes-v1.0.ttl     | Validation shapes.                       |
| principles-v1.0.csv           | Principle registry.                      |
| critical-gates-v1.0.csv       | Gate catalogue.                          |
| claim-language-v1.0.csv       | Controlled wording.                      |
| conformance-tests/            | Positive/negative fixtures.              |
| CHANGELOG.md / MIGRATION.md   | Release history and transition guidance. |

## 17. Validation rules

| **Rule**    | **Validation statement**                                           |
|-------------|--------------------------------------------------------------------|
| APS-VAL-001 | Every downstream requirement maps to at least one APS-REQ principle. |
| APS-VAL-002 | Every final decision identifies capability and outcomes.           |
| APS-VAL-003 | Every decision has scope, state, period, evidence and limitations. |
| APS-VAL-004 | Every material assertion has evidence or explicit UNKNOWN.         |
| APS-VAL-005 | Every gate CG-01 to CG-15 has a Gate Result and evidence.          |
| APS-VAL-006 | No score or maturity overrides a gate.                             |
| APS-VAL-007 | No UNKNOWN becomes a favourable numeric, boolean, result or gate state. |
| APS-VAL-008 | Every effectiveness claim identifies tested conditions.            |
| APS-VAL-009 | Every material change links affected decisions.                    |
| APS-VAL-010 | Every AI-generated item remains candidate until reviewed.          |
| APS-VAL-011 | Every exception is time-bound and preserves intent.                |
| APS-VAL-012 | Every nonconformance has disposition.                              |
| APS-VAL-013 | Every integrated package preserves native decisions.               |
| APS-VAL-014 | Every published claim uses a canonical decision state.             |
| APS-VAL-015 | Every superseded decision remains traceable.                       |

# Part XVIII - Worked applications and anti-patterns

## 18. AI training capability

| **Step**     | **Application**                                                                        |
|--------------|----------------------------------------------------------------------------------------|
| Capability   | Define training capacity, completion, checkpoint and recovery outcomes.                |
| Boundary     | Declare halls, clusters, storage, fabric, operators and providers.                     |
| Dependencies | Trace power, liquid cooling, management, identity, scheduler, storage, spares and OEM. |
| Failure      | Analyse cooling, power, metadata, congestion and common-mode firmware scenarios.       |
| Evidence     | Separate design, as-built, commissioned, operating and tested evidence.                |
| Gates        | All fifteen gates evaluated; decisive here are CG-05 power, CG-06 thermal, CG-07 control systems, CG-08 (including checkpoint storage), CG-10 recovery and CG-11 evidence. |
| Decision     | A bounded decision state (for example CONDITIONALLY_ASSURED) with UNKNOWN Records, residual paths, conditions and triggers. |

## 19. Colocation capability

| **Issue**                | **Treatment**                                                    |
|--------------------------|------------------------------------------------------------------|
| Provider certification   | Evidence only; no automatic inheritance.                         |
| Shared responsibility    | Owner/operator/custodian by function and state.                  |
| Excluded provider system | Visible external dependency with confidence limit.               |
| Boundary                 | Physical, network, identity, operational and evidence crossings. |
| Testing constraint       | Authorised safe validation and disclosed limitation.             |
| Critical UNKNOWN         | Evidence-inaccessible shared dependency may cap assurance.       |

## 20. Continuous monitoring

| **Question**             | **Required answer**                                |
|--------------------------|----------------------------------------------------|
| What is monitored?       | Named entities, relations, safeguards and metrics. |
| What is not?             | Blind spots and manual dependencies.               |
| How current?             | Collection/review cadence and latency.             |
| What changes a decision? | Threshold, gate and human-review logic.            |
| Coverage?                | Assets, states, sites, periods and scenarios.      |
| Point-in-time elements?  | Tests, inspections, studies and interviews.        |
| Permitted claim          | Only monitored evidenced scope.                    |

## 21. Anti-patterns

| **ID**  | **Anti-pattern**                                                        |
|---------|-------------------------------------------------------------------------|
| APAT-01 | Checklist completion presented as capability assurance.                 |
| APAT-02 | Facility rating inherited by every AI workload.                         |
| APAT-03 | Average score masks critical power, cooling, recovery or evidence gate. |
| APAT-04 | Redundancy claimed from asset count.                                    |
| APAT-05 | Policy used to claim technical effectiveness.                           |
| APAT-06 | UNKNOWN removed to complete dashboard.                                  |
| APAT-07 | Normal-state test generalised to recovery.                              |
| APAT-08 | External dependency omitted due to contract.                            |
| APAT-09 | Graph connection treated as authority or causality.                     |
| APAT-10 | Tool finding released without human approval.                           |
| APAT-11 | Maturity used as proxy for resilience.                                  |
| APAT-12 | Planned remediation treated as gate closure.                            |
| APAT-13 | Report treated as current after material change.                        |
| APAT-14 | Sensitive path published without protection.                            |
| APAT-15 | Any statement that AIDCF certifies, or an AIDCF decision presented as a certificate. |

# Appendix A - Principle registry

Each principle is a requirement of this standard and carries an APS-REQ identifier. Numbers are unchanged from v1.0, so the short form APS-NNN used in v1.0 and in the principle mappings of the AIDCF-007A registry is an exact alias of APS-REQ-NNN.

| **ID**      | **Principle**                    |
|-------------|----------------------------------|
| APS-REQ-001 | Capability-first assurance       |
| APS-REQ-002 | Outcome alignment                |
| APS-REQ-003 | Function before product          |
| APS-REQ-004 | Outcome-centric materiality      |
| APS-REQ-005 | Explicit boundary                |
| APS-REQ-006 | Operating-envelope discipline    |
| APS-REQ-007 | State-specific assurance         |
| APS-REQ-008 | Reality over intent              |
| APS-REQ-009 | Proportionate depth              |
| APS-REQ-010 | Dependency visibility            |
| APS-REQ-011 | External dependency continuity   |
| APS-REQ-012 | Shared-dependency scrutiny       |
| APS-REQ-013 | Concentration awareness          |
| APS-REQ-014 | Dependency ownership             |
| APS-REQ-015 | Failure-chain analysis           |
| APS-REQ-016 | Cross-domain propagation         |
| APS-REQ-017 | Compound conditions              |
| APS-REQ-018 | Resilience lifecycle             |
| APS-REQ-019 | Recovery evidence                |
| APS-REQ-020 | Safe validation                  |
| APS-REQ-021 | Safeguard reality                |
| APS-REQ-022 | Effectiveness by condition       |
| APS-REQ-023 | Safeguard dependency             |
| APS-REQ-024 | Defence diversity                |
| APS-REQ-025 | Residual-path disclosure         |
| APS-REQ-026 | Evidence before conclusion       |
| APS-REQ-027 | Evidence provenance              |
| APS-REQ-028 | Evidence sufficiency             |
| APS-REQ-029 | Evidence currency                |
| APS-REQ-030 | Assertion-specific confidence    |
| APS-REQ-031 | Conflict retention               |
| APS-REQ-032 | UNKNOWN preservation             |
| APS-REQ-033 | No assumed favourable state      |
| APS-REQ-034 | Limitation transparency          |
| APS-REQ-035 | Not-applicable discipline        |
| APS-REQ-036 | Critical-gate protection         |
| APS-REQ-037 | Non-compensation                 |
| APS-REQ-038 | Gate proportionality             |
| APS-REQ-039 | Gate closure                     |
| APS-REQ-040 | System-of-systems assurance      |
| APS-REQ-041 | Graph-native traceability        |
| APS-REQ-042 | Federated assurance              |
| APS-REQ-043 | Human approval of inference      |
| APS-REQ-044 | Bounded decision                 |
| APS-REQ-045 | Scoring restraint                |
| APS-REQ-046 | Maturity separation              |
| APS-REQ-047 | Reporting integrity              |
| APS-REQ-048 | No inherited assurance           |
| APS-REQ-049 | Impartiality                     |
| APS-REQ-050 | Competence                       |
| APS-REQ-051 | Professional scepticism          |
| APS-REQ-052 | Confidentiality and minimisation |
| APS-REQ-053 | Accountability                   |
| APS-REQ-054 | Appeal and challenge             |
| APS-REQ-055 | Temporal validity                |
| APS-REQ-056 | Material-change reassessment     |
| APS-REQ-057 | Incident learning                |
| APS-REQ-058 | Continuing-assurance restraint   |

# Appendix B - Canonical critical-gate catalogue

The fifteen gates below are canonical across AIDCF. Their detailed criteria, roll-up and decision ceilings are specified in AIDCF-010; the evidence floors are those of AIDCF-008. The capability profile determines applicability (a gate is set aside only as APPROVED_NA with approved boundary rationale) and the parameters of each criterion.

| **ID** | **Gate**                                          | **Scope (what it protects)**                                                                                                              | **Evidence floor** |
|--------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| CG-01  | Capability and outcome definition                 | Capability Instance, Service Outcomes, tolerances, criticality and decision question are defined, owned and approved                      | S3                 |
| CG-02  | Boundary and architecture integrity               | Assessment boundary, current architecture, as-built reconciliation and exclusions                                                         | S3                 |
| CG-03  | Critical dependency visibility                    | Material internal and external dependencies, common-mode and concentration are identified and owned                                       | S4                 |
| CG-04  | Life safety and hazardous energy                  | Fire, electrical arc-flash and shock, hazardous fluids and chemicals, confined space, refrigerants, battery thermal runaway and safe work | S4                 |
| CG-05  | Resilient electrical supply                       | Utility, distribution, UPS/BESS, generation, fuel, protection and power quality sufficient for the outcome across states                  | S5                 |
| CG-06  | Thermal continuity                                | Heat-removal path (air, liquid, facility water, heat rejection) sufficient across states, including transients                            | S5                 |
| CG-07  | Critical control-system integrity                 | BMS, EPMS, CDU, PLC, SCADA and automation function safely and fail safe, and are configured and governed                                  | S4                 |
| CG-08  | Compute, storage and network functional integrity | Accelerators, storage and fabrics deliver required function, performance and integrity                                                    | S4                 |
| CG-09  | Failure containment                               | Fault domains, isolation and blast-radius limits prevent propagation beyond tolerance                                                     | S4                 |
| CG-10  | Recovery readiness                                | Restoration of the outcome (power, cooling, compute, data and checkpoint, network, control plane) within tolerance is planned and tested  | S5                 |
| CG-11  | Evidence sufficiency                              | Evidence for decisive claims meets floors (meta-gate, evaluated across all controls)                                                      | S4                 |
| CG-12  | Critical UNKNOWN                                  | No unresolved US4 or US5 UNKNOWN without disposition (meta-gate, evaluated across all controls)                                           | S3                 |
| CG-13  | Responsibility and authority                      | Every critical function and dependency has an accountable owner and decision authority                                                    | S3                 |
| CG-14  | Change control                                    | Material changes are controlled, impact-assessed and validated                                                                            | S4                 |
| CG-15  | Integrated digital authority over infrastructure  | Identity, privilege, remote access and control-plane reach over facility and AI infrastructure are bounded, monitored and recoverable     | S4                 |

**Gate results.** A Gate Result is exactly one of PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED. There is no conditional gate state: conditions are expressed only on the Decision Recommendation and Assurance Decision.

**Roll-up (summary of AIDCF-010).** For an in-scope gate: FAIL if any in-scope CRITICAL control is NONCONFORMING or PARTIAL, or a gate criterion is demonstrated not met; otherwise UNKNOWN if any in-scope CRITICAL control is UNKNOWN or NOT_ASSESSED, gate evidence is below floor, or a US4 UNKNOWN is attached; otherwise PASS if all CRITICAL controls are CONFORMING at the required claim type, all criteria are met with evidence at or above floor, and every NONCONFORMING SUPPORTING control has a documented gate-level evaluation concluding no defeat. PARTIAL never yields PASS. CRITICAL and SUPPORTING roles are assigned per control in the AIDCF-007A registry.

## Gate record schema

| **Field**                 | **Requirement**                        |
|---------------------------|----------------------------------------|
| gateId                    | CG-01 to CG-15 and profile/version.    |
| subject/outcome           | Capability and Outcome protected.      |
| criterion                 | Testable prerequisite (AIDCF-010).     |
| applicability             | Why it applies, or APPROVED_NA rationale and approver. |
| criticalControls          | In-scope CRITICAL controls and their results. |
| failure/unknown condition | When the gate is FAIL or UNKNOWN under the roll-up. |
| evidence floor            | Minimum sufficiency (S3 to S5).        |
| methods                   | Analysis, inspection, test and review. |
| status                    | PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED. |
| decision effect           | Ceiling applied to the decision state. |
| owner/reviewer            | Accountable roles.                     |
| closure                   | Remediation and retest.                |

# Appendix C - UNKNOWN and limitation schemas

| **UNKNOWN field**     | **Content**                                             |
|-----------------------|---------------------------------------------------------|
| unknownId             | Stable ID.                                              |
| subject/attribute     | What is unresolved.                                     |
| reason                | Absent, inaccessible, stale, conflicting or not tested. |
| potential consequence | Why it matters.                                         |
| type                  | U1–U10 (AIDCF-008 §35): why it is unknown.              |
| severity              | US1–US5 (below) with rationale.                         |
| evidence needed       | Resolution requirement.                                 |
| owner                 | Owner if known.                                         |
| decision effect       | Effect required by its severity.                        |
| status/history        | Open, resolved, accepted or superseded.                 |

| **Severity** | **Name**  | **Test (first that applies, top-down)**                                      | **Decision effect**                                              |
|--------------|-----------|------------------------------------------------------------------------------|------------------------------------------------------------------|
| US5          | Systemic  | Affects the boundary, a Capability or Outcome definition, or two or more gates | Decision ≤ INCONCLUSIVE                                         |
| US4          | Critical  | Affects a gate-critical control or a gate criterion (CG-12 trigger)          | Gate UNKNOWN; decision ≤ LIMITED or INCONCLUSIVE per gate ceiling |
| US3          | Material  | Could change a control result or a decision condition but no gate            | Decision ≤ CONDITIONALLY_ASSURED; condition recorded             |
| US2          | Moderate  | Affects confidence but not any result                                        | Confidence ceiling CONF-2 for affected claims                    |
| US1          | Low       | No plausible effect on any result or condition                               | Record only                                                      |

The severity scale is canonical in AIDCF-002 §31.2.

| **Limitation field** | **Content**                                                        |
|----------------------|--------------------------------------------------------------------|
| limitationId         | Stable ID.                                                         |
| affected claim       | Claim/decision affected.                                           |
| type                 | Scope, evidence, state, method, access, time, competence or legal. |
| description          | Precise restriction.                                               |
| materiality          | Decision effect.                                                   |
| owner/treatment      | Resolution owner and treatment.                                    |
| visibility           | Where disclosed.                                                   |
| trigger              | Review/expiry condition.                                           |

# Appendix D - Conformance checklist

| **Check** | **Requirement**                                   |
|-----------|---------------------------------------------------|
| D-01      | Capability Instance and Outcomes defined.         |
| D-02      | Boundary, envelope, states and period declared.   |
| D-03      | Dependencies and providers visible.               |
| D-04      | Failure and recovery paths analysed cross-domain. |
| D-05      | Safeguards validated by condition.                |
| D-06      | Evidence linked to assertions with provenance.    |
| D-07      | UNKNOWN, conflicts and limitations preserved.     |
| D-08      | Critical gates defined and non-compensating.      |
| D-09      | Scores/maturity do not override gates.            |
| D-10      | Decision bounded and controlled.                  |
| D-11      | Competence, impartiality and review demonstrated. |
| D-12      | Change and reassessment triggers stated.          |
| D-13      | Tool output retains human approval.               |
| D-14      | Sensitive evidence protected.                     |
| D-15      | Exceptions and nonconformance controlled.         |

# Appendix E - Review and acceptance record

| **Review role**                      | **Status**      | **Focus**                          |
|--------------------------------------|-----------------|------------------------------------|
| Methodology author                   | Draft completed | Constitutional coherence.          |
| AIDCF ontology reviewer              | Pending         | AIDCF-003 consistency.             |
| Failure/resilience reviewer          | Pending         | AIDCF-004 consistency.             |
| AI Trust Graph integration reviewer  | Pending         | AIDCF-005 consistency.             |
| Electrical engineer                  | Pending         | Power gate validity.               |
| Mechanical/cooling engineer          | Pending         | Thermal gate validity.             |
| Compute/storage/network reviewer     | Pending         | AI infrastructure outcomes.        |
| Operations/OT reviewer               | Pending         | State, automation and authority.   |
| Assurance reviewer                   | Pending         | Evidence, independence and claims. |
| Claims and external-scheme reviewer  | Pending         | No certification claims; interface with third-party conformity-assessment schemes. |
| Security/privacy reviewer            | Pending         | Evidence/path protection.          |
| Legal/IP/publication reviewer        | Pending         | Rights and claims.                 |
| Independent practitioner             | Pending         | Reproducibility.                   |
| Public release                       | Not approved    | All gates closed.                  |

No approval has been granted for this document; the record states review status only.

## Acceptance criteria

- Downstream artifacts can map to this standard without contradiction.

- Evidence, UNKNOWN, gates, independence and bounded decisions are enforceable.

- No principle implies legal compliance, engineering approval or certification by itself.

- Machine-readable implementation does not change meaning.

- Independent multidisciplinary and publication review is completed.

## Change record

| **Version** | **Status**              | **Summary**                                      |
|-------------|-------------------------|--------------------------------------------------|
| 0.1         | Architecture draft          | Constitutional role and principle families.      |
| 0.5         | Integrated draft            | Decision, gate, ethics and conformance models.   |
| 1.0         | Controlled-review draft     | Comprehensive baseline for downstream artifacts. |
| 1.1         | Draft for controlled review | Certification claims removed; vocabularies, gates and chain aligned to AIDCF-002; APS-REQ IDs. |

## Final constitutional doctrine

AIDCF may express confidence only where the decision question is clear, the capability and outcomes are defined, dependencies and failure paths are sufficiently understood, safeguards are evidenced within relevant conditions, uncertainty remains visible, critical gates are satisfied, competent and impartial review has occurred, and the conclusion is bounded by scope, state, time and evidence. Where these conditions are not met, AIDCF shall reduce, condition, suspend or withhold assurance rather than manufacture certainty.
