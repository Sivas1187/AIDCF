> Markdown edition (source of truth). PDF: [AIDCF-003_Infrastructure_Ontology_and_Taxonomy_v1.0.pdf](AIDCF-003_Infrastructure_Ontology_and_Taxonomy_v1.0.pdf)

Canonical semantics for capability-centred AI infrastructure assurance

Artifact ID: AIDCF-IOT-001  
Artifact type: Normative foundation standard  
Status: Draft for controlled review  
Author: Siva Sethumadhavan  
Release 1: Foundational Methodology

This document defines the canonical entity classes, taxonomies, relationships, properties, constraints and machine-readable expectations used to represent AI infrastructure within AIDCF.

# Document control

| **Field**            | **Value**                                                                                                                                                                                                 |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Title                | AIDCF Infrastructure Ontology & Taxonomy v1.0                                                                                                                                                             |
| Artifact ID          | AIDCF-IOT-001                                                                                                                                                                                             |
| Artifact type        | Normative foundation standard                                                                                                                                                                             |
| Status               | Draft for controlled review                                                                                                                                                                               |
| Author               | Siva Sethumadhavan                                                                                                                                                                                        |
| Depends on           | AIDCF Manifesto v1.0; AIDCF Core Conceptual Model v1.0                                                                                                                                                    |
| Downstream users     | Threat, Hazard & Failure Model; AIDCF-AI Trust Graph Integration Standard; Domain Guides; Master Control Library; Evidence Model; Assessment Methodology; Scoring and Maturity Models; compatible tooling |
| Normative language   | Shall, shall not, should, may and can have the meanings defined in AIDCF Core Conceptual Model v1.0                                                                                                       |
| Intended audience    | AI infrastructure architects; data-centre engineers; assessors; operators; owners; technology teams; resilience, security and assurance practitioners; ontology engineers; product teams                  |
| Publication boundary | Independent methodology. Not a substitute for law, licensed engineering, safety approval, regulatory certification or vendor design authority.                                                            |

# Executive thesis

AIDCF represents an AI data centre as a capability-supporting system rather than a collection of equipment. The ontology begins with a defined Capability Instance and Service Outcomes, traces them to infrastructure functions and assets, expresses direct, indirect and shared dependencies, records capacity and operating conditions, and provides stable attachment points for failures, safeguards, evidence and assurance decisions.

## Canonical chain

Capability Instance -\> Service Outcome -\> Required Function -\> Infrastructure System -\> Asset Instance -\> Dependency -\> Operating Condition -\> Failure Exposure -\> Safeguard -\> Evidence -\> Assurance Decision

## How to use this standard

- Use Parts I-IV to establish a conformant assessment information model.

- Use Parts V-VII to classify infrastructure across the eight AIDCF domains.

- Use Parts VIII-XI to represent relationships, dependencies, states, capacity, responsibility and uncertainty.

- Use Parts XII-XIV to validate records, create implementation profiles and produce machine-readable releases.

- Do not treat the taxonomy as a control checklist or a substitute for engineering analysis.

# Contents

1\. Part I - Authority, scope and conformance

2\. Part II - Ontology architecture and design principles

3\. Part III - Upper ontology and canonical entities

4\. Part IV - Capability, outcome, boundary and lifecycle model

5\. Part V - Eight-domain infrastructure taxonomy

6\. Part VI - Cross-cutting classification facets

7\. Part VII - Asset, system, interface and resource model

8\. Part VIII - Relationship and dependency vocabulary

9\. Part IX - Capacity, redundancy, fault-domain and resilience semantics

10\. Part X - Operating state, temporal state and change semantics

11\. Part XI - Responsibility, evidence, confidence and UNKNOWN semantics

12\. Part XII - Conformance rules and validation shapes

13\. Part XIII - Reference implementation profiles

14\. Part XIV - Machine-readable publication specification

15\. Appendix A - Canonical class registry

16\. Appendix B - Canonical relationship registry

17\. Appendix C - Minimum property schemas

18\. Appendix D - Naming, identifier and namespace rules

19\. Appendix E - Standards and reference-source map

20\. Appendix F - Review and acceptance record

# Part I - Authority, scope and conformance

## 1. Purpose

This artifact establishes the controlled vocabulary and semantic structure by which AIDCF describes AI capabilities and the physical, engineered, technical, operational, human and external infrastructure on which they depend. It is intended to create consistency across documents, assessments, datasets, knowledge graphs, digital twins and future tooling.

## 2. Objectives

- Provide a capability-first upper ontology.

- Define a vendor-neutral eight-domain taxonomy.

- Express cross-domain and external dependencies without hiding scope boundaries.

- Distinguish systems, assets, components, interfaces, resources, services, roles and evidence.

- Represent capacity, redundancy, fault domains, operating states and temporal change.

- Preserve provenance, confidence, conflict and UNKNOWN.

- Provide machine-readable semantics without requiring proprietary software.

- Support future failure analysis, control mapping, assessment and assurance decisions.

## 3. Scope

The ontology covers entities materially relevant to the ability of a defined AI Capability Instance to deliver specified Service Outcomes. It spans site and physical protection; facilities engineering; power and thermal systems; environmental and resource performance; building operations; accelerator compute; storage and data infrastructure; and network and interconnect architecture.

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
> **IOT-REQ-003** Every material entity shall possess a stable identifier, class, lifecycle status, provenance and applicable confidence state.
>
> **IOT-REQ-004** Every assessment dataset shall identify the Capability Instance, Assessment Boundary, applicable Service Outcomes and Operating Envelope.
>
> **IOT-REQ-005** Dependencies crossing the Assessment Boundary shall remain represented as external dependencies or UNKNOWN; they shall not disappear because they are out of scope.
>
> **IOT-REQ-006** UNKNOWN shall remain a first-class semantic state and shall not be converted into pass, fail, zero, not applicable or accepted risk.

## 6. Conformance levels

| **Level** | **Name**                        | **Minimum expectation**                                                               |
|-----------|---------------------------------|---------------------------------------------------------------------------------------|
| C0        | Vocabulary alignment            | Uses canonical terms without contradictory meanings.                                  |
| C1        | Structured representation       | Implements required entities, identifiers and core relationships.                     |
| C2        | Assurance-ready dataset         | Adds boundaries, outcomes, dependencies, states, evidence, confidence and validation. |
| C3        | Graph-conformant implementation | Implements machine-readable schema, relationship semantics and validation shapes.     |
| C4        | Controlled extension            | Publishes namespace, mappings, governance, tests and change impact for extensions.    |

# Part II - Ontology architecture and design principles

## 7. Four-layer semantic architecture

| **Layer**                  | **Purpose**                               | **Examples**                                                            |
|----------------------------|-------------------------------------------|-------------------------------------------------------------------------|
| L0 Doctrine                | Constrains meaning and reasoning          | Capability-first; evidence-gated; cross-domain; UNKNOWN preservation.   |
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
> **P5 State awareness** Claims are tied to normal, degraded, maintenance, emergency, recovery or transition conditions.
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
| Domain              | Primary AIDCF domain or cross-domain.                     |
| Allowed relations   | Permitted outgoing and incoming relationships.            |
| Required properties | Minimum data needed for conformance.                      |
| Lifecycle status    | Draft, approved, deprecated or retired.                   |
| Provenance          | Origin, author, approval and version.                     |
| Examples            | Non-normative illustrations.                              |
| Exclusions          | Concepts intentionally not covered by the term.           |

# Part III - Upper ontology and canonical entities

## 10. Root entities

| **Class ID**               | **Definition**                                                          |
|----------------------------|-------------------------------------------------------------------------|
| AIDCF:Entity               | Root of all addressable objects.                                        |
| AIDCF:CapabilityEntity     | An intended ability and its bounded implementation.                     |
| AIDCF:OutcomeEntity        | A required or observed result.                                          |
| AIDCF:InfrastructureEntity | A system, asset, component, interface, location or resource.            |
| AIDCF:ConditionEntity      | A state, constraint, assumption, limit or environmental condition.      |
| AIDCF:AdverseEntity        | A threat, hazard, initiating event, cause, failure mode or consequence. |
| AIDCF:AssuranceEntity      | A safeguard, control, assertion, evidence, test, finding or decision.   |
| AIDCF:PartyEntity          | An organisation, actor, role, team or supplier.                         |
| AIDCF:TemporalEntity       | A lifecycle stage, timestamp, validity interval or change event.        |

## 11. Canonical class definitions

| **Preferred term**    | **Canonical definition**                                                                                   |
|-----------------------|------------------------------------------------------------------------------------------------------------|
| Capability            | An intended operational ability supported by infrastructure.                                               |
| Capability Instance   | A specific deployment bounded by ownership, location, architecture, capacity, criticality and obligations. |
| Service Outcome       | A measurable or assessable result required from a Capability Instance.                                     |
| Critical Function     | A function whose loss or degradation materially affects a Service Outcome.                                 |
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
| Evidence Object       | A record or observation used to support or challenge an assertion.                                         |
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
| UNKNOWN / Not applicable / Ineffective               | Evidence insufficiency is not the same as absence or failure.                  |

# Part IV - Capability, outcome, boundary and lifecycle model

## 13. Capability hierarchy

| **Level** | **Entity**                   | **Illustration**                                                                      |
|-----------|------------------------------|---------------------------------------------------------------------------------------|
| 1         | Capability family            | AI training; inference; fine-tuning; HPC simulation; shared accelerator service.      |
| 2         | Capability type              | Large-scale distributed training; low-latency inference; batch inference.             |
| 3         | Capability Instance          | A named deployment at a defined site with a declared architecture.                    |
| 4         | Service Outcome              | Availability, throughput, completion, latency, integrity or recovery outcome.         |
| 5         | Critical Function            | Heat removal, power continuity, scheduling, checkpoint persistence, fabric transport. |
| 6         | Supporting system and assets | Cooling loop, UPS path, compute cluster, storage system, network fabric.              |

## 14. Capability Instance minimum record

| **Property**         | **Requirement**                                                                         |
|----------------------|-----------------------------------------------------------------------------------------|
| capabilityInstanceId | Globally or organisationally unique and immutable.                                      |
| name                 | Human-readable identifier.                                                              |
| capabilityType       | Controlled vocabulary value.                                                            |
| owner                | Accountable organisation or role.                                                       |
| locations            | Sites and zones in which it is instantiated.                                            |
| lifecycleStage       | Concept, design, construction, commissioning, ready, operational, change or retirement. |
| serviceOutcomes      | One or more outcome records.                                                            |
| criticality          | Declared and justified criticality.                                                     |
| assessmentBoundary   | Included systems and explicit exclusions.                                               |
| operatingEnvelope    | Load, environmental, capacity, duration and state constraints.                          |
| architectureBaseline | Approved design or configuration reference.                                             |
| effectivePeriod      | Start/end or point-in-time applicability.                                               |
| confidenceState      | Confirmed, partial, asserted, inferred, conflicting, stale or UNKNOWN.                  |

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

> **IOT-REQ-016** An Assessment Boundary shall identify included Capability Instances, sites, zones, systems, assets, interfaces, lifecycle stages and time horizon.
>
> **IOT-REQ-017** Every exclusion shall identify rationale, owner, residual dependency and effect on confidence.
>
> **IOT-REQ-018** External services shall be represented through boundary-crossing relationships and shall not be treated as inherently reliable.

## 17. Lifecycle stages

| **Stage**             | **Ontology emphasis**                                                              |
|-----------------------|------------------------------------------------------------------------------------|
| Concept               | Capability intent, candidate site, constraints, assumptions and target outcomes.   |
| Design                | Required functions, systems, architecture, capacity, fault domains and interfaces. |
| Construction          | Asset instances, installation state, deviations and provenance.                    |
| Commissioning         | Tests, observations, results, outstanding defects and accepted limitations.        |
| Operational readiness | Procedures, personnel, spares, monitoring and transfer of authority.               |
| Operation             | Current state, telemetry, maintenance, incidents, evidence and drift.              |
| Change                | Impact, configuration transition, temporary states, evidence and revalidation.     |
| Decommissioning       | Isolation, removal, sanitisation, residual hazards and record retention.           |

