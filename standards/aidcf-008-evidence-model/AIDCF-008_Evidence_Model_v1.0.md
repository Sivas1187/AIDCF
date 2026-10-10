> Markdown edition. Source: [AIDCF-008_Evidence_Model_v1.0.docx](AIDCF-008_Evidence_Model_v1.0.docx) · PDF: [AIDCF-008_Evidence_Model_v1.0.pdf](AIDCF-008_Evidence_Model_v1.0.pdf)

A normative evidence architecture for traceable, current, sufficient and reviewable AI infrastructure assurance

Artifact ID: AIDCF-EVM-001  
Artifact type: Normative evidence architecture standard  
Status: Draft for controlled review  
Author: Siva Sethumadhavan  
Release 2: Practitioner Methodology

Evidence is the currency of assurance. Assertions, scores and decisions have no independent authority beyond their evidence, scope and review.

# Document control

| **Field**               | **Value**                                                                                                                                                                              |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Title                   | AIDCF Evidence Model v1.0                                                                                                                                                              |
| Artifact ID             | AIDCF-EVM-001                                                                                                                                                                          |
| Status                  | Draft for controlled review                                                                                                                                                            |
| Author                  | Siva Sethumadhavan                                                                                                                                                                     |
| Depends on              | AIDCF Manifesto; Core Conceptual Model; AIDCF-003; AIDCF-004; AIDCF-005; AIDCF-006; AIDCF-007                                                                                          |
| Purpose                 | Define evidence objects, classes, metadata, provenance, integrity, quality, freshness, coverage, sufficiency, confidence, conflict, retention and decision use.                        |
| Applies to              | All AIDCF controls, assertions, findings, critical gates, tests, scores, maturity determinations, reports, decisions and compatible tooling.                                           |
| Downstream              | AIDCF-009 Assessment Methodology; scoring, maturity, reporting and future scheme artifacts.                                                                                            |
| Safety/privacy boundary | Evidence collection shall be authorised, proportionate, lawful, minimally intrusive and protected. This standard does not authorise hazardous testing or unrestricted data collection. |

# Executive thesis

AIDCF assurance depends on whether a precise assertion is supported by evidence that is relevant, authentic, sufficiently complete, current for the represented state, traceable to its source, protected against inappropriate alteration, and reviewed by a competent accountable party. Evidence is not graded once for all purposes. Its usefulness is evaluated against the claim, Capability Instance, Service Outcome, boundary, operating state, period and decision question.

## Canonical evidence chain

Decision Question -\> Assertion -\> Evidence Requirement -\> Evidence Object -\> Provenance and Integrity -\> Relevance and Coverage -\> Quality and Freshness -\> Sufficiency -\> Confidence -\> Conflict and UNKNOWN -\> Finding / Critical Gate -\> Bounded Assurance Decision

## Key outputs

- Canonical EvidenceObject, EvidencePackage and EvidencePortfolio structures.

- Seven evidence classes and controlled subtypes.

- Six-dimensional evidence quality model.

- Freshness, retention and chain-of-custody rules.

- Assertion-specific sufficiency and confidence model.

- Evidence-to-control and evidence-to-critical-gate mappings.

- Conflict, derived evidence, automation and UNKNOWN rules.

- Machine-readable ontology, schema and validation expectations.

# Contents

1\. I Authority, scope and conformance

2\. II Evidence doctrine and mandatory distinctions

3\. III Evidence metamodel and object hierarchy

4\. IV Evidence taxonomy and subtype catalogue

5\. V Evidence metadata standard

6\. VI Provenance, integrity and chain of custody

7\. VII Evidence quality dimensions and grading

8\. VIII Freshness, validity, retention and legal hold

9\. IX Coverage, sampling and representativeness

10\. X Evidence sufficiency and confidence

11\. XI Evidence-to-assertion and finding model

12\. XII Evidence-to-control mapping

13\. XIII Critical-gate evidence profiles

14\. XIV Conflict, contradiction and UNKNOWN

15\. XV Derived, automated and AI-generated evidence

16\. XVI Evidence lifecycle and review workflow

17\. XVII Evidence security, privacy and disclosure

18\. XVIII Graph-native and machine-readable model

19\. XIX Conformance, validation and nonconformance

20\. XX Worked evidence packages

21\. Appendix A Evidence type registry

22\. Appendix B Quality scoring anchors

23\. Appendix C Control evidence profile matrix

24\. Appendix D Critical-gate evidence matrix

25\. Appendix E Record schemas

26\. Appendix F Review and release gates

# Part I - Authority, scope and conformance

## 1. Purpose

This standard operationalises the evidence commitments in AIDCF-006 and the minimum evidence expectations in AIDCF-007. It defines a common evidence language suitable for human assessments, structured workpapers, graph implementations and future assurance schemes.

## 2. Normative requirements

**EVM-REQ-001** Every material assertion shall link to supporting, challenging or qualifying Evidence Objects, or explicit UNKNOWN.

**EVM-REQ-002** Evidence shall retain identity, source, collection, scope, time, integrity, custody, classification and review metadata.

**EVM-REQ-003** Evidence quality and sufficiency shall be evaluated against a precise assertion; no evidence item has a universal grade.

**EVM-REQ-004** Design, implementation, operation and effectiveness claims shall use evidence appropriate to the claim type.

**EVM-REQ-005** Evidence conflict, staleness, inaccessible sources and coverage gaps shall remain visible.

**EVM-REQ-006** UNKNOWN shall not be transformed into pass, zero, false, Not Applicable or accepted risk.

**EVM-REQ-007** Critical-gate evidence shall meet the declared evidence floor or the gate shall remain UNKNOWN or Fail according to the criterion.

**EVM-REQ-008** Derived and AI-generated evidence shall retain source lineage, transformation logic and candidate review state.

**EVM-REQ-009** Evidence collection and testing shall be authorised, competent, proportionate, lawful and safe.

**EVM-REQ-010** Retention and deletion shall preserve legal, contractual, audit and decision-lineage obligations.

**EVM-REQ-011** Evidence reuse across controls or methods shall require assertion-specific relevance and scope evaluation.

**EVM-REQ-012** A score, maturity level or certificate shall not increase the evidential strength of its underlying sources.

## 3. Scope

- Evidence created or collected for all 360 AIDCF-007 controls.

- Evidence supporting infrastructure, dependency, failure, safeguard, recovery and graph assertions.

- Evidence needed to evaluate the 15 baseline critical gates.

- Evidence used by AIDCF and AI Trust Graph integrated decision packages.

- Human, machine, documentary, observational, test, operational and derived evidence.

## 4. Conformance levels

| **Level** | **Name**              | **Minimum expectation**                                                           |
|-----------|-----------------------|-----------------------------------------------------------------------------------|
| E0        | Vocabulary aligned    | Uses canonical evidence terms and source ownership.                               |
| E1        | Metadata complete     | Implements mandatory EvidenceObject fields.                                       |
| E2        | Provenance controlled | Adds source, collection, integrity, custody and classification.                   |
| E3        | Assertion linked      | Evaluates relevance, quality, freshness and coverage for precise assertions.      |
| E4        | Decision ready        | Supports sufficiency, confidence, gates, conflict, UNKNOWN and bounded decisions. |
| E5        | Machine conformant    | Passes schemas, validation shapes, versioning and audit tests.                    |

# Part II - Evidence doctrine and mandatory distinctions

## 5. Foundational doctrines

| **Doctrine**               | **Rule**                                                                              |
|----------------------------|---------------------------------------------------------------------------------------|
| Evidence before conclusion | No positive assurance conclusion without affirmative support.                         |
| Assertion specificity      | Evidence supports or challenges a precise proposition, not an object in the abstract. |
| Reality over intent        | Observed and tested evidence takes precedence where design intent conflicts.          |
| Bounded use                | Evidence applies only to stated scope, period, state, conditions and method.          |
| Independent review         | Collection, interpretation and decision authority remain distinguishable.             |
| Minimum false precision    | Scores express structured judgment but do not manufacture certainty.                  |
| Preserved uncertainty      | Missing, inaccessible, stale, conflicting or weak evidence remains visible.           |
| Non-inheritance            | Third-party certification or prior review is evidence, not automatic assurance.       |

## 6. Mandatory distinctions

| **Do not collapse**                              | **Reason**                                                                |
|--------------------------------------------------|---------------------------------------------------------------------------|
| Evidence Object / Evidence Package               | One item differs from a governed collection.                              |
| Source / Collector / Custodian / Reviewer        | Origin, acquisition, storage and judgment are different roles.            |
| Observation time / collection time / record time | The represented state may differ from acquisition or repository entry.    |
| Authenticity / integrity                         | Genuine origin differs from freedom from unauthorised alteration.         |
| Reliability / relevance                          | A reliable source may not support the claim.                              |
| Coverage / volume                                | Many records may still cover a narrow population or state.                |
| Quality / sufficiency                            | Strong evidence can still be insufficient in quantity or diversity.       |
| Evidence grade / confidence                      | Evidence characteristics differ from reviewer confidence in an assertion. |
| Stale / contradicting                            | Old evidence differs from current disagreement.                           |
| Independent / external                           | External does not necessarily mean impartial, competent or verified.      |
| Test result / effectiveness conclusion           | A test output requires scope and interpretation.                          |
| Derived evidence / source evidence               | Analysis does not replace its lineage sources.                            |

