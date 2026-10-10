# AIDCF-018-ENV Environmental and Resource Performance Domain Guide

## Document control

| Field | Value |
|---|---|
| Document ID | AIDCF-018-ENV |
| Title | Environmental and Resource Performance Domain Guide |
| Parent artifact | AIDCF-018 Domain Guides |
| Domain | ENV — Environmental and Resource Performance |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Control source | AIDCF-007A Canonical Master Control Registry, controls MCF-ENV-001 to MCF-ENV-024; this guide agrees exactly with the machine-readable control records |
| Depends on | AIDCF-003, AIDCF-004, AIDCF-007A, AIDCF-008, AIDCF-009, AIDCF-010, AIDCF-013, AIDCF-014 |
| Requirement prefix | DG-ENV-REQ-NNN |

### Revision history

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-10 | Initial issue: domain guide for the 24 ENV controls, gate linkage, parameters, evidence and testing-safety expectations. |

## 1 Purpose and scope

This guide explains how the ENV domain of AIDCF-007A is applied in an AIDCF assessment. The ENV domain has two faces, and both matter for AI capability:

- **Environmental conditions as a dependency of capability**: the temperature, humidity, contamination, vibration and acoustic conditions in which AI hardware must operate, and the climate and resource conditions (heat, drought, flood, water and grid availability) that the facility must withstand over its life.
- **Environmental performance as a claim about capability**: the energy, water and carbon performance (PUE, WUE, CUE, ERF, REF), the handling of hazardous materials (batteries, refrigerants, coolants, fuel, suppressants) and waste, and the traceability of reported metrics to regulators, customers and investors.

In scope: environmental operating envelopes (ENV-01); energy performance metrics and the resilience-efficiency trade-off (ENV-02); water source, quality, use and discharge (ENV-03); carbon accounting boundaries, energy attribute evidence, embodied data and reporting traceability (ENV-04); battery materials, refrigerants and coolants, fuel and suppressants, hardware and media waste (ENV-05); and climate adaptation and long-term resource constraints (ENV-06).

Out of scope, with interfaces: the design and capacity of cooling plant (THM), fire protection (PHY), battery systems in service (POW), media sanitisation methods (STO), and supplier sustainability due diligence (SUP).

This guide is informative except where a requirement carries a DG-ENV-REQ identifier.

## 2 Why this domain matters for AI capability

**Tighter coupling between environment and throughput.** Accelerators respond to inlet air or coolant temperature by throttling clock frequency before they fail. A hall that is "within allowable" may still be delivering less training throughput than the Service Outcome assumes. Measuring temperatures where equipment experiences them (rack inlet; technology cooling system supply) is therefore an outcome control, not housekeeping (MCF-ENV-001 (Temperature Control)).

**Condensation risk with liquid cooling.** Cold plates and manifolds run at coolant temperatures that may approach or fall below room dew point, especially with lower-temperature facility water or during humid weather. The margin between coolant supply temperature and dew point is a new and critical environmental parameter (MCF-ENV-002 (Humidity Control)).

**Acoustic and vibration effects.** Dense halls with high-speed fans can exceed occupational noise action values; inert-gas suppression discharge can produce sound pressure high enough to disrupt hard disk drives in storage arrays; vibration from rotating plant can degrade storage throughput (MCF-ENV-004 (Vibration and Acoustic Conditions)).

**Scale of resource demand.** AI campuses can demand hundreds of megawatts and, with evaporative heat rejection, large volumes of water. Grid capacity, water entitlements and environmental permits become long-term constraints on capability growth (MCF-ENV-024 (Long-Term Resource Constraints)) and on continuity during drought or heatwave (MCF-ENV-011 (Water Scarcity Response), MCF-ENV-021 (Heatwave Readiness)).

**Efficiency pressure can erode resilience.** UPS eco-mode, raised supply temperatures, reduced running redundant units and aggressive economiser hours each improve PUE and can each reduce ride-through or thermal margin. AIDCF requires an explicit resilience impact assessment for each (MCF-ENV-008 (Resilience-Efficiency Trade-Off)).

**Claims under scrutiny.** Regulators (for example under the EU Energy Efficiency Directive data-centre reporting scheme), customers and investors increasingly rely on reported PUE, WUE, renewable share and emissions. Metrics must be measured per the ISO/IEC 30134 family and traceable to meters (MCF-ENV-005, MCF-ENV-010, MCF-ENV-016).

**Hazardous materials at scale.** More lithium-ion, more refrigerant charge (with a shift to lower-GWP but mildly flammable A2L refrigerants), more glycol and, for immersion, dielectric fluids: each brings safety and environmental obligations (MCF-ENV-017 (Battery Materials), MCF-ENV-018 (Refrigerants and Coolants)).

