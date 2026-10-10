# AIDCF-018-SUP Supply Chain, OEM and Ecosystem Assurance Domain Guide

## Document control

| Field | Value |
|---|---|
| Document ID | AIDCF-018-SUP |
| Title | Supply Chain, OEM and Ecosystem Assurance Domain Guide |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Parent artifact | AIDCF-018 Domain Guides |
| Normative basis | AIDCF-007A (controls MCF-SUP-001 to MCF-SUP-024), AIDCF-008, AIDCF-010 |
| Requirement prefix | DG-SUP-REQ-NNN |

### Revision history

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-10 | First issue of the SUP domain guide, aligned with the rewritten SUP controls in AIDCF-007A and the per-control gate mapping rule. |

### Status of this guide

This guide explains how to apply the 24 SUP controls of AIDCF-007A. The control records are normative and are held in the AIDCF-007A registry; where this guide and a control record differ, the control record governs and the difference shall be raised as a baseline issue. Requirements numbered DG-SUP-REQ-NNN are normative for assessments that claim conformance to AIDCF-018-SUP. Other text is informative.

## 1 Purpose and scope

### 1.1 Purpose

The SUP domain establishes whether the organisations, products, firmware, spares, logistics and remote-support arrangements on which the AI Capability Instance depends are trustworthy, contractually secured, traceable and recoverable. Where DEP asks "what do we depend on?", SUP asks "can we rely on the parties and products we depend on, and can we get what we need from them when it matters?".

### 1.2 In scope

- Supplier due diligence: technical capability, financial and operational resilience, security and quality posture, sub-tier visibility (SUP-01).
- Contract and service obligations: service levels, evidence rights, incident and vulnerability notification, exit and transition rights (SUP-02).
- Hardware and component provenance: approved sourcing, counterfeit prevention, chain of custody, component traceability (SUP-03).
- Software, firmware and update supply: release provenance, signature validation, compatibility assurance and staged rollout, vulnerability response (SUP-04).
- Spares, logistics and obsolescence: critical spares, long-lead equipment lead times, logistics and specialist-labour continuity, end-of-life planning (SUP-05).
- Remote support and third-party access: named identities, activation and approval, session monitoring, revocation and review (SUP-06).

The supply base in scope includes accelerator and rack-scale system OEMs and integrators; NIC/DPU, switch and optics suppliers; storage OEMs; MV/LV switchgear, transformer, UPS, battery, generator and fuel suppliers; chiller, dry cooler, cooling tower, CDU and pump suppliers; BMS/EPMS and controls integrators; maintenance contractors; logistics providers; and managed-service and remote-support providers.

### 1.3 Out of scope

- Identifying that a dependency on a supplier or provider exists, and analysing its concentration (DEP-03, DEP-04).
- Platform security baselines, vulnerability management and patching of the owner's own systems (SEC-04), and the owner's own privileged access model (SEC-01). SUP covers the supplier side of these.
- Physical delivery, equipment movement and media custody within the site (PHY-05).
- Node rebuild, spares and RMA handling as part of compute operations (CMP-06); SUP sets the supply strategy that CMP-06 executes.

### 1.4 Boundaries with other domains

| Topic | SUP role | Other domain role |
|---|---|---|
| OEM dependency | Assures the supplier and contract (SUP-01, SUP-02) | DEP-03 records the dependency (MCF-DEP-011) |
| Supplier concentration | Provides sub-tier facts (MCF-SUP-004) | DEP-04 analyses concentration (MCF-DEP-014) |
| Firmware | Assures supply, provenance, signature and rollout (SUP-04) | CMP-04 assures the compute firmware baseline and upgrade testing; SEC-04 assures secure baseline and patching |
| Remote access | Assures third-party identity and session lifecycle (SUP-06) | SEC-01/SEC-03 assure identity, privileged and remote access architecture |
| Spares | Sets spares and lead-time strategy (SUP-05) | CMP-06 executes compute spares and RMA; POW/THM restoration uses spares |
| Delivery | Assures chain of custody up to receipt (MCF-SUP-011) | PHY-05 assures delivery controls and movement on site |

## 2 Why this domain matters for AI capability

AI infrastructure is built from a small number of highly specialised products made by a small number of suppliers, many of them supply-constrained. Accelerators, high-bandwidth memory, advanced packaging and high-speed optics are allocated rather than freely available; power transformers, MV switchgear, large generators, chillers and CDUs have long and variable manufacturing lead times; specialist labour for HV jointing, commissioning and liquid-cooling work is scarce in many regions. A failure that would be routine in a general-purpose facility (replace the part from stock) can become a long outage when the part is a long-lead item with no strategic spare.

