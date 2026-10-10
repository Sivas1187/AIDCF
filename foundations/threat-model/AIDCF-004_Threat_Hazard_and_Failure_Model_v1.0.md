> Markdown edition (source of truth). PDF: [AIDCF-004_Threat_Hazard_and_Failure_Model_v1.0.pdf](AIDCF-004_Threat_Hazard_and_Failure_Model_v1.0.pdf)

Capability-first adverse-condition, failure-propagation and resilience analysis

Artifact ID: AIDCF-THF-001  
Normative foundation standard  
Draft for controlled review  
Author: Siva Sethumadhavan  
Release 1: Foundational Methodology

Identify credible adversity. Separate cause from failure. Trace propagation. Validate safeguards safely. Preserve UNKNOWN.

# Document control

| **Field**       | **Value**                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| Title           | AIDCF Threat, Hazard & Failure Model v1.0                                                                                 |
| Artifact ID     | AIDCF-THF-001                                                                                                             |
| Status          | Draft for controlled review                                                                                               |
| Depends on      | AIDCF Manifesto v1.0; Core Conceptual Model v1.0; Infrastructure Ontology & Taxonomy v1.0                                 |
| Purpose         | Define threats, hazards, causes, failure modes, propagation, consequence, safeguards, residual exposure and recovery.     |
| Users           | Owners, operators, engineers, assessors, AI infrastructure teams, security, resilience, risk and assurance practitioners. |
| Safety boundary | Does not replace licensed engineering or authorise destructive, hazardous or operationally disruptive testing.            |

# Executive thesis

AIDCF determines whether credible adverse conditions can defeat required infrastructure functions, propagate through dependencies and fault domains, overcome safeguards, and prevent a Capability Instance from achieving its Service Outcomes. Component failure is not the endpoint. Capability consequence, residual state, recovery and evidence are.

## Canonical chain

Context -\> Threat / Hazard / Degradation -\> Initiating Event -\> Failure Cause -\> Failure Mode -\> Local Effect -\> Dependency Effect -\> Propagated Failure -\> Capability Consequence -\> Safeguard Response -\> Residual State -\> Recovery -\> Assurance Decision

# Contents

1\. Authority, scope and conformance

2\. Core ontology and distinctions

3\. Scenario and propagation architecture

4\. Threat taxonomy

5\. Hazard taxonomy

6\. Failure-cause taxonomy

7\. Failure-mode taxonomy

8\. Effects and consequences

9\. Safeguards and resilience

10\. Analysis techniques

11\. Criticality and uncertainty

12\. Eight-domain failure catalogue

13\. Cross-domain scenario library

14\. Assessment records and evidence

15\. Machine-readable model

16\. Governance and acceptance

17\. Appendices

# Part I - Authority, scope and conformance

## 1. Purpose

This standard provides a controlled, vendor-neutral method for identifying, representing, analysing and recording adverse conditions affecting AI data-centre capabilities across the eight AIDCF domains.

## 2. Normative requirements

**THF-REQ-001** Every material scenario shall identify a Capability Instance and Service Outcome.

**THF-REQ-002** Threat, hazard, initiating event, cause, failure mode, effect and consequence shall remain distinct.

**THF-REQ-003** Each scenario shall declare boundary, architecture baseline, operating state and operating envelope.

**THF-REQ-004** Propagation shall use explicit dependencies and fault domains from AIDCF-003.

**THF-REQ-005** Safeguard existence shall not imply effectiveness without applicable evidence.

**THF-REQ-006** UNKNOWN shall remain visible for any material unverified path element.

**THF-REQ-007** Critical safety analysis shall be performed or approved by competent authorised professionals.

**THF-REQ-008** Testing shall be proportionate, authorised and safe.

**THF-REQ-009** Excluded and external dependencies shall remain visible.

**THF-REQ-010** Average scores shall not override critical gates or catastrophic consequences.

## 3. Conformance levels

| **Level** | **Name**            | **Expectation**                                    |
|-----------|---------------------|----------------------------------------------------|
| F0        | Vocabulary aligned  | Uses canonical meanings.                           |
| F1        | Scenario structured | Records event, mode, effects and consequence.      |
| F2        | Dependency traced   | Maps path, fault domains and states.               |
| F3        | Evidence gated      | Links safeguards, tests, confidence and UNKNOWN.   |
| F4        | Machine actionable  | Uses controlled identifiers and validation shapes. |

# Part II - Core ontology and distinctions

| **Term**               | **Canonical definition**                                                                                         |
|------------------------|------------------------------------------------------------------------------------------------------------------|
| Threat                 | Deliberate actor, capability, intent or circumstance capable of adverse infrastructure consequence.              |
| Hazard                 | Non-deliberate source, condition or event with potential for injury, damage, disruption or environmental impact. |
| Degradation mechanism  | Process progressively reducing condition, margin or performance.                                                 |
| Initiating event       | Event or condition starting a specific scenario.                                                                 |
| Failure cause          | Circumstance or mechanism producing or contributing to a failure mode.                                           |
| Failure mode           | Manner in which a required function is lost, degraded, delayed, incorrect, intermittent or uncontrolled.         |
| Local effect           | Immediate result at the failed item or function.                                                                 |
| Next-level effect      | Effect on containing subsystem or dependent function.                                                            |
| End effect             | Effect on Capability Instance or Service Outcome.                                                                |
| Propagation path       | Ordered sequence through which effects move across entities and dependencies.                                    |
| Consequence            | Realised or foreseeable effect on capability and stakeholders.                                                   |
| Predisposing condition | Condition increasing susceptibility without necessarily initiating failure.                                      |
| Safeguard              | Measure intended to anticipate, prevent, detect, contain, respond, recover or adapt.                             |
| Barrier                | Safeguard positioned on a defined path.                                                                          |
| Residual condition     | State remaining after expected safeguards act.                                                                   |
| Recovery path          | Sequence restoring an approved service and infrastructure state.                                                 |
| Latent failure         | Failure not detected until another event, demand or test.                                                        |
| Common-cause failure   | Multiple failures arising from one shared cause.                                                                 |
| Common-mode failure    | Nominal alternatives fail similarly or through a shared dependency.                                              |
| Near miss              | Event capable of material consequence that did not realise it.                                                   |

## 4. Mandatory distinctions

| **Do not collapse**      | **Reason**                                                           |
|--------------------------|----------------------------------------------------------------------|
| Threat / hazard          | Deliberate and non-deliberate sources require different assumptions. |
| Cause / failure mode     | Why it failed differs from how the function failed.                  |
| Mode / effect            | Failure behaviour differs from resulting condition.                  |
| Effect / consequence     | Technical effect differs from capability impact.                     |
| Fault / failure          | A fault can exist without defeating function.                        |
| Event / state            | Occurrence differs from continuing condition.                        |
| Exposure / likelihood    | Contact differs from probability.                                    |
| Detection / prevention   | Observing does not stop failure.                                     |
| Failover / recovery      | Transfer differs from restoration.                                   |
| Redundancy / resilience  | Duplication does not prove sustained outcome.                        |
| UNKNOWN / low likelihood | Missing evidence is not evidence of improbability.                   |

# Part III - Scenario and propagation architecture

## 5. Bidirectional analysis

