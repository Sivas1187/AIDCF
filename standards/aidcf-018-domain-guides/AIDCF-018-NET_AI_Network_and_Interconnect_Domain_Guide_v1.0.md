# AIDCF-018-NET AI Network and Interconnect Architecture Domain Guide

**AIDCF – AI Data Centre Facilities Assurance Framework**

## Document control

| Field | Value |
|---|---|
| Document ID | AIDCF-018-NET |
| Title | AI Network and Interconnect Architecture Domain Guide |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Parent artifact | AIDCF-018 Domain Guides |
| Normative controls | MCF-NET-001 to MCF-NET-024 in AIDCF-007A (control records as maintained in the canonical registry) |
| Depends on | AIDCF-003, AIDCF-004, AIDCF-005, AIDCF-007A, AIDCF-008, AIDCF-009, AIDCF-010, AIDCF-013, AIDCF-014 |
| Requirement prefix | DG-NET-REQ-NNN |

### Revision history

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-10 | First issue of the NET domain guide, aligned to the rewritten MCF-NET control records, per-control gate mapping and canonical vocabularies. |

## 1 Purpose and scope

This guide explains how the AI Network and Interconnect Architecture (NET) domain is assessed under AIDCF. It gives assessors, network architects, fabric operators and assurance reviewers a common technical picture of what the 24 NET controls protect, why they matter for AI capability, what evidence demonstrates each claim type, and how NET results feed critical gates and the Assurance Decision.

The guide is informative except where a statement carries a DG-NET-REQ identifier. The controls themselves (MCF-NET-001 to MCF-NET-024 in AIDCF-007A) are normative; if this guide and a control record disagree, the control record prevails and the discrepancy shall be raised as a baseline issue.

In scope:

- **Scale-out back-end fabrics** carrying accelerator-to-accelerator collective traffic, whether InfiniBand or Ethernet with RDMA over Converged Ethernet version 2 (RoCEv2) or newer Ethernet transports.
- **Scale-up domains** (intra-node and rack-scale accelerator interconnects) where they are represented as network elements; the compute aspects of scale-up integrity are assessed under CMP-02.
- **Storage networks** (dedicated fabrics, dedicated planes or traffic classes on a converged fabric).
- **Front-end networks** carrying inference requests, APIs, orchestration, data ingest and user access, and the **service gateways** on those paths.
- **Management and out-of-band (OOB) networks**, console and BMC access, and break-glass network access.
- **Physical connectivity**: structured cabling, high-density fibre, transceivers and cables, cross-connects, meet-me rooms and path records.
- **WAN and data-centre interconnect (DCI)** for multi-site training, replication, alternate capacity and carrier diversity.
- **Network control and observability**: subnet managers, SDN/EVPN controllers, configuration and firmware management, telemetry, time, DNS, DHCP, IPAM and network AAA.

Out of scope here (covered elsewhere): security policy and authority over network devices and controllers (SEC, in particular SEC-007, SEC-009 to SEC-012), accelerator and node health (CMP), storage system performance and integrity (STO), and dependency discovery as a cross-domain discipline (DEP).

## 2 Why this domain matters for AI capability

For conventional enterprise workloads, the network is usually a shared utility whose short disruptions are absorbed by retries. For large-scale AI training and distributed inference the network is part of the computer. Synchronous data-parallel, tensor-parallel, pipeline-parallel and expert-parallel training issues collective operations (all-reduce, all-gather, reduce-scatter, all-to-all) on every step; the step completes only when the slowest participant finishes. The consequences for assurance are:

1. **Tail behaviour, not averages, determines outcome.** A single degraded link, mis-mapped rail or congested spine port lengthens every step for every accelerator in the job. A fabric can appear healthy on average utilisation while delivering a fraction of design throughput.
2. **Failure propagates by design.** Lossless configurations (Priority-based Flow Control on Ethernet, credit-based flow control on InfiniBand) deliberately push back-pressure upstream. Correctly bounded, this prevents loss; incorrectly bounded, it spreads a local fault into a fabric-wide stall (pause storms) or a permanent stall (deadlock from cyclic buffer dependency).
3. **Common-mode exposure is high.** Back-end fabrics are built from very large numbers of identical switches, NICs and optics running the same firmware. One defective optic lot, one NIC firmware regression or one bad configuration push can affect thousands of links simultaneously (AIDCF-004 scenario X08).
4. **Recovery depends on the network first.** Restoration of storage, compute and the AI control plane presupposes working OOB management, core network, time and name resolution. A network that is the last thing to recover, or that depends on systems it is needed to recover, converts a partial outage into a prolonged one.
5. **Checkpoint traffic is a periodic stress test.** Synchronised checkpoint writes from thousands of accelerators create bursts that can saturate storage uplinks and interfere with collective traffic (scenario X06). The checkpoint path is therefore both a performance outcome and a recovery prerequisite.

NET controls therefore address performance integrity (CG-08), containment of fabric failures (CG-09), network restoration as part of recovery readiness (CG-10), and the network's contribution to dependency visibility (CG-03), change control (CG-14) and bounded digital authority (CG-15).

## 3 Reference patterns and variants

AIDCF does not prescribe network designs. Assessors shall nevertheless recognise the common patterns because each has characteristic failure modes and evidence.

### 3.1 Back-end fabric topologies

| Pattern | Description | Assurance-relevant characteristics |
|---|---|---|
| Rail-optimised multi-plane | Ordinal NIC *n* of every node connects to leaf (rail) *n*; rails are aggregated by spines; several independent planes may exist. | Rail mapping errors force traffic across spines; plane loss reduces bandwidth proportionally; independent planes give natural fault domains if they do not share power, cooling or controllers. |
| Two-tier leaf-spine (folded Clos) | Every leaf connects to every spine. | Simple to reason about; bisection bandwidth set by uplink count and oversubscription; spine loss is a fractional reduction. |
| Three-tier fat-tree / Clos with super-spines or pods | Pods of leaf-spine joined by a super-spine or core tier. | Cross-pod traffic sees an extra tier and often oversubscription; pod boundaries are natural blast-radius boundaries; job placement matters. |
| Rack-scale scale-up domain | Accelerators in one or more racks joined by a dedicated high-bandwidth interconnect (switch trays or direct links). | Scale-up domain failure affects every accelerator in it; behaves as a single fault domain for many workloads; health is a CMP concern but its interconnect is a NET topology element. |

