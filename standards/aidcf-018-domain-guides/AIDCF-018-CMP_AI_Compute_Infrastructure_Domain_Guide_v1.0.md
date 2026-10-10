# AIDCF-018-CMP AI Compute Infrastructure Domain Guide

## Document control

| Element | Value |
|---|---|
| Document ID | AIDCF-018-CMP |
| Title | AI Compute Infrastructure Domain Guide |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Domain | CMP (AI Compute Infrastructure) |
| Controls covered | MCF-CMP-001 to MCF-CMP-024 (families CMP-01 to CMP-06) |
| Normative basis | AIDCF-007A (control registry), AIDCF-008 (evidence model), AIDCF-010 (scoring and gates) |
| Related documents | AIDCF-003, AIDCF-004, AIDCF-009, AIDCF-013, AIDCF-014, AIDCF-018-THM, AIDCF-018-STO, AIDCF-018-NET |

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-10 | Initial issue: domain guidance aligned to the rewritten CMP control records. |

Requirements in this guide are identified DG-CMP-REQ-NNN. The control records in AIDCF-007A remain the normative statement of each control; where this guide restates a control, the registry record prevails.

## 1 Purpose and scope

This guide explains how to apply the 24 CMP controls when assessing whether the accelerator compute supporting a Capability Instance delivers the function, performance and integrity its Service Outcomes require, across normal, degraded, maintenance, change and recovery states.

In scope:

- **Accelerators and nodes**: GPUs, TPUs and other AI accelerators; host CPUs, memory and local storage; NICs and DPUs; baseboard management controllers (BMCs) and platform firmware.
- **Rack-scale systems**: integrated compute trays, scale-up switch trays, power shelves, busbars and liquid manifolds delivered as a rack unit.
- **Cluster structure**: scale-up domains (accelerators joined by a high-bandwidth, low-latency interconnect, from a single node to a rack or multi-rack domain), cluster topology, partitions and the mapping of compute to facility fault domains.
- **Capacity and scheduling**: usable accelerator capacity, schedulers and orchestrators, reservations and contention.
- **Firmware, drivers and software stack**: firmware baselines, driver and library compatibility, upgrade and rollback.
- **Health and observability**: accelerator telemetry, node health checks, reliability, availability and serviceability (RAS) events including ECC errors and vendor fatal-error events, silent data corruption screening and performance baselines.
- **Lifecycle**: provisioning and burn-in, spares and RMA, rebuild and re-qualification, secure retirement.

Out of scope here: the scale-out and storage fabrics (NET), storage systems (STO), facility power and cooling (POW, THM), and identity and control-plane security as such (SEC), although each is an interface in §14. Model and application behaviour above the infrastructure (for example model quality or safety) is outside AIDCF and is handled by AI Trust Graph integration (AIDCF-005).

## 2 Why this domain matters for AI capability

The compute domain is where the facility's power and cooling are turned into AI capability, and where several properties specific to AI workloads concentrate risk.

**Synchronous scale.** Large training jobs run as a single program across thousands of accelerators exchanging gradients or activations at every step. The job advances at the speed of its slowest participant and generally halts when any participant fails. A single degraded link, throttled accelerator or flaky node therefore affects the whole job, and the probability that some component in a large job fails during a long run is high. Reliability engineering for AI compute is consequently about rapid detection, isolation and restart rather than preventing every component failure.

**Integrity, not only availability.** An accelerator that produces wrong results without signalling an error (silent data corruption) is more damaging than one that fails, because corrupted values can propagate into checkpoints and into the trained model. RAS telemetry, known-answer screening and linkage from faulty hardware to affected checkpoints (MCF-CMP-019) are integrity safeguards for the Service Outcome.

**Fleet homogeneity as a common mode.** AI clusters are built from large numbers of identical nodes with identical firmware and software. This makes performance predictable but means a defective firmware release, driver or configuration can affect every node at once (AIDCF-004 scenario X08). Staged rollout and rollback (MCF-CMP-015, -016) are the principal containment safeguards.

**Usable versus installed capacity.** At any time a fraction of accelerators is drained, failed, awaiting RMA, reserved or throttled. Capability depends on usable capacity, which can be materially below installed capacity and which is sensitive to facility conditions: thermal or power throttling reduces delivered compute without any device appearing failed (MCF-CMP-009).

**Coupling to facility.** Rack-scale systems integrate liquid cooling and high-power distribution into the IT product. The boundary between "facility" and "IT" therefore runs through the rack, and joint acceptance of power, liquid and structural interfaces (MCF-CMP-003) is essential.

## 3 Reference patterns and variants