# Part III - Evidence metamodel and object hierarchy

## 7. Core evidence entities

| **Entity**             | **Definition**                                                                                      |
|------------------------|-----------------------------------------------------------------------------------------------------|
| EvidenceObject         | Smallest independently identified evidence item used to support, challenge or qualify an assertion. |
| EvidenceSet            | A purpose-specific selection of Evidence Objects used together for one assertion or test.           |
| EvidencePackage        | A governed collection addressing a control, function, system, scenario or gate.                     |
| EvidencePortfolio      | A capability-level collection of Evidence Packages and decision records.                            |
| EvidenceSource         | Person, system, device, provider, repository or process from which evidence originates.             |
| CollectionActivity     | Authorised action that acquires or observes evidence.                                               |
| TransformationActivity | Declared process deriving one evidence object from others.                                          |
| EvidenceRequirement    | Claim-specific statement of required types, quality, coverage, age and independence.                |
| EvidenceAssessment     | Recorded evaluation of evidence against a requirement.                                              |
| EvidenceManifest       | Machine-readable inventory with identifiers, hashes, locations and status.                          |
| CustodyEvent           | Transfer, access, export, alteration, redaction or retention action.                                |
| EvidenceConflict       | Structured disagreement between evidence-supported assertions.                                      |

## 8. Hierarchy

EvidencePortfolio -\> EvidencePackage -\> EvidenceSet -\> EvidenceObject -\> Source and Collection Activity -\> Assertion / Control / Gate / Decision

## 9. EvidenceObject lifecycle states

| **State**  | **Meaning**                                                              |
|------------|--------------------------------------------------------------------------|
| EXPECTED   | Evidence requirement identified but object not yet collected.            |
| REQUESTED  | Collection request issued.                                               |
| COLLECTED  | Object acquired but not quality reviewed.                                |
| VALIDATED  | Identity, provenance, integrity and readability reviewed.                |
| ACCEPTED   | Approved for one or more stated assurance uses.                          |
| CHALLENGED | Material concern or contradiction recorded.                              |
| STALE      | No longer sufficiently representative.                                   |
| RESTRICTED | Use limited by security, privacy, contract or legal hold.                |
| SUPERSEDED | Replaced by a later object while history remains.                        |
| REJECTED   | Not suitable for the stated use; rationale retained.                     |
| RETIRED    | No longer current but retained according to policy.                      |
| DESTROYED  | Disposed under authorised retention process; destruction record remains. |

## 10. Evidence Package minimum structure

| **Component**          | **Requirement**                                                           |
|------------------------|---------------------------------------------------------------------------|
| Package ID and purpose | Stable identity and decision/claim addressed.                             |
| Subject and boundary   | Capability, control, system, gate, state and period.                      |
| Requirement profile    | Required evidence classes, quality, coverage, freshness and independence. |
| Manifest               | Complete list of included, missing, substituted and restricted items.     |
| Assessments            | Per-object quality and package sufficiency results.                       |
| Conflicts and UNKNOWN  | Unresolved contradictions, gaps and decision effects.                     |
| Review and approval    | Collector, analyst, reviewer and decision roles.                          |
| Version and custody    | Immutable release, hash, access and supersession lineage.                 |

# Part IV - Evidence taxonomy and subtype catalogue

| **Class** | **Name**                          | **Representative subtypes**                                                                                                                  |
|-----------|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| E1        | Documentary and Declarative       | policy; standard; procedure; runbook; design basis; architecture; drawing; contract; attestation; inventory                                  |
| E2        | Configuration and Technical State | device configuration; firmware inventory; cluster manifest; access policy; protection setting; topology export; configuration snapshot       |
| E3        | Operational and Observational     | telemetry; log; alarm; event; ticket; work order; capacity metric; performance metric; physical observation; inspection record               |
| E4        | Validation and Test               | commissioning; load test; failover test; recovery test; simulation; scenario exercise; functional test; calibration; witnessed demonstration |
| E5        | Independent and Third-Party       | independent engineering review; audit; provider assurance; witnessed test; laboratory result; accredited certificate; regulatory inspection  |
| E6        | Human and Experiential            | interview; workshop; walkthrough; operator demonstration; expert judgment; shift observation; competency evidence                            |
| E7        | Derived and Analytical            | trend; correlation; capacity analysis; failure analysis; dependency path; reconciled inventory; score; model output; AI-assisted extraction  |

## E1 Documentary and Declarative

Best suited to intent, requirements, authority, design and declared process. It shall not alone prove current implementation or effectiveness.

| **Subtype family**          | **Examples**                                                                                                | **Primary claim supported**            |
|-----------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------|
| Documentary and Declarative | policy, standard, procedure, runbook, design basis, architecture, drawing, contract, attestation, inventory | intent, governance and approved design |

## E2 Configuration and Technical State

Best suited to implementation and technical-state assertions. It requires provenance, extraction context and reconciliation to the current architecture.

| **Subtype family**                | **Examples**                                                                                                                           | **Primary claim supported**        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| Configuration and Technical State | device configuration, firmware inventory, cluster manifest, access policy, protection setting, topology export, configuration snapshot | implementation and technical state |

## E3 Operational and Observational

Best suited to operation over a stated period. Coverage, completeness, clock integrity, gaps and collection health shall be assessed.

| **Subtype family**            | **Examples**                                                                                                                   | **Primary claim supported**          |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| Operational and Observational | telemetry, log, alarm, event, ticket, work order, capacity metric, performance metric, physical observation, inspection record | operation, performance and incidents |

## E4 Validation and Test

Best suited to effectiveness and resilience under stated conditions. Test authorization, initial state, method, expected result and anomalies shall be retained.

| **Subtype family**  | **Examples**                                                                                                                                 | **Primary claim supported**  |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| Validation and Test | commissioning, load test, failover test, recovery test, simulation, scenario exercise, functional test, calibration, witnessed demonstration | validation and effectiveness |

## E5 Independent and Third-Party

May strengthen independence but shall be evaluated for scope, competence, method, age, exclusions and transferability.

| **Subtype family**          | **Examples**                                                                                                                                | **Primary claim supported** |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Independent and Third-Party | independent engineering review, audit, provider assurance, witnessed test, laboratory result, accredited certificate, regulatory inspection | independent corroboration   |

## E6 Human and Experiential

Useful for context, operating practice and explanation. Corroboration is required for material technical-effectiveness assertions.

| **Subtype family**     | **Examples**                                                                                                      | **Primary claim supported**      |
|------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Human and Experiential | interview, workshop, walkthrough, operator demonstration, expert judgment, shift observation, competency evidence | practice, competence and context |

## E7 Derived and Analytical

Useful for synthesis and decision support. Derived outputs never exceed the quality, scope and lineage of their sources.

| **Subtype family**     | **Examples**                                                                                                                                | **Primary claim supported**         |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| Derived and Analytical | trend, correlation, capacity analysis, failure analysis, dependency path, reconciled inventory, score, model output, AI-assisted extraction | analysis and relationship synthesis |

# Part V - Evidence metadata standard

## 11. Mandatory metadata

| **Field**                         | **Requirement**                                                       |
|-----------------------------------|-----------------------------------------------------------------------|
| evidenceId                        | Immutable unique identifier.                                          |
| title                             | Concise human-readable name.                                          |
| description                       | What the item contains and why it exists.                             |
| evidenceClass/subtype             | Controlled E1-E7 classification.                                      |
| sourceId/sourceType               | Originating person, system, provider or process.                      |
| owner/custodian                   | Accountable owner and storage custodian.                              |
| collector/collectionMethod        | Who or what collected it, how and under which authority.              |
| observationTime                   | When the represented condition existed.                               |
| collectionTime                    | When the evidence was acquired.                                       |
| recordTime                        | When entered into the repository.                                     |
| effectivePeriod                   | Period for which the evidence is applicable.                          |
| subjectRefs                       | Capabilities, assets, controls, gates, assertions or paths addressed. |
| scope                             | Locations, systems, tenant, population and states covered.            |
| architecture/configurationVersion | Baseline represented.                                                 |
| integrityMethod/hash              | Integrity protection and digest where applicable.                     |
| format/version                    | File, record, schema and tool versions.                               |
| classification                    | Security/privacy/contractual handling category.                       |
| retentionRule                     | Retention period, trigger and legal hold.                             |
| qualityAssessment                 | Dimension ratings and rationale.                                      |
| reviewState/reviewer              | Candidate, accepted, challenged, rejected, stale or superseded.       |
| limitations                       | Known gaps, exclusions, sampling or interpretation limits.            |
| relatedEvidence                   | Sources, derivatives, conflicts, replacements and package membership. |

## 12. Conditional metadata

- Test evidence: initial state, expected result, procedure, authorization, abort criteria, instrumentation, anomalies and witnesses.

