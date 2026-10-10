# AIDCF-018-STO AI Storage and Data Infrastructure Domain Guide

## Document control

| Element | Value |
|---|---|
| Document ID | AIDCF-018-STO |
| Title | AI Storage and Data Infrastructure Domain Guide |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Domain | STO (AI Storage and Data Infrastructure) |
| Controls covered | MCF-STO-001 to MCF-STO-024 (families STO-01 to STO-06) |
| Normative basis | AIDCF-007A (control registry), AIDCF-008 (evidence model), AIDCF-010 (scoring and gates) |
| Related documents | AIDCF-003, AIDCF-004, AIDCF-009, AIDCF-013, AIDCF-014, AIDCF-018-CMP, AIDCF-018-NET, AIDCF-018-RES |

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-10 | Initial issue: domain guidance aligned to the rewritten STO control records; MCF-STO-019 titled "Storage Recovery Sequencing". |

Requirements in this guide are identified DG-STO-REQ-NNN. The control records in AIDCF-007A remain the normative statement of each control; where this guide restates a control, the registry record prevails.

## 1 Purpose and scope

This guide explains how to apply the 24 STO controls when assessing whether the storage and data infrastructure supporting a Capability Instance delivers the throughput, integrity, protection and recoverability its Service Outcomes require.

In scope:

- **Tiers**: training and fine-tuning data; checkpoints (model weights, optimiser state, data-loader and random-number state); model and release artefacts (weights, adapters, tokenisers, configurations); archive.
- **Systems**: POSIX parallel file systems, scale-out NAS, object stores (on premises or cloud), node-local NVMe and burst-buffer tiers, and the data movers between them.
- **Properties**: throughput, IOPS and metadata performance; capacity and headroom; burst absorption; end-to-end integrity, scrubbing and configuration consistency; snapshots, replication, erasure coding and immutable recovery copies; checkpoint durability, restart and recovery; telemetry, forecasting, media health and sanitisation; data location and sovereignty.

Out of scope: the storage network fabric (NET-03), storage controller security as a control-plane matter (SEC-02), and data governance questions about the content of datasets (lawfulness, quality, bias), which belong to AI governance and are handed off through AIDCF-005. Data sovereignty is in scope to the extent that the infrastructure determines where data and its copies physically reside.

## 2 Why this domain matters for AI capability

**Storage is on the critical path of training.** Data loaders must keep every accelerator fed, and checkpoints must be written frequently enough that a failure loses only an acceptable amount of work. When storage is slow, accelerators wait; when it is unavailable, training stops; when checkpoints are lost or corrupt, days of compute may have to be repeated.

**Checkpoint economics.** Large models produce checkpoints of many terabytes, written by thousands of processes at once. The checkpoint interval trades lost work on failure against time spent checkpointing. A widely used first-order model (Young, later refined by Daly) puts the optimum interval near the square root of twice the checkpoint cost times the mean time between interruptions. Two consequences follow for assurance: the required write bandwidth is set by checkpoint size divided by the acceptable write window, and the acceptable interval depends on the job-level interruption rate observed in CMP. Both must be derived and evidenced (MCF-STO-002, -005).

**Burst behaviour.** Checkpoints arrive as synchronised bursts, and restarts after an outage arrive as read storms from every node at once. Average utilisation says little about whether storage survives these events (MCF-STO-008).

**Metadata as a single point of collapse.** Many-small-file datasets and per-rank checkpoint files can saturate metadata services; metadata loss can render intact data unreachable for an entire tier (MCF-STO-006, -010).

**Integrity and provenance.** Checkpoints and models are the product of the capability. A silently corrupted checkpoint resumed into training, or a tampered model artefact deployed, defeats the integrity outcome even when every system is "available". End-to-end checksums, verification before resume and provenance links from model to training run and dataset version are infrastructure safeguards for integrity (MCF-STO-003, -009, -017).

**Destructive threats.** Ransomware, compromised administrator accounts and operator error can destroy primary data and every copy administered from the same domain. An immutable copy in a separate administrative domain is the safeguard of last resort (MCF-STO-016).

**Location.** Training data, checkpoints and models may be subject to residency or sovereignty constraints. Caches, replicas and backups are the copies most often overlooked (MCF-STO-001, -014).

## 3 Reference patterns and variants