| **Approach**     | **Question**                                 | **Output**                                     |
|------------------|----------------------------------------------|------------------------------------------------|
| Bottom-up        | How can this function fail?                  | Mode, cause and local/global effects.          |
| Top-down         | What can defeat the outcome?                 | Top event and causal combinations.             |
| Path-based       | How can effects traverse dependencies?       | Ordered path and breakpoints.                  |
| State-based      | What changes during maintenance or recovery? | State-specific exposure.                       |
| Capability-based | What minimum outcome must remain?            | Consequence and graceful-degradation boundary. |

## 6. Path types

| **Path type**       | **Meaning**                                         |
|---------------------|-----------------------------------------------------|
| Local               | Contained within intended fault domain.             |
| Cascading           | One failure triggers additional failures.           |
| Common-cause        | One cause affects multiple paths.                   |
| Common-mode         | Similar alternatives fail similarly.                |
| Sequential          | Initial change enables later failure.               |
| Compound            | Multiple events or states combine.                  |
| Latent              | Hidden condition activated on demand.               |
| Maintenance-induced | Work or bypass creates exposure.                    |
| Recovery-induced    | Restoration action creates or reintroduces failure. |
| Cross-domain        | Path traverses multiple AIDCF domains.              |
| Cross-boundary      | Path crosses organisation or assessment scope.      |
| Slow-burn           | Degradation accumulates to threshold.               |
| Intermittent        | Repeated instability complicates diagnosis.         |

## 7. Scenario minimum record

| **Field**              | **Requirement**                                |
|------------------------|------------------------------------------------|
| scenarioId             | Required, or explicit UNKNOWN where permitted. |
| capabilityInstance     | Required, or explicit UNKNOWN where permitted. |
| serviceOutcomes        | Required, or explicit UNKNOWN where permitted. |
| architectureBaseline   | Required, or explicit UNKNOWN where permitted. |
| assessmentBoundary     | Required, or explicit UNKNOWN where permitted. |
| initialOperatingState  | Required, or explicit UNKNOWN where permitted. |
| threatOrHazard         | Required, or explicit UNKNOWN where permitted. |
| initiatingEvent        | Required, or explicit UNKNOWN where permitted. |
| predisposingConditions | Required, or explicit UNKNOWN where permitted. |
| failureCauses          | Required, or explicit UNKNOWN where permitted. |
| initialFailureMode     | Required, or explicit UNKNOWN where permitted. |
| orderedPathSteps       | Required, or explicit UNKNOWN where permitted. |
| faultDomains           | Required, or explicit UNKNOWN where permitted. |
| safeguards             | Required, or explicit UNKNOWN where permitted. |
| safeguardDependencies  | Required, or explicit UNKNOWN where permitted. |
| residualState          | Required, or explicit UNKNOWN where permitted. |
| capabilityConsequence  | Required, or explicit UNKNOWN where permitted. |
| recoveryPath           | Required, or explicit UNKNOWN where permitted. |
| evidence               | Required, or explicit UNKNOWN where permitted. |
| confidenceAndUnknown   | Required, or explicit UNKNOWN where permitted. |
| criticalGate           | Required, or explicit UNKNOWN where permitted. |
| owners                 | Required, or explicit UNKNOWN where permitted. |
| reassessmentTrigger    | Required, or explicit UNKNOWN where permitted. |

# Part IV - Threat taxonomy

| **Source family** | **Examples**                                                                     |
|-------------------|----------------------------------------------------------------------------------|
| External actor    | Trespasser, saboteur, criminal, activist, competitor or state-aligned actor.     |
| Insider           | Employee, contractor, supplier staff or coerced individual.                      |
| Supply chain      | Manufacturer, integrator, logistics, maintenance, software or firmware supplier. |
| Tenant/customer   | Authorised party acting maliciously, negligently or outside agreement.           |
| Remote operator   | Authorised or compromised remote support.                                        |
| Automated source  | Malicious code or automation creating infrastructure effect.                     |
| Unattributed      | Evidence supports deliberate activity but source is unresolved.                  |

| **Threat event**           | **Infrastructure interpretation**                                       |
|----------------------------|-------------------------------------------------------------------------|
| Unauthorised entry         | Access to site, plant, hall, cage or rack.                              |
| Physical interference      | Tampering, switching, obstruction or disconnection.                     |
| Theft/removal              | Removal of equipment, media, cable, fuel or spares.                     |
| Sabotage                   | Deliberate disabling or damage.                                         |
| Utility manipulation       | Interruption or corruption of power, water, fuel or telecom.            |
| OT compromise              | Manipulation of BMS, EPMS, SCADA, controllers or management.            |
| Configuration manipulation | Unauthorised change to settings, thresholds, routes or images.          |
| Supply-chain compromise    | Counterfeit, modified, malicious or unsupported component.              |
| Resource exhaustion        | Intentional consumption of compute, power, cooling, storage or network. |
| Evidence destruction       | Alteration of logs, telemetry, video or records.                        |
| Multi-vector attack        | Coordinated physical, cyber, supplier and social actions.               |

# Part V - Hazard taxonomy

| **Hazard family**        | **Examples**                                                             |
|--------------------------|--------------------------------------------------------------------------|
| Meteorological           | Extreme heat, humidity, wind, lightning, rain, drought or haze.          |
| Hydrological             | Flood, storm surge, groundwater, drainage failure or water scarcity.     |
| Geological               | Earthquake, settlement, subsidence or soil instability.                  |
| Environmental            | Particulate, corrosion, pollution, salt or biological contamination.     |
| External fire/industrial | Adjacent fire, smoke, explosion, vibration or vehicle impact.            |
| Electrical               | Arc, short circuit, overcurrent, overvoltage, backfeed or stored energy. |
| Thermal                  | Overtemperature, heat accumulation, transient or thermal runaway.        |
| Pressure/fluid           | Overpressure, rupture, cavitation, leak or contamination.                |
| Structural/mechanical    | Overload, vibration, anchorage failure, obstruction or collapse.         |
| Chemical/material        | Coolant, refrigerant, battery, fuel, suppressants or incompatibility.    |
| Human factors            | Fatigue, workload, interface ambiguity or lost situational awareness.    |
| Control interaction      | Bad sensor data, unsafe logic, setpoint conflict or unstable automation. |
| Utility/geopolitical     | Grid, water, fuel, telecom, border, sanctions or civil disruption.       |

# Part VI - Failure-cause taxonomy

| **Cause family**     | **Examples**                                                            |
|----------------------|-------------------------------------------------------------------------|
| Design               | Requirement, topology, sizing, protection, tolerance or integration.    |
| Manufacturing        | Defect, material variation, contamination or counterfeit.               |
| Installation         | Assembly, routing, termination, torque, cleanliness or labelling.       |
| Commissioning        | Incomplete scope, unrealistic load or unresolved defect.                |
| Configuration        | Setpoint, firmware, driver, route, threshold or compatibility.          |
| Operation            | Incorrect/delayed action, bypass, overload or deviation.                |
| Maintenance          | Missed/incorrect work, calibration, spares or temporary state.          |
| Ageing               | Wear, corrosion, fatigue, insulation, battery degradation or drift.     |
| Capacity             | Demand exceeds usable/resilient capacity or reserve is committed.       |
| Environment          | Temperature, humidity, fluid quality, particulate, vibration or flood.  |
| Dependency           | Upstream, shared, hidden, recovery-only or external reliance.           |
| Control/monitoring   | Sensor, logic, alarm, communication, historian or response failure.     |
| Human/organisational | Competence, staffing, fatigue, authority or knowledge concentration.    |
| Supplier/contract    | Service, SLA, lead time, access or support failure.                     |
| Security             | Unauthorised access, manipulation, sabotage or theft.                   |
| Change/transition    | Expansion, migration, upgrade, rollback or temporary state.             |
| Recovery             | Wrong sequence, corrupt baseline, insufficient spare or failed restart. |
| UNKNOWN              | Cause cannot be established with available evidence.                    |

