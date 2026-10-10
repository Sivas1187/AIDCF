> Markdown edition. Source: [AIDCF-015_Reference_Implementation_Synthetic_Dataset_and_Conformance_Pilot_v1.0.docx](AIDCF-015_Reference_Implementation_Synthetic_Dataset_and_Conformance_Pilot_v1.0.docx) · PDF: [AIDCF-015_Reference_Implementation_Synthetic_Dataset_and_Conformance_Pilot_v1.0.pdf](AIDCF-015_Reference_Implementation_Synthetic_Dataset_and_Conformance_Pilot_v1.0.pdf)

**AIDCF**

**AI Data Centre Facilities Assurance Framework**

**REFERENCE IMPLEMENTATION, SYNTHETIC DATASET  
AND CONFORMANCE PILOT**

**Version 1.0**

**  
A bounded, non-production demonstration of AIDCF architecture, machine-readable records, traceability, controls, evidence, assessment, gates, decisions, reports, events and AITG handoff**

Artifact ID: AIDCF-RIP-001  
Status: Draft for controlled review  
Author: Siva Sethumadhavan  
Depends on: AIDCF-003 through AIDCF-014  
Dataset status: Entirely synthetic and illustrative

# Document control

**Reference implementation requirement.**

| **Element**       | **Pilot specification**                                                                                                                                                |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Purpose           | Demonstrate that AIDCF can be instantiated, validated, traced, assessed, decided, reported and reassessed end to end.                                                  |
| Pilot subject     | Synthetic high-density liquid-cooled distributed AI training capability.                                                                                               |
| Outputs           | Baseline manifest, registries, schemas, semantic artifacts, synthetic records, tests, traceability graph, assessment, decision, reports and event-driven reassessment. |
| Non-production    | No record describes a real facility, provider, product deployment, engineering design or assurance conclusion.                                                         |
| Safety            | No operational switching, intrusive testing or hazardous action is authorised.                                                                                         |
| Non-certification | Technical conformance and synthetic pilot completion do not create AIDCF certification or accreditation.                                                               |

# Executive thesis

**AIDCF-015 proves the framework by exercising one bounded synthetic capability from architecture definition through machine validation, assurance evaluation, reporting and change impact. The pilot is designed to reveal gaps, contradictions and implementation burden before platform development.**

## Pilot chain

**Baseline -\> Synthetic Capability -\> Architecture -\> Dependencies -\> Scenarios -\> Safeguards -\> Controls -\> Evidence -\> Assessment -\> Findings/UNKNOWN -\> Gates -\> Scores -\> Decision -\> Reports -\> Change Event -\> Impact Analysis -\> Reassessment -\> Supersession -\> AITG Handoff**

# 1 Pilot principles

**Reference implementation requirement.**

| **Element**               | **Pilot specification** |
|---------------------------|-------------------------|
| Synthetic by construction | Required                |
| Capability first          | Required                |
| No hidden normalisation   | Required                |
| UNKNOWN preserved         | Required                |
| Gate dominance            | Required                |
| Scores contextual only    | Required                |
| Human authority           | Required                |
| Immutable snapshots       | Required                |
| Reverse traceability      | Required                |
| Security classification   | Required                |
| Reproducible validation   | Required                |
| No certification          | Required                |

# 2 Success criteria

**Reference implementation requirement.**

| **Element**                                | **Pilot specification** |
|--------------------------------------------|-------------------------|
| Baseline issues visible                    | Required                |
| Canonical IDs resolve                      | Required                |
| All required records validate              | Required                |
| Forward trace complete                     | Required                |
| Reverse trace complete                     | Required                |
| At least one material UNKNOWN              | Required                |
| At least one failed or conditional fixture | Required                |
| Gate constraints operate                   | Required                |
| Score is reproducible                      | Required                |
| Report matches decision                    | Required                |
| Change impact identifies affected records  | Required                |
| AITG handoff preserves ownership           | Required                |

# 3 Out of scope

**Reference implementation requirement.**

| **Element**                       | **Pilot specification** |
|-----------------------------------|-------------------------|
| Real engineering design           | Required                |
| Vendor selection                  | Required                |
| Live telemetry ingestion          | Required                |
| Operational testing               | Required                |
| Legal or regulatory opinion       | Required                |
| Production security accreditation | Required                |
| Real customer attestation         | Required                |
| Performance benchmarking          | Required                |
| Automated acceptance of risk      | Required                |
| Production platform SLA           | Required                |

# 4 Conformance target

**Reference implementation requirement.**

| **Element**                             | **Pilot specification** |
|-----------------------------------------|-------------------------|
| AIDCF-014 T0 vocabulary                 | Required                |
| T1 records                              | Required                |
| T2 traceability                         | Required                |
| T3 JSON validation                      | Required                |
| T4 graph validation                     | Required                |
| T5 decision-ready                       | Required                |
| T6 event and reassessment               | Required                |
| T7 fixture-tested technical conformance | Required                |

# 5 Pilot governance

**Reference implementation requirement.**

| **Element**           | **Pilot specification** |
|-----------------------|-------------------------|
| Pilot sponsor         | Required                |
| Methodology authority | Required                |
| Pilot lead            | Required                |
| Architecture lead     | Required                |
| Domain specialists    | Required                |
| Evidence lead         | Required                |
| Data/schema lead      | Required                |
| Independent reviewer  | Required                |
| Decision authority    | Required                |
| Security reviewer     | Required                |
| AITG reviewer         | Required                |
| Release manager       | Required                |

# 6 Baseline manifest

**Reference implementation requirement.**

| **Element**            | **Pilot specification**                                                                    |
|------------------------|--------------------------------------------------------------------------------------------|
| releaseId              | aidcf:release:pilot-015-v1.0                                                               |
| Status                 | CONDITIONALLY_BASELINED                                                                    |
| Included artifacts     | AIDCF-003 through AIDCF-014                                                                |
| Known blocker          | AIDCF-007 has conflicting published control-universe counts.                               |
| Pilot treatment        | Use only explicitly selected representative controls; do not claim catalogue completeness. |
| Resolution requirement | Authoritative correction and migration before public baseline.                             |
| Integrity              | Manifest and registry hashes recorded in implementation package.                           |
| Approval               | Methodology and independent review required.                                               |

