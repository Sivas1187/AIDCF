# AIDCF-007A Control Catalogue — DEP Dependency, Concentration and External Reliance Management

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-DEP](../../../aidcf-018-domain-guides/AIDCF-018-DEP_Dependency_and_Concentration_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-DEP-001](#mcf-dep-001) | Asset-to-Function Mapping | PREVENTIVE | IMPLEMENTATION | AL3 | CG-03 | CG-02 |
| [MCF-DEP-002](#mcf-dep-002) | Upstream Dependency Mapping | PREVENTIVE | IMPLEMENTATION | AL3 | CG-03 | CG-15 |
| [MCF-DEP-003](#mcf-dep-003) | Downstream Consequence Mapping | DIRECTIVE | DESIGN | AL2 | — | CG-03, CG-09 |
| [MCF-DEP-004](#mcf-dep-004) | Recovery Dependency Mapping | RECOVERY | IMPLEMENTATION | AL3 | — | CG-03, CG-10 |
| [MCF-DEP-005](#mcf-dep-005) | Shared Source Analysis | PREVENTIVE | IMPLEMENTATION | AL3 | CG-03 | CG-05, CG-06, CG-09 |
| [MCF-DEP-006](#mcf-dep-006) | Common Controller Analysis | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-03, CG-07, CG-09 |
| [MCF-DEP-007](#mcf-dep-007) | Shared Route Analysis | PREVENTIVE | IMPLEMENTATION | AL3 | CG-03 | CG-09 |
| [MCF-DEP-008](#mcf-dep-008) | Shared Human Dependency Analysis | PREVENTIVE | DESIGN | AL2 | — | CG-03, CG-13 |
| [MCF-DEP-009](#mcf-dep-009) | Utility Dependency | PREVENTIVE | IMPLEMENTATION | AL3 | CG-03 | CG-05 |
| [MCF-DEP-010](#mcf-dep-010) | Telecom Dependency | PREVENTIVE | IMPLEMENTATION | AL3 | CG-03 | CG-10 |
| [MCF-DEP-011](#mcf-dep-011) | OEM Dependency | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-03, CG-10 |
| [MCF-DEP-012](#mcf-dep-012) | Cloud and Service Dependency | PREVENTIVE | IMPLEMENTATION | AL3 | CG-03 | CG-15, CG-10 |
| [MCF-DEP-013](#mcf-dep-013) | Capacity Concentration | DIRECTIVE | DESIGN | AL2 | — | CG-03, CG-09 |
| [MCF-DEP-014](#mcf-dep-014) | Supplier Concentration | DIRECTIVE | DESIGN | AL2 | — | CG-03 |
| [MCF-DEP-015](#mcf-dep-015) | Knowledge Concentration | PREVENTIVE | DESIGN | AL2 | — | CG-13, CG-10 |
| [MCF-DEP-016](#mcf-dep-016) | Substitution Readiness | RECOVERY | EFFECTIVENESS | AL5 | — | CG-10, CG-03 |
| [MCF-DEP-017](#mcf-dep-017) | Assessment Boundary | DIRECTIVE | IMPLEMENTATION | AL3 | CG-02, CG-03 | — |
| [MCF-DEP-018](#mcf-dep-018) | Provider Boundary | DIRECTIVE | IMPLEMENTATION | AL3 | CG-13 | CG-03 |
| [MCF-DEP-019](#mcf-dep-019) | Tenant Boundary | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-09, CG-13 |
| [MCF-DEP-020](#mcf-dep-020) | Cross-Boundary Enforcement | DETECTIVE | OPERATION | AL4 | — | CG-09, CG-15 |
| [MCF-DEP-021](#mcf-dep-021) | Dependency Health Indicators | DETECTIVE | OPERATION | AL4 | — | CG-03 |
| [MCF-DEP-022](#mcf-dep-022) | Provider Performance | DETECTIVE | OPERATION | AL4 | — | CG-13 |
| [MCF-DEP-023](#mcf-dep-023) | Change Detection | DETECTIVE | OPERATION | AL4 | — | CG-14, CG-03 |
| [MCF-DEP-024](#mcf-dep-024) | Periodic Revalidation | DETECTIVE | OPERATION | AL4 | — | CG-03 |

## DEP-01 Dependency discovery

### MCF-DEP-001

**Asset-to-Function Mapping** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Every Required Function of the declared Capability Instance is traceable to the specific InfrastructureSystems and AssetInstances that implement it in each declared operating state, so that the consequence of losing, maintaining or changing any asset is known before it happens.

**Requirement.** The capability owner shall maintain a versioned asset-to-function map that links each Required Function to the InfrastructureSystems and AssetInstances (including redundant and standby units) that implement it, stated separately for each declared operating state. The facility operator shall reconcile the map against the as-built asset register and current configuration at least at the interval set in the capability profile and after every material change, and shall record every asset that cannot be mapped, or every function with no identified implementing asset, as an UNKNOWN Record.

**Assessment criteria**

1. Every Required Function in the assessment boundary has at least one IMPLEMENTED_BY relationship to an InfrastructureSystem, and every InfrastructureSystem resolves to identified AssetInstances.
2. Mappings are stated per operating state; at minimum NORMAL, MAINTENANCE (each planned maintenance configuration of a redundant path) and DEGRADED are distinguished where the implementing set differs.
3. A reconciliation sample of physical assets (by asset tag and location) and configuration items matches the map with no unexplained discrepancy above the profile tolerance.
4. Assets present in the as-built register but not mapped to any function are listed and dispositioned (mapped, excluded with rationale, or UNKNOWN).
5. The map is versioned, carries an effective date, and was re-validated after each material change recorded in the change log for the period.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Mapping completeness for critical Required Functions | % of functions with verified mapping | 100 | Illustrative; any unmapped critical function defeats dependency visibility, so the profile normally sets 100%. |
| Reconciliation sample size | assets per InfrastructureSystem | 10 or all if fewer | Illustrative; set by AIDCF-009 sampling rules and population size. |
| Reconciliation interval | months | 12 | Illustrative; shorten for estates with high deployment churn such as accelerator cluster expansion. |

**Minimum evidence**

- Current versioned asset-to-function map (export from CMDB/DCIM or dependency graph) with effective date and owner.
- As-built asset register extract for the boundary (asset tag, model, location, serial) at the same date.
- Single-line diagrams, P&IDs and network topology exports used to derive the map.
- Reconciliation record for the sample: asset-by-asset match/mismatch with resolution.
- List of unmapped assets and unmapped functions with disposition.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | Point-in-time reconciliation no older than the reconciliation interval; change log covering the 12 months preceding the assessment. |
| independence | Reconciliation sample shall be selected and checked by a person other than the map author; physical verification by walk-down or E2 export, not by the author's attestation. |
| mandatoryItems | Versioned asset-to-function map; Reconciliation record against as-built register |
| acceptableAlternatives | Where no CMDB/DCIM exists, a controlled spreadsheet register is acceptable if versioned, owned and reconciled by walk-down with photographic or inspection evidence. |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-03 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-02 require gate-level evaluation. |
| reassessmentTriggers | Addition, removal or relocation of assets implementing a Required Function; Change to redundancy configuration or maintenance arrangement; New Capability Instance or Service Outcome definition; Reconciliation interval elapsed |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INSPECTION, SAMPLING

**Assessment procedure**

1. Obtain the Required Function list for the Capability Instance and the current asset-to-function map with its version and effective date.
2. Check that every Required Function has implementing systems and assets per declared operating state; list gaps.
3. Select a reconciliation sample per InfrastructureSystem using AIDCF-009 sampling rules, weighted towards assets in recent changes.
4. Verify sampled assets by walk-down or authoritative E2 export (tag, location, serial, model) against the map and as-built register.
5. Extract assets in the register that are not mapped and confirm their disposition.
6. Confirm map re-validation after each material change in the period by cross-referencing the change log.
7. Record Findings for mismatches and UNKNOWN Records for unmappable functions or assets.

**Gate mappings.** CG-03 Critical dependency visibility (CRITICAL); CG-02 Boundary and architecture integrity (SUPPORTING)

**Applicability.** Applies to every assessment where a Capability Instance is declared. Not applicable only for a pure DESIGN-stage assessment where no asset yet exists; in that case MCF-DEP-003 and the design-stage dependency model carry the obligation.

**Lifecycle stages.** PLAN, DESIGN, BUILD, COMMISSION, OPERATE, CHANGE, DECOMMISSION · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION

**Failure modes addressed.** Required Function silently implemented by an unregistered asset; Maintenance on an asset not known to support a function (scenario X04); Map drift after cluster expansion or rack moves; Redundant unit recorded but not physically present or not connected

**Testing safety.** Walk-downs in electrical rooms, plant spaces and liquid-cooled halls shall be escorted and follow site access and PPE rules; no covers, panels or enclosures shall be opened for verification without a permit issued under MCF-OPS-007.

**UNKNOWN rule.** Record an UNKNOWN Record (U10 Dependency unknown, or U5 Coverage gap) for each Required Function with no verifiable implementing asset and for each sampled asset whose function cannot be established; any such UNKNOWN on a critical Required Function is US4.

**Ontology classes.** RequiredFunction, InfrastructureSystem, AssetInstance, Dependency, OperatingState, ArchitectureSnapshot · **Related controls.** MCF-DEP-002, MCF-DEP-003, MCF-DEP-017, MCF-OPS-017, MCF-CAP-004

**Informative references.** ISO/IEC/IEEE 42010 (architecture description); ISO 55001 (asset management systems); ISO/IEC 19770-1 (IT asset management); EN 50600-3-1 (data centre management and operational information)

### MCF-DEP-002

**Upstream Dependency Mapping** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Every material upstream dependency of each Required Function is traced to the point where it leaves the assessment boundary and, where knowable, to the first shared upstream node, so that external and shared reliance is visible rather than assumed.

**Requirement.** The capability owner shall maintain an upstream dependency graph for each Required Function that records, for every dependency, the provider, dependency type (electrical, thermal, hydraulic, network, control-system, timing/information, human/procedural, supplier/contractual, geographic, capacity), strength, applicable operating states and owner, following the AIDCF-003 dependency record schema. Tracing shall continue at least to the boundary exit point (for example the utility point of connection, carrier demarcation, facility-water flange, fuel delivery point, cloud or SaaS endpoint) and to the first known shared upstream node beyond it. The dependency owner shall record any trace that cannot be completed as an UNKNOWN Record.

**Assessment criteria**

1. Each Required Function has an upstream graph covering all dependency classes in AIDCF-003 that apply; classes judged not applicable are stated with rationale.
2. Each dependency record has provider, type, strength, applicable states, owner and evidence populated, or the missing attribute is recorded as UNKNOWN.
3. External dependencies are traced to the boundary exit point and to the first known shared upstream node (for example grid substation or transmission circuit, carrier point of presence, cloud region, identity provider tenant).
4. Timing/information dependencies (DNS, NTP/PTP, DHCP/PXE, IPAM, certificate authorities, licence servers, identity providers) are included for compute, network, storage and control-system functions.
5. A sample of dependency records is corroborated by an independent source (contract, provider route record, configuration export or test).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Minimum trace depth beyond boundary | upstream nodes | 1 (first shared upstream node) | Illustrative; deeper tracing is set in the profile where concentration risk is high. |
| Corroboration sample | % of external dependency records | 25 (minimum 5 records) | Illustrative; set per AIDCF-009 sampling rules. |

**Minimum evidence**

- Upstream dependency graph or register for each Required Function, with version and owner.
- Utility connection agreement or point-of-connection diagram; carrier circuit and route records; facility-water and fuel supply records.
- Configuration exports showing DNS, time, identity, licence and repository endpoints used by compute, network, storage and control systems.
- Corroboration record for sampled dependencies.
- UNKNOWN Records for traces that could not be completed.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY; RECOVERY |
| periodCoverage | Current at assessment date; graph reviewed within the revalidation interval of MCF-DEP-024. |
| independence | Corroboration from a source independent of the graph author (provider document, configuration export or technical test). |
| mandatoryItems | Upstream dependency graph per Required Function; Configuration evidence for timing/information dependencies |
| acceptableAlternatives | Provider attestations may substitute for route records only where the provider refuses disclosure; the dependency is then recorded with confidence no higher than CONF-2 and an UNKNOWN Record for the undisclosed attribute. |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-03 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-15 require gate-level evaluation. |
| reassessmentTriggers | New or changed provider, circuit, utility connection or cloud/SaaS service; Change to control-system or management-plane architecture; Provider notification of network or route change; Incident revealing an unrecorded dependency |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Select the Required Functions in scope and obtain their upstream graphs.
2. Check graph completeness against the AIDCF-003 dependency classes for each function; list omitted classes.
3. For external dependencies, confirm the boundary exit point and first shared upstream node from provider documents.
4. Extract configuration for timing, naming, identity, licensing and repository endpoints from a sample of compute, network, storage and BMS/EPMS systems and confirm each endpoint appears in the graph.
5. Corroborate the sampled records against independent evidence and record conflicts.
6. Record UNKNOWN Records for incomplete traces with US severity.

**Gate mappings.** CG-03 Critical dependency visibility (CRITICAL); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to every in-scope Required Function. Depth beyond the boundary may be limited by provider disclosure; that limitation is recorded, not treated as not applicable.

**Lifecycle stages.** PLAN, DESIGN, BUILD, COMMISSION, OPERATE, CHANGE, DECOMMISSION · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION

**Failure modes addressed.** Hidden dependency on a shared upstream node (substation, carrier POP, cloud region); Unrecorded reliance on an external identity provider or licence server; Time-source dependency not recorded (scenario X13); Dependency on a provider assumed to be diverse but sharing a parent

**Testing safety.** Configuration extraction shall use read-only accounts and approved export methods; no live query against BMS/EPMS or PLCs shall be made without authorisation from the control-system owner.

**UNKNOWN rule.** An incomplete upstream trace for a dependency of strength absolute or material is a U10 UNKNOWN Record of severity US4; an incomplete trace limited to supporting or recovery-only dependencies is US3 unless it affects a gate criterion.

**Ontology classes.** Dependency, RequiredFunction, Resource, Interface, UnknownRecord · **Related controls.** MCF-DEP-001, MCF-DEP-004, MCF-DEP-009, MCF-DEP-010, MCF-DEP-012

**Informative references.** AIDCF-003 dependency record schema; ISO 22317 (business impact analysis); IEC 61078 (reliability block diagrams); NIST SP 800-161r1 (cyber supply chain risk management)

### MCF-DEP-003

**Downstream Consequence Mapping** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** For each material asset, system and dependency, the Service Outcomes it affects and the time from its loss to outcome impact are known, so that prioritisation, maintenance planning and response are driven by consequence rather than by asset type.

**Requirement.** The capability owner shall maintain a downstream consequence analysis that states, for each material InfrastructureSystem and dependency, the Service Outcomes affected by its loss or degradation, the propagation path, and the time-to-impact under declared load (for example UPS autonomy, thermal ride-through of liquid-cooled racks, checkpoint interval loss for training, inference latency tolerance). A competent engineer independent of the author shall review the analysis before approval.

**Assessment criteria**

1. Each material system and dependency has recorded affected Service Outcomes and a propagation path using PROPAGATES_TO relationships.
2. Time-to-impact is stated with unit, load assumption and source (calculation, test or OEM data) for power, thermal and control dependencies.
3. Time-to-impact for AI workloads accounts for workload behaviour (for example training job failure on single-node loss within a synchronous collective, and the work lost since last checkpoint).
4. The analysis has been independently reviewed and approved, and its assumptions are listed.
5. The analysis is used: consequence classes appear in maintenance planning, alarm prioritisation and change risk assessment for a sample of records.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Thermal ride-through at declared rack load | seconds | Site-specific (no default) | Derived from THM analysis and test; liquid-cooled high-density racks can have very short ride-through, so it is never assumed. |
| Maximum training work lost per interruption | minutes of cluster time | Equal to checkpoint interval (illustrative 30) | Illustrative; set from the Service Outcome tolerance in CAP. |

**Minimum evidence**

- Approved consequence analysis (FMEA-style table or graph) with assumptions.
- Source calculations or test reports for time-to-impact values.
- Independent review record.
- Sample of maintenance plans, alarm priority records or change risk assessments showing use of consequence classes.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | Current approved version; reviewed within 12 months or after material change. |
| independence | Technical review by a competent engineer who did not author the analysis. |
| mandatoryItems | Approved consequence analysis with time-to-impact values and sources |
| acceptableAlternatives | A fault tree or reliability block model may substitute for a tabular FMEA if it states outcomes, paths and time-to-impact. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03, CG-09 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Change in rack power density or cooling method; Change in workload type (training vs inference) or checkpoint policy; New Service Outcome or tolerance; Incident with unexpected propagation |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, SAMPLING

**Assessment procedure**

1. Obtain the consequence analysis, its assumptions and review record.
2. Check coverage against the material systems in the asset-to-function map (MCF-DEP-001).
3. Recompute or check a sample of time-to-impact values against their sources (UPS discharge data, thermal test, checkpoint configuration).
4. Trace a sample of maintenance, alarm and change records to confirm consequence classes are used.
5. Record Findings for unsupported time-to-impact values or uncovered systems.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to all in-scope Capability Instances. Where the Capability Instance has a single Service Outcome, the analysis may be simplified to propagation paths and time-to-impact.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Consequence of a loss underestimated because ride-through was assumed rather than measured; Low-priority alarm on an asset with seconds-scale time-to-impact; Maintenance scheduled during a training run without checkpoint coordination

**Testing safety.** Desk-based analysis; where time-to-impact values require a test, the test is governed by the owning domain's control (POW/THM/RES) and not performed under this control.

**UNKNOWN rule.** Missing time-to-impact for a power, thermal or control dependency of a critical Required Function is a US3 UNKNOWN Record; it escalates to US4 if a CG-05, CG-06 or CG-10 criterion relies on that value.

**Ontology classes.** ServiceOutcome, FailureScenario, Dependency, InfrastructureSystem, FaultDomain · **Related controls.** MCF-DEP-001, MCF-DEP-013, MCF-OPS-013, MCF-OPS-018, MCF-CAP-010

**Informative references.** IEC 60812 (FMEA); IEC 61025 (fault tree analysis); ISO 22317 (business impact analysis); ASHRAE TC 9.9 thermal guidelines for data processing environments

### MCF-DEP-004

**Recovery Dependency Mapping** · RECOVERY · claim type IMPLEMENTATION · required AL3

**Objective.** Dependencies that are needed only, or mainly, during restoration are identified and available, and circular recovery dependencies are found and broken before an event rather than during it.

**Requirement.** The recovery owner shall maintain a recovery dependency map for each Required Function covering recovery-only and recovery-critical dependencies (for example generator start batteries and fuel delivery, black-start sequence, BMS/EPMS server and network availability, out-of-band management network, DHCP/PXE and golden images, licence and entitlement servers, identity provider and break-glass credentials, OEM remote support, spares and specialist labour). The recovery owner shall analyse the map for circular dependencies and for recovery dependencies that share a fault domain with the failure they recover from, and shall record each such case with a resolution or an UNKNOWN Record.

**Assessment criteria**

1. A recovery dependency map exists for each Required Function and states, for each dependency, whether it is recovery-only, and the operating states (RECOVERY, EMERGENCY, SHUTDOWN) in which it is needed.
2. A circular-dependency analysis has been performed (for example cooling controls require network, network requires power, power restoration sequence requires cooling controls) and each cycle is broken by a documented manual or independent path.
3. Each recovery dependency is checked for shared fault domain with the failure scenarios it is intended to recover from (for example golden-image repository hosted in the hall it restores).
4. Recovery-only external dependencies (OEM remote support, licence servers, cloud identity) have a verified offline or alternative path, or are recorded as UNKNOWN.
5. The map is consistent with the recovery sequences in RES-04 and the restoration procedures in POW/THM/CMP/STO/NET.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum acceptable unresolved circular dependencies on critical functions | count | 0 | Illustrative; any unresolved cycle on a critical function defeats recovery planning. |

**Minimum evidence**

- Recovery dependency map per Required Function.
- Circular-dependency analysis record with resolutions.
- Configuration evidence of offline or alternative paths (for example local licence caches, cached credentials, local image mirrors, out-of-band network design).
- Cross-reference to RES-04 recovery sequences.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | RECOVERY; EMERGENCY; SHUTDOWN |
| periodCoverage | Current at assessment date; updated after each recovery test or real recovery event. |
| independence | Analysis reviewed by a person from a different discipline (for example a facilities engineer reviewing an IT recovery map and vice versa). |
| mandatoryItems | Recovery dependency map; Circular-dependency analysis |
| acceptableAlternatives | A documented recovery exercise (RES-05) that exercised the full restoration path may substitute for part of the circular analysis for the paths it covered. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03, CG-10 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Change to recovery sequence, golden-image location or licence model; Introduction of a cloud or SaaS dependency in a management path; Recovery test or real event revealing an unrecorded dependency |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Obtain the recovery dependency maps and the RES-04 recovery sequences for in-scope functions.
2. Construct or review the dependency graph for the RECOVERY state and search for cycles.
3. For each recovery dependency, test for shared fault domain with the initiating scenario using the AIDCF-003 fault-domain taxonomy.
4. Verify by configuration evidence that declared offline or alternative paths exist.
5. Interview recovery owners on any dependency not represented in procedures.
6. Record Findings and UNKNOWN Records.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to every Capability Instance with a declared Recovery Outcome. Where no Recovery Outcome is declared, this is recorded as a CG-01 matter rather than treated as not applicable.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** RECOVERY, EMERGENCY, SHUTDOWN, FAILED

**Failure modes addressed.** Circular recovery dependency (cooling controls need network that needs cooled equipment); Golden image or configuration backup stored in the failed fault domain; Licence or entitlement server unreachable during recovery; Break-glass credentials depend on the failed identity provider; Recovery reintroduces corrupt configuration (scenario X15)

**Testing safety.** Analysis is desk-based. Verification of offline paths shall not include disconnecting live services; any such test is performed under RES-05 with change approval.

**UNKNOWN rule.** A recovery dependency whose availability in the RECOVERY state cannot be established is a U10 UNKNOWN Record; it is US4 where it lies on the restoration path of a critical Required Function and a CG-10 criterion depends on it, otherwise US3.

**Ontology classes.** Dependency, FaultDomain, RequiredFunction, OperatingState, FailureScenario · **Related controls.** MCF-RES-013, MCF-RES-014, MCF-POW-024, MCF-CMP-023, MCF-DEP-012

**Informative references.** ISO 22301 (business continuity management systems); ISO/IEC 27031 (ICT readiness for business continuity); NIST SP 800-34 (contingency planning)

## DEP-02 Shared and common-mode dependencies

### MCF-DEP-005

**Shared Source Analysis** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Nominally redundant or diverse supplies are shown, on as-built evidence, not to share a source whose loss would defeat both, or the shared source is declared, owned and reflected in the resilience claim.

**Requirement.** The facility owner shall analyse every redundant or diverse supply path that a resilience claim relies on (utility feeds, transformers, UPS paths, generator fuel, facility water, chilled-water plant, heat rejection, carrier circuits, cloud regions) for shared sources and record each pair as INDEPENDENT_OF only where as-built evidence supports independence for the stated hazard. Where a shared source exists, the facility owner shall record a SHARES_DEPENDENCY_WITH relationship, an owner and the residual exposure, and the capability owner shall reflect it in the resilience claim.

**Assessment criteria**

1. Every redundancy claim used in CG-05, CG-06 or CG-08 evaluation has a corresponding shared-source analysis.
2. Independence claims are supported by as-built evidence (for example utility statement of separate grid supply points, separate fuel contracts and storage, separate water mains), not by design intent alone.
3. Shared sources found (for example both utility feeds from one grid substation, both fuel contracts with one distributor, both carriers using one upstream fibre) are recorded with owner and residual exposure.
4. The resilience claim for each affected Required Function is consistent with the recorded shared sources.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Upstream depth examined for shared source | levels | To grid supply point / carrier POP / fuel terminal | Illustrative; profile sets depth based on the declared external hazard set. |

**Minimum evidence**

- Shared-source analysis per redundancy claim.
- Utility connection documentation identifying supply points; carrier route and POP documentation; fuel and water supply contracts.
- Single-line and P&ID diagrams for internal sources.
- Resilience claim records showing reflected shared sources.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Current; re-performed after any change to supply arrangements. |
| independence | Independence claims corroborated by a provider document or as-built record, not the designer's statement. |
| mandatoryItems | Shared-source analysis; Provider evidence for each claimed external independence |
| acceptableAlternatives | Where a utility will not disclose supply topology, a utility-signed statement of the number of independent supply points is acceptable at confidence no higher than CONF-2. |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-03 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-05, CG-06, CG-09 require gate-level evaluation. |
| reassessmentTriggers | Utility network reconfiguration notice; Change of fuel or water supplier; New carrier circuit or carrier merger; Change to internal redundancy configuration |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION, INSPECTION

**Assessment procedure**

1. List every redundancy or diversity claim relied on for the Capability Instance.
2. For each, obtain the shared-source analysis and the supporting provider and as-built evidence.
3. Trace each path upstream and identify the first common node, if any.
4. Compare findings with the resilience claim and record inconsistencies.
5. Inspect accessible internal points (for example generator fuel interconnection, chilled-water headers) where documents conflict.

**Gate mappings.** CG-03 Critical dependency visibility (CRITICAL); CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies wherever a resilience or availability claim relies on redundancy or diversity. Not applicable to a Capability Instance that declares no redundancy (in which case the single source is the dependency and DEP-02 still records it).

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED, EMERGENCY

**Failure modes addressed.** Two utility feeds from the same grid substation lost together; A and B fuel supply from one distributor or terminal; Diverse carriers sharing one long-haul fibre; Redundant cooling plant sharing one water main or make-up water source

**Testing safety.** Inspection of plant interconnections shall be non-intrusive; valves, breakers and isolators shall not be operated for verification.

**UNKNOWN rule.** Where independence of a pair cannot be established, the pair shall be treated as sharing a source for gate evaluation and an UNKNOWN Record (U10) raised; severity US4 when the pair underpins a CG-05 or CG-06 resilience criterion.

**Ontology classes.** Dependency, FaultDomain, Resource, InfrastructureSystem, CapacityAssertion · **Related controls.** MCF-DEP-006, MCF-DEP-007, MCF-DEP-009, MCF-POW-003, MCF-THM-016

**Informative references.** AIDCF-003 common-mode and concentration relationships; IEC 61508-6 (guidance on common cause failure); NUREG/CR-5485 (common-cause failure modelling guidelines)

### MCF-DEP-006

**Common Controller Analysis** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Redundant systems are not defeated together by a shared controller, management server, automation logic, firmware baseline or orchestration plane.

**Requirement.** The control-system owner shall identify, for each redundant infrastructure pair or group, every shared control element (PLCs, BMS/EPMS servers, CDU controllers and their master/lead-lag logic, sequence-of-operation software, cluster managers and schedulers, fabric controllers, storage controllers, firmware and configuration sources, automation and AI agents) and record whether loss, malfunction or unsafe command of that element can affect more than one member of the group. The control-system owner shall either demonstrate independence, implement a safeguard (local autonomous control, fail-safe default, staggered firmware) or record the common controller as a declared common mode with owner.

**Assessment criteria**

1. Each redundant group in POW, THM, CMP, STO and NET has a recorded common-controller analysis.
2. Controller failure behaviour (fail-last, fail-safe, fail-to-local) is stated from configuration or OEM evidence for each shared element.
3. Shared firmware or configuration sources are identified, and rollout to redundant members is staged (cross-reference MCF-SUP-015).
4. Each common controller that can affect more than one member has a safeguard or a recorded acceptance by the accountable owner.
5. Automation or AI agents with authority over more than one redundant member are recorded with their authority scope (cross-reference SEC-06).

**Minimum evidence**

- Control architecture drawings (BMS/EPMS network and controller layout, CDU control topology, cluster/fabric management architecture).
- Controller configuration exports showing failure mode settings.
- Common-controller analysis record and acceptance decisions.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED; FAILED |
| periodCoverage | Current; re-performed after control-system change. |
| independence | Review by an engineer not responsible for the control-system design. |
| mandatoryItems | Common-controller analysis; Configuration evidence of controller failure behaviour |
| acceptableAlternatives | OEM documentation of default failure behaviour is acceptable where configuration export is not possible, with an UNKNOWN Record for the as-configured state. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03, CG-07, CG-09 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | BMS/EPMS/CDU controller replacement or reprogramming; Change to sequence of operation; Introduction of new automation or agent authority; Firmware baseline change across a redundant group |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Identify redundant groups from the asset-to-function map.
2. For each group, obtain control architecture and identify shared elements.
3. Obtain configuration or OEM evidence of failure behaviour for each shared element.
4. Check the safeguard or acceptance record for each shared element affecting multiple members.
5. Record Findings and UNKNOWN Records.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING); CG-07 Critical control-system integrity (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to every redundant group of InfrastructureSystems controlled or managed by software or programmable controllers.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED, FAILED

**Failure modes addressed.** Single BMS server failure stops both chilled-water plants; CDU lead-lag controller fault stops all CDUs on a loop; Firmware rollout common-mode failure (scenario X08); Fabric controller fault isolates both rails; Automation acts on all redundant members at once

**Testing safety.** No controller shall be failed, isolated or forced to verify behaviour under this control; failure-behaviour tests are performed only under THM/POW/SEC test controls with authorisation from the control-system owner and the facility operator.

**UNKNOWN rule.** If controller failure behaviour cannot be established, record a U8 or U1 UNKNOWN Record; US4 where the redundant group supports a CG-05, CG-06 or CG-07 criterion.

**Ontology classes.** InfrastructureSystem, FaultDomain, Dependency, FailureMode · **Related controls.** MCF-DEP-005, MCF-SUP-015, MCF-THM-021, MCF-POW-021, MCF-SEC-021

**Informative references.** IEC 62443-3-2 (security risk assessment for system design); IEC 61508-6 (guidance on common cause failure); ASHRAE Guideline 36 (sequences of operation for HVAC control)

### MCF-DEP-007

**Shared Route Analysis** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Physically diverse paths for power, fluid and telecommunications are verified on site and on provider route records not to converge in a shared trench, duct, riser, bridge, building entry, cable tray, pipe rack or fire zone.

**Requirement.** The facility owner shall maintain route records for every path relied on for diversity (MV/LV cables, busways, fuel lines, chilled and facility water pipes, fibre between buildings and to carrier POPs, inter-hall fabric trunks) and shall identify every point where diverse routes converge or come within the separation distance set in the capability profile. The facility owner shall obtain route evidence from carriers and utilities for external routes, verify internal routes by inspection at least at the profile interval, and record each convergence point as a shared fault domain with owner.

**Assessment criteria**

1. Route records exist for each diverse path and identify building entries, risers, trenches, bridges and fire zones traversed.
2. Convergence points and sub-separation sections are listed with location and the hazards that could affect both routes (fire, flood, excavation, vehicle impact).
3. External carrier routes are supported by carrier route documentation (KMZ, route maps or signed statements of diversity) to at least the first POP or regeneration site.
4. A sample of internal routes has been physically inspected within the interval and matches records.
5. Each convergence point has an owner and is reflected in the fault-domain model (RES-02) and resilience claims.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Minimum physical separation for diverse routes | m | Site-specific (no default) | Set in capability profile with reference to fire-zone design and the separation guidance in the cabling standard adopted (for example ANSI/TIA-942 or EN 50600-2-4). |
| Route inspection interval | months | 24 | Illustrative; shorter where third-party works or construction occur nearby. |

**Minimum evidence**

- Route drawings for internal diverse paths with fire-zone overlay.
- Carrier route documentation for each external circuit relied on for diversity.
- Inspection record (dated, with photographs) for the sample.
- Convergence point register with owners.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Route evidence no older than the inspection interval; carrier documentation current within 12 months. |
| independence | Inspection by a person other than the route record author; carrier statements are provider evidence (E5 where independently produced). |
| mandatoryItems | Route records with convergence register; Carrier route documentation for diversity-relied circuits |
| acceptableAlternatives | Where a carrier will not disclose routes, a contractual diversity commitment plus independent fibre-path verification (for example latency fingerprinting by a third party) may be used, at confidence no higher than CONF-2. |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-03 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-09 require gate-level evaluation. |
| reassessmentTriggers | Carrier reroute or maintenance notification; Construction or excavation affecting routes; New cable or pipe installation in shared spaces; Fire-zone change |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, RECONCILIATION, SAMPLING

**Assessment procedure**

1. Obtain diverse path list and route records.
2. Overlay routes on site plans and fire zones; identify convergence points.
3. Obtain carrier and utility route evidence and check diversity to the first POP or supply point.
4. Inspect a sample of internal routes, prioritising building entries and risers.
5. Confirm convergence points are in the RES-02 fault-domain model.
6. Record Findings and UNKNOWN Records.

**Gate mappings.** CG-03 Critical dependency visibility (CRITICAL); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to all paths relied on for physical diversity. For colocation tenants, internal routes owned by the colocation provider are assessed through MCF-DEP-018 provider boundary evidence.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED, EMERGENCY

**Failure modes addressed.** Fire disables paired infrastructure routes (scenario X09); Diverse carrier circuits in one duct cut by excavation; A and B busways in one riser; Supply and return water mains crossing in one trench

**Testing safety.** Route inspection in risers, trenches and plant rooms shall follow confined-space and electrical safety rules; trench or manhole entry requires a permit under MCF-OPS-007 and confined-space controls.

**UNKNOWN rule.** Unverified diversity on a path relied on by a resilience claim shall be treated as shared for gate evaluation and recorded as U10 UNKNOWN; US4 where the path supports a CG-05, CG-06 or CG-08 criterion.

**Ontology classes.** Interface, FaultDomain, Dependency, AssetInstance · **Related controls.** MCF-DEP-005, MCF-DEP-010, MCF-NET-002, MCF-NET-020, MCF-RES-005

**Informative references.** ANSI/TIA-942 (telecommunications infrastructure standard for data centres); EN 50600-2-4 (telecommunications cabling infrastructure); EN 50600-2-2 (power distribution)

### MCF-DEP-008

**Shared Human Dependency Analysis** · PREVENTIVE · claim type DESIGN · required AL2

**Objective.** Redundant technical systems are not made dependent on the same individual, team, shift, contractor or authorisation holder in a way that defeats redundancy during response, maintenance or recovery.

**Requirement.** The operations manager shall analyse human and organisational dependencies for each Required Function, including authorised persons for HV/LV switching, refrigerant and liquid-cooling work, on-call specialists, OEM field engineers and maintenance contractors, and shall record where the same person, team or contractor is required to restore or operate more than one redundant member, or where response depends on fewer people than the emergency task analysis requires. The operations manager shall implement deputies, cross-authorisation or contractual capacity for each case or record it as a declared concentration with owner.

**Assessment criteria**

1. Human/procedural dependencies are recorded for each Required Function using the AIDCF-003 dependency classes.
2. For each emergency procedure, the number of competent and authorised people required is compared with those available on shift and on call within the response time.
3. Cases where one contractor maintains both redundant members (for example A and B UPS systems or all generators) are identified and assessed.
4. Each identified shared human dependency has a mitigation or accepted concentration with owner.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Minimum authorised persons per critical switching task available within response time | persons | 2 | Illustrative; reflects a two-person rule for HV switching common in safe systems of work; set from the site safety rules. |

**Minimum evidence**

- Human dependency analysis per Required Function.
- Authorisation register for hazardous tasks (cross-reference MCF-OPS-004).
- Roster and on-call schedules for a representative period.
- Maintenance contracts showing scope per system.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY; RECOVERY |
| periodCoverage | Roster sample covering at least 3 months including holiday periods. |
| independence | Reviewed by a person outside the operations line management (for example HSE or assurance). |
| mandatoryItems | Human dependency analysis; Authorisation register |
| acceptableAlternatives | A tabletop exercise (RES-05) testing staffing for concurrent events may substitute for part of the roster analysis. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03, CG-13 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Change of maintenance contractor; Departure of a key authorised person; Change to shift pattern; New system requiring specialist authorisation |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INQUIRY, SAMPLING

**Assessment procedure**

1. Obtain emergency task analysis and the human dependency analysis.
2. Sample rosters and on-call schedules and compare with required authorised persons per task.
3. Review maintenance contracts for single-contractor coverage of redundant members.
4. Interview shift leads on response capacity for concurrent events.
5. Record Findings and accepted concentrations.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING); CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to all staffed and contractor-supported operations in the boundary.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY, RECOVERY

**Failure modes addressed.** Only one authorised HV switching person available at night; Same contractor fault affects maintenance of both UPS systems; Concurrent events exceed on-shift capacity; Key-person absence prevents recovery

**Testing safety.** Analysis only; no staffing reduction or simulated absence shall be imposed on live operations to test this control.

**UNKNOWN rule.** If rosters or authorisation records are unavailable for the sample period, record U1 UNKNOWN of severity US3; escalate to US4 if CG-04 safe-work criteria rely on two-person availability.

**Ontology classes.** Dependency, RequiredFunction, FaultDomain, Resource · **Related controls.** MCF-DEP-015, MCF-OPS-001, MCF-OPS-004, MCF-GOV-023

**Informative references.** HSE HSG48 (reducing error and influencing behaviour); HSE HSG256 (managing shift work); Uptime Institute Tier Standard: Operational Sustainability

## DEP-03 External providers and utilities

### MCF-DEP-009

**Utility Dependency** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** The utility services the Capability Instance relies on (grid electricity, water, fuel, and where applicable gas or district cooling) are contracted, sized and characterised for the declared demand, ramp schedule and operating states, including any curtailment, flexibility or interruptibility terms.

**Requirement.** The facility owner shall maintain, for each utility dependency, the contractual and technical basis of supply: for grid electricity the connection agreement, firm and non-firm capacity, capacity reservation and energisation schedule, curtailment or flexible-connection terms, demand-response obligations, supply-point power quality characteristics and protection interface; for water the supply and discharge permits, contracted volume and restriction triggers; for fuel the supply contracts, priority status and delivery commitments. The facility owner shall reconcile contracted firm capacity against declared demand (including growth commitments from CAP-04) for each operating state and record any shortfall, non-firm reliance or undisclosed term as a Finding or UNKNOWN Record.

**Assessment criteria**

1. A current utility connection agreement exists for each grid supply, with firm and any non-firm capacity, energisation dates and curtailment terms identified.
2. Contracted firm capacity is equal to or greater than the declared demand in each operating state, or the gap is covered by an evidenced on-site measure and declared in the capability profile.
3. Capacity reservations and staged energisation milestones match the capability growth forecast; slippage is tracked.
4. Curtailment, flexible-connection and demand-response obligations are mapped to Service Outcome effects and to operating procedures.
5. Water and fuel supply contracts state volume, priority and delivery lead time, and are consistent with POW fuel autonomy and THM/ENV water continuity analyses.
6. Supply-point power quality data (for example voltage dips and interruptions) is available for the preceding period or recorded as UNKNOWN.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Firm capacity margin over declared peak demand | % of declared peak | 10 | Illustrative; set in the capability profile from load growth uncertainty and utility terms. |
| Minimum fuel resupply commitment under emergency | hours from call-off to delivery | Site-specific (no default) | Set from POW fuel autonomy (MCF-POW-007/008) so that autonomy exceeds the committed resupply time with margin. |
| Power quality history reviewed | months | 12 | Illustrative; longer history improves estimate of event frequency. |

**Minimum evidence**

- Grid connection agreement and any variation, capacity reservation and energisation schedule.
- Utility-provided supply characteristics (fault level, protection settings at interface, declared power quality).
- Demand reconciliation by operating state.
- Water supply and discharge permits; fuel supply contracts with emergency priority terms.
- Power quality monitoring records at the point of connection (EPMS or utility).

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY; TRANSITION |
| periodCoverage | Agreements current at assessment date; power quality records covering at least the preceding 12 months. |
| independence | Contractual evidence from the utility (E5 provider evidence) corroborated by on-site metering (E3). |
| mandatoryItems | Grid connection agreement with firm capacity; Demand reconciliation by operating state |
| acceptableAlternatives | Where a connection agreement is under negotiation, a utility offer letter with stated capacity and conditions supports DESIGN-stage assessment only, and the IMPLEMENTATION claim remains UNKNOWN. |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-03 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-05 require gate-level evaluation. |
| reassessmentTriggers | Change to connection agreement, capacity or curtailment terms; Revised energisation date; Demand forecast change; Utility network reinforcement or reconfiguration notice; New water restriction or fuel contract change |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS, INQUIRY

**Assessment procedure**

1. Obtain connection agreements, permits and fuel/water contracts.
2. Extract firm/non-firm capacity, curtailment and demand-response terms.
3. Reconcile contracted capacity with declared demand for each operating state and the growth forecast.
4. Check consistency with POW fuel autonomy and THM/ENV water analyses.
5. Review power quality records at the point of connection for the period.
6. Record Findings and UNKNOWN Records.

**Gate mappings.** CG-03 Critical dependency visibility (CRITICAL); CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies to every site supplying the Capability Instance. In colocation, the colocation provider's utility evidence is obtained through MCF-DEP-018; a tenant that cannot obtain it records UNKNOWN.

**Lifecycle stages.** PLAN, DESIGN, BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED, EMERGENCY, TRANSITION

**Failure modes addressed.** Capability expansion energised against non-firm capacity without declaration; Curtailment event not reflected in operating procedures; Energisation delay strands installed compute (scenario X17); Fuel resupply slower than autonomy under regional emergency; Water restriction reduces heat rejection (scenario X10)

**Testing safety.** Document and data review only; no switching, metering intervention or protection testing at the utility interface shall be performed under this control.

**UNKNOWN rule.** Undisclosed firm capacity or curtailment terms for a grid supply relied on by the Capability Instance is a U2 or U10 UNKNOWN Record of severity US4 (affects CG-03 and a CG-05 criterion).

**Ontology classes.** Dependency, Resource, CapacityAssertion, Interface, OperatingState · **Related controls.** MCF-POW-001, MCF-POW-002, MCF-POW-008, MCF-THM-015, MCF-CAP-015

**Informative references.** EN 50160 (voltage characteristics of public distribution networks); IEC 61000-4-30 (power quality measurement methods); IEEE 1159 (monitoring electric power quality); NFPA 110 (emergency and standby power systems); Applicable network operator connection agreement and grid code (jurisdiction-specific)

### MCF-DEP-010

**Telecom Dependency** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** External connectivity (internet transit, data-centre interconnect, wavelength or dark-fibre services, carrier-neutral cross-connects, out-of-band and management circuits) is provided by identified carriers over verified diverse routes with known service levels, so that connectivity Service Outcomes and remote management do not rest on unrecorded single carriers or paths.

**Requirement.** The network owner shall maintain a register of every external telecommunications circuit in scope, recording carrier, service type, A/Z ends, building entry, meet-me room and cross-connect identifiers, route diversity evidence, upstream carrier (where a reseller is used), service levels and fault escalation. The network owner shall verify that the circuits relied on for each connectivity outcome and for out-of-band management satisfy the declared diversity (carrier, route, entry, POP) and shall record shared elements and reseller dependencies as Findings or UNKNOWN Records.

**Assessment criteria**

1. Every external circuit relied on by a Service Outcome or management path is in the register with carrier, route and demarcation identifiers.
2. Declared carrier diversity accounts for resale and wholesale relationships (the underlying network operator is identified).
3. Building entries and meet-me rooms for diverse circuits are distinct, or the shared element is recorded (cross-reference MCF-DEP-007).
4. Out-of-band management connectivity does not depend on the same carrier and path as the production connectivity it is meant to back up.
5. Carrier service levels (availability, time to repair) are recorded and compared with the connectivity Service Outcome tolerance.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Minimum number of independent carriers for production connectivity | carriers | 2 | Illustrative; set by the connectivity Service Outcome. |
| Carrier time-to-repair commitment | hours | 4 | Illustrative; compare against outcome tolerance. |

**Minimum evidence**

- External circuit register.
- Carrier order forms and service descriptions; reseller disclosure of underlying carrier.
- Route diversity documentation (see MCF-DEP-007).
- Meet-me room and cross-connect records.
- Out-of-band management design.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY; RECOVERY |
| periodCoverage | Register current; carrier documents current within 12 months. |
| independence | Register entries corroborated by carrier documents and, for a sample, by configuration evidence (router interface descriptions, BGP sessions). |
| mandatoryItems | External circuit register; Underlying carrier identification for each diversity-relied circuit |
| acceptableAlternatives | Independent path verification by a third party may substitute for undisclosed carrier routes, at confidence no higher than CONF-2. |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-03 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-10 require gate-level evaluation. |
| reassessmentTriggers | New or cancelled circuit; Carrier merger, acquisition or wholesale change; Carrier reroute notice; Change to out-of-band design |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS, INSPECTION

**Assessment procedure**

1. Obtain the circuit register and connectivity Service Outcomes.
2. Reconcile register to router/switch configuration (interfaces, BGP neighbours) for a sample.
3. Identify underlying carriers and check claimed diversity.
4. Inspect meet-me room cross-connect records for diverse circuits.
5. Compare carrier service levels with outcome tolerance.
6. Record Findings and UNKNOWN Records.

**Gate mappings.** CG-03 Critical dependency visibility (CRITICAL); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies wherever a Service Outcome or management/recovery path depends on external connectivity. Fully air-gapped environments record the air-gap boundary instead.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED, EMERGENCY, RECOVERY

**Failure modes addressed.** Two 'diverse' carriers reselling one underlying fibre; Out-of-band circuit on same carrier as production; Single meet-me room for all external circuits; Carrier repair time exceeds outcome tolerance

**Testing safety.** No circuit shall be disconnected, shut or failed over to verify diversity under this control; failover testing is governed by NET and RES controls with change approval.

**UNKNOWN rule.** Undisclosed underlying carrier or route for a diversity-relied circuit is a U10 UNKNOWN Record; US4 where it underpins a connectivity Service Outcome assessed under CG-03 or CG-08.

**Ontology classes.** Dependency, Interface, Resource, FaultDomain · **Related controls.** MCF-DEP-007, MCF-NET-002, MCF-NET-015, MCF-NET-019, MCF-DEP-021

**Informative references.** ANSI/TIA-942 (telecommunications infrastructure standard for data centres); EN 50600-2-4 (telecommunications cabling infrastructure)

### MCF-DEP-011

**OEM Dependency** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Reliance on original equipment manufacturers and system integrators for the operation, support, repair and recovery of critical assets (accelerators and rack-scale systems, NICs/DPUs, switches and optics, storage, UPS, switchgear, generators, chillers, CDUs, BMS/EPMS) is identified per Required Function, including reliance that persists after installation such as entitlement, licensing, telemetry and remote diagnostics.

**Requirement.** The capability owner shall maintain an OEM dependency register that records, for each critical asset class, the OEM and integrator, support entitlement and its expiry, RMA and advance-replacement terms, licence or entitlement mechanisms required for operation (including licence servers and online activation), telemetry or phone-home requirements, field-engineer coverage for the site, proprietary tools or software needed for diagnosis or recovery, and the functions that would be lost or degraded if OEM support were unavailable. The capability owner shall record each operating dependency on OEM-hosted services as an external dependency in the upstream graph (MCF-DEP-002).

**Assessment criteria**

1. Every critical asset class in the asset-to-function map has an OEM dependency entry with current support entitlement and expiry.
2. Operating dependencies on OEM services (licence activation, entitlement checks, cloud management portals, remote diagnostics) are recorded with the effect of their loss on each Required Function.
3. Proprietary diagnostic or recovery tools are held on site or in an accessible repository with licences valid for emergency use.
4. Field-engineer coverage (response time, local presence, clearance requirements) is recorded and compared with recovery tolerances.
5. Entries are reconciled to contracts and to OEM portals for a sample of assets.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Support entitlement expiry warning | days before expiry | 180 | Illustrative; allows renewal or replacement before entitlement lapses. |

**Minimum evidence**

- OEM dependency register.
- Support contracts and entitlement records for sampled assets.
- Licence and activation design for software-licensed functions.
- Evidence of local copies of proprietary tools.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; RECOVERY |
| periodCoverage | Register current at assessment; entitlements checked against OEM records within 90 days. |
| independence | Entitlement status verified from the OEM record or portal, not from internal register alone. |
| mandatoryItems | OEM dependency register; Entitlement verification for sampled critical assets |
| acceptableAlternatives | An integrator-managed support arrangement is acceptable if the integrator's back-to-back OEM entitlement is evidenced. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03, CG-10 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | New asset class or OEM; Entitlement expiry or non-renewal; OEM change to licensing or telemetry model; OEM end-of-support notice |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INQUIRY, SAMPLING

**Assessment procedure**

1. Obtain the OEM dependency register and asset-to-function map.
2. Check coverage of critical asset classes.
3. Sample assets and verify entitlement against OEM records.
4. Review licence and telemetry dependencies for effect on operation if OEM services are unreachable.
5. Confirm local availability of proprietary tools.
6. Record Findings and UNKNOWN Records.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to all critical asset classes. Supplier due diligence and contract terms are assessed under SUP; this control records the dependency itself.

**Lifecycle stages.** PLAN, DESIGN, BUILD, OPERATE, CHANGE, DECOMMISSION · **Operating states.** NORMAL, MAINTENANCE, DEGRADED, RECOVERY

**Failure modes addressed.** Accelerator or switch feature stops after licence server unreachable; Loss of remote OEM support (scenario X18); Support entitlement lapsed unnoticed; Proprietary recovery tool unavailable during incident

**Testing safety.** Register and document review only; no licence server shall be blocked to test behaviour outside an approved RES-05 exercise.

**UNKNOWN rule.** An unknown entitlement status or an unrecorded OEM operating dependency for a critical asset class is a U10 UNKNOWN Record of severity US3, escalating to US4 if the dependency lies on a CG-10 restoration path.

**Ontology classes.** Dependency, AssetInstance, Resource, InfrastructureSystem · **Related controls.** MCF-SUP-001, MCF-SUP-005, MCF-SUP-021, MCF-CMP-022, MCF-DEP-014

**Informative references.** ISO/IEC 27036-2 (supplier relationships: requirements); ISO 22318 (guidelines for supply chain continuity)

### MCF-DEP-012

**Cloud and Service Dependency** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Dependencies on hyperscale cloud and SaaS control planes (identity providers, cloud-hosted DCIM/BMS analytics, cluster management and scheduling services, container and model registries, certificate authorities, DNS, ticketing and paging, OEM portals) are identified, their failure behaviour is known, and the infrastructure can continue to operate safely when they are unavailable.

**Requirement.** The capability owner shall maintain a register of every cloud or SaaS service on which an in-scope Required Function, management path or recovery path depends, recording the provider, region/zone, control-plane and data-plane dependencies, authentication path, the effect on each function if the service is unavailable or degraded, and the local fallback mode. The control-system owner shall ensure that no facility safety or continuity function (power, cooling, fire, leak detection and their alarming) requires a cloud or SaaS service to operate, and shall record any exception with accountable acceptance.

**Assessment criteria**

1. Every cloud/SaaS service used by in-scope functions is registered with provider, region and authentication path.
2. Failure behaviour on service unavailability is stated per function and is supported by provider documentation, configuration or test.
3. No facility safety or continuity control loop or critical alarm path depends on a cloud or SaaS service; exceptions are accepted by the accountable owner.
4. Identity dependencies (federated sign-on for operators, service accounts) have a documented local or break-glass path (cross-reference SEC-01).
5. Concentration in a single cloud provider or region across multiple functions is identified (cross-reference MCF-DEP-013/014).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum dependency of safety or continuity loops on cloud/SaaS services | count | 0 | Illustrative; profile may allow exceptions only with accountable acceptance. |

**Minimum evidence**

- Cloud/SaaS dependency register.
- Architecture diagrams for management and control planes.
- Configuration evidence of local fallback (local controller logic, cached credentials, on-premises DNS/NTP).
- Provider service descriptions and status-page history for the period.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; EMERGENCY; RECOVERY |
| periodCoverage | Register current; provider incident history for the preceding 12 months. |
| independence | Failure behaviour corroborated by configuration evidence or test, not provider marketing material. |
| mandatoryItems | Cloud/SaaS dependency register; Evidence that safety and continuity loops do not require cloud services |
| acceptableAlternatives | A completed RES-05 exercise simulating SaaS unavailability may substitute for configuration evidence for the functions exercised. |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-03 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-15, CG-10 require gate-level evaluation. |
| reassessmentTriggers | New cloud/SaaS service adopted for operations; Provider region or architecture change; Provider incident affecting operations; Identity federation change |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Obtain the register and management/control-plane architecture.
2. Reconcile register to egress firewall rules, DNS logs or configuration exports to find unregistered services.
3. For each service, obtain stated failure behaviour and check it against configuration evidence.
4. Confirm safety and continuity loops operate without cloud services.
5. Review provider incident history for events affecting operations.
6. Record Findings and UNKNOWN Records.

**Gate mappings.** CG-03 Critical dependency visibility (CRITICAL); CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to all Capability Instances. In hybrid cloud/on-premises patterns, cloud-hosted compute is a separate Capability Instance boundary matter (MCF-DEP-017).

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, EMERGENCY, RECOVERY

**Failure modes addressed.** Operators locked out when cloud identity provider fails (scenario X19); Cloud-hosted BMS analytics issuing setpoints with no local fallback; Cluster scheduler SaaS outage stops job admission; Container or model registry unavailable during recovery

**Testing safety.** Reconciliation uses log and configuration review only; blocking egress to test fallback is permitted only within an approved exercise with the facility operator's authorisation.

**UNKNOWN rule.** Unknown failure behaviour of a cloud/SaaS service on a management or control path of a critical function is a U10 UNKNOWN Record of severity US4.

**Ontology classes.** Dependency, Interface, Resource, RequiredFunction · **Related controls.** MCF-DEP-002, MCF-DEP-004, MCF-SEC-001, MCF-SEC-004, MCF-NET-024

**Informative references.** ISO/IEC 22123-1 (cloud computing vocabulary); ISO/IEC 19086-1 (cloud service level agreement framework); ISO/IEC 27017 (security controls for cloud services); CSA Cloud Controls Matrix

## DEP-04 Concentration and substitutability

### MCF-DEP-013

**Capacity Concentration** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** The share of AI capability concentrated in any single fault domain (site, building, hall, power train, UPS system, cooling loop or CDU group, scale-up domain, fabric pod, storage cluster) is quantified and kept within the impact tolerance of the Service Outcome.

**Requirement.** The capability owner shall calculate, for each declared fault domain, the proportion of the Capability Instance's usable capacity (for example accelerators, storage throughput, network bandwidth) that would be lost on its failure, and shall compare it with the concentration limit derived from the Service Outcome impact tolerance (CAP-03). Where a fault domain exceeds the limit, the capability owner shall record it as a CONCENTRATES relationship and either reduce the concentration, provide alternative capacity (RES-03) or obtain risk acceptance from the accountable owner.

**Assessment criteria**

1. Concentration is calculated for every fault domain in the RES-02 model, using current deployment data.
2. The concentration limit is derived from and traceable to the Service Outcome impact tolerance.
3. Fault domains exceeding the limit have an approved treatment or acceptance.
4. Calculations account for job topology: training jobs spanning several fault domains are counted as lost if any spanned domain fails, unless elastic recovery is evidenced.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum share of usable capability in one fault domain | % of usable capacity | Site-specific (no default) | Derived from the CAP-03 impact tolerance; there is no universal value. |

**Minimum evidence**

- Concentration analysis per fault domain.
- Deployment inventory and job placement data.
- Impact tolerance reference.
- Treatment or acceptance records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | Current deployment; recalculated at each capacity change. |
| independence | Calculation checked by a second analyst. |
| mandatoryItems | Concentration analysis; Traceability of limit to impact tolerance |
| acceptableAlternatives | A scheduler-generated report of capacity per fault domain is acceptable if its fault-domain labels are reconciled to RES-02. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03, CG-09 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Cluster expansion or consolidation; Change in job topology or placement policy; Change to fault-domain definitions |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW, RECONCILIATION

**Assessment procedure**

1. Obtain fault-domain model and deployment data.
2. Recompute concentration for a sample of fault domains.
3. Compare with limits and check traceability to impact tolerance.
4. Review treatment or acceptance for exceedances.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to all Capability Instances with more than one fault domain; a single-fault-domain capability records 100% concentration and its acceptance.

**Lifecycle stages.** PLAN, DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Majority of training capacity on one UPS system; All inference replicas in one hall; Large capability concentration exceeding tolerance

**Testing safety.** Desk-based analysis of deployment and placement data; no workload shall be moved or drained to test concentration.

**UNKNOWN rule.** If job placement or fault-domain labels are unavailable, record U1 UNKNOWN of severity US3 and treat the largest plausible concentration as the working value.

**Ontology classes.** FaultDomain, CapacityAssertion, CapabilityInstance, ServiceOutcome · **Related controls.** MCF-RES-005, MCF-RES-007, MCF-RES-010, MCF-CAP-010, MCF-CMP-008

**Informative references.** ISO 31000 (risk management); Regulation (EU) 2022/2554 (DORA), ICT concentration risk provisions — informative for financial-sector users

### MCF-DEP-014

**Supplier Concentration** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Single-source and sole-source reliance for critical products and services, including concentration at sub-tier (shared factories, components or logistics routes) and concentration in one firmware or software lineage, is identified and treated.

**Requirement.** The procurement lead shall maintain a supplier concentration analysis covering critical asset classes and services (accelerators and rack-scale systems, high-speed optics, switch silicon, storage media, transformers, MV/LV switchgear, UPS, generators, CDUs and pumps, chillers, BMS/EPMS platforms, maintenance contractors, specialist labour). For each, the procurement lead shall record whether supply is single-source (one qualified supplier available) or sole-source (only one supplier exists), the qualification time for an alternative, and known sub-tier concentration, and shall agree a treatment with the capability owner.

**Assessment criteria**

1. Each critical asset class and service has a recorded sourcing status (multi-, single-, sole-source).
2. Sub-tier concentration known from MCF-SUP-004 is incorporated (for example two transformer brands sharing one core-steel supplier).
3. Qualification time for an alternative supplier is estimated with basis.
4. Each single- or sole-source item has an agreed treatment (dual qualification, strategic stock, framework agreement, design change) or acceptance.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum share of a critical asset class from one supplier | % of installed base | Site-specific (no default) | Set in capability profile; standardisation benefits must be weighed against common-mode exposure. |

**Minimum evidence**

- Supplier concentration analysis.
- Approved supplier list.
- Sub-tier disclosures (from SUP-01).
- Treatment and acceptance records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; RECOVERY |
| periodCoverage | Current; reviewed at least annually. |
| independence | Review by a person outside the procurement function (engineering or risk). |
| mandatoryItems | Supplier concentration analysis with treatments |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Supplier exit, acquisition or allocation change; Sanctions or export-control change; New critical asset class |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INQUIRY

**Assessment procedure**

1. Obtain the concentration analysis and approved supplier list.
2. Check coverage of critical asset classes and services.
3. Verify sourcing status for a sample against market information and supplier disclosures.
4. Review treatments and acceptances.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to all critical asset classes and services.

**Lifecycle stages.** PLAN, DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, RECOVERY

**Failure modes addressed.** Sole-source accelerator allocation cut; One transformer supplier for all units with multi-year lead time; Single firmware lineage across all switches; Single contractor holds all specialist knowledge

**Testing safety.** Desk-based analysis; supplier enquiries shall not disclose site-sensitive architecture beyond what the supplier already holds under contract.

**UNKNOWN rule.** Unknown sourcing status for a critical class is US3; escalate to US4 where the class lies on a CG-10 restoration path with no strategic spare.

**Ontology classes.** Dependency, Resource, AssetInstance · **Related controls.** MCF-SUP-004, MCF-SUP-018, MCF-DEP-016, MCF-DEP-011

**Informative references.** ISO 22318 (guidelines for supply chain continuity); NIST SP 800-161r1 (cyber supply chain risk management); ISO 28000 (security and resilience: supply chain security management)

### MCF-DEP-015

**Knowledge Concentration** · PREVENTIVE · claim type DESIGN · required AL2

**Objective.** Knowledge essential to operate, maintain and recover critical systems (control logic, sequences of operation, protection philosophy, fabric configuration and tuning, storage recovery procedures, proprietary scripts) is not held by a single person or a single external party without a documented and tested transfer path.

**Requirement.** The operations manager shall identify knowledge items essential to each Required Function and record their holders, documentation status and accessibility. For each item held by fewer people than the profile minimum or held only by an external party, the operations manager shall implement documentation, cross-training or contractual access (including escrow of control logic and configuration where proprietary) and shall verify transfer by a practical demonstration.

**Assessment criteria**

1. Knowledge items essential to each Required Function are listed with holders.
2. Items below the minimum holder count have a documented treatment and target date.
3. Proprietary control logic and configuration for BMS/EPMS/CDU/PLC systems is held by the owner or in escrow, in a usable form.
4. At least one transfer per critical item has been demonstrated by a second holder performing the task or a walkthrough.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Minimum independent holders per critical knowledge item | persons | 2 | Illustrative; external parties count only where contractually available within response time. |

**Minimum evidence**

- Knowledge concentration register.
- Documentation inventory and storage location.
- Escrow or ownership evidence for control logic.
- Demonstration records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY; RECOVERY |
| periodCoverage | Current; reviewed annually and on staff change. |
| independence | Demonstration observed by someone other than the original holder. |
| mandatoryItems | Knowledge concentration register; Evidence of control-logic ownership or escrow |
| acceptableAlternatives | OEM contractual commitment to provide logic within a stated time is acceptable for non-safety logic. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-13, CG-10 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Departure of a key holder; Contractor change; New proprietary system |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY, OBSERVATION

**Assessment procedure**

1. Obtain register and documentation inventory.
2. Interview holders to test completeness.
3. Verify escrow or ownership of control logic.
4. Observe or review demonstration records.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to all critical systems; most material for proprietary control systems and bespoke automation.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, EMERGENCY, RECOVERY

**Failure modes addressed.** Only one engineer can modify CDU control logic; Integrator holds the only copy of PLC source; Fabric tuning undocumented

**Testing safety.** Demonstrations shall use simulators, test benches or walkthroughs; no live control-logic change for demonstration purposes.

**UNKNOWN rule.** Unknown holder count or inaccessible control logic for a critical system is US3; escalate to US4 where a CG-10 recovery step depends on it.

**Ontology classes.** Resource, Dependency, RequiredFunction · **Related controls.** MCF-DEP-008, MCF-OPS-004, MCF-SUP-008, MCF-GOV-023

**Informative references.** ISO 30401 (knowledge management systems); IEC 62443-2-4 (security requirements for IACS service providers)

### MCF-DEP-016

**Substitution Readiness** · RECOVERY · claim type EFFECTIVENESS · required AL5

**Objective.** For each material concentration or single external dependency, a substitute (alternative carrier path, alternate fuel supplier, mobile generation, temporary chillers or heat rejection, alternate OEM or qualified refurbished stock, alternate cloud region or provider, alternate capacity) can be brought into service within the time the Service Outcome tolerance allows, and this has been demonstrated.

**Requirement.** The capability owner shall define a substitution plan for each concentration or single dependency recorded under DEP-02 to DEP-04, stating the substitute, prerequisites (connection points, permits, contracts, qualification), activation authority and time-to-substitute. The capability owner shall validate each plan by test, exercise or documented precedent at the profile interval, and shall record the demonstrated time-to-substitute against tolerance.

**Assessment criteria**

1. Each recorded concentration or single external dependency has a substitution plan or an accepted no-substitute position.
2. Physical prerequisites (for example generator and chiller connection points, temporary fuel connections, spare fibre) exist and have been inspected.
3. Contractual prerequisites (call-off agreements, standby contracts) are current.
4. Each plan has been validated within the interval and demonstrated time-to-substitute is within tolerance, or the gap is recorded.
5. Lessons from validation have been incorporated.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Substitution validation interval | months | 24 | Illustrative; shorter for dependencies with high event frequency. |
| Time-to-substitute margin | % of tolerance | 75 (demonstrated time no more than 75% of tolerance) | Illustrative; provides margin for real-event degradation. |

**Minimum evidence**

- Substitution plans.
- Inspection records for physical prerequisites.
- Current call-off or standby contracts.
- Test, exercise or precedent records with timing.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E6; E7 |
| qualityFloor | P4 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | DEGRADED; EMERGENCY; RECOVERY |
| periodCoverage | Validation within the interval. |
| independence | Validation observed by a person independent of the plan owner. |
| mandatoryItems | Substitution plan; Validation record with demonstrated time |
| acceptableAlternatives | A documented real event in which the substitute was used is acceptable precedent if it occurred within the interval and conditions were comparable. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-10, CG-03 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Change to the dependency or substitute; Expiry of call-off contract; Validation interval elapsed |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, SCENARIO_EXERCISE, TEST

**Assessment procedure**

1. Obtain concentration and single-dependency records and corresponding plans.
2. Inspect physical prerequisites for a sample.
3. Verify contracts are current.
4. Review validation records and compare demonstrated times to tolerance.
5. Where proportionate, witness a substitution exercise.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to every material concentration or single external dependency; not applicable where an accepted no-substitute position exists and is reflected in the decision.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** DEGRADED, EMERGENCY, RECOVERY

**Failure modes addressed.** Temporary generator connection point missing or incompatible; Call-off contract expired; Substitute takes longer than tolerance; Alternate region lacks capacity at the time of need

**Testing safety.** Substitution tests involving temporary generation, temporary chillers, fuel transfer or electrical connection are hazardous; they require a method statement (MCF-OPS-006), permit to work (MCF-OPS-007), change approval (MCF-OPS-018) and authorisation by the facility operator's authorised person.

**UNKNOWN rule.** A plan never validated is UNKNOWN for the EFFECTIVENESS claim (U5 coverage gap, US3); where the dependency is on a CG-10 restoration path, US4.

**Ontology classes.** Dependency, Safeguard, TestRecord, FailureScenario · **Related controls.** MCF-RES-010, MCF-RES-011, MCF-DEP-013, MCF-DEP-014, MCF-SUP-019

**Informative references.** ISO 22301 (business continuity management systems); ISO 22318 (guidelines for supply chain continuity); NFPA 110 (emergency and standby power systems)

## DEP-05 Boundary and interface control

### MCF-DEP-017

**Assessment Boundary** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** The assessment boundary is drawn so that every material dependency of the Capability Instance is either inside it and assessed, or outside it and explicitly recorded as an external dependency with owner, evidence and decision effect; nothing material is excluded silently.

**Requirement.** The assurance lead shall define the assessment boundary for each Capability Instance by reference to the dependency graph (DEP-01), listing included systems, external dependencies crossing the boundary (with boundary interface, provider and evidence obtained), and exclusions with rationale and approver. The assurance lead shall reconcile the boundary with the asset-to-function map and upstream graph before fieldwork and after any material change, and shall treat any material dependency found outside the boundary and not recorded as a boundary defect.

**Assessment criteria**

1. The boundary statement lists included systems, crossing dependencies and exclusions, each with identifier.
2. Every dependency in the DEP-01 graph with strength absolute or material is either inside the boundary or recorded as a crossing dependency.
3. Each exclusion has a rationale and an approver with authority (GOV-01), and its decision effect is stated.
4. Each crossing dependency has an evidence plan (what will be obtained from the provider and how it will be verified).
5. Boundary reconciliation was performed before fieldwork and after material changes in the period.

**Minimum evidence**

- Approved boundary statement.
- Reconciliation record against DEP-01 graph.
- Exclusion approvals.
- Evidence plan for crossing dependencies.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY; RECOVERY |
| periodCoverage | Approved for the current assessment; reconciled within 30 days of fieldwork start. |
| independence | Boundary approved by a person with authority who is not the assessor performing reconciliation. |
| mandatoryItems | Approved boundary statement; Boundary-to-graph reconciliation record |
| acceptableAlternatives |  |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-02, CG-03 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Where the undetermined item concerns the boundary itself, the UNKNOWN is US5 and the decision is capped at INCONCLUSIVE. |
| reassessmentTriggers | Change in Capability Instance or Service Outcome; New dependency discovered; Provider change; Material architecture change |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Obtain the boundary statement, dependency graph and asset-to-function map.
2. Reconcile each material dependency to boundary inclusion or crossing record.
3. Check exclusion rationale, approver and decision effect.
4. Check evidence plans for crossing dependencies.
5. Record boundary defects as Findings and unresolved items as UNKNOWN Records.

**Gate mappings.** CG-02 Boundary and architecture integrity (CRITICAL); CG-03 Critical dependency visibility (CRITICAL)

**Applicability.** Applies to every assessment.

**Lifecycle stages.** PLAN, DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION

**Failure modes addressed.** Material dependency excluded without approval; Colocation provider infrastructure assumed in scope but not evidenced; Cloud control plane outside boundary but not recorded; Boundary drawn around compute only, ignoring facility dependencies

**Testing safety.** Desk-based.

**UNKNOWN rule.** A material dependency whose boundary status cannot be determined is a US5 Systemic UNKNOWN (it affects the boundary) and caps the decision at INCONCLUSIVE until resolved.

**Ontology classes.** ArchitectureSnapshot, Dependency, Interface, CapabilityInstance, UnknownRecord · **Related controls.** MCF-DEP-001, MCF-DEP-002, MCF-DEP-018, MCF-EVA-010, MCF-CAP-004

**Informative references.** ISO/IEC/IEEE 15026-2 (assurance case); ISO/IEC/IEEE 42010 (architecture description); ISO 19011 (guidelines for auditing management systems)

### MCF-DEP-018

**Provider Boundary** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** At every interface with a provider (colocation operator, utility, carrier, water or fuel supplier, cloud provider, managed-service or maintenance provider) the physical and logical demarcation point and the allocation of responsibility for operation, maintenance, monitoring, change, incident response and evidence are explicit for each lifecycle stage and operating state.

**Requirement.** The capability owner shall maintain, for each provider interface, a demarcation record identifying the physical or logical demarcation point (for example HV metering point, tenant breaker in provider switchboard, facility-water flange or CDU primary connection, meet-me room patch panel, cloud API boundary) and a shared-responsibility record conforming to AIDCF-003 (IOT-REQ-051) for each function across lifecycle stages and operating states, including who may operate, who responds to alarms, who approves changes and who holds evidence. The capability owner shall obtain the provider's acceptance of each record and shall treat any function without a responsible and an accountable party as a responsibility gap.

**Assessment criteria**

1. Each provider interface has a demarcation record with an identifiable physical or logical point.
2. Each shared function has a shared-responsibility record covering operation, maintenance, monitoring, change approval, incident response and evidence custody for NORMAL, MAINTENANCE, EMERGENCY and RECOVERY states.
3. The provider has accepted the record (signed, contractual schedule or equivalent).
4. Emergency authority across the boundary (for example who may shed tenant load or isolate a cooling loop) is explicit.
5. Responsibility gaps are recorded and dispositioned; contractual responsibility is not treated as proof of capability (IOT-REQ-052).

**Minimum evidence**

- Demarcation records with drawings or photographs of demarcation points.
- Shared-responsibility records.
- Provider acceptance evidence.
- Gap register.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY; RECOVERY |
| periodCoverage | Current; reviewed at contract renewal and annually. |
| independence | Records corroborated by the provider's own documentation (contract schedule, service description). |
| mandatoryItems | Demarcation record; Shared-responsibility record accepted by provider |
| acceptableAlternatives | Contract schedules containing equivalent allocation are acceptable if mapped to functions and states. |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-13 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-03 require gate-level evaluation. |
| reassessmentTriggers | Contract change or renewal; New provider; Incident revealing ambiguous responsibility; Change of demarcation point |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, INQUIRY, RECONCILIATION

**Assessment procedure**

1. List provider interfaces from the boundary statement.
2. Obtain demarcation and shared-responsibility records.
3. Inspect a sample of physical demarcation points.
4. Check states coverage and emergency authority.
5. Interview provider and owner staff on a sample of scenarios to test common understanding.
6. Record responsibility gaps.

**Gate mappings.** CG-13 Responsibility and authority (CRITICAL); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies wherever any function in the boundary is performed or supported by a third party.

**Lifecycle stages.** PLAN, BUILD, COMMISSION, OPERATE, CHANGE, DECOMMISSION · **Operating states.** NORMAL, MAINTENANCE, DEGRADED, EMERGENCY, RECOVERY

**Failure modes addressed.** Colocation responsibility gap (scenario X14); Neither party responds to a CDU primary-side alarm; Provider changes upstream configuration without tenant approval; Evidence held by provider not available to assessor

**Testing safety.** Inspection of demarcation points inside provider spaces requires provider escort and permission; no provider equipment shall be operated.

**UNKNOWN rule.** A critical function with no identifiable responsible or accountable party across a provider boundary is US4 (CG-13 criterion); an unaccepted but otherwise complete record is US3.

**Ontology classes.** Interface, Dependency, RequiredFunction, OperatingState · **Related controls.** MCF-DEP-017, MCF-DEP-019, MCF-GOV-006, MCF-OPS-002, MCF-SUP-005

**Informative references.** AIDCF-003 shared-responsibility record (IOT-REQ-051/052); EN 50600-3-1 (management and operational information); ISO/IEC 27036-3 (supplier relationships: ICT supply chain security)

### MCF-DEP-019

**Tenant Boundary** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** In shared or multi-tenant facilities and platforms, one tenant's load, configuration, actions or failures cannot propagate to another beyond declared limits, and shared infrastructure capacity is allocated and enforced.

**Requirement.** The platform or facility operator shall define for each shared resource (power path and UPS capacity, cooling loop and CDU capacity, coolant chemistry, fabric and storage, management plane) the per-tenant allocation, the enforcement mechanism (for example breaker sizing, power capping, flow limiting, QoS, quota) and the tenant obligations (load-step limits, coolant compatibility, change notification). The operator shall monitor tenant consumption against allocation and record exceedances as incidents.

**Assessment criteria**

1. Each shared resource has per-tenant allocations recorded.
2. Enforcement mechanisms are implemented and evidenced by configuration.
3. Tenant obligations are in agreements and are monitored.
4. Exceedances in the period are recorded and handled as incidents.
5. Tenant change that could affect shared infrastructure (for example new rack-scale systems with large load steps) requires operator approval.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Per-tenant load-step limit | kW per second | Site-specific (no default) | Derived from POW-05 load-step response analysis. |

**Minimum evidence**

- Allocation records per shared resource.
- Configuration evidence of enforcement.
- Tenant agreements with obligations.
- Consumption monitoring reports and exceedance incidents.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | Monitoring data for at least 3 months. |
| independence | Enforcement verified from configuration, not from tenant attestation. |
| mandatoryItems | Allocation records; Enforcement configuration evidence |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-09, CG-13 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | New tenant; Tenant expansion or hardware generation change; Shared resource capacity change |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS, SAMPLING

**Assessment procedure**

1. Obtain shared resource list and allocations.
2. Verify enforcement configuration for a sample.
3. Review monitoring and exceedances.
4. Review tenant change approvals.

**Gate mappings.** CG-09 Failure containment (SUPPORTING); CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies only to multi-tenant or shared-platform patterns. Not applicable to single-tenant dedicated facilities, with that pattern recorded in the boundary statement.

**Lifecycle stages.** DESIGN, BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Tenant rack load step trips shared UPS; Incompatible coolant introduced by tenant contaminates shared loop; Tenant consumes reserved headroom; Tenant fabric misconfiguration affects shared spine

**Testing safety.** No enforcement mechanism shall be tested by deliberate exceedance on live shared infrastructure.

**UNKNOWN rule.** Unverifiable enforcement on a shared resource supporting more than one tenant is US3; US4 where it is a CG-09 containment boundary.

**Ontology classes.** Interface, Resource, CapacityAssertion, FaultDomain · **Related controls.** MCF-PHY-012, MCF-NET-012, MCF-DEP-018, MCF-OPS-023, MCF-THM-017

**Informative references.** EN 50600-3-1 (management and operational information); ISO/IEC 27017 (cloud services security)

### MCF-DEP-020

**Cross-Boundary Enforcement** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** The conditions agreed at each boundary interface (power drawn, coolant supply temperature and flow, water quality, network traffic and routes, access) are measured at the boundary and deviations are detected, escalated and resolved, so that interface contracts operate in practice rather than on paper.

**Requirement.** The capability owner shall instrument each material boundary interface so that the agreed interface properties (per AIDCF-013 interface contracts) are measured at or near the demarcation point, shall set alarm thresholds for deviation, and shall route deviations to the responsible party under MCF-DEP-018 with escalation timelines. The capability owner shall review deviations and their resolution at the interval set in the capability profile.

**Assessment criteria**

1. Each material boundary interface has measured properties defined with units and thresholds.
2. Measurement exists at or near the demarcation point and data is retained for the period.
3. Deviations in the period were alarmed, routed to the responsible party and resolved within escalation timelines.
4. Recurring deviations have been raised as problems (MCF-OPS-016).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Interface deviation review interval | months | 1 | Illustrative. |

**Minimum evidence**

- Interface property definitions and thresholds.
- Boundary metering and telemetry data for the period.
- Deviation alarms and tickets with resolution times.
- Review records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | At least 6 months of operation (illustrative; profile-defined). |
| independence | Telemetry extracted by the assessor or from a system not controlled by the party being monitored where possible. |
| mandatoryItems | Boundary telemetry for the period; Deviation tickets |
| acceptableAlternatives | Provider-supplied measurements are acceptable if cross-checked against at least one owner-side measurement. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-09, CG-15 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | New interface or changed contract property; Repeated deviations; Metering change |

**Assessment methods.** ANALYSIS, SAMPLING, DOCUMENT_REVIEW, RECONCILIATION

**Assessment procedure**

1. Obtain interface property definitions.
2. Extract boundary telemetry for the period and identify deviations independently.
3. Reconcile independently identified deviations with alarms and tickets.
4. Check resolution times against escalation timelines.
5. Check problem records for recurrence.

**Gate mappings.** CG-09 Failure containment (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to material boundary interfaces where measurement is technically possible; where it is not, the gap is recorded as an UNKNOWN Record rather than not applicable.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Coolant supply temperature from provider above agreed limit undetected; Tenant draws above allocated power without alarm; Upstream route change unnoticed

**Testing safety.** Read-only telemetry extraction.

**UNKNOWN rule.** Missing boundary telemetry for a material interface is U1 UNKNOWN, US3; US4 where the interface is a CG-06 or CG-05 supply interface.

**Ontology classes.** Interface, Event, Dependency, CapacityAssertion · **Related controls.** MCF-DEP-018, MCF-DEP-021, MCF-OPS-013, MCF-OPS-022

**Informative references.** AIDCF-013 interface contracts; IEC 61000-4-30 (power quality measurement methods); ASHRAE TC 9.9 liquid cooling guidance

## DEP-06 Dependency monitoring and review

### MCF-DEP-021

**Dependency Health Indicators** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** The health of each material external and shared dependency is observed continuously or periodically through defined indicators, so that deterioration is detected before it defeats a Service Outcome.

**Requirement.** The operations manager shall define health indicators for each material dependency (for example utility voltage events and frequency deviations, fuel stock and delivery status, facility water pressure and quality, carrier circuit errors and availability, cloud/SaaS service status, OEM case backlog and RMA turnaround, spares stock against minimum) with thresholds and alarm routing into the NOC/BMS, and shall review indicator trends at the profile interval.

**Assessment criteria**

1. Each material dependency has at least one defined health indicator with threshold.
2. Indicators are collected and visible to the NOC or BMS operators.
3. Threshold breaches in the period generated alarms or tickets and were acted on.
4. Trend reviews were held at the interval and recorded actions.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Dependency trend review interval | months | 3 | Illustrative. |

**Minimum evidence**

- Indicator definitions.
- Dashboards or reports for the period.
- Threshold breach tickets.
- Trend review minutes.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | At least 6 months. |
| independence | Indicator data sampled by the assessor from source systems. |
| mandatoryItems | Indicator definitions with thresholds; Indicator data for the period |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | New material dependency; Indicator source change; Incident not preceded by indicator warning |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, SAMPLING, OBSERVATION

**Assessment procedure**

1. Obtain indicator definitions and map to material dependencies.
2. Observe NOC/BMS visibility of indicators.
3. Sample threshold breaches and trace to action.
4. Review trend minutes.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to all material dependencies recorded under DEP-01 to DEP-03.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Fuel stock below minimum unnoticed; Carrier error rate rising before outage; OEM RMA backlog growing; Cloud identity degradation not visible to operators

**Testing safety.** Observation only.

**UNKNOWN rule.** No indicator for a material dependency is US3 for OPERATION claims.

**Ontology classes.** Dependency, Event, Resource · **Related controls.** MCF-DEP-020, MCF-DEP-022, MCF-OPS-013, MCF-SUP-017

**Informative references.** ISO 22301 (business continuity management systems); EN 50600-3-1 (management and operational information)

### MCF-DEP-022

**Provider Performance** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Actual performance of each material provider against service levels and against the needs of the Service Outcome is measured and reviewed, and persistent shortfall leads to action.

**Requirement.** The supplier manager shall measure each material provider's performance against contracted service levels (availability, response and restore times, RMA turnaround, notification timeliness, RCA quality) from owner-side records, review it with the provider at the profile interval, and escalate persistent or material shortfall to the capability owner for treatment.

**Assessment criteria**

1. Measured performance from owner-side records exists for each material provider for the period.
2. Reviews were held at the interval with recorded actions.
3. Shortfall against service levels or Service Outcome needs was escalated and treated.
4. Provider RCAs for significant incidents were received and assessed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Provider review interval | months | 3 | Illustrative. |

**Minimum evidence**

- Performance measurements.
- Review minutes.
- Escalation records.
- Provider RCAs.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | At least 12 months. |
| independence | Measurement from owner-side tickets and telemetry, not provider self-reporting only. |
| mandatoryItems | Owner-side performance measurement |
| acceptableAlternatives | Provider reports are acceptable if reconciled to a sample of owner tickets. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-13 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Major provider incident; Contract renewal; Repeated shortfall |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, SAMPLING

**Assessment procedure**

1. Obtain service levels and measurements.
2. Recompute a sample of measurements from tickets.
3. Review minutes and escalation records.
4. Assess RCAs.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to material providers.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, RECOVERY

**Failure modes addressed.** Provider restore times exceed tolerance without escalation; Self-reported provider metrics mask shortfall; RCAs not received

**Testing safety.** Not applicable to physical testing; review only.

**UNKNOWN rule.** Absence of owner-side measurement is U1, US3 for OPERATION claims.

**Ontology classes.** Dependency, Event, Finding · **Related controls.** MCF-SUP-005, MCF-DEP-021, MCF-SUP-007

**Informative references.** ISO/IEC 20000-1 (service management system requirements); ISO 44001 (collaborative business relationship management)

### MCF-DEP-023

**Change Detection** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Changes that alter the dependency graph, whether made internally or by providers (carrier reroute, utility network reconfiguration, cloud region or API change, OEM licensing or end-of-life notice, contractor change, new tenant), are detected and the dependency records and affected assessments are updated.

**Requirement.** The dependency owner shall operate a change-detection process that combines internal change records (OPS-05), provider notifications, contract events and technical discovery (for example route and configuration diffs) to identify changes to material dependencies, and shall update the dependency graph and raise reassessment triggers within the time set in the capability profile.

**Assessment criteria**

1. Sources of dependency change are defined (internal changes, provider notifications, contract events, discovery).
2. Changes in the period were reflected in the dependency graph within the profile time.
3. Each material dependency change raised a ReassessmentTrigger where required.
4. A sample of provider notifications reconciles to graph updates.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum time to update dependency graph after detected change | working days | 10 | Illustrative. |

**Minimum evidence**

- Change-detection procedure.
- Provider notifications for the period.
- Graph version history.
- ReassessmentTrigger records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; TRANSITION |
| periodCoverage | At least 6 months. |
| independence | Reconciliation by assessor of notifications to graph versions. |
| mandatoryItems | Graph version history; Provider notifications |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-14, CG-03 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Change-detection source added or lost; Missed change revealed by incident |

**Assessment methods.** RECONCILIATION, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Obtain procedure and sources.
2. Sample provider notifications and internal changes.
3. Trace to graph updates and reassessment triggers.
4. Measure update latency.

**Gate mappings.** CG-14 Change control (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to all assessments with OPERATION claims on dependency controls.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, TRANSITION, MAINTENANCE

**Failure modes addressed.** Carrier reroute merges diverse paths unnoticed; OEM licensing change not reflected; Contractor change removes authorised staff

**Testing safety.** Review only.

**UNKNOWN rule.** Inability to show that provider notifications are received is U5, US3; escalate to US4 if a CG-03 critical dependency changed in the period without update.

**Ontology classes.** Event, Dependency, ReassessmentTrigger · **Related controls.** MCF-OPS-018, MCF-DEP-024, MCF-EVA-022

**Informative references.** ISO/IEC 20000-1 (service management system requirements); SAE EIA-649C (configuration management standard)

### MCF-DEP-024

**Periodic Revalidation** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** The dependency graph, route records, provider demarcations and concentration analyses are revalidated against fresh evidence at a defined interval, so that dependency visibility does not decay between change events.

**Requirement.** The dependency owner shall revalidate every material dependency record at the interval set in the capability profile by obtaining current evidence (walk-down, configuration export, provider statement or contract), shall mark records not revalidated within the interval as STALE, and shall treat stale records as UNKNOWN for assessment purposes.

**Assessment criteria**

1. A revalidation schedule covering all material dependency records exists.
2. Records were revalidated within the interval, with evidence attached.
3. Stale records are flagged and treated as UNKNOWN.
4. Revalidation findings led to graph updates.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Revalidation interval for material dependencies | months | 12 | Illustrative; shorter for high-churn dependencies (cloud services, carriers). |

**Minimum evidence**

- Revalidation schedule.
- Revalidation evidence per record.
- Stale record list.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | One full revalidation cycle. |
| independence | Revalidation evidence from a source other than the record itself. |
| mandatoryItems | Revalidation schedule and evidence |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Interval elapsed; Change in revalidation source |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, RECONCILIATION

**Assessment procedure**

1. Obtain schedule and record list.
2. Sample records and check revalidation date and evidence.
3. Confirm stale flagging and treatment.
4. Check resulting updates.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to all material dependency records.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Dependency graph accurate at build but stale years later; Provider demarcation changed without update

**Testing safety.** Walk-downs follow site safety rules as for MCF-DEP-001.

**UNKNOWN rule.** Stale material dependency records are U3 UNKNOWN; severity follows the dependency's gate role (US4 for CG-03 critical dependencies).

**Ontology classes.** Dependency, EvidenceObject, ReassessmentTrigger · **Related controls.** MCF-DEP-023, MCF-EVA-021, MCF-DEP-001

**Informative references.** AIDCF-008 freshness rule; ISO 55001 (asset management systems)
