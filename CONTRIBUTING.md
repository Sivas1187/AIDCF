# Contributing to AIDCF

Thank you for helping challenge and improve the AI Data Centre Facilities Assurance Framework.

AIDCF is a validation candidate. Contributions should increase technical validity, traceability, reproducibility and claim discipline. Contributions should not be used to create an impression of certification, organisational endorsement or external validation where those conditions do not exist.

## 1. Contribution scope

Contributions are welcomed in:

- electrical power and energy continuity;
- mechanical, thermal and liquid-cooling engineering;
- accelerated compute and HPC architecture;
- storage, metadata and checkpoint systems;
- high-performance network and interconnect fabrics;
- data-centre operations and service management;
- resilience, continuity and recovery;
- utilities, suppliers, OEMs and concentration risk;
- digital, OT and control-plane security;
- evidence and assurance methodology;
- measurement, scoring and calibration;
- ontology, knowledge graphs and semantic-web engineering;
- JSON Schema, JSON-LD, RDF/OWL and SHACL;
- validation fixtures and conformance tooling;
- structured research reviews;
- controlled pilot design;
- accessibility, terminology and editorial clarity.

## 2. Contribution types

### Issues

Use an issue for defects, review observations, questions, requests for evidence, proposed extensions and implementation problems.

### Pull requests

Use a pull request for a bounded change with identifiable affected artifacts, validation and migration impact.

### Review memoranda

Independent reviewers may submit a structured review covering competence, independence, scope, evidence, observations, severity and disposition recommendations.

### Pilot evidence

Pilot submissions require organisational authorisation, appropriate anonymisation, classification review and explicit permission for publication.

## 3. Issue taxonomy

| Code | Category |
|---|---|
| `TECH` | Infrastructure, engineering or architecture validity |
| `ASSUR` | Evidence, assessment, scoring, gates, decisions or reporting |
| `SEM` | Ontology, identifiers, graph semantics or machine validation |
| `SAFE` | Safety, legal, privacy or security-disclosure concern |
| `IMPL` | Schemas, validators, tooling or interoperability |
| `PILOT` | Pilot design, authorisation, measurement or evidence |
| `ED` | Editorial structure, terminology, accessibility or presentation |

## 4. Severity

| Severity | Meaning |
|---|---|
| `BLOCKER` | Could invalidate a material claim, create unsafe use, corrupt canonical identity or prevent release |
| `MAJOR` | Material technical, assurance or reproducibility weakness requiring correction |
| `MODERATE` | Important weakness that does not independently invalidate the framework |
| `EDITORIAL` | Clarity, formatting, navigation or non-substantive language issue |

## 5. Required issue fields

Every substantive issue should include:

```text
Issue ID
Issue category
Severity
Artifact and version
Section, object or canonical identifier
Problem statement
Evidence or reasoning
Affected claims or downstream artifacts
Recommended disposition
Conflict-of-interest disclosure
Security classification
```

Do not include confidential evidence, personal data, credentials, exploitable facility details or restricted diagrams in a public issue.

## 6. Evidence expectations

Strong contributions distinguish:

- directly observed fact;
- source-derived statement;
- interpretation;
- proposed design choice;
- hypothesis requiring validation;
- reviewer opinion.

Where possible, identify:

- authoritative source;
- edition or version;
- relevant section or record;
- access date for dynamic web content;
- applicability limits;
- conflicting evidence.

Missing or inconclusive evidence should remain `UNKNOWN` rather than being presented as fact.

## 7. Pull-request requirements

A pull request should contain:

1. a concise problem statement;
2. the affected artifact IDs and versions;
3. the proposed change;
4. reason and supporting evidence;
5. backward-compatibility assessment;
6. identifier and migration impact;
7. assessment, scoring, gate, report and graph impact;
8. tests or fixtures where applicable;
9. updated changelog entry;
10. disclosure of conflicts and generated content.

### Canonical identity rules

- Do not silently rename or reuse a canonical ID.
- Do not delete approved records from history.
- Use `DEPRECATED`, `SUPERSEDED` or `RETIRED` with explicit migration.
- Do not reintroduce the superseded 14/84/336 baseline.
- New controls require domain, family, intent, evidence, assessment, failure and gate analysis.

### Machine-readable changes

Changes to schemas, contexts, shapes or registries should include:

- schema version change;
- positive fixture;
- negative fixture;
- expected validation result;
- migration note;
- manifest and hash update;
- graph-query or score impact where applicable.

## 8. Critical-gate changes

Changes to `CG-01` through `CG-15` require heightened review.

A proposal must state:

- gate purpose;
- applicability rule;
- minimum evidence floor;
- `PASS` criteria;
- `FAIL` criteria;
- `UNKNOWN` criteria;
- `APPROVED_NA` criteria;
- decision effect;
- review authority;
- reassessment trigger;
- downstream control, score and reporting impact.

No gate change is canonical until approved under GOVERNANCE.md.

## 9. Safe research and testing

AIDCF does not authorise operational testing.

Do not submit or perform instructions for live switching, load shedding, discharge, failover, thermal stress, fluid interruption, exploitation, destructive testing or other material operational actions without explicit authority and competent safety and engineering governance.

Synthetic and lab tests should be clearly labelled and isolated from real-facility claims.

## 10. Use of AI-assisted tools

AI-assisted drafting, coding, extraction or summarisation may be used if:

- the contributor remains accountable;
- sources are verified;
- generated text is reviewed for fabricated claims;
- confidential content is not exposed improperly;
- generated candidate evidence is not treated as corroboration;
- the contribution discloses material AI assistance when appropriate.

## 11. Review and disposition

Maintainers may disposition a contribution as:

- `ACCEPT`;
- `PARTIAL`;
- `REJECT`;
- `DEFER`.

The disposition should include rationale and closure evidence. Author action does not equal independent reviewer acceptance.

## 12. Independence and conflicts

Reviewers should disclose:

- prior authorship or design involvement;
- employment or commercial interest;
- vendor relationships;
- assurance-provider role;
- pilot sponsor relationship;
- any other interest that may affect impartiality.

A disclosed conflict does not automatically disqualify a contribution, but it must be visible when assessing weight and independence.

## 13. Contributor conduct

Contributors must:

- engage respectfully and professionally;
- critique claims and evidence rather than individuals;
- avoid discriminatory, harassing or threatening conduct;
- respect confidentiality and intellectual property;
- avoid misleading claims of endorsement, accreditation or certification;
- accept that evidence may require revision of the framework.

The project Code of Conduct is in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## 14. Licensing

Do not contribute material unless you have the right to do so under the repository's selected licences.

Do not copy requirements, figures or substantial text from third-party standards unless permission and licensing allow it. A citation or crosswalk is not permission to reproduce proprietary content.

## 15. Suggested contribution workflow

```text
Open issue
→ Establish scope and classification
→ Provide evidence
→ Discuss alternatives
→ Submit bounded pull request
→ Run tests
→ Conduct technical and assurance review
→ Record disposition
→ Approve or reject
→ Update version, manifest and changelog
→ Preserve supersession history
```

## 16. Current priority areas

Priority contributions include:

- independent review of the 15-domain model;
- completeness and duplicate analysis of the 360-control catalogue;
- canonical gate ratification;
- reproducible scoring examples;
- independent execution of the synthetic package;
- semantic-runtime validation;
- inter-rater assessment experiments;
- authorised pilot design and execution;
- public source and derivation records;
- accessibility and archival publication quality.
