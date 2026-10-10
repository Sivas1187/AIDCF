> Markdown edition. Source: [AIDCF_Technical_Whitepaper_v3.0_Validation_Candidate.docx](AIDCF_Technical_Whitepaper_v3.0_Validation_Candidate.docx) · PDF: [AIDCF_Technical_Whitepaper_v3.0_Validation_Candidate.pdf](AIDCF_Technical_Whitepaper_v3.0_Validation_Candidate.pdf)

**AIDCF**

**AI Data Centre Facilities Assurance Framework**

*Capability-centred, evidence-gated and graph-native assurance for AI infrastructure*

![Figure 1. AIDCF canonical assurance argument](media/figure-1-assurance-argument.png)

*Figure 1. AIDCF canonical assurance argument.*

| **Field**             | **Value**                                                                                                       |
|-----------------------|-----------------------------------------------------------------------------------------------------------------|
| Artifact              | AIDCF-WP-001                                                                                                    |
| Version               | 3.0                                                                                                             |
| Status                | Validation Candidate for Independent Review                                                                     |
| Author                | Siva Sethumadhavan                                                                                              |
| Canonical baseline    | AIDCF-007A: 15 domains, 90 families and 360 controls                                                            |
| Implementation status | Synthetic, non-production reference implementation                                                              |
| Publication boundary  | Research framework; not law, certification, accreditation, engineering approval or hazardous-test authorisation |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>How to cite<br />
</strong>Sethumadhavan, S. AIDCF: AI Data Centre Facilities Assurance Framework. Technical Whitepaper v2.0, Public Review Draft, 2026. DOI to be assigned on public deposit.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Abstract

Artificial intelligence workloads create a capability system that couples dense electrical demand, heat rejection, liquid and air cooling, accelerated compute, checkpoint storage, high-bandwidth fabrics, orchestration, control planes, operational teams and external providers. Established facility, technology, cybersecurity and AI-governance approaches address important parts of this landscape, but do not necessarily provide one end-to-end argument from a specific AI service outcome to infrastructure reality, credible failure, implemented safeguards, evidence and decision. AIDCF addresses this perceived integration gap.

The framework defines a Capability Instance as the bounded subject of assurance and traces required Service Outcomes through functions, systems, assets, interfaces, dependencies, fault domains, operating states, failure paths, safeguards, controls, evidence, assessments, critical gates and accountable decisions. Its approved baseline contains fifteen domains, ninety control families and 360 controls. The method preserves UNKNOWN, separates intended, designed, installed, commissioned, observed and tested states, and prevents unrelated strengths or aggregate scores from overriding a controlling gate.

Version 3.0 consolidates the AIDCF artifact stack into a coherent research narrative. It documents the development protocol, related-work boundaries, assurance theory, domain derivation, system-of-systems architecture, control and evidence models, assessment and gate logic, a machine-executable publication model and a complete synthetic worked case. It also separates approved baseline content from controlled-review drafts, synthetic demonstrations and proposed extensions. AIDCF remains a proposed research framework requiring independent review, real-world pilots, calibration and multi-site validation.

# Executive summary

| **Problem pattern**                               | **AIDCF response**                                                                                          | **Decision value**                                          |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Facility and AI-platform reviews are disconnected | One capability chain links outcomes to power, thermal, compute, storage, network, operations and providers. | Exposes cross-domain dependencies and failure propagation.  |
| Design intent is confused with operating reality  | States are explicitly separated and evidence is assertion-specific.                                         | Restricts reliance to what was actually observed or tested. |
| Redundancy masks common mode                      | Dependencies, routes, controls, people and recovery resources are first-class.                              | Challenges superficial diversity claims.                    |
| Missing evidence is forced into a score           | UNKNOWN is visible and non-favourable.                                                                      | Prevents false certainty.                                   |
| Aggregate scores overwhelm critical failure       | Critical gates are non-compensating.                                                                        | Protects decision prerequisites.                            |
| Automation silently exercises authority           | Tools validate and recommend; accountable people decide.                                                    | Preserves governance and professional responsibility.       |

The paper does not claim that no adjacent method exists. It claims that the compared approaches leave a practical integration problem when a decision requires simultaneous reasoning across facility engineering, AI technology, operations, evidence and accountable assurance. This claim is a research proposition to be tested, not a settled conclusion.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Publication posture<br />
</strong>Public review draft. Suitable for expert critique, pilot recruitment and research timestamping. Not suitable for certification, accreditation, universal conformance claims or real-facility assurance.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 1. Formal research problem

The research problem is to determine whether a repeatable assurance method can reconstruct a bounded conclusion about a defined AI infrastructure capability from: service outcomes; architecture and dependencies; credible adverse conditions; effective safeguards; sufficient evidence; non-compensating prerequisites; competent review; and accountable decision authority.

| **Research question**                                     | **Proposition**                                               | **Empirical test**                                    |
|-----------------------------------------------------------|---------------------------------------------------------------|-------------------------------------------------------|
| Can assessors define the same bounded subject?            | Capability-first scoping reduces ambiguity.                   | Independent scoping and inter-rater agreement.        |
| Can facility and AI-platform layers be traced end to end? | Canonical objects and relationships enable reconstruction.    | Graph completeness and reverse-trace tests.           |
| Can hidden common modes be surfaced?                      | Dependency and fault-domain analysis improves discovery.      | Compare findings against conventional domain reviews. |
| Can score gaming be constrained?                          | UNKNOWN and gates resist favourable denominator manipulation. | Adversarial fixtures and re-performance.              |
| Can decisions remain explainable after change?            | Versioned identities and event impact support supersession.   | Change-event and affected-decision tests.             |

# 2. Claimed contribution and novelty

AIDCF does not claim novelty in power engineering, thermal engineering, systems reliability, cybersecurity, AI risk management, evidence management or assurance individually. Its claimed contribution is the disciplined integration of those elements around a bounded AI Capability Instance, with explicit graph traceability and decision constraints.

| **Contribution**               | **Distinctive element**                                                | **Current evidence status**                               |
|--------------------------------|------------------------------------------------------------------------|-----------------------------------------------------------|
| Capability-centred assurance   | Service Outcomes precede components and controls.                      | Conceptual and synthetic demonstration.                   |
| Cross-domain failure reasoning | Facility, technology, people and providers share one dependency graph. | Scenario and architecture artifacts; real pilots pending. |
| Evidence-gated conclusion      | Evidence quality and UNKNOWN are first-class objects.                  | Synthetic evidence fixtures.                              |
| Gate-dominant decision         | Critical prerequisites remain separate from scores.                    | Synthetic gate records and anti-gaming test.              |
| Machine-executable lineage     | Stable IDs, JSON Schema, JSON-LD, RDF/SHACL and manifests.             | Reference package; independent runtime review pending.    |

# 3. Framework-development protocol

The protocol below makes the construction process explicit. It is a retrospective methodological specification for future reproducible maintenance. A public source log, coding register and reviewer record remain required before the derivation can be considered independently reproducible.

| **Stage**              | **Procedure**                                                                                                 | **Required record**                           |
|------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| Corpus definition      | List included standards, methods, reference architectures and AIDCF source artifacts by edition and scope.    | Source register and inclusion rationale.      |
| Concept extraction     | Capture terms, objects, relationships, states, evidence and decision concepts.                                | Extraction matrix with source reference.      |
| Semantic normalization | Separate overloaded concepts such as hazard, cause, failure mode, effect, consequence, safeguard and control. | Terminology decision log.                     |
| Domain clustering      | Group concepts using coverage, separability and traceability tests.                                           | Cluster matrix and rejected alternatives.     |
| Control synthesis      | Express outcome-linked, assessable requirements with evidence and failure mappings.                           | Control design record and duplicate review.   |
| Assurance design       | Define assessment states, UNKNOWN, gates, scores, decisions and reporting.                                    | Rule register and test cases.                 |
| Machine formalisation  | Assign identifiers, schemas, graph shapes and conformance fixtures.                                           | Release manifest and validation results.      |
| Challenge and approval | Multidisciplinary peer review, disagreement resolution and independent challenge.                             | Reviewer register, comments and dispositions. |

# 4. Related work and comparative gap

The comparison is directional and limited to cited public scope statements. It is not a clause-by-clause equivalence analysis. ISO/IEC 22237-1 describes general principles, common aspects, facilities and infrastructure classification, and operation and management references, while excluding selection and configuration of IT and network equipment \[1\]. The Uptime Tier Standard provides an objective basis for comparing site-infrastructure topology and differentiates four classifications \[4\]. ANSI/TIA-942-C specifies data-centre and computer-room infrastructure requirements and includes telecommunications, power, cooling, architecture, fire protection, safety and physical security \[5\]. NIST AI RMF 1.0 provides a voluntary AI risk-management framework organised around Govern, Map, Measure and Manage \[2\]\[3\].

| **Approach**         | **Primary public scope**                                                             | **Integration gap AIDCF addresses**                                               | **No equivalence claim**                              |
|----------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------|
| ISO/IEC 22237        | Data-centre facility and infrastructure concepts, classes and management references. | Connection to configured AI compute, storage, fabrics and service outcomes.       | AIDCF does not claim ISO conformity.                  |
| Uptime Tier topology | Site-infrastructure functionality, capacity and expected availability by topology.   | Capability-specific workload, data, fabric, control-plane and evidence reasoning. | Tier evidence is bounded design evidence.             |
| ANSI/TIA-942-C       | Physical infrastructure requirements across multiple disciplines.                    | One assurance argument from AI outcome to operational evidence and decision.      | AIDCF does not certify TIA-942.                       |
| NIST AI RMF          | Voluntary management of AI risk and trustworthiness.                                 | Physical and infrastructure assurance below the AI system.                        | AIDCF is complementary, not a profile of NIST AI RMF. |
| AITG                 | Trust, authority and exposure reasoning.                                             | Infrastructure reality and physical failure paths.                                | Federate decisions; do not merge methods.             |

