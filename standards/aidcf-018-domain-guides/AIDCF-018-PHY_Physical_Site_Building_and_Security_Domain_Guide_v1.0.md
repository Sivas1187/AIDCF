# AIDCF-018-PHY Physical Site, Building and Security Infrastructure Domain Guide

## Document control

| Field | Value |
|---|---|
| Document ID | AIDCF-018-PHY |
| Title | Physical Site, Building and Security Infrastructure Domain Guide |
| Parent artifact | AIDCF-018 Domain Guides |
| Domain | PHY — Physical Site, Building and Security Infrastructure |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Control source | AIDCF-007A Canonical Master Control Registry, controls MCF-PHY-001 to MCF-PHY-024; this guide agrees exactly with the machine-readable control records |
| Depends on | AIDCF-003, AIDCF-004, AIDCF-007A, AIDCF-008, AIDCF-009, AIDCF-010, AIDCF-013, AIDCF-014 |
| Requirement prefix | DG-PHY-REQ-NNN |

### Revision history

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-10 | Initial issue: domain guide for the 24 PHY controls, gate linkage, parameters, evidence and testing-safety expectations. |

## 1 Purpose and scope

This guide explains how the PHY domain of AIDCF-007A is applied when assessing whether an AI Capability Instance can achieve its declared Service Outcomes. It covers the site, the building and its structure, physical zoning, access and surveillance, custody of assets and media, and fire, life-safety and emergency interfaces.

The PHY domain answers four questions for the assurance case:

1. Is the site exposed to natural or man-made events that could disable redundant infrastructure together?
2. Can the building physically carry, house and separate the dense, liquid-cooled and battery-laden equipment of AI capability?
3. Are people, plant and AI assets protected against unauthorised access, theft and tampering?
4. Will fire be detected and controlled, and people escape, without the emergency response itself causing an avoidable loss of capability?

In scope: site hazard assessment and external exposures; logistics routes; adjacent occupancies; structural capacity, rack loading, anchorage, vibration and envelope; security, fire, water and tenant zoning; physical access control, visitor management, video surveillance and alarm response; delivery, movement, media custody and decommissioning; fire detection, suppression interfaces, egress and emergency shutdown.

Out of scope, with interfaces: digital access to physical-security systems (SEC), electrical arc-flash and battery-system hazards (POW), refrigerants and battery materials handling (ENV), leak detection and liquid isolation functions (THM), hardware provenance (SUP).

This guide is informative except where a requirement carries a DG-PHY-REQ identifier.

## 2 Why this domain matters for AI capability

Physical design assumptions that were adequate for enterprise data centres are being exceeded by AI deployments in ways that are easy to miss.

**Mass and wet mass.** Rack-scale accelerator systems with integrated liquid-cooling manifolds weigh far more than legacy racks, and the operating mass includes coolant in cold plates, manifolds, rack-level CDUs and the secondary pipework above or below the rack. Immersion tanks concentrate several tonnes on a small footprint. Structural capacity statements prepared for air-cooled halls frequently use dry shipping mass or uniformly distributed loads that do not represent concentrated rack positions (MCF-PHY-005 (Structural Capacity), MCF-PHY-006 (Rack Loading)).

**Logistics.** A fully populated rack shipped as one integrated unit must travel from dock to position through doors, lifts, ramps and corridors rated for it. A site that cannot receive the rack without dismantling it has a capability constraint that may only be discovered at delivery (MCF-PHY-003 (Access and Logistics)).

**Liquid in the white space.** Liquid cooling brings water, glycol or dielectric fluid into rooms that also contain busway and PDUs at high current. Water zoning — the spatial and physical separation of liquid-bearing systems from electrical systems — becomes a first-order design control (MCF-PHY-011 (Water Zones)).

**Lithium-ion everywhere.** Lithium-ion UPS strings, BESS and rack battery backup units place stored chemical energy throughout the facility. Detection must find off-gassing before thermal runaway, compartments must contain a battery fire, and responders must know where the batteries are (MCF-PHY-010 (Fire Zones), MCF-PHY-021 (Fire Detection), MCF-PHY-023 (Egress and Emergency Access)).

**Fire response versus cooling continuity.** Fire-mode logic designed for air cooling (stop air handlers, close dampers) may, if applied to liquid cooling, stop CDUs and pumps in unaffected halls, turning a small local fire into a site-wide thermal event for accelerators with seconds of thermal inertia. Cause-and-effect matrices must be re-engineered for liquid-cooled halls (MCF-PHY-022 (Suppression Interfaces)).

**Asset value and data sensitivity.** Accelerator modules are high-value, portable and attractive to theft; local NVMe in training nodes may hold model weights, checkpoints or training data. Custody of media and decommissioned hardware is therefore both a security and a data-protection matter (MCF-PHY-019 (Media Custody), MCF-PHY-020 (Decommissioning Custody)).

**Plant as the soft target.** The physical routes to disabling AI capability often run through power and cooling plant — generator yards, fuel fill points, MV substations, dry-cooler compounds — rather than through the data hall. Zoning must protect plant at least as well as the halls it serves (MCF-PHY-009 (Security Zones)).