### 3.2 Transport variants

- **InfiniBand**: credit-based link-level flow control (inherently lossless), a subnet manager computing routes and assigning addresses, partition keys for isolation, adaptive routing and, in some products, in-network reduction. Assessment focus: subnet-manager redundancy and failover at scale, partition configuration, adaptive-routing settings and management-key protection.
- **Ethernet with RoCEv2**: RDMA over UDP/IP. Commonly operated as a lossless class with PFC plus ECN-based end-to-end congestion control (DCQCN-style rate control at the NIC driven by congestion notification packets), or with lossy-tolerant transports and selective retransmission. Assessment focus: traffic-class mapping, ECN thresholds, PFC headroom and watchdog, NIC rate-control parameters and deadlock analysis.
- **Newer Ethernet AI transports** (for example those specified by the Ultra Ethernet Consortium) change congestion control and loss tolerance assumptions. The same assessment questions apply; evidence must reflect the transport actually deployed.

### 3.3 Other networks

- **Storage network**: dedicated fabric, dedicated plane or traffic class on the back-end or front-end fabric. Converged designs must show that checkpoint bursts do not starve collective traffic.
- **Front-end network**: leaf-spine with BGP-based routing and ECMP is typical; inference gateways, load balancers and API gateways sit on this path.
- **Management and OOB**: separate switches for BMC, switch management, PDUs and console servers, with an independent upstream (separate carrier or cellular) and local authentication fallback.
- **WAN/DCI**: dark fibre with DWDM, leased wavelengths or carrier services; diversity must be physical (routes, entries, ducts) and organisational (not two brands on one wholesale route).

### 3.4 Deployment variants

The AIDCF-013 reference patterns change ownership and evidence access more than technical content. In **colocation**, the operator may own cross-connects, meet-me rooms and sometimes OOB uplinks; NET controls apply to the owned portion and DEP-018 governs the boundary. In **hybrid cloud**, front-end and DCI extend into provider networks whose evidence is typically E5 provider assurance. In **shared multi-tenant platforms**, NET-012 traffic isolation becomes a primary outcome. In **brownfield retrofits**, cabling standards and path documentation are frequently the weakest controls.

## 4 Required functions and capability linkage

NET implements the following Required Functions in the AIDCF assurance chain. Each links to Service Outcomes defined under CAP-02 and tolerances under RES-001.

| Required Function | Service Outcomes typically supported | Principal NET controls |
|---|---|---|
| Deliver inter-accelerator collective bandwidth and latency at required scale | Training throughput; distributed inference latency | NET-001, NET-003, NET-005, NET-007, NET-008 |
| Contain fabric faults within declared fault domains | Training availability; multi-tenant isolation | NET-004, NET-007, NET-012, NET-021 |
| Deliver dataset read and checkpoint write throughput | Training throughput; recovery point | NET-009 |
| Deliver inference and API traffic with redundancy | Inference availability and latency | NET-010, NET-011 |
| Provide independent management reach in all states | Recovery time; secure operations | NET-013 to NET-016 |
| Maintain physical-layer integrity and traceability | All outcomes (latent common mode) | NET-002, NET-017 to NET-020 |
| Keep network state controlled, observable and restorable | All outcomes; change integrity | NET-022, NET-023 |
| Provide time, name, address and AAA services | Cluster bring-up; log integrity; recovery | NET-024 |

**DG-NET-REQ-001** An assessor shall trace each NET control result used in a gate evaluation to at least one Required Function and Service Outcome of the assessed Capability Instance; a NET result with no such trace shall not be used to support a gate PASS.

## 5 Dependencies, fault domains and common-mode concerns

### 5.1 Upstream dependencies of the network

- **Power**: switches, optics and NICs draw from rack PDUs fed by the electrical distribution system. Redundant spines or planes fed from one UPS output or one switchboard section share a fault domain even if every switch has dual power supplies.
- **Cooling**: high-radix switches and high-power optics are sensitive to inlet temperature; liquid-cooled switch designs depend on the same CDU groups as compute.
- **Time, DNS, AAA**: switch configuration, telemetry and authentication depend on these core services (NET-024).
- **Controllers**: InfiniBand subnet managers, SDN/EVPN controllers and automation platforms (NET-021, NET-022).
- **Carriers and colocation operators** for WAN/DCI and cross-connects (NET-002, NET-019).

### 5.2 Downstream dependants

Compute job scheduling, storage access, cluster managers, monitoring, security telemetry, crisis communications and remote operations all depend on network function. NET failure therefore often appears first as a CMP, STO or OPS symptom.

### 5.3 Fault domains

The NET-004 fault-domain register should list at least: individual leaf, spine and super-spine switches; each rail and each plane; each pod; each subnet manager or controller instance; each OOB switch and console server; each WAN/DCI circuit and its route; and the power and cooling domains serving each of these. RES-005 integrates these into the site model; CMP-008 integrates them with compute placement.

### 5.4 Characteristic common modes

| Common mode | Mechanism | Detection and control |
|---|---|---|
| Firmware/NOS version | Identical defect across all switches or NICs | Staged rollout, canary, plane-by-plane change (NET-022) |
| Optics lot or model | Marginal batch degrading over time | Optics inventory by lot, RMA analysis (NET-018), error trending (NET-006) |
| Shared lossless class | Pause propagation across tenants or across storage and collective traffic | Traffic-class design, watchdog (NET-007), isolation testing (NET-012) |
| Shared route or entry | Excavation, fire or flood severing nominally diverse paths | Route evidence and shared-segment register (NET-002) |
| Shared controller | Subnet manager or automation platform failure or compromise affecting all planes | Redundancy and placement (NET-021); security (SEC-007) |
| Circular service dependency | OOB authentication, DNS or AAA hosted on the infrastructure being recovered | OOB independence (NET-015); core service analysis (NET-024); RES-013 |

## 6 Threats, hazards and failure scenarios with propagation paths to Service Outcomes

