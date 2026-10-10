> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-001_Manifesto_v1.1.pdf](AIDCF-001_Manifesto_v1.1.pdf).

**AIDCF**™

**MANIFESTO**

AI Data Centre Facilities Assurance Framework

**Version 1.1**

Make AI infrastructure visible. Make dependencies explicit. Make failure propagation understandable. Make resilience demonstrable. Make assurance decisions defensible.

Author: Siva Sethumadhavan  
Artifact ID: AIDCF-001 (short code MAN)  
Status: Draft for controlled review  
Date: 2026-10-10  
Release: Release 1, Foundational Methodology

# 0. Document Profile

| **Field**                   | **Value**                                                                                                                                                                                                                              |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Artifact title**          | AIDCF Manifesto                                                                                                                                                                                                                        |
| **Artifact ID**             | AIDCF-001 (short code MAN)                                                                                                                                                                                                             |
| **Version**                 | 1.1                                                                                                                                                                                                                                    |
| **Date**                    | 2026-10-10                                                                                                                                                                                                                             |
| **Artifact type**           | Canonical foundation                                                                                                                                                                                                                   |
| **Status**                  | Draft for controlled review                                                                                                                                                                                                            |
| **Author**                  | Siva Sethumadhavan                                                                                                                                                                                                                     |
| **Intended audience**       | Data centre owners, operators, customers, engineers, security professionals, AI infrastructure teams, assessors, executives, regulators and assurance practitioners                                                                    |
| **Downstream dependencies** | AIDCF-002 Core Conceptual Model; AIDCF-003 Infrastructure Ontology and Taxonomy; AIDCF-004 Threat, Hazard and Failure Model; AIDCF-005 AIDCF–AI Trust Graph Integration Standard; AIDCF-006 Assurance Principles Standard; AIDCF-007A Control Universe and Canonical Master Control Registry; AIDCF-008 to AIDCF-019 |

## Revision history

| **Version** | **Date**   | **Summary**                                                                                                                                                                                                                                              |
|-------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | —          | Controlled-review draft of the canonical Manifesto for Release 1.                                                                                                                                                                                        |
| 1.1         | 2026-10-10 | Re-baselined Part V to the 15-domain / 90-family / 360-control model of AIDCF-007A; adopted the canonical 16-step assurance chain; public artifact IDs; defined MATERIAL; added requirement IDs and Relationship to AIDCF-002; aligned decision and gate vocabulary. |

## 0.1. Authority and precedence

This Manifesto establishes the purpose, principles, commitments and boundaries of the AI Data Centre Facilities Assurance Framework, referred to as AIDCF. It is the highest-level doctrinal artifact within the methodology.

> **MAN-REQ-001** All downstream artifacts shall remain consistent with this Manifesto.
>
> **MAN-REQ-002** Where a downstream artifact conflicts with this Manifesto, the Manifesto shall take precedence until the conflict is formally resolved through methodology governance.

## 0.2. Claims and limitations

AIDCF does not certify. This document does not:

- Certify any facility as secure, safe, sustainable or resilient.

- Replace applicable law, regulation, licence conditions, codes or contractual requirements.

- Replace licensed professional engineering, fire, life-safety or workplace-safety judgment.

- Create a legal opinion or guarantee uninterrupted service.

- Establish that an assessed organisation is free from risk.

- Authorise unsafe, destructive or operationally disruptive testing.

- Endorse a manufacturer, vendor, technology, facility or service provider.

All AIDCF conclusions are bounded by scope, intended use, evidence, conditions, assumptions, limitations and the point in time at which the assessment was performed.

## 0.3. Relationship to AIDCF-002

This Manifesto states doctrine; AIDCF-002 Core Conceptual Model gives that doctrine its canonical meanings. Terms used here (Capability Instance, Service Outcome, Required Function, Safeguard, Control, Evidence Object, UNKNOWN Record, Gate Result, Assurance Decision and MATERIAL) carry the definitions in AIDCF-002; Appendix A of this Manifesto summarises them only for readability. The canonical assurance chain in Section 14 is defined in AIDCF-002, and AIDCF-002 holds the traceability mapping from the legacy domain model to the 15 domains described in Part V. Where wording here and in AIDCF-002 differ on the meaning of a term, AIDCF-002 governs the meaning and this Manifesto governs purpose and commitments.

Contents

**Part I** The case for AIDCF

**Part II** Identity and purpose

**Part III** Foundational doctrine

**Part IV** Core principles

**Part V** Fifteen-domain architecture

**Part VI** Cross-domain assurance

**Part VII** Evidence and assessment commitments

**Part VIII** Risk, resilience and maturity

**Part IX** Relationship with AI Trust Graph

**Part X** Governance, ethics and accountability

**Part XI** Expected methodology outputs

**Part XII** Limitations and reassessment

**Part XIII** Final commitments

**Appendix A** Canonical terms used by this Manifesto

**Appendix B** Review and change records

