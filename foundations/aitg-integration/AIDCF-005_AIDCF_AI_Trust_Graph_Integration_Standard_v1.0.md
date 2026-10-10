> Markdown edition (source of truth). PDF: [AIDCF-005_AIDCF_AI_Trust_Graph_Integration_Standard_v1.0.pdf](AIDCF-005_AIDCF_AI_Trust_Graph_Integration_Standard_v1.0.pdf)

A graph-native interoperability and semantic handoff standard for infrastructure assurance, digital trust, failure propagation, evidence and accountable decisions

Artifact ID: AIDCF-INT-001  
Artifact type: Normative integration standard  
Status: Draft for controlled review  
Author: Siva Sethumadhavan  
Release 1: Foundational Methodology

Connect infrastructure reality to AI-system trust without merging, weakening or overwriting either methodology.

# Document control

| **Field**        | **Value**                                                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Title            | AIDCF - AI Trust Graph Integration Standard v1.0                                                                                                                                                                                   |
| Artifact ID      | AIDCF-INT-001                                                                                                                                                                                                                      |
| Status           | Draft for controlled review                                                                                                                                                                                                        |
| Author           | Siva Sethumadhavan                                                                                                                                                                                                                 |
| Depends on       | AIDCF Manifesto v1.0; AIDCF Core Conceptual Model v1.0; AIDCF-003 Infrastructure Ontology & Taxonomy v1.0; AIDCF-004 Threat, Hazard & Failure Model v1.0; AI Trust Graph Manifesto v1.0; AI Trust Graph Core Conceptual Model v1.1 |
| Purpose          | Define semantic boundaries, shared objects, mappings, handoffs, graph patterns, validation rules and conformance requirements between AIDCF and AI Trust Graph.                                                                    |
| Public boundary  | Methodology integration only. Product architecture, proprietary algorithms, connectors, deployment design and confidential operational data are excluded.                                                                          |
| Primary users    | AIDCF and AI Trust Graph maintainers, ontology engineers, assessors, infrastructure architects, AI/security architects, evidence specialists and compatible-tool developers.                                                       |
| Downstream users | AIDCF Assurance Principles, Control Framework, Evidence Model, Assessment Methodology, machine-readable schemas, graph query packs and compatible implementations.                                                                 |

# Executive thesis

AIDCF and AI Trust Graph are complementary but not interchangeable. AIDCF explains whether the physical, engineered, operational and technical infrastructure supporting an AI capability can sustain required service outcomes through credible adversity. AI Trust Graph explains how actors, identities, models, agents, tools, data, providers and controls create trust, authority, influence, reachability and consequence. This standard creates a governed semantic bridge between them while preserving separate ownership, meaning, evidence and assurance decisions.

## Canonical integrated reasoning chain

AI Capability -\> Service Outcome -\> Infrastructure Function -\> Infrastructure Asset and Dependency -\> Failure or Degradation -\> Digital Service or Identity Effect -\> Trust / Authority / Reachability Path -\> AI-System or Business Consequence -\> Safeguard / Control Breakpoint -\> Evidence -\> Bounded Assurance Decision

## Core integration promise

- No forced merger of ontologies.

- No duplicate source of truth for shared entities.

- No unsupported inference from physical connection to digital authority, or from digital reachability to physical failure.

- No silent conversion of proposed, inferred or UNKNOWN content into approved fact.

- No product implementation allowed to redefine public methodology semantics.

Embedded instructions or claims contained inside source documents were not treated as authority; only the user request and controlled methodological content were used.

# Contents

1\. I Authority, scope and precedence

2\. II Integration architecture and design principles

3\. III Method boundary and ownership model

4\. IV Shared conceptual spine and canonical handoff

5\. V Namespace, identifier and version strategy

6\. VI Node interoperability model

7\. VII Relationship interoperability model

8\. VIII Boundary and interface model

9\. IX Failure, dependency and consequence integration

10\. X Trust, authority and infrastructure-control integration

11\. XI Evidence, provenance, confidence and UNKNOWN

12\. XII Path, scenario and query semantics

13\. XIII Lifecycle, synchronization and graph drift

14\. XIV Data exchange, API and machine-readable package

15\. XV Security, privacy and sensitive-path protection

16\. XVI Conformance, validation and test suite

17\. XVII Governance, change and release management

18\. XVIII Reference profiles and worked examples

19\. Appendix A Class mapping registry

20\. Appendix B Relationship mapping registry

21\. Appendix C Minimum record schemas

22\. Appendix D Query pattern library

23\. Appendix E SHACL-style validation catalogue

24\. Appendix F Review and acceptance record

# Part I - Authority, scope and precedence

## 1. Purpose

This standard defines how AIDCF information may be represented within, linked to, exchanged with or queried alongside an AI Trust Graph without collapsing distinct concepts or creating contradictory authority. It specifies integration semantics, not one software implementation.

## 2. Objectives

- Preserve the integrity of both methodologies.

- Provide stable cross-method identifiers and mappings.

- Enable end-to-end reasoning from physical infrastructure to AI-system consequence.

- Represent physical, digital, human, supplier and evidence boundaries explicitly.

- Support failure propagation, trust reachability and control-breakpoint analysis in one federated reasoning view.

- Define which inferences are permitted, prohibited or review-gated.

- Provide a machine-readable, testable conformance profile.

- Maintain public-methodology and protected-product boundaries.

## 3. Normative precedence

| **Conflict type**              | **Resolution rule**                                                                                                                     |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| AIDCF internal                 | Manifesto -\> Core Conceptual Model -\> AIDCF-003 -\> AIDCF-004 -\> this Integration Standard -\> downstream artifacts.                 |
| AI Trust Graph internal        | Manifesto -\> Core Conceptual Model -\> canonical ontology -\> assessment artifacts -\> compatible tooling.                             |
| Cross-method semantic conflict | Preserve each method within its declared boundary; create an explicit mapping or OPEN decision. Do not overwrite either canonical term. |
| Implementation conflict        | Public canonical artifacts prevail over product convenience or stored implementation state.                                             |
| Evidence conflict              | Retain both assertions with provenance; resolve through an accountable review record.                                                   |
| Safety conflict                | Applicable law, authorised engineering and life-safety authority prevail over methodological convenience.                               |

## 4. Scope

- Entity identity and cross-method references.

- Class and relationship mapping.

- Boundary and shared-interface semantics.

- Scenario, path, failure and consequence handoff.

- Evidence, provenance, confidence, review and decision linking.

- Query and validation expectations.

- Versioning, synchronization, security and governance.

## 5. Exclusions

- Detailed ExposureGraph or other product architecture.

- Deployment topology, storage engine or graph-database selection.

- Proprietary ranking, inference, remediation or scoring algorithms.

- Live connector credentials or collection procedures.

- Certification claims, legal opinions or engineering approval.

## 6. Conformance levels

| **Level** | **Name**                      | **Requirements**                                                                                         |
|-----------|-------------------------------|----------------------------------------------------------------------------------------------------------|
| I0        | Vocabulary aware              | Uses canonical labels and declares source methodology.                                                   |
| I1        | Reference linked              | Uses stable IDs and cross-method references.                                                             |
| I2        | Semantically mapped           | Applies approved class, relationship and boundary mappings.                                              |
| I3        | Evidence gated                | Attaches provenance, confidence, state and review to material assertions.                                |
| I4        | Query conformant              | Passes path, boundary and validation test catalogue.                                                     |
| I5        | Federated operational profile | Supports governed synchronization, version snapshots, drift and reassessment without semantic overwrite. |

**INT-REQ-001** Conformant integration shall preserve canonical source methodology and version for every mapped term.

**INT-REQ-002** AIDCF and AI Trust Graph shall remain independently usable.

**INT-REQ-003** Mappings shall not be treated as equivalence unless the equivalence is explicitly approved.

**INT-REQ-004** Material cross-method assertions shall include evidence, confidence, effective time and review state.

**INT-REQ-005** UNKNOWN shall remain visible across exchange and transformation.

**INT-REQ-006** Sensitive infrastructure and trust paths shall be protected according to their combined consequence.

# Part II - Integration architecture and design principles

## 7. Federated semantic architecture

| **Layer**  | **AIDCF responsibility**                               | **Integration responsibility**                                  | **AI Trust Graph responsibility**                                     |
|------------|--------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------------|
| Doctrine   | Capability-centred infrastructure assurance.           | Preserve complementary purpose and common commitments.          | System-level trust, authority, exposure and evidence.                 |
| Conceptual | Capability, outcome, dependency, failure, resilience.  | Define handoff concepts and prohibited collapses.               | Objects, relationships, conditions, paths, authority and consequence. |
| Ontology   | Infrastructure entities, states and failure semantics. | Mappings, shared IDs, boundary interfaces and bridge relations. | AI-system entities, trust/authority edges and path semantics.         |
| Assessment | Facility and infrastructure evidence and conclusions.  | Cross-method scenario, evidence and decision bundles.           | AI-system architecture, control and trust-path conclusions.           |
| Tooling    | Optional AIDCF-compatible implementation.              | Federation, exchange and query profile.                         | Optional AI Trust Graph-compatible implementation.                    |

## 8. Design principles

**IP-01** Separation with interoperability: connect methodologies without merging authority.

**IP-02** Source-of-truth discipline: each concept has one canonical owner and may have many references.

**IP-03** Bridge only where decision value exists.