# 7 BaselineIssue record

**Reference implementation requirement.**

| **Element**       | **Pilot specification**                                                          |
|-------------------|----------------------------------------------------------------------------------|
| issueId           | aidcf:baseline-issue:control-cardinality-001                                     |
| Sources           | AIDCF-007 cover and document-control section                                     |
| Conflict          | 15/90/360 versus 14/84/336.                                                      |
| Impact            | Control coverage, registry completeness, scoring denominator and release claims. |
| Pilot disposition | Open; does not block selected-control pilot.                                     |
| Prohibited claim  | No assertion that the pilot covers the full control universe.                    |
| Resolution owner  | Methodology authority.                                                           |
| Migration         | Reissue affected registry and downstream cardinality declarations.               |

# 8 Synthetic capability record

**Reference implementation requirement.**

| **Element**       | **Pilot specification**                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------------------------------|
| capabilityId      | aidcf:capability:synthetic-training-001                                                                         |
| Name              | Synthetic Liquid-Cooled Distributed Training Capability                                                         |
| Purpose           | Execute bounded distributed model-training jobs using a synthetic high-density data-centre architecture.        |
| Workload          | Distributed training with checkpoint and restart.                                                               |
| Boundary          | Synthetic site, facility systems, AI cluster, storage, fabrics, operations and named external services.         |
| Lifecycle         | Operational-assurance pilot snapshot.                                                                           |
| Criticality       | Illustrative high consequence for completion, integrity, thermal stability and controlled recovery.             |
| Owner             | Synthetic Capability Owner role.                                                                                |
| Classification    | INTERNAL / SYNTHETIC.                                                                                           |
| Decision question | Can the synthetic capability support the declared outcomes within the modelled states and evidence limitations? |

# 9 Synthetic Service Outcomes

**Reference implementation requirement.**

| **Outcome** | **Name**                                | **Synthetic statement**                                                            |
|-------------|-----------------------------------------|------------------------------------------------------------------------------------|
| SO-01       | Training service availability           | Service remains available within declared normal/degraded conditions.              |
| SO-02       | Distributed job completion              | Jobs complete or fail in a controlled, observable manner.                          |
| SO-03       | Checkpoint integrity and recoverability | Checkpoints are complete, consistent and restorable.                               |
| SO-04       | Thermal stability                       | Rack and accelerator thermal conditions remain within declared synthetic envelope. |
| SO-05       | Controlled recovery                     | Defined failures are contained and recovery is validated before return.            |

# 10 Required functions

**Reference implementation requirement.**

| **ID** | **Required function**                  |
|--------|----------------------------------------|
| FN-01  | Accept and schedule workload           |
| FN-02  | Provide accelerator compute            |
| FN-03  | Move distributed-training traffic      |
| FN-04  | Store datasets/checkpoints             |
| FN-05  | Deliver electrical power               |
| FN-06  | Remove heat through liquid cooling     |
| FN-07  | Monitor and control infrastructure     |
| FN-08  | Detect/contain incident                |
| FN-09  | Restore training service               |
| FN-10  | Preserve evidence and decision lineage |

# 11 Synthetic system inventory

**Reference implementation requirement.**

| **ID**     | **System**                         | **Domain** |
|------------|------------------------------------|------------|
| SYS-PWR-01 | Incoming power                     | POW        |
| SYS-PWR-02 | UPS and battery                    | POW        |
| SYS-PWR-03 | Generators and fuel                | POW        |
| SYS-PWR-04 | Distribution and busway            | POW        |
| SYS-THM-01 | Primary cooling plant              | THM        |
| SYS-THM-02 | CDU Train A                        | THM        |
| SYS-THM-03 | CDU Train B                        | THM        |
| SYS-THM-04 | Liquid loops/manifolds             | THM        |
| SYS-CMP-01 | Accelerator cluster                | CMP        |
| SYS-STO-01 | Dataset storage                    | STO        |
| SYS-STO-02 | Checkpoint service                 | STO        |
| SYS-NET-01 | Scale-out fabric                   | NET        |
| SYS-NET-02 | Storage fabric                     | NET        |
| SYS-SEC-01 | Management identity/control plane  | SEC        |
| SYS-OPS-01 | Operations centre                  | OPS        |
| SYS-EVA-01 | Evidence and assessment repository | EVA        |

# 12 Representative asset instances

**Reference implementation requirement.**

| **ID**  | **Synthetic asset**           | **System** |
|---------|-------------------------------|------------|
| AST-001 | Utility service point         | SYS-PWR-01 |
| AST-002 | UPS A                         | SYS-PWR-02 |
| AST-003 | UPS B                         | SYS-PWR-02 |
| AST-004 | Generator A                   | SYS-PWR-03 |
| AST-005 | Generator B                   | SYS-PWR-03 |
| AST-006 | CDU A controller              | SYS-THM-02 |
| AST-007 | CDU B controller              | SYS-THM-03 |
| AST-008 | Shared control-network switch | SYS-SEC-01 |
| AST-009 | Accelerator rack group        | SYS-CMP-01 |
| AST-010 | Checkpoint metadata service   | SYS-STO-02 |
| AST-011 | Fabric spine group            | SYS-NET-01 |
| AST-012 | Evidence store                | SYS-EVA-01 |

# 13 Interface contracts

**Reference implementation requirement.**

| **ID**    | **Interface**                        | **Type**      |
|-----------|--------------------------------------|---------------|
| IF-PWR-01 | Utility to switchgear                | Electrical    |
| IF-PWR-02 | UPS to busway                        | Electrical    |
| IF-THM-01 | Plant to CDU A                       | Thermal/fluid |
| IF-THM-02 | Plant to CDU B                       | Thermal/fluid |
| IF-THM-03 | CDUs to rack manifolds               | Thermal/fluid |
| IF-NET-01 | Compute to scale-out fabric          | Network       |
| IF-STO-01 | Compute to checkpoint service        | Data/network  |
| IF-CTL-01 | Management identity to BMS/EPMS/CDUs | Management    |
| IF-EVA-01 | Sources to evidence repository       | Assurance     |

# 14 Dependency register

