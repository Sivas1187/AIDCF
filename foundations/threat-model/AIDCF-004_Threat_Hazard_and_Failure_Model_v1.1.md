> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-004_Threat_Hazard_and_Failure_Model_v1.1.pdf](AIDCF-004_Threat_Hazard_and_Failure_Model_v1.1.pdf).

**AIDCF**

# THREAT, HAZARD & FAILURE MODEL

*AI Data Centre Facilities Assurance Framework*

Version 1.1

Capability-first adverse-condition, failure-propagation and resilience analysis

Artifact ID: AIDCF-004 (requirement short code THF)  
Artifact type: Normative foundation standard  
Status: Draft for controlled review  
Author: Siva Sethumadhavan  
Release 1: Foundational Methodology

Identify credible adversity. Separate cause from failure. Trace propagation. Validate safeguards safely. Preserve UNKNOWN.

# Document control

| **Field**        | **Value** |
|------------------|-----------|
| Title            | AIDCF Threat, Hazard and Failure Model |
| Artifact ID      | AIDCF-004 |
| Requirement code | THF (requirements are numbered THF-REQ-NNN) |
| Version          | 1.1 |
| Date             | 2026-10-10 |
| Status           | Draft for controlled review |
| Author           | Siva Sethumadhavan |
| Depends on       | AIDCF-001 AIDCF Manifesto; AIDCF-002 Core Conceptual Model; AIDCF-003 Infrastructure Ontology and Taxonomy |
| Used by          | AIDCF-006 Assurance Principles Standard; AIDCF-007A Canonical Master Control Registry; AIDCF-008 Evidence Model; AIDCF-009 Assessment Methodology Practitioner Handbook; AIDCF-010 Scoring and Decision Framework; AIDCF-013 AI Data Centre Assurance Reference Architecture; AIDCF-014 End-to-End Traceability and Machine-Executable Data Standard; AIDCF-018 Domain Guides |
| Purpose          | Define how threats, hazards, causes, failure modes, propagation, consequence, safeguards, residual state and recovery are identified, analysed and recorded so that they can support or challenge an assurance case. |
| Users            | Owners, operators, engineers, assessors, AI infrastructure teams, security, resilience, risk and assurance practitioners. |
| Safety boundary  | This standard does not replace licensed or competent engineering judgement and does not authorise destructive, hazardous or operationally disruptive testing. |

## Revision history

| **Version** | **Date**   | **Summary** |
|-------------|------------|-------------|
| 0.1         | —          | Architecture draft: ontology and doctrine. |
| 0.5         | —          | Integrated draft: domain catalogues, scenarios and graph semantics. |
| 1.0         | —          | Controlled-review draft: comprehensive baseline for expert review. |
| 1.1         | 2026-10-10 | Re-baselined to the 15 domains, canonical chain and SPEC vocabularies; distinct causal operators, techniques and consequence families; 20 engineered cross-domain scenarios; function-specific failure-mode catalogue; UNKNOWN permission rules; consecutive THF-REQ IDs with legacy mapping. |

# Executive thesis

AIDCF determines whether credible adverse conditions can defeat Required Functions, propagate through dependencies and fault domains, overcome safeguards, and prevent a Capability Instance from achieving its Service Outcomes within tolerance under its declared operating states. Component failure is not the endpoint. Capability consequence, residual state, recovery and evidence are.

AI data centres change the failure landscape in specific ways that this standard is built to capture:

- **Correlated, synchronous demand.** Large distributed training jobs move thousands of accelerators through compute, communication and checkpoint phases in lock-step. Electrical and thermal load can therefore swing by a large fraction of the hall or site load within seconds, which interacts with utility interconnection, UPS, generator and cooling-plant control in ways that conventional diversity-based enterprise data-centre analysis does not.
- **High density with small thermal inertia.** Direct-to-chip liquid cooling removes most heat through a technology cooling system (TCS) with little stored thermal capacity at the cold plate. Loss of coolant flow reaches accelerator thermal limits far faster than loss of air cooling in a legacy hall.
- **Tightly coupled workloads.** A synchronous job is only as available as its least available participant. Loss of one node, one link or one storage target can stall or terminate the whole job, so blast radius is defined by the job and the fabric, not the rack.
- **Fleet-wide common mode.** Accelerators, NICs, switches, CDUs and controllers are deployed in large homogeneous fleets sharing firmware, configuration sources and management planes. A single defect or change can reach the whole fleet faster than any physical failure.
- **Converged control planes.** BMS, EPMS, CDU controllers, cluster managers, fabric controllers and AI-enabled automation now share identity, network and time services. Digital authority over physical infrastructure is a first-class hazard and threat surface.
- **Recovery as a capability.** Restoration of training progress depends on checkpoint durability and restore throughput as much as on power and cooling restoration. Recovery-only dependencies are frequently untested at scale.

# Position in the canonical assurance chain

AIDCF uses one assurance chain, defined in AIDCF-002 and structured as an ISO/IEC/IEEE 15026-2 assurance case. The top claim is: *"Capability Instance X can achieve Service Outcomes Y within tolerances T under declared operating states S, for decision question Q, as of date D."*

The construction chain is:

1 Decision Question → 2 Capability Instance → 3 Service Outcome → 4 Required Function → 5 Architecture (InfrastructureSystem/Asset/Interface) → 6 Dependency and Fault Domain → **7 Threat / Hazard / Failure Scenario** → 8 Safeguard → 9 Control → 10 Evidence Requirement → 11 Evidence Object → 12 Control Assessment (result) → 13 Finding / UNKNOWN Record → 14 Gate Result → 15 Score Snapshot and Decision Recommendation → 16 Assurance Decision → (Report and Reassessment Trigger close the loop back to 2).

AIDCF-004 is the semantic owner of step 7 and defines how steps 6 and 8 are exercised by scenarios:

| **Chain step** | **AIDCF-004 role** |
|----------------|--------------------|
| 4 Required Function | Supplies the reference Required Function catalogue used for failure-mode analysis (Appendix A). Functions declared for a Capability Instance are mapped to these reference functions. |
| 6 Dependency and Fault Domain | Consumes dependency and fault-domain records from AIDCF-003; scenarios test whether declared independence and containment hold. |
| 7 Threat / Hazard / Failure Scenario | Owns the scenario anatomy, taxonomies, causal operators, analysis techniques, consequence families and scenario library. |
| 8 Safeguard | Defines safeguard and barrier records, path position, dependencies and safe validation, and how a safeguard is linked to controls in AIDCF-007A. |
| 13 Finding / UNKNOWN Record | Defines THF finding types and the rules for classifying scenario UNKNOWNs by type (U1–U10, AIDCF-008) and severity (US1–US5). |
| 14 Gate Result | Identifies which critical gates a scenario bears on and which unresolved path elements trigger CG-12. Gate criteria and roll-up are defined in AIDCF-010. |

In the 15026 structure, scenario sub-claims ("this scenario cannot defeat Service Outcome Y beyond tolerance T in state S") sit at step 7 and are supported by safeguard sub-claims at step 8. Unresolved scenario elements, demonstrated uncontrolled paths and contradicting events are defeaters, recorded as Findings, UNKNOWN Records or CHALLENGES relationships.

## Scenario anatomy (internal structure of step 7)

Within step 7 every scenario is decomposed using the following ordered anatomy. It is not a separate assurance chain; it is the internal structure of a FailureScenario object (AIDCF-014) and it terminates in the safeguard (step 8) and consequence it bears upon.

Context and operating state → Threat / Hazard / Degradation mechanism → Initiating event → Failure cause → Failure mode (of a Required Function) → Local effect → Dependency effect (via step 6 edges) → Propagated failure → Capability consequence (on step 3 Service Outcomes) → Safeguard response (step 8) → Residual state → Recovery path

| **Anatomy element (v1.0 "canonical chain" term)** | **Canonical chain step it belongs to** | **AIDCF-014 field** |
|---------------------------------------------------|----------------------------------------|---------------------|
| Context | 1–5 (decision, capability, outcome, function, architecture) and declared operating state | preState |
| Threat / Hazard / Degradation | 7 | initiatingSource (Threat or Hazard object) |
| Initiating event | 7 | initiatingSource / steps[0] |
| Failure cause | 7 | steps[n].cause |
| Failure mode | 7 (of a step 4 Required Function) | steps[n].failureMode |
| Local, dependency and propagated effects | 7 traversing 6 | steps[n] |
| Capability consequence | 7 bearing on 3 | outcomeEffects |
| Safeguard response | 8 | safeguards |
| Residual state | 7 | residualState |
| Recovery | 7 and 8 (recovery safeguards) | steps (RECOVERS operator), safeguards |
| Assurance decision | 16 (not owned by this standard) | — |

# Contents

1\. Part I — Authority, scope and conformance

2\. Part II — Core ontology and distinctions

3\. Part III — Scenario and propagation architecture

4\. Part IV — Threat taxonomy

5\. Part V — Hazard taxonomy

6\. Part VI — Failure-cause taxonomy

7\. Part VII — Failure-mode taxonomy

8\. Part VIII — Effects, causal operators and consequence

9\. Part IX — Safeguards and resilience

10\. Part X — Analysis techniques

11\. Part XI — Criticality and uncertainty

12\. Part XII — UNKNOWN permission and path-resolution rules

13\. Part XIII — Fifteen-domain scenario families

14\. Part XIV — Cross-domain scenario library (X01–X20)

15\. Part XV — Assessment records and evidence

16\. Part XVI — Machine-readable model

17\. Part XVII — Governance and acceptance

18\. Appendices A–E

# Part I - Authority, scope and conformance

## 1. Purpose

This standard provides a controlled, vendor-neutral method for identifying, representing, analysing and recording adverse conditions affecting AI data-centre capabilities across the fifteen AIDCF domains, so that scenario analysis can be traced to Required Functions, safeguards, controls (AIDCF-007A), evidence (AIDCF-008), critical gates and decisions (AIDCF-010).

## 2. Scope

The standard applies to every Capability Instance assessed under AIDCF, at every lifecycle stage (PLAN, DESIGN, BUILD, COMMISSION, OPERATE, CHANGE, DECOMMISSION), and to the fifteen domains:

| **Code** | **Domain** |
|----------|------------|
| GOV | Governance, Accountability and Assurance Direction |
| CAP | AI Capability, Service Outcome and Demand Management |
| DEP | Dependency, Concentration and External Reliance Management |
| PHY | Physical Site, Building and Security Infrastructure |
| POW | Electrical Power Infrastructure and Energy Continuity |
| THM | Cooling, Thermal and Fluid Infrastructure |
| ENV | Environmental and Resource Performance |
| CMP | AI Compute Infrastructure |
| STO | AI Storage and Data Infrastructure |
| NET | AI Network and Interconnect Architecture |
| OPS | Building Operations and Service Management |
| RES | Resilience, Continuity and Recovery |
| SUP | Supply Chain, OEM and Ecosystem Assurance |
| SEC | Digital, OT and Control-Plane Security |
| EVA | Evidence, Assessment and Assurance Management |

The legacy eight-domain model (D1–D8) used in v1.0 is superseded. Appendix E.2 maps the v1.0 domain catalogue to the fifteen domains for traceability only.

Out of scope: model-level AI risks (model behaviour, bias, content safety) except where they create an infrastructure effect, for example AI-enabled automation acting on infrastructure (SEC-06) or workload behaviour that changes electrical or thermal demand (CAP-04, CAP-05). Model-level assurance is handed off through AIDCF-005.

## 3. Normative language

"Shall" and "shall not" state requirements; "should" and "should not" state recommendations; "may" states permission; "can" states capability. Usage follows ISO/IEC Directives Part 2. A fact, dependency, condition, deficiency or UNKNOWN is **material** if, had it been known or resolved differently, a competent assessor would reasonably expect it to change a control result, a gate result, the decision state, or a condition, limitation or ceiling attached to the decision, for the declared Capability Instance, Service Outcomes and operating states.

## 4. Normative requirements (general)

**THF-REQ-001** Every material scenario shall identify the Capability Instance and the Service Outcomes (with tolerances) it can affect.

**THF-REQ-002** Threat, hazard, initiating event, cause, failure mode, effect and consequence shall be recorded as distinct elements and shall not be collapsed into one another.

**THF-REQ-003** Each scenario shall declare the assessment boundary, architecture baseline, initial operating state, the operating states traversed and the operating envelope in which it is analysed.

**THF-REQ-004** Propagation shall be expressed through explicit dependency and fault-domain records conforming to AIDCF-003; implicit or narrative-only propagation shall not be used to support or defeat a claim.

**THF-REQ-005** The existence of a safeguard shall not be treated as evidence of its effectiveness; effectiveness requires evidence meeting the floor of the relevant control's evidence profile (AIDCF-008) for the claimed claim type.

**THF-REQ-006** Any material unverified path element shall be represented as an UNKNOWN Record with a type (U1–U10) and severity (US1–US5) in accordance with Part XII.

**THF-REQ-007** Analysis of life-safety, hazardous-energy and safety-instrumented functions shall be performed or approved by competent, authorised professionals for the relevant discipline and jurisdiction.

**THF-REQ-008** Validation of safeguards shall be proportionate, authorised and safe, and shall follow the safe validation hierarchy in Part IX.

**THF-REQ-009** Excluded, external and cross-boundary dependencies shall remain visible in scenarios that traverse them, with owner and effect on confidence.

**THF-REQ-010** Average scores shall not override critical gates or consequence severity CS4–CS5 outcomes.

**THF-REQ-011** Cross-references to other AIDCF artifacts shall use public artifact identifiers (AIDCF-NNN); domain references shall use the fifteen domain codes; control references shall use AIDCF-007A identifiers (MCF-<DOM>-NNN or family <DOM>-NN).

## 5. Conformance levels

Conformance levels are designated THF-C0 to THF-C4 (v1.0 designations F0–F4 are retired to avoid confusion with the evidence quality dimension F).

| **Level** | **Name**            | **Expectation** |
|-----------|---------------------|-----------------|
| THF-C0    | Vocabulary aligned  | Uses the canonical terms, operators, failure-mode codes and consequence families of this standard. |
| THF-C1    | Scenario structured | Records context, initiating event, failure mode, effects and capability consequence for each material scenario. |
| THF-C2    | Dependency traced   | Expresses each path step through AIDCF-003 dependency and fault-domain records, with operating states and causal operators. |
| THF-C3    | Evidence gated      | Links credited safeguards to AIDCF-007A controls, evidence requirements and evidence objects; classifies UNKNOWNs by type and severity; identifies gate effects. |
| THF-C4    | Machine actionable  | Publishes scenarios as AIDCF-014 FailureScenario and Safeguard objects that pass the validation rules in Part XVI. |

An assessment that relies on scenarios to support EFFECTIVENESS or RESILIENCE claims (AIDCF-006, claim types in AIDCF-008) shall conform at THF-C3 or above.

# Part II - Core ontology and distinctions

## 6. Canonical terms

| **Term**               | **Canonical definition** | **AIDCF-014 class or field** |
|------------------------|--------------------------|------------------------------|
| Threat                 | Deliberate actor, capability, intent or circumstance capable of adverse infrastructure consequence. | Threat |
| Hazard                 | Non-deliberate source, condition or event with potential for injury, damage, disruption or environmental impact. | Hazard |
| Degradation mechanism  | Process progressively reducing condition, margin or performance (for example corrosion, fouling, battery capacity fade, insulation ageing, optic power decay). | Hazard (subtype) |
| Initiating event       | Event or condition starting a specific scenario. | FailureScenario.initiatingSource |
| Failure cause          | Circumstance or mechanism producing or contributing to a failure mode. | FailureScenario.steps[].cause |
| Failure mode           | Manner in which a Required Function is lost, degraded, delayed, incorrect, intermittent or uncontrolled (Part VII). | FailureMode |
| Local effect           | Immediate result at the failed item or function. | steps[].effect |
| Next-level effect      | Effect on the containing subsystem or dependent function. | steps[].effect |
| End effect             | Effect on the Capability Instance or Service Outcome. | outcomeEffects |
| Propagation path       | Ordered sequence of steps through which effects move across entities, dependencies and fault domains. | steps |
| Consequence            | Realised or foreseeable effect on capability and stakeholders, expressed in a consequence family (Part VIII). | outcomeEffects |
| Predisposing condition | Condition increasing susceptibility without necessarily initiating failure (for example a bypass, a deferred repair, an as-built divergence). | preState |
| Safeguard              | Measure intended to anticipate, prevent, detect, contain, respond, recover or adapt. | Safeguard |
| Barrier                | Safeguard positioned on a defined path at a defined position (cause side, escalation, consequence side, recovery side). | Safeguard with pathPosition |
| Residual condition     | State remaining after the credited safeguards act, given their demonstrated behaviour. | residualState |
| Recovery path          | Sequence restoring an approved service and infrastructure state, including validation. | steps (RECOVERS) and RECOVERS_THROUGH |
| Latent failure         | Failure present but not revealed until another event, demand or test. | FailureMode (M21) |
| Common-cause failure   | Multiple failures arising from one shared cause (for example one firmware defect in all CDUs). | steps operator CORRELATES_WITH and SHARES_FAULT_DOMAIN_WITH |
| Common-mode failure    | Nominally redundant alternatives fail in the same manner, through a shared dependency or similar susceptibility. | SHARES_FAULT_DOMAIN_WITH |
| Near miss              | Event capable of material consequence that did not realise it. | Event |

## 7. Mandatory distinctions

| **Do not collapse**      | **Reason** |
|--------------------------|------------|
| Threat / hazard          | Deliberate and non-deliberate sources require different assumptions about persistence, adaptation and concealment. |
| Cause / failure mode     | Why it failed differs from how the function failed; safeguards are often mode-specific and cause-agnostic. |
| Mode / effect            | Failure behaviour differs from resulting condition. |
| Effect / consequence     | Technical effect differs from capability impact on a Service Outcome. |
| Fault / failure          | A fault can exist without defeating function (for example a failed redundant pump). |
| Event / state            | Occurrence differs from continuing condition. |
| Exposure / likelihood    | Contact with a source differs from probability of consequence. |
| Detection / prevention   | Observing does not stop failure. |
| Failover / recovery      | Transfer to an alternative differs from restoration of the approved state. |
| Redundancy / resilience  | Duplication does not prove sustained outcome; shared causes and transfer behaviour must be shown. |
| UNKNOWN / low likelihood | Missing evidence is not evidence of improbability. |

# Part III - Scenario and propagation architecture

## 8. Bidirectional analysis

| **Approach**     | **Question**                                 | **Output** |
|------------------|----------------------------------------------|------------|
| Bottom-up        | How can this Required Function fail?         | Mode, cause and local/end effects (Appendix A). |
| Top-down         | What can defeat the Service Outcome?         | Top event and causal combinations. |
| Path-based       | How can effects traverse dependencies?       | Ordered path and breakpoints. |
| State-based      | What changes in MAINTENANCE, DEGRADED, TRANSITION or RECOVERY? | State-specific exposure. |
| Capability-based | What minimum outcome must remain?            | Consequence and graceful-degradation boundary. |

Bottom-up analysis alone misses interaction failures; top-down analysis alone misses unanticipated modes. Material Capability Instances shall be analysed in both directions and reconciled.

## 9. Path types

| **Path type**       | **Meaning** | **AI data-centre illustration** |
|---------------------|-------------|---------------------------------|
| Local               | Contained within the intended fault domain. | Single cold-plate blockage throttles one accelerator; scheduler drains the node. |
| Cascading           | One failure triggers additional failures. | Busway trip drops a row; the job's collective stalls; restart storm saturates checkpoint storage. |
| Common-cause        | One cause affects multiple paths. | One CDU firmware defect affects every CDU of that model. |
| Common-mode         | Similar alternatives fail similarly. | A and B fabric planes both lose their controller because they share a configuration source. |
| Sequential          | An initial change enables later failure. | A setpoint change made during commissioning removes thermal margin needed in a heatwave. |
| Compound            | Multiple events or states combine. | Utility outage during UPS maintenance. |
| Latent              | Hidden condition activated on demand. | A generator fuel filter partially blocked; revealed only during an extended run. |
| Maintenance-induced | Work or bypass creates exposure. | UPS on maintenance bypass when a sag arrives. |
| Recovery-induced    | Restoration action creates or reintroduces failure. | Restoring a switch configuration backup that contains the defect. |
| Cross-domain        | Path traverses multiple AIDCF domains. | SEC → THM → CMP: compromised BMS changes setpoints, leading to throttling. |
| Cross-boundary      | Path crosses organisation or assessment scope. | Colocation provider chiller maintenance affects tenant CDU supply temperature. |
| Slow-burn           | Degradation accumulates to threshold. | Heat-exchanger fouling raises approach temperature over months. |
| Intermittent        | Repeated instability complicates diagnosis. | Marginal optic produces link flaps that repeatedly abort collectives. |

## 10. Operating states in scenarios

Scenarios use the operating-state vocabulary of AIDCF-003 §45: NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION, SHUTDOWN, FAILED, UNKNOWN.

**THF-REQ-012** Each scenario shall record its initial operating state and every operating state it enters, including the state in which the credited safeguard is expected to act and the state in which recovery is completed.

**THF-REQ-013** A safeguard shall be credited only for the operating states in which its behaviour is evidenced; claims shall not be generalised to uncovered states (AIDCF-003 IOT-REQ-048).

| **State** | **Scenario analysis emphasis** |
|-----------|--------------------------------|
| NORMAL | Baseline exposure; whether design margin and automatic safeguards are sufficient without human intervention. |
| DEGRADED | Which redundancy, reserve or safeguard is already consumed, and whether a second event is now decisive. |
| MAINTENANCE | Bypasses, isolations, temporary configurations, reduced staffing at the point of work and procedures that remove automatic protection. |
| EMERGENCY | Time-critical human decisions, alarm load, life-safety priorities overriding continuity, and emergency changes. |
| RECOVERY | Recovery-only dependencies, restart sequencing, inrush and restart storms, validation of restored state, and reintroduction of the original cause. |
| TRANSITION | Expansion tie-ins, migrations, firmware rollouts and control-regime changes where two baselines coexist. |
| SHUTDOWN | Residual hazards (stored energy, pressurised fluids, battery state of charge) and the dependencies needed to restart. |
| FAILED | Consequence magnitude and duration, alternate capacity, and the shortest safe path back to RECOVERY. |
| UNKNOWN | When the state cannot be determined (for example loss of monitoring), the scenario shall be analysed for the most adverse credible state consistent with available evidence. |

## 11. Scenario minimum record

The scenario minimum record aligns with the AIDCF-014 FailureScenario profile. Field names in brackets are the AIDCF-014 field names. The column "UNKNOWN permitted" is normative and is defined in Part XII; class A fields never accept UNKNOWN in a submitted scenario.

| **Field** | **Content** | **UNKNOWN permitted** |
|-----------|-------------|-----------------------|
| scenarioId | Stable identifier. | No (class A) |
| capabilityInstance | Capability Instance identifier. | No (class A) |
| serviceOutcomes | Affected Service Outcomes with tolerances. | No (class A) |
| assessmentBoundary | Boundary reference, including exclusions traversed. | No (class A) |
| architectureBaseline | Baseline version analysed (intended, as-built, commissioned or observed). | No (class A) |
| initialOperatingState [preState] | Operating state code and predisposing conditions. | State: class B; predisposing conditions: class C |
| threatOrHazard [initiatingSource] | Threat or Hazard object. | Class C (attribution) / class B (source class) |
| initiatingEvent [initiatingSource] | Event description and class. | Class B |
| failureCauses [steps[].cause] | Causes per step, alternate hypotheses, excluded causes. | Class C |
| initialFailureMode [steps[0].failureMode] | Mode code (Part VII) of the first Required Function affected. | Class B |
| orderedPathSteps [steps] | Ordered steps with entity, Required Function, failure mode, causal operator, dependency/fault-domain edge and effect. | Class B |
| faultDomains | Fault domains traversed and those intended to contain the path. | Class B |
| operatingStatesTraversed | All states entered (§10). | Class B |
| safeguards | Credited and non-credited safeguards with path position. | Class B |
| safeguardDependencies | Power, sensing, control, people, supplier and data dependencies of each credited safeguard. | Class B |
| residualState [residualState] | State remaining after credited safeguards act. | Class D |
| capabilityConsequence [outcomeEffects] | Consequence family, magnitude, duration and severity band (CS0–CS5). | Class B |
| recoveryPath | Recovery steps, recovery-only dependencies and validation. | Class D |
| evidence [evidenceRefs] | Evidence objects supporting or challenging each credited safeguard. | Class D |
| confidenceAndUnknown [confidence] | Confidence (CONF-0 to CONF-4, flags) and UNKNOWN Record references. | No (the record itself is mandatory) |
| criticalGates | Gates whose scope the scenario traverses (Part XIII, Part XIV). | No (derived by rule) |
| controls | AIDCF-007A controls linked to credited safeguards. | Class D |
| owners | Scenario owner and owners of credited safeguards. | Class D |
| reassessmentTriggers | Changes that invalidate the analysis. | No |

# Part IV - Threat taxonomy

## 12. Threat sources

| **Source family** | **Examples** | **Analysis note** |
|-------------------|--------------|-------------------|
| External actor    | Trespasser, saboteur, criminal, activist, competitor or state-aligned actor. | Assume adaptation: a deliberate actor can choose timing (for example during MAINTENANCE) and combine vectors. |
| Insider           | Employee, contractor, supplier staff or coerced individual. | Authorised access bypasses perimeter safeguards; analyse separation of duties and two-person rules. |
| Supply chain      | Manufacturer, integrator, logistics, maintenance, software or firmware supplier. | Effects can be latent and fleet-wide; authenticity does not imply correctness. |
| Tenant/customer   | Authorised party acting maliciously, negligently or outside agreement. | Includes workloads deliberately or accidentally exceeding agreed power or thermal profile. |
| Remote operator   | Authorised or compromised remote support (OEM, BMS integrator, managed service). | Persistent remote paths into OT are a principal route to CG-15 defeat. |
| Automated source  | Malicious code, or legitimate automation and AI-enabled agents acting outside intended bounds. | Automation acts at machine speed across fleets; analyse authority, rate limits and allowlists (SEC-06). |
| Unattributed      | Evidence supports deliberate activity but source is unresolved. | Attribution may remain UNKNOWN (class C) if safeguards are source-agnostic. |

## 13. Threat events

| **Threat event**           | **Infrastructure interpretation** |
|----------------------------|-----------------------------------|
| Unauthorised entry         | Access to site, plant room, hall, cage or rack. |
| Physical interference      | Tampering, switching, obstruction, disconnection or valve operation. |
| Theft/removal              | Removal of equipment, accelerators, media, cable, fuel or spares. |
| Sabotage                   | Deliberate disabling or damage. |
| Utility manipulation       | Interruption or corruption of power, water, fuel or telecom supply. |
| OT compromise              | Manipulation of BMS, EPMS, SCADA, CDU controllers, PLCs or their engineering workstations. |
| Configuration manipulation | Unauthorised change to settings, thresholds, routes, images or protection settings. |
| Supply-chain compromise    | Counterfeit, modified, malicious or unsupported component or release. |
| Resource exhaustion        | Intentional consumption of compute, power, cooling, storage or network capacity. |
| Control-plane abuse        | Misuse of cluster manager, fabric controller, storage controller or automation authority to issue mass actions. |
| Evidence destruction       | Alteration or deletion of logs, telemetry, video or records. |
| Multi-vector attack        | Coordinated physical, cyber, supplier and social actions. |

# Part V - Hazard taxonomy

| **Hazard family**        | **Examples** |
|--------------------------|--------------|
| Meteorological           | Extreme dry-bulb or wet-bulb temperature, humidity, wind, lightning, rain, drought or haze. |
| Hydrological             | Flood, storm surge, groundwater, drainage failure or water scarcity. |
| Geological               | Earthquake, settlement, subsidence or soil instability. |
| Environmental            | Particulate, gaseous corrosion, pollution, salt or biological contamination. |
| External fire/industrial | Adjacent fire, smoke, explosion, vibration or vehicle impact. |
| Electrical               | Arc, short circuit, overcurrent, overvoltage, voltage sag, backfeed, resonance or stored energy. |
| Electrical-load dynamics | Large, fast, correlated load steps and oscillations from synchronous AI workloads interacting with utility, UPS, generator and protection behaviour. |
| Thermal                  | Overtemperature, heat accumulation, fast transients at low thermal inertia, or battery thermal runaway. |
| Pressure/fluid           | Overpressure, water hammer, rupture, cavitation, leak, air entrainment or contamination. |
| Structural/mechanical    | Overload (including rack mass of liquid-cooled systems), vibration, anchorage failure, obstruction or collapse. |
| Chemical/material        | Coolant, refrigerant, battery electrolyte and off-gas, fuel, suppressants or material incompatibility. |
| Human factors            | Fatigue, workload, interface ambiguity, alarm flood or lost situational awareness. |
| Control interaction      | Bad sensor data, unsafe logic, setpoint conflict, competing control loops or unstable automation. |
| Common-mode digital      | Shared firmware, configuration source, time source, identity service or management plane defect. |
| Utility/geopolitical     | Grid, water, fuel, telecom, border, sanctions or civil disruption. |

# Part VI - Failure-cause taxonomy

