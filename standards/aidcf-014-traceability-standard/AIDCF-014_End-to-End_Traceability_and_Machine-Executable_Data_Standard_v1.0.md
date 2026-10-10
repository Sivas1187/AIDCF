> Markdown edition (source of truth). PDF: [AIDCF-014_End-to-End_Traceability_and_Machine-Executable_Data_Standard_v1.0.pdf](AIDCF-014_End-to-End_Traceability_and_Machine-Executable_Data_Standard_v1.0.pdf)

**AIDCF**

**AI Data Centre Facilities Assurance Framework**

**END-TO-END TRACEABILITY &  
MACHINE-EXECUTABLE DATA STANDARD**

**Version 1.0**

**  
A canonical information contract for identifiers, lineage, schemas, graphs, validation, exchange, change impact and conformance**

Artifact ID: AIDCF-TDS-001  
Status: Draft for controlled review  
Author: Siva Sethumadhavan  
Depends on: AIDCF-003 through AIDCF-013

# Document control

**Normative requirements.**

| **Element** | **Requirement**                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------|
| Purpose     | Define canonical objects, relationships, IDs, traceability, serialization, validation, security and exchange. |
| Outputs     | Registries, JSON Schema, JSON-LD, RDF/OWL, SHACL, mappings, events, tests and fixtures.                       |
| Authority   | Tools implement declared rules; accountable people approve material facts and decisions.                      |
| Conflict    | Contradictory sources create BaselineIssue records.                                                           |
| Boundary    | Technical conformance is not engineering approval, assurance or certification.                                |

# Executive thesis

**Every material conclusion must be reconstructable from stable identities, approved source versions, explicit relationships, evidence and review. Missing or conflicting data remains UNKNOWN or a validation failure.**

## Canonical chain

**Capability -\> Outcome -\> Function -\> Architecture -\> Dependency/Fault Domain -\> Failure -\> Safeguard -\> Control -\> Evidence Requirement -\> Evidence -\> Assessment -\> Result -\> Finding/UNKNOWN -\> Gate -\> Score -\> Recommendation -\> Decision -\> Report -\> Trigger**

# 1 Authority and precedence

**Normative requirements.**

| **Element**                               | **Requirement** |
|-------------------------------------------|-----------------|
| Semantic owner retained                   | Required        |
| Schemas cannot weaken doctrine            | Required        |
| No silent reconciliation                  | Required        |
| Release manifest pins versions and hashes | Required        |
| Technology neutral                        | Required        |
| Human approval                            | Required        |
| History preserved                         | Required        |
| Validity is not assurance                 | Required        |

# 2 Constitutional invariants

**Normative requirements.**

| **Element**                     | **Requirement** |
|---------------------------------|-----------------|
| Capability/outcomes primary     | Required        |
| Assertions need evidence/review | Required        |
| UNKNOWN first-class             | Required        |
| Gates separate from scores      | Required        |
| Assurance dimensions distinct   | Required        |
| Dependencies visible            | Required        |
| Lineage mandatory               | Required        |
| Change can invalidate           | Required        |
| Automation proposes             | Required        |
| AIDCF/AITG conclusions separate | Required        |
| Connectivity is not causality   | Required        |
| Sensitive paths controlled      | Required        |

# 3 Conformance levels

**Normative requirements.**

| **Element**               | **Requirement** |
|---------------------------|-----------------|
| T0 vocabulary             | Required        |
| T1 records and IDs        | Required        |
| T2 traceability           | Required        |
| T3 JSON validation        | Required        |
| T4 graph validation       | Required        |
| T5 decision-ready         | Required        |
| T6 continuing assurance   | Required        |
| T7 test-suite conformance | Required        |

# 4 Release manifest

**Normative requirements.**

| **Element**          | **Requirement** |
|----------------------|-----------------|
| releaseId            | Required        |
| artifactManifest     | Required        |
| registryVersions     | Required        |
| schemaVersions       | Required        |
| approved cardinality | Required        |
| knownIssues          | Required        |
| migrationSet         | Required        |
| testSuite            | Required        |
| approvals            | Required        |
| integrity signature  | Required        |

# 5 Identifier standard

**Normative requirements.**

| **Element**                      | **Requirement** |
|----------------------------------|-----------------|
| Stable namespace or IRI          | Required        |
| Unique identity                  | Required        |
| Meaning change creates new ID    | Required        |
| Version separate from identity   | Required        |
| Controlled codes                 | Required        |
| Typed external IDs               | Required        |
| Reviewed aliases/shared identity | Required        |
| Candidate IDs non-authoritative  | Required        |
| Collision blocker                | Required        |

# 6 Baseline harmonisation

**Normative requirements.**

| **Element**   | **Requirement**                                                    |
|---------------|--------------------------------------------------------------------|
| BaselineIssue | First-class conflict object                                        |
| Trigger       | Conflicting counts, IDs, titles, definitions, mappings or statuses |
| Status        | BLOCKED or CONDITIONALLY_BASELINED                                 |
| Resolution    | Approved decision, registry update, migration and supersession     |
| Preservation  | Original values and source lineage retained                        |

# 7 Canonical object registry

**Normative requirements.**

| **Element**            | **Requirement**                     |
|------------------------|-------------------------------------|
| ReleaseManifest        | Canonical class with semantic owner |
| BaselineIssue          | Canonical class with semantic owner |
| CapabilityInstance     | Canonical class with semantic owner |
| ServiceOutcome         | Canonical class with semantic owner |
| RequiredFunction       | Canonical class with semantic owner |
| ArchitectureSnapshot   | Canonical class with semantic owner |
| InfrastructureSystem   | Canonical class with semantic owner |
| AssetInstance          | Canonical class with semantic owner |
| Interface              | Canonical class with semantic owner |
| Resource               | Canonical class with semantic owner |
| Dependency             | Canonical class with semantic owner |
| FaultDomain            | Canonical class with semantic owner |
| OperatingState         | Canonical class with semantic owner |
| CapacityAssertion      | Canonical class with semantic owner |
| Threat                 | Canonical class with semantic owner |
| Hazard                 | Canonical class with semantic owner |
| FailureMode            | Canonical class with semantic owner |
| FailureScenario        | Canonical class with semantic owner |
| Safeguard              | Canonical class with semantic owner |
| ControlDomain          | Canonical class with semantic owner |
| ControlFamily          | Canonical class with semantic owner |
| Control                | Canonical class with semantic owner |
| EvidenceRequirement    | Canonical class with semantic owner |
| EvidenceObject         | Canonical class with semantic owner |
| EvidencePackage        | Canonical class with semantic owner |
| AssuranceProgram       | Canonical class with semantic owner |
| Assessment             | Canonical class with semantic owner |
| AssessmentProcedure    | Canonical class with semantic owner |
| Sample                 | Canonical class with semantic owner |
| TestRecord             | Canonical class with semantic owner |
| ControlAssessment      | Canonical class with semantic owner |
| Finding                | Canonical class with semantic owner |
| UnknownRecord          | Canonical class with semantic owner |
| CriticalGate           | Canonical class with semantic owner |
| GateResult             | Canonical class with semantic owner |
| ScoreSnapshot          | Canonical class with semantic owner |
| DecisionRecommendation | Canonical class with semantic owner |
| ReviewRecord           | Canonical class with semantic owner |
| AssuranceDecision      | Canonical class with semantic owner |
| AssuranceStatement     | Canonical class with semantic owner |
| AssuranceReport        | Canonical class with semantic owner |
| Action                 | Canonical class with semantic owner |
| ReassessmentTrigger    | Canonical class with semantic owner |
| Event                  | Canonical class with semantic owner |
| IntegrationHandoff     | Canonical class with semantic owner |
| ValidationResult       | Canonical class with semantic owner |
| MigrationRecord        | Canonical class with semantic owner |
| DistributionControl    | Canonical class with semantic owner |

