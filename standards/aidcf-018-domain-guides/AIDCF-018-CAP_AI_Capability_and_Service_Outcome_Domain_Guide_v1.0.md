# AIDCF-018-CAP AI Capability, Service Outcome and Demand Management Domain Guide

## Document control

| Field | Value |
|---|---|
| Document ID | AIDCF-018-CAP |
| Title | AI Capability, Service Outcome and Demand Management Domain Guide |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Parent artifact | AIDCF-018 Domain Guides |
| Normative basis | AIDCF-007A (controls MCF-CAP-001 to MCF-CAP-024), AIDCF-002, AIDCF-006, AIDCF-008, AIDCF-010, AIDCF-013 |
| Requirement prefix | DG-CAP-REQ-NNN |

### Revision history

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-10 | Initial issue: domain guide aligned to the rewritten CAP controls and the control-level gate mappings of AIDCF-010. |

**Normative status.** This guide is informative except for the requirements labelled DG-CAP-REQ-NNN. The normative control requirements are those in the AIDCF-007A registry; the registry prevails if this guide differs. Normative keywords follow ISO/IEC Directives Part 2 usage.

## 1 Purpose and scope

CAP defines the subject of every AIDCF assurance case. The top claim — "Capability Instance X can achieve Service Outcomes Y within tolerances T under declared operating states S, for decision question Q, as of date D" — is meaningless unless X, Y, T and S are defined, owned, measured and kept current. CAP contains 24 controls in six families:

| Family | Name | Controls |
|---|---|---|
| CAP-01 | Capability inventory | MCF-CAP-001 to 004 |
| CAP-02 | Service outcome definition | MCF-CAP-005 to 008 |
| CAP-03 | Criticality and materiality | MCF-CAP-009 to 012 |
| CAP-04 | Demand and growth modelling | MCF-CAP-013 to 016 |
| CAP-05 | Operating envelope | MCF-CAP-017 to 020 |
| CAP-06 | Capability lifecycle and change | MCF-CAP-021 to 024 |

**In scope.** The capability register and ownership of Capability Instances; lifecycle status; linkage to the ArchitectureSnapshot; availability, performance, integrity and recovery Service Outcomes; criticality, impact tolerances, stakeholder consequence and priority classes; measured demand baselines, peak and transient characterisation, growth forecasts and scenario demand; load, environmental, duration and state-specific envelopes; design-to-operation traceability, commissioning acceptance, material change impact and retirement.

**Out of scope.** Whether power, cooling, compute, storage and network *deliver* against the outcomes and envelopes CAP defines — that is assessed in POW, THM, CMP, STO and NET; dependency concentration analysis (DEP); recovery planning and exercises (RES); change execution workflow (OPS); governance authority (GOV); evidence and gate mechanics (EVA).

**Boundary with other domains.** CAP states *what must be achieved and within what limits*; the infrastructure domains show *whether it is achieved*. For example, MCF-CAP-017 defines the CDU loop heat-load limit and verifies it is configured in alarms and capping; the THM domain assesses whether the CDU and facility water system actually remove that heat across states. MCF-CAP-019 validates duration limits (UPS autonomy, thermal ride-through) because those durations are capability properties that bind response and recovery timing; the THM and POW domains own the equipment that produces them.

## 2 Why this domain matters for AI capability

1. **Outcome units differ from facility uptime.** A traditional facility can report full availability of power and cooling while a training job is stalled because one fabric spine failed, accelerators are thermally throttled, or a checkpoint cannot be read. CAP requires outcomes in units of delivered AI work: schedulable healthy accelerators, served requests, training goodput, step-time stability, latency percentiles (MCF-CAP-005, MCF-CAP-006).
2. **Tight coupling makes partial failure total.** Synchronous distributed training advances at the pace of the slowest participant; losing a small fraction of nodes or links can stop the whole job until it restarts from checkpoint. Recovery outcomes therefore include lost training time (RPO) and the order of restoration from facility power to scheduler (MCF-CAP-008).
3. **Demand is dynamic at timescales the facility was not designed for.** Coordinated workloads produce rapid load steps at iteration boundaries, checkpoint pauses, job starts and job failures, and heat load on liquid loops follows those steps. Average telemetry hides them. MCF-CAP-014 requires characterisation at a resolution that resolves the transients, and distribution of that characterisation to the POW and THM design owners and the grid connection owner.
4. **Density and technology change quickly.** Rack power and liquid-cooled fraction grow with each accelerator generation; a capability that was within envelope at commissioning can exceed it after a refresh. MCF-CAP-015 links forecasts to lead times for utility connection and long-lead plant; MCF-CAP-023 treats such refreshes as material change.
5. **Integrity is an outcome.** Silent data corruption on accelerators and corrupted or partial checkpoints are infrastructure-relevant failures with outcome consequences. MCF-CAP-007 makes zero undetected corruption of recovery-critical checkpoints and weights an explicit tolerance with a stated detection mechanism.
6. **Envelopes are narrower and state-dependent.** Liquid-cooled equipment has OEM limits on supply temperature, flow and coolant quality; thermal ride-through on loss of facility water can be short; reduced-redundancy maintenance on one power path requires lower permitted load. MCF-CAP-018 to MCF-CAP-020 make those limits explicit, sourced and enforced.