**IP-04** A relationship is a conditional assertion, not an unqualified arrow.

**IP-05** Infrastructure failure and digital misuse are distinct but may form one consequence chain.

**IP-06** Evidence travels with assertions, not merely with files.

**IP-07** Inference proposes; accountable review approves.

**IP-08** Historical graph states remain immutable snapshots.

**IP-09** Security classification follows the most sensitive combined path.

**IP-10** Tool independence and vendor neutrality are mandatory.

## 9. Integration patterns

| **Pattern**          | **Use**                                                                                    | **Constraint**                                              |
|----------------------|--------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Reference            | One method points to an entity owned by the other.                                         | No property duplication beyond cache/display values.        |
| Mapping              | Two classes or relationships are aligned at broader, narrower or related meaning.          | Mapping type and reviewer required.                         |
| Shared identity      | The same real-world instance appears in both methods.                                      | One global ID plus method-specific views.                   |
| Boundary handoff     | An AIDCF infrastructure service becomes an AI Trust Graph dependency or enforcement point. | Interface record and effective conditions required.         |
| Scenario composition | AIDCF failure path combines with AI Trust Graph exposure or authority path.                | Each path segment retains native semantics.                 |
| Evidence reuse       | One evidence object supports assertions in both methods.                                   | Assertion-specific relevance and scope reviewed separately. |
| Decision federation  | Separate conclusions are presented in a coordinated decision package.                      | No automatic least/most favourable aggregation.             |

# Part III - Method boundary and ownership model

## 10. Canonical ownership matrix

| **Concept**                                                                      | **Canonical owner**                 | **Integration mode** | **Rule**                                                                                   |
|----------------------------------------------------------------------------------|-------------------------------------|----------------------|--------------------------------------------------------------------------------------------|
| Site, building, hall, rack and physical zone                                     | AIDCF                               | Reference only       | ATG may reference location/boundary where relevant.                                        |
| Power, cooling, fire, structural and facility OT systems                         | AIDCF                               | Reference/bridge     | ATG may model digital identity and authority to management interfaces.                     |
| Accelerator, compute node, storage platform and network fabric as infrastructure | AIDCF                               | Shared identity      | ATG may add identities, control-plane permissions and digital reachability.                |
| Model, agent, prompt, retriever, memory, tool and API                            | AI Trust Graph                      | Reference only       | AIDCF references only when needed to define capability or infrastructure load/dependency.  |
| Human and machine identity, credential, delegation and authority                 | AI Trust Graph                      | Bridge               | AIDCF references operator/management dependencies but does not redefine digital authority. |
| AI Capability Instance and Service Outcome                                       | AIDCF                               | Shared anchor        | ATG links AI system and business outcomes to the same capability anchor.                   |
| Threat, hazard, infrastructure failure and propagation                           | AIDCF                               | Scenario bridge      | ATG links downstream digital trust or authority effects.                                   |
| Trust, influence, authority, reachability and exposure path                      | AI Trust Graph                      | Scenario bridge      | AIDCF links infrastructural initiating conditions and dependencies.                        |
| Safeguard as real-world measure                                                  | AIDCF for infrastructure safeguards | Related concept      | ATG Control/Control Breakpoint may govern digital or cross-boundary path.                  |
| Evidence, assertion, confidence, review and decision                             | Joint governed profile              | Shared contract      | Native method can add specialised fields without breaking common core.                     |

## 11. Areas of deliberate overlap

- Compute, storage and network entities may be infrastructure assets and digital trust targets.

- BMS, EPMS, SCADA, cluster managers and provisioning services may be facility/compute systems and identity-governed digital control planes.

- Operators and suppliers may be infrastructure dependencies and trust/authority actors.

- Safeguards and controls may target the same real-world mechanism but represent different assessment abstractions.

- Evidence may support both physical-state and digital-authority assertions.

## 12. Prohibited collapses

| **Do not collapse**                            | **Reason**                                                                             |
|------------------------------------------------|----------------------------------------------------------------------------------------|
| Infrastructure dependency / trust relationship | Reliance is not the same as acceptance, delegation or authority.                       |
| Physical connectivity / digital reachability   | A cable or network path does not establish usable protocol, identity or permission.    |
| Digital access / physical control authority    | Read or login access does not necessarily permit consequential command.                |
| AIDCF safeguard / ATG control                  | A safeguard is the real measure; a control is an assessable requirement or breakpoint. |
| Failure propagation / exposure path            | Failure effects and compromise/misuse progression have different semantics.            |
| Capability consequence / security finding      | One is an outcome; the other is an assessed weakness or conclusion.                    |
| Evidence grade / confidence / effectiveness    | Support strength, belief and control performance are separate.                         |
| Shared entity / equivalent class               | The same instance can have two method-specific views without class equivalence.        |

# Part IV - Shared conceptual spine and canonical handoff

## 13. Integrated upper model

| **Concept family** | **Canonical shared anchors**                                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------|
| Context            | Assessment, DecisionQuestion, Scope, Boundary, Environment, EffectivePeriod, ArchitectureBaseline.     |
| Capability         | CapabilityInstance, ServiceOutcome, CriticalFunction, OperatingEnvelope.                               |
| System             | System, Asset, Component, Interface, Location, Provider, Actor, Identity.                              |
| Relationship       | Dependency, Connection, TrustGrant, Authority, Influence, Reachability, DataMovement, ControlCoverage. |
| Adversity          | Threat, Hazard, InitiatingEvent, FailureCause, FailureMode, Effect, Consequence.                       |
| Protection         | Safeguard, Control, Barrier, ControlBreakpoint, RecoveryAction.                                        |
| Assurance          | Assertion, EvidenceObject, Test, Finding, Unknown, Decision, Limitation.                               |
| Temporal           | Snapshot, ChangeEvent, ValidityInterval, GraphDrift, ReassessmentTrigger.                              |

## 14. Handoff chain

| **Handoff**                       | **Source object**             | **Bridge relation**             | **Target object**                            |
|-----------------------------------|-------------------------------|---------------------------------|----------------------------------------------|
| Capability context                | AIDCF CapabilityInstance      | REPRESENTED_BY_AI_SYSTEM        | ATG SystemOfInterest/AI System.              |
| Infrastructure service            | AIDCF CriticalFunction/System | ENABLES_DIGITAL_FUNCTION        | ATG Application/Model/Agent/Tool function.   |
| Control-plane interface           | AIDCF BMS/EPMS/ClusterManager | HAS_DIGITAL_INTERFACE           | ATG Service/API/Endpoint.                    |
| Machine identity                  | ATG WorkloadIdentity          | AUTHORIZES_CONTROL_OF           | AIDCF infrastructure management asset.       |
| Failure to trust effect           | AIDCF FailureMode/Effect      | CREATES_DIGITAL_CONDITION       | ATG trust/authority/reachability condition.  |
| Exposure to infrastructure action | ATG ExposurePath              | CAN_AFFECT                      | AIDCF asset, system, function or capability. |
| Control breakpoint                | ATG ControlBreakpoint         | REALIZED_BY                     | AIDCF Safeguard or system configuration.     |
| Evidence                          | Shared EvidenceObject         | SUPPORTS / DISPUTES             | AIDCF or ATG Assertion.                      |
| Decision                          | Method-specific Decision      | CONTRIBUTES_TO_DECISION_PACKAGE | Integrated DecisionPackage.                  |

## 15. Shared core properties

| **Property**              | **Required on**              | **Meaning**                                    |
|---------------------------|------------------------------|------------------------------------------------|
| globalId                  | All shared/mapped objects    | Immutable cross-method identifier.             |
| canonicalOwner            | All shared/mapped objects    | AIDCF, ATG or JointSharedProfile.              |
| sourceArtifact            | All terms and assertions     | Artifact and version controlling meaning.      |
| methodView                | Mapped/shared instances      | AIDCF view, ATG view or integrated view.       |
| scopeRef                  | Material assertions          | Assessment scope and boundary.                 |
| effectiveFrom/effectiveTo | Assertions and relationships | Validity interval.                             |
| evidenceRefs              | Material assertions          | Supporting, disputing and qualifying evidence. |
| confidenceState           | Material assertions          | Controlled confidence/UNKNOWN state.           |
| reviewState               | Proposed or approved content | Candidate, approved, rejected, superseded.     |
| securityClassification    | Sensitive objects and paths  | Handling requirement.                          |
| supersedes                | Versioned records            | Historical lineage without overwrite.          |

# Part V - Namespace, identifier and version strategy

## 16. Recommended namespaces

| **Prefix** | **Purpose**                       | **Illustrative namespace**              |
|------------|-----------------------------------|-----------------------------------------|
| aidcf:     | AIDCF canonical ontology          | https://w3id.org/aidcf/core/1.0/        |
| aidcf-thf: | AIDCF threat/failure extension    | https://w3id.org/aidcf/thf/1.0/         |
| atg:       | AI Trust Graph canonical ontology | https://w3id.org/aitrustgraph/core/1.0/ |
| aix:       | Integration bridge ontology       | https://w3id.org/aidcf/integration/1.0/ |
| prov:      | W3C provenance vocabulary         | http://www.w3.org/ns/prov#              |
| skos:      | Vocabulary mappings               | http://www.w3.org/2004/02/skos/core#    |

The namespace locations above are proposed publication patterns and require maintainer approval and persistent-identifier configuration before release.

## 17. Identifier model

