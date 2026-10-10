# AIDCF-018-OPS Building Operations and Service Management Domain Guide

## Document control

| Field | Value |
|---|---|
| Document ID | AIDCF-018-OPS |
| Title | Building Operations and Service Management Domain Guide |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Parent artifact | AIDCF-018 Domain Guides |
| Normative basis | AIDCF-007A (controls MCF-OPS-001 to MCF-OPS-024), AIDCF-008, AIDCF-010 |
| Requirement prefix | DG-OPS-REQ-NNN |

### Revision history

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-10 | First issue of the OPS domain guide, aligned with the rewritten OPS controls in AIDCF-007A and the per-control gate mapping rule. |

### Status of this guide

This guide explains how to apply the 24 OPS controls of AIDCF-007A. The control records are normative and are held in the AIDCF-007A registry; where this guide and a control record differ, the control record governs and the difference shall be raised as a baseline issue. Requirements numbered DG-OPS-REQ-NNN are normative for assessments that claim conformance to AIDCF-018-OPS. Other text is informative.

## 1 Purpose and scope

### 1.1 Purpose

The OPS domain establishes whether the facility and its AI infrastructure are operated, maintained and changed by competent, authorised and adequately staffed people, working from controlled procedures under safe systems of work, with alarms that inform rather than overwhelm, incidents and problems that are managed to closure, changes that are controlled, and capacity that is managed against real demand. Engineering domains (POW, THM, CMP, STO, NET) assure what was built; OPS assures how it is run.

### 1.2 In scope

- Operating model and staffing: 24x7 coverage, role clarity and authority, shift handover, competence and authorisation (OPS-01).
- Procedure and work control: SOPs, alarm response procedures and EOPs; method statements (MOPs); permit to work; lockout and tagout (OPS-02).
- Maintenance and reliability: maintenance strategy, condition monitoring, calibration, deferred maintenance (OPS-03).
- Alarm, incident and problem management: alarm rationalisation, incident response, root cause analysis, problem elimination (OPS-04).
- Change and configuration management: configuration baseline, change assessment, temporary configuration, rollback and validation (OPS-05).
- Capacity and service operations: capacity review and admission, service level monitoring, resource balancing, operational reporting (OPS-06).

OPS covers the facility operations team, the BMS/EPMS operators, the NOC and infrastructure operations for compute, storage and network, maintenance contractors working under the owner's systems of work, and the interfaces between them.

### 1.3 Out of scope

- The technical design and performance of the systems being operated (POW, THM, CMP, STO, NET), including domain-specific procedures such as electrical switching procedures (POW-06) and thermal maintenance states (THM-06), which OPS governs as procedures but whose technical content the owning domain assures.
- Crisis command, stakeholder communications and emergency change during a declared crisis (RES-06).
- Security incident detection and response (SEC-05); OPS incident management interfaces with it.
- Governance-level accountability and risk acceptance authority (GOV-02).

### 1.4 Boundaries with other domains

| Topic | OPS role | Other domain role |
|---|---|---|
| Emergency procedures | Controls the procedure set, its validation and availability (MCF-OPS-005) | POW-06, THM-06 and RES-04 assure technical content and sequencing |
| Permit to work and LOTO | Operates the safe system of work (MCF-OPS-007, MCF-OPS-008) | PHY-06, POW and THM identify the hazards and isolation points |
| Change | Operates the change process (OPS-05) | GOV-03 sets exception governance; CAP-06 assesses material change impact on capability; RES-06 handles crisis emergency change |
| Alarms | Rationalises and measures alarms (MCF-OPS-013) | POW-06 (EPMS coverage) and THM-02/THM-06 (monitoring, sensor trust) provide the instrumentation |
| Firmware updates | Controls change, baseline and rollback | SUP-04 assures supply and staged rollout; CMP-04 assures compute baseline |
| Capacity | Operates capacity review and admission (OPS-06) | CAP-04/CAP-05 define demand and envelope; POW/THM define rated capacity |

## 2 Why this domain matters for AI capability

Operational and human factors are a principal cause of data-centre outages, and AI facilities make operational error both more likely and more consequential:

- **Shorter time to act.** At high rack densities with direct-to-chip liquid cooling, the time from loss of coolant flow to accelerator throttling or shutdown can be short. Emergency procedures that rely on a person walking to a plant room and diagnosing a fault may not complete within that time. Staffing, alarm priority and EOP design have to be derived from measured time-to-impact (MCF-DEP-003), not from habit.
- **Coupled facility and IT operations.** A training job, a CDU loop and a UPS system are coupled: maintenance on one UPS module may be safe for the electrical system but unsafe for a training run that has not checkpointed; a cluster scheduler that starts a large synchronous job creates a load step the electrical and cooling systems must absorb. OPS controls require facilities and IT to assess and approve changes jointly.
- **More hazardous work.** Liquid cooling introduces pressurised fluid systems into IT spaces; high-capacity UPS and battery systems, including lithium-ion, carry stored-energy and thermal-runaway hazards; MV distribution extends deeper into buildings. Permit-to-work and LOTO are therefore central to CG-04.
- **Many software-controlled systems.** BMS, EPMS, CDU controllers, PLCs, cluster managers and fabric controllers are configured and updated frequently. Configuration drift, temporary overrides left in place and uncontrolled firmware updates are recurring failure causes.
- **Alarm volume.** Integrating facility and IT telemetry multiplies alarm sources. Without rationalisation, operators face alarm floods during exactly the events where clear prioritisation matters most (AIDCF-004 scenario X11).