## 3 Reference patterns and variants

| Pattern / variant | ENV characteristics | ENV questions that dominate |
|---|---|---|
| Air-cooled with evaporative heat rejection | High water use; good energy efficiency in dry climates | WUE; Legionella; water scarcity response |
| Air-cooled with economisation | Outdoor air exposure | Particulate and gaseous contamination; humidity control |
| Direct-to-chip liquid with dry coolers | Low water use; higher facility water temperatures; heat reuse potential | Dew point margin; heatwave capacity of dry coolers; ERF |
| Direct-to-chip with chillers | Refrigerant charge; trim cooling | Refrigerant safety and leak control; efficiency under part load |
| Immersion cooling | Dielectric fluids; very high density | Fluid handling, spills, end of life; acoustic conditions differ |
| Heat reuse to district network | Exported heat | Metered ERF; dependency of off-taker on data-centre operation |
| Colocation tenant | Provider metrics | Allocation of shared energy and water; reliance on provider data |
| Hyperscale campus | Utility-scale demand | Long-term grid and water constraints; permits; regulatory reporting |

Metric variants: PUE (ISO/IEC 30134-2) with measurement categories determined by where IT energy is metered; partial PUE for sub-systems; WUE (ISO/IEC 30134-9) for site water, with source-side water reported separately; CUE (ISO/IEC 30134-8); REF (ISO/IEC 30134-3); ERF (ISO/IEC 30134-6). Carbon accounting variants: location-based and market-based Scope 2; annual or hourly matching of energy attribute certificates.

## 4 Required functions and capability linkage

| Required Function | Implemented by | Controls |
|---|---|---|
| Maintain the environment within equipment envelopes | Sensors, environmental controls, filtration | MCF-ENV-001, MCF-ENV-002, MCF-ENV-003, MCF-ENV-004 |
| Measure and manage energy performance without eroding resilience | Meters, EPMS, energy management system | MCF-ENV-005, MCF-ENV-006, MCF-ENV-007, MCF-ENV-008 |
| Secure, measure and discharge water within limits | Water supply, treatment, meters, interceptors | MCF-ENV-009, MCF-ENV-010, MCF-ENV-011, MCF-ENV-012 |
| Account for carbon and resources traceably | Inventory methodology, registries, reporting systems | MCF-ENV-013, MCF-ENV-014, MCF-ENV-015, MCF-ENV-016 |
| Control hazardous materials and waste | Inventories, storage, detection, contractors | MCF-ENV-017, MCF-ENV-018, MCF-ENV-019, MCF-ENV-020 |
| Withstand climate extremes and resource limits over life | Adaptation plans, procedures, registers | MCF-ENV-021, MCF-ENV-022, MCF-ENV-023, MCF-ENV-024 |

Capability linkage: environmental conditions link directly to performance Service Outcomes (throttling) and to integrity outcomes (corrosion, condensation, acoustic disruption of storage). Resource continuity links to availability outcomes during heat and drought. Performance claims link to stakeholder obligations captured in GOV and CAP.

**DG-ENV-REQ-001** The assessor shall identify, for each ENV control in scope, whether it is assessed as a dependency of a Service Outcome or as support for a stakeholder performance claim, and shall record that linkage in the ControlAssessment.

## 5 Dependencies, fault domains and common-mode concerns

- **Weather as a common-mode initiator**: a heatwave simultaneously reduces heat-rejection capacity, derates generators and transformers, raises water demand, increases grid stress and may coincide with water restrictions (AIDCF-004 X10). These must be assessed together, not as independent events (MCF-ENV-021, MCF-ENV-011).
- **Single water source**: mains supply from one network, or one borehole, for all evaporative plant.
- **Shared sensing**: one weather station or one outdoor air sensor driving economiser decisions for all air handlers; a common sensor fault becomes a common environmental excursion.
- **Pollution events**: wildfire smoke or industrial releases affect all outdoor air intakes at once (MCF-ENV-003).
- **Metering dependencies**: performance claims depend on a small number of revenue and sub-meters; a single meter fault can distort reported PUE for a year.
- **Regulatory dependencies**: permits for water abstraction, discharge, generator emissions and refrigerant handling are external dependencies whose lapse can constrain operation.
- **Heat reuse off-taker**: where heat is exported, the off-taker depends on the data centre and the data centre may depend on the off-taker's heat sink; this bidirectional dependency must be explicit.

## 6 Threats, hazards and failure scenarios with propagation paths