## 3 Reference patterns and variants

| Pattern (AIDCF-013) | PHY characteristics | PHY questions that dominate |
|---|---|---|
| Single-site training facility | Purpose-built halls; slab-on-grade or structural slab; dedicated plant yards | Structural capacity for wet mass; fire zones separating A/B paths |
| Hyperscale campus | Multiple buildings; shared campus perimeter; central plant | Site hazards affecting whole campus; perimeter and hostile vehicle mitigation; logistics for continuous deployments |
| Colocation deployment | Tenant suite or cage in provider building | Tenant segregation; disclosure of shared risers and plant; access by provider staff |
| Modular facility | Prefabricated modules on prepared ground | Anchorage and flood level of modules; inter-module fire separation; module access for replacement |
| Liquid-cooled high-density cluster | Slab-mounted racks, overhead manifolds and busway | Water zones; rack loading; equipment movement |
| Brownfield retrofit | Existing building, often raised floor, re-purposed | Raised-floor and slab capacity; fire strategy currency; envelope condition |
| Edge inference estate | Small rooms in third-party premises | Adjacent risk; access by non-specialist staff; theft of hardware |

Security zoning variants are concentric (perimeter → building → secure corridor → critical space → cage/rack), with critical plant assigned to critical-space or higher zones. Fire-protection variants include very early warning aspirating detection with pre-action sprinklers, gaseous agents (inert or chemical) with enclosure integrity, and water mist; lithium-ion rooms add off-gas detection and explosion control (deflagration venting or prevention), guided by large-scale fire test data such as UL 9540A.

## 4 Required functions and capability linkage

| Required Function | Implemented by | Controls |
|---|---|---|
| Locate capability where site-wide hazards are within design protection | Site, earthworks, flood defences, perimeter | MCF-PHY-001, MCF-PHY-002, MCF-PHY-003, MCF-PHY-004 |
| Carry, restrain and enclose equipment | Structure, raised floor, anchorage, envelope | MCF-PHY-005, MCF-PHY-006, MCF-PHY-007, MCF-PHY-008 |
| Separate hazards and fault domains spatially | Security, fire, water and tenant zones | MCF-PHY-009, MCF-PHY-010, MCF-PHY-011, MCF-PHY-012 |
| Restrict and observe physical access | Access control, visitor management, video, alarm response | MCF-PHY-013, MCF-PHY-014, MCF-PHY-015, MCF-PHY-016 |
| Maintain custody of assets and data-bearing media | Goods-in, movement, custody store, decommissioning | MCF-PHY-017, MCF-PHY-018, MCF-PHY-019, MCF-PHY-020 |
| Detect and control fire and protect life | Detection, suppression, egress, emergency shutdown | MCF-PHY-021, MCF-PHY-022, MCF-PHY-023, MCF-PHY-024 |

Capability linkage: the physical layer rarely appears directly in a Service Outcome, but it determines whether redundant power, cooling and network paths are truly independent (fire, water, flood and intrusion as common-mode initiators) and whether recovery is possible (logistics for replacement plant, responder access). Assessors should therefore link PHY controls to the FaultDomain records of POW, THM and NET, and to recovery dependencies in RES.

**DG-PHY-REQ-001** The assessor shall overlay the redundant power, cooling and network paths of the declared architecture onto the fire, water and security zone plans, and shall record each zone that hosts both elements of a redundant pair as a shared FaultDomain or record a U5 UNKNOWN where the overlay cannot be produced.

## 5 Dependencies, fault domains and common-mode concerns

Physical common-mode initiators are among the most severe because they act on everything in a space at once.

- **Flood and water**: a single flood level, roof failure or burst main can affect both A and B plant if both are at grade or below the same roof (MCF-PHY-001, MCF-PHY-008, MCF-PHY-011).
- **Fire**: shared risers, cable galleries and plant rooms are classic single points where both paths meet (AIDCF-004 X09). Compartmentation is the containment boundary (MCF-PHY-010).
- **External events**: an explosion at an adjacent hazardous installation, a vehicle impact, or a wildfire smoke plume can affect both utility intakes or all heat-rejection plant (MCF-PHY-002).
- **Seismic**: all unanchored equipment of a class responds together (MCF-PHY-007).
- **Physical intrusion**: one breach of a weak plant-zone boundary can reach both generator yards (AIDCF-004 X16; MCF-PHY-009).
- **Emergency shutdown**: an EPO whose actual scope is wider than labelled is a deliberately engineered common-mode switch (MCF-PHY-024).
- **Shared landlord or provider elements**: in colocation, risers, roofs and plant may be shared with other tenants whose activities and incidents propagate (MCF-PHY-004, MCF-PHY-012).

Physical dependencies also include external services: fire and rescue response time, police response for alarm escalation, specialist contractors for heavy lifts, and fuel and water delivery routes.

## 6 Threats, hazards and failure scenarios with propagation paths