| Pattern | Description | Characteristic assurance concerns |
|---|---|---|
| C1 Node-scale scale-up | Servers with 4–8 accelerators joined by an in-node interconnect; scale-out fabric between nodes | Node health, rail-aligned fabric attachment, scale-out dominates collective performance |
| C2 Rack-scale scale-up | Rack-level domains in which many accelerators share a switched interconnect across trays; integrated liquid cooling and power shelves | Domain integrity across trays and switch trays; one rack becomes one large fault domain; facility interface acceptance |
| C3 Pod or multi-rack domain | Accelerator pods with inter-rack scale-up links (electrical or optical), common in some TPU-class and custom accelerator designs | Link health over long reach; pod-level partitioning and reconfiguration; pod as fault domain |
| C4 Heterogeneous fleet | Mixed accelerator generations or vendors behind one scheduler | Scheduling constraints; compatibility matrix; capacity accounting by type |
| C5 Multi-tenant partitioned cluster | Cluster shared by tenants or projects with quotas and isolation, possibly including accelerator-level partitioning | Partition enforcement across scheduler, fabric and storage; admin scope |
| C6 Inference fleet | Many smaller replicas serving requests, autoscaled | Health-based routing; capacity headroom for demand peaks; rolling upgrades |
| C7 Provider-operated capacity | Compute consumed as a cloud or managed service | Evidence through the service interface; residual UNKNOWNs for undisclosed layers |

## 4 Required functions and capability linkage

| Required Function | Description | Principal controls |
|---|---|---|
| RF-CMP-1 Provide accelerated compute | Deliver specified accelerator, memory and host resources per node | MCF-CMP-001, -002, -003 |
| RF-CMP-2 Coordinate accelerators | Provide healthy scale-up domains and topology for collective operations | MCF-CMP-005, -006 |
| RF-CMP-3 Allocate capacity | Schedule jobs onto healthy, topology-appropriate, permitted resources | MCF-CMP-007, -009, -010, -011, -012 |
| RF-CMP-4 Maintain a known configuration | Keep firmware, drivers and configuration at an approved baseline | MCF-CMP-004, -013, -014 |
| RF-CMP-5 Change safely | Introduce and reverse changes without common-mode failure | MCF-CMP-015, -016, -021 |
| RF-CMP-6 Detect degradation and corruption | Detect failing, degraded and corrupting hardware before impact | MCF-CMP-017, -018, -019, -020 |
| RF-CMP-7 Contain failure | Limit the capacity and outcomes affected by a single fault domain | MCF-CMP-008 |
| RF-CMP-8 Restore capacity | Repair, replace, rebuild and re-qualify nodes | MCF-CMP-022, -023 |
| RF-CMP-9 Retire safely | Remove hardware without data, credential or inventory exposure | MCF-CMP-024 |

The Capability Instance links to these functions through Service Outcomes such as "sustained training throughput for job class J", "inference latency within tolerance at demand D" and "model integrity preserved". The quantitative bridge is usable accelerator capacity (MCF-CMP-009) for availability and throughput outcomes, and RAS and SDC detection (MCF-CMP-019) for integrity outcomes.

## 5 Dependencies, fault domains, common-mode concerns

### 5.1 Dependencies

Compute depends on: facility power at rack level including power-shelf redundancy (POW-04); liquid and air cooling within OEM limits (THM-02, THM-03); scale-out and management networks (NET-01, NET-04); storage for data, checkpoints and images (STO); time synchronisation (NET-06); identity and secrets for BMCs and cluster services (SEC-01); the provisioning system and image repository; OEM support, RMA logistics and spares (SUP-05, DEP-03); and the scheduler control plane.

### 5.2 Fault domains

Compute fault domains nest from accelerator → node or tray → scale-up domain → rack → row or pod → hall. They intersect facility fault domains (power feed group, CDU loop, CRAH zone) and fabric fault domains (leaf, spine plane, rail). A training job's effective fault domain is the union of all domains its participants depend on. MCF-CMP-008 requires the mapping of every node to its facility and fabric domains and a limit on the share of a Capability Instance's capacity in any one. MCF-CMP-005 makes the topology machine-readable so that the scheduler can place jobs with this knowledge.

### 5.3 Common-mode concerns

- Identical firmware, driver or OS image deployed fleet-wide in one step.
- A single provisioning service, image repository or certificate authority needed to rebuild every node, located in the same fault domain as the event it recovers from.
- A single scheduler controller or database without tested failover.
- BMCs sharing credentials or reachable from a flat management network, giving one compromise fleet-wide reach (CG-15).
- One accelerator production lot with a latent defect, deployed across all racks.
- Facility common modes: all scale-up domains of a large job on one CDU loop or one power feed group.
- Single source for a long-lead component (for example a specific tray or switch tray) with no on-site spare.

## 6 Threats, hazards and failure scenarios with propagation paths to Service Outcomes