| Scenario | Propagation path | Primary safeguards (controls) |
|---|---|---|
| Extreme ambient plus water restriction (X10) | Heatwave above design ambient → dry coolers lose capacity, evaporative demand rises → water authority restricts supply → heat rejection insufficient → accelerators throttle → training throughput outcome missed | MCF-ENV-021, MCF-ENV-011, MCF-ENV-022 |
| Ambient exceedance at rack inlet | Containment breach or hot-air recirculation → inlet temperatures above envelope → throttling and hardware stress; masked if sensing is at return air | MCF-ENV-001 |
| Condensation | Facility water temperature lowered for capacity → coolant below room dew point in humid season → condensation on manifolds → water on electrical components | MCF-ENV-002 |
| Air contamination | Wildfire smoke drawn in by economisers → corrosive deposition → elevated hardware failure rate over months | MCF-ENV-003 |
| Suppression acoustic event | Inert-gas discharge in a hall with HDD-based storage → acoustic disruption → storage errors and possible data integrity events | MCF-ENV-004 |
| Refrigerant loss | Leak in machinery room → concentration above practical limit → asphyxiation or (A2L) ignition hazard; loss of chiller capacity | MCF-ENV-018 |
| Efficiency-resilience conflict | UPS placed in eco-mode → grid transient during AI load swing → transfer fails → load lost | MCF-ENV-008 |
| Poor coolant or water quality | Biofouling in cooling tower → capacity loss and Legionella risk | MCF-ENV-009 |
| Metering or claim error | PUE computed from an instantaneous snapshot or wrong meters → regulatory report misstated → restatement and loss of trust | MCF-ENV-005, MCF-ENV-016 |
| Battery spares incident | Lithium-ion spares stored at high state of charge next to critical plant → thermal runaway | MCF-ENV-017 |
| Fuel spill | Delivery overfill → fuel to surface drains → environmental incident; fire risk | MCF-ENV-019, MCF-ENV-012 |
| Climate-driven flood (X20) | Rainfall intensity above original design → drainage overwhelmed → flooding of plant | MCF-ENV-023 |
| Resource constraint | Grid reinforcement delayed → planned AI expansion cannot be energised → capability growth outcome missed | MCF-ENV-024 |

## 7 Safeguards

- **Prevent**: declared envelopes traceable to ASHRAE classes or OEM limits; dew point margin; filtration and economiser lockouts; quiet suppression nozzles; resilience impact assessment for efficiency measures; water treatment; secondary containment; refrigerant leak checks; safe state of charge for battery spares.
- **Detect**: rack-inlet and coolant-supply sensing; corrosion coupons; refrigerant detectors; water and energy metering; reconciliation of reported metrics.
- **Contain**: interceptors and bunds; quarantine containers for damaged cells; machinery-room ventilation.
- **Correct**: forecast-triggered heatwave procedures; water-restriction procedures; restatement of reported metrics.
- **Recover**: alternative water sources; load-reduction steps; demountable flood defences.

## 8 Critical-gate linkage

| Gate | Name | CRITICAL controls (this domain) | SUPPORTING controls (this domain) |
|---|---|---|---|
| CG-01 | Capability and outcome definition | none | MCF-ENV-024 |
| CG-03 | Critical dependency visibility | none | MCF-ENV-011, MCF-ENV-022, MCF-ENV-024 |
| CG-04 | Life safety and hazardous energy | MCF-ENV-018 | MCF-ENV-009, MCF-ENV-017, MCF-ENV-019 |
| CG-05 | Resilient electrical supply | none | MCF-ENV-008, MCF-ENV-021 |
| CG-06 | Thermal continuity | none | MCF-ENV-001, MCF-ENV-002, MCF-ENV-008, MCF-ENV-009, MCF-ENV-011, MCF-ENV-021 |
| CG-08 | Compute, storage and network functional integrity | none | MCF-ENV-001, MCF-ENV-003, MCF-ENV-004 |
| CG-09 | Failure containment | none | MCF-ENV-023 |
| CG-14 | Change control | none | MCF-ENV-008 |

Notes on the mapping:

- **CG-04** is carried in ENV by refrigerants and coolants (MCF-ENV-018, CRITICAL), because refrigerant release in occupied or machinery spaces is a direct life-safety hazard. Battery materials, fuel and suppressant handling and water hygiene are SUPPORTING; their in-service safety equivalents are in POW and PHY.
- **CG-06** is informed by six ENV controls (temperature and humidity envelopes, water quality, water scarcity response, heatwave readiness, and the resilience-efficiency trade-off). None is CRITICAL because CG-06 is carried by the THM heat-removal controls; ENV supplies the environmental conditions and stress cases.
- **CG-05** is informed by the resilience-efficiency trade-off (eco-mode, staging) and heatwave readiness (generator derating).
- **CG-08** is informed by environmental conditions that degrade hardware: temperature (throttling), contamination and acoustic effects.
- **CG-01** and **CG-03** are informed by long-term resource constraints and water dependencies.
- Energy, water and carbon performance controls (MCF-ENV-005, MCF-ENV-006, MCF-ENV-007, MCF-ENV-010, MCF-ENV-012 to MCF-ENV-016, MCF-ENV-020) map to no gate. They are scored in the ENV domain and are decisive for stakeholder performance claims, but not for the capability gates.