# Part V - Eight-domain infrastructure taxonomy

## 18. Taxonomy rules

> **IOT-REQ-019** Domain assignment shall indicate the primary classification only; cross-domain relationships shall remain explicit.
>
> **IOT-REQ-020** Technology-specific subclasses shall inherit canonical properties from vendor-neutral parent classes.
>
> **IOT-REQ-021** A taxonomy branch shall be extended only where the distinction changes assessment, dependency, evidence, failure or assurance meaning.

## 19. D1 Physical Data Centre Controls

| **Taxonomy family**          | **Illustrative subclasses**                                                                                                   |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Site and external perimeter  | Site, Campus, Property Boundary, Perimeter Barrier, Vehicle Barrier, Gate, Guard Post, External Approach, Standoff Zone       |
| Building and internal zoning | Building, Floor, Data Hall, Room, Cage, Suite, Row, Rack, Cabinet, Security Zone, Restricted Area, Loading Area, Staging Area |
| Entry and identity control   | Access Point, Turnstile, Mantrap, Door, Lock, Credential Reader, Biometric Reader, Visitor System, Key System                 |
| Detection and surveillance   | Camera, Video Management System, Intrusion Sensor, Door Contact, Motion Sensor, Security Alarm, Intercom                      |
| Asset movement and custody   | Loading Bay, Goods Lift, Screening Point, Storage Area, Seal, Chain-of-Custody Record                                         |
| Physical response            | Security Operations Centre, Guard Force, Response Procedure, Dispatch Channel, Incident Reconstruction Record                 |

## 20. D2 Facilities Engineering

| **Taxonomy family**               | **Illustrative subclasses**                                                                                                              |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Civil and structural              | Foundation, Floor Slab, Raised Floor, Roof, Wall, Ceiling, Rack Anchorage, Seismic Restraint, Load-Bearing Element                       |
| Electrical architecture           | Incoming Supply, Substation, Transformer, Switchgear, Protection Relay, Transfer Scheme, Earthing System, Lightning Protection           |
| Mechanical architecture           | Chilled Water Plant, Condenser System, Pump System, Air Distribution, Ventilation, Pressurisation, Drainage                              |
| Fire and life safety              | Detection Zone, Fire Alarm Panel, Suppression Zone, Agent System, Sprinkler System, Smoke Control, Emergency Egress, Emergency Power Off |
| Water and leak management         | Water Source, Pipework, Valve, Drain, Sump, Leak Detection Zone, Water Treatment System                                                  |
| Facility control and telemetry    | BMS, EPMS, SCADA, PLC, RTU, Sensor, Actuator, Gateway, Historian, Alarm Console                                                          |
| Engineering authority and records | Design Basis, Single-Line Diagram, P&ID, As-Built Drawing, Engineering Study, Commissioning Script, Deviation Record                     |

## 21. D3 Power and Cooling Resilience

| **Taxonomy family**               | **Illustrative subclasses**                                                                                                                    |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Utility and generation            | Utility Feed, Grid Connection, On-Site Generation, Generator, Fuel Tank, Fuel System, Starting System, Exhaust System                          |
| Power conversion and distribution | Transformer, MV Switchgear, LV Switchgear, UPS, Battery, Energy Storage, Static Transfer Switch, Busway, PDU, RPP, Rack PDU, Power Supply Unit |
| Power quality and protection      | Protection Device, Relay, Meter, Harmonic Filter, Surge Protection, Grounding, Power Quality Monitor                                           |
| Heat capture                      | Heat Sink, Cold Plate, Rear-Door Heat Exchanger, Air Handler, In-Row Cooler, Immersion Tank                                                    |
| Coolant distribution              | CDU, Primary Loop, Secondary Loop, Pump, Manifold, Quick Disconnect, Hose, Pipe, Heat Exchanger                                                |
| Heat rejection                    | Chiller, Cooling Tower, Dry Cooler, Condenser, Evaporative System, Heat-Reuse Interface                                                        |
| Thermal and leak monitoring       | Temperature Sensor, Humidity Sensor, Flow Sensor, Pressure Sensor, Leak Sensor, Coolant Quality Sensor, Thermal Camera                         |

## 22. D4 Environmental Standards and Resource Performance

| **Taxonomy family**             | **Illustrative subclasses**                                                                                    |
|---------------------------------|----------------------------------------------------------------------------------------------------------------|
| Energy resources                | Grid Electricity, Renewable Electricity, On-Site Energy, Stored Energy, Fuel                                   |
| Water resources                 | Potable Water, Process Water, Reclaimed Water, Cooling Water, Discharge Water                                  |
| Environmental conditions        | Ambient Temperature, Humidity, Air Quality, Particulate Level, Noise, Vibration, Flood Exposure, Heat Stress   |
| Material and chemical resources | Refrigerant, Coolant, Fire Suppressant, Battery Chemistry, Hazardous Material                                  |
| Performance indicators          | PUE Record, WUE Record, CUE Record, Energy Reuse Record, Cooling Efficiency Record, Compute Utilisation Record |
| Environmental obligations       | Permit, Reporting Requirement, Emission Limit, Water Limit, Waste Requirement, Environmental Commitment        |

## 23. D5 Building Operations

| **Taxonomy family**             | **Illustrative subclasses**                                                                                             |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Governance and authority        | Operating Model, Role, Delegation, Approval Authority, Escalation Path, Risk Acceptance                                 |
| Work control                    | Procedure, Method Statement, Permit to Work, Lockout Tagout, Maintenance Window, Change Record, Temporary Configuration |
| Maintenance and reliability     | Maintenance Plan, Work Order, Condition Monitoring, Inspection, Calibration, Spare Part, Obsolescence Record            |
| Staffing and competence         | Shift, Roster, Competency Record, Authorisation, Training Record, Contractor, Subject Matter Expert                     |
| Incident and emergency          | Alarm, Incident, Event Log, Emergency Procedure, Crisis Team, Exercise, Post-Incident Review                            |
| Supplier and service management | Supplier, Maintenance Contract, Service Level, Remote Support, Escalation Contact, Lead Time, Supply Constraint         |
| Configuration and documentation | Configuration Baseline, Asset Register, Drawing Register, Procedure Register, Revision, Document Custodian              |

## 24. D6 AI Compute Infrastructure

| **Taxonomy family**     | **Illustrative subclasses**                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Accelerated compute     | Accelerator, GPU, AI ASIC, Compute Node, GPU Baseboard, CPU, Memory, DPU, NIC                                                |
| Rack-scale systems      | Compute Tray, Rack-Scale System, Scale-Up Domain, NVLink Domain, Enclosure, Backplane, Power Shelf, Rack Controller          |
| Cluster systems         | Compute Cluster, Cluster Partition, Node Pool, Head Node, Login Node, Management Node, Provisioning Node                     |
| Management and firmware | BMC, Firmware, BIOS, Driver, Fabric Manager, Cluster Manager, Provisioning Service, Scheduler, Orchestrator                  |
| Workload infrastructure | Queue, Partition, Reservation, Container Runtime, Kubernetes Cluster, Job Scheduler, Checkpoint Agent                        |
| Compute observability   | GPU Telemetry, Node Telemetry, Health Service, Event Log, Performance Counter, Error Counter                                 |
| Compute lifecycle       | Golden Image, Firmware Baseline, Compatibility Matrix, Hardware Support Contract, RMA Process, Secure Decommissioning Record |

## 25. D7 AI Storage and Data Infrastructure

| **Taxonomy family**       | **Illustrative subclasses**                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------------------------|
| Storage systems           | Parallel File System, Scale-Out NAS, Object Storage, Block Storage, Local NVMe, Burst Buffer, Archive Storage |
| Storage nodes and media   | Storage Node, Metadata Server, Object Storage Node, Controller, SSD, HDD, Tape, NVRAM                         |
| Data-path services        | Namespace, Metadata Service, Data Mover, Cache, Gateway, Client Driver, Mount Service                         |
| AI artifact services      | Dataset Repository, Model Repository, Checkpoint Repository, Feature Store, Artifact Registry                 |
| Protection and recovery   | Snapshot, Replica, Backup Copy, Erasure Coding Group, Recovery Copy, Immutable Copy                           |
| Storage management        | Storage Manager, Capacity Manager, Tiering Policy, Retention Policy, Integrity Scanner, Telemetry Service     |
| Data logistics interfaces | Ingestion Interface, Export Interface, Data Transfer Node, WAN Transfer Service, Staging Area                 |

## 26. D8 AI Network and Interconnect Architecture

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
| Evidence status           | Confirmed, partially confirmed, asserted, inferred, conflicting, stale, UNKNOWN.                                                                |
| Replaceability            | Immediate, stocked spare, contractually replaceable, long-lead, irreplaceable, UNKNOWN.                                                         |
| Mobility                  | Fixed, relocatable, portable, virtualised, service-based.                                                                                       |
| Exposure                  | Public, campus, building, hall, cage, rack, management plane, isolated, UNKNOWN.                                                                |
| Sovereignty relevance     | Local control, foreign dependency, cross-border support, remote administration, jurisdiction-sensitive, not declared.                           |
| Environmental sensitivity | Temperature, humidity, water quality, vibration, particulate, altitude, electromagnetic, acoustic.                                              |

## 28. Criticality semantics

> **IOT-REQ-028** Criticality shall be assigned in relation to a Capability Instance and Service Outcome, not as an intrinsic universal property of an asset class.
>
> **IOT-REQ-029** Criticality rationale should consider consequence, time sensitivity, substitutability, concentration, recovery complexity, safety, regulatory and strategic significance.

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
| confidenceState    | Required                        | Confirmed through UNKNOWN.               |

# Part VIII - Relationship and dependency vocabulary

## 34. Relationship design rules

> **IOT-REQ-034** Every relationship shall identify subject, predicate and object; material relationships shall also identify scope, conditions, provenance, confidence and effective period.
>
> **IOT-REQ-035** Inverse relationships may be generated only where the canonical registry declares an inverse.
>
> **IOT-REQ-036** Symmetric relationships shall not be assumed for directional dependencies.
>
> **IOT-REQ-037** Transitive reasoning shall be applied only to approved predicates and shall not automatically infer engineering sufficiency.

## 35. Core structural relationships

| **Predicate**   | **Subject**     | **Object**         | **Logic**                 | **Inverse**        | **Meaning**                   |
|-----------------|-----------------|--------------------|---------------------------|--------------------|-------------------------------|
| PART_OF         | Entity          | Entity             | Transitive                | HAS_PART           | Composition.                  |
| CONTAINS        | Location/System | Entity             | Transitive                | LOCATED_IN/PART_OF | Containment.                  |
| LOCATED_IN      | Physical Entity | Location           | Transitive                | CONTAINS           | Physical placement.           |
| MEMBER_OF       | Entity          | Group              | No                        | HAS_MEMBER         | Group membership.             |
| IMPLEMENTS      | Asset/System    | Function           | No                        | IMPLEMENTED_BY     | Realises a required function. |
| SUPPORTS        | Entity          | Capability/Outcome | No                        | SUPPORTED_BY       | Contributes to outcome.       |
| INTERFACES_WITH | Entity          | Entity             | Symmetric                 | INTERFACES_WITH    | Defined exchange boundary.    |
| CONNECTED_TO    | Entity          | Entity             | Symmetric unless directed | CONNECTED_TO       | Realised connection.          |
| ROUTES_THROUGH  | Flow/Service    | Entity             | No                        | CARRIES            | Path relationship.            |

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
| RECOVERED_BY     | Entity/capability   | Recovery asset/process     | Restoration reliance.              |
| MAINTAINED_BY    | Entity              | Actor/organisation         | Maintenance reliance.              |
| OPERATED_BY      | Entity/system       | Actor/organisation         | Operational responsibility.        |
| EVIDENCED_BY     | Assertion/entity    | Evidence object            | Evidence support.                  |
| TESTED_BY        | Assertion/safeguard | Test record                | Validation link.                   |

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
| confidence          | Yes               | Confidence state and rationale.                                         |
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
> **IN_SAME_FAULT_DOMAIN_AS** Two entities are exposed to a declared common fault domain.
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