| **Cause family**     | **Examples** |
|----------------------|--------------|
| Design               | Requirement, topology, sizing, protection, tolerance or integration error. |
| Manufacturing        | Defect, material variation, contamination or counterfeit. |
| Installation         | Assembly, routing, termination, torque, cleanliness, labelling or cord-to-feed mapping. |
| Commissioning        | Incomplete scope, unrealistic load bank profile, untested transient or unresolved defect. |
| Configuration        | Setpoint, firmware, driver, route, QoS class, threshold or compatibility error. |
| Operation            | Incorrect or delayed action, bypass, overload or deviation. |
| Maintenance          | Missed or incorrect work, calibration, spares or temporary state. |
| Ageing               | Wear, corrosion, fatigue, insulation breakdown, battery capacity fade or sensor drift. |
| Capacity             | Demand exceeds usable or resilient capacity, or reserve is committed. |
| Environment          | Temperature, humidity, fluid quality, particulate, vibration or flood. |
| Dependency           | Upstream, shared, hidden, recovery-only or external reliance. |
| Control/monitoring   | Sensor, logic, alarm, communication, historian or response failure. |
| Human/organisational | Competence, staffing, fatigue, authority or knowledge concentration. |
| Supplier/contract    | Service, SLA, lead time, access or support failure. |
| Security             | Unauthorised access, manipulation, sabotage or theft. |
| Change/transition    | Expansion, migration, upgrade, rollback or temporary state. |
| Recovery             | Wrong sequence, corrupt baseline, insufficient spare or failed restart. |
| UNKNOWN              | Cause cannot be established with available evidence (Part XII rule C). |

**THF-REQ-014** Analysis shall not terminate at "human error"; systemic contributors (procedure, interface, alarm load, staffing, training, authority and time pressure) shall be examined and recorded.

**THF-REQ-015** Causal decomposition shall stop only where further analysis would not change treatment, accountability, safeguard selection or the classification of an UNKNOWN.

**THF-REQ-016** Alternate causal hypotheses and excluded causes shall be recorded with the basis for exclusion.

**THF-REQ-017** Where cause is UNKNOWN, the observed facts, timeline and failure mode shall be preserved unchanged.

# Part VII - Failure-mode taxonomy

Failure modes are coded M01–M30 and grouped by class. Appendix A applies only the modes that are meaningful for each Required Function; a mode shall not be listed against a function for which it has no physical or logical meaning.

| **Code** | **Class** | **Failure mode** | **Meaning** |
|----------|-----------|------------------|-------------|
| M01 | Loss | Complete loss | Function unavailable. |
| M02 | Demand response | Failure to start | Does not initiate on demand. |
| M03 | Demand response | Failure to stop | Continues when cessation is required. |
| M04 | Demand response | Failure to transfer | Alternate path or source not established. |
| M05 | Containment | Failure to isolate | Fault or effect crosses an intended boundary. |
| M06 | Recovery | Failure to reset/recover | Cannot return to approved state. |
| M07 | Quality | Degraded output | Below required capacity, rate or quality. |
| M08 | Quality | Excess output | Output exceeds a safe or allowed limit. |
| M09 | Quality | Incorrect output | Wrong value, route, state, setpoint or target. |
| M10 | Timing | Delayed output | Correct but too late for the outcome. |
| M11 | Timing | Premature output | Occurs before required conditions are satisfied. |
| M12 | Stability | Intermittent operation | Repeated appearance and disappearance. |
| M13 | Stability | Unstable/oscillating | Uncontrolled variation or hunting. |
| M14 | Capacity | Capacity exhaustion | Demand exceeds available capacity. |
| M15 | Capacity | Performance collapse | Non-linear degradation after a threshold. |
| M16 | Data | Data/configuration corruption | State becomes inconsistent or wrong. |
| M17 | Monitoring | Loss of visibility | Cannot observe or diagnose. |
| M18 | Monitoring | False indication | Indicates an absent condition or misses a present one. |
| M19 | Monitoring | Failure to alarm | Warning absent or late. |
| M20 | Monitoring | Nuisance alarm | False or excessive alarms mask real events. |
| M21 | Standby | Latent standby failure | Standby unavailable on demand. |
| M22 | Standby | Bypass left active | Temporary impairment persists after its authorised period. |
| M23 | Loss | Uncontrolled shutdown | Ceases without orderly preservation of state. |
| M24 | Spurious | Spurious operation | Operates without a valid demand (spurious trip, discharge, transfer or drain). |
| M25 | Escape | Leakage/escape | Fluid, energy, data or material escapes its boundary. |
| M26 | Flow | Congestion/blockage | Flow is impeded. |
| M27 | Coordination | Loss of synchronisation | Coordinated state diverges (time, phase, replicas, controllers). |
| M28 | Compatibility | Incompatibility | Versions, materials or protocols conflict. |
| M29 | Allocation | Misallocation | Resource assigned wrongly (wrong fault domain, wrong feed, wrong priority). |
| M30 | Control | Loss of control / unauthorised control | Function can no longer be commanded by its authorised controller, or is commanded by an unauthorised one. |
| M00 | Unknown | Unknown mode | Manner unresolved (class B UNKNOWN; Part XII). |

v1.0 "Unsafe persistence" is merged into M03 Failure to stop; "Uncontrolled shutdown" is retained as M23; M24 and M30 are new in v1.1 because spurious operation and loss of control are dominant modes for protection, fire-interface and automation functions.

# Part VIII - Effects, causal operators and consequence

## 14. Effect levels

| **Effect level** | **Question** |
|------------------|--------------|
| Local            | What happens at the failed item or Required Function? |
| Next-level       | What happens to the subsystem or dependent function? |
| Cross-domain     | Which other domain becomes impaired, and through which dependency class? |
| Capability       | Which Service Outcome is degraded or lost, by how much and for how long? |
| Stakeholder      | Who or what experiences the consequence? |

## 15. Causal and propagation operators

Operators are the controlled vocabulary for the `operator` attribute of each step in a FailureScenario (AIDCF-014). They describe how one scenario element acts on another. They are not graph relationship types; where a step also asserts a structural fact (a dependency, a shared fault domain, a protection relationship), that fact shall be recorded with the canonical AIDCF-014 relationship shown in the last column, so the scenario remains reconcilable with the architecture graph.

**THF-REQ-018** Each scenario step shall carry exactly one primary operator from Table 15.1 and may carry qualifiers from Table 15.2; free-text causal verbs shall not be used in a THF-C2 or higher scenario.

**THF-REQ-019** Where a step's operator depends on a structural relationship (dependency, shared fault domain, protection, recovery route), the corresponding canonical relationship shall exist in the architecture graph; if it does not, the step is an unresolved path element under Part XII.

### Table 15.1 — Primary operators

| **Operator** | **Definition** | **Logic and usage guidance** | **Example** | **Canonical relationship asserted** |
|--------------|----------------|------------------------------|-------------|-------------------------------------|
| CAUSES | A is sufficient, in the stated state and conditions, to produce B without any further event. | Deterministic, single-path causation. Use only when B follows from A in every credible instance of the declared conditions; otherwise use CONTRIBUTES_TO. Combinations of causes are expressed by grouping CONTRIBUTES_TO steps under a logic qualifier (AND, OR, K_OF_N). | Loss of both CDU pumps CAUSES loss of TCS flow. | DEPENDS_ON (B's function depends on A's) |
| CONTRIBUTES_TO | A raises the likelihood, magnitude or speed of B but is not sufficient alone. | Necessary-but-not-sufficient or partial causation; must be grouped with the other contributors and a logic qualifier. Used for enabling and predisposing conditions. | A deferred battery replacement CONTRIBUTES_TO UPS runtime shortfall (AND with utility outage). | — (scenario-internal) |
| TRIGGERS | A discrete event A changes the state of an element B that was already susceptible, initiating B's failure or a state transition. | Use for the moment of activation of a latent condition or the start of a protection or automation action. Requires a timing qualifier where the delay matters. | A utility voltage sag TRIGGERS UPS transfer to battery. | INITIATES (event to scenario or state) |
| PROPAGATES_VIA | The effect of A travels through an intermediate medium, resource or dependency C. | Names the conduit (busway, coolant loop, fabric plane, shared controller, identity service). Always paired with a PROPAGATES_TO step naming the receiving element. The conduit must exist as a dependency or resource in the architecture graph. | Pause frames PROPAGATE_VIA inter-switch links. | CONSUMES_RESOURCE or DEPENDS_ON (to the conduit) |
| PROPAGATES_TO | The effect reaches and impairs element or Service Outcome B. | Records the receiving element and the failure mode it now exhibits. A step that crosses a declared fault-domain boundary is a containment failure and shall be flagged. | TCS flow loss PROPAGATES_TO accelerator thermal protection. | PROPAGATES_TO |
| AMPLIFIES | A increases the magnitude, rate or extent of an effect that would occur anyway. | Non-linear interactions: resonance, synchronised demand, restart storms, alarm floods, positive feedback in control loops. Requires the amplification mechanism to be stated. | Synchronous training load swings AMPLIFY generator frequency excursions. | — (scenario-internal) |
| MASKS | A prevents detection or correct interpretation of B. | Applies to monitoring and alarm functions (M17–M20): sensor failure, alarm suppression, time skew, data loss, tampering. A masked step defers safeguard activation; record the masking duration. | Disabled BMS alarms MASK the rise in supply temperature. | — (scenario-internal; the monitored element is MONITORED_BY the masked safeguard) |
| BYPASSES | A path circumvents safeguard S without defeating S's function. | S still works on the paths it covers, but the scenario path does not pass through it (for example a maintenance bypass, an alternate access route, a direct-to-controller command that avoids the BMS limit). Indicates a coverage gap rather than a defective safeguard. | Vendor VPN directly to CDU controller BYPASSES BMS setpoint limits. | — (the safeguard's PROTECTED_BY scope is shown not to include the path) |
| DEFEATS | A causes safeguard S to fail to perform on a path it is intended to cover. | Use for loss of the safeguard's own dependency (power, sensing, logic, people), demand beyond its capacity or duration, or adversarial disabling. A DEFEATS step on a credited safeguard is decisive for the related claim. | Loss of control power DEFEATS automatic leak isolation. | CHALLENGES (event or finding to the safeguard claim) |
| CONTAINS | Safeguard S stops the effect from crossing a boundary. | Credit only with evidence for the demand, state and duration in the scenario. The residual state is recorded on the near side of the boundary. | PFC watchdog CONTAINS the pause storm to one switch port. | PROTECTED_BY |
| DELAYS | A increases the time before B occurs or before recovery completes. | Expresses ride-through and time-to-consequence (positive delays, such as stored thermal capacity) and recovery prolongation (negative delays, such as spares lead time). The delay shall be expressed as a duration parameter with basis. | Chilled-water storage DELAYS loss of heat rejection after chiller trip. | — (scenario-internal; delay parameter recorded) |
| RECOVERS | Action or safeguard R restores function or outcome B to an approved state. | Recovery steps follow the failure steps. Restoration is complete only when the restored state is validated; failover without restoration is CONTAINS or DELAYS, not RECOVERS. | Restart from last verified checkpoint RECOVERS training progress. | RECOVERS_THROUGH |
| REINTRODUCES | A recovery or change action re-creates the original or a new failure condition. | Mandatory for recovery-induced paths: restoration from a corrupted baseline, re-energisation into an uncleared fault, re-applying a defective configuration. | Restoring the latest switch backup REINTRODUCES the misconfigured QoS map. | — (scenario-internal; links the recovery step to the earlier cause) |
| CORRELATES_WITH | A and B co-occur or share an underlying cause, without asserted direct causation between them. | Common-cause and common-mode representation. The shared cause or shared fault domain shall be named; correlation without a named shared element is an UNKNOWN (U10). | CDU 1 and CDU 7 failures CORRELATE_WITH the same firmware release. | SHARES_FAULT_DOMAIN_WITH |
| CONFLICTS_WITH | Two actions, control objectives or assertions are mutually incompatible. | Control interaction (competing loops, contradictory automation), procedural conflict (fire strategy versus continuity) and evidential conflict. Evidential conflict also requires an AIDCF-008 conflict record. | Fire-alarm cause-and-effect shutdown of AHUs CONFLICTS_WITH continuity cooling for the adjacent hall. | CHALLENGES (for evidential conflict) |

### Table 15.2 — Qualifiers (logic, timing and causal character)

Qualifiers refine a step or a group of steps. Logic qualifiers apply to groups of CONTRIBUTES_TO steps; character qualifiers classify the cause so that common patterns can be searched and safeguards selected.

| **Qualifier** | **Type** | **Definition and usage** |
|---------------|----------|--------------------------|
| AND | Logic | All grouped contributors are required. Removing any one breaks the path; each is a candidate barrier point. |
| OR | Logic | Any one grouped contributor is sufficient. Each branch needs its own barrier or a common downstream barrier. |
| K_OF_N | Logic | At least k of n contributors are required (for example two of three generators failing to start defeat an N+1 plant). State k and n. |
| SEQUENCE | Logic / timing | Contributors must occur in a stated order (priority-AND). Used where the same events in another order are harmless, for example UPS bypass followed by utility sag. |
| INHIBIT | Logic | The step occurs only if a stated enabling condition is true (for example only when ambient wet-bulb exceeds design). |
| WITHIN(duration) | Timing | The effect must occur within the stated duration of the preceding step to propagate (for example generator acceptance before UPS energy is exhausted). Duration is a parameter with basis. |
| COMMON_CAUSE | Character | One cause acts on several elements simultaneously; requires the shared element to be named and SHARES_FAULT_DOMAIN_WITH asserted. |
| CASCADE | Character | The step's output becomes the initiating event of a further failure in a different element; used to chain domain transitions. |
| LATENT | Character | The condition existed before the initiating event and was not revealed by monitoring or testing; record when it was introduced if known. |
| ENABLING | Character | Condition that does not itself fail anything but makes the path possible (bypass active, alarm suppressed, reserve committed). |
| ESCALATION | Character | The consequence increases in severity band because a further condition is met (for example a leak reaches energised conductors). |
| SHARED_RESOURCE | Character | Propagation through a shared consumable or service: power bus, coolant loop, storage pool, fabric buffer, identity service, time source. |
| HUMAN_ACTION | Character | A human action or omission; requires the systemic contributors required by THF-REQ-014 to be recorded. |
| CONTROL_ACTION | Character | An automatic action by a control system, protection relay, scheduler or automation agent (correct or incorrect). |
| EXTERNAL_EVENT | Character | Originates outside the assessment boundary (utility, carrier, weather, supplier). |
| DEGRADATION | Character | Progressive loss of margin through ageing, fouling, wear, fade or drift; requires the degradation rate or the observation trend if known. |
| DEMAND_SURGE | Character | Demand exceeds the expected envelope (load step, restart storm, checkpoint storm, inference spike, alarm flood). |
| CONFIG_DRIFT | Character | Divergence of the actual configuration from the approved baseline without controlled change. |
| RECOVERY_INDUCED | Character | Arises from a recovery or restoration action; normally paired with REINTRODUCES or with a recovery-only dependency. |

## 16. Consequence families

Consequences are recorded in one or more families. Each family has measurable impact dimensions so that a consequence can be compared with the tolerance attached to a Service Outcome (AIDCF-003 §15; AIDCF-013 Service Outcome specification) and assigned a severity band (Part XI).

**THF-REQ-020** Each capability consequence shall state the consequence family, the affected Service Outcome, the impact dimensions measured or estimated, the tolerance it is compared with, the duration, the concentration (how much of the Capability Instance is affected), the assumptions and the confidence.

| **Consequence family** | **Definition** | **Measurable impact dimensions** | **Service Outcome family and tolerance link** |
|------------------------|----------------|----------------------------------|-----------------------------------------------|
| Life safety and health | Potential or actual harm to people from fire, explosion, toxic release, electrical shock or arc flash, pressurised fluid, biological hazard (for example water-borne pathogens from cooling towers) or structural failure. | People exposed; exposure type; proximity to energy or substance; time to safe egress; regulatory reportability. | Safety outcomes. No tolerance permits uncontrolled life-safety consequence; any credible path to it engages CG-04 regardless of continuity tolerances. |
| Capability availability | Loss or interruption of the ability to run the declared workloads. | Fraction of Capability Instance unavailable; interruption duration; number of jobs or tenants interrupted; time in DEGRADED or FAILED. | Availability outcomes; compared with tolerated interruption and degraded-mode availability. |
| Compute capacity | Reduction in usable accelerator capacity even where the service remains up. | Accelerators or nodes unusable; fraction of reserved or committed capacity lost; duration; stranded capacity created. | Capacity outcomes; compared with minimum usable capacity and resilient-capacity commitments. |
| Performance | Degradation of throughput, latency, job completion time or efficiency. | Training throughput (tokens or samples per second), step time, collective bandwidth, inference latency percentiles, checkpoint duration, throttled accelerator-hours. | Performance outcomes; compared with throughput, latency and completion tolerances. |
| Data/artifact integrity | Corruption, loss or inconsistency of training data, checkpoints, model artifacts, configuration or metadata. | Objects or checkpoints affected; age of last verified good state; training progress lost (accelerator-hours); detection latency; scope of contaminated outputs. | Integrity and recoverability outcomes; compared with tolerated progress loss and integrity requirements. |
| Isolation and security | Loss of tenant, cluster, management-plane, OT or physical separation, or unauthorised control. | Boundaries crossed; privileges obtained; systems reachable; duration of exposure; data or control actions affected. | Isolation outcomes; tolerance is normally zero crossing of declared boundaries; links to CG-15. |
| Physical damage | Damage to infrastructure or IT equipment. | Assets damaged; replacement cost class; lead time; contamination extent (coolant, smoke, suppressant residue). | Capacity and availability outcomes via repair time; recovery tolerance via lead time. |
| Environmental impact | Release to the environment or breach of resource limits. | Mass of refrigerant, glycol, fuel or electrolyte released; water abstraction and discharge beyond permit; emissions from extended generator running. | Efficiency and environmental outcomes; permit and regulatory limits act as hard tolerances. |
| Recovery complexity | Increase in the effort, time or uncertainty of restoration. | Mean and worst-case restoration time against recovery objective; number of recovery-only dependencies engaged; manual steps; specialist or OEM involvement required. | Recoverability outcomes; compared with recovery time and recovery-point tolerances. |
| Financial impact | Direct and indirect cost. | Lost accelerator-hours valued at internal rate; penalties and credits; repair and replacement; energy and fuel cost. | Derived from availability, capacity and performance consequences; used for prioritisation, never to offset gate results. |
| Contractual/regulatory impact | Breach of customer commitments, service levels, permits or regulatory obligations. | Commitments breached; notification deadlines triggered; permit conditions exceeded. | Customer commitments (GOV-05) and regulatory obligations act as externally imposed tolerances. |
| Strategic/sovereignty impact | Loss of declared location, operational control, supply or dependency constraints, or of strategic mission capability. | Workloads displaced outside declared jurisdiction; control exercised by undeclared parties; mission milestones missed. | Sovereignty outcomes; tolerance is normally zero breach of declared constraints. |
| Evidence and attribution loss | Inability to reconstruct, attribute or prove what happened or what state the infrastructure is in. | Telemetry and log gaps (duration, systems); time-correlation error; chain-of-custody breaks; records unrecoverable. | Observability outcomes; affects confidence and can create US2–US5 UNKNOWNs about subsequent claims. |

# Part IX - Safeguards and resilience

## 17. Safeguard functions

| **Function**       | **Examples** |
|--------------------|--------------|
| Anticipate         | Forecast, condition monitoring, capacity and demand planning, climate projection. |
| Prevent            | Access control, design margin, protection, maintenance, change control, signature validation. |
| Detect             | Sensors, telemetry, inspection, alarms, integrity checks. |
| Decide             | Logic, operator decision, escalation and authority. |
| Respond            | Transfer, isolation, throttling, power capping, draining and dispatch. |
| Contain            | Fault isolation, fire compartment, fabric segmentation, scheduler fault-domain placement. |
| Withstand          | Reserve, hardening, redundancy, ride-through energy and diversity. |
| Degrade gracefully | Priority, rate limiting, load shedding and orderly shutdown. |
| Recover            | Restart, rebuild, repair, checkpoint restore and data recovery. |
| Adapt              | Redesign, learning, and strengthened independence after events. |

## 18. Safeguard and barrier record

The barrier record extends the AIDCF-014 Safeguard profile (function, protectedSubject, activation, authority, dependencies, stateCoverage, failureModes, evidenceRefs, controlRefs).

| **Barrier field** | **Required content** |
|-------------------|----------------------|
| barrierId         | Stable identifier. |
| pathPosition      | Cause side (prevents the initiating event or failure mode), escalation (stops propagation), consequence side (limits outcome effect) or recovery side (restores). |
| objective         | Path condition altered, stated as the step and operator it interrupts (for example "CONTAINS step 3 at fault-domain boundary FD-NET-PLANE-A"). |
| activation        | Automatic, manual or procedural; trigger condition and required response time. |
| authority         | Who or what may activate, override or bypass it. |
| dependencies      | Power, sensing, control logic, communications, identity, people, supplier and data needs. A dependency shared with the path being interrupted is a common-mode finding. |
| applicableStates  | Operating states and transitions covered by evidence. |
| capacity/duration | Demand it withstands and for how long (for example energy, flow, bandwidth, staff hours). |
| failureModes      | How the barrier itself can fail (Part VII codes). |
| validation        | Safe validation level achieved (§19) and evidence objects. |
| controls          | AIDCF-007A controls that assure the barrier, with claim type sought. |
| confidence        | Evidence-bounded confidence (CONF-0 to CONF-4 with flags CONFLICTING, STALE). |
| residualExposure  | Path remaining after demonstrated action. |

**THF-REQ-021** A safeguard credited with interrupting a decisive path (Part XII) shall be linked to at least one AIDCF-007A control (safeguard GOVERNED_BY control, AIDCF-002 §18) whose claim type matches the credit sought: DESIGN for adequacy of the design, IMPLEMENTATION for as-built reconciliation, OPERATION for behaviour over a representative period, EFFECTIVENESS for behaviour under tested or observed adverse conditions, RESILIENCE for containment and recovery within tolerance.

**THF-REQ-022** A safeguard that shares a dependency with the path it is credited to interrupt shall not be credited for that path unless the shared dependency is shown, with evidence, not to be affected in the scenario.

## 19. Safe validation hierarchy

| **Level** | **Method** | **AIDCF-008 evidence classes typically produced** | **Assessment methods** | **Highest claim type normally supportable alone** |
|-----------|------------|---------------------------------------------------|------------------------|-------------------------------------------------|
| V0 | Document and configuration review | E1, E2 | DOCUMENT_REVIEW, RECONCILIATION | DESIGN; IMPLEMENTATION where E2 is extracted from the live system |
| V1 | Inspection and observation | E3, E6 | INSPECTION, OBSERVATION | IMPLEMENTATION |
| V2 | Historical event and telemetry analysis | E3, E7 | ANALYSIS, SAMPLING | OPERATION; EFFECTIVENESS where a real adverse event exercised the safeguard |
| V3 | Engineering analysis and simulation | E7 | ANALYSIS | DESIGN (EFFECTIVENESS only with a validated model and corroborating tests) |
| V4 | Tabletop and procedural exercise | E4, E6 | SCENARIO_EXERCISE, INQUIRY | OPERATION for procedural safeguards |
| V5 | Component functional test | E4 | TEST, REPERFORMANCE | EFFECTIVENESS for the component |
| V6 | Integrated systems test | E4, E5 | TEST, SCENARIO_EXERCISE | EFFECTIVENESS and RESILIENCE for the tested path and states |
| V7 | Live capability exercise where authorised and safe | E4, E3, E5 | SCENARIO_EXERCISE | RESILIENCE for the exercised Capability Instance |

**THF-REQ-023** Validation at V5–V7 involving hazardous energy, pressurised fluids, fire systems, batteries or production capability shall be authorised in writing by the asset owner and the competent person for the discipline, with a method statement, permit to work, rollback criteria and defined abort conditions (OPS-02, RES-05).

**THF-REQ-024** Where a safeguard cannot be validated above V3 without unacceptable risk, the residual limitation shall be recorded and the maximum claim type stated; the limitation shall not be concealed by aggregating other evidence.

# Part X - Analysis techniques

Techniques are selected for the question being asked, the lifecycle stage, the evidence available and the output required. Each technique below states where it fits in AIDCF and which AIDCF objects it produces. External standards are cited at document level; this standard does not reproduce their content.

**THF-REQ-025** The analysis plan for a Capability Instance shall record which techniques were applied to which Service Outcomes and Required Functions, and why; a technique's limitations listed below shall be addressed by a complementary technique where they are material.

**THF-REQ-026** Outputs of any technique that are used to support a claim shall be recorded as AIDCF-008 E7 (derived and analytical) evidence with their inputs, assumptions, model version and reviewer.

### T01 FMEA / FMECA

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Systematic bottom-up identification of how each Required Function or item can fail, the causes, local and end effects, and (FMECA) the criticality of each mode. |
| When to use in AIDCF | DESIGN and COMMISSION of power, thermal and fluid systems; CDU, manifold and rack-level liquid cooling; new accelerator platforms; any change introducing new equipment types. Appendix A is the seed catalogue. |
| Inputs | Required Function list; system decomposition (AIDCF-003); drawings, P&IDs, single-line diagrams; control narratives; vendor failure data where defensible; operating states. |
| Outputs | Mode–cause–effect rows; detection means; safeguard per mode; criticality (severity band, likelihood class, detectability) kept as separate attributes. |
| Mapping to AIDCF objects | Rows become FailureMode objects linked to RequiredFunction and AssetInstance; detection and mitigation become Safeguard objects; end effects become outcomeEffects on FailureScenario stubs. |
| Limitations | Single-failure orientation; weak on combinations, common cause, software and human interaction; RPN products are not permitted to decide assurance (Part XI). |
| Reference | IEC 60812:2018. |

### T02 Fault Tree Analysis (FTA)

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Top-down deduction of the combinations of events (minimal cut sets) that produce a defined top event such as "loss of heat removal to cluster partition P beyond tolerance". |
| When to use in AIDCF | For each Service Outcome whose loss is CS3 or higher; for verifying redundancy claims (N+1, 2N, distributed redundant) and identifying single points of failure and common-cause cut sets. |
| Inputs | Top event tied to a Service Outcome tolerance; system logic; dependency graph; failure-mode data from T01; state assumptions. |
| Outputs | Fault tree; minimal cut sets; single-element cut sets (single points); optional quantification where data are defensible. |
| Mapping to AIDCF objects | Gates map to logic qualifiers (AND, OR, K_OF_N, INHIBIT); basic events map to FailureMode objects; cut sets become FailureScenario candidates; single-element cut sets raise findings against CG-03 and CG-09. |
| Limitations | Static logic; poor at sequence and timing (use T10 or T03); quantification is sensitive to common-cause assumptions (use T09); trees reflect the analyst's model and can omit unmodelled dependencies. |
| Reference | IEC 61025:2006. |

### T03 Event Tree Analysis (ETA)

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Forward, inductive analysis of the sequence of safeguard successes and failures following an initiating event, producing outcome sequences. |
| When to use in AIDCF | Initiating events with ordered automatic responses: utility loss (UPS transfer → generator start → load acceptance → retransfer); CDU pump trip (standby start → flow restored → IT throttling); fire detection (pre-alarm → confirmation → suppression → shutdown interfaces). |
| Inputs | Initiating event; ordered list of safeguards with success criteria and time windows; state assumptions. |
| Outputs | Branch sequences with end states and consequence families; identification of sequences ending beyond tolerance. |
| Mapping to AIDCF objects | Each branch is a FailureScenario; each node is a Safeguard with pathPosition; branch time windows become WITHIN qualifiers; end states become residualState. |
| Limitations | Assumes the order of responses is known; branch independence must be justified; becomes unwieldy with many safeguards. |
| Reference | IEC 62502:2010. |

### T04 Bow-tie analysis

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Visualise threats and hazards leading to a central top event on the left, consequences on the right, with prevention and mitigation barriers and the escalation factors that degrade them. |
| When to use in AIDCF | Communicating and governing high-severity hazards: battery thermal runaway, coolant leak near energised equipment, arc flash, OT compromise. Useful for linking barriers to owners and controls. |
| Inputs | Top event; threat lines; consequence lines; barrier inventory; escalation factors and their controls. |
| Outputs | Barrier map with owner, dependency and status per barrier; escalation-factor list. |
| Mapping to AIDCF objects | Barriers become Safeguard objects with pathPosition cause side or consequence side; escalation factors become ENABLING or ESCALATION qualifiers and DEFEATS steps; barrier owners satisfy CG-13 evidence. |
| Limitations | Qualitative; does not capture timing or combinations rigorously; risks presenting barriers as independent when they share dependencies. |
| Reference | Described in IEC 31010:2019 (technique family). |

### T05 HAZOP-style study

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Structured, guideword-driven review of deviations (more, less, no, reverse, other than, early, late) in process parameters of a defined node. |
| When to use in AIDCF | Liquid-cooling loops (TCS and facility water), fuel systems, refrigerant circuits, water treatment, and control sequences; at DESIGN and before CHANGE such as expansion tie-ins. |
| Inputs | P&IDs; cause-and-effect matrices; control narratives; materials and fluid specifications; operating states. |
| Outputs | Deviation records with causes, consequences, safeguards and actions. |
| Mapping to AIDCF objects | Deviations become FailureMode instances (for example "less flow" → M07 on RF-THM-02); actions become Finding and Action objects; safeguards become Safeguard objects. |
| Limitations | Resource-intensive; dependent on team competence and node definition; weaker for software logic and cyber manipulation (complement with T16 and T19). |
| Reference | IEC 61882:2016. |