# 8 Common object envelope

**Normative requirements.**

| **Element**         | **Requirement**               |
|---------------------|-------------------------------|
| id                  | Mandatory unless explicit N/A |
| type                | Mandatory unless explicit N/A |
| semanticOwner       | Mandatory unless explicit N/A |
| version             | Mandatory unless explicit N/A |
| status              | Mandatory unless explicit N/A |
| sourceArtifact      | Mandatory unless explicit N/A |
| sourceRecord        | Mandatory unless explicit N/A |
| name                | Mandatory unless explicit N/A |
| description         | Mandatory unless explicit N/A |
| scope               | Mandatory unless explicit N/A |
| effectiveFrom       | Mandatory unless explicit N/A |
| effectiveTo         | Mandatory unless explicit N/A |
| createdAt           | Mandatory unless explicit N/A |
| createdBy           | Mandatory unless explicit N/A |
| modifiedAt          | Mandatory unless explicit N/A |
| modifiedBy          | Mandatory unless explicit N/A |
| classification      | Mandatory unless explicit N/A |
| provenance          | Mandatory unless explicit N/A |
| reviewState         | Mandatory unless explicit N/A |
| supersedes          | Mandatory unless explicit N/A |
| externalIdentifiers | Mandatory unless explicit N/A |
| extensions          | Mandatory unless explicit N/A |

# Object profile: Capability

**Normative requirements.**

| **Element**          | **Requirement**                  |
|----------------------|----------------------------------|
| owner                | Required or explicit N/A/UNKNOWN |
| lifecycle            | Required or explicit N/A/UNKNOWN |
| workload             | Required or explicit N/A/UNKNOWN |
| architectureBaseline | Required or explicit N/A/UNKNOWN |
| outcomeIds           | Required or explicit N/A/UNKNOWN |
| criticality          | Required or explicit N/A/UNKNOWN |
| boundary             | Required or explicit N/A/UNKNOWN |
| demandProfile        | Required or explicit N/A/UNKNOWN |
| operatingEnvelope    | Required or explicit N/A/UNKNOWN |

# Object profile: Architecture

**Normative requirements.**

| **Element**  | **Requirement**                  |
|--------------|----------------------------------|
| capabilityId | Required or explicit N/A/UNKNOWN |
| systems      | Required or explicit N/A/UNKNOWN |
| assets       | Required or explicit N/A/UNKNOWN |
| interfaces   | Required or explicit N/A/UNKNOWN |
| resources    | Required or explicit N/A/UNKNOWN |
| dependencies | Required or explicit N/A/UNKNOWN |
| faultDomains | Required or explicit N/A/UNKNOWN |
| states       | Required or explicit N/A/UNKNOWN |
| assertions   | Required or explicit N/A/UNKNOWN |
| validation   | Required or explicit N/A/UNKNOWN |

# Object profile: Dependency

**Normative requirements.**

| **Element**      | **Requirement**                  |
|------------------|----------------------------------|
| sourceId         | Required or explicit N/A/UNKNOWN |
| targetId         | Required or explicit N/A/UNKNOWN |
| dependencyType   | Required or explicit N/A/UNKNOWN |
| direction        | Required or explicit N/A/UNKNOWN |
| conditions       | Required or explicit N/A/UNKNOWN |
| criticality      | Required or explicit N/A/UNKNOWN |
| substitutability | Required or explicit N/A/UNKNOWN |
| sharedMode       | Required or explicit N/A/UNKNOWN |
| evidenceRefs     | Required or explicit N/A/UNKNOWN |
| confidence       | Required or explicit N/A/UNKNOWN |

# Object profile: FailureScenario

**Normative requirements.**

| **Element**      | **Requirement**                  |
|------------------|----------------------------------|
| preState         | Required or explicit N/A/UNKNOWN |
| initiatingSource | Required or explicit N/A/UNKNOWN |
| steps            | Required or explicit N/A/UNKNOWN |
| safeguards       | Required or explicit N/A/UNKNOWN |
| residualState    | Required or explicit N/A/UNKNOWN |
| outcomeEffects   | Required or explicit N/A/UNKNOWN |
| evidenceRefs     | Required or explicit N/A/UNKNOWN |
| confidence       | Required or explicit N/A/UNKNOWN |

# Object profile: Safeguard

**Normative requirements.**

| **Element**      | **Requirement**                  |
|------------------|----------------------------------|
| function         | Required or explicit N/A/UNKNOWN |
| protectedSubject | Required or explicit N/A/UNKNOWN |
| activation       | Required or explicit N/A/UNKNOWN |
| authority        | Required or explicit N/A/UNKNOWN |
| dependencies     | Required or explicit N/A/UNKNOWN |
| stateCoverage    | Required or explicit N/A/UNKNOWN |
| failureModes     | Required or explicit N/A/UNKNOWN |
| evidenceRefs     | Required or explicit N/A/UNKNOWN |
| controlRefs      | Required or explicit N/A/UNKNOWN |

# Object profile: Control

**Normative requirements.**

| **Element**         | **Requirement**                  |
|---------------------|----------------------------------|
| domainId            | Required or explicit N/A/UNKNOWN |
| familyId            | Required or explicit N/A/UNKNOWN |
| objective           | Required or explicit N/A/UNKNOWN |
| requirement         | Required or explicit N/A/UNKNOWN |
| applicability       | Required or explicit N/A/UNKNOWN |
| criteria            | Required or explicit N/A/UNKNOWN |
| methods             | Required or explicit N/A/UNKNOWN |
| assuranceDimensions | Required or explicit N/A/UNKNOWN |
| evidenceProfile     | Required or explicit N/A/UNKNOWN |
| gateRefs            | Required or explicit N/A/UNKNOWN |

