> Markdown edition. Source: [AIDCF_Manifesto_v1.0.docx](AIDCF_Manifesto_v1.0.docx) · PDF: [AIDCF_Manifesto_v1.0.pdf](AIDCF_Manifesto_v1.0.pdf)

**AIDCF**™

**MANIFESTO**

AI Data Centre Facilities Assurance Framework

**Version 1.0**

Make AI infrastructure visible. Make dependencies explicit. Make failure propagation understandable. Make resilience demonstrable. Make assurance decisions defensible.

Author: Siva Sethumadhavan  
Artifact ID: AIDCF-MAN-001  
Status: Draft for controlled review  
Release: Release 1, Foundational Methodology

# 0. Document Profile

| **Artifact title**          | AIDCF Manifesto                                                                                                                                                                                       |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Version**                 | 1.0                                                                                                                                                                                                   |
| **Artifact ID**             | AIDCF-MAN-001                                                                                                                                                                                         |
| **Artifact type**           | Canonical foundation                                                                                                                                                                                  |
| **Status**                  | Draft for controlled review                                                                                                                                                                           |
| **Author**                  | Siva Sethumadhavan                                                                                                                                                                                    |
| **Intended audience**       | Data centre owners, operators, customers, engineers, security professionals, AI infrastructure teams, assessors, executives, regulators and assurance practitioners                                   |
| **Downstream dependencies** | Core Conceptual Model; Infrastructure Ontology and Taxonomy; Threat, Hazard and Failure Model; AIDCF-AI Trust Graph Integration Standard; domain guides; controls; assessment and reporting artifacts |

## 0.1. Authority and precedence

This Manifesto establishes the purpose, principles, commitments and boundaries of the AI Data Centre Facilities Assurance Framework, referred to as AIDCF. It is the highest-level doctrinal artifact within the methodology. All downstream artifacts shall remain consistent with it.

Where a downstream artifact conflicts with this Manifesto, the Manifesto takes precedence until the conflict is formally resolved through methodology governance.

## 0.2. Claims and limitations

This document does not:

- Certify any facility as secure, safe, sustainable or resilient.

- Replace applicable law, regulation, licence conditions, codes or contractual requirements.

- Replace licensed professional engineering, fire, life-safety or workplace-safety judgment.

- Create a legal opinion or guarantee uninterrupted service.

- Establish that an assessed organisation is free from risk.

- Authorise unsafe, destructive or operationally disruptive testing.

- Endorse a manufacturer, vendor, technology, facility or service provider.

All AIDCF conclusions are bounded by scope, intended use, evidence, conditions, assumptions, limitations and the point in time at which the assessment was performed.

Contents

**Part I** The case for AIDCF

**Part II** Identity and purpose

**Part III** Foundational doctrine

**Part IV** Core principles

**Part V** Eight-domain architecture

**Part VI** Cross-domain assurance

**Part VII** Evidence and assessment commitments

**Part VIII** Risk, resilience and maturity

**Part IX** Relationship with AI Trust Graph

**Part X** Governance, ethics and accountability

**Part XI** Expected methodology outputs

**Part XII** Limitations and reassessment

**Part XIII** Final commitments

**Appendix A** Canonical terms introduced by this Manifesto

**Appendix B** Approval and change records

Part I: The case for AIDCF

# 1. The infrastructure beneath artificial intelligence

Artificial intelligence is often discussed as though it exists primarily in models, algorithms, datasets and applications. It does not. Every AI capability depends upon a physical and operational foundation.

That foundation includes land, buildings, security zones, electrical and mechanical systems, cooling and coolant systems, fire systems, accelerators, compute clusters, storage, high-performance fabrics, management systems, operators, contractors, suppliers, procedures, records and tests.

An AI service may appear digital to its users, but its availability and integrity remain dependent upon physical machinery, engineered systems and people. AIDCF exists to make this foundation visible and assessable.

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

