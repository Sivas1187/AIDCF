# AIDCF-007A Control Catalogue — ENV Environmental and Resource Performance

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-ENV](../../../aidcf-018-domain-guides/AIDCF-018-ENV_Environmental_and_Resource_Performance_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-ENV-001](#mcf-env-001) | Temperature Control | DETECTIVE | OPERATION | AL4 | — | CG-06, CG-08 |
| [MCF-ENV-002](#mcf-env-002) | Humidity Control | PREVENTIVE | OPERATION | AL4 | — | CG-06 |
| [MCF-ENV-003](#mcf-env-003) | Particulate and Corrosion | PREVENTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-ENV-004](#mcf-env-004) | Vibration and Acoustic Conditions | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-08 |
| [MCF-ENV-005](#mcf-env-005) | PUE Measurement | DETECTIVE | OPERATION | AL4 | — | — |
| [MCF-ENV-006](#mcf-env-006) | Energy Allocation | DIRECTIVE | IMPLEMENTATION | AL3 | — | — |
| [MCF-ENV-007](#mcf-env-007) | Efficiency Under Load | DETECTIVE | OPERATION | AL4 | — | — |
| [MCF-ENV-008](#mcf-env-008) | Resilience-Efficiency Trade-Off | DIRECTIVE | DESIGN | AL2 | — | CG-05, CG-06, CG-14 |
| [MCF-ENV-009](#mcf-env-009) | Water Source and Quality | PREVENTIVE | OPERATION | AL4 | — | CG-06, CG-04 |
| [MCF-ENV-010](#mcf-env-010) | WUE Measurement | DETECTIVE | OPERATION | AL4 | — | — |
| [MCF-ENV-011](#mcf-env-011) | Water Scarcity Response | RECOVERY | RESILIENCE | AL5 | — | CG-06, CG-03 |
| [MCF-ENV-012](#mcf-env-012) | Discharge Control | PREVENTIVE | OPERATION | AL4 | — | — |
| [MCF-ENV-013](#mcf-env-013) | Carbon Accounting Boundary | DIRECTIVE | DESIGN | AL2 | — | — |
| [MCF-ENV-014](#mcf-env-014) | Energy Attribute Evidence | DETECTIVE | IMPLEMENTATION | AL3 | — | — |
| [MCF-ENV-015](#mcf-env-015) | Embodied Resource Data | DIRECTIVE | DESIGN | AL2 | — | — |
| [MCF-ENV-016](#mcf-env-016) | Reporting Traceability | DETECTIVE | OPERATION | AL4 | — | — |
| [MCF-ENV-017](#mcf-env-017) | Battery Materials | PREVENTIVE | OPERATION | AL4 | — | CG-04 |
| [MCF-ENV-018](#mcf-env-018) | Refrigerants and Coolants | PREVENTIVE | OPERATION | AL4 | CG-04 | — |
| [MCF-ENV-019](#mcf-env-019) | Fuel and Suppressant Handling | PREVENTIVE | OPERATION | AL4 | — | CG-04 |
| [MCF-ENV-020](#mcf-env-020) | Hardware and Media Waste | DIRECTIVE | OPERATION | AL4 | — | — |
| [MCF-ENV-021](#mcf-env-021) | Heatwave Readiness | RECOVERY | RESILIENCE | AL5 | — | CG-06, CG-05 |
| [MCF-ENV-022](#mcf-env-022) | Drought Readiness | DIRECTIVE | DESIGN | AL2 | — | CG-03 |
| [MCF-ENV-023](#mcf-env-023) | Flood Adaptation | PREVENTIVE | DESIGN | AL2 | — | CG-09 |
| [MCF-ENV-024](#mcf-env-024) | Long-Term Resource Constraints | DIRECTIVE | DESIGN | AL2 | — | CG-01, CG-03 |

## ENV-01 Environmental operating conditions

### MCF-ENV-001

**Temperature Control** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Demonstrate that air inlet temperatures at IT equipment and liquid coolant supply temperatures to cold plates or immersion tanks stay within the declared envelope and rate-of-change limits in all declared operating states, measured where the equipment experiences them.

**Requirement.** The facility operator shall declare, for each hall and liquid loop, the environmental class (ASHRAE air-cooling class and liquid-cooling W class, or OEM envelope where more restrictive) and shall measure inlet air temperature at representative rack inlets and coolant supply temperature at the technology cooling system interface. The facility operator shall alarm excursions and rates of change outside the envelope, investigate them, and report excursion time per hall at the declared interval.

**Assessment criteria**

1. Each hall and loop has a declared envelope traceable to ASHRAE classes or OEM specification.
2. Inlet sensors are at rack inlets (not return air) at the declared density, and coolant supply sensors are at the TCS interface.
3. Excursion time outside the recommended envelope per hall is reported and within the declared limit.
4. Rate-of-change alarms exist and events are investigated.
5. Sensor calibration is current for the sampled sensors.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Recommended IT inlet air temperature envelope | °C | 18 to 27 | ASHRAE TC 9.9 thermal guidelines recommended envelope |
| Liquid-cooling facility/TCS supply class | ASHRAE W class | W32 or W45 (illustrative) | ASHRAE TC 9.9 liquid cooling classes; OEM requirement |
| Rack inlet sensor density | sensors per rack | 3 (top, middle, bottom; illustrative) | Capability profile; ASHRAE measurement practice |
| Permitted excursion time outside recommended envelope | hours per year | per OEM allowable (illustrative: 50) | Capability profile |

**Minimum evidence**

- Declared envelope per hall/loop
- Sensor location map
- Twelve months of inlet and supply temperature telemetry
- Excursion reports and investigations
- Calibration records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E7 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | Twelve months including the hottest season. |
| independence | Telemetry extracted under observation; excursion statistics recomputed by the assessor. |
| mandatoryItems | Envelope declaration; Telemetry export; Calibration records |
| acceptableAlternatives | Third-party monitoring service data where it is the sensor source |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-06, CG-08. |
| reassessmentTriggers | New hall or loop; Containment change; Setpoint change; Excursion event |

**Assessment methods.** ANALYSIS, INSPECTION, RECONCILIATION

**Assessment procedure**

1. Verify envelope declaration and source.
2. Inspect sensor positions in a sample of racks and loops.
3. Recompute excursion statistics from telemetry.
4. Review investigations and calibration.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all IT spaces and liquid loops in the boundary.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Return-air sensing masks hot inlets; Coolant supply drift causes accelerator throttling; Rapid temperature change after cooling restart

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If inlet sensing is only at return air, record a U8 method UNKNOWN; the OPERATION claim is UNKNOWN for that hall.

**Ontology classes.** OperatingState, Resource, EvidenceObject · **Related controls.** MCF-ENV-002, MCF-THM-008, MCF-THM-022, MCF-CAP-018

**Informative references.** ASHRAE TC 9.9 Thermal Guidelines for Data Processing Environments; EN 50600-2-3 (environmental control); ISO/IEC 22237 series

### MCF-ENV-002

**Humidity Control** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure moisture conditions avoid condensation on liquid-cooled components and pipework, electrostatic discharge risk at low humidity, and corrosion acceleration at high humidity.

**Requirement.** The facility operator shall control and monitor dew point and relative humidity in IT spaces within the declared envelope and shall maintain coolant supply temperatures above room dew point by the declared margin wherever uninsulated liquid-cooling components are exposed to room air. The facility operator shall alarm when the margin is lost and shall define the response.

**Assessment criteria**

1. Dew point and RH are monitored in each hall against the declared envelope.
2. Coolant supply temperature minus room dew point is monitored continuously for liquid-cooled halls and is at or above the declared margin for the period.
3. Margin-loss alarms exist with a defined response (raise supply temperature, dehumidify, isolate).
4. Humidification systems, if any, are maintained and water quality is controlled.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Recommended dew point envelope | °C dew point | -9 to 15, and ≤ 60% RH | ASHRAE TC 9.9 thermal guidelines recommended envelope |
| Minimum margin of coolant supply temperature above room dew point | K | 2 (illustrative) | Capability profile; CDU OEM guidance |

**Minimum evidence**

- Humidity telemetry
- Dew point margin trend for liquid-cooled halls
- Alarm configuration
- Response procedure
- Humidifier maintenance records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | Twelve months including the most humid season. |
| independence | Telemetry extracted under observation. |
| mandatoryItems | Humidity telemetry; Dew point margin trend |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-06. |
| reassessmentTriggers | Coolant supply temperature change; Envelope change; Condensation event |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW

**Assessment procedure**

1. Analyse dew point and RH telemetry.
2. Compute coolant-to-dew-point margin.
3. Review alarm and response.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to all IT spaces; margin element applies to liquid-cooled halls.

**Lifecycle stages.** DESIGN, OPERATE · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Condensation on cold plates or manifolds; ESD damage at very low humidity; Humidifier contamination

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If dew point margin is not monitored for a liquid-cooled hall, record a U1 UNKNOWN and refer to THM fluid controls.

**Ontology classes.** OperatingState, Hazard · **Related controls.** MCF-ENV-001, MCF-THM-011

**Informative references.** ASHRAE TC 9.9 Thermal Guidelines; EN 50600-2-3 (environmental control)

### MCF-ENV-003

**Particulate and Corrosion** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure airborne particulate and gaseous contaminants are controlled so that hardware reliability is not degraded, particularly where economisation or high airflow increases outdoor air exposure.

**Requirement.** The facility operator shall measure gaseous corrosivity by copper and silver reactivity coupons or real-time monitors and particulate cleanliness at the declared interval, shall maintain filtration to the declared grade, and shall act when the severity level exceeds the declared class, including restricting economiser operation during external pollution events.

**Assessment criteria**

1. Corrosivity measurements at the declared interval meet the declared severity level.
2. Particulate cleanliness meets the declared ISO 14644-1 class in sampled halls.
3. Filtration grade and replacement intervals are maintained.
4. Economiser operation has a contamination-triggered lockout or procedure.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Gaseous corrosion severity level | ANSI/ISA-71.04 class | G1 | ASHRAE TC 9.9 gaseous and particulate contamination guidance |
| Particulate cleanliness | ISO 14644-1 class | 8 | ASHRAE TC 9.9 contamination guidance |
| Corrosion coupon interval | months | 3 (illustrative) | Capability profile |

**Minimum evidence**

- Coupon or monitor reports
- Particulate survey
- Filter maintenance records
- Economiser control logic or procedure

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E3; E4 |
| optionalClasses | E1 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Twelve months of coupons. |
| independence | Coupons analysed by an independent laboratory. |
| mandatoryItems | Coupon or monitor reports |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-08. |
| reassessmentTriggers | Economiser introduction; Nearby pollution source; Hardware failure trend with corrosion cause |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, ANALYSIS

**Assessment procedure**

1. Review coupon and particulate results against classes.
2. Inspect filter condition.
3. Review economiser lockout.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to air-cooled spaces and to air-side portions of liquid-cooled halls; most material for economiser-equipped sites.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Sulphur corrosion of PCB traces; Zinc whiskers from raised floor; Wildfire smoke ingress

**Testing safety.** Coupon placement and retrieval by the operator; assessors do not enter during filter changes.

**UNKNOWN rule.** If no corrosivity measurement exists for an economiser site, record a U1 UNKNOWN.

**Ontology classes.** Hazard, Resource · **Related controls.** MCF-ENV-001, MCF-PHY-002, MCF-CMP-019

**Informative references.** ANSI/ISA-71.04 (environmental conditions: airborne contaminants); ISO 14644-1 (cleanroom classification); ASHRAE TC 9.9 contamination guidance

### MCF-ENV-004

**Vibration and Acoustic Conditions** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure vibration and sound levels do not degrade storage and IT equipment (including acoustic damage to hard disk drives during gaseous suppression discharge), do not exceed occupational noise limits in dense halls, and comply with boundary noise limits in permits.

**Requirement.** The facility owner shall specify suppression discharge nozzles and agent release rates that keep sound pressure at storage equipment below the storage OEM threshold, shall measure occupational noise exposure in halls and plant rooms against regulatory action values and provide hearing protection and signage where exceeded, and shall demonstrate that site boundary noise from generators, heat rejection and transformers complies with planning or permit limits.

**Assessment criteria**

1. Suppression nozzle and discharge design addresses acoustic impact on storage, with OEM threshold.
2. Occupational noise surveys exist for dense halls and plant rooms, with controls where action values are exceeded.
3. Boundary noise assessment or monitoring shows compliance with permit limits, including during generator testing.
4. Vibration-sensitive equipment locations are separated or isolated from vibration sources.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Occupational noise lower / upper exposure action values | dB(A) daily exposure | 80 / 85 | EU Directive 2003/10/EC (noise at work) or national equivalent |
| Sound pressure limit at storage arrays during discharge | dB | per storage OEM threshold | Storage OEM guidance; suppression designer |
| Site boundary noise limit | dB(A) | per planning or environmental permit | Permit conditions |

**Minimum evidence**

- Suppression acoustic design note
- Occupational noise survey
- Boundary noise assessment or monitoring
- Permit noise conditions

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E3 |
| optionalClasses | E4; E5 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY; MAINTENANCE |
| periodCoverage | Current surveys; boundary data covering generator testing. |
| independence | Noise surveys by a competent acoustic consultant. |
| mandatoryItems | Suppression acoustic design note (if gaseous suppression); Occupational noise survey |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-08. |
| reassessmentTriggers | New suppression system; New dense hall; Generator or heat-rejection additions; Noise complaint |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, ANALYSIS

**Assessment procedure**

1. Review suppression acoustic design.
2. Review occupational noise surveys and controls.
3. Review boundary noise evidence against permit.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Acoustic suppression elements apply where gaseous suppression protects HDD-based storage; occupational and boundary elements apply to all sites.

**Lifecycle stages.** DESIGN, BUILD, OPERATE · **Operating states.** NORMAL, EMERGENCY, MAINTENANCE

**Failure modes addressed.** Inert-gas discharge causes HDD read/write failures; Hearing damage in dense halls; Permit breach from generator test noise

**Testing safety.** Noise measurements in plant rooms require hearing protection; no suppression discharge is initiated for testing.

**UNKNOWN rule.** If the acoustic effect of discharge on storage is unassessed, record a U1 UNKNOWN and refer to STO integrity controls.

**Ontology classes.** Hazard, Safeguard · **Related controls.** MCF-PHY-022, MCF-PHY-007, MCF-STO-009

**Informative references.** EU Directive 2003/10/EC (noise at work); ISO 9613-2 (outdoor sound propagation); ISO 7779 (IT equipment noise measurement)

## ENV-02 Energy performance

### MCF-ENV-005

**PUE Measurement** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure power usage effectiveness is measured according to ISO/IEC 30134-2 with a declared measurement category, boundary and period, so that reported values are comparable, traceable and not distorted by metering gaps or boundary choices.

**Requirement.** The energy manager shall calculate PUE as annual total facility energy divided by annual IT equipment energy per ISO/IEC 30134-2, shall declare the measurement category and the metering points used for IT energy, shall include all energy sources (grid, on-site generation, fuel for generators), and shall report the value with category, period and data completeness.

**Assessment criteria**

1. PUE uses annual energy (not instantaneous power) over a 12-month period.
2. The ISO/IEC 30134-2 measurement category is declared and IT energy meters match it.
3. All facility energy inputs, including generator fuel energy, are included.
4. Meter accuracy classes and calibration are documented for the meters used.
5. Data completeness is reported and gaps are filled by a documented method.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| PUE measurement period | months | 12 | ISO/IEC 30134-2 |
| PUE measurement category | category | Category 2 or higher (illustrative) | ISO/IEC 30134-2; capability profile |
| Revenue/sub-meter accuracy class | class | 0.5S or better (illustrative) | IEC 62053 series |

**Minimum evidence**

- PUE calculation workbook
- Meter list with category mapping
- Meter calibration records
- Energy data with completeness report

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E2; E3; E7 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Twelve consecutive months. |
| independence | Calculation reperformed by the assessor from meter data. |
| mandatoryItems | Calculation workbook; Meter mapping |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | Meter change; Boundary change; New on-site generation |

**Assessment methods.** REPERFORMANCE, RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Reconcile meters to category definition.
2. Reperform PUE from raw meter data.
3. Check inclusion of all energy inputs.
4. Review data gaps and fill method.

**Gate mappings.** None

**Applicability.** Applies to sites reporting PUE internally or externally; colocation tenants report the provider's value with its basis.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** PUE computed from instantaneous snapshot; Generator fuel energy omitted; IT energy measured at wrong point

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If metering does not support the declared category, record a U8 method UNKNOWN and report PUE only with a limitation.

**Ontology classes.** EvidenceObject, Resource · **Related controls.** MCF-ENV-006, MCF-ENV-016, MCF-POW-021

**Informative references.** ISO/IEC 30134-2 (power usage effectiveness); EN 50600-4-2 (PUE); IEC 62053 series (electricity metering)

### MCF-ENV-006

**Energy Allocation** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure energy consumed by shared infrastructure is allocated to tenants, clusters or services by a documented and metered method, so that per-capability energy and emissions are defensible.

**Requirement.** The energy manager shall define an allocation method for shared facility energy (cooling, losses, lighting, offices) to tenants or AI clusters, shall base allocation on sub-metered data wherever metering exists, and shall report unallocated energy below the declared threshold.

**Assessment criteria**

1. An allocation method is documented and approved.
2. Allocation uses sub-meters for IT load and the best available meters for shared systems.
3. Unallocated energy is below the declared threshold.
4. Allocated totals reconcile to the site total.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum unallocated energy | % of site total | 2 (illustrative) | Capability profile |

**Minimum evidence**

- Allocation method
- Sub-meter data
- Reconciliation to site total

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E7 |
| optionalClasses | E3 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Twelve months. |
| independence | Reconciliation reperformed by the assessor. |
| mandatoryItems | Allocation method; Reconciliation |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | New tenant or cluster; Meter change |

**Assessment methods.** RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Review method.
2. Reconcile allocations to site total.
3. Check unallocated energy.

**Gate mappings.** None

**Applicability.** Applies to multi-tenant or multi-cluster sites where per-capability energy is reported.

**Lifecycle stages.** DESIGN, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Allocation does not reconcile; Shared cooling energy allocated by floor area only

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If allocation does not reconcile, record a U4 conflicting-evidence UNKNOWN on per-capability energy claims.

**Ontology classes.** Resource, EvidenceObject · **Related controls.** MCF-ENV-005, MCF-ENV-013

**Informative references.** ISO/IEC 30134-2; ISO 50001 (energy management systems); GHG Protocol Scope 2 Guidance

### MCF-ENV-007

**Efficiency Under Load** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure facility efficiency is characterised across the load range actually experienced by AI deployments (partial occupancy during ramp-up, variable training load) and that heat reuse, where claimed, is measured.

**Requirement.** The energy manager shall report PUE or partial PUE at the declared IT load points, shall document the efficiency curves of major equipment (UPS, chillers, CDUs) at those points, and, where heat is exported for reuse, shall measure exported heat energy and report the energy reuse factor per ISO/IEC 30134-6.

**Assessment criteria**

1. Efficiency is reported at each declared IT load point.
2. Equipment efficiency curves at those points are documented.
3. Where heat reuse is claimed, exported heat is metered with heat meters and ERF calculated.
4. Improvement actions target the load points where the site operates most hours.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| IT load points for efficiency characterisation | % of design IT load | 25 / 50 / 75 / 100 (illustrative) | Capability profile |
| Energy reuse factor reporting | ratio | measured annually | ISO/IEC 30134-6 |

**Minimum evidence**

- Load-point efficiency report
- Equipment efficiency curves
- Heat meter data and ERF calculation

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Twelve months. |
| independence | Heat meter data from the off-taker where available. |
| mandatoryItems | Load-point efficiency report |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | Large occupancy change; Heat reuse contract change |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW

**Assessment procedure**

1. Review load-point reports.
2. Check heat metering and ERF.
3. Review improvement actions.

**Gate mappings.** None

**Applicability.** Applies to sites reporting efficiency; ERF element applies only where heat reuse is claimed.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Efficiency reported only at design load; Heat reuse claimed without metering

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If heat reuse is claimed without heat metering, record a U1 UNKNOWN on the ERF claim.

**Ontology classes.** Resource, EvidenceObject · **Related controls.** MCF-ENV-005, MCF-ENV-008

**Informative references.** ISO/IEC 30134-6 (energy reuse factor); ISO/IEC 30134-2 (PUE); EN 50600-4-6

### MCF-ENV-008

**Resilience-Efficiency Trade-Off** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure that efficiency measures (UPS eco-mode, raised supply temperatures, reduced running redundant units, economiser hours, power capping) are evaluated for their effect on power and thermal resilience before adoption, so that efficiency gains do not silently consume resilience.

**Requirement.** The facility owner shall require a resilience impact assessment for every efficiency measure affecting power or cooling, reviewed by the electrical and mechanical engineers responsible for CG-05 and CG-06 evidence, stating the effect on transfer behaviour, ride-through, thermal ride-through time and redundancy in each declared operating state. The facility owner shall approve the measure under change control only when the assessment shows declared tolerances are still met.

**Assessment criteria**

1. A register of efficiency measures in use exists with linked resilience impact assessments.
2. Each assessment addresses transfer, ride-through, thermal margin and redundancy by operating state.
3. Assessments were reviewed by the responsible electrical and mechanical engineers.
4. Measures were approved under change control.

**Minimum evidence**

- Efficiency measure register
- Resilience impact assessments
- Change approvals

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E7 |
| optionalClasses | E4 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY |
| periodCoverage | All measures active at assessment date. |
| independence | Assessment reviewed by an engineer not sponsoring the efficiency measure. |
| mandatoryItems | Efficiency measure register; Resilience impact assessments |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-05, CG-06, CG-14. |
| reassessmentTriggers | New efficiency measure; Change in redundancy configuration; Incident linked to an efficiency measure |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INQUIRY

**Assessment procedure**

1. Identify efficiency measures from configuration (UPS mode, setpoints, staging).
2. Check each has an assessment and approval.
3. Evaluate assessment quality against operating states.

**Gate mappings.** CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all sites operating any efficiency measure affecting power or cooling.

**Lifecycle stages.** DESIGN, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY

**Failure modes addressed.** Eco-mode exposes load to transfer during grid event; Raised supply temperature reduces thermal ride-through below restart time; Redundant chiller switched off for efficiency

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If an efficiency measure is found in configuration without an assessment, record a U1 UNKNOWN and carry it into CG-05/CG-06 gate-level evaluation.

**Ontology classes.** Safeguard, OperatingState, FailureScenario · **Related controls.** MCF-POW-012, MCF-POW-019, MCF-OPS-018, MCF-THM-003

**Informative references.** ISO/IEC 30134 series (KPIs); EN 50600-2-2 and EN 50600-2-3; EU Code of Conduct on Data Centre Energy Efficiency (best practice guidelines)

## ENV-03 Water performance

### MCF-ENV-009

**Water Source and Quality** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure water supplies for heat rejection, adiabatic cooling and humidification are identified, of controlled quality, and treated to prevent scaling, corrosion, biofouling and Legionella risk.

**Requirement.** The facility operator shall document each water source (mains, borehole, reclaimed), its contracted or permitted volume and quality, and shall operate a water treatment programme with the declared monitoring frequency for chemistry and microbiology, including a Legionella risk assessment and control scheme for evaporative systems, reviewed by a competent person.

**Assessment criteria**

1. Each water source is documented with volume entitlement and quality.
2. Treatment programme monitoring results are within control limits for the period.
3. A current Legionella risk assessment exists for evaporative and adiabatic systems.
4. Out-of-limit results were acted on within the declared time.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Legionella risk assessment review interval | months | 24 (illustrative) | National Legionella guidance (e.g. HSE L8, ASHRAE 188); capability profile |

**Minimum evidence**

- Water source register
- Treatment monitoring records
- Legionella risk assessment
- Corrective action records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Twelve months. |
| independence | Microbiological samples analysed by an accredited laboratory. |
| mandatoryItems | Treatment monitoring records; Legionella risk assessment (if evaporative) |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-06, CG-04. |
| reassessmentTriggers | Source change; Out-of-limit microbiology; System modification |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Review source register.
2. Analyse treatment records.
3. Review Legionella assessment and actions.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to sites using water for heat rejection or humidification. Closed-loop dry-cooled sites apply the source register element for make-up water only.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Legionella outbreak from cooling tower; Scaling reduces heat-rejection capacity; Borehole quality change

**Testing safety.** Sampling from evaporative systems requires respiratory protection per the Legionella control scheme; assessors do not sample.

**UNKNOWN rule.** If no Legionella risk assessment exists for an evaporative system, record a U1 UNKNOWN and a Finding referred to CG-04 gate-level evaluation.

**Ontology classes.** Resource, Hazard, Dependency · **Related controls.** MCF-ENV-010, MCF-THM-018, MCF-THM-015

**Informative references.** ASHRAE 188 (Legionellosis risk management); HSE L8 (Legionnaires' disease control, UK); ISO 14046 (water footprint)

### MCF-ENV-010

**WUE Measurement** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure water usage effectiveness is measured per ISO/IEC 30134-9 with complete metering of site water inputs, so that water claims are comparable and traceable.

**Requirement.** The energy and sustainability manager shall calculate WUE as annual site water use divided by annual IT equipment energy per ISO/IEC 30134-9, shall meter every water input, shall state which uses are included (heat rejection, humidification, domestic) and shall report data completeness. Where source-side water (water used in electricity generation) is reported, the basis shall be stated separately.

**Assessment criteria**

1. All water inputs are metered and reconcile to utility bills.
2. WUE uses annual values and the ISO/IEC 30134-9 definition.
3. Inclusions and exclusions are stated.
4. Source-side water, if reported, is separate with stated basis.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| WUE measurement period | months | 12 | ISO/IEC 30134-9 |

**Minimum evidence**

- Water meter list
- Meter data and bills
- WUE calculation

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Twelve consecutive months. |
| independence | Calculation reperformed by the assessor. |
| mandatoryItems | WUE calculation; Meter reconciliation to bills |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | Meter change; Cooling technology change |

**Assessment methods.** REPERFORMANCE, RECONCILIATION

**Assessment procedure**

1. Reconcile meters to bills.
2. Reperform WUE.
3. Check stated inclusions.

**Gate mappings.** None

**Applicability.** Applies to sites reporting water performance.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Unmetered borehole abstraction; WUE uses design not measured data

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If an input is unmetered, record a U5 coverage UNKNOWN and report WUE with a limitation.

**Ontology classes.** Resource, EvidenceObject · **Related controls.** MCF-ENV-009, MCF-ENV-016

**Informative references.** ISO/IEC 30134-9 (water usage effectiveness); EN 50600-4-9

### MCF-ENV-011

**Water Scarcity Response** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Demonstrate that the site maintains heat-rejection capacity for the declared outcomes when water supply is restricted or interrupted, using storage, alternative sources or dry operation with a known capacity penalty.

**Requirement.** The facility owner shall maintain a water scarcity response plan stating on-site storage autonomy at design-day consumption, alternative sources, the capacity of heat rejection in water-free or reduced-water mode at design ambient, and the load-reduction actions if that capacity is below the declared IT load. The facility operator shall exercise switchover to reduced-water mode at the declared interval.

**Assessment criteria**

1. On-site water storage autonomy at design-day consumption is calculated and meets the declared value.
2. Heat-rejection capacity in reduced-water mode at design ambient is stated.
3. If that capacity is below IT load, load-reduction actions with MW values are defined.
4. Switchover to reduced-water mode was exercised within the interval.
5. Utility restriction notification arrangements are in place.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| On-site water storage autonomy at design-day consumption | hours | 48 (illustrative) | Capability profile |
| Heat-rejection capacity in reduced-water mode at design ambient | % of design IT load | per thermal design (illustrative: 80) | Thermal design basis |

**Minimum evidence**

- Water scarcity response plan
- Storage autonomy calculation
- Reduced-water capacity analysis
- Exercise records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E3; E4 |
| optionalClasses | E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | DEGRADED; EMERGENCY |
| periodCoverage | Exercise within interval. |
| independence | Exercise observed by the assessor or independent party. |
| mandatoryItems | Response plan; Exercise records |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-06, CG-03. |
| reassessmentTriggers | Drought declaration; Source change; Cooling plant change |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, SCENARIO_EXERCISE

**Assessment procedure**

1. Review plan.
2. Recompute storage autonomy.
3. Review capacity analysis.
4. Review exercise.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to sites whose heat rejection depends on water. Not applicable to fully dry-cooled sites, recorded with evidence.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** DEGRADED, EMERGENCY

**Failure modes addressed.** Water restriction during heatwave (AIDCF-004 X10); Storage depleted before supply restored; Dry-mode capacity unknown

**Testing safety.** Switchover exercises are performed by the operator under method statement with thermal contingency.

**UNKNOWN rule.** If reduced-water capacity is unknown, record a U1 UNKNOWN referred to CG-06.

**Ontology classes.** FailureScenario, Resource, Safeguard · **Related controls.** MCF-ENV-022, MCF-ENV-021, MCF-THM-015, MCF-THM-004

**Informative references.** ISO 22301 (business continuity); ISO 14046 (water footprint)

### MCF-ENV-012

**Discharge Control** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure discharges of cooling-tower blowdown, treated water, glycol and stormwater comply with permits and that accidental releases of coolant, fuel or fire-water are contained.

**Requirement.** The facility operator shall hold and comply with discharge consents for trade effluent and surface water, shall monitor discharge quality at the declared frequency, shall provide interceptors and containment for fuel, glycol and potentially contaminated fire-fighting water, and shall report permit breaches to the regulator as required.

**Assessment criteria**

1. Current discharge consents exist for each discharge.
2. Monitoring results are within consent limits.
3. Interceptors and containment for fuel, glycol and fire-water are installed and maintained.
4. Permit breaches in the period were reported and corrected.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Discharge monitoring frequency | per consent | per permit conditions | Discharge consent |

**Minimum evidence**

- Discharge consents
- Monitoring records
- Interceptor maintenance records
- Breach reports

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY |
| periodCoverage | Twelve months. |
| independence | Laboratory results from an accredited laboratory. |
| mandatoryItems | Discharge consents; Monitoring records |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | New discharge; Permit variation; Spill event |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION

**Assessment procedure**

1. Review consents.
2. Compare monitoring with limits.
3. Inspect interceptors and containment.

**Gate mappings.** None

**Applicability.** Applies to all sites with trade effluent or surface water discharge.

**Lifecycle stages.** DESIGN, OPERATE · **Operating states.** NORMAL, EMERGENCY

**Failure modes addressed.** Glycol release to surface water; Fire-water run-off contamination; Biocide over-discharge

**Testing safety.** Interceptor inspection follows confined-space rules where applicable; assessors inspect from surface.

**UNKNOWN rule.** If consents cannot be produced, record a U1 UNKNOWN and a regulatory-compliance Finding.

**Ontology classes.** Hazard, Safeguard · **Related controls.** MCF-ENV-019, MCF-ENV-009

**Informative references.** ISO 14001 (environmental management systems); National environmental permitting regime

## ENV-04 Carbon and resource reporting

### MCF-ENV-013

**Carbon Accounting Boundary** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure the organisational and operational boundary for greenhouse gas accounting of AI capability is defined consistently with the GHG Protocol, including colocation, leased and on-site generation emissions, so that carbon usage effectiveness and footprint claims are well-founded.

**Requirement.** The sustainability manager shall define the consolidation approach (operational or financial control, or equity share), the Scope 1 (generator fuel, refrigerant leakage), Scope 2 (location-based and market-based) and relevant Scope 3 categories (purchased hardware, construction, upstream fuel) for each site, shall state exclusions with justification, and shall calculate CUE per ISO/IEC 30134-8 on the declared basis.

**Assessment criteria**

1. Consolidation approach and site boundaries are documented.
2. Scope 1 includes generator fuel and refrigerant leakage.
3. Scope 2 is reported on both location-based and market-based methods.
4. Relevant Scope 3 categories are identified with inclusion decisions.
5. CUE basis (emission factor method) is declared.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Materiality threshold for boundary exclusions | % of total emissions | 5 (illustrative) | Capability profile; GHG Protocol guidance on exclusions |

**Minimum evidence**

- GHG inventory methodology
- Boundary statement
- Emission factor sources
- CUE calculation

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Current reporting year. |
| independence | Methodology reviewed by an independent verifier where externally reported. |
| mandatoryItems | Inventory methodology; Boundary statement |
| acceptableAlternatives | Third-party verification statement covering methodology |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | Acquisition or new site; Methodology change; New regulatory reporting requirement |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Review boundary and consolidation approach.
2. Check scope coverage.
3. Review CUE basis.

**Gate mappings.** None

**Applicability.** Applies wherever carbon or CUE claims are made for the capability.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Refrigerant leakage excluded from Scope 1; Only market-based Scope 2 reported; Colocation emissions omitted

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If the boundary is undefined, record a U9 interpretation UNKNOWN on all carbon claims.

**Ontology classes.** EvidenceObject, Resource · **Related controls.** MCF-ENV-014, MCF-ENV-016, MCF-ENV-018

**Informative references.** GHG Protocol Corporate Standard and Scope 2 Guidance; ISO 14064-1 (GHG inventories); ISO/IEC 30134-8 (carbon usage effectiveness)

### MCF-ENV-014

**Energy Attribute Evidence** · DETECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure claims of renewable or carbon-free electricity are backed by retired energy attribute certificates or contractual instruments matched to consumption by the declared temporal and geographic rules, without double counting.

**Requirement.** The sustainability manager shall hold evidence of cancellation or retirement of energy attribute certificates (for example guarantees of origin or RECs) or of contractual instruments (PPAs) for every claimed MWh, shall match them to consumption by the declared temporal granularity (annual or hourly) and market boundary, and shall ensure no instrument is claimed by another party.

**Assessment criteria**

1. Retirement evidence exists for every claimed MWh in the period.
2. Matching follows the declared temporal and geographic rules.
3. PPA volumes are reconciled to delivered generation data.
4. Registry records show retirement on behalf of the claiming entity.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Temporal matching granularity | interval | annual or hourly (declared) | GHG Protocol Scope 2 Guidance; hourly matching frameworks |

**Minimum evidence**

- Registry retirement statements
- PPA contracts and generation data
- Matching analysis

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E7 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Reporting year. |
| independence | Registry records obtained from the registry, not only from the broker. |
| mandatoryItems | Registry retirement statements |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | New PPA; Change in matching claim; Registry change |

**Assessment methods.** RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Reconcile claimed MWh to retirements.
2. Check matching rules.
3. Reconcile PPA volumes.

**Gate mappings.** None

**Applicability.** Applies where renewable or carbon-free electricity claims are made.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Certificates not retired; Double-counted PPA output; Hourly claim based on annual matching

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If retirement cannot be verified in the registry, record a U6 source-unverified UNKNOWN on the claim.

**Ontology classes.** EvidenceObject · **Related controls.** MCF-ENV-013, MCF-ENV-016

**Informative references.** GHG Protocol Scope 2 Guidance; EN 16325 (guarantees of origin); ISO/IEC 30134-3 (renewable energy factor)

### MCF-ENV-015

**Embodied Resource Data** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure embodied carbon and material data for buildings, plant and AI hardware are collected on a consistent life-cycle basis so that lifecycle footprint and refresh decisions are informed.

**Requirement.** The sustainability manager shall collect embodied-impact data for buildings and major plant from environmental product declarations or LCA studies, and for AI hardware from OEM product carbon footprints, using a documented life-cycle method, and shall report coverage by mass or spend.

**Assessment criteria**

1. A documented LCA method is used (system boundary, life stages, data sources).
2. Coverage of building, plant and hardware by mass or spend meets the declared threshold.
3. Data sources (EPDs, OEM PCFs) are referenced and dated.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Embodied data coverage | % of hardware and plant by spend | 80 (illustrative) | Capability profile |

**Minimum evidence**

- LCA method
- EPD and PCF register
- Coverage calculation

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S2 |
| stateCoverage | NORMAL |
| periodCoverage | Current inventory. |
| independence | Method reviewed by a competent LCA practitioner. |
| mandatoryItems | LCA method; EPD/PCF register |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | Hardware refresh; New build; Method change |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Review method.
2. Check data sources.
3. Compute coverage.

**Gate mappings.** None

**Applicability.** Applies where lifecycle or embodied claims are made.

**Lifecycle stages.** PLAN, DESIGN, DECOMMISSION · **Operating states.** NORMAL

**Failure modes addressed.** Embodied claim based on generic factors only; Hardware omitted

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If coverage is below threshold, report the claim with a limitation and record a U5 UNKNOWN.

**Ontology classes.** EvidenceObject, AssetInstance · **Related controls.** MCF-ENV-013, MCF-ENV-020

**Informative references.** ISO 14040 / ISO 14044 (life cycle assessment); EN 15978 (sustainability of construction works); ISO 14067 (carbon footprint of products)

### MCF-ENV-016

**Reporting Traceability** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure every reported environmental metric (energy, PUE, WUE, CUE, REF, ERF, emissions) traces to source meter data and calculation, and that restatements are controlled and disclosed, including for regulatory data-centre reporting.

**Requirement.** The sustainability manager shall maintain a reporting register that links each reported metric to its calculation, source data and approver, shall retain data for the declared period, shall restate when errors exceed the declared threshold, and shall meet the content and timing of applicable regulatory reporting (for example EU Energy Efficiency Directive data-centre reporting where in scope).

**Assessment criteria**

1. Each reported metric traces to calculation and source data in the register.
2. A sample of metrics is reperformed from source data within tolerance.
3. Restatements above threshold were made and disclosed.
4. Applicable regulatory reports were submitted on time with required indicators.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Restatement threshold | % change in reported metric | 5 (illustrative) | Capability profile |

**Minimum evidence**

- Reporting register
- Calculation files
- Regulatory submissions
- Restatement records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3; E7 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Last two reporting cycles. |
| independence | Reperformance by the assessor. |
| mandatoryItems | Reporting register; Regulatory submissions (if in scope) |
| acceptableAlternatives | Limited or reasonable assurance report by an external verifier |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | New regulatory requirement; Error discovered; Metering change |

**Assessment methods.** REPERFORMANCE, DOCUMENT_REVIEW, SAMPLING

**Assessment procedure**

1. Sample metrics.
2. Trace to source and reperform.
3. Review restatements and submissions.

**Gate mappings.** None

**Applicability.** Applies to all externally or regulatorily reported environmental metrics.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Reported PUE not reproducible; Late regulatory submission; Undisclosed restatement

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If a reported metric cannot be traced to source data, record a U6 UNKNOWN on that metric.

**Ontology classes.** EvidenceObject, AssuranceReport · **Related controls.** MCF-ENV-005, MCF-ENV-010, MCF-ENV-014, MCF-EVA-005

**Informative references.** EU Energy Efficiency Directive (EU) 2023/1791 and Delegated Regulation (EU) 2024/1364 (data-centre reporting); ISO/IEC 30134 series; ISO 14064-3 (verification of GHG statements)

## ENV-05 Hazardous materials and waste

### MCF-ENV-017

**Battery Materials** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure batteries in storage, transport, quarantine and end of life (UPS strings, BESS modules, rack battery backup units, spares) are inventoried, stored at safe state of charge, segregated when damaged and returned or recycled under applicable battery regulation.

**Requirement.** The facility operator shall maintain an inventory of batteries held outside service, shall store lithium-ion spares at or below the declared state of charge in a designated, detected and separated location, shall quarantine damaged or swollen cells in a fire-rated container away from critical plant, and shall transfer end-of-life batteries only to authorised recyclers with documentation meeting applicable battery and waste regulation.

**Assessment criteria**

1. An inventory of batteries outside service exists and reconciles to a physical count sample.
2. Lithium-ion spares are stored at or below the declared state of charge in a designated location.
3. A quarantine procedure and fire-rated container exist for damaged cells, with use recorded.
4. End-of-life transfers have waste transfer and recycler authorisation documents.
5. Spare battery storage is not within a compartment containing critical power or IT plant.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum state of charge for stored lithium-ion spares | % SoC | 30 (illustrative) | OEM guidance; aligns with air-transport limit for UN 3480 lithium-ion batteries |

**Minimum evidence**

- Battery inventory
- Storage location inspection
- Quarantine procedure and records
- Waste transfer and recycler documents

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Twelve months. |
| independence | Physical count sample by the assessor. |
| mandatoryItems | Battery inventory; Quarantine procedure |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-04. |
| reassessmentTriggers | Battery replacement programme; Damaged-cell event; Regulation change |

**Assessment methods.** RECONCILIATION, INSPECTION, DOCUMENT_REVIEW

**Assessment procedure**

1. Reconcile inventory to count sample.
2. Inspect storage and quarantine.
3. Review end-of-life records.

**Gate mappings.** CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to all sites holding batteries outside service.

**Lifecycle stages.** OPERATE, DECOMMISSION · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Thermal runaway of fully charged spares in store; Damaged cell left in plant room; Unauthorised disposal

**Testing safety.** Inspection only; damaged cells are handled only by trained staff with battery-hazard PPE.

**UNKNOWN rule.** If spare battery state of charge is not controlled, record a Finding and a U1 UNKNOWN referred to CG-04 gate-level evaluation.

**Ontology classes.** Hazard, AssetInstance, Safeguard · **Related controls.** MCF-POW-010, MCF-PHY-021, MCF-ENV-020

**Informative references.** EU Battery Regulation (EU) 2023/1542; IEC 62619 (safety of industrial lithium batteries); UN Manual of Tests and Criteria (lithium battery transport); NFPA 855

### MCF-ENV-018

**Refrigerants and Coolants** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure refrigerants, glycols and dielectric coolants are inventoried, contained, leak-checked and handled so that toxicity, flammability (including A2L refrigerants), asphyxiation and environmental hazards are controlled for people and plant.

**Requirement.** The facility operator shall maintain an inventory of refrigerant charge per system (type, mass, CO2-equivalent, ISO 817/ASHRAE 34 safety class) and of coolants and dielectric fluids, shall leak-check refrigerant systems at the frequencies required by applicable regulation, shall provide refrigerant detection, alarms and ventilation in machinery rooms and occupied spaces where concentration could exceed the practical limit, shall use only certified technicians for refrigerant work, and shall hold safety data sheets and handling procedures for every coolant.

**Assessment criteria**

1. Refrigerant inventory per system includes type, charge, CO2e and safety class.
2. Leak checks occurred at the required frequency, and leaks were repaired and rechecked.
3. Machinery rooms and spaces where the practical limit could be exceeded have detection, alarm and ventilation tested within the interval.
4. A2L or higher-flammability refrigerant installations have the ignition-source and ventilation measures required by the applicable safety standard.
5. Refrigerant work is performed by certified technicians, evidenced in the sample.
6. Coolant and dielectric fluid SDS and handling procedures are available, and spill kits are present.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Refrigerant leak-check frequency | per system | tiered by CO2e charge per applicable regulation | EU F-gas Regulation (EU) 2024/573 or national equivalent |
| Refrigerant detector alarm setpoint | % of practical limit or ATEL/ODL | per EN 378 / ISO 5149 (illustrative: 50% of practical limit) | EN 378 / ISO 5149 refrigerating systems safety |

**Minimum evidence**

- Refrigerant and coolant inventory
- Leak-check records
- Detector and ventilation test records
- Technician certification records
- SDS and handling procedures

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E3; E4; E5 |
| optionalClasses | E2 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Twelve months. |
| independence | Detector tests by a certified contractor; inventory reconciled by the assessor. |
| mandatoryItems | Inventory; Leak-check records; Detector test records |
| acceptableAlternatives |  |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-04 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Refrigerant change (e.g. to A2L); Leak event; New machinery room; Immersion cooling introduction |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INSPECTION, TEST

**Assessment procedure**

1. Reconcile inventory to plant nameplates in a sample.
2. Review leak-check records against required frequency.
3. Review detector and ventilation tests; witness an alarm test where possible.
4. Check technician certification and SDS availability.

**Gate mappings.** CG-04 Life safety and hazardous energy (CRITICAL)

**Applicability.** Applies to all sites with refrigerating systems, glycol loops or dielectric immersion fluids.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE, DECOMMISSION · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Refrigerant release in machinery room causing asphyxiation; A2L ignition from unrated equipment; Undetected chronic leakage; Dielectric fluid spill and slip/fire hazard

**Testing safety.** Detector bump tests use certified calibration gas by the contractor; assessors do not enter machinery rooms during alarm without the operator's clearance.

**UNKNOWN rule.** If detection in a machinery room is untested or absent where required, record a US4 UNKNOWN against CG-04.

**Ontology classes.** Hazard, Safeguard, AssetInstance · **Related controls.** MCF-THM-017, MCF-THM-013, MCF-ENV-013, MCF-ENV-019

**Informative references.** EN 378 / ISO 5149 (refrigerating systems: safety and environmental requirements); ISO 817 / ASHRAE 34 (refrigerant designation and safety classification); EU F-gas Regulation (EU) 2024/573; ASHRAE 15 (safety standard for refrigeration systems)

### MCF-ENV-019

**Fuel and Suppressant Handling** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure generator fuel and fire suppressant agents are stored, contained, transferred and disposed of safely and in compliance with permits, and that suppressant inventory reflects its environmental profile.

**Requirement.** The facility operator shall store fuel in tanks with secondary containment of the declared capacity, leak detection and overfill protection, shall control deliveries with a supervised procedure, shall inspect tanks and pipework at the declared interval, and shall maintain an inventory of suppressant agents with their pressure-vessel inspection status and environmental classification, recovering agents through certified contractors.

**Assessment criteria**

1. Fuel tanks have secondary containment of at least the declared capacity, leak detection and overfill protection.
2. Deliveries follow a supervised procedure with spill kit and drain protection.
3. Tank and pipework inspections are current.
4. Suppressant inventory includes agent type, mass, cylinder inspection dates and environmental status.
5. Agent recovery and disposal records exist for removed systems.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Secondary containment capacity | % of largest tank volume | 110 (illustrative) | Common oil-storage regulation and bunding practice; local permit |

**Minimum evidence**

- Tank specifications and containment calculations
- Delivery procedure and records
- Inspection records
- Suppressant inventory
- Recovery records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Twelve months. |
| independence | Tank inspection by a competent third party where required by regulation. |
| mandatoryItems | Containment calculations; Inspection records; Suppressant inventory |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-04. |
| reassessmentTriggers | Tank modification; Spill; Suppression system change |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION

**Assessment procedure**

1. Review containment.
2. Review delivery records and inspect fill point.
3. Review suppressant inventory.

**Gate mappings.** CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to sites storing fuel or suppressant agents.

**Lifecycle stages.** DESIGN, OPERATE, DECOMMISSION · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Fuel spill to drain during delivery; Overfill; Overdue pressure-vessel inspection of agent cylinders

**Testing safety.** Inspection of fuel areas follows ignition-source controls; assessors do not enter bunds.

**UNKNOWN rule.** If containment capacity cannot be verified, record a U1 UNKNOWN and an environmental Finding.

**Ontology classes.** Hazard, Safeguard, Resource · **Related controls.** MCF-POW-007, MCF-ENV-012, MCF-PHY-022

**Informative references.** NFPA 30 (flammable and combustible liquids); National oil-storage and pressure-equipment regulation; ISO 14520 / NFPA 2001 (agent handling)

### MCF-ENV-020

**Hardware and Media Waste** · DIRECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure retired AI hardware, network equipment and media are routed to reuse, refurbishment or authorised recycling with traceable records, after data sanitisation, and in line with waste electrical equipment regulation.

**Requirement.** The facility operator shall route retired equipment through the decommissioning custody process (MCF-PHY-020), shall prefer reuse or refurbishment where data and security rules allow, shall transfer waste only to authorised operators with waste transfer documentation, and shall report mass by disposition route.

**Assessment criteria**

1. Retired equipment disposition is recorded per serial and route (reuse, refurbish, recycle).
2. Waste transfers have authorised-operator and transfer documentation.
3. Mass by route is reported for the period.
4. Data sanitisation certificates precede reuse or recycling transfer.

**Minimum evidence**

- Disposition records
- Waste transfer notes
- Mass report
- Sanitisation certificates

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Twelve months. |
| independence | Sample traced by the assessor. |
| mandatoryItems | Disposition records; Waste transfer notes |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | Large refresh; Change of recycler |

**Assessment methods.** SAMPLING, RECONCILIATION

**Assessment procedure**

1. Sample retired serials.
2. Trace to route, transfer notes and certificates.
3. Review mass report.

**Gate mappings.** None

**Applicability.** Applies to all equipment retired from the boundary.

**Lifecycle stages.** DECOMMISSION · **Operating states.** NORMAL

**Failure modes addressed.** Unauthorised e-waste export; Reuse before sanitisation

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If disposition cannot be traced for sampled serials, record a U5 UNKNOWN and a Finding.

**Ontology classes.** AssetInstance, EvidenceObject · **Related controls.** MCF-PHY-020, MCF-ENV-015, MCF-CMP-024

**Informative references.** EU WEEE Directive 2012/19/EU; NIST SP 800-88 (media sanitisation)

## ENV-06 Climate adaptation and resource continuity

### MCF-ENV-021

**Heatwave Readiness** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Demonstrate that heat rejection, generators, transformers and battery rooms retain the capacity required by declared outcomes during extreme heat at or beyond the design ambient, and that operations has a tested response when forecasts approach design limits.

**Requirement.** The facility owner shall state the design extreme ambient used for heat rejection, generator and transformer rating, shall evaluate capacity at that ambient and at the declared climate-adjusted ambient, and shall maintain a heatwave procedure triggered by forecast that includes pre-cooling, cleaning of coils, deferral of maintenance, readiness of mobile plant and workload reduction steps. The facility operator shall exercise the procedure before each hot season.

**Assessment criteria**

1. Design extreme ambient is stated with source (e.g. ASHRAE climatic data n-year value).
2. Capacity of heat rejection, generators and transformers at design and climate-adjusted ambient is evaluated and covers declared load, or the shortfall has defined load reduction.
3. Recirculation of hot air at heat-rejection plant is assessed.
4. A forecast-triggered heatwave procedure exists and was exercised before the hot season.
5. Performance in the last heat event was reviewed with lessons applied.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Design extreme ambient dry-bulb | °C | site n=20-year extreme (illustrative) | ASHRAE Handbook climatic design data |
| Climate-adjusted design ambient uplift | K | 2 (illustrative) | Owner-adopted climate projection (e.g. IPCC AR6 scenario) |
| Forecast trigger margin below design ambient | K | 3 (illustrative) | Capability profile |

**Minimum evidence**

- Design ambient statement
- Capacity-at-ambient analysis
- Recirculation study
- Heatwave procedure
- Exercise and event review records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E3; E4; E7 |
| optionalClasses | E5 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | DEGRADED; EMERGENCY |
| periodCoverage | Exercise before the current hot season; last heat event. |
| independence | Analysis reviewed by a mechanical engineer independent of operations. |
| mandatoryItems | Capacity-at-ambient analysis; Heatwave procedure; Exercise record |
| acceptableAlternatives | Recorded performance during an event at or above design ambient |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-06, CG-05. |
| reassessmentTriggers | Record temperature at site; Climate projection update; Heat-rejection plant change |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW, SCENARIO_EXERCISE

**Assessment procedure**

1. Verify design ambient source.
2. Review capacity analysis.
3. Review procedure and exercise.
4. Review last heat event.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING); CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies to all sites; material where design ambient margin is small or recirculation exists.

**Lifecycle stages.** DESIGN, OPERATE · **Operating states.** DEGRADED, EMERGENCY

**Failure modes addressed.** Dry coolers lose capacity above design ambient; Generators derate in heatwave during grid stress; Transformer overheating

**Testing safety.** Exercises are procedural; no plant is deliberately disabled.

**UNKNOWN rule.** If capacity at design ambient is unevaluated, record a U1 UNKNOWN referred to CG-06 and CG-05.

**Ontology classes.** Hazard, CapacityAssertion, FailureScenario · **Related controls.** MCF-THM-004, MCF-POW-005, MCF-ENV-011

**Informative references.** ASHRAE Handbook - Fundamentals (climatic design conditions); ISO 14090 / ISO 14091 (adaptation to climate change); IPCC AR6 (climate scenarios)

### MCF-ENV-022

**Drought Readiness** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure long-term water availability risk is assessed for the site's water-dependent cooling, so that water stress does not become a strategic constraint on AI capability.

**Requirement.** The facility owner shall assess basin-level water stress over the declared planning horizon using recognised water-risk data and climate projections, shall evaluate the security of water entitlements, and shall define the strategy (alternative sources, technology change, reduced water design) if stress exceeds the declared threshold.

**Assessment criteria**

1. A water-stress assessment covers the planning horizon with stated data sources.
2. Water entitlements and their renewal risks are documented.
3. A strategy exists where stress exceeds threshold.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Water-stress planning horizon | years | 20 (illustrative) | Capability profile |

**Minimum evidence**

- Water-stress assessment
- Entitlement documents
- Strategy

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E7 |
| optionalClasses | E5 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | Current assessment within three years. |
| independence | Assessment by a competent hydrology or sustainability specialist. |
| mandatoryItems | Water-stress assessment |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-03. |
| reassessmentTriggers | Drought declaration; Entitlement renewal; Expansion plan |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Review assessment data sources.
2. Review entitlements.
3. Review strategy.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to sites with water-dependent cooling.

**Lifecycle stages.** PLAN, DESIGN · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Entitlement withdrawn; Basin stress forces cooling retrofit

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If no water-stress assessment exists, record a U1 UNKNOWN on long-term water dependency.

**Ontology classes.** Dependency, Resource, Hazard · **Related controls.** MCF-ENV-011, MCF-ENV-024, MCF-DEP-009

**Informative references.** WRI Aqueduct water-risk atlas; ISO 14046 (water footprint); ISO 14091 (climate risk assessment)

### MCF-ENV-023

**Flood Adaptation** · PREVENTIVE · claim type DESIGN · required AL2

**Objective.** Ensure that flood protection for critical plant remains adequate under projected climate change and that temporary flood defences are deployable in time.

**Requirement.** The facility owner shall evaluate flood levels under the declared climate scenario and horizon, shall confirm critical plant remains above the adjusted design level plus freeboard or is protected by permanent or demountable defences, and shall maintain a flood response plan with deployment time for demountable defences shorter than the warning lead time.

**Assessment criteria**

1. Climate-adjusted flood levels are evaluated for the declared scenario and horizon.
2. Critical plant is above adjusted level plus freeboard, or defended.
3. Demountable defence deployment time is shorter than warning lead time, demonstrated by drill.
4. Drainage and pumping capacity is evaluated for adjusted rainfall intensity.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Climate scenario and horizon for flood adaptation | scenario / year | SSP2-4.5 to 2060 (illustrative) | IPCC AR6 scenarios; owner-adopted projection |
| Demountable defence deployment time | hours | less than flood warning lead time (illustrative: 4) | Flood response plan |

**Minimum evidence**

- Climate-adjusted flood assessment
- Plant level survey
- Flood response plan
- Drill records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E7 |
| optionalClasses | E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY |
| periodCoverage | Current assessment; drill within twelve months where defences are demountable. |
| independence | Assessment by a competent flood-risk specialist. |
| mandatoryItems | Climate-adjusted flood assessment |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-09. |
| reassessmentTriggers | Flood map revision; Flood event; Climate projection update |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INSPECTION

**Assessment procedure**

1. Review adjusted flood assessment.
2. Compare plant levels.
3. Review drill records.

**Gate mappings.** CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to all sites with any flood exposure identified in MCF-PHY-001.

**Lifecycle stages.** PLAN, DESIGN, OPERATE · **Operating states.** NORMAL, EMERGENCY

**Failure modes addressed.** Climate-driven flood exceeds original design level; Defences not deployed in time (AIDCF-004 X20)

**Testing safety.** Drills of demountable defences follow manual-handling procedures.

**UNKNOWN rule.** If climate-adjusted flood levels are not evaluated, record a U1 UNKNOWN and limit flood protection claims to current hazard levels.

**Ontology classes.** Hazard, Safeguard, FailureScenario · **Related controls.** MCF-PHY-001, MCF-PHY-008, MCF-RES-003

**Informative references.** ISO 14090 / ISO 14091; IPCC AR6; National flood-risk guidance

### MCF-ENV-024

**Long-Term Resource Constraints** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure long-term constraints on grid capacity, water, permits and land that could limit growth or continuation of AI capability at the site are identified, owned and fed into capacity planning.

**Requirement.** The facility owner shall maintain a resource constraints register covering grid capacity availability and reinforcement timelines, water entitlement, environmental permits and their renewal dates, planning constraints and emission limits, over the declared horizon, and shall review it with capability owners when demand forecasts change.

**Assessment criteria**

1. The register covers grid, water, permit, planning and emission constraints with dates.
2. Each constraint has an owner and mitigation.
3. The register was reviewed with capability owners after the last demand forecast change.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Resource planning horizon | years | 15 (illustrative) | Capability profile |

**Minimum evidence**

- Resource constraints register
- Permit list with renewal dates
- Review minutes

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1 |
| optionalClasses | E6; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Current register. |
| independence | Reviewed by capability owners. |
| mandatoryItems | Resource constraints register |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-01, CG-03. |
| reassessmentTriggers | Demand forecast change; Permit renewal; Grid constraint notice |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY

**Assessment procedure**

1. Review register coverage.
2. Check owners and mitigations.
3. Confirm review with capability owners.

**Gate mappings.** CG-01 Capability and outcome definition (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to all sites with planned growth or long-lived capability.

**Lifecycle stages.** PLAN · **Operating states.** NORMAL

**Failure modes addressed.** Expansion blocked by grid reinforcement delay; Permit lapses; Emission cap limits generator testing

**Testing safety.** Desk-based review of records and meter data; no intervention in plant or IT systems.

**UNKNOWN rule.** If permit renewal dates are unknown, record a U1 UNKNOWN on resource continuity.

**Ontology classes.** Dependency, Resource, CapacityAssertion · **Related controls.** MCF-POW-001, MCF-ENV-022, MCF-CAP-015

**Informative references.** ISO 14001 (environmental management); ISO 50001 (energy management)