Part I: The case for AIDCF

# 1. The infrastructure beneath artificial intelligence

Artificial intelligence is often discussed as though it exists primarily in models, algorithms, datasets and applications. It does not. Every AI capability depends upon a physical and operational foundation.

That foundation includes land, buildings, security zones, electrical and mechanical systems, cooling and coolant systems, fire systems, accelerators, compute clusters, storage, high-performance fabrics, management systems, operators, contractors, suppliers, procedures, records and tests.

An AI service may appear digital to the people who use it, but its availability and integrity remain dependent upon physical machinery, engineered systems and people. AIDCF exists to make this foundation visible and assessable.

# 2. AI infrastructure represents concentrated capability

An AI data centre may concentrate the ability to train and refine models, run large-scale inference, process sensitive information, support regulated workloads, host strategic intellectual property and deliver shared compute capacity.

Its significance cannot be measured only by floor area, rack count, installed electrical capacity or equipment value. A small physical failure may affect a disproportionately significant capability. A facility may remain electrically operational while the loss of a specialised cluster, storage service, cooling loop or network fabric makes the intended AI service unavailable.

AIDCF therefore evaluates infrastructure in the context of the capability it is intended to support.

# 3. Why traditional assessment is insufficient by itself

Existing engineering, physical-security, cybersecurity, sustainability, availability and management frameworks remain valuable. AIDCF does not displace them.

The assurance problem arises because AI data centres cross professional boundaries. Individually valid reviews may still leave integrated infrastructure risk insufficiently understood. AIDCF provides a method for examining physical, engineering, operational and AI-specific infrastructure conditions as one system.

# 4. The assurance gap

The gap is not the complete absence of standards or good practice. It is the absence of a unified assurance method that consistently connects AI capability, physical assets, engineered systems, operational dependencies, threats and failures, safeguards, evidence and accountable decisions.

Part II: Identity and purpose

# 5. What AIDCF is

AIDCF is an independent, multidisciplinary and evidence-gated assurance methodology for the facilities and infrastructure supporting AI compute.

# 6. What AIDCF is not

AIDCF is not a certification scheme, a substitute for professional engineering, regulation or accredited certification, a generic cybersecurity framework, AI-model assurance, a sustainability rating, a vendor comparison or a licence for intrusive testing.

# 7. Mission

To make AI infrastructure visible, dependencies explicit, failure propagation understandable, safeguards verifiable, resilience demonstrable and assurance decisions defensible.

# 8. Vision

AIDCF envisions an ecosystem in which critical assets are known, dependencies and assumptions are explicit, material failure paths are examined, critical safeguards are validated, operational readiness is demonstrated, evidence can be traced and uncertainty is preserved.

# 9. Central assurance question

Can the facilities and infrastructure supporting the AI capability be reasonably trusted to operate safely, securely, efficiently and resiliently within defined conditions, including credible degradation, maintenance, stress and failure scenarios?

In an individual assessment this question is made precise as the top claim of an assurance case (following the claim–argument–evidence structure of ISO/IEC/IEEE 15026-2): *Capability Instance X can achieve Service Outcomes Y within tolerances T under declared operating states S, for decision question Q, as of date D.*

Part III: Foundational doctrine

# 10. AIDCF doctrine

Identify the capability. Establish the scope. Make the infrastructure visible. Reveal the dependencies. Identify failure modes. Trace failure propagation. Validate safeguards safely. Measure evidence coverage. Preserve uncertainty. Protect critical gates. Support accountable decisions. Reassess when conditions change.

# 11. Assurance is not the presence of controls

A control may exist only on paper, be incorrectly designed, operate only in normal conditions, share a failed dependency, lack capacity, produce unactioned alarms, be bypassed, or remain untested. AIDCF distinguishes control intention, design, implementation, operation, monitoring, validation, sustainability and effectiveness under adverse conditions. These distinctions are expressed as the claim types DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS and RESILIENCE defined in AIDCF-002 and applied in AIDCF-007A.

# 12. Trust is contextual

Infrastructure trust is bounded by intended workload, criticality, capacity, operating state, facility zone, tenancy model, evidence period, architecture version, assumptions and limitations. Trust is not universal or permanent.

# 13. Infrastructure trust is a system property

Trustworthy components do not automatically create trustworthy infrastructure. Shared utility, cooling, management, maintenance, software, supplier and human dependencies may defeat apparent redundancy.

# 14. Canonical assurance chain

AIDCF reasons along one canonical chain, defined in AIDCF-002 §9 and used unchanged by every downstream artifact:

1 Decision Question → 2 Capability Instance → 3 Service Outcome → 4 Required Function → 5 Architecture (Infrastructure System / Asset / Interface) → 6 Dependency and Fault Domain → 7 Threat / Hazard / Failure Scenario → 8 Safeguard → 9 Control → 10 Evidence Requirement → 11 Evidence Object → 12 Control Assessment (result) → 13 Finding / UNKNOWN Record → 14 Gate Result → 15 Score Snapshot and Decision Recommendation → 16 Assurance Decision.

