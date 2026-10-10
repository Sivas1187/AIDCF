> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-013_AI_Data_Centre_Assurance_Reference_Architecture_v1.1.pdf](AIDCF-013_AI_Data_Centre_Assurance_Reference_Architecture_v1.1.pdf).

**AIDCF**

**AI Data Centre Facilities Assurance Framework**

**AI DATA CENTRE ASSURANCE REFERENCE ARCHITECTURE**

**A capability-centred, system-of-systems architecture connecting AI service outcomes to facilities, engineered infrastructure, compute platforms, operations, evidence, failure paths, critical gates and accountable decisions**

**Model the capability. Expose the dependency. Trace the failure. Verify the safeguard. Preserve uncertainty. Bound the decision.**

# Document control

| **Field**           | **Value**                                                                                                                                 |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Public ID           | AIDCF-013                                                                                                                                 |
| Short code          | ARA (requirement IDs ARA-REQ-NNN)                                                                                                         |
| Title               | AI Data Centre Assurance Reference Architecture                                                                                           |
| Version             | 1.1                                                                                                                                       |
| Date                | 2026-10-10                                                                                                                                |
| Status              | Draft for controlled review                                                                                                               |
| Author              | Siva Sethumadhavan                                                                                                                        |
| Depends on          | AIDCF-002, AIDCF-003, AIDCF-004, AIDCF-005, AIDCF-006, AIDCF-007A, AIDCF-008, AIDCF-009, AIDCF-010, AIDCF-011, AIDCF-012                 |
| Data contract       | AIDCF-014 (classes, relationships, traceability) and AIDCF-016 (serialisation)                                                           |
| Purpose             | Define the layers, rails, viewpoints, system cards, interface contracts, patterns, evidence points, failure paths and graph mappings used to scope and assess an AI Capability Instance. |
| Boundary            | Not a vendor design, engineering code, operating procedure, certification or testing authority. Engineering values are capability-profile parameters; defaults shown are illustrative. |
| Safety              | Nothing in this document authorises switching, isolation, fault injection, intrusion or any other disruptive action. Such actions require the site's own authorisation, competent persons and safe systems of work (AIDCF-009). |

## Revision history

| **Version** | **Date**   | **Summary**                                                                                                                                                                                                                                                                                                          |
|-------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | Not stated | Initial draft (internal ID AIDCF-ARA-001): layers, viewpoints, domain profiles, system cards, interface contracts, patterns, models, templates, workflows and validation list.                                                                                                                                      |
| 1.1         | 2026-10-10 | Public ID AIDCF-013 adopted; control links moved to AIDCF-007A families and control ranges; relationship names aligned to AIDCF-014 canonical vocabulary with alias note; placeholder "Required" cells replaced with specific content; AI-specific architecture (high-density racks, TCS/FWS liquid cooling, training load dynamics, scale-up/scale-out fabrics, checkpoint storage, BMC/out-of-band, control planes) and assurance/resilience rails added; numbered requirements ARA-REQ-001 onward. |

# Executive thesis

**An AI data centre is represented as a capability-supporting system of systems. A conformant architecture traces Service Outcomes through Required Functions, systems, assets, interfaces, resources, dependencies, operating states, failure paths and safeguards to controls, evidence, critical gates and bounded decisions.**

AI infrastructure differs from conventional enterprise data-centre infrastructure in ways that change what an assessor must model:

- **Density and coupling.** Accelerator racks are designed for power densities several times those of air-cooled enterprise racks and depend on direct liquid cooling. The thermal time constant between loss of coolant flow and accelerator protective throttling or shutdown is short, so the power supply to pumps and controls becomes part of the thermal continuity path.
- **Synchronous workloads.** Large training jobs run thousands of accelerators in lockstep. The job is a single fault domain: one failed node, link or storage stall can stop all participants, and the job's aggregate power draw changes rapidly and in a correlated way at iteration, checkpoint and job boundaries.
- **Fabric-defined capability.** Usable capability depends on scale-up domains (high-bandwidth accelerator interconnect within a node or rack) and scale-out fabrics (RDMA back-end networks), not only on accelerator count.
- **State in storage.** Training progress is preserved only in checkpoints; recovery objectives are expressed as lost training time and restart time, and depend on checkpoint durability, integrity and restore bandwidth.
- **Converged control planes.** Facility controls (BMS, EPMS, CDU, PLC) and IT control planes (cluster manager, scheduler, fabric manager, BMC and out-of-band management) can each command power, cooling or compute state. Their identity, reach and failure behaviour are assurance subjects in their own right (CG-07, CG-15).

## Canonical assurance chain

The architecture is organised around the canonical 16-step assurance chain (AIDCF-014). This document defines how steps 2 to 9 are modelled and how steps 10 to 16 attach to them.

| **Step** | **Chain element**                          | **Where modelled in AIDCF-013**                                          |
|----------|--------------------------------------------|--------------------------------------------------------------------------|
| 1        | Decision Question                          | Layer L0; Capability record (Part VI)                                    |
| 2        | Capability Instance                        | Layer L1; Capability record                                              |
| 3        | Service Outcome                            | Layer L1; Service Outcome specification                                  |
| 4        | Required Function                          | Layer L2; reference service chains                                       |
| 5        | Architecture (InfrastructureSystem, AssetInstance, Interface) | Layers L3 to L6; domain profiles; system cards; interface contracts |
| 6        | Dependency and Fault Domain                | Resilience rail; dependency and fault-domain models                      |
| 7        | Threat / Hazard / Failure Scenario         | Failure-path model; AIDCF-004                                            |
| 8        | Safeguard                                  | Safeguard model; system cards                                            |
| 9        | Control                                    | Control attachment; AIDCF-007A families per domain                       |
| 10–12    | Evidence Requirement, Evidence Object, Control Assessment | Assurance rail; evidence attachment; AIDCF-008, AIDCF-009     |
| 13       | Finding / UNKNOWN Record                   | Assurance rail; AIDCF-009, AIDCF-008                                     |
| 14       | Gate Result                                | Critical-gate architecture; AIDCF-010                                    |
| 15–16    | Score Snapshot, Decision Recommendation, Assurance Decision | Layer L9; AIDCF-010                                         |
| Loop     | Report and Reassessment Trigger            | Layer L9; continuing-assurance workflow; AIDCF-011, AIDCF-012            |

# Part I - Authority and scope

**ARA-REQ-001** AIDCF-013 organises the canonical objects of AIDCF-003 and AIDCF-014 into layers, rails, views, system cards, interface contracts and patterns. It shall not define new object classes or relationship types; where an architecture concept has no canonical class, it shall be recorded as an attribute or a registered extension (AIDCF-014 §33).

| **Topic**              | **Authority**                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Semantic authority     | AIDCF-003 owns infrastructure entities and operating states; AIDCF-014 owns the 48 classes and 41 relationship types. |
| Failure authority      | AIDCF-004 owns threat, hazard, failure-mode, scenario and safeguard semantics.                                         |
| Integration authority  | AIDCF-005 governs AIDCF–AI Trust Graph handoffs.                                                                      |
| Assurance authority    | AIDCF-007A (controls), AIDCF-008 (evidence), AIDCF-009 (assessment), AIDCF-010 (gates, scores, decisions), AIDCF-011 (programme), AIDCF-012 (reporting). |
| Data authority         | AIDCF-014 (information contract) and AIDCF-016 (serialisation).                                                       |

**ARA-REQ-002** Architecture records shall describe required functions and properties before products. Vendor or product identity shall be recorded as an attribute of an AssetInstance, never as the definition of a function.

**ARA-REQ-003** There is no universal blueprint. A conformant architecture shall be tailored to the capability, site, technology, operating states, consequence and decision question, and shall record each tailoring choice with its rationale.

**ARA-REQ-004** A profile or extension of this architecture may add views, records or parameters; it shall not remove a mandatory view, record or traceability link without an approved NOT_APPLICABLE rationale.

# Part II - Architecture principles

| **Requirement**  | **Principle**            | **Statement**                                                                                                                                                                |
|------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ARA-REQ-005**     | Capability first         | Modelling shall start from the Capability Instance and its Service Outcomes; an inventory not linked to an outcome is not an assurance architecture.                          |
| **ARA-REQ-006**    | Function before product  | Each RequiredFunction shall be stated in measurable, vendor-neutral terms before the systems that implement it are listed.                                                  |
| **ARA-REQ-007**     | System of systems        | Facility, IT, control-plane, operational and external-provider systems shall be represented in one connected model, not in separate unlinked diagrams.                        |
| **ARA-REQ-008**     | Dependency explicitness  | Direct, indirect, shared, external and recovery-only reliance shall be recorded as DEPENDS_ON edges with Dependency records, or as UNKNOWN.                                   |
| **ARA-REQ-009**   | State awareness          | Every capacity, redundancy and safeguard claim shall state the operating states it covers (NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION, SHUTDOWN, FAILED, UNKNOWN). |
| **ARA-REQ-010**    | Failure informed         | Credible failure paths, including propagation across domains and through shared control planes, shall be represented as FailureScenarios.                                   |
| **ARA-REQ-011**      | Fault-domain clarity     | A redundancy claim shall be accompanied by independence evidence or by the common modes that limit it.                                                                       |
| **ARA-REQ-012**    | Evidence attachment      | Every material assertion shall carry evidence or an UnknownRecord.                                                                                                           |
| **ARA-REQ-013**    | Gate readiness           | For each applicable critical gate, the architecture shall identify where its evidence will come from.                                                                        |
| **ARA-REQ-014**   | Human approval           | Automated discovery and inference may propose records; an accountable person approves them (AIDCF-014).                                                                     |

# Part III - Conformance levels

Architecture conformance levels describe the completeness of the architecture model. They are distinct from assurance levels (AL0–AL6, AIDCF-011) and data conformance levels (T0–T7, AIDCF-014); an architecture at AR5 does not imply any assurance level.

| **Level** | **Name**                         | **Criteria (cumulative)**                                                                                                                                                         |
|-----------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AR0       | Vocabulary aligned               | Uses the 15 domains, canonical classes, relationship types and operating-state codes.                                                                                             |
| AR1       | Capability and outcomes mapped   | Capability record and Service Outcome specifications complete and approved; Required Functions identified.                                                                        |
| AR2       | Infrastructure mapped            | Systems, assets, interfaces and resources implementing each Required Function recorded and reconciled to as-built sources; ArchitectureSnapshot published.                        |
| AR3       | Dependencies and fault domains   | Dependency graph and fault-domain map complete for all Required Functions, including external providers and control planes; residual gaps recorded as UNKNOWN.                     |
| AR4       | Assurance attached               | Failure scenarios, safeguards, AIDCF-007A controls, evidence requirements and critical-gate evidence paths attached for all in-scope outcomes.                                      |
| AR5       | Graph conformant and versioned   | Architecture graph validates at AIDCF-014 T4; snapshots immutable and superseded with lineage.                                                                                    |
| AR6       | Continuing assurance             | Telemetry and change sources registered as evidence sources; reassessment triggers defined and tested end to end.                                                                 |

**ARA-REQ-015** A claim of conformance to this architecture shall state the AR level, the ArchitectureSnapshot identifier and the ReleaseManifest against which it was validated.

# Part IV - Architecture layers and rails

## Layers

The model has ten connected layers. Each record belongs to one layer; relationships may cross layers.

| **Layer** | **Name**                         | **Content**                                                                                                                                         | **Principal classes**                                                           |
|-----------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| L0        | Decision and governance          | Decision question, accountable owners, authority, risk appetite, assurance programme.                                                               | AssuranceProgram, Assessment (decisionQuestion)                                 |
| L1        | Capability and outcomes          | Capability Instance, workload model, Service Outcomes, tolerances, criticality, operating envelope.                                                 | CapabilityInstance, ServiceOutcome                                              |
| L2        | Functional service chain         | Required Functions in service-chain order (for example ingest, train, checkpoint, serve) and their performance requirements.                       | RequiredFunction                                                                |
| L3        | Logical platform                 | Cluster manager, scheduler, orchestration, model serving, storage services, fabric management, identity, time, DNS, provisioning.                  | InfrastructureSystem, Interface                                                 |
| L4        | Physical IT                      | Accelerator nodes, racks, scale-up domains, switches, optics and cabling, storage servers and media, BMCs, out-of-band network.                    | AssetInstance, InfrastructureSystem, Interface                                  |
| L5        | Facility engineering             | Utility interface, MV/LV distribution, UPS and BESS, generation and fuel, cooling (FWS, CDU, TCS, air), heat rejection, BMS, EPMS, fire and life safety, physical security. | InfrastructureSystem, AssetInstance, Resource, CapacityAssertion |
| L6        | External ecosystem               | Utilities, water, fuel, telecoms, cloud and SaaS dependencies, OEMs, maintainers, logistics, regulators.                                            | Dependency, AssetInstance (provider service), PartyEntity                       |
| L7        | Operations and resilience        | Operating model, procedures, permits, maintenance, incident and change, continuity and recovery arrangements.                                      | Safeguard, OperatingState, FailureScenario                                      |
| L8        | Assurance objects                | Controls, evidence requirements, evidence, control assessments, findings, UNKNOWN records, gate results.                                           | Control, EvidenceRequirement, EvidenceObject, ControlAssessment, Finding, UnknownRecord, GateResult |
| L9        | Decision, reporting, reassessment | Score snapshots, recommendations, decisions, statements, reports, actions, triggers and events.                                                  | ScoreSnapshot, DecisionRecommendation, AssuranceDecision, AssuranceReport, ReassessmentTrigger, Event |