The software supply chain is as material as the hardware. Accelerators, BMCs, NICs/DPUs, switches, storage controllers, UPS, PDUs, CDU controllers and PLCs all run vendor firmware that is updated over the life of the facility. A defective or malicious release, rolled out across all redundant members at once, is a common-mode failure (AIDCF-004 scenario X08) that no amount of physical redundancy prevents. Vendor remote access, often needed for diagnosis of proprietary systems, gives third parties consequential authority over facility and AI infrastructure and is directly relevant to CG-15.

Finally, supplier contracts determine what evidence the owner can obtain. Where a colocation provider, OEM or integrator will not disclose test records, sub-tier sources or firmware component inventories, the owner cannot reach the evidence floors for dependent controls in other domains, and the result is UNKNOWN rather than CONFORMING.

## 3 Reference patterns and variants

| Pattern (AIDCF-013) | Dominant SUP concerns | Controls most exercised |
|---|---|---|
| Single-site training facility | Long-lead spares for site-unique electrical and cooling plant; accelerator RMA turnaround | MCF-SUP-017, MCF-SUP-018, MCF-SUP-005 |
| Hyperscale campus | Standardised fleets with shared firmware lineage; framework agreements and slot reservations | MCF-SUP-015, MCF-SUP-018, MCF-SUP-004 |
| Colocation deployment | Evidence rights against the provider; provider's maintenance contractors | MCF-SUP-006, MCF-SUP-005, MCF-SUP-021 |
| Liquid-cooled high-density cluster | CDU and cold-plate OEM support; coolant supply; proprietary control logic | MCF-SUP-008, MCF-SUP-013, MCF-SUP-017 |
| Sovereign AI environment | Supplier jurisdiction, export controls, sub-tier disclosure, support personnel clearance | MCF-SUP-002, MCF-SUP-004, MCF-SUP-021 |
| Edge inference estate | Many sites with remote vendor support; logistics to dispersed sites | MCF-SUP-019, MCF-SUP-022 |
| Brownfield retrofit | Obsolete controllers and UPS models; broker-sourced parts | MCF-SUP-020, MCF-SUP-009, MCF-SUP-010 |
| Modular facility | Integrator-built skids with embedded controls; factory acceptance testing | MCF-SUP-001, MCF-SUP-013, MCF-SUP-011 |

**Variants.** In an *integrator-delivered* model (rack-scale or skid-level systems assembled and tested by an integrator), SUP-01 and SUP-03 controls are applied to the integrator and, through sub-tier visibility, to the OEMs behind it. In a *managed-service* model, SUP-06 applies to the managed-service provider's staff as third parties even when they are permanently on site.

## 4 Required functions and capability linkage

| Required Function (assurance view) | Linked Service Outcomes | Controls |
|---|---|---|
| Supplier fitness: critical suppliers can deliver, support and survive | Availability, growth and recovery outcomes | MCF-SUP-001 to MCF-SUP-004 |
| Contractual reliance: obligations, evidence, notification and exit are secured | All outcomes (through evidence and support) | MCF-SUP-005 to MCF-SUP-008 |
| Hardware integrity: installed components are genuine, untampered and traceable | Integrity, availability and life-safety outcomes | MCF-SUP-009 to MCF-SUP-012 |
| Firmware and software integrity: updates are authentic, compatible and safely deployed | Integrity and availability outcomes | MCF-SUP-013 to MCF-SUP-016 |
| Restoration supply: spares, long-lead equipment, logistics and labour are available within tolerance | Recovery outcomes | MCF-SUP-017 to MCF-SUP-020 |
| Bounded third-party authority: vendor access is identified, approved, monitored and revoked | Integrity and availability outcomes; CG-15 | MCF-SUP-021 to MCF-SUP-024 |

In the AIDCF-014 graph, a supplier or provider appears as the provider end of a Dependency (DEPENDS_ON from the consuming system or function). Contract evidence attaches through HAS_EVIDENCE_REQUIREMENT and EVIDENCED_BY; firmware releases attach to AssetInstances; and third-party access paths are Interfaces CONTROLLED_BY the owner's access gateway.

## 5 Dependencies, fault domains and common-mode concerns