| Pattern | Description | Characteristic assurance concerns |
|---|---|---|
| S1 Parallel file system for data and checkpoints | POSIX parallel file system with separate metadata and data servers over a high-speed storage fabric | Metadata scaling; throughput in degraded and rebuild states; client mount consistency |
| S2 Object store with cache | Datasets in an object store; node-local or shared cache for training reads | Cache coherency and location; request-rate limits; listing performance |
| S3 Tiered checkpointing | Checkpoint written first to node-local NVMe or a burst tier, then drained asynchronously to durable storage | Durability point definition; loss of local copies on node failure; drain bandwidth |
| S4 Cloud-hosted storage | Datasets and checkpoints in a provider's object or file service | Evidence through service interface; region and replication location; egress dependency |
| S5 Model registry | Versioned artefact store for models and releases | Immutability of versions; hash verification at deployment; provenance |
| S6 Multi-site protection | Replication to a second hall, site or region; immutable copy in a separate account or domain | Fault-domain and administrative independence; RPO; jurisdiction of replica |
| S7 Archive | Cold object storage or tape for long-term retention | Fixity checks; retrieval time; media and format migration |

## 4 Required functions and capability linkage

| Required Function | Description | Principal controls |
|---|---|---|
| RF-STO-1 Serve data | Deliver training data at the rate the data loaders require | MCF-STO-001, -005, -006 |
| RF-STO-2 Persist checkpoints | Write complete, consistent, durable checkpoints within the window | MCF-STO-002, -005, -008, -017 |
| RF-STO-3 Maintain metadata | Provide namespace and layout services at scale, consistently | MCF-STO-006, -010 |
| RF-STO-4 Preserve integrity | Detect and prevent corruption of data, checkpoints, artefacts and configuration | MCF-STO-003, -009, -011, -012 |
| RF-STO-5 Protect and replicate | Provide independent copies to recover from loss, corruption and destruction | MCF-STO-013, -014, -015, -016 |
| RF-STO-6 Restore and restart | Restore data and resume training within tolerance | MCF-STO-018, -019, -020 |
| RF-STO-7 Sustain capacity | Keep capacity and media health ahead of demand | MCF-STO-007, -021, -022, -023 |
| RF-STO-8 Retain and dispose | Archive what must be kept; sanitise what leaves service | MCF-STO-004, -024 |

Linkage to Service Outcomes runs principally through training throughput (data loading and checkpoint stall), recovery tolerance (lost work and restart time) and integrity (model and checkpoint correctness).

## 5 Dependencies, fault domains, common-mode concerns

### 5.1 Dependencies

Storage depends on: facility power and cooling for storage servers and enclosures (POW, THM); the storage fabric and front-end network (NET-03); time synchronisation and DNS (NET-06); identity and key management for access and encryption at rest (SEC-01); the storage software and firmware supply (SUP-04); media supply and RMA (SUP-05); and, for cloud patterns, the provider's region and service availability (DEP-03).

### 5.2 Fault domains

Storage fault domains nest from media → enclosure or server → rack → storage cluster → hall → site → region, plus an administrative fault domain (the set of credentials and control planes that can modify or delete data). Erasure coding and replication protect against physical domains only if stripes and replicas are placed across them (MCF-STO-015, -014). Snapshots protect against logical error but share the physical and administrative domain of the system (MCF-STO-013). Only an immutable copy in a separate administrative domain protects against destructive privileged action (MCF-STO-016).

The checkpoint tier must not share every fault domain with the compute it protects (MCF-STO-002): if a power or cooling event that halts the cluster can also destroy or make unavailable the latest checkpoints, the recovery tolerance cannot be met.

### 5.3 Common-mode concerns

- Erasure-coding stripes whose members sit in the same rack or on the same power feed group.
- Replication that faithfully copies corruption or deletion to the target (replication is not backup).
- Snapshots, replicas and backups all administered through one identity provider or one storage administrator role.
- Key management hosted on the storage it unlocks, creating a recovery circular dependency.
- DNS, time or identity services hosted on the storage cluster.
- A single storage software release deployed to primary and replica simultaneously.
- A batch of media from one production lot across all enclosures.

## 6 Threats, hazards and failure scenarios with propagation paths to Service Outcomes