| ID | Scenario (AIDCF-004 reference) | Propagation path | Outcome effect | Principal safeguards |
|---|---|---|---|---|
| CMP-S1 | Accelerator or node failure (D6) | Accelerator raises fatal error or hangs → collective operation stalls → job times out → restart from last checkpoint on spare capacity | Lost work since last checkpoint plus restart time | MCF-CMP-018, -019 detection and drain; MCF-CMP-011 reserve; MCF-STO-018 restart |
| CMP-S2 | Scale-up domain degradation | Interconnect link retrains to reduced width → domain bandwidth falls → all jobs using domain slow → job runs at fraction of rate without failing | Silent throughput loss | MCF-CMP-006 bandwidth validation and drain; MCF-CMP-020 baselines |
| CMP-S3 | Firmware rollout common-mode failure (X08) | New firmware deployed fleet-wide → latent defect triggers under specific workload → many nodes fail or corrupt results | Capability-wide outage or integrity loss | MCF-CMP-015 staged rollout; MCF-CMP-016 rollback; MCF-CMP-013 baseline |
| CMP-S4 | Silent data corruption | Defective accelerator computes wrong values without error → gradients corrupted → loss spikes or subtle model damage → corrupted checkpoint saved and propagated | Integrity outcome defeated; possibly long rollback | MCF-CMP-019 SDC screening and linkage; MCF-STO-009, -017 |
| CMP-S5 | Thermal throttling (D6) | Coolant supply temperature above OEM point or local flow restriction → accelerators reduce clocks → synchronous job runs at speed of slowest device | Throughput below outcome without visible failure | MCF-CMP-017 throttle telemetry; MCF-CMP-009 usable capacity; THM-03 |
| CMP-S6 | Mass reboot after facility event (D6) | Power or cooling loss → many nodes reboot or are drained → provisioning and storage overwhelmed by simultaneous rebuild and restart | Recovery time beyond tolerance | MCF-CMP-023 mass rebuild; MCF-STO-008 restart storm; THM-024 staged readmission |
| CMP-S7 | Golden-image corruption (D6) | Corrupted or misconfigured image promoted → rebuilt nodes fail or behave inconsistently | Spreading degradation during recovery (X15) | MCF-CMP-004 baseline hashes; MCF-CMP-021 acceptance |
| CMP-S8 | Scheduler failure (D6) | Scheduler controller fails without failover → no new jobs placed; running jobs may continue but cannot restart | Recovery blocked | MCF-CMP-010 HA |
| CMP-S9 | BMC compromise | Default or shared BMC credentials → attacker reflashes firmware or powers off nodes at scale | Capability-wide outage; integrity concerns | MCF-CMP-002 BMC hardening; MCF-CMP-013 attestation; SEC-01, SEC-02 |
| CMP-S10 | Expansion creates stranded compute (X17) | New racks installed before power, cooling or fabric capacity is ready → accelerators installed but unusable | Installed capacity reported but not usable | MCF-CMP-003 joint acceptance; MCF-CMP-009 |
| CMP-S11 | Long-lead spare after rare failure (X12) | Rack-scale switch tray fails → no spare on site → whole rack-scale domain unavailable for weeks | Large capacity loss | MCF-CMP-022 spares sizing |

## 7 Safeguards

- **Prevent**: approved architecture and baselines (MCF-CMP-001, -004); node configuration conformance and BMC hardening (MCF-CMP-002); joint rack acceptance (MCF-CMP-003); compatibility matrix (MCF-CMP-014); staged upgrade (MCF-CMP-015); burn-in before service (MCF-CMP-021); reservations (MCF-CMP-011); partitioning (MCF-CMP-007); fault-domain-aware placement (MCF-CMP-008, -010).
- **Detect**: telemetry (MCF-CMP-017); health checks (MCF-CMP-018); RAS and SDC detection (MCF-CMP-019); performance baselines (MCF-CMP-020); scale-up domain validation (MCF-CMP-006); usable-capacity reporting (MCF-CMP-009).
- **Contain**: automatic drain of failing nodes and domains (MCF-CMP-006, -018, -019); fault-domain limits (MCF-CMP-008); canary cohorts across fault domains (MCF-CMP-015).
- **Correct**: contention management and power-cap coordination (MCF-CMP-012); spares and RMA (MCF-CMP-022).
- **Recover**: rollback (MCF-CMP-016); rebuild and re-qualification (MCF-CMP-023).

Device attestation deserves particular mention. Where the platform supports it, measurements of firmware and device identity (for example through DMTF SPDM or TPM-based measured boot) let the operator demonstrate that the firmware running is the firmware approved, rather than relying on version strings reported by the same firmware. MCF-CMP-013 asks for attestation evidence where supported; a profile for high-assurance or sovereign capability may make it mandatory.

## 8 Critical-gate linkage

| Gate | CRITICAL controls | SUPPORTING controls |
|---|---|---|
| CG-01 | — | MCF-CMP-001, MCF-CMP-009 |
| CG-02 | — | MCF-CMP-004, MCF-CMP-005, MCF-CMP-024 |
| CG-03 | — | MCF-CMP-008, MCF-CMP-022 |
| CG-05 | — | MCF-CMP-003 |
| CG-06 | — | MCF-CMP-003, MCF-CMP-017 |
| CG-08 | MCF-CMP-006, MCF-CMP-009, MCF-CMP-013, MCF-CMP-019 | MCF-CMP-001, MCF-CMP-002, MCF-CMP-003, MCF-CMP-004, MCF-CMP-005, MCF-CMP-008, MCF-CMP-010, MCF-CMP-011, MCF-CMP-012, MCF-CMP-014, MCF-CMP-015, MCF-CMP-017, MCF-CMP-018, MCF-CMP-020, MCF-CMP-021, MCF-CMP-023 |
| CG-09 | MCF-CMP-008 | MCF-CMP-006, MCF-CMP-007, MCF-CMP-015 |
| CG-10 | MCF-CMP-023 | MCF-CMP-011, MCF-CMP-016, MCF-CMP-022 |
| CG-14 | MCF-CMP-015 | MCF-CMP-004, MCF-CMP-013, MCF-CMP-016, MCF-CMP-021 |
| CG-15 | — | MCF-CMP-002, MCF-CMP-007, MCF-CMP-010, MCF-CMP-013 |