## 3 Reference patterns and variants

| Pattern (AIDCF-013) | Dominant OPS concerns | Controls most exercised |
|---|---|---|
| Single-site training facility | Staffing for time-critical manual actions; checkpoint coordination with maintenance | MCF-OPS-001, MCF-OPS-006, MCF-OPS-018 |
| Hyperscale campus | Consistency of procedures across buildings; centralised NOC with local response; fleet-scale change | MCF-OPS-005, MCF-OPS-018, MCF-OPS-013 |
| Colocation deployment | Split operations between provider and tenant; permits and changes crossing the demarcation | MCF-OPS-002, MCF-OPS-007, MCF-OPS-018 |
| Liquid-cooled high-density cluster | Liquid-loop work under permit and LOTO; coolant quality monitoring; CDU temporary configurations | MCF-OPS-007, MCF-OPS-008, MCF-OPS-010, MCF-OPS-019 |
| Modular facility | Vendor-operated skids; integration of skid alarms into the site alarm system | MCF-OPS-013, MCF-OPS-004 |
| Edge inference estate | Unstaffed sites, remote NOC, dispatch times; automated safe states | MCF-OPS-001 (alternative evidence), MCF-OPS-014 |
| Brownfield retrofit | Stale procedures and drawings; legacy alarms; mixed old and new plant | MCF-OPS-005, MCF-OPS-017, MCF-OPS-013 |
| Shared multi-tenant platform | Tenant change notification; capacity admission and balancing across tenants | MCF-OPS-021, MCF-OPS-023 |

**Variants.** In *outsourced facilities management*, the operator's controls are assessed through the contractor's systems, but accountability and authority remain with the owner (MCF-OPS-002) and evidence must be obtainable under MCF-SUP-006. In a *combined facilities-and-IT NOC*, MCF-OPS-013 and MCF-OPS-022 should be assessed on the integrated view; in *separate* facilities and IT operations centres, the bridge arrangements of MCF-OPS-014 and the joint change approval of MCF-OPS-018 become decisive.

## 4 Required functions and capability linkage

| Required Function (assurance view) | Linked Service Outcomes | Controls |
|---|---|---|
| Competent response capacity: the right people are available and authorised to act within time-to-impact | Availability and recovery outcomes; life safety | MCF-OPS-001 to MCF-OPS-004 |
| Safe and controlled work execution | Life safety; availability during MAINTENANCE | MCF-OPS-005 to MCF-OPS-008 |
| Asset condition and measurement integrity | Availability; integrity of control and evidence | MCF-OPS-009 to MCF-OPS-012 |
| Detection, response and learning | Availability and recovery outcomes | MCF-OPS-013 to MCF-OPS-016 |
| Controlled configuration and change | All outcomes; CG-14 | MCF-OPS-017 to MCF-OPS-020 |
| Capacity and service stewardship | Availability, performance and growth outcomes | MCF-OPS-021 to MCF-OPS-024 |

In the AIDCF-014 graph, InfrastructureSystems are OPERATED_BY and MONITORED_BY organisational roles; Required Functions are PROTECTED_BY procedures, permits and isolations (Safeguards) in specific OperatingStates; changes are Events that may TRIGGERS_REASSESSMENT; and configuration baselines are ArchitectureSnapshots against which drift is detected.

## 5 Dependencies, fault domains and common-mode concerns

OPS introduces human and organisational common modes that can defeat technical redundancy:

| Common mode | Mechanism | Control |
|---|---|---|
| One procedure used on both redundant paths | A procedural error is repeated on A and B | MCF-OPS-006 (MOP per task with redundancy state per step); MCF-OPS-018 (conflict checking) |
| One shift handling concurrent events | Staff capacity exhausted by simultaneous alarms | MCF-OPS-001 (emergency task analysis), MCF-OPS-013 (alarm flood metrics) |
| One person holding authority | Only one authorised person for HV switching on shift | MCF-OPS-004 with MCF-DEP-008 |
| One CMMS or ticketing system | Loss of CMMS hides open permits and overdue work | MCF-OPS-003 (handover reconciliation); offline procedure availability (MCF-OPS-005) |
| One configuration source | Backups of control logic stored in the system they restore | MCF-OPS-017 (backups outside the fault domain) |
| Temporary configurations on redundant members | Both CDUs left in manual, or both UPS on bypass, after maintenance | MCF-OPS-019 |
| Maintenance windows aligned with peak AI load | Reduced redundancy at the time of highest thermal and electrical stress | MCF-OPS-009, MCF-OPS-021 |