| Scenario | Propagation path | Primary safeguards (controls) |
|---|---|---|
| Fire disables paired routes (X09) | Cable fire in shared riser → both A and B feeds and fibre routes damaged → loss of hall power and network → outcome loss for weeks | MCF-PHY-010, MCF-PHY-021, MCF-PHY-022 |
| Lithium-ion thermal runaway | Cell fault in rack BBU or UPS string → off-gas not detected → thermal runaway → deflagration → fire spreads to adjacent UPS room → both UPS paths lost; life-safety risk | MCF-PHY-021, MCF-PHY-010, MCF-PHY-023; MCF-POW-010 |
| Fire-mode cooling interlock | Smoke detected in one hall → cause-and-effect stops all CDUs site-wide → accelerators overheat in all halls → mass shutdown | MCF-PHY-022 |
| Inadvertent EPO | Visitor or operator presses unprotected EPO → hall de-energised → uncontrolled shutdown | MCF-PHY-024, MCF-PHY-014 |
| Structural overload | Retrofit liquid cooling raises wet mass → slab deflection and cracking → enforced decant of hall | MCF-PHY-005, MCF-PHY-006 |
| Water ingress (D2 family) | Roof drain blocks in storm → water enters above switchgear → arc fault → path lost | MCF-PHY-008, MCF-PHY-011 |
| Liquid leak with detection gap (X03) | Quick-disconnect fails → coolant reaches busway tap-off → fault → row lost | MCF-PHY-011 |
| Flood exceeds design (X20) | Extreme rainfall above design → generator yard and MV intake flooded → no utility, no generation | MCF-PHY-001; MCF-ENV-023 |
| Unauthorised entry / insider sabotage | Leaver retains access → enters generator yard → disables fuel transfer → generators stop during later outage | MCF-PHY-009, MCF-PHY-013, MCF-PHY-016 |
| Asset removal | Accelerator modules removed during RMA without custody → theft and data exposure | MCF-PHY-017, MCF-PHY-019, MCF-PHY-020 |
| Heavy move incident | Loaded rack tips on ramp → injury; damaged manifolds leak | MCF-PHY-018, MCF-PHY-003 |
| Emergency-access conflict | Security locks on containment doors fail secure on power loss → occupants trapped | MCF-PHY-023 |

## 7 Safeguards

- **Prevent**: site selection with quantified hazard levels and freeboard; perimeter stand-off and rated hostile vehicle mitigation; structural capacity with utilisation thresholds; anchorage to seismic design level; routing of liquids away from electrical equipment; compartmentation of redundant paths and battery rooms; identity-based access with multi-factor authentication; delivery and custody controls; protected EPO devices.
- **Detect**: aspirating smoke detection designed for high airflow; off-gas detection in battery spaces; leak detection in water zones; intrusion detection and video at zone boundaries; custody reconciliations.
- **Contain**: fire-rated compartments and fire-stopping; drip trays, bunding and drainage; zone boundaries without bypass routes; pre-action sprinklers or gaseous systems with verified enclosure integrity.
- **Correct**: cause-and-effect logic tested end to end; alarm response within declared times; impairment management with compensating measures.
- **Recover**: replacement routes for plant; responder information; decant and relocation plans for halls (with RES).

## 8 Critical-gate linkage

| Gate | Name | CRITICAL controls (this domain) | SUPPORTING controls (this domain) |
|---|---|---|---|
| CG-02 | Boundary and architecture integrity | none | MCF-PHY-001, MCF-PHY-005, MCF-PHY-012 |
| CG-03 | Critical dependency visibility | none | MCF-PHY-001, MCF-PHY-002, MCF-PHY-004 |
| CG-04 | Life safety and hazardous energy | MCF-PHY-021, MCF-PHY-022, MCF-PHY-023, MCF-PHY-024 | MCF-PHY-001, MCF-PHY-005, MCF-PHY-006, MCF-PHY-010, MCF-PHY-011, MCF-PHY-018 |
| CG-06 | Thermal continuity | none | MCF-PHY-008, MCF-PHY-022 |
| CG-07 | Critical control-system integrity | none | MCF-PHY-022, MCF-PHY-024 |
| CG-09 | Failure containment | MCF-PHY-010 | MCF-PHY-002, MCF-PHY-007, MCF-PHY-009, MCF-PHY-011, MCF-PHY-021, MCF-PHY-024 |
| CG-10 | Recovery readiness | none | MCF-PHY-003 |
| CG-13 | Responsibility and authority | none | MCF-PHY-012 |
| CG-14 | Change control | none | MCF-PHY-006 |
| CG-15 | Integrated digital authority over infrastructure | none | MCF-PHY-009, MCF-PHY-013 |

Notes on the mapping:

