> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-014_End-to-End_Traceability_and_Machine-Executable_Data_Standard_v1.1.pdf](AIDCF-014_End-to-End_Traceability_and_Machine-Executable_Data_Standard_v1.1.pdf).

**AIDCF**

**AI Data Centre Facilities Assurance Framework**

**END-TO-END TRACEABILITY AND MACHINE-EXECUTABLE DATA STANDARD**

**A canonical information contract for identifiers, objects, relationships, lineage, vocabularies, validation, exchange, change impact and conformance**

# Document control

| **Field**              | **Value**                                                                                                                                           |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Public ID              | AIDCF-014                                                                                                                                           |
| Short code             | TDS (requirement IDs TDS-REQ-NNN)                                                                                                                   |
| Title                  | End-to-End Traceability and Machine-Executable Data Standard                                                                                        |
| Version                | 1.1                                                                                                                                                 |
| Date                   | 2026-10-10                                                                                                                                          |
| Status                 | Draft for controlled review                                                                                                                         |
| Author                 | Siva Sethumadhavan                                                                                                                                  |
| Depends on             | AIDCF-002, AIDCF-003, AIDCF-004, AIDCF-005, AIDCF-006, AIDCF-007A, AIDCF-008, AIDCF-009, AIDCF-010, AIDCF-011, AIDCF-012, AIDCF-013                |
| Normative companion    | AIDCF-016 Machine-Executable Data Model Standard (serialisation, schema and ontology package)                                                       |
| Used by                | AIDCF-015 (reference implementation and synthetic dataset), AIDCF-017, AIDCF-018, AIDCF-019, AIDCF-VR-001                                           |
| Boundary               | Technical conformance to this standard is not engineering approval, assurance or certification.                                                    |

## Revision history

| **Version** | **Date**   | **Summary**                                                                                                                                                                                                                                                                                                                         |
|-------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | Not stated | Initial draft (internal ID AIDCF-TDS-001): object, relationship and registry inventories, serialisation list, business rules, conformance tests and templates.                                                                                                                                                                     |
| 1.1         | 2026-10-10 | Public ID AIDCF-014 adopted; vocabularies aligned to the canonical specification (control result, gate result, decision state and lifecycle, operating state) with legacy alias tables; namespace and version IRI declared; AIDCF-016 named as normative serialisation companion; 48 classes and 41 relationship types fully defined; release manifest requirements specified; boilerplate rows replaced; numbered requirements TDS-REQ-001 onward; §15–§17 aligned to published AIDCF-016 and registry catalogue. |

# Executive thesis

**Every material assurance conclusion shall be reconstructable, by a person or a machine, from stable identities, pinned source versions, typed relationships, evidence and recorded human review. Missing data is UNKNOWN, conflicting data is a BaselineIssue or a CHALLENGES edge, and neither is silently resolved.**

AIDCF-014 is the information contract of the framework. It defines *what* must be recorded and linked (classes, relationships, vocabularies, lineage, business rules and conformance tests). AIDCF-016 defines *how* it is serialised (JSON Schema, JSON-LD context, OWL ontology, SHACL shapes, CSV registry layouts and the versioned schema and ontology package). Where the two differ, AIDCF-014 governs meaning and AIDCF-016 governs syntax; a difference in meaning is a BaselineIssue (§6).

## Canonical assurance chain

The chain below is the only assurance chain in AIDCF and is based on the ISO/IEC/IEEE 15026-2 assurance-case structure. Each step is a class in §7; each arrow is one or more relationship types in §9; each traceability rule in §11 tests one or more arrows.

| **Step** | **Chain element**                              | **Principal classes (§7)**                                         | **Forward relationship(s) (§9)**                           |
|----------|------------------------------------------------|--------------------------------------------------------------------|------------------------------------------------------------|
| 1        | Decision Question                              | Assessment (decisionQuestion), AssuranceProgram                    | GOVERNED_BY (Assessment to AssuranceProgram)               |
| 2        | Capability Instance                            | CapabilityInstance                                                 | HAS_OUTCOME                                                |
| 3        | Service Outcome                                | ServiceOutcome                                                     | REQUIRES_FUNCTION                                          |
| 4        | Required Function                              | RequiredFunction                                                   | IMPLEMENTED_BY                                             |
| 5        | Architecture                                   | ArchitectureSnapshot, InfrastructureSystem, AssetInstance, Interface, Resource, CapacityAssertion | COMPOSED_OF, CONNECTS_TO, CONSUMES_RESOURCE, CONTROLLED_BY, MONITORED_BY, LOCATED_IN |
| 6        | Dependency and Fault Domain                    | Dependency, FaultDomain                                            | DEPENDS_ON, SHARES_FAULT_DOMAIN_WITH                       |
| 7        | Threat / Hazard / Failure Scenario             | Threat, Hazard, FailureMode, FailureScenario                       | EXPOSED_TO, INITIATES, PROPAGATES_TO                       |
| 8        | Safeguard                                      | Safeguard                                                          | PROTECTED_BY, RECOVERS_THROUGH                             |
| 9        | Control                                        | ControlDomain, ControlFamily, Control                              | GOVERNED_BY (Safeguard to Control)                         |
| 10       | Evidence Requirement                           | EvidenceRequirement                                                | HAS_EVIDENCE_REQUIREMENT                                   |
| 11       | Evidence Object                                | EvidenceObject, EvidencePackage                                    | EVIDENCED_BY, SUPPORTS, CHALLENGES, QUALIFIES              |
| 12       | Control Assessment (result)                    | Assessment, AssessmentProcedure, Sample, TestRecord, ControlAssessment | ASSESSED_BY, RESULTS_IN                                |
| 13       | Finding / UNKNOWN Record                       | Finding, UnknownRecord                                             | HAS_FINDING, HAS_UNKNOWN                                   |
| 14       | Gate Result                                    | CriticalGate, GateResult                                           | EVALUATES_GATE, CONSTRAINS                                 |
| 15       | Score Snapshot and Decision Recommendation     | ScoreSnapshot, DecisionRecommendation                              | SUMMARISED_BY, RECOMMENDS                                  |
| 16       | Assurance Decision                             | AssuranceDecision, ReviewRecord                                    | REVIEWED_BY, APPROVED_BY                                   |
| Loop     | Report and Reassessment Trigger                | AssuranceStatement, AssuranceReport, Action, ReassessmentTrigger, Event | REPORTED_IN, REQUIRES_ACTION, CLOSED_BY, INVALIDATED_BY, TRIGGERS_REASSESSMENT |

Assurance-case mapping: the top claim and sub-claims at steps 3 to 8 are Claims; decomposition by function, dependency and scenario is the Argument/Strategy; steps 10 to 12 are Evidence; CHALLENGES edges, Findings and UNKNOWN Records are defeaters; operating states, boundary and exclusions are Context.

# 1 Authority and precedence

**TDS-REQ-001** Each canonical class, relationship type and vocabulary shall have exactly one semantic owner artifact (§7, §9, §11A). A schema, ontology, shape or tool shall not redefine a term whose semantic owner is another artifact.

**TDS-REQ-002** A schema, shape, profile, extension or tool shall not weaken a normative rule of AIDCF-006 to AIDCF-012 (for example by making a mandatory link optional, accepting an undeclared state code or permitting a score to override a gate).

**TDS-REQ-003** Where two sources disagree on a count, identifier, title, definition, mapping or status, implementations shall not choose one silently; they shall create a BaselineIssue (§6).

**TDS-REQ-004** Every exchange or publication of AIDCF data shall be bound to a ReleaseManifest (§4) that pins the versions and hashes of the artifacts, registries, vocabularies, schemas and ontology it relies on.

**TDS-REQ-005** This standard is technology neutral. Conformance shall be evaluated on the information content and behaviour defined here, not on any particular database, graph store, programming language or product.

**TDS-REQ-006** Automated components may validate, derive, propose and flag. They shall not approve a material fact, a control result, a gate result, a decision or a report. Approval is recorded only through a ReviewRecord linked by REVIEWED_BY or APPROVED_BY to an accountable person.

**TDS-REQ-007** Records shall not be destructively overwritten. Change is expressed by a new version or by a superseding record (SUPERSEDES), and prior versions shall remain retrievable.

**TDS-REQ-008** Structural validity (schema, shape or test pass) shall not be presented as evidence that a claim is true, that a design is adequate, or that any assurance level has been achieved.

Precedence when sources conflict: (1) AIDCF-007A amendment instruments and the canonical specification baseline for identifiers and cardinality; (2) the semantic owner artifact named in §7 or §9 for meaning; (3) this standard for structure, linkage and validation; (4) AIDCF-016 for serialisation syntax; (5) implementation documentation. A conflict at any level is recorded as a BaselineIssue.

# 2 Constitutional invariants

The invariants below are properties that every conformant dataset shall exhibit at all times. Each is testable by the conformance tests in §31.

| **Requirement** | **Invariant**                          | **Testable statement**                                                                                                                                                                       |
|-----------------|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TDS-REQ-009**   | Capability and outcomes are primary    | Every Assessment references exactly one CapabilityInstance and at least one ServiceOutcome; no ControlAssessment exists without a scope that resolves to a CapabilityInstance.                |
| **TDS-REQ-010**  | Assertions require evidence or UNKNOWN | Every material assertion (CapacityAssertion, Dependency, FaultDomain independence, ControlAssessment, GateResult) has at least one EVIDENCED_BY edge to an EvidenceObject or a HAS_UNKNOWN edge. |
| **TDS-REQ-011**   | UNKNOWN is first-class                 | An unresolved fact is an UnknownRecord with type (U1–U10) and severity (US1–US5); a null value without nullReason is invalid.                                                                 |
| **TDS-REQ-012**  | Gates are separate from scores         | ScoreSnapshot never sets or modifies a GateResult; an AssuranceDecision references GateResults directly, not through scores.                                                                  |
| **TDS-REQ-013**  | Claim types are distinct               | A ControlAssessment records exactly one claim type (DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS, RESILIENCE); a result for one claim type is not reused for another.                     |
| **TDS-REQ-014**   | Dependencies are visible               | Every DEPENDS_ON edge references a Dependency record with direction, conditions (operating states) and criticality, or an UnknownRecord for each missing attribute.                          |
| **TDS-REQ-015**   | Lineage is mandatory                   | Every derived record (ControlAssessment, GateResult, ScoreSnapshot, DecisionRecommendation, AssuranceDecision, AssuranceStatement) can be traced to its inputs by the rules in §11.          |
| **TDS-REQ-016**   | Change can invalidate                  | An Event that matches a ReassessmentTrigger can create INVALIDATED_BY edges and change dependent decision lifecycle to SUSPENDED after human disposition.                                       |
| **TDS-REQ-017**  | Automation proposes                    | Records created by automated components carry reviewState CANDIDATE until a ReviewRecord accepts them.                                                                                       |
| **TDS-REQ-018**  | AIDCF and AITG conclusions are separate | An AIDCF AssuranceDecision is never asserted as, or derived automatically from, an AI Trust Graph conclusion, or vice versa; the only cross-framework link is INTEGRATION_HANDOFF (AIDCF-005). |
| **TDS-REQ-019**  | Connectivity is not causality          | CONNECTS_TO does not imply DEPENDS_ON, PROPAGATES_TO, CONTROLLED_BY or reachability; each must be asserted and evidenced separately.                                                          |
| **TDS-REQ-020**  | Sensitive paths are controlled         | Records and edges describing exploitable paths (for example remote-access routes to OT controllers) carry a classification and a DistributionControl, and are excluded from exports that do not authorise them. |

# 3 Conformance levels

Conformance levels are cumulative: level T*n* requires all criteria of T0 to T*n*−1. An implementation claims the highest level whose criteria it meets in full, stating the ReleaseManifest it was tested against.

| **Level** | **Name**                   | **Criteria (all mandatory for the level)**                                                                                                                                                                          |
|-----------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| T0        | Vocabulary                 | Uses canonical codes of §11A and the canonical specification; legacy codes accepted only on input and mapped through the alias tables; no undeclared code is emitted.                                              |
| T1        | Records and identifiers    | All records use the common envelope (§8) and the identifier rules (§5); IDs are unique and stable across versions.                                                                                                |
| T2        | Traceability               | All traceability rules TR-01 to TR-18 (§11) are evaluated; every gap is reported as a validation failure or an UnknownRecord.                                                                                     |
| T3        | Structural validation      | All records validate against the AIDCF-016 JSON Schema package for the pinned version, with additionalProperties false.                                                                                          |
| T4        | Graph validation           | The graph projection validates against the AIDCF-016 SHACL shapes, including the domain, range and cardinality constraints of §9.                                                                                |
| T5        | Decision-ready             | Business rules BR-001 to BR-015 (§18) are enforced; gate roll-up and decision ceilings are reproduced from inputs; reports are checked against decisions.                                                         |
| T6        | Continuing assurance       | Events (§20, §21) are ingested; the change-impact contract (§22) is executed; affected records are flagged and routed for human disposition.                                                                     |
| T7        | Test-suite conformance     | The full conformance test suite (§31) for the pinned release passes, and the results are published as a ValidationResult set referenced by the ReleaseManifest.                                                  |

**TDS-REQ-021** A conformance claim shall state the level, the ReleaseManifest identifier, the test-suite version and the date of testing. A claim of T5 or above shall be supported by a published ValidationResult set.

# 4 Release manifest

A ReleaseManifest is the signed, immutable bill of materials for one AIDCF release. All other records are interpreted against it.

**TDS-REQ-022** Every AIDCF release shall publish exactly one ReleaseManifest, serialised as defined in AIDCF-016, containing the fields below.

