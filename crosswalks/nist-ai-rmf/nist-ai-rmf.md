# AIDCF-019 Crosswalk: NIST AI Risk Management Framework 1.0

Part of [AIDCF-019 Standards Crosswalks](../README.md). Mapping file: [nist-ai-rmf-mapping.csv](nist-ai-rmf-mapping.csv).

| **Field** | **Value** |
|---|---|
| Artifact ID | AIDCF-019 (crosswalk: NIST AI RMF) |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| External edition basis | NIST AI 100-1, Artificial Intelligence Risk Management Framework (AI RMF 1.0), January 2023 |
| Mapping level | Functions and categories (for example GOVERN 2); subcategories (for example GOVERN 1.6) named in notes only where certain |
| Review status | Indicative; requires review by a competent AI RMF practitioner |

| **Version** | **Date** | **Summary** |
|---|---|---|
| 1.0 | 2026-10-10 | First issue replacing placeholder. |

## 1. Scope of the NIST AI RMF

The AI RMF is a voluntary framework for managing risks of AI systems to individuals, organisations and society, and for incorporating trustworthiness characteristics (valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, fair) into AI design, development, use and evaluation. Its core has four functions: GOVERN (cross-cutting culture, policies, accountability, third-party risk; categories GOVERN 1–6), MAP (context and risk identification; MAP 1–5), MEASURE (analysis, assessment and tracking; MEASURE 1–4) and MANAGE (prioritisation, treatment, response and recovery; MANAGE 1–4). It is not a certification scheme and produces no certificate. Profiles (including the Generative AI Profile, NIST AI 600-1) tailor it to use cases; profiles are not mapped here.

## 2. Where it overlaps with AIDCF

- **GOVERN** overlaps GOV-01 to GOV-06: policies and risk tolerance (GOVERN 1), accountability structures (GOVERN 2, a HIGH-confidence PARTIAL to GOV-02), team composition and training (GOVERN 2–3), stakeholder engagement (GOVERN 5) and third-party risk (GOVERN 6, overlapping DEP-03 and SUP-01).
- **AI system inventory** (GOVERN 1.6) overlaps CAP-01 as the demand-side register that AIDCF Capability Instances serve.
- **MEASURE 1.1** asks that risks that cannot be measured be documented. This is the nearest external analogue to AIDCF UNKNOWN preservation (EVA-04).
- **MANAGE 1.1** (determination whether the AI system achieves its purpose and whether deployment should proceed) parallels the Assurance Decision (EVA-05).
- **Human oversight and deactivation** (GOVERN 3, MAP 3, MANAGE 2.4) overlap SEC-06.
- **Environmental impact** (MEASURE 2.12) is CONTEXT for ENV-02 to ENV-04.

## 3. Where AIDCF goes beyond the AI RMF

The AI RMF addresses socio-technical risk of the AI system. It does not address the physical and digital infrastructure on which the system runs. AIDCF adds facility domains (PHY, POW, THM, ENV-01, ENV-05, ENV-06), AI infrastructure domains (CMP, STO, NET), operations (OPS), infrastructure resilience and recovery (RES), and evidence floors, UNKNOWN severity and Critical Gates that turn risk documentation into a bounded decision. The AI RMF's MEASURE 2.7 (security and resilience) evaluates the AI system; AIDCF RES and CG-05, CG-06, CG-09 and CG-10 evaluate whether the infrastructure keeps that system within outcome tolerance.

## 4. Using AI RMF outputs as AIDCF evidence

| Output | AIDCF evidence class | Useful for | Limits |
|---|---|---|---|
| AI RMF profile or self-assessment | E1 Documentary / E7 Derived | GOV families, CAP-02, CAP-03 | Self-declared; no third-party attestation implied |
| AI system inventory (GOVERN 1.6) | E1/E2 | CAP-01 linkage to consuming AI systems | Not an infrastructure inventory |
| Impact characterisation (MAP 5) | E1/E7 | CAP-03 criticality and stakeholder consequence | Does not set infrastructure tolerances |
| TEVV records (MEASURE 2) | E4 Validation and test | EVA-02, EVA-03; context for RES-05 | Evaluate AI system behaviour, not infrastructure failure modes |
| Documented unmeasured risks (MEASURE 1.1) | E1 | Seed for UNKNOWN Records (EVA-04) | Must be typed and given US severity under AIDCF |

## 5. Gaps and cautions