## 3 Reference patterns and variants

| Pattern | Characteristics | CAP emphasis |
|---|---|---|
| C-P1 Large synchronous training cluster | Thousands of accelerators in pods; high-bandwidth fabric; parallel file system for checkpoints; direct-to-chip liquid cooling | Goodput and step-time outcomes; RPO from checkpoint interval; transient demand; restart staging (MCF-CAP-016) |
| C-P2 Latency-sensitive inference pool | Many smaller replicas; multi-zone or multi-site; air or liquid cooled | Availability and p-percentile latency outcomes; priority classes for degradation; integrity of deployed weights |
| C-P3 Mixed fine-tuning and inference | Shared accelerators, scheduler pre-emption | Priority classification implemented consistently in scheduler and facility shed sequences (MCF-CAP-012) |
| C-P4 Retrofit air-to-liquid hall | Existing building converted for high-density racks | Envelope derivation from lowest-rated path element; commissioning acceptance under heat load; material change impact |
| C-P5 Modular or prefabricated pods | Factory-built power and cooling modules | Commissioning acceptance at capability boundary; architecture linkage for each module |
| C-P6 Colocation tenant capability | Tenant IT in provider facility | Ownership authority across contract (MCF-CAP-002); provider data for baselines and duration limits; U2 UNKNOWN risk |

Variants that change parameters but not controls: training versus inference work type; air, direct-to-chip, rear-door or immersion cooling; single-site versus multi-site recovery.

## 4 Required functions and capability linkage

CAP is where steps 2 to 4 of the canonical chain are established and linked to step 5:

- **Step 2 Capability Instance** — MCF-CAP-001 (register), MCF-CAP-002 (owner), MCF-CAP-003 (lifecycle status).
- **Step 3 Service Outcome** — MCF-CAP-005 to MCF-CAP-008, with tolerances (MCF-CAP-010) and criticality (MCF-CAP-009).
- **Step 4 Required Function** — linked to outcomes and to implementing systems in MCF-CAP-004.
- **Step 5 Architecture** — the ArchitectureSnapshot reference (MCF-CAP-004) and design-to-operation traceability (MCF-CAP-021).
- **Operating states S** — envelopes per state (MCF-CAP-017 to MCF-CAP-020).

Typical Required Functions for an AI Capability Instance, each of which MCF-CAP-004 links to implementing systems:

| Required Function | Implemented by (typical) | Assessed for delivery in |
|---|---|---|
| Deliver conditioned power to accelerators within envelope | Utility, MV/LV distribution, UPS/BESS, generation, busway, rack PDUs, power capping | POW |
| Remove heat from accelerators within OEM envelope | Cold plates, CDUs, technology cooling system, facility water, heat rejection, air handling | THM |
| Provide schedulable healthy accelerators | Nodes, accelerators, firmware, health checking, scheduler | CMP |
| Provide collective communication bandwidth | Scale-up and scale-out fabrics, optics, switches | NET |
| Persist and restore model state and data with integrity | Parallel file system, object store, checkpoint pipeline | STO |
| Govern and monitor infrastructure automation | BMS, EPMS, CDU controllers, DCIM, cluster control plane | SEC, OPS |
| Restore capability after failure | Recovery runbooks, restart staging, checkpoint restore | RES |

## 5 Dependencies, fault domains, common-mode concerns

CAP surfaces common-mode exposure by forcing explicit links from outcomes to shared elements:

- **Shared heat-removal path.** One facility water loop or heat-rejection plant serving several pods or halls; MCF-CAP-004 requires shared elements to be marked, which feeds CG-03 and CG-09 evaluation.
- **Shared storage for checkpoints.** A single parallel file system holding checkpoints for all instances is a common-mode dependency for every recovery outcome; scenario demand (MCF-CAP-016) checks whether simultaneous restore saturates it.
- **Shared control plane and identity.** Scheduler, cluster management and identity services are common to every job; restoration order (MCF-CAP-008) must place them before compute.
- **Demand coupling.** Synchronous workloads couple the electrical behaviour of thousands of racks; a common workload event (job failure, checkpoint) is a common-mode load step across the UPS and generation fault domains (MCF-CAP-014).
- **Lowest-rated element.** Envelope limits derive from the lowest-rated element in each path in the declared redundancy state (MCF-CAP-017); a single under-rated busway or CDU sets the limit for every rack it serves.
- **Shared measurement.** Baselines and outcome metrics that depend on one telemetry pipeline fail together; MCF-CAP-013 requires independent reconciliation for a sample.

## 6 Threats, hazards and failure scenarios with propagation paths to Service Outcomes