- Telemetry/log evidence: source clock, timezone, sampling interval, collection health, dropped data and query/filter.

- Configuration evidence: extraction command or interface, privilege used, configuration scope, redactions and target state.

- Human evidence: role, competence, interview protocol, date, corroboration and consent/recording status.

- External evidence: issuer, competence/accreditation where relevant, scope, validity, exclusions and permitted reliance.

- Derived evidence: source IDs, transformation code/query/version, assumptions, quality propagation and reviewer.

# Part VI - Provenance, integrity and chain of custody

## 13. Provenance model

| **Provenance object** | **Minimum content**                                               |
|-----------------------|-------------------------------------------------------------------|
| Entity                | Evidence object or source record.                                 |
| Activity              | Collection, observation, transformation, review or custody event. |
| Agent                 | Person, system, provider or organisation responsible.             |
| wasGeneratedBy        | Activity that produced the object.                                |
| wasDerivedFrom        | Source evidence and transformations.                              |
| wasAttributedTo       | Responsible source or owner.                                      |
| wasAssociatedWith     | Collector, reviewer or tool involved.                             |
| used                  | Source objects consumed by a transformation.                      |
| invalidatedAtTime     | When evidence became stale, superseded, withdrawn or destroyed.   |

## 14. Integrity levels

| **Level** | **Name**                   | **Anchor**                                                          |
|-----------|----------------------------|---------------------------------------------------------------------|
| I0        | Unknown                    | Integrity method absent or unverified.                              |
| I1        | Basic controlled           | Repository permissions and version history.                         |
| I2        | Verified copy              | Source comparison or controlled export metadata.                    |
| I3        | Hashed                     | Cryptographic digest recorded in manifest.                          |
| I4        | Signed / trusted timestamp | Digital signature or trusted timestamp validated.                   |
| I5        | Tamper-evident custody     | End-to-end signed custody, immutable storage or equivalent control. |

## 15. Chain-of-custody events

- Creation or acquisition.

- Transfer between collectors, custodians or repositories.

- Read/access for review.

- Transformation, parsing, redaction or export.

- Integrity verification.

- Challenge, correction or supersession.

- Legal hold, restriction, retention extension or authorised destruction.

**EVM-REQ-015** Every material transformation shall produce a new Evidence Object linked to source evidence; original evidence shall not be silently overwritten.

**EVM-REQ-016** Redaction shall preserve an unredacted controlled source where lawful and shall record the basis, method and affected content.

# Part VII - Evidence quality dimensions and grading

## 16. Quality dimensions

| **Code** | **Dimension** | **Question**                                                             |
|----------|---------------|--------------------------------------------------------------------------|
| P        | Provenance    | Can origin, authority and collection lineage be established?             |
| F        | Freshness     | Is the item sufficiently current and representative?                     |
| C        | Coverage      | Does it cover the required population, period, state and boundary?       |
| R        | Reliability   | Is the method/source repeatable, controlled and corroborated?            |
| T        | Traceability  | Can it be linked end to end to subject, assertion, control and decision? |
| I        | Integrity     | Is it protected against undetected alteration and custody loss?          |

## 17. Rating scale

### P rating anchors

| **Rating** | **Anchor**                                |
|------------|-------------------------------------------|
| P0         | Unknown origin                            |
| P1         | Identified but uncontrolled source        |
| P2         | Accountable internal source               |
| P3         | Controlled authoritative source           |
| P4         | Corroborated authoritative source         |
| P5         | Independently verified origin and lineage |

### F rating anchors

| **Rating** | **Anchor**                                              |
|------------|---------------------------------------------------------|
| F0         | Unknown age or state                                    |
| F1         | Obsolete for represented state                          |
| F2         | Stale or change-sensitive                               |
| F3         | Acceptable for decision                                 |
| F4         | Current and aligned to baseline                         |
| F5         | Near-real-time or event-current with healthy collection |

### C rating anchors

| **Rating** | **Anchor**                                           |
|------------|------------------------------------------------------|
| C0         | Unknown coverage                                     |
| C1         | Anecdotal or isolated                                |
| C2         | Limited sample/state                                 |
| C3         | Representative core scope                            |
| C4         | Broad scope and relevant states                      |
| C5         | Comprehensive declared population, period and states |

### R rating anchors

| **Rating** | **Anchor**                                    |
|------------|-----------------------------------------------|
| R0         | Unassessed                                    |
| R1         | Weak/uncontrolled method                      |
| R2         | Plausible but lightly corroborated            |
| R3         | Controlled repeatable method                  |
| R4         | Strong and independently corroborated         |
| R5         | Validated method and independent verification |

### T rating anchors

| **Rating** | **Anchor**                                    |
|------------|-----------------------------------------------|
| T0         | Unlinked                                      |
| T1         | Manual contextual link                        |
| T2         | Linked to subject or control                  |
| T3         | Linked to assertion, subject and period       |
| T4         | End-to-end to finding and gate                |
| T5         | End-to-end to decision with immutable lineage |

### I rating anchors

| **Rating** | **Anchor**                        |
|------------|-----------------------------------|
| I0         | Unknown integrity                 |
| I1         | Basic repository controls         |
| I2         | Verified source copy              |
| I3         | Hash verified                     |
| I4         | Signature/timestamp verified      |
| I5         | Tamper-evident end-to-end custody |

## 18. Evidence quality vector

Preferred expression: \[Class\]-P#-F#-C#-R#-T#-I#. Example: E4-P4-F4-C3-R4-T4-I3. The vector shall remain visible. A single averaged number may be used only as a secondary sorting aid and shall not replace the dimensions.

## 19. Evidence quality bands

| **Band**             | **Rule**                                                                               | **Permitted use**                                                             |
|----------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Q0 Unusable          | Any critical dimension P0, R0, T0 or I0 without accepted limitation.                   | Context only; no positive assertion.                                          |
| Q1 Weak              | Multiple dimensions 0-1 or unsupported source.                                         | Candidate/UNKNOWN; remediation priority.                                      |
| Q2 Limited           | Core provenance established but limited coverage/currentness/corroboration.            | Descriptive or limited implementation claim.                                  |
| Q3 Adequate          | All claim-critical dimensions at least 3.                                              | Design/implementation claim where appropriate.                                |
| Q4 Strong            | Most dimensions 4+, with no claim-critical dimension below 3.                          | Operating effectiveness with sufficient package coverage.                     |
| Q5 Highly defensible | Independent/corroborated, representative, current and traceable with strong integrity. | High-consequence gate or resilience claim, subject to method and sufficiency. |

# Part VIII - Freshness, validity, retention and legal hold

## 20. Freshness rule

Freshness is risk- and change-based. The windows below are default review triggers, not universal expiry. A material change invalidates representativeness even when the nominal window has not elapsed.

| **Evidence category**              | **Default currency basis**                                  | **Immediate invalidation/review triggers**                          |
|------------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------|
| Live telemetry and active alarms   | Current collection health; decision-specific lookback       | Collection outage, sensor/configuration change, incident.           |
| Event and security logs            | Usually current period and sufficient lookback for decision | Clock/source/query change, incident, retention gap.                 |
| Configuration snapshots            | At assessment and after material change                     | Firmware, policy, topology, identity or setpoint change.            |
| Capacity/performance metrics       | Current demand cycle and peak/seasonal state                | Expansion, workload shift, throttling or demand change.             |
| Maintenance/calibration records    | Current maintenance cycle                                   | Overdue work, failure, deferral or scope change.                    |
| Commissioning and validation tests | Until material change, adverse event or review trigger      | Architecture, load, firmware, procedure or provider change.         |
| Recovery and continuity exercises  | Risk-based periodic cycle and after material change         | Failure, failed exercise, new dependency or recovery design change. |
| Architecture/design documents      | Until superseded or material change                         | As-built discrepancy, expansion or reconfiguration.                 |
| Contracts/provider attestations    | Until expiry, renewal or service change                     | Provider, SLA, subprocessor or jurisdiction change.                 |
| Interviews and walkthroughs        | Point-in-time context                                       | Role/process change or contradictory technical evidence.            |

## 21. Retention classes

| **Class**                | **Purpose**                                                 | **Rule**                                                                                          |
|--------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| R0 Transient             | Temporary extraction or working copy.                       | Delete under controlled process after verified ingestion unless needed for decision traceability. |
| R1 Operational           | Routine monitoring and work records.                        | Retain for operational, contractual and investigation needs.                                      |
| R2 Assurance             | Assessment evidence and workpapers.                         | Retain through decision validity plus defined challenge/reassessment period.                      |
| R3 Critical decision     | Gate, resilience and high-consequence evidence.             | Longer risk-based retention with immutable lineage.                                               |
| R4 Legal/regulatory hold | Evidence subject to preservation obligation.                | No alteration/destruction until authorised release.                                               |
| R5 Canonical methodology | Schemas, mappings, approved examples and release artifacts. | Versioned permanent archive.                                                                      |

**EVM-REQ-021** Retention periods shall be defined by applicable legal, contractual, regulatory, security, privacy and operational requirements; this standard does not prescribe universal years.

