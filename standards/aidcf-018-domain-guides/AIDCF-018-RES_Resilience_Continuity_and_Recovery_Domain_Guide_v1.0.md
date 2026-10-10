# AIDCF-018-RES Resilience, Continuity and Recovery Domain Guide

**AIDCF – AI Data Centre Facilities Assurance Framework**

## Document control

| Field | Value |
|---|---|
| Document ID | AIDCF-018-RES |
| Title | Resilience, Continuity and Recovery Domain Guide |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Parent artifact | AIDCF-018 Domain Guides |
| Normative controls | MCF-RES-001 to MCF-RES-024 in AIDCF-007A |
| Depends on | AIDCF-002, AIDCF-003, AIDCF-004, AIDCF-007A, AIDCF-008, AIDCF-009, AIDCF-010, AIDCF-013, AIDCF-014 |
| Requirement prefix | DG-RES-REQ-NNN |

### Revision history

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-10 | First issue of the RES domain guide, aligned to the rewritten MCF-RES control records, per-control gate mapping and canonical vocabularies. |

## 1 Purpose and scope

This guide explains how the Resilience, Continuity and Recovery (RES) domain is assessed. RES is the integrating domain of AIDCF: it does not own power, cooling, compute, storage or network systems, but it owns the questions that cut across them. What minimum outcome must survive? Where are the fault domains and how far can a failure spread? What happens when capacity is partially lost? How is the capability restored, in what order and how fast? Has any of this been demonstrated?

The guide is informative except where a statement carries a DG-RES-REQ identifier. The 24 RES controls in AIDCF-007A are normative; if this guide and a control record disagree, the control record prevails and the discrepancy shall be raised as a baseline issue.

In scope:

- Minimum service outcomes, impact tolerances and business-impact analysis for each Capability Instance.
- Graceful degradation: planned reduction of AI service under partial loss.
- Scenario libraries, site fault-domain models, containment boundaries, blast-radius analysis and isolation validation.
- Continuity strategy, alternate capacity, site and provider continuity, and crisis priorities.
- Recovery dependencies (including circular and cold-start dependencies), black-start and restoration sequencing across power, cooling, network, storage, compute and control plane, configuration restoration, and data and checkpoint recovery.
- Component tests, integrated scenario tests, tabletop exercises and the lessons-and-retest loop.
- Crisis command, stakeholder communications, emergency change and post-event adaptation.

Domain-specific recovery mechanics remain in their domains: POW-024 (electrical black-start and restoration), THM-024 (thermal recovery), CMP-023 (node rebuild), STO-019 (storage recovery sequencing), NET-015 (OOB resilience). RES assesses whether these compose into an end-to-end, tested restoration of the Service Outcome.

## 2 Why this domain matters for AI capability

AI infrastructure changes the resilience problem in four ways.

1. **Concentration.** A single training job can occupy tens of thousands of accelerators in one hall or campus. A failure that a conventional data centre would absorb as the loss of a few tenants' racks can halt the whole Capability Instance. Blast radius must therefore be expressed in capability terms (accelerator-hours, jobs, tokens per second), not in racks or kilowatts.
2. **Tight coupling.** Synchronous training means the failure of any participant stops progress for all participants. Resilience for training is largely achieved not by keeping every component running but by **checkpointing** and **fast restart**: the impact of a failure is the work lost since the last checkpoint plus the time to detect, replace or exclude the failed component and restart. Lost work is a first-class impact measure.
3. **Power and thermal dynamics.** AI loads can change by large fractions of rated capacity in seconds as jobs start, synchronise and checkpoint. Restoration after a site event must manage load steps against generator and UPS capability and must not bring heat load online before heat removal is re-established. Liquid-cooled systems have limited thermal ride-through, so cooling restoration and IT load sequencing are coupled.
4. **Digital control-plane dependency.** Restoration depends on identity, time, DNS, orchestration, image repositories and licence services that are frequently hosted on the very infrastructure being restored. These circular dependencies are among the most common reasons recovery plans fail on first real use.

RES controls therefore provide most of the CRITICAL evidence for **CG-09 Failure containment** and **CG-10 Recovery readiness**, and they supply the tolerances against which every other domain's resilience claims are judged.

## 3 Reference patterns and variants

### 3.1 Resilience strategies

| Strategy | Typical use | Key RES evidence |
|---|---|---|
| In-site redundancy with checkpoint restart | Large single-site training | Fault-domain model, checkpoint policy, restart tests |
| Active-active multi-site | Latency-tolerant inference serving | Alternate capacity tests, DCI diversity, traffic failover |
| Warm standby capacity | Priority fine-tuning or sovereign workloads | Relocation tests, image and data compatibility |
| Contracted burst capacity (cloud) | Overflow and continuity for inference or smaller training | Contract terms, activation tests, data transfer analysis |
| Recovery-capacity pool (AIDCF-013) | Shared reserve across Capability Instances | Priority scheme, reservation enforcement |
| Accepted suspension | Non-critical research training | Approved acceptance, tolerance justification |

### 3.2 Impact tolerance framing

Impact tolerance is the maximum disruption a Capability Instance can sustain before the consequence becomes intolerable to its stakeholders. Financial-sector operational resilience regimes (for example the UK important-business-services and impact-tolerance approach, and the EU Digital Operational Resilience Act) use similar framing; AIDCF applies it to AI capability. Typical dimensions:

- **Maximum tolerable disruption** (duration).
- **Minimum retained capacity** in DEGRADED or EMERGENCY state.
- **Maximum lost work** (training) or **maximum failed requests** (inference).
- **Recovery time objective (RTO)** and **recovery point objective (RPO)**; for training, RPO is effectively the checkpoint interval plus any un-replicated checkpoints.
- **Integrity tolerance**: zero tolerance for silent model or data corruption is typical; recovery must restore a verified state.

### 3.3 Restoration architecture

The canonical recovery chain in AIDCF-013 is *detection → decision → containment → alternate capacity → restore → validate*. For a site-wide event, the restoration layer order is:

1. **Power**: utility return or generator start; distribution re-energisation in controlled steps; UPS recharge management.
2. **Cooling**: heat rejection, facility water and chilled water, then CDUs and secondary loops, confirmed stable before IT load.
3. **Out-of-band and core network**: OOB first (it is the tool for everything else), then core and management networks.
4. **Core services**: time, DNS, DHCP, IPAM, AAA and identity, ideally from fallbacks that do not depend on the main cluster.
5. **Storage**: metadata services and quorum before data services; integrity checks before admitting clients.
6. **Compute**: BMC reachability, firmware validation, health checks and burn-in before admission; staged power-on to respect load-step limits.
7. **AI control plane**: cluster manager, scheduler, image registry, then workload admission by priority.
8. **Validation**: Service Outcome checks (benchmarks, test jobs, inference canaries), not only system availability.

## 4 Required functions and capability linkage

| Required Function | Principal RES controls |
|---|---|
| Define minimum outcome and impact tolerance | RES-001, RES-012 |
| Degrade gracefully under partial loss | RES-002 |
| Anticipate credible scenarios | RES-003 |
| Own resilience across boundaries | RES-004 |
| Bound failure propagation | RES-005, RES-006, RES-007, RES-008 |
| Sustain or resume the outcome elsewhere | RES-009, RES-010, RES-011 |
| Restore the outcome within tolerance | RES-013, RES-014, RES-015, RES-016 |
| Demonstrate and improve resilience | RES-017, RES-018, RES-019, RES-020 |
| Command and adapt during and after crises | RES-021, RES-022, RES-023, RES-024 |

**DG-RES-REQ-001** An assessor shall not evaluate any RES-02 to RES-05 control as CONFORMING for a Capability Instance whose minimum service outcome and impact tolerance (RES-001) are absent or unapproved; the affected results shall be recorded as UNKNOWN with a US5 UNKNOWN Record against RES-001.

## 5 Dependencies, fault domains and common-mode concerns

### 5.1 The site fault-domain model

RES-005 requires a single fault-domain model covering electrical distribution paths and UPS systems, cooling strings and CDU groups, fire compartments, water zones, network planes, compute pods, storage failure domains and control-plane clusters, reconciled to as-built evidence. Its value is in the **overlaps**: redundant network spines inside one UPS output, storage replicas in one fire compartment, control-plane quorum members in one rack, both CDUs of a pair on one electrical board. The model is most efficiently held as a graph using AIDCF-014 classes (FaultDomain, Dependency, InfrastructureSystem, AssetInstance) and SHARES_FAULT_DOMAIN_WITH relationships, so that redundancy claims can be tested by query.

### 5.2 Recovery dependencies and circularity

Recovery dependencies are often different from operating dependencies. Examples that RES-013 should surface:

- Identity provider hosted on the cluster it unlocks (AIDCF-004 X19).
- DNS required to resolve the time server, while certificates fail until time is correct.
- Node images and firmware bundles stored only on the failed storage system.
- Licence servers for storage or orchestration software on the failed cluster.
- BMS/EPMS historian or engineering workstation virtualised on the failed IT platform.
- Runbooks and contact lists held only in a corporate wiki behind the failed identity provider.
- Key individuals for whom no alternate exists (shared human dependency, DEP-008).

Each cycle needs a documented break: an offline copy, a local fallback, an out-of-band path or a manual procedure, stored outside the failure domain it serves.

### 5.3 Common-mode concerns specific to resilience

- **Common-mode in recovery**: the same automation, image or configuration baseline used to restore every node can reintroduce a defect everywhere (X15). Recovery must restore a verified, pre-incident baseline.
- **Common-mode in alternate capacity**: a cloud burst contract offers little continuity if the regional cloud and the primary site share grid, carrier or weather exposure, or if the alternate is oversubscribed during the same event.
- **Common-mode in people**: crisis command, facility engineering and platform operations may all depend on a small group of individuals; exercises reveal this.

## 6 Threats, hazards and failure scenarios with propagation paths to Service Outcomes

RES uses the full AIDCF-004 scenario library. The cross-domain scenarios most often decisive for RES gate results are below.