**THF-REQ-018** Do not terminate analysis at human error without examining systemic contributors.

**THF-REQ-019** Stop decomposition only where further analysis would not change treatment or accountability.

**THF-REQ-020** Record alternate hypotheses and excluded causes.

**THF-REQ-021** Preserve the observed facts when cause is UNKNOWN.

# Part VII - Failure-mode taxonomy

| **Failure mode**              | **Meaning**                             |
|-------------------------------|-----------------------------------------|
| Complete loss                 | Function unavailable                    |
| Failure to start              | Does not initiate on demand             |
| Failure to stop               | Continues when cessation required       |
| Failure to transfer           | Alternate path not established          |
| Failure to isolate            | Fault crosses boundary                  |
| Failure to reset/recover      | Cannot return to approved state         |
| Degraded output               | Below required capacity or quality      |
| Excess output                 | Unsafe output exceeds limit             |
| Incorrect output              | Wrong value, route, state or target     |
| Delayed output                | Too late for outcome                    |
| Premature output              | Before required conditions              |
| Intermittent operation        | Repeated appearance/disappearance       |
| Unstable/oscillating          | Uncontrolled variation                  |
| Capacity exhaustion           | Demand exceeds capacity                 |
| Performance collapse          | Nonlinear degradation after threshold   |
| Data/configuration corruption | State becomes inconsistent              |
| Loss of visibility            | Cannot observe/diagnose                 |
| False indication              | Indicates absent condition              |
| Failure to alarm              | Warning absent or late                  |
| Nuisance alarm                | False/excessive alarms mask events      |
| Latent standby failure        | Standby unavailable on demand           |
| Bypass left active            | Temporary impairment persists           |
| Uncontrolled shutdown         | Ceases without orderly preservation     |
| Unsafe persistence            | Remains active when hazardous           |
| Leakage/escape                | Fluid, energy, data or material escapes |
| Congestion/blockage           | Flow is impeded                         |
| Loss of synchronisation       | Coordinated state diverges              |
| Incompatibility               | Versions/materials/protocols conflict   |
| Misallocation                 | Resource assigned wrongly               |
| Unknown mode                  | Manner unresolved                       |

# Part VIII - Effects, propagation and consequence

| **Effect level** | **Question**                               |
|------------------|--------------------------------------------|
| Local            | What happens at failed item/function?      |
| Next-level       | What happens to subsystem or dependent?    |
| Cross-domain     | Which other domain becomes impaired?       |
| Capability       | Which Service Outcome is degraded or lost? |
| Stakeholder      | Who or what experiences consequence?       |

| **Operator**    | **Use**                                                            |
|-----------------|--------------------------------------------------------------------|
| CAUSES          | Canonical causal, propagation, safeguard or evidence relationship. |
| CONTRIBUTES_TO  | Canonical causal, propagation, safeguard or evidence relationship. |
| TRIGGERS        | Canonical causal, propagation, safeguard or evidence relationship. |
| PROPAGATES_VIA  | Canonical causal, propagation, safeguard or evidence relationship. |
| PROPAGATES_TO   | Canonical causal, propagation, safeguard or evidence relationship. |
| AMPLIFIES       | Canonical causal, propagation, safeguard or evidence relationship. |
| MASKS           | Canonical causal, propagation, safeguard or evidence relationship. |
| BYPASSES        | Canonical causal, propagation, safeguard or evidence relationship. |
| DEFEATS         | Canonical causal, propagation, safeguard or evidence relationship. |
| CONTAINS        | Canonical causal, propagation, safeguard or evidence relationship. |
| DELAYS          | Canonical causal, propagation, safeguard or evidence relationship. |
| RECOVERS        | Canonical causal, propagation, safeguard or evidence relationship. |
| REINTRODUCES    | Canonical causal, propagation, safeguard or evidence relationship. |
| CORRELATES_WITH | Canonical causal, propagation, safeguard or evidence relationship. |
| CONFLICTS_WITH  | Canonical causal, propagation, safeguard or evidence relationship. |

| **Consequence family**        | **Required expression**                                                                          |
|-------------------------------|--------------------------------------------------------------------------------------------------|
| Life safety and health        | Affected capability/stakeholder, magnitude, duration, concentration, assumptions and confidence. |
| Capability availability       | Affected capability/stakeholder, magnitude, duration, concentration, assumptions and confidence. |
| Compute capacity              | Affected capability/stakeholder, magnitude, duration, concentration, assumptions and confidence. |
| Performance                   | Affected capability/stakeholder, magnitude, duration, concentration, assumptions and confidence. |
| Data/artifact integrity       | Affected capability/stakeholder, magnitude, duration, concentration, assumptions and confidence. |
| Isolation and security        | Affected capability/stakeholder, magnitude, duration, concentration, assumptions and confidence. |
| Physical damage               | Affected capability/stakeholder, magnitude, duration, concentration, assumptions and confidence. |
| Environmental impact          | Affected capability/stakeholder, magnitude, duration, concentration, assumptions and confidence. |
| Recovery complexity           | Affected capability/stakeholder, magnitude, duration, concentration, assumptions and confidence. |
| Financial impact              | Affected capability/stakeholder, magnitude, duration, concentration, assumptions and confidence. |
| Contractual/regulatory impact | Affected capability/stakeholder, magnitude, duration, concentration, assumptions and confidence. |
| Strategic/sovereignty impact  | Affected capability/stakeholder, magnitude, duration, concentration, assumptions and confidence. |
| Evidence and attribution loss | Affected capability/stakeholder, magnitude, duration, concentration, assumptions and confidence. |

# Part IX - Safeguards and resilience

| **Function**       | **Examples**                                            |
|--------------------|---------------------------------------------------------|
| Anticipate         | Forecast, condition monitoring, capacity planning.      |
| Prevent            | Access control, design margin, protection, maintenance. |
| Detect             | Sensors, telemetry, inspection and alarms.              |
| Decide             | Logic, operator, escalation and authority.              |
| Respond            | Transfer, isolation, throttling and dispatch.           |
| Contain            | Fault isolation, fire zone and segmentation.            |
| Withstand          | Reserve, hardening, redundancy and diversity.           |
| Degrade gracefully | Priority, rate limiting and orderly shutdown.           |
| Recover            | Restart, rebuild, repair and data recovery.             |
| Adapt              | Redesign, learning and strengthened independence.       |

| **Barrier field** | **Required content**                               |
|-------------------|----------------------------------------------------|
| barrierId         | Stable identifier                                  |
| pathPosition      | Cause, escalation, consequence or recovery side    |
| objective         | Path condition altered                             |
| dependencies      | Power, sensing, control, people and supplier needs |
| applicableStates  | States and transitions covered                     |
| capacity/duration | Demand it withstands                               |
| failureModes      | How barrier can fail                               |
| validation        | Test, inspection, event, analysis or simulation    |
| confidence        | Evidence-bounded state                             |
| residualExposure  | Path remaining after demonstrated action           |

## Safe validation hierarchy