# Part IX - Coverage, sampling and representativeness

## 22. Coverage dimensions

| **Dimension**    | **Coverage question**                                                   |
|------------------|-------------------------------------------------------------------------|
| Entity           | Which assets, systems, providers and interfaces are included?           |
| Population       | What proportion and which strata of the population are represented?     |
| Location         | Which sites, halls, zones, racks and jurisdictions?                     |
| Time             | Which period, season, demand cycle and incident window?                 |
| Operating state  | Normal, degraded, maintenance, emergency, recovery and transition?      |
| Scenario         | Which threat, hazard, failure, common-mode and recovery paths?          |
| Tenant/workload  | Which tenancy, cluster, workload or service outcomes?                   |
| Control behavior | Design, implementation, operation, monitoring, validation and recovery? |
| Dependency       | Which upstream, downstream, shared and external dependencies?           |

## 23. Sampling principles

- Sampling shall be risk-based, reproducible and documented.

- The population, strata, selection method, sample size rationale and exclusions shall be recorded.

- Judgmental sampling may target critical or anomalous items but shall not be represented as statistical coverage.

- Random or systematic sampling requires a trustworthy population frame.

- A sampled pass shall not be extrapolated beyond the represented population and conditions.

- Exceptions and failed samples shall influence expansion and conclusion.

## 24. Coverage rating

| **Level** | **Meaning**                                                                                    |
|-----------|------------------------------------------------------------------------------------------------|
| C0        | Population or scope unknown.                                                                   |
| C1        | Single example or anecdotal evidence.                                                          |
| C2        | Limited sample or one state.                                                                   |
| C3        | Representative core population and expected state.                                             |
| C4        | Broad population and material degraded/maintenance states.                                     |
| C5        | Comprehensive declared population, periods and applicable states, subject to practical limits. |

# Part X - Evidence sufficiency and confidence

## 25. Sufficiency model

Sufficiency is an assertion-specific judgment based on whether the combined evidence package meets required type diversity, quality floors, coverage, freshness, independence, conflict resolution and state/scenario representation. It shall not be calculated only from evidence count.

| **Level** | **Name**            | **Meaning**                                                                                                              |
|-----------|---------------------|--------------------------------------------------------------------------------------------------------------------------|
| S0        | None                | No usable evidence.                                                                                                      |
| S1        | Insufficient        | Some evidence exists but cannot support the claim.                                                                       |
| S2        | Minimum descriptive | Supports a bounded description or design intent.                                                                         |
| S3        | Reasonable          | Supports design or implementation within declared scope.                                                                 |
| S4        | Strong              | Supports operating effectiveness for representative conditions.                                                          |
| S5        | Highly defensible   | Supports high-consequence gate/resilience claim with diverse, current, traceable and appropriately independent evidence. |

## 26. Sufficiency decision factors

| **Factor**               | **Assessment**                                                                 |
|--------------------------|--------------------------------------------------------------------------------|
| Required class diversity | Are design, configuration, operation and validation types present as required? |
| Quality floor            | Does each mandatory item meet claim-specific minimums?                         |
| Complementarity          | Do items address different weaknesses rather than duplicate one source?        |
| Independence             | Are critical claims corroborated by an appropriately separate source/method?   |
| Coverage                 | Does the package represent population, state, time and scenario?               |
| Conflict                 | Are material contradictions resolved or bounded?                               |
| UNKNOWN                  | Are missing elements identified with decision effect?                          |
| Critical gate            | Does the package meet the declared non-compensating floor?                     |

## 27. Confidence states

| **State**        | **Meaning**                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------|
| CONF-0 UNKNOWN   | No defensible confidence state.                                                                 |
| CONF-1 Low       | Weak/limited evidence; high sensitivity to assumptions.                                         |
| CONF-2 Moderate  | Reasonable support with material limitations.                                                   |
| CONF-3 High      | Strong support with no unresolved material conflict within scope.                               |
| CONF-4 Very High | Highly defensible, independently corroborated and representative support for the bounded claim. |
| CONFLICTING      | Material evidence supports incompatible propositions.                                           |
| STALE            | Previously supported but no longer sufficiently current.                                        |

**EVM-REQ-027** Confidence shall be recorded with rationale and shall not be derived from a hidden formula.

**EVM-REQ-028** A confidence state shall not exceed the ceiling imposed by the weakest mandatory evidence requirement or critical UNKNOWN.

# Part XI - Evidence-to-assertion and finding model

## 28. Assertion structure

| **Field**           | **Requirement**                                                                                                |
|---------------------|----------------------------------------------------------------------------------------------------------------|
| assertionId         | Stable versioned identity.                                                                                     |
| proposition         | Subject-predicate-object or equivalent precise statement.                                                      |
| claimType           | Intent, design, implementation, operation, effectiveness, resilience, absence, compliance mapping or decision. |
| scope/conditions    | Capability, boundary, state, configuration, load, period and assumptions.                                      |
| evidenceRequirement | Required classes, quality floors, coverage and independence.                                                   |
| supportingEvidence  | Evidence Objects supporting proposition.                                                                       |
| challengingEvidence | Evidence Objects contradicting or weakening proposition.                                                       |
| qualifyingEvidence  | Evidence limiting scope or interpretation.                                                                     |
| assessment          | Quality, sufficiency, conflict and UNKNOWN evaluation.                                                         |
| confidence/review   | Controlled state, reviewer and date.                                                                           |
| decisionUse         | Findings, gate or decision that relies upon assertion.                                                         |

## 29. Claim-type evidence floors

| **Claim type**         | **Minimum pattern**                                                                                  |
|------------------------|------------------------------------------------------------------------------------------------------|
| Intent/governance      | E1 plus accountable approval and current applicability.                                              |
| Design suitability     | E1 design evidence plus competent technical analysis; E5 where required by authority or consequence. |
| Implemented            | E2 configuration/as-built evidence plus E3 or E6 observation; reconcile to design.                   |
| Operating              | E3 over representative period plus current E2 and exception/incident review.                         |
| Effective              | E4 representative validation plus E2/E3 supporting state and operating evidence.                     |
| Resilient/recoverable  | E4 scenario/recovery evidence plus cross-domain E2/E3 and dependency coverage.                       |
| Negative/absence claim | Documented discovery coverage, method sensitivity and residual UNKNOWN.                              |
| Independent assurance  | E5 scope and method plus access to underlying evidence where needed.                                 |
| Derived decision       | E7 with complete source lineage and human review.                                                    |

## 30. Finding model

| **Finding state** | **Evidence rule**                                                  |
|-------------------|--------------------------------------------------------------------|
| Observation       | Evidence describes a condition without determining control result. |
| Conforming        | Affirmative evidence meets requirement and sufficiency floor.      |
| Partial           | Some requirement elements or coverage are supported.               |
| Nonconforming     | Evidence demonstrates requirement not met.                         |
| UNKNOWN           | Evidence insufficient, inaccessible, stale or unresolved.          |
| Conflicting       | Material sources disagree.                                         |
| Not Applicable    | Approved evidence-based applicability rationale.                   |
| Suspended         | Change or expiry invalidates reliance on prior evidence.           |

# Part XII - Evidence-to-control mapping

## 31. Control evidence profile

Every AIDCF-007 control shall have an Evidence Requirement Profile. The profile is normative for evidence types and floors but may be strengthened by capability profile, criticality, scenario or decision need.

| **Field**              | **Meaning**                                                     |
|------------------------|-----------------------------------------------------------------|
| controlId              | AIDCF-007 control.                                              |
| claimType              | Design, implementation, operation, effectiveness or resilience. |
| requiredClasses        | Mandatory and optional E1-E7 classes.                           |
| qualityFloor           | Minimum P/F/C/R/T/I dimensions.                                 |
| sufficiencyFloor       | S0-S5.                                                          |
| stateCoverage          | Operating states to be represented.                             |
| periodCoverage         | Required period or risk-based window.                           |
| independence           | Required source/method separation.                              |
| mandatoryItems         | Non-substitutable evidence.                                     |
| acceptableAlternatives | Equivalent evidence with rationale.                             |
| unknownEffect          | Decision or gate consequence.                                   |
| reassessmentTrigger    | Evidence invalidation conditions.                               |

## 32. Control profile tiers

| **Tier**                 | **Use**                                                       | **Minimum evidence pattern**                                          |
|--------------------------|---------------------------------------------------------------|-----------------------------------------------------------------------|
| CP-1 Foundational        | Governance, inventory, design intent.                         | E1 plus accountable source; S2/S3.                                    |
| CP-2 Technical state     | Configuration, topology and implementation.                   | E1+E2 with observation/reconciliation; S3.                            |
| CP-3 Operational         | Operation, monitoring and maintenance.                        | E2+E3 across representative period; S3/S4.                            |
| CP-4 Effectiveness       | Controls tested under defined conditions.                     | E2+E3+E4; S4.                                                         |
| CP-5 Critical/resilience | Critical gate, compound scenario or high-consequence outcome. | Diverse E1-E4 and appropriate E5; S5 or profile-defined strong floor. |