The AIDCF-004 network scenario families (fabric partition, congestion collapse, scale-up link failure, management network loss, time-service failure, DNS/DHCP/IPAM failure, configuration blast radius, optical/cabling defect) and cross-domain scenarios X06, X08, X13, X15, X16 and X19 are the starting set. Representative propagation paths, expressed in the canonical chain (initiating event → path → Service Outcome effect), are below.

| Scenario | Initiating event | Propagation path | Service Outcome effect |
|---|---|---|---|
| PFC pause storm | NIC firmware fault continuously asserts pause on one priority | Pause propagates leaf → spine → other leaves; lossless class stalls across pod | All jobs in pod stall; training throughput collapses until watchdog isolates the port (NET-007) |
| PFC deadlock | Routing change after link failure creates cyclic buffer dependency | Buffers on a cycle of switches fill and wait on each other indefinitely | Persistent stall that survives the original fault; recovery requires manual intervention |
| Checkpoint burst congestion (X06) | Synchronised checkpoint across thousands of ranks | Storage uplinks saturate; storage traffic shares class with collectives; head-of-line blocking | Step time spikes; checkpoint exceeds window; recovery point degraded (NET-009, RES-016) |
| Optic lot degradation | Batch of transceivers with rising pre-FEC errors | Corrected errors become uncorrectable; link flaps; reroute; collective timeouts | Intermittent job failures at scale; lost work beyond tolerance (NET-006, NET-018) |
| Firmware common mode (X08) | NOS update pushed to all spines | All planes share defect; routing or forwarding failure | Fabric-wide outage; recovery depends on rollback (NET-022) |
| Subnet-manager failover at scale | Master subnet manager host fails | Standby takes over but full sweep at scale exceeds collective timeout | All running jobs fail; restart from checkpoint (NET-021, NET-004) |
| Management network loss | OOB switch row on single PDU loses power during maintenance | BMC and console reach lost for rows | Diagnosis and recovery slowed; recovery time objective missed (NET-015) |
| Time divergence (X13) | GNSS loss with no holdover; or misconfigured time source | Clock drift; certificate validation and log correlation fail | Authentication failures; forensic and evidence integrity reduced (NET-024) |
| Shared authentication failure (X19) | Identity provider for network AAA hosted on the failed cluster | No administrative login to network devices; break-glass untested | Recovery blocked (NET-016, NET-024, SEC-004) |
| Physical intrusion or wrong-cable pull (X16) | Unauthorised or erroneous patching | Surviving path of a redundant pair severed | Loss of DCI or storage connectivity (NET-019, NET-020) |
| Recovery reintroduces bad configuration (X15) | Restore from backup taken after drift | Faulty congestion settings reapplied | Recurrence of instability post-recovery (NET-022, RES-015) |

Threat sources relevant to NET include malicious insiders with patching access, compromised network automation, supply-chain substitution of optics or firmware, and tenants deliberately creating congestion. Authority aspects of these threats are assessed under SEC; NET assesses whether the fabric limits the consequence.

## 7 Safeguards

Using the AIDCF-004 safeguard functions:

- **Anticipate**: traffic-matrix analysis for oversubscription (NET-003); optics qualification (NET-018); scenario library entries for network failures (RES-003).
- **Prevent**: approved topology and reconciliation (NET-001); congestion-control design and deadlock analysis (NET-007); cabling standards (NET-017); cross-connect work control (NET-019); staged change (NET-022).
- **Detect**: latency baselines (NET-005); error and retransmission thresholds (NET-006); collective benchmarks (NET-008); telemetry coverage (NET-023); path audits (NET-020).
- **Decide and respond**: automated link isolation on error thresholds (NET-006); PFC watchdog (NET-007); controller failover (NET-021).
- **Contain**: fault-domain design (NET-004); traffic isolation (NET-012); management separation (NET-013).
- **Withstand**: path diversity (NET-002); redundant gateways (NET-011); redundant core services (NET-024).
- **Recover**: console access (NET-014); OOB resilience (NET-015); break-glass (NET-016); configuration backup and restore (NET-022).

## 8 Critical-gate linkage

Gate mappings are per control (SPEC §6.1). CRITICAL means the gate cannot PASS unless the control is CONFORMING at its required claim type when in scope; SUPPORTING means a NONCONFORMING result requires a documented gate-level evaluation. Meta-gates CG-11 and CG-12 are evaluated across all controls and are not mapped.

| Gate | Name | CRITICAL controls | SUPPORTING controls |
|---|---|---|---|
| CG-02 | Boundary and architecture integrity | — | NET-001, NET-020 |
| CG-03 | Critical dependency visibility | — | NET-002, NET-004, NET-015, NET-018, NET-020, NET-024 |
| CG-08 | Compute, storage and network functional integrity | NET-001, NET-007, NET-008, NET-009 | NET-002, NET-003, NET-004, NET-005, NET-006, NET-010, NET-011, NET-012, NET-013, NET-017, NET-018, NET-019, NET-021, NET-022, NET-023, NET-024 |
| CG-09 | Failure containment | NET-004 | NET-002, NET-007, NET-012, NET-021 |
| CG-10 | Recovery readiness | NET-015 | NET-009, NET-014, NET-016, NET-020, NET-021, NET-022, NET-024 |
| CG-14 | Change control | NET-022 | NET-019 |
| CG-15 | Integrated digital authority over infrastructure | — | NET-012, NET-013, NET-014, NET-015, NET-016 |

Rationale for the CRITICAL assignments:

- **CG-08** (functional integrity): an unreconciled topology (NET-001), untested congestion behaviour on a lossless fabric (NET-007), unmeasured collective performance (NET-008) or an unverified checkpoint path (NET-009) each directly defeats the claim that the fabric delivers the required function.
- **CG-09** (containment): NET-004 is the only control that demonstrates single-element fabric failures stay within declared blast radius.
- **CG-10** (recovery readiness): NET-015 is CRITICAL because every other restoration step depends on management reach that is independent of the failed systems.
- **CG-14** (change control): NET-022 is CRITICAL because uncontrolled NOS/firmware/configuration change across a fabric is the dominant common-mode path (X08) and cannot be compensated by site-level change governance alone.