| **Level** | **Method**                                         |
|-----------|----------------------------------------------------|
| V0        | Document/configuration review                      |
| V1        | Inspection/observation                             |
| V2        | Historical event and telemetry                     |
| V3        | Engineering analysis/simulation                    |
| V4        | Tabletop/procedural exercise                       |
| V5        | Component functional test                          |
| V6        | Integrated systems test                            |
| V7        | Live capability exercise where authorised and safe |

# Part X - Analysis techniques

| **Technique**                     | **AIDCF use**                                                                                                |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------|
| FMEA/FMECA                        | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| Fault Tree Analysis               | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| Event Tree Analysis               | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| Bow-tie Analysis                  | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| HAZOP-style study                 | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| What-if/SWIFT                     | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| Cause-consequence analysis        | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| Dependency graph analysis         | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| Common-cause analysis             | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| State-transition analysis         | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| Reliability block diagram         | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| Root-cause analysis               | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| Capability impact analysis        | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| Scenario stress analysis          | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |
| Validated digital-twin simulation | Selected according to purpose, lifecycle, complexity, evidence, state behaviour, safety and required output. |

Default AIDCF hybrid: capability impact + dependency graph + selected FMEA/FMECA + top-event analysis for critical outcomes + barrier analysis + state-based scenario validation. No single technique is sufficient by default.

# Part XI - Criticality and uncertainty

**THF-REQ-022** Severity, likelihood, detectability and confidence shall remain separate.

**THF-REQ-023** RPN or another arithmetic product shall not determine assurance by itself.

**THF-REQ-024** Critical gates and catastrophic consequence shall not be averaged away.

**THF-REQ-025** Quantitative probability shall be used only where data, model and assumptions are defensible.

| **Band**        | **Capability interpretation**                                          |
|-----------------|------------------------------------------------------------------------|
| S0 Negligible   | No material outcome effect.                                            |
| S1 Minor        | Local effect; outcome within requirement.                              |
| S2 Moderate     | Recoverable degradation within approved tolerance.                     |
| S3 Major        | Required outcome breached.                                             |
| S4 Critical     | Extended/concentrated loss or serious safety/strategic impact.         |
| S5 Catastrophic | Fatality potential, mission loss or systemic irreversible consequence. |

| **Uncertainty**      | **Treatment**                                           |
|----------------------|---------------------------------------------------------|
| Model                | Record alternate structures.                            |
| Parameter            | Use range and sensitivity.                              |
| Evidence gap         | Preserve UNKNOWN.                                       |
| Temporal             | State observation and validity.                         |
| Configuration        | Separate intended, as-built, commissioned and observed. |
| Expert disagreement  | Retain dissent and basis.                               |
| Rare event           | Avoid false precision.                                  |
| Emergent interaction | Use scenario, graph and stress analysis.                |

# Part XII - Eight-domain failure catalogue

## 31. D1 Physical

| **Scenario family**       | **Required analysis**                                                                                                                              |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Unauthorised entry        | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Insider sabotage          | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Surveillance blind spot   | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Asset removal             | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Security-zone collapse    | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Emergency-access conflict | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |

## 32. D2 Facilities Engineering

| **Scenario family**      | **Required analysis**                                                                                                                              |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Structural overload      | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Fire-system mismatch     | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Water ingress            | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Common controller defect | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| As-built divergence      | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Commissioning omission   | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |

## 33. D3 Power & Cooling

| **Scenario family**        | **Required analysis**                                                                                                                              |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Utility loss               | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Generator no-start         | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| UPS loss                   | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Protection miscoordination | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Rack overload              | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Cooling capacity loss      | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| CDU failure                | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Thermal transient          | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Liquid leak                | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Shared control failure     | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |

## 34. D4 Environmental & Resource

| **Scenario family**            | **Required analysis**                                                                                                                              |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Ambient exceedance             | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Water scarcity                 | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Poor coolant quality           | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Air contamination              | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Refrigerant loss               | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Efficiency-resilience conflict | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Metering/claim error           | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |

## 35. D5 Operations

| **Scenario family**        | **Required analysis**                                                                                                                              |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Maintenance-induced outage | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Procedure failure          | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Competence gap             | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Change failure             | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Alarm-response failure     | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Spares/obsolescence        | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Supplier support loss      | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Handover failure           | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |

## 36. D6 Compute

| **Scenario family**      | **Required analysis**                                                                                                                              |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Accelerator/node failure | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Scale-up domain failure  | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Firmware incompatibility | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Scheduler failure        | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Telemetry blindness      | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Thermal throttling       | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Mass reboot              | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Golden-image corruption  | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |

## 37. D7 Storage

| **Scenario family**      | **Required analysis**                                                                                                                              |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Metadata failure         | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Capacity exhaustion      | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Throughput collapse      | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Checkpoint failure       | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Protection common-mode   | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Silent corruption        | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Restore failure          | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Data-transfer bottleneck | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |

## 38. D8 Network

| **Scenario family**        | **Required analysis**                                                                                                                              |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Fabric partition           | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Congestion collapse        | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Scale-up link failure      | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Management network loss    | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Time-service failure       | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| DNS/DHCP/IPAM failure      | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Configuration blast radius | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |
| Optical/cabling defect     | Causes; functional mode; local and propagated effects; fault domains; safeguards; residual capability consequence; recovery; evidence and UNKNOWN. |

# Part XIII - Cross-domain scenario library

| **ID** | **Scenario**                                                | **Minimum path analysis**                                                                                                 |
|--------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| X01    | Utility loss + generator no-start + UPS autonomy exhaustion | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X02    | Cooling loss at sustained AI load                           | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X03    | Liquid leak with detection gap                              | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X04    | Maintenance removes hidden shared dependency                | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X05    | BMS/EPMS compromise or malfunction                          | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X06    | Fabric congestion during checkpoint demand                  | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X07    | Storage metadata failure during training                    | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X08    | Firmware rollout common-mode failure                        | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X09    | Fire disables paired infrastructure routes                  | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X10    | Extreme ambient plus water restriction                      | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X11    | Operator error during alarm flood                           | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X12    | Long-lead spare after rare failure                          | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X13    | Time-source divergence                                      | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X14    | Colocation responsibility gap                               | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X15    | Recovery reintroduces corrupt configuration                 | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X16    | Physical intrusion disrupts interconnect                    | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X17    | Expansion creates stranded compute                          | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X18    | Loss of remote OEM support                                  | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X19    | Shared authentication service failure                       | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |
| X20    | Compound flood/fire/grid/telecom event                      | Initiating state -\> affected entities -\> dependencies -\> safeguards -\> residual capability -\> recovery -\> evidence. |

## Scenario prioritisation gates

- Life safety or hazardous energy

- Essential cooling loss

- Standby/resilient power loss

- Containment failure

- Large capability concentration

- Checkpoint or recovery-baseline corruption

- Common-mode defeat of redundancy

- Recovery objective at risk

- Weakly evidenced external dependency

- Long-lead or irreplaceable component

- Sovereignty impact

- Critical UNKNOWN

# Part XIV - Assessment records and evidence

