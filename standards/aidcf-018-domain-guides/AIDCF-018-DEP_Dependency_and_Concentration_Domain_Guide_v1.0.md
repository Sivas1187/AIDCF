# AIDCF-018-DEP Dependency, Concentration and External Reliance Management Domain Guide

## Document control

| Field | Value |
|---|---|
| Document ID | AIDCF-018-DEP |
| Title | Dependency, Concentration and External Reliance Management Domain Guide |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Parent artifact | AIDCF-018 Domain Guides |
| Normative basis | AIDCF-007A (controls MCF-DEP-001 to MCF-DEP-024), AIDCF-008, AIDCF-010 |
| Requirement prefix | DG-DEP-REQ-NNN |

### Revision history

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-10 | First issue of the DEP domain guide, aligned with the rewritten DEP controls in AIDCF-007A and the per-control gate mapping rule. |

### Status of this guide

This guide explains how to apply the 24 DEP controls of AIDCF-007A. The control records (objective, requirement, assessment criteria, evidence profile, gate mappings) are normative and are held in the AIDCF-007A registry; where this guide and a control record differ, the control record governs and the difference shall be raised as a baseline issue. The requirements numbered DG-DEP-REQ-NNN in this guide are normative for assessments that claim conformance to AIDCF-018-DEP. Other text is informative.

## 1 Purpose and scope

### 1.1 Purpose

The DEP domain establishes whether the dependencies on which an AI Capability Instance relies are known, owned, evidenced and kept current, and whether concentration and common-mode exposure are understood well enough to support the resilience claims made in other domains. It is the domain that turns "we have two of everything" into "these two things do not share anything that matters, and here is the evidence".

In the canonical assurance chain (Decision Question → Capability Instance → Service Outcome → Required Function → Architecture → Dependency and Fault Domain → Threat / Hazard / Failure Scenario → Safeguard → Control → …), DEP owns step 6 as an assurance object: it provides the dependency graph, shared-source and shared-route analysis, concentration analysis and boundary definition that the other domains consume when they argue continuity, containment and recovery.

### 1.2 In scope

- Mapping of Required Functions to the InfrastructureSystems and AssetInstances that implement them, per operating state (DEP-01).
- Upstream, downstream and recovery-only dependency tracing, including timing/information services, identity, licensing and repositories (DEP-01).
- Shared-source, common-controller, shared-route and shared-human analysis across nominally redundant or diverse paths (DEP-02).
- External provider and utility reliance: grid interconnection and capacity reservations, water and fuel supply, carriers and diverse routes, OEM operating dependencies, hyperscale cloud and SaaS control planes (DEP-03).
- Concentration of capability, supplier and knowledge, and readiness to substitute (DEP-04).
- The assessment boundary, provider demarcations, tenant boundaries and enforcement of interface conditions across them (DEP-05).
- Health indicators, provider performance, detection of dependency change and periodic revalidation (DEP-06).

### 1.3 Out of scope

- The engineering adequacy of the power, thermal, compute, storage and network systems themselves (POW, THM, CMP, STO, NET). DEP establishes that a dependency exists and whether it is shared; the owning domain establishes whether it performs.
- Supplier due diligence, contract terms, provenance and remote third-party access (SUP). DEP records the dependency on an OEM or provider; SUP assures the relationship.
- Fault-domain definition, containment and blast-radius design (RES-02). DEP supplies the shared-source and shared-route facts that RES uses to draw fault domains.
- Security of the control plane (SEC). DEP records cloud and identity dependencies; SEC assures their protection.

### 1.4 Boundaries with other domains

| Topic | DEP role | Owning domain role |
|---|---|---|
| Utility capacity and quality | Records the contractual and technical basis of supply and reconciles firm capacity to demand (MCF-DEP-009) | POW-01 assures utility capacity, quality, connection reliability and contingency |
| Carrier diversity | Records carriers, underlying operators and route evidence (MCF-DEP-010, MCF-DEP-007) | NET-01/NET-05 assure path diversity and path documentation inside the fabric |
| OEM support | Records the operating dependency on OEM services (MCF-DEP-011) | SUP-02/SUP-06 assure contract obligations and support access |
| Fault domains | Supplies shared-source and route facts (DEP-02) | RES-02 defines and validates fault domains |
| Recovery | Maps recovery-only dependencies and circular dependencies (MCF-DEP-004) | RES-04 sequences recovery; POW/THM/CMP/STO/NET restore their systems |
| Boundary | Defines the assessment boundary by reference to the dependency graph (MCF-DEP-017) | EVA-03 governs assessment scope and criteria; CAP-01 links capability to architecture |

## 2 Why this domain matters for AI capability

AI data centres concentrate unusual amounts of capability in a small number of systems. A single training job may span thousands of accelerators that must all be available at once; a synchronous collective operation fails if a single participating node fails, so the job is only as available as the least available dependency it touches. Rack power densities and direct-to-chip liquid cooling reduce thermal ride-through to the point where the time between losing a cooling dependency and losing the outcome can be very short; that time is a site-specific value to be measured, not assumed. Growth is constrained by grid interconnection and by long-lead electrical equipment, so capacity commitments depend on utility energisation schedules and manufacturing slots outside the operator's control.

These properties make hidden dependencies unusually consequential:

- **Redundancy defeated by a shared upstream node.** Two utility feeds supplied from the same grid substation, two carriers riding one long-haul fibre, two fuel contracts drawn from one terminal, or two chilled-water plants fed by one make-up water main defeat the redundancy that POW, THM and NET rely on.
- **Control-plane reach.** Modern facilities depend on software: BMS/EPMS servers, CDU controllers with lead-lag logic, cluster managers and schedulers, fabric controllers, identity providers, licence and entitlement servers, and cloud-hosted analytics. A single controller, firmware lineage or SaaS outage can act on all redundant members at once.
- **Recovery-only dependencies.** Restoration often depends on things that are idle in NORMAL operation and therefore untested: generator start batteries, fuel resupply, out-of-band networks, golden images, licence servers, break-glass credentials, OEM remote support, spares and specialist labour. Circular dependencies (cooling controls need the network, the network needs cooled equipment) are common in designs that were not analysed for the RECOVERY state.
- **Concentration.** Standardising on one accelerator generation, one switch silicon family or one firmware baseline improves operability but concentrates common-mode exposure; placing most of a training capability on one UPS system or one CDU loop concentrates consequence.

