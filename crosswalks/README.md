# AIDCF-019 Standards Crosswalks

*AI Data Centre Facilities Assurance Framework*

Artifact ID: AIDCF-019
Requirement prefix: XW
Artifact type: Informative crosswalk set (normative interpretation rules in §5)
Status: Draft for controlled review
Author: Siva Sethumadhavan

## Document control

| **Field** | **Value** |
|---|---|
| Title | AIDCF Standards Crosswalks |
| Artifact ID | AIDCF-019 (requirement prefix XW) |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Depends on | AIDCF-007A Control Universe and Canonical Master Control Registry (90 families); AIDCF-008 Evidence Model; AIDCF-010 Scoring and Decision Framework |
| Applies to | Assessors, assurance programme owners and tooling that reuse outputs of external standards, certifications or regulatory regimes as inputs to AIDCF assessments |
| Review status | Indicative. Every mapping requires review by a competent holder of a licensed copy of the external standard before reliance (see §7). |

### Revision history

| **Version** | **Date** | **Summary** |
|---|---|---|
| 1.0 | 2026-10-10 | First issue: family-level crosswalks to eight external frameworks (replacing placeholder folders), relationship and confidence vocabularies, interpretation rules and coverage summary. |

## 1. Purpose

AIDCF assesses whether a bounded AI infrastructure Capability Instance can achieve declared Service Outcomes within tolerance across declared operating states. Most operators already hold management-system certifications, facility design ratings, OT security assessments and regulatory obligations. AIDCF-019 states, for each of the 90 AIDCF control families, how far each external framework addresses the same objective, how its outputs can be used as evidence, and where AIDCF assurance has no external counterpart.

The crosswalks serve three uses:

1. **Evidence planning.** Identify which existing certificates, reports, test records and registers can be requested as Evidence Objects, and which AIDCF families need new assessment work.
2. **Duplication control.** Avoid re-assessing what a competent external assessment already covers, while keeping the scope, period and state limits of that assessment visible.
3. **Differentiation.** Show explicitly which AIDCF families have no external equivalent, so that a holder of an external certificate does not assume coverage that does not exist.

## 2. Method

### 2.1 Unit of mapping

Mapping is performed at **family level** (AIDCF-007A families GOV-01 to EVA-06), not at control level. Each CSV contains exactly one row per family, 90 rows per framework, so that coverage gaps are explicit. A family row may cite several external provisions separated by semicolons. The external reference is given at the most specific level the author is confident of: clause or control number where certain, otherwise clause group, part, function or concept. Where an external framework is cited at part level only, the confidence is LOW or MEDIUM and the row says what must be confirmed.

### 2.2 Relationship types

Each row carries exactly one relationship, chosen as the strongest that applies, in this order of precedence:

| Relationship | Definition | Typical evidential use |
|---|---|---|
| EQUIVALENT | The external provision addresses substantially the same objective, scope and depth as the AIDCF family, including the operating states and tolerances the family requires. Any residual difference is immaterial to the family's assessment criteria. | Outputs may satisfy most family evidence requirements after AIDCF-008 scope, currency and sufficiency evaluation. |
| PARTIAL | The external provision addresses the same objective for part of the family's scope, or at lower depth (for example design intent without operating-state coverage, or IT scope without OT and facility scope). | Outputs are relevant evidence for the overlapping part; the remainder needs AIDCF-specific evidence. |
| SUPPORTS_EVIDENCE | The external framework does not set an equivalent requirement, but it produces outputs (certificates, demonstrations, registers, test records) that can be used as Evidence Objects for the family. | Outputs are E1, E4 or E5 evidence subject to AIDCF-008 evaluation. |
| CONTEXT | The external framework addresses an adjacent topic that frames or informs the family (terminology, risk context, upstream obligations) but neither sets an equivalent requirement nor produces directly usable evidence. | Background for scoping and assessment planning only. |
| NO_MATCH | No corresponding provision was identified at the level reviewed. | None; the family requires AIDCF-specific assessment. |

No row in this issue is assessed as EQUIVALENT. This is deliberate: an AIDCF family combines a capability-level objective, explicit Service Outcome tolerances, operating-state coverage (AIDCF-003 states NORMAL to UNKNOWN) and claim-type evidence floors (AIDCF-008). None of the crosswalked frameworks sets all four for the same scope. EQUIVALENT is retained in the vocabulary for future crosswalks and for reviewed revisions where a licensed holder demonstrates it.

### 2.3 Confidence

| Confidence | Meaning |
|---|---|
| HIGH | The external reference and its subject are well established and the relationship judgement is unlikely to change on review of the licensed text. |
| MEDIUM | The reference is correct at the level cited, but the depth or scope of overlap should be confirmed against the licensed text or the edition in use. |
| LOW | The reference is cited at a coarse level (part, function, concept or secondary source), or the relationship depends on content the author could not confirm. Rows marked LOW shall not be relied upon without review. |

For NO_MATCH rows the confidence (default MEDIUM) expresses how confident the author is that no provision applies at the level reviewed. Notes are given on NO_MATCH rows only where a pointer to another crosswalk is useful.