| **Step** | **Activity**                                                                |
|----------|-----------------------------------------------------------------------------|
| 1        | Frame decision, capability, outcome, boundary and state                     |
| 2        | Confirm intended, as-built, commissioned and observed baseline              |
| 3        | Map functions, assets, interfaces, dependencies and fault domains           |
| 4        | Identify threats, hazards, causes and failure modes                         |
| 5        | Construct local, cross-domain, compound, maintenance and recovery scenarios |
| 6        | Analyse effects, propagation, timing and concentration                      |
| 7        | Map safeguards and their dependencies                                       |
| 8        | Validate safely                                                             |
| 9        | Determine residual state, critical gates and UNKNOWN                        |
| 10       | Report finding, action, retest and reassessment triggers                    |

| **Evidence class**     | **Examples**                                                  |
|------------------------|---------------------------------------------------------------|
| Architecture           | Single lines, P&IDs, topologies, control narratives.          |
| As-built/configuration | Registers, settings, firmware, routes and dependencies.       |
| Commissioning/testing  | Functional, integrated, load, failover and recovery evidence. |
| Operations             | Telemetry, alarms, trends, work orders and logs.              |
| Incident               | Timelines, cause analysis and near misses.                    |
| Supplier/contract      | SLA, support, spares, lead time and responsibility.           |
| Observation/interview  | Walkthrough, witnessed action and competent testimony.        |
| Engineering analysis   | Studies, calculations and validated simulations.              |
| Threat evidence        | Site threat assessment, access, events and intelligence.      |

## Finding taxonomy

| **Finding**          | **Meaning**                                                      |
|----------------------|------------------------------------------------------------------|
| Uncontrolled path    | Material consequence without effective barrier.                  |
| Fragile safeguard    | Barrier has shared dependency, inadequate capacity or weak test. |
| Common-mode exposure | Alternatives share cause or dependency.                          |
| Containment gap      | Effect crosses intended boundary.                                |
| Capacity cliff       | Small change creates disproportionate loss.                      |
| Recovery fragility   | Restoration depends on unproven state, people or resource.       |
| Evidence gap         | Material assertion inadequately supported.                       |
| State coverage gap   | Degraded/maintenance/recovery state not covered.                 |
| Responsibility gap   | Authority or evidence obligation unclear.                        |
| Critical UNKNOWN     | Unresolved information caps assurance.                           |

# Part XV - Machine-readable model

| **Node**          | **Purpose**                           |
|-------------------|---------------------------------------|
| ThreatSource      | Canonical graph entity for AIDCF-004. |
| ThreatEvent       | Canonical graph entity for AIDCF-004. |
| Hazard            | Canonical graph entity for AIDCF-004. |
| InitiatingEvent   | Canonical graph entity for AIDCF-004. |
| FailureCause      | Canonical graph entity for AIDCF-004. |
| FailureMode       | Canonical graph entity for AIDCF-004. |
| Effect            | Canonical graph entity for AIDCF-004. |
| PropagationStep   | Canonical graph entity for AIDCF-004. |
| Consequence       | Canonical graph entity for AIDCF-004. |
| Safeguard         | Canonical graph entity for AIDCF-004. |
| BarrierClaim      | Canonical graph entity for AIDCF-004. |
| RecoveryAction    | Canonical graph entity for AIDCF-004. |
| Scenario          | Canonical graph entity for AIDCF-004. |
| EvidenceObject    | Canonical graph entity for AIDCF-004. |
| Finding           | Canonical graph entity for AIDCF-004. |
| AssuranceDecision | Canonical graph entity for AIDCF-004. |

| **Relationship** | **Semantic use**                                                                            |
|------------------|---------------------------------------------------------------------------------------------|
| TARGETS          | Controlled directed relation; material assertions require provenance, state and confidence. |
| EXPOSES          | Controlled directed relation; material assertions require provenance, state and confidence. |
| INITIATES        | Controlled directed relation; material assertions require provenance, state and confidence. |
| HAS_CAUSE        | Controlled directed relation; material assertions require provenance, state and confidence. |
| FAILS_AS         | Controlled directed relation; material assertions require provenance, state and confidence. |
| CAUSES           | Controlled directed relation; material assertions require provenance, state and confidence. |
| CONTRIBUTES_TO   | Controlled directed relation; material assertions require provenance, state and confidence. |
| TRIGGERS         | Controlled directed relation; material assertions require provenance, state and confidence. |
| HAS_LOCAL_EFFECT | Controlled directed relation; material assertions require provenance, state and confidence. |
| PROPAGATES_VIA   | Controlled directed relation; material assertions require provenance, state and confidence. |
| PROPAGATES_TO    | Controlled directed relation; material assertions require provenance, state and confidence. |
| AMPLIFIED_BY     | Controlled directed relation; material assertions require provenance, state and confidence. |
| AFFECTS          | Controlled directed relation; material assertions require provenance, state and confidence. |
| PREVENTED_BY     | Controlled directed relation; material assertions require provenance, state and confidence. |
| DETECTED_BY      | Controlled directed relation; material assertions require provenance, state and confidence. |
| CONTAINED_BY     | Controlled directed relation; material assertions require provenance, state and confidence. |
| RECOVERED_BY     | Controlled directed relation; material assertions require provenance, state and confidence. |
| DEFEATS          | Controlled directed relation; material assertions require provenance, state and confidence. |
| DEPENDS_ON       | Controlled directed relation; material assertions require provenance, state and confidence. |
| EVIDENCED_BY     | Controlled directed relation; material assertions require provenance, state and confidence. |
| CHALLENGED_BY    | Controlled directed relation; material assertions require provenance, state and confidence. |
| RESULTS_IN       | Controlled directed relation; material assertions require provenance, state and confidence. |
| INVALIDATES      | Controlled directed relation; material assertions require provenance, state and confidence. |

## Publication package

- OWL ontology and Turtle serialisation

- JSON-LD context and examples

- JSON Schema for scenario exchange

- SHACL validation shapes

- CSV failure-mode and relationship registries

- Worked liquid-cooling and distributed-training examples

- Changelog, migration and extension guidance

# Part XVI - Governance and acceptance

- Controlled vocabulary and change board

- Multidisciplinary domain review

- Semantic versioning and migration

- Normative core separated from informative examples

- Independent incident and test comparison

- Inter-assessor consistency testing

- Security classification of sensitive paths

- Vendor neutrality and conflict declarations

## Prohibited practices

- Generic list treated as complete assessment

- Unsupported precise probability

- Average/RPN overriding critical gates

- Stopping at operator error

- Assuming duplicated paths are independent

- Untested safeguard treated as effective

- Ignoring recovery-only dependencies

- Unsafe intrusive validation

- Publishing sensitive paths without access control

# Appendix A - Failure Mode Catalogue