## Rails

Rails are cross-cutting concerns that every layer from L2 to L7 shall carry. They are not separate layers: each rail is a set of attributes and relationships that must be present on records in every layer.

| **Rail**                  | **What every layer must carry**                                                                                                                                                                   | **Gates principally served**   |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| R1 Assurance rail         | For each material assertion: the AIDCF-007A control(s) that govern it, the evidence requirement (claim type, classes, floors), the evidence point (where and how evidence is obtained) and the UNKNOWN rule. | CG-11, CG-12, all others  |
| R2 Resilience rail        | Fault-domain membership, redundancy group and independence evidence, degraded-mode behaviour, minimum service outcome, recovery path (RECOVERS_THROUGH), recovery dependencies and recovery sequence. | CG-03, CG-09, CG-10            |
| R3 Digital authority rail | Which identities, control systems and automations can change the element's state (CONTROLLED_BY), through which management interfaces, with what privilege, approval and break-glass path. | CG-07, CG-15                   |
| R4 Observability rail     | Which telemetry observes the element (MONITORED_BY), at what resolution and latency, with what clock source, and which blind spots exist.                                                         | CG-11, CG-05, CG-06, CG-08     |
| R5 Change rail            | Configuration baseline, change authority, temporary-configuration states and the reassessment triggers that a change to the element fires.                                                       | CG-14, CG-02                   |

**ARA-REQ-016** Every InfrastructureSystem that implements a RequiredFunction of a CRITICAL Service Outcome shall carry content for all five rails, or an UnknownRecord for each rail it cannot populate.

**ARA-REQ-017** The resilience rail shall record, for each such system, the minimum service outcome it must sustain in DEGRADED and MAINTENANCE states and the recovery sequence position it occupies after a site-level event (for example, cooling controls and CDU pumps before accelerator power-on).

**ARA-REQ-018** The digital authority rail shall record every path by which a remote or automated actor can command power, cooling, fire-system interfaces, accelerator power state or firmware, including vendor remote-support paths and AI-enabled or scripted automation (AIDCF-007A SEC-06, SUP-06).

# Part V - Required viewpoints

Each viewpoint is a projection of one controlled model (the ArchitectureSnapshot), not an independent drawing.

**ARA-REQ-019** An assessment architecture shall provide each viewpoint below whose trigger applies. Omission of a triggered viewpoint requires an approved NOT_APPLICABLE rationale.

| **Viewpoint**    | **Concern answered**                                                                                   | **Minimum content**                                                                                                         | **Triggered when**                                               | **Gates informed**      |
|------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-------------------------|
| Capability       | What is assured, for whom, against what outcomes?                                                      | Capability Instance, users, workload classes, Service Outcomes and tolerances, decision question, boundary.                 | Always.                                                          | CG-01, CG-02            |
| Functional       | Which functions must be delivered for each outcome?                                                    | Service chains, Required Functions with measurable performance, function-to-outcome links.                                 | Always.                                                          | CG-01, CG-08            |
| System           | Which systems implement each function?                                                                 | System decomposition with IMPLEMENTED_BY and COMPOSED_OF; system cards.                                                    | Always.                                                          | CG-02                   |
| Physical         | Where are things, and what is co-located?                                                              | Site, building, hall, row and rack placement; fire, water and security zones; routes of feeders, pipes and fibre.           | Physical infrastructure in scope.                                | CG-02, CG-04, CG-09     |
| Dependency       | What does each function rely on, including external providers and control planes?                    | Dependency graph with type, strength, states, substitutability; external providers.                                         | Always.                                                          | CG-03                   |
| Fault-domain     | What fails together?                                                                                   | Fault domains, redundancy groups, independence evidence, common modes, blast radius.                                        | Any redundancy or containment claim.                             | CG-03, CG-09            |
| State            | How does the architecture behave outside NORMAL?                                                       | Operating-state matrix per system; transition triggers, authorities and exit criteria; maintenance configurations.         | Always.                                                          | CG-05, CG-06, CG-09     |
| Capacity         | Is there enough, with headroom, in each state?                                                         | Capacity assertions for power, cooling, fabric, storage and accelerator capacity per state, with derating and growth.       | Any capacity or performance outcome.                             | CG-05, CG-06, CG-08     |
| Failure          | How can outcomes be defeated?                                                                          | Failure scenarios with pre-state, initiator, propagation steps, safeguards, residual state and outcome effect.             | Always.                                                          | CG-04, CG-09            |
| Safeguard        | What prevents, detects, contains, corrects and recovers?                                               | Safeguard records with activation, authority, dependencies and state coverage, linked to scenarios and controls.           | Always.                                                          | CG-04 to CG-10          |
| Digital authority | Who and what can change infrastructure state?                                                         | Identities, privileges, control systems, management networks, remote-support paths, automations and break-glass.           | Any networked control system or BMC/out-of-band management.      | CG-07, CG-15            |
| Control/evidence | How is each claim assessed?                                                                            | Control-to-subject attachment, evidence requirements, evidence points, results, findings, UNKNOWNs.                        | Always.                                                          | CG-11, CG-12            |
| Decision         | What was decided, by whom, with what limits?                                                           | Gate results, score snapshot, recommendation, decision, conditions, validity.                                               | A decision is issued.                                            | All                     |
| Graph            | Is the model complete and consistent?                                                                  | Validated graph projection with ValidationResults.                                                                         | AR5 or above claimed.                                            | CG-02, CG-11            |
| Reporting        | What is disclosed, to whom?                                                                            | Statement-to-decision lineage, disclosure profile, redactions.                                                             | A report is issued.                                                  | —                       |

# Part VI - Capability architecture

## Capability record

**ARA-REQ-020** Every assessment shall be anchored to one approved Capability record containing the fields below (AIDCF-014 Capability profile). Fields that cannot be completed shall reference an UnknownRecord.

| **Field**                       | **Content**                                                                                                                                         | **AIDCF-007A family** |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| Identity, owner, lifecycle, version | Stable ID, accountable owner, lifecycle stage (PLAN to DECOMMISSION), record version.                                                         | CAP-01                |
| Mission and users               | Who relies on the capability and for what (internal research, external customers, regulated or sovereign users).                                   | CAP-03                |
| Workload model                  | Workload classes (pre-training, fine-tuning, batch inference, online inference, data processing), job sizes, synchronisation, duty cycle.          | CAP-04, CAP-05        |
| Demand model                    | Baseline, peak and transient demand for accelerators, power, cooling, fabric bandwidth and storage; growth forecast and scenario demand.           | CAP-04                |
| Service Outcomes                | Availability, performance, integrity and recovery outcomes (see specification below).                                                              | CAP-02                |
| Tolerances                      | Impact tolerance per outcome: maximum tolerable interruption, degradation and data or progress loss.                                               | CAP-03                |
| Criticality                     | Criticality class and its basis.                                                                                                                    | CAP-03                |
| Architecture baseline           | Current approved ArchitectureSnapshot.                                                                                                              | CAP-01, CAP-06        |
| Scope and boundary              | Included systems, excluded systems with rationale, external providers, shared or tenant boundaries.                                                | DEP-05                |
| Reassessment triggers           | Events that require the record and dependent decisions to be reviewed (for example new accelerator generation, rack density change, provider change). | CAP-06, EVA-06      |

## AI workload characteristics that shape the architecture

The parameters below shall be recorded in the capability profile where relevant. Values are site- and workload-specific; the defaults shown are illustrative only and carry no normative weight.

| **Parameter**                              | **Unit**           | **Illustrative default**              | **Why it matters**                                                                                                                       |
|--------------------------------------------|--------------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Rack design IT power                       | kW per rack        | 100 (liquid-cooled accelerator rack)  | Sets busway, rack PDU, CDU and TCS sizing; air-cooled designs at a fraction of this value cannot be assumed to scale.                    |
| Fraction of rack heat to liquid            | %                  | 80                                    | The remainder must be removed by air; hybrid racks need both paths assured.                                                               |
| Largest synchronous job size               | accelerators       | Site-specific                         | Defines the job-level fault domain and the fabric and storage capacity a single job needs.                                               |
| Job-level power swing                      | % of job power     | 50                                    | Correlated swings at iteration, communication and checkpoint phases load UPS, generators and the utility interface.                      |
| Power ramp rate at job start/stop          | MW per second      | Site-specific                         | Generator and grid-interface acceptance limits; may require scheduler ramp control or energy-storage buffering.                          |
| Checkpoint size                            | TB                 | Workload-specific                     | With checkpoint interval and target write time, sets burst write bandwidth.                                                              |
| Checkpoint interval                        | minutes            | 30                                    | Upper bound on lost training progress after a job-level failure.                                                                         |
| Thermal ride-through on loss of TCS flow   | seconds            | 30                                    | Time before accelerators throttle or trip; determines whether CDU pumps must be on UPS.                                                  |
| Inference latency objective                | ms at percentile   | Service-specific                      | Drives front-end network, placement and failover design.                                                                                 |

**ARA-REQ-021** Where training workloads are in scope, the capability profile shall state the job-level power swing and ramp-rate parameters, and the POW and THM architectures shall show how each is accommodated (equipment ratings, energy buffering, scheduler or firmware power management) or record an UnknownRecord.

## Service Outcome specification

**ARA-REQ-022** Every Service Outcome shall be an assessable object with the fields below.

| **Field**           | **Content**                                                                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| outcomeId           | Stable identifier.                                                                                                                                  |
| Outcome type        | AVAILABILITY, PERFORMANCE, INTEGRITY or RECOVERY (AIDCF-007A CAP-02).                                                                              |
| Measurable statement | For example "≥ N accelerators available to the training partition with fabric bandwidth ≥ B per accelerator" or "p99 inference latency ≤ L ms".   |
| Conditions and states | Operating states in which the outcome must hold, and the reduced outcome (if any) accepted in DEGRADED and MAINTENANCE.                          |
| Tolerance and duration | Maximum tolerable interruption, degradation and data or progress loss, and the measurement window.                                             |
| Required Functions  | REQUIRES_FUNCTION links.                                                                                                                            |
| Dependencies        | Material dependencies (derived from functions, reviewed).                                                                                           |
| Safeguards          | Safeguards relied on to keep the outcome within tolerance.                                                                                          |
| Evidence floor      | Sufficiency floor for decisive claims about the outcome (AIDCF-008).                                                                               |
| Critical gates      | Gates that must be evaluated for this outcome.                                                                                                      |
| Owner               | Accountable owner.                                                                                                                                  |
| Reassessment triggers | Changes that invalidate claims about the outcome.                                                                                                |

# Reference service chains

**ARA-REQ-023** Each in-scope workload shall be modelled as a service chain of Required Functions using the reference chains below as a starting point. Each function in the chain shall be linked by IMPLEMENTED_BY to the systems that realise it.

## Reference Service Chain - Training

**data ingest → dataset storage → data loading over storage fabric → distributed compute on accelerators over scale-up and scale-out fabrics → periodic checkpoint → model artifact output**

| **Aspect**                  | **Content**                                                                                                                                                                                                 |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key Required Functions      | Sustain dataset read throughput; deliver collective-communication bandwidth and latency; deliver accelerator capacity at rated performance; persist checkpoints durably within target write time; remove rack heat at design load; deliver continuous power with tolerable load dynamics. |
| Critical dependencies       | Parallel file system or object store; back-end RDMA fabric; scale-up domain integrity; scheduler and cluster manager; CDU/TCS and FWS; UPS and generation; time and identity services.                       |
| Characteristic failure paths | Single node or link failure stalls the synchronous job; fabric congestion or link flapping degrades step time across all ranks; checkpoint write stall extends lost progress; CDU pump trip leads to throttling across a rack row; correlated power swing exceeds generator load acceptance during utility outage. |
| Safeguards                  | Job-level fault detection and restart from checkpoint; spare-node pools; adaptive routing and congestion control; checkpoint verification; CDU redundancy and pumps on UPS; power capping and ramp control. |
| Primary gates               | CG-05, CG-06, CG-08, CG-09, CG-10                                                                                                                                                                           |
| Evidence points             | Scheduler job-failure and restart logs; fabric telemetry (errors, retransmissions, congestion notifications); checkpoint write and verification logs; CDU flow, pressure and supply temperature; EPMS waveform capture at job boundaries. |