> **IOT-REQ-041** A capacity value shall identify metric, unit, entity, operating state, environmental conditions, duration, derating assumptions, evidence date and confidence.
>
> **IOT-REQ-042** Nameplate, installed, commissioned, available, committed, resilient and uncommitted capacity shall not be used interchangeably.
>
> **IOT-REQ-043** A cross-domain capacity claim shall identify the limiting dependency and any stranded capacity.

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

> **IOT-REQ-046** State transitions shall identify trigger, authority, preconditions, required safeguards, expected duration, monitoring, exit criteria and evidence.
>
> **IOT-REQ-047** Temporary bypass and maintenance configurations shall be represented as explicit states or configuration versions.
>
> **IOT-REQ-048** Assurance claims shall identify the operating states they cover and shall not be generalised to uncovered states.

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

| **Relationship** | **Meaning**                                          |
|------------------|------------------------------------------------------|
| OWNS             | Legal, financial or accountable ownership.           |
| OPERATES         | Performs routine operation.                          |
| CONTROLS         | Holds authority to command or configure.             |
| MAINTAINS        | Performs inspection, servicing and repair.           |
| SUPPLIES         | Provides a resource, product or service.             |
| MONITORS         | Observes state and raises information or alerts.     |
| APPROVES         | Authorises design, change, work or decision.         |
| ASSURES          | Performs independent or internal assurance activity. |
| ACCEPTS_RISK_FOR | Holds authority to accept residual exposure.         |
| CUSTODIAN_OF     | Maintains an evidence or information object.         |
| RESPONDS_TO      | Has response responsibility for an event or alarm.   |
| ESCALATES_TO     | Transfers information or decision authority.         |

## 51. Shared-responsibility record

> **IOT-REQ-051** A shared-responsibility allocation shall identify function, assets, lifecycle stages, operating states, responsible party, accountable party, consulted parties, evidence custodian and unresolved gaps.
>
> **IOT-REQ-052** Contractual responsibility shall not be treated as proof of operational capability or control effectiveness.

## 52. Evidence attachment model

| **Evidence relation**  | **Meaning**                                                |
|------------------------|------------------------------------------------------------|
| SUPPORTS_ASSERTION     | Evidence supports a testable statement.                    |
| CHALLENGES_ASSERTION   | Evidence contradicts or weakens a statement.               |
| OBSERVES_ENTITY        | Evidence records the state of an entity.                   |
| VALIDATES_SAFEGUARD    | Evidence demonstrates a safeguard under stated conditions. |
| ESTABLISHES_PROVENANCE | Evidence identifies source, origin or custody.             |
| COVERS_PERIOD          | Evidence applies to a declared period.                     |
| COVERS_STATE           | Evidence applies to one or more operating states.          |
| CONFLICTS_WITH         | Evidence is inconsistent with another evidence object.     |
| SUPERSEDES             | Newer controlled evidence replaces an earlier record.      |

## 53. Confidence states

| **State**           | **Meaning**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| CONFIRMED           | Direct, relevant and sufficiently current evidence supports the assertion.  |
| PARTIALLY_CONFIRMED | Evidence supports part of the assertion or scope.                           |
| ASSERTED            | Claim provided by an accountable source but not independently corroborated. |
| INFERRED            | Derived from related facts using declared reasoning.                        |
| CONFLICTING         | Material sources disagree and conflict remains unresolved.                  |
| STALE               | Evidence or observation is no longer sufficiently current.                  |
| UNKNOWN             | Information is insufficient to reach a defensible state.                    |

## 54. UNKNOWN doctrine

> **IOT-REQ-054** UNKNOWN may apply to an entity existence, class, property, relationship, state, capacity, owner, evidence status or conclusion.
>
> **IOT-REQ-055** UNKNOWN shall identify the missing information, why it matters, current owner for resolution where known, and assurance impact.
>
> **IOT-REQ-056** UNKNOWN shall not be replaced with an assumed favourable value to enable scoring or certification.

## 55. Conflict representation

Conflicting records shall be retained with separate provenance and effective periods. A resolution record may select, reconcile or reject assertions, but the original conflict trail should remain auditable.

# Part XII - Conformance rules and validation shapes

## 56. Core validation rules

| **Rule** | **Validation statement**                                                                                                  |
|----------|---------------------------------------------------------------------------------------------------------------------------|
| VAL-001  | Every Capability Instance has at least one Service Outcome.                                                               |
| VAL-002  | Every Service Outcome is supported by at least one Critical Function.                                                     |
| VAL-003  | Every Critical Function is implemented by at least one System, Asset or external service, or is UNKNOWN.                  |
| VAL-004  | Every material physical Asset has a Location or UNKNOWN.                                                                  |
| VAL-005  | Every material Asset has an owner and operator or explicit UNKNOWN.                                                       |
| VAL-006  | Every boundary-crossing dependency identifies an external provider or UNKNOWN.                                            |
| VAL-007  | Every capacity assertion has metric, unit, state, condition, time and confidence.                                         |
| VAL-008  | Every redundancy claim identifies protected function, alternatives, transfer mechanism, common dependencies and evidence. |
| VAL-009  | Every independence claim is evidence-backed and condition-bounded.                                                        |
| VAL-010  | Every critical dependency identifies applicable states and strength.                                                      |
| VAL-011  | Every assurance-relevant relationship has provenance and effective period.                                                |
| VAL-012  | Every asset class derives from a canonical or registered extension class.                                                 |
| VAL-013  | Every Change Event links affected entities and assurance impact.                                                          |
| VAL-014  | Every UNKNOWN record states the unresolved attribute and its consequence.                                                 |
| VAL-015  | Every Service Outcome and resilience claim is tied to a Capability Instance and Operating Envelope.                       |
| VAL-016  | No evidence object is treated as a safeguard; it evidences a safeguard or assertion.                                      |
| VAL-017  | No control abstraction is represented as proof that a real safeguard exists.                                              |
| VAL-018  | No maturity value automatically creates an assurance decision.                                                            |
| VAL-019  | No excluded dependency is removed from the capability dependency view.                                                    |
| VAL-020  | No vendor-specific term replaces its canonical parent in cross-profile exchange.                                          |

## 57. Quality tests

| **Test family**          | **Questions**                                                                                           |
|--------------------------|---------------------------------------------------------------------------------------------------------|
| Completeness             | Are material capabilities, outcomes, functions, assets, external services and dependencies represented? |
| Consistency              | Do class and relationship uses obey definitions and cardinalities?                                      |
| Traceability             | Can each material assertion be traced to evidence and provenance?                                       |
| Currency                 | Do effective dates and configuration states reflect the assessment point in time?                       |
| Boundary integrity       | Are exclusions and boundary-crossing dependencies visible?                                              |
| Cross-domain integration | Do power, cooling, control, compute, storage and network chains connect?                                |
| Failure readiness        | Can Artifact 4 attach causes, failure modes, propagation and consequences without semantic gaps?        |
| Assurance readiness      | Can safeguards, evidence, findings and decisions attach to the represented subject?                     |
| Interoperability         | Can the dataset be exported using controlled identifiers and namespaces?                                |
| Human usability          | Can engineers and assessors interpret the model without specialist graph tooling?                       |

## 58. Prohibited modelling practices

- Using a single building-level rating as a property of every hosted capability.

- Treating product type as proof of performance or compliance.

- Hiding external dependencies because they are contractually assigned.

- Representing nominal redundancy without shared-dependency analysis.

- Combining designed, as-built and observed states into one unqualified record.

- Encoding UNKNOWN as zero, false, pass, fail or not applicable.

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
| Critical Functions        | Electrical continuity; heat capture and rejection; scale-out transport; metadata access; checkpoint persistence; scheduling.                  |
| Systems                   | Compute cluster; rack power path; liquid cooling system; parallel storage; AI fabric; management system.                                      |
| Boundary                  | Defined halls, racks, infrastructure systems and external utility/OEM services.                                                               |
| Cross-domain dependencies | Utility -\> UPS -\> busway -\> rack; cold plate -\> secondary loop -\> CDU -\> facility loop -\> heat rejection; node -\> fabric -\> storage. |
| Fault domains             | Rack-scale compute domain; CDU loop; electrical path; fabric plane; storage protection group; operator team.                                  |
| Operating states          | Normal, single-path maintenance, degraded cooling, recovery and transition.                                                                   |
| Critical UNKNOWN examples | Unverified secondary-loop autonomy; unclear shared controller; stale resilient-capacity study.                                                |
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
| aidcf-vocabulary-v1.0.csv          | Controlled term register.                |
| aidcf-relationships-v1.0.csv       | Relationship registry.                   |
| aidcf-example-minimal-v1.0.jsonld  | Minimal conformant example.              |
| aidcf-example-training-v1.0.jsonld | Worked training-cluster profile.         |
| CHANGELOG.md                       | Version history and changes.             |
| MIGRATION.md                       | Compatibility and migration guidance.    |
| LICENSE.md                         | Usage and extension rules.               |

## 63. Namespace policy

Recommended public namespace pattern: https://w3id.org/aidcf/iot/1.0/. A permanent redirect service or another governed persistent identifier may be selected before publication. Draft namespaces shall be clearly marked and shall not be represented as stable production identifiers.

## 64. Identifier rules

- Class identifiers use PascalCase, for example CapabilityInstance.

- Relationship identifiers use UPPER_SNAKE_CASE in human registries and stable lowerCamelCase or IRI form in machine schemas.

- Instance identifiers shall be opaque enough to avoid embedding sensitive facility details.

- Identifiers shall not be reassigned after retirement.

- Human-readable labels may change without changing semantic identifiers where meaning is stable.

- Breaking semantic changes require a new major namespace version.

## 65. JSON exchange skeleton

{  
"@context": "https://w3id.org/aidcf/iot/1.0/context.jsonld",  
"id": "capability-instance:example-001",  
"type": "CapabilityInstance",  
"name": "Example distributed training capability",  
"serviceOutcomes": \["outcome:compute-capacity", "outcome:checkpoint-recovery"\],  
"assessmentBoundary": "boundary:example-001",  
"operatingEnvelope": "envelope:example-001",  
"supportedBy": \["system:compute-cluster", "system:cooling-loop", "system:power-path"\],  
"confidenceState": "ASSERTED"  
}

## 66. Extension governance

> **IOT-REQ-066** An extension shall publish namespace, owner, scope, parent mappings, definitions, constraints, examples, tests, version and compatibility statement.
>
> **IOT-REQ-067** A profile shall not weaken canonical validation rules without declaring a nonconformance.
>
> **IOT-REQ-068** Vendor mappings should map product terms to canonical classes rather than creating competing upper ontologies.

## 67. Integration boundary with AI Trust Graph

| **AIDCF primary semantics**                                                                                              | **Shared handoff**                                                                                                    | **AI Trust Graph primary semantics**                                                                        |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Site, building, power, cooling, facility OT, physical assets, compute hardware, storage infrastructure and interconnect. | Identifiers, evidence, infrastructure services, machine identities, management interfaces, dependencies and findings. | Models, agents, tools, APIs, human and machine identities, authority, reachability and digital trust paths. |

# Appendix A - Canonical class registry

