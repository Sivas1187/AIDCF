# AIDCF-007A Control Catalogue — STO AI Storage and Data Infrastructure

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-STO](../../../aidcf-018-domain-guides/AIDCF-018-STO_AI_Storage_and_Data_Infrastructure_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-STO-001](#mcf-sto-001) | Training Data Tier | DIRECTIVE | DESIGN | AL2 | — | CG-08, CG-01 |
| [MCF-STO-002](#mcf-sto-002) | Checkpoint Tier | DIRECTIVE | DESIGN | AL2 | — | CG-08, CG-10 |
| [MCF-STO-003](#mcf-sto-003) | Model and Artifact Tier | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-08, CG-10 |
| [MCF-STO-004](#mcf-sto-004) | Archive Tier | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-10 |
| [MCF-STO-005](#mcf-sto-005) | Throughput and IOPS | PREVENTIVE | EFFECTIVENESS | AL5 | CG-08 | — |
| [MCF-STO-006](#mcf-sto-006) | Metadata Performance | DETECTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-STO-007](#mcf-sto-007) | Capacity Headroom | PREVENTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-STO-008](#mcf-sto-008) | Burst Handling | PREVENTIVE | EFFECTIVENESS | AL5 | — | CG-08, CG-09 |
| [MCF-STO-009](#mcf-sto-009) | Data Integrity | DETECTIVE | EFFECTIVENESS | AL5 | CG-08 | — |
| [MCF-STO-010](#mcf-sto-010) | Metadata Integrity | PREVENTIVE | EFFECTIVENESS | AL5 | CG-08 | CG-10 |
| [MCF-STO-011](#mcf-sto-011) | Checksum and Scrubbing | DETECTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-STO-012](#mcf-sto-012) | Configuration Consistency | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-14, CG-08 |
| [MCF-STO-013](#mcf-sto-013) | Snapshot Protection | PREVENTIVE | OPERATION | AL4 | — | CG-10 |
| [MCF-STO-014](#mcf-sto-014) | Replication | RECOVERY | RESILIENCE | AL5 | — | CG-10, CG-09, CG-03 |
| [MCF-STO-015](#mcf-sto-015) | Erasure Coding | PREVENTIVE | RESILIENCE | AL5 | CG-09 | CG-08 |
| [MCF-STO-016](#mcf-sto-016) | Immutable Recovery Copy | RECOVERY | RESILIENCE | AL5 | CG-10 | CG-15 |
| [MCF-STO-017](#mcf-sto-017) | Checkpoint Durability | PREVENTIVE | EFFECTIVENESS | AL5 | CG-08 | CG-10 |
| [MCF-STO-018](#mcf-sto-018) | Restart Readiness | RECOVERY | RESILIENCE | AL5 | CG-10 | — |
| [MCF-STO-019](#mcf-sto-019) | Storage Recovery Sequencing | RECOVERY | RESILIENCE | AL5 | — | CG-10, CG-09 |
| [MCF-STO-020](#mcf-sto-020) | Recovery Validation | CORRECTIVE | RESILIENCE | AL5 | CG-10 | — |
| [MCF-STO-021](#mcf-sto-021) | Storage Telemetry | DETECTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-STO-022](#mcf-sto-022) | Capacity Forecasting | PREVENTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-STO-023](#mcf-sto-023) | Media Health | DETECTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-STO-024](#mcf-sto-024) | Secure Sanitisation | PREVENTIVE | IMPLEMENTATION | AL3 | — | — |

## STO-01 Storage architecture and tiering

### MCF-STO-001

**Training Data Tier** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure the storage tier holding training and fine-tuning datasets is designed for the read pattern of data loaders at cluster scale, preserves dataset versions and lineage, and keeps data within declared sovereignty and residency boundaries.

**Requirement.** The storage engineering authority shall document the training data tier (system type, for example parallel file system or object store with cache; capacity; read throughput per accelerator; dataset versioning and lineage mechanism; locations and jurisdictions of every copy). The data owner shall approve the residency and sovereignty constraints and shall confirm that every copy, cache and replica lies within them.

**Assessment criteria**

1. The tier design states system type, capacity, read throughput per accelerator and caching strategy.
2. Required read throughput is derived from workload data rate per accelerator × accelerator count with stated assumptions.
3. Dataset versioning and lineage (source, transformations, hash) are implemented and referenced by training jobs.
4. Every location holding the data (primary, cache, replica, backup) is listed with jurisdiction.
5. The data owner's residency and sovereignty approval exists and matches the location list.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Data-loader read throughput per accelerator | GB/s | workload-specific (illustrative 1) | Workload characterisation |
| Permitted data jurisdictions | list | capability-specific | Data owner; applicable law and contracts |

**Minimum evidence**

- Training data tier design
- Throughput derivation
- Dataset version and lineage records
- Data location register with jurisdictions
- Data owner residency approval

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E2; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; TRANSITION |
| periodCoverage | Current design version |
| independence | Residency register cross-checked against storage configuration by the assessor |
| mandatoryItems | Tier design; Location register; Residency approval |
| acceptableAlternatives | Cloud provider data-location attestations with configuration export |
| unknownEffect | US3 Material: data-tier adequacy or residency uncertain; CG-08 supporting; residency gaps reported to the decision as condition |
| reassessmentTriggers | New dataset class; New storage location or provider; Change in residency obligations |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION

**Assessment procedure**

1. Obtain tier design and derivation.
2. Recompute required throughput.
3. Sample datasets for lineage records.
4. Reconcile location register with configuration.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-01 Capability and outcome definition (SUPPORTING)

**Applicability.** Applies where in-scope workloads read training or fine-tuning data from storage within or controlled by the boundary.

**Lifecycle stages.** PLAN, DESIGN, CHANGE · **Operating states.** NORMAL, TRANSITION

**Failure modes addressed.** Data-loader starvation leaving accelerators idle; Unversioned dataset preventing reproducibility; Cache replica outside permitted jurisdiction

**Testing safety.** Desk-based and read-only.

**UNKNOWN rule.** If any data location is unknown, record U10 dependency UNKNOWN; sovereignty conformance cannot be asserted.

**Ontology classes.** InfrastructureSystem, Resource, ArchitectureSnapshot, Dependency · **Related controls.** MCF-STO-005, MCF-STO-014, MCF-STO-022, MCF-DEP-012

**Informative references.** AIDCF-013 (AI Data Centre Assurance Reference Architecture); Regulation (EU) 2016/679 (GDPR) and applicable national data-residency law; ISO/IEC 27001 (information security management systems)

### MCF-STO-002

**Checkpoint Tier** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure the checkpoint tier is sized so that model and optimiser state can be written within the declared checkpoint window at the declared interval, with the interval chosen against observed failure rates, and that checkpoints are placed in a fault domain independent of the compute they protect.

**Requirement.** The storage engineering authority shall document checkpoint size per job class, required write bandwidth (checkpoint size ÷ checkpoint window), checkpoint interval and its derivation from job-level failure rate and checkpoint cost, retention count, and the fault-domain separation between the checkpoint tier and the protected compute. The AI platform operator shall confirm the parameters per production job class.

**Assessment criteria**

1. Checkpoint size per job class is stated with its basis (parameter count, precision, optimiser state, sharding).
2. Required write bandwidth is derived from size and window and is within the tier's demonstrated capability (MCF-STO-005).
3. Checkpoint interval is justified against job-level mean time between interruptions and checkpoint cost.
4. Retention of N most recent good checkpoints is defined.
5. Checkpoint storage does not share a power, cooling or fabric fault domain with all of the compute it protects, or the residual risk is accepted.
6. Asynchronous or tiered (local NVMe then parallel file system) checkpointing, if used, documents when a checkpoint is considered durable.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Checkpoint size (large training job) | TB | job-specific (illustrative 10) | Model architecture and optimiser state |
| Checkpoint write window | s | 120 (illustrative) | Capability profile; acceptable step stall |
| Checkpoint interval | min | derived (illustrative 30) | Young/Daly model using measured interruption rate |
| Retained good checkpoints | count | 3 (illustrative) | Capability profile |

**Minimum evidence**

- Checkpoint tier design
- Size and bandwidth derivation
- Interval derivation with interruption-rate data
- Fault-domain separation analysis
- Durability definition for asynchronous checkpointing

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E2; E3; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; RECOVERY |
| periodCoverage | Current design; interruption data for 90 days |
| independence | Assessor recomputes bandwidth and interval |
| mandatoryItems | Size/bandwidth derivation; Fault-domain separation analysis |
| acceptableAlternatives | Training framework configuration plus measured checkpoint timings |
| unknownEffect | US3 Material: checkpoint adequacy uncertain; CG-10 and CG-08 supporting |
| reassessmentTriggers | New model scale; Change of checkpoint strategy; Interruption rate change |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW, RECONCILIATION

**Assessment procedure**

1. Recompute bandwidth from size and window.
2. Recompute interval from interruption data.
3. Review fault-domain separation.
4. Review durability definition.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to all in-scope training and long-running fine-tuning workloads. Not applicable to stateless inference, where MCF-STO-003 covers model artefacts.

**Lifecycle stages.** DESIGN, CHANGE · **Operating states.** NORMAL, DEGRADED, RECOVERY

**Failure modes addressed.** Checkpoint exceeds write window, stalling training; Interval too long for failure rate, losing hours of work; Checkpoints co-located with compute lost in the same event; Asynchronous checkpoint believed durable before flush

**Testing safety.** Desk-based recalculation; no checkpoints triggered.

**UNKNOWN rule.** If job interruption rates are unknown, record U1 UNKNOWN for the interval justification.

**Ontology classes.** CapacityAssertion, FaultDomain, Resource, RequiredFunction · **Related controls.** MCF-STO-005, MCF-STO-017, MCF-STO-018, MCF-CMP-008

**Informative references.** Young/Daly optimum checkpoint interval model (published literature); AIDCF-013 (AI Data Centre Assurance Reference Architecture); IO500 benchmark methodology (HPC storage performance)

### MCF-STO-003

**Model and Artifact Tier** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure trained models, adapters, tokenisers, configurations and release artefacts are stored in a versioned, access-controlled, integrity-protected registry from which deployments and recoveries draw known-good, hash-verified artefacts.

**Requirement.** The AI platform operator shall store model and release artefacts in a registry that assigns immutable versions, records content hashes and provenance (training run, dataset version, checkpoint), restricts write and delete to authorised roles, and verifies hashes at deployment. The storage service owner shall protect the registry under MCF-STO-013 to MCF-STO-016.

**Assessment criteria**

1. Artefacts have immutable versions with content hashes.
2. Provenance links artefact to training run, dataset version and source checkpoint.
3. Write and delete are restricted and logged.
4. Deployments verify hashes before use (sampled).
5. The registry is included in protection and recovery scope.

**Minimum evidence**

- Registry configuration
- Sample artefact records with hashes and provenance
- Access policy and logs
- Deployment hash-verification logs

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; RECOVERY |
| periodCoverage | Current configuration and 3 months of logs |
| independence | Assessor recomputes hashes for sampled artefacts |
| mandatoryItems | Artefact records; Access logs |
| acceptableAlternatives | Signed artefact manifests verified by deployment tooling |
| unknownEffect | US3 Material: artefact integrity uncertain; CG-10 supporting |
| reassessmentTriggers | Registry migration; Access policy change |

**Assessment methods.** RECONCILIATION, REPERFORMANCE, SAMPLING

**Assessment procedure**

1. Sample artefacts.
2. Recompute hashes.
3. Review provenance and access logs.
4. Check deployment verification.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to all model and release artefacts produced or served within the boundary.

**Lifecycle stages.** BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, RECOVERY

**Failure modes addressed.** Overwritten model version; Deployment of tampered artefact; Lost provenance

**Testing safety.** Read-only hash verification.

**UNKNOWN rule.** Artefacts without hash or provenance are recorded as U6 source-unverified UNKNOWN.

**Ontology classes.** AssetInstance, EvidenceObject, Safeguard · **Related controls.** MCF-STO-016, MCF-STO-009, MCF-SUP-013

**Informative references.** ISO/IEC 27040 (storage security); NIST SP 800-209 (security guidelines for storage infrastructure); ISO/IEC 27001 (information security management systems)

### MCF-STO-004

**Archive Tier** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure long-term retention of datasets, model versions and checkpoints needed for reproducibility, audit or regulatory purposes is held on a durable archive tier with defined retention, retrievability, integrity checking and media-refresh plans.

**Requirement.** The storage service owner shall define retention classes for archived AI data, shall store archives with fixity checks and at least the declared number of geographically or administratively separate copies, shall test retrieval at a defined interval, and shall plan media or format migration before end of support.

**Assessment criteria**

1. Retention classes and durations are defined.
2. Archive copies meet the declared count and separation.
3. Fixity checks run periodically with results recorded.
4. Retrieval tests meet declared retrieval times.
5. Media/format migration plans exist.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Archive copies | count | 2 (illustrative) | Capability profile |
| Retrieval time objective | h | 48 (illustrative) | Capability profile |

**Minimum evidence**

- Retention schedule
- Archive configuration
- Fixity check results
- Retrieval test records
- Migration plan

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E5 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | 12 months |
| independence | Assessor-selected retrieval sample |
| mandatoryItems | Fixity results; Retrieval tests |
| acceptableAlternatives | Cloud archive service attestations with retrieval evidence |
| unknownEffect | US2 Moderate: long-term reproducibility confidence capped |
| reassessmentTriggers | Media end-of-life; Retention obligation change |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, TEST

**Assessment procedure**

1. Review retention classes.
2. Review fixity results.
3. Select retrieval sample and review or run test.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies where AI data must be retained beyond active use.

**Lifecycle stages.** BUILD, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Archive unreadable after media obsolescence; Bit rot undetected; Retrieval slower than obligation

**Testing safety.** Retrieval to a test location only.

**UNKNOWN rule.** If fixity checks are absent, record U7 integrity-uncertain UNKNOWN.

**Ontology classes.** Resource, AssetInstance, TestRecord · **Related controls.** MCF-STO-011, MCF-STO-016, MCF-STO-024

**Informative references.** ISO 14721 (OAIS reference model for archives); ISO/IEC 27040 (storage security)

## STO-02 Performance and capacity

### MCF-STO-005

**Throughput and IOPS** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Demonstrate that the storage system delivers the aggregate read throughput for data loading and the aggregate write throughput for checkpointing that the outcome requires, at full cluster concurrency and in degraded states (failed server, rebuild in progress).

**Requirement.** The storage engineering authority shall demonstrate, by benchmark at acceptance and after material change, that aggregate read and write throughput and IOPS meet the required values at the declared client concurrency, including with one storage server or enclosure failed and during erasure-coding or RAID rebuild. The AI platform operator shall measure production checkpoint write times and compare them with the window in MCF-STO-002.

**Assessment criteria**

1. Benchmark results at declared concurrency meet required read and write throughput.
2. Degraded-state benchmarks (server failed, rebuild active) meet the declared degraded-state minimum.
3. Production checkpoint write times are within the window for the period.
4. Benchmark method (tool, file sizes, access pattern, client count) represents the AI workload.
5. Network path between clients and storage is included in the test, not only server-side capability.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Required aggregate checkpoint write throughput | GB/s | derived: checkpoint size ÷ window (illustrative 100) | MCF-STO-002 derivation |
| Degraded-state minimum | % of required throughput | 70 (illustrative) | Capability profile |
| Required aggregate read throughput | GB/s | derived from MCF-STO-001 | Workload characterisation |

**Minimum evidence**

- Acceptance and post-change benchmark reports
- Degraded-state benchmark report
- Production checkpoint timing data
- Benchmark method statement

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C3 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; RECOVERY |
| periodCoverage | Benchmarks within 12 months; 90 days production timings |
| independence | Assessor review of raw benchmark output and configuration |
| mandatoryItems | Benchmark reports including degraded state; Production checkpoint timings |
| acceptableAlternatives | Production telemetry under peak concurrent checkpoint demonstrating required throughput |
| unknownEffect | US4 Critical: CG-08 UNKNOWN for training outcomes |
| reassessmentTriggers | Storage expansion or upgrade; Client count growth; Checkpoint window breach |

**Assessment methods.** TEST, ANALYSIS, DOCUMENT_REVIEW

**Assessment procedure**

1. Review benchmark method for representativeness.
2. Compare results with requirements.
3. Review degraded-state results.
4. Analyse production checkpoint timings.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (CRITICAL)

**Applicability.** Applies to storage serving in-scope training data loading or checkpointing.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, RECOVERY

**Failure modes addressed.** Throughput collapse during rebuild; Benchmark unrepresentative (small client count); Network bottleneck hidden

**Testing safety.** Benchmarks at full concurrency compete with production; schedule in maintenance windows with AI platform operator agreement. Degraded-state tests use controlled server removal approved by the storage engineering authority, never data deletion.

**UNKNOWN rule.** If no degraded-state benchmark exists, record U5 coverage-gap UNKNOWN; CONFORMING requires degraded-state evidence.

**Ontology classes.** CapacityAssertion, TestRecord, InfrastructureSystem · **Related controls.** MCF-STO-002, MCF-STO-006, MCF-STO-008, MCF-NET-009

**Informative references.** IO500 benchmark methodology (HPC storage performance); AIDCF-013 (AI Data Centre Assurance Reference Architecture)

### MCF-STO-006

**Metadata Performance** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure metadata operations (open, create, stat, list) scale to the concurrency of AI jobs, because many-small-file datasets and synchronous checkpoint creation can saturate metadata services and stall entire clusters.

**Requirement.** The storage service owner shall define required metadata operation rates and latency at peak concurrency, shall monitor metadata latency and queue depth continuously, and shall apply workload guidance (file packing, sharded checkpoints, directory fan-out limits) agreed with the AI platform operator.

**Assessment criteria**

1. Required metadata rates and latency targets are defined.
2. Metadata latency and queue telemetry is collected and within targets for the period.
3. Workload guidance exists and is applied by sampled jobs.
4. Metadata saturation events are investigated.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Metadata operation p99 latency | ms | 10 (illustrative) | Capability profile |
| Required metadata operations | ops/s | workload-specific | Workload characterisation |

**Minimum evidence**

- Metadata targets
- Latency/queue telemetry
- Workload guidance
- Saturation event reviews

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | 90 days |
| independence | Assessor review of raw telemetry |
| mandatoryItems | Telemetry; Targets |
| acceptableAlternatives | Metadata benchmark at declared concurrency |
| unknownEffect | US3 Material: metadata-induced stalls possible; CG-08 supporting |
| reassessmentTriggers | New dataset format; Saturation event; Metadata server change |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW, SAMPLING

**Assessment procedure**

1. Review targets.
2. Analyse telemetry.
3. Sample jobs against guidance.
4. Review events.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to file-system based storage; for object stores, applies to listing and request-rate limits.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Metadata storm at synchronous checkpoint; Millions of small files exceeding inode or listing limits; Single metadata server bottleneck

**Testing safety.** Read-only telemetry review; no metadata benchmarks on production namespaces.

**UNKNOWN rule.** If metadata telemetry is not collected, record U1 UNKNOWN.

**Ontology classes.** InfrastructureSystem, CapacityAssertion, FailureMode · **Related controls.** MCF-STO-005, MCF-STO-010, MCF-STO-021

**Informative references.** IO500 benchmark methodology (HPC storage performance)

### MCF-STO-007

**Capacity Headroom** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Maintain free capacity above the level at which the storage system's performance, rebuild ability or checkpoint retention degrade, so that capacity exhaustion never halts checkpointing.

**Requirement.** The storage service owner shall define a capacity headroom threshold per tier that accounts for performance degradation at high fill, rebuild space and retention of N checkpoints, shall alert at warning and critical thresholds, and shall enforce quotas so that one job or tenant cannot exhaust a shared tier.

**Assessment criteria**

1. Headroom thresholds are defined per tier with rationale.
2. Utilisation stayed below the critical threshold for the period, or breaches were handled.
3. Quotas are configured for shared tiers.
4. Checkpoint retention space is reserved or accounted for.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Critical utilisation threshold | % of usable capacity | 80 (illustrative) | Storage vendor guidance; capability profile |
| Warning threshold | % of usable capacity | 70 (illustrative) | Capability profile |

**Minimum evidence**

- Threshold definitions
- Utilisation trend
- Quota configuration
- Breach handling records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | 90 days |
| independence | Assessor check of raw utilisation |
| mandatoryItems | Utilisation trend; Quota configuration |
| acceptableAlternatives | Cloud bucket metrics plus quota policies |
| unknownEffect | US3 Material: exhaustion risk; CG-08 supporting |
| reassessmentTriggers | Threshold breach; New tenant; Retention change |

**Assessment methods.** ANALYSIS, RECONCILIATION

**Assessment procedure**

1. Review headroom thresholds and their rationale.
2. Analyse utilisation by tier over the period.
3. Review quotas and breach handling.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all in-scope storage tiers.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Checkpoint write fails on full file system; Performance collapse near full; Rebuild impossible due to lack of spare capacity

**Testing safety.** Read-only review of utilisation and quota configuration.

**UNKNOWN rule.** If utilisation data is unavailable for a tier, record U1 UNKNOWN.

**Ontology classes.** CapacityAssertion, Resource · **Related controls.** MCF-STO-022, MCF-STO-002, MCF-OPS-021

**Informative references.** ISO/IEC 27040 (storage security)

### MCF-STO-008

**Burst Handling** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure the storage system absorbs synchronised write bursts (many ranks checkpointing simultaneously, several jobs checkpointing at once, restart storms after an outage) without timeouts, job failure or degradation of other tenants.

**Requirement.** The storage engineering authority shall characterise peak burst demand (concurrent checkpoints, restart read storm), shall provide burst absorption (client-side or burst-buffer tier, QoS, admission control or staggered checkpoint scheduling), and shall demonstrate by test or production evidence that the declared burst completes within the window without client timeouts or impact beyond tolerance on other workloads.

**Assessment criteria**

1. Peak burst demand is characterised including post-outage restart reads.
2. Burst absorption mechanisms are configured.
3. A test or production event shows the declared burst completed within the window.
4. No client timeouts or job failures attributable to storage occurred during the burst.
5. Impact on other tenants stayed within tolerance.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Concurrent checkpointing jobs | count | 3 (illustrative) | Workload characterisation |
| Restart read-storm completion time | min | 15 (illustrative) | Capability profile |

**Minimum evidence**

- Burst characterisation
- QoS/burst-buffer configuration
- Burst test or event telemetry
- Timeout and job failure logs

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E1; E5; E7 |
| qualityFloor | P4 F4 C3 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; RECOVERY |
| periodCoverage | Test within 12 months or event in 90 days |
| independence | Assessor analysis of raw telemetry |
| mandatoryItems | Burst test or event telemetry |
| acceptableAlternatives | Simulation calibrated to measured single-job checkpoint |
| unknownEffect | US3 Material: burst resilience uncertain; CG-08 and CG-09 supporting |
| reassessmentTriggers | New large job; Checkpoint scheduling change; Timeout incident |

**Assessment methods.** TEST, ANALYSIS

**Assessment procedure**

1. Review characterisation.
2. Review configuration.
3. Analyse burst telemetry and logs.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to shared storage serving synchronous training or multiple jobs.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, RECOVERY

**Failure modes addressed.** Restart storm after outage overwhelms storage; Concurrent checkpoints time out; Noisy neighbour degrades inference

**Testing safety.** Burst tests in maintenance windows only.

**UNKNOWN rule.** If restart read-storm behaviour is untested, record U5 UNKNOWN and link to MCF-STO-018.

**Ontology classes.** FailureScenario, Safeguard, CapacityAssertion · **Related controls.** MCF-STO-005, MCF-STO-018, MCF-CMP-012, MCF-NET-007

**Informative references.** IO500 benchmark methodology (HPC storage performance); AIDCF-004 (Threat, Hazard and Failure Model)

## STO-03 Integrity and consistency

### MCF-STO-009

**Data Integrity** · DETECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure data, checkpoints and model artefacts are protected end-to-end against undetected corruption from client to media and back, so that silent corruption cannot enter training or deployment.

**Requirement.** The storage engineering authority shall implement end-to-end integrity protection (application or file-level checksums on checkpoints and artefacts, plus storage-level checksums or protection information) and shall verify checksums on read and on restore. The AI platform operator shall verify checkpoint checksums before resuming training from them and shall treat a verification failure as an integrity incident.

**Assessment criteria**

1. Checksum or protection-information mechanisms cover the path from client to media.
2. Checkpoints and artefacts carry application-level checksums recorded at write.
3. Checksums are verified on restore and before resume (sampled).
4. Verification failures are treated as integrity incidents with impact analysis.
5. Detection effectiveness was demonstrated by injected corruption on a test copy.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Checksum coverage of checkpoints and artefacts | % | 100 (illustrative) | Capability profile |

**Minimum evidence**

- Integrity architecture description
- Checkpoint/artefact checksum records
- Resume-time verification logs
- Integrity incident records
- Corruption-injection test record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E1; E5 |
| qualityFloor | P4 F4 C3 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; RECOVERY |
| periodCoverage | 90 days logs; injection test within 12 months |
| independence | Assessor recomputes checksums for sampled objects |
| mandatoryItems | Checksum records; Injection test record |
| acceptableAlternatives | Real corruption event detected with full trace |
| unknownEffect | US4 Critical: CG-08 UNKNOWN for integrity outcomes |
| reassessmentTriggers | Storage software change; Integrity incident; New checkpoint format |

**Assessment methods.** TEST, REPERFORMANCE, ANALYSIS, DOCUMENT_REVIEW

**Assessment procedure**

1. Review integrity architecture.
2. Recompute checksums on sample.
3. Review resume-time verification.
4. Review injection test.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (CRITICAL)

**Applicability.** Applies to all in-scope training data, checkpoints and model artefacts.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE · **Operating states.** NORMAL, DEGRADED, RECOVERY

**Failure modes addressed.** Silent corruption in checkpoint resumed into training; Bit flip in transit undetected; Corrupt model deployed

**Testing safety.** Corruption injection only on test copies in isolated namespaces. Tests run against test namespaces or copies; no destructive action against production data, snapshots or recovery copies is permitted without the data owner's written authorisation.

**UNKNOWN rule.** If no end-to-end checksum exists for a data class, record US4 UNKNOWN for that class.

**Ontology classes.** Safeguard, FailureMode, EvidenceObject · **Related controls.** MCF-STO-011, MCF-STO-017, MCF-CMP-019, MCF-STO-020

**Informative references.** T10 Protection Information (SCSI) and NVMe end-to-end data protection; ISO/IEC 27040 (storage security); NIST SP 800-209 (security guidelines for storage infrastructure)

### MCF-STO-010

**Metadata Integrity** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure file-system or object-store metadata (namespace, layout, allocation, object maps) is protected, consistent and recoverable, because metadata loss can render intact data unreachable for the whole tier.

**Requirement.** The storage engineering authority shall protect metadata with redundancy independent of the data path (replicated metadata servers or volumes), shall run consistency checks at a defined interval, shall back up metadata where the platform supports it, and shall demonstrate metadata service failover and recovery on a test system or in a controlled test.

**Assessment criteria**

1. Metadata redundancy is configured and independent of single server or enclosure.
2. Consistency checks run at the interval and results are reviewed.
3. Metadata backups exist where supported and have been restored on test.
4. Metadata failover has been demonstrated within the declared time.
5. Metadata service failures in the period were contained.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Metadata failover time | s | 60 (illustrative) | Capability profile; vendor data |
| Consistency check interval | days | 30 (illustrative) | Vendor guidance |

**Minimum evidence**

- Metadata redundancy configuration
- Consistency check results
- Metadata backup and test restore records
- Failover test record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E1; E5 |
| qualityFloor | P4 F4 C3 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; FAILED; RECOVERY |
| periodCoverage | Failover test within 12 months |
| independence | Failover test witnessed by a party independent of the storage vendor |
| mandatoryItems | Failover test; Consistency results |
| acceptableAlternatives | Real failover event telemetry |
| unknownEffect | US4 Critical: CG-08 UNKNOWN for storage function |
| reassessmentTriggers | Metadata server change; Consistency error; Failed failover |

**Assessment methods.** TEST, DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Review redundancy.
2. Review checks and backups.
3. Review failover test.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (CRITICAL); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to all in-scope storage systems with separate metadata services.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, FAILED, RECOVERY

**Failure modes addressed.** Metadata corruption making tier unreadable; Metadata failover hang during training; Shared metadata volume single point of failure

**Testing safety.** Failover tests on production need storage engineering authority approval and a maintenance window. Tests run against test namespaces or copies; no destructive action against production data, snapshots or recovery copies is permitted without the data owner's written authorisation.

**UNKNOWN rule.** If metadata failover is untested, record US4 UNKNOWN against CG-08.

**Ontology classes.** InfrastructureSystem, Safeguard, FaultDomain, TestRecord · **Related controls.** MCF-STO-006, MCF-STO-019, MCF-STO-020

**Informative references.** ISO/IEC 27040 (storage security); AIDCF-004 (Threat, Hazard and Failure Model)

### MCF-STO-011

**Checksum and Scrubbing** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Detect latent media and data errors before they are needed by scrubbing stored data and verifying checksums on a schedule that completes within the declared cycle.

**Requirement.** The storage service owner shall schedule scrubbing so that all data on in-scope tiers is verified within the declared cycle, shall monitor scrub completion and error rates, and shall repair detected errors from redundancy promptly.

**Assessment criteria**

1. Scrub schedule covers all in-scope tiers.
2. Scrub cycles completed within the declared period.
3. Detected errors were repaired and trended.
4. Scrub impact on production performance is bounded.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Scrub cycle | days | 30 (illustrative) | Vendor guidance; capability profile |

**Minimum evidence**

- Scrub schedule
- Scrub completion records
- Error and repair logs

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | Most recent 3 cycles |
| independence | Assessor review of raw scrub logs |
| mandatoryItems | Completion records; Error logs |
| acceptableAlternatives | Object-store background verification reports |
| unknownEffect | US2 Moderate: confidence ceiling CONF-2 for integrity operating claims |
| reassessmentTriggers | Scrub cycle overrun; Error-rate rise |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW

**Assessment procedure**

1. Review scrub schedule coverage of all tiers.
2. Analyse completion of the last three cycles.
3. Review detected errors and their repair from redundancy.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to in-scope tiers with redundancy that supports repair.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Latent sector errors accumulating; Scrub never completing on large tiers

**Testing safety.** Read-only review of scrub logs; scrub schedules are not altered.

**UNKNOWN rule.** If scrub completion cannot be shown, record U1 UNKNOWN.

**Ontology classes.** Safeguard, EvidenceObject · **Related controls.** MCF-STO-009, MCF-STO-023, MCF-STO-015

**Informative references.** ISO/IEC 27040 (storage security)

### MCF-STO-012

**Configuration Consistency** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure storage configuration (protection schemes, quotas, exports, client mount options, QoS, replication policies, retention locks) matches the approved baseline across all storage systems and clients.

**Requirement.** The storage service owner shall maintain an approved storage configuration baseline, shall detect drift automatically, shall apply changes under change control with post-change verification, and shall verify client mount options and versions across the fleet.

**Assessment criteria**

1. An approved baseline exists.
2. Drift detection runs and drift is remediated.
3. Changes have change records and post-change verification.
4. Client mount options and versions conform across sampled nodes.

**Minimum evidence**

- Configuration baseline
- Drift reports
- Change records
- Client mount survey

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; TRANSITION |
| periodCoverage | Current state and 3 months changes |
| independence | Assessor sample of client mounts |
| mandatoryItems | Baseline; Drift report |
| acceptableAlternatives | Infrastructure-as-code repository with plan/apply logs |
| unknownEffect | US3 Material: protection settings may differ from design; CG-14 supporting |
| reassessmentTriggers | Storage software upgrade; Unapproved change |

**Assessment methods.** RECONCILIATION, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Obtain baseline.
2. Review drift.
3. Sample client mounts.
4. Review changes.

**Gate mappings.** CG-14 Change control (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all in-scope storage systems and clients.

**Lifecycle stages.** BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, TRANSITION

**Failure modes addressed.** Replication policy silently disabled; Client mount options degrading performance; Retention lock removed

**Testing safety.** Read-only configuration exports and client mount surveys.

**UNKNOWN rule.** Systems without drift detection are U5 coverage-gap UNKNOWN.

**Ontology classes.** ArchitectureSnapshot, AssetInstance · **Related controls.** MCF-STO-014, MCF-STO-016, MCF-OPS-017, MCF-SEC-008

**Informative references.** NIST SP 800-209 (security guidelines for storage infrastructure); ISO/IEC 27040 (storage security)

## STO-04 Protection and replication

### MCF-STO-013

**Snapshot Protection** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure snapshots of datasets, artefact registries and checkpoint directories are taken at the declared frequency, retained, protected from deletion by ordinary users, and actually restorable, to recover from accidental deletion or logical corruption.

**Requirement.** The storage service owner shall configure snapshot schedules and retention per protected namespace, shall restrict snapshot deletion to authorised roles, shall monitor snapshot success, and shall restore from snapshot on a sample basis at a defined interval.

**Assessment criteria**

1. Snapshot schedules and retention are configured per protected namespace.
2. Snapshot success rate is monitored and failures remediated.
3. Snapshot deletion is restricted and logged.
4. Sample restores from snapshot succeeded within the period.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Snapshot recovery point objective | h | 4 (illustrative) | Capability profile |
| Snapshot retention | days | 14 (illustrative) | Capability profile |

**Minimum evidence**

- Snapshot policy configuration
- Success monitoring
- Deletion permission configuration and logs
- Sample restore records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; RECOVERY |
| periodCoverage | 90 days |
| independence | Assessor-selected restore sample |
| mandatoryItems | Success monitoring; Sample restores |
| acceptableAlternatives | Backup system restores providing the same RPO |
| unknownEffect | US3 Material: logical recovery uncertain; CG-10 supporting |
| reassessmentTriggers | Policy change; Snapshot failures; Restore failure |

**Assessment methods.** ANALYSIS, SAMPLING, TEST

**Assessment procedure**

1. Review snapshot policies per protected namespace.
2. Analyse snapshot success over the period.
3. Review snapshot deletion permissions and logs.
4. Review sample restore results.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to namespaces holding in-scope data. Snapshots do not satisfy MCF-STO-016 because they share the storage system's fault and administrative domain.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, RECOVERY

**Failure modes addressed.** Snapshots silently failing; Snapshot deleted by compromised user; Snapshots on same system as corruption

**Testing safety.** Restores to test namespace only. Tests run against test namespaces or copies; no destructive action against production data, snapshots or recovery copies is permitted without the data owner's written authorisation.

**UNKNOWN rule.** If no sample restore exists, record U1 UNKNOWN for recoverability.

**Ontology classes.** Safeguard, TestRecord · **Related controls.** MCF-STO-016, MCF-STO-020

**Informative references.** NIST SP 800-34 (contingency planning guide for information systems); ISO/IEC 27031 (ICT readiness for business continuity)

### MCF-STO-014

**Replication** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure data required for recovery is replicated to a target in an independent fault domain (another hall, site or region) within the declared recovery point objective, within permitted jurisdictions, and that replication lag and failures are detected.

**Requirement.** The storage service owner shall define replication scope, target, mode (synchronous or asynchronous) and RPO per data class, shall place targets outside the source's power, cooling, network and administrative fault domains as declared, shall keep targets within permitted jurisdictions, shall monitor lag, and shall demonstrate failover or restore from the replica.

**Assessment criteria**

1. Replication scope, target, mode and RPO are defined per data class.
2. Target fault-domain independence is documented.
3. Targets are within permitted jurisdictions.
4. Replication lag stayed within RPO for the period, with alerts on breach.
5. Restore or failover from replica has been demonstrated within the period.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Replication RPO (checkpoints) | min | 60 (illustrative) | Capability profile |
| Replication RPO (datasets and artefacts) | h | 24 (illustrative) | Capability profile |

**Minimum evidence**

- Replication policy
- Fault-domain independence analysis
- Jurisdiction mapping
- Lag telemetry and alerts
- Replica restore/failover test

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; DEGRADED; RECOVERY; EMERGENCY |
| periodCoverage | 90 days lag data; test within 12 months |
| independence | Restore test witnessed or reperformed by a party other than the replication administrator |
| mandatoryItems | Lag telemetry; Replica restore test |
| acceptableAlternatives | Provider-managed replication with attestation and customer-run restore |
| unknownEffect | US3 Material: off-domain recovery uncertain; CG-10 supporting |
| reassessmentTriggers | Target change; RPO breach; Jurisdiction change |

**Assessment methods.** ANALYSIS, TEST, DOCUMENT_REVIEW, RECONCILIATION

**Assessment procedure**

1. Review policy and independence.
2. Reconcile jurisdictions.
3. Analyse lag.
4. Review restore test.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-09 Failure containment (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to data classes whose loss would exceed the recovery tolerance if the primary storage fault domain were lost.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, RECOVERY, EMERGENCY

**Failure modes addressed.** Replica in same fault domain; Replication silently stalled; Corruption replicated to target; Replica in non-permitted jurisdiction

**Testing safety.** Failover tests require data owner approval and must not reverse replication over good data. Tests run against test namespaces or copies; no destructive action against production data, snapshots or recovery copies is permitted without the data owner's written authorisation.

**UNKNOWN rule.** If target fault-domain independence is not documented, record U10 dependency UNKNOWN.

**Ontology classes.** Dependency, FaultDomain, Safeguard, TestRecord · **Related controls.** MCF-STO-016, MCF-STO-001, MCF-RES-016, MCF-DEP-005

**Informative references.** ISO 22301 (business continuity management systems); ISO/IEC 27031 (ICT readiness for business continuity); NIST SP 800-34 (contingency planning guide for information systems); Regulation (EU) 2016/679 (GDPR) and applicable national data-residency law

### MCF-STO-015

**Erasure Coding** · PREVENTIVE · claim type RESILIENCE · required AL5

**Objective.** Ensure erasure coding or RAID protection is configured so that stripes span independent failure domains (drive, server, enclosure, rack) and tolerate the declared number of concurrent failures, with rebuild completing before a further failure is likely.

**Requirement.** The storage engineering authority shall document the protection scheme per tier (for example k+m), the failure domains across which stripes are placed, the number of concurrent domain failures tolerated, and expected rebuild time at current capacity; shall verify placement against physical topology; and shall demonstrate rebuild of a failed component within the declared time.

**Assessment criteria**

1. Protection scheme and failure-domain placement are documented per tier.
2. Placement is verified against physical rack and power topology.
3. Concurrent failure tolerance meets the declared requirement.
4. Rebuild time at current fill is measured and within the declared time.
5. Rebuild performance impact is within the degraded-state minimum (MCF-STO-005).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Protection scheme | k+m | 8+2 (illustrative) | Capability profile; vendor options |
| Concurrent failure-domain tolerance | count | 2 (illustrative) | Capability profile |
| Rebuild time objective | h | 24 (illustrative) | Capability profile; vendor data |

**Minimum evidence**

- Protection configuration
- Placement-to-topology reconciliation
- Rebuild test or event record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E4; E7 |
| optionalClasses | E3; E5 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; DEGRADED; RECOVERY |
| periodCoverage | Rebuild evidence within 12 months |
| independence | Placement reconciliation reperformed by the assessor |
| mandatoryItems | Placement reconciliation; Rebuild record |
| acceptableAlternatives | Vendor durability analysis with site topology inputs |
| unknownEffect | US4 Critical: CG-09 UNKNOWN for storage containment |
| reassessmentTriggers | Expansion; Topology change; Rebuild overrun |

**Assessment methods.** RECONCILIATION, ANALYSIS, TEST

**Assessment procedure**

1. Review protection scheme.
2. Reconcile placement with topology.
3. Review rebuild evidence.

**Gate mappings.** CG-09 Failure containment (CRITICAL); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all in-scope storage using erasure coding or RAID.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, RECOVERY

**Failure modes addressed.** Stripe members in same rack lost together; Rebuild too slow at high fill; Power-feed common mode across enclosures

**Testing safety.** Rebuild tests by controlled component removal approved by the storage engineering authority. Tests run against test namespaces or copies; no destructive action against production data, snapshots or recovery copies is permitted without the data owner's written authorisation.

**UNKNOWN rule.** If placement versus topology cannot be verified, record US4 UNKNOWN against CG-09.

**Ontology classes.** FaultDomain, Safeguard, CapacityAssertion · **Related controls.** MCF-STO-005, MCF-STO-023, MCF-RES-005, MCF-CMP-008

**Informative references.** ISO/IEC 27040 (storage security); AIDCF-004 (Threat, Hazard and Failure Model)

### MCF-STO-016

**Immutable Recovery Copy** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure at least one copy of recovery-critical data (latest good checkpoints, model artefacts, key datasets, storage and platform configuration) is immutable for its retention period and held in a separate administrative and fault domain, so that ransomware, privileged-account compromise or operator error cannot destroy every copy.

**Requirement.** The storage service owner shall maintain an immutable recovery copy of declared recovery-critical data with retention locks that cannot be shortened by administrators of the primary system, in a separate administrative domain with separate credentials, and shall demonstrate restore from it within the declared time.

**Assessment criteria**

1. Recovery-critical data scope is declared.
2. Immutable copy exists with retention locks in compliance (non-shortenable) mode.
3. Administrative domain and credentials are separate from the primary.
4. Attempted deletion by a primary-domain administrator is refused (tested).
5. Restore from the immutable copy met the declared time within the period.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Immutable retention | days | 30 (illustrative) | Capability profile |
| Restore time from immutable copy | h | 24 (illustrative) | Capability profile |

**Minimum evidence**

- Scope declaration
- Retention-lock configuration
- Administrative separation evidence
- Deletion-refusal test
- Restore test record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; EMERGENCY; RECOVERY |
| periodCoverage | Test within 12 months |
| independence | Restore test witnessed by a party independent of storage administration |
| mandatoryItems | Retention-lock configuration; Deletion-refusal test; Restore test |
| acceptableAlternatives | Offline media copy with custody and restore test |
| unknownEffect | US4 Critical: CG-10 UNKNOWN for recovery from destructive events |
| reassessmentTriggers | Credential model change; Retention change; Restore failure |

**Assessment methods.** TEST, INSPECTION, DOCUMENT_REVIEW, RECONCILIATION

**Assessment procedure**

1. Review scope.
2. Inspect lock configuration.
3. Verify administrative separation.
4. Review deletion-refusal and restore tests.

**Gate mappings.** CG-10 Recovery readiness (CRITICAL); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to all Capability Instances whose recovery depends on stored state.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, EMERGENCY, RECOVERY

**Failure modes addressed.** Ransomware encrypts all copies; Privileged admin deletes backups; Retention lock in governance mode bypassed

**Testing safety.** Deletion-refusal tests use a test object and test account. Tests run against test namespaces or copies; no destructive action against production data, snapshots or recovery copies is permitted without the data owner's written authorisation.

**UNKNOWN rule.** If the immutable copy shares administrative credentials with primary, record a Finding; if untested, US4 UNKNOWN.

**Ontology classes.** Safeguard, FaultDomain, TestRecord · **Related controls.** MCF-STO-013, MCF-STO-014, MCF-STO-020, MCF-SEC-003

**Informative references.** NIST SP 800-209 (security guidelines for storage infrastructure); ISO/IEC 27040 (storage security); NIST SP 800-34 (contingency planning guide for information systems); ISO 22301 (business continuity management systems)

## STO-05 Checkpoint and recovery services

### MCF-STO-017

**Checkpoint Durability** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure each checkpoint is complete, consistent across all shards and ranks, durably committed and verifiable before it is marked good and before older checkpoints are deleted.

**Requirement.** The AI platform operator shall mark a checkpoint good only after all shards are written, flushed to durable storage, checksummed and manifest-recorded; shall never delete the previous good checkpoint until the new one is verified; and shall retain the declared number of good checkpoints. The storage service owner shall ensure the checkpoint tier honours flush semantics.

**Assessment criteria**

1. Checkpoint completion requires all shards, flush, checksum and manifest.
2. Previous good checkpoint is retained until the new one is verified.
3. Retained count meets the declared value for sampled jobs.
4. Partial or failed checkpoints are detected and not used.
5. A test interrupting a checkpoint mid-write showed the previous good checkpoint remained usable.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Retained good checkpoints | count | 3 (illustrative) | Capability profile |

**Minimum evidence**

- Checkpoint manifest examples
- Framework configuration
- Retention evidence
- Interrupted-write test

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E1; E5 |
| qualityFloor | P4 F4 C3 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; FAILED; RECOVERY |
| periodCoverage | 90 days; test within 12 months |
| independence | Assessor verification of manifests and checksums |
| mandatoryItems | Manifests; Interrupted-write test |
| acceptableAlternatives | Real interruption event showing safe fallback |
| unknownEffect | US4 Critical: CG-08 UNKNOWN for training integrity |
| reassessmentTriggers | Framework change; Checkpoint failure |

**Assessment methods.** TEST, REPERFORMANCE, SAMPLING

**Assessment procedure**

1. Sample production jobs and their checkpoint manifests.
2. Verify shard checksums against the manifest.
3. Review retention of previous good checkpoints.
4. Review the interrupted-write test result.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (CRITICAL); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to checkpointed in-scope workloads.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, FAILED, RECOVERY

**Failure modes addressed.** Partial checkpoint marked good; Previous checkpoint deleted before new verified; Asynchronous flush lost on power event

**Testing safety.** Interrupted-write test on non-production job.

**UNKNOWN rule.** If checkpoint completion semantics are undocumented, record US4 UNKNOWN.

**Ontology classes.** Safeguard, FailureMode, TestRecord · **Related controls.** MCF-STO-002, MCF-STO-009, MCF-STO-018

**Informative references.** Young/Daly optimum checkpoint interval model (published literature); T10 Protection Information (SCSI) and NVMe end-to-end data protection

### MCF-STO-018

**Restart Readiness** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure a training or fine-tuning job can be restarted from its latest good checkpoint on available capacity (including a different set of nodes or a reduced node count where the framework supports re-sharding) within the declared restart time objective.

**Requirement.** The AI platform operator shall maintain restart procedures and automation for production job classes, shall verify that checkpoints can be loaded on a different node set, shall measure time from failure to resumed training, and shall exercise restart at a defined interval including after a storage or facility event.

**Assessment criteria**

1. Restart procedures and automation exist per job class.
2. Restart onto a different node set has been demonstrated.
3. Time from failure to resumed training is measured and within objective.
4. Restart after a storage or facility event has been exercised.
5. Dependencies of restart (scheduler, storage, identity, data loaders) are documented.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Restart time objective | min | 30 (illustrative) | Capability profile |
| Lost work tolerance | min of training | 60 (illustrative) | Capability profile; checkpoint interval |

**Minimum evidence**

- Restart procedures
- Restart timing records
- Different-node-set restart test
- Post-event restart exercise
- Dependency list

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | RECOVERY; FAILED; DEGRADED |
| periodCoverage | 90 days events; exercise within 12 months |
| independence | Exercise observed by a party independent of the job owner |
| mandatoryItems | Restart timing records; Post-event exercise |
| acceptableAlternatives | Real recovery events with timelines |
| unknownEffect | US4 Critical: CG-10 UNKNOWN for training recovery |
| reassessmentTriggers | Framework change; Restart failure; Cluster change |

**Assessment methods.** SCENARIO_EXERCISE, ANALYSIS, DOCUMENT_REVIEW

**Assessment procedure**

1. Review procedures.
2. Analyse restart timings.
3. Review exercises.
4. Review dependencies.

**Gate mappings.** CG-10 Recovery readiness (CRITICAL)

**Applicability.** Applies to checkpointed in-scope workloads whose recovery tolerance relies on resuming rather than restarting from scratch.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** RECOVERY, FAILED, DEGRADED

**Failure modes addressed.** Checkpoint not loadable on new topology; Restart blocked by storage read storm; Hidden dependency on failed service

**Testing safety.** Exercises on non-production jobs or with job-owner approval.

**UNKNOWN rule.** If no post-event restart exercise exists, record US4 UNKNOWN against CG-10.

**Ontology classes.** FailureScenario, Safeguard, TestRecord, Dependency · **Related controls.** MCF-STO-017, MCF-STO-019, MCF-CMP-023, MCF-RES-016

**Informative references.** Young/Daly optimum checkpoint interval model (published literature); ISO 22301 (business continuity management systems)

### MCF-STO-019

**Storage Recovery Sequencing** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure that after a site, power or cooling event, storage services are brought back in a defined order (power and cooling verified, network and time, identity, metadata services, data servers, consistency checks, client mounts, then job readmission) so that recovery does not corrupt data or stall on hidden dependencies.

**Requirement.** The storage service owner shall maintain a storage recovery sequence with prerequisites, hold points and verification checks for each step, aligned with facility (THM/POW) and compute (CMP) recovery, and shall exercise it at a defined interval.

**Assessment criteria**

1. A recovery sequence exists with prerequisites, hold points and checks.
2. The sequence is aligned with facility and compute recovery sequences.
3. Dependencies (time, DNS, identity, key management) are available independently of storage.
4. The sequence has been exercised and timings recorded.
5. Consistency checks precede client readmission.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Storage recovery time objective | h | 4 (illustrative) | Capability profile |

**Minimum evidence**

- Recovery sequence document
- Cross-domain alignment record
- Dependency analysis
- Exercise record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E6 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | RECOVERY; FAILED; SHUTDOWN |
| periodCoverage | Exercise within 12 months |
| independence | Exercise observed by a party independent of storage operations |
| mandatoryItems | Sequence document; Exercise record |
| acceptableAlternatives | Real recovery event timeline |
| unknownEffect | US3 Material: recovery order uncertain; CG-10 supporting |
| reassessmentTriggers | Architecture change; Failed recovery |

**Assessment methods.** SCENARIO_EXERCISE, DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Review sequence and alignment.
2. Review dependency analysis.
3. Review exercise timings.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to all in-scope storage systems.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** RECOVERY, FAILED, SHUTDOWN

**Failure modes addressed.** Clients mount before metadata consistency; Key management unavailable to unlock encrypted storage; Circular dependency on DNS hosted on storage

**Testing safety.** Tabletop or test-system exercise unless live exercise authorised.

**UNKNOWN rule.** If dependencies on key management or identity are not analysed, record U10 UNKNOWN.

**Ontology classes.** FailureScenario, Dependency, Safeguard · **Related controls.** MCF-STO-018, MCF-STO-020, MCF-RES-014, MCF-THM-024

**Informative references.** ISO 22301 (business continuity management systems); ISO/IEC 27031 (ICT readiness for business continuity); NIST SP 800-34 (contingency planning guide for information systems)

### MCF-STO-020

**Recovery Validation** · CORRECTIVE · claim type RESILIENCE · required AL5

**Objective.** Demonstrate by periodic restore tests that every protected data class can be restored from each protection mechanism (snapshot, replica, immutable copy) to a usable, integrity-verified state within the declared recovery time, and that restored checkpoints actually resume training.

**Requirement.** The storage service owner shall run restore tests at a defined interval for each protected data class and protection mechanism, shall verify integrity of restored data by checksum, and, for checkpoints, the AI platform operator shall resume a training job from the restored checkpoint and confirm loss and step continuity.

**Assessment criteria**

1. Restore test schedule covers each data class and each protection mechanism.
2. Restores in the period met the recovery time.
3. Restored data passed checksum verification.
4. A restored checkpoint resumed training with expected continuity.
5. Failures were remediated and retested.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Restore test interval | months | 3 (illustrative) | Capability profile |

**Minimum evidence**

- Restore test schedule
- Restore test records with timings
- Checksum verification results
- Training resume evidence

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | RECOVERY; NORMAL |
| periodCoverage | 12 months |
| independence | Assessor-selected restore sample |
| mandatoryItems | Restore records; Checksum results; Resume evidence |
| acceptableAlternatives | Real restores in incidents with full evidence |
| unknownEffect | US4 Critical: CG-10 UNKNOWN for data recovery |
| reassessmentTriggers | Protection change; Restore failure |

**Assessment methods.** TEST, REPERFORMANCE, SAMPLING, ANALYSIS

**Assessment procedure**

1. Review restore schedule coverage by data class and mechanism.
2. Select a sample and review or reperform restores.
3. Verify checksums of restored data against source records.
4. Review training resume evidence for restored checkpoints.

**Gate mappings.** CG-10 Recovery readiness (CRITICAL)

**Applicability.** Applies to all protected in-scope data classes.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** RECOVERY, NORMAL

**Failure modes addressed.** Backups unrestorable; Restored checkpoint incompatible with current framework; Restore slower than objective

**Testing safety.** Restores to isolated test locations only. Tests run against test namespaces or copies; no destructive action against production data, snapshots or recovery copies is permitted without the data owner's written authorisation.

**UNKNOWN rule.** Data classes without a restore test in the interval are US4 UNKNOWN for CG-10.

**Ontology classes.** TestRecord, Safeguard, EvidenceObject · **Related controls.** MCF-STO-013, MCF-STO-014, MCF-STO-016, MCF-RES-016

**Informative references.** NIST SP 800-34 (contingency planning guide for information systems); ISO 22301 (business continuity management systems); ISO/IEC 27031 (ICT readiness for business continuity)

## STO-06 Storage monitoring and lifecycle

### MCF-STO-021

**Storage Telemetry** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Collect storage telemetry (throughput, IOPS, latency percentiles, metadata latency, capacity, rebuild state, client errors, replication lag) with completeness monitoring and time synchronisation, to detect degradation and support incident analysis.

**Requirement.** The storage service owner shall collect telemetry from all in-scope storage systems and a representative sample of clients at the declared interval, shall monitor collection completeness, shall time-synchronise with compute and facility telemetry, and shall alert on thresholds.

**Assessment criteria**

1. Telemetry covers servers, metadata services and sampled clients.
2. Completeness is monitored and meets target.
3. Time is synchronised with compute and facility telemetry.
4. Alerts exist for latency, errors, capacity and lag.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Telemetry interval | s | 30 (illustrative) | Capability profile |

**Minimum evidence**

- Storage telemetry schema covering server, metadata and client metrics
- Storage collection completeness reports
- Time sync configuration
- Alert definitions

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; RECOVERY |
| periodCoverage | 90 days |
| independence | Assessor comparison with device counters |
| mandatoryItems | Completeness reports; Alert definitions |
| acceptableAlternatives | Vendor monitoring service export |
| unknownEffect | US2 Moderate: confidence ceiling CONF-2 |
| reassessmentTriggers | Collector change; Completeness drop |

**Assessment methods.** ANALYSIS, INSPECTION

**Assessment procedure**

1. Review telemetry coverage of servers, metadata services and clients.
2. Analyse completeness and time alignment with compute telemetry.
3. Review alert thresholds and a sample of alert handling.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all in-scope storage.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, DEGRADED, RECOVERY

**Failure modes addressed.** Client-side errors invisible to server telemetry; Clock skew preventing correlation

**Testing safety.** Read-only comparison of stored telemetry with device counters.

**UNKNOWN rule.** If client-side telemetry is absent, record U5 UNKNOWN.

**Ontology classes.** EvidenceObject, AssetInstance · **Related controls.** MCF-STO-006, MCF-STO-022, MCF-CMP-017, MCF-NET-024

**Informative references.** ISO/IEC 27040 (storage security)

### MCF-STO-022

**Capacity Forecasting** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Forecast storage capacity and performance demand from planned training runs, dataset growth, checkpoint retention and model registry growth, against procurement lead times, so that expansion arrives before headroom thresholds are reached.

**Requirement.** The storage service owner shall forecast capacity and throughput demand over a horizon at least as long as procurement and deployment lead time, using the AI platform's planned workloads, and shall trigger expansion when the forecast crosses headroom thresholds within the lead time.

**Assessment criteria**

1. The forecast horizon is ≥ lead time.
2. Inputs include planned training runs, dataset growth and retention.
3. Forecast accuracy is reviewed against actuals.
4. Expansion triggers fired in time historically.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Forecast horizon | months | 9 (illustrative) | Procurement lead time |

**Minimum evidence**

- Forecast model
- Input data
- Forecast-versus-actual review
- Expansion trigger records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | 12 months |
| independence | Assessor review of forecast against actuals |
| mandatoryItems | Forecast; Forecast-versus-actual review |
| acceptableAlternatives | Cloud capacity reservations covering forecast |
| unknownEffect | US2 Moderate: capacity confidence capped |
| reassessmentTriggers | Major new workload; Lead-time change |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW, INQUIRY

**Assessment procedure**

1. Review model and inputs.
2. Compare with actuals.
3. Review triggers.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all in-scope storage tiers whose growth is driven by planned AI workloads.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Expansion arrives after exhaustion; Forecast ignores checkpoint retention

**Testing safety.** Desk-based review of forecast and procurement records.

**UNKNOWN rule.** If no forecast exists, record U1 UNKNOWN.

**Ontology classes.** CapacityAssertion, Resource · **Related controls.** MCF-STO-007, MCF-CAP-015, MCF-SUP-018

**Informative references.** ISO/IEC 27040 (storage security)

### MCF-STO-023

**Media Health** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Monitor drive and media health (SMART/NVMe health logs, wear level, media errors, annualised failure rate by model and lot) and replace degrading media proactively before redundancy is consumed.

**Requirement.** The storage service owner shall collect media health indicators, shall define proactive replacement thresholds, shall track failure rates by model and lot, and shall replace media before failure where thresholds are crossed.

**Assessment criteria**

1. Media health indicators are collected for all media.
2. Replacement thresholds are defined.
3. Failure rates by model/lot are tracked.
4. Proactive replacements occurred where thresholds crossed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| NVMe wear replacement threshold | % of rated endurance used | 90 (illustrative) | Vendor endurance rating |
| AFR investigation threshold | % | 2× fleet baseline (illustrative) | Capability profile |

**Minimum evidence**

- Media health data
- Thresholds
- AFR trend
- Replacement records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | 12 months |
| independence | Assessor sample of raw health logs |
| mandatoryItems | Health data; Replacement records |
| acceptableAlternatives | Vendor predictive-failure service |
| unknownEffect | US2 Moderate: confidence capped |
| reassessmentTriggers | AFR rise; New media model |

**Assessment methods.** ANALYSIS, SAMPLING

**Assessment procedure**

1. Review proactive replacement thresholds against vendor endurance data.
2. Analyse annualised failure rate by model and lot.
3. Sample proactive replacements against threshold crossings.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all in-scope storage media.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Batch failure of same lot; Wear-out of checkpoint tier flash

**Testing safety.** Read-only access to media health logs.

**UNKNOWN rule.** Media without health data are U5 UNKNOWN.

**Ontology classes.** AssetInstance, FailureMode · **Related controls.** MCF-STO-015, MCF-STO-011, MCF-SUP-012

**Informative references.** NVMe Base Specification (SMART / health information log); ISO/IEC 27040 (storage security)

### MCF-STO-024

**Secure Sanitisation** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure storage media and systems leaving service, RMA or tenant reassignment are sanitised to a recognised standard with verification, so that training data, model weights and credentials cannot be recovered.

**Requirement.** The storage service owner shall sanitise media by clear, purge or destroy methods appropriate to media type and data classification under a recognised sanitisation standard, shall verify sanitisation, shall issue per-device certificates, and shall keep custody until sanitisation or destruction is complete, including for media sent for RMA.

**Assessment criteria**

1. Method per media type and classification is defined.
2. Per-device sanitisation certificates exist for sampled devices.
3. Verification is performed and recorded.
4. Custody is maintained until completion including RMA.
5. Cryptographic erase key destruction is evidenced where used.

**Minimum evidence**

- Sanitisation procedure
- Per-device certificates
- Verification records
- Media custody records including RMA shipments

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | SHUTDOWN; TRANSITION |
| periodCoverage | 12 months |
| independence | Third-party certificates or assessor verification |
| mandatoryItems | Certificates; Custody records |
| acceptableAlternatives | Physical destruction certificates |
| unknownEffect | US2 Moderate: no gate; record for data-protection assertions |
| reassessmentTriggers | Disposal vendor change; Media type change |

**Assessment methods.** SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Sample devices retired or sent for RMA in the period.
2. Verify method against media type and data classification.
3. Verify certificates and verification records.
4. Trace custody until sanitisation or destruction.

**Gate mappings.** None

**Applicability.** Applies to all media that held in-scope data.

**Lifecycle stages.** DECOMMISSION · **Operating states.** SHUTDOWN, TRANSITION

**Failure modes addressed.** Data recoverable from RMA drive; Crypto-erase without key destruction evidence

**Testing safety.** Record review only.

**UNKNOWN rule.** Devices without certificates are U1 UNKNOWN and Findings.

**Ontology classes.** AssetInstance, Action, Safeguard · **Related controls.** MCF-CMP-024, MCF-PHY-019, MCF-ENV-020

**Informative references.** NIST SP 800-88 (guidelines for media sanitisation); IEEE 2883 (standard for sanitizing storage); ISO/IEC 27040 (storage security)