**DG-NET-REQ-002** Where a fabric is in scope for a gate to which a NET control is mapped CRITICAL, the assessor shall evaluate that control at its required claim type for that fabric; a result obtained for a different fabric of similar design shall not be substituted without a documented representativeness argument accepted by the assessment lead.

## 9 Capability-profile parameters

All values below are illustrative defaults for capability profiles, not requirements. A capability profile shall set site- and outcome-specific values with a recorded basis. Parameters are listed as defined in the control records.

| Control | Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|---|
| NET-001 | Rail-mapping conformance | % of accelerator ports on design rail/leaf | 100 (illustrative) | Rail-optimised designs assume ordinal NIC n connects to rail n; any deviation alters collective paths. Site-specific. |
| NET-001 | Maximum topology reconciliation age | days | 90 (illustrative) | Capability-profile parameter; shorten where change rate is high. |
| NET-002 | Minimum physical separation between diverse routes | m | Site-specific; set by risk analysis (illustrative: separate containment and entry points) | Capability-profile parameter; no universal distance applies. |
| NET-002 | Route evidence age | months | 12 (illustrative) | Carriers re-groom circuits; evidence ages. |
| NET-003 | Back-end fabric design oversubscription | ratio (downlink:uplink) | 1:1 (illustrative) | Common design choice for large training fabrics; site and workload specific. |
| NET-003 | Front-end/storage uplink oversubscription | ratio | Workload-derived (illustrative 3:1) | Capability-profile parameter justified by traffic analysis. |
| NET-003 | Minimum tolerated effective ratio under N-1 | ratio | Set per Service Outcome (illustrative 1.15:1 for back-end) | Derived from performance outcome tolerance. |
| NET-004 | Maximum endpoints affected by a single switch failure | accelerator ports | Equal to leaf downlink count (illustrative) | Derived from topology; outcome-specific tolerance. |
| NET-004 | Maximum reroute/reconvergence time after single spine loss | s | Set by job collective timeout margin (illustrative 30) | Must be below framework collective timeouts; site-specific. |
| NET-004 | Subnet-manager failover time | s | Vendor- and scale-dependent (illustrative 60) | Capability-profile parameter verified by test. |
| NET-005 | Latency deviation alert threshold | % above baseline at p99 | 25 (illustrative) | Capability-profile parameter tuned to measurement noise. |
| NET-005 | Baseline percentile set | percentiles | p50, p99, p99.9 (illustrative) | Tail latency drives synchronous collective step time. |
| NET-006 | Link flap isolation threshold | flaps per hour | 3 (illustrative) | Capability-profile parameter. |
| NET-006 | Post-FEC uncorrectable codeword threshold | count per interval | Any non-zero sustained (illustrative) | Post-FEC errors become packet loss; vendor guidance applies. |
| NET-006 | Pre-FEC BER warning threshold | BER | Vendor/PHY specific (illustrative: one order of magnitude below FEC limit) | Set from IEEE 802.3 FEC capability and vendor guidance. |
| NET-007 | PFC watchdog detection time | ms | Vendor default unless tuned (illustrative 200) | Configured per NOS; verified by test. |
| NET-007 | Maximum tolerated pause propagation | hops from congestion point | 1 (illustrative) | Design objective to keep pause local. |
| NET-007 | Lossless traffic classes | count | 1 or 2 (illustrative) | Fewer lossless classes reduce deadlock and headroom exposure. |
| NET-008 | Collective acceptance target | % of design bus bandwidth | 90 (illustrative) | Capability-profile parameter derived from performance outcome. |
| NET-008 | Benchmark periodic interval | days | 30 (illustrative) | Detects slow drift. |
| NET-009 | Checkpoint write window | s | Derived from checkpoint size and goodput target (illustrative 120) | Capability-profile parameter; see RES-016. |
| NET-009 | Tolerated collective degradation during checkpoint | % bus bandwidth reduction | 10 (illustrative) | Capability-profile parameter. |
| NET-010 | Front-end peak utilisation ceiling | % of uplink capacity | 70 (illustrative) | Capability-profile parameter for headroom. |
| NET-011 | Gateway capacity alert threshold | % of rated connections/throughput | 70 (illustrative) | Capability-profile parameter. |
| NET-011 | Tolerated failover disruption | s | Set by inference availability outcome (illustrative 5) | Derived from Service Outcome. |
| NET-012 | Guaranteed bandwidth share per tenant class | % of link | Contract-specific (illustrative 25) | Set by tenant commitments (GOV-021). |
| NET-012 | Tolerated cross-tenant degradation | % throughput reduction | 5 (illustrative) | Capability-profile parameter. |
| NET-014 | Console reachability check interval | days | 30 (illustrative) | Capability-profile parameter. |
| NET-015 | OOB power autonomy | h | Equal to or greater than black-start sequence duration (illustrative 4) | Derived from RES-014 restoration sequence. |
| NET-015 | OOB test interval | months | 6 (illustrative) | Capability-profile parameter. |
| NET-016 | Break-glass post-use review time | h | 24 (illustrative) | Capability-profile parameter. |
| NET-016 | Break-glass test interval | months | 6 (illustrative) | Capability-profile parameter. |
| NET-017 | Maximum containment fill | % cross-section | Per adopted standard (illustrative 50) | From adopted cabling standard; site-specific. |
| NET-017 | Fibre link loss acceptance margin | dB below transceiver budget | Set from optics budget (illustrative 1.0) | Ensures operating margin; see NET-018. |
| NET-018 | Rx power warning margin | dB above receiver sensitivity | 2 (illustrative) | Capability-profile parameter derived from vendor budget. |
| NET-018 | Optics failure-rate review trigger | failures per 1000 per month | Site baseline-derived (illustrative) | Triggers lot-level analysis. |
| NET-019 | Record update time after change | h | 24 (illustrative) | Capability-profile parameter. |
| NET-020 | Path record accuracy target | % of audited links correct end-to-end | 99 (illustrative) | Capability-profile parameter. |
| NET-020 | Audit sample size | links per audit | Statistically justified (illustrative 200) | Sampling per AIDCF-009. |
| NET-021 | Controller failover time tolerance | s | Below job collective timeout margin (illustrative 60) | Capability-profile parameter. |
| NET-021 | Controller failover test interval | months | 12 (illustrative) | Capability-profile parameter. |
| NET-022 | Drift detection interval | h | 24 (illustrative) | Capability-profile parameter. |
| NET-022 | Canary stage size | % of devices | ≤5 (illustrative) | Limits firmware common-mode exposure (X08). |
| NET-023 | Telemetry collection interval for congestion counters | s | 10 (illustrative) | Capability-profile parameter; finer for diagnosis. |
| NET-023 | Telemetry retention | days | Per evidence retention class (illustrative 395) | AIDCF-008 retention classes. |
| NET-024 | Time offset tolerance | ms | Workload- and log-correlation-dependent (illustrative 1 for NTP; sub-microsecond for PTP where required) | Capability-profile parameter. |
| NET-024 | Holdover duration | h | Covers time-source repair time (illustrative 24) | Capability-profile parameter. |

