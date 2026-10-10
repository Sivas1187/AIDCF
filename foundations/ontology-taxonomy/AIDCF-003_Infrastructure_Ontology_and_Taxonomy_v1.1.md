> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-003_Infrastructure_Ontology_and_Taxonomy_v1.1.pdf](AIDCF-003_Infrastructure_Ontology_and_Taxonomy_v1.1.pdf).

**AIDCF**

# INFRASTRUCTURE ONTOLOGY & TAXONOMY

*AI Data Centre Facilities Assurance Framework*

Version 1.1

Canonical semantics for capability-centred AI infrastructure assurance

Artifact ID: AIDCF-003 (short code IOT)  
Artifact type: Normative foundation standard  
Status: Draft for controlled review  
Date: 2026-10-10  
Author: Siva Sethumadhavan  
Release 1: Foundational Methodology

This document defines the canonical entity classes, taxonomies, relationships, properties, constraints and machine-readable expectations used to represent AI infrastructure within AIDCF.

# Document control

| **Field**            | **Value**                                                                                                                                                                                                |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Title                | AIDCF Infrastructure Ontology and Taxonomy                                                                                                                                                               |
| Artifact ID          | AIDCF-003 (short code IOT)                                                                                                                                                                               |
| Version              | 1.1                                                                                                                                                                                                      |
| Date                 | 2026-10-10                                                                                                                                                                                               |
| Artifact type        | Normative foundation standard                                                                                                                                                                            |
| Status               | Draft for controlled review                                                                                                                                                                              |
| Author               | Siva Sethumadhavan                                                                                                                                                                                       |
| Depends on           | AIDCF-001 AIDCF Manifesto; AIDCF-002 Core Conceptual Model                                                                                                                                               |
| Aligned with         | AIDCF-007A Canonical Master Control Registry (15 domains, 90 families, 360 controls); AIDCF-014 End-to-End Traceability and Machine-Executable Data Standard (§7 object classes, §9 relationship types) |
| Downstream users     | AIDCF-004; AIDCF-005; AIDCF-008; AIDCF-009; AIDCF-010; AIDCF-016; AIDCF-018 domain guides; compatible tooling                                                                                            |
| Normative language   | Shall / shall not = requirement; should / should not = recommendation; may = permission; can = capability, as defined in AIDCF-002                                                                       |
| Intended audience    | AI infrastructure architects; data-centre engineers; assessors; operators; owners; technology teams; resilience, security and assurance practitioners; ontology engineers; product teams                 |
| Publication boundary | Independent methodology. Not a substitute for law, licensed engineering, safety approval, regulatory certification or vendor design authority. AIDCF does not certify.                                   |

## Revision history

| **Version** | **Date**   | **Summary**                                                                                                                                                                                                                                                                                                                                     |
|-------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | —          | Controlled-review baseline for expert review and machine-readable implementation.                                                                                                                                                                                                                                                              |
| 1.1         | 2026-10-10 | Re-baselined taxonomy and class registry to the 15 AIDCF-007A domain codes; added assurance-chain classes (Part XV) and IEC 62443 IACS concepts (Part XVI); adopted the canonical 16-step chain, "Required Function", the `https://w3id.org/aidcf/ontology#` namespace and AIDCF-014 predicate mappings; aligned confidence to CONF-0..CONF-4; public artifact IDs; consecutive requirement IDs (legacy mapping in Appendix G). |

## Relationship to AIDCF-002

AIDCF-002 Core Conceptual Model defines what the AIDCF concepts mean and how they reason together; this standard defines how those concepts are represented as classes, properties, relationships, controlled values and validation rules. Every class in this ontology realises a concept defined in AIDCF-002, and where a definition here is shorter or more formal, the AIDCF-002 meaning governs. The canonical assurance chain, the definition of MATERIAL, the claim types, result, gate and decision vocabularies, and the legacy-to-15 domain mapping are owned by AIDCF-002 and are reused here without redefinition. AIDCF-014 then fixes the exchange names of the same classes and relationships; this ontology maps to those names explicitly (Appendix A, Appendix B).

# Executive thesis

AIDCF represents an AI data centre as a capability-supporting system rather than a collection of equipment. The ontology begins with a defined Capability Instance and Service Outcomes, traces them to infrastructure functions and assets, expresses direct, indirect and shared dependencies, records capacity and operating conditions, and provides stable attachment points for failures, safeguards, evidence and assurance decisions.

## Canonical chain

This standard uses the canonical AIDCF assurance chain defined in AIDCF-002 §9 without modification:

1 Decision Question → 2 Capability Instance → 3 Service Outcome → 4 Required Function → 5 Architecture (InfrastructureSystem / AssetInstance / Interface) → 6 Dependency and Fault Domain → 7 Threat / Hazard / Failure Scenario → 8 Safeguard → 9 Control → 10 Evidence Requirement → 11 Evidence Object → 12 Control Assessment (result) → 13 Finding / UNKNOWN Record → 14 Gate Result → 15 Score Snapshot and Decision Recommendation → 16 Assurance Decision → (Assurance Report and Reassessment Trigger close the loop back to 2).

Parts III–XI of this standard specify the classes for steps 2–6 and the attachment points for steps 7–8 (whose semantics are owned by AIDCF-004). Part XV specifies the classes for steps 1 and 9–16 and the closing loop. Operating states (Part X) qualify every step as context and assumptions.

## How to use this standard

- Use Parts I-IV to establish a conformant assessment information model.

- Use Parts V-VII to classify infrastructure across the fifteen AIDCF domains (GOV, CAP, DEP, PHY, POW, THM, ENV, CMP, STO, NET, OPS, RES, SUP, SEC, EVA).

- Use Parts VIII-XI to represent relationships, dependencies, states, capacity, responsibility and uncertainty.

- Use Parts XII-XIV to validate records, create implementation profiles and produce machine-readable releases.

- Use Parts XV-XVI to represent the assurance half of the chain (controls, evidence, results, gates, decisions, reports, triggers) and industrial control-system security concepts.

- Do not treat the taxonomy as a control checklist or a substitute for engineering analysis.

# Contents

1\. Part I - Authority, scope and conformance

2\. Part II - Ontology architecture and design principles

3\. Part III - Upper ontology and canonical entities

4\. Part IV - Capability, outcome, boundary and lifecycle model

5\. Part V - Fifteen-domain infrastructure taxonomy

6\. Part VI - Cross-cutting classification facets

7\. Part VII - Asset, system, interface and resource model

8\. Part VIII - Relationship and dependency vocabulary

9\. Part IX - Capacity, redundancy, fault-domain and resilience semantics

10\. Part X - Operating state, temporal state and change semantics

11\. Part XI - Responsibility, evidence, confidence and UNKNOWN semantics

12\. Part XII - Conformance rules and validation shapes

13\. Part XIII - Reference implementation profiles

14\. Part XIV - Machine-readable publication specification

15\. Part XV - Assurance-chain classes

16\. Part XVI - Industrial automation and control system security concepts (IEC 62443 alignment)

17\. Appendix A - Canonical class registry

18\. Appendix B - Canonical relationship registry

19\. Appendix C - Minimum property schemas

20\. Appendix D - Naming, identifier and namespace rules

21\. Appendix E - Standards and reference-source map

22\. Appendix F - Review and acceptance record

23\. Appendix G - Legacy identifier mapping

# Part I - Authority, scope and conformance

## 1. Purpose

This artifact establishes the controlled vocabulary and semantic structure by which AIDCF describes AI capabilities and the physical, engineered, technical, operational, human and external infrastructure on which they depend. It is intended to create consistency across documents, assessments, datasets, knowledge graphs, digital twins and future tooling.

## 2. Objectives

- Provide a capability-first upper ontology.

- Define a vendor-neutral taxonomy organised by the fifteen AIDCF domain codes of AIDCF-007A.

- Express cross-domain and external dependencies without hiding scope boundaries.

- Distinguish systems, assets, components, interfaces, resources, services, roles and evidence.

- Represent capacity, redundancy, fault domains, operating states and temporal change.

- Preserve provenance, confidence, conflict and UNKNOWN.

- Provide machine-readable semantics without requiring proprietary software.

- Provide the classes on which failure analysis (AIDCF-004), control mapping (AIDCF-007A), evidence (AIDCF-008), assessment (AIDCF-009), gates and decisions (AIDCF-010) and reporting (AIDCF-012) attach.

## 3. Scope

The ontology covers entities materially relevant to the ability of a defined AI Capability Instance to deliver specified Service Outcomes. It spans the fifteen AIDCF domains: governance (GOV); capability, outcome and demand (CAP); dependency and external reliance (DEP); physical site, building and security (PHY); electrical power (POW); cooling, thermal and fluid systems (THM); environmental and resource performance (ENV); AI compute (CMP); AI storage and data (STO); AI network and interconnect (NET); building operations (OPS); resilience and recovery (RES); supply chain (SUP); digital, OT and control-plane security (SEC); and evidence, assessment and assurance management (EVA).

## 4. Exclusions

- Model quality, fairness, explainability and responsible-AI governance, except where a digital element is an infrastructure dependency.

- Application business logic, agent authority and model-to-tool trust paths, which remain primarily within AI Trust Graph.

- Legal compliance determinations and jurisdiction-specific certification decisions.

- Professional engineering approval, safety certification and life-safety design authority.

- Vendor endorsement or prescriptive selection of accelerator, fabric, storage or cooling technology.

## 5. Normative conformance

> **IOT-REQ-001** A conformant implementation shall preserve the canonical meanings and required distinctions in this artifact.
>
> **IOT-REQ-002** Extensions may add classes, relationships or properties but shall not silently redefine canonical terms.
>
> **IOT-REQ-003** Every material entity shall possess a stable identifier, class, lifecycle status, provenance, evidence status and, where it supports an assurance claim, a confidence value (CONF-0 to CONF-4 per AIDCF-008).
>
> **IOT-REQ-004** Every assessment dataset shall identify the Capability Instance, Assessment Boundary, applicable Service Outcomes and Operating Envelope.
>
> **IOT-REQ-005** Dependencies crossing the Assessment Boundary shall remain represented as external dependencies or UNKNOWN; they shall not disappear because they are out of scope.
>
> **IOT-REQ-006** UNKNOWN shall remain a first-class semantic state and shall not be converted into pass, fail, zero, not applicable or accepted risk.

## 6. Conformance levels

| **Level** | **Name**                        | **Minimum expectation**                                                                                            |
|-----------|---------------------------------|--------------------------------------------------------------------------------------------------------------------|
| IOT-CL0   | Vocabulary alignment            | Uses canonical terms and the fifteen domain codes without contradictory meanings.                                  |
| IOT-CL1   | Structured representation       | Implements required entities, identifiers and core relationships.                                                  |
| IOT-CL2   | Assurance-ready dataset         | Adds boundaries, outcomes, dependencies, states, evidence, confidence, the Part XV assurance classes and validation. |
| IOT-CL3   | Graph-conformant implementation | Implements machine-readable schema, AIDCF-014 relationship mappings and validation shapes.                         |
| IOT-CL4   | Controlled extension            | Publishes namespace, mappings, governance, tests and change impact for extensions.                                 |

Conformance levels IOT-CL0 to IOT-CL4 were labelled C0 to C4 in v1.0; they are renamed so that they cannot be confused with the evidence coverage dimension C of AIDCF-008.

# Part II - Ontology architecture and design principles

## 7. Four-layer semantic architecture

| **Layer**                  | **Purpose**                               | **Examples**                                                            |
|----------------------------|-------------------------------------------|-------------------------------------------------------------------------|
| L0 Doctrine                | Constrains meaning and reasoning          | Capability-first; evidence-gated; cross-domain; UNKNOWN preservation (AIDCF-001, AIDCF-002). |
| L1 Upper ontology          | Defines universal entity types            | Capability, Outcome, System, Asset, Dependency, State, Actor, Evidence. |
| L2 Domain taxonomy         | Classifies domain-specific infrastructure | UPS, CDU, accelerator node, parallel file system, scale-out fabric.     |
| L3 Profiles and extensions | Specialises for deployment patterns       | Sovereign AI, colocation, liquid-cooled training, enterprise inference. |

## 8. Design principles

> **P1 Capability primacy** The ontology begins with what the infrastructure must enable.
>
> **P2 Instance specificity** An assessed deployment is represented as an instance, not merely a generic type.
>
> **P3 Function before product** Required functions are separated from the products that implement them.
>
> **P4 Relationship explicitness** Material dependencies and interfaces are encoded, not left only in narrative.
>
> **P5 State awareness** Claims are tied to declared operating states (NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION, SHUTDOWN, FAILED, UNKNOWN; §45).
>
> **P6 Time awareness** Design, as-built, commissioned and current states are distinguishable.
>
> **P7 Evidence anchoring** Material assertions can be linked to evidence and provenance.
>
> **P8 Vendor neutrality** Canonical classes do not require one supplier, topology or technology.
>
> **P9 Safe extensibility** Profiles can specialise the model without breaking semantic compatibility.
>
> **P10 Minimal false precision** Unknown or conflicting information remains visible.

## 9. Metamodel

Each ontology term is described through a common metamodel.

| **Field**           | **Meaning**                                               |
|---------------------|-----------------------------------------------------------|
| Canonical ID        | Stable AIDCF identifier.                                  |
| Preferred label     | Authoritative human-readable name.                        |
| Definition          | Necessary and distinguishing meaning.                     |
| Entity type         | Class, relationship, property, enumeration or constraint. |
| Parent              | Immediate broader concept.                                |
| Domain              | One primary AIDCF domain code (GOV … EVA) and optional secondary codes, or Upper for cross-domain upper-ontology classes. |
| Allowed relations   | Permitted outgoing and incoming relationships.            |
| Required properties | Minimum data needed for conformance.                      |
| Lifecycle status    | Draft, released, deprecated or retired.                   |
| Provenance          | Origin, author, approval and version.                     |
| Examples            | Non-normative illustrations.                              |
| Exclusions          | Concepts intentionally not covered by the term.           |

# Part III - Upper ontology and canonical entities

## 10. Root entities

| **Class ID**               | **Definition**                                                          |
|----------------------------|-------------------------------------------------------------------------|
| aidcf:Entity               | Root of all addressable objects.                                        |
| aidcf:CapabilityEntity     | An intended ability and its bounded implementation.                     |
| aidcf:OutcomeEntity        | A required or observed result.                                          |
| aidcf:InfrastructureEntity | A system, asset, component, interface, location or resource.            |
| aidcf:ConditionEntity      | A state, constraint, assumption, limit or environmental condition.      |
| aidcf:AdverseEntity        | A threat, hazard, initiating event, cause, failure mode or consequence. |
| aidcf:AssuranceEntity      | A safeguard, control, assertion, evidence, test, finding or decision.   |
| aidcf:PartyEntity          | An organisation, actor, role, team or supplier.                         |
| aidcf:TemporalEntity       | A lifecycle stage, timestamp, validity interval or change event.        |

## 11. Canonical class definitions

| **Preferred term**    | **Canonical definition**                                                                                   |
|-----------------------|------------------------------------------------------------------------------------------------------------|
| Capability            | An intended operational ability supported by infrastructure.                                               |
| Capability Instance   | A specific deployment bounded by ownership, location, architecture, capacity, criticality and obligations. |
| Service Outcome       | A measurable or assessable result required from a Capability Instance.                                     |
| Required Function     | A function whose loss or degradation would materially affect a Service Outcome (formerly "Required Function"). |
| Assessment Boundary   | The declared inclusion perimeter for direct assessment.                                                    |
| Operating Envelope    | The bounded conditions under which a capability or system is intended to operate.                          |
| Infrastructure System | A coordinated set of assets and interfaces providing one or more functions.                                |
| Asset Instance        | An identifiable real-world item, service, person, procedure or resource.                                   |
| Component             | A constituent part of an asset or system represented where material.                                       |
| Interface             | A defined point or mechanism of exchange between entities.                                                 |
| Connection            | A realised physical, logical, hydraulic, electrical, thermal or organisational link.                       |
| Resource              | Consumable or constrained input required for operation.                                                    |
| Location              | A geographic, site, building, zone, room, row, rack or logical placement.                                  |
| Dependency            | A reliance by one entity upon another entity, resource, condition or decision.                             |
| Fault Domain          | A set of entities expected to be affected by a common failure.                                             |
| Redundancy Group      | Assets or paths deliberately arranged to preserve a function.                                              |
| Safeguard             | A real-world measure intended to anticipate, prevent, detect, contain, respond, recover or adapt.          |
| Evidence Object       | A record or observation used to support, challenge or qualify an assertion (Part XV).                      |
| Actor                 | A human or machine participant with a relevant role.                                                       |
| Organisation          | A legally or operationally recognised party.                                                               |
| Role                  | A named set of responsibilities and authorities.                                                           |
| Operating State       | A defined condition of operation.                                                                          |
| Change Event          | An approved, observed or unapproved modification affecting the represented system.                         |

## 12. Mandatory distinctions

| **Do not collapse**                                  | **Reason**                                                                     |
|------------------------------------------------------|--------------------------------------------------------------------------------|
| Capability / Capability Instance                     | A generic ability is not the assessed deployment.                              |
| System / Asset / Component                           | Composition and assessment granularity differ.                                 |
| Function / Implementing asset                        | A function can be reallocated or implemented by multiple technologies.         |
| Interface / Dependency                               | An interface enables exchange; a dependency is reliance.                       |
| Connection / Relationship                            | A connection is realised; a relationship may be logical or asserted.           |
| Capacity / Demand / Reserve                          | They answer different questions.                                               |
| Redundancy / Diversity / Independence / Resilience   | Additional paths do not prove common-cause independence or outcome resilience. |
| Designed / Installed / Commissioned / Observed state | Documentation and reality may diverge.                                         |
| Owner / Operator / Maintainer / Risk owner           | Commercial and operational responsibilities differ.                            |
| UNKNOWN / NOT_APPLICABLE / NONCONFORMING / NOT_ASSESSED | Evidence insufficiency is not the same as approved non-applicability, demonstrated failure or absence of assessment. |
| Safeguard / Control                                  | A safeguard is the real-world measure; a control is the assessable requirement in AIDCF-007A evaluated against it. |
| Evidence status / Confidence                         | Evidence status describes a record's support (§53); confidence (CONF-0 to CONF-4) is the assessor's bounded belief in a claim. |

# Part IV - Capability, outcome, boundary and lifecycle model

## 13. Capability hierarchy

| **Level** | **Entity**                   | **Illustration**                                                                      |
|-----------|------------------------------|---------------------------------------------------------------------------------------|
| 1         | Capability family            | AI training; inference; fine-tuning; HPC simulation; shared accelerator service.      |
| 2         | Capability type              | Large-scale distributed training; low-latency inference; batch inference.             |
| 3         | Capability Instance          | A named deployment at a defined site with a declared architecture.                    |
| 4         | Service Outcome              | Availability, throughput, completion, latency, integrity or recovery outcome.         |
| 5         | Required Function            | Heat removal, power continuity, scheduling, checkpoint persistence, fabric transport. |
| 6         | Supporting system and assets | Cooling loop, UPS path, compute cluster, storage system, network fabric.              |

## 14. Capability Instance minimum record

| **Property**         | **Requirement**                                                                         |
|----------------------|-----------------------------------------------------------------------------------------|
| capabilityInstanceId | Globally or organisationally unique and immutable.                                      |
| name                 | Human-readable identifier.                                                              |
| capabilityType       | Controlled vocabulary value.                                                            |
| owner                | Accountable organisation or role.                                                       |
| locations            | Sites and zones in which it is instantiated.                                            |
| lifecycleStage       | PLAN, DESIGN, BUILD, COMMISSION, OPERATE, CHANGE or DECOMMISSION (§17).                 |
| serviceOutcomes      | One or more outcome records.                                                            |
| criticality          | Declared and justified criticality.                                                     |
| assessmentBoundary   | Included systems and explicit exclusions.                                               |
| operatingEnvelope    | Load, environmental, capacity, duration and state constraints.                          |
| architectureBaseline | Approved design or configuration reference.                                             |
| effectivePeriod      | Start/end or point-in-time applicability.                                               |
| evidenceStatus       | CONFIRMED, PARTIALLY_CONFIRMED, ASSERTED, INFERRED, CONFLICTING, STALE or UNKNOWN (§53). |

## 15. Service Outcome taxonomy

| **Outcome family** | **Examples of assessable properties**                                                   |
|--------------------|-----------------------------------------------------------------------------------------|
| Availability       | Required service continuity; tolerated interruption; degraded-mode availability.        |
| Capacity           | Minimum usable accelerator, storage, network, power and cooling capacity.               |
| Performance        | Throughput, latency, job completion, checkpoint duration, fabric efficiency.            |
| Integrity          | Correct configuration, artifact integrity, data-path integrity and state consistency.   |
| Isolation          | Tenant, cluster, management, physical and fault-domain separation.                      |
| Recoverability     | Recovery objective, restart conditions, restoration sequence and validation.            |
| Safety             | Safe thermal, electrical, fire, structural and human operating conditions.              |
| Efficiency         | Resource performance within defined resilience constraints.                             |
| Sovereignty        | Declared location, operational control, supply, maintenance and dependency constraints. |
| Observability      | Minimum telemetry, alarm and diagnostic visibility needed to operate and assure.        |

## 16. Boundary model

> **IOT-REQ-007** An Assessment Boundary shall identify included Capability Instances, sites, zones, systems, assets, interfaces, lifecycle stages and time horizon.
>
> **IOT-REQ-008** Every exclusion shall identify rationale, owner, residual dependency and effect on confidence.
>
> **IOT-REQ-009** External services shall be represented through boundary-crossing relationships and shall not be treated as inherently reliable.

## 17. Lifecycle stages

