> Markdown edition. Source: [AIDCF-013_AI_Data_Centre_Assurance_Reference_Architecture_v1.0.docx](AIDCF-013_AI_Data_Centre_Assurance_Reference_Architecture_v1.0.docx) · PDF: [AIDCF-013_AI_Data_Centre_Assurance_Reference_Architecture_v1.0.pdf](AIDCF-013_AI_Data_Centre_Assurance_Reference_Architecture_v1.0.pdf)

**AIDCF**

**AI Data Centre Facilities Assurance Framework**

**AI DATA CENTRE ASSURANCE  
REFERENCE ARCHITECTURE**

**Version 1.0**

**  
A capability-centred, system-of-systems architecture connecting AI service outcomes to facilities, engineered infrastructure, compute platforms, operations, evidence, failure paths, critical gates and accountable decisions**

Artifact ID: AIDCF-ARA-001  
Status: Draft for controlled review  
Author: Siva Sethumadhavan  
Depends on: AIDCF-003 through AIDCF-012

**  
Model the capability. Expose the dependency. Trace the failure. Verify the safeguard. Preserve uncertainty. Bound the decision.**

# Document control

**AIDCF-013 bridges the AIDCF standards stack and deployable assurance implementations.**

| **Element**     | **Architecture requirement**                                                                                                                     |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Purpose         | Define layers, viewpoints, entities, systems, interfaces, patterns, evidence points, failure paths and graph mappings.                           |
| Primary subject | Defined AI Capability Instance and required Service Outcomes.                                                                                    |
| Scope           | Site, physical, power, thermal, environment, compute, storage, network, operations, resilience, supply chain, security, evidence and governance. |
| Uses            | Assessment scoping, AITG graphs, digital twins, schemas, controls, evidence, dashboards and profiles.                                            |
| Boundary        | Not a vendor design, engineering code, operating procedure, certification or testing authority.                                                  |
| Safety          | No switching, intrusion or disruption is authorised.                                                                                             |

# Executive thesis

**An AI data centre is represented as a capability-supporting system of systems. A conformant architecture traces Service Outcomes through functions, systems, assets, interfaces, resources, dependencies, states, failure paths and safeguards to evidence, controls, critical gates and bounded decisions.**

## Canonical chain

**Capability -\> Outcome -\> Function -\> Service Chain -\> System -\> Asset/Interface/Resource -\> Dependency/Fault Domain -\> State -\> Failure -\> Safeguard -\> Evidence -\> Control -\> Finding/UNKNOWN -\> Gate -\> Score -\> Decision -\> Report/Reassessment**

# Part I - Authority and scope

**AIDCF-013 organises existing AIDCF objects into deployable views and patterns.**

| **Element**            | **Architecture requirement**                                                                          |
|------------------------|-------------------------------------------------------------------------------------------------------|
| Semantic authority     | AIDCF-003 owns canonical entities and relationships.                                                  |
| Failure authority      | AIDCF-004 owns threat, hazard and propagation semantics.                                              |
| Integration authority  | AIDCF-005 governs AIDCF-AITG handoffs.                                                                |
| Assurance authority    | AIDCF-007 through AIDCF-012 govern controls, evidence, assessment, decisions, programs and reporting. |
| Vendor neutrality      | Functions and requirements precede products.                                                          |
| No universal blueprint | Tailor by capability, site, technology, state, consequence and decision.                              |
| Change control         | Extensions cannot silently weaken the baseline.                                                       |

# Part II - Architecture principles

**Principles constrain all implementations.**

| **Element**             | **Architecture requirement**                                             |
|-------------------------|--------------------------------------------------------------------------|
| Capability first        | Start from service outcomes, not inventory.                              |
| Function before product | Keep requirements vendor-neutral.                                        |
| System of systems       | Connect facility, digital, operational and external services.            |
| Dependency explicitness | Record direct, indirect, shared, external and recovery reliance.         |
| State awareness         | Model normal, maintenance, degraded, emergency, recovery and transition. |
| Failure informed        | Represent credible paths and propagation.                                |
| Fault-domain clarity    | Substantiate independence and common modes.                              |
| Evidence attachment     | Attach evidence or UNKNOWN to material assertions.                       |
| Gate readiness          | Design evidence paths for applicable gates.                              |
| Human approval          | Automation may propose; accountable review approves.                     |

# Part III - Conformance levels

**Progressive conformance retains common semantics.**

| **Element** | **Architecture requirement**                       |
|-------------|----------------------------------------------------|
| AR0         | Vocabulary aligned.                                |
| AR1         | Capability and outcomes mapped.                    |
| AR2         | Infrastructure mapped.                             |
| AR3         | Dependency and fault domains complete.             |
| AR4         | Controls, evidence, scenarios and gates attached.  |
| AR5         | Graph conformant and versioned.                    |
| AR6         | Continuing-assurance sources and triggers defined. |

# Part IV - Architecture layers

**Ten connected layers form the model.**

| **Element** | **Architecture requirement**          |
|-------------|---------------------------------------|
| L0          | Decision and governance.              |
| L1          | Capability and outcomes.              |
| L2          | Functional service chain.             |
| L3          | Logical platform.                     |
| L4          | Physical IT.                          |
| L5          | Facility engineering.                 |
| L6          | External ecosystem.                   |
| L7          | Operations and resilience.            |
| L8          | Assurance objects.                    |
| L9          | Decision, reporting and reassessment. |

# Part V - Required viewpoints

**Each view is a projection of one controlled model.**

| **Element**      | **Architecture requirement**                         |
|------------------|------------------------------------------------------|
| Capability       | Required when material; omission requires rationale. |
| Functional       | Required when material; omission requires rationale. |
| System           | Required when material; omission requires rationale. |
| Physical         | Required when material; omission requires rationale. |
| Dependency       | Required when material; omission requires rationale. |
| Fault-domain     | Required when material; omission requires rationale. |
| State            | Required when material; omission requires rationale. |
| Capacity         | Required when material; omission requires rationale. |
| Failure          | Required when material; omission requires rationale. |
| Safeguard        | Required when material; omission requires rationale. |
| Control/evidence | Required when material; omission requires rationale. |
| Decision         | Required when material; omission requires rationale. |
| Graph            | Required when material; omission requires rationale. |
| Reporting        | Required when material; omission requires rationale. |

# Part VI - Capability architecture

**The model is anchored to a precise capability record.**

| **Element**                             | **Architecture requirement** |
|-----------------------------------------|------------------------------|
| stable identity/owner/lifecycle/version | Required                     |
| mission and users                       | Required                     |
| workload model                          | Required                     |
| demand model                            | Required                     |
| Service Outcomes                        | Required                     |
| tolerances                              | Required                     |
| criticality                             | Required                     |
| architecture baseline                   | Required                     |
| scope/boundary                          | Required                     |
| reassessment triggers                   | Required                     |

# Service Outcome specification

**Every outcome is an assessable object.**

| **Element**           | **Architecture requirement** |
|-----------------------|------------------------------|
| outcomeId             | Required                     |
| measurable statement  | Required                     |
| conditions/state      | Required                     |
| tolerance/duration    | Required                     |
| critical functions    | Required                     |
| dependencies          | Required                     |
| safeguards            | Required                     |
| evidence floor        | Required                     |
| critical gates        | Required                     |
| owner                 | Required                     |
| reassessment triggers | Required                     |

# Reference Service Chain - Training

**ingest -\> storage -\> fabric -\> accelerators -\> checkpoint -\> output**

| **Element**      | **Architecture requirement**                                             |
|------------------|--------------------------------------------------------------------------|
| Flow             | ingest -\> storage -\> fabric -\> accelerators -\> checkpoint -\> output |
| Objects          | Functions, systems, interfaces, resources, states, owners and providers. |
| Dependencies     | Internal, shared, external and recovery.                                 |
| Failure analysis | Modes, paths, safeguards, residual state and recovery.                   |
| Assurance        | Controls, evidence, findings, UNKNOWN, gates and decisions.              |
| Boundary         | Excluded services remain explicit.                                       |
| Validation       | Reconcile logical, physical and observed states.                         |

# Reference Service Chain - Inference

**ingress -\> route -\> preprocess -\> model service -\> compute -\> response**