Notes on the mapping:

- **CG-08 Compute, storage and network functional integrity** receives four CRITICAL CMP controls: scale-up domain integrity (MCF-CMP-006), usable accelerator capacity (-009), firmware baseline (-013) and error and degradation detection including SDC (-019). Together they establish that the compute function exists at the required capacity, in a known state, and with integrity failures detected. The remaining CMP controls are SUPPORTING.
- **CG-09 Failure containment** receives MCF-CMP-008 as CRITICAL: without a verified mapping and concentration limit, a single facility fault domain can remove more capacity than the outcome tolerates.
- **CG-10 Recovery readiness** receives MCF-CMP-023 as CRITICAL: compute re-qualification and mass rebuild are prerequisites for restoring the outcome after a facility event.
- **CG-14 Change control** receives MCF-CMP-015 as CRITICAL because fleet-wide firmware and software change is the dominant common-mode change risk in AI compute.
- **CG-15 Integrated digital authority** receives SUPPORTING mappings from BMC hardening (-002), partitioning (-007), scheduler administration (-010) and firmware authenticity (-013); the CRITICAL controls for CG-15 sit in SEC.

The CG-08 evidence floor is S4 with classes E2+E3+E4. CRITICAL CMP controls carry sufficiency floor S4 at minimum; MCF-CMP-008 and MCF-CMP-023, as RESILIENCE claims, carry S5.

## 9 Capability-profile parameters

Values are **illustrative defaults**; each capability profile shall set its own values with the stated basis (DG-CMP-REQ-001).

| Parameter | Unit | Illustrative default | Basis | Used by |
|---|---|---|---|---|
| Accelerators per scale-up domain | count | platform-specific (illustrative: 8 node-scale; 72 rack-scale) | Platform OEM architecture | MCF-CMP-001 |
| Scale-out bandwidth per accelerator | Gb/s | 400 (illustrative) | Fabric design; platform OEM reference architecture | MCF-CMP-001 |
| Rack power envelope | kW | 120 (illustrative) | Platform OEM data; facility power budget | MCF-CMP-001 |
| Configuration conformance coverage | % of nodes | 100 (illustrative) | Capability profile | MCF-CMP-002 |
| Conformance scan interval | days | 7 (illustrative) | Capability profile | MCF-CMP-002 |
| Nonconforming node remediation time | days | 3 (illustrative) | Capability profile | MCF-CMP-002 |
| Rack weight | kg | platform-specific (illustrative 1,500) | Platform OEM data; structural rating | MCF-CMP-003 |
| Fleet on current baseline | % of nodes | 98 (illustrative) | Capability profile | MCF-CMP-004 |
| Maximum exception age | days | 30 (illustrative) | Capability profile | MCF-CMP-004 |
| Minimum scale-up bandwidth | % of rated all-reduce bandwidth | 90 (illustrative) | Platform OEM performance data; capability profile | MCF-CMP-006 |
| Re-validation interval | days | 30 (illustrative) | Capability profile | MCF-CMP-006 |
| Link-error drain threshold | errors per hour per link | platform-specific | Platform OEM RAS guidance | MCF-CMP-006 |
| Maximum capacity fraction in a single facility fault domain | % of Capability Instance accelerators | 25 (illustrative) | Capability profile; outcome tolerance | MCF-CMP-008 |
| Job resumption time after fault-domain loss | min | 60 (illustrative) | Capability profile; checkpoint interval | MCF-CMP-008 |
| Required usable capacity | % of installed accelerators | 92 (illustrative) | Capability profile; Service Outcome | MCF-CMP-009 |
| Throttle performance threshold | % of rated clock or throughput | 95 (illustrative) | Capability profile | MCF-CMP-009 |
| Scheduler controller failover time | s | 60 (illustrative) | Capability profile | MCF-CMP-010 |
| Recovery reserve | % of job size | 5 (illustrative) | Capability profile; observed node failure rate | MCF-CMP-011 |
| Reclaim time | min | 15 (illustrative) | Capability profile | MCF-CMP-011 |
| Priority job slowdown tolerance | % versus baseline | 10 (illustrative) | Capability profile | MCF-CMP-012 |
| Firmware drift remediation time | days | 7 (illustrative) | Capability profile | MCF-CMP-013 |
| Firmware inventory coverage | % of devices | 100 (illustrative) | Capability profile | MCF-CMP-013 |
| Canary cohort size | % of fleet | 2 (illustrative) | Capability profile | MCF-CMP-015 |
| Soak period per stage | h | 72 (illustrative) | Capability profile | MCF-CMP-015 |
| Halt criterion: error-rate increase | × baseline | 2 (illustrative) | Capability profile | MCF-CMP-015 |
| Rollback time objective | h | 4 (illustrative) | Capability profile | MCF-CMP-016 |
| Telemetry interval | s | 10 (illustrative) | Capability profile | MCF-CMP-017 |
| Collection completeness | % of expected samples | 99 (illustrative) | Capability profile | MCF-CMP-017 |
| Retention | days | 90 (illustrative) | Capability profile | MCF-CMP-017 |
| Periodic health-check interval | h | 24 (illustrative) | Capability profile | MCF-CMP-018 |
| Maximum drained-node age before escalation | days | 5 (illustrative) | Capability profile | MCF-CMP-018 |
| Drain time after fatal error event | min | 5 (illustrative) | Capability profile | MCF-CMP-019 |
| SDC screening interval | days | 30 (illustrative) | Capability profile; OCP SDC practice | MCF-CMP-019 |
| Correctable ECC escalation threshold | events per day per accelerator | platform-specific | Platform OEM RAS guidance | MCF-CMP-019 |
| Performance regression threshold | % below baseline | 5 (illustrative) | Capability profile | MCF-CMP-020 |
| Burn-in duration | h | 48 (illustrative) | Capability profile; OEM guidance | MCF-CMP-021 |
| On-site spares | % of installed by class | 3 (illustrative) | Capability profile; failure-rate analysis | MCF-CMP-022 |
| RMA turnaround obligation | days | contractual | Supplier contract | MCF-CMP-022 |
| Single-node rebuild time objective | h | 2 (illustrative) | Capability profile | MCF-CMP-023 |
| Mass rebuild fraction | % of cluster | 25 (illustrative) | Capability profile | MCF-CMP-023 |
| Mass rebuild time objective | h | 12 (illustrative) | Capability profile | MCF-CMP-023 |