The DEP domain makes these exposures explicit so that gate CG-03 (Critical dependency visibility) can be evaluated on evidence, and so that the resilience claims evaluated at CG-05, CG-06, CG-08, CG-09 and CG-10 are not built on unverified independence.

## 3 Reference patterns and variants

AIDCF-013 defines the reference patterns. Their DEP-specific emphasis is summarised here.

| Pattern (AIDCF-013) | Dominant DEP concerns | Controls most exercised |
|---|---|---|
| Single-site training facility | Shared upstream utility and carrier nodes; capacity concentration in one site; recovery dependencies on site-resident images and tools | MCF-DEP-005, MCF-DEP-007, MCF-DEP-013, MCF-DEP-004 |
| Dual-site capability | Proof that the sites do not share grid supply point, carrier routes, cloud control plane, identity or supplier; substitution of one site by the other | MCF-DEP-005, MCF-DEP-012, MCF-DEP-016 |
| Colocation deployment | Provider demarcation and shared responsibility; access to provider evidence on utility, generators and cooling | MCF-DEP-018, MCF-DEP-017, MCF-DEP-020 |
| Hyperscale campus | Shared campus substations and heat rejection; campus-wide control planes; carrier concentration at campus entry | MCF-DEP-005, MCF-DEP-006, MCF-DEP-010 |
| Liquid-cooled high-density cluster | Short time-to-impact; CDU common controllers; facility-water interfaces | MCF-DEP-003, MCF-DEP-006, MCF-DEP-020 |
| Hybrid cloud/on-premises | Cloud and SaaS control-plane dependencies; identity federation; boundary treatment of cloud-hosted capacity | MCF-DEP-012, MCF-DEP-017 |
| Sovereign AI environment | Disclosure limits on providers; jurisdiction of control planes and support; sub-tier visibility | MCF-DEP-012, MCF-DEP-002, MCF-DEP-011 |
| Shared multi-tenant platform | Tenant boundary enforcement; shared resource allocation | MCF-DEP-019, MCF-DEP-020 |
| Edge inference estate | Dependency on carrier and remote management; low staffing; many small concentrations | MCF-DEP-010, MCF-DEP-008, MCF-DEP-013 |
| Brownfield retrofit | Stale drawings and route records; legacy controllers shared with retained plant | MCF-DEP-001, MCF-DEP-007, MCF-DEP-024 |
| Recovery-capacity pool | Proof that the pool does not share dependencies with the capacity it protects | MCF-DEP-004, MCF-DEP-005, MCF-DEP-016 |

**Variants.** Two variants change how the controls are applied. In a *tenant-only* assessment (the assessed party leases space and power), DEP-03 and DEP-05 evidence about utility, generators and heat rejection comes through the provider; where it cannot be obtained, the dependency is recorded with an UNKNOWN Record rather than treated as out of scope (MCF-DEP-017). In a *design-stage* assessment, MCF-DEP-001 is replaced by design-model mapping and IMPLEMENTATION claims remain NOT_ASSESSED until assets exist.

## 4 Required functions and capability linkage

DEP does not deliver a Service Outcome directly; it delivers the knowledge that makes other domains' Required Functions assessable. The Required Functions DEP assures are:

| Required Function (assurance view) | Linked Service Outcomes | Controls |
|---|---|---|
| Dependency knowledge: every material dependency of every Required Function is identified and owned | All outcomes of the Capability Instance | MCF-DEP-001, MCF-DEP-002, MCF-DEP-003, MCF-DEP-004 |
| Independence assurance: redundancy and diversity claims rest on evidenced independence | Availability and recovery outcomes | MCF-DEP-005 to MCF-DEP-008 |
| External reliance management: utilities, carriers, OEMs and cloud/SaaS are characterised for the declared demand and states | Availability, performance, growth and recovery outcomes | MCF-DEP-009 to MCF-DEP-012 |
| Concentration management: consequence and supplier concentration are within tolerance or treated | Availability and recovery outcomes | MCF-DEP-013 to MCF-DEP-016 |
| Boundary integrity: the assessed boundary and provider and tenant interfaces are explicit and enforced | All outcomes; decision scope | MCF-DEP-017 to MCF-DEP-020 |
| Dependency currency: dependency knowledge remains current | All outcomes | MCF-DEP-021 to MCF-DEP-024 |

Linkage to capability is through the relationships of AIDCF-014 §9: a ServiceOutcome is linked to RequiredFunctions by REQUIRES_FUNCTION; each RequiredFunction is IMPLEMENTED_BY InfrastructureSystems; systems DEPENDS_ON Resources and other systems; pairs SHARES_FAULT_DOMAIN_WITH one another where DEP-02 finds a shared source or route; and loss PROPAGATES_TO outcomes along the paths recorded under MCF-DEP-003. AIDCF-003 §39 provides the finer-grained common-mode predicates (SHARES_DEPENDENCY_WITH, INDEPENDENT_OF, CONCENTRATES, SINGLE_POINT_FOR) used in the dependency register; these are recorded as qualifiers on canonical relationships, not as additional relationship types.

## 5 Dependencies, fault domains and common-mode concerns

### 5.1 Dependency classes to trace

Assessors should check that the upstream graph (MCF-DEP-002) covers each AIDCF-003 §38 dependency class that applies: electrical, thermal, hydraulic, mechanical/structural, network, control-system, timing/information, human/procedural, supplier/contractual, geographic/environmental, capacity, and recovery-only. In AI facilities the classes most often missing are timing/information (DNS, NTP/PTP, DHCP/PXE, IPAM, certificate authorities, licence servers), control-system (shared PLCs and BMS servers), and recovery-only.