- **CG-04** (Life safety and hazardous energy) is carried in PHY by fire detection (MCF-PHY-021), suppression interfaces (MCF-PHY-022), egress and emergency access (MCF-PHY-023) and emergency shutdown governance (MCF-PHY-024). Each is CRITICAL because its failure directly defeats protection of life. The CG-04 evidence profile in AIDCF-008 Part XIII requires E1+E4+E5 at S4, which is why these controls require independent (E5) evidence such as authority-having-jurisdiction acceptance or certified inspection.
- **CG-09** (Failure containment) depends on fire compartmentation separating redundant paths (MCF-PHY-010, CRITICAL); water, security and seismic separation are SUPPORTING.
- **CG-02** (Boundary and architecture integrity) is informed by site hazard assessment, structural capacity and tenant segregation; these are SUPPORTING because CG-02's decisive criteria (boundary approval and as-built reconciliation) are carried by architecture and boundary controls in other domains.
- **CG-15** is informed by physical access control (MCF-PHY-013) and zoning (MCF-PHY-009), because physical access to control rooms, EPMS/BMS servers and consoles is part of authority over infrastructure.

**DG-PHY-REQ-002** Where the assessment boundary includes occupied facilities, the assessor shall evaluate CG-04 using every in-scope CRITICAL PHY control and shall not record CG-04 PASS on the basis of a fire certificate or insurer letter alone without the control-level results.

**DG-PHY-REQ-003** The assessor shall record the gate-level evaluation required for every SUPPORTING PHY control that is NONCONFORMING before a gate PASS is recorded.

## 9 Capability-profile parameters

Values marked illustrative show order of magnitude only. Unlabelled values are attributed to the cited source family. Site-specific structural, hazard and fire values must come from the competent engineer of record and the fire strategy.

| Control | Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|---|
| MCF-PHY-001 | Design flood annual exceedance probability for critical plant | % per year | 0.1 (illustrative) | Capability profile; national flood-risk mapping commonly publishes 1% and 0.1% AEP extents |
| MCF-PHY-001 | Freeboard above design flood level for critical plant | mm | 300 (illustrative) | Capability profile; site flood-risk assessment |
| MCF-PHY-001 | Hazard assessment review interval | months | 36 (illustrative) | Capability profile |
| MCF-PHY-002 | External exposure assessment radius | km | 2 (illustrative) | Capability profile; threat assessment |
| MCF-PHY-002 | Hostile vehicle mitigation rating | vehicle mass / impact speed | 7,500 kg at 48 km/h (illustrative) | Threat assessment; rating per IWA 14-1 or PAS 68 test classification |
| MCF-PHY-002 | External exposure review interval | months | 12 (illustrative) | Capability profile |
| MCF-PHY-003 | Heaviest declared delivered item on IT route (crated rack) | kg | 3,000 (illustrative) | Capability profile; rack OEM shipping data |
| MCF-PHY-003 | Independent access routes for fuel and emergency vehicles | count | 2 (illustrative) | Capability profile; emergency services consultation |
| MCF-PHY-004 | Adjacent-risk register review interval | months | 12 (illustrative) | Capability profile |
| MCF-PHY-005 | Design uniformly distributed live load, data hall | kN/m² | 20 (illustrative) | Structural engineer of record; capability profile for dense liquid-cooled racks |
| MCF-PHY-005 | Planned-load utilisation threshold requiring structural re-check | % of rated capacity | 80 (illustrative) | Capability profile |
| MCF-PHY-006 | Maximum operating mass per rack position | kg | 2,000 (illustrative) | Structural capacity statement; capability profile |
| MCF-PHY-006 | Rack-load reconciliation sample | % of positions | 10 (illustrative) | Assessment sampling plan |
| MCF-PHY-007 | Transmitted vibration limit at IT equipment | mm/s RMS | per most restrictive OEM specification | OEM installation requirements |
| MCF-PHY-008 | Envelope inspection interval | months | 6 (illustrative) | Capability profile; roofing guidance |
| MCF-PHY-009 | Authentication factors at critical-space zone entry | count | 2 (illustrative) | Capability profile; threat assessment |
| MCF-PHY-010 | Fire resistance between compartments holding redundant paths | minutes | 120 (illustrative) | Fire strategy; national building regulations; capability profile |
| MCF-PHY-010 | Fire-stopping inspection sample per interval | % of penetrations | 20 (illustrative) | Capability profile |
| MCF-PHY-011 | Leak alarm to isolation time (automatic isolation zones) | s | 60 (illustrative) | Capability profile; CDU OEM guidance |
| MCF-PHY-011 | Maximum credible leak rate for drainage sizing | L/min | per largest pipe and pump capacity in zone | Thermal design basis |
| MCF-PHY-013 | Critical-zone access review interval | days | 90 (illustrative) | Capability profile |
| MCF-PHY-013 | Leaver revocation latency | hours | 4 (illustrative) | Capability profile |
| MCF-PHY-014 | Maximum visitors per escort in critical zones | ratio | 3:1 (illustrative) | Capability profile |
| MCF-PHY-015 | Recording retention | days | 90 (illustrative) | Capability profile; local privacy law limits |
| MCF-PHY-015 | Pixel density for identification views | px/m | 250 | IEC 62676-4 operational requirement categories |
| MCF-PHY-016 | Alarm acknowledgement time | s | 60 (illustrative) | Capability profile |
| MCF-PHY-016 | Attendance time at critical-zone alarm | minutes | 5 (illustrative) | Capability profile |
| MCF-PHY-016 | Unannounced response exercises | per year | 4 (illustrative) | Capability profile |
| MCF-PHY-017 | Inbound critical shipments with seal inspection | % | 100 (illustrative) | Capability profile |
| MCF-PHY-018 | Rack or plant mass requiring an approved move plan | kg | 1,500 (illustrative) | Capability profile |
| MCF-PHY-019 | Media custody inventory reconciliation interval | days | 30 (illustrative) | Capability profile |
| MCF-PHY-020 | Decommissioned data-bearing devices with per-serial certificate | % | 100 (illustrative) | Capability profile |
| MCF-PHY-021 | Aspirating detection maximum transport time | s | per design; not greater than the EN 54-20 class limit | EN 54-20 (aspirating smoke detectors); system design |
| MCF-PHY-021 | Detection functional test interval | months | 12 (illustrative) | NFPA 72 or national fire code; capability profile |
| MCF-PHY-021 | Maximum detection impairment duration without compensating measure | hours | 0 (illustrative) | Capability profile |
| MCF-PHY-022 | Gaseous agent design hold time | minutes | 10 (illustrative) | NFPA 2001 or ISO 14520 design practice; fire engineer's design |
| MCF-PHY-022 | Enclosure integrity test interval | months | 12 (illustrative) | Capability profile; agent standard |
| MCF-PHY-023 | Emergency lighting full-duration test interval | months | 12 (illustrative) | National emergency lighting standard (e.g. EN 50172); capability profile |
| MCF-PHY-024 | Emergency shutdown functional test interval | months | 12 (illustrative) | Capability profile; applicable electrical code |