| ID | Scenario | Propagation path | Service Outcome effect | Primary CAP safeguards |
|---|---|---|---|---|
| CAP-FS-01 | Accelerator refresh raises rack power beyond the CDU loop rating, not treated as material change | Refresh → higher heat load → CDU loop at limit in N state → pump failure → supply temperature rises → throttling then thermal trips | Performance and availability outcomes breached for the pod | MCF-CAP-023, MCF-CAP-017, MCF-CAP-015 |
| CAP-FS-02 | Transient load steps from synchronous training interact with UPS or generator control | Job-wide step → UPS or genset transient response → protection trip or transfer to bypass → hall-level outage | Availability and recovery outcomes | MCF-CAP-014 (characterisation supplied to POW) |
| CAP-FS-03 | Checkpoint interval longer than tolerated lost training time | Power event → job restarts from old checkpoint → hours of training lost | Recovery outcome (RPO) breached | MCF-CAP-008, MCF-CAP-010 |
| CAP-FS-04 | Simultaneous restart after a site power event | All racks restart → inrush and checkpoint-restore read burst → upstream breaker trip or storage saturation → RTO exceeded | Recovery outcome (RTO) breached | MCF-CAP-016, MCF-CAP-020 |
| CAP-FS-05 | Facility water setpoint raised for efficiency beyond accelerator OEM limit | Setpoint change → reduced margin → throttling under peak | Performance outcome degraded silently while availability reports 100% | MCF-CAP-018, MCF-CAP-006 |
| CAP-FS-06 | Silent data corruption on an accelerator not detected | Corrupted gradients → corrupted checkpoint → restore propagates corruption | Integrity outcome breached; recovery from corrupt state | MCF-CAP-007 |
| CAP-FS-07 | Full AI load maintained during maintenance on one power path | Second fault on remaining path → loss of supply to the pod | Availability outcome; uncontained failure | MCF-CAP-020, MCF-CAP-017 |
| CAP-FS-08 | Load shedding order inconsistent with priority | Power deficit → shed sequence drops critical inference before research training | Highest-criticality outcome breached first | MCF-CAP-012 |
| CAP-FS-09 | Production workload placed on a partially commissioned pod | Deferred CDU failover test → failure in service → no validated transfer | Availability and performance outcomes | MCF-CAP-003, MCF-CAP-022 |

## 7 Safeguards

- **Authoritative register reconciled to the scheduler and asset register** (MCF-CAP-001) — the instance boundary is grounded in what actually runs.
- **Outcomes in AI work units with measurement sources** (MCF-CAP-005 to MCF-CAP-008), which make infrastructure-induced degradation visible.
- **Approved, testable impact tolerances** within risk appetite (MCF-CAP-010, MCF-GOV-014).
- **Priority classes implemented consistently** in scheduler pre-emption, power capping, load-shed sequences and thermal curtailment (MCF-CAP-012).
- **Measured demand with transient characterisation** shared with power, cooling and grid owners (MCF-CAP-013, MCF-CAP-014).
- **Scenario demand staging validated in exercise** (MCF-CAP-016).
- **Enforced load and environmental envelopes** derived from lowest-rated elements and OEM specifications (MCF-CAP-017, MCF-CAP-018).
- **Validated duration limits with response margin** in alarms and runbooks (MCF-CAP-019).
- **State-specific limits** in permits, freezes, scheduler policies and capping profiles (MCF-CAP-020).
- **Integrated commissioning acceptance** under heat load with failure transfers (MCF-CAP-022).
- **Capability impact assessment for every material change** with post-change validation and reassessment triggers (MCF-CAP-023).

## 8 Critical-gate linkage

CAP provides most of the CRITICAL controls for CG-01 (Capability and outcome definition), one of the two CG-02 CRITICAL controls held in the CAP and EVA domains, the capability-owner control for CG-13, and the capability-impact control for CG-14.

| Gate | CRITICAL controls in this domain | SUPPORTING controls in this domain |
|---|---|---|
| CG-01 | MCF-CAP-001 Capability Register (IMPLEMENTATION)<br>MCF-CAP-005 Availability Outcomes (DESIGN)<br>MCF-CAP-006 Performance Outcomes (DESIGN)<br>MCF-CAP-007 Integrity Outcomes (DESIGN)<br>MCF-CAP-008 Recovery Outcomes (DESIGN)<br>MCF-CAP-010 Impact Tolerance (DESIGN) | MCF-CAP-002, MCF-CAP-003, MCF-CAP-004, MCF-CAP-009, MCF-CAP-011, MCF-CAP-023 |
| CG-02 | MCF-CAP-004 Architecture Linkage (IMPLEMENTATION) | MCF-CAP-021, MCF-CAP-022, MCF-CAP-024 |
| CG-03 | — | MCF-CAP-004 |
| CG-04 | — | MCF-CAP-024 |
| CG-05 | — | MCF-CAP-012, MCF-CAP-013, MCF-CAP-014, MCF-CAP-016, MCF-CAP-017, MCF-CAP-019 |
| CG-06 | — | MCF-CAP-012, MCF-CAP-013, MCF-CAP-014, MCF-CAP-017, MCF-CAP-018, MCF-CAP-019 |
| CG-08 | — | MCF-CAP-006, MCF-CAP-007, MCF-CAP-022 |
| CG-09 | — | MCF-CAP-020 |
| CG-10 | — | MCF-CAP-008, MCF-CAP-016, MCF-CAP-019, MCF-CAP-020 |
| CG-13 | MCF-CAP-002 Capability Ownership (IMPLEMENTATION) | — |
| CG-14 | MCF-CAP-023 Material Change Impact (OPERATION) | MCF-CAP-003, MCF-CAP-022, MCF-CAP-024 |

