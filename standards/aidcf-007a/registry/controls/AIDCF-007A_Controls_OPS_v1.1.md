# AIDCF-007A Control Catalogue — OPS Building Operations and Service Management

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-OPS](../../../aidcf-018-domain-guides/AIDCF-018-OPS_Building_Operations_and_Service_Management_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-OPS-001](#mcf-ops-001) | 24x7 Coverage | PREVENTIVE | OPERATION | AL4 | — | CG-13, CG-10 |
| [MCF-OPS-002](#mcf-ops-002) | Role Clarity | DIRECTIVE | IMPLEMENTATION | AL3 | CG-13 | CG-14 |
| [MCF-OPS-003](#mcf-ops-003) | Shift Handover | PREVENTIVE | OPERATION | AL4 | — | CG-04, CG-14 |
| [MCF-OPS-004](#mcf-ops-004) | Competence and Authorisation | PREVENTIVE | OPERATION | AL4 | CG-04 | CG-13 |
| [MCF-OPS-005](#mcf-ops-005) | Standard Operating Procedures | DIRECTIVE | IMPLEMENTATION | AL3 | — | CG-10, CG-13, CG-14 |
| [MCF-OPS-006](#mcf-ops-006) | Method Statements | PREVENTIVE | OPERATION | AL4 | CG-14 | CG-04 |
| [MCF-OPS-007](#mcf-ops-007) | Permit to Work | PREVENTIVE | OPERATION | AL4 | CG-04 | — |
| [MCF-OPS-008](#mcf-ops-008) | Lockout and Tagout | PREVENTIVE | OPERATION | AL4 | CG-04 | — |
| [MCF-OPS-009](#mcf-ops-009) | Maintenance Strategy | DIRECTIVE | DESIGN | AL2 | — | CG-05, CG-06 |
| [MCF-OPS-010](#mcf-ops-010) | Condition Monitoring | DETECTIVE | OPERATION | AL4 | — | CG-05, CG-06 |
| [MCF-OPS-011](#mcf-ops-011) | Calibration | PREVENTIVE | OPERATION | AL4 | — | CG-07 |
| [MCF-OPS-012](#mcf-ops-012) | Deferred Maintenance | CORRECTIVE | OPERATION | AL4 | — | CG-05, CG-06, CG-13 |
| [MCF-OPS-013](#mcf-ops-013) | Alarm Rationalisation | DETECTIVE | OPERATION | AL4 | CG-07 | CG-06, CG-05 |
| [MCF-OPS-014](#mcf-ops-014) | Incident Response | CORRECTIVE | OPERATION | AL4 | — | CG-10, CG-13 |
| [MCF-OPS-015](#mcf-ops-015) | Root Cause Analysis | CORRECTIVE | OPERATION | AL4 | — | CG-09 |
| [MCF-OPS-016](#mcf-ops-016) | Problem Elimination | CORRECTIVE | EFFECTIVENESS | AL5 | — | CG-14 |
| [MCF-OPS-017](#mcf-ops-017) | Configuration Baseline | PREVENTIVE | IMPLEMENTATION | AL3 | CG-14 | CG-02, CG-07 |
| [MCF-OPS-018](#mcf-ops-018) | Change Assessment | PREVENTIVE | OPERATION | AL4 | CG-14 | CG-03 |
| [MCF-OPS-019](#mcf-ops-019) | Temporary Configuration | PREVENTIVE | OPERATION | AL4 | — | CG-14, CG-07, CG-04 |
| [MCF-OPS-020](#mcf-ops-020) | Rollback and Validation | CORRECTIVE | EFFECTIVENESS | AL5 | CG-14 | CG-10 |
| [MCF-OPS-021](#mcf-ops-021) | Capacity Review | DETECTIVE | OPERATION | AL4 | — | CG-05, CG-06 |
| [MCF-OPS-022](#mcf-ops-022) | Service Level Monitoring | DETECTIVE | OPERATION | AL4 | — | — |
| [MCF-OPS-023](#mcf-ops-023) | Resource Balancing | PREVENTIVE | OPERATION | AL4 | — | CG-05, CG-06, CG-09 |
| [MCF-OPS-024](#mcf-ops-024) | Operational Reporting | DIRECTIVE | OPERATION | AL4 | — | CG-13 |

## OPS-01 Operating model and staffing

### MCF-OPS-001

**24x7 Coverage** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Competent and authorised staff are present or available within response time, every hour of every day, in the numbers and disciplines needed to perform the time-critical tasks of the emergency procedures within the time-to-impact of the failures they address.

**Requirement.** The operations manager shall define minimum staffing per shift and per discipline (electrical, mechanical/thermal, controls/BMS, NOC/IT infrastructure, security) derived from an emergency task analysis that lists the time-critical manual actions in each EOP (for example manual generator start or transfer, CDU failover, leak isolation, load shedding) and compares their completion time with the time-to-impact from MCF-DEP-003. The operations manager shall roster to that minimum, record every shift that falls below it and the compensating measures, and shall define on-call response times for specialists not on site.

**Assessment criteria**

1. An emergency task analysis exists linking EOP time-critical actions to time-to-impact and required staff.
2. Minimum staffing per shift and discipline is derived from that analysis and approved.
3. Rosters and time-and-attendance records for the period show the minimum was met, or each shortfall is recorded with compensating measures.
4. On-call specialist response times are defined and met in call-outs during the period.
5. Fatigue limits (maximum shift length, consecutive shifts) are defined and adhered to.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Minimum on-site staff per shift | persons by discipline | Site-specific (no default) | Derived from emergency task analysis; there is no universal staffing ratio. |
| On-call specialist attendance time | minutes | 60 | Illustrative; must be shorter than the time available after on-site staff stabilise the event. |
| Maximum shift length | hours | 12 | Illustrative; set with reference to HSE HSG256 guidance and local working-time law. |

**Minimum evidence**

- Emergency task analysis.
- Approved minimum staffing matrix.
- Rosters and attendance records for the period.
- Call-out logs with response times.
- Shortfall records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; EMERGENCY; MAINTENANCE |
| periodCoverage | At least 3 months of rosters including night, weekend and holiday periods. |
| independence | Attendance records from access-control or time systems, not rosters alone. |
| mandatoryItems | Emergency task analysis; Attendance records against minimum |
| acceptableAlternatives | For unstaffed or lightly staffed sites (for example edge inference), a remote NOC with demonstrated dispatch times plus automated safe-state design may substitute, if the task analysis shows no manual action is required within the time-to-impact. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-13, CG-10 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Change in shift pattern or headcount; New system with manual emergency actions; Change in time-to-impact (density increase); Incident where response was delayed |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, SAMPLING, ANALYSIS, OBSERVATION

**Assessment procedure**

1. Obtain the emergency task analysis and staffing matrix.
2. Check the analysis against EOP time-critical steps and DEP-003 time-to-impact.
3. Reconcile a sample of shifts (including nights and holidays) from access-control records to the minimum.
4. Sample call-outs and measure response times.
5. Observe a shift change and staffing on site during an unannounced visit where permitted.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to all staffed facilities and NOCs supporting the Capability Instance; for provider-operated facilities assessed via MCF-DEP-018 evidence.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY

**Failure modes addressed.** Night shift below minimum when a generator fails to start; Specialist call-out takes longer than thermal ride-through; Fatigue-related operator error; Concurrent events exceed staff capacity

**Testing safety.** Unannounced observation shall not interfere with operations; staffing shall not be reduced to test resilience.

**UNKNOWN rule.** Missing attendance evidence for night and weekend shifts is U1, US3; escalate to US4 if a CG-05/06/10 criterion depends on manual action within ride-through.

**Ontology classes.** Resource, RequiredFunction, OperatingState · **Related controls.** MCF-DEP-008, MCF-OPS-004, MCF-OPS-005, MCF-DEP-003

**Informative references.** Uptime Institute Tier Standard: Operational Sustainability; EN 50600-3-1 (management and operational information); HSE HSG256 (managing shift work)

### MCF-OPS-002

**Role Clarity** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** For every Required Function, dependency and operating state, it is clear who operates, who maintains, who monitors, who may approve change, who responds to alarms and who holds emergency decision authority, including across facilities, IT/NOC, tenant and provider teams.

**Requirement.** The operations manager shall maintain a responsibility and authority matrix for every Required Function and material dependency across NORMAL, MAINTENANCE, EMERGENCY and RECOVERY states, naming the role and current holder (and deputy) for operation, maintenance, monitoring, change approval, alarm response and emergency decisions (for example authority to transfer to generator, shed load, power-cap or drain a cluster, isolate a cooling loop, or invoke an EOP). The matrix shall be consistent with GOV-02 accountability and with provider shared-responsibility records (MCF-DEP-018).

**Assessment criteria**

1. A matrix covers every Required Function and material dependency for the four states.
2. Each role has a named current holder and deputy.
3. Emergency decision authorities are explicit, including cross-team decisions (facilities ordering IT load reduction and vice versa).
4. The matrix is consistent with GOV-02 and DEP-018 records.
5. Interviewed role holders can state their responsibilities and authorities consistently with the matrix.

**Minimum evidence**

- Responsibility and authority matrix.
- Named role holder list with deputies.
- Cross-reference to GOV-02 and DEP-018.
- Interview records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY; RECOVERY |
| periodCoverage | Current. |
| independence | Interviews performed by the assessor with role holders selected by the assessor. |
| mandatoryItems | Responsibility and authority matrix with named holders |
| acceptableAlternatives |  |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-13 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-14 require gate-level evaluation. |
| reassessmentTriggers | Organisational change; Role holder change; New function or provider; Incident with authority confusion |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY, RECONCILIATION

**Assessment procedure**

1. Obtain the matrix and holder list.
2. Check coverage against Required Functions and dependencies.
3. Reconcile with GOV-02 and DEP-018.
4. Interview a sample of holders using scenarios (for example cooling loss at sustained AI load).
5. Record gaps and inconsistencies.

**Gate mappings.** CG-13 Responsibility and authority (CRITICAL); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all assessments.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY, RECOVERY

**Failure modes addressed.** No one authorised to order cluster power-capping during cooling loss; Facilities and NOC each assume the other responds; Deputy undefined at night

**Testing safety.** Interviews only.

**UNKNOWN rule.** A Required Function with no identifiable emergency decision authority is US4 (CG-13 criterion).

**Ontology classes.** RequiredFunction, Dependency, OperatingState · **Related controls.** MCF-GOV-005, MCF-GOV-006, MCF-DEP-018, MCF-RES-021

**Informative references.** ISO/IEC 20000-1 (service management system requirements); EN 50600-3-1 (management and operational information); ISO 22320 (emergency management: incident management)

### MCF-OPS-003

**Shift Handover** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Situational awareness is transferred completely at every shift change: plant and system state, active alarms, open permits and isolations, temporary configurations, deferred maintenance, degraded redundancy, in-progress work and expected events.

**Requirement.** The shift lead shall conduct and record a structured handover at each shift change using a defined template covering: current operating state per system and redundancy level, active and standing alarms, open permits to work and isolations, temporary configurations and overrides, work in progress and planned work, deferred maintenance with risk, provider or tenant events, and expected events (deliveries, tests, high-load periods). Outgoing and incoming leads shall both sign, and the incoming lead shall verify critical items at the BMS/EPMS/NOC consoles.

**Assessment criteria**

1. A handover template covering the listed elements exists.
2. Handover records exist for the sampled shifts, signed by both leads.
3. Open permits and temporary configurations in handover records reconcile with the permit and temporary-configuration registers at that time.
4. Incoming leads verified critical items at consoles (record or observation).

**Minimum evidence**

- Handover template.
- Handover records for sample.
- Permit and temporary-configuration registers for the same times.
- Observation of a handover.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | Sample of at least 20 handovers over 3 months (illustrative). |
| independence | Assessor reconciles handover content to registers. |
| mandatoryItems | Handover records; Reconciliation to permit register |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-04, CG-14 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Change to shift pattern; Incident attributable to handover |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, OBSERVATION, SAMPLING

**Assessment procedure**

1. Obtain template and sample records.
2. Reconcile with permit and temporary-configuration registers.
3. Observe a live handover.
4. Record omissions.

**Gate mappings.** CG-04 Life safety and hazardous energy (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all shift-based operations, including NOC.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY

**Failure modes addressed.** Open isolation not handed over and re-energised; Alarm inhibit forgotten; Degraded redundancy unknown to incoming shift

**Testing safety.** Observation shall not distract operators during the handover.

**UNKNOWN rule.** Missing handover records is U1, US3.

**Ontology classes.** OperatingState, Event, Safeguard · **Related controls.** MCF-OPS-007, MCF-OPS-019, MCF-OPS-012

**Informative references.** HSE HSG48 (reducing error and influencing behaviour); Uptime Institute Tier Standard: Operational Sustainability

### MCF-OPS-004

**Competence and Authorisation** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Only people assessed as competent, and formally authorised for the task and system, perform hazardous or consequential work, including HV/LV switching, work on battery systems, liquid-cooling and pressurised fluid systems, refrigerants, and control-system changes.

**Requirement.** The operations manager shall maintain a competence framework defining required knowledge, skills and assessment for each task class, and an authorisation register recording each person's authorisations (for example authorised person and competent person for HV/LV systems, refrigerant handling certification where legally required, liquid-cooling and CDU work, BMS/EPMS engineering), their scope, expiry and assessor. The operations manager shall verify contractor competence and authorisation before work and shall ensure permits (MCF-OPS-007) are issued only to authorised persons.

**Assessment criteria**

1. Competence framework covers all hazardous and consequential task classes.
2. Authorisation register records scope, expiry and assessor for each person.
3. No authorisation in the sample has expired.
4. Permits in the sample were issued to and received by persons authorised for that task.
5. Contractor competence was verified before work for sampled jobs.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Authorisation revalidation interval | months | 36 | Illustrative; set by site safety rules and legal requirements. |

**Minimum evidence**

- Competence framework.
- Authorisation register.
- Training and assessment records.
- Permit sample cross-referenced to register.
- Contractor verification records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | 12 months of permits. |
| independence | Assessor cross-references permits to register independently. |
| mandatoryItems | Authorisation register; Permit-to-authorisation reconciliation |
| acceptableAlternatives |  |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-04 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-13 require gate-level evaluation. |
| reassessmentTriggers | New task class or system; Incident involving competence; Change of contractor |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, SAMPLING, INQUIRY

**Assessment procedure**

1. Obtain framework and register.
2. Sample permits and reconcile issuers and receivers to authorisations.
3. Check expiry and scope.
4. Sample contractor jobs for pre-work verification.
5. Interview a sample of authorised persons on scope.

**Gate mappings.** CG-04 Life safety and hazardous energy (CRITICAL); CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to all hazardous and consequential work in the boundary, by staff or contractors.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE, DECOMMISSION · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY, RECOVERY

**Failure modes addressed.** Unauthorised person performs HV switching; Contractor without liquid-cooling competence breaks a pressurised loop; Expired authorisation

**Testing safety.** Assessment is documentary and interview-based; no competence demonstration shall involve live hazardous work.

**UNKNOWN rule.** Inability to verify authorisation of persons receiving hazardous-energy permits is US4 (CG-04 critical).

**Ontology classes.** Resource, Safeguard, Hazard · **Related controls.** MCF-OPS-007, MCF-OPS-008, MCF-GOV-023, MCF-DEP-008

**Informative references.** BS EN 50110-1 (operation of electrical installations); NFPA 70E (electrical safety in the workplace); ISO 45001 (occupational health and safety management systems); HSE HSG85 (electricity at work: safe working practices)

## OPS-02 Procedure and work control

### MCF-OPS-005

**Standard Operating Procedures** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Routine, alarm-response and emergency operations on critical infrastructure are performed from controlled, technically reviewed and current procedures (SOPs, alarm response procedures, EOPs) that match the as-built systems and are available at the point of use.

**Requirement.** The operations manager shall maintain a controlled procedure set comprising SOPs for routine operation, alarm response procedures for critical alarms, and EOPs for each credible emergency scenario (including utility loss, generator failure to start, UPS failure, cooling loss at sustained AI load, CDU or secondary-loop failure, liquid leak, fire alarm and suppression interfaces, BMS/EPMS loss, and loss of NOC). Each procedure shall have an owner, technical reviewer, version and review date, shall be validated against the as-built system by walkthrough before issue, and shall be available at the point of use including when the BMS and IT systems are unavailable.

**Assessment criteria**

1. The procedure set includes EOPs for each scenario in the RES-01 scenario list and alarm response procedures for each critical alarm.
2. Each procedure has owner, reviewer, version and review date within the interval.
3. A sample of procedures matches as-built equipment identifiers, valve and breaker designations and current setpoints.
4. Procedures are available in hard copy or offline form at points of use.
5. Walkthrough validation is recorded for procedures issued or revised in the period.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Procedure review interval | months | 12 | Illustrative. |

**Minimum evidence**

- Procedure register.
- Sample procedures.
- As-built cross-check records.
- Walkthrough validation records.
- Point-of-use inspection.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY; RECOVERY |
| periodCoverage | Current. |
| independence | As-built cross-check by assessor during walk-down. |
| mandatoryItems | Procedure register with EOP coverage; As-built cross-check |
| acceptableAlternatives | Electronic procedures on a system with independent power and offline availability. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-10, CG-13, CG-14 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Change to equipment or configuration; Incident revealing procedure gap; Review interval elapsed |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, SAMPLING, OBSERVATION

**Assessment procedure**

1. Obtain register and map EOPs to scenarios.
2. Sample procedures and check control metadata.
3. Walk down sampled procedures against equipment.
4. Inspect point-of-use availability.
5. Observe an operator walk through an EOP.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-13 Responsibility and authority (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all critical infrastructure operations.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY, RECOVERY

**Failure modes addressed.** EOP references removed equipment; No EOP for CDU failure; Procedures only on unavailable intranet; Operator error during alarm flood (scenario X11)

**Testing safety.** Walk-downs follow site safety rules; walkthroughs shall not operate equipment.

**UNKNOWN rule.** Missing EOP for a scenario prioritised under CG-05/06/10 is a Finding (NONCONFORMING); inability to verify as-built match is US3.

**Ontology classes.** Safeguard, FailureScenario, OperatingState · **Related controls.** MCF-OPS-006, MCF-OPS-013, MCF-RES-003, MCF-POW-023

**Informative references.** Uptime Institute Tier Standard: Operational Sustainability; EN 50600-3-1 (management and operational information); ISO 22320 (emergency management: incident management)

### MCF-OPS-006

**Method Statements** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Non-routine work on critical infrastructure is executed from a task-specific method of procedure (MOP) that states the exact steps, hold points, isolation points, expected readings, redundancy exposure during the work, and back-out steps, so that maintenance and change do not cause outages.

**Requirement.** The maintenance manager shall require an approved MOP for every non-routine task on critical infrastructure, including: scope and affected assets; the operating state and redundancy level during each step (for example N during work on one of N+1 UPS modules); preconditions (for example job checkpoint or workload drain agreed with the platform owner, spare on hand, weather); step-by-step actions with hold points and expected indications; isolation and LOTO points; back-out steps; communications plan; and approvals by engineering, operations and change control (MCF-OPS-018). The MOP shall be executed as written with each step signed off and deviations stopped and escalated.

**Assessment criteria**

1. Every non-routine task in the sample had an approved MOP before work.
2. MOPs state redundancy exposure per step and preconditions including workload coordination.
3. Executed MOPs show step sign-off; deviations were stopped and escalated.
4. MOPs were reviewed by engineering and operations and linked to an approved change.
5. Back-out steps are present for each irreversible step boundary.

**Minimum evidence**

- MOP register.
- Sample of approved and executed MOPs.
- Linked change records.
- Deviation records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | MAINTENANCE; TRANSITION |
| periodCoverage | 12 months of non-routine work. |
| independence | Sample selected by the assessor from work-order system, not from MOP register. |
| mandatoryItems | Executed MOPs with sign-off; Linked approvals |
| acceptableAlternatives |  |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-14 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-04 require gate-level evaluation. |
| reassessmentTriggers | Incident during maintenance; New equipment type |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, RECONCILIATION, OBSERVATION

**Assessment procedure**

1. Extract non-routine work orders for the period.
2. Reconcile each to an approved MOP and change.
3. Check content against required elements.
4. Review executed sign-off and deviations.
5. Observe a MOP execution where scheduled.

**Gate mappings.** CG-14 Change control (CRITICAL); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to non-routine work on critical infrastructure.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE, DECOMMISSION · **Operating states.** MAINTENANCE, TRANSITION, DEGRADED

**Failure modes addressed.** Maintenance removes hidden shared dependency (scenario X04); Wrong breaker opened; Work during training run without checkpoint; No back-out when step fails

**Testing safety.** Observation of MOP execution only from a safe position as directed by the person in charge; observers shall not operate equipment.

**UNKNOWN rule.** Non-routine work without a traceable MOP is a Finding; missing work-order data for the sample period is US4 (CG-14 critical).

**Ontology classes.** Safeguard, OperatingState, Event · **Related controls.** MCF-OPS-007, MCF-OPS-018, MCF-OPS-020, MCF-THM-023

**Informative references.** Uptime Institute Tier Standard: Operational Sustainability; ISO 45001 (occupational health and safety management systems); EN 50600-3-1 (management and operational information)

### MCF-OPS-007

**Permit to Work** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Hazardous work is authorised, controlled, coordinated and handed back through a permit-to-work system so that hazardous energy, fluids, confined spaces, hot work and work at height are controlled and conflicting work is prevented.

**Requirement.** The facility operator shall operate a permit-to-work system for hazardous work, including electrical (HV and LV), battery and DC systems, hot work, confined spaces (for example tanks, pits, trenches, plenums), work at height, pressurised and liquid-cooling systems, refrigerants and fire-suppression systems. Each permit shall identify the work, hazards, isolations (cross-referenced to LOTO), precautions, issuer and receiver (both authorised under MCF-OPS-004), validity period, and cross-references to other live permits in the same system. Permits shall be suspended at shift change unless re-validated, and closed only after hand-back confirms the system is safe to return to service.

**Assessment criteria**

1. Permit types cover all hazardous work categories present on site.
2. Sampled permits are complete and issuer and receiver are authorised.
3. Conflicting permits in the same system were cross-referenced and coordinated.
4. Permits were suspended or re-validated at shift change.
5. Hand-back records confirm the system state before return to service.
6. Periodic audits of live permits at the worksite were performed and findings closed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Permit audit frequency | audits per month | 4 | Illustrative. |

**Minimum evidence**

- Permit procedure.
- Permit register and sample permits.
- Cross-reference to LOTO records.
- Worksite permit audits.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | MAINTENANCE; EMERGENCY; NORMAL |
| periodCoverage | 12 months of permits. |
| independence | Worksite verification by assessor or HSE function. |
| mandatoryItems | Permit sample; Worksite audit records |
| acceptableAlternatives |  |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-04 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. |
| reassessmentTriggers | Safety incident or near miss; New hazard type; Change of permit system |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, INSPECTION, OBSERVATION

**Assessment procedure**

1. Obtain permit procedure and register.
2. Sample permits across types.
3. Check completeness, authorisation, cross-reference and hand-back.
4. Inspect live permits at worksites.
5. Review audit findings.

**Gate mappings.** CG-04 Life safety and hazardous energy (CRITICAL)

**Applicability.** Applies to all hazardous work in the boundary including contractors and provider staff in owner spaces.

**Lifecycle stages.** BUILD, COMMISSION, OPERATE, CHANGE, DECOMMISSION · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY, RECOVERY

**Failure modes addressed.** Conflicting work on same electrical system; Confined-space entry without permit; Liquid loop opened while pressurised; System returned to service before hand-back

**Testing safety.** Worksite inspection only under escort of the permit issuer; assessors shall not enter the permit boundary unless included on the permit.

**UNKNOWN rule.** Missing permit records for hazardous work in the period is US4 (CG-04 critical).

**Ontology classes.** Safeguard, Hazard, Event · **Related controls.** MCF-OPS-004, MCF-OPS-008, MCF-OPS-003, MCF-PHY-024

**Informative references.** HSE HSG250 (guidance on permit-to-work systems); ISO 45001 (occupational health and safety management systems); NFPA 70E (electrical safety in the workplace); BS EN 50110-1 (operation of electrical installations)

### MCF-OPS-008

**Lockout and Tagout** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** All hazardous energy sources (electrical including back-feeds and DC/battery sources, stored energy in capacitors and UPS, mechanical, hydraulic and pneumatic, pressurised coolant, thermal) are isolated, locked, tagged and proven dead or depressurised before work, and restored only under control.

**Requirement.** The facility operator shall define LOTO procedures for each equipment class that identify every energy source (including generator, UPS and battery back-feeds, BESS, capacitors, CDU pumps, pressurised secondary loops and facility water), the isolation points, locking devices, and the method to prove isolation (test-before-touch with a proven tester, pressure and temperature verification). Each worker shall apply a personal lock, group lockboxes shall be used for multi-worker jobs, and restoration shall follow a verified sequence. The facility operator shall audit LOTO practice at the profile interval.

**Assessment criteria**

1. Equipment-specific LOTO procedures identify all energy sources including back-feeds and stored energy.
2. Sampled jobs have LOTO records with personal locks, proving tests and restoration sign-off.
3. Testers are proven before and after use (live-dead-live) and are in calibration.
4. LOTO audits were performed at the interval and findings closed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| LOTO field audit interval | months | 3 | Illustrative. |

**Minimum evidence**

- Equipment LOTO procedures.
- LOTO records for sampled jobs.
- Tester calibration records.
- Audit reports.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | MAINTENANCE; EMERGENCY |
| periodCoverage | 12 months. |
| independence | Field audit by HSE or a person independent of the work team. |
| mandatoryItems | Equipment-specific LOTO procedures; LOTO records for sampled hazardous jobs |
| acceptableAlternatives |  |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-04 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. |
| reassessmentTriggers | Near miss or injury; New equipment with stored energy; Procedure change |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, OBSERVATION, INSPECTION

**Assessment procedure**

1. Obtain procedures and verify energy-source identification against SLDs and P&IDs for a sample.
2. Sample LOTO records.
3. Check tester calibration.
4. Observe a LOTO application from a safe position.
5. Review audits.

**Gate mappings.** CG-04 Life safety and hazardous energy (CRITICAL)

**Applicability.** Applies to all work requiring isolation of hazardous energy.

**Lifecycle stages.** BUILD, COMMISSION, OPERATE, DECOMMISSION · **Operating states.** MAINTENANCE, EMERGENCY, RECOVERY

**Failure modes addressed.** Back-feed from UPS output energises isolated busway; Battery DC source not isolated; Pressurised coolant released on disconnection; Isolation removed by another worker

**Testing safety.** Assessors shall only observe; they shall never apply, remove or test locks or test-before-touch themselves.

**UNKNOWN rule.** LOTO procedures not identifying back-feed or stored-energy sources is a Finding; missing LOTO records is US4 (CG-04 critical).

**Ontology classes.** Safeguard, Hazard, AssetInstance · **Related controls.** MCF-OPS-007, MCF-OPS-004, MCF-POW-012, MCF-THM-020

**Informative references.** OSHA 29 CFR 1910.147 (control of hazardous energy); NFPA 70E (electrical safety in the workplace); BS EN 50110-1 (operation of electrical installations); ISO 14118 (safety of machinery: prevention of unexpected start-up)

## OPS-03 Maintenance and reliability

### MCF-OPS-009

**Maintenance Strategy** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Each critical asset class has a maintenance strategy (preventive, predictive, condition-based or run-to-failure) justified by its failure modes and consequence, aligned with OEM requirements and recognised practice, and executable without exceeding the redundancy available in the MAINTENANCE state.

**Requirement.** The maintenance manager shall define and approve a maintenance strategy for each critical asset class (including MV/LV switchgear and protection, transformers, UPS and batteries, generators and fuel systems, busways and PDUs, chillers, CRAH/fan walls, CDUs and secondary loops, pumps, cooling towers or dry coolers, BMS/EPMS, fire detection and suppression, and IT infrastructure hardware) stating tasks, intervals, basis (OEM, recognised practice, reliability analysis), and the operating state and redundancy level during each task. The capability owner shall confirm that each maintenance configuration leaves capacity sufficient for the declared load, or that maintenance windows are coordinated with workload reduction.

**Assessment criteria**

1. A maintenance strategy exists per critical asset class with stated basis.
2. Intervals are consistent with OEM requirements or deviations are justified.
3. Each task states the redundancy level during the task and the capacity check for declared load.
4. Run-to-failure decisions are limited to items whose failure is tolerable and are approved.
5. The strategy is approved by a competent engineer.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Generator load test frequency | per year | Per NFPA 110 or site standard (no default) | Set from the adopted standard and OEM requirements. |

**Minimum evidence**

- Maintenance strategy documents.
- OEM maintenance requirements.
- Maintenance-state capacity checks.
- Approval records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | MAINTENANCE; NORMAL |
| periodCoverage | Current approved version. |
| independence | Engineering approval independent of the maintenance contractor. |
| mandatoryItems | Maintenance strategy per critical class with capacity check |
| acceptableAlternatives | An RCM analysis record may substitute for a narrative strategy. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-05, CG-06 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | New asset class; OEM requirement change; Failure revealing strategy gap; Load increase reducing maintenance headroom |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Obtain strategies.
2. Check coverage of critical classes.
3. Compare intervals with OEM requirements.
4. Check maintenance-state capacity analyses against current load.
5. Check approvals.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to all critical asset classes.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Maintenance on one CDU leaves insufficient capacity at current AI load; Battery maintenance interval exceeded; Protection relays never tested

**Testing safety.** Desk-based.

**UNKNOWN rule.** No maintenance-state capacity check for a redundant group is US3; US4 where CG-05 or CG-06 maintenance-state criteria rely on it.

**Ontology classes.** AssetInstance, OperatingState, CapacityAssertion, Safeguard · **Related controls.** MCF-POW-022, MCF-THM-023, MCF-OPS-010, MCF-OPS-012

**Informative references.** NFPA 70B (electrical equipment maintenance); NFPA 110 (emergency and standby power systems); IEC 60300-3-11 (reliability centred maintenance); SAE JA1011 (RCM evaluation criteria); ISO 55001 (asset management systems)

### MCF-OPS-010

**Condition Monitoring** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Deterioration of critical assets is detected before functional failure through defined condition-monitoring techniques with thresholds and actions.

**Requirement.** The maintenance manager shall operate condition monitoring for critical assets using techniques appropriate to their failure modes, for example infrared thermography of electrical connections, partial discharge monitoring on MV equipment, dissolved gas and oil analysis on transformers, battery impedance or conductance and temperature monitoring, vibration analysis on pumps, fans and chillers, coolant quality monitoring (conductivity, pH, inhibitor and biocide levels, particulates) on liquid-cooling loops, and filter differential pressure. Each technique shall have defined thresholds and response actions, and exceedances shall generate work orders.

**Assessment criteria**

1. Techniques are defined per critical asset class aligned to failure modes.
2. Measurements were taken at the defined frequency in the period.
3. Thresholds and actions are defined; exceedances generated work orders that were completed.
4. Coolant quality for liquid-cooled systems is within the OEM-specified envelope or deviations were actioned.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Thermography frequency for critical switchgear and busway | per year | 1 | Illustrative; NFPA 70B provides guidance. |
| Coolant quality sampling interval | weeks | 4 | Illustrative; set from CDU and cold-plate OEM requirements. |

**Minimum evidence**

- Condition monitoring plan.
- Measurement records and reports.
- Threshold definitions.
- Work orders from exceedances.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | 12 months. |
| independence | Specialist reports from qualified technicians; assessor samples raw data. |
| mandatoryItems | Condition monitoring records; Exceedance work orders |
| acceptableAlternatives | Continuous online monitoring data in lieu of periodic surveys. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-05, CG-06 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Failure not preceded by detected deterioration; New asset class |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, ANALYSIS

**Assessment procedure**

1. Obtain plan.
2. Sample records and check frequency.
3. Trace exceedances to work orders.
4. Review coolant quality data against OEM envelope.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to critical asset classes.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Hot joint on busway undetected; Coolant contamination fouls cold plates; Transformer incipient fault missed; Battery cell failure undetected

**Testing safety.** Thermography and partial-discharge surveys of energised equipment are hazardous; they shall be carried out by qualified persons under the site's electrical safety rules and, where covers are removed, under permit with appropriate arc-flash PPE.

**UNKNOWN rule.** No condition monitoring for a critical class is US3.

**Ontology classes.** AssetInstance, Event, Safeguard · **Related controls.** MCF-OPS-009, MCF-THM-018, MCF-POW-010

**Informative references.** NFPA 70B (electrical equipment maintenance); ISO 17359 (condition monitoring and diagnostics of machines); IEC 60599 (dissolved gas analysis interpretation); IEC 60270 (partial discharge measurements); ISO 20816 (mechanical vibration); ASHRAE TC 9.9 liquid cooling guidance

### MCF-OPS-011

**Calibration** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Instruments whose readings drive control, protection, alarming, billing or assurance decisions (temperature, pressure, flow, leak, power and energy meters, CTs/VTs, protection relays, gas detectors, and the test instruments used by technicians) are calibrated to traceable standards at defined intervals, so that control loops and evidence are trustworthy.

**Requirement.** The maintenance manager shall maintain a calibration register for critical instruments, including sensors used in BMS/EPMS/CDU control loops and alarms, protection relays (secondary injection testing), revenue and sub-meters, leak detection, and portable test equipment, stating interval, method, traceability and tolerance. Out-of-tolerance results shall trigger an impact assessment of decisions and evidence that relied on the instrument since its last good calibration.

**Assessment criteria**

1. Register covers instruments in control loops, alarms, protection and evidence.
2. Calibrations in the sample were performed within interval with traceable certificates.
3. Out-of-tolerance results had impact assessments.
4. Protection relay testing records are current.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Calibration interval for control-loop temperature sensors | months | 12 | Illustrative; set from OEM and criticality. |

**Minimum evidence**

- Calibration register.
- Calibration certificates.
- Relay test reports.
- Out-of-tolerance impact assessments.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | 12 months. |
| independence | Certificates from accredited calibration providers where available (E5). |
| mandatoryItems | Calibration register; Certificates for sample |
| acceptableAlternatives | In-situ comparison against a calibrated reference with recorded results. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-07 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Sensor replacement; Control instability; Out-of-tolerance result |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, INSPECTION

**Assessment procedure**

1. Obtain register.
2. Sample instruments by tag and verify certificate and date.
3. Inspect calibration labels on a sample in the field.
4. Review out-of-tolerance handling.

**Gate mappings.** CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies to critical instruments.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Drifted supply-temperature sensor causes CDU to under-cool; Uncalibrated leak sensor; Protection relay maloperation

**Testing safety.** Relay secondary injection and in-situ calibration of control-loop sensors require permits and control-system owner authorisation; assessors only inspect labels and records.

**UNKNOWN rule.** Unknown calibration status of control-loop sensors is US3; US4 where CG-07 relies on them.

**Ontology classes.** AssetInstance, EvidenceObject, Safeguard · **Related controls.** MCF-THM-022, MCF-POW-021, MCF-OPS-013

**Informative references.** ISO 10012 (measurement management systems); ISO/IEC 17025 (competence of testing and calibration laboratories); NFPA 70B (electrical equipment maintenance)

### MCF-OPS-012

**Deferred Maintenance** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Maintenance that is deferred, overdue or cancelled is visible, risk-assessed, approved by someone with authority, time-limited and reflected in the declared operating state, so that the accumulated risk of deferral does not silently erode resilience.

**Requirement.** The maintenance manager shall record every deferral or overdue item of maintenance on critical assets in a deferred maintenance register with reason, risk assessment, compensating measures, approver with authority, and expiry date. Deferrals beyond the profile limit shall require re-approval by the accountable owner. Deferred safety-critical maintenance shall be reflected in the operating state (for example the system declared DEGRADED) and in handover (MCF-OPS-003).

**Assessment criteria**

1. All overdue critical maintenance in the CMMS appears in the register.
2. Each deferral has risk assessment, approver and expiry.
3. No deferral exceeds the limit without re-approval.
4. Safety-critical deferrals are reflected in operating state and handover.
5. Aggregate deferral is reported to the accountable owner.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum deferral without re-approval | days | 30 | Illustrative. |

**Minimum evidence**

- Deferred maintenance register.
- CMMS overdue report.
- Approvals.
- Operating-state records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | 12 months. |
| independence | CMMS extract by assessor reconciled to register. |
| mandatoryItems | CMMS overdue report reconciled to register |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-05, CG-06, CG-13 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Overdue count rises above threshold; Failure of deferred asset |

**Assessment methods.** RECONCILIATION, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Extract overdue items from CMMS.
2. Reconcile to register.
3. Sample approvals and expiry.
4. Check operating-state reflection.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING); CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to critical assets.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Generator maintenance repeatedly deferred; Overdue battery replacement; Hidden accumulation of deferrals

**Testing safety.** Records review; inspection of deferred assets is visual only and follows site access rules.

**UNKNOWN rule.** CMMS data unavailable is U2, US3.

**Ontology classes.** Action, OperatingState, AssetInstance · **Related controls.** MCF-OPS-009, MCF-OPS-003, MCF-OPS-024, MCF-GOV-007

**Informative references.** ISO 55001 (asset management systems); NFPA 70B (electrical equipment maintenance)

## OPS-04 Alarm, incident and problem management

### MCF-OPS-013

**Alarm Rationalisation** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Alarms from BMS, EPMS, CDU, fire, leak detection, security and NOC systems are rationalised so that every alarm is meaningful, prioritised by consequence and time to respond, has a defined response, and the alarm load on operators remains manageable in normal and upset conditions.

**Requirement.** The control-system owner shall maintain an alarm philosophy and master alarm database for in-scope monitoring systems in which each alarm has a documented cause, consequence, priority (derived from consequence and time-to-impact per MCF-DEP-003), setpoint basis, and response procedure. The control-system owner shall measure alarm performance (alarm rates per operator in normal and upset conditions, standing alarms, chattering alarms, shelved or suppressed alarms) at the profile interval, act on exceedances, and control alarm suppression and shelving through MCF-OPS-019.

**Assessment criteria**

1. An approved alarm philosophy exists covering priority definitions and performance targets.
2. Each critical alarm in a sample has cause, consequence, priority, setpoint basis and response procedure.
3. Priorities are consistent with time-to-impact (no low-priority alarm on a seconds-scale consequence).
4. Alarm performance metrics are measured at the interval in normal and upset periods, and exceedances actioned.
5. Shelved and suppressed alarms are recorded, time-limited and reviewed.
6. Critical alarms are annunciated to a continuously attended location with defined escalation.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Target average alarm rate per operator in normal operation | alarms per hour | Per alarm philosophy (no default) | Set in the alarm philosophy with reference to IEC 62682 / ANSI/ISA-18.2 and EEMUA 191 benchmarks. |
| Alarm performance review interval | months | 1 | Illustrative. |

**Minimum evidence**

- Alarm philosophy.
- Master alarm database extract.
- Alarm performance reports for the period, including an upset event.
- Shelving/suppression log.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY |
| periodCoverage | At least 3 months of alarm logs including at least one upset event where one occurred. |
| independence | Assessor computes metrics from raw alarm logs. |
| mandatoryItems | Master alarm database; Raw alarm logs |
| acceptableAlternatives |  |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-07 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-06, CG-05 require gate-level evaluation. |
| reassessmentTriggers | New monitoring system or integration; Alarm flood incident; Setpoint change programme |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, SAMPLING, OBSERVATION

**Assessment procedure**

1. Obtain philosophy and database.
2. Sample critical alarms and check rationalisation fields.
3. Cross-check priorities with DEP-003 time-to-impact.
4. Compute alarm rates and standing/chattering counts from raw logs.
5. Review shelving log.
6. Observe console annunciation and escalation.

**Gate mappings.** CG-07 Critical control-system integrity (CRITICAL); CG-06 Thermal continuity (SUPPORTING); CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies to all monitoring systems annunciating to operators for in-scope infrastructure.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY, MAINTENANCE

**Failure modes addressed.** Operator error during alarm flood (scenario X11); Critical CDU alarm buried among nuisance alarms; Leak alarm shelved and forgotten; Alarm routed to unattended console

**Testing safety.** Analysis of logs only; no alarms shall be generated on live systems for assessment, except under an approved test plan with operators informed.

**UNKNOWN rule.** Raw alarm logs unavailable is U1, US4 (CG-07 critical).

**Ontology classes.** Safeguard, Event, InfrastructureSystem · **Related controls.** MCF-DEP-003, MCF-OPS-019, MCF-THM-008, MCF-POW-021

**Informative references.** IEC 62682 (management of alarm systems for the process industries); ANSI/ISA-18.2 (management of alarm systems); EEMUA Publication 191 (alarm systems guide)

### MCF-OPS-014

**Incident Response** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Incidents affecting infrastructure or Service Outcomes are detected, classified by outcome impact, escalated, coordinated across facilities, NOC, platform, tenant and provider teams, and stabilised within defined timescales.

**Requirement.** The operations manager shall operate an incident management process that classifies incidents by Service Outcome impact and safety, defines escalation timescales and authorities, establishes a joint bridge between facilities, NOC, platform and provider teams for cross-domain incidents, links to EOPs and to RES-06 crisis command, records a timeline, and requires a post-incident review for incidents above the profile threshold.

**Assessment criteria**

1. Classification criteria reference Service Outcome impact and safety.
2. Escalation timescales are defined and met in sampled incidents.
3. Cross-domain incidents had a joint bridge with facilities and IT participation.
4. Incident timelines are recorded.
5. Post-incident reviews were held above threshold.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Escalation time for Service Outcome-impacting incidents | minutes | 15 | Illustrative. |

**Minimum evidence**

- Incident procedure.
- Incident records for period.
- Bridge logs.
- Post-incident reviews.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | DEGRADED; EMERGENCY; RECOVERY |
| periodCoverage | 12 months. |
| independence | Assessor reconstructs timelines from source logs for a sample. |
| mandatoryItems | Incident records with timelines |
| acceptableAlternatives | Where no qualifying incident occurred, a scenario exercise (RES-05) supports the OPERATION claim at confidence no higher than CONF-2. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-10, CG-13 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Major incident; Process change; Organisational change |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Obtain procedure.
2. Sample incidents including cross-domain ones.
3. Reconstruct timelines from BMS/EPMS/NOC logs.
4. Compare escalation to timescales.
5. Review post-incident reviews.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to all infrastructure incidents within the boundary, including those initiated by providers or tenants.

**Lifecycle stages.** OPERATE · **Operating states.** DEGRADED, EMERGENCY, RECOVERY

**Failure modes addressed.** Facilities and NOC work separately on a cooling incident; Escalation delayed; No timeline recorded

**Testing safety.** Records review and interviews; incident simulations, if used, follow RES-05 exercise controls and are announced to operators.

**UNKNOWN rule.** Incident records incomplete is US3.

**Ontology classes.** Event, Finding, Action · **Related controls.** MCF-RES-021, MCF-OPS-015, MCF-OPS-005, MCF-SEC-019

**Informative references.** ISO 22320 (emergency management: incident management); ISO/IEC 20000-1 (service management system requirements); ISO/IEC 27035 (information security incident management)

### MCF-OPS-015

**Root Cause Analysis** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Significant incidents and near misses are analysed to their root and contributing causes, including latent design, organisational and human-factors causes, so that corrective actions address causes rather than symptoms.

**Requirement.** The operations manager shall require a root cause analysis using a recognised method for each incident or near miss above the profile threshold, completed within the profile time, identifying direct, contributing and root causes (including procedure, competence, alarm, design, supplier and organisational factors), propagation beyond expected containment, and corrective and preventive actions with owners. RCAs of provider-caused events shall be obtained from the provider and assessed.

**Assessment criteria**

1. RCAs exist for incidents above threshold, completed within time.
2. A recognised method is used and contributing human and organisational factors are considered.
3. Propagation beyond expected fault domain is identified where it occurred.
4. Actions have owners and dates.
5. Provider RCAs were obtained and assessed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| RCA completion time | working days | 20 | Illustrative. |

**Minimum evidence**

- RCA reports.
- Action records.
- Provider RCAs.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; RECOVERY |
| periodCoverage | 12 months. |
| independence | RCA facilitated by a person not directly involved in the incident. |
| mandatoryItems | RCA reports for incidents above threshold |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-09 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Recurring incident; RCA overdue |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, ANALYSIS

**Assessment procedure**

1. Identify incidents above threshold.
2. Check RCA existence and timeliness.
3. Assess depth of analysis for a sample.
4. Check actions.

**Gate mappings.** CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to incidents and near misses above the profile threshold, including provider-caused events affecting the boundary.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, RECOVERY

**Failure modes addressed.** Blame attributed to individual without systemic cause; Same failure recurs; Propagation path not understood

**Testing safety.** Records review; RCA interviews shall not be used to attribute individual blame.

**UNKNOWN rule.** Missing RCAs is US3.

**Ontology classes.** Finding, FailureScenario, Action · **Related controls.** MCF-OPS-014, MCF-OPS-016, MCF-RES-020

**Informative references.** IEC 62740 (root cause analysis); HSE HSG245 (investigating accidents and incidents); IEC 61025 (fault tree analysis)

### MCF-OPS-016

**Problem Elimination** · CORRECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Corrective and preventive actions from incidents, RCAs, audits and trends are implemented and verified to have eliminated or reduced recurrence, and known errors are managed until fixed.

**Requirement.** The operations manager shall track problems and corrective/preventive actions to closure, shall verify effectiveness of closed actions by evidence that the failure mode has not recurred over a defined period or by test, shall maintain a known-error record with workarounds for unresolved problems, and shall review recurrence trends at the profile interval.

**Assessment criteria**

1. Problems and actions are tracked with owners and dates.
2. Closed actions have effectiveness verification.
3. No recurrence of verified-closed failure modes in the period, or recurrence reopened the problem.
4. Known errors have workarounds communicated to operators.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Effectiveness verification period | months | 6 | Illustrative. |

**Minimum evidence**

- Problem register.
- Action closure and verification records.
- Recurrence analysis.
- Known-error records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E6; E7 |
| qualityFloor | P4 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | At least 12 months. |
| independence | Verification by a person other than the action owner. |
| mandatoryItems | Effectiveness verification records |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-14 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Recurrence; Overdue actions |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, SAMPLING

**Assessment procedure**

1. Obtain register.
2. Sample closed actions and check verification.
3. Analyse incident data for recurrence.
4. Review known errors.

**Gate mappings.** CG-14 Change control (SUPPORTING)

**Applicability.** Applies to problems arising from incidents, RCAs, audits, assessments and trend analysis in the boundary.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Actions closed without implementation; Recurring failure; Workaround unknown to night shift

**Testing safety.** Effectiveness tests follow owning-domain test controls and authorisation.

**UNKNOWN rule.** No verification evidence for closed actions is US3.

**Ontology classes.** Action, Finding, ValidationResult · **Related controls.** MCF-OPS-015, MCF-RES-020, MCF-DEP-020

**Informative references.** ISO/IEC 20000-1 (service management system requirements); ISO 9001 (quality management systems)

## OPS-05 Change and configuration management

### MCF-OPS-017

**Configuration Baseline** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** An authoritative, current baseline exists for the configuration of facility and AI infrastructure that matters to Required Functions, so that changes can be assessed against it, drift detected and known-good states restored.

**Requirement.** The configuration manager shall maintain an approved configuration baseline covering, at minimum: as-built single-line diagrams and P&IDs; protection settings and coordination study revision; BMS/EPMS/CDU setpoints, sequences of operation and PLC logic versions; UPS, ATS and PDU settings; firmware and software versions of facility and IT infrastructure; network and fabric configurations; storage and cluster-manager configuration. The baseline shall be versioned, access-controlled, reconciled to the live state at the profile interval and after each change, and backed up outside the fault domain it describes.

**Assessment criteria**

1. The baseline covers each listed category for in-scope systems.
2. Baseline items are versioned and access-controlled.
3. Live configuration in a sample reconciles to baseline, or drift is recorded and dispositioned.
4. Drawings (SLD, P&ID) match as-built for a sample walk-down.
5. Baseline backups are held outside the fault domain and restorable.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Baseline reconciliation interval | months | 6 | Illustrative; continuous automated drift detection where available. |

**Minimum evidence**

- Baseline repository index.
- Live configuration exports for sample.
- Drift reports.
- Drawing walk-down record.
- Backup location and restore test evidence.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; RECOVERY |
| periodCoverage | Current; reconciliations for 12 months. |
| independence | Live state captured by assessor or automated system independent of the configuration manager. |
| mandatoryItems | Baseline index; Live-to-baseline reconciliation |
| acceptableAlternatives |  |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-14 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-02, CG-07 require gate-level evaluation. |
| reassessmentTriggers | Change implemented; Drift detected; Recovery event |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INSPECTION, SAMPLING

**Assessment procedure**

1. Obtain baseline index.
2. Sample systems across categories.
3. Capture live configuration (read-only) and compare.
4. Walk down drawings for a sample.
5. Verify backup location and restore evidence.

**Gate mappings.** CG-14 Change control (CRITICAL); CG-02 Boundary and architecture integrity (SUPPORTING); CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies to all in-scope configurable systems.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE, DECOMMISSION · **Operating states.** NORMAL, MAINTENANCE, RECOVERY, TRANSITION

**Failure modes addressed.** Protection settings differ from coordination study; CDU setpoint drift; Recovery reintroduces corrupt configuration (scenario X15); SLD out of date

**Testing safety.** Configuration capture shall be read-only; reading protection relay settings requires the relay owner's procedure.

**UNKNOWN rule.** No baseline for a category of control-system configuration is US4 (CG-14 critical).

**Ontology classes.** ArchitectureSnapshot, AssetInstance, EvidenceObject · **Related controls.** MCF-OPS-018, MCF-NET-022, MCF-CMP-004, MCF-RES-015, MCF-SUP-013

**Informative references.** SAE EIA-649C (configuration management standard); ISO 10007 (guidelines for configuration management); ISO/IEC 20000-1 (service management system requirements)

### MCF-OPS-018

**Change Assessment** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Every change to critical facility or AI infrastructure is classified, impact-assessed against the dependency graph, fault domains and redundancy, scheduled in coordination with workloads, and approved by people with authority across facilities and IT before implementation.

**Requirement.** The change manager shall operate a change process that requires, for each change to in-scope infrastructure: classification (standard, normal, emergency) with criteria; impact assessment that identifies affected Required Functions using the asset-to-function and dependency maps, redundancy and fault-domain exposure during the change, safety implications, and workload coordination (for example checkpoint or drain); a linked MOP for non-routine work; approval by a change authority with both facilities and IT representation for cross-domain changes; and conflict checking against other scheduled changes and maintenance. Emergency changes shall be retrospectively reviewed.

**Assessment criteria**

1. Change classification criteria are defined.
2. Sampled changes have documented impact assessment using dependency and fault-domain data.
3. Cross-domain changes were approved with both facilities and IT representation.
4. Conflicting changes were detected and resolved by scheduling.
5. Emergency changes were reviewed retrospectively.
6. No changes to in-scope systems occurred without a change record (reconciled against configuration drift and logs).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Emergency change retrospective review time | working days | 5 | Illustrative. |

**Minimum evidence**

- Change procedure.
- Change records for period.
- CAB minutes.
- Reconciliation of configuration changes to change records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | MAINTENANCE; TRANSITION; NORMAL |
| periodCoverage | 12 months. |
| independence | Assessor reconciles detected changes (drift, logs) to records independently. |
| mandatoryItems | Change records; Unrecorded-change reconciliation |
| acceptableAlternatives |  |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-14 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-03 require gate-level evaluation. |
| reassessmentTriggers | Change-related incident; Process or tool change |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Obtain procedure.
2. Sample changes across classes.
3. Check impact assessments for dependency and fault-domain analysis.
4. Check approvals.
5. Reconcile configuration drift and device logs to change records.
6. Review emergency changes.

**Gate mappings.** CG-14 Change control (CRITICAL); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to all changes to in-scope infrastructure.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, TRANSITION

**Failure modes addressed.** Change removes hidden shared dependency (scenario X04); IT change triggers load step without facilities approval; Concurrent changes reduce redundancy twice; Unrecorded change

**Testing safety.** Not applicable (records review).

**UNKNOWN rule.** Inability to reconcile changes (no logs) is US4 (CG-14 critical).

**Ontology classes.** Event, Dependency, FaultDomain, ReassessmentTrigger · **Related controls.** MCF-OPS-006, MCF-OPS-017, MCF-OPS-020, MCF-RES-023, MCF-CAP-023

**Informative references.** ISO/IEC 20000-1 (service management system requirements); ITIL 4 change enablement practice guide; SAE EIA-649C (configuration management standard)

### MCF-OPS-019

**Temporary Configuration** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Temporary configurations (bypasses, jumpers, forced points, overrides, manual mode on automatic systems, inhibited or shelved alarms, temporary chillers or generators, load banks, temporary cabling and hoses) are approved, registered, time-limited, visible to operators and removed with verification.

**Requirement.** The shift lead shall record every temporary configuration of critical infrastructure in a temporary configuration register with description, reason, risk assessment, approver, expiry, compensating measures and removal verification. Temporary configurations shall be visible at the operator console where technically possible, included in handover, reviewed at each expiry, and any extension shall be re-approved. Safety-system overrides (fire, leak, gas detection, emergency power off) shall require approval at the level set in the capability profile.

**Assessment criteria**

1. Register exists and is current.
2. Live temporary configurations found on inspection or console are in the register.
3. Each entry has approver and expiry; expired entries were removed or re-approved.
4. Safety-system overrides had the required approval level.
5. Removal verification is recorded.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum temporary configuration duration without re-approval | days | 7 | Illustrative. |

**Minimum evidence**

- Temporary configuration register.
- BMS/EPMS forced-point and override reports.
- Alarm shelving log.
- Removal records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | MAINTENANCE; DEGRADED; EMERGENCY; NORMAL |
| periodCoverage | 6 months. |
| independence | Assessor extracts forced points and overrides from systems directly. |
| mandatoryItems | Register; System override extract reconciled |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-14, CG-07, CG-04 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Incident involving temporary configuration; System upgrade affecting override visibility |

**Assessment methods.** RECONCILIATION, INSPECTION, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Obtain register.
2. Extract overrides, forced points and shelved alarms from BMS/EPMS/CDU.
3. Reconcile to register.
4. Inspect plant for physical temporary configurations.
5. Check approvals and removal verification.

**Gate mappings.** CG-14 Change control (SUPPORTING); CG-07 Critical control-system integrity (SUPPORTING); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to all critical infrastructure.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** MAINTENANCE, DEGRADED, EMERGENCY, NORMAL, RECOVERY

**Failure modes addressed.** CDU left in manual after maintenance; Fire alarm zone isolated and forgotten; UPS left on maintenance bypass; Forced BMS point masks failure

**Testing safety.** Inspection is visual; assessors shall not remove or alter any temporary configuration.

**UNKNOWN rule.** Inability to extract overrides from a control system is US3; US4 if a safety-system override cannot be ruled out.

**Ontology classes.** OperatingState, Safeguard, Event · **Related controls.** MCF-OPS-003, MCF-OPS-013, MCF-POW-012, MCF-OPS-017

**Informative references.** IEC 62682 (management of alarm systems); HSE HSG250 (guidance on permit-to-work systems)

### MCF-OPS-020

**Rollback and Validation** · CORRECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Each material change can be reversed to a known-good state when it fails, and its success is validated by defined post-change tests and observation before the change is closed and redundancy is declared restored.

**Requirement.** The change manager shall require each material change to define back-out criteria, a back-out procedure tested or rehearsed where practicable, and post-change validation (functional checks, telemetry review, alarm review, redundancy restoration check, and for IT infrastructure job or health checks) with evidence attached before closure. Failed validations shall trigger back-out or an incident, and post-implementation review shall be held for failed or backed-out changes.

**Assessment criteria**

1. Sampled material changes define back-out criteria and procedure.
2. Post-change validation evidence is attached before closure.
3. Redundancy restoration was confirmed for changes affecting redundant systems.
4. Failed validations led to back-out or incident.
5. Back-out procedures for high-risk changes were rehearsed or tested.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Post-change observation period for facility control changes | hours | 24 | Illustrative. |

**Minimum evidence**

- Change records with back-out plans.
- Validation evidence.
- Back-out rehearsal records.
- Post-implementation reviews.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E6; E7 |
| qualityFloor | P4 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | MAINTENANCE; TRANSITION; NORMAL |
| periodCoverage | 12 months. |
| independence | Validation reviewed by someone other than the implementer. |
| mandatoryItems | Validation evidence attached to closed changes |
| acceptableAlternatives |  |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-14 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-10 require gate-level evaluation. |
| reassessmentTriggers | Failed change; Change process modification |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, REPERFORMANCE, ANALYSIS

**Assessment procedure**

1. Sample material changes.
2. Check back-out and validation evidence.
3. Reperform a validation check from telemetry for a sample.
4. Review failed changes.

**Gate mappings.** CG-14 Change control (CRITICAL); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to material changes.

**Lifecycle stages.** CHANGE, OPERATE · **Operating states.** MAINTENANCE, TRANSITION, NORMAL, RECOVERY

**Failure modes addressed.** Change closed while redundancy not restored; No back-out for firmware change; Silent degradation after change

**Testing safety.** Back-out rehearsals on facility systems require MOP, permit and change approval.

**UNKNOWN rule.** Closed material changes without validation evidence is US4 (CG-14 critical).

**Ontology classes.** ValidationResult, TestRecord, Event · **Related controls.** MCF-OPS-018, MCF-CMP-016, MCF-SEC-024, MCF-SUP-015

**Informative references.** ISO/IEC 20000-1 (service management system requirements); SAE EIA-649C (configuration management standard)

## OPS-06 Capacity and service operations

### MCF-OPS-021

**Capacity Review** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Power, cooling, space, network and contracted utility capacity is reviewed against measured demand and committed growth, by operating state, so that new deployments are admitted only where capacity including maintenance and failure states is available.

**Requirement.** The capacity manager shall review at the profile interval rated, available, reserved, consumed and headroom capacity for each capacity-bearing element (utility contract, transformers, UPS systems, busways and PDUs, generator capacity, chiller and heat-rejection plant, CDU and secondary loops, air cooling, floor loading, network ports and optics), considering N and N-1 (maintenance) states and transient AI load behaviour (for example synchronous training power swings). New deployments shall pass a capacity admission check against these values before installation.

**Assessment criteria**

1. Capacity is recorded per element with rated, available, reserved, consumed and headroom values from measured data.
2. N-1 and maintenance-state headroom is calculated.
3. Transient and peak AI load behaviour is considered (from CAP-04 and POW-05).
4. Deployments in the period passed a documented admission check.
5. Elements approaching threshold triggered action.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Capacity planning threshold | % of N-1 available capacity | 80 | Illustrative. |

**Minimum evidence**

- Capacity reports.
- Measured demand data (EPMS, BMS, CDU telemetry).
- Admission check records.
- Actions for elements above threshold.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | 12 months. |
| independence | Assessor recomputes headroom for a sample from telemetry. |
| mandatoryItems | Capacity reports by element; Admission records |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-05, CG-06 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Deployment; Density increase; Capacity element change |

**Assessment methods.** ANALYSIS, SAMPLING, RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Obtain capacity reports.
2. Recompute headroom from telemetry for a sample.
3. Check N-1 analysis.
4. Sample deployments and check admission.
5. Check actions above threshold.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to all capacity-bearing elements.

**Lifecycle stages.** PLAN, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Deployment exceeds N-1 UPS capacity; CDU loop above capacity in maintenance; Expansion creates stranded compute (scenario X17)

**Testing safety.** Analysis only.

**UNKNOWN rule.** No measured data for a capacity element is US3; US4 where CG-05/06 capacity criteria rely on it.

**Ontology classes.** CapacityAssertion, Resource, OperatingState · **Related controls.** MCF-CAP-014, MCF-POW-015, MCF-THM-010, MCF-OPS-023

**Informative references.** ISO/IEC 20000-1 (service management system requirements); EN 50600-3-1 (management and operational information)

### MCF-OPS-022

**Service Level Monitoring** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Service Outcome indicators (for example accelerator availability per partition, job interruption rate attributable to infrastructure, inference latency and availability, environmental envelope compliance at the IT inlet or coolant supply, power and cooling availability to tenants) are measured accurately and visibly to the NOC and BMS operators.

**Requirement.** The operations manager shall define and measure indicators for each Service Outcome, with measurement method, source, and data quality checks, shall display them to NOC and BMS operators in an integrated view, and shall report performance against tolerance at the profile interval.

**Assessment criteria**

1. Indicators are defined for each Service Outcome with method and source.
2. Measurement data quality (gaps, clock alignment) is checked.
3. Operators have an integrated view of facility and IT indicators.
4. Performance against tolerance is reported.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Indicator reporting interval | months | 1 | Illustrative. |

**Minimum evidence**

- Indicator definitions.
- Measurement data.
- Dashboard observation.
- Reports.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | 6 months. |
| independence | Assessor recomputes indicators from source data for a sample. |
| mandatoryItems | Indicator definitions and data |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result caps the decision at CONDITIONALLY_ASSURED with a recorded condition; downgrade to US2 (confidence ceiling CONF-2) only where the assessor records that no control result or decision condition depends on it. |
| reassessmentTriggers | New Service Outcome; Monitoring platform change |

**Assessment methods.** ANALYSIS, OBSERVATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Obtain definitions.
2. Recompute a sample.
3. Observe operator view.
4. Review reports.

**Gate mappings.** None

**Applicability.** Applies to all declared Service Outcomes.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, DEGRADED, RECOVERY

**Failure modes addressed.** Outcome degradation invisible to facilities operators; Indicator computed from incomplete data

**Testing safety.** Observation of operator displays only; assessors shall not interact with operator consoles.

**UNKNOWN rule.** No measurement for a Service Outcome is US3 (it limits OPERATION claims across domains).

**Ontology classes.** ServiceOutcome, Event, EvidenceObject · **Related controls.** MCF-CAP-005, MCF-CAP-006, MCF-OPS-024, MCF-EVA-023

**Informative references.** ISO/IEC 20000-1 (service management system requirements); ASHRAE TC 9.9 thermal guidelines

### MCF-OPS-023

**Resource Balancing** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Load is placed and balanced across phases, PDUs, UPS modules, busways, CDU loops and rows so that no element exceeds its rating in N or N-1 states, capacity is not stranded, and AI workload controls (power capping, placement constraints) are coordinated with facility limits.

**Requirement.** The capacity manager shall define placement rules and balance limits (phase imbalance, per-PDU and per-UPS load, per-CDU flow and heat load) for in-scope infrastructure, shall monitor balance continuously or at the profile interval, and shall coordinate with the platform owner on workload controls (scheduler placement, power capping) so that facility limits are respected. Imbalance or exceedance shall be corrected through change control.

**Assessment criteria**

1. Placement rules and balance limits are defined.
2. Monitoring shows balance within limits or exceedances corrected.
3. Workload controls (power capping, placement constraints) are configured to respect facility limits where used.
4. Corrections were made through change control.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum phase imbalance | % | Site-specific (no default) | Set from UPS and transformer OEM limits. |

**Minimum evidence**

- Placement rules.
- Balance monitoring data.
- Scheduler or power-cap configuration.
- Correction change records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | 6 months. |
| independence | Assessor extracts balance data directly. |
| mandatoryItems | Balance monitoring data |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-05, CG-06, CG-09 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Deployment; Hardware generation change |

**Assessment methods.** ANALYSIS, RECONCILIATION, INSPECTION

**Assessment procedure**

1. Obtain rules.
2. Extract balance data.
3. Inspect workload control configuration.
4. Review corrections.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to in-scope power and cooling distribution.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Phase imbalance overloads UPS; Single PDU overloaded on failover; Stranded capacity on one CDU loop

**Testing safety.** Data extraction is read-only; no load shall be moved or capped to test balance limits.

**UNKNOWN rule.** No balance data is US3.

**Ontology classes.** CapacityAssertion, Resource, FaultDomain · **Related controls.** MCF-OPS-021, MCF-CMP-010, MCF-DEP-019, MCF-POW-015

**Informative references.** EN 50600-2-2 (power distribution); ASHRAE TC 9.9 liquid cooling guidance

### MCF-OPS-024

**Operational Reporting** · DIRECTIVE · claim type OPERATION · required AL4

**Objective.** Accountable owners receive accurate, traceable periodic reports on operational risk and performance (incidents and near misses, Service Outcome performance, capacity headroom, deferred maintenance, temporary configurations, open findings and actions, staffing shortfalls, supplier performance) on which they can make decisions.

**Requirement.** The operations manager shall issue operational reports to accountable owners at the profile interval containing the listed indicators with data sources and lineage, trends and exceptions, and shall record decisions or actions arising.

**Assessment criteria**

1. Reports were issued at the interval with the listed content.
2. Figures trace to source systems.
3. Exceptions are highlighted with recommendations.
4. Decisions arising are recorded.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Operational reporting interval | months | 1 | Illustrative. |

**Minimum evidence**

- Operational reports.
- Source data for sampled figures.
- Decision records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | 12 months. |
| independence | Assessor traces figures to sources. |
| mandatoryItems | Reports for period |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-13 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Reporting change; Organisational change |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, SAMPLING

**Assessment procedure**

1. Obtain reports.
2. Trace sampled figures to sources.
3. Review decisions arising.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to the operations function reporting to accountable owners named under GOV-02.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Accountable owner unaware of deferred maintenance backlog; Report figures inconsistent with source

**Testing safety.** Records review only.

**UNKNOWN rule.** Reports whose figures cannot be traced to source systems are US2 (confidence ceiling CONF-2 on dependent OPERATION claims) unless a decision condition relies on the reported figures, in which case US3.

**Ontology classes.** AssuranceReport, EvidenceObject, Action · **Related controls.** MCF-OPS-012, MCF-OPS-022, MCF-GOV-003, MCF-DEP-022

**Informative references.** ISO/IEC 20000-1 (service management system requirements); EN 50600-3-1 (management and operational information)