| **Code**     | **Stage**                                 | **Ontology emphasis**                                                                                                                       |
|--------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| PLAN         | Concept                                   | Capability intent, candidate site, constraints, assumptions and target outcomes.                                                            |
| DESIGN       | Design                                    | Required Functions, systems, architecture, capacity, fault domains and interfaces.                                                          |
| BUILD        | Construction                              | Asset instances, installation state, deviations and provenance.                                                                             |
| COMMISSION   | Commissioning and operational readiness   | Tests, observations, results, outstanding defects, accepted limitations; procedures, personnel, spares, monitoring and transfer of authority. |
| OPERATE      | Operation                                 | Current state, telemetry, maintenance, incidents, evidence and drift.                                                                       |
| CHANGE       | Change                                    | Impact, configuration transition, temporary states, evidence and revalidation.                                                              |
| DECOMMISSION | Decommissioning                           | Isolation, removal, sanitisation, residual hazards and record retention.                                                                    |

The codes are the canonical lifecycle stages of AIDCF-002. v1.0 listed operational readiness as a separate stage; it is the closing part of COMMISSION.

# Part V - Fifteen-domain infrastructure taxonomy

## 18. Taxonomy rules

> **IOT-REQ-010** Domain assignment shall indicate the primary classification only; cross-domain relationships shall remain explicit.
>
> **IOT-REQ-011** Every class in Appendix A shall carry exactly one primary domain code from the fifteen AIDCF domain codes of AIDCF-007A, or the tag Upper for cross-domain upper-ontology classes, and may carry secondary codes where controls in another domain routinely assess the class.
>
> **IOT-REQ-012** A domain code on a class shall not be read as restricting which AIDCF-007A controls may reference the class; controls declare the classes they assess through their ontologyClasses attribute.
>
> **IOT-REQ-013** Technology-specific subclasses shall inherit canonical properties from vendor-neutral parent classes.
>
> **IOT-REQ-014** A taxonomy branch shall be extended only where the distinction changes assessment, dependency, evidence, failure or assurance meaning.

## 19. Domain index

The taxonomy uses the fifteen domain codes of AIDCF-007A. The superseded eight-domain model is mapped to these codes in AIDCF-002 Part X; it is not used in this standard.

| **Code** | **Domain** | **AIDCF-007A families** | **Described in** |
|----------|------------|-------------------------|------------------|
| GOV | Governance, Accountability and Assurance Direction | GOV-01 to GOV-06 (MCF-GOV-001 to MCF-GOV-024) | §20.1 |
| CAP | AI Capability, Service Outcome and Demand Management | CAP-01 to CAP-06 (MCF-CAP-001 to MCF-CAP-024) | §20.2 |
| DEP | Dependency, Concentration and External Reliance Management | DEP-01 to DEP-06 (MCF-DEP-001 to MCF-DEP-024) | §20.3 |
| PHY | Physical Site, Building and Security Infrastructure | PHY-01 to PHY-06 (MCF-PHY-001 to MCF-PHY-024) | §21 |
| POW | Electrical Power Infrastructure and Energy Continuity | POW-01 to POW-06 (MCF-POW-001 to MCF-POW-024) | §22 |
| THM | Cooling, Thermal and Fluid Infrastructure | THM-01 to THM-06 (MCF-THM-001 to MCF-THM-024) | §23 |
| ENV | Environmental and Resource Performance | ENV-01 to ENV-06 (MCF-ENV-001 to MCF-ENV-024) | §24 |
| CMP | AI Compute Infrastructure | CMP-01 to CMP-06 (MCF-CMP-001 to MCF-CMP-024) | §25.1 |
| STO | AI Storage and Data Infrastructure | STO-01 to STO-06 (MCF-STO-001 to MCF-STO-024) | §25.2 |
| NET | AI Network and Interconnect Architecture | NET-01 to NET-06 (MCF-NET-001 to MCF-NET-024) | §25.3 |
| OPS | Building Operations and Service Management | OPS-01 to OPS-06 (MCF-OPS-001 to MCF-OPS-024) | §26.1 |
| RES | Resilience, Continuity and Recovery | RES-01 to RES-06 (MCF-RES-001 to MCF-RES-024) | §26.2 |
| SUP | Supply Chain, OEM and Ecosystem Assurance | SUP-01 to SUP-06 (MCF-SUP-001 to MCF-SUP-024) | §26.3 |
| SEC | Digital, OT and Control-Plane Security | SEC-01 to SEC-06 (MCF-SEC-001 to MCF-SEC-024) | §26.4 |
| EVA | Evidence, Assessment and Assurance Management | EVA-01 to EVA-06 (MCF-EVA-001 to MCF-EVA-024) | §26.5 |

## 20. Direction and definition domains (GOV, CAP, DEP)

### 20.1 GOV Governance, Accountability and Assurance Direction

GOV classes represent the authority structure behind assurance: who may approve, delegate, accept risk and grant exceptions. They are the objects to which AIDCF-007A GOV-01 to GOV-06 controls and gate CG-13 attach. Individual roles and organisations use the upper classes Role and Organisation (§11).

| **Taxonomy family**       | **Illustrative subclasses**                                                       |
|---------------------------|-----------------------------------------------------------------------------------|
| Governance and authority  | Operating Model, Delegation, Approval Authority, Escalation Path, Risk Acceptance |
| Obligations and baselines | Policy, Technical Standard Baseline, Exception Record, Contractual Obligation     |

### 20.2 CAP AI Capability, Service Outcome and Demand Management

CAP classes hold the capability, demand and engineering-baseline records against which every other domain is assessed. The Capability Instance, Service Outcome, Required Function and Operating Envelope themselves are upper classes (§11, Part IV) tagged CAP in Appendix A. Engineering records sit here because they define design intent (CAP-06 design-to-operation traceability); each also carries the code of the engineering domain it documents.

| **Taxonomy family**              | **Illustrative subclasses**                                                                                          |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Capability and demand records    | Capability Register, Demand Profile, Load Step Profile, Growth Forecast                                              |
| Engineering baseline and records | Design Basis, Single-Line Diagram, P&ID, As-Built Drawing, Engineering Study, Commissioning Script, Deviation Record |

### 20.3 DEP Dependency, Concentration and External Reliance Management

DEP classes make reliance across the assessment boundary representable. The Dependency and Assessment Boundary classes are upper classes (§11, Part VIII); the classes below represent the external services and boundary crossings that DEP-03 and DEP-05 controls examine.

| **Taxonomy family**           | **Illustrative subclasses**                                      |
|-------------------------------|------------------------------------------------------------------|
| Boundary and external service | External Service, Boundary Crossing, Service Interface Agreement |

## 21. PHY Physical Site, Building and Security Infrastructure

PHY covers the site, the building fabric and structure that carries AI equipment, physical security, and fire and life-safety systems. Civil and structural and fire classes were classified under facilities engineering in v1.0.

| **Taxonomy family**          | **Illustrative subclasses**                                                                                                                          |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Site and external perimeter  | Site, Campus, Property Boundary, Perimeter Barrier, Vehicle Barrier, Gate, Guard Post, External Approach, Standoff Zone                              |
| Building and internal zoning | Building, Floor, Data Hall, Room, Cage, Suite, Row, Rack, Cabinet, Security Zone, Restricted Area, Loading Area, Staging Area                        |
| Civil and structural         | Foundation, Floor Slab, Raised Floor, Roof, Wall, Ceiling, Rack Anchorage, Seismic Restraint, Load-Bearing Element                                   |
| Entry and identity control   | Access Point, Turnstile, Mantrap, Door, Lock, Credential Reader, Biometric Reader, Visitor System, Key System                                        |
| Detection and surveillance   | Camera, Video Management System, Intrusion Sensor, Door Contact, Motion Sensor, Security Alarm, Intercom                                             |
| Asset movement and custody   | Loading Bay, Goods Lift, Screening Point, Storage Area, Seal, Chain-of-Custody Record                                                                |
| Physical response            | Security Operations Centre, Guard Force, Response Procedure, Dispatch Channel, Incident Reconstruction Record                                        |
| Fire and life safety         | Detection Zone, Fire Alarm Panel, Suppression Zone, Suppression Agent System, Sprinkler System, Smoke Control, Emergency Egress, Emergency Power Off |

## 22. POW Electrical Power Infrastructure and Energy Continuity

POW covers the electrical path from utility connection to the rack power shelf, including generation, energy storage, protection and electrical monitoring.

| **Taxonomy family**                         | **Illustrative subclasses**                                                                                                                                                 |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Utility and grid interface                  | Incoming Supply, Utility Feed, Grid Connection, Substation                                                                                                                  |
| Generation and fuel                         | On-Site Generation, Generator, Fuel Tank, Fuel System, Starting System, Exhaust System                                                                                      |
| Conversion, energy storage and distribution | Transformer, Switchgear, MV Switchgear, LV Switchgear, Transfer Scheme, Static Transfer Switch, UPS, Battery, Energy Storage, Busway, PDU, RPP, Rack PDU, Power Supply Unit |
| Protection, earthing and power quality      | Protection Relay, Protection Device, Relay, Earthing System, Grounding, Lightning Protection, Harmonic Filter, Surge Protection                                             |
| Electrical monitoring                       | EPMS, Meter, Power Quality Monitor                                                                                                                                          |

## 23. THM Cooling, Thermal and Fluid Infrastructure

THM covers the heat path from the accelerator package to heat rejection: heat capture, coolant distribution, facility water, air-side systems, fluid quality and leak management.

| **Taxonomy family**              | **Illustrative subclasses**                                                                                                                             |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Air-side and mechanical systems  | Chilled Water Plant, Condenser System, Pump System, Air Distribution, Ventilation, Pressurisation, Air Handler, In-Row Cooler, Rear-Door Heat Exchanger |
| Heat capture at the IT load      | Heat Sink, Cold Plate, Immersion Tank                                                                                                                   |
| Coolant distribution             | CDU, Primary Loop, Secondary Loop, Pump, Manifold, Quick Disconnect, Hose, Pipe, Heat Exchanger                                                         |
| Heat rejection                   | Chiller, Cooling Tower, Dry Cooler, Condenser, Evaporative System, Heat-Reuse Interface                                                                 |
| Fluid, water and leak management | Water Source, Pipework, Valve, Drain, Sump, Drainage, Leak Detection Zone, Water Treatment System                                                       |
| Thermal and leak monitoring      | Temperature Sensor, Humidity Sensor, Flow Sensor, Pressure Sensor, Leak Sensor, Coolant Quality Sensor, Thermal Camera                                  |

## 24. ENV Environmental and Resource Performance

ENV classes are resources, conditions, indicators and obligations rather than equipment. They are used to qualify capacity assertions (§41), operating envelopes and environmental claims.

| **Taxonomy family**             | **Illustrative subclasses**                                                                                    |
|---------------------------------|----------------------------------------------------------------------------------------------------------------|
| Energy resources                | Grid Electricity, Renewable Electricity, On-Site Energy, Stored Energy, Fuel                                   |
| Water resources                 | Potable Water, Process Water, Reclaimed Water, Cooling Water, Discharge Water                                  |
| Environmental conditions        | Ambient Temperature, Humidity, Air Quality, Particulate Level, Noise, Vibration, Flood Exposure, Heat Stress   |
| Material and chemical resources | Refrigerant, Coolant, Fire Suppressant, Battery Chemistry, Hazardous Material                                  |
| Performance indicators          | PUE Record, WUE Record, CUE Record, Energy Reuse Record, Cooling Efficiency Record, Compute Utilisation Record |
| Environmental obligations       | Permit, Reporting Requirement, Emission Limit, Water Limit, Waste Requirement, Environmental Commitment        |

## 25. AI infrastructure domains (CMP, STO, NET)

### 25.1 CMP AI Compute Infrastructure

CMP covers accelerator hardware, rack-scale systems, clusters and the firmware and management software that make them usable. Vendor-specific subclasses (for example NVLink Domain, Kubernetes Cluster) are specialisations of their vendor-neutral parents (Scale-Up Domain, Orchestrator) per IOT-REQ-013.

| **Taxonomy family**     | **Illustrative subclasses**                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Accelerated compute     | Accelerator, GPU, AI ASIC, Compute Node, GPU Baseboard, CPU, Memory, DPU, NIC                                                |
| Rack-scale systems      | Compute Tray, Rack-Scale System, Scale-Up Domain, NVLink Domain, Enclosure, Backplane, Power Shelf, Rack Controller          |
| Cluster systems         | Compute Cluster, Cluster Partition, Node Pool, Head Node, Login Node, Management Node, Provisioning Node                     |
| Management and firmware | BMC, Firmware, BIOS, Driver, Cluster Manager, Provisioning Service, Scheduler, Orchestrator                                  |
| Workload infrastructure | Queue, Scheduler Partition, Reservation, Container Runtime, Kubernetes Cluster, Job Scheduler, Checkpoint Agent              |
| Compute observability   | GPU Telemetry, Node Telemetry, Health Service, Performance Counter, Error Counter                                            |
| Compute lifecycle       | Golden Image, Firmware Baseline, Compatibility Matrix, Hardware Support Contract, RMA Process, Secure Decommissioning Record |

### 25.2 STO AI Storage and Data Infrastructure

STO covers storage systems, data-path services and the repositories that hold datasets, models and checkpoints, including protection copies used for recovery.

| **Taxonomy family**       | **Illustrative subclasses**                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------------------------|
| Storage systems           | Parallel File System, Scale-Out NAS, Object Storage, Block Storage, Local NVMe, Burst Buffer, Archive Storage |
| Storage nodes and media   | Storage Node, Metadata Server, Object Storage Node, Controller, SSD, HDD, Tape, NVRAM                         |
| Data-path services        | Namespace, Metadata Service, Data Mover, Cache, Data-Path Gateway, Client Driver, Mount Service               |
| AI artifact services      | Dataset Repository, Model Repository, Checkpoint Repository, Feature Store, Artifact Registry                 |
| Protection and recovery   | Snapshot, Replica, Backup Copy, Erasure Coding Group, Recovery Copy, Immutable Copy                           |
| Storage management        | Storage Manager, Capacity Manager, Tiering Policy, Retention Policy, Integrity Scanner, Telemetry Service     |
| Data logistics interfaces | Ingestion Interface, Export Interface, Data Transfer Node, WAN Transfer Service, Data Staging Area            |

### 25.3 NET AI Network and Interconnect Architecture

NET covers scale-up and scale-out fabrics, storage, frontend and management networks, core network services and physical connectivity.

| **Taxonomy family**            | **Illustrative subclasses**                                                                                    |
|--------------------------------|----------------------------------------------------------------------------------------------------------------|
| Scale-up interconnect          | Scale-Up Fabric, Switch Fabric, Interconnect Link, Topology Domain                                             |
| Scale-out compute fabric       | InfiniBand Fabric, Ethernet AI Fabric, RoCE Fabric, Compute Leaf, Compute Spine, Fabric Manager                |
| Storage fabric                 | Storage Network, Storage Leaf, Storage Spine, SAN Fabric, Storage Gateway                                      |
| Frontend and service network   | Frontend Network, Load Balancer, Service Gateway, Edge Router, Firewall, API Network                           |
| Management and control network | Management Network, Out-of-Band Network, Console Server, Management Switch, Jump Service                       |
| Timing and core services       | Time Service, DNS Service, DHCP Service, IPAM Service, Certificate Service, Authentication Service             |
| Physical connectivity          | Cable, Optical Fibre, Copper Link, Transceiver, Patch Panel, Meet-Me Room, Cross-Connect                       |
| Network observability          | Flow Telemetry, Fabric Telemetry, Packet Capture Service, Network Controller, Congestion Monitor, Path Monitor |

## 26. Operation, resilience and assurance domains (OPS, RES, SUP, SEC, EVA)

### 26.1 OPS Building Operations and Service Management

OPS covers how the facility is run: work control, maintenance, staffing, alarms and incidents, configuration records, and the facility monitoring and control systems operated day to day. Facility control systems are also industrial automation and control systems in the sense of Part XVI and carry SEC as a secondary code.

| **Taxonomy family**             | **Illustrative subclasses**                                                                                             |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Work control                    | Procedure, Method Statement, Permit to Work, Lockout Tagout, Maintenance Window, Change Record, Temporary Configuration |
| Maintenance and reliability     | Maintenance Plan, Work Order, Condition Monitoring, Inspection, Calibration, Spare Part, Obsolescence Record            |
| Staffing and competence         | Shift, Roster, Competency Record, Authorisation, Training Record, Contractor, Subject Matter Expert                     |
| Alarm and incident              | Alarm, Incident, Event Log, Post-Incident Review                                                                        |
| Configuration and documentation | Configuration Baseline, Asset Register, Drawing Register, Procedure Register, Revision, Document Custodian              |
| Facility monitoring and control | BMS, SCADA, PLC, RTU, Sensor, Actuator, Control-System Gateway, Historian, Alarm Console                                |

### 26.2 RES Resilience, Continuity and Recovery

RES classes represent continuity and recovery arrangements. Fault Domain and Redundancy Group are upper classes (§11, Part IX) tagged RES; protection copies in STO and golden images in CMP carry RES as a secondary code.

| **Taxonomy family**               | **Illustrative subclasses**                                                                      |
|-----------------------------------|--------------------------------------------------------------------------------------------------|
| Continuity and emergency response | Emergency Procedure, Crisis Team, Exercise, Continuity Plan, Recovery Plan, Alternative Capacity |

### 26.3 SUP Supply Chain, OEM and Ecosystem Assurance

SUP covers supplier relationships, service obligations and the provenance of hardware, software and firmware. Supplier management classes were classified under building operations in v1.0.

| **Taxonomy family**             | **Illustrative subclasses**                                                                                     |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Supplier and service management | Supplier, Maintenance Contract, Service Level, Remote Support, Escalation Contact, Lead Time, Supply Constraint |
| Provenance and software supply  | Software Release, Signature Record, Software Bill of Materials, Component Provenance Record                     |

### 26.4 SEC Digital, OT and Control-Plane Security

SEC covers identity, privileged and remote access, security monitoring, and authority for automated or AI-enabled action over infrastructure. Industrial control-system zones, conduits and security levels are specified in Part XVI.

| **Taxonomy family**              | **Illustrative subclasses**                                                                                                |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Identity and privileged access   | Identity Provider, Human Identity, Machine Identity, Privileged Access Service, Break-Glass Account, Remote Access Gateway |
| Security monitoring and response | Security Telemetry Service, Security Incident, Vulnerability Record                                                        |
| Automated and AI-enabled action  | Automation Agent, Command Allowlist, Approval Workflow                                                                     |

### 26.5 EVA Evidence, Assessment and Assurance Management

EVA has no infrastructure taxonomy of its own: its classes are the assurance-chain classes of Part XV (Control Domain to Reassessment Trigger), tagged EVA in Appendix A.

# Part VI - Cross-cutting classification facets

## 27. Facet model

Domain classification alone is insufficient. Every material entity may also be classified through orthogonal facets that support analysis without creating duplicate classes.

| **Facet**                 | **Controlled values / meaning**                                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Criticality               | Critical, High, Moderate, Low, Unclassified, UNKNOWN.                                                                                           |
| Lifecycle status          | Planned, designed, procured, installed, commissioned, operational, standby, degraded, under maintenance, bypassed, failed, recovering, retired. |
| Physicality               | Physical, logical, human, procedural, contractual, environmental, informational.                                                                |
| Boundary position         | Internal, boundary-crossing, external, excluded-but-dependent, UNKNOWN.                                                                         |
| Tenancy                   | Dedicated, shared, multi-tenant, pooled, reserved, burst, UNKNOWN.                                                                              |
| Control authority         | Direct, delegated, contractual, advisory, none, UNKNOWN.                                                                                        |
| Evidence status           | CONFIRMED, PARTIALLY_CONFIRMED, ASSERTED, INFERRED, CONFLICTING, STALE, UNKNOWN (§53).                                                          |
| Replaceability            | Immediate, stocked spare, contractually replaceable, long-lead, irreplaceable, UNKNOWN.                                                         |
| Mobility                  | Fixed, relocatable, portable, virtualised, service-based.                                                                                       |
| Exposure                  | Public, campus, building, hall, cage, rack, management plane, isolated, UNKNOWN.                                                                |
| Sovereignty relevance     | Local control, foreign dependency, cross-border support, remote administration, jurisdiction-sensitive, not declared.                           |
| Environmental sensitivity | Temperature, humidity, water quality, vibration, particulate, altitude, electromagnetic, acoustic.                                              |

## 28. Criticality semantics

> **IOT-REQ-015** Criticality shall be assigned in relation to a Capability Instance and Service Outcome, not as an intrinsic universal property of an asset class.
>
> **IOT-REQ-016** Criticality rationale should consider consequence, time sensitivity, substitutability, concentration, recovery complexity, safety, regulatory and strategic significance.

## 29. Classification inheritance

A subclass inherits properties and permitted relationships from its parent unless an approved extension explicitly narrows or adds semantics. Inheritance shall not be used to infer an operational fact about an instance. For example, classifying an asset as a UPS does not establish its capacity, redundancy, condition or effectiveness.

# Part VII - Asset, system, interface and resource model

## 30. System decomposition

| **Construct**         | **Use**                                                     |
|-----------------------|-------------------------------------------------------------|
| Infrastructure System | Group assets that collectively provide a function.          |
| Subsystem             | Represent a meaningful functional subdivision.              |
| Asset Group           | Group similar instances for inventory or analysis.          |
| Functional Group      | Group heterogeneous assets that realise a function.         |
| Redundancy Group      | Represent alternatives designed to preserve a function.     |
| Fault Domain          | Represent common failure exposure.                          |
| Protection Zone       | Represent a security, fire, electrical or thermal boundary. |
| Maintenance Group     | Represent assets taken out of service together.             |
| Capacity Pool         | Represent shared capacity available to consumers.           |

## 31. Interface taxonomy