AIDCF is not a substitute for professional engineering, regulation, accredited certification, a generic cybersecurity framework, AI-model assurance, a sustainability rating, a vendor comparison or a licence for intrusive testing.

# 7. Mission

To make AI infrastructure visible, dependencies explicit, failure propagation understandable, safeguards verifiable, resilience demonstrable and assurance decisions defensible.

# 8. Vision

AIDCF envisions an ecosystem in which critical assets are known, dependencies and assumptions are explicit, material failure paths are examined, critical safeguards are validated, operational readiness is demonstrated, evidence can be traced and uncertainty is preserved.

# 9. Central assurance question

Can the facilities and infrastructure supporting the AI capability be reasonably trusted to operate safely, securely, efficiently and resiliently within defined conditions, including credible degradation, maintenance, stress and failure scenarios?

Part III: Foundational doctrine

# 10. AIDCF doctrine

Identify the capability. Establish the scope. Make the infrastructure visible. Reveal the dependencies. Identify failure modes. Trace failure propagation. Validate safeguards safely. Measure evidence coverage. Preserve uncertainty. Protect critical gates. Support accountable decisions. Reassess when conditions change.

# 11. Assurance is not the presence of controls

A control may exist only on paper, be incorrectly designed, operate only in normal conditions, share a failed dependency, lack capacity, produce unactioned alarms, be bypassed, or remain untested. AIDCF distinguishes control intention, design, implementation, operation, monitoring, validation, sustainability and effectiveness under adverse conditions.

# 12. Trust is contextual

Infrastructure trust is bounded by intended workload, criticality, capacity, operating state, facility zone, tenancy model, evidence period, architecture version, assumptions and limitations. Trust is not universal or permanent.

# 13. Infrastructure trust is a system property

Trustworthy components do not automatically create trustworthy infrastructure. Shared utility, cooling, management, maintenance, software, supplier and human dependencies may defeat apparent redundancy.

# 14. Canonical reasoning chain

AI capability -\> service requirement -\> supporting asset -\> dependency -\> threat, hazard or failure -\> propagation path -\> consequence -\> safeguard -\> evidence -\> residual exposure -\> assurance decision.

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

Missing evidence is not proof of effectiveness or failure. UNKNOWN remains a valid result state and must not be silently converted into a score, pass, failure or assumption.

# 23. Separate evidence quality from confidence

The methodology distinguishes source quality, relevance, currency, coverage, consistency, independence and conclusion confidence.

# 24. Protect critical gates

Life safety, essential cooling, standby power, critical access, recovery capability and other non-compensable conditions may cap the assurance conclusion regardless of strong average performance.

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

Part V: Eight-domain architecture

The domains organise assessment work but do not divide the infrastructure into isolated risk silos. Each domain guide will define scope, exclusions, concepts, failure modes, control families, evidence expectations, safe validation and cross-domain mappings.

# 30. Domain 1: Physical Data Centre Controls

Whether physical security arrangements protect critical AI infrastructure against unauthorised access, interference, removal, sabotage and other physical threats.

## Primary concerns

- Site and perimeter security

- Vehicle, loading and delivery controls

- Identity and physical access

- Security zoning and critical-area protection

- Surveillance and intrusion detection

- Visitor and contractor management

- Asset movement and chain of custody

- Insider-risk safeguards

- Security operations, response and reconstruction

## Central assurance question

Can a person physically access, interfere with, remove or disrupt critical AI infrastructure without appropriate prevention, detection, attribution and response?

# 31. Domain 2: Facilities Engineering

Whether structural, electrical, mechanical, fire-protection and control-system design is suitable for the intended AI infrastructure and operating conditions.

## Primary concerns

- Design basis and engineering authority

- Structural and rack loading

- Space planning and maintainability

- Electrical and mechanical architecture

- Fire detection and suppression

- Water and leak management

- BMS, EPMS and operational technology

- Commissioning and engineering change

## Central assurance question

Is the facility engineered, commissioned and maintained to support the physical characteristics, density and failure behavior of the intended AI infrastructure?