**DG-ENV-REQ-002** The assessor shall record the gate-level evaluation required for every SUPPORTING ENV control that is NONCONFORMING, stating whether the deficiency defeats the gate scope, before a gate PASS is recorded.

**DG-ENV-REQ-003** An ENV performance claim (energy, water, carbon) shall not be reported in an assurance statement unless the corresponding control is CONFORMING at its required claim type, or the claim is reported with the limitation and UNKNOWN Record that apply.

## 9 Capability-profile parameters

Unlabelled values are attributed to the cited source family; values labelled illustrative show order of magnitude only.

| Control | Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|---|
| MCF-ENV-001 | Recommended IT inlet air temperature envelope | °C | 18 to 27 | ASHRAE TC 9.9 thermal guidelines recommended envelope |
| MCF-ENV-001 | Liquid-cooling facility/TCS supply class | ASHRAE W class | W32 or W45 (illustrative) | ASHRAE TC 9.9 liquid cooling classes; OEM requirement |
| MCF-ENV-001 | Rack inlet sensor density | sensors per rack | 3 (top, middle, bottom; illustrative) | Capability profile; ASHRAE measurement practice |
| MCF-ENV-001 | Permitted excursion time outside recommended envelope | hours per year | per OEM allowable (illustrative: 50) | Capability profile |
| MCF-ENV-002 | Recommended dew point envelope | °C dew point | -9 to 15, and ≤ 60% RH | ASHRAE TC 9.9 thermal guidelines recommended envelope |
| MCF-ENV-002 | Minimum margin of coolant supply temperature above room dew point | K | 2 (illustrative) | Capability profile; CDU OEM guidance |
| MCF-ENV-003 | Gaseous corrosion severity level | ANSI/ISA-71.04 class | G1 | ASHRAE TC 9.9 gaseous and particulate contamination guidance |
| MCF-ENV-003 | Particulate cleanliness | ISO 14644-1 class | 8 | ASHRAE TC 9.9 contamination guidance |
| MCF-ENV-003 | Corrosion coupon interval | months | 3 (illustrative) | Capability profile |
| MCF-ENV-004 | Occupational noise lower / upper exposure action values | dB(A) daily exposure | 80 / 85 | EU Directive 2003/10/EC (noise at work) or national equivalent |
| MCF-ENV-004 | Sound pressure limit at storage arrays during discharge | dB | per storage OEM threshold | Storage OEM guidance; suppression designer |
| MCF-ENV-004 | Site boundary noise limit | dB(A) | per planning or environmental permit | Permit conditions |
| MCF-ENV-005 | PUE measurement period | months | 12 | ISO/IEC 30134-2 |
| MCF-ENV-005 | PUE measurement category | category | Category 2 or higher (illustrative) | ISO/IEC 30134-2; capability profile |
| MCF-ENV-005 | Revenue/sub-meter accuracy class | class | 0.5S or better (illustrative) | IEC 62053 series |
| MCF-ENV-006 | Maximum unallocated energy | % of site total | 2 (illustrative) | Capability profile |
| MCF-ENV-007 | IT load points for efficiency characterisation | % of design IT load | 25 / 50 / 75 / 100 (illustrative) | Capability profile |
| MCF-ENV-007 | Energy reuse factor reporting | ratio | measured annually | ISO/IEC 30134-6 |
| MCF-ENV-009 | Legionella risk assessment review interval | months | 24 (illustrative) | National Legionella guidance (e.g. HSE L8, ASHRAE 188); capability profile |
| MCF-ENV-010 | WUE measurement period | months | 12 | ISO/IEC 30134-9 |
| MCF-ENV-011 | On-site water storage autonomy at design-day consumption | hours | 48 (illustrative) | Capability profile |
| MCF-ENV-011 | Heat-rejection capacity in reduced-water mode at design ambient | % of design IT load | per thermal design (illustrative: 80) | Thermal design basis |
| MCF-ENV-012 | Discharge monitoring frequency | per consent | per permit conditions | Discharge consent |
| MCF-ENV-013 | Materiality threshold for boundary exclusions | % of total emissions | 5 (illustrative) | Capability profile; GHG Protocol guidance on exclusions |
| MCF-ENV-014 | Temporal matching granularity | interval | annual or hourly (declared) | GHG Protocol Scope 2 Guidance; hourly matching frameworks |
| MCF-ENV-015 | Embodied data coverage | % of hardware and plant by spend | 80 (illustrative) | Capability profile |
| MCF-ENV-016 | Restatement threshold | % change in reported metric | 5 (illustrative) | Capability profile |
| MCF-ENV-017 | Maximum state of charge for stored lithium-ion spares | % SoC | 30 (illustrative) | OEM guidance; aligns with air-transport limit for UN 3480 lithium-ion batteries |
| MCF-ENV-018 | Refrigerant leak-check frequency | per system | tiered by CO2e charge per applicable regulation | EU F-gas Regulation (EU) 2024/573 or national equivalent |
| MCF-ENV-018 | Refrigerant detector alarm setpoint | % of practical limit or ATEL/ODL | per EN 378 / ISO 5149 (illustrative: 50% of practical limit) | EN 378 / ISO 5149 refrigerating systems safety |
| MCF-ENV-019 | Secondary containment capacity | % of largest tank volume | 110 (illustrative) | Common oil-storage regulation and bunding practice; local permit |
| MCF-ENV-021 | Design extreme ambient dry-bulb | °C | site n=20-year extreme (illustrative) | ASHRAE Handbook climatic design data |
| MCF-ENV-021 | Climate-adjusted design ambient uplift | K | 2 (illustrative) | Owner-adopted climate projection (e.g. IPCC AR6 scenario) |
| MCF-ENV-021 | Forecast trigger margin below design ambient | K | 3 (illustrative) | Capability profile |
| MCF-ENV-022 | Water-stress planning horizon | years | 20 (illustrative) | Capability profile |
| MCF-ENV-023 | Climate scenario and horizon for flood adaptation | scenario / year | SSP2-4.5 to 2060 (illustrative) | IPCC AR6 scenarios; owner-adopted projection |
| MCF-ENV-023 | Demountable defence deployment time | hours | less than flood warning lead time (illustrative: 4) | Flood response plan |
| MCF-ENV-024 | Resource planning horizon | years | 15 (illustrative) | Capability profile |