# Object profile: Evidence

**Normative requirements.**

| **Element**   | **Requirement**                  |
|---------------|----------------------------------|
| evidenceClass | Required or explicit N/A/UNKNOWN |
| source        | Required or explicit N/A/UNKNOWN |
| collector     | Required or explicit N/A/UNKNOWN |
| custodian     | Required or explicit N/A/UNKNOWN |
| assertionRefs | Required or explicit N/A/UNKNOWN |
| scope         | Required or explicit N/A/UNKNOWN |
| period        | Required or explicit N/A/UNKNOWN |
| state         | Required or explicit N/A/UNKNOWN |
| integrity     | Required or explicit N/A/UNKNOWN |
| qualityVector | Required or explicit N/A/UNKNOWN |
| sufficiency   | Required or explicit N/A/UNKNOWN |
| restrictions  | Required or explicit N/A/UNKNOWN |

# Object profile: Assessment

**Normative requirements.**

| **Element**      | **Requirement**                  |
|------------------|----------------------------------|
| programId        | Required or explicit N/A/UNKNOWN |
| decisionQuestion | Required or explicit N/A/UNKNOWN |
| capabilityId     | Required or explicit N/A/UNKNOWN |
| scope            | Required or explicit N/A/UNKNOWN |
| profile          | Required or explicit N/A/UNKNOWN |
| methods          | Required or explicit N/A/UNKNOWN |
| team             | Required or explicit N/A/UNKNOWN |
| evidenceManifest | Required or explicit N/A/UNKNOWN |
| results          | Required or explicit N/A/UNKNOWN |
| gates            | Required or explicit N/A/UNKNOWN |
| review           | Required or explicit N/A/UNKNOWN |

# Object profile: Finding

**Normative requirements.**

| **Element**    | **Requirement**                  |
|----------------|----------------------------------|
| criterionRef   | Required or explicit N/A/UNKNOWN |
| condition      | Required or explicit N/A/UNKNOWN |
| evidenceRefs   | Required or explicit N/A/UNKNOWN |
| cause          | Required or explicit N/A/UNKNOWN |
| consequence    | Required or explicit N/A/UNKNOWN |
| classification | Required or explicit N/A/UNKNOWN |
| gateEffect     | Required or explicit N/A/UNKNOWN |
| scoreEffect    | Required or explicit N/A/UNKNOWN |
| owner          | Required or explicit N/A/UNKNOWN |
| status         | Required or explicit N/A/UNKNOWN |

# Object profile: UNKNOWN

**Normative requirements.**

| **Element**      | **Requirement**                  |
|------------------|----------------------------------|
| subjectRef       | Required or explicit N/A/UNKNOWN |
| missingAttribute | Required or explicit N/A/UNKNOWN |
| reason           | Required or explicit N/A/UNKNOWN |
| materiality      | Required or explicit N/A/UNKNOWN |
| decisionEffect   | Required or explicit N/A/UNKNOWN |
| evidenceNeeded   | Required or explicit N/A/UNKNOWN |
| owner            | Required or explicit N/A/UNKNOWN |
| trigger          | Required or explicit N/A/UNKNOWN |
| status           | Required or explicit N/A/UNKNOWN |

# Object profile: GateResult

**Normative requirements.**

| **Element**    | **Requirement**                  |
|----------------|----------------------------------|
| gateId         | Required or explicit N/A/UNKNOWN |
| applicability  | Required or explicit N/A/UNKNOWN |
| criterion      | Required or explicit N/A/UNKNOWN |
| evidenceRefs   | Required or explicit N/A/UNKNOWN |
| stateCoverage  | Required or explicit N/A/UNKNOWN |
| findings       | Required or explicit N/A/UNKNOWN |
| unknowns       | Required or explicit N/A/UNKNOWN |
| status         | Required or explicit N/A/UNKNOWN |
| decisionEffect | Required or explicit N/A/UNKNOWN |
| review         | Required or explicit N/A/UNKNOWN |

# Object profile: Score

**Normative requirements.**

| **Element**       | **Requirement**                  |
|-------------------|----------------------------------|
| subjectRef        | Required or explicit N/A/UNKNOWN |
| profileVersion    | Required or explicit N/A/UNKNOWN |
| inputs            | Required or explicit N/A/UNKNOWN |
| weights           | Required or explicit N/A/UNKNOWN |
| rawIndicator      | Required or explicit N/A/UNKNOWN |
| adjustedIndicator | Required or explicit N/A/UNKNOWN |
| coverage          | Required or explicit N/A/UNKNOWN |
| confidence        | Required or explicit N/A/UNKNOWN |
| gateOverlay       | Required or explicit N/A/UNKNOWN |
| unknownOverlay    | Required or explicit N/A/UNKNOWN |

# Object profile: Decision

**Normative requirements.**

| **Element**       | **Requirement**                  |
|-------------------|----------------------------------|
| question          | Required or explicit N/A/UNKNOWN |
| subjectRef        | Required or explicit N/A/UNKNOWN |
| scope             | Required or explicit N/A/UNKNOWN |
| recommendationRef | Required or explicit N/A/UNKNOWN |
| gateResults       | Required or explicit N/A/UNKNOWN |
| unknowns          | Required or explicit N/A/UNKNOWN |
| scores            | Required or explicit N/A/UNKNOWN |
| conditions        | Required or explicit N/A/UNKNOWN |
| decisionState     | Required or explicit N/A/UNKNOWN |
| authority         | Required or explicit N/A/UNKNOWN |
| validity          | Required or explicit N/A/UNKNOWN |

# Object profile: Report

**Normative requirements.**

| **Element**    | **Requirement**                  |
|----------------|----------------------------------|
| reportClass    | Required or explicit N/A/UNKNOWN |
| programRef     | Required or explicit N/A/UNKNOWN |
| assessmentRef  | Required or explicit N/A/UNKNOWN |
| decisionRef    | Required or explicit N/A/UNKNOWN |
| issuer         | Required or explicit N/A/UNKNOWN |
| users          | Required or explicit N/A/UNKNOWN |
| intendedUse    | Required or explicit N/A/UNKNOWN |
| classification | Required or explicit N/A/UNKNOWN |
| validity       | Required or explicit N/A/UNKNOWN |
| sections       | Required or explicit N/A/UNKNOWN |
| approvals      | Required or explicit N/A/UNKNOWN |