The MAINTENANCE operating state deserves particular attention. Many AIDCF resilience claims are stated for NORMAL; OPS controls require each maintenance configuration to be explicit (MCF-OPS-006, MCF-OPS-009) so that the capacity and redundancy actually present during work can be checked against the declared load.

**DG-OPS-REQ-001** For each sampled MOP on a redundant system, the assessor shall verify that the MOP states the redundancy level during each step and that the capacity check for that level (MCF-OPS-009 or MCF-OPS-021) was current at the time the work was performed.

## 6 Threats, hazards and failure scenarios with propagation paths

| Scenario | Initiating condition | Propagation path to Service Outcome | OPS controls that interrupt the path |
|---|---|---|---|
| Maintenance-induced outage (AIDCF-004 D5); X04 | Work on one UPS module or switchboard under an incomplete MOP | Hidden dependency or wrong isolation → second path de-energised → racks lose power → training jobs fail; inference unavailable | MCF-OPS-006, MCF-OPS-018, MCF-OPS-017 |
| X11 Operator error during alarm flood | Utility disturbance generates hundreds of alarms across EPMS, BMS and NOC | Critical CDU low-flow alarm not noticed → cold-plate temperatures rise → accelerators throttle then shut down | MCF-OPS-013, MCF-OPS-005, MCF-OPS-001 |
| Handover failure (D5) | Open isolation not handed over | Incoming shift re-energises equipment under work → injury risk and outage | MCF-OPS-003, MCF-OPS-007, MCF-OPS-008 |
| Competence gap (D5) | Contractor without liquid-cooling competence disconnects a pressurised hose | Coolant release onto energised equipment → leak, electrical fault, loss of a rack row | MCF-OPS-004, MCF-OPS-007, MCF-OPS-008 |
| Change failure (D5) | CDU control-logic update without back-out | Loop pumps cycle unstably → flow oscillation → throttling across loop | MCF-OPS-018, MCF-OPS-020, MCF-OPS-017 |
| Temporary configuration left in place | UPS left on maintenance bypass after work | Later utility disturbance passes straight to load → racks drop | MCF-OPS-019, MCF-OPS-003 |
| Deferred maintenance accumulation | Generator maintenance repeatedly deferred | Generator fails to start on utility loss (X01) | MCF-OPS-012, MCF-OPS-009 |
| Measurement drift | Supply-temperature sensor drifts low | CDU control under-cools while reporting normal → hot spots → hardware degradation | MCF-OPS-011, MCF-OPS-010 |
| X17 Expansion creates stranded compute | Racks installed without capacity admission | N-1 capacity exceeded; deployment cannot be energised or runs without redundancy | MCF-OPS-021, MCF-OPS-023 |

Hazards relevant to OPS (AIDCF-004 Part V) include electrical (arc, stored energy, back-feed), pressure/fluid (rupture, leak), chemical/material (coolant, refrigerant, battery), and human factors (fatigue, workload, interface ambiguity, lost situational awareness).

## 7 Safeguards

| Safeguard | Function | Controls |
|---|---|---|
| Staffing derived from emergency task analysis | Ensures time-critical manual actions can be completed | MCF-OPS-001 |
| Responsibility and authority matrix by state | Removes hesitation and gaps in emergencies | MCF-OPS-002 |
| Structured, reconciled handover | Preserves situational awareness | MCF-OPS-003 |
| Competence framework and authorisation register | Restricts hazardous work to authorised persons | MCF-OPS-004 |
| Controlled SOP/ARP/EOP set available offline | Guides correct action | MCF-OPS-005 |
| Task-specific MOPs with hold points and back-out | Prevents maintenance-induced outage | MCF-OPS-006 |
| Permit to work and LOTO | Controls hazardous energy and conflicting work | MCF-OPS-007, MCF-OPS-008 |
| Maintenance strategy with maintenance-state capacity check | Keeps maintenance within redundancy | MCF-OPS-009 |
| Condition monitoring and calibration | Detects deterioration; keeps measurements trustworthy | MCF-OPS-010, MCF-OPS-011 |
| Deferred maintenance register with authority and expiry | Prevents silent risk accumulation | MCF-OPS-012 |
| Rationalised alarms with measured performance | Keeps operator load manageable | MCF-OPS-013 |
| Incident, RCA and problem management | Stabilises, learns and prevents recurrence | MCF-OPS-014 to MCF-OPS-016 |
| Configuration baseline, change assessment, temporary configuration control, rollback | Controls change | MCF-OPS-017 to MCF-OPS-020 |
| Capacity admission and balancing | Prevents overload and stranded capacity | MCF-OPS-021, MCF-OPS-023 |

## 8 Critical-gate linkage

OPS holds the CRITICAL controls for CG-14 (Change control), the safe-work CRITICAL controls for CG-04 (Life safety and hazardous energy), the role-clarity CRITICAL control for CG-13 (Responsibility and authority), and the alarm-management CRITICAL control for CG-07 (Critical control-system integrity).