## 10 Evidence expectations by claim type

| Claim type | Assurance Level | Controls | Profile tiers used | Sufficiency floors used |
|---|---|---|---|---|
| DESIGN | AL2 | MCF-ENV-008, MCF-ENV-013, MCF-ENV-015, MCF-ENV-022, MCF-ENV-023, MCF-ENV-024 | CP-1, CP-2 | S2, S3 |
| IMPLEMENTATION | AL3 | MCF-ENV-004, MCF-ENV-006, MCF-ENV-014 | CP-2 | S3 |
| OPERATION | AL4 | MCF-ENV-001, MCF-ENV-002, MCF-ENV-003, MCF-ENV-005, MCF-ENV-007, MCF-ENV-009, MCF-ENV-010, MCF-ENV-012, MCF-ENV-016, MCF-ENV-017, MCF-ENV-018, MCF-ENV-019, MCF-ENV-020 | CP-3, CP-5 | S3, S4 |
| RESILIENCE | AL5 | MCF-ENV-011, MCF-ENV-021 | CP-4 | S4 |

- **DESIGN (AL2)**: methodology and boundary statements, LCA methods, climate and water-stress assessments, resilience impact assessments (E1 with E7 analysis). Climate assessments name the scenario, horizon and data source.
- **IMPLEMENTATION (AL3)**: meter-to-category mapping, allocation methods reconciled to meters, registry retirement statements, acoustic and noise surveys as built (E1+E2 with reconciliation).
- **OPERATION (AL4)**: twelve months of telemetry and meter data, coupon results, leak-check records, treatment records, inventories reconciled to physical counts (E3, often with E2 configuration evidence).
- **RESILIENCE (AL5)**: exercises of water-restriction switchover and heatwave procedures, or records of real events at or beyond design conditions (E4).

Evidence cautions:

- PUE and WUE are annual energy and water ratios; instantaneous or monthly snapshots do not satisfy ISO/IEC 30134-2 or -9.
- Environmental telemetry is E3 only if sensor location and calibration are established; return-air sensing does not evidence inlet temperature (U8).
- Certificates of renewable energy are evidence only when their retirement is verified in the registry (U6 otherwise).
- Supplier sustainability reports are E5 at best for their own scope; they rarely evidence the site's metrics.

**DG-ENV-REQ-004** Reported energy and water metrics relied on in an assurance statement shall be reperformed by the assessor from source meter data for at least the reporting period, and the reperformance shall be retained as E7 evidence with lineage to the meters.

## 11 Assessment guidance