### 5.2 Characteristic common modes

| Common mode | Typical evidence of the shared element | Where it bites |
|---|---|---|
| Grid supply point or transmission circuit shared by "independent" feeds | Utility connection documentation; network operator statement | CG-05; scenario X01 |
| Carrier resale over one underlying fibre or duct | Underlying-carrier disclosure; route KMZ; latency fingerprint | CG-08 connectivity outcomes; out-of-band management |
| Single building entry, riser or meet-me room for diverse paths | Route drawings; inspection | Scenario X09, X16 |
| Shared make-up water or one water utility for all heat rejection | Water supply permits; P&ID | CG-06; scenario X10 |
| Shared BMS/EPMS server, CDU lead-lag controller or PLC | Control architecture; configuration | CG-07; scenario X05 |
| One firmware lineage or rollout pipeline across redundant members | Repository and rollout records | Scenario X08 |
| One identity provider for operators and service accounts | Identity federation design | CG-15; scenario X19 |
| One maintenance contractor for all units of a redundant group | Contracts | Scenario X04 |
| One authorised person able to perform critical switching at night | Rosters; authorisation register | CG-04; CG-05 |

### 5.3 Fault-domain handoff

DEP findings are inputs to RES-02. Every shared element found by DEP-02 shall be visible in the fault-domain model as a SHARES_FAULT_DOMAIN_WITH relationship or as a documented reason why it is not material.

**DG-DEP-REQ-001** The assessor shall confirm that every shared source, common controller, shared route and shared human dependency recorded under MCF-DEP-005 to MCF-DEP-008 for an in-scope Required Function is represented in the RES-02 fault-domain model or has a recorded materiality rationale.

### 5.4 Strength and state

Dependencies differ by state. A generator fuel contract is a supporting dependency in NORMAL and absolute in EMERGENCY after the first hours of a utility outage; an OEM licence server may be irrelevant in NORMAL and absolute in RECOVERY. The dependency record's applicableStates field (AIDCF-003 §37) shall be populated; a record that lists only NORMAL for a dependency that is material in EMERGENCY or RECOVERY is a Finding.

## 6 Threats, hazards and failure scenarios with propagation paths

The following scenarios from the AIDCF-004 cross-domain library are those in which a DEP control failure is the decisive weakness. Each path is written from initiating condition to Service Outcome.

| Scenario | Initiating condition | Propagation path to Service Outcome | DEP controls that interrupt the path |
|---|---|---|---|
| X01 Utility loss + generator no-start + UPS autonomy exhaustion | Grid fault at a shared upstream substation removes both utility feeds | Both feeds lost → generators required → start failure on one set and inadequate capacity on the remainder → UPS autonomy exhausted → loss of power to accelerator racks → training job failure, work lost since last checkpoint; inference unavailability | MCF-DEP-005 reveals the shared substation; MCF-DEP-009 records the supply-point arrangement; MCF-DEP-003 states time-to-impact |
| X04 Maintenance removes hidden shared dependency | Planned maintenance isolates a switchboard believed to feed only A-side loads | Hidden B-side dependency (for example a CDU controller power supply or a BMS network switch) lost → CDU controller loses power → secondary-loop pumps fail or go to an unsafe default → cold-plate temperatures rise within ride-through → accelerator throttling then shutdown | MCF-DEP-001 asset-to-function mapping; MCF-DEP-006 common controller analysis |
| X09 Fire disables paired infrastructure routes | Fire in a riser through which A and B paths both pass | Both paths lost → loss of power or cooling to a hall → outcome loss beyond the expected fault domain | MCF-DEP-007 shared route analysis |
| X10 Extreme ambient plus water restriction | Heatwave with utility water restriction | Evaporative heat rejection capacity reduced → chilled or facility water temperature rises → CDU approach temperature exceeded → throttling → performance outcome missed | MCF-DEP-009 records restriction triggers; MCF-DEP-005 identifies shared water source |
| X14 Colocation responsibility gap | Alarm on the primary side of a CDU at a provider demarcation | Neither provider nor tenant responds → loss of facility water flow → thermal trip of racks | MCF-DEP-018 provider boundary; MCF-DEP-020 cross-boundary enforcement |
| X17 Expansion creates stranded compute | Utility energisation slips or firm capacity reduced | Installed accelerators cannot be energised → growth outcome missed; capital stranded | MCF-DEP-009 capacity reservation tracking; MCF-DEP-013 |
| X18 Loss of remote OEM support | OEM support channel unavailable during a fabric or storage failure | Diagnosis and repair delayed beyond recovery tolerance | MCF-DEP-011; MCF-DEP-016 |
| X19 Shared authentication service failure | Cloud identity provider outage | Operators cannot log in to BMS/EPMS or cluster management → delayed response to unrelated incident; automation using service accounts fails | MCF-DEP-012; MCF-DEP-004 |
| X15 Recovery reintroduces corrupt configuration | Configuration backups stored in the failed fault domain or not validated | Recovery restores a bad state or cannot restore at all | MCF-DEP-004 |

Threat sources (AIDCF-004 Part IV) relevant to DEP include utility manipulation, supply-chain compromise and coordinated multi-vector attack, where a capable adversary targets the shared element precisely because it is shared. Hazards include meteorological and hydrological events affecting shared routes and sources, and utility or geopolitical disruption affecting providers.

## 7 Safeguards

DEP safeguards are mostly preventive (knowledge that stops a consequential action being taken in ignorance) and detective (indicators that reveal deterioration of an external dependency). They are effective only if other domains use them.

