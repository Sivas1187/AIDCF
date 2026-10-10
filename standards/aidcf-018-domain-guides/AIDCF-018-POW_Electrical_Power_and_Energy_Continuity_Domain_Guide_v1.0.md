# AIDCF-018-POW Electrical Power Infrastructure and Energy Continuity Domain Guide

## Document control

| Field | Value |
|---|---|
| Document ID | AIDCF-018-POW |
| Title | Electrical Power Infrastructure and Energy Continuity Domain Guide |
| Parent artifact | AIDCF-018 Domain Guides |
| Domain | POW — Electrical Power Infrastructure and Energy Continuity |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Control source | AIDCF-007A Canonical Master Control Registry, controls MCF-POW-001 to MCF-POW-024; this guide agrees exactly with the machine-readable control records |
| Depends on | AIDCF-003, AIDCF-004, AIDCF-007A, AIDCF-008, AIDCF-009, AIDCF-010, AIDCF-013, AIDCF-014 |
| Requirement prefix | DG-POW-REQ-NNN |

### Revision history

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-10 | Initial issue: domain guide for the 24 POW controls, gate linkage, parameters, evidence and testing-safety expectations. |

## 1 Purpose and scope

This guide explains how the POW domain of AIDCF-007A is applied when assessing whether an AI Capability Instance can achieve its declared Service Outcomes. It gives assessors, facility owners, electrical engineers and capability owners a shared understanding of what each of the 24 POW controls protects, how they combine into the CG-05 Resilient electrical supply gate and contribute to CG-04, CG-07, CG-09 and CG-10, what evidence is expected at each claim type, and how hazardous-energy testing is authorised.

The domain covers the electrical system from the utility point of common coupling (PCC) to the rack power distribution unit (PDU) outlet:

- utility interconnection, firm and non-firm capacity, grid quality and obligations of the site as a large load;
- on-site generation, fuel storage, fuel quality and replenishment;
- uninterruptible power supply (UPS) systems, battery energy storage (BESS), rack-level battery backup units (BBUs) and their batteries;
- medium-voltage (MV) and low-voltage (LV) distribution: transformers, switchgear, automatic and static transfer switches (ATS/STS), busway, remote power panels and rack PDUs;
- protection, selective coordination, earthing, bonding and arc-flash hazard control;
- power quality, harmonics, transient ride-through and the dynamic behaviour of AI training load;
- the electrical power monitoring system (EPMS), maintenance, switching and restoration from a dead site.

Out of scope: the internal power conversion of servers and accelerators (CMP), the security of EPMS and control networks (SEC-02, referenced here as an interface), the operation of cooling plant (THM), and general maintenance governance (OPS), each of which is referenced where it interacts with POW.

This guide is informative except where a requirement carries a DG-POW-REQ identifier. The control requirements themselves are those of AIDCF-007A and are summarised in section 16.

## 2 Why this domain matters for AI capability

Traditional enterprise and cloud data centres have been engineered around loads that are large but statistically smooth: thousands of independent servers whose aggregate demand changes slowly. AI training and large-scale inference change the electrical problem in five ways.

**Density and concentration.** Rack power for liquid-cooled accelerator systems is an order of magnitude higher than legacy enterprise racks. A single row can draw what a legacy hall drew. Busway, tap-offs and PDUs operate near their continuous ratings, and the failover load on the surviving feed of an A/B pair becomes the binding constraint (MCF-POW-015 (Busway and PDU Capacity)).

**Synchronous dynamics.** A synchronous training job runs thousands of accelerators in lock-step through compute and communication phases. Aggregate power therefore oscillates, can step by a large fraction of cluster load when a job starts, stops, checkpoints or fails, and can contain periodic components in a frequency band that interacts with generator governors and voltage regulators, UPS rectifier controls and the grid. These effects are not visible in 15-minute utility metering. MCF-POW-020 (Load-Step Response) requires that the dynamics are characterised at sub-second resolution and that every source is shown to tolerate them.

**Grid significance.** A campus of hundreds of megawatts is a large load in grid terms. Network operators increasingly attach obligations to such loads: ride-through during faults, ramp-rate limits, curtailment and demand-response instructions. The connection agreement becomes a Service Outcome constraint (MCF-POW-001 (Utility Capacity), MCF-POW-004 (Utility Contingency), MCF-POW-019 (Transient Ride-Through)).

**Outcome-dependent redundancy.** Some AI designs deliberately omit UPS on accelerator load and rely on checkpointing, while keeping UPS on cooling, controls, storage and network. Whether that is acceptable depends on the declared Service Outcome (for example a recovery-point tolerance for a training run) rather than on a topology label. AIDCF therefore evaluates redundancy by failure analysis against outcome (MCF-POW-009 (UPS Topology)), not by the name "2N" or "N+1".

**Distributed lithium-ion energy.** Lithium-ion UPS strings, BESS and BBUs inside IT racks put large quantities of stored chemical energy close to people and critical plant. Thermal runaway, off-gassing and explosion hazards make battery condition a life-safety matter as well as a continuity matter (MCF-POW-010 (Battery Condition)).

The consequence is that a site that would be well-engineered for traditional IT can fail an AI Service Outcome: its generators may hunt under periodic load, its distributed redundant reserve may be consumed by densification, and its runtime may be insufficient for an orderly checkpoint.

## 3 Reference patterns and variants

AIDCF-013 defines reference patterns. Their electrical variants and the POW questions they raise are summarised below.

| Pattern (AIDCF-013) | Typical electrical arrangement | POW questions that dominate |
|---|---|---|
| Single-site training facility | MV utility intake (one or two feeds), MV/LV transformers per block, block-redundant or distributed-redundant UPS, N+1 generators per block | Load dynamics on generators; block reserve consumption; restoration sequence |
| Hyperscale campus | Dedicated substation(s), MV ring or radial distribution, catcher-block or distributed-redundant UPS, generator farm or MV generation | Upstream independence of feeds; grid obligations; MV protection selectivity; campus black start |
| Liquid-cooled high-density cluster | Overhead busway with high-rated tap-offs, rack-level BBUs, UPS on CDUs and pumps | Failover load on busway; BBU safety; ride-through of CDU drives |
| Colocation deployment | Provider-owned UPS and generation, tenant-owned PDUs and busway | Disclosure of shared paths; maintenance switching notification; tenant visibility of EPMS data |
| Modular facility | Skid-mounted power modules with integrated UPS/BESS | Module fault domains; transportable BESS safety; factory test vs site test |
| Brownfield retrofit | Legacy 2N UPS re-tasked for AI load | Rating headroom; harmonic and leading power factor behaviour; arc-flash study currency |
| Edge inference estate | Single utility feed, small UPS, sometimes no generator | Runtime against outcome; remote restoration |