- Global IDs identify real-world or conceptual instances across views.

- Canonical term IDs remain in their source namespace.

- Mapping records receive independent IDs and lifecycle status.

- Path and run identifiers are immutable and versioned.

- Sensitive instance IDs should be opaque and must not reveal facility details.

- Retired identifiers are never reassigned.

## 18. Mapping semantics

| **Mapping type** | **Meaning**                                                | **Permitted use**                               |
|------------------|------------------------------------------------------------|-------------------------------------------------|
| EXACT            | Semantics equivalent for declared scope.                   | Requires joint maintainer approval.             |
| CLOSE            | Substantially aligned but differences remain.              | Interoperability with disclosed limitation.     |
| BROADER          | Source concept is broader than target.                     | Taxonomy navigation, not property inheritance.  |
| NARROWER         | Source concept is narrower than target.                    | Profile specialization.                         |
| RELATED          | Material relationship without semantic equivalence.        | Default for most cross-method links.            |
| SHARED_INSTANCE  | Two representations refer to the same real-world instance. | Identity federation with separate method views. |
| NO_MAP           | Concept intentionally has no counterpart.                  | Boundary preservation.                          |

**INT-REQ-018** Mapped terms shall declare mapping type, source and target versions, rationale, approver and effective period.

**INT-REQ-019** Close, broader, narrower and related mappings shall not drive automatic property equivalence.

**INT-REQ-020** Breaking changes shall increment the major version and publish migration guidance.

# Part VI - Node interoperability model

## 19. Node superclasses

| **Node superclass**      | **Definition**                                                           |
|--------------------------|--------------------------------------------------------------------------|
| aix:ContextNode          | Assessment, scope, boundary, environment, decision and version context.  |
| aix:CapabilityNode       | Capability Instance, Service Outcome and Critical Function anchors.      |
| aix:InfrastructureNode   | Location, system, asset, component, interface and resource.              |
| aix:DigitalSystemNode    | AI system, model, agent, tool, data, prompt, pipeline, API and provider. |
| aix:ActorNode            | Person, team, organisation, supplier, operator and assessor.             |
| aix:IdentityNode         | Human, workload, service, device and federated identities.               |
| aix:AdverseConditionNode | Threat, hazard, cause, failure, effect and consequence.                  |
| aix:ProtectionNode       | Safeguard, control, barrier, breakpoint and recovery action.             |
| aix:AssuranceNode        | Assertion, evidence, test, finding, decision and limitation.             |
| aix:TemporalNode         | Snapshot, change event, state and validity interval.                     |
| aix:IntegrationNode      | Mapping, handoff, decision package, synchronization event and conflict.  |

## 20. Shared-entity identity rules

**INT-REQ-021** A shared entity shall have one globalId and one or more method-specific views.

**INT-REQ-022** Method views shall retain canonical class, owner, properties, evidence and lifecycle.

**INT-REQ-023** A merged display shall be labelled integrated view and shall not replace native records.

**INT-REQ-024** Conflicting properties shall remain separate assertions until resolved.

**INT-REQ-025** Node granularity shall follow the decision question; aggregation shall preserve membership and consequence.

## 21. Primary shared-node candidates

| **Real-world subject**    | **AIDCF view**                | **ATG view**                            | **Integration rule**                                                       |
|---------------------------|-------------------------------|-----------------------------------------|----------------------------------------------------------------------------|
| GPU compute node          | Compute Asset                 | Workload/Infrastructure Target          | Shared instance; distinct operational and authority properties.            |
| Cluster manager           | Compute Management System     | Service/API/Privileged Target           | Shared instance with control-plane interface.                              |
| BMS/EPMS/SCADA            | Facility Control System       | Service/Control Plane/Privileged Target | Shared instance; physical function remains AIDCF-owned.                    |
| Storage platform          | Storage System                | Data/Service Target                     | Shared instance; distinguish infrastructure availability from data access. |
| Network fabric controller | Network Management System     | Control Plane/Privileged Target         | Shared instance; distinguish fabric function from digital authority.       |
| Operator                  | Human Dependency/Role         | Human Actor/Identity                    | Shared person/role link; avoid replacing identity with job role.           |
| Supplier                  | External Dependency           | Provider/Organisation                   | Shared organisation with separate contractual and trust edges.             |
| Evidence item             | Evidence Object               | Evidence Object                         | Joint profile where lawful and relevant.                                   |
| Assessment boundary       | Infrastructure scope boundary | System/trust boundary                   | Related or overlapping boundaries, not automatically identical.            |

## 22. Node lifecycle states

| **State**  | **Meaning**                                               |
|------------|-----------------------------------------------------------|
| CANDIDATE  | Proposed by collector, inference or analyst.              |
| OBSERVED   | Directly observed but not yet approved as canonical fact. |
| APPROVED   | Reviewed and accepted for the declared scope/snapshot.    |
| DISPUTED   | Material conflict unresolved.                             |
| STALE      | Evidence or state no longer sufficiently current.         |
| SUPERSEDED | Replaced by a later approved version.                     |
| RETIRED    | No longer active but retained historically.               |
| UNKNOWN    | Existence, class or material attribute unresolved.        |

# Part VII - Relationship interoperability model

## 23. Edge families

| **Family**         | **AIDCF examples**                       | **ATG examples**                           | **Bridge examples**                               |
|--------------------|------------------------------------------|--------------------------------------------|---------------------------------------------------|
| Structural         | PART_OF, LOCATED_IN, IMPLEMENTS          | CONTAINS, DEPLOYED_IN, PART_OF             | SHARED_INSTANCE_OF, METHOD_VIEW_OF.               |
| Dependency         | DEPENDS_ON, POWERED_BY, COOLED_BY        | RELIES_ON, PROVIDED_BY                     | ENABLES, PROVIDES_INFRASTRUCTURE_SERVICE_TO.      |
| Connectivity       | CONNECTED_TO, INTERFACES_WITH            | NETWORK_REACHES, CALLS, INVOKES            | HAS_DIGITAL_INTERFACE, EXPOSES_ENDPOINT.          |
| Identity/authority | OPERATED_BY, MAINTAINED_BY               | AUTHENTICATES_AS, AUTHORIZES, DELEGATES_TO | AUTHORIZES_CONTROL_OF, OPERATES_THROUGH_IDENTITY. |
| Failure            | CAUSES, PROPAGATES_TO, AFFECTS           | ENABLES_PATH, AMPLIFIES, COMPROMISES       | CREATES_DIGITAL_CONDITION, CAN_AFFECT.            |
| Protection         | PROTECTED_BY, CONTAINED_BY, RECOVERED_BY | CONTROLLED_BY, BLOCKED_BY, DETECTED_BY     | REALIZED_BY, BREAKS_INTEGRATED_PATH.              |
| Evidence           | EVIDENCED_BY, CHALLENGED_BY              | SUPPORTS, DISPUTES, QUALIFIES              | SAME_EVIDENCE_OBJECT, RELEVANT_TO_VIEW.           |
| Decision           | RESULTS_IN, INVALIDATES                  | INFORMS, ACCEPTED_BY, SUPERSEDES           | CONTRIBUTES_TO_DECISION_PACKAGE.                  |

## 24. Bridge relationship registry

| **Bridge edge**                    | **Source**              | **Target**                      | **Meaning**                                                     |
|------------------------------------|-------------------------|---------------------------------|-----------------------------------------------------------------|
| REPRESENTED_BY_AI_SYSTEM           | CapabilityInstance      | ATG SystemOfInterest            | Links capability to digital system representation.              |
| ENABLES_DIGITAL_FUNCTION           | CriticalFunction/System | ATG Function/Object             | Infrastructure function enables digital behavior.               |
| PROVIDES_INFRASTRUCTURE_SERVICE_TO | AIDCF System            | ATG Object                      | Power, cooling, compute, storage, network or facility service.  |
| HAS_DIGITAL_INTERFACE              | AIDCF Asset/System      | ATG Service/API/Endpoint        | Management or telemetry interface.                              |
| OPERATES_THROUGH_IDENTITY          | AIDCF Actor/Role        | ATG Identity                    | Identity used to exercise operational action.                   |
| AUTHORIZES_CONTROL_OF              | ATG Identity/Authority  | AIDCF Asset/System              | Digital authority can command/configure infrastructure.         |
| CREATES_DIGITAL_CONDITION          | AIDCF Failure/Effect    | ATG Condition                   | Infrastructure event changes digital state or trust conditions. |
| CAN_AFFECT                         | ATG Path/Actor/Tool     | AIDCF Asset/Function/Capability | Digital path may cause physical or infrastructure consequence.  |
| REALIZED_BY                        | ATG Control             | AIDCF Safeguard                 | Control is implemented by real infrastructure measure.          |
| BREAKS_INTEGRATED_PATH             | Control/Safeguard       | IntegratedPath                  | Verified interruption of cross-method progression.              |
| METHOD_VIEW_OF                     | Method-specific node    | Shared entity                   | Associates native view with global instance.                    |
| MAPS_TO                            | Canonical term          | Canonical term                  | Controlled semantic mapping.                                    |
| CONTRIBUTES_TO_DECISION_PACKAGE    | Decision                | DecisionPackage                 | Federates conclusions without aggregation.                      |
| TRIGGERS_REASSESSMENT_OF           | Change/Finding          | Assessment/Snapshot             | Change invalidates or limits prior conclusion.                  |

## 25. Edge minimum record