| ID | Scenario (AIDCF-004 reference) | Propagation path | Outcome effect | Principal safeguards |
|---|---|---|---|---|
| STO-S1 | Storage metadata failure during training (X07) | Metadata server fails or metadata saturates → file opens stall → all ranks block on I/O → job hangs or times out | Training halted; possible corruption if failover is unclean | MCF-STO-006, -010; MCF-STO-019 |
| STO-S2 | Fabric congestion during checkpoint demand (X06) | Synchronous checkpoint burst → storage fabric and servers saturate → checkpoint exceeds window → step stall; other tenants degraded | Throughput loss; risk of incomplete checkpoint | MCF-STO-005, -008; NET-02, NET-03 |
| STO-S3 | Checkpoint failure | Async checkpoint marked complete before flush → node or power loss → latest checkpoint incomplete → resume from older checkpoint or from scratch | Lost work beyond tolerance | MCF-STO-017; MCF-STO-002 durability definition |
| STO-S4 | Silent corruption | Bit error or software defect corrupts checkpoint shard → not detected at write → resumed into training | Integrity outcome defeated | MCF-STO-009, -011; MCF-CMP-019 |
| STO-S5 | Capacity exhaustion | Retention growth and new datasets fill tier above threshold → performance degrades → checkpoint writes fail | Training halted | MCF-STO-007, -022 |
| STO-S6 | Throughput collapse during rebuild | Enclosure fails → erasure-coding rebuild consumes bandwidth → checkpoint throughput falls below requirement | Degraded throughput for rebuild duration | MCF-STO-005 degraded-state tests; MCF-STO-015 |
| STO-S7 | Protection common-mode / ransomware | Compromised admin account deletes snapshots and replicas, encrypts primary | Loss of all data administered from that domain | MCF-STO-016; SEC-01 |
| STO-S8 | Restore failure | Backups exist but restore fails (format change, missing keys, incompatible framework) | Recovery objective missed | MCF-STO-020; MCF-STO-019 |
| STO-S9 | Recovery reintroduces corrupt configuration (X15) | Storage configuration restored from stale or corrupt baseline → protection policies disabled | Latent exposure after recovery | MCF-STO-012 |
| STO-S10 | Restart read storm | Facility event → all jobs restart together → checkpoint reads saturate storage → restarts time out repeatedly | Prolonged recovery | MCF-STO-008, -018; MCF-THM-024 staged readmission |
| STO-S11 | Data placed outside permitted jurisdiction | Cache or replica configured in another region | Sovereignty obligation breached | MCF-STO-001, -014 |

## 7 Safeguards

- **Prevent**: tier design with derived requirements (MCF-STO-001, -002, -003, -004); throughput and burst capability (MCF-STO-005, -008); headroom and quotas (MCF-STO-007); configuration baseline (MCF-STO-012); erasure-coding placement (MCF-STO-015); checkpoint completion semantics (MCF-STO-017); capacity forecasting (MCF-STO-022); sanitisation (MCF-STO-024).
- **Detect**: end-to-end checksums and verification before resume (MCF-STO-009); scrubbing (MCF-STO-011); telemetry (MCF-STO-021); metadata monitoring (MCF-STO-006); media health (MCF-STO-023).
- **Contain**: fault-domain placement of stripes and replicas (MCF-STO-014, -015); quotas and QoS (MCF-STO-007, -008); administrative separation of the immutable copy (MCF-STO-016).
- **Correct**: repair from redundancy (MCF-STO-011, -015); snapshot restore (MCF-STO-013).
- **Recover**: replication and immutable copies (MCF-STO-014, -016); restart readiness (MCF-STO-018); recovery sequencing (MCF-STO-019); restore validation (MCF-STO-020).

## 8 Critical-gate linkage

| Gate | CRITICAL controls | SUPPORTING controls |
|---|---|---|
| CG-01 | — | MCF-STO-001 |
| CG-03 | — | MCF-STO-014 |
| CG-08 | MCF-STO-005, MCF-STO-009, MCF-STO-010, MCF-STO-017 | MCF-STO-001, MCF-STO-002, MCF-STO-003, MCF-STO-006, MCF-STO-007, MCF-STO-008, MCF-STO-011, MCF-STO-012, MCF-STO-015, MCF-STO-021, MCF-STO-022, MCF-STO-023 |
| CG-09 | MCF-STO-015 | MCF-STO-008, MCF-STO-014, MCF-STO-019 |
| CG-10 | MCF-STO-016, MCF-STO-018, MCF-STO-020 | MCF-STO-002, MCF-STO-003, MCF-STO-004, MCF-STO-010, MCF-STO-013, MCF-STO-014, MCF-STO-017, MCF-STO-019 |
| CG-14 | — | MCF-STO-012 |
| CG-15 | — | MCF-STO-016 |

Notes on the mapping:

- **CG-08 Compute, storage and network functional integrity** receives four CRITICAL STO controls: throughput and IOPS including degraded states (MCF-STO-005), end-to-end data integrity (-009), metadata integrity (-010) and checkpoint durability (-017).
- **CG-10 Recovery readiness** receives three CRITICAL STO controls: immutable recovery copy (MCF-STO-016), restart readiness (-018) and recovery validation (-020). Snapshot, replication, artefact and archive controls are SUPPORTING. MCF-STO-019 Storage Recovery Sequencing is SUPPORTING because its adequacy can only be judged jointly with the cross-domain recovery sequence (RES-04); a storage sequence that is internally sound but misaligned with facility and compute recovery is evaluated at gate level.
- **CG-09 Failure containment** receives MCF-STO-015 as CRITICAL: stripes that do not span independent domains turn a single rack or feed failure into data loss.
- **CG-15 Integrated digital authority** receives MCF-STO-016 as SUPPORTING because administrative separation of the immutable copy bounds privileged reach.
- **MCF-STO-024 Secure Sanitisation** maps to no gate. Its failure exposes data confidentiality and sovereignty obligations, which are reported as Findings and decision conditions but do not fall within any critical gate's scope.

The CG-10 evidence floor is S5 (E1+E2+E3+E4); CRITICAL CG-10 controls therefore carry CP-5 and S5. The CG-08 floor is S4 (E2+E3+E4).

## 9 Capability-profile parameters

Values are **illustrative defaults**; each capability profile shall set its own values with the stated basis (DG-STO-REQ-001).

| Parameter | Unit | Illustrative default | Basis | Used by |
|---|---|---|---|---|
| Data-loader read throughput per accelerator | GB/s | workload-specific (illustrative 1) | Workload characterisation | MCF-STO-001 |
| Permitted data jurisdictions | list | capability-specific | Data owner; applicable law and contracts | MCF-STO-001 |
| Checkpoint size (large training job) | TB | job-specific (illustrative 10) | Model architecture and optimiser state | MCF-STO-002 |
| Checkpoint write window | s | 120 (illustrative) | Capability profile; acceptable step stall | MCF-STO-002 |
| Checkpoint interval | min | derived (illustrative 30) | Young/Daly model using measured interruption rate | MCF-STO-002 |
| Retained good checkpoints | count | 3 (illustrative) | Capability profile | MCF-STO-002 |
| Archive copies | count | 2 (illustrative) | Capability profile | MCF-STO-004 |
| Retrieval time objective | h | 48 (illustrative) | Capability profile | MCF-STO-004 |
| Required aggregate checkpoint write throughput | GB/s | derived: checkpoint size ÷ window (illustrative 100) | MCF-STO-002 derivation | MCF-STO-005 |
| Degraded-state minimum | % of required throughput | 70 (illustrative) | Capability profile | MCF-STO-005 |
| Required aggregate read throughput | GB/s | derived from MCF-STO-001 | Workload characterisation | MCF-STO-005 |
| Metadata operation p99 latency | ms | 10 (illustrative) | Capability profile | MCF-STO-006 |
| Required metadata operations | ops/s | workload-specific | Workload characterisation | MCF-STO-006 |
| Critical utilisation threshold | % of usable capacity | 80 (illustrative) | Storage vendor guidance; capability profile | MCF-STO-007 |
| Warning threshold | % of usable capacity | 70 (illustrative) | Capability profile | MCF-STO-007 |
| Concurrent checkpointing jobs | count | 3 (illustrative) | Workload characterisation | MCF-STO-008 |
| Restart read-storm completion time | min | 15 (illustrative) | Capability profile | MCF-STO-008 |
| Checksum coverage of checkpoints and artefacts | % | 100 (illustrative) | Capability profile | MCF-STO-009 |
| Metadata failover time | s | 60 (illustrative) | Capability profile; vendor data | MCF-STO-010 |
| Consistency check interval | days | 30 (illustrative) | Vendor guidance | MCF-STO-010 |
| Scrub cycle | days | 30 (illustrative) | Vendor guidance; capability profile | MCF-STO-011 |
| Snapshot recovery point objective | h | 4 (illustrative) | Capability profile | MCF-STO-013 |
| Snapshot retention | days | 14 (illustrative) | Capability profile | MCF-STO-013 |
| Replication RPO (checkpoints) | min | 60 (illustrative) | Capability profile | MCF-STO-014 |
| Replication RPO (datasets and artefacts) | h | 24 (illustrative) | Capability profile | MCF-STO-014 |
| Protection scheme | k+m | 8+2 (illustrative) | Capability profile; vendor options | MCF-STO-015 |
| Concurrent failure-domain tolerance | count | 2 (illustrative) | Capability profile | MCF-STO-015 |
| Rebuild time objective | h | 24 (illustrative) | Capability profile; vendor data | MCF-STO-015 |
| Immutable retention | days | 30 (illustrative) | Capability profile | MCF-STO-016 |
| Restore time from immutable copy | h | 24 (illustrative) | Capability profile | MCF-STO-016 |
| Retained good checkpoints | count | 3 (illustrative) | Capability profile | MCF-STO-017 |
| Restart time objective | min | 30 (illustrative) | Capability profile | MCF-STO-018 |
| Lost work tolerance | min of training | 60 (illustrative) | Capability profile; checkpoint interval | MCF-STO-018 |
| Storage recovery time objective | h | 4 (illustrative) | Capability profile | MCF-STO-019 |
| Restore test interval | months | 3 (illustrative) | Capability profile | MCF-STO-020 |
| Telemetry interval | s | 30 (illustrative) | Capability profile | MCF-STO-021 |
| Forecast horizon | months | 9 (illustrative) | Procurement lead time | MCF-STO-022 |
| NVMe wear replacement threshold | % of rated endurance used | 90 (illustrative) | Vendor endurance rating | MCF-STO-023 |
| AFR investigation threshold | % | 2× fleet baseline (illustrative) | Capability profile | MCF-STO-023 |