| Scenario | Path summary | Service Outcome effect | RES controls exercised |
|---|---|---|---|
| X01 Utility loss + generator no-start + UPS autonomy exhaustion | Utility loss → UPS carries load → one generator fails to start → autonomy consumed → load shed or drop | Training halts; lost work equals time since last checkpoint; inference availability depends on shedding | RES-002, RES-012, RES-014, RES-016, RES-018 |
| X02 Cooling loss at sustained AI load | Chiller or CDU failure → supply temperature rise → thermal throttling → protective shutdown | Throughput falls then halts; restart constrained by cooling recovery | RES-002, RES-014, RES-018 |
| X04 Maintenance removes hidden shared dependency | Planned isolation of one path → hidden shared element removes the redundant path | Unplanned outage during maintenance | RES-005, RES-007, RES-008 |
| X05 BMS/EPMS compromise or malfunction | Malicious or faulty command → setpoint or mode change → plant response | Thermal or electrical continuity defeated; recovery needs trusted configuration | RES-015, RES-019, RES-021 |
| X08 Firmware rollout common-mode failure | Update pushed broadly → identical failure across domains | Large blast radius; recovery depends on rollback and image availability | RES-007, RES-013, RES-015 |
| X09 Fire disables paired infrastructure routes | Fire in one compartment → paired cable or pipe routes both affected | Loss of both "redundant" paths | RES-005, RES-006, RES-008 |
| X15 Recovery reintroduces corrupt configuration | Restore from drifted or compromised backup | Fault recurs after recovery | RES-015, RES-020 |
| X18 Loss of remote OEM support | Supplier unavailable during incident | Diagnosis and repair delayed | RES-011, RES-013 |
| X19 Shared authentication service failure | Identity provider outage → no administrative access | Recovery blocked | RES-013, RES-014 |
| X20 Compound flood/fire/grid/telecom event | Several initiators coincide | Site loss | RES-009, RES-010, RES-021 |

Recovery-induced failures deserve specific attention: simultaneous power-on of thousands of nodes can exceed generator load-step capability; restoring IT load before CDUs and secondary loops are primed and stable can trip thermal protection; starting storage data services before metadata quorum can cause inconsistency; and admitting workloads before health checks can propagate faulty nodes into jobs.

## 7 Safeguards

| Safeguard function | RES contribution |
|---|---|
| Anticipate | Scenario library (RES-003); business-impact analysis (RES-001) |
| Prevent | Fault-domain design and containment boundaries (RES-005, RES-006) |
| Detect | Component and integrated tests (RES-017, RES-018) reveal latent failure |
| Decide | Crisis command and priorities (RES-021, RES-012) |
| Respond | Graceful degradation (RES-002); emergency change (RES-023) |
| Contain | Blast-radius limits and isolation validation (RES-007, RES-008) |
| Withstand | Continuity strategy and alternate capacity (RES-009, RES-010, RES-011) |
| Degrade gracefully | Priority preemption, power capping and checkpoint-and-drain (RES-002) |
| Recover | Recovery dependencies, sequencing, configuration and checkpoint restoration (RES-013 to RES-016) |
| Adapt | Lessons and retest; post-event adaptation (RES-020, RES-024) |

## 8 Critical-gate linkage

| Gate | Name | CRITICAL controls | SUPPORTING controls |
|---|---|---|---|
| CG-01 | Capability and outcome definition | — | RES-001, RES-009, RES-012 |
| CG-02 | Boundary and architecture integrity | — | RES-005 |
| CG-03 | Critical dependency visibility | — | RES-003, RES-005, RES-007, RES-010, RES-011, RES-013 |
| CG-04 | Life safety and hazardous energy | — | RES-008 |
| CG-05 | Resilient electrical supply | — | RES-014, RES-017, RES-018 |
| CG-06 | Thermal continuity | — | RES-014, RES-017, RES-018 |
| CG-07 | Critical control-system integrity | — | RES-015 |
| CG-08 | Compute, storage and network functional integrity | — | RES-016 |
| CG-09 | Failure containment | RES-005, RES-007, RES-008 | RES-001, RES-002, RES-003, RES-006, RES-018 |
| CG-10 | Recovery readiness | RES-013, RES-014, RES-016, RES-018 | RES-001, RES-002, RES-003, RES-009, RES-010, RES-011, RES-012, RES-015, RES-017, RES-019, RES-020, RES-021 |
| CG-13 | Responsibility and authority | — | RES-004, RES-019, RES-021, RES-022 |
| CG-14 | Change control | — | RES-015, RES-020, RES-023, RES-024 |

Rationale for the CRITICAL assignments:

- **CG-09**: RES-005 (fault-domain model reconciled to as-built), RES-007 (blast radius quantified against tolerance) and RES-008 (isolation validated) together are the containment argument. If the model is wrong, the blast radius unknown, or isolation untested, containment is asserted rather than demonstrated.
- **CG-10**: RES-013 (recovery dependencies including circularity), RES-014 (tested restoration sequence), RES-016 (checkpoint and data recovery) and RES-018 (integrated scenario tests) are each necessary for recovery readiness. RES-015 (configuration restoration) is SUPPORTING because CG-10 also draws on domain-specific restoration controls (for example NET-022, CMP-016, STO-019) and SEC-024; a gap in RES-015 requires gate-level evaluation of whether those controls compensate.

RES-001 is SUPPORTING for CG-01, CG-09 and CG-10 rather than CRITICAL, because a missing tolerance is handled more strongly: it raises a US5 UNKNOWN (DG-RES-REQ-001), which caps the decision at INCONCLUSIVE regardless of gate results.

## 9 Capability-profile parameters

All values are illustrative defaults to be set per capability profile with a recorded basis.