The Assurance Report and Reassessment Trigger close the loop back to step 2. Steps 1–8 build the claim and its argument (what must be true, through which functions and dependencies, against which adverse scenarios and safeguards); steps 9–13 gather and evaluate evidence and record what defeats or limits the claim; steps 14–16 turn results into a bounded, accountable conclusion.

Part IV: Core principles

# 15. Begin with the intended capability

Assessment begins by understanding what capability is supported, who depends on it, the required availability, integrity and recovery outcomes, acceptable operating conditions and intolerable consequences.

# 16. Make critical infrastructure visible

Unknown assets create unknown exposure. Sites, zones, halls, racks, compute, storage, fabrics, management systems, power, cooling, fire systems, OT, utilities, suppliers and accountable operators must be represented with sufficient reliability.

# 17. Make dependencies explicit

Dependencies may be physical, electrical, mechanical, thermal, hydraulic, digital, human, procedural, contractual, environmental, geographic, supply-chain related or time-sensitive. Direct, indirect, shared and inherited dependencies matter.

# 18. Examine failure propagation

AIDCF examines local, upstream, downstream, cascading, common-mode, common-cause, correlated, latent, sequential, compound, degraded-state, maintenance-induced and recovery failures.

# 19. Distinguish redundancy from resilience

Redundancy is additional capacity or paths. Resilience is the demonstrated ability to continue, contain, adapt and recover. Shared dependencies, inadequate capacity, untested transfer and common configuration can make redundancy ineffective.

# 20. Validate safely

Testing must be authorised, competent and proportionate. Where live testing is unsafe, justified alternatives may include commissioning records, witnessed tests, historical events, approved simulations, engineering analysis and tabletop exercises.

# 21. Preserve provenance

Material evidence should identify source, custodian, method, date, system, version, conditions, reviewer, limitations and related assertion.

# 22. Preserve UNKNOWN

Missing evidence is not proof of effectiveness or failure. UNKNOWN remains a valid control result and is recorded as an UNKNOWN Record with a type and severity; it must not be silently converted into a score, pass, failure or assumption. A MATERIAL UNKNOWN constrains the decision rather than disappearing from it.

# 23. Separate evidence quality from confidence

The methodology distinguishes source quality, relevance, currency, coverage, consistency, independence and conclusion confidence. Evidence quality and sufficiency are rated under AIDCF-008; confidence is expressed separately on the CONF-0 to CONF-4 scale.

# 24. Protect critical gates

Life safety, resilient electrical supply, thermal continuity, control-system integrity, recovery readiness, evidence sufficiency and other non-compensable conditions may cap the assurance conclusion regardless of strong average performance. AIDCF defines fifteen critical gates (CG-01 to CG-15); their criteria, roll-up and decision ceilings are specified in AIDCF-010. A gate result is PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED; there is no conditional gate result.

# 25. Separate maturity from assurance

Maturity indicates institutionalised capability. Assurance indicates confidence in a defined claim under defined conditions. Neither substitutes for the other.

# 26. Report profiles, not false precision

Reporting preserves domain condition, critical gates, evidence coverage, design adequacy, operating effectiveness, failure paths, maturity, residual exposure, confidence and UNKNOWN conditions.

# 27. Evaluate all relevant operating states

Normal, degraded, maintenance, emergency, recovery and transition states may create different exposure. State transitions require explicit consideration.

# 28. Treat people and procedures as dependencies

Competency, staffing, shift coverage, authorisation, decision rights, work control, vendors, emergency response, fatigue and knowledge concentration affect resilience.

# 29. Maintain independence and professional humility

Assessors work within competence, disclose conflicts, distinguish fact from judgment, preserve dissent, identify limitations and refuse unsafe activities.

Part V: Fifteen-domain architecture

AIDCF organises assessment work into fifteen domains, each with six control families and four controls per family: 15 domains, 90 families and 360 controls in the Canonical Master Control Registry of AIDCF-007A. This structure supersedes the earlier eight-domain model; the legacy-to-15 mapping is kept in AIDCF-002 Part X for traceability only.

The domains organise work; they do not divide the infrastructure into isolated risk silos. A single failure path routinely crosses several domains (for example, a firmware change in a coolant distribution unit controller crosses SUP, SEC, THM and CMP), and Part VI requires such paths to be reasoned end to end. Each domain guide in AIDCF-018 defines scope, exclusions, concepts, failure modes, control families, evidence expectations, safe validation and cross-domain mappings.

The domains fall into three groups:

| **Group**                         | **Domains**                    | **Role in the chain**                                                                                   |
|-----------------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------|
| Direction and definition          | GOV, CAP, DEP                  | Who decides, what capability and outcomes are required, and what the capability relies upon.           |
| Infrastructure                    | PHY, POW, THM, ENV, CMP, STO, NET | The engineered and technical systems that implement Required Functions.                             |
| Operation, resilience and assurance | OPS, RES, SUP, SEC, EVA      | How the infrastructure is run, recovered, supplied, protected and assured.                            |