| **Field**              | **Requirement**                                                             |
|------------------------|-----------------------------------------------------------------------------|
| edgeId                 | Immutable identifier.                                                       |
| edgeType               | Canonical native or bridge predicate.                                       |
| source/target          | Compatible endpoint IDs.                                                    |
| canonicalOwner         | AIDCF, ATG or Integration.                                                  |
| direction              | Explicit; inverse only if registered.                                       |
| scope/conditions       | Identity, state, protocol, environment, load, time or approval as relevant. |
| evidenceRefs           | Supporting/disputing evidence.                                              |
| confidenceState        | Controlled confidence or UNKNOWN.                                           |
| reviewState            | Candidate through superseded.                                               |
| effectivePeriod        | Time for which assertion applies.                                           |
| securityClassification | Handling requirement.                                                       |
| sourceVersion          | Controlling artifact/schema version.                                        |

# Part VIII - Boundary and interface model

## 26. Boundary classes

| **Boundary**       | **AIDCF emphasis**                                       | **ATG emphasis**                                             | **Integrated question**                                          |
|--------------------|----------------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------------|
| Physical           | Site, hall, cage, rack and route.                        | Physical access as trust precondition.                       | Can access create digital or physical consequence?               |
| Electrical/thermal | Power and cooling fault/containment boundaries.          | Dependency and consequence target.                           | Can failure cross into digital service or authority loss?        |
| Network            | Fabric, management and external connectivity.            | Reachability, segmentation and protocol conditions.          | Does connectivity plus identity create actionable control?       |
| Identity           | Operator accounts and management access dependencies.    | Principal, credential, federation, delegation and privilege. | Who can act on infrastructure, under what conditions?            |
| Administrative     | Owner, operator, tenant and supplier responsibility.     | Trust grant, provider and decision authority.                | Where does accountability or enforcement change?                 |
| Provider           | Utility, OEM, colocation and service provider.           | AI/cloud/tool/data provider boundary.                        | Which external dependency can collapse multiple assumptions?     |
| Sovereignty        | Location, operation, maintenance and supply constraints. | Data flow, identity, provider and control jurisdiction.      | Do physical and digital dependencies meet sovereignty intent?    |
| Evidence           | Facility data classification and disclosure limits.      | Graph evidence, identity and finding sensitivity.            | Can assurance remain traceable without exposing sensitive paths? |

## 27. Boundary Crossing object

| **Property**                  | **Required content**                                              |
|-------------------------------|-------------------------------------------------------------------|
| crossingId                    | Stable identifier.                                                |
| sourceBoundary/targetBoundary | Explicit boundary objects.                                        |
| crossingEntity                | Flow, identity, service, person, supplier, resource or path.      |
| nativeRelation                | AIDCF or ATG relationship.                                        |
| bridgeRelation                | Integration relation where applicable.                            |
| expectedEnforcement           | Control, safeguard or authority gate.                             |
| operatingStates               | Normal, degraded, maintenance, emergency, recovery or transition. |
| evidence                      | Design and observed evidence.                                     |
| owner                         | Responsible and accountable parties.                              |
| failureModes                  | How crossing or enforcement may fail.                             |
| confidence/UNKNOWN            | Current evidence-bounded state.                                   |

# Part IX - Failure, dependency and consequence integration

## 28. Integrated scenario metamodel

| **Stage**                       | **Native owner** | **Required object**                                                                    |
|---------------------------------|------------------|----------------------------------------------------------------------------------------|
| Decision context                | Joint            | DecisionQuestion, CapabilityInstance, ServiceOutcome, scope and snapshot.              |
| Infrastructure context          | AIDCF            | Assets, systems, dependencies, fault domains, state and operating envelope.            |
| Adverse initiation              | AIDCF            | Threat/hazard, initiating event, cause and failure mode.                               |
| Infrastructure propagation      | AIDCF            | Effects through explicit dependencies and fault domains.                               |
| Digital handoff                 | Integration      | CREATES_DIGITAL_CONDITION or loss/change of interface, identity, telemetry or service. |
| Trust/authority propagation     | ATG              | Conditional path across identity, access, delegation, invocation, influence or trust.  |
| Capability/business consequence | Joint            | Technical, AI-system, service, stakeholder and strategic consequence.                  |
| Protection                      | Joint            | Infrastructure safeguards, digital controls and cross-boundary breakpoints.            |
| Evidence/decision               | Joint            | Assertions, evidence bundle, UNKNOWN, findings and separate/federated decisions.       |

## 29. Integrated path types

| **Path type**              | **Description**                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Infrastructure-to-digital  | Physical or operational failure alters digital service, identity, telemetry or control-plane condition.        |
| Digital-to-infrastructure  | Identity, tool or service authority can alter infrastructure configuration or operation.                       |
| Compound cyber-physical    | Deliberate digital action combines with physical or engineering condition.                                     |
| Common-dependency collapse | One utility, identity, controller, provider, team or service affects both methodologies.                       |
| Detection/attribution loss | Failure removes telemetry needed for AI Trust Graph evidence or infrastructure response.                       |
| Recovery-coupled           | Digital recovery depends on physical infrastructure, or facility recovery depends on digital control/identity. |
| Sovereignty path           | Physical location, operator, provider, support identity and data/control jurisdiction combine.                 |
| Change/transition path     | Upgrade, expansion, migration or temporary bypass changes both infrastructure and trust state.                 |

## 30. Cross-method causal discipline

**INT-REQ-030** A native AIDCF causal relationship shall not be relabelled as an ATG authority relationship.

**INT-REQ-031** An ATG reachability path shall not be treated as an infrastructure failure without an evidenced action and effect.

**INT-REQ-032** Integrated scenarios shall identify the exact semantic handoff step.

**INT-REQ-033** Every path step shall declare native or bridge semantics.

**INT-REQ-034** Propagation may stop at UNKNOWN and shall not be completed by assumption.

**INT-REQ-035** Controls and safeguards shall be evaluated against the specific path segment and operating state they cover.

## 31. Consequence alignment

| **AIDCF consequence**     | **ATG consequence alignment**                | **Integration note**                                              |
|---------------------------|----------------------------------------------|-------------------------------------------------------------------|
| Capability availability   | System/service unavailability                | Same event may have infrastructure and digital causal segments.   |
| Compute capacity          | Loss of AI processing/actionability          | Do not equate capacity loss with compromise.                      |
| Data/artifact integrity   | Data/model integrity consequence             | Trace whether cause is storage failure, authority misuse or both. |
| Isolation/security        | Boundary or trust collapse                   | Preserve physical and digital isolation semantics.                |
| Recovery complexity       | Containment/rollback/revocation difficulty   | Model recovery dependencies across both methods.                  |
| Strategic/sovereignty     | Provider, jurisdiction or authority exposure | Assess physical and digital sovereignty jointly.                  |
| Evidence/attribution loss | Observability and audit-path failure         | Evidence degradation may cap both conclusions.                    |

# Part X - Trust, authority and infrastructure-control integration

## 32. Infrastructure authority model

Infrastructure authority is represented when a human or machine identity can observe, configure, command, isolate, bypass, update, stop, start, transfer, reset or otherwise affect an infrastructure asset or function. Authority remains distinct from network reachability and from role ownership.

| **Authority action** | **Examples of target**                  | **Required conditions**                                       |
|----------------------|-----------------------------------------|---------------------------------------------------------------|
| OBSERVE              | BMS, EPMS, telemetry, logs              | Identity, permission, interface, scope and evidence.          |
| CONFIGURE            | Setpoint, protection, route, firmware   | Write authority, approval, change control and rollback.       |
| COMMAND              | Start/stop/transfer/isolate             | Action permission, safety interlock and operating state.      |
| BYPASS               | Alarm, protection, redundancy, approval | Explicit authorization, duration, monitoring and restoration. |
| UPDATE               | Firmware, image, policy, logic          | Supply integrity, compatibility, approval and recovery.       |
| REVOKE               | Session, credential, remote support     | Revocation mechanism and verified effect.                     |
| RECOVER              | Restore configuration/service           | Approved baseline, identity, sequence and validation.         |

## 33. Authority amplification patterns

| **Pattern**                   | **Integrated example**                                           | **Required analysis**                                                  |
|-------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------|
| Shared management identity    | One account controls multiple cooling, power or compute systems. | Blast radius, credential boundary, approval, telemetry and revocation. |
| Control-plane inheritance     | Group or federated role inherits infrastructure write rights.    | Delegation chain, scope, conditions and evidence.                      |
| Tool-mediated action          | AI agent or automation invokes a management API.                 | Effective identity, tool scope, approval and reversibility.            |
| Provider remote support       | OEM identity can access privileged interfaces.                   | Contract, activation, monitoring, jurisdiction and revocation.         |
| Emergency bypass              | Operational role gains exceptional authority.                    | Trigger, duration, independent review and cleanup.                     |
| Telemetry-to-command coupling | Monitoring platform can issue automated control actions.         | Sensor trust, logic, fail state and common dependency.                 |

## 34. Control and safeguard alignment