**DG-PHY-REQ-004** The assessor shall take structural, flood and fire-resistance parameter values from the engineer of record, flood-risk assessment and fire strategy for the site, and shall record any illustrative default retained as an assumption subject to an UNKNOWN Record.

## 10 Evidence expectations by claim type

| Claim type | Assurance Level | Controls | Profile tiers used | Sufficiency floors used |
|---|---|---|---|---|
| DESIGN | AL2 | MCF-PHY-001, MCF-PHY-002, MCF-PHY-004, MCF-PHY-005 | CP-1, CP-2 | S3 |
| IMPLEMENTATION | AL3 | MCF-PHY-006, MCF-PHY-007, MCF-PHY-009, MCF-PHY-010, MCF-PHY-011, MCF-PHY-012, MCF-PHY-015 | CP-2, CP-4 | S3, S4 |
| OPERATION | AL4 | MCF-PHY-003, MCF-PHY-008, MCF-PHY-013, MCF-PHY-014, MCF-PHY-017, MCF-PHY-018, MCF-PHY-019, MCF-PHY-020, MCF-PHY-023 | CP-3, CP-5 | S3, S4 |
| EFFECTIVENESS | AL5 | MCF-PHY-016, MCF-PHY-021, MCF-PHY-022, MCF-PHY-024 | CP-4, CP-5 | S4 |

- **DESIGN (AL2)**: hazard assessments, exposure registers, structural statements, adjacency registers. E1 by competent specialists, with E7 analysis (for example overlay of redundant paths on hazard contours). Dates and the source data edition matter: a flood assessment based on superseded mapping is stale (U3).
- **IMPLEMENTATION (AL3)**: as-built zoning, compartmentation, water-zone layouts, anchorage and rack load registers reconciled to the installation by inspection sample. Configuration exports from access-control and video systems (E2).
- **OPERATION (AL4)**: E3 over a representative period: access reviews and leaver reconciliations, visitor records, goods-in and custody logs, inspection records for envelope and fire-stopping, egress inspections, delivery records for the heaviest rack.
- **EFFECTIVENESS (AL5)**: E4 tests: aspirating transport-time tests, end-to-end cause-and-effect tests, enclosure integrity tests, EPO scope tests, unannounced alarm-response exercises. For CG-04 CRITICAL controls, E5 independent evidence is required.

Evidence cautions:

- An insurer survey or a certificate of occupancy is valuable E5 evidence but is evaluated for scope, age and exclusions; it rarely covers liquid-cooling interlocks or rack BBUs.
- Photographs are E3 evidence only when their location, date and integrity are established (AIDCF-008 metadata).
- A fire strategy drawing shows intent (E1); fire-stopping inspection shows implementation (E3); neither shows that detection works (E4).

## 11 Assessment guidance