| Common mode | How it arises | Control |
|---|---|---|
| Single firmware lineage across redundant members | Standardisation plus a single rollout pipeline | MCF-SUP-015 (fault-domain-aligned waves; redundant members never in one wave) |
| Shared sub-tier source behind "diverse" suppliers | Two UPS brands with one battery-cell maker; two optics vendors with one laser source | MCF-SUP-004 |
| One integrator or contractor across systems | Same contractor maintains all generators or both UPS systems | MCF-SUP-001; DEP-02 shared human dependency |
| One logistics route or port for heavy equipment | Transformers and generators delivered through one route or crossing | MCF-SUP-019 |
| One vendor remote-access path to many sites | A vendor's support platform with standing access to the estate | MCF-SUP-022 |
| One spares location | All strategic spares in the same building as the equipment they protect | MCF-SUP-017 |

The human/operational and external fault-domain categories of AIDCF-003 §43 ("team, shift, procedure, supplier or authority concentration"; "utility, carrier, water source, fuel supply, vendor or geographic region") are where SUP findings are recorded.

**DG-SUP-REQ-001** The assessor shall confirm that each firmware rollout sampled under MCF-SUP-015 was planned against the RES-02 fault-domain model current at the time of the rollout, and shall record as a Finding any wave that included more than one member of a redundant group.

## 6 Threats, hazards and failure scenarios with propagation paths

| Scenario | Initiating condition | Propagation path to Service Outcome | SUP controls that interrupt the path |
|---|---|---|---|
| X08 Firmware rollout common-mode failure | Defective NIC or switch firmware release | Deployed to all spine switches in one change → fabric partition → collective operations fail → training jobs fail across the cluster | MCF-SUP-015 staged waves; MCF-SUP-014 signature validation; MCF-SUP-013 provenance |
| X12 Long-lead spare after rare failure | Internal fault in a site transformer or MV switchgear section | No strategic spare → replacement lead time far exceeds tolerance → prolonged operation at reduced redundancy or reduced capacity → availability and growth outcomes missed | MCF-SUP-017, MCF-SUP-018, MCF-SUP-019 |
| X18 Loss of remote OEM support | OEM support platform unavailable, or supplier withdraws support | Diagnosis of a proprietary storage or fabric fault delayed → recovery beyond tolerance | MCF-SUP-005, MCF-SUP-008, MCF-SUP-020 |
| Supply-chain compromise (AIDCF-004 threat event) | Modified BMC firmware or tampered network device introduced in transit | Persistent foothold on management plane → manipulation of power capping or cooling setpoints | MCF-SUP-011, MCF-SUP-014, MCF-SUP-010 |
| Counterfeit protection device | Counterfeit MCCB or relay installed | Fails to clear a fault → arc-flash hazard and wider outage than the protection study assumed | MCF-SUP-009, MCF-SUP-010 (CG-04 SUPPORTING) |
| Vendor access abuse or compromise | Standing shared vendor account on CDU controllers | Unauthorised setpoint change across loops → thermal excursion | MCF-SUP-021, MCF-SUP-022, MCF-SUP-023 |
| Supplier distress or export restriction | Supplier insolvency, plant outage or export-control change | Accelerator deliveries or spares stop → expansion stalls; RMA backlog grows | MCF-SUP-002, MCF-SUP-004, MCF-SUP-018 |

## 7 Safeguards

| Safeguard | Function | Controls |
|---|---|---|
| Pre-award capability and posture assessment | Prevents reliance on suppliers unable to deliver or support | MCF-SUP-001, MCF-SUP-003 |
| Supplier monitoring | Detects distress, allocation and export exposure early | MCF-SUP-002 |
| Measurable service levels tied to tolerances | Aligns support with time-to-impact | MCF-SUP-005 |
| Evidence rights | Makes supplier-held evidence obtainable | MCF-SUP-006 |
| Approved sourcing, receipt inspection and custody | Excludes counterfeit and tampered parts | MCF-SUP-009 to MCF-SUP-011 |
| Serial-level traceability | Scopes recalls and advisories quickly | MCF-SUP-012 |
| Controlled release repository and signature enforcement | Excludes unauthentic firmware | MCF-SUP-013, MCF-SUP-014 |
| Compatibility matrix and fault-domain-aligned rollout | Contains defective releases | MCF-SUP-015 |
| Strategic spares, lead-time tracking and logistics pre-arrangements | Bounds restoration time | MCF-SUP-017 to MCF-SUP-019 |
| Named, off-by-default, brokered and recorded vendor access | Bounds third-party authority | MCF-SUP-021 to MCF-SUP-024 |

## 8 Critical-gate linkage