| **AIDCF safeguard function** | **ATG control function**         | **Integrated use**                                               |
|------------------------------|----------------------------------|------------------------------------------------------------------|
| Anticipate                   | Govern/classify                  | Identify preconditions and high-consequence paths.               |
| Prevent                      | Block/constrain                  | Stop failure or unauthorized action before progression.          |
| Detect                       | Observe/alert                    | Detect physical, digital or integrated state change.             |
| Decide                       | Approve/authorize                | Apply human or machine decision gate.                            |
| Respond                      | Revoke/isolate                   | Constrain active progression.                                    |
| Contain                      | Segment/limit blast radius       | Keep effect within fault/trust boundary.                         |
| Withstand                    | Maintain service/least authority | Sustain minimum outcome while limiting actionability.            |
| Recover                      | Restore/rollback                 | Return infrastructure and digital system to approved state.      |
| Adapt                        | Relearn/reconfigure              | Update models, controls, architecture and evidence after change. |

# Part XI - Evidence, provenance, confidence and UNKNOWN

## 35. Common evidence profile

| **Field family** | **Minimum content**                                                                   |
|------------------|---------------------------------------------------------------------------------------|
| Identity         | evidenceId, type, title and canonical owner.                                          |
| Source           | Source system, owner, authority and original reference.                               |
| Collection       | Collector, method, authorization, date and query/procedure.                           |
| Scope            | Assets, identities, environment, population, period and states.                       |
| Integrity        | Hash/signature, custody and transformation history.                                   |
| Quality          | Grade, relevance, currentness, corroboration and representativeness.                  |
| Protection       | Classification, privacy, need-to-know, retention and legal hold.                      |
| Traceability     | Assertions, nodes, edges, paths, controls, findings and decisions supported/disputed. |
| Review           | Reviewer, outcome, conflicts, limitations and supersession.                           |

## 36. Provenance alignment

The integration profile should use a provenance model capable of distinguishing entities, activities and responsible agents. Where RDF/OWL is used, W3C PROV-O is the preferred external vocabulary for interoperable provenance links, with AIDCF/ATG-specific specialisations where needed.

## 37. Evidence grades and state mapping

| **Grade/state** | **Integration interpretation**                                                                           |
|-----------------|----------------------------------------------------------------------------------------------------------|
| E0              | No usable evidence. Relevant assertion remains UNKNOWN or Not Tested.                                    |
| E1              | Inference or uncorroborated signal. Candidate content only.                                              |
| E2              | Accountable attestation. Supports claimed practice, not independent effectiveness.                       |
| E3              | Approved documentation. Supports design/governance intent.                                               |
| E4              | Corroborated technical evidence. May support implementation within observed scope.                       |
| E5              | Direct current technical evidence plus representative test/operation. May support bounded effectiveness. |
| CONFLICTING     | Material sources disagree; do not average or pick silently.                                              |
| STALE           | Evidence no longer sufficiently representative after time or change.                                     |
| UNKNOWN         | Insufficient evidence or unresolved conflict; preserved end to end.                                      |

## 38. Assertion contract

| **Property**             | **Requirement**                                                 |
|--------------------------|-----------------------------------------------------------------|
| assertionId              | Stable versioned identifier.                                    |
| subject/predicate/object | One precise proposition using canonical terms.                  |
| methodOwner              | AIDCF, ATG or Integration.                                      |
| scope/conditions         | Boundary, environment, state, identity, configuration and time. |
| evidenceRefs             | Supporting, disputing and qualifying evidence.                  |
| confidence               | Controlled state plus rationale.                                |
| review                   | Candidate, approved, rejected, modified or superseded.          |
| limitations              | Explicit non-covered conditions.                                |
| derivedFrom              | Transformation/query/rule and source version.                   |
| decisionImpact           | Which finding, path or decision relies upon it.                 |

**INT-REQ-038** Transformation shall preserve source IDs, provenance, evidence grade, confidence and review state.

**INT-REQ-039** AI-generated extraction or inference shall create a candidate assertion and shall not overwrite approved facts.

**INT-REQ-040** One evidence item may support both methods only after assertion-specific relevance and scope are evaluated.

**INT-REQ-041** Conflicting evidence shall remain queryable after resolution.

**INT-REQ-042** Evidence classification may restrict graph display without deleting traceability.

# Part XII - Path, scenario and query semantics

## 39. IntegratedPath object

| **Field**         | **Required content**                                                        |
|-------------------|-----------------------------------------------------------------------------|
| pathId            | Immutable ID and version.                                                   |
| pathType          | Infrastructure-to-digital, digital-to-infrastructure, compound, etc.        |
| startCondition    | Actor, threat, hazard, failure, identity or state.                          |
| orderedSteps      | Native nodes/edges and bridge handoff steps.                                |
| target            | Capability, asset, privileged action, data, stakeholder or service outcome. |
| preconditions     | Identity, authority, protocol, load, state, environment and timing.         |
| boundariesCrossed | Physical, network, identity, provider, administrative or sovereignty.       |
| breakpoints       | Controls/safeguards attached to specific steps.                             |
| evidenceCoverage  | Evidence per material step.                                                 |
| unknownSteps      | Unverified elements and impact.                                             |
| residualPath      | Remaining progression after controls.                                       |
| reviewState       | Candidate, validated, disputed, superseded.                                 |
| snapshot          | Graph/version context.                                                      |

## 40. Path validity rules

**PATH-001** Every adjacent step shall be type-compatible.

**PATH-002** Every bridge step shall use an approved integration relationship.

**PATH-003** A topological connection shall not imply executable authority.

**PATH-004** A reachable digital target shall not imply realised infrastructure effect.

**PATH-005** Conditions and operating states shall be evaluated at each material step.

**PATH-006** A control shall interrupt only the path conditions it has demonstrably covered.

**PATH-007** Alternative and common-dependency paths shall be considered before closure.

**PATH-008** A path with critical UNKNOWN may be prioritised but not declared proven.

**PATH-009** Historical paths shall remain bound to their graph snapshot.

**PATH-010** Sensitive paths shall be access controlled and safely abstracted for broad reports.

## 41. Canonical query families

| **Query family**              | **Decision question**                                                                                              |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Capability dependency         | Which infrastructure and external dependencies support this AI capability?                                         |
| Physical-to-digital failure   | Which digital services, identities or AI components are affected by loss of this infrastructure function?          |
| Digital-to-physical authority | Which identities, agents, tools or providers can affect critical facility or compute functions?                    |
| Common dependency             | Which safeguards and controls share a utility, identity, controller, provider, team or management service?         |
| Control breakpoint            | Which verified intervention interrupts the most material integrated paths?                                         |
| Critical UNKNOWN              | Which unverified bridge relationships cap assurance?                                                               |
| Recovery chain                | Which identities, systems, spares, services and infrastructure conditions are required to restore capability?      |
| Evidence coverage             | Which nodes, edges and path steps lack current evidence?                                                           |
| Graph drift                   | Which changed entities or relationships invalidate a prior integrated decision?                                    |
| Sovereignty                   | Which cross-border physical, support, identity, provider or data dependencies affect the stated sovereignty claim? |

## 42. Query result contract

- Query ID and version.

- Decision question and authorized purpose.

- Graph snapshot and schema versions.

- Start/target scope and filters.

- Returned nodes, edges and paths with native ownership.

- Evidence and confidence per material assertion.

- UNKNOWN and excluded data.

- Security classification.

- Reviewer and disposition where used for a finding or decision.

# Part XIII - Lifecycle, synchronization and graph drift

## 43. Snapshot model

| **Snapshot**        | **Meaning**                                                                                                    |
|---------------------|----------------------------------------------------------------------------------------------------------------|
| AIDCF snapshot      | Infrastructure configuration, state, evidence and scenario view at a point or period.                          |
| ATG snapshot        | AI ecosystem objects, trust/authority edges, evidence and path view.                                           |
| Integrated snapshot | References compatible native snapshots plus bridge assertions; does not copy them into a new hidden authority. |
| Decision snapshot   | Frozen integrated subgraph used for a named decision.                                                          |
| Comparison snapshot | Pair/set of snapshots used for drift and reassessment analysis.                                                |

## 44. Synchronization modes

| **Mode**                  | **Use**                                             | **Constraint**                                                   |
|---------------------------|-----------------------------------------------------|------------------------------------------------------------------|
| Manual controlled import  | Review-led exchange of approved packages.           | Full provenance and validation required.                         |
| Scheduled synchronization | Periodic exchange of changed approved records.      | No implication of continuous monitoring.                         |
| Event-driven update       | Change event proposes affected bridge assertions.   | Human review for material facts/decisions.                       |
| Federated query           | Query native repositories without copying all data. | Access, performance and snapshot consistency declared.           |
| Offline evidence package  | Sanitised package for independent assessment.       | Immutable manifest, classification and completeness limitations. |

## 45. Drift taxonomy

| **Drift**          | **Example**                                                   | **Required response**                |
|--------------------|---------------------------------------------------------------|--------------------------------------|
| Entity drift       | New controller, identity, rack or provider.                   | Discovery and mapping review.        |
| Relationship drift | Changed permission, route, dependency or operator.            | Path re-analysis.                    |
| State drift        | Maintenance, bypass, degraded cooling or emergency access.    | State-specific re-evaluation.        |
| Evidence drift     | Evidence stale, superseded or conflicting.                    | Confidence review.                   |
| Control drift      | Control disabled, scope reduced, exception added.             | Breakpoint and residual-path review. |
| Schema drift       | Class, edge or property version changes.                      | Compatibility and migration review.  |
| Boundary drift     | Ownership, tenant, network, provider or jurisdiction changes. | Boundary-crossing review.            |
| Capability drift   | Workload, scale, autonomy or service outcome changes.         | Rebaseline AIDCF and ATG scopes.     |