# 30. GOV — Governance, Accountability and Assurance Direction

Whether assurance is directed, owned and decided by people with defined authority, and whether policy, risk appetite, exceptions and independent review are governed.

## Primary concerns

- Governance charter, decision rights, committee oversight and methodology ownership

- Role ownership, accountability for Required Functions, risk-acceptance authority and evidence custody

- Policy hierarchy, technical-standard baselines, exception governance and document lifecycle

- Assurance planning, risk-appetite linkage, critical-gate governance and independent review

- Stakeholder, regulatory and customer obligations, and external reporting

- Conflict management, assessor independence, competence and appeal

## Central assurance question

Does every material function, dependency, risk acceptance and assurance decision have an accountable owner with defined authority, exercised independently of commercial or management pressure?

# 31. CAP — AI Capability, Service Outcome and Demand Management

Whether the AI capability is defined precisely enough, in outcomes, tolerances, demand and operating envelope, that its supporting infrastructure can be assessed against it.

## Primary concerns

- Capability register, ownership, lifecycle status and architecture linkage

- Availability, performance, integrity and recovery outcomes

- Criticality criteria, impact tolerance and stakeholder consequence

- Current, peak and transient demand, including the rapid power and heat swings of synchronous accelerator workloads, and growth scenarios

- Operating envelope: load, environmental, duration and state-specific limits

- Design-to-operation traceability, commissioning acceptance, material-change impact and retirement

## Central assurance question

Is the Capability Instance defined, owned and bounded so that each Service Outcome, tolerance and demand profile can be traced to the infrastructure that must deliver it?

# 32. DEP — Dependency, Concentration and External Reliance Management

Whether material dependencies, including those outside the assessment boundary and those shared by nominally independent paths, are known, owned and monitored.

## Primary concerns

- Asset-to-function, upstream, downstream-consequence and recovery dependency mapping

- Shared sources, common controllers, shared routes and shared human dependencies

- Utility, telecommunications, OEM, cloud and service-provider dependencies

- Capacity, supplier and knowledge concentration, and substitution readiness

- Assessment, provider and tenant boundaries and cross-boundary enforcement

- Dependency health indicators, provider performance, change detection and periodic revalidation

## Central assurance question

Which dependencies, if lost, would defeat a Service Outcome, and are any of them shared by paths that are claimed to be independent?

# 33. PHY — Physical Site, Building and Security Infrastructure

Whether the site and building can physically host the intended AI infrastructure, and whether physical security and life-safety arrangements protect it against unauthorised access, interference, removal, sabotage, fire and site hazards.

## Primary concerns

- Site hazard, external exposure, access and logistics, and adjacent risk

- Structural capacity, rack loading of dense rack-scale systems, anchorage, vibration and building envelope

- Security, fire and water zoning, and tenant segregation

- Identity-based physical access, visitor control, surveillance coverage and alarm response

- Delivery controls, equipment movement, media custody and decommissioning custody

- Fire detection, suppression interfaces, egress, emergency access and emergency-shutdown governance

## Central assurance question

Can the building safely carry and protect the AI infrastructure, and can a person physically access, interfere with, remove or disrupt it without appropriate prevention, detection, attribution and response?

# 34. POW — Electrical Power Infrastructure and Energy Continuity

Whether electrical supply, generation, energy storage, distribution and protection sustain safe AI compute operation under demand, maintenance, degradation and failure.

## Primary concerns

- Utility capacity, grid quality, connection reliability and utility contingency

- Generator capacity, start reliability, fuel autonomy and fuel replenishment

- UPS topology, battery condition, runtime and derating, and bypass exposure

- Switchgear integrity, selective coordination, busway and PDU capacity, earthing and bonding

- Voltage quality, harmonics, transient ride-through and load-step response to accelerator workloads

- EPMS coverage, preventive maintenance, switching procedures, black start and restoration

## Central assurance question

Can the electrical system deliver sufficient power of adequate quality to the AI load across normal, maintenance, degraded and recovery states, including load transients, and restore it safely after loss?

# 35. THM — Cooling, Thermal and Fluid Infrastructure

Whether heat can be removed from accelerators and rejected to atmosphere, through air and liquid paths, with sufficient margin across operating states.

## Primary concerns

- Heat-load model, design capacity, resilient capacity and seasonal derating

- Airflow management, containment, CRAH and in-row capacity, and air-side monitoring

- Direct-to-chip architecture, coolant distribution unit capacity, secondary-loop integrity and quick-disconnect management

- Chillers, cooling towers or dry coolers, water continuity and heat-rejection dependency

- Coolant compatibility, water quality, leak detection, isolation and drainage

- Control stability, sensor trust, maintenance states and thermal recovery