Redundancy topologies encountered:

- **N**: capacity equals load; any component failure or maintenance reduces capacity. Acceptable only where the declared outcome tolerates the loss.
- **N+1 (or N+x)**: spare modules within a system; protects against module failure but not against failure of shared output switchgear or controls.
- **2N (system plus system)**: two independent paths each able to carry the full load. In normal operation each path is loaded to at most half its rating; the critical risk is undeclared shared elements (common output board, common controls, common battery room).
- **Distributed redundant (for example 4-to-make-3)**: several systems with load spread so that the loss of one is absorbed by the others. Reserve is easily consumed by growth because no single system is visibly "spare".
- **Block redundant / catcher**: several active blocks plus a reserve block reached through static or automatic transfer. Correctness depends on transfer behaviour and the reserve not being committed.
- **No UPS on accelerator load**: outcome-based design relying on checkpoint and restart, with UPS retained on cooling, controls, storage and network.

UPS performance is classified under IEC 62040-3 by dependency of output on input (VFI, VI, VFD) and by dynamic output performance. Eco-mode operation changes a VFI system to a VFD-like behaviour in normal operation; its effect on transfer under AI load swings must be assessed (MCF-POW-012 (Bypass Exposure), MCF-ENV-008 in the ENV domain).

## 4 Required functions and capability linkage

The POW domain implements the following Required Functions (AIDCF-002 chain step 4), each linked to Service Outcomes through HAS_OUTCOME / REQUIRES_FUNCTION relationships and implemented by InfrastructureSystems (IMPLEMENTED_BY):

| Required Function | Implemented by (typical InfrastructureSystem) | Controls |
|---|---|---|
| Import sufficient utility energy within connection limits | Utility intake, MV switchgear, transformers | MCF-POW-001, MCF-POW-002, MCF-POW-003, MCF-POW-004 |
| Generate energy during utility absence | Generators, paralleling switchgear, fuel system | MCF-POW-005, MCF-POW-006, MCF-POW-007, MCF-POW-008 |
| Bridge interruptions and condition power | UPS, BESS, BBUs, static bypass | MCF-POW-009, MCF-POW-010, MCF-POW-011, MCF-POW-012 |
| Distribute and protect | Switchgear, busway, PDUs, protection relays, earthing | MCF-POW-013, MCF-POW-014, MCF-POW-015, MCF-POW-016 |
| Deliver stable power to loads in all states | UPS controls, generator governors/AVRs, filters, STS | MCF-POW-017, MCF-POW-018, MCF-POW-019, MCF-POW-020 |
| Observe, maintain, switch and restore | EPMS, maintenance system, MOPs/EOPs, restoration plan | MCF-POW-021, MCF-POW-022, MCF-POW-023, MCF-POW-024 |

The capability linkage is explicit: a training Service Outcome expressed as "sustained throughput with a recovery point no worse than the last checkpoint" places requirements on runtime (time to complete a checkpoint), on load-step tolerance and on restoration time; an inference Service Outcome expressed as an availability and latency tolerance places requirements on transfer behaviour and redundancy in maintenance states. Assessors should obtain the Service Outcome tolerances from the CAP domain before setting POW parameters.

**DG-POW-REQ-001** The assessor shall derive the POW capability-profile parameters (section 9) from the declared Service Outcome tolerances and operating states, and shall record the derivation, rather than adopting illustrative defaults without justification.

## 5 Dependencies, fault domains and common-mode concerns

Electrical systems are rich in hidden shared elements. The following common-mode concerns recur and should be explicitly tested in the fault-domain model (AIDCF-013 fault-domain model; SHARES_FAULT_DOMAIN_WITH relationships):

- **Upstream utility**: two "independent" feeds originating from one grid substation busbar, one circuit corridor, or one protection intertrip scheme (MCF-POW-003 (Connection Reliability)).
- **Shared output or distribution boards**: a 2N UPS whose two systems feed a common board or a common STS upstream of the racks.
- **Shared controls**: a single paralleling controller for all generators; one PLC or master controller for the block-redundant transfer scheme; one EPMS server that sequences restoration.
- **Shared battery rooms**: batteries for both A and B UPS in the same fire compartment, so a single battery fire removes both (with PHY-03 fire zones).
- **Shared fuel system**: one fuel transfer pump set, one day-tank fill line, one bulk tank for all generators (MCF-POW-007 (Fuel Autonomy)).
- **Shared fuel supplier**: two contracts both served from the same terminal (MCF-POW-008 (Fuel Replenishment)).
- **Common firmware**: identical UPS or BMS firmware across all systems with a shared defect, or a common setting change pushed to all protection relays.
- **Common people and procedures**: one switching team, one MOP template with a systematic error.
- **Cross-domain**: cooling plant on non-UPS supplies whose restart time exceeds the thermal ride-through of liquid-cooled racks; BMS and CDU controllers on supplies that drop during transfer; EPMS on a network that depends on the IT fabric it monitors.

**DG-POW-REQ-002** The assessor shall trace every A/B or N+x claim in the electrical architecture to the first shared element upstream and downstream, and shall record each shared element as a Dependency with a FaultDomain, or record a U10 UNKNOWN where the trace cannot be completed.

## 6 Threats, hazards and failure scenarios with propagation paths

The scenarios below are drawn from AIDCF-004 (Part XII power and cooling families and the cross-domain library X01–X20) and are written as propagation paths from initiating event to Service Outcome.