| **Element**      | **Architecture requirement**                                                |
|------------------|-----------------------------------------------------------------------------|
| Flow             | ingress -\> route -\> preprocess -\> model service -\> compute -\> response |
| Objects          | Functions, systems, interfaces, resources, states, owners and providers.    |
| Dependencies     | Internal, shared, external and recovery.                                    |
| Failure analysis | Modes, paths, safeguards, residual state and recovery.                      |
| Assurance        | Controls, evidence, findings, UNKNOWN, gates and decisions.                 |
| Boundary         | Excluded services remain explicit.                                          |
| Validation       | Reconcile logical, physical and observed states.                            |

# Reference Service Chain - Fine-tuning

**dataset -\> transfer -\> training -\> checkpoint -\> evaluation -\> registry**

| **Element**      | **Architecture requirement**                                                 |
|------------------|------------------------------------------------------------------------------|
| Flow             | dataset -\> transfer -\> training -\> checkpoint -\> evaluation -\> registry |
| Objects          | Functions, systems, interfaces, resources, states, owners and providers.     |
| Dependencies     | Internal, shared, external and recovery.                                     |
| Failure analysis | Modes, paths, safeguards, residual state and recovery.                       |
| Assurance        | Controls, evidence, findings, UNKNOWN, gates and decisions.                  |
| Boundary         | Excluded services remain explicit.                                           |
| Validation       | Reconcile logical, physical and observed states.                             |

# Reference Service Chain - Sovereign

**authorised ingress -\> controlled processing -\> protected storage -\> approved egress**

| **Element**      | **Architecture requirement**                                                           |
|------------------|----------------------------------------------------------------------------------------|
| Flow             | authorised ingress -\> controlled processing -\> protected storage -\> approved egress |
| Objects          | Functions, systems, interfaces, resources, states, owners and providers.               |
| Dependencies     | Internal, shared, external and recovery.                                               |
| Failure analysis | Modes, paths, safeguards, residual state and recovery.                                 |
| Assurance        | Controls, evidence, findings, UNKNOWN, gates and decisions.                            |
| Boundary         | Excluded services remain explicit.                                                     |
| Validation       | Reconcile logical, physical and observed states.                                       |

# Reference Service Chain - Shared platform

**tenant intake -\> scheduling -\> shared infrastructure -\> monitoring**

| **Element**      | **Architecture requirement**                                             |
|------------------|--------------------------------------------------------------------------|
| Flow             | tenant intake -\> scheduling -\> shared infrastructure -\> monitoring    |
| Objects          | Functions, systems, interfaces, resources, states, owners and providers. |
| Dependencies     | Internal, shared, external and recovery.                                 |
| Failure analysis | Modes, paths, safeguards, residual state and recovery.                   |
| Assurance        | Controls, evidence, findings, UNKNOWN, gates and decisions.              |
| Boundary         | Excluded services remain explicit.                                       |
| Validation       | Reconcile logical, physical and observed states.                         |

# Reference Service Chain - Recovery

**detection -\> decision -\> containment -\> alternate capacity -\> restore -\> validate**

| **Element**      | **Architecture requirement**                                                           |
|------------------|----------------------------------------------------------------------------------------|
| Flow             | detection -\> decision -\> containment -\> alternate capacity -\> restore -\> validate |
| Objects          | Functions, systems, interfaces, resources, states, owners and providers.               |
| Dependencies     | Internal, shared, external and recovery.                                               |
| Failure analysis | Modes, paths, safeguards, residual state and recovery.                                 |
| Assurance        | Controls, evidence, findings, UNKNOWN, gates and decisions.                            |
| Boundary         | Excluded services remain explicit.                                                     |
| Validation       | Reconcile logical, physical and observed states.                                       |

# GOV Domain Reference Architecture - Governance

**Canonical profile for governance.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | authority; ownership; policy; review                                                        |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | charters; decisions                                                                         |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-13; CG-14                                                                                |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# CAP Domain Reference Architecture - Capability

**Canonical profile for capability.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | capability; workload; outcome; demand; envelope                                             |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | register; SLO; plan                                                                         |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-01; CG-02                                                                                |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# DEP Domain Reference Architecture - Dependencies

**Canonical profile for dependencies.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | dependency; provider; shared service; concentration                                         |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | graph; contract; route                                                                      |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-03; CG-12                                                                                |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# PHY Domain Reference Architecture - Physical

**Canonical profile for physical.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | site; building; room; zone; rack; barrier                                                   |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | drawing; inspection; access                                                                 |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-02; CG-04                                                                                |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# POW Domain Reference Architecture - Power

**Canonical profile for power.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | utility; transformer; UPS; generator; distribution                                          |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | SLD; telemetry; tests                                                                       |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-05                                                                                       |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# THM Domain Reference Architecture - Thermal

**Canonical profile for thermal.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | chiller; pump; CRAH; CDU; loop; leak detection                                              |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | P&ID; telemetry; tests                                                                      |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-06                                                                                       |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# ENV Domain Reference Architecture - Environment

**Canonical profile for environment.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | sensor; meter; water; waste; hazard zone                                                    |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | telemetry; permits                                                                          |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-02; CG-04                                                                                |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# CMP Domain Reference Architecture - Compute

**Canonical profile for compute.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | accelerator; host; rack; cluster; scheduler; firmware                                       |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | topology; health; tests                                                                     |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-08                                                                                       |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# STO Domain Reference Architecture - Storage

**Canonical profile for storage.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | tier; controller; metadata; replication; checkpoint                                         |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | integrity; restore                                                                          |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-08; CG-10                                                                                |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# NET Domain Reference Architecture - Network

**Canonical profile for network.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | fabric; switch; optic; cable; OOB; time                                                     |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | topology; telemetry                                                                         |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-08                                                                                       |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# OPS Domain Reference Architecture - Operations

**Canonical profile for operations.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | operator; procedure; alarm; incident; change                                                |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | work orders; tickets                                                                        |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-07; CG-13; CG-14                                                                         |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# RES Domain Reference Architecture - Resilience

**Canonical profile for resilience.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | fault domain; plan; exercise; crisis team                                                   |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | scenario; exercise                                                                          |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-09; CG-10                                                                                |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# SUP Domain Reference Architecture - Supply Chain

**Canonical profile for supply chain.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | supplier; OEM; spare; support; update source                                                |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | contract; provenance                                                                        |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-03; CG-13                                                                                |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# SEC Domain Reference Architecture - Security

**Canonical profile for security.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | identity; privilege; zone; gateway; control plane                                           |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | config; logs; tests                                                                         |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-07; CG-15                                                                                |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# EVA Domain Reference Architecture - Evidence/Assurance

**Canonical profile for evidence/assurance.**

| **Element**    | **Architecture requirement**                                                                |
|----------------|---------------------------------------------------------------------------------------------|
| Objects        | evidence; assertion; result; finding; gate; decision                                        |
| Relationships  | IMPLEMENTS; CONNECTS_TO; DEPENDS_ON; LOCATED_IN; CONTROLLED_BY; MONITORED_BY; PROTECTED_BY. |
| Boundary       | Owned, operated, third-party, shared and excluded.                                          |
| States         | Normal, maintenance, degraded, emergency, recovery and transition.                          |
| Capacity       | Rated, available, reserved, consumed, headroom and constraint.                              |
| Fault domains  | Redundancy, common modes and containment.                                                   |
| Evidence       | manifest; workpaper                                                                         |
| Controls       | Applicable AIDCF-007 controls.                                                              |
| Critical gates | CG-11; CG-12                                                                                |
| Outputs        | View, dependency map, scenarios and evidence points.                                        |
| Reassessment   | Configuration, capacity, provider, incident or evidence change.                             |

# System Architecture Card - Incoming power

**Reusable record for incoming power.**

| **Element**           | **Architecture requirement**                          |
|-----------------------|-------------------------------------------------------|
| Purpose               | Required function and linked outcomes.                |
| Components/interfaces | utility; feeders; protection; transfer                |
| Capacity/envelope     | Demand, available capacity, headroom and constraints. |
| States                | Normal through transition.                            |
| Dependencies          | Upstream, shared, external and recovery.              |
| Fault domains         | Independence and common modes.                        |
| Failure               | Modes and propagation.                                |
| Safeguards            | Prevent, detect, contain, correct and recover.        |
| Evidence              | Design, configuration, operation and validation.      |
| Controls/gates        | Applicable controls and gates.                        |
| Owners                | Design, operation, maintenance and evidence.          |
| Triggers              | Versioned reassessment events.                        |