| **Canonical ID**                   | **Preferred label**            | **Definition / use**                                                                                       | **Domain** |
|------------------------------------|--------------------------------|------------------------------------------------------------------------------------------------------------|------------|
| AIDCF:Capability                   | Capability                     | An intended operational ability supported by infrastructure.                                               | Core       |
| AIDCF:CapabilityInstance           | Capability Instance            | A specific deployment bounded by ownership, location, architecture, capacity, criticality and obligations. | Core       |
| AIDCF:ServiceOutcome               | Service Outcome                | A measurable or assessable result required from a Capability Instance.                                     | Core       |
| AIDCF:CriticalFunction             | Critical Function              | A function whose loss or degradation materially affects a Service Outcome.                                 | Core       |
| AIDCF:AssessmentBoundary           | Assessment Boundary            | The declared inclusion perimeter for direct assessment.                                                    | Core       |
| AIDCF:OperatingEnvelope            | Operating Envelope             | The bounded conditions under which a capability or system is intended to operate.                          | Core       |
| AIDCF:InfrastructureSystem         | Infrastructure System          | A coordinated set of assets and interfaces providing one or more functions.                                | Core       |
| AIDCF:AssetInstance                | Asset Instance                 | An identifiable real-world item, service, person, procedure or resource.                                   | Core       |
| AIDCF:Component                    | Component                      | A constituent part of an asset or system represented where material.                                       | Core       |
| AIDCF:Interface                    | Interface                      | A defined point or mechanism of exchange between entities.                                                 | Core       |
| AIDCF:Connection                   | Connection                     | A realised physical, logical, hydraulic, electrical, thermal or organisational link.                       | Core       |
| AIDCF:Resource                     | Resource                       | Consumable or constrained input required for operation.                                                    | Core       |
| AIDCF:Location                     | Location                       | A geographic, site, building, zone, room, row, rack or logical placement.                                  | Core       |
| AIDCF:Dependency                   | Dependency                     | A reliance by one entity upon another entity, resource, condition or decision.                             | Core       |
| AIDCF:FaultDomain                  | Fault Domain                   | A set of entities expected to be affected by a common failure.                                             | Core       |
| AIDCF:RedundancyGroup              | Redundancy Group               | Assets or paths deliberately arranged to preserve a function.                                              | Core       |
| AIDCF:Safeguard                    | Safeguard                      | A real-world measure intended to anticipate, prevent, detect, contain, respond, recover or adapt.          | Core       |
| AIDCF:EvidenceObject               | Evidence Object                | A record or observation used to support or challenge an assertion.                                         | Core       |
| AIDCF:Actor                        | Actor                          | A human or machine participant with a relevant role.                                                       | Core       |
| AIDCF:Organisation                 | Organisation                   | A legally or operationally recognised party.                                                               | Core       |
| AIDCF:Role                         | Role                           | A named set of responsibilities and authorities.                                                           | Core       |
| AIDCF:OperatingState               | Operating State                | A defined condition of operation.                                                                          | Core       |
| AIDCF:ChangeEvent                  | Change Event                   | An approved, observed or unapproved modification affecting the represented system.                         | Core       |
| AIDCF:Site                         | Site                           | Site as classified within Site and external perimeter.                                                     | D1         |
| AIDCF:Campus                       | Campus                         | Campus as classified within Site and external perimeter.                                                   | D1         |
| AIDCF:PropertyBoundary             | Property Boundary              | Property Boundary as classified within Site and external perimeter.                                        | D1         |
| AIDCF:PerimeterBarrier             | Perimeter Barrier              | Perimeter Barrier as classified within Site and external perimeter.                                        | D1         |
| AIDCF:VehicleBarrier               | Vehicle Barrier                | Vehicle Barrier as classified within Site and external perimeter.                                          | D1         |
| AIDCF:Gate                         | Gate                           | Gate as classified within Site and external perimeter.                                                     | D1         |
| AIDCF:GuardPost                    | Guard Post                     | Guard Post as classified within Site and external perimeter.                                               | D1         |
| AIDCF:ExternalApproach             | External Approach              | External Approach as classified within Site and external perimeter.                                        | D1         |
| AIDCF:StandoffZone                 | Standoff Zone                  | Standoff Zone as classified within Site and external perimeter.                                            | D1         |
| AIDCF:Building                     | Building                       | Building as classified within Building and internal zoning.                                                | D1         |
| AIDCF:Floor                        | Floor                          | Floor as classified within Building and internal zoning.                                                   | D1         |
| AIDCF:DataHall                     | Data Hall                      | Data Hall as classified within Building and internal zoning.                                               | D1         |
| AIDCF:Room                         | Room                           | Room as classified within Building and internal zoning.                                                    | D1         |
| AIDCF:Cage                         | Cage                           | Cage as classified within Building and internal zoning.                                                    | D1         |
| AIDCF:Suite                        | Suite                          | Suite as classified within Building and internal zoning.                                                   | D1         |
| AIDCF:Row                          | Row                            | Row as classified within Building and internal zoning.                                                     | D1         |
| AIDCF:Rack                         | Rack                           | Rack as classified within Building and internal zoning.                                                    | D1         |
| AIDCF:Cabinet                      | Cabinet                        | Cabinet as classified within Building and internal zoning.                                                 | D1         |
| AIDCF:SecurityZone                 | Security Zone                  | Security Zone as classified within Building and internal zoning.                                           | D1         |
| AIDCF:RestrictedArea               | Restricted Area                | Restricted Area as classified within Building and internal zoning.                                         | D1         |
| AIDCF:LoadingArea                  | Loading Area                   | Loading Area as classified within Building and internal zoning.                                            | D1         |
| AIDCF:StagingArea                  | Staging Area                   | Staging Area as classified within Building and internal zoning.                                            | D1         |
| AIDCF:AccessPoint                  | Access Point                   | Access Point as classified within Entry and identity control.                                              | D1         |
| AIDCF:Turnstile                    | Turnstile                      | Turnstile as classified within Entry and identity control.                                                 | D1         |
| AIDCF:Mantrap                      | Mantrap                        | Mantrap as classified within Entry and identity control.                                                   | D1         |
| AIDCF:Door                         | Door                           | Door as classified within Entry and identity control.                                                      | D1         |
| AIDCF:Lock                         | Lock                           | Lock as classified within Entry and identity control.                                                      | D1         |
| AIDCF:CredentialReader             | Credential Reader              | Credential Reader as classified within Entry and identity control.                                         | D1         |
| AIDCF:BiometricReader              | Biometric Reader               | Biometric Reader as classified within Entry and identity control.                                          | D1         |
| AIDCF:VisitorSystem                | Visitor System                 | Visitor System as classified within Entry and identity control.                                            | D1         |
| AIDCF:KeySystem                    | Key System                     | Key System as classified within Entry and identity control.                                                | D1         |
| AIDCF:Camera                       | Camera                         | Camera as classified within Detection and surveillance.                                                    | D1         |
| AIDCF:VideoManagementSystem        | Video Management System        | Video Management System as classified within Detection and surveillance.                                   | D1         |
| AIDCF:IntrusionSensor              | Intrusion Sensor               | Intrusion Sensor as classified within Detection and surveillance.                                          | D1         |
| AIDCF:DoorContact                  | Door Contact                   | Door Contact as classified within Detection and surveillance.                                              | D1         |
| AIDCF:MotionSensor                 | Motion Sensor                  | Motion Sensor as classified within Detection and surveillance.                                             | D1         |
| AIDCF:SecurityAlarm                | Security Alarm                 | Security Alarm as classified within Detection and surveillance.                                            | D1         |
| AIDCF:Intercom                     | Intercom                       | Intercom as classified within Detection and surveillance.                                                  | D1         |
| AIDCF:LoadingBay                   | Loading Bay                    | Loading Bay as classified within Asset movement and custody.                                               | D1         |
| AIDCF:GoodsLift                    | Goods Lift                     | Goods Lift as classified within Asset movement and custody.                                                | D1         |
| AIDCF:ScreeningPoint               | Screening Point                | Screening Point as classified within Asset movement and custody.                                           | D1         |
| AIDCF:StorageArea                  | Storage Area                   | Storage Area as classified within Asset movement and custody.                                              | D1         |
| AIDCF:Seal                         | Seal                           | Seal as classified within Asset movement and custody.                                                      | D1         |
| AIDCF:Chain-of-CustodyRecord       | Chain-of-Custody Record        | Chain-of-Custody Record as classified within Asset movement and custody.                                   | D1         |
| AIDCF:SecurityOperationsCentre     | Security Operations Centre     | Security Operations Centre as classified within Physical response.                                         | D1         |
| AIDCF:GuardForce                   | Guard Force                    | Guard Force as classified within Physical response.                                                        | D1         |
| AIDCF:ResponseProcedure            | Response Procedure             | Response Procedure as classified within Physical response.                                                 | D1         |
| AIDCF:DispatchChannel              | Dispatch Channel               | Dispatch Channel as classified within Physical response.                                                   | D1         |
| AIDCF:IncidentReconstructionRecord | Incident Reconstruction Record | Incident Reconstruction Record as classified within Physical response.                                     | D1         |
| AIDCF:Foundation                   | Foundation                     | Foundation as classified within Civil and structural.                                                      | D2         |
| AIDCF:FloorSlab                    | Floor Slab                     | Floor Slab as classified within Civil and structural.                                                      | D2         |
| AIDCF:RaisedFloor                  | Raised Floor                   | Raised Floor as classified within Civil and structural.                                                    | D2         |
| AIDCF:Roof                         | Roof                           | Roof as classified within Civil and structural.                                                            | D2         |
| AIDCF:Wall                         | Wall                           | Wall as classified within Civil and structural.                                                            | D2         |
| AIDCF:Ceiling                      | Ceiling                        | Ceiling as classified within Civil and structural.                                                         | D2         |
| AIDCF:RackAnchorage                | Rack Anchorage                 | Rack Anchorage as classified within Civil and structural.                                                  | D2         |
| AIDCF:SeismicRestraint             | Seismic Restraint              | Seismic Restraint as classified within Civil and structural.                                               | D2         |
| AIDCF:Load-BearingElement          | Load-Bearing Element           | Load-Bearing Element as classified within Civil and structural.                                            | D2         |
| AIDCF:IncomingSupply               | Incoming Supply                | Incoming Supply as classified within Electrical architecture.                                              | D2         |
| AIDCF:Substation                   | Substation                     | Substation as classified within Electrical architecture.                                                   | D2         |
| AIDCF:Transformer                  | Transformer                    | Transformer as classified within Electrical architecture.                                                  | D2         |
| AIDCF:Switchgear                   | Switchgear                     | Switchgear as classified within Electrical architecture.                                                   | D2         |
| AIDCF:ProtectionRelay              | Protection Relay               | Protection Relay as classified within Electrical architecture.                                             | D2         |
| AIDCF:TransferScheme               | Transfer Scheme                | Transfer Scheme as classified within Electrical architecture.                                              | D2         |
| AIDCF:EarthingSystem               | Earthing System                | Earthing System as classified within Electrical architecture.                                              | D2         |
| AIDCF:LightningProtection          | Lightning Protection           | Lightning Protection as classified within Electrical architecture.                                         | D2         |
| AIDCF:ChilledWaterPlant            | Chilled Water Plant            | Chilled Water Plant as classified within Mechanical architecture.                                          | D2         |
| AIDCF:CondenserSystem              | Condenser System               | Condenser System as classified within Mechanical architecture.                                             | D2         |
| AIDCF:PumpSystem                   | Pump System                    | Pump System as classified within Mechanical architecture.                                                  | D2         |
| AIDCF:AirDistribution              | Air Distribution               | Air Distribution as classified within Mechanical architecture.                                             | D2         |
| AIDCF:Ventilation                  | Ventilation                    | Ventilation as classified within Mechanical architecture.                                                  | D2         |
| AIDCF:Pressurisation               | Pressurisation                 | Pressurisation as classified within Mechanical architecture.                                               | D2         |
| AIDCF:Drainage                     | Drainage                       | Drainage as classified within Mechanical architecture.                                                     | D2         |
| AIDCF:DetectionZone                | Detection Zone                 | Detection Zone as classified within Fire and life safety.                                                  | D2         |
| AIDCF:FireAlarmPanel               | Fire Alarm Panel               | Fire Alarm Panel as classified within Fire and life safety.                                                | D2         |
| AIDCF:SuppressionZone              | Suppression Zone               | Suppression Zone as classified within Fire and life safety.                                                | D2         |
| AIDCF:AgentSystem                  | Agent System                   | Agent System as classified within Fire and life safety.                                                    | D2         |
| AIDCF:SprinklerSystem              | Sprinkler System               | Sprinkler System as classified within Fire and life safety.                                                | D2         |
| AIDCF:SmokeControl                 | Smoke Control                  | Smoke Control as classified within Fire and life safety.                                                   | D2         |
| AIDCF:EmergencyEgress              | Emergency Egress               | Emergency Egress as classified within Fire and life safety.                                                | D2         |
| AIDCF:EmergencyPowerOff            | Emergency Power Off            | Emergency Power Off as classified within Fire and life safety.                                             | D2         |
| AIDCF:WaterSource                  | Water Source                   | Water Source as classified within Water and leak management.                                               | D2         |
| AIDCF:Pipework                     | Pipework                       | Pipework as classified within Water and leak management.                                                   | D2         |
| AIDCF:Valve                        | Valve                          | Valve as classified within Water and leak management.                                                      | D2         |
| AIDCF:Drain                        | Drain                          | Drain as classified within Water and leak management.                                                      | D2         |
| AIDCF:Sump                         | Sump                           | Sump as classified within Water and leak management.                                                       | D2         |
| AIDCF:LeakDetectionZone            | Leak Detection Zone            | Leak Detection Zone as classified within Water and leak management.                                        | D2         |
| AIDCF:WaterTreatmentSystem         | Water Treatment System         | Water Treatment System as classified within Water and leak management.                                     | D2         |
| AIDCF:BMS                          | BMS                            | BMS as classified within Facility control and telemetry.                                                   | D2         |
| AIDCF:EPMS                         | EPMS                           | EPMS as classified within Facility control and telemetry.                                                  | D2         |
| AIDCF:SCADA                        | SCADA                          | SCADA as classified within Facility control and telemetry.                                                 | D2         |
| AIDCF:PLC                          | PLC                            | PLC as classified within Facility control and telemetry.                                                   | D2         |
| AIDCF:RTU                          | RTU                            | RTU as classified within Facility control and telemetry.                                                   | D2         |
| AIDCF:Sensor                       | Sensor                         | Sensor as classified within Facility control and telemetry.                                                | D2         |
| AIDCF:Actuator                     | Actuator                       | Actuator as classified within Facility control and telemetry.                                              | D2         |
| AIDCF:Gateway                      | Gateway                        | Gateway as classified within Facility control and telemetry.                                               | D2         |
| AIDCF:Historian                    | Historian                      | Historian as classified within Facility control and telemetry.                                             | D2         |
| AIDCF:AlarmConsole                 | Alarm Console                  | Alarm Console as classified within Facility control and telemetry.                                         | D2         |
| AIDCF:DesignBasis                  | Design Basis                   | Design Basis as classified within Engineering authority and records.                                       | D2         |
| AIDCF:Single-LineDiagram           | Single-Line Diagram            | Single-Line Diagram as classified within Engineering authority and records.                                | D2         |
| AIDCF:P&ID                         | P&ID                           | P&ID as classified within Engineering authority and records.                                               | D2         |
| AIDCF:As-BuiltDrawing              | As-Built Drawing               | As-Built Drawing as classified within Engineering authority and records.                                   | D2         |
| AIDCF:EngineeringStudy             | Engineering Study              | Engineering Study as classified within Engineering authority and records.                                  | D2         |
| AIDCF:CommissioningScript          | Commissioning Script           | Commissioning Script as classified within Engineering authority and records.                               | D2         |
| AIDCF:DeviationRecord              | Deviation Record               | Deviation Record as classified within Engineering authority and records.                                   | D2         |
| AIDCF:UtilityFeed                  | Utility Feed                   | Utility Feed as classified within Utility and generation.                                                  | D3         |
| AIDCF:GridConnection               | Grid Connection                | Grid Connection as classified within Utility and generation.                                               | D3         |
| AIDCF:On-SiteGeneration            | On-Site Generation             | On-Site Generation as classified within Utility and generation.                                            | D3         |
| AIDCF:Generator                    | Generator                      | Generator as classified within Utility and generation.                                                     | D3         |
| AIDCF:FuelTank                     | Fuel Tank                      | Fuel Tank as classified within Utility and generation.                                                     | D3         |
| AIDCF:FuelSystem                   | Fuel System                    | Fuel System as classified within Utility and generation.                                                   | D3         |
| AIDCF:StartingSystem               | Starting System                | Starting System as classified within Utility and generation.                                               | D3         |
| AIDCF:ExhaustSystem                | Exhaust System                 | Exhaust System as classified within Utility and generation.                                                | D3         |
| AIDCF:Transformer                  | Transformer                    | Transformer as classified within Power conversion and distribution.                                        | D3         |
| AIDCF:MVSwitchgear                 | MV Switchgear                  | MV Switchgear as classified within Power conversion and distribution.                                      | D3         |
| AIDCF:LVSwitchgear                 | LV Switchgear                  | LV Switchgear as classified within Power conversion and distribution.                                      | D3         |
| AIDCF:UPS                          | UPS                            | UPS as classified within Power conversion and distribution.                                                | D3         |
| AIDCF:Battery                      | Battery                        | Battery as classified within Power conversion and distribution.                                            | D3         |
| AIDCF:EnergyStorage                | Energy Storage                 | Energy Storage as classified within Power conversion and distribution.                                     | D3         |
| AIDCF:StaticTransferSwitch         | Static Transfer Switch         | Static Transfer Switch as classified within Power conversion and distribution.                             | D3         |
| AIDCF:Busway                       | Busway                         | Busway as classified within Power conversion and distribution.                                             | D3         |
| AIDCF:PDU                          | PDU                            | PDU as classified within Power conversion and distribution.                                                | D3         |
| AIDCF:RPP                          | RPP                            | RPP as classified within Power conversion and distribution.                                                | D3         |
| AIDCF:RackPDU                      | Rack PDU                       | Rack PDU as classified within Power conversion and distribution.                                           | D3         |
| AIDCF:PowerSupplyUnit              | Power Supply Unit              | Power Supply Unit as classified within Power conversion and distribution.                                  | D3         |
| AIDCF:ProtectionDevice             | Protection Device              | Protection Device as classified within Power quality and protection.                                       | D3         |
| AIDCF:Relay                        | Relay                          | Relay as classified within Power quality and protection.                                                   | D3         |
| AIDCF:Meter                        | Meter                          | Meter as classified within Power quality and protection.                                                   | D3         |
| AIDCF:HarmonicFilter               | Harmonic Filter                | Harmonic Filter as classified within Power quality and protection.                                         | D3         |
| AIDCF:SurgeProtection              | Surge Protection               | Surge Protection as classified within Power quality and protection.                                        | D3         |
| AIDCF:Grounding                    | Grounding                      | Grounding as classified within Power quality and protection.                                               | D3         |
| AIDCF:PowerQualityMonitor          | Power Quality Monitor          | Power Quality Monitor as classified within Power quality and protection.                                   | D3         |
| AIDCF:HeatSink                     | Heat Sink                      | Heat Sink as classified within Heat capture.                                                               | D3         |
| AIDCF:ColdPlate                    | Cold Plate                     | Cold Plate as classified within Heat capture.                                                              | D3         |
| AIDCF:Rear-DoorHeatExchanger       | Rear-Door Heat Exchanger       | Rear-Door Heat Exchanger as classified within Heat capture.                                                | D3         |
| AIDCF:AirHandler                   | Air Handler                    | Air Handler as classified within Heat capture.                                                             | D3         |
| AIDCF:In-RowCooler                 | In-Row Cooler                  | In-Row Cooler as classified within Heat capture.                                                           | D3         |
| AIDCF:ImmersionTank                | Immersion Tank                 | Immersion Tank as classified within Heat capture.                                                          | D3         |
| AIDCF:CDU                          | CDU                            | CDU as classified within Coolant distribution.                                                             | D3         |
| AIDCF:PrimaryLoop                  | Primary Loop                   | Primary Loop as classified within Coolant distribution.                                                    | D3         |
| AIDCF:SecondaryLoop                | Secondary Loop                 | Secondary Loop as classified within Coolant distribution.                                                  | D3         |
| AIDCF:Pump                         | Pump                           | Pump as classified within Coolant distribution.                                                            | D3         |
| AIDCF:Manifold                     | Manifold                       | Manifold as classified within Coolant distribution.                                                        | D3         |
| AIDCF:QuickDisconnect              | Quick Disconnect               | Quick Disconnect as classified within Coolant distribution.                                                | D3         |
| AIDCF:Hose                         | Hose                           | Hose as classified within Coolant distribution.                                                            | D3         |
| AIDCF:Pipe                         | Pipe                           | Pipe as classified within Coolant distribution.                                                            | D3         |
| AIDCF:HeatExchanger                | Heat Exchanger                 | Heat Exchanger as classified within Coolant distribution.                                                  | D3         |
| AIDCF:Chiller                      | Chiller                        | Chiller as classified within Heat rejection.                                                               | D3         |
| AIDCF:CoolingTower                 | Cooling Tower                  | Cooling Tower as classified within Heat rejection.                                                         | D3         |
| AIDCF:DryCooler                    | Dry Cooler                     | Dry Cooler as classified within Heat rejection.                                                            | D3         |
| AIDCF:Condenser                    | Condenser                      | Condenser as classified within Heat rejection.                                                             | D3         |
| AIDCF:EvaporativeSystem            | Evaporative System             | Evaporative System as classified within Heat rejection.                                                    | D3         |
| AIDCF:Heat-ReuseInterface          | Heat-Reuse Interface           | Heat-Reuse Interface as classified within Heat rejection.                                                  | D3         |
| AIDCF:TemperatureSensor            | Temperature Sensor             | Temperature Sensor as classified within Thermal and leak monitoring.                                       | D3         |
| AIDCF:HumiditySensor               | Humidity Sensor                | Humidity Sensor as classified within Thermal and leak monitoring.                                          | D3         |
| AIDCF:FlowSensor                   | Flow Sensor                    | Flow Sensor as classified within Thermal and leak monitoring.                                              | D3         |
| AIDCF:PressureSensor               | Pressure Sensor                | Pressure Sensor as classified within Thermal and leak monitoring.                                          | D3         |
| AIDCF:LeakSensor                   | Leak Sensor                    | Leak Sensor as classified within Thermal and leak monitoring.                                              | D3         |
| AIDCF:CoolantQualitySensor         | Coolant Quality Sensor         | Coolant Quality Sensor as classified within Thermal and leak monitoring.                                   | D3         |
| AIDCF:ThermalCamera                | Thermal Camera                 | Thermal Camera as classified within Thermal and leak monitoring.                                           | D3         |
| AIDCF:GridElectricity              | Grid Electricity               | Grid Electricity as classified within Energy resources.                                                    | D4         |
| AIDCF:RenewableElectricity         | Renewable Electricity          | Renewable Electricity as classified within Energy resources.                                               | D4         |
| AIDCF:On-SiteEnergy                | On-Site Energy                 | On-Site Energy as classified within Energy resources.                                                      | D4         |
| AIDCF:StoredEnergy                 | Stored Energy                  | Stored Energy as classified within Energy resources.                                                       | D4         |
| AIDCF:Fuel                         | Fuel                           | Fuel as classified within Energy resources.                                                                | D4         |
| AIDCF:PotableWater                 | Potable Water                  | Potable Water as classified within Water resources.                                                        | D4         |
| AIDCF:ProcessWater                 | Process Water                  | Process Water as classified within Water resources.                                                        | D4         |
| AIDCF:ReclaimedWater               | Reclaimed Water                | Reclaimed Water as classified within Water resources.                                                      | D4         |
| AIDCF:CoolingWater                 | Cooling Water                  | Cooling Water as classified within Water resources.                                                        | D4         |
| AIDCF:DischargeWater               | Discharge Water                | Discharge Water as classified within Water resources.                                                      | D4         |
| AIDCF:AmbientTemperature           | Ambient Temperature            | Ambient Temperature as classified within Environmental conditions.                                         | D4         |
| AIDCF:Humidity                     | Humidity                       | Humidity as classified within Environmental conditions.                                                    | D4         |
| AIDCF:AirQuality                   | Air Quality                    | Air Quality as classified within Environmental conditions.                                                 | D4         |
| AIDCF:ParticulateLevel             | Particulate Level              | Particulate Level as classified within Environmental conditions.                                           | D4         |
| AIDCF:Noise                        | Noise                          | Noise as classified within Environmental conditions.                                                       | D4         |
| AIDCF:Vibration                    | Vibration                      | Vibration as classified within Environmental conditions.                                                   | D4         |
| AIDCF:FloodExposure                | Flood Exposure                 | Flood Exposure as classified within Environmental conditions.                                              | D4         |
| AIDCF:HeatStress                   | Heat Stress                    | Heat Stress as classified within Environmental conditions.                                                 | D4         |
| AIDCF:Refrigerant                  | Refrigerant                    | Refrigerant as classified within Material and chemical resources.                                          | D4         |
| AIDCF:Coolant                      | Coolant                        | Coolant as classified within Material and chemical resources.                                              | D4         |
| AIDCF:FireSuppressant              | Fire Suppressant               | Fire Suppressant as classified within Material and chemical resources.                                     | D4         |
| AIDCF:BatteryChemistry             | Battery Chemistry              | Battery Chemistry as classified within Material and chemical resources.                                    | D4         |
| AIDCF:HazardousMaterial            | Hazardous Material             | Hazardous Material as classified within Material and chemical resources.                                   | D4         |
| AIDCF:PUERecord                    | PUE Record                     | PUE Record as classified within Performance indicators.                                                    | D4         |
| AIDCF:WUERecord                    | WUE Record                     | WUE Record as classified within Performance indicators.                                                    | D4         |
| AIDCF:CUERecord                    | CUE Record                     | CUE Record as classified within Performance indicators.                                                    | D4         |
| AIDCF:EnergyReuseRecord            | Energy Reuse Record            | Energy Reuse Record as classified within Performance indicators.                                           | D4         |
| AIDCF:CoolingEfficiencyRecord      | Cooling Efficiency Record      | Cooling Efficiency Record as classified within Performance indicators.                                     | D4         |
| AIDCF:ComputeUtilisationRecord     | Compute Utilisation Record     | Compute Utilisation Record as classified within Performance indicators.                                    | D4         |
| AIDCF:Permit                       | Permit                         | Permit as classified within Environmental obligations.                                                     | D4         |
| AIDCF:ReportingRequirement         | Reporting Requirement          | Reporting Requirement as classified within Environmental obligations.                                      | D4         |
| AIDCF:EmissionLimit                | Emission Limit                 | Emission Limit as classified within Environmental obligations.                                             | D4         |
| AIDCF:WaterLimit                   | Water Limit                    | Water Limit as classified within Environmental obligations.                                                | D4         |
| AIDCF:WasteRequirement             | Waste Requirement              | Waste Requirement as classified within Environmental obligations.                                          | D4         |
| AIDCF:EnvironmentalCommitment      | Environmental Commitment       | Environmental Commitment as classified within Environmental obligations.                                   | D4         |
| AIDCF:OperatingModel               | Operating Model                | Operating Model as classified within Governance and authority.                                             | D5         |
| AIDCF:Role                         | Role                           | Role as classified within Governance and authority.                                                        | D5         |
| AIDCF:Delegation                   | Delegation                     | Delegation as classified within Governance and authority.                                                  | D5         |
| AIDCF:ApprovalAuthority            | Approval Authority             | Approval Authority as classified within Governance and authority.                                          | D5         |
| AIDCF:EscalationPath               | Escalation Path                | Escalation Path as classified within Governance and authority.                                             | D5         |
| AIDCF:RiskAcceptance               | Risk Acceptance                | Risk Acceptance as classified within Governance and authority.                                             | D5         |
| AIDCF:Procedure                    | Procedure                      | Procedure as classified within Work control.                                                               | D5         |
| AIDCF:MethodStatement              | Method Statement               | Method Statement as classified within Work control.                                                        | D5         |
| AIDCF:PermittoWork                 | Permit to Work                 | Permit to Work as classified within Work control.                                                          | D5         |
| AIDCF:LockoutTagout                | Lockout Tagout                 | Lockout Tagout as classified within Work control.                                                          | D5         |
| AIDCF:MaintenanceWindow            | Maintenance Window             | Maintenance Window as classified within Work control.                                                      | D5         |
| AIDCF:ChangeRecord                 | Change Record                  | Change Record as classified within Work control.                                                           | D5         |
| AIDCF:TemporaryConfiguration       | Temporary Configuration        | Temporary Configuration as classified within Work control.                                                 | D5         |
| AIDCF:MaintenancePlan              | Maintenance Plan               | Maintenance Plan as classified within Maintenance and reliability.                                         | D5         |
| AIDCF:WorkOrder                    | Work Order                     | Work Order as classified within Maintenance and reliability.                                               | D5         |
| AIDCF:ConditionMonitoring          | Condition Monitoring           | Condition Monitoring as classified within Maintenance and reliability.                                     | D5         |
| AIDCF:Inspection                   | Inspection                     | Inspection as classified within Maintenance and reliability.                                               | D5         |
| AIDCF:Calibration                  | Calibration                    | Calibration as classified within Maintenance and reliability.                                              | D5         |
| AIDCF:SparePart                    | Spare Part                     | Spare Part as classified within Maintenance and reliability.                                               | D5         |
| AIDCF:ObsolescenceRecord           | Obsolescence Record            | Obsolescence Record as classified within Maintenance and reliability.                                      | D5         |
| AIDCF:Shift                        | Shift                          | Shift as classified within Staffing and competence.                                                        | D5         |
| AIDCF:Roster                       | Roster                         | Roster as classified within Staffing and competence.                                                       | D5         |
| AIDCF:CompetencyRecord             | Competency Record              | Competency Record as classified within Staffing and competence.                                            | D5         |
| AIDCF:Authorisation                | Authorisation                  | Authorisation as classified within Staffing and competence.                                                | D5         |
| AIDCF:TrainingRecord               | Training Record                | Training Record as classified within Staffing and competence.                                              | D5         |
| AIDCF:Contractor                   | Contractor                     | Contractor as classified within Staffing and competence.                                                   | D5         |
| AIDCF:SubjectMatterExpert          | Subject Matter Expert          | Subject Matter Expert as classified within Staffing and competence.                                        | D5         |
| AIDCF:Alarm                        | Alarm                          | Alarm as classified within Incident and emergency.                                                         | D5         |
| AIDCF:Incident                     | Incident                       | Incident as classified within Incident and emergency.                                                      | D5         |
| AIDCF:EventLog                     | Event Log                      | Event Log as classified within Incident and emergency.                                                     | D5         |
| AIDCF:EmergencyProcedure           | Emergency Procedure            | Emergency Procedure as classified within Incident and emergency.                                           | D5         |
| AIDCF:CrisisTeam                   | Crisis Team                    | Crisis Team as classified within Incident and emergency.                                                   | D5         |
| AIDCF:Exercise                     | Exercise                       | Exercise as classified within Incident and emergency.                                                      | D5         |
| AIDCF:Post-IncidentReview          | Post-Incident Review           | Post-Incident Review as classified within Incident and emergency.                                          | D5         |
| AIDCF:Supplier                     | Supplier                       | Supplier as classified within Supplier and service management.                                             | D5         |
| AIDCF:MaintenanceContract          | Maintenance Contract           | Maintenance Contract as classified within Supplier and service management.                                 | D5         |
| AIDCF:ServiceLevel                 | Service Level                  | Service Level as classified within Supplier and service management.                                        | D5         |
| AIDCF:RemoteSupport                | Remote Support                 | Remote Support as classified within Supplier and service management.                                       | D5         |
| AIDCF:EscalationContact            | Escalation Contact             | Escalation Contact as classified within Supplier and service management.                                   | D5         |
| AIDCF:LeadTime                     | Lead Time                      | Lead Time as classified within Supplier and service management.                                            | D5         |
| AIDCF:SupplyConstraint             | Supply Constraint              | Supply Constraint as classified within Supplier and service management.                                    | D5         |
| AIDCF:ConfigurationBaseline        | Configuration Baseline         | Configuration Baseline as classified within Configuration and documentation.                               | D5         |
| AIDCF:AssetRegister                | Asset Register                 | Asset Register as classified within Configuration and documentation.                                       | D5         |
| AIDCF:DrawingRegister              | Drawing Register               | Drawing Register as classified within Configuration and documentation.                                     | D5         |
| AIDCF:ProcedureRegister            | Procedure Register             | Procedure Register as classified within Configuration and documentation.                                   | D5         |
| AIDCF:Revision                     | Revision                       | Revision as classified within Configuration and documentation.                                             | D5         |
| AIDCF:DocumentCustodian            | Document Custodian             | Document Custodian as classified within Configuration and documentation.                                   | D5         |
| AIDCF:Accelerator                  | Accelerator                    | Accelerator as classified within Accelerated compute.                                                      | D6         |
| AIDCF:GPU                          | GPU                            | GPU as classified within Accelerated compute.                                                              | D6         |
| AIDCF:AIASIC                       | AI ASIC                        | AI ASIC as classified within Accelerated compute.                                                          | D6         |
| AIDCF:ComputeNode                  | Compute Node                   | Compute Node as classified within Accelerated compute.                                                     | D6         |
| AIDCF:GPUBaseboard                 | GPU Baseboard                  | GPU Baseboard as classified within Accelerated compute.                                                    | D6         |
| AIDCF:CPU                          | CPU                            | CPU as classified within Accelerated compute.                                                              | D6         |
| AIDCF:Memory                       | Memory                         | Memory as classified within Accelerated compute.                                                           | D6         |
| AIDCF:DPU                          | DPU                            | DPU as classified within Accelerated compute.                                                              | D6         |
| AIDCF:NIC                          | NIC                            | NIC as classified within Accelerated compute.                                                              | D6         |
| AIDCF:ComputeTray                  | Compute Tray                   | Compute Tray as classified within Rack-scale systems.                                                      | D6         |
| AIDCF:Rack-ScaleSystem             | Rack-Scale System              | Rack-Scale System as classified within Rack-scale systems.                                                 | D6         |
| AIDCF:Scale-UpDomain               | Scale-Up Domain                | Scale-Up Domain as classified within Rack-scale systems.                                                   | D6         |
| AIDCF:NVLinkDomain                 | NVLink Domain                  | NVLink Domain as classified within Rack-scale systems.                                                     | D6         |
| AIDCF:Enclosure                    | Enclosure                      | Enclosure as classified within Rack-scale systems.                                                         | D6         |
| AIDCF:Backplane                    | Backplane                      | Backplane as classified within Rack-scale systems.                                                         | D6         |
| AIDCF:PowerShelf                   | Power Shelf                    | Power Shelf as classified within Rack-scale systems.                                                       | D6         |
| AIDCF:RackController               | Rack Controller                | Rack Controller as classified within Rack-scale systems.                                                   | D6         |
| AIDCF:ComputeCluster               | Compute Cluster                | Compute Cluster as classified within Cluster systems.                                                      | D6         |
| AIDCF:ClusterPartition             | Cluster Partition              | Cluster Partition as classified within Cluster systems.                                                    | D6         |
| AIDCF:NodePool                     | Node Pool                      | Node Pool as classified within Cluster systems.                                                            | D6         |
| AIDCF:HeadNode                     | Head Node                      | Head Node as classified within Cluster systems.                                                            | D6         |
| AIDCF:LoginNode                    | Login Node                     | Login Node as classified within Cluster systems.                                                           | D6         |
| AIDCF:ManagementNode               | Management Node                | Management Node as classified within Cluster systems.                                                      | D6         |
| AIDCF:ProvisioningNode             | Provisioning Node              | Provisioning Node as classified within Cluster systems.                                                    | D6         |
| AIDCF:BMC                          | BMC                            | BMC as classified within Management and firmware.                                                          | D6         |
| AIDCF:Firmware                     | Firmware                       | Firmware as classified within Management and firmware.                                                     | D6         |
| AIDCF:BIOS                         | BIOS                           | BIOS as classified within Management and firmware.                                                         | D6         |
| AIDCF:Driver                       | Driver                         | Driver as classified within Management and firmware.                                                       | D6         |
| AIDCF:FabricManager                | Fabric Manager                 | Fabric Manager as classified within Management and firmware.                                               | D6         |
| AIDCF:ClusterManager               | Cluster Manager                | Cluster Manager as classified within Management and firmware.                                              | D6         |
| AIDCF:ProvisioningService          | Provisioning Service           | Provisioning Service as classified within Management and firmware.                                         | D6         |
| AIDCF:Scheduler                    | Scheduler                      | Scheduler as classified within Management and firmware.                                                    | D6         |
| AIDCF:Orchestrator                 | Orchestrator                   | Orchestrator as classified within Management and firmware.                                                 | D6         |
| AIDCF:Queue                        | Queue                          | Queue as classified within Workload infrastructure.                                                        | D6         |
| AIDCF:Partition                    | Partition                      | Partition as classified within Workload infrastructure.                                                    | D6         |
| AIDCF:Reservation                  | Reservation                    | Reservation as classified within Workload infrastructure.                                                  | D6         |
| AIDCF:ContainerRuntime             | Container Runtime              | Container Runtime as classified within Workload infrastructure.                                            | D6         |
| AIDCF:KubernetesCluster            | Kubernetes Cluster             | Kubernetes Cluster as classified within Workload infrastructure.                                           | D6         |
| AIDCF:JobScheduler                 | Job Scheduler                  | Job Scheduler as classified within Workload infrastructure.                                                | D6         |
| AIDCF:CheckpointAgent              | Checkpoint Agent               | Checkpoint Agent as classified within Workload infrastructure.                                             | D6         |
| AIDCF:GPUTelemetry                 | GPU Telemetry                  | GPU Telemetry as classified within Compute observability.                                                  | D6         |
| AIDCF:NodeTelemetry                | Node Telemetry                 | Node Telemetry as classified within Compute observability.                                                 | D6         |
| AIDCF:HealthService                | Health Service                 | Health Service as classified within Compute observability.                                                 | D6         |
| AIDCF:EventLog                     | Event Log                      | Event Log as classified within Compute observability.                                                      | D6         |
| AIDCF:PerformanceCounter           | Performance Counter            | Performance Counter as classified within Compute observability.                                            | D6         |
| AIDCF:ErrorCounter                 | Error Counter                  | Error Counter as classified within Compute observability.                                                  | D6         |
| AIDCF:GoldenImage                  | Golden Image                   | Golden Image as classified within Compute lifecycle.                                                       | D6         |
| AIDCF:FirmwareBaseline             | Firmware Baseline              | Firmware Baseline as classified within Compute lifecycle.                                                  | D6         |
| AIDCF:CompatibilityMatrix          | Compatibility Matrix           | Compatibility Matrix as classified within Compute lifecycle.                                               | D6         |
| AIDCF:HardwareSupportContract      | Hardware Support Contract      | Hardware Support Contract as classified within Compute lifecycle.                                          | D6         |
| AIDCF:RMAProcess                   | RMA Process                    | RMA Process as classified within Compute lifecycle.                                                        | D6         |
| AIDCF:SecureDecommissioningRecord  | Secure Decommissioning Record  | Secure Decommissioning Record as classified within Compute lifecycle.                                      | D6         |
| AIDCF:ParallelFileSystem           | Parallel File System           | Parallel File System as classified within Storage systems.                                                 | D7         |
| AIDCF:Scale-OutNAS                 | Scale-Out NAS                  | Scale-Out NAS as classified within Storage systems.                                                        | D7         |
| AIDCF:ObjectStorage                | Object Storage                 | Object Storage as classified within Storage systems.                                                       | D7         |
| AIDCF:BlockStorage                 | Block Storage                  | Block Storage as classified within Storage systems.                                                        | D7         |
| AIDCF:LocalNVMe                    | Local NVMe                     | Local NVMe as classified within Storage systems.                                                           | D7         |
| AIDCF:BurstBuffer                  | Burst Buffer                   | Burst Buffer as classified within Storage systems.                                                         | D7         |
| AIDCF:ArchiveStorage               | Archive Storage                | Archive Storage as classified within Storage systems.                                                      | D7         |
| AIDCF:StorageNode                  | Storage Node                   | Storage Node as classified within Storage nodes and media.                                                 | D7         |
| AIDCF:MetadataServer               | Metadata Server                | Metadata Server as classified within Storage nodes and media.                                              | D7         |
| AIDCF:ObjectStorageNode            | Object Storage Node            | Object Storage Node as classified within Storage nodes and media.                                          | D7         |
| AIDCF:Controller                   | Controller                     | Controller as classified within Storage nodes and media.                                                   | D7         |
| AIDCF:SSD                          | SSD                            | SSD as classified within Storage nodes and media.                                                          | D7         |
| AIDCF:HDD                          | HDD                            | HDD as classified within Storage nodes and media.                                                          | D7         |
| AIDCF:Tape                         | Tape                           | Tape as classified within Storage nodes and media.                                                         | D7         |
| AIDCF:NVRAM                        | NVRAM                          | NVRAM as classified within Storage nodes and media.                                                        | D7         |
| AIDCF:Namespace                    | Namespace                      | Namespace as classified within Data-path services.                                                         | D7         |
| AIDCF:MetadataService              | Metadata Service               | Metadata Service as classified within Data-path services.                                                  | D7         |
| AIDCF:DataMover                    | Data Mover                     | Data Mover as classified within Data-path services.                                                        | D7         |
| AIDCF:Cache                        | Cache                          | Cache as classified within Data-path services.                                                             | D7         |
| AIDCF:Gateway                      | Gateway                        | Gateway as classified within Data-path services.                                                           | D7         |
| AIDCF:ClientDriver                 | Client Driver                  | Client Driver as classified within Data-path services.                                                     | D7         |
| AIDCF:MountService                 | Mount Service                  | Mount Service as classified within Data-path services.                                                     | D7         |
| AIDCF:DatasetRepository            | Dataset Repository             | Dataset Repository as classified within AI artifact services.                                              | D7         |
| AIDCF:ModelRepository              | Model Repository               | Model Repository as classified within AI artifact services.                                                | D7         |
| AIDCF:CheckpointRepository         | Checkpoint Repository          | Checkpoint Repository as classified within AI artifact services.                                           | D7         |
| AIDCF:FeatureStore                 | Feature Store                  | Feature Store as classified within AI artifact services.                                                   | D7         |
| AIDCF:ArtifactRegistry             | Artifact Registry              | Artifact Registry as classified within AI artifact services.                                               | D7         |
| AIDCF:Snapshot                     | Snapshot                       | Snapshot as classified within Protection and recovery.                                                     | D7         |
| AIDCF:Replica                      | Replica                        | Replica as classified within Protection and recovery.                                                      | D7         |
| AIDCF:BackupCopy                   | Backup Copy                    | Backup Copy as classified within Protection and recovery.                                                  | D7         |
| AIDCF:ErasureCodingGroup           | Erasure Coding Group           | Erasure Coding Group as classified within Protection and recovery.                                         | D7         |
| AIDCF:RecoveryCopy                 | Recovery Copy                  | Recovery Copy as classified within Protection and recovery.                                                | D7         |
| AIDCF:ImmutableCopy                | Immutable Copy                 | Immutable Copy as classified within Protection and recovery.                                               | D7         |
| AIDCF:StorageManager               | Storage Manager                | Storage Manager as classified within Storage management.                                                   | D7         |
| AIDCF:CapacityManager              | Capacity Manager               | Capacity Manager as classified within Storage management.                                                  | D7         |
| AIDCF:TieringPolicy                | Tiering Policy                 | Tiering Policy as classified within Storage management.                                                    | D7         |
| AIDCF:RetentionPolicy              | Retention Policy               | Retention Policy as classified within Storage management.                                                  | D7         |
| AIDCF:IntegrityScanner             | Integrity Scanner              | Integrity Scanner as classified within Storage management.                                                 | D7         |
| AIDCF:TelemetryService             | Telemetry Service              | Telemetry Service as classified within Storage management.                                                 | D7         |
| AIDCF:IngestionInterface           | Ingestion Interface            | Ingestion Interface as classified within Data logistics interfaces.                                        | D7         |
| AIDCF:ExportInterface              | Export Interface               | Export Interface as classified within Data logistics interfaces.                                           | D7         |
| AIDCF:DataTransferNode             | Data Transfer Node             | Data Transfer Node as classified within Data logistics interfaces.                                         | D7         |
| AIDCF:WANTransferService           | WAN Transfer Service           | WAN Transfer Service as classified within Data logistics interfaces.                                       | D7         |
| AIDCF:StagingArea                  | Staging Area                   | Staging Area as classified within Data logistics interfaces.                                               | D7         |
| AIDCF:Scale-UpFabric               | Scale-Up Fabric                | Scale-Up Fabric as classified within Scale-up interconnect.                                                | D8         |
| AIDCF:SwitchFabric                 | Switch Fabric                  | Switch Fabric as classified within Scale-up interconnect.                                                  | D8         |
| AIDCF:InterconnectLink             | Interconnect Link              | Interconnect Link as classified within Scale-up interconnect.                                              | D8         |
| AIDCF:TopologyDomain               | Topology Domain                | Topology Domain as classified within Scale-up interconnect.                                                | D8         |
| AIDCF:InfiniBandFabric             | InfiniBand Fabric              | InfiniBand Fabric as classified within Scale-out compute fabric.                                           | D8         |
| AIDCF:EthernetAIFabric             | Ethernet AI Fabric             | Ethernet AI Fabric as classified within Scale-out compute fabric.                                          | D8         |
| AIDCF:RoCEFabric                   | RoCE Fabric                    | RoCE Fabric as classified within Scale-out compute fabric.                                                 | D8         |
| AIDCF:ComputeLeaf                  | Compute Leaf                   | Compute Leaf as classified within Scale-out compute fabric.                                                | D8         |
| AIDCF:ComputeSpine                 | Compute Spine                  | Compute Spine as classified within Scale-out compute fabric.                                               | D8         |
| AIDCF:FabricManager                | Fabric Manager                 | Fabric Manager as classified within Scale-out compute fabric.                                              | D8         |
| AIDCF:StorageNetwork               | Storage Network                | Storage Network as classified within Storage fabric.                                                       | D8         |
| AIDCF:StorageLeaf                  | Storage Leaf                   | Storage Leaf as classified within Storage fabric.                                                          | D8         |
| AIDCF:StorageSpine                 | Storage Spine                  | Storage Spine as classified within Storage fabric.                                                         | D8         |
| AIDCF:SANFabric                    | SAN Fabric                     | SAN Fabric as classified within Storage fabric.                                                            | D8         |
| AIDCF:StorageGateway               | Storage Gateway                | Storage Gateway as classified within Storage fabric.                                                       | D8         |
| AIDCF:FrontendNetwork              | Frontend Network               | Frontend Network as classified within Frontend and service network.                                        | D8         |
| AIDCF:LoadBalancer                 | Load Balancer                  | Load Balancer as classified within Frontend and service network.                                           | D8         |
| AIDCF:ServiceGateway               | Service Gateway                | Service Gateway as classified within Frontend and service network.                                         | D8         |
| AIDCF:EdgeRouter                   | Edge Router                    | Edge Router as classified within Frontend and service network.                                             | D8         |
| AIDCF:Firewall                     | Firewall                       | Firewall as classified within Frontend and service network.                                                | D8         |
| AIDCF:APINetwork                   | API Network                    | API Network as classified within Frontend and service network.                                             | D8         |
| AIDCF:ManagementNetwork            | Management Network             | Management Network as classified within Management and control network.                                    | D8         |
| AIDCF:Out-of-BandNetwork           | Out-of-Band Network            | Out-of-Band Network as classified within Management and control network.                                   | D8         |
| AIDCF:ConsoleServer                | Console Server                 | Console Server as classified within Management and control network.                                        | D8         |
| AIDCF:ManagementSwitch             | Management Switch              | Management Switch as classified within Management and control network.                                     | D8         |
| AIDCF:JumpService                  | Jump Service                   | Jump Service as classified within Management and control network.                                          | D8         |
| AIDCF:TimeService                  | Time Service                   | Time Service as classified within Timing and core services.                                                | D8         |
| AIDCF:DNSService                   | DNS Service                    | DNS Service as classified within Timing and core services.                                                 | D8         |
| AIDCF:DHCPService                  | DHCP Service                   | DHCP Service as classified within Timing and core services.                                                | D8         |
| AIDCF:IPAMService                  | IPAM Service                   | IPAM Service as classified within Timing and core services.                                                | D8         |
| AIDCF:CertificateService           | Certificate Service            | Certificate Service as classified within Timing and core services.                                         | D8         |
| AIDCF:AuthenticationService        | Authentication Service         | Authentication Service as classified within Timing and core services.                                      | D8         |
| AIDCF:Cable                        | Cable                          | Cable as classified within Physical connectivity.                                                          | D8         |
| AIDCF:OpticalFibre                 | Optical Fibre                  | Optical Fibre as classified within Physical connectivity.                                                  | D8         |
| AIDCF:CopperLink                   | Copper Link                    | Copper Link as classified within Physical connectivity.                                                    | D8         |
| AIDCF:Transceiver                  | Transceiver                    | Transceiver as classified within Physical connectivity.                                                    | D8         |
| AIDCF:PatchPanel                   | Patch Panel                    | Patch Panel as classified within Physical connectivity.                                                    | D8         |
| AIDCF:Meet-MeRoom                  | Meet-Me Room                   | Meet-Me Room as classified within Physical connectivity.                                                   | D8         |
| AIDCF:Cross-Connect                | Cross-Connect                  | Cross-Connect as classified within Physical connectivity.                                                  | D8         |
| AIDCF:FlowTelemetry                | Flow Telemetry                 | Flow Telemetry as classified within Network observability.                                                 | D8         |
| AIDCF:FabricTelemetry              | Fabric Telemetry               | Fabric Telemetry as classified within Network observability.                                               | D8         |
| AIDCF:PacketCaptureService         | Packet Capture Service         | Packet Capture Service as classified within Network observability.                                         | D8         |
| AIDCF:NetworkController            | Network Controller             | Network Controller as classified within Network observability.                                             | D8         |
| AIDCF:CongestionMonitor            | Congestion Monitor             | Congestion Monitor as classified within Network observability.                                             | D8         |
| AIDCF:PathMonitor                  | Path Monitor                   | Path Monitor as classified within Network observability.                                                   | D8         |