## Reference Service Chain - Inference

**request ingress → load balancing and routing → pre-processing → model serving → accelerator execution → response**

| **Aspect**                  | **Content**                                                                                                                                                                         |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key Required Functions      | Accept and route requests within latency objective; load models from the artifact tier; execute on accelerators; fail over between serving instances, halls or sites.               |
| Critical dependencies       | Front-end network, DNS, certificate and identity services, model artifact tier, serving platform, telecom carriers, power and cooling of serving halls.                            |
| Characteristic failure paths | Carrier or DNS failure isolates the service; model artifact unavailability blocks scale-out; shared identity provider failure blocks all regions; thermal throttling raises tail latency. |
| Safeguards                  | Multi-carrier diverse routes; multi-instance and multi-site serving; cached artifacts; capacity headroom per failure domain.                                                        |
| Primary gates               | CG-03, CG-08, CG-09, CG-10                                                                                                                                                          |
| Evidence points             | Latency and error-rate telemetry by percentile; carrier route diversity records; failover test records; capacity-per-fault-domain calculations.                                    |

## Reference Service Chain - Fine-tuning

**dataset preparation → transfer into the environment → training → checkpoint → evaluation → registration in the model registry**

| **Aspect**                  | **Content**                                                                                                                                         |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Key Required Functions      | Controlled data transfer; isolated training partition; checkpoint persistence; evaluation compute; integrity-protected model registry.              |
| Critical dependencies       | Data transfer path, tenant isolation on shared clusters, storage integrity, registry service.                                                       |
| Characteristic failure paths | Cross-tenant data exposure through shared storage or fabric; corrupted checkpoint promoted to registry; partition pre-emption by higher-priority work. |
| Safeguards                  | Partitioning and traffic isolation; checksum verification at each hand-off; reservation controls.                                                  |
| Primary gates               | CG-08, CG-09, CG-15                                                                                                                                 |
| Evidence points             | Partition configuration; storage access logs; checksum records; scheduler reservation records.                                                     |

## Reference Service Chain - Sovereign

**authorised ingress → controlled processing within a declared jurisdiction and boundary → protected storage → approved egress**

| **Aspect**                  | **Content**                                                                                                                                                         |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key Required Functions      | Keep data, models and administrative control within the declared boundary; restrict remote support and telemetry export; preserve operation if external services are withdrawn. |
| Critical dependencies       | Identity and key management location; vendor remote support; firmware and software update sources; cloud control-plane dependencies; local spares.                |
| Characteristic failure paths | Hidden dependency on an out-of-boundary control plane or licence server; vendor support access from outside the boundary; telemetry export carrying restricted data. |
| Safeguards                  | Boundary enforcement at network and identity layers; local update mirrors; supervised support sessions; local spares and maintainers.                             |
| Primary gates               | CG-02, CG-03, CG-13, CG-15                                                                                                                                          |
| Evidence points             | Boundary definition and enforcement configuration; dependency discovery results; support-session logs; data-flow records.                                         |

## Reference Service Chain - Shared platform

**tenant intake → quota and reservation → scheduling → shared infrastructure execution → monitoring and accounting**

| **Aspect**                  | **Content**                                                                                                                                  |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Key Required Functions      | Allocate accelerator, fabric and storage capacity per tenant commitment; isolate tenants; attribute power and cooling to tenants.            |
| Critical dependencies       | Scheduler, cluster manager, fabric partitioning, storage multi-tenancy, metering.                                                             |
| Characteristic failure paths | Noisy-neighbour congestion breaches another tenant's performance outcome; scheduler failure affects all tenants; misattributed capacity. |
| Safeguards                  | Fabric partitioning and quality-of-service; reservation and contention controls; per-tenant monitoring.                                      |
| Primary gates               | CG-08, CG-09, CG-13                                                                                                                          |
| Evidence points             | Partition and QoS configuration; per-tenant performance telemetry; contention incident records.                                             |

## Reference Service Chain - Recovery

**detection → decision → containment → switch to alternate capacity → restoration of infrastructure → restart of workloads from checkpoint or replica → validation**

| **Aspect**                  | **Content**                                                                                                                                                                                         |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key Required Functions      | Detect and declare; contain blast radius; restore power and cooling in a safe sequence; restore control planes (identity, time, DNS, cluster manager, fabric manager); restore storage and checkpoints; restart and validate workloads. |
| Critical dependencies       | Recovery dependencies that are often outside the normal service chain: out-of-band management, break-glass identities, offline documentation, spares, vendor engineers, fuel and water replenishment. |
| Characteristic failure paths | Recovery tooling hosted on the failed infrastructure; circular dependency between identity and the systems needed to restore it; simultaneous power-on inrush or cooling demand exceeding available capacity. |
| Safeguards                  | Independent recovery tooling and identities; documented recovery sequence; staged power-on; tested restores.                                                                                       |
| Primary gates               | CG-10, CG-03, CG-09                                                                                                                                                                                 |
| Evidence points             | Recovery runbooks and sequence; exercise TestRecords with timings; restore verification logs.                                                                                                      |

# Domain reference architectures

Every domain profile below applies the following common rules, which are stated once and not repeated per domain.

**ARA-REQ-024** For each domain, the architecture shall: classify every element as owned, operated, third-party, shared or excluded; record its states across the full operating-state vocabulary; express capacity as rated, available, reserved, consumed, headroom and constraint per state; identify redundancy groups, common modes and containment boundaries; and record the reassessment triggers that apply to it.

**ARA-REQ-025** Control attachment for each domain shall use the AIDCF-007A families listed for that domain. Gate roles (CRITICAL or SUPPORTING) are assigned per control in the AIDCF-007A registry and shall be taken from it; the gates listed below are those for which the domain typically supplies controls, not a whole-domain mapping.

Relationship names in this section are the canonical AIDCF-014 types.

## GOV Domain Reference Architecture - Governance

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Governance charter, decision rights, accountable roles, policies and technical standard baselines, exceptions, assurance plan, independent review. |
| Key relationships      | OPERATED_BY (system to accountable party); GOVERNED_BY (assessment to programme); APPROVED_BY and REVIEWED_BY (decisions to review records).        |
| AI-specific concerns   | Decision rights over capacity allocation between training and inference; authority to accept risk on accelerated deployment schedules; accountability across facility, IT and provider boundaries. |
| Fault domains          | Single individual holding multiple approval roles; one committee approving both design and assurance.                                              |
| Evidence points        | Charters, terms of reference, RACI matrices, decision logs, exception registers, independence declarations.                                        |
| AIDCF-007A families    | GOV-01 Governance architecture (MCF-GOV-001 to MCF-GOV-004); GOV-02 Accountability and responsibility (MCF-GOV-005 to MCF-GOV-008); GOV-03 Policy and standards management (MCF-GOV-009 to MCF-GOV-012); GOV-04 Risk and assurance governance (MCF-GOV-013 to MCF-GOV-016); GOV-05 Stakeholder and regulatory interface (MCF-GOV-017 to MCF-GOV-020); GOV-06 Ethics, impartiality and competence (MCF-GOV-021 to MCF-GOV-024)                                                                                                                                          |
| Gates                  | CG-13, CG-14, CG-01                                                                                                                                  |
| Reassessment triggers  | Organisational change, new decision authority, policy revision, risk-appetite change.                                                              |

## CAP Domain Reference Architecture - Capability

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Capability register, Capability Instance, workload classes, Service Outcomes, criticality, demand model, operating envelope.                        |
| Key relationships      | HAS_OUTCOME; REQUIRES_FUNCTION; CONSUMES_RESOURCE (functions to power, cooling, accelerator capacity).                                               |
| AI-specific concerns   | Outcomes expressed in usable accelerator capacity and fabric performance, not only uptime; transient demand from synchronous jobs; rapid hardware-generation turnover changing the envelope. |
| Fault domains          | Outcome definitions that silently assume a single hall or site.                                                                                     |
| Evidence points        | Capability register, outcome specifications, SLOs, demand forecasts, envelope documents, commissioning acceptance records.                         |
| AIDCF-007A families    | CAP-01 Capability inventory (MCF-CAP-001 to MCF-CAP-004); CAP-02 Service outcome definition (MCF-CAP-005 to MCF-CAP-008); CAP-03 Criticality and materiality (MCF-CAP-009 to MCF-CAP-012); CAP-04 Demand and growth modelling (MCF-CAP-013 to MCF-CAP-016); CAP-05 Operating envelope (MCF-CAP-017 to MCF-CAP-020); CAP-06 Capability lifecycle and change (MCF-CAP-021 to MCF-CAP-024)                                                                                                                                          |
| Gates                  | CG-01, CG-02, CG-14                                                                                                                                  |
| Reassessment triggers  | New workload class, density increase, accelerator generation change, outcome or tolerance change.                                                  |

## DEP Domain Reference Architecture - Dependencies

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Dependency records, providers, shared services, common controllers, shared routes, concentration, boundaries.                                      |
| Key relationships      | DEPENDS_ON (with Dependency records); SHARES_FAULT_DOMAIN_WITH; RECOVERS_THROUGH.                                                                   |
| AI-specific concerns   | Concentration on a small number of accelerator, network and liquid-cooling OEMs; dependency of facility operations on cloud-hosted BMS or DCIM services; shared identity and time services across sites. |
| Fault domains          | Common controller across redundant trains; shared conduit or riser; single carrier entrance; single specialist maintainer.                         |
| Evidence points        | Dependency graph, contracts, route diagrams, discovery and reconciliation reports.                                                                  |
| AIDCF-007A families    | DEP-01 Dependency discovery (MCF-DEP-001 to MCF-DEP-004); DEP-02 Shared and common-mode dependencies (MCF-DEP-005 to MCF-DEP-008); DEP-03 External providers and utilities (MCF-DEP-009 to MCF-DEP-012); DEP-04 Concentration and substitutability (MCF-DEP-013 to MCF-DEP-016); DEP-05 Boundary and interface control (MCF-DEP-017 to MCF-DEP-020); DEP-06 Dependency monitoring and review (MCF-DEP-021 to MCF-DEP-024)                                                                                                                                          |
| Gates                  | CG-03, CG-09, CG-02                                                                                                                                  |
| Reassessment triggers  | Provider change, new shared service, route change, discovery of an unmodelled dependency.                                                          |

## PHY Domain Reference Architecture - Physical

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Site, building, hall, room, zone, row, rack position, structural elements, barriers, security and fire zones, egress routes.                        |
| Key relationships      | LOCATED_IN; EXPOSED_TO (site hazards); PROTECTED_BY (fire detection, suppression, access control).                                                  |
| AI-specific concerns   | Floor and slab loading of fully populated liquid-cooled racks and manifolds; water above or near electrical rooms; equipment delivery routes for heavy racks; fire strategy for halls with large lithium-ion inventories in BESS or UPS. |
| Fault domains          | Single building or structural zone; shared fire zone between redundant rooms; shared delivery route.                                               |
| Evidence points        | Drawings, structural calculations, inspection records, fire strategy, access logs, surveillance coverage maps.                                     |
| AIDCF-007A families    | PHY-01 Site and location resilience (MCF-PHY-001 to MCF-PHY-004); PHY-02 Building and structural integrity (MCF-PHY-005 to MCF-PHY-008); PHY-03 Physical zoning and segregation (MCF-PHY-009 to MCF-PHY-012); PHY-04 Access and surveillance (MCF-PHY-013 to MCF-PHY-016); PHY-05 Asset movement and custody (MCF-PHY-017 to MCF-PHY-020); PHY-06 Fire, life safety and emergency interfaces (MCF-PHY-021 to MCF-PHY-024)                                                                                                                                          |
| Gates                  | CG-02, CG-04, CG-09                                                                                                                                  |
| Reassessment triggers  | Rack weight or layout change, fire-strategy change, new hazard information, structural modification.                                             |