SUP holds three CRITICAL mappings: MCF-SUP-004 for CG-03, and MCF-SUP-021 and MCF-SUP-022 for CG-15. All other mappings are SUPPORTING; SUP findings frequently drive gate-level evaluation of CG-08, CG-10, CG-14 and CG-15 and supporting evaluation of CG-04 (counterfeit protection devices) and CG-05/CG-06 (spares and logistics).

| Gate | Gate name | CRITICAL controls in this domain | SUPPORTING controls in this domain |
|---|---|---|---|
| CG-03 | Critical dependency visibility | MCF-SUP-004 | MCF-SUP-001, MCF-SUP-002, MCF-SUP-006, MCF-SUP-007, MCF-SUP-012, MCF-SUP-018, MCF-SUP-020 |
| CG-04 | Life safety and hazardous energy | none | MCF-SUP-009, MCF-SUP-010 |
| CG-05 | Resilient electrical supply | none | MCF-SUP-017, MCF-SUP-019 |
| CG-06 | Thermal continuity | none | MCF-SUP-017 |
| CG-08 | Compute, storage and network functional integrity | none | MCF-SUP-003, MCF-SUP-009, MCF-SUP-010, MCF-SUP-011, MCF-SUP-012, MCF-SUP-014, MCF-SUP-015 |
| CG-09 | Failure containment | none | MCF-SUP-015 |
| CG-10 | Recovery readiness | none | MCF-SUP-005, MCF-SUP-008, MCF-SUP-017, MCF-SUP-018, MCF-SUP-019 |
| CG-13 | Responsibility and authority | none | MCF-SUP-005, MCF-SUP-021, MCF-SUP-024 |
| CG-14 | Change control | none | MCF-SUP-013, MCF-SUP-015, MCF-SUP-022 |
| CG-15 | Integrated digital authority over infrastructure | MCF-SUP-021, MCF-SUP-022 | MCF-SUP-003, MCF-SUP-007, MCF-SUP-013, MCF-SUP-014, MCF-SUP-016, MCF-SUP-023, MCF-SUP-024 |

CRITICAL controls in this domain:

- **MCF-SUP-004 Sub-Tier Visibility** — CRITICAL for CG-03; claim type IMPLEMENTATION at AL3, sufficiency floor S4.
- **MCF-SUP-021 Support Identity** — CRITICAL for CG-15; claim type IMPLEMENTATION at AL3, sufficiency floor S4.
- **MCF-SUP-022 Activation and Approval** — CRITICAL for CG-15; claim type OPERATION at AL4, sufficiency floor S4.

**Rationale for the CRITICAL choices.** Sub-tier visibility (MCF-SUP-004) is CRITICAL for CG-03 because a shared sub-tier source behind nominally diverse suppliers is a material dependency that is invisible without it. Support identity and activation (MCF-SUP-021, MCF-SUP-022) are CRITICAL for CG-15 because standing or shared vendor access to BMS/EPMS, CDU, BMC or cluster-management interfaces directly defeats the bound on digital authority that CG-15 protects. Spares and logistics controls are SUPPORTING for CG-10 rather than CRITICAL because the CG-10 CRITICAL controls in POW, THM, CMP, STO, NET and RES evaluate restoration end-to-end; a spares shortfall is assessed through them.

**DG-SUP-REQ-002** Where MCF-SUP-021 or MCF-SUP-022 is assessed, the assessor shall include facility control systems (BMS, EPMS, CDU controllers, UPS and switchgear management interfaces) in the sample population alongside IT management interfaces, and shall not record CONFORMING on a sample drawn from IT systems alone.

## 9 Capability-profile parameters

All defaults are illustrative and shall be replaced in the capability profile with site-specific values and their basis.