# Part XIII - Critical-gate evidence profiles

| **Gate** | **Name**                                          | **Mandatory evidence profile**                                                                                       | **Classes** | **Floor** | **Decision effect**                                                                 |
|----------|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------|-----------|-------------------------------------------------------------------------------------|
| CG-01    | Capability and outcome definition                 | Capability register; approved outcomes; criticality and tolerance analysis; architecture linkage                     | E1+E7       | S3        | UNKNOWN capability/outcome blocks positive capability assurance.                    |
| CG-02    | Boundary and architecture integrity               | Approved boundary; current architecture; as-built/configuration reconciliation; exclusions and external dependencies | E1+E2+E6    | S3        | Unclear material boundary blocks final conclusion.                                  |
| CG-03    | Critical dependency visibility                    | Dependency graph; source/route/provider evidence; common-mode analysis; ownership                                    | E1+E2+E7    | S4        | Critical hidden dependency remains UNKNOWN or Fail if demonstrated absent.          |
| CG-04    | Life safety and hazardous energy                  | Authorised engineering/safety records; inspection; permits; tests; unresolved hazard status                          | E1+E4+E5    | S4        | Unsafe unresolved condition blocks relevant assurance/testing.                      |
| CG-05    | Resilient electrical supply                       | SLD; protection/capacity study; UPS/generator tests; fuel; maintenance; EPMS/incident evidence                       | E1+E2+E3+E4 | S5        | Missing critical continuity evidence -\> UNKNOWN; demonstrated inability -\> Fail.  |
| CG-06    | Thermal continuity                                | Thermal design/model; P&ID; capacity/flow telemetry; leak/transfer/failover tests; maintenance                       | E1+E2+E3+E4 | S5        | Unverified critical heat-removal path -\> UNKNOWN; demonstrated shortfall -\> Fail. |
| CG-07    | Critical control-system integrity                 | BMS/EPMS/controller architecture; configuration; identity/authority; telemetry; fail-safe tests                      | E1+E2+E3+E4 | S4        | Uncontrolled or unverifiable critical automation limits/blocks assurance.           |
| CG-08    | Compute, storage and network functional integrity | Current topology/configuration; capacity/performance telemetry; error data; failover/recovery tests                  | E2+E3+E4    | S4        | Unverified critical infrastructure function caps operating/resilience assurance.    |
| CG-09    | Failure containment                               | Fault-domain model; isolation design; scenario analysis; containment tests/incidents                                 | E1+E2+E4+E7 | S4        | Absent/failed containment may be Fail; untested critical boundary is UNKNOWN.       |
| CG-10    | Recovery readiness                                | Recovery plan; prerequisites; configuration/data sources; exercises/tests; defects and signoff                       | E1+E2+E3+E4 | S5        | Plan without representative test supports design only, not recoverability.          |
| CG-11    | Evidence sufficiency                              | Evidence requirements; manifest; quality/sufficiency assessments; conflicts and limitations                          | E1+E7       | S4        | Failure to meet evidence floor blocks the dependent claim.                          |
| CG-12    | Critical UNKNOWN                                  | UNKNOWN register; consequence; resolution ownership; evidence requests; decision ceiling                             | E1+E7       | S3        | Unresolved critical UNKNOWN caps, conditions, suspends or blocks assurance.         |
| CG-13    | Responsibility and authority                      | RACI; delegations; owner/operator/provider clauses; escalation; decision authority                                   | E1+E6       | S3        | Unowned critical function/dependency blocks accountable disposition.                |
| CG-14    | Change control                                    | Baseline; change request; impact analysis; test/rollback; approval; post-change validation                           | E1+E2+E3+E4 | S4        | Material uncontrolled change suspends affected evidence/decision.                   |
| CG-15    | Integrated digital authority                      | Identity and privilege records; reachability; control-plane interfaces; session logs; action/rollback tests          | E2+E3+E4+E7 | S4        | Unverified consequential authority remains critical UNKNOWN.                        |

**EVM-REQ-033** Evidence for a critical gate shall not be substituted below its mandatory type or quality floor merely to produce a complete scorecard.

# Part XIV - Conflict, contradiction and UNKNOWN

## 33. Evidence relationship states

| **State**      | **Meaning**                                                  |
|----------------|--------------------------------------------------------------|
| SUPPORTS       | Evidence increases support for a precise assertion.          |
| CHALLENGES     | Evidence weakens or contradicts assertion.                   |
| QUALIFIES      | Evidence narrows scope or conditions.                        |
| INCOMPLETE     | Evidence covers only part of requirement.                    |
| STALE          | Evidence no longer represents current state.                 |
| INACCESSIBLE   | Evidence is believed to exist but cannot be reviewed.        |
| UNVERIFIED     | Origin, integrity or method is not sufficiently established. |
| SUPERSEDES     | New object replaces current use while preserving history.    |
| DUPLICATES     | Same underlying source is represented more than once.        |
| CONFLICTS_WITH | Two supported propositions are materially incompatible.      |

## 34. Conflict workflow

Detect -\> register separate assertions -\> preserve both evidence lineages -\> assess scope/time/state differences -\> seek corroboration -\> competent review -\> resolve, bound or escalate -\> update decision while preserving history

## 35. UNKNOWN categories

| **Code** | **Category**              | **Definition**                                                   |
|----------|---------------------------|------------------------------------------------------------------|
| U1       | Missing                   | Expected evidence not produced.                                  |
| U2       | Inaccessible              | Evidence exists but access is restricted or unavailable.         |
| U3       | Stale                     | Evidence does not represent current state.                       |
| U4       | Conflicting               | Material sources disagree.                                       |
| U5       | Coverage gap              | Required population, state, period or scenario not represented.  |
| U6       | Source unverified         | Origin/authority cannot be established.                          |
| U7       | Integrity uncertain       | Alteration or custody cannot be ruled out.                       |
| U8       | Method uncertain          | Collection/test method insufficiently defined.                   |
| U9       | Interpretation unresolved | Competent reviewers cannot yet determine meaning.                |
| U10      | Dependency unknown        | Evidence cannot establish a material external/shared dependency. |

**EVM-REQ-035** Each UNKNOWN shall identify subject, missing attribute, reason, potential consequence, evidence needed, owner if known, status and decision/gate impact.

# Part XV - Derived, automated and AI-generated evidence

## 36. Derived evidence rules

- Retain every source Evidence ID and the transformation method.

- Record query, script, model, parameters, assumptions and version.

- Do not assign a quality dimension higher than source support without independent corroboration relevant to that dimension.

- Distinguish deterministic transformation from interpretive inference.

- Preserve failed, excluded and conflicting source records where material.

- Recalculate or invalidate derived evidence when a source changes or is withdrawn.

## 37. AI-assisted evidence

| **Use**                   | **Permitted status**      | **Required safeguards**                                                  |
|---------------------------|---------------------------|--------------------------------------------------------------------------|
| Classification/extraction | Candidate                 | Source link, model/version, prompt/process record, review and sampling.  |
| Summarisation             | Candidate workpaper       | Traceable citations to source passages and reviewer verification.        |
| Anomaly detection         | Signal/candidate          | Baseline, sensitivity, false-positive/negative review and corroboration. |
| Path inference            | Candidate graph assertion | Approved semantics, source evidence and accountable human review.        |
| Quality scoring           | Recommendation            | Transparent inputs/rules and override rationale.                         |
| Final finding/decision    | Not autonomous            | Competent accountable human approval required.                           |

**EVM-REQ-037** AI-generated text or graph content shall not be treated as independent corroboration of the source data from which it was generated.

# Part XVI - Evidence lifecycle and review workflow

## 38. Lifecycle

Plan -\> Request -\> Collect -\> Identify -\> Validate -\> Classify -\> Protect -\> Assess Quality -\> Link to Assertion -\> Assess Sufficiency -\> Review Conflict/UNKNOWN -\> Accept or Reject -\> Use in Decision -\> Monitor Freshness -\> Supersede/Retain/Destroy

## 39. Role model

| **Role**                        | **Responsibility**                                               |
|---------------------------------|------------------------------------------------------------------|
| Evidence owner                  | Accountable for source availability, quality and authorised use. |
| Collector                       | Acquires evidence under approved method and records provenance.  |
| Custodian                       | Protects, versions, retains and controls access.                 |
| Technical specialist            | Evaluates engineering or technical meaning.                      |
| Assessor                        | Links evidence to criteria and assertions.                       |
| Independent reviewer            | Challenges sufficiency, conflict and decision use.               |
| Decision owner                  | Authorises bounded conclusion and conditions.                    |
| Privacy/security/legal reviewer | Determines handling, redaction, disclosure and hold obligations. |
| Tool/system owner               | Maintains collection and transformation integrity.               |

## 40. Evidence request record