| Safeguard | Function | Delivered by |
|---|---|---|
| Versioned dependency graph reconciled to as-built | Prevents action on an incomplete model; feeds change impact assessment | MCF-DEP-001, MCF-DEP-002 |
| Shared-element registers | Converts hidden common modes into declared, owned fault domains | MCF-DEP-005 to MCF-DEP-008 |
| Firm-capacity reconciliation and curtailment mapping | Prevents commitment of capability beyond firm supply | MCF-DEP-009 |
| Local fallback for cloud/SaaS dependencies | Keeps safety and continuity loops independent of external control planes | MCF-DEP-012 |
| Concentration limits traceable to impact tolerance | Bounds consequence of single fault-domain loss | MCF-DEP-013 |
| Validated substitution plans | Restores capability when a single dependency fails | MCF-DEP-016 |
| Explicit demarcation and shared-responsibility records | Prevents responsibility gaps at provider and tenant boundaries | MCF-DEP-018, MCF-DEP-019 |
| Boundary-point measurement | Detects breach of interface conditions | MCF-DEP-020 |
| Dependency health indicators and change detection | Detects deterioration and silent change | MCF-DEP-021, MCF-DEP-023 |
| Revalidation with STALE marking | Prevents reliance on decayed evidence | MCF-DEP-024 |

## 8 Critical-gate linkage

DEP is the principal domain for CG-03 (Critical dependency visibility). It also holds the boundary control that is CRITICAL for CG-02 and the provider-boundary control that is CRITICAL for CG-13. Its other mappings are SUPPORTING: a NONCONFORMING result requires gate-level evaluation (AIDCF-010) but does not automatically fail the gate.

| Gate | Gate name | CRITICAL controls in this domain | SUPPORTING controls in this domain |
|---|---|---|---|
| CG-02 | Boundary and architecture integrity | MCF-DEP-017 | MCF-DEP-001 |
| CG-03 | Critical dependency visibility | MCF-DEP-001, MCF-DEP-002, MCF-DEP-005, MCF-DEP-007, MCF-DEP-009, MCF-DEP-010, MCF-DEP-012, MCF-DEP-017 | MCF-DEP-003, MCF-DEP-004, MCF-DEP-006, MCF-DEP-008, MCF-DEP-011, MCF-DEP-013, MCF-DEP-014, MCF-DEP-016, MCF-DEP-018, MCF-DEP-021, MCF-DEP-023, MCF-DEP-024 |
| CG-05 | Resilient electrical supply | none | MCF-DEP-005, MCF-DEP-009 |
| CG-06 | Thermal continuity | none | MCF-DEP-005 |
| CG-07 | Critical control-system integrity | none | MCF-DEP-006 |
| CG-09 | Failure containment | none | MCF-DEP-003, MCF-DEP-005, MCF-DEP-006, MCF-DEP-007, MCF-DEP-013, MCF-DEP-019, MCF-DEP-020 |
| CG-10 | Recovery readiness | none | MCF-DEP-004, MCF-DEP-010, MCF-DEP-011, MCF-DEP-012, MCF-DEP-015, MCF-DEP-016 |
| CG-13 | Responsibility and authority | MCF-DEP-018 | MCF-DEP-008, MCF-DEP-015, MCF-DEP-019, MCF-DEP-022 |
| CG-14 | Change control | none | MCF-DEP-023 |
| CG-15 | Integrated digital authority over infrastructure | none | MCF-DEP-002, MCF-DEP-012, MCF-DEP-020 |

CRITICAL controls in this domain:

- **MCF-DEP-001 Asset-to-Function Mapping** — CRITICAL for CG-03; claim type IMPLEMENTATION at AL3, sufficiency floor S4.
- **MCF-DEP-002 Upstream Dependency Mapping** — CRITICAL for CG-03; claim type IMPLEMENTATION at AL3, sufficiency floor S4.
- **MCF-DEP-005 Shared Source Analysis** — CRITICAL for CG-03; claim type IMPLEMENTATION at AL3, sufficiency floor S4.
- **MCF-DEP-007 Shared Route Analysis** — CRITICAL for CG-03; claim type IMPLEMENTATION at AL3, sufficiency floor S4.
- **MCF-DEP-009 Utility Dependency** — CRITICAL for CG-03; claim type IMPLEMENTATION at AL3, sufficiency floor S4.
- **MCF-DEP-010 Telecom Dependency** — CRITICAL for CG-03; claim type IMPLEMENTATION at AL3, sufficiency floor S4.
- **MCF-DEP-012 Cloud and Service Dependency** — CRITICAL for CG-03; claim type IMPLEMENTATION at AL3, sufficiency floor S4.
- **MCF-DEP-017 Assessment Boundary** — CRITICAL for CG-02, CG-03; claim type IMPLEMENTATION at AL3, sufficiency floor S4.
- **MCF-DEP-018 Provider Boundary** — CRITICAL for CG-13; claim type IMPLEMENTATION at AL3, sufficiency floor S3.

**Gate roll-up reminder (AIDCF-010).** For CG-03, a single PARTIAL or NONCONFORMING result on any of the CRITICAL controls above yields a gate FAIL; an UNKNOWN or NOT_ASSESSED result yields gate UNKNOWN. The CG-03 evidence floor is S4; the CRITICAL controls in this domain carry sufficiency floor S4 accordingly. MCF-DEP-017 is also CRITICAL for CG-02 (floor S3), and an undetermined boundary status is a US5 Systemic UNKNOWN that caps the decision at INCONCLUSIVE.

**DG-DEP-REQ-002** Where a CG-03 CRITICAL control is assessed by sampling, the assessor shall state the population, sample and selection basis in the Control Assessment, and shall not record CONFORMING unless the sample includes dependencies of every dependency class that applies to the Required Functions in scope.

## 9 Capability-profile parameters

The parameters below are carried in the control records. All defaults are illustrative and shall be replaced in the capability profile with site-specific values and their basis; "no default" indicates a value that must be derived for the site.