## POW Domain Reference Architecture - Power

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Utility interface and grid connection, MV switchgear, transformers, LV switchboards, UPS and BESS, generators and fuel, static and automatic transfer, busway, rack PDUs and power shelves, protection, earthing, EPMS. |
| Key relationships      | COMPOSED_OF; CONNECTS_TO (electrical interfaces); DEPENDS_ON (dependencyType ELECTRICAL); CONTROLLED_BY (EPMS, PLC, generator controllers); MONITORED_BY; SHARES_FAULT_DOMAIN_WITH; RECOVERS_THROUGH. |
| AI-specific concerns   | Correlated, fast load swings from synchronous training at iteration, checkpoint and job boundaries; load-step acceptance of generators on utility loss; UPS and BESS sizing for both runtime and dynamic response; harmonics and power-factor behaviour of accelerator power supplies; mechanical loads (CDU pumps, controls) that must be on uninterruptible supply; grid-interface obligations for large, variable loads. |
| Fault domains          | Shared MV ring or single utility substation; common generator paralleling controls; shared fuel system; busway serving a full row; static transfer switch as a single point.            |
| Evidence points        | Single-line diagrams, protection coordination studies, EPMS waveform and event capture, UPS and generator load-bank and transfer test records, fuel autonomy calculations, maintenance records. |
| AIDCF-007A families    | POW-01 Utility and grid interface (MCF-POW-001 to MCF-POW-004); POW-02 Generation and fuel (MCF-POW-005 to MCF-POW-008); POW-03 UPS and energy storage (MCF-POW-009 to MCF-POW-012); POW-04 Distribution and protection (MCF-POW-013 to MCF-POW-016); POW-05 Power quality and transient response (MCF-POW-017 to MCF-POW-020); POW-06 Electrical monitoring, maintenance and recovery (MCF-POW-021 to MCF-POW-024)                                                                                                                                          |
| Gates                  | CG-05, CG-04, CG-07, CG-10                                                                                                                           |
| Reassessment triggers  | New load or density, firmware change affecting power management, UPS or generator change, protection setting change, utility connection change.  |

## THM Domain Reference Architecture - Thermal

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Heat-rejection plant (chillers, dry coolers, cooling towers), facility water system (FWS), coolant distribution units (CDUs), technology cooling system (TCS) secondary loops, manifolds, quick disconnects, cold plates, rear-door heat exchangers, CRAH and in-row units, containment, water treatment, leak detection, thermal controls. |
| Key relationships      | COMPOSED_OF; CONNECTS_TO (thermal and fluid interfaces); DEPENDS_ON (dependencyType THERMAL, FLUID, ELECTRICAL, CONTROL); CONTROLLED_BY (BMS, CDU controllers); MONITORED_BY; SHARES_FAULT_DOMAIN_WITH; PROTECTED_BY (leak detection, isolation valves). |
| AI-specific concerns   | Short thermal ride-through of cold-plate-cooled accelerators on loss of TCS flow; CDU pumps and controls on UPS; FWS supply temperature class and approach across seasons (ASHRAE TC 9.9 liquid-cooling guidance); TCS fluid quality, filtration and compatibility of wetted materials; residual air heat in hybrid racks; leak consequence near electrical equipment; thermal transients when large jobs start. |
| Fault domains          | Common CDU controller or BMS logic across redundant CDUs; shared FWS header; single heat-rejection plant per hall; common make-up water source.     |
| Evidence points        | P&IDs, CDU and TCS commissioning records, flow, pressure and temperature telemetry, fluid-quality test results, leak-detection test records, seasonal capacity analyses. |
| AIDCF-007A families    | THM-01 Thermal architecture and capacity (MCF-THM-001 to MCF-THM-004); THM-02 Air cooling systems (MCF-THM-005 to MCF-THM-008); THM-03 Liquid cooling systems (MCF-THM-009 to MCF-THM-012); THM-04 Heat rejection and water systems (MCF-THM-013 to MCF-THM-016); THM-05 Fluid quality and leak management (MCF-THM-017 to MCF-THM-020); THM-06 Thermal control, maintenance and recovery (MCF-THM-021 to MCF-THM-024)                                                                                                                                          |
| Gates                  | CG-06, CG-04, CG-07, CG-09, CG-10                                                                                                                    |
| Reassessment triggers  | Rack density or cold-plate design change, CDU or TCS modification, fluid change, control-logic change, seasonal extreme beyond design basis.       |

## ENV Domain Reference Architecture - Environment

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Environmental sensors, energy and water meters, water sources and discharge, hazardous materials (batteries, refrigerants, coolants, fuel), waste streams, climate hazard exposure. |
| Key relationships      | MONITORED_BY; CONSUMES_RESOURCE (water, energy); EXPOSED_TO (heatwave, drought, flood).                                                             |
| AI-specific concerns   | Water use of evaporative heat rejection at high load; refrigerant and coolant handling at scale; large battery inventories; resilience–efficiency trade-offs during heatwaves. |
| Fault domains          | Single water source for make-up water; regional heatwave affecting all heat-rejection plant simultaneously.                                         |
| Evidence points        | Metering data, permits, water-quality records, hazardous-material registers, climate risk assessments.                                             |
| AIDCF-007A families    | ENV-01 Environmental operating conditions (MCF-ENV-001 to MCF-ENV-004); ENV-02 Energy performance (MCF-ENV-005 to MCF-ENV-008); ENV-03 Water performance (MCF-ENV-009 to MCF-ENV-012); ENV-04 Carbon and resource reporting (MCF-ENV-013 to MCF-ENV-016); ENV-05 Hazardous materials and waste (MCF-ENV-017 to MCF-ENV-020); ENV-06 Climate adaptation and resource continuity (MCF-ENV-021 to MCF-ENV-024)                                                                                                                                          |
| Gates                  | CG-04, CG-06, CG-02                                                                                                                                  |
| Reassessment triggers  | Permit change, water restriction, new hazardous inventory, climate-hazard reassessment.                                                            |

## CMP Domain Reference Architecture - Compute

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Accelerators, nodes, rack-scale systems, scale-up domains, clusters and partitions, scheduler and cluster manager, BMCs, firmware and drivers, spare pools. |
| Key relationships      | COMPOSED_OF (cluster to node to accelerator); DEPENDS_ON (fabric, storage, power, cooling, scheduler); CONTROLLED_BY (cluster manager, BMC); MONITORED_BY; SHARES_FAULT_DOMAIN_WITH (scale-up domain, rack, power or cooling segment). |
| AI-specific concerns   | Usable versus installed accelerator capacity after failures and reservations; integrity of the scale-up domain (one failed switch tray or link can degrade a whole rack-scale system); firmware and driver compatibility across thousands of nodes; silent data corruption and degraded accelerators that pass basic health checks; power capping interaction with facility limits. |
| Fault domains          | Scale-up domain, rack, power segment, CDU segment, scheduler instance, firmware baseline.                                                           |
| Evidence points        | Topology exports, accelerator and node telemetry, burn-in and diagnostic results, firmware inventories, scheduler configuration, RMA records.      |
| AIDCF-007A families    | CMP-01 Compute architecture and configuration (MCF-CMP-001 to MCF-CMP-004); CMP-02 Cluster and scale-up domains (MCF-CMP-005 to MCF-CMP-008); CMP-03 Capacity, scheduling and utilisation (MCF-CMP-009 to MCF-CMP-012); CMP-04 Firmware, driver and compatibility (MCF-CMP-013 to MCF-CMP-016); CMP-05 Compute health and observability (MCF-CMP-017 to MCF-CMP-020); CMP-06 Compute lifecycle and recovery (MCF-CMP-021 to MCF-CMP-024)                                                                                                                                          |
| Gates                  | CG-08, CG-09, CG-10, CG-14                                                                                                                           |
| Reassessment triggers  | Firmware or driver upgrade, accelerator generation change, partition change, abnormal failure rate.                                               |

## STO Domain Reference Architecture - Storage

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Training-data tier, checkpoint tier, model and artifact tier, archive tier, storage controllers and metadata services, replication and erasure coding, immutable recovery copies. |
| Key relationships      | COMPOSED_OF; DEPENDS_ON (storage fabric, power, metadata service); RECOVERS_THROUGH (checkpoint and replica); PROTECTED_BY (snapshots, immutable copies). |
| AI-specific concerns   | Checkpoint burst write bandwidth across thousands of clients; metadata-service saturation at job start; checkpoint integrity and completeness before older checkpoints are deleted; restore bandwidth for restart; ransomware-resilient copies of model artifacts. |
| Fault domains          | Metadata service, storage controller pair, single storage fabric, single site for all checkpoint copies.                                            |
| Evidence points        | Throughput and latency telemetry during checkpoint windows, scrubbing and checksum records, replication status, restore test records.              |
| AIDCF-007A families    | STO-01 Storage architecture and tiering (MCF-STO-001 to MCF-STO-004); STO-02 Performance and capacity (MCF-STO-005 to MCF-STO-008); STO-03 Integrity and consistency (MCF-STO-009 to MCF-STO-012); STO-04 Protection and replication (MCF-STO-013 to MCF-STO-016); STO-05 Checkpoint and recovery services (MCF-STO-017 to MCF-STO-020); STO-06 Storage monitoring and lifecycle (MCF-STO-021 to MCF-STO-024)                                                                                                                                          |
| Gates                  | CG-08, CG-10, CG-09                                                                                                                                  |
| Reassessment triggers  | Checkpoint size or frequency change, storage software upgrade, capacity threshold breach, integrity error.                                        |

## NET Domain Reference Architecture - Network

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Scale-up interconnect, scale-out back-end fabric (RDMA over InfiniBand or Ethernet), storage fabric, front-end network, management and out-of-band networks, optics and cabling, fabric managers and controllers, time services (NTP/PTP), DNS. |
| Key relationships      | CONNECTS_TO; DEPENDS_ON (dependencyType NETWORK, TIMING); CONTROLLED_BY (fabric manager, SDN controller); MONITORED_BY; SHARES_FAULT_DOMAIN_WITH (leaf, spine plane, rail, cable path). |
| AI-specific concerns   | Collective-communication performance is limited by the slowest path; link flaps and optic degradation stall synchronous jobs; congestion control and lossless configuration must be correct end to end; rail-optimised topologies create plane-level fault domains; fabric managers are single points of control. |
| Fault domains          | Spine plane, rail, leaf pair, fabric manager, optic batch, cable tray route.                                                                         |
| Evidence points        | Topology and cabling records, link error and retransmission counters, congestion telemetry, collective benchmark results, configuration baselines. |
| AIDCF-007A families    | NET-01 Scale-up and scale-out fabrics (MCF-NET-001 to MCF-NET-004); NET-02 Performance and congestion control (MCF-NET-005 to MCF-NET-008); NET-03 Storage and service networks (MCF-NET-009 to MCF-NET-012); NET-04 Management and out-of-band networks (MCF-NET-013 to MCF-NET-016); NET-05 Physical connectivity and optics (MCF-NET-017 to MCF-NET-020); NET-06 Network control and observability (MCF-NET-021 to MCF-NET-024)                                                                                                                                          |
| Gates                  | CG-08, CG-09, CG-15, CG-10                                                                                                                           |
| Reassessment triggers  | Topology change, fabric software upgrade, optics vendor change, congestion-control change.                                                         |

## OPS Domain Reference Architecture - Operations

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Operating model and staffing, procedures, method statements, permits to work, lockout/tagout, maintenance, alarms, incidents, change and configuration, capacity operations. |
| Key relationships      | OPERATED_BY; PROTECTED_BY (procedural safeguards); GOVERNED_BY (procedures to controls).                                                            |
| AI-specific concerns   | Coordinated facility and IT change windows for liquid-cooled racks; work on live TCS loops; alarm floods from thousands of accelerator sensors; coupling between scheduler actions and facility load. |
| Fault domains          | Single shift with sole competent person for a system; shared alarm platform for facility and IT.                                                    |
| Evidence points        | Work orders, permits, shift logs, alarm statistics, incident and problem records, change records.                                                  |
| AIDCF-007A families    | OPS-01 Operating model and staffing (MCF-OPS-001 to MCF-OPS-004); OPS-02 Procedure and work control (MCF-OPS-005 to MCF-OPS-008); OPS-03 Maintenance and reliability (MCF-OPS-009 to MCF-OPS-012); OPS-04 Alarm, incident and problem management (MCF-OPS-013 to MCF-OPS-016); OPS-05 Change and configuration management (MCF-OPS-017 to MCF-OPS-020); OPS-06 Capacity and service operations (MCF-OPS-021 to MCF-OPS-024)                                                                                                                                          |
| Gates                  | CG-07, CG-13, CG-14, CG-04                                                                                                                           |
| Reassessment triggers  | Staffing model change, major incident, procedure change, maintenance backlog threshold.                                                            |