## 46. Reassessment triggers

- Material AIDCF Change Event.

- New or changed ATG identity, authority, tool, agent or provider relationship.

- Critical incident or near miss.

- Failure of a safeguard or control breakpoint.

- Evidence expiry or conflict.

- Capacity expansion or new liquid-cooled/high-density deployment.

- Provider, jurisdiction or remote-support change.

- Schema major version or mapping change.

- Resolution of a critical UNKNOWN.

# Part XIV - Data exchange, API and machine-readable package

## 47. Required publication package

| **Artifact**                        | **Purpose**                                             |
|-------------------------------------|---------------------------------------------------------|
| aidcf-atg-integration-v1.0.owl      | Bridge ontology and formal class/property declarations. |
| aidcf-atg-integration-v1.0.ttl      | Readable RDF/Turtle serialization.                      |
| aidcf-atg-context-v1.0.jsonld       | JSON-LD context.                                        |
| aidcf-atg-exchange-v1.0.schema.json | JSON exchange contract.                                 |
| aidcf-atg-shapes-v1.0.ttl           | SHACL validation shapes.                                |
| class-mappings-v1.0.csv             | Class mapping registry.                                 |
| relationship-mappings-v1.0.csv      | Relationship and bridge edge registry.                  |
| query-catalog-v1.0.yaml             | Named query definitions and expected outputs.           |
| conformance-tests-v1.0/             | Positive, negative and migration fixtures.              |
| examples/                           | Synthetic integrated profiles and decision packages.    |
| CHANGELOG.md                        | Versioned change history.                               |
| MIGRATION.md                        | Compatibility and migration instructions.               |
| SECURITY.md                         | Sensitive-path and vulnerability disclosure guidance.   |
| LICENSE.md                          | Rights and obligations for public reuse.                |

## 48. Exchange envelope

{  
"packageId": "aix-package:example-001",  
"schemaVersion": "1.0",  
"aidcfSnapshot": "aidcf-snapshot:001",  
"atgSnapshot": "atg-snapshot:014",  
"bridgeAssertions": \["aix-edge:001"\],  
"evidenceManifest": \["evidence:001"\],  
"unknowns": \["unknown:001"\],  
"securityClassification": "RESTRICTED",  
"reviewState": "CANDIDATE"  
}

## 49. API resource model

| **Resource**        | **Minimum operations / behavior**                                         |
|---------------------|---------------------------------------------------------------------------|
| /mappings           | Retrieve approved mappings by version and status.                         |
| /shared-entities    | Resolve global ID to native method views.                                 |
| /bridge-assertions  | Create candidate, review, approve, supersede and query bridge assertions. |
| /snapshots          | Register immutable native and integrated snapshots.                       |
| /paths              | Submit/query integrated paths and validation state.                       |
| /evidence-manifests | Reference evidence metadata without exposing protected content.           |
| /unknowns           | Track unresolved information and assurance impact.                        |
| /decision-packages  | Assemble separate conclusions and shared limitations.                     |
| /conformance        | Validate package/schema/mapping/test profile.                             |

This resource model is normative at the information-contract level only. It does not prescribe transport protocol, authentication product, database or deployment topology.

## 50. OWL, SHACL and JSON roles

| **Technology** | **Role**                                                            | **Anti-error rule**                                                       |
|----------------|---------------------------------------------------------------------|---------------------------------------------------------------------------|
| OWL/RDF        | Semantic classes, properties, mappings and reasoning.               | Open-world reasoning does not validate required record completeness.      |
| SHACL          | Validate RDF data shapes, cardinality and compatibility.            | Validation shapes do not prove real-world truth or control effectiveness. |
| JSON Schema    | Validate exchange structure and datatypes.                          | Structural validity is not semantic or assurance validity.                |
| JSON-LD        | Carry linked identifiers in JSON exchange.                          | Context resolution and version must be controlled.                        |
| PROV-O         | Represent interoperable provenance entities, activities and agents. | Specialization shall preserve provenance semantics.                       |

# Part XV - Security, privacy and sensitive-path protection

## 51. Information sensitivity

| **Information class**   | **Examples**                                                            | **Minimum handling**                                         |
|-------------------------|-------------------------------------------------------------------------|--------------------------------------------------------------|
| Public methodology      | Canonical terms, synthetic examples and abstract patterns.              | Approved public repository.                                  |
| Controlled methodology  | Draft mappings, unresolved decisions and review notes.                  | Maintainer access.                                           |
| Restricted architecture | Facility layout, power/cooling paths, identities, routes and providers. | Need-to-know, encryption and monitored access.               |
| Highly restricted path  | Combined physical and digital path to critical control or capability.   | Segregated access, strong approval and limited export.       |
| Evidence protected      | Logs, configs, contracts, telemetry and personal data.                  | Lawful purpose, minimisation, retention and access controls. |
| Security vulnerability  | Actionable weakness or live exploit path.                               | Coordinated disclosure and restricted remediation workflow.  |

## 52. Security requirements

**SEC-001** Integrated-path access shall be authorised by consequence and sensitivity, not only by repository membership.

**SEC-002** Exports shall support redaction or abstraction while retaining reference integrity.

**SEC-003** Credentials, secrets and sensitive values shall not be stored as ordinary node properties.

**SEC-004** Query and export activity for restricted graphs shall be auditable.

**SEC-005** Tenant and client data shall remain logically and cryptographically separated where required.

**SEC-006** Synthetic examples shall not reveal identifiable facility or client details.

**SEC-007** Inference and automation shall operate within explicit data-handling and output-release controls.

**SEC-008** Deletion and retention actions shall preserve required audit lineage and legal obligations.

## 53. Safe publication pattern

- Publish canonical schemas, mappings and synthetic examples.

- Do not publish instance graphs of real facilities or live privilege paths.

- Separate public identifiers from operational identifiers.

- Provide abstract path narratives where detailed disclosure creates risk.

- Perform employer, client, IP, privacy, security and licensing review before release.

# Part XVI - Conformance, validation and test suite

## 54. Core validation catalogue

| **Rule** | **Validation statement**                                                                     |
|----------|----------------------------------------------------------------------------------------------|
| VAL-001  | Every mapping declares source and target artifact versions.                                  |
| VAL-002  | Every shared instance has one globalId and at least one native method view.                  |
| VAL-003  | Every bridge edge has allowed source and target classes.                                     |
| VAL-004  | Every material bridge assertion has evidence, confidence, review and effective period.       |
| VAL-005  | Every integrated path contains at least one explicit approved handoff edge.                  |
| VAL-006  | Every path step identifies native owner or Integration ownership.                            |
| VAL-007  | No digital reachability edge is treated as physical effect without action/effect evidence.   |
| VAL-008  | No physical connection is treated as digital authority without identity/permission evidence. |
| VAL-009  | Every control-break claim identifies covered path segment and test conditions.               |
| VAL-010  | Every unresolved critical step is represented as UNKNOWN.                                    |
| VAL-011  | Every integrated decision package retains separate native conclusions.                       |
| VAL-012  | Every snapshot references immutable native graph versions.                                   |
| VAL-013  | Every supersession retains prior record and rationale.                                       |
| VAL-014  | Every restricted path carries security classification.                                       |
| VAL-015  | Every AI-generated assertion remains candidate until approved.                               |
| VAL-016  | Every evidence reuse is reviewed for assertion-specific relevance.                           |
| VAL-017  | Every schema major-version change has migration guidance.                                    |
| VAL-018  | Every mapping conflict is recorded as OPEN, disputed or resolved.                            |
| VAL-019  | Every boundary crossing identifies expected enforcement and owner.                           |
| VAL-020  | Every synchronization run produces audit and validation results.                             |

## 55. Positive conformance tests

- Resolve a shared compute manager into AIDCF and ATG views.

- Build an infrastructure-to-digital failure path with one bridge handoff.

- Build a digital-to-infrastructure authority path with evidenced identity and permission.

- Attach one evidence item to separate assertions with different scope ratings.

- Supersede a bridge assertion without deleting history.

- Compare integrated snapshots and identify drift-triggered reassessment.

- Produce a decision package with separate AIDCF, ATG and integrated limitations.

## 56. Negative tests

- Reject bridge edge with incompatible endpoints.

- Reject approved material assertion lacking evidence or explicit UNKNOWN.

- Reject path that jumps from network connection to control authority.

- Reject path closure based solely on policy evidence.

- Reject mapping that silently upgrades RELATED to EXACT.

- Reject package that replaces UNKNOWN with null, false or zero.

- Reject snapshot mutation after decision finalisation.

- Reject export of restricted path without authorization/classification.

## 57. Conformance report

| **Field**                | **Required content**                              |
|--------------------------|---------------------------------------------------|
| implementationId/version | Named implementation and release.                 |
| profile/level            | I0-I5 and optional profile.                       |
| schema versions          | AIDCF, ATG and integration versions.              |
| tests executed           | Positive, negative, security and migration tests. |
| results                  | Pass, fail, not tested and UNKNOWN.               |
| exceptions               | Approved deviations and rationale.                |
| evidence                 | Logs, fixtures, reviewer and date.                |
| limitations              | Unsupported features and interoperability impact. |
| approval                 | Technical and methodology reviewers.              |
| expiry/retest            | Triggers and validity conditions.                 |

# Part XVII - Governance, change and release management