| **Interface class** | **Examples**                                           | **Minimum properties**                                     |
|---------------------|--------------------------------------------------------|------------------------------------------------------------|
| Electrical          | Supply, feeder, bus, breaker termination               | Voltage, phase, capacity, protection, source, destination. |
| Thermal             | Air or liquid heat transfer point                      | Medium, temperature, flow, pressure, capacity, direction.  |
| Hydraulic           | Coolant or water connection                            | Fluid, pressure, flow, valve/isolation, leak boundary.     |
| Network             | Port, link, VLAN, subnet, fabric endpoint              | Protocol, bandwidth, topology role, path, security zone.   |
| Mechanical          | Mounting, anchoring, ventilation or structural contact | Load, tolerance, connection, isolation.                    |
| Control             | Sensor, command, alarm or automation interface         | Signal, authority, fail state, protocol, authentication.   |
| Human/procedural    | Handover, approval, escalation or work interface       | Role, trigger, response objective, record.                 |
| Contractual/service | Utility, supplier or maintenance service boundary      | Provider, service level, capacity, escalation, evidence.   |

## 32. Resource taxonomy

| **Resource**                  | **Key semantics**                                                          |
|-------------------------------|----------------------------------------------------------------------------|
| Electrical energy             | Source, quality, capacity, duration, carbon attribute, dependency.         |
| Fuel                          | Type, quantity, quality, replenishment, usable duration.                   |
| Cooling capacity              | Heat-removal capacity under defined conditions.                            |
| Water                         | Source, quality, quantity, permitted use and continuity.                   |
| Coolant/refrigerant           | Type, compatibility, quantity, quality and handling constraints.           |
| Space and structural capacity | Area, volume, floor loading, rack loading and access.                      |
| Network bandwidth             | Usable throughput, latency, oversubscription and state.                    |
| Storage capacity              | Usable capacity, performance tier, protection overhead and headroom.       |
| Compute capacity              | Usable accelerator/CPU/memory capacity and allocation.                     |
| Human capacity                | Competence, availability, authorisation and concentration.                 |
| Time                          | Transfer time, autonomy, response time, maintenance window, recovery time. |
| Spares                        | Quantity, compatibility, location, lead time and preservation state.       |

## 33. Minimum asset record

| **Property**       | **Cardinality**                 | **Meaning**                              |
|--------------------|---------------------------------|------------------------------------------|
| assetId            | Required                        | Stable identifier.                       |
| assetClass         | Required                        | Canonical or approved extension class.   |
| name               | Required                        | Human-readable name.                     |
| systemMembership   | Required where applicable       | Parent system(s).                        |
| location           | Required for physical assets    | Placement or service jurisdiction.       |
| owner              | Required                        | Accountable owner or UNKNOWN.            |
| operator           | Required for operational assets | Operator or UNKNOWN.                     |
| maintainer         | Conditional                     | Maintenance party.                       |
| lifecycleStatus    | Required                        | Controlled value.                        |
| criticality        | Required if material            | Capability-specific value and rationale. |
| capacityProperties | Conditional                     | Units and operating conditions.          |
| interfaces         | Conditional                     | Connections and service boundaries.      |
| dependencies       | Required if material            | Direct and known indirect reliances.     |
| faultDomains       | Required if resilience-relevant | One or more fault-domain memberships.    |
| evidenceLinks      | Required for assurance use      | Evidence supporting material attributes. |
| validity           | Required                        | Effective period and observation date.   |
| evidenceStatus     | Required                        | CONFIRMED through UNKNOWN (§53).         |

# Part VIII - Relationship and dependency vocabulary

## 34. Relationship design rules

> **IOT-REQ-017** Every relationship shall identify subject, predicate and object; material relationships shall also identify scope, conditions, provenance, confidence and effective period.
>
> **IOT-REQ-018** Inverse relationships may be generated only where the canonical registry declares an inverse.
>
> **IOT-REQ-019** Symmetric relationships shall not be assumed for directional dependencies.
>
> **IOT-REQ-020** Transitive reasoning shall be applied only to approved predicates and shall not automatically infer engineering sufficiency.
>
> **IOT-REQ-021** Records exchanged between tools shall use the AIDCF-014 §9 relationship types; ontology predicates in this standard that are not AIDCF-014 types shall be exchanged through the mapping in Appendix B and shall not be emitted as new exchange types.

## 35. Core structural relationships

| **Predicate**   | **Subject**     | **Object**         | **Logic**                 | **Inverse**        | **Meaning**                   |
|-----------------|-----------------|--------------------|---------------------------|--------------------|-------------------------------|
| PART_OF           | Entity              | Entity            | Transitive                | HAS_PART           | Composition.                                   |
| CONTAINS          | Location/System     | Entity            | Transitive                | LOCATED_IN/PART_OF | Containment.                                   |
| LOCATED_IN        | Physical Entity     | Location          | Transitive                | CONTAINS           | Physical placement.                            |
| MEMBER_OF         | Entity              | Group             | No                        | HAS_MEMBER         | Group membership.                              |
| HAS_OUTCOME       | CapabilityInstance  | ServiceOutcome    | No                        | —                  | Capability requires the outcome.               |
| REQUIRES_FUNCTION | ServiceOutcome      | RequiredFunction  | No                        | —                  | Outcome depends on the function.               |
| IMPLEMENTED_BY    | RequiredFunction    | System/Asset      | No                        | IMPLEMENTS         | Function is realised by the system or asset.   |
| INTERFACES_WITH   | Entity              | Entity            | Symmetric                 | INTERFACES_WITH    | Defined exchange boundary.                     |
| CONNECTS_TO       | Entity              | Entity            | Symmetric unless directed | CONNECTS_TO        | Realised connection.                           |
| ROUTES_THROUGH    | Flow/Service        | Entity            | No                        | CARRIES            | Path relationship.                             |

v1.0 used SUPPORTS for "entity contributes to capability or outcome". That use is withdrawn: SUPPORTS is reserved for evidence supporting an assertion (AIDCF-014 §9). Contribution to an outcome is expressed as HAS_OUTCOME → REQUIRES_FUNCTION → IMPLEMENTED_BY. IMPLEMENTS is retained only as the inverse of IMPLEMENTED_BY, and CONNECTED_TO is renamed CONNECTS_TO.

## 36. Functional dependency relationships

| **Predicate**    | **Subject**         | **Object**                 | **Meaning**                        |
|------------------|---------------------|----------------------------|------------------------------------|
| DEPENDS_ON       | Consumer entity     | Provider/entity/condition  | General reliance.                  |
| POWERED_BY       | Load/system         | Electrical source/path     | Electrical reliance.               |
| COOLED_BY        | Heat source/system  | Cooling system/path        | Thermal reliance.                  |
| SUPPLIED_BY      | Consumer            | Provider/resource          | Resource or service supply.        |
| CONTROLLED_BY    | Asset/system        | Controller/actor           | Operational or automated control.  |
| MONITORED_BY     | Entity              | Monitoring entity          | Visibility and detection reliance. |
| PROTECTED_BY     | Entity              | Safeguard                  | Protective relationship.           |
| AUTHENTICATED_BY | Entity/service      | Identity service           | Identity reliance.                 |
| TIMED_BY         | Entity/service      | Time source                | Timing reliance.                   |
| CONFIGURED_BY    | Entity              | Configuration source/actor | Configuration reliance.            |
| RECOVERS_THROUGH | Entity/capability   | Recovery asset/process     | Restoration reliance.              |
| MAINTAINED_BY    | Entity              | Actor/organisation         | Maintenance reliance.              |
| OPERATED_BY      | Entity/system       | Actor/organisation         | Operational responsibility.        |
| EVIDENCED_BY     | Assertion/entity    | Evidence object            | Evidence support.                  |
| TESTED_BY        | Assertion/safeguard | Test record                | Validation link (exchanged as ASSESSED_BY with method TEST). |

## 37. Dependency record schema

| **Field**           | **Required**      | **Description**                                                         |
|---------------------|-------------------|-------------------------------------------------------------------------|
| dependencyId        | Yes               | Stable relationship identifier.                                         |
| consumer            | Yes               | Entity reliant on another.                                              |
| provider            | Yes or UNKNOWN    | Entity, resource or condition relied upon.                              |
| dependencyType      | Yes               | Electrical, thermal, hydraulic, network, control, human, supplier, etc. |
| strength            | Yes               | Absolute, material, conditional, supporting, recovery-only or UNKNOWN.  |
| direction           | Yes               | Provider to consumer effect direction.                                  |
| applicableStates    | Yes               | Operating states in which reliance is material.                         |
| capacityRequirement | Conditional       | Required quantity, unit, duration and quality.                          |
| substitutability    | Conditional       | Alternative provider or workaround.                                     |
| transferMechanism   | Conditional       | Automatic, manual, procedural or none.                                  |
| commonDependencies  | Conditional       | Shared providers or causes.                                             |
| owner               | Yes or UNKNOWN    | Responsible party for the dependency.                                   |
| evidence            | Yes for assurance | Supporting documents, observations or tests.                            |
| evidenceStatus      | Yes               | Evidence status (§53).                                                  |
| confidence          | Yes for assurance | CONF-0 to CONF-4 with rationale, and CONFLICTING/STALE flags where set. |
| validity            | Yes               | Effective period and validation date.                                   |

## 38. Dependency classes

| **Class**                | **Definition**                                                      | **Examples**                                        |
|--------------------------|---------------------------------------------------------------------|-----------------------------------------------------|
| Electrical               | Reliance on electrical supply, quality, protection or distribution. | GPU rack -\> rack PDU -\> busway -\> UPS path.      |
| Thermal                  | Reliance on heat capture, transport or rejection.                   | GPU tray -\> cold plate -\> secondary loop -\> CDU. |
| Hydraulic                | Reliance on fluid path, pressure, flow or quality.                  | CDU -\> facility water loop.                        |
| Mechanical/structural    | Reliance on physical support, airflow or mechanical function.       | Rack-scale system -\> floor loading and anchoring.  |
| Network                  | Reliance on connectivity, bandwidth, route or fabric service.       | Compute node -\> scale-out fabric.                  |
| Control-system           | Reliance on sensors, automation, logic or command.                  | Cooling valve -\> PLC -\> sensor chain.             |
| Timing/information       | Reliance on time, name, address, telemetry or configuration.        | Cluster service -\> DNS/NTP/IPAM.                   |
| Human/procedural         | Reliance on competent action, approval, handover or procedure.      | Generator response -\> operator and escalation.     |
| Supplier/contractual     | Reliance on external service, warranty, spares or service level.    | Storage recovery -\> OEM support.                   |
| Geographic/environmental | Reliance on location, ambient or external condition.                | Heat rejection -\> outdoor wet-bulb condition.      |
| Capacity                 | Reliance on sufficient headroom or reserve.                         | Cluster expansion -\> resilient power headroom.     |
| Recovery-only            | Reliance primarily during restoration.                              | Compute rebuild -\> golden image repository.        |

## 39. Common-mode and concentration relationships

> **SHARES_DEPENDENCY_WITH** Two entities rely on the same material provider.
>
> **SHARES_FAULT_DOMAIN_WITH** Two entities are exposed to a declared common fault domain (formerly IN_SAME_FAULT_DOMAIN_AS).
>
> **DIVERSE_FROM** Two implementations differ in a declared material characteristic.
>
> **INDEPENDENT_OF** An evidence-backed claim of relevant independence under stated conditions.
>
> **REDUNDANT_WITH** An alternative intended to preserve a function.
>
> **CONCENTRATES** An entity aggregates capability, capacity or dependency consequence.
>
> **SINGLE_POINT_FOR** Failure of an entity defeats a required outcome without effective alternative.
>
> **ISOLATED_FROM** A tested or designed separation relevant to a declared hazard or threat.

# Part IX - Capacity, redundancy, fault-domain and resilience semantics

## 40. Capacity model

| **Capacity term**     | **Canonical meaning**                                                   |
|-----------------------|-------------------------------------------------------------------------|
| Nameplate capacity    | Manufacturer or design rating before contextual adjustment.             |
| Installed capacity    | Capacity physically present.                                            |
| Commissioned capacity | Capacity demonstrated within commissioning scope.                       |
| Available capacity    | Capacity currently usable after condition, derating and outage.         |
| Committed capacity    | Capacity allocated, contracted or reserved.                             |
| Demand                | Observed or forecast requirement under stated condition.                |
| Headroom              | Available capacity less demand and commitments, subject to constraints. |
| Resilient capacity    | Capacity available during a defined adverse or maintenance condition.   |
| Stranded capacity     | Installed capacity unusable because another dependency constrains it.   |
| Transient capacity    | Capacity supportable for a limited duration.                            |
| Recovery capacity     | Capacity available while restoration is underway.                       |
| UNKNOWN capacity      | Capacity cannot be established with sufficient evidence.                |

## 41. Capacity assertion schema

> **IOT-REQ-022** A capacity value shall identify metric, unit, entity, operating state, environmental conditions, duration, derating assumptions, evidence date and confidence.
>
> **IOT-REQ-023** Nameplate, installed, commissioned, available, committed, resilient and uncommitted capacity shall not be used interchangeably.
>
> **IOT-REQ-024** A cross-domain capacity claim shall identify the limiting dependency and any stranded capacity.

## 42. Redundancy semantics

| **Concept**                  | **Required elements**                                                                                                   |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Redundancy claim             | Protected function, alternatives, required capacity, failure condition, transfer mechanism, transfer time and evidence. |
| Diversity claim              | Characteristic in which alternatives materially differ, such as route, technology, supplier or control.                 |
| Independence claim           | Relevant common causes considered, shared dependencies identified, applicable states and evidence.                      |
| Maintainability claim        | Function sustained while defined assets are removed from service safely.                                                |
| Concurrent-maintenance claim | Specific maintenance scenario, capacity, operational restrictions and evidence.                                         |
| Fault tolerance claim        | Failure set, containment boundary, residual outcome and evidence.                                                       |
| Graceful degradation         | Priority, reduced outcome, trigger, control mechanism and recovery path.                                                |

## 43. Fault-domain taxonomy

- Physical: room, rack, route, fire zone, flood zone or structural area.

- Electrical: utility source, transformer, switchboard, UPS path, busway or protection zone.

- Thermal: air zone, coolant loop, CDU, chiller train, heat-rejection path.

- Network: switch, plane, fabric, route, controller or failure group.

- Storage: node group, enclosure, metadata service, protection set or site.

- Compute: node, tray, rack, scale-up domain, cluster partition or scheduler domain.

- Control-system: sensor chain, controller, automation logic, communication path or management platform.

- Software/configuration: firmware baseline, driver, image, policy or configuration source.

- Human/operational: team, shift, procedure, supplier or authority concentration.

- External: utility, carrier, water source, fuel supply, vendor or geographic region.

## 44. Resilience claim record

| **Property**         | **Meaning**                                                       |
|----------------------|-------------------------------------------------------------------|
| subject              | Capability, outcome, function or system.                          |
| adverseCondition     | Failure, threat, hazard, maintenance or compound scenario.        |
| initialState         | State before the event.                                           |
| requiredOutcome      | Minimum acceptable service result.                                |
| permittedDegradation | Allowed reduction and duration.                                   |
| safeguards           | Measures expected to act.                                         |
| responseSequence     | Detection, decision, transfer, containment and recovery sequence. |
| recoveryObjective    | Target restoration condition.                                     |
| evidence             | Tests, events, analysis or observations.                          |
| limitations          | Uncovered states, assumptions and constraints.                    |
| confidence           | Supported conclusion and rationale.                               |

# Part X - Operating state, temporal state and change semantics

## 45. Operating state taxonomy

| **Code**    | **Definition**                                                                                   |
|-------------|--------------------------------------------------------------------------------------------------|
| NORMAL      | Approved architecture operates within declared envelope; no material planned impairment.         |
| DEGRADED    | One or more functions, safeguards, paths or reserves are impaired while some capability remains. |
| MAINTENANCE | A planned intervention changes availability, configuration, staffing or safeguards.              |
| EMERGENCY   | Exceptional condition requiring urgent protective action.                                        |
| RECOVERY    | Controlled restoration and validation after disruption.                                          |
| TRANSITION  | Movement between architectures, states, locations or control regimes.                            |
| SHUTDOWN    | Intentional cessation with controlled residual dependencies.                                     |
| FAILED      | Required function is not delivered.                                                              |
| UNKNOWN     | Current operating state cannot be determined.                                                    |

## 46. State transition model

> **IOT-REQ-025** State transitions shall identify trigger, authority, preconditions, required safeguards, expected duration, monitoring, exit criteria and evidence.
>
> **IOT-REQ-026** Temporary bypass and maintenance configurations shall be represented as explicit states or configuration versions.
>
> **IOT-REQ-027** Assurance claims shall identify the operating states they cover and shall not be generalised to uncovered states.

## 47. Temporal truth

| **Temporal construct** | **Use**                                                        |
|------------------------|----------------------------------------------------------------|
| Observation time       | When a fact was observed.                                      |
| Effective time         | When a fact or relationship applies in the represented system. |
| Record time            | When the information entered the repository.                   |
| Validity interval      | Start and end of applicability.                                |
| Evidence period        | Period covered by evidence.                                    |
| Review date            | When a record was last assessed.                               |
| Expiry date            | When evidence or an assertion is no longer presumed current.   |
| Supersedes             | Links a new record or baseline to the prior one.               |
| Derived from           | Links a conclusion to source records.                          |

## 48. Configuration perspectives

| **Perspective**  | **Meaning**                                                       |
|------------------|-------------------------------------------------------------------|
| Intended         | Approved requirement or design intent.                            |
| Designed         | Documented architecture.                                          |
| Procured         | Contracted or ordered implementation.                             |
| Installed        | Physical or logical implementation present.                       |
| As-built         | Recorded installed configuration.                                 |
| Commissioned     | Configuration subjected to defined acceptance tests.              |
| Observed         | State directly observed or measured.                              |
| Current approved | Authoritative operational baseline.                               |
| Temporary        | Time-bounded deviation or workaround.                             |
| Future           | Planned target state.                                             |
| Retired          | No longer active but retained for history and dependency closure. |

## 49. Change Event schema

| **Field**          | **Description**                                                                                                             |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------|
| changeId           | Stable identifier.                                                                                                          |
| changeType         | Addition, removal, replacement, upgrade, reconfiguration, relocation, capacity change, supplier change or emergency change. |
| affectedEntities   | Assets, systems, interfaces, outcomes and dependencies.                                                                     |
| preState/postState | Configuration and operating state before and after.                                                                         |
| impactAnalysis     | Affected capacity, fault domains, safeguards, evidence and claims.                                                          |
| authority          | Approver and implementer.                                                                                                   |
| plannedWindow      | Applicable schedule if planned.                                                                                             |
| validation         | Required testing and acceptance.                                                                                            |
| rollback           | Restoration path and conditions.                                                                                            |
| assuranceImpact    | Claims invalidated, limited or requiring reassessment.                                                                      |

# Part XI - Responsibility, evidence, confidence and UNKNOWN semantics

## 50. Responsibility model

| **Relationship** | **Meaning**                                          | **AIDCF-014 exchange form**                                    |
|------------------|------------------------------------------------------|----------------------------------------------------------------|
| OWNS             | Legal, financial or accountable ownership.           | GOVERNED_BY (inverse) with role = owner                        |
| OPERATES         | Performs routine operation.                          | OPERATED_BY (inverse)                                          |
| CONTROLS         | Holds authority to command or configure.             | CONTROLLED_BY (inverse)                                        |
| MAINTAINS        | Performs inspection, servicing and repair.           | OPERATED_BY (inverse) with role = maintainer                   |
| SUPPLIES         | Provides a resource, product or service.             | DEPENDS_ON or CONSUMES_RESOURCE from the consumer              |
| MONITORS         | Observes state and raises information or alerts.     | MONITORED_BY (inverse)                                         |
| APPROVES         | Authorises design, change, work or decision.         | APPROVED_BY (inverse)                                          |
| ASSURES          | Performs independent or internal assurance activity. | ASSESSED_BY or REVIEWED_BY (inverse)                           |
| ACCEPTS_RISK_FOR | Holds authority to accept residual exposure.         | APPROVED_BY (inverse) on the risk-acceptance record            |
| CUSTODIAN_OF     | Maintains an evidence or information object.         | Custodian attribute of EvidenceObject                          |
| RESPONDS_TO      | Has response responsibility for an event or alarm.   | OPERATED_BY (inverse) with role = responder                    |
| ESCALATES_TO     | Transfers information or decision authority.         | GOVERNED_BY with role = escalation                             |

## 51. Shared-responsibility record

> **IOT-REQ-028** A shared-responsibility allocation shall identify function, assets, lifecycle stages, operating states, responsible party, accountable party, consulted parties, evidence custodian and unresolved gaps.
>
> **IOT-REQ-029** Contractual responsibility shall not be treated as proof of operational capability or control effectiveness.

## 52. Evidence attachment model

| **Evidence relation**  | **Meaning**                                                | **AIDCF-014 exchange form**                         |
|------------------------|------------------------------------------------------------|-----------------------------------------------------|
| SUPPORTS_ASSERTION     | Evidence supports a testable statement.                    | SUPPORTS                                            |
| CHALLENGES_ASSERTION   | Evidence contradicts or weakens a statement.               | CHALLENGES                                          |
| QUALIFIES_ASSERTION    | Evidence limits the scope or conditions of a statement.    | QUALIFIES                                           |
| OBSERVES_ENTITY        | Evidence records the state of an entity.                   | EVIDENCED_BY (inverse, from the entity)             |
| VALIDATES_SAFEGUARD    | Evidence demonstrates a safeguard under stated conditions. | SUPPORTS on the assertion about the safeguard       |
| ESTABLISHES_PROVENANCE | Evidence identifies source, origin or custody.             | Provenance attributes (AIDCF-014 §26)               |
| COVERS_PERIOD          | Evidence applies to a declared period.                     | period attribute                                    |
| COVERS_STATE           | Evidence applies to one or more operating states.          | state attribute                                     |
| CONFLICTS_WITH         | Evidence is inconsistent with another evidence object.     | CHALLENGES between assertions, with CONFLICTING flag |
| SUPERSEDES             | Newer controlled evidence replaces an earlier record.      | SUPERSEDES                                          |