# System Architecture Card - Generation/fuel

**Reusable record for generation/fuel.**

| **Element**           | **Architecture requirement**                          |
|-----------------------|-------------------------------------------------------|
| Purpose               | Required function and linked outcomes.                |
| Components/interfaces | generators; starting; fuel; controls                  |
| Capacity/envelope     | Demand, available capacity, headroom and constraints. |
| States                | Normal through transition.                            |
| Dependencies          | Upstream, shared, external and recovery.              |
| Fault domains         | Independence and common modes.                        |
| Failure               | Modes and propagation.                                |
| Safeguards            | Prevent, detect, contain, correct and recover.        |
| Evidence              | Design, configuration, operation and validation.      |
| Controls/gates        | Applicable controls and gates.                        |
| Owners                | Design, operation, maintenance and evidence.          |
| Triggers              | Versioned reassessment events.                        |

# System Architecture Card - UPS/storage

**Reusable record for ups/storage.**

| **Element**           | **Architecture requirement**                          |
|-----------------------|-------------------------------------------------------|
| Purpose               | Required function and linked outcomes.                |
| Components/interfaces | inverter; bypass; batteries                           |
| Capacity/envelope     | Demand, available capacity, headroom and constraints. |
| States                | Normal through transition.                            |
| Dependencies          | Upstream, shared, external and recovery.              |
| Fault domains         | Independence and common modes.                        |
| Failure               | Modes and propagation.                                |
| Safeguards            | Prevent, detect, contain, correct and recover.        |
| Evidence              | Design, configuration, operation and validation.      |
| Controls/gates        | Applicable controls and gates.                        |
| Owners                | Design, operation, maintenance and evidence.          |
| Triggers              | Versioned reassessment events.                        |

# System Architecture Card - Distribution

**Reusable record for distribution.**

| **Element**           | **Architecture requirement**                          |
|-----------------------|-------------------------------------------------------|
| Purpose               | Required function and linked outcomes.                |
| Components/interfaces | switchgear; busway; PDU; protection                   |
| Capacity/envelope     | Demand, available capacity, headroom and constraints. |
| States                | Normal through transition.                            |
| Dependencies          | Upstream, shared, external and recovery.              |
| Fault domains         | Independence and common modes.                        |
| Failure               | Modes and propagation.                                |
| Safeguards            | Prevent, detect, contain, correct and recover.        |
| Evidence              | Design, configuration, operation and validation.      |
| Controls/gates        | Applicable controls and gates.                        |
| Owners                | Design, operation, maintenance and evidence.          |
| Triggers              | Versioned reassessment events.                        |

# System Architecture Card - Air cooling

**Reusable record for air cooling.**

| **Element**           | **Architecture requirement**                          |
|-----------------------|-------------------------------------------------------|
| Purpose               | Required function and linked outcomes.                |
| Components/interfaces | chiller; tower; pump; CRAH; containment               |
| Capacity/envelope     | Demand, available capacity, headroom and constraints. |
| States                | Normal through transition.                            |
| Dependencies          | Upstream, shared, external and recovery.              |
| Fault domains         | Independence and common modes.                        |
| Failure               | Modes and propagation.                                |
| Safeguards            | Prevent, detect, contain, correct and recover.        |
| Evidence              | Design, configuration, operation and validation.      |
| Controls/gates        | Applicable controls and gates.                        |
| Owners                | Design, operation, maintenance and evidence.          |
| Triggers              | Versioned reassessment events.                        |

# System Architecture Card - Liquid cooling

**Reusable record for liquid cooling.**

| **Element**           | **Architecture requirement**                          |
|-----------------------|-------------------------------------------------------|
| Purpose               | Required function and linked outcomes.                |
| Components/interfaces | CDU; loops; manifolds; fluid; leak detection          |
| Capacity/envelope     | Demand, available capacity, headroom and constraints. |
| States                | Normal through transition.                            |
| Dependencies          | Upstream, shared, external and recovery.              |
| Fault domains         | Independence and common modes.                        |
| Failure               | Modes and propagation.                                |
| Safeguards            | Prevent, detect, contain, correct and recover.        |
| Evidence              | Design, configuration, operation and validation.      |
| Controls/gates        | Applicable controls and gates.                        |
| Owners                | Design, operation, maintenance and evidence.          |
| Triggers              | Versioned reassessment events.                        |

# System Architecture Card - Compute cluster

**Reusable record for compute cluster.**

| **Element**           | **Architecture requirement**                          |
|-----------------------|-------------------------------------------------------|
| Purpose               | Required function and linked outcomes.                |
| Components/interfaces | nodes; accelerators; scheduler; firmware              |
| Capacity/envelope     | Demand, available capacity, headroom and constraints. |
| States                | Normal through transition.                            |
| Dependencies          | Upstream, shared, external and recovery.              |
| Fault domains         | Independence and common modes.                        |
| Failure               | Modes and propagation.                                |
| Safeguards            | Prevent, detect, contain, correct and recover.        |
| Evidence              | Design, configuration, operation and validation.      |
| Controls/gates        | Applicable controls and gates.                        |
| Owners                | Design, operation, maintenance and evidence.          |
| Triggers              | Versioned reassessment events.                        |

# System Architecture Card - Storage platform

**Reusable record for storage platform.**

| **Element**           | **Architecture requirement**                          |
|-----------------------|-------------------------------------------------------|
| Purpose               | Required function and linked outcomes.                |
| Components/interfaces | tiers; controllers; metadata; replication; checkpoint |
| Capacity/envelope     | Demand, available capacity, headroom and constraints. |
| States                | Normal through transition.                            |
| Dependencies          | Upstream, shared, external and recovery.              |
| Fault domains         | Independence and common modes.                        |
| Failure               | Modes and propagation.                                |
| Safeguards            | Prevent, detect, contain, correct and recover.        |
| Evidence              | Design, configuration, operation and validation.      |
| Controls/gates        | Applicable controls and gates.                        |
| Owners                | Design, operation, maintenance and evidence.          |
| Triggers              | Versioned reassessment events.                        |

# System Architecture Card - Network fabrics

**Reusable record for network fabrics.**

| **Element**           | **Architecture requirement**                          |
|-----------------------|-------------------------------------------------------|
| Purpose               | Required function and linked outcomes.                |
| Components/interfaces | scale-up; scale-out; service; storage; OOB; optics    |
| Capacity/envelope     | Demand, available capacity, headroom and constraints. |
| States                | Normal through transition.                            |
| Dependencies          | Upstream, shared, external and recovery.              |
| Fault domains         | Independence and common modes.                        |
| Failure               | Modes and propagation.                                |
| Safeguards            | Prevent, detect, contain, correct and recover.        |
| Evidence              | Design, configuration, operation and validation.      |
| Controls/gates        | Applicable controls and gates.                        |
| Owners                | Design, operation, maintenance and evidence.          |
| Triggers              | Versioned reassessment events.                        |

# System Architecture Card - BMS/EPMS

**Reusable record for bms/epms.**

| **Element**           | **Architecture requirement**                          |
|-----------------------|-------------------------------------------------------|
| Purpose               | Required function and linked outcomes.                |
| Components/interfaces | sensor; controller; gateway; HMI; historian           |
| Capacity/envelope     | Demand, available capacity, headroom and constraints. |
| States                | Normal through transition.                            |
| Dependencies          | Upstream, shared, external and recovery.              |
| Fault domains         | Independence and common modes.                        |
| Failure               | Modes and propagation.                                |
| Safeguards            | Prevent, detect, contain, correct and recover.        |
| Evidence              | Design, configuration, operation and validation.      |
| Controls/gates        | Applicable controls and gates.                        |
| Owners                | Design, operation, maintenance and evidence.          |
| Triggers              | Versioned reassessment events.                        |

# System Architecture Card - Operations centre

**Reusable record for operations centre.**