Notes on the mapping:

- **CG-01.** The register (MCF-CAP-001), the four outcome-definition controls (MCF-CAP-005 to MCF-CAP-008) and impact tolerance (MCF-CAP-010) are CRITICAL because each defines an element of the top claim (X, Y or T). MCF-EVA-009 (Decision Question) is the further CRITICAL control for CG-01, held in EVA. Criticality criteria, stakeholder consequence, lifecycle status and change impact are SUPPORTING: they improve the definition but their absence does not by itself leave X, Y or T undefined.
- **CG-02.** Architecture linkage (MCF-CAP-004) is CRITICAL because an assessment boundary that is not grounded in the current architecture cannot be shown to have integrity. MCF-EVA-010 (Scope and Criteria) is the other CRITICAL control from these domains; further CRITICAL controls for CG-02 are expected from domains that hold as-built reconciliation.
- **CG-13.** MCF-CAP-002 is CRITICAL alongside four GOV controls.
- **CG-14.** MCF-CAP-023 is CRITICAL: a material change that is not capability-impact assessed directly defeats the gate scope. Commissioning acceptance, lifecycle status and retirement are SUPPORTING.
- **CG-05, CG-06, CG-08, CG-09, CG-10.** CAP controls are SUPPORTING. They supply the demand, envelope, duration and outcome definitions against which the infrastructure domains' CRITICAL controls are judged. A NONCONFORMING CAP result here requires gate-level evaluation (for example, CG-06 cannot conclude thermal continuity is sufficient if the heat load it is compared against is unmeasured).
- **CG-04.** Retirement control (MCF-CAP-024) is SUPPORTING because draining liquid loops and removing batteries are hazardous activities.
- **CG-11 and CG-12** are meta-gates evaluated across all controls and are not mapped per control.

**DG-CAP-REQ-001** Where a CAP control that is SUPPORTING for CG-05, CG-06 or CG-10 is NONCONFORMING or UNKNOWN, the gate-level evaluation shall state whether the capacity, envelope or duration figure on which the gate's CRITICAL controls relied is still supported, and shall treat an unsupported figure as a gate criterion not demonstrated.

## 9 Capability-profile parameters

All defaults are illustrative and shall be replaced by values approved in the capability profile. Where the default reads "measured" or "validated", the value is a characteristic of the instance to be established by evidence, not a design choice.

| Control | Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|---|
| MCF-CAP-001 | Capability register reconciliation interval | months | 3 | Capability-profile parameter; illustrative, aligned to the rate of cluster expansion |
| MCF-CAP-004 | Architecture reconciliation interval | months | 6 | Capability-profile parameter; illustrative |
| MCF-CAP-005 | Availability target | % of measurement window | 99.5 (training) / 99.9 (inference) | Capability-profile parameter set by the capability owner; illustrative only |
| MCF-CAP-005 | Availability measurement window | days | 30 | Capability-profile parameter; illustrative |
| MCF-CAP-005 | Maximum single-interruption duration | minutes | 60 | Capability-profile parameter; illustrative, derived from impact tolerance |
| MCF-CAP-006 | Training goodput floor | % of wall-clock time doing useful training progress | 90 | Capability-profile parameter; illustrative |
| MCF-CAP-006 | Inference latency percentile and bound | ms at p99 | set per service | Capability-profile parameter; no generic default |
| MCF-CAP-006 | Throttling event tolerance | accelerator-hours throttled per week | 0 attributable to facility conditions | Capability-profile parameter; illustrative |
| MCF-CAP-007 | Checkpoint integrity verification point | event | on write and before restore | Capability-profile parameter; illustrative |
| MCF-CAP-007 | Tolerated detection latency for dataset corruption | hours | 24 | Capability-profile parameter; illustrative |
| MCF-CAP-008 | Recovery time objective | hours to restore stated capacity | 4 to 80% capacity | Capability-profile parameter; illustrative |
| MCF-CAP-008 | Recovery point objective (training) | minutes of lost training | 30 | Capability-profile parameter; illustrative, constrained by checkpoint write time |
| MCF-CAP-008 | Recovered capacity fraction for RTO | % of committed accelerators | 80 | Capability-profile parameter; illustrative |
| MCF-CAP-010 | Maximum tolerable interruption | hours | 8 | Capability-profile parameter; illustrative |
| MCF-CAP-010 | Maximum tolerable capacity reduction | % of committed capacity for stated duration | 50% for 24 h | Capability-profile parameter; illustrative |
| MCF-CAP-010 | Maximum tolerable lost training progress | hours of training | 2 | Capability-profile parameter; illustrative |
| MCF-CAP-012 | Priority reconciliation interval | months | 6 | Capability-profile parameter; illustrative |
| MCF-CAP-013 | Baseline period | days | 90 | Capability-profile parameter; illustrative, should include representative workload cycles |
| MCF-CAP-013 | Baseline telemetry resolution | seconds | 60 | Capability-profile parameter; illustrative, transient characterisation is addressed in MCF-CAP-014 |
| MCF-CAP-013 | Baseline refresh interval | months | 3 | Capability-profile parameter; illustrative |
| MCF-CAP-014 | Transient measurement resolution | ms | 100 or finer | Capability-profile parameter; illustrative, must resolve the fastest step of interest |
| MCF-CAP-014 | Maximum load step change | % of pod IT load | measured; no default | Measured characteristic, not a design default |
| MCF-CAP-014 | Maximum ramp rate | kW per second per pod | measured; no default | Measured characteristic, not a design default |
| MCF-CAP-015 | Planning horizon | months | 36 | Capability-profile parameter; illustrative |
| MCF-CAP-015 | Forecast review interval | months | 6 | Capability-profile parameter; illustrative |
| MCF-CAP-016 | Scenario demand exercise interval | months | 12 | Capability-profile parameter; illustrative |
| MCF-CAP-016 | Restart staging group size | % of instance accelerators per step | 25 | Capability-profile parameter; illustrative |
| MCF-CAP-017 | Design margin below lowest-rated element | % of rating | 10 | Capability-profile parameter; illustrative |
| MCF-CAP-018 | Air inlet temperature range | degC | 18-27 | ASHRAE TC 9.9 recommended envelope for air-cooled IT; OEM limits prevail where stricter |
| MCF-CAP-018 | Technology cooling system supply temperature upper limit | degC | per OEM specification | OEM specification; no generic default |
| MCF-CAP-019 | Duration validation interval | months | 12 | Capability-profile parameter; illustrative |
| MCF-CAP-019 | Thermal ride-through on loss of facility water | minutes | validated value; no default | Validated characteristic, not a design default |
| MCF-CAP-019 | Response margin before limit | % of validated duration | 50 | Capability-profile parameter; illustrative |
| MCF-CAP-020 | Maximum IT load in reduced-redundancy maintenance | % of normal envelope | per redundancy study; no default | Derived from POW/THM redundancy studies |
| MCF-CAP-021 | Traceability reconciliation interval | months | 12 | Capability-profile parameter; illustrative |
| MCF-CAP-022 | Commissioning test load | % of design IT load | 100 | Capability-profile parameter; illustrative, using load banks or representative workloads |
| MCF-CAP-024 | Record update time after retirement | working days | 10 | Capability-profile parameter; illustrative |

