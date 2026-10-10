# AIDCF-007A Control Catalogue — CAP AI Capability, Service Outcome and Demand Management

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-CAP](../../../aidcf-018-domain-guides/AIDCF-018-CAP_AI_Capability_and_Service_Outcome_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-CAP-001](#mcf-cap-001) | Capability Register | DIRECTIVE | IMPLEMENTATION | AL3 | CG-01 | — |
| [MCF-CAP-002](#mcf-cap-002) | Capability Ownership | DIRECTIVE | IMPLEMENTATION | AL3 | CG-13 | CG-01 |
| [MCF-CAP-003](#mcf-cap-003) | Lifecycle Status | DETECTIVE | OPERATION | AL4 | — | CG-01, CG-14 |
| [MCF-CAP-004](#mcf-cap-004) | Architecture Linkage | DIRECTIVE | IMPLEMENTATION | AL3 | CG-02 | CG-03, CG-01 |
| [MCF-CAP-005](#mcf-cap-005) | Availability Outcomes | DIRECTIVE | DESIGN | AL2 | CG-01 | — |
| [MCF-CAP-006](#mcf-cap-006) | Performance Outcomes | DIRECTIVE | DESIGN | AL2 | CG-01 | CG-08 |
| [MCF-CAP-007](#mcf-cap-007) | Integrity Outcomes | DIRECTIVE | DESIGN | AL2 | CG-01 | CG-08 |
| [MCF-CAP-008](#mcf-cap-008) | Recovery Outcomes | DIRECTIVE | DESIGN | AL2 | CG-01 | CG-10 |
| [MCF-CAP-009](#mcf-cap-009) | Criticality Criteria | DIRECTIVE | DESIGN | AL2 | — | CG-01 |
| [MCF-CAP-010](#mcf-cap-010) | Impact Tolerance | DIRECTIVE | DESIGN | AL2 | CG-01 | — |
| [MCF-CAP-011](#mcf-cap-011) | Stakeholder Consequence | DIRECTIVE | DESIGN | AL2 | — | CG-01 |
| [MCF-CAP-012](#mcf-cap-012) | Priority Classification | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-05, CG-06 |
| [MCF-CAP-013](#mcf-cap-013) | Current Demand Baseline | DETECTIVE | OPERATION | AL4 | — | CG-05, CG-06 |
| [MCF-CAP-014](#mcf-cap-014) | Peak and Transient Demand | DETECTIVE | OPERATION | AL4 | — | CG-05, CG-06 |
| [MCF-CAP-015](#mcf-cap-015) | Growth Forecast | DIRECTIVE | DESIGN | AL2 | — | — |
| [MCF-CAP-016](#mcf-cap-016) | Scenario Demand | RECOVERY | RESILIENCE | AL5 | — | CG-10, CG-05 |
| [MCF-CAP-017](#mcf-cap-017) | Load Envelope | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-05, CG-06 |
| [MCF-CAP-018](#mcf-cap-018) | Environmental Envelope | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-06 |
| [MCF-CAP-019](#mcf-cap-019) | Duration Limits | PREVENTIVE | EFFECTIVENESS | AL5 | — | CG-05, CG-06, CG-10 |
| [MCF-CAP-020](#mcf-cap-020) | State-Specific Limits | PREVENTIVE | OPERATION | AL4 | — | CG-09, CG-10 |
| [MCF-CAP-021](#mcf-cap-021) | Design-to-Operation Traceability | DETECTIVE | IMPLEMENTATION | AL3 | — | CG-02 |
| [MCF-CAP-022](#mcf-cap-022) | Commissioning Acceptance | PREVENTIVE | EFFECTIVENESS | AL5 | — | CG-02, CG-08, CG-14 |
| [MCF-CAP-023](#mcf-cap-023) | Material Change Impact | PREVENTIVE | OPERATION | AL4 | CG-14 | CG-01 |
| [MCF-CAP-024](#mcf-cap-024) | Retirement Control | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-14, CG-02, CG-04 |

## CAP-01 Capability inventory

### MCF-CAP-001

**Capability Register** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Maintain an authoritative register of AI Capability Instances (for example a named training cluster, an inference service pool, a sovereign AI hall) so that every assurance claim is anchored to an identified, bounded instance rather than to a site or product.

**Requirement.** The capability owner shall maintain a capability register in which each Capability Instance has a unique identifier, a description of the AI work it delivers (training, fine-tuning, inference, data preparation), its physical and logical location (site, hall, pods, clusters), its tenancy model, its lifecycle status, its accountable owner, its Service Outcomes and its current ArchitectureSnapshot reference. The capability owner shall reconcile the register to the scheduler or orchestration inventory and to the facility asset register at no more than the register reconciliation interval and after every material change.

**Assessment criteria**

1. Every Capability Instance has a unique, stable identifier and the required attributes (work type, location, tenancy model, lifecycle status, owner, Service Outcomes, ArchitectureSnapshot reference).
2. Every accelerator cluster, pod or service pool present in the scheduler or orchestration inventory is assigned to exactly one Capability Instance or recorded as out of scope with rationale.
3. Every Capability Instance in the register maps to physical locations present in the facility asset register.
4. The last reconciliation is within the reconciliation interval and after every material change in the period.
5. No assurance report in the period refers to a capability not present in the register at the report date.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Capability register reconciliation interval | months | 3 | Capability-profile parameter; illustrative, aligned to the rate of cluster expansion |

**Minimum evidence**

- Capability register extract with all attributes
- Scheduler or orchestration inventory export (cluster, pod, node counts) dated within the reconciliation interval
- Facility asset register extract for the halls and pods concerned
- Reconciliation record listing unmatched items and dispositions

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E7 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C4 R3 T4 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Register state at the assessment date and reconciliations over the preceding two intervals |
| independence | Scheduler and asset exports shall be produced by query executed or witnessed by the assessor |
| mandatoryItems | Capability register extract with all attributes; Scheduler or orchestration inventory export (cluster, pod, node counts) dated within the reconciliation interval; Reconciliation record listing unmatched items and dispositions |
| acceptableAlternatives | Configuration management database extract with capability tagging, where the CMDB is itself reconciled to the scheduler |
| unknownEffect | US5 Systemic: the Capability Instance definition is unresolved; CG-01 Gate Result UNKNOWN and decision capped at INCONCLUSIVE |
| reassessmentTriggers | New cluster, pod or service pool brought into service; Re-allocation of accelerators between instances; Change of tenancy model; Hall or site added to or removed from an instance |

**Assessment methods.** RECONCILIATION, INSPECTION, DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Obtain the register extract and check each instance for the required attributes.
2. Extract the scheduler or orchestration inventory and reconcile clusters, pods and node counts to Capability Instances.
3. Reconcile instance locations to the facility asset register.
4. Analyse unmatched items and their dispositions; treat unexplained differences as Findings.
5. Check reconciliation dates against the interval and change events.
6. Compare capabilities named in reports issued in the period with the register.

**Gate mappings.** CG-01 Capability and outcome definition (CRITICAL)

**Applicability.** Applies to every assurance programme; there is no assurance subject without it.

**Lifecycle stages.** PLAN, DESIGN, BUILD, OPERATE, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** Assurance claim made about 'the data centre' rather than a defined instance; New cluster in production but not in the register; Same accelerators counted in two instances; Register location does not match physical deployment

**Testing safety.** Read-only queries against scheduler and asset systems, executed by the system owner under assessor observation; no job submission or node draining is performed.

**UNKNOWN rule.** If the scheduler or orchestration inventory cannot be accessed, the instance boundary is unverified: record a US5 UNKNOWN Record against the Capability Instance and do not rely on the register alone.

**Ontology classes.** CapabilityInstance, ArchitectureSnapshot, AssetInstance · **Related controls.** MCF-CAP-002, MCF-CAP-004, MCF-CAP-003, MCF-GOV-001

**Informative references.** ISO/IEC 22237 series (data centre facilities and infrastructures); ISO/IEC 20000-1 (service management system) - service catalogue; ISO 55000 series (asset management); AIDCF-002 Core Conceptual Model

### MCF-CAP-002

**Capability Ownership** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that each Capability Instance has one accountable owner who owns its Service Outcomes, tolerances, risks and remediation, and who has authority over the facility and IT resources needed to sustain them.

**Requirement.** The accountable executive shall appoint, for each Capability Instance, one capability owner with documented authority over the Service Outcomes, impact tolerances, risk acceptance within delegated limits, and the commitment of facility, platform and provider resources needed to meet them. The capability owner shall be identified in the capability register, the RACI and the decision-rights matrix, and a deputy shall be named for EMERGENCY and RECOVERY states.

**Assessment criteria**

1. Each Capability Instance has exactly one appointed capability owner with a dated appointment.
2. The owner's authority over Service Outcomes, tolerances, risk acceptance limits and resource commitment is documented.
3. The owner is consistently identified in the capability register, RACI and decision-rights matrix.
4. A deputy is named and authorised for EMERGENCY and RECOVERY states.
5. Where facility and AI platform are run by different organisations, the owner's authority over each is established by contract or internal agreement.

**Minimum evidence**

- Capability owner appointment records
- Authority statement or delegation
- Capability register, RACI and decision-rights extracts
- Deputy appointment
- Facility and platform agreements establishing owner authority where organisations differ

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E6 |
| optionalClasses | E2 |
| qualityFloor | P3 F3 C4 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY; RECOVERY |
| periodCoverage | Appointments in force at the assessment date |
| independence | Assessor interviews the owner and deputy separately from the appointing executive |
| mandatoryItems | Capability owner appointment records; Capability register, RACI and decision-rights extracts |
| acceptableAlternatives | Organisational role description with explicit capability ownership, plus appointment of the current holder |
| unknownEffect | US4 Critical: CG-13 Gate Result UNKNOWN for the instance; decision capped at LIMITED |
| reassessmentTriggers | Owner or deputy change; Reorganisation; Change of facility operator or platform provider |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Obtain appointment and authority records for each instance.
2. Reconcile owner identity across register, RACI and decision-rights matrix.
3. Confirm deputy appointment and authority for EMERGENCY and RECOVERY.
4. Review agreements establishing authority across facility and platform organisations.
5. Interview the owner and deputy on authority to commit resources and accept risk.

**Gate mappings.** CG-13 Responsibility and authority (CRITICAL); CG-01 Capability and outcome definition (SUPPORTING)

**Applicability.** Applies to every Capability Instance in the register.

**Lifecycle stages.** PLAN, OPERATE, CHANGE · **Operating states.** NORMAL, EMERGENCY, RECOVERY

**Failure modes addressed.** Instance owned jointly by facility and platform teams with no single accountable owner; Owner lacks authority over the colocation facility; No deputy during a cooling emergency; Owner identity differs between registers

**Testing safety.** Interview and document review only.

**UNKNOWN rule.** If no appointment record exists, record a US4 UNKNOWN Record against CG-13 for the instance; de facto ownership described in interview is not sufficient.

**Ontology classes.** CapabilityInstance, ServiceOutcome, AssuranceDecision · **Related controls.** MCF-CAP-001, MCF-GOV-005, MCF-GOV-006, MCF-GOV-002

**Informative references.** ISO 37000 (governance of organizations); ISO/IEC 20000-1 (service management system); ISO 55000 series (asset management)

### MCF-CAP-003

**Lifecycle Status** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that each Capability Instance's lifecycle status (planned, in design, in build, commissioning, in service, degraded-service, in change, retiring, retired) is accurate at all times so that the claim type, evidence and gates applied match the instance's real stage.

**Requirement.** The capability owner shall define lifecycle status values and transition criteria for Capability Instances, shall record each status transition with date, approver and the evidence that the transition criteria were met, and shall not transition an instance to in-service until commissioning acceptance (MCF-CAP-022) is recorded. The assurance programme lead shall use the recorded status to select claim types and Assurance Levels for each assessment.

**Assessment criteria**

1. Lifecycle status values and transition criteria are defined.
2. Every status transition in the period has date, approver and evidence that transition criteria were met.
3. No instance entered in-service status before commissioning acceptance was recorded.
4. The recorded status of each instance matches observed reality (for example production workloads are not running on an instance recorded as commissioning).
5. Assessment plans in the period selected claim types consistent with the recorded status.

**Minimum evidence**

- Lifecycle status definitions and transition criteria
- Status transition log for the period
- Commissioning acceptance records
- Scheduler evidence of production workload on each instance
- Assessment plans

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E2; E7 |
| qualityFloor | P3 F4 C4 R3 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; TRANSITION |
| periodCoverage | Status transitions over the twelve months preceding the assessment |
| independence | Assessor obtains scheduler or tenancy evidence independently of the status log owner |
| mandatoryItems | Status transition log for the period; Commissioning acceptance records; Scheduler evidence of production workload on each instance |
| acceptableAlternatives | Change records for go-live with linked acceptance evidence |
| unknownEffect | US3 Material: claim-type selection for the instance may be wrong; decision condition recorded |
| reassessmentTriggers | Status transition; Production workload observed on a non-in-service instance; Partial retirement |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, OBSERVATION, SAMPLING

**Assessment procedure**

1. Review status definitions and transition criteria.
2. Sample transitions and verify approver and criteria evidence.
3. Compare in-service dates with commissioning acceptance dates.
4. Compare recorded status with scheduler or tenancy evidence of production use.
5. Check claim types in assessment plans against recorded status.

**Gate mappings.** CG-01 Capability and outcome definition (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to every Capability Instance.

**Lifecycle stages.** BUILD, COMMISSION, OPERATE, CHANGE, DECOMMISSION · **Operating states.** NORMAL, TRANSITION

**Failure modes addressed.** Customer workloads placed on a partially commissioned pod; Instance reported in service after partial retirement; Operation claims assessed on a capability still in build

**Testing safety.** Read-only scheduler queries; no workload is moved or paused.

**UNKNOWN rule.** If actual production use cannot be determined, record a U5 UNKNOWN against the status criterion and do not assume the recorded status is correct.

**Ontology classes.** CapabilityInstance, OperatingState, Event · **Related controls.** MCF-CAP-001, MCF-CAP-022, MCF-CAP-024

**Informative references.** ISO/IEC/IEEE 15288 (system life cycle processes); ISO 55000 series (asset management)

### MCF-CAP-004

**Architecture Linkage** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that each Capability Instance is linked to a current ArchitectureSnapshot that identifies the InfrastructureSystems, AssetInstances and Interfaces implementing its Required Functions (power, cooling, compute, storage, network, control plane), so that the assessment boundary is grounded in the real architecture.

**Requirement.** The capability architect shall maintain, for each Capability Instance, a current ArchitectureSnapshot linked in the assurance graph that identifies the Required Functions of each Service Outcome and the InfrastructureSystems, AssetInstances and Interfaces implementing them, including shared and external elements. The capability architect shall version the snapshot after every material change and shall reconcile it to as-built and as-configured evidence at no more than the architecture reconciliation interval.

**Assessment criteria**

1. Each Capability Instance has a current ArchitectureSnapshot reference in the graph.
2. Every Service Outcome is linked to Required Functions, and every Required Function is linked to the InfrastructureSystems that implement it.
3. Shared elements (for example a facility water loop serving several halls, a common spine layer, a shared parallel file system) and external elements are identified as such.
4. A sample of graph links reconciles to as-built drawings, single-line diagrams, P&IDs, topology exports and cluster manifests.
5. The snapshot was versioned after each material change and reconciled within the interval.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Architecture reconciliation interval | months | 6 | Capability-profile parameter; illustrative |

**Minimum evidence**

- ArchitectureSnapshot record and version history
- Assurance graph extract of Outcome-Function-System links
- As-built drawings, single-line diagrams and P&IDs for sampled links
- Network topology and cluster manifest exports
- Reconciliation record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E7 |
| optionalClasses | E6; E3 |
| qualityFloor | P3 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Snapshot current at the assessment date |
| independence | Technical exports taken from source systems by or in front of the assessor; drawings verified by site inspection for a sample |
| mandatoryItems | Assurance graph extract of Outcome-Function-System links; As-built drawings, single-line diagrams and P&IDs for sampled links; Network topology and cluster manifest exports |
| acceptableAlternatives | Where no graph exists, a controlled architecture register with function-to-system tables, with a traceability limitation recorded |
| unknownEffect | US4 Critical: CG-02 Gate Result UNKNOWN; decision capped at LIMITED |
| reassessmentTriggers | Material architecture change; Expansion or re-cabling of a fabric; Change in cooling topology; As-built discrepancy found |

**Assessment methods.** RECONCILIATION, INSPECTION, ANALYSIS, DOCUMENT_REVIEW

**Assessment procedure**

1. Obtain the snapshot and graph extract and check Outcome-Function-System completeness.
2. Identify shared and external elements and confirm they are marked.
3. Select a sample of links stratified by domain and reconcile to drawings, topology and manifests.
4. Verify a subset of the sample by site inspection or live read-only query.
5. Check versioning against the change log.

**Gate mappings.** CG-02 Boundary and architecture integrity (CRITICAL); CG-03 Critical dependency visibility (SUPPORTING); CG-01 Capability and outcome definition (SUPPORTING)

**Applicability.** Applies to every Capability Instance assessed above AL1.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** Assessment boundary drawn from a design that no longer matches the as-built state; Shared facility water loop not identified, hiding common-mode exposure; Storage system serving checkpoints omitted from architecture; Graph links to decommissioned equipment

**Testing safety.** Site verification follows induction and escort rules; no panels are opened and no equipment is operated. Network and cluster exports are read-only.

**UNKNOWN rule.** Any Required Function with no linked implementing system, or any link that cannot be reconciled to evidence, is recorded as a US4 UNKNOWN Record against CG-02.

**Ontology classes.** ArchitectureSnapshot, RequiredFunction, InfrastructureSystem, AssetInstance, Interface · **Related controls.** MCF-CAP-001, MCF-CAP-021, MCF-GOV-006, MCF-EVA-010

**Informative references.** ISO/IEC/IEEE 42010 (architecture description); ISO/IEC 22237 series (data centre facilities and infrastructures); AIDCF-013 AI Data Centre Assurance Reference Architecture

## CAP-02 Service outcome definition

### MCF-CAP-005

**Availability Outcomes** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Define availability Service Outcomes for each Capability Instance in units that reflect AI work actually delivered (for example usable accelerator capacity, job-serving availability), with measurement window, exclusions and tolerance, so that power, cooling and platform continuity can be assessed against a stated target.

**Requirement.** The capability owner shall approve, for each Capability Instance, availability Service Outcomes that state the unit of availability (for example fraction of committed accelerators schedulable and healthy, or fraction of inference requests served), the target, the measurement window, the maximum single-interruption duration, permitted exclusions (for example planned maintenance) and the data source for measurement. The capability owner shall ensure the outcomes are consistent with customer commitments (MCF-GOV-019) and impact tolerances (MCF-CAP-010).

**Assessment criteria**

1. Each Capability Instance has at least one approved availability Service Outcome.
2. Each outcome states unit, target, measurement window, maximum single-interruption duration, exclusions and measurement data source.
3. The unit measures delivered AI capability (schedulable healthy accelerators, served requests or equivalent) rather than facility uptime alone.
4. Targets and exclusions are consistent with customer commitments and impact tolerances.
5. The measurement data source exists and produces the metric for the current period.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Availability target | % of measurement window | 99.5 (training) / 99.9 (inference) | Capability-profile parameter set by the capability owner; illustrative only |
| Availability measurement window | days | 30 | Capability-profile parameter; illustrative |
| Maximum single-interruption duration | minutes | 60 | Capability-profile parameter; illustrative, derived from impact tolerance |

**Minimum evidence**

- Approved Service Outcome records for availability
- Metric definition and measurement data source description
- Current-period metric output
- Reconciliation to customer commitments and impact tolerances

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E3; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | Outcome definitions in force at the assessment date |
| independence | Approval by the capability owner, separate from the author; assessor reperforms metric derivation from source for one window |
| mandatoryItems | Approved Service Outcome records for availability; Metric definition and measurement data source description |
| acceptableAlternatives | Service level objective specification in the platform's SLO system, approved by the capability owner |
| unknownEffect | US5 Systemic: Service Outcome definition unresolved; CG-01 Gate Result UNKNOWN and decision capped at INCONCLUSIVE |
| reassessmentTriggers | Change of availability target or exclusions; Change of measurement data source; New customer commitment; Change of impact tolerance |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Obtain approved availability outcomes for each instance and check required fields.
2. Assess whether the unit measures delivered AI capability.
3. Reconcile targets and exclusions to customer commitments and impact tolerances.
4. Obtain the current-period metric and reperform its derivation from the data source for one window.
5. Interview the capability owner on how the target was derived.

**Gate mappings.** CG-01 Capability and outcome definition (CRITICAL)

**Applicability.** Applies to every in-service or planned Capability Instance with an availability expectation; research instances with no availability expectation shall record that expectation explicitly rather than omit the outcome.

**Lifecycle stages.** PLAN, DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Availability defined as facility power uptime while accelerators are unschedulable; No measurement window, so outages are averaged away; Exclusions so broad that the outcome is untestable; Target exceeds designed redundancy

**Testing safety.** Desk review and read-only metric extraction; no fault is induced to measure availability.

**UNKNOWN rule.** If the measurement data source cannot produce the metric, the outcome is defined but unmeasurable: criterion 5 is not met and a U1 UNKNOWN is recorded; this is not treated as a missing definition.

**Ontology classes.** ServiceOutcome, CapabilityInstance, CapacityAssertion · **Related controls.** MCF-CAP-010, MCF-GOV-019, MCF-CAP-008, MCF-CAP-006

**Informative references.** ISO/IEC 20000-1 (service management system); IEC 60300 series (dependability management); ISO/IEC 22237 series (data centre facilities and infrastructures) - availability classes

### MCF-CAP-006

**Performance Outcomes** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Define performance Service Outcomes that capture whether the infrastructure lets AI work run at its required speed (for example training goodput, step-time stability, inference latency percentiles, collective bandwidth), so that throttling, fabric congestion or storage stalls are visible as outcome failures rather than hidden behind availability.

**Requirement.** The capability owner shall approve, for each Capability Instance, performance Service Outcomes that state the metric (for example training goodput fraction, median and tail step time, inference latency at a stated percentile, sustained accelerator power without thermal or power throttling), target, measurement method, measurement window, workload or benchmark reference, and the infrastructure conditions under which the target applies. The AI platform owner shall ensure the measurement method is implemented and its data retained.

**Assessment criteria**

1. Each Capability Instance has at least one approved performance Service Outcome appropriate to its work type.
2. Each outcome states metric, target, method, window, workload or benchmark reference and infrastructure conditions.
3. At least one outcome detects infrastructure-induced degradation (thermal or power throttling, fabric congestion, storage stall).
4. The measurement method is implemented and produces data for the current period.
5. Targets are consistent with the design basis for power per accelerator, cooling capacity and fabric bandwidth.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Training goodput floor | % of wall-clock time doing useful training progress | 90 | Capability-profile parameter; illustrative |
| Inference latency percentile and bound | ms at p99 | set per service | Capability-profile parameter; no generic default |
| Throttling event tolerance | accelerator-hours throttled per week | 0 attributable to facility conditions | Capability-profile parameter; illustrative |

**Minimum evidence**

- Approved performance Service Outcome records
- Metric and method specifications with workload reference
- Current-period metric data
- Design basis extracts for power, cooling and fabric

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E3; E4 |
| qualityFloor | P3 F4 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | Outcome definitions in force at the assessment date |
| independence | Assessor or compute specialist reviews metric adequacy independently of the platform team |
| mandatoryItems | Approved performance Service Outcome records; Metric and method specifications with workload reference |
| acceptableAlternatives | SLO specifications in the platform observability system, approved by the capability owner |
| unknownEffect | US5 Systemic: Service Outcome definition unresolved; CG-01 Gate Result UNKNOWN and decision capped at INCONCLUSIVE |
| reassessmentTriggers | New accelerator generation or workload type; Change of benchmark or measurement method; Change of design power per accelerator; Fabric re-architecture |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INQUIRY

**Assessment procedure**

1. Obtain approved performance outcomes and check required fields.
2. Evaluate with a compute specialist whether the metrics detect infrastructure-induced degradation.
3. Confirm current-period data exist and reperform one metric derivation.
4. Compare targets with design basis for power, cooling and fabric.
5. Interview the AI platform owner on measurement implementation and retention.

**Gate mappings.** CG-01 Capability and outcome definition (CRITICAL); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to every Capability Instance whose value depends on delivered compute speed; that is all training and inference instances.

**Lifecycle stages.** PLAN, DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Accelerators thermally throttle under high facility water temperature while availability shows 100%; Fabric congestion halves training throughput unnoticed; Storage stalls during checkpointing degrade goodput; Performance target set without reference to power or cooling design

**Testing safety.** Desk review and read-only metric extraction. Benchmark runs, if requested for corroboration, are scheduled by the platform owner on non-production capacity.

**UNKNOWN rule.** If throttling or congestion data are not collected, record a U1 UNKNOWN against criterion 3; the outcome cannot then support CG-08 evaluation.

**Ontology classes.** ServiceOutcome, RequiredFunction, CapacityAssertion · **Related controls.** MCF-CAP-005, MCF-CAP-017, MCF-CAP-018, MCF-CAP-014

**Informative references.** MLCommons MLPerf benchmark suites (training and inference); ISO/IEC 25010 (systems and software quality models) - performance efficiency; ASHRAE TC 9.9 thermal guidelines for data processing environments

### MCF-CAP-007

**Integrity Outcomes** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Define integrity Service Outcomes for model weights, checkpoints, training data and inference results so that silent data corruption, partial writes and configuration drift are treated as outcome failures with stated tolerances and detection expectations.

**Requirement.** The capability owner shall approve, for each Capability Instance, integrity Service Outcomes stating which data and states are protected (model weights, optimiser state, checkpoints, datasets, configuration), the integrity property required (no undetected corruption, verified completeness, version provenance), the detection mechanism expected (checksums, end-to-end verification, accelerator error reporting), the tolerated detection latency and the required response. The data platform owner shall confirm that each detection mechanism exists.

**Assessment criteria**

1. Integrity outcomes identify protected data and states, including checkpoints and model weights.
2. Each outcome states the integrity property, detection mechanism, tolerated detection latency and required response.
3. Undetected corruption of model weights and checkpoints relied upon for recovery has a tolerance of zero.
4. Hardware-originated silent data corruption on accelerators is addressed by a stated detection expectation.
5. The data platform owner has confirmed each detection mechanism exists for the current architecture.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Checkpoint integrity verification point | event | on write and before restore | Capability-profile parameter; illustrative |
| Tolerated detection latency for dataset corruption | hours | 24 | Capability-profile parameter; illustrative |

**Minimum evidence**

- Approved integrity Service Outcome records
- Detection mechanism description per protected data class
- Data platform owner confirmation
- Response procedure references

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E2 |
| optionalClasses | E7; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; RECOVERY |
| periodCoverage | Outcome definitions in force at the assessment date |
| independence | Storage or compute specialist reviews adequacy of detection mechanisms |
| mandatoryItems | Approved integrity Service Outcome records; Detection mechanism description per protected data class |
| acceptableAlternatives | Data protection design specification approved by the capability owner and containing equivalent statements |
| unknownEffect | US5 Systemic: Service Outcome definition unresolved; CG-01 Gate Result UNKNOWN and decision capped at INCONCLUSIVE |
| reassessmentTriggers | Change of checkpoint format or storage system; New accelerator generation; Incident of detected or suspected silent data corruption; Change of dataset pipeline |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INQUIRY, INSPECTION

**Assessment procedure**

1. Obtain integrity outcomes and check coverage of protected data classes.
2. Review each detection mechanism with a storage or compute specialist.
3. Confirm zero tolerance for undetected corruption of recovery-critical checkpoints and weights.
4. Inspect configuration evidence that detection mechanisms exist (for example checksum settings, error-reporting configuration).
5. Interview the data platform owner on response procedures.

**Gate mappings.** CG-01 Capability and outcome definition (CRITICAL); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to every Capability Instance that stores model state or data whose corruption would affect outcomes; that is all training instances and inference instances serving stored weights.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, RECOVERY

**Failure modes addressed.** Corrupted checkpoint discovered only on restore after a power event; Silent data corruption on an accelerator propagates into a trained model; Partial checkpoint write accepted as complete; Model weights deployed without provenance verification

**Testing safety.** Desk review and read-only configuration inspection; no fault injection into production data.

**UNKNOWN rule.** If no detection mechanism can be shown for a protected data class, criterion 5 is NONCONFORMING (not UNKNOWN); UNKNOWN applies only where mechanism existence cannot be verified.

**Ontology classes.** ServiceOutcome, RequiredFunction, FailureMode · **Related controls.** MCF-CAP-008, MCF-CAP-006, MCF-EVA-006

**Informative references.** ISO/IEC 27040 (storage security); ISO/IEC 25012 (data quality model); NIST SP 800-209 (security guidelines for storage infrastructure)

### MCF-CAP-008

**Recovery Outcomes** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Define recovery Service Outcomes for each Capability Instance (time to restore stated capacity, tolerated loss of training progress, restoration order, recovered-state verification) so that power, cooling, compute, storage, network and control-plane recovery can be assessed against a stated target.

**Requirement.** The capability owner shall approve, for each Capability Instance, recovery Service Outcomes that state the recovery time objective for restoring a stated fraction of capacity, the recovery point objective (for training expressed as maximum lost training time, driving checkpoint interval; for inference as maximum state or configuration loss), the restoration order of dependent services (facility power, cooling, control plane, storage, fabric, compute, scheduler), and the verification required before declaring recovery. The capability owner shall ensure these outcomes are consistent with impact tolerances and customer commitments.

**Assessment criteria**

1. Each Capability Instance has approved recovery outcomes with RTO for a stated capacity fraction and RPO.
2. For training instances, RPO is expressed as maximum lost training time and is consistent with the configured checkpoint interval.
3. A restoration order of dependent services is defined from facility power through to scheduler.
4. Verification criteria for declaring recovery are defined (for example accelerator health checks, fabric validation, checkpoint integrity).
5. Recovery outcomes are consistent with impact tolerances and customer commitments.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Recovery time objective | hours to restore stated capacity | 4 to 80% capacity | Capability-profile parameter; illustrative |
| Recovery point objective (training) | minutes of lost training | 30 | Capability-profile parameter; illustrative, constrained by checkpoint write time |
| Recovered capacity fraction for RTO | % of committed accelerators | 80 | Capability-profile parameter; illustrative |

**Minimum evidence**

- Approved recovery Service Outcome records
- Restoration order definition
- Recovery verification criteria
- Checkpoint interval configuration extract
- Reconciliation to impact tolerances and commitments

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E2 |
| optionalClasses | E7; E4 |
| qualityFloor | P3 F4 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | RECOVERY; FAILED; EMERGENCY |
| periodCoverage | Outcome definitions in force at the assessment date |
| independence | Resilience specialist reviews consistency of RTO/RPO with architecture |
| mandatoryItems | Approved recovery Service Outcome records; Restoration order definition |
| acceptableAlternatives | Business continuity plan section for the instance, approved by the capability owner, containing equivalent content |
| unknownEffect | US5 Systemic: Service Outcome definition unresolved; CG-01 Gate Result UNKNOWN and decision capped at INCONCLUSIVE |
| reassessmentTriggers | Change of RTO/RPO; Change of checkpoint strategy or storage; New dependency in the restoration path; Failed recovery exercise |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Obtain recovery outcomes and check RTO, RPO, restoration order and verification criteria.
2. Extract checkpoint interval configuration and compare with RPO.
3. Analyse restoration order against the architecture snapshot for missing dependencies.
4. Reconcile to impact tolerances and customer commitments.

**Gate mappings.** CG-01 Capability and outcome definition (CRITICAL); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to every Capability Instance in service or in design.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** RECOVERY, FAILED, EMERGENCY

**Failure modes addressed.** Checkpoint interval longer than the tolerated lost training time; Restoration order omits the control plane or identity service; No criteria for declaring recovery, so degraded capacity is declared recovered; RTO shorter than the time to restart cooling and stabilise facility water

**Testing safety.** Desk review and read-only configuration extraction; recovery is not exercised under this control.

**UNKNOWN rule.** If the checkpoint interval cannot be extracted, record a U1 UNKNOWN against criterion 2; the RPO is then unsupported for CG-10 evaluation.

**Ontology classes.** ServiceOutcome, RequiredFunction, OperatingState · **Related controls.** MCF-CAP-010, MCF-CAP-016, MCF-CAP-007, MCF-CAP-005

**Informative references.** ISO 22301 (business continuity management systems); ISO/IEC 27031 (ICT readiness for business continuity)

## CAP-03 Criticality and materiality

### MCF-CAP-009

**Criticality Criteria** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Establish approved criteria for classifying Capability Instances, Service Outcomes and Required Functions by criticality, so that assurance depth, evidence floors, gate applicability and remediation priority follow consequence consistently.

**Requirement.** The accountable executive shall approve criticality criteria that classify Capability Instances, Service Outcomes and Required Functions into defined classes using stated consequence dimensions (safety, customer and contractual, financial, regulatory, reputational, societal dependency) and thresholds. The capability owner shall apply the criteria to every in-scope item, record the class and rationale, and re-apply them after every material change.

**Assessment criteria**

1. Criticality criteria are approved and define classes, consequence dimensions and thresholds.
2. Every in-scope Capability Instance, Service Outcome and Required Function has a recorded class and rationale.
3. Reperformance of the classification for a sample yields the same class.
4. Classifications were re-applied after each material change in the period.
5. Criticality class is used to set assurance depth in the assurance plan (MCF-GOV-013).

**Minimum evidence**

- Approved criticality criteria
- Classification register with rationale
- Change-triggered reclassification records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E6 |
| qualityFloor | P3 F3 C4 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Classifications in force at the assessment date |
| independence | Assessor reperforms classification for a sample |
| mandatoryItems | Approved criticality criteria; Classification register with rationale |
| acceptableAlternatives | Business impact analysis outputs applying approved criteria |
| unknownEffect | US3 Material: assurance depth may be mis-set; decision condition recorded |
| reassessmentTriggers | New Capability Instance or Service Outcome; Change of consequence thresholds; Material change to an instance |

**Assessment methods.** DOCUMENT_REVIEW, REPERFORMANCE, SAMPLING

**Assessment procedure**

1. Review the criteria for classes, dimensions and thresholds.
2. Check completeness of the classification register.
3. Reperform classification for a sample.
4. Check reclassification after material changes and use in the assurance plan.

**Gate mappings.** CG-01 Capability and outcome definition (SUPPORTING)

**Applicability.** Applies to every programme.

**Lifecycle stages.** PLAN, DESIGN, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** Inconsistent classification across instances; Criticality not updated after a customer contract change; Assurance depth unrelated to consequence

**Testing safety.** Desk review and reperformance on records only.

**UNKNOWN rule.** If rationale is missing for a classification, reperform it; record a U9 UNKNOWN only if reviewers cannot agree on the class.

**Ontology classes.** CapabilityInstance, ServiceOutcome, RequiredFunction · **Related controls.** MCF-CAP-010, MCF-CAP-011, MCF-CAP-012, MCF-GOV-013

**Informative references.** ISO 22301 (business continuity management systems) - business impact analysis; ISO 31000 (risk management guidelines)

### MCF-CAP-010

**Impact Tolerance** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Set approved, measurable impact tolerances for each Service Outcome (maximum tolerable interruption, capacity reduction, lost work and integrity loss) that define the limit beyond which harm is unacceptable, and against which gates and decisions are evaluated.

**Requirement.** The capability owner shall set, and the accountable executive shall approve, for each Service Outcome of each Capability Instance, impact tolerances stating maximum tolerable interruption duration, maximum tolerable capacity reduction and its duration, maximum tolerable loss of work (for example training progress), and tolerated integrity loss, each with units and the operating states to which it applies. Tolerances shall lie within risk appetite limits (MCF-GOV-014) or have governing-body approval of the exceedance.

**Assessment criteria**

1. Each Service Outcome has approved impact tolerances with units and applicable operating states.
2. Tolerances cover interruption duration, capacity reduction with duration, loss of work and integrity loss.
3. Tolerances lie within risk appetite limits or the exceedance is approved by the governing body.
4. Tolerances are at least as stringent as customer commitments for the same outcome.
5. Tolerances are expressed so that a test or observation can show whether they were breached.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum tolerable interruption | hours | 8 | Capability-profile parameter; illustrative |
| Maximum tolerable capacity reduction | % of committed capacity for stated duration | 50% for 24 h | Capability-profile parameter; illustrative |
| Maximum tolerable lost training progress | hours of training | 2 | Capability-profile parameter; illustrative |

**Minimum evidence**

- Approved impact tolerance records per Service Outcome
- Approval record by the accountable executive
- Reconciliation to risk appetite and customer commitments

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C4 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY; RECOVERY |
| periodCoverage | Tolerances in force at the assessment date |
| independence | Approval by the accountable executive, separate from the capability owner who set them |
| mandatoryItems | Approved impact tolerance records per Service Outcome; Approval record by the accountable executive |
| acceptableAlternatives | Business impact analysis with approved maximum tolerable periods of disruption |
| unknownEffect | US5 Systemic: tolerance T in the top claim is undefined; CG-01 Gate Result UNKNOWN and decision capped at INCONCLUSIVE |
| reassessmentTriggers | Change of risk appetite; New or changed customer commitment; Incident exceeding a tolerance |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Obtain tolerance records and approvals for each Service Outcome.
2. Check coverage of the four tolerance dimensions and operating states.
3. Reconcile to risk appetite limits and customer commitments.
4. Assess each tolerance for testability.

**Gate mappings.** CG-01 Capability and outcome definition (CRITICAL)

**Applicability.** Applies to every Service Outcome of every in-scope Capability Instance.

**Lifecycle stages.** PLAN, DESIGN, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY, RECOVERY

**Failure modes addressed.** Tolerance stated qualitatively ('minimal disruption'); Tolerance looser than customer SLA; No tolerance for degraded capacity, only total outage; Tolerance not approved

**Testing safety.** Desk review only; tolerances are not validated by inducing disruption under this control.

**UNKNOWN rule.** A tolerance that exists but is not testable makes criterion 5 PARTIAL; UNKNOWN is recorded only if the approval cannot be evidenced.

**Ontology classes.** ServiceOutcome, CapabilityInstance, OperatingState · **Related controls.** MCF-CAP-005, MCF-CAP-008, MCF-GOV-014, MCF-GOV-007

**Informative references.** ISO 22301 (business continuity management systems); ISO 22317 (business impact analysis); ISO 31000 (risk management guidelines)

### MCF-CAP-011

**Stakeholder Consequence** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Identify who is harmed, and how, when each Service Outcome is not met (internal research teams, external tenants, downstream services relying on inference, safety-relevant users), so that criticality and tolerances reflect real consequence chains.

**Requirement.** The capability owner shall record, for each Service Outcome, the stakeholder groups affected by its failure, the consequence mechanism (for example lost training progress, failed inference for a dependent service, breach of a regulatory obligation), the consequence severity under each operating state and any downstream dependency outside the boundary. The capability owner shall review the analysis with representatives of affected stakeholder groups at least once per planning period.

**Assessment criteria**

1. Each Service Outcome lists affected stakeholder groups and consequence mechanisms.
2. Consequence severity is stated per operating state.
3. Downstream services outside the boundary that depend on the outcome are identified.
4. Representatives of affected stakeholder groups reviewed the analysis in the current planning period.
5. The analysis is reflected in criticality classification and impact tolerances.

**Minimum evidence**

- Stakeholder consequence analysis per Service Outcome
- Stakeholder review records
- Traceability to criticality and tolerances

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E6 |
| optionalClasses | E7 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; FAILED |
| periodCoverage | Analysis current within the planning period |
| independence | Assessor interviews at least one affected stakeholder representative directly |
| mandatoryItems | Stakeholder consequence analysis per Service Outcome; Stakeholder review records |
| acceptableAlternatives | Business impact analysis containing stakeholder consequence content |
| unknownEffect | US3 Material: criticality and tolerance rationale qualified; decision condition recorded |
| reassessmentTriggers | New tenant or dependent service; Incident revealing unanticipated consequence; Change of Service Outcome |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY, ANALYSIS

**Assessment procedure**

1. Obtain the consequence analysis and check coverage per outcome and state.
2. Interview at least one affected stakeholder representative.
3. Check identification of downstream dependent services.
4. Trace the analysis to criticality and tolerance records.

**Gate mappings.** CG-01 Capability and outcome definition (SUPPORTING)

**Applicability.** Applies to every Service Outcome; where the only stakeholder is the owner's own research function, the analysis may be brief but is still required.

**Lifecycle stages.** PLAN, DESIGN · **Operating states.** NORMAL, DEGRADED, FAILED

**Failure modes addressed.** Inference outage affects a dependent safety-relevant service not considered; Tenants' contractual exposure unknown to the owner; Consequence in degraded state ignored

**Testing safety.** Interview and desk review only; stakeholder interviews do not disclose other stakeholders' confidential information.

**UNKNOWN rule.** If an affected stakeholder group cannot be consulted, record a U2 UNKNOWN against its consequence entry.

**Ontology classes.** ServiceOutcome, Dependency, OperatingState · **Related controls.** MCF-CAP-009, MCF-CAP-010, MCF-GOV-017

**Informative references.** ISO 22317 (business impact analysis); ISO 22301 (business continuity management systems)

### MCF-CAP-012

**Priority Classification** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that the relative priority of workloads, tenants and Capability Instances is defined and implemented in the mechanisms that allocate scarce resources during degradation (power capping, load shedding, thermal curtailment, scheduler pre-emption), so that the most critical outcomes are protected first.

**Requirement.** The capability owner shall define priority classes for workloads, tenants and Capability Instances derived from criticality, and the AI platform owner and facility operator shall implement those classes in scheduler pre-emption policies, power-capping and load-shedding sequences and thermal curtailment procedures. The capability owner shall confirm at the priority reconciliation interval that implemented sequences match the defined classes.

**Assessment criteria**

1. Priority classes are defined and derived from criticality classification.
2. Scheduler pre-emption and quota configuration implement the priority classes.
3. Power-capping and load-shedding sequences (EPMS or rack power management) and thermal curtailment procedures implement the same priority order.
4. Reconciliation of implemented sequences to priority classes is within the interval.
5. No safety-related or control-plane load is placed in a shed group ahead of AI workload.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Priority reconciliation interval | months | 6 | Capability-profile parameter; illustrative |

**Minimum evidence**

- Priority class definitions
- Scheduler pre-emption and quota configuration export
- Load-shedding and power-capping sequence configuration
- Thermal curtailment procedure
- Reconciliation record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4 |
| qualityFloor | P3 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY |
| periodCoverage | Configuration current at the assessment date |
| independence | Configuration exports taken from source systems under assessor observation |
| mandatoryItems | Priority class definitions; Scheduler pre-emption and quota configuration export; Load-shedding and power-capping sequence configuration |
| acceptableAlternatives | Where load shedding is manual, the switching procedure with shed order and evidence of operator training |
| unknownEffect | US3 Material: degraded-state protection of critical outcomes unverified; decision condition recorded |
| reassessmentTriggers | New tenant or workload class; Change of shed sequence or EPMS logic; Scheduler policy change |

**Assessment methods.** RECONCILIATION, INSPECTION, DOCUMENT_REVIEW

**Assessment procedure**

1. Review priority class definitions and their derivation from criticality.
2. Export scheduler pre-emption and quota configuration and map to classes.
3. Export load-shedding and power-capping sequences and review thermal curtailment procedures; map to classes.
4. Confirm that safety and control-plane loads are not shed before AI workloads.
5. Check the reconciliation record date.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to instances where any resource can become constrained in a degraded state; that is all instances with shared power or cooling.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY

**Failure modes addressed.** Load shedding drops the highest-priority tenant first; Power capping applied uniformly, degrading critical inference; Control-plane servers in the same shed group as training racks; Scheduler pre-emption contradicts facility priority

**Testing safety.** Read-only configuration export; shed sequences are not exercised under this control. Any sequence test is performed under the POW or THM domain controls with their authorisation requirements.

**UNKNOWN rule.** If EPMS shed-sequence configuration cannot be exported, record a U2 UNKNOWN against criterion 3.

**Ontology classes.** Safeguard, CapabilityInstance, OperatingState · **Related controls.** MCF-CAP-009, MCF-CAP-017, MCF-CAP-020

**Informative references.** IEC 60364 series (low-voltage electrical installations); ISO/IEC 20000-1 (service management system)

## CAP-04 Demand and growth modelling

### MCF-CAP-013

**Current Demand Baseline** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Establish a measured baseline of the current IT, cooling and network demand of each Capability Instance (electrical load per pod and hall, heat rejected to air and liquid, facility water flow, fabric utilisation, storage throughput) from telemetry over a representative period, so that capacity and headroom claims rest on measurement rather than nameplate.

**Requirement.** The capacity manager shall establish, for each Capability Instance, a demand baseline derived from telemetry over at least the baseline period, covering electrical demand at rack, row, pod and hall level, heat load to air and to liquid, facility water flow and temperatures, and fabric and storage utilisation. The capacity manager shall state telemetry sources, resolution, gaps and calibration status, and refresh the baseline at the baseline refresh interval and after material change.

**Assessment criteria**

1. The baseline covers electrical, thermal (air and liquid), facility water, fabric and storage demand for each instance.
2. The baseline is derived from telemetry over at least the baseline period, with sources, resolution and gaps stated.
3. Metering used for electrical and thermal baselines has current calibration or accuracy verification.
4. Baseline values reconcile to an independent source for a sample (for example utility meter, UPS output, CDU heat-meter readings).
5. The baseline was refreshed within the interval and after each material change.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Baseline period | days | 90 | Capability-profile parameter; illustrative, should include representative workload cycles |
| Baseline telemetry resolution | seconds | 60 | Capability-profile parameter; illustrative, transient characterisation is addressed in MCF-CAP-014 |
| Baseline refresh interval | months | 3 | Capability-profile parameter; illustrative |

**Minimum evidence**

- Demand baseline report with methods and sources
- Telemetry extracts for the baseline period
- Meter calibration or verification records
- Independent reconciliation sample

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | At least the baseline period ending within the refresh interval |
| independence | Assessor reperforms aggregation for one hall or pod from raw telemetry |
| mandatoryItems | Demand baseline report with methods and sources; Telemetry extracts for the baseline period; Independent reconciliation sample |
| acceptableAlternatives | Commissioning load measurements for an instance in service for less than the baseline period, with limitation recorded |
| unknownEffect | US3 Material: capacity headroom claims in POW and THM rest on unverified demand; decision condition recorded |
| reassessmentTriggers | New accelerator generation or cluster expansion; Change of workload mix; Meter replacement or recalibration; Telemetry outage longer than 10% of the baseline period |

**Assessment methods.** ANALYSIS, RECONCILIATION, INSPECTION, REPERFORMANCE

**Assessment procedure**

1. Obtain the baseline report and check coverage across domains.
2. Obtain raw telemetry and reperform aggregation for one hall or pod.
3. Review meter calibration and telemetry gap records.
4. Reconcile a sample of baseline values to independent sources.
5. Check refresh dates against the interval and change events.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to every in-service Capability Instance. For instances in design, MCF-CAP-015 forecasts substitute until in service.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Headroom claimed from nameplate ratings while actual load is far higher; Liquid heat load not metered, so cooling headroom is guessed; Telemetry gaps conceal peak periods; Uncalibrated meters bias the baseline

**Testing safety.** Read-only telemetry extraction; no meter is disconnected or tested under this control.

**UNKNOWN rule.** If telemetry gaps exceed 10% of the baseline period or calibration status is unknown for a primary meter, record a U5 or U6 UNKNOWN and limit the baseline to the covered portion.

**Ontology classes.** CapacityAssertion, Resource, InfrastructureSystem · **Related controls.** MCF-CAP-014, MCF-CAP-015, MCF-CAP-017

**Informative references.** ISO/IEC 30134 series (data centre key performance indicators); ISO 50001 (energy management systems); ASHRAE TC 9.9 thermal guidelines for data processing environments

### MCF-CAP-014

**Peak and Transient Demand** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Characterise the peak and fast-transient demand of AI workloads (synchronous training power swings at iteration and checkpoint boundaries, job start and stop steps, inrush on restart, rapid heat-load changes on liquid loops) so that UPS, generation, grid connection, protection and cooling control are sized and tuned for real dynamics.

**Requirement.** The capacity manager, with the electrical and mechanical leads, shall characterise for each Capability Instance the peak demand and the transient demand profile, stating the maximum step change, ramp rate and repetition frequency of electrical load and heat load, measured at a resolution sufficient to resolve the transients, under representative workloads including job start, synchronous training, checkpointing and job failure. The capacity manager shall provide the characterisation to the POW and THM design owners and to the grid connection owner, and refresh it after any change in accelerator generation, workload type or power-management configuration.

**Assessment criteria**

1. Peak electrical and thermal demand per pod and hall is stated with its measurement basis.
2. The transient profile states maximum step change, ramp rate and repetition frequency for electrical and heat load.
3. Measurements were taken at a resolution sufficient to resolve the stated transients and under the representative workload set (job start, synchronous training, checkpoint, job failure).
4. The characterisation was provided to POW and THM design owners and the grid connection owner, with recorded acknowledgement.
5. The characterisation was refreshed after each change in accelerator generation, workload type or power-management configuration.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Transient measurement resolution | ms | 100 or finer | Capability-profile parameter; illustrative, must resolve the fastest step of interest |
| Maximum load step change | % of pod IT load | measured; no default | Measured characteristic, not a design default |
| Maximum ramp rate | kW per second per pod | measured; no default | Measured characteristic, not a design default |

**Minimum evidence**

- Peak and transient characterisation report
- High-resolution power-quality or meter captures for representative workloads
- Heat-load and facility water temperature transient captures from CDUs or heat meters
- Distribution records to POW, THM and grid connection owners
- Workload schedule showing representative workloads during capture

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E4; E1 |
| qualityFloor | P4 F4 C3 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; TRANSITION; RECOVERY |
| periodCoverage | Captures covering each representative workload type, taken since the last change in accelerator generation or power-management configuration |
| independence | Electrical specialist independent of the capacity manager reviews capture method and resolution |
| mandatoryItems | Peak and transient characterisation report; High-resolution power-quality or meter captures for representative workloads |
| acceptableAlternatives | OEM-provided transient profiles for the accelerator platform, only for DESIGN-stage use and with the limitation recorded |
| unknownEffect | US3 Material: POW and THM capacity and control-stability claims lack a demand basis; affected CG-05 and CG-06 evaluation records the gap |
| reassessmentTriggers | New accelerator generation; Change in power-capping or power-smoothing configuration; New workload type (for example very large synchronous training); Protection trip or UPS alarm correlated with workload steps |

**Assessment methods.** ANALYSIS, INSPECTION, DOCUMENT_REVIEW, INQUIRY

**Assessment procedure**

1. Obtain the characterisation report and check peak and transient attributes.
2. Examine raw captures and confirm resolution and workload coverage against the workload schedule.
3. Have an electrical specialist review the capture method and a mechanical specialist review heat-load transients.
4. Confirm distribution to POW, THM and grid connection owners.
5. Check refresh against change events.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to every instance running synchronous distributed training or other workloads with coordinated load changes; for inference-only instances with smoothed load the characterisation may be limited to peak and start-up steps, with rationale.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, TRANSITION, RECOVERY

**Failure modes addressed.** Synchronous training load steps cause UPS or generator instability; Grid connection ramp-rate condition breached; Upstream protection trips on restart inrush; CDU control loop hunts under rapid heat-load swings, causing temperature overshoot

**Testing safety.** Connection of power-quality analysers to live switchgear is hazardous-energy work and shall be performed only by authorised electrical personnel under the site's safe system of work and permit, with arc-flash PPE appropriate to the incident-energy study. The assessor observes; the assessor does not connect instruments. Workload scheduling for captures is arranged by the platform owner on capacity they control.

**UNKNOWN rule.** If no capture at sufficient resolution exists, record a U1 UNKNOWN; average-interval telemetry shall not be used to infer the absence of transients.

**Ontology classes.** CapacityAssertion, Resource, FailureMode, InfrastructureSystem · **Related controls.** MCF-CAP-013, MCF-CAP-017, MCF-CAP-016, MCF-GOV-017

**Informative references.** IEC 61000-4-30 (power quality measurement methods); IEC 62040-3 (UPS performance and test requirements); ASHRAE TC 9.9 liquid cooling guidelines

### MCF-CAP-015

**Growth Forecast** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Forecast demand growth for each Capability Instance (accelerator count, power per accelerator, rack density, liquid-cooled fraction, fabric scale, storage capacity and throughput) over the planning horizon so that power, cooling, space and supply-chain lead times are committed before demand arrives.

**Requirement.** The capacity manager shall maintain a growth forecast for each Capability Instance over the planning horizon stating expected accelerator deployments by generation, power per accelerator and rack, liquid-cooled fraction, fabric and storage scale, with the assumptions and their sources, an uncertainty range, and the date by which each infrastructure commitment must be made given supplier and utility lead times. The capability owner shall approve the forecast and review it against actuals at the forecast review interval.

**Assessment criteria**

1. A forecast exists per instance covering accelerators, power per rack, liquid-cooled fraction, fabric and storage over the planning horizon.
2. Assumptions are stated with sources and an uncertainty range.
3. Commitment dates are derived from stated lead times for power (including grid connection), cooling plant, and long-lead equipment.
4. The forecast is approved by the capability owner and was compared with actuals at the review interval.
5. Forecast values at the upper end of the uncertainty range are compared with site power and cooling limits.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Planning horizon | months | 36 | Capability-profile parameter; illustrative |
| Forecast review interval | months | 6 | Capability-profile parameter; illustrative |

**Minimum evidence**

- Approved growth forecast with assumptions and uncertainty
- Lead-time register for utility and long-lead equipment
- Forecast-versus-actual review records
- Comparison to site limits

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E3; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Forecast current at the assessment date and the last review against actuals |
| independence | Assessor reperforms one commitment-date derivation |
| mandatoryItems | Approved growth forecast with assumptions and uncertainty; Lead-time register for utility and long-lead equipment |
| acceptableAlternatives | Capital plan with capacity assumptions, approved by the capability owner |
| unknownEffect | US2 Moderate: confidence in forward-looking capacity claims limited to CONF-2 |
| reassessmentTriggers | Change of accelerator roadmap; Change of utility connection timeline; Forecast error beyond the uncertainty range |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, REPERFORMANCE

**Assessment procedure**

1. Review forecast coverage, assumptions and uncertainty.
2. Reperform a commitment-date derivation from lead times.
3. Compare upper-range values with site limits.
4. Review forecast-versus-actual records.

**Gate mappings.** None

**Applicability.** Applies to instances expected to grow within the planning horizon; static instances record 'no growth' as an approved forecast.

**Lifecycle stages.** PLAN, DESIGN, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Accelerators delivered before liquid cooling capacity exists; Grid connection lead time exceeds forecast need; Rack density growth exceeds floor loading or busway rating; Forecast never compared with actuals

**Testing safety.** Desk review only; forecasts are commercially sensitive and handled under restriction.

**UNKNOWN rule.** If the source of a key assumption (for example power per accelerator for an unreleased generation) cannot be identified, record a U6 UNKNOWN and widen the uncertainty range.

**Ontology classes.** CapacityAssertion, CapabilityInstance, Resource · **Related controls.** MCF-CAP-013, MCF-CAP-016, MCF-CAP-017

**Informative references.** ISO/IEC 30134 series (data centre key performance indicators); ISO 55000 series (asset management) - asset planning

### MCF-CAP-016

**Scenario Demand** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Characterise demand under adverse and recovery scenarios (simultaneous restart after power loss, checkpoint-restore storage bursts, failover of load to surviving halls, cooling recovery with high residual heat) and validate it in exercise, so that recovery does not itself overload power, cooling, fabric or storage.

**Requirement.** The capacity manager, with the resilience lead, shall model for each Capability Instance the demand on power, cooling, fabric and storage during the declared recovery and failover scenarios (including restart inrush, checkpoint-restore read bursts, re-scheduling storms and transfer of load to surviving fault domains), shall define the staging that keeps demand within supply during recovery, and shall validate the model and staging in at least one recovery exercise per exercise interval.

**Assessment criteria**

1. Recovery and failover scenarios are listed with modelled demand on power, cooling, fabric and storage.
2. Restart inrush, checkpoint-restore bursts and re-scheduling load are included where applicable.
3. A staging plan keeps modelled demand within available supply in each recovery step.
4. At least one recovery exercise in the interval measured actual demand against the model and staging.
5. Differences between measured and modelled demand were analysed and the model or staging updated.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Scenario demand exercise interval | months | 12 | Capability-profile parameter; illustrative |
| Restart staging group size | % of instance accelerators per step | 25 | Capability-profile parameter; illustrative |

**Minimum evidence**

- Scenario demand model
- Recovery staging plan
- Exercise record with measured demand
- Model-versus-measured analysis and updates

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E3; E4; E7 |
| optionalClasses | E2; E5 |
| qualityFloor | P4 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | RECOVERY; TRANSITION; DEGRADED |
| periodCoverage | Model current at the assessment date; exercise within the exercise interval |
| independence | Exercise observed by a party independent of the team that built the model |
| mandatoryItems | Scenario demand model; Recovery staging plan; Exercise record with measured demand |
| acceptableAlternatives | Measured demand from a genuine recovery event, analysed against the model, in place of an exercise |
| unknownEffect | US3 Material: recovery staging unvalidated; CG-10 evaluation records the gap; decision condition recorded |
| reassessmentTriggers | Change of recovery architecture or checkpoint strategy; Expansion of instance; Recovery event with demand exceeding model |

**Assessment methods.** ANALYSIS, SCENARIO_EXERCISE, DOCUMENT_REVIEW, OBSERVATION

**Assessment procedure**

1. Review the scenario list and modelled demand by domain.
2. Check staging plan against available supply per step.
3. Examine the exercise record and measured demand; observe an exercise if one is scheduled.
4. Compare measured with modelled demand and review the resulting updates.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies to instances whose recovery outcomes require restoration of more than one fault domain or of large accelerator populations; small single-rack instances may record NOT_APPLICABLE with rationale.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** RECOVERY, TRANSITION, DEGRADED

**Failure modes addressed.** Simultaneous restart of all racks trips upstream breakers; Checkpoint restore saturates the storage system and extends RTO; Failover of load to a surviving hall exceeds its cooling capacity; Scheduler re-queue storm overloads the control plane

**Testing safety.** Recovery exercises that energise or de-energise equipment, restart cooling plant or perform restart of accelerator populations are hazardous-energy and service-affecting activities: they require written authorisation from the capability owner and facility operator, a method statement with abort criteria and initial-state verification, permits under the site safe system of work, and the safety authority's right to stop. Assessors observe and do not operate equipment.

**UNKNOWN rule.** If no exercise has measured recovery demand, the RESILIENCE claim is UNKNOWN (U1); the model alone supports only a DESIGN-level statement.

**Ontology classes.** FailureScenario, CapacityAssertion, OperatingState, TestRecord · **Related controls.** MCF-CAP-008, MCF-CAP-014, MCF-CAP-019, MCF-CAP-020

**Informative references.** ISO 22301 (business continuity management systems) - exercising and testing; ISO 22398 (guidelines for exercises); IEC 62040-3 (UPS performance and test requirements)

## CAP-05 Operating envelope

### MCF-CAP-017

**Load Envelope** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Define and enforce the electrical and thermal load envelope of each Capability Instance (maximum IT load per rack, row, pod and hall; maximum liquid heat load per CDU loop; power per accelerator) and ensure mechanisms prevent load from exceeding it.

**Requirement.** The capability architect shall define, for each Capability Instance, the load envelope: maximum IT power per rack, row, pod and hall, maximum heat load per CDU or liquid loop, and permitted power per accelerator, each derived from the lowest-rated element in the power and cooling path in the declared redundancy state. The AI platform owner and facility operator shall implement enforcement (power capping, admission control for new racks or jobs, alarm thresholds) and shall verify that configured limits equal the envelope.

**Assessment criteria**

1. The envelope states rack, row, pod, hall and CDU loop limits and power per accelerator.
2. Each limit is derived from the lowest-rated element in its path in the declared redundancy state, with the derivation recorded.
3. Enforcement mechanisms (power capping, admission control, alarm thresholds) are configured at or below the envelope.
4. Configured limits reconcile to the envelope for a sample of racks, pods and loops.
5. Envelope exceedances in the period, if any, were alarmed and actioned.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Design margin below lowest-rated element | % of rating | 10 | Capability-profile parameter; illustrative |

**Minimum evidence**

- Load envelope definition with derivations
- Power-capping and admission-control configuration export
- BMS/EPMS alarm threshold configuration
- Exceedance alarm and action records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E7 |
| qualityFloor | P3 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | Configuration current at the assessment date and exceedances in the preceding twelve months |
| independence | Configuration exports taken from source systems under assessor observation |
| mandatoryItems | Load envelope definition with derivations; Power-capping and admission-control configuration export; BMS/EPMS alarm threshold configuration |
| acceptableAlternatives | Where enforcement is procedural, deployment approval records showing envelope checks before each rack installation |
| unknownEffect | US3 Material: overload protection of power and cooling paths unverified; decision condition recorded |
| reassessmentTriggers | New accelerator generation; Change in redundancy state; Rating change of any path element; Exceedance event |

**Assessment methods.** RECONCILIATION, INSPECTION, ANALYSIS, DOCUMENT_REVIEW

**Assessment procedure**

1. Review envelope limits and derivations against path element ratings.
2. Export enforcement configurations and alarm thresholds.
3. Reconcile a sample of configured limits to the envelope.
4. Review exceedance alarms and actions in the period.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to every in-service Capability Instance.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Rack load exceeds busway or PDU rating; CDU loop heat load exceeds capacity in N state after a pump failure; Power capping disabled for a benchmark and not restored; New racks deployed without envelope check

**Testing safety.** Read-only configuration export; capping and admission control are not tested by overloading equipment.

**UNKNOWN rule.** If the rating of a path element cannot be established, record a U1 UNKNOWN against the derived limit and treat the envelope for that path as unverified.

**Ontology classes.** CapacityAssertion, Safeguard, InfrastructureSystem · **Related controls.** MCF-CAP-013, MCF-CAP-014, MCF-CAP-018, MCF-CAP-020

**Informative references.** IEC 60364 series (low-voltage electrical installations); ASHRAE TC 9.9 liquid cooling guidelines; ISO/IEC 22237 series (data centre facilities and infrastructures)

### MCF-CAP-018

**Environmental Envelope** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Define the environmental envelope the AI equipment requires (air inlet temperature and humidity, facility water and technology cooling system supply temperature, flow and pressure, coolant quality) by reference to OEM specifications and recognised thermal guidelines, and ensure setpoints and alarms enforce it.

**Requirement.** The capability architect shall define, for each Capability Instance, the environmental envelope covering air inlet temperature and humidity, technology cooling system and facility water supply temperature, minimum flow and differential pressure, and coolant quality, derived from accelerator and server OEM specifications and the applicable ASHRAE TC 9.9 classes. The facility operator shall configure BMS and CDU setpoints and alarm thresholds within the envelope and shall reconcile them to the envelope after every OEM specification revision.

**Assessment criteria**

1. The envelope covers air temperature and humidity, liquid supply temperature, flow, differential pressure and coolant quality.
2. Each envelope value cites the OEM specification or ASHRAE TC 9.9 class from which it is derived.
3. BMS and CDU setpoints and alarm thresholds for a sample of zones and loops lie within the envelope.
4. Setpoints were reconciled after each OEM specification revision in the period.
5. Where OEM limits differ across equipment sharing a loop, the most restrictive limit is applied.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Air inlet temperature range | degC | 18-27 | ASHRAE TC 9.9 recommended envelope for air-cooled IT; OEM limits prevail where stricter |
| Technology cooling system supply temperature upper limit | degC | per OEM specification | OEM specification; no generic default |

**Minimum evidence**

- Environmental envelope definition with sources
- OEM specification extracts
- BMS and CDU setpoint and alarm configuration export
- Reconciliation records after OEM revisions

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3 |
| qualityFloor | P3 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | Configuration current at the assessment date |
| independence | Mechanical specialist verifies envelope derivation; configuration exported under assessor observation |
| mandatoryItems | Environmental envelope definition with sources; BMS and CDU setpoint and alarm configuration export |
| acceptableAlternatives | Commissioning records of setpoints, where no change has occurred since commissioning and change records confirm this |
| unknownEffect | US3 Material: thermal protection of equipment unverified; CG-06 evaluation records the gap |
| reassessmentTriggers | OEM specification revision; New equipment sharing a loop; Change of BMS or CDU setpoints; Thermal throttling or over-temperature event |

**Assessment methods.** RECONCILIATION, INSPECTION, DOCUMENT_REVIEW

**Assessment procedure**

1. Review envelope values and their sources.
2. Export BMS and CDU setpoints and alarm thresholds.
3. Reconcile a sample of zones and loops to the envelope, applying the most restrictive OEM limit.
4. Check reconciliation after OEM revisions.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to every in-service Capability Instance; liquid-cooling criteria apply where liquid cooling is used.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Facility water supply temperature raised for efficiency beyond accelerator OEM limits; Flow alarm threshold below OEM minimum; Mixed-generation loop set to the less restrictive limit; Humidity outside envelope causing condensation risk on cold plates

**Testing safety.** Read-only export of BMS and CDU configuration; no setpoint is changed during assessment.

**UNKNOWN rule.** If an OEM specification is unavailable for installed equipment, record a U1 UNKNOWN against the affected envelope value; a generic guideline value shall not be substituted without approval.

**Ontology classes.** OperatingState, Safeguard, InfrastructureSystem · **Related controls.** MCF-CAP-017, MCF-CAP-019, MCF-CAP-006

**Informative references.** ASHRAE TC 9.9 thermal guidelines for data processing environments; ASHRAE TC 9.9 liquid cooling guidelines; ISO/IEC 22237 series (data centre facilities and infrastructures) - environmental control

### MCF-CAP-019

**Duration Limits** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Establish and validate how long each Capability Instance can sustain its outcomes in each degraded condition (UPS autonomy at actual load, thermal ride-through of liquid loops and rooms on loss of cooling, fuel autonomy, time on reduced redundancy) so that response and recovery actions are timed within real limits.

**Requirement.** The capability architect shall state, for each Capability Instance, duration limits for each declared degraded condition: battery autonomy at measured load, thermal ride-through time before equipment limits are reached on loss of chilled or facility water, generator fuel autonomy, and maximum time on reduced redundancy. The facility operator shall validate each limit by test, measurement or validated model at the duration validation interval and after material change, and shall align alarms and runbooks to the validated limits.

**Assessment criteria**

1. Duration limits are stated for each declared degraded condition, including UPS autonomy, thermal ride-through, fuel autonomy and reduced-redundancy time.
2. Each limit is validated by test, measured event or validated model at current load.
3. Thermal ride-through validation accounts for the actual liquid-cooled heat load and thermal mass of the loops.
4. Alarms and runbooks trigger actions with sufficient margin before each validated limit.
5. Validation is within the interval and after material change.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Duration validation interval | months | 12 | Capability-profile parameter; illustrative |
| Thermal ride-through on loss of facility water | minutes | validated value; no default | Validated characteristic, not a design default |
| Response margin before limit | % of validated duration | 50 | Capability-profile parameter; illustrative |

**Minimum evidence**

- Duration limit statement
- UPS autonomy test or discharge record at measured load
- Thermal ride-through test, event record or validated model
- Fuel autonomy calculation with measured consumption
- Alarm and runbook timing extracts

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E1; E5; E7 |
| qualityFloor | P4 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | DEGRADED; EMERGENCY; MAINTENANCE |
| periodCoverage | Validations within the duration validation interval at current load |
| independence | Test witnessed by a party independent of the facility operator or by an electrical/mechanical specialist assessor |
| mandatoryItems | Duration limit statement; UPS autonomy test or discharge record at measured load; Thermal ride-through test, event record or validated model |
| acceptableAlternatives | Validated computational model calibrated against a measured event, for thermal ride-through where a test is not safe |
| unknownEffect | US3 Material: response timing unsupported; CG-05, CG-06 and CG-10 evaluations record the gap; decision condition recorded |
| reassessmentTriggers | Load increase beyond the validated level; Battery replacement or ageing alarms; Cooling topology change; Event where a limit was approached or exceeded |

**Assessment methods.** TEST, ANALYSIS, DOCUMENT_REVIEW, OBSERVATION

**Assessment procedure**

1. Review stated limits for completeness across degraded conditions.
2. Examine validation evidence for each limit and its load basis.
3. Have a mechanical specialist review thermal ride-through validation against liquid heat load and loop thermal mass.
4. Compare alarm and runbook timings with validated limits and margin.
5. Observe a scheduled validation test where one occurs in the assessment window.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to every in-service instance; fuel autonomy is not applicable where no on-site generation exists, with rationale.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** DEGRADED, EMERGENCY, MAINTENANCE

**Failure modes addressed.** UPS autonomy at today's AI load is a fraction of the design value; Liquid-cooled racks exceed thermal limits within seconds of facility water loss, faster than runbook response; Fuel autonomy calculated from nameplate consumption; Extended operation on N redundancy unnoticed

**Testing safety.** UPS discharge and cooling-interruption tests are hazardous and service-affecting: they require written authorisation from the facility operator and capability owner, an engineered method statement with initial-state verification, abort criteria and restoration steps, load banks or protected test loads where possible, permits under the site safe system of work, and a safety authority able to stop the test. Thermal ride-through on production accelerators shall not be tested by deliberately stopping cooling; a calibrated model or measured event is used instead.

**UNKNOWN rule.** If a limit has never been validated at current load, record a U3 (stale) or U1 UNKNOWN; design values shall not be presented as validated.

**Ontology classes.** OperatingState, CapacityAssertion, TestRecord, Safeguard · **Related controls.** MCF-CAP-016, MCF-CAP-018, MCF-CAP-020, MCF-CAP-010

**Informative references.** IEC 62040-3 (UPS performance and test requirements); IEEE 1188 (maintenance and testing of VRLA batteries); ISO 8528 series (reciprocating engine generating sets); ASHRAE TC 9.9 liquid cooling guidelines

### MCF-CAP-020

**State-Specific Limits** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Define and enforce limits that apply only in non-normal operating states (maintenance with reduced redundancy, degraded cooling, emergency, recovery, transition) so that permitted load, activities and changes are restricted when margins are smaller.

**Requirement.** The capability architect shall define for each Capability Instance the limits applying in each non-normal operating state, including maximum permitted IT load, prohibited activities (for example concurrent maintenance on both power paths, firmware rollouts, large job starts), required approvals and maximum duration. The facility operator and AI platform owner shall implement these limits in maintenance permits, change freezes, scheduler policies and power-capping profiles, and shall record state entry and exit.

**Assessment criteria**

1. State-specific limits are defined for MAINTENANCE, DEGRADED, EMERGENCY, RECOVERY and TRANSITION states.
2. Limits include permitted load, prohibited activities, approvals and maximum duration.
3. Maintenance permits, change freezes, scheduler policies and capping profiles implement the limits.
4. State entry and exit events in the period are recorded.
5. For a sample of non-normal state periods, telemetry and change records show the limits were respected.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum IT load in reduced-redundancy maintenance | % of normal envelope | per redundancy study; no default | Derived from POW/THM redundancy studies |

**Minimum evidence**

- State-specific limit definitions
- Maintenance permits and change freeze records
- Scheduler and capping profile configuration for non-normal states
- State entry/exit log
- Telemetry and change records for sampled state periods

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | MAINTENANCE; DEGRADED; EMERGENCY; RECOVERY; TRANSITION |
| periodCoverage | Non-normal state periods in the twelve months preceding the assessment |
| independence | Assessor samples state periods from the log and obtains telemetry independently |
| mandatoryItems | State-specific limit definitions; State entry/exit log; Telemetry and change records for sampled state periods |
| acceptableAlternatives | Maintenance window records with associated telemetry where no formal state log exists, with limitation recorded |
| unknownEffect | US3 Material: containment in non-normal states unverified; CG-09 evaluation records the gap |
| reassessmentTriggers | New maintenance regime; Incident during a non-normal state; Redundancy topology change |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, ANALYSIS, RECONCILIATION

**Assessment procedure**

1. Review limit definitions for each non-normal state.
2. Inspect implementation in permits, freezes, scheduler policies and capping profiles.
3. Sample non-normal state periods from the log.
4. Analyse telemetry and change records for each sampled period against the limits.

**Gate mappings.** CG-09 Failure containment (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to every in-service instance.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** MAINTENANCE, DEGRADED, EMERGENCY, RECOVERY, TRANSITION

**Failure modes addressed.** Full AI load run during maintenance on one power path, so a second fault drops the hall; Firmware rollout during degraded cooling; Large job start during recovery overloads restored supply; Maintenance state left open beyond its duration

**Testing safety.** Record and telemetry review only; no state transition is induced.

**UNKNOWN rule.** If state entry and exit cannot be reconstructed for a period, record a U5 UNKNOWN for that period.

**Ontology classes.** OperatingState, Safeguard, FaultDomain · **Related controls.** MCF-CAP-017, MCF-CAP-019, MCF-CAP-012, MCF-CAP-016

**Informative references.** ISO/IEC 22237 series (data centre facilities and infrastructures) - operational information; ISO/IEC 20000-1 (service management system) - change management

## CAP-06 Capability lifecycle and change

### MCF-CAP-021

**Design-to-Operation Traceability** · DETECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that design intent (Service Outcomes, envelopes, redundancy, fault domains) is traceable through build and commissioning into the operating configuration, so that differences between designed, installed, commissioned and operated states are visible.

**Requirement.** The capability architect shall maintain traceability from each Service Outcome and envelope to design requirements, to as-built records, to commissioning results and to the current operating configuration for each Capability Instance, recording deviations at each stage with disposition. The facility operator and AI platform owner shall provide current configuration evidence for reconciliation at the traceability reconciliation interval.

**Assessment criteria**

1. Traceability links exist from Service Outcomes and envelopes to design requirements, as-built records, commissioning results and operating configuration.
2. Deviations at each stage are recorded with disposition.
3. A sample traced end to end shows no undisclosed deviation between design and operating configuration.
4. Reconciliation to current configuration is within the interval.
5. Designed, installed, commissioned and operated states are recorded distinctly, not overwritten.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Traceability reconciliation interval | months | 12 | Capability-profile parameter; illustrative |

**Minimum evidence**

- Traceability matrix or graph extract
- Design requirement records
- As-built records
- Commissioning results
- Current configuration exports
- Deviation register

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E4 |
| optionalClasses | E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Current configuration and the most recent design and commissioning baseline |
| independence | Assessor selects trace samples and obtains configuration independently |
| mandatoryItems | Traceability matrix or graph extract; Current configuration exports; Deviation register |
| acceptableAlternatives | Per-system design basis and commissioning dossiers linked by system identifier |
| unknownEffect | US3 Material: IMPLEMENTATION claims in infrastructure domains qualified; CG-02 evaluation records the gap |
| reassessmentTriggers | Material change; Discovery of undisclosed deviation; New design baseline |

**Assessment methods.** RECONCILIATION, SAMPLING, DOCUMENT_REVIEW, INSPECTION

**Assessment procedure**

1. Obtain the traceability matrix or graph extract.
2. Select samples across domains and trace each from outcome to operating configuration.
3. Compare deviations found with the deviation register.
4. Confirm states are recorded distinctly and reconciliation is within interval.

**Gate mappings.** CG-02 Boundary and architecture integrity (SUPPORTING)

**Applicability.** Applies to every instance assessed at AL3 or above.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Redundancy designed as 2N but operated as N+1 after an undocumented change; As-built CDU configuration differs from design; Commissioning results overwritten by later configuration; Design envelope not carried into operating limits

**Testing safety.** Read-only configuration exports; site inspection under escort without operating equipment.

**UNKNOWN rule.** If any stage record (design, as-built, commissioning) is missing for a sampled trace, record a U1 UNKNOWN for that stage and do not infer it from the adjacent stage.

**Ontology classes.** ArchitectureSnapshot, ServiceOutcome, InfrastructureSystem, TestRecord · **Related controls.** MCF-CAP-004, MCF-CAP-022, MCF-GOV-010

**Informative references.** ISO/IEC/IEEE 15288 (system life cycle processes); ISO/IEC/IEEE 42010 (architecture description); ASHRAE Guideline 0 (the commissioning process)

### MCF-CAP-022

**Commissioning Acceptance** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure that a Capability Instance, or an expansion of it, is accepted into service only after integrated commissioning demonstrates that the combined power, cooling, control, compute, storage and network systems deliver the Service Outcomes under normal and declared degraded conditions.

**Requirement.** The commissioning manager shall plan and execute integrated systems testing for each new or expanded Capability Instance that exercises power, cooling, control systems, compute, storage and fabric together at representative load, including declared failure transfers (for example loss of a UPS module, CDU pump failover, loss of a fabric link) and their effect on Service Outcomes. The capability owner shall sign acceptance only when acceptance criteria tied to Service Outcomes are met or deviations are dispositioned, and shall record the accepted configuration baseline.

**Assessment criteria**

1. An integrated test plan exists with acceptance criteria traced to Service Outcomes and envelopes.
2. Tests were executed at representative load, including heat load to liquid loops where liquid cooled.
3. Declared failure transfers were exercised and their effect on Service Outcomes measured.
4. Every failed or deferred test has a disposition approved by the capability owner before acceptance.
5. Acceptance was signed by the capability owner and the accepted configuration baseline recorded.
6. Commissioning results are retained as E4 evidence with test conditions and anomalies.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Commissioning test load | % of design IT load | 100 | Capability-profile parameter; illustrative, using load banks or representative workloads |

**Minimum evidence**

- Integrated test plan with acceptance criteria
- Executed test scripts with results, conditions and anomalies
- Failure-transfer test records
- Deviation dispositions
- Signed acceptance and accepted configuration baseline

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5 |
| qualityFloor | P4 F4 C4 R4 T3 I4 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; TRANSITION |
| periodCoverage | Commissioning of the current configuration or the latest expansion |
| independence | Commissioning witnessed by a commissioning authority independent of the installing contractor |
| mandatoryItems | Integrated test plan with acceptance criteria; Executed test scripts with results, conditions and anomalies; Failure-transfer test records; Signed acceptance and accepted configuration baseline |
| acceptableAlternatives | For an expansion of an accepted instance, a delta integrated test covering affected systems plus regression on shared systems |
| unknownEffect | US3 Material: operating outcomes rest on unaccepted configuration; CG-02 and CG-08 evaluations record the gap |
| reassessmentTriggers | Expansion or major reconfiguration; Deferred commissioning tests outstanding; Failure in service of a function accepted at commissioning |

**Assessment methods.** DOCUMENT_REVIEW, TEST, OBSERVATION, RECONCILIATION

**Assessment procedure**

1. Review the test plan and trace acceptance criteria to Service Outcomes.
2. Examine executed scripts for load, conditions and anomalies.
3. Examine failure-transfer tests and measured outcome effects.
4. Review deviation dispositions and acceptance signature.
5. Reconcile accepted baseline to current configuration; observe commissioning if in progress.

**Gate mappings.** CG-02 Boundary and architecture integrity (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to every new Capability Instance and every expansion or major reconfiguration; for capability in a colocation facility, facility-level commissioning by the provider is assessed through MCF-SUP controls and integrated testing remains required at the capability boundary.

**Lifecycle stages.** COMMISSION, CHANGE · **Operating states.** NORMAL, DEGRADED, TRANSITION

**Failure modes addressed.** Systems commissioned individually but never together under heat load; CDU failover untested at full liquid load; Acceptance signed with open critical tests; Accepted baseline not recorded, so later drift is undetectable

**Testing safety.** Integrated systems tests involve energised switching, load banks, pressurised liquid loops and induced failures: they require an approved commissioning method statement, initial-state verification, abort criteria, isolation and permits under the site safe system of work, competent operators, and a safety authority with stop authority. Assessors observe from a designated position and do not operate equipment.

**UNKNOWN rule.** If test records lack conditions (load, state, configuration), record a U8 UNKNOWN against the affected test; the result shall not be used as effectiveness evidence.

**Ontology classes.** TestRecord, CapabilityInstance, ArchitectureSnapshot, ServiceOutcome · **Related controls.** MCF-CAP-021, MCF-CAP-003, MCF-CAP-023

**Informative references.** ASHRAE Guideline 0 (the commissioning process); ASHRAE Standard 202 (commissioning process for buildings and systems); ISO/IEC 22237 series (data centre facilities and infrastructures); IEC 62040-3 (UPS performance and test requirements)

### MCF-CAP-023

**Material Change Impact** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that every proposed change that could affect a Capability Instance's Service Outcomes, envelopes, fault domains or dependencies (accelerator refresh, density increase, cooling conversion, fabric expansion, provider change) is assessed for capability impact, validated after implementation and used to trigger reassessment.

**Requirement.** The capability owner shall ensure that every change classified as material for a Capability Instance has a capability impact assessment before approval that identifies affected Service Outcomes, envelopes, fault domains, dependencies, controls, gates and evidence; defines post-change validation; and identifies assurance claims to be suspended or reassessed. The change authority shall not approve a material change without the impact assessment, and the capability owner shall confirm post-change validation before the change is closed.

**Assessment criteria**

1. Materiality criteria for capability changes are defined and applied to every change in the period.
2. Every material change in the sample had a capability impact assessment before approval identifying outcomes, envelopes, fault domains, dependencies, controls, gates and evidence.
3. Every material change in the sample had post-change validation confirmed by the capability owner before closure.
4. Assurance claims identified as affected were suspended or scheduled for reassessment.
5. A sample of changes classified non-material shows no misclassification.

**Minimum evidence**

- Change materiality criteria
- Change log for the period with materiality classification
- Capability impact assessments for sampled material changes
- Post-change validation records
- Reassessment or suspension records triggered

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E7 |
| qualityFloor | P3 F4 C4 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; TRANSITION; MAINTENANCE |
| periodCoverage | All changes in the twelve months preceding the assessment |
| independence | Assessor selects samples of both material and non-material changes from the full change log |
| mandatoryItems | Change log for the period with materiality classification; Capability impact assessments for sampled material changes; Post-change validation records |
| acceptableAlternatives | Programme-level impact assessment for a coordinated set of changes, if each change references it |
| unknownEffect | US4 Critical: CG-14 Gate Result UNKNOWN; decision capped at LIMITED |
| reassessmentTriggers | Change of materiality criteria; Material change implemented without assessment; Post-change incident |

**Assessment methods.** SAMPLING, DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Review materiality criteria and their application across the change log.
2. Sample material changes and verify impact assessments preceded approval.
3. Verify post-change validation before closure.
4. Trace affected claims to suspension or reassessment records.
5. Sample non-material changes and test classification.

**Gate mappings.** CG-14 Change control (CRITICAL); CG-01 Capability and outcome definition (SUPPORTING)

**Applicability.** Applies to every change affecting an in-scope Capability Instance, whether initiated by the owner, operator or a provider.

**Lifecycle stages.** CHANGE, OPERATE · **Operating states.** NORMAL, TRANSITION, MAINTENANCE

**Failure modes addressed.** Accelerator refresh raises rack power beyond the cooling envelope without assessment; Conversion from air to liquid cooling not treated as material; Provider changes a shared dependency without notification; Change closed without validation; Prior assurance relied on after material change

**Testing safety.** Record review only; post-change validation tests are assessed under the relevant domain controls with their own safety requirements.

**UNKNOWN rule.** If changes made by providers cannot be enumerated, record a U10 UNKNOWN (dependency unknown) against the provider's changes and treat CG-14 as UNKNOWN for affected dependencies.

**Ontology classes.** Event, ReassessmentTrigger, CapabilityInstance, Action · **Related controls.** MCF-EVA-022, MCF-GOV-011, MCF-CAP-022, MCF-CAP-024

**Informative references.** ISO/IEC 20000-1 (service management system) - change management; ISO/IEC/IEEE 15288 (system life cycle processes); ISO 55000 series (asset management)

### MCF-CAP-024

**Retirement Control** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that retiring all or part of a Capability Instance (decommissioning racks, draining liquid loops, removing storage, ending a provider service) is controlled so that remaining outcomes, data protection and safety are not compromised and records are updated.

**Requirement.** The capability owner shall approve a retirement plan for each retirement of capability or infrastructure that identifies remaining Service Outcomes affected, dependencies to be removed or transferred, data sanitisation of storage media and accelerator memory, safe isolation and draining of liquid loops and disposal of batteries and coolant, and updates to the capability register, architecture snapshot and assurance graph. The facility operator shall confirm completion of each step with evidence.

**Assessment criteria**

1. Each retirement in the period had an approved plan covering affected outcomes, dependencies, data sanitisation, safe isolation and disposal, and record updates.
2. Data sanitisation of retired storage media is evidenced to the required sanitisation level.
3. Liquid loops were isolated and drained, and batteries and coolant disposed of under safe-work and environmental requirements.
4. Capability register, architecture snapshot and assurance graph were updated within the record update time.
5. Remaining Service Outcomes were verified after retirement.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Record update time after retirement | working days | 10 | Capability-profile parameter; illustrative |

**Minimum evidence**

- Approved retirement plans
- Data sanitisation certificates or records
- Isolation, draining and disposal records
- Register, snapshot and graph update records
- Post-retirement outcome verification

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | SHUTDOWN; TRANSITION |
| periodCoverage | Retirements completed in the twelve months preceding the assessment |
| independence | Sanitisation evidence from the performing party verified against asset serial numbers by the assessor |
| mandatoryItems | Approved retirement plans; Data sanitisation certificates or records; Register, snapshot and graph update records |
| acceptableAlternatives | Physical destruction certificates for media where sanitisation was by destruction |
| unknownEffect | US3 Material: residual data exposure or stale architecture records; decision condition recorded |
| reassessmentTriggers | Retirement of an entire instance; Provider service termination; Media found outside sanitisation process |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, SAMPLING, INSPECTION

**Assessment procedure**

1. List retirements in the period and obtain plans.
2. Reconcile sanitisation records to retired asset serial numbers.
3. Review isolation, draining and disposal records.
4. Verify record updates and post-retirement outcome verification.

**Gate mappings.** CG-14 Change control (SUPPORTING); CG-02 Boundary and architecture integrity (SUPPORTING); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies whenever capability or infrastructure supporting an in-scope instance is retired; not applicable in a period with no retirements.

**Lifecycle stages.** DECOMMISSION, CHANGE · **Operating states.** SHUTDOWN, TRANSITION

**Failure modes addressed.** Storage media containing model weights leave site unsanitised; Shared loop drained while still serving adjacent racks; Retired equipment remains in the architecture snapshot; Removal of a shared PDU drops a remaining rack

**Testing safety.** Isolation and draining of liquid loops and removal of batteries are hazardous activities performed only by authorised personnel under permit and lock-out/tag-out; the assessor reviews records and, if observing, does so from a safe position without handling equipment or fluids.

**UNKNOWN rule.** If sanitisation evidence cannot be matched to an asset serial number, record a U6 UNKNOWN for that asset and report it as a potential data exposure.

**Ontology classes.** AssetInstance, CapabilityInstance, ArchitectureSnapshot, Event · **Related controls.** MCF-CAP-023, MCF-CAP-001, MCF-CAP-004

**Informative references.** NIST SP 800-88 (guidelines for media sanitization); IEEE 2883 (standard for sanitizing storage); ISO/IEC 27040 (storage security)
