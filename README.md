# AIDCF

## AI Data Centre Facilities Assurance Framework

**Capability-centred, evidence-gated and graph-native assurance for AI infrastructure**

> **Repository status:** Validation Candidate for Independent Review  
> **Public framework version:** Whitepaper v3.1 (release AIDCF-REL-2026.10.1)  
> **Canonical control baseline:** 15 domains · 90 control families · 360 controls (registry v1.0 approved baseline; v1.1 testable-control revision PROPOSED)  
> **Current implementation:** Synthetic, non-production reference implementation (AIDCF-015 v1.3, data model AIDCF-016 MDM 1.3)  
> **External validation:** Not yet completed

---

## Overview

AIDCF is a research framework and controlled assurance methodology for evaluating the facilities and infrastructure that support AI compute.

It connects defined AI service outcomes to the physical, engineered, technical, operational and external systems on which those outcomes depend. It then traces credible failure paths, safeguards, evidence, assessment results, critical gates and accountable decisions.

AIDCF treats an AI data centre as a **capability-supporting system**, not merely a collection of equipment.

The framework is organised around the following assurance chain:

```text
Capability Instance
→ Service Outcome
→ Required Function
→ Architecture
→ Dependency / Fault Domain
→ Threat / Hazard / Failure Scenario
→ Safeguard
→ Control
→ Evidence Requirement
→ Evidence Object
→ Assessment Result
→ Finding / UNKNOWN
→ Critical Gate
→ Score / Recommendation
→ Assurance Decision
→ Report / Reassessment Trigger
```

AIDCF is intended to help infrastructure owners, operators, architects, engineering teams, risk and assurance practitioners, technology providers and researchers form a more defensible view of whether a bounded AI infrastructure capability can achieve its required outcomes under declared operating conditions.

---


## Quick Start

Choose the path that matches your purpose.

### Executive or decision-maker