| Parameter | Unit | Illustrative default | Basis | Control |
|---|---|---|---|---|
| Supplier monitoring interval | months | 6 | Illustrative; quarterly for sole-source suppliers. | MCF-SUP-002 |
| Sub-tier depth for critical classes | tiers | 2 | Illustrative; deeper where single-source components are known. | MCF-SUP-004 |
| Maximum on-site attendance time for critical electrical/mechanical faults | hours | 4 | Illustrative; set from DEP-003 time-to-impact and spares held. | MCF-SUP-005 |
| Evidence delivery time on request | working days | 10 | Illustrative. | MCF-SUP-006 |
| Notification intake test interval | months | 6 | Illustrative. | MCF-SUP-007 |
| Minimum transition assistance period | months | 12 | Illustrative. | MCF-SUP-008 |
| Serial verification coverage for safety-critical protection devices | % of units received | 100 | Illustrative. | MCF-SUP-010 |
| Target time to identify all affected units | hours | 24 | Illustrative. | MCF-SUP-012 |
| Traceability exercise interval | months | 12 | Illustrative. | MCF-SUP-012 |
| Maximum share of a redundant group updated per wave | % of group | 50 (and never all members) | Illustrative. | MCF-SUP-015 |
| Soak time between waves | hours | 24 | Illustrative. | MCF-SUP-015 |
| Remediation target for critical, exposed vulnerabilities | days | 14 | Illustrative; OT may require longer with compensating controls. | MCF-SUP-016 |
| Spares stock review interval | months | 6 | Illustrative. | MCF-SUP-017 |
| Spare-to-installed ratio for accelerator trays | % of installed | Site-specific (no default) | Derived from observed failure rates, RMA turnaround and the compute availability outcome. | MCF-SUP-017 |
| Lead-time refresh interval | months | 6 | Illustrative; lead times for electrical equipment can change materially within a year. | MCF-SUP-018 |
| Logistics continuity validation interval | months | 24 | Illustrative. | MCF-SUP-019 |
| Obsolescence planning horizon | months | 24 | Illustrative. | MCF-SUP-020 |
| Maximum default session duration | hours | 4 | Illustrative. | MCF-SUP-022 |
| Emergency activation review time | hours | 24 | Illustrative. | MCF-SUP-022 |
| Session recording retention | days | 90 | Illustrative. | MCF-SUP-023 |
| Maximum revocation time after notification | hours | 24 | Illustrative. | MCF-SUP-024 |
| Recertification interval | months | 3 | Illustrative. | MCF-SUP-024 |

## 10 Evidence expectations by claim type

| Claim type | AL | Profile tier | Controls in this domain | Sufficiency floors applied |
|---|---|---|---|---|
| DESIGN | AL2 | CP-1 | MCF-SUP-001, MCF-SUP-008, MCF-SUP-018 | S3 |
| IMPLEMENTATION | AL3 | CP-2 | MCF-SUP-003, MCF-SUP-004, MCF-SUP-005, MCF-SUP-006, MCF-SUP-009, MCF-SUP-013, MCF-SUP-021 | S3, S4 |
| OPERATION | AL4 | CP-3 | MCF-SUP-002, MCF-SUP-007, MCF-SUP-010, MCF-SUP-011, MCF-SUP-016, MCF-SUP-017, MCF-SUP-020, MCF-SUP-022, MCF-SUP-023, MCF-SUP-024 | S4 |
| EFFECTIVENESS | AL5 | CP-4 | MCF-SUP-012, MCF-SUP-014, MCF-SUP-015 | S4 |
| RESILIENCE | AL5 | CP-5 | MCF-SUP-019 | S5 |

**DESIGN claims** (MCF-SUP-001, MCF-SUP-008, MCF-SUP-018) rest on E1 records (capability assessments, contract clauses, lead-time registers) and analysis, approved by a competent engineer outside the procurement line. They do not show that the supplier performs.

**IMPLEMENTATION claims** (for example MCF-SUP-004, MCF-SUP-005, MCF-SUP-009, MCF-SUP-013, MCF-SUP-021) require E2 technical-state evidence: purchasing-system configuration, repository inventories reconciled to device-reported versions, and account exports from the systems themselves. A supplier's statement that it uses named accounts is not evidence of the as-configured state.

**OPERATION claims** (for example MCF-SUP-010, MCF-SUP-016, MCF-SUP-017, MCF-SUP-022 to MCF-SUP-024) require E3 evidence over the period: receipt inspection records, advisory logs, stock reconciliations, gateway session logs and recertification records. The assessor should compute from raw records (session start/end, approval timestamps) rather than rely on summary reports.

**EFFECTIVENESS claims** (MCF-SUP-012, MCF-SUP-014, MCF-SUP-015) require E4 evidence: a traceability exercise against a defined notice, a rejection test of an unsigned image on non-production equipment, and pre-production compatibility tests with health-gated rollout records.

**RESILIENCE claims** (MCF-SUP-019) require scenario evidence that logistics and labour can be mobilised within tolerance under a regional-disruption assumption, with cross-domain dependency coverage.

E5 evidence is common in this domain (certificates, audit reports, supplier attestations). AIDCF-008 requires it to be evaluated for scope, method, age, exclusions and transferability; a quality certificate does not cover firmware security, and a supplier's SOC-type report covers only the systems in its stated scope.

## 11 Assessment guidance