# 32. Domain 3: Power and Cooling Resilience

Whether power and thermal systems sustain safe AI compute operation under demand, maintenance, degradation and failure.

## Primary concerns

- Utility capacity and diversity

- Electrical distribution, UPS and batteries

- Standby generation and fuel

- Rack power

- Air and liquid cooling

- CDUs, pumps and heat exchangers

- Leak and thermal detection

- Capacity reserve, failover and restoration

- Integrated resilience testing

## Central assurance question

Can the facility preserve safe and sufficient electrical and thermal conditions throughout credible disruptions and recovery scenarios?

# 33. Domain 4: Environmental Standards and Resource Performance

Whether resource use, environmental performance and sustainability claims are governed, measured and evidenced.

## Primary concerns

- Obligations register

- Energy management and PUE

- Water use and WUE

- Carbon and green-energy claims

- Equipment efficiency and compute utilisation

- Higher-temperature operation

- Refrigerants and hazardous materials

- Waste, lifecycle and reporting integrity

## Central assurance question

Can the facility demonstrate responsible and efficient resource use without undermining intended resilience?

# 34. Domain 5: Building Operations

Whether operating governance, personnel, procedures, maintenance and emergency capability preserve the facility design.

## Primary concerns

- Accountability and procedures

- Shift management and handover

- Competency and authorisation

- Permit to work

- Change and configuration management

- Preventive and predictive maintenance

- Spares and obsolescence

- Vendor governance

- Incident, crisis and exercise management

## Central assurance question

Can the organisation operate, maintain and recover the facility consistently without unacceptable human, procedural or governance risk?

# 35. Domain 6: AI Compute Infrastructure

Whether accelerator-based compute is appropriately designed, inventoried, protected, monitored, maintained and resilient.

## Primary concerns

- Compute architecture

- GPU and accelerator inventory

- Ownership and criticality

- Hardware provenance and platform integrity

- Firmware and management controllers

- Cluster configuration and isolation

- Scheduling and fault containment

- Capacity and telemetry

- Lifecycle and decommissioning

## Central assurance question

Can accelerator infrastructure reliably provide required AI compute while containing faults and supporting recovery?

# 36. Domain 7: AI Storage and Data Infrastructure

Whether AI datasets, model artifacts and checkpoints have the required availability, integrity, capacity, throughput and recoverability.

## Primary concerns

- Storage architecture, inventory and ownership

- Capacity, performance and throughput

- Fault domains and replication

- Backup and recovery

- Checkpoint and model-artifact storage

- Corruption detection and integrity validation

- Media handling and sanitisation

- Storage telemetry

## Central assurance question

Can storage infrastructure reliably supply, retain, protect and recover the technical data and artifacts required for the intended AI capability?

# 37. Domain 8: AI Network and Interconnect Architecture

Whether compute, storage, management and external connectivity are supported by isolated, observable, performant and resilient fabrics.

## Primary concerns

- Reference topology

- Compute and storage fabrics

- Management and out-of-band networks

- InfiniBand and RoCE

- Segmentation and cluster isolation

- East-west visibility

- Redundancy and congestion management

- Time synchronisation

- Inter-site and external connectivity

- Failure and recovery testing

## Central assurance question

Can AI infrastructure communicate at required scale while maintaining isolation, visibility, performance and resilience?

Part VI: Cross-domain assurance

# 38. Domains must not become silos

A material event may originate in one domain and propagate through several others. AIDCF therefore requires integrated failure-path reasoning, not isolated control aggregation.

# 39. Cross-domain finding record

A material cross-domain finding identifies the initiating condition, originating and contributing domains, affected capability and assets, dependency chain, control breakpoints, observed safeguards, evidence, confidence, consequence, containment, remediation and retest.

# 40. Common-mode dependencies

Utility, fuel, coolant, control platforms, management services, authentication, suppliers, routes, software, spares, teams and procedures may be shared by systems represented as independent. Redundancy claims must be examined for these dependencies.