| Parameter | Unit | Illustrative default | Basis | Control |
|---|---|---|---|---|
| Mapping completeness for critical Required Functions | % of functions with verified mapping | 100 | Illustrative; any unmapped critical function defeats dependency visibility, so the profile normally sets 100%. | MCF-DEP-001 |
| Reconciliation sample size | assets per InfrastructureSystem | 10 or all if fewer | Illustrative; set by AIDCF-009 sampling rules and population size. | MCF-DEP-001 |
| Reconciliation interval | months | 12 | Illustrative; shorten for estates with high deployment churn such as accelerator cluster expansion. | MCF-DEP-001 |
| Minimum trace depth beyond boundary | upstream nodes | 1 (first shared upstream node) | Illustrative; deeper tracing is set in the profile where concentration risk is high. | MCF-DEP-002 |
| Corroboration sample | % of external dependency records | 25 (minimum 5 records) | Illustrative; set per AIDCF-009 sampling rules. | MCF-DEP-002 |
| Thermal ride-through at declared rack load | seconds | Site-specific (no default) | Derived from THM analysis and test; liquid-cooled high-density racks can have very short ride-through, so it is never assumed. | MCF-DEP-003 |
| Maximum training work lost per interruption | minutes of cluster time | Equal to checkpoint interval (illustrative 30) | Illustrative; set from the Service Outcome tolerance in CAP. | MCF-DEP-003 |
| Maximum acceptable unresolved circular dependencies on critical functions | count | 0 | Illustrative; any unresolved cycle on a critical function defeats recovery planning. | MCF-DEP-004 |
| Upstream depth examined for shared source | levels | To grid supply point / carrier POP / fuel terminal | Illustrative; profile sets depth based on the declared external hazard set. | MCF-DEP-005 |
| Minimum physical separation for diverse routes | m | Site-specific (no default) | Set in capability profile with reference to fire-zone design and the separation guidance in the cabling standard adopted (for example ANSI/TIA-942 or EN 50600-2-4). | MCF-DEP-007 |
| Route inspection interval | months | 24 | Illustrative; shorter where third-party works or construction occur nearby. | MCF-DEP-007 |
| Minimum authorised persons per critical switching task available within response time | persons | 2 | Illustrative; reflects a two-person rule for HV switching common in safe systems of work; set from the site safety rules. | MCF-DEP-008 |
| Firm capacity margin over declared peak demand | % of declared peak | 10 | Illustrative; set in the capability profile from load growth uncertainty and utility terms. | MCF-DEP-009 |
| Minimum fuel resupply commitment under emergency | hours from call-off to delivery | Site-specific (no default) | Set from POW fuel autonomy (MCF-POW-007/008) so that autonomy exceeds the committed resupply time with margin. | MCF-DEP-009 |
| Power quality history reviewed | months | 12 | Illustrative; longer history improves estimate of event frequency. | MCF-DEP-009 |
| Minimum number of independent carriers for production connectivity | carriers | 2 | Illustrative; set by the connectivity Service Outcome. | MCF-DEP-010 |
| Carrier time-to-repair commitment | hours | 4 | Illustrative; compare against outcome tolerance. | MCF-DEP-010 |
| Support entitlement expiry warning | days before expiry | 180 | Illustrative; allows renewal or replacement before entitlement lapses. | MCF-DEP-011 |
| Maximum dependency of safety or continuity loops on cloud/SaaS services | count | 0 | Illustrative; profile may allow exceptions only with accountable acceptance. | MCF-DEP-012 |
| Maximum share of usable capability in one fault domain | % of usable capacity | Site-specific (no default) | Derived from the CAP-03 impact tolerance; there is no universal value. | MCF-DEP-013 |
| Maximum share of a critical asset class from one supplier | % of installed base | Site-specific (no default) | Set in capability profile; standardisation benefits must be weighed against common-mode exposure. | MCF-DEP-014 |
| Minimum independent holders per critical knowledge item | persons | 2 | Illustrative; external parties count only where contractually available within response time. | MCF-DEP-015 |
| Substitution validation interval | months | 24 | Illustrative; shorter for dependencies with high event frequency. | MCF-DEP-016 |
| Time-to-substitute margin | % of tolerance | 75 (demonstrated time no more than 75% of tolerance) | Illustrative; provides margin for real-event degradation. | MCF-DEP-016 |
| Per-tenant load-step limit | kW per second | Site-specific (no default) | Derived from POW-05 load-step response analysis. | MCF-DEP-019 |
| Interface deviation review interval | months | 1 | Illustrative. | MCF-DEP-020 |
| Dependency trend review interval | months | 3 | Illustrative. | MCF-DEP-021 |
| Provider review interval | months | 3 | Illustrative. | MCF-DEP-022 |
| Maximum time to update dependency graph after detected change | working days | 10 | Illustrative. | MCF-DEP-023 |
| Revalidation interval for material dependencies | months | 12 | Illustrative; shorter for high-churn dependencies (cloud services, carriers). | MCF-DEP-024 |

## 10 Evidence expectations by claim type

The DEP controls distribute across claim types as follows. Tier and sufficiency floor follow claim type (AIDCF-008 §32), raised to the gate floor where the control is CRITICAL.

| Claim type | AL | Profile tier | Controls in this domain | Sufficiency floors applied |
|---|---|---|---|---|
| DESIGN | AL2 | CP-1 | MCF-DEP-003, MCF-DEP-008, MCF-DEP-013, MCF-DEP-014, MCF-DEP-015 | S3 |
| IMPLEMENTATION | AL3 | CP-2 | MCF-DEP-001, MCF-DEP-002, MCF-DEP-004, MCF-DEP-005, MCF-DEP-006, MCF-DEP-007, MCF-DEP-009, MCF-DEP-010, MCF-DEP-011, MCF-DEP-012, MCF-DEP-017, MCF-DEP-018, MCF-DEP-019 | S3, S4 |
| OPERATION | AL4 | CP-3 | MCF-DEP-020, MCF-DEP-021, MCF-DEP-022, MCF-DEP-023, MCF-DEP-024 | S4 |
| EFFECTIVENESS | AL5 | CP-4 | MCF-DEP-016 | S4 |