## 53. Evidence status and confidence

Two distinct properties are recorded. **Evidence status** describes how a record or assertion is currently supported; it is a property of the information. **Confidence** is the assessor's bounded belief in an assurance claim and uses the canonical AIDCF-008 scale; it is a property of a conclusion. Evidence status informs confidence but does not determine it, and neither is a control result.

| **Evidence status** | **Meaning**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| CONFIRMED           | Direct, relevant and sufficiently current evidence supports the assertion.  |
| PARTIALLY_CONFIRMED | Evidence supports part of the assertion or scope.                           |
| ASSERTED            | Claim provided by an accountable source but not independently corroborated. |
| INFERRED            | Derived from related facts using declared reasoning.                        |
| CONFLICTING         | Material sources disagree and conflict remains unresolved.                  |
| STALE               | Evidence or observation is no longer sufficiently current.                  |
| UNKNOWN             | Information is insufficient to reach a defensible state.                    |

| **Confidence** | **Meaning (AIDCF-008)**                                                                         |
|----------------|-------------------------------------------------------------------------------------------------|
| CONF-0 UNKNOWN   | No defensible confidence state.                                                               |
| CONF-1 LOW       | Weak or limited evidence; high sensitivity to assumptions.                                    |
| CONF-2 MODERATE  | Reasonable support with material limitations.                                                 |
| CONF-3 HIGH      | Strong support with no unresolved material conflict within scope.                             |
| CONF-4 VERY_HIGH | Highly defensible, independently corroborated and representative support for the bounded claim. |

The flags CONFLICTING and STALE may be attached to any confidence value. v1.0 used the evidence-status codes above as "confidence states"; records migrating from v1.0 move them to evidenceStatus and assign confidence separately.

## 54. UNKNOWN doctrine

Materiality is defined in AIDCF-002 §22 and used here unchanged: a fact, dependency, condition, deficiency or UNKNOWN is **MATERIAL** if, had it been known or resolved differently, a competent assessor would reasonably expect it to change (a) a control result, (b) a gate result, (c) the decision state, or (d) a condition, limitation or ceiling attached to the decision, for the declared Capability Instance, Service Outcomes and operating states. Wherever this standard says "material", that test applies.

> **IOT-REQ-030** UNKNOWN may apply to an entity existence, class, property, relationship, state, capacity, owner, evidence status or conclusion.
>
> **IOT-REQ-031** UNKNOWN shall be recorded as an UnknownRecord (Part XV) identifying the missing information, why it is MATERIAL or not, current owner for resolution where known, UNKNOWN type (U1–U10), severity (US1–US5) and assurance impact.
>
> **IOT-REQ-032** UNKNOWN shall not be replaced with an assumed favourable value to enable scoring, a gate PASS or a favourable decision state.

## 55. Conflict representation

Conflicting records shall be retained with separate provenance and effective periods. A resolution record may select, reconcile or reject assertions, but the original conflict trail should remain auditable.

# Part XII - Conformance rules and validation shapes

## 56. Core validation rules

| **Rule**    | **Validation statement**                                                                                                  |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| IOT-VAL-001 | Every Capability Instance has at least one Service Outcome.                                                               |
| IOT-VAL-002 | Every Service Outcome REQUIRES_FUNCTION at least one Required Function.                                                     |
| IOT-VAL-003 | Every Required Function is IMPLEMENTED_BY at least one System, Asset or external service, or has an UnknownRecord.                  |
| IOT-VAL-004 | Every material physical Asset has a Location or UNKNOWN.                                                                  |
| IOT-VAL-005 | Every material Asset has an owner and operator or explicit UNKNOWN.                                                       |
| IOT-VAL-006 | Every boundary-crossing dependency identifies an external provider or UNKNOWN.                                            |
| IOT-VAL-007 | Every capacity assertion has metric, unit, state, condition, time and confidence.                                         |
| IOT-VAL-008 | Every redundancy claim identifies protected function, alternatives, transfer mechanism, common dependencies and evidence. |
| IOT-VAL-009 | Every independence claim is evidence-backed and condition-bounded.                                                        |
| IOT-VAL-010 | Every critical dependency identifies applicable states and strength.                                                      |
| IOT-VAL-011 | Every assurance-relevant relationship has provenance and effective period.                                                |
| IOT-VAL-012 | Every asset class derives from a canonical or registered extension class.                                                 |
| IOT-VAL-013 | Every Change Event links affected entities and assurance impact.                                                          |
| IOT-VAL-014 | Every UNKNOWN record states the unresolved attribute and its consequence.                                                 |
| IOT-VAL-015 | Every Service Outcome and resilience claim is tied to a Capability Instance and Operating Envelope.                       |
| IOT-VAL-016 | No evidence object is treated as a safeguard; it evidences a safeguard or assertion.                                      |
| IOT-VAL-017 | No control abstraction is represented as proof that a real safeguard exists.                                              |
| IOT-VAL-018 | No maturity value automatically creates an assurance decision.                                                            |
| IOT-VAL-019 | No excluded dependency is removed from the capability dependency view.                                                    |
| IOT-VAL-020 | No vendor-specific term replaces its canonical parent in cross-profile exchange.                                          |
| IOT-VAL-021 | Every class instance carries a valid primary domain code or the Upper tag, consistent with Appendix A.                    |
| IOT-VAL-022 | Every ControlAssessment has exactly one result, one claim type, a scope, operating states and an evidence package or UnknownRecord. |
| IOT-VAL-023 | Every GateResult status is one of PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED.                                       |
| IOT-VAL-024 | Every AssuranceDecision has a decision state, lifecycle state, authority, scope, validity and links to its GateResults and UnknownRecords. |
| IOT-VAL-025 | Every IACS Zone and Conduit in scope declares SL-T; any claimed SL-A is evidence-backed and never copied from SL-C.        |

## 57. Quality tests

| **Test family**          | **Questions**                                                                                           |
|--------------------------|---------------------------------------------------------------------------------------------------------|
| Completeness             | Are material capabilities, outcomes, functions, assets, external services and dependencies represented? |
| Consistency              | Do class and relationship uses obey definitions and cardinalities?                                      |
| Traceability             | Can each material assertion be traced to evidence and provenance?                                       |
| Currency                 | Do effective dates and configuration states reflect the assessment point in time?                       |
| Boundary integrity       | Are exclusions and boundary-crossing dependencies visible?                                              |
| Cross-domain integration | Do power, cooling, control, compute, storage and network chains connect?                                |
| Failure readiness        | Can AIDCF-004 attach causes, failure modes, propagation and consequences without semantic gaps?         |
| Assurance readiness      | Can controls, evidence, results, findings, UNKNOWN Records, gate results and decisions attach to the represented subject? |
| Interoperability         | Can the dataset be exported using controlled identifiers and namespaces?                                |
| Human usability          | Can engineers and assessors interpret the model without specialist graph tooling?                       |

## 58. Prohibited modelling practices

- Using a single building-level rating as a property of every hosted capability.

- Treating product type as proof of performance or compliance.

- Hiding external dependencies because they are contractually assigned.

- Representing nominal redundancy without shared-dependency analysis.

- Combining designed, as-built and observed states into one unqualified record.

- Encoding UNKNOWN as zero, false, PASS, NONCONFORMING or NOT_APPLICABLE.

- Creating vendor-specific top-level classes where a vendor-neutral parent is sufficient.

- Using transitive graph reasoning to infer capacity, safety or engineering adequacy.

- Removing superseded records needed to understand historical decisions.

- Treating an ontology completeness score as infrastructure assurance.

# Part XIII - Reference implementation profiles

## 59. Profile construction method

A profile selects mandatory classes, relationships, properties, evidence expectations and validation rules for a repeatable deployment pattern. Profiles shall not alter upper ontology meaning.

| **Profile**                        | **Scope and emphasis**                                                                                                                                                      |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Enterprise inference facility      | Low- or moderate-scale inference in an enterprise site. Emphasis: latency, service networks, shared power/cooling, tenant interaction, recoverability.                      |
| Distributed training cluster       | Multi-node accelerated training. Emphasis: scale-up/scale-out fabrics, checkpoint storage, job completion, power/thermal concentration and failure containment.             |
| Liquid-cooled rack-scale AI system | High-density rack-scale system. Emphasis: direct-liquid loops, CDU dependencies, water quality, leak boundaries, transient response, rack power and structural load.        |
| AI colocation tenancy              | Tenant equipment hosted in provider facility. Emphasis: boundary, responsibility, evidence access, contracted capacity, shared fault domains and cross-connects.            |
| Sovereign AI infrastructure        | Strategic capability with location and control constraints. Emphasis: operational autonomy, remote support, jurisdiction, supply, spares, identities and external services. |
| AI supercomputing facility         | Large HPC/AI deployment. Emphasis: high-performance fabric, parallel storage, scheduler, job resilience, large-scale power/cooling and recovery.                            |
| Edge AI facility                   | Constrained remote deployment. Emphasis: environmental envelope, limited staffing, network dependence, remote management and local safety.                                  |
| Multi-site AI service              | Capability distributed across sites. Emphasis: inter-site dependencies, data replication, routing, control plane, failover and service-level boundary.                      |

## 60. Worked profile: liquid-cooled distributed training capability

| **Element**               | **Illustrative ontology record**                                                                                                              |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Capability Instance       | Distributed foundation-model training capability at Site A.                                                                                   |
| Service Outcomes          | Minimum usable accelerator capacity; maximum interruption; checkpoint survival; bounded restart time.                                         |
| Required Functions        | Electrical continuity; heat capture and rejection; scale-out transport; metadata access; checkpoint persistence; scheduling.                  |
| Systems                   | Compute cluster; rack power path; liquid cooling system; parallel storage; AI fabric; management system.                                      |
| Boundary                  | Defined halls, racks, infrastructure systems and external utility/OEM services.                                                               |
| Cross-domain dependencies | Utility -\> UPS -\> busway -\> rack; cold plate -\> secondary loop -\> CDU -\> facility loop -\> heat rejection; node -\> fabric -\> storage. |
| Fault domains             | Rack-scale compute domain; CDU loop; electrical path; fabric plane; storage protection group; operator team.                                  |
| Operating states          | NORMAL; MAINTENANCE (single electrical path); DEGRADED (cooling); RECOVERY; TRANSITION.                                                       |
| Material UNKNOWN examples | Unverified secondary-loop autonomy; unclear shared controller; stale resilient-capacity study (each an UnknownRecord with type and severity). |
| Evidence links            | As-built diagrams, commissioning tests, telemetry, maintenance records, failure tests and observed configuration.                             |

## 61. Competency questions for profile review

- Can every required service outcome be traced to functions, systems and assets?

- Are physical and logical topology views consistent?

- Are power and cooling capacities expressed under the same operating conditions as compute demand?

- Are management and control dependencies represented, including those required during recovery?

- Are shared dependencies visible across apparent redundant paths?

- Does evidence cover degraded and maintenance states, not only normal operation?

- Can an external reviewer identify what remains UNKNOWN without reverse-engineering narrative reports?

# Part XIV - Machine-readable publication specification

## 62. Required publication package

| **File**                           | **Purpose**                              |
|------------------------------------|------------------------------------------|
| aidcf-iot-v1.0.owl                 | Formal ontology in OWL.                  |
| aidcf-iot-v1.0.ttl                 | Human-readable RDF/Turtle serialization. |
| aidcf-context-v1.0.jsonld          | JSON-LD context.                         |
| aidcf-schema-v1.0.json             | JSON Schema for exchange records.        |
| aidcf-shapes-v1.0.ttl              | SHACL validation shapes.                 |
| aidcf-vocabulary-v1.0.csv          | Controlled term register, including domain codes and Appendix A tags. |
| aidcf-relationships-v1.0.csv       | Relationship registry.                   |
| aidcf-example-minimal-v1.0.jsonld  | Minimal conformant example.              |
| aidcf-example-training-v1.0.jsonld | Worked training-cluster profile.         |
| CHANGELOG.md                       | Version history and changes.             |
| MIGRATION.md                       | Compatibility and migration guidance.    |
| LICENSE.md                         | Usage and extension rules.               |

## 63. Namespace policy

The AIDCF ontology namespace is `https://w3id.org/aidcf/ontology#` with the prefix `aidcf:`, and the version IRI of the current release line is `https://w3id.org/aidcf/ontology/1.3`. Registration of the `aidcf` space with the w3id.org persistent-identifier service is pending; until it is confirmed these IRIs shall be treated as reserved draft identifiers and shall not be represented as resolvable production identifiers. v1.0 proposed `https://w3id.org/aidcf/iot/1.0/`; that pattern is withdrawn. The class and relationship names in this standard are the local names under this namespace (for example `aidcf:CapabilityInstance`).

## 64. Identifier rules

- Class identifiers use PascalCase, for example CapabilityInstance.

- Relationship identifiers use UPPER_SNAKE_CASE in human registries and stable lowerCamelCase or IRI form in machine schemas.

- Instance identifiers shall be opaque enough to avoid embedding sensitive facility details.

- Identifiers shall not be reassigned after retirement.

- Human-readable labels may change without changing semantic identifiers where meaning is stable.

- Breaking semantic changes require a new major namespace version.

## 65. JSON exchange skeleton

Illustrative only; the context IRI resolves only once w3id registration is complete (§63).


{  
"@context": "https://w3id.org/aidcf/ontology/1.3/context.jsonld",  
"id": "capability-instance:example-001",  
"type": "CapabilityInstance",  
"name": "Example distributed training capability",  
"serviceOutcomes": \["outcome:compute-capacity", "outcome:checkpoint-recovery"\],  
"assessmentBoundary": "boundary:example-001",  
"operatingEnvelope": "envelope:example-001",  
"requiredFunctions": \["function:power-continuity", "function:heat-removal", "function:scale-out-transport"\],
"evidenceStatus": "ASSERTED",  
"confidence": "CONF-1"  
}

## 66. Extension governance

> **IOT-REQ-033** An extension shall publish namespace, owner, scope, parent mappings, definitions, constraints, examples, tests, version and compatibility statement.
>
> **IOT-REQ-034** A profile shall not weaken canonical validation rules without declaring a nonconformance.
>
> **IOT-REQ-035** Vendor mappings should map product terms to canonical classes rather than creating competing upper ontologies.

## 67. Integration boundary with AI Trust Graph

AIDCF-005 specifies the integration in full; the summary below fixes only the ontology boundary.

| **AIDCF primary semantics**                                                                                              | **Shared handoff**                                                                                                    | **AI Trust Graph primary semantics**                                                                        |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Site, building, power, cooling, facility OT, physical assets, compute hardware, storage infrastructure and interconnect. | Identifiers, evidence, infrastructure services, machine identities, management interfaces, dependencies and findings. | Models, agents, tools, APIs, human and machine identities, authority, reachability and digital trust paths. |

# Part XV - Assurance-chain classes

Parts III to XI represent the infrastructure half of the canonical chain (steps 2 to 6) and the attachment points for adverse scenarios and safeguards (steps 7 and 8). This Part represents the assurance half: the decision question (step 1), controls and evidence (steps 9 to 11), results, findings and UNKNOWN Records (steps 12 and 13), gates, scores and decisions (steps 14 to 16), and the report and reassessment trigger that close the loop. Meanings are those of AIDCF-002; controlled values are owned by the artifacts named in §69. Class names are identical to the AIDCF-014 §7 object classes except where §68 states otherwise.

## 68. Class definitions

| **Class** | **Definition** | **Key attributes** | **AIDCF-014 class** |
|-----------|----------------|--------------------|---------------------|
| aidcf:DecisionQuestion | The precise question an assessment exists to answer, fixing subject, intended use, decision owner and date of reliance; the context of the assurance-case top claim. | questionText; capabilityInstanceRef; intendedUse; decisionOwner; asOfDate; serviceOutcomeRefs; operatingStates | Carried as the decisionQuestion attribute of Assessment and AssuranceDecision |
| aidcf:ControlDomain | One of the fifteen top-level groupings of the AIDCF-007A registry, identified by a fixed three-letter code (GOV … EVA). | domainId; title; familyIds (exactly six); registryVersion | ControlDomain |
| aidcf:ControlFamily | A group of four related controls within one domain, identified as `<DOM>-01` to `<DOM>-06`. | familyId; domainId; title; controlIds (exactly four) | ControlFamily |
| aidcf:Control | An assessable requirement in the AIDCF-007A registry, identified as `MCF-<DOM>-NNN`, stating objective, requirement, assessment criteria and evidence profile. A control is evaluated against one or more Safeguards; it is not itself a protective measure. | controlId; familyId; objective; requirement; assessmentCriteria; parameters; evidenceProfile (claimType, profileTier, sufficiencyFloor); assessmentMethods; controlType; requiredAssuranceLevel; gateMappings (gateId, role CRITICAL or SUPPORTING); ontologyClasses; applicability | Control |
| aidcf:EvidenceRequirement | The evidence a control needs for a stated claim type: required and optional evidence classes, quality floor, sufficiency floor, state and period coverage, independence and mandatory items. | evidenceRequirementId; controlRef; claimType; requiredClasses (E1–E7); qualityFloor (P F C R T I); sufficiencyFloor (S2–S5); stateCoverage; periodCoverage; independence; mandatoryItems; acceptableAlternatives; unknownEffect | EvidenceRequirement |
| aidcf:EvidenceObject | A record, observation, measurement, test output or analysis used to support, challenge or qualify one or more Assertions. | evidenceId; evidenceClass (E1–E7); source; collector; custodian; observationTime; period; operatingStates; scope; integrity (I0–I5); quality vector (P, F, C, R, T, I each 0–5); qualityBand (Q0–Q5); assertionRefs; restrictions | EvidenceObject |
| aidcf:EvidencePackage | A versioned, integrity-protected set of Evidence Objects assembled for a defined control, gate or decision, with a manifest and a sufficiency rating. | packageId; purposeRef (control, gate or decision); members; manifestHash; sufficiency (S0–S5); coverage (scope, states, period); gaps; reviewer | EvidencePackage |
| aidcf:Assertion | One precise, testable proposition, expressed as subject, predicate and object with scope, conditions and effective time, that evidence supports, challenges or qualifies. | assertionId; subjectRef; predicate; objectRef or value; scope; conditions; effectivePeriod; status (CANDIDATE, SUPPORTED, CHALLENGED, QUALIFIED, CONFLICTING, UNKNOWN, SUPERSEDED); evidenceRefs; confidence | No standalone class: carried through assertionRefs on EvidenceObject and the claim on ControlAssessment, with status from the AIDCF-014 Assertion vocabulary |
| aidcf:ControlAssessment | The evaluation of one Control for one claim type over a declared scope, set of operating states and period, yielding exactly one control result. | controlAssessmentId; controlRef; claimType; scope; operatingStates; period; methods; evidencePackageRef; result; confidence (CONF-0–CONF-4); findingRefs; unknownRefs; assessor; reviewer; lifecycleState (including SUSPENDED) | ControlAssessment |
| aidcf:Finding | A recorded condition, against a stated criterion, that is a deficiency or a MATERIAL observation, with its cause, consequence and effect on gates and scores. | findingId; criterionRef; condition; evidenceRefs; cause; consequence; classification; gateEffect; scoreEffect; owner; status; closureRef | Finding |
| aidcf:UnknownRecord | A preserved record that a MATERIAL attribute, relationship, result or criterion cannot be determined, with its type, severity and decision effect. | unknownId; subjectRef; missingAttribute; reason; unknownType (U1–U10); severity (US1–US5); decisionEffect; evidenceNeeded; owner; trigger; status | UnknownRecord |
| aidcf:CriticalGate | One of the fifteen non-compensable conditions CG-01 to CG-15, with its protected scope, criteria and evidence floor. | gateId; name; scope; criteria (AIDCF-010); evidenceFloor (S3–S5); criticalControlRefs (from AIDCF-007A gate mappings); decisionCeilings | CriticalGate |
| aidcf:GateResult | The evaluation of one CriticalGate for one assessment, with a status of PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED. There is no conditional gate status. | gateResultId; gateRef; assessmentRef; applicability; criterionResults; criticalControlResults; supportingControlEvaluations; evidenceRefs; stateCoverage; findingRefs; unknownRefs; status; decisionEffect; reviewer | GateResult |
| aidcf:ScoreSnapshot | An immutable record of scores computed under AIDCF-010 at a point in time: control state values, family and domain means, coverage and bands. Scores never override gates. | snapshotId; assessmentRef; profileVersion; inputs (ControlAssessment refs); weights; familyScores; domainScores; coverage; band (B1–B5 or withheld); withheldReason; computedAt | ScoreSnapshot |
| aidcf:DecisionRecommendation | The assessor's proposed decision state, with conditions, limitations and ceilings derived from Gate Results, UNKNOWN severities and scores, submitted for review and approval. | recommendationId; assessmentRef; proposedState; gateCeilings; unknownCeilings; conditions; limitations; rationale; recommender | DecisionRecommendation |
| aidcf:AssuranceDecision | The accountable, authorised conclusion answering the Decision Question, in one decision state, with its authority, scope, conditions and validity. | decisionId; decisionQuestion; subjectRef; scope; recommendationRef; gateResultRefs; unknownRefs; scoreSnapshotRef; conditions; decisionState; lifecycleState; authority; validity | AssuranceDecision |
| aidcf:AssuranceStatement | The controlled wording that expresses an approved Assurance Decision for a named audience, with mandatory bounds and limitations (AIDCF-012). | statementId; decisionRef; audience; wording; bounds; limitations; issuer; issueDate | AssuranceStatement |
| aidcf:AssuranceReport | The issued report carrying one or more Assurance Statements and their basis: results, findings, UNKNOWN register, gate results, scores and limitations (AIDCF-012). | reportId; reportClass; programRef; assessmentRef; decisionRefs; statementRefs; intendedUsers; classification; validity; approvals; distributionControl | AssuranceReport |
| aidcf:ReassessmentTrigger | A condition or event that invalidates, limits or requires review of prior results or a decision, such as a material change, incident, evidence expiry, UNKNOWN resolution or monitoring threshold. | triggerId; triggerType; rule or threshold; subjectRefs; affectedObjectRefs; requiredAction; raisedAt; status | ReassessmentTrigger |

