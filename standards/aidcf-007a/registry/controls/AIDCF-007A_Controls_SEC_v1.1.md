# AIDCF-007A Control Catalogue — SEC Digital, OT and Control-Plane Security

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-SEC](../../../aidcf-018-domain-guides/AIDCF-018-SEC_Digital_OT_and_Control-Plane_Security_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-SEC-001](#mcf-sec-001) | Human Identity | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-15, CG-07, CG-13 |
| [MCF-SEC-002](#mcf-sec-002) | Machine Identity | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-15, CG-08 |
| [MCF-SEC-003](#mcf-sec-003) | Privileged Access | PREVENTIVE | EFFECTIVENESS | AL5 | CG-15 | CG-07 |
| [MCF-SEC-004](#mcf-sec-004) | Break-Glass Governance | CORRECTIVE | OPERATION | AL4 | — | CG-15, CG-10 |
| [MCF-SEC-005](#mcf-sec-005) | BMS and EPMS Security | PREVENTIVE | EFFECTIVENESS | AL5 | CG-07 | CG-15, CG-05, CG-06 |
| [MCF-SEC-006](#mcf-sec-006) | Cluster Manager Security | PREVENTIVE | EFFECTIVENESS | AL5 | CG-15 | CG-08 |
| [MCF-SEC-007](#mcf-sec-007) | Fabric Controller Security | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-15, CG-08 |
| [MCF-SEC-008](#mcf-sec-008) | Storage Controller Security | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-15, CG-10, CG-08 |
| [MCF-SEC-009](#mcf-sec-009) | Security Zoning | PREVENTIVE | IMPLEMENTATION | AL3 | CG-07 | CG-15, CG-09 |
| [MCF-SEC-010](#mcf-sec-010) | Management-Plane Segmentation | PREVENTIVE | EFFECTIVENESS | AL5 | CG-15 | CG-07 |
| [MCF-SEC-011](#mcf-sec-011) | Filtering and Gateways | PREVENTIVE | OPERATION | AL4 | — | CG-07, CG-15 |
| [MCF-SEC-012](#mcf-sec-012) | Remote Access | PREVENTIVE | EFFECTIVENESS | AL5 | CG-15 | CG-07 |
| [MCF-SEC-013](#mcf-sec-013) | Secure Baseline | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-07, CG-15, CG-08 |
| [MCF-SEC-014](#mcf-sec-014) | Vulnerability Management | DETECTIVE | OPERATION | AL4 | — | CG-07, CG-15 |
| [MCF-SEC-015](#mcf-sec-015) | Patch Governance | PREVENTIVE | OPERATION | AL4 | — | CG-14, CG-07 |
| [MCF-SEC-016](#mcf-sec-016) | Exception and Compensating Control | DIRECTIVE | OPERATION | AL4 | — | CG-07, CG-15 |
| [MCF-SEC-017](#mcf-sec-017) | Security Telemetry | DETECTIVE | OPERATION | AL4 | — | CG-15, CG-07 |
| [MCF-SEC-018](#mcf-sec-018) | Behaviour Detection | DETECTIVE | EFFECTIVENESS | AL5 | — | CG-15, CG-07 |
| [MCF-SEC-019](#mcf-sec-019) | Incident Containment | CORRECTIVE | RESILIENCE | AL5 | — | CG-09, CG-15, CG-07, CG-10 |
| [MCF-SEC-020](#mcf-sec-020) | Forensic Readiness | DETECTIVE | IMPLEMENTATION | AL3 | — | CG-15 |
| [MCF-SEC-021](#mcf-sec-021) | Agent or Automation Authority | DIRECTIVE | IMPLEMENTATION | AL3 | CG-15 | CG-07 |
| [MCF-SEC-022](#mcf-sec-022) | Approval Controls | PREVENTIVE | EFFECTIVENESS | AL5 | — | CG-15, CG-14 |
| [MCF-SEC-023](#mcf-sec-023) | Command Allowlisting | PREVENTIVE | EFFECTIVENESS | AL5 | CG-07 | CG-15 |
| [MCF-SEC-024](#mcf-sec-024) | Safe Rollback | RECOVERY | RESILIENCE | AL5 | — | CG-15, CG-10, CG-07 |

## SEC-01 Identity and privileged access

### MCF-SEC-001

**Human Identity** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure every person who can observe, configure or command facility OT, infrastructure management planes or AI control planes is uniquely identified, strongly authenticated and lifecycle-managed, with no shared or orphaned accounts.

**Requirement.** The identity and access manager shall ensure that every human identity with access to BMS, EPMS, CDU and PLC engineering workstations and HMIs, BMC/Redfish interfaces, network devices, hypervisor and Kubernetes control planes, cluster managers and storage controllers is individually attributable, uses phishing-resistant multi-factor authentication where the system supports it (with compensating controls recorded where it does not, for example legacy HMIs), and is joined, moved and removed through an authoritative identity source within defined deadlines. The OT security owner shall maintain an inventory of OT systems that cannot integrate with central identity and the compensating controls applied.

**Assessment criteria**

1. All human accounts on in-scope systems map to a named individual in the authoritative identity source; shared accounts are absent or individually approved with session attribution.
2. Phishing-resistant MFA is enforced for remote and privileged access to in-scope systems, with exceptions listed and compensated.
3. Leaver access is removed within the defined deadline (sampled against HR leaver records).
4. Periodic access recertification of in-scope systems occurred at the defined interval.
5. OT systems lacking central identity integration are inventoried with compensating controls (for example jump-host attribution, local account review).
6. Identity services relied upon for infrastructure access have documented fallback for outage (linked to SEC-004).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Leaver access removal deadline | h | 24 (illustrative) | Capability-profile parameter. |
| Access recertification interval | months | 3 for privileged, 6 for standard (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Account extracts from in-scope systems reconciled to the identity source
- MFA enforcement configuration and exception list
- Leaver sample reconciliation
- Recertification records
- OT identity exception inventory

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Account extracts within 30 days (illustrative); leaver sample over 6 months. |
| independence | Account extracts taken by the assessor directly from target systems, not from the identity system alone. |
| mandatoryItems | Account extracts from target systems; Leaver reconciliation |
| acceptableAlternatives | Witnessed screen extraction from legacy OT systems that cannot export accounts |
| unknownEffect | US3; US4 against CG-15 where accounts on BMS/EPMS or BMC planes cannot be enumerated. |
| reassessmentTriggers | Identity platform change; New in-scope system; Mass onboarding of contractors |

**Assessment methods.** RECONCILIATION, SAMPLING, DOCUMENT_REVIEW, INSPECTION

**Assessment procedure**

1. Enumerate in-scope systems including OT HMIs and engineering workstations.
2. Extract local and directory-linked accounts from a sample of each class.
3. Reconcile to the identity source and HR records.
4. Verify MFA enforcement and review exceptions.
5. Review recertification and OT exception inventory.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-07 Critical control-system integrity (SUPPORTING); CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to all human access to in-scope OT, infrastructure management and AI control-plane systems, including contractors and provider staff (with SUP-021 for provider identities).

**Lifecycle stages.** BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Shared HMI login preventing attribution; Leaver retaining BMC access; MFA absent on remote engineering access; Orphaned local admin on switches

**Testing safety.** Account extraction shall use read-only methods; no password testing or credential guessing is permitted without written authorisation from the security owner and, for OT, the facility owner.

**UNKNOWN rule.** Systems whose accounts cannot be enumerated are recorded with U2 and their access treated as uncontrolled in authority-path analysis.

**Ontology classes.** Safeguard, InfrastructureSystem, Interface · **Related controls.** MCF-SEC-003, MCF-SEC-004, MCF-SUP-021, MCF-PHY-013

**Informative references.** NIST SP 800-63 (Digital identity guidelines); FIDO2 / W3C Web Authentication (phishing-resistant authentication); ISA/IEC 62443-3-3 (System security requirements and security levels); NIST SP 800-82 Rev. 3 (Guide to operational technology security); ISO/IEC 27002 (Information security controls)

### MCF-SEC-002

**Machine Identity** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure machine identities (service accounts, API tokens, certificates, workload identities, node and device identities) used by automation, controllers and agents are inventoried, scoped, rotated and, for hardware, anchored in a root of trust with attestation.

**Requirement.** The platform security lead shall maintain an inventory of machine identities with access to in-scope infrastructure, including owner, purpose, scope, credential type, rotation interval and expiry, and shall prohibit long-lived static credentials for consequential authority where short-lived or certificate-based credentials are supported. The platform security lead shall require hardware-rooted identity (for example TPM or device identity certificates) and boot or firmware attestation (for example via SPDM or TPM quotes) for accelerator nodes, BMCs and fabric devices that support it, and shall gate cluster admission on successful attestation.

**Assessment criteria**

1. A machine-identity inventory covers service accounts, tokens, certificates and workload identities with owner and scope.
2. Long-lived static credentials with write or command authority are absent or individually approved with rotation.
3. Certificates and tokens are rotated within defined intervals and expiry is monitored.
4. Nodes and devices supporting hardware root of trust present device identity and attestation, and cluster admission rejects failed attestation.
5. Machine identities are scoped to least privilege (sampled).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum static credential lifetime (consequential authority) | days | 90 (illustrative) | Capability-profile parameter. |
| Certificate expiry warning window | days | 30 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Machine-identity inventory
- Credential type and rotation evidence
- Certificate expiry monitoring
- Attestation configuration and admission logs
- Scope samples

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; RECOVERY |
| periodCoverage | Inventory within 30 days (illustrative); admission logs for 90 days. |
| independence | Inventory reconciled by the assessor to secrets stores and target-system configurations. |
| mandatoryItems | Machine-identity inventory; Attestation admission logs where supported |
| acceptableAlternatives | Secrets-manager reports combined with target-side token listings |
| unknownEffect | US3; US4 against CG-15 where unscoped machine credentials with OT or control-plane write authority exist. |
| reassessmentTriggers | New automation or agent; PKI change; Node hardware generation change |

**Assessment methods.** RECONCILIATION, INSPECTION, SAMPLING, ANALYSIS

**Assessment procedure**

1. Review the inventory and reconcile with secrets stores and target systems.
2. Identify static credentials with consequential authority.
3. Review rotation and expiry monitoring.
4. Review attestation configuration and sample admission logs including rejections.
5. Sample scopes for least privilege.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to machine identities with access to in-scope infrastructure. Hardware attestation criteria apply only where devices support it; unsupported classes are listed.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE · **Operating states.** NORMAL, MAINTENANCE, RECOVERY

**Failure modes addressed.** Hard-coded API token in automation with BMS write access; Expired certificate halting control plane; Tampered node joining cluster without attestation; Over-scoped service account

**Testing safety.** Attestation rejection tests shall use a designated test node; do not alter firmware on production nodes to test rejection.

**UNKNOWN rule.** Credentials discovered on target systems but absent from inventory are Findings; if discovery is not possible, record U5.

**Ontology classes.** Safeguard, AssetInstance, Interface · **Related controls.** MCF-SEC-021, MCF-SEC-013, MCF-CMP-021, MCF-SUP-014

**Informative references.** Trusted Computing Group TPM 2.0 Library Specification; DMTF DSP0274 (Security Protocol and Data Model, SPDM); IETF RFC 9334 (Remote ATtestation procedureS architecture); NIST SP 800-193 (Platform firmware resiliency guidelines); NIST SP 800-207 (Zero trust architecture)

### MCF-SEC-003

**Privileged Access** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure privileged and consequential authority over facility OT, BMC/Redfish, network, hypervisor/Kubernetes, cluster manager and storage control planes is least-privilege, brokered, time-bound and monitored, so no single compromised identity can command cross-domain infrastructure.

**Requirement.** The infrastructure security owner shall define privileged roles by authority action (observe, configure, command, bypass, update, revoke, recover, per AIDCF-005) and by domain, shall prohibit standing cross-domain privileged roles (for example a single role with write access to both BMS/EPMS and cluster control planes) except as approved break-glass, and shall broker privileged sessions through a privileged access management (PAM) system or jump hosts providing just-in-time elevation, session recording and approval for command and bypass actions. The infrastructure security owner shall test at a defined interval that privilege boundaries hold, including that elevation requires approval and that sessions are recorded.

**Assessment criteria**

1. Privileged roles are defined by authority action and domain, with an effective-permission analysis for each.
2. No standing identity holds command or bypass authority across more than one infrastructure domain without approved break-glass status.
3. Privileged access to in-scope systems is brokered with just-in-time elevation and session recording.
4. Command and bypass actions on OT systems require approval or are restricted to authorised operators on site.
5. Tests in the interval confirmed that direct (non-brokered) privileged access is blocked and elevation requires approval.
6. Privileged session logs are reviewed at a defined frequency.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum JIT elevation duration | h | 4 (illustrative) | Capability-profile parameter. |
| Privilege boundary test interval | months | 6 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Privileged role catalogue by authority action and domain
- Effective-permission analysis
- PAM configuration and session recordings sample
- Bypass-path test results
- Session review records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY; RECOVERY |
| periodCoverage | Test within interval; 90 days (illustrative) of session logs. |
| independence | Bypass-path testing by the security function or an independent tester. |
| mandatoryItems | Effective-permission analysis; Bypass-path test results |
| acceptableAlternatives | Configuration analysis of network and host controls proving non-brokered paths are blocked, where active testing is not authorised |
| unknownEffect | US4: CG-15 cannot PASS while consequential cross-domain authority is unanalysed or untested. |
| reassessmentTriggers | New control plane; Role model change; PAM platform change; Incident involving privileged misuse |

**Assessment methods.** ANALYSIS, TEST, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Review role catalogue and effective permissions, including group and federation inheritance.
2. Identify identities with cross-domain command or bypass authority.
3. Review PAM configuration and sample session recordings.
4. Review or perform tests of non-brokered access paths.
5. Review session review records.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (CRITICAL); CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies to all privileged access to in-scope OT, infrastructure management and AI control-plane systems.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY, RECOVERY

**Failure modes addressed.** Domain admin inheriting BMS write rights (control-plane inheritance); Direct SSH to BMCs bypassing PAM; Standing cluster-admin token; Shared management identity across power and cooling

**Testing safety.** Bypass-path tests shall be non-destructive (attempt authentication or connection only, no commands) and require written authorisation from the security owner; tests touching OT systems also require facility owner authorisation and must not issue any write or command.

**UNKNOWN rule.** If effective permissions cannot be computed because of opaque federation or local roles, record U9 at US4 against CG-15.

**Ontology classes.** Safeguard, Interface, InfrastructureSystem, TestRecord · **Related controls.** MCF-SEC-001, MCF-SEC-004, MCF-SEC-010, MCF-SEC-021, MCF-SUP-022

**Informative references.** AIDCF-005 (AIDCF–AI Trust Graph Integration Standard); NIST SP 800-207 (Zero trust architecture); ISA/IEC 62443-3-3 (System security requirements and security levels); NIST SP 800-53 Rev. 5 (Security and privacy controls); NIST SP 800-82 Rev. 3 (Guide to operational technology security)

### MCF-SEC-004

**Break-Glass Governance** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure emergency accounts and procedures across OT, infrastructure and control planes work when central identity fails, are protected against misuse, and every use is reviewed.

**Requirement.** The infrastructure security owner shall govern break-glass arrangements for all in-scope domains: inventory of emergency accounts, storage under dual control with an offline copy outside the failure domains they recover, use triggers, notification on use, maximum duration, mandatory post-use review and credential rotation. The infrastructure security owner shall verify at a defined interval that break-glass retrieval and login work with the primary identity provider and vault unavailable, and shall review all uses.

**Assessment criteria**

1. Break-glass inventory covers OT, BMC, network, hypervisor/Kubernetes, cluster manager and storage domains.
2. Credentials are under dual control with an offline copy located outside recovered failure domains.
3. Use triggers alerts to the security function in real time.
4. Every use in the period was reviewed and followed by rotation within the deadline.
5. Retrieval and login tests with primary identity and vault unavailable succeeded in the interval.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Break-glass rotation after use | h | 24 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Break-glass inventory and storage arrangements
- Alerting configuration
- Use, review and rotation records
- Retrieval/login test records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | EMERGENCY; FAILED; RECOVERY |
| periodCoverage | 12 months (illustrative) of uses; test within 12 months. |
| independence | Use reviews by security function independent of the user. |
| mandatoryItems | Use and review records; Retrieval test record |
| acceptableAlternatives |  |
| unknownEffect | US3; US4 against CG-10 if no tested emergency access exists for recovery-critical control planes. |
| reassessmentTriggers | Use event; Vault change; Identity provider change; Holder change |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, TEST, ANALYSIS

**Assessment procedure**

1. Review inventory coverage across domains.
2. Inspect storage and offline copy location against fault domains.
3. Verify alerting on use.
4. Sample uses for review and rotation.
5. Review retrieval test.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to all in-scope domains. Network-specific break-glass implementation is NET-016.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** EMERGENCY, FAILED, RECOVERY

**Failure modes addressed.** Offline copy stored in the data centre it recovers; Silent break-glass use; Emergency account used as routine admin

**Testing safety.** Retrieval tests shall not disable production identity; simulate unavailability for the test client only, and rotate credentials afterwards.

**UNKNOWN rule.** Domains without a tested break-glass path are recorded with U1 for recovery claims.

**Ontology classes.** Safeguard, Event, Dependency · **Related controls.** MCF-NET-016, MCF-SEC-003, MCF-RES-013, MCF-SEC-001

**Informative references.** NIST SP 800-53 Rev. 5 (Security and privacy controls); ISA/IEC 62443-3-3 (System security requirements and security levels); NIST SP 800-82 Rev. 3 (Guide to operational technology security)

## SEC-02 Control-plane protection

### MCF-SEC-005

**BMS and EPMS Security** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure building management, electrical power monitoring, CDU and PLC/SCADA systems that monitor and command power and cooling are secured to a target security level appropriate to their consequence, so compromise or misuse cannot defeat electrical or thermal continuity.

**Requirement.** The OT security owner shall perform a security risk assessment for BMS, EPMS, CDU controllers, PLCs, SCADA servers, historians and engineering workstations using a zone-and-conduit approach consistent with ISA/IEC 62443, assign a target security level (SL-T) to each zone, and implement countermeasures across the foundational requirement areas (identification and authentication, use control, system integrity, data confidentiality, restricted data flow, timely response to events, resource availability). The facility owner shall ensure that safety-instrumented and protection functions (electrical protection relays, emergency shutdown, hardwired interlocks) are independent of BMS/EPMS networks, and the OT security owner shall verify by test that unauthorised write or command attempts against controllers are blocked or detected and that controllers fail to a defined safe state on loss of supervisory communication.

**Assessment criteria**

1. A security risk assessment exists for BMS/EPMS/CDU/PLC assets with zones, conduits and assigned SL-T.
2. Achieved countermeasures are assessed against SL-T for each foundational requirement area, with gaps recorded.
3. Protection relays, emergency shutdown and hardwired interlocks do not depend on BMS/EPMS network availability or integrity.
4. Default credentials are absent and engineering protocols (for example BACnet, Modbus/TCP) are restricted to defined conduits.
5. Tests confirmed that unauthorised write/command attempts from outside permitted conduits are blocked or alarmed.
6. Controllers fail to the defined safe state (for example last good setpoint, mechanical fail-safe position) on loss of supervisory communication, verified by test or vendor-witnessed evidence.
7. Controller logic and firmware changes are detected (checksum or version monitoring).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Target security level for power and cooling control zones | SL (ISA/IEC 62443) | SL-T 2 minimum; SL-T 3 for zones whose compromise defeats CG-05/CG-06 (illustrative) | Assigned by risk assessment per ISA/IEC 62443-3-2. |
| Controller logic integrity check interval | days | 7 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- OT security risk assessment with zone/conduit model and SL-T
- SL gap assessment against foundational requirements
- Independence analysis for protection and safety functions
- Credential and protocol configuration evidence
- Write/command blocking test results
- Fail-safe behaviour test or witnessed vendor evidence
- Logic/firmware integrity monitoring records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED; EMERGENCY |
| periodCoverage | Tests within 12 months (illustrative); integrity monitoring for 90 days. |
| independence | Testing by an OT security specialist independent of the BMS/EPMS integrator. |
| mandatoryItems | Risk assessment with SL-T; Protection-independence analysis; Write/command blocking test; Fail-safe evidence |
| acceptableAlternatives | Test on a representative OT test bench with identical firmware and configuration, plus production configuration review |
| unknownEffect | US4: CG-07 cannot PASS while BMS/EPMS write/command exposure or fail-safe behaviour is unverified (scenario X05). |
| reassessmentTriggers | Controller firmware or logic change; New integration (for example IT/OT data export); Integrator change; OT security incident |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, ANALYSIS, TEST, RECONCILIATION

**Assessment procedure**

1. Review the risk assessment, zone/conduit model and SL-T assignments.
2. Review SL gap assessment by foundational requirement area.
3. Trace protection and safety functions to confirm independence from BMS/EPMS networks.
4. Inspect credential and protocol restrictions on a sample of controllers.
5. Review or witness write/command blocking tests from non-permitted zones.
6. Review fail-safe evidence and logic integrity monitoring.

**Gate mappings.** CG-07 Critical control-system integrity (CRITICAL); CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-05 Resilient electrical supply (SUPPORTING); CG-06 Thermal continuity (SUPPORTING)

**Applicability.** Applies to all BMS, EPMS, CDU, PLC, SCADA, historian and OT engineering systems supporting in-scope power and cooling. Where operated by a colocation provider, evidence rights are required (DEP-018, SUP-006).

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, DEGRADED, EMERGENCY

**Failure modes addressed.** Malicious setpoint change causing cooling loss at load; EPMS compromise masking electrical alarms; Protection logic dependent on BMS network; Default credentials on CDU controller; Controller failing to unsafe state on comms loss

**Testing safety.** No active scanning, fuzzing, write or command test shall be performed against production BMS/EPMS/CDU/PLC systems without written authorisation from the facility owner and OT security owner, plant in a safe state, operator presence, and vendor consultation; passive monitoring and test-bench testing are preferred. Fail-safe tests that remove supervisory communication require engineering authorisation and a defined restoration plan.

**UNKNOWN rule.** If controller logic integrity or fail-safe state cannot be established, record U8 at US4 against CG-07; do not infer from vendor marketing material.

**Ontology classes.** InfrastructureSystem, Safeguard, Threat, FaultDomain, TestRecord · **Related controls.** MCF-SEC-009, MCF-SEC-023, MCF-POW-021, MCF-THM-021, MCF-THM-022

**Informative references.** ISA/IEC 62443-3-2 (Security risk assessment, zones and conduits); ISA/IEC 62443-3-3 (System security requirements and security levels); ISA/IEC 62443-4-2 (Technical security requirements for IACS components); NIST SP 800-82 Rev. 3 (Guide to operational technology security); MITRE ATT&CK for ICS (knowledge base)

### MCF-SEC-006

**Cluster Manager Security** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure the AI control plane (Kubernetes or HPC scheduler, cluster manager, provisioning and image services, hypervisor managers) cannot be used to gain unbounded authority over compute, data and connected infrastructure.

**Requirement.** The platform security lead shall harden each cluster manager and control plane to a documented benchmark (for example CIS Kubernetes Benchmark where applicable), restrict API server and scheduler administrative access to brokered privileged paths, enforce admission control that blocks privileged containers, host-namespace access and unapproved images on accelerator nodes, protect control-plane state stores (for example etcd) with encryption and access restriction, and separate tenant-facing from infrastructure-administrative interfaces. The platform security lead shall test at a defined interval that a tenant or workload identity cannot escalate to node, cluster-admin or BMC authority.

**Assessment criteria**

1. Control-plane hardening against a documented benchmark is assessed with deviations recorded.
2. Administrative API access is restricted to brokered privileged paths.
3. Admission control blocks privileged pods, host mounts and unapproved images on accelerator nodes (verified by test).
4. Control-plane state stores are encrypted and access-restricted.
5. Tenant-facing and administrative interfaces are separated.
6. Escalation tests in the interval found no path from tenant workload to node, cluster-admin or BMC authority, or Findings were raised.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Escalation test interval | months | 12 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Hardening benchmark assessment
- API access configuration
- Admission policy and rejection logs
- State store protection evidence
- Escalation test reports

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; RECOVERY |
| periodCoverage | Test within interval; admission logs 90 days. |
| independence | Escalation tests by an independent tester. |
| mandatoryItems | Escalation test report; Admission policy evidence |
| acceptableAlternatives |  |
| unknownEffect | US4: CG-15 cannot PASS while tenant-to-infrastructure escalation paths are untested. |
| reassessmentTriggers | Control-plane version upgrade; New tenant model; Admission policy change |

**Assessment methods.** INSPECTION, TEST, DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Review hardening assessment and deviations.
2. Inspect administrative access paths.
3. Test admission control with prohibited workload specifications in a test namespace.
4. Review state store protection.
5. Review escalation test reports.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (CRITICAL); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all cluster managers, schedulers and hypervisor managers controlling in-scope compute.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, RECOVERY

**Failure modes addressed.** Privileged container giving node root and BMC reach; Exposed etcd; Cluster-admin token leaked; Unapproved image with tampered drivers

**Testing safety.** Escalation tests shall run in designated test namespaces or clusters under written authorisation; no tests shall modify production workloads or node firmware.

**UNKNOWN rule.** Where the control plane is provider-managed and escalation testing is not permitted, record U2 and require provider assurance (E5).

**Ontology classes.** InfrastructureSystem, Safeguard, Threat, TestRecord · **Related controls.** MCF-SEC-003, MCF-CMP-010, MCF-SEC-002, MCF-SEC-010

**Informative references.** CIS Kubernetes Benchmark; NIST SP 800-190 (Application container security guide); NIST SP 800-207 (Zero trust architecture)

### MCF-SEC-007

**Fabric Controller Security** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure fabric controllers, subnet managers, SDN controllers and network automation platforms are protected so that their compromise cannot reconfigure, partition or blackhole fabrics.

**Requirement.** The infrastructure security owner shall ensure fabric controllers, subnet managers and network automation platforms are reachable only from the management zone, use individually attributable and brokered administrative access, authenticate southbound connections to devices (for example certificate-based gNMI/NETCONF), protect fabric security keys (for example InfiniBand management and partition keys), and log all configuration actions to the security telemetry platform. The fabric operations lead shall reconcile controller access configuration to this requirement at a defined interval.

**Assessment criteria**

1. Controllers and automation platforms are reachable only from the management zone (verified).
2. Administrative access is individually attributable and brokered.
3. Southbound device connections are authenticated and encrypted where supported.
4. Fabric security keys are managed and not left at defaults.
5. All configuration actions are logged to security telemetry.

**Minimum evidence**

- Controller network access configuration
- Administrative access configuration
- Southbound authentication configuration
- Key management evidence
- Configuration action logs

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Reconciliation within 90 days (illustrative). |
| independence | Reconciliation by security function. |
| mandatoryItems | Access configuration; Action logs |
| acceptableAlternatives |  |
| unknownEffect | US3: unknown controller exposure conditions CG-15 and CG-08 claims. |
| reassessmentTriggers | Controller upgrade; Automation platform change |

**Assessment methods.** INSPECTION, RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Inspect network reachability of controllers.
2. Review administrative access and logging.
3. Review southbound authentication and keys.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to fabric controllers, subnet managers and network automation affecting in-scope fabrics. Resilience of controllers is NET-021.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Default management key enabling rogue subnet manager; Automation platform compromised to push malicious config; Unauthenticated southbound sessions

**Testing safety.** Non-intrusive configuration review; do not attempt rogue subnet-manager tests on production fabrics.

**UNKNOWN rule.** If default fabric keys cannot be ruled out, record U7 against fabric integrity.

**Ontology classes.** InfrastructureSystem, Safeguard, Interface · **Related controls.** MCF-NET-021, MCF-NET-022, MCF-SEC-010, MCF-SEC-023

**Informative references.** InfiniBand Trade Association, InfiniBand Architecture Specification (Volumes 1 and 2); OpenConfig gNMI specification and OpenConfig data models; ISA/IEC 62443-3-3 (System security requirements and security levels)

### MCF-SEC-008

**Storage Controller Security** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure storage management planes cannot be used to destroy, encrypt or exfiltrate training data, checkpoints and model artefacts, and that destructive operations require additional protection.

**Requirement.** The storage platform owner shall restrict storage controller and management interfaces to the management zone with brokered privileged access, shall require multi-person approval or delayed execution for destructive operations (volume or bucket deletion, snapshot or retention policy reduction, replication break), shall protect immutable recovery copies with retention locks that administrators cannot shorten, and shall log management actions to security telemetry.

**Assessment criteria**

1. Storage management interfaces are reachable only from the management zone.
2. Privileged storage access is brokered and attributable.
3. Destructive operations require multi-person approval or delayed execution.
4. Immutable recovery copies have retention locks not reducible by administrators (verified configuration).
5. Management actions are logged to security telemetry.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Destructive-operation delay | h | 24 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Storage management access configuration
- Destructive-operation approval configuration
- Retention lock configuration
- Management action logs

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; RECOVERY |
| periodCoverage | Configuration within 90 days (illustrative). |
| independence | Configuration extracted by assessor. |
| mandatoryItems | Retention lock configuration; Destructive-operation protection configuration |
| acceptableAlternatives |  |
| unknownEffect | US3; US4 against CG-10 where checkpoint recovery copies lack immutability. |
| reassessmentTriggers | Storage platform change; Retention policy change |

**Assessment methods.** INSPECTION, RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Inspect management reachability.
2. Review privileged access.
3. Verify destructive-operation protection.
4. Verify retention locks.
5. Review logging.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-10 Recovery readiness (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to storage platforms holding in-scope training data, checkpoints and model artefacts.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, RECOVERY

**Failure modes addressed.** Compromised admin deleting all snapshots; Ransomware encrypting checkpoint tier; Retention lock shortened by admin

**Testing safety.** Do not execute destructive operations to test protections; use a test volume in a non-production namespace.

**UNKNOWN rule.** If immutability cannot be verified, treat recovery copies as mutable (U7) in recovery analysis.

**Ontology classes.** InfrastructureSystem, Safeguard, Resource · **Related controls.** MCF-STO-016, MCF-STO-013, MCF-RES-016, MCF-SEC-003

**Informative references.** NIST SP 800-53 Rev. 5 (Security and privacy controls); ISO/IEC 27002 (Information security controls)

## SEC-03 Network security and segmentation

### MCF-SEC-009

**Security Zoning** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure the facility OT, infrastructure management, AI control-plane, tenant and corporate environments are partitioned into security zones with defined conduits, so that compromise in one zone cannot reach consequential authority in another.

**Requirement.** The infrastructure security owner shall maintain a zone-and-conduit model covering facility OT (BMS, EPMS, CDU, PLC, fire and physical security integrations), infrastructure management (BMC, PDU, switch management, OOB), AI control planes, storage management, tenant and corporate networks and external connections, with each conduit's permitted flows, protocols and direction, and the security level target per zone. The OT security owner shall reconcile the as-built network (firewall rules, VLAN/VRF configuration, physical links, wireless and cellular devices) to the model at a defined interval and after change, and shall record every undocumented path (including dual-homed hosts and vendor-installed modems) as a Finding.

**Assessment criteria**

1. A zone-and-conduit model covers all listed environments with permitted flows and SL-T.
2. Firewall, VLAN/VRF and routing configuration reconcile to the model.
3. Dual-homed hosts, unmanaged switches, wireless and cellular devices bridging zones are discovered and dispositioned.
4. Conduits between OT and IT pass through defined boundary devices (for example an industrial DMZ) with no direct routed path.
5. Reconciliation was performed in the interval and after material change.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Zone reconciliation interval | months | 6 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Zone-and-conduit model
- Configuration reconciliation report
- Passive discovery results (for example network traffic analysis) for undocumented paths
- Disposition of discovered bridging devices

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Reconciliation within interval; passive discovery covering at least 30 days (illustrative). |
| independence | Reconciliation and discovery by a party independent of the network implementers. |
| mandatoryItems | Zone-and-conduit model; Configuration reconciliation; Discovery results |
| acceptableAlternatives | Physical inspection of OT network cabinets for undocumented links where passive monitoring is not deployed |
| unknownEffect | US4: CG-07 cannot PASS while an undocumented path into a power or cooling control zone cannot be ruled out. |
| reassessmentTriggers | New integration between zones; Vendor installation; Firewall platform change; Discovery of bridging device |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS, INSPECTION, OBSERVATION

**Assessment procedure**

1. Review the zone-and-conduit model against the environment inventory.
2. Reconcile firewall, VLAN/VRF and routing configuration to permitted conduits.
3. Review passive discovery for undocumented flows and bridging devices.
4. Inspect a sample of OT cabinets for unmanaged switches and modems.
5. Confirm dispositions of discovered paths.

**Gate mappings.** CG-07 Critical control-system integrity (CRITICAL); CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-09 Failure containment (SUPPORTING)

**Applicability.** Applies to all in-scope sites and environments. Physical zoning is PHY-009; this control covers network and logical zones.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Vendor cellular modem bridging BMS to internet; Dual-homed historian linking corporate IT and OT; Flat management network spanning BMC and BMS; Unreviewed any-any rule in conduit

**Testing safety.** Discovery in OT zones shall be passive (traffic mirroring) unless active scanning is authorised in writing by the facility owner and OT security owner after vendor consultation; active scans of controllers can disrupt them.

**UNKNOWN rule.** Zones without discovery coverage are recorded with U5 and treated as potentially bridged in authority-path analysis.

**Ontology classes.** FaultDomain, Interface, Safeguard, ArchitectureSnapshot · **Related controls.** MCF-SEC-010, MCF-SEC-011, MCF-SEC-005, MCF-PHY-009, MCF-NET-013

**Informative references.** ISA/IEC 62443-3-2 (Security risk assessment, zones and conduits); ISA/IEC 62443-3-3 (System security requirements and security levels); NIST SP 800-82 Rev. 3 (Guide to operational technology security); NIST SP 800-207 (Zero trust architecture)

### MCF-SEC-010

**Management-Plane Segmentation** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure management planes (BMC/IPMI/Redfish, switch management, PDU, hypervisor and Kubernetes administrative APIs, storage management) are segmented so that tenant, workload and corporate networks cannot reach them, and so that one management plane cannot be used to pivot to another.

**Requirement.** The infrastructure security owner shall segment each management plane into its own zone, shall disable insecure management protocols (for example IPMI over LAN where Redfish is available, unauthenticated SNMP versions, Telnet), shall restrict BMC access to brokered administrative paths, and shall prevent host operating systems from reaching their own or other BMCs over the network except where required and approved. The infrastructure security owner shall test at a defined interval from representative tenant, workload and corporate vantage points that management interfaces are unreachable and that pivoting between management planes is blocked.

**Assessment criteria**

1. Each management plane is a distinct zone with permitted conduits only.
2. Insecure management protocols are disabled on BMCs, switches and PDUs (sampled configuration).
3. Host-to-BMC network access and in-band BMC interfaces are disabled or approved.
4. Reachability tests from tenant, workload and corporate vantage points found no management interface reachable.
5. Pivot tests between management planes (for example BMC zone to OT zone) found paths blocked.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Management segmentation test interval | months | 6 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Management zone design
- Protocol configuration samples
- Reachability and pivot test reports

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; RECOVERY |
| periodCoverage | Test within interval. |
| independence | Tests by security function or independent tester. |
| mandatoryItems | Reachability test report; Pivot test report |
| acceptableAlternatives | Rule-base analysis with path computation tooling where active tests are not authorised |
| unknownEffect | US4: CG-15 cannot PASS while BMC or control-plane reachability from tenant workloads is untested. |
| reassessmentTriggers | New hardware generation; Network redesign; Tenant model change |

**Assessment methods.** TEST, INSPECTION, ANALYSIS

**Assessment procedure**

1. Review management zone design.
2. Sample protocol configuration on BMCs, switches and PDUs.
3. Run or review reachability tests from tenant, workload and corporate vantage points.
4. Run or review pivot tests between management planes.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (CRITICAL); CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies to all management planes of in-scope infrastructure.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, RECOVERY

**Failure modes addressed.** Tenant workload reaching BMCs and reflashing firmware; IPMI cipher weaknesses exploited; Pivot from BMC zone to BMS; PDU web interface reachable from corporate network

**Testing safety.** Reachability and pivot tests shall attempt connection only and shall not authenticate or issue commands; they require written authorisation from the security owner, and from the facility owner for any test touching OT zones.

**UNKNOWN rule.** Vantage points not tested are recorded with U5; untested pairs of management planes are treated as connected.

**Ontology classes.** FaultDomain, Interface, Safeguard, TestRecord · **Related controls.** MCF-NET-013, MCF-SEC-009, MCF-SEC-003, MCF-SEC-011

**Informative references.** DMTF DSP0266 (Redfish specification); ISA/IEC 62443-3-3 (System security requirements and security levels); NIST SP 800-53 Rev. 5 (Security and privacy controls); NIST SP 800-207 (Zero trust architecture)

### MCF-SEC-011

**Filtering and Gateways** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure conduits between zones are enforced by managed boundary devices whose rule sets are minimal, reviewed and monitored, including industrial DMZs, unidirectional gateways and API gateways for automation.

**Requirement.** The security operations manager shall operate boundary devices on every conduit in the zone model with deny-by-default rule sets, documented business justification and owner for each rule, review of rules at a defined interval, removal of unused rules, and logging of denied and permitted consequential flows to security telemetry. The OT security owner shall use unidirectional or protocol-break gateways where the zone model requires one-way data export from power and cooling control zones.

**Assessment criteria**

1. Every conduit is enforced by a managed boundary device with deny-by-default.
2. Each rule has justification and owner; any-any or overly broad rules are absent or approved.
3. Rule reviews occurred in the interval with unused rules removed.
4. Required unidirectional or protocol-break gateways are deployed for OT data export.
5. Boundary logs are forwarded to security telemetry.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Rule review interval | months | 6 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Boundary device inventory mapped to conduits
- Rule sets with justification
- Rule review records
- Gateway deployment evidence
- Log forwarding configuration

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | 12 months (illustrative) of reviews. |
| independence | Rule analysis by assessor using exported rule sets. |
| mandatoryItems | Rule sets; Review records |
| acceptableAlternatives |  |
| unknownEffect | US3: unreviewed rules condition CG-07/CG-15 evaluation. |
| reassessmentTriggers | New conduit; Boundary platform change; Incident |

**Assessment methods.** ANALYSIS, DOCUMENT_REVIEW, SAMPLING

**Assessment procedure**

1. Map boundary devices to conduits.
2. Analyse rule sets for breadth and justification.
3. Review rule review records.
4. Verify gateways for OT export.
5. Check log forwarding.

**Gate mappings.** CG-07 Critical control-system integrity (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to every conduit in the SEC-009 model.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Temporary vendor rule left open; Bidirectional path where one-way export intended; Rule sprawl hiding consequential paths

**Testing safety.** Rule analysis is offline; any active validation follows SEC-010 testing restrictions.

**UNKNOWN rule.** Conduits without an identified enforcing device are treated as open (U1).

**Ontology classes.** Safeguard, Interface, AssetInstance · **Related controls.** MCF-SEC-009, MCF-SEC-010, MCF-NET-011, MCF-SEC-017

**Informative references.** ISA/IEC 62443-3-3 (System security requirements and security levels); NIST SP 800-82 Rev. 3 (Guide to operational technology security); NIST SP 800-53 Rev. 5 (Security and privacy controls)

### MCF-SEC-012

**Remote Access** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure all remote access to OT, infrastructure management and AI control planes, especially by vendors and OEMs, is brokered, approved per session, time-bound, monitored and revocable.

**Requirement.** The infrastructure security owner shall permit remote access to in-scope systems only through a managed remote-access gateway that enforces individual identity, MFA, per-session approval by the system owner for vendor and OEM access, time limits, session recording and the ability to terminate sessions in real time, and shall prohibit persistent vendor connections, vendor-installed remote-access tools and modems. The OT security owner shall require that remote sessions to power and cooling control systems with write or command capability are supervised by an on-site or on-shift authorised operator.

**Assessment criteria**

1. All remote access paths to in-scope systems traverse the managed gateway (no alternative paths found in discovery).
2. Vendor/OEM sessions require per-session approval and are time-limited.
3. Sessions are recorded and can be terminated in real time (demonstrated).
4. Persistent vendor connections and unmanaged remote tools are absent.
5. Remote write/command sessions to OT systems were supervised (sampled).
6. Revocation of a vendor's access takes effect within the defined time (tested).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum vendor session duration | h | 8 (illustrative) | Capability-profile parameter. |
| Revocation effect time | min | 15 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Remote access architecture
- Gateway configuration
- Session approval and recording samples
- Discovery results for alternative paths
- Revocation test record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Six months (illustrative) of sessions; revocation test within 12 months. |
| independence | Discovery and revocation tests by security function. |
| mandatoryItems | Session approval and recording samples; Discovery results; Revocation test |
| acceptableAlternatives |  |
| unknownEffect | US4: CG-15 cannot PASS while an unmanaged remote path into OT or control planes cannot be ruled out. |
| reassessmentTriggers | New vendor support contract; Remote access platform change; Discovery of unmanaged path |

**Assessment methods.** TEST, SAMPLING, INSPECTION, ANALYSIS

**Assessment procedure**

1. Review remote access architecture.
2. Review discovery results for alternative paths and vendor tools.
3. Sample sessions for approval, recording and supervision.
4. Witness real-time termination and revocation test.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (CRITICAL); CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies to all remote access to in-scope OT, management and control-plane systems. Supplier-side identity and contractual obligations are SUP-021 to SUP-024.

**Lifecycle stages.** COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Always-on OEM VPN to BMS; Vendor remote tool installed on HMI; Compromised vendor account issuing commands; Session not terminable

**Testing safety.** Revocation tests shall use a designated test vendor account; do not terminate live vendor sessions supporting active work without coordinating with the system owner.

**UNKNOWN rule.** If discovery has not covered all OT zones, record U5 at US4 against CG-15.

**Ontology classes.** Interface, Safeguard, Dependency, TestRecord · **Related controls.** MCF-SUP-021, MCF-SUP-022, MCF-SUP-023, MCF-SUP-024, MCF-SEC-003

**Informative references.** ISA/IEC 62443-2-4 (Security programme requirements for IACS service providers); ISA/IEC 62443-3-3 (System security requirements and security levels); NIST SP 800-82 Rev. 3 (Guide to operational technology security); NIST SP 800-207 (Zero trust architecture)

## SEC-04 Configuration, vulnerability and patching

### MCF-SEC-013

**Secure Baseline** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure OT controllers, BMCs, accelerator nodes, NICs, switches and control-plane hosts run hardened configurations and integrity-verified firmware with secure boot, so that tampered or insecure states are prevented or detected.

**Requirement.** The infrastructure security owner shall define secure configuration baselines for each in-scope device class, including disabled unused services, credential policy, logging, and for firmware-bearing devices the approved signed firmware versions, secure boot enablement, firmware rollback protection and measured boot where supported. The platform security lead shall verify compliance with the baseline at a defined interval using automated assessment or attestation and shall record non-compliant devices as Findings.

**Assessment criteria**

1. Secure baselines exist for each device class including firmware and boot-integrity settings.
2. Secure boot is enabled on devices that support it (sampled or attested).
3. Firmware versions match approved signed versions; unsigned or unknown firmware is absent.
4. Firmware rollback protection is enabled where supported.
5. Compliance assessment ran in the interval with non-compliance tracked.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Baseline compliance assessment interval | days | 30 (illustrative) | Capability-profile parameter. |
| Baseline compliance target | % devices compliant | 98 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Secure baselines per device class
- Compliance assessment reports
- Firmware inventory with signature status
- Secure boot and attestation evidence

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; RECOVERY |
| periodCoverage | Assessment within interval. |
| independence | Assessor reperforms compliance checks on a sample. |
| mandatoryItems | Compliance reports; Firmware inventory |
| acceptableAlternatives | Manual inspection of OT controller firmware versions where automated assessment is unavailable |
| unknownEffect | US3; US4 against CG-07 where OT controller firmware integrity is unknown. |
| reassessmentTriggers | New device class; Firmware release; Baseline change |

**Assessment methods.** INSPECTION, REPERFORMANCE, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Review baselines per device class.
2. Review compliance reports and reperform on sample.
3. Check firmware signature status and secure boot.
4. Review non-compliance tracking.

**Gate mappings.** CG-07 Critical control-system integrity (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-08 Compute, storage and network functional integrity (SUPPORTING)

**Applicability.** Applies to all in-scope device classes.

**Lifecycle stages.** DESIGN, BUILD, COMMISSION, OPERATE · **Operating states.** NORMAL, MAINTENANCE, RECOVERY

**Failure modes addressed.** Secure boot disabled on accelerator nodes; Unsigned BMC firmware; Firmware downgrade to vulnerable version; Insecure services enabled on controllers

**Testing safety.** Compliance checks shall be read-only; firmware updates are not part of this control.

**UNKNOWN rule.** Devices whose firmware cannot be read are treated as non-compliant (U1).

**Ontology classes.** ArchitectureSnapshot, Safeguard, AssetInstance · **Related controls.** MCF-CMP-013, MCF-SUP-014, MCF-NET-022, MCF-SEC-002

**Informative references.** NIST SP 800-193 (Platform firmware resiliency guidelines); Trusted Computing Group TPM 2.0 Library Specification; DMTF DSP0274 (Security Protocol and Data Model, SPDM); ISA/IEC 62443-4-2 (Technical security requirements for IACS components); NIST SP 800-53 Rev. 5 (Security and privacy controls)

### MCF-SEC-014

**Vulnerability Management** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure vulnerabilities in OT, infrastructure management, firmware and AI control-plane components are identified, prioritised by exploitability and infrastructure consequence, and remediated or mitigated within defined times.

**Requirement.** The security operations manager shall maintain vulnerability visibility for all in-scope asset classes (including passive or vendor-advisory-based identification for OT assets that cannot be actively scanned), shall prioritise using exploitation evidence (for example known-exploited catalogues) and infrastructure consequence (reachability to CG-05/CG-06/CG-07/CG-15 authority), and shall meet remediation or mitigation times defined per priority. The security operations manager shall report overdue items to governance.

**Assessment criteria**

1. Vulnerability identification covers all in-scope asset classes with method stated (scan, agent, passive, advisory).
2. Prioritisation considers exploitation evidence and infrastructure consequence.
3. Remediation or mitigation times are met per priority (sampled).
4. Overdue items are reported and have exceptions (SEC-016).
5. OT vendor advisories are monitored and assessed.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Remediation time for known-exploited vulnerabilities on reachable management planes | days | 14 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Coverage report by asset class
- Prioritisation method
- Remediation SLA reports
- Overdue reports
- Advisory monitoring records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Six months (illustrative). |
| independence | Assessor samples from asset inventory. |
| mandatoryItems | Coverage report; Remediation SLA reports |
| acceptableAlternatives |  |
| unknownEffect | US3: unknown vulnerability state conditions CG-07/CG-15 evaluation. |
| reassessmentTriggers | New asset class; Critical advisory |

**Assessment methods.** ANALYSIS, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Compare coverage with asset inventory.
2. Review prioritisation method.
3. Sample vulnerabilities for SLA adherence.
4. Review advisory monitoring.

**Gate mappings.** CG-07 Critical control-system integrity (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to all in-scope assets.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Exploitable BMC vulnerability unpatched; OT asset blind spot; Prioritisation ignoring consequence

**Testing safety.** Active scanning of OT assets is prohibited unless authorised in writing by the facility owner after vendor consultation; prefer passive identification.

**UNKNOWN rule.** Assets without any identification method are recorded with U5.

**Ontology classes.** Threat, AssetInstance, Finding · **Related controls.** MCF-SEC-015, MCF-SEC-016, MCF-SUP-016

**Informative references.** NIST SP 800-40 Rev. 4 (Guide to enterprise patch management planning); CISA Known Exploited Vulnerabilities catalogue; IEC TR 62443-2-3 (Patch management in the IACS environment); NIST SP 800-82 Rev. 3 (Guide to operational technology security)

### MCF-SEC-015

**Patch Governance** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure security patches and firmware updates to OT and infrastructure are tested for compatibility and operational impact, staged to avoid common-mode failure, and applied within defined times.

**Requirement.** The change authority shall require that patches and firmware updates to OT controllers, BMCs, NICs, switches, accelerator nodes and control planes are tested on representative test systems, approved by the system owner and, for OT, the vendor where required, applied in stages that never update all redundant members or all fault domains simultaneously, and verified after application with rollback available. The security operations manager shall measure patch latency against defined targets.

**Assessment criteria**

1. Patches are tested on representative test systems before production.
2. OT patches have vendor compatibility confirmation where required.
3. Staging prevents simultaneous update of all redundant members or fault domains.
4. Post-patch verification and rollback availability are recorded.
5. Patch latency meets targets or exceptions exist.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum fraction of a redundancy group patched in one stage | % | 50 (illustrative) | Avoids common-mode failure (X08). |

**Minimum evidence**

- Patch test records
- Vendor compatibility confirmations
- Staged change records
- Post-patch verification
- Patch latency reports

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | MAINTENANCE; TRANSITION; NORMAL |
| periodCoverage | Six months (illustrative). |
| independence | Assessor samples from deployed version changes. |
| mandatoryItems | Staged change records; Test records |
| acceptableAlternatives |  |
| unknownEffect | US3; CG-14 SUPPORTING evaluation. |
| reassessmentTriggers | Patch-induced incident; Process change |

**Assessment methods.** SAMPLING, DOCUMENT_REVIEW, RECONCILIATION

**Assessment procedure**

1. Identify version changes from inventories.
2. Trace to test, approval and staging records.
3. Check redundancy-group staging.
4. Review latency.

**Gate mappings.** CG-14 Change control (SUPPORTING); CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies to all patching of in-scope assets.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** MAINTENANCE, TRANSITION, NORMAL

**Failure modes addressed.** Firmware update bricking all CDU controllers; Patch applied to both PLC redundant pair; Untested BMC update breaking node boot

**Testing safety.** Patch testing shall be on test systems; production pilots follow change control.

**UNKNOWN rule.** Version changes without matching records are Findings.

**Ontology classes.** Action, AssetInstance, TestRecord · **Related controls.** MCF-SEC-014, MCF-CMP-015, MCF-NET-022, MCF-OPS-018

**Informative references.** IEC TR 62443-2-3 (Patch management in the IACS environment); NIST SP 800-40 Rev. 4 (Guide to enterprise patch management planning); NIST SP 800-82 Rev. 3 (Guide to operational technology security)

### MCF-SEC-016

**Exception and Compensating Control** · DIRECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure security exceptions (unpatchable OT, legacy protocols, missing MFA) are approved by appropriate authority, time-bound and backed by verified compensating controls.

**Requirement.** The infrastructure security owner shall maintain a security exception register for in-scope systems recording the deviation, risk assessment including infrastructure consequence, compensating controls, approver at the authority level required by consequence, and expiry. The infrastructure security owner shall verify compensating controls are in place before approval and at renewal.

**Assessment criteria**

1. All known deviations are in the register.
2. Approvals match the required authority for the consequence.
3. Compensating controls were verified before approval and at renewal.
4. No exceptions are expired without renewal.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum exception duration | months | 12 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Exception register
- Approval records
- Compensating-control verification records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E4 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE |
| periodCoverage | Current register; 12 months of approvals (illustrative). |
| independence | Assessor cross-checks deviations from SEC-013/SEC-014 against the register. |
| mandatoryItems | Exception register; Verification records |
| acceptableAlternatives |  |
| unknownEffect | US3: unapproved deviations condition the decision. |
| reassessmentTriggers | Exception expiry; New deviation |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INSPECTION

**Assessment procedure**

1. Reconcile deviations to the register.
2. Check approval authority.
3. Inspect compensating controls for a sample.
4. Check expiries.

**Gate mappings.** CG-07 Critical control-system integrity (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to all in-scope security deviations.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE

**Failure modes addressed.** Indefinite exception for legacy HMI; Compensating control never implemented; Approver lacking authority

**Testing safety.** Inspection only.

**UNKNOWN rule.** Deviations not in the register are Findings; compensating controls not verified are recorded as U1.

**Ontology classes.** Finding, Safeguard, Control · **Related controls.** MCF-GOV-011, MCF-SEC-013, MCF-SEC-014

**Informative references.** ISO/IEC 27001 (Information security management systems); ISA/IEC 62443-2-1 (Security programme requirements for IACS asset owners)

## SEC-05 Detection and response

### MCF-SEC-017

**Security Telemetry** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure security-relevant logs and events from OT, management planes, control planes, remote access and identity systems are collected centrally with integrity, time synchronisation and retention sufficient for detection and investigation.

**Requirement.** The security operations manager shall collect security telemetry from identity providers, PAM, remote-access gateways, boundary devices, BMCs, network devices, fabric controllers, cluster managers, storage controllers and OT passive monitoring (including controller write and program-change events), with time synchronised to NET-024 sources, integrity protection, and retention per the evidence retention class, and shall monitor source health and alert on silent sources.

**Assessment criteria**

1. Telemetry sources cover all listed classes with gaps recorded.
2. OT passive monitoring captures controller write and program-change events.
3. Timestamps are synchronised and offsets monitored.
4. Logs are integrity-protected and retained per class.
5. Silent-source alerts operate and gaps are investigated.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Silent-source alert threshold | min | 60 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Source coverage report
- OT monitoring coverage
- Time synchronisation evidence
- Integrity and retention configuration
- Source health alerts

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F3 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY; RECOVERY |
| periodCoverage | 90 days (illustrative). |
| independence | Assessor queries telemetry platform directly. |
| mandatoryItems | Coverage report; Source health records |
| acceptableAlternatives |  |
| unknownEffect | US2 for confidence; US3 where OT write events are not visible. |
| reassessmentTriggers | New source class; Platform change |

**Assessment methods.** ANALYSIS, SAMPLING, INSPECTION

**Assessment procedure**

1. Compare sources to inventory.
2. Query sample events from each class.
3. Check time offset and integrity.
4. Review silent-source alerts.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies to all in-scope security-relevant systems.

**Lifecycle stages.** COMMISSION, OPERATE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY, RECOVERY

**Failure modes addressed.** BMC logs not collected; OT program change invisible; Logs alterable by attacker; Silent source unnoticed

**Testing safety.** Passive OT monitoring via traffic mirroring only.

**UNKNOWN rule.** Source classes without collection are recorded with U5.

**Ontology classes.** EvidenceObject, Safeguard, Event · **Related controls.** MCF-SEC-018, MCF-NET-023, MCF-NET-024, MCF-EVA-006

**Informative references.** NIST SP 800-92 (Guide to computer security log management); NIST SP 800-82 Rev. 3 (Guide to operational technology security); ISA/IEC 62443-3-3 (System security requirements and security levels)

### MCF-SEC-018

**Behaviour Detection** · DETECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure detection of anomalous or malicious behaviour against infrastructure authority, including unexpected OT writes, BMC firmware operations, mass configuration changes, privilege escalation and anomalous automation actions.

**Requirement.** The security operations manager shall maintain detection use cases mapped to infrastructure threat scenarios (for example ATT&CK for ICS techniques and AIDCF-004 scenarios X05, X08, X15), covering unexpected controller writes or program changes, BMC firmware update or power commands outside change windows, mass configuration pushes, privilege escalation, anomalous remote sessions and automation acting outside its scope, and shall validate detection effectiveness by safe simulation at a defined interval.

**Assessment criteria**

1. Detection use cases map to listed infrastructure scenarios.
2. Use cases cover OT writes, BMC operations, mass config, privilege escalation, remote sessions and automation scope violations.
3. Simulations in the interval demonstrated detection and alert triage within target time.
4. Missed detections were remediated.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Detection-to-triage target | min | 15 (illustrative) | Capability-profile parameter. |
| Detection validation interval | months | 6 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Use case catalogue with mapping
- Simulation records and results
- Remediation records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Simulations within interval. |
| independence | Simulations designed by red/purple team independent of detection engineers. |
| mandatoryItems | Simulation results |
| acceptableAlternatives | Analysed real detections covering the same use cases |
| unknownEffect | US3: untested detection reduces CG-15 confidence. |
| reassessmentTriggers | New scenario; Detection platform change; Missed detection |

**Assessment methods.** TEST, DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Review use case mapping.
2. Review or witness simulations.
3. Measure detection-to-triage times.
4. Review remediation of misses.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies to all in-scope infrastructure authority.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Unexpected setpoint write undetected; Mass firmware push unnoticed; Agent acting outside scope undetected

**Testing safety.** Simulations on OT shall replay benign traffic or use test benches; never issue real writes to production controllers. Simulations require written authorisation from the security owner and facility owner.

**UNKNOWN rule.** Use cases never validated are recorded with U8.

**Ontology classes.** Safeguard, Threat, TestRecord · **Related controls.** MCF-SEC-017, MCF-SEC-019, MCF-SEC-021

**Informative references.** MITRE ATT&CK for ICS (knowledge base); NIST SP 800-61 Rev. 3 (Incident response recommendations); NIST SP 800-82 Rev. 3 (Guide to operational technology security)

### MCF-SEC-019

**Incident Containment** · CORRECTIVE · claim type RESILIENCE · required AL5

**Objective.** Ensure cyber and cyber-physical incidents affecting infrastructure can be contained without causing unsafe states or unnecessary loss of AI service, with pre-approved containment actions and safety-coordinated decision-making.

**Requirement.** The security operations manager shall maintain incident playbooks for infrastructure scenarios (BMS/EPMS compromise, BMC compromise, control-plane compromise, malicious automation, vendor account compromise) that define pre-approved containment actions (credential revocation, conduit closure, session termination, controller isolation to local or manual control), the safety checks required before each action, and the decision authority. The facility owner shall ensure that OT containment actions are coordinated with facility operations so that isolating supervisory control does not remove cooling or power continuity, and the security operations manager shall exercise the playbooks at a defined interval.

**Assessment criteria**

1. Playbooks exist for each listed scenario with containment actions, safety checks and authority.
2. OT containment actions specify the safe fallback (local/manual control, last-good setpoints) and facility operations role.
3. Containment actions are technically available (for example conduit closure capability verified).
4. Exercises in the interval executed containment decisions and actions (or simulations) within target time.
5. Containment does not depend on systems likely to be compromised in the scenario.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Containment decision time target | min | 30 (illustrative) | Capability-profile parameter. |
| Playbook exercise interval | months | 12 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Infrastructure incident playbooks
- Safe fallback definitions
- Containment capability verification
- Exercise records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | EMERGENCY; DEGRADED; RECOVERY |
| periodCoverage | Exercise within interval. |
| independence | Exercises observed by an independent party. |
| mandatoryItems | Playbooks; Exercise records; Safe fallback definitions |
| acceptableAlternatives | Analysed real incidents demonstrating containment |
| unknownEffect | US3; US4 against CG-09 for cyber-physical scenarios with no exercised containment. |
| reassessmentTriggers | New scenario; Incident; Facility control architecture change |

**Assessment methods.** DOCUMENT_REVIEW, SCENARIO_EXERCISE, TEST, INQUIRY

**Assessment procedure**

1. Review playbooks for scenarios, actions, safety checks and authority.
2. Review safe fallback definitions with facility operations.
3. Verify containment capability.
4. Review exercise records.
5. Check dependencies of containment actions.

**Gate mappings.** CG-09 Failure containment (SUPPORTING); CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-07 Critical control-system integrity (SUPPORTING); CG-10 Recovery readiness (SUPPORTING)

**Applicability.** Applies to all in-scope infrastructure.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** EMERGENCY, DEGRADED, RECOVERY

**Failure modes addressed.** Isolating BMS causes cooling loss; Containment relies on compromised identity provider; No authority to sever vendor access; Delayed decision allows spread

**Testing safety.** Containment exercises on OT shall be simulations or tabletop unless live isolation to local control is authorised by the facility owner with operators in attendance and plant in a stable state.

**UNKNOWN rule.** Scenarios without an exercised playbook are recorded with U1.

**Ontology classes.** Safeguard, Action, FailureScenario · **Related controls.** MCF-RES-019, MCF-RES-021, MCF-SEC-018, MCF-SEC-020, MCF-OPS-014

**Informative references.** NIST SP 800-61 Rev. 3 (Incident response recommendations); NIST SP 800-82 Rev. 3 (Guide to operational technology security); ISA/IEC 62443-2-1 (Security programme requirements for IACS asset owners)

### MCF-SEC-020

**Forensic Readiness** · DETECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that evidence needed to investigate infrastructure incidents (logs, controller programs, firmware images, session recordings) is preserved with chain of custody and that collection does not endanger operations.

**Requirement.** The security operations manager shall define forensic collection procedures for each in-scope system class, including OT controllers and BMCs, specifying what to collect, how to collect safely, and chain-of-custody requirements, and shall ensure retention and legal hold capability for telemetry and session recordings. The OT security owner shall ensure baseline copies of controller programs and firmware hashes are available for comparison.

**Assessment criteria**

1. Collection procedures exist per system class including OT and BMC.
2. Procedures specify safe collection methods.
3. Chain-of-custody and legal hold capability exist.
4. Baseline controller programs and firmware hashes are available.

**Minimum evidence**

- Forensic procedures
- Chain-of-custody templates and tooling
- Legal hold capability evidence
- Baseline program and hash repository

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E5; E6 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S3 |
| stateCoverage | EMERGENCY; RECOVERY |
| periodCoverage | Current. |
| independence | Reviewed by forensic specialist. |
| mandatoryItems | Procedures; Baseline repository |
| acceptableAlternatives |  |
| unknownEffect | US2: affects investigation confidence; US3 if baseline programs are absent. |
| reassessmentTriggers | New system class; Incident |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION

**Assessment procedure**

1. Review procedures per class.
2. Inspect chain-of-custody tooling and legal hold.
3. Verify baseline repository contents for a sample.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies to all in-scope system classes.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** EMERGENCY, RECOVERY

**Failure modes addressed.** Evidence destroyed during recovery; Unsafe collection disrupting controller; No baseline to detect logic tampering

**Testing safety.** Forensic collection from OT controllers shall use vendor-supported read methods only.

**UNKNOWN rule.** Classes without collection procedures are recorded with U1.

**Ontology classes.** EvidenceObject, Safeguard · **Related controls.** MCF-SEC-017, MCF-EVA-006, MCF-SEC-019

**Informative references.** NIST SP 800-86 (Guide to integrating forensic techniques into incident response); NIST SP 800-61 Rev. 3 (Incident response recommendations); NIST SP 800-82 Rev. 3 (Guide to operational technology security)

## SEC-06 AI-enabled and automated action

### MCF-SEC-021

**Agent or Automation Authority** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure every AI agent, automation pipeline and closed-loop controller that can act on infrastructure has an explicit, bounded and inventoried authority scope, so that tool-mediated actions cannot exceed what the owner approved.

**Requirement.** The automation owner shall register every agent, automation and closed-loop control that can observe, configure, command, bypass, update or recover infrastructure (including AIOps remediation, cooling optimisation loops, power capping, network automation and AI agents with tool access), stating its effective identity, tools and APIs, target systems, permitted actions, rate and magnitude limits, operating states in which it may act, and its human owner. The infrastructure security owner shall reconcile registered scope with effective permissions at a defined interval and shall prohibit any automation from holding cross-domain command or bypass authority without approval under SEC-003.

**Assessment criteria**

1. All automations and agents with infrastructure authority are registered with identity, tools, targets, actions, limits, states and owner.
2. Effective permissions reconcile to registered scope (no excess).
3. Rate and magnitude limits (for example maximum setpoint change, maximum nodes acted on) are enforced technically.
4. Automation is restricted to declared operating states (for example disabled in EMERGENCY unless approved).
5. No automation holds unapproved cross-domain command or bypass authority.
6. Telemetry-to-command coupling is analysed for sensor-trust dependency (AIDCF-005 pattern).

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum automated setpoint change per interval | units per min | System-specific (illustrative: 1 °C per 5 min for supply temperature) | Capability-profile parameter set by engineering authority. |
| Maximum nodes acted on per automated action | count | Fault-domain size (illustrative) | Limits blast radius. |

**Minimum evidence**

- Automation and agent authority register
- Effective permission reconciliation
- Limit enforcement configuration
- State restriction configuration
- Telemetry-to-command analysis

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3; E7 |
| optionalClasses | E4 |
| qualityFloor | P3 F3 C3 R3 T3 I2 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE; EMERGENCY |
| periodCoverage | Reconciliation within 90 days (illustrative). |
| independence | Reconciliation by security function independent of automation owners. |
| mandatoryItems | Authority register; Effective permission reconciliation |
| acceptableAlternatives | Graph-based authority path analysis per AIDCF-005 with human review |
| unknownEffect | US4: CG-15 cannot PASS while any automation or agent with consequential infrastructure authority is unregistered or unreconciled. |
| reassessmentTriggers | New agent or automation; New tool or API granted; Model or prompt change to an agent with infrastructure tools |

**Assessment methods.** RECONCILIATION, ANALYSIS, INSPECTION, DOCUMENT_REVIEW

**Assessment procedure**

1. Discover automations and agents from identity, API gateway and controller logs.
2. Compare with the register.
3. Compute effective permissions and reconcile to scope.
4. Inspect technical limit and state enforcement.
5. Review telemetry-to-command analysis.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (CRITICAL); CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies to every automated or AI-enabled actor with any authority beyond OBSERVE over in-scope infrastructure.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE, EMERGENCY

**Failure modes addressed.** AIOps agent with power-cycle rights over all nodes; Cooling optimiser driven by spoofed sensors; Agent inheriting operator's full privileges; Automation acting during EMERGENCY

**Testing safety.** Reconciliation is read-only; do not invoke agent tools against production systems to test scope.

**UNKNOWN rule.** Automations discovered in logs but not registered are recorded as US4 UNKNOWN (U1) against CG-15 until registered and reconciled.

**Ontology classes.** Safeguard, Interface, Dependency, InfrastructureSystem · **Related controls.** MCF-SEC-022, MCF-SEC-023, MCF-SEC-024, MCF-SEC-002, MCF-THM-021

**Informative references.** AIDCF-005 (AIDCF–AI Trust Graph Integration Standard); NIST AI 100-1 (AI Risk Management Framework); OWASP Top 10 for Large Language Model Applications; NIST SP 800-207 (Zero trust architecture)

### MCF-SEC-022

**Approval Controls** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure consequential automated or agent-initiated infrastructure actions require human approval proportionate to consequence, and that approvals cannot be bypassed.

**Requirement.** The automation owner shall classify each automated action by consequence and reversibility and shall require human approval (single or dual) for actions above the defined threshold, such as OT setpoint or mode changes beyond limits, power-cycling beyond one fault domain, firmware updates, fabric-wide configuration pushes and destructive storage operations. The infrastructure security owner shall verify by test that approval cannot be bypassed by the automation's own identity.

**Assessment criteria**

1. Actions are classified by consequence and reversibility.
2. Approval requirements are defined per class.
3. Approval enforcement is technical, outside the automation's control.
4. Tests confirmed approval cannot be bypassed.
5. Approval records exist for sampled consequential actions.

**Minimum evidence**

- Action classification
- Approval configuration
- Bypass test results
- Approval records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Test within 12 months (illustrative); records for 90 days. |
| independence | Bypass tests by security function. |
| mandatoryItems | Bypass test results |
| acceptableAlternatives |  |
| unknownEffect | US3; US4 against CG-15 where OT command approvals are self-enforced by the agent. |
| reassessmentTriggers | New action class; Automation platform change |

**Assessment methods.** TEST, SAMPLING, DOCUMENT_REVIEW

**Assessment procedure**

1. Review classification.
2. Inspect approval enforcement architecture.
3. Review or witness bypass tests in a test environment.
4. Sample approval records.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-14 Change control (SUPPORTING)

**Applicability.** Applies to automation and agents registered under SEC-021 whose actions are classified above the lowest consequence class.

**Lifecycle stages.** DESIGN, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Agent self-approves; Approval fatigue rubber-stamping; Approval enforced only in prompt instructions

**Testing safety.** Bypass tests in test environment only.

**UNKNOWN rule.** Approvals enforced only by agent instructions or prompts are treated as absent (U8).

**Ontology classes.** Safeguard, Action, TestRecord · **Related controls.** MCF-SEC-021, MCF-SEC-023, MCF-RES-023

**Informative references.** AIDCF-005 (AIDCF–AI Trust Graph Integration Standard); NIST AI 100-1 (AI Risk Management Framework); OWASP Top 10 for Large Language Model Applications

### MCF-SEC-023

**Command Allowlisting** · PREVENTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure that only explicitly allowlisted commands, write operations and parameter ranges can be issued to power, cooling and critical infrastructure controllers by any automated or remote actor, enforced at a point the actor cannot modify.

**Requirement.** The OT security owner shall enforce, at a boundary or broker the actor cannot modify (for example an OT protocol-aware gateway, a command broker or controller-level write protection), an allowlist of permitted commands, registers or objects, and parameter ranges for writes to BMS, EPMS, CDU and PLC systems from automation, agents and remote sessions, and shall block or require approval for anything outside the list. The OT security owner shall test at a defined interval that out-of-list writes and out-of-range values are blocked and alarmed.

**Assessment criteria**

1. Allowlists exist for each automation/remote actor writing to OT systems, covering commands, objects and ranges.
2. Enforcement is at a point outside the actor's control.
3. Out-of-list and out-of-range attempts are blocked and alarmed (test results).
4. Allowlists are reviewed with engineering authority after control-logic changes.
5. Controller-level write protection (for example key switch or run mode) is used where supported.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Allowlist test interval | months | 6 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Allowlist definitions
- Enforcement architecture
- Test results
- Review records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5 |
| qualityFloor | P3 F4 C3 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; MAINTENANCE; EMERGENCY |
| periodCoverage | Test within interval. |
| independence | Testing by OT security specialist independent of the automation owner. |
| mandatoryItems | Test results; Allowlist definitions |
| acceptableAlternatives | Test-bench testing with identical gateway configuration |
| unknownEffect | US4: CG-07 cannot PASS while automated or remote writes to power/cooling controllers are unrestricted or untested. |
| reassessmentTriggers | Control-logic change; New automation; Gateway change |

**Assessment methods.** TEST, INSPECTION, DOCUMENT_REVIEW

**Assessment procedure**

1. Review allowlists per actor.
2. Inspect enforcement point.
3. Review or witness block tests on test bench or under authorisation.
4. Review allowlist reviews after logic changes.

**Gate mappings.** CG-07 Critical control-system integrity (CRITICAL); CG-15 Integrated digital authority over infrastructure (SUPPORTING)

**Applicability.** Applies wherever automation, agents or remote sessions can write to in-scope OT controllers.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE, CHANGE · **Operating states.** NORMAL, MAINTENANCE, EMERGENCY

**Failure modes addressed.** Agent writing unsafe CDU flow setpoint; Remote session changing protection mode; Malicious write to chiller sequencing

**Testing safety.** Block tests against production controllers shall use benign out-of-list requests that the gateway intercepts, with operator presence and facility owner authorisation; test benches are preferred.

**UNKNOWN rule.** If enforcement sits within the actor's own software, record U8 and treat writes as unrestricted.

**Ontology classes.** Safeguard, Interface, TestRecord · **Related controls.** MCF-SEC-005, MCF-SEC-021, MCF-SEC-022, MCF-THM-021

**Informative references.** ISA/IEC 62443-3-3 (System security requirements and security levels); NIST SP 800-82 Rev. 3 (Guide to operational technology security); AIDCF-005 (AIDCF–AI Trust Graph Integration Standard)

### MCF-SEC-024

**Safe Rollback** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure automated or agent-initiated infrastructure changes can be detected, halted and reversed to a known-safe state quickly, including when the automation itself has failed or been compromised.

**Requirement.** The automation owner shall provide, for every registered automation and agent, a kill switch that halts its actions without depending on the automation itself, a record of actions taken sufficient to reverse them, and a defined safe state (for example last approved setpoints, previous configuration) for each target. The automation owner shall test at a defined interval that the kill switch halts actions within target time and that rollback restores the safe state, coordinating OT rollback with facility operations.

**Assessment criteria**

1. Every registered automation has an independent kill switch.
2. Action logs are sufficient for reversal.
3. Safe states are defined per target.
4. Tests in the interval demonstrated halt within target time and rollback to safe state.
5. OT rollback procedures are coordinated with facility operations.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Kill-switch halt time | s | 60 (illustrative) | Capability-profile parameter. |

**Minimum evidence**

- Kill switch design
- Action logs
- Safe state definitions
- Halt and rollback test records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5; E7 |
| qualityFloor | P4 F4 C4 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; EMERGENCY; RECOVERY; DEGRADED |
| periodCoverage | Test within 12 months (illustrative). |
| independence | Tests witnessed by security and facility operations. |
| mandatoryItems | Halt and rollback test records |
| acceptableAlternatives |  |
| unknownEffect | US3; US4 against CG-15 for automations with OT command authority lacking tested halt. |
| reassessmentTriggers | New automation; Automation platform change; Incident involving automation |

**Assessment methods.** TEST, DOCUMENT_REVIEW, SCENARIO_EXERCISE

**Assessment procedure**

1. Review kill switch independence.
2. Review action log completeness.
3. Review safe state definitions.
4. Review or witness halt and rollback tests.

**Gate mappings.** CG-15 Integrated digital authority over infrastructure (SUPPORTING); CG-10 Recovery readiness (SUPPORTING); CG-07 Critical control-system integrity (SUPPORTING)

**Applicability.** Applies to every automation and agent registered under SEC-021, including vendor-supplied optimisation loops embedded in BMS or CDU controllers.

**Lifecycle stages.** DESIGN, COMMISSION, OPERATE · **Operating states.** NORMAL, EMERGENCY, RECOVERY, DEGRADED

**Failure modes addressed.** Runaway automation power-cycling nodes; Kill switch dependent on compromised platform; Rollback restores corrupt state

**Testing safety.** Halt and rollback tests on OT targets require facility owner authorisation and operator presence; prefer test benches.

**UNKNOWN rule.** Automations without tested halt are recorded with U1.

**Ontology classes.** Safeguard, Action, TestRecord · **Related controls.** MCF-SEC-021, MCF-RES-015, MCF-NET-022, MCF-CMP-016

**Informative references.** AIDCF-005 (AIDCF–AI Trust Graph Integration Standard); NIST AI 100-1 (AI Risk Management Framework); NIST SP 800-82 Rev. 3 (Guide to operational technology security)