| **Element**           | **Architecture requirement**                          |
|-----------------------|-------------------------------------------------------|
| Purpose               | Required function and linked outcomes.                |
| Components/interfaces | people; monitoring; work; incident; change            |
| Capacity/envelope     | Demand, available capacity, headroom and constraints. |
| States                | Normal through transition.                            |
| Dependencies          | Upstream, shared, external and recovery.              |
| Fault domains         | Independence and common modes.                        |
| Failure               | Modes and propagation.                                |
| Safeguards            | Prevent, detect, contain, correct and recover.        |
| Evidence              | Design, configuration, operation and validation.      |
| Controls/gates        | Applicable controls and gates.                        |
| Owners                | Design, operation, maintenance and evidence.          |
| Triggers              | Versioned reassessment events.                        |

# System Architecture Card - Provider ecosystem

**Reusable record for provider ecosystem.**

| **Element**           | **Architecture requirement**                          |
|-----------------------|-------------------------------------------------------|
| Purpose               | Required function and linked outcomes.                |
| Components/interfaces | utility; telco; water; fuel; OEM; logistics           |
| Capacity/envelope     | Demand, available capacity, headroom and constraints. |
| States                | Normal through transition.                            |
| Dependencies          | Upstream, shared, external and recovery.              |
| Fault domains         | Independence and common modes.                        |
| Failure               | Modes and propagation.                                |
| Safeguards            | Prevent, detect, contain, correct and recover.        |
| Evidence              | Design, configuration, operation and validation.      |
| Controls/gates        | Applicable controls and gates.                        |
| Owners                | Design, operation, maintenance and evidence.          |
| Triggers              | Versioned reassessment events.                        |

# Interface Contract - Electrical

**Minimum contract for electrical interfaces.**

| **Element**              | **Architecture requirement** |
|--------------------------|------------------------------|
| interfaceId/version      | Required                     |
| endpoints/purpose        | Required                     |
| properties/units         | Required                     |
| states/transitions       | Required                     |
| capacity/performance     | Required                     |
| authority/change rights  | Required                     |
| monitoring/source health | Required                     |
| failure/safe state       | Required                     |
| evidence                 | Required                     |
| controls/gates           | Required                     |
| reassessment             | Required                     |

# Interface Contract - Thermal

**Minimum contract for thermal interfaces.**

| **Element**              | **Architecture requirement** |
|--------------------------|------------------------------|
| interfaceId/version      | Required                     |
| endpoints/purpose        | Required                     |
| properties/units         | Required                     |
| states/transitions       | Required                     |
| capacity/performance     | Required                     |
| authority/change rights  | Required                     |
| monitoring/source health | Required                     |
| failure/safe state       | Required                     |
| evidence                 | Required                     |
| controls/gates           | Required                     |
| reassessment             | Required                     |

# Interface Contract - Fluid

**Minimum contract for fluid interfaces.**

| **Element**              | **Architecture requirement** |
|--------------------------|------------------------------|
| interfaceId/version      | Required                     |
| endpoints/purpose        | Required                     |
| properties/units         | Required                     |
| states/transitions       | Required                     |
| capacity/performance     | Required                     |
| authority/change rights  | Required                     |
| monitoring/source health | Required                     |
| failure/safe state       | Required                     |
| evidence                 | Required                     |
| controls/gates           | Required                     |
| reassessment             | Required                     |

# Interface Contract - Network

**Minimum contract for network interfaces.**

| **Element**              | **Architecture requirement** |
|--------------------------|------------------------------|
| interfaceId/version      | Required                     |
| endpoints/purpose        | Required                     |
| properties/units         | Required                     |
| states/transitions       | Required                     |
| capacity/performance     | Required                     |
| authority/change rights  | Required                     |
| monitoring/source health | Required                     |
| failure/safe state       | Required                     |
| evidence                 | Required                     |
| controls/gates           | Required                     |
| reassessment             | Required                     |

# Interface Contract - Management

**Minimum contract for management interfaces.**

| **Element**              | **Architecture requirement** |
|--------------------------|------------------------------|
| interfaceId/version      | Required                     |
| endpoints/purpose        | Required                     |
| properties/units         | Required                     |
| states/transitions       | Required                     |
| capacity/performance     | Required                     |
| authority/change rights  | Required                     |
| monitoring/source health | Required                     |
| failure/safe state       | Required                     |
| evidence                 | Required                     |
| controls/gates           | Required                     |
| reassessment             | Required                     |

# Interface Contract - Data

**Minimum contract for data interfaces.**

| **Element**              | **Architecture requirement** |
|--------------------------|------------------------------|
| interfaceId/version      | Required                     |
| endpoints/purpose        | Required                     |
| properties/units         | Required                     |
| states/transitions       | Required                     |
| capacity/performance     | Required                     |
| authority/change rights  | Required                     |
| monitoring/source health | Required                     |
| failure/safe state       | Required                     |
| evidence                 | Required                     |
| controls/gates           | Required                     |
| reassessment             | Required                     |

# Interface Contract - Physical

**Minimum contract for physical interfaces.**

| **Element**              | **Architecture requirement** |
|--------------------------|------------------------------|
| interfaceId/version      | Required                     |
| endpoints/purpose        | Required                     |
| properties/units         | Required                     |
| states/transitions       | Required                     |
| capacity/performance     | Required                     |
| authority/change rights  | Required                     |
| monitoring/source health | Required                     |
| failure/safe state       | Required                     |
| evidence                 | Required                     |
| controls/gates           | Required                     |
| reassessment             | Required                     |

# Interface Contract - Operational handoff

**Minimum contract for operational handoff interfaces.**

| **Element**              | **Architecture requirement** |
|--------------------------|------------------------------|
| interfaceId/version      | Required                     |
| endpoints/purpose        | Required                     |
| properties/units         | Required                     |
| states/transitions       | Required                     |
| capacity/performance     | Required                     |
| authority/change rights  | Required                     |
| monitoring/source health | Required                     |
| failure/safe state       | Required                     |
| evidence                 | Required                     |
| controls/gates           | Required                     |
| reassessment             | Required                     |

# Interface Contract - Provider

**Minimum contract for provider interfaces.**

| **Element**              | **Architecture requirement** |
|--------------------------|------------------------------|
| interfaceId/version      | Required                     |
| endpoints/purpose        | Required                     |
| properties/units         | Required                     |
| states/transitions       | Required                     |
| capacity/performance     | Required                     |
| authority/change rights  | Required                     |
| monitoring/source health | Required                     |
| failure/safe state       | Required                     |
| evidence                 | Required                     |
| controls/gates           | Required                     |
| reassessment             | Required                     |

# Interface Contract - Assurance

**Minimum contract for assurance interfaces.**

| **Element**              | **Architecture requirement** |
|--------------------------|------------------------------|
| interfaceId/version      | Required                     |
| endpoints/purpose        | Required                     |
| properties/units         | Required                     |
| states/transitions       | Required                     |
| capacity/performance     | Required                     |
| authority/change rights  | Required                     |
| monitoring/source health | Required                     |
| failure/safe state       | Required                     |
| evidence                 | Required                     |
| controls/gates           | Required                     |
| reassessment             | Required                     |

# Reference Pattern - Single-site training facility

**Implementation pattern for single-site training facility.**

| **Element**  | **Architecture requirement**                                                          |
|--------------|---------------------------------------------------------------------------------------|
| Question     | Can the pattern support declared outcomes in defined states?                          |
| Boundary     | Included and external systems/providers.                                              |
| Views        | Capability, system, dependency, fault domain, state, capacity, failure and assurance. |
| Evidence     | Architecture, configuration, operation, changes and validation.                       |
| Gates        | Derived from material outcomes and dependencies.                                      |
| UNKNOWN      | Unverified shared/external reliance remains visible.                                  |
| AITG         | Reviewed native objects and handoffs.                                                 |
| Reassessment | Pattern-specific change, incident and expiry triggers.                                |

# Reference Pattern - Dual-site capability

**Implementation pattern for dual-site capability.**