**DG-CAP-REQ-002** A capability profile shall not adopt an illustrative default from this table without recording the basis for its applicability to the Capability Instance.

## 10 Evidence expectations by claim type

| Claim type | Controls | Profile tiers | Required classes (union) | Sufficiency floors |
|---|---|---|---|---|
| DESIGN | MCF-CAP-005, MCF-CAP-006, MCF-CAP-007, MCF-CAP-008, MCF-CAP-009, MCF-CAP-010, MCF-CAP-011, MCF-CAP-015 | CP-1 | E1+E2+E6+E7 | S3 |
| IMPLEMENTATION | MCF-CAP-001, MCF-CAP-002, MCF-CAP-004, MCF-CAP-012, MCF-CAP-017, MCF-CAP-018, MCF-CAP-021, MCF-CAP-024 | CP-2 | E1+E2+E3+E4+E6+E7 | S3 |
| OPERATION | MCF-CAP-003, MCF-CAP-013, MCF-CAP-014, MCF-CAP-020, MCF-CAP-023 | CP-3 | E1+E2+E3+E7 | S4 |
| EFFECTIVENESS | MCF-CAP-019, MCF-CAP-022 | CP-4 | E1+E2+E3+E4 | S4 |
| RESILIENCE | MCF-CAP-016 | CP-5 | E1+E3+E4+E7 | S5 |

- **DESIGN (AL2).** Outcome, tolerance and criticality controls are DESIGN claims: they are satisfied by approved definitions (E1) with derivations or reconciliations (E7), and with a measurement data source shown to exist. A definition that cannot be measured is PARTIAL against its measurement criterion.
- **IMPLEMENTATION (AL3).** Register, ownership, architecture linkage, priority classes, envelopes and traceability require technical state (E2): scheduler inventories, configuration exports of capping, admission control, BMS/CDU setpoints and shed sequences, reconciled to the definitions. Exports should be taken by query executed or witnessed by the assessor.
- **OPERATION (AL4).** Demand baselines and transients, lifecycle status, state-specific limits and change impact require operational records (E3) over representative periods and states. For transients, captures at a resolution that resolves the step are required; interval-averaged telemetry is not acceptable evidence of the absence of transients.
- **EFFECTIVENESS (AL5).** Duration limits and commissioning acceptance require tests (E4) at representative load with recorded conditions, plus supporting E2/E3. A calibrated model may substitute for a thermal ride-through test where testing production accelerators would be unsafe.
- **RESILIENCE (AL5).** Scenario demand requires a recovery exercise (or real event) that measured demand against the model and staging, with cross-domain E2/E3. A model alone supports only DESIGN.

## 11 Assessment guidance

**Sequence.**