## Central assurance question

Can the heat-removal path keep accelerators within their thermal limits through transients, component failure, maintenance and loss of facility water, before throttling or protective shutdown defeats the Service Outcome?

# 36. ENV — Environmental and Resource Performance

Whether environmental conditions, resource use and sustainability claims are governed, measured and evidenced without undermining intended resilience.

## Primary concerns

- Temperature, humidity, particulate and corrosion, vibration and acoustic conditions

- Energy-performance measurement (such as PUE), energy allocation, efficiency under load and resilience–efficiency trade-offs

- Water source and quality, WUE measurement, water-scarcity response and discharge control

- Carbon-accounting boundary, energy-attribute evidence, embodied-resource data and reporting traceability

- Battery materials, refrigerants and coolants, fuel and suppressant handling, hardware and media waste

- Heatwave, drought and flood readiness, and long-term resource constraints

## Central assurance question

Can the facility demonstrate responsible, accurately reported resource use and maintain the environmental conditions the infrastructure requires, without trading away resilience?

# 37. CMP — AI Compute Infrastructure

Whether accelerator-based compute is appropriately designed, configured, observed, maintained and recoverable.

## Primary concerns

- Accelerator architecture, node configuration, rack-scale composition and approved baselines

- Cluster topology, scale-up domain integrity, partitioning and fault-domain design

- Usable accelerator capacity, scheduler controls, resource reservation and contention management

- Firmware baselines, driver compatibility, upgrade testing and rollback readiness

- GPU telemetry, node health, error and degradation detection, and performance baselines

- Provisioning, spares and RMA, node rebuild and secure retirement

## Central assurance question

Can accelerator infrastructure reliably provide the required usable compute while containing faults and supporting recovery?

# 38. STO — AI Storage and Data Infrastructure

Whether datasets, model artifacts and checkpoints have the required availability, integrity, capacity, throughput and recoverability.

## Primary concerns

- Training-data, checkpoint, model-and-artifact and archive tiers

- Throughput and IOPS, metadata performance, capacity headroom and burst handling

- Data and metadata integrity, checksumming and scrubbing, configuration consistency

- Snapshots, replication, erasure coding and immutable recovery copies

- Checkpoint durability, restart readiness, storage recovery sequencing and recovery validation

- Storage telemetry, capacity forecasting, media health and secure sanitisation

## Central assurance question

Can storage infrastructure reliably supply, retain, protect and recover the data and artifacts the AI capability requires, at the throughput it requires?

# 39. NET — AI Network and Interconnect Architecture

Whether compute, storage, management and external connectivity are supported by isolated, observable, performant and resilient fabrics.

## Primary concerns

- Scale-up and scale-out fabric topology, path diversity, oversubscription and fabric fault-domain design

- Latency baselines, loss and retransmission, congestion control and collective-communication performance

- Storage fabric, frontend network, service gateways and traffic isolation

- Management separation, console access, out-of-band resilience and break-glass access

- Cabling standards, optics compatibility, cross-connect control and path documentation

- Controller resilience, configuration management, flow telemetry, time and core services

## Central assurance question

Can AI infrastructure communicate at the required scale and performance while maintaining isolation, visibility and resilience, including when the management network is itself degraded?

# 40. OPS — Building Operations and Service Management

Whether operating governance, personnel, procedures, maintenance and service operations preserve the facility design in practice.

## Primary concerns

- 24x7 coverage, role clarity, shift handover, competence and authorisation

- Standard operating procedures, method statements, permit to work, lockout and tagout

- Maintenance strategy, condition monitoring, calibration and deferred maintenance

- Alarm rationalisation, incident response, root-cause analysis and problem elimination

- Configuration baselines, change assessment, temporary configurations, rollback and validation

- Capacity review, service-level monitoring, resource balancing and operational reporting

## Central assurance question

Can the organisation operate, maintain and change the facility consistently without unacceptable human, procedural or configuration risk?

# 41. RES — Resilience, Continuity and Recovery

Whether failure is contained within declared fault domains and the capability can continue in degraded form and be restored within tolerance, as demonstrated rather than planned.

## Primary concerns

- Minimum service outcome, graceful degradation, resilience scenarios and resilience ownership

- Fault-domain definition, containment boundaries, blast radius and isolation validation

- Continuity strategy, alternative capacity, site and provider continuity, crisis priorities

- Recovery dependencies, recovery sequencing, configuration restoration, data and checkpoint recovery

- Component tests, integrated scenario tests, tabletop exercises, lessons and retest

- Crisis command, stakeholder communications, emergency change and post-event adaptation

## Central assurance question

When a credible failure occurs, does it stay within its fault domain, and has restoration of the Service Outcome within tolerance been demonstrated?

# 42. SUP — Supply Chain, OEM and Ecosystem Assurance

Whether suppliers, OEMs, components, firmware and third-party access can be relied upon for the capability's lifetime.