**DESIGN claims** (for example MCF-DEP-003, MCF-DEP-008, MCF-DEP-013) rest on E1 analysis records and E7 derived analysis (dependency paths, concentration calculations) reviewed by a competent person who did not author them. A design claim does not establish that the dependency graph reflects the as-built facility.

**IMPLEMENTATION claims** (most of DEP-01 to DEP-03 and DEP-05) require E2 evidence reconciled to the as-built state: configuration exports showing which DNS, time, identity and licence endpoints are actually used; as-built single-line diagrams and P&IDs; carrier and utility documents identifying supply points and routes; and inspection of route convergence points. Provider attestations are acceptable only at reduced confidence (generally no higher than CONF-2) and with an UNKNOWN Record for what the provider would not disclose.

**OPERATION claims** (DEP-06 and MCF-DEP-020) require E3 evidence over the period stated in the control: boundary telemetry, indicator histories, provider-performance measurements computed from owner-side tickets, and graph version histories showing timely updates.

**EFFECTIVENESS claims** (MCF-DEP-016) require E4 evidence: a substitution exercise, test or documented precedent with measured time-to-substitute compared with tolerance.

Evidence that commonly fails the quality floor in this domain: dependency registers populated from design intent with no as-built check (F and C below floor); carrier "diversity" letters that do not name the underlying operator (R below floor); and graphs last revalidated before a major expansion (T below floor; mark STALE).

## 11 Assessment guidance

1. **Start from outcomes, not assets.** Obtain the Capability Instance, its Service Outcomes and Required Functions (CAP), then the asset-to-function map. Assessing the dependency register in isolation produces completeness without relevance.
2. **Reconcile, then analyse.** Reconcile the map and upstream graph to as-built evidence (MCF-DEP-001, MCF-DEP-002) before evaluating shared-source and route analyses; analysis on an unreconciled graph inherits its gaps.
3. **Search for absence.** The main DEP failure is a dependency that is not recorded. Use independent discovery: egress firewall and DNS logs to find cloud/SaaS services; controller configuration to find time and identity sources; walk-downs of risers and building entries; maintenance contracts to find shared contractors. Record the discovery method so that the negative claim ("no further material dependencies") is bounded (AIDCF-008 §29 negative/absence claim).
4. **Follow redundancy claims upstream.** For every redundancy claim used in POW, THM, NET or CMP, trace both legs to their first common node. If the trace stops at the boundary for lack of disclosure, the pair is treated as sharing a source for gate evaluation (MCF-DEP-005 unknown rule).
5. **Test recovery-state reasoning.** Ask "what does this need to start again?" for each system on a restoration path, and draw the RECOVERY-state graph. Circular dependencies are usually found this way, not in NORMAL-state diagrams.
6. **Use provider evidence correctly.** Contractual responsibility is not proof of capability (AIDCF-003 IOT-REQ-052). Provider statements support the existence and terms of a dependency; they do not support its performance unless accompanied by operational or test evidence.
7. **Record UNKNOWN precisely.** Each UNKNOWN Record shall name the dependency, the missing attribute (for example underlying carrier, supply point, controller failure behaviour), the reason (U1–U10), the potential consequence and the gate affected (AIDCF-008 EVM-REQ-035), and shall be classified US1–US5 using the SPEC table.

**DG-DEP-REQ-003** The assessor shall record, for each IMPLEMENTATION claim on MCF-DEP-001, MCF-DEP-002 and MCF-DEP-012, at least one independent discovery method used to search for unrecorded dependencies, and shall bound the resulting absence claim by that method's coverage.

**DG-DEP-REQ-004** The assessor shall not accept an INDEPENDENT_OF qualifier between two dependency paths unless the supporting evidence addresses the specific hazards for which independence is claimed (for example fire, flood, excavation, grid fault, software defect).

## 12 Testing safety

DEP assessment is predominantly documentary, analytical and observational. The following apply:

- Walk-downs of electrical rooms, risers, trenches and plant spaces follow site access, PPE and escort rules. Entry into trenches, manholes or other confined spaces requires a permit under MCF-OPS-007 and confined-space controls; opening of covers or enclosures requires a permit.
- Configuration extraction from BMS/EPMS, PLCs, CDU controllers and network devices uses read-only accounts and approved export methods, authorised by the control-system owner. No live query that could change controller state is permitted.
- No breaker, valve, isolator, circuit or service shall be operated, disconnected or failed over to verify independence or diversity under a DEP control. Such tests belong to the owning domain (POW, THM, NET, RES) and require method statement, permit, change approval and authorisation by the facility operator's authorised person.
- Substitution exercises under MCF-DEP-016 that involve temporary generation, temporary chillers, fuel transfer or electrical connection are hazardous-energy activities and require MCF-OPS-006, MCF-OPS-007 and MCF-OPS-018 controls.
- Blocking egress to cloud or SaaS services to test fallback (MCF-DEP-012) is permitted only within an approved RES-05 exercise with operators informed.

## 13 UNKNOWN hot-spots

The following attributes are frequently unavailable in this domain. Each should be anticipated in the evidence request plan.

| Hot-spot | Typical UNKNOWN type | Typical severity | Resolution route |
|---|---|---|---|
| Grid supply-point topology behind "dual feeds" | U2 Inaccessible / U10 Dependency unknown | US4 (affects CG-03 and a CG-05 criterion) | Network operator statement; connection agreement schedules |
| Firm vs non-firm capacity and curtailment terms | U2 / U10 | US4 | Connection agreement; utility offer letter (DESIGN only) |
| Underlying carrier and route for resold circuits | U10 | US4 where diversity-relied | Reseller disclosure; third-party path verification |
| Provider (colocation) generator, UPS and cooling evidence | U2 | US3–US4 depending on gate reliance | Evidence rights (MCF-SUP-006); provider audit reports |
| Controller failure behaviour (fail-last, fail-safe) | U8 / U1 | US4 where CG-05/06/07 rely on it | Configuration export; OEM documentation; owning-domain test |
| Cloud/SaaS failure behaviour on management paths | U10 | US4 | Configuration; RES-05 exercise |
| Recovery dependencies (licence, image, identity) | U10 / U5 | US3–US4 | Recovery dependency map; RES-05 exercise |
| Job placement relative to fault domains | U1 | US3 | Scheduler export reconciled to RES-02 labels |