**DG-STO-REQ-001** A capability profile that adopts STO controls shall state a value and basis for each applicable parameter above, or record it as not applicable with rationale.

**DG-STO-REQ-002** Required checkpoint write throughput and checkpoint interval shall be derived in the profile from checkpoint size, write window and measured job interruption rate, and the derivation shall be retained as E7 evidence.

## 10 Evidence expectations by claim type

| Claim type | Required AL | Controls | Typical profile tier and sufficiency floor |
|---|---|---|---|
| DESIGN | AL2 | MCF-STO-001, MCF-STO-002 | CP-1/S3 |
| IMPLEMENTATION | AL3 | MCF-STO-003, MCF-STO-004, MCF-STO-012, MCF-STO-024 | CP-2/S3 |
| OPERATION | AL4 | MCF-STO-006, MCF-STO-007, MCF-STO-011, MCF-STO-013, MCF-STO-021, MCF-STO-022, MCF-STO-023 | CP-3/S4 |
| EFFECTIVENESS | AL5 | MCF-STO-005, MCF-STO-008, MCF-STO-009, MCF-STO-010, MCF-STO-017 | CP-4/S4, CP-5/S4 |
| RESILIENCE | AL5 | MCF-STO-014, MCF-STO-015, MCF-STO-016, MCF-STO-018, MCF-STO-019, MCF-STO-020 | CP-5/S5 |

- **DESIGN (AL2)**: tier designs with derived requirements, location registers, checkpoint size and interval derivations. A design claim cannot show that the throughput exists.
- **IMPLEMENTATION (AL3)**: configuration exports from storage systems and clients (protection schemes, quotas, mount options, retention locks) reconciled to the baseline, plus artefact and fixity records.
- **OPERATION (AL4)**: telemetry over at least 90 days including checkpoint timings, capacity, metadata latency, snapshot success and media health. Completeness and time alignment with compute telemetry should be shown.
- **EFFECTIVENESS (AL5)**: benchmarks at declared concurrency including degraded and rebuild states; corruption injection on test copies; metadata failover; interrupted-write tests.
- **RESILIENCE (AL5)**: replica and immutable-copy restores, restart exercises after storage or facility events, recovery sequencing exercises, and restore validation that ends with training actually resuming from the restored checkpoint.

Typical weaknesses are vendor benchmark sheets presented as site evidence, benchmarks run with far fewer clients than production, restore "tests" that confirm a backup job succeeded rather than restoring and verifying data, and replication dashboards that show configuration but not lag history.

**DG-STO-REQ-003** A restore test shall count as E4 evidence for MCF-STO-020 only if data was restored to a usable location, verified by checksum against source records and, for checkpoints, used to resume training; a successful backup job alone is E3 evidence.

**DG-STO-REQ-004** Benchmark evidence for MCF-STO-005 shall state client count, access pattern, file or object sizes and network path; where the client count is below production concurrency, the assessor shall record the result as qualified and shall not accept it as CONFORMING without an independently reviewed extrapolation.

## 11 Assessment guidance

### 11.1 Sequencing

1. **Derive the requirements.** Start with MCF-STO-001 and -002: required read throughput, checkpoint size, window, interval and retention. Obtain the job interruption rate from CMP.
2. **Establish the as-built state.** Reconcile configuration (MCF-STO-012), protection schemes and placement (MCF-STO-015) and the location register (MCF-STO-001).
3. **Test performance claims.** Compare benchmark and production evidence with the derived requirements, in normal and degraded states (MCF-STO-005, -006, -008).
4. **Test integrity.** Recompute checksums on sampled checkpoints and artefacts; review verification before resume; review scrub completion (MCF-STO-009, -011, -017).
5. **Follow the recovery chain.** From each protection mechanism to restore to resumed training (MCF-STO-013, -014, -016, -018, -019, -020). Confirm administrative separation of the immutable copy.
6. **Check lifecycle.** Capacity forecast, media health and sanitisation.