| **Field**                  | **Content**                                            |
|----------------------------|--------------------------------------------------------|
| requestId                  | Stable identifier.                                     |
| decision/assertion/control | Why evidence is required.                              |
| requested type/floor       | Classes, metadata, quality, period, state and format.  |
| source/owner               | Expected provider and accountable owner.               |
| authority/purpose          | Permitted collection and use.                          |
| due/review trigger         | Operational scheduling field.                          |
| received/status            | Collected, partial, inaccessible, rejected or UNKNOWN. |
| handling                   | Classification, transfer and retention.                |
| substitution               | Alternative evidence and approval rationale.           |
| escalation                 | Decision and gate effect of non-production.            |

# Part XVII - Evidence security, privacy and disclosure

## 41. Classification levels

| **Level**         | **Examples**                                                                | **Handling intent**                                         |
|-------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| PUBLIC            | Published methodology, synthetic examples.                                  | Approved public release.                                    |
| INTERNAL          | General workpapers and non-sensitive procedures.                            | Authenticated organisational access.                        |
| CONFIDENTIAL      | Client architecture, contracts, findings and operational records.           | Need-to-know, encryption, restricted export.                |
| RESTRICTED        | Facility layouts, configurations, identities, routes and security evidence. | Strong access approval, logging and controlled sharing.     |
| HIGHLY RESTRICTED | Combined physical/digital paths, secrets, live control authority.           | Segregated storage, minimal access and sanitised reporting. |
| LEGAL HOLD        | Any evidence under preservation obligation.                                 | No deletion or unapproved alteration.                       |

## 42. Security and privacy requirements

**EVM-SEC-001** Collect only evidence necessary for the authorised assurance purpose.

**EVM-SEC-002** Secrets and reusable credentials shall not be stored as ordinary evidence values.

**EVM-SEC-003** Evidence access, export, redaction and deletion shall be auditable for restricted classes.

**EVM-SEC-004** Personal data shall be minimised, lawfully handled and retained only as justified.

**EVM-SEC-005** Cross-tenant and cross-client evidence shall remain isolated.

**EVM-SEC-006** Reports may abstract sensitive details while retaining stable traceability to protected evidence.

**EVM-SEC-007** Evidence used across jurisdictions shall identify location, transfer and access restrictions.

# Part XVIII - Graph-native and machine-readable model

## 43. Core graph nodes

| **Node**               | **Purpose**                               |
|------------------------|-------------------------------------------|
| EvidenceObject         | Addressable source item.                  |
| EvidenceSet            | Assertion-specific collection.            |
| EvidencePackage        | Control/system/gate package.              |
| EvidencePortfolio      | Capability-level evidence collection.     |
| EvidenceRequirement    | Required type and threshold.              |
| EvidenceAssessment     | Quality and sufficiency judgment.         |
| EvidenceSource         | Originating system/person/provider.       |
| CollectionActivity     | Acquisition event.                        |
| TransformationActivity | Derived evidence process.                 |
| CustodyEvent           | Access/transfer/change event.             |
| Assertion              | Proposition supported/challenged.         |
| UnknownRecord          | Missing or unresolved evidence condition. |
| EvidenceConflict       | Contradictory evidence relationship.      |
| ReviewRecord           | Human challenge/approval.                 |
| Decision               | Bounded assurance output.                 |

## 44. Core graph relationships

| **Predicate**         | **Meaning**                                         |
|-----------------------|-----------------------------------------------------|
| SUPPORTS              | Evidence supports a precise assertion.              |
| CHALLENGES            | Evidence weakens or contradicts assertion.          |
| QUALIFIES             | Evidence limits scope/conditions.                   |
| SATISFIES_REQUIREMENT | Evidence package meets requirement.                 |
| COLLECTED_BY          | Object acquired by agent/tool.                      |
| GENERATED_BY          | Object produced by activity.                        |
| DERIVED_FROM          | Derived object traces to source.                    |
| OBSERVES              | Evidence records an entity/state.                   |
| COVERS                | Evidence covers scope, state, period or population. |
| VALIDATES             | Test evidence evaluates a safeguard or claim.       |
| CONFLICTS_WITH        | Objects/assertions materially disagree.             |
| SUPERSEDES            | New object replaces current use.                    |
| MEMBER_OF             | Object belongs to set/package/portfolio.            |
| CUSTODIAN_OF          | Party holds custody.                                |
| LIMITS                | UNKNOWN/limitation constrains conclusion.           |
| EVIDENCES_GATE        | Package contributes to gate result.                 |

## 45. Publication package

| **File**                           | **Purpose**                                          |
|------------------------------------|------------------------------------------------------|
| aidcf-evm-v1.0.owl                 | Formal evidence ontology.                            |
| aidcf-evm-v1.0.ttl                 | RDF/Turtle serialisation.                            |
| aidcf-evm-context-v1.0.jsonld      | JSON-LD context.                                     |
| evidence-object-schema-v1.0.json   | EvidenceObject exchange schema.                      |
| evidence-package-schema-v1.0.json  | Package/portfolio schema.                            |
| aidcf-evm-shapes-v1.0.ttl          | SHACL validation shapes.                             |
| evidence-types-v1.0.csv            | Type registry.                                       |
| quality-ratings-v1.0.csv           | Quality dimension anchors.                           |
| control-evidence-profiles-v1.0.csv | AIDCF-007 mapping matrix.                            |
| critical-gate-evidence-v1.0.csv    | Gate profile matrix.                                 |
| retention-classes-v1.0.csv         | Retention definitions.                               |
| conformance-tests/                 | Positive, negative, migration and security fixtures. |
| CHANGELOG.md / MIGRATION.md        | Version history and transition guidance.             |

# Part XIX - Conformance, validation and nonconformance

## 46. Validation rules

| **Rule**    | **Validation statement**                                                                                     |
|-------------|--------------------------------------------------------------------------------------------------------------|
| EVM-VAL-001 | Every EvidenceObject has stable ID, class, source, scope, observation time, classification and review state. |
| EVM-VAL-002 | Every accepted material EvidenceObject links to at least one assertion or requirement.                       |
| EVM-VAL-003 | Every derived object links to sources and transformation activity.                                           |
| EVM-VAL-004 | Every quality rating has rationale and reviewer.                                                             |
| EVM-VAL-005 | Every evidence package evaluates freshness, coverage, conflict and sufficiency.                              |
| EVM-VAL-006 | Every critical-gate result references its evidence requirement and package.                                  |
| EVM-VAL-007 | Every missing mandatory item creates UNKNOWN or explicit adverse result.                                     |
| EVM-VAL-008 | No UNKNOWN is encoded as favourable pass or numeric zero.                                                    |
| EVM-VAL-009 | No evidence item is treated as universal proof across unreviewed assertions.                                 |
| EVM-VAL-010 | Every stale/superseded object remains historically traceable.                                                |
| EVM-VAL-011 | Every restricted item has handling and access metadata.                                                      |
| EVM-VAL-012 | Every AI-generated assertion remains candidate until approved.                                               |
| EVM-VAL-013 | Every evidence deletion has authorised destruction record unless prohibited by hold.                         |
| EVM-VAL-014 | Every test evidence object records initial state, method, conditions and anomalies.                          |
| EVM-VAL-015 | Every assurance decision links to an immutable evidence manifest or snapshot.                                |

## 47. Evidence nonconformance classes

| **Class**   | **Examples**                                                                                                                         | **Decision treatment**                                                                         |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Critical    | Fabricated/falsified evidence; concealed material conflict; unsafe unauthorised collection; custody breach affecting critical claim. | Stop use, preserve records, escalate, independently investigate and suspend affected decision. |
| Major       | Missing provenance; unsupported effectiveness; stale critical evidence; incomplete gate package; hidden UNKNOWN.                     | Reject/limit evidence and reassess conclusion.                                                 |
| Minor       | Non-material metadata defect or formatting inconsistency.                                                                            | Correct and record.                                                                            |
| Observation | Improvement opportunity without current decision impact.                                                                             | Track through quality process.                                                                 |

# Part XX - Worked evidence packages

## 48. Power continuity package

| **Component**   | **Example**                                                                          |
|-----------------|--------------------------------------------------------------------------------------|
| Assertions      | Required power continuity and resilient capacity exist for declared load/states.     |
| E1              | SLD, design basis, protection/capacity study, switching and fuel procedures.         |
| E2              | Protection settings, UPS/generator/EPMS configuration, asset inventory.              |
| E3              | Load, runtime, fuel, alarms, maintenance and incident evidence.                      |
| E4              | Generator start/transfer, UPS runtime, load-step and restoration tests.              |
| E5              | Independent engineering/witness review where required.                               |
| Quality focus   | Current load/configuration, representative states, shared dependencies, test safety. |
| Gate            | CG-05; evidence floor S5 or profile-defined strong floor.                            |
| UNKNOWN example | Unverified shared bus or fuel replenishment autonomy.                                |
| Decision limit  | No resilience conclusion beyond tested load, duration and states.                    |

## 49. Liquid cooling package