| **Element**  | **Architecture requirement**                                                          |
|--------------|---------------------------------------------------------------------------------------|
| Question     | Can the pattern support declared outcomes in defined states?                          |
| Boundary     | Included and external systems/providers.                                              |
| Views        | Capability, system, dependency, fault domain, state, capacity, failure and assurance. |
| Evidence     | Architecture, configuration, operation, changes and validation.                       |
| Gates        | Derived from material outcomes and dependencies.                                      |
| UNKNOWN      | Unverified shared/external reliance remains visible.                                  |
| AITG         | Reviewed native objects and handoffs.                                                 |
| Reassessment | Pattern-specific change, incident and expiry triggers.                                |

# Reference Pattern - Colocation deployment

**Implementation pattern for colocation deployment.**

| **Element**  | **Architecture requirement**                                                          |
|--------------|---------------------------------------------------------------------------------------|
| Question     | Can the pattern support declared outcomes in defined states?                          |
| Boundary     | Included and external systems/providers.                                              |
| Views        | Capability, system, dependency, fault domain, state, capacity, failure and assurance. |
| Evidence     | Architecture, configuration, operation, changes and validation.                       |
| Gates        | Derived from material outcomes and dependencies.                                      |
| UNKNOWN      | Unverified shared/external reliance remains visible.                                  |
| AITG         | Reviewed native objects and handoffs.                                                 |
| Reassessment | Pattern-specific change, incident and expiry triggers.                                |

# Reference Pattern - Hyperscale campus

**Implementation pattern for hyperscale campus.**

| **Element**  | **Architecture requirement**                                                          |
|--------------|---------------------------------------------------------------------------------------|
| Question     | Can the pattern support declared outcomes in defined states?                          |
| Boundary     | Included and external systems/providers.                                              |
| Views        | Capability, system, dependency, fault domain, state, capacity, failure and assurance. |
| Evidence     | Architecture, configuration, operation, changes and validation.                       |
| Gates        | Derived from material outcomes and dependencies.                                      |
| UNKNOWN      | Unverified shared/external reliance remains visible.                                  |
| AITG         | Reviewed native objects and handoffs.                                                 |
| Reassessment | Pattern-specific change, incident and expiry triggers.                                |

# Reference Pattern - Modular facility

**Implementation pattern for modular facility.**

| **Element**  | **Architecture requirement**                                                          |
|--------------|---------------------------------------------------------------------------------------|
| Question     | Can the pattern support declared outcomes in defined states?                          |
| Boundary     | Included and external systems/providers.                                              |
| Views        | Capability, system, dependency, fault domain, state, capacity, failure and assurance. |
| Evidence     | Architecture, configuration, operation, changes and validation.                       |
| Gates        | Derived from material outcomes and dependencies.                                      |
| UNKNOWN      | Unverified shared/external reliance remains visible.                                  |
| AITG         | Reviewed native objects and handoffs.                                                 |
| Reassessment | Pattern-specific change, incident and expiry triggers.                                |

# Reference Pattern - Liquid-cooled high-density cluster

**Implementation pattern for liquid-cooled high-density cluster.**

| **Element**  | **Architecture requirement**                                                          |
|--------------|---------------------------------------------------------------------------------------|
| Question     | Can the pattern support declared outcomes in defined states?                          |
| Boundary     | Included and external systems/providers.                                              |
| Views        | Capability, system, dependency, fault domain, state, capacity, failure and assurance. |
| Evidence     | Architecture, configuration, operation, changes and validation.                       |
| Gates        | Derived from material outcomes and dependencies.                                      |
| UNKNOWN      | Unverified shared/external reliance remains visible.                                  |
| AITG         | Reviewed native objects and handoffs.                                                 |
| Reassessment | Pattern-specific change, incident and expiry triggers.                                |

# Reference Pattern - Hybrid cloud/on-prem

**Implementation pattern for hybrid cloud/on-prem.**

| **Element**  | **Architecture requirement**                                                          |
|--------------|---------------------------------------------------------------------------------------|
| Question     | Can the pattern support declared outcomes in defined states?                          |
| Boundary     | Included and external systems/providers.                                              |
| Views        | Capability, system, dependency, fault domain, state, capacity, failure and assurance. |
| Evidence     | Architecture, configuration, operation, changes and validation.                       |
| Gates        | Derived from material outcomes and dependencies.                                      |
| UNKNOWN      | Unverified shared/external reliance remains visible.                                  |
| AITG         | Reviewed native objects and handoffs.                                                 |
| Reassessment | Pattern-specific change, incident and expiry triggers.                                |

# Reference Pattern - Sovereign AI environment

**Implementation pattern for sovereign ai environment.**

| **Element**  | **Architecture requirement**                                                          |
|--------------|---------------------------------------------------------------------------------------|
| Question     | Can the pattern support declared outcomes in defined states?                          |
| Boundary     | Included and external systems/providers.                                              |
| Views        | Capability, system, dependency, fault domain, state, capacity, failure and assurance. |
| Evidence     | Architecture, configuration, operation, changes and validation.                       |
| Gates        | Derived from material outcomes and dependencies.                                      |
| UNKNOWN      | Unverified shared/external reliance remains visible.                                  |
| AITG         | Reviewed native objects and handoffs.                                                 |
| Reassessment | Pattern-specific change, incident and expiry triggers.                                |

# Reference Pattern - Shared multi-tenant platform

**Implementation pattern for shared multi-tenant platform.**

| **Element**  | **Architecture requirement**                                                          |
|--------------|---------------------------------------------------------------------------------------|
| Question     | Can the pattern support declared outcomes in defined states?                          |
| Boundary     | Included and external systems/providers.                                              |
| Views        | Capability, system, dependency, fault domain, state, capacity, failure and assurance. |
| Evidence     | Architecture, configuration, operation, changes and validation.                       |
| Gates        | Derived from material outcomes and dependencies.                                      |
| UNKNOWN      | Unverified shared/external reliance remains visible.                                  |
| AITG         | Reviewed native objects and handoffs.                                                 |
| Reassessment | Pattern-specific change, incident and expiry triggers.                                |

# Reference Pattern - Edge inference estate

**Implementation pattern for edge inference estate.**

| **Element**  | **Architecture requirement**                                                          |
|--------------|---------------------------------------------------------------------------------------|
| Question     | Can the pattern support declared outcomes in defined states?                          |
| Boundary     | Included and external systems/providers.                                              |
| Views        | Capability, system, dependency, fault domain, state, capacity, failure and assurance. |
| Evidence     | Architecture, configuration, operation, changes and validation.                       |
| Gates        | Derived from material outcomes and dependencies.                                      |
| UNKNOWN      | Unverified shared/external reliance remains visible.                                  |
| AITG         | Reviewed native objects and handoffs.                                                 |
| Reassessment | Pattern-specific change, incident and expiry triggers.                                |

# Reference Pattern - Brownfield retrofit

**Implementation pattern for brownfield retrofit.**

| **Element**  | **Architecture requirement**                                                          |
|--------------|---------------------------------------------------------------------------------------|
| Question     | Can the pattern support declared outcomes in defined states?                          |
| Boundary     | Included and external systems/providers.                                              |
| Views        | Capability, system, dependency, fault domain, state, capacity, failure and assurance. |
| Evidence     | Architecture, configuration, operation, changes and validation.                       |
| Gates        | Derived from material outcomes and dependencies.                                      |
| UNKNOWN      | Unverified shared/external reliance remains visible.                                  |
| AITG         | Reviewed native objects and handoffs.                                                 |
| Reassessment | Pattern-specific change, incident and expiry triggers.                                |

# Reference Pattern - Recovery-capacity pool

**Implementation pattern for recovery-capacity pool.**

| **Element**  | **Architecture requirement**                                                          |
|--------------|---------------------------------------------------------------------------------------|
| Question     | Can the pattern support declared outcomes in defined states?                          |
| Boundary     | Included and external systems/providers.                                              |
| Views        | Capability, system, dependency, fault domain, state, capacity, failure and assurance. |
| Evidence     | Architecture, configuration, operation, changes and validation.                       |
| Gates        | Derived from material outcomes and dependencies.                                      |
| UNKNOWN      | Unverified shared/external reliance remains visible.                                  |
| AITG         | Reviewed native objects and handoffs.                                                 |
| Reassessment | Pattern-specific change, incident and expiry triggers.                                |

# Operating-state model

**Canonical architecture model.**