**Reference implementation requirement.**

| **ID** | **Source**           | **Target**                    | **Criticality**      |
|--------|----------------------|-------------------------------|----------------------|
| DEP-01 | Accelerator cluster  | Electrical distribution       | Critical             |
| DEP-02 | Accelerator cluster  | CDUs and liquid loops         | Critical             |
| DEP-03 | Training job         | Scale-out fabric              | Critical             |
| DEP-04 | Job recovery         | Checkpoint service            | Critical             |
| DEP-05 | Both CDU trains      | Shared control-network switch | Common-mode critical |
| DEP-06 | Generator continuity | Fuel replenishment service    | External critical    |
| DEP-07 | Operations           | Management identity service   | Critical             |
| DEP-08 | Decision lineage     | Evidence repository           | Critical             |
| DEP-09 | Recovery             | OEM support and spares        | External material    |

# 15 Fault-domain register

**Reference implementation requirement.**

| **ID** | **Fault domain**                    | **Potential scope**                         |
|--------|-------------------------------------|---------------------------------------------|
| FD-01  | Utility supply boundary             | Incoming power dependencies                 |
| FD-02  | Electrical room/common distribution | UPS and downstream paths                    |
| FD-03  | Cooling control network             | Both CDU trains                             |
| FD-04  | Cooling plant common header         | Both liquid-cooling trains                  |
| FD-05  | Training fabric control plane       | Distributed job communication               |
| FD-06  | Checkpoint metadata domain          | Checkpoint discovery and restore            |
| FD-07  | Management identity domain          | Privileged facility and platform operations |

# 16 Operating-state model

**Reference implementation requirement.**

| **State**   | **Synthetic meaning**                                     |
|-------------|-----------------------------------------------------------|
| NORMAL      | All declared systems available.                           |
| MAINTENANCE | One synthetic redundant train intentionally unavailable.  |
| DEGRADED    | Reduced redundancy/capacity; workload restrictions apply. |
| EMERGENCY   | Protective response and workload containment.             |
| RECOVERY    | Restoration and validation in progress.                   |
| TRANSITION  | Failover, restart or controlled return.                   |
| UNKNOWN     | Reliable evidence cannot establish state.                 |

# 17 Capacity assertions

**Reference implementation requirement.**

| **ID** | **Assertion**                   | **Representation**                     | **Limitation**            |
|--------|---------------------------------|----------------------------------------|---------------------------|
| CAP-01 | Accelerator demand              | Synthetic units only                   | No real engineering value |
| CAP-02 | Electrical available capacity   | Qualitative sufficient/limited/unknown | Synthetic evidence        |
| CAP-03 | Thermal available capacity      | Qualitative sufficient/limited/unknown | Synthetic evidence        |
| CAP-04 | Checkpoint performance envelope | Qualitative normal/degraded            | Synthetic evidence        |
| CAP-05 | Recovery capacity               | Reserved/not proven                    | UNKNOWN retained          |

# 18 Failure-scenario catalogue

**Reference implementation requirement.**

| **ID** | **Scenario**                              | **Initiating condition**                                         | **Potential outcome effect**                                        |
|--------|-------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------|
| SCN-01 | CDU A loss under maintenance exposure     | CDU A fails while CDU B is carrying declared load.               | Thermal degradation; workload throttling; possible controlled stop. |
| SCN-02 | Shared cooling control-network failure    | Shared switch prevents control/telemetry across both CDU trains. | Common-mode loss of visibility/control; emergency containment.      |
| SCN-03 | Checkpoint metadata degradation           | Metadata service becomes unavailable during checkpoint commit.   | Checkpoint status becomes UNKNOWN; restart claim constrained.       |
| SCN-04 | Utility loss with Generator B unavailable | Utility loss coincides with generator maintenance.               | Reduced continuity margin and conditional runtime.                  |
| SCN-05 | Privileged automation error               | Authorised automation issues incorrect cooling setpoint.         | Thermal excursion risk and evidence/authority challenge.            |

# Scenario workbook: SCN-01

**Reference implementation requirement.**

| **Element**          | **Pilot specification**                                             |
|----------------------|---------------------------------------------------------------------|
| Name                 | CDU A loss under maintenance exposure                               |
| Pre-state            | NORMAL or declared maintenance state.                               |
| Initiating condition | CDU A fails while CDU B is carrying declared load.                  |
| Propagation          | Explicit system/dependency/fault-domain steps.                      |
| Safeguards           | Detection, containment, workload control and recovery measures.     |
| Residual state       | Thermal degradation; workload throttling; possible controlled stop. |
| Evidence             | Synthetic telemetry, configuration, procedure and test records.     |
| UNKNOWN              | Any unverified independence, restoration or source-health fact.     |
| Gates                | Applicable CG results and decision effect.                          |
| Review               | Technical and independent review required.                          |

# Scenario workbook: SCN-02

**Reference implementation requirement.**

| **Element**          | **Pilot specification**                                          |
|----------------------|------------------------------------------------------------------|
| Name                 | Shared cooling control-network failure                           |
| Pre-state            | NORMAL or declared maintenance state.                            |
| Initiating condition | Shared switch prevents control/telemetry across both CDU trains. |
| Propagation          | Explicit system/dependency/fault-domain steps.                   |
| Safeguards           | Detection, containment, workload control and recovery measures.  |
| Residual state       | Common-mode loss of visibility/control; emergency containment.   |
| Evidence             | Synthetic telemetry, configuration, procedure and test records.  |
| UNKNOWN              | Any unverified independence, restoration or source-health fact.  |
| Gates                | Applicable CG results and decision effect.                       |
| Review               | Technical and independent review required.                       |

# Scenario workbook: SCN-03

**Reference implementation requirement.**

| **Element**          | **Pilot specification**                                         |
|----------------------|-----------------------------------------------------------------|
| Name                 | Checkpoint metadata degradation                                 |
| Pre-state            | NORMAL or declared maintenance state.                           |
| Initiating condition | Metadata service becomes unavailable during checkpoint commit.  |
| Propagation          | Explicit system/dependency/fault-domain steps.                  |
| Safeguards           | Detection, containment, workload control and recovery measures. |
| Residual state       | Checkpoint status becomes UNKNOWN; restart claim constrained.   |
| Evidence             | Synthetic telemetry, configuration, procedure and test records. |
| UNKNOWN              | Any unverified independence, restoration or source-health fact. |
| Gates                | Applicable CG results and decision effect.                      |
| Review               | Technical and independent review required.                      |

