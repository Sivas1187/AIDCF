> Markdown edition (source of truth). PDF: [AIDCF-006_Assurance_Principles_Standard_v1.0.pdf](AIDCF-006_Assurance_Principles_Standard_v1.0.pdf)

**AIDCF**

# ASSURANCE PRINCIPLES STANDARD

*AI Data Centre Facilities Assurance Framework*

Version 1.0

The constitutional rules governing claims, evidence, uncertainty, critical gates, decisions, independence and responsible use

Artifact ID: AIDCF-APS-001  
Artifact type: Normative constitutional standard  
Status: Draft for controlled review  
Author: Siva Sethumadhavan  
Release 1: Foundational Methodology

Assurance is bounded confidence supported by evidence, not confidence created by presentation.

# Document control

| **Field**            | **Value**                                                                                                                                 |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Title                | AIDCF Assurance Principles Standard v1.0                                                                                                  |
| Artifact ID          | AIDCF-APS-001                                                                                                                             |
| Artifact type        | Normative constitutional standard                                                                                                         |
| Status               | Draft for controlled review                                                                                                               |
| Author               | Siva Sethumadhavan                                                                                                                        |
| Depends on           | AIDCF Manifesto v1.0; Core Conceptual Model v1.0; AIDCF-003; AIDCF-004; AIDCF-005                                                         |
| Authority            | Governs downstream controls, evidence, assessment, scoring, maturity, reporting, certification and tooling.                               |
| Publication boundary | Independent methodology; not law, licensed engineering, safety approval, accredited certification or authorisation for hazardous testing. |

# Executive thesis

AIDCF assurance is a bounded, evidence-supported and accountable conclusion about whether the facilities and infrastructure supporting a defined AI Capability Instance can be reasonably relied upon to achieve required Service Outcomes within declared boundaries, states, operating conditions and time. It is not a guarantee, a generic quality label, a score, a maturity level or an inherited certificate.

## Constitutional reasoning chain

Decision Question -\> Capability Instance -\> Service Outcomes -\> Boundary and Operating Envelope -\> Assets and Dependencies -\> Adverse Conditions and Failure Paths -\> Safeguards and Recovery -\> Evidence and UNKNOWN -\> Critical Gates -\> Independent Review -\> Bounded Assurance Decision

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

## 2. Artifact precedence

| **Layer**             | **Authority**                                               |
|-----------------------|-------------------------------------------------------------|
| Manifesto             | Purpose, identity and public commitments.                   |
| Core Conceptual Model | Canonical meanings and reasoning.                           |
| Artifacts 003-005     | Ontology, failure semantics and graph integration.          |
| Artifact 006          | Constitutional assurance rules.                             |
| Downstream standards  | Operational controls, methods, scores, reports and schemes. |
| Tooling               | Declared implementation only, never hidden authority.       |

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

# Part II - Assurance architecture and terminology

## 5. Definition of assurance

Assurance is a reasoned and reviewable level of confidence, for a defined decision, that specified claims about a Capability Instance and supporting infrastructure are supported by sufficient appropriate evidence within a declared scope, state, period and set of limitations.

## 6. Assurance levels

| **Level**         | **Permitted conclusion**                                 | **Minimum basis**                                  |
|-------------------|----------------------------------------------------------|----------------------------------------------------|
| A0 No assurance   | No positive conclusion.                                  | No/insufficient evidence or critical uncertainty.  |
| A1 Descriptive    | Known state described.                                   | Traceable inventory and observations.              |
| A2 Design         | Requirements/design supported.                           | Approved design evidence and competent review.     |
| A3 Implementation | Measures implemented in observed scope.                  | Corroborated technical/as-built evidence.          |
| A4 Operating      | Measures effective for tested conditions/period.         | Representative operating/test evidence.            |
| A5 Resilience     | Capability sustained or recovered for defined scenarios. | Cross-domain scenario, gate and recovery evidence. |

## 7. Mandatory distinctions

| **Do not collapse**         | **Reason**                                                      |
|-----------------------------|-----------------------------------------------------------------|
| Assurance / guarantee       | Assurance is bounded confidence, not certainty.                 |
| Evidence grade / confidence | Support strength differs from reviewer confidence.              |
| Control / safeguard         | Requirement differs from real-world mechanism.                  |
| Maturity / effectiveness    | Institutionalisation differs from performance.                  |
| Score / decision            | Number cannot replace reasoning and gates.                      |
| UNKNOWN / failure           | Missing knowledge differs from demonstrated adverse state.      |
| Not Applicable / not tested | Irrelevance differs from missing activity.                      |
| Failover / recovery         | Transfer differs from restoration.                              |
| Redundancy / resilience     | Duplication does not prove outcome continuity.                  |
| Connection / authority      | Reachability does not prove permission or consequential action. |

# Part III - Capability and outcome principles

## APS-001 Capability-first assurance

The primary object of AIDCF assurance shall be a defined Capability Instance and required Service Outcomes.

Assets and controls matter because of the functions and outcomes they support.

| **Dimension**             | **Requirement**                                                                             |
|---------------------------|---------------------------------------------------------------------------------------------|
| Application               | Define capability, owner, architecture baseline, lifecycle stage, outcomes and criticality. |
| Prohibited interpretation | Generic facility assurance without a Capability Instance.                                   |
| Minimum evidence          | Capability record, outcome requirements and architecture.                                   |
| Decision effect           | Missing capability or outcome blocks positive capability assurance.                         |

## APS-002 Outcome alignment

Every material test, control, finding and recommendation shall identify the Service Outcome or decision it protects.

Outcome alignment prevents checklist completion from becoming the objective.

| **Dimension**             | **Requirement**                                                       |
|---------------------------|-----------------------------------------------------------------------|
| Application               | Record affected outcome, tolerance, time sensitivity and consequence. |
| Prohibited interpretation | Control activity justified only because it is customary.              |
| Minimum evidence          | Service requirements and impact analysis.                             |
| Decision effect           | Unlinked activity cannot determine capability assurance.              |

## APS-003 Function before product

Required functions shall be defined independently from products implementing them.

This preserves vendor neutrality and enables substitution and failure analysis.