## 69. Controlled values used by assurance classes

The controlled values below are owned by the artifacts named and are listed here so that the ontology can type them. This standard does not redefine them.

| **Attribute** | **Controlled values** | **Owner** |
|---------------|-----------------------|-----------|
| claimType | DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS, RESILIENCE | AIDCF-002; AIDCF-007A |
| requiredAssuranceLevel | AL2 to AL5 (programme levels AL0 to AL6) | AIDCF-011 |
| result (ControlAssessment) | CONFORMING, PARTIAL, NONCONFORMING, UNKNOWN, NOT_APPLICABLE, NOT_ASSESSED | AIDCF-002; AIDCF-010 |
| status (GateResult) | PASS, FAIL, UNKNOWN, APPROVED_NA, NOT_ASSESSED | AIDCF-010 |
| decisionState | REASONABLY_ASSURED, CONDITIONALLY_ASSURED, LIMITED, NOT_ASSURED, INCONCLUSIVE | AIDCF-010 |
| lifecycleState (AssuranceDecision) | DRAFT, RECOMMENDED, APPROVED, ACTIVE, SUSPENDED, WITHDRAWN, SUPERSEDED, EXPIRED | AIDCF-010 |
| confidence | CONF-0 UNKNOWN to CONF-4 VERY_HIGH, with flags CONFLICTING and STALE | AIDCF-008 |
| evidenceClass; quality; qualityBand; sufficiency; integrity | E1–E7; P, F, C, R, T, I rated 0–5; Q0–Q5; S0–S5; I0–I5 | AIDCF-008 |
| unknownType; severity | U1–U10; US1 Low to US5 Systemic | AIDCF-008; AIDCF-002 §31 |
| methods | INQUIRY, DOCUMENT_REVIEW, INSPECTION, OBSERVATION, RECONCILIATION, ANALYSIS, SAMPLING, TEST, REPERFORMANCE, SCENARIO_EXERCISE | AIDCF-009 |
| controlType | DIRECTIVE, PREVENTIVE, DETECTIVE, CORRECTIVE, RECOVERY | AIDCF-007A |
| band | B5 Strong to B1 Very weak, or "Band withheld (coverage/UNKNOWN)" | AIDCF-010 |

## 70. Assurance-chain relationships

All predicates below are AIDCF-014 §9 relationship types.

| **Subject** | **Predicate** | **Object** | **Meaning** |
|-------------|---------------|------------|-------------|
| Safeguard | GOVERNED_BY | Control | The safeguard is the real measure that the control evaluates. |
| ControlDomain | COMPOSED_OF | ControlFamily | A domain holds six families. |
| ControlFamily | COMPOSED_OF | Control | A family holds four controls. |
| Control | HAS_EVIDENCE_REQUIREMENT | EvidenceRequirement | The control's claim needs this evidence. |
| EvidenceRequirement | EVIDENCED_BY | EvidencePackage | The package is offered against the requirement. |
| EvidencePackage | COMPOSED_OF | EvidenceObject | Package membership. |
| EvidenceObject | SUPPORTS / CHALLENGES / QUALIFIES | Assertion | Evidence bears on a precise proposition. |
| Control | ASSESSED_BY | ControlAssessment | The control was evaluated for a claim type and scope. |
| ControlAssessment | HAS_FINDING / HAS_UNKNOWN | Finding / UnknownRecord | Deficiencies and indeterminacies arising from the evaluation. |
| GateResult | EVALUATES_GATE | CriticalGate | The result is the evaluation of that gate. |
| ControlAssessment | SUPPORTS or CHALLENGES | GateResult | A CRITICAL or SUPPORTING control result informs the gate evaluation. |
| Finding / UnknownRecord | CONSTRAINS | GateResult / AssuranceDecision | Defeaters and ceilings on the gate or the decision. |
| ControlAssessment | SUMMARISED_BY | ScoreSnapshot | Scored inputs to the snapshot. |
| DecisionRecommendation | RECOMMENDS | AssuranceDecision | Proposed state, conditions and ceilings. |
| AssuranceDecision | REVIEWED_BY / APPROVED_BY | Role | Independent review and decision authority. |
| AssuranceDecision | REPORTED_IN | AssuranceReport | The decision is expressed in the report through an AssuranceStatement. |
| Finding | REQUIRES_ACTION / CLOSED_BY | Action | Remediation and closure. |
| ReassessmentTrigger | TRIGGERS_REASSESSMENT | ControlAssessment / GateResult / AssuranceDecision | The trigger requires review of the object. |
| AssuranceDecision | INVALIDATED_BY / SUPERSEDES | ReassessmentTrigger / AssuranceDecision | Loss of validity and replacement without erasure. |

## 71. Requirements for assurance-chain records

> **IOT-REQ-036** Implementations shall represent controls, evidence, results, findings, UNKNOWN Records, gate results, scores, recommendations, decisions, statements, reports and reassessment triggers using the classes of §68 and the AIDCF-014 class names they map to.
>
> **IOT-REQ-037** A ControlAssessment shall record exactly one result for exactly one claim type, scope, set of operating states and period; a control assessed for several claim types shall have one ControlAssessment per claim type.
>
> **IOT-REQ-038** A ControlAssessment whose evidence is below the floor of its EvidenceRequirement shall carry the result UNKNOWN and link an UnknownRecord; it shall not carry a reduced numeric value in place of the result.
>
> **IOT-REQ-039** A GateResult shall carry one of PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED; conditions shall be represented only on the DecisionRecommendation and AssuranceDecision.
>
> **IOT-REQ-040** An AssuranceDecision shall reference the DecisionRecommendation, GateResults, UnknownRecords and ScoreSnapshot on which it relies, and a ScoreSnapshot shall not be the sole basis of a decision state.
>
> **IOT-REQ-041** An Evidence Object shall not be typed as a Safeguard or a Control; it evidences an Assertion about a Safeguard, an asset or a result.

# Part XVI - Industrial automation and control system security concepts (IEC 62443 alignment)

AI data centres depend on industrial automation and control systems for their Required Functions: the BMS, EPMS and SCADA platforms, programmable logic controllers in coolant distribution units, chiller plants and switchgear, generator and transfer-scheme controllers, fire-alarm interfaces, and the engineering workstations and remote-support paths used to change them. The IEC 62443 series provides the established vocabulary for securing such systems. This Part imports the concepts needed to represent them; it paraphrases and references the series at document level and does not reproduce its requirements. Conformity with IEC 62443 is not claimed or implied by using these classes.

## 72. IACS classes

| **Class** | **Definition** | **Key attributes** | **Relationships** |
|-----------|----------------|--------------------|-------------------|
| aidcf:IACS | Industrial Automation and Control System: the personnel, hardware, software and policies that operate, monitor and protect a physical process. In AIDCF, the control systems of power, cooling, fire and building services, including their engineering workstations, historians and gateways. Subclass of InfrastructureSystem. | iacsId; controlledFunctions (RequiredFunction refs); components (BMS, EPMS, SCADA, PLC, RTU, controllers); assetOwner; integrator; maintainer; zoneRefs | CONTROLLED_BY (from POW, THM and PHY systems to the IACS); COMPOSED_OF (zones, components) |
| aidcf:IACSZone | A grouping of logical or physical assets that share common security requirements, defined through a security risk assessment (IEC 62443-3-2). Distinct from the physical aidcf:SecurityZone. | zoneId; members; controlledFunctions; riskAssessmentRef; slTarget; slAchieved; owner; boundaryDescription | COMPOSED_OF (assets); PROTECTED_BY (safeguards); SHARES_FAULT_DOMAIN_WITH (where zones share platforms, identities or networks) |
| aidcf:Conduit | A logical grouping of communication channels connecting two or more zones that share common security requirements (IEC 62443-3-2). | conduitId; connectedZones; channels (protocols, endpoints, direction); slTarget; slAchieved; countermeasures; remoteAccess (yes/no); owner | CONNECTS_TO (zones); PROTECTED_BY (filtering, gateways, remote-access controls) |
| aidcf:SecurityLevel | A level 0 to 4 expressing the protection a zone, conduit or component provides against increasingly capable violation, recorded per foundational requirement as a seven-element vector. Three kinds are distinguished: **SL-T** (target) is the level required for a zone or conduit by the risk assessment; **SL-C** (capability) is the level a component or system can provide when properly configured (IEC 62443-3-3, IEC 62443-4-2); **SL-A** (achieved) is the level actually provided by the deployed zone or conduit as assessed. | kind (SL-T, SL-C, SL-A); subjectRef; vector (FR1–FR7, each 0–4); basis; evidenceRefs; assessedAt | Attribute vector on IACSZone, Conduit and Component; SL-A is EVIDENCED_BY assessment evidence |
| aidcf:FoundationalRequirement | One of the seven IEC 62443 foundational requirements against which security levels are expressed: FR1 Identification and authentication control; FR2 Use control; FR3 System integrity; FR4 Data confidentiality; FR5 Restricted data flow; FR6 Timely response to events; FR7 Resource availability. | frId (FR1–FR7); label | Index of the SecurityLevel vector |

## 73. Relationship to SEC controls and to gates CG-07 and CG-15

The concepts in §72 give SEC controls in AIDCF-007A a precise subject. Gate roles (CRITICAL or SUPPORTING) are assigned per control in the AIDCF-007A registry and are not restated here.

| **Concept** | **AIDCF-007A controls that assess it** | **Gate relevance** |
|-------------|------------------------------------------|--------------------|
| IACS inventory and controlled functions | MCF-SEC-005 BMS and EPMS Security; POW-06 and THM-06 monitoring and control families; OPS-05 configuration baseline | CG-07: the gate cannot be evaluated without knowing which IACS components control which Required Functions |
| Zone and conduit model with SL-T | MCF-SEC-009 Security Zoning; MCF-SEC-010 Management-Plane Segmentation; MCF-SEC-011 Filtering and Gateways | CG-07 (control-system integrity) and CG-15 (bounded digital authority) |
| Remote and third-party access across conduits | MCF-SEC-012 Remote Access; SUP-06 remote support controls (MCF-SUP-021 to MCF-SUP-024) | CG-15 |
| FR1 and FR2 (identification, authentication and use control) | SEC-01 controls (MCF-SEC-001 to MCF-SEC-004) | CG-15 |
| FR3 (system integrity) | SEC-04 controls (MCF-SEC-013 to MCF-SEC-016); SUP-04 software and firmware supply | CG-07; CG-14 (change control) |
| FR6 (timely response to events) | SEC-05 controls (MCF-SEC-017 to MCF-SEC-020) | CG-07; CG-15 |
| FR7 (resource availability) | POW, THM and RES controls for the controlled functions | CG-05, CG-06, CG-10 through the controlled functions |
| Automated or AI-enabled commands into a zone | SEC-06 controls (MCF-SEC-021 to MCF-SEC-024) | CG-07; CG-15 |

## 74. Requirements for IACS representation

> **IOT-REQ-042** Where an IACS controls or protects a Required Function within the assessment boundary, the dataset shall represent the IACS, its zones and conduits, and the Required Functions each zone controls.
>
> **IOT-REQ-043** Every in-scope IACSZone and Conduit shall declare an SL-T vector with the risk-assessment reference that justifies it, or carry an UnknownRecord stating that no SL-T has been established.
>
> **IOT-REQ-044** An SL-A vector shall be supported by assessment evidence of the deployed zone or conduit; the SL-C of a component shall not be recorded as the SL-A of the zone or conduit that contains it.
>
> **IOT-REQ-045** Where SL-A is below SL-T for any foundational requirement in a zone or conduit that controls a Required Function, the difference shall be recorded as a Finding linked to the affected controls and evaluated in the GateResults for CG-07 and, where identity, privilege or remote access is involved, CG-15; where SL-A has not been evidenced, an UnknownRecord shall be raised and its severity assigned under the canonical US1–US5 scale.
>
> **IOT-REQ-046** A physical aidcf:SecurityZone shall not be used as a substitute for an aidcf:IACSZone, and network adjacency shall not be represented as a Conduit unless the communication channels it carries are identified.

# Appendix A - Canonical class registry

All identifiers are local names in the `aidcf:` namespace (§63). **Domain code(s)** gives the primary AIDCF-007A domain first, then secondary codes; Upper marks a cross-domain upper-ontology class. **AIDCF-014 class** gives the exchange class under which instances are serialised; a dash means the class is an ontology-level concept carried as an attribute or relationship rather than a separate exchange object.

## A.1 Upper-ontology and core classes

| **Canonical ID**           | **Preferred label**   | **Definition**                                                                                             | **Domain code(s)** | **AIDCF-014 class**                     |
|----------------------------|-----------------------|------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------|
| aidcf:Capability           | Capability            | An intended operational ability supported by infrastructure.                                               | CAP                | —                                       |
| aidcf:CapabilityInstance   | Capability Instance   | A specific deployment bounded by ownership, location, architecture, capacity, criticality and obligations. | CAP                | CapabilityInstance                      |
| aidcf:ServiceOutcome       | Service Outcome       | A measurable or assessable result required from a Capability Instance.                                     | CAP                | ServiceOutcome                          |
| aidcf:RequiredFunction     | Required Function     | A function whose loss or degradation would materially affect a Service Outcome (v1.0: CriticalFunction).   | CAP                | RequiredFunction                        |
| aidcf:OperatingEnvelope    | Operating Envelope    | The bounded conditions under which a capability or system is intended to operate.                          | CAP                | — (attribute set of CapabilityInstance) |
| aidcf:AssessmentBoundary   | Assessment Boundary   | The declared inclusion perimeter for direct assessment.                                                    | DEP, EVA           | — (scope of Assessment)                 |
| aidcf:Dependency           | Dependency            | A reliance by one entity upon another entity, resource, condition or decision.                             | DEP                | Dependency                              |
| aidcf:FaultDomain          | Fault Domain          | A set of entities expected to be affected by a common failure.                                             | RES, DEP           | FaultDomain                             |
| aidcf:RedundancyGroup      | Redundancy Group      | Assets or paths deliberately arranged to preserve a function.                                              | RES                | — (attribute of FaultDomain/Dependency) |
| aidcf:InfrastructureSystem | Infrastructure System | A coordinated set of assets and interfaces providing one or more functions.                                | Upper              | InfrastructureSystem                    |
| aidcf:AssetInstance        | Asset Instance        | An identifiable real-world item, service, person, procedure or resource.                                   | Upper              | AssetInstance                           |
| aidcf:Component            | Component             | A constituent part of an asset or system represented where material.                                       | Upper              | AssetInstance (componentOf)             |
| aidcf:Interface            | Interface             | A defined point or mechanism of exchange between entities.                                                 | Upper              | Interface                               |
| aidcf:Connection           | Connection            | A realised physical, logical, hydraulic, electrical, thermal or organisational link.                       | Upper              | CONNECTS_TO relationship                |
| aidcf:Resource             | Resource              | Consumable or constrained input required for operation.                                                    | Upper              | Resource                                |
| aidcf:Location             | Location              | A geographic, site, building, zone, room, row, rack or logical placement.                                  | Upper              | — (LOCATED_IN target)                   |
| aidcf:Safeguard            | Safeguard             | A real-world measure intended to anticipate, prevent, detect, contain, respond, recover or adapt.          | Upper              | Safeguard                               |
| aidcf:Actor                | Actor                 | A human or machine participant with a relevant role.                                                       | Upper              | —                                       |
| aidcf:Organisation         | Organisation          | A legally or operationally recognised party.                                                               | Upper              | —                                       |
| aidcf:Role                 | Role                  | A named set of responsibilities and authorities.                                                           | GOV                | —                                       |
| aidcf:OperatingState       | Operating State       | A defined condition of operation (§45).                                                                    | Upper              | OperatingState                          |
| aidcf:ChangeEvent          | Change Event          | An approved, observed or unapproved modification affecting the represented system.                         | OPS, CAP           | Event (eventType = CHANGE)              |

## A.2 Domain taxonomy classes

Each class below is a specialisation of the upper class appropriate to its kind (InfrastructureSystem, AssetInstance, Component, Interface, Resource, Location, Role or a record class) and is defined by its preferred label within the taxonomy family named; the family descriptions in Part V give the context. Instances are exchanged under the AIDCF-014 class of their upper class (normally AssetInstance or InfrastructureSystem; resources as Resource; records as EvidenceObject). Classes marked † were added in v1.1.