## Primary concerns

- Supplier capability, financial and operational resilience, security and quality posture, sub-tier visibility

- Service levels, evidence rights, incident notification, exit and transition rights

- Approved sourcing, counterfeit prevention, chain of custody and component traceability

- Release provenance, signature validation, compatibility assurance and vulnerability response for software and firmware

- Critical spares, lead times, logistics continuity and end-of-life planning

- Support identity, activation and approval, session monitoring, revocation and review for remote support

## Central assurance question

Can the capability be built, maintained, updated and repaired with trustworthy components and support, and can a supplier failure or compromise be absorbed?

# 43. SEC — Digital, OT and Control-Plane Security

Whether identity, privilege and control-plane reach over facility and AI infrastructure are bounded, monitored and recoverable.

## Primary concerns

- Human and machine identity, privileged access and break-glass governance

- Security of BMS and EPMS, cluster managers, fabric controllers and storage controllers

- Security zoning (including zones and conduits in the sense of IEC 62443), management-plane segmentation, filtering and gateways, remote access

- Secure baselines, vulnerability management, patch governance and compensating controls

- Security telemetry, behaviour detection, incident containment and forensic readiness

- Authority, approval, command allowlisting and safe rollback for AI-enabled and automated action

## Central assurance question

Who and what can digitally observe, configure or command the facility and the AI infrastructure, and is that reach bounded, monitored and recoverable?

# 44. EVA — Evidence, Assessment and Assurance Management

Whether the assurance conclusion is traceable to sufficient evidence, with UNKNOWNs, conflicts and limitations preserved, gates evaluated and the decision independently made and kept current.

## Primary concerns

- Evidence taxonomy, ownership, repository, retention and protection

- Source provenance, integrity and custody, relevance and reliability, currency and coverage

- Decision question, scope and criteria, sampling and testing, specialist involvement

- Finding traceability, UNKNOWN preservation, conflict handling and limitation disclosure

- Gate applicability, gate evidence, independent decision and claim language

- Evidence expiry, change triggers, monitoring coverage, decision suspension and supersession

## Central assurance question

Could an independent reviewer reconstruct the Assurance Decision from the recorded evidence, results, findings, UNKNOWN Records and gate results, and would they reach the same bounded conclusion?

Part VI: Cross-domain assurance

# 45. Domains must not become silos

A material event may originate in one domain and propagate through several others. AIDCF therefore requires integrated failure-path reasoning, not isolated control aggregation.

# 46. Cross-domain finding record

A material cross-domain finding identifies the initiating condition, originating and contributing domains, affected capability and assets, dependency chain, control breakpoints, observed safeguards, evidence, confidence, consequence, containment, remediation and retest.

# 47. Common-mode dependencies

Utility, fuel, coolant, control platforms, management services, authentication, suppliers, routes, software, spares, teams and procedures may be shared by systems represented as independent. Redundancy claims must be examined for these dependencies.

Part VII: Evidence and assessment commitments

# 48. Evidence classes

Evidence may include approved design and as-built documents, diagrams, studies, commissioning and maintenance records, alarms, incidents, access and surveillance records, telemetry, work orders, procedures, competencies, contracts, attestations, observation, interviews, samples, simulations and exercises. AIDCF-008 classifies these as evidence classes E1 (documentary and declarative) to E7 (derived and analytical).

# 49. Evidence hierarchy

Evidence strength is evaluated through directness, authenticity, relevance, currency, completeness, independence, repeatability, context, coverage and corroboration. AIDCF-008 rates these through quality dimensions, quality bands Q0–Q5 and sufficiency levels S0–S5.

# 50. Evidence conflict

Conflicting evidence is recorded, evaluated and disclosed. Unresolved conflict limits confidence and remains visible.

# 51. Safe validation hierarchy

Validation ranges from inspection and interview to analysis, historical evidence, witnessed routine tests, controlled functional tests, simulation, tabletop exercises and integrated recovery tests. Selection remains proportionate to safety and authority.

# 52. Prohibited validation behaviour

Assessments must not disable life safety, interrupt critical service without authority, exceed operating limits, bypass safety procedure, alter production without change control, create hazardous conditions or misrepresent simulation as live evidence.

Part VIII: Risk, resilience and maturity

# 53. Risk classes

AIDCF recognises threat, hazard, engineering failure, operational, supply-chain, capacity and concentration, and recovery risk. These classes may interact and produce compound consequence. AIDCF-004 defines their semantics.

# 54. Resilience lifecycle

AIDCF evaluates the ability to anticipate, prevent, detect, contain, recover and adapt.

# 55. Maturity doctrine

AIDCF-017 Capability Assurance Maturity Model defines maturity levels and criteria. Maturity does not override critical gates, replace engineering analysis, prove resilience, demonstrate compliance or convert UNKNOWN into confidence.

Part IX: Relationship with AI Trust Graph

# 56. Complementary purpose