- Because the AI RMF is voluntary and certificate-free, its outputs are usually E1 or E7 evidence prepared by the organisation itself; independence must be established separately.
- Subcategory numbering has been stable since 1.0, but reviewers should confirm any subcategory cited in notes against the current NIST publication and Playbook.

## 6. Coverage summary

| Relationship | Families | Share of 90 |
|---|---:|---:|
| EQUIVALENT | 0 | 0% |
| PARTIAL | 15 | 17% |
| SUPPORTS_EVIDENCE | 0 | 0% |
| CONTEXT | 24 | 27% |
| NO_MATCH | 51 | 57% |
| **Total** | **90** | **100%** |

Coverage by AIDCF domain (count of families with EQUIVALENT or PARTIAL / SUPPORTS_EVIDENCE / CONTEXT / NO_MATCH, out of 6):

| Domain | EQ or PARTIAL | SUPPORTS_EVIDENCE | CONTEXT | NO_MATCH |
|---|---:|---:|---:|---:|
| GOV | 6 | 0 | 0 | 0 |
| CAP | 1 | 0 | 3 | 2 |
| DEP | 2 | 0 | 3 | 1 |
| PHY | 0 | 0 | 0 | 6 |
| POW | 0 | 0 | 0 | 6 |
| THM | 0 | 0 | 0 | 6 |
| ENV | 0 | 0 | 3 | 3 |
| CMP | 0 | 0 | 1 | 5 |
| STO | 0 | 0 | 0 | 6 |
| NET | 0 | 0 | 0 | 6 |
| OPS | 0 | 0 | 3 | 3 |
| RES | 0 | 0 | 5 | 1 |
| SUP | 1 | 0 | 3 | 2 |
| SEC | 1 | 0 | 1 | 4 |
| EVA | 4 | 0 | 2 | 0 |

### AIDCF differentiation

51 AIDCF families have no corresponding provision in this framework (NO_MATCH). These are where AIDCF assurance goes beyond it; evidence for them must come from AIDCF-specific assessment or another crosswalked framework.

| Domain | Families with NO_MATCH |
|---|---|
| CAP | CAP-04 Demand and growth modelling; CAP-05 Operating envelope |
| DEP | DEP-02 Shared and common-mode dependencies |
| PHY | PHY-01 Site and location resilience; PHY-02 Building and structural integrity; PHY-03 Physical zoning and segregation; PHY-04 Access and surveillance; PHY-05 Asset movement and custody; PHY-06 Fire, life safety and emergency interfaces |
| POW | POW-01 Utility and grid interface; POW-02 Generation and fuel; POW-03 UPS and energy storage; POW-04 Distribution and protection; POW-05 Power quality and transient response; POW-06 Electrical monitoring, maintenance and recovery |
| THM | THM-01 Thermal architecture and capacity; THM-02 Air cooling systems; THM-03 Liquid cooling systems; THM-04 Heat rejection and water systems; THM-05 Fluid quality and leak management; THM-06 Thermal control, maintenance and recovery |
| ENV | ENV-01 Environmental operating conditions; ENV-05 Hazardous materials and waste; ENV-06 Climate adaptation and resource continuity |
| CMP | CMP-01 Compute architecture and configuration; CMP-02 Cluster and scale-up domains; CMP-03 Capacity, scheduling and utilisation; CMP-04 Firmware, driver and compatibility; CMP-06 Compute lifecycle and recovery |
| STO | STO-01 Storage architecture and tiering; STO-02 Performance and capacity; STO-03 Integrity and consistency; STO-04 Protection and replication; STO-05 Checkpoint and recovery services; STO-06 Storage monitoring and lifecycle |
| NET | NET-01 Scale-up and scale-out fabrics; NET-02 Performance and congestion control; NET-03 Storage and service networks; NET-04 Management and out-of-band networks; NET-05 Physical connectivity and optics; NET-06 Network control and observability |
| OPS | OPS-02 Procedure and work control; OPS-03 Maintenance and reliability; OPS-05 Change and configuration management |
| RES | RES-02 Fault-domain and containment design |
| SUP | SUP-05 Spares, logistics and obsolescence; SUP-06 Remote support and third-party access |
| SEC | SEC-01 Identity and privileged access; SEC-02 Control-plane protection; SEC-03 Network security and segmentation; SEC-04 Configuration, vulnerability and patching |

## 7. Review status

Indicative. Requires review by a competent AI RMF practitioner before reliance (AIDCF-019 §7, XW-REQ-006).