### 11.2 Sampling

Sample by data class (dataset, checkpoint, artefact, configuration) and protection mechanism, so that each combination required by the profile is represented. For checkpoints, include the largest production job and at least one job restarted after a failure. For integrity, sample shards from different storage servers and enclosures.

### 11.3 Interpreting results

- Throughput that meets requirements only in NORMAL state leaves MCF-STO-005 short of CONFORMING; the degraded-state minimum is part of the control.
- A replica with lag inside RPO but in the same administrative domain as primary supports MCF-STO-014 but does not satisfy MCF-STO-016.
- Retention locks in a mode that administrators can shorten do not provide immutability for MCF-STO-016.
- An SDC event in CMP that touched a job whose checkpoints were not re-verified is an integrity UNKNOWN against the affected artefacts (link MCF-CMP-019 → MCF-STO-009).

**DG-STO-REQ-005** The assessor shall verify that the immutable recovery copy cannot be deleted or have its retention shortened using any credential that can administer the primary storage, and shall record the result against MCF-STO-016.

**DG-STO-REQ-006** Where data, cache, replica or backup locations cannot be established for a data class with declared residency constraints, the assessor shall record a U10 UNKNOWN and report the residency status of that data class as unverified.

## 12 Testing safety

Storage tests rarely endanger people, but they can destroy the very data whose protection is being assessed.

- No test shall delete, overwrite, encrypt or roll back production data, snapshots, replicas or recovery copies without the data owner's written authorisation (DG-STO-REQ-007).
- Restores shall target isolated namespaces or accounts; replica failover tests shall not reverse replication over good data.
- Corruption injection (MCF-STO-009) shall be performed only on test copies in isolated namespaces.
- Degraded-state benchmarks (MCF-STO-005) and rebuild tests (MCF-STO-015) shall remove components in a controlled way approved by the storage engineering authority, during agreed windows, with protection margin sufficient to tolerate a further unplanned failure.
- Full-concurrency benchmarks compete with production and shall be scheduled with the AI platform operator.
- Deletion-refusal tests on immutable copies (MCF-STO-016) shall use a dedicated test object and test account.

**DG-STO-REQ-007** No STO test shall delete, overwrite, encrypt or roll back production data or any copy relied on for recovery unless the data owner has authorised it in writing and an independent verified copy exists.

**DG-STO-REQ-008** A test that removes storage components from service shall not proceed unless the remaining protection tolerates at least one further failure of the same component class during the test.

## 13 UNKNOWN hot-spots

| Hot-spot | Typical type | Typical severity | Why |
|---|---|---|---|
| Throughput in degraded and rebuild states | U5 Coverage gap | US4 (CG-08) | Only normal-state benchmarks exist |
| Checkpoint recovery after correlated metadata or fabric disruption (AIDCF-008 §50 example) | U5 Coverage gap | US4 (CG-10) | Restart tested only after single-node failures |
| Durability point of asynchronous checkpoints | U8 Method uncertain | US4 (CG-08) | Framework semantics undocumented |
| Administrative independence of the immutable copy | U10 Dependency | US4 (CG-10) | Shared identity provider not recognised as common mode |
| Key-management availability during recovery | U10 Dependency | US3–US4 | Keys hosted on dependent infrastructure |
| Cache and replica locations in cloud patterns | U2 Inaccessible | US3 | Provider configuration not exposed |
| Erasure-coding placement versus physical topology | U4 Conflicting | US4 (CG-09) | Storage software view differs from rack and power records |
| Integrity of checkpoints from jobs on later-failed hardware | U9 Interpretation unresolved | US4 (CG-08) | No linkage from CMP RAS events to STO artefacts |

**DG-STO-REQ-009** An UNKNOWN affecting a CRITICAL STO control (MCF-STO-005, -009, -010, -015, -016, -017, -018 or -020) shall be recorded at severity US4 or higher with the gate consequence defined in AIDCF-010.

## 14 Interfaces with other domains