**DG-CMP-REQ-001** A capability profile that adopts CMP controls shall state a value and basis for each applicable parameter above, or record it as not applicable with rationale.

**DG-CMP-REQ-002** Parameters whose basis is "platform OEM" or "platform-specific" shall be sourced from the OEM's current documentation for the deployed platform generation and the source shall be cited in the profile.

## 10 Evidence expectations by claim type

| Claim type | Required AL | Controls | Typical profile tier and sufficiency floor |
|---|---|---|---|
| DESIGN | AL2 | MCF-CMP-001, MCF-CMP-005 | CP-1/S3 |
| IMPLEMENTATION | AL3 | MCF-CMP-002, MCF-CMP-003, MCF-CMP-004, MCF-CMP-007, MCF-CMP-010, MCF-CMP-013, MCF-CMP-014, MCF-CMP-021, MCF-CMP-024 | CP-2/S3, CP-4/S4 |
| OPERATION | AL4 | MCF-CMP-009, MCF-CMP-011, MCF-CMP-012, MCF-CMP-017, MCF-CMP-018, MCF-CMP-020, MCF-CMP-022 | CP-3/S4, CP-4/S4 |
| EFFECTIVENESS | AL5 | MCF-CMP-006, MCF-CMP-015, MCF-CMP-019 | CP-4/S4, CP-5/S4 |
| RESILIENCE | AL5 | MCF-CMP-008, MCF-CMP-016, MCF-CMP-023 | CP-5/S5 |

- **DESIGN (AL2)**: architecture records, workload requirement linkage, topology. E1 with E7 analysis. Evidence of design adequacy does not show the fleet is built that way.
- **IMPLEMENTATION (AL3)**: configuration and inventory evidence collected from devices (E2), reconciled to the approved baseline, with inspection or reperformance on a sample. Automated collection is preferred, but the assessor should reperform collection on a sample to confirm the tooling (DG-CMP-REQ-003).
- **OPERATION (AL4)**: telemetry, health-check logs, capacity reports and RMA records over at least the declared period (typically 90 days), with completeness evidence. Operation evidence should include periods of degradation, maintenance and change, not only steady running.
- **EFFECTIVENESS (AL5)**: tests demonstrating that a safeguard works: bandwidth tests on scale-up domains, drain automation responding to injected or real faults, SDC screening detecting known-bad hardware, staged rollouts halting on criteria.
- **RESILIENCE (AL5)**: fault-domain drain tests, mass rebuild exercises and rollback tests with timelines against objectives.

Common evidence weaknesses in this domain are dashboards without raw data (low reliability and traceability), vendor tool summaries that cannot be traced to devices, and performance claims based on vendor benchmarks rather than on the site's own topology and firmware. AIDCF-008 §50 states the governing limit: performance evidence does not prove recovery or integrity unless they are directly assessed.

**DG-CMP-REQ-003** Where a CMP IMPLEMENTATION or OPERATION claim relies on automated fleet tooling, the assessor shall reperform collection directly against a sample of devices and record any discrepancy as challenging evidence.

**DG-CMP-REQ-004** Benchmark evidence used for CMP claims shall state the topology, firmware baseline, software stack and scale at which it was obtained; benchmarks obtained on a different baseline shall not support a claim about the current baseline.

## 11 Assessment guidance

### 11.1 Sequencing