| Control | Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|---|
| RES-001 | Maximum tolerable disruption (training outcome) | h | Business-impact derived (illustrative 24) | ISO/TS 22317-style impact analysis; capability-specific. |
| RES-001 | Maximum tolerable disruption (inference outcome) | min | Business-impact derived (illustrative 15) | Capability-specific. |
| RES-001 | Maximum lost training progress | h of cluster time | Equal to checkpoint interval plus restart time (illustrative 2) | Links to RES-016. |
| RES-001 | Minimum retained capacity in DEGRADED state | % of nominal | 50 (illustrative) | Capability-profile parameter. |
| RES-002 | Time to shed load to residual target | min | Less than UPS autonomy minus margin (illustrative 5) | Derived from POW and THM ride-through. |
| RES-002 | Accelerator power-cap floor | % of TDP | Vendor-supported range (illustrative 60) | Capability-profile parameter; vendor limits apply. |
| RES-005 | Fault-domain model reconciliation age | days | 180 (illustrative) | Capability-profile parameter. |
| RES-007 | Maximum blast radius per single credible failure | % of Capability Instance capacity | Impact-tolerance derived (illustrative 25) | Capability-profile parameter. |
| RES-008 | Isolation validation cycle | months | 24 (illustrative) | Capability-profile parameter. |
| RES-010 | Alternate capacity activation time | h | Within maximum tolerable disruption (illustrative 8) | Derived from RES-001. |
| RES-010 | Relocation test interval | months | 12 (illustrative) | Capability-profile parameter. |
| RES-011 | Provider continuity evidence age | months | 12 (illustrative) | Capability-profile parameter. |
| RES-014 | Target black-start-to-service time | h | Within RTO (illustrative 12) | Derived from RES-001. |
| RES-014 | Maximum IT load step during restoration | % of generator rating | Generator- and UPS-specific (illustrative 25) | From POW-020 load-step analysis. |
| RES-014 | Integrated restoration test interval | months | 24 (illustrative) | Capability-profile parameter. |
| RES-015 | Configuration backup interval | h | 24 or on change (illustrative) | Capability-profile parameter. |
| RES-015 | Restore test interval per class | months | 12 (illustrative) | Capability-profile parameter. |
| RES-016 | Checkpoint interval | min | Optimised from failure rate and checkpoint cost (illustrative 60) | Young/Daly-style approximation; capability-specific. |
| RES-016 | Durable checkpoint copies outside cluster failure domain | count | 1 (illustrative) | Capability-profile parameter. |
| RES-016 | Restart-from-checkpoint time | min | Within RTO (illustrative 30) | Derived from RES-001. |
| RES-017 | Programme adherence target | % of scheduled tests completed on time | 95 (illustrative) | Capability-profile parameter. |
| RES-018 | Integrated test cycle | months | 24 (illustrative) | Capability-profile parameter. |
| RES-018 | Representative load during test | % of design IT load | As high as safely authorised (illustrative 70) | Load banks or real workload; site-specific. |
| RES-019 | Tabletop cycle | months | 6 (illustrative) | Capability-profile parameter. |
| RES-020 | Maximum age of open gate-critical lesson | days | 90 (illustrative) | Capability-profile parameter. |
| RES-021 | Crisis command activation time | min from trigger | 30 (illustrative) | Capability-profile parameter. |
| RES-023 | Emergency change retrospective review deadline | working days | 5 (illustrative) | Capability-profile parameter. |
| RES-024 | Post-event review deadline | days | 30 (illustrative) | Capability-profile parameter. |