# 5. Assurance theory

AIDCF defines assurance as bounded confidence in a proposition about a specific capability, for identified users and intended use, within a declared boundary, operating states and period. Assurance is not the inventory of controls, a maturity score or a topology label.

Figure 2. Forward assurance construction and reverse reconstruction.

| **Proposition layer** | **Question**                                                      |
|-----------------------|-------------------------------------------------------------------|
| Outcome               | What must the capability achieve, within what tolerance?          |
| Architecture          | Which systems, interfaces and resources implement that result?    |
| Dependency            | What internal, shared, external or recovery-only reliance exists? |
| Failure               | How can the outcome be degraded or lost?                          |
| Safeguard             | What prevents, detects, contains, recovers or adapts?             |
| Evidence              | What supports or challenges each assertion?                       |
| Gate                  | Which prerequisite cannot be compensated?                         |
| Decision              | What reliance is permitted, for whom and for how long?            |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Conceptual expression<br />
</strong>Bounded Assurance = f(Outcome Definition, Architecture and Dependency Confidence, Safeguard Effectiveness, Evidence Confidence, Gate State, Review Quality, Decision Authority). This is a dependency expression, not a numeric multiplication formula.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 6. Canonical terminology and acronyms

| **Term**            | **Canonical meaning**                                                                                                      |
|---------------------|----------------------------------------------------------------------------------------------------------------------------|
| Capability Instance | A specific deployment bounded by owner, location, architecture, demand, criticality, service requirements and obligations. |
| Service Outcome     | A measurable availability, performance, integrity, recovery or restraint condition.                                        |
| Critical Function   | A function whose degradation materially affects a Service Outcome.                                                         |
| Dependency          | Reliance on an entity, resource, condition, provider, person or decision.                                                  |
| Fault Domain        | Objects expected to be affected by the same failure.                                                                       |
| Failure Scenario    | Initiating condition through propagation, consequence, safeguards and recovery.                                            |
| Evidence Object     | Controlled item supporting, challenging or qualifying an assertion.                                                        |
| Critical Gate       | Non-compensating prerequisite constraining an Assurance Decision.                                                          |
| Assurance Decision  | Bounded conclusion issued by accountable authority.                                                                        |
| UNKNOWN             | State where sufficient and reliable determination cannot be made.                                                          |

| **Acronym** | **Meaning**                                      |
|-------------|--------------------------------------------------|
| AIDCF       | AI Data Centre Facilities Assurance Framework    |
| AITG        | AI Trust Graph                                   |
| APS         | AIDCF Assurance Principle                        |
| MCF         | Master Control Framework identifier              |
| CDU         | Cooling Distribution Unit                        |
| SHACL       | Shapes Constraint Language                       |
| RDF         | Resource Description Framework                   |
| TEVV        | Testing, evaluation, verification and validation |

# 7. Status taxonomy and component maturity

| **Status**                  | Validation Candidate for Independent Review                         | **Use in this whitepaper**                             |
|-----------------------------|---------------------------------------------------------------------|--------------------------------------------------------|
| Approved baseline           | Constitutionally approved AIDCF identity and cardinality baseline.  | AIDCF-007A 15/90/360 only.                             |
| Controlled-review draft     | Substantive methodology awaiting multidisciplinary review.          | Most AIDCF standards and handbooks.                    |
| Synthetic demonstration     | Non-production data and execution for method testing.               | AIDCF-015 v1.2.                                        |
| Proposed research extension | Concept requiring governance and validation before operational use. | Maturity model, claim patterns and future-state ideas. |
| Externally validated        | Independent execution or empirical validation completed.            | Not yet achieved.                                      |

This taxonomy prevents the whitepaper from presenting every component as equally mature. Canonical identity can be approved while substantive control adequacy, gate calibration and real-world effectiveness remain open for review.

# 8. Why fifteen domains

The fifteen-domain structure applies three design tests. Coverage asks whether every material condition can be anchored without arbitrary omission. Separability asks whether a group has coherent ownership, competence and evidence. Traceability asks whether cross-domain effects can remain explicit rather than hidden inside broad categories.

| **Cluster**             | **Domains**   | **Rationale**                                                              |
|-------------------------|---------------|----------------------------------------------------------------------------|
| Direction and subject   | GOV, CAP      | Separate governance and decision rights from the capability being assured. |
| Dependency and place    | DEP, PHY      | Make hidden reliance and physical boundary explicit.                       |
| Facility engineering    | POW, THM, ENV | Different mechanisms, expertise, telemetry and failure modes.              |
| AI technology chain     | CMP, STO, NET | Distinct but tightly coupled compute, data and communication functions.    |
| Operation and recovery  | OPS, RES      | Separate routine control from continuity, crisis and restoration.          |
| Ecosystem and authority | SUP, SEC      | Separate supplier/lifecycle reliance from digital and OT authority.        |
| Assurance integrity     | EVA           | Independently govern evidence, assessment, gates and decision integrity.   |

This remains a design hypothesis. Completeness must be tested through expert review, real incidents, pilot assessments and analysis of unmapped requirements.

# 9. Domain model and control baseline

| **Code** | **Domain**                                            | **Primary gate mapping** |
|----------|-------------------------------------------------------|--------------------------|
| GOV      | Governance, Accountability and Assurance Direction    | CG-13, CG-14             |
| CAP      | AI Capability, Service Outcome and Demand Management  | CG-01, CG-02             |
| DEP      | Dependency, Concentration and External Reliance       | CG-03, CG-12             |
| PHY      | Physical Site, Building and Security Infrastructure   | CG-02, CG-04             |
| POW      | Electrical Power Infrastructure and Energy Continuity | CG-05                    |
| THM      | Cooling, Thermal and Fluid Infrastructure             | CG-06                    |
| ENV      | Environmental and Resource Performance                | CG-02, CG-04             |
| CMP      | AI Compute Infrastructure                             | CG-08                    |
| STO      | AI Storage and Data Infrastructure                    | CG-08, CG-10             |
| NET      | AI Network and Interconnect Architecture              | CG-08                    |
| OPS      | Building Operations and Service Management            | CG-07, CG-13, CG-14      |
| RES      | Resilience, Continuity and Recovery                   | CG-09, CG-10             |
| SUP      | Supply Chain, OEM and Ecosystem Assurance             | CG-03, CG-13             |
| SEC      | Digital, OT and Control-Plane Security                | CG-07, CG-15             |
| EVA      | Evidence, Assessment and Assurance Management         | CG-11, CG-12             |

Each domain contains six families and twenty-four controls, yielding ninety families and 360 controls. Stable identity does not imply immutable wording. Meaning-changing replacements require new identifiers and explicit supersession.

# 10. System-of-systems reference architecture

![Figure 3. Reference architecture with assurance and resilience rails](media/figure-3-reference-architecture.png)

*Figure 3. Reference architecture with assurance and resilience rails.*

The vertical service stack traces how external resources and facilities enable AI technology and AI services to achieve business outcomes. The assurance rail attaches controls, evidence, assessments, gates and decisions to every layer. The resilience rail attaches states, dependencies, fault domains, failure paths, safeguards and recovery.

| **Mandatory view**    | **Required content**                                                                                                              |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Capability            | Owner, lifecycle, outcomes, tolerances and criticality.                                                                           |
| Boundary              | Physical, logical, organisational, provider and temporal limits.                                                                  |
| Service chain         | Functions and interfaces from workload to facility resources.                                                                     |
| Dependency            | Internal, shared, external and recovery-only reliance.                                                                            |
| State and capacity    | Normal, maintenance, degraded, emergency, recovery and transition states; installed, available, resilient and committed capacity. |
| Failure and safeguard | Initiating condition, propagation, consequence, safeguards, residual path and recovery.                                           |
| Assurance attachment  | Controls, evidence, assessments, findings, gates, score and decision.                                                             |

# 11. Capability service chains

| **Capability pattern** | **Required functions**                                                                                       | **Representative adverse conditions**                                                     |
|------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Distributed training   | Scheduling, accelerator capacity, collective communication, training data, checkpointing, power and cooling. | Fabric partition, thermal throttling, checkpoint loss, scheduler failure.                 |
| Inference              | Request routing, model serving, accelerator availability, cache/data access and latency observability.       | Tail-latency excursion, overload, model-store or network degradation.                     |
| Fine-tuning            | Data preparation, workload placement, artifact management and reproducible recovery.                         | Configuration drift, dataset access loss, interrupted checkpoint cycle.                   |
| Sovereign AI           | Boundary enforcement, local operations, supply visibility, restricted administration and continuity.         | Remote authority, jurisdictional dependency, external telemetry or support concentration. |
| Shared AI platform     | Tenant isolation, fair scheduling, capacity reservation, telemetry and service management.                   | Noisy neighbour, privilege misuse and resource contention.                                |

# 12. Dependency, capacity and fault-domain analysis

| **Capacity state** | **Meaning**                                              |
|--------------------|----------------------------------------------------------|
| Installed          | Nominal capacity physically present.                     |
| Available          | Usable after condition, maintenance and derating.        |
| Resilient          | Available in a defined adverse condition.                |
| Committed          | Allocated or contractually reserved.                     |
| Headroom           | Remaining usable capacity beyond demand and commitments. |