| Domain | Interface | What STO needs | What STO provides |
|---|---|---|---|
| CMP | Checkpoints, restart, images | Checkpoint size, interval, job interruption rate; SDC events linked to jobs | Checkpoint throughput and durability; restart reads; image repository availability |
| NET | Storage fabric | Bandwidth and congestion behaviour under checkpoint bursts | Traffic profile of bursts and restart storms |
| THM / POW | Facility | Power and cooling of storage; fault-domain information | Storage heat and power; placement needs relative to compute fault domains |
| SEC | Control plane and identity | Privileged access control for storage administration; key management | Administrative domain design; deletion-refusal evidence |
| RES | Recovery | Cross-domain recovery sequence (RES-04) and data and checkpoint recovery (MCF-RES-016) | Storage recovery sequence; restore evidence |
| DEP | External and cloud | Provider region, service and replication dependencies | Location register |
| PHY / ENV | Custody and waste | Media custody; hardware and media waste handling | Sanitisation certificates |
| SUP | Media and software supply | Release provenance; media lead times | Failure trends by lot |
| CAP | Outcomes and demand | Lost-work and restart tolerances; growth forecast | Capacity forecast |

## 15 Informative references

- ISO/IEC 27040 (storage security); NIST SP 800-209 (security guidelines for storage infrastructure).
- NIST SP 800-88 (guidelines for media sanitisation); IEEE 2883 (standard for sanitizing storage).
- ISO 22301 (business continuity management systems); ISO/IEC 27031 (ICT readiness for business continuity); NIST SP 800-34 (contingency planning guide for information systems).
- ISO/IEC 27001 (information security management systems).
- T10 Protection Information (SCSI) and NVMe end-to-end data protection; NVMe Base Specification (SMART / health information log).
- IO500 benchmark methodology (HPC storage performance).
- Young/Daly optimum checkpoint interval model (published literature).
- ISO 14721 (OAIS reference model for archives).
- Regulation (EU) 2016/679 (GDPR) and applicable national data-residency law.
- AIDCF-004, AIDCF-005, AIDCF-007A, AIDCF-008, AIDCF-009, AIDCF-010, AIDCF-013, AIDCF-014.

## 16 Control summary

| Control ID | Title | Type | AL | Claim type | Gate mappings |
|---|---|---|---|---|---|
| MCF-STO-001 | Training Data Tier | DIRECTIVE | AL2 | DESIGN | CG-08 SUPPORTING; CG-01 SUPPORTING |
| MCF-STO-002 | Checkpoint Tier | DIRECTIVE | AL2 | DESIGN | CG-08 SUPPORTING; CG-10 SUPPORTING |
| MCF-STO-003 | Model and Artifact Tier | PREVENTIVE | AL3 | IMPLEMENTATION | CG-08 SUPPORTING; CG-10 SUPPORTING |
| MCF-STO-004 | Archive Tier | PREVENTIVE | AL3 | IMPLEMENTATION | CG-10 SUPPORTING |
| MCF-STO-005 | Throughput and IOPS | PREVENTIVE | AL5 | EFFECTIVENESS | CG-08 CRITICAL |
| MCF-STO-006 | Metadata Performance | DETECTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-STO-007 | Capacity Headroom | PREVENTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-STO-008 | Burst Handling | PREVENTIVE | AL5 | EFFECTIVENESS | CG-08 SUPPORTING; CG-09 SUPPORTING |
| MCF-STO-009 | Data Integrity | DETECTIVE | AL5 | EFFECTIVENESS | CG-08 CRITICAL |
| MCF-STO-010 | Metadata Integrity | PREVENTIVE | AL5 | EFFECTIVENESS | CG-08 CRITICAL; CG-10 SUPPORTING |
| MCF-STO-011 | Checksum and Scrubbing | DETECTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-STO-012 | Configuration Consistency | PREVENTIVE | AL3 | IMPLEMENTATION | CG-14 SUPPORTING; CG-08 SUPPORTING |
| MCF-STO-013 | Snapshot Protection | PREVENTIVE | AL4 | OPERATION | CG-10 SUPPORTING |
| MCF-STO-014 | Replication | RECOVERY | AL5 | RESILIENCE | CG-10 SUPPORTING; CG-09 SUPPORTING; CG-03 SUPPORTING |
| MCF-STO-015 | Erasure Coding | PREVENTIVE | AL5 | RESILIENCE | CG-09 CRITICAL; CG-08 SUPPORTING |
| MCF-STO-016 | Immutable Recovery Copy | RECOVERY | AL5 | RESILIENCE | CG-10 CRITICAL; CG-15 SUPPORTING |
| MCF-STO-017 | Checkpoint Durability | PREVENTIVE | AL5 | EFFECTIVENESS | CG-08 CRITICAL; CG-10 SUPPORTING |
| MCF-STO-018 | Restart Readiness | RECOVERY | AL5 | RESILIENCE | CG-10 CRITICAL |
| MCF-STO-019 | Storage Recovery Sequencing | RECOVERY | AL5 | RESILIENCE | CG-10 SUPPORTING; CG-09 SUPPORTING |
| MCF-STO-020 | Recovery Validation | CORRECTIVE | AL5 | RESILIENCE | CG-10 CRITICAL |
| MCF-STO-021 | Storage Telemetry | DETECTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-STO-022 | Capacity Forecasting | PREVENTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-STO-023 | Media Health | DETECTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-STO-024 | Secure Sanitisation | PREVENTIVE | AL3 | IMPLEMENTATION | None |