1. **Separate the two faces.** Decide for each control whether it supports outcomes or performance claims (DG-ENV-REQ-001).
2. **Check envelopes at the equipment.** Confirm sensor locations at rack inlet and TCS supply; compute excursion time and, for liquid-cooled halls, dew point margin.
3. **Stress the climate.** Take the design extreme ambient and the climate-adjusted ambient; check heat rejection, generators and transformers together, then add water restriction.
4. **Find the efficiency measures.** Read UPS modes, setpoints and staging from configuration, not from policy; check each has a resilience impact assessment.
5. **Reperform the metrics.** Recompute PUE, WUE and CUE from meter data; reconcile allocation to the site total; verify certificate retirement.
6. **Inspect hazardous materials.** Reconcile refrigerant, coolant and battery inventories to nameplates and stores; check detection, ventilation, containment and quarantine.
7. **Read the permits.** List environmental permits with conditions and renewal dates; compare monitoring data with limits.
8. **Roll up.** Record results, Findings and UNKNOWN Records; evaluate CG-04 for MCF-ENV-018 and supply gate-level evaluations for SUPPORTING mappings.

Common pitfalls: accepting design PUE as measured; omitting generator fuel from total facility energy; counting refrigerant leakage outside Scope 1; ignoring A2L requirements when refrigerants are changed; treating dry-cooler capacity at ISO conditions as available in a heatwave.

## 12 Testing safety (hazardous-energy testing authorisation)

Most ENV assessment is desk-based or observational. The exceptions involve hazardous atmospheres, chemicals and plant operation.

**DG-ENV-REQ-005** An assessor shall not take water, fuel or refrigerant samples, operate plant to change environmental conditions, or enter machinery rooms during a refrigerant alarm; sampling and tests relied on as evidence shall have been performed by competent persons under the site's procedures.

**DG-ENV-REQ-006** Exercises that change cooling mode (for example switchover to reduced-water or dry operation) relied on as evidence shall have been performed under a method statement approved by the facility operator, with thermal contingency in place and the capability owner informed.

| Activity | Hazard | Precondition |
|---|---|---|
| Refrigerant detector test (MCF-ENV-018) | Calibration gas; alarm-triggered ventilation | Certified contractor; machinery room cleared |
| Legionella sampling (MCF-ENV-009) | Aerosol exposure | Respiratory protection per control scheme |
| Fuel sampling (MCF-ENV-019 with POW) | Flammable liquid | Ignition-source control; spill kit |
| Reduced-water switchover (MCF-ENV-011) | Thermal margin loss | Method statement; thermal contingency |
| Occupational noise survey (MCF-ENV-004) | Noise exposure | Hearing protection |
| Interceptor inspection (MCF-ENV-012) | Confined space | Inspection from surface only |

## 13 UNKNOWN hot-spots

| Control | UNKNOWN rule |
|---|---|
| MCF-ENV-001 Temperature Control | If inlet sensing is only at return air, record a U8 method UNKNOWN; the OPERATION claim is UNKNOWN for that hall. |
| MCF-ENV-002 Humidity Control | If dew point margin is not monitored for a liquid-cooled hall, record a U1 UNKNOWN and refer to THM fluid controls. |
| MCF-ENV-005 PUE Measurement | If metering does not support the declared category, record a U8 method UNKNOWN and report PUE only with a limitation. |
| MCF-ENV-008 Resilience-Efficiency Trade-Off | If an efficiency measure is found in configuration without an assessment, record a U1 UNKNOWN and carry it into CG-05/CG-06 gate-level evaluation. |
| MCF-ENV-011 Water Scarcity Response | If reduced-water capacity is unknown, record a U1 UNKNOWN referred to CG-06. |
| MCF-ENV-014 Energy Attribute Evidence | If retirement cannot be verified in the registry, record a U6 source-unverified UNKNOWN on the claim. |
| MCF-ENV-018 Refrigerants and Coolants | If detection in a machinery room is untested or absent where required, record a US4 UNKNOWN against CG-04. |
| MCF-ENV-021 Heatwave Readiness | If capacity at design ambient is unevaluated, record a U1 UNKNOWN referred to CG-06 and CG-05. |

Typical causes: colocation providers supplying summary metrics without meter data (U2); sensors at return air rather than inlet (U8); no evaluation of capacity at design ambient (U1); efficiency measures configured without assessment (U1); certificates bought but retirement not visible in the registry (U6).

**DG-ENV-REQ-007** Any UNKNOWN affecting MCF-ENV-018 shall be recorded with severity US4 and shall set CG-04 to UNKNOWN until dispositioned; UNKNOWNs on ENV performance claims shall be disclosed with the claim.

## 14 Interfaces with other domains