| **Dimension**             | **Requirement**                                                   |
|---------------------------|-------------------------------------------------------------------|
| Application               | Define function, demand, duration, state and implementing assets. |
| Prohibited interpretation | Using a vendor product name as the control objective.             |
| Minimum evidence          | Functional requirements and observed implementation.              |
| Decision effect           | Unclear function limits design and effectiveness conclusions.     |

## APS-004 Outcome-centric materiality

Materiality shall be based on plausible effect on outcomes, safety, stakeholders and obligations.

Issue count, novelty and cost alone do not establish materiality.

| **Dimension**             | **Requirement**                                                                   |
|---------------------------|-----------------------------------------------------------------------------------|
| Application               | Assess magnitude, duration, concentration, recoverability and stakeholder effect. |
| Prohibited interpretation | Averaging catastrophic and trivial effects.                                       |
| Minimum evidence          | Capability impact analysis and accountable criteria.                              |
| Decision effect           | Materiality determines depth, gates and escalation.                               |

# Part IV - Scope, boundary and state principles

## APS-005 Explicit boundary

Every conclusion shall declare included systems, locations, organisations, states and time.

A boundary makes claims interpretable.

| **Dimension**             | **Requirement**                                                   |
|---------------------------|-------------------------------------------------------------------|
| Application               | Record inclusions, exclusions and boundary-crossing dependencies. |
| Prohibited interpretation | Treating out-of-scope as non-existent.                            |
| Minimum evidence          | Approved scope, architecture and dependency record.               |
| Decision effect           | Unclear boundary blocks final assurance wording.                  |

## APS-006 Operating-envelope discipline

Assurance applies only within defined load, environmental, capacity, duration and state conditions.

Evidence in one condition cannot automatically support another.

| **Dimension**             | **Requirement**                                                 |
|---------------------------|-----------------------------------------------------------------|
| Application               | State demand, headroom, limits, duration and applicable states. |
| Prohibited interpretation | Generalising low-load tests to peak AI load.                    |
| Minimum evidence          | Operating envelope, telemetry and test conditions.              |
| Decision effect           | Claims outside the envelope remain unassured.                   |

## APS-007 State-specific assurance

Normal, degraded, maintenance, emergency, recovery and transition states shall be considered separately where material.

Normal operation can hide maintenance or recovery fragility.

| **Dimension**             | **Requirement**                                       |
|---------------------------|-------------------------------------------------------|
| Application               | Identify state coverage for each claim and safeguard. |
| Prohibited interpretation | Assuming normal-state evidence proves all states.     |
| Minimum evidence          | State model, work controls, incidents and tests.      |
| Decision effect           | Uncovered critical states cap resilience assurance.   |

## APS-008 Reality over intent

Observed and tested reality shall take precedence over intended design where they conflict.

Intent cannot prove current implementation.

| **Dimension**             | **Requirement**                                                                  |
|---------------------------|----------------------------------------------------------------------------------|
| Application               | Separate intended, designed, installed, commissioned, observed and tested state. |
| Prohibited interpretation | Silently reconciling records to match design.                                    |
| Minimum evidence          | Current configuration, observation and test evidence.                            |
| Decision effect           | Conflict is disclosed and evaluated.                                             |

## APS-009 Proportionate depth

Assessment depth shall match consequence, complexity, change, uncertainty and decision need.

Proportionality prevents both superficiality and unsafe overtesting.

| **Dimension**             | **Requirement**                                    |
|---------------------------|----------------------------------------------------|
| Application               | Document depth, sampling and escalation rationale. |
| Prohibited interpretation | One fixed checklist depth for all capabilities.    |
| Minimum evidence          | Scoping, criticality and test authorisation.       |
| Decision effect           | Insufficient depth limits the conclusion.          |

# Part V - Dependency and concentration principles

## APS-010 Dependency visibility

Material dependencies shall be explicit, typed, directional and state-aware.

Hidden dependencies undermine redundancy and recovery claims.

| **Dimension**             | **Requirement**                                                                       |
|---------------------------|---------------------------------------------------------------------------------------|
| Application               | Map upstream, downstream, shared, external, human, control and recovery dependencies. |
| Prohibited interpretation | Omitting outsourced dependencies.                                                     |
| Minimum evidence          | Dependency graph, architecture, contracts and observed paths.                         |
| Decision effect           | Critical hidden dependency may trigger a gate.                                        |

## APS-011 External dependency continuity

External providers remain part of capability reasoning even when outside direct assessment.

Exclusion does not remove consequence.

| **Dimension**             | **Requirement**                                                                       |
|---------------------------|---------------------------------------------------------------------------------------|
| Application               | Identify provider, service, capacity, evidence access, failure effect and escalation. |
| Prohibited interpretation | Assuming an SLA proves continuity.                                                    |
| Minimum evidence          | Contracts, provider evidence and scenario analysis.                                   |
| Decision effect           | Weakly evidenced critical external dependency caps assurance.                         |

## APS-012 Shared-dependency scrutiny

Nominal alternatives shall be examined for common causes, routes, controllers, identities, teams and providers.

Duplication does not establish independence.

| **Dimension**             | **Requirement**                                                  |
|---------------------------|------------------------------------------------------------------|
| Application               | Map shared fault domains and common-mode events.                 |
| Prohibited interpretation | Calling dual paths resilient without shared-dependency analysis. |
| Minimum evidence          | Topology, configuration and test evidence.                       |
| Decision effect           | Unresolved common mode prevents independence claims.             |

## APS-013 Concentration awareness

Capability, capacity, authority, supplier and knowledge concentration shall be explicit.

Concentration magnifies consequence.

| **Dimension**             | **Requirement**                                                 |
|---------------------------|-----------------------------------------------------------------|
| Application               | Identify aggregation points, blast radius and recovery options. |
| Prohibited interpretation | Dismissing concentration using component reliability alone.     |
| Minimum evidence          | Capacity, topology, role and provider data.                     |
| Decision effect           | Critical concentration increases scenario priority.             |

## APS-014 Dependency ownership

Every material dependency shall have an owner or explicit UNKNOWN owner.

Responsibility is required for evidence, treatment and recovery.