| Scenario | Propagation path | Primary safeguards (controls) |
|---|---|---|
| Utility loss + generator no-start + UPS autonomy exhaustion (X01) | Grid fault → incomers open → generators fail to start (starting battery, fuel air-lock, controller) → UPS discharges → runtime exhausted before manual start → IT load lost without checkpoint → training outcome misses recovery-point tolerance | MCF-POW-006, MCF-POW-011, MCF-POW-010, MCF-POW-024 |
| Generator instability under training load | Utility loss → cluster on generator → periodic power oscillation in the governor bandwidth → frequency/voltage hunting → UPS rectifiers walk off, batteries cycle → generator protection trips → load on UPS only | MCF-POW-020, MCF-POW-005, MCF-POW-018 |
| Protection miscoordination | Fault in a rack PDU → branch device does not clear (inverter-limited fault current) → upstream switchboard trips → whole row or hall lost → outcome loss far beyond the faulted rack | MCF-POW-014, MCF-POW-015 |
| Distributed reserve consumed | Growth deployments added across systems → each below rating in normal state → one UPS fails → reallocated load exceeds survivors → cascading overload transfer to bypass → exposure to grid transient | MCF-POW-009, MCF-POW-012, MCF-POW-015 |
| Cooling restart failure on transfer (X02) | Grid dip → non-UPS chillers and dry-cooler fans trip → controls on non-UPS supply reboot → restart exceeds thermal ride-through → accelerators throttle then shut down | MCF-POW-019, THM recovery controls |
| Maintenance removes hidden shared dependency (X04) | MOP isolates A-side board → undocumented B-side dependency on A-side controls → B-side transfer fails → load lost | MCF-POW-023, MCF-POW-009, MCF-POW-021 |
| Battery thermal runaway | Cell defect or abuse → BMS alarm not acted on → thermal runaway and off-gas → deflagration or fire in UPS room → loss of both A and B if co-located → life-safety event | MCF-POW-010, PHY fire controls |
| Arc flash during switching | Out-of-date arc-flash study after fault-level increase → wrong PPE → arc event → injury and switchgear destruction → loss of the path for weeks | MCF-POW-013, MCF-POW-023 |
| Curtailment instruction | Grid emergency → network operator instructs load reduction → no rehearsed throttling path → uncontrolled shedding loses training state or breaches obligation | MCF-POW-004, MCF-POW-001 |
| EPMS compromise or malfunction (X05) | EPMS misreports loads → provisioning overloads PDUs, or remote command opens breakers | MCF-POW-021 with SEC-02 |
| Prolonged regional outage | Utility out for days → fuel autonomy exhausted → deliveries blocked by flood or regional priority → generators stop | MCF-POW-007, MCF-POW-008, MCF-POW-004 |
| Black start | Total site loss → BMS/EPMS without power → chillers and IT restarted simultaneously on generators → generator trips → prolonged recovery | MCF-POW-024, MCF-POW-020 |

## 7 Safeguards

Safeguards in this domain map to the AIDCF-004 Part IX functions as follows.

- **Prevent**: adequate firm capacity and margin; generator rating class and derating; fuel autonomy and quality; redundancy topology proven by failure analysis; selective coordination; continuous-load limits on busway and PDUs; power smoothing and ramp limits on accelerator clusters; harmonic mitigation; earthing and bonding; incident-energy reduction.
- **Detect**: Class A power quality monitoring at the PCC; EPMS with time-synchronised sequence-of-events; battery monitoring and BMS alarms; infrared thermography and partial-discharge monitoring; bypass alarms.
- **Contain**: selective protection; fault-domain separation between paths; separate battery compartments; static transfer to healthy sources; block reserve not committed.
- **Correct**: emergency operating procedures; automatic transfer; load-reduction and throttling procedures; deferral risk assessment.
- **Recover**: black-start and restoration plans with staged pick-up; fuel replenishment; hand-over criteria to IT restart.

The effectiveness of each safeguard is claimed only to the depth evidenced. A safeguard that exists in design but has not been tested supports a DESIGN claim; a CG-05 gate PASS requires CONFORMING results at the claim types in section 16.

## 8 Critical-gate linkage

POW controls are mapped individually to gates under the AIDCF-010 control-to-gate mapping rule. CRITICAL means the gate cannot PASS unless the control is CONFORMING at its required claim type; SUPPORTING means a NONCONFORMING result requires a documented gate-level evaluation.

| Gate | Name | CRITICAL controls (this domain) | SUPPORTING controls (this domain) |
|---|---|---|---|
| CG-02 | Boundary and architecture integrity | none | MCF-POW-009 |
| CG-03 | Critical dependency visibility | none | MCF-POW-001, MCF-POW-003, MCF-POW-008, MCF-POW-020 |
| CG-04 | Life safety and hazardous energy | MCF-POW-010, MCF-POW-013, MCF-POW-016, MCF-POW-023 | none |
| CG-05 | Resilient electrical supply | MCF-POW-001, MCF-POW-005, MCF-POW-006, MCF-POW-007, MCF-POW-009, MCF-POW-011, MCF-POW-019, MCF-POW-020 | MCF-POW-002, MCF-POW-003, MCF-POW-004, MCF-POW-008, MCF-POW-010, MCF-POW-012, MCF-POW-013, MCF-POW-014, MCF-POW-015, MCF-POW-016, MCF-POW-017, MCF-POW-018, MCF-POW-021, MCF-POW-022, MCF-POW-024 |
| CG-06 | Thermal continuity | none | MCF-POW-019 |
| CG-07 | Critical control-system integrity | MCF-POW-021 | MCF-POW-006, MCF-POW-023, MCF-POW-024 |
| CG-09 | Failure containment | MCF-POW-014 | MCF-POW-003, MCF-POW-009, MCF-POW-012 |
| CG-10 | Recovery readiness | MCF-POW-024 | MCF-POW-004, MCF-POW-008 |
| CG-14 | Change control | none | MCF-POW-015, MCF-POW-023 |
| CG-15 | Integrated digital authority over infrastructure | none | MCF-POW-021 |

Notes on the mapping:

- **CG-05** is carried by eight CRITICAL POW controls covering capacity (MCF-POW-001), generation (MCF-POW-005, MCF-POW-006, MCF-POW-007), UPS topology and runtime (MCF-POW-009, MCF-POW-011), and dynamic behaviour (MCF-POW-019, MCF-POW-020). The remaining POW controls inform CG-05 as SUPPORTING. CG-05 evidence floor is S5 (AIDCF-008 Part XIII): missing critical continuity evidence yields UNKNOWN; demonstrated inability yields FAIL.
- **CG-04** includes the POW electrical-safety controls: battery hazards (MCF-POW-010), arc-flash and switchgear condition (MCF-POW-013), shock protection through earthing and bonding (MCF-POW-016) and safe switching with lockout/tagout (MCF-POW-023).
- **CG-07** treats the EPMS as a critical control system (MCF-POW-021). Generator start and paralleling controls, switching automation and restoration sequencing are SUPPORTING.
- **CG-09** relies on selective coordination (MCF-POW-014) as the electrical containment mechanism.
- **CG-10** relies on black-start and restoration (MCF-POW-024).

**DG-POW-REQ-003** Where the assessment boundary includes critical electrical supply, the assessor shall evaluate CG-05 using every in-scope CRITICAL control listed above and shall not substitute a domain score for a missing CRITICAL control result.

**DG-POW-REQ-004** The assessor shall record the gate-level evaluation required for every SUPPORTING POW control that is NONCONFORMING, stating whether the deficiency defeats the gate scope, before a gate PASS is recorded.

## 9 Capability-profile parameters

Values marked illustrative are not recommendations; they show the order of magnitude a profile might adopt. Values without the label are attributed to the cited source family. Every parameter used in an assessment shall be set in the approved capability profile (DG-POW-REQ-001).

| Control | Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|---|
| MCF-POW-001 | Margin of firm import capacity over modelled peak demand | % of firm capacity | 10 (illustrative) | Capability profile |
| MCF-POW-001 | Demand forecast horizon | months | 36 (illustrative) | Capability profile; utility lead times |
| MCF-POW-001 | Metered demand integration interval | minutes | 15 or finer | Utility tariff metering practice; finer resolution needed to capture AI load dynamics |
| MCF-POW-002 | Supply voltage variation assumed in design | % of nominal | ±10 (illustrative) | EN 50160 voltage characteristics or utility declaration |
| MCF-POW-002 | Power quality data retention | months | 24 (illustrative) | Capability profile |
| MCF-POW-003 | Interruption history period | years | 5 (illustrative) | Capability profile; network operator data |
| MCF-POW-004 | Time to achieve declared load reduction on curtailment instruction | minutes | 15 (illustrative) | Connection agreement; capability profile |
| MCF-POW-004 | Plan exercise interval | months | 12 (illustrative) | Capability profile |
| MCF-POW-005 | Generator redundancy | topology | N+1 (illustrative) | Capability profile; outcome tolerance |
| MCF-POW-005 | Site design ambient for generator derating | °C | site extreme design value (ASHRAE climatic data, n-year return; illustrative n=20) | ASHRAE Handbook climatic design data; capability profile |
| MCF-POW-005 | Periodic load-bank test duration at rated load | hours | 4 (illustrative) | NFPA 110 or national emergency power practice; capability profile |
| MCF-POW-006 | Maximum start-to-load-acceptance time | s | 10 (illustrative; NFPA 110 Type 10 defines 10 s) | NFPA 110 type classification; UPS autonomy |
| MCF-POW-006 | Monthly test load | % of nameplate | 30 (illustrative) | NFPA 110 monthly exercise practice |
| MCF-POW-006 | Start reliability threshold for incident review | failed or delayed starts per year | 0 (illustrative) | Capability profile |
| MCF-POW-007 | On-site fuel autonomy at declared load | hours | 48 (illustrative) | Capability profile; outcome tolerance and replenishment risk |
| MCF-POW-007 | Fuel quality test interval | months | 6 (illustrative) | Capability profile; fuel specification (EN 590, ASTM D975 or EN 15940) |
| MCF-POW-008 | Guaranteed emergency resupply lead time | hours | 12 (illustrative) | Supply contracts; capability profile |
| MCF-POW-008 | Independent fuel suppliers | count | 2 (illustrative) | Capability profile |
| MCF-POW-009 | Declared UPS redundancy | topology | 2N or distributed redundant (illustrative) | Capability profile |
| MCF-POW-009 | Maximum normal-state loading of each path in a 2N design | % of path rating | 45 (illustrative) | Capability profile; failure analysis |
| MCF-POW-010 | Battery end-of-life capacity threshold | % of rated capacity | 80 | IEEE 450 / IEEE 1188 replacement criterion for lead-acid; OEM criterion for lithium-ion |
| MCF-POW-010 | Battery capacity test interval | months | 12 (illustrative) | Capability profile; IEEE 450/1188 |
| MCF-POW-010 | BMS critical alarm response time | minutes | 15 (illustrative) | Capability profile |
| MCF-POW-011 | Minimum UPS/BESS runtime at declared load, end of life | minutes | 5 (illustrative) | Capability profile; generator start time and workload preservation time |
| MCF-POW-011 | Load growth threshold triggering runtime recalculation | % of declared load | 10 (illustrative) | Capability profile |
| MCF-POW-012 | Cumulative bypass exposure limit per UPS system | hours per year | 24 (illustrative) | Capability profile |
| MCF-POW-012 | Unplanned bypass escalation time | minutes | 15 (illustrative) | Capability profile |
| MCF-POW-013 | Arc-flash study review interval | years | 5 | NFPA 70E review requirement |
| MCF-POW-013 | Incident energy threshold requiring reduction measure | cal/cm² | 8 (illustrative) | Capability profile; NFPA 70E / IEEE 1584 methodology |
| MCF-POW-013 | Infrared thermography interval | months | 12 (illustrative) | NFPA 70B / capability profile |
| MCF-POW-014 | Protection setting extraction and comparison interval | months | 24 (illustrative) | Capability profile |
| MCF-POW-014 | Permitted deviation of as-found settings from study | count | 0 (illustrative) | Capability profile |
| MCF-POW-015 | Continuous load limit | % of device rating | 80 (illustrative; for devices not rated for 100% continuous duty) | NFPA 70 / IEC 60364 continuous-load sizing conventions; device rating |
| MCF-POW-015 | Maximum phase imbalance at PDU/busway | % | 10 (illustrative) | Capability profile |
| MCF-POW-016 | Periodic inspection and test interval | years | 5 (illustrative) | IEC 60364-6 / national wiring regulations; capability profile |
| MCF-POW-017 | Steady-state voltage envelope at critical boards | % of nominal | ±5 (illustrative) | Equipment PSU specifications; capability profile |
| MCF-POW-017 | Voltage unbalance limit | % | 2 (illustrative) | EN 50160 / IEC 61000-2 compatibility levels |
| MCF-POW-018 | Voltage THD limit at PCC, 1 kV < V ≤ 69 kV | % | 5 | IEEE 519 voltage distortion limits |
| MCF-POW-018 | Voltage THD limit at PCC, V ≤ 1 kV | % | 8 | IEEE 519 voltage distortion limits |
| MCF-POW-019 | Static transfer switch transfer time | ms | 4 (illustrative; within PSU hold-up) | STS OEM data; PSU hold-up specification |
| MCF-POW-019 | Maximum restart time for non-UPS cooling plant | s | per thermal ride-through analysis (THM) | Thermal design basis |
| MCF-POW-020 | Maximum cluster power swing amplitude | % of cluster IT load | 50 (illustrative) | Measured cluster data or accelerator vendor specification |
| MCF-POW-020 | Power oscillation frequency band of concern | Hz | 0.1 to 20 (illustrative) | Cluster characterisation; generator and grid modal analysis |
| MCF-POW-020 | Maximum single load step on generator supply | % of generator rating | per ISO 8528-5 class and test data (illustrative: 50) | ISO 8528-5 load acceptance performance classes |
| MCF-POW-020 | Measurement resolution for AI load dynamics | ms | 100 or finer (illustrative) | Capability profile |
| MCF-POW-021 | Critical-node metering coverage | % of critical nodes | 100 (illustrative) | Capability profile |
| MCF-POW-021 | Clock synchronisation accuracy for sequence of events | ms | 1 (illustrative) | Capability profile; IEC 61850 time-sync practice |
| MCF-POW-021 | Maximum EPMS data gap per point | % of period | 1 (illustrative) | Capability profile |
| MCF-POW-022 | On-time completion of critical electrical maintenance | % | 95 (illustrative) | Capability profile |
| MCF-POW-022 | Maximum overdue period without approved deferral | days | 30 (illustrative) | Capability profile |
| MCF-POW-023 | Planned critical switching with approved, peer-checked MOP | % | 100 (illustrative) | Capability profile |
| MCF-POW-024 | Restoration time from dead site to full critical load | hours | 4 (illustrative) | Capability profile; recovery outcome |
| MCF-POW-024 | Black-start exercise interval | months | 12 (illustrative) | Capability profile |