# Object profile: Event

**Normative requirements.**

| **Element**        | **Requirement**                  |
|--------------------|----------------------------------|
| eventType          | Required or explicit N/A/UNKNOWN |
| subjectRef         | Required or explicit N/A/UNKNOWN |
| source             | Required or explicit N/A/UNKNOWN |
| observedAt         | Required or explicit N/A/UNKNOWN |
| effectiveAt        | Required or explicit N/A/UNKNOWN |
| payload            | Required or explicit N/A/UNKNOWN |
| severity           | Required or explicit N/A/UNKNOWN |
| triggerRule        | Required or explicit N/A/UNKNOWN |
| reviewState        | Required or explicit N/A/UNKNOWN |
| affectedAssertions | Required or explicit N/A/UNKNOWN |

# 9 Relationship registry

**Normative requirements.**

| **Element**              | **Requirement**                                   |
|--------------------------|---------------------------------------------------|
| HAS_OUTCOME              | Typed, directed, scoped, versioned and reviewable |
| REQUIRES_FUNCTION        | Typed, directed, scoped, versioned and reviewable |
| IMPLEMENTED_BY           | Typed, directed, scoped, versioned and reviewable |
| COMPOSED_OF              | Typed, directed, scoped, versioned and reviewable |
| CONNECTS_TO              | Typed, directed, scoped, versioned and reviewable |
| CONSUMES_RESOURCE        | Typed, directed, scoped, versioned and reviewable |
| DEPENDS_ON               | Typed, directed, scoped, versioned and reviewable |
| SHARES_FAULT_DOMAIN_WITH | Typed, directed, scoped, versioned and reviewable |
| LOCATED_IN               | Typed, directed, scoped, versioned and reviewable |
| OPERATED_BY              | Typed, directed, scoped, versioned and reviewable |
| CONTROLLED_BY            | Typed, directed, scoped, versioned and reviewable |
| MONITORED_BY             | Typed, directed, scoped, versioned and reviewable |
| PROTECTED_BY             | Typed, directed, scoped, versioned and reviewable |
| EXPOSED_TO               | Typed, directed, scoped, versioned and reviewable |
| INITIATES                | Typed, directed, scoped, versioned and reviewable |
| PROPAGATES_TO            | Typed, directed, scoped, versioned and reviewable |
| RECOVERS_THROUGH         | Typed, directed, scoped, versioned and reviewable |
| GOVERNED_BY              | Typed, directed, scoped, versioned and reviewable |
| HAS_EVIDENCE_REQUIREMENT | Typed, directed, scoped, versioned and reviewable |
| EVIDENCED_BY             | Typed, directed, scoped, versioned and reviewable |
| SUPPORTS                 | Typed, directed, scoped, versioned and reviewable |
| CHALLENGES               | Typed, directed, scoped, versioned and reviewable |
| QUALIFIES                | Typed, directed, scoped, versioned and reviewable |
| ASSESSED_BY              | Typed, directed, scoped, versioned and reviewable |
| RESULTS_IN               | Typed, directed, scoped, versioned and reviewable |
| HAS_FINDING              | Typed, directed, scoped, versioned and reviewable |
| HAS_UNKNOWN              | Typed, directed, scoped, versioned and reviewable |
| EVALUATES_GATE           | Typed, directed, scoped, versioned and reviewable |
| CONSTRAINS               | Typed, directed, scoped, versioned and reviewable |
| SUMMARISED_BY            | Typed, directed, scoped, versioned and reviewable |
| RECOMMENDS               | Typed, directed, scoped, versioned and reviewable |
| REVIEWED_BY              | Typed, directed, scoped, versioned and reviewable |
| APPROVED_BY              | Typed, directed, scoped, versioned and reviewable |
| REPORTED_IN              | Typed, directed, scoped, versioned and reviewable |
| REQUIRES_ACTION          | Typed, directed, scoped, versioned and reviewable |
| CLOSED_BY                | Typed, directed, scoped, versioned and reviewable |
| INVALIDATED_BY           | Typed, directed, scoped, versioned and reviewable |
| TRIGGERS_REASSESSMENT    | Typed, directed, scoped, versioned and reviewable |
| SUPERSEDES               | Typed, directed, scoped, versioned and reviewable |
| MIGRATED_FROM            | Typed, directed, scoped, versioned and reviewable |
| INTEGRATION_HANDOFF      | Typed, directed, scoped, versioned and reviewable |

# 10 Relationship envelope

**Normative requirements.**

| **Element**    | **Requirement** |
|----------------|-----------------|
| relationshipId | Required        |
| type           | Required        |
| sourceId       | Required        |
| targetId       | Required        |
| semanticOwner  | Required        |
| scope          | Required        |
| conditions     | Required        |
| effectiveFrom  | Required        |
| effectiveTo    | Required        |
| sourceRecord   | Required        |
| evidenceRefs   | Required        |
| confidence     | Required        |
| reviewState    | Required        |
| classification | Required        |
| version        | Required        |
| supersedes     | Required        |

# 11 End-to-end traceability

**Normative requirements.**

| **Element** | **Requirement**                      |
|-------------|--------------------------------------|
| TR-01       | Capability to Outcome                |
| TR-02       | Outcome to Function                  |
| TR-03       | Function to Architecture             |
| TR-04       | Architecture to Dependency           |
| TR-05       | Dependency to Failure                |
| TR-06       | Failure to Safeguard                 |
| TR-07       | Safeguard to Control                 |
| TR-08       | Control to Evidence Requirement      |
| TR-09       | Requirement to Evidence or UNKNOWN   |
| TR-10       | Procedure to Result                  |
| TR-11       | Result to Finding or UNKNOWN         |
| TR-12       | Gate to Evidence/Findings/UNKNOWN    |
| TR-13       | Score to immutable inputs/profile    |
| TR-14       | Recommendation to constraints        |
| TR-15       | Decision to authority/scope/validity |
| TR-16       | Report to approved decision          |
| TR-17       | Trigger to impacted objects          |
| TR-18       | Supersession to prior/successor      |

# Controlled vocabulary: Lifecycle

**Normative requirements.**

| **Element** | **Requirement** |
|-------------|-----------------|
| DRAFT       | Controlled code |
| CANDIDATE   | Controlled code |
| REVIEWED    | Controlled code |
| APPROVED    | Controlled code |
| ACTIVE      | Controlled code |
| SUSPENDED   | Controlled code |
| WITHDRAWN   | Controlled code |
| SUPERSEDED  | Controlled code |
| RETIRED     | Controlled code |