### 2.4 Sources and editions

| Folder | Framework and edition basis | Level of mapping |
|---|---|---|
| [iso42001/](iso42001/iso42001.md) | ISO/IEC 42001:2023 Artificial intelligence management system | Clauses 4–10; Annex A control objective groups A.2–A.10 |
| [nist-ai-rmf/](nist-ai-rmf/nist-ai-rmf.md) | NIST AI 100-1, AI Risk Management Framework 1.0 (January 2023) | Functions GOVERN, MAP, MEASURE, MANAGE and their categories; subcategories named in notes where certain |
| [iso27001/](iso27001/iso27001.md) | ISO/IEC 27001:2022 (with Amd 1:2024) | Clauses 4–10; Annex A controls 5.1–8.34 |
| [en50600/](en50600/en50600.md) | EN 50600 series (ISO/IEC 22237 series counterpart) | Parts 1, 2-1 to 2-5, 3-1 and 4-x KPI parts |
| [tia942/](tia942/tia942.md) | ANSI/TIA-942 (edition to be confirmed by the assessor) | Rated levels and the four infrastructure subsystems |
| [uptime/](uptime/uptime.md) | Uptime Institute Tier Standard: Topology and Tier Standard: Operational Sustainability | Concept level |
| [isa62443/](isa62443/isa62443.md) | ISA/IEC 62443 parts 2-1, 2-4, 3-2, 3-3, 4-1, 4-2 | Parts; foundational requirements FR1–FR7; security levels |
| [singapore/](singapore/singapore.md) | Singapore instruments verified as of 2026-10-10 | Instrument level; section level only where verified |

## 3. Index and coverage

| Framework | Folder | EQUIVALENT | PARTIAL | SUPPORTS_EVIDENCE | CONTEXT | NO_MATCH |
|---|---|---:|---:|---:|---:|---:|
| ISO/IEC 42001:2023 | [iso42001/](iso42001/iso42001.md) | 0 | 15 | 1 | 20 | 54 |
| NIST AI RMF 1.0 | [nist-ai-rmf/](nist-ai-rmf/nist-ai-rmf.md) | 0 | 15 | 0 | 24 | 51 |
| ISO/IEC 27001:2022 | [iso27001/](iso27001/iso27001.md) | 0 | 51 | 1 | 29 | 9 |
| EN 50600 / ISO/IEC 22237 | [en50600/](en50600/en50600.md) | 0 | 32 | 0 | 17 | 41 |
| ANSI/TIA-942 | [tia942/](tia942/tia942.md) | 0 | 16 | 0 | 12 | 62 |
| Uptime Institute Tier Standard | [uptime/](uptime/uptime.md) | 0 | 20 | 2 | 8 | 60 |
| ISA/IEC 62443 | [isa62443/](isa62443/isa62443.md) | 0 | 19 | 0 | 15 | 56 |
| Singapore baseline | [singapore/](singapore/singapore.md) | 0 | 29 | 1 | 12 | 48 |

Each folder contains a narrative (`<folder>.md`: scope, overlap, where AIDCF goes beyond the framework, use of outputs as evidence, gaps, coverage tables) and a mapping file (`<folder>-mapping.csv`, columns `aidcfFamilyId, aidcfFamilyName, externalRef, externalTitle, relationship, confidence, notes`).

[coverage-summary.csv](coverage-summary.csv) aggregates the eight crosswalks: one row per family, the relationship assigned in each framework, counts per relationship type, and an `aidcfDifferentiation` value:

| aidcfDifferentiation | Rule |
|---|---|
| NO_EXTERNAL_COVERAGE | No framework is EQUIVALENT, PARTIAL or SUPPORTS_EVIDENCE |
| MINIMAL_EXTERNAL_COVERAGE | Not NO_EXTERNAL_COVERAGE, and at most one framework is EQUIVALENT or PARTIAL |
| LIMITED_EXTERNAL_COVERAGE | Two or three frameworks are EQUIVALENT or PARTIAL |
| BROAD_EXTERNAL_COVERAGE | Four or more frameworks are EQUIVALENT or PARTIAL |

### 3.1 AIDCF differentiation across all crosswalks

9 families have no EQUIVALENT, PARTIAL or SUPPORTS_EVIDENCE relationship in any crosswalked framework: POW-05 Power quality and transient response; ENV-05 Hazardous materials and waste; ENV-06 Climate adaptation and resource continuity; CMP-02 Cluster and scale-up domains; CMP-05 Compute health and observability; STO-01 Storage architecture and tiering; STO-03 Integrity and consistency; NET-02 Performance and congestion control; SUP-05 Spares, logistics and obsolescence.