## 10 Evidence expectations by claim type

Evidence classes, quality dimensions and sufficiency follow AIDCF-008. The POW controls use claim types as follows.

| Claim type | Assurance Level | Controls | Profile tiers used | Sufficiency floors used |
|---|---|---|---|---|
| DESIGN | AL2 | MCF-POW-003 | CP-2 | S3 |
| IMPLEMENTATION | AL3 | MCF-POW-009, MCF-POW-014, MCF-POW-016, MCF-POW-021 | CP-4, CP-5 | S4, S5 |
| OPERATION | AL4 | MCF-POW-001, MCF-POW-002, MCF-POW-006, MCF-POW-007, MCF-POW-010, MCF-POW-012, MCF-POW-013, MCF-POW-015, MCF-POW-017, MCF-POW-018, MCF-POW-022, MCF-POW-023 | CP-3, CP-4, CP-5 | S3, S4, S5 |
| EFFECTIVENESS | AL5 | MCF-POW-005, MCF-POW-011, MCF-POW-019, MCF-POW-020 | CP-5 | S5 |
| RESILIENCE | AL5 | MCF-POW-004, MCF-POW-008, MCF-POW-024 | CP-5 | S4, S5 |

Expectations by claim type:

- **DESIGN (AL2)**: approved design basis, single-line diagrams, studies (short-circuit, coordination, harmonic, arc-flash, failure analysis) by competent engineers; E1 with E7 analysis. A DESIGN conclusion says nothing about the installed system.
- **IMPLEMENTATION (AL3)**: as-built single-line diagram reconciled to the installation by inspection sample; extracted configuration (protection settings, UPS mode, EPMS point list); E2 configuration evidence reconciled to E1 design. Protection settings must be extracted from devices, not copied from the study.
- **OPERATION (AL4)**: E3 data over a representative period that includes the seasonal peak and peak AI utilisation; generator monthly test logs reconciled to controller event logs; maintenance work-order history; bypass logs reconciled to UPS event logs.
- **EFFECTIVENESS (AL5)**: E4 tests under representative conditions: load-bank tests at rated load, discharge tests, transfer tests with waveform capture, load-step or oscillation tests on generator supply.
- **RESILIENCE (AL5)**: E4 scenario evidence that a failure is contained and the outcome restored within tolerance: curtailment exercises with measured MW reduction, fuel delivery exercises, black-start or staged restoration exercises with milestone times.

Specific evidence cautions for POW:

- 15-minute revenue metering cannot evidence AI load dynamics; MCF-POW-020 requires sub-second data.
- A load-bank test at constant load does not demonstrate tolerance of periodic oscillation; programmable load banks or real cluster load are needed for MCF-POW-020 EFFECTIVENESS.
- UPS runtime from the vendor's datasheet at beginning-of-life capacity is not evidence of end-of-life runtime at worst battery temperature (MCF-POW-011).
- A generator "start" in a monthly test that did not reach the declared load does not evidence capacity (MCF-POW-005) and only partially evidences start reliability (MCF-POW-006).
- A real outage is valuable evidence, but only for the load, duration and states it actually covered (AIDCF-008 worked package 48: no resilience conclusion beyond tested load, duration and states).