### T06 What-if / SWIFT

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Rapid structured brainstorming of "what if" questions against a system or procedure, organised by prompt categories. |
| When to use in AIDCF | Early PLAN/DESIGN screening; MAINTENANCE method statements; reviewing procedures where full HAZOP is disproportionate. |
| Inputs | System description; procedure; prompt list (utilities, human factors, controls, external events). |
| Outputs | Scenario candidates, safeguards, actions. |
| Mapping to AIDCF objects | Scenario candidates enter the FailureScenario backlog with status DRAFT; actions become Action objects. |
| Limitations | Completeness depends on facilitator and prompts; not sufficient alone for CS4–CS5 consequences. |
| Reference | Described in IEC 31010:2019. |

### T07 Cause-consequence analysis

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Combines fault-tree reasoning (causes of each safeguard failure) with event-tree reasoning (consequence sequences) in one diagram. |
| When to use in AIDCF | Sequences where the failure of each response has its own complex causes, for example generator load acceptance failure after UPS transfer during a synchronous load swing. |
| Inputs | As T02 and T03. |
| Outputs | Combined diagram; sequences with cut sets for each branch failure. |
| Mapping to AIDCF objects | As T02 and T03; branch-failure cut sets attach as DEFEATS steps to safeguards. |
| Limitations | Complex to build and review; quantification shares FTA limitations. |
| Reference | Described in IEC 31010:2019. |

### T08 Dependency graph analysis

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Traverse the AIDCF-003 dependency and fault-domain graph to find upstream and downstream reach, shared providers, concentration, single points and recovery-only dependencies. |
| When to use in AIDCF | Always, for every assessed Capability Instance (it is part of the default hybrid). Mandatory evidence base for CG-03 and CG-09. |
| Inputs | Asset, system, interface, resource, dependency and fault-domain records with confidence and validity; as-built reconciliation. |
| Outputs | Reachability sets per Required Function; shared-dependency and SHARES_FAULT_DOMAIN_WITH sets; centrality and concentration measures; recovery-only dependency lists. |
| Mapping to AIDCF objects | Produces Dependency and FaultDomain findings; candidate common-cause groups for T09; PROPAGATES_VIA conduits for scenarios. |
| Limitations | Only as complete as the graph; hidden or undocumented dependencies (U10) are invisible to traversal and must be sought by inspection and reconciliation. |
| Reference | AIDCF-003; AIDCF-014. |

### T09 Common-cause analysis (including beta-factor)

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Identify shared causes that can defeat redundancy (shared design, firmware, configuration source, maintenance team, environment, location, supplier) and, where quantification is used, estimate the common-cause contribution. |
| When to use in AIDCF | Any redundancy or diversity claim supporting CG-05, CG-06, CG-08 or CG-09; fleet-wide firmware and configuration management; homogeneous CDU, UPS and switch fleets. |
| Inputs | Redundancy groups; T08 shared-dependency sets; design, supplier and maintenance records; defence checklist (separation, diversity, procedures, competence, environmental control). |
| Outputs | Common-cause groups; defences scored against checklist; beta-factor estimate where justified. |
| Mapping to AIDCF objects | Common-cause groups become SHARES_FAULT_DOMAIN_WITH relationships and CORRELATES_WITH scenario steps; defences become Safeguard objects (for example staged rollout, diverse controllers). |
| Limitations | Beta-factor values from safety-instrumented-system practice are not directly transferable to IT and AI fleets; software and configuration common cause is poorly represented by hardware-oriented models. Values shall be treated as parameters with basis, not facts. |
| Reference | IEC 61508-6 (common-cause estimation guidance); NUREG/CR-5485 (common-cause modelling guidance). |

### T10 State-transition and Markov analysis

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Model a system as states and transitions (failure, repair, switchover, maintenance) to analyse sequence, repair and time-dependent behaviour, and (Markov) to compute availability under stated rates. |
| When to use in AIDCF | Concurrent maintenance claims; repairable redundant systems where repair time and spares lead time matter; AIDCF operating-state transitions (NORMAL → MAINTENANCE → DEGRADED); evaluating exposure windows. |
| Inputs | State definitions (AIDCF-003 §45 plus system-specific substates); transition triggers and rates or durations; repair and spare assumptions. |
| Outputs | State diagrams; time in exposure states; availability estimates with sensitivity. |
| Mapping to AIDCF objects | States map to OperatingState objects; transition triggers map to initiating events; exposure windows qualify scenario WITHIN and SEQUENCE qualifiers. |
| Limitations | State explosion for large systems; Markov models assume memoryless transitions that rarely hold for ageing and human action; rates are often weakly evidenced. |
| Reference | IEC 61165:2006. |

### T11 Reliability block diagram (RBD)

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Represent success logic of a Required Function as series and parallel blocks to identify structure and estimate availability. |
| When to use in AIDCF | Early design comparison of topologies (for example block-redundant versus distributed-redundant UPS; N+1 versus N+2 CDUs per row); explaining redundancy claims to decision makers. |
| Inputs | Functional success criteria; component structure; availability data where defensible. |
| Outputs | Success diagram; single points; availability estimate. |
| Mapping to AIDCF objects | Blocks map to InfrastructureSystem and AssetInstance; parallel blocks become redundancy claims requiring T09 for independence. |
| Limitations | Assumes block independence; cannot express sequence, transfer behaviour or shared control. |
| Reference | IEC 61078:2016. |

### T12 Root-cause analysis (RCA)

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Retrospective identification of causal factors and systemic contributors of an event or near miss. |
| When to use in AIDCF | After incidents and near misses (OPS-04, RES-05); when an event contradicts a credited safeguard; to update scenarios and reassessment triggers. |
| Inputs | Timeline; telemetry and logs with trusted time; interviews; configuration history; physical evidence. |
| Outputs | Causal factor chart; root and contributing causes; corrective actions. |
| Mapping to AIDCF objects | Event objects; Findings; CHALLENGES relationships against safeguard claims; ReassessmentTrigger; updated FailureScenario. |
| Limitations | Retrospective; quality limited by evidence retention and time correlation (RF-EVA-01); prone to stopping at human error (prohibited by THF-REQ-014). |
| Reference | IEC 62740:2015. |

### T13 Capability impact analysis

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Translate technical effects into Service Outcome consequences: which workloads, tenants and outcomes are affected, by how much and for how long, and what minimum outcome must be preserved. |
| When to use in AIDCF | Always (default hybrid); framing every scenario's end effect; defining graceful-degradation priorities (RES-01). |
| Inputs | Capability Instance, Service Outcomes and tolerances (CG-01); workload model (job size, synchronisation, checkpoint interval); scheduler placement. |
| Outputs | Consequence statements in families (Part VIII §16) with severity band; minimum service outcome. |
| Mapping to AIDCF objects | outcomeEffects on FailureScenario; ServiceOutcome tolerance references; severity band. |
| Limitations | Depends on accurate workload and placement knowledge, which changes daily; must be refreshed when the job mix changes. |
| Reference | AIDCF-003 §15; AIDCF-013 Service Outcome specification. |

### T14 Scenario stress analysis

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Push a scenario beyond design assumptions (higher ambient, longer outage, larger load step, slower repair, second failure) to locate capacity cliffs and margins. |
| When to use in AIDCF | Resilience claims; climate adaptation (ENV-06); growth (CAP-04); fuel and water autonomy; checkpoint restore at full-cluster scale. |
| Inputs | Base scenario; stressor set and ranges; capacity assertions with derating. |
| Outputs | Margin-to-cliff per stressor; threshold at which outcome breaches tolerance; sensitivity ranking. |
| Mapping to AIDCF objects | Capacity cliff findings; parameters for capability profiles; ReassessmentTrigger thresholds. |
| Limitations | Choice of stressors is judgemental; results are only as good as the underlying models. |
| Reference | IEC 31010:2019 (scenario analysis family). |

### T15 Validated digital-twin simulation

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Use a calibrated model of electrical, thermal, hydraulic or network behaviour to explore transient and combined scenarios that cannot be safely tested live. |
| When to use in AIDCF | Thermal transients after CDU or chiller loss; generator and UPS response to AI load profiles; fabric congestion under collective patterns; only where the model has been validated against measured behaviour. |
| Inputs | Model with version and calibration record; measured validation data; boundary conditions; scenario script. |
| Outputs | Time-series predictions; time-to-limit; margin estimates with stated uncertainty. |
| Mapping to AIDCF objects | E7 evidence; DELAYS durations; capacity assertions; supports DESIGN claims and corroborates EFFECTIVENESS claims. |
| Limitations | An unvalidated model is not evidence of behaviour; validity is limited to the calibrated range; model drift after physical change. |
| Reference | No single governing standard; validation shall be documented as E7 with AIDCF-008 quality ratings. |

### T16 System-Theoretic Process Analysis (STPA)

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Identify unsafe control actions and their causal scenarios by modelling the system as a hierarchical control structure (controllers, actuators, sensors, feedback). |
| When to use in AIDCF | Interactions between automation layers: BMS, CDU controllers, EPMS, IT power capping, schedulers and AI-enabled automation agents; cases where each component works as specified but the combination is unsafe. |
| Inputs | Losses (Service Outcome and safety losses); hazards; control structure; control actions and feedback paths; process models. |
| Outputs | Unsafe control actions (not provided, provided incorrectly, wrong timing or order, applied too long or stopped too soon); loss scenarios; constraints. |
| Mapping to AIDCF objects | Unsafe control actions map to M09, M10, M11, M03 and M30 failure modes on control functions; loss scenarios become FailureScenario objects with CONTROL_ACTION qualifiers; constraints become Safeguard objects linked to SEC-06, THM-06 and OPS-05 controls. |
| Limitations | Requires a good control-structure model; less suited to physical degradation; outputs are qualitative. |
| Reference | STPA Handbook (Leveson and Thomas, 2018). |

### T17 Layer of Protection Analysis (LOPA)

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Semi-quantitative check of whether the independent protection layers on a hazard scenario reduce frequency of a consequence to a tolerable level. |
| When to use in AIDCF | Life-safety and hazardous-energy scenarios (CG-04): battery thermal runaway, fuel system fire, refrigerant release in occupied space, overpressure in liquid-cooling loops. |
| Inputs | Initiating event frequency (with basis); consequence; candidate protection layers; independence and effectiveness criteria; tolerability criteria set by the owner. |
| Outputs | Credited independent protection layers; gap to target; requirement for further layers or safety-instrumented functions. |
| Mapping to AIDCF objects | Independent protection layers become Safeguard objects with independence claims; gaps become Findings against CG-04. |
| Limitations | Order-of-magnitude method; independence assumptions must be evidenced; tolerability criteria are owner and jurisdiction specific and are not set by AIDCF. |
| Reference | CCPS Layer of Protection Analysis guidance; IEC 61511 (series) for safety-instrumented functions. |

### T18 Attack trees

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Decompose an adversary goal (for example "raise TCS supply temperature beyond limit without alarm") into alternative and combined sub-goals and techniques. |
| When to use in AIDCF | Deliberate-threat scenarios against OT, control planes and physical security; prioritising CG-15 and SEC-02 safeguards. |
| Inputs | Adversary goal; architecture and access paths; known techniques (for example MITRE ATT&CK for ICS); safeguards. |
| Outputs | Tree of AND/OR attack steps; cheapest or least-detectable paths; safeguards per node. |
| Mapping to AIDCF objects | Root goals map to Threat objects; leaves to initiating events; AND/OR to logic qualifiers; safeguards to Safeguard objects with BYPASSES and DEFEATS analysis. |
| Limitations | Adversary capability and cost estimates are uncertain; trees omit unknown techniques; must be refreshed with threat intelligence. |
| Reference | MITRE ATT&CK for ICS (knowledge base); IEC 31010:2019. |

### T19 OT and control-plane threat modelling (STRIDE adapted, zones and conduits)

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Enumerate threats per element and data flow of the facility and AI control planes using STRIDE categories (spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege), extended for OT with loss of view, loss of control and manipulation of view, organised by security zones and conduits. |
| When to use in AIDCF | DESIGN and CHANGE of BMS/EPMS/CDU/PLC networks, cluster managers, fabric and storage controllers, remote-support paths and automation agents (SEC-01 to SEC-06, SUP-06). |
| Inputs | Data-flow and zone/conduit diagrams; identity and privilege model; remote-access paths; asset inventory with firmware. |
| Outputs | Threat list per element and conduit; required security levels per zone; mitigations. |
| Mapping to AIDCF objects | Threat objects; FailureScenario stubs with M09, M17, M18 and M30 modes; Safeguard objects mapped to SEC and SUP controls; evidence for CG-15. |
| Limitations | Enumerative rather than consequence-driven; must be joined to T13 to prioritise by Service Outcome; STRIDE was designed for software and needs the OT extensions to be meaningful. |
| Reference | IEC 62443-3-2:2020 (security risk assessment for zones and conduits); NIST SP 800-82 Rev. 3 (OT security guidance). |

### T20 Engineering transient studies (electrical and thermal-hydraulic)

| **Aspect** | **Content** |
|------------|-------------|
| Purpose | Discipline studies that establish whether physical systems withstand faults and transients: short-circuit, protection coordination, arc-flash incident energy, load-flow, harmonic, transient stability and generator load acceptance; hydraulic transient (water hammer) and thermal transient analysis for liquid cooling. |
| When to use in AIDCF | DESIGN and CHANGE affecting POW and THM; any increase in AI load density or change in load dynamics; evidence for CG-04, CG-05 and CG-06. |
| Inputs | As-built single-line diagrams and P&IDs; protection settings; equipment data; measured or modelled AI load profiles (step size, ramp rate, oscillation frequency content). |
| Outputs | Study reports with settings, margins and constraints; identified miscoordination and transient risks. |
| Mapping to AIDCF objects | E7 evidence for POW-04, POW-05, THM-01 and THM-03 controls; parameters for capability profiles; findings when as-built differs from study basis. |
| Limitations | Valid only for the modelled configuration and load profile; studies based on conventional diversified IT loads may not represent synchronous AI loads; require competent engineers. |
| Reference | IEEE 1584 (arc-flash calculation); ISO 8528-5 (generating-set transient performance); IEC 62040-3 (UPS performance). |

### Default AIDCF hybrid

Capability impact analysis (T13) + dependency graph analysis (T08) + selected FMEA/FMECA (T01) + top-event analysis for each CS3+ Service Outcome (T02 or T03) + common-cause analysis for every redundancy claim (T09) + barrier analysis (T04 or T17 for life safety) + control-interaction analysis where automation spans domains (T16) + OT threat modelling for control planes (T19) + state-based scenario validation (T10, T14). No single technique is sufficient by default.

# Part XI - Criticality and uncertainty

**THF-REQ-027** Consequence severity, likelihood, detectability and confidence shall be recorded as separate attributes.

**THF-REQ-028** A risk priority number or other arithmetic product shall not by itself determine a control result, gate result or decision.

**THF-REQ-029** Critical gates and CS4–CS5 consequences shall not be averaged away by scores.

**THF-REQ-030** Quantitative probability shall be used only where data, model and assumptions are defensible and recorded as E7 evidence with their basis.

## 20. Consequence severity bands

Consequence severity bands are designated CS0–CS5 (v1.0 designations S0–S5 are retired because S0–S5 denotes evidence sufficiency in AIDCF-008).

| **Band** | **Name** | **Capability interpretation** | **Assurance effect** |
|----------|----------|-------------------------------|----------------------|
| CS0 | Negligible | No material outcome effect. | Record only. |
| CS1 | Minor | Local effect; outcome within requirement. | Analysed at function level. |
| CS2 | Moderate | Recoverable degradation within approved tolerance. | Safeguards require OPERATION evidence. |
| CS3 | Major | Required Service Outcome breached beyond tolerance. | Path is decisive (Part XII); credited safeguards require EFFECTIVENESS or RESILIENCE evidence. |
| CS4 | Critical | Extended or concentrated loss of capability, serious safety exposure or strategic impact. | Decisive; engages the relevant critical gate. |
| CS5 | Catastrophic | Fatality potential, loss of mission or systemic irreversible consequence. | Decisive; engages CG-04 where life safety is involved; decision ceiling as defined in AIDCF-010. |

Likelihood is recorded as a qualitative class with basis (for example "has occurred in this fleet", "has occurred in industry", "credible but not observed", "requires multiple independent failures"). Detectability is recorded as the time between failure-mode onset and alarm reaching an authorised responder relative to time-to-consequence.

## 21. Uncertainty treatment

| **Uncertainty**      | **Treatment** | **Typical UNKNOWN type (AIDCF-008)** |
|----------------------|---------------|--------------------------------------|
| Model                | Record alternate structures and test each. | U9 Interpretation unresolved |
| Parameter            | Use range and sensitivity (T14). | U8 Method uncertain |
| Evidence gap         | Preserve UNKNOWN. | U1 Missing, U2 Inaccessible |
| Temporal             | State observation time and validity interval. | U3 Stale |
| Configuration        | Separate intended, as-built, commissioned and observed baselines. | U4 Conflicting, U5 Coverage gap |
| Expert disagreement  | Retain dissent and basis. | U9 Interpretation unresolved, U4 Conflicting |
| Rare event           | Avoid false precision; use scenario and bounding. | U5 Coverage gap |
| Emergent interaction | Use scenario, graph, STPA and stress analysis. | U10 Dependency unknown, U9 |
| Provenance           | Verify source of vendor or provider claims. | U6 Source unverified, U7 Integrity uncertain |

# Part XII - UNKNOWN permission and path-resolution rules

This Part defines exactly where an explicit UNKNOWN may appear in a scenario and where a failure path must be resolved before it can support a positive claim. It applies the AIDCF-008 UNKNOWN types (U1–U10) and the canonical UNKNOWN severity scale (US1–US5). Gate criteria and decision ceilings are defined in AIDCF-010; CG-12 (Critical UNKNOWN) is the gate that holds unresolved US4 and US5 UNKNOWNs visible.

## 22. Definitions

| **Term** | **Definition** |
|----------|----------------|
| Decisive path | A scenario path that (a) without credited safeguards would produce a CS3 or higher consequence on an in-scope Service Outcome, or (b) traverses the scope of any critical gate CG-01 to CG-10 or CG-13 to CG-15, or (c) is cited in the assurance case as interrupted by a safeguard in support of a positive claim. |
| Credited safeguard | A safeguard on which the assurance case relies to interrupt a decisive path. |
| Interruption point | The step at which the credited safeguard acts (prevents, contains or limits) such that the residual state is within tolerance. |
| Upstream segment | All path elements from the initial state and initiating event up to and including the interruption point, together with the credited safeguard's activation, dependencies, state coverage and capacity/duration. |
| Downstream segment | Path elements after the interruption point that would only be reached if the credited safeguard failed. |
| Resolved path | A decisive path whose upstream segment contains no UNKNOWN element, whose credited safeguard has evidence meeting the floor of its linked control's evidence profile for the claim type sought, and whose residual state is shown to be within tolerance. |
| Positive claim | Any of: a control result of CONFORMING at OPERATION, EFFECTIVENESS or RESILIENCE claim type that relies on the scenario; a gate result of PASS whose criteria rely on the scenario; a decision state of REASONABLY_ASSURED or CONDITIONALLY_ASSURED whose argument cites the scenario. |

## 23. Field classes and UNKNOWN permission

| **Class** | **Scenario fields** | **UNKNOWN permitted?** | **Rule** |
|-----------|---------------------|------------------------|----------|
| A — Framing | scenarioId, capabilityInstance, serviceOutcomes (with tolerances), assessmentBoundary, architectureBaseline | No | A scenario without these cannot be submitted (status remains DRAFT). If the underlying Capability Instance, Service Outcome, tolerance or boundary is itself UNKNOWN, that is recorded once as an UNKNOWN Record against the capability (not the scenario); it is US5 by the canonical test and caps the decision at INCONCLUSIVE (CG-01, CG-02). |
| B — Path structure | initial operating state, initiating event and source class, failure mode at each step, ordered path steps and operators, fault domains traversed, operating states traversed, credited safeguards and their dependencies, capability consequence | Yes, as an UNKNOWN Record with type and severity | Permitted so the scenario remains visible, but an UNKNOWN in the upstream segment of a decisive path prevents that path from supporting a positive claim (§24). Severity is assigned by §25. |
| C — Explanation | failure cause, predisposing conditions, threat-actor attribution, alternate hypotheses, likelihood class | Yes | Permitted where the credited safeguard is cause-agnostic and source-agnostic for the path (it acts on the failure mode or effect, whatever its cause) and its evidence covers the demand range of the credible causes. Otherwise the cause becomes part of the upstream segment and class B rules apply. |
| D — Assurance support | residual state, recovery path, evidence references, linked controls, owners | Yes, with mandatory gate evaluation | Permitted only with an UNKNOWN Record. An UNKNOWN residual state or evidence on a decisive path is equivalent to an unresolved upstream element. An UNKNOWN owner of a credited safeguard engages CG-13. An UNKNOWN recovery path on a decisive path engages CG-10. |
| — Mandatory, never UNKNOWN | confidenceAndUnknown record, criticalGates (derived by rule), reassessmentTriggers | No | These fields describe the analysis itself and are always populated; "none identified" is an allowed value for reassessment triggers only with reviewer sign-off. |

**THF-REQ-031** Class A fields of a submitted scenario shall not be UNKNOWN; where the capability framing is itself UNKNOWN, the UNKNOWN shall be recorded against the Capability Instance with severity US5.

**THF-REQ-032** Every UNKNOWN in a class B, C or D field shall be recorded as an UNKNOWN Record that states subject, missing attribute, UNKNOWN type (U1–U10), severity (US1–US5), reason, potential consequence, evidence needed, owner if known, status and gate impact (AIDCF-008 EVM-REQ-035).

**THF-REQ-033** A failure cause may remain UNKNOWN only where the credited safeguard acts independently of the cause and its evidence covers the range of demands the credible causes impose; otherwise the cause shall be resolved or classified under §25 as an upstream-segment UNKNOWN.

## 24. Path resolution before a positive claim

**THF-REQ-034** A decisive path shall be resolved before it is cited in support of a positive claim. Specifically, for each decisive path the following shall be known, not UNKNOWN: the initial operating state; the initiating event class; the failure mode at every step of the upstream segment; every dependency and fault-domain edge in the upstream segment; the identity, activation condition, authority, dependencies, state coverage and capacity/duration of the credited safeguard; and the residual state after interruption.

**THF-REQ-035** Elements of the downstream segment of a decisive path may remain UNKNOWN only if the credited safeguard's effectiveness has been demonstrated at the claim type sought and the downstream UNKNOWN could not change the residual-state conclusion; such UNKNOWNs are classified US1 or US2.

**THF-REQ-036** Where more than one safeguard is credited in series on a decisive path, the path shall be resolved up to the first safeguard whose demonstrated effectiveness alone keeps the residual state within tolerance; safeguards beyond that point may carry UNKNOWNs classified under §25 but shall not be counted toward the positive claim.

**THF-REQ-037** A scenario whose decisive path is unresolved shall be reported with its UNKNOWN Records and shall not be omitted from the assurance case, reworded as low likelihood, or replaced by an assumed favourable value (AIDCF-003 IOT-REQ-056).

The resolution test is applied in this order:

1. Identify whether the path is decisive (§22).
2. Identify the credited safeguard and the interruption point.
3. Check every upstream-segment element for UNKNOWN; check the credited safeguard's evidence against its control's evidence profile floor (sufficiency and quality bands, state coverage) for the claim type.
4. Check whether the safeguard shares a dependency with the path (Part IX §18); if so the shared dependency is an upstream element.
5. If all are known and evidenced, the path is resolved and may support the positive claim. If not, classify each unresolved element by §25 and apply its decision effect.

## 25. Severity of scenario UNKNOWNs

The canonical severity tests are applied top-down; the first that applies determines severity. The table states how the tests are interpreted for scenario elements.

| **Severity** | **Canonical test** | **Scenario interpretation** | **Effect** |
|--------------|--------------------|-----------------------------|------------|
| US5 Systemic | Affects the boundary, a Capability/Outcome definition, or two or more gates | The UNKNOWN concerns capability framing (class A substance), or an upstream-segment element whose resolution could change the result of two or more gates. Typical cases: an undiscovered shared dependency between power and cooling paths (CG-05 and CG-06); a common identity or time service whose fault domain is unknown and which every recovery path uses (CG-10 and CG-15); the operating state of the facility unknown during a period relied on for OPERATION evidence across domains. | Decision no higher than INCONCLUSIVE. |
| US4 Critical | Affects a gate-critical control or a gate criterion (CG-12 trigger) | An upstream-segment element of a decisive path within a single gate scope, or evidence for a credited safeguard linked to a control mapped CRITICAL to that gate. Typical cases: generator load-acceptance behaviour under the site's measured AI load profile not established (CG-05); TCS thermal ride-through after CDU pump loss not established (CG-06); PFC watchdog behaviour not verified on the deployed switch software (CG-08 or CG-09). | The affected gate cannot PASS and is UNKNOWN; CG-12 is engaged; decision no higher than LIMITED or INCONCLUSIVE according to the gate ceiling in AIDCF-010. |
| US3 Material | Could change a control result or a decision condition, but no gate | An upstream-segment element of a path that is decisive only under criterion (c) of §22 for a non-gate claim; or a class C cause UNKNOWN where the safeguard is cause-agnostic but its evidence covers only part of the demand range. | Decision no higher than CONDITIONALLY_ASSURED, with the condition recorded. |
| US2 Moderate | Affects confidence but not any result | Downstream-segment UNKNOWNs behind a demonstrated safeguard where resolution would change confidence in the residual state but not the conclusion; non-decisive path elements relevant to more than one Service Outcome. | Confidence ceiling CONF-2 for the affected claims. |
| US1 Low | No plausible effect on any result or condition | Attribution of a source where safeguards are source-agnostic; downstream elements with no plausible effect; historical cause of a past event already superseded by redesign. | Record only. |

**THF-REQ-038** Each scenario UNKNOWN shall be assigned severity by applying the tests in §25 top-down; an UNKNOWN shall not be downgraded on the basis of assumed low likelihood.

**THF-REQ-039** A US4 or US5 scenario UNKNOWN shall be presented to CG-12 with one of the following dispositions recorded: resolved (evidence obtained, UNKNOWN closed); bounded (a further safeguard demonstrated effective independently of the unknown element, so that the element is moved to the downstream segment and reclassified with justification); boundary changed (the affected scope excluded through an approved boundary change, with CG-02 re-evaluated); or carried (the UNKNOWN remains open and the gate and decision effects in §25 apply). A disposition of "carried" shall not be represented as resolution.

## 26. UNKNOWN type guidance for scenarios

| **Type** | **Typical scenario occurrence** |
|----------|---------------------------------|
| U1 Missing | No integrated test record for the transfer sequence; no restore test at full-cluster scale. |
| U2 Inaccessible | Carrier will not disclose fibre routes; colocation provider will not share plant telemetry; OEM will not release firmware defect details. |
| U3 Stale | Protection study predates the AI load increase; dependency map predates expansion tie-in. |
| U4 Conflicting | EPMS and BMS disagree on the feed a rack is connected to; vendor and operator disagree on CDU failure behaviour. |
| U5 Coverage gap | Safeguard tested in NORMAL but not MAINTENANCE; generator tested with load bank but not with dynamic AI load. |
| U6 Source unverified | Supplier attestation of firmware provenance not independently verified. |
| U7 Integrity uncertain | Logs from a compromised BMS used as evidence of setpoint history. |
| U8 Method uncertain | Leak detection test method does not state fluid, volume or location. |
| U9 Interpretation unresolved | Experts disagree whether observed oscillation is governor instability or load behaviour. |
| U10 Dependency unknown | Whether diverse circuits share a duct; whether break-glass credentials depend on the identity provider. |

# Part XIII - Fifteen-domain scenario families

Each domain lists the scenario families that shall be considered for every in-scope Capability Instance. The analysis focus states what is specific to that family; the generic scenario minimum record (§11) applies to all. Required Function references are to Appendix A. Families carried over from the v1.0 eight-domain catalogue are marked †.

**THF-REQ-040** The analysis plan shall record, for each scenario family below, whether it was analysed, screened out with rationale, or deferred with an UNKNOWN Record.

## 27. GOV — Governance, Accountability and Assurance Direction

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| Decision authority unavailable in an emergency | Whether a person with authority to shed load, invoke continuity or accept risk can be reached within the time-to-consequence, out of hours, when the identity and communication services are themselves degraded. | CG-13 | RF-GOV-01 |
| Exception outlives its rationale | Temporary risk acceptances (bypasses, deferred maintenance, overdue patches) that persist past expiry and become predisposing conditions for other scenarios. | CG-13, CG-14 | RF-GOV-02 |
| Continuity versus safety conflict | Whether governance has pre-decided priorities where continuity of training conflicts with life-safety or equipment-protection actions (for example EPO, fire strategy). | CG-04, CG-13 | RF-GOV-01 |

