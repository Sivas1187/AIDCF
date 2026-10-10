# AIDCF-007A Control Catalogue — THM Cooling, Thermal and Fluid Infrastructure

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-THM](../../../aidcf-018-domain-guides/AIDCF-018-THM_Cooling_Thermal_and_Fluid_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-THM-001](#mcf-thm-001) | Heat-Load Model | DIRECTIVE | DESIGN | AL2 | — | CG-06, CG-01 |
| [MCF-THM-002](#mcf-thm-002) | Design Capacity | PREVENTIVE | IMPLEMENTATION | AL3 | CG-06 | CG-02 |
| [MCF-THM-003](#mcf-thm-003) | Resilient Capacity | PREVENTIVE | RESILIENCE | AL5 | CG-06 | CG-09, CG-05 |
| [MCF-THM-004](#mcf-thm-004) | Seasonal Derating | PREVENTIVE | OPERATION | AL4 | CG-06 | CG-03 |
| [MCF-THM-005](#mcf-thm-005) | Airflow Management | PREVENTIVE | OPERATION | AL4 | — | CG-06 |
| [MCF-THM-006](#mcf-thm-006) | Containment | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-06, CG-04 |
| [MCF-THM-007](#mcf-thm-007) | CRAH and In-Row Capacity | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-06 |
| [MCF-THM-008](#mcf-thm-008) | Air-Side Monitoring | DETECTIVE | OPERATION | AL4 | — | CG-06 |
| [MCF-THM-009](#mcf-thm-009) | Direct-to-Chip Architecture | DIRECTIVE | DESIGN | AL2 | — | CG-06 |
| [MCF-THM-010](#mcf-thm-010) | CDU Capacity | PREVENTIVE | EFFECTIVENESS | AL5 | CG-06 | CG-07 |
| [MCF-THM-011](#mcf-thm-011) | Secondary Loop Integrity | PREVENTIVE | OPERATION | AL4 | CG-06 | CG-09 |
| [MCF-THM-012](#mcf-thm-012) | Quick-Disconnect Management | PREVENTIVE | OPERATION | AL4 | — | CG-06, CG-04, CG-14 |
| [MCF-THM-013](#mcf-thm-013) | Chiller Capacity | PREVENTIVE | EFFECTIVENESS | AL5 | CG-06 | CG-04 |
| [MCF-THM-014](#mcf-thm-014) | Cooling Tower or Dry Cooler | PREVENTIVE | OPERATION | AL4 | — | CG-06 |
| [MCF-THM-015](#mcf-thm-015) | Water Continuity | PREVENTIVE | RESILIENCE | AL5 | CG-06 | CG-03 |
| [MCF-THM-016](#mcf-thm-016) | Heat-Rejection Dependency | DIRECTIVE | DESIGN | AL2 | — | CG-03, CG-09, CG-06 |
| [MCF-THM-017](#mcf-thm-017) | Coolant Compatibility | PREVENTIVE | DESIGN | AL2 | — | CG-04, CG-06 |
| [MCF-THM-018](#mcf-thm-018) | Water Quality | PREVENTIVE | OPERATION | AL4 | CG-04 | CG-06 |
| [MCF-THM-019](#mcf-thm-019) | Leak Detection | DETECTIVE | EFFECTIVENESS | AL5 | — | CG-06, CG-09, CG-04 |
| [MCF-THM-020](#mcf-thm-020) | Isolation and Drainage | CORRECTIVE | EFFECTIVENESS | AL5 | CG-09 | CG-04, CG-06 |
| [MCF-THM-021](#mcf-thm-021) | Control Stability | PREVENTIVE | EFFECTIVENESS | AL5 | CG-07 | CG-06, CG-15 |
| [MCF-THM-022](#mcf-thm-022) | Sensor Trust | DETECTIVE | OPERATION | AL4 | — | CG-07, CG-06 |
| [MCF-THM-023](#mcf-thm-023) | Maintenance States | PREVENTIVE | OPERATION | AL4 | — | CG-06, CG-14, CG-04 |
| [MCF-THM-024](#mcf-thm-024) | Thermal Recovery | RECOVERY | RESILIENCE | AL5 | CG-10 | CG-06 |

## THM-01 Thermal architecture and capacity

### MCF-THM-001

**Heat-Load Model** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Establish an authoritative, versioned model of the heat that each fault domain must reject, split by heat-removal path (air, direct-to-chip liquid, rear-door, immersion), so that every downstream capacity, redundancy and recovery claim is tested against a defensible demand figure rather than nameplate or average IT power.

**Requirement.** The thermal engineering authority shall maintain a versioned heat-load model for each Capability Instance that states, per hall, row, rack group and CDU or air-handling fault domain, the design and peak heat load in kW, the liquid-capture ratio by platform, residual heat to air, and the transient load profile of synchronous AI training. The facility owner shall approve the model and shall not accept capacity claims that are not traceable to the current model version.

**Assessment criteria**

1. The model exists as a controlled, versioned document or dataset with a named owner and approval record dated within the review interval.
2. Heat load is apportioned to each fault domain (hall, row, rack group, CDU loop, CRAH zone) and the sum reconciles to the IT power model within the stated tolerance.
3. For each liquid-cooled platform, the liquid-capture ratio and residual air-side heat are taken from OEM thermal data or measurement and the source is cited.
4. The model includes a synchronous-load transient profile (step change and ramp rate) for training workloads, not only steady-state averages.
5. Non-IT heat (power conversion losses, lighting, envelope gain, CDU pump heat) is included or explicitly excluded with rationale.
6. Planned densification and the next approved deployment phase are represented as named scenarios.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Rack design heat load (liquid-cooled AI rack) | kW per rack | 120 (illustrative) | Platform OEM thermal design data; site-specific |
| Liquid-capture ratio (direct-to-chip platform) | % of rack heat to liquid | 80 (illustrative) | OEM thermal data or measured; varies by platform generation |
| Synchronous load step | % of fault-domain design load within 1 s | 50 (illustrative) | Workload characterisation of synchronous training; to be measured |
| Model-to-measured reconciliation tolerance | % of measured heat load | ±10 (illustrative) | Capability profile |

**Minimum evidence**

- Current heat-load model with version, owner and approval signature
- IT power model or rack power budget the heat-load model is reconciled to
- OEM thermal design guides or datasheets for each deployed accelerator platform
- Fault-domain allocation table (rack → CDU loop → CRAH zone → chilled-water or facility-water branch)
- Comparison of model against measured heat load for at least one operating hall where available

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; TRANSITION |
| periodCoverage | Current model version; reviewed at least every 12 months and at each deployment phase |
| independence | Model review by an engineer not responsible for producing the model |
| mandatoryItems | Approved heat-load model version; OEM thermal data per platform |
| acceptableAlternatives | Computational fluid dynamics study that includes the same apportionment; Measured heat-load dataset from metered CDUs and air handlers for existing halls |
| unknownEffect | US3 Material: capacity controls MCF-THM-002/003 cannot be rated CONFORMING against an unverified demand; decision condition recorded |
| reassessmentTriggers | New accelerator platform or rack density; Change of liquid-capture ratio; Measured load deviates beyond tolerance; Deployment phase change |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Obtain the current model and confirm version, owner and approval.
2. Trace three sampled rack groups from OEM thermal data through the model to the fault-domain totals.
3. Reconcile total modelled heat to the IT power budget and to metered data where available.
4. Check that transient load and densification scenarios are represented.
5. Record deviations beyond tolerance as Findings and unresolved inputs as UNKNOWN Records.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING); CG-01 Capability and outcome definition (SUPPORTING)

**Applicability.** Applies to every Capability Instance with in-scope heat-removal infrastructure. Not applicable only where the thermal infrastructure is wholly outside the assessment boundary and that exclusion is approved under CG-02.

**Lifecycle stages.** PLAN, DESIGN, CHANGE · **Operating states.** NORMAL, TRANSITION

**Failure modes addressed.** Capacity sized to average rather than peak synchronous load; Liquid-capture ratio overstated so residual air heat exceeds air-side capacity; Heat load not apportioned to fault domains, hiding local overload; Stale model after densification

**Testing safety.** Desk-based; no intrusive testing. Any metering added to validate the model is installed under the site change process.

**UNKNOWN rule.** If the liquid-capture ratio or transient profile for a deployed platform cannot be sourced, record a U1 UNKNOWN against this control and carry it to every capacity control that depends on that platform.

**Ontology classes.** CapacityAssertion, InfrastructureSystem, FaultDomain, ArchitectureSnapshot · **Related controls.** MCF-THM-002, MCF-THM-003, MCF-CAP-013, MCF-CAP-014

**Informative references.** ASHRAE TC 9.9 Thermal Guidelines for Data Processing Environments; ASHRAE TC 9.9 Liquid Cooling Guidelines for Datacom Equipment Centers; AIDCF-013 (AI Data Centre Assurance Reference Architecture); ASHRAE Standard 90.4 (energy standard for data centres)

### MCF-THM-002

**Design Capacity** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Demonstrate that the installed and commissioned capacity of every stage of the heat-removal path (air, TCS, CDU, FWS, heat rejection) meets the current heat-load model at design conditions, so that the facility can actually remove the heat it is declared to support.

**Requirement.** The thermal engineering authority shall demonstrate, for each heat-removal stage and fault domain, that commissioned capacity at design ambient and design supply temperatures is not less than the design heat load from MCF-THM-001 plus the approved margin. The facility operator shall hold the commissioning records and shall not admit IT load beyond the demonstrated capacity of the weakest stage in the path.

**Assessment criteria**

1. A stage-by-stage capacity table exists (CRAH/fan wall, rear-door, CDU, TCS pumps, FWS pumps, chillers, dry coolers or towers) with rated and commissioned capacity at stated conditions.
2. The weakest stage in each path is identified and its commissioned capacity is ≥ design load plus margin.
3. Commissioning (functional and integrated systems tests) was performed at or extrapolated with documented method to design load using load banks or equivalent.
4. Capacity ratings are stated at the actual design supply temperature and ΔT, not catalogue nominal conditions.
5. Admitted IT load is reconciled to the demonstrated capacity and no fault domain exceeds it.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Design capacity margin above design heat load | % | 10 (illustrative) | Capability profile; design authority |
| Commissioning load-bank test level | % of design heat load | 100 (illustrative) | ASHRAE Guideline 0 practice; site commissioning plan |

**Minimum evidence**

- Stage-by-stage capacity table with rated and commissioned figures
- Integrated systems test (IST) or Level 5 commissioning report with load-bank data
- Equipment performance data at design conditions
- Current admitted-load register per fault domain

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; TRANSITION |
| periodCoverage | Commissioning record plus most recent 3 months of load telemetry |
| independence | Commissioning witnessed by a commissioning authority independent of the installing contractor |
| mandatoryItems | Commissioning report with load-bank results; Current admitted-load register |
| acceptableAlternatives | Retro-commissioning test at partial load with validated extrapolation method reviewed by an independent engineer |
| unknownEffect | US4 Critical: CG-06 Gate Result becomes UNKNOWN for the affected fault domains; decision ceiling per CG-06 |
| reassessmentTriggers | Admitted IT load approaches demonstrated capacity; Equipment replacement or capacity upgrade; Change of design supply temperature |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS, INSPECTION

**Assessment procedure**

1. Obtain the capacity table and commissioning reports for the sampled fault domains.
2. Verify test conditions (ambient, supply temperature, load level) against design conditions.
3. Identify the weakest stage in each path and compare with the heat-load model.
4. Reconcile admitted IT load per fault domain with demonstrated capacity.
5. Inspect nameplates of a sample of units against the capacity table.

**Gate mappings.** CG-06 Thermal continuity (CRITICAL); CG-02 Boundary and architecture integrity (SUPPORTING)

**Applicability.** Applies to all in-scope heat-removal stages. For colocation where the operator provides cooling as a service, applies to the provider-supplied evidence under the service interface.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, CHANGE · **Operating states.** NORMAL, TRANSITION

**Failure modes addressed.** Catalogue capacity assumed at non-design conditions; Weakest stage (often CDU or FWS pumps) unidentified; Load admitted above demonstrated capacity; Commissioning performed at partial load without valid extrapolation

**Testing safety.** Load-bank testing involves hazardous energy and high-temperature exhaust; it requires an approved commissioning plan, permit-to-work and the site authorising engineer's authority. Assessors observe or review; they do not operate plant.

**UNKNOWN rule.** If commissioning at design load cannot be evidenced for any stage, record UNKNOWN (U1 or U5) for that fault domain; the result cannot be CONFORMING on rated data alone.

**Ontology classes.** CapacityAssertion, InfrastructureSystem, AssetInstance, TestRecord · **Related controls.** MCF-THM-001, MCF-THM-003, MCF-THM-010, MCF-THM-013

**Informative references.** ASHRAE Guideline 0 (the commissioning process); ASHRAE TC 9.9 Thermal Guidelines for Data Processing Environments; ASHRAE TC 9.9 Liquid Cooling Guidelines for Datacom Equipment Centers; Uptime Institute Tier Standard: Topology; ANSI/TIA-942 (telecommunications infrastructure standard for data centres)

### MCF-THM-003

**Resilient Capacity** · PREVENTIVE · claim type RESILIENCE · required AL5

**Objective.** Ensure heat removal remains within the IT inlet and coolant envelopes when any single credible component, path or controller is lost, during maintenance, and through power-event transients (utility loss, UPS transfer, generator start, chiller restart).

**Requirement.** The thermal engineering authority shall define the declared redundancy (for example N+1, 2N) for each heat-removal stage and shall demonstrate that, with the largest single unit or path out of service, capacity meets design load. The facility owner shall demonstrate thermal ride-through: that pumps, CDUs and controls needed to keep coolant moving are on continuous power, and that thermal storage or ride-through margin keeps TCS supply and IT inlet temperatures within limits until chillers or heat rejection restart.

**Assessment criteria**

1. Declared redundancy per stage is documented and the N−1 capacity analysis shows design load is met with the largest unit lost.
2. Common-mode elements that defeat redundancy (shared header, single controller, common power board, single make-up water feed) are identified with treatment.
3. TCS and CDU pumps and their controls are supplied from UPS or equivalent continuous power, verified on the single-line diagram.
4. A ride-through analysis or test shows TCS supply temperature and IT inlet temperature stay within declared limits from loss of mechanical cooling until restart to capacity.
5. An integrated test (utility loss / generator transfer) recorded coolant temperature, flow and IT throttling during the transient.
6. Redundancy is maintained, or a documented risk acceptance applies, during planned maintenance of each stage.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Declared redundancy for CDU stage | configuration | N+1 (illustrative) | Capability profile |
| Chiller restart-to-capacity time after power interruption | s | 300 (illustrative) | Manufacturer rapid-restart data; verify by test |
| Thermal ride-through required | s | 600 (illustrative) | Derived: restart time plus margin; capability profile |
| Maximum TCS supply temperature rise during transient | K | 5 (illustrative) | OEM coolant inlet limit minus normal setpoint |

**Minimum evidence**

- N−1 capacity analysis per stage
- Single-line diagram extract showing pump/CDU/control power sources
- Ride-through calculation including thermal-storage volume and pipework thermal mass
- IST or black-building test record with time-stamped coolant temperature and flow traces
- Maintenance-state redundancy matrix

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE; EMERGENCY; TRANSITION; RECOVERY |
| periodCoverage | Most recent integrated transient test (≤ 24 months) plus 12 months of operating data |
| independence | Integrated test witnessed by an independent commissioning or engineering party |
| mandatoryItems | N−1 capacity analysis; Time-stamped transient test traces |
| acceptableAlternatives | Validated dynamic thermal simulation calibrated against a partial transient test, reviewed independently |
| unknownEffect | US4 Critical: CG-06 UNKNOWN for affected fault domains; decision ≤ LIMITED until ride-through is evidenced |
| reassessmentTriggers | Load growth above tested level; Change to UPS coverage of mechanical loads; Thermal-storage modification; Any thermal excursion during a power event |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW, TEST, SCENARIO_EXERCISE, RECONCILIATION

**Assessment procedure**

1. Review the redundancy declaration and N−1 analysis for each stage.
2. Trace pump, CDU and controller power to UPS on the single-line diagram.
3. Review the ride-through calculation inputs (volume, ΔT, load) against current heat load.
4. Examine transient test traces for TCS supply temperature, flow and IT throttling events.
5. Compare maintenance-state redundancy matrix with the maintenance schedule.
6. Record common-mode elements without treatment as Findings.

**Gate mappings.** CG-06 Thermal continuity (CRITICAL); CG-09 Failure containment (SUPPORTING); CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies wherever a Service Outcome requires continuity of heat removal through component loss or power events. A reduced scope applies where the outcome tolerates controlled shutdown, provided that tolerance is approved under CG-01.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, TRANSITION, RECOVERY

**Failure modes addressed.** Redundancy defeated by shared header or controller; CDU or TCS pumps not on UPS, stopping coolant flow on utility loss; Chiller restart longer than ride-through, causing thermal trip; Redundancy lost during maintenance without compensating measure

**Testing safety.** Utility-loss and transfer tests are hazardous and capability-affecting. Requires a permit-to-work and method statement approved by the site authorising engineer, the IT operator's agreement on load at risk, and a rollback plan. Prefer analysis and records of previous tests over new disruptive tests.

**UNKNOWN rule.** If no transient test or calibrated simulation exists for the current load, record a U5 coverage-gap UNKNOWN; CONFORMING requires transient evidence, not steady-state capacity alone.

**Ontology classes.** FaultDomain, CapacityAssertion, FailureScenario, Safeguard, TestRecord · **Related controls.** MCF-THM-002, MCF-THM-024, MCF-POW-009, MCF-POW-019, MCF-DEP-005

**Informative references.** Uptime Institute Tier Standard: Topology; ASHRAE TC 9.9 Thermal Guidelines for Data Processing Environments; ASHRAE TC 9.9 Liquid Cooling Guidelines for Datacom Equipment Centers; EN 50600-2-3 / ISO/IEC 22237-3 (data centre environmental control); ASHRAE Guideline 0 (the commissioning process); AIDCF-004 (Threat, Hazard and Failure Model)

### MCF-THM-004

**Seasonal Derating** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure heat-rejection and economiser capacity is rated at the site's extreme design ambient conditions, including projected climate change, so that capacity claims hold through heatwaves and high wet-bulb periods.

**Requirement.** The thermal engineering authority shall define design ambient dry-bulb and wet-bulb conditions from a stated climatic data source and return period, shall derate chillers, dry coolers and cooling towers to those conditions, and shall review the derating annually against observed extremes. The facility operator shall monitor available heat-rejection capacity against load during high-ambient periods and shall invoke load-management procedures before capacity is exceeded.

**Assessment criteria**

1. Design ambient conditions are documented with source and return period (for example an extreme annual percentile from a named climatic dataset).
2. Heat-rejection equipment capacity is derated to design ambient with manufacturer data at those conditions.
3. Observed ambient extremes over the last 12 months (including any period above design ambient) are compared with the design basis.
4. Available capacity against load during the hottest observed period shows the declared margin was maintained.
5. A high-ambient procedure exists with trigger thresholds and load-management actions agreed with the AI platform operator.
6. A climate-projection allowance is defined for the asset life or its absence is recorded.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Design ambient dry-bulb | °C | site-specific (illustrative: 0.4% annual extreme) | ASHRAE climatic design conditions or national equivalent |
| Design ambient wet-bulb (evaporative systems) | °C | site-specific | ASHRAE climatic design conditions |
| Climate-change allowance on design ambient | K | 2 (illustrative) | Capability profile; regional projections |
| High-ambient action threshold | % of derated capacity | 90 (illustrative) | Capability profile |

**Minimum evidence**

- Climatic design basis with source
- Manufacturer capacity data at design ambient
- 12 months of ambient and heat-rejection load telemetry
- High-ambient operating procedure and records of its use

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY |
| periodCoverage | At least 12 months including the local peak-ambient season |
| independence | Ambient data cross-checked against an independent meteorological source |
| mandatoryItems | Climatic design basis; Peak-season capacity-versus-load trend |
| acceptableAlternatives | Where less than a year of operation exists, manufacturer derated performance plus a witnessed high-ambient test or validated simulation |
| unknownEffect | US4 Critical: CG-06 UNKNOWN for high-ambient states; decision ceiling applied to EMERGENCY/peak-season claims |
| reassessmentTriggers | Observed ambient above design basis; Fouling or performance decline of heat-rejection units; Change to economiser or setpoint strategy; Load growth |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, SAMPLING, INQUIRY

**Assessment procedure**

1. Confirm the climatic design basis and its source.
2. Check derated capacity calculations against manufacturer data at design ambient.
3. Analyse telemetry for the hottest days in the period: load, available capacity, supply temperatures.
4. Review high-ambient procedure use and outcomes.
5. Record any period where margin fell below threshold as a Finding.

**Gate mappings.** CG-06 Thermal continuity (CRITICAL); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to all sites with ambient-dependent heat rejection. Not applicable to heat rejection to a source independent of ambient (for example a stable ground-water or district system), where MCF-THM-016 covers the dependency.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY

**Failure modes addressed.** Capacity rated at nominal rather than extreme ambient; Recirculation of hot exhaust raising effective ambient at dry coolers; Fouled coils reducing capacity in summer; No load-management plan for heatwaves

**Testing safety.** Analysis of records only. High-ambient tests are not induced; any witnessed test during natural peak conditions follows the site permit-to-work.

**UNKNOWN rule.** If design ambient basis or peak-season data is unavailable, record UNKNOWN (U1/U5); do not infer peak-season adequacy from mild-season data.

**Ontology classes.** CapacityAssertion, OperatingState, InfrastructureSystem, Hazard · **Related controls.** MCF-THM-001, MCF-THM-013, MCF-THM-014, MCF-ENV-021

**Informative references.** ASHRAE Standard 169 / ASHRAE Handbook Fundamentals (climatic design conditions); ASHRAE TC 9.9 Thermal Guidelines for Data Processing Environments; EN 50600-2-3 / ISO/IEC 22237-3 (data centre environmental control); AIDCF-004 (Threat, Hazard and Failure Model)

## THM-02 Air cooling systems

### MCF-THM-005

**Airflow Management** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure cold supply air reaches IT inlets at the required temperature and volume without bypass or recirculation, including the residual air-side heat from liquid-cooled racks.

**Requirement.** The facility operator shall maintain an airflow management regime (blanking, brush grommets, cable cut-out sealing, floor-tile or supply-diffuser placement, fan-wall or CRAH control) and shall verify by periodic measurement that IT inlet temperatures at the top, middle and bottom of sampled racks remain within the declared envelope and that bypass and recirculation are within declared limits.

**Assessment criteria**

1. IT inlet temperature measurements at multiple heights across sampled racks are within the declared envelope for the period.
2. Supply/return temperature differential at air handlers is consistent with low bypass (within declared range).
3. A sample inspection finds blanking panels, cable sealing and tile/diffuser placement consistent with the airflow standard.
4. Residual air heat from liquid-cooled racks is included in airflow planning and measured in at least one hall.
5. Exceptions (hot spots, missing blanking) are ticketed and closed within the declared time.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| IT inlet temperature envelope | °C | 18–27 | ASHRAE TC 9.9 recommended envelope (classes A1–A4); site may adopt narrower OEM limits |
| Air-handler ΔT lower bound (bypass indicator) | K | 8 (illustrative) | Capability profile |
| Hot-spot closure time | h | 24 (illustrative) | Capability profile |

**Minimum evidence**

- IT inlet temperature telemetry at multiple rack heights
- Airflow standard and inspection checklist
- Inspection records for sampled rows
- Hot-spot tickets and closure records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Most recent 6 months |
| independence | Sample inspection by a party other than the hall operations team |
| mandatoryItems | Inlet temperature telemetry; Sample inspection record |
| acceptableAlternatives | Handheld survey grid at defined points where rack sensors are not deployed |
| unknownEffect | US3 Material: air-side adequacy uncertain; condition recorded against CG-06 supporting evaluation |
| reassessmentTriggers | Rack layout change; New platform with different airflow; Hot-spot alarms above threshold |

**Assessment methods.** OBSERVATION, INSPECTION, SAMPLING, ANALYSIS

**Assessment procedure**

1. Select sample rows covering highest-density racks.
2. Analyse inlet telemetry by height for the period.
3. Walk the sampled rows and inspect blanking, sealing and containment interfaces.
4. Review hot-spot tickets for closure time.
5. Compare air-handler ΔT with the bypass indicator.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies wherever any IT heat is removed by air, including residual heat from liquid-cooled racks. Not applicable to fully immersion-cooled halls with no air-cooled IT.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Recirculation of exhaust air to inlets; Bypass air reducing effective capacity; Missing blanking after maintenance; Residual heat from liquid racks unplanned

**Testing safety.** Non-intrusive: inspection without opening live electrical enclosures; follow hall access rules and hot-aisle heat-stress limits.

**UNKNOWN rule.** If inlet measurement is absent for high-density racks, record U5 UNKNOWN for those racks; do not rely on room-average temperatures.

**Ontology classes.** InfrastructureSystem, AssetInstance, Safeguard · **Related controls.** MCF-THM-006, MCF-THM-008, MCF-THM-001

**Informative references.** ASHRAE TC 9.9 Thermal Guidelines for Data Processing Environments; EN 50600-2-3 / ISO/IEC 22237-3 (data centre environmental control); ANSI/TIA-942 (telecommunications infrastructure standard for data centres)

### MCF-THM-006

**Containment** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure hot-aisle or cold-aisle containment, chimney cabinets or rear-door heat exchangers are installed and maintained as designed so that supply and exhaust air streams remain separated, and that containment does not compromise fire detection, suppression or egress.

**Requirement.** The facility operator shall install and maintain containment in accordance with the approved design, shall reconcile the as-built containment (doors, roof panels, end-of-row doors, rear-door heat exchangers) with the design, and shall demonstrate that fire detection and suppression coverage inside containment and the release of drop-away or fusible panels have been accepted by the fire-safety authority.

**Assessment criteria**

1. As-built containment reconciles to the approved design for sampled rows.
2. Doors, roof panels and seals are present and closed in sampled rows.
3. Fire detection and suppression design covers the contained volume and has fire-safety authority acceptance.
4. Where rear-door heat exchangers are used, their water connections, leak detection and fan power are documented and their capacity matches rack heat.
5. Egress from contained aisles meets the site safety rules.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum leakage area of containment | % of containment area | declared by design (illustrative 2) | Design authority |

**Minimum evidence**

- Containment design drawings
- As-built inspection record
- Fire-safety authority acceptance for contained aisles
- Rear-door heat exchanger schedule and connection details (if used)

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E5 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Inspection within 6 months |
| independence | Fire-safety acceptance from the competent fire authority or fire engineer |
| mandatoryItems | As-built inspection; Fire-safety acceptance |
| acceptableAlternatives | Thermal imaging survey demonstrating separation where physical inspection is restricted |
| unknownEffect | US3 Material: air separation unverified; CG-06 supporting; any fire-safety acceptance gap escalated to CG-04 evaluation |
| reassessmentTriggers | Row reconfiguration; Containment modification; Fire system change |

**Assessment methods.** INSPECTION, DOCUMENT_REVIEW, RECONCILIATION

**Assessment procedure**

1. Obtain containment design and fire acceptance.
2. Inspect sampled rows for completeness and condition.
3. Reconcile rear-door heat exchanger connections and leak detection where present.
4. Record deviations.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies where containment or rear-door heat exchangers are part of the air-side design. Not applicable to open-room designs that declare no containment, if MCF-THM-005 demonstrates inlet compliance.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Open containment doors causing mixing; Containment obstructing suppression agent distribution; Rear-door heat exchanger fan or water failure unmonitored

**Testing safety.** Inspection only. Do not open containment roof panels or trigger drop-away mechanisms.

**UNKNOWN rule.** If fire-safety acceptance cannot be produced, record UNKNOWN and refer to the CG-04 evaluation; the control cannot be CONFORMING.

**Ontology classes.** AssetInstance, Safeguard, Hazard · **Related controls.** MCF-THM-005, MCF-THM-019, MCF-PHY-021, MCF-PHY-022

**Informative references.** ASHRAE TC 9.9 Thermal Guidelines for Data Processing Environments; NFPA 75 (fire protection of information technology equipment); EN 50600-2-3 / ISO/IEC 22237-3 (data centre environmental control)

### MCF-THM-007

**CRAH and In-Row Capacity** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure computer-room air handlers, fan walls and in-row coolers deliver the air-side capacity required by the heat-load model, with declared redundancy, at the actual chilled-water or facility-water supply temperature.

**Requirement.** The facility operator shall maintain a unit schedule for air handlers and in-row coolers stating sensible capacity at the actual entering-water and return-air conditions, and shall demonstrate that each air-cooling zone meets residual air heat with the declared redundancy. The thermal engineering authority shall re-rate capacity when supply water temperature or return-air setpoints change.

**Assessment criteria**

1. Unit schedule states sensible capacity at site entering-water and return-air conditions.
2. Each zone's capacity with the largest unit out of service meets zone air-side heat load.
3. Fan, valve and controller configuration matches commissioning records for sampled units.
4. Zone heat load used is the residual air heat from MCF-THM-001, including liquid-rack residual heat.
5. Units are maintained per schedule with no overdue critical maintenance in the sample.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Air-side redundancy per zone | configuration | N+1 (illustrative) | Capability profile |
| Entering-water temperature for rating | °C | site design value | Design basis |

**Minimum evidence**

- Unit schedule with rated sensible capacity at site conditions
- Zone capacity analysis
- Unit configuration export or BMS point list
- Air-handler and in-row cooler planned-maintenance completion records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4; E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | Current configuration plus 6 months maintenance history |
| independence | Configuration export obtained directly from BMS rather than operator summary |
| mandatoryItems | Zone N−1 capacity analysis; Configuration export |
| acceptableAlternatives | Commissioning functional performance test results at site conditions |
| unknownEffect | US3 Material: zone air-side capacity uncertain; CG-06 supporting evaluation required |
| reassessmentTriggers | Supply water temperature change; Unit replacement; Zone load change |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INSPECTION, ANALYSIS

**Assessment procedure**

1. Obtain unit schedule and zone analysis.
2. Recalculate one zone's N−1 capacity at site conditions.
3. Reconcile configuration export with commissioning settings.
4. Check maintenance records for sampled units.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies where air handlers or in-row coolers remove in-scope heat.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Capacity overstated at elevated water temperature; Zone redundancy lost due to unit placement; Fan speed limits misconfigured

**Testing safety.** Records and configuration review. Any unit isolation to verify redundancy follows site permit-to-work.

**UNKNOWN rule.** If unit capacity at site water temperature is not documented, record UNKNOWN (U1) for the zone.

**Ontology classes.** AssetInstance, CapacityAssertion, InfrastructureSystem · **Related controls.** MCF-THM-001, MCF-THM-002, MCF-THM-005

**Informative references.** ASHRAE TC 9.9 Thermal Guidelines for Data Processing Environments; EN 50600-2-3 / ISO/IEC 22237-3 (data centre environmental control); ASHRAE Guideline 0 (the commissioning process)

### MCF-THM-008

**Air-Side Monitoring** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure air temperature, humidity and differential pressure are measured at points that represent IT inlet conditions, with alarm thresholds that give operators time to act before IT thermal limits or throttling are reached.

**Requirement.** The facility operator shall deploy and maintain air-side sensors at IT inlet positions (not only at return air), with calibrated accuracy, defined alarm thresholds tiered below the IT envelope limits, and alarm routing to a staffed function. The facility operator shall review alarm performance, sensor coverage and nuisance alarms at least quarterly.

**Assessment criteria**

1. Sensor coverage includes IT inlet positions in every row of high-density racks.
2. Sensors have calibration records within the calibration interval.
3. Warning and critical thresholds are defined below the declared envelope limits and documented.
4. Alarm routing reaches a staffed function and response times are recorded.
5. Data gaps and sensor failures are detected and tracked.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Inlet sensor density | sensors per row | ≥ 3 (illustrative) | Capability profile |
| Sensor accuracy | K | ±0.5 (illustrative) | Capability profile; instrument specification |
| Calibration interval | months | 12 (illustrative) | Instrument manufacturer / site metrology policy |

**Minimum evidence**

- Sensor layout drawing or point list
- Calibration certificates for air-side temperature and humidity sensors
- Alarm threshold schedule
- Alarm log and response records
- Telemetry data-completeness report

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | Most recent 3 months of telemetry and alarm logs |
| independence | Spot check with a calibrated reference instrument by the assessor |
| mandatoryItems | Point list with thresholds; Alarm and response log |
| acceptableAlternatives | Portable logger survey for halls with incomplete fixed sensors |
| unknownEffect | US2 Moderate: confidence ceiling CONF-2 for air-side operating claims |
| reassessmentTriggers | Sensor replacement or relocation; Threshold change; Missed alarm incident |

**Assessment methods.** INSPECTION, SAMPLING, ANALYSIS, REPERFORMANCE

**Assessment procedure**

1. Compare point list with rack layout.
2. Sample calibration records.
3. Review alarm thresholds against the envelope.
4. Analyse alarm log for response time and gaps.
5. Spot-check sensor reading against reference instrument.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies wherever air-side cooling serves in-scope IT.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Sensors at return air only, masking inlet hot spots; Uncalibrated sensors reading low; Alarms routed to unstaffed queue; Data gaps unnoticed

**Testing safety.** Reference-instrument spot checks are non-intrusive; do not disconnect live sensors.

**UNKNOWN rule.** If sensor calibration or data completeness cannot be shown, treat telemetry as R2 and record UNKNOWN for operating claims relying on it.

**Ontology classes.** AssetInstance, Safeguard, EvidenceObject · **Related controls.** MCF-THM-005, MCF-THM-022, MCF-OPS-013

**Informative references.** ASHRAE TC 9.9 Thermal Guidelines for Data Processing Environments; EN 50600-2-3 / ISO/IEC 22237-3 (data centre environmental control)

## THM-03 Liquid cooling systems

### MCF-THM-009

**Direct-to-Chip Architecture** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure the direct-to-chip liquid-cooling architecture (cold plates, manifolds, technology cooling system, CDUs and facility water interface) is designed to the accelerator OEM's coolant, temperature, flow, pressure and wetted-material requirements and to an explicit facility water class.

**Requirement.** The thermal engineering authority shall document a direct-to-chip design basis stating: the TCS fluid, supply temperature range, minimum flow per rack and per cold plate, maximum pressure and differential pressure, filtration, wetted materials, and the ASHRAE liquid-cooling W-class of the facility water system at the CDU interface. The facility owner shall obtain written OEM confirmation that the design basis meets the platform requirements and shall maintain a TCS/FWS P&ID.

**Assessment criteria**

1. The design basis states TCS fluid, supply temperature, flow, pressure, filtration and wetted materials, each with OEM source.
2. The FWS-to-TCS interface is classified by W-class with the facility water supply temperature range stated.
3. The approach temperature across the CDU heat exchanger is stated and the TCS supply temperature is achievable at worst-case FWS supply temperature.
4. A current P&ID shows TCS and FWS loops, CDUs, isolation valves, filters, expansion and fill points, and sensors.
5. OEM confirmation of compatibility with the design basis exists for each deployed platform.
6. The architecture identifies whether CDUs are liquid-to-liquid or liquid-to-air and the consequences for heat-rejection dependency.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Facility water class at CDU interface | ASHRAE W-class | W32 (illustrative) | ASHRAE TC 9.9 liquid-cooling classes W17–W45 and W+ |
| TCS supply temperature to cold plates | °C | OEM-specified (illustrative 30–40) | Platform OEM specification |
| CDU heat-exchanger approach temperature | K | 3 (illustrative) | CDU manufacturer data |
| TCS filtration rating | µm | 50 (illustrative; OEM may require finer) | Platform OEM specification; OCP cold-plate guidance |

**Minimum evidence**

- Direct-to-chip design basis document
- TCS/FWS P&ID
- OEM coolant and facility requirements documents
- OEM compatibility confirmation
- CDU selection data at design FWS temperature

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; TRANSITION |
| periodCoverage | Current design-basis version |
| independence | Design review by an engineer independent of the cooling vendor |
| mandatoryItems | Design basis; P&ID; OEM requirement documents |
| acceptableAlternatives | OEM-supplied reference design adopted without modification, with deviations listed |
| unknownEffect | US3 Material: liquid-cooling design adequacy uncertain; CG-06 supporting; downstream CDU and loop controls conditioned |
| reassessmentTriggers | New platform or cold-plate generation; Change of TCS fluid; Change of FWS temperature strategy |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INQUIRY

**Assessment procedure**

1. Obtain design basis, P&ID and OEM requirements.
2. Compare each design parameter with the OEM requirement.
3. Check approach temperature: worst-case FWS supply + approach ≤ maximum TCS supply.
4. Confirm OEM compatibility statements.
5. Record mismatches as Findings.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies where any in-scope IT is cooled by direct-to-chip cold plates. Immersion systems are covered by MCF-THM-017 and MCF-THM-010 for their coolant and heat-exchange stages.

**Lifecycle stages.** PLAN, DESIGN, CHANGE · **Operating states.** NORMAL, TRANSITION

**Failure modes addressed.** TCS supply temperature unattainable at peak FWS temperature; Wetted-material incompatibility causing corrosion; Flow per cold plate below OEM minimum; Undocumented loop topology

**Testing safety.** Desk-based review; no intrusive action.

**UNKNOWN rule.** If OEM requirements for a platform are unavailable, record U1 UNKNOWN and treat dependent CDU capacity claims as unverified.

**Ontology classes.** InfrastructureSystem, Interface, ArchitectureSnapshot, Resource · **Related controls.** MCF-THM-010, MCF-THM-011, MCF-THM-017, MCF-CMP-003

**Informative references.** ASHRAE TC 9.9 Liquid Cooling Guidelines for Datacom Equipment Centers; Open Compute Project Advanced Cooling Solutions guidance (cold plate, CDU, immersion); ASHRAE TC 9.9 Thermal Guidelines for Data Processing Environments; AIDCF-013 (AI Data Centre Assurance Reference Architecture)

### MCF-THM-010

**CDU Capacity** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Demonstrate that coolant distribution units deliver the required heat transfer, flow and supply temperature to every served rack under design load, with declared redundancy of pumps, heat exchangers and power supplies.

**Requirement.** The thermal engineering authority shall demonstrate, by commissioning or periodic test, that each CDU group delivers design heat transfer at design FWS temperature with the declared pump and heat-exchanger redundancy, and that pump failover maintains flow without TCS supply temperature leaving the OEM limit. The facility operator shall not connect racks to a CDU group beyond its demonstrated capacity.

**Assessment criteria**

1. Each CDU group has a test record at design load (or load bank) showing heat transfer, TCS supply temperature and flow.
2. Pump redundancy (for example duty/standby or N+1) is tested by failing a duty pump; flow recovers within the declared time without exceeding TCS temperature limits.
3. CDU power supplies are dual-fed or the single-feed risk is treated under MCF-THM-003.
4. Racks connected per CDU group are within the demonstrated capacity.
5. For liquid-to-air CDUs, capacity is rated at the hall air temperature actually available.
6. Strainers and filters are monitored for differential pressure and the impact of fouling on flow is bounded.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| CDU pump failover recovery time | s | 10 (illustrative) | CDU manufacturer data; verify by test |
| Minimum TCS flow per rack | l/min | OEM-specified | Platform OEM specification |
| CDU group redundancy | configuration | N+1 (illustrative) | Capability profile |

**Minimum evidence**

- CDU test records at design load
- Pump failover test traces (flow, pressure, TCS supply temperature)
- CDU-to-rack connection register
- CDU configuration export (pump control mode, setpoints)
- Filter differential-pressure trend

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE; TRANSITION |
| periodCoverage | Test within 12 months plus 3 months of telemetry |
| independence | Failover test witnessed by a party independent of the CDU vendor |
| mandatoryItems | Design-load test record; Pump failover test traces |
| acceptableAlternatives | Operational evidence of an unplanned pump failure with full telemetry, analysed against criteria |
| unknownEffect | US4 Critical: CG-06 UNKNOWN for racks served by untested CDU groups |
| reassessmentTriggers | Racks added to CDU group; CDU firmware or control change; Pump replacement; Filter change to finer rating |

**Assessment methods.** TEST, DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Select CDU groups serving the highest-load racks.
2. Review design-load and failover test records against criteria.
3. Reconcile rack connection register with demonstrated capacity.
4. Review CDU configuration and filter ΔP trends.
5. Record untested groups as UNKNOWN.

**Gate mappings.** CG-06 Thermal continuity (CRITICAL); CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies to all CDUs serving in-scope IT, including in-rack, in-row and facility-scale CDUs and immersion-tank heat exchangers.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, TRANSITION

**Failure modes addressed.** Duty pump failure without successful standby start; CDU overloaded by rack additions; Strainer fouling reducing flow; Liquid-to-air CDU starved by high hall temperature

**Testing safety.** Pump failover tests on live loops risk thermal trips of production IT. Requires a permit-to-work and method statement approved by the site authorising engineer, AI platform operator agreement and an abort criterion based on TCS supply temperature.

**UNKNOWN rule.** If no failover test exists for a CDU group, record U1 UNKNOWN; design data alone cannot support the EFFECTIVENESS claim.

**Ontology classes.** AssetInstance, CapacityAssertion, TestRecord, FaultDomain · **Related controls.** MCF-THM-009, MCF-THM-011, MCF-THM-021, MCF-THM-002

**Informative references.** ASHRAE TC 9.9 Liquid Cooling Guidelines for Datacom Equipment Centers; Open Compute Project Advanced Cooling Solutions guidance (cold plate, CDU, immersion); ASHRAE Guideline 0 (the commissioning process)

### MCF-THM-011

**Secondary Loop Integrity** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure the technology cooling system (secondary loop) maintains pressure, flow, temperature and fluid inventory within limits, is pressure-tested, and has no unmanaged single points of failure between CDU and cold plate.

**Requirement.** The facility operator shall monitor TCS supply and return temperature, differential pressure, flow, system pressure and make-up/fill volume continuously, shall pressure-test new and modified TCS pipework before fill, and shall investigate any unexplained make-up volume. The thermal engineering authority shall maintain a single-point-of-failure analysis of the TCS from CDU to manifold to cold plate.

**Assessment criteria**

1. TCS pressure, differential pressure, flow and supply/return temperature are monitored continuously and trends are within limits for the period.
2. Pressure tests are recorded for all new or modified TCS pipework before fill, at the specified test pressure and hold time.
3. Make-up volume is metered and any unexplained loss is investigated.
4. A single-point-of-failure analysis of the TCS path (header, manifold, hoses, valves) exists and identified points are treated.
5. Rack ΔT and flow anomalies are alarmed before OEM throttle thresholds.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Pressure test level | × maximum operating pressure | 1.5 (illustrative) | Piping code or manufacturer specification |
| Pressure test hold time | min | 30 (illustrative) | Piping code or manufacturer specification |
| Unexplained make-up volume investigation threshold | l per week per loop | 5 (illustrative) | Capability profile |

**Minimum evidence**

- TCS telemetry trends (P, ΔP, flow, T)
- Pressure-test certificates
- Make-up volume log
- TCS single-point-of-failure analysis
- Alarm schedule for TCS points

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE; RECOVERY |
| periodCoverage | Most recent 6 months of telemetry and all pressure tests since last fill |
| independence | Pressure test witnessed by a party other than the installer |
| mandatoryItems | Telemetry trends; Pressure-test certificates; Make-up log |
| acceptableAlternatives | Inventory reconciliation by expansion-tank level where make-up meters are absent |
| unknownEffect | US4 Critical: CG-06 UNKNOWN for loops with unverified integrity |
| reassessmentTriggers | Loop modification; Unexplained fluid loss; Pressure excursion; Hose or manifold replacement |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW, INSPECTION, SAMPLING

**Assessment procedure**

1. Analyse TCS telemetry for excursions and trends.
2. Sample pressure-test certificates against modification records.
3. Reconcile make-up volume log with investigations.
4. Review the single-point-of-failure analysis.
5. Inspect a sample of manifolds and hose routes.

**Gate mappings.** CG-06 Thermal continuity (CRITICAL); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to all liquid TCS loops serving in-scope IT.

**Lifecycle stages.** BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, RECOVERY

**Failure modes addressed.** Slow leak depleting inventory; Air ingress causing pump cavitation; Manifold single point of failure; Over-pressure on valve closure

**Testing safety.** Pressure testing of filled loops is hazardous; it requires an approved method statement, pressure-equipment competence and isolation from IT equipment. Assessors do not operate valves.

**UNKNOWN rule.** If make-up volume or pressure-test records are missing for modified sections, record U1 UNKNOWN for those loops.

**Ontology classes.** InfrastructureSystem, FaultDomain, Safeguard, AssetInstance · **Related controls.** MCF-THM-010, MCF-THM-012, MCF-THM-019

**Informative references.** ASHRAE TC 9.9 Liquid Cooling Guidelines for Datacom Equipment Centers; Open Compute Project Advanced Cooling Solutions guidance (cold plate, CDU, immersion); ASME B31.9 (building services piping); Pressure Equipment Directive 2014/68/EU or equivalent national pressure-equipment regulation

### MCF-THM-012

**Quick-Disconnect Management** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure quick-disconnect couplings between manifolds and IT are specified, compatible, connected, inspected and replaced under control, because they are the most frequently operated wetted joints and a common leak and flow-restriction source.

**Requirement.** The facility operator shall maintain a register of quick-disconnect coupling types and compatibility by platform, shall perform connect/disconnect only under a documented procedure by trained staff with drip containment, and shall inspect and replace couplings and seals on a defined interval or cycle count. The AI platform operator shall not install IT with couplings outside the register.

**Assessment criteria**

1. A coupling register lists types, ratings, compatible counterparts and wetted materials per platform.
2. A connect/disconnect procedure exists with drip containment, purge and post-connection leak check.
3. Staff performing connections have recorded training.
4. Sample work orders show the procedure was followed, including post-connection leak checks.
5. Couplings are inspected or replaced per interval or cycle count, and failures are trended.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Coupling inspection interval | months | 12 (illustrative) | Coupling manufacturer guidance |
| Rated connect/disconnect cycles | cycles | manufacturer-rated | Coupling manufacturer data |

**Minimum evidence**

- Coupling register
- Connect/disconnect procedure
- Training records
- Sample work orders with leak-check sign-off
- Coupling failure trend

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; TRANSITION |
| periodCoverage | Most recent 6 months of work orders |
| independence | Observation of a live connection by the assessor |
| mandatoryItems | Coupling register; Sample work orders |
| acceptableAlternatives | Witnessed demonstration on a non-production rack |
| unknownEffect | US3 Material: leak initiation risk unbounded; supports CG-06 and CG-04 evaluation |
| reassessmentTriggers | New coupling type; Coupling leak incident; Rack swap campaign |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, OBSERVATION, INQUIRY

**Assessment procedure**

1. Review register against deployed platforms.
2. Sample work orders for procedure adherence.
3. Observe a connection or disconnection where possible.
4. Review failure trend and replacement records.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING); CG-04 Life safety and hazardous energy (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies where IT is connected to TCS manifolds by quick-disconnect couplings. Not applicable to hard-piped cold-plate systems.

**Lifecycle stages.** BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, TRANSITION

**Failure modes addressed.** Incompatible couplings mated; Seal degradation causing drip leak; Partial engagement restricting flow; Coolant spill onto energised equipment

**Testing safety.** Observation only; connections are made by trained site staff under procedure. Spill onto energised equipment is an electrical hazard: the procedure must require drip containment.

**UNKNOWN rule.** If the coupling register does not cover a deployed platform, record U1 UNKNOWN for that platform.

**Ontology classes.** AssetInstance, Interface, Hazard, Safeguard · **Related controls.** MCF-THM-011, MCF-THM-019, MCF-CMP-021

**Informative references.** Open Compute Project Advanced Cooling Solutions guidance (cold plate, CDU, immersion); ASHRAE TC 9.9 Liquid Cooling Guidelines for Datacom Equipment Centers

## THM-04 Heat rejection and water systems

### MCF-THM-013

**Chiller Capacity** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Demonstrate that chillers (where present) deliver required capacity at design condenser conditions with declared redundancy, restart quickly after power interruption, and that refrigerant hazards are controlled.

**Requirement.** The facility operator shall demonstrate chiller capacity at design condenser conditions with the declared redundancy, shall evidence restart-to-capacity time after power interruption, and shall maintain refrigerant inventory, leak detection, machinery-room ventilation and safety classification records in accordance with the applicable refrigeration safety standard.

**Assessment criteria**

1. Chiller capacity at design condenser conditions with N−1 meets design load.
2. Restart-to-capacity time after power interruption is evidenced by test and is within the ride-through window.
3. Refrigerant type, charge, safety class and machinery-room requirements are documented.
4. Refrigerant leak detection and ventilation are installed and functionally tested.
5. Refrigerant leak and charge records meet applicable regulatory requirements.
6. Chiller sequencing logic is documented and tested for failure of the lead chiller.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Chiller restart-to-capacity | s | 300 (illustrative) | Manufacturer rapid-restart data |
| Chiller redundancy | configuration | N+1 (illustrative) | Capability profile |

**Minimum evidence**

- Chiller performance test or commissioning data at design conditions
- Restart test record
- Refrigerant register and safety classification
- Refrigerant detector test records
- Sequencing logic description and test

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E1; E5 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY; RECOVERY |
| periodCoverage | Tests within 12 months; refrigerant records for 12 months |
| independence | Refrigerant safety inspection by a certified refrigeration engineer |
| mandatoryItems | Capacity test at design conditions; Restart test; Refrigerant register |
| acceptableAlternatives | Manufacturer factory witness test plus site performance verification at partial load |
| unknownEffect | US4 Critical: CG-06 UNKNOWN for chilled-water-dependent paths; refrigerant safety gaps escalated to CG-04 |
| reassessmentTriggers | Chiller replacement or refrigerant change; Restart failure; Refrigerant leak |

**Assessment methods.** TEST, DOCUMENT_REVIEW, INSPECTION, ANALYSIS

**Assessment procedure**

1. Review capacity and restart test records.
2. Compare restart time with ride-through analysis in MCF-THM-003.
3. Inspect refrigerant detection and machinery-room provisions.
4. Review sequencing tests and refrigerant records.

**Gate mappings.** CG-06 Thermal continuity (CRITICAL); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies where mechanical refrigeration is in the heat-removal path. Not applicable to chiller-less designs (for example W32+ with dry coolers only), provided MCF-THM-004 shows dry-cooler capacity at design ambient.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY, RECOVERY

**Failure modes addressed.** Chiller fails to restart after transfer; Lead chiller failure without sequencing to standby; Refrigerant leak in occupied space; Capacity loss at high condenser temperature

**Testing safety.** Restart tests interrupt chilled water; Requires a permit-to-work and method statement approved by the site authorising engineer and thermal-storage or redundancy cover. Refrigerant work requires certified personnel.

**UNKNOWN rule.** If restart-to-capacity has not been tested, record U1 UNKNOWN; this carries into MCF-THM-003 ride-through.

**Ontology classes.** AssetInstance, CapacityAssertion, Hazard, TestRecord · **Related controls.** MCF-THM-003, MCF-THM-004, MCF-THM-024

**Informative references.** ASHRAE Standard 15 / ISO 5149 / EN 378 (refrigeration system safety); EU F-gas Regulation or applicable refrigerant regulation; ASHRAE Guideline 0 (the commissioning process); Uptime Institute Tier Standard: Topology

### MCF-THM-014

**Cooling Tower or Dry Cooler** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure final heat-rejection equipment (cooling towers, adiabatic or dry coolers) operates at the required capacity, is protected against fouling, freezing, recirculation and fan or spray failures, and is maintained to preserve capacity.

**Requirement.** The facility operator shall operate and maintain heat-rejection units to preserve capacity at design ambient, shall monitor approach temperature and fan/pump status per unit, shall protect against freezing and hot-air recirculation, and shall record fouling and coil-cleaning interventions. Where evaporative or adiabatic systems are used, the facility operator shall implement MCF-THM-018 water treatment.

**Assessment criteria**

1. Approach temperature per unit is trended and units with degraded approach are investigated.
2. Fan and pump status is monitored per unit with alarms.
3. Freeze protection (glycol concentration, heat tracing, drain-down) is in place where ambient can fall below freezing.
4. Layout or wind analysis addresses hot-air recirculation between units and from adjacent sources.
5. Coil cleaning or tower maintenance follows schedule.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Approach temperature degradation threshold | K above commissioned | 2 (illustrative) | Capability profile |

**Minimum evidence**

- Approach temperature trends
- Unit status alarms
- Freeze-protection records
- Recirculation study or observation
- Coil-cleaning and tower maintenance records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | 12 months including summer and winter |
| independence | Thermal imaging or independent recirculation survey |
| mandatoryItems | Approach temperature trends; Maintenance records |
| acceptableAlternatives | Seasonal performance test by the manufacturer |
| unknownEffect | US3 Material: heat-rejection capacity condition recorded; CG-06 supporting |
| reassessmentTriggers | New adjacent heat source; Unit failure; Fouling event |

**Assessment methods.** ANALYSIS, INSPECTION, DOCUMENT_REVIEW

**Assessment procedure**

1. Analyse approach temperature by unit.
2. Inspect units for fouling, damage and recirculation paths.
3. Review freeze protection.
4. Review maintenance compliance.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to all final heat-rejection equipment in the boundary.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Hot-air recirculation raising entering temperature; Coil fouling; Freeze damage; Fan failure at peak ambient

**Testing safety.** Roof and plant-yard inspection requires working-at-height controls; evaporative towers require respiratory precautions under the legionella risk assessment.

**UNKNOWN rule.** If per-unit monitoring is absent, record U5 UNKNOWN for unit-level degradation.

**Ontology classes.** AssetInstance, InfrastructureSystem, Hazard · **Related controls.** MCF-THM-004, MCF-THM-016, MCF-THM-018

**Informative references.** ASHRAE Standard 169 / ASHRAE Handbook Fundamentals (climatic design conditions); ASHRAE Standard 188 (legionellosis risk management for building water systems); EN 50600-2-3 / ISO/IEC 22237-3 (data centre environmental control)

### MCF-THM-015

**Water Continuity** · PREVENTIVE · claim type RESILIENCE · required AL5

**Objective.** Ensure evaporative and adiabatic heat rejection, and loop make-up, can continue through loss or restriction of mains water supply for the declared autonomy period.

**Requirement.** The facility owner shall determine water consumption at design ambient and peak load, shall provide on-site storage or alternative supply for the declared water autonomy, and shall document the dependency on the water utility, including restriction scenarios and drought orders. The facility operator shall test the switchover to stored or alternative water and shall monitor stored volume.

**Assessment criteria**

1. Peak water consumption at design ambient and load is calculated.
2. On-site storage or alternative supply provides the declared autonomy at peak consumption.
3. Switchover to stored water is tested and recorded.
4. Stored volume is monitored with low-level alarms.
5. The water utility dependency, including restriction scenarios, is documented and owned.
6. A fallback mode (for example dry operation with reduced capacity) is defined with its capacity impact on IT load.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Water autonomy at peak consumption | h | 48 (illustrative) | Capability profile; utility risk assessment |
| Peak water consumption | m³/h | site-calculated | Design calculation at design wet-bulb and load |

**Minimum evidence**

- Water consumption calculation
- Storage capacity data
- Switchover test record
- Level telemetry and alarms
- Utility dependency record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY |
| periodCoverage | Test within 12 months; 12 months level data |
| independence | Utility restriction scenario reviewed with the water utility or an independent hydrologist |
| mandatoryItems | Consumption calculation; Switchover test |
| acceptableAlternatives | Contracted tanker supply with tested delivery and connection |
| unknownEffect | US4 Critical: CG-06 UNKNOWN for water-dependent heat rejection under EMERGENCY states |
| reassessmentTriggers | Drought order or utility restriction; Change to evaporative capacity; Storage modification |

**Assessment methods.** ANALYSIS, TEST, DOCUMENT_REVIEW, INQUIRY

**Assessment procedure**

1. Recalculate peak consumption.
2. Compare with storage autonomy.
3. Review switchover test.
4. Review dependency ownership and fallback mode.

**Gate mappings.** CG-06 Thermal continuity (CRITICAL); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies where heat rejection or loop make-up depends on water supply. Not applicable to closed-loop dry heat rejection with no evaporative component, except for loop make-up which is covered by MCF-THM-011.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY

**Failure modes addressed.** Mains supply loss exhausting storage; Drought restriction curtailing evaporative cooling; Switchover valve failure

**Testing safety.** Switchover tests follow the site permit-to-work and must not drain storage below the minimum safe level.

**UNKNOWN rule.** If peak consumption is not calculated, record U1 UNKNOWN; autonomy cannot be asserted.

**Ontology classes.** Dependency, Resource, CapacityAssertion, FailureScenario · **Related controls.** MCF-THM-014, MCF-THM-016, MCF-DEP-009, MCF-ENV-011, MCF-ENV-022

**Informative references.** ASHRAE Standard 188 (legionellosis risk management for building water systems); EN 50600-2-3 / ISO/IEC 22237-3 (data centre environmental control); AIDCF-004 (Threat, Hazard and Failure Model)

### MCF-THM-016

**Heat-Rejection Dependency** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Make explicit every dependency of the heat-removal path on external or shared resources (water, power, controls, district systems, shared plant with other tenants) and the common modes that could remove several redundant trains at once.

**Requirement.** The thermal engineering authority shall maintain a heat-rejection dependency map from IT heat source to final heat sink, identifying shared headers, common controllers, common power boards, shared water supplies, third-party plant and heat-reuse interfaces, and shall record the treatment and owner of each common mode. The facility owner shall ensure heat-reuse or district-energy interfaces cannot reduce heat-rejection capacity below design load.

**Assessment criteria**

1. A dependency map exists from rack to final heat sink for each redundant train.
2. Common-mode points (shared header, controller, board, water feed) are listed with treatment and owner.
3. Third-party or shared plant is identified with contractual service levels.
4. Heat-reuse or district interfaces have a defined fall-back that preserves heat rejection when the external heat sink is unavailable.
5. The map is reconciled to the current P&ID.

**Minimum evidence**

- Heat-rejection dependency map
- Common-mode register
- Third-party service agreements
- Heat-reuse interface design and fall-back

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E2; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY |
| periodCoverage | Current version |
| independence | Review by an engineer independent of the designer |
| mandatoryItems | Dependency map; Common-mode register |
| acceptableAlternatives | Fault tree for loss of heat rejection covering the same elements |
| unknownEffect | US3 Material: hidden common mode possible; referred to CG-03 and CG-09 evaluation |
| reassessmentTriggers | New shared plant; Heat-reuse connection; Tenant change in shared facility |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION

**Assessment procedure**

1. Obtain dependency map and P&ID.
2. Trace each train for shared elements.
3. Review treatment of each common mode.
4. Review heat-reuse fall-back.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING); CG-09 Failure containment (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to all heat-rejection paths in scope.

**Lifecycle stages.** PLAN, DESIGN, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY

**Failure modes addressed.** Shared header defeating redundancy; District heat sink unavailable; Common controller failure; Tenant plant change

**Testing safety.** Desk-based review of dependency records and P&IDs; site walk-downs to confirm shared elements are visual only.

**UNKNOWN rule.** Any unmapped shared element discovered during inspection is recorded as a U10 dependency UNKNOWN and escalated to CG-03.

**Ontology classes.** Dependency, FaultDomain, Interface, InfrastructureSystem · **Related controls.** MCF-THM-015, MCF-THM-003, MCF-DEP-005, MCF-DEP-006

**Informative references.** Uptime Institute Tier Standard: Topology; AIDCF-004 (Threat, Hazard and Failure Model); AIDCF-013 (AI Data Centre Assurance Reference Architecture)

## THM-05 Fluid quality and leak management

### MCF-THM-017

**Coolant Compatibility** · PREVENTIVE · claim type DESIGN · required AL2

**Objective.** Ensure every coolant and immersion fluid is compatible with all wetted materials and IT components, is safe to handle, and that its hazards (toxicity, flammability, environmental, pressure) are identified and controlled.

**Requirement.** The thermal engineering authority shall specify each coolant (for example propylene-glycol solution, treated water, dielectric immersion fluid) with its composition, inhibitor package, approved wetted materials and OEM approval, and shall obtain and act upon the safety data sheet. The facility owner shall ensure fluid handling, storage, spill response and disposal arrangements are in place and accepted by the site safety authority.

**Assessment criteria**

1. Each coolant has a specification with composition, inhibitor package and OEM approval for every platform it contacts.
2. A wetted-materials list exists for each loop and is checked against the coolant's compatibility data.
3. Mixing of incompatible fluids is prevented by labelling, dedicated fill equipment and procedure.
4. Safety data sheets are held and hazards are reflected in handling, PPE, storage and spill procedures.
5. For immersion fluids, flammability, material compatibility with IT components and long-term fluid degradation are assessed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Glycol concentration | % by volume | OEM-specified (illustrative 25) | Platform OEM coolant specification; OCP propylene-glycol guidance |

**Minimum evidence**

- Coolant specification per loop
- Wetted-materials list
- OEM approval letters
- Safety data sheets
- Handling and spill procedures

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Current specification |
| independence | Compatibility confirmed by OEM or fluid supplier technical service |
| mandatoryItems | Coolant specification; Safety data sheets |
| acceptableAlternatives | Laboratory compatibility test report for non-standard materials |
| unknownEffect | US3 Material: corrosion or fluid-hazard risk unbounded; CG-04 supporting evaluation |
| reassessmentTriggers | Coolant supplier change; New wetted material; Immersion fluid change |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY, INSPECTION

**Assessment procedure**

1. Review coolant specifications against OEM requirements.
2. Cross-check wetted-materials list.
3. Inspect fluid storage and labelling.
4. Review handling procedures against the SDS.

**Gate mappings.** CG-04 Life safety and hazardous energy (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to all liquid and immersion cooling fluids in scope.

**Lifecycle stages.** DESIGN, BUILD, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Galvanic corrosion from mixed metals; Inhibitor package incompatible with wetted materials; Fluid mixing; Dielectric fluid incompatibility with cable jackets

**Testing safety.** Fluid sampling follows the SDS and site PPE requirements.

**UNKNOWN rule.** If OEM approval for a coolant cannot be shown, record UNKNOWN and treat the loop's integrity claims as conditioned.

**Ontology classes.** Resource, Hazard, Safeguard, Interface · **Related controls.** MCF-THM-018, MCF-THM-009, MCF-THM-020, MCF-ENV-018

**Informative references.** ASHRAE TC 9.9 Liquid Cooling Guidelines for Datacom Equipment Centers; Open Compute Project Advanced Cooling Solutions guidance (cold plate, CDU, immersion); Regulation (EC) No 1272/2008 (CLP) / GHS safety data sheets

### MCF-THM-018

**Water Quality** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Maintain the chemistry, cleanliness and microbiological quality of TCS, FWS and condenser water so that cold plates do not foul, corrosion is controlled, and evaporative systems do not present a legionella risk to people.

**Requirement.** The facility operator shall implement a water-quality programme with sampling frequencies and limits for each loop (pH, conductivity, inhibitor level, glycol concentration, suspended solids, microbiological counts), shall maintain filtration to the OEM rating, and shall act on out-of-limit results within defined times. Where evaporative cooling towers or adiabatic systems exist, the facility owner shall maintain a legionella risk assessment and written control scheme under the applicable regulation, reviewed by a competent person.

**Assessment criteria**

1. Sampling schedule and limits exist for each loop and are derived from OEM and fluid-supplier requirements.
2. Sample results for the period are within limits or exceedances were corrected within the defined time.
3. Filter differential pressure and replacement records show filtration maintained.
4. A current legionella risk assessment and written scheme exist for evaporative systems, with competent-person review.
5. Microbiological testing results for evaporative systems are recorded and actioned.
6. Laboratory analyses use an accredited or OEM-approved laboratory.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| TCS sampling frequency | per month | 1 (illustrative) | OEM/fluid supplier guidance |
| Out-of-limit corrective-action time | days | 7 (illustrative) | Capability profile |
| Legionella risk assessment review interval | months | 24 or on change (illustrative) | Applicable national regulation/ACOP |

**Minimum evidence**

- Water-quality programme and limits
- Sample results
- Filter records
- Legionella risk assessment and written scheme
- Microbiological test results

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E3; E4; E5 |
| optionalClasses | E2 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | 12 months of results |
| independence | Accredited laboratory analysis; legionella scheme reviewed by an independent competent person |
| mandatoryItems | Sample results; Legionella risk assessment (where evaporative systems exist) |
| acceptableAlternatives | Inline monitoring of conductivity/pH with periodic laboratory confirmation |
| unknownEffect | US4 Critical where evaporative systems exist (CG-04 life safety); otherwise US3 Material for CG-06 |
| reassessmentTriggers | Out-of-limit result; Positive legionella result; Change of treatment supplier; System modification |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, SAMPLING, INSPECTION

**Assessment procedure**

1. Obtain programme and limits.
2. Analyse 12 months of results for exceedances and corrective actions.
3. Review filter records.
4. Review legionella risk assessment, scheme and results.
5. Inspect a sample point and dosing equipment.

**Gate mappings.** CG-04 Life safety and hazardous energy (CRITICAL); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to all water and water-glycol loops in scope. Legionella criteria apply only where evaporative or aerosol-generating systems exist.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Cold-plate microchannel fouling; Biofilm and microbiologically influenced corrosion; Legionella proliferation in cooling towers; Inhibitor depletion

**Testing safety.** Sampling of evaporative systems requires respiratory protection per the legionella risk assessment. Chemical dosing equipment is operated only by the water-treatment contractor.

**UNKNOWN rule.** If no microbiological results exist for an evaporative system, record US4 UNKNOWN against CG-04; the control cannot be CONFORMING.

**Ontology classes.** Resource, Hazard, Safeguard, EvidenceObject · **Related controls.** MCF-THM-017, MCF-THM-014, MCF-ENV-009

**Informative references.** ASHRAE Standard 188 (legionellosis risk management for building water systems); HSE ACOP L8 (control of legionella bacteria in water systems, UK); ASHRAE TC 9.9 Liquid Cooling Guidelines for Datacom Equipment Centers; Open Compute Project Advanced Cooling Solutions guidance (cold plate, CDU, immersion)

### MCF-THM-019

**Leak Detection** · DETECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure liquid leaks from TCS, FWS, rear-door heat exchangers and immersion tanks are detected quickly and located precisely enough to isolate the right section before liquid reaches energised equipment or spreads beyond its fault domain.

**Requirement.** The facility operator shall install leak detection (rope/cable sensors, spot sensors, CDU and rack-level detection, flow/pressure-based detection) covering every wetted zone above or adjacent to IT and electrical equipment, shall route alarms to a staffed function with locational information, and shall functionally test detection at defined intervals. The thermal engineering authority shall define detection coverage and response time requirements per zone.

**Assessment criteria**

1. A coverage map shows detection for every zone where liquid is present above, within or adjacent to IT or electrical equipment.
2. Functional tests (wet test or manufacturer test method) are recorded for sampled sensors within the interval.
3. Alarms carry zone/location and reach a staffed function; response time is measured.
4. Detection is supplemented by flow/pressure or make-up anomaly detection for slow leaks.
5. False-alarm rates are tracked and do not lead to disabled sensors.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Leak detection functional test interval | months | 12 (illustrative) | Manufacturer guidance; capability profile |
| Alarm-to-acknowledgement time | min | 5 (illustrative) | Capability profile |

**Minimum evidence**

- Leak detection coverage map
- Functional test records
- Alarm log with response times
- Slow-leak analytics configuration
- Disabled-sensor register

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E1; E5; E7 |
| qualityFloor | P4 F4 C3 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | 12 months of alarm records; tests within interval |
| independence | Assessor-witnessed functional test of sampled sensors |
| mandatoryItems | Coverage map; Functional test records |
| acceptableAlternatives | Incident evidence of real leak detection with full alarm timeline |
| unknownEffect | US3 Material: leak detection effectiveness uncertain; CG-09 and CG-04 supporting evaluation |
| reassessmentTriggers | New wetted zone; Sensor disabled; Undetected leak incident |

**Assessment methods.** TEST, INSPECTION, ANALYSIS, DOCUMENT_REVIEW

**Assessment procedure**

1. Review coverage map against the P&ID and room layout.
2. Witness or review functional tests on sampled sensors.
3. Analyse alarm log for response times.
4. Check disabled-sensor register.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING); CG-09 Failure containment (SUPPORTING); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies wherever liquid cooling or water piping is present in or above IT or electrical spaces.

**Lifecycle stages.** BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Leak in an uncovered zone; Sensor disabled after false alarms; Alarm without location; Slow leak below sensor threshold

**Testing safety.** Wet tests use small water volumes away from energised equipment, under permit, with the IT operator informed.

**UNKNOWN rule.** Zones with no functional-test record within interval are recorded as U3 stale UNKNOWN.

**Ontology classes.** Safeguard, AssetInstance, FailureScenario · **Related controls.** MCF-THM-020, MCF-THM-011, MCF-OPS-013, MCF-PHY-011

**Informative references.** ASHRAE TC 9.9 Liquid Cooling Guidelines for Datacom Equipment Centers; Open Compute Project Advanced Cooling Solutions guidance (cold plate, CDU, immersion); EN 50600-2-3 / ISO/IEC 22237-3 (data centre environmental control)

### MCF-THM-020

**Isolation and Drainage** · CORRECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure a detected leak can be isolated to the smallest practicable section, the released liquid is contained and drained away from energised equipment, and the remaining cooling capacity is preserved, so that a leak remains within its fault domain.

**Requirement.** The thermal engineering authority shall design isolation valves, drip trays, bunding and drainage so that a leak at any credible point can be isolated to a defined fault domain and drained without reaching electrical equipment outside that domain. The facility operator shall maintain isolation procedures, exercise valves, and demonstrate isolation of a representative section while adjacent sections continue cooling.

**Assessment criteria**

1. Isolation points are defined so that each credible leak location can be isolated within a defined fault domain.
2. Automatic isolation (where used) is linked to leak detection and tested.
3. Drip trays, bunding or floor drainage direct liquid away from electrical equipment and are inspected.
4. Valve exercise records show isolation valves operate and seal.
5. A representative isolation test showed adjacent fault domains maintained cooling.
6. Spill volumes per fault domain are bounded by design.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum release volume per isolated section | l | design-specific (illustrative 50) | Design authority |
| Valve exercise interval | months | 12 (illustrative) | Manufacturer guidance |

**Minimum evidence**

- Isolation design and fault-domain definition
- Automatic isolation test record
- Drainage and containment inspection
- Valve exercise records
- Representative isolation test

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5 |
| qualityFloor | P4 F4 C3 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY; MAINTENANCE |
| periodCoverage | Tests within 12 months |
| independence | Isolation test witnessed by a party independent of the maintenance contractor |
| mandatoryItems | Isolation design; Representative isolation test |
| acceptableAlternatives | Documented real leak incident showing isolation and containment within fault domain |
| unknownEffect | US4 Critical: CG-09 UNKNOWN for liquid-leak containment |
| reassessmentTriggers | Pipework change; Valve failure; Leak propagating beyond domain |

**Assessment methods.** TEST, INSPECTION, DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Review isolation design against P&ID.
2. Inspect drip trays and drainage.
3. Review valve exercise and automatic isolation tests.
4. Review representative isolation test results.
5. Assess release volume bounds.

**Gate mappings.** CG-09 Failure containment (CRITICAL); CG-04 Life safety and hazardous energy (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies wherever liquid cooling is present in IT space.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE · **Operating states.** NORMAL, DEGRADED, EMERGENCY, MAINTENANCE

**Failure modes addressed.** Isolation valve seized; Isolation of a leak removes cooling from a larger domain than intended; Liquid tracks to electrical busway; Automatic isolation fails to close

**Testing safety.** Isolation tests reduce cooling to the isolated section; Requires a permit-to-work and method statement approved by the site authorising engineer, with the affected IT drained or protected.

**UNKNOWN rule.** If no isolation test exists, record U1 UNKNOWN; design review alone supports DESIGN, not EFFECTIVENESS.

**Ontology classes.** FaultDomain, Safeguard, AssetInstance, TestRecord · **Related controls.** MCF-THM-019, MCF-THM-011, MCF-RES-006, MCF-RES-008, MCF-PHY-011

**Informative references.** ASHRAE TC 9.9 Liquid Cooling Guidelines for Datacom Equipment Centers; Open Compute Project Advanced Cooling Solutions guidance (cold plate, CDU, immersion); ASME B31.9 (building services piping)

## THM-06 Thermal control, maintenance and recovery

### MCF-THM-021

**Control Stability** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure cooling controls (CDU controllers, BMS sequences, chiller plant managers, pump and valve PID loops) remain stable under rapid AI load swings, fail to a safe cooling state on controller or network loss, and cannot be changed without control.

**Requirement.** The controls engineering authority shall document control sequences and fail-safe states for each cooling controller, shall demonstrate stability of temperature and pressure loops under step load changes representative of synchronous training, and shall demonstrate that loss of controller, sensor or controls network leaves pumps running and valves in a safe position. The facility operator shall manage controller configuration under change control with version-controlled backups.

**Assessment criteria**

1. Sequences of operation and fail-safe states are documented per controller.
2. Step-load test shows TCS supply temperature and pressure settle within the declared band and time without sustained oscillation.
3. Loss-of-controller and loss-of-network tests show pumps continue and valves fail to the safe state.
4. Controller configurations are backed up, version-controlled and reconciled to the approved baseline.
5. Remote write access to cooling controllers is restricted and logged.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Settling time after load step | s | 120 (illustrative) | Controls design; capability profile |
| Temperature control band | K | ±1 (illustrative) | Controls design |

**Minimum evidence**

- Sequences of operation
- Step-load test traces
- Fail-safe test record
- Configuration baseline and backup
- Access log for controller changes

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5 |
| qualityFloor | P4 F4 C3 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; TRANSITION; FAILED |
| periodCoverage | Tests within 12 months; 3 months control trends |
| independence | Fail-safe test witnessed by an independent controls engineer |
| mandatoryItems | Fail-safe test; Step-load test; Configuration baseline |
| acceptableAlternatives | Recorded production load step with full telemetry analysed against criteria |
| unknownEffect | US4 Critical: CG-07 UNKNOWN for cooling controls |
| reassessmentTriggers | Controller firmware or logic change; Oscillation event; New load profile |

**Assessment methods.** TEST, DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Review sequences and fail-safe definitions.
2. Review step-load and fail-safe test traces.
3. Reconcile running configuration with baseline.
4. Review access controls and logs.

**Gate mappings.** CG-07 Critical control-system integrity (CRITICAL); CG-06 Thermal continuity (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to all automated controls in the heat-removal path, including vendor CDU controllers.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, TRANSITION, FAILED

**Failure modes addressed.** PID oscillation under synchronous load; Controller failure stopping pumps; Valve fails closed on network loss; Unauthorised setpoint change

**Testing safety.** Fail-safe tests on live systems are hazardous; Requires a permit-to-work and method statement approved by the site authorising engineer, controls specialist on site and manual override available.

**UNKNOWN rule.** If fail-safe behaviour is undocumented or untested, record US4 UNKNOWN against CG-07.

**Ontology classes.** InfrastructureSystem, Safeguard, Interface, TestRecord · **Related controls.** MCF-THM-010, MCF-THM-022, MCF-SEC-005, MCF-OPS-017

**Informative references.** IEC 62443 series (industrial automation and control system security); IEC 61131-3 (programmable controller languages); ASHRAE Guideline 0 (the commissioning process)

### MCF-THM-022

**Sensor Trust** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure the sensors that drive cooling control and alarming (temperature, pressure, flow, leak, level) are accurate, calibrated, redundant where control-critical, and that implausible or failed readings are detected before they mislead control or operators.

**Requirement.** The facility operator shall identify control-critical sensors, shall calibrate them at defined intervals, shall provide redundancy or plausibility checks (cross-sensor comparison, rate-of-change, stuck-value detection) for control-critical points, and shall configure controllers to a safe default on sensor failure.

**Assessment criteria**

1. Control-critical sensors are identified in a register.
2. Calibration records exist within interval for sampled sensors.
3. Control-critical points have redundant sensors or plausibility logic.
4. Controllers default to safe action on sensor failure, verified by documentation or test.
5. Sensor faults are alarmed and tracked.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Control-critical sensor calibration interval | months | 12 (illustrative) | Instrument manufacturer / metrology policy |
| Redundant-sensor divergence alarm | K | 1.5 (illustrative) | Capability profile |

**Minimum evidence**

- Control-critical sensor register
- Calibration certificates for control-critical temperature, pressure and flow sensors
- Plausibility logic description
- Sensor-fault alarm log

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | 12 months of calibration and fault records |
| independence | Assessor spot check with reference instrument |
| mandatoryItems | Sensor register; Calibration records |
| acceptableAlternatives | Cross-comparison analysis of redundant sensors over the period |
| unknownEffect | US3 Material: telemetry reliability reduced; dependent operating claims capped at CONF-2 |
| reassessmentTriggers | Sensor replacement; Control incident traced to sensor; Calibration overdue |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, ANALYSIS, REPERFORMANCE

**Assessment procedure**

1. Review register.
2. Sample calibration certificates.
3. Review plausibility logic.
4. Analyse sensor-fault log.
5. Spot-check readings.

**Gate mappings.** CG-07 Critical control-system integrity (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to sensors used for cooling control or alarming of in-scope systems.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Drifted sensor causing undercooling; Stuck flow meter masking flow loss; Single sensor failure driving valve closed

**Testing safety.** Non-intrusive spot checks only.

**UNKNOWN rule.** If a control-critical sensor has no calibration record, treat its data as unverified (U6) and record UNKNOWN against controls relying on it.

**Ontology classes.** AssetInstance, Safeguard, EvidenceObject · **Related controls.** MCF-THM-021, MCF-THM-008, MCF-OPS-011

**Informative references.** IEC 62443 series (industrial automation and control system security); ASHRAE TC 9.9 Liquid Cooling Guidelines for Datacom Equipment Centers; ASHRAE TC 9.9 Thermal Guidelines for Data Processing Environments

### MCF-THM-023

**Maintenance States** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure planned maintenance on cooling plant (CDU servicing, filter changes, valve replacement, chiller overhaul, loop drain-down) is carried out without unplanned loss of cooling, with declared residual redundancy and safe isolation of pressurised fluid systems.

**Requirement.** The facility operator shall plan cooling maintenance with a documented method statement stating residual capacity and redundancy during the work, required IT load limits, isolation and lock-out points, and back-out steps; shall coordinate with the AI platform operator where IT load must be reduced; and shall record post-maintenance return-to-service checks.

**Assessment criteria**

1. Method statements for sampled cooling work state residual capacity and redundancy.
2. IT load limits during maintenance are agreed with the AI platform operator where required.
3. Isolation and lock-out of pressurised and energised systems are recorded.
4. Post-maintenance return-to-service checks (flow, pressure, temperature, leak check) are recorded.
5. Maintenance-induced incidents are analysed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Minimum residual redundancy during maintenance | configuration | N (illustrative) | Capability profile; risk acceptance |

**Minimum evidence**

- Method statements
- Load-limit agreements
- Isolation records
- Return-to-service checks
- Incident analyses

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | MAINTENANCE; TRANSITION; NORMAL |
| periodCoverage | Most recent 6 months of cooling maintenance |
| independence | Observation of a maintenance activity by the assessor |
| mandatoryItems | Method statements; Return-to-service checks |
| acceptableAlternatives | Computerised maintenance management system records with embedded checklists |
| unknownEffect | US3 Material: maintenance-state continuity uncertain; CG-06 and CG-14 supporting |
| reassessmentTriggers | Maintenance-induced incident; New maintenance contractor; Plant change |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, OBSERVATION, INQUIRY

**Assessment procedure**

1. Sample method statements.
2. Check residual capacity statements against N−1 analysis.
3. Review isolation and return-to-service records.
4. Observe a maintenance activity where possible.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING); CG-14 Change control (SUPPORTING); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to all planned work on in-scope cooling systems.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** MAINTENANCE, TRANSITION, NORMAL

**Failure modes addressed.** Maintenance removes the redundant unit while another is degraded; Air trapped after drain-down; Unsafe isolation of pressurised loop; Return to service without leak check

**Testing safety.** Observation only; assessors do not take part in isolation.

**UNKNOWN rule.** If residual capacity is not stated on method statements, record a Finding; if records are missing, record U1 UNKNOWN.

**Ontology classes.** OperatingState, Safeguard, Action · **Related controls.** MCF-THM-003, MCF-OPS-006, MCF-OPS-007, MCF-OPS-008

**Informative references.** ASHRAE Guideline 0 (the commissioning process); Uptime Institute Tier Standard: Topology; EN 50600-2-3 / ISO/IEC 22237-3 (data centre environmental control)

### MCF-THM-024

**Thermal Recovery** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure that after loss of cooling or power, the heat-removal path is restored in the right order (power, controls, pumps, heat rejection, CDUs) and IT load is readmitted in steps that do not exceed recovering capacity or trigger repeated thermal trips.

**Requirement.** The facility operator shall maintain a thermal recovery procedure defining restart sequence, prerequisites, hold points, verification criteria (flow, TCS supply temperature, leak checks) and staged IT readmission limits agreed with the AI platform operator, and shall exercise it at a defined interval. The facility owner shall define the thermal recovery time objective for each fault domain.

**Assessment criteria**

1. A recovery procedure defines restart sequence, prerequisites and hold points.
2. Verification criteria for each step (flow, pressure, temperature, no leak) are defined.
3. Staged IT readmission limits are defined and agreed with the AI platform operator.
4. The procedure has been exercised (test or real event) within the interval, achieving the recovery time objective.
5. Lessons from exercises and incidents are incorporated.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Thermal recovery time objective | min | 30 (illustrative) | Capability profile |
| IT readmission step | % of fault-domain design load | 25 (illustrative) | Capability profile; recovering capacity |

**Minimum evidence**

- Thermal recovery procedure
- Recovery time objective definition
- Exercise or incident record with timeline
- Readmission agreement
- Lessons-learned record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E6; E7 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | RECOVERY; EMERGENCY; FAILED; TRANSITION |
| periodCoverage | Exercise within 12 months |
| independence | Exercise observed by a party independent of the operating shift |
| mandatoryItems | Recovery procedure; Exercise record |
| acceptableAlternatives | Real recovery event with full timeline and analysis |
| unknownEffect | US4 Critical: CG-10 UNKNOWN for thermal recovery |
| reassessmentTriggers | Plant or control change; Failed recovery; Load growth |

**Assessment methods.** SCENARIO_EXERCISE, DOCUMENT_REVIEW, ANALYSIS, INQUIRY

**Assessment procedure**

1. Review the recovery procedure and its alignment with power restoration.
2. Review the exercise timeline step by step against the recovery time objective.
3. Check readmission limits against recovering capacity.
4. Interview shift staff on hold points and verification criteria.
5. Record unachieved steps as Findings.

**Gate mappings.** CG-10 Recovery readiness (CRITICAL); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to all heat-removal paths serving in-scope IT.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** RECOVERY, EMERGENCY, FAILED, TRANSITION

**Failure modes addressed.** Pumps restarted before controls, causing pressure surge; IT readmitted too fast, causing repeat trip; Air lock after restart; No agreed readmission plan

**Testing safety.** Recovery exercises should be tabletop or on isolated sections unless a live exercise is authorised; Requires a permit-to-work and method statement approved by the site authorising engineer and AI platform operator agreement.

**UNKNOWN rule.** If no exercise or real event is recorded, record US4 UNKNOWN against CG-10.

**Ontology classes.** FailureScenario, Safeguard, TestRecord, OperatingState · **Related controls.** MCF-THM-003, MCF-CMP-023, MCF-RES-014, MCF-POW-024

**Informative references.** Uptime Institute Tier Standard: Topology; ASHRAE Guideline 0 (the commissioning process); ISO 22301 (business continuity management systems)