1. Register and boundary: MCF-CAP-001, MCF-CAP-002, MCF-CAP-003, MCF-CAP-004 (with MCF-EVA-010). Stop and raise US5 if the instance boundary cannot be grounded.
2. Outcomes and tolerances: MCF-CAP-005 to MCF-CAP-011. These must be fixed before any infrastructure domain can conclude.
3. Demand and envelopes: MCF-CAP-013, MCF-CAP-014, MCF-CAP-017, MCF-CAP-018. Hand the results to POW and THM specialists before they assess capacity.
4. Priority and state-specific limits: MCF-CAP-012, MCF-CAP-020.
5. Validation: MCF-CAP-019, MCF-CAP-022, MCF-CAP-016 — schedule early because they depend on test windows.
6. Lifecycle and change: MCF-CAP-021, MCF-CAP-023, MCF-CAP-024, MCF-CAP-015.

**Interviews.** Capability owner and deputy; AI platform owner (scheduler, health checks, checkpointing); capacity manager; capability architect; electrical and mechanical leads; commissioning manager; grid connection owner; tenant representatives for stakeholder consequence; facility operator duty manager for state-specific limits.

**Inspections and extractions.** Scheduler inventory (clusters, pods, node counts, pre-emption policy); power-capping and admission configuration; EPMS shed sequences; BMS and CDU setpoints and alarm thresholds; checkpoint interval configuration; high-resolution power and heat-load captures; commissioning dossiers; change log.

**Sampling.** Reconcile the scheduler inventory in full (it is usually small enough). For envelope reconciliation, stratify racks, rows and CDU loops by density and by generation; include the highest-density and oldest-rated paths judgementally. For changes, sample both material and non-material classifications to test misclassification (MCF-CAP-023).

**Safe tests.** Reperformance of metric derivations from telemetry; read-only configuration reconciliation; observation of scheduled commissioning and duration tests; recovery exercises run by operators. Assessors do not induce faults.

**DG-CAP-REQ-003** The CAP results for Service Outcomes, impact tolerances and envelopes shall be issued to the infrastructure-domain assessors before those assessors conclude on capacity, continuity or recovery controls, and any later change to those CAP results shall trigger review of the dependent conclusions.

## 12 Testing safety

Several CAP controls rely on tests that are hazardous or service-affecting:

- **Transient captures (MCF-CAP-014)** require connection of power-quality analysers to live switchgear. This is hazardous-energy work performed only by authorised electrical personnel under the site safe system of work, permits and arc-flash PPE selected from the incident-energy study. The assessor observes and does not connect instruments.
- **Duration validation (MCF-CAP-019)** may involve UPS discharge, generator runs or cooling interruption. These require written authorisation from the facility operator and capability owner, an engineered method statement with initial-state verification, abort criteria and restoration steps, load banks or protected test loads where possible, and a safety authority who can stop the test. Thermal ride-through on production accelerators shall not be tested by deliberately stopping cooling; use a calibrated model or measured event.
- **Commissioning (MCF-CAP-022)** involves energised switching, load banks, pressurised liquid loops and induced failures; it requires an approved commissioning method statement, isolations and permits, competent operators and stop authority.
- **Recovery exercises (MCF-CAP-016)** that restart cooling plant or accelerator populations follow the same authorisation chain and must not exceed the supply available in each staging step.
- **Retirement (MCF-CAP-024)** draining of liquid loops and removal of batteries require permits and lock-out/tag-out.

**DG-CAP-REQ-004** No CAP test shall be performed on equipment supporting a production Service Outcome unless the capability owner has accepted, in writing, the outcome risk of the test and its abort criteria, and the safety authority has authorised it.

## 13 UNKNOWN hot-spots and how to resolve them

| Hot-spot | Typical UNKNOWN type | Severity | Resolution route |
|---|---|---|---|
| Scheduler inventory not accessible (provider-operated platform) | U2 | US5 (Capability Instance definition) | Provider export under restriction; provider attestation plus sampled node-level evidence |
| Outcome defined but no measurement source | U1 | US3 for the measurement criterion | Instrument the metric; define data source; first measured window |
| No transient capture at sufficient resolution | U1 | US3 | Arrange authorised capture during representative workloads |
| Liquid heat load not metered at CDU | U1 / U5 | US3 | Install or enable heat metering; interim derivation from flow and temperature difference with stated uncertainty |
| OEM envelope for installed accelerators unavailable | U1 | US3 | Obtain OEM specification under NDA; do not substitute generic guidance without approval |
| Thermal ride-through never validated at current load | U3 Stale / U1 | US3 | Calibrated model validated against a measured event |
| Provider changes not enumerable | U10 | US4 for CG-14 | Contractual change notification; provider change log extract |
| Disputed lifecycle status (production use on commissioning pod) | U5 | US3 | Scheduler and tenancy evidence over the period |

## 14 Interfaces with other domains