## 28. CAP — AI Capability, Service Outcome and Demand Management

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| Synchronous load swing | Magnitude, ramp rate and periodicity of training-job power swings versus the ride-through and control bandwidth of utility interface, UPS, generators and cooling plant. | CG-05, CG-06 | RF-CAP-01, RF-POW-06 |
| Envelope exceedance by workload change | New model architectures or accelerator generations change rack power, heat flux or coolant demand beyond the envelope assumed in design. | CG-01, CG-06, CG-14 | RF-CAP-01, RF-CAP-02 |
| Reserve consumed by growth † (expansion creates stranded compute) | Committed or resilient capacity used for growth so that N+1 exists on paper only; stranded compute because one dependency (power, cooling, fabric ports) limits the others. | CG-05, CG-06 | RF-CAP-02 |
| Outcome definition gap | Service Outcomes stated without tolerances or without operating states, so scenarios cannot be judged decisive. | CG-01 | — |

## 29. DEP — Dependency, Concentration and External Reliance Management

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| Hidden shared dependency † | Nominally independent paths that share a controller, route, source, configuration repository, person or supplier (T08, T09). | CG-03, CG-09 | RF-DEP-01 |
| External provider correlated failure | Utility, carrier, water and fuel providers failing together under a regional event. | CG-03 | RF-DEP-02 |
| Recovery-only dependency | Dependencies used only during restoration (image repositories, identity, OEM support, spares, black-start services) that are not exercised in NORMAL. | CG-03, CG-10 | RF-DEP-01, RF-RES-03 |
| Responsibility gap across boundary † | Colocation, managed service or cloud boundary where the dependency owner, evidence rights and notification duties are unclear. | CG-03, CG-13 | RF-DEP-02 |

## 30. PHY — Physical Site, Building and Security Infrastructure

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| Unauthorised entry † | Paths to plant rooms, meet-me rooms, fibre entry points and fuel and water systems, not only to data halls. | CG-15 (where it reaches control points), CG-09 | RF-PHY-01 |
| Insider sabotage † | Authorised staff or contractors operating switchgear, valves or EPO; two-person rule and attribution. | CG-04, CG-13 | RF-PHY-01, RF-PHY-02 |
| Surveillance blind spot † | Coverage and retention gaps at critical plant and asset-movement points. | CG-11 | RF-PHY-02 |
| Asset removal † | Theft of accelerators, media or spares; custody of decommissioned storage. | CG-08 | RF-PHY-02 |
| Security-zone collapse † | Fire-alarm door release, emergency egress or maintenance access that opens multiple zones at once. | CG-04, CG-09 | RF-PHY-01 |
| Emergency-access conflict † | Security measures delaying fire service or responder access; responder access defeating security. | CG-04 | RF-PHY-01, RF-PHY-04 |
| Structural overload † | Rack mass of liquid-cooled rack-scale systems, filled manifolds and CDUs versus floor and slab capacity; seismic anchorage. | CG-04, CG-08 | RF-PHY-03 |
| Fire-system mismatch † | Detection unsuited to high-airflow halls; suppression interfaces that shut down cooling; cause-and-effect matrix errors. | CG-04, CG-06 | RF-PHY-04 |
| Water ingress † | Roof, façade, flood and pipework routes into halls and electrical rooms. | CG-04, CG-09 | RF-PHY-05 |

## 31. POW — Electrical Power Infrastructure and Energy Continuity

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| Utility loss † | Duration distribution, repeated auto-reclose events and grid-operator obligations for large loads. | CG-05 | RF-POW-01 |
| Generator no-start † | Start reliability, fuel quality, starting batteries, controls and synchronisation; K-of-N failure combinations. | CG-05 | RF-POW-02 |
| Generator load-acceptance failure | Response to large AI load steps after transfer: frequency and voltage dip, governor and AVR stability, UPS input window. | CG-05 | RF-POW-02, RF-POW-06 |
| UPS loss † | Runtime with aged batteries, transfer to bypass, inverter overload, battery thermal runaway. | CG-05, CG-04 | RF-POW-03 |
| Protection miscoordination † | Upstream device clearing before downstream; settings not updated after load growth; arc-flash energy beyond study. | CG-05, CG-04 | RF-POW-04 |
| Rack and busway overload † | Rack power increases beyond busway, PDU or power-shelf rating; single-feed loading during maintenance. | CG-05 | RF-POW-05 |
| Power-quality interaction | Harmonics and resonance from rectifier loads; sag ride-through of rack power supplies. | CG-05 | RF-POW-01, RF-POW-06 |
| Electrical monitoring loss | EPMS loss of view or false indication during events; sequence-of-events time skew. | CG-07, CG-11 | RF-POW-07 |

## 32. THM — Cooling, Thermal and Fluid Infrastructure

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| Cooling capacity loss at sustained AI load † | Resilient capacity with one chiller or CDU unavailable at design ambient; restart time of chillers after power loss. | CG-06 | RF-THM-04 |
| CDU failure † | Pump, controller, valve and heat-exchanger failure modes; standby transfer; common firmware. | CG-06, CG-07 | RF-THM-02, RF-THM-03 |
| Thermal transient † | Time from loss of flow or heat rejection to accelerator thermal limits; ride-through versus restoration time. | CG-06 | RF-THM-01, RF-THM-02 |
| Liquid leak † | Leak at quick-disconnects, manifolds and hoses; detection, isolation, make-up behaviour, proximity to energised equipment. | CG-04, CG-06 | RF-THM-06 |
| Shared control failure † | One controller, network or sensor chain serving multiple cooling units. | CG-07, CG-09 | RF-THM-08 |
| Poor coolant quality † | Chemistry, inhibitor depletion, particulate and biological fouling in TCS and facility water. | CG-06 | RF-THM-07 |
| Air-side residual load | Heat from power supplies, memory and network equipment not captured by liquid; recirculation in mixed halls. | CG-06 | RF-THM-05 |

## 33. ENV — Environmental and Resource Performance

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| Ambient exceedance † | Wet-bulb and dry-bulb conditions beyond design under climate projection; derating of heat rejection. | CG-06 | RF-ENV-02, RF-THM-04 |
| Water scarcity † | Restrictions on abstraction or supply during drought or heatwave; storage autonomy. | CG-03, CG-06 | RF-ENV-02 |
| Air contamination † | Gaseous corrosion and particulate from external sources or construction; humidity and condensation risk around cold surfaces. | CG-08 | RF-ENV-01 |
| Refrigerant loss † | Leak from chillers or DX units; occupational exposure; environmental release. | CG-04 | RF-ENV-04 |
| Efficiency-resilience conflict † | Efficiency optimisation (raised setpoints, reduced redundancy running) that removes transient margin. | CG-06, CG-14 | RF-THM-08 |
| Metering and claim error † | Incorrect energy, water or carbon attribution leading to false reporting or wrong capacity decisions. | CG-11 | RF-ENV-03 |

## 34. CMP — AI Compute Infrastructure

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| Accelerator/node failure † | Failure rates at scale; effect on synchronous jobs; spare-node pool; drain time. | CG-08 | RF-CMP-01, RF-CMP-05 |
| Scale-up domain failure † | Loss of one element of a rack-scale or NVLink-class domain collapsing the domain; repair granularity. | CG-08, CG-09 | RF-CMP-02 |
| Firmware incompatibility † | Interactions between GPU, NIC, BMC, driver and switch firmware; rollback. | CG-08, CG-14 | RF-CMP-04 |
| Scheduler failure † | Control-plane loss; placement ignoring fault domains. | CG-08, CG-09 | RF-CMP-03 |
| Telemetry blindness † | Loss of GPU and node health telemetry, causing undetected degradation or spurious drains. | CG-08 | RF-CMP-05 |
| Thermal throttling † | Throttling as a consequence of THM paths and its effect on step time and job completion. | CG-06, CG-08 | RF-CMP-01 |
| Mass reboot † | Simultaneous reboot from power event, automation or firmware; restart storm on provisioning and storage. | CG-08, CG-10 | RF-CMP-06 |
| Golden-image corruption † | Defective or tampered image reaching the fleet; validation before use. | CG-08, CG-10 | RF-CMP-06 |
| Silent data corruption | Accelerators producing incorrect results without error indication; effect on training integrity and checkpoints. | CG-08 | RF-CMP-01 |

## 35. STO — AI Storage and Data Infrastructure

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| Metadata failure † | Metadata service loss or hotspot under many-small-file access; consistency after failover. | CG-08 | RF-STO-01, RF-STO-04 |
| Capacity exhaustion † | Checkpoint retention filling the tier; write failures and loss of recent checkpoints. | CG-08 | RF-STO-02 |
| Throughput collapse † | Read or write bandwidth below training or checkpoint demand; noisy neighbours. | CG-08 | RF-STO-01 |
| Checkpoint failure † | Incomplete, corrupt or unverified checkpoints; asynchronous drain not completed before failure. | CG-08, CG-10 | RF-STO-02 |
| Protection common-mode † | Replicas and backups sharing credentials, controllers or site. | CG-09, CG-10 | RF-STO-05 |
| Silent corruption † | Undetected data or metadata corruption propagating into checkpoints and replicas. | CG-08 | RF-STO-04 |
| Restore failure † | Restore throughput at full-cluster scale; restore of incompatible checkpoint formats. | CG-10 | RF-STO-03 |
| Data-transfer bottleneck † | Dataset staging and inter-site replication limited by WAN or gateway capacity. | CG-08 | RF-STO-01, RF-NET-03 |

## 36. NET — AI Network and Interconnect Architecture

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| Fabric partition † | Loss of spine or plane splitting the cluster; job behaviour under partial connectivity. | CG-08, CG-09 | RF-NET-01, RF-NET-02 |
| Congestion collapse † | Incast during collectives and checkpoints; PFC storms and deadlock; congestion-control tuning. | CG-08, CG-09 | RF-NET-01 |
| Scale-up link failure † | Link degradation inside scale-up domains; retraining and error rates. | CG-08 | RF-CMP-02 |
| Management network loss † | Loss of in-band and out-of-band management together; dependency on same switches or power. | CG-07, CG-10 | RF-NET-04 |
| Time-service failure † | Grandmaster or GNSS failure; clock step; effects on security, storage and evidence. | CG-08, CG-11 | RF-NET-05 |
| DNS/DHCP/IPAM failure † | Core services needed for provisioning, recovery and control planes. | CG-10 | RF-NET-05 |
| Configuration blast radius † | One change applied fleet-wide by controller or automation. | CG-09, CG-14 | RF-NET-02 |
| Optical/cabling defect † | Dirty connectors, marginal optics, miscabling; intermittent link flaps. | CG-08 | RF-NET-06 |

## 37. OPS — Building Operations and Service Management

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| Maintenance-induced outage † | Work on one path removing redundancy while the other path has a latent defect. | CG-05, CG-06, CG-14 | RF-OPS-02 |
| Procedure failure † | Procedures that are incorrect, unavailable or ambiguous in EMERGENCY. | CG-13 | RF-OPS-01 |
| Competence gap † | Staff not authorised or practised for rare operations (manual transfer, black start, CDU isolation). | CG-13 | RF-OPS-05 |
| Change failure † | Unassessed or incorrectly implemented change; temporary configuration left in place. | CG-14 | RF-OPS-03 |
| Alarm-response failure † | Alarm flood, poor prioritisation, delayed response. | CG-07 | RF-OPS-01 |
| Handover failure † | Loss of situational information at shift change during an evolving event. | CG-13 | RF-OPS-05 |
| Deferred maintenance | Backlog creating latent standby failures. | CG-05, CG-06 | RF-OPS-04 |

## 38. RES — Resilience, Continuity and Recovery

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| Containment failure | Effects crossing declared fault-domain boundaries. | CG-09 | RF-RES-01 |
| Failure to degrade gracefully | Load shedding and job prioritisation not executed or executed in wrong order. | CG-09, CG-10 | RF-RES-02 |
| Restoration sequence failure | Power, cooling, control plane, storage and compute restored in an order that causes secondary failure. | CG-10 | RF-RES-03 |
| Recovery reintroduces fault † | Restoring defective configuration or re-energising into an uncleared fault. | CG-10, CG-14 | RF-RES-04 |
| Alternate capacity unavailable | Second site or provider capacity not available or not compatible when invoked. | CG-10 | RF-RES-05 |
| Compound regional event † | Flood, fire, grid and telecom together; extended duration; staff and fuel access. | CG-03, CG-05, CG-10 | RF-RES-02, RF-RES-05 |

## 39. SUP — Supply Chain, OEM and Ecosystem Assurance

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| Defective authentic release | Signed firmware or software that is genuine but defective, deployed widely. | CG-08, CG-14 | RF-SUP-01 |
| Spares/obsolescence † (long-lead spare after rare failure) | Lead time of transformers, switchgear, CDUs, chillers and accelerators versus recovery tolerance. | CG-10 | RF-SUP-02 |
| Supplier support loss † (loss of remote OEM support) | OEM or integrator unavailable, insolvent or restricted; knowledge concentration. | CG-03, CG-10 | RF-SUP-03 |
| Counterfeit or modified hardware | Components with altered firmware or substandard materials. | CG-08 | RF-SUP-04 |

## 40. SEC — Digital, OT and Control-Plane Security

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| OT compromise via remote access | Vendor and integrator remote paths into BMS, EPMS, CDU and PLC networks. | CG-07, CG-15 | RF-SEC-01, RF-SEC-02 |
| Shared authentication service failure † | Identity provider or MFA outage blocking operators and break-glass. | CG-10, CG-15 | RF-SEC-01 |
| Automation over-reach | Automated or AI-enabled actions exceeding blast-radius limits. | CG-09, CG-15 | RF-SEC-03 |
| Protection logic tampering | Modification of protection, interlock or safety logic. | CG-04, CG-07 | RF-SEC-05 |
| Containment-induced outage | Security response (isolation of networks) cutting control or monitoring paths needed for safe operation. | CG-07 | RF-SEC-04 |

## 41. EVA — Evidence, Assessment and Assurance Management

| **Scenario family** | **Analysis focus** | **Primary gates** | **Functions** |
|---------------------|--------------------|-------------------|---------------|
| As-built divergence † | Drawings, registers and dependency maps diverging from installed reality. | CG-02, CG-11 | RF-EVA-02 |
| Commissioning omission † | Tests not performed for transients, maintenance states or integrated sequences. | CG-11 | RF-EVA-02 |
| Evidence loss or corruption | Telemetry and logs lost, unsynchronised or altered, preventing reconstruction. | CG-11 | RF-EVA-01 |
| UNKNOWN suppression | UNKNOWNs closed by assumption or omitted from reports. | CG-12 | RF-EVA-03 |

# Part XIV - Cross-domain scenario library (X01–X20)

The library contains twenty reference scenarios that cross at least three domains. They are reference patterns: each assessed Capability Instance shall instantiate the applicable scenarios against its own architecture, parameters and evidence, and shall not cite a library scenario as evidence. Durations, thresholds and capacities are capability-profile parameters; where an example value is given it is labelled illustrative.

**THF-REQ-041** For each in-scope Capability Instance, every library scenario shall be instantiated, screened out with rationale (for example "no BESS installed"), or recorded as deferred with an UNKNOWN Record.

**THF-REQ-042** An instantiated library scenario shall replace the reference path with the site's actual entities, dependency edges, parameters and evidence, and shall record where the site's path differs from the reference path.

Each scenario is presented as: initiating event; preconditions; operating states; propagation path (step, domain, operator); affected Required Functions; affected Service Outcomes; safeguards that should interrupt it; relevant MCF control families; relevant critical gates; evidence that would show the safeguards work; typical UNKNOWNs.

## X01 Utility voltage sag during a synchronous training load swing

**Initiating event.** A transmission-system fault produces a voltage sag at the point of connection that exceeds the UPS input tolerance, followed within seconds by a sustained utility interruption from protection operation upstream.

**Preconditions.** A large synchronous training job is running with periodic power swings between compute and communication or checkpoint phases (swing magnitude and period are capability-profile parameters). UPS modules operate in a high-efficiency mode with a transfer time to inverter. Generator load-acceptance capability was verified with resistive load banks in steps, not with dynamic load. The utility interconnection agreement may contain requirements on load fluctuation.

**Operating states.** NORMAL → EMERGENCY (on battery, generators starting) → DEGRADED (on generators) → RECOVERY (retransfer to utility) → NORMAL; FAILED for affected blocks if load acceptance fails.

**Propagation path.**

1. POW — Sag TRIGGERS UPS transfer from mains or high-efficiency mode to inverter; batteries carry the full IT load including the swing (EXTERNAL_EVENT).
2. POW — Utility interruption TRIGGERS generator start; UPS battery energy DELAYS consequence for the battery runtime at current state of health (WITHIN the runtime parameter).
3. CAP → POW — When generators close onto the bus and UPS rectifiers walk in, the training load swing CONTRIBUTES_TO repeated large load steps on the generators; synchronous phase alignment across the job AMPLIFIES the step (DEMAND_SURGE).
4. POW — Generator governor and AVR response produces frequency and voltage excursions; UPS rectifiers reject the generator source when frequency leaves their input window and return to battery, which CONTRIBUTES_TO further battery depletion (CONTROL_ACTION, AND with step 3).
5. POW — Repeated rejection AND reduced battery state of health lead to battery exhaustion on one or more UPS blocks before stable generator supply is accepted (SEQUENCE).
6. POW → CMP — Loss of output on those blocks PROPAGATES_TO the racks they serve; dual-corded racks whose second feed is on a surviving block ride through; single-path rack-scale systems drop.
7. CMP → STO — Node loss in any participant TRIGGERS failure of the whole synchronous job (CASCADE); training progress since the last durable checkpoint is lost.
8. THM — If CDU pumps or chilled-water pumps are on the affected blocks or are not UPS-backed, loss of flow PROPAGATES_TO surviving racks as a thermal transient (SHARED_RESOURCE).
9. RES — Restart of all affected jobs at once creates a restore demand on checkpoint storage (links to X04).

**Affected Required Functions.** RF-POW-01, RF-POW-02, RF-POW-03, RF-POW-06, RF-CAP-01, RF-THM-02, RF-CMP-01, RF-STO-03.

**Affected Service Outcomes.** Training job completion and tolerated loss of progress (performance, recoverability); cluster availability (availability); compute capacity during the generator period (capacity).

**Safeguards that should interrupt it.**

- Cause side: workload power smoothing (power capping, ramp-rate limiting or on-site energy buffering) that bounds swing magnitude and ramp rate to the plant's characterised acceptance (interrupts step 3).
- Escalation: generator sizing and governor/AVR tuning verified against the measured AI load profile; UPS rectifier walk-in and input-window settings coordinated with generator capability (interrupts step 4).
- Escalation: UPS battery runtime at end-of-life capacity sized for repeated retransfer attempts (DELAYS step 5).
- Consequence side: mechanical-cooling and CDU pumps on UPS-backed supply (interrupts step 8); scheduler-level checkpoint interval matched to tolerated loss (limits step 7).

**Relevant MCF control families.** CAP-04 Demand and growth modelling; CAP-05 Operating envelope; POW-02 Generation and fuel; POW-03 UPS and energy storage; POW-05 Power quality and transient response; THM-06 Thermal control, maintenance and recovery; STO-05 Checkpoint and recovery services.

**Relevant critical gates.** CG-05 Resilient electrical supply; CG-06 Thermal continuity; CG-10 Recovery readiness.

**Evidence that would show the safeguards work.**

- E3 high-resolution power-quality recordings of the actual training load profile at UPS output and site level (magnitude, ramp, frequency content).
- E4 integrated test of generator acceptance with a dynamic load profile representative of the AI load (programmable load bank or controlled workload), including UPS rectifier behaviour, witnessed (V6).
- E7 generator transient-response study against ISO 8528-5 performance class and the measured profile; UPS coordination study.
- E2 configuration extract of power-capping or ramp-limit settings on the fleet, reconciled to the approved value.
- E3 battery state-of-health measurements and runtime test results.

**Typical UNKNOWNs.** Generator behaviour under dynamic AI load not tested (U5; US4 on CG-05). Swing profile of the next model generation unknown (U1; US3 unless it changes the envelope, then US4). Utility fault-level and sag statistics not provided (U2; US3).

## X02 CDU pump-controller firmware fault causes loss of TCS flow

**Initiating event.** A CDU controller firmware release mishandles a failed differential-pressure sensor reading and commands both duty and standby pumps to a minimum or stopped state, or enters a watchdog reset loop.

**Preconditions.** The same firmware version was deployed to all CDUs of that model across the hall within a short window. Standby pump start depends on the same controller. No hardwired fail-safe keeps a pump running on controller fault. IT-side power capping on coolant-flow loss is not configured. OEM remote support is required to diagnose controller faults.

**Operating states.** NORMAL (or TRANSITION during rollout) → EMERGENCY → FAILED for affected racks → RECOVERY.

**Propagation path.**

1. SUP → THM — Defective release, deployed through the CDU management tool, is a LATENT condition in all CDUs (COMMON_CAUSE).
2. THM — Sensor fault TRIGGERS incorrect controller action; both pumps stop (M09 then M01 on RF-THM-02); because the standby depends on the same controller, redundancy is DEFEATED.
3. THM → CMP — Loss of TCS flow PROPAGATES_TO cold plates; low thermal inertia means accelerators reach thermal limits within the TCS ride-through time (a capability-profile parameter, illustratively tens of seconds).
4. CMP — Accelerators throttle and then hardware thermal protection shuts them down (M23 on RF-CMP-01).
5. CMP → STO — The synchronous job fails (CASCADE); progress since the last checkpoint is lost.
6. THM — Further CDUs with the same sensor condition fail the same way; failures CORRELATE_WITH the firmware release.
7. SUP → RES — Diagnosis waits for OEM remote support (DELAYS recovery); manual pump override may be the only immediate recovery.

**Affected Required Functions.** RF-THM-02, RF-THM-08, RF-THM-01, RF-CMP-01, RF-SUP-01, RF-SUP-03.

**Affected Service Outcomes.** Training throughput and completion; compute capacity of affected rows; potential equipment damage if thermal protection is slow or disabled.

**Safeguards that should interrupt it.**

- Cause side: staged firmware rollout with canary CDUs and defined soak period; pre-deployment test of sensor-fault handling (interrupts step 1).
- Escalation: independent standby pump control or hardwired fail-run on controller fault; pumps default to running at safe speed on loss of control (interrupts step 2).
- Escalation: coolant flow and pressure alarms independent of the CDU controller, feeding the BMS and the IT power-management system to cap power before thermal limits (DELAYS step 3).
- Consequence side: scheduler placement spreading jobs across CDU fault domains where feasible; checkpoint interval (limits step 5).
- Recovery: documented manual override procedure, practised; firmware rollback package held locally.

**Relevant MCF control families.** THM-03 Liquid cooling systems; THM-06 Thermal control, maintenance and recovery; SUP-04 Software, firmware and update supply; SUP-06 Remote support and third-party access; OPS-05 Change and configuration management; CMP-05 Compute health and observability.

**Relevant critical gates.** CG-06 Thermal continuity; CG-07 Critical control-system integrity; CG-09 Failure containment; CG-14 Change control.

**Evidence that would show the safeguards work.**

- E4 test record of sensor-fault injection on a non-production CDU with the deployed firmware, showing fail-run behaviour (V5).
- E2 firmware inventory per CDU showing version distribution and rollout waves.
- E4 measured TCS ride-through after pump trip at representative load (time from flow loss to accelerator throttling), V6 under controlled conditions.
- E3 alarm and event history showing flow-loss alarms reach operators and power-capping triggers.
- E1 change record with canary results and approval.

**Typical UNKNOWNs.** CDU controller failure behaviour on sensor fault not documented by OEM (U2 or U9; US4 on CG-06/CG-07). Whether standby pump control is independent (U10; US4). TCS ride-through at current density (U1; US4).

## X03 PFC storm in a RoCE fabric from a misconfigured switch

**Initiating event.** A switch configuration change maps lossless traffic class priorities inconsistently (for example a DSCP-to-priority mismatch or a buffer threshold error), or a faulty NIC continuously transmits priority flow control (PFC) pause frames.

**Preconditions.** The scale-out fabric uses RoCE with PFC for lossless transport. PFC watchdog (storm detection) is disabled or set with a long timer. Congestion control (ECN-based) is tuned for steady state, not for incast during collectives. Configuration templates are pushed by a fabric controller to many switches.

**Operating states.** NORMAL or TRANSITION (during change) → DEGRADED → FAILED for affected jobs → RECOVERY.

**Propagation path.**

1. NET — Misconfiguration or faulty NIC TRIGGERS persistent pause generation on one port (CONFIG_DRIFT or HUMAN_ACTION).
2. NET — Pause PROPAGATES_VIA inter-switch links hop by hop; head-of-line blocking spreads to unrelated flows sharing the priority; cyclic buffer dependencies can create PFC deadlock (SHARED_RESOURCE, AMPLIFIES).
3. NET → CMP — Collective operations (all-reduce, all-gather) stall cluster-wide because every rank waits for the slowest (CASCADE).
4. CMP — Collective timeouts TRIGGER job failures across many jobs, not only the job on the faulty port.
5. NET → STO — If storage traffic shares the fabric or priority, checkpoint writes stall (MASKS the last-good checkpoint state).
6. OPS — Telemetry shows link-level health as normal (links up), which MASKS the cause and DELAYS diagnosis.

**Affected Required Functions.** RF-NET-01, RF-NET-02, RF-NET-03, RF-CMP-03, RF-STO-02.

**Affected Service Outcomes.** Collective communication performance; training throughput; job completion across the cluster; checkpoint durability.

**Safeguards that should interrupt it.**

- Cause side: pre-deployment configuration validation of QoS and PFC consistency across the fabric; staged change with blast-radius limits (interrupts step 1).
- Escalation: PFC watchdog enabled with timers shorter than collective timeouts, disabling PFC or dropping on the offending queue (CONTAINS step 2).
- Escalation: congestion control (ECN marking thresholds, rate control) validated under incast; deadlock-free routing design.
- Consequence side: storage traffic on separate fabric or priority (interrupts step 5).
- Detection: pause-frame counters and queue telemetry with alerts (interrupts step 6).

**Relevant MCF control families.** NET-01 Scale-up and scale-out fabrics; NET-02 Performance and congestion control; NET-03 Storage and service networks; NET-06 Network control and observability; OPS-05 Change and configuration management.

**Relevant critical gates.** CG-08 Compute, storage and network functional integrity; CG-09 Failure containment; CG-14 Change control.

**Evidence that would show the safeguards work.**

- E2 configuration extract showing PFC watchdog enabled and QoS mapping consistent on all switches, reconciled to the template.
- E4 controlled pause-injection test in a test fabric or isolated partition with the production software version, showing watchdog containment time (V5/V6).
- E3 fabric telemetry history of pause counters and ECN marks during large collectives.
- E1 change records showing staged rollout and validation gates.

**Typical UNKNOWNs.** Watchdog behaviour on the deployed switch software (U1; US4 on CG-09). Whether storage and compute share a lossless priority (U4 if documents disagree; US3). Deadlock freedom of the routing scheme (U9; US4).

## X04 Checkpoint storage saturation extends recovery beyond tolerance

**Initiating event.** A facility event (for example X01) terminates many training jobs at once; operators and schedulers restart all of them simultaneously.

**Preconditions.** Checkpoint tier sized for steady-state write bandwidth, not for concurrent full-cluster restore. Checkpoint retention policy leaves little free capacity. Metadata service is a single scaling domain. Restart admission is not rate-limited.

**Operating states.** FAILED → RECOVERY (extended) → DEGRADED → NORMAL.

**Propagation path.**

1. RES → CMP — Simultaneous restart TRIGGERS a read storm against the checkpoint tier (DEMAND_SURGE).
2. STO — Read demand exceeds tier throughput; metadata operations from many ranks opening shards create a metadata hotspot (M15 on RF-STO-03) which AMPLIFIES latency.
3. STO — Before the event, retention had filled the tier so recent checkpoint writes failed silently or were truncated; the last verified checkpoint is older than expected (LATENT, CONTRIBUTES_TO progress loss).
4. NET — Storage fabric congestion from the storm PROPAGATES_TO other tenants and to provisioning traffic (SHARED_RESOURCE).
5. STO → CAP — Restore time across the cluster exceeds the recovery tolerance; accelerators sit idle (DELAYS recovery).
6. CMP — Timeouts during restore cause repeated restart attempts that AMPLIFY the storm (positive feedback).

**Affected Required Functions.** RF-STO-02, RF-STO-03, RF-STO-01, RF-RES-04, RF-NET-03, RF-CMP-03.

**Affected Service Outcomes.** Recovery time objective for training; tolerated loss of progress; compute capacity utilisation during recovery.

**Safeguards that should interrupt it.**

- Cause side: restart admission control in the scheduler (staggered, priority-ordered restore) (interrupts step 1).
- Escalation: checkpoint tier and metadata service sized and tested for concurrent restore of the declared job population; tiered checkpointing using node-local storage with asynchronous drain (interrupts step 2).
- Escalation: capacity headroom alarms and retention enforcement; checkpoint completion verification before the previous checkpoint is released (interrupts step 3).
- Consequence side: QoS isolation of storage traffic (CONTAINS step 4); exponential back-off on restart retries (interrupts step 6).

**Relevant MCF control families.** STO-02 Performance and capacity; STO-05 Checkpoint and recovery services; STO-06 Storage monitoring and lifecycle; CMP-03 Capacity, scheduling and utilisation; RES-04 Recovery planning; RES-05 Testing and exercising.

**Relevant critical gates.** CG-08 Compute, storage and network functional integrity; CG-10 Recovery readiness.

**Evidence that would show the safeguards work.**

- E4 restore test at the declared concurrent scale (or a validated scaled test with T15 extrapolation) measuring time to all jobs running (V6).
- E3 checkpoint write and verification logs showing completion and integrity over a representative period.
- E2 scheduler configuration of restart admission limits.
- E3 capacity forecasting reports with headroom against retention policy.