# Scenario workbook: SCN-04

**Reference implementation requirement.**

| **Element**          | **Pilot specification**                                         |
|----------------------|-----------------------------------------------------------------|
| Name                 | Utility loss with Generator B unavailable                       |
| Pre-state            | NORMAL or declared maintenance state.                           |
| Initiating condition | Utility loss coincides with generator maintenance.              |
| Propagation          | Explicit system/dependency/fault-domain steps.                  |
| Safeguards           | Detection, containment, workload control and recovery measures. |
| Residual state       | Reduced continuity margin and conditional runtime.              |
| Evidence             | Synthetic telemetry, configuration, procedure and test records. |
| UNKNOWN              | Any unverified independence, restoration or source-health fact. |
| Gates                | Applicable CG results and decision effect.                      |
| Review               | Technical and independent review required.                      |

# Scenario workbook: SCN-05

**Reference implementation requirement.**

| **Element**          | **Pilot specification**                                         |
|----------------------|-----------------------------------------------------------------|
| Name                 | Privileged automation error                                     |
| Pre-state            | NORMAL or declared maintenance state.                           |
| Initiating condition | Authorised automation issues incorrect cooling setpoint.        |
| Propagation          | Explicit system/dependency/fault-domain steps.                  |
| Safeguards           | Detection, containment, workload control and recovery measures. |
| Residual state       | Thermal excursion risk and evidence/authority challenge.        |
| Evidence             | Synthetic telemetry, configuration, procedure and test records. |
| UNKNOWN              | Any unverified independence, restoration or source-health fact. |
| Gates                | Applicable CG results and decision effect.                      |
| Review               | Technical and independent review required.                      |

# 24 Safeguard register

**Reference implementation requirement.**

| **ID** | **Safeguard**                        | **Function**    |
|--------|--------------------------------------|-----------------|
| SG-01  | Power-path monitoring                | Detect          |
| SG-02  | UPS/generator transfer sequence      | Prevent/Recover |
| SG-03  | Dual CDU architecture                | Prevent/Contain |
| SG-04  | Independent local thermal protection | Contain         |
| SG-05  | Workload throttling/controlled stop  | Contain         |
| SG-06  | Checkpoint validation                | Detect          |
| SG-07  | Checkpoint restore test              | Recover         |
| SG-08  | Privileged-access control            | Prevent         |
| SG-09  | Command logging and rollback         | Detect/Correct  |
| SG-10  | Incident and recovery procedure      | Respond/Recover |
| SG-11  | Evidence integrity and review        | Assure          |

# 25 Representative control profile

**Reference implementation requirement.**

| **Pilot control** | **Domain** | **Pilot objective**                            |
|-------------------|------------|------------------------------------------------|
| CTL-001           | CAP        | Capability and outcomes defined                |
| CTL-002           | DEP        | Critical dependencies visible                  |
| CTL-003           | POW        | Power continuity design and operating evidence |
| CTL-004           | THM        | Thermal continuity and liquid-cooling evidence |
| CTL-005           | CMP        | Compute configuration and health               |
| CTL-006           | STO        | Checkpoint integrity and restore               |
| CTL-007           | NET        | Fabric availability and monitoring             |
| CTL-008           | OPS        | Work control, incident and change management   |
| CTL-009           | RES        | Containment and recovery validation            |
| CTL-010           | SEC        | Privileged digital/OT authority                |
| CTL-011           | EVA        | Evidence provenance and quality                |
| CTL-012           | EVA        | Gate/decision/reassessment integrity           |

# 26 Control coverage limitation

**Reference implementation requirement.**

| **Element**    | **Pilot specification**                                                                                    |
|----------------|------------------------------------------------------------------------------------------------------------|
| Important      | Pilot control IDs are local synthetic identifiers, not replacements for canonical MCF IDs.                 |
| Reason         | AIDCF-007 cardinality and catalogue baseline must be harmonised before authoritative full-control mapping. |
| Permitted use  | Demonstrate traceability, evidence, assessment, gates and decision logic.                                  |
| Prohibited use | Claim full AIDCF-007 control coverage or real-world conformity.                                            |
| Migration      | Replace local IDs with approved canonical control registry after baseline release.                         |

# 27 Evidence-object register

**Reference implementation requirement.**

| **ID** | **Evidence**                               | **Class**     | **Status**      |
|--------|--------------------------------------------|---------------|-----------------|
| EV-001 | Synthetic architecture snapshot            | Documentary   | Accepted        |
| EV-002 | Synthetic power single-line assurance view | Documentary   | Accepted        |
| EV-003 | Synthetic cooling P&ID assurance view      | Documentary   | Accepted        |
| EV-004 | Synthetic power telemetry extract          | Operational   | Accepted        |
| EV-005 | Synthetic cooling telemetry extract        | Operational   | Accepted        |
| EV-006 | Synthetic compute/fabric health extract    | Operational   | Accepted        |
| EV-007 | Synthetic checkpoint integrity record      | Test          | Accepted        |
| EV-008 | Synthetic restore exercise                 | Test          | Qualified       |
| EV-009 | Synthetic privileged-access review         | Configuration | Accepted        |
| EV-010 | Synthetic incident/recovery drill          | Exercise      | Accepted        |
| EV-011 | CDU control-network independence evidence  | Expected      | Missing/UNKNOWN |
| EV-012 | Synthetic evidence manifest/hash register  | Integrity     | Accepted        |

# 28 Evidence quality ratings

**Reference implementation requirement.**

| **Element**  | **Pilot specification**                            |
|--------------|----------------------------------------------------|
| Provenance   | Declared synthetic source and creator.             |
| Freshness    | Aligned to pilot snapshot.                         |
| Coverage     | Representative, not complete.                      |
| Reliability  | Internally consistent synthetic fixture.           |
| Traceability | Linked to assertions, controls and gates.          |
| Integrity    | Hash field and immutable snapshot illustrated.     |
| Sufficiency  | Claim-specific; EV-011 intentionally insufficient. |
| Restriction  | Synthetic INTERNAL classification.                 |