| Gate | Gate name | CRITICAL controls in this domain | SUPPORTING controls in this domain |
|---|---|---|---|
| CG-02 | Boundary and architecture integrity | none | MCF-OPS-017 |
| CG-03 | Critical dependency visibility | none | MCF-OPS-018 |
| CG-04 | Life safety and hazardous energy | MCF-OPS-004, MCF-OPS-007, MCF-OPS-008 | MCF-OPS-003, MCF-OPS-006, MCF-OPS-019 |
| CG-05 | Resilient electrical supply | none | MCF-OPS-009, MCF-OPS-010, MCF-OPS-012, MCF-OPS-013, MCF-OPS-021, MCF-OPS-023 |
| CG-06 | Thermal continuity | none | MCF-OPS-009, MCF-OPS-010, MCF-OPS-012, MCF-OPS-013, MCF-OPS-021, MCF-OPS-023 |
| CG-07 | Critical control-system integrity | MCF-OPS-013 | MCF-OPS-011, MCF-OPS-017, MCF-OPS-019 |
| CG-09 | Failure containment | none | MCF-OPS-015, MCF-OPS-023 |
| CG-10 | Recovery readiness | none | MCF-OPS-001, MCF-OPS-005, MCF-OPS-014, MCF-OPS-020 |
| CG-13 | Responsibility and authority | MCF-OPS-002 | MCF-OPS-001, MCF-OPS-004, MCF-OPS-005, MCF-OPS-012, MCF-OPS-014, MCF-OPS-024 |
| CG-14 | Change control | MCF-OPS-006, MCF-OPS-017, MCF-OPS-018, MCF-OPS-020 | MCF-OPS-002, MCF-OPS-003, MCF-OPS-005, MCF-OPS-016, MCF-OPS-019 |

CRITICAL controls in this domain:

- **MCF-OPS-002 Role Clarity** — CRITICAL for CG-13; claim type IMPLEMENTATION at AL3, sufficiency floor S3.
- **MCF-OPS-004 Competence and Authorisation** — CRITICAL for CG-04; claim type OPERATION at AL4, sufficiency floor S4.
- **MCF-OPS-006 Method Statements** — CRITICAL for CG-14; claim type OPERATION at AL4, sufficiency floor S4.
- **MCF-OPS-007 Permit to Work** — CRITICAL for CG-04; claim type OPERATION at AL4, sufficiency floor S4.
- **MCF-OPS-008 Lockout and Tagout** — CRITICAL for CG-04; claim type OPERATION at AL4, sufficiency floor S4.
- **MCF-OPS-013 Alarm Rationalisation** — CRITICAL for CG-07; claim type OPERATION at AL4, sufficiency floor S4.
- **MCF-OPS-017 Configuration Baseline** — CRITICAL for CG-14; claim type IMPLEMENTATION at AL3, sufficiency floor S4.
- **MCF-OPS-018 Change Assessment** — CRITICAL for CG-14; claim type OPERATION at AL4, sufficiency floor S4.
- **MCF-OPS-020 Rollback and Validation** — CRITICAL for CG-14; claim type EFFECTIVENESS at AL5, sufficiency floor S4.

**Rationale for the CRITICAL choices.** CG-14 cannot pass if non-routine work is done without MOPs (MCF-OPS-006), if there is no baseline to change against (MCF-OPS-017), if changes are not impact-assessed and approved (MCF-OPS-018), or if changes are closed without validation and rollback provision (MCF-OPS-020). CG-04 cannot pass if hazardous work is done by unauthorised persons (MCF-OPS-004), without permits (MCF-OPS-007) or without effective isolation of hazardous energy (MCF-OPS-008). CG-13 cannot pass if emergency decision authority for a Required Function is undefined (MCF-OPS-002). CG-07 cannot pass if operators cannot reliably perceive and act on critical control-system alarms (MCF-OPS-013). Other mappings are SUPPORTING: for example, temporary configuration control (MCF-OPS-019) is SUPPORTING for CG-14, CG-07 and CG-04 because its failure is usually evaluated through its effect on the baseline, alarm and permit controls.

**DG-OPS-REQ-002** When CG-04 is in scope, the assessor shall assess MCF-OPS-004, MCF-OPS-007 and MCF-OPS-008 for every category of hazardous work present in the boundary (including liquid-cooling and pressurised fluid work and battery or DC systems where present), and shall not record CONFORMING for any of them on a sample that omits a category present on site.

## 9 Capability-profile parameters

All defaults are illustrative and shall be replaced in the capability profile with site-specific values and their basis.