Apparent diversity is not independence. Two paths may share utility supply, fuel, heat rejection, management network, firmware, time service, carrier, physical route, operator or OEM. A dependency assertion records consumer, provider, direction, condition, required capacity, criticality, evidence, confidence, owner and validation date.

# 13. Threat, hazard and failure model

| **Object**    | **Analytical question**                                            |
|---------------|--------------------------------------------------------------------|
| Threat source | Who or what could intentionally create an adverse event?           |
| Hazard        | What condition has potential to cause degradation or harm?         |
| Cause         | Why did the failure mode occur?                                    |
| Failure mode  | How did the required function fail?                                |
| Local effect  | What occurred at the failed object?                                |
| Propagation   | Which dependencies transmitted the effect?                         |
| Consequence   | Which Service Outcome or stakeholder interest was affected?        |
| Safeguard     | What anticipates, prevents, detects, contains, recovers or adapts? |
| Residual path | What material route remains after safeguards?                      |

AIDCF can consume FMEA/FMECA, fault-tree, event-tree, bow-tie, HAZOP-style and graph-traversal outputs. The framework does not replace competent use of those techniques or applicable engineering and safety requirements.

# 14. AI-native failure scenarios

| **Scenario**                   | **Failure path**                                                                                                              | **Primary domains**     |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| Accelerator thermal throttling | Liquid-flow degradation -\> temperature rise -\> frequency reduction -\> collective desynchronisation -\> checkpoint exposure | THM, CMP, NET, OPS, RES |
| Fabric congestion              | Oversubscription or path imbalance -\> collective latency -\> stalled or elongated job                                        | NET, CMP, DEP, OPS      |
| Checkpoint corruption          | Metadata or storage degradation -\> apparently successful but unusable recovery point                                         | STO, NET, RES, EVA      |
| Scheduler collapse             | Stale capacity or policy failure -\> placement failure despite installed accelerators                                         | CMP, CAP, OPS, SEC      |
| Inference instability          | Load spike, cache miss, fabric or thermal degradation -\> tail-latency breach                                                 | CAP, CMP, NET, STO, THM |
| Sovereign-boundary failure     | Remote support or telemetry path -\> declared authority or jurisdiction boundary breach                                       | GOV, DEP, SUP, SEC      |
| AI capacity cliff              | Committed demand plus degraded resilient capacity -\> insufficient usable headroom                                            | CAP, POW, THM, CMP, NET |

# 15. Safeguards and resilience

| **Safeguard role** | **Examples**                                                           | **Evidence focus**                             |
|--------------------|------------------------------------------------------------------------|------------------------------------------------|
| Anticipate         | Demand forecasting, trend and concentration review.                    | Model validity and review.                     |
| Prevent            | Redundancy, authority enforcement and environmental control.           | Design and implementation.                     |
| Detect             | Telemetry, alarms, anomaly detection and integrity checks.             | Coverage, source health and latency.           |
| Contain            | Fault isolation, segmentation, safe load reduction and leak isolation. | Activation and effectiveness.                  |
| Recover            | Restore configuration, capacity, data and service.                     | Sequencing, elapsed time and proof of outcome. |
| Adapt              | Architecture, procedure and operating-envelope change.                 | Approved change and supersession.              |

A standby mechanism is not an effective safeguard if it depends on the failed controller, lacks capacity, cannot activate in time or creates an unsafe restoration path.

# 16. Evidence model

| **Dimension** | **Assessment question**                                            |
|---------------|--------------------------------------------------------------------|
| Provenance    | Can source and lineage be identified?                              |
| Freshness     | Does evidence represent the relevant state and period?             |
| Coverage      | Does it cover the required population, path, state and time?       |
| Reliability   | Was it produced by a controlled and repeatable method?             |
| Traceability  | Can it be linked to assertion, finding, gate and decision?         |
| Integrity     | Is inappropriate alteration detectable and custody controlled?     |
| Sufficiency   | Is the evidence set adequate for the decision and assurance depth? |

Evidence is assertion-specific. A signed design supports intent but not necessarily implementation. Telemetry can support current operation but not historical commissioning. A test can support one state or scenario without proving all conditions. AI-assisted extraction or summarisation creates candidate evidence only; it does not independently corroborate its source.

# 17. Assessment methodology

| **Stage** | **Key output**                                                     |
|-----------|--------------------------------------------------------------------|
| Initiate  | Decision question, sponsor, users and charter.                     |
| Profile   | Capability, Service Outcomes, architecture and operating envelope. |
| Scope     | Boundary, dependencies, states, criteria and exclusions.           |
| Tailor    | Applicable controls, gates, evidence and assurance depth.          |
| Plan      | Methods, sampling, tests, safety and review.                       |
| Collect   | Controlled Evidence Objects and restrictions.                      |
| Validate  | Provenance, integrity, freshness, coverage and sufficiency.        |
| Assess    | Control, safeguard, scenario and domain results.                   |
| Analyse   | Propagation, common mode, concentration and residual paths.        |
| Gate      | Applicable CG-01 through CG-15.                                    |
| Find      | Findings, UNKNOWN, limitations and recommendations.                |
| Review    | Technical and independent challenge.                               |
| Decide    | Bounded Assurance Decision.                                        |
| Report    | Executive, technical and machine-readable packages.                |
| Reassess  | Change, incident, expiry and supersession.                         |

# 18. Critical gates and governance

Gate identity and domain mappings are canonical in the registry. The explanatory names and decision effects below are public-review profiles, not replacements for the controlled gate registry. They must be approved through AIDCF governance before being called canonical gate definitions.

| **Gate** | **Proposed explanatory profile**          |
|----------|-------------------------------------------|
| CG-01    | Capability definition                     |
| CG-02    | Boundary and operating envelope           |
| CG-03    | Dependency and provider confidence        |
| CG-04    | Physical and environmental suitability    |
| CG-05    | Electrical continuity                     |
| CG-06    | Thermal and fluid continuity              |
| CG-07    | Operational and control authority         |
| CG-08    | AI technology service-chain integrity     |
| CG-09    | Containment and resilience                |
| CG-10    | Recovery and restoration                  |
| CG-11    | Evidence integrity and sufficiency        |
| CG-12    | Traceability and completeness             |
| CG-13    | Governance, competence and accountability |
| CG-14    | Validity, change and continuing assurance |
| CG-15    | Digital and OT security authority         |

Controlled states are PASS, FAIL, UNKNOWN, APPROVED_NA and NOT_ASSESSED. Conditions are separate fields. FAIL demonstrates that a prerequisite is not met. UNKNOWN means the evidence cannot establish the state. Neither can be treated as favourable.

# 19. Scoring and decision model

Scores support synthesis and trend analysis. They do not create assurance, neutralise UNKNOWN, override a gate or replace accountable judgement.

| **Decision state**     | **Meaning**                                                                                                              |
|------------------------|--------------------------------------------------------------------------------------------------------------------------|
| REASONABLY ASSURED     | Required evidence and gates support the bounded claim. This is an AIDCF internal state, not a regulated assurance level. |
| CONDITIONALLY ASSURED  | The core claim is supported subject to named, time-bound conditions and no controlling failure.                          |
| LIMITED                | Material scope, evidence or UNKNOWN restricts reliance.                                                                  |
| NOT ASSURED            | Evidence demonstrates material failure or a controlling gate fails.                                                      |
| UNKNOWN / INCONCLUSIVE | Evidence, method or boundary cannot support determination.                                                               |
| SUSPENDED              | A prior decision is invalidated by change, incident, expiry or gate state.                                               |
| WITHDRAWN              | Decision removed after material integrity or governance failure.                                                         |
| SUPERSEDED             | New approved snapshot replaces the earlier decision.                                                                     |

# 20. Machine-executable publication and conformance

| **Component**       | **Purpose**                                          | **Proof boundary**          |
|---------------------|------------------------------------------------------|-----------------------------|
| CSV registries      | Canonical identities and vocabularies.               | Identity and completeness.  |
| JSON Schema         | Structural validation.                               | Shape, not factual truth.   |
| JSON-LD             | Linked-data exchange.                                | Context and identity.       |
| RDF/OWL             | Semantic classes and relationships.                  | Declared semantics.         |
| SHACL               | Graph-shape and cardinality constraints.             | Graph conformance.          |
| Fixtures            | Positive, negative, migration and anti-gaming tests. | Expected rule behaviour.    |
| Manifest and hashes | Release inventory and integrity.                     | File-level reproducibility. |
| Conformance report  | Captured execution, versions and limitations.        | Technical result only.      |

Machine conformance cannot establish engineering adequacy, safety, operating effectiveness or assurance over a real facility. AIDCF-015 v1.2 is a canonical-baseline-aligned synthetic reference implementation, subject to independent T7 review and stated runtime limitations.

# 21. Complete synthetic worked case

![Figure 4. Synthetic service chain and assessed boundary](media/figure-4-synthetic-service-chain.png)

*Figure 4. Synthetic service chain and assessed boundary.*

The case demonstrates method execution without representing a real organisation or facility. The Capability Instance is a synthetic liquid-cooled distributed-training service. Required outcomes are job completion, checkpoint integrity, controlled thermal operation and bounded restoration. The scope contains one cluster service chain and twelve representative control assessments. This equals 3.3333% of the 360-control catalogue and cannot support full-coverage claims.