# Controlled vocabulary: Assertion

**Normative requirements.**

| **Element** | **Requirement** |
|-------------|-----------------|
| CANDIDATE   | Controlled code |
| SUPPORTED   | Controlled code |
| CHALLENGED  | Controlled code |
| QUALIFIED   | Controlled code |
| CONFLICTING | Controlled code |
| UNKNOWN     | Controlled code |
| SUPERSEDED  | Controlled code |

# Controlled vocabulary: ControlResult

**Normative requirements.**

| **Element**           | **Requirement** |
|-----------------------|-----------------|
| NOT_ASSESSED          | Controlled code |
| UNKNOWN               | Controlled code |
| N/A                   | Controlled code |
| NOT_IMPLEMENTED       | Controlled code |
| PARTIAL               | Controlled code |
| IMPLEMENTED           | Controlled code |
| OPERATING_EFFECTIVELY | Controlled code |
| INEFFECTIVE           | Controlled code |
| SUSPENDED             | Controlled code |

# Controlled vocabulary: GateResult

**Normative requirements.**

| **Element**  | **Requirement** |
|--------------|-----------------|
| PASS         | Controlled code |
| FAIL         | Controlled code |
| UNKNOWN      | Controlled code |
| APPROVED_N/A | Controlled code |
| NOT_ASSESSED | Controlled code |

# Controlled vocabulary: Decision

**Normative requirements.**

| **Element**           | **Requirement** |
|-----------------------|-----------------|
| REASONABLY_ASSURED    | Controlled code |
| CONDITIONALLY_ASSURED | Controlled code |
| LIMITED               | Controlled code |
| ADVERSE_NOT_ASSURED   | Controlled code |
| UNKNOWN_INCONCLUSIVE  | Controlled code |
| SUSPENDED             | Controlled code |
| WITHDRAWN             | Controlled code |
| SUPERSEDED            | Controlled code |

# Controlled vocabulary: OperatingState

**Normative requirements.**

| **Element** | **Requirement** |
|-------------|-----------------|
| NORMAL      | Controlled code |
| MAINTENANCE | Controlled code |
| DEGRADED    | Controlled code |
| EMERGENCY   | Controlled code |
| RECOVERY    | Controlled code |
| TRANSITION  | Controlled code |
| UNKNOWN     | Controlled code |

# Controlled vocabulary: Classification

**Normative requirements.**

| **Element**       | **Requirement** |
|-------------------|-----------------|
| PUBLIC            | Controlled code |
| INTERNAL          | Controlled code |
| CLIENT_RESTRICTED | Controlled code |
| CONFIDENTIAL      | Controlled code |
| HIGHLY_RESTRICTED | Controlled code |

# 12 Serialization architecture

**Normative requirements.**

| **Element**         | **Requirement**             |
|---------------------|-----------------------------|
| JSON                | Application exchange        |
| JSON Schema 2020-12 | Structural validation       |
| JSON-LD 1.1         | Linked data                 |
| RDF/Turtle          | Graph exchange              |
| OWL 2               | Formal semantics            |
| SHACL               | Closed-world validation     |
| CSV                 | Registries                  |
| NDJSON              | Streams                     |
| Parquet             | Non-authoritative analytics |

# 13 JSON design rules

**Normative requirements.**

| **Element**                | **Requirement** |
|----------------------------|-----------------|
| UTF-8                      | Required        |
| camelCase                  | Required        |
| ISO8601                    | Required        |
| explicit-nullReason        | Required        |
| enum-codes                 | Required        |
| stable-schema              | Required        |
| additionalProperties-false | Required        |
| namespaced-extensions      | Required        |
| discriminator              | Required        |
| stable-references          | Required        |
| integrity-metadata         | Required        |
| classification             | Required        |

# 14 Semantic graph rules

**Normative requirements.**

| **Element**                             | **Requirement** |
|-----------------------------------------|-----------------|
| Protected JSON-LD terms                 | Required        |
| Stable prefixes and typed IDs           | Required        |
| Separate AIDCF/AITG contexts            | Required        |
| OWL classes mirror registry             | Required        |
| No automatic approval through inference | Required        |
| SHACL for closed-world cardinality      | Required        |
| Pinned imports                          | Required        |
| Resolvable deprecations                 | Required        |

# 15 JSON Schema package

**Normative requirements.**

| **Element**                        | **Requirement**  |
|------------------------------------|------------------|
| release-manifest.schema.json       | Normative schema |
| common-envelope.schema.json        | Normative schema |
| capability.schema.json             | Normative schema |
| architecture.schema.json           | Normative schema |
| dependency.schema.json             | Normative schema |
| failure-scenario.schema.json       | Normative schema |
| safeguard.schema.json              | Normative schema |
| control.schema.json                | Normative schema |
| evidence-requirement.schema.json   | Normative schema |
| evidence-object.schema.json        | Normative schema |
| assessment.schema.json             | Normative schema |
| result-finding-unknown.schema.json | Normative schema |
| gate.schema.json                   | Normative schema |
| score.schema.json                  | Normative schema |
| decision.schema.json               | Normative schema |
| program.schema.json                | Normative schema |
| report-statement.schema.json       | Normative schema |
| action-trigger-event.schema.json   | Normative schema |
| integration-handoff.schema.json    | Normative schema |
| validation-result.schema.json      | Normative schema |

# 16 Semantic publication package

**Normative requirements.**

| **Element**               | **Requirement** |
|---------------------------|-----------------|
| aidcf-context-v1.0.jsonld | Context         |
| aidcf-core-v1.0.owl       | Ontology        |
| aidcf-core-v1.0.ttl       | Turtle          |
| aidcf-shapes-v1.0.ttl     | SHACL           |
| registries/\*.csv         | Registries      |
| examples/\*.jsonld        | Examples        |
| conformance-tests/        | Fixtures        |

# 17 Registry catalogue

**Normative requirements.**

| **Element**               | **Requirement**                                               |
|---------------------------|---------------------------------------------------------------|
| artifacts.csv             | code label definition owner version status source replacement |
| object-types.csv          | code label definition owner version status source replacement |
| relationship-types.csv    | code label definition owner version status source replacement |
| states.csv                | code label definition owner version status source replacement |
| domains.csv               | code label definition owner version status source replacement |
| control-families.csv      | code label definition owner version status source replacement |
| controls.csv              | code label definition owner version status source replacement |
| critical-gates.csv        | code label definition owner version status source replacement |
| evidence-classes.csv      | code label definition owner version status source replacement |
| evidence-quality.csv      | code label definition owner version status source replacement |
| assessment-methods.csv    | code label definition owner version status source replacement |
| finding-classes.csv       | code label definition owner version status source replacement |
| unknown-reasons.csv       | code label definition owner version status source replacement |
| decision-states.csv       | code label definition owner version status source replacement |
| report-types.csv          | code label definition owner version status source replacement |
| architecture-patterns.csv | code label definition owner version status source replacement |
| external-mappings.csv     | code label definition owner version status source replacement |
| deprecated-terms.csv      | code label definition owner version status source replacement |
| migration-rules.csv       | code label definition owner version status source replacement |