1. **Define the compute the outcome needs.** Confirm MCF-CMP-001 links architecture to workload requirements and that the required usable capacity in MCF-CMP-009 is derived from the Service Outcome.
2. **Establish the as-built state.** Reconcile the approved baseline (MCF-CMP-004), firmware (MCF-CMP-013), drivers (MCF-CMP-014), node configuration (MCF-CMP-002) and topology (MCF-CMP-005). Discrepancies here invalidate later performance evidence.
3. **Map to fault domains.** Use MCF-CMP-005 and MCF-CMP-008 to place every node in its rack, power, cooling and fabric domains, and compute concentration.
4. **Assess health and integrity.** Review RAS classification and actions, health checks, scale-up domain validation and SDC screening. Reconstruct timelines for a sample of fatal events.
5. **Assess capacity.** Recompute usable capacity for a sampled day from raw scheduler and telemetry data.
6. **Assess change and recovery.** Review recent rollouts against staging, canary and halt criteria; review rollback and mass rebuild exercises.

### 11.2 Sampling

The population for CMP sampling is large and homogeneous, which makes statistical sampling feasible, but failures cluster by rack, lot and firmware version. Samples should therefore be stratified by node type, firmware version, rack and production lot, and should include the nodes with the most recent RMA or rebuild.

### 11.3 Interpreting results

- Installed capacity presented as usable capacity is a Finding against MCF-CMP-009; the control cannot be CONFORMING until the exclusions are applied.
- An absence of SDC screening is a US4 UNKNOWN for integrity outcomes, not merely a missing best practice, because SDC is otherwise undetectable.
- A canary cohort confined to one rack or one fault domain does not meet MCF-CMP-015 even if the rollout succeeded.
- Thermal throttling found in telemetry shall be passed to the THM assessment as challenging evidence (AIDCF-018-THM DG-THM-REQ-005).

**DG-CMP-REQ-005** The assessor shall reconstruct the detection-to-drain timeline for a sample of fatal accelerator or node error events and compare it with the declared drain time before concluding MCF-CMP-019 is CONFORMING.

**DG-CMP-REQ-006** Where nodes are found running firmware or software outside the approved baseline without an approved exception, the assessor shall record a Finding against MCF-CMP-013 or MCF-CMP-014 and shall treat performance and integrity evidence from those nodes as qualified.

## 12 Testing safety

Compute tests are rarely hazardous to people, but they are capability-affecting and can damage hardware or data if performed carelessly.

- Bandwidth tests, health diagnostics, burn-in and fault injection shall run only on drained nodes or domains with the AI platform operator's change authority and job-owner notification (DG-CMP-REQ-007).
- Fault injection (for example forcing an error to verify drain automation) shall use vendor-supported mechanisms on test nodes; it shall never be applied to nodes running production jobs.
- Firmware and rollback tests shall be performed in staging. Components with anti-rollback protection shall be identified before any test, because a failed downgrade can render hardware unusable.
- Fault-domain drain tests (MCF-CMP-008) are performed by draining compute through the scheduler; they shall not induce facility power or cooling faults. Facility fault tests are governed by AIDCF-018-POW and AIDCF-018-THM.
- Assessor access to BMCs and fleet tools shall use read-only accounts authorised by the operator; assessors shall not change configuration.
- Accelerator power-limit changes for testing shall respect the facility's rack power and cooling envelope.

**DG-CMP-REQ-007** A CMP test that removes capacity from production, injects faults, or changes firmware shall not be performed or requested without the AI platform operator's change authority, notification of affected job owners and, for fault injection, use of non-production nodes.

**DG-CMP-REQ-008** Assessors shall use read-only, operator-authorised credentials for any direct device or tool access and shall not retain those credentials after the assessment.

## 13 UNKNOWN hot-spots

| Hot-spot | Typical type | Typical severity | Why |
|---|---|---|---|
| Firmware of components not reachable by fleet tooling (power shelves, switch trays, retimers) | U5 Coverage gap | US4 (CG-08) | Inventory tools cover accelerators and BMCs but not all firmware-bearing parts |
| Silent data corruption detection | U1 Missing | US4 (CG-08) | Screening not performed or coverage unknown |
| Provider-operated layers (C7) | U2 Inaccessible | US3–US4 | Firmware, topology and RAS data not disclosed by service interface |
| Node-to-facility fault-domain mapping | U10 Dependency | US4 (CG-09) | Compute teams lack facility data; facility teams lack node placement |
| Mass rebuild capability | U5 Coverage gap | US4 (CG-10) | Only single-node rebuild exercised |
| Throttling measurement | U1 Missing | US3 | Throttle reasons not collected; usable capacity overstated |
| Attestation of firmware identity | U8 Method uncertain | US3 | Version strings self-reported by firmware |
| Rollback feasibility under anti-rollback | U9 Interpretation unresolved | US3 | OEM documentation unclear on downgrade paths |

**DG-CMP-REQ-009** An UNKNOWN affecting a CRITICAL CMP control (MCF-CMP-006, -008, -009, -013, -015, -019 or -023) shall be recorded at severity US4 or higher with the gate consequence defined in AIDCF-010.

## 14 Interfaces with other domains

