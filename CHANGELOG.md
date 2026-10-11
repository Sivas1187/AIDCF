# Changelog

All notable changes to this repository are recorded here. Versions refer to the public framework release.

## [Unreleased]

### Added
- **AIDCF-VAL-001 Incident Back-Testing Protocol v1.0** (`research/back-testing/`): retrospective coding of publicly reported incidents against AIDCF controls, AIDCF-004 failure scenarios and critical gates; two coders with hindsight-bias controls; coding sheet, data dictionary, empty incident register and a checker (`backtest_check.py`, including Cohen's kappa). No incidents coded yet.
- **AIDCF-VAL-002 Expert Panel Content Validation v1.0** (`validation/expert-panel/`): modified Delphi protocol, deterministic 48-control stratified sample plus all 15 gates, Round 1 questionnaire, item booklet and response template, participant information and consent template, and an analysis script (I-CVI, modified kappa, S-CVI/Ave) with a synthetic self-test. No panel convened.
- **Mini-pilot pack AIDCF-PIL-001 to 005** (`pilots/`): protocol for an authorised AL3 research assessment of one AI cluster, a 58-control Starter Profile and its generator (gates CG-01, CG-02, CG-03, CG-05, CG-06, CG-07 and CG-10 plus the meta-gates), authorisation and evidence-request templates, result record, metrics and lessons-learned templates. No pilot has taken place.
- CI checks for the three new generators and checkers.
- AIDCF-VAL-001 sampling frame: 221 real incident candidates screened from 115 searches of provider post-incident reports and regulator reports (140 eligible), with a run log of the flow, shortfalls (liquid cooling, storage) and open items. Not yet second-checked, selected or coded.
- `backtest_check.py` accepts a blank incident date only when flagged DATE_UNRESOLVED, and a blank category only on EXCLUDED rows.

## [3.1 Validation Candidate] - 2026-10-10

Release identifier AIDCF-REL-2026.10.1. This release acts on the architecture review of 2026-10-10: it adds the missing artifacts, makes the controls testable, gives every term one source of truth and makes the machine-executable layer validate real data. Every new or revised document is a draft for controlled review. No independent review, inter-rater trial or authorised pilot has taken place.

### Added
- **AIDCF-002 Core Conceptual Model v1.0**: normative keywords, the canonical 16-step assurance chain mapped to ISO/IEC/IEEE 15026-2 and GSN, core concepts, a glossary (including "material" and where UNKNOWN is permitted), the artifact-ID scheme, the controlled vocabularies, and the legacy eight-domain to fifteen-domain mapping.
- **AIDCF-007A registry v1.1 (PROPOSED, amendment AMD-002)**: a distinct, testable requirement, objective and claim type for each of the 360 controls; one evidence requirement profile per control (AIDCF-008 §31); per-control gate mapping with CRITICAL and SUPPORTING roles (106 and 483 mappings, at least three CRITICAL controls per gate); 508 named parameters with illustrative defaults; gate names and the assessment template moved in from the superseded AIDCF-007 v1.0. Fifteen per-domain control catalogues in `standards/aidcf-007a/registry/controls/`.
- **Critical-gate criteria**: `registries/gates/critical-gate-criteria.csv` (101 criteria), with evidence floors and FAIL and UNKNOWN decision ceilings in `critical-gates.csv`.
- **Controlled vocabularies**: 25 CSV files in `registries/vocabularies/`, each with legacy aliases, including the control-result score mapping (CONFORMING 100, PARTIAL 50, NONCONFORMING 0) and the UNKNOWN severity tests US1 to US5.
- **AIDCF-016 Machine-Executable Data Model Standard v1.0** and the generated MDM 1.3 schema set in `schemas/`: closed JSON Schemas (2020-12) for every AIDCF-014 object class, a JSON-LD 1.1 context with `@vocab`, an OWL 2 ontology (`schemas/owl/aidcf-core-1.3.ttl`, namespace `https://w3id.org/aidcf/ontology#`, w3id registration pending) and SHACL shapes that run against instance data. All are generated from one model, `schemas/tools/aidcf_model.py`.
- **AIDCF-015 package v1.3**: synthetic reference implementation on MDM 1.3. `run_all.py` runs 13 validation layers including the valid, invalid and business fixture directories, recomputes every gate from the roll-up rule, fails on RDF parse errors and no longer invalidates its own manifest.
- **AIDCF-017 Capability Assurance Maturity Model v1.0**, diagnostic only, with no effect on results, gates or decisions.
- **AIDCF-018 Domain Guides v1.0**, one for each of the 15 domains.
- **AIDCF-019 Crosswalks**: indicative family-level mappings of all 90 families to ISO/IEC 42001, NIST AI RMF, ISO/IEC 27001, EN 50600, TIA-942, Uptime Institute Tier, ISA/IEC 62443 and the Singapore baseline, with a coverage summary. No standard text is reproduced.
- Registry catalogue for AIDCF-014 §17 in `registries/catalogue/`.
- GitHub Actions CI (`.github/workflows/ci.yml`): registry cardinality, Turtle and JSON-LD parsing, generated-schema freshness and the v1.3 `run_all.py`.
- Issue form, pull-request template and private security-reporting route (GitHub private vulnerability reporting).

### Changed
- **Artifact IDs**: one public scheme (AIDCF-NNN). The Manifesto is AIDCF-001 and the Core Conceptual Model AIDCF-002. The validation report, previously mislabelled AIDCF-016, is now AIDCF-VR-001. The whitepaper is AIDCF-WP-001. Requirement IDs are consecutive.
- **Revised to v1.1** and renamed accordingly: AIDCF-001 Manifesto, AIDCF-003, 004, 005, 006, the 007A amendment, 008, 010, 011, 012, 013, 014 and AIDCF-VR-001. AIDCF-009 is now Part A Core Practitioner Handbook v1.1 and Part B Enhanced Practitioner Companion v1.2. Old filenames remain in git history.
- **Foundations re-baselined** to the 15 domains and MCF identifiers. Every document uses the one canonical chain from AIDCF-002 and refers to AIDCF-007A, not AIDCF-007.
- **One definition of a control**: a control is a distinct requirement with one claim type (DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS or RESILIENCE). AIDCF-007A, AIDCF-009 and AIDCF-010 are aligned to this.
- **Gate mapping is per control**, not per domain. CG-11 and CG-12 are meta-gates. PARTIAL never yields PASS.
- **AIDCF-010**: explicit EQI weights (P 0.20, F 0.20, C 0.15, R 0.20, T 0.15, I 0.10, used for sorting only); score bands recalibrated (B5 at least 90, B4 75 to 89.99, B3 50 to 74.99, B2 25 to 49.99, B1 below 25); a band is reported only with at least 80% coverage and no US4 or US5 UNKNOWN; coverage below 50% gives INCONCLUSIVE and below 80% caps the decision at LIMITED.
- **Decision vocabulary**: INCONCLUSIVE replaces UNKNOWN_OR_INCONCLUSIVE, ADVERSE and "Withheld"; SUSPENDED, WITHDRAWN and SUPERSEDED are lifecycle states, not decision outcomes. Ceilings combine by the AIDCF-010 order, in which NOT_ASSURED is the most restrictive; AIDCF-016 and the rule engine, which had ranked NOT_ASSURED and INCONCLUSIVE equal, now follow it. An applicable NOT_ASSESSED gate applies the gate's UNKNOWN ceiling (AIDCF-002 aligned to AIDCF-010).
- **Evidence quality dimensions (meaning change)**: AIDCF-008 v1.1 defines F as fitness and relevance and T as timeliness and currentness. In v1.0, F was freshness and T was traceability. Freshness is now part of T, and traceability is a mandatory linkage requirement (§17A) rather than a scored dimension. Quality ratings made under v1.0 must be re-rated before comparison.
- **AIDCF-004**: generic boilerplate (shared operator definitions, technique text, scenario paths and the 256-row generated failure catalogue) replaced with specific content.
- **AIDCF-011**: management-system loop (plan, do, check, act; internal audit; management review) added so AIDCF fits alongside ISO/IEC 42001 and 27001 programmes.
- **Whitepaper v3.1** (from v3.0, archived in `whitepaper/archive/v3.0/`): drafting-assistant text removed, v2.0 leftovers and the §7 header fixed, a single argument and conclusion, the worked case aligned to the v1.3 dataset, Figure 2 added and references completed.
- README, LICENSE, CITATION.cff, SECURITY.md and folder READMEs updated to the new structure. The ontology and all schemas are Apache 2.0.

### Fixed
- AIDCF-009 Practitioner Handbook v1.0 restored to active status (now Part A).
- `registries/controls/controls.csv` placeholder titles and requirements replaced.
- Duplicated control titles (MCF-CMP-008 and MCF-NET-004; MCF-STO-019 and MCF-RES-014) made distinct.
- The synthetic dataset no longer passes gates on PARTIAL controls. Its computed decision is NOT_ASSURED (CG-07 FAIL ceiling), with coverage 11 of 360 scored (3.0556%).
- Registry rows carry the AIDCF-014 lifecycle status CANDIDATE (proposed, awaiting review) instead of the non-canonical PROPOSED.
- Relationship aliases EVALUATES, TESTED_BY and RECOVERED_BY added to the vocabulary, matching AIDCF-014 §9.1.
- The generators for the registry, control catalogues and registry catalogue are now in `registries/tools/`.

### Known limitations
- Registry v1.1, the gate criteria and the per-control gate mapping are PROPOSED and await multidisciplinary approval under GOVERNANCE.md. Registry v1.0 remains the approved baseline.
- The approval record for AIDCF-007A AMD-001 (the 15/90/360 cardinality decision) has no stated approver or date.
- Crosswalks are indicative and need review by people holding each standard.
- The synthetic package assesses 12 of 360 controls; it describes no real facility.
- The release manifest is not signed.
- The w3id namespace is not yet registered, so ontology IRIs do not resolve.
- The AIDCF-015 v1.0 specification describes the earlier package design and is kept as a historical record.

## [3.0 Validation Candidate] - 2026-10-10

### Added
- Technical Whitepaper v3.0 (Validation Candidate for Independent Review)
- Manifesto v1.0 and foundation standards AIDCF-003 to AIDCF-006
- AIDCF-007A Control Universe Constitutional Amendment and Canonical Master Control Registry (15 domains, 90 families, 360 controls)
- Standards AIDCF-008 to AIDCF-014
- AIDCF-015 v1.2 canonical-baseline synthetic reference implementation, with registries and schemas
- AIDCF-016 Full Stack Validation Report v1.0
- Licensing: CC BY 4.0 for documentation, standards, registries and data; Apache 2.0 for schemas and software
- Governance, contribution, security, conduct and citation files
- PDF editions of all documents
- Markdown editions of all documents (source of truth) and Markdown renderings of the Excel registries

### Removed
- Word (.docx) source files, superseded by the Markdown editions (available in git history)

### Archived
- AIDCF-007 Control Catalogue v1.0 (superseded by AIDCF-007A)
- AIDCF-015 v1.1 Executable Reference Implementation (superseded by v1.2)