# 18 Business rules

**Normative requirements.**

| **Element** | **Requirement**                                          |
|-------------|----------------------------------------------------------|
| BR-001      | Applied control requires subject/applicability           |
| BR-002      | N/A requires rationale; missing evidence is UNKNOWN      |
| BR-003      | Positive result cannot exceed assessed dimension         |
| BR-004      | Gate PASS requires evidence                              |
| BR-005      | Reasonably Assured blocked by gate FAIL/critical UNKNOWN |
| BR-006      | Scores require coverage/confidence/profile/gates         |
| BR-007      | Report cannot exceed decision                            |
| BR-008      | Closure requires evidence/reassessment                   |
| BR-009      | Supersession preserves history                           |
| BR-010      | AITG mapping preserves ownership                         |
| BR-011      | Inference cannot auto-promote                            |
| BR-012      | Sensitive export requires authority                      |
| BR-013      | Material change triggers impact review                   |
| BR-014      | Risk acceptance is not conformity                        |
| BR-015      | Evidence reuse requires assertion review                 |

# 19 Canonical queries

**Normative requirements.**

| **Element** | **Requirement**                            |
|-------------|--------------------------------------------|
| Q01         | Capability to systems/dependencies         |
| Q02         | Outcome to failure paths/fault domains     |
| Q03         | Control to evidence/results/findings       |
| Q04         | Evidence to assertions/lineage/decisions   |
| Q05         | Gate to criterion/evidence/UNKNOWN/effect  |
| Q06         | Decision to gates/UNKNOWN/scores/approvals |
| Q07         | Statement to decision consistency          |
| Q08         | Event to impacted objects                  |
| Q09         | Provider to concentration/common modes     |
| Q10         | Snapshot to successor/migration            |
| Q11         | Candidates awaiting review                 |
| Q12         | Sensitive paths by disclosure profile      |

# 20 Event model

**Normative requirements.**

| **Element**        | **Requirement** |
|--------------------|-----------------|
| eventId            | Required        |
| eventType          | Required        |
| source             | Required        |
| subjectRef         | Required        |
| observedAt         | Required        |
| effectiveAt        | Required        |
| payload            | Required        |
| schemaVersion      | Required        |
| sourceHealth       | Required        |
| severity           | Required        |
| materiality        | Required        |
| affectedAssertions | Required        |
| candidateTriggers  | Required        |
| humanDisposition   | Required        |
| resultingDecision  | Required        |
| snapshot           | Required        |
| supersession       | Required        |

# 21 Event types

**Normative requirements.**

| **Element**                 | **Requirement**                        |
|-----------------------------|----------------------------------------|
| ARCHITECTURE_CHANGED        | Candidate event; human review required |
| CAPACITY_THRESHOLD_BREACHED | Candidate event; human review required |
| CONFIGURATION_CHANGED       | Candidate event; human review required |
| PROVIDER_CHANGED            | Candidate event; human review required |
| SOURCE_UNAVAILABLE          | Candidate event; human review required |
| EVIDENCE_EXPIRED            | Candidate event; human review required |
| EVIDENCE_CONFLICT           | Candidate event; human review required |
| INCIDENT_DETECTED           | Candidate event; human review required |
| TEST_FAILED                 | Candidate event; human review required |
| GATE_STATUS_CHANGED         | Candidate event; human review required |
| FINDING_CLOSED              | Candidate event; human review required |
| CONTROL_DRIFT               | Candidate event; human review required |
| DEPENDENCY_DRIFT            | Candidate event; human review required |
| DECISION_SUSPENDED          | Candidate event; human review required |
| REPORT_WITHDRAWN            | Candidate event; human review required |

# 22 Change-impact contract

**Normative requirements.**

| **Element** | **Requirement**                     |
|-------------|-------------------------------------|
| 1           | Validate event                      |
| 2           | Resolve identity/snapshot           |
| 3           | Traverse assertions/dependencies    |
| 4           | Identify controls/scenarios/gates   |
| 5           | Recompute candidate coverage/scores |
| 6           | Apply candidate ceilings            |
| 7           | Route review                        |
| 8           | Approve disposition                 |
| 9           | Create superseding snapshot         |
| 10          | Notify report owners                |

# 23 API and exchange

**Normative requirements.**

| **Element**              | **Requirement** |
|--------------------------|-----------------|
| versioned-media-type     | Required        |
| idempotency              | Required        |
| optimistic-concurrency   | Required        |
| immutable-snapshots      | Required        |
| pagination               | Required        |
| filtering                | Required        |
| bulk-validation          | Required        |
| dry-run                  | Required        |
| explicit-errors          | Required        |
| classification-aware     | Required        |
| audit-log                | Required        |
| no-destructive-overwrite | Required        |

# 24 Semantic operations

**Normative requirements.**

| **Element**             | **Requirement**    |
|-------------------------|--------------------|
| validateRecord          | Expected operation |
| validatePackage         | Expected operation |
| resolveIdentifier       | Expected operation |
| getLineage              | Expected operation |
| getTraceabilityPath     | Expected operation |
| getImpactAnalysis       | Expected operation |
| createCandidateRecord   | Expected operation |
| submitForReview         | Expected operation |
| approveRecord           | Expected operation |
| supersedeRecord         | Expected operation |
| publishSnapshot         | Expected operation |
| exportDisclosurePackage | Expected operation |
| ingestEvent             | Expected operation |
| getConformanceResult    | Expected operation |

# 25 Security/privacy/disclosure

**Normative requirements.**

| **Element**              | **Requirement** |
|--------------------------|-----------------|
| classification           | Required        |
| attribute-access         | Required        |
| edge-access              | Required        |
| purpose-bound-disclosure | Required        |
| redaction                | Required        |
| encryption               | Required        |
| integrity                | Required        |
| no-secrets               | Required        |
| query-monitoring         | Required        |
| export-controls          | Required        |
| segregation              | Required        |
| minimisation             | Required        |
| retention                | Required        |
| breach-impact            | Required        |
| AI-derived-candidate     | Required        |

# 26 Provenance/integrity

**Normative requirements.**