| **Dimension**             | **Requirement**                                              |
|---------------------------|--------------------------------------------------------------|
| Application               | Assign owner, operator, provider, maintainer and escalation. |
| Prohibited interpretation | Treating contract assignment as proof of control.            |
| Minimum evidence          | Responsibility model and operating procedure.                |
| Decision effect           | Unowned critical dependency is a responsibility gap.         |

# Part VI - Failure, resilience and recovery principles

## APS-015 Failure-chain analysis

Material failures shall be analysed from initiating condition through mode, effect, propagation, consequence, safeguard and recovery.

Stopping at component failure misses capability impact.

| **Dimension**             | **Requirement**                                       |
|---------------------------|-------------------------------------------------------|
| Application               | Apply Artifact 004 distinctions and dependency paths. |
| Prohibited interpretation | Collapsing cause, mode, effect and consequence.       |
| Minimum evidence          | Scenario records and failure analysis.                |
| Decision effect           | Incomplete chain limits resilience conclusions.       |

## APS-016 Cross-domain propagation

Failure analysis shall cross domain boundaries wherever dependencies transmit effect.

Resilience emerges from interactions.

| **Dimension**             | **Requirement**                                                         |
|---------------------------|-------------------------------------------------------------------------|
| Application               | Trace power, cooling, compute, storage, network and operations effects. |
| Prohibited interpretation | Siloed domain assessment as end-to-end assurance.                       |
| Minimum evidence          | Cross-domain graph, telemetry and tests.                                |
| Decision effect           | Unexamined material path remains UNKNOWN.                               |

## APS-017 Compound conditions

Credible combinations of failure, maintenance, demand, threat and recovery shall be considered.

Systemic failures often require multiple conditions.

| **Dimension**             | **Requirement**                                                  |
|---------------------------|------------------------------------------------------------------|
| Application               | Analyse latent, sequential, compound and common-cause scenarios. |
| Prohibited interpretation | Dismissing combinations solely on individual rarity.             |
| Minimum evidence          | Scenario basis, incident data and stress analysis.               |
| Decision effect           | Catastrophic credible scenario may become a gate.                |

## APS-018 Resilience lifecycle

Resilience shall cover anticipate, prevent, detect, decide, respond, contain, withstand, degrade, recover and adapt as applicable.

Prevention alone is not resilience.

| **Dimension**             | **Requirement**                                                     |
|---------------------------|---------------------------------------------------------------------|
| Application               | Map safeguards and gaps across the lifecycle.                       |
| Prohibited interpretation | Equating monitoring or redundancy with resilience.                  |
| Minimum evidence          | Safeguard model, exercises and recovery records.                    |
| Decision effect           | Missing essential lifecycle capability limits resilience assurance. |

## APS-019 Recovery evidence

Recovery claims shall identify prerequisites, sequence, authority, resources and validation.

A plan does not prove recoverability.

| **Dimension**             | **Requirement**                                           |
|---------------------------|-----------------------------------------------------------|
| Application               | Validate critical recovery steps and dependencies safely. |
| Prohibited interpretation | Assuming failover equals recovery.                        |
| Minimum evidence          | Recovery tests, incidents and baselines.                  |
| Decision effect           | Untested critical recovery remains design intent.         |

## APS-020 Safe validation

Validation shall be authorised, competent, proportionate and non-destructive by default.

Assurance does not justify new unmanaged risk.

| **Dimension**             | **Requirement**                                                                |
|---------------------------|--------------------------------------------------------------------------------|
| Application               | Use least intrusive sufficient method, rules of engagement and abort criteria. |
| Prohibited interpretation | Hazardous live testing without explicit authority.                             |
| Minimum evidence          | Authorisation, risk assessment, test plan and results.                         |
| Decision effect           | Unsafe evidence is not accepted and is escalated.                              |

# Part VII - Safeguard and validation principles

## APS-021 Safeguard reality

A control requirement and real-world safeguard shall remain distinct.

A policy cannot substitute for implemented protection.

| **Dimension**             | **Requirement**                                            |
|---------------------------|------------------------------------------------------------|
| Application               | Identify mechanism, owner, scope, states and dependencies. |
| Prohibited interpretation | Counting a control statement as an operating safeguard.    |
| Minimum evidence          | Configuration and observation evidence.                    |
| Decision effect           | Absent implementation supports intent only.                |

## APS-022 Effectiveness by condition

Safeguard effectiveness shall be concluded only for validated scope, conditions and period.

Effectiveness is contextual.

| **Dimension**             | **Requirement**                                            |
|---------------------------|------------------------------------------------------------|
| Application               | Define trigger, capacity, timing, state and failure modes. |
| Prohibited interpretation | Generalising one successful test to all conditions.        |
| Minimum evidence          | Representative test and operating evidence.                |
| Decision effect           | Outside tested conditions remains unproven.                |

## APS-023 Safeguard dependency

Safeguards shall be assessed for power, sensing, control, identity, operator and supplier dependencies.

A safeguard can fail through the same cause it manages.

| **Dimension**             | **Requirement**                                 |
|---------------------------|-------------------------------------------------|
| Application               | Model dependencies and common mode.             |
| Prohibited interpretation | Assuming safeguards are independent.            |
| Minimum evidence          | Architecture, configuration and failure tests.  |
| Decision effect           | Shared dependency may invalidate barrier claim. |

## APS-024 Defence diversity

Multiple safeguards strengthen assurance only when mechanisms and dependencies are meaningfully diverse.

Layer count is not defence depth.

| **Dimension**             | **Requirement**                                    |
|---------------------------|----------------------------------------------------|
| Application               | Define diversity and correlated bypass.            |
| Prohibited interpretation | Counting duplicate policies as independent layers. |
| Minimum evidence          | Design and scenario evidence.                      |
| Decision effect           | No independence claim without evidence.            |

## APS-025 Residual-path disclosure

Material paths remaining after safeguards shall be disclosed.

Remediation existence does not prove closure.

| **Dimension**             | **Requirement**                                     |
|---------------------------|-----------------------------------------------------|
| Application               | Reanalyse alternate and residual paths.             |
| Prohibited interpretation | Reporting only planned control.                     |
| Minimum evidence          | Post-control analysis and retest.                   |
| Decision effect           | Residual exposure informs conditions and follow-up. |

