# AIDCF Governance

## 1. Purpose

This document defines governance for the AI Data Centre Facilities Assurance Framework.

AIDCF is currently a validation candidate. Governance must preserve technical integrity, canonical identity, evidence discipline, reviewer independence, safe use and truthful public claims.

## 2. Governance principles

1. **Capability primacy:** assurance begins with a bounded Capability Instance and Service Outcomes.
2. **Evidence before conclusion:** material assertions require relevant and reviewable evidence.
3. **Visible uncertainty:** material uncertainty remains `UNKNOWN`.
4. **Gate dominance:** critical prerequisites are not averaged away.
5. **Human authority:** tools recommend; accountable people decide.
6. **Stable identity:** canonical identifiers are not silently reused or redefined.
7. **Traceable change:** changes include rationale, impact, version and migration.
8. **Separation of duties:** preparation, review and decision authority should be distinguishable.
9. **Safe application:** the framework does not authorise hazardous or disruptive testing.
10. **Claim restraint:** adoption does not imply certification, accreditation, legal compliance or engineering approval.

## 3. Governance scope

Governance applies to:

- whitepapers and public documentation;
- foundation standards;
- the canonical control registry;
- critical-gate definitions;
- evidence, assessment, scoring and reporting methods;
- architecture and machine-executable standards;
- schemas, contexts, shapes and registries;
- synthetic implementation packages;
- validation records;
- pilot profiles and results;
- names, marks and public claims;
- repository releases and supersession.

## 4. Authority hierarchy

When AIDCF artifacts conflict, use this order until superseded by a formally approved release manifest:

1. approved constitutional amendments;
2. approved canonical registries;
3. approved release manifest and migration records;
4. current normative methodology artifacts;
5. implementation profiles and schemas;
6. whitepapers and explanatory material;
7. synthetic examples;
8. historical and archived artifacts.

External law, regulation, professional engineering obligations, safety requirements, contractual duties and source standards remain authoritative within their scope.

## 5. Governance roles

| Role | Responsibility | Current position |
|---|---|---|
| Methodology Owner | Maintains framework coherence and release proposals | Author-controlled pending broader governance |
| Registry Custodian | Maintains canonical IDs, statuses and mappings | To be formally appointed |
| Technical Maintainers | Maintain documents, schemas, tests and tooling | To be appointed by area |
| Domain Reviewers | Challenge technical requirements and evidence by domain | Independent reviewers pending |
| Assurance Reviewer | Reviews evidence doctrine, gates, scoring and decision constraints | Pending |
| Semantic Reviewer | Reviews ontology, graph, JSON-LD, RDF/OWL and SHACL | Pending |
| Safety, Legal and Privacy Reviewer | Reviews safety boundaries, claims, disclosure and legal risk | Pending |
| Pilot Sponsor | Authorises a real pilot and owns organisational decision use | No authorised pilot claimed |
| Decision Authority | Issues a bounded Assurance Decision for a specific engagement | Engagement-specific |
| Release Approver | Approves publication status after release gates are evaluated | Current framework owner pending independent review structure |

The current role model is transitional. Author control must not be presented as independent approval.

## 6. Artifact statuses

| Status | Meaning |
|---|---|
| `DRAFT` | Under active development |
| `CONTROLLED_REVIEW` | Stable enough for structured review but not approved |
| `APPROVED_BASELINE` | Adopted within AIDCF governance for identity or normative use |
| `VALIDATION_CANDIDATE` | Integrated release awaiting independent evidence |
| `EXTERNALLY_VALIDATED` | Independent execution or empirical validation completed for the stated scope |
| `DEPRECATED` | Retained but discouraged for new use |
| `SUPERSEDED` | Replaced by an identified later artifact |
| `RETIRED` | Historical, no longer supported |

## 7. Canonical baseline

AIDCF-007A establishes the current AIDCF-internal baseline:

```text
15 domains
90 control families
360 controls
```

The superseded 14/84/336 baseline must not be used in live coverage, scoring, reporting or machine execution.

Canonical identifiers remain stable. Meaning-changing replacement requires a new version or identifier, explicit impact analysis and migration.

## 8. Change classes

### Editorial change

Clarifies language without changing meaning, applicability, evidence, result or decision effect.

### Minor normative change

Changes a requirement or mapping without altering the framework's constitutional doctrine or control-universe cardinality.

### Major normative change

Changes domain structure, control objective, gate logic, scoring behaviour, assurance decision rules or machine contract materially.

### Constitutional change

Changes principles, authority boundaries, cardinality, canonical status model or governance doctrine.

## 9. Change proposal requirements

Every material change proposal must include:

```text
Change ID
Proposer
Affected artifact and version
Change class
Problem statement
Evidence and rationale
Proposed text or machine delta
Backward-compatibility impact
Control and gate impact
Evidence and assessment impact
Scoring and decision impact
Schema and graph impact
Security and safety impact
Migration plan
Reviewer requirements
```

## 10. Approval thresholds

### Editorial

May be accepted by the relevant maintainer with recorded review.

### Minor normative

Requires the methodology owner, relevant artifact maintainer and at least one competent reviewer.

### Major normative

Requires multidisciplinary technical and assurance review, validation evidence, migration analysis and release approval.