# Appendix B - Canonical relationship registry

| **Predicate**           | **Subject**         | **Object**                 | **Logic**                 | **Inverse**               | **Meaning**                             |
|-------------------------|---------------------|----------------------------|---------------------------|---------------------------|-----------------------------------------|
| PART_OF                 | Entity              | Entity                     | Transitive                | HAS_PART                  | Composition.                            |
| CONTAINS                | Location/System     | Entity                     | Transitive                | LOCATED_IN/PART_OF        | Containment.                            |
| LOCATED_IN              | Physical Entity     | Location                   | Transitive                | CONTAINS                  | Physical placement.                     |
| MEMBER_OF               | Entity              | Group                      | No                        | HAS_MEMBER                | Group membership.                       |
| IMPLEMENTS              | Asset/System        | Function                   | No                        | IMPLEMENTED_BY            | Realises a required function.           |
| SUPPORTS                | Entity              | Capability/Outcome         | No                        | SUPPORTED_BY              | Contributes to outcome.                 |
| INTERFACES_WITH         | Entity              | Entity                     | Symmetric                 | INTERFACES_WITH           | Defined exchange boundary.              |
| CONNECTED_TO            | Entity              | Entity                     | Symmetric unless directed | CONNECTED_TO              | Realised connection.                    |
| ROUTES_THROUGH          | Flow/Service        | Entity                     | No                        | CARRIES                   | Path relationship.                      |
| DEPENDS_ON              | Consumer entity     | Provider/entity/condition  | Directional               | Declared where applicable | General reliance.                       |
| POWERED_BY              | Load/system         | Electrical source/path     | Directional               | Declared where applicable | Electrical reliance.                    |
| COOLED_BY               | Heat source/system  | Cooling system/path        | Directional               | Declared where applicable | Thermal reliance.                       |
| SUPPLIED_BY             | Consumer            | Provider/resource          | Directional               | Declared where applicable | Resource or service supply.             |
| CONTROLLED_BY           | Asset/system        | Controller/actor           | Directional               | Declared where applicable | Operational or automated control.       |
| MONITORED_BY            | Entity              | Monitoring entity          | Directional               | Declared where applicable | Visibility and detection reliance.      |
| PROTECTED_BY            | Entity              | Safeguard                  | Directional               | Declared where applicable | Protective relationship.                |
| AUTHENTICATED_BY        | Entity/service      | Identity service           | Directional               | Declared where applicable | Identity reliance.                      |
| TIMED_BY                | Entity/service      | Time source                | Directional               | Declared where applicable | Timing reliance.                        |
| CONFIGURED_BY           | Entity              | Configuration source/actor | Directional               | Declared where applicable | Configuration reliance.                 |
| RECOVERED_BY            | Entity/capability   | Recovery asset/process     | Directional               | Declared where applicable | Restoration reliance.                   |
| MAINTAINED_BY           | Entity              | Actor/organisation         | Directional               | Declared where applicable | Maintenance reliance.                   |
| OPERATED_BY             | Entity/system       | Actor/organisation         | Directional               | Declared where applicable | Operational responsibility.             |
| EVIDENCED_BY            | Assertion/entity    | Evidence object            | Directional               | Declared where applicable | Evidence support.                       |
| TESTED_BY               | Assertion/safeguard | Test record                | Directional               | Declared where applicable | Validation link.                        |
| SHARES_DEPENDENCY_WITH  | Entity              | Entity                     | Predicate-specific        | May be symmetric          | Common provider exposure.               |
| IN_SAME_FAULT_DOMAIN_AS | Entity              | Entity                     | Predicate-specific        | May be symmetric          | Shared failure exposure.                |
| DIVERSE_FROM            | Entity              | Entity                     | Predicate-specific        | May be symmetric          | Declared material difference.           |
| INDEPENDENT_OF          | Entity              | Entity                     | Predicate-specific        | May be symmetric          | Evidence-bounded relevant independence. |
| REDUNDANT_WITH          | Entity              | Entity                     | Predicate-specific        | May be symmetric          | Alternative for a protected function.   |
| CONCENTRATES            | Entity              | Entity                     | Predicate-specific        | May be symmetric          | Aggregates capability or consequence.   |
| SINGLE_POINT_FOR        | Entity              | Entity                     | Predicate-specific        | May be symmetric          | Unmitigated single-point relationship.  |
| ISOLATED_FROM           | Entity              | Entity                     | Predicate-specific        | May be symmetric          | Declared separation.                    |