# Part VIII - Evidence and confidence principles

## APS-026 Evidence before conclusion

Every material conclusion shall be supported by evidence appropriate to claim type.

Evidence is the basis, not an appendix.

| **Dimension**             | **Requirement**                                                                  |
|---------------------------|----------------------------------------------------------------------------------|
| Application               | Match design, implementation and effectiveness claims to corresponding evidence. |
| Prohibited interpretation | Policy alone for operating effectiveness.                                        |
| Minimum evidence          | Assertion-specific evidence bundle.                                              |
| Decision effect           | Unsupported claim remains UNKNOWN or intent.                                     |

## APS-027 Evidence provenance

Evidence shall retain source, collection, time, scope, integrity and transformation.

Without provenance evidence cannot be reviewed.

| **Dimension**             | **Requirement**                         |
|---------------------------|-----------------------------------------|
| Application               | Use stable IDs and custody records.     |
| Prohibited interpretation | Detached screenshots without context.   |
| Minimum evidence          | Evidence manifest and provenance chain. |
| Decision effect           | Material provenance gap limits use.     |

## APS-028 Evidence sufficiency

Sufficiency depends on relevance, reliability, currency, coverage, corroboration and representativeness.

Quantity alone does not create assurance.

| **Dimension**             | **Requirement**                                     |
|---------------------------|-----------------------------------------------------|
| Application               | Review each assertion and common-source dependence. |
| Prohibited interpretation | Averaging evidence grades.                          |
| Minimum evidence          | Sufficiency rationale.                              |
| Decision effect           | Insufficient evidence caps the claim.               |

## APS-029 Evidence currency

Evidence remains valid only while representative of the assessed state.

Time and change can invalidate evidence.

| **Dimension**             | **Requirement**                                     |
|---------------------------|-----------------------------------------------------|
| Application               | Define expiry and change triggers.                  |
| Prohibited interpretation | Universal fixed validity without change review.     |
| Minimum evidence          | Timestamp, configuration and change records.        |
| Decision effect           | Stale evidence triggers limitation or reassessment. |

## APS-030 Assertion-specific confidence

Confidence shall attach to a precise assertion, not a whole report.

Claims in one document may have unequal support.

| **Dimension**             | **Requirement**                                          |
|---------------------------|----------------------------------------------------------|
| Application               | State rationale and unresolved conditions per assertion. |
| Prohibited interpretation | One overall confidence label hiding weak claims.         |
| Minimum evidence          | Assertion register and review.                           |
| Decision effect           | Confidence shapes wording, never replaces evidence.      |

## APS-031 Conflict retention

Conflicting evidence shall remain visible until resolved or bounded.

Deleting conflict creates false certainty.

| **Dimension**             | **Requirement**                              |
|---------------------------|----------------------------------------------|
| Application               | Record each source and resolution rationale. |
| Prohibited interpretation | Selecting favourable evidence silently.      |
| Minimum evidence          | Conflict and supersession record.            |
| Decision effect           | Unresolved conflict limits assurance.        |

# Part IX - UNKNOWN and limitation principles

## APS-032 UNKNOWN preservation

UNKNOWN shall remain a first-class state.

Transparency is safer than fabricated completeness.

| **Dimension**             | **Requirement**                                                 |
|---------------------------|-----------------------------------------------------------------|
| Application               | Record what is unknown, materiality, owner and resolution path. |
| Prohibited interpretation | Encoding UNKNOWN as zero, pass, fail or N/A.                    |
| Minimum evidence          | Unknown register.                                               |
| Decision effect           | Critical UNKNOWN may cap or block assurance.                    |

## APS-033 No assumed favourable state

Absence of adverse evidence shall not prove effectiveness or resilience.

Not finding is not proving.

| **Dimension**             | **Requirement**                                             |
|---------------------------|-------------------------------------------------------------|
| Application               | Distinguish not assessed, not tested, inconclusive and N/A. |
| Prohibited interpretation | Assumed pass where evidence is unavailable.                 |
| Minimum evidence          | Coverage and state records.                                 |
| Decision effect           | No positive claim without affirmative support.              |

## APS-034 Limitation transparency

Material exclusions, sampling, stale evidence and access constraints shall be prominent.

Decision makers need to know what is not covered.

| **Dimension**             | **Requirement**                                      |
|---------------------------|------------------------------------------------------|
| Application               | State limitations beside conclusions and in exports. |
| Prohibited interpretation | Burying critical limits in appendices.               |
| Minimum evidence          | Limitation register.                                 |
| Decision effect           | Limitations shape wording and validity.              |

## APS-035 Not-applicable discipline

N/A requires approved rationale that no relevant subject or outcome exists.

N/A must not remove hard or untested requirements.

| **Dimension**             | **Requirement**                            |
|---------------------------|--------------------------------------------|
| Application               | Name criterion, rationale and approver.    |
| Prohibited interpretation | Using N/A because evidence is unavailable. |
| Minimum evidence          | Applicability decision.                    |
| Decision effect           | Improper N/A becomes UNKNOWN or gap.       |

# Part X - Critical-gate principles

## APS-036 Critical-gate protection

Critical prerequisites shall be evaluated separately from scores and maturity.

Some conditions are indispensable.

| **Dimension**             | **Requirement**                                                        |
|---------------------------|------------------------------------------------------------------------|
| Application               | Define gate, failure/unknown criteria, evidence floor and consequence. |
| Prohibited interpretation | Averaging a failed gate into a good score.                             |
| Minimum evidence          | Gate record and evidence.                                              |
| Decision effect           | Failed or critical-UNKNOWN gate limits or blocks assurance.            |

## APS-037 Non-compensation

Strong performance in one area shall not compensate for a failed prerequisite or catastrophic scenario.

Substitution hides fragility.

| **Dimension**             | **Requirement**                                                                        |
|---------------------------|----------------------------------------------------------------------------------------|
| Application               | Use non-compensating logic for safety, continuity, containment, recovery and evidence. |
| Prohibited interpretation | Points trading across unrelated domains.                                               |
| Minimum evidence          | Gate and outcome analysis.                                                             |
| Decision effect           | Decision follows the most restrictive applicable condition.                            |