1. **Start from outcomes and the fault-domain model.** Identify which redundant paths the PHY controls must keep apart.
2. **Overlay.** Produce the overlay of redundant paths on fire, water and security zones (DG-PHY-REQ-001). This is the most productive single analytical step in PHY.
3. **Walk down.** Inspect plant yards, risers, battery rooms, CDU rooms, roofs (where safe access exists) and a sample of halls. Look for uncontained liquid joints above electrical equipment, unsealed penetrations, zone bypass routes and blocked egress.
4. **Reconcile loads.** Rebuild rack-position loads from the deployment pipeline using operating mass and compare with structural capacity.
5. **Review fire interfaces.** Reconcile the cause-and-effect matrix to fire panel and BMS logic; check what fire mode does to CDUs and pumps.
6. **Test operations.** Reconcile access rights to approvals and leavers; reconcile custody inventories; time alarm responses.
7. **Witness tests.** Witness detection and interface tests where scheduled, from safe positions.
8. **Roll up.** Record results, Findings and UNKNOWN Records; evaluate CG-04 and CG-09 per AIDCF-010.

Sampling guidance: fire-stopping penetrations, rack positions and access holders are large homogeneous populations — sample with weighting to recent works, densest rows and critical zones. Fire detection zones, battery rooms and EPO circuits are assessed exhaustively.

Common pitfalls: accepting a structural statement prepared before liquid cooling; assuming zone continuity without looking above ceilings and below floors; treating plant yards as perimeter-only zones; not checking that rack BBUs are in the battery safety assessment; accepting an EPO test that verified activation but not scope.

## 12 Testing safety (hazardous-energy testing authorisation)

PHY tests can endanger people (gaseous discharge, isolation of life-safety systems) and capability (EPO, cooling interlocks).

**DG-PHY-REQ-005** An assessor shall not operate fire, suppression, EPO, access-control or isolation devices, and shall witness tests only as directed by the person in control of the work.

**DG-PHY-REQ-006** A test of suppression interfaces, emergency shutdown or fire-mode cooling interlocks relied on as evidence shall have been performed under a written authorisation by the facility owner's authorised engineer and the fire safety manager, with agent release physically disabled and verified, the alarm receiving centre notified, thermal contingency in place for cooling interlocks, and an approved shutdown window or load transfer for emergency shutdown tests.

| Test | Hazard | Precondition |
|---|---|---|
| Aspirating transport time (MCF-PHY-021) | False alarm, inadvertent release | Release isolated; ARC notified |
| End-to-end cause and effect (MCF-PHY-022) | Agent discharge; loss of cooling | Agent disabled and verified; CDU contingency; method statement |
| Enclosure integrity (MCF-PHY-022) | Pressure on doors; occupancy | Room cleared and posted |
| EPO scope (MCF-PHY-024) | Uncontrolled shutdown; electrical hazard | Shutdown window or load transferred; authorised engineer; rollback plan |
| Door release (MCF-PHY-023) | Security zone exposure | Security staff posted |
| Alarm response exercise (MCF-PHY-016) | Mis-dispatch of emergency services | Control-room supervisor briefed; no suppression or EPO circuit triggered |

Where a life-safety condition is unsafe and unresolved (for example missing detection in a battery room), the CG-04 evidence profile blocks relevant testing as well as assurance until it is resolved.

## 13 UNKNOWN hot-spots

| Control | UNKNOWN rule |
|---|---|
| MCF-PHY-001 Site Hazard Assessment | If the hazard assessment is absent or predates a material revision of hazard mapping, record a U1 or U3 UNKNOWN against the site and treat flood and seismic protection of critical plant as unverified for CG-02 and CG-04 evaluation. |
| MCF-PHY-005 Structural Capacity | If the load schedule cannot be reconciled to installed equipment, record a U5 UNKNOWN and treat structural adequacy for the affected area as unverified. |
| MCF-PHY-010 Fire Zones | If the redundant-path overlay cannot be produced, record a U5 UNKNOWN; CG-09 becomes UNKNOWN for fire as a common-mode initiator. |
| MCF-PHY-011 Water Zones | If the overlay cannot be produced for a liquid-cooled hall, record a U5 UNKNOWN and carry it into THM leak-management and CG-09 evaluation. |
| MCF-PHY-012 Tenant Segregation | If the provider will not disclose shared elements, record a U2 UNKNOWN and a U10 dependency UNKNOWN for the affected power and cooling paths. |
| MCF-PHY-021 Fire Detection | If functional test evidence for detection in a battery room or IT hall is missing or older than the interval, record a US4 UNKNOWN against CG-04; testing that depends on the room (for example load tests) is not authorised until resolved. |
| MCF-PHY-022 Suppression Interfaces | If the matrix cannot be reconciled to configured logic, or no end-to-end test is current, record a US4 UNKNOWN against CG-04 and refer the cooling interlock gap to CG-06. |
| MCF-PHY-023 Egress and Emergency Access | If egress in containment or battery rooms cannot be verified, record a US4 UNKNOWN for CG-04. |
| MCF-PHY-024 Emergency Shutdown Governance | If the actual scope of an EPO function has never been verified by test, record a US4 UNKNOWN against CG-04 and an associated UNKNOWN on CG-09 for unbounded shutdown scope. |

Typical causes: landlord or provider refusal to disclose shared risers and plant (U2); fire strategy not updated after liquid-cooling retrofit (U3); no evidence that EPO scope was ever tested (U5); structural load schedule not reconcilable to installed equipment (U5).