1. Read the [technical whitepaper](whitepaper/current/AIDCF_Technical_Whitepaper_v3.1_Validation_Candidate.md).
2. Review [The Problem AIDCF Solves](#the-problem-aidcf-solves).
3. Review [Example Use Cases](#example-use-cases).
4. Review the framework's status and limitations before relying on any conclusion.

### Infrastructure, engineering or operations practitioner

1. Read the Manifesto (AIDCF-001) and the Core Conceptual Model (AIDCF-002).
2. Review AIDCF-003 through AIDCF-006 for ontology, failure reasoning, graph integration and assurance principles.
3. Review the AIDCF-007A canonical registry and the AIDCF-018 domain guide for each domain in scope.
4. Use AIDCF-008 through AIDCF-012 for evidence, assessment, scoring, programme governance and reporting.
5. Review AIDCF-013 for the system-of-systems reference architecture and AIDCF-017 for capability maturity.
6. Use the AIDCF-019 crosswalks to relate AIDCF controls to standards you already apply.

### Researcher or independent reviewer

1. Read the whitepaper's research problem, contribution, limitations and threats to validity.
2. Review the derivation records and reviewer dispositions in `validation/`.
3. Challenge the domain model, control symmetry, gate model, scoring rules and evidence doctrine.
4. Submit issues using the review taxonomy in [CONTRIBUTING.md](CONTRIBUTING.md).

### Developer or semantic-model implementer

1. Review AIDCF-014 and AIDCF-016.
2. Inspect the CSV registries and vocabularies in `registries/`, and the JSON Schemas, JSON-LD context, OWL ontology and SHACL shapes in `schemas/`.
3. From `implementation/aidcf-015-v1.3/`, run:

```bash
python3 -m pip install -r requirements.txt
python3 -B tools/run_all.py
```

4. Inspect captured validation, graph-query and score re-performance outputs.
5. Do not interpret technical conformance as assurance over a real facility.

### Minimum reading order

```text
Whitepaper
→ Manifesto
→ Core Conceptual Model
→ AIDCF-003 to AIDCF-006
→ AIDCF-007A Registry and AIDCF-018 Domain Guides
→ AIDCF-008 to AIDCF-012
→ AIDCF-013, AIDCF-014, AIDCF-016
→ AIDCF-017 Maturity Model and AIDCF-019 Crosswalks
→ Validation and pilot records
```

---

## The Problem AIDCF Solves

Traditional reviews commonly examine facilities, technology platforms, cybersecurity, operations or AI governance as separate subjects.

AI-service failure can cross all of those boundaries.

A distributed-training or inference outcome may depend simultaneously on electrical continuity, thermal capacity, accelerated compute, checkpoint storage, low-latency fabrics, orchestration, privileged control planes, operational authority, external providers and recovery resources.

AIDCF provides a single reconstructable assurance argument across that system:

```text
What must the AI capability achieve?
→ Which functions and systems enable it?
→ What can fail together?
→ How can failure propagate?
→ Which safeguards matter?
→ What evidence supports each assertion?
→ Which prerequisites are non-compensating?
→ What bounded decision can an accountable authority issue?
```

AIDCF's purpose is not to replace existing engineering, security, management-system or AI-risk standards. It is to connect their relevant outputs to a capability-centred infrastructure assurance decision.

---

## Architecture Diagram

```mermaid
flowchart TB
    BO[Business and mission outcomes]
    CI[Capability Instance]
    SO[Service Outcomes and tolerances]
    RF[Required Functions]

    subgraph AI[AI technology service chain]
        ORCH[Orchestration and scheduling]
        CMP[Accelerated compute]
        NET[Scale-up and scale-out fabrics]
        STO[Training data, model and checkpoint storage]
    end

    subgraph FAC[Facility and physical infrastructure]
        PHY[Site, building and physical zones]
        POW[Electrical power and energy continuity]
        THM[Thermal, cooling and fluid systems]
        ENV[Environmental and resource conditions]
    end

    subgraph ECO[Operations and external ecosystem]
        OPS[Operations and service management]
        RES[Resilience, recovery and restoration]
        SUP[Utilities, carriers, OEMs and suppliers]
        SEC[Digital, OT and control-plane security]
    end

    subgraph ASSUR[Assurance rail]
        CTRL[Canonical controls]
        EVID[Evidence Objects]
        ASMT[Assessment results]
        GATE[Critical gates]
        SCORE[Scores and confidence]
        DEC[Accountable Assurance Decision]
        REP[Reports and reassessment]
    end

    BO --> CI --> SO --> RF
    RF --> ORCH
    ORCH --> CMP
    CMP <--> NET
    CMP <--> STO
    CMP --> POW
    CMP --> THM
    POW --> PHY
    THM --> ENV
    AI --> OPS
    FAC --> OPS
    SUP --> FAC
    SUP --> AI
    SEC --> AI
    SEC --> FAC
    OPS --> RES

    CI -.scope.-> CTRL
    AI -.assessed by.-> CTRL
    FAC -.assessed by.-> CTRL
    ECO -.assessed by.-> CTRL
    CTRL --> EVID --> ASMT --> GATE --> SCORE --> DEC --> REP
    REP -.change or expiry.-> CI
```

### How to read the diagram

- The vertical path begins with a defined business or mission outcome and a bounded Capability Instance.
- The AI technology chain depends on physical facilities, utilities, providers, people and control authority.
- Controls attach to specific capability, architecture, dependency, failure and safeguard assertions.
- Evidence supports or challenges those assertions.
- Critical gates constrain scores and recommendations.
- Only accountable authority may issue, suspend, withdraw or supersede an Assurance Decision.

---

## Example Use Cases

AIDCF can be considered for the following controlled uses. Each use requires an explicitly defined decision question, scope, evidence profile and competent review.

### AI data-centre readiness

Assess whether a planned or upgraded facility has a coherent capability model, declared operating envelope, mapped dependencies, applicable controls, evidence ownership and commissioning pathway before production use.

### High-density training-cluster assurance

Connect training-job outcomes to accelerator capacity, collective communication, checkpoint storage, electrical and thermal continuity, orchestration, fault domains and recovery dependencies.

### Inference-platform resilience review

Evaluate whether the infrastructure supporting an inference service can maintain required capacity, latency, integrity and recovery outcomes under defined demand, degradation and failure conditions.

### Liquid-cooling assurance

Review coolant distribution, heat-load assumptions, CDUs, loops, sensors, controls, fluid quality, leak management, common controllers, operating states, fail-safe behaviour and recovery interactions with compute workloads.

### Sovereign AI infrastructure

Examine jurisdictional, provider, remote-support, telemetry, administration, supply-chain and recovery dependencies against declared sovereignty and control-boundary outcomes.

### Colocation AI deployment review

Define provider and tenant boundaries, shared services, power and cooling commitments, access restrictions, evidence availability, dependency concentration and responsibility for recovery.

### AI infrastructure resilience and recovery

Analyse fault domains, common-mode dependencies, containment, graceful degradation, alternate capacity, checkpoint integrity, recovery sequencing and outcome restoration.

### OT and control-plane security review

Assess privileged access, remote support, segmentation, monitoring, change control and safe automation across BMS, EPMS, cooling, power and AI management planes.

### Supplier and concentration-risk review

Analyse exposure to utilities, carriers, OEMs, firmware, specialist labour, spares, logistics, cloud services and single-source dependencies.

### AI infrastructure due diligence

Support a bounded review of infrastructure claims, capacity assumptions, material dependencies, evidence quality and unresolved uncertainty for investment, acquisition, outsourcing or major procurement decisions.

### Continuing assurance and change impact

Use event-driven reassessment to identify which evidence, controls, gates, scores, decisions and reports may be affected by architecture, load, provider, incident or configuration changes.

### Research and method evaluation

Test the AIDCF ontology, control structure, evidence rules, critical gates, scoring constraints, graph queries, semantic validation and inter-rater reproducibility.

These examples do not imply that AIDCF is already validated for every use case or jurisdiction.

---

## Audience Matrix

| Audience | Primary interest | Relevant AIDCF outputs | Important boundary |
|---|---|---|---|
| Board and executive leadership | Bounded decision, exposure, residual uncertainty and investment priorities | Executive report, gate summary, Assurance Decision and action roadmap | AIDCF is not a guarantee or statutory opinion |
| CIO, CTO and infrastructure leadership | Capability outcomes, architecture, capacity and dependency risks | Capability profile, architecture views, domain results and change-impact records | Requires competent domain review |
| CISO and OT-security leadership | Privileged authority, segmentation, remote access and control-plane risk | SEC domain results, CG-07, CG-15, evidence and findings | Does not replace specialised cyber testing |
| Data-centre owner or operator | Facility readiness, operations, maintenance, resilience and recovery | POW, THM, PHY, ENV, OPS and RES profiles | Does not replace engineering or safety approval |
| AI/HPC platform owner | Compute, storage, fabric, scheduling and checkpoint outcomes | CMP, STO, NET, CAP and DEP results | Infrastructure assurance is not model assurance |
| Engineering teams | Power, thermal, fluid, physical and system-of-systems integrity | Reference architecture, scenarios, safeguards and evidence requirements | Hazardous testing requires explicit authorisation |
| Internal audit and assurance | Scope, evidence, workpapers, independence and conclusion lineage | Assessment package, gate register, decision record and reports | Does not create certification authority |
| Enterprise risk management | Criticality, concentration, failure consequences and treatment | Risk-linked findings, scenarios, decisions and reassessment triggers | Risk acceptance must remain with accountable authority |
| Procurement and supplier management | Provider dependence, support, lifecycle, contracts and substitution | SUP and DEP mappings, evidence requests and concentration analysis | Contract interpretation remains source-owned |
| Customer assurance teams | Transparent scope, limitations and infrastructure evidence | Bounded customer statement and disclosure package | Must not imply universal safety or resilience |
| Regulators and public-sector users | Traceability, accountability, evidence and material limitations | Regulatory report, control mapping and decision lineage | AIDCF does not determine legal compliance |
| Investors and transaction teams | Capacity credibility, hidden dependencies and evidence quality | Due-diligence profile and bounded findings | Not a valuation or investment recommendation |
| Researchers and standards practitioners | Reproducibility, construct validity and methodological gaps | Whitepaper, derivation records, registry and validation corpus | Current framework remains a validation candidate |
| Developers and ontology engineers | Schemas, identifiers, graphs, validation and interoperability | AIDCF-014, AIDCF-015 and AIDCF-016 | Machine conformance does not establish factual truth |

---

## Relationship to Existing Standards and Frameworks

AIDCF is intended to complement existing standards and methods. It does not claim equivalence, certification, conformity or clause-level coverage unless a separate, reviewed crosswalk explicitly establishes it.

Indicative family-level crosswalks (all 90 control families) for eight framework families are in [`crosswalks/`](crosswalks/README.md) (AIDCF-019). They map AIDCF families to clause or topic references only, reproduce no standard text, and have not yet been reviewed by holders of those standards.

| Standard or framework family | Primary role | Relationship with AIDCF |
|---|---|---|
| ISO/IEC 42001 | AI management-system governance | Can inform organisational AI-governance context, roles, objectives, risk processes and supplier governance around the capability |
| NIST AI RMF | Voluntary AI risk-management framework | Can provide AI-system context through Govern, Map, Measure and Manage; AIDCF focuses more deeply on the supporting infrastructure assurance chain |
| ISO/IEC 27001 | Information-security management system | Can provide organisational security governance and control context; AIDCF applies infrastructure-specific digital and OT assurance logic |
| ISO/IEC 22237 and EN 50600 | Data-centre facilities and infrastructure | Can provide facility and infrastructure requirements or evidence inputs across physical, power, thermal, environmental, operational and resilience domains |
| ANSI/TIA-942 | Data-centre telecommunications and physical infrastructure | Can provide relevant architecture and implementation evidence for physical, power, cooling and network infrastructure |
| Uptime Institute Tier Standard | Site-infrastructure topology and performance expectations | Tier evidence can support relevant design assertions, but a Tier classification is not converted automatically into an AIDCF Assurance Decision |
| BICSI 002 | Data-centre design and implementation guidance | Can provide design and implementation evidence for relevant technical domains where applicable |
| ISA/IEC 62443 | Industrial automation and control-system security | Can inform OT, control-plane, lifecycle, supplier and operational-security evidence |
| NIST SP 800-53 / NIST RMF | Security and privacy controls and risk-management processes | Can provide control and governance inputs where infrastructure systems fall within the selected scope |
| ASHRAE data-centre guidance | Thermal, environmental and energy engineering | Can support thermal, environmental and operating-envelope criteria; source engineering guidance remains authoritative |
| Reliability and safety methods | FMEA/FMECA, fault trees, event trees, bow ties and related analysis | AIDCF can consume structured outputs to model causes, failure modes, propagation, consequences and safeguards |
| W3C PROV-O | Provenance representation | Can support machine-readable evidence lineage and transformation records |
| Assurance-case methods (ISO/IEC/IEEE 15026-2, GSN) | Structured claims, arguments and evidence | AIDCF-002 maps each step of the canonical chain to 15026-2 assurance-case elements and GSN; independent review of that mapping is pending |
| Singapore baselines (IMDA Advisory Guidelines 2025, Digital Infrastructure Bill, Cybersecurity Act and CCoP-CII, CSA AI-security guidelines, Green Mark for Data Centres 2024, SS 564, SS 697, SS 715, SS 726, MAS TRM and BCM) | National data-centre, energy, resilience and security baselines | Indicative mapping in `crosswalks/singapore/` |
| AI Trust Graph | Trust, authority and exposure reasoning | Interoperates through reference, mapping, shared identity, boundary handoff, scenario composition, evidence reuse and decision federation |

### Important interpretation rule

Existing certifications, classifications or compliance results are treated as bounded evidence. They do not automatically establish:

- control applicability;
- current operating effectiveness;
- absence of common-mode failure;
- capability-level resilience;
- evidence sufficiency;
- a favourable Critical Gate result;
- an AIDCF Assurance Decision.

NIST describes the AI RMF as voluntary and intended to improve organisations' ability to incorporate trustworthiness considerations into AI design, development, use and evaluation. AIDCF therefore treats it as a complementary AI-risk context rather than an infrastructure certification mechanism.

---

## Research Questions

AIDCF is designed to be challenged through explicit research questions.

Three validation instruments are ready to run. None has been executed yet.

| Instrument | Method | Informs | Location |
|---|---|---|---|
| AIDCF-VAL-001 Incident Back-Testing Protocol | Retrospective coding of publicly reported incidents against AIDCF controls, failure scenarios and gates, with two coders and hindsight-bias controls | RQ2, RQ4, RQ5, RQ8 | [`research/back-testing/`](research/back-testing/README.md) |
| AIDCF-VAL-002 Expert Panel Content Validation | Modified Delphi rating of a 48-control stratified sample and all 15 gates; content validity indices and modified kappa | RQ3, RQ8 | [`validation/expert-panel/`](validation/expert-panel/README.md) |
| AIDCF-PIL-001 Mini-Pilot Protocol | Authorised research assessment of one bounded AI cluster at AL3 using the 58-control Starter Profile | RQ1 to RQ4, RQ6 to RQ8, RQ10, RQ11, RQ13, RQ15 | [`pilots/`](pilots/README.md) |

### RQ1: Subject definition

Can independent assessors consistently define the same bounded Capability Instance, Service Outcomes and operating envelope for a real AI infrastructure service?

### RQ2: Cross-domain completeness

Does the fifteen-domain model capture material facility, technology, operational, supplier, security and assurance conditions without excessive overlap or omission?

### RQ3: Control-universe validity

Does the 15/90/360 catalogue provide adequate coverage without padding less-complex domains or compressing more-complex domains?

### RQ4: Dependency discovery

Does capability-centred graph modelling identify hidden, shared, external and recovery-only dependencies that conventional domain-by-domain reviews miss?

### RQ5: Failure-path usefulness

Does explicit modelling of causes, failure modes, propagation, safeguards and residual paths improve the quality of resilience conclusions?

### RQ6: Evidence quality

Do provenance, fitness, coverage, reliability, timeliness, integrity, traceability and sufficiency rules improve the defensibility and reproducibility of assessments?

### RQ7: UNKNOWN discipline

Does preserving material uncertainty as a first-class result reduce false confidence compared with approaches that convert missing evidence into a score or maturity weakness?

### RQ8: Critical-gate effectiveness

Do non-compensating Critical Gates prevent high aggregate scores from obscuring decisive infrastructure, evidence, recovery or governance weaknesses?

### RQ9: Scoring validity

Are AIDCF control, family, domain and capability indicators stable, interpretable and appropriately sensitive to evidence quality, coverage and UNKNOWN?

### RQ10: Inter-rater reliability

Do independently trained assessors reach acceptably consistent applicability, control-result, gate and decision recommendations?

### RQ11: Machine traceability

Can a material report statement be reconstructed reliably through decision, gate, finding, assessment, evidence, control, safeguard, failure and architecture records?

### RQ12: Change impact

Can event-driven graph analysis identify the records and decisions affected by architecture, provider, load, configuration, incident or evidence changes?

### RQ13: Decision usefulness

Do named decision users consider AIDCF outputs more relevant, transparent and actionable than existing siloed review outputs?

### RQ14: Economic relevance

Can authorised pilots identify measurable relationships between assurance findings and accelerator availability, workload interruption, recovery effort, evidence friction or delayed programme value?

### RQ15: Scalability

Can the method remain practicable across enterprise, colocation, sovereign, hyperscale and edge AI deployments without losing claim discipline?

### RQ16: AITG interoperability

Can AIDCF infrastructure findings and AI Trust Graph authority or exposure findings be federated without collapsing their native semantics or decisions?

Research outcomes, including negative or null results, should be recorded transparently and used to revise the framework.

---

## Why AIDCF

AI workloads create tightly coupled dependencies across:

- electrical power and energy continuity;
- cooling, thermal and fluid systems;
- accelerated compute infrastructure;
- high-performance storage and checkpoint services;
- high-bandwidth network and interconnect fabrics;
- orchestration, scheduling and control planes;
- building and technology operations;
- resilience, recovery and crisis response;
- OEMs, utilities, carriers and external providers;
- physical, digital and OT security;
- evidence, assessment and accountable decision-making.

A technically available facility does not necessarily mean that a distributed-training, fine-tuning, inference or sovereign-AI capability can achieve its required service outcomes.

AIDCF addresses this integration problem by making dependencies explicit, preserving uncertainty and linking conclusions to evidence and decision authority.

---

## What makes AIDCF different

### Capability-first

The assessed subject is a specific **Capability Instance**, bounded by owner, architecture, location, operating states, service outcomes, demand, criticality and obligations.

### Cross-domain

AIDCF connects facility engineering, configured AI technology, operations, security, providers, evidence and assurance rather than reviewing each area in isolation.

### Evidence-gated

Assertions are not treated as facts unless supported by evidence that is relevant, traceable, current, sufficiently complete and appropriate for the decision.

### UNKNOWN is first-class

Missing, inaccessible, stale, conflicting or insufficient evidence remains visible as `UNKNOWN`. It is not automatically converted to pass, fail, zero, not applicable or accepted risk.

### Critical gates are non-compensating

A favourable average score cannot neutralise a controlling failure or material uncertainty in a critical prerequisite.

### Graph-native

AIDCF supports forward and reverse traceability across capability, architecture, dependency, failure, controls, evidence, assessments, gates, decisions and reports.

### Human accountability is retained

Automation may validate structures, calculate indicators, identify affected records and generate recommendations. It must not independently approve material facts, critical gates or assurance decisions.

---

## Framework status and claim boundary

AIDCF is currently a **Validation Candidate for Independent Review**.

The repository distinguishes five maturity states:

| Status | Meaning |
|---|---|
| Approved AIDCF baseline | AIDCF-internal identity and cardinality decision formally adopted within the framework |
| Controlled-review draft | Substantive methodology awaiting multidisciplinary review |
| Synthetic demonstration | Non-production data and execution used to test the method |
| Proposed research extension | Concept requiring governance, calibration and validation before operational use |
| Externally validated | Independently executed or empirically validated; **not yet achieved** |

### AIDCF is

- a research framework;
- an assurance methodology;
- a control and evidence architecture;
- a capability-centred reference model;
- a machine-readable traceability model;
- a basis for controlled pilots and independent review.

### AIDCF is not

- an accredited standard;
- a certification or accreditation scheme;
- a legal or regulatory determination;
- a licensed engineering opinion;
- a safety approval;
- a substitute for applicable law, codes or professional judgement;
- a vendor endorsement;
- an authorisation for intrusive, destructive or hazardous testing;
- an assurance conclusion about any real facility merely because the framework is used.

The phrases **“AIDCF Certified”** and **“AIDCF Accredited”** are not authorised by this repository.

---

## Canonical control baseline

The authoritative AIDCF control universe is established by AIDCF-007A:

```text
15 control domains
90 control families
360 normative controls
6 families per domain
4 controls per family
```

Any earlier reference to `14 domains / 84 families / 336 controls` is superseded and must not be used for coverage, scoring, reporting or machine execution.

### Fifteen domains

| Code | Domain |
|---|---|
| `GOV` | Governance, Accountability and Assurance Direction |
| `CAP` | AI Capability, Service Outcome and Demand Management |
| `DEP` | Dependency, Concentration and External Reliance Management |
| `PHY` | Physical Site, Building and Security Infrastructure |
| `POW` | Electrical Power Infrastructure and Energy Continuity |
| `THM` | Cooling, Thermal and Fluid Infrastructure |
| `ENV` | Environmental and Resource Performance |
| `CMP` | AI Compute Infrastructure |
| `STO` | AI Storage and Data Infrastructure |
| `NET` | AI Network and Interconnect Architecture |
| `OPS` | Building Operations and Service Management |
| `RES` | Resilience, Continuity and Recovery |
| `SUP` | Supply Chain, OEM and Ecosystem Assurance |
| `SEC` | Digital, OT and Control-Plane Security |
| `EVA` | Evidence, Assessment and Assurance Management |

Stable canonical control identifiers use this pattern:

```text
MCF-<DOMAIN>-<NUMBER>
```

Examples:

```text
MCF-CAP-001
MCF-POW-012
MCF-THM-024
MCF-EVA-024
```

Stable identity does not imply that control wording can never evolve. Meaning-changing revisions require explicit versioning, impact analysis, migration and supersession.

---

## Repository map

```text
AIDCF/
├── README.md, LICENSE, LICENSES/, CITATION.cff, CHANGELOG.md,
│   GOVERNANCE.md, CONTRIBUTING.md, SECURITY.md, CODE_OF_CONDUCT.md
├── .github/         CI workflow, issue templates, pull-request template
├── docs/            images, diagrams, presentations, publications
├── whitepaper/
│   ├── current/     Technical Whitepaper v3.1 (Markdown, PDF, figures)
│   └── archive/     earlier whitepaper versions
├── foundations/
│   ├── manifesto/             AIDCF-001 Manifesto v1.1
│   ├── conceptual-model/      AIDCF-002 Core Conceptual Model v1.0
│   ├── ontology-taxonomy/     AIDCF-003 v1.1
│   ├── threat-model/          AIDCF-004 v1.1
│   ├── aitg-integration/      AIDCF-005 v1.1
│   └── assurance-principles/  AIDCF-006 v1.1
├── standards/
│   ├── aidcf-007a/            amendment/ (v1.1) and registry/ (v1.0 approved, v1.1 PROPOSED,
│   │                          per-domain control catalogues in registry/controls/)
│   ├── aidcf-008-evidence-model/            v1.1
│   ├── aidcf-009-assessment-methodology/    Part A Core Handbook v1.1, Part B Companion v1.2
│   ├── aidcf-010-scoring-framework/         v1.1
│   ├── aidcf-011-assurance-program/         v1.1
│   ├── aidcf-012-reporting-standard/        v1.1
│   ├── aidcf-013-reference-architecture/    v1.1
│   ├── aidcf-014-traceability-standard/     v1.1
│   ├── aidcf-016-machine-executable-model/  v1.0 (MDM 1.3)
│   ├── aidcf-017-maturity-model/            v1.0
│   └── aidcf-018-domain-guides/             15 domain guides v1.0
├── registries/      domains, families, controls, evidence profiles, gate mappings,
│                    gate criteria, parameters, states, 25 controlled vocabularies (CSV)
├── schemas/         json-schema, jsonld, owl, shacl (MDM 1.3) and the generator in tools/
├── implementation/
│   ├── aidcf-015-v1.3/        current synthetic reference implementation
│   └── aidcf-015-v1.2/        previous package, retained unchanged for comparison
├── assurance/       assessment, scoring, decision and report models; statements
├── validation/      AIDCF-VR-001 Full Stack Validation Report v1.1,
│                    expert-panel/ (AIDCF-VAL-002 content-validation kit), independent review,
│                    dispositions, derivations, gate approvals
├── pilots/          mini-pilot pack AIDCF-PIL-001 to 005: protocol, Starter Profile,
│                    authorisation, evidence request, result and lessons-learned templates
├── crosswalks/      AIDCF-019: ISO/IEC 42001, NIST AI RMF, ISO/IEC 27001, EN 50600,
│                    TIA-942, Uptime, ISA/IEC 62443, Singapore baselines
├── research/        back-testing/ (AIDCF-VAL-001 incident back-testing kit), review papers,
│                    derivations, literature, hypotheses, questions
├── examples/        worked assessment, evidence, report, decision, capability
└── archive/         superseded, duplicates, working drafts, historical releases
```

Folders holding only a README (examples, and parts of research, validation and assurance) are reserved for records that do not yet exist. They are empty on purpose: no pilot, expert panel, back-test or independent review has taken place yet.

Markdown (`.md`) is the source of truth for every document, with an archival PDF alongside. Excel workbooks remain authoritative for the control registry and have Markdown renderings. Structured registries and machine-readable files stay in their native formats.

---

## Artifact catalogue

| Artifact | Purpose | Current status |
|---|---|---|
| [AIDCF-001 Manifesto v1.1](foundations/manifesto/AIDCF-001_Manifesto_v1.1.md) | Identity, mission, scope and assurance philosophy | Draft for controlled review |
| [AIDCF-002 Core Conceptual Model v1.0](foundations/conceptual-model/AIDCF-002_Core_Conceptual_Model_v1.0.md) | Normative keywords, canonical 16-step chain, core concepts and definitions | Draft for controlled review |
| [AIDCF-003 v1.1](foundations/ontology-taxonomy/AIDCF-003_Infrastructure_Ontology_and_Taxonomy_v1.1.md) | Infrastructure ontology and taxonomy | Draft for controlled review |
| [AIDCF-004 v1.1](foundations/threat-model/AIDCF-004_Threat_Hazard_and_Failure_Model_v1.1.md) | Threat, hazard, failure and recovery model | Draft for controlled review |
| [AIDCF-005 v1.1](foundations/aitg-integration/AIDCF-005_AIDCF_AI_Trust_Graph_Integration_Standard_v1.1.md) | Integration boundary with AI Trust Graph | Draft for controlled review |
| [AIDCF-006 v1.1](foundations/assurance-principles/AIDCF-006_Assurance_Principles_Standard_v1.1.md) | Constitutional assurance principles | Draft for controlled review |
| [AIDCF-007A Amendment v1.1](standards/aidcf-007a/amendment/AIDCF-007A_Control_Universe_Constitutional_Amendment_v1.1.md) | Authoritative 15/90/360 cardinality decision and amendment log | Cardinality approved; amendment AMD-002 proposed |
| [AIDCF-007A Registry v1.0](standards/aidcf-007a/registry/AIDCF-007A_Canonical_Master_Control_Registry_15-90-360_v1.0.md) | Canonical domains, families and controls (approved baseline) | Approved AIDCF baseline |
| [AIDCF-007A Registry v1.1](standards/aidcf-007a/registry/AIDCF-007A_Canonical_Master_Control_Registry_15-90-360_v1.1.md) | Testable controls, evidence profiles, per-control gate mapping, parameters | PROPOSED (AMD-002), not yet approved |
| [AIDCF-008 v1.1](standards/aidcf-008-evidence-model/AIDCF-008_Evidence_Model_v1.1.md) | Evidence model | Draft for controlled review |
| [AIDCF-009 Part A v1.1](standards/aidcf-009-assessment-methodology/AIDCF-009_Part_A_Core_Practitioner_Handbook_v1.1.md) | Core practitioner handbook: roles, stage gates, playbooks, workpapers | Draft for controlled review |
| [AIDCF-009 Part B v1.2](standards/aidcf-009-assessment-methodology/AIDCF-009_Part_B_Enhanced_Practitioner_Companion_v1.2.md) | Enhanced practitioner companion | Draft for controlled review |
| [AIDCF-010 v1.1](standards/aidcf-010-scoring-framework/AIDCF-010_Scoring_and_Decision_Framework_v1.1.md) | Scoring and decision framework | Draft for controlled review |
| [AIDCF-011 v1.1](standards/aidcf-011-assurance-program/AIDCF-011_Assurance_Program_Framework_v1.1.md) | Non-certification assurance programme framework | Draft for controlled review |
| [AIDCF-012 v1.1](standards/aidcf-012-reporting-standard/AIDCF-012_Reporting_and_Assurance_Statement_Standard_v1.1.md) | Reporting and assurance-statement standard | Draft for controlled review |
| [AIDCF-013 v1.1](standards/aidcf-013-reference-architecture/AIDCF-013_AI_Data_Centre_Assurance_Reference_Architecture_v1.1.md) | AI data-centre assurance reference architecture | Draft for controlled review |
| [AIDCF-014 v1.1](standards/aidcf-014-traceability-standard/AIDCF-014_End-to-End_Traceability_and_Machine-Executable_Data_Standard_v1.1.md) | End-to-end traceability and machine-executable data standard | Draft for controlled review |
| [AIDCF-015 spec v1.0](implementation/AIDCF-015_Reference_Implementation_Synthetic_Dataset_and_Conformance_Pilot_v1.0.md) | Reference implementation specification (historical; package v1.3 is current) | Draft for controlled review |
| [AIDCF-015 package v1.3](implementation/aidcf-015-v1.3/README.md) | Synthetic reference implementation on MDM 1.3 | Synthetic demonstration |
| [AIDCF-016 v1.0](standards/aidcf-016-machine-executable-model/AIDCF-016_Machine-Executable_Data_Model_Standard_v1.0.md) | Machine-executable data-model standard (MDM 1.3) | Draft for controlled review |
| [AIDCF-017 v1.0](standards/aidcf-017-maturity-model/AIDCF-017_Capability_Assurance_Maturity_Model_v1.0.md) | Capability assurance maturity model | Draft for controlled review |
| [AIDCF-018 v1.0](standards/aidcf-018-domain-guides/) | Fifteen domain guides, one per control domain | Draft for controlled review |
| [AIDCF-019](crosswalks/README.md) | Crosswalks to eight external frameworks (indicative) | Indicative; needs review by holders of each standard |
| [AIDCF-VR-001 v1.1](validation/validation-report/AIDCF-VR-001_Full_Stack_Validation_Report_v1.1.md) | Full stack validation report | Draft for controlled review |
| [AIDCF-WP-001 Whitepaper v3.1](whitepaper/current/AIDCF_Technical_Whitepaper_v3.1_Validation_Candidate.md) | Consolidated research argument and validation candidate | Independent review pending |

---

## Critical-gate model

AIDCF uses fifteen critical gates, identified as `CG-01` through `CG-15`.

Gates are mapped control by control, not by whole domain. Each mapping has the role CRITICAL or SUPPORTING (`registries/controls/gate-mappings.csv`, 106 CRITICAL and 483 SUPPORTING mappings), and every gate has at least three CRITICAL controls. CG-11 (evidence integrity) and CG-12 (assessment independence and quality) are meta-gates that apply to every assessment. Pass criteria are in `registries/gates/critical-gate-criteria.csv` (101 criteria) and the roll-up rule is in AIDCF-010:

- any CRITICAL control NONCONFORMING, or a gate criterion failed, gives FAIL;
- any CRITICAL control PARTIAL gives FAIL, because PARTIAL never yields PASS;
- any CRITICAL control UNKNOWN or not assessed, with nothing failed, gives UNKNOWN;
- PASS requires every CRITICAL control CONFORMING and every criterion met.

These names, criteria and mappings are proposed in registry v1.1 and remain candidates for formal multidisciplinary approval until a signed canonical gate registry is published.

The controlled gate-state vocabulary is:

```text
PASS
FAIL
UNKNOWN
APPROVED_NA
NOT_ASSESSED
```

Conditions, limitations and remediation commitments are recorded separately. A condition is not a substitute gate state.

A gate evaluation constrains an assurance decision. It does not independently issue one.

---

## Evidence doctrine

Evidence is evaluated for:

- provenance (P);
- fitness and relevance to the assertion (F);
- coverage (C);
- reliability (R);
- timeliness and currentness (T);
- integrity (I);
- sufficiency (S0 to S5) against the control's evidence requirement profile;
- conflict;
- applicability to the assertion, boundary, state and period.

Traceability is a linkage requirement on every evidence object (AIDCF-008 §17A), not a quality score. Each of the 360 controls in registry v1.1 has an evidence requirement profile naming required evidence classes, a quality floor and a sufficiency floor (`registries/controls/evidence-profiles.csv`).

Evidence has no universal authority outside its source, method, scope, time and intended assertion.

The evidence classes are:

- E1 documentary and declarative evidence;
- E2 configuration and technical-state evidence;
- E3 operational and observational evidence;
- E4 validation and test evidence;
- E5 independent and third-party evidence;
- E6 human and experiential evidence;
- E7 derived and analytical evidence.

AI-generated extraction or summarisation may support review but does not independently corroborate its source.

---

## Assessment lifecycle

AIDCF defines the following practitioner lifecycle:

```text
Initiate
→ Profile
→ Scope
→ Tailor
→ Plan
→ Collect
→ Validate
→ Assess
→ Analyse
→ Gate
→ Find
→ Review
→ Decide
→ Report
→ Reassess
```

Assessment methods may include document review, configuration inspection, telemetry analysis, interviews, observation, sampling, scenario analysis and authorised testing.

No disruptive, destructive, hazardous or operationally material test is authorised merely because it appears in AIDCF. Testing requires explicit approval, competent engineering governance, defined rules of engagement and safety controls.

---

## Scoring and decision doctrine

AIDCF scoring supports synthesis, prioritisation, comparison and trend analysis.

It does not create assurance.

The governing rule is:

```text
Evidence supports.
Scores summarise.
Critical gates constrain.
Accountable authority decides.
```

The decision vocabulary includes:

```text
REASONABLY_ASSURED
CONDITIONALLY_ASSURED
LIMITED
NOT_ASSURED
INCONCLUSIVE
```

A decision also has a lifecycle state, recorded separately: `DRAFT`, `RECOMMENDED`, `APPROVED`, `ACTIVE`, `SUSPENDED`, `WITHDRAWN`, `SUPERSEDED`, `EXPIRED`. Legacy labels such as `ADVERSE` and `UNKNOWN_OR_INCONCLUSIVE` are aliases, mapped in `registries/vocabularies/`.

Control results score CONFORMING 100, PARTIAL 50 and NONCONFORMING 0. UNKNOWN, NOT_APPLICABLE and NOT_ASSESSED are excluded from the mean and reduce coverage. Assessment coverage below 50% caps the decision at INCONCLUSIVE and below 80% at LIMITED. Ceilings combine by taking the most restrictive, in the order REASONABLY_ASSURED > CONDITIONALLY_ASSURED > LIMITED > INCONCLUSIVE > NOT_ASSURED, so a demonstrated gate FAIL is never softened to INCONCLUSIVE by thin coverage. A score band (B1 to B5) is reported only when coverage is at least 80% and no US4 or US5 UNKNOWN is open; otherwise the band is WITHHELD.

These are internal AIDCF decision states. They must not be represented as statutory, regulated or accredited assurance levels.

---

## Machine-executable implementation

AIDCF-016 defines the machine-executable data model (MDM 1.3). The generated schema set in `schemas/` covers every AIDCF-014 object class and relationship, using:

- CSV registries;
- JSON Schema;
- JSON-LD;
- RDF and Turtle;
- OWL 2 (`schemas/owl/aidcf-core-1.3.ttl`, namespace `https://w3id.org/aidcf/ontology#`, registration pending);
- SHACL;
- property-graph projections;
- validation fixtures;
- manifests and file hashes;
- graph queries;
- score re-performance records;
- change and supersession events.

The common record model preserves:

- stable identity;
- schema, methodology and profile versions;
- provenance;
- classification;
- observed, recorded and valid times;
- review state;
- accountable roles;
- explicit UNKNOWN;
- supersession and migration.

Technical conformance proves only that declared data and rule requirements were met. It does not prove factual truth, engineering adequacy, safety, operational effectiveness or real-facility assurance.

---

## Synthetic reference implementation

AIDCF-015 v1.3 is the current synthetic reference implementation. It is built on the AIDCF-016 MDM 1.3 schemas and the v1.1 registry.

It includes:

- the complete 15/90/360 registries with per-control gate mappings and evidence profiles;
- closed JSON Schema 2020-12 definitions, a JSON-LD 1.1 context, SHACL shapes and the OWL 2 ontology;
- a synthetic JSON-LD dataset with evidence fixtures and SHA-256 values;
- control assessments, gate results recomputed from the roll-up rule, a score snapshot and deterministic re-performance;
- graph-query outputs;
- positive, negative and anti-gaming fixtures, each expected to fail at a stated layer for a stated reason;
- a release manifest and known-issues register.

All 13 validation layers pass on the current package. The synthetic result is deliberately weak: CG-03, CG-07 and CG-15 FAIL, five gates are UNKNOWN, and the computed decision is NOT_ASSURED because the CG-07 FAIL ceiling controls. The mean is 77.27 over 11 scored controls (12 assessed, one UNKNOWN), and the band is WITHHELD.

### Explicit limitations

- Only 12 representative controls are assessed.
- Coverage equals 3.0556% of the 360-control universe (11 of 360 scored, 12 assessed).
- Evidence is synthetic.
- No real facility is assessed.
- No production assurance conclusion is issued.
- Independent execution and signed review remain pending.
- The release manifest signature is PENDING.

Do not convert the synthetic demonstration into a claim of full implementation, catalogue coverage or real-world assurance.

---

## Relationship with AI Trust Graph

AIDCF and AI Trust Graph are separate but interoperable methods.

AIDCF focuses on infrastructure capability, physical and digital dependencies, failure propagation, safeguards, evidence and bounded infrastructure assurance decisions.

AI Trust Graph focuses on trust, authority and exposure relationships around AI systems.

Supported integration patterns include:

- reference;
- semantic mapping;
- shared identity;
- boundary handoff;
- scenario composition;
- evidence reuse;
- decision federation.

Each method retains its native semantics, findings and decisions. Conclusions must not be automatically merged into a single best-case or worst-case result.

---

## Getting started

### 1. Read the whitepaper

Start with:

```text
whitepaper/current/AIDCF_Technical_Whitepaper_v3.1_Validation_Candidate.md
```

This provides the research problem, framework proposition, status boundaries, limitations and validation roadmap.

### 2. Understand the foundations

Read the Manifesto (AIDCF-001) and the Core Conceptual Model (AIDCF-002), followed by AIDCF-003 through AIDCF-006. AIDCF-002 defines the normative keywords, the canonical chain and the terms used everywhere else.

### 3. Inspect the canonical registry

Review:

```text
standards/aidcf-007a/registry/AIDCF-007A_Canonical_Master_Control_Registry_15-90-360_v1.0.xlsx   (approved baseline)
standards/aidcf-007a/registry/AIDCF-007A_Canonical_Master_Control_Registry_15-90-360_v1.1.xlsx   (PROPOSED)
```

Then read the domain guide (AIDCF-018) for the domains in scope.

Use only canonical `MCF-*` identifiers for new mappings and assessments.

### 4. Review the practitioner method

Read AIDCF-008 through AIDCF-012 for evidence, assessment, scoring, programme governance and reporting requirements, and AIDCF-017 for capability maturity.

### 5. Review the architecture and data standards

Read AIDCF-013, AIDCF-014 and AIDCF-016.

### 6. Run the synthetic package

From `implementation/aidcf-015-v1.3/`:

```bash
python3 -m pip install -r requirements.txt
python3 -B tools/run_all.py
```

The same run executes in CI on every push (`.github/workflows/ci.yml`).

Review the captured outputs rather than relying only on terminal success.

### 7. Do not treat the synthetic result as a facility conclusion

The reference implementation demonstrates structure, validation and traceability. It is not a substitute for an authorised, multidisciplinary assessment of a real capability.

---

## How to review AIDCF

Public and expert review should use issue-based feedback.

Recommended issue categories:

| Code | Category |
|---|---|
| `TECH` | Engineering, architecture or AI-infrastructure validity |
| `ASSUR` | Evidence, assurance, scoring, critical gates or decisions |
| `SEM` | Ontology, identifiers, graph semantics or machine validation |
| `SAFE` | Safety, legal, privacy or security-disclosure concerns |
| `ED` | Editorial clarity, terminology or structure |
| `IMPL` | Implementation, interoperability or tooling |
| `PILOT` | Pilot design, feasibility or measures |

Each issue should contain:

```text
Issue ID
Artifact and version
Section, object or identifier
Issue statement
Evidence or reasoning
Severity
Recommended change
Conflict-of-interest disclosure
```

Recommended severity levels:

```text
BLOCKER
MAJOR
MODERATE
EDITORIAL
```

A disposition should be recorded as:

```text
ACCEPT
PARTIAL
REJECT
DEFER
```

with rationale and closure evidence.

---

## Contributing

AIDCF welcomes evidence-based technical, assurance, semantic, implementation and editorial contributions. Review expectations, issue taxonomy, pull-request requirements, conflict disclosure and contributor conduct are defined in [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Independent review needed

The framework specifically seeks independent challenge from:

- electrical-power engineers;
- mechanical and liquid-cooling engineers;
- compute and HPC architects;
- storage and network-fabric specialists;
- data-centre operations and reliability practitioners;
- OT and control-system security specialists;
- evidence and assurance specialists;
- statistics and measurement reviewers;
- safety, legal and privacy reviewers;
- ontology and semantic-web reviewers;
- independent practitioners not involved in the framework's development.

Independent review should challenge the framework, not endorse it by default. The structured instrument for this is the expert-panel kit in [`validation/expert-panel/`](validation/expert-panel/README.md).

---

## Pilot programme

AIDCF includes a mini-pilot pack in [`pilots/`](pilots/README.md): the AIDCF-PIL-001 protocol, a 58-control Starter Profile covering gates CG-01, CG-02, CG-03, CG-05, CG-06, CG-07 and CG-10 at AL3 (no disruptive testing), and authorisation, evidence-request, result and lessons-learned templates. The best decision such a pilot can reach is LIMITED, because the other gates are out of scope. No authorised pilot is claimed by this repository unless signed pilot records are published.

A legitimate pilot requires:

- a named organisational sponsor;
- a defined Capability Instance;
- a capability owner;
- a bounded decision question;
- an approved scope and profile;
- explicit evidence access;
- safety and testing authorisation;
- competent multidisciplinary assessors;
- an independent reviewer;
- information-classification and disclosure decisions;
- accountable decision authority;
- approved public-use terms for any published findings.

Unsigned templates or synthetic cases are not evidence of an authorised pilot.

---

## Security and responsible disclosure

AIDCF materials may expose sensitive infrastructure dependencies, privileged paths, recovery weaknesses or physical routes. Do not publish secrets, credentials, real-site vulnerabilities or unauthorised evidence. Review the classification model and private-reporting expectations in [SECURITY.md](SECURITY.md).

---

## Governance

AIDCF governance covers artifact authority, canonical identifiers, decision rights, change control, reviewer independence, gate ratification, release status and claims. The complete governance model is defined in [GOVERNANCE.md](GOVERNANCE.md).

---

## Release policy

AIDCF must remain labelled **Validation Candidate** or **Public Review Draft** until the applicable release gates are satisfied.

Current major release gates include:

- independent multidisciplinary review;
- ratification of the complete critical-gate registry;
- complete framework-derivation records;
- disclosed and reproducible scoring inputs;
- independent semantic and conformance execution;
- at least one genuinely authorised pilot;
- reviewer dispositions and closure evidence;
- selected licences;
- DOI and publication metadata;
- accessible archival PDF;
- public review channel and governance process.

---

## Citation

Until a DOI is assigned, cite the whitepaper as:

```text
Sethumadhavan, S. AIDCF: AI Data Centre Facilities Assurance Framework.
Technical Whitepaper v3.1, Validation Candidate for Independent Review, 2026.
```

Citation metadata is in [CITATION.cff](CITATION.cff).

---

## Licence

AIDCF uses separate licences for content and code. See [LICENSE](LICENSE) for the full mapping.

| Material | Licence |
|---|---|
| Whitepapers, documentation, standards, registries and data | [CC BY 4.0](LICENSES/CC-BY-4.0.txt) |
| Schemas, validators, software and the AIDCF-015 reference implementation | [Apache 2.0](LICENSES/Apache-2.0.txt) |
| AIDCF name, logos and marks | Not licensed |

No rights to third-party standards or proprietary material are granted by AIDCF.

---

## Author and conflict disclosure

**Author:** Siva Sethumadhavan

The author originated AIDCF and therefore has an inherent intellectual and professional interest in its development and adoption.

The framework mitigates this conflict through explicit limitations, visible UNKNOWN, negative and anti-gaming tests, versioned evidence, open review, reviewer-disposition records and a roadmap for independent challenge.

No external organisational endorsement is claimed unless expressly and verifiably stated in a signed publication record.

---

## Current roadmap

### Immediate priorities

- complete independent multidisciplinary review;
- ratify the canonical critical-gate registry;
- populate and review the full derivation records;
- perform independent T7 execution;
- complete runtime semantic validation;
- approve licences and publication metadata;
- execute one authorised pilot (pack ready in `pilots/`);
- run the incident back-test (AIDCF-VAL-001) and the expert panel (AIDCF-VAL-002).

### After pilot evidence

- calibrate control and gate wording;
- evaluate inter-rater agreement;
- publish anonymised lessons where authorised;
- update the whitepaper and practitioner artifacts;
- define an implementation backlog from validated evidence;
- assess whether a reference software platform is justified.

---

## Repository integrity checklist

Before each release, confirm:

- [ ] only current authoritative artifacts are in the main branch;
- [ ] superseded drafts are archived or released under historical tags;
- [ ] every artifact has a version, status and owner;
- [ ] registry cardinalities equal 15 domains, 90 families and 360 controls;
- [ ] all live control references use canonical `MCF-*` identifiers;
- [ ] every executable file appears in the release manifest;
- [ ] release hashes are regenerated and verified;
- [ ] positive, negative and anti-gaming tests are executed;
- [ ] graph-query and score re-performance outputs are retained;
- [ ] unresolved UNKNOWN and limitations remain visible;
- [ ] no certification or real-facility assurance claim is introduced;
- [ ] publication classification and redaction checks are complete;
- [ ] licence, citation and DOI metadata are accurate;
- [ ] independent review status is stated truthfully.

---

## Final doctrine

> AIDCF does not create assurance through document volume, control counts or scores. Assurance is bounded by the capability, outcomes, architecture, dependencies, operating states, evidence, critical gates, review quality and accountable decision authority.

Where the evidence chain is incomplete, AIDCF preserves uncertainty and withholds stronger claims rather than manufacturing certainty.