## RES Domain Reference Architecture - Resilience

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Minimum service outcomes, fault domains and containment boundaries, continuity strategy, alternative capacity, recovery plans and sequences, exercises, crisis arrangements. |
| Key relationships      | RECOVERS_THROUGH; SHARES_FAULT_DOMAIN_WITH; PROPAGATES_TO (scenario steps); PROTECTED_BY.                                                           |
| AI-specific concerns   | Lost-progress and restart-time objectives for training; alternative capacity that matches accelerator generation and fabric scale; recovery sequencing across power, cooling, control planes and storage. |
| Fault domains          | Recovery dependencies shared with the primary (identity, tooling, people).                                                                          |
| Evidence points        | Scenario analyses, recovery runbooks, exercise records with timings, lessons-learned and retest records.                                           |
| AIDCF-007A families    | RES-01 Resilience strategy (MCF-RES-001 to MCF-RES-004); RES-02 Fault-domain and containment design (MCF-RES-005 to MCF-RES-008); RES-03 Continuity planning (MCF-RES-009 to MCF-RES-012); RES-04 Recovery planning (MCF-RES-013 to MCF-RES-016); RES-05 Testing and exercising (MCF-RES-017 to MCF-RES-020); RES-06 Crisis and adaptive response (MCF-RES-021 to MCF-RES-024)                                                                                                                                          |
| Gates                  | CG-09, CG-10, CG-03                                                                                                                                  |
| Reassessment triggers  | Exercise failure, incident, architecture change affecting fault domains, alternative-capacity change.                                              |

## SUP Domain Reference Architecture - Supply Chain

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Suppliers and OEMs, contracts, component provenance, firmware and software release sources, spares and logistics, remote support access.           |
| Key relationships      | DEPENDS_ON (dependencyType SUPPLIER); OPERATED_BY (maintainers); CONTROLLED_BY (remote support paths).                                              |
| AI-specific concerns   | Long lead times for accelerators, optics, CDUs and switchgear; firmware supply for BMCs, accelerators, switches and CDU controllers; vendor remote access into OT and BMC networks. |
| Fault domains          | Single OEM for accelerators and fabric; single spares depot; shared firmware signing infrastructure.                                                |
| Evidence points        | Supplier due-diligence records, contracts, provenance records, signature validation logs, spares inventories, remote-session logs.                 |
| AIDCF-007A families    | SUP-01 Supplier due diligence (MCF-SUP-001 to MCF-SUP-004); SUP-02 Contract and service obligations (MCF-SUP-005 to MCF-SUP-008); SUP-03 Hardware and component provenance (MCF-SUP-009 to MCF-SUP-012); SUP-04 Software, firmware and update supply (MCF-SUP-013 to MCF-SUP-016); SUP-05 Spares, logistics and obsolescence (MCF-SUP-017 to MCF-SUP-020); SUP-06 Remote support and third-party access (MCF-SUP-021 to MCF-SUP-024)                                                                                                                                          |
| Gates                  | CG-03, CG-13, CG-15, CG-10                                                                                                                           |
| Reassessment triggers  | Supplier change, end-of-life notice, vulnerability disclosure, support-access change.                                                              |

## SEC Domain Reference Architecture - Security

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Human and machine identities, privileged access, control planes (BMS, EPMS, cluster manager, fabric controller, storage controller), security zones, management-plane segmentation, gateways, remote access, vulnerability and patching, detection and response, automated and AI-enabled action. |
| Key relationships      | CONTROLLED_BY; CONNECTS_TO (management interfaces); PROTECTED_BY; EXPOSED_TO (threats).                                                             |
| AI-specific concerns   | BMC and out-of-band management can power off or reflash large numbers of nodes; cluster managers and schedulers can shift megawatts of load; automated or AI-enabled operations tools may hold write access to facility controls. |
| Fault domains          | Shared identity provider across facility and IT; single privileged-access system; flat management network.                                        |
| Evidence points        | Access configurations, privilege inventories, segmentation tests, logs, vulnerability scans, automation allowlists.                                |
| AIDCF-007A families    | SEC-01 Identity and privileged access (MCF-SEC-001 to MCF-SEC-004); SEC-02 Control-plane protection (MCF-SEC-005 to MCF-SEC-008); SEC-03 Network security and segmentation (MCF-SEC-009 to MCF-SEC-012); SEC-04 Configuration, vulnerability and patching (MCF-SEC-013 to MCF-SEC-016); SEC-05 Detection and response (MCF-SEC-017 to MCF-SEC-020); SEC-06 AI-enabled and automated action (MCF-SEC-021 to MCF-SEC-024)                                                                                                                                          |
| Gates                  | CG-15, CG-07, CG-09                                                                                                                                  |
| Reassessment triggers  | New management path, identity-system change, vulnerability affecting a control plane, new automation with write access.                           |

## EVA Domain Reference Architecture - Evidence/Assurance

| **Aspect**             | **Content**                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Objects                | Evidence taxonomy and repository, provenance, assessment plans, findings, UNKNOWN records, gate evaluation, decisions, reassessment.                 |
| Key relationships      | EVIDENCED_BY; SUPPORTS; CHALLENGES; QUALIFIES; HAS_FINDING; HAS_UNKNOWN; EVALUATES_GATE; CONSTRAINS.                                                |
| AI-specific concerns   | Very high telemetry volumes requiring sampling and summarisation with preserved lineage; evidence produced by the same automation that is being assessed. |
| Fault domains          | Evidence repository hosted on the infrastructure being assessed; single evidence custodian.                                                         |
| Evidence points        | Evidence manifests, workpapers, review records, gate worksheets.                                                                                   |
| AIDCF-007A families    | EVA-01 Evidence architecture (MCF-EVA-001 to MCF-EVA-004); EVA-02 Evidence provenance and quality (MCF-EVA-005 to MCF-EVA-008); EVA-03 Assessment planning and execution (MCF-EVA-009 to MCF-EVA-012); EVA-04 Findings, UNKNOWN and limitations (MCF-EVA-013 to MCF-EVA-016); EVA-05 Critical gates and decisions (MCF-EVA-017 to MCF-EVA-020); EVA-06 Reassessment and continuing assurance (MCF-EVA-021 to MCF-EVA-024)                                                                                                                                          |
| Gates                  | CG-11, CG-12 (meta-gates, evaluated across all controls)                                                                                            |
| Reassessment triggers  | Evidence expiry, source unavailability, conflict, change trigger.                                                                                  |

# System architecture cards

**ARA-REQ-026** Each InfrastructureSystem that implements a RequiredFunction of an in-scope Service Outcome shall have a system card with the content below. The cards in this section give the reference content for common AI data-centre systems.

The common card structure is: purpose and linked functions; components and interfaces; capacity and envelope parameters; states of concern; dependencies; fault domains and common modes; principal failure modes; safeguards; evidence; AIDCF-007A families; gates; owners (design, operation, maintenance, evidence); reassessment triggers. Owners and triggers are site-specific and recorded per instance.

## System Architecture Card - Incoming power

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Deliver utility power within contracted capacity and quality to the site's MV distribution.                                         |
| Components/interfaces | Utility feeders, point of connection, MV switchgear, protection relays, metering, transfer schemes.                                 |
| Capacity/envelope     | Contracted import capacity; firm versus non-firm capacity; permitted ramp rates and power-quality limits at the point of connection. |
| States of concern     | Utility outage, voltage sag, planned utility maintenance, curtailment or demand-response events.                                    |
| Dependencies          | Utility network, upstream substations, utility protection schemes and communications.                                                |
| Fault domains         | Common upstream substation or transmission corridor for nominally diverse feeds.                                                    |
| Failure modes         | Loss of supply, sag or swell, protection mis-operation, curtailment.                                                                |
| Safeguards            | Diverse feeds where available, UPS ride-through, generator transfer, load management agreements.                                    |
| Evidence              | Connection agreements, utility reliability data, power-quality monitoring, protection studies.                                      |
| AIDCF-007A families   | POW-01, POW-05, DEP-03                                                                                                              |
| Gates                 | CG-05, CG-03                                                                                                                        |

## System Architecture Card - Generation/fuel

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Supply site load during utility loss for the declared autonomy.                                                                     |
| Components/interfaces | Generator sets, starting systems, paralleling and control, fuel storage, day tanks, fuel polishing, replenishment contracts.         |
| Capacity/envelope     | Rated and site-derated output; block-load and load-step acceptance; start and transfer time; fuel autonomy at design load.          |
| States of concern     | EMERGENCY (sustained run), MAINTENANCE (sets out of service), RECOVERY (retransfer to utility).                                     |
| Dependencies          | Starting batteries, controls power, fuel supply, cooling for generators, ventilation.                                               |
| Fault domains         | Common paralleling controller or master PLC; shared fuel system; common fuel batch quality.                                         |
| Failure modes         | Failure to start, failure to synchronise, failure to accept load step from correlated AI load, fuel contamination.                  |
| Safeguards            | N+x sets, independent controls, load-bank testing, fuel quality testing, load-step management with UPS and scheduler.               |
| Evidence              | Load-bank and transfer test records, maintenance records, fuel test results, autonomy calculations.                                  |
| AIDCF-007A families   | POW-02, POW-05, POW-06                                                                                                              |
| Gates                 | CG-05, CG-10, CG-04                                                                                                                 |

## System Architecture Card - UPS/storage

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Provide continuous power through utility disturbances and transfer to generation; buffer dynamic load.                              |
| Components/interfaces | UPS modules, rectifiers and inverters, static and maintenance bypass, batteries or BESS, battery management systems.                |
| Capacity/envelope     | Rated kW; runtime at load; dynamic response to load steps and swings; derating with age and temperature.                            |
| States of concern     | Bypass operation (loss of conditioning), battery discharge, MAINTENANCE with reduced redundancy, eco-mode operation.               |
| Dependencies          | Upstream supply, battery room cooling and ventilation, battery management system communications.                                   |
| Fault domains         | Shared bypass, shared battery string, common control firmware.                                                                      |
| Failure modes         | Transfer to bypass under fault, battery failure, thermal runaway, firmware fault.                                                   |
| Safeguards            | Redundant modules, battery monitoring, fire detection and suppression appropriate to battery chemistry, bypass governance.         |
| Evidence              | Test records, battery monitoring data, runtime calculations, firmware inventory.                                                    |
| AIDCF-007A families   | POW-03, POW-05, ENV-05, PHY-06                                                                                                      |
| Gates                 | CG-05, CG-04, CG-10                                                                                                                 |

## System Architecture Card - Distribution

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Distribute power from UPS and switchboards to racks with selective protection.                                                      |
| Components/interfaces | LV switchboards, busway, tap-off units, rack PDUs or power shelves, protection devices, earthing and bonding.                        |
| Capacity/envelope     | Busway and PDU ampacity per row and rack; per-rack design power; diversity assumptions validated against AI load.                   |
| States of concern     | Single-path operation during maintenance; overloaded busway after density changes.                                                 |
| Dependencies          | Upstream UPS paths; EPMS for monitoring; cooling of electrical rooms.                                                               |
| Fault domains         | Busway serving a full row; shared switchboard section.                                                                              |
| Failure modes         | Overload, loss of selectivity, connection failure, arc-flash event.                                                                 |
| Safeguards            | Dual-path distribution, selective coordination, thermographic inspection, arc-flash mitigation.                                    |
| Evidence              | Coordination studies, arc-flash studies, thermographic records, load measurements.                                                 |
| AIDCF-007A families   | POW-04, POW-06, OPS-02                                                                                                              |
| Gates                 | CG-05, CG-04, CG-09                                                                                                                 |

## System Architecture Card - Air cooling

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Remove the air-side heat (including residual heat from liquid-cooled racks and all heat from air-cooled equipment).                 |
| Components/interfaces | Chillers or dry coolers, pumps, CRAH or in-row units, containment, airflow controls.                                                 |
| Capacity/envelope     | Air-side capacity per hall at design ambient; inlet temperature envelope (ASHRAE TC 9.9 thermal guidelines as declared).           |
| States of concern     | Unit maintenance, fan failures, containment breach, heatwave.                                                                       |
| Dependencies          | FWS or chilled water, power to fans and pumps, BMS.                                                                                 |
| Fault domains         | Common chilled-water loop; common BMS control logic.                                                                               |
| Failure modes         | Loss of airflow, recirculation, control instability.                                                                               |
| Safeguards            | N+x units, containment, temperature monitoring at inlet.                                                                           |
| Evidence              | CFD or measured airflow studies, inlet temperature telemetry, commissioning records.                                               |
| AIDCF-007A families   | THM-01, THM-02, THM-06, ENV-01                                                                                                      |
| Gates                 | CG-06                                                                                                                               |