| **Field**            | **Content and rule**                                                                                                                                                                                                  |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| releaseId            | Stable identifier of the release (pattern AIDCF-REL-YYYY.MM.N); never reused.                                                                                                                                         |
| releaseStatus        | Lifecycle code (§11A.1). A release containing any artifact whose status is "Draft for controlled review" shall itself be no higher than REVIEWED.                                                                     |
| artifactManifest     | One entry per artifact: public ID (AIDCF-NNN, AIDCF-007A, AIDCF-VR-001, AIDCF-WP-001), title, version, status, repository path, media type and SHA-256 digest of the exact file.                                       |
| registryVersions     | One entry per registry (§17): name, version, record count and digest. The control registry entry shall assert the cardinality 15 domains, 90 families, 360 controls and shall fail validation if the counts differ. |
| vocabularyVersions   | Version and digest of each controlled vocabulary file (registries/vocabularies/*.csv).                                                                                                                                |
| schemaVersions       | Version and digest of each JSON Schema, the JSON-LD context, the OWL ontology and the SHACL shapes in the AIDCF-016 package, including the ontology version IRI.                                                       |
| approvedCardinality  | The cardinality decision record in force (AIDCF-007A-AMD-001) and any later amendment that applies.                                                                                                                  |
| knownIssues          | References to every open BaselineIssue, with status BLOCKED or CONDITIONALLY_BASELINED.                                                                                                                              |
| migrationSet         | References to MigrationRecords that convert records from the previous release, including vocabulary alias migrations.                                                                                                |
| testSuite            | Conformance test-suite version, digest, and references to the ValidationResult set produced against this release.                                                                                                   |
| approvals            | ReviewRecord references for each required review (§38), each with outcome APPROVED, PENDING or REJECTED. PENDING approvals shall be listed, not omitted.                                                             |
| classification       | Classification code (§11A.8) of the manifest itself.                                                                                                                                                                    |
| supersedes           | releaseId of the previous release, if any.                                                                                                                                                                            |
| integrity            | Digest algorithm, canonicalisation method and detached signature over the manifest.                                                                                                                                  |

**TDS-REQ-023** Digests shall be SHA-256 over the exact bytes of each file. The manifest itself shall be canonicalised with the JSON Canonicalization Scheme (IETF RFC 8785) before its digest is computed and signed.

**TDS-REQ-024** A published ReleaseManifest shall not be modified. A correction is a new ReleaseManifest that SUPERSEDES the previous one.

**TDS-REQ-025** A consumer shall reject, or treat as UNKNOWN, any record whose referenced artifact, registry, vocabulary or schema version is not listed in the ReleaseManifest the record declares.

**TDS-REQ-026** A release whose approvals include any PENDING entry shall be labelled "Draft for controlled review" in every human-readable rendering.

# 5 Identifier standard

## 5.1 Namespace

The AIDCF ontology namespace is `https://w3id.org/aidcf/ontology#` with the prefix `aidcf:`. The version IRI of the ontology aligned to this release is `https://w3id.org/aidcf/ontology/1.3`. Registration of the `w3id.org/aidcf` redirect is pending; until it is confirmed, these IRIs are identifiers only and shall not be assumed to resolve. AIDCF-016 defines the instance-data IRI pattern and the JSON-LD context that maps JSON keys to these IRIs.

## 5.2 Rules

**TDS-REQ-027** Every record shall have an identifier that is unique within its class across all releases and is never reused for a different meaning.

**TDS-REQ-028** A change of meaning shall create a new identifier and a SUPERSEDES edge from the new record to the old. A change that does not alter meaning (correction of a typographical error, a disambiguating title change recorded by amendment) shall create a new version of the same identifier.

**TDS-REQ-029** Version shall be carried separately from identity (the `version` envelope field); identifiers shall not embed version numbers, except release identifiers and ontology version IRIs.

**TDS-REQ-030** Controlled codes shall be used exactly as defined in the canonical patterns below; case is significant.

| **Object**                  | **Pattern**              | **Example**        | **Semantic owner** |
|-----------------------------|--------------------------|--------------------|--------------------|
| Artifact                    | AIDCF-NNN, AIDCF-007A, AIDCF-018-DOM, AIDCF-VR-NNN, AIDCF-WP-NNN | AIDCF-008 | AIDCF-014 |
| Control domain              | three-letter code        | THM                | AIDCF-007A         |
| Control family              | DOM-NN (01–06)           | THM-03             | AIDCF-007A         |
| Control                     | MCF-DOM-NNN (001–024)    | MCF-THM-010        | AIDCF-007A         |
| Critical gate               | CG-NN (01–15)            | CG-06              | AIDCF-010          |
| Amendment                   | AIDCF-007A-AMD-NNN       | AIDCF-007A-AMD-002 | AIDCF-007A         |
| Requirement                 | SHORT-REQ-NNN            | TDS-REQ-001        | Owning artifact    |
| Release                     | AIDCF-REL-YYYY.MM.N      | AIDCF-REL-2026.10.1 | AIDCF-014         |

**TDS-REQ-031** External identifiers (asset tags, CMDB keys, ticket numbers, vendor serial numbers, AITG identifiers) shall be recorded in `externalIdentifiers` as typed pairs (scheme, value) and shall never be used as the AIDCF identifier.

**TDS-REQ-032** Two identifiers that denote the same real-world entity shall be linked only by a reviewed shared-identity assertion carrying evidence and a ReviewRecord; automated matching produces a candidate only.

**TDS-REQ-033** Identifiers minted by automated discovery shall be marked CANDIDATE and shall not be referenced by an approved decision until accepted by review.

**TDS-REQ-034** An identifier collision (same identifier, different meaning) shall block release and create a BaselineIssue with status BLOCKED.

# 6 Baseline harmonisation

**TDS-REQ-035** Conflicts between AIDCF sources shall be recorded as BaselineIssue records, never resolved in place.

| **Attribute**   | **Rule**                                                                                                                                         |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Trigger         | Conflicting counts, identifiers, titles, definitions, mappings, vocabulary codes or statuses between two or more pinned sources.                  |
| Sources         | Each conflicting source is referenced with artifact ID, version, location and the exact conflicting value; original values are preserved verbatim. |
| Status          | BLOCKED (release cannot proceed; dependent records are UNKNOWN) or CONDITIONALLY_BASELINED (a provisional value is adopted with a stated condition and expiry). |
| Resolution      | An approved decision (ReviewRecord), the registry update, a MigrationRecord and, where meaning changes, a SUPERSEDES edge.                         |
| Closure         | CLOSED_BY the ReviewRecord and MigrationRecord; the issue remains in history.                                                                     |

Example: the cardinality conflict between the AIDCF-007 v1.0 workbook (15/90/360) and narrative statements of 14/84/336 is a resolved BaselineIssue, closed by AIDCF-007A-AMD-001.

# 7 Canonical object registry

**TDS-REQ-036** The 48 classes below are the canonical object classes of AIDCF. Each is an `aidcf:` class in the AIDCF-016 ontology; no implementation shall add a class to this list except by extension (§33).

The owner artifact is the semantic owner of the class's meaning (§1). The chain step refers to the canonical assurance chain.

| **#** | **Class**              | **Definition**                                                                                                                              | **Owner artifact** | **Chain step** |
|-------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------|----------------|
| 1     | ReleaseManifest        | Signed, immutable bill of materials pinning every artifact, registry, vocabulary, schema and ontology version of one release.               | AIDCF-014          | Context        |
| 2     | BaselineIssue          | Recorded conflict between pinned sources, with original values, status and resolution lineage.                                              | AIDCF-014          | Context        |
| 3     | CapabilityInstance     | A specific deployment of an AI capability bounded by ownership, location, architecture, capacity, criticality and obligations.              | AIDCF-003          | 2              |
| 4     | ServiceOutcome         | A measurable or assessable result the CapabilityInstance must achieve, with tolerance, duration and operating-state conditions.             | AIDCF-003          | 3              |
| 5     | RequiredFunction       | A function whose loss or degradation materially affects one or more ServiceOutcomes (for example "remove 100% of rack heat at design inlet temperature"). | AIDCF-003 | 4  |
| 6     | ArchitectureSnapshot   | A versioned, approved and immutable view of the architecture in scope at a point in time, against which assessments are performed.         | AIDCF-013          | 5              |
| 7     | InfrastructureSystem   | A coordinated set of assets and interfaces providing one or more functions (for example a CDU secondary loop, a UPS system, a scale-out fabric). | AIDCF-003      | 5              |
| 8     | AssetInstance          | An identifiable real-world item, service, procedure or resource provider represented where material (for example a switchboard, a CDU, a GPU node). | AIDCF-003    | 5              |
| 9     | Interface              | A defined point or mechanism of exchange between entities (electrical, thermal, fluid, network, management, data, physical, operational, provider). | AIDCF-003   | 5              |
| 10    | Resource               | A consumable or constrained input required for operation (electrical capacity, cooling capacity, water, fuel, rack space, accelerator hours). | AIDCF-003         | 5              |
| 11    | Dependency             | A reified reliance of one entity on another entity, resource, condition or decision, with direction, strength, states and substitutability. | AIDCF-003          | 6              |
| 12    | FaultDomain            | A set of entities expected to be affected together by a common cause of failure, with its boundary and blast radius.                        | AIDCF-003          | 6              |
| 13    | OperatingState         | A defined condition of operation (NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION, SHUTDOWN, FAILED, UNKNOWN).              | AIDCF-003          | Context        |
| 14    | CapacityAssertion      | A conditioned claim about a capacity value: metric, unit, subject, operating state, environment, duration, derating, evidence date and confidence. | AIDCF-003     | 5              |
| 15    | Threat                 | An actor-driven or intentional source of potential harm (for example unauthorised remote command of a cooling controller).                  | AIDCF-004          | 7              |
| 16    | Hazard                 | A non-intentional source of potential harm (for example utility voltage sag, coolant leak, heatwave, battery thermal runaway).              | AIDCF-004          | 7              |
| 17    | FailureMode            | The manner in which an entity fails to perform its function (for example pump seizure, breaker failure to trip, optic degradation).         | AIDCF-004          | 7              |
| 18    | FailureScenario        | An ordered path from initiating source through propagation steps and safeguards to residual state and outcome effect, from a stated pre-state. | AIDCF-004       | 7              |
| 19    | Safeguard              | A real-world measure that prevents, detects, contains, corrects or recovers from a failure, threat or hazard.                               | AIDCF-004          | 8              |
| 20    | ControlDomain          | One of the 15 AIDCF-007A control domains.                                                                                                   | AIDCF-007A         | 9              |
| 21    | ControlFamily          | One of the 90 AIDCF-007A control families (six per domain).                                                                                 | AIDCF-007A         | 9              |
| 22    | Control                | One of the 360 AIDCF-007A normative controls: objective, requirement, criteria, evidence profile, procedure and gate mappings.              | AIDCF-007A         | 9              |
| 23    | EvidenceRequirement    | The evidence a control or gate needs for a claim type: classes, quality and sufficiency floors, state and period coverage, independence.   | AIDCF-008          | 10             |
| 24    | EvidenceObject         | A record or observation, with provenance and integrity, used to support, challenge or qualify an assertion.                                 | AIDCF-008          | 11             |
| 25    | EvidencePackage        | A sealed, manifest-listed set of EvidenceObjects collected for an assessment or gate, with custody and integrity metadata.                  | AIDCF-008          | 11             |
| 26    | AssuranceProgram       | The programme within which assessments are planned and decisions issued: assurance level target, profile, cadence and authority.            | AIDCF-011          | 1              |
| 27    | Assessment             | One bounded assessment answering one decision question for one CapabilityInstance, scope and ArchitectureSnapshot.                          | AIDCF-009          | 1, 12          |
| 28    | AssessmentProcedure    | The ordered method steps used to assess one control for one claim type, using canonical assessment methods.                                 | AIDCF-009          | 12             |
| 29    | Sample                 | A defined selection of population items examined by a procedure, with population, selection method and size rationale.                     | AIDCF-009          | 12             |
| 30    | TestRecord             | The record of an authorised test or scenario exercise: authority, preconditions, safety controls, steps, observations and outcome.          | AIDCF-009          | 12             |
| 31    | ControlAssessment      | The result of assessing one control, for one claim type, in one scope: result code, confidence, evidence, method, assessor and lifecycle.   | AIDCF-009          | 12             |
| 32    | Finding                | A documented deficiency against a stated criterion, with condition, cause, consequence, evidence and gate and score effect.                 | AIDCF-009          | 13             |
| 33    | UnknownRecord          | A material fact that cannot be determined, with type (U1–U10), severity (US1–US5), reason, decision effect, evidence needed and owner.      | AIDCF-008          | 13             |
| 34    | CriticalGate           | One of the 15 non-compensating critical gates CG-01 to CG-15, with scope, criteria and evidence floor.                                      | AIDCF-010          | 14             |
| 35    | GateResult             | The evaluated status of one CriticalGate in one assessment scope (PASS, FAIL, UNKNOWN, APPROVED_NA, NOT_ASSESSED) with its inputs.          | AIDCF-010          | 14             |
| 36    | ScoreSnapshot          | An immutable, reproducible computation of control, family and domain scores, coverage and band from pinned inputs and profile.              | AIDCF-010          | 15             |
| 37    | DecisionRecommendation | The decision state, conditions, ceilings and limitations proposed from gate results, UNKNOWNs and scores, before authority review.         | AIDCF-010          | 15             |
| 38    | ReviewRecord           | A recorded human review or approval: reviewer, authority, independence, scope reviewed, outcome and date.                                   | AIDCF-009          | 16             |
| 39    | AssuranceDecision      | The decision of the accountable authority: decision state, conditions, scope, validity period and lifecycle.                               | AIDCF-010          | 16             |
| 40    | AssuranceStatement     | The bounded, disclosed wording of an AssuranceDecision for a named audience, which cannot exceed the decision.                             | AIDCF-012          | Loop           |
| 41    | AssuranceReport        | The issued report carrying statements, scope, findings, UNKNOWNs, limitations, distribution and validity.                                  | AIDCF-012          | Loop           |
| 42    | Action                 | A remediation, evidence-collection or condition-fulfilment task with owner, due date and closure criteria.                                 | AIDCF-011          | Loop           |
| 43    | ReassessmentTrigger    | A declared rule describing which events or conditions require reassessment of which records.                                               | AIDCF-011          | Loop           |
| 44    | Event                  | An observed or reported occurrence (change, incident, test failure, evidence expiry) ingested for impact analysis.                         | AIDCF-014          | Loop           |
| 45    | IntegrationHandoff     | A reviewed exchange of identity or findings between AIDCF and the AI Trust Graph, preserving each framework's ownership.                    | AIDCF-005          | Context        |
| 46    | ValidationResult       | The outcome of a structural, semantic or business-rule validation of a record or package against a pinned release.                         | AIDCF-014          | Context        |
| 47    | MigrationRecord        | The record of converting data between versions or vocabularies: source, target, rule, mapping, exceptions and validation.                  | AIDCF-014          | Context        |
| 48    | DistributionControl    | The classification-bound disclosure rule for a record, edge, package or report: permitted audiences, purpose, redaction and expiry.        | AIDCF-014          | Context        |

**Reference classes.** Relationship ranges in §9 also use three AIDCF-003 classes that are not among the 48 canonical assurance classes: **Location** (site, building, hall, room, row, rack position or logical placement), **PartyEntity** (organisation, role, actor or team) and **Component** (a constituent part of an asset represented where material). They are imported from the AIDCF-003 module of the ontology and are referenced, not redefined, here.

# 8 Common object envelope

**TDS-REQ-037** Every record of every class in §7 shall carry the envelope below. A field marked "Mandatory" shall be present and non-empty; a field marked "Conditional" shall be present when its condition holds, and otherwise may be omitted. A mandatory value that cannot be supplied shall be null with a `nullReason` (§13).

| **Field**           | **Type**                                 | **Obligation**                         | **Meaning**                                                                                         |
|---------------------|------------------------------------------|----------------------------------------|-----------------------------------------------------------------------------------------------------|
| id                  | identifier (§5)                          | Mandatory                              | Stable identity of the record.                                                                      |
| type                | class name (§7)                          | Mandatory                              | Discriminator; exactly one canonical class or registered extension class.                           |
| semanticOwner       | artifact public ID                       | Mandatory                              | Artifact that owns the meaning of this record's class.                                              |
| version             | semantic version string                  | Mandatory                              | Version of this record (§27).                                                                       |
| status              | lifecycle code (§11A.1)                   | Mandatory                              | Record lifecycle.                                                                                   |
| releaseRef          | releaseId                                | Mandatory                              | ReleaseManifest against which the record is valid.                                                  |
| sourceArtifact      | artifact public ID                       | Mandatory for registry-derived records | Artifact the record was derived from.                                                               |
| sourceRecord        | typed reference                          | Conditional: derived or imported       | Originating record in a source system (CMDB, EPMS historian, ticketing).                            |
| name                | string                                   | Mandatory                              | Human-readable name.                                                                                |
| description         | string                                   | Conditional: class profile requires it | Definition or narrative.                                                                            |
| scope               | scope object                             | Mandatory for assessable classes       | CapabilityInstance, boundary and ArchitectureSnapshot the record applies to.                        |
| effectiveFrom       | ISO 8601 date-time                       | Mandatory                              | Start of validity.                                                                                  |
| effectiveTo         | ISO 8601 date-time                       | Conditional: time-bounded records      | End of validity (evidence expiry, decision validity).                                               |
| createdAt, createdBy | date-time, party reference              | Mandatory                              | Creation provenance.                                                                                |
| modifiedAt, modifiedBy | date-time, party reference            | Mandatory once modified                | Last modification provenance.                                                                       |
| classification      | classification code (§11A.8)              | Mandatory                              | Sensitivity of the record.                                                                          |
| distributionControlRef | DistributionControl reference         | Conditional: classification above INTERNAL | Disclosure rule.                                                                                |
| provenance          | provenance object (§26)                  | Mandatory                              | Source system, method, transformation version, hash.                                                |
| reviewState         | assertion code (§11A.2)                   | Mandatory for assertion-bearing classes | CANDIDATE until reviewed.                                                                         |
| supersedes          | list of identifiers                      | Conditional: replaces earlier record   | Records this one supersedes.                                                                        |
| externalIdentifiers | list of (scheme, value)                  | Optional                               | Typed external keys (§5).                                                                           |
| extensions          | object keyed by registered namespace     | Optional                               | Extension properties (§33).                                                                         |

# 8A Object profiles

**TDS-REQ-038** In addition to the envelope, records of the classes below shall carry the profile fields listed. Each field shall hold a value, an approved NOT_APPLICABLE with rationale, or a reference to an UnknownRecord; an empty field is invalid.

## Capability profile (CapabilityInstance)

| **Field**            | **Content**                                                                                                     |
|----------------------|-----------------------------------------------------------------------------------------------------------------|
| owner                | PartyEntity accountable for the capability.                                                                     |
| lifecycle            | Lifecycle stage (PLAN, DESIGN, BUILD, COMMISSION, OPERATE, CHANGE, DECOMMISSION).                               |
| workload             | Workload classes served (training, fine-tuning, inference, data processing) and their characteristics.         |
| architectureBaseline | Current approved ArchitectureSnapshot.                                                                          |
| outcomeIds           | ServiceOutcomes (via HAS_OUTCOME).                                                                              |
| criticality          | Criticality classification per AIDCF-007A CAP-03.                                                               |
| boundary             | Inclusions, exclusions and external providers.                                                                  |
| demandProfile        | Baseline, peak and transient demand, growth forecast (AIDCF-007A CAP-04).                                       |
| operatingEnvelope    | Load, environmental, duration and state-specific limits (AIDCF-007A CAP-05).                                    |

## Architecture profile (ArchitectureSnapshot)

| **Field**    | **Content**                                                                        |
|--------------|------------------------------------------------------------------------------------|
| capabilityId | CapabilityInstance the snapshot describes.                                         |
| systems, assets, interfaces, resources | Member records (via COMPOSED_OF).                        |
| dependencies, faultDomains | Dependency and FaultDomain records in scope.                         |
| states       | OperatingStates represented and their transition rules.                            |
| assertions   | CapacityAssertions and independence assertions.                                    |
| asBuiltReconciliation | Reference to the reconciliation evidence between design and observed state. |
| validation   | ValidationResults for the snapshot.                                                |

## Dependency profile

| **Field**        | **Content**                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------|
| sourceId, targetId | Consumer and provider entities.                                                                                |
| dependencyType   | ELECTRICAL, THERMAL, FLUID, NETWORK, CONTROL, TIMING, IDENTITY, CONFIGURATION, DATA, HUMAN, SUPPLIER, UTILITY, RECOVERY. |
| strength         | ABSOLUTE, MATERIAL, CONDITIONAL, SUPPORTING, RECOVERY_ONLY, UNKNOWN (AIDCF-003).                                 |
| direction        | Effect direction from provider to consumer.                                                                      |
| conditions       | OperatingStates in which the reliance is material.                                                               |
| criticality      | Effect on ServiceOutcome if lost.                                                                                |
| substitutability | Alternatives and time to substitute.                                                                             |
| sharedMode       | FaultDomain reference where the provider is shared.                                                              |
| evidenceRefs, confidence | Evidence and confidence (CONF-0 to CONF-4).                                                              |

## FailureScenario profile

| **Field**        | **Content**                                                                       |
|------------------|-----------------------------------------------------------------------------------|
| preState         | OperatingState and configuration before initiation.                               |
| initiatingSource | Threat, Hazard or FailureMode (via INITIATES).                                    |
| steps            | Ordered PROPAGATES_TO edges with timing.                                          |
| safeguards       | Safeguards expected to act at each step (via PROTECTED_BY).                       |
| residualState    | State after safeguards act or fail.                                               |
| outcomeEffects   | Effect on each ServiceOutcome against tolerance.                                  |
| evidenceRefs, confidence | Analysis or test evidence and confidence.                                 |

## Safeguard profile

| **Field**        | **Content**                                                                     |
|------------------|---------------------------------------------------------------------------------|
| function         | PREVENT, DETECT, CONTAIN, CORRECT or RECOVER.                                   |
| protectedSubject | Entity or outcome protected (inverse of PROTECTED_BY).                          |
| activation       | Automatic, manual or hybrid; trigger and time to act.                           |
| authority        | PartyEntity or control system authorised to activate.                          |
| dependencies     | What the safeguard itself depends on (power, control, network, people).         |
| stateCoverage    | OperatingStates in which it is effective.                                       |
| failureModes     | How the safeguard itself can fail.                                              |
| controlRefs      | Controls that govern it (GOVERNED_BY).                                          |

## Control profile

| **Field**           | **Content**                                                                                                        |
|---------------------|--------------------------------------------------------------------------------------------------------------------|
| domainId, familyId  | Canonical codes.                                                                                                   |
| objective, requirement, assessmentCriteria | As in the AIDCF-007A registry.                                                            |
| applicability       | When the control applies and does not.                                                                             |
| assessmentMethods   | Canonical method codes.                                                                                            |
| claimType, requiredAssuranceLevel | Primary claim type and AL2–AL5.                                                                      |
| evidenceProfile     | EvidenceRequirement reference (HAS_EVIDENCE_REQUIREMENT).                                                          |
| gateMappings        | List of (gateId, role) with role CRITICAL or SUPPORTING (EVALUATES_GATE).                                          |

## Evidence profile (EvidenceObject)

| **Field**     | **Content**                                                                    |
|---------------|--------------------------------------------------------------------------------|
| evidenceClass | E1 to E7.                                                                      |
| source, collector, custodian | Provenance and custody.                                         |
| assertionRefs | Assertions supported, challenged or qualified.                                 |
| period, state | Observation period and OperatingStates covered.                                |
| integrity     | Integrity level I0 to I5 and digest.                                           |
| qualityVector | P, F, C, R, T, I ratings 0 to 5; quality band Q0 to Q5.                        |
| sufficiency   | Sufficiency S0 to S5 for the assertion concerned.                              |
| restrictions  | DistributionControl reference.                                                 |

## Assessment profile

| **Field**        | **Content**                                                                        |
|------------------|------------------------------------------------------------------------------------|
| programId        | AssuranceProgram.                                                                  |
| decisionQuestion | The question the assessment answers.                                               |
| capabilityId, scope | CapabilityInstance, ServiceOutcomes, boundary, ArchitectureSnapshot, states.    |
| profile          | Capability profile, parameter set and weighting (if any).                          |
| team             | Assessors and specialists, with independence declarations.                        |
| evidenceManifest | EvidencePackage references.                                                        |
| results, gates   | ControlAssessments and GateResults (COMPOSED_OF).                                  |
| review           | ReviewRecords.                                                                     |

## Finding profile

| **Field**      | **Content**                                                                       |
|----------------|-----------------------------------------------------------------------------------|
| criterionRef   | Control and criterion (or gate criterion) not met.                                |
| condition, cause, consequence | What was found, why, and its effect on outcomes.                   |
| evidenceRefs   | Evidence of the condition.                                                        |
| classification | Finding class (finding-classes registry).                                         |
| gateEffect, scoreEffect | Effect on GateResults and ScoreSnapshot.                                 |
| owner, status  | Accountable owner and lifecycle.                                                  |

## UNKNOWN profile (UnknownRecord)

| **Field**        | **Content**                                                                  |
|------------------|------------------------------------------------------------------------------|
| subjectRef       | Record or attribute that is unknown.                                         |
| unknownType      | U1 to U10 (AIDCF-008).                                                       |
| severity         | US1 to US5 (canonical specification §5.7).                                   |
| reason           | Why it cannot be determined.                                                 |
| decisionEffect   | Ceiling or gate effect implied by the severity.                              |
| evidenceNeeded   | Evidence that would resolve it.                                              |
| owner, trigger, status | Owner, resolution trigger and lifecycle.                               |

## GateResult profile

| **Field**      | **Content**                                                                         |
|----------------|-------------------------------------------------------------------------------------|
| gateId         | CG-01 to CG-15.                                                                     |
| applicability  | In scope, or APPROVED_NA with boundary rationale and approver.                      |
| criticalInputs | ControlAssessments of CRITICAL controls and their results.                          |
| supportingInputs | ControlAssessments of SUPPORTING controls; gate-level evaluation for each NONCONFORMING. |
| criteria       | Gate criteria evaluated and outcome.                                                |
| evidenceRefs   | Gate evidence and achieved sufficiency against the floor.                           |
| stateCoverage  | OperatingStates covered.                                                            |
| findings, unknowns | Linked Findings and UnknownRecords.                                             |
| result         | Gate result code (§11A.4).                                                           |
| decisionEffect | Ceiling applied to the decision (AIDCF-010).                                        |

## Score profile (ScoreSnapshot)

| **Field**      | **Content**                                                                                  |
|----------------|----------------------------------------------------------------------------------------------|
| subjectRef     | Assessment and scope.                                                                        |
| profileVersion | Scoring profile and weighting version.                                                       |
| inputs         | Pinned ControlAssessment versions.                                                           |
| values         | Control score values (100, 50, 0; UNKNOWN excluded) and family/domain means.                 |
| coverage       | Scored / (in-scope − NOT_APPLICABLE), per family and domain.                                 |
| band           | B1 to B5, or "Band withheld (coverage/UNKNOWN)".                                             |
| unknownOverlay | UNKNOWN counts by severity.                                                                  |

## Decision profile (AssuranceDecision)

| **Field**         | **Content**                                                                       |
|-------------------|-----------------------------------------------------------------------------------|
| question, subjectRef, scope | Decision question, CapabilityInstance and scope.                        |
| recommendationRef | DecisionRecommendation (RECOMMENDS).                                              |
| gateResults, unknowns, scores | Inputs, referenced directly.                                          |
| conditions        | Conditions and limitations, each with owner and due date.                         |
| decisionState     | Decision state (§11A.5).                                                           |
| lifecycle         | Decision lifecycle (§11A.6).                                                       |
| authority         | ReviewRecord of the approving authority (APPROVED_BY).                            |
| validity          | effectiveFrom and effectiveTo; reassessment triggers.                             |

## Report profile (AssuranceReport)

| **Field**      | **Content**                                                               |
|----------------|---------------------------------------------------------------------------|
| reportClass    | Report type (report-types registry, AIDCF-012).                           |
| programRef, assessmentRef, decisionRef | Lineage.                                          |
| issuer, users, intendedUse | Issuer, intended users and permitted use.                     |
| statements     | AssuranceStatements (REPORTED_IN).                                        |
| validity, approvals | Validity period and ReviewRecords.                                   |

## Event profile

| **Field**          | **Content**                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| eventType          | Event type code (§21).                                                      |
| subjectRef, source | Affected entity and reporting source with its health.                       |
| observedAt, effectiveAt | When observed and when it took effect.                                  |
| payload            | Type-specific content, schema-versioned.                                    |
| severity, materiality | Assessed significance (candidate until reviewed).                       |
| triggerRule        | Matched ReassessmentTrigger.                                                |
| affectedAssertions | Records identified by impact analysis (§22).                                |
| reviewState        | Human disposition state.                                                    |

# 9 Relationship registry

**TDS-REQ-039** The 41 relationship types below are the canonical relationship vocabulary of AIDCF. Every edge in an AIDCF graph shall use one of them (or a registered extension, §33), shall respect the stated domain and range, and shall be validated against the stated cardinality.

Conventions:

- **Domain** is the class of the edge's source; **range** is the class of its target. "Architecture element" means InfrastructureSystem, AssetInstance, Interface or Resource.
- **Cardinality** is written *out* / *in*: *out* is the number of edges of this type that each source instance may have; *in* is the number each target instance may have. Unless otherwise stated, cardinality is evaluated within one ArchitectureSnapshot or one Assessment.
- **Inverse** names the inverse property defined in the ontology for query and navigation. Inverses are derived, never asserted separately, so that an edge is stored once.
- All edges carry the relationship envelope (§10).

| **#** | **Type**                 | **Definition**                                                                                                                                   | **Domain**                                                                 | **Range**                                                                  | **Cardinality (out / in)** | **Inverse**          |
|-------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------|----------------------|
| 1     | HAS_OUTCOME              | The capability instance is required to achieve the target service outcome.                                                                       | CapabilityInstance                                                         | ServiceOutcome                                                             | 1..* / 1..1                | outcomeOf            |
| 2     | REQUIRES_FUNCTION        | Achieving the outcome requires the target function to be delivered.                                                                              | ServiceOutcome                                                             | RequiredFunction                                                           | 1..* / 1..*                | functionRequiredBy   |
| 3     | IMPLEMENTED_BY           | The function, or the safeguard, is realised by the target architecture element.                                                                  | RequiredFunction, Safeguard                                                | InfrastructureSystem, AssetInstance, Interface                             | 1..* / 0..*                | implements           |
| 4     | COMPOSED_OF              | Whole-part structure: the source contains the target as a constituent. Acyclic.                                                                  | ArchitectureSnapshot, InfrastructureSystem, AssetInstance, ControlDomain, ControlFamily, AssuranceProgram, Assessment, EvidencePackage | InfrastructureSystem, AssetInstance, Component, Interface, Resource, ControlFamily, Control, Assessment, ControlAssessment, GateResult, Sample, TestRecord, EvidenceObject | 0..* / 0..* (ControlFamily in 1..1 from ControlDomain; Control in 1..1 from ControlFamily) | partOf |
| 5     | CONNECTS_TO              | The source is an endpoint of the target interface. Physical or logical connection only; implies no dependency, causality or reachability.        | InfrastructureSystem, AssetInstance                                        | Interface                                                                  | 0..* / 2..*                | hasEndpoint          |
| 6     | CONSUMES_RESOURCE        | The source draws on the target constrained resource (power, cooling, water, fuel, space, accelerator capacity).                                  | RequiredFunction, InfrastructureSystem, AssetInstance                      | Resource                                                                   | 0..* / 0..*                | consumedBy           |
| 7     | DEPENDS_ON               | The source relies on the target to perform its function; each edge references exactly one Dependency record carrying type, strength and states. AIDCF-003 specialised predicates (POWERED_BY, COOLED_BY, SUPPLIED_BY, AUTHENTICATED_BY, TIMED_BY, CONFIGURED_BY, MAINTAINED_BY) are DEPENDS_ON with the corresponding dependencyType. | RequiredFunction, Safeguard, architecture element | Architecture element, Safeguard, PartyEntity                     | 0..* / 0..*                | dependencyOf         |
| 8     | SHARES_FAULT_DOMAIN_WITH | Source and target are members of the same FaultDomain and can fail together from its common cause. Symmetric; each edge references the FaultDomain record. | Architecture element, Safeguard                                         | Architecture element, Safeguard                                            | 0..* / 0..*                | (symmetric)          |
| 9     | LOCATED_IN               | The source is physically or logically placed in the target location.                                                                             | InfrastructureSystem, AssetInstance, FaultDomain                           | Location                                                                   | 0..1 / 0..*                | locationOf           |
| 10    | OPERATED_BY              | The target party holds operational responsibility for the source.                                                                                | CapabilityInstance, InfrastructureSystem, AssetInstance, Safeguard         | PartyEntity                                                                | 1..* / 0..*                | operates             |
| 11    | CONTROLLED_BY            | The target control system or actor can command the source's state or setpoints (for example a CDU controlled by a BMS, a node controlled by a cluster manager via BMC). | InfrastructureSystem, AssetInstance                    | InfrastructureSystem, AssetInstance, PartyEntity                           | 0..* / 0..*                | controls             |
| 12    | MONITORED_BY             | The target observes the source and is relied on to detect its condition.                                                                         | Architecture element, Safeguard, Dependency                                | InfrastructureSystem, AssetInstance                                        | 0..* / 0..*                | monitors             |
| 13    | PROTECTED_BY             | The target safeguard acts to prevent, detect, contain, correct or recover from failure of, or harm to, the source.                               | ServiceOutcome, RequiredFunction, architecture element                     | Safeguard                                                                  | 0..* / 1..*                | protects             |
| 14    | EXPOSED_TO               | The source is credibly susceptible to the target threat, hazard or failure mode.                                                                 | CapabilityInstance, architecture element, Safeguard                        | Threat, Hazard, FailureMode                                                | 0..* / 0..*                | exposes              |
| 15    | INITIATES                | The threat, hazard or failure mode is the initiating source of the target scenario.                                                              | Threat, Hazard, FailureMode                                                | FailureScenario                                                            | 0..* / 1..*                | initiatedBy          |
| 16    | PROPAGATES_TO            | Within a named scenario, failure of the source causes failure or degradation of the target; carries scenarioRef and step ordinal.                | Architecture element, RequiredFunction                                     | Architecture element, RequiredFunction, ServiceOutcome                     | 0..* / 0..*                | propagatedFrom       |
| 17    | RECOVERS_THROUGH         | The source is restored to tolerance by means of the target recovery path, alternate capacity or recovery safeguard.                              | ServiceOutcome, RequiredFunction, architecture element                     | Architecture element, Safeguard                                            | 0..* / 0..*                | recoveryPathFor      |
| 18    | GOVERNED_BY              | The source is subject to the requirements, method or disclosure rule of the target.                                                              | Safeguard, ControlAssessment, Assessment, any record (for DistributionControl) | Control, AssessmentProcedure, AssuranceProgram, DistributionControl    | 0..* / 0..* (Assessment out 1..1 to AssuranceProgram) | governs  |
| 19    | HAS_EVIDENCE_REQUIREMENT | The control or gate requires the target evidence requirement for a stated claim type.                                                            | Control, CriticalGate                                                      | EvidenceRequirement                                                        | 1..* / 1..1                | requirementOf        |
| 20    | EVIDENCED_BY             | The source is offered the target evidence. Records that evidence was presented, not that it is sufficient.                                      | EvidenceRequirement, CapacityAssertion, Dependency, FaultDomain, ControlAssessment, GateResult, Finding | EvidenceObject, EvidencePackage                  | 0..* / 0..*                | evidences            |
| 21    | SUPPORTS                 | After review, the source evidence corroborates the target claim.                                                                                 | EvidenceObject                                                             | CapacityAssertion, Dependency, FaultDomain, ControlAssessment, GateResult, FailureScenario | 0..* / 0..*        | supportedBy          |
| 22    | CHALLENGES               | The source contradicts or undermines the target claim (defeater). Alias: DISPUTES.                                                              | EvidenceObject, Finding, UnknownRecord, ReviewRecord, BaselineIssue        | Any assertion-bearing record                                               | 0..* / 0..*                | challengedBy         |
| 23    | QUALIFIES                | The source limits the scope, states or conditions under which the target claim holds, without contradicting it.                                | EvidenceObject, ReviewRecord, UnknownRecord                                | Any assertion-bearing record                                               | 0..* / 0..*                | qualifiedBy          |
| 24    | ASSESSED_BY              | The control is assessed, for one claim type in one scope, by the target control assessment.                                                     | Control                                                                    | ControlAssessment                                                          | 0..* / 1..1                | assesses             |
| 25    | RESULTS_IN               | Execution of the procedure, sample or test produced (contributes to) the target control assessment.                                             | AssessmentProcedure, Sample, TestRecord                                    | ControlAssessment                                                          | 0..* / 1..*                | resultOf             |
| 26    | HAS_FINDING              | The source result or gate evaluation records the target finding.                                                                                | ControlAssessment, GateResult, Assessment                                  | Finding                                                                    | 0..* / 1..*                | findingOf            |
| 27    | HAS_UNKNOWN              | The source has a material undetermined fact recorded by the target UNKNOWN record.                                                               | Any record                                                                 | UnknownRecord                                                              | 0..* / 1..*                | unknownOf            |
| 28    | EVALUATES_GATE           | Control to CriticalGate: registry gate mapping, mandatory attribute gateRole (CRITICAL or SUPPORTING). ControlAssessment to GateResult: the result is an input to that gate evaluation. GateResult to CriticalGate: the result evaluates that gate. | Control, ControlAssessment, GateResult      | CriticalGate, GateResult                                                   | Control 0..* ; GateResult out 1..1 / CriticalGate in 0..* | evaluatedBy |
| 29    | CONSTRAINS               | The source imposes a ceiling, condition, limitation or band withholding on the target. Attribute constraintType: CEILING, CONDITION, LIMITATION, BAND_WITHHELD, GATE_EFFECT. Aliases: CONSTRAINS_GATE, LIMITS_DECISION. | GateResult, UnknownRecord, Finding | GateResult, ScoreSnapshot, DecisionRecommendation, AssuranceDecision, AssuranceStatement | 0..* / 0..* | constrainedBy |
| 30    | SUMMARISED_BY            | The source results are aggregated into the target score snapshot or recommendation.                                                              | ControlAssessment, GateResult, ScoreSnapshot, UnknownRecord                | ScoreSnapshot, DecisionRecommendation                                      | 0..* / 1..*                | summarises           |
| 31    | RECOMMENDS               | The recommendation proposes the decision state and conditions taken up (or departed from, with reasons) by the target decision.                 | DecisionRecommendation                                                     | AssuranceDecision                                                          | 0..1 / 1..1                | recommendedBy        |
| 32    | REVIEWED_BY              | The source record has been reviewed in the target review record.                                                                                 | Any record                                                                 | ReviewRecord                                                               | 0..* / 1..*                | reviews              |
| 33    | APPROVED_BY              | The source record has been approved by the authority recorded in the target review record (reviewType APPROVAL).                                | AssuranceDecision, AssuranceStatement, AssuranceReport, ReleaseManifest, MigrationRecord, ArchitectureSnapshot, BaselineIssue resolution, Control (registry release) | ReviewRecord | 0..* / 1..* (AssuranceDecision out 1..*) | approves |
| 34    | REPORTED_IN              | The source is disclosed in the target report.                                                                                                    | AssuranceDecision, AssuranceStatement, Finding, UnknownRecord, GateResult, ScoreSnapshot | AssuranceReport                                         | 0..* / 0..*                | reports              |
| 35    | REQUIRES_ACTION          | The source requires the target action to be completed (remediation, evidence collection, decision condition).                                   | Finding, UnknownRecord, AssuranceDecision, BaselineIssue                   | Action                                                                     | 0..* / 1..*                | actionFor            |
| 36    | CLOSED_BY                | The source is closed by the target closure evidence, reassessment result or review.                                                              | Finding, UnknownRecord, Action, BaselineIssue                              | ReviewRecord, EvidenceObject, ControlAssessment, MigrationRecord           | 0..* / 0..*                | closes               |
| 37    | INVALIDATED_BY           | The source can no longer be relied on because of the target event (evidence expiry, configuration drift, incident, test failure).               | EvidenceObject, CapacityAssertion, ControlAssessment, GateResult, ScoreSnapshot, AssuranceDecision, AssuranceStatement | Event                                      | 0..* / 0..*                | invalidates          |
| 38    | TRIGGERS_REASSESSMENT    | The source event or trigger rule requires reassessment of the target.                                                                            | Event, ReassessmentTrigger                                                 | Control, ControlAssessment, GateResult, Assessment, AssuranceDecision, ServiceOutcome | 0..* / 0..*     | reassessmentTriggeredBy |
| 39    | SUPERSEDES               | The source replaces the target record of the same class; the target is retained with status SUPERSEDED. Acyclic.                                 | Any record                                                                 | Record of the same class                                                   | 0..* / 0..1                | supersededBy         |
| 40    | MIGRATED_FROM            | The source was produced from the target (prior version, legacy vocabulary or legacy record) by the migration recorded in migrationRef.          | Any record                                                                 | Any record                                                                 | 0..* / 0..*                | migratedTo           |
| 41    | INTEGRATION_HANDOFF      | The source AIDCF record is exchanged with the AI Trust Graph through the target reviewed handoff record (AIDCF-005).                             | Any canonical record                                                       | IntegrationHandoff                                                         | 0..* / 1..*                | handoffOf            |

## 9.1 Legacy relationship aliases

**TDS-REQ-040** Legacy relationship names shall be accepted only on input and shall be migrated by a MigrationRecord to the canonical type, reversing direction where stated. They shall not be emitted.

| **Legacy name**   | **Canonical type** | **Direction change**                                                                                                     |
|-------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| SUPPORTS_OUTCOME  | IMPLEMENTED_BY     | Reverse: "System SUPPORTS_OUTCOME Function" becomes "Function IMPLEMENTED_BY System". Outcome links use HAS_OUTCOME and REQUIRES_FUNCTION. |
| IMPLEMENTS        | IMPLEMENTED_BY     | Reverse.                                                                                                                 |
| CONSTRAINS_GATE   | CONSTRAINS         | None; constraintType GATE_EFFECT.                                                                                        |
| LIMITS_DECISION   | CONSTRAINS         | None; constraintType CEILING or LIMITATION.                                                                              |
| PROTECTS          | PROTECTED_BY       | Reverse.                                                                                                                 |
| DISPUTES          | CHALLENGES         | None.                                                                                                                    |
| EVALUATES         | ASSESSED_BY        | Reverse ("ControlAssessment EVALUATES Control" becomes "Control ASSESSED_BY ControlAssessment").                        |
| TESTED_BY         | EVIDENCED_BY       | None; target is a TestRecord-derived EvidenceObject.                                                                     |
| RECOVERED_BY      | RECOVERS_THROUGH   | None.                                                                                                                    |

# 10 Relationship envelope

**TDS-REQ-041** Every edge shall be a first-class record carrying the fields below. Edges without a relationshipId, type, sourceId and targetId are invalid.

| **Field**      | **Rule**                                                                                                        |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| relationshipId | Stable identifier; edges are versioned like records.                                                            |
| type           | One of the 41 types or a registered extension.                                                                  |
| sourceId, targetId | Identifiers whose classes satisfy the domain and range in §9.                                               |
| semanticOwner  | Owner artifact of the relationship type.                                                                        |
| scope          | ArchitectureSnapshot or Assessment within which the edge is asserted.                                           |
| conditions     | OperatingStates and other conditions under which the edge holds (mandatory for DEPENDS_ON, PROTECTED_BY, PROPAGATES_TO, RECOVERS_THROUGH). |
| qualifiers     | Type-specific attributes: dependencyRef, faultDomainRef, scenarioRef and step, gateRole, constraintType, migrationRef. |
| effectiveFrom, effectiveTo | Validity interval.                                                                                  |
| sourceRecord   | Originating record in a source system, where imported.                                                          |
| evidenceRefs   | Evidence for the edge itself (for example independence evidence for the absence of a shared fault domain).     |
| confidence     | CONF-0 to CONF-4, with CONFLICTING and STALE flags.                                                             |
| reviewState    | CANDIDATE until reviewed (§11A.2).                                                                               |
| classification | Classification code.                                                                                            |
| version, supersedes | Version and superseded edge identifiers.                                                                   |

# 11 End-to-end traceability

**TDS-REQ-042** A conformant dataset at T2 or above shall evaluate every rule below for every in-scope record and shall report each failure as a ValidationResult. A traceability gap that cannot be closed by data shall be represented as an UnknownRecord on the source record; it shall not be ignored.

| **Rule** | **From → to**                        | **Test**                                                                                                                                         | **Chain steps** |
|----------|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| TR-01    | Capability → Outcome                 | Every CapabilityInstance has ≥1 HAS_OUTCOME; every ServiceOutcome has exactly one incoming HAS_OUTCOME.                                          | 2→3             |
| TR-02    | Outcome → Function                   | Every ServiceOutcome has ≥1 REQUIRES_FUNCTION.                                                                                                   | 3→4             |
| TR-03    | Function → Architecture              | Every RequiredFunction has ≥1 IMPLEMENTED_BY to an element in the current ArchitectureSnapshot.                                                  | 4→5             |
| TR-04    | Architecture → Dependency            | Every element implementing a RequiredFunction has its DEPENDS_ON edges recorded, or an UnknownRecord stating that dependency discovery is incomplete. | 5→6         |
| TR-05    | Dependency → Failure                 | Every Dependency of strength ABSOLUTE or MATERIAL, and every FaultDomain containing redundant elements, is covered by ≥1 FailureScenario.        | 6→7             |
| TR-06    | Failure → Safeguard                  | Every FailureScenario whose outcome effect exceeds tolerance identifies the Safeguards expected to act (PROTECTED_BY on the affected elements).  | 7→8             |
| TR-07    | Safeguard → Control                  | Every Safeguard relied on in a scenario is GOVERNED_BY ≥1 Control.                                                                               | 8→9             |
| TR-08    | Control → Evidence Requirement       | Every in-scope Control has HAS_EVIDENCE_REQUIREMENT for its claim type.                                                                          | 9→10            |
| TR-09    | Requirement → Evidence or UNKNOWN    | Every EvidenceRequirement in scope has EVIDENCED_BY ≥1 EvidenceObject meeting its floors, or HAS_UNKNOWN.                                        | 10→11           |
| TR-10    | Procedure → Result                   | Every ControlAssessment has ≥1 RESULTS_IN from a procedure, sample or test, names its method codes and assessor, and is REVIEWED_BY.              | 11→12           |
| TR-11    | Result → Finding or UNKNOWN          | Every PARTIAL or NONCONFORMING result has HAS_FINDING; every UNKNOWN result has HAS_UNKNOWN.                                                     | 12→13           |
| TR-12    | Gate → Evidence, Findings, UNKNOWN   | Every GateResult has EVALUATES_GATE to its CriticalGate, links the ControlAssessments of all in-scope CRITICAL controls, and links its evidence, Findings and UnknownRecords. | 13→14 |
| TR-13    | Score → immutable inputs and profile | Every ScoreSnapshot references pinned input versions and profile version, and recomputation from them yields the same values.                    | 12→15           |
| TR-14    | Recommendation → constraints         | Every DecisionRecommendation links all GateResults and every US3–US5 UnknownRecord in scope and applies their CONSTRAINS edges.                  | 14→15           |
| TR-15    | Decision → authority, scope, validity | Every AssuranceDecision has RECOMMENDS incoming, APPROVED_BY a ReviewRecord of the declared authority, a scope and effectiveTo.                  | 15→16           |
| TR-16    | Report → approved decision           | Every AssuranceStatement and AssuranceReport traces to an AssuranceDecision whose lifecycle is APPROVED or ACTIVE, and does not exceed it.       | 16→Loop         |
| TR-17    | Trigger → impacted objects           | Every Event matched to a ReassessmentTrigger yields TRIGGERS_REASSESSMENT or INVALIDATED_BY edges to all dependent records found by §22.          | Loop→2          |
| TR-18    | Supersession → prior and successor   | Every SUPERSEDED record has exactly one supersededBy and the chain is acyclic.                                                                   | All             |

# 11A Controlled vocabularies

**TDS-REQ-043** The codes in this section and in the canonical specification are the only codes that conformant implementations shall emit. Codes are published as CSV files under `registries/vocabularies/` (one file per vocabulary) and listed in the ReleaseManifest.

**TDS-REQ-044** Legacy codes shall be accepted only on input, shall be converted by a MigrationRecord using the alias tables below, and the original code shall be preserved in provenance.

Vocabularies defined elsewhere and used unchanged: claim types and assurance levels AL0–AL6 (AIDCF-011 and the canonical specification §5.1), confidence CONF-0 to CONF-4 (AIDCF-008), evidence classes E1–E7, quality dimensions, bands Q0–Q5, sufficiency S0–S5, integrity I0–I5, profile tiers CP-1 to CP-5 and evidence-system conformance EC0–EC5 (AIDCF-008), UNKNOWN types U1–U10 (AIDCF-008) and severities US1–US5, assessment methods, control types, lifecycle stages and score bands B1–B5 (AIDCF-009, AIDCF-010).

## 11A.1 Record lifecycle

Applies to the `status` field of every record (not to decision state).

| **Code**   | **Meaning**                                                          |
|------------|----------------------------------------------------------------------|
| DRAFT      | Being prepared; not for use in assessment.                           |
| CANDIDATE  | Proposed (often by automation); awaiting review.                     |
| REVIEWED   | Reviewed; not yet approved.                                          |
| APPROVED   | Approved by the accountable authority.                               |
| ACTIVE     | Approved and in use.                                                 |
| SUSPENDED  | Temporarily not to be relied on, pending reassessment.               |
| WITHDRAWN  | Removed from use before expiry; retained for history.                |
| SUPERSEDED | Replaced by a newer record (SUPERSEDES).                             |
| RETIRED    | End of life without replacement; retained for history.               |

## 11A.2 Assertion review state

| **Code**    | **Meaning**                                                         |
|-------------|---------------------------------------------------------------------|
| CANDIDATE   | Asserted but not reviewed.                                          |
| SUPPORTED   | Reviewed; supported by evidence meeting the applicable floor.       |
| CHALLENGED  | Subject to an unresolved CHALLENGES edge.                           |
| QUALIFIED   | Holds only under the conditions stated by QUALIFIES edges.          |
| CONFLICTING | Supported and challenged by evidence of comparable quality.         |
| UNKNOWN     | Cannot be determined; HAS_UNKNOWN is mandatory.                     |
| SUPERSEDED  | Replaced by a newer assertion.                                      |

## 11A.3 Control result (ControlAssessment.result)

| **Code**       | **Meaning**                                                                          | **Score value**                                   |
|----------------|--------------------------------------------------------------------------------------|---------------------------------------------------|
| CONFORMING     | All assessment criteria met for the claim type; evidence at or above the profile floor. | 100                                            |
| PARTIAL        | Some criteria met; specific deficiencies recorded as Findings.                        | 50                                                |
| NONCONFORMING  | Criteria materially not met, or a safeguard demonstrated ineffective.                 | 0                                                 |
| UNKNOWN        | Result cannot be determined (evidence below floor, conflict, inaccessible).           | None; excluded from mean; counted in coverage and the UNKNOWN register |
| NOT_APPLICABLE | Approved non-applicability with rationale and approver.                              | Excluded                                          |
| NOT_ASSESSED   | In scope but not yet assessed.                                                        | Excluded; counted as coverage gap                 |

Legacy alias table:

| **Legacy code**                         | **Canonical code** | **Condition**                                                                                         |
|-----------------------------------------|--------------------|-------------------------------------------------------------------------------------------------------|
| NOT_IMPLEMENTED                         | NONCONFORMING      | None.                                                                                                 |
| INEFFECTIVE                             | NONCONFORMING      | None.                                                                                                 |
| IMPLEMENTED                             | CONFORMING         | Valid only for DESIGN or IMPLEMENTATION claims; for any other claim type the migrated result is UNKNOWN. |
| OPERATING_EFFECTIVELY, STRONGLY_EFFECTIVE | CONFORMING       | For OPERATION or EFFECTIVENESS claims.                                                                |
| N/A                                     | NOT_APPLICABLE     | Rationale and approver must exist, otherwise the migrated result is UNKNOWN.                         |
| Not Assessed                            | NOT_ASSESSED       | None.                                                                                                 |
| SUSPENDED                               | UNKNOWN            | Record lifecycle of the ControlAssessment set to SUSPENDED.                                          |

Implementation maturity IM0 to IM5 (AIDCF-017) is a diagnostic attribute and is never a result code.

## 11A.4 Gate result (GateResult.result)

| **Code**     | **Meaning**                                                                                        |
|--------------|----------------------------------------------------------------------------------------------------|
| PASS         | All CRITICAL controls CONFORMING at required claim type, gate criteria met, evidence at floor, SUPPORTING nonconformities evaluated. |
| FAIL         | Any in-scope CRITICAL control NONCONFORMING or PARTIAL, or a gate criterion demonstrated not met. |
| UNKNOWN      | Not FAIL, and any CRITICAL control UNKNOWN or NOT_ASSESSED, gate evidence below floor, or a US4 UNKNOWN attached. |
| APPROVED_NA  | Gate out of scope with approved boundary rationale.                                                |
| NOT_ASSESSED | Gate in scope but not yet evaluated.                                                               |

There is no conditional gate result; conditions exist only at decision level. Legacy spelling `APPROVED_N/A` is an input alias of APPROVED_NA.

## 11A.5 Decision state (AssuranceDecision.decisionState)

| **Code**              | **Meaning (rules in AIDCF-010)**                                                             |
|-----------------------|----------------------------------------------------------------------------------------------|
| REASONABLY_ASSURED    | All applicable gates PASS; no US3–US5 UNKNOWN open; scores and coverage support the claim.  |
| CONDITIONALLY_ASSURED | Gates PASS; specified conditions with owners and dates must be met for the claim to hold.   |
| LIMITED               | Assurance holds only for a reduced scope, set of outcomes or states, stated explicitly.     |
| NOT_ASSURED           | Evidence shows the claim does not hold (for example a gate FAIL that defeats it).           |
| INCONCLUSIVE          | The claim cannot be decided (for example US5 UNKNOWN or gate UNKNOWN beyond ceiling).       |

Legacy alias table:

| **Legacy code**                                                   | **Canonical code**    |
|-------------------------------------------------------------------|-----------------------|
| ADVERSE, ADVERSE_NOT_ASSURED, "Adverse / Not assured"             | NOT_ASSURED           |
| UNKNOWN, UNKNOWN_INCONCLUSIVE, UNKNOWN_OR_INCONCLUSIVE, Withheld  | INCONCLUSIVE          |
| CONDITIONAL                                                       | CONDITIONALLY_ASSURED |
| SUSPENDED, WITHDRAWN, SUPERSEDED (formerly listed as states)       | Decision lifecycle codes (§11A.6); decision state unchanged |
| NOT ASSESSED                                                      | Not a decision state; no AssuranceDecision is issued |

## 11A.6 Decision lifecycle (AssuranceDecision.lifecycle)

| **Code**    | **Meaning**                                                         |
|-------------|---------------------------------------------------------------------|
| DRAFT       | Being prepared.                                                     |
| RECOMMENDED | DecisionRecommendation complete; awaiting authority.                |
| APPROVED    | Approved by the authority; not yet effective.                       |
| ACTIVE      | In effect within its validity period.                               |
| SUSPENDED   | Not to be relied on pending reassessment after a triggering event.  |
| WITHDRAWN   | Revoked by the authority.                                           |
| SUPERSEDED  | Replaced by a newer decision.                                       |
| EXPIRED     | Validity period ended without renewal.                              |

## 11A.7 Operating state

Owner AIDCF-003 §45.

| **Code**    | **Meaning**                                                                                      |
|-------------|--------------------------------------------------------------------------------------------------|
| NORMAL      | Approved architecture operates within declared envelope; no material planned impairment.         |
| DEGRADED    | One or more functions, safeguards, paths or reserves are impaired while some capability remains. |
| MAINTENANCE | A planned intervention changes availability, configuration, staffing or safeguards.              |
| EMERGENCY   | Exceptional condition requiring urgent protective action.                                        |
| RECOVERY    | Controlled restoration and validation after disruption.                                          |
| TRANSITION  | Movement between architectures, states, locations or control regimes.                            |
| SHUTDOWN    | Intentional cessation with controlled residual dependencies.                                     |
| FAILED      | Required function is not delivered.                                                              |
| UNKNOWN     | Current operating state cannot be determined.                                                    |

## 11A.8 Classification

| **Code**          | **Meaning**                                                                                       |
|-------------------|---------------------------------------------------------------------------------------------------|
| PUBLIC            | Approved for public release.                                                                      |
| INTERNAL          | For the owning organisation and its assessors.                                                    |
| CLIENT_RESTRICTED | For named client parties under agreement.                                                         |
| CONFIDENTIAL      | Need-to-know within named roles; disclosure would cause commercial or security harm.              |
| HIGHLY_RESTRICTED | Exploitable detail (for example OT access paths, protection settings); named individuals only.    |

# 12 Serialisation architecture

**TDS-REQ-045** AIDCF-016 is the normative serialisation companion to this standard. It defines the schema and ontology package (JSON Schema, JSON-LD context, OWL ontology, SHACL shapes, CSV layouts) that realises §7 to §11A. Conformant implementations shall serialise AIDCF data as defined in AIDCF-016 for the release pinned in the ReleaseManifest.

| **Format**                 | **Role**                                                      | **Authority**                                     |
|----------------------------|---------------------------------------------------------------|---------------------------------------------------|
| JSON                       | Application exchange of records and edges                     | Authoritative record form                         |
| JSON Schema 2020-12        | Structural validation                                         | Normative (AIDCF-016)                             |
| JSON-LD 1.1                | Mapping of JSON keys to `aidcf:` IRIs                          | Normative (AIDCF-016)                             |
| RDF (Turtle)               | Graph exchange                                                | Equivalent projection of JSON records             |
| OWL 2                      | Class, property, domain, range and inverse declarations       | Normative (AIDCF-016)                             |
| SHACL                      | Closed-world cardinality and business-rule validation         | Normative (AIDCF-016)                             |
| CSV                        | Registries and controlled vocabularies                        | Normative for codes                               |
| NDJSON                     | Event streams                                                 | Exchange only                                     |
| Parquet or similar columnar | Analytics                                                    | Non-authoritative                                 |

# 13 JSON design rules

**TDS-REQ-046** JSON records shall comply with every rule below; AIDCF-016 schemas enforce them.

| **Rule**                   | **Requirement**                                                                                                     |
|----------------------------|---------------------------------------------------------------------------------------------------------------------|
| Encoding                   | UTF-8 without byte-order mark.                                                                                      |
| Naming                     | Property names in lowerCamelCase; class names in UpperCamelCase; codes in UPPER_SNAKE_CASE.                         |
| Dates and times            | ISO 8601 with explicit UTC offset; durations as ISO 8601 durations.                                                 |
| Explicit null reason       | A null value is permitted only with a sibling `nullReason` (NOT_APPLICABLE with rationale reference, or UNKNOWN with UnknownRecord reference). |
| Enumerated codes           | Every coded field is an enum bound to a vocabulary file version.                                                    |
| Stable schema identifiers  | Each schema has a versioned `$id`; records declare the schema version they conform to.                              |
| additionalProperties false | Every object schema sets `additionalProperties: false`. Extension data is permitted only under `extensions` (§33). |
| Namespaced extensions      | Keys under `extensions` are registered namespace prefixes.                                                          |
| Discriminator              | Every record carries `type`; polymorphic references carry the target type.                                          |
| Stable references          | References are identifiers, never array positions or display names.                                                 |
| Integrity metadata         | Records exported in packages carry a digest; packages carry a manifest of digests.                                  |
| Classification             | Every record carries `classification`.                                                                              |
| Units                      | Quantities carry value and unit; units are taken from a declared unit vocabulary (SI and derived units).            |

# 14 Semantic graph rules

| **Requirement**         | **Rule**                                                                                                                       |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **TDS-REQ-047**        | JSON-LD contexts shall use protected term definitions so that an imported context cannot redefine AIDCF terms.                 |
| **TDS-REQ-048**         | The `aidcf:` prefix shall resolve to `https://w3id.org/aidcf/ontology#`; instance IRIs follow the AIDCF-016 pattern.            |
| **TDS-REQ-049**           | AIDCF and AI Trust Graph terms shall be held in separate contexts and named graphs; mixing is permitted only through IntegrationHandoff records. |
| **TDS-REQ-050**         | OWL classes and properties shall mirror §7 and §9 exactly, including declared inverses and symmetric properties.               |
| **TDS-REQ-051**        | OWL or rule-based inference shall not produce APPROVED, SUPPORTED, CONFORMING, PASS or any decision state; inferred triples are held in a separate named graph with reviewState CANDIDATE. |
| **TDS-REQ-052**          | Cardinality, mandatory-link and vocabulary constraints shall be validated with SHACL under closed-world assumptions, not inferred under OWL open-world semantics. |
| **TDS-REQ-053**         | Ontology imports shall be pinned by version IRI.                                                                                |
| **TDS-REQ-054**         | Deprecated terms shall remain declared with `owl:deprecated true` and a pointer to their replacement.                         |

# 15 JSON Schema package

The schema package is defined, versioned and published by AIDCF-016. The logical coverage it must provide is listed below; AIDCF-016 may split or combine files provided coverage is complete.

**TDS-REQ-055** The AIDCF-016 schema package shall provide schemas covering, at minimum: release manifest; common envelope and relationship envelope; capability, outcome and function; architecture snapshot, system, asset, interface, resource and capacity assertion; dependency and fault domain; threat, hazard, failure mode and failure scenario; safeguard; control domain, family and control; evidence requirement, object and package; assurance programme, assessment, procedure, sample and test record; control assessment, finding and UNKNOWN record; critical gate and gate result; score snapshot; decision recommendation, review record and assurance decision; assurance statement and report; action, reassessment trigger and event; integration handoff; validation result, migration record, baseline issue and distribution control.

AIDCF-016 v1.0 publishes the MDM 1.3 schema set in `schemas/json-schema/`: `definitions.schema.json`, `common-envelope.schema.json` and one closed JSON Schema 2020-12 file per class (58 classes: the 48 canonical classes of §7, the 3 reference classes, 6 supporting classes pending registration and the auxiliary RelationshipRecord). The set is generated from `schemas/tools/aidcf_model.py` by `schemas/tools/build_schemas.py`, whose `--check` mode fails if a published file differs from the generated one. The earlier v1.2 subset (control assessment, evidence, gate, score, decision) is superseded. Its only copies are those released with the AIDCF-015 v1.2 package under `implementation/aidcf-015-v1.2/schemas/`. They are kept unchanged for that package, and data validated against them is migrated to MDM 1.3 under §27.

# 16 Semantic publication package

**TDS-REQ-056** AIDCF-016 shall publish, for each release, a JSON-LD context, an OWL ontology with version IRI, a Turtle serialisation, SHACL shapes, the registry and vocabulary CSV files, example instance data, and the conformance-test fixtures, each listed with its digest in the ReleaseManifest. File names and versions are defined by AIDCF-016.

The current release, MDM 1.3 (AIDCF-016 v1.0), publishes the JSON-LD context `schemas/jsonld/aidcf-context-1.3.jsonld`, the OWL ontology with SKOS concept schemes `schemas/owl/aidcf-core-1.3.ttl` (Turtle; version IRI `https://w3id.org/aidcf/ontology/1.3`) and the SHACL shapes `schemas/shacl/aidcf-shapes-1.3.ttl`. The registries and vocabularies are the CSV files under `registries/`, and the example data and conformance fixtures are in the AIDCF-015 v1.3 package (`implementation/aidcf-015-v1.3/`). w3id registration is pending, so the IRIs do not yet resolve. The v1.2 files (`aidcf-context-v1.2.jsonld`, `aidcf-core-v1.2.ttl`, `aidcf-shapes-v1.2.ttl`) are superseded and are no longer under `schemas/`. They survive only in `implementation/aidcf-015-v1.2/semantic/`, unchanged as released with that package.

# 17 Registry catalogue

**TDS-REQ-057** Every registry CSV shall carry the common columns `code`, `label`, `definition`, `semanticOwner`, `version`, `status` and `replacedBy`, plus the registry-specific columns below.

| **Registry file**          | **Registry-specific columns**                                                                         | **Owner**  |
|----------------------------|--------------------------------------------------------------------------------------------------------|------------|
| artifacts.csv              | publicId, shortCode, title, path, artifactVersion, artifactStatus                                      | AIDCF-014  |
| object-types.csv           | chainStep, ownerArtifact, schemaRef                                                                    | AIDCF-014  |
| relationship-types.csv     | domain, range, cardinalityOut, cardinalityIn, inverse, symmetric, qualifiers                           | AIDCF-014  |
| vocabularies/*.csv         | vocabulary, sortOrder, scoreValue (where applicable), legacyAliases                                    | Per §11A    |
| domains.csv                | familyCount, controlCount                                                                              | AIDCF-007A |
| control-families.csv       | domainCode, familyNumber, controlRange                                                                 | AIDCF-007A |
| controls.csv               | familyId, claimType, requiredAssuranceLevel, controlType, gateMappings (gateId:role list), amendmentRef | AIDCF-007A |
| critical-gates.csv         | name, scope, evidenceFloor, criticalControlCount                                                       | AIDCF-010  |
| evidence-classes.csv       | classCode, examples                                                                                    | AIDCF-008  |
| evidence-quality.csv       | dimension, level, criterion                                                                            | AIDCF-008  |
| assessment-methods.csv     | methodCode, typicalEvidenceClasses, safetyConstraint                                                   | AIDCF-009  |
| finding-classes.csv        | severity, gateEffect                                                                                   | AIDCF-009  |
| unknown-types.csv          | typeCode (U1–U10), defaultSeverityTest                                                                 | AIDCF-008  |
| unknown-severity.csv       | severityCode (US1–US5), test, decisionEffect                                                           | AIDCF-010  |
| decision-states.csv        | rank, ceilingRule                                                                                      | AIDCF-010  |
| report-types.csv           | audience, mandatorySections                                                                            | AIDCF-012  |
| architecture-patterns.csv  | patternCode, mandatoryViews, typicalGates                                                              | AIDCF-013  |
| external-mappings.csv      | externalScheme, externalCode, aidcfCode, mappingType, crosswalkRef                                     | AIDCF-019  |
| deprecated-terms.csv       | deprecatedTerm, canonicalTerm, directionChange, effectiveRelease                                       | AIDCF-014  |
| migration-rules.csv        | sourceVersion, targetVersion, rule, condition, fallback                                                | AIDCF-014  |

**Implementation status.** `registries/catalogue/registry-index.csv` lists the twenty registries above with their published path, owner, row count, sources, whether the common columns are present, and the columns still missing. The index is computed from the published file headers. `registries/tools/build_catalogue.py` generates fifteen of the registries in `registries/catalogue/` with the full common and registry-specific columns: artifacts, object types, relationship types, evidence classes, evidence quality, assessment methods, finding classes, UNKNOWN types, UNKNOWN severity, decision states, report types, architecture patterns, external mappings, deprecated terms and migration rules. The tool's `--check` mode fails if regenerating would change any file. Where no source artifact defines a value, the cell is left empty rather than inferred. Examples are AIDCF-013 pattern codes, finding-class severity, typical evidence classes per assessment method, report-type definitions and effective releases of deprecated terms.

The UNKNOWN-severity entry above was listed in earlier drafts as `unknown-severities.csv`. It is now named `unknown-severity.csv`, the vocabulary file name. The catalogue file of that name is a projection of `registries/vocabularies/unknown-severity.csv`, and if the two differ the vocabulary file governs. The same holds for the catalogue projections of evidence classes, UNKNOWN types, decision states and assessment methods.

TDS-REQ-057 is not yet met in full. The domains, control-families, controls and critical-gates registries and the 25 vocabulary files are maintained by other tools, and they do not yet carry all of the common columns. For example, they use `domainId`, `familyId`, `controlId`, `gateId` or `name` in place of `code` and `label`, and they have no `semanticOwner` or `replacedBy`. Their registry status `PROPOSED` is also outside the §11A.1 record lifecycle. The missing columns of each are listed in `registry-index.csv`. A registry is conformant only when its index row shows no missing columns.

**TDS-REQ-058** The controls registry shall contain exactly 360 rows, 24 per domain and four per family; the families registry exactly 90 rows; the domains registry exactly 15 rows. Any deviation is a BLOCKED BaselineIssue.

# 18 Business rules

**TDS-REQ-059** Implementations claiming T5 or above shall enforce the business rules below and shall reject or flag (as stated) records that violate them.

| **Rule** | **Statement**                                                                                                                                                                                 | **On violation** |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| BR-001   | A ControlAssessment shall identify its control, claim type, scope subject and the applicability basis for that subject.                                                                     | Reject           |
| BR-002   | NOT_APPLICABLE requires a rationale and an approving ReviewRecord. Missing evidence yields UNKNOWN, never NOT_APPLICABLE.                                                                    | Reject           |
| BR-003   | A CONFORMING result applies only to the claim type assessed; it shall not be presented as conformance for a higher claim type.                                                              | Reject           |
| BR-004   | A GateResult of PASS requires evidence at or above the gate evidence floor and CONFORMING results for every in-scope CRITICAL control.                                                     | Reject           |
| BR-005   | REASONABLY_ASSURED is not permitted while any applicable GateResult is FAIL or UNKNOWN, or any US4/US5 UnknownRecord is open in scope.                                                      | Reject           |
| BR-006   | A ScoreSnapshot shall state coverage and UNKNOWN overlay; a band shall be withheld when coverage < 80% or a US4/US5 UNKNOWN is open in scope. A score never changes a gate.                 | Reject           |
| BR-007   | An AssuranceStatement or AssuranceReport shall not state a decision state, scope, outcome or validity stronger than the AssuranceDecision it reports.                                       | Reject           |
| BR-008   | Closure of a Finding or UnknownRecord requires CLOSED_BY closure evidence or a reassessment result, reviewed by someone other than the action owner where independence is required.        | Reject           |
| BR-009   | Supersession preserves history: superseded records remain retrievable and unchanged.                                                                                                        | Reject           |
| BR-010   | AITG mappings preserve ownership: an IntegrationHandoff shall not change the owner, state or decision of either framework's record.                                                         | Reject           |
| BR-011   | Inferred or automatically generated records and edges remain CANDIDATE until reviewed and shall not be inputs to an approved decision.                                                     | Flag and exclude |
| BR-012   | Export of a record classified CONFIDENTIAL or HIGHLY_RESTRICTED requires a DistributionControl authorising the recipient and purpose.                                                       | Block export     |
| BR-013   | An Event classified as material change shall trigger impact analysis (§22) before any dependent decision is renewed.                                                                        | Flag             |
| BR-014   | Risk acceptance is recorded as a decision condition or limitation; it shall not change a control result or gate result.                                                                    | Reject           |
| BR-015   | Reuse of an EvidenceObject for a different assertion, scope or period requires a fresh SUPPORTS/QUALIFIES review for that assertion.                                                       | Flag             |

# 19 Canonical queries

**TDS-REQ-060** Implementations claiming T4 or above shall be able to answer the queries below against a pinned snapshot, returning record identifiers and versions.

| **Query** | **Question answered**                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------|
| Q01       | Which systems, assets and dependencies implement the functions required by Capability X?                   |
| Q02       | Which failure scenarios and fault domains can defeat Outcome Y, and in which operating states?             |
| Q03       | For Control C, what evidence, results and findings exist, by claim type and scope?                         |
| Q04       | For EvidenceObject E, which assertions does it support or challenge, and which decisions depend on it?     |
| Q05       | For Gate G, which criteria, CRITICAL controls, evidence and UNKNOWNs determine its result, and what ceiling follows? |
| Q06       | For Decision D, which gates, UNKNOWNs, scores, conditions and approvals produced it?                       |
| Q07       | Is every statement in Report R consistent with its decision (BR-007)?                                      |
| Q08       | Which records are affected by Event V (§22)?                                                               |
| Q09       | Which providers are single points of concentration or common modes across outcomes?                       |
| Q10       | What succeeds snapshot S, and by which migration?                                                          |
| Q11       | Which candidate records await review, by age and materiality?                                              |
| Q12       | Which sensitive paths are visible to disclosure profile P?                                                 |

# 20 Event model

**TDS-REQ-061** Every Event shall carry: eventId, eventType (§21), source and sourceHealth, subjectRef, observedAt, effectiveAt, payload with schemaVersion, severity and materiality (candidate values until reviewed), affectedAssertions (from §22), candidateTriggers, humanDisposition (ReviewRecord), resultingDecisionEffect, the ArchitectureSnapshot in force, and supersession links where an event corrects an earlier one.

**TDS-REQ-062** Events shall not change any approved record directly. An Event can only create candidate INVALIDATED_BY and TRIGGERS_REASSESSMENT edges and propose lifecycle changes, which take effect on human disposition.

# 21 Event types

| **Event type**              | **Typical source**                                     | **Typical candidate effect**                                                    |
|-----------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------|
| ARCHITECTURE_CHANGED        | Change management, design repository                   | New ArchitectureSnapshot required; dependent ControlAssessments flagged.        |
| CAPACITY_THRESHOLD_BREACHED | EPMS, BMS, CDU telemetry, scheduler                    | CapacityAssertion INVALIDATED_BY; CG-05/CG-06 reassessment candidate.           |
| CONFIGURATION_CHANGED       | Configuration management, controller audit logs        | Implementation-claim results for affected controls flagged.                     |
| PROVIDER_CHANGED            | Contract or supplier management                        | Dependency and CG-03 reassessment candidate.                                    |
| SOURCE_UNAVAILABLE          | Evidence connector health                              | Evidence currency reduced; potential UNKNOWN.                                   |
| EVIDENCE_EXPIRED            | Evidence repository                                    | EvidenceObject INVALIDATED_BY; dependent results flagged.                       |
| EVIDENCE_CONFLICT           | Validation engine, assessor                            | CHALLENGES edge candidate; assertion state CONFLICTING.                         |
| INCIDENT_DETECTED           | Incident management                                    | Scenario and safeguard results flagged; decision suspension candidate.          |
| TEST_FAILED                 | Test records, commissioning, exercises                 | Effectiveness or resilience results NONCONFORMING candidate.                    |
| GATE_STATUS_CHANGED         | Gate engine                                            | DecisionRecommendation recomputation.                                           |
| FINDING_CLOSED              | Action tracking                                        | Closure review (BR-008).                                                        |
| CONTROL_DRIFT               | Continuous control monitoring                          | Operation-claim results flagged.                                                |
| DEPENDENCY_DRIFT            | Discovery, CMDB reconciliation                         | Dependency records flagged; CG-03 reassessment candidate.                       |
| DECISION_SUSPENDED          | Decision authority                                     | Dependent statements and reports flagged for withdrawal or annotation.          |
| REPORT_WITHDRAWN            | Report issuer                                          | Distribution recipients notified.                                               |

# 22 Change-impact contract

**TDS-REQ-063** Impact analysis of an Event shall execute the steps below in order, recording each step's output in a ValidationResult linked to the Event.

1. Validate the event against its schema and source health; reject or mark UNKNOWN if invalid.
2. Resolve the subject identity and the ArchitectureSnapshot in force at effectiveAt.
3. Traverse DEPENDS_ON, COMPOSED_OF, IMPLEMENTED_BY, PROTECTED_BY, SHARES_FAULT_DOMAIN_WITH and EVIDENCED_BY edges from the subject to identify affected assertions.
4. Identify affected Controls, FailureScenarios, GateResults and ServiceOutcomes.
5. Recompute candidate coverage, scores and gate results on a copy; never on approved records.
6. Apply candidate decision ceilings from §11A and AIDCF-010.
7. Route the analysis to the record owners and the decision authority for review.
8. Record the approved disposition in a ReviewRecord.
9. Create a superseding snapshot or records where the disposition requires change.
10. Notify owners of affected statements and reports, and record the notifications.

# 23 API and exchange

**TDS-REQ-064** An implementation exposing an exchange interface shall provide: versioned media types bound to the schema version; idempotent writes keyed by client request identifier; optimistic concurrency on record version; immutable published snapshots; pagination and filtering by class, scope, status and classification; bulk validation and dry-run modes that never persist; explicit machine-readable errors referencing the violated requirement or business rule; classification-aware access control; an append-only audit log; and no destructive overwrite of any record version.

# 24 Semantic operations

| **Operation**           | **Behaviour**                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------------|
| validateRecord          | Validate one record against schema, shapes and business rules; return ValidationResult.           |
| validatePackage         | Validate an exchange bundle (§29) including manifest digests.                                     |
| resolveIdentifier       | Return the current and historical versions of an identifier and any reviewed shared identities.   |
| getLineage              | Return the inputs and provenance of a derived record.                                             |
| getTraceabilityPath     | Return the TR-01 to TR-18 path between two records, with gaps.                                    |
| getImpactAnalysis       | Execute §22 in dry-run mode.                                                                      |
| createCandidateRecord   | Create a record with reviewState CANDIDATE.                                                       |
| submitForReview         | Route a candidate to its owner.                                                                   |
| approveRecord           | Record a ReviewRecord of type APPROVAL by an authorised person; never callable by automation alone. |
| supersedeRecord         | Create a successor and mark the predecessor SUPERSEDED.                                            |
| publishSnapshot         | Freeze and digest an ArchitectureSnapshot or assessment snapshot.                                 |
| exportDisclosurePackage | Export records permitted by a DistributionControl, with redaction applied.                       |
| ingestEvent             | Accept an Event and start §22.                                                                     |
| getConformanceResult    | Return the latest ValidationResult set for the conformance suite.                                 |

# 25 Security, privacy and disclosure

**TDS-REQ-065** Classification shall be enforced at record, attribute and edge level. An edge inherits at least the higher classification of its two endpoints.

**TDS-REQ-066** Records and edges describing access paths to OT, BMS, EPMS, CDU, BMC/out-of-band or fabric-controller interfaces, protection settings, or security weaknesses shall be classified CONFIDENTIAL or HIGHLY_RESTRICTED and released only under a DistributionControl that names the purpose and recipients.

**TDS-REQ-067** Credentials, keys, tokens and secrets shall never be stored in AIDCF records or evidence payloads; evidence of their existence or configuration shall be recorded by reference or attestation.

**TDS-REQ-068** Personal data shall be minimised to what is needed for accountability (role, authority, review). Retention shall follow the AIDCF-008 evidence retention rules and applicable law.

**TDS-REQ-069** Records and packages at rest and in transit shall be protected for integrity (digests and signatures per §26) and confidentiality appropriate to their classification. Queries against HIGHLY_RESTRICTED data shall be logged and monitored.

**TDS-REQ-070** Content derived by AI or other automated analysis shall be labelled as such in provenance and shall remain CANDIDATE until reviewed.

**TDS-REQ-071** An integrity or confidentiality breach affecting AIDCF records shall be raised as an Event and shall trigger review of all decisions whose lineage includes the affected records.

# 26 Provenance and integrity

**TDS-REQ-072** The provenance object of every record shall carry: source system and source record; creator and collector; collection method; observation, collection and ingestion timestamps; clock source where timing matters to the assertion; transformation or migration version; SHA-256 digest; signature where the record is part of a published package; custodian and chain-of-custody entries; classification; review and disposition; SUPPORTS and CHALLENGES links; supersession and migration links. The model aligns to the W3C PROV-O concepts of entity, activity and agent.

# 27 Versioning and migration

| **Requirement**  | **Rule**                                                                                                                   |
|------------------|----------------------------------------------------------------------------------------------------------------------------|
| **TDS-REQ-073** | Schemas, ontology, registries and vocabularies shall use semantic versioning: major for breaking changes (removed field, changed meaning, tightened cardinality), minor for additive optional changes, patch for metadata and documentation. |
| **TDS-REQ-074**    | Every major or minor change shall publish migration rules from the previous version, and each migration run shall produce MigrationRecords and ValidationResults. |
| **TDS-REQ-075** | Migration shall not reinterpret meaning automatically; a value without a defined mapping becomes UNKNOWN with a migration reason. |
| **TDS-REQ-076**    | Deprecated terms shall remain resolvable to their replacement through `deprecated-terms.csv` and the ontology.            |
| **TDS-REQ-077**  | Decisions and reports whose lineage includes migrated records shall be revalidated against BR-001 to BR-015 before renewal. |

# 28 Source-artifact binding

**TDS-REQ-078** Each record shall identify its semantic owner by public ID. The binding of content to artifacts is:

| **Artifact** | **Content bound**                                                                 |
|--------------|-----------------------------------------------------------------------------------|
| AIDCF-002    | Core concepts and the canonical assurance chain                                   |
| AIDCF-003    | Infrastructure ontology, taxonomy, operating states, reference classes            |
| AIDCF-004    | Threats, hazards, failure modes, scenarios, safeguards                            |
| AIDCF-005    | AITG integration and IntegrationHandoff                                           |
| AIDCF-006    | Assurance principles                                                              |
| AIDCF-007A   | Control domains, families, controls, gate mappings                                |
| AIDCF-008    | Evidence requirements, objects, quality, sufficiency, UNKNOWN types               |
| AIDCF-009    | Assessments, procedures, samples, tests, control assessments, findings, reviews   |
| AIDCF-010    | Gates, scores, recommendations, decisions                                          |
| AIDCF-011    | Assurance programmes, actions, reassessment triggers, assurance levels            |
| AIDCF-012    | Statements, reports                                                               |
| AIDCF-013    | Reference architecture, architecture snapshots, patterns and views                |
| AIDCF-014    | Manifest, identifiers, relationships, traceability, events, validation, migration |
| AIDCF-016    | Serialisation, schema and ontology package                                        |

# 29 Exchange bundles

**TDS-REQ-079** An exchange bundle shall contain a bundle manifest (bundle type, releaseRef, record list with digests, classification, DistributionControl), the records, and the ValidationResults produced by validatePackage. The bundle types and their minimum record sets are:

| **Bundle**   | **Minimum records**                                                                              |
|--------------|--------------------------------------------------------------------------------------------------|
| Baseline     | ReleaseManifest, registries, vocabularies, open BaselineIssues                                    |
| Architecture | CapabilityInstance, ServiceOutcomes, RequiredFunctions, ArchitectureSnapshot and members, Dependencies, FaultDomains |
| Scenario     | Threats, Hazards, FailureModes, FailureScenarios, Safeguards and their edges                     |
| Control      | Controls in scope, EvidenceRequirements, gate mappings                                            |
| Evidence     | EvidencePackages and EvidenceObjects with custody and integrity                                   |
| Assessment   | Assessment, procedures, samples, test records, ControlAssessments, Findings, UnknownRecords      |
| Decision     | GateResults, ScoreSnapshot, DecisionRecommendation, ReviewRecords, AssuranceDecision              |
| Reporting    | AssuranceStatements, AssuranceReport, DistributionControl                                          |
| Continuing   | Events, ReassessmentTriggers, impact ValidationResults, Actions                                   |
| Integration  | IntegrationHandoffs and the referenced AIDCF records                                              |

# 30 Synthetic dataset

**TDS-REQ-080** The AIDCF-015 synthetic dataset shall exercise every class in §7 and every relationship type in §9 at least once, and shall include: a CapabilityInstance with training and inference outcomes; a training service chain; power, cooling (including liquid cooling), compute, storage and network systems; external utility and provider dependencies; at least one shared fault domain spanning nominally redundant paths; failure scenarios with safeguards; controls with evidence; at least one UNKNOWN of each severity US2 to US5; gate results including at least one FAIL and one UNKNOWN; a score snapshot and decision; reports; a change event with reassessment; and an AITG handoff. All synthetic records shall be labelled as synthetic in provenance and shall not represent any real facility.

# 31 Conformance tests

**TDS-REQ-081** The conformance test suite shall contain, for each test below, positive and negative fixtures, and shall be versioned and listed in the ReleaseManifest.

| **Test** | **Name**              | **What it verifies**                                                                                                  |
|----------|-----------------------|-----------------------------------------------------------------------------------------------------------------------|
| CT-01    | Positive records      | Valid fixtures for every class and relationship type are accepted.                                                     |
| CT-02    | Missing mandatory     | Records missing envelope or profile fields without nullReason are rejected.                                          |
| CT-03    | UNKNOWN handling      | UNKNOWN results are excluded from means, counted in coverage, and severities apply the correct ceilings.            |
| CT-04    | Gate dominance        | A gate FAIL or UNKNOWN blocks REASONABLY_ASSURED irrespective of scores; PARTIAL never yields PASS.                   |
| CT-05    | Score reproducibility | Recomputing a ScoreSnapshot from pinned inputs yields identical values, coverage and band.                            |
| CT-06    | Report consistency    | Statements stronger than the decision are rejected (BR-007).                                                          |
| CT-07    | Supersession          | Superseded records remain retrievable; cycles are rejected.                                                           |
| CT-08    | Migration             | Legacy vocabulary and relationship aliases migrate correctly, with conditional mappings applied and UNKNOWN fallback. |
| CT-09    | Security              | Classified records and edges are excluded from unauthorised exports; inherited edge classification applies.          |
| CT-10    | AITG handoff          | Handoffs preserve ownership and do not alter either framework's decisions.                                           |
| CT-11    | Event impact          | A change event identifies all dependent records and changes nothing without disposition.                              |
| CT-12    | Anti-gaming           | Attempts to reach a stronger decision by re-scoping, reclassifying UNKNOWN as NOT_APPLICABLE, or reusing evidence across claim types are detected. |
| CT-13    | Baseline conflict     | Conflicting counts or identifiers create BLOCKED BaselineIssues.                                                       |
| CT-14    | Performance           | Validation of the reference dataset completes within the time stated in the test-suite profile (illustrative default: under 10 minutes on a single commodity server). |

# 31A Templates

All templates carry the common envelope (§8). The fields below are the template-specific content; the envelope is not repeated.

| **Template**            | **Specific fields**                                                                                                         |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Release Manifest        | As §4.                                                                                                                      |
| Baseline Issue          | conflictingSources (artifact, version, location, value), conflictType, impact, status, provisionalValue, condition, expiry, resolutionRefs |
| Object Registry Entry   | className, definition, ownerArtifact, chainStep, profileFields, schemaRef, shapeRef                                          |
| Relationship Entry      | typeName, definition, domain, range, cardinalityOut, cardinalityIn, inverse, symmetric, qualifiers, aliases                 |
| Traceability Link       | ruleId (TR-NN), fromRef, toRef, pathEdges, result (MET, GAP, UNKNOWN), gapUnknownRef                                       |
| Validation Result       | subjectRef, validator and version, ruleSet, ruleId, outcome (PASS, FAIL, WARNING), message, releaseRef, runAt              |
| Migration Record        | sourceVersion, targetVersion, ruleRefs, inputRefs, outputRefs, unmappedValues, fallbackApplied, validationRefs              |
| Impact Analysis         | eventRef, snapshotRef, traversedEdges, affectedRecords, candidateEffects, reviewRef, disposition                            |
| Disclosure Profile      | audience, purpose, permittedClasses, maxClassification, redactionRules, expiry, approverRef                                |
| Conformance Report      | implementation, level claimed, releaseRef, testSuiteVersion, results per test, exceptions, date, reviewerRef                |
| Integration Handoff     | aidcfRefs, aitgRefs, direction, payload type, ownershipStatement, reviewRef                                                 |
| Source-System Mapping   | sourceSystem, sourceObject, sourceField, targetClass, targetField, transformation, unit, qualityNotes                      |
| Extension Registration  | As §33.                                                                                                                     |
| Schema Change Request   | requestedChange, rationale, affectedClasses, versionImpact (major, minor, patch), migrationPlan, reviewRefs                |

# 32 Data governance roles

| **Role**              | **Accountability**                                                                    |
|-----------------------|---------------------------------------------------------------------------------------|
| Methodology authority | Normative meanings, release approval.                                                 |
| Registry steward      | Codes, registries, vocabularies and alias mappings.                                   |
| Schema maintainer     | AIDCF-016 schemas, context, ontology and shapes.                                      |
| Domain steward        | Domain-specific mappings for one of the 15 domains.                                   |
| Evidence steward      | Evidence semantics and quality rules.                                                 |
| Decision steward      | Gate, score and decision logic.                                                       |
| Security steward      | Classification and disclosure.                                                        |
| AITG steward          | Shared identity and handoffs.                                                         |
| Tool implementer      | Implementation fidelity and audit logging.                                            |
| Independent reviewer  | Challenge of conformance claims.                                                      |
| Release authority     | Publication, manifest signature and migration.                                        |

# 33 Extension governance

**TDS-REQ-082** An extension (class, property, relationship type or code) shall be registered before use with: a namespace prefix distinct from `aidcf:`; an owner; a justification; target classes; proof of no collision with canonical terms; datatype and cardinality; classification; JSON Schema fragment and SHACL shape; examples; tests; approval; and deprecation and migration rules. An extension shall not weaken any canonical rule (§1) and shall not be required to interpret a canonical record.

# 34 Data quality

**TDS-REQ-083** Data quality shall be measured and reported separately from assurance confidence; good data quality does not raise confidence in a claim, and poor data quality is reported as UNKNOWN or ValidationResult failures.

| **Dimension**  | **Measure**                                                                   |
|----------------|-------------------------------------------------------------------------------|
| Completeness   | Mandatory fields and traceability links present (§8, §11).                    |
| Validity       | Values conform to schema and vocabularies.                                    |
| Consistency    | No contradictions between records, versions or sources.                       |
| Uniqueness     | No duplicate identities.                                                      |
| Timeliness     | Records current relative to their effectiveTo and source update frequency.    |
| Accuracy       | Reconciliation to source systems and observed state.                         |
| Lineage        | Provenance complete (§26).                                                    |
| Integrity      | Digests and signatures verify.                                                |
| Reviewability  | Proportion of material records with ReviewRecords.                           |
| Security       | Classification and DistributionControl coverage.                             |

# 35 Reference implementation components

| **Component**          | **Responsibility**                                                                  |
|------------------------|-------------------------------------------------------------------------------------|
| ArtifactRepository     | Stores artifacts and their digests.                                                 |
| RegistryRepository     | Stores registries and vocabularies by version.                                      |
| SchemaRegistry         | Serves the AIDCF-016 package by version.                                            |
| IdentifierService      | Mints, resolves and checks collisions of identifiers.                               |
| IngestionService       | Imports source-system data as candidate records.                                    |
| ValidationEngine       | Runs schema, shape, traceability and business-rule validation.                      |
| TraceabilityGraph      | Holds records and edges with versions and named snapshots.                          |
| EvidenceConnectors     | Collect evidence with provenance and integrity.                                     |
| AssessmentWorkflow     | Supports procedures, sampling, tests and review.                                    |
| GateScoreEngine        | Computes gate results and scores reproducibly.                                      |
| DecisionReviewWorkflow | Routes recommendations to authority and records approvals.                         |
| ReportingService       | Generates statements and reports and checks BR-007.                                 |
| EventImpactService     | Ingests events and runs §22.                                                        |
| DisclosureService      | Applies DistributionControls to exports.                                            |
| AuditLog               | Append-only log of all writes and approvals.                                       |
| ConformanceRunner      | Runs the §31 suite and publishes ValidationResults.                                 |

These are logical components; AIDCF-015 provides a reference implementation.

# 36 Storage projections

**TDS-REQ-084** Any storage projection (graph database, triple store, relational, search index, warehouse, cache) shall: retain the canonical record or a lossless reference to it; preserve edge provenance and version; use named graphs or equivalent for snapshots and inferred data; use stable keys equal to AIDCF identifiers; treat search indexes and caches as non-authoritative; reference evidence blobs by digest rather than copy them into derived stores; and never approve or overwrite canonical records.

# 36A Worked traces

The traces below are illustrative and synthetic.

## 36A.1 Electrical

Outcome "training job availability within tolerance" REQUIRES_FUNCTION "continuous power to accelerator racks"; IMPLEMENTED_BY the rack power train (UPS system, distribution, busway, rack PDUs). The UPS DEPENDS_ON utility and generator (Dependency strength MATERIAL in NORMAL and EMERGENCY). Scenario: a utility voltage sag INITIATES transfer to UPS; PROPAGATES_TO generator start and load step. Safeguards: UPS ride-through, generator load acceptance, load-step management by the cluster power-capping function. Controls MCF-POW-011 (Runtime and Derating) and MCF-POW-020 (Load-Step Response) are ASSESSED_BY ControlAssessments; their ControlAssessments are linked by EVALUATES_GATE to the CG-05 GateResult. If generator load-acceptance test evidence is older than its currency floor, the result is UNKNOWN, HAS_UNKNOWN a US4 record, and CG-05 is UNKNOWN.

## 36A.2 Thermal

Outcome REQUIRES_FUNCTION "remove rack heat at design load". It is IMPLEMENTED_BY the CDU secondary loop and the facility water system. Two nominally redundant CDUs SHARES_FAULT_DOMAIN_WITH each other through a common BMS controller (CONTROLLED_BY). Scenario: controller failure stops both CDU pumps; PROPAGATES_TO accelerator thermal throttling and job failure. Controls MCF-THM-010 (CDU Capacity) and MCF-THM-021 (Control Stability) are linked to CG-06, CG-07 and CG-09. Independence evidence that is absent yields a QUALIFIES edge or an UnknownRecord on the redundancy claim.

## 36A.3 Digital authority

Outcome depends on cooling and power control. The BMS, EPMS and BMC/out-of-band management network are CONTROLLED_BY PartyEntities acting through privileged identities. A remote-support path (SUP-06) CONNECTS_TO the OT gateway. Controls MCF-SEC-005 (BMS and EPMS Security) and MCF-NET-016 (Break-Glass Access) link to CG-07 and CG-15. The access-path records are HIGHLY_RESTRICTED (§25).

## 36A.4 Recovery

Outcome "resume training from checkpoint within recovery tolerance" RECOVERS_THROUGH the checkpoint tier and alternate capacity. The checkpoint tier DEPENDS_ON the storage fabric and the scheduler. Controls MCF-STO-017 (Checkpoint Durability), MCF-STO-019 (Storage Recovery Sequencing) and MCF-RES-016 (Data and Checkpoint Recovery) link to CG-10; the restore exercise TestRecord RESULTS_IN their effectiveness assessments.

## 36A.5 Report lineage

AssuranceDecision (CONDITIONALLY_ASSURED, ACTIVE) is RECOMMENDS-linked from its DecisionRecommendation, CONSTRAINS-linked from a US3 UnknownRecord (condition), APPROVED_BY the authority's ReviewRecord, and REPORTED_IN an AssuranceReport. An EVIDENCE_EXPIRED event later INVALIDATED_BY-links a decisive EvidenceObject; on disposition the decision lifecycle moves to SUSPENDED and the report owner is notified.

# 37 Conformance validation

| **Check**   | **Verification**                                                                     | **Requirements verified**                      |
|-------------|--------------------------------------------------------------------------------------|------------------------------------------------|
| TDS-VAL-001 | ReleaseManifest present, complete, signed and digests verify.                        | TDS-REQ-022, TDS-REQ-023                  |
| TDS-VAL-002 | All source conflicts recorded as BaselineIssues.                                     | TDS-REQ-003, TDS-REQ-035           |
| TDS-VAL-003 | Identifiers stable, unique and pattern-conformant.                                   | TDS-REQ-027, TDS-REQ-030                |
| TDS-VAL-004 | Envelope fields present (owner, source, version, status).                            | TDS-REQ-037                                  |
| TDS-VAL-005 | Edges conform to domain, range and cardinality, or gaps are UNKNOWN.                 | TDS-REQ-039, TDS-REQ-042                     |
| TDS-VAL-006 | NOT_APPLICABLE justified and approved.                                               | TDS-REQ-059                               |
| TDS-VAL-007 | Material assertions evidenced or UNKNOWN.                                            | TDS-REQ-010                                 |
| TDS-VAL-008 | Evidence quality evaluated per claim type.                                           | TDS-REQ-013                                 |
| TDS-VAL-009 | Results link method, subject, evidence and reviewer.                                 | TDS-REQ-042                                   |
| TDS-VAL-010 | Gate PASS has evidence at floor and conforming CRITICAL controls.                    | TDS-REQ-059                               |
| TDS-VAL-011 | Scores reproducible.                                                                 | TDS-REQ-012                                 |
| TDS-VAL-012 | Decision respects gates and UNKNOWN ceilings.                                        | TDS-REQ-059                               |
| TDS-VAL-013 | Reports do not exceed decisions.                                                     | TDS-REQ-059                               |
| TDS-VAL-014 | Events do not auto-approve.                                                          | TDS-REQ-062, TDS-REQ-006              |
| TDS-VAL-015 | History preserved.                                                                   | TDS-REQ-007                             |
| TDS-VAL-016 | Migrations explicit and recorded.                                                    | TDS-REQ-044, TDS-REQ-040, TDS-REQ-074 |
| TDS-VAL-017 | AITG ownership preserved.                                                            | TDS-REQ-018                                 |
| TDS-VAL-018 | Sensitive paths classified and controlled.                                           | TDS-REQ-020, TDS-REQ-066                |
| TDS-VAL-019 | Extensions registered and non-colliding.                                             | TDS-REQ-082                                      |
| TDS-VAL-020 | Conformance tests pass for the claimed level.                                        | TDS-REQ-021, TDS-REQ-081               |

# 38 Review and release gates

All reviews below are pending. No review, pilot or independent conformance assessment of this standard has been completed.

| **Reviewer or pilot**           | **Status** |
|---------------------------------|------------|
| Methodology author              | Pending    |
| Ontology and data architect     | Pending    |
| Control and evidence reviewer   | Pending    |
| Assessment reviewer             | Pending    |
| Scoring and decision reviewer   | Pending    |
| Programme and reporting reviewer | Pending   |
| Reference-architecture reviewer | Pending    |
| JSON Schema reviewer            | Pending    |
| RDF, OWL and SHACL reviewer     | Pending    |
| Security and privacy reviewer   | Pending    |
| AITG reviewer                   | Pending    |
| Synthetic dataset pilot         | Pending    |
| Graph pilot                     | Pending    |
| API and event pilot             | Pending    |
| Independent conformance review  | Pending    |
| Public release                  | Pending    |

## Final doctrine

**AIDCF-014 makes assurance claims reconstructable and testable without giving machines authority they do not possess. Structural validity does not prove truth, engineering adequacy or assurance. Conflict, incomplete lineage and missing evidence remain explicit and prevent stronger conclusions.**