Part VII: Evidence and assessment commitments

# 41. Evidence classes

Evidence may include approved design and as-built documents, diagrams, studies, commissioning and maintenance records, alarms, incidents, access and surveillance records, telemetry, work orders, procedures, competencies, contracts, attestations, observation, interviews, samples, simulations and exercises.

# 42. Evidence hierarchy

Evidence strength is evaluated through directness, authenticity, relevance, currency, completeness, independence, repeatability, context, coverage and corroboration.

# 43. Evidence conflict

Conflicting evidence is recorded, evaluated and disclosed. Unresolved conflict limits confidence and remains visible.

# 44. Safe validation hierarchy

Validation ranges from inspection and interview to analysis, historical evidence, witnessed routine tests, controlled functional tests, simulation, tabletop exercises and integrated recovery tests. Selection remains proportionate to safety and authority.

# 45. Prohibited validation behavior

Assessments must not disable life safety, interrupt critical service without authority, exceed operating limits, bypass safety procedure, alter production without change control, create hazardous conditions or misrepresent simulation as live evidence.

Part VIII: Risk, resilience and maturity

# 46. Risk classes

AIDCF recognises threat, hazard, engineering failure, operational, supply-chain, capacity and concentration, and recovery risk. These classes may interact and produce compound consequence.

# 47. Resilience lifecycle

AIDCF evaluates the ability to anticipate, prevent, detect, contain, recover and adapt.

# 48. Maturity doctrine

A future maturity model will define levels and criteria. Maturity does not override critical gates, replace engineering analysis, prove resilience, demonstrate compliance or convert UNKNOWN into confidence.

Part IX: Relationship with AI Trust Graph

# 49. Complementary purpose

AIDCF addresses facilities and infrastructure assurance. AI Trust Graph addresses relationships, authority, reachability, dependencies and controls within the AI ecosystem.

# 50. Primary AIDCF boundaries

AIDCF primarily owns site, building, physical security, facilities engineering, power, cooling, environmental performance, building operations, AI compute hardware, supporting storage, high-performance networking, facility OT and physical infrastructure dependencies.

# 51. Primary AI Trust Graph boundaries

AI Trust Graph primarily owns models, agents, tools, APIs, human and machine identities, authority, trust relationships, data reachability, action paths and emergent digital consequence.

# 52. Shared-boundary handling

Where an infrastructure component also participates in a digital trust path, the frameworks contribute distinct perspectives. The Integration Standard will establish handoff and joint-finding rules.

Part X: Governance, ethics and accountability

# 53. Intended users

AIDCF supports owners, operators, providers, customers, engineering and security teams, risk functions, independent assessors, boards, regulators and policymakers. Tailored use must be disclosed.

# 54. Competency model

A comprehensive assessment may require physical security, electrical, mechanical, cooling, fire and life safety, structural, OT, cybersecurity, AI compute, storage, HPC networking, sustainability, continuity and assurance expertise.

# 55. Independence

Conclusions should be protected from commercial pressure, vendor influence, management override, artificial score targets and pressure to remove UNKNOWN or conceal limitations.

# 56. Responsible claims

Reports distinguish observation, verified fact, judgment, engineering opinion, management or vendor assertion, assumption, limitation, UNKNOWN and recommendation.

# 57. Confidentiality

Facility layouts, security controls, power, cooling, management networks, failure paths and supplier dependencies require lawful collection, classification, access control, secure retention and controlled disclosure.

# 58. Intellectual property boundary

Products may operationalise the methodology through workflow, evidence management, visualisation, testing, scoring and reporting. Tooling shall not silently redefine canonical doctrine.

# 59. Change governance

Changes are proposed, impact-classified, consistency-reviewed, version-controlled, approved, logged and propagated to dependent artifacts.

Part XI: Expected methodology outputs

# 60. Assessment outputs