**Typical UNKNOWNs.** Restore throughput at full scale (U5; US4 on CG-10). Whether the latest checkpoints are complete (U7; US4). Metadata scaling limit (U1; US3).

## X05 BMS remote-vendor credential compromise alters chilled-water setpoints

**Initiating event.** An attacker uses a compromised BMS integrator remote-support credential (shared account, persistent VPN, no MFA) to access the BMS supervisory server.

**Preconditions.** Vendor remote access is always on. BMS permits setpoint and alarm-limit changes without second approval. Controllers accept setpoints from the supervisory layer without hard limits. Independent temperature monitoring of TCS and facility water does not exist outside the BMS.

**Operating states.** NORMAL → DEGRADED (slow-burn) → EMERGENCY → RECOVERY; analysis shall also consider initiation during MAINTENANCE.

**Propagation path.**

1. SUP → SEC — Compromised vendor credential BYPASSES perimeter controls through the vendor conduit (HUMAN_ACTION by adversary).
2. SEC → THM — Attacker raises chilled-water supply setpoint and widens alarm limits; alarm suppression MASKS the change (M09, M19).
3. THM — Facility water supply temperature rises gradually; CDU approach temperature consumes margin (DEGRADATION driven by adversary).
4. THM → CMP — TCS supply temperature rises; accelerators throttle (M07 on RF-CMP-01); throughput degrades without obvious alarm.
5. SEC → THM — Attacker optionally disables chiller staging or commands CDU valve closure, which ESCALATES to loss of heat rejection.
6. CMP — Thermal shutdown of accelerators; jobs fail; possible equipment stress.
7. EVA — BMS audit logs altered, causing evidence and attribution loss.

**Affected Required Functions.** RF-SEC-01, RF-SEC-02, RF-SEC-05, RF-THM-08, RF-THM-04, RF-THM-03, RF-CMP-01, RF-EVA-01.

**Affected Service Outcomes.** Training throughput; availability; isolation and security outcomes; evidence and observability outcomes.

**Safeguards that should interrupt it.**

- Cause side: just-in-time vendor access with MFA, approval per session and session recording (interrupts step 1).
- Escalation: setpoint hard limits enforced in field controllers, not only in the supervisory layer; two-person approval for setpoint and alarm-limit changes (interrupts step 2).
- Detection: independent temperature and flow telemetry from IT-side sensors (accelerator inlet coolant temperature) correlated with BMS values; configuration change detection on BMS (interrupts steps 2–4).
- Consequence side: IT power capping on coolant temperature (DELAYS step 6).
- Evidence: write-once off-box logging of BMS changes (interrupts step 7).

**Relevant MCF control families.** SUP-06 Remote support and third-party access; SEC-01 Identity and privileged access; SEC-02 Control-plane protection; SEC-03 Network security and segmentation; SEC-05 Detection and response; THM-06 Thermal control, maintenance and recovery; EVA-02 Evidence provenance and quality.

**Relevant critical gates.** CG-15 Integrated digital authority over infrastructure; CG-07 Critical control-system integrity; CG-06 Thermal continuity.

**Evidence that would show the safeguards work.**

- E2 remote-access configuration showing JIT activation, MFA and session recording; E3 sample of session records reconciled to work orders.
- E4 test that a setpoint outside hard limits is rejected by the field controller (V5, non-production or authorised window).
- E3 correlation between IT-side coolant telemetry and BMS readings over a representative period.
- E5 independent OT security assessment against IEC 62443-3-2 zones and conduits.

**Typical UNKNOWNs.** Whether vendor accounts are unique and revoked on staff change (U2; US4 on CG-15). Whether controllers enforce limits (U1; US4 on CG-07). Integrity of BMS logs (U7; US2–US3).

## X06 Lithium-ion BESS or UPS battery thermal runaway

**Initiating event.** An internal short circuit in a lithium-ion cell of a UPS battery cabinet or BESS module initiates thermal runaway.

**Preconditions.** Battery installed in a room adjacent to electrical rooms or data hall. Off-gas detection may not be fitted; battery management system (BMS-battery) alarms are routed to the UPS, not to the fire system. Fire-test evidence for propagation (for example UL 9540A test reports) may not match the installed configuration. Emergency response plan does not address re-ignition.

**Operating states.** NORMAL → EMERGENCY → SHUTDOWN (battery string and possibly UPS) → DEGRADED (UPS without battery) → RECOVERY (long, with replacement).

**Propagation path.**

1. POW — Cell runaway releases flammable and toxic off-gas before visible fire (M25 on RF-POW-03).
2. POW → PHY — Off-gas accumulates; without detection and ventilation the room atmosphere can reach deflagration conditions (ESCALATION; CG-04).
3. POW — Heat PROPAGATES_TO adjacent cells and modules unless module design and spacing CONTAIN it.
4. PHY — Fire detection and suppression act; suppression may not stop cell-level runaway (re-ignition risk); smoke PROPAGATES_VIA shared ventilation to adjacent spaces.
5. PHY → POW — Emergency response requires de-energising the UPS and its battery; the UPS block loses ride-through, so the load is either transferred to bypass (exposed to utility disturbances) or shut down (CONTROL_ACTION or HUMAN_ACTION).
6. POW → CMP — Racks on that block operate without ride-through or are lost; synchronous jobs fail if any participant is affected.
7. ENV — Electrolyte, combustion products and suppressant residue contaminate equipment; environmental release reporting.
8. SUP → RES — Replacement battery modules and cabinet repair have long lead times (DELAYS recovery to NORMAL).

**Affected Required Functions.** RF-POW-03, RF-PHY-04, RF-ENV-04, RF-OPS-01, RF-RES-03, RF-SUP-02.

**Affected Service Outcomes.** Safety outcomes (primary); availability and capacity of the affected block; recovery outcomes; environmental compliance.

**Safeguards that should interrupt it.**

- Cause side: cell and module condition monitoring with thermal and voltage anomaly detection; manufacturer quality and approved sourcing (interrupts step 1).
- Escalation: off-gas detection triggering ventilation and alarm; explosion control (venting or exhaust) per the installation's hazard analysis (interrupts step 2).
- Escalation: module-level propagation resistance evidenced by large-scale fire testing of the installed configuration; separation distances and fire-rated enclosure (CONTAINS step 3).
- Consequence side: fire strategy and emergency response plan specific to lithium-ion, including fire-service liaison, re-ignition watch and safe de-energisation (CONTAINS steps 4–5).
- Consequence side: electrical topology where loss of one battery string does not remove ride-through from the whole load (limits step 6).

**Relevant MCF control families.** POW-03 UPS and energy storage; PHY-06 Fire, life safety and emergency interfaces; ENV-05 Hazardous materials and waste; OPS-02 Procedure and work control; RES-06 Crisis and adaptive response; SUP-05 Spares, logistics and obsolescence.

**Relevant critical gates.** CG-04 Life safety and hazardous energy; CG-05 Resilient electrical supply; CG-10 Recovery readiness.

**Evidence that would show the safeguards work.**

- E5 large-scale fire test report for the installed battery product and configuration, reviewed by a competent fire engineer against the installation.
- E7 hazard mitigation analysis and explosion-control design calculation for the room.
- E4 functional test of off-gas detection and ventilation interlocks (V5).
- E1/E4 emergency response plan and exercise record with the fire service (V4).
- E3 battery management system telemetry and alarm routing configuration (E2).

**Typical UNKNOWNs.** Applicability of fire-test results to the installed configuration (U9; US4 on CG-04). Whether off-gas alarms reach the fire system (U10; US4). Replacement lead time (U2; US3 on CG-10).

## X07 Coolant leak at a rack manifold or quick-disconnect

**Initiating event.** A quick-disconnect seal fails or a rack manifold cracks, often during a pressure transient (pump start, valve closure) or after a maintenance reconnection.

**Preconditions.** Rack manifold sits above power shelves or busbar connections. Leak detection is a single sensing cable at floor level. The CDU automatically makes up coolant from a reservoir when pressure falls. Per-rack isolation valves are manual.

**Operating states.** NORMAL or MAINTENANCE → EMERGENCY → DEGRADED (rack isolated) → RECOVERY.

**Propagation path.**

1. THM — Pressure transient TRIGGERS seal failure at a degraded quick-disconnect (DEGRADATION, CONTRIBUTES_TO); coolant escapes (M25 on RF-THM-06).
2. THM — Automatic make-up maintains loop pressure, which MASKS the leak at the CDU and sustains the leak volume.
3. THM → POW — Coolant reaches power shelves or busbar connections; ESCALATION to electrical fault, arc or tracking (CG-04).
4. POW — Rack power protection trips; if protection is slow or the fault involves the busway, upstream protection clears a larger section (M05 if miscoordinated).
5. POW → CMP — Rack and possibly row loss; synchronous jobs fail.
6. PHY — Coolant spreads under or between racks to adjacent equipment; floor-level detection alarms only after pooling (DELAYS detection).
7. OPS → RES — Isolation, drying, inspection and requalification of affected equipment before re-energisation (RECOVERY); risk that re-energising wet equipment REINTRODUCES the fault.

**Affected Required Functions.** RF-THM-06, RF-THM-02, RF-POW-04, RF-POW-05, RF-CMP-01, RF-OPS-02.

**Affected Service Outcomes.** Safety (electrical hazard); availability and capacity of affected racks; physical damage; recovery.

**Safeguards that should interrupt it.**

- Cause side: quick-disconnect inspection and replacement interval; pressure-test after any reconnection; soft-start and controlled valve timing to limit transients (interrupts step 1).
- Detection: point leak sensors at manifold connections and drip trays; CDU make-up volume and rate alarm and limit (interrupts step 2).
- Escalation: physical separation or shielding of fluid connections from energised conductors; automatic per-rack isolation on leak detection (interrupts step 3).
- Consequence side: selective protection coordination at rack and busway level (CONTAINS step 4).
- Recovery: re-energisation procedure with insulation testing and competent sign-off (interrupts step 7).

**Relevant MCF control families.** THM-03 Liquid cooling systems; THM-05 Fluid quality and leak management; POW-04 Distribution and protection; OPS-02 Procedure and work control; PHY-03 Physical zoning and segregation.

**Relevant critical gates.** CG-04 Life safety and hazardous energy; CG-06 Thermal continuity; CG-09 Failure containment.

**Evidence that would show the safeguards work.**

- E4 leak-detection functional test with a defined fluid, volume and location at manifold level, recording time to alarm and isolation (V5).
- E2 CDU configuration showing make-up limit and alarm settings.
- E4 commissioning pressure-test records per rack and after maintenance reconnections.
- E7 protection coordination study covering rack power shelves and busway taps.
- E1 re-energisation procedure; E6 interview evidence that staff know it.

**Typical UNKNOWNs.** Behaviour of make-up logic during leak (U1; US4 on CG-06). Leak detection coverage at manifold height (U5; US4 on CG-04). QD condition across fleet (U5; US3).

## X08 Facility water contamination fouls heat exchangers and cold plates

**Initiating event.** A water-treatment failure in an open cooling-tower circuit (dosing pump fault, missed chemistry checks) or construction debris from an expansion tie-in enters the facility water loop.

**Preconditions.** Facility water passes through CDU heat exchangers with tight approach-temperature design. Side-stream filtration is undersized or bypassed. Chemistry monitoring is manual and periodic. Flushing and cleanliness requirements for tie-ins are not enforced. TCS fill water and inhibitor are managed by a different team.

**Operating states.** NORMAL → DEGRADED (slow-burn) → EMERGENCY if approach collapses → MAINTENANCE (cleaning) → RECOVERY.

**Propagation path.**

1. ENV/THM — Chemistry excursion or debris CAUSES fouling and biological growth in the facility loop (DEGRADATION; M07 on RF-THM-07).
2. THM — Fouling of CDU heat-exchanger plates increases approach temperature (M07 on RF-THM-03) across many CDUs fed by the same loop (COMMON_CAUSE).
3. THM → CMP — TCS supply temperature rises at a given load; accelerators throttle at peak load (M07 on RF-CMP-01).
4. THM — If TCS is contaminated (HX breach, improper fill or material incompatibility), cold-plate microchannels foul or corrode, which ESCALATES to localised overheating and possible leaks.
5. PHY/ENV — Biological growth in cooling towers creates a water-borne pathogen hazard (ESCALATION to CG-04).
6. OPS — Cleaning requires taking CDUs out of service, which reduces resilient capacity (MAINTENANCE state).

**Affected Required Functions.** RF-THM-07, RF-THM-03, RF-THM-04, RF-ENV-02, RF-CMP-01, RF-OPS-04.

**Affected Service Outcomes.** Training throughput at peak load; resilient cooling capacity; safety; equipment life.

**Safeguards that should interrupt it.**

- Cause side: water-treatment programme with continuous chemistry monitoring and alarms; filtration and strainers; flushing and cleanliness acceptance for tie-ins (interrupts step 1).
- Detection: approach-temperature trending per CDU heat exchanger with alarm on drift (interrupts step 2).
- Escalation: TCS chemistry and material compatibility management with periodic sampling (interrupts step 4).
- Escalation: cooling-tower pathogen risk management per applicable regulation (interrupts step 5).
- Consequence side: N+1 CDU capacity allowing cleaning without loss of outcome (limits step 6).

**Relevant MCF control families.** THM-05 Fluid quality and leak management; THM-04 Heat rejection and water systems; ENV-03 Water performance; OPS-03 Maintenance and reliability; THM-01 Thermal architecture and capacity.

**Relevant critical gates.** CG-06 Thermal continuity; CG-04 Life safety and hazardous energy.

**Evidence that would show the safeguards work.**

- E3 chemistry monitoring records and laboratory results over a representative period.
- E3 approach-temperature trend data per CDU with alarm configuration (E2).
- E4 tie-in flushing and cleanliness acceptance records.
- E5 independent water-treatment audit.

**Typical UNKNOWNs.** TCS chemistry history (U1; US3). Material compatibility of mixed-vendor cold plates and manifolds (U9; US3). Fouling rate (U8; US2).

## X09 Shared fibre route cut defeats diverse connectivity

**Initiating event.** Third-party excavation near the site cuts a duct carrying fibre for two carriers that were contracted as diverse.

**Preconditions.** Diversity was accepted on carrier assurance without route evidence. Both carriers' circuits enter through different building entries but share a duct or bridge crossing outside the boundary. Inference ingress, inter-site checkpoint replication, remote vendor access and cloud identity services all depend on these circuits. Out-of-band access has no independent path.

**Operating states.** NORMAL → DEGRADED or FAILED (external connectivity) → RECOVERY (carrier repair).

**Propagation path.**

1. PHY/DEP — External excavation TRIGGERS a cut of the shared duct (EXTERNAL_EVENT; COMMON_CAUSE through the shared route).
2. NET — Both carriers' circuits fail; diversity DEFEATED (M01 on RF-NET-03 frontend and WAN).
3. NET → CAP — Inference ingress lost; inference Service Outcome breached immediately.
4. NET → STO — Inter-site checkpoint replication stops; recovery-point exposure grows (DELAYS replication).
5. NET → SEC — Cloud-hosted identity or MFA unreachable; operators cannot authenticate to some systems (links to X15).
6. NET → SUP — Remote vendor support unavailable during any concurrent incident (SHARED_RESOURCE).
7. EVA — Remote monitoring of the site lost; site-local evidence must be retained.

**Affected Required Functions.** RF-NET-03, RF-NET-04, RF-DEP-02, RF-STO-05, RF-SEC-01, RF-SUP-03.

**Affected Service Outcomes.** Inference availability and latency; recovery-point outcome for training; observability.

**Safeguards that should interrupt it.**

- Cause side: route-level diversity verified with carrier route evidence to a defined separation, including outside-plant segments (interrupts step 2).
- Escalation: third diverse path using different medium (for example a different route or wireless backup) for critical control, OOB and identity traffic (CONTAINS steps 5–6).
- Consequence side: inference failover to another site with capacity reserved (limits step 3); local identity fallback (limits step 5).

**Relevant MCF control families.** DEP-02 Shared and common-mode dependencies; DEP-03 External providers and utilities; NET-05 Physical connectivity and optics; NET-04 Management and out-of-band networks; RES-03 Continuity planning.

**Relevant critical gates.** CG-03 Critical dependency visibility; CG-09 Failure containment; CG-10 Recovery readiness.

**Evidence that would show the safeguards work.**

- E5 carrier route documentation with separation evidence, reviewed against physical survey.
- E4 failover test of inference ingress to an alternate site (V6).
- E4 test that OOB and identity fallback work with all carrier circuits disabled (V5/V6, in an authorised window).

**Typical UNKNOWNs.** Carrier route geometry (U2; US4 on CG-03 when diversity is credited). Dependence of identity on WAN (U10; US5 if it affects CG-10 and CG-15).

## X10 Firmware supply-chain defect across the GPU fleet

**Initiating event.** An authentic, correctly signed accelerator firmware or driver release contains a defect that, under a specific power or clock state, produces silent data corruption or uncorrectable memory errors.

**Preconditions.** Release passes signature validation and functional smoke tests. Rollout policy allows fleet-wide deployment within a short window. Silent data corruption screening is not part of acceptance. Checkpoint retention keeps only a few recent checkpoints. Fleet has no firmware diversity.

**Operating states.** TRANSITION (rollout) → NORMAL (latent) → DEGRADED (detected) → RECOVERY (rollback and re-training from a known-good checkpoint).

**Propagation path.**

1. SUP → CMP — Defective release is deployed to the fleet; signature validation passes, so authenticity checks do not interrupt it (LATENT, COMMON_CAUSE).
2. CMP — Under the triggering power state, some accelerators compute incorrect results without error indication (M16 / M09 on RF-CMP-01).
3. CMP → STO — Corrupted gradients are incorporated into model state; checkpoints written after onset are corrupted (PROPAGATES_TO RF-STO-04).
4. CAP — Training loss anomalies appear later; detection lag means older good checkpoints may already have been rotated out (DELAYS detection; ESCALATION of progress loss).
5. CMP — Uncorrectable errors on other devices cause node failures and job restarts that CORRELATE_WITH the release.
6. RES — Recovery requires rollback of firmware across the fleet and re-training from the last verified checkpoint; rollback package availability and compatibility determine duration.

**Affected Required Functions.** RF-SUP-01, RF-CMP-04, RF-CMP-01, RF-CMP-05, RF-STO-04, RF-STO-05, RF-RES-04.

**Affected Service Outcomes.** Data and model integrity; training completion; compute capacity during rollback.

**Safeguards that should interrupt it.**

- Cause side: staged rollout with canary population and soak period including SDC screening tests and burn-in under representative power states (interrupts step 1).
- Detection: periodic SDC detection tests and cross-replica result comparison; training-health monitoring (loss and gradient anomalies) with alerts (interrupts steps 2–4).
- Consequence side: retention of verified checkpoints spanning more than the expected detection lag; checkpoint integrity validation (limits step 4).
- Recovery: tested rollback package and procedure (interrupts step 6).

**Relevant MCF control families.** SUP-04 Software, firmware and update supply; CMP-04 Firmware, driver and compatibility; CMP-05 Compute health and observability; STO-03 Integrity and consistency; STO-05 Checkpoint and recovery services; OPS-05 Change and configuration management.

**Relevant critical gates.** CG-08 Compute, storage and network functional integrity; CG-14 Change control; CG-10 Recovery readiness.

**Evidence that would show the safeguards work.**

- E1/E4 rollout records showing canary waves, soak duration and SDC test results.
- E2 fleet firmware inventory by version and wave.
- E4 rollback test on a representative partition (V5).
- E3 training-health monitoring alerts and responses.

**Typical UNKNOWNs.** OEM defect disclosure (U2/U6; US3). SDC test coverage of triggering conditions (U8; US4 on CG-08). Detection lag (U1; US3).

## X11 Concurrent maintenance exposes a hidden shared electrical dependency

**Initiating event.** The A-side UPS and distribution path is taken out of service for planned maintenance.

**Preconditions.** Racks are designed dual-corded A/B, but an as-built divergence exists: some rack power shelves have both inputs connected to A-side PDUs, or rack-scale systems with single-input power shelves were added on the A side. The B path's capacity was checked against design load, not measured peak AI load. The method statement does not require verification of cord-to-feed mapping or B-side headroom immediately before isolation.

**Operating states.** NORMAL → MAINTENANCE → FAILED (affected racks) → RECOVERY.

**Propagation path.**

1. OPS — Planned isolation of the A path (HUMAN_ACTION, ENABLING).
2. POW — Racks whose both cords are on A lose power (M29 misallocation, LATENT; CAUSES M01 on RF-POW-05 for those racks).
3. POW — B path carries all remaining load; at peak training load B-side PDUs or busway taps exceed rating and trip (M14), which CASCADES to further rack loss.
4. POW → CMP — Synchronous jobs on affected racks fail; job loss extends to all jobs with any participant on those racks.
5. CMP → THM — Sudden load drop and then restart surge cause cooling-plant control transients (AMPLIFIES).
6. OPS → RES — Maintenance must be aborted and A path restored under time pressure, raising the risk of switching error (links to X16).

**Affected Required Functions.** RF-POW-05, RF-POW-04, RF-DEP-01, RF-OPS-02, RF-OPS-03, RF-EVA-02, RF-CMP-01.

**Affected Service Outcomes.** Availability and capacity during maintenance (concurrent-maintainability claim); training completion.

**Safeguards that should interrupt it.**

- Cause side: periodic as-built audit of cord-to-feed mapping reconciled in EPMS, and per-outlet metering that detects single-path loading (interrupts step 2).
- Cause side: pre-isolation readiness check in the method statement: measured B-side load and headroom at expected peak, list of single-path racks, workload drain or power capping applied (interrupts steps 2–3).
- Escalation: power capping on B-side overload risk (interrupts step 3).
- Consequence side: scheduler drain of single-path racks before maintenance (limits step 4).

**Relevant MCF control families.** OPS-02 Procedure and work control; OPS-05 Change and configuration management; POW-04 Distribution and protection; POW-06 Electrical monitoring, maintenance and recovery; DEP-01 Dependency discovery; EVA-02 Evidence provenance and quality.

**Relevant critical gates.** CG-02 Boundary and architecture integrity; CG-05 Resilient electrical supply; CG-14 Change control.

**Evidence that would show the safeguards work.**

- E2 EPMS per-outlet load and feed mapping export reconciled to the rack power register (RECONCILIATION).
- E1 method statement with readiness checks; E3 record of the checks performed for the last maintenance events.
- E4 concurrent-maintenance test with representative load (V6).

**Typical UNKNOWNs.** Cord-to-feed mapping for racks added since commissioning (U3; US5 where it bears on both CG-02 and CG-05, otherwise US4 on CG-05). Measured peak B-side load (U1; US4).

## X12 Heatwave combined with water restriction on evaporative heat rejection

**Initiating event.** A prolonged heatwave raises ambient wet-bulb temperature above the heat-rejection design condition while the water utility imposes abstraction or supply restrictions.

**Preconditions.** Evaporative cooling towers or adiabatic coolers provide most heat rejection. Design ambient was based on historical data without climate projection. On-site water storage autonomy is limited. The grid operator issues demand-response requests in the same period.

**Operating states.** NORMAL → DEGRADED (derated) → EMERGENCY (load shedding) → RECOVERY.

**Propagation path.**

1. ENV — Ambient exceedance (EXTERNAL_EVENT) CAUSES reduced heat-rejection capacity (M07 on RF-THM-04).
2. ENV/DEP — Water restriction CONTRIBUTES_TO further capacity loss as evaporative duty cannot be sustained (AND with step 1; M14 on RF-ENV-02).
3. THM — Chillers operate at high condensing pressure; some trip on high-pressure protection (M24 if spurious, M01 if genuine), consuming redundancy.
4. THM → CMP — Facility water and TCS supply temperatures rise; accelerators throttle; at the limit, load must be shed.
5. POW/DEP — Grid demand-response obligations and higher cooling power CONFLICT_WITH sustaining full IT load.
6. RES — Load shedding by priority (graceful degradation) must be executed; if not pre-planned, ad hoc decisions DELAY response.

**Affected Required Functions.** RF-THM-04, RF-ENV-02, RF-THM-03, RF-CMP-01, RF-RES-02, RF-CAP-02.

**Affected Service Outcomes.** Compute capacity and throughput; availability of lower-priority workloads; environmental compliance (water).

**Safeguards that should interrupt it.**

- Cause side: heat-rejection design and derating at projected extreme ambient; hybrid dry/wet operation (interrupts step 1).
- Escalation: water storage autonomy sized for the restriction scenario; alternative supply agreement (interrupts step 2).
- Consequence side: pre-approved load-shedding priorities and automated power capping by workload class (limits steps 4–6).

**Relevant MCF control families.** ENV-06 Climate adaptation and resource continuity; ENV-03 Water performance; THM-01 Thermal architecture and capacity; THM-04 Heat rejection and water systems; RES-01 Resilience strategy; CAP-05 Operating envelope.

**Relevant critical gates.** CG-06 Thermal continuity; CG-03 Critical dependency visibility; CG-01 Capability and outcome definition.

**Evidence that would show the safeguards work.**

- E7 heat-rejection capacity analysis at projected extreme ambient, with derating curves from equipment data.
- E3 performance during the hottest observed periods (V2).
- E1 water-supply agreement and storage autonomy calculation.
- E4 exercise of load-shedding priorities (V4/V6).

**Typical UNKNOWNs.** Extreme-ambient design basis under climate projection (U9; US3–US4). Utility restriction policy (U2; US3).

## X13 Time-source failure causes divergence across control planes

**Initiating event.** GNSS signal loss or interference at the grandmaster antennas, or a misconfigured clock wins best-master selection and steps time.

**Preconditions.** PTP and NTP hierarchy depends on one GNSS source type; holdover oscillators are limited; clients permit large time steps; the same time hierarchy serves the AI fabric, storage, identity, BMS/EPMS and logging.

**Operating states.** NORMAL → DEGRADED (holdover or wrong time) → RECOVERY.

**Propagation path.**

1. NET — GNSS loss TRIGGERS holdover; drift accumulates; or a rogue clock is selected (M09 on RF-NET-05).
2. NET → SEC — Clock offset beyond tolerance causes certificate and token validation failures; operators and services fail to authenticate (PROPAGATES_TO RF-SEC-01).
3. NET → STO — Distributed storage leases and consensus behave incorrectly; possible metadata inconsistency (M27).
4. NET → CMP — Scheduler timeouts and job failures from skewed heartbeats.
5. NET → EVA — Logs and EPMS sequence-of-events records lose correlation, causing evidence and attribution loss for any concurrent event (MASKS causal reconstruction).

**Affected Required Functions.** RF-NET-05, RF-SEC-01, RF-STO-04, RF-CMP-03, RF-POW-07, RF-EVA-01.

**Affected Service Outcomes.** Availability; data integrity; observability and evidence.

**Safeguards that should interrupt it.**

- Cause side: multiple diverse time sources with authenticated distribution and grandmaster priority settings restricting which clocks can become master (interrupts step 1).
- Escalation: holdover oscillator quality sized for the expected outage; client policy to slew rather than step beyond threshold; offset monitoring at every tier with alarms (interrupts steps 2–4).
- Evidence: logs carry source and synchronisation status; EPMS has local high-accuracy time-stamping (limits step 5).

**Relevant MCF control families.** NET-06 Network control and observability; SEC-01 Identity and privileged access; STO-03 Integrity and consistency; EVA-02 Evidence provenance and quality.

**Relevant critical gates.** CG-08 Compute, storage and network functional integrity; CG-11 Evidence sufficiency; CG-15 Integrated digital authority over infrastructure.

**Evidence that would show the safeguards work.**

- E2 time-hierarchy configuration including master priorities and client step policy.
- E4 GNSS-loss test in holdover with measured drift over the declared holdover period (V5).
- E3 offset monitoring history.

**Typical UNKNOWNs.** Which systems depend on which time source (U10; US4–US5 depending on gates affected). Holdover performance (U1; US3).

## X14 Recovery reintroduces a corrupt configuration or image

**Initiating event.** After an incident caused by a defective configuration change (for example X03) or a defective image, operators restore from the most recent backup.

**Preconditions.** Backups are taken on schedule after every change, so the latest backup contains the defect. There is no "known good" tag. The golden image repository has no validation gate. BMS controller backups contain outdated logic or setpoints.

**Operating states.** FAILED → RECOVERY → FAILED (again) → RECOVERY.

**Propagation path.**

1. RES — Recovery selects the latest backup (HUMAN_ACTION under time pressure).
2. RES → NET/CMP/THM — Restore REINTRODUCES the defective configuration or image (RECOVERY_INDUCED).
3. NET/CMP — Original failure recurs; or an older BMS backup removes interlocks added after an earlier incident (M16 on RF-SEC-05 or RF-THM-08).
4. RES — Repeated failure extends recovery time beyond tolerance and erodes confidence in recovery (DELAYS).

**Affected Required Functions.** RF-RES-04, RF-RES-03, RF-OPS-03, RF-CMP-06, RF-NET-02, RF-THM-08.

**Affected Service Outcomes.** Recovery time; availability; integrity of configuration.

**Safeguards that should interrupt it.**

