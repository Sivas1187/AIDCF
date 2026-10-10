# AIDCF-019 Crosswalk: Uptime Institute Tier Standard

Part of [AIDCF-019 Standards Crosswalks](../README.md). Mapping file: [uptime-mapping.csv](uptime-mapping.csv).

| **Field** | **Value** |
|---|---|
| Artifact ID | AIDCF-019 (crosswalk: Uptime Institute Tier Standard) |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| External edition basis | Uptime Institute Tier Standard: Topology; Tier Standard: Operational Sustainability; associated Tier Certification programmes |
| Mapping level | Concept level (Tier I–IV objectives; Operational Sustainability elements) |
| Review status | Indicative; requires review by a person competent in the Tier Standards |

| **Version** | **Date** | **Summary** |
|---|---|---|
| 1.0 | 2026-10-10 | First issue replacing placeholder. |

## 1. Scope of the Tier Standards

**Tier Standard: Topology** defines four performance objectives for site infrastructure supporting IT equipment: Tier I basic capacity; Tier II redundant capacity components; Tier III concurrently maintainable (every capacity component and distribution path can be removed for planned maintenance without affecting the critical environment); Tier IV fault tolerant (a single failure of a component or path does not affect the critical environment, with compartmentalisation of complementary systems and continuous cooling). The topology concept treats on-site engine-generators as the primary power source and the utility as an economic alternative.

**Tier Standard: Operational Sustainability** addresses the behaviours and risks beyond topology that affect long-term performance: management and operations (staffing and organisation, maintenance, training, planning, coordination and management, operating conditions), building characteristics, and site location.

Uptime Institute offers certification of design documents, of the constructed facility, and of operational sustainability; it also offers management and operations assessments. Tier ratings apply to site infrastructure (power and cooling), not to IT equipment.

## 2. Where it overlaps with AIDCF

- **Power and thermal topology.** POW-01 to POW-04 and THM-01, THM-04 are PARTIAL; POW-02 (engine-generator as primary source) is a HIGH-confidence PARTIAL.
- **Common mode and containment.** Concurrent maintainability and fault tolerance with compartmentalisation overlap DEP-02 and RES-02 for power and cooling paths.
- **Operations.** Operational Sustainability overlaps OPS-01 (staffing and organisation) and OPS-03 (maintenance) strongly, and OPS-02, OPS-04 to OPS-06 partially.
- **Site location.** PHY-01.

## 3. Where AIDCF goes beyond the Tier Standards

- **Scope.** Tiers exclude IT equipment. AIDCF CMP, STO and NET domains, and the dependency of AI capability on facility behaviour, are outside Tier scope.
- **Outcome under AI load.** A Tier objective concerns the critical environment during maintenance and failure events. AIDCF additionally requires evidence on transient electrical behaviour of AI loads (POW-05), liquid-cooling continuity (THM-03), thermal recovery (THM-06) and the consequence for training and inference Service Outcomes.
- **Security, supply chain and evidence.** SEC, SUP and EVA domains have no Tier counterpart; physical security (PHY-04) is outside Tier scope.
- **Continuing assurance.** A Tier Certification of Constructed Facility demonstrates topology at a point in time. AIDCF requires current IMPLEMENTATION and OPERATION evidence and treats post-certification change (CG-14) as a reassessment trigger.

## 4. Using Tier outputs as AIDCF evidence

| Output | AIDCF evidence class | Useful for | Limits |
|---|---|---|---|
| Tier Certification of Design Documents | E5 | POW, THM DESIGN claims | Design only; superseded by construction changes |
| Tier Certification of Constructed Facility, including witnessed demonstrations | E4/E5 | CAP-06 Commissioning Acceptance; RES-05 Component Tests; DEP-02, RES-02 for power and cooling | Point in time; IT load at demonstration may differ from AI production load; does not cover liquid-cooling secondary loops unless explicitly in scope |
| Operational Sustainability certification or management and operations assessment | E5 | OPS-01, OPS-03, OPS-02; EVA-06 context | Period-bound; site-infrastructure operations only |

A Tier certificate shall not be converted into an AIDCF Gate Result (XW-REQ-003). It is relevant evidence for CG-05 and CG-06 at DESIGN or IMPLEMENTATION claim level only.

## 5. Gaps and cautions

- Tier concepts are described here in paraphrase; requirements such as on-site fuel and water storage durations and specific demonstration criteria shall be read from the current Tier Standard.
- Applicability of Tier concepts to CDU-based liquid cooling and to rear-door or immersion systems should be confirmed with the Tier Standard owner.