| **Case-local ID** | **Canonical domain** | **Assertion**                                                         | **Evidence object**                   |
|-------------------|----------------------|-----------------------------------------------------------------------|---------------------------------------|
| SYN-CTL-01        | CAP                  | Outcomes and operating envelope are defined.                          | EV-001 capability and outcome record. |
| SYN-CTL-02        | DEP                  | Material power, cooling, network and storage dependencies are mapped. | EV-002 dependency map.                |
| SYN-CTL-03        | POW                  | Available and resilient capacity are distinguished.                   | EV-003 capacity study.                |
| SYN-CTL-04        | THM                  | CDU and cooling-loop capacity supports declared load.                 | EV-004 thermal model.                 |
| SYN-CTL-05        | CMP                  | Cluster topology and scheduler state are controlled.                  | EV-005 compute baseline.              |
| SYN-CTL-06        | STO                  | Checkpoint integrity and restoration are addressed.                   | EV-006 storage record.                |
| SYN-CTL-07        | NET                  | Fabric topology and degraded-path performance are addressed.          | EV-007 network record.                |
| SYN-CTL-08        | OPS                  | Operational authority and response procedures are assigned.           | EV-008 procedure record.              |
| SYN-CTL-09        | RES                  | Containment and recovery dependencies are analysed.                   | EV-009 scenario record.               |
| SYN-CTL-10        | SEC                  | Privileged control-plane authority is controlled.                     | EV-010 access record.                 |
| SYN-CTL-11        | EVA                  | Evidence lineage and integrity values are retained.                   | EV-011 evidence manifest.             |
| SYN-CTL-12        | EVA                  | Decision, limitations and validity are recorded.                      | EV-012 decision record.               |

# 22. Worked-case assessment results

| **Case-local ID** | **Procedure**                                                     | **Result** | **Decision effect**                |
|-------------------|-------------------------------------------------------------------|------------|------------------------------------|
| SYN-CTL-01        | Inspect capability/outcome record and trace architecture linkage. | CONFORMING | Supports CG-01.                    |
| SYN-CTL-02        | Trace upstream, shared and recovery dependencies.                 | PARTIAL    | CG-03 remains constrained.         |
| SYN-CTL-03        | Reconcile installed, available, resilient and committed capacity. | CONFORMING | Supports CG-05 in synthetic scope. |
| SYN-CTL-04        | Review heat-load model and CDU dependency.                        | CONFORMING | Supports CG-06 in synthetic scope. |
| SYN-CTL-05        | Inspect topology, scheduler and health data.                      | CONFORMING | Supports CG-08.                    |
| SYN-CTL-06        | Inspect checkpoint evidence and restoration result.               | UNKNOWN    | CG-10 remains UNKNOWN.             |
| SYN-CTL-07        | Review fabric topology and degraded-path test.                    | PARTIAL    | Limits CG-08 confidence.           |
| SYN-CTL-08        | Review procedures and authority.                                  | CONFORMING | Supports CG-07.                    |
| SYN-CTL-09        | Review containment and recovery scenario.                         | UNKNOWN    | CG-09 and CG-10 constrained.       |
| SYN-CTL-10        | Review privilege and change evidence.                             | CONFORMING | Supports CG-15.                    |
| SYN-CTL-11        | Reperform hashes and lineage.                                     | CONFORMING | Supports CG-11.                    |
| SYN-CTL-12        | Reperform decision and limitation wording.                        | CONFORMING | Supports decision integrity.       |

Gate outcome: no real-facility gate conclusion is made. Within the synthetic case, recovery and containment remain materially UNKNOWN. Coverage is 3.3333%. The appropriate bounded decision is LIMITED. The case prohibits any claim about a real facility, complete control coverage, certification or production conformance.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Worked-case conclusion<br />
</strong>LIMITED, synthetic, non-production and non-certification. The favourable results for selected controls do not overcome low catalogue coverage or material UNKNOWN.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 23. Reporting and permitted descriptive claims

| **Claim pattern**            | **Minimum disclosure**                                                         | **Must not imply**                              |
|------------------------------|--------------------------------------------------------------------------------|-------------------------------------------------|
| AIDCF-aligned                | Artifact versions, adopted concepts and deviations.                            | Complete assessment.                            |
| Assessed using AIDCF         | Capability, profile, scope, states, period, evidence access, gates and issuer. | Certification or universal safety.              |
| AIDCF assurance-ready        | Prepared architecture, evidence ownership and programme governance.            | That controls are effective.                    |
| Continuing-assurance enabled | Approved monitoring, evidence-health and reassessment triggers.                | Perpetual validity or autonomous certification. |

These are proposed descriptive claim patterns, not badges or conformance marks. Public mark use, eligibility, evidence packages, withdrawal and challenge procedures require separate governance. “AIDCF Certified” and “AIDCF Accredited” remain prohibited.

# 24. AIDCF and AI Trust Graph

| **Integration pattern** | **Use**                                                                         | **Constraint**                                  |
|-------------------------|---------------------------------------------------------------------------------|-------------------------------------------------|
| Reference               | One method points to an entity owned by the other.                              | Do not duplicate authoritative properties.      |
| Mapping                 | Classes or relationships are broader, narrower, close or related.               | Record mapping type and reviewer.               |
| Shared identity         | The same real-world instance appears in both.                                   | One global identity with method-specific views. |
| Boundary handoff        | An infrastructure service becomes an AI-system dependency or enforcement point. | Record conditions and effective period.         |
| Scenario composition    | Infrastructure failure path connects to trust or authority path.                | Retain native semantics.                        |
| Evidence reuse          | One Evidence Object supports distinct assertions.                               | Assess relevance separately.                    |
| Decision federation     | Separate conclusions appear in one package.                                     | No automatic best- or worst-case aggregation.   |

AIDCF represents infrastructure reality and physical/digital failure. AITG represents trust, authority and exposure. The integration standard is a controlled-review draft and product architecture, proprietary algorithms, deployment design and confidential operational data remain outside its public scope.

# 25. Adoption, maturity and economics

The maturity and economic models are proposed research extensions. They are included for pilot design and are not approved AIDCF baseline content.

| **Maturity stage**                    | **Observable capability**                                          | **Caution**                           |
|---------------------------------------|--------------------------------------------------------------------|---------------------------------------|
| 1 Foundational                        | Named owner, bounded capability and critical evidence inventory.   | Not an assurance conclusion.          |
| 2 Managed                             | Repeatable ownership, architecture and issue management.           | Local consistency only.               |
| 3 Defined                             | Standard profiles, canonical IDs and traceable assessments.        | Requires quality review.              |
| 4 Measured                            | Evidence health, scenario tests and calibrated indicators.         | Requires comparable scope and method. |
| 5 Adaptive and continuously evidenced | Independent challenge, timely suspension and controlled evolution. | Must not be branded “Assured.”        |

| **Economic mechanism**        | **Pilot measure**                                                                    |
|-------------------------------|--------------------------------------------------------------------------------------|
| Stranded accelerator capacity | Unavailable accelerator-hours attributable to facility or service-chain constraints. |
| Training interruption         | Rework, restart frequency and lost job time.                                         |
| Inference degradation         | Service-outcome breach frequency and duration.                                       |
| Emergency intervention        | Unplanned specialist, vendor and logistics cost.                                     |
| Delayed programme value       | Decision delay attributable to infrastructure uncertainty.                           |
| Evidence friction             | Repeated evidence collection and review effort.                                      |

# 26. Validation status and roadmap

![Figure 5. Validation roadmap from synthetic execution to independent evidence](media/figure-5-validation-roadmap.png)

*Figure 5. Validation roadmap from synthetic execution to independent evidence.*

| **Validation item**                | **Current status**                                       | **Required closure**                                     |
|------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Canonical identity and cardinality | Approved 15/90/360 baseline.                             | Maintain controlled registry and supersession.           |
| Synthetic package                  | Baseline-aligned, twelve representative controls.        | Retain limited, synthetic claim.                         |
| Independent T7 execution           | Pending.                                                 | Independent rerun and signed report.                     |
| RDF/SHACL runtime                  | Attempted when runtime available; static tests retained. | Capture tool versions and executed output.               |
| Real capability pilot              | Not completed.                                           | Authorised multidisciplinary pilot.                      |
| Inter-rater reproducibility        | Not completed.                                           | Independent teams and disagreement analysis.             |
| Multi-site calibration             | Not completed.                                           | Different architectures, providers and operating models. |
| Public benchmark corpus            | Not completed.                                           | Anonymised permitted cases and expected outputs.         |

# 27. Threats to validity

| **Threat**                   | **Effect**                                                              | **Mitigation**                                                   |
|------------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------|
| Author concentration         | Framework design and review may reflect one viewpoint.                  | Independent multidisciplinary reviewers and public dispositions. |
| Source-selection bias        | Compared literature may omit adjacent methods.                          | Publish source register, search terms and inclusion criteria.    |
| Construct validity           | Domains, gates or maturity stages may not measure intended constructs.  | Expert review, pilot observation and revision.                   |
| Synthetic-case bias          | Fixtures can reflect designed rules rather than operational complexity. | Real evidence, messy data and external cases.                    |
| Inter-rater variability      | Different assessors may interpret requirements differently.             | Calibration, decision rules and blinded comparison.              |
| Commercial confirmation bias | Economic value may be overstated.                                       | Predefined pilot measures and transparent null results.          |
| Security disclosure risk     | Detailed dependency paths may expose sensitive infrastructure.          | Classification, minimisation and controlled reporting.           |

# 28. Limitations and exclusions

- AIDCF is a research framework and controlled methodology, not an accredited standard or certification scheme.

- The control baseline has approved identity and cardinality, but substantive adequacy still requires multidisciplinary review and pilot evidence.

- The synthetic implementation exercises twelve controls, not the full 360-control universe.

- No statistically meaningful real-facility or multi-site validation has been completed.

- Proposed gate profiles, maturity stages, claim patterns and economic measures require governance and calibration.

- Machine conformance does not prove factual truth, engineering adequacy, safety or operating effectiveness.