## 14 Interfaces with other domains

| Domain | DEP provides | DEP receives |
|---|---|---|
| GOV | Accountable owners for dependencies; acceptance decisions for concentration | Decision rights and risk acceptance authority (GOV-01, GOV-02) |
| CAP | Dependency-aware boundary; time-to-impact | Capability Instance, outcomes, impact tolerance, growth forecast (CAP-01 to CAP-04) |
| PHY | Route convergence points | Fire, water and security zones (PHY-03); delivery and logistics access (PHY-01) |
| POW | Shared-source findings; utility dependency records | Utility capacity and contingency (POW-01); fuel replenishment (POW-02) |
| THM | Shared water and heat-rejection sources; CDU common controllers | Heat-rejection dependency and water continuity (THM-04) |
| ENV | Water and grid restriction dependencies | Water scarcity and heatwave readiness (ENV-03, ENV-06) |
| CMP, STO, NET | Timing, identity, licence and repository dependencies; concentration analysis | Topology, fault-domain design and core services (CMP-02, STO-05, NET-06) |
| OPS | Dependency graph for change impact; shared human dependencies | Change records (OPS-05) for change detection; staffing (OPS-01) |
| RES | Shared-element facts; recovery dependency map; substitution plans | Fault-domain model (RES-02); recovery sequences (RES-04); exercises (RES-05) |
| SUP | OEM and provider dependency records | Sub-tier visibility, contract terms, evidence rights (SUP-01, SUP-02) |
| SEC | Cloud/SaaS and identity dependency register | Control-plane security and break-glass (SEC-01, SEC-02) |
| EVA | UNKNOWN Records; boundary statement | Scope and criteria, UNKNOWN preservation, evidence expiry (EVA-03, EVA-04, EVA-06) |

## 15 Informative references

Document-level references; no clause-level reliance is implied.

- ISO/IEC/IEEE 15026-2 (systems and software assurance: assurance case)
- ISO/IEC/IEEE 42010 (architecture description)
- ISO 22301 (business continuity management systems); ISO 22317 (business impact analysis); ISO 22318 (supply chain continuity)
- ISO/IEC 27031 (ICT readiness for business continuity)
- ISO 31000 (risk management)
- ISO 55001 (asset management systems); ISO/IEC 19770-1 (IT asset management)
- IEC 60812 (FMEA); IEC 61025 (fault tree analysis); IEC 61078 (reliability block diagrams)
- IEC 61508-6 (guidance on common cause failure); NUREG/CR-5485 (common-cause failure modelling)
- ANSI/TIA-942 (telecommunications infrastructure standard for data centres); EN 50600 series (data centre facilities and infrastructures), in particular EN 50600-2-2, EN 50600-2-4 and EN 50600-3-1
- EN 50160 (voltage characteristics of public distribution networks); IEC 61000-4-30 (power quality measurement); IEEE 1159 (power quality monitoring)
- NFPA 110 (emergency and standby power systems)
- ISO/IEC 22123-1 (cloud computing vocabulary); ISO/IEC 19086-1 (cloud SLA framework); ISO/IEC 27017 (cloud services security); CSA Cloud Controls Matrix
- NIST SP 800-161r1 (cyber supply chain risk management); NIST SP 800-34 (contingency planning)
- Regulation (EU) 2022/2554 (DORA) — informative for financial-sector users on ICT concentration and third-party reliance
- AIDCF-003, AIDCF-004, AIDCF-008, AIDCF-010, AIDCF-013, AIDCF-014

## 16 Control summary

| Control | Title | Type | AL | Claim type | Gate mappings |
|---|---|---|---|---|---|
| MCF-DEP-001 | Asset-to-Function Mapping | PREVENTIVE | AL3 | IMPLEMENTATION | CG-03 (C); CG-02 (S) |
| MCF-DEP-002 | Upstream Dependency Mapping | PREVENTIVE | AL3 | IMPLEMENTATION | CG-03 (C); CG-15 (S) |
| MCF-DEP-003 | Downstream Consequence Mapping | DIRECTIVE | AL2 | DESIGN | CG-03 (S); CG-09 (S) |
| MCF-DEP-004 | Recovery Dependency Mapping | RECOVERY | AL3 | IMPLEMENTATION | CG-03 (S); CG-10 (S) |
| MCF-DEP-005 | Shared Source Analysis | PREVENTIVE | AL3 | IMPLEMENTATION | CG-03 (C); CG-05 (S); CG-06 (S); CG-09 (S) |
| MCF-DEP-006 | Common Controller Analysis | PREVENTIVE | AL3 | IMPLEMENTATION | CG-03 (S); CG-07 (S); CG-09 (S) |
| MCF-DEP-007 | Shared Route Analysis | PREVENTIVE | AL3 | IMPLEMENTATION | CG-03 (C); CG-09 (S) |
| MCF-DEP-008 | Shared Human Dependency Analysis | PREVENTIVE | AL2 | DESIGN | CG-03 (S); CG-13 (S) |
| MCF-DEP-009 | Utility Dependency | PREVENTIVE | AL3 | IMPLEMENTATION | CG-03 (C); CG-05 (S) |
| MCF-DEP-010 | Telecom Dependency | PREVENTIVE | AL3 | IMPLEMENTATION | CG-03 (C); CG-10 (S) |
| MCF-DEP-011 | OEM Dependency | PREVENTIVE | AL3 | IMPLEMENTATION | CG-03 (S); CG-10 (S) |
| MCF-DEP-012 | Cloud and Service Dependency | PREVENTIVE | AL3 | IMPLEMENTATION | CG-03 (C); CG-15 (S); CG-10 (S) |
| MCF-DEP-013 | Capacity Concentration | DIRECTIVE | AL2 | DESIGN | CG-03 (S); CG-09 (S) |
| MCF-DEP-014 | Supplier Concentration | DIRECTIVE | AL2 | DESIGN | CG-03 (S) |
| MCF-DEP-015 | Knowledge Concentration | PREVENTIVE | AL2 | DESIGN | CG-13 (S); CG-10 (S) |
| MCF-DEP-016 | Substitution Readiness | RECOVERY | AL5 | EFFECTIVENESS | CG-10 (S); CG-03 (S) |
| MCF-DEP-017 | Assessment Boundary | DIRECTIVE | AL3 | IMPLEMENTATION | CG-02 (C); CG-03 (C) |
| MCF-DEP-018 | Provider Boundary | DIRECTIVE | AL3 | IMPLEMENTATION | CG-13 (C); CG-03 (S) |
| MCF-DEP-019 | Tenant Boundary | PREVENTIVE | AL3 | IMPLEMENTATION | CG-09 (S); CG-13 (S) |
| MCF-DEP-020 | Cross-Boundary Enforcement | DETECTIVE | AL4 | OPERATION | CG-09 (S); CG-15 (S) |
| MCF-DEP-021 | Dependency Health Indicators | DETECTIVE | AL4 | OPERATION | CG-03 (S) |
| MCF-DEP-022 | Provider Performance | DETECTIVE | AL4 | OPERATION | CG-13 (S) |
| MCF-DEP-023 | Change Detection | DETECTIVE | AL4 | OPERATION | CG-14 (S); CG-03 (S) |
| MCF-DEP-024 | Periodic Revalidation | DETECTIVE | AL4 | OPERATION | CG-03 (S) |