AIDCF addresses facilities and infrastructure assurance. AI Trust Graph addresses relationships, authority, reachability, dependencies and controls within the AI ecosystem.

# 57. Primary AIDCF boundaries

AIDCF primarily owns site, building, physical security, power, cooling, environmental performance, building operations, AI compute hardware, supporting storage, high-performance networking, facility OT, control-plane security over infrastructure and physical infrastructure dependencies.

# 58. Primary AI Trust Graph boundaries

AI Trust Graph primarily owns models, agents, tools, APIs, human and machine identities as trust subjects, authority, trust relationships, data reachability, action paths and emergent digital consequence.

# 59. Shared-boundary handling

Where an infrastructure component also participates in a digital trust path, the frameworks contribute distinct perspectives. AIDCF-005 establishes the handoff, shared-identity and joint-finding rules.

Part X: Governance, ethics and accountability

# 60. Intended users

AIDCF supports owners, operators, providers, customers, engineering and security teams, risk functions, independent assessors, boards, regulators and policymakers. Tailored use must be disclosed.

# 61. Competency model

A comprehensive assessment may require physical security, electrical, mechanical, cooling, fire and life safety, structural, OT, cybersecurity, AI compute, storage, HPC networking, sustainability, continuity and assurance expertise.

# 62. Independence

Conclusions should be protected from commercial pressure, vendor influence, management override, artificial score targets and pressure to remove UNKNOWN or conceal limitations.

# 63. Responsible claims

Reports distinguish observation, verified fact, judgment, engineering opinion, management or vendor assertion, assumption, limitation, UNKNOWN and recommendation.

# 64. Confidentiality

Facility layouts, security controls, power, cooling, management networks, failure paths and supplier dependencies require lawful collection, classification, access control, secure retention and controlled disclosure.

# 65. Intellectual property boundary

Products may operationalise the methodology through workflow, evidence management, visualisation, testing, scoring and reporting.

> **MAN-REQ-003** Tooling shall not silently redefine canonical doctrine, terms, vocabularies or decision rules.

# 66. Change governance

Changes are proposed, impact-classified, consistency-reviewed, version-controlled, approved, logged and propagated to dependent artifacts.

Part XI: Expected methodology outputs

# 67. Assessment outputs

Outputs may include charter, scope, facility and capability profiles, asset and dependency registers, maps, evidence register, Control Assessment results and Gate Results, threat and failure analyses, scenario and test records, domain and maturity profiles, Findings, UNKNOWN Records, decisions, roadmap, reassessment plan and report annexes.

# 68. Decision outcomes

AIDCF supports decisions about facility suitability, design progression, commissioning sufficiency, operational readiness, expansion risk, failure-path remediation, resilience evidence, risk treatment and reassessment. An Assurance Decision takes one of five states: REASONABLY_ASSURED, CONDITIONALLY_ASSURED, LIMITED, NOT_ASSURED or INCONCLUSIVE (AIDCF-010). Accountability for acting on the decision remains with the organisation.

Part XII: Limitations and reassessment

# 69. Point-in-time limitation

Confidence may change after capacity, hardware, network, cooling, power, control-system, supplier, staffing, regulatory or operational changes. Trust requires maintenance and reassessment.

# 70. Reassessment triggers

Potential triggers include new construction, major design change, high-density compute, liquid cooling, utility changes, redundancy changes, significant incident, failed recovery, supplier change, newly available evidence and completion of material remediation.

Part XIII: Final commitments

# 71. AIDCF commitments

1.  The methodology remains understandable without proprietary software.

2.  Documented intention is distinguished from demonstrated effectiveness.

3.  Uncertainty is preserved rather than converted into manufactured confidence.

4.  Critical failures are not concealed by averaging.

5.  Tests are proportionate, authorised and safe.

6.  Conclusions are traceable to evidence.

7.  Scope, assumptions and limitations remain visible.

8.  Maturity is not presented as a substitute for assurance.

9.  Engineering judgment is respected and appropriately bounded.

10. Cross-domain dependencies are examined rather than assigned away.

11. AIDCF complements AI Trust Graph rather than duplicating it.

12. The methodology evolves through controlled governance and independent review.

# 72. Final doctrine

Artificial intelligence is not sustained by software alone. It depends upon buildings, electrical systems, cooling systems, networks, machines, people, suppliers and procedures operating as an interconnected whole.

Infrastructure that is invisible cannot be adequately governed. Dependencies that are unknown cannot be reliably protected. Redundancy that is not examined cannot be assumed to provide resilience. Resilience that has not been demonstrated cannot be treated as assured. Evidence that is incomplete cannot justify unconditional confidence.

Identify the AI capability. Make the infrastructure visible. Reveal the dependencies. Understand credible failure. Trace propagation and consequence. Validate safeguards safely. Protect critical gates. Preserve evidence and uncertainty. Report without false precision. Enable defensible decisions. Reassess when the system changes.

Appendix A: Canonical terms used by this Manifesto