- Cause side: versioned configuration with known-good tagging and change correlation; restore procedure selects the last validated baseline, not the latest backup (interrupts step 1).
- Escalation: validation of restored configuration or image in a staging environment or canary before fleet application (interrupts step 2).
- Escalation: BMS and controller backups version-controlled and reconciled to current approved logic (interrupts step 3).

**Relevant MCF control families.** RES-04 Recovery planning; OPS-05 Change and configuration management; CMP-06 Compute lifecycle and recovery; NET-06 Network control and observability; THM-06 Thermal control, maintenance and recovery.

**Relevant critical gates.** CG-10 Recovery readiness; CG-14 Change control; CG-07 Critical control-system integrity.

**Evidence that would show the safeguards work.**

- E2 configuration repository showing tagged known-good baselines and correlation to changes.
- E4 restore exercise selecting a known-good baseline and validating it (V5/V6).
- E1 recovery procedure with validation steps.

**Typical UNKNOWNs.** Whether controller backups match the current approved logic (U3; US4 on CG-07). Whether known-good baselines exist for all device classes (U5; US3).

## X15 Shared identity service failure blocks operators and break-glass access during an incident

**Initiating event.** The central identity provider or MFA service becomes unavailable (for example through a power event in the hall hosting it, a WAN loss as in X09, or a certificate expiry).

**Preconditions.** BMS, EPMS, cluster managers, jump hosts and fabric controllers authenticate against the same identity service. Break-glass accounts are stored in a vault that itself depends on the identity service or is hosted in the same fault domain. Local console access to OT HMIs has been removed.

**Operating states.** Any → EMERGENCY (if concurrent incident) → RECOVERY.

**Propagation path.**

1. SEC — Identity service failure (M01 on RF-SEC-01), possibly CASCADING from a power or network event.
2. SEC → OPS — Operators cannot log in to BMS, EPMS or cluster managers (SHARED_RESOURCE).
3. SEC — Break-glass procedure depends on the same service or fault domain; break-glass is DEFEATED.
4. OPS → THM/POW/CMP — Response to any concurrent incident is DELAYED; automated systems continue unsupervised.
5. RES — Recovery of the identity service may itself require privileged access that depends on the identity service (circular recovery dependency).

**Affected Required Functions.** RF-SEC-01, RF-OPS-01, RF-RES-03, RF-NET-04, RF-GOV-01.

**Affected Service Outcomes.** Recovery time of any concurrent incident; availability; control-plane integrity.

**Safeguards that should interrupt it.**

- Cause side: identity service deployed across independent fault domains, with local authentication caches at critical systems (interrupts step 2).
- Escalation: break-glass credentials held offline in physical custody, independent of the identity service, tested on a schedule (interrupts step 3).
- Escalation: local operator panels for safety-relevant OT functions (interrupts step 4).
- Recovery: documented, non-circular identity recovery procedure (interrupts step 5).

**Relevant MCF control families.** SEC-01 Identity and privileged access; NET-04 Management and out-of-band networks; RES-04 Recovery planning; DEP-02 Shared and common-mode dependencies; OPS-01 Operating model and staffing.

**Relevant critical gates.** CG-15 Integrated digital authority over infrastructure; CG-10 Recovery readiness; CG-13 Responsibility and authority.

**Evidence that would show the safeguards work.**

- E4 break-glass test with the identity service disabled (V5, authorised window).
- E2 identity-service deployment map against fault domains.
- E1 identity recovery procedure; E4 exercise record (V4).

**Typical UNKNOWNs.** Dependence of break-glass on identity (U10; US4 on CG-15, US5 if CG-10 also affected). Hosting fault domain of identity components (U10; US4).

## X16 Alarm flood during an electrical event leads to operator mis-switching

**Initiating event.** A medium-voltage fault causes loss of one utility feed and multiple automatic transfers, generating thousands of BMS and EPMS alarms within minutes.

**Preconditions.** Alarm rationalisation has not been performed; there is no first-out or state-based suppression. Emergency operating procedures are generic. The single-line diagram on the HMI does not match the as-built after recent changes. Staffing at night is minimal.

**Operating states.** EMERGENCY → FAILED (if mis-switching) → RECOVERY.

**Propagation path.**

1. POW — Fault TRIGGERS protection and transfers; alarm flood follows (M20 on RF-OPS-01; DEMAND_SURGE on operators).
2. OPS — Alarm flood MASKS the root alarm; operator misidentifies which side is healthy (HUMAN_ACTION; systemic contributors: interface, alarm load, staffing).
3. OPS → POW — Operator opens the wrong breaker during a manual transfer, dropping the remaining healthy side (M09 on RF-OPS-02).
4. POW → THM/CMP — Load lost across the affected block; cooling pumps and CDUs on that block stop; synchronous jobs fail.
5. RES — Recovery sequence executed under stress; risk of further error.

**Affected Required Functions.** RF-OPS-01, RF-OPS-02, RF-OPS-05, RF-POW-07, RF-EVA-02.

**Affected Service Outcomes.** Availability; safety (switching error near energised equipment); recovery time.

**Safeguards that should interrupt it.**

- Cause side: alarm rationalisation and state-based suppression with first-out indication (interrupts step 2).
- Escalation: event-specific emergency operating procedures with decision aids; two-person verification for switching; key interlocks preventing unsafe breaker combinations (interrupts step 3).
- Escalation: HMI single-line diagram reconciled to as-built after every change (interrupts step 2).
- Competence: simulator or tabletop training for rare transfer scenarios.

**Relevant MCF control families.** OPS-04 Alarm, incident and problem management; OPS-01 Operating model and staffing; OPS-02 Procedure and work control; POW-06 Electrical monitoring, maintenance and recovery; EVA-02 Evidence provenance and quality.

**Relevant critical gates.** CG-07 Critical control-system integrity; CG-13 Responsibility and authority; CG-05 Resilient electrical supply.

**Evidence that would show the safeguards work.**

- E3 alarm-rate statistics during past events against the rationalisation target.
- E1 emergency operating procedures; E4 exercise records (V4).
- E1/E2 interlock schemes and HMI drawing revision control reconciled to as-built.

**Typical UNKNOWNs.** HMI as-built accuracy (U3; US3–US4). Night-shift competence for manual transfer (U5; US3).

## X17 Fire in a shared compartment disables paired A/B routes and triggers cascading shutdowns

**Initiating event.** A cable fire in a riser or an electrical room in which both A and B feeders (or both fabric trunk routes) pass.

**Preconditions.** Route segregation is by tray, not by fire compartment. The fire-alarm cause-and-effect matrix shuts down air handlers and, in one zone, initiates EPO across a wider area than intended. Clean-agent discharge in an adjacent hall requires evacuation and delays re-entry.

**Operating states.** NORMAL → EMERGENCY → FAILED → RECOVERY (extended by damage).

**Propagation path.**

1. PHY — Cable fault ignites cables (M25); smoke PROPAGATES_VIA the shared compartment.
2. PHY → POW/NET — Both A and B routes are damaged (COMMON_CAUSE through shared compartment; redundancy DEFEATED).
3. PHY → THM — Fire-alarm interface shuts down air handlers in the adjacent hall (CONTROL_ACTION; CONFLICTS_WITH continuity cooling).
4. PHY → POW — EPO initiated over a wider area than the fire zone (M24 spurious extent; M05).
5. CMP/STO — Large-scale loss of compute and storage; unclean shutdown of storage systems.
6. RES — Re-entry, damage assessment and cable replacement extend recovery; contamination cleaning of equipment.

**Affected Required Functions.** RF-PHY-04, RF-POW-05, RF-NET-06, RF-THM-05, RF-RES-01, RF-RES-03.

**Affected Service Outcomes.** Safety; availability; capacity; recovery time; physical damage.

**Safeguards that should interrupt it.**

- Cause side: segregation of A/B routes into separate fire compartments or fire-rated enclosures (interrupts step 2).
- Detection: early-warning smoke detection suited to high-airflow spaces (DELAYS escalation).
- Escalation: cause-and-effect matrix verified by integrated test so that shutdown actions are limited to the affected zone (interrupts steps 3–4).
- Consequence side: storage systems with protected write caches and orderly-shutdown signals (limits step 5).

**Relevant MCF control families.** PHY-03 Physical zoning and segregation; PHY-06 Fire, life safety and emergency interfaces; POW-04 Distribution and protection; NET-05 Physical connectivity and optics; RES-02 Fault-domain and containment design.

**Relevant critical gates.** CG-04 Life safety and hazardous energy; CG-09 Failure containment; CG-05 Resilient electrical supply.

**Evidence that would show the safeguards work.**

- E2/E1 route survey showing compartment of each A/B route, reconciled to drawings.
- E4 integrated fire-alarm cause-and-effect test record (V6) witnessed by fire and electrical engineers.
- E5 fire-strategy review by a competent fire engineer.

**Typical UNKNOWNs.** Whether A/B routes share a compartment at any point (U10; US5 if both CG-05 and CG-09 are affected). Actual extent of EPO zones (U4 if drawings and logic disagree; US4 on CG-04).

## X18 Automated remediation or AI-enabled agent performs a mass action

**Initiating event.** A telemetry pipeline defect generates false accelerator error events across a large fraction of nodes; an automated remediation system (or AI-enabled operations agent) drains and reboots the affected nodes, or applies a fleet-wide power cap, in one action.

**Preconditions.** Automation has authority to act on any number of nodes; no blast-radius limit or rate limit; no human approval above a threshold; telemetry inputs are not validated for plausibility; power-cap changes have no ramp-rate limit.

**Operating states.** NORMAL → DEGRADED → FAILED (jobs) → RECOVERY.

**Propagation path.**

1. EVA/CMP — Telemetry defect produces false indications (M18 on RF-CMP-05).
2. SEC — Automation acts on the false indications at fleet scale (CONTROL_ACTION; M08 excess output on RF-SEC-03).
3. SEC → CMP — Mass drain and reboot terminates many jobs (CASCADE).
4. CMP → POW — Sudden load drop followed by restart surge creates large load steps at UPS and, if on generator, at the generators (DEMAND_SURGE; links to X01).
5. CMP → THM — Cooling-plant control responds to rapid load change; overshoot or undershoot of supply temperature (M13 on RF-THM-08).
6. CMP → STO — Restart storm on provisioning and checkpoint storage (links to X04).

**Affected Required Functions.** RF-SEC-03, RF-CMP-05, RF-CMP-06, RF-CAP-01, RF-POW-06, RF-THM-08, RF-STO-03.

**Affected Service Outcomes.** Availability; training completion; recovery time; electrical and thermal stability.

**Safeguards that should interrupt it.**

- Cause side: plausibility checks on telemetry before automated action (interrupts step 1).
- Escalation: blast-radius and rate limits on automated actions; human approval above a node-count or power threshold; command allowlisting (interrupts step 2).
- Escalation: ramp-rate limits on fleet power-cap changes (interrupts step 4).
- Consequence side: restart admission control (limits step 6).

**Relevant MCF control families.** SEC-06 AI-enabled and automated action; CMP-05 Compute health and observability; CAP-05 Operating envelope; POW-05 Power quality and transient response; THM-06 Thermal control, maintenance and recovery.

**Relevant critical gates.** CG-15 Integrated digital authority over infrastructure; CG-09 Failure containment; CG-05 Resilient electrical supply.

**Evidence that would show the safeguards work.**

- E2 automation policy configuration showing limits, approvals and allowlists.
- E4 test in a staging environment that an above-threshold action is blocked or held for approval (V5).
- E3 automation action logs reconciled to approvals.

**Typical UNKNOWNs.** Full set of automation systems with infrastructure authority (U1; US4 on CG-15). Electrical effect of maximum credible load step from automation (U1; US4 on CG-05).

## X19 Colocation density increase silently consumes resilient capacity

**Initiating event.** A colocation tenant replaces equipment with a higher-density accelerator generation within its contracted power allocation, but with a less diversified, more synchronous load profile and higher liquid-cooling demand.

**Preconditions.** The provider's capacity model assumes diversity across tenants. The tenant's CDUs depend on provider facility water within a supply-temperature band. The shared-responsibility matrix does not specify notification of load-profile change or of provider plant maintenance. The tenant has no evidence rights to provider plant telemetry.

**Operating states.** NORMAL (apparent) → MAINTENANCE (provider chiller maintenance) → DEGRADED → EMERGENCY.

**Propagation path.**

1. CAP — Tenant load-profile change (DEMAND_SURGE in peak terms) CONTRIBUTES_TO loss of provider headroom (M14 on RF-CAP-02), LATENT because contracted kW are not exceeded.
2. DEP — Responsibility gap: neither party analyses the combined effect (M17 on RF-DEP-02).
3. THM — Provider takes one chiller out for maintenance assuming N+1 exists (ENABLING; HUMAN_ACTION).
4. THM — At peak load, facility water supply temperature exceeds the tenant CDU's band (M07 on RF-THM-04).
5. THM → CMP — Tenant accelerators throttle; jobs slow or fail.
6. GOV/DEP — Contractual dispute over responsibility; evidence missing on both sides, producing evidence and attribution loss.

**Affected Required Functions.** RF-CAP-02, RF-DEP-02, RF-THM-04, RF-THM-03, RF-GOV-02, RF-EVA-01.

**Affected Service Outcomes.** Tenant training throughput; provider service levels; contractual commitments.

**Safeguards that should interrupt it.**

- Cause side: shared-responsibility record that requires notification and joint assessment of load-profile changes; provider capacity model using measured peak and correlation (interrupts steps 1–2).
- Escalation: provider maintenance readiness check against measured load; notification to tenants (interrupts step 3).
- Detection: tenant monitoring of facility water supply temperature at CDU inlet with alerts; shared telemetry (interrupts step 4).

**Relevant MCF control families.** DEP-05 Boundary and interface control; SUP-02 Contract and service obligations; CAP-04 Demand and growth modelling; THM-01 Thermal architecture and capacity; OPS-06 Capacity and service operations.

**Relevant critical gates.** CG-03 Critical dependency visibility; CG-06 Thermal continuity; CG-13 Responsibility and authority.

**Evidence that would show the safeguards work.**

- E1 shared-responsibility record and contract clauses for notification and evidence rights.
- E3 measured peak load and supply-temperature data at CDU inlets.
- E7 provider resilient-capacity calculation with measured tenant profiles.

**Typical UNKNOWNs.** Provider resilient capacity (U2; US4 on CG-06). Other tenants' load profiles (U2; US3).

## X20 Compound regional event: flood, extended grid loss, telecom loss and fuel logistics

**Initiating event.** A regional storm causes river flooding, extended grid outage, loss of public telecom and road closures around the site.

**Preconditions.** Ground-level switchgear and fuel tank fill points lie within a credible flood extent; fuel autonomy is sized for a delivery interval that assumes open roads; fuel suppliers are regional and share the same roads; staff relief depends on public transport; generators have not run for an extended duration recently; fuel quality has not been tested for some time.

**Operating states.** NORMAL → EMERGENCY → DEGRADED (on generators, extended) → possible SHUTDOWN (controlled) → RECOVERY.

**Propagation path.**

1. PHY/ENV — Flood threatens switchgear and fuel-system equipment (EXTERNAL_EVENT).
2. POW — Grid loss (EXTERNAL_EVENT, CORRELATES_WITH step 1) TRIGGERS generator operation for an extended period.
3. POW — Extended running reveals fuel contamination or filter blockage (LATENT; M21 on RF-POW-02); one or more generators fail; K_OF_N redundancy at risk.
4. DEP/SUP — Road closures and regional demand prevent fuel replenishment (M10 on RF-SUP-02 and RF-DEP-02; DELAYS replenishment beyond autonomy).
5. NET — Public telecom loss removes WAN and remote support (links to X09, X15).
6. OPS — Staff fatigue and inability to relieve shifts (HUMAN_ACTION contributors).
7. RES — Decision to degrade to minimum Service Outcome, migrate workloads or execute a controlled shutdown before fuel exhaustion; if not pre-decided, decision delay increases the probability of uncontrolled shutdown (M23).

**Affected Required Functions.** RF-PHY-05, RF-POW-02, RF-SUP-02, RF-DEP-02, RF-NET-03, RF-OPS-05, RF-RES-02, RF-RES-05, RF-GOV-01.

**Affected Service Outcomes.** Availability; recovery; safety (flood and fuel handling); strategic or sovereignty outcomes if workloads must move.

**Safeguards that should interrupt it.**

- Cause side: flood protection of critical plant above the credible flood level; site hazard assessment (interrupts step 1).
- Escalation: fuel quality testing and polishing programme; periodic extended-duration generator runs (interrupts step 3).
- Escalation: fuel autonomy sized for the replenishment scenario, multiple suppliers with priority contracts and independent routes (interrupts step 4).
- Consequence side: pre-approved crisis priorities, graceful degradation and controlled shutdown plan; staff welfare and accommodation plan (limits steps 6–7).
- Consequence side: alternate site capacity with tested migration (limits step 7).

**Relevant MCF control families.** PHY-01 Site and location resilience; POW-02 Generation and fuel; SUP-05 Spares, logistics and obsolescence; RES-03 Continuity planning; RES-06 Crisis and adaptive response; ENV-06 Climate adaptation and resource continuity; OPS-01 Operating model and staffing.

**Relevant critical gates.** CG-03 Critical dependency visibility; CG-05 Resilient electrical supply; CG-10 Recovery readiness; CG-04 Life safety and hazardous energy.

**Evidence that would show the safeguards work.**

- E7 site flood assessment and plant elevation survey.
- E4 extended-duration generator run records and fuel quality test results.
- E1 fuel supply contracts, autonomy calculation and replenishment plan; E4 crisis exercise (V4).
- E4 workload migration test to alternate capacity (V6).

**Typical UNKNOWNs.** Fuel supplier performance under regional event (U2; US4 on CG-05). Credible flood extent under updated projections (U9; US3–US4). Staff availability (U5; US3).

## Scenario prioritisation

Scenarios shall be prioritised for analysis depth and validation effort when any of the following apply; each criterion is linked to the gate it most directly engages.

| **Priority criterion** | **Primary gate** |
|------------------------|------------------|
| Life safety or hazardous energy | CG-04 |
| Essential cooling loss | CG-06 |
| Standby or resilient power loss | CG-05 |
| Containment failure | CG-09 |
| Large capability concentration | CG-03 |
| Checkpoint or recovery-baseline corruption | CG-10 |
| Common-mode defeat of redundancy | CG-09 |
| Recovery objective at risk | CG-10 |
| Weakly evidenced external dependency | CG-03 |
| Long-lead or irreplaceable component | CG-10 |
| Control-plane or remote-access exposure | CG-15 |
| Sovereignty impact | CG-01 |
| Critical UNKNOWN (US4 or US5) | CG-12 |

# Part XV - Assessment records and evidence

## 42. Assessment workflow

| **Step** | **Activity** | **Canonical chain steps** |
|----------|--------------|---------------------------|
| 1 | Frame decision question, Capability Instance, Service Outcomes, tolerances, boundary and operating states. | 1–3 |
| 2 | Confirm intended, as-built, commissioned and observed baselines. | 5 |
| 3 | Map Required Functions, assets, interfaces, dependencies and fault domains. | 4–6 |
| 4 | Identify threats, hazards, causes and failure modes (Appendix A as seed). | 7 |
| 5 | Construct local, cross-domain, compound, maintenance and recovery scenarios; instantiate the X01–X20 library. | 7 |
| 6 | Analyse effects, propagation, timing and concentration with the techniques in Part X. | 7 |
| 7 | Map safeguards, their dependencies and their linked controls. | 8–9 |
| 8 | Define evidence requirements and validate safely (Part IX §19). | 10–11 |
| 9 | Determine control results, residual state, UNKNOWN Records (Part XII) and gate effects. | 12–14 |
| 10 | Report findings, actions, retest and reassessment triggers. | 13–16 and loop |

## 43. Evidence sources mapped to AIDCF-008 classes

| **Evidence source** | **Examples** | **AIDCF-008 class** |
|---------------------|--------------|---------------------|
| Architecture | Single-line diagrams, P&IDs, fabric topologies, control narratives, cause-and-effect matrices. | E1 |
| As-built and configuration | Registers, protection settings, firmware inventories, switch configurations, cord-to-feed mappings. | E2 |
| Commissioning and testing | Functional, integrated, load, failover and recovery test records. | E4 |
| Operations | Telemetry, alarms, trends, work orders and logs. | E3 |
| Incident | Timelines, cause analyses and near-miss records. | E3, E7 |
| Supplier and contract | Service levels, support terms, spares, lead times, responsibility records, third-party test reports. | E1, E5 |
| Observation and interview | Walkthroughs, witnessed actions and competent testimony. | E6 |
| Engineering analysis | Studies, calculations and validated simulations. | E7 |
| Threat evidence | Site threat assessments, access records, security events and intelligence. | E3, E5 |

## 44. Finding taxonomy

| **Finding** | **Meaning** | **Typical gate engaged** |
|-------------|-------------|--------------------------|
| Uncontrolled path | Material consequence without an effective credited barrier. | Gate whose scope the path traverses |
| Fragile safeguard | Barrier has a shared dependency, inadequate capacity or duration, or weak validation. | CG-09 or the protected gate |
| Common-mode exposure | Alternatives share a cause or dependency. | CG-03, CG-09 |
| Containment gap | Effect crosses an intended boundary. | CG-09 |
| Capacity cliff | A small change creates disproportionate loss. | CG-05, CG-06, CG-08 |
| Recovery fragility | Restoration depends on unproven state, people or resources. | CG-10 |
| Evidence gap | Material assertion inadequately supported. | CG-11 |
| State coverage gap | DEGRADED, MAINTENANCE, TRANSITION or RECOVERY state not covered. | Protected gate |
| Responsibility gap | Authority or evidence obligation unclear. | CG-13 |
| Control-plane overreach | Digital authority reaches infrastructure without bounds. | CG-15 |
| Critical UNKNOWN | Unresolved US4 or US5 UNKNOWN on a decisive path. | CG-12 |

**THF-REQ-043** Each THF finding shall reference the scenario, the step or safeguard concerned, the gate engaged and the controls affected, and shall be recorded as an AIDCF-014 Finding with a CHALLENGES relationship to the affected claim.

# Part XVI - Machine-readable model

## 45. Object mapping to AIDCF-014

v1.0 defined local node types. In v1.1 all scenario content is carried by AIDCF-014 canonical classes; v1.0 node names are retained only as aliases.

| **v1.0 node** | **Canonical AIDCF-014 class or field** |
|---------------|----------------------------------------|
| ThreatSource, ThreatEvent | Threat |
| Hazard | Hazard |
| InitiatingEvent | FailureScenario.initiatingSource (references Threat, Hazard or Event) |
| FailureCause | FailureScenario.steps[].cause |
| FailureMode | FailureMode |
| Effect, PropagationStep | FailureScenario.steps[] |
| Consequence | FailureScenario.outcomeEffects |
| Safeguard, BarrierClaim | Safeguard (claim expressed through linked Control and ControlAssessment) |
| RecoveryAction | FailureScenario.steps[] with operator RECOVERS; Action for remediation |
| Scenario | FailureScenario |
| EvidenceObject | EvidenceObject |
| Finding | Finding; UnknownRecord for UNKNOWNs |
| AssuranceDecision | AssuranceDecision (not owned by this standard) |

## 46. Relationship mapping to the canonical vocabulary

Structural relationships use the 41 canonical AIDCF-014 relationship types. v1.0 relationship names map as follows; names with no structural equivalent become scenario-step operators (Part VIII §15).

| **v1.0 relationship** | **v1.1 representation** |
|-----------------------|-------------------------|
| TARGETS, EXPOSES | EXPOSED_TO (asset or system EXPOSED_TO Threat or Hazard) |
| INITIATES | INITIATES |
| HAS_CAUSE, FAILS_AS, HAS_LOCAL_EFFECT | FailureScenario.steps[] fields (cause, failureMode, effect) |
| CAUSES, CONTRIBUTES_TO, TRIGGERS, AMPLIFIED_BY | Step operators CAUSES, CONTRIBUTES_TO, TRIGGERS, AMPLIFIES |
| PROPAGATES_VIA | Step operator PROPAGATES_VIA, with DEPENDS_ON or CONSUMES_RESOURCE to the conduit |
| PROPAGATES_TO, AFFECTS | PROPAGATES_TO |
| PREVENTED_BY, DETECTED_BY, CONTAINED_BY | PROTECTED_BY, with Safeguard.function = prevent, detect or contain |
| RECOVERED_BY | RECOVERS_THROUGH |
| (v1.0 BarrierClaim to control link) | GOVERNED_BY (Safeguard GOVERNED_BY Control) |
| DEFEATS | Step operator DEFEATS; CHALLENGES from the Event or Finding to the safeguard claim |
| DEPENDS_ON | DEPENDS_ON |
| EVIDENCED_BY | EVIDENCED_BY |
| CHALLENGED_BY | CHALLENGES (inverse direction) |
| RESULTS_IN | RESULTS_IN |
| INVALIDATES | INVALIDATED_BY (inverse direction) |

## 47. Validation rules

| **Rule** | **Validation statement** |
|----------|--------------------------|
| THF-VAL-01 | Every FailureScenario references one Capability Instance, at least one Service Outcome with tolerance, a boundary and a baseline (class A fields non-UNKNOWN). |
| THF-VAL-02 | Every step has exactly one primary operator from Table 15.1. |
| THF-VAL-03 | Every PROPAGATES_VIA step references a conduit that exists as a Dependency or Resource. |
| THF-VAL-04 | Every CORRELATES_WITH step names a shared element linked by SHARES_FAULT_DOMAIN_WITH, or has a U10 UNKNOWN Record. |
| THF-VAL-05 | Every credited Safeguard has stateCoverage including the states the scenario traverses at its interruption point. |
| THF-VAL-06 | Every credited Safeguard on a decisive path has at least one controlRef to an AIDCF-007A control. |
| THF-VAL-07 | Every UNKNOWN Record linked to a scenario has a type U1–U10 and severity US1–US5. |
| THF-VAL-08 | No decisive path with an upstream-segment UNKNOWN of US4 or US5 is linked by SUPPORTS to a positive claim. |
| THF-VAL-09 | Every outcomeEffect carries a consequence family and a severity band CS0–CS5. |
| THF-VAL-10 | Every scenario has at least one ReassessmentTrigger. |

## 48. Publication package

- OWL ontology and Turtle serialisation using the namespace https://w3id.org/aidcf/ontology# (prefix aidcf:), version IRI https://w3id.org/aidcf/ontology/1.3 (w3id registration is pending).
- JSON-LD context and examples.
- JSON Schema for FailureScenario and Safeguard exchange conforming to AIDCF-014.
- SHACL shapes implementing THF-VAL-01 to THF-VAL-10.
- CSV registries for failure modes (M00–M30), operators and qualifiers, consequence families, reference Required Functions and the Appendix A catalogue.
- Worked instantiations of X02 (liquid cooling) and X04 (distributed-training recovery).
- Changelog, migration and extension guidance.

# Part XVII - Governance and acceptance

- Controlled vocabulary and change board for operators, qualifiers, failure-mode codes and consequence families.
- Multidisciplinary domain review covering all fifteen domains.
- Semantic versioning and migration records (AIDCF-014 MigrationRecord).
- Normative core separated from informative examples (the X01–X20 library and Appendix A are reference content, not evidence).
- Independent incident and test comparison: scenarios are compared with real events and near misses at least at each reassessment.
- Inter-assessor consistency testing on scenario instantiation and UNKNOWN severity classification.
- Security classification and access control for sensitive paths (attack paths, route details, protection settings).
- Vendor neutrality and conflict declarations.

**THF-REQ-044** Instantiated scenarios that reveal exploitable attack paths, physical routes or protection weaknesses shall be classified and distributed only to authorised recipients (AIDCF-014 DistributionControl).

## 49. Prohibited practices

- Treating a generic list (including this library) as a complete assessment.
- Unsupported precise probability.
- Averages or risk priority numbers overriding critical gates.
- Stopping causal analysis at operator error.
- Assuming duplicated paths are independent.
- Treating an untested safeguard as effective.
- Ignoring recovery-only dependencies.
- Unsafe intrusive validation.
- Downgrading UNKNOWN severity on the basis of assumed low likelihood.
- Publishing sensitive paths without access control.

# Appendix A - Failure-mode catalogue by Required Function

This catalogue is the seed for bottom-up analysis (T01). It lists reference Required Functions for AI data centres, grouped by the fifteen domains, and for each function only the failure modes (Part VII codes) that are physically or logically meaningful for it. Capability Instances map their declared Required Functions to these reference functions; the catalogue is not exhaustive and does not replace site-specific FMEA.

Columns: **Mode** is the Part VII code; **Typical causes** are examples, not a complete list; **Detection** is how the mode is normally revealed; **Effect on outcome** is the typical end effect if no safeguard acts; **Families** are the AIDCF-007A control families most directly addressing the mode.

## A.0 Reference Required Functions