| **Component**   | **Example**                                                                        |
|-----------------|------------------------------------------------------------------------------------|
| Assertions      | Heat removal remains within envelope under normal and defined degraded states.     |
| E1              | P&ID, thermal model, design limits, water/coolant specification.                   |
| E2              | CDU, controller, setpoint, sensor and loop configuration.                          |
| E3              | Flow, temperature, pressure, leak, quality and alarm telemetry.                    |
| E4              | Failover, isolation, leak response and thermal recovery test.                      |
| E5              | Specialist engineering review for high-consequence or novel architecture.          |
| Quality focus   | Sensor trust, seasonal condition, transient response and shared loop dependencies. |
| Gate            | CG-06.                                                                             |
| UNKNOWN example | Secondary-loop autonomy not verified at peak load.                                 |
| Decision limit  | No generalisation from steady low load to full transient AI demand.                |

## 50. Compute-storage-network package

| **Component**   | **Example**                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------|
| Assertions      | Required usable performance, integrity and recovery are sustained for defined service outcomes. |
| E1              | Cluster/fabric/storage architecture and compatibility basis.                                    |
| E2              | Firmware, driver, topology, scheduler and storage configurations.                               |
| E3              | GPU errors, fabric congestion, storage performance, capacity and incident records.              |
| E4              | Benchmark, node/fabric failure, checkpoint and restore tests.                                   |
| E5              | Independent validation where required.                                                          |
| Quality focus   | Representative workload, topology version, error gaps and failure-domain coverage.              |
| Gate            | CG-08 and CG-10.                                                                                |
| UNKNOWN example | Checkpoint recovery not tested after correlated metadata/fabric disruption.                     |
| Decision limit  | Performance evidence does not prove recovery or integrity unless directly assessed.             |

## 51. Digital authority over infrastructure

| **Component**   | **Example**                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------|
| Assertions      | Only approved identities can cause consequential infrastructure actions within stated conditions. |
| E1              | Access policy, responsibility and remote-support process.                                         |
| E2              | Identity, role, permission, gateway and controller configuration.                                 |
| E3              | Authentication, session, command, change and revocation logs.                                     |
| E4              | Authorised access-path, command restriction and revocation tests.                                 |
| E7              | Integrated authority-path analysis using Artifact 005 semantics.                                  |
| Quality focus   | Effective identity, inherited privilege, dormant routes, provider access and rollback.            |
| Gate            | CG-15.                                                                                            |
| UNKNOWN example | Remote OEM command scope cannot be independently verified.                                        |
| Decision limit  | Reachability alone does not prove authority or realised physical effect.                          |

# Appendix A - Evidence type registry

| **Subtype ID** | **Class** | **Preferred label**                      | **Rule**                                                                            |
|----------------|-----------|------------------------------------------|-------------------------------------------------------------------------------------|
| E1-01          | E1        | Policy                                   | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E1-02          | E1        | Standard                                 | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E1-03          | E1        | Procedure                                | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E1-04          | E1        | Runbook                                  | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E1-05          | E1        | Design Basis                             | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E1-06          | E1        | Architecture Diagram                     | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E1-07          | E1        | Single-Line Diagram                      | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E1-08          | E1        | P&ID                                     | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E1-09          | E1        | As-Built Drawing                         | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E1-10          | E1        | Contract                                 | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E1-11          | E1        | SLA                                      | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E1-12          | E1        | Attestation                              | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E1-13          | E1        | Inventory                                | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E1-14          | E1        | Risk Record                              | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E2-01          | E2        | Device Configuration                     | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E2-02          | E2        | Protection Setting                       | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E2-03          | E2        | Firmware Baseline                        | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E2-04          | E2        | Driver Matrix                            | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E2-05          | E2        | Cluster Manifest                         | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E2-06          | E2        | Scheduler Policy                         | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E2-07          | E2        | Access Policy                            | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E2-08          | E2        | Topology Export                          | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E2-09          | E2        | Controller Logic                         | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E2-10          | E2        | Configuration Snapshot                   | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E2-11          | E2        | Golden Image                             | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E3-01          | E3        | Telemetry Series                         | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E3-02          | E3        | Event Log                                | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E3-03          | E3        | Alarm Record                             | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E3-04          | E3        | Capacity Metric                          | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E3-05          | E3        | Performance Metric                       | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E3-06          | E3        | Work Order                               | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E3-07          | E3        | Maintenance Record                       | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E3-08          | E3        | Incident Record                          | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E3-09          | E3        | Change Record                            | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E3-10          | E3        | Access Log                               | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E3-11          | E3        | Video/Photo Observation                  | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E3-12          | E3        | Inspection Record                        | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E4-01          | E4        | Commissioning Test                       | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E4-02          | E4        | Functional Test                          | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E4-03          | E4        | Load Test                                | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E4-04          | E4        | Failover Test                            | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E4-05          | E4        | Recovery Test                            | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E4-06          | E4        | Scenario Exercise                        | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E4-07          | E4        | Simulation                               | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E4-08          | E4        | Calibration Result                       | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E4-09          | E4        | Witnessed Demonstration                  | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E4-10          | E4        | Penetration/Control Test when authorised | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E5-01          | E5        | Independent Engineering Review           | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E5-02          | E5        | Third-Party Assessment                   | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E5-03          | E5        | Audit Report                             | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E5-04          | E5        | Accredited Certificate                   | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E5-05          | E5        | Laboratory Result                        | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E5-06          | E5        | Provider Assurance Report                | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E5-07          | E5        | Regulatory Inspection                    | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E5-08          | E5        | Independent Witness Record               | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E6-01          | E6        | Interview Record                         | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E6-02          | E6        | Workshop Record                          | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E6-03          | E6        | Walkthrough                              | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E6-04          | E6        | Operator Demonstration                   | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E6-05          | E6        | Expert Judgment                          | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E6-06          | E6        | Shift Observation                        | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E6-07          | E6        | Competency Record                        | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E6-08          | E6        | Training Record                          | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E7-01          | E7        | Trend Analysis                           | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E7-02          | E7        | Correlation Analysis                     | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E7-03          | E7        | Capacity Model                           | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E7-04          | E7        | Failure Analysis                         | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E7-05          | E7        | Dependency Graph                         | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E7-06          | E7        | Reconciled Inventory                     | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E7-07          | E7        | Evidence Quality Assessment              | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E7-08          | E7        | Score/Rating Output                      | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E7-09          | E7        | AI-Assisted Extraction                   | Controlled subtype; profile may add narrower terms without redefining parent class. |
| E7-10          | E7        | Query Result                             | Controlled subtype; profile may add narrower terms without redefining parent class. |

# Appendix B - Quality scoring anchors

## P

| **Rating** | **Anchor**                                |
|------------|-------------------------------------------|
| P0         | Unknown origin                            |
| P1         | Identified but uncontrolled source        |
| P2         | Accountable internal source               |
| P3         | Controlled authoritative source           |
| P4         | Corroborated authoritative source         |
| P5         | Independently verified origin and lineage |

## F

| **Rating** | **Anchor**                                              |
|------------|---------------------------------------------------------|
| F0         | Unknown age or state                                    |
| F1         | Obsolete for represented state                          |
| F2         | Stale or change-sensitive                               |
| F3         | Acceptable for decision                                 |
| F4         | Current and aligned to baseline                         |
| F5         | Near-real-time or event-current with healthy collection |

## C

| **Rating** | **Anchor**                                           |
|------------|------------------------------------------------------|
| C0         | Unknown coverage                                     |
| C1         | Anecdotal or isolated                                |
| C2         | Limited sample/state                                 |
| C3         | Representative core scope                            |
| C4         | Broad scope and relevant states                      |
| C5         | Comprehensive declared population, period and states |

## R

| **Rating** | **Anchor**                                    |
|------------|-----------------------------------------------|
| R0         | Unassessed                                    |
| R1         | Weak/uncontrolled method                      |
| R2         | Plausible but lightly corroborated            |
| R3         | Controlled repeatable method                  |
| R4         | Strong and independently corroborated         |
| R5         | Validated method and independent verification |

## T

| **Rating** | **Anchor**                                    |
|------------|-----------------------------------------------|
| T0         | Unlinked                                      |
| T1         | Manual contextual link                        |
| T2         | Linked to subject or control                  |
| T3         | Linked to assertion, subject and period       |
| T4         | End-to-end to finding and gate                |
| T5         | End-to-end to decision with immutable lineage |

## I

| **Rating** | **Anchor**                        |
|------------|-----------------------------------|
| I0         | Unknown integrity                 |
| I1         | Basic repository controls         |
| I2         | Verified source copy              |
| I3         | Hash verified                     |
| I4         | Signature/timestamp verified      |
| I5         | Tamper-evident end-to-end custody |

# Appendix C - Control evidence profile matrix

The 360-control evidence profile matrix is maintained in the AIDCF-007 companion catalogue and shall be published as control-evidence-profiles-v1.0.csv.

# Appendix D - Critical-gate evidence matrix