A further 25 families are addressed as EQUIVALENT or PARTIAL by at most one framework (some also have SUPPORTS_EVIDENCE rows): CAP-02 Service outcome definition; CAP-04 Demand and growth modelling; CAP-06 Capability lifecycle and change; DEP-01 Dependency discovery; DEP-04 Concentration and substitutability; PHY-05 Asset movement and custody; PHY-06 Fire, life safety and emergency interfaces; THM-03 Liquid cooling systems; THM-05 Fluid quality and leak management; ENV-03 Water performance; CMP-01 Compute architecture and configuration; CMP-03 Capacity, scheduling and utilisation; CMP-04 Firmware, driver and compatibility; CMP-06 Compute lifecycle and recovery; STO-02 Performance and capacity; STO-04 Protection and replication; STO-05 Checkpoint and recovery services; STO-06 Storage monitoring and lifecycle; NET-01 Scale-up and scale-out fabrics; NET-03 Storage and service networks; NET-06 Network control and observability; RES-06 Crisis and adaptive response; SUP-03 Hardware and component provenance; EVA-02 Evidence provenance and quality; EVA-05 Critical gates and decisions.

These families are concentrated in AI compute, storage and network infrastructure, capability and outcome definition, dependency and concentration analysis, and evidence and decision management. They are where an AIDCF assessment adds most to an existing certification portfolio. The pattern is structural: management-system standards (ISO/IEC 42001, ISO/IEC 27001) govern processes at organisation level; facility standards (EN 50600, TIA-942, Tier) govern site infrastructure design and operation; ISA/IEC 62443 governs control-system security. None addresses accelerator clusters, scale-up domains, collective-communication performance, checkpoint durability or the evidential chain from Capability Instance to Assurance Decision.

## 4. How to use a crosswalk in an assessment

1. Start from the AIDCF Capability Instance, Service Outcomes and boundary (CG-01, CG-02). Determine which in-scope families are relevant.
2. For each relevant family, read the rows in the crosswalks for the frameworks the operator holds. Request the cited external outputs as candidate Evidence Objects.
3. Evaluate each external output under AIDCF-008 like any other evidence: issuer and competence, scope and exclusions, period and currency, operating states covered, method, and permitted reliance (AIDCF-008 §12 conditional metadata for external evidence).
4. Record what the external output does not cover as an assessment requirement for AIDCF-specific evidence, or as an UNKNOWN Record where that evidence is not obtained.
5. Do not change a control result, gate result or decision because an external certificate exists; change it only on the basis of evaluated evidence.

## 5. Interpretation rules (normative)

**XW-REQ-001** A crosswalk row shall not be treated as transferring conformity in either direction. Conformity with an external standard does not establish a CONFORMING control result in AIDCF, and an AIDCF result does not establish conformity with the external standard.

**XW-REQ-002** External certificates, ratings, classifications, attestations and regulatory approvals shall be treated as bounded evidence under AIDCF-008 (doctrine of non-inheritance; EVM-REQ-012). They shall be evaluated for issuer, competence or accreditation, scope, validity period, exclusions, operating states covered and permitted reliance before use.

**XW-REQ-003** An external certificate or rating shall not by itself establish control applicability, current operating effectiveness, absence of common-mode failure, capability-level resilience, evidence sufficiency, a PASS Gate Result, or an Assurance Decision.

**XW-REQ-004** Reuse of one external output across several AIDCF families or controls shall be justified per assertion (EVM-REQ-011); an output relevant to one family is not thereby relevant to the others cited in the same crosswalk row.

**XW-REQ-005** A relationship of EQUIVALENT or PARTIAL indicates where evidence is likely to be found; it shall not reduce the evidence floor, claim type or required assurance level of any AIDCF control.

**XW-REQ-006** Where the edition of an external standard in use differs from the edition basis in §2.4, or where a row is marked LOW confidence, the assessor shall confirm the mapping against the licensed text before relying on it, and record the confirmation or the residual uncertainty.

**XW-REQ-007** A NO_MATCH or CONTEXT relationship shall not be read as a defect in the external framework; it records a difference of scope.

## 6. Copyright and use of standards text

No text of any external standard is reproduced in AIDCF-019. Clause, control, part and category identifiers and short titles are cited only for identification; descriptions are paraphrased summaries written for this crosswalk. Users shall consult licensed copies of ISO, IEC, CENELEC, TIA, ISA and Uptime Institute publications and the official publications of Singapore authorities for the authoritative text. A citation or crosswalk grants no rights to third-party standards content (see CONTRIBUTING.md).

## 7. Review status and limitations

- All crosswalks in this issue are **indicative**. They were prepared from general knowledge of the external frameworks and, for Singapore, from official and secondary public sources consulted on 2026-10-10. They have not yet been reviewed by competent holders of each standard.
- Before reliance in a formal assessment, each crosswalk shall be reviewed by a person competent in the external framework and holding a licensed copy of the edition in use. The review outcome shall be recorded in that crosswalk's revision history.
- Clause and control numbers are given only where the author is confident of them. Where a framework has been revised (for example TIA-942 editions, EN 50600 part revisions and ISO/IEC 22237 counterparts), the assessor shall confirm numbering against the edition in use.
- Mapping at family level can hide control-level differences. A PARTIAL family may contain one control that is fully addressed externally and three that are not.
- External frameworks not crosswalked in this issue but cited in the AIDCF README (BICSI 002, NIST SP 800-53, ASHRAE TC 9.9 guidance, W3C PROV-O, assurance-case methods) are candidates for later issues.
