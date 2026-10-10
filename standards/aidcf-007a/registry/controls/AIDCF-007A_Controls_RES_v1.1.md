# AIDCF-007A Control Catalogue — RES Resilience, Continuity and Recovery

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-RES](../../../aidcf-018-domain-guides/AIDCF-018-RES_Resilience_Continuity_and_Recovery_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-RES-001](#mcf-res-001) | Minimum Service Outcome | DIRECTIVE | DESIGN | AL2 | — | CG-01, CG-10, CG-09 |
| [MCF-RES-002](#mcf-res-002) | Graceful Degradation | CORRECTIVE | EFFECTIVENESS | AL5 | — | CG-09, CG-10 |
| [MCF-RES-003](#mcf-res-003) | Resilience Scenarios | DIRECTIVE | DESIGN | AL2 | — | CG-09, CG-10, CG-03 |
| [MCF-RES-004](#mcf-res-004) | Resilience Ownership | DIRECTIVE | DESIGN | AL2 | — | CG-13 |
| [MCF-RES-005](#mcf-res-005) | Fault-Domain Definition | PREVENTIVE | IMPLEMENTATION | AL3 | CG-09 | CG-03, CG-02 |
| [MCF-RES-006](#mcf-res-006) | Containment Boundaries | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-09 |
| [MCF-RES-007](#mcf-res-007) | Blast Radius | PREVENTIVE | IMPLEMENTATION | AL3 | CG-09 | CG-03 |
| [MCF-RES-008](#mcf-res-008) | Isolation Validation | DETECTIVE | RESILIENCE | AL5 | CG-09 | CG-04 |
| [MCF-RES-009](#mcf-res-009) | Continuity Strategy | DIRECTIVE | DESIGN | AL2 | — | CG-10, CG-01 |
| [MCF-RES-010](#mcf-res-010) | Alternative Capacity | RECOVERY | EFFECTIVENESS | AL5 | — | CG-10, CG-03 |
| [MCF-RES-011](#mcf-res-011) | Site and Provider Continuity | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-03, CG-10 |
| [MCF-RES-012](#mcf-res-012) | Crisis Priorities | DIRECTIVE | DESIGN | AL2 | — | CG-10, CG-01 |
| [MCF-RES-013](#mcf-res-013) | Recovery Dependencies | RECOVERY | IMPLEMENTATION | AL3 | CG-10 | CG-03 |
| [MCF-RES-014](#mcf-res-014) | Recovery Sequencing | RECOVERY | RESILIENCE | AL5 | CG-10 | CG-05, CG-06 |
| [MCF-RES-015](#mcf-res-015) | Configuration Restoration | RECOVERY | EFFECTIVENESS | AL5 | — | CG-10, CG-07, CG-14 |
| [MCF-RES-016](#mcf-res-016) | Data and Checkpoint Recovery | RECOVERY | RESILIENCE | AL5 | CG-10 | CG-08 |
| [MCF-RES-017](#mcf-res-017) | Component Tests | DETECTIVE | OPERATION | AL4 | — | CG-10, CG-05, CG-06 |
| [MCF-RES-018](#mcf-res-018) | Integrated Scenario Tests | DETECTIVE | RESILIENCE | AL5 | CG-10 | CG-09, CG-05, CG-06 |
| [MCF-RES-019](#mcf-res-019) | Tabletop Exercises | DETECTIVE | OPERATION | AL4 | — | CG-10, CG-13 |
| [MCF-RES-020](#mcf-res-020) | Lessons and Retest | CORRECTIVE | OPERATION | AL4 | — | CG-10, CG-14 |
| [MCF-RES-021](#mcf-res-021) | Crisis Command | CORRECTIVE | EFFECTIVENESS | AL5 | — | CG-13, CG-10 |
| [MCF-RES-022](#mcf-res-022) | Stakeholder Communications | CORRECTIVE | OPERATION | AL4 | — | CG-13 |
| [MCF-RES-023](#mcf-res-023) | Emergency Change | CORRECTIVE | OPERATION | AL4 | — | CG-14 |
| [MCF-RES-024](#mcf-res-024) | Post-Event Adaptation | CORRECTIVE | OPERATION | AL4 | — | CG-14 |

## RES-01 Resilience strategy

### MCF-RES-001

**Minimum Service Outcome** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure every in-scope Capability Instance has a defined minimum service outcome and impact tolerance (maximum tolerable disruption, minimum capacity, maximum lost work, maximum data loss) that resilience design, testing and recovery claims can be measured against.

**Requirement.** The capability owner shall define and approve, for each in-scope Capability Instance, the minimum service outcome to be sustained under DEGRADED and EMERGENCY states and the impact tolerance, expressed as maximum tolerable duration of disruption, minimum retained capacity (for example accelerator-hours or tokens per second), maximum tolerable lost training progress, recovery time and recovery point objectives, and the business-impact basis for each. The resilience owner shall ensure every RES-02 to RES-05 control and every NET, POW, THM, CMP and STO recovery claim references these tolerances.

**Assessment criteria**

1. Each in-scope Capability Instance has an approved minimum service outcome and impact tolerance with measurable units.
2. Tolerances are derived from a business-impact analysis that considers customers, contractual commitments and dependent services.
3. RTO and RPO (or maximum lost work) are stated and consistent with each other and with checkpoint strategy (RES-016).
4. Minimum outcomes are stated per declared operating state (NORMAL, DEGRADED, EMERGENCY, RECOVERY).
5. Resilience and recovery controls reference the tolerances explicitly.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum tolerable disruption (training outcome) | h | Business-impact derived (illustrative 24) | ISO/TS 22317-style impact analysis; capability-specific. |
| Maximum tolerable disruption (inference outcome) | min | Business-impact derived (illustrative 15) | Capability-specific. |
| Maximum lost training progress | h of cluster time | Equal to checkpoint interval plus restart time (illustrative 2) | Links to RES-016. |
| Minimum retained capacity in DEGRADED state | % of nominal | 50 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Approved minimum service outcome and impact tolerance statement per Capability Instance
- Business-impact analysis
- Mapping of tolerances to resilience and recovery controls

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C2 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY; RECOVERY |
| periodCoverage | Current approved version, reviewed within 12 months (illustrative). |
| independence | Approved by the capability owner and reviewed by the resilience owner; author distinct from approver. |
| mandatoryItems | Approved tolerance statement; Business-impact analysis |
| acceptableAlternatives | Contractual service levels where they fully express the tolerances, with the business-impact rationale recorded |
| unknownEffect | US5: undefined tolerances affect every resilience and recovery gate (CG-09, CG-10); decision ≤ INCONCLUSIVE. |
| reassessmentTriggers | New Capability Instance; New customer commitment; Change in workload criticality; Regulatory change |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY, ANALYSIS

**Assessment procedure**

1. Obtain the tolerance statement for each Capability Instance and confirm approval.
2. Review the business-impact analysis and trace each tolerance to it.
3. Check internal consistency of RTO, RPO, lost-work and checkpoint strategy.
4. Confirm state-specific minimum outcomes are defined.
5. Sample resilience and recovery controls to confirm they reference tolerances.

**Gate mappings.** CG-01 Capability and outcome definition (SUPPORTING); CG-10 Recovery readiness (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to every in-scope Capability Instance. Service Outcomes themselves are defined under CAP-02; this control defines the resilience minimum and tolerance.

**Lifecycle stages.** PLAN, DESIGN, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY, RECOVERY

**Failure modes addressed.** Recovery tested against no defined objective; RPO inconsistent with checkpoint interval; Tolerances set without business basis; DEGRADED state with no defined minimum

**Testing safety.** Document-based; no operational testing.

**UNKNOWN rule.** Where any in-scope Capability Instance lacks an approved tolerance, record a US5 UNKNOWN and do not assess recovery or containment controls as CONFORMING against an assumed tolerance.

**Ontology classes.** ServiceOutcome, CapabilityInstance, OperatingState, CapacityAssertion · **Related controls.** MCF-CAP-008, MCF-CAP-010, MCF-RES-002, MCF-RES-016, MCF-RES-012

**Informative references.** ISO 22301 (Business continuity management systems: requirements); ISO/TS 22317 (Business impact analysis guidelines); UK PRA/FCA operational resilience policy (important business services and impact tolerances); Regulation (EU) 2022/2554 (Digital Operational Resilience Act)

### MCF-RES-002

**Graceful Degradation** · CORRECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure that partial loss of power, cooling, compute, storage or network capacity results in planned, controlled reduction of AI service (load shedding, job preemption, throttling, reduced replicas) rather than uncontrolled failure.

**Requirement.** The resilience owner shall define graceful-degradation modes for each Capability Instance, stating the trigger condition (for example loss of one cooling string, utility loss on UPS autonomy, loss of a fabric plane), the action (power capping, job preemption by priority, checkpoint-and-drain, inference replica reduction, admission control), the owner of the decision and the expected residual capacity. The platform operations lead shall implement the actions as tested automation or procedures and shall demonstrate by test or analysed event that each mode achieves the expected residual capacity within the time available before the triggering constraint is exceeded.

**Assessment criteria**

1. Degradation modes are defined per Capability Instance with trigger, action, decision owner and residual capacity.
2. Each mode's time-to-act is shorter than the time available (for example UPS autonomy or thermal ride-through).
3. Actions are implemented as tested automation or procedures, with job-priority classes defined in the scheduler.
4. Tests or events in the period demonstrated achieved residual capacity and time-to-act.
5. Power capping or throttling actions are verified not to create unsafe electrical or thermal transients.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Time to shed load to residual target | min | Less than UPS autonomy minus margin (illustrative 5) | Derived from POW and THM ride-through. |
| Accelerator power-cap floor | % of TDP | Vendor-supported range (illustrative 60) | Capability-profile parameter; vendor limits apply. |

**Minimum evidence**

- Degradation mode catalogue
- Scheduler priority and preemption configuration
- Power-capping and checkpoint-and-drain automation
- Test or event records with measured residual capacity and timings

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | DEGRADED; EMERGENCY; TRANSITION |
| periodCoverage | Tests within 12 months (illustrative) and after material change to power, cooling or scheduler. |
| independence | Test witnessed by a party independent of platform operations. |
| mandatoryItems | Degradation mode catalogue; Test or event records |
| acceptableAlternatives | Partial-scale tests extrapolated with documented analysis where full-scale tests are not authorised |
| unknownEffect | US3: unverified degradation modes condition the decision; CG-09/CG-10 SUPPORTING evaluation. |
| reassessmentTriggers | Change in UPS autonomy or cooling ride-through; Scheduler change; New workload priority class |

**Assessment methods.** DOCUMENT_REVIEW, TEST, SCENARIO_EXERCISE, ANALYSIS

**Assessment procedure**

1. Review the degradation catalogue against declared failure scenarios.
2. Compare time-to-act with available ride-through from POW/THM evidence.
3. Review scheduler and power-capping configuration.
4. Review or witness a degradation test and measure residual capacity.
5. Check for adverse transients created by the action.

**Gate mappings.** CG-09 Failure containment (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to every Capability Instance whose infrastructure can lose partial capacity. Not applicable where the declared outcome is all-or-nothing and that is explicitly accepted.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** DEGRADED, EMERGENCY, TRANSITION

**Failure modes addressed.** Load not shed before UPS exhaustion; All jobs killed instead of priority preemption; Power cap causing simultaneous load step; Thermal ride-through exceeded

**Testing safety.** Degradation tests that cap power or preempt jobs affect workloads and require capability owner authorisation; tests that remove power or cooling capacity require facility authorisation under OPS-007 and engineering safety review.

**UNKNOWN rule.** If time-to-act has not been measured, treat the mode as unavailable (U1) for scenarios where available time is shorter than the estimated time-to-act.

**Ontology classes.** Safeguard, OperatingState, CapacityAssertion, TestRecord · **Related controls.** MCF-RES-001, MCF-CMP-010, MCF-POW-011, MCF-THM-003, MCF-POW-020

**Informative references.** ISO 22316 (Organizational resilience: principles and attributes); ISO/IEC 27031 (ICT readiness for business continuity); AIDCF-004 (Threat, Hazard and Failure Model)

### MCF-RES-003

**Resilience Scenarios** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure a maintained library of credible single, compound and common-mode scenarios is used to design and test resilience, including the AIDCF-004 cross-domain scenarios relevant to the site.

**Requirement.** The resilience owner shall maintain a scenario library for each site and Capability Instance that includes, at minimum, the applicable AIDCF-004 cross-domain scenarios (X01 to X20), site-specific hazards, and maintenance-induced and recovery-induced scenarios; each scenario shall have an initiating event, initial operating state, propagation path, safeguards, residual capability and recovery path. The resilience owner shall prioritise scenarios using the AIDCF-004 prioritisation criteria and shall review the library annually and after major incidents.

**Assessment criteria**

1. A scenario library exists with the minimum record fields from AIDCF-004.
2. Applicable cross-domain scenarios X01–X20 are included or excluded with rationale.
3. Maintenance-induced, recovery-induced and compound scenarios are represented.
4. Scenarios are prioritised and linked to tests (RES-017/RES-018) and exercises (RES-019).
5. The library was reviewed in the last 12 months and after major incidents.

**Minimum evidence**

- Scenario library
- Applicability rationale for X01–X20
- Prioritisation record
- Review records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C2 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE; EMERGENCY; RECOVERY; TRANSITION |
| periodCoverage | Current version, reviewed within 12 months (illustrative). |
| independence | Reviewed by a cross-domain panel including facilities, network, compute, storage and security. |
| mandatoryItems | Scenario library; Applicability rationale |
| acceptableAlternatives |  |
| unknownEffect | US3: missing scenarios limit coverage of CG-09/CG-10 evidence; US4 if a prioritised scenario is excluded without rationale. |
| reassessmentTriggers | Major incident; Architecture change; New site hazard; Annual review |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INQUIRY

**Assessment procedure**

1. Review library completeness against AIDCF-004 fields.
2. Check applicability rationale for each X-scenario.
3. Confirm maintenance- and recovery-induced scenarios exist.
4. Trace prioritised scenarios to tests and exercises.
5. Confirm review history.

**Gate mappings.** CG-09 Failure containment (SUPPORTING); CG-10 Recovery readiness (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to every in-scope site and Capability Instance; scenario libraries may be shared across sites of identical design if site-specific hazards are added.

**Lifecycle stages.** PLAN, DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION

**Failure modes addressed.** Compound scenario never considered; Recovery-induced failure not anticipated; Library not updated after incident

**Testing safety.** Scenario development is analytical. Where scenario parameters are validated against live telemetry, collection shall be read-only.

**UNKNOWN rule.** Scenarios whose propagation path crosses an unanalysed dependency are recorded with U10 and flagged for DEP analysis.

**Ontology classes.** FailureScenario, Threat, Hazard, FaultDomain · **Related controls.** MCF-RES-018, MCF-RES-019, MCF-DEP-002, MCF-RES-007

**Informative references.** AIDCF-004 (Threat, Hazard and Failure Model); IEC 31010 (Risk management: risk assessment techniques); IEC 60812 (Failure modes and effects analysis); IEC 61025 (Fault tree analysis)

### MCF-RES-004

**Resilience Ownership** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure resilience of each Capability Instance has a single accountable owner with authority across facility, IT and provider boundaries and that resilience responsibilities are explicit for every contributing domain.

**Requirement.** The executive sponsor shall appoint an accountable resilience owner for each site or Capability Instance with authority to set resilience requirements, approve accepted limitations and direct cross-domain testing. The resilience owner shall maintain a resilience responsibility matrix naming the responsible owner for power, cooling, network, compute, storage, control-plane and provider elements of each resilience and recovery capability, including colocation and cloud provider responsibilities.

**Assessment criteria**

1. An accountable resilience owner is appointed in writing with defined authority.
2. A resilience responsibility matrix covers all contributing domains and providers.
3. Provider responsibilities are reflected in contracts or service descriptions.
4. Accepted resilience limitations are approved by the resilience owner or higher authority.
5. Owners named in the matrix confirm awareness (sampled).

**Minimum evidence**

- Appointment record
- Resilience responsibility matrix
- Provider contract or service description extracts
- Accepted limitation register

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C2 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY; RECOVERY |
| periodCoverage | Current version. |
| independence | Matrix confirmed by interviews with a sample of named owners. |
| mandatoryItems | Appointment record; Responsibility matrix |
| acceptableAlternatives |  |
| unknownEffect | US4 against CG-13 where a recovery-critical element has no owner. |
| reassessmentTriggers | Organisational change; New provider; Owner departure |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY

**Assessment procedure**

1. Review appointment and authority.
2. Review matrix coverage against domains and providers.
3. Check provider contract alignment.
4. Interview a sample of owners.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to all in-scope sites and Capability Instances.

**Lifecycle stages.** PLAN, OPERATE, CHANGE · **Operating states.** NORMAL, EMERGENCY, RECOVERY

**Failure modes addressed.** Colocation responsibility gap (X14); No one owns cross-domain recovery; Limitations accepted by unauthorised staff

**Testing safety.** Not applicable (governance control).

**UNKNOWN rule.** Any recovery-critical element with no named owner is recorded as a US4 UNKNOWN for CG-13.

**Ontology classes.** CapabilityInstance, Dependency, Control · **Related controls.** MCF-GOV-006, MCF-GOV-005, MCF-DEP-018, MCF-RES-021

**Informative references.** ISO 22301 (Business continuity management systems: requirements); ISO 22316 (Organizational resilience: principles and attributes)

## RES-02 Fault-domain and containment design

### MCF-RES-005

**Fault-Domain Definition** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure the site-level fault-domain model (power, cooling, fire, water, network, compute, storage and control-plane domains) is defined and reconciled to the as-built infrastructure, so that redundancy and independence claims are traceable.

**Requirement.** The resilience owner shall maintain a site fault-domain model that defines each fault domain (for example electrical distribution paths, UPS systems, cooling strings and CDU groups, fire compartments, water zones, network planes, compute pods, storage failure domains, control-plane clusters) with its members, and records which domains overlap. The resilience owner shall reconcile the model to as-built evidence (single-line diagrams, P&IDs, rack power and cooling mapping, fabric topology, scheduler and storage placement) at commissioning and after material change, and shall flag every redundancy claim whose members share a fault domain.

**Assessment criteria**

1. A fault-domain model exists covering all infrastructure classes.
2. Domain membership is reconciled to as-built evidence for each class.
3. Overlaps between domains (for example a network plane inside a single power path) are recorded.
4. Every redundancy claim is checked for members sharing a fault domain, and such cases are dispositioned.
5. The model was updated after each material change in the period.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Fault-domain model reconciliation age | days | 180 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Fault-domain model
- As-built references used in reconciliation (SLD, P&ID, rack maps, topology, placement)
- Overlap and shared-domain register
- Change-linked updates

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | Reconciliation within the age parameter. |
| independence | Reconciled by a party other than the model author, using primary as-built sources. |
| mandatoryItems | Fault-domain model; Reconciliation record; Shared-domain register |
| acceptableAlternatives | Graph-based dependency model meeting AIDCF-014 with automated reconciliation |
| unknownEffect | US4: CG-09 cannot PASS while the site fault-domain model is unreconciled for gate-critical outcomes. |
| reassessmentTriggers | Electrical or cooling re-zoning; Rack placement change; Expansion; Incident affecting more than one domain |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS, INSPECTION

**Assessment procedure**

1. Review model coverage across infrastructure classes.
2. Reconcile a sample of domains to primary as-built sources.
3. Examine overlaps and shared-domain register.
4. Test a sample of redundancy claims for shared membership.
5. Confirm update after recent changes.

**Gate mappings.** CG-09 Failure containment (CRITICAL); CG-03 Critical dependency visibility (SUPPORTING); CG-02 Boundary and architecture integrity (SUPPORTING)

**Applicability.** Applies to every in-scope site. Domain-specific fault-domain controls (NET-004, CMP-008) feed this model.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Redundant spines on one UPS path; Dual-fed racks on PDUs from one switchboard; Storage replicas in one fire compartment; Control-plane quorum in one rack

**Testing safety.** Reconciliation is non-intrusive; physical verification of power feeds shall use visual inspection or EPMS data only, never live disconnection.

**UNKNOWN rule.** Domain membership that cannot be reconciled is recorded as U1 or U3 and the affected redundancy claims are treated as unproven.

**Ontology classes.** FaultDomain, Dependency, ArchitectureSnapshot, InfrastructureSystem · **Related controls.** MCF-NET-004, MCF-CMP-008, MCF-DEP-005, MCF-RES-007, MCF-RES-006

**Informative references.** IEC 31010 (Risk management: risk assessment techniques); ANSI/TIA-942 (Telecommunications infrastructure standard for data centres); EN 50600 series / ISO/IEC 22237 series (Data centre facilities and infrastructures); AIDCF-013 (AI Data Centre Assurance Reference Architecture)

### MCF-RES-006

**Containment Boundaries** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure physical, electrical, thermal, network and logical boundaries that are intended to stop propagation are implemented as designed, with their isolating devices identified and maintained.

**Requirement.** The resilience owner shall identify each containment boundary relied upon (for example fire compartment, electrical protection discrimination point, cooling-loop isolation valves, fabric partition, security zone, scheduler placement constraint, storage failure domain) together with the isolating device or mechanism and its required response. The domain owners shall confirm that each mechanism is installed, configured and maintained as designed and shall record mechanisms in bypass or override as temporary configurations under OPS-019.

**Assessment criteria**

1. A containment-boundary register lists boundaries, isolating mechanisms and intended response.
2. Mechanisms are installed and configured as designed (sampled inspection or configuration extract).
3. Maintenance status of isolating devices is current.
4. Mechanisms in bypass or override are recorded as temporary configurations with expiry.
5. Scheduler and storage placement constraints that enforce logical containment are configured and verified.

**Minimum evidence**

- Containment-boundary register
- Inspection or configuration evidence per mechanism
- Maintenance records
- Temporary configuration register

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | Current configuration; maintenance within manufacturer interval. |
| independence | Inspection by domain specialists independent of the register author. |
| mandatoryItems | Boundary register; Configuration or inspection evidence |
| acceptableAlternatives |  |
| unknownEffect | US3; US4 against CG-09 where the boundary protects a gate-critical outcome. |
| reassessmentTriggers | Boundary device replacement; Bypass applied; Layout change |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, RECONCILIATION, SAMPLING

**Assessment procedure**

1. Review the register for completeness against the scenario library.
2. Sample mechanisms and verify installation and configuration.
3. Check maintenance records.
4. Review bypass/override records.
5. Verify logical placement constraints in scheduler and storage.

**Gate mappings.** CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to every containment boundary relied upon in fault-domain or blast-radius claims.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Isolation valve seized; Breaker discrimination lost after setting change; Fire damper not closing; Placement constraint removed from scheduler

**Testing safety.** Operating isolating devices is not part of this control; functional tests belong to RES-008 and require authorisation.

**UNKNOWN rule.** Boundaries whose mechanism status is unknown are treated as absent in blast-radius analysis.

**Ontology classes.** Safeguard, FaultDomain, AssetInstance · **Related controls.** MCF-RES-005, MCF-RES-008, MCF-OPS-019, MCF-NET-012, MCF-THM-020

**Informative references.** IEC 31010 (Risk management: risk assessment techniques); EN 50600 series / ISO/IEC 22237 series (Data centre facilities and infrastructures)

### MCF-RES-007

**Blast Radius** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure the maximum consequence of each credible failure is quantified in capability terms (accelerators, jobs, tenants, inference capacity, data) and compared with the impact tolerance.

**Requirement.** The resilience owner shall perform and maintain a blast-radius analysis for each prioritised scenario and each fault domain, stating the affected assets, the affected Capability Instances, the capability consequence in outcome units and comparison with impact tolerance, including common-cause and common-mode failures (for example firmware rollout, shared controller, shared identity provider). The resilience owner shall record every blast radius exceeding tolerance as a Finding with a treatment plan or approved limitation.

**Assessment criteria**

1. Blast-radius analysis covers every prioritised scenario and fault domain.
2. Consequences are stated in outcome units and compared with impact tolerance.
3. Common-cause and common-mode cases (software, firmware, configuration, identity, automation) are included.
4. Analysis is reconciled to the current fault-domain model (RES-005).
5. Exceedances have treatment plans or approved limitations.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum blast radius per single credible failure | % of Capability Instance capacity | Impact-tolerance derived (illustrative 25) | Capability-profile parameter. |

**Minimum evidence**

- Blast-radius analysis
- Reconciliation to fault-domain model
- Exceedance register and treatment plans

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E7 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE; FAILED |
| periodCoverage | Current; updated after material change. |
| independence | Reviewed by a cross-domain panel independent of the analyst. |
| mandatoryItems | Blast-radius analysis; Exceedance register |
| acceptableAlternatives | Graph-query outputs from a conformant AIDCF-014 model with human review |
| unknownEffect | US4: CG-09 cannot PASS while blast radius for gate-critical scenarios is unquantified. |
| reassessmentTriggers | Fault-domain model change; New common-mode dependency; Incident exceeding predicted blast radius |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW, RECONCILIATION

**Assessment procedure**

1. Review coverage against scenarios and domains.
2. Recompute blast radius for a sample of scenarios from the fault-domain model.
3. Check common-mode inclusion.
4. Compare with tolerances and review exceedances.

**Gate mappings.** CG-09 Failure containment (CRITICAL); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to all in-scope Capability Instances, including multi-tenant platforms where blast radius is expressed per tenant.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, FAILED

**Failure modes addressed.** Firmware update bricking all nodes; Shared identity provider outage blocking all operations; Single cooling loop serving whole cluster; Concentration of tenant capacity in one hall

**Testing safety.** Analytical.

**UNKNOWN rule.** If a scenario's blast radius depends on an unresolved dependency, record U10 and use the worst credible case.

**Ontology classes.** FailureScenario, FaultDomain, CapacityAssertion, Finding · **Related controls.** MCF-RES-005, MCF-RES-003, MCF-NET-004, MCF-DEP-013

**Informative references.** IEC 31010 (Risk management: risk assessment techniques); IEC 60812 (Failure modes and effects analysis); IEC 61025 (Fault tree analysis); AIDCF-004 (Threat, Hazard and Failure Model)

### MCF-RES-008

**Isolation Validation** · DETECTIVE · claim type RESILIENCE · required AL5

**Objective.** Ensure containment boundaries actually stop propagation when demanded, verified by representative tests, analysed incidents or safe simulations.

**Requirement.** The resilience owner shall maintain an isolation validation plan that assigns a validation method from the AIDCF-004 safe validation hierarchy (V0–V7) to each containment boundary, with the highest safe level for gate-critical boundaries, and shall execute the plan over a defined cycle. The domain owners shall record results, including failed or partial isolation, and shall retest after remediation.

**Assessment criteria**

1. Each boundary has an assigned validation method and level.
2. Gate-critical boundaries are validated at V5 (component functional test) or above, or the shortfall is justified and recorded.
3. Validation in the cycle demonstrated isolation within the expected response.
4. Failed or partial isolation results led to remediation and retest.
5. Network and logical isolation (fabric partitions, security zones, scheduler placement) are included alongside physical boundaries.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Isolation validation cycle | months | 24 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Isolation validation plan
- Test, incident or simulation records
- Remediation and retest records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T3 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE; FAILED; EMERGENCY |
| periodCoverage | Within the validation cycle. |
| independence | Tests witnessed by an independent party (E5) for gate-critical boundaries. |
| mandatoryItems | Validation plan; Results for gate-critical boundaries |
| acceptableAlternatives | Analysed real incident demonstrating isolation, with event evidence |
| unknownEffect | US4: untested gate-critical boundaries leave CG-09 UNKNOWN. |
| reassessmentTriggers | Boundary change; Failed test; Incident; Cycle expiry |

**Assessment methods.** TEST, SCENARIO_EXERCISE, ANALYSIS, DOCUMENT_REVIEW

**Assessment procedure**

1. Review the plan and assigned levels.
2. Sample gate-critical boundaries and review results.
3. Check failed/partial results for remediation and retest.
4. Confirm logical boundaries are included.

**Gate mappings.** CG-09 Failure containment (CRITICAL); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to all containment boundaries in the RES-006 register.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, FAILED, EMERGENCY

**Failure modes addressed.** Boundary passes design review but fails on demand; Fire damper fails to close; Fabric partition leaks traffic; Protection fails to discriminate

**Testing safety.** Isolation tests involving electrical protection, fire systems, fluid isolation or production fabrics are hazardous or disruptive; they require written authorisation from the facility owner and the relevant engineering authority, permit-to-work, method statements, and a safety and rollback plan. Tests at V6/V7 require additional executive authorisation.

**UNKNOWN rule.** Boundaries validated only at V0–V2 are recorded with U8 for effectiveness claims.

**Ontology classes.** TestRecord, Safeguard, FaultDomain · **Related controls.** MCF-RES-006, MCF-RES-017, MCF-RES-018, MCF-NET-012, MCF-SEC-019

**Informative references.** AIDCF-004 (Threat, Hazard and Failure Model); IEC 31010 (Risk management: risk assessment techniques); EN 50600 series / ISO/IEC 22237 series (Data centre facilities and infrastructures)

## RES-03 Continuity planning

### MCF-RES-009

**Continuity Strategy** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure an approved continuity strategy states how each Capability Instance's minimum outcome will be sustained or resumed across site loss, provider loss and major infrastructure loss.

**Requirement.** The resilience owner shall maintain an approved continuity strategy for each Capability Instance that selects and justifies the continuity approach (for example in-site redundancy, active-active multi-site inference, warm standby training capacity, checkpoint replication to an alternate site, contracted cloud burst, or accepted suspension), states the dependencies of the chosen approach, and is consistent with the impact tolerances in RES-001.

**Assessment criteria**

1. An approved strategy exists per Capability Instance with the selected approach and justification.
2. The strategy meets or explicitly accepts shortfall against impact tolerances.
3. Dependencies of the strategy (alternate site, provider, data replication, staff) are listed.
4. The strategy addresses site loss, major provider loss and loss of the AI control plane.

**Minimum evidence**

- Continuity strategy
- Tolerance comparison
- Strategy dependency list

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C2 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | EMERGENCY; FAILED; RECOVERY |
| periodCoverage | Current approved version, reviewed within 12 months (illustrative). |
| independence | Approved by the capability owner and reviewed by the resilience owner. |
| mandatoryItems | Approved strategy |
| acceptableAlternatives |  |
| unknownEffect | US3; US4 against CG-10 where no strategy exists for a gate-critical outcome. |
| reassessmentTriggers | New site or provider; Tolerance change; Major incident |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INQUIRY

**Assessment procedure**

1. Review strategy and approval.
2. Compare with tolerances.
3. Review dependencies and coverage of site, provider and control-plane loss.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-01 Capability and outcome definition (SUPPORTING)

**Applicability.** Applies to all in-scope Capability Instances, including those whose approved strategy is accepted suspension (the acceptance itself is assessed).

**Lifecycle stages.** PLAN, DESIGN, CHANGE · **Operating states.** EMERGENCY, FAILED, RECOVERY

**Failure modes addressed.** No plan for site loss; Strategy relies on unavailable alternate capacity; Control-plane loss not considered

**Testing safety.** Strategy review is analytical; feasibility of the selected approach is tested under RES-010 and RES-018 with their own authorisation requirements.

**UNKNOWN rule.** Strategies that rely on an unverified dependency are recorded with U10.

**Ontology classes.** CapabilityInstance, Dependency, Safeguard · **Related controls.** MCF-RES-001, MCF-RES-010, MCF-RES-011, MCF-DEP-016

**Informative references.** ISO 22301 (Business continuity management systems: requirements); ISO 22313 (Business continuity management systems: guidance); ISO/IEC 27031 (ICT readiness for business continuity); NIST SP 800-34 Rev. 1 (Contingency planning guide for federal information systems)

### MCF-RES-010

**Alternative Capacity** · RECOVERY · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure alternate compute, storage and network capacity relied upon by the continuity strategy exists, is compatible and can be brought into service within tolerance.

**Requirement.** The capability owner shall identify the alternate capacity relied upon (alternate cluster, partitioned reserve, alternate site, cloud contract) with its size, compatibility (accelerator generation, software stack, fabric, storage access) and activation time, and shall secure it by reservation or contract. The platform operations lead shall demonstrate by test at a defined interval that a representative workload can be relocated to alternate capacity and resumed from checkpoint or served within the activation time.

**Assessment criteria**

1. Alternate capacity is identified with size, compatibility and activation time.
2. Capacity is reserved or contracted, with terms that hold during regional demand surges.
3. Software stack, images and data access on alternate capacity are kept compatible.
4. A relocation test in the interval demonstrated resumption within activation time.
5. Data transfer or replication capacity for relocation is sufficient (checkpoint size over link capacity).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Alternate capacity activation time | h | Within maximum tolerable disruption (illustrative 8) | Derived from RES-001. |
| Relocation test interval | months | 12 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Alternate capacity register
- Reservation or contract terms
- Compatibility matrix
- Relocation test records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | EMERGENCY; RECOVERY; FAILED |
| periodCoverage | Test within the interval. |
| independence | Test witnessed by the resilience owner's function. |
| mandatoryItems | Relocation test record; Contract or reservation evidence |
| acceptableAlternatives |  |
| unknownEffect | US3; US4 against CG-10 where the continuity strategy depends solely on alternate capacity. |
| reassessmentTriggers | Capacity contract change; Accelerator generation change; Software stack change |

**Assessment methods.** DOCUMENT_REVIEW, TEST, ANALYSIS

**Assessment procedure**

1. Review register and contract terms.
2. Check compatibility of stack, images and data access.
3. Review or witness a relocation test.
4. Recompute data transfer time for relocation.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies where the continuity strategy relies on alternate capacity. Not applicable where accepted suspension is the approved strategy.

**Lifecycle stages.** PLAN, OPERATE, CHANGE · **Operating states.** EMERGENCY, RECOVERY, FAILED

**Failure modes addressed.** Alternate cloud capacity unavailable during regional surge; Incompatible accelerator generation; Checkpoint transfer exceeds tolerance; Images outdated on standby cluster

**Testing safety.** Relocation tests consume alternate capacity and may incur cost; production workloads shall not be moved without capability owner authorisation.

**UNKNOWN rule.** Alternate capacity with no test is recorded as U1 for activation-time claims.

**Ontology classes.** Resource, CapacityAssertion, Dependency, TestRecord · **Related controls.** MCF-RES-009, MCF-DEP-012, MCF-DEP-016, MCF-STO-014

**Informative references.** ISO 22301 (Business continuity management systems: requirements); ISO/IEC 27031 (ICT readiness for business continuity); Regulation (EU) 2022/2554 (Digital Operational Resilience Act)

### MCF-RES-011

**Site and Provider Continuity** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure the continuity arrangements of sites, colocation operators, utilities, carriers and critical service providers are known, evidenced and compatible with the Capability Instance's tolerances.

**Requirement.** The resilience owner shall obtain, for each site operator and critical provider (colocation, utility, carrier, cloud, OEM support), evidence of their continuity arrangements relevant to the outcome (for example operator emergency response, fuel contracts, carrier restoration commitments, provider recovery objectives), and shall reconcile provider objectives with the Capability Instance's tolerances. The resilience owner shall record every mismatch as a dependency limitation.

**Assessment criteria**

1. Each critical site operator and provider has continuity evidence on file.
2. Provider recovery objectives are compared with tolerances.
3. Mismatches are recorded as limitations or treated.
4. Evidence rights and incident notification are contractually defined (SUP-006, SUP-007).
5. Provider evidence is current within the evidence-age parameter.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Provider continuity evidence age | months | 12 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Provider continuity evidence
- Tolerance reconciliation
- Limitation register

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E5 |
| optionalClasses | E3; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | EMERGENCY; FAILED; RECOVERY |
| periodCoverage | Within evidence age. |
| independence | Third-party evidence (E5) where available; otherwise contractual attestation corroborated by inquiry. |
| mandatoryItems | Provider continuity evidence; Reconciliation |
| acceptableAlternatives | Independent audit reports covering continuity scope |
| unknownEffect | US3; US4 against CG-03 where a sole provider's continuity is unknown. |
| reassessmentTriggers | Provider change; Provider incident; Contract renewal |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY, ANALYSIS

**Assessment procedure**

1. List critical providers.
2. Review continuity evidence and currency.
3. Reconcile objectives with tolerances.
4. Review limitations and contractual rights.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to all critical providers and site operators.

**Lifecycle stages.** PLAN, OPERATE, CHANGE · **Operating states.** EMERGENCY, FAILED, RECOVERY

**Failure modes addressed.** Carrier restoration time beyond tolerance; Colocation fuel contract shared with neighbours; OEM support unavailable in crisis (X18)

**Testing safety.** Provider evidence is reviewed as documents; any joint failover exercise with a provider requires a jointly approved test plan and provider authorisation.

**UNKNOWN rule.** Providers refusing evidence are recorded with U2 and treated as single points of failure in strategy analysis.

**Ontology classes.** Dependency, Interface, Resource · **Related controls.** MCF-DEP-009, MCF-DEP-010, MCF-DEP-011, MCF-SUP-006, MCF-NET-002

**Informative references.** ISO 22301 (Business continuity management systems: requirements); Regulation (EU) 2022/2554 (Digital Operational Resilience Act); ISO/IEC 27031 (ICT readiness for business continuity)

### MCF-RES-012

**Crisis Priorities** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure pre-agreed restoration and allocation priorities exist for when capacity is scarce, so that crisis decisions on which workloads, tenants and services are protected or restored first are not improvised.

**Requirement.** The capability owner shall approve a priority scheme stating, for scarce power, cooling, compute and network capacity during DEGRADED, EMERGENCY and RECOVERY states, which workloads, tenants and services are protected, preempted and restored first, consistent with contractual commitments and life-safety precedence. The platform operations lead shall implement the scheme in scheduler priority classes and runbooks.

**Assessment criteria**

1. An approved priority scheme exists covering protection, preemption and restoration order.
2. The scheme is consistent with contractual commitments and life-safety precedence.
3. Scheduler priority classes and runbooks implement the scheme.
4. Crisis command (RES-021) uses the scheme in exercises.

**Minimum evidence**

- Priority scheme
- Scheduler configuration
- Runbook extracts
- Exercise records using the scheme

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C2 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | DEGRADED; EMERGENCY; RECOVERY |
| periodCoverage | Current approved version. |
| independence | Approval by the capability owner, review by commercial/contract owner. |
| mandatoryItems | Approved priority scheme |
| acceptableAlternatives |  |
| unknownEffect | US3: absent priorities condition recovery decisions. |
| reassessmentTriggers | New tenant commitment; Workload criticality change |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY, RECONCILIATION

**Assessment procedure**

1. Review scheme and approval.
2. Check consistency with commitments.
3. Reconcile to scheduler configuration.
4. Review exercise use.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-01 Capability and outcome definition (SUPPORTING)

**Applicability.** Applies to all shared or multi-workload Capability Instances.

**Lifecycle stages.** PLAN, DESIGN, OPERATE · **Operating states.** DEGRADED, EMERGENCY, RECOVERY

**Failure modes addressed.** Low-priority jobs restored before critical inference; Contractual breach during shedding; Improvised priorities under pressure

**Testing safety.** Priority review is document-based; testing preemption against live workloads is governed by RES-002 and requires capability owner authorisation.

**UNKNOWN rule.** If the scheme is not reflected in scheduler configuration, record a Finding; claims of priority-based shedding are limited to DESIGN.

**Ontology classes.** ServiceOutcome, OperatingState, Control · **Related controls.** MCF-RES-001, MCF-RES-002, MCF-RES-021, MCF-GOV-021

**Informative references.** ISO 22301 (Business continuity management systems: requirements); ISO 22320 (Emergency management: guidelines for incident management)

## RES-04 Recovery planning

### MCF-RES-013

**Recovery Dependencies** · RECOVERY · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure every prerequisite for recovering each Capability Instance (power, cooling, network, time, identity, DNS, storage metadata, controllers, images, licences, people and providers) is identified, including circular and cold-start dependencies.

**Requirement.** The recovery manager shall maintain a recovery dependency map for each Capability Instance, derived from DEP-004, listing every prerequisite system, service, credential, artefact, person and provider required to restore the outcome from a cold or failed state, and shall identify circular dependencies (for example identity provider hosted on the cluster it unlocks, DNS required to reach the time source, BMC firmware repository on the failed storage) and the means by which each is broken. The recovery manager shall verify the map against the last integrated recovery test.

**Assessment criteria**

1. A recovery dependency map exists per Capability Instance covering infrastructure, services, credentials, artefacts, people and providers.
2. Circular and cold-start dependencies are identified with a documented break (for example offline copy, local fallback, out-of-band path).
3. Each dependency has an owner and a recovery path.
4. The map was verified against the most recent integrated recovery test and updated with discovered dependencies.
5. Offline artefacts (images, configuration backups, credentials) are stored outside the failure domain they recover.

**Minimum evidence**

- Recovery dependency map
- Circular-dependency analysis and breaks
- Integrated test discrepancy log
- Offline artefact inventory and location

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S5 |
| stateCoverage | FAILED; RECOVERY; SHUTDOWN; EMERGENCY |
| periodCoverage | Verified against a test within 24 months (illustrative). |
| independence | Verified by a party independent of the map author, preferably through test observation. |
| mandatoryItems | Recovery dependency map; Circular-dependency analysis |
| acceptableAlternatives | Graph-based dependency model with automated cycle detection and human review |
| unknownEffect | US4: CG-10 cannot PASS while circular recovery dependencies are unanalysed. |
| reassessmentTriggers | New control-plane service; Identity architecture change; Storage platform change; Recovery test discovering missing dependency |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Review the recovery dependency map for completeness against DEP-004.
2. Run or review cycle detection for circular dependencies.
3. Verify breaks for each cycle (offline copies, local auth, OOB).
4. Check offline artefact locations against fault domains.
5. Compare the map with the last integrated test discrepancies.

**Gate mappings.** CG-10 Recovery readiness (CRITICAL); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to every in-scope Capability Instance.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** FAILED, RECOVERY, SHUTDOWN, EMERGENCY

**Failure modes addressed.** Identity provider on the failed cluster (X19); Images only on failed storage; Licence server unreachable; Key personnel unavailable

**Testing safety.** Analytical; verification draws on RES-018 tests.

**UNKNOWN rule.** Any recovery prerequisite whose location or availability in a failure state is unknown is recorded as U10 at US4 against CG-10.

**Ontology classes.** Dependency, RequiredFunction, FaultDomain, Resource · **Related controls.** MCF-DEP-004, MCF-RES-014, MCF-NET-015, MCF-NET-024, MCF-SEC-004

**Informative references.** ISO/IEC 27031 (ICT readiness for business continuity); NIST SP 800-34 Rev. 1 (Contingency planning guide for federal information systems); AIDCF-004 (Threat, Hazard and Failure Model)

### MCF-RES-014

**Recovery Sequencing** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure a tested, ordered restoration sequence exists from total or partial loss through power, cooling, network, storage, compute and control plane to validated service, with hold points and safety checks between stages.

**Requirement.** The recovery manager shall maintain a black-start and restoration sequence for each site and Capability Instance that orders restoration through power (utility or generation, distribution, UPS), cooling (heat rejection, facility water, CDUs and liquid loops before IT load), out-of-band and core network, time and identity services, storage (metadata and quorum before data services), compute (BMC, firmware validation, health checks, burn-in) and AI control plane (cluster manager, scheduler), with entry criteria, hold points, load-step limits and safety checks at each stage. The recovery manager shall demonstrate the sequence by integrated test or exercise at a defined interval and shall record achieved stage durations against the recovery time objective.

**Assessment criteria**

1. A restoration sequence exists covering power, cooling, network, storage, compute and control plane with entry criteria and hold points.
2. Cooling capacity is confirmed before IT load is restored at each step, and load-step limits respect generator and UPS capability.
3. The sequence references POW-024, THM-024, STO-019, CMP-023 and NET restoration runbooks consistently.
4. An integrated test or exercise in the interval executed the sequence (fully or in representative segments) and recorded stage durations.
5. Total achieved duration is within the recovery time objective, or the shortfall is a Finding.
6. Validation at the end of the sequence confirms Service Outcome restoration, not only system availability.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Target black-start-to-service time | h | Within RTO (illustrative 12) | Derived from RES-001. |
| Maximum IT load step during restoration | % of generator rating | Generator- and UPS-specific (illustrative 25) | From POW-020 load-step analysis. |
| Integrated restoration test interval | months | 24 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Restoration sequence document
- Cross-references to domain restoration runbooks
- Integrated test or exercise records with stage timings
- Validation records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T3 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | SHUTDOWN; FAILED; RECOVERY; TRANSITION; EMERGENCY |
| periodCoverage | Integrated test within the interval. |
| independence | Witnessed by an independent party (E5) for gate-critical outcomes. |
| mandatoryItems | Restoration sequence; Integrated test record with stage timings |
| acceptableAlternatives | Segmented tests (for example power-to-cooling at site level; network-to-control-plane at cluster level) with interface hand-offs explicitly tested, plus a full tabletop walk-through |
| unknownEffect | US4: CG-10 cannot PASS while the restoration sequence is untested end-to-end or by segments with tested hand-offs. |
| reassessmentTriggers | Major architecture change; New control-plane dependency; Failed or incomplete test; Real restoration event |

**Assessment methods.** DOCUMENT_REVIEW, SCENARIO_EXERCISE, TEST, ANALYSIS, OBSERVATION

**Assessment procedure**

1. Review the sequence for order, entry criteria, hold points and safety checks.
2. Cross-check against domain restoration runbooks for consistency.
3. Check load-step and cooling-before-load constraints.
4. Review or observe an integrated test and extract stage durations.
5. Compare total duration with RTO.
6. Confirm service-outcome validation at completion.

**Gate mappings.** CG-10 Recovery readiness (CRITICAL); CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to every in-scope site and Capability Instance. Single-system recovery runbooks remain under their domain controls.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** SHUTDOWN, FAILED, RECOVERY, TRANSITION, EMERGENCY

**Failure modes addressed.** IT load restored before cooling, causing thermal trip; Simultaneous node power-on exceeding generator load-step; Control plane restored before identity and time; Storage data services started before metadata quorum

**Testing safety.** Black-start tests involve hazardous energy and site-wide disruption and require written authorisation from the facility owner, the electrical and mechanical engineering authorities and the capability owner, permit-to-work, a safety case and a rollback plan. Segmented and simulation-based tests are preferred where full tests are not authorised.

**UNKNOWN rule.** Stages never executed in test are recorded with U5 and the sequence is assessed only to DESIGN for those stages.

**Ontology classes.** RequiredFunction, Action, OperatingState, TestRecord · **Related controls.** MCF-POW-024, MCF-THM-024, MCF-STO-019, MCF-CMP-023, MCF-NET-015

**Informative references.** ISO/IEC 27031 (ICT readiness for business continuity); NIST SP 800-34 Rev. 1 (Contingency planning guide for federal information systems); ISO 22301 (Business continuity management systems: requirements); AIDCF-013 (AI Data Centre Assurance Reference Architecture)

### MCF-RES-015

**Configuration Restoration** · RECOVERY · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure the configuration of infrastructure and control-plane systems can be restored from a known-good, integrity-verified baseline, avoiding reintroduction of corrupt or malicious configuration.

**Requirement.** The recovery manager shall ensure that configuration backups of network devices, controllers, BMS/EPMS, CDU controllers, storage controllers, cluster managers and identity systems are taken at a defined interval, are integrity-protected (hashed or signed), are stored outside the failure and compromise domain they protect, and are tagged with the approved baseline they correspond to. The recovery manager shall test restoration of a sample of each system class at a defined interval, including verification that the restored configuration matches the approved baseline and not a compromised or drifted state.

**Assessment criteria**

1. Backups exist for every system class with defined interval.
2. Backups are integrity-protected and stored outside the protected failure/compromise domain.
3. Backups are tagged to an approved baseline and integrity is verified before restore.
4. Restore tests per system class in the interval succeeded and were verified against baseline.
5. A procedure exists for selecting a pre-compromise baseline when compromise is suspected (X15).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Configuration backup interval | h | 24 or on change (illustrative) | Capability-profile parameter. |
| Restore test interval per class | months | 12 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Backup inventory and schedules
- Integrity mechanism evidence
- Storage location analysis
- Restore test records
- Pre-compromise baseline selection procedure

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | RECOVERY; FAILED; MAINTENANCE |
| periodCoverage | Restore tests within interval. |
| independence | Restore test observed by a party independent of the system administrators. |
| mandatoryItems | Restore test records; Integrity verification evidence |
| acceptableAlternatives |  |
| unknownEffect | US3; US4 against CG-10 where BMS/EPMS or fabric controller configuration has no tested restore. |
| reassessmentTriggers | Backup platform change; System class added; Compromise incident |

**Assessment methods.** DOCUMENT_REVIEW, TEST, REPERFORMANCE, SAMPLING

**Assessment procedure**

1. Review backup inventory coverage.
2. Verify integrity protection and storage location.
3. Review or reperform a restore and compare to baseline.
4. Review pre-compromise baseline procedure.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-07 Critical control-system integrity (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all configuration-bearing infrastructure and control-plane systems in scope.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** RECOVERY, FAILED, MAINTENANCE

**Failure modes addressed.** Restoring compromised configuration (X15); Backups on the same failed storage; BMS controller backup never restored; Restored config drifted from baseline

**Testing safety.** Restores to OT controllers (BMS, EPMS, CDU, PLC) shall be performed only on test benches or spare controllers unless a maintenance window is authorised by the facility owner with plant in a safe state.

**UNKNOWN rule.** Systems with backups but no restore test are recorded as U1 for restore claims.

**Ontology classes.** ArchitectureSnapshot, Safeguard, TestRecord, EvidenceObject · **Related controls.** MCF-NET-022, MCF-SEC-024, MCF-OPS-020, MCF-STO-012, MCF-CMP-016

**Informative references.** ISO/IEC 27031 (ICT readiness for business continuity); NIST SP 800-34 Rev. 1 (Contingency planning guide for federal information systems); ISA/IEC 62443-2-1 (Security programme requirements for IACS asset owners)

### MCF-RES-016

**Data and Checkpoint Recovery** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure training state (checkpoints, optimiser state, data-loader position), model artefacts and essential datasets can be recovered within the recovery point and time objectives and that restarted jobs resume correctly.

**Requirement.** The capability owner shall set a checkpoint policy per training Capability Instance stating checkpoint interval (justified against failure rate, checkpoint cost and maximum lost work, for example using a Young/Daly-style optimisation), checkpoint retention, and the number and placement of durable copies outside the training cluster's failure domain. The platform operations lead shall verify checkpoint integrity at write and before restore, and shall test at a defined interval that a representative job can be restarted from checkpoint (including on a different set of nodes) and reaches equivalent training state within RTO and lost-work tolerance.

**Assessment criteria**

1. Checkpoint interval, retention and copy placement are defined and justified against lost-work tolerance.
2. Durable copies are stored outside the training cluster's power, storage and compromise domain.
3. Checkpoint integrity is verified at write and before restore.
4. Restart tests in the interval achieved resumption within RTO and lost-work tolerance, including on alternate nodes.
5. Model artefacts and essential datasets have recovery copies meeting RPO.
6. Inference model artefacts can be redeployed within the inference RTO.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Checkpoint interval | min | Optimised from failure rate and checkpoint cost (illustrative 60) | Young/Daly-style approximation; capability-specific. |
| Durable checkpoint copies outside cluster failure domain | count | 1 (illustrative) | Capability-profile parameter. |
| Restart-from-checkpoint time | min | Within RTO (illustrative 30) | Derived from RES-001. |

**Minimum evidence**

- Checkpoint policy and justification
- Copy placement evidence
- Integrity verification logs
- Restart test records
- Artefact and dataset recovery-copy evidence

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T3 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; FAILED; RECOVERY; DEGRADED |
| periodCoverage | Restart test within 6 months (illustrative); integrity logs for 90 days. |
| independence | Restart test witnessed independently of the training team. |
| mandatoryItems | Checkpoint policy; Restart test record; Integrity verification logs |
| acceptableAlternatives | Production restart events with recorded resumption times and training-state checks |
| unknownEffect | US4: CG-10 cannot PASS while checkpoint restart is untested for gate-critical training outcomes. |
| reassessmentTriggers | Model size growth; Storage platform change; Framework change; Failed restart |

**Assessment methods.** DOCUMENT_REVIEW, TEST, ANALYSIS, SAMPLING

**Assessment procedure**

1. Review the checkpoint policy and interval justification.
2. Verify copy placement against fault domains.
3. Sample integrity logs.
4. Review or witness a restart test including alternate nodes.
5. Review artefact and dataset recovery copies.

**Gate mappings.** CG-10 Recovery readiness (CRITICAL); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to training and fine-tuning Capability Instances, and to inference for model artefact recovery.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, FAILED, RECOVERY, DEGRADED

**Failure modes addressed.** Corrupt checkpoint discovered only at restore; All checkpoints on the failed storage; Restart fails on different topology; Lost-work exceeds tolerance due to long interval

**Testing safety.** Restart tests consume capacity and shall be scheduled with the capability owner; do not delete or overwrite production checkpoints during tests.

**UNKNOWN rule.** Checkpoints without integrity verification are recorded as U7 and do not support recovery claims.

**Ontology classes.** Resource, RequiredFunction, TestRecord, Safeguard · **Related controls.** MCF-STO-017, MCF-STO-018, MCF-STO-016, MCF-NET-009, MCF-RES-001

**Informative references.** ISO/IEC 27031 (ICT readiness for business continuity); NIST SP 800-34 Rev. 1 (Contingency planning guide for federal information systems)

## RES-05 Testing and exercising

### MCF-RES-017

**Component Tests** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure resilience-relevant components (generators, UPS, transfer switches, CDU pumps, valves, fabric failover, controller failover, storage failover) are functionally tested on a defined programme and results tracked.

**Requirement.** The resilience owner shall maintain a component test programme listing each resilience-relevant component class, the test method, frequency and acceptance criteria, coordinated with domain maintenance programmes. Domain owners shall execute tests per programme, record results, and raise and close defects; the resilience owner shall review programme adherence quarterly.

**Assessment criteria**

1. A component test programme exists with class, method, frequency and acceptance criteria.
2. Tests were executed per schedule in the period (adherence rate meets target).
3. Failed tests raised defects that were closed or have approved deferral.
4. Quarterly adherence reviews occurred.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Programme adherence target | % of scheduled tests completed on time | 95 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Component test programme
- Test records for the period
- Defect records
- Adherence reviews

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E3; E4 |
| optionalClasses | E1; E2 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | 12 months (illustrative). |
| independence | Assessor samples from asset registers rather than from completed-test lists. |
| mandatoryItems | Test records; Defect records |
| acceptableAlternatives |  |
| unknownEffect | US3: programme gaps reduce support for CG-05/06/08/10 claims. |
| reassessmentTriggers | Programme change; Repeated test failures |

**Assessment methods.** SAMPLING, DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Review programme coverage.
2. Sample components from asset registers and trace tests.
3. Review defects and closure.
4. Review adherence reviews.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to all resilience-relevant components across domains.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Latent failure of untested component (generator no-start); Test failures not remediated; Programme drift

**Testing safety.** Component tests involving hazardous energy require permit-to-work and authorised persons under OPS-007; disruptive IT failover tests require change approval.

**UNKNOWN rule.** Components with no test record in the period are recorded as U1 for operational claims.

**Ontology classes.** TestRecord, AssetInstance, Action · **Related controls.** MCF-POW-006, MCF-THM-010, MCF-NET-021, MCF-OPS-009

**Informative references.** NIST SP 800-84 (Guide to test, training and exercise programs for IT plans and capabilities); ISO 22301 (Business continuity management systems: requirements)

### MCF-RES-018

**Integrated Scenario Tests** · DETECTIVE · claim type RESILIENCE · required AL5

**Objective.** Ensure prioritised cross-domain scenarios are exercised as integrated tests across power, cooling, network, compute, storage and control plane, demonstrating that the Capability Instance stays within or recovers within tolerance.

**Requirement.** The resilience owner shall plan and execute integrated scenario tests for prioritised scenarios from RES-003 (for example utility loss with generator start and UPS transfer under AI load, cooling string loss at sustained load, fabric plane loss during checkpoint, control-plane loss), measuring capability-level outcomes (job survival, lost work, inference availability, restoration time) as well as system behaviour. The resilience owner shall define test objectives, safety case, abort criteria and success criteria tied to impact tolerances before each test and shall record results and defects.

**Assessment criteria**

1. Integrated tests cover the highest-priority scenarios on a defined cycle.
2. Each test has objectives, safety case, abort criteria and success criteria tied to tolerances.
3. Tests measure capability-level outcomes, not only component behaviour.
4. Results demonstrated outcomes within tolerance, or Findings were raised.
5. Defects discovered are tracked to closure and retest (RES-020).
6. Tests are conducted at representative load or the load difference is analysed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Integrated test cycle | months | 24 (illustrative) | Capability-profile parameter. |
| Representative load during test | % of design IT load | As high as safely authorised (illustrative 70) | Load banks or real workload; site-specific. |

**Minimum evidence**

- Integrated test plans with safety cases
- Test records with capability-level measurements
- Defect and retest records
- Load representativeness analysis

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T3 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY; FAILED; RECOVERY; TRANSITION |
| periodCoverage | Within the cycle for each prioritised scenario. |
| independence | Witnessed by an independent party (E5). |
| mandatoryItems | Integrated test records; Safety case |
| acceptableAlternatives | Analysed real events with equivalent capability-level measurements |
| unknownEffect | US4: CG-10 cannot PASS for an outcome whose prioritised scenarios have never been integrated-tested or analysed from real events. |
| reassessmentTriggers | Major architecture change; New prioritised scenario; Cycle expiry; Real event revealing new behaviour |

**Assessment methods.** SCENARIO_EXERCISE, TEST, OBSERVATION, ANALYSIS

**Assessment procedure**

1. Review test plans, safety cases and success criteria.
2. Observe or review test execution records.
3. Verify capability-level measurements.
4. Assess load representativeness.
5. Review defect closure and retest.

**Gate mappings.** CG-10 Recovery readiness (CRITICAL); CG-09 Failure containment (SUPPORTING); CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to every in-scope Capability Instance with gate-critical outcomes.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY, FAILED, RECOVERY, TRANSITION

**Failure modes addressed.** Cross-domain interaction not revealed by component tests; Generator stable on load bank but unstable on AI load steps; Jobs fail on UPS transfer despite systems passing; Hidden shared dependency (X04)

**Testing safety.** Integrated tests are disruptive and may be hazardous; they require written authorisation from the facility owner, engineering authorities and capability owner, a safety case, permit-to-work for energised work, a defined abort authority, and communication to affected tenants. Live capability exercises (AIDCF-004 V7) require executive authorisation.

**UNKNOWN rule.** Scenarios tested only at reduced load without representativeness analysis are recorded with U5.

**Ontology classes.** TestRecord, FailureScenario, ServiceOutcome, Event · **Related controls.** MCF-RES-003, MCF-RES-014, MCF-RES-020, MCF-POW-020, MCF-THM-003

**Informative references.** NIST SP 800-84 (Guide to test, training and exercise programs for IT plans and capabilities); ISO 22301 (Business continuity management systems: requirements); AIDCF-004 (Threat, Hazard and Failure Model)

### MCF-RES-019

**Tabletop Exercises** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure decision-makers, operators and providers rehearse response to scenarios that cannot safely be tested live, including cyber-physical, compound and site-loss events.

**Requirement.** The resilience owner shall run tabletop exercises on a defined cycle covering scenarios not testable live, including at least one cyber-physical scenario (for example BMS/EPMS compromise, X05) and one compound event (X20) per cycle, with participation of crisis command, facility, IT, security and key providers. The resilience owner shall record decisions, timings, gaps and actions and shall track actions to closure.

**Assessment criteria**

1. Exercises occurred on the defined cycle with documented scenarios and objectives.
2. Each cycle includes a cyber-physical and a compound scenario.
3. Participants include crisis command, facility, IT, security and key providers.
4. Gaps and actions are recorded and tracked to closure.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Tabletop cycle | months | 6 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Exercise plans and scenarios
- Attendance records
- Exercise reports with gaps and actions
- Action tracker

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E3; E6 |
| optionalClasses | E1; E4 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | EMERGENCY; RECOVERY; FAILED |
| periodCoverage | 12 months (illustrative). |
| independence | Facilitated or observed by a party independent of the plan authors. |
| mandatoryItems | Exercise reports; Action tracker |
| acceptableAlternatives |  |
| unknownEffect | US2 for confidence; US3 if no cyber-physical scenario was ever exercised. |
| reassessmentTriggers | Crisis team change; Major incident; New scenario |

**Assessment methods.** DOCUMENT_REVIEW, OBSERVATION, INQUIRY

**Assessment procedure**

1. Review exercise schedule and scenarios.
2. Check scenario mix and participation.
3. Review reports and action closure.
4. Interview participants.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to every in-scope site and Capability Instance; exercises may be combined across sites where crisis command is shared.

**Lifecycle stages.** OPERATE · **Operating states.** EMERGENCY, RECOVERY, FAILED

**Failure modes addressed.** Decision paralysis in cyber-physical event; Provider roles unclear; Actions from exercises never closed

**Testing safety.** Tabletop exercises are non-intrusive; do not issue live commands to systems during exercises.

**UNKNOWN rule.** Tabletop results support OPERATION claims for decision processes only, not technical recovery effectiveness.

**Ontology classes.** TestRecord, FailureScenario, Action · **Related controls.** MCF-RES-021, MCF-RES-020, MCF-SEC-019, MCF-RES-003

**Informative references.** NIST SP 800-84 (Guide to test, training and exercise programs for IT plans and capabilities); ISO 22320 (Emergency management: guidelines for incident management); ISO 22301 (Business continuity management systems: requirements)

### MCF-RES-020

**Lessons and Retest** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that defects and lessons from tests, exercises and real incidents are tracked to closure, reflected in plans and designs, and verified by retest.

**Requirement.** The resilience owner shall maintain a lessons register capturing every defect and lesson from tests, exercises and incidents with owner, due date, and the plan, runbook, design or control affected. The resilience owner shall require retest or equivalent verification before closure of any lesson affecting a gate-critical safeguard and shall report overdue items to governance monthly.

**Assessment criteria**

1. All defects and lessons from the period are in the register with owner and due date.
2. Affected plans, runbooks and designs were updated.
3. Gate-critical items were closed only after retest or equivalent verification.
4. Overdue items were reported to governance.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum age of open gate-critical lesson | days | 90 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Lessons register
- Updated plan/runbook versions
- Retest records
- Governance reports

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E4; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; RECOVERY |
| periodCoverage | 12 months (illustrative). |
| independence | Assessor traces from source test/incident reports to the register. |
| mandatoryItems | Lessons register; Retest evidence for closed gate-critical items |
| acceptableAlternatives |  |
| unknownEffect | US3: unclosed gate-critical lessons condition the decision. |
| reassessmentTriggers | New test or incident report |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, RECONCILIATION

**Assessment procedure**

1. Trace defects from test, exercise and incident reports into the register.
2. Sample closed items for plan updates and retest.
3. Review overdue items and governance reporting.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all resilience tests, exercises and incidents in scope.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, RECOVERY

**Failure modes addressed.** Same defect recurring in successive tests; Lessons closed without verification

**Testing safety.** Retests follow the safety requirements of the original test control.

**UNKNOWN rule.** Items closed without verification evidence are reopened as UNKNOWN U1.

**Ontology classes.** Finding, Action, TestRecord · **Related controls.** MCF-RES-018, MCF-RES-019, MCF-RES-024, MCF-OPS-016

**Informative references.** ISO 22301 (Business continuity management systems: requirements); NIST SP 800-84 (Guide to test, training and exercise programs for IT plans and capabilities)

## RES-06 Crisis and adaptive response

### MCF-RES-021

**Crisis Command** · CORRECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure a crisis command structure with defined levels, authority, activation criteria and facilities can take timely decisions during major infrastructure and cyber-physical events.

**Requirement.** The executive sponsor shall establish a crisis command structure with strategic, tactical and operational levels, named primary and alternate role holders, activation criteria, decision authority (including authority to shed load, suspend tenants, invoke alternate capacity and order controlled shutdown), and command facilities and communication channels that remain available when site systems, corporate identity or primary communications fail. The crisis management lead shall demonstrate activation and decision timings in exercises or real events.

**Assessment criteria**

1. The command structure defines levels, roles, alternates and decision authority.
2. Activation criteria are defined and linked to monitoring and incident triggers.
3. Command facilities and communications are available independently of site systems and corporate identity.
4. Exercises or events in the period demonstrated activation within the target time and decisions within authority.
5. Decision logs were maintained.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Crisis command activation time | min from trigger | 30 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Crisis command plan
- Role and alternate roster
- Communication channel independence analysis
- Exercise/event records with timings and decision logs

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E3; E4; E6 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | EMERGENCY; FAILED; RECOVERY |
| periodCoverage | Exercises within 12 months (illustrative). |
| independence | Exercises observed by a party independent of the crisis team. |
| mandatoryItems | Exercise/event records with timings; Decision logs |
| acceptableAlternatives |  |
| unknownEffect | US3; escalates to US4 against CG-13 if no decision authority exists for controlled shutdown. |
| reassessmentTriggers | Organisational change; Communication platform change; Event post-review |

**Assessment methods.** DOCUMENT_REVIEW, SCENARIO_EXERCISE, OBSERVATION, INQUIRY

**Assessment procedure**

1. Review plan, roles and authority.
2. Check communication independence.
3. Review exercise or event timings and decision logs.
4. Interview role holders on authority.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to every in-scope organisation and site.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** EMERGENCY, FAILED, RECOVERY

**Failure modes addressed.** No one authorised to order controlled shutdown; Crisis bridge relies on failed identity provider; Alternate role holders untrained

**Testing safety.** Exercises shall be clearly labelled to prevent confusion with real events; live notifications to customers or authorities during exercises require prior approval.

**UNKNOWN rule.** If command communications depend on an unanalysed service, record U10 against crisis command availability.

**Ontology classes.** Safeguard, Action, Event · **Related controls.** MCF-RES-022, MCF-RES-012, MCF-OPS-014, MCF-GOV-002

**Informative references.** ISO 22320 (Emergency management: guidelines for incident management); ISO 22301 (Business continuity management systems: requirements); NIST SP 800-61 Rev. 3 (Incident response recommendations)

### MCF-RES-022

**Stakeholder Communications** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure timely, accurate communication to customers, tenants, regulators, providers and staff during disruption, consistent with contractual and regulatory notification obligations.

**Requirement.** The crisis management lead shall maintain a communications plan listing stakeholders, notification obligations and deadlines (contractual and regulatory), approved message templates, approval authority and channels that remain available during site and identity failures. The crisis management lead shall record each notification issued during events and exercises with timestamp and approver and shall review timeliness against obligations.

**Assessment criteria**

1. A communications plan lists stakeholders, obligations, deadlines and channels.
2. Templates and approval authorities are defined.
3. Notifications in events and exercises in the period met deadlines.
4. Channels are available independently of site and corporate identity systems.

**Minimum evidence**

- Communications plan
- Obligation register
- Notification logs

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | EMERGENCY; RECOVERY |
| periodCoverage | 12 months (illustrative). |
| independence | Assessor reconciles logs with obligation deadlines. |
| mandatoryItems | Notification logs; Obligation register |
| acceptableAlternatives |  |
| unknownEffect | US2; US3 where regulatory notification timeliness cannot be established. |
| reassessmentTriggers | New regulatory obligation; New customer contract |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Review the plan and obligation register.
2. Reconcile notification logs with deadlines.
3. Check channel independence.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to every in-scope organisation.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** EMERGENCY, RECOVERY

**Failure modes addressed.** Missed regulatory notification; Inconsistent customer messaging; Communication channel lost with site

**Testing safety.** Exercise messages shall be marked as exercise and not sent externally without approval.

**UNKNOWN rule.** Obligations without a known deadline are recorded as U9 pending legal interpretation.

**Ontology classes.** Action, Event, Interface · **Related controls.** MCF-RES-021, MCF-GOV-019, MCF-GOV-022, MCF-SUP-007

**Informative references.** ISO 22320 (Emergency management: guidelines for incident management); Regulation (EU) 2022/2554 (Digital Operational Resilience Act); ISO 22301 (Business continuity management systems: requirements)

### MCF-RES-023

**Emergency Change** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure changes made under emergency conditions are authorised by defined emergency authority, minimal, recorded, and reconciled back to baseline after the event.

**Requirement.** The change authority shall define an emergency change procedure stating who may authorise emergency changes to infrastructure, OT and control-plane systems, the minimum record to be captured at the time, and the deadline for retrospective review. The recovery manager shall ensure every emergency change is retrospectively reviewed, either reverted or formalised, and that baselines and evidence are updated, and shall report unreconciled emergency changes.

**Assessment criteria**

1. An emergency change procedure defines authority, minimum records and retrospective review deadline.
2. Emergency changes in the period were authorised by defined authority.
3. Each emergency change was reviewed within the deadline and reverted or formalised.
4. Baselines (NET-022, OPS-017) were updated after formalised emergency changes.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Emergency change retrospective review deadline | working days | 5 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Emergency change procedure
- Emergency change records
- Retrospective reviews
- Baseline updates

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | EMERGENCY; RECOVERY |
| periodCoverage | 12 months (illustrative). |
| independence | Assessor identifies emergency changes from configuration drift and logs, not only from the change system. |
| mandatoryItems | Emergency change records; Retrospective reviews |
| acceptableAlternatives |  |
| unknownEffect | US3; affects CG-14 SUPPORTING evaluation. |
| reassessmentTriggers | Major incident; Procedure change |

**Assessment methods.** SAMPLING, RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Review procedure.
2. Identify emergency changes from logs and drift.
3. Check authorisation and retrospective review.
4. Verify baseline updates.

**Gate mappings.** CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all infrastructure, OT and control-plane systems in scope.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** EMERGENCY, RECOVERY

**Failure modes addressed.** Emergency bypass left in place; Unrecorded emergency configuration becoming latent fault; Emergency authority exceeded

**Testing safety.** Records-based.

**UNKNOWN rule.** Emergency changes identified from drift with no record are Findings; if logs are unavailable, record U2.

**Ontology classes.** Action, Event, ArchitectureSnapshot · **Related controls.** MCF-OPS-018, MCF-OPS-019, MCF-NET-022, MCF-SEC-022

**Informative references.** ISO 22301 (Business continuity management systems: requirements); NIST SP 800-61 Rev. 3 (Incident response recommendations)

### MCF-RES-024

**Post-Event Adaptation** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that after material events the organisation analyses root causes and systemic contributors, adapts design, operations and assurance, and triggers reassessment of affected claims.

**Requirement.** The resilience owner shall require a post-event review within a defined time after every material event, covering timeline, root and contributing causes, safeguard performance against expectation, recovery performance against tolerance, and required adaptations to design, operations, controls and evidence. The resilience owner shall raise reassessment triggers for affected controls and gate results and shall track adaptations to completion.

**Assessment criteria**

1. Post-event reviews were completed for every material event within the defined time.
2. Reviews compare safeguard and recovery performance with expectation and tolerance.
3. Adaptations are tracked to completion.
4. Reassessment triggers were raised for affected controls and gates.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Post-event review deadline | days | 30 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Post-event review reports
- Adaptation tracker
- Reassessment trigger records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3; E7 |
| optionalClasses | E6 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | RECOVERY; NORMAL |
| periodCoverage | 24 months (illustrative). |
| independence | Reviews facilitated by a party independent of the teams involved. |
| mandatoryItems | Post-event reviews; Reassessment trigger records |
| acceptableAlternatives |  |
| unknownEffect | US3: unreviewed events may invalidate existing evidence. |
| reassessmentTriggers | Material event |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, INQUIRY

**Assessment procedure**

1. List material events from incident systems.
2. Check review completion and content.
3. Trace adaptations and reassessment triggers.

**Gate mappings.** CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all material events affecting in-scope outcomes.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** RECOVERY, NORMAL

**Failure modes addressed.** Repeat incidents from unaddressed systemic causes; Evidence relied on despite invalidating event

**Testing safety.** Post-event reviews are non-intrusive; any reproduction of the event to confirm causes is a test governed by RES-018 authorisation requirements.

**UNKNOWN rule.** Events without a completed review mark the evidence of affected controls as STALE until reviewed.

**Ontology classes.** Event, ReassessmentTrigger, Finding, Action · **Related controls.** MCF-RES-020, MCF-OPS-015, MCF-EVA-022, MCF-OPS-016

**Informative references.** ISO 22316 (Organizational resilience: principles and attributes); ISO 22301 (Business continuity management systems: requirements); NIST SP 800-61 Rev. 3 (Incident response recommendations)