| **Element** | **Architecture requirement**  |
|-------------|-------------------------------|
| NORMAL      | Required and evidence-linked. |
| MAINTENANCE | Required and evidence-linked. |
| DEGRADED    | Required and evidence-linked. |
| EMERGENCY   | Required and evidence-linked. |
| RECOVERY    | Required and evidence-linked. |
| TRANSITION  | Required and evidence-linked. |
| UNKNOWN     | Required and evidence-linked. |

# Capacity and envelope

**Canonical architecture model.**

| **Element** | **Architecture requirement**  |
|-------------|-------------------------------|
| Demand      | Required and evidence-linked. |
| Rated       | Required and evidence-linked. |
| Available   | Required and evidence-linked. |
| Reserved    | Required and evidence-linked. |
| Consumed    | Required and evidence-linked. |
| Headroom    | Required and evidence-linked. |
| Constraint  | Required and evidence-linked. |
| Burst       | Required and evidence-linked. |
| Growth      | Required and evidence-linked. |
| UNKNOWN     | Required and evidence-linked. |

# Fault-domain model

**Canonical architecture model.**

| **Element**         | **Architecture requirement**  |
|---------------------|-------------------------------|
| FaultDomain         | Required and evidence-linked. |
| RedundancyGroup     | Required and evidence-linked. |
| IndependenceClaim   | Required and evidence-linked. |
| CommonMode          | Required and evidence-linked. |
| ContainmentBoundary | Required and evidence-linked. |
| BlastRadius         | Required and evidence-linked. |
| RecoveryDomain      | Required and evidence-linked. |
| Evidence            | Required and evidence-linked. |

# Failure-path model

**Canonical architecture model.**

| **Element**         | **Architecture requirement**  |
|---------------------|-------------------------------|
| initiating source   | Required and evidence-linked. |
| pre-state           | Required and evidence-linked. |
| failure mode        | Required and evidence-linked. |
| local effect        | Required and evidence-linked. |
| dependency edge     | Required and evidence-linked. |
| next entity         | Required and evidence-linked. |
| safeguard           | Required and evidence-linked. |
| residual state      | Required and evidence-linked. |
| outcome effect      | Required and evidence-linked. |
| evidence/confidence | Required and evidence-linked. |
| gate effect         | Required and evidence-linked. |

# Safeguard model

**Canonical architecture model.**

| **Element**     | **Architecture requirement**  |
|-----------------|-------------------------------|
| identity        | Required and evidence-linked. |
| function        | Required and evidence-linked. |
| subject         | Required and evidence-linked. |
| activation      | Required and evidence-linked. |
| authority       | Required and evidence-linked. |
| dependencies    | Required and evidence-linked. |
| state coverage  | Required and evidence-linked. |
| failure modes   | Required and evidence-linked. |
| evidence        | Required and evidence-linked. |
| control mapping | Required and evidence-linked. |

# Observability model

**Canonical architecture model.**

| **Element**     | **Architecture requirement**  |
|-----------------|-------------------------------|
| metric/event    | Required and evidence-linked. |
| source          | Required and evidence-linked. |
| subject         | Required and evidence-linked. |
| time/clock      | Required and evidence-linked. |
| state context   | Required and evidence-linked. |
| quality/gaps    | Required and evidence-linked. |
| threshold/owner | Required and evidence-linked. |
| alarm route     | Required and evidence-linked. |
| evidence use    | Required and evidence-linked. |
| blind spot      | Required and evidence-linked. |

# Evidence attachment

**Canonical architecture model.**

| **Element**      | **Architecture requirement**  |
|------------------|-------------------------------|
| assertion        | Required and evidence-linked. |
| evidence classes | Required and evidence-linked. |
| source authority | Required and evidence-linked. |
| collection       | Required and evidence-linked. |
| quality floor    | Required and evidence-linked. |
| sufficiency      | Required and evidence-linked. |
| conflict         | Required and evidence-linked. |
| UNKNOWN rule     | Required and evidence-linked. |
| retention        | Required and evidence-linked. |
| reassessment     | Required and evidence-linked. |

# Control attachment

**Canonical architecture model.**

| **Element**       | **Architecture requirement**  |
|-------------------|-------------------------------|
| controlId         | Required and evidence-linked. |
| subject           | Required and evidence-linked. |
| applicability     | Required and evidence-linked. |
| dimensions        | Required and evidence-linked. |
| methods           | Required and evidence-linked. |
| evidence          | Required and evidence-linked. |
| result/confidence | Required and evidence-linked. |
| finding/UNKNOWN   | Required and evidence-linked. |
| gates             | Required and evidence-linked. |
| reassessment      | Required and evidence-linked. |

# Critical-gate architecture

**Gate readiness is designed into the architecture.**

| **Gate** | **Architecture focus**            |
|----------|-----------------------------------|
| CG-01    | Capability/outcome definition     |
| CG-02    | Boundary/architecture integrity   |
| CG-03    | Critical dependency visibility    |
| CG-04    | Life safety/hazardous energy      |
| CG-05    | Electrical continuity             |
| CG-06    | Thermal continuity                |
| CG-07    | Control-system integrity          |
| CG-08    | Compute/storage/network integrity |
| CG-09    | Failure containment               |
| CG-10    | Recovery readiness                |
| CG-11    | Evidence sufficiency              |
| CG-12    | Critical UNKNOWN                  |
| CG-13    | Responsibility/authority          |
| CG-14    | Change control                    |
| CG-15    | Integrated digital authority      |

# Canonical graph nodes

**The graph projects the controlled architecture.**

| **Element**          | **Architecture requirement**                           |
|----------------------|--------------------------------------------------------|
| CapabilityInstance   | Stable ID, version, source, status and classification. |
| ServiceOutcome       | Stable ID, version, source, status and classification. |
| RequiredFunction     | Stable ID, version, source, status and classification. |
| InfrastructureSystem | Stable ID, version, source, status and classification. |
| AssetInstance        | Stable ID, version, source, status and classification. |
| Interface            | Stable ID, version, source, status and classification. |
| Resource             | Stable ID, version, source, status and classification. |
| Dependency           | Stable ID, version, source, status and classification. |
| FaultDomain          | Stable ID, version, source, status and classification. |
| OperatingState       | Stable ID, version, source, status and classification. |
| FailureScenario      | Stable ID, version, source, status and classification. |
| Safeguard            | Stable ID, version, source, status and classification. |
| EvidenceObject       | Stable ID, version, source, status and classification. |
| ControlAssessment    | Stable ID, version, source, status and classification. |
| GateResult           | Stable ID, version, source, status and classification. |
| AssuranceDecision    | Stable ID, version, source, status and classification. |

# Canonical graph relationships

**Edges preserve native meaning and evidence.**

| **Element**              | **Architecture requirement**                               |
|--------------------------|------------------------------------------------------------|
| SUPPORTS_OUTCOME         | Directed, scoped, versioned, reviewed and evidence-linked. |
| REQUIRES_FUNCTION        | Directed, scoped, versioned, reviewed and evidence-linked. |
| IMPLEMENTED_BY           | Directed, scoped, versioned, reviewed and evidence-linked. |
| COMPOSED_OF              | Directed, scoped, versioned, reviewed and evidence-linked. |
| CONNECTS_TO              | Directed, scoped, versioned, reviewed and evidence-linked. |
| DEPENDS_ON               | Directed, scoped, versioned, reviewed and evidence-linked. |
| SHARES_FAULT_DOMAIN_WITH | Directed, scoped, versioned, reviewed and evidence-linked. |
| LOCATED_IN               | Directed, scoped, versioned, reviewed and evidence-linked. |
| OPERATED_BY              | Directed, scoped, versioned, reviewed and evidence-linked. |
| CONTROLLED_BY            | Directed, scoped, versioned, reviewed and evidence-linked. |
| MONITORED_BY             | Directed, scoped, versioned, reviewed and evidence-linked. |
| PROTECTED_BY             | Directed, scoped, versioned, reviewed and evidence-linked. |
| EXPOSED_TO               | Directed, scoped, versioned, reviewed and evidence-linked. |
| PROPAGATES_TO            | Directed, scoped, versioned, reviewed and evidence-linked. |
| RECOVERS_THROUGH         | Directed, scoped, versioned, reviewed and evidence-linked. |
| EVIDENCED_BY             | Directed, scoped, versioned, reviewed and evidence-linked. |
| ASSESSED_BY              | Directed, scoped, versioned, reviewed and evidence-linked. |
| CONSTRAINS_GATE          | Directed, scoped, versioned, reviewed and evidence-linked. |
| LIMITS_DECISION          | Directed, scoped, versioned, reviewed and evidence-linked. |
| REPORTED_IN              | Directed, scoped, versioned, reviewed and evidence-linked. |
| SUPERSEDES               | Directed, scoped, versioned, reviewed and evidence-linked. |
| INTEGRATION_HANDOFF      | Directed, scoped, versioned, reviewed and evidence-linked. |