# 29 Assessment procedures

**Reference implementation requirement.**

| **ID** | **Procedure**                               |
|--------|---------------------------------------------|
| AP-01  | Review capability/outcome records           |
| AP-02  | Reconcile architecture and system inventory |
| AP-03  | Trace dependencies and fault domains        |
| AP-04  | Review scenario propagation                 |
| AP-05  | Inspect synthetic evidence manifest         |
| AP-06  | Reperform selected trace links              |
| AP-07  | Evaluate representative control results     |
| AP-08  | Evaluate gates                              |
| AP-09  | Reproduce score snapshot                    |
| AP-10  | Challenge decision/report consistency       |
| AP-11  | Inject change event and run impact analysis |
| AP-12  | Validate AITG handoff                       |

# 30 Synthetic control results

**Reference implementation requirement.**

| **Control** | **Result** | **Confidence** |
|-------------|------------|----------------|
| CTL-001     | SUPPORTED  | High           |
| CTL-002     | SUPPORTED  | Medium         |
| CTL-003     | SUPPORTED  | Medium         |
| CTL-004     | PARTIAL    | Medium         |
| CTL-005     | SUPPORTED  | Medium         |
| CTL-006     | PARTIAL    | Medium         |
| CTL-007     | SUPPORTED  | Medium         |
| CTL-008     | SUPPORTED  | Medium         |
| CTL-009     | PARTIAL    | Medium         |
| CTL-010     | SUPPORTED  | Medium         |
| CTL-011     | SUPPORTED  | High           |
| CTL-012     | SUPPORTED  | Medium         |

# 31 Finding register

**Reference implementation requirement.**

| **ID**  | **Class**            | **Condition**                                                                                  | **Status** |
|---------|----------------------|------------------------------------------------------------------------------------------------|------------|
| FND-001 | Significant weakness | Shared CDU control-network independence is not evidenced.                                      | Open       |
| FND-002 | Weakness             | Checkpoint restore evidence is qualified and does not cover every declared recovery condition. | Open       |
| FND-003 | Observation          | Generator maintenance state reduces synthetic continuity margin.                               | Open       |

# 32 UNKNOWN register

**Reference implementation requirement.**

| **ID**  | **Unknown**                                                         | **Materiality** | **Decision effect**                              |
|---------|---------------------------------------------------------------------|-----------------|--------------------------------------------------|
| UNK-001 | Independence of both CDU trains from shared control-network failure | Critical        | Blocks unqualified thermal resilience conclusion |
| UNK-002 | Recovery capacity under simultaneous power and cooling degradation  | Material        | Limits recovery assurance                        |
| UNK-003 | OEM support availability during synthetic recovery window           | Moderate        | Condition on recovery decision                   |

# 33 Gate-results register

**Reference implementation requirement.**

| **Gate** | **Status**  | **Pilot basis**                                          |
|----------|-------------|----------------------------------------------------------|
| CG-01    | PASS        | Capability/outcomes defined                              |
| CG-02    | PASS        | Boundary and operating envelope defined for pilot        |
| CG-03    | CONDITIONAL | External dependencies modelled with limitations          |
| CG-04    | PASS        | Safety boundary and synthetic-only testing               |
| CG-05    | CONDITIONAL | Power continuity supported with maintenance limitation   |
| CG-06    | UNKNOWN     | Cooling-control common mode unresolved                   |
| CG-07    | PASS        | Control-system authority modelled                        |
| CG-08    | PASS        | Compute/storage/network integrity represented            |
| CG-09    | UNKNOWN     | Containment under common-mode cooling failure unresolved |
| CG-10    | CONDITIONAL | Recovery evidence qualified                              |
| CG-11    | PASS        | Evidence manifest and lineage validated                  |
| CG-12    | PASS        | Critical UNKNOWN visible                                 |
| CG-13    | PASS        | Roles and decisions defined                              |
| CG-14    | PASS        | Change control and review defined                        |
| CG-15    | PASS        | Digital authority path represented                       |

# 34 Score snapshot

**Reference implementation requirement.**

| **Element**               | **Pilot specification**                                          |
|---------------------------|------------------------------------------------------------------|
| Profile                   | Synthetic Pilot Profile v1.0                                     |
| Controls assessed         | 12 representative synthetic controls                             |
| Raw indicator             | Illustrative only; not a framework-wide score.                   |
| Coverage                  | Representative pilot coverage, not full catalogue coverage.      |
| Confidence                | Medium overall due to synthetic evidence and open UNKNOWN.       |
| Gate overlay              | CG-06 and CG-09 UNKNOWN control the decision ceiling.            |
| Anti-gaming               | UNKNOWN excluded from favourable averaging and remains explicit. |
| Reproducibility           | Inputs, weights and calculations fixed in snapshot.              |
| Prohibited interpretation | No facility rating, certification, benchmark or real assurance.  |

# 35 Decision recommendation

**Reference implementation requirement.**

| **Element**         | **Pilot specification**                                                                     |
|---------------------|---------------------------------------------------------------------------------------------|
| Recommended state   | LIMITED                                                                                     |
| Reason 1            | Pilot architecture, evidence and traceability are substantially complete for demonstration. |
| Reason 2            | Critical cooling-control common-mode independence remains UNKNOWN.                          |
| Reason 3            | Recovery evidence is qualified.                                                             |
| Controlling gates   | CG-06 UNKNOWN; CG-09 UNKNOWN; CG-10 CONDITIONAL.                                            |
| Permitted reliance  | Technical demonstration of AIDCF workflow.                                                  |
| Prohibited reliance | Real facility, safety, resilience or certification conclusion.                              |
| Conditions          | Resolve UNK-001 and broaden recovery evidence before stronger synthetic conclusion.         |

# 36 Synthetic assurance decision

**Reference implementation requirement.**