Definitions are summarised from AIDCF-002, which is authoritative.

| **Term**                   | **Canonical meaning**                                                                                                                                                                                                                                                       |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Capability Instance**    | A specific AI capability deployment bounded by ownership, location, architecture, capacity, criticality and obligations; the primary assurance object.                                                                                                                      |
| **Service Outcome**        | A measurable or assessable result required from a Capability Instance, with stated tolerances.                                                                                                                                                                              |
| **Required Function**      | A function whose loss or degradation would materially affect a Service Outcome (for example heat removal, power continuity, checkpoint persistence).                                                                                                                       |
| **Asset**                  | A physical, technical, environmental, human or procedural element relevant to the intended capability.                                                                                                                                                                      |
| **Dependency**             | A condition, asset, service, person or relationship required for another element to operate as intended.                                                                                                                                                                    |
| **Failure mode**           | A defined manner in which an asset, control, process or dependency may fail.                                                                                                                                                                                                |
| **Propagation path**       | The sequence through which an initiating condition produces effects across assets or domains.                                                                                                                                                                               |
| **Safeguard**              | A real-world preventive, detective, containing, recovery or adaptive measure intended to modify risk or consequence.                                                                                                                                                       |
| **Control**                | An assessable requirement in the AIDCF-007A registry against which a Safeguard is evaluated; a control is not itself the protective measure.                                                                                                                                |
| **Critical gate**          | A non-compensable condition (CG-01 to CG-15) whose Gate Result of FAIL or UNKNOWN caps the Assurance Decision.                                                                                                                                                             |
| **Evidence coverage**      | The extent to which relevant scope, time, conditions and assertions are supported by evidence.                                                                                                                                                                              |
| **UNKNOWN**                | A preserved result used where evidence is insufficient to reach a defensible conclusion; recorded as an UNKNOWN Record with type and severity.                                                                                                                             |
| **MATERIAL**               | (AIDCF-002 §22) A fact, dependency, condition, deficiency or UNKNOWN is material if, had it been known or resolved differently, a competent assessor would reasonably expect it to change a control result, a gate result, the decision state, or a condition, limitation or ceiling attached to the decision, for the declared Capability Instance, Service Outcomes and operating states. |
| **Assurance Decision**     | A bounded, accountable conclusion in one of the states REASONABLY_ASSURED, CONDITIONALLY_ASSURED, LIMITED, NOT_ASSURED or INCONCLUSIVE, supported by defined evidence, analysis and limitations.                                                                           |
| **Operating state**        | A defined facility condition: NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION, SHUTDOWN, FAILED or UNKNOWN.                                                                                                                                                  |
| **Common-mode dependency** | A shared dependency capable of defeating supposedly independent systems or paths.                                                                                                                                                                                           |

Appendix B: Review and change records

# Review record

No approval has been granted for this document. The record below states review status only.

| **Review role**                        | **Status**                               |
|----------------------------------------|------------------------------------------|
| Methodology author, Siva Sethumadhavan | Draft completed                          |
| Chief product architecture review      | Internal author review pending           |
| Data-centre engineering review         | Independent review pending               |
| Electrical engineering review          | Independent review pending               |
| Mechanical and cooling review          | Independent review pending               |
| Physical-security review               | Independent review pending               |
| Fire and life-safety review            | Independent review pending               |
| AI compute and HPC review              | Independent review pending               |
| OT-security review                     | Independent review pending               |
| Assurance-method review                | Independent review pending               |
| Employer and IP review                 | Pending                                  |
| Confidentiality review                 | Pending                                  |
| Legal and claims review                | Pending                                  |
| Licence and trademark review           | Pending                                  |
| Public release                         | Not approved until mandatory gates close |

# Change record

| **Version** | **Date**   | **Status**                  | **Summary**                                                                                                  |
|-------------|------------|-----------------------------|--------------------------------------------------------------------------------------------------------------|
| 0.1         | —          | Initial concept             | Established the initial purpose and domain concept.                                                         |
| 0.2         | —          | Expanded draft              | Added assurance doctrine, boundaries and integration principles.                                            |
| 1.0         | —          | Controlled-review draft     | Established the comprehensive canonical Manifesto for Release 1.                                            |
| 1.1         | 2026-10-10 | Draft for controlled review | 15-domain re-baseline, canonical chain, public IDs, MATERIAL, requirement IDs, decision and gate vocabulary. |

# Manifesto acceptance criteria

- Purpose is clearly differentiated from conventional data-centre standards.

- The fifteen domains, their boundaries and their mapping to AIDCF-007A families are stable.

- Relationship with AI Trust Graph is unambiguous.

- Public and proprietary boundaries are accepted.

- Evidence, UNKNOWN and critical-gate doctrines are retained.

- Safety and engineering limitations are explicit.

- No section prematurely defines downstream controls.

- Independent expert, IP, confidentiality and publication reviews are recorded.