## 10 Evidence expectations by claim type

The NET controls use all five claim types. The following table summarises which controls carry each claim type, the evidence classes required by their profiles (AIDCF-008) and the typical decisive evidence.

| Control | Claim type | Profile tier | Required classes | Quality floor | Sufficiency floor | Mandatory items |
|---|---|---|---|---|---|---|
| NET-003 | DESIGN | CP-1 | E1+E7 | P3 F3 C2 R3 T2 I2 | S3 | Per-tier ratio table; Workload-justification analysis |
| NET-017 | DESIGN | CP-1 | E1+E7 | P3 F3 C2 R3 T2 I2 | S3 | Site cabling standard |
| NET-001 | IMPLEMENTATION | CP-2 | E1+E2+E3 | P3 F3 C3 R3 T3 I2 | S4 | Discovered topology export; Design-to-as-built reconciliation report |
| NET-002 | IMPLEMENTATION | CP-2 | E1+E2+E3 | P3 F3 C3 R3 T3 I2 | S4 | Route evidence for each external circuit in a redundant group; Shared-segment register |
| NET-010 | IMPLEMENTATION | CP-2 | E1+E2+E3 | P3 F3 C3 R3 T3 I2 | S3 | Configuration reconciliation; Attachment inventory |
| NET-013 | IMPLEMENTATION | CP-2 | E1+E2+E3 | P3 F3 C3 R3 T3 I2 | S3 | Device-to-segment inventory; Reachability evidence |
| NET-014 | IMPLEMENTATION | CP-2 | E1+E2+E3 | P3 F3 C3 R3 T3 I2 | S3 | Console mapping inventory; Reachability check reports |
| NET-018 | IMPLEMENTATION | CP-2 | E1+E2+E3 | P3 F3 C3 R3 T3 I2 | S3 | Installed optics inventory; Qualified-optics matrix |
| NET-020 | IMPLEMENTATION | CP-2 | E1+E2+E3 | P3 F3 C3 R3 T3 I2 | S3 | Audit records; Electronic reconciliation |
| NET-005 | OPERATION | CP-3 | E2+E3 | P3 F3 C3 R3 T3 I3 | S3 | Baseline report; Probe telemetry for the period |
| NET-006 | OPERATION | CP-3 | E2+E3 | P3 F3 C3 R3 T3 I3 | S3 | Port error telemetry; Isolation/drain ticket history |
| NET-011 | OPERATION | CP-3 | E2+E3 | P3 F3 C3 R3 T3 I3 | S3 | Capacity telemetry; Failover evidence |
| NET-019 | OPERATION | CP-3 | E2+E3 | P3 F3 C3 R3 T3 I3 | S3 | Work orders; Link-event logs for reconciliation |
| NET-022 | OPERATION | CP-3 | E2+E3 | P3 F3 C3 R3 T3 I3 | S4 | Drift reports; Staged change records; Restore test record |
| NET-023 | OPERATION | CP-3 | E2+E3 | P3 F3 C3 R3 T3 I3 | S3 | Coverage report; Gap reports |
| NET-007 | EFFECTIVENESS | CP-4 | E2+E3+E4 | P3 F4 C3 R4 T3 I3 | S4 | Configuration reconciliation; Incast test results; Pause-storm/watchdog test result |
| NET-008 | EFFECTIVENESS | CP-4 | E2+E3+E4 | P3 F4 C3 R4 T3 I3 | S4 | Raw benchmark outputs; Approved targets |
| NET-009 | EFFECTIVENESS | CP-4 | E2+E3+E4 | P3 F4 C3 R4 T3 I3 | S4 | Checkpoint-burst test result; Traffic-class configuration extract |
| NET-012 | EFFECTIVENESS | CP-4 | E2+E3+E4 | P3 F4 C3 R4 T3 I3 | S4 | Reachability test results; Configuration-to-tenant reconciliation |
| NET-016 | EFFECTIVENESS | CP-4 | E2+E3+E4 | P3 F4 C3 R4 T3 I3 | S4 | Test records; Use and rotation records |
| NET-021 | EFFECTIVENESS | CP-4 | E2+E3+E4 | P3 F4 C3 R4 T3 I3 | S4 | Failover test record; Placement analysis |
| NET-024 | EFFECTIVENESS | CP-4 | E2+E3+E4 | P3 F4 C3 R4 T3 I3 | S4 | Circular-dependency analysis; Failure test records |
| NET-004 | RESILIENCE | CP-5 | E1+E2+E3+E4 | P4 F4 C4 R4 T3 I3 | S5 | Fault-domain register; At least one test or analysed incident per fault-domain class; Power/cooling co-location analysis |
| NET-015 | RESILIENCE | CP-5 | E1+E2+E3+E4 | P4 F4 C4 R4 T3 I3 | S5 | OOB dependency analysis; Isolation test record |

Typical decisive evidence by claim type:

- **DESIGN** (NET-003, NET-017): approved design documents with analysis (E1 plus E7), for example a traffic-matrix analysis showing why a 1:1 back-end and 3:1 front-end ratio is adequate. Design evidence alone never supports operating or effectiveness claims.
- **IMPLEMENTATION** (NET-001, NET-002, NET-010, NET-013, NET-014, NET-018, NET-020): machine-discovered state (LLDP or subnet-manager topology, optics inventory, configuration extracts) reconciled to design. Discovery output obtained by the assessor is stronger than an operator-produced summary.
- **OPERATION** (NET-005, NET-006, NET-011, NET-019, NET-022, NET-023): telemetry and records over a representative period that includes at least one maintenance window, with exceptions and incidents reviewed.
- **EFFECTIVENESS** (NET-007, NET-008, NET-009, NET-012, NET-016, NET-021, NET-024): representative tests (incast, pause-storm, collective benchmarks, checkpoint bursts, isolation, failover) plus supporting configuration and telemetry.
- **RESILIENCE** (NET-004, NET-015): tested or analysed failure and recovery across states, with cross-domain power/cooling mapping and independent witnessing.

Evidence pitfalls specific to NET:

- **Vendor reference designs** are E1 for design intent only; they do not evidence the as-built fabric.
- **Benchmarks under non-production settings** (different collective library version, environment variables or NIC firmware) are not representative and shall be recorded as coverage gaps (U5).
- **Average utilisation dashboards** do not evidence congestion behaviour; per-class pause, ECN mark and drop counters at adequate resolution are needed.
- **Carrier diversity letters** without route detail are E1 declarations; corroborate with route maps or entry walk-downs.

## 11 Assessment guidance

### 11.1 Scoping

1. Enumerate every network supporting the Capability Instance: each back-end fabric and plane, scale-up domains, storage network, front-end, management/OOB and WAN/DCI.
2. Record ownership and evidence access per network, especially provider-operated segments.
3. Identify which networks are in scope for which gates using the mappings in Section 8.

### 11.2 Sequencing the assessment

A practical order is: topology and path records (NET-001, NET-020) → physical layer (NET-017, NET-018) → configuration baseline (NET-022) → telemetry coverage (NET-023) → performance and congestion (NET-005 to NET-009) → isolation and fault domains (NET-004, NET-012) → management and recovery (NET-013 to NET-016, NET-021, NET-024). Topology and configuration reconciliation come first because every later result depends on knowing what is actually deployed.

### 11.3 Sampling

Fabrics are large and homogeneous; sampling is acceptable for physical inspection and configuration review provided the sample is stratified by device role (leaf, spine, super-spine), plane, hardware generation and recent change. Automated full-population reconciliation is preferred where read-only access permits. Sampling rationale shall follow AIDCF-009.

### 11.4 Interpreting results

- A collective benchmark that meets target at full scale but fails at the declared degraded scale is PARTIAL for NET-008, not CONFORMING.
- A congestion-control design that is correct but whose configuration has drifted on a minority of switches is NONCONFORMING for NET-007 unless the drift is shown to be immaterial, because a single misconfigured switch can originate a pause storm.
- Absence of observed pause storms in telemetry is a negative claim; it requires evidence that telemetry would have detected one (resolution, coverage) before it can be relied upon.

### 11.5 Key assessment questions by family

- **NET-01 Scale-up and scale-out fabrics.** Does discovered topology match design on every plane, including nodes replaced since commissioning? Is each oversubscription ratio justified by the declared workload mix, including all-to-all traffic from expert-parallel models? What is the measured, not asserted, effect of losing one leaf, one spine, one plane and the primary subnet manager or controller, and do redundant fabric elements share a UPS output, switchboard section or cooling zone?
- **NET-02 Performance and congestion control.** Are latency baselines current for the deployed NOS and firmware? Are FEC, symbol-error, flap and NIC retransmission thresholds defined and acted upon? Has a pause-storm or watchdog test been run for the current NIC firmware, and has deadlock been analysed for failure routing as well as normal routing? Do collective benchmarks meet targets at the declared degraded scale?
- **NET-03 Storage and service networks.** Has a synchronised checkpoint burst been tested at declared scale with concurrent collective measurement? Are metadata services reachable over redundant paths? Are inference gateways redundant, with session behaviour on failover understood? Has RDMA-layer isolation been tested separately from IP-layer isolation on shared fabrics?
- **NET-04 Management and OOB networks.** Can every BMC, switch, PDU and storage controller be reached out of band? Does OOB depend on production identity, DNS, the production fabric or the primary carrier? Has break-glass been exercised with central authentication unreachable?
- **NET-05 Physical connectivity and optics.** Are installed optics on the qualified matrix, including module firmware? Do field labels and path records agree for an independently selected sample? Do link-event logs reconcile to approved work orders, and has anyone worked on both members of a redundant path group at once?
- **NET-06 Network control and observability.** Is NOS, NIC, optics and controller firmware held to a baseline with drift detection? Are changes staged so that no single change reaches all planes? Does telemetry resolution suffice to see congestion events? Are time, DNS, DHCP, IPAM and AAA free of circular dependencies on the cluster they serve?

**DG-NET-REQ-003** An assessor shall not record NET-007 as CONFORMING for a lossless Ethernet fabric unless evidence of a pause-storm or watchdog test, or an analysed real pause-storm event, is available for the deployed NOS and NIC firmware versions.

**DG-NET-REQ-004** An assessor shall record the collective library version, NIC firmware version and NOS version against every benchmark or congestion test result used as evidence, and shall treat a later change of any of these as a reassessment trigger for that evidence.

## 12 Testing safety

Many NET effectiveness and resilience tests are disruptive. Incast tests, pause-storm tests, switch or plane removal, subnet-manager failover, controller failover, front-end gateway failover and DCI circuit failover can each stall or terminate production workloads, and some (power-feed removal to switch rows) involve hazardous energy.

**DG-NET-REQ-005** No disruptive network test shall be performed on a production fabric without written authorisation from the service owner and the network change authority, a scheduled window, workload drain or explicit workload-owner consent, a defined abort criterion and abort authority, and a rollback plan.

**DG-NET-REQ-006** Tests that remove power from network equipment shall additionally be authorised under the site permit-to-work regime (OPS-007) by the electrical authority.

**DG-NET-REQ-007** Assessors shall use read-only credentials and interfaces for discovery and configuration extraction; any credential with write capability issued for an assessment shall be time-bound and revoked on completion.