- The framework does not authorise switching, intrusion, failover, discharge, thermal stress or destructive testing.

- Applicable law, engineering codes, safety rules, contractual duties and professional standards remain authoritative.

# 29. Conclusion

AIDCF proposes a capability-centred assurance architecture for AI data centres and AI infrastructure. Its contribution is the explicit trace from Service Outcome to architecture, dependency and fault domain; from credible failure to safeguard; from assertion to Evidence Object and assessment; and from critical gate to accountable, bounded decision.

Version 3.0 corrects the narrative and governance weaknesses of the earlier expanded draft. It distinguishes approved baseline content from controlled-review drafts and proposed extensions, qualifies its novelty claim, documents a reproducible maintenance protocol, clarifies gate authority, provides a complete synthetic case and states threats to validity. It does not convert the framework into an established standard. The next source of credibility must be independent execution, multidisciplinary review and empirical pilot evidence.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Final proposition<br />
</strong>AIDCF should earn authority through transparent evidence, reproducible method and disciplined claim boundaries, consistent with the assurance doctrine it applies to AI infrastructure.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Appendix A. External-framework crosswalk

| **Framework**                  | **Published scope used here**                                                                                                                      | **Typical AIDCF interface**               | **Reference** |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|---------------|
| ISO/IEC 22237-1:2021           | General principles, common aspects, facilities/infrastructure classification and management references.                                            | PHY, POW, THM, ENV, OPS and RES evidence. | \[1\]         |
| NIST AI RMF 1.0                | Voluntary AI risk management and trustworthiness; Govern, Map, Measure, Manage.                                                                    | GOV, CAP, SEC and EVA linkage.            | \[2\]\[3\]    |
| Uptime Tier Standard: Topology | Site-infrastructure topology, capacity components, distribution paths and performance confirmation.                                                | POW, THM, PHY and OPS design evidence.    | \[4\]         |
| ANSI/TIA-942-C                 | Data-centre infrastructure requirements including telecommunications, power, cooling, architecture, fire protection, safety and physical security. | PHY, POW, THM and NET evidence.           | \[5\]         |
| W3C PROV-O                     | Provenance representation.                                                                                                                         | Evidence lineage and transformation.      | \[6\]         |

This crosswalk is directional and non-normative. It does not establish equivalence, coverage or conformity.

# Appendix B. Source and artifact register

| **ID**         | **Artifact**                                                      | **Status used in v2.0**                                           |
|----------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| AIDCF-005      | AI Trust Graph Integration Standard v1.0                          | Controlled-review draft.                                          |
| AIDCF-007A     | Constitutional Amendment and Canonical Registry v1.0              | Approved identity/cardinality baseline.                           |
| AIDCF-009      | Enhanced Practitioner Handbook v1.1                               | Controlled-review draft.                                          |
| AIDCF-012      | Reporting and Assurance Statement Standard v1.0                   | Controlled-review draft.                                          |
| AIDCF-013      | AI Data Centre Assurance Reference Architecture v1.0              | Controlled-review draft.                                          |
| AIDCF-014      | End-to-End Traceability and Machine-Executable Data Standard v1.0 | Controlled-review draft.                                          |
| AIDCF-015 v1.2 | Canonical Baseline Migration Package                              | Synthetic, non-production implementation; independent T7 pending. |

# Appendix C. Review and release checklist

| **Gate** | **Release requirement**                                                    | **v2.0 status**                                          |
|----------|----------------------------------------------------------------------------|----------------------------------------------------------|
| R1       | Narrative follows research sequence and has one conclusion.                | Complete.                                                |
| R2       | Novelty claim is qualified.                                                | Complete.                                                |
| R3       | Development protocol, source register and threats to validity are visible. | Protocol complete; detailed extraction register pending. |
| R4       | Gate authority distinguishes canonical and explanatory content.            | Complete.                                                |
| R5       | Complete synthetic case and claim boundaries included.                     | Complete.                                                |
| R6       | External claims have numbered citations and reference details.             | Complete for cited public scope statements.              |
| R7       | Independent multidisciplinary technical review completed.                  | Pending.                                                 |
| R8       | Independent T7 and semantic runtime evidence complete.                     | Pending.                                                 |
| R9       | Real capability pilot and inter-rater study complete.                      | Pending.                                                 |
| R10      | Licence, DOI and public repository metadata approved.                      | Pending publication decision.                            |

# Appendix D. Authorship, conflicts and contribution statement

Author: Siva Sethumadhavan. Contributions: conceptualisation, methodology design, artifact architecture, control-framework design, writing, synthetic implementation direction and visualisation. Independent technical review has not yet been completed. No claim of external organisational endorsement is made in this document. Any employment affiliation should be added only after applicable review and authorisation.

Conflict-of-interest statement: the author is the originator of AIDCF and therefore has an inherent interest in its adoption. This is mitigated through explicit limitations, open review, publication of negative tests, separation of baseline identity from substantive validation, and a roadmap for independent challenge.

# Appendix E. Version history and publication metadata

| **Version** | 3.0                     | **Principal change**                                                                                                                  |
|-------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | Internal draft          | Initial consolidated whitepaper.                                                                                                      |
| 1.1         | Expanded internal draft | Added research, gate, maturity, economics, AITG and validation sections, but retained duplicated narrative.                           |
| 2.0         | Public Review Draft     | Rebuilt narrative, qualified novelty, added protocol, status taxonomy, worked case, threats to validity, citations and release gates. |

| **Metadata field** | **Value**                                                                                                                                        |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Resource type      | Technical report / preprint                                                                                                                      |
| Title              | AIDCF: AI Data Centre Facilities Assurance Framework                                                                                             |
| Version            | 3.0                                                                                                                                              |
| Creator            | Siva Sethumadhavan                                                                                                                               |
| Licence            | To be selected before public deposit                                                                                                             |
| DOI                | To be reserved before final PDF if displayed in document                                                                                         |
| Related outputs    | Canonical registry dataset and synthetic implementation package                                                                                  |
| Keywords           | AI data centre; AI factory; infrastructure assurance; accelerated compute; liquid cooling; evidence; resilience; knowledge graph; critical gates |

# 30. v3.0 release posture and evidence boundary

Version 3.0 is a validation candidate, not a final validated standard. It consolidates the technical, editorial and governance recommendations raised during the v1.1 and v2.0 adversarial reviews. It includes author dispositions, a candidate critical-gate approval package, a derivation-record structure, an independent-review protocol and an authorised-pilot package. It does not claim that independent reviewer acceptance, canonical gate ratification or a real authorised pilot has occurred where no signed evidence is available.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Non-fabrication boundary<br />
</strong>No reviewer name, approval signature, pilot sponsor, site, result or authorisation is asserted without a signed source record. The registers below distinguish author-resolved items from evidence still pending.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| **Component**                       | **v3.0 state**                                              | **Permitted interpretation**                                         |
|-------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------------|
| Narrative and technical corrections | Author-resolved                                             | Whitepaper text incorporates the identified corrections.             |
| Reviewer dispositions               | Author disposition recorded; independent acceptance pending | Issues have proposed resolutions, not third-party endorsement.       |
| Critical-gate registry              | Candidate canonical package                                 | Ready for governance review; not independently ratified.             |
| Derivation records                  | Register structure and current evidence assembled           | Partially populated; retrospective source coding remains incomplete. |
| Pilot package                       | Authorisation and execution templates complete              | No real authorised pilot claimed.                                    |
| Synthetic implementation            | Existing AIDCF-015 v1.2                                     | Technical demonstration only, twelve controls and 3.3333% coverage.  |

# 31. Consolidated reviewer-disposition register

The register records the substantive issues raised in adversarial reviews of v1.1 and v2.0. “Author-resolved” means the text or package was changed by the framework author. It does not mean an independent reviewer accepted the disposition.

| **ID** | **Issue**                                    | **Disposition**                                                              | **Status**         | **Residual action**                                     |
|--------|----------------------------------------------|------------------------------------------------------------------------------|--------------------|---------------------------------------------------------|
| RD-001 | Narrative duplicated and concluded too early | Reordered into one research sequence with one conclusion.                    | Author-resolved    | Independent editorial acceptance pending                |
| RD-002 | Novelty claim overbroad                      | Reframed as a perceived integration gap and testable proposition.            | Author-resolved    | Literature-review challenge pending                     |
| RD-003 | Derivation not reproducible                  | Added protocol, source register, extraction and decision-log requirements.   | Partially resolved | Retrospective population pending                        |
| RD-004 | 15/90/360 symmetry not technically justified | Separated identity/cardinality design from empirical completeness.           | Author-resolved    | Domain SME challenge pending                            |
| RD-005 | Gate profiles not canonical                  | Created candidate gate-approval package and explicit provisional status.     | Partially resolved | Governance ratification pending                         |
| RD-006 | Scoring not reperformable from whitepaper    | Added scoring specification and re-performance requirements.                 | Partially resolved | Canonical numeric example pending source extraction     |
| RD-007 | Architecture too conceptual                  | Added system-of-systems, authority, evidence and failure viewpoints.         | Author-resolved    | Engineering review pending                              |
| RD-008 | Related work too narrow                      | Expanded source families and comparison criteria.                            | Author-resolved    | Systematic-search completeness pending                  |
| RD-009 | Worked case insufficiently complete          | Added traceability, evidence, result, gate and decision record requirements. | Partially resolved | Canonical MCF mapping must come from executable package |
| RD-010 | Maturity model could be misused              | Renamed Level 5 and kept model as research extension.                        | Author-resolved    | Pilot calibration pending                               |
| RD-011 | Conformance labels may become badges         | Reframed as descriptive claim patterns with governance restrictions.         | Author-resolved    | Legal and mark-governance review pending                |
| RD-012 | Economic claims not evidenced                | Converted to pilot measures and hypotheses.                                  | Author-resolved    | Empirical data pending                                  |
| RD-013 | Security disclosure governance weak          | Added information-classification and public-release rules.                   | Author-resolved    | Security review pending                                 |
| RD-014 | Public review not operationalised            | Added reviewer instructions, issue taxonomy and disposition workflow.        | Author-resolved    | Repository/contact metadata pending                     |
| RD-015 | Independent review absent                    | Added independent-review board charter and sign-off matrix.                  | Open               | Named independent reviewers pending                     |
| RD-016 | Real authorised pilot absent                 | Added pilot charter, authorisation gate and evidence pack.                   | Open               | Sponsor and signed authorisation pending                |