| **ID** | **Required Function** |
|--------|-----------------------|
| RF-GOV-01 | Exercise decision and risk-acceptance authority for critical infrastructure, including during emergencies |
| RF-GOV-02 | Govern exceptions, temporary deviations and their expiry |
| RF-CAP-01 | Keep AI workload electrical and thermal demand within the declared envelope (power capping, ramp-rate limits) |
| RF-CAP-02 | Allocate and reserve resilient capacity for committed Service Outcomes |
| RF-DEP-01 | Maintain a current, reconciled dependency and fault-domain map |
| RF-DEP-02 | Detect and respond to degradation of external providers (utility, carrier, water, fuel, colocation, cloud) |
| RF-PHY-01 | Prevent unauthorised entry to critical zones |
| RF-PHY-02 | Detect, attribute and record physical access and asset movement |
| RF-PHY-03 | Provide structural support and anchorage for high-density equipment |
| RF-PHY-04 | Detect fire and execute suppression and emergency interfaces |
| RF-PHY-05 | Exclude external water and flood from critical spaces |
| RF-POW-01 | Import utility power within quality limits |
| RF-POW-02 | Start, synchronise and carry load on standby generation |
| RF-POW-03 | Bridge supply through UPS and energy storage |
| RF-POW-04 | Detect and clear electrical faults selectively |
| RF-POW-05 | Distribute power to racks within rating, maintaining A/B independence |
| RF-POW-06 | Withstand load transients and power-quality interactions from AI workloads |
| RF-POW-07 | Monitor electrical state (EPMS) |
| RF-THM-01 | Capture heat at accelerators and components (cold plates and air) |
| RF-THM-02 | Circulate TCS coolant at required flow and pressure (CDU pumping) |
| RF-THM-03 | Transfer heat from TCS to facility water (CDU heat exchange) |
| RF-THM-04 | Reject heat to atmosphere (chillers, towers, dry coolers) |
| RF-THM-05 | Maintain air-side conditions for residual air-cooled load |
| RF-THM-06 | Detect, contain and isolate coolant leaks |
| RF-THM-07 | Maintain coolant and water quality |
| RF-THM-08 | Control thermal plant stably (setpoints, sequencing, sensor trust) |
| RF-ENV-01 | Maintain IT environmental conditions (humidity, dew point, contamination) |
| RF-ENV-02 | Secure water supply for heat rejection |
| RF-ENV-03 | Measure and attribute energy, water and carbon |
| RF-ENV-04 | Contain hazardous materials (refrigerant, fuel, electrolyte, glycol, suppressant) |
| RF-CMP-01 | Provide healthy, correctly computing accelerators and nodes |
| RF-CMP-02 | Maintain scale-up domain integrity |
| RF-CMP-03 | Schedule and place jobs respecting capacity and fault domains |
| RF-CMP-04 | Maintain the approved firmware and driver baseline |
| RF-CMP-05 | Detect and drain unhealthy nodes |
| RF-CMP-06 | Provision and rebuild nodes from a trusted image |
| RF-STO-01 | Serve training and inference data at required throughput and latency |
| RF-STO-02 | Persist checkpoints durably within the checkpoint window |
| RF-STO-03 | Restore checkpoints for restart within recovery tolerance |
| RF-STO-04 | Preserve data and metadata integrity |
| RF-STO-05 | Maintain protected and immutable recovery copies |
| RF-NET-01 | Transport collective traffic on the scale-out fabric with bounded loss and latency |
| RF-NET-02 | Provide path diversity and contained reconvergence |
| RF-NET-03 | Transport storage, frontend and WAN traffic with isolation |
| RF-NET-04 | Provide out-of-band management reachability |
| RF-NET-05 | Provide core services: time, DNS, DHCP, IPAM |
| RF-NET-06 | Maintain physical connectivity (optics and cabling) |
| RF-OPS-01 | Detect, prioritise and respond to alarms and incidents |
| RF-OPS-02 | Control work and hazardous-energy isolation (permit to work, lockout/tagout) |
| RF-OPS-03 | Control change and temporary configuration |
| RF-OPS-04 | Maintain assets on condition |
| RF-OPS-05 | Staff, authorise and hand over critical operations |
| RF-RES-01 | Contain failures within declared fault domains |
| RF-RES-02 | Degrade gracefully to the minimum Service Outcome |
| RF-RES-03 | Restore infrastructure in a safe, correct sequence |
| RF-RES-04 | Restore workloads, configuration and data to a validated state |
| RF-RES-05 | Provide alternate capacity on demand |
| RF-SUP-01 | Supply authentic, correct and compatible firmware and software |
| RF-SUP-02 | Supply critical spares and consumables (including fuel) within recovery tolerance |
| RF-SUP-03 | Provide OEM and integrator support when required |
| RF-SUP-04 | Supply authentic hardware components |
| RF-SEC-01 | Authenticate and authorise human and machine identities to infrastructure |
| RF-SEC-02 | Enforce segmentation between IT, OT, management and AI control planes |
| RF-SEC-03 | Bound automated and AI-enabled actions on infrastructure |
| RF-SEC-04 | Detect and contain intrusion in OT and control planes |
| RF-SEC-05 | Protect protection, interlock and safety logic from unauthorised modification |
| RF-EVA-01 | Capture and retain trustworthy telemetry and logs as evidence |
| RF-EVA-02 | Reconcile as-built and observed state to the approved design |
| RF-EVA-03 | Preserve UNKNOWNs and conflicts through to decision |

## A.1 GOV

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-GOV-001 | RF-GOV-01 | M10 Delayed output | Authority not delegated out of hours; escalation contacts stale; identity or phone systems degraded. | Exercise timing; incident timelines. | Load shedding or continuity invocation too late; uncontrolled shutdown. | GOV-02, RES-06 |
| FM-GOV-002 | RF-GOV-01 | M09 Incorrect output | Decision taken by a role without authority; priorities not pre-agreed (continuity versus safety). | Post-incident review; decision log audit. | Wrong workloads shed; safety actions overridden. | GOV-01, GOV-02 |
| FM-GOV-003 | RF-GOV-02 | M22 Bypass left active | Exceptions without expiry; no review cadence. | Exception register ageing report. | Predisposing condition for other scenarios (for example disabled interlock). | GOV-03 |
| FM-GOV-004 | RF-GOV-02 | M09 Incorrect output | Exception approved without impact assessment on gates. | Exception audit against gate scope. | Unrecognised gate defeat. | GOV-03, GOV-04 |

## A.2 CAP

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-CAP-001 | RF-CAP-01 | M08 Excess output | Power capping not configured on new hardware; job mix change; capping service down. | Rack and row power telemetry versus envelope. | Busway, UPS or cooling demand beyond design; protection trips. | CAP-05, POW-05 |
| FM-CAP-002 | RF-CAP-01 | M13 Unstable/oscillating | Synchronous compute/communication phases; no ramp-rate limiting. | High-resolution power-quality recording. | Generator or UPS instability; utility interconnection non-compliance. | CAP-04, POW-05 |
| FM-CAP-003 | RF-CAP-01 | M24 Spurious operation | Capping triggered by false telemetry or wrong threshold. | Throughput drop correlated with cap events. | Unnecessary performance loss. | CAP-05, CMP-05 |
| FM-CAP-004 | RF-CAP-02 | M29 Misallocation | Resilient reserve sold or allocated to growth; diversity assumptions. | Capacity reconciliation of committed versus resilient capacity. | N+1 exists on paper only; outage in MAINTENANCE or DEGRADED. | CAP-04, OPS-06 |
| FM-CAP-005 | RF-CAP-02 | M14 Capacity exhaustion | Growth beyond forecast; stranded capacity from a limiting dependency. | Capacity forecasting; headroom alarms. | Unable to place committed workloads. | CAP-04, CAP-06 |

## A.3 DEP

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-DEP-001 | RF-DEP-01 | M09 Incorrect output | As-built divergence; undocumented changes; shared dependencies not modelled. | Reconciliation against inspection and telemetry. | Redundancy and containment claims invalid. | DEP-01, DEP-02, EVA-02 |
| FM-DEP-002 | RF-DEP-01 | M17 Loss of visibility | Recovery-only and external dependencies never recorded. | Recovery exercises; T08 gap analysis. | Recovery fails on an unplanned dependency. | DEP-01, RES-04 |
| FM-DEP-003 | RF-DEP-02 | M19 Failure to alarm | No provider health indicators; notification obligations absent. | Provider performance review. | Late response to utility, carrier or water degradation. | DEP-06, SUP-02 |
| FM-DEP-004 | RF-DEP-02 | M04 Failure to transfer | Alternative provider not contracted or not compatible. | Substitution readiness test. | Extended outage dependent on one provider. | DEP-04, DEP-03 |

## A.4 PHY

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-PHY-001 | RF-PHY-01 | M01 Complete loss | Access control system outage with fail-open doors; power loss to locks. | Door status monitoring; alarm. | Zones unprotected; sabotage exposure. | PHY-04 |
| FM-PHY-002 | RF-PHY-01 | M07 Degraded output | Tailgating; shared credentials; poor visitor control. | Anti-passback events; video review. | Unattributed access to critical plant. | PHY-04 |
| FM-PHY-003 | RF-PHY-01 | M05 Failure to isolate | Fire-alarm door release opens multiple security zones. | Cause-and-effect review; integrated test. | Zone collapse during emergency. | PHY-03, PHY-06 |
| FM-PHY-004 | RF-PHY-02 | M17 Loss of visibility | CCTV blind spots at plant and fibre entry; recorder failure. | Coverage survey; recorder health. | Intrusion or tampering unattributed. | PHY-04 |
| FM-PHY-005 | RF-PHY-02 | M01 Complete loss | Retention period shorter than detection lag; storage overwrite. | Retention audit. | Evidence and attribution loss. | PHY-04, EVA-01 |
| FM-PHY-006 | RF-PHY-02 | M19 Failure to alarm | Asset movement without custody record; media removal. | Inventory reconciliation. | Theft of accelerators or data-bearing media undetected. | PHY-05 |
| FM-PHY-007 | RF-PHY-03 | M14 Capacity exhaustion | Liquid-cooled rack-scale systems and filled manifolds exceed floor or slab rating. | Structural assessment against actual rack mass. | Structural damage; life-safety risk. | PHY-02 |
| FM-PHY-008 | RF-PHY-03 | M01 Complete loss | Inadequate anchorage under seismic event or vibration. | Anchorage inspection; seismic assessment. | Rack toppling; fluid and electrical hazards. | PHY-02 |
| FM-PHY-009 | RF-PHY-04 | M19 Failure to alarm | Detection unsuited to high airflow; detector contamination. | Detector testing; smoke tests. | Fire grows before response. | PHY-06 |
| FM-PHY-010 | RF-PHY-04 | M24 Spurious operation | Detector fault, dust from construction, logic error. | Discharge or shutdown without fire. | Unnecessary suppression discharge or cooling shutdown. | PHY-06 |
| FM-PHY-011 | RF-PHY-04 | M09 Incorrect output | Cause-and-effect matrix shuts down wider area or wrong plant; EPO zone wider than fire zone. | Integrated cause-and-effect test. | Cascade from local fire to hall-wide outage. | PHY-06, THM-06 |
| FM-PHY-012 | RF-PHY-04 | M05 Failure to isolate | Fire stopping breached at penetrations; shared compartments for A/B routes. | Fire-stopping survey. | Fire or smoke disables redundant paths. | PHY-03, PHY-06 |
| FM-PHY-013 | RF-PHY-05 | M25 Leakage/escape | Roof or façade failure; pipe routes over halls; flood barriers not deployed. | Water detection; inspection. | Water on IT or electrical equipment. | PHY-01, PHY-02 |
| FM-PHY-014 | RF-PHY-05 | M26 Congestion/blockage | Drainage blocked; pumps failed. | Drain inspection; pump alarms. | Flood ingress during heavy rain. | PHY-01, ENV-06 |

## A.5 POW

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-POW-001 | RF-POW-01 | M01 Complete loss | Grid fault, upstream protection, extreme weather, utility maintenance. | Utility monitoring relays; EPMS. | Transfer to UPS and generation; exposure to X01 path. | POW-01 |
| FM-POW-002 | RF-POW-01 | M07 Degraded output | Voltage sags, swells, unbalance, frequency deviations. | Power-quality meters (IEC 61000-4-30 class instruments). | UPS transfers; rack power supply dropouts. | POW-05, POW-01 |
| FM-POW-003 | RF-POW-01 | M12 Intermittent operation | Repeated auto-reclose; marginal utility connection. | Event recorder. | Repeated transfers; battery cycling; generator start/stop. | POW-01, POW-03 |
| FM-POW-004 | RF-POW-02 | M02 Failure to start | Starting battery failure; fuel supply fault; control fault; low coolant temperature. | Start tests; generator controller alarms. | UPS autonomy exhausted; load lost. | POW-02 |
| FM-POW-005 | RF-POW-02 | M07 Degraded output | Inability to accept large load steps; governor or AVR mistuned; derating at high ambient. | Load-acceptance test with dynamic profile. | Frequency/voltage excursion; UPS rejects source; load lost. | POW-02, POW-05 |
| FM-POW-006 | RF-POW-02 | M27 Loss of synchronisation | Paralleling controller fault; breaker failure to close. | Paralleling alarms; integrated tests. | Insufficient generation online; load shedding. | POW-02, POW-06 |
| FM-POW-007 | RF-POW-02 | M21 Latent standby failure | Fuel contamination, filter blockage, fuel degradation in storage. | Fuel quality testing; extended runs. | Generator stops during extended outage. | POW-02, OPS-03 |
| FM-POW-008 | RF-POW-02 | M14 Capacity exhaustion | Fuel autonomy shorter than replenishment time. | Autonomy calculation; level monitoring. | Controlled or uncontrolled shutdown. | POW-02, SUP-05 |
| FM-POW-009 | RF-POW-03 | M04 Failure to transfer | Inverter fault; static switch fault; battery string open. | UPS alarms; transfer tests. | Instant load loss on mains disturbance. | POW-03 |
| FM-POW-010 | RF-POW-03 | M07 Degraded output | Battery capacity fade; high temperature; cell failures. | Battery monitoring; runtime tests. | Runtime shorter than generator acceptance time. | POW-03 |
| FM-POW-011 | RF-POW-03 | M24 Spurious operation | Unnecessary transfer to bypass on internal fault or overload. | UPS event logs. | Load exposed to raw utility; disturbance passes to IT. | POW-03 |
| FM-POW-012 | RF-POW-03 | M25 Leakage/escape | Lithium-ion thermal runaway; VRLA hydrogen release. | Battery management alarms; off-gas or hydrogen detection. | Fire, explosion, toxic exposure (X06). | POW-03, PHY-06, ENV-05 |
| FM-POW-013 | RF-POW-03 | M22 Bypass left active | Maintenance bypass not returned after work. | UPS status monitoring; handover checks. | Loss of ride-through for next disturbance. | POW-03, OPS-02 |
| FM-POW-014 | RF-POW-04 | M05 Failure to isolate | Protection device failure; settings wrong; CT or trip-circuit fault. | Protection testing; trip-circuit supervision. | Upstream clearance; larger outage; equipment damage. | POW-04 |
| FM-POW-015 | RF-POW-04 | M24 Spurious operation | Nuisance trips from inrush, harmonics, earth leakage from rectifier loads. | Trip records analysis. | Unnecessary loss of distribution section. | POW-04, POW-05 |
| FM-POW-016 | RF-POW-04 | M09 Incorrect output | Miscoordination after load growth or device change. | Coordination study review against as-built. | Wider outage than fault location requires. | POW-04 |
| FM-POW-017 | RF-POW-04 | M08 Excess output | Arc-flash incident energy beyond study or PPE category due to setting change. | Arc-flash study update; settings audit. | Life-safety exposure during work. | POW-04, OPS-02 |
| FM-POW-018 | RF-POW-05 | M14 Capacity exhaustion | Rack power growth beyond busway, PDU or power-shelf rating; single-feed loading during maintenance. | Per-circuit metering versus rating. | Overload trip; cascade to adjacent racks. | POW-04, CAP-05 |
| FM-POW-019 | RF-POW-05 | M29 Misallocation | Cords connected to wrong feed; both cords on one side. | Cord-to-feed audit; EPMS per-outlet data. | Dual-corded racks lose both feeds when one path is removed (X11). | POW-04, EVA-02 |
| FM-POW-020 | RF-POW-05 | M07 Degraded output | High-resistance joints in busway or terminations. | Thermography; joint temperature monitoring. | Overheating, fire risk, outage. | POW-04, OPS-03 |
| FM-POW-021 | RF-POW-06 | M13 Unstable/oscillating | Interaction between AI load swings and generator, UPS or grid control. | High-resolution recording; transient studies. | Equipment trips; non-compliance with grid connection. | POW-05, CAP-04 |
| FM-POW-022 | RF-POW-06 | M08 Excess output | Harmonic distortion or resonance with power-factor correction. | Harmonic measurement; resonance study. | Overheating; capacitor failure; protection operation. | POW-05 |
| FM-POW-023 | RF-POW-07 | M17 Loss of visibility | EPMS network or server failure; meter communication loss. | Communication health alarms. | Operators blind during events. | POW-06, NET-04 |
| FM-POW-024 | RF-POW-07 | M18 False indication | Meter misconfiguration; wrong CT ratio; time skew in sequence-of-events. | Cross-check with independent meters. | Wrong operator decisions; misleading evidence. | POW-06, EVA-02 |

## A.6 THM

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-THM-001 | RF-THM-01 | M07 Degraded output | Cold-plate fouling; poor thermal interface; flow maldistribution in manifold. | Accelerator temperature versus coolant temperature trend. | Throttling of individual accelerators; job slowdown. | THM-03, CMP-05 |
| FM-THM-002 | RF-THM-01 | M26 Congestion/blockage | Particulate or biological growth in microchannels; air lock after fill. | Flow per rack; temperature anomaly. | Localised overheating; device shutdown. | THM-03, THM-05 |
| FM-THM-003 | RF-THM-02 | M01 Complete loss | Pump failure; controller fault; loss of power to pumps. | Flow and differential-pressure alarms. | Rapid thermal transient; accelerator shutdown (X02). | THM-03 |
| FM-THM-004 | RF-THM-02 | M04 Failure to transfer | Standby pump depends on same controller; standby failed latently. | Periodic pump changeover test. | Redundancy defeated on duty pump failure. | THM-03, THM-06 |
| FM-THM-005 | RF-THM-02 | M07 Degraded output | Strainer blockage; pump wear; air entrainment; valve mispositioned. | Flow trend; pressure drop across strainers. | Reduced cooling at peak load; throttling. | THM-03, OPS-03 |
| FM-THM-006 | RF-THM-02 | M08 Excess output | Overpressure from control fault or closed valve; water hammer on pump start. | Pressure transducers; relief valve operation. | Hose or QD failure; leak (X07). | THM-03 |
| FM-THM-007 | RF-THM-02 | M24 Spurious operation | Pumps stop on false low-level or leak signal. | Event logs; correlation with sensor faults. | Unnecessary loss of flow. | THM-03, THM-06 |
| FM-THM-008 | RF-THM-03 | M07 Degraded output | Heat-exchanger fouling on facility side; facility water too warm. | Approach-temperature trending. | TCS supply temperature rise; throttling (X08). | THM-03, THM-05 |
| FM-THM-009 | RF-THM-03 | M25 Leakage/escape | Heat-exchanger plate breach mixing fluids. | Chemistry change in TCS; level changes. | TCS contamination; corrosion; fouling. | THM-05 |
| FM-THM-010 | RF-THM-04 | M14 Capacity exhaustion | Ambient beyond design; equipment out for maintenance; load growth. | Plant capacity margin monitoring. | Facility water temperature rise; load shedding. | THM-01, THM-04 |
| FM-THM-011 | RF-THM-04 | M06 Failure to reset/recover | Chiller restart time after power loss longer than thermal ride-through. | Restart tests after power interruption. | Thermal excursion after short power disturbance. | THM-04, THM-06 |
| FM-THM-012 | RF-THM-04 | M02 Failure to start | Standby chiller or dry cooler fails to start on demand. | Rotation and start tests. | Loss of resilient capacity. | THM-04 |
| FM-THM-013 | RF-THM-04 | M07 Degraded output | Loss of make-up water for evaporative systems. | Water level and flow monitoring. | Capacity reduction in heatwave (X12). | THM-04, ENV-03 |
| FM-THM-014 | RF-THM-05 | M07 Degraded output | Containment leakage; recirculation; residual air load underestimated in liquid-cooled halls. | Inlet temperature mapping. | Overheating of air-cooled components (power supplies, network). | THM-02 |
| FM-THM-015 | RF-THM-05 | M01 Complete loss | CRAH/fan-wall loss through power or control failure. | Air-side monitoring. | Room temperature rise; network and storage equipment failure. | THM-02 |
| FM-THM-016 | RF-THM-06 | M25 Leakage/escape | QD seal failure; manifold crack; hose damage during maintenance. | Leak sensors; CDU level and make-up monitoring. | Fluid on electrical equipment; rack loss (X07). | THM-03, THM-05 |
| FM-THM-017 | RF-THM-06 | M19 Failure to alarm | Leak sensors absent at connection points; sensor cable damaged. | Periodic functional test. | Leak spreads undetected. | THM-05 |
| FM-THM-018 | RF-THM-06 | M05 Failure to isolate | Isolation valves manual or failed; make-up continues to feed leak. | Isolation tests. | Larger fluid release; adjacent damage. | THM-05 |
| FM-THM-019 | RF-THM-06 | M20 Nuisance alarm | Condensation or cleaning fluids triggering sensors. | Alarm statistics. | Operators desensitised; real leak ignored. | THM-05, OPS-04 |
| FM-THM-020 | RF-THM-07 | M07 Degraded output | Inhibitor depletion; biological growth; particulate; incompatible materials. | Chemistry sampling; filter differential pressure. | Fouling and corrosion; long-term capacity loss. | THM-05 |
| FM-THM-021 | RF-THM-07 | M28 Incompatibility | Mixed metals or elastomers incompatible with coolant; mixed coolant types after top-up. | Material compatibility review; sampling. | Corrosion; seal degradation; leaks. | THM-05, SUP-03 |
| FM-THM-022 | RF-THM-08 | M13 Unstable/oscillating | Competing control loops (CDU and chiller plant); poor tuning for fast AI load changes. | Trend analysis of temperatures and valve positions. | Temperature swings; equipment wear; throttling. | THM-06 |
| FM-THM-023 | RF-THM-08 | M09 Incorrect output | Wrong setpoint (error or manipulation); sensor drift. | Setpoint change detection; sensor cross-checks. | Gradual margin loss; throttling (X05). | THM-06, SEC-02 |
| FM-THM-024 | RF-THM-08 | M30 Loss of control / unauthorised control | Controller failure without defined fail-state; unauthorised command. | Controller health monitoring; command audit. | Plant in undefined state. | THM-06, SEC-02 |

## A.7 ENV

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-ENV-001 | RF-ENV-01 | M07 Degraded output | Gaseous contamination from external sources; construction dust. | Corrosion coupons; particulate monitoring. | Increased hardware failure rates. | ENV-01 |
| FM-ENV-002 | RF-ENV-01 | M08 Excess output | Humidity above dew point near cold surfaces (coolant below room dew point). | Dew-point monitoring versus coolant temperature. | Condensation on electronics. | ENV-01, THM-06 |
| FM-ENV-003 | RF-ENV-02 | M01 Complete loss | Utility supply interruption; drought restriction. | Supply flow and storage level. | Loss of evaporative heat rejection. | ENV-03, ENV-06 |
| FM-ENV-004 | RF-ENV-02 | M07 Degraded output | Supply quality change (hardness, chlorides). | Water quality testing. | Scaling; corrosion; treatment chemistry shift. | ENV-03, THM-05 |
| FM-ENV-005 | RF-ENV-03 | M09 Incorrect output | Meter error; boundary misallocation; double counting. | Meter reconciliation. | False reporting; wrong capacity or efficiency decisions. | ENV-02, ENV-04 |
| FM-ENV-006 | RF-ENV-04 | M25 Leakage/escape | Refrigerant leak; fuel spill; glycol release; suppressant discharge. | Leak detection; inventory reconciliation. | Occupational exposure; environmental release. | ENV-05 |

## A.8 CMP

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-CMP-001 | RF-CMP-01 | M01 Complete loss | Accelerator, memory, power-supply or board failure. | Node health checks; scheduler errors. | Synchronous job failure; restart from checkpoint. | CMP-05, CMP-06 |
| FM-CMP-002 | RF-CMP-01 | M07 Degraded output | Thermal throttling; power capping; degraded memory; link errors. | Performance baseline deviation. | Step-time increase for the whole job (slowest participant). | CMP-05 |
| FM-CMP-003 | RF-CMP-01 | M09 Incorrect output | Silent data corruption from hardware defect or firmware (X10). | SDC screening; cross-replica checks; training-health anomalies. | Corrupted model state and checkpoints. | CMP-05, CMP-04 |
| FM-CMP-004 | RF-CMP-01 | M23 Uncontrolled shutdown | Hardware thermal protection trip; power loss. | Event logs. | Job loss; possible hardware stress. | CMP-05, THM-03 |
| FM-CMP-005 | RF-CMP-02 | M01 Complete loss | Loss of a switch tray or link in a rack-scale domain; power shelf fault. | Domain health monitoring. | Entire scale-up domain unusable; large capacity loss. | CMP-02 |
| FM-CMP-006 | RF-CMP-02 | M12 Intermittent operation | Marginal links; connector issues; retraining. | Link error counters. | Repeated job aborts; hard-to-diagnose slowdowns. | CMP-02, NET-05 |
| FM-CMP-007 | RF-CMP-03 | M29 Misallocation | Placement ignores fault domains; replicas or critical services co-located. | Placement audit against fault-domain map. | Single facility failure takes out all replicas. | CMP-03, CMP-02 |
| FM-CMP-008 | RF-CMP-03 | M01 Complete loss | Scheduler control-plane failure; database corruption. | Control-plane health monitoring. | No new jobs; restart impossible. | CMP-03, SEC-02 |
| FM-CMP-009 | RF-CMP-03 | M15 Performance collapse | Contention; fragmentation; queue starvation. | Queue and utilisation metrics. | Committed capacity not delivered. | CMP-03 |
| FM-CMP-010 | RF-CMP-04 | M28 Incompatibility | GPU, NIC, BMC, driver and switch firmware combinations not qualified. | Compatibility matrix check; canary failures. | Failures or performance loss after change. | CMP-04 |
| FM-CMP-011 | RF-CMP-04 | M09 Incorrect output | Configuration drift from baseline. | Baseline compliance scans. | Inconsistent behaviour; hidden common mode. | CMP-01, CMP-04 |
| FM-CMP-012 | RF-CMP-04 | M06 Failure to reset/recover | Rollback package unavailable or untested. | Rollback test. | Extended degraded operation after bad release. | CMP-04 |
| FM-CMP-013 | RF-CMP-05 | M19 Failure to alarm | Telemetry gaps; thresholds too permissive. | Telemetry coverage audit. | Degraded nodes slow or corrupt jobs. | CMP-05 |
| FM-CMP-014 | RF-CMP-05 | M24 Spurious operation | False error signals; telemetry bugs; over-aggressive automation. | Drain statistics versus confirmed faults. | Mass drain; capacity loss (X18). | CMP-05, SEC-06 |
| FM-CMP-015 | RF-CMP-06 | M02 Failure to start | Image repository, PXE, DHCP or identity unavailable. | Provisioning failure rates. | Nodes cannot return after mass reboot. | CMP-06, NET-06 |
| FM-CMP-016 | RF-CMP-06 | M16 Data/configuration corruption | Defective or tampered golden image. | Image signing and validation; canary boot. | Fleet-wide defect introduced during recovery. | CMP-06, SUP-04 |

## A.9 STO

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-STO-001 | RF-STO-01 | M15 Performance collapse | Metadata hotspot; small-file access pattern; noisy neighbour. | Latency and metadata operation metrics. | Accelerators idle waiting for data. | STO-02 |
| FM-STO-002 | RF-STO-01 | M01 Complete loss | Storage cluster failure; network partition; controller failure. | Storage health monitoring. | Training halt; inference model load failure. | STO-01, STO-02 |
| FM-STO-003 | RF-STO-02 | M10 Delayed output | Write bandwidth below checkpoint demand; drain from node-local tier too slow. | Checkpoint duration metrics. | Checkpoint window exceeded; larger progress loss. | STO-02, STO-05 |
| FM-STO-004 | RF-STO-02 | M16 Data/configuration corruption | Partial writes; failure mid-checkpoint; no completion marker. | Checkpoint verification. | Unusable checkpoint; fallback to older one. | STO-05, STO-03 |
| FM-STO-005 | RF-STO-02 | M14 Capacity exhaustion | Retention policy filling tier. | Capacity alarms; forecast. | Writes fail; recent checkpoints missing (X04). | STO-06, STO-02 |
| FM-STO-006 | RF-STO-03 | M10 Delayed output | Concurrent restore storm; metadata limits. | Restore time metrics; tests at scale. | Recovery beyond tolerance (X04). | STO-05, RES-04 |
| FM-STO-007 | RF-STO-03 | M28 Incompatibility | Checkpoint format incompatible after software change. | Restore validation tests. | Unable to resume; re-training required. | STO-05, CMP-04 |
| FM-STO-008 | RF-STO-04 | M16 Data/configuration corruption | Silent media errors; software defects; split-brain metadata. | Checksums; scrubbing; consistency checks. | Corrupted training data or checkpoints propagated to replicas. | STO-03 |
| FM-STO-009 | RF-STO-04 | M27 Loss of synchronisation | Replica divergence; time skew affecting leases. | Replica consistency monitoring. | Inconsistent reads; metadata corruption. | STO-03, NET-06 |
| FM-STO-010 | RF-STO-05 | M05 Failure to isolate | Backups and replicas share credentials, controllers or site with primary. | Protection architecture review. | Single compromise or failure destroys all copies. | STO-04 |
| FM-STO-011 | RF-STO-05 | M10 Delayed output | Replication lag; WAN constraint. | Lag monitoring. | Recovery point older than tolerance. | STO-04, NET-03 |
| FM-STO-012 | RF-STO-05 | M01 Complete loss | Deletion or encryption by attacker or error; immutability not enforced. | Immutability configuration audit; deletion alerts. | No recovery copy. | STO-04, SEC-05 |