## 58. Governance bodies and roles

| **Role/body**                         | **Accountability**                                                               |
|---------------------------------------|----------------------------------------------------------------------------------|
| AIDCF methodology maintainer          | Approves AIDCF meanings and native mappings.                                     |
| AI Trust Graph methodology maintainer | Approves ATG meanings and native mappings.                                       |
| Integration architecture board        | Owns bridge ontology, mapping conflicts and conformance profile.                 |
| Domain SMEs                           | Review engineering, compute, storage, networking, OT, identity and AI semantics. |
| Evidence and assurance reviewer       | Reviews provenance, confidence, UNKNOWN and decision discipline.                 |
| Security reviewer                     | Reviews sensitive path, access, export and disclosure controls.                  |
| Legal/IP/publication reviewer         | Reviews ownership, licensing, employer/client and public claims.                 |
| Release manager                       | Produces versioned package, changelog, signatures and migration artifacts.       |

## 59. Change classes

| **Class**               | **Example**                                                   | **Version impact**                |
|-------------------------|---------------------------------------------------------------|-----------------------------------|
| Editorial               | Clarification without semantic change.                        | Patch.                            |
| Additive compatible     | New bridge mapping or optional property.                      | Minor.                            |
| Constraining compatible | New validation shape that formalises existing requirement.    | Minor with impact note.           |
| Breaking semantic       | Changed meaning, endpoint compatibility or required property. | Major.                            |
| Security emergency      | Restriction or deprecation to prevent harmful exposure.       | Patch/minor plus urgent advisory. |
| Deprecation             | Term remains readable but replacement specified.              | Minor; removal only in major.     |

## 60. Mapping proposal record

| **Field**        | **Content**                                               |
|------------------|-----------------------------------------------------------|
| proposalId       | Stable ID.                                                |
| source/target    | Canonical term IDs and versions.                          |
| mappingType      | EXACT, CLOSE, BROADER, NARROWER, RELATED or NO_MAP.       |
| rationale        | Decision use and semantic comparison.                     |
| differences      | Scope, properties, conditions and exclusions.             |
| impact           | Queries, profiles, data migration and decisions affected. |
| evidence         | Examples and validation tests.                            |
| reviewers        | AIDCF, ATG, ontology and domain reviewers.                |
| status           | Proposed, approved, rejected, deprecated or superseded.   |
| effectiveVersion | Integration release in which valid.                       |

## 61. Release gates

- Semantic consistency with all six canonical dependencies.

- No unresolved breaking conflicts hidden in mappings.

- Schema, shapes, mappings and examples pass conformance tests.

- Synthetic examples reviewed for safety and validity.

- Public/private boundary verified.

- Employer, IP, confidentiality, privacy, legal, trademark and license review completed.

- Migration and changelog published.

- Independent practitioner usability review completed.

# Part XVIII - Reference profiles and worked examples

## 62. Reference profiles

| **Profile**            | **Focus**                                                                              | **Mandatory bridge objects**                                                                                    |
|------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| AI factory training    | Distributed compute, parallel storage, high-speed fabric, power/cooling and scheduler. | Capability, infrastructure services, management identities, failure-to-digital handoff, checkpoint consequence. |
| AI colocation          | Provider/tenant responsibilities and evidence access.                                  | Provider boundaries, shared instances, contracts, remote identities and UNKNOWN ownership.                      |
| Sovereign AI           | Location, operator control, provider support and jurisdiction.                         | Sovereignty boundaries, external dependencies, identities, data/control crossings and decision package.         |
| Agentic operations     | Agent/tool authority affecting infrastructure or capacity.                             | Agent, tool, identity, approval, target asset, action, safeguard/control and rollback.                          |
| Facility OT management | BMS/EPMS/SCADA digital control of engineering systems.                                 | Control interface, identities, authority, failure modes, telemetry and containment.                             |
| Recovery assurance     | Restore AI capability after compound disruption.                                       | Recovery dependencies, identities, golden configs, spares, infrastructure state and evidence.                   |

## 63. Worked example A: cooling degradation to AI consequence

| **Step** | **Native semantics**   | **Example assertion**                                                                                  |
|----------|------------------------|--------------------------------------------------------------------------------------------------------|
| 1        | AIDCF State            | Cooling system is DEGRADED under sustained training load.                                              |
| 2        | AIDCF Failure          | CDU capacity loss creates thermal effect on rack-scale system.                                         |
| 3        | Integration handoff    | Thermal effect CREATES_DIGITAL_CONDITION: accelerator throttling/health alarms.                        |
| 4        | ATG System path        | Scheduler and observability services receive reduced/unstable capacity signals.                        |
| 5        | ATG Authority/decision | Automation may reschedule, throttle or terminate jobs under approved policy.                           |
| 6        | Joint consequence      | Required training completion and checkpoint outcomes are at risk.                                      |
| 7        | Protection             | AIDCF safeguard and ATG approval/control breakpoint constrain progression.                             |
| 8        | Evidence               | Facility telemetry, GPU telemetry, scheduler events and test record support separate assertions.       |
| 9        | Decision               | AIDCF and ATG conclusions remain separate; integrated decision package identifies combined limitation. |

## 64. Worked example B: privileged remote support to physical effect

| **Step** | **Native semantics** | **Example assertion**                                                                       |
|----------|----------------------|---------------------------------------------------------------------------------------------|
| 1        | ATG Actor/Identity   | OEM support identity is activated for a defined maintenance window.                         |
| 2        | ATG Reachability     | Identity can authenticate to management gateway and reach a controller API.                 |
| 3        | ATG Authority        | Permission permits configuration change to the cooling control system.                      |
| 4        | Integration handoff  | Authority AUTHORIZES_CONTROL_OF an AIDCF cooling controller.                                |
| 5        | AIDCF Effect         | Incorrect setpoint can degrade heat removal under high load.                                |
| 6        | AIDCF Propagation    | Thermal effect propagates to compute capacity and service outcome.                          |
| 7        | Controls             | Just-in-time activation, approval, command allowlist, independent telemetry and revocation. |
| 8        | Evidence             | Identity logs, permission export, change record, controller logs and thermal telemetry.     |
| 9        | UNKNOWN              | If command scope is not evidenced, path remains candidate and assurance is capped.          |

## 65. Worked example C: evidence conflict

| **Source**            | **Assertion**                                                                                                          | **Treatment**                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| Approved architecture | Management network is isolated from enterprise access.                                                                 | E3 supports design intent.                 |
| Observed route export | A restricted gateway route exists.                                                                                     | E4 challenges current isolation assertion. |
| Identity inventory    | Accessible identity scope is incomplete.                                                                               | UNKNOWN for who can use route.             |
| Integration outcome   | Retain design and observed assertions separately; mark conflict and create candidate path.                             |                                            |
| Decision              | Do not declare exploitable access or effective isolation until identity/permission and tested conditions are resolved. |                                            |

# Appendix A - Class mapping registry

| **AIDCF class**            | **ATG class**                 | **Mapping**                 | **Rule**                                                   |
|----------------------------|-------------------------------|-----------------------------|------------------------------------------------------------|
| aidcf:CapabilityInstance   | atg:SystemOfInterest/AISystem | CLOSE/RELATED               | Shared capability anchor; not universal equivalence.       |
| aidcf:ServiceOutcome       | atg:Outcome                   | CLOSE                       | Outcome semantics aligned with method-specific properties. |
| aidcf:CriticalFunction     | atg:Function                  | CLOSE                       | AIDCF function is infrastructure/capability centred.       |
| aidcf:AssetInstance        | atg:Asset/Object              | BROADER/NARROWER            | Use shared instance mapping for real systems.              |
| aidcf:InfrastructureSystem | atg:InfrastructureObject      | CLOSE                       | ATG view adds trust/authority semantics.                   |
| aidcf:Dependency           | atg:Dependency                | CLOSE                       | Do not treat as TrustGrant.                                |
| aidcf:AssessmentBoundary   | atg:Boundary                  | RELATED                     | Boundary dimensions may overlap but differ.                |
| aidcf:OperatingState       | atg:Condition/State           | CLOSE                       | Preserve AIDCF enumerations.                               |
| aidcf-thf:Threat           | atg:ThreatCandidate           | RELATED                     | Threat analysis scope differs.                             |
| aidcf-thf:FailureMode      | atg:FailureCondition          | CLOSE                       | Use AIDCF canonical failure distinctions.                  |
| aidcf-thf:PropagationPath  | atg:Path                      | RELATED                     | Failure path differs from trust/exposure path.             |
| aidcf:Safeguard            | atg:Control/ControlBreakpoint | RELATED                     | Real measure vs assessment/control abstraction.            |
| aidcf:EvidenceObject       | atg:EvidenceItem              | CLOSE                       | Joint evidence profile may be used.                        |
| aidcf:Finding              | atg:Finding                   | CLOSE                       | Keep source method and decision basis.                     |
| aidcf:AssuranceDecision    | atg:Decision                  | CLOSE                       | Federate, do not aggregate automatically.                  |
| aidcf:Unknown              | atg:UNKNOWN                   | EXACT within shared profile | Preserve as first-class state.                             |

# Appendix B - Relationship mapping registry