**DG-POW-REQ-005** Evidence used for a CG-05 CRITICAL control shall meet the sufficiency floor of S5 recorded in its evidence profile; evidence below the floor shall result in UNKNOWN, not in a reduced score.

## 11 Assessment guidance

A practical sequence for a POW assessment:

1. **Obtain outcomes and states.** Read the Service Outcome tolerances and declared operating states from CAP. Set parameters.
2. **Freeze the architecture.** Obtain the as-built single-line diagram and reconcile it by inspection sample before reviewing any study. Record the ArchitectureSnapshot version used. Studies based on a different revision are flagged.
3. **Trace shared elements.** Follow every redundant path upstream and downstream to its first shared element (DG-POW-REQ-002).
4. **Rebuild the demand model.** Independently compute peak demand from rack power limits, mechanical load at design ambient and recharge, and compare with firm capacity and metered peaks.
5. **Run the failure analysis yourself.** For the UPS topology, take each single failure and each maintenance state and recompute surviving loading at current and forecast load. This is the single most productive analytical step in POW.
6. **Characterise the dynamics.** For AI clusters, obtain high-resolution power data or vendor specifications and compare with generator load-acceptance class, UPS dynamic behaviour and grid obligations.
7. **Reconcile operations evidence.** Reconcile logs to controller and EPMS event data; do not rely on manually maintained logs alone.
8. **Witness tests.** Witness a representative subset of tests from a safe position (section 12) and review the remainder.
9. **Roll up.** Record control results per claim type, Findings and UNKNOWN Records, then evaluate gates using the AIDCF-010 roll-up rule.

Sampling: for homogeneous populations (rack PDUs, busway tap-offs, breakers) use risk-weighted samples concentrated on the densest rows and the most recent deployments. For unique assets (generators, UPS systems, MV switchgear) assess every unit.

Common pitfalls observed in assessments of this kind:

- accepting "2N" from a design report while the as-built has a shared output board;
- reviewing the coordination study but not extracting settings from relays;
- assessing generator capacity at ISO conditions rather than site design ambient with yard recirculation;
- counting the whole tank volume as usable fuel;
- treating a UPS that transfers to bypass during a load swing as "working as designed".

**DG-POW-REQ-006** The assessor shall reconcile the as-built single-line diagram to the installation before relying on any electrical study, and shall record the drawing revision used in each ControlAssessment.

## 12 Testing safety (hazardous-energy testing authorisation)

Most POW effectiveness and resilience evidence comes from tests that involve hazardous energy (arc flash, shock, stored battery energy, rotating machines, fuel) and that can cause loss of critical load if they go wrong. AIDCF does not authorise any test. Assessors rely on tests authorised and performed by the facility owner's competent persons, and may witness them.

**DG-POW-REQ-007** An assessor shall not operate, switch, isolate, test or open any electrical equipment, and shall witness hazardous-energy tests only from outside the arc-flash boundary or as directed by the person in control of the work.

**DG-POW-REQ-008** A hazardous-energy test relied on as evidence shall have been performed under a written test authorisation by the facility owner's authorised engineer, a method statement or MOP with hold points and abort criteria, a permit to work and lockout/tagout where isolation is involved, confirmation of healthy redundancy before start, and the capability owner's acceptance of the risk to the Service Outcome.

Test-specific expectations:

| Test | Principal hazards | Authorisation preconditions |
|---|---|---|
| Generator load-bank (MCF-POW-005) | Temporary cabling, hot exhaust, rotating plant | Engineered connection points; cabling inspected; exclusion zone |
| Transfer and ride-through (MCF-POW-006, MCF-POW-019) | Loss of critical load | Redundancy verified; thermal contingency; IT notified; abort criteria |
| UPS/battery discharge (MCF-POW-010, MCF-POW-011) | Stored energy, hydrogen, thermal runaway | No active BMS faults; minimum cell-voltage abort; battery PPE |
| Load-step/oscillation on generator (MCF-POW-020) | Generator trip, voltage collapse | Programmable load bank preferred; if real cluster load, workload checkpointed and capability owner approval |
| Secondary injection (MCF-POW-014) | Unintended trip | Trip outputs isolated or circuit outage |
| Thermography (MCF-POW-013) | Arc flash with covers open | IR windows or energised-work permit |
| Black start (MCF-POW-024) | All of the above, plus loss of controls | Approved plan, written authorisation by facility and capability owners, workloads drained; staged tests preferred |

An unsafe unresolved condition (for example no current arc-flash study or a battery room without a safety assessment) blocks relevant testing as well as assurance, per the CG-04 evidence profile in AIDCF-008 Part XIII. In that case the control result for the dependent test-based claim is UNKNOWN, and the UNKNOWN is recorded with severity US4.

## 13 UNKNOWN hot-spots

The following POW UNKNOWNs occur frequently and have gate consequences. Each control's own rule is reproduced from its record.

| Control | UNKNOWN rule |
|---|---|
| MCF-POW-001 Utility Capacity | If metered peak demand for the cooling peak season is unavailable, record a U5 UNKNOWN; CG-05 becomes UNKNOWN for the capacity criterion until data for that season exists. |
| MCF-POW-003 Connection Reliability | If the network operator does not provide upstream topology, record a U10 dependency UNKNOWN and treat feeds as one fault domain for CG-05 sizing. |
| MCF-POW-006 Start Reliability | If monthly test records are missing for any unit for more than one month, or controller logs cannot corroborate timing, record a US4 UNKNOWN against CG-05. |
| MCF-POW-009 UPS Topology | If the as-built single-line diagram cannot be reconciled, record a US4 UNKNOWN against CG-05 and a U5 against CG-02 architecture integrity. |
| MCF-POW-011 Runtime and Derating | If no discharge test exists within the interval, record a US4 UNKNOWN against CG-05; runtime claims are limited to calculation (DESIGN depth). |
| MCF-POW-014 Selective Coordination | If settings cannot be extracted or the study omits generator or UPS source configurations, record a US4 UNKNOWN against CG-09 for electrical fault containment. |
| MCF-POW-020 Load-Step Response | If cluster dynamics are uncharacterised for a site where the applicability threshold is met, record a US4 UNKNOWN against CG-05; generator and UPS adequacy claims are limited to static load. |
| MCF-POW-021 EPMS Coverage | If the point list cannot be reconciled to the single-line diagram, record a US4 UNKNOWN against CG-07; EPMS-derived evidence for other POW controls is downgraded to T2 until resolved. |
| MCF-POW-024 Black-Start and Restoration | If restoration has never been exercised, record a US4 UNKNOWN against CG-10; the plan supports design only, not recoverability. |