| **Element**       | **Pilot specification**                               |
|-------------------|-------------------------------------------------------|
| decisionId        | aidcf:decision:synthetic-training-001                 |
| Decision          | LIMITED                                               |
| Authority         | Synthetic Decision Authority role.                    |
| Scope             | Defined synthetic capability and pilot snapshot only. |
| Evidence period   | Pilot fixture snapshot.                               |
| Conditions        | Open findings/UNKNOWN and gate constraints.           |
| Validity          | Until synthetic change event or superseding snapshot. |
| Non-certification | Not a certificate, guarantee or engineering approval. |

# 37 Executive report example

**Reference implementation requirement.**

| **Element**         | **Pilot specification**                                                          |
|---------------------|----------------------------------------------------------------------------------|
| Decision            | LIMITED                                                                          |
| What is supported   | End-to-end traceability and machine validation operate on the synthetic dataset. |
| Top risk            | Shared cooling-control common mode is unresolved.                                |
| Critical gates      | CG-06 and CG-09 UNKNOWN.                                                         |
| Priority action     | Separate or independently protect CDU control pathways and produce evidence.     |
| Residual limitation | Recovery evidence remains qualified.                                             |
| Decision ask        | Approve pilot completion; do not claim stronger assurance.                       |

# 38 Technical report example

**Reference implementation requirement.**

| **Element**  | **Pilot specification**                                                    |
|--------------|----------------------------------------------------------------------------|
| Capability   | Synthetic distributed training.                                            |
| Architecture | Power, liquid cooling, compute, storage, network, controls and operations. |
| Scenarios    | Five synthetic scenarios.                                                  |
| Evidence     | Twelve synthetic evidence objects.                                         |
| Controls     | Twelve representative local pilot controls.                                |
| Findings     | Three open findings.                                                       |
| UNKNOWN      | Three records, including one critical.                                     |
| Gates        | 15 gate results with gate dominance.                                       |
| Decision     | LIMITED.                                                                   |
| Traceability | Forward and reverse trace tested.                                          |

# 39 Graph instance summary

**Reference implementation requirement.**

| **Element**          | **Pilot specification**         |
|----------------------|---------------------------------|
| CapabilityInstance   | Instantiated in synthetic graph |
| ServiceOutcome       | Instantiated in synthetic graph |
| RequiredFunction     | Instantiated in synthetic graph |
| InfrastructureSystem | Instantiated in synthetic graph |
| AssetInstance        | Instantiated in synthetic graph |
| Interface            | Instantiated in synthetic graph |
| Dependency           | Instantiated in synthetic graph |
| FaultDomain          | Instantiated in synthetic graph |
| FailureScenario      | Instantiated in synthetic graph |
| Safeguard            | Instantiated in synthetic graph |
| Control              | Instantiated in synthetic graph |
| EvidenceObject       | Instantiated in synthetic graph |
| Assessment           | Instantiated in synthetic graph |
| ControlAssessment    | Instantiated in synthetic graph |
| Finding              | Instantiated in synthetic graph |
| UnknownRecord        | Instantiated in synthetic graph |
| GateResult           | Instantiated in synthetic graph |
| ScoreSnapshot        | Instantiated in synthetic graph |
| AssuranceDecision    | Instantiated in synthetic graph |
| AssuranceReport      | Instantiated in synthetic graph |
| Event                | Instantiated in synthetic graph |
| ReassessmentTrigger  | Instantiated in synthetic graph |

# 40 Pilot graph queries

**Reference implementation requirement.**

| **Query** | **Expected semantic answer**                            |
|-----------|---------------------------------------------------------|
| Q-01      | Return all systems and dependencies supporting SO-04.   |
| Q-02      | Return failure paths affecting SO-04.                   |
| Q-03      | Return evidence supporting CG-06.                       |
| Q-04      | Return findings and UNKNOWN constraining the decision.  |
| Q-05      | Reconstruct executive-report decision text to evidence. |
| Q-06      | Return all objects affected by control-network change.  |
| Q-07      | List candidate inferences awaiting review.              |
| Q-08      | Return AIDCF-AITG handoff objects only.                 |

# 41 Reference implementation package

**Reference implementation requirement.**

| **Element**                   | **Pilot specification**          |
|-------------------------------|----------------------------------|
| release-manifest.json         | Required implementation artifact |
| known-issues.json             | Required implementation artifact |
| registries/\*.csv             | Required implementation artifact |
| schemas/\*.json               | Required implementation artifact |
| semantic/aidcf-context.jsonld | Required implementation artifact |
| semantic/aidcf-core.ttl       | Required implementation artifact |
| semantic/aidcf-shapes.ttl     | Required implementation artifact |
| dataset/capability.jsonld     | Required implementation artifact |
| dataset/architecture.jsonld   | Required implementation artifact |
| dataset/dependencies.jsonld   | Required implementation artifact |
| dataset/scenarios.jsonld      | Required implementation artifact |
| dataset/safeguards.jsonld     | Required implementation artifact |
| dataset/evidence.jsonld       | Required implementation artifact |
| dataset/assessment.jsonld     | Required implementation artifact |
| dataset/gates.jsonld          | Required implementation artifact |
| dataset/score.jsonld          | Required implementation artifact |
| dataset/decision.jsonld       | Required implementation artifact |
| dataset/reports.jsonld        | Required implementation artifact |
| events/change-event.jsonld    | Required implementation artifact |
| tests/valid                   | Required implementation artifact |
| tests/invalid                 | Required implementation artifact |
| tests/security                | Required implementation artifact |
| tests/migration               | Required implementation artifact |
| conformance-report.json       | Required implementation artifact |

# 42 Positive conformance fixtures

**Reference implementation requirement.**

| **Fixture** | **Expected result**               |
|-------------|-----------------------------------|
| POS-01      | Capability record valid           |
| POS-02      | Outcome/function path valid       |
| POS-03      | Architecture snapshot valid       |
| POS-04      | Evidence record valid             |
| POS-05      | Gate result valid                 |
| POS-06      | Decision/report consistency valid |
| POS-07      | Event/reassessment valid          |

# 43 Negative conformance fixtures

**Reference implementation requirement.**