## APS-038 Gate proportionality

Critical gates shall be capability-specific, not a universal static list.

Different profiles have different indispensable conditions.

| **Dimension**             | **Requirement**                                           |
|---------------------------|-----------------------------------------------------------|
| Application               | Derive gates from outcomes, dependencies and scenarios.   |
| Prohibited interpretation | Declaring every control a gate.                           |
| Minimum evidence          | Capability profile and rationale.                         |
| Decision effect           | Improper gate design invalidates score/certification use. |

## APS-039 Gate closure

A critical gate closes only with corrective evidence and required independent review.

Planned action is not closure.

| **Dimension**             | **Requirement**                      |
|---------------------------|--------------------------------------|
| Application               | Retest condition and residual paths. |
| Prohibited interpretation | Closure by management promise.       |
| Minimum evidence          | Remediation and retest evidence.     |
| Decision effect           | Open gate remains visible in claims. |

# Part XI - Cross-domain and graph-native principles

## APS-040 System-of-systems assurance

AIDCF shall reason across all material domains as one capability-supporting system.

Local conformance does not prove end-to-end outcome.

| **Dimension**             | **Requirement**                                  |
|---------------------------|--------------------------------------------------|
| Application               | Use integrated dependency and scenario views.    |
| Prohibited interpretation | End-to-end decision from siloed checklists only. |
| Minimum evidence          | Cross-domain graph and scenarios.                |
| Decision effect           | Missing interaction limits system assurance.     |

## APS-041 Graph-native traceability

Material entities, relations, assertions, paths and decisions should be versioned graph objects.

Graph form makes lineage and propagation explicit.

| **Dimension**             | **Requirement**                                      |
|---------------------------|------------------------------------------------------|
| Application               | Use canonical IDs, evidence and snapshots.           |
| Prohibited interpretation | Treating graph connection as causality or authority. |
| Minimum evidence          | Conformant exchange records.                         |
| Decision effect           | Graph supports reasoning but proves nothing alone.   |

## APS-042 Federated assurance

AIDCF and AI Trust Graph conclusions shall remain native while contributing to an integrated decision package.

Integration must not collapse semantics.

| **Dimension**             | **Requirement**                                         |
|---------------------------|---------------------------------------------------------|
| Application               | Use approved bridge assertions and native snapshots.    |
| Prohibited interpretation | Merging distinct findings into one unsupported verdict. |
| Minimum evidence          | Artifact 005 package.                                   |
| Decision effect           | Integrated decision states separate limitations.        |

## APS-043 Human approval of inference

Automation may propose content; material facts and decisions require accountable review.

Model confidence cannot confer authority.

| **Dimension**             | **Requirement**                                      |
|---------------------------|------------------------------------------------------|
| Application               | Store candidate state, source and reviewer outcome.  |
| Prohibited interpretation | Automatic conversion of inference to fact.           |
| Minimum evidence          | Inference and review log.                            |
| Decision effect           | Unreviewed inference cannot support final assurance. |

# Part XII - Decision, scoring, maturity and reporting principles

## APS-044 Bounded decision

Every decision shall state subject, question, scope, criteria, evidence, states, period, limitations and owner.

Bounds prevent misleading transfer.

| **Dimension**             | **Requirement**                                      |
|---------------------------|------------------------------------------------------|
| Application               | Use canonical decision record.                       |
| Prohibited interpretation | Unqualified statements such as fully assured.        |
| Minimum evidence          | Complete decision package.                           |
| Decision effect           | Missing bounds make decision provisional or invalid. |

## APS-045 Scoring restraint

Scores may aid prioritisation but shall not create facts, hide uncertainty or override gates.

Numbers can overstate support.

| **Dimension**             | **Requirement**                                    |
|---------------------------|----------------------------------------------------|
| Application               | Publish formula, inputs, coverage and sensitivity. |
| Prohibited interpretation | Opaque overall score.                              |
| Minimum evidence          | Transparent scoring and gate record.               |
| Decision effect           | Evidence and gates govern wording.                 |

## APS-046 Maturity separation

Maturity shall remain distinct from effectiveness, evidence, risk and assurance.

Mature process can still fail a specific outcome.

| **Dimension**             | **Requirement**                             |
|---------------------------|---------------------------------------------|
| Application               | Use cumulative criteria and separate gates. |
| Prohibited interpretation | Inferring resilience from maturity.         |
| Minimum evidence          | Maturity evidence and rule-based decision.  |
| Decision effect           | Maturity contextualises, not overrides.     |

## APS-047 Reporting integrity

Reports shall give findings, limits, UNKNOWN, conflict, coverage and gate status appropriate prominence.

Selective presentation harms decisions.

| **Dimension**             | **Requirement**                               |
|---------------------------|-----------------------------------------------|
| Application               | Provide executive and technical traceability. |
| Prohibited interpretation | Green dashboards hiding critical limits.      |
| Minimum evidence          | Release and traceability review.              |
| Decision effect           | Misleading presentation is nonconformance.    |

## APS-048 No inherited assurance

External certification or vendor validation may be evidence but shall not automatically transfer.

Scope, conditions and time differ.

| **Dimension**             | **Requirement**                                |
|---------------------------|------------------------------------------------|
| Application               | Assess relevance, currency and coverage.       |
| Prohibited interpretation | Automatic pass by certification inheritance.   |
| Minimum evidence          | Third-party report and applicability analysis. |
| Decision effect           | Unsupported inheritance remains a limitation.  |

# Part XIII - Independence, competence and ethics

## APS-049 Impartiality

Conclusions shall be protected from commercial, managerial, political and vendor pressure.

Credibility depends on objective interpretation.

| **Dimension**             | **Requirement**                                                                |
|---------------------------|--------------------------------------------------------------------------------|
| Application               | Declare conflicts and separate evaluation, review and decision where required. |
| Prohibited interpretation | Outcome-contingent conclusion.                                                 |
| Minimum evidence          | Conflict register and independent review.                                      |
| Decision effect           | Unmanageable conflict blocks decision.                                         |