| **Element**           | **Requirement** |
|-----------------------|-----------------|
| sourceSystem          | Required        |
| sourceRecord          | Required        |
| creator               | Required        |
| collector             | Required        |
| method                | Required        |
| timestamps            | Required        |
| clock                 | Required        |
| transformationVersion | Required        |
| hash                  | Required        |
| signature             | Required        |
| custodian             | Required        |
| classification        | Required        |
| chainOfCustody        | Required        |
| review                | Required        |
| disposition           | Required        |
| supportLinks          | Required        |
| challengeLinks        | Required        |
| supersession          | Required        |
| migration             | Required        |

# 27 Versioning/migration

**Normative requirements.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Semantic versioning               | Rule            |
| Major for breaking                | Rule            |
| Minor for additive optional       | Rule            |
| Patch for metadata                | Rule            |
| Source/target migration           | Rule            |
| No automatic reinterpretation     | Rule            |
| Deprecated terms resolvable       | Rule            |
| Invalid migration blocked/UNKNOWN | Rule            |
| Migration and validation records  | Rule            |
| Decision/report revalidation      | Rule            |

# 28 Source-artifact binding

**Normative requirements.**

| **Element** | **Requirement**   |
|-------------|-------------------|
| 003         | Ontology/taxonomy |
| 004         | Failure model     |
| 005         | AITG integration  |
| 006         | Principles        |
| 007         | Controls          |
| 008         | Evidence          |
| 009         | Assessment        |
| 010         | Scoring/decision  |
| 011         | Program           |
| 012         | Reporting         |
| 013         | Architecture      |

# 29 Exchange bundles

**Normative requirements.**

| **Element**  | **Requirement**                                  |
|--------------|--------------------------------------------------|
| Baseline     | Manifest, records, validation and classification |
| Architecture | Manifest, records, validation and classification |
| Scenario     | Manifest, records, validation and classification |
| Control      | Manifest, records, validation and classification |
| Evidence     | Manifest, records, validation and classification |
| Assessment   | Manifest, records, validation and classification |
| Decision     | Manifest, records, validation and classification |
| Reporting    | Manifest, records, validation and classification |
| Continuing   | Manifest, records, validation and classification |
| Integration  | Manifest, records, validation and classification |

# 30 Synthetic dataset

**Normative requirements.**

| **Element**                           | **Requirement**            |
|---------------------------------------|----------------------------|
| Capability/outcomes                   | Required synthetic fixture |
| Training chain                        | Required synthetic fixture |
| Power/cooling/compute/storage/network | Required synthetic fixture |
| External dependencies                 | Required synthetic fixture |
| Fault domains/common modes            | Required synthetic fixture |
| Failure scenarios                     | Required synthetic fixture |
| Safeguards                            | Required synthetic fixture |
| Controls/evidence                     | Required synthetic fixture |
| At least one UNKNOWN                  | Required synthetic fixture |
| Gates                                 | Required synthetic fixture |
| Score/decision                        | Required synthetic fixture |
| Reports                               | Required synthetic fixture |
| Change/reassessment                   | Required synthetic fixture |
| AITG handoff                          | Required synthetic fixture |

# 31 Conformance tests

**Normative requirements.**

| **Element** | **Requirement**       |
|-------------|-----------------------|
| CT-01       | Positive records      |
| CT-02       | Missing mandatory     |
| CT-03       | UNKNOWN handling      |
| CT-04       | Gate dominance        |
| CT-05       | Score reproducibility |
| CT-06       | Report consistency    |
| CT-07       | Supersession          |
| CT-08       | Migration             |
| CT-09       | Security              |
| CT-10       | AITG handoff          |
| CT-11       | Event impact          |
| CT-12       | Anti-gaming           |
| CT-13       | Baseline conflict     |
| CT-14       | Performance           |

# Template: Release Manifest

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# Template: Baseline Issue

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# Template: Object Registry Entry

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# Template: Relationship Entry

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# Template: Traceability Link

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# Template: Validation Result

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# Template: Migration Record

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# Template: Impact Analysis

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# Template: Disclosure Profile

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# Template: Conformance Report

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# Template: Integration Handoff

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# Template: Source-System Mapping

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# Template: Extension Registration

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# Template: Schema Change Request

**Normative requirements.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| id              |                 |
| type            |                 |
| version         |                 |
| status          |                 |
| scope           |                 |
| sources         |                 |
| subjects        |                 |
| rule            |                 |
| evidence        |                 |
| lineage         |                 |
| owner           |                 |
| reviewer        |                 |
| approval        |                 |
| effectivePeriod |                 |
| classification  |                 |
| supersession    |                 |

# 32 Data governance roles

**Normative requirements.**

| **Element**           | **Requirement**                 |
|-----------------------|---------------------------------|
| Methodology authority | Normative meanings/release      |
| Registry steward      | Codes/mappings                  |
| Schema maintainer     | Schemas/context/ontology/shapes |
| Domain steward        | Domain mappings                 |
| Evidence steward      | Evidence semantics              |
| Decision steward      | Gate/score/decision             |
| Security steward      | Classification/disclosure       |
| AITG steward          | Identity/handoff                |
| Tool implementer      | Implementation/audit            |
| Independent reviewer  | Conformance challenge           |
| Release authority     | Publication/migration           |

# 33 Extension governance

**Normative requirements.**

| **Element**    | **Requirement** |
|----------------|-----------------|
| namespace      | Required        |
| owner          | Required        |
| justification  | Required        |
| targets        | Required        |
| no-collision   | Required        |
| datatype       | Required        |
| cardinality    | Required        |
| classification | Required        |
| schema         | Required        |
| shape          | Required        |
| examples       | Required        |
| tests          | Required        |
| approval       | Required        |
| deprecation    | Required        |
| migration      | Required        |

# 34 Data quality

**Normative requirements.**

| **Element**   | **Requirement**                                        |
|---------------|--------------------------------------------------------|
| Completeness  | Measured/reported separately from assurance confidence |
| Validity      | Measured/reported separately from assurance confidence |
| Consistency   | Measured/reported separately from assurance confidence |
| Uniqueness    | Measured/reported separately from assurance confidence |
| Timeliness    | Measured/reported separately from assurance confidence |
| Accuracy      | Measured/reported separately from assurance confidence |
| Lineage       | Measured/reported separately from assurance confidence |
| Integrity     | Measured/reported separately from assurance confidence |
| Reviewability | Measured/reported separately from assurance confidence |
| Security      | Measured/reported separately from assurance confidence |

# 35 Reference implementation

**Normative requirements.**