Typical sources of these UNKNOWNs:

- network operators unwilling to disclose upstream topology (U10);
- protection settings that cannot be extracted without an outage (U2);
- AI power dynamics never measured at sub-second resolution (U5);
- colocation providers who provide summary EPMS data but not the event logs that would corroborate transfer behaviour (U2);
- restoration plans that exist but have never been exercised (U5).

**DG-POW-REQ-009** Any UNKNOWN affecting a CG-05, CG-04, CG-07, CG-09 or CG-10 CRITICAL POW control shall be recorded with severity US4 and shall set the affected gate to UNKNOWN until dispositioned.

## 14 Interfaces with other domains

| Domain | Interface | What POW needs | What POW provides |
|---|---|---|---|
| CAP | Outcomes, demand | Outcome tolerances; peak and transient demand | Capacity assertions; outcome-based redundancy evaluation |
| DEP | Dependencies | Shared-source and utility dependency analyses | Electrical dependency and fault-domain records |
| PHY | Fire zones, structure | Separation of A/B paths and battery compartments; structural capacity for batteries and switchgear | Battery hazard data; arc-flash boundaries for egress and responder information |
| THM | Cooling restart | Thermal ride-through time; CDU and pump power requirements | UPS backing of cooling and controls; restart behaviour on transfer |
| ENV | Efficiency, fuel, batteries | Resilience impact of eco-mode; fuel and battery material handling | Energy data for PUE; generator fuel for Scope 1 |
| CMP | Power capping | Accelerator power limits; power-smoothing features; checkpoint timing | Runtime; load-step limits |
| STO | Checkpoint | Checkpoint durability and duration | Runtime to complete checkpoint |
| OPS | Work control | Permit-to-work, LOTO, maintenance strategy | Electrical MOPs and EOPs |
| RES | Recovery | Recovery sequencing and exercises | Restoration milestones |
| SEC | EPMS security | BMS/EPMS security, remote access control | EPMS architecture and point list |
| SUP | Fuel and spares | Logistics continuity; supplier concentration | Fuel replenishment requirements |

## 15 Informative references

Document-level references; no clause-level reliance is implied.

- IEC 60364 series — Low-voltage electrical installations
- IEC 61439 series — Low-voltage switchgear and controlgear assemblies (including busbar trunking)
- IEC 62271-200 — AC metal-enclosed switchgear (internal arc classification)
- IEC 60076 series — Power transformers
- IEC 60909 — Short-circuit currents in three-phase AC systems
- IEC 62040-1 and IEC 62040-3 — UPS safety and UPS performance/test requirements
- IEC 61000 series — Electromagnetic compatibility (compatibility levels, emission limits, IEC 61000-4-30 power quality measurement)
- EN 50160 — Voltage characteristics of electricity supplied by public networks
- IEEE 519 — Harmonic control in electric power systems
- IEEE 1584 — Arc-flash hazard calculations
- NFPA 70E — Electrical safety in the workplace; NFPA 70B — Electrical equipment maintenance; NFPA 70 — National Electrical Code
- NFPA 110 — Emergency and standby power systems
- ISO 8528 series — Reciprocating internal combustion engine driven generating sets (rating classes, load acceptance)
- IEC 62619, IEC 62485, NFPA 855, UL 9540 / UL 9540A — Battery and energy storage safety
- IEEE 450, IEEE 1188, IEEE 485, IEEE 1184 — Battery maintenance and sizing
- IEC 61850 — Communication for power utility automation; IEC 62443 series — industrial control system security
- EN 50600-2-2 / ISO/IEC 22237 — Data centre power supply and distribution
- EN 50110 — Operation of electrical installations
- Network operator connection codes for demand facilities (for example the EU Network Code on Demand Connection)

## 16 Control summary