| Domain | Interface | What ENV needs | What ENV provides |
|---|---|---|---|
| THM | Cooling | Plant capacity curves; setpoints; refrigerant inventory | Envelopes; dew point margin; climate stress cases; water constraints |
| POW | Energy and batteries | Meter data; UPS mode; generator fuel use; battery inventory | Resilience impact of efficiency measures; heatwave derating case |
| PHY | Site and fire | Site hazard assessment; suppression design | Climate-adjusted flood; acoustic constraints on suppression |
| CMP | Hardware | Throttling telemetry; OEM envelopes | Environmental excursion data |
| STO | Storage | Acoustic and vibration sensitivity | Discharge acoustic design |
| CAP | Outcomes and growth | Demand forecasts | Resource constraints on growth |
| GOV | Reporting | Stakeholder and regulatory obligations | Traceable metrics |
| SUP | Recyclers, suppliers | Authorised waste operators; OEM product footprints | Disposition records |
| EVA | Evidence | Provenance rules | Reperformed metrics with lineage |

## 15 Informative references

Document-level references; no clause-level reliance is implied.

- ISO/IEC 30134 series — Data centre key performance indicators: -2 PUE, -3 REF, -6 ERF, -8 CUE, -9 WUE (EN 50600-4-x equivalents)
- ASHRAE TC 9.9 — Thermal Guidelines for Data Processing Environments; liquid cooling guidelines; gaseous and particulate contamination guidance
- ANSI/ISA-71.04 — Environmental conditions for process measurement and control systems: airborne contaminants
- ISO 14644-1 — Cleanroom air cleanliness classification
- EN 50600-2-3 / ISO/IEC 22237 — Environmental control
- ISO 14001 — Environmental management systems; ISO 50001 — Energy management systems
- GHG Protocol Corporate Standard and Scope 2 Guidance; ISO 14064-1 and -3
- ISO 14040 / ISO 14044 — Life cycle assessment; EN 15978; ISO 14067
- ISO 14046 — Water footprint; WRI Aqueduct water-risk atlas
- ISO 14090 / ISO 14091 — Adaptation to climate change; IPCC AR6
- ASHRAE Handbook — Fundamentals (climatic design conditions)
- EN 378 / ISO 5149 — Refrigerating systems safety; ISO 817 / ASHRAE 34 — refrigerant safety classification; ASHRAE 15
- EU F-gas Regulation (EU) 2024/573; EU Battery Regulation (EU) 2023/1542; EU WEEE Directive 2012/19/EU
- EU Energy Efficiency Directive (EU) 2023/1791 and Delegated Regulation (EU) 2024/1364 on the data-centre rating scheme
- EU Directive 2003/10/EC — noise at work; ISO 9613-2; ISO 7779
- ASHRAE 188 and HSE L8 — Legionella risk management
- EU Code of Conduct on Data Centre Energy Efficiency — best practice guidelines

## 16 Control summary

| Control ID | Title | Control type | Required AL | Claim type | Gate mappings |
|---|---|---|---|---|---|
| MCF-ENV-001 | Temperature Control | DETECTIVE | AL4 | OPERATION | CG-06 SUPPORTING; CG-08 SUPPORTING |
| MCF-ENV-002 | Humidity Control | PREVENTIVE | AL4 | OPERATION | CG-06 SUPPORTING |
| MCF-ENV-003 | Particulate and Corrosion | PREVENTIVE | AL4 | OPERATION | CG-08 SUPPORTING |
| MCF-ENV-004 | Vibration and Acoustic Conditions | PREVENTIVE | AL3 | IMPLEMENTATION | CG-08 SUPPORTING |
| MCF-ENV-005 | PUE Measurement | DETECTIVE | AL4 | OPERATION | none |
| MCF-ENV-006 | Energy Allocation | DIRECTIVE | AL3 | IMPLEMENTATION | none |
| MCF-ENV-007 | Efficiency Under Load | DETECTIVE | AL4 | OPERATION | none |
| MCF-ENV-008 | Resilience-Efficiency Trade-Off | DIRECTIVE | AL2 | DESIGN | CG-05 SUPPORTING; CG-06 SUPPORTING; CG-14 SUPPORTING |
| MCF-ENV-009 | Water Source and Quality | PREVENTIVE | AL4 | OPERATION | CG-06 SUPPORTING; CG-04 SUPPORTING |
| MCF-ENV-010 | WUE Measurement | DETECTIVE | AL4 | OPERATION | none |
| MCF-ENV-011 | Water Scarcity Response | RECOVERY | AL5 | RESILIENCE | CG-06 SUPPORTING; CG-03 SUPPORTING |
| MCF-ENV-012 | Discharge Control | PREVENTIVE | AL4 | OPERATION | none |
| MCF-ENV-013 | Carbon Accounting Boundary | DIRECTIVE | AL2 | DESIGN | none |
| MCF-ENV-014 | Energy Attribute Evidence | DETECTIVE | AL3 | IMPLEMENTATION | none |
| MCF-ENV-015 | Embodied Resource Data | DIRECTIVE | AL2 | DESIGN | none |
| MCF-ENV-016 | Reporting Traceability | DETECTIVE | AL4 | OPERATION | none |
| MCF-ENV-017 | Battery Materials | PREVENTIVE | AL4 | OPERATION | CG-04 SUPPORTING |
| MCF-ENV-018 | Refrigerants and Coolants | PREVENTIVE | AL4 | OPERATION | CG-04 CRITICAL |
| MCF-ENV-019 | Fuel and Suppressant Handling | PREVENTIVE | AL4 | OPERATION | CG-04 SUPPORTING |
| MCF-ENV-020 | Hardware and Media Waste | DIRECTIVE | AL4 | OPERATION | none |
| MCF-ENV-021 | Heatwave Readiness | RECOVERY | AL5 | RESILIENCE | CG-06 SUPPORTING; CG-05 SUPPORTING |
| MCF-ENV-022 | Drought Readiness | DIRECTIVE | AL2 | DESIGN | CG-03 SUPPORTING |
| MCF-ENV-023 | Flood Adaptation | PREVENTIVE | AL2 | DESIGN | CG-09 SUPPORTING |
| MCF-ENV-024 | Long-Term Resource Constraints | DIRECTIVE | AL2 | DESIGN | CG-01 SUPPORTING; CG-03 SUPPORTING |