| **Canonical ID**                      | **Preferred label**            | **Part V family**                                 | **Domain code(s)** |
|---------------------------------------|--------------------------------|---------------------------------------------------|--------------------|
| aidcf:OperatingModel                  | Operating Model                | GOV — Governance and authority                    | GOV, OPS           |
| aidcf:Delegation                      | Delegation                     | GOV — Governance and authority                    | GOV                |
| aidcf:ApprovalAuthority               | Approval Authority             | GOV — Governance and authority                    | GOV                |
| aidcf:EscalationPath                  | Escalation Path                | GOV — Governance and authority                    | GOV, OPS           |
| aidcf:RiskAcceptance                  | Risk Acceptance                | GOV — Governance and authority                    | GOV                |
| aidcf:Policy                          | Policy †                       | GOV — Obligations and baselines                   | GOV                |
| aidcf:TechnicalStandardBaseline       | Technical Standard Baseline †  | GOV — Obligations and baselines                   | GOV                |
| aidcf:ExceptionRecord                 | Exception Record †             | GOV — Obligations and baselines                   | GOV, EVA           |
| aidcf:ContractualObligation           | Contractual Obligation †       | GOV — Obligations and baselines                   | GOV, SUP           |
| aidcf:CapabilityRegister              | Capability Register †          | CAP — Capability and demand records               | CAP                |
| aidcf:DemandProfile                   | Demand Profile †               | CAP — Capability and demand records               | CAP                |
| aidcf:LoadStepProfile                 | Load Step Profile †            | CAP — Capability and demand records               | CAP, POW, THM      |
| aidcf:GrowthForecast                  | Growth Forecast †              | CAP — Capability and demand records               | CAP                |
| aidcf:DesignBasis                     | Design Basis                   | CAP — Engineering baseline and records            | CAP, GOV           |
| aidcf:SingleLineDiagram               | Single-Line Diagram            | CAP — Engineering baseline and records            | POW, CAP, EVA      |
| aidcf:PipingAndInstrumentationDiagram | P&ID                           | CAP — Engineering baseline and records            | THM, CAP, EVA      |
| aidcf:AsBuiltDrawing                  | As-Built Drawing               | CAP — Engineering baseline and records            | CAP, EVA           |
| aidcf:EngineeringStudy                | Engineering Study              | CAP — Engineering baseline and records            | CAP, EVA           |
| aidcf:CommissioningScript             | Commissioning Script           | CAP — Engineering baseline and records            | CAP, EVA           |
| aidcf:DeviationRecord                 | Deviation Record               | CAP — Engineering baseline and records            | CAP, EVA           |
| aidcf:ExternalService                 | External Service †             | DEP — Boundary and external service               | DEP, SUP           |
| aidcf:BoundaryCrossing                | Boundary Crossing †            | DEP — Boundary and external service               | DEP                |
| aidcf:ServiceInterfaceAgreement       | Service Interface Agreement †  | DEP — Boundary and external service               | DEP, SUP           |
| aidcf:Site                            | Site                           | PHY — Site and external perimeter                 | PHY                |
| aidcf:Campus                          | Campus                         | PHY — Site and external perimeter                 | PHY                |
| aidcf:PropertyBoundary                | Property Boundary              | PHY — Site and external perimeter                 | PHY                |
| aidcf:PerimeterBarrier                | Perimeter Barrier              | PHY — Site and external perimeter                 | PHY                |
| aidcf:VehicleBarrier                  | Vehicle Barrier                | PHY — Site and external perimeter                 | PHY                |
| aidcf:Gate                            | Gate                           | PHY — Site and external perimeter                 | PHY                |
| aidcf:GuardPost                       | Guard Post                     | PHY — Site and external perimeter                 | PHY                |
| aidcf:ExternalApproach                | External Approach              | PHY — Site and external perimeter                 | PHY                |
| aidcf:StandoffZone                    | Standoff Zone                  | PHY — Site and external perimeter                 | PHY                |
| aidcf:Building                        | Building                       | PHY — Building and internal zoning                | PHY                |
| aidcf:Floor                           | Floor                          | PHY — Building and internal zoning                | PHY                |
| aidcf:DataHall                        | Data Hall                      | PHY — Building and internal zoning                | PHY                |
| aidcf:Room                            | Room                           | PHY — Building and internal zoning                | PHY                |
| aidcf:Cage                            | Cage                           | PHY — Building and internal zoning                | PHY                |
| aidcf:Suite                           | Suite                          | PHY — Building and internal zoning                | PHY                |
| aidcf:Row                             | Row                            | PHY — Building and internal zoning                | PHY                |
| aidcf:Rack                            | Rack                           | PHY — Building and internal zoning                | PHY, CMP           |
| aidcf:Cabinet                         | Cabinet                        | PHY — Building and internal zoning                | PHY                |
| aidcf:SecurityZone                    | Security Zone                  | PHY — Building and internal zoning                | PHY                |
| aidcf:RestrictedArea                  | Restricted Area                | PHY — Building and internal zoning                | PHY                |
| aidcf:LoadingArea                     | Loading Area                   | PHY — Building and internal zoning                | PHY                |
| aidcf:StagingArea                     | Staging Area                   | PHY — Building and internal zoning                | PHY                |
| aidcf:Foundation                      | Foundation                     | PHY — Civil and structural                        | PHY                |
| aidcf:FloorSlab                       | Floor Slab                     | PHY — Civil and structural                        | PHY                |
| aidcf:RaisedFloor                     | Raised Floor                   | PHY — Civil and structural                        | PHY                |
| aidcf:Roof                            | Roof                           | PHY — Civil and structural                        | PHY                |
| aidcf:Wall                            | Wall                           | PHY — Civil and structural                        | PHY                |
| aidcf:Ceiling                         | Ceiling                        | PHY — Civil and structural                        | PHY                |
| aidcf:RackAnchorage                   | Rack Anchorage                 | PHY — Civil and structural                        | PHY                |
| aidcf:SeismicRestraint                | Seismic Restraint              | PHY — Civil and structural                        | PHY                |
| aidcf:LoadBearingElement              | Load-Bearing Element           | PHY — Civil and structural                        | PHY                |
| aidcf:AccessPoint                     | Access Point                   | PHY — Entry and identity control                  | PHY                |
| aidcf:Turnstile                       | Turnstile                      | PHY — Entry and identity control                  | PHY                |
| aidcf:Mantrap                         | Mantrap                        | PHY — Entry and identity control                  | PHY                |
| aidcf:Door                            | Door                           | PHY — Entry and identity control                  | PHY                |
| aidcf:Lock                            | Lock                           | PHY — Entry and identity control                  | PHY                |
| aidcf:CredentialReader                | Credential Reader              | PHY — Entry and identity control                  | PHY, SEC           |
| aidcf:BiometricReader                 | Biometric Reader               | PHY — Entry and identity control                  | PHY                |
| aidcf:VisitorSystem                   | Visitor System                 | PHY — Entry and identity control                  | PHY                |
| aidcf:KeySystem                       | Key System                     | PHY — Entry and identity control                  | PHY                |
| aidcf:Camera                          | Camera                         | PHY — Detection and surveillance                  | PHY                |
| aidcf:VideoManagementSystem           | Video Management System        | PHY — Detection and surveillance                  | PHY, SEC           |
| aidcf:IntrusionSensor                 | Intrusion Sensor               | PHY — Detection and surveillance                  | PHY                |
| aidcf:DoorContact                     | Door Contact                   | PHY — Detection and surveillance                  | PHY                |
| aidcf:MotionSensor                    | Motion Sensor                  | PHY — Detection and surveillance                  | PHY                |
| aidcf:SecurityAlarm                   | Security Alarm                 | PHY — Detection and surveillance                  | PHY                |
| aidcf:Intercom                        | Intercom                       | PHY — Detection and surveillance                  | PHY                |
| aidcf:LoadingBay                      | Loading Bay                    | PHY — Asset movement and custody                  | PHY                |
| aidcf:GoodsLift                       | Goods Lift                     | PHY — Asset movement and custody                  | PHY                |
| aidcf:ScreeningPoint                  | Screening Point                | PHY — Asset movement and custody                  | PHY                |
| aidcf:StorageArea                     | Storage Area                   | PHY — Asset movement and custody                  | PHY                |
| aidcf:Seal                            | Seal                           | PHY — Asset movement and custody                  | PHY                |
| aidcf:ChainOfCustodyRecord            | Chain-of-Custody Record        | PHY — Asset movement and custody                  | PHY, SUP, EVA      |
| aidcf:SecurityOperationsCentre        | Security Operations Centre     | PHY — Physical response                           | PHY                |
| aidcf:GuardForce                      | Guard Force                    | PHY — Physical response                           | PHY                |
| aidcf:ResponseProcedure               | Response Procedure             | PHY — Physical response                           | PHY                |
| aidcf:DispatchChannel                 | Dispatch Channel               | PHY — Physical response                           | PHY                |
| aidcf:IncidentReconstructionRecord    | Incident Reconstruction Record | PHY — Physical response                           | PHY, EVA           |
| aidcf:DetectionZone                   | Detection Zone                 | PHY — Fire and life safety                        | PHY                |
| aidcf:FireAlarmPanel                  | Fire Alarm Panel               | PHY — Fire and life safety                        | PHY                |
| aidcf:SuppressionZone                 | Suppression Zone               | PHY — Fire and life safety                        | PHY                |
| aidcf:SuppressionAgentSystem          | Suppression Agent System †     | PHY — Fire and life safety                        | PHY, ENV           |
| aidcf:SprinklerSystem                 | Sprinkler System               | PHY — Fire and life safety                        | PHY                |
| aidcf:SmokeControl                    | Smoke Control                  | PHY — Fire and life safety                        | PHY                |
| aidcf:EmergencyEgress                 | Emergency Egress               | PHY — Fire and life safety                        | PHY                |
| aidcf:EmergencyPowerOff               | Emergency Power Off            | PHY — Fire and life safety                        | PHY, POW           |
| aidcf:IncomingSupply                  | Incoming Supply                | POW — Utility and grid interface                  | POW, DEP           |
| aidcf:UtilityFeed                     | Utility Feed                   | POW — Utility and grid interface                  | POW, DEP           |
| aidcf:GridConnection                  | Grid Connection                | POW — Utility and grid interface                  | POW, DEP           |
| aidcf:Substation                      | Substation                     | POW — Utility and grid interface                  | POW                |
| aidcf:OnSiteGeneration                | On-Site Generation             | POW — Generation and fuel                         | POW                |
| aidcf:Generator                       | Generator                      | POW — Generation and fuel                         | POW                |
| aidcf:FuelTank                        | Fuel Tank                      | POW — Generation and fuel                         | POW, ENV           |
| aidcf:FuelSystem                      | Fuel System                    | POW — Generation and fuel                         | POW                |
| aidcf:StartingSystem                  | Starting System                | POW — Generation and fuel                         | POW                |
| aidcf:ExhaustSystem                   | Exhaust System                 | POW — Generation and fuel                         | POW, ENV           |
| aidcf:Transformer                     | Transformer                    | POW — Conversion, energy storage and distribution | POW                |
| aidcf:Switchgear                      | Switchgear                     | POW — Conversion, energy storage and distribution | POW                |
| aidcf:MVSwitchgear                    | MV Switchgear                  | POW — Conversion, energy storage and distribution | POW                |
| aidcf:LVSwitchgear                    | LV Switchgear                  | POW — Conversion, energy storage and distribution | POW                |
| aidcf:TransferScheme                  | Transfer Scheme                | POW — Conversion, energy storage and distribution | POW                |
| aidcf:StaticTransferSwitch            | Static Transfer Switch         | POW — Conversion, energy storage and distribution | POW                |
| aidcf:UPS                             | UPS                            | POW — Conversion, energy storage and distribution | POW                |
| aidcf:Battery                         | Battery                        | POW — Conversion, energy storage and distribution | POW, ENV           |
| aidcf:EnergyStorage                   | Energy Storage                 | POW — Conversion, energy storage and distribution | POW                |
| aidcf:Busway                          | Busway                         | POW — Conversion, energy storage and distribution | POW                |
| aidcf:PDU                             | PDU                            | POW — Conversion, energy storage and distribution | POW                |
| aidcf:RPP                             | RPP                            | POW — Conversion, energy storage and distribution | POW                |
| aidcf:RackPDU                         | Rack PDU                       | POW — Conversion, energy storage and distribution | POW                |
| aidcf:PowerSupplyUnit                 | Power Supply Unit              | POW — Conversion, energy storage and distribution | POW, CMP           |
| aidcf:ProtectionRelay                 | Protection Relay               | POW — Protection, earthing and power quality      | POW                |
| aidcf:ProtectionDevice                | Protection Device              | POW — Protection, earthing and power quality      | POW                |
| aidcf:Relay                           | Relay                          | POW — Protection, earthing and power quality      | POW                |
| aidcf:EarthingSystem                  | Earthing System                | POW — Protection, earthing and power quality      | POW                |
| aidcf:Grounding                       | Grounding                      | POW — Protection, earthing and power quality      | POW                |
| aidcf:LightningProtection             | Lightning Protection           | POW — Protection, earthing and power quality      | POW, PHY           |
| aidcf:HarmonicFilter                  | Harmonic Filter                | POW — Protection, earthing and power quality      | POW                |
| aidcf:SurgeProtection                 | Surge Protection               | POW — Protection, earthing and power quality      | POW                |
| aidcf:EPMS                            | EPMS                           | POW — Electrical monitoring                       | POW, OPS, SEC      |
| aidcf:Meter                           | Meter                          | POW — Electrical monitoring                       | POW                |
| aidcf:PowerQualityMonitor             | Power Quality Monitor          | POW — Electrical monitoring                       | POW                |
| aidcf:ChilledWaterPlant               | Chilled Water Plant            | THM — Air-side and mechanical systems             | THM                |
| aidcf:CondenserSystem                 | Condenser System               | THM — Air-side and mechanical systems             | THM                |
| aidcf:PumpSystem                      | Pump System                    | THM — Air-side and mechanical systems             | THM                |
| aidcf:AirDistribution                 | Air Distribution               | THM — Air-side and mechanical systems             | THM                |
| aidcf:Ventilation                     | Ventilation                    | THM — Air-side and mechanical systems             | THM, ENV           |
| aidcf:Pressurisation                  | Pressurisation                 | THM — Air-side and mechanical systems             | THM                |
| aidcf:AirHandler                      | Air Handler                    | THM — Air-side and mechanical systems             | THM                |
| aidcf:InRowCooler                     | In-Row Cooler                  | THM — Air-side and mechanical systems             | THM                |
| aidcf:RearDoorHeatExchanger           | Rear-Door Heat Exchanger       | THM — Air-side and mechanical systems             | THM                |
| aidcf:HeatSink                        | Heat Sink                      | THM — Heat capture at the IT load                 | THM, CMP           |
| aidcf:ColdPlate                       | Cold Plate                     | THM — Heat capture at the IT load                 | THM, CMP           |
| aidcf:ImmersionTank                   | Immersion Tank                 | THM — Heat capture at the IT load                 | THM, CMP           |
| aidcf:CDU                             | CDU                            | THM — Coolant distribution                        | THM                |
| aidcf:PrimaryLoop                     | Primary Loop                   | THM — Coolant distribution                        | THM                |
| aidcf:SecondaryLoop                   | Secondary Loop                 | THM — Coolant distribution                        | THM                |
| aidcf:Pump                            | Pump                           | THM — Coolant distribution                        | THM                |
| aidcf:Manifold                        | Manifold                       | THM — Coolant distribution                        | THM                |
| aidcf:QuickDisconnect                 | Quick Disconnect               | THM — Coolant distribution                        | THM                |
| aidcf:Hose                            | Hose                           | THM — Coolant distribution                        | THM                |
| aidcf:Pipe                            | Pipe                           | THM — Coolant distribution                        | THM                |
| aidcf:HeatExchanger                   | Heat Exchanger                 | THM — Coolant distribution                        | THM                |
| aidcf:Chiller                         | Chiller                        | THM — Heat rejection                              | THM                |
| aidcf:CoolingTower                    | Cooling Tower                  | THM — Heat rejection                              | THM, ENV           |
| aidcf:DryCooler                       | Dry Cooler                     | THM — Heat rejection                              | THM                |
| aidcf:Condenser                       | Condenser                      | THM — Heat rejection                              | THM                |
| aidcf:EvaporativeSystem               | Evaporative System             | THM — Heat rejection                              | THM, ENV           |
| aidcf:HeatReuseInterface              | Heat-Reuse Interface           | THM — Heat rejection                              | THM, ENV           |
| aidcf:WaterSource                     | Water Source                   | THM — Fluid, water and leak management            | THM, ENV, DEP      |
| aidcf:Pipework                        | Pipework                       | THM — Fluid, water and leak management            | THM                |
| aidcf:Valve                           | Valve                          | THM — Fluid, water and leak management            | THM                |
| aidcf:Drain                           | Drain                          | THM — Fluid, water and leak management            | THM                |
| aidcf:Sump                            | Sump                           | THM — Fluid, water and leak management            | THM                |
| aidcf:Drainage                        | Drainage                       | THM — Fluid, water and leak management            | THM                |
| aidcf:LeakDetectionZone               | Leak Detection Zone            | THM — Fluid, water and leak management            | THM                |
| aidcf:WaterTreatmentSystem            | Water Treatment System         | THM — Fluid, water and leak management            | THM, ENV           |
| aidcf:TemperatureSensor               | Temperature Sensor             | THM — Thermal and leak monitoring                 | THM                |
| aidcf:HumiditySensor                  | Humidity Sensor                | THM — Thermal and leak monitoring                 | THM, ENV           |
| aidcf:FlowSensor                      | Flow Sensor                    | THM — Thermal and leak monitoring                 | THM                |
| aidcf:PressureSensor                  | Pressure Sensor                | THM — Thermal and leak monitoring                 | THM                |
| aidcf:LeakSensor                      | Leak Sensor                    | THM — Thermal and leak monitoring                 | THM                |
| aidcf:CoolantQualitySensor            | Coolant Quality Sensor         | THM — Thermal and leak monitoring                 | THM                |
| aidcf:ThermalCamera                   | Thermal Camera                 | THM — Thermal and leak monitoring                 | THM                |
| aidcf:GridElectricity                 | Grid Electricity               | ENV — Energy resources                            | ENV, POW           |
| aidcf:RenewableElectricity            | Renewable Electricity          | ENV — Energy resources                            | ENV, POW           |
| aidcf:OnSiteEnergy                    | On-Site Energy                 | ENV — Energy resources                            | ENV, POW           |
| aidcf:StoredEnergy                    | Stored Energy                  | ENV — Energy resources                            | ENV, POW           |
| aidcf:Fuel                            | Fuel                           | ENV — Energy resources                            | ENV, POW           |
| aidcf:PotableWater                    | Potable Water                  | ENV — Water resources                             | ENV                |
| aidcf:ProcessWater                    | Process Water                  | ENV — Water resources                             | ENV, THM           |
| aidcf:ReclaimedWater                  | Reclaimed Water                | ENV — Water resources                             | ENV                |
| aidcf:CoolingWater                    | Cooling Water                  | ENV — Water resources                             | ENV, THM           |
| aidcf:DischargeWater                  | Discharge Water                | ENV — Water resources                             | ENV                |
| aidcf:AmbientTemperature              | Ambient Temperature            | ENV — Environmental conditions                    | ENV, THM           |
| aidcf:Humidity                        | Humidity                       | ENV — Environmental conditions                    | ENV, THM           |
| aidcf:AirQuality                      | Air Quality                    | ENV — Environmental conditions                    | ENV                |
| aidcf:ParticulateLevel                | Particulate Level              | ENV — Environmental conditions                    | ENV                |
| aidcf:Noise                           | Noise                          | ENV — Environmental conditions                    | ENV                |
| aidcf:Vibration                       | Vibration                      | ENV — Environmental conditions                    | ENV, PHY           |
| aidcf:FloodExposure                   | Flood Exposure                 | ENV — Environmental conditions                    | ENV, PHY           |
| aidcf:HeatStress                      | Heat Stress                    | ENV — Environmental conditions                    | ENV, THM           |
| aidcf:Refrigerant                     | Refrigerant                    | ENV — Material and chemical resources             | ENV, THM           |
| aidcf:Coolant                         | Coolant                        | ENV — Material and chemical resources             | ENV, THM           |
| aidcf:FireSuppressant                 | Fire Suppressant               | ENV — Material and chemical resources             | ENV, PHY           |
| aidcf:BatteryChemistry                | Battery Chemistry              | ENV — Material and chemical resources             | ENV, POW, PHY      |
| aidcf:HazardousMaterial               | Hazardous Material             | ENV — Material and chemical resources             | ENV, PHY           |
| aidcf:PUERecord                       | PUE Record                     | ENV — Performance indicators                      | ENV                |
| aidcf:WUERecord                       | WUE Record                     | ENV — Performance indicators                      | ENV                |
| aidcf:CUERecord                       | CUE Record                     | ENV — Performance indicators                      | ENV                |
| aidcf:EnergyReuseRecord               | Energy Reuse Record            | ENV — Performance indicators                      | ENV                |
| aidcf:CoolingEfficiencyRecord         | Cooling Efficiency Record      | ENV — Performance indicators                      | ENV, THM           |
| aidcf:ComputeUtilisationRecord        | Compute Utilisation Record     | ENV — Performance indicators                      | ENV, CMP           |
| aidcf:Permit                          | Permit                         | ENV — Environmental obligations                   | ENV, GOV           |
| aidcf:ReportingRequirement            | Reporting Requirement          | ENV — Environmental obligations                   | ENV, GOV           |
| aidcf:EmissionLimit                   | Emission Limit                 | ENV — Environmental obligations                   | ENV                |
| aidcf:WaterLimit                      | Water Limit                    | ENV — Environmental obligations                   | ENV                |
| aidcf:WasteRequirement                | Waste Requirement              | ENV — Environmental obligations                   | ENV                |
| aidcf:EnvironmentalCommitment         | Environmental Commitment       | ENV — Environmental obligations                   | ENV, GOV           |
| aidcf:Accelerator                     | Accelerator                    | CMP — Accelerated compute                         | CMP                |
| aidcf:GPU                             | GPU                            | CMP — Accelerated compute                         | CMP                |
| aidcf:AIASIC                          | AI ASIC                        | CMP — Accelerated compute                         | CMP                |
| aidcf:ComputeNode                     | Compute Node                   | CMP — Accelerated compute                         | CMP                |
| aidcf:GPUBaseboard                    | GPU Baseboard                  | CMP — Accelerated compute                         | CMP                |
| aidcf:CPU                             | CPU                            | CMP — Accelerated compute                         | CMP                |
| aidcf:Memory                          | Memory                         | CMP — Accelerated compute                         | CMP                |
| aidcf:DPU                             | DPU                            | CMP — Accelerated compute                         | CMP, NET           |
| aidcf:NIC                             | NIC                            | CMP — Accelerated compute                         | CMP, NET           |
| aidcf:ComputeTray                     | Compute Tray                   | CMP — Rack-scale systems                          | CMP                |
| aidcf:RackScaleSystem                 | Rack-Scale System              | CMP — Rack-scale systems                          | CMP, PHY, POW, THM |
| aidcf:ScaleUpDomain                   | Scale-Up Domain                | CMP — Rack-scale systems                          | CMP, NET           |
| aidcf:NVLinkDomain                    | NVLink Domain                  | CMP — Rack-scale systems                          | CMP, NET           |
| aidcf:Enclosure                       | Enclosure                      | CMP — Rack-scale systems                          | CMP                |
| aidcf:Backplane                       | Backplane                      | CMP — Rack-scale systems                          | CMP                |
| aidcf:PowerShelf                      | Power Shelf                    | CMP — Rack-scale systems                          | CMP, POW           |
| aidcf:RackController                  | Rack Controller                | CMP — Rack-scale systems                          | CMP, SEC           |
| aidcf:ComputeCluster                  | Compute Cluster                | CMP — Cluster systems                             | CMP                |
| aidcf:ClusterPartition                | Cluster Partition              | CMP — Cluster systems                             | CMP                |
| aidcf:NodePool                        | Node Pool                      | CMP — Cluster systems                             | CMP                |
| aidcf:HeadNode                        | Head Node                      | CMP — Cluster systems                             | CMP                |
| aidcf:LoginNode                       | Login Node                     | CMP — Cluster systems                             | CMP, SEC           |
| aidcf:ManagementNode                  | Management Node                | CMP — Cluster systems                             | CMP, SEC           |
| aidcf:ProvisioningNode                | Provisioning Node              | CMP — Cluster systems                             | CMP                |
| aidcf:BMC                             | BMC                            | CMP — Management and firmware                     | CMP, SEC           |
| aidcf:Firmware                        | Firmware                       | CMP — Management and firmware                     | CMP, SUP, SEC      |
| aidcf:BIOS                            | BIOS                           | CMP — Management and firmware                     | CMP, SEC           |
| aidcf:Driver                          | Driver                         | CMP — Management and firmware                     | CMP, SUP           |
| aidcf:ClusterManager                  | Cluster Manager                | CMP — Management and firmware                     | CMP, SEC           |
| aidcf:ProvisioningService             | Provisioning Service           | CMP — Management and firmware                     | CMP                |
| aidcf:Scheduler                       | Scheduler                      | CMP — Management and firmware                     | CMP                |
| aidcf:Orchestrator                    | Orchestrator                   | CMP — Management and firmware                     | CMP                |
| aidcf:Queue                           | Queue                          | CMP — Workload infrastructure                     | CMP                |
| aidcf:SchedulerPartition              | Scheduler Partition †          | CMP — Workload infrastructure                     | CMP                |
| aidcf:Reservation                     | Reservation                    | CMP — Workload infrastructure                     | CMP                |
| aidcf:ContainerRuntime                | Container Runtime              | CMP — Workload infrastructure                     | CMP                |
| aidcf:KubernetesCluster               | Kubernetes Cluster             | CMP — Workload infrastructure                     | CMP                |
| aidcf:JobScheduler                    | Job Scheduler                  | CMP — Workload infrastructure                     | CMP                |
| aidcf:CheckpointAgent                 | Checkpoint Agent               | CMP — Workload infrastructure                     | CMP, STO           |
| aidcf:GPUTelemetry                    | GPU Telemetry                  | CMP — Compute observability                       | CMP                |
| aidcf:NodeTelemetry                   | Node Telemetry                 | CMP — Compute observability                       | CMP                |
| aidcf:HealthService                   | Health Service                 | CMP — Compute observability                       | CMP                |
| aidcf:PerformanceCounter              | Performance Counter            | CMP — Compute observability                       | CMP                |
| aidcf:ErrorCounter                    | Error Counter                  | CMP — Compute observability                       | CMP                |
| aidcf:GoldenImage                     | Golden Image                   | CMP — Compute lifecycle                           | CMP, RES           |
| aidcf:FirmwareBaseline                | Firmware Baseline              | CMP — Compute lifecycle                           | CMP, SUP           |
| aidcf:CompatibilityMatrix             | Compatibility Matrix           | CMP — Compute lifecycle                           | CMP                |
| aidcf:HardwareSupportContract         | Hardware Support Contract      | CMP — Compute lifecycle                           | CMP, SUP           |
| aidcf:RMAProcess                      | RMA Process                    | CMP — Compute lifecycle                           | CMP, SUP           |
| aidcf:SecureDecommissioningRecord     | Secure Decommissioning Record  | CMP — Compute lifecycle                           | CMP, PHY, EVA      |
| aidcf:ParallelFileSystem              | Parallel File System           | STO — Storage systems                             | STO                |
| aidcf:ScaleOutNAS                     | Scale-Out NAS                  | STO — Storage systems                             | STO                |
| aidcf:ObjectStorage                   | Object Storage                 | STO — Storage systems                             | STO                |
| aidcf:BlockStorage                    | Block Storage                  | STO — Storage systems                             | STO                |
| aidcf:LocalNVMe                       | Local NVMe                     | STO — Storage systems                             | STO, CMP           |
| aidcf:BurstBuffer                     | Burst Buffer                   | STO — Storage systems                             | STO                |
| aidcf:ArchiveStorage                  | Archive Storage                | STO — Storage systems                             | STO                |
| aidcf:StorageNode                     | Storage Node                   | STO — Storage nodes and media                     | STO                |
| aidcf:MetadataServer                  | Metadata Server                | STO — Storage nodes and media                     | STO                |
| aidcf:ObjectStorageNode               | Object Storage Node            | STO — Storage nodes and media                     | STO                |
| aidcf:Controller                      | Controller                     | STO — Storage nodes and media                     | STO                |
| aidcf:SSD                             | SSD                            | STO — Storage nodes and media                     | STO                |
| aidcf:HDD                             | HDD                            | STO — Storage nodes and media                     | STO                |
| aidcf:Tape                            | Tape                           | STO — Storage nodes and media                     | STO                |
| aidcf:NVRAM                           | NVRAM                          | STO — Storage nodes and media                     | STO                |
| aidcf:Namespace                       | Namespace                      | STO — Data-path services                          | STO                |
| aidcf:MetadataService                 | Metadata Service               | STO — Data-path services                          | STO                |
| aidcf:DataMover                       | Data Mover                     | STO — Data-path services                          | STO                |
| aidcf:Cache                           | Cache                          | STO — Data-path services                          | STO                |
| aidcf:DataPathGateway                 | Data-Path Gateway †            | STO — Data-path services                          | STO                |
| aidcf:ClientDriver                    | Client Driver                  | STO — Data-path services                          | STO                |
| aidcf:MountService                    | Mount Service                  | STO — Data-path services                          | STO                |
| aidcf:DatasetRepository               | Dataset Repository             | STO — AI artifact services                        | STO                |
| aidcf:ModelRepository                 | Model Repository               | STO — AI artifact services                        | STO                |
| aidcf:CheckpointRepository            | Checkpoint Repository          | STO — AI artifact services                        | STO, RES           |
| aidcf:FeatureStore                    | Feature Store                  | STO — AI artifact services                        | STO                |
| aidcf:ArtifactRegistry                | Artifact Registry              | STO — AI artifact services                        | STO                |
| aidcf:Snapshot                        | Snapshot                       | STO — Protection and recovery                     | STO, RES           |
| aidcf:Replica                         | Replica                        | STO — Protection and recovery                     | STO, RES           |
| aidcf:BackupCopy                      | Backup Copy                    | STO — Protection and recovery                     | STO, RES           |
| aidcf:ErasureCodingGroup              | Erasure Coding Group           | STO — Protection and recovery                     | STO                |
| aidcf:RecoveryCopy                    | Recovery Copy                  | STO — Protection and recovery                     | STO, RES           |
| aidcf:ImmutableCopy                   | Immutable Copy                 | STO — Protection and recovery                     | STO, RES, SEC      |
| aidcf:StorageManager                  | Storage Manager                | STO — Storage management                          | STO, SEC           |
| aidcf:CapacityManager                 | Capacity Manager               | STO — Storage management                          | STO                |
| aidcf:TieringPolicy                   | Tiering Policy                 | STO — Storage management                          | STO                |
| aidcf:RetentionPolicy                 | Retention Policy               | STO — Storage management                          | STO, EVA           |
| aidcf:IntegrityScanner                | Integrity Scanner              | STO — Storage management                          | STO                |
| aidcf:TelemetryService                | Telemetry Service              | STO — Storage management                          | STO                |
| aidcf:IngestionInterface              | Ingestion Interface            | STO — Data logistics interfaces                   | STO                |
| aidcf:ExportInterface                 | Export Interface               | STO — Data logistics interfaces                   | STO                |
| aidcf:DataTransferNode                | Data Transfer Node             | STO — Data logistics interfaces                   | STO, NET           |
| aidcf:WANTransferService              | WAN Transfer Service           | STO — Data logistics interfaces                   | STO, NET, DEP      |
| aidcf:DataStagingArea                 | Data Staging Area †            | STO — Data logistics interfaces                   | STO                |
| aidcf:ScaleUpFabric                   | Scale-Up Fabric                | NET — Scale-up interconnect                       | NET, CMP           |
| aidcf:SwitchFabric                    | Switch Fabric                  | NET — Scale-up interconnect                       | NET                |
| aidcf:InterconnectLink                | Interconnect Link              | NET — Scale-up interconnect                       | NET                |
| aidcf:TopologyDomain                  | Topology Domain                | NET — Scale-up interconnect                       | NET                |
| aidcf:InfiniBandFabric                | InfiniBand Fabric              | NET — Scale-out compute fabric                    | NET                |
| aidcf:EthernetAIFabric                | Ethernet AI Fabric             | NET — Scale-out compute fabric                    | NET                |
| aidcf:RoCEFabric                      | RoCE Fabric                    | NET — Scale-out compute fabric                    | NET                |
| aidcf:ComputeLeaf                     | Compute Leaf                   | NET — Scale-out compute fabric                    | NET                |
| aidcf:ComputeSpine                    | Compute Spine                  | NET — Scale-out compute fabric                    | NET                |
| aidcf:FabricManager                   | Fabric Manager                 | NET — Scale-out compute fabric                    | NET, CMP, SEC      |
| aidcf:StorageNetwork                  | Storage Network                | NET — Storage fabric                              | NET, STO           |
| aidcf:StorageLeaf                     | Storage Leaf                   | NET — Storage fabric                              | NET, STO           |
| aidcf:StorageSpine                    | Storage Spine                  | NET — Storage fabric                              | NET, STO           |
| aidcf:SANFabric                       | SAN Fabric                     | NET — Storage fabric                              | NET, STO           |
| aidcf:StorageGateway                  | Storage Gateway                | NET — Storage fabric                              | NET, STO           |
| aidcf:FrontendNetwork                 | Frontend Network               | NET — Frontend and service network                | NET                |
| aidcf:LoadBalancer                    | Load Balancer                  | NET — Frontend and service network                | NET                |
| aidcf:ServiceGateway                  | Service Gateway                | NET — Frontend and service network                | NET                |
| aidcf:EdgeRouter                      | Edge Router                    | NET — Frontend and service network                | NET, DEP           |
| aidcf:Firewall                        | Firewall                       | NET — Frontend and service network                | NET, SEC           |
| aidcf:APINetwork                      | API Network                    | NET — Frontend and service network                | NET                |
| aidcf:ManagementNetwork               | Management Network             | NET — Management and control network              | NET, SEC           |
| aidcf:OutOfBandNetwork                | Out-of-Band Network            | NET — Management and control network              | NET, SEC, RES      |
| aidcf:ConsoleServer                   | Console Server                 | NET — Management and control network              | NET, SEC           |
| aidcf:ManagementSwitch                | Management Switch              | NET — Management and control network              | NET                |
| aidcf:JumpService                     | Jump Service                   | NET — Management and control network              | NET, SEC           |
| aidcf:TimeService                     | Time Service                   | NET — Timing and core services                    | NET                |
| aidcf:DNSService                      | DNS Service                    | NET — Timing and core services                    | NET                |
| aidcf:DHCPService                     | DHCP Service                   | NET — Timing and core services                    | NET                |
| aidcf:IPAMService                     | IPAM Service                   | NET — Timing and core services                    | NET                |
| aidcf:CertificateService              | Certificate Service            | NET — Timing and core services                    | NET, SEC           |
| aidcf:AuthenticationService           | Authentication Service         | NET — Timing and core services                    | NET, SEC           |
| aidcf:Cable                           | Cable                          | NET — Physical connectivity                       | NET, PHY           |
| aidcf:OpticalFibre                    | Optical Fibre                  | NET — Physical connectivity                       | NET                |
| aidcf:CopperLink                      | Copper Link                    | NET — Physical connectivity                       | NET                |
| aidcf:Transceiver                     | Transceiver                    | NET — Physical connectivity                       | NET                |
| aidcf:PatchPanel                      | Patch Panel                    | NET — Physical connectivity                       | NET                |
| aidcf:MeetMeRoom                      | Meet-Me Room                   | NET — Physical connectivity                       | NET, PHY, DEP      |
| aidcf:CrossConnect                    | Cross-Connect                  | NET — Physical connectivity                       | NET, DEP           |
| aidcf:FlowTelemetry                   | Flow Telemetry                 | NET — Network observability                       | NET                |
| aidcf:FabricTelemetry                 | Fabric Telemetry               | NET — Network observability                       | NET                |
| aidcf:PacketCaptureService            | Packet Capture Service         | NET — Network observability                       | NET, SEC           |
| aidcf:NetworkController               | Network Controller             | NET — Network observability                       | NET, SEC           |
| aidcf:CongestionMonitor               | Congestion Monitor             | NET — Network observability                       | NET                |
| aidcf:PathMonitor                     | Path Monitor                   | NET — Network observability                       | NET                |
| aidcf:Procedure                       | Procedure                      | OPS — Work control                                | OPS                |
| aidcf:MethodStatement                 | Method Statement               | OPS — Work control                                | OPS                |
| aidcf:PermitToWork                    | Permit to Work                 | OPS — Work control                                | OPS, PHY           |
| aidcf:LockoutTagout                   | Lockout Tagout                 | OPS — Work control                                | OPS, POW, PHY      |
| aidcf:MaintenanceWindow               | Maintenance Window             | OPS — Work control                                | OPS                |
| aidcf:ChangeRecord                    | Change Record                  | OPS — Work control                                | OPS                |
| aidcf:TemporaryConfiguration          | Temporary Configuration        | OPS — Work control                                | OPS                |
| aidcf:MaintenancePlan                 | Maintenance Plan               | OPS — Maintenance and reliability                 | OPS                |
| aidcf:WorkOrder                       | Work Order                     | OPS — Maintenance and reliability                 | OPS                |
| aidcf:ConditionMonitoring             | Condition Monitoring           | OPS — Maintenance and reliability                 | OPS                |
| aidcf:Inspection                      | Inspection                     | OPS — Maintenance and reliability                 | OPS                |
| aidcf:Calibration                     | Calibration                    | OPS — Maintenance and reliability                 | OPS, EVA           |
| aidcf:SparePart                       | Spare Part                     | OPS — Maintenance and reliability                 | OPS, SUP           |
| aidcf:ObsolescenceRecord              | Obsolescence Record            | OPS — Maintenance and reliability                 | OPS, SUP           |
| aidcf:Shift                           | Shift                          | OPS — Staffing and competence                     | OPS                |
| aidcf:Roster                          | Roster                         | OPS — Staffing and competence                     | OPS                |
| aidcf:CompetencyRecord                | Competency Record              | OPS — Staffing and competence                     | OPS, GOV           |
| aidcf:Authorisation                   | Authorisation                  | OPS — Staffing and competence                     | OPS                |
| aidcf:TrainingRecord                  | Training Record                | OPS — Staffing and competence                     | OPS                |
| aidcf:Contractor                      | Contractor                     | OPS — Staffing and competence                     | OPS, SUP           |
| aidcf:SubjectMatterExpert             | Subject Matter Expert          | OPS — Staffing and competence                     | OPS                |
| aidcf:Alarm                           | Alarm                          | OPS — Alarm and incident                          | OPS                |
| aidcf:Incident                        | Incident                       | OPS — Alarm and incident                          | OPS, RES           |
| aidcf:EventLog                        | Event Log                      | OPS — Alarm and incident                          | OPS, CMP, SEC, EVA |
| aidcf:PostIncidentReview              | Post-Incident Review           | OPS — Alarm and incident                          | OPS, RES           |
| aidcf:ConfigurationBaseline           | Configuration Baseline         | OPS — Configuration and documentation             | OPS, SEC           |
| aidcf:AssetRegister                   | Asset Register                 | OPS — Configuration and documentation             | OPS, DEP           |
| aidcf:DrawingRegister                 | Drawing Register               | OPS — Configuration and documentation             | OPS                |
| aidcf:ProcedureRegister               | Procedure Register             | OPS — Configuration and documentation             | OPS                |
| aidcf:Revision                        | Revision                       | OPS — Configuration and documentation             | OPS                |
| aidcf:DocumentCustodian               | Document Custodian             | OPS — Configuration and documentation             | OPS, EVA           |
| aidcf:BMS                             | BMS                            | OPS — Facility monitoring and control             | OPS, THM, SEC      |
| aidcf:SCADA                           | SCADA                          | OPS — Facility monitoring and control             | OPS, POW, THM, SEC |
| aidcf:PLC                             | PLC                            | OPS — Facility monitoring and control             | OPS, THM, POW, SEC |
| aidcf:RTU                             | RTU                            | OPS — Facility monitoring and control             | OPS, POW, SEC      |
| aidcf:Sensor                          | Sensor                         | OPS — Facility monitoring and control             | OPS, THM, POW      |
| aidcf:Actuator                        | Actuator                       | OPS — Facility monitoring and control             | OPS, THM, POW      |
| aidcf:ControlSystemGateway            | Control-System Gateway †       | OPS — Facility monitoring and control             | OPS, SEC, NET      |
| aidcf:Historian                       | Historian                      | OPS — Facility monitoring and control             | OPS, EVA, SEC      |
| aidcf:AlarmConsole                    | Alarm Console                  | OPS — Facility monitoring and control             | OPS                |
| aidcf:EmergencyProcedure              | Emergency Procedure            | RES — Continuity and emergency response           | RES, OPS           |
| aidcf:CrisisTeam                      | Crisis Team                    | RES — Continuity and emergency response           | RES, GOV           |
| aidcf:Exercise                        | Exercise                       | RES — Continuity and emergency response           | RES, EVA           |
| aidcf:ContinuityPlan                  | Continuity Plan †              | RES — Continuity and emergency response           | RES                |
| aidcf:RecoveryPlan                    | Recovery Plan †                | RES — Continuity and emergency response           | RES                |
| aidcf:AlternativeCapacity             | Alternative Capacity †         | RES — Continuity and emergency response           | RES, CAP, DEP      |
| aidcf:Supplier                        | Supplier                       | SUP — Supplier and service management             | SUP, DEP           |
| aidcf:MaintenanceContract             | Maintenance Contract           | SUP — Supplier and service management             | SUP, OPS           |
| aidcf:ServiceLevel                    | Service Level                  | SUP — Supplier and service management             | SUP, DEP           |
| aidcf:RemoteSupport                   | Remote Support                 | SUP — Supplier and service management             | SUP, SEC           |
| aidcf:EscalationContact               | Escalation Contact             | SUP — Supplier and service management             | SUP, OPS           |
| aidcf:LeadTime                        | Lead Time                      | SUP — Supplier and service management             | SUP                |
| aidcf:SupplyConstraint                | Supply Constraint              | SUP — Supplier and service management             | SUP, DEP           |
| aidcf:SoftwareRelease                 | Software Release †             | SUP — Provenance and software supply              | SUP                |
| aidcf:SignatureRecord                 | Signature Record †             | SUP — Provenance and software supply              | SUP, SEC           |
| aidcf:SoftwareBillOfMaterials         | Software Bill of Materials †   | SUP — Provenance and software supply              | SUP, SEC           |
| aidcf:ComponentProvenanceRecord       | Component Provenance Record †  | SUP — Provenance and software supply              | SUP, EVA           |
| aidcf:IdentityProvider                | Identity Provider †            | SEC — Identity and privileged access              | SEC                |
| aidcf:HumanIdentity                   | Human Identity †               | SEC — Identity and privileged access              | SEC                |
| aidcf:MachineIdentity                 | Machine Identity †             | SEC — Identity and privileged access              | SEC                |
| aidcf:PrivilegedAccessService         | Privileged Access Service †    | SEC — Identity and privileged access              | SEC                |
| aidcf:BreakGlassAccount               | Break-Glass Account †          | SEC — Identity and privileged access              | SEC, RES           |
| aidcf:RemoteAccessGateway             | Remote Access Gateway †        | SEC — Identity and privileged access              | SEC, NET, SUP      |
| aidcf:SecurityTelemetryService        | Security Telemetry Service †   | SEC — Security monitoring and response            | SEC, EVA           |
| aidcf:SecurityIncident                | Security Incident †            | SEC — Security monitoring and response            | SEC, OPS, RES      |
| aidcf:VulnerabilityRecord             | Vulnerability Record †         | SEC — Security monitoring and response            | SEC, SUP           |
| aidcf:AutomationAgent                 | Automation Agent †             | SEC — Automated and AI-enabled action             | SEC, OPS           |
| aidcf:CommandAllowlist                | Command Allowlist †            | SEC — Automated and AI-enabled action             | SEC                |
| aidcf:ApprovalWorkflow                | Approval Workflow †            | SEC — Automated and AI-enabled action             | SEC, GOV           |