# Appendix C - Minimum property schemas

## C.1 Capability Instance

| **Property**         | **Cardinality** | **Type**               |
|----------------------|-----------------|------------------------|
| capabilityInstanceId | 1               | Identifier             |
| name                 | 1               | String                 |
| capabilityType       | 1               | Controlled term        |
| owner                | 1               | Party                  |
| lifecycleStage       | 1               | Enumeration            |
| serviceOutcomes      | 1..\* / 0..\*   | ServiceOutcome         |
| criticality          | 1..\* / 0..\*   | Criticality            |
| assessmentBoundary   | 1               | Boundary               |
| operatingEnvelope    | 1               | Envelope               |
| architectureBaseline | 1..\* / 0..\*   | Document/Configuration |
| effectivePeriod      | 1..\* / 0..\*   | Temporal interval      |
| confidenceState      | 1               | Confidence             |

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
| confidence          | 1               | ConfidenceState   |
| validity            | 1               | Temporal interval |

## C.3 Evidence Object

| **Property**         | **Cardinality** | **Type**          |
|----------------------|-----------------|-------------------|
| evidenceId           | 1               | Identifier        |
| title                | 1               | String            |
| evidenceType         | 1               | Controlled term   |
| source               | 1               | Source            |
| custodian            | 1               | Party             |
| collectionMethod     | 1               | Controlled term   |
| observationTime      | 1               | Date/time         |
| effectivePeriod      | 0..1            | Temporal interval |
| scope                | 1               | Entity set        |
| integrityStatus      | 0..1            | Controlled term   |
| supportsOrChallenges | 1..\*           | Assertion         |
| limitations          | 0..\*           | String            |
| reviewer             | 0..1            | Party             |
| confidence           | 1               | Confidence state  |

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
| AIDCF Manifesto v1.0                                       | Internal canonical source | Purpose, doctrine, eight domains, evidence and UNKNOWN principles.                                                                                               |
| AIDCF Core Conceptual Model v1.0                           | Internal canonical source | Capability, assets, dependencies, capacity, failure, safeguard and assurance concepts.                                                                           |
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
| Methodology author                  | Draft completed | Internal coherence and alignment with Artifacts 1 and 2.        |
| Ontology/knowledge-model reviewer   | Pending         | Class, relationship, constraint and machine-readable integrity. |
| Data-centre architecture reviewer   | Pending         | Facility and system taxonomy usability.                         |
| Electrical engineering reviewer     | Pending         | Power semantics and dependency accuracy.                        |
| Mechanical/cooling reviewer         | Pending         | Thermal, hydraulic and liquid-cooling semantics.                |
| Fire/life-safety reviewer           | Pending         | Boundary and safety terminology.                                |
| Physical-security reviewer          | Pending         | Physical control and zoning taxonomy.                           |
| AI compute/HPC reviewer             | Pending         | Compute, rack-scale and cluster taxonomy.                       |
| Storage reviewer                    | Pending         | Data infrastructure and recovery semantics.                     |
| Network/interconnect reviewer       | Pending         | Scale-up, scale-out and management fabrics.                     |
| OT/security reviewer                | Pending         | BMS, EPMS, SCADA and control relationships.                     |
| Assurance/evidence reviewer         | Pending         | UNKNOWN, confidence, provenance and claims.                     |
| AI Trust Graph integration reviewer | Pending         | Handoff and shared-node semantics.                              |
| Legal/IP/trademark review           | Pending         | Publication claims, licensing and ownership.                    |
| Public release                      | Not approved    | All mandatory review gates closed.                              |