**DG-PHY-REQ-007** Any UNKNOWN affecting a CG-04 or CG-09 CRITICAL PHY control shall be recorded with severity US4 and shall set the affected gate to UNKNOWN until dispositioned.

## 14 Interfaces with other domains

| Domain | Interface | What PHY needs | What PHY provides |
|---|---|---|---|
| POW | Battery rooms, switchgear, generator yards | Battery safety assessments; arc-flash boundaries; plant layouts | Compartmentation; zoning; structural capacity; responder information |
| THM | Liquid cooling, CDUs, heat rejection | Pipe routes; fire-mode behaviour of CDUs; leak isolation | Water zones; suppression interfaces; plant-zone protection |
| ENV | Flood adaptation, refrigerants, waste | Climate-adjusted flood levels; refrigerant hazards | Site hazard data; decommissioning custody |
| NET | Diverse routes | Fibre route plans | Fire and security separation of diverse routes |
| SEC | PACS and VMS security | Logical security of access-control and video systems | Physical protection of control rooms and consoles |
| SUP | Deliveries, provenance | Expected shipments; chain-of-custody requirements | Goods-in records and seal inspections |
| STO/CMP | Media and hardware | Data classification; sanitisation methods | Custody and decommissioning records |
| OPS | Work control | Permits, method statements | Move plans; inspection records |
| RES | Recovery | Relocation and decant plans | Logistics routes for replacement equipment |
| DEP | Boundaries | Tenant and provider boundary definitions | Shared-element disclosure |

## 15 Informative references

Document-level references; no clause-level reliance is implied.

- EN 50600-1, EN 50600-2-1 (building construction), EN 50600-2-5 (security systems) / ISO/IEC 22237 series
- ANSI/TIA-942 — Telecommunications infrastructure standard for data centres
- NFPA 75 — Fire protection of information technology equipment
- NFPA 76 — Fire protection of telecommunications facilities
- NFPA 72 — National fire alarm and signalling code; EN 54 series — fire detection and fire alarm systems (EN 54-20 aspirating detectors)
- NFPA 2001 — Clean agent fire extinguishing systems; ISO 14520 series — gaseous fire-extinguishing systems
- NFPA 13 — Installation of sprinkler systems
- NFPA 855 — Installation of stationary energy storage systems; UL 9540A — thermal runaway fire propagation test method
- NFPA 101 — Life safety code, or national building regulations; EN 50172 — emergency escape lighting
- FM Global Property Loss Prevention Data Sheets (data centres; energy storage; natural hazards)
- EN 1991 / ASCE/SEI 7 — actions and minimum design loads; EN 1998 — seismic design
- IEC 62305 series — protection against lightning
- IWA 14-1 and PAS 68 — vehicle security barriers
- IEC 60839-11 — electronic access control systems; IEC 62676 series — video surveillance systems; EN 50131 series — intrusion alarm systems
- ISO/IEC 27001 and ISO/IEC 27002 — information security controls (physical controls)
- ISO 28000 — security management systems for the supply chain
- NIST SP 800-88 and IEEE 2883 — media sanitisation

## 16 Control summary