# 32. Canonical critical-gate approval candidate

This section defines the candidate governance record required to ratify CG-01 through CG-15. It is proposed for approval and must not be described as independently approved until the approval table is signed by the defined authorities.

| **Field**          | **Candidate rule**                                                                                                       |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| Owner              | AIDCF methodology owner.                                                                                                 |
| Approvers          | Methodology owner plus independent assurance reviewer and relevant domain specialists.                                   |
| Approval unit      | Gate identity, name, purpose, applicability, evidence floor, state criteria, decision effect and reassessment trigger.   |
| Allowed states     | PASS, FAIL, UNKNOWN, APPROVED_NA and NOT_ASSESSED.                                                                       |
| Change rule        | Meaning-changing revision requires version increment, impact analysis and supersession.                                  |
| Conflict rule      | Conflicting evidence creates UNKNOWN or FAIL according to the approved gate criterion; it cannot be silently reconciled. |
| Authority boundary | Gate evaluation constrains but does not itself issue an Assurance Decision.                                              |

| **Gate** | **Candidate name**                        | **Minimum evidence floor**                                        | **FAIL/UNKNOWN trigger**                                    | **Decision effect**         |
|----------|-------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------|-----------------------------|
| CG-01    | Capability definition                     | Defined Capability Instance, owner, outcomes and criticality      | Undefined or materially ambiguous subject                   | Blocks positive conclusion  |
| CG-02    | Boundary and operating envelope           | Physical, logical, provider, state, time and demand boundary      | Material boundary or tolerance UNKNOWN                      | Applies ceiling             |
| CG-03    | Dependency and provider confidence        | Internal, shared, external and recovery dependencies              | Hidden common mode or critical provider uncertainty         | Constrains reliance         |
| CG-04    | Physical and environmental suitability    | Site, building, zoning, hazard and environmental evidence         | Material suitability deficiency                             | May produce NOT ASSURED     |
| CG-05    | Electrical continuity                     | Capacity, quality, protection, autonomy and restoration           | Controlling path failure or insufficient evidence           | Non-compensating            |
| CG-06    | Thermal and fluid continuity              | Heat-load model, resilient capacity, fluid integrity and recovery | Thermal excursion, common controller or unverified recovery | Non-compensating            |
| CG-07    | Operational and control authority         | Competence, procedures, alarms, access and safe change            | Unclear authority or unsafe control                         | Blocks operational reliance |
| CG-08    | AI technology service-chain integrity     | Compute, storage and network performance and health               | Material technology-chain failure                           | Constrains capability claim |
| CG-09    | Containment and resilience                | Fault domains, graceful degradation and containment evidence      | Uncontained propagation or untested material scenario       | Blocks resilience claim     |
| CG-10    | Recovery and restoration                  | Recovery capacity, sequence, integrity and outcome test           | Material recovery path UNKNOWN or failed                    | Limits or suspends          |
| CG-11    | Evidence integrity and sufficiency        | Provenance, freshness, coverage, integrity and sufficiency        | Evidence cannot support a material assertion                | Blocks favourable result    |
| CG-12    | Traceability and completeness             | Forward/reverse lineage, conflicts, exclusions and UNKNOWN        | Orphan result or incomplete chain                           | Blocks issued statement     |
| CG-13    | Governance, competence and accountability | Decision rights, ownership, competence and independence           | No accountable authority or material conflict               | Blocks issuance             |
| CG-14    | Validity, change and continuing assurance | Validity, monitoring, trigger and reassessment records            | Material change invalidates conditions                      | Suspends prior decision     |
| CG-15    | Digital and OT security authority         | Identity, privilege, segmentation, detection and safe automation  | Uncontrolled privileged or automated path                   | May block operation         |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Approval status<br />
</strong>Candidate canonical package prepared. Formal ratification remains PENDING because no signed multidisciplinary approval record was found or provided.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 33. Critical-gate approval record and sign-off matrix

| **Role**                   | **Required review**                                      | **Decision** | **Evidence required**   |
|----------------------------|----------------------------------------------------------|--------------|-------------------------|
| Methodology owner          | Coherence with AIDCF principles and downstream artifacts | Pending      | Signed approval record  |
| Assurance/scoring reviewer | Gate dominance, UNKNOWN and decision effects             | Pending      | Independent review memo |
| Electrical SME             | CG-05 and cross-domain electrical effects                | Pending      | Domain disposition      |
| Mechanical/thermal SME     | CG-06 and thermal/fluid effects                          | Pending      | Domain disposition      |
| Compute/HPC SME            | CG-08 compute service chain                              | Pending      | Domain disposition      |
| Storage/network SME        | CG-08 and CG-10 data/fabric effects                      | Pending      | Domain disposition      |
| Operations/resilience SME  | CG-07, CG-09, CG-10 and CG-14                            | Pending      | Domain disposition      |
| OT/security SME            | CG-07 and CG-15                                          | Pending      | Domain disposition      |
| Evidence specialist        | CG-11 and CG-12 evidence floors                          | Pending      | Domain disposition      |
| Safety/legal reviewer      | Safety and public-claim boundaries                       | Pending      | Review memorandum       |

A gate becomes CANONICAL only when the required approvals are complete, unresolved objections are recorded and the resulting registry is versioned with an effective date. Author approval alone is insufficient for independent validation.

# 34. Full derivation-record package

The derivation package is the evidence needed to show how AIDCF was constructed. The table distinguishes records present conceptually from records that still require retrospective population or independent verification.

| **Record**                        | **Required contents**                                                                    | **v3.0 state**                                                  |
|-----------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| DR-01 Source register             | Title, publisher, edition, scope, access basis, inclusion rationale and extraction date. | Partially populated in references; full register pending.       |
| DR-02 Search protocol             | Databases/sites, search strings, dates, inclusion/exclusion criteria and reviewer.       | Specified below; execution log pending.                         |
| DR-03 Concept extraction matrix   | Source passage, concept, class, property, relationship and analyst note.                 | Template complete; population pending.                          |
| DR-04 Terminology log             | Ambiguous term, alternatives, adopted meaning and rationale.                             | Core terminology populated; full decisions pending.             |
| DR-05 Domain cluster matrix       | Concept-to-domain mapping, rejected clusters and coverage test.                          | High-level cluster rationale complete; detailed matrix pending. |
| DR-06 Control derivation register | Source need, objective, canonical control, duplicate review and evidence mapping.        | Canonical registry exists; derivation evidence pending.         |
| DR-07 Gate derivation register    | Failure consequence, prerequisite, evidence floor and decision effect.                   | Candidate package complete; approval pending.                   |
| DR-08 Reviewer register           | Reviewer competence, independence, comments and dispositions.                            | Author dispositions complete; independent register pending.     |
| DR-09 Change and supersession log | Changed object, reason, impact, version and migration.                                   | AIDCF-007A and AIDCF-015 migration evidence exists.             |
| DR-10 Validation corpus           | Positive, negative, anti-gaming and benchmark cases.                                     | Synthetic fixtures exist; public corpus pending.                |

## 34.1 Search and inclusion protocol

- Prioritise official standards bodies, public institutional guidance, peer-reviewed or established assurance literature and authoritative vendor-neutral technical bodies.

- Record exact search terms, date executed, source URL or DOI, edition, access restriction and reviewer.

- Include sources relevant to facilities, AI technology, OT/control systems, reliability, evidence, assurance arguments, provenance and machine validation.

- Exclude unsupported marketing claims, unattributed summaries and sources whose scope cannot be established.

- Treat paywalled normative standards through their accessible abstracts unless licensed full text is available. Do not imply clause-level comparison from public abstracts.

## 34.2 Comparative analysis criteria

| **Criterion**        | **Question**                                                         |
|----------------------|----------------------------------------------------------------------|
| Subject              | What system or proposition is assessed?                              |
| Facility coverage    | Are power, thermal, physical and environmental systems included?     |
| AI technology        | Are configured compute, storage, fabrics and orchestration included? |
| Operations           | Are operating states, change and recovery addressed?                 |
| Failure reasoning    | Are common modes and propagation explicit?                           |
| Evidence             | Are provenance, freshness, coverage and sufficiency explicit?        |
| Uncertainty          | Can missing or conflicting evidence remain UNKNOWN?                  |
| Decision restraint   | Can critical prerequisites override aggregate scores?                |
| Machine traceability | Can conclusions be reconstructed and validated?                      |
| Authority            | Who may issue, rely on, suspend or withdraw a conclusion?            |

# 35. Expanded related-work map