Preferred safe alternatives, in line with the AIDCF-004 safe validation hierarchy, are: analysis of real events with good telemetry (V2); staging fabrics at representative scale with identical software and parameters (V3/V5 with a representativeness argument); and segmented tests during planned maintenance. Scans of management networks that include OT gateways shall follow SEC-009 restrictions.

## 13 UNKNOWN hot-spots

The following are common sources of UNKNOWN Records in NET assessments, with typical type and severity (AIDCF-008 U-types; SPEC §5.7 severity):

| Hot-spot | Typical type | Typical severity | Resolution route |
|---|---|---|---|
| As-built topology not discoverable for a fabric | U1/U5 | US4 (CG-08) | Read-only discovery; witnessed port audit |
| NIC-side congestion parameters not extractable | U2 | US4 (CG-08) where lossless | Host-side tooling under platform team; vendor support |
| Carrier refuses route disclosure | U2/U10 | US3, US4 if sole DCI path | Contractual diversity clause; entry and first-mile survey |
| Benchmarks run under non-production settings | U5 | US4 (CG-08) | Rerun with production environment captured |
| Subnet-manager failover never tested at scale | U8 | US4 (CG-09/CG-08) | Staging test at scale; analysed incident |
| OOB dependency on production identity or DNS unanalysed | U10 | US4 (CG-10) | Dependency analysis; simulated isolation test |
| Optics firmware not in baseline | U5 | US3 | Extend inventory to module firmware |
| Telemetry gaps over assessment period | U5 | US2 | Pipeline health records; alternative counter snapshots |
| Provider-operated front-end or cross-connects | U2 | US3 | E5 provider assurance; evidence rights (SUP-006) |

## 14 Interfaces with other domains

| Domain | Interface | Key controls |
|---|---|---|
| CMP | Rail/plane attachment, scale-up domains, NIC firmware, job placement across fault domains | CMP-005, CMP-006, CMP-008, CMP-013 |
| STO | Checkpoint and dataset paths, metadata service reachability | STO-005, STO-008, STO-017 |
| POW | Power paths of switches, controllers and OOB; load-step limits during restoration | POW-015, POW-024 |
| THM | Switch cooling, liquid-cooled switch dependency on CDUs | THM-010, THM-024 |
| DEP | Shared routes, telecom dependency, provider boundaries | DEP-007, DEP-010, DEP-018 |
| SEC | Management segmentation, controller security, remote access, zoning | SEC-007, SEC-009, SEC-010, SEC-012 |
| OPS | Change assessment, permit-to-work, method statements | OPS-006, OPS-007, OPS-018 |
| RES | Site fault-domain model, recovery dependencies and sequencing | RES-005, RES-013, RES-014 |
| SUP | Optics provenance, counterfeit prevention, firmware supply | SUP-010, SUP-014, SUP-015 |
| PHY | Fire zones for cable routes, physical access to patching | PHY-010, PHY-013 |

## 15 Informative references

Cited at document level; no clause-level text is reproduced.

- InfiniBand Trade Association: InfiniBand Architecture Specification (Volumes 1 and 2) and the RoCEv2 annex.
- IEEE 802.1Q (bridges and bridged networks); IEEE 802.1Qbb (Priority-based Flow Control); IEEE 802.1Qaz (Enhanced Transmission Selection and DCBX).
- IEEE 802.3 (Ethernet, including optical PHYs and FEC).
- IETF RFC 3168 (Explicit Congestion Notification); RFC 7938 (BGP in large-scale data centres); RFC 5905 (NTPv4); RFC 8915 (Network Time Security); RFC 7011 (IPFIX).
- IEEE 1588 (Precision Time Protocol).
- Ultra Ethernet Consortium specification (UEC 1.0).
- OSFP MSA and QSFP-DD MSA module specifications; CMIS.
- ANSI/TIA-942; ANSI/TIA-606; ISO/IEC 11801 series; ISO/IEC 14763 series; IEC 61300-3-35; EN 50600 series / ISO/IEC 22237 series.
- OpenConfig gNMI and data models; sFlow version 5.
- ISA/IEC 62443-3-3 and NIST SP 800-82 Rev. 3 (for management-network segmentation context).
- AIDCF-004, AIDCF-005, AIDCF-008, AIDCF-009, AIDCF-010, AIDCF-013, AIDCF-014.

## 16 Control summary