1. **Build the critical-supplier list from DEP.** Use the OEM dependency register (MCF-DEP-011) and supplier concentration analysis (MCF-DEP-014) to select suppliers. Do not sample suppliers by spend.
2. **Read the contract against the control evidence profiles.** For each critical supplier, check whether the contract gives access to the mandatory evidence items of the controls the supplier affects in POW, THM, CMP, STO, NET and RES. Gaps here explain later UNKNOWN results.
3. **Reconcile firmware from the device side.** Pull versions from the devices (Redfish/BMC inventory, switch OS show commands, UPS and CDU controller interfaces, PLC project versions) using read-only methods and reconcile to the repository, not the other way round.
4. **Walk a rollout.** Pick a recent fleet-wide update and reconstruct the waves from deployment records; check them against the fault-domain model and against the redundant-group membership.
5. **Count the spares.** Physical count of a sample of critical spares, with condition check (battery float charge records, storage conditions, firmware level of spare boards), is the only reliable evidence that spares exist and are usable.
6. **Follow a vendor session end to end.** From ticket to approval to activation to recording to deactivation; then check that the vendor account was recertified at the last review.
7. **Treat refusal as data.** A supplier's refusal to disclose sub-tier sources, SBOMs or test records is recorded as an UNKNOWN Record against the affected controls, with the supplier named, and not as NOT_APPLICABLE.

**DG-SUP-REQ-003** The assessor shall reconcile deployed firmware and software versions from device-reported data for a sample of each in-scope device class, including at least one facility controller class, when assessing MCF-SUP-013.

**DG-SUP-REQ-004** The assessor shall record supplier refusal of evidence required by a control's mandatory items as an UNKNOWN Record of type U2 against each affected control, and shall not substitute a supplier attestation for the mandatory item without recording the confidence ceiling applied.

## 12 Testing safety

- Signature rejection tests (MCF-SUP-014) are performed only on non-production devices isolated from production management networks. Flashing production devices to test signature enforcement is prohibited.
- Counterfeit testing of protection devices (MCF-SUP-010) is performed on a test bench by competent persons; no device in a live switchboard is tested under this control.
- Account and session reviews (MCF-SUP-021 to MCF-SUP-024) use read-only exports; assessors shall not attempt log-in with vendor or default credentials against production controllers, and shall not revoke access.
- Session termination tests (MCF-SUP-023) use a test session on non-production systems.
- Logistics exercises (MCF-SUP-019) are tabletop or walkthrough; any physical mobilisation trial involving cranes or heavy haulage requires a lift plan and permit under site rules.
- Notification-intake tests (MCF-SUP-007) use clearly marked synthetic notifications agreed with the supplier.

## 13 UNKNOWN hot-spots

| Hot-spot | Typical UNKNOWN type | Typical severity | Resolution route |
|---|---|---|---|
| Sub-tier sources for accelerators, optics, transformers, batteries | U2 / U10 | US4 (CG-03 CRITICAL) | Supplier disclosure under NDA; industry mapping; teardown evidence |
| Firmware SBOM and build provenance for facility controllers | U1 / U6 | US3 | Evidence rights; OEM release records |
| Account state on facility controllers that cannot export users | U2 | US4 where CG-15 relies on it | Configuration backup review; OEM tool export |
| Real stock and condition of OEM-held or regional spares | U2 | US3 | Vendor-managed inventory visibility; audit rights |
| Transformer and switchgear lead times | U1 / U3 | US3 | Current quotations; slot reservations |
| Supplier business continuity arrangements | U2 | US3 | Supplier BCP summary; audit |
| Provider maintenance-contractor competence in colocation | U2 | US3 | Provider evidence rights; witness |

## 14 Interfaces with other domains

| Domain | SUP provides | SUP receives |
|---|---|---|
| GOV | Supplier risk acceptance requests | Risk acceptance authority; policy (GOV-02, GOV-03) |
| CAP | Lead times vs growth schedule | Growth forecast (CAP-04) |
| DEP | Sub-tier facts; supplier posture | OEM dependency register; concentration analysis (DEP-03, DEP-04) |
| PHY | Custody to receipt | Delivery and movement controls on site (PHY-05) |
| POW, THM | Spares and lead-time strategy for electrical and cooling plant | Restoration requirements; maintenance plans |
| CMP, STO, NET | Firmware supply, compatibility and staged rollout | Firmware baselines and upgrade testing (CMP-04, NET-06) |
| OPS | Supplier service levels; vendor access approvals tied to tickets | Change and work control (OPS-02, OPS-05) |
| RES | Logistics and labour arrangements | Recovery scenarios and exercises (RES-03 to RES-05) |
| SEC | Third-party identity lifecycle; supplier advisories | Identity architecture, remote access, vulnerability management (SEC-01, SEC-03, SEC-04) |
| EVA | Evidence-rights mapping; supplier UNKNOWN Records | Evidence ownership and custody (EVA-01, EVA-02) |