| **ID**  | **Group**         | **Required function**   | **Failure mode**         |
|---------|-------------------|-------------------------|--------------------------|
| FM-0001 | Physical security | prevent entry           | Complete loss            |
| FM-0002 | Physical security | prevent entry           | Failure to start         |
| FM-0003 | Physical security | prevent entry           | Failure to stop          |
| FM-0004 | Physical security | prevent entry           | Failure to transfer      |
| FM-0005 | Physical security | prevent entry           | Failure to isolate       |
| FM-0006 | Physical security | prevent entry           | Failure to reset/recover |
| FM-0007 | Physical security | prevent entry           | Degraded output          |
| FM-0008 | Physical security | prevent entry           | Excess output            |
| FM-0009 | Physical security | detect intrusion        | Complete loss            |
| FM-0010 | Physical security | detect intrusion        | Failure to start         |
| FM-0011 | Physical security | detect intrusion        | Failure to stop          |
| FM-0012 | Physical security | detect intrusion        | Failure to transfer      |
| FM-0013 | Physical security | detect intrusion        | Failure to isolate       |
| FM-0014 | Physical security | detect intrusion        | Failure to reset/recover |
| FM-0015 | Physical security | detect intrusion        | Degraded output          |
| FM-0016 | Physical security | detect intrusion        | Excess output            |
| FM-0017 | Physical security | attribute access        | Complete loss            |
| FM-0018 | Physical security | attribute access        | Failure to start         |
| FM-0019 | Physical security | attribute access        | Failure to stop          |
| FM-0020 | Physical security | attribute access        | Failure to transfer      |
| FM-0021 | Physical security | attribute access        | Failure to isolate       |
| FM-0022 | Physical security | attribute access        | Failure to reset/recover |
| FM-0023 | Physical security | attribute access        | Degraded output          |
| FM-0024 | Physical security | attribute access        | Excess output            |
| FM-0025 | Physical security | retain evidence         | Complete loss            |
| FM-0026 | Physical security | retain evidence         | Failure to start         |
| FM-0027 | Physical security | retain evidence         | Failure to stop          |
| FM-0028 | Physical security | retain evidence         | Failure to transfer      |
| FM-0029 | Physical security | retain evidence         | Failure to isolate       |
| FM-0030 | Physical security | retain evidence         | Failure to reset/recover |
| FM-0031 | Physical security | retain evidence         | Degraded output          |
| FM-0032 | Physical security | retain evidence         | Excess output            |
| FM-0033 | Electrical        | supply power            | Complete loss            |
| FM-0034 | Electrical        | supply power            | Failure to start         |
| FM-0035 | Electrical        | supply power            | Failure to stop          |
| FM-0036 | Electrical        | supply power            | Failure to transfer      |
| FM-0037 | Electrical        | supply power            | Failure to isolate       |
| FM-0038 | Electrical        | supply power            | Failure to reset/recover |
| FM-0039 | Electrical        | supply power            | Degraded output          |
| FM-0040 | Electrical        | supply power            | Excess output            |
| FM-0041 | Electrical        | transfer source         | Complete loss            |
| FM-0042 | Electrical        | transfer source         | Failure to start         |
| FM-0043 | Electrical        | transfer source         | Failure to stop          |
| FM-0044 | Electrical        | transfer source         | Failure to transfer      |
| FM-0045 | Electrical        | transfer source         | Failure to isolate       |
| FM-0046 | Electrical        | transfer source         | Failure to reset/recover |
| FM-0047 | Electrical        | transfer source         | Degraded output          |
| FM-0048 | Electrical        | transfer source         | Excess output            |
| FM-0049 | Electrical        | protect fault           | Complete loss            |
| FM-0050 | Electrical        | protect fault           | Failure to start         |
| FM-0051 | Electrical        | protect fault           | Failure to stop          |
| FM-0052 | Electrical        | protect fault           | Failure to transfer      |
| FM-0053 | Electrical        | protect fault           | Failure to isolate       |
| FM-0054 | Electrical        | protect fault           | Failure to reset/recover |
| FM-0055 | Electrical        | protect fault           | Degraded output          |
| FM-0056 | Electrical        | protect fault           | Excess output            |
| FM-0057 | Electrical        | distribute power        | Complete loss            |
| FM-0058 | Electrical        | distribute power        | Failure to start         |
| FM-0059 | Electrical        | distribute power        | Failure to stop          |
| FM-0060 | Electrical        | distribute power        | Failure to transfer      |
| FM-0061 | Electrical        | distribute power        | Failure to isolate       |
| FM-0062 | Electrical        | distribute power        | Failure to reset/recover |
| FM-0063 | Electrical        | distribute power        | Degraded output          |
| FM-0064 | Electrical        | distribute power        | Excess output            |
| FM-0065 | Cooling           | capture heat            | Complete loss            |
| FM-0066 | Cooling           | capture heat            | Failure to start         |
| FM-0067 | Cooling           | capture heat            | Failure to stop          |
| FM-0068 | Cooling           | capture heat            | Failure to transfer      |
| FM-0069 | Cooling           | capture heat            | Failure to isolate       |
| FM-0070 | Cooling           | capture heat            | Failure to reset/recover |
| FM-0071 | Cooling           | capture heat            | Degraded output          |
| FM-0072 | Cooling           | capture heat            | Excess output            |
| FM-0073 | Cooling           | transport coolant       | Complete loss            |
| FM-0074 | Cooling           | transport coolant       | Failure to start         |
| FM-0075 | Cooling           | transport coolant       | Failure to stop          |
| FM-0076 | Cooling           | transport coolant       | Failure to transfer      |
| FM-0077 | Cooling           | transport coolant       | Failure to isolate       |
| FM-0078 | Cooling           | transport coolant       | Failure to reset/recover |
| FM-0079 | Cooling           | transport coolant       | Degraded output          |
| FM-0080 | Cooling           | transport coolant       | Excess output            |
| FM-0081 | Cooling           | reject heat             | Complete loss            |
| FM-0082 | Cooling           | reject heat             | Failure to start         |
| FM-0083 | Cooling           | reject heat             | Failure to stop          |
| FM-0084 | Cooling           | reject heat             | Failure to transfer      |
| FM-0085 | Cooling           | reject heat             | Failure to isolate       |
| FM-0086 | Cooling           | reject heat             | Failure to reset/recover |
| FM-0087 | Cooling           | reject heat             | Degraded output          |
| FM-0088 | Cooling           | reject heat             | Excess output            |
| FM-0089 | Cooling           | detect leak             | Complete loss            |
| FM-0090 | Cooling           | detect leak             | Failure to start         |
| FM-0091 | Cooling           | detect leak             | Failure to stop          |
| FM-0092 | Cooling           | detect leak             | Failure to transfer      |
| FM-0093 | Cooling           | detect leak             | Failure to isolate       |
| FM-0094 | Cooling           | detect leak             | Failure to reset/recover |
| FM-0095 | Cooling           | detect leak             | Degraded output          |
| FM-0096 | Cooling           | detect leak             | Excess output            |
| FM-0097 | Facilities OT     | sense state             | Complete loss            |
| FM-0098 | Facilities OT     | sense state             | Failure to start         |
| FM-0099 | Facilities OT     | sense state             | Failure to stop          |
| FM-0100 | Facilities OT     | sense state             | Failure to transfer      |
| FM-0101 | Facilities OT     | sense state             | Failure to isolate       |
| FM-0102 | Facilities OT     | sense state             | Failure to reset/recover |
| FM-0103 | Facilities OT     | sense state             | Degraded output          |
| FM-0104 | Facilities OT     | sense state             | Excess output            |
| FM-0105 | Facilities OT     | execute logic           | Complete loss            |
| FM-0106 | Facilities OT     | execute logic           | Failure to start         |
| FM-0107 | Facilities OT     | execute logic           | Failure to stop          |
| FM-0108 | Facilities OT     | execute logic           | Failure to transfer      |
| FM-0109 | Facilities OT     | execute logic           | Failure to isolate       |
| FM-0110 | Facilities OT     | execute logic           | Failure to reset/recover |
| FM-0111 | Facilities OT     | execute logic           | Degraded output          |
| FM-0112 | Facilities OT     | execute logic           | Excess output            |
| FM-0113 | Facilities OT     | command actuator        | Complete loss            |
| FM-0114 | Facilities OT     | command actuator        | Failure to start         |
| FM-0115 | Facilities OT     | command actuator        | Failure to stop          |
| FM-0116 | Facilities OT     | command actuator        | Failure to transfer      |
| FM-0117 | Facilities OT     | command actuator        | Failure to isolate       |
| FM-0118 | Facilities OT     | command actuator        | Failure to reset/recover |
| FM-0119 | Facilities OT     | command actuator        | Degraded output          |
| FM-0120 | Facilities OT     | command actuator        | Excess output            |
| FM-0121 | Facilities OT     | raise alarm             | Complete loss            |
| FM-0122 | Facilities OT     | raise alarm             | Failure to start         |
| FM-0123 | Facilities OT     | raise alarm             | Failure to stop          |
| FM-0124 | Facilities OT     | raise alarm             | Failure to transfer      |
| FM-0125 | Facilities OT     | raise alarm             | Failure to isolate       |
| FM-0126 | Facilities OT     | raise alarm             | Failure to reset/recover |
| FM-0127 | Facilities OT     | raise alarm             | Degraded output          |
| FM-0128 | Facilities OT     | raise alarm             | Excess output            |
| FM-0129 | Operations        | authorise work          | Complete loss            |
| FM-0130 | Operations        | authorise work          | Failure to start         |
| FM-0131 | Operations        | authorise work          | Failure to stop          |
| FM-0132 | Operations        | authorise work          | Failure to transfer      |
| FM-0133 | Operations        | authorise work          | Failure to isolate       |
| FM-0134 | Operations        | authorise work          | Failure to reset/recover |
| FM-0135 | Operations        | authorise work          | Degraded output          |
| FM-0136 | Operations        | authorise work          | Excess output            |
| FM-0137 | Operations        | isolate energy          | Complete loss            |
| FM-0138 | Operations        | isolate energy          | Failure to start         |
| FM-0139 | Operations        | isolate energy          | Failure to stop          |
| FM-0140 | Operations        | isolate energy          | Failure to transfer      |
| FM-0141 | Operations        | isolate energy          | Failure to isolate       |
| FM-0142 | Operations        | isolate energy          | Failure to reset/recover |
| FM-0143 | Operations        | isolate energy          | Degraded output          |
| FM-0144 | Operations        | isolate energy          | Excess output            |
| FM-0145 | Operations        | respond                 | Complete loss            |
| FM-0146 | Operations        | respond                 | Failure to start         |
| FM-0147 | Operations        | respond                 | Failure to stop          |
| FM-0148 | Operations        | respond                 | Failure to transfer      |
| FM-0149 | Operations        | respond                 | Failure to isolate       |
| FM-0150 | Operations        | respond                 | Failure to reset/recover |
| FM-0151 | Operations        | respond                 | Degraded output          |
| FM-0152 | Operations        | respond                 | Excess output            |
| FM-0153 | Operations        | recover                 | Complete loss            |
| FM-0154 | Operations        | recover                 | Failure to start         |
| FM-0155 | Operations        | recover                 | Failure to stop          |
| FM-0156 | Operations        | recover                 | Failure to transfer      |
| FM-0157 | Operations        | recover                 | Failure to isolate       |
| FM-0158 | Operations        | recover                 | Failure to reset/recover |
| FM-0159 | Operations        | recover                 | Degraded output          |
| FM-0160 | Operations        | recover                 | Excess output            |
| FM-0161 | Compute           | boot node               | Complete loss            |
| FM-0162 | Compute           | boot node               | Failure to start         |
| FM-0163 | Compute           | boot node               | Failure to stop          |
| FM-0164 | Compute           | boot node               | Failure to transfer      |
| FM-0165 | Compute           | boot node               | Failure to isolate       |
| FM-0166 | Compute           | boot node               | Failure to reset/recover |
| FM-0167 | Compute           | boot node               | Degraded output          |
| FM-0168 | Compute           | boot node               | Excess output            |
| FM-0169 | Compute           | execute workload        | Complete loss            |
| FM-0170 | Compute           | execute workload        | Failure to start         |
| FM-0171 | Compute           | execute workload        | Failure to stop          |
| FM-0172 | Compute           | execute workload        | Failure to transfer      |
| FM-0173 | Compute           | execute workload        | Failure to isolate       |
| FM-0174 | Compute           | execute workload        | Failure to reset/recover |
| FM-0175 | Compute           | execute workload        | Degraded output          |
| FM-0176 | Compute           | execute workload        | Excess output            |
| FM-0177 | Compute           | coordinate accelerators | Complete loss            |
| FM-0178 | Compute           | coordinate accelerators | Failure to start         |
| FM-0179 | Compute           | coordinate accelerators | Failure to stop          |
| FM-0180 | Compute           | coordinate accelerators | Failure to transfer      |
| FM-0181 | Compute           | coordinate accelerators | Failure to isolate       |
| FM-0182 | Compute           | coordinate accelerators | Failure to reset/recover |
| FM-0183 | Compute           | coordinate accelerators | Degraded output          |
| FM-0184 | Compute           | coordinate accelerators | Excess output            |
| FM-0185 | Compute           | schedule jobs           | Complete loss            |
| FM-0186 | Compute           | schedule jobs           | Failure to start         |
| FM-0187 | Compute           | schedule jobs           | Failure to stop          |
| FM-0188 | Compute           | schedule jobs           | Failure to transfer      |
| FM-0189 | Compute           | schedule jobs           | Failure to isolate       |
| FM-0190 | Compute           | schedule jobs           | Failure to reset/recover |
| FM-0191 | Compute           | schedule jobs           | Degraded output          |
| FM-0192 | Compute           | schedule jobs           | Excess output            |
| FM-0193 | Storage           | serve data              | Complete loss            |
| FM-0194 | Storage           | serve data              | Failure to start         |
| FM-0195 | Storage           | serve data              | Failure to stop          |
| FM-0196 | Storage           | serve data              | Failure to transfer      |
| FM-0197 | Storage           | serve data              | Failure to isolate       |
| FM-0198 | Storage           | serve data              | Failure to reset/recover |
| FM-0199 | Storage           | serve data              | Degraded output          |
| FM-0200 | Storage           | serve data              | Excess output            |
| FM-0201 | Storage           | maintain metadata       | Complete loss            |
| FM-0202 | Storage           | maintain metadata       | Failure to start         |
| FM-0203 | Storage           | maintain metadata       | Failure to stop          |
| FM-0204 | Storage           | maintain metadata       | Failure to transfer      |
| FM-0205 | Storage           | maintain metadata       | Failure to isolate       |
| FM-0206 | Storage           | maintain metadata       | Failure to reset/recover |
| FM-0207 | Storage           | maintain metadata       | Degraded output          |
| FM-0208 | Storage           | maintain metadata       | Excess output            |
| FM-0209 | Storage           | persist checkpoint      | Complete loss            |
| FM-0210 | Storage           | persist checkpoint      | Failure to start         |
| FM-0211 | Storage           | persist checkpoint      | Failure to stop          |
| FM-0212 | Storage           | persist checkpoint      | Failure to transfer      |
| FM-0213 | Storage           | persist checkpoint      | Failure to isolate       |
| FM-0214 | Storage           | persist checkpoint      | Failure to reset/recover |
| FM-0215 | Storage           | persist checkpoint      | Degraded output          |
| FM-0216 | Storage           | persist checkpoint      | Excess output            |
| FM-0217 | Storage           | restore data            | Complete loss            |
| FM-0218 | Storage           | restore data            | Failure to start         |
| FM-0219 | Storage           | restore data            | Failure to stop          |
| FM-0220 | Storage           | restore data            | Failure to transfer      |
| FM-0221 | Storage           | restore data            | Failure to isolate       |
| FM-0222 | Storage           | restore data            | Failure to reset/recover |
| FM-0223 | Storage           | restore data            | Degraded output          |
| FM-0224 | Storage           | restore data            | Excess output            |
| FM-0225 | Network           | forward traffic         | Complete loss            |
| FM-0226 | Network           | forward traffic         | Failure to start         |
| FM-0227 | Network           | forward traffic         | Failure to stop          |
| FM-0228 | Network           | forward traffic         | Failure to transfer      |
| FM-0229 | Network           | forward traffic         | Failure to isolate       |
| FM-0230 | Network           | forward traffic         | Failure to reset/recover |
| FM-0231 | Network           | forward traffic         | Degraded output          |
| FM-0232 | Network           | forward traffic         | Excess output            |
| FM-0233 | Network           | control congestion      | Complete loss            |
| FM-0234 | Network           | control congestion      | Failure to start         |
| FM-0235 | Network           | control congestion      | Failure to stop          |
| FM-0236 | Network           | control congestion      | Failure to transfer      |
| FM-0237 | Network           | control congestion      | Failure to isolate       |
| FM-0238 | Network           | control congestion      | Failure to reset/recover |
| FM-0239 | Network           | control congestion      | Degraded output          |
| FM-0240 | Network           | control congestion      | Excess output            |
| FM-0241 | Network           | provide timing          | Complete loss            |
| FM-0242 | Network           | provide timing          | Failure to start         |
| FM-0243 | Network           | provide timing          | Failure to stop          |
| FM-0244 | Network           | provide timing          | Failure to transfer      |
| FM-0245 | Network           | provide timing          | Failure to isolate       |
| FM-0246 | Network           | provide timing          | Failure to reset/recover |
| FM-0247 | Network           | provide timing          | Degraded output          |
| FM-0248 | Network           | provide timing          | Excess output            |
| FM-0249 | Network           | enable management       | Complete loss            |
| FM-0250 | Network           | enable management       | Failure to start         |
| FM-0251 | Network           | enable management       | Failure to stop          |
| FM-0252 | Network           | enable management       | Failure to transfer      |
| FM-0253 | Network           | enable management       | Failure to isolate       |
| FM-0254 | Network           | enable management       | Failure to reset/recover |
| FM-0255 | Network           | enable management       | Degraded output          |
| FM-0256 | Network           | enable management       | Excess output            |