| **Fixture** | **Expected rejection**                            |
|-------------|---------------------------------------------------|
| NEG-01      | Missing capability owner rejected                 |
| NEG-02      | Broken dependency target rejected                 |
| NEG-03      | Evidence without assertion link rejected          |
| NEG-04      | Gate PASS without evidence rejected               |
| NEG-05      | Reasonably Assured with critical UNKNOWN rejected |
| NEG-06      | Report stronger than decision rejected            |
| NEG-07      | Supersession cycle rejected                       |
| NEG-08      | Sensitive export without profile rejected         |

# 44 Anti-gaming fixtures

**Reference implementation requirement.**

| **ID** | **Attempt**                                       | **Expected** |
|--------|---------------------------------------------------|--------------|
| AG-01  | Convert UNKNOWN to N/A                            | Reject       |
| AG-02  | Duplicate one evidence object to inflate coverage | Detect       |
| AG-03  | Average away failed/unknown gate                  | Reject       |
| AG-04  | Remove external dependency from report            | Reject       |
| AG-05  | Close finding without closure evidence            | Reject       |
| AG-06  | Promote inferred edge to approved fact            | Reject       |

# 45 Synthetic change event

**Reference implementation requirement.**

| **Element**      | **Pilot specification**                                                                 |
|------------------|-----------------------------------------------------------------------------------------|
| eventId          | EVT-CHANGE-001                                                                          |
| Type             | ARCHITECTURE_CHANGED                                                                    |
| Subject          | Shared cooling control-network path                                                     |
| Synthetic change | CDU B is moved to a separate control-network segment with independent local protection. |
| Evidence         | Updated synthetic topology, configuration and test record.                              |
| Initial state    | Candidate, not automatically approved.                                                  |
| Trigger          | Reassess dependencies, scenarios, controls, CG-06, CG-09, score and decision.           |
| Classification   | INTERNAL / SYNTHETIC.                                                                   |

# 46 Impact-analysis result

**Reference implementation requirement.**

| **Element**           | **Pilot specification**                                          |
|-----------------------|------------------------------------------------------------------|
| Affected dependencies | DEP-05                                                           |
| Affected fault domain | FD-03                                                            |
| Affected scenarios    | SCN-02 and SCN-05                                                |
| Affected safeguard    | SG-03, SG-04, SG-09                                              |
| Affected controls     | CTL-004, CTL-009, CTL-010, CTL-011                               |
| Affected finding      | FND-001                                                          |
| Affected UNKNOWN      | UNK-001                                                          |
| Affected gates        | CG-06, CG-07, CG-09, CG-10                                       |
| Affected outputs      | Score snapshot, decision, executive report and technical report. |

# 47 Reassessment record

**Reference implementation requirement.**

| **Element**     | **Pilot specification**                                                           |
|-----------------|-----------------------------------------------------------------------------------|
| New evidence    | EV-013 synthetic independent-control topology; EV-014 synthetic common-mode test. |
| Disposition     | Evidence technically reviewed in pilot.                                           |
| FND-001         | Ready for validation, not auto-closed.                                            |
| UNK-001         | Resolved for synthetic changed snapshot.                                          |
| CG-06           | Candidate PASS after review.                                                      |
| CG-09           | Candidate CONDITIONAL due remaining recovery evidence.                            |
| Decision effect | Candidate improvement from LIMITED to CONDITIONALLY_ASSURED.                      |
| Authority       | Requires new decision approval.                                                   |

# 48 Superseding decision

**Reference implementation requirement.**

| **Element**    | **Pilot specification**                                                       |
|----------------|-------------------------------------------------------------------------------|
| New decision   | CONDITIONALLY_ASSURED                                                         |
| Conditions     | Broaden recovery evidence; confirm OEM support dependency; retain monitoring. |
| Supersedes     | aidcf:decision:synthetic-training-001                                         |
| Does not erase | Prior limited decision, open history or original evidence.                    |
| New snapshot   | aidcf:snapshot:synthetic-training-002                                         |
| Report status  | Prior reports superseded; new reports issued.                                 |
| Restriction    | Synthetic demonstration only.                                                 |

# 49 AITG handoff registry

**Reference implementation requirement.**

| **ID** | **AIDCF object**     | **AITG view**              | **Mapping**                 |
|--------|----------------------|----------------------------|-----------------------------|
| H-01   | CapabilityInstance   | AITG SystemOfInterest      | RELATED                     |
| H-02   | ServiceOutcome       | AITG Outcome               | CLOSE                       |
| H-03   | InfrastructureSystem | AITG InfrastructureObject  | CLOSE                       |
| H-04   | Dependency           | AITG Dependency            | CLOSE                       |
| H-05   | FailureScenario      | AITG FailureCondition/Path | RELATED                     |
| H-06   | Safeguard            | AITG Control/Breakpoint    | RELATED                     |
| H-07   | EvidenceObject       | AITG EvidenceItem          | CLOSE                       |
| H-08   | AssuranceDecision    | AITG Decision              | CLOSE but federated         |
| H-09   | UnknownRecord        | AITG UNKNOWN               | EXACT within shared profile |

# 50 AITG integration constraints

**Reference implementation requirement.**

| **Element** | **Pilot specification**                                   |
|-------------|-----------------------------------------------------------|
| Identity    | Shared real-world identity only when reviewed.            |
| Semantics   | No property duplication beyond controlled display/cache.  |
| Evidence    | Reuse requires assertion-specific relevance.              |
| Paths       | Failure path is not automatically a trust/exposure path.  |
| Decisions   | AIDCF and AITG conclusions remain separate and federated. |
| UNKNOWN     | Preserved as first-class state.                           |
| Security    | Sensitive infrastructure paths restricted.                |
| Automation  | No automatic favourable aggregation.                      |

# 51 Pilot conformance summary

**Reference implementation requirement.**

| **Element** | **Pilot specification**                                                         |
|-------------|---------------------------------------------------------------------------------|
| T0          | PASS - controlled vocabulary used.                                              |
| T1          | PASS - canonical records and IDs.                                               |
| T2          | PASS - forward/reverse traceability.                                            |
| T3          | PASS for illustrative schema fixtures.                                          |
| T4          | PASS at specification/pilot-model level; independent ontology review pending.   |
| T5          | PASS - evidence, gates, decision and reports.                                   |
| T6          | PASS - synthetic change and reassessment.                                       |
| T7          | CONDITIONAL - independent runner and full machine package remain release gates. |
| Overall     | CONDITIONALLY CONFORMANT SYNTHETIC PILOT.                                       |