## APS-050 Competence

Assessment shall use collectively competent engineering, AI infrastructure, operations, security and assurance professionals.

No single discipline covers AIDCF.

| **Dimension**             | **Requirement**                                                |
|---------------------------|----------------------------------------------------------------|
| Application               | Define competence by scope and use specialists.                |
| Prohibited interpretation | General audit competence for licensed engineering conclusions. |
| Minimum evidence          | Competence matrix and assignments.                             |
| Decision effect           | Gap limits scope or requires specialist review.                |

## APS-051 Professional scepticism

Assessors shall test whether evidence supports claims and consider alternatives.

Assurance is challenge, not confirmation.

| **Dimension**             | **Requirement**                                            |
|---------------------------|------------------------------------------------------------|
| Application               | Seek corroboration, exceptions and failed cases.           |
| Prohibited interpretation | Assuming title equals evidence.                            |
| Minimum evidence          | Review notes and samples.                                  |
| Decision effect           | Unchallenged material claim cannot support high assurance. |

## APS-052 Confidentiality and minimisation

Collection and reporting shall be authorised, necessary, proportionate and protected.

Assurance does not justify overcollection.

| **Dimension**             | **Requirement**                                              |
|---------------------------|--------------------------------------------------------------|
| Application               | Apply classification, access, retention and lawful handling. |
| Prohibited interpretation | Publishing live sensitive paths.                             |
| Minimum evidence          | Authorisation and evidence inventory.                        |
| Decision effect           | Improper material is escalated and may be excluded.          |

## APS-053 Accountability

Owners retain operational responsibility; assessors retain method and conclusion responsibility.

Assurance informs but does not transfer accountability.

| **Dimension**             | **Requirement**                                    |
|---------------------------|----------------------------------------------------|
| Application               | Name owner, assessor, reviewer and decision owner. |
| Prohibited interpretation | Using assessor opinion to avoid owner decision.    |
| Minimum evidence          | Signed role and decision record.                   |
| Decision effect           | Unclear authority prevents final disposition.      |

## APS-054 Appeal and challenge

Material findings and decisions shall permit controlled challenge.

Fair challenge improves quality.

| **Dimension**             | **Requirement**                                              |
|---------------------------|--------------------------------------------------------------|
| Application               | Record grounds, evidence, reviewer independence and outcome. |
| Prohibited interpretation | Informal deletion of disputed findings.                      |
| Minimum evidence          | Appeal record.                                               |
| Decision effect           | Decision status remains explicit until resolved.             |

# Part XIV - Lifecycle and continuing assurance

## APS-055 Temporal validity

Assurance remains valid only for declared snapshot, period and conditions.

Systems, evidence and dependencies change.

| **Dimension**             | **Requirement**                                          |
|---------------------------|----------------------------------------------------------|
| Application               | State effective and expiry conditions; preserve history. |
| Prohibited interpretation | Perpetual validity claim.                                |
| Minimum evidence          | Snapshot and validity metadata.                          |
| Decision effect           | Expired conclusion cannot be current.                    |

## APS-056 Material-change reassessment

Changes affecting outcomes, dependencies, capacity, state, safeguards or evidence shall trigger impact review.

Prior decisions cannot survive unexamined change.

| **Dimension**             | **Requirement**                                               |
|---------------------------|---------------------------------------------------------------|
| Application               | Define triggers and affected assertions.                      |
| Prohibited interpretation | Updating report date without reassessment.                    |
| Minimum evidence          | Change and impact record.                                     |
| Decision effect           | Affected conclusions become limited, suspended or superseded. |

## APS-057 Incident learning

Incidents, tests and near misses shall feed back into scenarios, controls and methods.

Observed outcomes test assumptions.

| **Dimension**             | **Requirement**                                |
|---------------------------|------------------------------------------------|
| Application               | Compare event to model and update records.     |
| Prohibited interpretation | Closing incident without methodology feedback. |
| Minimum evidence          | Incident and change record.                    |
| Decision effect           | Recurring weakness may trigger broader review. |

## APS-058 Continuing-assurance restraint

Continuous assurance may be claimed only for monitored scope, signals, freshness and decision logic actually implemented.

Telemetry does not create universal assurance.

| **Dimension**             | **Requirement**                                                 |
|---------------------------|-----------------------------------------------------------------|
| Application               | State monitored objects, blind spots, cadence and human review. |
| Prohibited interpretation | Calling periodic collection continuous assurance.               |
| Minimum evidence          | Monitoring design and operation.                                |
| Decision effect           | Unmonitored conditions remain point-in-time or UNKNOWN.         |

# Part XV - Claim language and assurance decision model

## 8. Decision statuses

| **Status**         | **Meaning**                                                         |
|--------------------|---------------------------------------------------------------------|
| NOT ASSESSED       | No relevant activity; no conclusion.                                |
| UNKNOWN            | Evidence absent, insufficient or conflicting.                       |
| INCONCLUSIVE       | Activity occurred but cannot support determination.                 |
| ADVERSE            | Evidence demonstrates material unmet condition.                     |
| LIMITED            | Some claims supported, with material limitations.                   |
| CONDITIONAL        | Conclusion depends on named continuing conditions.                  |
| REASONABLY ASSURED | Sufficient appropriate evidence supports bounded claim and gates.   |
| SUSPENDED          | Material change, gate failure or evidence expiry prevents reliance. |
| WITHDRAWN          | Decision authority removed the conclusion.                          |
| SUPERSEDED         | Newer decision replaces prior current state.                        |

## 9. Assurance decision record

| **Field**                 | **Required content**                            |
|---------------------------|-------------------------------------------------|
| decisionId                | Stable, versioned identifier.                   |
| decisionQuestion          | Exact decision supported.                       |
| subject/outcomes          | Capability Instance and Service Outcomes.       |
| scope/boundary            | Inclusions, exclusions, states and period.      |
| criteria/methods          | Artifacts, profiles, tests and samples.         |
| evidence/coverage         | Manifest, sufficiency and coverage.             |
| unknowns/conflicts        | Material unresolved items.                      |
| criticalGates             | Applicable gate statuses.                       |
| findings/residualExposure | Material results and remaining paths.           |
| status/limitations        | Controlled status, conditions and restrictions. |
| validity/triggers         | Expiry and reassessment.                        |
| roles                     | Assessor, reviewer and decision owner.          |
| snapshot                  | Machine-readable reference where applicable.    |