Note on checkpoint interval. For a job with checkpoint cost *C* (time to write a checkpoint) and mean time between job-interrupting failures *M*, a widely used first-order approximation for the interval that minimises expected lost time is √(2·C·M) (Young's approximation, refined by Daly). The capability owner should record *C* and *M* as measured for the Capability Instance and justify the chosen interval against the lost-work tolerance; the approximation is a guide, not a requirement.

## 10 Evidence expectations by claim type

| Control | Claim type | Profile tier | Required classes | Quality floor | Sufficiency floor | Mandatory items |
|---|---|---|---|---|---|---|
| RES-001 | DESIGN | CP-1 | E1+E7 | P3 F3 C2 R3 T2 I2 | S3 | Approved tolerance statement; Business-impact analysis |
| RES-003 | DESIGN | CP-1 | E1+E7 | P3 F3 C2 R3 T2 I2 | S3 | Scenario library; Applicability rationale |
| RES-004 | DESIGN | CP-1 | E1+E7 | P3 F3 C2 R3 T2 I2 | S3 | Appointment record; Responsibility matrix |
| RES-009 | DESIGN | CP-1 | E1+E7 | P3 F3 C2 R3 T2 I2 | S3 | Approved strategy |
| RES-012 | DESIGN | CP-1 | E1+E7 | P3 F3 C2 R3 T2 I2 | S3 | Approved priority scheme |
| RES-005 | IMPLEMENTATION | CP-2 | E1+E2+E3 | P3 F3 C3 R3 T3 I2 | S4 | Fault-domain model; Reconciliation record; Shared-domain register |
| RES-006 | IMPLEMENTATION | CP-2 | E1+E2+E3 | P3 F3 C3 R3 T3 I2 | S4 | Boundary register; Configuration or inspection evidence |
| RES-007 | IMPLEMENTATION | CP-2 | E1+E2+E7 | P3 F3 C3 R3 T3 I2 | S4 | Blast-radius analysis; Exceedance register |
| RES-011 | IMPLEMENTATION | CP-2 | E1+E2+E5 | P3 F3 C3 R3 T3 I2 | S3 | Provider continuity evidence; Reconciliation |
| RES-013 | IMPLEMENTATION | CP-2 | E1+E2+E3 | P3 F3 C3 R3 T3 I2 | S5 | Recovery dependency map; Circular-dependency analysis |
| RES-017 | OPERATION | CP-3 | E3+E4 | P3 F3 C3 R3 T3 I3 | S3 | Test records; Defect records |
| RES-019 | OPERATION | CP-3 | E3+E6 | P3 F3 C3 R3 T3 I3 | S3 | Exercise reports; Action tracker |
| RES-020 | OPERATION | CP-3 | E1+E3 | P3 F3 C3 R3 T3 I3 | S3 | Lessons register; Retest evidence for closed gate-critical items |
| RES-022 | OPERATION | CP-3 | E1+E3 | P3 F3 C3 R3 T3 I3 | S3 | Notification logs; Obligation register |
| RES-023 | OPERATION | CP-3 | E1+E2+E3 | P3 F3 C3 R3 T3 I3 | S3 | Emergency change records; Retrospective reviews |
| RES-024 | OPERATION | CP-3 | E1+E3+E7 | P3 F3 C3 R3 T3 I3 | S3 | Post-event reviews; Reassessment trigger records |
| RES-002 | EFFECTIVENESS | CP-4 | E2+E3+E4 | P3 F4 C3 R4 T3 I3 | S4 | Degradation mode catalogue; Test or event records |
| RES-010 | EFFECTIVENESS | CP-4 | E2+E3+E4 | P3 F4 C3 R4 T3 I3 | S4 | Relocation test record; Contract or reservation evidence |
| RES-015 | EFFECTIVENESS | CP-4 | E2+E3+E4 | P3 F4 C3 R4 T3 I3 | S4 | Restore test records; Integrity verification evidence |
| RES-021 | EFFECTIVENESS | CP-4 | E1+E3+E4+E6 | P3 F4 C3 R4 T3 I3 | S4 | Exercise/event records with timings; Decision logs |
| RES-008 | RESILIENCE | CP-5 | E1+E2+E3+E4 | P4 F4 C4 R4 T3 I3 | S5 | Validation plan; Results for gate-critical boundaries |
| RES-014 | RESILIENCE | CP-5 | E1+E2+E3+E4 | P4 F4 C4 R4 T3 I3 | S5 | Restoration sequence; Integrated test record with stage timings |
| RES-016 | RESILIENCE | CP-5 | E1+E2+E3+E4 | P4 F4 C4 R4 T3 I3 | S5 | Checkpoint policy; Restart test record; Integrity verification logs |
| RES-018 | RESILIENCE | CP-5 | E1+E2+E3+E4 | P4 F4 C4 R4 T3 I3 | S5 | Integrated test records; Safety case |

Typical decisive evidence:

- **DESIGN** (RES-001, RES-003, RES-004, RES-009, RES-012): approved statements and analyses with accountable approval. Tolerances must be measurable and internally consistent (for example RPO compatible with checkpoint interval).
- **IMPLEMENTATION** (RES-005, RES-006, RES-007, RES-011, RES-013): models and registers reconciled to primary as-built sources (single-line diagrams, P&IDs, rack power and cooling maps, fabric topology, scheduler and storage placement). Reconciliation by a party other than the author.
- **OPERATION** (RES-017, RES-019, RES-020, RES-022, RES-023, RES-024): records across a representative period showing the programme runs as designed, with exceptions handled.
- **EFFECTIVENESS** (RES-002, RES-010, RES-015, RES-021): tests or events demonstrating the safeguard works under defined adverse conditions, with timings.
- **RESILIENCE** (RES-008, RES-014, RES-016, RES-018): scenario and recovery tests with cross-domain state coverage, independent witnessing and capability-level measurements.

Evidence pitfalls:

- **Plans without tests** support DESIGN only (AIDCF-008 Part XIII, CG-10 decision effect).
- **Component tests are not integrated tests.** A generator that starts on a load bank and a UPS that transfers on a monthly test do not demonstrate that an AI cluster survives utility loss; the interaction under AI load steps must be tested or analysed (RES-018).
- **System availability is not outcome restoration.** "All nodes up" does not demonstrate that training resumed at required throughput from a verified checkpoint.
- **Tabletop exercises evidence decision processes**, not technical recovery.

## 11 Assessment guidance

### 11.1 Start from tolerances

Obtain RES-001 tolerances first. Every later RES judgement compares something against them: degradation residual capacity, blast radius, alternate-capacity activation time, restoration duration, lost work.

### 11.2 Build or obtain the fault-domain and recovery-dependency graph

Where the organisation maintains an AIDCF-014 conformant model, query it for (a) redundancy groups whose members share a FaultDomain, and (b) cycles in recovery DEPENDS_ON relationships. Where it does not, construct a minimum version from as-built documents for the gate-critical outcomes before evaluating RES-005, RES-007 and RES-013.

### 11.3 Walk the restoration sequence

For RES-014, walk the sequence stage by stage with the people who would execute it. At each stage ask: what are the entry criteria, who decides, what credentials and tools are needed and where are they, how long did this take in the last test, and what is the hold point before the next stage? Cross-check against POW-024, THM-024, NET-015, STO-019 and CMP-023 runbooks; inconsistencies between domain runbooks are frequent and material.

### 11.4 Judge test representativeness

Integrated tests are often run at reduced load, on a subset of the estate, or with simulated components. That is acceptable if the representativeness argument is explicit: which behaviours scale linearly, which do not (load steps, thermal transients, subnet-manager sweeps, storage metadata recovery), and what residual UNKNOWN remains.

**DG-RES-REQ-002** An assessor shall record, for every test used as RESILIENCE evidence, the load level, scale, operating states and components exercised, and shall record a U5 coverage-gap UNKNOWN for any gate-critical behaviour that the test did not exercise and that is not covered by analysis.

**DG-RES-REQ-003** An assessor shall not accept a restoration sequence as tested end-to-end unless either a full test occurred or every hand-off between adjacent segment tests was itself tested.

### 11.5 Crisis management evidence

For RES-021 and RES-022, evidence should show that command activated within target time, decisions were taken by the right authority (including authority for controlled shutdown and tenant suspension), decision logs exist, and communications reached stakeholders within contractual and regulatory deadlines. Interview alternates, not only primary role holders.

### 11.6 Key assessment questions by family

- **RES-01 Resilience strategy.** Is there an approved, measurable impact tolerance per Capability Instance, derived from business-impact analysis rather than copied from a service catalogue? Are graceful-degradation actions fast enough relative to UPS autonomy and thermal ride-through, and have they been measured? Does the scenario library include maintenance-induced, recovery-induced and compound scenarios? Does one person hold accountable authority across facility, IT and provider boundaries?
- **RES-02 Fault-domain and containment design.** Has the fault-domain model been reconciled against primary as-built sources, and which redundancy claims fail the shared-domain test? Is blast radius expressed in outcome units and compared with tolerance, including firmware, configuration, identity and automation common modes? Which containment boundaries have been validated at V5 or above, and which only by inspection?
- **RES-03 Continuity planning.** Is the continuity strategy explicit about site loss, provider loss and control-plane loss? Is alternate capacity actually reserved or contracted on terms that hold during a regional surge, and has a relocation been tested end to end including checkpoint transfer? Are provider recovery objectives compatible with the tolerances? Are crisis priorities implemented in scheduler classes, not just written down?
- **RES-04 Recovery planning.** Which recovery prerequisites are hosted on the infrastructure they help recover, and how is each cycle broken? Does the restoration sequence bring cooling up before heat load and respect load-step limits? Has each hand-off between restoration stages been tested? Can configuration be restored from a pre-incident, integrity-verified baseline? Has a training job restarted from checkpoint on different nodes within RTO?
- **RES-05 Testing and exercising.** Does the component test programme run as scheduled, and are failures closed? Which prioritised scenarios have been integrated-tested at representative load, and what did the tests measure at capability level? Do tabletop exercises include cyber-physical and compound scenarios? Are gate-critical lessons closed only after retest?
- **RES-06 Crisis and adaptive response.** Can crisis command activate and communicate without site systems or corporate identity? Who is authorised to order controlled shutdown or tenant suspension, and do alternates know it? Are emergency changes reconciled back to baseline? Do post-event reviews raise reassessment triggers against affected controls and gates?

## 12 Testing safety

Resilience testing is the most hazardous testing in AIDCF. Integrated scenario tests, black-start tests, isolation validation of electrical protection, fire or fluid isolation, and degradation tests that remove power or cooling capacity involve hazardous energy, risk to equipment and risk to customer service.

**DG-RES-REQ-004** No integrated scenario, black-start, isolation-validation or capacity-removal test shall be performed without written authorisation from the facility owner, the relevant electrical and mechanical engineering authorities and the capability owner; a safety case; permit-to-work for energised or hazardous work (OPS-007, OPS-008); a named abort authority with defined abort criteria; and a restoration plan.

**DG-RES-REQ-005** Live capability exercises at AIDCF-004 validation level V7 shall additionally require executive authorisation and advance notice to affected tenants and customers.

**DG-RES-REQ-006** Assessors shall not initiate, direct or modify any test; they may observe authorised tests and review records.

Preferred alternatives in order: analysis of real events with good telemetry; segmented tests with tested hand-offs; simulation and digital-twin analysis validated against component tests; tabletop walk-throughs to expose procedural gaps.

## 13 UNKNOWN hot-spots

| Hot-spot | Typical type | Typical severity | Resolution route |
|---|---|---|---|
| Impact tolerance not defined or not approved | U1 | US5 | Capability owner approval (RES-001, CAP-010) |
| Fault-domain model not reconciled to as-built | U3/U5 | US4 (CG-09) | Reconcile to SLD, P&ID, rack maps and topology |
| Circular recovery dependency not analysed | U10 | US4 (CG-10) | Dependency cycle analysis; break documentation |
| Restoration sequence never tested end-to-end | U5 | US4 (CG-10) | Segmented tests with tested hand-offs |
| Checkpoint restart never tested on alternate nodes | U5 | US4 (CG-10) | Restart test at representative scale |
| Integrated test at unrepresentative load | U5 | US3/US4 | Representativeness analysis; higher-load test |
| Provider continuity arrangements undisclosed | U2 | US3 (US4 if sole provider) | Contractual evidence rights; E5 assurance |
| Alternate capacity untested | U1 | US3 (US4 if sole strategy) | Relocation test |
| Post-event review incomplete | U3 | US3 | Complete review; mark evidence STALE meanwhile |

## 14 Interfaces with other domains

| Domain | Interface | Key controls |
|---|---|---|
| CAP | Service Outcomes, criticality and impact tolerance | CAP-008, CAP-010 |
| DEP | Recovery dependency mapping, shared sources and routes, substitution | DEP-004, DEP-005, DEP-007, DEP-016 |
| POW | Electrical black-start, load-step response, UPS runtime | POW-011, POW-020, POW-024 |
| THM | Resilient capacity, thermal recovery, isolation and drainage | THM-003, THM-020, THM-024 |
| NET | Fabric fault domains, OOB resilience, configuration management, core services | NET-004, NET-015, NET-022, NET-024 |
| CMP | Compute fault domains, rollback, node rebuild | CMP-008, CMP-016, CMP-023 |
| STO | Checkpoint durability, restart readiness, storage recovery sequencing | STO-017, STO-018, STO-019 |
| SEC | Break-glass, incident containment, safe rollback | SEC-004, SEC-019, SEC-024 |
| OPS | Permit-to-work, incident response, change, temporary configuration | OPS-007, OPS-014, OPS-018, OPS-019 |
| GOV | Accountability, stakeholder obligations, external reporting | GOV-005, GOV-006, GOV-019, GOV-022 |
| EVA | Change triggers and evidence expiry after events | EVA-021, EVA-022 |

## 15 Informative references

Cited at document level; no clause-level text is reproduced.

- ISO 22301 (Business continuity management systems: requirements); ISO 22313 (guidance); ISO/TS 22317 (business impact analysis); ISO 22316 (organizational resilience); ISO 22320 (incident management).
- ISO/IEC 27031 (ICT readiness for business continuity).
- NIST SP 800-34 Rev. 1 (contingency planning); NIST SP 800-84 (test, training and exercise programmes); NIST SP 800-61 Rev. 3 (incident response).
- IEC 31010 (risk assessment techniques); IEC 60812 (FMEA); IEC 61025 (fault tree analysis).
- Regulation (EU) 2022/2554 (Digital Operational Resilience Act); UK PRA/FCA operational resilience policy.
- ANSI/TIA-942; EN 50600 series / ISO/IEC 22237 series.
- ISA/IEC 62443-2-1 (for OT configuration backup and restoration context).
- AIDCF-004, AIDCF-008, AIDCF-010, AIDCF-013, AIDCF-014.

## 16 Control summary

| Control ID | Title | Control type | Required AL | Claim type | Gate mappings |
|---|---|---|---|---|---|
| MCF-RES-001 | Minimum Service Outcome | DIRECTIVE | AL2 | DESIGN | CG-01 SUPPORTING; CG-10 SUPPORTING; CG-09 SUPPORTING |
| MCF-RES-002 | Graceful Degradation | CORRECTIVE | AL5 | EFFECTIVENESS | CG-09 SUPPORTING; CG-10 SUPPORTING |
| MCF-RES-003 | Resilience Scenarios | DIRECTIVE | AL2 | DESIGN | CG-09 SUPPORTING; CG-10 SUPPORTING; CG-03 SUPPORTING |
| MCF-RES-004 | Resilience Ownership | DIRECTIVE | AL2 | DESIGN | CG-13 SUPPORTING |
| MCF-RES-005 | Fault-Domain Definition | PREVENTIVE | AL3 | IMPLEMENTATION | CG-09 CRITICAL; CG-03 SUPPORTING; CG-02 SUPPORTING |
| MCF-RES-006 | Containment Boundaries | PREVENTIVE | AL3 | IMPLEMENTATION | CG-09 SUPPORTING |
| MCF-RES-007 | Blast Radius | PREVENTIVE | AL3 | IMPLEMENTATION | CG-09 CRITICAL; CG-03 SUPPORTING |
| MCF-RES-008 | Isolation Validation | DETECTIVE | AL5 | RESILIENCE | CG-09 CRITICAL; CG-04 SUPPORTING |
| MCF-RES-009 | Continuity Strategy | DIRECTIVE | AL2 | DESIGN | CG-10 SUPPORTING; CG-01 SUPPORTING |
| MCF-RES-010 | Alternative Capacity | RECOVERY | AL5 | EFFECTIVENESS | CG-10 SUPPORTING; CG-03 SUPPORTING |
| MCF-RES-011 | Site and Provider Continuity | PREVENTIVE | AL3 | IMPLEMENTATION | CG-03 SUPPORTING; CG-10 SUPPORTING |
| MCF-RES-012 | Crisis Priorities | DIRECTIVE | AL2 | DESIGN | CG-10 SUPPORTING; CG-01 SUPPORTING |
| MCF-RES-013 | Recovery Dependencies | RECOVERY | AL3 | IMPLEMENTATION | CG-10 CRITICAL; CG-03 SUPPORTING |
| MCF-RES-014 | Recovery Sequencing | RECOVERY | AL5 | RESILIENCE | CG-10 CRITICAL; CG-05 SUPPORTING; CG-06 SUPPORTING |
| MCF-RES-015 | Configuration Restoration | RECOVERY | AL5 | EFFECTIVENESS | CG-10 SUPPORTING; CG-07 SUPPORTING; CG-14 SUPPORTING |
| MCF-RES-016 | Data and Checkpoint Recovery | RECOVERY | AL5 | RESILIENCE | CG-10 CRITICAL; CG-08 SUPPORTING |
| MCF-RES-017 | Component Tests | DETECTIVE | AL4 | OPERATION | CG-10 SUPPORTING; CG-05 SUPPORTING; CG-06 SUPPORTING |
| MCF-RES-018 | Integrated Scenario Tests | DETECTIVE | AL5 | RESILIENCE | CG-10 CRITICAL; CG-09 SUPPORTING; CG-05 SUPPORTING; CG-06 SUPPORTING |
| MCF-RES-019 | Tabletop Exercises | DETECTIVE | AL4 | OPERATION | CG-10 SUPPORTING; CG-13 SUPPORTING |
| MCF-RES-020 | Lessons and Retest | CORRECTIVE | AL4 | OPERATION | CG-10 SUPPORTING; CG-14 SUPPORTING |
| MCF-RES-021 | Crisis Command | CORRECTIVE | AL5 | EFFECTIVENESS | CG-13 SUPPORTING; CG-10 SUPPORTING |
| MCF-RES-022 | Stakeholder Communications | CORRECTIVE | AL4 | OPERATION | CG-13 SUPPORTING |
| MCF-RES-023 | Emergency Change | CORRECTIVE | AL4 | OPERATION | CG-14 SUPPORTING |
| MCF-RES-024 | Post-Event Adaptation | CORRECTIVE | AL4 | OPERATION | CG-14 SUPPORTING |

## 17 Worked synthetic example

*This example is entirely synthetic. The site, figures and results are invented to illustrate the method and do not describe any real facility, organisation or test.*

**Context.** Synthetic site S-2 hosts Capability Instance CI-T2 (a 4,096-accelerator training cluster, liquid-cooled) and CI-I2 (an inference service on a separate air-cooled hall). Decision question: can CI-T2 be restored to ≥ 90% of nominal training throughput within 12 hours of a site-wide power loss with no more than 2 hours of lost training progress, as of the assessment date?

**Tolerances (RES-001).** Approved: maximum tolerable disruption 24 h; RTO 12 h; maximum lost training progress 2 h; minimum retained capacity in DEGRADED state 50%. Checkpoint interval 45 min, justified with measured checkpoint cost of 90 s and observed job-interrupting failure interval (synthetic) using the Young/Daly approximation.

**Assessment findings.**

| Control | Claim type | Evidence | Result |
|---|---|---|---|
| MCF-RES-005 | IMPLEMENTATION | Fault-domain graph reconciled to SLD, P&ID and rack maps; one CDU pair found fed from the same switchboard section | CONFORMING (shared domain recorded and dispositioned: a second feed was already in the approved change plan and is captured as an accepted limitation with expiry) |
| MCF-RES-007 | IMPLEMENTATION | Blast-radius analysis covers 18 prioritised scenarios; switchboard-section loss removes 50% of CI-T2 cooling, within the 50% DEGRADED minimum | CONFORMING |
| MCF-RES-008 | RESILIENCE | CDU isolation and electrical discrimination validated at V5; fabric partition validated at V5; fire-compartment cable separation validated only at V1 inspection | PARTIAL (Finding: V1 insufficient for a gate-critical boundary without justification) |
| MCF-RES-013 | IMPLEMENTATION | Recovery dependency graph; cycle detection found the image registry for node rebuild hosted on the CI-T2 storage cluster, with no offline copy | NONCONFORMING (cycle without break) |
| MCF-RES-014 | RESILIENCE | Segmented tests: power-to-cooling (site test) and network-to-control-plane (cluster test); hand-off from cooling-stable to staged node power-on not tested | UNKNOWN (U5, US4) |
| MCF-RES-016 | RESILIENCE | Restart test on alternate nodes completed in 22 min; checkpoint integrity verified | CONFORMING |
| MCF-RES-018 | RESILIENCE | Utility-loss test at 60% IT load witnessed independently; jobs checkpointed and drained as designed; representativeness analysis covers load steps | CONFORMING |

**Gate roll-up (SPEC §6.2).**

- **CG-09**: CRITICAL controls RES-005 and RES-007 are CONFORMING; RES-008 is PARTIAL → **FAIL** (also subject to NET-004 and other domains' CRITICAL controls).
- **CG-10**: RES-013 is NONCONFORMING → **FAIL**, irrespective of RES-014 being UNKNOWN and RES-016 and RES-018 being CONFORMING.

**Decision effect and actions.** The decision recommendation is bounded by the AIDCF-010 ceilings for CG-09 and CG-10 FAIL; the US4 UNKNOWN on RES-014 is also carried to CG-12. Actions: place an offline, integrity-verified copy of node images and firmware bundles outside the CI-T2 storage fault domain and re-run cycle detection; test the cooling-stable to staged power-on hand-off with load-step measurements under authorisation; justify or raise the validation level for fire-compartment separation (for example through a fire-engineering review and inspection of cable route separation). Each action carries a reassessment trigger linked to the affected controls and gates.

**What the example illustrates.** The site had strong component and integrated test evidence and a conforming checkpoint regime, yet recovery readiness failed on a single unbroken circular dependency. This is typical: RES assessments most often fail not on whether systems can be restarted, but on whether the things needed to restart them survive the event.
