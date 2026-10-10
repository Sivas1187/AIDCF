# AIDCF-007A Control Catalogue — CMP AI Compute Infrastructure

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-CMP](../../../aidcf-018-domain-guides/AIDCF-018-CMP_AI_Compute_Infrastructure_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-CMP-001](#mcf-cmp-001) | Accelerator Architecture | DIRECTIVE | DESIGN | AL2 | — | CG-08, CG-01 |
| [MCF-CMP-002](#mcf-cmp-002) | Node Configuration | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-08, CG-15 |
| [MCF-CMP-003](#mcf-cmp-003) | Rack-Scale Composition | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-08, CG-06, CG-05 |
| [MCF-CMP-004](#mcf-cmp-004) | Approved Baseline | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-02, CG-08, CG-14 |
| [MCF-CMP-005](#mcf-cmp-005) | Cluster Topology | DIRECTIVE | DESIGN | AL2 | — | CG-08, CG-02 |
| [MCF-CMP-006](#mcf-cmp-006) | Scale-Up Domain Integrity | DETECTIVE | EFFECTIVENESS | AL5 | CG-08 | CG-09 |
| [MCF-CMP-007](#mcf-cmp-007) | Partitioning | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-09, CG-15 |
| [MCF-CMP-008](#mcf-cmp-008) | Fault-Domain Design | PREVENTIVE | RESILIENCE | AL5 | CG-09 | CG-08, CG-03 |
| [MCF-CMP-009](#mcf-cmp-009) | Usable Accelerator Capacity | DETECTIVE | OPERATION | AL4 | CG-08 | CG-01 |
| [MCF-CMP-010](#mcf-cmp-010) | Scheduler Controls | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-08, CG-15 |
| [MCF-CMP-011](#mcf-cmp-011) | Resource Reservation | PREVENTIVE | OPERATION | AL4 | — | CG-10, CG-08 |
| [MCF-CMP-012](#mcf-cmp-012) | Contention Management | CORRECTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-CMP-013](#mcf-cmp-013) | Firmware Baseline | PREVENTIVE | IMPLEMENTATION | AL3 | CG-08 | CG-14, CG-15 |
| [MCF-CMP-014](#mcf-cmp-014) | Driver Compatibility | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-08 |
| [MCF-CMP-015](#mcf-cmp-015) | Upgrade Testing | PREVENTIVE | EFFECTIVENESS | AL5 | CG-14 | CG-09, CG-08 |
| [MCF-CMP-016](#mcf-cmp-016) | Rollback Readiness | RECOVERY | RESILIENCE | AL5 | — | CG-10, CG-14 |
| [MCF-CMP-017](#mcf-cmp-017) | GPU Telemetry | DETECTIVE | OPERATION | AL4 | — | CG-08, CG-06 |
| [MCF-CMP-018](#mcf-cmp-018) | Node Health | DETECTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-CMP-019](#mcf-cmp-019) | Error and Degradation Detection | DETECTIVE | EFFECTIVENESS | AL5 | CG-08 | — |
| [MCF-CMP-020](#mcf-cmp-020) | Performance Baselines | DETECTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-CMP-021](#mcf-cmp-021) | Provisioning | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-08, CG-14 |
| [MCF-CMP-022](#mcf-cmp-022) | Spares and RMA | CORRECTIVE | OPERATION | AL4 | — | CG-10, CG-03 |
| [MCF-CMP-023](#mcf-cmp-023) | Node Rebuild | RECOVERY | RESILIENCE | AL5 | CG-10 | CG-08 |
| [MCF-CMP-024](#mcf-cmp-024) | Secure Retirement | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-02 |

## CMP-01 Compute architecture and configuration

### MCF-CMP-001

**Accelerator Architecture** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Establish a documented, approved accelerator architecture that links the Capability Instance's workload (training, fine-tuning, inference) to the accelerator type, memory capacity and bandwidth, scale-up domain size, scale-out fabric, power and cooling envelope, so that compute is sized and constrained by the Service Outcome rather than by procurement availability.

**Requirement.** The compute engineering authority shall maintain an accelerator architecture record per cluster stating accelerator model and generation, accelerator memory capacity and bandwidth, scale-up domain size and interconnect, host CPU and memory ratio, scale-out network attachment per accelerator, per-node and per-rack power and heat, and the cooling method required. The AI platform owner shall approve the record and shall confirm its sufficiency against the performance and integrity outcomes defined for the Capability Instance.

**Assessment criteria**

1. An approved architecture record exists per cluster with the attributes listed in the requirement.
2. Each attribute traces to a workload requirement (model size, parallelism strategy, sequence length, throughput or latency target).
3. Power and heat per rack in the record reconcile with the facility heat-load model (MCF-THM-001) and power budget.
4. Scale-up and scale-out attachment ratios are stated and match the fabric design (NET-01).
5. Mixed-generation or heterogeneous accelerators, where present, are identified with their scheduling constraints.
6. Known platform limitations and OEM errata relevant to the outcome are recorded.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Accelerators per scale-up domain | count | platform-specific (illustrative: 8 node-scale; 72 rack-scale) | Platform OEM architecture |
| Scale-out bandwidth per accelerator | Gb/s | 400 (illustrative) | Fabric design; platform OEM reference architecture |
| Rack power envelope | kW | 120 (illustrative) | Platform OEM data; facility power budget |

**Minimum evidence**

- Approved accelerator architecture record
- Workload requirement statement linked to the Service Outcome
- OEM reference architecture or design guide
- Reconciliation with facility power and heat budgets

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; TRANSITION |
| periodCoverage | Current record version |
| independence | Review by an architect not responsible for procurement |
| mandatoryItems | Architecture record; Workload requirement linkage |
| acceptableAlternatives | OEM reference architecture adopted with documented site deviations |
| unknownEffect | US3 Material: compute sufficiency for outcome unverified; CG-08 supporting evaluation |
| reassessmentTriggers | New accelerator generation; Change of workload class; Change of scale-up domain size |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INQUIRY, RECONCILIATION

**Assessment procedure**

1. Obtain the architecture record and workload statement.
2. Trace each attribute to a workload requirement.
3. Reconcile rack power and heat with facility budgets.
4. Check consistency with fabric design.
5. Record untraced attributes as Findings and missing workload inputs as UNKNOWN Records.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-01 Capability and outcome definition (SUPPORTING)

**Applicability.** Applies to every in-scope accelerator cluster, owned or provider-operated. For cloud capacity consumed as a service, applies to the provider's documented architecture to the extent the service interface discloses it, with residual items recorded as UNKNOWN.

**Lifecycle stages.** PLAN, DESIGN, CHANGE · **Operating states.** NORMAL, TRANSITION

**Failure modes addressed.** Accelerator memory insufficient for model/parallelism plan; Scale-up domain smaller than tensor-parallel group; Rack power exceeding facility budget; Undeclared heterogeneous fleet

**Testing safety.** Desk-based review; no system access needed.

**UNKNOWN rule.** If workload requirements are not defined, record a U1 UNKNOWN linked to CG-01; architecture sufficiency cannot be judged.

**Ontology classes.** InfrastructureSystem, ArchitectureSnapshot, CapacityAssertion, RequiredFunction · **Related controls.** MCF-CMP-003, MCF-CMP-005, MCF-THM-001, MCF-NET-001

**Informative references.** AIDCF-013 (AI Data Centre Assurance Reference Architecture); MLCommons MLPerf Training and Inference benchmark rules; Open Compute Project hardware management and fault-management specifications

### MCF-CMP-002

**Node Configuration** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure each compute node's hardware and low-level configuration (BIOS/UEFI settings, BMC configuration, PCIe topology, NUMA and accelerator affinity, NIC attachment, power and thermal limits) matches the approved node specification, because silent configuration drift degrades performance and reliability of collective workloads.

**Requirement.** The AI platform operator shall define a node configuration specification per node type and shall verify, at provisioning and at a defined interval, that every node conforms, using automated collection from the BMC (for example via Redfish) and host OS. The AI platform operator shall secure BMC interfaces with unique credentials, management-network isolation and logged access.

**Assessment criteria**

1. A node configuration specification exists per node type covering BIOS/UEFI, BMC, PCIe/NUMA topology, accelerator power limits and NIC mapping.
2. Automated conformance collection covers ≥ the declared percentage of nodes and runs at the declared interval.
3. Nonconforming nodes are quarantined or remediated within the declared time.
4. BMCs use unique credentials, are reachable only from the management network, and access is logged.
5. Accelerator power and clock limits set in configuration match the facility power and thermal envelope.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Configuration conformance coverage | % of nodes | 100 (illustrative) | Capability profile |
| Conformance scan interval | days | 7 (illustrative) | Capability profile |
| Nonconforming node remediation time | days | 3 (illustrative) | Capability profile |

**Minimum evidence**

- Node configuration specification
- Automated conformance report (per-node)
- Quarantine/remediation records
- BMC credential and network-isolation configuration
- BMC access logs

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Most recent 3 conformance scans |
| independence | Assessor re-runs collection on a sample of nodes |
| mandatoryItems | Configuration specification; Per-node conformance report |
| acceptableAlternatives | Manual sample inspection where automation coverage is below target, with sample sized per AIDCF-009 |
| unknownEffect | US3 Material: node configuration drift possible; CG-08 supporting |
| reassessmentTriggers | New node type; BIOS/BMC update; Conformance coverage below target |

**Assessment methods.** RECONCILIATION, SAMPLING, REPERFORMANCE, INSPECTION

**Assessment procedure**

1. Obtain specification and latest conformance reports.
2. Reperform collection on a sample of nodes.
3. Check remediation of nonconforming nodes.
4. Review BMC isolation and access logs.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to all in-scope compute nodes. For provider-managed nodes, applies to the evidence the provider supplies under its service obligations.

**Lifecycle stages.** BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** NUMA/PCIe misaffinity degrading bandwidth; Accelerator power limit above rack budget; Default BMC credentials; Configuration drift after RMA

**Testing safety.** Read-only collection; no configuration changes by the assessor. BMC access uses a read-only account authorised by the operator.

**UNKNOWN rule.** If conformance collection covers less than the target population, record U5 coverage-gap UNKNOWN for the uncovered nodes.

**Ontology classes.** AssetInstance, ArchitectureSnapshot, Interface · **Related controls.** MCF-CMP-004, MCF-CMP-013, MCF-SEC-003, MCF-NET-013

**Informative references.** DMTF Redfish (platform management API); NIST SP 800-128 (security-focused configuration management); NIST SP 800-147B (BIOS protection guidelines for servers)

### MCF-CMP-003

**Rack-Scale Composition** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure rack-scale systems (integrated compute trays, scale-up switch trays, power shelves, busbars, liquid manifolds) are composed, connected and accepted as a unit, with their facility interfaces (power, liquid, network, weight) verified against the facility design.

**Requirement.** The AI platform operator shall maintain a rack-scale composition record for each rack type (trays, switch trays, power shelves, manifold and QD layout, cable/backplane mapping) and shall verify each installed rack at acceptance. The facility operator and AI platform operator shall jointly sign the facility interface checklist covering power feeds, liquid connections and flow, floor loading and network uplinks before energisation.

**Assessment criteria**

1. A composition record exists per rack type and matches OEM configuration.
2. Each installed rack has an acceptance record including tray inventory and scale-up interconnect validation.
3. A joint facility interface checklist (power, liquid, structural, network) is signed before energisation.
4. Rack power shelf redundancy and feed assignment match the electrical design.
5. Rack weight and point loads are within the floor or slab rating.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Rack weight | kg | platform-specific (illustrative 1,500) | Platform OEM data; structural rating |

**Minimum evidence**

- Rack composition record
- Per-rack acceptance records
- Joint facility interface checklists
- Power feed assignment register
- Structural load check

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; TRANSITION |
| periodCoverage | All racks accepted in the last 12 months (sampled) |
| independence | Joint sign-off by facility and platform teams |
| mandatoryItems | Composition record; Signed interface checklists |
| acceptableAlternatives | OEM factory integration report plus site interface verification |
| unknownEffect | US3 Material: facility interface conformance uncertain; CG-06 and CG-05 supporting |
| reassessmentTriggers | New rack type; Rack relocation; Power shelf change |

**Assessment methods.** INSPECTION, DOCUMENT_REVIEW, RECONCILIATION, SAMPLING

**Assessment procedure**

1. Sample racks and obtain acceptance records.
2. Inspect rack against composition record.
3. Review signed interface checklists.
4. Reconcile feed assignments with the electrical design.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-06 Thermal continuity (SUPPORTING); CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies to integrated rack-scale systems and to conventional racks with liquid or high-power facility interfaces.

**Lifecycle stages.** BUILD, COMMISSION, CHANGE · **Operating states.** NORMAL, TRANSITION

**Failure modes addressed.** Both power shelves fed from same upstream source; Manifold connected without flow verification; Tray missing or mis-slotted; Floor overload

**Testing safety.** Inspection of energised racks follows the site electrical safety rules; assessors do not open trays or power shelves.

**UNKNOWN rule.** If no joint interface checklist exists for a rack, record U1 UNKNOWN and reference the corresponding THM and POW controls.

**Ontology classes.** AssetInstance, Interface, InfrastructureSystem · **Related controls.** MCF-CMP-001, MCF-THM-009, MCF-THM-012, MCF-PHY-006

**Informative references.** AIDCF-013 (AI Data Centre Assurance Reference Architecture); Open Compute Project hardware management and fault-management specifications; IEC 62368-1 (audio/video, information and communication technology equipment safety)

### MCF-CMP-004

**Approved Baseline** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Maintain a single, approved, version-controlled compute baseline (hardware bill of materials, firmware set, driver and runtime stack, OS image, configuration) against which every node can be reconciled and every change can be measured.

**Requirement.** The AI platform operator shall publish an approved compute baseline per node type that enumerates hardware components, firmware versions, driver and runtime versions, OS image hash and configuration profile, shall approve changes to it under change control, and shall reconcile the deployed fleet to it continuously, reporting the fraction of nodes on the current baseline.

**Assessment criteria**

1. An approved baseline exists per node type with versioned components and image hashes.
2. Baseline changes have change records with approval.
3. Fleet reconciliation reports show the fraction of nodes on the current baseline and the age of exceptions.
4. Exceptions are approved with expiry dates.
5. The baseline is linked to the Capability Instance's architecture snapshot.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Fleet on current baseline | % of nodes | 98 (illustrative) | Capability profile |
| Maximum exception age | days | 30 (illustrative) | Capability profile |

**Minimum evidence**

- Approved baseline manifest
- Change records for baseline updates
- Fleet reconciliation report
- Exception register

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; TRANSITION |
| periodCoverage | Current baseline and 3 months of reconciliation |
| independence | Assessor reconciliation of a node sample against the manifest |
| mandatoryItems | Baseline manifest; Fleet reconciliation report |
| acceptableAlternatives | Configuration management database export with per-node attributes |
| unknownEffect | US3 Material: as-built state uncertain; CG-02 supporting |
| reassessmentTriggers | Baseline change; Reconciliation below target; Emergency change |

**Assessment methods.** RECONCILIATION, DOCUMENT_REVIEW, SAMPLING

**Assessment procedure**

1. Obtain baseline manifest and change history.
2. Reconcile node sample to manifest.
3. Review exceptions and their expiry.
4. Link baseline to architecture snapshot.

**Gate mappings.** CG-02 Boundary and architecture integrity (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all in-scope compute fleets.

**Lifecycle stages.** BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, TRANSITION

**Failure modes addressed.** Untracked component substitution; Mixed images across a training partition; Expired exceptions persisting

**Testing safety.** Read-only reconciliation.

**UNKNOWN rule.** If no approved baseline exists, record U1 UNKNOWN against this control and against MCF-CMP-013/014.

**Ontology classes.** ArchitectureSnapshot, AssetInstance, InfrastructureSystem · **Related controls.** MCF-CMP-013, MCF-CMP-014, MCF-OPS-017, MCF-SUP-012

**Informative references.** NIST SP 800-128 (security-focused configuration management); ISO/IEC 19770 series (IT asset management); ISO/IEC 20000-1 (service management system requirements)

## CMP-02 Cluster and scale-up domains

### MCF-CMP-005

**Cluster Topology** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Document the cluster topology (nodes, scale-up domains, scale-out rails, storage attachment, management plane) so that job placement, failure analysis and capacity statements can be reasoned about against physical and logical locality.

**Requirement.** The AI platform operator shall maintain a machine-readable cluster topology describing node-to-scale-up-domain membership, node-to-rail and leaf mapping, rack, power and cooling domain of every node, and storage and management attachment. The compute engineering authority shall reconcile the topology with the fabric (NET-01) and facility models at each change.

**Assessment criteria**

1. A machine-readable topology exists and covers all in-scope nodes.
2. Each node's scale-up domain, fabric rail/leaf, rack, power feed group and cooling loop are recorded.
3. Topology reconciles with fabric and facility records for a sample.
4. The scheduler's topology view matches the documented topology.
5. Topology version is linked to the architecture snapshot.

**Minimum evidence**

- Machine-readable topology export
- Reconciliation report against fabric and facility models
- Scheduler topology configuration

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E2; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; TRANSITION |
| periodCoverage | Current version |
| independence | Reconciliation performed by assessor against independent sources (fabric LLDP, facility asset register) |
| mandatoryItems | Topology export; Reconciliation report |
| acceptableAlternatives | Generated topology from fabric discovery plus manual mapping to facility domains |
| unknownEffect | US3 Material: placement and failure analysis uncertain; CG-02 supporting |
| reassessmentTriggers | Cluster expansion; Rack move; Fabric recabling |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Obtain topology export.
2. Reconcile a sample against fabric discovery and facility registers.
3. Compare with scheduler topology.
4. Record mismatches.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-02 Boundary and architecture integrity (SUPPORTING)

**Applicability.** Applies to all multi-node accelerator clusters.

**Lifecycle stages.** DESIGN, BUILD, CHANGE · **Operating states.** NORMAL, TRANSITION

**Failure modes addressed.** Scheduler unaware of rack/power domains; Topology stale after expansion; Rail mis-mapping

**Testing safety.** Desk-based; read-only exports.

**UNKNOWN rule.** Nodes absent from the topology are recorded as U5 coverage-gap UNKNOWN.

**Ontology classes.** ArchitectureSnapshot, InfrastructureSystem, FaultDomain · **Related controls.** MCF-CMP-008, MCF-CMP-010, MCF-NET-001, MCF-NET-004

**Informative references.** AIDCF-013 (AI Data Centre Assurance Reference Architecture); Open Compute Project hardware management and fault-management specifications

### MCF-CMP-006

**Scale-Up Domain Integrity** · DETECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure each scale-up domain (the accelerator group joined by the high-bandwidth, low-latency interconnect, from a single node to a rack-scale domain) delivers its rated bandwidth with all links and switches healthy, and that a degraded domain is detected and withdrawn before it slows or corrupts a training job.

**Requirement.** The AI platform operator shall validate every scale-up domain at acceptance and at a defined interval by running an all-to-all or all-reduce bandwidth test against the platform's rated performance, shall monitor interconnect link errors, retrains and lane degradation continuously, and shall automatically drain domains that fall below the declared bandwidth threshold or exceed the link-error threshold.

**Assessment criteria**

1. Acceptance bandwidth tests for each scale-up domain meet the declared fraction of rated bandwidth.
2. Periodic re-validation runs at the declared interval with results recorded.
3. Link error, retrain and lane-width telemetry is collected for every domain.
4. Drain automation triggers on threshold breach and has been observed to work (test or real event).
5. Domains returned to service after repair pass the bandwidth test.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Minimum scale-up bandwidth | % of rated all-reduce bandwidth | 90 (illustrative) | Platform OEM performance data; capability profile |
| Re-validation interval | days | 30 (illustrative) | Capability profile |
| Link-error drain threshold | errors per hour per link | platform-specific | Platform OEM RAS guidance |

**Minimum evidence**

- Acceptance bandwidth test results per domain
- Periodic re-validation results
- Link-error telemetry
- Drain automation configuration and event log
- Return-to-service test results

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C3 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; RECOVERY |
| periodCoverage | 3 months of telemetry and the last re-validation cycle |
| independence | Assessor re-runs the bandwidth test on a sample of domains |
| mandatoryItems | Bandwidth test results; Drain event log |
| acceptableAlternatives | Vendor diagnostic suite results that include equivalent bandwidth tests |
| unknownEffect | US4 Critical: CG-08 UNKNOWN for training outcomes relying on unvalidated scale-up domains |
| reassessmentTriggers | Interconnect firmware change; Switch tray replacement; Rise in link errors |

**Assessment methods.** TEST, REPERFORMANCE, ANALYSIS, SAMPLING

**Assessment procedure**

1. Sample scale-up domains across racks.
2. Review acceptance and periodic test results.
3. Reperform the bandwidth test on idle sampled domains.
4. Analyse link-error telemetry and drain events.
5. Check return-to-service evidence.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (CRITICAL); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to all accelerator platforms with a scale-up interconnect. For single-accelerator nodes with no scale-up domain, record NOT_APPLICABLE with rationale.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, RECOVERY

**Failure modes addressed.** Degraded lane width halving bandwidth; Switch tray fault isolating part of domain; Intermittent link errors causing job hangs; Domain returned to service without retest

**Testing safety.** Bandwidth tests run only on drained domains with operator authorisation. Draining nodes or partitions removes capacity from production jobs; the AI platform operator's change authority and job-owner notification are required.

**UNKNOWN rule.** If no re-validation within interval exists for a domain, record U3 stale UNKNOWN for that domain.

**Ontology classes.** FaultDomain, InfrastructureSystem, TestRecord, FailureMode · **Related controls.** MCF-CMP-005, MCF-CMP-019, MCF-CMP-023, MCF-NET-008

**Informative references.** Open Compute Project hardware management and fault-management specifications; MLCommons MLPerf Training and Inference benchmark rules; PCI Express Base Specification (Advanced Error Reporting)

### MCF-CMP-007

**Partitioning** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure logical partitions of the cluster (tenant, project, production versus test, accelerator partitioning such as multi-instance modes) are enforced so that one partition's jobs, faults or administrators cannot consume, disrupt or read another's resources.

**Requirement.** The AI platform operator shall define partitions with membership, quotas, network and storage isolation, and administrator scope, shall enforce them in the scheduler, fabric and storage configuration, and shall verify enforcement after each change. Where accelerator-level partitioning is used, the AI platform operator shall document its isolation properties as stated by the OEM.

**Assessment criteria**

1. Partition definitions exist with membership, quotas and admin scope.
2. Scheduler configuration enforces partition boundaries (verified by configuration review and a negative test).
3. Network and storage isolation for each partition is configured and reconciled.
4. Accelerator-level partition isolation properties are documented from OEM sources.
5. Partition changes have change records and post-change verification.

**Minimum evidence**

- Partition definitions
- Scheduler, fabric and storage configuration exports
- Negative test record (job cannot use other partition's nodes)
- OEM isolation documentation

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Current configuration |
| independence | Assessor-designed negative test |
| mandatoryItems | Configuration exports; Negative test |
| acceptableAlternatives | Policy-as-code repository with automated tests |
| unknownEffect | US3 Material: isolation uncertain; CG-09 and CG-15 supporting |
| reassessmentTriggers | New tenant; Scheduler upgrade; Partition change |

**Assessment methods.** RECONCILIATION, TEST, DOCUMENT_REVIEW

**Assessment procedure**

1. Obtain definitions and configurations.
2. Reconcile across scheduler, fabric and storage.
3. Run or review the negative test.
4. Review OEM isolation statements.

**Gate mappings.** CG-09 Failure containment (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies where more than one tenant, project or environment shares the cluster.

**Lifecycle stages.** DESIGN, BUILD, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Job escapes partition quota; Storage namespace shared unintentionally; Partition admin with cluster-wide rights

**Testing safety.** Negative tests use a test account and minimal resources; no attempt to access other tenants' data.

**UNKNOWN rule.** If isolation in any layer cannot be evidenced, record UNKNOWN for that layer and do not assert partition isolation.

**Ontology classes.** FaultDomain, Interface, Safeguard · **Related controls.** MCF-CMP-010, MCF-NET-012, MCF-STO-012, MCF-SEC-006

**Informative references.** NIST SP 800-128 (security-focused configuration management); ISO/IEC 27001 (information security management systems)

### MCF-CMP-008

**Fault-Domain Design** · PREVENTIVE · claim type RESILIENCE · required AL5

**Objective.** Ensure the cluster is laid out so that loss of any single facility or infrastructure fault domain (rack, power feed group, CDU loop, leaf switch, scale-up domain) removes no more than the declared fraction of capacity and does not halt the Service Outcome beyond tolerance.

**Requirement.** The compute engineering authority shall map each compute node to its facility and infrastructure fault domains, shall limit the fraction of a Capability Instance's capacity in any single fault domain to the declared maximum, and shall demonstrate, by controlled drain or real event, that loss of a representative fault domain is contained and that jobs resume on remaining capacity within the recovery tolerance.

**Assessment criteria**

1. Every node is mapped to rack, power group, cooling loop, leaf and scale-up domain.
2. The largest fraction of capacity in any single fault domain is computed and is within the declared maximum.
3. Shared fault domains between nominally independent partitions are identified.
4. A controlled fault-domain drain or real event demonstrated containment and job resumption within tolerance.
5. The scheduler is configured to spread or co-locate according to the fault-domain policy.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum capacity fraction in a single facility fault domain | % of Capability Instance accelerators | 25 (illustrative) | Capability profile; outcome tolerance |
| Job resumption time after fault-domain loss | min | 60 (illustrative) | Capability profile; checkpoint interval |

**Minimum evidence**

- Node-to-fault-domain mapping
- Fault-domain concentration analysis
- Drain test or incident record with timeline
- Scheduler placement policy

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E4; E7 |
| optionalClasses | E3; E5 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; DEGRADED; FAILED; RECOVERY |
| periodCoverage | Test or event within 12 months |
| independence | Concentration analysis reperformed by the assessor |
| mandatoryItems | Fault-domain mapping; Concentration analysis; Drain test or incident record |
| acceptableAlternatives | Tabletop plus simulation using scheduler replay, where no live test is authorised (supports DESIGN only) |
| unknownEffect | US4 Critical: CG-09 UNKNOWN for compute containment |
| reassessmentTriggers | Cluster expansion; Facility fault-domain change; Fault-domain loss event |

**Assessment methods.** ANALYSIS, RECONCILIATION, SCENARIO_EXERCISE, TEST

**Assessment procedure**

1. Obtain mapping and reconcile with facility and fabric data.
2. Recompute concentration per fault domain.
3. Review drain test or incident timeline.
4. Review scheduler placement policy.
5. Record exceedances.

**Gate mappings.** CG-09 Failure containment (CRITICAL); CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to all in-scope clusters. For a single-rack deployment, the control evaluates whether the outcome tolerates loss of the whole cluster.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, FAILED, RECOVERY

**Failure modes addressed.** All scale-up domains of a job in one CDU loop; Capacity concentrated on a single power feed group; Hidden shared leaf between partitions

**Testing safety.** Controlled drains are capability-affecting. Draining nodes or partitions removes capacity from production jobs; the AI platform operator's change authority and job-owner notification are required. No facility fault (power or cooling) is induced for this control.

**UNKNOWN rule.** If node-to-facility-fault-domain mapping is incomplete, record U10 dependency UNKNOWN and US4 against CG-09.

**Ontology classes.** FaultDomain, Dependency, FailureScenario, CapacityAssertion · **Related controls.** MCF-CMP-005, MCF-NET-004, MCF-RES-005, MCF-RES-007

**Informative references.** AIDCF-004 (Threat, Hazard and Failure Model); AIDCF-013 (AI Data Centre Assurance Reference Architecture); Uptime Institute Tier Standard: Topology

## CMP-03 Capacity, scheduling and utilisation

### MCF-CMP-009

**Usable Accelerator Capacity** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Measure the accelerator capacity actually usable by the Capability Instance (healthy, schedulable, at rated performance, not thermally or power-throttled) and compare it with the capacity the outcome requires, rather than reporting installed accelerator count.

**Requirement.** The AI platform operator shall compute and report, at least daily, usable accelerator capacity as installed accelerators minus those drained, failed, quarantined, under repair, reserved, or throttled below the declared performance threshold, and shall compare it with the outcome's required capacity. The AI platform owner shall be notified when usable capacity falls below the required level.

**Assessment criteria**

1. The usable-capacity definition excludes drained, failed, quarantined, repair, reserved and throttled accelerators.
2. Usable capacity is reported at least daily for the period.
3. Usable capacity is compared with required capacity and breaches are notified to the AI platform owner.
4. Thermal or power throttling is counted using accelerator telemetry, not inferred.
5. Reported usable capacity reconciles with scheduler state on a sampled day.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Required usable capacity | % of installed accelerators | 92 (illustrative) | Capability profile; Service Outcome |
| Throttle performance threshold | % of rated clock or throughput | 95 (illustrative) | Capability profile |

**Minimum evidence**

- Usable-capacity definition and calculation
- Daily usable-capacity reports
- Notification records
- Throttle telemetry
- Scheduler state snapshot for reconciliation

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | Most recent 90 days |
| independence | Assessor reconciliation of one day's report to scheduler and telemetry data |
| mandatoryItems | Daily reports; Reconciliation sample |
| acceptableAlternatives | Goodput metrics from the training platform with equivalent exclusions |
| unknownEffect | US4 Critical: CG-08 UNKNOWN for capacity-dependent outcomes |
| reassessmentTriggers | Usable capacity below required; Definition change; Fleet expansion |

**Assessment methods.** ANALYSIS, RECONCILIATION, SAMPLING

**Assessment procedure**

1. Review the calculation definition.
2. Analyse 90-day trend against required capacity.
3. Reconcile a sampled day to scheduler state and telemetry.
4. Review notifications for breaches.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (CRITICAL); CG-01 Capability and outcome definition (SUPPORTING)

**Applicability.** Applies to all in-scope accelerator capacity.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Installed count reported as usable; Throttled accelerators masked; Long-running quarantines eroding capacity

**Testing safety.** Read-only data analysis.

**UNKNOWN rule.** If throttling cannot be measured, record U5 UNKNOWN; usable capacity cannot be asserted above the unthrottled-unknown fraction.

**Ontology classes.** CapacityAssertion, Resource, EvidenceObject · **Related controls.** MCF-CMP-017, MCF-CMP-018, MCF-CAP-013, MCF-OPS-021

**Informative references.** ISO/IEC 20000-1 (service management system requirements); MLCommons MLPerf Training and Inference benchmark rules

### MCF-CMP-010

**Scheduler Controls** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure the workload scheduler (for example Slurm or Kubernetes-based schedulers) enforces placement, priority, quota, topology-awareness and health-gating so that jobs land only on healthy nodes in the right topology and privileged scheduler functions are restricted.

**Requirement.** The AI platform operator shall configure the scheduler to admit jobs only to nodes passing health checks, to apply topology-aware placement for scale-up and rail locality, to enforce quotas and priorities per partition, and shall restrict scheduler administrative actions (drain, reservation, priority override) to authorised roles with logging. The scheduler control plane shall have documented high availability.

**Assessment criteria**

1. Health-gating is configured so failed or quarantined nodes are not schedulable.
2. Topology-aware placement is configured consistent with MCF-CMP-005.
3. Quotas and priorities per partition are configured and match policy.
4. Administrative actions require authorised roles and are logged.
5. Scheduler controller high availability is configured and has been failed over (test or event).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Scheduler controller failover time | s | 60 (illustrative) | Capability profile |

**Minimum evidence**

- Scheduler configuration export
- Health-gating rules
- Role and permission configuration
- Admin action logs
- Controller failover record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | Current configuration and 3 months of admin logs |
| independence | Assessor review of configuration export, not operator summary |
| mandatoryItems | Configuration export; Admin action logs |
| acceptableAlternatives | Policy-as-code repository with tests |
| unknownEffect | US3 Material: job placement integrity uncertain; CG-08 supporting |
| reassessmentTriggers | Scheduler upgrade; Policy change; Unauthorised admin action |

**Assessment methods.** RECONCILIATION, DOCUMENT_REVIEW, SAMPLING

**Assessment procedure**

1. Obtain configuration export.
2. Verify health-gating and topology rules.
3. Sample admin logs for authorisation.
4. Review failover evidence.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to all in-scope job schedulers and orchestrators.

**Lifecycle stages.** BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Jobs scheduled onto failing node; Topology-blind placement degrading collectives; Unauthorised priority override; Scheduler controller single point of failure

**Testing safety.** Read-only; no scheduler changes by the assessor. Failover tests only with operator authorisation.

**UNKNOWN rule.** If admin logs are unavailable, record U1 UNKNOWN for administrative-control assertions.

**Ontology classes.** InfrastructureSystem, Safeguard, Interface · **Related controls.** MCF-CMP-005, MCF-CMP-018, MCF-SEC-006, MCF-SEC-003

**Informative references.** NIST SP 800-128 (security-focused configuration management); ISO/IEC 20000-1 (service management system requirements)

### MCF-CMP-011

**Resource Reservation** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure capacity required for priority outcomes, hot spares and recovery (re-running from checkpoint after failure) is reserved and actually available when needed, rather than consumed by lower-priority work.

**Requirement.** The AI platform operator shall reserve accelerator capacity for declared priority outcomes and for recovery (hot spare nodes or scale-up domains), shall verify daily that reservations are intact and healthy, and shall be able to reclaim reserved capacity from lower-priority jobs within the declared time.

**Assessment criteria**

1. Reservations for priority outcomes and recovery are defined with sizes.
2. Daily verification shows reserved capacity is healthy and available.
3. Reclaim from lower-priority jobs works within the declared time (test or event).
4. Reservation size is justified against failure rates and recovery needs.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Recovery reserve | % of job size | 5 (illustrative) | Capability profile; observed node failure rate |
| Reclaim time | min | 15 (illustrative) | Capability profile |

**Minimum evidence**

- Reservation definitions
- Daily reservation health reports
- Reclaim test or event record
- Sizing rationale

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; RECOVERY |
| periodCoverage | Most recent 90 days |
| independence | Assessor sample of daily reports against scheduler state |
| mandatoryItems | Reservation health reports; Reclaim evidence |
| acceptableAlternatives | Scheduler logs showing successful use of reserve during failures |
| unknownEffect | US3 Material: recovery capacity uncertain; CG-10 supporting |
| reassessmentTriggers | Change in failure rate; Reservation change; Failed reclaim |

**Assessment methods.** ANALYSIS, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Review definitions and sizing.
2. Analyse daily health reports.
3. Review reclaim evidence.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies where priority outcomes or recovery depend on reserved compute.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, RECOVERY

**Failure modes addressed.** Reserve nodes unhealthy when needed; Reserve consumed by preemptible jobs not reclaimed; Reserve undersized for failure rate

**Testing safety.** Reclaim tests preempt jobs; job-owner notification required.

**UNKNOWN rule.** If reservation health is not verified, record U5 UNKNOWN for recovery-capacity assertions.

**Ontology classes.** CapacityAssertion, Resource, Safeguard · **Related controls.** MCF-CMP-009, MCF-CMP-023, MCF-RES-010, MCF-STO-018

**Informative references.** ISO/IEC 20000-1 (service management system requirements)

### MCF-CMP-012

**Contention Management** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Detect and manage contention for shared resources (accelerators, fabric, storage bandwidth, power caps) so that one workload's demand does not degrade another priority outcome beyond tolerance, including coordinated facility power capping.

**Requirement.** The AI platform operator shall define contention policies (preemption, fair share, bandwidth QoS, power-cap allocation), shall monitor indicators of contention (queue wait, job slowdown, fabric and storage saturation), and shall act when priority outcomes degrade beyond tolerance. Where facility-driven power capping is used, the AI platform operator and facility operator shall agree the capping protocol and its effect on priority outcomes.

**Assessment criteria**

1. Contention policies are documented and configured.
2. Contention indicators are monitored with thresholds.
3. Events where priority outcomes degraded show timely action.
4. Facility power-capping protocol is agreed and exercised where used.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Priority job slowdown tolerance | % versus baseline | 10 (illustrative) | Capability profile |

**Minimum evidence**

- Contention policy
- Monitoring dashboards and thresholds
- Contention event records
- Power-capping protocol and exercise

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY |
| periodCoverage | Most recent 90 days |
| independence | Assessor analysis of raw indicators |
| mandatoryItems | Contention policy; Event records |
| acceptableAlternatives | Post-incident reviews covering contention |
| unknownEffect | US2 Moderate: confidence ceiling CONF-2 for performance outcomes |
| reassessmentTriggers | New tenant; Workload mix change; Power-cap event |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW, INQUIRY

**Assessment procedure**

1. Review contention policies and their configuration.
2. Analyse queue-wait, slowdown and saturation indicators for the period.
3. Review handling of events where priority outcomes degraded.
4. Review the facility power-capping protocol and its last exercise.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to shared clusters and to clusters subject to facility power capping.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY

**Failure modes addressed.** Storage saturation by one job stalling others; Uncoordinated power capping slowing priority training; Starvation of priority queue

**Testing safety.** Analysis only.

**UNKNOWN rule.** If contention indicators are not collected, record U1 UNKNOWN for performance-outcome assertions.

**Ontology classes.** Resource, Safeguard, OperatingState · **Related controls.** MCF-CMP-009, MCF-STO-008, MCF-NET-007, MCF-POW-020

**Informative references.** ISO/IEC 20000-1 (service management system requirements)

## CMP-04 Firmware, driver and compatibility

### MCF-CMP-013

**Firmware Baseline** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure firmware on accelerators, NICs, BMCs, BIOS/UEFI, interconnect switches and power shelves is at approved, authenticated versions across the fleet, because firmware mismatch is a common-mode source of hangs, errors and security exposure.

**Requirement.** The AI platform operator shall maintain an approved firmware matrix per node and rack type, shall verify signature or provenance of each firmware image before deployment, shall measure firmware versions across the fleet automatically, and shall remediate drift within the declared time. Where the platform supports it, the AI platform operator shall use device attestation (for example SPDM measurements or TPM-based measured boot) to confirm firmware identity.

**Assessment criteria**

1. An approved firmware matrix exists covering every firmware-bearing component class.
2. Firmware image provenance or signature is verified before deployment.
3. Automated inventory covers the declared fraction of the fleet.
4. Drift beyond the declared time is absent or approved as exception.
5. Attestation evidence is collected where supported.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Firmware drift remediation time | days | 7 (illustrative) | Capability profile |
| Firmware inventory coverage | % of devices | 100 (illustrative) | Capability profile |

**Minimum evidence**

- Approved firmware matrix
- Signature/provenance verification records
- Fleet firmware inventory
- Drift and exception register
- Attestation reports where supported

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E5 |
| qualityFloor | P4 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; TRANSITION |
| periodCoverage | Current inventory and 3 months of drift history |
| independence | Assessor queries device firmware directly on a sample |
| mandatoryItems | Firmware matrix; Fleet inventory |
| acceptableAlternatives | Vendor fleet-management tool report with raw export |
| unknownEffect | US4 Critical: CG-08 UNKNOWN where fleet firmware state is unverified |
| reassessmentTriggers | Firmware release; Drift above threshold; Security advisory |

**Assessment methods.** RECONCILIATION, SAMPLING, REPERFORMANCE, DOCUMENT_REVIEW

**Assessment procedure**

1. Obtain matrix and inventory.
2. Reperform version query on a sample.
3. Review signature verification records.
4. Review drift and exceptions.
5. Review attestation where supported.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (CRITICAL); CG-14 Change control (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to all firmware-bearing components in the compute boundary.

**Lifecycle stages.** BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, TRANSITION

**Failure modes addressed.** Mixed accelerator firmware within a job; Unsigned BMC firmware; NIC firmware incompatible with fabric; Power-shelf firmware bug

**Testing safety.** Read-only queries with operator-authorised accounts.

**UNKNOWN rule.** If any component class is not inventoried, record U5 UNKNOWN for that class; the control cannot be CONFORMING.

**Ontology classes.** AssetInstance, ArchitectureSnapshot, Safeguard · **Related controls.** MCF-CMP-004, MCF-CMP-015, MCF-SUP-014, MCF-SEC-013

**Informative references.** NIST SP 800-193 (platform firmware resiliency guidelines); NIST SP 800-147B (BIOS protection guidelines for servers); DMTF SPDM (Security Protocol and Data Model) for device authentication and attestation; TCG TPM 2.0 Library Specification; DMTF Redfish (platform management API)

### MCF-CMP-014

**Driver Compatibility** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure accelerator drivers, communication libraries, runtimes, kernel and container base images form a tested compatible stack, and that workloads run only on stacks in the compatibility matrix.

**Requirement.** The AI platform operator shall maintain a compatibility matrix linking firmware, kernel, accelerator driver, communication library, runtime and container base images, shall test each matrix entry before approval, and shall prevent workloads from running on unapproved combinations through image and node labelling.

**Assessment criteria**

1. A compatibility matrix exists and is versioned.
2. Each approved combination has a test record.
3. Node labels or admission controls prevent unapproved combinations.
4. Container base images declare required driver ranges.
5. Deviations are tracked.

**Minimum evidence**

- Compatibility matrix
- Test records per combination
- Admission control configuration
- Image manifests

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; TRANSITION |
| periodCoverage | Current matrix |
| independence | Assessor sample check of running node stacks |
| mandatoryItems | Compatibility matrix; Test records |
| acceptableAlternatives | Vendor-certified stack documentation plus site regression tests |
| unknownEffect | US3 Material: stack compatibility uncertain; CG-08 supporting |
| reassessmentTriggers | Driver or library release; Kernel update; Image change |

**Assessment methods.** RECONCILIATION, DOCUMENT_REVIEW, SAMPLING

**Assessment procedure**

1. Obtain matrix and tests.
2. Sample running nodes for stack versions.
3. Verify admission controls.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all accelerator software stacks used by in-scope workloads.

**Lifecycle stages.** BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, TRANSITION

**Failure modes addressed.** Driver/firmware mismatch causing hangs; Library version causing silent numerical changes; Container with incompatible driver expectation

**Testing safety.** Read-only sampling of running stacks via operator-provided inventory tooling.

**UNKNOWN rule.** If running stacks cannot be sampled, record U2 inaccessible UNKNOWN.

**Ontology classes.** ArchitectureSnapshot, AssetInstance, Interface · **Related controls.** MCF-CMP-013, MCF-CMP-015, MCF-SUP-015

**Informative references.** NIST SP 800-128 (security-focused configuration management); DMTF SPDM (Security Protocol and Data Model) for device authentication and attestation

### MCF-CMP-015

**Upgrade Testing** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure firmware, driver and software upgrades are tested on representative workloads and rolled out in stages with soak periods and automatic halt criteria, so that a defective release cannot become a fleet-wide common-mode failure.

**Requirement.** The AI platform operator shall test each upgrade on a staging environment with representative workloads (including multi-node collective tests and checkpoint/restore), shall roll out in stages starting with a canary cohort spread across fault domains, shall define soak periods and halt criteria based on error rates and performance, and shall record each stage's go/no-go decision.

**Assessment criteria**

1. Each upgrade has a staging test record including multi-node collective and checkpoint/restore tests.
2. Rollout plans define canary, staged cohorts, soak periods and halt criteria.
3. Canary cohorts span multiple fault domains but are limited in size.
4. Go/no-go decisions per stage are recorded with metrics.
5. At least one halted rollout or a test of halt automation demonstrates halt criteria work.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Canary cohort size | % of fleet | 2 (illustrative) | Capability profile |
| Soak period per stage | h | 72 (illustrative) | Capability profile |
| Halt criterion: error-rate increase | × baseline | 2 (illustrative) | Capability profile |

**Minimum evidence**

- Staging test records
- Rollout plans
- Stage go/no-go records with metrics
- Halt event or test record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5 |
| qualityFloor | P4 F4 C3 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | TRANSITION; NORMAL; DEGRADED |
| periodCoverage | Most recent 3 upgrades |
| independence | Review of go/no-go by a role independent of the release engineer |
| mandatoryItems | Staging test records; Stage go/no-go records |
| acceptableAlternatives | Vendor-managed rollout with equivalent stage evidence |
| unknownEffect | US4 Critical: CG-14 UNKNOWN for compute change control |
| reassessmentTriggers | Skipped stage; Fleet-wide incident after upgrade; Process change |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, ANALYSIS, INQUIRY

**Assessment procedure**

1. Sample recent upgrades.
2. Review staging tests.
3. Review rollout plans and stage decisions.
4. Check halt evidence.

**Gate mappings.** CG-14 Change control (CRITICAL); CG-09 Failure containment (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all firmware, driver and system software changes on in-scope compute.

**Lifecycle stages.** CHANGE, OPERATE · **Operating states.** TRANSITION, NORMAL, DEGRADED

**Failure modes addressed.** Fleet-wide firmware defect (common-mode); Upgrade breaks checkpoint compatibility; Canary in single fault domain hiding issues; Soak too short to show intermittent errors

**Testing safety.** Reviews of records; no upgrades performed by assessor.

**UNKNOWN rule.** If stage go/no-go evidence is missing for a sampled upgrade, record U1 UNKNOWN and Finding.

**Ontology classes.** Action, TestRecord, FailureScenario, Safeguard · **Related controls.** MCF-CMP-013, MCF-CMP-016, MCF-OPS-018, MCF-SUP-015

**Informative references.** NIST SP 800-128 (security-focused configuration management); ISO/IEC 20000-1 (service management system requirements); AIDCF-004 (Threat, Hazard and Failure Model)

### MCF-CMP-016

**Rollback Readiness** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure every firmware and software change can be rolled back to the previous known-good baseline within the declared time, including components where rollback is constrained (anti-rollback fuses, one-way firmware migrations).

**Requirement.** The AI platform operator shall define a rollback procedure for each change class, shall identify components where rollback is constrained or impossible and treat them as higher-risk changes, shall retain previous known-good images, and shall test rollback in staging for each change before production rollout.

**Assessment criteria**

1. Rollback procedures exist per change class.
2. Components with rollback constraints are identified and flagged in change records.
3. Previous known-good images are retained and integrity-verified.
4. Rollback has been tested in staging for sampled changes within the declared time.
5. A production rollback (test or event) achieved the declared time.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Rollback time objective | h | 4 (illustrative) | Capability profile |

**Minimum evidence**

- Rollback procedures
- Rollback-constraint register
- Image retention records with hashes
- Staging rollback tests
- Production rollback record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | TRANSITION; RECOVERY; DEGRADED |
| periodCoverage | Most recent 3 changes |
| independence | Assessor verification of image hashes |
| mandatoryItems | Rollback procedures; Staging rollback tests |
| acceptableAlternatives | Real rollback event records |
| unknownEffect | US3 Material: recovery from defective change uncertain; CG-10 supporting |
| reassessmentTriggers | New anti-rollback firmware; Failed rollback; Image retention change |

**Assessment methods.** DOCUMENT_REVIEW, TEST, REPERFORMANCE

**Assessment procedure**

1. Review procedures and constraints.
2. Verify retained image hashes.
3. Review staging and production rollback records.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all changes in the compute baseline.

**Lifecycle stages.** CHANGE, OPERATE · **Operating states.** TRANSITION, RECOVERY, DEGRADED

**Failure modes addressed.** Anti-rollback fuse prevents downgrade; Previous image deleted; Rollback untested

**Testing safety.** Rollback tests in staging only unless authorised.

**UNKNOWN rule.** If rollback has not been tested, record U1 UNKNOWN; the RESILIENCE claim cannot be CONFORMING.

**Ontology classes.** Action, Safeguard, TestRecord · **Related controls.** MCF-CMP-015, MCF-CMP-023, MCF-OPS-020, MCF-SEC-024

**Informative references.** NIST SP 800-193 (platform firmware resiliency guidelines); NIST SP 800-128 (security-focused configuration management)

## CMP-05 Compute health and observability

### MCF-CMP-017

**GPU Telemetry** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Collect accelerator telemetry (temperature, power, clocks, throttle reasons, memory ECC counts, page/row retirement, interconnect errors, utilisation) at sufficient frequency and completeness to detect degradation and to correlate compute behaviour with facility events.

**Requirement.** The AI platform operator shall collect accelerator telemetry from every in-scope accelerator at the declared interval using vendor management interfaces, shall monitor collection completeness, shall time-synchronise telemetry with facility (BMS/EPMS) data, and shall retain it for the declared period.

**Assessment criteria**

1. Telemetry includes temperature, power, clocks, throttle reasons, ECC counts, retirement events and interconnect errors.
2. Collection covers the declared fraction of accelerators with completeness monitoring.
3. Timestamps are synchronised to a common time source shared with facility systems.
4. Retention meets the declared period.
5. Throttle-reason telemetry is used to report thermal and power throttling to facility operations.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Telemetry interval | s | 10 (illustrative) | Capability profile |
| Collection completeness | % of expected samples | 99 (illustrative) | Capability profile |
| Retention | days | 90 (illustrative) | Capability profile |

**Minimum evidence**

- Accelerator telemetry schema
- Per-rack collection completeness reports
- Time synchronisation configuration
- Retention configuration
- Throttle reports to facility

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE; EMERGENCY |
| periodCoverage | Most recent 90 days |
| independence | Assessor comparison of raw device query with stored telemetry |
| mandatoryItems | Completeness report; Time-sync evidence |
| acceptableAlternatives | Vendor fleet telemetry service export |
| unknownEffect | US3 Material: degradation detection and thermal correlation limited; CG-08 and CG-06 supporting |
| reassessmentTriggers | Collector change; Completeness below target; New accelerator type |

**Assessment methods.** ANALYSIS, REPERFORMANCE, INSPECTION

**Assessment procedure**

1. Review the telemetry schema against the required fields.
2. Analyse collection completeness by rack and accelerator.
3. Compare a live device query with stored values.
4. Check time synchronisation with BMS/EPMS and retention settings.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to all in-scope accelerators.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Telemetry blindness on a rack; Clock skew preventing correlation with cooling event; Throttling unreported

**Testing safety.** Read-only device queries using an operator-authorised monitoring account.

**UNKNOWN rule.** If telemetry completeness is below target, record U5 UNKNOWN for affected accelerators.

**Ontology classes.** EvidenceObject, AssetInstance, Interface · **Related controls.** MCF-CMP-018, MCF-CMP-019, MCF-NET-024, MCF-THM-008

**Informative references.** DMTF Redfish (platform management API); Open Compute Project hardware management and fault-management specifications

### MCF-CMP-018

**Node Health** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure each node's health is checked before, during and after jobs by automated checks (accelerator diagnostics, memory, interconnect, NIC, storage mount, thermal state) and unhealthy nodes are drained before they cause job failure.

**Requirement.** The AI platform operator shall run automated health checks at job prolog/epilog and at a periodic interval, shall define pass criteria per check, shall drain nodes failing a check automatically, and shall track drained nodes to repair or return-to-service.

**Assessment criteria**

1. Health-check suite and pass criteria are documented.
2. Checks run at prolog/epilog and periodically, with logs.
3. Failing nodes are drained automatically.
4. Drained nodes are tracked to resolution with ageing.
5. Job failures attributable to node faults are trended.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Periodic health-check interval | h | 24 (illustrative) | Capability profile |
| Maximum drained-node age before escalation | days | 5 (illustrative) | Capability profile |

**Minimum evidence**

- Health-check suite definition
- Check execution logs
- Drain events
- Drained-node tracker
- Job-failure attribution trend

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | Most recent 90 days |
| independence | Assessor sample of job failures traced to node health records |
| mandatoryItems | Check logs; Drain events |
| acceptableAlternatives | Vendor diagnostic scheduler integration logs |
| unknownEffect | US3 Material: job reliability uncertain; CG-08 supporting |
| reassessmentTriggers | Check suite change; Rise in node-attributed job failures |

**Assessment methods.** ANALYSIS, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Review suite.
2. Sample logs.
3. Trace job failures.
4. Review drained-node ageing.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all in-scope nodes.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Unhealthy node admitted to job; Drained nodes forgotten; Health check too shallow

**Testing safety.** Read-only review of health-check logs; no health checks triggered on production nodes.

**UNKNOWN rule.** If health-check logs are unavailable, record U1 UNKNOWN.

**Ontology classes.** AssetInstance, Safeguard, EvidenceObject · **Related controls.** MCF-CMP-017, MCF-CMP-019, MCF-CMP-010

**Informative references.** Open Compute Project hardware management and fault-management specifications; ISO/IEC 20000-1 (service management system requirements)

### MCF-CMP-019

**Error and Degradation Detection** · DETECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Detect accelerator and node errors that threaten job integrity (uncorrectable ECC, rising correctable ECC, memory row remapping exhaustion, vendor fatal error events such as XID-type events, PCIe AER errors, interconnect CRC errors) and silent data corruption, and respond before corrupted results propagate into checkpoints or models.

**Requirement.** The AI platform operator shall classify accelerator and node error events by severity with defined automatic actions (drain, reset, RMA), shall trend correctable error rates against thresholds, and shall run periodic silent-data-corruption screening (known-answer tests) across the fleet. The AI platform operator shall link detected corruption to affected jobs and checkpoints for integrity assessment.

**Assessment criteria**

1. An error classification exists with severity and automatic action per event class.
2. Uncorrectable and fatal events trigger automatic drain within the declared time (verified on sample events).
3. Correctable error rates are trended and threshold breaches are actioned.
4. Silent-data-corruption screening runs fleet-wide at the declared interval and failures are actioned.
5. Jobs and checkpoints run on nodes later found faulty are identified for integrity review.
6. Detection has been validated by fault injection, known-bad hardware or real events.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Drain time after fatal error event | min | 5 (illustrative) | Capability profile |
| SDC screening interval | days | 30 (illustrative) | Capability profile; OCP SDC practice |
| Correctable ECC escalation threshold | events per day per accelerator | platform-specific | Platform OEM RAS guidance |

**Minimum evidence**

- Error classification and action table
- Sample error events with timestamps of action
- Correctable error trend
- SDC screening results
- Job/checkpoint impact analyses

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E1; E5; E7 |
| qualityFloor | P4 F4 C3 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; FAILED |
| periodCoverage | Most recent 90 days |
| independence | Assessor reconstructs timeline for sampled events |
| mandatoryItems | Classification table; Event-to-action timelines; SDC screening results |
| acceptableAlternatives | Vendor RAS service reports with raw events |
| unknownEffect | US4 Critical: CG-08 UNKNOWN for integrity outcomes |
| reassessmentTriggers | New error class; SDC finding; Detection miss |

**Assessment methods.** ANALYSIS, SAMPLING, TEST, DOCUMENT_REVIEW

**Assessment procedure**

1. Review classification.
2. Sample fatal events and reconstruct drain timelines.
3. Analyse correctable error trends.
4. Review SDC screening coverage and results.
5. Review job/checkpoint impact analyses.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (CRITICAL)

**Applicability.** Applies to all in-scope accelerators and hosts.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, DEGRADED, FAILED

**Failure modes addressed.** Silent data corruption contaminating checkpoints; Fatal error not draining node causing job hangs; Rising correctable ECC preceding failure unnoticed; Row-remap exhaustion

**Testing safety.** Fault injection only on drained test nodes with operator authorisation; never on production jobs.

**UNKNOWN rule.** If SDC screening is not performed, record US4 UNKNOWN against CG-08 for integrity outcomes.

**Ontology classes.** FailureMode, Safeguard, EvidenceObject, FailureScenario · **Related controls.** MCF-CMP-017, MCF-CMP-018, MCF-STO-009, MCF-STO-017

**Informative references.** Open Compute Project server component resilience and silent data corruption materials; JEDEC memory standards (DDR and HBM families) for ECC and RAS features; PCI Express Base Specification (Advanced Error Reporting); Open Compute Project hardware management and fault-management specifications

### MCF-CMP-020

**Performance Baselines** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Maintain performance baselines (single-accelerator throughput, scale-up bandwidth, multi-node collective bandwidth, representative training step time) so that degradation from hardware, firmware, thermal or fabric causes is detected quantitatively.

**Requirement.** The AI platform operator shall define baseline benchmarks per node type and cluster scale, shall run them at acceptance, after changes and at a periodic interval, and shall investigate deviations beyond the declared threshold.

**Assessment criteria**

1. Baseline benchmarks and expected results are defined per node type and scale.
2. Benchmarks run at acceptance, after changes and periodically.
3. Deviations beyond the threshold are investigated with root cause.
4. Baselines are refreshed with approval when the baseline changes.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Performance regression threshold | % below baseline | 5 (illustrative) | Capability profile |

**Minimum evidence**

- Benchmark definitions and baselines
- Benchmark run results
- Deviation investigations

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; TRANSITION |
| periodCoverage | Most recent 6 months |
| independence | Assessor review of raw benchmark output |
| mandatoryItems | Baselines; Run results |
| acceptableAlternatives | Production job step-time telemetry with normalisation |
| unknownEffect | US2 Moderate: confidence ceiling CONF-2 for performance outcomes |
| reassessmentTriggers | Baseline change; Unexplained regression |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW, SAMPLING

**Assessment procedure**

1. Review definitions.
2. Analyse run results.
3. Review investigations.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all in-scope clusters.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, TRANSITION

**Failure modes addressed.** Gradual regression unnoticed; Thermal throttling reducing throughput; Post-upgrade slowdown

**Testing safety.** Benchmarks run on drained nodes only.

**UNKNOWN rule.** If no baseline exists, record U1 UNKNOWN for performance-outcome claims.

**Ontology classes.** CapacityAssertion, TestRecord, EvidenceObject · **Related controls.** MCF-CMP-006, MCF-CMP-015, MCF-NET-008

**Informative references.** MLCommons MLPerf Training and Inference benchmark rules

## CMP-06 Compute lifecycle and recovery

### MCF-CMP-021

**Provisioning** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure new and repaired hardware enters service only after verified identity, baseline conformance and burn-in acceptance, so that infant-mortality failures and counterfeit or mis-configured components are caught before production.

**Requirement.** The AI platform operator shall provision nodes through an automated pipeline that verifies component identity against the purchase and provenance records, applies the approved baseline, runs a burn-in and acceptance suite (stress, memory, interconnect, thermal, storage) for the declared duration, and records acceptance before the node becomes schedulable.

**Assessment criteria**

1. Component identity is verified against provenance records.
2. Baseline is applied automatically and verified.
3. Burn-in runs for the declared duration with defined pass criteria.
4. Nodes become schedulable only after recorded acceptance.
5. Burn-in failure rates are trended by supplier and lot.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Burn-in duration | h | 48 (illustrative) | Capability profile; OEM guidance |

**Minimum evidence**

- Provisioning pipeline definition
- Identity verification records
- Burn-in results
- Acceptance records
- Failure trend by lot

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | TRANSITION; NORMAL |
| periodCoverage | Nodes provisioned in the last 6 months (sample) |
| independence | Assessor trace of sampled nodes from receipt to acceptance |
| mandatoryItems | Burn-in results; Acceptance records |
| acceptableAlternatives | OEM factory burn-in with site acceptance subset |
| unknownEffect | US3 Material: infant-mortality risk; CG-08 supporting |
| reassessmentTriggers | New supplier or lot; Burn-in suite change |

**Assessment methods.** SAMPLING, DOCUMENT_REVIEW, RECONCILIATION

**Assessment procedure**

1. Sample nodes.
2. Trace identity, baseline, burn-in and acceptance.
3. Review failure trends.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all nodes entering service, including after RMA.

**Lifecycle stages.** BUILD, COMMISSION, CHANGE · **Operating states.** TRANSITION, NORMAL

**Failure modes addressed.** Infant-mortality failure in production; Counterfeit component; Node admitted without baseline

**Testing safety.** Burn-in is performed by operator; assessors review records.

**UNKNOWN rule.** Nodes without acceptance records are U1 UNKNOWN.

**Ontology classes.** AssetInstance, TestRecord, Safeguard · **Related controls.** MCF-CMP-004, MCF-CMP-022, MCF-SUP-010, MCF-SUP-012

**Informative references.** Open Compute Project hardware management and fault-management specifications; ISO/IEC 20243 (Open Trusted Technology Provider Standard)

### MCF-CMP-022

**Spares and RMA** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure spare accelerators, nodes, trays, switch trays, NICs and cables are held in quantities and locations sufficient to restore usable capacity within tolerance, and that RMA turnaround is tracked against supplier obligations.

**Requirement.** The AI platform operator shall size spares from observed failure rates and lead times, shall hold spares on site or within the declared logistics time, shall track RMA turnaround against contractual obligations, and shall ensure returned parts are sanitised or tracked under custody.

**Assessment criteria**

1. Spares sizing uses observed failure rates and lead times.
2. Spares inventory matches the sizing for sampled component classes.
3. RMA turnaround is tracked against supplier obligations.
4. Long-lead components are identified with mitigation.
5. Returned components with storage are sanitised or under custody.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| On-site spares | % of installed by class | 3 (illustrative) | Capability profile; failure-rate analysis |
| RMA turnaround obligation | days | contractual | Supplier contract |

**Minimum evidence**

- Spares sizing analysis
- Inventory records
- RMA tracker
- Long-lead register
- Custody/sanitisation records for returns

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; RECOVERY |
| periodCoverage | Most recent 6 months |
| independence | Assessor physical count of a spares sample |
| mandatoryItems | Sizing analysis; Inventory and RMA records |
| acceptableAlternatives | Supplier-managed spares pool contract with evidence of availability |
| unknownEffect | US3 Material: restoration capacity uncertain; CG-10 supporting |
| reassessmentTriggers | Failure-rate increase; Supplier change; Stock-out |

**Assessment methods.** ANALYSIS, INSPECTION, DOCUMENT_REVIEW

**Assessment procedure**

1. Review sizing.
2. Physically count sample.
3. Review RMA performance.
4. Review custody for returns.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to all in-scope compute hardware.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, DEGRADED, RECOVERY

**Failure modes addressed.** Stock-out of long-lead part; RMA delay eroding usable capacity; Returned drive leaking data

**Testing safety.** Inspection of stores under escort.

**UNKNOWN rule.** If inventory cannot be reconciled, record U4 conflicting UNKNOWN.

**Ontology classes.** Resource, Dependency, AssetInstance · **Related controls.** MCF-CMP-021, MCF-SUP-017, MCF-SUP-018, MCF-DEP-011

**Informative references.** ISO/IEC 19770 series (IT asset management); NIST SP 800-88 (guidelines for media sanitisation)

### MCF-CMP-023

**Node Rebuild** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure nodes and scale-up domains can be rebuilt from bare metal to an accepted, schedulable state within the declared time after failure, corruption or mass events (for example after a power or cooling outage), including re-qualification before rejoining production.

**Requirement.** The AI platform operator shall maintain an automated rebuild path (image, baseline, configuration, credentials, health and bandwidth re-qualification) that does not depend on services lost in the same event, shall define the rebuild time objective per node and for a mass rebuild of a declared fraction of the cluster, and shall exercise mass rebuild at a defined interval. After facility power or cooling events, the AI platform operator shall re-qualify affected nodes before readmission.

**Assessment criteria**

1. An automated rebuild path exists and its dependencies (image repository, provisioning network, identity) are documented.
2. Rebuild dependencies are not in the same fault domain as the event they recover from, or the gap is treated.
3. Single-node rebuild meets the time objective on sampled events.
4. A mass rebuild exercise of the declared fraction met the time objective.
5. Post-facility-event re-qualification is defined and was applied in the last event.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Single-node rebuild time objective | h | 2 (illustrative) | Capability profile |
| Mass rebuild fraction | % of cluster | 25 (illustrative) | Capability profile |
| Mass rebuild time objective | h | 12 (illustrative) | Capability profile |

**Minimum evidence**

- Rebuild automation definition
- Rebuild dependency map
- Single-node rebuild timings
- Mass rebuild exercise record
- Re-qualification records after facility events

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | RECOVERY; FAILED; TRANSITION |
| periodCoverage | Exercise within 12 months |
| independence | Exercise observed by a party independent of the provisioning team |
| mandatoryItems | Dependency map; Mass rebuild exercise record |
| acceptableAlternatives | Real mass-recovery event with full timeline |
| unknownEffect | US4 Critical: CG-10 UNKNOWN for compute recovery |
| reassessmentTriggers | Provisioning system change; Failed rebuild; Cluster growth beyond tested fraction |

**Assessment methods.** SCENARIO_EXERCISE, ANALYSIS, DOCUMENT_REVIEW, SAMPLING

**Assessment procedure**

1. Review rebuild path and dependencies.
2. Sample single-node rebuild timings.
3. Review mass rebuild exercise.
4. Review post-event re-qualification.

**Gate mappings.** CG-10 Recovery readiness (CRITICAL); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all in-scope compute.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** RECOVERY, FAILED, TRANSITION

**Failure modes addressed.** Image repository in same failed domain; Mass rebuild overwhelms provisioning network; Nodes readmitted after thermal event without re-qualification

**Testing safety.** Mass rebuild exercises are capability-affecting. Draining nodes or partitions removes capacity from production jobs; the AI platform operator's change authority and job-owner notification are required.

**UNKNOWN rule.** If no mass rebuild exercise exists, record US4 UNKNOWN against CG-10.

**Ontology classes.** FailureScenario, Safeguard, TestRecord, Dependency · **Related controls.** MCF-CMP-016, MCF-THM-024, MCF-RES-015, MCF-STO-018

**Informative references.** AIDCF-004 (Threat, Hazard and Failure Model); ISO/IEC 20000-1 (service management system requirements); ISO 22301 (business continuity management systems)

### MCF-CMP-024

**Secure Retirement** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure retired or returned compute hardware (nodes, accelerators with memory, BMCs, boot drives, NICs with persistent configuration) is removed from inventory, sanitised, and disposed of with custody, so that data, credentials and model weights are not exposed and the asset register stays accurate.

**Requirement.** The AI platform operator shall execute a retirement procedure that revokes credentials and attestation identities, sanitises persistent storage per a recognised sanitisation standard with verification, resets BMC and firmware secrets, updates the asset register and topology, and records custody to disposal or resale.

**Assessment criteria**

1. The retirement procedure covers credentials, storage sanitisation, BMC reset, register update and custody.
2. Sanitisation method and verification are recorded per device.
3. Asset register and topology are updated for sampled retirements.
4. Custody chain to disposal or resale is complete.
5. Credentials and certificates of retired nodes are revoked.

**Minimum evidence**

- Retirement procedure
- Sanitisation certificates for boot drives and persistent devices
- Asset register changes
- Custody records from decommissioning to disposal
- Credential revocation records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | SHUTDOWN; TRANSITION |
| periodCoverage | Retirements in the last 12 months (sample) |
| independence | Third-party sanitisation certificate or assessor verification sample |
| mandatoryItems | Sanitisation certificates; Custody records |
| acceptableAlternatives | Physical destruction certificates |
| unknownEffect | US2 Moderate: no gate; record for data-protection and inventory assertions |
| reassessmentTriggers | Retirement campaign; Disposal vendor change |

**Assessment methods.** SAMPLING, DOCUMENT_REVIEW, RECONCILIATION

**Assessment procedure**

1. Sample retirements from the last 12 months.
2. Verify credential and attestation-identity revocation for each sampled node.
3. Verify sanitisation certificates and method for each persistent device.
4. Reconcile asset register and topology removal.
5. Trace custody to disposal or resale.

**Gate mappings.** CG-02 Boundary and architecture integrity (SUPPORTING)

**Applicability.** Applies to all retired in-scope compute hardware.

**Lifecycle stages.** DECOMMISSION · **Operating states.** SHUTDOWN, TRANSITION

**Failure modes addressed.** Model weights recoverable from retired drive; Stale node in asset register; Unrevoked certificates

**Testing safety.** Record review; no handling of media.

**UNKNOWN rule.** Retirements without sanitisation evidence are recorded as U1 UNKNOWN and Findings.

**Ontology classes.** AssetInstance, Action, Safeguard · **Related controls.** MCF-STO-024, MCF-PHY-020, MCF-ENV-020, MCF-CMP-022

**Informative references.** NIST SP 800-88 (guidelines for media sanitisation); IEEE 2883 (standard for sanitizing storage); ISO/IEC 19770 series (IT asset management)
