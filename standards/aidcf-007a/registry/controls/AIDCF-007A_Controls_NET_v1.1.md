# AIDCF-007A Control Catalogue — NET AI Network and Interconnect Architecture

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-NET](../../../aidcf-018-domain-guides/AIDCF-018-NET_AI_Network_and_Interconnect_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-NET-001](#mcf-net-001) | Fabric Topology | PREVENTIVE | IMPLEMENTATION | AL3 | CG-08 | CG-02 |
| [MCF-NET-002](#mcf-net-002) | Path Diversity | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-03, CG-08, CG-09 |
| [MCF-NET-003](#mcf-net-003) | Oversubscription | PREVENTIVE | DESIGN | AL2 | — | CG-08 |
| [MCF-NET-004](#mcf-net-004) | Fabric Fault-Domain Design | PREVENTIVE | RESILIENCE | AL5 | CG-09 | CG-08, CG-03 |
| [MCF-NET-005](#mcf-net-005) | Latency Baseline | DETECTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-NET-006](#mcf-net-006) | Loss and Retransmission | DETECTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-NET-007](#mcf-net-007) | Congestion Control | PREVENTIVE | EFFECTIVENESS | AL5 | CG-08 | CG-09 |
| [MCF-NET-008](#mcf-net-008) | Collective Communication Performance | DETECTIVE | EFFECTIVENESS | AL5 | CG-08 | — |
| [MCF-NET-009](#mcf-net-009) | Storage Fabric | PREVENTIVE | EFFECTIVENESS | AL5 | CG-08 | CG-10 |
| [MCF-NET-010](#mcf-net-010) | Frontend Network | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-08 |
| [MCF-NET-011](#mcf-net-011) | Service Gateways | DETECTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-NET-012](#mcf-net-012) | Traffic Isolation | PREVENTIVE | EFFECTIVENESS | AL5 | — | CG-09, CG-08, CG-15 |
| [MCF-NET-013](#mcf-net-013) | Management Separation | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-15, CG-08 |
| [MCF-NET-014](#mcf-net-014) | Console Access | CORRECTIVE | IMPLEMENTATION | AL3 | — | CG-10, CG-15 |
| [MCF-NET-015](#mcf-net-015) | OOB Resilience | RECOVERY | RESILIENCE | AL5 | CG-10 | CG-15, CG-03 |
| [MCF-NET-016](#mcf-net-016) | Break-Glass Access | RECOVERY | EFFECTIVENESS | AL5 | — | CG-15, CG-10 |
| [MCF-NET-017](#mcf-net-017) | Cabling Standards | DIRECTIVE | DESIGN | AL2 | — | CG-08 |
| [MCF-NET-018](#mcf-net-018) | Optics Compatibility | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-08, CG-03 |
| [MCF-NET-019](#mcf-net-019) | Cross-Connect Control | PREVENTIVE | OPERATION | AL4 | — | CG-14, CG-08 |
| [MCF-NET-020](#mcf-net-020) | Path Documentation | DETECTIVE | IMPLEMENTATION | AL3 | — | CG-02, CG-03, CG-10 |
| [MCF-NET-021](#mcf-net-021) | Controller Resilience | PREVENTIVE | EFFECTIVENESS | AL5 | — | CG-08, CG-09, CG-10 |
| [MCF-NET-022](#mcf-net-022) | Configuration Management | PREVENTIVE | OPERATION | AL4 | CG-14 | CG-08, CG-10 |
| [MCF-NET-023](#mcf-net-023) | Flow Telemetry | DETECTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-NET-024](#mcf-net-024) | Time and Core Services | PREVENTIVE | EFFECTIVENESS | AL5 | — | CG-08, CG-03, CG-10 |

## NET-01 Scale-up and scale-out fabrics

### MCF-NET-001

**Fabric Topology** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure the scale-up and scale-out fabrics are built to an approved topology whose bisection bandwidth, tiering, rail assignment and endpoint attachment match what the declared training and inference Service Outcomes require.

**Requirement.** The network architecture owner shall maintain an approved topology design for every back-end (scale-out) fabric and scale-up domain in scope, stating the topology class (for example rail-optimised multi-plane, two-tier leaf-spine or three-tier fat-tree/Clos, or rack-scale scale-up domain), switch radix, tier count, rail and plane assignment, endpoint-to-leaf mapping and the design bisection bandwidth per Capability Instance. The fabric operations lead shall reconcile the as-built fabric (LLDP or subnet-manager discovered topology, cabling records and port maps) to the approved design at commissioning and after every material change, and shall record every deviation as either an approved variance or a Finding.

**Assessment criteria**

1. An approved topology design exists for each in-scope fabric and identifies topology class, tiers, radix, planes/rails, endpoint attachment and design bisection bandwidth.
2. Discovered topology (LLDP neighbour tables, InfiniBand subnet-manager topology dump or controller inventory) reconciles to the design with all mismatched, missing or miswired links listed and dispositioned.
3. Each accelerator NIC port is attached to the rail/plane and leaf required by the design; rail-mapping errors are zero or individually approved.
4. Design bisection bandwidth and per-endpoint injection bandwidth are traceable to the Service Outcome performance requirement for the Capability Instance.
5. Topology changes since the last reconciliation are linked to approved change records.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Rail-mapping conformance | % of accelerator ports on design rail/leaf | 100 (illustrative) | Rail-optimised designs assume ordinal NIC n connects to rail n; any deviation alters collective paths. Site-specific. |
| Maximum topology reconciliation age | days | 90 (illustrative) | Capability-profile parameter; shorten where change rate is high. |

**Minimum evidence**

- Approved fabric topology design and high-level design document, with version and approver
- Discovered topology export (LLDP tables, subnet-manager topology file or fabric-controller inventory) dated within the reconciliation window
- Automated or manual reconciliation report of discovered versus designed links and port maps
- Rail/plane mapping table per node type
- Change records for topology modifications since the previous reconciliation

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Point-in-time reconciliation no older than the reconciliation-age parameter, plus change history since the previous reconciliation. |
| independence | Reconciliation produced from machine-discovered topology, not from the design author's own drawings; reviewed by an engineer other than the design author. |
| mandatoryItems | Discovered topology export; Design-to-as-built reconciliation report |
| acceptableAlternatives | Witnessed physical port audit of a statistically justified sample of racks where automated discovery is unavailable, with the sample rationale recorded |
| unknownEffect | US4: CG-08 cannot PASS while as-built topology of a gate-critical fabric is unreconciled; record UNKNOWN U5 or U3 as applicable. |
| reassessmentTriggers | Fabric expansion or re-cabling; Change of topology class or tier count; Major NOS or subnet-manager upgrade altering discovery; Discovery showing unreconciled links |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS, SAMPLING, INSPECTION

**Assessment procedure**

1. Obtain the approved topology design and confirm its version applies to the assessed Capability Instance.
2. Extract discovered topology from switches or the subnet manager using read-only collection.
3. Run or reperform the reconciliation of discovered links, port speeds and neighbours against design port maps.
4. Verify rail and plane assignment for a sample of nodes of each type, including recently replaced nodes.
5. Trace design bisection bandwidth to the Service Outcome performance requirement and to NET-003 oversubscription analysis.
6. Disposition every mismatch as approved variance or Finding and record residual UNKNOWNs.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (CRITICAL); CG-02 Boundary and architecture integrity (SUPPORTING)

**Applicability.** Applies to every back-end scale-out fabric (InfiniBand or Ethernet/RoCEv2) and every scale-up domain supporting an in-scope Capability Instance. Front-end and storage networks are covered by NET-009 and NET-010. Not applicable to single-node inference with no inter-node fabric, subject to approved rationale.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, CHANGE · **Operating states.** NORMAL, MAINTENANCE, TRANSITION

**Failure modes addressed.** Miswired or missing links reducing effective bisection bandwidth; Rail-mapping error forcing cross-rail traffic through spine; Undocumented topology drift after expansion; Mixed link speeds negotiated below design rate

**Testing safety.** Topology collection shall use read-only interfaces and credentials. Re-cabling or port disablement to verify mapping shall not be performed on a production fabric without an approved change and workload owner consent.

**UNKNOWN rule.** If discovered topology cannot be obtained for a gate-critical fabric, or reconciliation coverage is below the full fabric without a justified sample, record a US4 UNKNOWN against CG-08 and do not infer conformance from design documents.

**Ontology classes.** ArchitectureSnapshot, InfrastructureSystem, AssetInstance, Interface, CapacityAssertion · **Related controls.** MCF-NET-002, MCF-NET-003, MCF-NET-020, MCF-CMP-005, MCF-CMP-006

**Informative references.** InfiniBand Trade Association, InfiniBand Architecture Specification (Volumes 1 and 2); InfiniBand Trade Association, RoCEv2 annex to the InfiniBand Architecture Specification; IETF RFC 7938 (Use of BGP for routing in large-scale data centres); AIDCF-013 (AI Data Centre Assurance Reference Architecture)

### MCF-NET-002

**Path Diversity** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that logical redundancy in fabrics, inter-hall links and WAN/DCI connections is matched by physically diverse paths, so a single cable route, conduit, carrier or building entry cannot defeat redundant connectivity.

**Requirement.** The network architecture owner shall define, for each redundant path group (spine uplinks between halls, storage and front-end uplinks, WAN and data-centre interconnect circuits, OOB uplinks), the required diversity attributes: separate cable routes and containment, separate building entries, separate carriers or carrier-neutral dark-fibre routes, and separate optical line systems where DWDM is used. The connectivity manager shall obtain route evidence (carrier KMZ or route maps, cable-route surveys, containment records) for each path and shall record every shared segment, shared conduit, shared meet-me room or shared upstream carrier as a common-mode dependency.

**Assessment criteria**

1. Each redundant path group has documented diversity requirements derived from the outcome criticality.
2. Route evidence for each external circuit identifies building entry, route and any shared segments to a defined granularity.
3. Intra-site redundant trunks are routed in separate containment or the shared section is analysed and accepted.
4. Carrier diversity accounts for wholesale or tail-circuit sharing (diverse brand on a shared underlying route is not treated as diverse).
5. Shared segments are registered as common-mode dependencies with owners and linked to DEP-007.
6. Diversity is re-verified after carrier grooming or re-routing notices.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Minimum physical separation between diverse routes | m | Site-specific; set by risk analysis (illustrative: separate containment and entry points) | Capability-profile parameter; no universal distance applies. |
| Route evidence age | months | 12 (illustrative) | Carriers re-groom circuits; evidence ages. |

**Minimum evidence**

- Path-group register listing redundant groups and diversity requirements
- Carrier route documentation (maps, KMZ or route letters) for WAN/DCI circuits
- Internal cable-route and containment drawings for inter-hall trunks
- Common-mode analysis of shared segments with dispositions
- Carrier notifications of re-routing and the review of each

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | Current route evidence within the evidence-age parameter; carrier change notices for the prior 12 months. |
| independence | External route claims corroborated by a second source (site walk-down of entries, independent route survey, or carrier-signed route letter). |
| mandatoryItems | Route evidence for each external circuit in a redundant group; Shared-segment register |
| acceptableAlternatives | Where a carrier will not disclose routes, a contractual diversity guarantee plus an independent survey of building entry and first-kilometre routes, with the remainder recorded as UNKNOWN U2 |
| unknownEffect | US3 by default; US4 against CG-03 where the undisclosed segment carries the only DCI path for a gate-critical outcome. |
| reassessmentTriggers | Carrier grooming or re-routing notice; New circuit or carrier; Civil works near cable routes; Incident affecting two nominally diverse paths |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, ANALYSIS, RECONCILIATION, INQUIRY

**Assessment procedure**

1. List all redundant path groups and their stated diversity requirements.
2. Collect route evidence for each member path and overlay routes to identify shared segments, entries and nodes.
3. Walk down building entries, risers and inter-hall containment for a sample of paths.
4. Check whether diverse carriers share wholesale tails, ducts or landing points.
5. Confirm each shared segment is in the dependency register with an owner and disposition.
6. Review carrier change notices for unreviewed re-routing.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to every network path relied upon as redundant for an in-scope outcome, including WAN/DCI used for multi-site training, replication or alternate capacity. Not applicable to paths whose loss is explicitly tolerated by the Service Outcome.

**Lifecycle stages.** DESIGN, BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Single excavation severing both 'diverse' DCI circuits; Both trunks in one cable tray exposed to one fire; Diverse carriers sharing one wholesale route; Silent carrier re-grooming removing diversity

**Testing safety.** Route verification is non-intrusive. Failover tests between diverse circuits shall be scheduled under change control with the service owner, and shall not be performed during declared DEGRADED states.

**UNKNOWN rule.** If a route for any member of a redundant path group cannot be evidenced, record UNKNOWN U2 or U10 and treat the group as non-diverse for CG-03 and blast-radius analysis until evidenced.

**Ontology classes.** Dependency, FaultDomain, Interface, Resource · **Related controls.** MCF-DEP-007, MCF-DEP-010, MCF-NET-020, MCF-RES-011, MCF-PHY-010

**Informative references.** ANSI/TIA-942 (Telecommunications infrastructure standard for data centres); EN 50600 series / ISO/IEC 22237 series (Data centre facilities and infrastructures); AIDCF-004 (Threat, Hazard and Failure Model)

### MCF-NET-003

**Oversubscription** · PREVENTIVE · claim type DESIGN · required AL2

**Objective.** Ensure each fabric tier's oversubscription ratio is a deliberate design decision justified against the expected traffic matrix of the declared workloads, so collective and storage traffic are not throttled by uplink scarcity.

**Requirement.** The network architecture owner shall state the design oversubscription ratio at every tier boundary (leaf-to-spine, spine-to-superspine, pod-to-core, storage and front-end uplinks) and shall justify each ratio against the traffic matrix of the declared workloads, including all-reduce, all-to-all (for example expert-parallel) and checkpoint bursts. The fabric operations lead shall re-derive effective oversubscription after link failures, partial builds and planned maintenance, and shall record the minimum tolerated effective ratio for each Service Outcome.

**Assessment criteria**

1. Design oversubscription ratios are stated per tier and per fabric.
2. Each ratio is justified by a traffic-matrix or workload analysis covering the collective patterns and checkpoint traffic of declared workloads.
3. Effective oversubscription under N-1 uplink and N-1 spine conditions is calculated and compared to the tolerated ratio.
4. Partial-build or phased-expansion states that temporarily increase oversubscription are identified with accepted limitations.
5. Back-end fabrics designated non-blocking are verified to have uplink capacity equal to downlink capacity at each tier.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Back-end fabric design oversubscription | ratio (downlink:uplink) | 1:1 (illustrative) | Common design choice for large training fabrics; site and workload specific. |
| Front-end/storage uplink oversubscription | ratio | Workload-derived (illustrative 3:1) | Capability-profile parameter justified by traffic analysis. |
| Minimum tolerated effective ratio under N-1 | ratio | Set per Service Outcome (illustrative 1.15:1 for back-end) | Derived from performance outcome tolerance. |

**Minimum evidence**

- Fabric design ratio table per tier
- Traffic-matrix or workload communication analysis for declared workloads
- N-1 effective-capacity calculation
- Phased-build limitation statements

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C2 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE; TRANSITION |
| periodCoverage | Current design baseline; reconfirmed at each fabric expansion phase. |
| independence | Analysis reviewed by a network engineer independent of the design author or by the workload performance team. |
| mandatoryItems | Per-tier ratio table; Workload-justification analysis |
| acceptableAlternatives | Simulation or emulation results from a vendor or internal fabric model, provided inputs are traceable to declared workloads |
| unknownEffect | US3: unjustified ratios cap performance assurance; CG-08 SUPPORTING evaluation required. |
| reassessmentTriggers | Change of workload mix (for example introduction of expert-parallel models); Fabric expansion phase; Change of link speed at one tier only |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INQUIRY

**Assessment procedure**

1. Obtain the per-tier ratio table and the topology design from NET-001.
2. Recompute ratios from port counts and speeds.
3. Review the workload traffic analysis and confirm it covers declared collectives and checkpoint bursts.
4. Calculate effective ratios under N-1 uplink and N-1 spine and compare to tolerated values.
5. Record limitations for phased-build states.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to every multi-tier fabric in scope. Single-tier fabrics need only the endpoint-to-switch capacity check.

**Lifecycle stages.** PLAN, DESIGN, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, TRANSITION

**Failure modes addressed.** Uplink scarcity throttling all-to-all traffic; Checkpoint burst saturating storage uplinks; Ratio degrading beyond tolerance after spine loss; Phased build left in temporary state

**Testing safety.** Analytical; no production traffic injection is required. Synthetic load tests belong to NET-007/NET-008 and require scheduling with workload owners.

**UNKNOWN rule.** If no traffic analysis exists for a declared workload class, record UNKNOWN U1 against the performance outcome and do not accept a ratio solely on vendor reference designs.

**Ontology classes.** CapacityAssertion, InfrastructureSystem, OperatingState · **Related controls.** MCF-NET-001, MCF-NET-008, MCF-NET-009, MCF-CAP-006, MCF-STO-008

**Informative references.** IETF RFC 7938 (Use of BGP for routing in large-scale data centres); InfiniBand Trade Association, InfiniBand Architecture Specification (Volumes 1 and 2); AIDCF-013 (AI Data Centre Assurance Reference Architecture)

### MCF-NET-004

**Fabric Fault-Domain Design** · PREVENTIVE · claim type RESILIENCE · required AL5

**Objective.** Ensure fabric failure domains (switch, rail, plane, pod, spine group, subnet manager, controller, power feed and cooling zone) are designed so that any single credible failure stays within a blast radius the Service Outcome tolerates.

**Requirement.** The network architecture owner shall define the fault domains of each fabric, including each switch, rail, plane, pod, spine group, subnet manager or fabric controller instance, and the power and cooling zones serving fabric equipment, and shall state for each the maximum affected endpoints and the resulting outcome impact. The fabric operations lead shall demonstrate, by controlled test or by analysed incident, that loss of a leaf, a spine, a rail or plane, a subnet-manager master and one power feed to a switch row each stay within the declared blast radius, and that fabric equipment does not share an undisclosed power or cooling fault domain with its own redundancy.

**Assessment criteria**

1. Fault-domain register for each fabric lists domain, members, maximum affected endpoints and tolerated impact.
2. Redundant fabric elements (spines, planes, subnet managers, controllers) are not co-located in a single power distribution path, cooling zone or rack without accepted rationale.
3. Loss of a single leaf, spine, plane or subnet-manager master has been tested or observed, and the measured effect (endpoints lost, job failures, reroute time) is within declared tolerance.
4. Fabric behaviour that widens a failure (for example PFC pause propagation, routing reconvergence storms or subnet-manager sweep load) is analysed and bounded.
5. Fault domains reconcile to CMP-008 compute fault domains and RES-005 site fault domains.
6. Residual multi-element failure scenarios outside tolerance are recorded with accepted limitations.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum endpoints affected by a single switch failure | accelerator ports | Equal to leaf downlink count (illustrative) | Derived from topology; outcome-specific tolerance. |
| Maximum reroute/reconvergence time after single spine loss | s | Set by job collective timeout margin (illustrative 30) | Must be below framework collective timeouts; site-specific. |
| Subnet-manager failover time | s | Vendor- and scale-dependent (illustrative 60) | Capability-profile parameter verified by test. |

**Minimum evidence**

- Fabric fault-domain register and blast-radius analysis
- Power and cooling mapping of fabric switches, subnet managers and controllers
- Test records or incident analyses for leaf, spine, plane and subnet-manager failure
- PFC-propagation and reconvergence analysis
- Reconciliation to compute and site fault-domain models

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T3 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE; FAILED; RECOVERY |
| periodCoverage | Tests or incidents within the previous 24 months and after any topology class change. |
| independence | Test witnessed by a party independent of the fabric operations team, or independent review of incident analysis. |
| mandatoryItems | Fault-domain register; At least one test or analysed incident per fault-domain class; Power/cooling co-location analysis |
| acceptableAlternatives | Pre-production or staging fabric test at representative scale, with a documented representativeness argument |
| unknownEffect | US4: CG-09 cannot PASS while a gate-critical fabric's single-failure blast radius is untested and unanalysed. |
| reassessmentTriggers | Topology or scale change; Subnet-manager or controller architecture change; Power or cooling re-zoning of network rows; Incident with impact beyond the declared domain |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, TEST, SCENARIO_EXERCISE, RECONCILIATION

**Assessment procedure**

1. Review the fault-domain register and confirm completeness against NET-001 topology.
2. Map each fabric element to its power path and cooling zone and identify co-location of redundant elements.
3. Review test plans and results for single-element failures, checking measured blast radius and reroute time.
4. Analyse PFC pause propagation and routing reconvergence as failure-widening mechanisms.
5. Reconcile fabric fault domains with CMP-008 and RES-005.
6. Record residual scenarios outside tolerance and their acceptance status.

**Gate mappings.** CG-09 Failure containment (CRITICAL); CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to all fabrics supporting in-scope Capability Instances. For fabrics where loss of any element is tolerated by job restart from checkpoint, the analysis still applies but tolerance may be expressed as lost work.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, FAILED, RECOVERY

**Failure modes addressed.** Both subnet managers on one PDU; Spine group sharing one cooling zone; PFC storm spreading a single NIC fault fabric-wide; Reconvergence exceeding collective timeouts and killing all jobs

**Testing safety.** Element-failure tests on a production fabric (switch power-off, link shutdown, subnet-manager failover) are disruptive and shall only be performed with written authorisation from the service owner and network change board, a rollback plan, workload drain or owner consent, and monitoring in place. Power-feed removal tests require electrical authorisation under OPS-007 permit-to-work.

**UNKNOWN rule.** Where blast radius has only been asserted by the vendor and not tested or observed locally, record UNKNOWN U8 (method uncertain) at US4 against CG-09.

**Ontology classes.** FaultDomain, FailureScenario, Dependency, TestRecord, InfrastructureSystem · **Related controls.** MCF-CMP-008, MCF-RES-005, MCF-RES-007, MCF-NET-021, MCF-POW-015

**Informative references.** InfiniBand Trade Association, InfiniBand Architecture Specification (Volumes 1 and 2); IEEE 802.1Qbb (Priority-based Flow Control); IETF RFC 7938 (Use of BGP for routing in large-scale data centres); AIDCF-004 (Threat, Hazard and Failure Model); AIDCF-013 (AI Data Centre Assurance Reference Architecture)

## NET-02 Performance and congestion control

### MCF-NET-005

**Latency Baseline** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure the fabric has a measured latency baseline (idle and loaded, per path class) against which degradation can be detected and Service Outcome performance claims tested.

**Requirement.** The fabric operations lead shall establish and maintain latency baselines for each path class (intra-leaf, intra-pod, cross-spine, cross-plane, storage path, front-end path) including idle round-trip time, loaded tail latency at defined percentiles and switch-hop count, measured with a repeatable method (for example perftest-class RDMA latency tools or active probing). The fabric operations lead shall alert on deviation from baseline beyond a defined threshold and shall re-baseline after any material NOS, firmware, topology or congestion-control change.

**Assessment criteria**

1. Baselines exist per path class with method, tool, message size and date recorded.
2. Tail latency percentiles are captured under representative load, not only idle conditions.
3. Continuous or periodic probing compares current latency to baseline and alerts on deviation.
4. Re-baselining occurred after each material change in the period.
5. Deviations exceeding the threshold in the period were investigated and closed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Latency deviation alert threshold | % above baseline at p99 | 25 (illustrative) | Capability-profile parameter tuned to measurement noise. |
| Baseline percentile set | percentiles | p50, p99, p99.9 (illustrative) | Tail latency drives synchronous collective step time. |

**Minimum evidence**

- Baseline report per path class with method details
- Probe telemetry for the assessment period
- Alert and investigation records for deviations
- Change-linked re-baseline records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | Representative operating period of at least 90 days (illustrative) including a maintenance window. |
| independence | Telemetry extracted directly from the probe system by the assessor, not summarised by the operations team. |
| mandatoryItems | Baseline report; Probe telemetry for the period |
| acceptableAlternatives | Workload-derived step-time telemetry where synthetic probes are not permitted, with mapping to path classes |
| unknownEffect | US2: absent baselines reduce confidence in performance claims; US3 if a performance Service Outcome depends on latency tolerance. |
| reassessmentTriggers | NOS or NIC firmware change; Congestion-control parameter change; Topology change; Sustained deviation alert |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, SAMPLING, OBSERVATION

**Assessment procedure**

1. Review baseline reports for method repeatability and coverage of path classes.
2. Sample probe telemetry across the period and compare against baselines.
3. Trace deviations to alerts and investigation records.
4. Verify re-baselining after material changes recorded in NET-022.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to latency-sensitive fabrics supporting training or low-latency inference outcomes. May be limited to idle baselines for batch-only storage networks with approved rationale.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Silent latency regression after firmware update; Degraded optic causing retransmission-driven tail latency; Unnoticed path asymmetry after reroute

**Testing safety.** Active probes shall be rate-limited and run in a dedicated traffic class; loaded-latency measurements on production fabrics require scheduling with workload owners.

**UNKNOWN rule.** If baselines predate the current NOS/firmware baseline, treat them as stale (U3) and do not use them to support performance claims.

**Ontology classes.** CapacityAssertion, EvidenceObject, InfrastructureSystem · **Related controls.** MCF-NET-006, MCF-NET-008, MCF-NET-023, MCF-CMP-020

**Informative references.** InfiniBand Trade Association, InfiniBand Architecture Specification (Volumes 1 and 2); InfiniBand Trade Association, RoCEv2 annex to the InfiniBand Architecture Specification; AIDCF-013 (AI Data Centre Assurance Reference Architecture)

### MCF-NET-006

**Loss and Retransmission** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure packet loss, link errors and transport retransmissions are monitored against thresholds so that degrading links, optics and lossless-class failures are detected before they defeat job progress.

**Requirement.** The fabric operations lead shall monitor, per port and per traffic class, pre-FEC and post-FEC bit error indicators, FEC corrected and uncorrectable codeword counts, CRC/symbol errors, link flaps, discards, and RDMA transport retransmission and out-of-sequence counters at NICs, against defined thresholds. The fabric operations lead shall automatically isolate or drain links that exceed uncorrectable-error or flap thresholds, shall track each to closure, and shall verify that the lossless traffic class shows no congestion drops under normal operation.

**Assessment criteria**

1. Thresholds are defined for FEC uncorrectable codewords, symbol/CRC errors, link flaps and NIC retransmission rates.
2. Collection covers all switch ports and NICs in the fabric with gaps listed.
3. Links breaching thresholds were isolated or drained and tracked through remediation in the period.
4. The lossless (RDMA) traffic class shows zero congestion drops in normal operation, or each drop event is explained.
5. Trend analysis identifies slow-burn degradation (rising corrected-error rates) before uncorrectable thresholds are reached.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Link flap isolation threshold | flaps per hour | 3 (illustrative) | Capability-profile parameter. |
| Post-FEC uncorrectable codeword threshold | count per interval | Any non-zero sustained (illustrative) | Post-FEC errors become packet loss; vendor guidance applies. |
| Pre-FEC BER warning threshold | BER | Vendor/PHY specific (illustrative: one order of magnitude below FEC limit) | Set from IEEE 802.3 FEC capability and vendor guidance. |

**Minimum evidence**

- Threshold configuration in monitoring system
- Error counter telemetry for all ports for the period
- Auto-isolation or drain events and tickets
- Lossless-class drop counters
- Trend reports

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | At least 90 days (illustrative) of continuous counter data. |
| independence | Counter data sampled directly from devices or the telemetry store by the assessor. |
| mandatoryItems | Port error telemetry; Isolation/drain ticket history |
| acceptableAlternatives | Periodic counter snapshots at defined intervals where streaming telemetry is unavailable, with interval justification |
| unknownEffect | US3: unmonitored error classes may hide job-defeating link faults; CG-08 SUPPORTING evaluation. |
| reassessmentTriggers | New optic or cable type; NIC firmware change; Rise in job failures attributed to network; Threshold change |

**Assessment methods.** ANALYSIS, SAMPLING, DOCUMENT_REVIEW, OBSERVATION

**Assessment procedure**

1. Review threshold definitions against PHY and vendor guidance.
2. Confirm telemetry coverage across switch ports and NICs and list gaps.
3. Sample breaching links and trace isolation, ticket and remediation.
4. Inspect lossless-class drop counters and explain each event.
5. Review trend analysis for slow-burn degradation detection.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all back-end, storage and front-end fabrics. Lossless-class criteria apply only to fabrics carrying RDMA over Ethernet or InfiniBand.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Marginal optic causing intermittent uncorrectable errors and job stalls; Link flapping triggering repeated reroute; Lossless-class drops due to misconfigured PFC headroom; Slow optical degradation unnoticed

**Testing safety.** Monitoring review only. Deliberate error injection or link disablement requires change approval and workload owner consent.

**UNKNOWN rule.** If NIC-side retransmission counters are not collected, record U5 coverage gap; switch-side counters alone shall not support a claim of transport health.

**Ontology classes.** FailureMode, AssetInstance, EvidenceObject, Event · **Related controls.** MCF-NET-005, MCF-NET-007, MCF-NET-018, MCF-NET-023, MCF-CMP-019

**Informative references.** IEEE 802.3 (Ethernet, including optical PHY and FEC clauses); InfiniBand Trade Association, InfiniBand Architecture Specification (Volumes 1 and 2); InfiniBand Trade Association, RoCEv2 annex to the InfiniBand Architecture Specification; IEEE 802.1Qbb (Priority-based Flow Control)

### MCF-NET-007

**Congestion Control** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure congestion control and lossless configuration (ECN marking, PFC, DCQCN-style or vendor rate control, adaptive routing, InfiniBand credit-based flow control) keep fabrics stable under incast and many-to-one load, and that lossless-mode hazards such as PFC storms and deadlocks are prevented or contained.

**Requirement.** The network architecture owner shall define a congestion-control design per fabric stating traffic-class mapping, ECN marking thresholds, PFC enablement and headroom per priority, PFC watchdog behaviour, end-host rate-control algorithm and parameters, and adaptive routing settings, and shall analyse the design for cyclic buffer dependency (PFC deadlock) and pause-storm propagation. The fabric operations lead shall verify by controlled test that incast and congestion scenarios representative of declared workloads do not cause lossless-class drops, sustained pause propagation beyond the congested port, or deadlock, and that the PFC watchdog detects and breaks a stuck-pause condition within the configured time.

**Assessment criteria**

1. A congestion-control design states class mapping, ECN thresholds, PFC priorities and headroom, watchdog settings, NIC rate-control parameters and routing behaviour.
2. Device configurations across the fabric match the design for all congestion-related parameters (sampled or fully reconciled).
3. Deadlock analysis demonstrates absence of cyclic buffer dependency under normal and failure routing, or mitigations (for example limiting lossless classes, routing restrictions) are in place.
4. Incast/congestion tests representative of declared workloads show no lossless-class drops and bounded pause propagation.
5. A simulated stuck-pause (pause-storm) condition is detected and isolated by the PFC watchdog or equivalent within the configured time.
6. ECN marking and congestion notification counters are monitored and show expected behaviour in operation.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| PFC watchdog detection time | ms | Vendor default unless tuned (illustrative 200) | Configured per NOS; verified by test. |
| Maximum tolerated pause propagation | hops from congestion point | 1 (illustrative) | Design objective to keep pause local. |
| Lossless traffic classes | count | 1 or 2 (illustrative) | Fewer lossless classes reduce deadlock and headroom exposure. |

**Minimum evidence**

- Congestion-control design document
- Configuration reconciliation of ECN, PFC, headroom, watchdog and NIC rate-control settings
- Deadlock/cyclic-dependency analysis
- Incast and pause-storm test plans and results
- Operational ECN/PFC/CNP counter telemetry

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | Tests within the previous 12 months and after any congestion-control parameter or NOS change; 90 days (illustrative) of counter telemetry. |
| independence | Test designed or witnessed by an engineer independent of the person who tuned the parameters. |
| mandatoryItems | Configuration reconciliation; Incast test results; Pause-storm/watchdog test result |
| acceptableAlternatives | Representative staging-fabric tests with identical NOS, NIC firmware and parameters where production testing is not authorised, with representativeness argument |
| unknownEffect | US4: CG-08 cannot PASS for an RDMA-over-Ethernet fabric while lossless behaviour under congestion is untested. |
| reassessmentTriggers | NOS or NIC firmware change; Change of ECN/PFC/rate-control parameters; Addition of lossless traffic class; Observed pause storm or deadlock |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS, TEST, REPERFORMANCE

**Assessment procedure**

1. Review the congestion-control design and its rationale.
2. Reconcile congestion parameters across all fabric devices and NICs, recording drift.
3. Review deadlock analysis including failure-routing cases.
4. Review or witness incast tests and evaluate drops, pause propagation and job-level effect.
5. Review or witness a controlled pause-storm test and confirm watchdog action.
6. Sample operational counters for unexplained pause or drop events.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (CRITICAL); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to every fabric carrying RDMA (RoCEv2, InfiniBand) or other congestion-sensitive collective traffic. For InfiniBand, PFC criteria are replaced by credit-based flow control and adaptive-routing configuration review.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** PFC storm from a malfunctioning NIC halting a pod; PFC deadlock from cyclic buffer dependency after a routing change; Insufficient headroom causing lossless drops; ECN thresholds too high leading to buffer exhaustion; Parameter drift between switches

**Testing safety.** Incast and pause-storm tests can stall production fabrics and shall only be run with explicit written authorisation from the service owner and network change board, in a scheduled window, with the workload drained or isolated, the watchdog verified enabled beforehand and an abort criterion defined.

**UNKNOWN rule.** If NIC-side rate-control parameters cannot be extracted, record U2 and treat the end-to-end congestion design as unverified.

**Ontology classes.** Safeguard, InfrastructureSystem, FailureMode, TestRecord · **Related controls.** MCF-NET-006, MCF-NET-008, MCF-NET-004, MCF-NET-022, MCF-CMP-012

**Informative references.** IEEE 802.1Qbb (Priority-based Flow Control); IEEE 802.1Qaz (Enhanced Transmission Selection and DCBX); IETF RFC 3168 (Explicit Congestion Notification); InfiniBand Trade Association, RoCEv2 annex to the InfiniBand Architecture Specification; InfiniBand Trade Association, InfiniBand Architecture Specification (Volumes 1 and 2); Ultra Ethernet Consortium specification (UEC 1.0)

### MCF-NET-008

**Collective Communication Performance** · DETECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure collective operations (all-reduce, all-gather, reduce-scatter, all-to-all) achieve the bus bandwidth and step-time required by declared training and inference outcomes at full and degraded scale.

**Requirement.** The fabric operations lead shall run a defined collective benchmark suite (for example NCCL- or RCCL-class tests and a representative workload proxy) at commissioning, after every material fabric, NIC or library change and at a defined periodic interval, covering message sizes and scales used by declared workloads, and shall compare achieved bus bandwidth and latency to acceptance targets. The capability owner shall set the acceptance targets from the performance Service Outcome and shall accept or reject results for degraded scale (for example one plane or one spine unavailable).

**Assessment criteria**

1. A collective benchmark suite is defined with operations, message sizes, scales, library versions and environment variables recorded.
2. Acceptance targets per operation and scale are approved by the capability owner and traceable to the performance Service Outcome.
3. Current results at full scale meet targets, or shortfalls are recorded as Findings.
4. Results at defined degraded scale meet the degraded targets.
5. Benchmarks were rerun after every material change and at the periodic interval.
6. Per-node or per-rail outliers are identified and remediated.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Collective acceptance target | % of design bus bandwidth | 90 (illustrative) | Capability-profile parameter derived from performance outcome. |
| Benchmark periodic interval | days | 30 (illustrative) | Detects slow drift. |

**Minimum evidence**

- Benchmark suite definition
- Approved acceptance targets
- Benchmark results with raw outputs and environment captures
- Degraded-scale results
- Outlier remediation records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; TRANSITION |
| periodCoverage | Most recent periodic run within the interval parameter, and runs after each material change in the previous 12 months. |
| independence | Assessor reperforms or witnesses at least one benchmark run, or raw outputs are independently parsed. |
| mandatoryItems | Raw benchmark outputs; Approved targets |
| acceptableAlternatives | Production job step-time telemetry from instrumented workloads, where synthetic benchmarks are impractical, with mapping to operations and scales |
| unknownEffect | US4: CG-08 cannot PASS while collective performance at required scale is unmeasured. |
| reassessmentTriggers | Collective library upgrade; NIC firmware or driver change; Topology or congestion-control change; Regression detected in workloads |

**Assessment methods.** TEST, REPERFORMANCE, ANALYSIS, DOCUMENT_REVIEW

**Assessment procedure**

1. Review the benchmark suite definition against declared workload communication patterns.
2. Confirm targets are approved and traceable to Service Outcomes.
3. Parse raw outputs and verify reported bus bandwidth and latency.
4. Witness or reperform a benchmark run at representative scale.
5. Review degraded-scale results and acceptance.
6. Trace outliers to remediation.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (CRITICAL)

**Applicability.** Applies to multi-node training and distributed inference Capability Instances. Not applicable where outcomes do not depend on inter-node collectives.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, TRANSITION

**Failure modes addressed.** Collective bandwidth regression after library upgrade; Single bad node or rail throttling a whole job; Degraded-scale performance below outcome tolerance; Environment misconfiguration bypassing RDMA

**Testing safety.** Full-scale benchmarks consume the cluster and shall be scheduled with the capability owner; degraded-scale tests that disable a plane or spine are disruptive and require change-board authorisation.

**UNKNOWN rule.** Benchmarks run with library versions or environment settings different from production are not representative (U5) and shall not support a CONFORMING result.

**Ontology classes.** TestRecord, CapacityAssertion, ServiceOutcome, InfrastructureSystem · **Related controls.** MCF-NET-003, MCF-NET-005, MCF-NET-007, MCF-CMP-020, MCF-CAP-006

**Informative references.** InfiniBand Trade Association, InfiniBand Architecture Specification (Volumes 1 and 2); InfiniBand Trade Association, RoCEv2 annex to the InfiniBand Architecture Specification; Ultra Ethernet Consortium specification (UEC 1.0); AIDCF-013 (AI Data Centre Assurance Reference Architecture)

## NET-03 Storage and service networks

### MCF-NET-009

**Storage Fabric** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure the storage network (dedicated or converged) delivers the throughput, latency and isolation needed for dataset reads and checkpoint write bursts without interfering with collective traffic.

**Requirement.** The network architecture owner shall define the storage network design: whether storage traffic uses a dedicated fabric, a dedicated plane or a separate traffic class on the compute fabric; the path from compute nodes to storage servers and metadata services; capacity per storage server; and the traffic-class and congestion policy that prevents checkpoint bursts from degrading collective traffic. The storage platform owner and fabric operations lead shall jointly test a synchronised checkpoint write and a dataset-read burst at declared scale and confirm achieved throughput and the effect on concurrent collective performance meet targets.

**Assessment criteria**

1. Storage network design states topology, traffic-class policy, capacity per storage target and metadata service paths.
2. Configured traffic-class and QoS settings match the design.
3. A synchronised checkpoint-write test at declared scale achieves the throughput needed to meet the checkpoint-time target.
4. Concurrent collective performance during the checkpoint burst stays within the tolerated degradation.
5. Storage metadata services are reachable over redundant paths with no single switch dependency.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Checkpoint write window | s | Derived from checkpoint size and goodput target (illustrative 120) | Capability-profile parameter; see RES-016. |
| Tolerated collective degradation during checkpoint | % bus bandwidth reduction | 10 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Storage network design and traffic-class policy
- QoS/traffic-class configuration extracts
- Checkpoint-burst and dataset-read test results
- Concurrent collective measurement during burst
- Metadata path redundancy analysis

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | Test within 12 months and after storage or network capacity change. |
| independence | Joint test witnessed by an assessor or a party independent of both storage and network teams. |
| mandatoryItems | Checkpoint-burst test result; Traffic-class configuration extract |
| acceptableAlternatives | Production checkpoint telemetry from large jobs showing achieved write throughput and concurrent step time |
| unknownEffect | US4: CG-08 cannot PASS while checkpoint-path throughput at declared scale is unverified (scenario X06). |
| reassessmentTriggers | Storage capacity or server change; Checkpoint size growth; Traffic-class change; Cluster expansion |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, TEST, ANALYSIS

**Assessment procedure**

1. Review storage network design and confirm path to metadata and data services.
2. Reconcile traffic-class configuration on switches and NICs.
3. Review or witness checkpoint-burst and dataset-read tests.
4. Measure or review collective performance during the burst.
5. Confirm metadata path redundancy.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (CRITICAL); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to any Capability Instance that reads training data or writes checkpoints over a network. Local-NVMe-only checkpointing still requires assessment of the path used to drain checkpoints to durable storage.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Checkpoint burst saturating shared uplinks (X06); Storage and collective traffic sharing a lossless class causing head-of-line blocking; Metadata service reachable via a single switch; Dataset-read starvation reducing accelerator utilisation

**Testing safety.** Checkpoint-burst tests load shared storage and may affect other tenants; schedule with the storage platform owner and notify affected service owners. Do not run destructive storage tests under this control.

**UNKNOWN rule.** If checkpoint throughput is only known from storage vendor specifications, record U8 and limit the claim to DESIGN.

**Ontology classes.** InfrastructureSystem, Interface, CapacityAssertion, TestRecord · **Related controls.** MCF-STO-005, MCF-STO-008, MCF-STO-017, MCF-NET-003, MCF-RES-016

**Informative references.** InfiniBand Trade Association, RoCEv2 annex to the InfiniBand Architecture Specification; IEEE 802.1Qaz (Enhanced Transmission Selection and DCBX); AIDCF-013 (AI Data Centre Assurance Reference Architecture)

### MCF-NET-010

**Frontend Network** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure the front-end network that carries user, API, inference request, orchestration and data-ingest traffic is built to an approved, redundant design and reconciles to it.

**Requirement.** The network architecture owner shall maintain an approved front-end network design covering node attachment (dual-homed or single-homed), routing protocol and ECMP design, uplinks to core and edge, load-balancer and gateway placement, and capacity for inference request and data-ingest peaks. The network operations manager shall reconcile as-built configuration and attachment to the design at commissioning and after material changes, and shall confirm that loss of a single front-end switch or uplink does not disconnect inference endpoints or orchestration control traffic beyond tolerance.

**Assessment criteria**

1. Approved front-end design exists with attachment, routing, capacity and redundancy stated.
2. As-built attachment and routing configuration reconcile to design.
3. Inference and orchestration endpoints have redundant attachment or an accepted single-homed rationale.
4. Capacity for declared inference request and ingest peaks is demonstrated by telemetry or test.
5. Single-switch or uplink failure has been tested or observed with effect within tolerance.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Front-end peak utilisation ceiling | % of uplink capacity | 70 (illustrative) | Capability-profile parameter for headroom. |

**Minimum evidence**

- Front-end network design
- Configuration and attachment reconciliation
- Utilisation telemetry at peak
- Failover test or incident record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | Reconciliation within 90 days (illustrative); peak telemetry over a representative period. |
| independence | Reconciliation reviewed by someone other than the implementer. |
| mandatoryItems | Configuration reconciliation; Attachment inventory |
| acceptableAlternatives | Witnessed sample inspection of attachment where automated inventory is incomplete |
| unknownEffect | US3: unreconciled front-end attachment may hide single points of failure for inference outcomes. |
| reassessmentTriggers | Front-end expansion; Routing design change; Load-balancer platform change |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS, SAMPLING

**Assessment procedure**

1. Review design and capacity basis.
2. Reconcile attachment and routing configuration.
3. Check redundancy of inference and orchestration endpoints.
4. Review peak utilisation telemetry.
5. Review failover evidence.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to front-end networks serving in-scope inference, orchestration and data-ingest. Where the front end is provided by a cloud or colocation provider, the provider boundary (DEP-018) governs evidence rights.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Single-homed inference gateways; ECMP imbalance saturating one uplink; Orchestration traffic lost on front-end switch failure

**Testing safety.** Front-end failover tests affect customer-facing inference and require service owner authorisation and customer-impact assessment.

**UNKNOWN rule.** Where provider-operated front-end segments cannot be inspected, record U2 and bound claims to the owned segment.

**Ontology classes.** InfrastructureSystem, Interface, ArchitectureSnapshot · **Related controls.** MCF-NET-011, MCF-NET-012, MCF-DEP-018, MCF-CAP-005

**Informative references.** IETF RFC 7938 (Use of BGP for routing in large-scale data centres); IEEE 802.1Q (Bridges and bridged networks); ANSI/TIA-942 (Telecommunications infrastructure standard for data centres)

### MCF-NET-011

**Service Gateways** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure gateways, load balancers, NAT, firewalls and edge routers on the service path operate within capacity, with health monitoring and redundancy that sustain inference and data-ingest outcomes.

**Requirement.** The network operations manager shall operate each service gateway cluster (load balancers, inference API gateways, NAT, edge routers and in-path firewalls) as a redundant pair or cluster with health checks, session-state handling and capacity monitoring, and shall define capacity thresholds for connections, throughput and TLS handshakes. The network operations manager shall review gateway capacity and failover events monthly and shall demonstrate that gateway failover occurred, or was tested, within tolerance in the assessment period.

**Assessment criteria**

1. Every in-path gateway is redundant or the single instance is an accepted limitation.
2. Capacity thresholds for connections, throughput and handshake rate are defined and monitored.
3. Health checks and failover triggers are configured and their behaviour is understood (state synchronisation, session loss).
4. Monthly capacity and event reviews occurred in the period with actions tracked.
5. Failover occurred or was tested in the period with measured disruption within tolerance.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Gateway capacity alert threshold | % of rated connections/throughput | 70 (illustrative) | Capability-profile parameter. |
| Tolerated failover disruption | s | Set by inference availability outcome (illustrative 5) | Derived from Service Outcome. |

**Minimum evidence**

- Gateway inventory with redundancy mode
- Capacity telemetry and thresholds
- Monthly review records
- Failover event or test records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | At least six months (illustrative) of capacity data and reviews. |
| independence | Assessor samples telemetry directly. |
| mandatoryItems | Capacity telemetry; Failover evidence |
| acceptableAlternatives | Provider service-level reports for managed gateways, with evidence rights per SUP-006 |
| unknownEffect | US3: unknown gateway capacity or failover behaviour conditions the inference availability claim. |
| reassessmentTriggers | Gateway platform change; Traffic growth beyond forecast; Failover anomaly |

**Assessment methods.** ANALYSIS, SAMPLING, DOCUMENT_REVIEW, INQUIRY

**Assessment procedure**

1. Inventory in-path gateways and redundancy modes.
2. Review thresholds and sample telemetry for breaches.
3. Review monthly reviews and actions.
4. Examine failover events or tests and measured disruption.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to gateways on the path of in-scope inference, API and data-ingest outcomes. Security policy content of firewalls is assessed under SEC-011.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Gateway connection-table exhaustion; Failover dropping all sessions; TLS handshake capacity exhausted at peak; Asymmetric routing through stateful gateways

**Testing safety.** Gateway failover tests disrupt sessions and require service owner authorisation and a customer communication plan where external customers are affected.

**UNKNOWN rule.** If session-state behaviour during failover is undocumented and untested, record U8 and limit availability claims.

**Ontology classes.** AssetInstance, CapacityAssertion, Event · **Related controls.** MCF-NET-010, MCF-SEC-011, MCF-OPS-022

**Informative references.** IETF RFC 7938 (Use of BGP for routing in large-scale data centres); AIDCF-013 (AI Data Centre Assurance Reference Architecture)

### MCF-NET-012

**Traffic Isolation** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure tenant, workload and traffic-class isolation on shared fabrics prevents one tenant or job from degrading, observing or reaching another beyond tolerance.

**Requirement.** The network architecture owner shall define the isolation model for shared fabrics: InfiniBand partition keys, VRFs, VXLAN/EVPN segments, VLANs, RDMA queue-pair and memory-region protections, traffic-class guarantees and rate limits. The fabric operations lead shall verify by test that endpoints in one isolation domain cannot reach endpoints in another, and that a saturating or misbehaving tenant cannot reduce another tenant's guaranteed bandwidth or trigger fabric-wide pause beyond the defined tolerance.

**Assessment criteria**

1. The isolation model states mechanisms, domains, and which traffic classes are shared.
2. Configuration of partitions, VRFs or segments reconciles to tenant assignments.
3. Reachability tests confirm no unintended cross-domain connectivity at layer 2, layer 3 and RDMA.
4. Performance-isolation tests show a saturating tenant does not reduce another tenant's guaranteed share beyond tolerance.
5. Tenant onboarding and offboarding updates isolation configuration and is verified.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Guaranteed bandwidth share per tenant class | % of link | Contract-specific (illustrative 25) | Set by tenant commitments (GOV-021). |
| Tolerated cross-tenant degradation | % throughput reduction | 5 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Isolation model
- Partition/VRF/segment configuration extracts with tenant mapping
- Reachability test results
- Performance-isolation test results
- Onboarding/offboarding change records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | Tests within 12 months and after isolation model change; onboarding records for the period. |
| independence | Reachability tests executed or witnessed by the security function independent of fabric operations. |
| mandatoryItems | Reachability test results; Configuration-to-tenant reconciliation |
| acceptableAlternatives | Staging-fabric performance-isolation tests with identical configuration, with representativeness argument |
| unknownEffect | US3 for single-tenant estates; US4 against CG-09 for multi-tenant platforms where isolation is a declared outcome. |
| reassessmentTriggers | New tenant class; Isolation mechanism change; Cross-tenant incident |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, TEST, SAMPLING

**Assessment procedure**

1. Review the isolation model and tenant assignments.
2. Reconcile partition/VRF/segment configuration with tenant records.
3. Review or witness reachability tests across domains.
4. Review or witness performance-isolation tests.
5. Sample onboarding/offboarding changes for verification.

**Gate mappings.** CG-09 Failure containment (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to fabrics shared by more than one tenant, customer or trust domain. For single-tenant fabrics, only traffic-class isolation between storage, collective and management traffic applies.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Partition key misassignment exposing tenant RDMA memory; Noisy-neighbour congestion degrading other tenants; Stale segment after offboarding; Shared lossless class propagating pause across tenants

**Testing safety.** Cross-tenant reachability tests shall use designated test endpoints and shall not access tenant data. Saturation tests require tenant notification and change approval.

**UNKNOWN rule.** If RDMA-layer isolation has not been tested separately from IP-layer isolation, record U5 and do not infer RDMA isolation from IP results.

**Ontology classes.** FaultDomain, Safeguard, Interface, TestRecord · **Related controls.** MCF-DEP-019, MCF-SEC-009, MCF-CMP-007, MCF-NET-007, MCF-RES-006

**Informative references.** InfiniBand Trade Association, InfiniBand Architecture Specification (Volumes 1 and 2); IEEE 802.1Q (Bridges and bridged networks); IEEE 802.1Qaz (Enhanced Transmission Selection and DCBX); AIDCF-013 (AI Data Centre Assurance Reference Architecture)

## NET-04 Management and out-of-band networks

### MCF-NET-013

**Management Separation** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure management traffic for switches, servers, BMCs, PDUs, storage and facility gateways traverses a management network separated from data and tenant networks, so data-plane failure or compromise does not remove management reach.

**Requirement.** The network architecture owner shall define the management network architecture, separating in-band management, BMC/out-of-band management and facility OT management, and shall prohibit management interfaces from being reachable from tenant or data networks except through defined conduits. The network operations manager shall reconcile the management network attachment of every switch management port, BMC, PDU, console server and storage controller to the design, and shall record any device whose management is only reachable in-band as a Finding.

**Assessment criteria**

1. Management network architecture defines in-band, out-of-band and OT management segments and permitted conduits.
2. Every in-scope managed device has its management interface attached to the designated segment.
3. No management interface is reachable from tenant or data networks except via defined conduits (verified by scan or ACL review).
4. Devices relying solely on in-band management are listed and dispositioned.
5. Management network capacity and addressing are independent of the data fabric.

**Minimum evidence**

- Management network architecture
- Device-to-management-segment inventory
- Reachability scan or ACL analysis from tenant/data networks
- List of in-band-only devices

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Reconciliation within 90 days (illustrative). |
| independence | Reachability scan run by the security function. |
| mandatoryItems | Device-to-segment inventory; Reachability evidence |
| acceptableAlternatives | Firewall and ACL rule analysis where active scanning is not permitted |
| unknownEffect | US3; escalates to US4 against CG-15 where BMCs or facility gateways are reachable from tenant networks. |
| reassessmentTriggers | New device class; Management network redesign; Scan finding |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, TEST, SAMPLING

**Assessment procedure**

1. Review the management architecture and conduits.
2. Reconcile device management attachment against inventory.
3. Review reachability scans or ACL analysis from tenant/data segments.
4. Disposition in-band-only devices.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all managed network, compute, storage, power-distribution and facility gateway devices supporting in-scope outcomes. Security policy of the conduits is assessed under SEC-010.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** BMCs on tenant VLAN; Switch management only in-band, lost when the fabric fails; Facility gateways bridged to IT management

**Testing safety.** Reachability scans shall be non-intrusive, rate-limited and authorised by the security owner; scanning OT segments requires OT owner approval (see SEC-009).

**UNKNOWN rule.** Devices whose management attachment cannot be determined are treated as reachable from data networks (U1) until evidenced.

**Ontology classes.** InfrastructureSystem, Interface, FaultDomain · **Related controls.** MCF-SEC-010, MCF-NET-014, MCF-NET-015, MCF-SEC-009

**Informative references.** ISA/IEC 62443-3-3 (System security requirements and security levels); NIST SP 800-82 Rev. 3 (Guide to operational technology security); ANSI/TIA-942 (Telecommunications infrastructure standard for data centres)

### MCF-NET-014

**Console Access** · CORRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure serial console and remote KVM access to network, compute and storage devices exists, is authenticated and is reachable independently of the data plane.

**Requirement.** The network operations manager shall provide serial console access to every switch, router, firewall and storage controller, and BMC/KVM access to every server, through console servers or OOB infrastructure that is independent of the data fabric, and shall require individual authentication, session logging and role-based authorisation for console sessions. The network operations manager shall verify console reachability for every device at a defined interval and after rack moves.

**Assessment criteria**

1. Every in-scope device has a mapped console or BMC path recorded in inventory.
2. Console servers authenticate individual users against a central identity source with local fallback governed by NET-016.
3. Console sessions are logged with user, device, time and, where supported, keystroke capture.
4. Periodic console reachability checks cover all devices and failures are remediated.
5. Console port mappings are verified after rack moves or re-cabling.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Console reachability check interval | days | 30 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Console mapping inventory
- Console server authentication configuration
- Session log samples
- Reachability check reports

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; FAILED; RECOVERY |
| periodCoverage | Most recent reachability check within the interval and checks over the prior six months. |
| independence | Assessor samples console reachability live with read-only login. |
| mandatoryItems | Console mapping inventory; Reachability check reports |
| acceptableAlternatives | Witnessed manual console checks on a sample where automated checks are unavailable |
| unknownEffect | US3: unknown console reach weakens recovery assurance; SUPPORTING evaluation for CG-10. |
| reassessmentTriggers | Console server replacement; Rack moves; Identity source change |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, SAMPLING, TEST

**Assessment procedure**

1. Review console mapping completeness against device inventory.
2. Review console authentication and logging configuration.
3. Sample devices and confirm live console reach using read-only access.
4. Review reachability check history and remediation.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to all network, storage and compute devices that would need recovery action during fabric or control-plane failure.

**Lifecycle stages.** BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, FAILED, RECOVERY

**Failure modes addressed.** Unmapped console after rack move; Shared console credentials; Console servers dependent on the failed fabric

**Testing safety.** Live console checks shall use read-only roles and shall not send break signals or keystrokes that could interrupt device boot or operation.

**UNKNOWN rule.** If console mapping completeness cannot be verified, treat unmapped devices as lacking recovery access (U1) in recovery-sequence analysis.

**Ontology classes.** Interface, AssetInstance, Safeguard · **Related controls.** MCF-NET-013, MCF-NET-015, MCF-NET-016, MCF-SEC-003

**Informative references.** ANSI/TIA-942 (Telecommunications infrastructure standard for data centres); ISA/IEC 62443-3-3 (System security requirements and security levels)

### MCF-NET-015

**OOB Resilience** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure the out-of-band management network remains available when the data fabric, site core, primary identity services or primary WAN fail, so restoration can proceed.

**Requirement.** The network architecture owner shall design the OOB network with its own switching, power supply from a protected source with defined autonomy, independent upstream connectivity (for example a separate carrier or cellular path), and locally available authentication and name resolution, and shall document every dependency the OOB network has on the systems it is used to recover. The network operations manager shall test at a defined interval that OOB access to critical devices is achievable with the production fabric, primary WAN and primary identity provider unavailable.

**Assessment criteria**

1. OOB design states switching, power source and autonomy, upstream paths and authentication fallback.
2. Dependency analysis shows the OOB network does not depend on the production fabric, production DNS/identity or the primary WAN, or each dependency is mitigated.
3. OOB equipment power is from a protected supply with autonomy meeting the recovery-sequence requirement.
4. A test in the period demonstrated OOB reach to critical devices with production fabric, primary WAN and primary identity unavailable (or simulated unavailable).
5. OOB health is monitored and failures alarm to an independent channel.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| OOB power autonomy | h | Equal to or greater than black-start sequence duration (illustrative 4) | Derived from RES-014 restoration sequence. |
| OOB test interval | months | 6 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- OOB design and dependency analysis
- Power path and autonomy evidence for OOB equipment
- OOB isolation test record
- OOB health monitoring configuration and alarms

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T3 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; FAILED; EMERGENCY; RECOVERY |
| periodCoverage | Isolation test within the interval parameter; health telemetry for six months. |
| independence | Test witnessed by the recovery or resilience function independent of network operations. |
| mandatoryItems | OOB dependency analysis; Isolation test record |
| acceptableAlternatives | Scenario exercise with simulated isolation (credentials and paths forced to fallback) where full isolation is not authorised, with residual UNKNOWN recorded |
| unknownEffect | US4: CG-10 cannot PASS while OOB independence from the systems it recovers is unverified. |
| reassessmentTriggers | OOB redesign; Identity provider change; Change of OOB carrier; Recovery exercise failure |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, TEST, SCENARIO_EXERCISE, INSPECTION

**Assessment procedure**

1. Review the OOB design and list its dependencies.
2. Trace OOB power to its source and verify autonomy.
3. Confirm local authentication and name resolution fallback exist and are tested.
4. Review or witness the isolation test.
5. Review OOB health monitoring and alarm routing.

**Gate mappings.** CG-10 Recovery readiness (CRITICAL); CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to every site supporting in-scope outcomes. Where OOB is provided by a colocation operator, responsibilities shall be explicit under DEP-018.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, FAILED, EMERGENCY, RECOVERY

**Failure modes addressed.** OOB authentication dependent on the identity provider hosted on the failed cluster; OOB switches powered from non-protected supply; OOB uplink sharing the primary carrier route; Circular dependency on production DNS

**Testing safety.** Isolation tests shall not disconnect production identity or WAN; they shall simulate isolation by forcing OOB clients to fallback paths, under an approved change with a rollback plan.

**UNKNOWN rule.** Any OOB dependency on a production service that has not been analysed is recorded as U10 at US4 against CG-10.

**Ontology classes.** InfrastructureSystem, Dependency, Safeguard, TestRecord · **Related controls.** MCF-NET-013, MCF-NET-016, MCF-RES-013, MCF-RES-014, MCF-SEC-004

**Informative references.** ANSI/TIA-942 (Telecommunications infrastructure standard for data centres); EN 50600 series / ISO/IEC 22237 series (Data centre facilities and infrastructures); NIST SP 800-82 Rev. 3 (Guide to operational technology security)

### MCF-NET-016

**Break-Glass Access** · RECOVERY · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure emergency access to network devices and controllers works when central authentication is unavailable, and that its use is controlled, logged and reviewed.

**Requirement.** The network operations manager shall provision break-glass local credentials or offline authentication for network devices, fabric controllers, subnet managers and console servers, stored in a sealed or vaulted mechanism with dual control, and shall test break-glass login on a sample of device classes at a defined interval. The infrastructure security owner shall review every break-glass use within a defined time, rotate the credentials afterwards, and confirm that break-glass accounts are disabled for routine use.

**Assessment criteria**

1. Break-glass credentials exist for every device class needed in recovery and are stored under dual control.
2. Break-glass login works on a sampled device of each class when central authentication is unreachable.
3. Every break-glass use in the period was logged, reviewed within the defined time and followed by credential rotation.
4. Break-glass accounts are not used for routine operations (log analysis).
5. Retrieval of break-glass credentials is possible during loss of the primary vault (offline copy governed by SEC-004).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Break-glass post-use review time | h | 24 (illustrative) | Capability-profile parameter. |
| Break-glass test interval | months | 6 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Break-glass account inventory per device class
- Vault and dual-control configuration
- Break-glass test records
- Use logs, reviews and rotation records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; EMERGENCY; FAILED; RECOVERY |
| periodCoverage | Test within the interval; all uses in the previous 12 months. |
| independence | Security function reviews use logs independently of network operations. |
| mandatoryItems | Test records; Use and rotation records |
| acceptableAlternatives | Tabletop plus a single live test on a non-production device of each class where production tests are not authorised |
| unknownEffect | US3; US4 against CG-10 if no tested emergency access exists for gate-critical fabric controllers. |
| reassessmentTriggers | Vault platform change; Identity provider change; Break-glass use; Personnel departure from dual-control holders |

**Assessment methods.** DOCUMENT_REVIEW, TEST, SAMPLING, ANALYSIS

**Assessment procedure**

1. Review break-glass inventory against recovery device classes.
2. Inspect dual-control and offline retrieval arrangements.
3. Review or witness a break-glass login test with central authentication made unreachable for the test device.
4. Sample use events and confirm review and rotation.
5. Analyse logs for routine use of break-glass accounts.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to network devices, fabric controllers, subnet managers and console servers supporting in-scope outcomes. Governance of break-glass across all infrastructure is SEC-004.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** EMERGENCY, FAILED, RECOVERY

**Failure modes addressed.** Break-glass password unknown or expired at time of need; Vault unreachable during outage; Break-glass account used routinely; No rotation after use

**Testing safety.** Break-glass tests shall be performed on a non-critical device or in a maintenance window, without disabling central authentication for other devices; rotation shall follow every test.

**UNKNOWN rule.** If no break-glass test has been performed for a device class, record U1 and treat emergency access for that class as unavailable in recovery analysis.

**Ontology classes.** Safeguard, TestRecord, Event · **Related controls.** MCF-SEC-004, MCF-NET-014, MCF-NET-015, MCF-SEC-003

**Informative references.** ISA/IEC 62443-3-3 (System security requirements and security levels); NIST SP 800-82 Rev. 3 (Guide to operational technology security)

## NET-05 Physical connectivity and optics

### MCF-NET-017

**Cabling Standards** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure structured cabling and high-density fibre plant are designed to recognised standards for pathways, bend radius, polarity, labelling, density and serviceability so that the physical layer does not become a latent fabric failure source.

**Requirement.** The cabling plant owner shall maintain a cabling design standard for the site covering pathway and containment fill limits, segregation from power, minimum bend radius by cable type, MPO/MTP polarity method, connector cleanliness acceptance, labelling scheme and test acceptance (insertion loss and, where applicable, reflectance), aligned with recognised data-centre cabling standards. The cabling plant owner shall approve deviations, and installers shall be bound to the standard contractually.

**Assessment criteria**

1. A site cabling standard exists covering pathways, fill, segregation, bend radius, polarity, cleanliness, labelling and test acceptance.
2. The standard references recognised cabling standards families and is approved by the cabling plant owner.
3. High-density back-end trunk designs (fibre counts, breakout scheme, patch-panel density) are specified.
4. Installer contracts reference the standard and its acceptance tests.
5. Deviations are approved and recorded.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum containment fill | % cross-section | Per adopted standard (illustrative 50) | From adopted cabling standard; site-specific. |
| Fibre link loss acceptance margin | dB below transceiver budget | Set from optics budget (illustrative 1.0) | Ensures operating margin; see NET-018. |

**Minimum evidence**

- Site cabling standard
- Trunk and breakout design for back-end fabrics
- Installer contract clauses
- Deviation register

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C2 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Current approved version. |
| independence | Review by a qualified cabling designer other than the author. |
| mandatoryItems | Site cabling standard |
| acceptableAlternatives | Adoption of an operator-wide standard with site addendum |
| unknownEffect | US2: absent standard reduces confidence in physical-layer claims; US3 where NET-018 shows optics failures attributable to cabling. |
| reassessmentTriggers | New fibre or connector type; New hall or density class; Recurring physical-layer incidents |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, INQUIRY

**Assessment procedure**

1. Review the cabling standard against adopted standards families.
2. Check coverage of high-density back-end trunk design.
3. Inspect a sample of installed pathways for conformance.
4. Review installer contracts and deviations.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all owned or operated cabling plant supporting in-scope fabrics. Provider-owned cabling is governed by provider contracts.

**Lifecycle stages.** PLAN, DESIGN, BUILD · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Bend-radius violations causing marginal loss; Polarity errors on MPO trunks; Overfilled trays preventing safe moves; Dirty connectors

**Testing safety.** Physical inspection shall not disturb live cabling; opening trays or handling live fibre requires an approved method statement.

**UNKNOWN rule.** If no site standard exists, physical-layer claims rely only on test results (NET-018/NET-020) and confidence is capped at CONF-2.

**Ontology classes.** Control, AssetInstance, Interface · **Related controls.** MCF-NET-018, MCF-NET-019, MCF-NET-020, MCF-PHY-005

**Informative references.** ANSI/TIA-942 (Telecommunications infrastructure standard for data centres); ISO/IEC 11801 series (Generic cabling for customer premises, including data centres); ISO/IEC 14763 series (Implementation and operation of customer premises cabling, including optical fibre testing); ANSI/TIA-606 (Administration standard for telecommunications infrastructure); EN 50600 series / ISO/IEC 22237 series (Data centre facilities and infrastructures); IEC 61300-3-35 (Fibre optic connector endface visual and automated inspection)

### MCF-NET-018

**Optics Compatibility** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure transceivers, active and passive cables and NIC/switch firmware are qualified combinations with adequate link budget, so optics do not become a common-mode source of link errors and flaps.

**Requirement.** The network architecture owner shall maintain a qualified-optics matrix listing approved transceiver and cable part numbers, firmware versions, host switch/NIC models and NOS/firmware versions, reach and link-budget class. The fabric operations lead shall reconcile installed optics (from digital diagnostic and CMIS inventory) to the matrix, shall monitor optical diagnostics (Rx/Tx power, temperature, bias, pre-FEC error indicators), and shall quarantine unqualified or degrading optics.

**Assessment criteria**

1. A qualified-optics matrix exists with part numbers, firmware, host combinations and link-budget class.
2. Installed optics inventory reconciles to the matrix; unqualified parts are listed and dispositioned.
3. Optical diagnostics are collected for all optics with thresholds for low Rx power and high temperature.
4. Measured link loss for a sample of links is within the transceiver budget with the defined margin.
5. Optics firmware is at qualified versions; mixed versions within a fabric are justified.
6. Failure and RMA data are analysed for batch or lot-level common modes.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Rx power warning margin | dB above receiver sensitivity | 2 (illustrative) | Capability-profile parameter derived from vendor budget. |
| Optics failure-rate review trigger | failures per 1000 per month | Site baseline-derived (illustrative) | Triggers lot-level analysis. |

**Minimum evidence**

- Qualified-optics matrix
- Installed optics inventory with serial, part and firmware
- Optical diagnostics telemetry
- Link loss test records
- RMA and failure analysis

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Inventory within 30 days (illustrative); diagnostics for 90 days. |
| independence | Inventory extracted by assessor from devices. |
| mandatoryItems | Installed optics inventory; Qualified-optics matrix |
| acceptableAlternatives | Sample-based physical inspection with serial capture where diagnostics are not readable |
| unknownEffect | US3: unqualified optics at scale are a common-mode exposure; escalate to US4 under CG-08 if failure analysis shows lot-level defects. |
| reassessmentTriggers | New optic vendor or part; Optics firmware release; Failure-rate spike; Supplier substitution |

**Assessment methods.** RECONCILIATION, ANALYSIS, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Review the qualified-optics matrix for completeness.
2. Extract installed optics inventory and reconcile.
3. Review diagnostics thresholds and sample telemetry.
4. Sample link loss test records against budget.
5. Review RMA data for lot or firmware common modes.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to all pluggable optics, AOCs and DACs in in-scope fabrics; for co-packaged or linear-drive optics, the matrix records host and module firmware combinations.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Unqualified optic causing intermittent errors; Optic lot defect affecting thousands of links; Firmware mismatch between module and host; Insufficient link margin

**Testing safety.** Reading diagnostics is non-intrusive; removing optics for inspection requires change approval and link drain.

**UNKNOWN rule.** Optics whose diagnostics cannot be read are treated as unqualified (U1) pending inspection.

**Ontology classes.** AssetInstance, FailureMode, Resource · **Related controls.** MCF-NET-006, MCF-NET-017, MCF-SUP-010, MCF-SUP-015

**Informative references.** OSFP MSA and QSFP-DD MSA module specifications; CMIS (Common Management Interface Specification); IEEE 802.3 (Ethernet, including optical PHY and FEC clauses); IEC 61300-3-35 (Fibre optic connector endface visual and automated inspection); ISO/IEC 14763 series (Implementation and operation of customer premises cabling, including optical fibre testing)

### MCF-NET-019

**Cross-Connect Control** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure physical moves, adds and changes to patching and cross-connects (including in meet-me rooms and carrier demarcations) are authorised, recorded and verified, so that maintenance does not sever redundant paths.

**Requirement.** The network operations manager shall require an approved work order for every physical patch or cross-connect change, specifying both ends, labels, affected path groups and redundancy impact, and shall verify after each change that the link came up on the expected ports and that the cabling records were updated. The network operations manager shall prohibit simultaneous work on members of the same redundant path group unless explicitly approved.

**Assessment criteria**

1. Every physical change in the sampled period has an approved work order identifying both ends and path-group impact.
2. Post-change verification (link state, neighbour, label) is recorded for each change.
3. Cabling records are updated within the defined time after change.
4. No simultaneous work on members of one redundant path group occurred without approval.
5. Carrier and colocation cross-connect changes are reconciled to provider orders.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Record update time after change | h | 24 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Work-order records for physical changes
- Post-change verification records
- Cabling record audit trail
- Provider cross-connect orders

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | At least six months (illustrative) of changes. |
| independence | Assessor selects the sample from device link-event logs rather than from the work-order system. |
| mandatoryItems | Work orders; Link-event logs for reconciliation |
| acceptableAlternatives |  |
| unknownEffect | US3: link events without matching work orders indicate uncontrolled physical change; CG-14 SUPPORTING. |
| reassessmentTriggers | Unplanned outage caused by patching; Change of field services provider |

**Assessment methods.** SAMPLING, RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Extract link up/down events for the period from devices.
2. Match events to work orders and identify unmatched changes.
3. Check sampled work orders for path-group impact and post-change verification.
4. Check for concurrent work on redundant pairs.
5. Reconcile provider cross-connect orders.

**Gate mappings.** CG-14 Change control (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all owned patching and to provider cross-connects for in-scope paths.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Wrong cable pulled during maintenance severing the surviving path; Unrecorded patch causing rail mis-mapping; Simultaneous work on both diverse trunks

**Testing safety.** Reconciliation is records-based and non-intrusive.

**UNKNOWN rule.** Unmatched link events are recorded as Findings unless explained; if link-event logs are unavailable, record U2 and limit the claim.

**Ontology classes.** Event, Action, Interface · **Related controls.** MCF-NET-020, MCF-OPS-018, MCF-OPS-006, MCF-NET-002

**Informative references.** ANSI/TIA-606 (Administration standard for telecommunications infrastructure); ANSI/TIA-942 (Telecommunications infrastructure standard for data centres)

### MCF-NET-020

**Path Documentation** · DETECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure end-to-end physical and logical path records (port to patch panel to trunk to panel to port, and circuit to route) are complete and accurate enough to support fault isolation, diversity analysis and recovery.

**Requirement.** The network operations manager shall maintain a path-documentation system (DCIM or cable-management database) recording every in-scope link from endpoint port through patch panels, trunks and cross-connects to the far-end port, with labels matching the physical plant and links to circuit IDs for external paths. The network operations manager shall audit a sample of paths physically and electronically at a defined interval and shall correct discrepancies, with an accuracy target set as a capability-profile parameter.

**Assessment criteria**

1. Path records exist for all in-scope links including intermediate panels and trunks.
2. Labels in the field match records for the audited sample.
3. Electronic reconciliation (LLDP or subnet-manager neighbours) matches end-to-end records.
4. Audit accuracy meets the target, and discrepancies are corrected.
5. External circuit records link to provider circuit IDs and routes (NET-002).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Path record accuracy target | % of audited links correct end-to-end | 99 (illustrative) | Capability-profile parameter. |
| Audit sample size | links per audit | Statistically justified (illustrative 200) | Sampling per AIDCF-009. |

**Minimum evidence**

- Path-documentation system extract
- Physical audit records
- Electronic reconciliation report
- Discrepancy correction log

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; RECOVERY |
| periodCoverage | Most recent audit within 12 months (illustrative). |
| independence | Physical audit performed by the assessor or a party independent of the record maintainers. |
| mandatoryItems | Audit records; Electronic reconciliation |
| acceptableAlternatives |  |
| unknownEffect | US3: inaccurate path records undermine diversity (CG-03) and recovery (CG-10) analysis. |
| reassessmentTriggers | Major expansion; Audit accuracy below target; Incident where records misled responders |

**Assessment methods.** INSPECTION, RECONCILIATION, SAMPLING

**Assessment procedure**

1. Extract path records for in-scope fabrics.
2. Select a sample and physically verify labels and routes.
3. Reconcile electronically against neighbour data.
4. Compute accuracy and review corrections.

**Gate mappings.** CG-02 Boundary and architecture integrity (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to all in-scope links and external circuits.

**Lifecycle stages.** BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, RECOVERY

**Failure modes addressed.** Records misidentifying the surviving path during an incident; Untraceable trunks after expansion; Circuit ID not linked to route

**Testing safety.** Physical audits shall not disturb live cables beyond visual label inspection.

**UNKNOWN rule.** Where records cannot be reconciled for a fabric segment, the segment's paths are treated as undocumented (U1) in diversity and blast-radius analysis.

**Ontology classes.** ArchitectureSnapshot, Interface, EvidenceObject · **Related controls.** MCF-NET-001, MCF-NET-002, MCF-NET-019, MCF-DEP-007

**Informative references.** ANSI/TIA-606 (Administration standard for telecommunications infrastructure); ANSI/TIA-942 (Telecommunications infrastructure standard for data centres); ISO/IEC 14763 series (Implementation and operation of customer premises cabling, including optical fibre testing)

## NET-06 Network control and observability

### MCF-NET-021

**Controller Resilience** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure fabric control functions (InfiniBand subnet managers, SDN or EVPN controllers, fabric management platforms, route reflectors) survive single failures and that their loss does not disrupt forwarding beyond tolerance.

**Requirement.** The network architecture owner shall deploy fabric control functions with redundancy (master/standby subnet managers, clustered controllers, redundant route reflectors) placed in separate power and rack fault domains, and shall document the data-plane behaviour when the control function is lost (forwarding continues with stale state, or fails). The fabric operations lead shall test controller and subnet-manager failover at a defined interval and after upgrades and shall confirm forwarding continuity and failover time within tolerance.

**Assessment criteria**

1. Each fabric control function has redundancy and placement in separate power/rack domains.
2. Data-plane behaviour on control-plane loss is documented.
3. Failover tests in the period show forwarding continuity and failover time within tolerance.
4. Controller state backups exist and restore has been tested.
5. Controller health is monitored and alarms on loss of redundancy.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Controller failover time tolerance | s | Below job collective timeout margin (illustrative 60) | Capability-profile parameter. |
| Controller failover test interval | months | 12 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Controller architecture and placement
- Behaviour-on-loss documentation
- Failover test records
- Backup and restore test records
- Health monitoring configuration

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; FAILED; RECOVERY |
| periodCoverage | Failover test within the interval and after the last upgrade. |
| independence | Test witnessed by a party independent of fabric operations. |
| mandatoryItems | Failover test record; Placement analysis |
| acceptableAlternatives | Staging test at representative scale where production failover is not authorised |
| unknownEffect | US3; US4 against CG-08 for InfiniBand fabrics where subnet-manager failover is untested. |
| reassessmentTriggers | Controller software upgrade; Fabric scale change; Controller incident |

**Assessment methods.** DOCUMENT_REVIEW, TEST, ANALYSIS, INSPECTION

**Assessment procedure**

1. Review controller architecture and placement against power and rack domains.
2. Review documented behaviour on control-plane loss.
3. Review or witness failover test.
4. Review backup/restore test.
5. Verify health monitoring.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-09 Failure containment (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to fabrics whose forwarding or configuration depends on a control function. Security of controllers is SEC-007.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, FAILED, RECOVERY

**Failure modes addressed.** Subnet-manager split-brain; Standby controller unable to take over at scale; Controllers co-located on one PDU; Controller loss causing data-plane flush

**Testing safety.** Controller failover tests risk fabric-wide disruption and require change-board authorisation, a rollback plan and workload owner consent.

**UNKNOWN rule.** If data-plane behaviour on controller loss is undocumented and untested, record U8 at US4 against CG-08.

**Ontology classes.** InfrastructureSystem, FaultDomain, TestRecord, Safeguard · **Related controls.** MCF-NET-004, MCF-SEC-007, MCF-RES-015, MCF-NET-022

**Informative references.** InfiniBand Trade Association, InfiniBand Architecture Specification (Volumes 1 and 2); IETF RFC 7938 (Use of BGP for routing in large-scale data centres); OpenConfig gNMI specification and OpenConfig data models

### MCF-NET-022

**Configuration Management** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure network operating system, firmware and configuration across switches, NICs, optics and controllers are held to an approved baseline, changed only through staged and verified rollout, and restorable.

**Requirement.** The fabric operations lead shall maintain a version-controlled source of truth for intended network configuration and an approved baseline of NOS, switch firmware, NIC firmware and driver, optics firmware and controller versions; shall detect configuration and version drift at a defined interval; and shall roll out changes in stages (canary, partial, full) with automated pre- and post-change checks and defined rollback. The network operations manager shall ensure that no single change can be applied simultaneously to both members of a redundant pair or to all planes of a fabric.

**Assessment criteria**

1. A version-controlled intended configuration and an approved version baseline exist for each device class.
2. Drift detection runs at the defined interval and drift is remediated or approved.
3. Changes in the period followed staged rollout with pre- and post-checks and recorded rollback plans.
4. No change was applied simultaneously to both members of a redundant pair or all planes without approval.
5. Configuration backups exist for all devices and a restore from backup has been tested.
6. Emergency changes were retrospectively reviewed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Drift detection interval | h | 24 (illustrative) | Capability-profile parameter. |
| Canary stage size | % of devices | ≤5 (illustrative) | Limits firmware common-mode exposure (X08). |

**Minimum evidence**

- Source of truth repository and version baseline
- Drift reports for the period
- Change records with stage plans, checks and rollback
- Configuration backup inventory and restore test

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; TRANSITION; RECOVERY |
| periodCoverage | At least six months (illustrative) of changes and drift reports. |
| independence | Assessor runs or reperforms a drift comparison on a sample of devices. |
| mandatoryItems | Drift reports; Staged change records; Restore test record |
| acceptableAlternatives |  |
| unknownEffect | US4: uncontrolled NOS/firmware change on a gate-critical fabric defeats CG-14; CG-08 SUPPORTING. |
| reassessmentTriggers | NOS major version; Automation platform change; Change-induced incident; Drift above threshold |

**Assessment methods.** REPERFORMANCE, SAMPLING, DOCUMENT_REVIEW, RECONCILIATION

**Assessment procedure**

1. Review the source of truth and version baseline.
2. Reperform drift detection on a sample of devices.
3. Sample changes and verify staged rollout, checks and rollback plans.
4. Check for simultaneous change to redundant pairs or all planes.
5. Review backup coverage and the restore test.
6. Review emergency change retrospectives.

**Gate mappings.** CG-14 Change control (CRITICAL); CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to all network devices, NICs, optics and fabric controllers in scope. Site-wide change governance is OPS-018.

**Lifecycle stages.** OPERATE, CHANGE, COMMISSION · **Operating states.** NORMAL, MAINTENANCE, TRANSITION, RECOVERY

**Failure modes addressed.** Firmware rollout common-mode failure across all planes (X08); Configuration drift breaking congestion control; No backup for recovery; Recovery restoring corrupt configuration (X15)

**Testing safety.** Drift comparison is read-only. Restore tests shall be on a spare or isolated device unless a maintenance window is authorised.

**UNKNOWN rule.** If NIC or optics firmware versions are not in the baseline, record U5 and treat firmware common-mode exposure as unassessed.

**Ontology classes.** ArchitectureSnapshot, Action, ReassessmentTrigger, AssetInstance · **Related controls.** MCF-OPS-017, MCF-OPS-018, MCF-CMP-013, MCF-RES-015, MCF-SEC-013

**Informative references.** OpenConfig gNMI specification and OpenConfig data models; IETF RFC 7938 (Use of BGP for routing in large-scale data centres); AIDCF-004 (Threat, Hazard and Failure Model)

### MCF-NET-023

**Flow Telemetry** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure network telemetry (counters, streaming telemetry, flow sampling, congestion and buffer metrics) is collected with sufficient coverage, resolution and retention to detect degradation, attribute job slowdowns and support evidence for assurance.

**Requirement.** The fabric operations lead shall collect streaming or polled telemetry from all in-scope switches and NICs covering interface counters, error counters, PFC pause and ECN mark counts, buffer occupancy, and flow sampling, at a resolution sufficient to observe collective-scale events, and shall retain it for the evidence retention period. The fabric operations lead shall monitor telemetry pipeline health and alert on collection gaps.

**Assessment criteria**

1. Telemetry coverage includes all in-scope switches and NICs with gaps listed.
2. Counters include errors, PFC pause, ECN marks, buffer occupancy and drops per traffic class.
3. Collection resolution meets the defined parameter for congestion visibility.
4. Retention meets the evidence retention requirement.
5. Pipeline gaps are alerted and recorded, and gap rates are within tolerance.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Telemetry collection interval for congestion counters | s | 10 (illustrative) | Capability-profile parameter; finer for diagnosis. |
| Telemetry retention | days | Per evidence retention class (illustrative 395) | AIDCF-008 retention classes. |

**Minimum evidence**

- Telemetry coverage report
- Collector configuration
- Pipeline health and gap reports
- Retention configuration

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE; RECOVERY |
| periodCoverage | At least 90 days (illustrative). |
| independence | Assessor queries the telemetry store directly. |
| mandatoryItems | Coverage report; Gap reports |
| acceptableAlternatives |  |
| unknownEffect | US2: gaps reduce confidence of all NET OPERATION claims relying on telemetry. |
| reassessmentTriggers | Telemetry platform change; New device class; Gap rate above tolerance |

**Assessment methods.** ANALYSIS, SAMPLING, INSPECTION

**Assessment procedure**

1. Compare telemetry source list to device inventory.
2. Query a sample of counters and check resolution.
3. Review gap reports and pipeline health.
4. Verify retention.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all in-scope fabrics and networks.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, RECOVERY

**Failure modes addressed.** Telemetry gaps hiding congestion events; Coarse sampling missing microbursts; Telemetry pipeline sharing failure domain with fabric

**Testing safety.** Non-intrusive; increasing collection frequency on production switches shall be assessed for control-plane CPU impact first.

**UNKNOWN rule.** Telemetry with unresolved gaps covering the assessed period is marked INCOMPLETE and cannot alone support OPERATION claims.

**Ontology classes.** EvidenceObject, InfrastructureSystem, Safeguard · **Related controls.** MCF-NET-005, MCF-NET-006, MCF-SEC-017, MCF-CMP-017

**Informative references.** OpenConfig gNMI specification and OpenConfig data models; sFlow version 5 specification (sFlow.org); IETF RFC 7011 (IPFIX protocol specification)

### MCF-NET-024

**Time and Core Services** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure time (NTP/PTP), DNS, DHCP, IPAM and network AAA services that fabrics and clusters depend on are redundant, independent of the services they support, and resilient to failure and divergence.

**Requirement.** The network architecture owner shall deploy time sources (with at least two independent references such as GNSS and a holdover oscillator or a remote time service), DNS, DHCP, IPAM and network AAA as redundant services placed in separate fault domains, and shall document every circular dependency between these services and the systems they support. The network operations manager shall monitor time offset, stratum and source agreement, and service availability, and shall test failure of a time source and of a DNS/AAA instance at a defined interval.

**Assessment criteria**

1. Each core service has redundancy across separate power and rack fault domains.
2. Time architecture has independent references with holdover and monitors offset and source divergence (X13).
3. Circular dependencies (for example DNS needed to reach the time server, or AAA hosted on the cluster it authenticates) are documented and broken or mitigated.
4. Tests of time-source loss and DNS/AAA instance loss in the period showed service continuity.
5. Clients are configured with multiple servers and sensible failover.
6. Time offset across a sample of devices stays within tolerance.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Time offset tolerance | ms | Workload- and log-correlation-dependent (illustrative 1 for NTP; sub-microsecond for PTP where required) | Capability-profile parameter. |
| Holdover duration | h | Covers time-source repair time (illustrative 24) | Capability-profile parameter. |

**Minimum evidence**

- Core service architecture and placement
- Circular-dependency analysis
- Time offset and source telemetry
- Failure test records
- Client configuration samples

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; FAILED; RECOVERY |
| periodCoverage | Tests within 12 months (illustrative); telemetry for 90 days. |
| independence | Assessor samples device time offset directly. |
| mandatoryItems | Circular-dependency analysis; Failure test records |
| acceptableAlternatives | Analysed incidents of time-source or DNS loss in the period |
| unknownEffect | US3; US4 against CG-10 where a circular dependency could prevent cold start (X19). |
| reassessmentTriggers | Time architecture change; GNSS anomaly; DNS/AAA platform change; Cluster hosting a core service |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, TEST, SAMPLING

**Assessment procedure**

1. Review architecture and placement for each core service.
2. Review circular-dependency analysis against RES-013.
3. Sample time offsets and source agreement.
4. Review failure tests.
5. Sample client configurations.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to time, DNS, DHCP, IPAM and network AAA services relied upon by in-scope infrastructure.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE · **Operating states.** NORMAL, DEGRADED, FAILED, RECOVERY

**Failure modes addressed.** Time-source divergence corrupting log correlation and certificate validity (X13); AAA hosted on the failed cluster; DNS loss blocking cluster bring-up; GNSS spoofing or loss without holdover

**Testing safety.** Time-source failure tests shall be performed by withdrawing one source while monitoring offset; never step production clocks. DNS/AAA instance tests require change approval.

**UNKNOWN rule.** If time source independence cannot be established, record U10 and treat time as a single common-mode dependency.

**Ontology classes.** InfrastructureSystem, Dependency, FaultDomain, TestRecord · **Related controls.** MCF-RES-013, MCF-RES-014, MCF-SEC-001, MCF-NET-015

**Informative references.** IEEE 1588 (Precision Time Protocol); IETF RFC 5905 (Network Time Protocol version 4); IETF RFC 8915 (Network Time Security for NTP); AIDCF-004 (Threat, Hazard and Failure Model)