## System Architecture Card - Liquid cooling (FWS, CDU and TCS)

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Remove the liquid-side heat from cold plates at design load and transient conditions, keeping accelerator coolant supply within the OEM envelope. |
| Components/interfaces | FWS (primary loop to heat rejection); CDUs (liquid-to-liquid or liquid-to-air, in-row or in-rack) with pumps, heat exchangers, filters and controls; TCS secondary loop, manifolds, quick disconnects, hoses, cold plates; leak detection; isolation valves. |
| Capacity/envelope     | CDU heat-transfer capacity at stated FWS supply temperature and approach; TCS flow rate and differential pressure per rack; supply temperature limits; filtration; fluid composition (for example propylene-glycol mixtures) and quality limits. All values per OEM specification and capability profile. |
| States of concern     | CDU pump failover; FWS temperature excursion; TCS fill, drain and maintenance; rack connection and disconnection; utility-to-generator transfer. |
| Dependencies          | Uninterruptible power for CDU pumps and controls; FWS from heat rejection; BMS or CDU controller; make-up fluid supply.               |
| Fault domains         | Multiple CDUs on one TCS header; shared CDU control logic or controller; common FWS header; single fluid batch.                     |
| Failure modes         | Loss of flow, loss of pressure, supply temperature rise, leak at quick disconnect or manifold, fouling or particulate blockage of cold plates, control instability, air entrainment. |
| Safeguards            | CDU redundancy with automatic failover; pumps and controls on UPS; leak detection with isolation; fluid-quality monitoring and filtration; accelerator thermal throttling as last-line protection (not a continuity safeguard). |
| Evidence              | Commissioning and integrated systems test records, CDU telemetry, fluid analysis reports, leak-detection tests, failover test records.             |
| AIDCF-007A families   | THM-03, THM-04, THM-05, THM-06, POW-03                                                                                              |
| Gates                 | CG-06, CG-04, CG-07, CG-09, CG-10                                                                                                   |

## System Architecture Card - Compute cluster

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Deliver usable accelerator capacity at rated performance to the scheduler.                                                          |
| Components/interfaces | Accelerator nodes or rack-scale systems, scale-up domains, host CPUs and memory, local NVMe, BMCs, firmware and drivers, scheduler and cluster manager. |
| Capacity/envelope     | Installed, healthy, allocatable and reserved accelerators; per-rack power and cooling limits; power-capping settings.               |
| States of concern     | Rolling firmware upgrades, partial scale-up domain degradation, drain for maintenance.                                              |
| Dependencies          | Power, cooling, fabrics, storage, identity, time, scheduler.                                                                        |
| Fault domains         | Scale-up domain, rack, power and CDU segment, firmware baseline.                                                                    |
| Failure modes         | Accelerator or node failure, silent data corruption, thermal throttling, firmware incompatibility.                                 |
| Safeguards            | Health checks and burn-in, spare pools, staged firmware rollout with rollback, job checkpointing.                                   |
| Evidence              | Topology and inventory exports, health telemetry, diagnostic results, firmware inventory, RMA records.                              |
| AIDCF-007A families   | CMP-01 to CMP-06                                                                                                                    |
| Gates                 | CG-08, CG-09, CG-14                                                                                                                 |

## System Architecture Card - Storage platform

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Serve training data, persist checkpoints and protect model artifacts.                                                               |
| Components/interfaces | Storage tiers, controllers, metadata services, client mounts, replication and erasure coding, snapshot and immutable copy services. |
| Capacity/envelope     | Sustained read throughput, burst write bandwidth for checkpoints, metadata operations rate, usable capacity and headroom.            |
| States of concern     | Rebuild after media failure, controller failover, replication lag.                                                                  |
| Dependencies          | Storage fabric, power, cooling, metadata service, identity.                                                                         |
| Fault domains         | Metadata service, controller pair, single site.                                                                                     |
| Failure modes         | Checkpoint write stall, metadata saturation, silent corruption, ransomware encryption.                                              |
| Safeguards            | Checksums and scrubbing, replication, immutable copies, checkpoint verification before retention rotation.                          |
| Evidence              | Performance telemetry, integrity reports, restore tests.                                                                            |
| AIDCF-007A families   | STO-01 to STO-06                                                                                                                    |
| Gates                 | CG-08, CG-10                                                                                                                        |

## System Architecture Card - Network fabrics

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Provide scale-up, scale-out, storage, front-end and management connectivity with required bandwidth, latency and isolation.         |
| Components/interfaces | Scale-up switches and links, back-end leaf and spine switches, NICs, optics and cables, fabric managers, front-end routers, storage fabric. |
| Capacity/envelope     | Bisection bandwidth, oversubscription ratio per tier, link speeds, congestion thresholds.                                           |
| States of concern     | Link or switch failure, fabric-manager failover, rolling upgrade.                                                                   |
| Dependencies          | Power and cooling of network racks, fabric manager, time service, optics supply.                                                    |
| Fault domains         | Spine plane, rail, leaf pair, fabric manager, optic batch.                                                                          |
| Failure modes         | Link flaps, optic degradation, congestion collapse, misconfiguration, fabric-manager failure.                                       |
| Safeguards            | Path diversity, adaptive routing, congestion control, configuration management, spare optics.                                      |
| Evidence              | Topology exports, error counters, congestion telemetry, collective benchmarks.                                                      |
| AIDCF-007A families   | NET-01 to NET-06                                                                                                                    |
| Gates                 | CG-08, CG-09                                                                                                                        |

## System Architecture Card - BMC and out-of-band management

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Provide independent management access to nodes, switches, PDUs, power shelves and rack liquid-cooling controllers for power control, firmware, console and recovery. |
| Components/interfaces | BMCs (Redfish or IPMI interfaces), rack and chassis management controllers, out-of-band switches, console servers, management jump hosts. |
| Capacity/envelope     | Reachability of every managed device; independence from in-band networks and identity where required for recovery.                 |
| States of concern     | RECOVERY (used to restore after in-band failure), EMERGENCY (remote power-off), MAINTENANCE (firmware updates).                    |
| Dependencies          | Separate power path where specified, OOB identity, out-of-band carrier link if remote.                                              |
| Fault domains         | OOB network sharing switches or identity with in-band; single console aggregation point.                                           |
| Failure modes         | OOB unavailable when needed; compromise enabling mass power-off or malicious firmware; stale BMC firmware.                         |
| Safeguards            | Segmentation, privileged access with approval, firmware signature validation, break-glass governance.                              |
| Evidence              | Network design and segmentation tests, BMC firmware inventory, access logs, recovery exercise records.                             |
| AIDCF-007A families   | NET-04, SEC-01, SEC-02, SEC-03, SUP-04                                                                                              |
| Gates                 | CG-15, CG-07, CG-10                                                                                                                 |

## System Architecture Card - Cluster and fabric control planes

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Allocate, configure and orchestrate compute, fabric and storage resources.                                                          |
| Components/interfaces | Scheduler, cluster manager, provisioning, fabric manager or subnet manager, storage management, identity, time, DNS and certificate services. |
| Capacity/envelope     | Control-plane availability; number of nodes manageable; scheduling latency.                                                         |
| States of concern     | Control-plane failover; upgrade; recovery after site-level event (control planes restored first).                                   |
| Dependencies          | Identity, time, DNS, databases, storage, management network.                                                                        |
| Fault domains         | Single scheduler instance; shared database; shared identity across facility and IT.                                                |
| Failure modes         | Unavailable control plane blocks all new work; erroneous action drains or powers down many nodes; unsafe load changes at facility scale. |
| Safeguards            | High availability, change control, command allowlists and approval for bulk actions, ramp-rate limits.                              |
| Evidence              | HA configuration, change records, access logs, failover test records.                                                               |
| AIDCF-007A families   | SEC-02, SEC-06, CMP-03, NET-06, OPS-05                                                                                              |
| Gates                 | CG-15, CG-08, CG-14                                                                                                                 |

## System Architecture Card - BMS/EPMS

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Monitor and control facility power and mechanical systems.                                                                          |
| Components/interfaces | Sensors, controllers and PLCs, gateways, HMIs, historians, CDU controller integrations.                                             |
| Capacity/envelope     | Point counts, scan rates, historian retention, control-loop response.                                                               |
| States of concern     | Controller failover, network loss (fail-safe states), firmware update.                                                              |
| Dependencies          | Power, OT network, time service.                                                                                                    |
| Fault domains         | Single controller for redundant plant; shared OT network.                                                                           |
| Failure modes         | Loss of control, wrong command, sensor drift, unsafe default on communication loss.                                                 |
| Safeguards            | Redundant controllers, defined fail-safe states, sensor validation, segmentation.                                                  |
| Evidence              | Control narratives, cause-and-effect matrices, fail-safe tests, configuration backups.                                              |
| AIDCF-007A families   | SEC-02, THM-06, POW-06, OPS-05                                                                                                      |
| Gates                 | CG-07, CG-15, CG-06, CG-05                                                                                                          |

## System Architecture Card - Operations centre

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Detect, decide and act across facility and IT.                                                                                      |
| Components/interfaces | People, monitoring platforms, work management, incident and change tooling.                                                         |
| Capacity/envelope     | Staffing per shift; alarm handling capacity.                                                                                        |
| States of concern     | Shift handover, major incident, site evacuation.                                                                                    |
| Dependencies          | Monitoring platforms, communications, documentation access.                                                                         |
| Fault domains         | Single operations centre; tooling hosted on the monitored infrastructure.                                                          |
| Failure modes         | Alarm overload, missed handover information, unavailable tooling.                                                                   |
| Safeguards            | Alarm rationalisation, handover procedures, alternate operations location.                                                         |
| Evidence              | Staffing rosters, alarm statistics, incident records.                                                                               |
| AIDCF-007A families   | OPS-01, OPS-04, RES-06                                                                                                              |
| Gates                 | CG-13, CG-07                                                                                                                        |

## System Architecture Card - Provider ecosystem

| **Aspect**            | **Content**                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Purpose               | Represent external services on which outcomes depend.                                                                               |
| Components/interfaces | Utility, telecom carriers, water, fuel, OEM support, logistics, cloud and SaaS services.                                             |
| Capacity/envelope     | Contracted service levels and response times.                                                                                       |
| States of concern     | Regional events affecting several providers simultaneously.                                                                         |
| Dependencies          | Provider sub-tier dependencies.                                                                                                     |
| Fault domains         | Shared upstream infrastructure across nominally diverse providers.                                                                  |
| Failure modes         | Provider outage, delayed response, contractual exit.                                                                                |
| Safeguards            | Diverse providers, contractual evidence and notification rights, exit plans.                                                        |
| Evidence              | Contracts, provider reports, route diversity evidence.                                                                              |
| AIDCF-007A families   | DEP-03, DEP-04, SUP-01, SUP-02                                                                                                      |
| Gates                 | CG-03                                                                                                                               |

# Interface contracts

**ARA-REQ-027** Every material Interface shall have a contract record with the common fields below (AIDCF-014 Interface class).

| **Field**                | **Content**                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------------|
| interfaceId and version  | Stable identifier and version.                                                                      |
| Endpoints and purpose    | The two or more endpoints (CONNECTS_TO) and the function served.                                    |
| Properties and units     | Type-specific properties (table below), with units.                                                 |
| States and transitions   | Behaviour in each operating state and on transition.                                               |
| Capacity and performance | Rated and available capacity; performance limits.                                                  |
| Authority and change rights | Party authorised to change the interface and approval required.                                  |
| Monitoring               | Telemetry observing the interface and its source health.                                           |
| Failure and safe state   | Failure modes and the defined safe state on loss.                                                  |
| Evidence                 | Evidence that the contract is met.                                                                 |
| Controls and gates       | AIDCF-007A controls and gates that depend on the interface.                                        |
| Reassessment             | Triggers that require contract review.                                                             |

**ARA-REQ-028** Each interface contract shall additionally record the type-specific properties below.

| **Interface type**    | **Type-specific properties (illustrative)**                                                         | **Typical safe state on loss**                         | **Gates**         |
|-----------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------|-------------------|
| Electrical            | Voltage, frequency, current rating, fault level, protection settings, power quality limits, ramp limits | Upstream protection isolates; downstream on alternate path | CG-05, CG-04  |
| Thermal               | Heat-transfer duty, approach temperature, supply and return temperature limits                         | Redundant unit takes duty; throttling as last resort   | CG-06             |
| Fluid                 | Flow, differential pressure, fluid composition, filtration, wetted-materials compatibility, leak detection | Isolation valves close; drainage contains leak     | CG-06, CG-04      |
| Network               | Bandwidth, latency, loss, MTU, lossless configuration, routing, isolation                              | Traffic re-routes; job pauses or restarts              | CG-08, CG-09      |
| Management            | Protocol (for example Redfish, Modbus, BACnet), authentication, authorisation, permitted commands       | Equipment holds last safe state; local control remains | CG-07, CG-15      |
| Data                  | Format, integrity check, throughput, retention, classification                                        | Writes fail closed; last verified copy retained        | CG-08, CG-10      |
| Physical              | Space, weight, access, fire separation, routes                                                         | Not applicable (structural)                            | CG-02, CG-04      |
| Operational handoff   | Responsibilities, notification times, escalation, permits                                             | Default to most restrictive party's procedure          | CG-13             |
| Provider              | Service level, notification, evidence rights, exit                                                    | Alternate provider or degraded outcome                 | CG-03             |
| Assurance             | Evidence exchanged, format, classification, timeliness                                                | Assertion becomes UNKNOWN                              | CG-11             |