## A.3 Assurance-chain classes

Defined in Part XV (§68). All carry the primary domain code EVA because they are governed by EVA-01 to EVA-06; Control Domain, Control Family and Control are additionally the organising classes of every domain.

| **Canonical ID**             | **Preferred label**     | **Domain code(s)** | **AIDCF-014 class**                                                |
|------------------------------|-------------------------|--------------------|--------------------------------------------------------------------|
| aidcf:ControlDomain          | Control Domain          | EVA (all domains)  | ControlDomain                                                      |
| aidcf:ControlFamily          | Control Family          | EVA (all domains)  | ControlFamily                                                      |
| aidcf:Control                | Control                 | EVA (all domains)  | Control                                                            |
| aidcf:EvidenceRequirement    | Evidence Requirement    | EVA                | EvidenceRequirement                                                |
| aidcf:EvidenceObject         | Evidence Object         | EVA                | EvidenceObject                                                     |
| aidcf:EvidencePackage        | Evidence Package        | EVA                | EvidencePackage                                                    |
| aidcf:Assertion              | Assertion               | EVA                | — (assertionRefs; AIDCF-014 Assertion vocabulary)                  |
| aidcf:ControlAssessment      | Control Assessment      | EVA                | ControlAssessment                                                  |
| aidcf:Finding                | Finding                 | EVA                | Finding                                                            |
| aidcf:UnknownRecord          | UNKNOWN Record          | EVA                | UnknownRecord                                                      |
| aidcf:CriticalGate           | Critical Gate           | EVA, GOV           | CriticalGate                                                       |
| aidcf:GateResult             | Gate Result             | EVA                | GateResult                                                         |
| aidcf:ScoreSnapshot          | Score Snapshot          | EVA                | ScoreSnapshot                                                      |
| aidcf:DecisionRecommendation | Decision Recommendation | EVA                | DecisionRecommendation                                             |
| aidcf:AssuranceDecision      | Assurance Decision      | EVA, GOV           | AssuranceDecision                                                  |
| aidcf:AssuranceStatement     | Assurance Statement     | EVA                | AssuranceStatement                                                 |
| aidcf:AssuranceReport        | Assurance Report        | EVA                | AssuranceReport                                                    |
| aidcf:ReassessmentTrigger    | Reassessment Trigger    | EVA                | ReassessmentTrigger                                                |
| aidcf:DecisionQuestion       | Decision Question       | EVA, GOV           | — (decisionQuestion attribute of Assessment and AssuranceDecision) |

## A.4 Industrial automation and control system security classes

Defined in Part XVI (§72).

| **Canonical ID**              | **Preferred label**                             | **Domain code(s)** | **AIDCF-014 class**                                       |
|-------------------------------|-------------------------------------------------|--------------------|-----------------------------------------------------------|
| aidcf:IACS                    | Industrial Automation and Control System (IACS) | SEC, OPS, POW, THM | InfrastructureSystem (systemType = IACS)                  |
| aidcf:IACSZone                | Zone (IEC 62443)                                | SEC                | — (InfrastructureSystem grouping, systemType = IACS_ZONE) |
| aidcf:Conduit                 | Conduit (IEC 62443)                             | SEC, NET           | Interface (interfaceType = IACS_CONDUIT)                  |
| aidcf:SecurityLevel           | Security Level                                  | SEC                | — (attribute vector on Zone/Conduit/Component)            |
| aidcf:FoundationalRequirement | Foundational Requirement                        | SEC                | — (controlled vocabulary FR1–FR7)                         |

## A.5 Aliases and disambiguation

