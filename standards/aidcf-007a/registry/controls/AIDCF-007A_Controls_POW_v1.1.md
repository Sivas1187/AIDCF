# AIDCF-007A Control Catalogue — POW Electrical Power Infrastructure and Energy Continuity

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-POW](../../../aidcf-018-domain-guides/AIDCF-018-POW_Electrical_Power_and_Energy_Continuity_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-POW-001](#mcf-pow-001) | Utility Capacity | PREVENTIVE | OPERATION | AL4 | CG-05 | CG-03 |
| [MCF-POW-002](#mcf-pow-002) | Grid Quality | DETECTIVE | OPERATION | AL4 | — | CG-05 |
| [MCF-POW-003](#mcf-pow-003) | Connection Reliability | DIRECTIVE | DESIGN | AL2 | — | CG-03, CG-05, CG-09 |
| [MCF-POW-004](#mcf-pow-004) | Utility Contingency | RECOVERY | RESILIENCE | AL5 | — | CG-05, CG-10 |
| [MCF-POW-005](#mcf-pow-005) | Generator Capacity | PREVENTIVE | EFFECTIVENESS | AL5 | CG-05 | — |
| [MCF-POW-006](#mcf-pow-006) | Start Reliability | PREVENTIVE | OPERATION | AL4 | CG-05 | CG-07 |
| [MCF-POW-007](#mcf-pow-007) | Fuel Autonomy | PREVENTIVE | OPERATION | AL4 | CG-05 | — |
| [MCF-POW-008](#mcf-pow-008) | Fuel Replenishment | RECOVERY | RESILIENCE | AL5 | — | CG-05, CG-03, CG-10 |
| [MCF-POW-009](#mcf-pow-009) | UPS Topology | PREVENTIVE | IMPLEMENTATION | AL3 | CG-05 | CG-09, CG-02 |
| [MCF-POW-010](#mcf-pow-010) | Battery Condition | DETECTIVE | OPERATION | AL4 | CG-04 | CG-05 |
| [MCF-POW-011](#mcf-pow-011) | Runtime and Derating | PREVENTIVE | EFFECTIVENESS | AL5 | CG-05 | — |
| [MCF-POW-012](#mcf-pow-012) | Bypass Exposure | DETECTIVE | OPERATION | AL4 | — | CG-05, CG-09 |
| [MCF-POW-013](#mcf-pow-013) | Switchgear Integrity | PREVENTIVE | OPERATION | AL4 | CG-04 | CG-05 |
| [MCF-POW-014](#mcf-pow-014) | Selective Coordination | PREVENTIVE | IMPLEMENTATION | AL3 | CG-09 | CG-05 |
| [MCF-POW-015](#mcf-pow-015) | Busway and PDU Capacity | PREVENTIVE | OPERATION | AL4 | — | CG-05, CG-14 |
| [MCF-POW-016](#mcf-pow-016) | Earthing and Bonding | PREVENTIVE | IMPLEMENTATION | AL3 | CG-04 | CG-05 |
| [MCF-POW-017](#mcf-pow-017) | Voltage Quality | DETECTIVE | OPERATION | AL4 | — | CG-05 |
| [MCF-POW-018](#mcf-pow-018) | Harmonics | PREVENTIVE | OPERATION | AL4 | — | CG-05 |
| [MCF-POW-019](#mcf-pow-019) | Transient Ride-Through | PREVENTIVE | EFFECTIVENESS | AL5 | CG-05 | CG-06 |
| [MCF-POW-020](#mcf-pow-020) | Load-Step Response | PREVENTIVE | EFFECTIVENESS | AL5 | CG-05 | CG-03 |
| [MCF-POW-021](#mcf-pow-021) | EPMS Coverage | DETECTIVE | IMPLEMENTATION | AL3 | CG-07 | CG-05, CG-15 |
| [MCF-POW-022](#mcf-pow-022) | Preventive Maintenance | PREVENTIVE | OPERATION | AL4 | — | CG-05 |
| [MCF-POW-023](#mcf-pow-023) | Switching Procedures | PREVENTIVE | OPERATION | AL4 | CG-04 | CG-07, CG-14 |
| [MCF-POW-024](#mcf-pow-024) | Black-Start and Restoration | RECOVERY | RESILIENCE | AL5 | CG-10 | CG-05, CG-07 |

## POW-01 Utility and grid interface

### MCF-POW-001

**Utility Capacity** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Demonstrate that contracted and physically available utility import capacity covers the declared peak site demand, including AI training clusters at full power, cooling at design ambient and battery recharge after an outage, with margin and with a forecast that precedes deployments.

**Requirement.** The facility owner shall hold a connection agreement stating firm import capacity and any non-firm or curtailable portions, and shall maintain a site demand model that sums IT load at declared accelerator power limits, cooling and mechanical load at design ambient, losses, and UPS/BESS recharge load. The facility owner shall show firm capacity exceeds modelled peak demand by the declared margin, shall compare modelled with metered peak demand at least quarterly, and shall not commission additional AI capacity that would erode the margin without an approved capacity increase or load-limiting measure.

**Assessment criteria**

1. The connection agreement states firm import capacity, non-firm portions and any curtailment terms.
2. The demand model includes IT load at declared power limits, mechanical load at design ambient, distribution and conversion losses, and UPS/BESS recharge.
3. Firm capacity exceeds modelled peak demand by at least the declared margin.
4. Metered 15-minute or finer peak demand over the period is within the modelled value, or the model has been corrected.
5. Planned AI deployments in the next forecast horizon are included and a capacity gap, if any, has an approved remediation before deployment.
6. Transformer and incomer ratings in the as-built single-line diagram are consistent with the firm capacity and the demand model.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Margin of firm import capacity over modelled peak demand | % of firm capacity | 10 (illustrative) | Capability profile |
| Demand forecast horizon | months | 36 (illustrative) | Capability profile; utility lead times |
| Metered demand integration interval | minutes | 15 or finer | Utility tariff metering practice; finer resolution needed to capture AI load dynamics |

**Minimum evidence**

- Connection agreement and any curtailment/flexible connection terms
- Site demand model with assumptions (accelerator power limits, PUE at design ambient, recharge)
- Metered demand data from the revenue or EPMS meters for the period
- As-built single-line diagram with incomer and transformer ratings
- Capacity forecast and approved remediation actions

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E7 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; DEGRADED; RECOVERY |
| periodCoverage | Twelve months of metered demand including the seasonal cooling peak and peak AI utilisation. |
| independence | Demand model recomputed by the assessor from source data; metered data obtained from the revenue meter operator or EPMS export under observation. |
| mandatoryItems | Connection agreement; Demand model; Metered demand data; As-built single-line diagram |
| acceptableAlternatives | Utility capacity statement letter where the agreement is confidential, if it states firm capacity and curtailment terms |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-05 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | New AI cluster or accelerator generation with higher power limit; Change to connection agreement; Metered peak within margin; Utility network reinforcement or constraint notice |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION

**Assessment procedure**

1. Extract firm and non-firm capacity and curtailment terms from the agreement.
2. Rebuild the demand model from rack power limits, mechanical design data and recharge rates.
3. Compare with metered peaks at the finest available resolution.
4. Check margin and forecast deployments against firm capacity.
5. Reconcile incomer and transformer ratings on the single-line diagram.

**Gate mappings.** CG-05 Resilient electrical supply (CRITICAL); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to every site drawing utility power. For colocation tenants the provider's capacity allocation to the tenant's suite replaces the connection agreement.

**Lifecycle stages.** PLAN, DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, RECOVERY

**Failure modes addressed.** Peak demand exceeds firm capacity during seasonal cooling peak; Recharge load after outage trips incomers; Non-firm capacity relied on for critical load; Deployment commissioned before capacity upgrade

**Testing safety.** Desk-based analysis and meter data export; no switching or measurement inside energised enclosures.

**UNKNOWN rule.** If metered peak demand for the cooling peak season is unavailable, record a U5 UNKNOWN; CG-05 becomes UNKNOWN for the capacity criterion until data for that season exists.

**Ontology classes.** CapacityAssertion, Dependency, Resource, InfrastructureSystem · **Related controls.** MCF-POW-002, MCF-POW-004, MCF-POW-020, MCF-CAP-014

**Informative references.** EN 50600-2-2 (power supply and distribution); Distribution or transmission network connection codes of the jurisdiction (e.g. EU Network Code on Demand Connection); IEC 60076 (power transformers)

### MCF-POW-002

**Grid Quality** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Establish the actual quality of the utility supply at the point of common coupling (voltage variations, dips, swells, interruptions, unbalance, flicker and harmonics) and confirm that the facility's ride-through and conversion equipment is specified for it.

**Requirement.** The facility operator shall measure supply quality at each utility point of common coupling using power quality instruments conforming to IEC 61000-4-30 Class A, shall retain events and statistics for the declared period, and shall compare measured characteristics with the voltage characteristics assumed in the design basis and with the utility's declared characteristics. The facility operator shall report events that exceeded design assumptions to the electrical engineer responsible for MCF-POW-019 for evaluation.

**Assessment criteria**

1. Class A power quality monitoring is installed at each utility point of common coupling.
2. Statistics for voltage magnitude, unbalance, flicker and harmonics are available for the period.
3. All dips, swells and interruptions in the period are logged with magnitude and duration.
4. Measured characteristics are compared with the design basis and the utility's declared characteristics.
5. Events outside design assumptions have an engineering evaluation.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Supply voltage variation assumed in design | % of nominal | ±10 (illustrative) | EN 50160 voltage characteristics or utility declaration |
| Power quality data retention | months | 24 (illustrative) | Capability profile |

**Minimum evidence**

- Power quality instrument list and Class A certificates
- PQ statistics and event logs
- Design basis voltage assumptions
- Utility declared characteristics or connection terms
- Engineering evaluations of exceeding events

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | Twelve months of continuous monitoring. |
| independence | PQ data exported under observation; evaluation by an electrical engineer independent of operations where events exceeded design. |
| mandatoryItems | PQ event logs; PQ statistics |
| acceptableAlternatives | Utility-provided PQ data at the PCC, if Class A and covering the period |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-05. |
| reassessmentTriggers | Utility network change; New large load or generator nearby; Unexplained UPS transfers |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW, INSPECTION

**Assessment procedure**

1. Confirm instrument class and location at each PCC.
2. Analyse event logs and statistics for the period.
3. Compare with design assumptions and utility declaration.
4. Review evaluations of exceeding events.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies to sites with a direct utility connection. Colocation tenants obtain provider PQ data at the tenant's UPS input.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Frequent dips cause UPS battery cycling and premature ageing; Unbalance overheats transformers; Grid harmonics excite filter resonance

**Testing safety.** Instrument data is retrieved via EPMS; installation of portable PQ loggers inside energised panels is performed only by authorised persons under permit with appropriate PPE.

**UNKNOWN rule.** If no Class A data exists at the PCC, record a U1 UNKNOWN; ride-through claims under MCF-POW-019 are limited to design evidence.

**Ontology classes.** Resource, Event, Dependency · **Related controls.** MCF-POW-017, MCF-POW-019, MCF-POW-018

**Informative references.** IEC 61000-4-30 (power quality measurement methods); EN 50160 (voltage characteristics of public supply); IEEE 1159 (monitoring electric power quality)

### MCF-POW-003

**Connection Reliability** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Establish the real independence and reliability of the utility connection(s), including shared upstream substations, transmission circuits and protection schemes, so that claimed dual feeds are not a single upstream fault domain.

**Requirement.** The facility owner shall obtain from the network operator the upstream topology of each utility feed to the first point of independent supply, and shall identify shared substations, busbars, circuits, rights-of-way and protection schemes. The facility owner shall record the historic interruption performance of each feed, and shall not describe feeds as independent in the design basis unless no shared upstream element is identified.

**Assessment criteria**

1. Upstream topology to the first independent source point is documented for each feed.
2. Shared upstream elements (substation, bus, circuit, route, protection) are listed or explicitly none.
3. Interruption history for each feed over the declared period is recorded.
4. Design basis claims of feed independence are consistent with the shared-element list.
5. Residual common-mode exposures are reflected in generator and UPS autonomy sizing.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Interruption history period | years | 5 (illustrative) | Capability profile; network operator data |

**Minimum evidence**

- Network operator topology statement
- Shared-element list
- Interruption history
- Design basis feed independence statement

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E7 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY |
| periodCoverage | Current topology; interruption history for the declared period. |
| independence | Topology from the network operator, not the facility's own assumption. |
| mandatoryItems | Network operator topology statement |
| acceptableAlternatives | Independent grid study commissioned by the owner using network operator data |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-03, CG-05, CG-09. |
| reassessmentTriggers | Network operator reconfiguration; New substation; Multi-feed outage |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INQUIRY

**Assessment procedure**

1. Obtain topology and trace each feed upstream.
2. Identify shared elements and compare with design basis claims.
3. Review interruption history and correlation between feeds.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING); CG-05 Resilient electrical supply (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to all utility-connected sites; most significant where the design basis claims dual independent feeds.

**Lifecycle stages.** PLAN, DESIGN, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY

**Failure modes addressed.** Two feeds from the same grid substation bus; Shared overhead route damaged by storm; Common intertrip scheme

**Testing safety.** Desk-based.

**UNKNOWN rule.** If the network operator does not provide upstream topology, record a U10 dependency UNKNOWN and treat feeds as one fault domain for CG-05 sizing.

**Ontology classes.** Dependency, FaultDomain, InfrastructureSystem · **Related controls.** MCF-POW-001, MCF-POW-004, MCF-DEP-005, MCF-DEP-009

**Informative references.** IEEE 3006 series (power system reliability); EN 50600-2-2 (power supply and distribution)

### MCF-POW-004

**Utility Contingency** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure the facility can sustain declared outcomes through prolonged utility interruption, grid emergency instructions, curtailment and demand-response events, and can meet its grid connection obligations as a large load.

**Requirement.** The facility owner shall maintain a utility contingency plan covering prolonged interruption, grid-operator curtailment or disconnection instructions, demand-response commitments and re-energisation constraints. The facility owner shall define, for each event type, which AI workloads are shed or throttled, how cooling and IT load are reduced in a controlled sequence, the decision authority, and the communications with the network operator, and shall exercise the plan at the declared interval.

**Assessment criteria**

1. The plan covers prolonged outage, curtailment instruction, demand response and re-energisation.
2. Load-reduction steps identify workloads (by class or cluster), expected MW reduction and time to achieve it.
3. Workload throttling or checkpoint-and-pause is demonstrated in an exercise to achieve the declared reduction within the declared time.
4. Contractual obligations as a large load (notification, ride-through, ramp limits) are listed and mapped to procedures.
5. Decision authority and network-operator contacts are current.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Time to achieve declared load reduction on curtailment instruction | minutes | 15 (illustrative) | Connection agreement; capability profile |
| Plan exercise interval | months | 12 (illustrative) | Capability profile |

**Minimum evidence**

- Utility contingency plan
- Connection obligations list
- Exercise records with achieved MW reduction and time
- Contact and authority lists

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E3; E4 |
| optionalClasses | E6; E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | EMERGENCY; DEGRADED; RECOVERY |
| periodCoverage | Most recent exercise within interval; twelve months of curtailment events. |
| independence | Exercise observed by the assessor or a party independent of the operations team. |
| mandatoryItems | Utility contingency plan; Exercise record |
| acceptableAlternatives | Record of a real curtailment event handled per plan |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-05, CG-10. |
| reassessmentTriggers | Change in connection agreement or flexibility contract; Grid emergency event; New AI cluster with different shed characteristics |

**Assessment methods.** DOCUMENT_REVIEW, SCENARIO_EXERCISE, ANALYSIS

**Assessment procedure**

1. Review plan coverage against event types.
2. Trace load-reduction steps to scheduler or power-capping mechanisms.
3. Review or observe an exercise and compare achieved reduction with plan.
4. Check obligations mapping and contacts.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to sites with grid connection agreements that include curtailment, flexibility or large-load obligations, and to all sites for prolonged outage planning.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** EMERGENCY, DEGRADED, RECOVERY

**Failure modes addressed.** Curtailment instruction cannot be met in time; Uncontrolled shedding loses training state; Re-energisation inrush violates connection limits

**Testing safety.** Exercises use workload throttling or scheduler controls; no electrical switching is performed for the exercise unless separately authorised under MCF-POW-023.

**UNKNOWN rule.** If the plan has never been exercised, record a U5 UNKNOWN; the RESILIENCE claim is UNKNOWN and supports design only.

**Ontology classes.** FailureScenario, Safeguard, Dependency, OperatingState · **Related controls.** MCF-POW-001, MCF-POW-020, MCF-RES-002, MCF-CMP-010

**Informative references.** EU Network Code on Demand Connection (Regulation (EU) 2016/1388); Network operator large-load connection requirements of the jurisdiction; ISO 22301 (business continuity management)

## POW-02 Generation and fuel

### MCF-POW-005

**Generator Capacity** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Demonstrate that standby or prime generation can carry the declared critical load, including mechanical load and AI load dynamics, with the declared redundancy, at site design ambient and altitude, for the declared duration.

**Requirement.** The facility owner shall size generation using the ISO 8528-1 rating class appropriate to the duty (for example data-centre continuous power where unlimited running hours at variable load are required) with derating for design ambient temperature, altitude and fuel. The facility owner shall verify by load-bank or real-load testing at commissioning and at the declared interval that each generator, and the paralleled system, carries its rated load at the declared redundancy with one unit out of service.

**Assessment criteria**

1. Generator rating class and kW rating per ISO 8528-1 are recorded and are appropriate to the declared duty and running hours.
2. Derated capacity at site design ambient and altitude covers critical IT plus mechanical load with the declared redundancy (for example N+1) available.
3. Commissioning and periodic load-bank or real-load tests reached the declared load and duration for each unit and the paralleled system.
4. Generator capacity is reconciled to the current demand model in MCF-POW-001.
5. Radiator and air-intake performance at design ambient (including recirculation in the yard) is accounted for in derating.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Generator redundancy | topology | N+1 (illustrative) | Capability profile; outcome tolerance |
| Site design ambient for generator derating | °C | site extreme design value (ASHRAE climatic data, n-year return; illustrative n=20) | ASHRAE Handbook climatic design data; capability profile |
| Periodic load-bank test duration at rated load | hours | 4 (illustrative) | NFPA 110 or national emergency power practice; capability profile |

**Minimum evidence**

- Generator datasheets with ISO 8528 rating class
- Derating calculation for ambient and altitude
- Commissioning load-bank reports
- Periodic load test records
- Yard airflow/recirculation study

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Commissioning test plus the most recent periodic load test within interval. |
| independence | Load tests witnessed by a party independent of the generator maintenance contractor. |
| mandatoryItems | Rating class evidence; Derating calculation; Load test reports |
| acceptableAlternatives | Recorded real-load operation during a utility outage at or above the declared load, with EPMS data |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-05 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Increase in critical load; Generator replacement or controller change; Design ambient revision; Failed load test |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, TEST, REPERFORMANCE

**Assessment procedure**

1. Verify rating class and duty match.
2. Recompute derated capacity at design ambient and altitude.
3. Compare with demand model and redundancy with one unit out.
4. Review load test records for load, duration and anomalies.
5. Witness a load test where scheduled.

**Gate mappings.** CG-05 Resilient electrical supply (CRITICAL)

**Applicability.** Applies to sites with on-site generation for critical load. Not applicable where the declared outcome tolerance accepts loss on utility failure beyond UPS autonomy and this is approved.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Generators derate below load during heatwave; Prime-rated units used beyond rating class; Paralleled system cannot carry load with one unit out

**Testing safety.** Hazardous-energy activity. Tests and switching are performed only by authorised persons under the site electrical safety rules, an approved method statement and permit to work, with written authorisation from the facility owner's authorised engineer; assessors witness from outside the arc-flash boundary and never operate equipment. Load-bank connection points are engineered; temporary cabling is inspected before energising.

**UNKNOWN rule.** If no load test at rated load exists within the interval, record a US4 UNKNOWN against CG-05.

**Ontology classes.** CapacityAssertion, InfrastructureSystem, TestRecord · **Related controls.** MCF-POW-006, MCF-POW-007, MCF-ENV-021, MCF-POW-020

**Informative references.** ISO 8528 series (reciprocating engine generating sets); NFPA 110 (emergency and standby power systems); EN 50600-2-2 (power supply and distribution)

### MCF-POW-006

**Start Reliability** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Demonstrate that generators start, synchronise and accept load within the time the UPS or BESS autonomy allows, on every demand, including after long standby periods and in cold or hot ambient.

**Requirement.** The facility operator shall test each generator by monthly start and run tests at the declared load and by periodic transfer tests through the automatic transfer or paralleling controls, shall record start time, time to ready-to-load and anomalies, shall maintain starting systems (batteries or air, jacket-water heating, fuel priming), and shall treat any failed or delayed start as an incident with root cause analysis.

**Assessment criteria**

1. Monthly start/run tests at the declared load and duration are recorded for every unit.
2. Recorded start-to-ready-to-load time is within the declared limit and within the UPS/BESS autonomy with margin.
3. Starting batteries or air systems, jacket-water heaters and fuel priming are maintained and monitored.
4. Failed or delayed starts in the period have root cause and corrective action.
5. Paralleling or transfer control sequences have been tested end to end at the declared interval.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum start-to-load-acceptance time | s | 10 (illustrative; NFPA 110 Type 10 defines 10 s) | NFPA 110 type classification; UPS autonomy |
| Monthly test load | % of nameplate | 30 (illustrative) | NFPA 110 monthly exercise practice |
| Start reliability threshold for incident review | failed or delayed starts per year | 0 (illustrative) | Capability profile |

**Minimum evidence**

- Generator test logs with times
- Controller event logs
- Starting system maintenance records
- Incident and RCA records
- End-to-end transfer test reports

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Twelve months of monthly tests including winter and summer. |
| independence | Test logs reconciled to controller event logs extracted under observation. |
| mandatoryItems | Monthly test logs; Controller event logs |
| acceptableAlternatives | Real utility-outage starts with controller logs, if timing is recorded |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-05 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Failed start; Controller firmware change; Starting system replacement |

**Assessment methods.** ANALYSIS, RECONCILIATION, TEST, SAMPLING

**Assessment procedure**

1. Analyse twelve months of tests for completeness, timing and load.
2. Reconcile manual logs to controller event logs.
3. Review starting system maintenance and alarms.
4. Review failed or delayed starts and RCA.
5. Witness a monthly test where scheduled.

**Gate mappings.** CG-05 Resilient electrical supply (CRITICAL); CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies to all critical-load generators.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Starting battery failure (AIDCF-004 X01); Fuel line air lock after maintenance; Paralleling controller fails to close breaker; Cold-start delay exceeds UPS autonomy

**Testing safety.** Hazardous-energy activity. Tests and switching are performed only by authorised persons under the site electrical safety rules, an approved method statement and permit to work, with written authorisation from the facility owner's authorised engineer; assessors witness from outside the arc-flash boundary and never operate equipment. Transfer tests with live critical load require approval of the test window and confirmation that UPS/BESS autonomy and redundancy are healthy before starting.

**UNKNOWN rule.** If monthly test records are missing for any unit for more than one month, or controller logs cannot corroborate timing, record a US4 UNKNOWN against CG-05.

**Ontology classes.** InfrastructureSystem, TestRecord, FailureMode, Event · **Related controls.** MCF-POW-005, MCF-POW-011, MCF-POW-021, MCF-OPS-010

**Informative references.** NFPA 110 (emergency and standby power systems); ISO 8528 series (generating sets)

### MCF-POW-007

**Fuel Autonomy** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Demonstrate that on-site fuel stored, usable and of acceptable quality supports generation at the declared load for the declared autonomy, without relying on deliveries during that period.

**Requirement.** The facility operator shall maintain usable on-site fuel (excluding unusable tank bottoms and day-tank minimums) sufficient for the declared autonomy at the declared load, using measured consumption curves, and shall keep the minimum stock level as an alarmed threshold. The facility operator shall test fuel quality at the declared interval against the applicable fuel specification, shall polish or replace fuel that fails, and shall maintain fuel transfer pumps and controls in a redundant configuration matching the generator redundancy.

**Assessment criteria**

1. Usable fuel volume is calculated excluding unusable volumes and is at or above the minimum level for the declared autonomy at the declared load.
2. Consumption is based on measured or OEM curves at the declared load, not nameplate maximum only.
3. Fuel level telemetry with a minimum-stock alarm exists and is reconciled to dip or delivery records.
4. Fuel quality tests at the declared interval meet the fuel specification, or remediation is recorded.
5. Fuel transfer pumps, controls and piping have no single point of failure that disables more than the generator redundancy allows.
6. For renewable diesel (HVO) or blends, OEM approval and storage stability are documented.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| On-site fuel autonomy at declared load | hours | 48 (illustrative) | Capability profile; outcome tolerance and replenishment risk |
| Fuel quality test interval | months | 6 (illustrative) | Capability profile; fuel specification (EN 590, ASTM D975 or EN 15940) |

**Minimum evidence**

- Autonomy calculation with usable volumes and consumption curve
- Fuel level telemetry and alarm configuration
- Dip and delivery reconciliation
- Fuel test certificates
- Fuel system schematic showing pump redundancy

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; EMERGENCY; MAINTENANCE |
| periodCoverage | Twelve months of levels and tests. |
| independence | Fuel test by an accredited laboratory; autonomy recalculated by the assessor. |
| mandatoryItems | Autonomy calculation; Fuel level records; Fuel test certificates |
| acceptableAlternatives |  |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-05 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Load increase; Tank modification; Fuel type change; Failed fuel test |

**Assessment methods.** ANALYSIS, RECONCILIATION, DOCUMENT_REVIEW, INSPECTION

**Assessment procedure**

1. Recompute usable volume and autonomy at declared load.
2. Reconcile telemetry to dips and deliveries.
3. Review fuel test certificates.
4. Trace fuel transfer system for single points of failure.

**Gate mappings.** CG-05 Resilient electrical supply (CRITICAL)

**Applicability.** Applies to sites with liquid-fuelled generation. Gas-fuelled sites substitute supply-pressure and pipeline-dependency evidence and are assessed under MCF-POW-008 for supply continuity.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, EMERGENCY, MAINTENANCE

**Failure modes addressed.** Autonomy overstated by counting unusable volume; Microbial contamination blocks filters; Single transfer pump failure starves day tanks

**Testing safety.** Fuel sampling follows the site's fuel handling procedure (ignition-source control, spill kit); assessors do not take samples.

**UNKNOWN rule.** If usable volume cannot be established, record a US4 UNKNOWN against CG-05 for autonomy.

**Ontology classes.** Resource, CapacityAssertion, InfrastructureSystem · **Related controls.** MCF-POW-008, MCF-ENV-019, MCF-POW-005

**Informative references.** NFPA 110 (emergency and standby power systems); NFPA 30 (flammable and combustible liquids); EN 590 / ASTM D975 / EN 15940 (fuel specifications)

### MCF-POW-008

**Fuel Replenishment** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure that fuel can be replenished before on-site autonomy is exhausted during a regional emergency, when road access, supplier capacity and competing priority customers are constrained.

**Requirement.** The facility owner shall hold fuel supply contracts with at least the declared number of independent suppliers, specifying guaranteed delivery lead time during declared emergencies, priority status and delivery capacity. The facility operator shall maintain a refuelling procedure that includes delivery while generators run, and shall exercise a delivery under emergency conditions or verify supplier capability at the declared interval.

**Assessment criteria**

1. Contracts with the declared number of independent suppliers (not sharing a terminal) exist.
2. Guaranteed emergency lead time is shorter than on-site autonomy by the declared margin.
3. Supplier delivery capacity covers consumption at declared load for the outage duration being planned.
4. A refuelling-while-running procedure exists and has been performed or exercised.
5. Supplier capability was verified within the interval (exercise or real delivery record).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Guaranteed emergency resupply lead time | hours | 12 (illustrative) | Supply contracts; capability profile |
| Independent fuel suppliers | count | 2 (illustrative) | Capability profile |

**Minimum evidence**

- Fuel supply contracts
- Supplier terminal locations
- Refuelling procedure
- Delivery exercise or real delivery records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E3; E4 |
| optionalClasses | E5; E6 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | EMERGENCY; RECOVERY |
| periodCoverage | Current contracts; exercise within twelve months. |
| independence | Contracts reviewed directly; supplier capability confirmed with the supplier. |
| mandatoryItems | Fuel supply contracts; Refuelling procedure |
| acceptableAlternatives | Government or utility priority fuel scheme membership with documented terms |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-05, CG-03, CG-10. |
| reassessmentTriggers | Supplier change; Regional fuel disruption; Load increase reducing autonomy |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY, SCENARIO_EXERCISE

**Assessment procedure**

1. Review contracts for lead time, priority and capacity.
2. Check supplier independence (terminal, transport).
3. Compare lead time with autonomy.
4. Review or observe a delivery exercise.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies wherever declared outage tolerance exceeds on-site fuel autonomy. Where autonomy alone covers the declared outage scenario, the control is assessed at DESIGN depth only.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** EMERGENCY, RECOVERY

**Failure modes addressed.** Both suppliers served from one terminal; Delivery blocked by flood; Supplier prioritises hospitals in regional emergency

**Testing safety.** Refuelling-while-running exercises follow the fuel handling procedure with fire watch; assessors observe from outside the delivery hazard zone.

**UNKNOWN rule.** If emergency lead time is not contractually defined, record a U10 dependency UNKNOWN and limit CG-05 conclusions to on-site autonomy.

**Ontology classes.** Dependency, Resource, FailureScenario · **Related controls.** MCF-POW-007, MCF-PHY-003, MCF-SUP-019, MCF-DEP-014

**Informative references.** NFPA 110 (emergency and standby power systems); ISO 22301 (business continuity management)

## POW-03 UPS and energy storage

### MCF-POW-009

**UPS Topology** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Demonstrate that the as-built UPS and critical distribution topology (N, N+1, 2N, distributed or block redundant, or rack-level battery backup) delivers the declared Service Outcomes in every declared operating state, judged by failure analysis rather than by topology label.

**Requirement.** The electrical engineer of record shall document the UPS topology and IEC 62040-3 performance classification of each system, and shall perform a failure analysis that, for every single component failure and every planned maintenance state, identifies the critical load that remains supported and the resulting loading of surviving modules. The facility owner shall reconcile the as-built single-line diagram to the analysis and shall not claim a redundancy level the analysis does not support for the declared load.

**Assessment criteria**

1. The as-built single-line diagram reconciles to the installed UPS, static switch and distribution configuration in a site inspection sample.
2. Each UPS system's IEC 62040-3 classification (e.g. VFI) and operating mode (double conversion, eco-mode) is recorded.
3. A failure analysis covers every single UPS module, battery string, static switch and distribution board failure and every planned maintenance state.
4. In each analysed state, surviving modules remain within rating at the declared load including AI load swings; for distributed redundant designs, load reallocation after a failure is shown.
5. The redundancy claim stated in reports matches the analysis outcome at the current load.
6. Rack-level battery backup units, where used, are included and their interaction with upstream UPS is analysed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Declared UPS redundancy | topology | 2N or distributed redundant (illustrative) | Capability profile |
| Maximum normal-state loading of each path in a 2N design | % of path rating | 45 (illustrative) | Capability profile; failure analysis |

**Minimum evidence**

- As-built single-line diagram
- UPS datasheets with IEC 62040-3 classification
- Failure and maintenance-state analysis
- Load data per UPS and path
- Inspection reconciliation

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E7 |
| optionalClasses | E4; E5 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED; TRANSITION |
| periodCoverage | Current configuration and twelve months of path loading. |
| independence | Failure analysis reviewed by an electrical engineer independent of the designer or operator. |
| mandatoryItems | As-built single-line diagram; Failure and maintenance-state analysis; Path load data |
| acceptableAlternatives | Independent engineer's topology review report covering the same states |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-05 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Load growth; UPS module addition or removal; Change to eco-mode; Distribution reconfiguration |

**Assessment methods.** RECONCILIATION, ANALYSIS, INSPECTION

**Assessment procedure**

1. Reconcile single-line diagram to installed equipment in a sample.
2. Review failure analysis completeness against component and maintenance-state list.
3. Recompute surviving-module loading using current and peak AI load.
4. Compare redundancy claims in reports with analysis results.

**Gate mappings.** CG-05 Resilient electrical supply (CRITICAL); CG-09 Failure containment (SUPPORTING); CG-02 Boundary and architecture integrity (SUPPORTING)

**Applicability.** Applies to all UPS-backed critical load. For AI clusters deliberately designed without UPS on accelerator load (relying on checkpointing), the analysis records that decision and its approval and remains applicable to cooling and control loads.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED, TRANSITION

**Failure modes addressed.** Distributed redundant reserve consumed by growth; Maintenance state leaves load on single module; Topology label 2N but shared output switchboard; Eco-mode transfer exposes load to grid transients

**Testing safety.** Inspection only; panel covers are not removed. Load data is obtained from EPMS.

**UNKNOWN rule.** If the as-built single-line diagram cannot be reconciled, record a US4 UNKNOWN against CG-05 and a U5 against CG-02 architecture integrity.

**Ontology classes.** ArchitectureSnapshot, FaultDomain, CapacityAssertion, InfrastructureSystem · **Related controls.** MCF-POW-011, MCF-POW-012, MCF-POW-020, MCF-RES-005

**Informative references.** IEC 62040-3 (UPS performance and test requirements); IEC 62040-1 (UPS safety); EN 50600-2-2 (power supply and distribution); IEEE 3006 series (reliability)

### MCF-POW-010

**Battery Condition** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure UPS, BESS and rack-level batteries retain the capacity assumed in runtime claims and that lithium-ion and lead-acid hazards (thermal runaway, off-gassing, hydrogen evolution) are detected and managed before they cause fire or loss of energy storage.

**Requirement.** The facility operator shall monitor battery condition continuously (cell or block voltage, temperature, internal resistance or impedance, and for lithium-ion the battery management system state of health and alarms), shall perform capacity tests at the declared interval, and shall replace batteries at the end-of-life capacity threshold. The facility owner shall hold a battery safety assessment for each lithium-ion installation, using large-scale fire test data (for example UL 9540A) to set separation, ventilation, explosion control and detection, and shall maintain hydrogen ventilation for vented lead-acid rooms.

**Assessment criteria**

1. Continuous battery monitoring covers every string or rack and alarms to a staffed location.
2. Capacity tests at the declared interval show every string above the end-of-life threshold, or replacement is scheduled before the next interval.
3. Lithium-ion BMS alarms (over-temperature, cell imbalance, communication loss) are configured, routed and acted on within the declared time.
4. A battery safety assessment exists for each lithium-ion installation and its required measures (separation, explosion control, off-gas detection, suppression) are installed.
5. Rack-level battery backup units are inventoried, monitored and included in the safety assessment.
6. Vented lead-acid rooms have ventilation sized for hydrogen evolution and it is interlocked or alarmed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Battery end-of-life capacity threshold | % of rated capacity | 80 | IEEE 450 / IEEE 1188 replacement criterion for lead-acid; OEM criterion for lithium-ion |
| Battery capacity test interval | months | 12 (illustrative) | Capability profile; IEEE 450/1188 |
| BMS critical alarm response time | minutes | 15 (illustrative) | Capability profile |

**Minimum evidence**

- Battery monitoring configuration and alarm routing
- Capacity test reports
- BMS alarm logs and responses
- Battery safety assessment with UL 9540A or equivalent data
- Ventilation design and tests for lead-acid rooms
- Rack BBU inventory

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4; E5 |
| optionalClasses | E7 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED; EMERGENCY |
| periodCoverage | Twelve months of monitoring data and the latest capacity test cycle. |
| independence | Battery safety assessment by a fire or battery safety engineer independent of the supplier; capacity tests witnessed or reviewed independently. |
| mandatoryItems | Monitoring alarm configuration; Capacity test reports; Battery safety assessment (Li-ion) |
| acceptableAlternatives | Continuous impedance trending with OEM-validated correlation in place of discharge test for VRLA, if the OEM supports it |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-04 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Battery replacement or chemistry change; BMS firmware change; Thermal event; Ambient change in battery room |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW, INSPECTION, TEST

**Assessment procedure**

1. Review monitoring coverage and alarm routing.
2. Analyse capacity test results against threshold.
3. Review BMS alarm handling in the period.
4. Review the battery safety assessment and inspect required measures.
5. Inventory rack BBUs and confirm monitoring.

**Gate mappings.** CG-04 Life safety and hazardous energy (CRITICAL); CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies to all battery energy storage supporting critical load, including UPS strings, BESS and rack-level BBUs. Supercapacitor-only systems apply monitoring and safety elements.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE, DECOMMISSION · **Operating states.** NORMAL, MAINTENANCE, DEGRADED, EMERGENCY

**Failure modes addressed.** Lithium-ion thermal runaway propagating between racks; Hydrogen accumulation in lead-acid room; String capacity below runtime assumption; BMS communication loss hides cell fault

**Testing safety.** Discharge capacity tests are hazardous-energy activities and also reduce autonomy: they are performed by authorised persons under permit with the string isolated from critical load or with redundancy confirmed, written authorisation, and battery-hazard PPE. No test is performed on a lithium-ion string with an active BMS fault.

**UNKNOWN rule.** If no battery safety assessment exists for a lithium-ion installation, record a US4 UNKNOWN against CG-04; hazardous testing in that room is not authorised until resolved.

**Ontology classes.** Hazard, AssetInstance, Safeguard, InfrastructureSystem · **Related controls.** MCF-POW-011, MCF-PHY-021, MCF-ENV-017, MCF-THM-019

**Informative references.** IEC 62619 (safety of industrial lithium batteries); IEC 62485 (safety of secondary battery installations); NFPA 855 (stationary energy storage systems); UL 9540 / UL 9540A (ESS safety and thermal runaway fire test method); IEEE 450 and IEEE 1188 (lead-acid battery maintenance)

### MCF-POW-011

**Runtime and Derating** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Demonstrate that UPS and BESS runtime at the declared load, at end-of-life battery capacity and worst-case room temperature, exceeds the time needed for generators to accept load (or for orderly workload preservation where no generation exists) with margin.

**Requirement.** The electrical engineer shall calculate runtime per UPS system at the declared load using end-of-life capacity and the battery temperature derating at the highest declared battery room temperature, and shall compare it with the generator start-to-load time and the time needed to checkpoint or gracefully pause AI workloads. The facility operator shall verify runtime by a discharge test at the declared interval and shall recalculate after load growth.

**Assessment criteria**

1. Runtime calculations use end-of-life capacity, current declared load and worst-case battery temperature.
2. Calculated runtime exceeds generator start-to-load time plus the declared margin.
3. Where generation is absent or fails, runtime exceeds the time needed to complete declared workload preservation (checkpoint or pause) demonstrated by CMP/STO controls.
4. A discharge test at the declared interval confirmed runtime at or above calculation at a representative load.
5. Recalculation was performed after each load increase above the declared threshold.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Minimum UPS/BESS runtime at declared load, end of life | minutes | 5 (illustrative) | Capability profile; generator start time and workload preservation time |
| Load growth threshold triggering runtime recalculation | % of declared load | 10 (illustrative) | Capability profile |

**Minimum evidence**

- Runtime calculation
- Battery temperature records
- Discharge test reports
- Workload preservation timing evidence from CMP/STO
- Recalculation records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; EMERGENCY; MAINTENANCE |
| periodCoverage | Latest discharge test within interval; twelve months of loads and battery temperatures. |
| independence | Runtime recalculated by the assessor; test witnessed independently. |
| mandatoryItems | Runtime calculation; Discharge test report |
| acceptableAlternatives | Recorded real-event discharge with EPMS data of sufficient duration and load |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-05 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Load increase above threshold; Battery replacement; Battery room temperature change; Generator start-time change |

**Assessment methods.** ANALYSIS, REPERFORMANCE, TEST

**Assessment procedure**

1. Reperform runtime calculation from current load and battery data.
2. Compare with generator start time and workload preservation time.
3. Review discharge test conditions and results.
4. Confirm recalculation after load increases.

**Gate mappings.** CG-05 Resilient electrical supply (CRITICAL)

**Applicability.** Applies to all UPS and BESS supporting critical load.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, EMERGENCY, MAINTENANCE

**Failure modes addressed.** Runtime at end of life below generator start time; Battery room overheating reduces capacity; Load growth erodes runtime unnoticed (AIDCF-004 X01)

**Testing safety.** Hazardous-energy activity. Tests and switching are performed only by authorised persons under the site electrical safety rules, an approved method statement and permit to work, with written authorisation from the facility owner's authorised engineer; assessors witness from outside the arc-flash boundary and never operate equipment. Discharge tests on live systems require confirmed redundancy and an abort criterion on minimum cell voltage.

**UNKNOWN rule.** If no discharge test exists within the interval, record a US4 UNKNOWN against CG-05; runtime claims are limited to calculation (DESIGN depth).

**Ontology classes.** CapacityAssertion, TestRecord, InfrastructureSystem · **Related controls.** MCF-POW-010, MCF-POW-006, MCF-STO-017, MCF-CMP-010

**Informative references.** IEC 62040-3 (UPS performance); IEEE 485 / IEEE 1184 (battery sizing); IEEE 450 / IEEE 1188

### MCF-POW-012

**Bypass Exposure** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that time spent with critical load on static or maintenance bypass, eco-mode or other unconditioned paths is known, minimised, authorised and accounted for in risk, because the load is then exposed directly to utility or generator disturbances.

**Requirement.** The facility operator shall log every transfer of critical load to static bypass, maintenance bypass or eco-mode with start, end, cause and authorisation, shall alarm and escalate any unplanned bypass within the declared time, shall require approval for planned bypass and verify return to normal, and shall report cumulative bypass exposure per system at the declared interval.

**Assessment criteria**

1. All bypass transfers in the period are logged with cause and authorisation, reconciled to UPS event logs.
2. Unplanned bypass alarms were escalated within the declared time.
3. Planned bypass had approval and a recorded return-to-normal verification.
4. Cumulative bypass exposure per system is reported and within the declared limit.
5. Eco-mode operation, if used, is evaluated against AI load dynamics and grid quality (MCF-POW-002).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Cumulative bypass exposure limit per UPS system | hours per year | 24 (illustrative) | Capability profile |
| Unplanned bypass escalation time | minutes | 15 (illustrative) | Capability profile |

**Minimum evidence**

- UPS event logs
- Bypass log
- Approvals
- Exposure reports
- Eco-mode evaluation

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | Twelve months. |
| independence | Reconciliation to UPS controller logs by the assessor. |
| mandatoryItems | UPS event logs; Bypass log |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-05, CG-09. |
| reassessmentTriggers | Unplanned bypass event; Eco-mode enablement; UPS firmware change |

**Assessment methods.** RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Extract UPS event logs and reconcile to bypass log.
2. Check approvals and return-to-normal verification.
3. Compute cumulative exposure and compare with limit.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to all UPS systems with static or maintenance bypass.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Bypass left active after maintenance; Unnoticed static bypass during generator operation; Eco-mode transfer fails during fast AI load swing

**Testing safety.** Log review only; no bypass operation by or for the assessor.

**UNKNOWN rule.** If UPS event logs are unavailable for a system, record a U1 UNKNOWN; cumulative exposure for that system is UNKNOWN.

**Ontology classes.** OperatingState, Event, FailureMode · **Related controls.** MCF-POW-009, MCF-POW-023, MCF-OPS-019

**Informative references.** IEC 62040-3 (UPS performance); EN 50600-2-2 (power supply and distribution)

## POW-04 Distribution and protection

### MCF-POW-013

**Switchgear Integrity** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure MV and LV switchgear, transformers and switchboards are maintained in a safe and serviceable condition and that arc-flash hazards are quantified, labelled, minimised and controlled for all persons working on or near them.

**Requirement.** The electrical duty holder shall maintain a current arc-flash risk assessment (incident energy analysis) for all switchgear, switchboards, busway and PDUs, shall label equipment with incident energy or PPE category and boundaries, shall apply incident-energy reduction measures where assessed energy exceeds the declared threshold (for example maintenance switches, arc-flash relays, arc-resistant switchgear), and shall perform condition maintenance including infrared thermography, MV partial-discharge monitoring and breaker testing at the declared intervals.

**Assessment criteria**

1. An arc-flash study exists for all equipment, reviewed within the declared interval and after changes to fault level or protection settings.
2. Equipment labels in a sample match the study.
3. Where incident energy exceeds the threshold, a reduction measure is installed and tested.
4. MV switchgear is arc-classified (IAC per IEC 62271-200) or has documented compensating controls.
5. Infrared thermography and MV partial-discharge results within the interval show no unresolved critical anomalies.
6. Breaker maintenance and trip testing are current per manufacturer and standard intervals.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Arc-flash study review interval | years | 5 | NFPA 70E review requirement |
| Incident energy threshold requiring reduction measure | cal/cm² | 8 (illustrative) | Capability profile; NFPA 70E / IEEE 1584 methodology |
| Infrared thermography interval | months | 12 (illustrative) | NFPA 70B / capability profile |

**Minimum evidence**

- Arc-flash study (IEEE 1584 method or equivalent)
- Label sample photographs
- Incident-energy reduction test records
- Switchgear IAC classification
- Thermography and partial-discharge reports
- Breaker test records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E3; E4; E5 |
| optionalClasses | E2 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Current study; twelve months of condition maintenance. |
| independence | Arc-flash study by a competent electrical engineer independent of operations; thermography by a certified thermographer. |
| mandatoryItems | Arc-flash study; Label sample; Thermography reports |
| acceptableAlternatives | Online thermal monitoring with trending in place of periodic thermography where coverage is complete |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-04 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Utility fault-level change; Protection setting change; Switchgear modification; Arc incident |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, SAMPLING, ANALYSIS

**Assessment procedure**

1. Review study date, method, and inputs against current fault levels and settings.
2. Sample labels against the study.
3. Check high-energy locations for reduction measures and their tests.
4. Review thermography and partial-discharge findings and closure.
5. Review breaker maintenance records.

**Gate mappings.** CG-04 Life safety and hazardous energy (CRITICAL); CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies to all electrical distribution equipment in the boundary operated or maintained by the assessed party; colocation tenants assess equipment within their suite.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Arc-flash injury due to outdated labels; Hot joint undetected leading to switchboard failure; MV cable termination partial discharge leading to flashover

**Testing safety.** Thermography is performed by authorised persons; where covers must be removed, energised-work justification and permit are required per NFPA 70E or national rules, or IR windows are used. Assessors do not open equipment.

**UNKNOWN rule.** If no arc-flash study exists or it predates a fault-level change, record a US4 UNKNOWN against CG-04; energised work on affected equipment is not authorised until resolved.

**Ontology classes.** Hazard, AssetInstance, Safeguard · **Related controls.** MCF-POW-014, MCF-POW-023, MCF-POW-022

**Informative references.** NFPA 70E (electrical safety in the workplace); IEEE 1584 (arc-flash hazard calculations); IEC 62271-200 (AC metal-enclosed switchgear); IEC 61439 (LV switchgear assemblies); NFPA 70B (electrical equipment maintenance)

### MCF-POW-014

**Selective Coordination** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that protective devices are selective so that a fault is cleared by the device nearest to it, limiting loss of supply to the smallest fault domain, across utility, generator and UPS (inverter-limited) fault-current sources.

**Requirement.** The electrical engineer of record shall maintain a short-circuit and protection coordination study covering every source configuration (utility, generator, UPS inverter, bypass) and the declared maintenance states, and shall demonstrate selectivity from the rack PDU branch up to the main incomers within the declared fault-current range. The facility operator shall ensure as-found protection settings match the study by periodic setting extraction and secondary injection testing.

**Assessment criteria**

1. Short-circuit study covers all source configurations including inverter-limited fault current.
2. Coordination curves show selectivity between each upstream and downstream device pair for the declared range, or approved exceptions are listed.
3. Rack PDU and busway tap-off protection is selective with upstream devices for faults at the rack.
4. Extracted relay and trip-unit settings match the study for the sampled devices.
5. Secondary injection tests at the declared interval confirm trip characteristics.
6. Changes to settings since the last study are controlled under change management.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Protection setting extraction and comparison interval | months | 24 (illustrative) | Capability profile |
| Permitted deviation of as-found settings from study | count | 0 (illustrative) | Capability profile |

**Minimum evidence**

- Short-circuit and coordination study
- Coordination curves
- Relay/trip unit setting exports
- Secondary injection test reports
- Change records for settings

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E4; E7 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Current study; most recent setting extraction and tests. |
| independence | Study by a protection engineer; setting comparison reperformed by the assessor. |
| mandatoryItems | Coordination study; Setting exports; Secondary injection reports |
| acceptableAlternatives | Independent protection audit with setting verification |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-09 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Source change (new generator, UPS); Fault level change; Setting change; Nuisance or non-selective trip event |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS, REPERFORMANCE

**Assessment procedure**

1. Review study scope for all source configurations.
2. Check coordination curves for each critical device pair.
3. Compare extracted settings with study.
4. Review secondary injection results.
5. Review non-selective trip events in the period.

**Gate mappings.** CG-09 Failure containment (CRITICAL); CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies to all critical distribution. Partial applicability for colocation tenants: from the tenant's distribution boards downstream, with provider evidence upstream.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Rack fault trips upstream switchboard (AIDCF-004 protection miscoordination); Inverter-limited fault current fails to trip branch device; Setting drift after maintenance

**Testing safety.** Hazardous-energy activity. Tests and switching are performed only by authorised persons under the site electrical safety rules, an approved method statement and permit to work, with written authorisation from the facility owner's authorised engineer; assessors witness from outside the arc-flash boundary and never operate equipment. Secondary injection requires isolation of trip outputs or an outage of the protected circuit.

**UNKNOWN rule.** If settings cannot be extracted or the study omits generator or UPS source configurations, record a US4 UNKNOWN against CG-09 for electrical fault containment.

**Ontology classes.** FaultDomain, Safeguard, InfrastructureSystem · **Related controls.** MCF-POW-013, MCF-POW-015, MCF-RES-007, MCF-OPS-017

**Informative references.** IEC 60909 (short-circuit currents); IEC 60364 (LV electrical installations); IEEE 242 / IEEE 3004 series (protection and coordination); IEC 60947-2 (circuit-breakers)

### MCF-POW-015

**Busway and PDU Capacity** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure overhead busway, tap-off units, remote power panels and rack PDUs are rated for the continuous and peak load of dense AI racks, are balanced across phases, and keep capacity in failover states where one feed carries the full rack load.

**Requirement.** The facility operator shall maintain a capacity register for every busway run, tap-off and rack PDU showing rating, continuous load limit, measured peak per phase and failover load (the load each feed must carry if its partner fails). The facility operator shall prevent provisioning that would cause failover load to exceed the continuous limit and shall correct phase imbalance above the declared threshold.

**Assessment criteria**

1. The register covers every busway, tap-off and rack PDU serving AI racks.
2. Measured per-phase peak and calculated failover load are within the continuous load limit for every device.
3. Phase imbalance is below the declared threshold or a correction is scheduled.
4. Provisioning workflows check the register before new load is connected.
5. Busway joints are torque-checked or thermally surveyed at the declared interval.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Continuous load limit | % of device rating | 80 (illustrative; for devices not rated for 100% continuous duty) | NFPA 70 / IEC 60364 continuous-load sizing conventions; device rating |
| Maximum phase imbalance at PDU/busway | % | 10 (illustrative) | Capability profile |

**Minimum evidence**

- Capacity register
- EPMS per-phase peak data
- Failover load calculations
- Provisioning workflow evidence
- Busway joint inspection records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | Twelve months of per-phase peaks including peak AI utilisation. |
| independence | Failover loads recomputed by the assessor from EPMS data. |
| mandatoryItems | Capacity register; Per-phase peak data |
| acceptableAlternatives | DCIM power capacity module if it is the controlled source and uses measured data |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-05, CG-14. |
| reassessmentTriggers | New rack deployment; Rack power-limit increase; Busway extension |

**Assessment methods.** ANALYSIS, RECONCILIATION, SAMPLING

**Assessment procedure**

1. Extract per-phase peaks and pair A/B feeds.
2. Compute failover load and compare with continuous limit.
3. Check phase imbalance.
4. Sample provisioning records for register checks.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all critical distribution to AI racks.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Failover overloads surviving PDU and trips rack; Phase imbalance overheats neutral; Loose busway joint fails under sustained high load

**Testing safety.** Data review only; joint inspections by authorised persons under permit.

**UNKNOWN rule.** If per-phase data is unavailable for a device class, record a U1 UNKNOWN and limit the claim to devices with data.

**Ontology classes.** CapacityAssertion, AssetInstance, Interface · **Related controls.** MCF-POW-014, MCF-POW-021, MCF-CMP-003, MCF-OPS-021

**Informative references.** IEC 61439-6 (busbar trunking systems); IEC 60364 (LV installations); EN 50600-2-2

### MCF-POW-016

**Earthing and Bonding** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that earthing, equipotential bonding and lightning protection protect people against electric shock, provide fault-current return for protective devices and limit noise and transient damage to IT equipment, including metallic liquid-cooling pipework.

**Requirement.** The electrical engineer of record shall design the earthing system (system earthing type, earth electrodes, main earthing terminal, supplementary bonding) and the facility operator shall verify it by initial and periodic inspection and testing, including earth electrode resistance, protective conductor continuity, earth fault loop impedance and bonding of liquid-cooling pipework, manifolds, raised floors and cable containment.

**Assessment criteria**

1. Earthing design documents the system earthing type and bonding scheme for each building.
2. Periodic inspection and test records within the interval show earth electrode resistance, continuity and fault loop impedance within design values.
3. Liquid-cooling pipework, manifolds and CDUs are bonded, verified in a sample.
4. Bonding between generator, transformer and building earthing is verified.
5. Defects are corrected before the circuit is returned to service or within the declared period.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Periodic inspection and test interval | years | 5 (illustrative) | IEC 60364-6 / national wiring regulations; capability profile |

**Minimum evidence**

- Earthing design
- Periodic inspection and test reports
- Bonding sample records
- Defect records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E3; E4; E5 |
| optionalClasses | E2 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Most recent periodic inspection within interval. |
| independence | Inspection and test by a qualified electrical inspector. |
| mandatoryItems | Periodic inspection and test report |
| acceptableAlternatives |  |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-04 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Electrical installation change; Liquid-cooling installation; Lightning strike |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, SAMPLING

**Assessment procedure**

1. Review design and periodic test reports.
2. Inspect bonding of a sample of liquid-cooling and containment elements.
3. Check defect closure.

**Gate mappings.** CG-04 Life safety and hazardous energy (CRITICAL); CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies to all electrical installations in the boundary.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Touch voltage on unbonded coolant manifold; High earth fault loop impedance prevents disconnection; Lightning surge damages IT through poor bonding

**Testing safety.** Hazardous-energy activity. Tests and switching are performed only by authorised persons under the site electrical safety rules, an approved method statement and permit to work, with written authorisation from the facility owner's authorised engineer; assessors witness from outside the arc-flash boundary and never operate equipment. Earth electrode testing near energised substations follows the network operator's rules.

**UNKNOWN rule.** If no periodic inspection report is current, record a US4 UNKNOWN against CG-04 for shock protection.

**Ontology classes.** Safeguard, Hazard, InfrastructureSystem · **Related controls.** MCF-POW-013, MCF-PHY-011, MCF-THM-011

**Informative references.** IEC 60364 series (LV electrical installations); IEC 62305 series (lightning protection); IEEE 1100 (powering and grounding electronic equipment); EN 50310 (bonding in buildings with IT equipment)

## POW-05 Power quality and transient response

### MCF-POW-017

**Voltage Quality** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure voltage delivered to critical IT and cooling loads stays within equipment tolerance in all source configurations, including on generator and during load swings from AI clusters.

**Requirement.** The facility operator shall monitor voltage magnitude, unbalance and short-duration variations at UPS outputs, critical switchboards and a representative sample of rack PDUs, shall compare results with the tolerance of connected equipment (power supply unit specifications and the ITIC/CBEMA or SEMI F47 curves where adopted), and shall investigate excursions.

**Assessment criteria**

1. Voltage monitoring exists at UPS outputs, critical switchboards and sampled rack PDUs.
2. Excursions outside the declared envelope are logged and investigated.
3. Voltage on generator operation was recorded during a test and within envelope.
4. Unbalance at critical boards is within the declared limit.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Steady-state voltage envelope at critical boards | % of nominal | ±5 (illustrative) | Equipment PSU specifications; capability profile |
| Voltage unbalance limit | % | 2 (illustrative) | EN 50160 / IEC 61000-2 compatibility levels |

**Minimum evidence**

- Monitoring point list
- Voltage statistics and excursion log
- Generator-test voltage records
- Investigation records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E7 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY; DEGRADED |
| periodCoverage | Twelve months including generator tests. |
| independence | Data exported under observation. |
| mandatoryItems | Voltage statistics; Excursion log |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-05. |
| reassessmentTriggers | New load type; UPS mode change; Repeated PSU failures |

**Assessment methods.** ANALYSIS, INSPECTION

**Assessment procedure**

1. Confirm monitoring points.
2. Analyse statistics and excursions.
3. Review generator-test voltage records.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies to all critical distribution.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, EMERGENCY, DEGRADED

**Failure modes addressed.** Undervoltage on generator during AI ramp; Unbalance causing PSU derating

**Testing safety.** Data review via EPMS.

**UNKNOWN rule.** If no monitoring exists at rack level, record a U5 UNKNOWN for rack-level voltage quality.

**Ontology classes.** Resource, Event · **Related controls.** MCF-POW-002, MCF-POW-019, MCF-POW-021

**Informative references.** IEC 61000-2 series (compatibility levels); EN 50160; ITIC (CBEMA) curve application note; SEMI F47 (voltage sag immunity)

### MCF-POW-018

**Harmonics** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure harmonic distortion from rectifier-based IT loads, UPS, VFDs and BESS inverters is within limits at the point of common coupling and internally, does not overheat transformers, neutrals or generators, and does not cause resonance with filters or power-factor correction.

**Requirement.** The electrical engineer shall perform a harmonic study for the declared load mix covering utility and generator source configurations, and the facility operator shall measure voltage and current harmonics at the PCC and at critical boards. The facility owner shall keep harmonic emissions at the PCC within the limits of the connection agreement (for example IEEE 519 or the applicable IEC 61000-3 limits) and shall derate or specify transformers and generators for measured harmonic content.

**Assessment criteria**

1. A harmonic study covers utility and generator configurations and capacitive or filter elements.
2. Measured voltage THD and current TDD at the PCC are within the applicable limits.
3. Transformer and generator ratings account for measured harmonic content (K-factor or derating).
4. Leading power factor from IT PSUs and filters at light load is evaluated against generator capability.
5. Neutral currents in 4-wire systems are measured and within conductor rating.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Voltage THD limit at PCC, 1 kV < V ≤ 69 kV | % | 5 | IEEE 519 voltage distortion limits |
| Voltage THD limit at PCC, V ≤ 1 kV | % | 8 | IEEE 519 voltage distortion limits |

**Minimum evidence**

- Harmonic study
- PCC harmonic measurements
- Transformer and generator derating evidence
- Neutral current measurements
- Generator capability chart vs leading PF

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E7 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; EMERGENCY |
| periodCoverage | Twelve months of PQ data and at least one generator-supplied measurement. |
| independence | Study by an electrical engineer; data exported under observation. |
| mandatoryItems | Harmonic study; PCC measurements |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-05. |
| reassessmentTriggers | New rectifier or inverter loads; Filter or PFC change; Generator change |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Review study scope and assumptions vs current load.
2. Compare PCC measurements with limits.
3. Check derating and leading-PF evaluation.
4. Review neutral currents.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies to all sites; leading-PF element applies to generator-backed sites.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE · **Operating states.** NORMAL, EMERGENCY

**Failure modes addressed.** Generator AVR instability from leading PF at light load; Filter resonance amplifies harmonics; Transformer overheating

**Testing safety.** Measurements via installed meters; portable instruments installed only by authorised persons under permit.

**UNKNOWN rule.** If generator-supplied harmonic and PF behaviour is unmeasured, record a U5 UNKNOWN and refer to MCF-POW-020.

**Ontology classes.** Resource, Hazard, InfrastructureSystem · **Related controls.** MCF-POW-002, MCF-POW-020, MCF-POW-005

**Informative references.** IEEE 519 (harmonic control); IEC 61000-3 series (emission limits); IEC 61000-4-7 (harmonic measurement); ISO 8528 series

### MCF-POW-019

**Transient Ride-Through** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Demonstrate that critical IT, cooling and control loads ride through grid voltage dips, transfers between sources and switching transients without loss of service, and that the facility meets any fault ride-through obligations of its grid connection.

**Requirement.** The electrical engineer shall define the ride-through envelope for each load class (IT, CDU and pump drives, chillers, controls), including source transfers (UPS to bypass, static transfer switch, ATS, generator synchronisation) and grid dips. The facility owner shall verify by commissioning and periodic transfer tests that loads remain online for transfers within the envelope, shall ensure mechanical loads not on UPS restart automatically within the thermal time constant, and shall document compliance with connection-agreement ride-through requirements.

**Assessment criteria**

1. A ride-through envelope is documented for each load class, including STS and ATS transfer times.
2. Transfer tests demonstrate IT and UPS-backed cooling loads remained online.
3. Non-UPS cooling drives and chillers restart automatically within the thermal ride-through time established by THM controls, demonstrated in test.
4. Control systems (BMS, EPMS, CDU controllers) are UPS-backed and remain operational through transfers.
5. Grid-code ride-through obligations for the site as a large load are identified and evidence of compliance exists.
6. Real dip events in the period caused no unexpected load loss, or loss was investigated.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Static transfer switch transfer time | ms | 4 (illustrative; within PSU hold-up) | STS OEM data; PSU hold-up specification |
| Maximum restart time for non-UPS cooling plant | s | per thermal ride-through analysis (THM) | Thermal design basis |

**Minimum evidence**

- Ride-through envelope
- Transfer test reports with waveform captures
- Restart test records
- Control system power supply schematic
- Grid-code compliance evidence
- Dip event analysis

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; TRANSITION; EMERGENCY; RECOVERY |
| periodCoverage | Commissioning and most recent periodic transfer tests; twelve months of dip events. |
| independence | Transfer tests witnessed by an independent commissioning or electrical engineer. |
| mandatoryItems | Transfer test reports; Restart test records |
| acceptableAlternatives | Integrated systems test results covering the same transfers |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-05 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | UPS, STS or ATS change; Cooling drive change; New load class (e.g. accelerator generation); Unexpected load loss on a dip |

**Assessment methods.** DOCUMENT_REVIEW, TEST, ANALYSIS

**Assessment procedure**

1. Review envelope for completeness by load class.
2. Review transfer test waveforms and load continuity.
3. Review restart tests for non-UPS cooling against thermal ride-through time.
4. Check control system power supply.
5. Analyse real dip events.

**Gate mappings.** CG-05 Resilient electrical supply (CRITICAL); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to all critical loads; grid-code element applies where the connection agreement contains ride-through obligations.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, TRANSITION, EMERGENCY, RECOVERY

**Failure modes addressed.** Chillers trip on dip and fail to restart (AIDCF-004 X02); STS transfer exceeds PSU hold-up; CDU controller reboots during transfer; Site trips off grid during fault, breaching obligations

**Testing safety.** Hazardous-energy activity. Tests and switching are performed only by authorised persons under the site electrical safety rules, an approved method statement and permit to work, with written authorisation from the facility owner's authorised engineer; assessors witness from outside the arc-flash boundary and never operate equipment. Transfer tests on live critical load require confirmed healthy redundancy, an approved test window, thermal contingency, and abort criteria.

**UNKNOWN rule.** If transfer tests have never been performed with representative load, record a US4 UNKNOWN against CG-05; THM restart dependency is referred to CG-06.

**Ontology classes.** Safeguard, TestRecord, OperatingState, FailureScenario · **Related controls.** MCF-POW-017, MCF-POW-020, MCF-THM-024, MCF-THM-021

**Informative references.** IEC 62040-3 (UPS performance, output dynamic performance classification); SEMI F47 (voltage sag immunity); EU Network Code on Demand Connection; NFPA 110

### MCF-POW-020

**Load-Step Response** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Demonstrate that UPS, BESS, generators and the grid connection remain stable under the load steps and synchronous power oscillations produced by large accelerator clusters (collective compute/communication phases, job start and stop, checkpoint pauses and failure-driven drops), and that these dynamics are bounded within the capability of every source.

**Requirement.** The facility owner shall characterise the power dynamics of each AI cluster (step magnitude, ramp rate, oscillation amplitude and frequency band), using measured data at sub-second resolution or the accelerator vendor's specified behaviour, and shall verify that UPS rectifier and inverter controls, BESS, generator governors and voltage regulators, and the grid connection tolerate them without instability, protective trips or breach of connection limits. Where they do not, the facility owner shall apply mitigation (accelerator power-smoothing or ramp-limit features, workload scheduling, energy-storage buffering) and shall verify it by test, including a load-step test on generator supply.

**Assessment criteria**

1. Cluster power dynamics are characterised with step size, ramp rate and oscillation band, from measured data at sub-second resolution or vendor specification.
2. Generator load-acceptance capability (ISO 8528-5 performance class or test data) covers the characterised steps with frequency and voltage deviation within declared limits.
3. UPS and BESS behaviour under characterised oscillation is verified (no rectifier walk-in conflict, battery cycling within design, no transfer to bypass).
4. Grid-connection ramp and oscillation obligations are identified and measured behaviour at the PCC is within them.
5. A load-step or oscillation test on generator supply, using load banks programmed to the characterised profile or the cluster itself, shows stable operation.
6. Mitigations in use (power smoothing, ramp limits) are configured, under change control and monitored.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum cluster power swing amplitude | % of cluster IT load | 50 (illustrative) | Measured cluster data or accelerator vendor specification |
| Power oscillation frequency band of concern | Hz | 0.1 to 20 (illustrative) | Cluster characterisation; generator and grid modal analysis |
| Maximum single load step on generator supply | % of generator rating | per ISO 8528-5 class and test data (illustrative: 50) | ISO 8528-5 load acceptance performance classes |
| Measurement resolution for AI load dynamics | ms | 100 or finer (illustrative) | Capability profile |

**Minimum evidence**

- Cluster power-dynamics characterisation report
- High-resolution power measurements at cluster and PCC
- Generator load-acceptance data or test
- UPS/BESS dynamic test records
- Grid-connection obligation analysis
- Mitigation configuration exports

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; EMERGENCY; TRANSITION |
| periodCoverage | Characterisation for each cluster generation; test on generator within the declared interval. |
| independence | Characterisation reviewed by a power-systems engineer independent of the cluster operator. |
| mandatoryItems | Power-dynamics characterisation; Generator load-step or oscillation test record |
| acceptableAlternatives | Validated dynamic simulation calibrated against measured data, where testing on generator with real cluster load is not authorised; supports DESIGN depth only |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-05 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | New accelerator generation or cluster expansion; Change of power-smoothing configuration; Generator governor or AVR change; Unexplained UPS or generator alarms during training |

**Assessment methods.** ANALYSIS, TEST, DOCUMENT_REVIEW, RECONCILIATION

**Assessment procedure**

1. Obtain characterisation and verify data resolution and coverage of job phases.
2. Compare characterised dynamics with generator, UPS and BESS capability.
3. Review grid-connection obligations against PCC measurements.
4. Review or witness the load-step or oscillation test on generator.
5. Verify mitigation configuration and change control.

**Gate mappings.** CG-05 Resilient electrical supply (CRITICAL); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to sites hosting synchronous training or large inference clusters whose aggregate power can change by more than a declared fraction of site load within seconds. Not applicable to sites where AI load is a small fraction of source capacity, recorded with the calculation.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, EMERGENCY, TRANSITION

**Failure modes addressed.** Generator governor hunting under periodic training load; UPS transfers to bypass under swing; Forced oscillation at PCC breaches grid obligations; Synchronous job drop causes overfrequency on generator

**Testing safety.** Hazardous-energy activity. Tests and switching are performed only by authorised persons under the site electrical safety rules, an approved method statement and permit to work, with written authorisation from the facility owner's authorised engineer; assessors witness from outside the arc-flash boundary and never operate equipment. Tests on generator with real cluster load require approval from the capability owner, a checkpointed workload, and abort criteria on frequency and voltage; programmable load-bank tests are preferred.

**UNKNOWN rule.** If cluster dynamics are uncharacterised for a site where the applicability threshold is met, record a US4 UNKNOWN against CG-05; generator and UPS adequacy claims are limited to static load.

**Ontology classes.** Resource, CapacityAssertion, TestRecord, FailureScenario · **Related controls.** MCF-POW-005, MCF-POW-009, MCF-POW-001, MCF-CAP-014, MCF-CMP-017

**Informative references.** ISO 8528-5 (generating set load acceptance); IEC 62040-3 (UPS dynamic performance); Network operator large-load connection requirements of the jurisdiction; IEEE 2800 (inverter-based resource interconnection; for grid-forming BESS behaviour)

## POW-06 Electrical monitoring, maintenance and recovery

### MCF-POW-021

**EPMS Coverage** · DETECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure the electrical power monitoring system observes every critical node with accurate, time-synchronised data and alarms, functions independently of the systems it monitors, and is configured and protected as a critical control system.

**Requirement.** The facility operator shall instrument every utility incomer, generator, UPS, STS, critical switchboard, busway and representative rack PDU with metering connected to the EPMS, shall synchronise device clocks to the declared accuracy for sequence-of-events analysis, shall configure alarms per an approved alarm philosophy, and shall power the EPMS and its network from protected supplies. The facility operator shall maintain the EPMS configuration under change control and its access under SEC controls.

**Assessment criteria**

1. A point list reconciles EPMS devices to the as-built single-line diagram with no unmonitored critical node.
2. Clock synchronisation accuracy meets the declared value, demonstrated by sequence-of-events data.
3. Alarm configuration matches the alarm philosophy and critical alarms reach a staffed location.
4. EPMS servers, network and gateways are on UPS-backed supplies and remain available through transfers.
5. EPMS configuration and firmware are baselined and changes are controlled.
6. Data gaps in the period are below the declared threshold and are investigated.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Critical-node metering coverage | % of critical nodes | 100 (illustrative) | Capability profile |
| Clock synchronisation accuracy for sequence of events | ms | 1 (illustrative) | Capability profile; IEC 61850 time-sync practice |
| Maximum EPMS data gap per point | % of period | 1 (illustrative) | Capability profile |

**Minimum evidence**

- EPMS point list
- As-built single-line diagram reconciliation
- Sequence-of-events records
- Alarm philosophy and configuration export
- EPMS power and network schematic
- Configuration baseline and change records
- Data completeness report

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E7 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; TRANSITION; EMERGENCY |
| periodCoverage | Current configuration; twelve months of data completeness. |
| independence | Point-list reconciliation reperformed by the assessor. |
| mandatoryItems | Point list; Configuration baseline; Alarm configuration |
| acceptableAlternatives |  |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-07 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | EPMS upgrade; Distribution change; Data gap above threshold; Security incident on OT network |

**Assessment methods.** RECONCILIATION, INSPECTION, ANALYSIS, TEST

**Assessment procedure**

1. Reconcile EPMS point list to the single-line diagram.
2. Review sequence-of-events timing from a recent event.
3. Compare alarm configuration with philosophy and test a critical alarm path.
4. Review EPMS power and network resilience.
5. Review configuration baseline and change records.

**Gate mappings.** CG-07 Critical control-system integrity (CRITICAL); CG-05 Resilient electrical supply (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to all sites with critical electrical infrastructure; colocation tenants assess provider EPMS data access and coverage of their feeds.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION

**Failure modes addressed.** Unmonitored switchboard hides overload; Clock drift prevents fault reconstruction; EPMS lost during transfer when needed most; Unauthorised EPMS configuration change

**Testing safety.** Alarm path tests use simulation or test points authorised by the facility operator; no protective device is operated.

**UNKNOWN rule.** If the point list cannot be reconciled to the single-line diagram, record a US4 UNKNOWN against CG-07; EPMS-derived evidence for other POW controls is downgraded to T2 until resolved.

**Ontology classes.** InfrastructureSystem, Safeguard, EvidenceObject, Interface · **Related controls.** MCF-SEC-005, MCF-OPS-013, MCF-POW-015, MCF-POW-024

**Informative references.** IEC 61850 (communication for power utility automation); IEC 62443 series (industrial automation and control system security); EN 50600-2-6 (management and operational information); ISA-18.2 / IEC 62682 (alarm management)

### MCF-POW-022

**Preventive Maintenance** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure electrical assets are maintained at intervals and to scopes that keep their reliability and safety within the assumptions of the design and resilience analysis, without maintenance itself introducing unmanaged risk.

**Requirement.** The facility operator shall maintain a maintenance programme for each electrical asset class (switchgear, transformers, UPS, batteries, generators, ATS/STS, busway, PDUs, protection relays) with scopes and intervals based on manufacturer requirements and recognised maintenance practice, shall complete maintenance on time, and shall record deferrals with risk assessment and approval.

**Assessment criteria**

1. Every critical electrical asset is in the maintenance system with scope and interval.
2. On-time completion in the period meets the declared percentage.
3. No critical maintenance is overdue beyond the declared tolerance without an approved deferral.
4. Deferrals have risk assessment and approval by the accountable engineer.
5. Findings from maintenance are tracked to closure.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| On-time completion of critical electrical maintenance | % | 95 (illustrative) | Capability profile |
| Maximum overdue period without approved deferral | days | 30 (illustrative) | Capability profile |

**Minimum evidence**

- Maintenance programme
- Work order history
- Deferral approvals
- Findings tracking

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E7 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Twelve months. |
| independence | Completion statistics recomputed by the assessor from work-order data. |
| mandatoryItems | Work order history; Asset-to-programme reconciliation |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-05. |
| reassessmentTriggers | Maintenance contractor change; Asset additions; Failure attributed to maintenance |

**Assessment methods.** RECONCILIATION, ANALYSIS, SAMPLING

**Assessment procedure**

1. Reconcile asset register to maintenance programme.
2. Compute on-time completion.
3. Review overdue items and deferrals.
4. Sample findings to closure.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies to all electrical assets operated or maintained by the assessed party.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Breaker fails to trip after missed maintenance; Deferred battery replacement; Maintenance-induced failure without method statement

**Testing safety.** Records review; observation of maintenance only from outside the work area.

**UNKNOWN rule.** If the maintenance system does not cover all critical assets, record a U5 UNKNOWN for uncovered assets.

**Ontology classes.** AssetInstance, Safeguard, Action · **Related controls.** MCF-OPS-009, MCF-OPS-012, MCF-POW-013, MCF-POW-010

**Informative references.** NFPA 70B (electrical equipment maintenance); EN 50600-2-2; IEC 60300 (dependability management)

### MCF-POW-023

**Switching Procedures** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that every planned and emergency switching operation on critical distribution is performed to an approved, verified procedure by authorised persons, with hazardous energy controlled, so that switching neither injures people nor drops critical load.

**Requirement.** The electrical duty holder shall require a method of procedure (MOP) for every planned switching operation on critical distribution, prepared from the current single-line diagram, checked by a second authorised person, and executed with step verification. The electrical duty holder shall maintain emergency operating procedures for foreseeable failures, shall apply lockout/tagout and permit-to-work for isolation, and shall authorise persons for switching by competence assessment.

**Assessment criteria**

1. Every sampled planned switching operation has an approved MOP checked by a second authorised person.
2. MOP steps reference current single-line diagram revision and include hold points and rollback.
3. Emergency operating procedures exist for each failure in the UPS failure analysis (MCF-POW-009).
4. Isolations in the sample applied lockout/tagout with permit-to-work and test-before-touch.
5. Persons performing switching hold current authorisation for the voltage level and equipment.
6. Switching incidents in the period were investigated.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Planned critical switching with approved, peer-checked MOP | % | 100 (illustrative) | Capability profile |

**Minimum evidence**

- MOP sample
- Emergency operating procedures
- Permits and LOTO records
- Authorisation register
- Switching incident records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E3; E5 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | MAINTENANCE; EMERGENCY; TRANSITION |
| periodCoverage | Twelve months of switching operations. |
| independence | Authorisation scheme audited by an independent authorising engineer. |
| mandatoryItems | MOP sample; Permit/LOTO records; Authorisation register |
| acceptableAlternatives |  |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-04 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Distribution change; Switching incident; Change of maintenance contractor |

**Assessment methods.** SAMPLING, DOCUMENT_REVIEW, OBSERVATION

**Assessment procedure**

1. Sample planned switching operations.
2. Check MOP preparation, peer check and SLD revision.
3. Review EOP coverage against failure analysis.
4. Check permits, LOTO and authorisations.
5. Observe a switching operation where scheduled, from a safe position.

**Gate mappings.** CG-04 Life safety and hazardous energy (CRITICAL); CG-07 Critical control-system integrity (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all switching on critical distribution by the assessed party or its contractors.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** MAINTENANCE, EMERGENCY, TRANSITION, RECOVERY

**Failure modes addressed.** Wrong breaker opened drops live path; Backfeed from generator during isolation; Unauthorised person switches MV; MOP based on outdated drawing (AIDCF-004 X04)

**Testing safety.** Hazardous-energy activity. Tests and switching are performed only by authorised persons under the site electrical safety rules, an approved method statement and permit to work, with written authorisation from the facility owner's authorised engineer; assessors witness from outside the arc-flash boundary and never operate equipment.

**UNKNOWN rule.** If LOTO and permit records for sampled isolations cannot be produced, record a US4 UNKNOWN against CG-04.

**Ontology classes.** Safeguard, Hazard, AssessmentProcedure, Action · **Related controls.** MCF-OPS-008, MCF-OPS-007, MCF-OPS-006, MCF-POW-012

**Informative references.** NFPA 70E (electrical safety in the workplace); EN 50110 (operation of electrical installations); ISO 45001 (occupational health and safety)

### MCF-POW-024

**Black-Start and Restoration** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Demonstrate that after a total loss of power the site can be restored from a dead state, in a safe and dependency-correct sequence (controls, cooling, then IT), within the declared recovery time, and that AI workloads can resume.

**Requirement.** The facility owner shall maintain a black-start and restoration plan that defines the restoration sequence, the dependencies of each step (control power, EPMS/BMS availability, cooling restart, battery recharge limits, inrush and staged load pick-up on generator), the authority to proceed, and the hand-over to IT for workload restart. The facility owner shall exercise the plan at the declared interval, either by a full integrated test or by staged tests that together cover every step, and shall measure time to each milestone.

**Assessment criteria**

1. A restoration sequence exists covering control power, EPMS/BMS, cooling, battery recharge and IT pick-up with dependencies.
2. Generator staged load pick-up respects load-acceptance limits including cooling motor inrush and IT power-on surge.
3. Restoration was exercised within the interval and measured milestones met declared times.
4. Manual operation is possible if EPMS/BMS is unavailable, with procedures and trained staff.
5. Hand-over criteria to IT and workload restart dependencies (storage, network, scheduler) are defined.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Restoration time from dead site to full critical load | hours | 4 (illustrative) | Capability profile; recovery outcome |
| Black-start exercise interval | months | 12 (illustrative) | Capability profile |

**Minimum evidence**

- Restoration plan
- Exercise or IST reports with milestone times
- Manual operation procedures
- Training records
- Hand-over criteria

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E6 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | FAILED; RECOVERY; SHUTDOWN |
| periodCoverage | Most recent exercise within interval. |
| independence | Exercise witnessed by a party independent of the operations team. |
| mandatoryItems | Restoration plan; Exercise report with milestone times |
| acceptableAlternatives | Record of a real total-loss event and restoration with milestone times |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-10 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Change in distribution or control architecture; Generator change; Real total-loss event; Major cooling plant change |

**Assessment methods.** DOCUMENT_REVIEW, SCENARIO_EXERCISE, TEST, ANALYSIS

**Assessment procedure**

1. Review sequence for dependency correctness.
2. Check staged pick-up against generator load acceptance.
3. Review exercise milestone times against declared values.
4. Verify manual operation procedures and training.
5. Check hand-over criteria with CMP/STO/NET restart dependencies.

**Gate mappings.** CG-10 Recovery readiness (CRITICAL); CG-05 Resilient electrical supply (SUPPORTING); CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies to all sites hosting critical AI capability. Colocation tenants assess the provider's plan and their own IT restart dependencies.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** FAILED, RECOVERY, SHUTDOWN

**Failure modes addressed.** Restoration blocked because BMS needs power it controls; Generator trips on simultaneous chiller restart; IT restarted before cooling stable; Battery recharge overloads generators

**Testing safety.** Black-start exercises are among the most hazardous tests: they require an approved test plan, written authorisation by the facility owner and capability owner, workloads drained or checkpointed, emergency services informed where required, and abort criteria. Staged tests are preferred where a full dead-site test is not authorised.

**UNKNOWN rule.** If restoration has never been exercised, record a US4 UNKNOWN against CG-10; the plan supports design only, not recoverability.

**Ontology classes.** FailureScenario, Safeguard, TestRecord, Dependency · **Related controls.** MCF-RES-014, MCF-THM-024, MCF-STO-018, MCF-POW-021

**Informative references.** ISO 22301 (business continuity); NFPA 110; EN 50600-2-2