## 15 Informative references

Document-level references; no clause-level reliance is implied.

- ISO 9001 (quality management systems); ISO 44001 (collaborative business relationship management)
- ISO 22301 (business continuity management systems); ISO 22318 (supply chain continuity); ISO 28000 (supply chain security management)
- ISO/IEC 27001 (information security management systems); ISO/IEC 27036 series (information security for supplier relationships)
- ISO/IEC 20243 (Open Trusted Technology Provider Standard)
- NIST SP 800-161r1 (cyber supply chain risk management); NIST SP 800-218 (Secure Software Development Framework); NIST SP 800-193 (platform firmware resiliency); NIST SP 800-147 (BIOS protection); NIST SP 800-82r3 (OT security); NIST SP 800-53 Rev. 5 (AC and MA control families)
- IEC 62443 series, in particular IEC 62443-2-4 (service providers), IEC 62443-4-1 (secure product development) and IEC TR 62443-2-3 (patch management)
- ISO/IEC 29147 (vulnerability disclosure); ISO/IEC 30111 (vulnerability handling); FIRST CVSS; CISA Known Exploited Vulnerabilities catalogue
- ISO/IEC 5962 (SPDX); ECMA-424 (CycloneDX); NTIA minimum elements for an SBOM
- DMTF DSP0274 (SPDM); DMTF Redfish; IETF RFC 9334 (remote attestation architecture)
- SAE AS5553, SAE AS6081, SAE AS6171, SAE AS6174 (counterfeit parts avoidance, detection and mitigation)
- TAPA Freight Security Requirements
- IEC 62402 (obsolescence management); ISO 55001 (asset management systems); IEC 60300-3-11 (reliability centred maintenance)
- ISO/IEC 19086-1 (cloud SLA framework); ISO/IEC 20000-1 (service management)
- Directive (EU) 2022/2555 (NIS2) and Regulation (EU) 2022/2554 (DORA) — informative for in-scope sectors
- AIDCF-003, AIDCF-004, AIDCF-008, AIDCF-010, AIDCF-013, AIDCF-014

## 16 Control summary

| Control | Title | Type | AL | Claim type | Gate mappings |
|---|---|---|---|---|---|
| MCF-SUP-001 | Supplier Capability | PREVENTIVE | AL2 | DESIGN | CG-03 (S) |
| MCF-SUP-002 | Financial and Operational Resilience | DETECTIVE | AL4 | OPERATION | CG-03 (S) |
| MCF-SUP-003 | Security and Quality Posture | PREVENTIVE | AL3 | IMPLEMENTATION | CG-08 (S); CG-15 (S) |
| MCF-SUP-004 | Sub-Tier Visibility | PREVENTIVE | AL3 | IMPLEMENTATION | CG-03 (C) |
| MCF-SUP-005 | Service Levels | DIRECTIVE | AL3 | IMPLEMENTATION | CG-10 (S); CG-13 (S) |
| MCF-SUP-006 | Evidence Rights | DIRECTIVE | AL3 | IMPLEMENTATION | CG-03 (S) |
| MCF-SUP-007 | Incident Notification | DETECTIVE | AL4 | OPERATION | CG-03 (S); CG-15 (S) |
| MCF-SUP-008 | Exit and Transition Rights | DIRECTIVE | AL2 | DESIGN | CG-10 (S) |
| MCF-SUP-009 | Approved Sourcing | PREVENTIVE | AL3 | IMPLEMENTATION | CG-08 (S); CG-04 (S) |
| MCF-SUP-010 | Counterfeit Prevention | DETECTIVE | AL4 | OPERATION | CG-04 (S); CG-08 (S) |
| MCF-SUP-011 | Chain of Custody | PREVENTIVE | AL4 | OPERATION | CG-08 (S) |
| MCF-SUP-012 | Component Traceability | DETECTIVE | AL5 | EFFECTIVENESS | CG-08 (S); CG-03 (S) |
| MCF-SUP-013 | Release Provenance | PREVENTIVE | AL3 | IMPLEMENTATION | CG-15 (S); CG-14 (S) |
| MCF-SUP-014 | Signature Validation | PREVENTIVE | AL5 | EFFECTIVENESS | CG-15 (S); CG-08 (S) |
| MCF-SUP-015 | Compatibility Assurance | PREVENTIVE | AL5 | EFFECTIVENESS | CG-14 (S); CG-08 (S); CG-09 (S) |
| MCF-SUP-016 | Vulnerability Response | CORRECTIVE | AL4 | OPERATION | CG-15 (S) |
| MCF-SUP-017 | Critical Spares | RECOVERY | AL4 | OPERATION | CG-10 (S); CG-05 (S); CG-06 (S) |
| MCF-SUP-018 | Lead Times | DIRECTIVE | AL2 | DESIGN | CG-10 (S); CG-03 (S) |
| MCF-SUP-019 | Logistics Continuity | RECOVERY | AL5 | RESILIENCE | CG-10 (S); CG-05 (S) |
| MCF-SUP-020 | End-of-Life Planning | PREVENTIVE | AL4 | OPERATION | CG-03 (S) |
| MCF-SUP-021 | Support Identity | PREVENTIVE | AL3 | IMPLEMENTATION | CG-15 (C); CG-13 (S) |
| MCF-SUP-022 | Activation and Approval | PREVENTIVE | AL4 | OPERATION | CG-15 (C); CG-14 (S) |
| MCF-SUP-023 | Session Monitoring | DETECTIVE | AL4 | OPERATION | CG-15 (S) |
| MCF-SUP-024 | Revocation and Review | CORRECTIVE | AL4 | OPERATION | CG-15 (S); CG-13 (S) |