## 6. Coverage summary

| Relationship | Families | Share of 90 |
|---|---:|---:|
| EQUIVALENT | 0 | 0% |
| PARTIAL | 20 | 22% |
| SUPPORTS_EVIDENCE | 2 | 2% |
| CONTEXT | 8 | 9% |
| NO_MATCH | 60 | 67% |
| **Total** | **90** | **100%** |

Coverage by AIDCF domain (count of families with EQUIVALENT or PARTIAL / SUPPORTS_EVIDENCE / CONTEXT / NO_MATCH, out of 6):

| Domain | EQ or PARTIAL | SUPPORTS_EVIDENCE | CONTEXT | NO_MATCH |
|---|---:|---:|---:|---:|
| GOV | 0 | 0 | 0 | 6 |
| CAP | 1 | 1 | 3 | 1 |
| DEP | 2 | 0 | 0 | 4 |
| PHY | 2 | 0 | 0 | 4 |
| POW | 5 | 0 | 0 | 1 |
| THM | 3 | 0 | 2 | 1 |
| ENV | 0 | 0 | 0 | 6 |
| CMP | 0 | 0 | 0 | 6 |
| STO | 0 | 0 | 0 | 6 |
| NET | 0 | 0 | 0 | 6 |
| OPS | 6 | 0 | 0 | 0 |
| RES | 1 | 1 | 1 | 3 |
| SUP | 0 | 0 | 1 | 5 |
| SEC | 0 | 0 | 0 | 6 |
| EVA | 0 | 0 | 1 | 5 |

### AIDCF differentiation

60 AIDCF families have no corresponding provision in this framework (NO_MATCH). These are where AIDCF assurance goes beyond it; evidence for them must come from AIDCF-specific assessment or another crosswalked framework.

| Domain | Families with NO_MATCH |
|---|---|
| GOV | GOV-01 Governance architecture; GOV-02 Accountability and responsibility; GOV-03 Policy and standards management; GOV-04 Risk and assurance governance; GOV-05 Stakeholder and regulatory interface; GOV-06 Ethics, impartiality and competence |
| CAP | CAP-01 Capability inventory |
| DEP | DEP-01 Dependency discovery; DEP-04 Concentration and substitutability; DEP-05 Boundary and interface control; DEP-06 Dependency monitoring and review |
| PHY | PHY-02 Building and structural integrity; PHY-04 Access and surveillance; PHY-05 Asset movement and custody; PHY-06 Fire, life safety and emergency interfaces |
| POW | POW-05 Power quality and transient response |
| THM | THM-05 Fluid quality and leak management |
| ENV | ENV-01 Environmental operating conditions; ENV-02 Energy performance; ENV-03 Water performance; ENV-04 Carbon and resource reporting; ENV-05 Hazardous materials and waste; ENV-06 Climate adaptation and resource continuity |
| CMP | CMP-01 Compute architecture and configuration; CMP-02 Cluster and scale-up domains; CMP-03 Capacity, scheduling and utilisation; CMP-04 Firmware, driver and compatibility; CMP-05 Compute health and observability; CMP-06 Compute lifecycle and recovery |
| STO | STO-01 Storage architecture and tiering; STO-02 Performance and capacity; STO-03 Integrity and consistency; STO-04 Protection and replication; STO-05 Checkpoint and recovery services; STO-06 Storage monitoring and lifecycle |
| NET | NET-01 Scale-up and scale-out fabrics; NET-02 Performance and congestion control; NET-03 Storage and service networks; NET-04 Management and out-of-band networks; NET-05 Physical connectivity and optics; NET-06 Network control and observability |
| RES | RES-03 Continuity planning; RES-04 Recovery planning; RES-06 Crisis and adaptive response |
| SUP | SUP-01 Supplier due diligence; SUP-02 Contract and service obligations; SUP-03 Hardware and component provenance; SUP-04 Software, firmware and update supply; SUP-06 Remote support and third-party access |
| SEC | SEC-01 Identity and privileged access; SEC-02 Control-plane protection; SEC-03 Network security and segmentation; SEC-04 Configuration, vulnerability and patching; SEC-05 Detection and response; SEC-06 AI-enabled and automated action |
| EVA | EVA-01 Evidence architecture; EVA-02 Evidence provenance and quality; EVA-03 Assessment planning and execution; EVA-04 Findings, UNKNOWN and limitations; EVA-05 Critical gates and decisions |

## 7. Review status

Indicative. Requires review by a person competent in the current Tier Standards before reliance (AIDCF-019 §7, XW-REQ-006).