## 17 Worked synthetic example

**Synthetic example. All names, figures and results below are invented for illustration and do not describe any real storage system, provider or assessment.**

**Context.** Capability Instance CI-SYN-STO-01 trains a large model on a 4,096-accelerator cluster. Checkpoints are 12 TB. The capability profile sets a checkpoint write window of 120 s, a degraded-state throughput minimum of 70 %, three retained good checkpoints, an immutable retention of 30 days and a permitted data jurisdiction of a single named country. Storage follows pattern S1 for checkpoints with S2 for datasets and S6 for protection.

**Requirements (MCF-STO-002).** Required checkpoint write throughput is 12 TB ÷ 120 s = 100 GB/s. CMP data show a job-level mean time between interruptions of about 6 h. With a checkpoint cost of 120 s, the Young approximation gives an interval near √(2 × 120 s × 21,600 s) ≈ 2,280 s, about 38 minutes. The configured interval is 60 minutes. The assessor records an observation that the interval is longer than the first-order optimum; the lost-work tolerance (60 minutes) is still met on average, so this is not a nonconformity, but the profile owner is asked to confirm the choice.

**Throughput (MCF-STO-005).** The acceptance benchmark at production client count achieved 140 GB/s. A degraded-state benchmark with one storage server removed achieved 85 GB/s, which is 85 % of the requirement and above the 70 % minimum. However, no benchmark was run during erasure-coding rebuild; a production incident three months earlier shows checkpoint writes taking 260 s during a rebuild. The rebuild state is therefore demonstrated below requirement: MCF-STO-005 is **PARTIAL** with a Finding, and CG-08 is FAIL on this input.

**Integrity (MCF-STO-009, -017).** Checkpoints carry per-shard checksums in a manifest, and the training framework verifies them before resume. The assessor recomputed checksums for 40 sampled shards; all matched. An interrupted-write test showed that the previous good checkpoint remained usable. Both controls are **CONFORMING**. A link from CMP is noted: two nodes later failed SDC screening; the checkpoints from the job they ran in are checksum-consistent but were written from potentially corrupted state. Checksums cannot detect this. The assessor records a US4 UNKNOWN (U9) against the affected checkpoints' integrity, owned jointly with MCF-CMP-019.

**Protection (MCF-STO-014, -016).** Checkpoints replicate to a second site within a 45-minute lag (RPO 60 minutes). An immutable copy is held in object storage with retention locks, but in a mode that the storage administrator role can shorten, and that role is federated from the same identity provider as primary administration. MCF-STO-016 is **NONCONFORMING**; CG-10 is FAIL on this input. A dataset cache was found in a second region outside the permitted jurisdiction: a Finding against MCF-STO-001 and the residency condition is reported to the decision.

**Recovery (MCF-STO-018, -020).** Quarterly restore tests restored a checkpoint from the replica and resumed training with continuous loss curves. A restart after a simulated metadata failover has not been exercised. MCF-STO-020 is **CONFORMING**; MCF-STO-018 is **UNKNOWN** (U5, US4) for the metadata-disruption scenario, matching the AIDCF-008 §50 example.

**Gate Results (STO inputs only).** CG-08 FAIL (MCF-STO-005 PARTIAL), with an additional US4 UNKNOWN on checkpoint integrity; CG-10 FAIL (MCF-STO-016 NONCONFORMING), with MCF-STO-018 UNKNOWN; CG-09 not defeated by STO inputs (MCF-STO-015 CONFORMING after placement reconciliation). Final Gate Results depend on the controls of other domains.

**Actions.** Switch retention locks to a non-shortenable mode under a separately administered account and identity; benchmark during rebuild and tune rebuild priority or add capacity; remove the out-of-jurisdiction cache; exercise restart after metadata failover; screen or roll back checkpoints written while failed nodes participated. Each action carries a reassessment trigger.