Key: (C) = CRITICAL role, (S) = SUPPORTING role, per AIDCF-010 gate roll-up. CG-11 and CG-12 are evaluated across all controls and are not mapped per control.

## 17 Worked synthetic example

> **Synthetic example.** All names, values and results below are invented for illustration. They do not describe any real supplier, product, facility or assessment.

**Context.** Synthetic Capability Instance CI-SYN-INF-02 is an inference platform in an owner-operated hall with direct-to-chip liquid cooling from six CDUs on a shared secondary loop, and a two-tier leaf-spine fabric. The decision question asks whether the platform can meet its availability outcome under NORMAL, MAINTENANCE and RECOVERY states.

**Firmware rollout (MCF-SUP-015).** The assessor reconstructed the last NIC firmware rollout. The compatibility matrix had been updated and a pre-production test passed. Rollout records showed three waves, each confined to one fabric pod, with a 24-hour soak and automated health gates; redundant members were never in one wave. Result: CONFORMING (EFFECTIVENESS, S4).

**Signature validation (MCF-SUP-014).** Verification logs covered all staged releases. Signature enforcement was enabled on BMCs and switches. The CDU controllers could not enforce signatures; this was recorded with a compensating hash check before upload. A rejection test had been performed on a lab BMC and lab switch within the interval. Result: CONFORMING.

**Support identity (MCF-SUP-021).** Account exports from the BMS, EPMS and two sampled CDU controllers found a generic "service" account on all six CDU controllers, shared by the CDU OEM's field engineers and not vaulted. Result: NONCONFORMING (Finding: shared vendor account on control-plane devices).

**Activation and approval (MCF-SUP-022).** The access gateway was off by default and all sampled IT sessions had approvals. However, the CDU OEM had a separate cellular modem on the CDU management network for remote diagnostics, always on and outside the gateway. Result: NONCONFORMING.

**Critical spares (MCF-SUP-017).** Strategy existed; physical count matched records; one spare CDU pump on site against six installed, with OEM regional stock committed at 48 hours. Result: CONFORMING. Supporting to CG-10.

**Gate result.** CG-15 has MCF-SUP-021 and MCF-SUP-022 as CRITICAL controls in this domain (with the SEC CRITICAL controls). Both are NONCONFORMING, so **CG-15 = FAIL** under the AIDCF-010 roll-up rule, regardless of the SEC results. CG-14 and CG-08 receive SUPPORTING inputs from MCF-SUP-015 (CONFORMING) and need no gate-level evaluation from this domain.

**Decision effect and actions.** A FAIL on CG-15 prevents a REASONABLY_ASSURED decision; the ceiling is that defined for CG-15 in AIDCF-010. Actions: remove the cellular modem or bring it behind the access gateway with off-by-default activation; replace the shared CDU account with named vendor identities or a vaulted per-use checkout; re-export accounts to verify. Reassessment trigger: closure of both Findings with E2 evidence.

**What the example shows.** The IT management plane was well controlled; the exposure sat in a facility controller supplied and supported by an OEM, reached through a path the IT team did not own. SUP-06 controls, applied to facility systems as well as IT, are what surface it.