# Graph validation rules

**Graph implementations fail safely.**

| **ID**    | **Rule**                                                      |
|-----------|---------------------------------------------------------------|
| ARA-GV-01 | Stable IDs and lineage.                                       |
| ARA-GV-02 | Capability links outcomes.                                    |
| ARA-GV-03 | Outcomes link functions and systems.                          |
| ARA-GV-04 | Dependencies have direction, conditions and evidence.         |
| ARA-GV-05 | Redundancy links fault domains and independence evidence.     |
| ARA-GV-06 | Scenarios include states, paths, safeguards and outcomes.     |
| ARA-GV-07 | Controls link subjects and evidence.                          |
| ARA-GV-08 | Gates link mandatory evidence.                                |
| ARA-GV-09 | Decisions link scope, gates, UNKNOWN, validity and authority. |
| ARA-GV-10 | Inference cannot become fact automatically.                   |
| ARA-GV-11 | Connectivity does not imply causality/reachability/authority. |
| ARA-GV-12 | AIDCF/AITG decisions remain separate.                         |
| ARA-GV-13 | Sensitive paths are restricted.                               |
| ARA-GV-14 | Supersession preserves history.                               |

# Required work products

**Select applicable products and justify omissions.**

| **Element**                  | **Architecture requirement**                  |
|------------------------------|-----------------------------------------------|
| Capability Context Diagram   | Required when material to scope and decision. |
| Service Chain Map            | Required when material to scope and decision. |
| System Decomposition         | Required when material to scope and decision. |
| Power Assurance View         | Required when material to scope and decision. |
| Thermal/Fluid Assurance View | Required when material to scope and decision. |
| Compute/Storage/Network View | Required when material to scope and decision. |
| Dependency Graph             | Required when material to scope and decision. |
| Fault-Domain Map             | Required when material to scope and decision. |
| Operating-State Matrix       | Required when material to scope and decision. |
| Capacity Model               | Required when material to scope and decision. |
| Failure Map                  | Required when material to scope and decision. |
| Safeguard Map                | Required when material to scope and decision. |
| Control/Evidence Matrix      | Required when material to scope and decision. |
| Critical-Gate Map            | Required when material to scope and decision. |
| Decision Lineage View        | Required when material to scope and decision. |
| AITG Handoff Package         | Required when material to scope and decision. |

# Template - Capability Record

**Human and machine-readable capability record.**

| **Element**  | **Architecture requirement** |
|--------------|------------------------------|
| capabilityId |                              |
| owner        |                              |
| lifecycle    |                              |
| workload     |                              |
| outcomes     |                              |
| demand       |                              |
| criticality  |                              |
| baseline     |                              |
| scope        |                              |
| version      |                              |

# Template - Outcome Record

**Human and machine-readable outcome record.**

| **Element**  | **Architecture requirement** |
|--------------|------------------------------|
| outcomeId    |                              |
| statement    |                              |
| conditions   |                              |
| tolerance    |                              |
| functions    |                              |
| dependencies |                              |
| safeguards   |                              |
| evidence     |                              |
| gates        |                              |
| owner        |                              |

# Template - System Record

**Human and machine-readable system record.**

| **Element**  | **Architecture requirement** |
|--------------|------------------------------|
| systemId     |                              |
| purpose      |                              |
| type         |                              |
| components   |                              |
| interfaces   |                              |
| capacity     |                              |
| states       |                              |
| dependencies |                              |
| faultDomains |                              |
| owners       |                              |
| evidence     |                              |

# Template - Asset Record

**Human and machine-readable asset record.**

| **Element**   | **Architecture requirement** |
|---------------|------------------------------|
| assetId       |                              |
| class         |                              |
| location      |                              |
| configuration |                              |
| state         |                              |
| system        |                              |
| owner         |                              |
| lifecycle     |                              |
| evidence      |                              |

# Template - Interface Record

**Human and machine-readable interface record.**

| **Element** | **Architecture requirement** |
|-------------|------------------------------|
| interfaceId |                              |
| endpoints   |                              |
| type        |                              |
| purpose     |                              |
| capacity    |                              |
| authority   |                              |
| monitoring  |                              |
| failure     |                              |
| evidence    |                              |

# Template - Dependency Record

**Human and machine-readable dependency record.**

| **Element**      | **Architecture requirement** |
|------------------|------------------------------|
| dependencyId     |                              |
| source           |                              |
| target           |                              |
| type             |                              |
| conditions       |                              |
| criticality      |                              |
| substitutability |                              |
| evidence         |                              |
| confidence       |                              |

# Template - FaultDomain Record

**Human and machine-readable faultdomain record.**

| **Element**   | **Architecture requirement** |
|---------------|------------------------------|
| faultDomainId |                              |
| members       |                              |
| source        |                              |
| boundary      |                              |
| blastRadius   |                              |
| safeguards    |                              |
| evidence      |                              |

# Template - Scenario Record

**Human and machine-readable scenario record.**

| **Element**   | **Architecture requirement** |
|---------------|------------------------------|
| scenarioId    |                              |
| preState      |                              |
| source        |                              |
| steps         |                              |
| safeguards    |                              |
| residual      |                              |
| outcomeEffect |                              |
| evidence      |                              |
| confidence    |                              |

# Template - Safeguard Record

**Human and machine-readable safeguard record.**

| **Element**  | **Architecture requirement** |
|--------------|------------------------------|
| safeguardId  |                              |
| function     |                              |
| subject      |                              |
| activation   |                              |
| authority    |                              |
| dependencies |                              |
| states       |                              |
| failureModes |                              |
| evidence     |                              |

# Template - Assertion Record

**Human and machine-readable assertion record.**

| **Element** | **Architecture requirement** |
|-------------|------------------------------|
| assertionId |                              |
| subject     |                              |
| predicate   |                              |
| value       |                              |
| conditions  |                              |
| evidence    |                              |
| UNKNOWN     |                              |
| reviewer    |                              |
| status      |                              |

# Template - Snapshot Record

**Human and machine-readable snapshot record.**

| **Element**    | **Architecture requirement** |
|----------------|------------------------------|
| snapshotId     |                              |
| capability     |                              |
| scope          |                              |
| sourceVersions |                              |
| nodes          |                              |
| edges          |                              |
| validation     |                              |
| approval       |                              |
| supersedes     |                              |

# Architecture Workflow - New capability

**Need -\> outcomes -\> boundary -\> chains -\> systems -\> dependencies -\> states/capacity -\> scenarios -\> assurance -\> review.**

| **Element** | **Architecture requirement**                                                                                                       |
|-------------|------------------------------------------------------------------------------------------------------------------------------------|
| Flow        | Need -\> outcomes -\> boundary -\> chains -\> systems -\> dependencies -\> states/capacity -\> scenarios -\> assurance -\> review. |
| Entry       | Authorised question and owner.                                                                                                     |
| Outputs     | Versioned architecture, evidence and validation.                                                                                   |
| Stop        | Unsafe action, unresolved authority, source integrity or competence.                                                               |
| UNKNOWN     | Preserve unresolved facts.                                                                                                         |
| Review      | Architecture, technical, evidence and independent review.                                                                          |
| Trigger     | Reassessment and supersession.                                                                                                     |

# Architecture Workflow - Existing facility

**Baseline -\> reconcile -\> discover -\> UNKNOWN -\> map -\> validate -\> gates -\> snapshot.**