# 52 Defect and gap register

**Reference implementation requirement.**

| **ID**  | **Gap**                                                  | **Disposition**               |
|---------|----------------------------------------------------------|-------------------------------|
| GAP-001 | AIDCF-007 control cardinality conflict                   | Block public baseline         |
| GAP-002 | Representative controls use local pilot IDs              | Migrate after registry freeze |
| GAP-003 | Synthetic evidence does not establish real effectiveness | Permanent limitation          |
| GAP-004 | OWL/SHACL independent review pending                     | Release gate                  |
| GAP-005 | No live source connectors exercised                      | MVP backlog                   |
| GAP-006 | No production-scale performance test                     | MVP backlog                   |
| GAP-007 | Security model specified but not penetration tested      | Production gate               |
| GAP-008 | Industry-specific regulatory mappings not exercised      | Future profiles               |

# 53 Lessons learned

**Reference implementation requirement.**

| **ID** | **Pilot lesson**                                                             |
|--------|------------------------------------------------------------------------------|
| L-01   | Baseline consistency is prerequisite to authoritative machine execution.     |
| L-02   | Architecture and evidence must be claim-specific.                            |
| L-03   | UNKNOWN materially changes decisions and cannot be cosmetic.                 |
| L-04   | Shared control planes create hidden common modes.                            |
| L-05   | Gate logic prevents favourable scores from masking critical uncertainty.     |
| L-06   | Report generation must reference immutable decision snapshots.               |
| L-07   | Event handling must separate candidate impact from approved decision change. |
| L-08   | AITG integration works best through reviewed handoffs, not semantic merging. |

# 54 MVP backlog derived from pilot

**Reference implementation requirement.**

| **Priority** | **Capability**                                      |
|--------------|-----------------------------------------------------|
| P0           | Resolve baseline and release manifest               |
| P0           | Build canonical registries                          |
| P0           | Implement JSON schemas and validator                |
| P0           | Implement immutable snapshot/lineage store          |
| P0           | Implement graph ingest/query                        |
| P0           | Implement evidence and assessment records           |
| P0           | Implement gates and decision constraints            |
| P1           | Implement report generation                         |
| P1           | Implement events and impact analysis                |
| P1           | Implement AITG handoff                              |
| P1           | Build conformance runner                            |
| P2           | Add source connectors and monitoring                |
| P2           | Add security administration and disclosure profiles |
| P2           | Add multi-tenant operations and analytics           |

# 55 Repository structure

**Reference implementation requirement.**

| **Element**  | **Pilot specification**                                 |
|--------------|---------------------------------------------------------|
| /docs        | AIDCF-015 narrative, pilot report and decisions         |
| /baseline    | Release manifest, issues and changelog                  |
| /registries  | Controlled CSV registries                               |
| /schemas     | JSON Schemas                                            |
| /semantic    | JSON-LD, Turtle, OWL and SHACL                          |
| /dataset     | Synthetic capability records                            |
| /events      | Change and reassessment records                         |
| /reports     | Executive and technical examples                        |
| /tests       | Positive, negative, security, migration and anti-gaming |
| /tools       | Validator, loader and query examples                    |
| /conformance | Results and release checklist                           |

# 56 Pilot execution workflow

**Reference implementation requirement.**

| **Phase** | **Activity**                                  |
|-----------|-----------------------------------------------|
| P0        | Approve charter and synthetic-use boundary    |
| P1        | Load baseline and known issues                |
| P2        | Instantiate capability/outcomes/architecture  |
| P3        | Instantiate dependencies/scenarios/safeguards |
| P4        | Map controls/evidence and assess              |
| P5        | Evaluate findings/UNKNOWN/gates/scores        |
| P6        | Approve decision and reports                  |
| P7        | Run validation and graph query suite          |
| P8        | Inject change event                           |
| P9        | Run impact analysis and reassessment          |
| P10       | Supersede decision/reports                    |
| P11       | Publish conformance report and backlog        |

# 57 Quality review checklist

**Reference implementation requirement.**

| **Element**                      | **Pilot specification**       |
|----------------------------------|-------------------------------|
| Synthetic labels on every output | Required before pilot release |
| No real vendor/facility claims   | Required before pilot release |
| Baseline issue visible           | Required before pilot release |
| IDs resolve                      | Required before pilot release |
| Schemas validate                 | Required before pilot release |
| Graph links complete             | Required before pilot release |
| UNKNOWN visible                  | Required before pilot release |
| Gate logic verified              | Required before pilot release |
| Score reproducible               | Required before pilot release |
| Reports match decisions          | Required before pilot release |
| Event impact reviewed            | Required before pilot release |
| Prior snapshots retained         | Required before pilot release |
| AITG mappings reviewed           | Required before pilot release |
| Sensitive paths classified       | Required before pilot release |
| Independent reviewer sign-off    | Required before pilot release |

# 58 Review and release gates

**Reference implementation requirement.**

| **Reviewer/gate**                    | **Status** |
|--------------------------------------|------------|
| Methodology authority                | Pending    |
| Data-centre architect                | Pending    |
| Electrical specialist                | Pending    |
| Liquid-cooling specialist            | Pending    |
| AI/HPC specialist                    | Pending    |
| Storage/network specialist           | Pending    |
| OT/security specialist               | Pending    |
| Evidence specialist                  | Pending    |
| Assurance reviewer                   | Pending    |
| JSON Schema reviewer                 | Pending    |
| RDF/OWL/SHACL reviewer               | Pending    |
| AITG reviewer                        | Pending    |
| Security/privacy reviewer            | Pending    |
| Independent pilot rerun              | Pending    |
| Control registry baseline resolution | Pending    |
| Public release decision              | Pending    |

## Final pilot doctrine

**AIDCF-015 is a synthetic proof of executability, not a certificate or representation of a real facility. The pilot succeeds only if the complete assurance chain is reproducible in both directions, uncertainty remains visible, gates constrain decisions, reports match approved snapshots, changes trigger reviewed reassessment, and all semantic ownership boundaries remain intact.**