| Domain | Interface | What CMP needs | What CMP provides |
|---|---|---|---|
| THM | Liquid and air cooling at rack | TCS supply temperature, flow and quality within OEM limits; staged readmission after recovery | Rack heat and liquid-capture ratio; coolant requirements; throttle telemetry |
| POW | Rack power | Feed redundancy to power shelves; capping protocol; ride-through | Rack power envelope; load-step characteristics of synchronous jobs |
| NET | Scale-out and management fabrics | Fabric topology, health and fault domains; OOB network | Rail mapping; NIC firmware baseline; collective performance baselines |
| STO | Data, checkpoints, images | Checkpoint throughput and durability; restart reads; image repository | Checkpoint size and interval; job restart requirements; SDC linkage to affected checkpoints |
| SEC | BMC and cluster manager security | Identity, privilege and segmentation of BMCs and schedulers | BMC inventory; scheduler admin roles |
| SUP | Firmware supply, spares, provenance | Release provenance and signatures; spares and lead times; component traceability | Failure trends by lot; RMA performance |
| OPS | Change and incident management | Change process; incident and problem records | Rollout records; health and drain events |
| RES | Recovery | Cross-domain recovery sequencing | Rebuild time objectives; re-qualification procedure |
| CAP | Demand and outcomes | Required capacity and integrity outcomes | Usable capacity reporting |

## 15 Informative references

- DMTF Redfish (platform management API); DMTF SPDM (Security Protocol and Data Model).
- NIST SP 800-193 (platform firmware resiliency guidelines); NIST SP 800-147B (BIOS protection guidelines for servers).
- TCG TPM 2.0 Library Specification.
- NIST SP 800-128 (security-focused configuration management).
- NIST SP 800-88 (guidelines for media sanitisation); IEEE 2883 (standard for sanitizing storage).
- Open Compute Project hardware management and fault-management specifications; OCP server component resilience and silent data corruption materials.
- JEDEC memory standards (DDR and HBM families); PCI Express Base Specification (Advanced Error Reporting).
- MLCommons MLPerf Training and Inference benchmark rules.
- ISO/IEC 20000-1 (service management); ISO/IEC 19770 series (IT asset management); ISO/IEC 27001; ISO/IEC 20243 (Open Trusted Technology Provider Standard).
- IEC 62368-1 (ICT equipment safety).
- ISO 22301 (business continuity management systems); Uptime Institute Tier Standard: Topology.
- AIDCF-004, AIDCF-005, AIDCF-007A, AIDCF-008, AIDCF-009, AIDCF-010, AIDCF-013, AIDCF-014.

## 16 Control summary

| Control ID | Title | Type | AL | Claim type | Gate mappings |
|---|---|---|---|---|---|
| MCF-CMP-001 | Accelerator Architecture | DIRECTIVE | AL2 | DESIGN | CG-08 SUPPORTING; CG-01 SUPPORTING |
| MCF-CMP-002 | Node Configuration | PREVENTIVE | AL3 | IMPLEMENTATION | CG-08 SUPPORTING; CG-15 SUPPORTING |
| MCF-CMP-003 | Rack-Scale Composition | PREVENTIVE | AL3 | IMPLEMENTATION | CG-08 SUPPORTING; CG-06 SUPPORTING; CG-05 SUPPORTING |
| MCF-CMP-004 | Approved Baseline | PREVENTIVE | AL3 | IMPLEMENTATION | CG-02 SUPPORTING; CG-08 SUPPORTING; CG-14 SUPPORTING |
| MCF-CMP-005 | Cluster Topology | DIRECTIVE | AL2 | DESIGN | CG-08 SUPPORTING; CG-02 SUPPORTING |
| MCF-CMP-006 | Scale-Up Domain Integrity | DETECTIVE | AL5 | EFFECTIVENESS | CG-08 CRITICAL; CG-09 SUPPORTING |
| MCF-CMP-007 | Partitioning | PREVENTIVE | AL3 | IMPLEMENTATION | CG-09 SUPPORTING; CG-15 SUPPORTING |
| MCF-CMP-008 | Fault-Domain Design | PREVENTIVE | AL5 | RESILIENCE | CG-09 CRITICAL; CG-08 SUPPORTING; CG-03 SUPPORTING |
| MCF-CMP-009 | Usable Accelerator Capacity | DETECTIVE | AL4 | OPERATION | CG-08 CRITICAL; CG-01 SUPPORTING |
| MCF-CMP-010 | Scheduler Controls | PREVENTIVE | AL3 | IMPLEMENTATION | CG-08 SUPPORTING; CG-15 SUPPORTING |
| MCF-CMP-011 | Resource Reservation | PREVENTIVE | AL4 | OPERATION | CG-10 SUPPORTING; CG-08 SUPPORTING |
| MCF-CMP-012 | Contention Management | CORRECTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-CMP-013 | Firmware Baseline | PREVENTIVE | AL3 | IMPLEMENTATION | CG-08 CRITICAL; CG-14 SUPPORTING; CG-15 SUPPORTING |
| MCF-CMP-014 | Driver Compatibility | PREVENTIVE | AL3 | IMPLEMENTATION | CG-08 SUPPORTING |
| MCF-CMP-015 | Upgrade Testing | PREVENTIVE | AL5 | EFFECTIVENESS | CG-14 CRITICAL; CG-09 SUPPORTING; CG-08 SUPPORTING |
| MCF-CMP-016 | Rollback Readiness | RECOVERY | AL5 | RESILIENCE | CG-10 SUPPORTING; CG-14 SUPPORTING |
| MCF-CMP-017 | GPU Telemetry | DETECTIVE | AL4 | OPERATION | CG-08 SUPPORTING; CG-06 SUPPORTING |
| MCF-CMP-018 | Node Health | DETECTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-CMP-019 | Error and Degradation Detection | DETECTIVE | AL5 | EFFECTIVENESS | CG-08 CRITICAL |
| MCF-CMP-020 | Performance Baselines | DETECTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-CMP-021 | Provisioning | PREVENTIVE | AL3 | IMPLEMENTATION | CG-08 SUPPORTING; CG-14 SUPPORTING |
| MCF-CMP-022 | Spares and RMA | CORRECTIVE | AL4 | OPERATION | CG-10 SUPPORTING; CG-03 SUPPORTING |
| MCF-CMP-023 | Node Rebuild | RECOVERY | AL5 | RESILIENCE | CG-10 CRITICAL; CG-08 SUPPORTING |
| MCF-CMP-024 | Secure Retirement | PREVENTIVE | AL3 | IMPLEMENTATION | CG-02 SUPPORTING |