### Constitutional

Requires a formal amendment, published rationale, cross-artifact impact analysis and explicit supersession.

Until an independent governance body exists, approvals must disclose that they are AIDCF-internal and author-controlled where applicable.

## 11. Critical-gate governance

Critical gates are non-compensating decision constraints.

A canonical gate record must define:

- gate ID and name;
- purpose;
- applicability rule;
- minimum evidence floor;
- `PASS`, `FAIL`, `UNKNOWN`, `APPROVED_NA` and `NOT_ASSESSED` rules;
- assurance ceiling and decision effect;
- required reviewer competence;
- reassessment triggers;
- version and supersession.

A gate definition is not canonical solely because it appears in a whitepaper, example or implementation package.

Formal gate ratification requires review by relevant domain specialists, an assurance/scoring reviewer and the methodology owner, with unresolved objections recorded.

## 12. Control governance

A canonical control must include:

- stable control ID;
- domain and family;
- title and intent;
- normative requirement;
- applicability and operating states;
- assessment criteria and method;
- minimum evidence;
- failure and safeguard linkage;
- gate mapping;
- reassessment triggers;
- status and version.

Controls are not deleted silently. They may be deprecated or superseded with migration.

## 13. Scoring governance

Scoring configurations must be versioned and reproducible.

They must disclose:

- applicable profile;
- dimensions and weights;
- raw and adjusted calculations;
- evidence-quality treatment;
- UNKNOWN and coverage treatment;
- aggregation rules;
- gate overlay;
- recommendation rule;
- input and output hashes where machine execution is claimed.

Scores do not issue or strengthen an Assurance Decision beyond the evidence and gate position.

## 14. Independent review

Independent review should collectively cover:

- electrical power;
- thermal and fluid systems;
- compute/HPC;
- storage and networks;
- operations and resilience;
- OT and control-plane security;
- evidence and assurance;
- measurement and statistics;
- safety, legal and privacy;
- ontology and machine validation.

Reviewers disclose conflicts, prior design involvement and commercial interest.

Review outcomes are:

```text
ACCEPT
ACCEPT_WITH_CONDITIONS
REJECT
DEFER
```

Author disposition is not equivalent to independent reviewer acceptance.

## 15. Pilot governance

A real pilot requires:

- named sponsor and Capability Owner;
- decision question and intended users;
- approved boundary and operating states;
- control, gate and evidence profile;
- assessor competence and independence decisions;
- safety and test authorisation;
- classification and data-handling approval;
- independent reviewer;
- accountable Decision Authority;
- agreed publication and anonymisation rules.

Synthetic fixtures and unsigned templates are not authorised pilots.

## 16. Release governance

A release must include:

- version and status;
- authoritative artifact list;
- change log;
- supersession and migration records;
- known issues;
- validation results;
- classification review;
- manifest and hashes for executable packages;
- licence and citation metadata;
- approval record.

The default branch should expose only the current authoritative set. Historical material should be preserved in releases, tags or an archive branch.

## 17. Public-claim governance

Permitted claims must state version, scope and status.

Examples:

```text
Uses concepts from AIDCF vX.Y
Assessed using AIDCF vX.Y within the stated scope
AIDCF validation candidate implementation
Synthetic AIDCF reference implementation
```

Prohibited or controlled claims include:

```text
AIDCF Certified
AIDCF Accredited
Globally compliant
Universally safe or resilient
Externally validated
Production proven
```

unless a future authorised governance mechanism and evidence specifically permit the claim.

## 18. Conflict resolution

Conflicts between artifacts create a `BaselineIssue` or equivalent controlled record.

The resolution must identify:

- competing sources;
- authoritative decision;
- affected objects;
- migration;
- downstream impact;
- effective date;
- supersession.

Content must not be reconciled silently merely to produce a favourable outcome.

## 19. Appeals and challenges

A contributor or reviewer may challenge:

- applicability;
- control wording;
- gate state;
- evidence sufficiency;
- reviewer competence or independence;
- scoring and recommendation;
- release status;
- public claim.

The challenge should identify evidence and requested remedy. The resolver must be sufficiently independent of the original decision.

## 20. Records and transparency

Governance records should include:

- issue and change registers;
- review comments and dispositions;
- conflict disclosures;
- approval records;
- decision logs;
- release manifests;
- pilot authorisations;
- supersession and migration records.

Sensitive records may be restricted, but public releases should disclose material limitations and governance status.

## 21. Current governance gaps

The current framework still requires:

- named independent reviewers;
- ratified canonical gate records;
- populated derivation records;
- independent T7 execution;
- runtime semantic validation;
- a genuinely authorised pilot;
- selected licences;
- public review and security-reporting channels;
- a durable multi-person maintenance model.

Until those items are addressed, AIDCF remains a validation candidate.

## 22. Governance review cycle

Governance should be reviewed after:

- a major release;
- a material pilot finding;
- an incident or unsafe-use report;
- a control-universe change;
- a material external standard change;
- emergence of a new stakeholder or authority model;
- evidence that the current process impedes valid challenge or correction.

## 23. Final governance doctrine

AIDCF authority must be earned through transparent evidence, competent review, reproducible execution and disciplined claims. Document volume, control counts and author approval do not independently establish external validity.