## 10. Claim language

| **Avoid**                   | **Use instead**                                                                                              |
|-----------------------------|--------------------------------------------------------------------------------------------------------------|
| Fully compliant             | Assessed against named criteria within stated scope; compliance not determined unless separately authorised. |
| Zero risk                   | No material adverse condition identified within tested scope; residual and UNKNOWN remain.                   |
| Fail-proof                  | Validated for specified scenario and conditions.                                                             |
| Certified by AIDCF          | Assessed against named AIDCF artifact/profile, unless an approved scheme applies.                            |
| Continuously assured        | Monitored for named signals, scope, cadence and review process.                                              |
| All dependencies identified | No additional material dependency identified within documented discovery coverage.                           |
| Control effective           | Evidence supports effectiveness for tested scope, period and conditions.                                     |
| Redundant                   | Alternative exists; independence and common-mode status stated separately.                                   |

## 11. Assurance ceilings

| **Constraint**                            | **Ceiling**                       |
|-------------------------------------------|-----------------------------------|
| No Capability Instance/Outcome            | No capability assurance.          |
| No current boundary/architecture          | Descriptive or provisional only.  |
| E0-E1 for material claim                  | UNKNOWN/candidate only.           |
| Document-only evidence                    | Design intent at most.            |
| No representative operating/test evidence | No operating-effectiveness claim. |
| Critical UNKNOWN                          | Limited, conditional or blocked.  |
| Failed critical gate                      | Adverse, limited or blocked.      |
| Unassessed degraded/recovery state        | No resilience claim for state.    |
| Material change/stale evidence            | Suspend or reassess.              |

# Part XVI - Conformance and enforcement

## 12. Conformance levels

| **Level** | **Name**              | **Expectation**                                                        |
|-----------|-----------------------|------------------------------------------------------------------------|
| P0        | Aware                 | Uses vocabulary without formal claim.                                  |
| P1        | Declared              | Identifies applicable principles and deviations.                       |
| P2        | Assessment conformant | Applies evidence, UNKNOWN, gate, independence and decision rules.      |
| P3        | Artifact conformant   | Maps downstream requirements to APS principles.                        |
| P4        | Tool conformant       | Preserves semantics, validation, audit and human approval.             |
| P5        | Scheme conformant     | Demonstrates impartiality, review, surveillance and controlled claims. |

## 13. Nonconformance

| **Class**   | **Examples**                                                                                        | **Response**                                                      |
|-------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Critical    | Fabricated evidence, hidden gate failure, unsafe test, suppressed conflict, misleading certificate. | Stop claim, preserve evidence, escalate and independently review. |
| Major       | Unsupported effectiveness, UNKNOWN converted to pass, boundary omission, unmanaged conflict.        | Withdraw/limit and remediate before release.                      |
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

| **Relationship**         | **Meaning**                                      |
|--------------------------|--------------------------------------------------|
| GOVERNS                  | Principle constrains artifact, claim or process. |
| REQUIRES                 | Principle mandates obligation.                   |
| PROHIBITS                | Principle disallows practice.                    |
| SUPPORTED_BY             | Claim/decision linked to evidence.               |
| LIMITED_BY               | Claim constrained by limitation/UNKNOWN.         |
| BLOCKED_BY               | Gate prevents conclusion.                        |
| REVIEWED_BY              | Accountable review.                              |
| SUPERSEDES               | New version replaces without erasing history.    |
| TRIGGERS_REASSESSMENT_OF | Change affects prior decision.                   |
| CONFORMS_TO              | Artifact/tool declares tested conformance.       |

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
| APS-VAL-001 | Every downstream requirement maps to at least one principle.       |
| APS-VAL-002 | Every final decision identifies capability and outcomes.           |
| APS-VAL-003 | Every decision has scope, state, period, evidence and limitations. |
| APS-VAL-004 | Every material assertion has evidence or explicit UNKNOWN.         |
| APS-VAL-005 | Every applicable gate has status and evidence.                     |
| APS-VAL-006 | No score or maturity overrides a gate.                             |
| APS-VAL-007 | No UNKNOWN becomes favourable numeric/boolean state.               |
| APS-VAL-008 | Every effectiveness claim identifies tested conditions.            |
| APS-VAL-009 | Every material change links affected decisions.                    |
| APS-VAL-010 | Every AI-generated item remains candidate until reviewed.          |
| APS-VAL-011 | Every exception is time-bound and preserves intent.                |
| APS-VAL-012 | Every nonconformance has disposition.                              |
| APS-VAL-013 | Every integrated package preserves native decisions.               |
| APS-VAL-014 | Every published claim uses controlled status.                      |
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
| Gates        | Thermal, power, checkpoint, recovery and observability gates.                          |
| Decision     | Bounded readiness with UNKNOWN, residual paths and triggers.                           |

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
| APAT-15 | Certification claim without approved scheme.                            |

# Appendix A - Principle registry