# Appendix B - Working templates

\[Context/state\], \[threat/hazard/event\] causes \[mode\] in \[entity/function\]. Effect propagates through \[dependencies/fault domains\] and affects \[Service Outcome\]. \[Safeguards\] are expected to act. Evidence \[supports/challenges/is insufficient\]. Residual state is \[state\], with \[confidence/UNKNOWN\].

| **Step** | **Entity** | **Pre-state** | **Event/mode** | **Dependency** | **Effect** | **Safeguard** | **Post-state** | **Evidence** |
|----------|------------|---------------|----------------|----------------|------------|---------------|----------------|--------------|
| 1        |            |               |                |                |            |               |                |              |
| 2        |            |               |                |                |            |               |                |              |
| 3        |            |               |                |                |            |               |                |              |
| 4        |            |               |                |                |            |               |                |              |
| 5        |            |               |                |                |            |               |                |              |
| 6        |            |               |                |                |            |               |                |              |
| 7        |            |               |                |                |            |               |                |              |
| 8        |            |               |                |                |            |               |                |              |

| **Function** | **Mode** | **Cause** | **Local effect** | **End effect** | **Safeguards** | **Evidence** | **Criticality** | **Action** |
|--------------|----------|-----------|------------------|----------------|----------------|--------------|-----------------|------------|
|              |          |           |                  |                |                |              |                 |            |
|              |          |           |                  |                |                |              |                 |            |
|              |          |           |                  |                |                |              |                 |            |
|              |          |           |                  |                |                |              |                 |            |
|              |          |           |                  |                |                |              |                 |            |
|              |          |           |                  |                |                |              |                 |            |
|              |          |           |                  |                |                |              |                 |            |