| **Gate** | **Name**                                          | **Mandatory evidence**                                                                                               | **Classes** | **Floor** | **Decision effect**                                                                 |
|----------|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------|-----------|-------------------------------------------------------------------------------------|
| CG-01    | Capability and outcome definition                 | Capability register; approved outcomes; criticality and tolerance analysis; architecture linkage                     | E1+E7       | S3        | UNKNOWN capability/outcome blocks positive capability assurance.                    |
| CG-02    | Boundary and architecture integrity               | Approved boundary; current architecture; as-built/configuration reconciliation; exclusions and external dependencies | E1+E2+E6    | S3        | Unclear material boundary blocks final conclusion.                                  |
| CG-03    | Critical dependency visibility                    | Dependency graph; source/route/provider evidence; common-mode analysis; ownership                                    | E1+E2+E7    | S4        | Critical hidden dependency remains UNKNOWN or Fail if demonstrated absent.          |
| CG-04    | Life safety and hazardous energy                  | Authorised engineering/safety records; inspection; permits; tests; unresolved hazard status                          | E1+E4+E5    | S4        | Unsafe unresolved condition blocks relevant assurance/testing.                      |
| CG-05    | Resilient electrical supply                       | SLD; protection/capacity study; UPS/generator tests; fuel; maintenance; EPMS/incident evidence                       | E1+E2+E3+E4 | S5        | Missing critical continuity evidence -\> UNKNOWN; demonstrated inability -\> Fail.  |
| CG-06    | Thermal continuity                                | Thermal design/model; P&ID; capacity/flow telemetry; leak/transfer/failover tests; maintenance                       | E1+E2+E3+E4 | S5        | Unverified critical heat-removal path -\> UNKNOWN; demonstrated shortfall -\> Fail. |
| CG-07    | Critical control-system integrity                 | BMS/EPMS/controller architecture; configuration; identity/authority; telemetry; fail-safe tests                      | E1+E2+E3+E4 | S4        | Uncontrolled or unverifiable critical automation limits/blocks assurance.           |
| CG-08    | Compute, storage and network functional integrity | Current topology/configuration; capacity/performance telemetry; error data; failover/recovery tests                  | E2+E3+E4    | S4        | Unverified critical infrastructure function caps operating/resilience assurance.    |
| CG-09    | Failure containment                               | Fault-domain model; isolation design; scenario analysis; containment tests/incidents                                 | E1+E2+E4+E7 | S4        | Absent/failed containment may be Fail; untested critical boundary is UNKNOWN.       |
| CG-10    | Recovery readiness                                | Recovery plan; prerequisites; configuration/data sources; exercises/tests; defects and signoff                       | E1+E2+E3+E4 | S5        | Plan without representative test supports design only, not recoverability.          |
| CG-11    | Evidence sufficiency                              | Evidence requirements; manifest; quality/sufficiency assessments; conflicts and limitations                          | E1+E7       | S4        | Failure to meet evidence floor blocks the dependent claim.                          |
| CG-12    | Critical UNKNOWN                                  | UNKNOWN register; consequence; resolution ownership; evidence requests; decision ceiling                             | E1+E7       | S3        | Unresolved critical UNKNOWN caps, conditions, suspends or blocks assurance.         |
| CG-13    | Responsibility and authority                      | RACI; delegations; owner/operator/provider clauses; escalation; decision authority                                   | E1+E6       | S3        | Unowned critical function/dependency blocks accountable disposition.                |
| CG-14    | Change control                                    | Baseline; change request; impact analysis; test/rollback; approval; post-change validation                           | E1+E2+E3+E4 | S4        | Material uncontrolled change suspends affected evidence/decision.                   |
| CG-15    | Integrated digital authority                      | Identity and privilege records; reachability; control-plane interfaces; session logs; action/rollback tests          | E2+E3+E4+E7 | S4        | Unverified consequential authority remains critical UNKNOWN.                        |

# Appendix E - Record schemas

## E.1 EvidenceObject

| **Property**         | **Cardinality** | **Type**                              |
|----------------------|-----------------|---------------------------------------|
| evidenceId           | 1               | Controlled value or referenced object |
| title                | 1               | Controlled value or referenced object |
| description          | 0..1 / 0..\*    | Controlled value or referenced object |
| evidenceClass        | 1               | Controlled value or referenced object |
| subtype              | 0..1 / 0..\*    | Controlled value or referenced object |
| sourceId             | 1               | Controlled value or referenced object |
| owner                | 0..1 / 0..\*    | Controlled value or referenced object |
| collector            | 0..1 / 0..\*    | Controlled value or referenced object |
| collectionMethod     | 0..1 / 0..\*    | Controlled value or referenced object |
| observationTime      | 1               | Controlled value or referenced object |
| collectionTime       | 0..1 / 0..\*    | Controlled value or referenced object |
| effectivePeriod      | 0..1 / 0..\*    | Controlled value or referenced object |
| subjectRefs          | 0..1 / 0..\*    | Controlled value or referenced object |
| scope                | 0..1 / 0..\*    | Controlled value or referenced object |
| configurationVersion | 0..1 / 0..\*    | Controlled value or referenced object |
| integrityMethod      | 0..1 / 0..\*    | Controlled value or referenced object |
| hash                 | 0..1 / 0..\*    | Controlled value or referenced object |
| classification       | 1               | Controlled value or referenced object |
| retentionRule        | 0..1 / 0..\*    | Controlled value or referenced object |
| qualityAssessment    | 0..1 / 0..\*    | Controlled value or referenced object |
| reviewState          | 1               | Controlled value or referenced object |
| limitations          | 0..1 / 0..\*    | Controlled value or referenced object |
| relatedEvidence      | 0..1 / 0..\*    | Controlled value or referenced object |

## E.2 EvidenceAssessment

| **Property**           | **Meaning**                        |
|------------------------|------------------------------------|
| assessmentId           | Stable ID.                         |
| assertionOrRequirement | Precise evaluation target.         |
| evidenceRefs           | Items assessed.                    |
| qualityVector          | P/F/C/R/T/I ratings and rationale. |
| sufficiency            | S0-S5 and rationale.               |
| confidence             | Controlled assertion confidence.   |
| conflictsAndUnknowns   | Unresolved conditions.             |
| reviewer/competence    | Accountable reviewer.              |
| date/snapshot          | Temporal and version context.      |
| decisionEffect         | Finding, gate or claim ceiling.    |

## E.3 EvidenceManifest

| **Property**        | **Meaning**                                  |
|---------------------|----------------------------------------------|
| manifestId/version  | Immutable package identity.                  |
| package/portfolio   | Parent scope.                                |
| evidenceItems       | IDs, hashes, versions, locations and states. |
| missingItems        | Expected but absent objects.                 |
| restrictedItems     | Protected references and access rules.       |
| supersession        | Replaced objects and lineage.                |
| signature/timestamp | Manifest integrity method.                   |
| review/approval     | Release roles and date.                      |

# Appendix F - Review and release gates

| **Review role**               | **Status**      | **Focus**                                                  |
|-------------------------------|-----------------|------------------------------------------------------------|
| Methodology author            | Draft completed | Evidence architecture coherence.                           |
| Assurance/evidence specialist | Pending         | Quality, sufficiency and confidence model.                 |
| Electrical engineering        | Pending         | CG-05 evidence profile.                                    |
| Mechanical/liquid cooling     | Pending         | CG-06 evidence profile.                                    |
| Compute/storage/network       | Pending         | CG-08/10 evidence profile.                                 |
| Operations/reliability        | Pending         | Operational and recovery evidence.                         |
| OT/cybersecurity              | Pending         | Control-plane, identity and logging evidence.              |
| Ontology/graph                | Pending         | Evidence classes/relationships and Artifact 005 alignment. |
| Data/privacy/security         | Pending         | Classification, minimisation and handling.                 |
| Legal/records management      | Pending         | Retention, legal hold and disclosure.                      |
| Certification/accreditation   | Pending         | Evidence floors and scheme implications.                   |
| Independent practitioner      | Pending         | Usability and reproducibility.                             |
| Public release                | Not approved    | Mandatory review gates closed.                             |

## Acceptance criteria

- All AIDCF-007 controls can receive a complete Evidence Requirement Profile.

- Evidence quality dimensions remain visible and non-compensating where claim-critical.

- UNKNOWN, conflicts and stale evidence cannot be hidden by scoring.

- Critical-gate evidence floors are enforceable.

- Human and machine-readable records preserve provenance and review.

- Security, privacy, retention and lawful handling are operationally usable.

- Artifact 009 can directly consume the model for assessment procedures.

## Change record

| **Version** | **Status**              | **Summary**                                             |
|-------------|-------------------------|---------------------------------------------------------|
| 0.1         | Architecture draft      | Evidence doctrine, hierarchy and taxonomy.              |
| 0.5         | Integrated draft        | Quality, sufficiency, gate, graph and lifecycle models. |
| 1.0         | Controlled-review draft | Full evidence standard and 360-control profile matrix.  |

## Final doctrine

Evidence is the currency of AIDCF assurance. An evidence item has no universal authority outside its provenance, scope, time, state, method and assertion. A strong-looking package cannot compensate for a missing mandatory type, critical coverage gap, unresolved conflict or failed gate. When evidence cannot support the requested conclusion, AIDCF preserves UNKNOWN, states the limitation and withholds stronger assurance rather than manufacturing certainty.