| **AIDCF/bridge**              | **ATG**                   | **Mapping** | **Constraint**                                                   |
|-------------------------------|---------------------------|-------------|------------------------------------------------------------------|
| aidcf:DEPENDS_ON              | atg:RELIES_ON             | CLOSE       | Preserve dependency type and strength.                           |
| aidcf:CONNECTED_TO            | atg:NETWORK_REACHES       | RELATED     | Connection does not prove network reachability.                  |
| aidcf:INTERFACES_WITH         | atg:CALLS/INVOKES         | RELATED     | Interface existence does not prove invocation.                   |
| aidcf:OPERATED_BY             | atg:ACTS_AS/USES_IDENTITY | RELATED     | Operation role does not define effective identity.               |
| aidcf:PROTECTED_BY            | atg:CONTROLLED_BY         | RELATED     | Safeguard existence does not prove control effectiveness.        |
| aidcf:EVIDENCED_BY            | atg:SUPPORTS              | RELATED     | Evidence supports a precise assertion, not an object in general. |
| aidcf-thf:PROPAGATES_TO       | atg:ENABLES_PATH          | RELATED     | Failure propagation differs from trust-path enablement.          |
| aidcf-thf:AFFECTS             | atg:IMPACTS               | CLOSE       | Scope and consequence must be stated.                            |
| aix:AUTHORIZES_CONTROL_OF     | No native equivalent      | BRIDGE      | Digital authority targets infrastructure control.                |
| aix:CREATES_DIGITAL_CONDITION | No native equivalent      | BRIDGE      | Infrastructure effect alters digital condition.                  |
| aix:REALIZED_BY               | No native equivalent      | BRIDGE      | Digital control is realised by infrastructure safeguard.         |
| aix:METHOD_VIEW_OF            | No native equivalent      | BRIDGE      | Method-specific view references shared entity.                   |

# Appendix C - Minimum record schemas

## C.1 Mapping record

| **Property**    | **Cardinality** | **Type**        |
|-----------------|-----------------|-----------------|
| mappingId       | 1               | Identifier      |
| sourceTerm      | 1               | IRI             |
| targetTerm      | 1               | IRI             |
| mappingType     | 1               | Enumeration     |
| sourceVersion   | 1               | Version         |
| targetVersion   | 1               | Version         |
| rationale       | 1               | String          |
| differences     | 0..\*           | String          |
| reviewers       | 1..\*           | Party           |
| status          | 1               | Lifecycle state |
| effectivePeriod | 1               | Interval        |
| tests           | 1..\*           | Test reference  |

## C.2 Bridge assertion

| **Property**           | **Cardinality**  | **Type**             |
|------------------------|------------------|----------------------|
| bridgeAssertionId      | 1                | Identifier           |
| subject                | 1                | Native/shared entity |
| predicate              | 1                | Approved bridge edge |
| object                 | 1                | Native/shared entity |
| scope                  | 1                | Scope                |
| conditions             | 0..\*            | Condition            |
| evidence               | 1..\* or UNKNOWN | Evidence reference   |
| confidence             | 1                | State                |
| reviewState            | 1                | State                |
| effectivePeriod        | 1                | Interval             |
| securityClassification | 1                | Enumeration          |
| sourceSnapshot         | 1..2             | Snapshot references  |

## C.3 Integrated decision package

| **Property**       | **Cardinality** | **Type**            |
|--------------------|-----------------|---------------------|
| packageId          | 1               | Identifier          |
| decisionQuestion   | 1               | String/reference    |
| aidcfDecision      | 0..1            | Native Decision     |
| atgDecision        | 0..1            | Native Decision     |
| integratedFindings | 0..\*           | Finding             |
| criticalUnknowns   | 0..\*           | UNKNOWN             |
| evidenceManifest   | 1               | Manifest            |
| limitations        | 1..\*           | String              |
| decisionOwner      | 1               | Party               |
| reviewers          | 1..\*           | Party               |
| snapshot           | 1               | Integrated Snapshot |
| status             | 1               | State               |

# Appendix D - Query pattern library

| **ID**                                  | **Purpose**                                                                                                    |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Q-001 Critical infrastructure authority | Find ATG identities/actors with AUTHORIZES_CONTROL_OF paths to AIDCF critical assets.                          |
| Q-002 Failure-to-AI impact              | Traverse AIDCF PROPAGATES_TO then CREATES_DIGITAL_CONDITION to affected ATG systems and service outcomes.      |
| Q-003 Shared control dependency         | Find AIDCF safeguards and ATG controls that DEPEND_ON one identity, controller, provider or telemetry service. |
| Q-004 Missing bridge evidence           | Find approved/candidate bridge assertions with E0/E1, stale, conflicting or UNKNOWN support.                   |
| Q-005 Boundary enforcement gap          | Find crossings without expected enforcement, owner or current evidence.                                        |
| Q-006 Recovery dependency chain         | Find RECOVERED_BY and ATG authority/service paths required to restore a Capability Instance.                   |
| Q-007 Integrated single point           | Find entities whose loss or compromise disconnects the capability or defeats multiple controls.                |
| Q-008 Drift invalidation                | Compare snapshots and return changed bridge edges used by final decisions.                                     |
| Q-009 Residual path                     | Find alternate routes after a control or safeguard is applied.                                                 |
| Q-010 Sovereignty dependency            | Find cross-jurisdiction provider, identity, support, data or infrastructure dependencies for a capability.     |

# Appendix E - SHACL-style validation catalogue

| **Shape**            | **Target**               | **Constraint**                                                                                  |
|----------------------|--------------------------|-------------------------------------------------------------------------------------------------|
| SharedEntityShape    | aix:SharedEntity         | Exactly one globalId; at least one method view; canonical owner declared.                       |
| BridgeEdgeShape      | aix:BridgeAssertion      | Approved predicate; compatible endpoints; scope, evidence/UNKNOWN, confidence, review and time. |
| IntegratedPathShape  | aix:IntegratedPath       | Start, target, ordered steps, at least one bridge edge, snapshot and evidence coverage.         |
| DecisionPackageShape | aix:DecisionPackage      | Decision question, snapshot, evidence manifest, limitations and owner.                          |
| MappingShape         | aix:Mapping              | Source/target versions, mapping type, rationale, reviewer, status and tests.                    |
| UnknownShape         | aix:Unknown              | Unresolved attribute, materiality, owner if known and assurance impact.                         |
| SensitivePathShape   | aix:IntegratedPath       | Classification and access/export policy when target or steps are restricted.                    |
| SnapshotShape        | aix:IntegratedSnapshot   | Immutable IDs for compatible AIDCF and ATG snapshots.                                           |
| EvidenceShape        | aix:EvidenceObject       | Source, collection, scope, integrity, grade, protection, review and assertion links.            |
| ChangeShape          | aix:SynchronizationEvent | Changed records, validation result, actor, time, source versions and audit reference.           |

# Appendix F - Review and acceptance record

| **Review role**                     | **Status**      | **Focus**                                    |
|-------------------------------------|-----------------|----------------------------------------------|
| Methodology author                  | Draft completed | Overall coherence.                           |
| AIDCF ontology reviewer             | Pending         | AIDCF term and relationship integrity.       |
| AIDCF failure-model reviewer        | Pending         | Scenario and propagation semantics.          |
| AI Trust Graph ontology reviewer    | Pending         | ATG object, edge and path integrity.         |
| Data-centre engineering reviewer    | Pending         | Infrastructure handoff accuracy.             |
| AI/security architecture reviewer   | Pending         | Identity, authority, trust and reachability. |
| OT/control-system security reviewer | Pending         | BMS/EPMS/SCADA bridge risk.                  |
| Evidence/assurance reviewer         | Pending         | Provenance, confidence and decisions.        |
| Knowledge-graph engineer            | Pending         | OWL/RDF/JSON-LD/SHACL implementation.        |
| Security/privacy reviewer           | Pending         | Sensitive paths and data handling.           |
| Legal/IP/publication reviewer       | Pending         | Rights, licensing and claims.                |
| Independent practitioner review     | Pending         | Usability and interoperability.              |
| Public release                      | Not approved    | All mandatory gates closed.                  |

## Acceptance criteria

- Artifact 005 preserves the separate authority and independent usability of both methodologies.

- All shared concepts have a canonical owner and mapping type.

- Cross-method paths require explicit handoff edges and evidence.

- Physical connectivity, digital reachability, authority and realised consequence remain distinct.

- Evidence, confidence, UNKNOWN and supersession survive exchange.

- Machine-readable artifacts can be generated from the registries without inventing new semantics.

- Synthetic examples pass positive and negative conformance tests.

- Sensitive-path protection and publication boundaries are explicit.

- Multidisciplinary, legal, IP and security reviews are recorded before release.

## Change record

| **Version** | **Status**              | **Summary**                                                                             |
|-------------|-------------------------|-----------------------------------------------------------------------------------------|
| 0.1         | Architecture draft      | Established method boundaries, integration patterns and shared anchors.                 |
| 0.5         | Integrated draft        | Added mappings, bridge relationships, path semantics, validation and profiles.          |
| 1.0         | Controlled-review draft | Comprehensive normative baseline for expert review and machine-readable implementation. |

## Final doctrine

AIDCF and AI Trust Graph meet at the boundary between infrastructure capability and digital trust. Their integration must reveal how physical systems, operational dependencies, identities, digital authority, failure, exposure, controls and evidence combine to create or constrain consequence. Integration does not mean semantic collapse. The correct result is a traceable federation of native facts, explicit bridge assertions, evidence-bounded paths, preserved uncertainty and accountable decisions.