| Parameter | Unit | Illustrative default | Basis | Control |
|---|---|---|---|---|
| Minimum on-site staff per shift | persons by discipline | Site-specific (no default) | Derived from emergency task analysis; there is no universal staffing ratio. | MCF-OPS-001 |
| On-call specialist attendance time | minutes | 60 | Illustrative; must be shorter than the time available after on-site staff stabilise the event. | MCF-OPS-001 |
| Maximum shift length | hours | 12 | Illustrative; set with reference to HSE HSG256 guidance and local working-time law. | MCF-OPS-001 |
| Authorisation revalidation interval | months | 36 | Illustrative; set by site safety rules and legal requirements. | MCF-OPS-004 |
| Procedure review interval | months | 12 | Illustrative. | MCF-OPS-005 |
| Permit audit frequency | audits per month | 4 | Illustrative. | MCF-OPS-007 |
| LOTO field audit interval | months | 3 | Illustrative. | MCF-OPS-008 |
| Generator load test frequency | per year | Per NFPA 110 or site standard (no default) | Set from the adopted standard and OEM requirements. | MCF-OPS-009 |
| Thermography frequency for critical switchgear and busway | per year | 1 | Illustrative; NFPA 70B provides guidance. | MCF-OPS-010 |
| Coolant quality sampling interval | weeks | 4 | Illustrative; set from CDU and cold-plate OEM requirements. | MCF-OPS-010 |
| Calibration interval for control-loop temperature sensors | months | 12 | Illustrative; set from OEM and criticality. | MCF-OPS-011 |
| Maximum deferral without re-approval | days | 30 | Illustrative. | MCF-OPS-012 |
| Target average alarm rate per operator in normal operation | alarms per hour | Per alarm philosophy (no default) | Set in the alarm philosophy with reference to IEC 62682 / ANSI/ISA-18.2 and EEMUA 191 benchmarks. | MCF-OPS-013 |
| Alarm performance review interval | months | 1 | Illustrative. | MCF-OPS-013 |
| Escalation time for Service Outcome-impacting incidents | minutes | 15 | Illustrative. | MCF-OPS-014 |
| RCA completion time | working days | 20 | Illustrative. | MCF-OPS-015 |
| Effectiveness verification period | months | 6 | Illustrative. | MCF-OPS-016 |
| Baseline reconciliation interval | months | 6 | Illustrative; continuous automated drift detection where available. | MCF-OPS-017 |
| Emergency change retrospective review time | working days | 5 | Illustrative. | MCF-OPS-018 |
| Maximum temporary configuration duration without re-approval | days | 7 | Illustrative. | MCF-OPS-019 |
| Post-change observation period for facility control changes | hours | 24 | Illustrative. | MCF-OPS-020 |
| Capacity planning threshold | % of N-1 available capacity | 80 | Illustrative. | MCF-OPS-021 |
| Indicator reporting interval | months | 1 | Illustrative. | MCF-OPS-022 |
| Maximum phase imbalance | % | Site-specific (no default) | Set from UPS and transformer OEM limits. | MCF-OPS-023 |
| Operational reporting interval | months | 1 | Illustrative. | MCF-OPS-024 |

## 10 Evidence expectations by claim type

| Claim type | AL | Profile tier | Controls in this domain | Sufficiency floors applied |
|---|---|---|---|---|
| DESIGN | AL2 | CP-1 | MCF-OPS-009 | S3 |
| IMPLEMENTATION | AL3 | CP-2 | MCF-OPS-002, MCF-OPS-005, MCF-OPS-017 | S3, S4 |
| OPERATION | AL4 | CP-3 | MCF-OPS-001, MCF-OPS-003, MCF-OPS-004, MCF-OPS-006, MCF-OPS-007, MCF-OPS-008, MCF-OPS-010, MCF-OPS-011, MCF-OPS-012, MCF-OPS-013, MCF-OPS-014, MCF-OPS-015, MCF-OPS-018, MCF-OPS-019, MCF-OPS-021, MCF-OPS-022, MCF-OPS-023, MCF-OPS-024 | S4 |
| EFFECTIVENESS | AL5 | CP-4 | MCF-OPS-016, MCF-OPS-020 | S4 |

OPS is predominantly an OPERATION domain: most of its controls assert that a practice operates as intended over a representative period and across states. The evidence pattern is E2+E3 over the period, with E6 observation and interview to confirm practice.

**OPERATION claims.** The assessor should draw samples from the source system that records the activity (CMMS work orders, permit register, access-control attendance, BMS/EPMS alarm logs, gateway or change-tool logs), not from the curated register the control owner maintains, and then reconcile. Typical reconciliations: non-routine work orders → MOPs (MCF-OPS-006); permits → authorisation register (MCF-OPS-004); BMS overrides and forced points → temporary configuration register (MCF-OPS-019); configuration drift and device logs → change records (MCF-OPS-018); CMMS overdue → deferred maintenance register (MCF-OPS-012). Period coverage should include night, weekend and holiday shifts and at least one MAINTENANCE period on a redundant system.

**IMPLEMENTATION claims** (MCF-OPS-002, MCF-OPS-005, MCF-OPS-017) require reconciliation of documented state to the as-built and as-configured state: procedures walked down against equipment identifiers; baseline items compared with live configuration.

**DESIGN claims** (MCF-OPS-009) require E1 strategy documents with engineering approval and maintenance-state capacity analysis.

**EFFECTIVENESS claims** (MCF-OPS-016, MCF-OPS-020) require evidence that the practice achieves its objective: no recurrence of verified-closed failure modes; post-change validation that detected and reversed failed changes.