## 17 Worked synthetic example

**Synthetic example. All names, figures and results below are invented for illustration and do not describe any real cluster, vendor or assessment.**

**Context.** Capability Instance CI-SYN-CMP-01 is a training cluster of 512 nodes with eight accelerators each (4,096 accelerators), pattern C1, in four rows of 16 racks with eight nodes per rack. The Service Outcome requires 92 % of installed accelerators to be usable for training (profile parameter for MCF-CMP-009) and model integrity to be preserved. The profile adopts a 2 % canary cohort, 72 h soak and a 25 % maximum capacity fraction per facility fault domain.

**Usable capacity (MCF-CMP-009).** For the sampled day the operator reports 4,096 usable accelerators. The assessor recomputes from scheduler state and telemetry: 61 accelerators on drained nodes, 23 quarantined, 40 awaiting RMA, 128 in the recovery reservation and 37 throttled below the 95 % performance threshold. Usable capacity is 4,096 − 289 = 3,807, or 92.9 %. The requirement is met, but the operator's daily report did not apply the exclusions defined in the control. The result is **PARTIAL** (definition not implemented in the report) with a Finding; because MCF-CMP-009 is CRITICAL for CG-08, CG-08 will be FAIL until the reporting is corrected and re-evidenced.

**Throttling.** The 37 throttled accelerators sit in two racks served by one CDU group. Throttle-reason telemetry shows thermal limits. The assessor passes this to the THM assessment as challenging evidence against MCF-THM-010 and MCF-THM-011 for that group.

**Firmware and change (MCF-CMP-013, -015).** Fleet inventory covers accelerators, NICs, BIOS and BMCs; it does not cover power-shelf firmware. MCF-CMP-013 is **UNKNOWN** (U5, US4) for that component class. The last NIC firmware rollout used a canary of eight nodes (1.6 % of the fleet), all in one rack. The rollout succeeded, but the canary did not span fault domains or node lots. MCF-CMP-015 is **PARTIAL**; CG-14 is FAIL on this input.

**Integrity (MCF-CMP-019).** Fatal error events trigger automatic drain; reconstructed timelines for ten sampled events show drains within 2–4 minutes against a 5-minute objective. SDC screening runs monthly but on only 60 % of nodes, because nodes in long-running jobs are skipped. MCF-CMP-019 is **PARTIAL**. The assessor also notes that two nodes later found to fail SDC screening had participated in a job whose checkpoints were not reviewed: an integrity UNKNOWN (U9, US4) is recorded against the affected model artefacts and passed to STO (MCF-STO-009).

**Fault domains (MCF-CMP-008).** Rows A and B share one power feed group, which carries 50 % of the cluster. This exceeds the 25 % profile limit; MCF-CMP-008 is **NONCONFORMING** and CG-09 is FAIL on this input.

**Recovery (MCF-CMP-023).** Single-node rebuilds average 70 minutes. A mass rebuild of 128 nodes was exercised six months ago and completed in 9 hours against a 12-hour objective, with the image repository located in a different hall from the cluster. MCF-CMP-023 is **CONFORMING**.

**Gate Results (CMP inputs only).** CG-08 FAIL (MCF-CMP-009 and MCF-CMP-019 PARTIAL); CG-09 FAIL (MCF-CMP-008 NONCONFORMING); CG-14 FAIL (MCF-CMP-015 PARTIAL); CG-10 not defeated by CMP inputs. Final Gate Results depend on the controls of other domains mapped to the same gates.

**Actions.** Apply the usable-capacity definition in daily reporting; extend firmware inventory to power shelves; redefine canary cohorts to span rows, power groups and lots; schedule SDC screening between job segments to reach full coverage, and screen checkpoints of jobs that ran on failed nodes; rebalance placement or the electrical design so that no feed group carries more than 25 % of the cluster. Each action carries a reassessment trigger on the affected controls.