| **Source family**                         | **Explicit public scope used**                                                                         | **AIDCF interface**                           | **Review caveat**                                           |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------|-------------------------------------------------------------|
| ISO/IEC 22237 and EN 50600                | Data-centre facilities, infrastructure, availability, security, efficiency and management concepts.    | PHY, POW, THM, ENV, OPS and RES.              | No clause-level equivalence claimed.                        |
| ANSI/TIA-942-C                            | Telecommunications, power, cooling, architecture, fire protection, safety and physical security.       | PHY, POW, THM and NET.                        | No TIA certification claim.                                 |
| Uptime Tier Topology                      | Site-infrastructure capacity components and distribution paths across Tier classifications.            | POW, THM, PHY and OPS design evidence.        | Tier is not converted to capability assurance.              |
| ISA/IEC 62443                             | Requirements and processes for electronically secure IACS across lifecycle, operations and technology. | SEC, OPS and SUP.                             | Cybersecurity proof does not establish facility resilience. |
| NIST AI RMF                               | Voluntary AI risk-management and trustworthiness functions.                                            | GOV, CAP, SEC and EVA linkage.                | AIDCF is complementary, not a NIST profile.                 |
| ASHRAE data-centre resources              | Cooling, energy, environmental and technology-space design/operation guidance.                         | THM and ENV evidence.                         | Engineering criteria remain source-owned.                   |
| Reliability and safety techniques         | FMEA/FMECA, fault trees, event trees, bow ties and structured hazard analysis.                         | DEP, RES and engineering domains.             | Competent method use required.                              |
| Assurance-case methods                    | Structured claim, argument and evidence patterns.                                                      | AIDCF assurance graph and reporting.          | Formal GSN mapping remains future work.                     |
| W3C PROV-O and semantic standards         | Provenance and graph representation.                                                                   | Evidence lineage and machine exchange.        | Semantic conformance does not prove truth.                  |
| OCP and vendor AI reference architectures | Open or validated implementation patterns for AI infrastructure.                                       | Architecture evidence and interface patterns. | Reference design does not prove site operation.             |

# 36. Control-universe completeness and symmetry test

The 15/90/360 structure is an AIDCF-internal identity and cardinality baseline. Equal family and control counts are catalogue-design constraints supporting stable identity and machine processing. They are not evidence that all domains possess equal inherent complexity.

| **Test**                      | **Method**                                                            | **Acceptance**                                                         |
|-------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------|
| External requirement coverage | Map source requirements and concepts to domains/families/controls.    | No material orphan without documented exclusion.                       |
| Incident coverage             | Map representative AI-infrastructure incidents and failure scenarios. | Every material path maps or triggers extension.                        |
| Duplicate analysis            | Compare objectives, conditions, evidence and effects.                 | Duplicates merged or differentiated explicitly.                        |
| Padding test                  | Challenge low-density families and generic control wording.           | No control retained solely to satisfy cardinality.                     |
| Compression test              | Challenge high-complexity domains for overloaded controls.            | Split when one control has materially distinct evidence and ownership. |
| Pilot orphan test             | Record findings that cannot be classified.                            | Unmapped material finding creates change proposal.                     |

# 37. Scoring re-performance specification

AIDCF-010 states that raw and adjusted indicators, coverage, confidence, gate overlays and accountable decisions remain separate, and that scores do not create assurance. The whitepaper therefore defines a minimum re-performance record without inventing numeric weights not present in approved source evidence.

| **Field**          | **Required value**                                                        |
|--------------------|---------------------------------------------------------------------------|
| Capability/profile | Stable ID, version and applicable control set.                            |
| Control input      | Dimension results, applicability, assessor and reviewer.                  |
| Evidence overlay   | Evidence-quality index, sufficiency and confidence.                       |
| Coverage           | Applicable, numerically assessed, UNKNOWN, not assessed and approved N/A. |
| Formula version    | Exact configuration and weight set.                                       |
| Raw indicator      | Deterministic output before evidence/gate effects.                        |
| Adjusted indicator | Separately labelled output after declared evidence rule.                  |
| Gate overlay       | All applicable gate states and controlling reasons.                       |
| Recommendation     | Engine output with reasons.                                               |
| Decision           | Human authority, review, limitations, validity and triggers.              |
| Re-performance     | Input hash, tool version, output hash and independent result.             |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Current evidence<br />
</strong>The synthetic package contains a score snapshot and deterministic score re-performance output, but v3.0 does not reproduce an exact numeric calculation because the necessary source values were not available in the retrieved excerpts. Fabricating weights or scores would violate the framework’s evidence doctrine.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 38. Technical architecture viewpoints

| **Viewpoint**           | **Mandatory elements**                                                               | **Review question**                                  |
|-------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------|
| Service outcome         | Capability, users, outcomes, tolerances and criticality.                             | What result must be protected?                       |
| Physical facility       | Site, space, power, cooling, fluid, environment and physical routes.                 | What physical infrastructure enables the outcome?    |
| AI technology           | Compute, scheduler, storage, metadata, fabrics, gateways and management planes.      | What configured technology enables the outcome?      |
| Authority               | Identities, privileges, automation, remote support and emergency control.            | Who or what can change the state?                    |
| Dependency/fault domain | Shared sources, controls, routes, people, suppliers and recovery resources.          | What can fail together?                              |
| Evidence                | Telemetry, configuration, tests, documents, human evidence and independent evidence. | What proves each assertion?                          |
| Failure and recovery    | Initiation, propagation, containment, recovery and residual path.                    | How is the outcome lost and restored?                |
| AITG handoff            | Shared identity, boundary interface, trust/authority path and federated decision.    | Where do infrastructure and AI trust reasoning meet? |

# 39. Full scenario-record example

| **Field**              | **Synthetic example**                                                                           |
|------------------------|-------------------------------------------------------------------------------------------------|
| Scenario ID            | SCN-SYN-THM-001                                                                                 |
| Capability outcome     | Distributed-training job completion and controlled thermal operation.                           |
| Initiating condition   | Synthetic reduction in CDU flow.                                                                |
| Preconditions          | Declared high-load training state and dependence on the affected loop.                          |
| Local failure mode     | Reduced coolant flow at the synthetic cooling distribution unit.                                |
| Propagation            | Temperature rise -\> accelerator throttling -\> collective delay -\> checkpoint exposure.       |
| Affected states        | Normal transitions to degraded; recovery path required.                                         |
| Safeguards             | Flow alarm, temperature telemetry, load reduction, isolation and recovery procedure.            |
| Safeguard dependencies | Sensor integrity, management network, operator authority and alternate capacity.                |
| Residual path          | Common controller or insufficient alternate thermal capacity.                                   |
| Evidence requirements  | P&ID, heat-load model, flow/temperature telemetry, alarms, operator record and authorised test. |
| Gate effects           | CG-06, CG-08, CG-09 and CG-10.                                                                  |
| Safety boundary        | No live reduction or switching without explicit competent authorisation.                        |
| Reassessment trigger   | Thermal design, firmware, load, provider, incident or evidence change.                          |

# 40. Information-classification and disclosure model

| **Class**         | **Permitted content**                                                                             | **Restricted examples**                                    |
|-------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| PUBLIC            | Framework concepts, synthetic examples, public references and aggregate validation status.        | No real site paths, credentials or exploitable weaknesses. |
| CONTROLLED        | Detailed control mappings, reviewer comments and non-sensitive pilot summaries.                   | Distribution limited to authorised reviewers.              |
| CONFIDENTIAL      | Architecture, provider boundaries, evidence, findings and remediation.                            | No public deposit.                                         |
| HIGHLY RESTRICTED | Privileged paths, physical routes, emergency procedures, vulnerabilities and sensitive telemetry. | Need-to-know access and separate secure repository.        |

- Public reports may redact detail but must not hide decision limitations, material gate FAIL/UNKNOWN or scope restrictions.

- Graph exports must filter restricted nodes, relationships and properties according to classification.

- Evidence references should use controlled identifiers rather than embedding secrets or sensitive records.

- Public benchmark cases must be synthetic or demonstrably authorised and anonymised.

# 41. Independent review board charter

| **Element**  | **Requirement**                                                                                                                                        |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Purpose      | Challenge technical adequacy, evidence doctrine, claims, safety, scoring, semantics and usability.                                                     |
| Independence | Reviewers disclose conflicts, prior design involvement and commercial interest.                                                                        |
| Competence   | Collective electrical, mechanical, AI/HPC, storage/network, operations, OT security, assurance, measurement, legal/safety and semantic-web competence. |
| Method       | Issue-based review using severity, evidence, recommendation and disposition.                                                                           |
| Decision     | Accept, accept with condition, reject, or defer each material disposition.                                                                             |
| Transparency | Publish non-sensitive comments and dispositions with reviewer consent.                                                                                 |
| Authority    | Review board advises; framework governance approves releases.                                                                                          |
| Stop rule    | Material unresolved safety, evidence-integrity or claim issue prevents final release.                                                                  |

# 42. Public review instructions and issue taxonomy

A real public-review release must publish a review channel and dates in the repository or deposit metadata. Those details cannot be invented in this document and remain placeholders until selected by the author.

| **Issue type** | **Use**                                                     |
|----------------|-------------------------------------------------------------|
| TECH           | Technical validity, engineering or AI-infrastructure issue. |
| ASSUR          | Evidence, assurance, gates, scoring or decision issue.      |
| SEM            | Ontology, graph, identity or machine-validation issue.      |
| SAFE           | Safety, legality, privacy or security-disclosure issue.     |
| ED             | Editorial, terminology or structure issue.                  |
| IMPL           | Implementation, tooling or interoperability issue.          |
| PILOT          | Pilot design, feasibility or measurement issue.             |