## A.10 NET

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-NET-001 | RF-NET-01 | M15 Performance collapse | Incast; congestion-control mistuning; oversubscription. | Collective bandwidth benchmarks; ECN and queue telemetry. | Step-time increase cluster-wide. | NET-02 |
| FM-NET-002 | RF-NET-01 | M26 Congestion/blockage | PFC storm or deadlock (X03). | Pause counters; PFC watchdog events. | Cluster-wide collective stall. | NET-02, NET-01 |
| FM-NET-003 | RF-NET-01 | M12 Intermittent operation | Link flaps from optics or cabling. | Link event logs; error counters. | Repeated job aborts. | NET-05, NET-02 |
| FM-NET-004 | RF-NET-01 | M01 Complete loss | Spine or plane failure; power loss to fabric switches. | Fabric monitoring. | Cluster partition; job failures. | NET-01 |
| FM-NET-005 | RF-NET-02 | M04 Failure to transfer | ECMP polarisation; slow reconvergence; insufficient path diversity. | Failure tests; flow distribution analysis. | Hot spots and loss after link failure. | NET-01 |
| FM-NET-006 | RF-NET-02 | M05 Failure to isolate | Fleet-wide configuration push; controller defect. | Change blast-radius review. | Fabric-wide outage from one change. | NET-06, OPS-05 |
| FM-NET-007 | RF-NET-03 | M05 Failure to isolate | Storage and compute traffic in same class; tenant isolation errors. | QoS audit; isolation tests. | Interference; checkpoint stalls; isolation breach. | NET-03 |
| FM-NET-008 | RF-NET-03 | M01 Complete loss | Carrier or WAN failure; shared route (X09). | WAN monitoring. | Inference ingress and replication loss. | NET-03, DEP-03 |
| FM-NET-009 | RF-NET-04 | M01 Complete loss | OOB shares switches, power or route with in-band. | OOB test with in-band down. | No remote access during incidents. | NET-04 |
| FM-NET-010 | RF-NET-04 | M30 Loss of control / unauthorised control | Console servers exposed; weak authentication. | Access review; penetration testing. | Attacker control of infrastructure consoles. | NET-04, SEC-03 |
| FM-NET-011 | RF-NET-05 | M09 Incorrect output | Time step from wrong grandmaster; DNS misconfiguration. | Offset monitoring; DNS validation. | Authentication failures; service errors (X13). | NET-06 |
| FM-NET-012 | RF-NET-05 | M01 Complete loss | DHCP, DNS or IPAM outage. | Service monitoring. | Provisioning and recovery blocked. | NET-06, RES-04 |
| FM-NET-013 | RF-NET-06 | M07 Degraded output | Dirty connectors; optic ageing; bend radius. | Bit error rate and optical power monitoring. | Retransmissions; performance loss. | NET-05 |
| FM-NET-014 | RF-NET-06 | M09 Incorrect output | Miscabling; incorrect cross-connect. | Topology validation (LLDP against plan). | Wrong topology; performance and isolation issues. | NET-05 |

## A.11 OPS

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-OPS-001 | RF-OPS-01 | M20 Nuisance alarm | Unrationalised alarms; flood during events. | Alarm rate statistics. | Root alarm missed; wrong response (X16). | OPS-04 |
| FM-OPS-002 | RF-OPS-01 | M10 Delayed output | Insufficient staffing; unclear escalation; remote-only operations. | Response time metrics. | Consequence reaches outcome before action. | OPS-01, OPS-04 |
| FM-OPS-003 | RF-OPS-01 | M09 Incorrect output | Generic procedures; inaccurate HMI; lack of practice. | Exercise performance. | Wrong action worsens event. | OPS-02, OPS-01 |
| FM-OPS-004 | RF-OPS-02 | M05 Failure to isolate | Incomplete isolation; stored energy not discharged. | Isolation verification. | Injury; arc flash; uncontrolled fluid release. | OPS-02 |
| FM-OPS-005 | RF-OPS-02 | M29 Misallocation | Wrong asset isolated (labelling, drawings). | Two-person verification. | Outage of live path during maintenance. | OPS-02, EVA-02 |
| FM-OPS-006 | RF-OPS-03 | M09 Incorrect output | Change not impact-assessed; wrong implementation. | Change review; post-change validation. | Outage or latent defect. | OPS-05 |
| FM-OPS-007 | RF-OPS-03 | M22 Bypass left active | Temporary configuration not removed. | Temporary-configuration register. | Persistent impairment. | OPS-05 |
| FM-OPS-008 | RF-OPS-04 | M21 Latent standby failure | Deferred maintenance; missed tests. | Maintenance backlog metrics. | Standby fails on demand. | OPS-03 |
| FM-OPS-009 | RF-OPS-04 | M24 Spurious operation | Maintenance-induced trips; incorrect procedure. | Incident records. | Unplanned outage during work. | OPS-03, OPS-02 |
| FM-OPS-010 | RF-OPS-05 | M17 Loss of visibility | Handover omissions during evolving event. | Handover records review. | Next shift unaware of degraded state. | OPS-01 |
| FM-OPS-011 | RF-OPS-05 | M07 Degraded output | Competence gaps for rare operations; knowledge concentration in one person. | Competence records; exercises. | Unsafe or slow response. | OPS-01, DEP-04 |

## A.12 RES

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-RES-001 | RF-RES-01 | M05 Failure to isolate | Fault domains defined on paper only; shared dependencies across domains. | Isolation validation tests. | Local failure becomes site-wide. | RES-02 |
| FM-RES-002 | RF-RES-02 | M03 Failure to stop | Lower-priority load not shed on capacity loss. | Exercise of shedding. | Total loss rather than graceful degradation. | RES-01 |
| FM-RES-003 | RF-RES-02 | M29 Misallocation | Wrong workloads shed; priorities outdated. | Priority review. | Critical outcomes lost while others continue. | RES-01, RES-06 |
| FM-RES-004 | RF-RES-03 | M09 Incorrect output | Wrong restart sequence (cooling after IT; control plane last). | Recovery exercises. | Secondary failures during recovery. | RES-04 |
| FM-RES-005 | RF-RES-03 | M14 Capacity exhaustion | Restart inrush and restart storms. | Recovery tests with measurement. | Protection trips during recovery. | RES-04, POW-06 |
| FM-RES-006 | RF-RES-04 | M16 Data/configuration corruption | Restoring defective configuration or image (X14). | Validation of restored state. | Recurrence of failure. | RES-04 |
| FM-RES-007 | RF-RES-04 | M10 Delayed output | Missing recovery-only dependencies; manual steps. | Recovery time measurement. | Recovery beyond tolerance. | RES-04, RES-05 |
| FM-RES-008 | RF-RES-05 | M02 Failure to start | Alternate capacity not available, not compatible or not authorised. | Invocation test. | No continuity option. | RES-03 |

## A.13 SUP

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-SUP-001 | RF-SUP-01 | M09 Incorrect output | Authentic but defective release (X02, X10). | Canary testing; field monitoring. | Fleet-wide failure or corruption. | SUP-04 |
| FM-SUP-002 | RF-SUP-01 | M16 Data/configuration corruption | Tampered release; compromised build or update channel. | Signature and provenance validation. | Malicious code in infrastructure. | SUP-04, SEC-04 |
| FM-SUP-003 | RF-SUP-02 | M10 Delayed output | Long lead times for transformers, switchgear, CDUs, chillers, accelerators. | Lead-time tracking; spares register. | Extended DEGRADED operation. | SUP-05 |
| FM-SUP-004 | RF-SUP-02 | M28 Incompatibility | Spares of wrong revision or firmware. | Spares validation. | Spare cannot be used. | SUP-05, SUP-03 |
| FM-SUP-005 | RF-SUP-03 | M01 Complete loss | Vendor insolvency, sanctions, end of support. | Supplier monitoring. | No diagnosis or repair path. | SUP-01, SUP-02 |
| FM-SUP-006 | RF-SUP-03 | M10 Delayed output | Support response slower than recovery tolerance. | SLA monitoring. | Recovery beyond tolerance. | SUP-02 |
| FM-SUP-007 | RF-SUP-04 | M09 Incorrect output | Counterfeit or substandard components. | Provenance checks; inspection. | Premature failure; hidden modification. | SUP-03 |

## A.14 SEC

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-SEC-001 | RF-SEC-01 | M01 Complete loss | Identity provider or MFA outage (X15). | Authentication monitoring. | Operators locked out during incidents. | SEC-01 |
| FM-SEC-002 | RF-SEC-01 | M30 Loss of control / unauthorised control | Stolen or shared credentials; vendor accounts not revoked. | Access anomaly detection; account reviews. | Unauthorised infrastructure control (X05). | SEC-01, SUP-06 |
| FM-SEC-003 | RF-SEC-01 | M08 Excess output | Excessive privileges; standing admin rights. | Privilege reviews. | Large blast radius of compromise or error. | SEC-01 |
| FM-SEC-004 | RF-SEC-02 | M05 Failure to isolate | Flat networks; undocumented conduits; dual-homed hosts. | Segmentation testing. | Compromise spreads from IT to OT. | SEC-03 |
| FM-SEC-005 | RF-SEC-03 | M08 Excess output | Automation without rate or blast-radius limits (X18). | Action logs; policy audit. | Mass action affecting large capacity. | SEC-06 |
| FM-SEC-006 | RF-SEC-03 | M30 Loss of control / unauthorised control | Agent or automation issues commands outside allowlist. | Command allowlist enforcement logs. | Unsafe infrastructure commands. | SEC-06 |
| FM-SEC-007 | RF-SEC-04 | M19 Failure to alarm | No OT monitoring; logs not collected. | Detection coverage review. | Prolonged undetected manipulation. | SEC-05 |
| FM-SEC-008 | RF-SEC-04 | M24 Spurious operation | Containment action cuts control or monitoring paths. | Response playbook review; exercises. | Loss of control during response. | SEC-05 |
| FM-SEC-009 | RF-SEC-05 | M16 Data/configuration corruption | Unauthorised logic change in PLC or protection relay. | Logic integrity checks; change detection. | Protection disabled; unsafe operation. | SEC-02, SEC-04 |

## A.15 EVA

| **ID** | **Function** | **Mode** | **Typical causes** | **Detection** | **Effect on outcome** | **Families** |
|--------|--------------|----------|--------------------|---------------|-----------------------|--------------|
| FM-EVA-001 | RF-EVA-01 | M01 Complete loss | Telemetry retention shorter than investigation needs; logging disabled. | Retention audit. | Events cannot be reconstructed. | EVA-01 |
| FM-EVA-002 | RF-EVA-01 | M16 Data/configuration corruption | Logs altered on compromised systems; no integrity protection. | Integrity verification. | Evidence untrustworthy (U7). | EVA-02 |
| FM-EVA-003 | RF-EVA-01 | M27 Loss of synchronisation | Time skew across sources. | Time-offset checks. | Incorrect causal sequence. | EVA-02, NET-06 |
| FM-EVA-004 | RF-EVA-02 | M09 Incorrect output | As-built drift undetected; drawings not updated. | Periodic reconciliation. | Analyses based on wrong architecture. | EVA-02, CAP-06 |
| FM-EVA-005 | RF-EVA-03 | M18 False indication | UNKNOWN closed by assumption; omitted from reports. | Assurance review; UNKNOWN register audit. | Overstated assurance decision. | EVA-04 |

# Appendix B - Working templates

**Scenario statement template.** In [operating state], [threat/hazard/initiating event] causes [failure mode code] in [Required Function / entity]. The effect propagates via [dependency/fault-domain conduit] to [next entity], and affects [Service Outcome] beyond/within [tolerance]. [Credited safeguard] is expected to [prevent/contain/limit/recover] at step [n]. Evidence [supports/challenges/is insufficient for] that expectation at claim type [claim type]. Residual state is [state], with confidence [CONF level] and UNKNOWN Records [IDs, type, severity].

**Path step template.**

| **Step** | **Domain** | **Entity / Required Function** | **Pre-state** | **Failure mode (code)** | **Operator and qualifiers** | **Dependency / fault-domain edge** | **Effect** | **Safeguard (position)** | **Post-state** | **Evidence / UNKNOWN** |
|----------|------------|--------------------------------|---------------|-------------------------|-----------------------------|------------------------------------|------------|--------------------------|----------------|------------------------|
| 1 | | | | | | | | | | |
| 2 | | | | | | | | | | |
| 3 | | | | | | | | | | |
| 4 | | | | | | | | | | |
| 5 | | | | | | | | | | |
| 6 | | | | | | | | | | |

**FMEA row template.**

| **Required Function** | **Mode (code)** | **Cause** | **Local effect** | **End effect (Service Outcome)** | **Detection** | **Safeguards** | **Controls** | **Evidence** | **Severity band** | **Likelihood class** | **Action** |
|-----------------------|-----------------|-----------|------------------|----------------------------------|---------------|----------------|--------------|--------------|-------------------|----------------------|------------|
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |

# Appendix C - References

| **Reference** | **Use** |
|---------------|---------|
| AIDCF-001 AIDCF Manifesto | Doctrine, evidence, UNKNOWN and critical-gate principles. |
| AIDCF-002 Core Conceptual Model | Canonical assurance chain, concept definitions and assurance-case decomposition. |
| AIDCF-003 Infrastructure Ontology and Taxonomy | Entities, dependencies, operating states, capacity and fault domains. |
| AIDCF-006 Assurance Principles Standard | Assurance principles applied to scenario-based claims. |
| AIDCF-007A Canonical Master Control Registry | Controls and families linked to safeguards. |
| AIDCF-008 Evidence Model | Evidence classes, quality, sufficiency, UNKNOWN types U1–U10. |
| AIDCF-010 Scoring and Decision Framework | Gate criteria, roll-up and decision ceilings. |
| AIDCF-013 AI Data Centre Assurance Reference Architecture | Reference service chains, failure-path and safeguard models. |
| AIDCF-014 End-to-End Traceability and Machine-Executable Data Standard | FailureScenario and Safeguard profiles; relationship vocabulary. |
| ISO/IEC/IEEE 15026-2 | Assurance-case structure. |
| IEC 31010:2019 | Selection and application of risk-assessment techniques. |
| IEC 60812:2018 | FMEA and FMECA. |
| IEC 61025:2006 | Fault tree analysis. |
| IEC 62502:2010 | Event tree analysis. |
| IEC 61882:2016 | Hazard and operability studies. |
| IEC 61078:2016 | Reliability block diagrams. |
| IEC 61165:2006 | Application of Markov techniques. |
| IEC 62740:2015 | Root cause analysis. |
| IEC 61508 (series), Part 6 | Functional safety; common-cause estimation guidance. |
| IEC 61511 (series) | Safety-instrumented systems for the process sector (LOPA context). |
| NUREG/CR-5485 | Guidance on modelling common-cause failures. |
| CCPS Layer of Protection Analysis guidance | LOPA method. |
| STPA Handbook (Leveson and Thomas, 2018) | System-theoretic process analysis. |
| IEC 62443-3-2:2020 | Security risk assessment for system design (zones and conduits). |
| NIST SP 800-82 Rev. 3 | Operational technology security guidance. |
| NIST SP 800-30 Rev. 1 | Threat-oriented risk-assessment comparison. |
| MITRE ATT&CK for ICS | Adversary technique knowledge base for attack trees. |
| IEC 62040-3 | UPS performance and test methods. |
| ISO 8528-5 | Generating-set transient performance. |
| IEEE 1584 | Arc-flash incident energy calculation. |
| IEC 61000-4-30 | Power-quality measurement methods. |
| IEEE 1588 | Precision time protocol. |
| IEEE 802.1Qbb | Priority-based flow control. |
| UL 9540A | Test method for thermal runaway fire propagation in battery energy storage systems. |
| NFPA 855 | Installation of stationary energy storage systems. |
| ASHRAE TC 9.9 guidance | Data-centre thermal and equipment-environment context, including liquid-cooling guidance. |

# Appendix D - Review and change record

| **Review role** | **Status** | **Review focus** |
|-----------------|------------|------------------|
| Methodology author | Draft completed | Coherence with AIDCF-002 chain, Part XII UNKNOWN rules and AIDCF-014 mapping. |
| Reliability/FMEA | Pending | Appendix A mode applicability; technique selection and limitations in Part X. |
| Data-centre architecture | Pending | Credibility of X01–X20 propagation paths and fault-domain assumptions. |
| Electrical | Pending | X01, X06, X11, X16, X17 and POW rows of Appendix A; transient and protection statements. |
| Mechanical/liquid cooling | Pending | X02, X07, X08, X12 and THM rows; TCS ride-through and fluid-quality treatment. |
| Fire/life safety | Pending | X06, X17; CG-04 linkage; battery and suppression statements. |
| Physical security | Pending | PHY scenario families and threat taxonomy. |
| AI compute/HPC | Pending | X03, X04, X10, X18 and CMP rows; synchronous-workload statements. |
| Storage | Pending | X04 and STO rows; checkpoint and restore treatment. |
| Network/fabric | Pending | X03, X09, X13 and NET rows; PFC and time-service statements. |
| OT security | Pending | X05, X15, X18; T18 and T19; CG-15 linkage. |
| Operations/recovery | Pending | X11, X14, X16, X20; OPS and RES rows. |
| Ontology/graph | Pending | Part VIII operator semantics and Part XVI mappings to AIDCF-014. |
| Legal/IP | Pending | Reference citations at document level; no reproduction of standard text. |
| Public release | Not approved | Release gates closed. |

# Appendix E - Legacy mapping (v1.0 → v1.1)

## E.1 Requirement identifiers

v1.0 requirement identifiers were not consecutive (THF-REQ-010 was followed by THF-REQ-018). v1.1 renumbers all requirements consecutively in document order. v1.0 identifiers THF-REQ-001 to THF-REQ-010 keep their numbers.

| **v1.1 ID** | **v1.0 ID** | **Subject** |
|-------------|-------------|-------------|
| THF-REQ-001 | THF-REQ-001 | Every material scenario shall identify the Capability Instance and the Service Outcomes (with tolerances) … |
| THF-REQ-002 | THF-REQ-002 | Threat, hazard, initiating event, cause, failure mode, effect and consequence shall be recorded as … |
| THF-REQ-003 | THF-REQ-003 | Each scenario shall declare the assessment boundary, architecture baseline, initial operating state, the … |
| THF-REQ-004 | THF-REQ-004 | Propagation shall be expressed through explicit dependency and fault-domain records conforming to … |
| THF-REQ-005 | THF-REQ-005 | The existence of a safeguard shall not be treated as evidence of its effectiveness; effectiveness requires … |
| THF-REQ-006 | THF-REQ-006 | Any material unverified path element shall be represented as an UNKNOWN Record with a type (U1–U10) and … |
| THF-REQ-007 | THF-REQ-007 | Analysis of life-safety, hazardous-energy and safety-instrumented functions shall be performed or approved … |
| THF-REQ-008 | THF-REQ-008 | Validation of safeguards shall be proportionate, authorised and safe, and shall follow the safe validation … |
| THF-REQ-009 | THF-REQ-009 | Excluded, external and cross-boundary dependencies shall remain visible in scenarios that traverse them, … |
| THF-REQ-010 | THF-REQ-010 | Average scores shall not override critical gates or consequence severity CS4–CS5 outcomes |
| THF-REQ-011 | — (new in v1.1) | Cross-references to other AIDCF artifacts shall use public artifact identifiers (AIDCF-NNN); domain … |
| THF-REQ-012 | — (new in v1.1) | Each scenario shall record its initial operating state and every operating state it enters, including the … |
| THF-REQ-013 | — (new in v1.1) | A safeguard shall be credited only for the operating states in which its behaviour is evidenced; claims … |
| THF-REQ-014 | THF-REQ-018 | Analysis shall not terminate at "human error"; systemic contributors (procedure, interface, alarm load, … |
| THF-REQ-015 | THF-REQ-019 | Causal decomposition shall stop only where further analysis would not change treatment, accountability, … |
| THF-REQ-016 | THF-REQ-020 | Alternate causal hypotheses and excluded causes shall be recorded with the basis for exclusion |
| THF-REQ-017 | THF-REQ-021 | Where cause is UNKNOWN, the observed facts, timeline and failure mode shall be preserved unchanged |
| THF-REQ-018 | — (new in v1.1) | Each scenario step shall carry exactly one primary operator from Table 15.1 and may carry qualifiers from … |
| THF-REQ-019 | — (new in v1.1) | Where a step's operator depends on a structural relationship (dependency, shared fault domain, protection, … |
| THF-REQ-020 | — (new in v1.1) | Each capability consequence shall state the consequence family, the affected Service Outcome, the impact … |
| THF-REQ-021 | — (new in v1.1) | A safeguard credited with interrupting a decisive path (Part XII) shall be linked to at least one … |
| THF-REQ-022 | — (new in v1.1) | A safeguard that shares a dependency with the path it is credited to interrupt shall not be credited for … |
| THF-REQ-023 | — (new in v1.1) | Validation at V5–V7 involving hazardous energy, pressurised fluids, fire systems, batteries or production … |
| THF-REQ-024 | — (new in v1.1) | Where a safeguard cannot be validated above V3 without unacceptable risk, the residual limitation shall be … |
| THF-REQ-025 | — (new in v1.1) | The analysis plan for a Capability Instance shall record which techniques were applied to which Service … |
| THF-REQ-026 | — (new in v1.1) | Outputs of any technique that are used to support a claim shall be recorded as AIDCF-008 E7 (derived and … |
| THF-REQ-027 | THF-REQ-022 | Consequence severity, likelihood, detectability and confidence shall be recorded as separate attributes |
| THF-REQ-028 | THF-REQ-023 | A risk priority number or other arithmetic product shall not by itself determine a control result, gate … |
| THF-REQ-029 | THF-REQ-024 | Critical gates and CS4–CS5 consequences shall not be averaged away by scores |
| THF-REQ-030 | THF-REQ-025 | Quantitative probability shall be used only where data, model and assumptions are defensible and recorded … |
| THF-REQ-031 | — (new in v1.1) | Class A fields of a submitted scenario shall not be UNKNOWN; where the capability framing is itself … |
| THF-REQ-032 | — (new in v1.1) | Every UNKNOWN in a class B, C or D field shall be recorded as an UNKNOWN Record that states subject, … |
| THF-REQ-033 | — (new in v1.1) | A failure cause may remain UNKNOWN only where the credited safeguard acts independently of the cause and … |
| THF-REQ-034 | — (new in v1.1) | A decisive path shall be resolved before it is cited in support of a positive claim |
| THF-REQ-035 | — (new in v1.1) | Elements of the downstream segment of a decisive path may remain UNKNOWN only if the credited safeguard's … |
| THF-REQ-036 | — (new in v1.1) | Where more than one safeguard is credited in series on a decisive path, the path shall be resolved up to … |
| THF-REQ-037 | — (new in v1.1) | A scenario whose decisive path is unresolved shall be reported with its UNKNOWN Records and shall not be … |
| THF-REQ-038 | — (new in v1.1) | Each scenario UNKNOWN shall be assigned severity by applying the tests in §25 top-down; an UNKNOWN shall … |
| THF-REQ-039 | — (new in v1.1) | A US4 or US5 scenario UNKNOWN shall be presented to CG-12 with one of the following dispositions recorded: … |
| THF-REQ-040 | — (new in v1.1) | The analysis plan shall record, for each scenario family below, whether it was analysed, screened out with … |
| THF-REQ-041 | — (new in v1.1) | For each in-scope Capability Instance, every library scenario shall be instantiated, screened out with … |
| THF-REQ-042 | — (new in v1.1) | An instantiated library scenario shall replace the reference path with the site's actual entities, … |
| THF-REQ-043 | — (new in v1.1) | Each THF finding shall reference the scenario, the step or safeguard concerned, the gate engaged and the … |
| THF-REQ-044 | — (new in v1.1) | Instantiated scenarios that reveal exploitable attack paths, physical routes or protection weaknesses … |

v1.0 identifiers THF-REQ-011 to THF-REQ-017 were never issued. Because v1.1 numbers THF-REQ-014 to THF-REQ-030 carry different requirements from v1.0 requirements with the same numbers, any citation of a v1.0 requirement shall state the version (for example "THF-REQ-018 (v1.0)") and should be migrated using this table.

## E.2 Domain catalogue

| **v1.0 domain** | **v1.0 scenario families** | **v1.1 location** |
|-----------------|----------------------------|-------------------|
| D1 Physical | Unauthorised entry; insider sabotage; surveillance blind spot; asset removal; security-zone collapse; emergency-access conflict | PHY (§30) |
| D2 Facilities Engineering | Structural overload; fire-system mismatch; water ingress | PHY (§30) |
| D2 Facilities Engineering | Common controller defect | THM shared control failure (§32); SEC (§40) |
| D2 Facilities Engineering | As-built divergence; commissioning omission | EVA (§41) |
| D3 Power & Cooling | Utility loss; generator no-start; UPS loss; protection miscoordination; rack overload | POW (§31) |
| D3 Power & Cooling | Cooling capacity loss; CDU failure; thermal transient; liquid leak; shared control failure | THM (§32) |
| D4 Environmental & Resource | Ambient exceedance; water scarcity; air contamination; refrigerant loss; efficiency-resilience conflict; metering/claim error | ENV (§33) |
| D4 Environmental & Resource | Poor coolant quality | THM (§32) |
| D5 Operations | Maintenance-induced outage; procedure failure; competence gap; change failure; alarm-response failure; handover failure | OPS (§37) |
| D5 Operations | Spares/obsolescence; supplier support loss | SUP (§39) |
| D6 Compute | All eight families | CMP (§34) |
| D7 Storage | All eight families | STO (§35) |
| D8 Network | All eight families | NET (§36) |
| — | (no v1.0 equivalent) | GOV, CAP, DEP, RES, SEC families added |

## E.3 Renamed designations and vocabulary

| **v1.0** | **v1.1** | **Reason** |
|----------|----------|------------|
| Artifact ID AIDCF-THF-001 | AIDCF-004 (requirement short code THF) | Public identifier scheme. |
| Severity bands S0–S5 | Consequence severity bands CS0–CS5 (same meanings) | S0–S5 denotes evidence sufficiency in AIDCF-008. |
| Conformance levels F0–F4 | THF-C0 to THF-C4 | F denotes the fitness quality dimension in AIDCF-008. |
| "Canonical chain" (Context → … → Assurance Decision) | Scenario anatomy within chain step 7; the only chain is the AIDCF-002 sixteen-step chain | Single canonical chain. |
| Eight domains D1–D8 | Fifteen domains | Domain model. |
| Evidence classes (Architecture, As-built, …) | Evidence sources mapped to E1–E7 | AIDCF-008 classes are canonical. |
| Local node and relationship types | AIDCF-014 classes and the 41 canonical relationships; THF operators as step attributes | Single data model. |
| Failure modes without codes | M00–M30 | Machine-readable catalogue; M24 and M30 added. |
| Appendix A: 32 functions × 8 generic modes (FM-0001 to FM-0256) | Appendix A: function-specific catalogue (FM-<DOM>-NNN) | Generic cross-product removed; v1.0 FM-nnnn identifiers are withdrawn and have no one-to-one successor. |
| "Required, or explicit UNKNOWN where permitted" | Field classes A–D with explicit permission rules (Part XII) | Defines where UNKNOWN is permitted. |

## E.4 Cross-domain scenario library

| **v1.0** | **v1.1** |
|----------|----------|
| X01 Utility loss + generator no-start + UPS autonomy exhaustion | X01 (load-acceptance variant) and X20 (extended outage, fuel) |
| X02 Cooling loss at sustained AI load | X02, X12 |
| X03 Liquid leak with detection gap | X07 |
| X04 Maintenance removes hidden shared dependency | X11 |
| X05 BMS/EPMS compromise or malfunction | X05 |
| X06 Fabric congestion during checkpoint demand | X03, X04 |
| X07 Storage metadata failure during training | X04 (metadata hotspot); STO scenario family |
| X08 Firmware rollout common-mode failure | X10, X02 |
| X09 Fire disables paired infrastructure routes | X17 |
| X10 Extreme ambient plus water restriction | X12 |
| X11 Operator error during alarm flood | X16 |
| X12 Long-lead spare after rare failure | X06 (recovery), SUP scenario family |
| X13 Time-source divergence | X13 |
| X14 Colocation responsibility gap | X19 |
| X15 Recovery reintroduces corrupt configuration | X14 |
| X16 Physical intrusion disrupts interconnect | PHY scenario family (unauthorised entry) and X09 (route) |
| X17 Expansion creates stranded compute | X19; CAP scenario family |
| X18 Loss of remote OEM support | X02 (recovery), SUP scenario family |
| X19 Shared authentication service failure | X15 |
| X20 Compound flood/fire/grid/telecom event | X20 |

## Final doctrine

Do not ask only whether a control exists or a component is redundant. Ask what the capability requires, what can disturb the required conditions, how functions can fail, where effects propagate, which barriers remain available in the applicable state, what evidence demonstrates their behaviour, what consequence remains, how recovery is achieved and what is still UNKNOWN — and do not let an unresolved decisive path support a positive claim.