| **ID**  | **Principle**                    |
|---------|----------------------------------|
| APS-001 | Capability-first assurance       |
| APS-002 | Outcome alignment                |
| APS-003 | Function before product          |
| APS-004 | Outcome-centric materiality      |
| APS-005 | Explicit boundary                |
| APS-006 | Operating-envelope discipline    |
| APS-007 | State-specific assurance         |
| APS-008 | Reality over intent              |
| APS-009 | Proportionate depth              |
| APS-010 | Dependency visibility            |
| APS-011 | External dependency continuity   |
| APS-012 | Shared-dependency scrutiny       |
| APS-013 | Concentration awareness          |
| APS-014 | Dependency ownership             |
| APS-015 | Failure-chain analysis           |
| APS-016 | Cross-domain propagation         |
| APS-017 | Compound conditions              |
| APS-018 | Resilience lifecycle             |
| APS-019 | Recovery evidence                |
| APS-020 | Safe validation                  |
| APS-021 | Safeguard reality                |
| APS-022 | Effectiveness by condition       |
| APS-023 | Safeguard dependency             |
| APS-024 | Defence diversity                |
| APS-025 | Residual-path disclosure         |
| APS-026 | Evidence before conclusion       |
| APS-027 | Evidence provenance              |
| APS-028 | Evidence sufficiency             |
| APS-029 | Evidence currency                |
| APS-030 | Assertion-specific confidence    |
| APS-031 | Conflict retention               |
| APS-032 | UNKNOWN preservation             |
| APS-033 | No assumed favourable state      |
| APS-034 | Limitation transparency          |
| APS-035 | Not-applicable discipline        |
| APS-036 | Critical-gate protection         |
| APS-037 | Non-compensation                 |
| APS-038 | Gate proportionality             |
| APS-039 | Gate closure                     |
| APS-040 | System-of-systems assurance      |
| APS-041 | Graph-native traceability        |
| APS-042 | Federated assurance              |
| APS-043 | Human approval of inference      |
| APS-044 | Bounded decision                 |
| APS-045 | Scoring restraint                |
| APS-046 | Maturity separation              |
| APS-047 | Reporting integrity              |
| APS-048 | No inherited assurance           |
| APS-049 | Impartiality                     |
| APS-050 | Competence                       |
| APS-051 | Professional scepticism          |
| APS-052 | Confidentiality and minimisation |
| APS-053 | Accountability                   |
| APS-054 | Appeal and challenge             |
| APS-055 | Temporal validity                |
| APS-056 | Material-change reassessment     |
| APS-057 | Incident learning                |
| APS-058 | Continuing-assurance restraint   |

# Appendix B - Baseline critical-gate catalogue

This is a candidate baseline. Profiles determine applicability, detailed criterion and evidence floor. It is not a universal pass/fail list.

| **ID** | **Gate**                                          |
|--------|---------------------------------------------------|
| CG-01  | Capability and outcome definition                 |
| CG-02  | Boundary and architecture integrity               |
| CG-03  | Critical dependency visibility                    |
| CG-04  | Life safety and hazardous energy                  |
| CG-05  | Resilient electrical supply                       |
| CG-06  | Thermal continuity                                |
| CG-07  | Critical control-system integrity                 |
| CG-08  | Compute, storage and network functional integrity |
| CG-09  | Failure containment                               |
| CG-10  | Recovery readiness                                |
| CG-11  | Evidence sufficiency                              |
| CG-12  | Critical UNKNOWN                                  |
| CG-13  | Responsibility and authority                      |
| CG-14  | Change control                                    |
| CG-15  | Integrated digital authority over infrastructure  |

## Gate record schema

| **Field**                 | **Requirement**                        |
|---------------------------|----------------------------------------|
| gateId                    | Stable ID and profile/version.         |
| subject/outcome           | Capability and Outcome protected.      |
| criterion                 | Testable prerequisite.                 |
| applicability             | Why it applies.                        |
| failure/unknown condition | When gate fails or remains UNKNOWN.    |
| evidence floor            | Minimum support.                       |
| methods                   | Analysis, inspection, test and review. |
| status                    | Pass, Fail, UNKNOWN or approved N/A.   |
| decision effect           | Block, cap, condition or escalate.     |
| owner/reviewer            | Accountable roles.                     |
| closure                   | Remediation and retest.                |

# Appendix C - UNKNOWN and limitation schemas

| **UNKNOWN field**     | **Content**                                             |
|-----------------------|---------------------------------------------------------|
| unknownId             | Stable ID.                                              |
| subject/attribute     | What is unresolved.                                     |
| reason                | Absent, inaccessible, stale, conflicting or not tested. |
| potential consequence | Why it matters.                                         |
| criticality           | Criticality and rationale.                              |
| evidence needed       | Resolution requirement.                                 |
| owner                 | Owner if known.                                         |
| decision effect       | Limit, condition, block or suspend.                     |
| status/history        | Open, resolved, accepted or superseded.                 |

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
| AIDCF ontology reviewer              | Pending         | Artifact 003 consistency.          |
| Failure/resilience reviewer          | Pending         | Artifact 004 consistency.          |
| AI Trust Graph integration reviewer  | Pending         | Artifact 005 consistency.          |
| Electrical engineer                  | Pending         | Power gate validity.               |
| Mechanical/cooling engineer          | Pending         | Thermal gate validity.             |
| Compute/storage/network reviewer     | Pending         | AI infrastructure outcomes.        |
| Operations/OT reviewer               | Pending         | State, automation and authority.   |
| Assurance reviewer                   | Pending         | Evidence, independence and claims. |
| Certification/accreditation reviewer | Pending         | Scheme implications.               |
| Security/privacy reviewer            | Pending         | Evidence/path protection.          |
| Legal/IP/publication reviewer        | Pending         | Rights and claims.                 |
| Independent practitioner             | Pending         | Reproducibility.                   |
| Public release                       | Not approved    | All gates closed.                  |

## Acceptance criteria

- Downstream artifacts can map to this standard without contradiction.

- Evidence, UNKNOWN, gates, independence and bounded decisions are enforceable.

- No principle implies legal compliance or engineering approval by itself.

- Machine-readable implementation does not change meaning.

- Independent multidisciplinary and publication review is completed.

## Change record

| **Version** | **Status**              | **Summary**                                      |
|-------------|-------------------------|--------------------------------------------------|
| 0.1         | Architecture draft      | Constitutional role and principle families.      |
| 0.5         | Integrated draft        | Decision, gate, ethics and conformance models.   |
| 1.0         | Controlled-review draft | Comprehensive baseline for downstream artifacts. |

## Final constitutional doctrine

AIDCF may express confidence only where the decision question is clear, the capability and outcomes are defined, dependencies and failure paths are sufficiently understood, safeguards are evidenced within relevant conditions, uncertainty remains visible, critical gates are satisfied, competent and impartial review has occurred, and the conclusion is bounded by scope, state, time and evidence. Where these conditions are not met, AIDCF shall reduce, condition, suspend or withhold assurance rather than manufacture certainty.