| **Required comment field** | **Content**                                      |
|----------------------------|--------------------------------------------------|
| Comment ID                 | Stable identifier.                               |
| Section/object             | Exact artifact version and location.             |
| Issue                      | Concise statement.                               |
| Evidence                   | Source or reasoning.                             |
| Severity                   | Blocker, major, moderate or editorial.           |
| Recommendation             | Proposed change.                                 |
| Disposition                | Accept, partial, reject or defer with rationale. |
| Reviewer response          | Acceptance or objection.                         |
| Closure evidence           | Changed artifact, test or decision record.       |

# 43. Authorised pilot programme package

The user requested at least one authorised pilot. No signed AIDCF pilot charter, named sponsor, authorised site or completed pilot result was found in the available AIDCF sources. Therefore v3.0 includes the complete pilot-authorisation and execution package but does not falsely claim that a real pilot has been authorised or completed.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Pilot status<br />
</strong>PILOT-001: NOT AUTHORISED / NOT EXECUTED. This is a controlled template and execution plan, not a pilot result.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| **Pilot field**   | **Required content**                                                                    |
|-------------------|-----------------------------------------------------------------------------------------|
| Pilot ID          | PILOT-001                                                                               |
| Sponsor           | Named accountable organisational sponsor.                                               |
| Capability owner  | Owner of the bounded AI Capability Instance.                                            |
| Decision question | Exact intended decision and prohibited interpretation.                                  |
| Scope             | Physical, logical, organisational, provider and temporal boundary.                      |
| Operating states  | Normal, maintenance, degraded, emergency, recovery and transition as applicable.        |
| Profile           | Control, gate, evidence and assurance-depth profile.                                    |
| Authorisation     | Signed scope, access, safety, testing and disclosure approval.                          |
| Team              | Lead assessor, domain SMEs, evidence lead, independent reviewer and decision authority. |
| Data handling     | Classification, retention, redaction and permitted publication.                         |
| Stop criteria     | Unsafe condition, unresolved authority, source-integrity failure or scope breach.       |
| Outputs           | Charter, plan, evidence manifest, workpapers, gates, decision, report and lessons.      |

## 43.1 Pilot acceptance criteria

- Every assessed assertion has a stable identity and evidence reference.

- All applicable gates have completed workbooks and independent review.

- UNKNOWN, exclusions, conflicts and inaccessible scope remain visible.

- Coverage is calculated against the approved applicable profile.

- No test exceeds written authority or competent engineering governance.

- The issued decision is bounded by scope, states, period, evidence and intended users.

- Any public case material has explicit disclosure approval.

# 44. Pilot execution plan and measurement framework

| **Phase**      | **Activity**                                                           | **Exit evidence**                   |
|----------------|------------------------------------------------------------------------|-------------------------------------|
| Authorise      | Approve charter, roles, safety, access, data handling and publication. | Signed pilot authorisation.         |
| Profile        | Define outcomes, architecture, boundaries, states, controls and gates. | Approved pilot profile.             |
| Plan           | Methods, samples, tests, reviewers and stop rules.                     | Assessment plan.                    |
| Collect        | Acquire evidence with provenance, integrity and restrictions.          | Evidence manifest.                  |
| Assess         | Execute control procedures and scenario analysis.                      | Reviewed workpapers.                |
| Gate and score | Evaluate gates and reproduce score.                                    | Gate register and score snapshot.   |
| Decide         | Independent review and accountable decision.                           | Signed bounded decision.            |
| Report         | Issue controlled reports and public summary if authorised.             | Report package.                     |
| Learn          | Record usability, disagreements, orphan findings and changes.          | Pilot lessons and change proposals. |

| **Measure**         | **Definition**                                                                                     |
|---------------------|----------------------------------------------------------------------------------------------------|
| Scope agreement     | Inter-rater consistency in capability and boundary definition.                                     |
| Trace completeness  | Required chain links present and reverse-queryable.                                                |
| Evidence effort     | Effort to collect, validate and review evidence.                                                   |
| Gate agreement      | Inter-rater gate-state agreement and disagreement causes.                                          |
| Control agreement   | Inter-rater control-result agreement.                                                              |
| Orphan findings     | Material findings without a suitable domain/control mapping.                                       |
| Decision usefulness | Named user assessment of relevance and clarity.                                                    |
| Economic signal     | Observed accelerator-hours, interruption, recovery or evidence-friction measures where authorised. |

# 45. Pilot authorisation and result record

| **Approval/result**             | **Status**     | **Required evidence**                  |
|---------------------------------|----------------|----------------------------------------|
| Sponsor authorisation           | PENDING        | Signed charter                         |
| Capability-owner authorisation  | PENDING        | Scope and evidence-access approval     |
| Safety/testing authorisation    | PENDING        | Rules of engagement and stop criteria  |
| Data/privacy/security approval  | PENDING        | Classification and disclosure decision |
| Independent reviewer acceptance | PENDING        | Review memorandum                      |
| Execution                       | NOT STARTED    | Workpapers and logs                    |
| Assurance Decision              | NOT ISSUED     | Signed decision record                 |
| Public summary                  | NOT AUTHORISED | Publication approval                   |

This record is intentionally incomplete. Completing it requires real organisational authority, named reviewers and evidence that cannot be fabricated by the whitepaper author or the drafting assistant.

# 46. AITG composed scenario example

| **Layer**                 | **Synthetic composed path**                                                                                               |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------|
| AIDCF infrastructure path | Cooling-control dependency degrades thermal capacity and affects accelerator operation.                                   |
| Boundary handoff          | The cooling-management service is referenced as a dependency and enforcement point for the AI capability.                 |
| AITG path                 | Authority over the management interface and remote-support relationship are examined as trust and exposure relationships. |
| Evidence reuse            | Access logs and configuration records support separate AIDCF and AITG assertions with distinct relevance reviews.         |
| Native findings           | AIDCF reports infrastructure safeguard and recovery effects; AITG reports authority/exposure effects.                     |
| Federated decision        | Both conclusions appear in one package without automatic aggregation.                                                     |

# 47. Publication and archival release gate

| **Release item**                 | **Required before final v3.0**                                                          |
|----------------------------------|-----------------------------------------------------------------------------------------|
| Table of contents and navigation | Generate and update fields in final PDF/DOCX.                                           |
| Licence                          | Select whitepaper, dataset and software licences separately.                            |
| DOI                              | Reserve DOI and insert into final artefacts and metadata.                               |
| Independent review               | Close or disclose all blocker/major issues.                                             |
| Gate approval                    | Publish signed canonical gate registry.                                                 |
| Pilot                            | Complete at least one genuinely authorised pilot or retain validation-candidate status. |
| Accessibility                    | Alt text, tagged reading order, table headers, bookmarks and contrast.                  |
| Archival PDF                     | Produce stable PDF/PDF-A as appropriate with embedded fonts.                            |
| Manifest                         | Publish checksums, versions and related-output identifiers.                             |
| Review channel                   | Publish issue/contact channel and disposition policy.                                   |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Release rule<br />
</strong>If independent gate approval and an authorised pilot remain incomplete, the document must retain VALIDATION CANDIDATE or PUBLIC REVIEW DRAFT status. It must not be presented as a final validated framework.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 48. v3.0 conclusion

AIDCF v3.0 is a comprehensive validation candidate. It integrates the conceptual model, control universe, evidence and assessment doctrine, gate-controlled decision model, machine-executable traceability, reviewer dispositions, candidate gate registry, derivation-record package, security disclosure model, independent-review charter and pilot programme package.

The remaining work is evidential, not editorial: named independent reviewers must accept or challenge the dispositions; the critical gates must be ratified through documented governance; the derivation registers must be populated and reviewed; scoring must be re-performed from disclosed source values; and at least one real pilot must be authorised and executed. Until those records exist, v3.0 is not described as externally validated.

# References

\[1\] International Organization for Standardization. ISO/IEC 22237-1:2021, Information technology - Data centre facilities and infrastructures - Part 1: General concepts. Edition 1, October 2021. https://www.iso.org/standard/78550.html

\[2\] National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1. January 2023. DOI: 10.6028/NIST.AI.100-1.

\[3\] National Institute of Standards and Technology. NIST AI RMF Playbook. Companion guidance for Govern, Map, Measure and Manage. Public web resource, updated June 10, 2026.

\[4\] Uptime Institute. Tier Standard: Topology. Public abstract describing comparison of site-infrastructure topology and four Tier classifications. https://uptimeinstitute.com/publications/asset/tier-standard-topology

\[5\] Telecommunications Industry Association. ANSI/TIA-942-C, Telecommunications Infrastructure Standard for Data Centers. Revision C, published May 2024. https://tiaonline.org/standard/tia-942/

\[6\] World Wide Web Consortium. PROV-O: The PROV Ontology. W3C Recommendation, April 30, 2013.

\[7\] Sethumadhavan, S. AIDCF-005 AI Trust Graph Integration Standard v1.0. Controlled-review draft.

\[8\] Sethumadhavan, S. AIDCF-007A Constitutional Amendment and Canonical Master Control Registry v1.0. Approved AIDCF baseline.

\[9\] Sethumadhavan, S. AIDCF-009 Assessment Methodology Enhanced Practitioner Handbook v1.1. Controlled-review draft.

\[10\] Sethumadhavan, S. AIDCF-012 Reporting and Assurance Statement Standard v1.0. Controlled-review draft.

\[11\] Sethumadhavan, S. AIDCF-013 AI Data Centre Assurance Reference Architecture v1.0. Controlled-review draft.

\[12\] Sethumadhavan, S. AIDCF-014 End-to-End Traceability and Machine-Executable Data Standard v1.0. Controlled-review draft.

\[13\] Sethumadhavan, S. AIDCF-015 v1.2 Canonical Baseline Migration Package. Synthetic, non-production reference implementation.