| **Term**                                       | **Treatment**                                                                                                                                         |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| CriticalFunction (v1.0)                        | Replaced by aidcf:RequiredFunction.                                                                                                                   |
| AgentSystem (v1.0)                             | Renamed aidcf:SuppressionAgentSystem to avoid confusion with AI agents (aidcf:AutomationAgent).                                                       |
| Gateway (v1.0, two uses)                       | Split into aidcf:ControlSystemGateway (OPS/SEC) and aidcf:DataPathGateway (STO).                                                                      |
| Partition (v1.0)                               | Renamed aidcf:SchedulerPartition; distinct from aidcf:ClusterPartition (hardware/cluster subdivision).                                                |
| Staging Area                                   | aidcf:StagingArea is a physical area (PHY); aidcf:DataStagingArea is a data-logistics location (STO).                                                 |
| Security Zone                                  | aidcf:SecurityZone is a physical access zone (PHY); aidcf:IACSZone is an IEC 62443 zone (SEC). A physical zone may bound an IACS zone but is not one. |
| Transformer, Role, Event Log (v1.0 duplicates) | Each now registered once with multiple domain codes.                                                                                                  |
| Grounding / Earthing System                    | aidcf:Grounding is retained as a regional synonym label of aidcf:EarthingSystem; implementations should emit EarthingSystem.                          |
| Relay / Protection Relay                       | aidcf:ProtectionRelay is a protective relay; aidcf:Relay is an auxiliary or control relay without a protection function.                              |
| NVLink Domain, Kubernetes Cluster              | Product-specific specialisations of aidcf:ScaleUpDomain and aidcf:Orchestrator respectively (IOT-REQ-013).                                            |

# Appendix B - Canonical relationship registry

Ontology predicates are listed with their logic and with the AIDCF-014 §9 relationship type used for exchange (see the exchange requirement in §34). Assurance-chain relationships are listed in §70.

| **Predicate**            | **Subject**         | **Object**                 | **Logic**                                         | **Inverse**              | **Meaning**                             | **AIDCF-014 exchange type**                                                          |
|--------------------------|---------------------|----------------------------|---------------------------------------------------|--------------------------|-----------------------------------------|--------------------------------------------------------------------------------------|
| PART_OF                  | Entity              | Entity                     | Transitive                                        | HAS_PART                 | Composition.                            | COMPOSED_OF (inverse)                                                                |
| CONTAINS                 | Location/System     | Entity                     | Transitive                                        | LOCATED_IN / PART_OF     | Containment.                            | COMPOSED_OF or LOCATED_IN (inverse)                                                  |
| LOCATED_IN               | Physical Entity     | Location                   | Transitive                                        | CONTAINS                 | Physical placement.                     | LOCATED_IN                                                                           |
| MEMBER_OF                | Entity              | Group                      | Not transitive                                    | HAS_MEMBER               | Group membership.                       | COMPOSED_OF (inverse, from the group)                                                |
| HAS_OUTCOME              | CapabilityInstance  | ServiceOutcome             | Not transitive                                    | —                        | Capability requires outcome.            | HAS_OUTCOME                                                                          |
| REQUIRES_FUNCTION        | ServiceOutcome      | RequiredFunction           | Not transitive                                    | —                        | Outcome depends on function.            | REQUIRES_FUNCTION                                                                    |
| IMPLEMENTED_BY           | RequiredFunction    | System/Asset               | Not transitive                                    | IMPLEMENTS               | Function realised by system or asset.   | IMPLEMENTED_BY                                                                       |
| INTERFACES_WITH          | Entity              | Entity                     | Symmetric                                         | INTERFACES_WITH          | Defined exchange boundary.              | CONNECTS_TO via an Interface record                                                  |
| CONNECTS_TO              | Entity              | Entity                     | Symmetric unless directed                         | CONNECTS_TO              | Realised connection.                    | CONNECTS_TO                                                                          |
| ROUTES_THROUGH           | Flow/Service        | Entity                     | Transitive along a path                           | CARRIES                  | Path relationship.                      | DEPENDS_ON (dependencyType = Network, path qualifier)                                |
| DEPENDS_ON               | Consumer entity     | Provider/entity/condition  | Directional; transitive for path tracing only     | None registered          | General reliance.                       | DEPENDS_ON                                                                           |
| POWERED_BY               | Load/system         | Electrical source/path     | Directional; transitive along the electrical path | None registered          | Electrical reliance.                    | DEPENDS_ON (dependencyType = Electrical); CONSUMES_RESOURCE for energy               |
| COOLED_BY                | Heat source/system  | Cooling system/path        | Directional; transitive along the heat path       | None registered          | Thermal reliance.                       | DEPENDS_ON (dependencyType = Thermal)                                                |
| SUPPLIED_BY              | Consumer            | Provider/resource          | Directional                                       | None registered          | Resource or service supply.             | CONSUMES_RESOURCE (resource) or DEPENDS_ON (service)                                 |
| CONTROLLED_BY            | Asset/system        | Controller/actor           | Directional                                       | None registered          | Operational or automated control.       | CONTROLLED_BY                                                                        |
| MONITORED_BY             | Entity              | Monitoring entity          | Directional                                       | None registered          | Visibility and detection reliance.      | MONITORED_BY                                                                         |
| PROTECTED_BY             | Entity              | Safeguard                  | Directional                                       | None registered          | Protective relationship.                | PROTECTED_BY                                                                         |
| AUTHENTICATED_BY         | Entity/service      | Identity service           | Directional                                       | None registered          | Identity reliance.                      | DEPENDS_ON (dependencyType = Identity)                                               |
| TIMED_BY                 | Entity/service      | Time source                | Directional                                       | None registered          | Timing reliance.                        | DEPENDS_ON (dependencyType = Timing)                                                 |
| CONFIGURED_BY            | Entity              | Configuration source/actor | Directional                                       | None registered          | Configuration reliance.                 | DEPENDS_ON (dependencyType = Configuration)                                          |
| RECOVERS_THROUGH         | Entity/capability   | Recovery asset/process     | Directional                                       | None registered          | Restoration reliance.                   | RECOVERS_THROUGH                                                                     |
| MAINTAINED_BY            | Entity              | Actor/organisation         | Directional                                       | None registered          | Maintenance reliance.                   | OPERATED_BY (role = maintainer)                                                      |
| OPERATED_BY              | Entity/system       | Actor/organisation         | Directional                                       | None registered          | Operational responsibility.             | OPERATED_BY                                                                          |
| EVIDENCED_BY             | Assertion/entity    | Evidence object            | Directional                                       | None registered          | Evidence support.                       | EVIDENCED_BY                                                                         |
| TESTED_BY                | Assertion/safeguard | Test record                | Directional                                       | None registered          | Validation link.                        | ASSESSED_BY (method = TEST)                                                          |
| SHARES_DEPENDENCY_WITH   | Entity              | Entity                     | Symmetric; derived                                | SHARES_DEPENDENCY_WITH   | Common provider exposure.               | Derived from two DEPENDS_ON to one provider; may be materialised as DEPENDS_ON pairs |
| SHARES_FAULT_DOMAIN_WITH | Entity              | Entity                     | Symmetric                                         | SHARES_FAULT_DOMAIN_WITH | Shared failure exposure.                | SHARES_FAULT_DOMAIN_WITH                                                             |
| DIVERSE_FROM             | Entity              | Entity                     | Symmetric; characteristic-specific                | DIVERSE_FROM             | Declared material difference.           | Assertion on the RedundancyGroup (no AIDCF-014 type)                                 |
| INDEPENDENT_OF           | Entity              | Entity                     | Symmetric; condition-bounded                      | INDEPENDENT_OF           | Evidence-bounded relevant independence. | Assertion with EVIDENCED_BY (no AIDCF-014 type)                                      |
| REDUNDANT_WITH           | Entity              | Entity                     | Symmetric within a RedundancyGroup                | REDUNDANT_WITH           | Alternative for a protected function.   | COMPOSED_OF from the RedundancyGroup                                                 |
| CONCENTRATES             | Entity              | Entity                     | Directional                                       | None registered          | Aggregates capability or consequence.   | Assertion on the Dependency (no AIDCF-014 type)                                      |
| SINGLE_POINT_FOR         | Entity              | Function/Outcome           | Directional                                       | None registered          | Unmitigated single-point relationship.  | Finding or Assertion referencing DEPENDS_ON (no AIDCF-014 type)                      |
| ISOLATED_FROM            | Entity              | Entity                     | Symmetric; hazard- or threat-specific             | ISOLATED_FROM            | Declared separation.                    | Assertion with EVIDENCED_BY (no AIDCF-014 type)                                      |

Legacy predicates: SUPPORTS (entity to outcome) is withdrawn in favour of HAS_OUTCOME / REQUIRES_FUNCTION / IMPLEMENTED_BY; IMPLEMENTS is the inverse of IMPLEMENTED_BY; CONNECTED_TO is renamed CONNECTS_TO; RECOVERED_BY is renamed RECOVERS_THROUGH; IN_SAME_FAULT_DOMAIN_AS is renamed SHARES_FAULT_DOMAIN_WITH.

# Appendix C - Minimum property schemas

## C.1 Capability Instance

| **Property**         | **Cardinality** | **Type**               |
|----------------------|-----------------|------------------------|
| capabilityInstanceId | 1               | Identifier             |
| name                 | 1               | String                 |
| capabilityType       | 1               | Controlled term        |
| owner                | 1               | Party                  |
| lifecycleStage       | 1               | Enumeration            |
| serviceOutcomes      | 1..\*           | ServiceOutcome         |
| criticality          | 1..\*           | Criticality            |
| assessmentBoundary   | 1               | Boundary               |
| operatingEnvelope    | 1               | Envelope               |
| architectureBaseline | 1..\*           | Document/Configuration |
| effectivePeriod      | 1               | Temporal interval      |
| evidenceStatus       | 1               | Evidence status (§53)  |

## C.2 Dependency

| **Property**        | **Cardinality** | **Type**          |
|---------------------|-----------------|-------------------|
| dependencyId        | 1               | Identifier        |
| consumer            | 1               | Entity            |
| provider            | 1               | Entity or UNKNOWN |
| dependencyType      | 1               | Controlled term   |
| strength            | 1               | Enumeration       |
| applicableStates    | 1..\*           | OperatingState    |
| capacityRequirement | 0..\*           | CapacityAssertion |
| substitutability    | 0..1            | Enumeration       |
| owner               | 1               | Party or UNKNOWN  |
| evidence            | 0..\*           | EvidenceObject    |
| evidenceStatus      | 1               | Evidence status   |
| confidence          | 0..1            | CONF-0..CONF-4    |
| validity            | 1               | Temporal interval |

## C.3 Evidence Object

| **Property**         | **Cardinality** | **Type**          |
|----------------------|-----------------|-------------------|
| evidenceId           | 1               | Identifier        |
| title                | 1               | String            |
| evidenceClass        | 1               | E1–E7 (AIDCF-008) |
| source               | 1               | Source            |
| custodian            | 1               | Party             |
| collectionMethod     | 1               | Controlled term   |
| observationTime      | 1               | Date/time         |
| effectivePeriod      | 0..1            | Temporal interval |
| scope                | 1               | Entity set        |
| integrity            | 1               | I0–I5 (AIDCF-008) |
| qualityBand          | 1               | Q0–Q5 (AIDCF-008) |
| supportsOrChallenges | 1..\*           | Assertion         |
| limitations          | 0..\*           | String            |
| reviewer             | 0..1            | Party             |
| evidenceStatus       | 1               | Evidence status   |

# Appendix D - Naming, identifier and namespace rules

- Use singular nouns for classes and active predicates for relationships.

- Avoid acronyms as canonical labels unless universally necessary; retain aliases separately.

- Record regional spellings as labels without creating duplicate semantic classes.

- Keep metrics and units separate from values.

- Do not encode confidentiality, location or owner in public identifiers.

- Use explicit version metadata for vocabularies, schemas and profiles.

- Mark deprecated terms with replacement mappings and retirement rationale.

- Maintain a collision register for extensions and imported vocabularies.

# Appendix E - Standards and reference-source map

The sources below informed scope comparisons and terminology analysis. AIDCF does not reproduce proprietary requirements and does not claim conformity with a referenced standard merely by mapping concepts.

| **Reference**                                              | **Publisher/type**        | **Relevance**                                                                                                                                                    |
|------------------------------------------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AIDCF-001 AIDCF Manifesto                                  | Internal canonical source | Purpose, doctrine, fifteen-domain architecture, evidence and UNKNOWN principles.                                                                                 |
| AIDCF-002 Core Conceptual Model                            | Internal canonical source | Capability, assets, dependencies, capacity, failure, safeguard and assurance concepts; canonical chain; MATERIAL; legacy domain mapping.                       |
| AIDCF-007A Canonical Master Control Registry               | Internal canonical source | Fifteen domain codes, 90 families and 360 controls to which Part V and Part XV align.                                                                            |
| AIDCF-014 Traceability and Machine-Executable Data Standard | Internal canonical source | Exchange object classes (§7) and relationship types (§9) to which Appendices A and B map.                                                                        |
| ISO/IEC/IEEE 15026-2                                       | ISO/IEC/IEEE              | Assurance-case structure (claims, arguments, evidence) underlying the canonical chain.                                                                           |
| IEC 62443 series (in particular parts 1-1, 3-2, 3-3 and 4-2) | IEC                     | Industrial automation and control system security concepts: zones, conduits, foundational requirements and security levels (Part XVI).                          |
| W3C OWL 2, SHACL, JSON-LD 1.1 and PROV-O                   | W3C                       | Machine-readable publication formats (Part XIV).                                                                                                                 |
| ISO/IEC 22237-1:2021                                       | ISO                       | General data-centre concepts, reference models and classification context; the standard explicitly excludes selection/configuration of IT and network equipment. |
| ISO/IEC 22237 series                                       | ISO/IEC                   | Facilities and infrastructure topics spanning building, power, environmental control, cabling, security and operations.                                          |
| EN 50600 series                                            | CENELEC                   | European data-centre facilities and infrastructure planning, construction and operation context.                                                                 |
| NVIDIA Enterprise Reference Architectures                  | NVIDIA                    | Validated and repeatable AI-factory designs integrating compute, networking, storage and software.                                                               |
| Open Systems for AI: Blueprint for Scalable Infrastructure | Open Compute Project      | Open and interoperable AI infrastructure ecosystem context.                                                                                                      |
| AI-Ready Data Storage Infrastructure taxonomy              | IDC                       | Storage-specific AI readiness and data logistics taxonomy context.                                                                                               |
| Cisco AI-ready infrastructure design guides                | Cisco                     | Examples of AI infrastructure design profiles and validated designs.                                                                                             |

## E.1 Public links

ISO/IEC 22237-1:2021: https://www.iso.org/standard/78550.html

NVIDIA Reference Architectures: https://docs.nvidia.com/reference-architectures/index.html

NVIDIA Enterprise Reference Architectures: https://www.nvidia.com/en-us/technologies/enterprise-reference-architecture/

Open Systems for AI whitepaper: https://www.opencompute.org/documents/ocp-open-systems-for-ai-whitepaper-v1-0-0-final-pdf/

Cisco AI-ready infrastructure design guides: https://www.cisco.com/c/en/us/solutions/design-zone/ai-ready-infrastructure.html

# Appendix F - Review and acceptance record

| **Review role**                     | **Status**      | **Acceptance focus**                                            |
|-------------------------------------|-----------------|-----------------------------------------------------------------|
| Methodology author                  | Draft completed | Internal coherence and alignment with AIDCF-001 and AIDCF-002.  |
| Ontology/knowledge-model reviewer   | Pending         | Class, relationship, constraint and machine-readable integrity. |
| Data-centre architecture reviewer   | Pending         | Facility and system taxonomy usability.                         |
| Electrical engineering reviewer     | Pending         | Power semantics and dependency accuracy.                        |
| Mechanical/cooling reviewer         | Pending         | Thermal, hydraulic and liquid-cooling semantics.                |
| Fire/life-safety reviewer           | Pending         | Boundary and safety terminology.                                |
| Physical-security reviewer          | Pending         | Physical control and zoning taxonomy.                           |
| AI compute/HPC reviewer             | Pending         | Compute, rack-scale and cluster taxonomy.                       |
| Storage reviewer                    | Pending         | Data infrastructure and recovery semantics.                     |
| Network/interconnect reviewer       | Pending         | Scale-up, scale-out and management fabrics.                     |
| OT/security reviewer                | Pending         | BMS, EPMS, SCADA, IEC 62443 zone/conduit and control relationships. |
| Assurance/evidence reviewer         | Pending         | UNKNOWN, confidence, provenance and claims.                     |
| AI Trust Graph integration reviewer | Pending         | Handoff and shared-node semantics.                              |
| Legal/IP/trademark review           | Pending         | Publication claims, licensing and ownership.                    |
| Public release                      | Not approved    | All mandatory review gates closed.                              |

No approval has been granted for this document; the record states review status only.

## F.1 Acceptance criteria

- Canonical terms remain consistent with the Manifesto and Core Conceptual Model.

- All fifteen domains are represented without becoming isolated silos, and every class carries a valid domain code.

- Capability, outcome, function, system, asset and dependency distinctions are operationally usable.

- Capacity and redundancy claims are condition- and evidence-bounded.

- Time, state, responsibility and UNKNOWN are first-class semantics.

- AIDCF-004 can attach threats, hazards, failures and propagation paths without restructuring the ontology.

- The assurance half of the chain (Part XV) can be populated for a synthetic assessment and exchanged through AIDCF-014 without loss.

- Machine-readable schemas can be generated from the normative registries.

- No content creates an unsupported certification or engineering claim.

- Independent multidisciplinary review and change control are recorded.

## Change record

| **Version** | **Status**              | **Summary**                                                                       |
|-------------|-------------------------|-----------------------------------------------------------------------------------|
| 0.1         | Architecture draft          | Established upper ontology and initial domain taxonomy.                                                    |
| 0.5         | Integrated draft            | Added relationships, state, capacity, responsibility, validation and profiles.                             |
| 1.0         | Controlled-review draft     | Baseline for expert review and machine-readable implementation.                                           |
| 1.1         | Draft for controlled review | 15-domain re-baseline; assurance-chain and IEC 62443 classes; AIDCF-014 alignment; renumbered requirements. |

## Final doctrine

AIDCF infrastructure is represented only when its meaning can be connected to a Capability Instance, Service Outcome, Required Function, dependency, state or assurance purpose. Classification alone is insufficient. The ontology must reveal how the system is assembled, what it relies upon, under which conditions claims apply, who is responsible, what evidence supports the representation and what remains UNKNOWN.

# Appendix G - Legacy identifier mapping

Requirement identifiers were renumbered in v1.1 to remove gaps. The table maps v1.0 identifiers to v1.1 identifiers; requirements new in v1.1 are listed for completeness.

| **v1.0 ID**     | **v1.1 ID** |
|-----------------|-------------|
| IOT-REQ-001     | IOT-REQ-001 |
| IOT-REQ-002     | IOT-REQ-002 |
| IOT-REQ-003     | IOT-REQ-003 |
| IOT-REQ-004     | IOT-REQ-004 |
| IOT-REQ-005     | IOT-REQ-005 |
| IOT-REQ-006     | IOT-REQ-006 |
| IOT-REQ-016     | IOT-REQ-007 |
| IOT-REQ-017     | IOT-REQ-008 |
| IOT-REQ-018     | IOT-REQ-009 |
| IOT-REQ-019     | IOT-REQ-010 |
| — (new in v1.1) | IOT-REQ-011 |
| — (new in v1.1) | IOT-REQ-012 |
| IOT-REQ-020     | IOT-REQ-013 |
| IOT-REQ-021     | IOT-REQ-014 |
| IOT-REQ-028     | IOT-REQ-015 |
| IOT-REQ-029     | IOT-REQ-016 |
| IOT-REQ-034     | IOT-REQ-017 |
| IOT-REQ-035     | IOT-REQ-018 |
| IOT-REQ-036     | IOT-REQ-019 |
| IOT-REQ-037     | IOT-REQ-020 |
| — (new in v1.1) | IOT-REQ-021 |
| IOT-REQ-041     | IOT-REQ-022 |
| IOT-REQ-042     | IOT-REQ-023 |
| IOT-REQ-043     | IOT-REQ-024 |
| IOT-REQ-046     | IOT-REQ-025 |
| IOT-REQ-047     | IOT-REQ-026 |
| IOT-REQ-048     | IOT-REQ-027 |
| IOT-REQ-051     | IOT-REQ-028 |
| IOT-REQ-052     | IOT-REQ-029 |
| IOT-REQ-054     | IOT-REQ-030 |
| IOT-REQ-055     | IOT-REQ-031 |
| IOT-REQ-056     | IOT-REQ-032 |
| IOT-REQ-066     | IOT-REQ-033 |
| IOT-REQ-067     | IOT-REQ-034 |
| IOT-REQ-068     | IOT-REQ-035 |
| — (new in v1.1) | IOT-REQ-036 |
| — (new in v1.1) | IOT-REQ-037 |
| — (new in v1.1) | IOT-REQ-038 |
| — (new in v1.1) | IOT-REQ-039 |
| — (new in v1.1) | IOT-REQ-040 |
| — (new in v1.1) | IOT-REQ-041 |
| — (new in v1.1) | IOT-REQ-042 |
| — (new in v1.1) | IOT-REQ-043 |
| — (new in v1.1) | IOT-REQ-044 |
| — (new in v1.1) | IOT-REQ-045 |
| — (new in v1.1) | IOT-REQ-046 |

Validation rules VAL-001 to VAL-020 are renamed IOT-VAL-001 to IOT-VAL-020 with unchanged numbers (IOT-VAL-021 to IOT-VAL-025 are new). Conformance levels C0 to C4 are renamed IOT-CL0 to IOT-CL4. The v1.0 artifact identifier AIDCF-IOT-001 is replaced by the public ID AIDCF-003.