| Domain | Interface |
|---|---|
| GOV | Capability owner authority; risk appetite and tolerance approval; customer commitments reconcile to outcomes |
| EVA | Decision question and scope reference CAP instances and outcomes; MCF-CAP-004 grounds MCF-EVA-010 |
| DEP | Shared and external elements identified in MCF-CAP-004 feed dependency and concentration analysis |
| POW | Load envelope, peak and transient demand, duration limits (UPS, fuel), priority shed sequences |
| THM | Heat-load baseline, environmental envelope, thermal ride-through, CDU loop limits |
| CMP | Performance outcomes (goodput, throttling), accelerator health for availability, silent data corruption detection |
| STO | Integrity outcomes, checkpoint interval and restore throughput, retirement sanitisation |
| NET | Performance outcomes dependent on fabric bandwidth; restoration order |
| OPS | Change records, maintenance states, document control for runbooks |
| RES | Recovery outcomes, restoration order, scenario demand exercises |
| SUP | OEM specifications; provider data for colocation instances |
| ENV | Growth forecasts drive energy and water demand projections |
| SEC | Control-plane restoration in recovery order; configuration access for envelope reconciliation |

## 15 Informative references

Document-level references only.

- ASHRAE TC 9.9 — Thermal guidelines for data processing environments; liquid cooling guidelines.
- ASHRAE Guideline 0 and ASHRAE Standard 202 — Commissioning process.
- ISO/IEC 22237 series and EN 50600 series — Data centre facilities and infrastructures.
- ISO/IEC 30134 series — Data centre key performance indicators.
- ISO 50001 — Energy management systems.
- IEC 61000-4-30 — Power quality measurement methods.
- IEC 62040-3 — UPS performance and test requirements; IEEE 1188 — VRLA battery maintenance and testing; ISO 8528 series — Generating sets.
- IEC 60364 series — Low-voltage electrical installations.
- IEC 60300 series — Dependability management.
- ISO 22301, ISO 22317, ISO/IEC 27031 — Business continuity, business impact analysis, ICT readiness.
- ISO/IEC/IEEE 15288 — System life cycle processes; ISO/IEC/IEEE 42010 — Architecture description.
- ISO 55000 series — Asset management.
- ISO/IEC 20000-1 — Service management system.
- ISO/IEC 25010 and ISO/IEC 25012 — Product quality and data quality models.
- ISO/IEC 27040 and NIST SP 800-209 — Storage security; NIST SP 800-88 and IEEE 2883 — Media sanitisation.
- MLCommons MLPerf — Training and inference benchmark suites.
- AIDCF-002, AIDCF-003, AIDCF-013.

## 16 Control summary table

| Control ID | Title | Control type | AL | Claim type | Gate mappings |
|---|---|---|---|---|---|
| MCF-CAP-001 | Capability Register | DIRECTIVE | AL3 | IMPLEMENTATION | CG-01 CRITICAL |
| MCF-CAP-002 | Capability Ownership | DIRECTIVE | AL3 | IMPLEMENTATION | CG-13 CRITICAL; CG-01 SUPPORTING |
| MCF-CAP-003 | Lifecycle Status | DETECTIVE | AL4 | OPERATION | CG-01 SUPPORTING; CG-14 SUPPORTING |
| MCF-CAP-004 | Architecture Linkage | DIRECTIVE | AL3 | IMPLEMENTATION | CG-02 CRITICAL; CG-03 SUPPORTING; CG-01 SUPPORTING |
| MCF-CAP-005 | Availability Outcomes | DIRECTIVE | AL2 | DESIGN | CG-01 CRITICAL |
| MCF-CAP-006 | Performance Outcomes | DIRECTIVE | AL2 | DESIGN | CG-01 CRITICAL; CG-08 SUPPORTING |
| MCF-CAP-007 | Integrity Outcomes | DIRECTIVE | AL2 | DESIGN | CG-01 CRITICAL; CG-08 SUPPORTING |
| MCF-CAP-008 | Recovery Outcomes | DIRECTIVE | AL2 | DESIGN | CG-01 CRITICAL; CG-10 SUPPORTING |
| MCF-CAP-009 | Criticality Criteria | DIRECTIVE | AL2 | DESIGN | CG-01 SUPPORTING |
| MCF-CAP-010 | Impact Tolerance | DIRECTIVE | AL2 | DESIGN | CG-01 CRITICAL |
| MCF-CAP-011 | Stakeholder Consequence | DIRECTIVE | AL2 | DESIGN | CG-01 SUPPORTING |
| MCF-CAP-012 | Priority Classification | PREVENTIVE | AL3 | IMPLEMENTATION | CG-05 SUPPORTING; CG-06 SUPPORTING |
| MCF-CAP-013 | Current Demand Baseline | DETECTIVE | AL4 | OPERATION | CG-05 SUPPORTING; CG-06 SUPPORTING |
| MCF-CAP-014 | Peak and Transient Demand | DETECTIVE | AL4 | OPERATION | CG-05 SUPPORTING; CG-06 SUPPORTING |
| MCF-CAP-015 | Growth Forecast | DIRECTIVE | AL2 | DESIGN | — |
| MCF-CAP-016 | Scenario Demand | RECOVERY | AL5 | RESILIENCE | CG-10 SUPPORTING; CG-05 SUPPORTING |
| MCF-CAP-017 | Load Envelope | PREVENTIVE | AL3 | IMPLEMENTATION | CG-05 SUPPORTING; CG-06 SUPPORTING |
| MCF-CAP-018 | Environmental Envelope | PREVENTIVE | AL3 | IMPLEMENTATION | CG-06 SUPPORTING |
| MCF-CAP-019 | Duration Limits | PREVENTIVE | AL5 | EFFECTIVENESS | CG-05 SUPPORTING; CG-06 SUPPORTING; CG-10 SUPPORTING |
| MCF-CAP-020 | State-Specific Limits | PREVENTIVE | AL4 | OPERATION | CG-09 SUPPORTING; CG-10 SUPPORTING |
| MCF-CAP-021 | Design-to-Operation Traceability | DETECTIVE | AL3 | IMPLEMENTATION | CG-02 SUPPORTING |
| MCF-CAP-022 | Commissioning Acceptance | PREVENTIVE | AL5 | EFFECTIVENESS | CG-02 SUPPORTING; CG-08 SUPPORTING; CG-14 SUPPORTING |
| MCF-CAP-023 | Material Change Impact | PREVENTIVE | AL4 | OPERATION | CG-14 CRITICAL; CG-01 SUPPORTING |
| MCF-CAP-024 | Retirement Control | PREVENTIVE | AL3 | IMPLEMENTATION | CG-14 SUPPORTING; CG-02 SUPPORTING; CG-04 SUPPORTING |