| Control ID | Title | Control type | Required AL | Claim type | Gate mappings |
|---|---|---|---|---|---|
| MCF-POW-001 | Utility Capacity | PREVENTIVE | AL4 | OPERATION | CG-05 CRITICAL; CG-03 SUPPORTING |
| MCF-POW-002 | Grid Quality | DETECTIVE | AL4 | OPERATION | CG-05 SUPPORTING |
| MCF-POW-003 | Connection Reliability | DIRECTIVE | AL2 | DESIGN | CG-03 SUPPORTING; CG-05 SUPPORTING; CG-09 SUPPORTING |
| MCF-POW-004 | Utility Contingency | RECOVERY | AL5 | RESILIENCE | CG-05 SUPPORTING; CG-10 SUPPORTING |
| MCF-POW-005 | Generator Capacity | PREVENTIVE | AL5 | EFFECTIVENESS | CG-05 CRITICAL |
| MCF-POW-006 | Start Reliability | PREVENTIVE | AL4 | OPERATION | CG-05 CRITICAL; CG-07 SUPPORTING |
| MCF-POW-007 | Fuel Autonomy | PREVENTIVE | AL4 | OPERATION | CG-05 CRITICAL |
| MCF-POW-008 | Fuel Replenishment | RECOVERY | AL5 | RESILIENCE | CG-05 SUPPORTING; CG-03 SUPPORTING; CG-10 SUPPORTING |
| MCF-POW-009 | UPS Topology | PREVENTIVE | AL3 | IMPLEMENTATION | CG-05 CRITICAL; CG-09 SUPPORTING; CG-02 SUPPORTING |
| MCF-POW-010 | Battery Condition | DETECTIVE | AL4 | OPERATION | CG-04 CRITICAL; CG-05 SUPPORTING |
| MCF-POW-011 | Runtime and Derating | PREVENTIVE | AL5 | EFFECTIVENESS | CG-05 CRITICAL |
| MCF-POW-012 | Bypass Exposure | DETECTIVE | AL4 | OPERATION | CG-05 SUPPORTING; CG-09 SUPPORTING |
| MCF-POW-013 | Switchgear Integrity | PREVENTIVE | AL4 | OPERATION | CG-04 CRITICAL; CG-05 SUPPORTING |
| MCF-POW-014 | Selective Coordination | PREVENTIVE | AL3 | IMPLEMENTATION | CG-09 CRITICAL; CG-05 SUPPORTING |
| MCF-POW-015 | Busway and PDU Capacity | PREVENTIVE | AL4 | OPERATION | CG-05 SUPPORTING; CG-14 SUPPORTING |
| MCF-POW-016 | Earthing and Bonding | PREVENTIVE | AL3 | IMPLEMENTATION | CG-04 CRITICAL; CG-05 SUPPORTING |
| MCF-POW-017 | Voltage Quality | DETECTIVE | AL4 | OPERATION | CG-05 SUPPORTING |
| MCF-POW-018 | Harmonics | PREVENTIVE | AL4 | OPERATION | CG-05 SUPPORTING |
| MCF-POW-019 | Transient Ride-Through | PREVENTIVE | AL5 | EFFECTIVENESS | CG-05 CRITICAL; CG-06 SUPPORTING |
| MCF-POW-020 | Load-Step Response | PREVENTIVE | AL5 | EFFECTIVENESS | CG-05 CRITICAL; CG-03 SUPPORTING |
| MCF-POW-021 | EPMS Coverage | DETECTIVE | AL3 | IMPLEMENTATION | CG-07 CRITICAL; CG-05 SUPPORTING; CG-15 SUPPORTING |
| MCF-POW-022 | Preventive Maintenance | PREVENTIVE | AL4 | OPERATION | CG-05 SUPPORTING |
| MCF-POW-023 | Switching Procedures | PREVENTIVE | AL4 | OPERATION | CG-04 CRITICAL; CG-07 SUPPORTING; CG-14 SUPPORTING |
| MCF-POW-024 | Black-Start and Restoration | RECOVERY | AL5 | RESILIENCE | CG-10 CRITICAL; CG-05 SUPPORTING; CG-07 SUPPORTING |

## 17 Worked synthetic example

**Synthetic example. The site, figures and results below are invented for illustration and do not describe any real facility or assessment.**

*Context.* Synthetic Site S-1 hosts a 24 MW (IT) synchronous training cluster and 6 MW of storage and network in two halls. The decision question is whether S-1 can sustain the declared training Service Outcome ("no loss of more than one checkpoint interval of training progress per utility event; restoration to full throughput within 6 hours of a total site loss") under NORMAL, MAINTENANCE and EMERGENCY states. The capability profile sets: margin of firm capacity 10%; generator redundancy N+1; runtime at end of life ≥ 6 minutes (derived from a measured checkpoint duration of 3.5 minutes plus generator start margin); maximum cluster swing 50% of cluster IT load in the 0.1–20 Hz band; restoration time 4 hours (illustrative values chosen for the example).

*Architecture.* Two MV feeds, four 2N UPS pairs (block 1–4), eight generators per block set (N+1), overhead busway, rack PDUs fed A and B.

*Selected results.*

| Control | Claim type | Synthetic observation | Result |
|---|---|---|---|
| MCF-POW-001 | OPERATION | Firm capacity 48 MW; rebuilt peak demand 41.5 MW including recharge; metered 1-second peak 42.3 MW during summer | CONFORMING (margin 11.9%) |
| MCF-POW-003 | DESIGN | Network operator topology shows both feeds from one grid substation busbar section | NONCONFORMING (design basis claims independence) |
| MCF-POW-009 | IMPLEMENTATION | As-built reconciles; failure analysis shows block 3 A-side at 104% of rating when B-side in maintenance at forecast load | PARTIAL (current load acceptable; forecast exceeds) |
| MCF-POW-011 | EFFECTIVENESS | Recalculated end-of-life runtime at 30 °C battery room: 7.2 minutes; discharge test 8.1 minutes at 92% load | CONFORMING |
| MCF-POW-020 | EFFECTIVENESS | Cluster data at 100 ms resolution shows 38% swings at about 0.5 Hz; no test on generator supply; generator governor response not assessed | UNKNOWN (U5 coverage gap) |
| MCF-POW-024 | RESILIENCE | Staged restoration exercises cover all steps; measured total 3 h 40 min | CONFORMING |

*Findings and UNKNOWN Records.* F-1 (MCF-POW-003): feed independence claim is unsupported; the two feeds are one upstream fault domain. U-1 (MCF-POW-020, U5, US4): generator tolerance of the measured oscillation is unverified.

*Gate Results.* CG-05: MCF-POW-009 is PARTIAL, therefore CG-05 = FAIL under the AIDCF-010 roll-up rule (PARTIAL never yields PASS), independently of U-1. MCF-POW-003 is SUPPORTING to CG-03, CG-05 and CG-09, so its NONCONFORMING result requires a gate-level evaluation for each: for CG-03 the shared upstream busbar is now visible and owned, so the evaluation concludes no defeat of dependency visibility; for CG-05 the evaluation is recorded but does not change the FAIL; for CG-09 it concludes that containment within the site is not defeated. With MCF-POW-014 CONFORMING (not shown), CG-09 = PASS for electrical containment. CG-10: PASS on MCF-POW-024 together with other domains' recovery controls (not shown).

*Effect on decision.* With CG-05 FAIL the decision recommendation cannot be REASONABLY_ASSURED or CONDITIONALLY_ASSURED for outcomes that depend on resilient supply. The synthetic report recommends actions: (a) re-balance block 3 or add UPS capacity before the forecast deployment; (b) perform a programmable load-bank oscillation test on generator supply to resolve U-1; (c) correct the design basis and size generator autonomy for a single upstream fault domain. Once (a) is implemented and evidenced, CG-05 would move to UNKNOWN until (b) resolves U-1.
