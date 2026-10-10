# AIDCF-007A Control Catalogue — PHY Physical Site, Building and Security Infrastructure

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-PHY](../../../aidcf-018-domain-guides/AIDCF-018-PHY_Physical_Site_Building_and_Security_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-PHY-001](#mcf-phy-001) | Site Hazard Assessment | DIRECTIVE | DESIGN | AL2 | — | CG-02, CG-03, CG-04 |
| [MCF-PHY-002](#mcf-phy-002) | External Exposure | PREVENTIVE | DESIGN | AL2 | — | CG-09, CG-03 |
| [MCF-PHY-003](#mcf-phy-003) | Access and Logistics | PREVENTIVE | OPERATION | AL4 | — | CG-10 |
| [MCF-PHY-004](#mcf-phy-004) | Adjacent Risk | DIRECTIVE | DESIGN | AL2 | — | CG-03 |
| [MCF-PHY-005](#mcf-phy-005) | Structural Capacity | PREVENTIVE | DESIGN | AL2 | — | CG-02, CG-04 |
| [MCF-PHY-006](#mcf-phy-006) | Rack Loading | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-04, CG-14 |
| [MCF-PHY-007](#mcf-phy-007) | Anchorage and Vibration | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-09 |
| [MCF-PHY-008](#mcf-phy-008) | Building Envelope | PREVENTIVE | OPERATION | AL4 | — | CG-06 |
| [MCF-PHY-009](#mcf-phy-009) | Security Zones | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-15, CG-09 |
| [MCF-PHY-010](#mcf-phy-010) | Fire Zones | PREVENTIVE | IMPLEMENTATION | AL3 | CG-09 | CG-04 |
| [MCF-PHY-011](#mcf-phy-011) | Water Zones | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-09, CG-04 |
| [MCF-PHY-012](#mcf-phy-012) | Tenant Segregation | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-13, CG-02 |
| [MCF-PHY-013](#mcf-phy-013) | Identity-Based Access | PREVENTIVE | OPERATION | AL4 | — | CG-15 |
| [MCF-PHY-014](#mcf-phy-014) | Visitor Control | PREVENTIVE | OPERATION | AL4 | — | — |
| [MCF-PHY-015](#mcf-phy-015) | Surveillance Coverage | DETECTIVE | IMPLEMENTATION | AL3 | — | — |
| [MCF-PHY-016](#mcf-phy-016) | Alarm Response | DETECTIVE | EFFECTIVENESS | AL5 | — | — |
| [MCF-PHY-017](#mcf-phy-017) | Delivery Controls | PREVENTIVE | OPERATION | AL4 | — | — |
| [MCF-PHY-018](#mcf-phy-018) | Equipment Movement | PREVENTIVE | OPERATION | AL4 | — | CG-04 |
| [MCF-PHY-019](#mcf-phy-019) | Media Custody | PREVENTIVE | OPERATION | AL4 | — | — |
| [MCF-PHY-020](#mcf-phy-020) | Decommissioning Custody | PREVENTIVE | OPERATION | AL4 | — | — |
| [MCF-PHY-021](#mcf-phy-021) | Fire Detection | DETECTIVE | EFFECTIVENESS | AL5 | CG-04 | CG-09 |
| [MCF-PHY-022](#mcf-phy-022) | Suppression Interfaces | CORRECTIVE | EFFECTIVENESS | AL5 | CG-04 | CG-06, CG-07 |
| [MCF-PHY-023](#mcf-phy-023) | Egress and Emergency Access | PREVENTIVE | OPERATION | AL4 | CG-04 | — |
| [MCF-PHY-024](#mcf-phy-024) | Emergency Shutdown Governance | DIRECTIVE | EFFECTIVENESS | AL5 | CG-04 | CG-07, CG-09 |

## PHY-01 Site and location resilience

### MCF-PHY-001

**Site Hazard Assessment** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Establish that the natural and man-made hazards to which the site is exposed are identified, quantified against declared design levels and reflected in the design of facilities that host AI capability, so that no credible site-wide event exceeds the protection assumed by the architecture.

**Requirement.** The facility owner shall maintain a site hazard assessment, prepared or reviewed by competent specialists, that quantifies flood (fluvial, pluvial, coastal and groundwater), seismic, wind, lightning, extreme-temperature, wildfire and subsidence hazards at the declared design exceedance levels. The facility owner shall record, for each hazard, the design level adopted, the protective measures relied on and the residual exposure, and shall reassess the hazards when hazard mapping, climate projections or the site layout change.

**Assessment criteria**

1. A hazard assessment exists that covers every hazard family in AIDCF-004 Part V applicable to the site, with excluded hazards justified.
2. Each quantified hazard states the source data, return period or annual exceedance probability and the design level adopted for critical plant.
3. Critical plant (MV intake, transformers, switchgear, UPS, generators, fuel, heat rejection, CDUs) elevation and protection are shown to meet the adopted flood design level plus freeboard.
4. Seismic design category and non-structural component requirements derived from the local code are recorded and traced into PHY-02 anchorage requirements.
5. Residual exposures are recorded as risks with an owner and are reflected in the resilience scenarios.
6. The assessment is no older than the declared review interval and post-dates the last material change to hazard mapping or site layout.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Design flood annual exceedance probability for critical plant | % per year | 0.1 (illustrative) | Capability profile; national flood-risk mapping commonly publishes 1% and 0.1% AEP extents |
| Freeboard above design flood level for critical plant | mm | 300 (illustrative) | Capability profile; site flood-risk assessment |
| Hazard assessment review interval | months | 36 (illustrative) | Capability profile |

**Minimum evidence**

- Site hazard assessment report with hazard-by-hazard design levels and data sources
- Flood-risk assessment and topographic survey showing critical plant finished floor levels
- Seismic hazard determination and design category from the structural engineer of record
- Lightning risk assessment (e.g. IEC 62305-2 method) and protection design
- Risk register entries for residual site exposures with owners

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY |
| periodCoverage | Current assessment within the review interval; hazard data at its latest published edition. |
| independence | Hazard quantification by a competent specialist; acceptance by a reviewer independent of the site-selection sponsor. |
| mandatoryItems | Site hazard assessment; Flood-risk assessment with critical plant levels |
| acceptableAlternatives | Insurer-commissioned natural-hazard survey where it quantifies the same hazards at stated exceedance levels |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-02, CG-03, CG-04. |
| reassessmentTriggers | Revised flood, seismic or wildfire hazard maps; New climate projection adopted by the owner; Relocation or addition of critical plant; Hazard event at or near the site |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INSPECTION

**Assessment procedure**

1. Obtain the hazard assessment and confirm its date, author competence and hazard coverage.
2. Compare adopted design levels to the capability-profile parameters and to current public hazard data.
3. Walk down critical plant locations and verify finished floor and equipment plinth levels against survey.
4. Trace seismic and wind design levels into structural and anchorage design documents.
5. Confirm residual exposures appear in the risk register and in at least one resilience scenario.

**Gate mappings.** CG-02 Boundary and architecture integrity (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to every site in the assessment boundary, including colocation sites where the assessed party must obtain the provider's hazard assessment. Not applicable to purely logical capability with no physical site in the boundary.

**Lifecycle stages.** PLAN, DESIGN, CHANGE · **Operating states.** NORMAL, EMERGENCY

**Failure modes addressed.** Critical plant located below credible flood level; Seismic design level understated for non-structural components; Hazard assessment based on superseded mapping; Residual exposure not carried into resilience scenarios

**Testing safety.** Desk-based assessment; no hazardous testing. Site walk-downs follow the host site induction and are escorted in plant areas.

**UNKNOWN rule.** If the hazard assessment is absent or predates a material revision of hazard mapping, record a U1 or U3 UNKNOWN against the site and treat flood and seismic protection of critical plant as unverified for CG-02 and CG-04 evaluation.

**Ontology classes.** Hazard, InfrastructureSystem, FailureScenario, Safeguard · **Related controls.** MCF-PHY-002, MCF-PHY-007, MCF-ENV-023, MCF-RES-003

**Informative references.** ISO 31000 (risk management); IEC 62305 series (lightning protection); ASCE/SEI 7 or EN 1998 (seismic actions, per jurisdiction); EN 50600-2-1 (building construction); FM Global Property Loss Prevention Data Sheets (natural hazards)

### MCF-PHY-002

**External Exposure** · PREVENTIVE · claim type DESIGN · required AL2

**Objective.** Ensure that threats and hazards originating outside the site boundary, including adjacent industrial activity, transport corridors, airspace, hostile vehicles and airborne contaminants, are characterised and mitigated so that they cannot disable redundant infrastructure together.

**Requirement.** The facility owner shall identify external exposures within a defined radius of the site, including major-accident-hazard installations, pipelines, rail and road corridors carrying hazardous goods, flight paths, high-voltage corridors and sources of smoke or corrosive emissions. The facility owner shall specify perimeter protection (stand-off, hostile vehicle mitigation, blast and intrusion resistance) proportionate to the assessed threat, and shall show that no single external event can impair both redundant utility intakes, both generator yards or all heat-rejection plant.

**Assessment criteria**

1. An external exposure register exists covering the declared radius, with each exposure's consequence path to site infrastructure described.
2. Hostile vehicle mitigation at the perimeter is rated to the vehicle mass and speed set in the threat assessment and covers all vehicle-accessible approaches to critical plant.
3. Redundant utility intakes, generator yards and heat-rejection plant are separated so that a single external event in the register cannot reach both.
4. Air intakes for halls and plant are located and protected against smoke, exhaust re-entrainment (including from the site's own generators) and corrosive emissions identified in the register.
5. Exposure changes in the surrounding area are monitored and the register is reviewed at the declared interval.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| External exposure assessment radius | km | 2 (illustrative) | Capability profile; threat assessment |
| Hostile vehicle mitigation rating | vehicle mass / impact speed | 7,500 kg at 48 km/h (illustrative) | Threat assessment; rating per IWA 14-1 or PAS 68 test classification |
| External exposure review interval | months | 12 (illustrative) | Capability profile |

**Minimum evidence**

- External exposure register with distances and consequence paths
- Security threat assessment and perimeter protection specification
- Test certificates for installed hostile vehicle mitigation products
- Site plan showing separation of redundant intakes, generator yards and heat rejection
- Air-intake and exhaust plume study for generator exhaust re-entrainment

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E7 |
| optionalClasses | E3; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY |
| periodCoverage | Register current within the review interval. |
| independence | Threat assessment by a security specialist not responsible for the perimeter budget. |
| mandatoryItems | External exposure register; Perimeter protection specification with ratings |
| acceptableAlternatives | Statutory land-use consultation-zone determinations in place of a bespoke industrial-hazard study, where they cover the declared radius |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-09, CG-03. |
| reassessmentTriggers | New hazardous installation, pipeline or transport route within the radius; Change in threat level from the security function; Perimeter layout change; Generator relocation or new exhaust stacks |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, ANALYSIS

**Assessment procedure**

1. Review the exposure register and test it against public land-use and hazardous-installation data.
2. Inspect perimeter protection and match installed products to rated test certificates.
3. Overlay single external events (explosion overpressure contour, vehicle impact, smoke plume) on the site plan and check whether any reaches both redundant elements.
4. Review the exhaust re-entrainment study against current generator and intake positions.

**Gate mappings.** CG-09 Failure containment (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to owned and leased sites; for colocation the assessed party relies on the provider's register and perimeter evidence. Not applicable where the site is wholly within a host facility whose perimeter is assessed as a separate boundary element.

**Lifecycle stages.** PLAN, DESIGN, CHANGE · **Operating states.** NORMAL, EMERGENCY

**Failure modes addressed.** Single external explosion or fire affecting both redundant intakes; Vehicle-borne attack reaching transformer or generator yard; Generator exhaust drawn into hall air intakes during utility outage; New adjacent hazard not detected

**Testing safety.** Desk-based assessment; no hazardous testing. Site walk-downs follow the host site induction and are escorted in plant areas.

**UNKNOWN rule.** If separation of redundant intakes or generator yards against a registered external event cannot be demonstrated from drawings, record a U5 coverage UNKNOWN and carry it into the CG-09 evaluation as an untested containment boundary.

**Ontology classes.** Threat, Hazard, FaultDomain, Safeguard · **Related controls.** MCF-PHY-001, MCF-PHY-009, MCF-DEP-007

**Informative references.** IWA 14-1 (vehicle security barriers); PAS 68 (hostile vehicle mitigation); EN 50600-2-5 (security systems); ISO/IEC 27002 (physical and environmental security)

### MCF-PHY-003

**Access and Logistics** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that the site can receive the deliveries, emergency services and replacement equipment on which continuity and recovery of AI capability depend, including heavy dense racks, transformers and fuel, under normal and emergency conditions.

**Requirement.** The facility operator shall maintain a logistics and access plan that defines routes and constraints for fuel delivery, emergency services, rack-scale IT deliveries and replacement of the largest plant items (transformers, generators, chillers, CDUs). The facility operator shall verify that loading docks, lifts, corridors, ramps and doors along each route are rated for the mass and dimensions of the heaviest declared item, and shall maintain an alternative access route for fuel and emergency services when the primary route is obstructed.

**Assessment criteria**

1. Each route in the plan states the governing constraint (door clear opening, lift rating, ramp gradient, slab or dock rating) and the heaviest item it is verified for.
2. The heaviest declared fully populated rack (including integrated liquid-cooling manifolds) can be moved from dock to its final position without exceeding any route rating.
3. A replacement path exists for each transformer, generator and chiller that does not require de-energising the redundant counterpart.
4. At least the declared number of independent access routes for fuel tankers and fire appliances exists and has been driven or walked within the review period.
5. Logistics constraints are communicated to IT deployment teams before procurement of new rack types.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Heaviest declared delivered item on IT route (crated rack) | kg | 3,000 (illustrative) | Capability profile; rack OEM shipping data |
| Independent access routes for fuel and emergency vehicles | count | 2 (illustrative) | Capability profile; emergency services consultation |

**Minimum evidence**

- Logistics and access plan with route constraints
- Lift, dock leveller and slab rating certificates or structural statements
- Plant replacement method statements for largest items
- Records of route trials or delivery records for the heaviest rack type deployed
- Fire-service access consultation records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E4; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Twelve months of delivery and route records, including at least one heaviest-rack delivery. |
| independence | Route verification records produced by the logistics or facilities team, sampled by the assessor against physical measurements. |
| mandatoryItems | Logistics and access plan; Route rating evidence for the heaviest declared rack |
| acceptableAlternatives | Structural engineer's statement for route slabs where load-test certificates are unavailable |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-10. |
| reassessmentTriggers | Introduction of a heavier rack type or integrated liquid-cooled rack; Site works obstructing a route; Lift or dock replacement; Change of fuel supplier vehicle type |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, SAMPLING, OBSERVATION

**Assessment procedure**

1. Review the plan and identify the governing constraint on each route.
2. Measure a sample of constraints (door openings, ramp gradients) and compare with the plan.
3. Compare the heaviest rack in the deployment pipeline with lift and route ratings.
4. Review plant replacement method statements for dependency on redundant counterparts.
5. Confirm the alternative fuel and emergency route is unobstructed on the day of inspection.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to all sites hosting rack-scale or liquid-cooled AI systems and to any site relying on fuel deliveries for autonomy. Reduced scope applies to colocation tenants, who verify only the IT delivery route and rely on provider evidence for plant and fuel routes.

**Lifecycle stages.** DESIGN, BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION

**Failure modes addressed.** Rack cannot be delivered without exceeding lift or slab rating; Transformer replacement requires outage of the redundant unit; Fuel tanker cannot reach fill point during flood or obstruction; Emergency services access blocked by deliveries

**Testing safety.** Inspection only. Route trials with loaded racks are conducted by trained movers under the equipment-movement procedure (MCF-PHY-018); assessors do not participate in heavy-item moves.

**UNKNOWN rule.** If route ratings for the heaviest declared rack cannot be established, record a U1 UNKNOWN and treat deployment of that rack type as unverified for PHY-02 structural claims.

**Ontology classes.** Resource, Dependency, InfrastructureSystem, CapacityAssertion · **Related controls.** MCF-PHY-006, MCF-PHY-018, MCF-POW-008, MCF-SUP-019

**Informative references.** EN 50600-2-1 (building construction); ANSI/TIA-942 (data centre infrastructure)

### MCF-PHY-004

**Adjacent Risk** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure that risks arising from adjacent occupancies, shared structures and neighbouring tenants on the same campus or in the same building are identified and cannot propagate into the facility hosting the assessed capability.

**Requirement.** The facility owner shall identify adjacent occupancies and shared building elements (party walls, roofs, risers, plant rooms, car parks and loading areas) and the hazards they present, including fire load, water, vibration, vehicle impact and uncontrolled access. The facility owner shall agree with neighbouring occupiers or the landlord the separation, notification and emergency-coordination arrangements for each adjacent risk, and shall record any adjacent risk that cannot be controlled as an accepted risk with an accountable owner.

**Assessment criteria**

1. An adjacency register identifies every occupancy sharing a structural element, riser or plant space with the facility.
2. Each adjacent risk has a recorded separation measure (fire rating, physical barrier, drainage, vibration isolation) or an approved risk acceptance.
3. Notification arrangements exist for adjacent works (hot works, roof works, demolition) that could affect the facility.
4. Emergency coordination with adjacent occupiers is documented, including shared alarms and evacuation interfaces.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Adjacent-risk register review interval | months | 12 (illustrative) | Capability profile |

**Minimum evidence**

- Adjacency register with shared elements and hazards
- Landlord or neighbour agreements covering notification of works
- Fire strategy extracts for party walls and shared risers
- Risk acceptances for uncontrolled adjacent risks

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1 |
| optionalClasses | E6; E3 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY |
| periodCoverage | Register current within the review interval. |
| independence | Register reviewed by someone other than the author; agreements verified against signed copies. |
| mandatoryItems | Adjacency register |
| acceptableAlternatives | Building fire strategy where it identifies all adjacent occupancies and separations |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-03. |
| reassessmentTriggers | New adjacent tenant or change of use; Construction or demolition adjacent to the facility; Incident in an adjacent occupancy |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY, INSPECTION

**Assessment procedure**

1. Obtain the adjacency register and verify it against building plans and site walk-down.
2. Check each shared riser and plant space for third-party equipment or access.
3. Review agreements and evidence that notification of adjacent works has operated.
4. Confirm uncontrolled risks have approved acceptance by the accountable owner.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to multi-occupancy buildings, campuses and colocation facilities. A standalone single-occupier building with no shared structure records the determination and is otherwise not applicable.

**Lifecycle stages.** PLAN, DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Fire in adjacent occupancy breaches party wall; Water from neighbour plant floods hall; Uncoordinated hot works in shared riser; Neighbour access through shared roof

**Testing safety.** Desk-based assessment; no hazardous testing. Site walk-downs follow the host site induction and are escorted in plant areas.

**UNKNOWN rule.** Where adjacent occupancies cannot be determined (for example landlord refuses disclosure), record a U2 UNKNOWN and treat the shared element as an unverified fault domain.

**Ontology classes.** Hazard, Dependency, FaultDomain · **Related controls.** MCF-PHY-010, MCF-PHY-012, MCF-DEP-018

**Informative references.** EN 50600-2-1 (building construction); NFPA 101 (life safety code) or national building regulations

## PHY-02 Building and structural integrity

### MCF-PHY-005

**Structural Capacity** · PREVENTIVE · claim type DESIGN · required AL2

**Objective.** Demonstrate that floor slabs, raised floors, roofs and supports can carry the loads imposed by dense AI racks, liquid-filled cooling systems, battery systems and rooftop heat-rejection plant, with margin, for the declared deployment.

**Requirement.** The facility owner shall hold a structural capacity statement from the structural engineer of record that states the uniformly distributed and concentrated load capacity of each data hall, plant room, battery room and roof area. The facility owner shall ensure the statement accounts for operating (wet) mass of liquid-cooled racks, CDUs, manifolds, coolant distribution pipework and immersion tanks, and shall require a structural re-check before any deployment that raises planned load above the declared utilisation threshold.

**Assessment criteria**

1. Structural capacity is stated for every area hosting IT, power, battery or cooling equipment, in kN/m² distributed and kN concentrated.
2. The load model uses operating mass including coolant, not dry shipping mass, for liquid-cooled equipment and pipework.
3. Roof and plant-deck capacity covers heat-rejection plant at operating weight, including any additions for AI expansion.
4. Raised-floor pedestals and panels, where used, are rated for rolling and concentrated loads of the heaviest rack during movement.
5. Planned load per area is below the utilisation threshold, or a structural re-check is on file.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Design uniformly distributed live load, data hall | kN/m² | 20 (illustrative) | Structural engineer of record; capability profile for dense liquid-cooled racks |
| Planned-load utilisation threshold requiring structural re-check | % of rated capacity | 80 (illustrative) | Capability profile |

**Minimum evidence**

- Structural capacity statement or drawings with load capacities per area
- Load schedule with operating mass of racks, CDUs, pipework and battery systems
- Raised-floor system rating certificates (where raised floor used)
- Structural re-check reports for deployments above threshold

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E7 |
| optionalClasses | E5 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Current statement reconciled to the latest load schedule. |
| independence | Capacity statement by a chartered or licensed structural engineer; load schedule reconciliation by the assessor. |
| mandatoryItems | Structural capacity statement; Operating-mass load schedule |
| acceptableAlternatives | Original design calculations plus a current letter of reliance from a structural engineer |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-02, CG-04. |
| reassessmentTriggers | New rack type with higher mass or density; Introduction of liquid or immersion cooling; Rooftop plant addition; Change of use of a room |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION

**Assessment procedure**

1. Obtain the structural statement and confirm author competence and date.
2. Rebuild the planned load per area from the rack and plant schedule using operating mass.
3. Compare planned load with capacity and with the utilisation threshold.
4. Verify re-check reports exist where thresholds are exceeded.

**Gate mappings.** CG-02 Boundary and architecture integrity (SUPPORTING); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to all facilities and to colocation suites where the tenant's equipment imposes load; the tenant obtains the provider's rated capacity and supplies its own load schedule.

**Lifecycle stages.** DESIGN, BUILD, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Slab overstressed by wet mass of liquid-cooled racks; Roof overloaded by added dry coolers; Raised floor pedestal failure under rolling load; Load model based on dry mass

**Testing safety.** Desk-based assessment; no hazardous testing. Site walk-downs follow the host site induction and are escorted in plant areas.

**UNKNOWN rule.** If the load schedule cannot be reconciled to installed equipment, record a U5 UNKNOWN and treat structural adequacy for the affected area as unverified.

**Ontology classes.** CapacityAssertion, InfrastructureSystem, Hazard · **Related controls.** MCF-PHY-006, MCF-PHY-018, MCF-THM-009

**Informative references.** EN 1991 (actions on structures) or ASCE/SEI 7 (minimum design loads); EN 50600-2-1 (building construction)

### MCF-PHY-006

**Rack Loading** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that as-installed rack positions do not exceed the floor, raised-floor and rack-frame ratings for the actual mass of installed equipment, including liquid in manifolds and cold plates.

**Requirement.** The facility operator shall maintain a rack-position load register recording the operating mass of every rack and the rated capacity of its position. The facility operator shall verify rack mass at installation for each new rack type, shall prevent installation where the position rating would be exceeded, and shall reconcile the register to installed equipment at the declared interval.

**Assessment criteria**

1. The load register covers every occupied rack position in the assessed halls.
2. For each rack type, operating mass is evidenced by OEM data or weighing, including coolant.
3. No position exceeds its rated capacity; any exceedance has a structural engineer's acceptance.
4. A sample of positions reconciles to installed equipment during inspection.
5. Installation workflow blocks commissioning of a rack whose mass is not recorded.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum operating mass per rack position | kg | 2,000 (illustrative) | Structural capacity statement; capability profile |
| Rack-load reconciliation sample | % of positions | 10 (illustrative) | Assessment sampling plan |

**Minimum evidence**

- Rack-position load register
- OEM mass data or weighing records for each rack type
- Installation records showing load check
- Inspection reconciliation sample results

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E7 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Register reconciled within the last 12 months and after each new rack type. |
| independence | Reconciliation sample selected and checked by the assessor. |
| mandatoryItems | Rack-position load register |
| acceptableAlternatives | DCIM asset records with mass fields where they are the controlled source |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-04, CG-14. |
| reassessmentTriggers | New rack type; Retrofit of liquid cooling to existing racks; Hall re-layout |

**Assessment methods.** RECONCILIATION, SAMPLING, INSPECTION

**Assessment procedure**

1. Select a sample of positions across halls, weighted to the densest rows.
2. Compare installed equipment to the register and recompute mass.
3. Compare with position rating and identify exceedances.
4. Review the installation workflow for the mass check gate.

**Gate mappings.** CG-04 Life safety and hazardous energy (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all halls hosting AI racks. Not applicable to areas with only network or low-mass equipment where the register shows ample margin.

**Lifecycle stages.** BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Position overloaded after mid-life densification; Rack frame rating exceeded; Register not updated after rack swap

**Testing safety.** Inspection only; assessors do not move or open racks. Weighing is performed by the operator's trained staff using rated equipment.

**UNKNOWN rule.** If more than the sampled tolerance of positions cannot be reconciled, record a U5 UNKNOWN for the hall and limit the PHY-005 conclusion to reconciled areas.

**Ontology classes.** AssetInstance, CapacityAssertion · **Related controls.** MCF-PHY-005, MCF-PHY-018, MCF-CMP-003

**Informative references.** EN 50600-2-1 (building construction); Rack OEM installation guides

### MCF-PHY-007

**Anchorage and Vibration** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that racks, CDUs, battery systems, tanks, switchgear and suspended services are restrained against seismic and operational loads, and that vibration from rotating plant does not degrade IT or storage equipment.

**Requirement.** The facility owner shall specify and install anchorage and bracing for racks, CDUs, battery cabinets, fuel and water tanks, switchgear, busway and overhead cable and pipe supports to the seismic design level determined in MCF-PHY-001. The facility operator shall isolate generators, chillers and pumps so that vibration transmitted to IT spaces remains within the most restrictive OEM limit for installed equipment, and shall verify installed anchorage by inspection at commissioning and after changes.

**Assessment criteria**

1. Anchorage design for each equipment class references the site seismic design level.
2. A sample inspection finds installed anchors and bracing matching the design for the sampled items.
3. Overhead busway, cable tray and liquid-cooling manifolds have bracing compatible with the design level.
4. Vibration isolation is installed on rotating plant and measured transmitted vibration in IT spaces is within the declared limit.
5. Seismic flexibility is provided at liquid pipework connections to racks and CDUs where the design level requires it.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Transmitted vibration limit at IT equipment | mm/s RMS | per most restrictive OEM specification | OEM installation requirements |

**Minimum evidence**

- Anchorage and bracing design calculations or details
- Commissioning inspection records for anchorage
- Vibration survey report for IT spaces with plant running
- Photographic inspection sample

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E3 |
| optionalClasses | E4; E5 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY |
| periodCoverage | Commissioning records and a vibration survey after the last plant change. |
| independence | Sample inspection by the assessor or an independent structural inspector. |
| mandatoryItems | Anchorage design; Anchorage inspection records |
| acceptableAlternatives | Manufacturer seismic certification for pre-engineered racks where installed per instructions |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-09. |
| reassessmentTriggers | New equipment class; Seismic hazard revision; Generator or chiller replacement |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, SAMPLING

**Assessment procedure**

1. Trace seismic design level into anchorage design per equipment class.
2. Inspect a sample of racks, CDUs, battery cabinets and tanks for anchors and bracing.
3. Review vibration survey conditions and results against limits.
4. Check flexible connections on liquid pipework at rack and CDU interfaces.

**Gate mappings.** CG-09 Failure containment (SUPPORTING)

**Applicability.** Seismic elements apply where the local code assigns a seismic design category requiring non-structural restraint; vibration elements apply to all sites with rotating plant.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, CHANGE · **Operating states.** NORMAL, EMERGENCY

**Failure modes addressed.** Battery cabinet overturn in seismic event; Rigid pipe connection fracture releasing coolant; Storage throughput degradation from transmitted vibration

**Testing safety.** Visual inspection only; no load testing of anchors by assessors. Inspection in energised rooms follows site electrical-safety rules and keeps outside arc-flash boundaries.

**UNKNOWN rule.** If anchorage design is unavailable for battery or tank systems, record a U1 UNKNOWN and carry it into CG-09 as an unverified containment element.

**Ontology classes.** AssetInstance, Hazard, Safeguard · **Related controls.** MCF-PHY-001, MCF-PHY-005, MCF-THM-011

**Informative references.** ASCE/SEI 7 or EN 1998 (non-structural seismic provisions); Equipment OEM installation guides

### MCF-PHY-008

**Building Envelope** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure the building envelope keeps water, wind-driven rain, dust and uncontrolled air out of IT and plant spaces and maintains the enclosure integrity on which gaseous suppression and air management depend.

**Requirement.** The facility operator shall inspect roofs, roof penetrations, gutters, façades, louvres and doors at the declared interval and after severe weather, shall correct defects within a risk-based period, and shall prohibit water-bearing services and roof drainage from passing over IT and electrical rooms unless they are contained and monitored.

**Assessment criteria**

1. Envelope inspection records exist at the declared interval and after each severe-weather warning.
2. No uncontained water-bearing pipe or roof drain passes over IT or electrical rooms.
3. Open envelope defects are tracked with risk-based target dates and none affecting IT spaces is overdue.
4. Water ingress events in the last 12 months have root cause and corrective action recorded.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Envelope inspection interval | months | 6 (illustrative) | Capability profile; roofing guidance |

**Minimum evidence**

- Envelope inspection records
- Defect log with dates
- Incident records for water ingress
- Drawings showing services over IT and electrical rooms

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY |
| periodCoverage | Twelve months including at least one wet season. |
| independence | Records sampled and roof inspected by the assessor where safe access exists. |
| mandatoryItems | Envelope inspection records |
| acceptableAlternatives | Roofing contractor maintenance reports |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-06. |
| reassessmentTriggers | Water ingress incident; Roof works or new penetrations; Severe-weather event |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, OBSERVATION

**Assessment procedure**

1. Review inspection and defect records for completeness against the interval.
2. Inspect ceilings of IT and electrical rooms for water marks and uncontained services.
3. Review water ingress incidents and closure of actions.

**Gate mappings.** CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to all enclosed facilities, including modular and containerised units; colocation tenants rely on provider evidence.

**Lifecycle stages.** BUILD, OPERATE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Roof leak onto energised switchgear; Louvre failure admitting wind-driven rain; Envelope leakage defeating suppression hold time

**Testing safety.** Roof access only under the site's work-at-height permit with edge protection; assessors do not access fragile roofs.

**UNKNOWN rule.** If envelope inspection records are missing for more than one interval, record a U1 UNKNOWN; the control result is UNKNOWN for OPERATION claims.

**Ontology classes.** InfrastructureSystem, Hazard, Safeguard · **Related controls.** MCF-PHY-011, MCF-PHY-022, MCF-ENV-023

**Informative references.** EN 50600-2-1 (building construction)

## PHY-03 Physical zoning and segregation

### MCF-PHY-009

**Security Zones** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that the site is divided into layered security zones whose protection increases towards the most critical assets, including power and cooling plant as well as IT halls, so that access to any asset that can disable AI capability requires passing proportionate barriers.

**Requirement.** The security manager shall define a zoning model with at least perimeter, building, secure-corridor, critical-space and rack/cage levels, and shall assign every critical asset (MV intake, switchgear, UPS and battery rooms, generator yard, fuel, heat rejection, CDU and pump rooms, meet-me rooms, data halls, control rooms) to a zone. The security manager shall ensure each zone boundary has physical barriers, access control and detection appropriate to the zone and that critical plant zones are protected no less than the IT halls they serve.

**Assessment criteria**

1. A zoning plan assigns every critical asset in the boundary to a zone with stated protection measures.
2. Power, cooling and fuel plant zones have access control and intrusion detection at least equivalent to the data halls they serve.
3. Zone boundaries are continuous (no bypass via ceiling voids, raised floors, risers or louvres) in the sampled areas.
4. Access to critical-space zones requires multi-factor authentication and anti-tailgating measures.
5. The zoning model is reconciled to the current floor plan and security system configuration.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Authentication factors at critical-space zone entry | count | 2 (illustrative) | Capability profile; threat assessment |

**Minimum evidence**

- Zoning plan with asset assignment
- Access-control system zone and reader configuration export
- Barrier specifications and intrusion detection layout
- Inspection notes for zone continuity

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Current configuration and plan at assessment date. |
| independence | Zone continuity inspection by the assessor or an independent security consultant. |
| mandatoryItems | Zoning plan; Access-control configuration export |
| acceptableAlternatives | Certified physical-security audit report covering zone continuity, if current |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-15, CG-09. |
| reassessmentTriggers | Floor plan or use change; New critical plant area; Security incident; Threat level change |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INSPECTION

**Assessment procedure**

1. Map each critical asset from the architecture to a zone in the plan.
2. Reconcile zone readers and doors in the access-control export to the plan.
3. Inspect a sample of zone boundaries for bypass routes through voids and risers.
4. Compare plant-zone protection with data-hall protection.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to all physical sites in the boundary. Colocation tenants assess the zones they control and rely on provider evidence for shared zones.

**Lifecycle stages.** DESIGN, BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION

**Failure modes addressed.** Generator yard protected only by perimeter fence; Ceiling void bypasses hall boundary; Zoning plan out of date with hall extension

**Testing safety.** Inspection only. Above-ceiling and below-floor checks are performed by facilities staff under permit; assessors do not lift floor tiles in live halls.

**UNKNOWN rule.** If a critical plant area cannot be assigned to a zone or its boundary inspected, record a U5 UNKNOWN against that asset and treat its physical protection as unverified.

**Ontology classes.** FaultDomain, Safeguard, Threat, InfrastructureSystem · **Related controls.** MCF-PHY-013, MCF-PHY-015, MCF-SEC-009

**Informative references.** EN 50600-2-5 (security systems); ISO/IEC 27002 (physical security perimeters); ANSI/TIA-942 (data centre infrastructure)

### MCF-PHY-010

**Fire Zones** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that fire compartmentation separates redundant power, cooling and network paths so that a single fire cannot disable both halves of a redundant system, and limits fire and smoke spread between IT, battery, electrical and plant spaces.

**Requirement.** The facility owner shall define fire compartments in the fire strategy so that A and B power paths, redundant UPS and battery rooms, redundant cooling plant and diverse network routes are in separate compartments or are protected by fire-rated enclosures of the declared rating. The facility operator shall maintain fire-stopping of every penetration through compartment boundaries and shall inspect a sample of penetrations at the declared interval and after works.

**Assessment criteria**

1. The fire strategy identifies compartments and their fire-resistance ratings.
2. An overlay of redundant paths on compartments shows no single compartment containing both redundant elements of any path, or a rated enclosure where they share one.
3. Lithium-ion battery rooms (UPS or BESS) are separate compartments of at least the declared rating.
4. A sample of penetrations inspected shows intact, certified fire-stopping matching the tested system.
5. Penetrations created by works in the last 12 months have fire-stopping completion records.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Fire resistance between compartments holding redundant paths | minutes | 120 (illustrative) | Fire strategy; national building regulations; capability profile |
| Fire-stopping inspection sample per interval | % of penetrations | 20 (illustrative) | Capability profile |

**Minimum evidence**

- Fire strategy and compartmentation drawings
- Overlay of redundant paths on compartments
- Fire-stopping register with certified product data
- Penetration inspection records
- Works completion records for new penetrations

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; EMERGENCY |
| periodCoverage | Fire strategy current; penetration inspection within the last interval. |
| independence | Penetration sample inspected by the assessor or a third-party fire-stopping inspector. |
| mandatoryItems | Compartmentation drawings; Redundant-path overlay; Penetration inspection records |
| acceptableAlternatives | Third-party certified fire-stopping installer records, where the inspector is independent of the installer |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-09 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | New cable or pipe routes through compartment boundaries; Hall extension; Fire strategy revision; Introduction of lithium-ion batteries in a new location |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INSPECTION, SAMPLING

**Assessment procedure**

1. Overlay A/B power, redundant cooling and diverse network routes from the architecture onto the compartment drawings.
2. Identify any compartment hosting both redundant elements and check for rated enclosures.
3. Inspect a sample of penetrations against the fire-stopping register.
4. Review works records for penetrations created since the last inspection.

**Gate mappings.** CG-09 Failure containment (CRITICAL); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to all facilities. In modular or containerised deployments, compartments are the modules and the overlay shows separation between modules hosting redundant elements.

**Lifecycle stages.** DESIGN, BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Single fire disables both A and B paths in a shared riser (AIDCF-004 X09); Unsealed penetration after cabling works; Battery fire spreads to adjacent UPS room

**Testing safety.** Inspection only; no penetration is opened. Access to energised electrical rooms follows site electrical-safety rules.

**UNKNOWN rule.** If the redundant-path overlay cannot be produced, record a U5 UNKNOWN; CG-09 becomes UNKNOWN for fire as a common-mode initiator.

**Ontology classes.** FaultDomain, Hazard, Safeguard, FailureScenario · **Related controls.** MCF-PHY-021, MCF-POW-009, MCF-RES-006, MCF-NET-002

**Informative references.** NFPA 75 (protection of IT equipment); NFPA 76 (fire protection of telecommunications facilities); EN 50600-2-1 (building construction); NFPA 855 (stationary energy storage systems)

### MCF-PHY-011

**Water Zones** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that liquid-bearing systems, which are pervasive in liquid-cooled AI halls, are spatially and physically separated from electrical distribution and that any leak is contained, detected and drained before it reaches energised equipment.

**Requirement.** The facility owner shall define water zones identifying all spaces where water, glycol, dielectric fluid or refrigerant-bearing pipework is present. The facility owner shall locate or protect electrical switchgear, UPS, busway and PDUs so that a leak from any pipe, joint, CDU, manifold or quick-disconnect cannot reach them uncontained, using routing above or below with drip trays, bunding, falls to drains and zoned leak detection that alarms and, where declared, initiates isolation.

**Assessment criteria**

1. A water-zone plan shows every liquid-bearing route and its relation to electrical equipment.
2. No liquid joint or valve is located directly above switchgear, UPS, busway tap-off or PDU without containment.
3. Leak detection covers each containment area and alarms to a monitored location; where isolation is automatic, valve closure has been tested.
4. Drainage capacity for each zone is sized for the declared maximum credible leak rate.
5. Raised-floor or slab areas with liquid distribution have falls or barriers preventing migration to electrical zones.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Leak alarm to isolation time (automatic isolation zones) | s | 60 (illustrative) | Capability profile; CDU OEM guidance |
| Maximum credible leak rate for drainage sizing | L/min | per largest pipe and pump capacity in zone | Thermal design basis |

**Minimum evidence**

- Water-zone plan overlaid on electrical layout
- Leak detection layout and alarm configuration
- Isolation valve functional test records
- Drainage design calculation
- Inspection photographs of containment under joints

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Current layout; isolation tests within the last 12 months. |
| independence | Overlay and inspection sample by the assessor. |
| mandatoryItems | Water-zone plan; Leak detection configuration |
| acceptableAlternatives | 3D coordination model where it is the controlled as-built source |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-09, CG-04. |
| reassessmentTriggers | Liquid-cooling retrofit or expansion; Leak incident; Re-routing of pipework or busway |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, RECONCILIATION

**Assessment procedure**

1. Overlay liquid routes on electrical layouts and list proximity conflicts.
2. Inspect each conflict for containment and leak detection.
3. Review alarm routing and isolation test records.
4. Check drainage falls and barriers in a sample of zones.

**Gate mappings.** CG-09 Failure containment (SUPPORTING); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to all spaces with liquid-bearing systems, including chilled-water air cooling. Most demanding for direct-to-chip and immersion halls.

**Lifecycle stages.** DESIGN, BUILD, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Quick-disconnect leak onto rack PDU; Glycol leak migrating under raised floor to busway; Leak detection alarm not routed; Drain overwhelmed by pump discharge

**Testing safety.** Assessors do not operate isolation valves. Functional tests of automatic isolation are performed by the operator under a method statement with the affected loop in a declared maintenance state.

**UNKNOWN rule.** If the overlay cannot be produced for a liquid-cooled hall, record a U5 UNKNOWN and carry it into THM leak-management and CG-09 evaluation.

**Ontology classes.** FaultDomain, Hazard, Safeguard, Interface · **Related controls.** MCF-THM-019, MCF-THM-020, MCF-PHY-010, MCF-POW-015

**Informative references.** ASHRAE TC 9.9 liquid cooling guidance; EN 50600-2-3 (environmental control)

### MCF-PHY-012

**Tenant Segregation** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that, in shared or colocation facilities, each tenant's equipment and the shared infrastructure serving it are physically segregated and that responsibility for shared elements is explicit.

**Requirement.** The facility provider shall physically segregate tenant spaces using cages, suites or dedicated halls with access restricted to authorised tenant personnel, and shall disclose to each tenant the shared infrastructure (power paths, cooling loops, meet-me rooms, risers) serving its space. The tenant shall map its capability to those shared elements and record provider and tenant responsibilities for each.

**Assessment criteria**

1. Each tenant space is enclosed with access limited to that tenant and authorised provider staff.
2. The provider's disclosure lists the shared power, cooling and connectivity elements serving the tenant space.
3. A responsibility matrix covers each shared element, including maintenance switching notification.
4. Inspection finds no tenant equipment or cabling outside its space or in another tenant's space.

**Minimum evidence**

- Provider disclosure of shared infrastructure
- Responsibility matrix
- Access lists for tenant spaces
- Inspection notes

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E6 |
| optionalClasses | E3 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Current at assessment date. |
| independence | Disclosure verified by inspection by the assessor. |
| mandatoryItems | Shared-infrastructure disclosure; Responsibility matrix |
| acceptableAlternatives | Colocation service description and SLA where they enumerate shared elements |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-13, CG-02. |
| reassessmentTriggers | New tenant adjacent to assessed space; Provider infrastructure change; Contract renewal |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, INQUIRY

**Assessment procedure**

1. Obtain disclosure and map shared elements to the tenant's capability architecture.
2. Inspect tenant space boundaries and shared cable routes.
3. Review the responsibility matrix for maintenance switching and incident notification.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING); CG-02 Boundary and architecture integrity (SUPPORTING)

**Applicability.** Applies to colocation and multi-tenant facilities. Not applicable to single-tenant facilities, which record the determination.

**Lifecycle stages.** PLAN, BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Undisclosed shared UPS serving multiple tenants; Neighbour tenant access to shared riser; Maintenance switching on shared path without tenant notification (AIDCF-004 X14)

**Testing safety.** Desk-based assessment; no hazardous testing. Site walk-downs follow the host site induction and are escorted in plant areas.

**UNKNOWN rule.** If the provider will not disclose shared elements, record a U2 UNKNOWN and a U10 dependency UNKNOWN for the affected power and cooling paths.

**Ontology classes.** Dependency, Interface, FaultDomain · **Related controls.** MCF-DEP-019, MCF-DEP-018, MCF-PHY-009

**Informative references.** EN 50600-1 (general concepts); ISO/IEC 27002 (physical security)

## PHY-04 Access and surveillance

### MCF-PHY-013

**Identity-Based Access** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure physical access to critical zones is granted to identified individuals on a need basis, is promptly revoked, and is recorded so that every entry to a critical space can be attributed.

**Requirement.** The security manager shall operate a physical access control system that grants access to critical-space zones only to named individuals with approved business need, enforces multi-factor authentication at those zones, revokes access within the declared latency when a person leaves or changes role, and reviews critical-zone access rights at the declared interval. The security manager shall integrate leaver events from the authoritative HR or contractor source.

**Assessment criteria**

1. Access rights to critical zones are traceable to an approval for every sampled holder.
2. Leavers in the sample period had critical-zone access revoked within the declared latency.
3. Access reviews for critical zones were completed at the declared interval with removals actioned.
4. Shared or generic credentials do not grant critical-zone access.
5. Access events are retained and time-synchronised for the declared period.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Critical-zone access review interval | days | 90 (illustrative) | Capability profile |
| Leaver revocation latency | hours | 4 (illustrative) | Capability profile |

**Minimum evidence**

- Access-control system user and rights export
- Approval records for sampled holders
- HR/contractor leaver list reconciled to revocation logs
- Access review sign-offs
- Access event log sample

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Twelve months of access reviews and leaver events. |
| independence | Reconciliation performed by the assessor from system exports obtained under observation. |
| mandatoryItems | Rights export; Leaver reconciliation |
| acceptableAlternatives | Independent audit sample of the same population and period |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-15. |
| reassessmentTriggers | Access-control system migration; Security incident involving access; Change of security contractor |

**Assessment methods.** RECONCILIATION, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Export critical-zone rights under observation and sample holders.
2. Trace each sampled holder to an approval.
3. Reconcile leavers in the period to revocation timestamps.
4. Review access-review evidence and removal actions.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies wherever the assessed party controls physical access; colocation tenants assess the provider's process for their space through provider evidence.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION

**Failure modes addressed.** Leaver retains access to switchgear room; Contractor credential shared; Access rights accumulate

**Testing safety.** Desk-based assessment; no hazardous testing. Site walk-downs follow the host site induction and are escorted in plant areas.

**UNKNOWN rule.** If the leaver population cannot be obtained, record a U2 UNKNOWN; the OPERATION claim is UNKNOWN.

**Ontology classes.** Safeguard, Threat, EvidenceObject · **Related controls.** MCF-PHY-009, MCF-PHY-014, MCF-SEC-001

**Informative references.** EN 50600-2-5 (security systems); ISO/IEC 27002 (physical entry controls); IEC 60839-11 (electronic access control systems)

### MCF-PHY-014

**Visitor Control** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that visitors, vendors and contractors, including OEM field engineers servicing accelerator systems, are identified, authorised, escorted and supervised in critical spaces.

**Requirement.** The security manager shall require pre-registration, identity verification and host approval for every visitor, shall issue time-limited credentials, and shall require escort in critical-space zones at no more than the declared visitor-to-escort ratio. The facility operator shall link contractor attendance in plant spaces to an approved work order or permit.

**Assessment criteria**

1. Every sampled visitor entry has pre-registration, ID verification and host approval.
2. Visitor credentials expire at the end of the approved visit.
3. Escort ratio in critical zones did not exceed the declared value in sampled visits.
4. Contractor entries to plant spaces trace to an approved work order or permit.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum visitors per escort in critical zones | ratio | 3:1 (illustrative) | Capability profile |

**Minimum evidence**

- Visitor management records
- Credential issue and expiry logs
- Work orders linked to contractor entries
- Observation of a visitor process

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E3 |
| optionalClasses | E1; E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | A sample from the last six months. |
| independence | Sample selected by the assessor. |
| mandatoryItems | Visitor management records |
| acceptableAlternatives | Manual visitor log where electronic system not used, if sequential and complete |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | Visitor system change; Incident involving a visitor |

**Assessment methods.** SAMPLING, OBSERVATION, RECONCILIATION

**Assessment procedure**

1. Sample visitor entries to critical zones.
2. Trace each to pre-registration, ID check and approval.
3. Reconcile contractor entries to work orders.
4. Observe a visitor journey.

**Gate mappings.** None

**Applicability.** Applies to all staffed sites. Unstaffed edge sites apply the work-order linkage element only.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Unescorted vendor in data hall; Contractor working without permit; Credential reused after visit

**Testing safety.** Desk-based assessment; no hazardous testing. Site walk-downs follow the host site induction and are escorted in plant areas.

**UNKNOWN rule.** If visitor records are incomplete for the sample, record a U1 UNKNOWN and a Finding.

**Ontology classes.** Safeguard, Threat · **Related controls.** MCF-PHY-013, MCF-OPS-007, MCF-SUP-021

**Informative references.** ISO/IEC 27002 (physical entry controls); EN 50600-2-5 (security systems)

### MCF-PHY-015

**Surveillance Coverage** · DETECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure video surveillance covers entries to critical zones, critical plant and high-value asset areas at an image quality sufficient for the declared purpose, with retention and integrity supporting investigation.

**Requirement.** The security manager shall define an operational requirement for each camera view stating its purpose (detect, observe, recognise or identify), shall install and maintain cameras to meet it, shall retain recordings for the declared period with integrity protection, and shall verify coverage after layout changes.

**Assessment criteria**

1. An operational requirement lists each critical zone entry and plant area with its purpose category.
2. Sampled camera views meet the image quality for their declared purpose.
3. Recordings are retained for the declared period and the sample retrieves successfully.
4. Camera health monitoring alarms on loss of view and outages are corrected within the declared time.
5. Exported footage has integrity protection (hash or signed export).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Recording retention | days | 90 (illustrative) | Capability profile; local privacy law limits |
| Pixel density for identification views | px/m | 250 | IEC 62676-4 operational requirement categories |

**Minimum evidence**

- Operational requirement document
- Camera layout
- Sample stills per view
- Retention configuration
- Camera health logs

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses |  |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Current configuration; health logs for three months. |
| independence | Stills and retrieval performed under assessor observation. |
| mandatoryItems | Operational requirement; Retention configuration |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | Layout change; VMS upgrade; Security incident |

**Assessment methods.** INSPECTION, SAMPLING, TEST

**Assessment procedure**

1. Review the operational requirement against the zoning plan.
2. Sample views and assess image quality against purpose.
3. Retrieve a recording at the end of the retention window.
4. Review camera health alarms and outage closure.

**Gate mappings.** None

**Applicability.** Applies where surveillance is a declared safeguard; privacy law may limit retention and is recorded as a constraint.

**Lifecycle stages.** DESIGN, BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION

**Failure modes addressed.** Blind spot at generator yard gate; Recordings overwritten before investigation; Camera outage undetected

**Testing safety.** Desk-based assessment; no hazardous testing. Site walk-downs follow the host site induction and are escorted in plant areas.

**UNKNOWN rule.** If retrieval cannot be demonstrated, record a U8 method UNKNOWN for surveillance evidence.

**Ontology classes.** Safeguard, EvidenceObject · **Related controls.** MCF-PHY-009, MCF-PHY-016, MCF-EVA-006

**Informative references.** IEC 62676 series (video surveillance systems); EN 50600-2-5 (security systems)

### MCF-PHY-016

**Alarm Response** · DETECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Demonstrate that intrusion, forced-door, held-door and tamper alarms at critical zones are acknowledged and physically attended within declared times, including at night and when many alarms occur together.

**Requirement.** The security manager shall define acknowledgement and attendance times for each alarm class in critical zones, shall staff and equip the response to meet them, and shall test response by unannounced exercises at the declared interval, including an exercise during concurrent facility alarms.

**Assessment criteria**

1. Alarm classes and target acknowledgement and attendance times are defined.
2. Alarm records for the period show the targets were met for the declared percentage of alarms.
3. At least the declared number of unannounced exercises were run and met attendance targets.
4. One exercise tested response while other facility alarms were active.
5. Missed targets have root cause and corrective action.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Alarm acknowledgement time | s | 60 (illustrative) | Capability profile |
| Attendance time at critical-zone alarm | minutes | 5 (illustrative) | Capability profile |
| Unannounced response exercises | per year | 4 (illustrative) | Capability profile |

**Minimum evidence**

- Alarm response procedure
- Alarm logs with acknowledgement and attendance times
- Exercise records
- Corrective action records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E6 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; EMERGENCY |
| periodCoverage | Twelve months of alarms and exercises, including night shifts. |
| independence | At least one exercise designed and timed by the assessor or an independent party. |
| mandatoryItems | Alarm logs; Exercise records |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | Change of guard force or staffing; Control room relocation; Missed target in exercise |

**Assessment methods.** TEST, SCENARIO_EXERCISE, ANALYSIS

**Assessment procedure**

1. Analyse alarm logs for acknowledgement and attendance times by class.
2. Review exercises for design, unannounced status and results.
3. Conduct or witness an unannounced exercise at a plant-zone door.
4. Review corrective actions for missed targets.

**Gate mappings.** None

**Applicability.** Applies to staffed or remotely monitored sites. Unstaffed sites declare remote-response times and use the same criteria.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, EMERGENCY, DEGRADED

**Failure modes addressed.** Forced-door alarm acknowledged but not attended; Alarm missed during facility alarm flood (AIDCF-004 X11)

**Testing safety.** Exercises are coordinated with the control room supervisor so that the exercise is not mistaken for a real event requiring emergency services; no exercise triggers suppression or EPO circuits.

**UNKNOWN rule.** If attendance times are not recorded, record a U1 UNKNOWN; the EFFECTIVENESS claim is UNKNOWN.

**Ontology classes.** Safeguard, TestRecord, Event · **Related controls.** MCF-PHY-015, MCF-OPS-013, MCF-SEC-019

**Informative references.** EN 50131 series (intrusion and hold-up alarm systems); EN 50600-2-5 (security systems)

## PHY-05 Asset movement and custody

### MCF-PHY-017

**Delivery Controls** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure inbound deliveries of high-value AI hardware, storage media and critical spares are received against an expected manifest, inspected for tampering and held under custody until accepted.

**Requirement.** The facility operator shall receive critical deliveries only against an advance notice and purchase reference, shall inspect seals and packaging for tampering, shall record serial numbers at receipt and shall hold received items in a controlled store until they are accepted into the asset register.

**Assessment criteria**

1. Sampled deliveries trace to advance notice and purchase reference.
2. Seal and packaging inspection is recorded for every sampled critical delivery.
3. Serial numbers recorded at receipt match the shipping manifest and the asset register.
4. Received items are stored in a controlled zone until acceptance.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Inbound critical shipments with seal inspection | % | 100 (illustrative) | Capability profile |

**Minimum evidence**

- Goods-in records
- Seal inspection records
- Asset register entries
- Controlled-store access logs

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E3 |
| optionalClasses | E1; E2 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Six months of receipts. |
| independence | Sample selected by the assessor. |
| mandatoryItems | Goods-in records |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | New logistics provider; Discrepancy or tamper event |

**Assessment methods.** SAMPLING, RECONCILIATION, OBSERVATION

**Assessment procedure**

1. Sample critical deliveries.
2. Trace to notice, inspection, serials and register.
3. Observe the controlled store.

**Gate mappings.** None

**Applicability.** Applies to sites receiving accelerators, storage media, network optics or critical spares.

**Lifecycle stages.** BUILD, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Tampered accelerator module accepted; Serial mismatch undetected; Delivery left in unsecured dock

**Testing safety.** Desk-based assessment; no hazardous testing. Site walk-downs follow the host site induction and are escorted in plant areas.

**UNKNOWN rule.** If receipt records cannot be reconciled to serials, record a U5 UNKNOWN and refer to SUP provenance controls.

**Ontology classes.** AssetInstance, Threat, Safeguard · **Related controls.** MCF-SUP-011, MCF-SUP-010, MCF-PHY-018

**Informative references.** ISO 28000 (security management for the supply chain); ISO/IEC 27002 (delivery and loading areas)

### MCF-PHY-018

**Equipment Movement** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure movement of dense racks and heavy plant within the facility is planned, authorised and executed without exceeding route ratings, damaging live infrastructure or creating tip-over and crush hazards.

**Requirement.** The facility operator shall require a move plan, approved by the facilities engineer, for every movement of a rack or plant item above the declared mass threshold, stating route, route ratings, equipment (skates, tuggers, lifting), crew competence and proximity to live services. The facility operator shall drain or isolate liquid-cooled racks where the OEM requires it before movement.

**Assessment criteria**

1. Every sampled move above threshold has an approved move plan.
2. Move plans reference route ratings from MCF-PHY-003 and floor ratings from MCF-PHY-005.
3. Crew competence for heavy moves is evidenced.
4. Liquid-cooled racks were moved in the OEM-required fluid state.
5. Move incidents (floor damage, near misses) are recorded and investigated.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Rack or plant mass requiring an approved move plan | kg | 1,500 (illustrative) | Capability profile |

**Minimum evidence**

- Move plans
- Crew training records
- Incident records
- Observation of a move

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Twelve months of moves. |
| independence | Sample selected by the assessor. |
| mandatoryItems | Move plans for sampled moves |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material): the decision is capped at CONDITIONALLY_ASSURED with a recorded condition; the UNKNOWN is carried into the gate-level evaluation of CG-04. |
| reassessmentTriggers | New rack type; Move incident; Change of moving contractor |

**Assessment methods.** SAMPLING, DOCUMENT_REVIEW, OBSERVATION

**Assessment procedure**

1. Sample moves from work orders.
2. Check move plans for route and floor rating references.
3. Verify crew competence and fluid-state compliance.
4. Observe a move where scheduled.

**Gate mappings.** CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to sites deploying racks or plant above the mass threshold.

**Lifecycle stages.** BUILD, OPERATE, CHANGE, DECOMMISSION · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Rack tip-over on ramp; Raised floor collapse under rolling load; Coolant spill during move

**Testing safety.** Assessors observe moves from outside the exclusion zone set by the move supervisor and never assist.

**UNKNOWN rule.** If move plans are missing for the sample, record a U1 UNKNOWN and a Finding.

**Ontology classes.** Hazard, Safeguard, AssetInstance · **Related controls.** MCF-PHY-003, MCF-PHY-006, MCF-OPS-006

**Informative references.** Rack OEM installation and relocation guides; National manual-handling and lifting regulations

### MCF-PHY-019

**Media Custody** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure storage media holding training data, checkpoints or model weights are inventoried and in unbroken custody whenever they are removed from service, in transit, under repair or awaiting destruction.

**Requirement.** The facility operator shall maintain a serialised inventory of data-bearing media outside production service, shall record each custody transfer with time, person and location, shall store media in a controlled container or room, and shall reconcile the inventory at the declared interval. The data owner shall define which media classes require encryption verification before leaving the controlled store.

**Assessment criteria**

1. Every data-bearing device removed from service in the sample appears in the custody inventory.
2. Custody transfers are recorded without gaps from removal to final disposition.
3. Inventory reconciliation at the declared interval shows no unexplained missing media.
4. Failed drives returned to OEMs under RMA follow the data owner's rule (retain, sanitise or encrypt).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Media custody inventory reconciliation interval | days | 30 (illustrative) | Capability profile |

**Minimum evidence**

- Custody inventory
- Transfer logs
- Reconciliation records
- RMA records with media disposition

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Twelve months. |
| independence | Reconciliation reperformed by the assessor for a sample. |
| mandatoryItems | Custody inventory; Reconciliation records |
| acceptableAlternatives |  |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | Missing media; Change of RMA provider; New media type |

**Assessment methods.** RECONCILIATION, REPERFORMANCE, SAMPLING

**Assessment procedure**

1. Sample drive removals from storage health and ticket records.
2. Trace each to the custody inventory and transfers.
3. Reperform a reconciliation of the controlled store.
4. Review RMA disposition against the data owner's rule.

**Gate mappings.** None

**Applicability.** Applies to all data-bearing media in the boundary, including accelerator node local NVMe.

**Lifecycle stages.** OPERATE, DECOMMISSION · **Operating states.** NORMAL, MAINTENANCE, RECOVERY

**Failure modes addressed.** Drive with model weights shipped under RMA unencrypted; Media missing from store; Custody gap during transit

**Testing safety.** Desk-based assessment; no hazardous testing. Site walk-downs follow the host site induction and are escorted in plant areas.

**UNKNOWN rule.** If any media cannot be accounted for, record a Finding; if the inventory cannot be reconciled, record a U5 UNKNOWN.

**Ontology classes.** AssetInstance, Threat, EvidenceObject · **Related controls.** MCF-PHY-020, MCF-STO-024, MCF-STO-023

**Informative references.** NIST SP 800-88 (media sanitisation); IEEE 2883 (storage sanitisation); ISO/IEC 27002 (media handling)

### MCF-PHY-020

**Decommissioning Custody** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that equipment leaving the facility at end of life, including accelerators, servers, storage and network devices, is sanitised or destroyed to the declared standard with verified certificates, and that decommissioning does not disturb live infrastructure.

**Requirement.** The facility operator shall decommission equipment only under an approved decommissioning work order that identifies the asset, its data-bearing components, dependent power and cooling connections and the sanitisation or destruction method. The facility operator shall obtain a certificate per serial from any third-party disposal provider and shall reconcile certificates to the decommissioning list.

**Assessment criteria**

1. Each sampled decommissioned asset has an approved work order.
2. Sanitisation or destruction method matches the data owner's classification.
3. Certificates exist per serial and reconcile to the decommissioning list.
4. Isolation of power and liquid connections followed the approved method statement.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Decommissioned data-bearing devices with per-serial certificate | % | 100 (illustrative) | Capability profile |

**Minimum evidence**

- Decommissioning work orders
- Sanitisation or destruction certificates
- Reconciliation of certificates to asset list
- Isolation method statements

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Twelve months of decommissioning. |
| independence | Certificate reconciliation by the assessor. |
| mandatoryItems | Certificates per serial |
| acceptableAlternatives | Witnessed on-site destruction records |
| unknownEffect | US3 (Material) where the control result could change a decision condition, otherwise US2 (Moderate) with a confidence ceiling of CONF-2 for the affected claims. |
| reassessmentTriggers | Change of disposal provider; Large refresh programme; Certificate discrepancy |

**Assessment methods.** RECONCILIATION, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Sample decommissioned assets from the register.
2. Trace each to work order, method and certificate.
3. Review isolation evidence for liquid-cooled equipment.

**Gate mappings.** None

**Applicability.** Applies to all decommissioning in the boundary.

**Lifecycle stages.** DECOMMISSION · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Unsanitised drive leaves site; Wrong rack isolated during decommissioning; Certificate missing

**Testing safety.** Assessors do not witness isolations inside arc-flash boundaries; liquid disconnection is observed from outside the drip zone.

**UNKNOWN rule.** If certificates cannot be reconciled, record a U1 UNKNOWN per unreconciled serial and a Finding.

**Ontology classes.** AssetInstance, Safeguard · **Related controls.** MCF-PHY-019, MCF-ENV-020, MCF-CMP-024

**Informative references.** NIST SP 800-88 (media sanitisation); IEEE 2883 (storage sanitisation)

## PHY-06 Fire, life safety and emergency interfaces

### MCF-PHY-021

**Fire Detection** · DETECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Demonstrate that fire detection in IT, electrical, battery and plant spaces detects incipient fires early enough for safe evacuation and for controlled response before a fire disables redundant infrastructure, accounting for high airflow and liquid-cooled hall conditions.

**Requirement.** The fire safety manager shall provide detection designed for the airflow conditions of each space: very early warning aspirating smoke detection in high-airflow IT halls and electrical rooms, and off-gas or appropriate gas detection plus heat and smoke detection in lithium-ion battery rooms and enclosures. The fire safety manager shall test detection functionally at the declared interval, including smoke transport time for aspirating systems, and shall ensure alarms are received at a continuously staffed location.

**Assessment criteria**

1. Detection design for each space states the detection type and how high airflow was accounted for.
2. Lithium-ion battery rooms and BESS enclosures have off-gas detection as specified by the battery safety assessment, in addition to smoke and heat detection.
3. Functional tests at the declared interval cover all detectors or sampling points, with aspirating transport times within the design value.
4. Detection alarms are received and acknowledged at a continuously staffed location, demonstrated in the period.
5. Impairments are recorded with compensating measures and closed within the declared time.
6. Acceptance or periodic inspection by the authority having jurisdiction or a certified inspector is current.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Aspirating detection maximum transport time | s | per design; not greater than the EN 54-20 class limit | EN 54-20 (aspirating smoke detectors); system design |
| Detection functional test interval | months | 12 (illustrative) | NFPA 72 or national fire code; capability profile |
| Maximum detection impairment duration without compensating measure | hours | 0 (illustrative) | Capability profile |

**Minimum evidence**

- Detection design and cause-and-effect matrix
- Functional test reports with transport times
- Battery safety assessment specifying off-gas detection
- Alarm receipt records
- Impairment log
- AHJ or certified inspector reports

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E4; E5 |
| optionalClasses | E3 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Most recent full test cycle and twelve months of impairments. |
| independence | Functional test performed or witnessed by a certified fire-system contractor or inspector independent of the design author. |
| mandatoryItems | Functional test reports; AHJ or certified inspection record |
| acceptableAlternatives | Insurer engineering survey including witnessed detection tests |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-04 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Change of airflow regime (containment, liquid-cooling retrofit); New battery installation; Detector or panel replacement; Fire or false-alarm incident |

**Assessment methods.** DOCUMENT_REVIEW, TEST, INSPECTION, OBSERVATION

**Assessment procedure**

1. Review detection design for airflow and battery hazards.
2. Check test reports for coverage, transport times and defects.
3. Witness a smoke or transport-time test at a sampled point.
4. Verify alarm receipt and acknowledgement at the staffed location.
5. Review impairment records and compensating measures.

**Gate mappings.** CG-04 Life safety and hazardous energy (CRITICAL); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to all facilities. Colocation tenants rely on provider test evidence and witness where contractually permitted.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION

**Failure modes addressed.** Smoke diluted by high airflow below detector threshold; Battery off-gas undetected before thermal runaway; Aspirating pipe blocked; Alarm not received during control-room outage

**Testing safety.** Detection tests use approved test aerosols or smoke sources; the fire safety manager isolates suppression release and notifies the alarm receiving centre before testing, and restores after. No test is performed in a battery room during a known battery fault.

**UNKNOWN rule.** If functional test evidence for detection in a battery room or IT hall is missing or older than the interval, record a US4 UNKNOWN against CG-04; testing that depends on the room (for example load tests) is not authorised until resolved.

**Ontology classes.** Safeguard, Hazard, TestRecord · **Related controls.** MCF-PHY-022, MCF-PHY-010, MCF-POW-010, MCF-ENV-017

**Informative references.** NFPA 72 (fire alarm and signalling); EN 54 series (fire detection and fire alarm systems); NFPA 75 (protection of IT equipment); NFPA 855 (stationary energy storage systems); FM Global Property Loss Prevention Data Sheets (data centres; energy storage)

### MCF-PHY-022

**Suppression Interfaces** · CORRECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Demonstrate that suppression systems and their interfaces with power, cooling, ventilation and control systems act as designed, so that suppression is effective without causing an avoidable loss of AI capability or an unsafe condition.

**Requirement.** The fire safety manager shall maintain a cause-and-effect matrix covering every interface between detection, suppression (sprinkler, pre-action, water mist, gaseous agent) and other systems, including HVAC shutdown, damper closure, CDU and pump behaviour, power isolation and door release. The fire safety manager shall test the matrix end to end at the declared interval, shall verify room integrity for gaseous systems by enclosure test, and shall confirm that fire-mode actions do not stop liquid cooling to unaffected areas unless the fire strategy requires it.

**Assessment criteria**

1. A cause-and-effect matrix exists and matches the configured logic in the fire panel and BMS.
2. End-to-end interface tests at the declared interval demonstrate each output, with deviations closed.
3. Gaseous-agent rooms pass an enclosure integrity test demonstrating the design hold time.
4. Fire-mode effects on liquid cooling and CDUs are defined, and unaffected halls keep cooling in the test.
5. Suppression agent quantity and cylinder pressure are verified at the declared interval.
6. Water-based suppression in IT spaces is pre-action or otherwise protected against inadvertent discharge, where the fire strategy requires.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Gaseous agent design hold time | minutes | 10 (illustrative) | NFPA 2001 or ISO 14520 design practice; fire engineer's design |
| Enclosure integrity test interval | months | 12 (illustrative) | Capability profile; agent standard |

**Minimum evidence**

- Cause-and-effect matrix
- Fire panel and BMS logic exports
- End-to-end interface test reports
- Enclosure integrity test reports
- Agent quantity and cylinder inspection records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E4; E5 |
| optionalClasses | E3 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; EMERGENCY |
| periodCoverage | Most recent full interface test and enclosure test within interval. |
| independence | Interface tests witnessed by a party independent of the fire contractor (assessor, insurer or AHJ). |
| mandatoryItems | Cause-and-effect matrix; End-to-end interface test report; Enclosure integrity test report |
| acceptableAlternatives | Integrated systems test (IST) report where it exercises the full matrix |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-04 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | BMS or fire panel logic change; Liquid-cooling installation; Room alteration affecting integrity; Discharge event |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, TEST, OBSERVATION

**Assessment procedure**

1. Reconcile the matrix to fire panel and BMS logic exports.
2. Review end-to-end test reports for coverage and deviations.
3. Witness an interface test where scheduled, including CDU behaviour.
4. Review enclosure integrity results against design hold time.
5. Confirm agent inventory and cylinder inspections.

**Gate mappings.** CG-04 Life safety and hazardous energy (CRITICAL); CG-06 Thermal continuity (SUPPORTING); CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies wherever suppression is installed; partial applicability where only sprinklers exist (enclosure test not applicable).

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, EMERGENCY, MAINTENANCE

**Failure modes addressed.** Fire alarm stops all CDUs site-wide; Gaseous agent leaks out before hold time; Damper fails open; Inadvertent discharge damages storage (acoustic) or IT (water)

**Testing safety.** End-to-end tests are performed with agent release physically disabled and verified disabled before testing; HVAC and CDU interlocks are tested under a method statement approved by the facility operator with thermal contingency in place. Gaseous rooms are cleared and posted before enclosure tests; no assessor is present during any live discharge.

**UNKNOWN rule.** If the matrix cannot be reconciled to configured logic, or no end-to-end test is current, record a US4 UNKNOWN against CG-04 and refer the cooling interlock gap to CG-06.

**Ontology classes.** Safeguard, Interface, TestRecord, Hazard · **Related controls.** MCF-PHY-021, MCF-PHY-024, MCF-ENV-004, MCF-THM-021

**Informative references.** NFPA 2001 (clean agent systems); ISO 14520 series (gaseous fire-extinguishing systems); NFPA 13 (sprinkler systems); NFPA 75 (protection of IT equipment)

### MCF-PHY-023

**Egress and Emergency Access** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure occupants of data halls, plant rooms and battery rooms can escape safely and emergency responders can gain access, including in dense hot-aisle/cold-aisle containment, liquid-cooled halls with overhead manifolds and spaces protected by gaseous agents.

**Requirement.** The fire safety manager shall maintain egress routes from every occupied space within the travel distances of the fire strategy, shall ensure secured doors on escape routes release on fire alarm or by local override, shall provide pre-discharge warning and abort controls for gaseous systems, and shall provide emergency responders with plans, hazard information (batteries, refrigerants, coolants, arc-flash hazards) and access means.

**Assessment criteria**

1. Travel distances and exit widths in sampled spaces meet the fire strategy, including inside containment.
2. Containment doors and escape-route doors release on fire alarm and by local override, demonstrated.
3. Gaseous-agent spaces have audible and visual pre-discharge warnings and abort controls at exits.
4. Emergency responder information packs exist and include battery, refrigerant and electrical hazards.
5. Egress routes are unobstructed during inspection.
6. Emergency lighting is tested at the declared interval.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Emergency lighting full-duration test interval | months | 12 (illustrative) | National emergency lighting standard (e.g. EN 50172); capability profile |

**Minimum evidence**

- Fire strategy egress plans
- Door release test records
- Pre-discharge warning test records
- Responder information pack
- Emergency lighting test records
- Inspection notes

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E3; E4; E5 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; EMERGENCY; MAINTENANCE |
| periodCoverage | Twelve months of tests; inspection at assessment. |
| independence | Fire authority or certified inspector acceptance current; inspection by the assessor. |
| mandatoryItems | Egress plans; Door release test; Responder information pack |
| acceptableAlternatives |  |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-04 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Containment installation or change; Layout change; New battery or refrigerant system; Fire authority visit with findings |

**Assessment methods.** INSPECTION, DOCUMENT_REVIEW, TEST

**Assessment procedure**

1. Walk egress routes from the furthest point in sampled halls and plant rooms.
2. Test a sample of containment and escape doors for release.
3. Review gaseous warning and abort tests.
4. Review the responder pack for current hazards.

**Gate mappings.** CG-04 Life safety and hazardous energy (CRITICAL)

**Applicability.** Applies to all occupied facilities. Unoccupied modular units declare responder access only.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION

**Failure modes addressed.** Escape blocked by containment doors that lock on power loss; Responders unaware of lithium-ion BESS; Abort control unreachable

**Testing safety.** Door release tests are coordinated with security so that zone protection is maintained; tests that drop fire alarm outputs follow the fire safety manager's isolation procedure.

**UNKNOWN rule.** If egress in containment or battery rooms cannot be verified, record a US4 UNKNOWN for CG-04.

**Ontology classes.** Safeguard, Hazard · **Related controls.** MCF-PHY-021, MCF-PHY-022, MCF-POW-013

**Informative references.** NFPA 101 (life safety code) or national building regulations; EN 50172 (emergency escape lighting); NFPA 2001 (clean agent systems)

### MCF-PHY-024

**Emergency Shutdown Governance** · DIRECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure emergency power-off (EPO) and other emergency shutdown functions protect people and responders while being protected against inadvertent or malicious activation that would cause an uncontrolled shutdown of AI capability.

**Requirement.** The facility owner shall define the scope of each emergency shutdown function (EPO, battery disconnect, fuel shut-off, CDU emergency stop) and the authority to activate it. The facility operator shall protect activation devices against inadvertent operation (covers, two-action operation, location), shall verify by test at the declared interval that each function isolates exactly its declared scope, and shall review any activation as a significant incident.

**Assessment criteria**

1. Each emergency shutdown function has a documented scope, activation authority and legal basis (code requirement or fire strategy).
2. Activation devices have protection against inadvertent operation and are labelled with scope.
3. Functional tests at the declared interval show each function isolates exactly its declared scope (no more, no less).
4. Remote or software activation paths, where present, are identified and protected under SEC controls.
5. Activations in the period were investigated with lessons applied.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Emergency shutdown functional test interval | months | 12 (illustrative) | Capability profile; applicable electrical code |

**Minimum evidence**

- Emergency shutdown scope schedule
- Activation device inspection
- Functional test reports
- Incident records for activations
- Control logic exports for remote paths

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E4; E5 |
| optionalClasses | E3 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; EMERGENCY; MAINTENANCE |
| periodCoverage | Most recent test cycle and twelve months of activations. |
| independence | Test witnessed by an independent electrical or fire engineer. |
| mandatoryItems | Scope schedule; Functional test reports |
| acceptableAlternatives | Test during integrated systems test with recorded scope verification |
| unknownEffect | US4 (Critical): an UNKNOWN result on this gate-critical control sets CG-04 to UNKNOWN and caps the decision at LIMITED or INCONCLUSIVE per the gate ceiling until dispositioned. |
| reassessmentTriggers | Change in electrical distribution or CDU controls; Activation event; Code change |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, TEST

**Assessment procedure**

1. Review scope schedule and legal basis.
2. Inspect a sample of activation devices for protection and labelling.
3. Review functional test evidence for scope correctness.
4. Identify remote activation paths and confirm protection.

**Gate mappings.** CG-04 Life safety and hazardous energy (CRITICAL); CG-07 Critical control-system integrity (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies wherever EPO or emergency shutdown functions are installed; where codes do not require EPO and none is installed, battery and fuel shut-off elements still apply.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION

**Failure modes addressed.** Unprotected EPO button pressed in error; EPO scope wider than labelled; Remote EPO path reachable from IT network; Battery disconnect fails to isolate

**Testing safety.** EPO and shutdown function tests are hazardous to capability: they are performed only during an approved shutdown window or with the load transferred, under a method statement approved by the facility owner's authorised engineer, with written authorisation and a rollback plan. Assessors witness and do not operate.

**UNKNOWN rule.** If the actual scope of an EPO function has never been verified by test, record a US4 UNKNOWN against CG-04 and an associated UNKNOWN on CG-09 for unbounded shutdown scope.

**Ontology classes.** Safeguard, Interface, Hazard, TestRecord · **Related controls.** MCF-PHY-022, MCF-POW-023, MCF-SEC-005

**Informative references.** NFPA 70 (information technology equipment provisions); NFPA 75 (protection of IT equipment); IEC 60204-1 (emergency stop principles, by analogy)