# Reference patterns

**ARA-REQ-029** An architecture that matches a reference pattern shall address the distinguishing assurance concerns of that pattern in addition to the domain profiles.

| **Pattern**                       | **Distinguishing assurance concerns**                                                                                                                                         | **Mandatory views beyond the minimum** | **Typical gates**         |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|---------------------------|
| Single-site training facility     | Site-level single points of failure; correlated training load on site power; checkpoint copy location relative to the site.                                                   | State, Capacity, Failure               | CG-05, CG-06, CG-09, CG-10 |
| Dual-site capability              | True independence of sites (shared carriers, identity, staff, providers); data and checkpoint replication; failover capacity match.                                            | Dependency, Fault-domain               | CG-03, CG-09, CG-10       |
| Colocation deployment             | Division of responsibility between provider and customer; evidence access to provider systems; customer-installed liquid cooling interfacing with provider FWS.               | Dependency, Interface contracts        | CG-02, CG-03, CG-13       |
| Hyperscale campus                 | Shared campus infrastructure (substation, water, heat rejection) across buildings; scale of control planes; grid interaction of large aggregate load.                          | Dependency, Fault-domain, Capacity     | CG-03, CG-05, CG-09       |
| Modular facility                  | Factory-integrated modules with vendor controls; interfaces between modules; transport and installation risks.                                                                | System, Interface contracts            | CG-02, CG-07, CG-14       |
| Liquid-cooled high-density cluster | TCS/FWS continuity, CDU power on UPS, thermal ride-through, leak consequence, residual air heat, fluid quality.                                                               | State, Capacity, Failure, Safeguard    | CG-04, CG-06, CG-07, CG-09 |
| Hybrid cloud/on-premises          | Dependency on cloud control planes, identity and networks; data movement; consistent outcome definitions across environments.                                                  | Dependency, Digital authority          | CG-03, CG-15              |
| Sovereign AI environment          | Boundary enforcement for data, operations and support; hidden external dependencies; local continuity if external services are withdrawn.                                     | Dependency, Digital authority          | CG-02, CG-03, CG-15       |
| Shared multi-tenant platform      | Tenant isolation in compute, fabric and storage; per-tenant outcomes; shared control plane as common mode.                                                                    | Fault-domain, Digital authority        | CG-08, CG-09, CG-15       |
| Edge inference estate             | Many small sites with limited on-site staff; remote management; environmental exposure; aggregate outcome across sites.                                                        | Physical, Digital authority            | CG-07, CG-10, CG-15       |
| Brownfield retrofit               | Reconciliation of legacy as-built records; structural, power and cooling capacity for added density; integration of liquid cooling into air-cooled facilities.             | Physical, Capacity, State              | CG-02, CG-05, CG-06, CG-14 |
| Recovery-capacity pool            | Matching accelerator generation, fabric scale and storage; activation time; contention with other demands on the pool.                                                       | Capacity, Dependency                   | CG-10, CG-03              |

For every pattern: unverified shared or external reliance shall remain visible as UNKNOWN; AITG objects linked to the capability shall be handled through reviewed handoffs (AIDCF-005); and pattern-specific change, incident and evidence-expiry triggers shall be recorded.

# Architecture models

## Operating-state model

**ARA-REQ-030** Each InfrastructureSystem implementing a CRITICAL function shall record its behaviour in each operating state below, with the trigger, authority, preconditions, safeguards, expected duration, monitoring and exit criteria of each transition (AIDCF-003).

| **State**   | **Architecture must represent**                                                                                     |
|-------------|---------------------------------------------------------------------------------------------------------------------|
| NORMAL      | Approved configuration, capacity and redundancy.                                                                     |
| MAINTENANCE | Reduced-redundancy configuration, temporary bypasses, permits, duration and minimum service outcome.                 |
| DEGRADED    | Which functions and reserves are impaired and the remaining outcome.                                                 |
| EMERGENCY   | Protective actions, authority to act, and safeguards relied on (for example emergency power-off, isolation).         |
| RECOVERY    | Recovery sequence, dependencies and validation before return to NORMAL.                                              |
| TRANSITION  | Changes between architectures, control regimes or locations, including migration of workloads.                       |
| SHUTDOWN    | Intentional cessation; residual dependencies (for example cooling of batteries, fire protection).                    |
| FAILED      | Function not delivered; effect on outcomes; recovery path.                                                           |
| UNKNOWN     | How an indeterminate state is detected and handled; claims are not generalised to it.                                |

## Capacity and envelope

**ARA-REQ-031** Every capacity claim shall be a CapacityAssertion stating metric, unit, subject, operating state, environmental conditions, duration, derating assumptions, evidence date and confidence.

| **Term**   | **Definition**                                                                                   |
|------------|--------------------------------------------------------------------------------------------------|
| Demand     | Required capacity for the outcome, including transient peaks.                                   |
| Rated      | Manufacturer or design rating under stated conditions.                                          |
| Available  | Capacity actually deliverable in the stated state after derating and failures.                  |
| Reserved   | Capacity committed but not consumed.                                                            |
| Consumed   | Measured use.                                                                                   |
| Headroom   | Available minus (consumed plus reserved), per state.                                            |
| Constraint | The limiting element (for example busway rating, CDU capacity, FWS temperature).                |
| Burst      | Short-duration demand above steady state (job start, checkpoint write).                         |
| Growth     | Forecast demand change over the decision validity period.                                       |
| UNKNOWN    | Any of the above that cannot be determined, recorded as an UnknownRecord.                       |

## Fault-domain model

| **Element**          | **Definition and rule**                                                                                                    |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| FaultDomain          | Set of entities affected by a common cause; recorded with members, cause and boundary.                                     |
| Redundancy group     | Entities arranged to preserve a function; each redundancy claim names the fault domains it is intended to survive.         |
| Independence claim   | Assertion that two members do not share a fault domain; requires evidence (design, inspection, test) or is UNKNOWN.        |
| Common mode          | A shared element (controller, route, source, firmware, person) that defeats redundancy; recorded as SHARES_FAULT_DOMAIN_WITH. |
| Containment boundary | The physical, electrical, hydraulic, logical or administrative barrier that limits propagation.                             |
| Blast radius         | The outcomes and capacity lost when the fault domain fails.                                                                 |
| Recovery domain      | The set of entities restored together and in what sequence.                                                                 |

**ARA-REQ-032** Fault-domain analysis for AI clusters shall include, at minimum, the job (synchronous training), the scale-up domain, the rack, the power segment, the CDU/TCS segment, the fabric plane or rail, the storage metadata service and each control plane.

## Failure-path model

**ARA-REQ-033** Each FailureScenario shall record, in order: initiating source; pre-state; failure mode; local effect; dependency edge followed; next entity; safeguard expected to act; residual state; outcome effect against tolerance; evidence and confidence; and gate effect (AIDCF-004, AIDCF-014).

## Safeguard model

**ARA-REQ-034** Each Safeguard shall record identity, function (prevent, detect, contain, correct, recover), protected subject, activation (automatic or manual, trigger, time to act), authority, its own dependencies, state coverage, its own failure modes, evidence, and governing AIDCF-007A controls.

## Observability model

**ARA-REQ-035** Each telemetry source used as evidence shall record the metric or event, source system, subject, time base and clock source, state context, data quality and gaps, thresholds and owners, alarm route, evidence use, and known blind spots. Telemetry used for power and thermal transient claims shall have sufficient time resolution for the transient being claimed; this resolution is a capability-profile parameter.

## Evidence attachment

**ARA-REQ-036** Each material assertion shall record the evidence classes required (E1 to E7), the authoritative source, the collection method, quality and sufficiency floors, conflict handling, the UNKNOWN rule, retention and reassessment trigger, per AIDCF-008.

## Control attachment

**ARA-REQ-037** Each control attachment shall record the AIDCF-007A controlId, the subject (record identifier), applicability, claim type, assessment methods, evidence, result and confidence, findings and UNKNOWNs, gate mappings with role, and reassessment triggers.

# Critical-gate architecture

**ARA-REQ-038** For each applicable critical gate the architecture shall identify the views and evidence points that supply its evidence. Gate names are those defined in AIDCF-007A.

| **Gate** | **Name**                                          | **Architecture evidence path**                                                                                     |
|----------|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| CG-01    | Capability and outcome definition                 | Capability record, Service Outcome specifications, decision question.                                              |
| CG-02    | Boundary and architecture integrity               | Boundary record, ArchitectureSnapshot, as-built reconciliation, exclusions.                                       |
| CG-03    | Critical dependency visibility                    | Dependency graph including external providers and control planes; concentration analysis.                        |
| CG-04    | Life safety and hazardous energy                  | Physical view, fire strategy, arc-flash studies, fluid and battery hazard analysis, safe-work arrangements.       |
| CG-05    | Resilient electrical supply                       | Power system cards, capacity per state, load-dynamics analysis, transfer and load-step evidence.                  |
| CG-06    | Thermal continuity                                | Thermal system cards, liquid and air capacity per state, ride-through analysis, CDU power path.                   |
| CG-07    | Critical control-system integrity                 | BMS/EPMS and CDU control cards, fail-safe states, control narratives.                                             |
| CG-08    | Compute, storage and network functional integrity | Compute, storage and fabric cards, performance baselines, integrity evidence.                                     |
| CG-09    | Failure containment                               | Fault-domain map, containment boundaries, blast-radius analysis.                                                  |
| CG-10    | Recovery readiness                                | Recovery service chain, recovery sequence, exercise records for power, cooling, compute, storage, network, control planes. |
| CG-11    | Evidence sufficiency                              | Evidence attachment across all views.                                                                             |
| CG-12    | Critical UNKNOWN                                  | UNKNOWN register across all views.                                                                                |
| CG-13    | Responsibility and authority                      | Owners on every system card and dependency; operational handoff contracts.                                        |
| CG-14    | Change control                                    | Change rail; configuration baselines; snapshot lineage.                                                           |
| CG-15    | Integrated digital authority over infrastructure  | Digital authority view; BMC/OOB and control-plane cards; remote-support paths.                                    |

# Canonical graph nodes

**ARA-REQ-039** Graph projections of the architecture shall use the AIDCF-014 classes. The principal node classes produced by this architecture are:

| **Class**            | **Produced by**                                 |
|----------------------|-------------------------------------------------|
| CapabilityInstance   | Capability record                               |
| ServiceOutcome       | Service Outcome specification                   |
| RequiredFunction     | Service chains                                  |
| ArchitectureSnapshot | Published architecture baseline                 |
| InfrastructureSystem | System cards                                    |
| AssetInstance        | Asset records                                   |
| Interface            | Interface contracts                             |
| Resource             | Capacity model                                  |
| CapacityAssertion    | Capacity model                                  |
| Dependency           | Dependency view                                 |
| FaultDomain          | Fault-domain model                              |
| OperatingState       | Operating-state model                           |
| FailureScenario      | Failure-path model                              |
| Safeguard            | Safeguard model                                 |
| EvidenceObject       | Evidence attachment                             |
| ControlAssessment    | Control attachment                              |
| GateResult           | Critical-gate architecture                      |
| AssuranceDecision    | Decision view                                   |

Every node carries the AIDCF-014 common envelope (stable ID, version, source, status, classification).

# Canonical graph relationships

**ARA-REQ-040** Edges shall use the AIDCF-014 relationship types and envelope (directed, scoped, versioned, reviewed and evidence-linked). The types most used in architecture views are HAS_OUTCOME, REQUIRES_FUNCTION, IMPLEMENTED_BY, COMPOSED_OF, CONNECTS_TO, CONSUMES_RESOURCE, DEPENDS_ON, SHARES_FAULT_DOMAIN_WITH, LOCATED_IN, OPERATED_BY, CONTROLLED_BY, MONITORED_BY, PROTECTED_BY, EXPOSED_TO, INITIATES, PROPAGATES_TO, RECOVERS_THROUGH, GOVERNED_BY, EVIDENCED_BY, ASSESSED_BY, EVALUATES_GATE, CONSTRAINS, REPORTED_IN, SUPERSEDES and INTEGRATION_HANDOFF.