| **Element**            | **Requirement**                      |
|------------------------|--------------------------------------|
| ArtifactRepository     | Technology-neutral logical component |
| RegistryRepository     | Technology-neutral logical component |
| SchemaRegistry         | Technology-neutral logical component |
| IdentifierService      | Technology-neutral logical component |
| IngestionService       | Technology-neutral logical component |
| ValidationEngine       | Technology-neutral logical component |
| TraceabilityGraph      | Technology-neutral logical component |
| EvidenceConnectors     | Technology-neutral logical component |
| AssessmentWorkflow     | Technology-neutral logical component |
| GateScoreEngine        | Technology-neutral logical component |
| DecisionReviewWorkflow | Technology-neutral logical component |
| ReportingService       | Technology-neutral logical component |
| EventImpactService     | Technology-neutral logical component |
| DisclosureService      | Technology-neutral logical component |
| AuditLog               | Technology-neutral logical component |
| ConformanceRunner      | Technology-neutral logical component |

# 36 Storage projections

**Normative requirements.**

| **Element**                           | **Requirement** |
|---------------------------------------|-----------------|
| Canonical object retained             | Rule            |
| Graph edges retain provenance/version | Rule            |
| RDF named snapshots/shapes            | Rule            |
| Relational stable keys                | Rule            |
| Search non-authoritative              | Rule            |
| Warehouse snapshot dimensions         | Rule            |
| Evidence blobs referenced             | Rule            |
| Caches cannot approve/overwrite       | Rule            |

# Worked trace: Electrical

**Normative requirements.**

| **Element** | **Requirement**                                                                                            |
|-------------|------------------------------------------------------------------------------------------------------------|
| Trace       | Outcome -\> power -\> dependencies -\> failure -\> safeguards -\> controls/evidence -\> CG-05 -\> decision |
| Forward     | Outcome to report                                                                                          |
| Reverse     | Claim to evidence/source                                                                                   |
| UNKNOWN     | Missing link explicit                                                                                      |
| Change      | Affected objects identified                                                                                |
| Review      | Candidate inference remains unapproved                                                                     |

# Worked trace: Thermal

**Normative requirements.**

| **Element** | **Requirement**                                                                        |
|-------------|----------------------------------------------------------------------------------------|
| Trace       | Outcome -\> cooling -\> common mode -\> scenario -\> controls/evidence -\> CG-06/09/10 |
| Forward     | Outcome to report                                                                      |
| Reverse     | Claim to evidence/source                                                               |
| UNKNOWN     | Missing link explicit                                                                  |
| Change      | Affected objects identified                                                            |
| Review      | Candidate inference remains unapproved                                                 |

# Worked trace: Digital authority

**Normative requirements.**

| **Element** | **Requirement**                                             |
|-------------|-------------------------------------------------------------|
| Trace       | Outcome -\> identity/controller -\> safeguards -\> CG-07/15 |
| Forward     | Outcome to report                                           |
| Reverse     | Claim to evidence/source                                    |
| UNKNOWN     | Missing link explicit                                       |
| Change      | Affected objects identified                                 |
| Review      | Candidate inference remains unapproved                      |

# Worked trace: Recovery

**Normative requirements.**

| **Element** | **Requirement**                                                                         |
|-------------|-----------------------------------------------------------------------------------------|
| Trace       | Outcome -\> restore/alternate capacity -\> dependencies -\> exercise -\> CG-03/08/09/10 |
| Forward     | Outcome to report                                                                       |
| Reverse     | Claim to evidence/source                                                                |
| UNKNOWN     | Missing link explicit                                                                   |
| Change      | Affected objects identified                                                             |
| Review      | Candidate inference remains unapproved                                                  |

# Worked trace: Report lineage

**Normative requirements.**

| **Element** | **Requirement**                                                                           |
|-------------|-------------------------------------------------------------------------------------------|
| Trace       | Decision -\> gates/UNKNOWN/scores -\> statement -\> validity -\> trigger -\> supersession |
| Forward     | Outcome to report                                                                         |
| Reverse     | Claim to evidence/source                                                                  |
| UNKNOWN     | Missing link explicit                                                                     |
| Change      | Affected objects identified                                                               |
| Review      | Candidate inference remains unapproved                                                    |

# 37 Conformance validation

**Normative requirements.**

| **Element** | **Requirement**                               |
|-------------|-----------------------------------------------|
| TDS-VAL-001 | Manifest approved                             |
| TDS-VAL-002 | Baseline conflicts visible                    |
| TDS-VAL-003 | IDs stable/unique                             |
| TDS-VAL-004 | Owner/source/version/status present           |
| TDS-VAL-005 | Relationships or UNKNOWN                      |
| TDS-VAL-006 | N/A justified                                 |
| TDS-VAL-007 | Assertions evidenced/UNKNOWN                  |
| TDS-VAL-008 | Evidence quality claim-specific               |
| TDS-VAL-009 | Results link method/subject/evidence/reviewer |
| TDS-VAL-010 | Gate PASS has evidence                        |
| TDS-VAL-011 | Scores reproducible                           |
| TDS-VAL-012 | Decision respects gates/UNKNOWN               |
| TDS-VAL-013 | Report matches decision                       |
| TDS-VAL-014 | Events do not auto-approve                    |
| TDS-VAL-015 | History preserved                             |
| TDS-VAL-016 | Migrations explicit                           |
| TDS-VAL-017 | AITG ownership preserved                      |
| TDS-VAL-018 | Sensitive paths controlled                    |
| TDS-VAL-019 | Extensions non-colliding                      |
| TDS-VAL-020 | Tests pass                                    |

# 38 Review and release gates

**Normative requirements.**

| **Element**                     | **Requirement** |
|---------------------------------|-----------------|
| Methodology author              | Pending         |
| Ontology/data architect         | Pending         |
| Semantic reviewers              | Pending         |
| Control/evidence reviewer       | Pending         |
| Assessment reviewer             | Pending         |
| Scoring/decision reviewer       | Pending         |
| Program/reporting reviewer      | Pending         |
| Reference-architecture reviewer | Pending         |
| JSON Schema reviewer            | Pending         |
| RDF/OWL/SHACL reviewer          | Pending         |
| Security/privacy reviewer       | Pending         |
| AITG reviewer                   | Pending         |
| Synthetic dataset pilot         | Pending         |
| Graph pilot                     | Pending         |
| API/event pilot                 | Pending         |
| Independent conformance review  | Pending         |
| Public release                  | Pending         |

## Final doctrine

**AIDCF-014 makes assurance claims reconstructable and testable without giving machines authority they do not possess. Structural validity does not prove truth, engineering adequacy or assurance. Conflict, incomplete lineage and missing evidence remain explicit and prevent stronger conclusions.**
