# AIDCF-007A Control Catalogue — SUP Supply Chain, OEM and Ecosystem Assurance

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-SUP](../../../aidcf-018-domain-guides/AIDCF-018-SUP_Supply_Chain_OEM_and_Ecosystem_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-SUP-001](#mcf-sup-001) | Supplier Capability | PREVENTIVE | DESIGN | AL2 | — | CG-03 |
| [MCF-SUP-002](#mcf-sup-002) | Financial and Operational Resilience | DETECTIVE | OPERATION | AL4 | — | CG-03 |
| [MCF-SUP-003](#mcf-sup-003) | Security and Quality Posture | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-08, CG-15 |
| [MCF-SUP-004](#mcf-sup-004) | Sub-Tier Visibility | PREVENTIVE | IMPLEMENTATION | AL3 | CG-03 | — |
| [MCF-SUP-005](#mcf-sup-005) | Service Levels | DIRECTIVE | IMPLEMENTATION | AL3 | — | CG-10, CG-13 |
| [MCF-SUP-006](#mcf-sup-006) | Evidence Rights | DIRECTIVE | IMPLEMENTATION | AL3 | — | CG-03 |
| [MCF-SUP-007](#mcf-sup-007) | Incident Notification | DETECTIVE | OPERATION | AL4 | — | CG-03, CG-15 |
| [MCF-SUP-008](#mcf-sup-008) | Exit and Transition Rights | DIRECTIVE | DESIGN | AL2 | — | CG-10 |
| [MCF-SUP-009](#mcf-sup-009) | Approved Sourcing | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-08, CG-04 |
| [MCF-SUP-010](#mcf-sup-010) | Counterfeit Prevention | DETECTIVE | OPERATION | AL4 | — | CG-04, CG-08 |
| [MCF-SUP-011](#mcf-sup-011) | Chain of Custody | PREVENTIVE | OPERATION | AL4 | — | CG-08 |
| [MCF-SUP-012](#mcf-sup-012) | Component Traceability | DETECTIVE | EFFECTIVENESS | AL5 | — | CG-08, CG-03 |
| [MCF-SUP-013](#mcf-sup-013) | Release Provenance | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-15, CG-14 |
| [MCF-SUP-014](#mcf-sup-014) | Signature Validation | PREVENTIVE | EFFECTIVENESS | AL5 | — | CG-15, CG-08 |
| [MCF-SUP-015](#mcf-sup-015) | Compatibility Assurance | PREVENTIVE | EFFECTIVENESS | AL5 | — | CG-14, CG-08, CG-09 |
| [MCF-SUP-016](#mcf-sup-016) | Vulnerability Response | CORRECTIVE | OPERATION | AL4 | — | CG-15 |
| [MCF-SUP-017](#mcf-sup-017) | Critical Spares | RECOVERY | OPERATION | AL4 | — | CG-10, CG-05, CG-06 |
| [MCF-SUP-018](#mcf-sup-018) | Lead Times | DIRECTIVE | DESIGN | AL2 | — | CG-10, CG-03 |
| [MCF-SUP-019](#mcf-sup-019) | Logistics Continuity | RECOVERY | RESILIENCE | AL5 | — | CG-10, CG-05 |
| [MCF-SUP-020](#mcf-sup-020) | End-of-Life Planning | PREVENTIVE | OPERATION | AL4 | — | CG-03 |
| [MCF-SUP-021](#mcf-sup-021) | Support Identity | PREVENTIVE | IMPLEMENTATION | AL3 | CG-15 | CG-13 |
| [MCF-SUP-022](#mcf-sup-022) | Activation and Approval | PREVENTIVE | OPERATION | AL4 | CG-15 | CG-14 |
| [MCF-SUP-023](#mcf-sup-023) | Session Monitoring | DETECTIVE | OPERATION | AL4 | — | CG-15 |
| [MCF-SUP-024](#mcf-sup-024) | Revocation and Review | CORRECTIVE | OPERATION | AL4 | — | CG-15, CG-13 |

## SUP-01 Supplier due diligence

### MCF-SUP-001

**Supplier Capability** · PREVENTIVE · claim type DESIGN · required AL2

**Objective.** Suppliers of critical equipment and services are shown, before award and at renewal, to have the technical, manufacturing, integration, installation and field-support capability required by the Capability Instance at the site and scale proposed.

**Requirement.** The procurement lead shall perform and record a capability assessment for each supplier of a critical asset class or service before award and at renewal, covering engineering competence, manufacturing and test capacity (including factory acceptance testing), rack-scale or skid integration capability where applicable, installation and commissioning resources, field-service coverage and response at the site, and references for comparable deployments. A competent engineer shall approve the technical part of the assessment.

**Assessment criteria**

1. A capability assessment exists for each critical supplier, dated before award or last renewal.
2. The assessment addresses manufacturing/test capacity, integration, installation/commissioning and field-service coverage for the specific site.
3. Factory acceptance test (FAT) capability and witness arrangements are confirmed for equipment where FAT is specified (for example switchgear, UPS, CDUs, rack-scale systems).
4. Technical approval by a competent engineer is recorded.
5. Identified capability gaps have conditions in the contract or an accepted risk.

**Minimum evidence**

- Supplier capability assessments.
- FAT plans or capability statements.
- Field-service coverage statements.
- Engineering approval records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Assessment valid for the current contract term. |
| independence | Technical approval by an engineer not in the procurement line. |
| mandatoryItems | Capability assessment with engineering approval |
| acceptableAlternatives | Prior successful delivery of the same product at a comparable site by the same supplier, documented by acceptance records, may replace part of the reference check. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | New critical supplier; Contract renewal; Supplier acquisition or restructuring; Significant delivery or quality failure |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY, SAMPLING

**Assessment procedure**

1. List critical suppliers from DEP-011/DEP-014.
2. Obtain capability assessments and approvals.
3. Check coverage of manufacturing, integration, installation and field service.
4. Verify gaps have contractual conditions or acceptance.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to suppliers of critical asset classes and services; non-critical suppliers follow standard procurement.

**Lifecycle stages.** PLAN, DESIGN, BUILD, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** Integrator lacks capacity to test rack-scale systems before delivery; No field engineer within response time of the site; Supplier cannot perform specified FAT

**Testing safety.** Not applicable (documentary assessment).

**UNKNOWN rule.** Missing capability assessment for a critical supplier is U1, US3.

**Ontology classes.** Dependency, Resource, AssetInstance · **Related controls.** MCF-SUP-002, MCF-SUP-003, MCF-DEP-011, MCF-CAP-022

**Informative references.** ISO 9001 (quality management systems); ISO 44001 (collaborative business relationship management); ISO/IEC 27036-2 (supplier relationships: requirements)

### MCF-SUP-002

**Financial and Operational Resilience** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** The financial health, manufacturing footprint, allocation exposure and business-continuity capability of critical suppliers are monitored so that supplier distress or disruption is detected early enough to act.

**Requirement.** The supplier manager shall monitor each critical supplier at the profile interval for financial distress indicators, manufacturing and logistics concentration (single plant or region), allocation or quota exposure (for example accelerator allocations), sanctions and export-control exposure, and business-continuity arrangements, and shall escalate adverse changes to the capability owner with a proposed treatment.

**Assessment criteria**

1. Each critical supplier has monitoring records at the interval for the period.
2. Manufacturing and logistics concentration is recorded per supplier.
3. Allocation, sanctions and export-control exposure is assessed for supply-constrained classes.
4. Supplier business-continuity evidence has been obtained for the most critical suppliers.
5. Adverse changes in the period were escalated with treatment.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Supplier monitoring interval | months | 6 | Illustrative; quarterly for sole-source suppliers. |

**Minimum evidence**

- Supplier monitoring records.
- Financial risk reports (credit agency or equivalent).
- Supplier BCP summaries.
- Escalation records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | At least 12 months. |
| independence | At least one external information source (credit agency, public filings) per supplier. |
| mandatoryItems | Monitoring records for the period |
| acceptableAlternatives | Group-level monitoring by a parent organisation is acceptable if it covers the specific suppliers. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Adverse financial signal; Plant disruption; Sanctions or export-control change; Allocation change |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INQUIRY

**Assessment procedure**

1. Obtain monitoring records.
2. Check interval adherence and coverage.
3. Review export and allocation exposure analyses.
4. Trace adverse changes to escalation.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to critical suppliers.

**Lifecycle stages.** PLAN, OPERATE, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** Supplier insolvency halts spares; Single plant outage stops supply; Export restriction blocks accelerator deliveries

**Testing safety.** Desk-based monitoring; no site testing is involved.

**UNKNOWN rule.** No monitoring of a sole-source supplier is US3.

**Ontology classes.** Dependency, Threat, Resource · **Related controls.** MCF-SUP-001, MCF-DEP-014, MCF-SUP-018

**Informative references.** ISO 22318 (guidelines for supply chain continuity); ISO 22301 (business continuity management systems); NIST SP 800-161r1 (cyber supply chain risk management)

### MCF-SUP-003

**Security and Quality Posture** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Critical suppliers operate quality management and secure development practices adequate for products that will run, control or protect AI infrastructure, including product security incident response for firmware and control software.

**Requirement.** The procurement lead shall obtain and evaluate evidence of each critical supplier's quality management system, product security development lifecycle for firmware and control software, product security incident response (PSIRT) and vulnerability disclosure process, and factory test and outgoing quality controls. The procurement lead shall record identified gaps with contract conditions and shall track incoming quality (defects on receipt, early-life failures) for each supplier.

**Assessment criteria**

1. Quality management evidence (certificate or audit) is current for each critical supplier.
2. Secure development lifecycle evidence exists for suppliers of firmware or control software.
3. A PSIRT or equivalent contact and disclosure process exists for each firmware or software supplier.
4. Incoming quality data is tracked and reviewed.
5. Gaps have contractual conditions.

**Minimum evidence**

- QMS certificates or audit reports.
- Secure development evidence (for example IEC 62443-4-1 assessment or equivalent attestation).
- PSIRT contacts and disclosure policy.
- Incoming quality records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Certificates current; incoming quality for 12 months. |
| independence | Third-party certificates or audit reports preferred (E5). |
| mandatoryItems | QMS evidence; PSIRT/disclosure evidence for firmware suppliers |
| acceptableAlternatives | Owner-performed supplier audit may replace third-party certificate. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-08, CG-15 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Certificate expiry; Product security incident; Quality escape |

**Assessment methods.** DOCUMENT_REVIEW, INQUIRY, ANALYSIS

**Assessment procedure**

1. Obtain supplier posture evidence.
2. Check currency and scope.
3. Review incoming quality data.
4. Check gap conditions.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to critical hardware, firmware and control-software suppliers.

**Lifecycle stages.** PLAN, BUILD, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Supplier without vulnerability disclosure process; Batch quality escape in optics or memory; Uncontrolled firmware build process

**Testing safety.** Desk-based evaluation; any supplier site audit follows the supplier's site safety rules.

**UNKNOWN rule.** Missing PSIRT evidence for a firmware supplier is US3.

**Ontology classes.** Dependency, Threat, AssetInstance · **Related controls.** MCF-SUP-016, MCF-SUP-013, MCF-SEC-014

**Informative references.** ISO 9001 (quality management systems); IEC 62443-4-1 (secure product development lifecycle); NIST SP 800-218 (Secure Software Development Framework); ISO/IEC 29147 (vulnerability disclosure); ISO/IEC 30111 (vulnerability handling processes)

### MCF-SUP-004

**Sub-Tier Visibility** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Critical sub-tier dependencies behind first-tier suppliers (for example high-bandwidth memory and advanced packaging for accelerators, laser and optical components, transformer core steel and bushings, switchgear breaker mechanisms, CDU pumps and heat exchangers, battery cells, controller chipsets, and contract manufacturers) are known well enough to reveal shared sub-tier sources across nominally diverse suppliers.

**Requirement.** The procurement lead shall obtain, for each critical asset class, disclosure of material sub-tier suppliers and manufacturing locations from first-tier suppliers, record them in the dependency graph, and identify sub-tier sources shared across nominally diverse first-tier suppliers. Where a supplier declines disclosure, the procurement lead shall record an UNKNOWN Record and the capability owner shall decide on treatment.

**Assessment criteria**

1. Sub-tier disclosure has been requested and recorded for each critical asset class.
2. Shared sub-tier sources across diverse first-tier suppliers are identified.
3. Sub-tier information is in the dependency graph and used in DEP-014 concentration analysis.
4. Declined or partial disclosures are UNKNOWN Records with treatment decisions.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Sub-tier depth for critical classes | tiers | 2 | Illustrative; deeper where single-source components are known. |

**Minimum evidence**

- Sub-tier disclosure records.
- Dependency graph sub-tier entries.
- UNKNOWN Records for declined disclosures.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; RECOVERY |
| periodCoverage | Current; refreshed at renewal. |
| independence | Corroboration from a second source (market intelligence, teardown, certification records) for a sample. |
| mandatoryItems | Sub-tier disclosure records for critical classes |
| acceptableAlternatives | Industry consortium sub-tier mapping may substitute where suppliers participate. |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-03 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. |
| reassessmentTriggers | Supplier change of contract manufacturer; Sub-tier disruption reported; Renewal |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, INQUIRY, RECONCILIATION

**Assessment procedure**

1. Obtain disclosures.
2. Map into dependency graph.
3. Search for shared sub-tier nodes.
4. Corroborate a sample.
5. Review UNKNOWN treatment.

**Gate mappings.** CG-03 Critical dependency visibility (CRITICAL)

**Applicability.** Applies to critical asset classes with constrained supply or long lead times.

**Lifecycle stages.** PLAN, DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, RECOVERY

**Failure modes addressed.** Two UPS brands share one battery-cell maker; All accelerator suppliers depend on one packaging capacity; Transformer suppliers share one bushing source

**Testing safety.** Desk-based analysis; sub-tier disclosures may be commercially sensitive and shall be handled under the classification rules of AIDCF-008.

**UNKNOWN rule.** Declined sub-tier disclosure for a critical class whose failure would defeat recovery or expansion is U2/U10, US4 (CG-03 critical).

**Ontology classes.** Dependency, Resource, UnknownRecord · **Related controls.** MCF-DEP-014, MCF-SUP-002, MCF-SUP-018, MCF-DEP-002

**Informative references.** NIST SP 800-161r1 (cyber supply chain risk management); ISO 22318 (guidelines for supply chain continuity); ISO 28000 (supply chain security management)

## SUP-02 Contract and service obligations

### MCF-SUP-005

**Service Levels** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Contracts for maintenance, support and supply of critical systems contain measurable service levels (response, on-site attendance, restore, parts availability, RMA turnaround) that are consistent with the Service Outcome and recovery tolerances.

**Requirement.** The supplier manager shall ensure each critical support or maintenance contract states measurable service levels with units, measurement points, exclusions and escalation, and shall document that each service level is consistent with the time-to-impact and recovery tolerances in DEP-003 and CAP-02. Where contracted levels are inconsistent, the capability owner shall record the gap and its treatment (on-site spares, resident engineers, alternative supplier).

**Assessment criteria**

1. Each critical contract has measurable service levels with units and measurement points.
2. Service levels are compared with tolerances and the comparison is recorded.
3. Inconsistencies have treatments.
4. Escalation contacts and paths are current.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum on-site attendance time for critical electrical/mechanical faults | hours | 4 | Illustrative; set from DEP-003 time-to-impact and spares held. |

**Minimum evidence**

- Contracts or schedules with service levels.
- Tolerance comparison.
- Escalation contact lists.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; EMERGENCY; RECOVERY |
| periodCoverage | Current contracts. |
| independence | Comparison checked by engineering, not only procurement. |
| mandatoryItems | Contracts with measurable service levels |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-10, CG-13 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Contract renewal; Tolerance change; Supplier change |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. List critical contracts.
2. Extract service levels.
3. Compare with tolerances.
4. Review treatments and escalation lists.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to critical support and maintenance contracts.

**Lifecycle stages.** PLAN, BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, EMERGENCY, RECOVERY

**Failure modes addressed.** Next-business-day support for asset with minutes time-to-impact; Exclusions void service level during regional event

**Testing safety.** Contract review only; no response-time test shall be performed by raising false faults with suppliers.

**UNKNOWN rule.** Service level absent for a critical contract is US3.

**Ontology classes.** Dependency, Interface, Resource · **Related controls.** MCF-DEP-022, MCF-DEP-003, MCF-SUP-017

**Informative references.** ISO/IEC 20000-1 (service management system requirements); ISO/IEC 19086-1 (cloud SLA framework)

### MCF-SUP-006

**Evidence Rights** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** The owner has contractual rights to obtain the evidence needed to assess supplier-provided and provider-operated functions: test and commissioning records, maintenance records, firmware SBOMs and release notes, telemetry access, incident RCAs, audit reports and access for witness testing and audit.

**Requirement.** The supplier manager shall ensure that each critical supplier and provider contract grants rights to the evidence listed in the AIDCF-008 control evidence profiles relevant to the supplied function, within stated timescales and formats, including rights to witness tests and to audit or receive independent assurance reports, and shall record any evidence the supplier will not provide as an UNKNOWN Record against the affected controls.

**Assessment criteria**

1. Each critical contract has an evidence-rights clause or schedule.
2. The listed evidence covers mandatory items of the affected controls.
3. Rights to witness FAT/SAT and audit exist where needed.
4. Refused evidence is recorded as UNKNOWN against controls.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Evidence delivery time on request | working days | 10 | Illustrative. |

**Minimum evidence**

- Contract evidence-rights clauses.
- Mapping of rights to control evidence profiles.
- Records of evidence requests and responses.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Current contracts; request log for 12 months. |
| independence | Not applicable beyond document review. |
| mandatoryItems | Evidence-rights clauses |
| acceptableAlternatives | Independent assurance reports (for example SOC 2 or ISO certification audit reports) with access to underlying evidence on request. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Renewal; Refused evidence request |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING

**Assessment procedure**

1. Obtain clauses.
2. Map to control evidence profiles.
3. Sample evidence requests and responses.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to critical supplier and provider contracts.

**Lifecycle stages.** PLAN, BUILD, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Colocation provider refuses generator test records; OEM declines firmware SBOM; No right to witness CDU FAT

**Testing safety.** Contract review only; evidence requests are made through the contract channel, not by direct access to supplier systems.

**UNKNOWN rule.** Absent evidence rights for a provider-operated critical function is US3 for this control; the consequential UNKNOWN on dependent controls takes those controls' severity.

**Ontology classes.** EvidenceRequirement, Dependency, UnknownRecord · **Related controls.** MCF-DEP-018, MCF-EVA-002, MCF-SUP-013

**Informative references.** ISO/IEC 27036-2 (supplier relationships: requirements); ISO 19011 (auditing management systems); AICPA SOC 2 reporting framework

### MCF-SUP-007

**Incident Notification** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Suppliers and providers notify the owner promptly of incidents, vulnerabilities, field notices, recalls, allocation changes and planned changes that could affect supplied functions, and the notifications reach the people who must act.

**Requirement.** The supplier manager shall ensure critical supplier and provider contracts define notification obligations and timescales for incidents, security vulnerabilities, field notices and recalls, planned maintenance and changes, and allocation or end-of-life changes, and shall operate a monitored intake (shared mailbox, portal subscription, ticket integration) that routes notifications to the responsible owner. The supplier manager shall test the intake path at the profile interval.

**Assessment criteria**

1. Notification obligations and timescales exist in critical contracts.
2. Notification intake is monitored and routed to responsible owners.
3. Notifications in the period were received, routed and acted on within timescales.
4. The intake path was tested within the interval.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Notification intake test interval | months | 6 | Illustrative. |

**Minimum evidence**

- Contract notification clauses.
- Intake configuration and routing rules.
- Notification log for period.
- Intake test records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED |
| periodCoverage | At least 6 months. |
| independence | Assessor cross-checks a sample of public supplier advisories against the intake log. |
| mandatoryItems | Notification log; Intake test record |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03, CG-15 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Missed notification; Contact change; New supplier |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, TEST, SAMPLING

**Assessment procedure**

1. Obtain clauses and intake design.
2. Compare public advisories to intake log.
3. Trace sample to action.
4. Review intake tests.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to critical suppliers and providers that can affect a supplied function through incidents, vulnerabilities, recalls or planned changes.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED

**Failure modes addressed.** Field notice for breaker trip units missed; Carrier planned works not received; Vulnerability advisory for BMC firmware unnoticed

**Testing safety.** Intake tests send synthetic notifications only.

**UNKNOWN rule.** No notification log is U1, US3.

**Ontology classes.** Event, Dependency, Action · **Related controls.** MCF-SUP-016, MCF-DEP-023, MCF-SUP-020

**Informative references.** Directive (EU) 2022/2555 (NIS2), supply chain and incident reporting provisions — informative; ISO/IEC 27036-3 (ICT supply chain security); ISO/IEC 29147 (vulnerability disclosure)

### MCF-SUP-008

**Exit and Transition Rights** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** The owner can exit or replace a critical supplier or provider without losing the ability to operate, maintain or recover critical systems, including access to configuration, control logic, data, documentation, licences, spares and transition assistance.

**Requirement.** The supplier manager shall ensure each critical contract provides exit and transition rights proportionate to the dependency, including export of configuration and operational data in usable formats, ownership or escrow of control logic and configuration for programmable controllers, perpetual or transition licences for software required to operate installed equipment, option to purchase spares and tools, documentation hand-over, and transition assistance for a stated period. The capability owner shall maintain an exit plan for each sole-source or high-concentration supplier.

**Assessment criteria**

1. Exit and transition clauses exist in critical contracts.
2. Control logic and configuration ownership or escrow is established for programmable controllers.
3. Licences needed to operate installed equipment survive termination or transition.
4. Exit plans exist for sole-source and high-concentration suppliers.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Minimum transition assistance period | months | 12 | Illustrative. |

**Minimum evidence**

- Contract exit clauses.
- Escrow agreements or ownership evidence.
- Licence terms.
- Exit plans.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; TRANSITION |
| periodCoverage | Current contracts. |
| independence | Legal and engineering review recorded. |
| mandatoryItems | Exit clauses; Exit plans for sole-source suppliers |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-10 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Renewal; Supplier distress; Licensing model change |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Obtain clauses and plans.
2. Check control-logic and licence provisions.
3. Review exit plans for feasibility.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to critical suppliers and providers; mandatory exit plans apply to sole-source and high-concentration suppliers identified under MCF-DEP-014.

**Lifecycle stages.** PLAN, OPERATE, DECOMMISSION · **Operating states.** NORMAL, TRANSITION

**Failure modes addressed.** Supplier exit leaves BMS without editable logic; Licence revocation disables installed equipment; Provider holds operational data hostage

**Testing safety.** Contract and plan review only; escrow release or licence-transfer trials are performed only under agreement with the supplier.

**UNKNOWN rule.** No exit plan for a sole-source supplier is US3.

**Ontology classes.** Dependency, Resource · **Related controls.** MCF-DEP-015, MCF-DEP-016, MCF-SUP-020

**Informative references.** ISO/IEC 27036-2 (supplier relationships: requirements); ISO/IEC 19086-1 (cloud SLA framework); Regulation (EU) 2022/2554 (DORA), exit strategy provisions — informative

## SUP-03 Hardware and component provenance

### MCF-SUP-009

**Approved Sourcing** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Critical components (protection devices, circuit breakers and trip units, relays, UPS modules and batteries, accelerators and boards, memory, optics, NICs/DPUs, storage media, controllers and sensors) are purchased only from the OEM or OEM-authorised channels, so that counterfeit, grey-market, refurbished-as-new and tampered parts are excluded at source.

**Requirement.** The procurement lead shall maintain an approved source list for each critical component class naming the OEM and authorised distributors, shall configure purchasing controls so that orders for critical classes can be placed only with approved sources, and shall require documented engineering approval and enhanced inspection (MCF-SUP-010) for any exception, such as broker purchase of obsolete parts.

**Assessment criteria**

1. An approved source list exists per critical component class.
2. Purchasing system controls restrict critical-class orders to approved sources.
3. A sample of purchase orders in the period shows only approved sources or approved exceptions.
4. Each exception has engineering approval and enhanced inspection evidence.

**Minimum evidence**

- Approved source list.
- Purchasing system configuration.
- Sampled purchase orders.
- Exception approvals.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; RECOVERY |
| periodCoverage | 12 months of purchase orders. |
| independence | Sample drawn by assessor from the purchasing system. |
| mandatoryItems | Approved source list; Purchase order sample |
| acceptableAlternatives | Where a purchasing system cannot enforce restrictions, a documented manual pre-approval with monthly reconciliation is acceptable. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-08, CG-04 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | OEM changes authorised distributors; Exception purchase; Counterfeit incident |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, RECONCILIATION

**Assessment procedure**

1. Obtain list and system configuration.
2. Sample orders including emergency purchases during incidents.
3. Verify source approval and exceptions.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to critical component classes; emergency purchases during recovery are in scope.

**Lifecycle stages.** BUILD, OPERATE, CHANGE · **Operating states.** NORMAL, RECOVERY, EMERGENCY

**Failure modes addressed.** Counterfeit breaker fails to interrupt fault current; Grey-market optics with altered EEPROM; Refurbished GPUs sold as new

**Testing safety.** Purchasing records review only.

**UNKNOWN rule.** Unverifiable source of installed protection devices is US3; US4 if CG-04 relies on their interrupting performance.

**Ontology classes.** AssetInstance, Threat, Safeguard · **Related controls.** MCF-SUP-010, MCF-SUP-011, MCF-PHY-017

**Informative references.** SAE AS5553 (counterfeit electronic parts avoidance); SAE AS6081 (counterfeit parts avoidance for distributors); ISO/IEC 20243 (Open Trusted Technology Provider Standard)

### MCF-SUP-010

**Counterfeit Prevention** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Counterfeit, cloned, remarked or tampered components are detected at receipt, before installation, by inspection and test proportionate to risk, and suspect parts are quarantined and reported.

**Requirement.** The receiving and engineering leads shall operate a risk-based incoming inspection for critical component classes, including label, serial and packaging verification against OEM records, physical inspection, and where risk warrants electrical or functional testing (for example protection device trip testing, optics DOM/EEPROM checks, firmware identity checks on boards). Suspect items shall be quarantined, reported to the OEM and, where required, to the relevant authority, and shall not be installed until cleared.

**Assessment criteria**

1. Incoming inspection criteria are defined per critical class and risk level.
2. Inspection records exist for receipts in the period.
3. OEM serial verification is performed for high-value or safety-critical items.
4. Suspect items were quarantined and reported.
5. No installed critical item in a sample lacks an inspection record.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Serial verification coverage for safety-critical protection devices | % of units received | 100 | Illustrative. |

**Minimum evidence**

- Inspection criteria.
- Receipt inspection records.
- OEM serial verification responses.
- Quarantine log.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; RECOVERY |
| periodCoverage | 12 months of receipts. |
| independence | Inspection by receiving staff independent of the requisitioner. |
| mandatoryItems | Receipt inspection records; Quarantine log |
| acceptableAlternatives | OEM-direct shipment with tamper-evident seals verified on receipt may reduce inspection depth. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-04, CG-08 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Counterfeit alert from industry or OEM; Change of distributor; Emergency purchase |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, INSPECTION, REPERFORMANCE

**Assessment procedure**

1. Obtain inspection criteria.
2. Sample receipts and installed items.
3. Reperform serial verification for a sample.
4. Review quarantine handling.

**Gate mappings.** CG-04 Life safety and hazardous energy (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to receipts of critical component classes.

**Lifecycle stages.** BUILD, OPERATE · **Operating states.** NORMAL, RECOVERY

**Failure modes addressed.** Counterfeit MCCB installed in PDU; Cloned optics causing fabric errors; Remarked memory modules

**Testing safety.** Electrical testing of protection devices shall be done on a test bench by competent persons; no testing of devices in live switchboards under this control.

**UNKNOWN rule.** Installed safety-critical device without inspection record is US3; US4 where it is a protection device relied on by CG-04.

**Ontology classes.** AssetInstance, Threat, TestRecord · **Related controls.** MCF-SUP-009, MCF-SUP-011, MCF-SUP-012

**Informative references.** SAE AS5553 (counterfeit electronic parts avoidance); SAE AS6171 (test methods for suspect counterfeit parts); SAE AS6174 (counterfeit materiel)

### MCF-SUP-011

**Chain of Custody** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** High-value and integrity-sensitive equipment (accelerator systems, storage media, network gear, controllers, spare boards) is under recorded custody from the factory or integrator to installation, so that theft, substitution and tampering in transit or staging are prevented or detected.

**Requirement.** The logistics lead shall require tamper-evident packaging and seals for critical shipments, recorded hand-offs between factory, freight forwarder, carrier and site, secure staging areas with access control, and receipt verification of seals and serials against the advance shipping notice. Breaks in custody or seal anomalies shall be recorded as security events and the affected items quarantined pending inspection.

**Assessment criteria**

1. Custody requirements are in logistics contracts for critical shipments.
2. Custody records exist for sampled shipments end-to-end.
3. Seal and serial verification at receipt is recorded.
4. Staging areas are access-controlled and logged.
5. Custody anomalies were treated as security events.

**Minimum evidence**

- Logistics contracts.
- Custody records and seal logs.
- Advance shipping notices.
- Staging access logs.
- Anomaly reports.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | 12 months of critical shipments. |
| independence | Assessor reconciles records from forwarder and site independently. |
| mandatoryItems | Custody records for sampled shipments |
| acceptableAlternatives | Secure freight programme certification of the carrier may reduce sampling depth. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-08 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Theft or tamper event; Change of forwarder; New staging location |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, INSPECTION, RECONCILIATION

**Assessment procedure**

1. Sample shipments.
2. Reconcile custody records across parties.
3. Inspect staging area controls.
4. Review anomalies.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to critical and high-value shipments, including RMA returns and spares.

**Lifecycle stages.** BUILD, OPERATE, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** Theft of accelerator trays in transit; Tampered network device inserted; Unlogged staging access

**Testing safety.** Staging-area inspection follows site access control; sealed shipments shall not be opened by the assessor.

**UNKNOWN rule.** Custody gap for an installed integrity-sensitive item is US3.

**Ontology classes.** AssetInstance, Threat, Event · **Related controls.** MCF-PHY-017, MCF-PHY-018, MCF-SUP-010

**Informative references.** ISO 28000 (supply chain security management); TAPA Freight Security Requirements; ISO/IEC 20243 (Open Trusted Technology Provider Standard)

### MCF-SUP-012

**Component Traceability** · DETECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Critical installed components can be traced by serial number, part number, revision and firmware to their location and the functions they support, quickly enough to act on a field notice, recall or vulnerability before it causes harm.

**Requirement.** The asset manager shall record serial, part number, hardware revision and firmware version for critical components (accelerators and boards, NICs/DPUs, optics, switch line cards, storage media, breaker trip units, relays, UPS modules, batteries, CDU pumps and controllers) in the asset register linked to location and Required Function, and shall demonstrate at the profile interval, by exercise, that all units affected by a given notice can be identified within the target time.

**Assessment criteria**

1. Critical component records include serial, part, revision and firmware with location.
2. Records reconcile to installed units for a sample.
3. A traceability exercise in the interval identified all affected units within target time.
4. Real field notices in the period were traced and actioned.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Target time to identify all affected units | hours | 24 | Illustrative. |
| Traceability exercise interval | months | 12 | Illustrative. |

**Minimum evidence**

- Asset register extract.
- Reconciliation sample.
- Exercise record with timing.
- Field notice action records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E6; E7 |
| qualityFloor | P4 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Exercise within the interval. |
| independence | Exercise scenario set by the assessor or a party independent of the asset manager. |
| mandatoryItems | Exercise record; Reconciliation sample |
| acceptableAlternatives | A real recall response within the interval is acceptable in place of an exercise. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-08, CG-03 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Asset register platform change; Major deployment; Interval elapsed |

**Assessment methods.** RECONCILIATION, SCENARIO_EXERCISE, SAMPLING, TEST

**Assessment procedure**

1. Obtain register.
2. Reconcile sample to installed units via inspection or telemetry (for example inventory from BMC/Redfish).
3. Run or review traceability exercise with a defined notice.
4. Review real notice handling.

**Gate mappings.** CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to critical component classes.

**Lifecycle stages.** BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL

**Failure modes addressed.** Recall for battery cells cannot be scoped; Optics batch with defect cannot be located; Firmware vulnerability scope unknown

**Testing safety.** Exercise is desk-based; reading inventory via management interfaces uses read-only accounts.

**UNKNOWN rule.** Inability to scope a real field notice affecting critical components is US3; US4 where the notice concerns a life-safety or protection device.

**Ontology classes.** AssetInstance, TestRecord, Event · **Related controls.** MCF-DEP-001, MCF-CMP-013, MCF-SUP-007

**Informative references.** ISO/IEC 19770-1 (IT asset management); DMTF Redfish (platform management API) for inventory retrieval; GS1 identification standards

## SUP-04 Software, firmware and update supply

### MCF-SUP-013

**Release Provenance** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Every firmware, software and configuration package deployed to AI and facility infrastructure (accelerator and board firmware, BMC/BIOS, NIC/DPU firmware, switch OS, storage controller software, drivers and runtime stacks, UPS/PDU/ATS firmware, BMS/EPMS software, CDU and PLC logic) comes from an authenticated source with release notes and component inventory, and is held in a controlled internal repository before deployment.

**Requirement.** The platform and control-system owners shall obtain releases only from authenticated OEM channels, record for each release its origin, version, hash, release notes and software bill of materials where available, store it in a controlled repository with access control and integrity protection, and deploy only from that repository. Releases for programmable facility controllers shall be held with the same controls as IT firmware.

**Assessment criteria**

1. A controlled repository exists for firmware and software releases covering IT and facility systems.
2. Each release in the repository has origin, version, hash and release notes recorded; SBOM is held where the supplier provides one.
3. Deployment tooling pulls only from the repository (configuration evidence).
4. A sample of deployed versions reconciles to repository entries.
5. PLC/CDU/BMS logic versions are held with equivalent controls.

**Minimum evidence**

- Repository inventory with metadata.
- Repository access control configuration.
- Deployment tool configuration.
- Reconciliation of deployed versions.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; RECOVERY |
| periodCoverage | Current; sample from the preceding 12 months of deployments. |
| independence | Reconciliation by assessor from device-reported versions. |
| mandatoryItems | Repository inventory; Deployed-version reconciliation |
| acceptableAlternatives | For devices updated only by OEM field engineers, an OEM-signed release record per update is acceptable. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-15, CG-14 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | New device class; Repository platform change; OEM channel change |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, SAMPLING, INSPECTION

**Assessment procedure**

1. Obtain repository inventory.
2. Check metadata completeness.
3. Inspect deployment tooling configuration.
4. Reconcile deployed versions from devices to repository.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to all programmable devices in the boundary.

**Lifecycle stages.** BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, RECOVERY

**Failure modes addressed.** Firmware downloaded from unofficial mirror; PLC logic version unknown; Untracked driver stack on part of cluster

**Testing safety.** Device version reads use read-only interfaces; no update is performed under this control.

**UNKNOWN rule.** Unknown provenance of deployed firmware on a control-system or protection device is US3; US4 where CG-07 or CG-15 relies on it.

**Ontology classes.** AssetInstance, EvidenceObject, Threat · **Related controls.** MCF-SUP-014, MCF-CMP-013, MCF-SEC-013, MCF-OPS-017

**Informative references.** NIST SP 800-218 (Secure Software Development Framework); ISO/IEC 5962 (SPDX); ECMA-424 (CycloneDX); NTIA minimum elements for an SBOM

### MCF-SUP-014

**Signature Validation** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Firmware and software are cryptographically verified before installation and, where the platform supports it, at boot, so that modified or malicious images are rejected.

**Requirement.** The platform and control-system owners shall verify OEM signatures (or, where signing is unavailable, OEM-published hashes obtained over an authenticated channel) before staging any release to the repository and before deployment, shall enable platform secure-boot and firmware-signature enforcement where supported (for example on BMCs, accelerators, NICs/DPUs, switches), and shall record device classes that cannot enforce signatures with compensating controls. The owners shall demonstrate rejection of an unsigned or altered image on a non-production device for each enforcing device class.

**Assessment criteria**

1. Signature or hash verification is performed and logged for each release staged in the period.
2. Signature enforcement is enabled on supporting device classes (configuration evidence).
3. Non-enforcing device classes are listed with compensating controls.
4. A rejection test on non-production equipment has been performed for each enforcing class.
5. Where supported, firmware attestation (for example via SPDM measurements) is collected.

**Minimum evidence**

- Verification logs.
- Device configuration showing signature enforcement.
- Non-enforcing class register.
- Rejection test records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E6; E7 |
| qualityFloor | P4 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; RECOVERY |
| periodCoverage | Verification logs for 12 months; tests within 24 months (illustrative). |
| independence | Rejection test witnessed or performed by security function. |
| mandatoryItems | Verification logs; Rejection test records |
| acceptableAlternatives | OEM documentation of enforced verification may substitute for testing of device classes where no non-production unit exists, at confidence no higher than CONF-2. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-15, CG-08 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | New device class; Change to signing keys or enforcement settings; OEM key compromise advisory |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, TEST, SAMPLING

**Assessment procedure**

1. Obtain logs and configuration.
2. Sample releases and check verification.
3. Inspect enforcement settings.
4. Review or witness rejection test.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all programmable devices; enforcement criterion applies where the platform supports it.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, RECOVERY

**Failure modes addressed.** Malicious BMC firmware installed; Tampered switch OS image; Unsigned PLC logic loaded

**Testing safety.** Rejection tests shall be performed only on non-production devices isolated from production management networks; flashing production devices to test is prohibited.

**UNKNOWN rule.** Unknown enforcement status on a device class with control-plane authority is US3; US4 where CG-15 relies on it.

**Ontology classes.** Safeguard, TestRecord, AssetInstance · **Related controls.** MCF-SUP-013, MCF-SEC-013, MCF-CMP-013

**Informative references.** NIST SP 800-193 (platform firmware resiliency); NIST SP 800-147 (BIOS protection); DMTF DSP0274 (SPDM); IETF RFC 9334 (remote attestation procedures architecture)

### MCF-SUP-015

**Compatibility Assurance** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Firmware, driver and software updates are deployed only in combinations that are validated as compatible, and are rolled out in stages aligned to fault domains so that a defective release cannot defeat redundant capacity at once.

**Requirement.** The platform owner shall maintain a compatibility matrix for interdependent components (for example accelerator firmware, driver and runtime libraries, NIC/DPU firmware, switch OS, BMC/BIOS, storage client; and for facility systems UPS firmware and EPMS, CDU controller and BMS integration), shall test each new combination on a representative non-production environment, and shall deploy through staged waves where each wave is confined to one fault domain and passes defined health criteria before the next begins. Redundant members of a group shall not be updated in the same wave.

**Assessment criteria**

1. A compatibility matrix exists and is current.
2. Each deployed combination in the period was tested before production.
3. Rollouts followed fault-domain-aligned waves with health gates (deployment records).
4. No rollout updated redundant members of a group in one wave.
5. Health-gate failures halted rollouts and triggered rollback.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum share of a redundant group updated per wave | % of group | 50 (and never all members) | Illustrative. |
| Soak time between waves | hours | 24 | Illustrative. |

**Minimum evidence**

- Compatibility matrix.
- Pre-production test records.
- Rollout plans and wave records.
- Health-gate results.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E6; E7 |
| qualityFloor | P4 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | MAINTENANCE; TRANSITION; NORMAL |
| periodCoverage | Rollouts in the preceding 12 months. |
| independence | Health-gate criteria set by a team other than the deploying team. |
| mandatoryItems | Compatibility matrix; Wave records |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-14, CG-08, CG-09 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | New hardware generation; Major software stack change; Rollout incident |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, ANALYSIS, TEST

**Assessment procedure**

1. Obtain matrix and rollout records.
2. Sample rollouts and verify tests and waves.
3. Check redundant-member separation.
4. Review halted rollouts.

**Gate mappings.** CG-14 Change control (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to firmware and software updates on in-scope infrastructure.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** MAINTENANCE, TRANSITION, NORMAL

**Failure modes addressed.** Firmware rollout common-mode failure (scenario X08); Driver/firmware mismatch causes accelerator errors; UPS firmware breaks EPMS integration

**Testing safety.** Facility controller updates require method statement and change approval (MCF-OPS-006/018).

**UNKNOWN rule.** Unknown rollout history for a redundant group is US3.

**Ontology classes.** Safeguard, FaultDomain, TestRecord · **Related controls.** MCF-CMP-014, MCF-CMP-015, MCF-DEP-006, MCF-OPS-020

**Informative references.** ISO/IEC/IEEE 12207 (software life cycle processes); SAE EIA-649C (configuration management)

### MCF-SUP-016

**Vulnerability Response** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Vulnerabilities disclosed by suppliers for firmware, OT controllers and AI infrastructure components are triaged, and fixes or compensating controls are applied within timescales proportionate to exposure and consequence.

**Requirement.** The security owner shall track supplier advisories for in-scope products, triage each against the asset register and exposure (network reachability, privilege required), assign a remediation target based on severity and consequence, and record either patch deployment through change control or a compensating control with approved exception. The security owner shall report remediation performance to the accountable owner.

**Assessment criteria**

1. Supplier advisories for in-scope products are tracked.
2. Each relevant advisory was triaged against the asset register.
3. Remediation targets are set by severity and consequence and met, or exceptions approved.
4. OT and facility controller advisories are included.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Remediation target for critical, exposed vulnerabilities | days | 14 | Illustrative; OT may require longer with compensating controls. |

**Minimum evidence**

- Advisory tracking log.
- Triage records.
- Remediation and exception records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | 12 months. |
| independence | Assessor checks a sample of public advisories against the log. |
| mandatoryItems | Advisory tracking log |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-15 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Exploited vulnerability in a used product; New product class |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, RECONCILIATION

**Assessment procedure**

1. Obtain log.
2. Compare with public advisories for in-scope products.
3. Sample remediation timing.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to in-scope products with supplier advisories.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** BMC vulnerability unpatched; PLC advisory ignored; Untracked advisory for CDU controller

**Testing safety.** Patching of facility controllers is performed under change control, never under assessment.

**UNKNOWN rule.** No tracking of OT advisories is US3.

**Ontology classes.** Threat, Action, AssetInstance · **Related controls.** MCF-SEC-014, MCF-SEC-015, MCF-SUP-007

**Informative references.** ISO/IEC 30111 (vulnerability handling processes); FIRST CVSS; CISA Known Exploited Vulnerabilities catalogue; IEC 62443-2-3 (patch management in the IACS environment)

## SUP-05 Spares, logistics and obsolescence

### MCF-SUP-017

**Critical Spares** · RECOVERY · claim type OPERATION · required AL4

**Objective.** Spares for critical assets are held in the quantity, location and condition needed to restore Required Functions within tolerance, based on failure behaviour, installed population, repair time and resupply lead time, rather than on habit or warranty terms.

**Requirement.** The maintenance manager shall define a spares strategy for each critical asset class (for example UPS modules and capacitors, battery strings, breakers and trip units, protection relays, generator starter motors and controllers, CDU pumps and controllers, chiller compressors and VFDs, transformer bushings or, where justified, a strategic spare transformer, accelerator trays or boards, NICs, optics, switch line cards, storage drives), stating stock level, location (on site, regional, OEM-held), basis (population, failure rate, MTTR target, lead time) and condition-maintenance requirements for stored spares. The maintenance manager shall reconcile stock to records at the profile interval and replenish below-minimum stock as a tracked action.

**Assessment criteria**

1. Spares strategy exists for each critical asset class with stated basis.
2. Stock levels and locations meet strategy; physical count reconciles to records for a sample.
3. Stored spares are maintained in serviceable condition (for example battery shelf charge, transformer storage conditions, firmware level of spare boards).
4. Below-minimum events in the period were replenished or escalated.
5. OEM-held or regional spares are contractually committed with delivery time.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Spares stock review interval | months | 6 | Illustrative. |
| Spare-to-installed ratio for accelerator trays | % of installed | Site-specific (no default) | Derived from observed failure rates, RMA turnaround and the compute availability outcome. |

**Minimum evidence**

- Spares strategy.
- Stock records and reconciliation counts.
- Storage condition records.
- Replenishment actions.
- OEM spares commitments.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; RECOVERY; DEGRADED |
| periodCoverage | 12 months of stock movement. |
| independence | Physical count by the assessor or a party independent of the stores controller. |
| mandatoryItems | Spares strategy with basis; Physical count reconciliation |
| acceptableAlternatives | Vendor-managed inventory with real-time stock visibility and audit rights. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-10, CG-05, CG-06 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Change in installed population; Lead-time change; Stock-out event; New asset class |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, RECONCILIATION, SAMPLING, ANALYSIS

**Assessment procedure**

1. Obtain strategy and stock records.
2. Check basis against population and lead times.
3. Count a sample physically.
4. Inspect storage conditions.
5. Review stock-out and replenishment records.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to critical asset classes on a restoration path; non-critical consumables follow normal stores management.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, RECOVERY

**Failure modes addressed.** Long-lead spare after rare failure (scenario X12); Spare battery string unusable through self-discharge; Spare boards at incompatible firmware; Stock recorded but not physically present

**Testing safety.** Handling of heavy spares, batteries and pressurised components follows site manual-handling and hazardous-material procedures.

**UNKNOWN rule.** Unknown stock or condition for a spare on a CG-05/06/10 restoration path is US3; US4 where the restoration-time criterion relies on it.

**Ontology classes.** Resource, AssetInstance, Safeguard · **Related controls.** MCF-CMP-022, MCF-SUP-018, MCF-DEP-021, MCF-RES-013

**Informative references.** ISO 55001 (asset management systems); IEC 60300-3-11 (reliability centred maintenance); IEEE 1188 (VRLA battery maintenance) — for stored battery spares

### MCF-SUP-018

**Lead Times** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Lead times for long-lead equipment (power transformers, MV switchgear, generators, UPS systems, chillers and dry coolers, CDUs, accelerator systems, high-speed optics, switch hardware) are known, tracked and compared with recovery and growth needs, so that both failure replacement and planned expansion are realistic.

**Requirement.** The procurement lead shall maintain current quoted and observed lead times for each long-lead equipment class, including manufacturing slot reservations and logistics time, and the capability owner shall compare each with (a) the recovery tolerance for loss of an installed unit and (b) the capacity growth schedule, recording each case where lead time exceeds tolerance or schedule with a treatment (strategic spare, slot reservation, framework order, design change) or acceptance.

**Assessment criteria**

1. Lead times are recorded per long-lead class with date and source.
2. Lead times are compared with recovery tolerances.
3. Lead times are compared with the growth schedule, including manufacturing slot reservations.
4. Exceedances have treatments or acceptance.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Lead-time refresh interval | months | 6 | Illustrative; lead times for electrical equipment can change materially within a year. |

**Minimum evidence**

- Lead-time register.
- Supplier quotations or slot reservations.
- Comparison with tolerances and schedule.
- Treatment records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T2 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; RECOVERY |
| periodCoverage | Register refreshed within interval. |
| independence | Observed lead times from recent orders corroborate quotations. |
| mandatoryItems | Lead-time register; Tolerance comparison |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-10, CG-03 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Supplier lead-time change; Growth plan change; Failure of a long-lead unit |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, RECONCILIATION

**Assessment procedure**

1. Obtain register.
2. Reconcile with recent orders.
3. Check comparisons and treatments.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to long-lead classes in the boundary.

**Lifecycle stages.** PLAN, DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, RECOVERY

**Failure modes addressed.** Transformer failure with replacement far beyond tolerance; Expansion stranded by switchgear delay (scenario X17); Accelerator delivery slips beyond commitment

**Testing safety.** Desk-based analysis.

**UNKNOWN rule.** Unknown lead time for a long-lead class on a restoration path is US3.

**Ontology classes.** Resource, Dependency, CapacityAssertion · **Related controls.** MCF-SUP-017, MCF-DEP-014, MCF-CAP-015, MCF-SUP-004

**Informative references.** ISO 55001 (asset management systems); ISO 22318 (guidelines for supply chain continuity)

### MCF-SUP-019

**Logistics Continuity** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** The logistics and labour needed for recovery and urgent replacement (heavy-haul transport and route permits for transformers and generators, port and customs clearance, cross-border movement under export controls, emergency fuel delivery, and mobilisation of specialist labour such as HV jointers, commissioning engineers, OEM field engineers and liquid-cooling technicians) can be delivered within recovery tolerance under declared regional disruption.

**Requirement.** The recovery owner shall identify the logistics and specialist-labour prerequisites for each recovery scenario involving replacement of long-lead equipment or emergency resupply, shall secure them through contracts or pre-arrangements (heavy-haul contractors, route surveys, customs brokers, export licences, fuel priority, labour call-off agreements), and shall validate them by exercise or documented precedent at the profile interval, including under at least one regional-disruption assumption.

**Assessment criteria**

1. Logistics and labour prerequisites are identified per relevant recovery scenario.
2. Pre-arrangements are in place and current.
3. Heavy-haul access to site (route survey, crane and pad locations) is documented for the largest replaceable units.
4. Validation by exercise or precedent within the interval, including a regional-disruption assumption, shows delivery within tolerance or records the gap.
5. Export-control and customs requirements for cross-border spares are pre-cleared where possible.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Logistics continuity validation interval | months | 24 | Illustrative. |

**Minimum evidence**

- Prerequisite register per scenario.
- Contracts and pre-arrangements.
- Route surveys.
- Exercise or precedent records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E6; E7 |
| qualityFloor | P4 F4 C4 R4 T3 I3 |
| sufficiencyFloor | S5 |
| stateCoverage | EMERGENCY; RECOVERY |
| periodCoverage | Validation within interval. |
| independence | Exercise facilitated by a party independent of the recovery owner. |
| mandatoryItems | Prerequisite register; Validation record |
| acceptableAlternatives | Real event precedent within interval. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-10, CG-05 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Change of logistics provider; Site access change; Export-control change; Regional event |

**Assessment methods.** DOCUMENT_REVIEW, SCENARIO_EXERCISE, INSPECTION, ANALYSIS

**Assessment procedure**

1. Obtain register and arrangements.
2. Inspect heavy-haul access provisions.
3. Review exercise including regional disruption.
4. Compare times to tolerance.

**Gate mappings.** CG-10 Recovery readiness (SUPPORTING); CG-05 Resilient electrical supply (SUPPORTING)

**Applicability.** Applies where recovery scenarios include equipment replacement or emergency resupply.

**Lifecycle stages.** PLAN, DESIGN, OPERATE · **Operating states.** EMERGENCY, RECOVERY

**Failure modes addressed.** No heavy-haul route for replacement transformer; Specialist labour unavailable regionally; Fuel deliveries deprioritised in regional emergency; Spares held at border

**Testing safety.** Exercises are tabletop or walkthrough; any physical mobilisation trial (crane, heavy-haul) requires a lift plan and permit under site rules.

**UNKNOWN rule.** Unvalidated logistics for a CG-10 restoration path is US3 for this RESILIENCE claim; US4 where the CG-10 restoration-time criterion depends on it.

**Ontology classes.** Dependency, Resource, FailureScenario, TestRecord · **Related controls.** MCF-SUP-018, MCF-POW-008, MCF-RES-011, MCF-DEP-016

**Informative references.** ISO 22301 (business continuity management systems); ISO 22318 (guidelines for supply chain continuity); ISO 28000 (supply chain security management)

### MCF-SUP-020

**End-of-Life Planning** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** End-of-sale, end-of-support and obsolescence of critical hardware, firmware and control platforms (PLCs, BMS/EPMS controllers and servers, UPS models, protection relays, accelerator generations, switch OS, storage platforms) are anticipated and managed before support or parts cease.

**Requirement.** The asset manager shall maintain a lifecycle register recording vendor end-of-sale and end-of-support dates for critical assets, shall review it at the profile interval, and shall ensure each asset reaching end-of-support within the planning horizon has an approved treatment (refresh, last-time buy, extended support, third-party support with compensating controls) recorded before the date.

**Assessment criteria**

1. Lifecycle register covers critical asset classes with vendor dates.
2. Register reviewed at the interval.
3. Assets within the planning horizon have approved treatments.
4. No critical asset is past end-of-support without an approved treatment.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Obsolescence planning horizon | months | 24 | Illustrative. |

**Minimum evidence**

- Lifecycle register.
- Vendor end-of-life notices.
- Treatment approvals.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Current; review records for 12 months. |
| independence | Vendor dates verified against vendor notices. |
| mandatoryItems | Lifecycle register |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-03 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Vendor end-of-life notice; Asset class addition |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, SAMPLING

**Assessment procedure**

1. Obtain register.
2. Verify dates against notices.
3. Check treatments for horizon assets.
4. Identify assets past end-of-support.

**Gate mappings.** CG-03 Critical dependency visibility (SUPPORTING)

**Applicability.** Applies to critical hardware, firmware and control platforms with vendor lifecycle dates; bespoke or in-house items are covered by their own lifecycle plan.

**Lifecycle stages.** PLAN, OPERATE, DECOMMISSION · **Operating states.** NORMAL

**Failure modes addressed.** BMS controllers unsupported with no spares; Unsupported PLC firmware with known vulnerabilities; Accelerator generation losing driver support

**Testing safety.** Register review only; no end-of-support device shall be taken out of service for assessment.

**UNKNOWN rule.** Unknown support status of a control-system platform is US3.

**Ontology classes.** AssetInstance, Resource, Action · **Related controls.** MCF-DEP-011, MCF-SUP-008, MCF-CAP-024

**Informative references.** IEC 62402 (obsolescence management); ISO 55001 (asset management systems)

## SUP-06 Remote support and third-party access

### MCF-SUP-021

**Support Identity** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Every person from an OEM, integrator, maintenance contractor or managed-service provider who can access facility or AI infrastructure, remotely or on site, is individually identified and authenticated; shared vendor accounts and default credentials do not exist.

**Requirement.** The security owner shall require that all third-party support access to BMS/EPMS, CDU and PLC systems, UPS and switchgear management interfaces, BMCs, cluster managers, fabric and storage controllers uses named individual identities, verified by the supplier and registered by the owner, with multi-factor authentication for remote access. Shared, generic and default vendor accounts shall be disabled or, where technically unavoidable, vaulted with per-use checkout bound to a named person and recorded as an exception.

**Assessment criteria**

1. Third-party identities are registered individually with supplier verification.
2. Account exports from in-scope systems show no active shared or default vendor accounts, or only vaulted exceptions.
3. Remote third-party authentication enforces multi-factor authentication.
4. Exceptions list technical reason, compensating control and approver.

**Minimum evidence**

- Third-party identity register.
- Account exports from sampled systems.
- MFA configuration.
- Exception records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E3; E4; E5 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Current; register changes over 12 months. |
| independence | Account exports obtained by the assessor directly or under observation. |
| mandatoryItems | Account exports from sampled control-plane systems; Third-party identity register |
| acceptableAlternatives | For devices without local account export, configuration backup files reviewed by the assessor. |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-15 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-13 require gate-level evaluation. |
| reassessmentTriggers | New supplier access; System added; Credential exposure event |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, RECONCILIATION, SAMPLING

**Assessment procedure**

1. Obtain register.
2. Export accounts from a sample of systems including facility controllers.
3. Reconcile accounts to named identities.
4. Check MFA and exceptions.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (CRITICAL); CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to every system in the boundary accessible by third parties.

**Lifecycle stages.** BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY, RECOVERY

**Failure modes addressed.** Shared vendor account used across sites; Default credentials on CDU controller; Former contractor credentials active

**Testing safety.** Account exports use read-only methods; no credentials shall be tested by login attempts against production controllers.

**UNKNOWN rule.** Inability to obtain account data from a control-plane system with third-party access is U2, US4 (CG-15 critical).

**Ontology classes.** Interface, Threat, Safeguard · **Related controls.** MCF-SEC-001, MCF-SEC-012, MCF-SUP-022, MCF-SUP-024

**Informative references.** IEC 62443-2-4 (security requirements for IACS service providers); NIST SP 800-82r3 (OT security); NIST SP 800-53 Rev. 5 (AC and MA control families); ISO/IEC 27001 (information security management systems)

### MCF-SUP-022

**Activation and Approval** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Third-party remote access to facility and AI infrastructure is off by default and is enabled only for an approved, time-limited, asset-scoped session linked to a work order or change.

**Requirement.** The facility operator shall ensure that third-party remote access paths are disabled by default and are activated only on approval by an authorised owner representative, for a stated duration and set of target assets, referencing an approved ticket or change, through a brokered access gateway. Access shall be deactivated automatically at expiry. Emergency activation shall follow a defined path with retrospective review within the profile time.

**Assessment criteria**

1. Remote access paths are disabled by default (configuration evidence).
2. Each session in the sample had prior approval, a ticket or change reference, a time limit and asset scope.
3. Sessions ended at or before expiry.
4. Emergency activations were reviewed retrospectively within the profile time.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum default session duration | hours | 4 | Illustrative. |
| Emergency activation review time | hours | 24 | Illustrative. |

**Minimum evidence**

- Gateway configuration.
- Session approval records.
- Session logs with start/end.
- Emergency review records.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | At least 3 months of sessions. |
| independence | Session logs extracted from the gateway by the assessor. |
| mandatoryItems | Session logs; Approval records |
| acceptableAlternatives |  |
| unknownEffect | US4 Critical: an UNKNOWN result on this control sets CG-15 to UNKNOWN (CG-12 trigger); the decision is capped at LIMITED or INCONCLUSIVE per the gate ceiling until the UNKNOWN Record is dispositioned. Supporting gates CG-14 require gate-level evaluation. |
| reassessmentTriggers | New remote access path; Gateway change; Unapproved session detected |

**Assessment methods.** INSPECTION, SAMPLING, RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Inspect gateway default state.
2. Sample sessions and reconcile to approvals and tickets.
3. Check expiry enforcement.
4. Review emergency activations.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (CRITICAL); CG-14 Change control (SUPPORTING)

**Applicability.** Applies where any third party has remote access to in-scope systems.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY, RECOVERY

**Failure modes addressed.** Always-on vendor VPN to BMS; Session left open after work; Remote change without ticket

**Testing safety.** Observation and log review only.

**UNKNOWN rule.** Missing session logs for a remote path to a control-plane system is U1, US4 (CG-15 critical).

**Ontology classes.** Interface, Safeguard, Event · **Related controls.** MCF-SEC-012, MCF-SUP-021, MCF-SUP-023, MCF-OPS-018

**Informative references.** IEC 62443-2-4 (security requirements for IACS service providers); NIST SP 800-82r3 (OT security); NIST SP 800-53 Rev. 5 (AC and MA control families)

### MCF-SUP-023

**Session Monitoring** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Third-party sessions on control-plane and OT systems are recorded and, for high-consequence systems, monitored in real time by a competent owner representative able to terminate the session.

**Requirement.** The security owner shall record all third-party sessions to in-scope control-plane and OT systems (keystroke or screen recording through the access broker where feasible), shall require live monitoring by a competent owner representative for sessions to systems designated high-consequence (for example EPMS switching, BMS/CDU control, protection relay configuration), and shall retain recordings for the profile period. The owner representative shall have and use the means to terminate a session.

**Assessment criteria**

1. Session recording is enabled for in-scope systems.
2. High-consequence sessions in the sample had a named live monitor.
3. Recordings are retained for the period.
4. Termination capability exists and has been exercised or tested.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Session recording retention | days | 90 | Illustrative. |

**Minimum evidence**

- Broker recording configuration.
- Session monitor records.
- Retained recordings.
- Termination test or event.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | At least 3 months. |
| independence | Assessor retrieves sample recordings directly. |
| mandatoryItems | Recording configuration; Sample recordings |
| acceptableAlternatives | Where recording is not technically feasible, continuous live supervision with a written session log. |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-15 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | New system; Recording failure; Suspicious session |

**Assessment methods.** INSPECTION, SAMPLING, OBSERVATION

**Assessment procedure**

1. Inspect broker configuration.
2. Retrieve sample recordings.
3. Check monitor assignment for high-consequence sessions.
4. Review termination evidence.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to third-party sessions on control-plane and OT systems.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Unmonitored vendor changes to CDU setpoints; No evidence after incident; Owner unable to terminate session

**Testing safety.** Termination tests use a test session on non-production systems.

**UNKNOWN rule.** No recordings for high-consequence sessions is US3.

**Ontology classes.** Event, Safeguard, EvidenceObject · **Related controls.** MCF-SUP-022, MCF-SEC-017, MCF-SEC-020

**Informative references.** IEC 62443-2-4 (security requirements for IACS service providers); NIST SP 800-82r3 (OT security)

### MCF-SUP-024

**Revocation and Review** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Third-party logical and physical access is revoked promptly when no longer needed and is periodically recertified, so that access does not outlive the person, contract or task.

**Requirement.** The security owner shall revoke third-party logical access, credentials, tokens and physical badges within the profile time of contract end, personnel departure notified by the supplier, or task completion, and shall recertify all third-party access with the owning system owner at the profile interval, removing any access not positively confirmed.

**Assessment criteria**

1. Revocations in the period met the profile time.
2. Suppliers notify personnel departures (contract obligation and evidence).
3. Recertification occurred at the interval with removals recorded.
4. Sample of current accounts all map to active contracts and people.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum revocation time after notification | hours | 24 | Illustrative. |
| Recertification interval | months | 3 | Illustrative. |

**Minimum evidence**

- Revocation records with timestamps.
- Supplier departure notifications.
- Recertification records.
- Account sample.

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E4; E5; E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | 12 months. |
| independence | Assessor samples accounts independently. |
| mandatoryItems | Recertification records; Account sample reconciliation |
| acceptableAlternatives |  |
| unknownEffect | US3 Material: an UNKNOWN result requires gate-level evaluation for CG-15, CG-13 and caps the decision at CONDITIONALLY_ASSURED with a recorded condition until resolved. |
| reassessmentTriggers | Contract end; Supplier personnel change; Recertification interval elapsed |

**Assessment methods.** SAMPLING, RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Obtain revocation and recertification records.
2. Sample accounts and badges.
3. Reconcile to active contracts and personnel.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to all third-party access.

**Lifecycle stages.** OPERATE, DECOMMISSION · **Operating states.** NORMAL

**Failure modes addressed.** Departed contractor badge active; Expired contract vendor account active

**Testing safety.** Account and badge reconciliation only; no access shall be revoked or tested by the assessor.

**UNKNOWN rule.** No recertification evidence is US3.

**Ontology classes.** Safeguard, Action, Interface · **Related controls.** MCF-SUP-021, MCF-SEC-001, MCF-PHY-013

**Informative references.** ISO/IEC 27001 (information security management systems); IEC 62443-2-4 (security requirements for IACS service providers)