E6 evidence (interviews, shift observation, operator walkthrough of an EOP) is essential in this domain but, under AIDCF-008, requires corroboration for material technical-effectiveness assertions.

## 11 Assessment guidance

1. **Begin with time-to-impact.** Obtain MCF-DEP-003 time-to-impact values for power, cooling and control dependencies. These drive staffing (MCF-OPS-001), alarm priority (MCF-OPS-013) and EOP design (MCF-OPS-005).
2. **Sample from the system of record.** For every OPERATION control, define the population from the source system and record the selection basis. Curated registers are the thing being tested, not the population.
3. **Reconcile across controls.** Many OPS failures are only visible as inconsistencies between controls: a permit open in the register but absent from handover; an override in the BMS but absent from the temporary configuration register; a configuration change in device logs with no change record.
4. **Observe a live activity.** Where safe and authorised, observe a shift handover, an EOP walkthrough, a permit issue and a MOP execution. Observation is from a safe position as directed by the person in charge.
5. **Test the facilities–IT seam.** Pick a recent change on facility infrastructure and check that IT/platform owners assessed workload impact (checkpoint, drain); pick a recent IT change with a material load step and check that facilities approved it.
6. **Compute alarm metrics yourself.** Obtain raw alarm logs and compute rates, standing and chattering alarms for a normal period and an upset event. Compare with the alarm philosophy's targets.
7. **Check MAINTENANCE-state reality.** For a sampled maintenance on a redundant system, reconstruct the actual configuration during work from EPMS/BMS logs and compare with the MOP's declared redundancy and the current load.

**DG-OPS-REQ-003** For each OPERATION claim in this domain, the assessor shall record the source system from which the population was drawn and the reconciliation performed against the control owner's register; a sample drawn only from the control owner's register shall not support CONFORMING.

**DG-OPS-REQ-004** The assessor shall compute alarm performance metrics for MCF-OPS-013 from raw alarm logs covering at least one normal period and, where one occurred in the assessment period, one upset event, and shall record the event used.

## 12 Testing safety

OPS assessment involves presence in operational and hazardous areas. In addition to the per-control testing-safety statements:

- Assessors shall not operate, isolate, lock, tag, test or alter any equipment, and shall not enter a permit boundary unless included on the permit.
- Observation of MOP execution, permit issue, LOTO and condition-monitoring surveys (for example thermography of energised switchgear) is from a safe position directed by the person in charge, with PPE appropriate to the hazard (including arc-flash PPE where required by the site's electrical safety rules).
- No alarm shall be generated on a live system for assessment except under an approved test plan with operators informed; no staffing reduction shall be imposed to test coverage.
- Rehearsals of back-out procedures on facility systems (MCF-OPS-020), substitution exercises and any test involving hazardous energy require an approved MOP (MCF-OPS-006), permit (MCF-OPS-007), change approval (MCF-OPS-018) and authorisation by the facility operator's authorised person.
- Configuration capture (MCF-OPS-017, MCF-OPS-019) is read-only and authorised by the control-system owner.

## 13 UNKNOWN hot-spots

| Hot-spot | Typical UNKNOWN type | Typical severity | Resolution route |
|---|---|---|---|
| Attendance on nights, weekends and holidays | U1 / U5 | US3; US4 where CG-05/06/10 depend on manual action | Access-control records |
| Permit and LOTO records for contractor work | U1 / U2 | US4 (CG-04 CRITICAL) | Permit register; contractor records under evidence rights |
| Raw alarm logs (retention too short or not exportable) | U1 / U2 | US4 (CG-07 CRITICAL) | BMS/EPMS historian export; retention change |
| Device logs to reconcile unrecorded changes | U1 | US4 (CG-14 CRITICAL) | Device and controller logs; drift detection |
| Overrides and forced points on facility controllers | U2 | US3–US4 | Controller exports; OEM tools |
| Calibration status of control-loop sensors | U1 | US3; US4 where CG-07 relies on them | Calibration register; field labels |
| Provider operations evidence in colocation | U2 | US3–US4 | Provider evidence rights; witness |

## 14 Interfaces with other domains

| Domain | OPS provides | OPS receives |
|---|---|---|
| GOV | Operational reporting; deferred maintenance and risk exposure | Accountability, risk acceptance, competence management (GOV-02, GOV-06) |
| CAP | Service level measurement; capacity admission | Service Outcomes, envelope and demand (CAP-02, CAP-04, CAP-05) |
| DEP | Change records; staffing data | Time-to-impact; dependency graph for change impact; shared human dependencies (DEP-01, DEP-02) |
| PHY | Permits for work in fire, security and water zones | Zones and emergency shutdown governance (PHY-03, PHY-06) |
| POW | Operation and maintenance of electrical systems; switching under permit | Switching procedures, EPMS coverage, preventive maintenance requirements (POW-06) |
| THM | Operation of cooling and liquid systems; coolant monitoring | Maintenance states, sensor trust, control stability (THM-06) |
| CMP, STO, NET | Change and configuration control; workload coordination in MOPs | Baselines, upgrade testing, rollback readiness (CMP-04, NET-06) |
| RES | Incident records and RCAs; EOPs | Scenarios, crisis command, emergency change (RES-01, RES-06) |
| SUP | Ticket linkage for vendor access; contractor work control | Supplier service levels and vendor access controls (SUP-02, SUP-06) |
| SEC | Change records for security-relevant changes | Privileged access, automation authority and safe rollback (SEC-01, SEC-06) |
| EVA | Operational evidence (work orders, logs, permits) | Evidence repository, custody and expiry (EVA-01, EVA-06) |

## 15 Informative references

Document-level references; no clause-level reliance is implied.

- Uptime Institute Tier Standard: Operational Sustainability
- EN 50600 series (data centre facilities and infrastructures), in particular EN 50600-3-1 (management and operational information) and EN 50600-2-2 (power distribution)
- ISO/IEC 20000-1 (service management system requirements); ITIL 4 practice guides
- ISO 22320 (emergency management: incident management); ISO/IEC 27035 (information security incident management)
- IEC 62740 (root cause analysis); IEC 61025 (fault tree analysis); HSE HSG245 (investigating accidents and incidents)
- ISO 45001 (occupational health and safety management systems)
- HSE HSG250 (guidance on permit-to-work systems); HSE HSG85 (electricity at work: safe working practices); HSE HSG48 (reducing error and influencing behaviour); HSE HSG256 (managing shift work)
- BS EN 50110-1 (operation of electrical installations); NFPA 70E (electrical safety in the workplace); NFPA 70B (electrical equipment maintenance); NFPA 110 (emergency and standby power systems)
- OSHA 29 CFR 1910.147 (control of hazardous energy); ISO 14118 (prevention of unexpected start-up)
- IEC 60300-3-11 (reliability centred maintenance); SAE JA1011 (RCM evaluation criteria); ISO 55001 (asset management systems)
- ISO 17359 (condition monitoring and diagnostics of machines); ISO 20816 (mechanical vibration); IEC 60599 (dissolved gas analysis interpretation); IEC 60270 (partial discharge measurements)
- ISO 10012 (measurement management systems); ISO/IEC 17025 (testing and calibration laboratories)
- IEC 62682 (management of alarm systems for the process industries); ANSI/ISA-18.2 (management of alarm systems); EEMUA Publication 191 (alarm systems guide)
- SAE EIA-649C (configuration management standard); ISO 10007 (guidelines for configuration management)
- ASHRAE TC 9.9 thermal and liquid cooling guidelines
- AIDCF-003, AIDCF-004, AIDCF-008, AIDCF-010, AIDCF-013, AIDCF-014

## 16 Control summary

| Control | Title | Type | AL | Claim type | Gate mappings |
|---|---|---|---|---|---|
| MCF-OPS-001 | 24x7 Coverage | PREVENTIVE | AL4 | OPERATION | CG-13 (S); CG-10 (S) |
| MCF-OPS-002 | Role Clarity | DIRECTIVE | AL3 | IMPLEMENTATION | CG-13 (C); CG-14 (S) |
| MCF-OPS-003 | Shift Handover | PREVENTIVE | AL4 | OPERATION | CG-04 (S); CG-14 (S) |
| MCF-OPS-004 | Competence and Authorisation | PREVENTIVE | AL4 | OPERATION | CG-04 (C); CG-13 (S) |
| MCF-OPS-005 | Standard Operating Procedures | DIRECTIVE | AL3 | IMPLEMENTATION | CG-10 (S); CG-13 (S); CG-14 (S) |
| MCF-OPS-006 | Method Statements | PREVENTIVE | AL4 | OPERATION | CG-14 (C); CG-04 (S) |
| MCF-OPS-007 | Permit to Work | PREVENTIVE | AL4 | OPERATION | CG-04 (C) |
| MCF-OPS-008 | Lockout and Tagout | PREVENTIVE | AL4 | OPERATION | CG-04 (C) |
| MCF-OPS-009 | Maintenance Strategy | DIRECTIVE | AL2 | DESIGN | CG-05 (S); CG-06 (S) |
| MCF-OPS-010 | Condition Monitoring | DETECTIVE | AL4 | OPERATION | CG-05 (S); CG-06 (S) |
| MCF-OPS-011 | Calibration | PREVENTIVE | AL4 | OPERATION | CG-07 (S) |
| MCF-OPS-012 | Deferred Maintenance | CORRECTIVE | AL4 | OPERATION | CG-05 (S); CG-06 (S); CG-13 (S) |
| MCF-OPS-013 | Alarm Rationalisation | DETECTIVE | AL4 | OPERATION | CG-07 (C); CG-06 (S); CG-05 (S) |
| MCF-OPS-014 | Incident Response | CORRECTIVE | AL4 | OPERATION | CG-10 (S); CG-13 (S) |
| MCF-OPS-015 | Root Cause Analysis | CORRECTIVE | AL4 | OPERATION | CG-09 (S) |
| MCF-OPS-016 | Problem Elimination | CORRECTIVE | AL5 | EFFECTIVENESS | CG-14 (S) |
| MCF-OPS-017 | Configuration Baseline | PREVENTIVE | AL3 | IMPLEMENTATION | CG-14 (C); CG-02 (S); CG-07 (S) |
| MCF-OPS-018 | Change Assessment | PREVENTIVE | AL4 | OPERATION | CG-14 (C); CG-03 (S) |
| MCF-OPS-019 | Temporary Configuration | PREVENTIVE | AL4 | OPERATION | CG-14 (S); CG-07 (S); CG-04 (S) |
| MCF-OPS-020 | Rollback and Validation | CORRECTIVE | AL5 | EFFECTIVENESS | CG-14 (C); CG-10 (S) |
| MCF-OPS-021 | Capacity Review | DETECTIVE | AL4 | OPERATION | CG-05 (S); CG-06 (S) |
| MCF-OPS-022 | Service Level Monitoring | DETECTIVE | AL4 | OPERATION | none |
| MCF-OPS-023 | Resource Balancing | PREVENTIVE | AL4 | OPERATION | CG-05 (S); CG-06 (S); CG-09 (S) |
| MCF-OPS-024 | Operational Reporting | DIRECTIVE | AL4 | OPERATION | CG-13 (S) |

Key: (C) = CRITICAL role, (S) = SUPPORTING role, per AIDCF-010 gate roll-up. CG-11 and CG-12 are evaluated across all controls and are not mapped per control.

## 17 Worked synthetic example

> **Synthetic example.** All names, values and results below are invented for illustration. They do not describe any real facility, operator or assessment.

**Context.** Synthetic Capability Instance CI-SYN-TRN-03 is a training cluster in an owner-operated facility with N+1 UPS modules per hall and four CDUs per row in a lead-lag arrangement. The decision question asks whether the cluster can meet its availability outcome across NORMAL, MAINTENANCE and EMERGENCY states.

**Method statements (MCF-OPS-006).** The population was drawn from CMMS non-routine work orders (42 in 12 months); 12 were sampled. Eleven had approved MOPs with redundancy state per step and workload coordination. One CDU pump replacement was executed under a generic maintenance procedure with no MOP; the CDU pair was operated at N for four hours during a training run without checkpoint coordination. Result: PARTIAL (Finding).

**Configuration baseline (MCF-OPS-017).** Baseline covered SLDs, protection settings, BMS sequences, CDU setpoints and firmware versions. Live exports from four CDUs reconciled; one CDU had a supply-temperature setpoint 1 K below baseline with no change record. Result: PARTIAL (Finding: unrecorded drift).

**Change assessment (MCF-OPS-018).** Sampled changes had impact assessments and joint facilities–IT approval. Reconciling device logs found the CDU setpoint change above, made by a vendor engineer during a support session. Result: PARTIAL (Finding: change outside process). The vendor-session evidence was passed to the SUP assessor (MCF-SUP-022).

**Rollback and validation (MCF-OPS-020).** All sampled material changes had validation evidence and back-out plans. Result: CONFORMING.

**Permit to work and LOTO (MCF-OPS-007, MCF-OPS-008).** Permits for electrical, liquid-cooling and battery work were sampled; all were complete, cross-referenced and handed back, and LOTO records showed personal locks and live-dead-live testing. Results: CONFORMING. MCF-OPS-004 also CONFORMING. Together with the PHY, POW, THM and ENV CG-04 CRITICAL controls, CG-04 is evaluated separately.

**Alarm rationalisation (MCF-OPS-013).** The alarm philosophy and master alarm database existed. Metrics computed from raw logs for a utility-disturbance event showed an alarm flood, but the critical CDU and UPS alarms were at the highest priority with response procedures and were acknowledged within target. Standing alarms exceeded the philosophy target and had no action plan. Result: PARTIAL.

**Gate results.** CG-14 has CRITICAL controls MCF-OPS-006 (PARTIAL), MCF-OPS-017 (PARTIAL), MCF-OPS-018 (PARTIAL) and MCF-OPS-020 (CONFORMING); under the AIDCF-010 roll-up rule **CG-14 = FAIL**. CG-07 has MCF-OPS-013 PARTIAL as a CRITICAL control; **CG-07 = FAIL** regardless of the POW, THM and SEC CRITICAL results. A PARTIAL result never yields a gate PASS.

**Decision effect and actions.** FAIL on CG-14 and CG-07 prevents a REASONABLY_ASSURED decision; ceilings are those defined in AIDCF-010. Actions: require MOPs for all non-routine CDU work with checkpoint coordination; bring vendor support sessions under change control and approval; reconcile and correct the CDU setpoint; create a standing-alarm reduction plan with dated targets. Reassessment triggers: closure of the Findings with fresh E2/E3 evidence over a further sampling period.

**What the example shows.** Each individual lapse was small, but OPS controls are CRITICAL for change control and alarm integrity because the effect of small lapses accumulates in exactly the states (MAINTENANCE, EMERGENCY) where redundancy is lowest.