# Appendix C - References

| **Reference**                    | **Use**                                                                |
|----------------------------------|------------------------------------------------------------------------|
| IEC 60812:2018                   | FMEA/FMECA planning, execution, documentation and maintenance context. |
| IEC 31010:2019                   | Selection and application of risk-assessment techniques.               |
| NIST SP 800-30 Rev. 1            | Threat-oriented risk-assessment comparison.                            |
| AIDCF Manifesto v1.0             | Doctrine, evidence, UNKNOWN and critical-gate principles.              |
| AIDCF Core Conceptual Model v1.0 | Canonical failure-propagation concepts.                                |
| AIDCF-003 v1.0                   | Entities, dependencies, states, capacity and fault domains.            |
| ASHRAE TC 9.9 guidance           | Data-centre thermal and equipment-environment context.                 |

# Appendix D - Review and change record

| **Review role**           | **Status**      | **Focus**                                                            |
|---------------------------|-----------------|----------------------------------------------------------------------|
| Methodology author        | Draft completed | Discipline validity, boundaries, evidence and publication readiness. |
| Reliability/FMEA          | Pending         | Discipline validity, boundaries, evidence and publication readiness. |
| Data-centre architecture  | Pending         | Discipline validity, boundaries, evidence and publication readiness. |
| Electrical                | Pending         | Discipline validity, boundaries, evidence and publication readiness. |
| Mechanical/liquid cooling | Pending         | Discipline validity, boundaries, evidence and publication readiness. |
| Fire/life safety          | Pending         | Discipline validity, boundaries, evidence and publication readiness. |
| Physical security         | Pending         | Discipline validity, boundaries, evidence and publication readiness. |
| AI compute/HPC            | Pending         | Discipline validity, boundaries, evidence and publication readiness. |
| Storage                   | Pending         | Discipline validity, boundaries, evidence and publication readiness. |
| Network/fabric            | Pending         | Discipline validity, boundaries, evidence and publication readiness. |
| OT security               | Pending         | Discipline validity, boundaries, evidence and publication readiness. |
| Operations/recovery       | Pending         | Discipline validity, boundaries, evidence and publication readiness. |
| Ontology/graph            | Pending         | Discipline validity, boundaries, evidence and publication readiness. |
| Legal/IP                  | Pending         | Discipline validity, boundaries, evidence and publication readiness. |
| Public release            | Not approved    | Mandatory gates closed.                                              |

| **Version** | **Status**              | **Summary**                                       |
|-------------|-------------------------|---------------------------------------------------|
| 0.1         | Architecture draft      | Ontology and doctrine.                            |
| 0.5         | Integrated draft        | Domain catalogues, scenarios and graph semantics. |
| 1.0         | Controlled-review draft | Comprehensive baseline for expert review.         |

## Final doctrine

Do not ask only whether a control exists or a component is redundant. Ask what the capability requires, what can disturb the required conditions, how functions can fail, where effects propagate, which barriers remain available in the applicable state, what evidence demonstrates their behaviour, what consequence remains, how recovery is achieved and what is still UNKNOWN.