| **Element** | **Architecture requirement**                                                                 |
|-------------|----------------------------------------------------------------------------------------------|
| Flow        | Baseline -\> reconcile -\> discover -\> UNKNOWN -\> map -\> validate -\> gates -\> snapshot. |
| Entry       | Authorised question and owner.                                                               |
| Outputs     | Versioned architecture, evidence and validation.                                             |
| Stop        | Unsafe action, unresolved authority, source integrity or competence.                         |
| UNKNOWN     | Preserve unresolved facts.                                                                   |
| Review      | Architecture, technical, evidence and independent review.                                    |
| Trigger     | Reassessment and supersession.                                                               |

# Architecture Workflow - Material change

**Detect -\> impact -\> suspend stale claims -\> update -\> reassess -\> supersede.**

| **Element** | **Architecture requirement**                                                      |
|-------------|-----------------------------------------------------------------------------------|
| Flow        | Detect -\> impact -\> suspend stale claims -\> update -\> reassess -\> supersede. |
| Entry       | Authorised question and owner.                                                    |
| Outputs     | Versioned architecture, evidence and validation.                                  |
| Stop        | Unsafe action, unresolved authority, source integrity or competence.              |
| UNKNOWN     | Preserve unresolved facts.                                                        |
| Review      | Architecture, technical, evidence and independent review.                         |
| Trigger     | Reassessment and supersession.                                                    |

# Architecture Workflow - Incident

**Reconstruct path -\> affected claims/gates -\> residual state -\> recovery evidence -\> reassess.**

| **Element** | **Architecture requirement**                                                                      |
|-------------|---------------------------------------------------------------------------------------------------|
| Flow        | Reconstruct path -\> affected claims/gates -\> residual state -\> recovery evidence -\> reassess. |
| Entry       | Authorised question and owner.                                                                    |
| Outputs     | Versioned architecture, evidence and validation.                                                  |
| Stop        | Unsafe action, unresolved authority, source integrity or competence.                              |
| UNKNOWN     | Preserve unresolved facts.                                                                        |
| Review      | Architecture, technical, evidence and independent review.                                         |
| Trigger     | Reassessment and supersession.                                                                    |

# Architecture Workflow - Continuing assurance

**Register sources -\> detect drift -\> human triage -\> reassess -\> update.**

| **Element** | **Architecture requirement**                                                |
|-------------|-----------------------------------------------------------------------------|
| Flow        | Register sources -\> detect drift -\> human triage -\> reassess -\> update. |
| Entry       | Authorised question and owner.                                              |
| Outputs     | Versioned architecture, evidence and validation.                            |
| Stop        | Unsafe action, unresolved authority, source integrity or competence.        |
| UNKNOWN     | Preserve unresolved facts.                                                  |
| Review      | Architecture, technical, evidence and independent review.                   |
| Trigger     | Reassessment and supersession.                                              |

# Architecture Workflow - AITG integration

**Validate IDs -\> shared identity -\> reviewed handoff -\> lineage/security -\> federation.**

| **Element** | **Architecture requirement**                                                               |
|-------------|--------------------------------------------------------------------------------------------|
| Flow        | Validate IDs -\> shared identity -\> reviewed handoff -\> lineage/security -\> federation. |
| Entry       | Authorised question and owner.                                                             |
| Outputs     | Versioned architecture, evidence and validation.                                           |
| Stop        | Unsafe action, unresolved authority, source integrity or competence.                       |
| UNKNOWN     | Preserve unresolved facts.                                                                 |
| Review      | Architecture, technical, evidence and independent review.                                  |
| Trigger     | Reassessment and supersession.                                                             |

# Synthetic Example - Training cluster

**Illustrative only, not a real design or conclusion.**

| **Element** | **Architecture requirement**                                                              |
|-------------|-------------------------------------------------------------------------------------------|
| Context     | Shared cooling control across redundant trains.                                           |
| Treatment   | Model common mode and CG-06/07/09/10.                                                     |
| Views       | Capability, systems, dependencies, fault domains, states/capacity, failure and assurance. |
| Decision    | No positive conclusion without evidence and gate support.                                 |
| Graph       | Versioned nodes/edges with review state.                                                  |

# Synthetic Example - Colocation

**Illustrative only, not a real design or conclusion.**

| **Element** | **Architecture requirement**                                                              |
|-------------|-------------------------------------------------------------------------------------------|
| Context     | Customer IT depends on provider facility/operations.                                      |
| Treatment   | Separate boundaries and restricted evidence.                                              |
| Views       | Capability, systems, dependencies, fault domains, states/capacity, failure and assurance. |
| Decision    | No positive conclusion without evidence and gate support.                                 |
| Graph       | Versioned nodes/edges with review state.                                                  |

# Synthetic Example - Dual-site recovery

**Illustrative only, not a real design or conclusion.**

| **Element** | **Architecture requirement**                                                              |
|-------------|-------------------------------------------------------------------------------------------|
| Context     | Sites share telecom and identity service.                                                 |
| Treatment   | Model shared recovery dependencies and exercises.                                         |
| Views       | Capability, systems, dependencies, fault domains, states/capacity, failure and assurance. |
| Decision    | No positive conclusion without evidence and gate support.                                 |
| Graph       | Versioned nodes/edges with review state.                                                  |

# Synthetic Example - Brownfield retrofit

**Illustrative only, not a real design or conclusion.**

| **Element** | **Architecture requirement**                                                              |
|-------------|-------------------------------------------------------------------------------------------|
| Context     | Dense load added to legacy power/air cooling.                                             |
| Treatment   | Reconcile baseline, capacity, thermal envelope and change.                                |
| Views       | Capability, systems, dependencies, fault domains, states/capacity, failure and assurance. |
| Decision    | No positive conclusion without evidence and gate support.                                 |
| Graph       | Versioned nodes/edges with review state.                                                  |

# Conformance validation

**Conformant architectures pass semantic, structural, evidence, safety and lineage tests.**

| **ID**      | **Validation**                           |
|-------------|------------------------------------------|
| ARA-VAL-001 | Capability/outcomes explicit.            |
| ARA-VAL-002 | Functions precede products.              |
| ARA-VAL-003 | Scope/external dependencies visible.     |
| ARA-VAL-004 | Stable IDs.                              |
| ARA-VAL-005 | States/transitions represented.          |
| ARA-VAL-006 | Capacity claims conditioned/evidenced.   |
| ARA-VAL-007 | Fault domains/common modes mapped.       |
| ARA-VAL-008 | Dependencies evidenced or UNKNOWN.       |
| ARA-VAL-009 | Failure paths link safeguards/outcomes.  |
| ARA-VAL-010 | Controls attach subjects.                |
| ARA-VAL-011 | Evidence attaches assertions.            |
| ARA-VAL-012 | Gates separate from scores.              |
| ARA-VAL-013 | Decision lineage complete.               |
| ARA-VAL-014 | AIDCF/AITG semantics native.             |
| ARA-VAL-015 | Sensitive paths controlled.              |
| ARA-VAL-016 | Automation cannot approve facts.         |
| ARA-VAL-017 | Snapshots immutable/superseded.          |
| ARA-VAL-018 | Safety/engineering boundaries preserved. |

# Review and release gates

**Draft pending multidisciplinary review and pilots.**

| **Reviewer/pilot**                 | **Status** |
|------------------------------------|------------|
| Methodology author                 | Pending    |
| Data-centre architect              | Pending    |
| Electrical engineer                | Pending    |
| Mechanical/liquid-cooling engineer | Pending    |
| AI/HPC architect                   | Pending    |
| Storage architect                  | Pending    |
| Network architect                  | Pending    |
| Operations/reliability             | Pending    |
| OT/security                        | Pending    |
| Evidence specialist                | Pending    |
| Ontology/graph engineer            | Pending    |
| Safety/legal/privacy               | Pending    |
| Colocation pilot                   | Pending    |
| High-density cooling pilot         | Pending    |
| Hybrid/sovereign pilot             | Pending    |
| AITG pilot                         | Pending    |
| Public release                     | Pending    |

## Final architecture doctrine

**AIDCF-013 makes the assurance subject and dependencies explicit. It is not a vendor design, equipment checklist or substitute for licensed engineering. Where architecture or evidence is incomplete, AIDCF preserves UNKNOWN and limits assurance.**