**Alias note.** AIDCF-013 v1.0 used non-canonical names. They are deprecated and shall be migrated as follows: SUPPORTS_OUTCOME becomes IMPLEMENTED_BY in the reverse direction (Function IMPLEMENTED_BY System), with outcome links expressed by HAS_OUTCOME and REQUIRES_FUNCTION; IMPLEMENTS becomes IMPLEMENTED_BY (reversed); CONSTRAINS_GATE and LIMITS_DECISION become CONSTRAINS; PROTECTS becomes PROTECTED_BY (reversed).

# Graph validation rules

| **ID**    | **Rule**                                                                                                         |
|-----------|------------------------------------------------------------------------------------------------------------------|
| ARA-GV-01 | Every node has a stable ID, version and lineage to its source.                                                   |
| ARA-GV-02 | Every CapabilityInstance has at least one HAS_OUTCOME.                                                           |
| ARA-GV-03 | Every ServiceOutcome has REQUIRES_FUNCTION, and every RequiredFunction has IMPLEMENTED_BY.                       |
| ARA-GV-04 | Every DEPENDS_ON references a Dependency record with direction, conditions and evidence, or an UnknownRecord.   |
| ARA-GV-05 | Every redundancy claim links its fault domains and independence evidence.                                       |
| ARA-GV-06 | Every FailureScenario includes pre-state, propagation path, safeguards and outcome effect.                      |
| ARA-GV-07 | Every control attachment links a subject and evidence or UNKNOWN.                                               |
| ARA-GV-08 | Every GateResult links its CRITICAL control assessments and mandatory evidence.                                 |
| ARA-GV-09 | Every AssuranceDecision links scope, gates, UNKNOWNs, validity and authority.                                   |
| ARA-GV-10 | Inferred edges remain CANDIDATE until reviewed.                                                                 |
| ARA-GV-11 | CONNECTS_TO is never treated as DEPENDS_ON, causality, reachability or authority.                               |
| ARA-GV-12 | AIDCF and AITG conclusions remain separate; links only via INTEGRATION_HANDOFF.                                  |
| ARA-GV-13 | Sensitive paths (OT, BMC/OOB, protection settings) are classified and access-controlled.                         |
| ARA-GV-14 | Supersession preserves prior snapshots unchanged.                                                               |

**ARA-REQ-041** Architecture graphs claiming AR5 or above shall pass rules ARA-GV-01 to ARA-GV-14.

# Required work products

**ARA-REQ-042** The assessment architecture shall include each work product whose trigger applies; omissions require an approved rationale.

| **Work product**             | **Content**                                                                         | **Triggered when**                       |
|------------------------------|-------------------------------------------------------------------------------------|------------------------------------------|
| Capability Context Diagram   | Capability, users, outcomes, boundary, external providers.                          | Always.                                  |
| Service Chain Map            | Functions in order, with implementing systems.                                      | Always.                                  |
| System Decomposition         | Systems, assets, interfaces (COMPOSED_OF, IMPLEMENTED_BY).                          | Always.                                  |
| Power Assurance View         | Single-line, capacity per state, load dynamics, transfer sequence.                  | Power in scope.                          |
| Thermal/Fluid Assurance View | FWS, CDU, TCS and air paths, capacity per state, ride-through, CDU power path.      | Cooling in scope.                        |
| Compute/Storage/Network View | Clusters, scale-up domains, fabrics, storage tiers, control planes.                 | IT infrastructure in scope.              |
| Dependency Graph             | All material dependencies including external and recovery dependencies.             | Always.                                  |
| Fault-Domain Map             | Fault domains, redundancy groups, common modes, blast radius.                       | Any redundancy or containment claim.     |
| Operating-State Matrix       | Behaviour of each critical system in each state.                                    | Always.                                  |
| Capacity Model               | CapacityAssertions per resource and state.                                          | Any capacity outcome.                    |
| Failure Map                  | Scenarios and propagation paths.                                                    | Always.                                  |
| Safeguard Map                | Safeguards linked to scenarios and controls.                                        | Always.                                  |
| Digital Authority Map        | Identities, control planes, management paths, remote support, automation.           | Networked control or BMC/OOB in scope.   |
| Control/Evidence Matrix      | Controls, subjects, evidence requirements and evidence points.                      | Always.                                  |
| Critical-Gate Map            | Gate evidence paths and CRITICAL controls.                                          | Always.                                  |
| Decision Lineage View        | Decision to gates, UNKNOWNs, scores and approvals.                                  | A decision is issued.                    |
| AITG Handoff Package         | Reviewed handoff records.                                                           | AITG integration in scope.               |

# Templates

Templates are the minimum content of architecture records. They are serialised as AIDCF-014 records (common envelope plus the fields below) using the AIDCF-016 schemas.

| **Template**        | **Fields beyond the common envelope**                                                                                 |
|---------------------|-----------------------------------------------------------------------------------------------------------------------|
| Capability Record   | owner, lifecycle, workload, outcomes, demand, criticality, architectureBaseline, scope, reassessmentTriggers          |
| Outcome Record      | outcomeType, statement, conditions, tolerance, functions, dependencies, safeguards, evidenceFloor, gates, owner       |
| System Record       | purpose, systemType, components, interfaces, capacity, states, dependencies, faultDomains, owners, evidence, rails   |
| Asset Record        | assetClass, location, configuration, state, system, owner, lifecycle, evidence                                        |
| Interface Record    | interfaceType, endpoints, purpose, typeProperties, capacity, authority, monitoring, safeState, evidence                |
| Dependency Record   | source, target, dependencyType, strength, conditions, criticality, substitutability, sharedMode, evidence, confidence |
| FaultDomain Record  | members, commonCause, boundary, blastRadius, safeguards, evidence                                                     |
| Scenario Record     | preState, initiatingSource, steps, safeguards, residualState, outcomeEffect, evidence, confidence                     |
| Safeguard Record    | function, subject, activation, authority, dependencies, states, failureModes, controls, evidence                     |
| Assertion Record    | subject, predicate, value, unit, conditions, evidence, unknownRef, reviewer, reviewState                              |
| Snapshot Record     | capability, scope, sourceVersions, members, validation, approval, supersedes                                          |

# Architecture workflows

**ARA-REQ-043** Each architecture workflow shall start from an authorised decision question and named owner, produce versioned architecture records with evidence and ValidationResults, preserve unresolved facts as UNKNOWN, include architecture, technical, evidence and (where required) independent review, and stop if continuing would require an unsafe action, unresolved authority, compromised source integrity or absent competence.

| **Workflow**          | **Steps**                                                                                                                                  | **Specific outputs**                                                     |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| New capability        | Need → outcomes → boundary → service chains → systems → dependencies → states and capacity → scenarios → assurance attachment → review.    | Capability record, first ArchitectureSnapshot, gate evidence plan.       |
| Existing facility     | Baseline documents → reconcile to as-built and telemetry → discover undocumented dependencies → record UNKNOWNs → map → validate → gates → snapshot. | Reconciliation report, UNKNOWN register, ArchitectureSnapshot.     |
| Material change       | Detect → impact analysis (AIDCF-014 §22) → suspend affected claims → update records → reassess → supersede snapshot.                       | Impact analysis, superseding snapshot, reassessment results.             |
| Incident              | Reconstruct failure path → identify affected claims and gates → record residual state → collect recovery evidence → reassess.             | Scenario record from the event, findings, updated safeguards.            |
| Continuing assurance  | Register telemetry and change sources → detect drift → human triage → reassess → update records.                                            | Event records, triggered reassessments.                                  |
| AITG integration      | Validate identifiers → establish reviewed shared identity → create handoff → check lineage and classification → federate.                  | IntegrationHandoff records.                                              |

# Synthetic examples

The examples are illustrative and synthetic. They are not real designs, sites or conclusions.

| **Example**          | **Context**                                                                                                                    | **Architecture treatment**                                                                                                        | **Likely gate effect**                                                                                 |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Training cluster     | Two CDUs serving a liquid-cooled row are presented as N+1, but both are commanded by one BMS controller and their pumps are on mechanical (non-UPS) power. | Model SHARES_FAULT_DOMAIN_WITH via the controller; record the CDU power path; build the utility-loss scenario with thermal ride-through versus generator start and transfer time. | CG-06 and CG-09 cannot PASS on the N+1 claim; CG-07 depends on controller fail-safe evidence; the decision is bounded by the AIDCF-010 ceilings for the affected gates until resolved. |
| Colocation           | Customer accelerators depend on provider power, FWS and operations; provider evidence is available only as summaries.          | Separate provider and customer boundaries; operational handoff and provider interface contracts; restricted evidence recorded with quality limits. | CG-03 and CG-11 may be UNKNOWN if provider evidence is below floor; recorded as US4 where gate-critical. |
| Dual-site recovery   | Two sites are presented as independent but share a telecom carrier entrance route and a single identity provider.             | Model shared recovery dependencies; recovery service chain with identity restoration; exercise records.                             | CG-03 and CG-10 limited by the common modes; independence claim QUALIFIED.                              |
| Brownfield retrofit  | Liquid-cooled racks added to a legacy air-cooled hall with existing busway and chilled water.                                   | Reconcile as-built capacity; CapacityAssertions for busway, FWS temperature and residual air heat; change records.                  | CG-02, CG-05, CG-06 and CG-14 evaluated against reconciled capacity; gaps UNKNOWN.                      |

# Conformance validation

| **ID**      | **Validation**                                                         | **Requirements verified**            |
|-------------|------------------------------------------------------------------------|--------------------------------------|
| ARA-VAL-001 | Capability and outcomes explicit and approved.                         | ARA-REQ-020, ARA-REQ-022         |
| ARA-VAL-002 | Functions stated before products.                                      | ARA-REQ-006, ARA-REQ-002    |
| ARA-VAL-003 | Scope and external dependencies visible.                               | ARA-REQ-008, ARA-REQ-019         |
| ARA-VAL-004 | Stable identifiers.                                                    | ARA-REQ-039                             |
| ARA-VAL-005 | States and transitions represented.                                    | ARA-REQ-009, ARA-REQ-030       |
| ARA-VAL-006 | Capacity claims conditioned and evidenced.                             | ARA-REQ-031, ARA-REQ-021            |
| ARA-VAL-007 | Fault domains and common modes mapped, including AI-specific domains.  | ARA-REQ-011, ARA-REQ-032             |
| ARA-VAL-008 | Dependencies evidenced or UNKNOWN.                                     | ARA-REQ-008                         |
| ARA-VAL-009 | Failure paths link safeguards and outcomes.                            | ARA-REQ-033, ARA-REQ-034                   |
| ARA-VAL-010 | Controls attach to subjects using AIDCF-007A families.                 | ARA-REQ-037, ARA-REQ-025         |
| ARA-VAL-011 | Evidence attaches to assertions.                                       | ARA-REQ-036                         |
| ARA-VAL-012 | Gates separate from scores; gate evidence paths identified.            | ARA-REQ-038                        |
| ARA-VAL-013 | Decision lineage complete.                                             | ARA-REQ-041                             |
| ARA-VAL-014 | Canonical relationship vocabulary; AIDCF/AITG semantics separate.      | ARA-REQ-040                             |
| ARA-VAL-015 | Sensitive paths controlled.                                            | ARA-REQ-018                      |
| ARA-VAL-016 | Automation cannot approve facts.                                       | ARA-REQ-014                       |
| ARA-VAL-017 | Snapshots immutable and superseded with lineage.                       | ARA-REQ-041                             |
| ARA-VAL-018 | Safety and engineering boundaries preserved.                           | ARA-REQ-001                       |
| ARA-VAL-019 | All five rails populated for critical systems.                         | ARA-REQ-016, ARA-REQ-017       |

# Review and release gates

All reviews and pilots below are pending. No review, pilot or independent assessment of this architecture has been completed.

| **Reviewer or pilot**                | **Status** |
|--------------------------------------|------------|
| Methodology author                   | Pending    |
| Data-centre architect                | Pending    |
| Electrical engineer                  | Pending    |
| Mechanical and liquid-cooling engineer | Pending  |
| AI/HPC architect                     | Pending    |
| Storage architect                    | Pending    |
| Network architect                    | Pending    |
| Operations and reliability           | Pending    |
| OT and security                      | Pending    |
| Evidence specialist                  | Pending    |
| Ontology and graph engineer          | Pending    |
| Safety, legal and privacy            | Pending    |
| Colocation pilot                     | Pending    |
| High-density cooling pilot           | Pending    |
| Hybrid and sovereign pilot           | Pending    |
| AITG pilot                           | Pending    |
| Public release                       | Pending    |

## Final architecture doctrine

**AIDCF-013 makes the assurance subject and its dependencies explicit. It is not a vendor design, equipment checklist or substitute for licensed engineering. Where architecture or evidence is incomplete, AIDCF preserves UNKNOWN and limits assurance.**