Outputs may include charter, scope, facility and capability profiles, asset and dependency registers, maps, evidence register, control and critical-gate results, threat and failure analyses, scenario and test records, domain and maturity profiles, findings, decisions, roadmap, reassessment plan and report annexes.

# 61. Decision outcomes

AIDCF supports decisions about facility suitability, design progression, commissioning sufficiency, operational readiness, expansion risk, failure-path remediation, resilience evidence, risk treatment and reassessment. Accountability remains with the organisation.

Part XII: Limitations and reassessment

# 62. Point-in-time limitation

Confidence may change after capacity, hardware, network, cooling, power, control-system, supplier, staffing, regulatory or operational changes. Trust requires maintenance and reassessment.

# 63. Reassessment triggers

Potential triggers include new construction, major design change, high-density compute, liquid cooling, utility changes, redundancy changes, significant incident, failed recovery, supplier change, newly available evidence and completion of material remediation.

Part XIII: Final commitments

# 64. AIDCF commitments

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

# 65. Final doctrine

Artificial intelligence is not sustained by software alone. It depends upon buildings, electrical systems, cooling systems, networks, machines, people, suppliers and procedures operating as an interconnected whole.

Infrastructure that is invisible cannot be adequately governed. Dependencies that are unknown cannot be reliably protected. Redundancy that is not examined cannot be assumed to provide resilience. Resilience that has not been demonstrated cannot be treated as assured. Evidence that is incomplete cannot justify unconditional confidence.

Identify the AI capability. Make the infrastructure visible. Reveal the dependencies. Understand credible failure. Trace propagation and consequence. Validate safeguards safely. Protect critical gates. Preserve evidence and uncertainty. Report without false precision. Enable defensible decisions. Reassess when the system changes.

Appendix A: Canonical terms introduced by this Manifesto

| **Term**                   | **Canonical meaning**                                                                                     |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| **AI capability**          | The intended service, outcome or operational ability supported by the infrastructure within scope.        |
| **Asset**                  | A physical, technical, environmental, human or procedural element relevant to the intended capability.    |
| **Dependency**             | A condition, asset, service, person or relationship required for another element to operate as intended.  |
| **Failure mode**           | A defined manner in which an asset, control, process or dependency may fail.                              |
| **Propagation path**       | The sequence through which an initiating condition produces effects across assets or domains.             |
| **Safeguard**              | A preventive, detective, containing, recovery or adaptive measure intended to modify risk or consequence. |
| **Critical gate**          | A non-compensable or conclusion-limiting condition whose failure caps assurance.                          |
| **Evidence coverage**      | The extent to which relevant scope, time, conditions and assertions are supported by evidence.            |
| **UNKNOWN**                | A preserved result state used where evidence is insufficient to reach a defensible conclusion.            |
| **Assurance decision**     | A bounded conclusion or decision supported by defined evidence, analysis and limitations.                 |
| **Operating state**        | A defined facility condition such as normal, degraded, maintenance, emergency, recovery or transition.    |
| **Common-mode dependency** | A shared dependency capable of defeating supposedly independent systems or paths.                         |

Appendix B: Approval and change records

# Approval record

| **Approval role**                      | **Status**                               |
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

| **Version** | **Status**              | **Summary**                                                      |
|-------------|-------------------------|------------------------------------------------------------------|
| 0.1         | Initial concept         | Established the initial purpose and eight-domain idea.           |
| 0.2         | Expanded draft          | Added assurance doctrine, boundaries and integration principles. |
| 1.0         | Controlled-review draft | Established the comprehensive canonical Manifesto for Release 1. |

# Manifesto acceptance criteria

- Purpose is clearly differentiated from conventional data-centre standards.

- Eight domains and their boundaries are stable.

- Relationship with AI Trust Graph is unambiguous.

- Public and proprietary boundaries are accepted.

- Evidence, UNKNOWN and critical-gate doctrines are retained.

- Safety and engineering limitations are explicit.

- No section prematurely defines downstream controls.

- Independent expert, IP, confidentiality and publication reviews are recorded.
