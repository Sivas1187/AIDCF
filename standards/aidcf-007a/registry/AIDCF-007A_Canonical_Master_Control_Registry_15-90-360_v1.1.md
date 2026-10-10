# AIDCF-007A Canonical Master Control Registry 15-90-360 v1.1

Markdown rendering of `AIDCF-007A_Canonical_Master_Control_Registry_15-90-360_v1.1.xlsx`. The workbook is the authoritative source.

## Sheets

- [README](#readme)
- [Summary](#summary)
- [Domains](#domains)
- [Families](#families)
- [Control Registry](#control-catalogues) (in the workbook; rendered per domain)
- [Evidence Profiles](#control-catalogues) (in the workbook; rendered per domain)
- [Gate Mapping](#control-catalogues) (in the workbook; rendered per domain)
- [Critical Gates](#critical-gates)
- [Parameters](#control-catalogues) (in the workbook; rendered per domain)
- [Assessment Template](#control-catalogues) (in the workbook; rendered per domain)
- [Amendment Log](#amendment-log)

## README

| Topic | Guidance |
|---|---|
| Registry | AIDCF-007A Canonical Master Control Registry, version 1.1 (amendment AIDCF-007A-AMD-002), 2026-10-10. |
| Status | PROPOSED - Draft for controlled review. Version 1.0 (AIDCF-007A-AMD-001) remains the approved cardinality and identifier baseline until v1.1 completes controlled methodology review and independent ratification. |
| What changed in v1.1 | Control content rewritten per control (objective, requirement, criteria, parameters, evidence profile, procedure, testing safety, UNKNOWN rule); IDs and 15/90/360 structure unchanged; duplicate titles fixed (MCF-NET-004, MCF-STO-019); control-specific gate mappings with CRITICAL/SUPPORTING roles replace whole-domain mapping; Required Assurance Level assigned per control from its claim type (AL2-AL5). |
| Gate roll-up | A gate cannot PASS unless every in-scope CRITICAL control is CONFORMING at its required claim type; PARTIAL never yields PASS. SUPPORTING controls inform the gate evaluation. CG-11 and CG-12 are meta-gates evaluated across all controls. See AIDCF-010. |
| Vocabularies | All codes are canonical per AIDCF-002 and registries/vocabularies/. |
| Constitutional rule | Controls do not create assurance by existence. Missing evidence is UNKNOWN, not N/A. Scores never override gates (AIDCF-006). |
| Parameters | Engineering values are capability-profile parameters; defaults are illustrative unless attributed to a named source. |
| Machine-readable copies | registries/controls/controls.json (full), controls.csv, gate-mappings.csv, evidence-profiles.csv, parameters.csv. |

## Summary

| Metric | Value |
|---|---|
| Domains | 15 |
| Families | 90 |
| Controls | 360 |
| Controls per family | 4 |
| Unique titles | 360 |
| CRITICAL gate mappings | 106 |
| SUPPORTING gate mappings | 483 |
| Claim type DESIGN | 52 |
| Claim type IMPLEMENTATION | 94 |
| Claim type OPERATION | 133 |
| Claim type EFFECTIVENESS | 52 |
| Claim type RESILIENCE | 29 |

## Domains

| Domain Code | Domain | Families | Controls | Gates with CRITICAL controls |
|---|---|---|---|---|
| GOV | Governance, Accountability and Assurance Direction | 6 | 24 | CG-13 |
| CAP | AI Capability, Service Outcome and Demand Management | 6 | 24 | CG-01; CG-02; CG-13; CG-14 |
| DEP | Dependency, Concentration and External Reliance Management | 6 | 24 | CG-02; CG-03; CG-13 |
| PHY | Physical Site, Building and Security Infrastructure | 6 | 24 | CG-04; CG-09 |
| POW | Electrical Power Infrastructure and Energy Continuity | 6 | 24 | CG-04; CG-05; CG-07; CG-09; CG-10 |
| THM | Cooling, Thermal and Fluid Infrastructure | 6 | 24 | CG-04; CG-06; CG-07; CG-09; CG-10 |
| ENV | Environmental and Resource Performance | 6 | 24 | CG-04 |
| CMP | AI Compute Infrastructure | 6 | 24 | CG-08; CG-09; CG-10; CG-14 |
| STO | AI Storage and Data Infrastructure | 6 | 24 | CG-08; CG-09; CG-10 |
| NET | AI Network and Interconnect Architecture | 6 | 24 | CG-08; CG-09; CG-10; CG-14 |
| OPS | Building Operations and Service Management | 6 | 24 | CG-04; CG-07; CG-13; CG-14 |
| RES | Resilience, Continuity and Recovery | 6 | 24 | CG-09; CG-10 |
| SUP | Supply Chain, OEM and Ecosystem Assurance | 6 | 24 | CG-03; CG-15 |
| SEC | Digital, OT and Control-Plane Security | 6 | 24 | CG-07; CG-15 |
| EVA | Evidence, Assessment and Assurance Management | 6 | 24 | CG-01; CG-02 |

## Families

| Family ID | Domain Code | Control Family | Controls | Gates with CRITICAL controls |
|---|---|---|---|---|
| GOV-01 | GOV | Governance architecture | MCF-GOV-001 Governance Charter; MCF-GOV-002 Decision Rights; MCF-GOV-003 Committee Oversight; MCF-GOV-004 Methodology Ownership | CG-13 |
| GOV-02 | GOV | Accountability and responsibility | MCF-GOV-005 RACI and Role Ownership; MCF-GOV-006 Critical Function Accountability; MCF-GOV-007 Risk Acceptance Authority; MCF-GOV-008 Evidence Custody | CG-13 |
| GOV-03 | GOV | Policy and standards management | MCF-GOV-009 Policy Hierarchy; MCF-GOV-010 Technical Standard Baselines; MCF-GOV-011 Exception Governance; MCF-GOV-012 Document Lifecycle |  |
| GOV-04 | GOV | Risk and assurance governance | MCF-GOV-013 Assurance Plan; MCF-GOV-014 Risk Appetite Linkage; MCF-GOV-015 Critical Gate Governance; MCF-GOV-016 Independent Review |  |
| GOV-05 | GOV | Stakeholder and regulatory interface | MCF-GOV-017 Stakeholder Obligations; MCF-GOV-018 Regulatory Monitoring; MCF-GOV-019 Customer Commitments; MCF-GOV-020 External Reporting |  |
| GOV-06 | GOV | Ethics, impartiality and competence | MCF-GOV-021 Conflict Management; MCF-GOV-022 Assessor Independence; MCF-GOV-023 Competence Management; MCF-GOV-024 Appeal and Challenge |  |
| CAP-01 | CAP | Capability inventory | MCF-CAP-001 Capability Register; MCF-CAP-002 Capability Ownership; MCF-CAP-003 Lifecycle Status; MCF-CAP-004 Architecture Linkage | CG-01; CG-02; CG-13 |
| CAP-02 | CAP | Service outcome definition | MCF-CAP-005 Availability Outcomes; MCF-CAP-006 Performance Outcomes; MCF-CAP-007 Integrity Outcomes; MCF-CAP-008 Recovery Outcomes | CG-01 |
| CAP-03 | CAP | Criticality and materiality | MCF-CAP-009 Criticality Criteria; MCF-CAP-010 Impact Tolerance; MCF-CAP-011 Stakeholder Consequence; MCF-CAP-012 Priority Classification | CG-01 |
| CAP-04 | CAP | Demand and growth modelling | MCF-CAP-013 Current Demand Baseline; MCF-CAP-014 Peak and Transient Demand; MCF-CAP-015 Growth Forecast; MCF-CAP-016 Scenario Demand |  |
| CAP-05 | CAP | Operating envelope | MCF-CAP-017 Load Envelope; MCF-CAP-018 Environmental Envelope; MCF-CAP-019 Duration Limits; MCF-CAP-020 State-Specific Limits |  |
| CAP-06 | CAP | Capability lifecycle and change | MCF-CAP-021 Design-to-Operation Traceability; MCF-CAP-022 Commissioning Acceptance; MCF-CAP-023 Material Change Impact; MCF-CAP-024 Retirement Control | CG-14 |
| DEP-01 | DEP | Dependency discovery | MCF-DEP-001 Asset-to-Function Mapping; MCF-DEP-002 Upstream Dependency Mapping; MCF-DEP-003 Downstream Consequence Mapping; MCF-DEP-004 Recovery Dependency Mapping | CG-03 |
| DEP-02 | DEP | Shared and common-mode dependencies | MCF-DEP-005 Shared Source Analysis; MCF-DEP-006 Common Controller Analysis; MCF-DEP-007 Shared Route Analysis; MCF-DEP-008 Shared Human Dependency Analysis | CG-03 |
| DEP-03 | DEP | External providers and utilities | MCF-DEP-009 Utility Dependency; MCF-DEP-010 Telecom Dependency; MCF-DEP-011 OEM Dependency; MCF-DEP-012 Cloud and Service Dependency | CG-03 |
| DEP-04 | DEP | Concentration and substitutability | MCF-DEP-013 Capacity Concentration; MCF-DEP-014 Supplier Concentration; MCF-DEP-015 Knowledge Concentration; MCF-DEP-016 Substitution Readiness |  |
| DEP-05 | DEP | Boundary and interface control | MCF-DEP-017 Assessment Boundary; MCF-DEP-018 Provider Boundary; MCF-DEP-019 Tenant Boundary; MCF-DEP-020 Cross-Boundary Enforcement | CG-02; CG-03; CG-13 |
| DEP-06 | DEP | Dependency monitoring and review | MCF-DEP-021 Dependency Health Indicators; MCF-DEP-022 Provider Performance; MCF-DEP-023 Change Detection; MCF-DEP-024 Periodic Revalidation |  |
| PHY-01 | PHY | Site and location resilience | MCF-PHY-001 Site Hazard Assessment; MCF-PHY-002 External Exposure; MCF-PHY-003 Access and Logistics; MCF-PHY-004 Adjacent Risk |  |
| PHY-02 | PHY | Building and structural integrity | MCF-PHY-005 Structural Capacity; MCF-PHY-006 Rack Loading; MCF-PHY-007 Anchorage and Vibration; MCF-PHY-008 Building Envelope |  |
| PHY-03 | PHY | Physical zoning and segregation | MCF-PHY-009 Security Zones; MCF-PHY-010 Fire Zones; MCF-PHY-011 Water Zones; MCF-PHY-012 Tenant Segregation | CG-09 |
| PHY-04 | PHY | Access and surveillance | MCF-PHY-013 Identity-Based Access; MCF-PHY-014 Visitor Control; MCF-PHY-015 Surveillance Coverage; MCF-PHY-016 Alarm Response |  |
| PHY-05 | PHY | Asset movement and custody | MCF-PHY-017 Delivery Controls; MCF-PHY-018 Equipment Movement; MCF-PHY-019 Media Custody; MCF-PHY-020 Decommissioning Custody |  |
| PHY-06 | PHY | Fire, life safety and emergency interfaces | MCF-PHY-021 Fire Detection; MCF-PHY-022 Suppression Interfaces; MCF-PHY-023 Egress and Emergency Access; MCF-PHY-024 Emergency Shutdown Governance | CG-04 |
| POW-01 | POW | Utility and grid interface | MCF-POW-001 Utility Capacity; MCF-POW-002 Grid Quality; MCF-POW-003 Connection Reliability; MCF-POW-004 Utility Contingency | CG-05 |
| POW-02 | POW | Generation and fuel | MCF-POW-005 Generator Capacity; MCF-POW-006 Start Reliability; MCF-POW-007 Fuel Autonomy; MCF-POW-008 Fuel Replenishment | CG-05 |
| POW-03 | POW | UPS and energy storage | MCF-POW-009 UPS Topology; MCF-POW-010 Battery Condition; MCF-POW-011 Runtime and Derating; MCF-POW-012 Bypass Exposure | CG-04; CG-05 |
| POW-04 | POW | Distribution and protection | MCF-POW-013 Switchgear Integrity; MCF-POW-014 Selective Coordination; MCF-POW-015 Busway and PDU Capacity; MCF-POW-016 Earthing and Bonding | CG-04; CG-09 |
| POW-05 | POW | Power quality and transient response | MCF-POW-017 Voltage Quality; MCF-POW-018 Harmonics; MCF-POW-019 Transient Ride-Through; MCF-POW-020 Load-Step Response | CG-05 |
| POW-06 | POW | Electrical monitoring, maintenance and recovery | MCF-POW-021 EPMS Coverage; MCF-POW-022 Preventive Maintenance; MCF-POW-023 Switching Procedures; MCF-POW-024 Black-Start and Restoration | CG-04; CG-07; CG-10 |
| THM-01 | THM | Thermal architecture and capacity | MCF-THM-001 Heat-Load Model; MCF-THM-002 Design Capacity; MCF-THM-003 Resilient Capacity; MCF-THM-004 Seasonal Derating | CG-06 |
| THM-02 | THM | Air cooling systems | MCF-THM-005 Airflow Management; MCF-THM-006 Containment; MCF-THM-007 CRAH and In-Row Capacity; MCF-THM-008 Air-Side Monitoring |  |
| THM-03 | THM | Liquid cooling systems | MCF-THM-009 Direct-to-Chip Architecture; MCF-THM-010 CDU Capacity; MCF-THM-011 Secondary Loop Integrity; MCF-THM-012 Quick-Disconnect Management | CG-06 |
| THM-04 | THM | Heat rejection and water systems | MCF-THM-013 Chiller Capacity; MCF-THM-014 Cooling Tower or Dry Cooler; MCF-THM-015 Water Continuity; MCF-THM-016 Heat-Rejection Dependency | CG-06 |
| THM-05 | THM | Fluid quality and leak management | MCF-THM-017 Coolant Compatibility; MCF-THM-018 Water Quality; MCF-THM-019 Leak Detection; MCF-THM-020 Isolation and Drainage | CG-04; CG-09 |
| THM-06 | THM | Thermal control, maintenance and recovery | MCF-THM-021 Control Stability; MCF-THM-022 Sensor Trust; MCF-THM-023 Maintenance States; MCF-THM-024 Thermal Recovery | CG-07; CG-10 |
| ENV-01 | ENV | Environmental operating conditions | MCF-ENV-001 Temperature Control; MCF-ENV-002 Humidity Control; MCF-ENV-003 Particulate and Corrosion; MCF-ENV-004 Vibration and Acoustic Conditions |  |
| ENV-02 | ENV | Energy performance | MCF-ENV-005 PUE Measurement; MCF-ENV-006 Energy Allocation; MCF-ENV-007 Efficiency Under Load; MCF-ENV-008 Resilience-Efficiency Trade-Off |  |
| ENV-03 | ENV | Water performance | MCF-ENV-009 Water Source and Quality; MCF-ENV-010 WUE Measurement; MCF-ENV-011 Water Scarcity Response; MCF-ENV-012 Discharge Control |  |
| ENV-04 | ENV | Carbon and resource reporting | MCF-ENV-013 Carbon Accounting Boundary; MCF-ENV-014 Energy Attribute Evidence; MCF-ENV-015 Embodied Resource Data; MCF-ENV-016 Reporting Traceability |  |
| ENV-05 | ENV | Hazardous materials and waste | MCF-ENV-017 Battery Materials; MCF-ENV-018 Refrigerants and Coolants; MCF-ENV-019 Fuel and Suppressant Handling; MCF-ENV-020 Hardware and Media Waste | CG-04 |
| ENV-06 | ENV | Climate adaptation and resource continuity | MCF-ENV-021 Heatwave Readiness; MCF-ENV-022 Drought Readiness; MCF-ENV-023 Flood Adaptation; MCF-ENV-024 Long-Term Resource Constraints |  |
| CMP-01 | CMP | Compute architecture and configuration | MCF-CMP-001 Accelerator Architecture; MCF-CMP-002 Node Configuration; MCF-CMP-003 Rack-Scale Composition; MCF-CMP-004 Approved Baseline |  |
| CMP-02 | CMP | Cluster and scale-up domains | MCF-CMP-005 Cluster Topology; MCF-CMP-006 Scale-Up Domain Integrity; MCF-CMP-007 Partitioning; MCF-CMP-008 Fault-Domain Design | CG-08; CG-09 |
| CMP-03 | CMP | Capacity, scheduling and utilisation | MCF-CMP-009 Usable Accelerator Capacity; MCF-CMP-010 Scheduler Controls; MCF-CMP-011 Resource Reservation; MCF-CMP-012 Contention Management | CG-08 |
| CMP-04 | CMP | Firmware, driver and compatibility | MCF-CMP-013 Firmware Baseline; MCF-CMP-014 Driver Compatibility; MCF-CMP-015 Upgrade Testing; MCF-CMP-016 Rollback Readiness | CG-08; CG-14 |
| CMP-05 | CMP | Compute health and observability | MCF-CMP-017 GPU Telemetry; MCF-CMP-018 Node Health; MCF-CMP-019 Error and Degradation Detection; MCF-CMP-020 Performance Baselines | CG-08 |
| CMP-06 | CMP | Compute lifecycle and recovery | MCF-CMP-021 Provisioning; MCF-CMP-022 Spares and RMA; MCF-CMP-023 Node Rebuild; MCF-CMP-024 Secure Retirement | CG-10 |
| STO-01 | STO | Storage architecture and tiering | MCF-STO-001 Training Data Tier; MCF-STO-002 Checkpoint Tier; MCF-STO-003 Model and Artifact Tier; MCF-STO-004 Archive Tier |  |
| STO-02 | STO | Performance and capacity | MCF-STO-005 Throughput and IOPS; MCF-STO-006 Metadata Performance; MCF-STO-007 Capacity Headroom; MCF-STO-008 Burst Handling | CG-08 |
| STO-03 | STO | Integrity and consistency | MCF-STO-009 Data Integrity; MCF-STO-010 Metadata Integrity; MCF-STO-011 Checksum and Scrubbing; MCF-STO-012 Configuration Consistency | CG-08 |
| STO-04 | STO | Protection and replication | MCF-STO-013 Snapshot Protection; MCF-STO-014 Replication; MCF-STO-015 Erasure Coding; MCF-STO-016 Immutable Recovery Copy | CG-09; CG-10 |
| STO-05 | STO | Checkpoint and recovery services | MCF-STO-017 Checkpoint Durability; MCF-STO-018 Restart Readiness; MCF-STO-019 Storage Recovery Sequencing; MCF-STO-020 Recovery Validation | CG-08; CG-10 |
| STO-06 | STO | Storage monitoring and lifecycle | MCF-STO-021 Storage Telemetry; MCF-STO-022 Capacity Forecasting; MCF-STO-023 Media Health; MCF-STO-024 Secure Sanitisation |  |
| NET-01 | NET | Scale-up and scale-out fabrics | MCF-NET-001 Fabric Topology; MCF-NET-002 Path Diversity; MCF-NET-003 Oversubscription; MCF-NET-004 Fabric Fault-Domain Design | CG-08; CG-09 |
| NET-02 | NET | Performance and congestion control | MCF-NET-005 Latency Baseline; MCF-NET-006 Loss and Retransmission; MCF-NET-007 Congestion Control; MCF-NET-008 Collective Communication Performance | CG-08 |
| NET-03 | NET | Storage and service networks | MCF-NET-009 Storage Fabric; MCF-NET-010 Frontend Network; MCF-NET-011 Service Gateways; MCF-NET-012 Traffic Isolation | CG-08 |
| NET-04 | NET | Management and out-of-band networks | MCF-NET-013 Management Separation; MCF-NET-014 Console Access; MCF-NET-015 OOB Resilience; MCF-NET-016 Break-Glass Access | CG-10 |
| NET-05 | NET | Physical connectivity and optics | MCF-NET-017 Cabling Standards; MCF-NET-018 Optics Compatibility; MCF-NET-019 Cross-Connect Control; MCF-NET-020 Path Documentation |  |
| NET-06 | NET | Network control and observability | MCF-NET-021 Controller Resilience; MCF-NET-022 Configuration Management; MCF-NET-023 Flow Telemetry; MCF-NET-024 Time and Core Services | CG-14 |
| OPS-01 | OPS | Operating model and staffing | MCF-OPS-001 24x7 Coverage; MCF-OPS-002 Role Clarity; MCF-OPS-003 Shift Handover; MCF-OPS-004 Competence and Authorisation | CG-04; CG-13 |
| OPS-02 | OPS | Procedure and work control | MCF-OPS-005 Standard Operating Procedures; MCF-OPS-006 Method Statements; MCF-OPS-007 Permit to Work; MCF-OPS-008 Lockout and Tagout | CG-04; CG-14 |
| OPS-03 | OPS | Maintenance and reliability | MCF-OPS-009 Maintenance Strategy; MCF-OPS-010 Condition Monitoring; MCF-OPS-011 Calibration; MCF-OPS-012 Deferred Maintenance |  |
| OPS-04 | OPS | Alarm, incident and problem management | MCF-OPS-013 Alarm Rationalisation; MCF-OPS-014 Incident Response; MCF-OPS-015 Root Cause Analysis; MCF-OPS-016 Problem Elimination | CG-07 |
| OPS-05 | OPS | Change and configuration management | MCF-OPS-017 Configuration Baseline; MCF-OPS-018 Change Assessment; MCF-OPS-019 Temporary Configuration; MCF-OPS-020 Rollback and Validation | CG-14 |
| OPS-06 | OPS | Capacity and service operations | MCF-OPS-021 Capacity Review; MCF-OPS-022 Service Level Monitoring; MCF-OPS-023 Resource Balancing; MCF-OPS-024 Operational Reporting |  |
| RES-01 | RES | Resilience strategy | MCF-RES-001 Minimum Service Outcome; MCF-RES-002 Graceful Degradation; MCF-RES-003 Resilience Scenarios; MCF-RES-004 Resilience Ownership |  |
| RES-02 | RES | Fault-domain and containment design | MCF-RES-005 Fault-Domain Definition; MCF-RES-006 Containment Boundaries; MCF-RES-007 Blast Radius; MCF-RES-008 Isolation Validation | CG-09 |
| RES-03 | RES | Continuity planning | MCF-RES-009 Continuity Strategy; MCF-RES-010 Alternative Capacity; MCF-RES-011 Site and Provider Continuity; MCF-RES-012 Crisis Priorities |  |
| RES-04 | RES | Recovery planning | MCF-RES-013 Recovery Dependencies; MCF-RES-014 Recovery Sequencing; MCF-RES-015 Configuration Restoration; MCF-RES-016 Data and Checkpoint Recovery | CG-10 |
| RES-05 | RES | Testing and exercising | MCF-RES-017 Component Tests; MCF-RES-018 Integrated Scenario Tests; MCF-RES-019 Tabletop Exercises; MCF-RES-020 Lessons and Retest | CG-10 |
| RES-06 | RES | Crisis and adaptive response | MCF-RES-021 Crisis Command; MCF-RES-022 Stakeholder Communications; MCF-RES-023 Emergency Change; MCF-RES-024 Post-Event Adaptation |  |
| SUP-01 | SUP | Supplier due diligence | MCF-SUP-001 Supplier Capability; MCF-SUP-002 Financial and Operational Resilience; MCF-SUP-003 Security and Quality Posture; MCF-SUP-004 Sub-Tier Visibility | CG-03 |
| SUP-02 | SUP | Contract and service obligations | MCF-SUP-005 Service Levels; MCF-SUP-006 Evidence Rights; MCF-SUP-007 Incident Notification; MCF-SUP-008 Exit and Transition Rights |  |
| SUP-03 | SUP | Hardware and component provenance | MCF-SUP-009 Approved Sourcing; MCF-SUP-010 Counterfeit Prevention; MCF-SUP-011 Chain of Custody; MCF-SUP-012 Component Traceability |  |
| SUP-04 | SUP | Software, firmware and update supply | MCF-SUP-013 Release Provenance; MCF-SUP-014 Signature Validation; MCF-SUP-015 Compatibility Assurance; MCF-SUP-016 Vulnerability Response |  |
| SUP-05 | SUP | Spares, logistics and obsolescence | MCF-SUP-017 Critical Spares; MCF-SUP-018 Lead Times; MCF-SUP-019 Logistics Continuity; MCF-SUP-020 End-of-Life Planning |  |
| SUP-06 | SUP | Remote support and third-party access | MCF-SUP-021 Support Identity; MCF-SUP-022 Activation and Approval; MCF-SUP-023 Session Monitoring; MCF-SUP-024 Revocation and Review | CG-15 |
| SEC-01 | SEC | Identity and privileged access | MCF-SEC-001 Human Identity; MCF-SEC-002 Machine Identity; MCF-SEC-003 Privileged Access; MCF-SEC-004 Break-Glass Governance | CG-15 |
| SEC-02 | SEC | Control-plane protection | MCF-SEC-005 BMS and EPMS Security; MCF-SEC-006 Cluster Manager Security; MCF-SEC-007 Fabric Controller Security; MCF-SEC-008 Storage Controller Security | CG-07; CG-15 |
| SEC-03 | SEC | Network security and segmentation | MCF-SEC-009 Security Zoning; MCF-SEC-010 Management-Plane Segmentation; MCF-SEC-011 Filtering and Gateways; MCF-SEC-012 Remote Access | CG-07; CG-15 |
| SEC-04 | SEC | Configuration, vulnerability and patching | MCF-SEC-013 Secure Baseline; MCF-SEC-014 Vulnerability Management; MCF-SEC-015 Patch Governance; MCF-SEC-016 Exception and Compensating Control |  |
| SEC-05 | SEC | Detection and response | MCF-SEC-017 Security Telemetry; MCF-SEC-018 Behaviour Detection; MCF-SEC-019 Incident Containment; MCF-SEC-020 Forensic Readiness |  |
| SEC-06 | SEC | AI-enabled and automated action | MCF-SEC-021 Agent or Automation Authority; MCF-SEC-022 Approval Controls; MCF-SEC-023 Command Allowlisting; MCF-SEC-024 Safe Rollback | CG-07; CG-15 |
| EVA-01 | EVA | Evidence architecture | MCF-EVA-001 Evidence Taxonomy; MCF-EVA-002 Evidence Ownership; MCF-EVA-003 Evidence Repository; MCF-EVA-004 Retention and Protection |  |
| EVA-02 | EVA | Evidence provenance and quality | MCF-EVA-005 Source Provenance; MCF-EVA-006 Integrity and Custody; MCF-EVA-007 Relevance and Reliability; MCF-EVA-008 Currency and Coverage |  |
| EVA-03 | EVA | Assessment planning and execution | MCF-EVA-009 Decision Question; MCF-EVA-010 Scope and Criteria; MCF-EVA-011 Sampling and Testing; MCF-EVA-012 Specialist Involvement | CG-01; CG-02 |
| EVA-04 | EVA | Findings, UNKNOWN and limitations | MCF-EVA-013 Finding Traceability; MCF-EVA-014 UNKNOWN Preservation; MCF-EVA-015 Conflict Handling; MCF-EVA-016 Limitation Disclosure |  |
| EVA-05 | EVA | Critical gates and decisions | MCF-EVA-017 Gate Applicability; MCF-EVA-018 Gate Evidence; MCF-EVA-019 Independent Decision; MCF-EVA-020 Claim Language |  |
| EVA-06 | EVA | Reassessment and continuing assurance | MCF-EVA-021 Evidence Expiry; MCF-EVA-022 Change Triggers; MCF-EVA-023 Monitoring Coverage; MCF-EVA-024 Decision Suspension and Supersession |  |


## Control catalogues

The full content of the Control Registry, Evidence Profiles, Gate Mapping, Parameters and Assessment Template sheets is in the workbook and rendered per domain:

- [GOV](controls/AIDCF-007A_Controls_GOV_v1.1.md)
- [CAP](controls/AIDCF-007A_Controls_CAP_v1.1.md)
- [DEP](controls/AIDCF-007A_Controls_DEP_v1.1.md)
- [PHY](controls/AIDCF-007A_Controls_PHY_v1.1.md)
- [POW](controls/AIDCF-007A_Controls_POW_v1.1.md)
- [THM](controls/AIDCF-007A_Controls_THM_v1.1.md)
- [ENV](controls/AIDCF-007A_Controls_ENV_v1.1.md)
- [CMP](controls/AIDCF-007A_Controls_CMP_v1.1.md)
- [STO](controls/AIDCF-007A_Controls_STO_v1.1.md)
- [NET](controls/AIDCF-007A_Controls_NET_v1.1.md)
- [OPS](controls/AIDCF-007A_Controls_OPS_v1.1.md)
- [RES](controls/AIDCF-007A_Controls_RES_v1.1.md)
- [SUP](controls/AIDCF-007A_Controls_SUP_v1.1.md)
- [SEC](controls/AIDCF-007A_Controls_SEC_v1.1.md)
- [EVA](controls/AIDCF-007A_Controls_EVA_v1.1.md)

Machine-readable: `registries/controls/` (controls.json, controls.csv, gate-mappings.csv, evidence-profiles.csv, parameters.csv).

## Critical Gates

| Gate | Name | Scope | Evidence Floor | CRITICAL controls | SUPPORTING controls | CRITICAL control IDs |
|---|---|---|---|---|---|---|
| CG-01 | Capability and outcome definition | Capability Instance, Service Outcomes, tolerances, criticality and decision question are defined, owned and approved | S3 | 7 | 16 | MCF-CAP-001; MCF-CAP-005; MCF-CAP-006; MCF-CAP-007; MCF-CAP-008; MCF-CAP-010; MCF-EVA-009 |
| CG-02 | Boundary and architecture integrity | Assessment boundary, current architecture, as-built reconciliation and exclusions | S3 | 3 | 16 | MCF-CAP-004; MCF-DEP-017; MCF-EVA-010 |
| CG-03 | Critical dependency visibility | Material internal and external dependencies, common-mode exposure and concentration are identified and owned | S4 | 9 | 50 | MCF-DEP-001; MCF-DEP-002; MCF-DEP-005; MCF-DEP-007; MCF-DEP-009; MCF-DEP-010; MCF-DEP-012; MCF-DEP-017; MCF-SUP-004 |
| CG-04 | Life safety and hazardous energy | Fire, electrical arc-flash and shock, hazardous fluids and chemicals, confined space, refrigerants, battery thermal runaway and safe work | S4 | 13 | 24 | MCF-PHY-021; MCF-PHY-022; MCF-PHY-023; MCF-PHY-024; MCF-POW-010; MCF-POW-013; MCF-POW-016; MCF-POW-023; MCF-THM-018; MCF-ENV-018; MCF-OPS-004; MCF-OPS-007; MCF-OPS-008 |
| CG-05 | Resilient electrical supply | Utility, distribution, UPS/BESS, generation, fuel, protection and power quality sufficient for the Service Outcomes across operating states | S5 | 8 | 39 | MCF-POW-001; MCF-POW-005; MCF-POW-006; MCF-POW-007; MCF-POW-009; MCF-POW-011; MCF-POW-019; MCF-POW-020 |
| CG-06 | Thermal continuity | Heat-removal path (air, liquid, facility water, heat rejection) sufficient across operating states including transients | S5 | 7 | 46 | MCF-THM-002; MCF-THM-003; MCF-THM-004; MCF-THM-010; MCF-THM-011; MCF-THM-013; MCF-THM-015 |
| CG-07 | Critical control-system integrity | BMS, EPMS, CDU, PLC/SCADA and automation function safely, fail safe, and are configured and governed | S4 | 6 | 26 | MCF-POW-021; MCF-THM-021; MCF-OPS-013; MCF-SEC-005; MCF-SEC-009; MCF-SEC-023 |
| CG-08 | Compute, storage and network functional integrity | Accelerators, storage and fabrics deliver the required function, performance and integrity | S4 | 12 | 63 | MCF-CMP-006; MCF-CMP-009; MCF-CMP-013; MCF-CMP-019; MCF-STO-005; MCF-STO-009; MCF-STO-010; MCF-STO-017; MCF-NET-001; MCF-NET-007; MCF-NET-008; MCF-NET-009 |
| CG-09 | Failure containment | Fault domains, isolation and blast-radius limits prevent propagation beyond tolerance | S4 | 9 | 42 | MCF-PHY-010; MCF-POW-014; MCF-THM-020; MCF-CMP-008; MCF-STO-015; MCF-NET-004; MCF-RES-005; MCF-RES-007; MCF-RES-008 |
| CG-10 | Recovery readiness | Restoration of outcomes (power, cooling, compute, data and checkpoint, network, control plane) within tolerance is planned and tested | S5 | 11 | 56 | MCF-POW-024; MCF-THM-024; MCF-CMP-023; MCF-STO-016; MCF-STO-018; MCF-STO-020; MCF-NET-015; MCF-RES-013; MCF-RES-014; MCF-RES-016; MCF-RES-018 |
| CG-11 | Evidence sufficiency | Evidence for decisive claims meets the AIDCF-008 floors (meta-gate across all controls) | S4 | 0 | 0 | Meta-gate: evaluated across all controls |
| CG-12 | Critical UNKNOWN | No unresolved US4 or US5 UNKNOWN without disposition (meta-gate across all controls) | S3 | 0 | 0 | Meta-gate: evaluated across all controls |
| CG-13 | Responsibility and authority | Every critical function and dependency has an accountable owner and decision authority | S3 | 7 | 28 | MCF-GOV-002; MCF-GOV-005; MCF-GOV-006; MCF-GOV-007; MCF-CAP-002; MCF-DEP-018; MCF-OPS-002 |
| CG-14 | Change control | Material changes are controlled, impact-assessed and validated | S4 | 7 | 35 | MCF-CAP-023; MCF-CMP-015; MCF-NET-022; MCF-OPS-006; MCF-OPS-017; MCF-OPS-018; MCF-OPS-020 |
| CG-15 | Integrated digital authority over infrastructure | Identity, privilege, remote access and control-plane reach over facility and AI infrastructure are bounded, monitored and recoverable | S4 | 7 | 42 | MCF-SUP-021; MCF-SUP-022; MCF-SEC-003; MCF-SEC-006; MCF-SEC-010; MCF-SEC-012; MCF-SEC-021 |

## Amendment Log

| Amendment ID | Date | Status | Summary |
|---|---|---|---|
| AIDCF-007A-AMD-001 | (as stated in v1.0 issue) | Approved by baseline owner; independent ratification pending | Adopted the 15/90/360 cardinality and MCF identifier baseline and deprecated narrative statements of 14/84/336. |
| AIDCF-007A-AMD-002 | 2026-10-10 | PROPOSED - Draft for controlled review | Per-control content rewrite, duplicate-title fixes, control-specific CRITICAL/SUPPORTING gate mapping, per-control assurance levels, evidence requirement profiles, assessment template restored. |