Key: (C) = CRITICAL role, (S) = SUPPORTING role, per AIDCF-010 gate roll-up. CG-11 and CG-12 are evaluated across all controls and are not mapped per control.

## 17 Worked synthetic example

> **Synthetic example.** All names, values and results below are invented for illustration. They do not describe any real facility, provider or assessment.

**Decision question.** Can synthetic Capability Instance CI-SYN-TRN-01 (a liquid-cooled training cluster in a colocation hall, operated by a tenant) achieve its availability outcome (cluster available for scheduled training with interruption no longer than the declared tolerance) under NORMAL, MAINTENANCE and EMERGENCY states, as of the assessment date?

**Boundary (MCF-DEP-017).** The boundary includes the tenant's racks, CDUs, fabric and storage, and records as crossing dependencies the colocation provider's utility supply, generators, UPS, facility water and carrier meet-me room, plus a cloud identity provider and a SaaS cluster-scheduling service. The boundary statement was approved and reconciled to the dependency graph. Result: CONFORMING (IMPLEMENTATION, S4).

**Dependency discovery (MCF-DEP-001, MCF-DEP-002).** Asset-to-function reconciliation sampled 10 racks and 6 CDUs; one CDU found in the field was not in the map (it had been added during an expansion). The map was updated during fieldwork, but the reconciliation record showed it had not been re-validated after the expansion change. Upstream tracing via DNS and egress logs found an OEM licence server used by the fabric management software that was not in the graph. Results: MCF-DEP-001 PARTIAL (Finding: map not re-validated after change); MCF-DEP-002 PARTIAL (Finding: unrecorded licence dependency).

**Shared source (MCF-DEP-005).** The provider's documentation described "two independent utility feeds". The network operator's connection documentation, obtained through the provider under MCF-SUP-006 rights, showed both feeds originate from one grid substation on different transformers. Independence holds for a transformer fault but not for a substation event. The provider had not recorded this. Result: NONCONFORMING for the independence claim as stated; Finding raised; the shared substation recorded as SHARES_FAULT_DOMAIN_WITH and passed to RES-02 and POW-01.

**Shared route (MCF-DEP-007).** Two carriers serve the hall. One carrier's route documentation was provided; the other, a reseller, would not name its underlying operator. Result: UNKNOWN; UNKNOWN Record raised (U10, US4 because the circuits support a connectivity outcome under CG-03).

**Cloud and service (MCF-DEP-012).** The register listed both cloud services. Configuration showed BMS and CDU control loops are local; operator log-in to cluster management depends on the cloud identity provider with a tested local break-glass account. Result: CONFORMING.

**Gate result.** CG-03 has CRITICAL controls MCF-DEP-001, -002, -005, -007, -009, -010, -012 and -017 in scope, plus MCF-SUP-004 (assessed CONFORMING in this example). With PARTIAL on MCF-DEP-001 and MCF-DEP-002 and NONCONFORMING on MCF-DEP-005, the roll-up rule gives **CG-03 = FAIL** (a FAIL condition takes precedence over the UNKNOWN on MCF-DEP-007). CG-02 has MCF-DEP-017 CONFORMING and is evaluated with the other CG-02 CRITICAL controls in CAP and PHY.

**Decision effect.** A FAIL on CG-03 prevents a REASONABLY_ASSURED decision; the applicable ceiling is the one defined for CG-03 in AIDCF-010. The US4 UNKNOWN on the reseller route is recorded in the UNKNOWN register and evaluated under CG-12. Actions: provider to declare the shared substation in its resilience statement and the tenant to reflect it in the availability claim; tenant to obtain underlying-carrier disclosure or replace the circuit; dependency graph re-validation added to the expansion change template (MCF-DEP-023). Reassessment triggers: closure of the three Findings and resolution of the UNKNOWN Record.

**What the example shows.** The redundancy claims evaluated in POW and NET looked sound in isolation; only the DEP analysis exposed that the utility redundancy did not cover a substation event and that carrier diversity was unverified. The decision changes because of facts no single engineering domain would have surfaced on its own.