| Control ID | Title | Control type | Required AL | Claim type | Gate mappings |
|---|---|---|---|---|---|
| MCF-PHY-001 | Site Hazard Assessment | DIRECTIVE | AL2 | DESIGN | CG-02 SUPPORTING; CG-03 SUPPORTING; CG-04 SUPPORTING |
| MCF-PHY-002 | External Exposure | PREVENTIVE | AL2 | DESIGN | CG-09 SUPPORTING; CG-03 SUPPORTING |
| MCF-PHY-003 | Access and Logistics | PREVENTIVE | AL4 | OPERATION | CG-10 SUPPORTING |
| MCF-PHY-004 | Adjacent Risk | DIRECTIVE | AL2 | DESIGN | CG-03 SUPPORTING |
| MCF-PHY-005 | Structural Capacity | PREVENTIVE | AL2 | DESIGN | CG-02 SUPPORTING; CG-04 SUPPORTING |
| MCF-PHY-006 | Rack Loading | PREVENTIVE | AL3 | IMPLEMENTATION | CG-04 SUPPORTING; CG-14 SUPPORTING |
| MCF-PHY-007 | Anchorage and Vibration | PREVENTIVE | AL3 | IMPLEMENTATION | CG-09 SUPPORTING |
| MCF-PHY-008 | Building Envelope | PREVENTIVE | AL4 | OPERATION | CG-06 SUPPORTING |
| MCF-PHY-009 | Security Zones | PREVENTIVE | AL3 | IMPLEMENTATION | CG-15 SUPPORTING; CG-09 SUPPORTING |
| MCF-PHY-010 | Fire Zones | PREVENTIVE | AL3 | IMPLEMENTATION | CG-09 CRITICAL; CG-04 SUPPORTING |
| MCF-PHY-011 | Water Zones | PREVENTIVE | AL3 | IMPLEMENTATION | CG-09 SUPPORTING; CG-04 SUPPORTING |
| MCF-PHY-012 | Tenant Segregation | PREVENTIVE | AL3 | IMPLEMENTATION | CG-13 SUPPORTING; CG-02 SUPPORTING |
| MCF-PHY-013 | Identity-Based Access | PREVENTIVE | AL4 | OPERATION | CG-15 SUPPORTING |
| MCF-PHY-014 | Visitor Control | PREVENTIVE | AL4 | OPERATION | none |
| MCF-PHY-015 | Surveillance Coverage | DETECTIVE | AL3 | IMPLEMENTATION | none |
| MCF-PHY-016 | Alarm Response | DETECTIVE | AL5 | EFFECTIVENESS | none |
| MCF-PHY-017 | Delivery Controls | PREVENTIVE | AL4 | OPERATION | none |
| MCF-PHY-018 | Equipment Movement | PREVENTIVE | AL4 | OPERATION | CG-04 SUPPORTING |
| MCF-PHY-019 | Media Custody | PREVENTIVE | AL4 | OPERATION | none |
| MCF-PHY-020 | Decommissioning Custody | PREVENTIVE | AL4 | OPERATION | none |
| MCF-PHY-021 | Fire Detection | DETECTIVE | AL5 | EFFECTIVENESS | CG-04 CRITICAL; CG-09 SUPPORTING |
| MCF-PHY-022 | Suppression Interfaces | CORRECTIVE | AL5 | EFFECTIVENESS | CG-04 CRITICAL; CG-06 SUPPORTING; CG-07 SUPPORTING |
| MCF-PHY-023 | Egress and Emergency Access | PREVENTIVE | AL4 | OPERATION | CG-04 CRITICAL |
| MCF-PHY-024 | Emergency Shutdown Governance | DIRECTIVE | AL5 | EFFECTIVENESS | CG-04 CRITICAL; CG-07 SUPPORTING; CG-09 SUPPORTING |

## 17 Worked synthetic example

**Synthetic example. The site, figures and results below are invented for illustration and do not describe any real facility or assessment.**

*Context.* Synthetic Site S-2 is a brownfield building retrofitted for a direct-to-chip cluster in Hall 2, with lithium-ion UPS in two UPS rooms and rack BBUs in the cluster racks. The decision question is whether Hall 2 can host the cluster at the declared Service Outcomes through NORMAL, MAINTENANCE and EMERGENCY states. Profile parameters (illustrative for the example): structural re-check threshold 80%; fire resistance between redundant paths 120 minutes; leak alarm to isolation 60 s.

*Overlay.* The assessor overlays A/B busway, the two UPS rooms and the two fibre routes on the fire-compartment drawings. Both UPS rooms are separate compartments; however both fibre routes and the A and B busway feeders pass through a single riser compartment on level 1.

*Selected results.*

| Control | Claim type | Synthetic observation | Result |
|---|---|---|---|
| MCF-PHY-005 | DESIGN | Structural statement predates retrofit and uses dry rack mass; recomputed wet load reaches 92% of capacity in two rows | PARTIAL |
| MCF-PHY-010 | IMPLEMENTATION | Shared level-1 riser hosts both busway feeders and both fibre routes with no rated enclosure | NONCONFORMING |
| MCF-PHY-011 | IMPLEMENTATION | Manifold joints above two tap-off units without drip trays | PARTIAL |
| MCF-PHY-021 | EFFECTIVENESS | Aspirating tests current; rack BBUs not covered by battery safety assessment; no off-gas detection in Hall 2 | NONCONFORMING |
| MCF-PHY-022 | EFFECTIVENESS | Cause-and-effect stops all CDUs on any Hall 2 alarm; end-to-end test current | CONFORMING for the matrix as designed; Finding raised against design intent and referred to CG-06 |
| MCF-PHY-024 | EFFECTIVENESS | EPO scope never tested since retrofit | UNKNOWN (U5, US4) |

*Gate Results.* CG-04: MCF-PHY-021 NONCONFORMING → FAIL (the US4 UNKNOWN on MCF-PHY-024 would on its own have set CG-04 to UNKNOWN; FAIL takes precedence under the roll-up rule, and the UNKNOWN remains open). MCF-PHY-005 PARTIAL is SUPPORTING to CG-02 and CG-04 and receives a gate-level evaluation: the 92% loading is within capacity, so it does not defeat either gate, but it is carried as a condition. CG-09: MCF-PHY-010 NONCONFORMING → FAIL. The PHY-022 Finding is evaluated at CG-06 gate level (SUPPORTING): the thermal domain must show whether stopping all CDUs defeats thermal continuity.

*Effect on decision.* With CG-04 and CG-09 FAIL, the synthetic recommendation is NOT_ASSURED for the Hall 2 outcomes. Actions: enclose one busway feeder and one fibre route in a 120-minute rated enclosure or reroute; include rack BBUs in the battery safety assessment and install the off-gas detection it specifies; obtain a structural re-check; fit drip trays; perform an authorised EPO scope test in the next shutdown window.