## F.1 Acceptance criteria

- Canonical terms remain consistent with the Manifesto and Core Conceptual Model.

- All eight domains are represented without becoming isolated silos.

- Capability, outcome, function, system, asset and dependency distinctions are operationally usable.

- Capacity and redundancy claims are condition- and evidence-bounded.

- Time, state, responsibility and UNKNOWN are first-class semantics.

- Artifact 4 can attach threats, hazards, failures and propagation paths without restructuring the ontology.

- Machine-readable schemas can be generated from the normative registries.

- No content creates an unsupported certification or engineering claim.

- Independent multidisciplinary review and change control are recorded.

## Change record

| **Version** | **Status**              | **Summary**                                                                       |
|-------------|-------------------------|-----------------------------------------------------------------------------------|
| 0.1         | Architecture draft      | Established upper ontology and eight-domain taxonomy.                             |
| 0.5         | Integrated draft        | Added relationships, state, capacity, responsibility, validation and profiles.    |
| 1.0         | Controlled-review draft | Publication-grade baseline for expert review and machine-readable implementation. |

##  Final doctrine

AIDCF infrastructure is represented only when its meaning can be connected to a Capability Instance, Service Outcome, required function, dependency, state or assurance purpose. Classification alone is insufficient. The ontology must reveal how the system is assembled, what it relies upon, under which conditions claims apply, who is responsible, what evidence supports the representation and what remains UNKNOWN.