## 17 Worked synthetic example

> **SYNTHETIC EXAMPLE.** All names, organisations, values and results below are invented for illustration. They do not describe any real facility, organisation or assessment, and the figures are not benchmarks.

**Context.** Capability Instance SYN-CI-12 "Inference and Fine-Tune Hall B" (pattern C-P3) serves an internal inference platform and a fine-tuning queue on the same accelerator pool. The hall was converted from air to direct-to-chip liquid cooling 18 months ago (pattern C-P4). Decision question: "Can SYN-CI-12 meet its inference availability and p99 latency outcomes within tolerance through loss of one CDU per row and during single-path power maintenance, as of 2026-09-30?"

**Capability profile values (synthetic).** Inference availability 99.9% per 30-day window; p99 latency bound set per service; maximum single interruption 15 minutes; maximum tolerable capacity reduction 30% for 4 hours; CDU loop limit derived from the lowest-rated element (the row manifold) less the profile margin.

**Fieldwork summary (CAP).**

| Control | Observation | Result |
|---|---|---|
| MCF-CAP-001 | Register reconciled to scheduler last month; 2 nodes unassigned with disposition | CONFORMING (IMPLEMENTATION) |
| MCF-CAP-005 | Availability defined as schedulable healthy accelerators and served requests; measurement source exists | CONFORMING (DESIGN) |
| MCF-CAP-006 | p99 latency outcome defined; no metric for throttling attributable to facility conditions | PARTIAL (DESIGN) |
| MCF-CAP-010 | Tolerances approved and within appetite | CONFORMING (DESIGN) |
| MCF-CAP-012 | Scheduler pre-empts fine-tuning before inference; EPMS shed sequence drops rows in physical order, not by priority | PARTIAL (IMPLEMENTATION) |
| MCF-CAP-014 | Transient captures at 100 ms show inference load is smooth; fine-tuning job starts produce large steps; captures distributed to POW and THM | CONFORMING (OPERATION) |
| MCF-CAP-017 | Capping configured at envelope for 38 of 40 sampled racks; 2 racks uncapped after a benchmark | PARTIAL (IMPLEMENTATION) |
| MCF-CAP-020 | During two maintenance windows on power path A, full load was retained against the state limit | NONCONFORMING (OPERATION) |
| MCF-CAP-023 | Air-to-liquid conversion treated as material; impact assessment complete | CONFORMING (OPERATION) |
| MCF-CAP-007, MCF-CAP-008 | Integrity and recovery outcomes defined with detection mechanisms, RTO, RPO and restoration order | CONFORMING (DESIGN) |

**Gate effects.**

- **CG-01**: CAP CRITICAL controls MCF-CAP-001, 005, 007, 008, 010 CONFORMING; **MCF-CAP-006 PARTIAL** → CG-01 = FAIL under the AIDCF-010 rule (PARTIAL never yields PASS). Remediation is a definitional fix: add a throttling metric with a facility-attribution method.
- **CG-14**: MCF-CAP-023 CONFORMING; other CRITICAL controls assessed in OPS.
- **CG-09 and CG-10** (SUPPORTING from MCF-CAP-020): the nonconformity requires gate-level evaluation. The resilience specialist concludes that the retained full load during maintenance means a second fault on path B would drop the hall, which is a demonstrated containment weakness; the CG-09 evaluation records the CAP result as a gate criterion not met for the MAINTENANCE state.
- **CG-05** (SUPPORTING from MCF-CAP-012 and MCF-CAP-017): gate-level evaluation records that shed order does not follow priority; the POW specialist judges whether it defeats continuity of the inference outcome.

**Decision effect.** With CG-01 at FAIL, the outcome definition the question depends on is not established, so REASONABLY_ASSURED and CONDITIONALLY_ASSURED are unavailable; AIDCF-012 controlled language for a controlling gate FAIL is NOT_ASSURED. The report presents the CG-01 FAIL and the MAINTENANCE-state containment weakness on its first page.

**What this example shows.** The hall's power and cooling can be well engineered and still not support an assured outcome when the outcome is not fully defined, priority is not implemented end to end, and state-specific limits are not respected.