## 17 Worked synthetic example

**Synthetic example. The site, figures and results below are invented for illustration and do not describe any real facility or assessment.**

*Context.* Synthetic Site S-3 is a direct-to-chip liquid-cooled site with adiabatic-assisted dry coolers, two chillers for trim cooling using an A2L refrigerant, and a published annual PUE. The decision question has two parts: (a) can S-3 sustain the training Service Outcome through the declared heatwave and water-restriction scenario; (b) is the published PUE fit to be cited in the operator's regulatory report. Profile parameters (illustrative for the example): design extreme ambient taken from the site's n=20-year value; climate uplift 2 K; water storage autonomy 48 hours; dew point margin 2 K.

*Selected results.*

| Control | Claim type | Synthetic observation | Result |
|---|---|---|---|
| MCF-ENV-001 | OPERATION | Rack-inlet sensors in place; excursion time within limit; coolant supply sensors at CDU secondary outlet | CONFORMING |
| MCF-ENV-002 | OPERATION | Dew point margin fell to 0.4 K for 30 hours in August after facility water setpoint was lowered | NONCONFORMING |
| MCF-ENV-005 | OPERATION | Reperformed PUE from meters differs by 0.03 from published value; generator fuel energy omitted | PARTIAL |
| MCF-ENV-008 | DESIGN | Lowered facility water setpoint (efficiency/capacity change) made without resilience impact assessment | NONCONFORMING |
| MCF-ENV-011 | RESILIENCE | Storage autonomy recomputed at 31 hours at design-day consumption; dry-mode capacity 78% of IT load; exercise performed | PARTIAL |
| MCF-ENV-018 | OPERATION | A2L chiller room has detection and ventilation tested; leak checks current | CONFORMING |
| MCF-ENV-021 | RESILIENCE | Capacity analysis at climate-adjusted ambient not performed | UNKNOWN (U1) |

*Gate-level evaluations.* CG-04: MCF-ENV-018 CONFORMING; ENV contributes no defeat. CG-06 (SUPPORTING inputs): MCF-ENV-002 NONCONFORMING and MCF-ENV-008 NONCONFORMING are referred to the THM-led CG-06 evaluation, which must decide whether condensation risk and the unassessed setpoint change defeat thermal continuity; MCF-ENV-011 PARTIAL and the MCF-ENV-021 UNKNOWN mean that the heatwave-plus-restriction scenario is not shown to be sustained, and the CG-06 evaluation records this as a material condition. CG-14: MCF-ENV-008 NONCONFORMING indicates an uncontrolled material change, evaluated at CG-14 gate level.

*Performance claim.* Under DG-ENV-REQ-003 the published PUE is not cited without a limitation: the reperformed value including generator fuel energy is reported, with the PARTIAL result disclosed.

*Actions.* Restore dew point margin or add room dehumidification; perform a resilience impact assessment of the setpoint change under change control; increase water storage or reduce design-day consumption; complete capacity analysis at climate-adjusted ambient; correct the PUE calculation.