| Control ID | Title | Control type | Required AL | Claim type | Gate mappings |
|---|---|---|---|---|---|
| MCF-NET-001 | Fabric Topology | PREVENTIVE | AL3 | IMPLEMENTATION | CG-08 CRITICAL; CG-02 SUPPORTING |
| MCF-NET-002 | Path Diversity | PREVENTIVE | AL3 | IMPLEMENTATION | CG-03 SUPPORTING; CG-08 SUPPORTING; CG-09 SUPPORTING |
| MCF-NET-003 | Oversubscription | PREVENTIVE | AL2 | DESIGN | CG-08 SUPPORTING |
| MCF-NET-004 | Fabric Fault-Domain Design | PREVENTIVE | AL5 | RESILIENCE | CG-09 CRITICAL; CG-08 SUPPORTING; CG-03 SUPPORTING |
| MCF-NET-005 | Latency Baseline | DETECTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-NET-006 | Loss and Retransmission | DETECTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-NET-007 | Congestion Control | PREVENTIVE | AL5 | EFFECTIVENESS | CG-08 CRITICAL; CG-09 SUPPORTING |
| MCF-NET-008 | Collective Communication Performance | DETECTIVE | AL5 | EFFECTIVENESS | CG-08 CRITICAL |
| MCF-NET-009 | Storage Fabric | PREVENTIVE | AL5 | EFFECTIVENESS | CG-08 CRITICAL; CG-10 SUPPORTING |
| MCF-NET-010 | Frontend Network | PREVENTIVE | AL3 | IMPLEMENTATION | CG-08 SUPPORTING |
| MCF-NET-011 | Service Gateways | DETECTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-NET-012 | Traffic Isolation | PREVENTIVE | AL5 | EFFECTIVENESS | CG-09 SUPPORTING; CG-08 SUPPORTING; CG-15 SUPPORTING |
| MCF-NET-013 | Management Separation | PREVENTIVE | AL3 | IMPLEMENTATION | CG-15 SUPPORTING; CG-08 SUPPORTING |
| MCF-NET-014 | Console Access | CORRECTIVE | AL3 | IMPLEMENTATION | CG-10 SUPPORTING; CG-15 SUPPORTING |
| MCF-NET-015 | OOB Resilience | RECOVERY | AL5 | RESILIENCE | CG-10 CRITICAL; CG-15 SUPPORTING; CG-03 SUPPORTING |
| MCF-NET-016 | Break-Glass Access | RECOVERY | AL5 | EFFECTIVENESS | CG-15 SUPPORTING; CG-10 SUPPORTING |
| MCF-NET-017 | Cabling Standards | DIRECTIVE | AL2 | DESIGN | CG-08 SUPPORTING |
| MCF-NET-018 | Optics Compatibility | PREVENTIVE | AL3 | IMPLEMENTATION | CG-08 SUPPORTING; CG-03 SUPPORTING |
| MCF-NET-019 | Cross-Connect Control | PREVENTIVE | AL4 | OPERATION | CG-14 SUPPORTING; CG-08 SUPPORTING |
| MCF-NET-020 | Path Documentation | DETECTIVE | AL3 | IMPLEMENTATION | CG-02 SUPPORTING; CG-03 SUPPORTING; CG-10 SUPPORTING |
| MCF-NET-021 | Controller Resilience | PREVENTIVE | AL5 | EFFECTIVENESS | CG-08 SUPPORTING; CG-09 SUPPORTING; CG-10 SUPPORTING |
| MCF-NET-022 | Configuration Management | PREVENTIVE | AL4 | OPERATION | CG-14 CRITICAL; CG-08 SUPPORTING; CG-10 SUPPORTING |
| MCF-NET-023 | Flow Telemetry | DETECTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-NET-024 | Time and Core Services | PREVENTIVE | AL5 | EFFECTIVENESS | CG-08 SUPPORTING; CG-03 SUPPORTING; CG-10 SUPPORTING |

## 17 Worked synthetic example

*This example is entirely synthetic. The site, figures and results are invented to illustrate the method and do not describe any real facility, organisation or test.*

**Context.** Synthetic site S-1 hosts Capability Instance CI-T1, a training cluster of 2,048 accelerators in 256 nodes, with an eight-plane rail-optimised RoCEv2 back-end fabric, a dedicated storage plane, a leaf-spine front-end and a separate OOB network. The decision question is whether CI-T1 can sustain its training throughput outcome (≥ 85% of design step rate at full scale, ≥ 70% with one plane unavailable) and recover within a 12-hour RTO after a site-wide power event, as of the assessment date. Tolerances come from RES-001.

**Selected NET results.**

| Control | Claim type | Evidence obtained | Result |
|---|---|---|---|
| MCF-NET-001 | IMPLEMENTATION | Assessor-run LLDP discovery reconciled to design; 3 mis-mapped NIC ports on two recently replaced nodes, corrected during assessment with change records | CONFORMING (Findings closed with evidence) |
| MCF-NET-004 | RESILIENCE | Plane-loss test witnessed; leaf-loss analysed from a real incident; subnet-manager equivalent not applicable (Ethernet); both spine groups of plane 3 found on one UPS output | PARTIAL (Finding: co-located redundancy) |
| MCF-NET-007 | EFFECTIVENESS | Design and full configuration reconciliation; incast test passed; no pause-storm or watchdog test for current NIC firmware | UNKNOWN (U5, US4) |
| MCF-NET-008 | EFFECTIVENESS | Benchmarks at full and one-plane-down scale with production environment captured; 91% and 78% of design bus bandwidth | CONFORMING |
| MCF-NET-009 | EFFECTIVENESS | Checkpoint burst test at full scale; checkpoint window met; collective degradation 6% | CONFORMING |
| MCF-NET-015 | RESILIENCE | OOB design reviewed; simulated isolation test passed; OOB switches on protected supply with 6 h autonomy | CONFORMING |
| MCF-NET-022 | OPERATION | Six months of drift reports and staged changes; one emergency NOS change applied to two planes simultaneously, retrospectively reviewed | PARTIAL (Finding) |

**Gate roll-up (SPEC §6.2).**

- **CG-08**: CRITICAL NET controls NET-001, NET-008 and NET-009 are CONFORMING; NET-007 is UNKNOWN at US4. No CRITICAL control is NONCONFORMING or PARTIAL, so the gate is not FAIL on NET evidence; because a CRITICAL control is UNKNOWN, CG-08 = **UNKNOWN** (subject also to CMP and STO critical controls).
- **CG-09**: NET-004 is CRITICAL and PARTIAL, so CG-09 = **FAIL**. The Finding (two spine groups of one plane on one UPS output) is material because loss of that UPS output would remove an entire plane, reducing capacity to the one-plane-down level; the gate fails because PARTIAL never yields PASS for a CRITICAL control.
- **CG-10**: NET-015 is CONFORMING; the gate result depends on RES, POW, THM, CMP and STO critical controls.
- **CG-14**: NET-022 is CRITICAL and PARTIAL, so CG-14 = **FAIL** for the network scope.

**Decision effect.** With CG-09 and CG-14 at FAIL and CG-08 at UNKNOWN, the decision recommendation is bounded by the AIDCF-010 ceilings for those gates; the US4 UNKNOWN additionally triggers CG-12. Recommended actions: re-home one spine group of plane 3 to a different UPS output and retest plane loss; perform a watchdog test in a staging fabric with production NIC firmware or in an authorised window; amend the emergency change procedure so emergency NOS changes are applied plane-by-plane. Each action is linked to a reassessment trigger so that closure re-evaluates the affected gates rather than the score alone.

**Score view.** The NET domain score is computed as the mean of scored controls (CONFORMING 100, PARTIAL 50), excluding the UNKNOWN; with an UNKNOWN at US4 in scope, the band is withheld ("Band withheld (coverage/UNKNOWN)"). The score does not override the gate failures.
