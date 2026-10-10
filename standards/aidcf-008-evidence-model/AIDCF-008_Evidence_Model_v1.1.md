> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-008_Evidence_Model_v1.1.pdf](AIDCF-008_Evidence_Model_v1.1.pdf).

**AIDCF**

# EVIDENCE MODEL

*AI Data Centre Facilities Assurance Framework*

Version 1.1

A normative evidence architecture for traceable, current, sufficient and reviewable AI infrastructure assurance

Artifact ID: AIDCF-008  
Requirement prefix: EVM  
Artifact type: Normative evidence architecture standard  
Status: Draft for controlled review  
Author: Siva Sethumadhavan

Evidence is the currency of assurance. Assertions, scores and decisions have no independent authority beyond their evidence, scope and review.

# Document control

| **Field** | **Value** |
|---|---|
| Title | AIDCF Evidence Model |
| Artifact ID | AIDCF-008 (requirement prefix EVM) |
| Version | 1.1 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Depends on | AIDCF-001 Manifesto; AIDCF-002 Core Conceptual Model; AIDCF-003; AIDCF-004; AIDCF-005; AIDCF-006; AIDCF-007A |
| Purpose | Define evidence objects, classes, metadata, provenance, integrity, quality, timeliness, coverage, sufficiency, confidence, conflict, UNKNOWN typing and severity, retention and decision use. |
| Applies to | All AIDCF-007A controls, assertions, Findings, critical gates, tests, scores, maturity determinations, reports, decisions and compatible tooling. |
| Downstream | AIDCF-009 Assessment Methodology; AIDCF-010 Scoring and Decision Framework; AIDCF-012 Reporting and Assurance Statement Standard; AIDCF-014 and AIDCF-016 machine-executable models; AIDCF-017 Capability Assurance Maturity Model. |
| Safety/privacy boundary | Evidence collection shall be authorised, proportionate, lawful, minimally intrusive and protected. This standard does not authorise hazardous testing or unrestricted data collection. |

## Revision history

| **Version** | **Date** | **Summary** |
|---|---|---|
| 1.0 | — | Controlled-review draft: full evidence standard and 360-control profile approach. |
| 1.1 | 2026-10-10 | Live references moved to AIDCF-007A; conformance levels renamed EC0–EC5; quality dimensions aligned to canonical P/F/C/R/T/I meanings; confidence flags; UNKNOWN severity US1–US5 and per-type grading; Evidence Requirement Profiles carried in the AIDCF-007A registry; gate names aligned; consecutive EVM-REQ IDs with mapping annex. |

# Executive thesis

AIDCF assurance depends on whether a precise assertion is supported by evidence that is relevant, authentic, sufficiently complete, current for the represented state, traceable to its source, protected against inappropriate alteration, and reviewed by a competent accountable party. Evidence is not graded once for all purposes. Its usefulness is evaluated against the claim, Capability Instance, Service Outcome, boundary, operating state, period and decision question.

## Canonical evidence chain

Within the canonical sixteen-step assurance chain (AIDCF-002; Decision Question → … → Assurance Decision), this standard governs steps 10 to 13 (Evidence Requirement, Evidence Object, Control Assessment, Finding / UNKNOWN Record) and the evidence inputs to step 14 (Gate Result). The evidence-specific reasoning inside those steps is:

Decision Question -\> Assertion -\> Evidence Requirement -\> Evidence Object -\> Provenance and Integrity -\> Fitness and Coverage -\> Quality and Timeliness -\> Sufficiency -\> Confidence -\> Conflict and UNKNOWN (type and severity) -\> Finding / Gate Result -\> Bounded Assurance Decision

## Key outputs

- Canonical EvidenceObject, EvidencePackage and EvidencePortfolio structures.

- Seven evidence classes (E1–E7) and controlled subtypes.

- Six-dimensional evidence quality model (P, F, C, R, T, I) and quality bands Q0–Q5.

- Timeliness, retention and chain-of-custody rules.

- Assertion-specific sufficiency (S0–S5) and confidence (CONF-0 to CONF-4, flags CONFLICTING and STALE).

- Evidence Requirement Profiles for all 360 controls, carried in the AIDCF-007A registry.

- Critical-gate evidence profiles for CG-01 to CG-15.

- Conflict, derived evidence, automation, UNKNOWN type (U1–U10) and UNKNOWN severity (US1–US5) rules.

- Machine-readable ontology, schema and validation expectations.

# Contents

1\. I Authority, scope and conformance

2\. II Evidence doctrine and mandatory distinctions

3\. III Evidence metamodel and object hierarchy

4\. IV Evidence taxonomy and subtype catalogue

5\. V Evidence metadata standard

6\. VI Provenance, integrity and chain of custody

7\. VII Evidence quality dimensions and grading

8\. VIII Timeliness, validity, retention and legal hold

9\. IX Coverage, sampling and representativeness

10\. X Evidence sufficiency and confidence

11\. XI Evidence-to-assertion and result model

12\. XII Evidence-to-control mapping (Evidence Requirement Profiles)

13\. XIII Critical-gate evidence profiles

14\. XIV Conflict, contradiction and UNKNOWN

15\. XV Derived, automated and AI-generated evidence

16\. XVI Evidence lifecycle and review workflow

17\. XVII Evidence security, privacy and disclosure

18\. XVIII Graph-native and machine-readable model

19\. XIX Conformance, validation and nonconformance

20\. XX Worked evidence packages

21\. Appendix A Evidence type registry

22\. Appendix B Quality rating matrix

23\. Appendix C Control Evidence Requirement Profile register

24\. Appendix D Critical-gate evidence register

25\. Appendix E Record schemas

26\. Appendix F Review and release gates

27\. Annex G Requirement identifier mapping (v1.0 to v1.1)

# Part I - Authority, scope and conformance

## 1. Purpose

This standard operationalises the evidence commitments in AIDCF-006 and the Evidence Requirement Profiles carried in the AIDCF-007A Canonical Master Control Registry. It defines a common evidence language suitable for human assessments, structured workpapers, graph implementations and future assurance schemes. Normative keywords (shall, should, may, can) follow ISO/IEC Directives Part 2 usage.

## 2. Normative requirements

**EVM-REQ-001** Every material assertion shall link to supporting, challenging or qualifying Evidence Objects, or to an explicit UNKNOWN Record.

**EVM-REQ-002** Evidence shall retain identity, source, collection, scope, time, integrity, custody, classification and review metadata.

**EVM-REQ-003** Evidence quality and sufficiency shall be evaluated against a precise assertion; no evidence item has a universal grade.

**EVM-REQ-004** DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS and RESILIENCE claims shall use evidence appropriate to the claim type (§29).

**EVM-REQ-005** Evidence conflict, staleness, inaccessible sources and coverage gaps shall remain visible.

**EVM-REQ-006** UNKNOWN shall not be transformed into pass, zero, false, NOT_APPLICABLE or accepted risk.

**EVM-REQ-007** Critical-gate evidence shall meet the declared evidence floor (Part XIII) or the gate shall remain UNKNOWN or FAIL according to the gate criterion and the roll-up rule in AIDCF-010.

**EVM-REQ-008** Derived and AI-generated evidence shall retain source lineage, transformation logic and candidate review state.

**EVM-REQ-009** Evidence collection and testing shall be authorised, competent, proportionate, lawful and safe.

**EVM-REQ-010** Retention and deletion shall preserve legal, contractual, audit and decision-lineage obligations.

**EVM-REQ-011** Evidence reuse across controls or methods shall require assertion-specific relevance and scope evaluation.

**EVM-REQ-012** A score, maturity level or certificate shall not increase the evidential strength of its underlying sources.

## 3. Scope

- Evidence created or collected for all 360 AIDCF-007A controls.

- Evidence supporting infrastructure, dependency, failure, safeguard, recovery and graph assertions.

- Evidence needed to evaluate the 15 baseline critical gates (CG-01 to CG-15).

- Evidence used by AIDCF and AI Trust Graph integrated decision packages (AIDCF-005).

- Human, machine, documentary, observational, test, operational and derived evidence.

## 4. Evidence-system conformance levels

These levels describe how completely an implementation (repository, tool or assessment practice) realises this standard. They were labelled E0–E5 in v1.0 and are renamed EC0–EC5 to avoid confusion with evidence classes E1–E7 (Part IV).

| **Level** | **Name** | **Minimum expectation** |
|---|---|---|
| EC0 | Vocabulary aligned | Uses canonical evidence terms and source ownership. |
| EC1 | Metadata complete | Implements mandatory EvidenceObject fields (§11). |
| EC2 | Provenance controlled | Adds source, collection, integrity, custody and classification (Part VI). |
| EC3 | Assertion linked | Evaluates fitness, quality, timeliness and coverage for precise assertions. |
| EC4 | Decision ready | Supports sufficiency, confidence, gates, conflict, UNKNOWN type and severity, and bounded decisions. |
| EC5 | Machine conformant | Passes schemas, validation shapes, versioning and audit tests (Part XIX). |

**EVM-REQ-013** An implementation claiming conformance to this standard shall declare its EC level, and each level shall include all requirements of the levels below it. Evidence used for a Gate Result shall be managed by an implementation at EC4 or above.

# Part II - Evidence doctrine and mandatory distinctions

## 5. Foundational doctrines

| **Doctrine** | **Rule** |
|---|---|
| Evidence before conclusion | No positive assurance conclusion without affirmative support. |
| Assertion specificity | Evidence supports or challenges a precise proposition, not an object in the abstract. |
| Reality over intent | Observed and tested evidence takes precedence where design intent conflicts. |
| Bounded use | Evidence applies only to stated scope, period, state, conditions and method. |
| Independent review | Collection, interpretation and decision authority remain distinguishable. |
| Minimum false precision | Scores express structured judgment but do not manufacture certainty. |
| Preserved uncertainty | Missing, inaccessible, stale, conflicting or weak evidence remains visible. |
| Non-inheritance | Third-party certification or prior review is evidence, not automatic assurance. |

## 6. Mandatory distinctions

| **Do not collapse** | **Reason** |
|---|---|
| Evidence Object / Evidence Package | One item differs from a governed collection. |
| Source / Collector / Custodian / Reviewer | Origin, acquisition, storage and judgment are different roles. |
| Observation time / collection time / record time | The represented state may differ from acquisition or repository entry. |
| Authenticity / integrity | Genuine origin differs from freedom from unauthorised alteration. |
| Reliability / fitness | A reliable source may not be relevant to, or fit for, the claim. |
| Coverage / volume | Many records may still cover a narrow population or state. |
| Quality / sufficiency | Strong evidence can still be insufficient in quantity or diversity. |
| Evidence quality / confidence | Evidence characteristics differ from reviewer confidence in an assertion. |
| UNKNOWN type / UNKNOWN severity | Why something is unknown (U1–U10) differs from what it could change (US1–US5). |
| Stale / contradicting | Old evidence differs from current disagreement. |
| Independent / external | External does not necessarily mean impartial, competent or verified. |
| Test result / effectiveness conclusion | A test output requires scope and interpretation. |
| Derived evidence / source evidence | Analysis does not replace its lineage sources. |
| Implementation Maturity / control result | Diagnostic maturity (IM0–IM5, AIDCF-017) never substitutes for a control result. |

# Part III - Evidence metamodel and object hierarchy

## 7. Core evidence entities

| **Entity** | **Definition** |
|---|---|
| EvidenceObject | Smallest independently identified evidence item used to support, challenge or qualify an assertion. |
| EvidenceSet | A purpose-specific selection of Evidence Objects used together for one assertion or test. |
| EvidencePackage | A governed collection addressing a control, function, system, scenario or gate. |
| EvidencePortfolio | A capability-level collection of Evidence Packages and decision records. |
| EvidenceSource | Person, system, device, provider, repository or process from which evidence originates. |
| CollectionActivity | Authorised action that acquires or observes evidence. |
| TransformationActivity | Declared process deriving one evidence object from others. |
| EvidenceRequirement | Claim-specific statement of required classes, quality, coverage, age and independence; for controls, instantiated from the Evidence Requirement Profile in the AIDCF-007A registry. |
| EvidenceAssessment | Recorded evaluation of evidence against a requirement. |
| EvidenceManifest | Machine-readable inventory with identifiers, hashes, locations and status. |
| CustodyEvent | Transfer, access, export, alteration, redaction or retention action. |
| EvidenceConflict | Structured disagreement between evidence-supported assertions. |
| UnknownRecord | Typed (U1–U10) and severity-graded (US1–US5) record of an unresolved evidence condition. |

## 8. Hierarchy

EvidencePortfolio -\> EvidencePackage -\> EvidenceSet -\> EvidenceObject -\> Source and Collection Activity -\> Assertion / Control Assessment / Gate Result / Assurance Decision

## 9. EvidenceObject lifecycle states

| **State** | **Meaning** |
|---|---|
| EXPECTED | Evidence requirement identified but object not yet collected. |
| REQUESTED | Collection request issued. |
| COLLECTED | Object acquired but not quality reviewed. |
| VALIDATED | Identity, provenance, integrity and readability reviewed. |
| ACCEPTED | Approved for one or more stated assurance uses. |
| CHALLENGED | Material concern or contradiction recorded. |
| STALE | No longer sufficiently representative. |
| RESTRICTED | Use limited by security, privacy, contract or legal hold. |
| SUPERSEDED | Replaced by a later object while history remains. |
| REJECTED | Not suitable for the stated use; rationale retained. |
| RETIRED | No longer current but retained according to policy. |
| DESTROYED | Disposed under authorised retention process; destruction record remains. |

## 10. Evidence Package minimum structure

| **Component** | **Requirement** |
|---|---|
| Package ID and purpose | Stable identity and decision/claim addressed. |
| Subject and boundary | Capability Instance, control, system, gate, operating state and period. |
| Requirement profile | Required evidence classes, quality floor, sufficiency floor, state and period coverage, and independence (from the AIDCF-007A Evidence Requirement Profile or Part XIII). |
| Manifest | Complete list of included, missing, substituted and restricted items. |
| Assessments | Per-object quality vector and package sufficiency results. |
| Conflicts and UNKNOWN | Unresolved contradictions, gaps, UNKNOWN type and severity, and decision effects. |
| Review and approval | Collector, analyst, reviewer and decision roles. |
| Version and custody | Immutable release, hash, access and supersession lineage. |

# Part IV - Evidence taxonomy and subtype catalogue

| **Class** | **Name** | **Representative subtypes** |
|---|---|---|
| E1 | Documentary and declarative | policy; standard; procedure; runbook; design basis; architecture; drawing; contract; attestation; inventory |
| E2 | Configuration and technical state | device configuration; firmware inventory; cluster manifest; access policy; protection setting; topology export; configuration snapshot |
| E3 | Operational and observational | telemetry; log; alarm; event; ticket; work order; capacity metric; performance metric; physical observation; inspection record |
| E4 | Validation and test | commissioning; load test; failover test; recovery test; simulation; scenario exercise; functional test; calibration; witnessed demonstration |
| E5 | Independent and third-party | independent engineering review; audit; provider assurance; witnessed test; laboratory result; accredited certificate; regulatory inspection |
| E6 | Human and experiential | interview; workshop; walkthrough; operator demonstration; expert judgment; shift observation; competency evidence |
| E7 | Derived and analytical | trend; correlation; capacity analysis; failure analysis; dependency path; reconciled inventory; score; model output; AI-assisted extraction |

| **Class** | **Primary claim supported** | **Use rule** |
|---|---|---|
| E1 Documentary and declarative | Intent, governance and approved design | Best suited to intent, requirements, authority, design and declared process. It shall not alone prove current implementation or effectiveness. |
| E2 Configuration and technical state | Implementation and technical state | Requires provenance, extraction context and reconciliation to the current architecture. |
| E3 Operational and observational | Operation, performance and incidents | Best suited to operation over a stated period. Coverage, completeness, clock integrity, gaps and collection health shall be assessed. |
| E4 Validation and test | Validation, effectiveness and resilience | Best suited to effectiveness and resilience under stated conditions. Test authorisation, initial state, method, expected result and anomalies shall be retained. |
| E5 Independent and third-party | Independent corroboration | May strengthen independence but shall be evaluated for scope, competence, method, age, exclusions and transferability. |
| E6 Human and experiential | Practice, competence and context | Useful for context, operating practice and explanation. Corroboration is required for material technical-effectiveness assertions. |
| E7 Derived and analytical | Analysis and relationship synthesis | Useful for synthesis and decision support. Derived outputs never exceed the quality, scope and lineage of their sources. |

# Part V - Evidence metadata standard

## 11. Mandatory metadata

| **Field** | **Requirement** |
|---|---|
| evidenceId | Immutable unique identifier. |
| title | Concise human-readable name. |
| description | What the item contains and why it exists. |
| evidenceClass/subtype | Controlled E1–E7 classification and Appendix A subtype. |
| sourceId/sourceType | Originating person, system, provider or process. |
| owner/custodian | Accountable owner and storage custodian. |
| collector/collectionMethod | Who or what collected it, how and under which authority; method recorded using the canonical assessment-method codes where applicable (INQUIRY, DOCUMENT_REVIEW, INSPECTION, OBSERVATION, RECONCILIATION, ANALYSIS, SAMPLING, TEST, REPERFORMANCE, SCENARIO_EXERCISE). |
| observationTime | When the represented condition existed. |
| collectionTime | When the evidence was acquired. |
| recordTime | When entered into the repository. |
| effectivePeriod | Period for which the evidence is applicable. |
| subjectRefs | Capabilities, assets, controls, gates, assertions or paths addressed. |
| scope | Locations, systems, tenant, population and operating states covered (canonical operating states: NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION, SHUTDOWN, FAILED, UNKNOWN). |
| architecture/configurationVersion | Baseline represented. |
| integrityMethod/hash | Integrity protection and digest where applicable. |
| format/version | File, record, schema and tool versions. |
| classification | Security/privacy/contractual handling category (§41). |
| retentionRule | Retention class (§21), trigger and legal hold. |
| qualityAssessment | Dimension ratings P/F/C/R/T/I and rationale. |
| reviewState/reviewer | Lifecycle state (§9) and accountable reviewer. |
| limitations | Known gaps, exclusions, sampling or interpretation limits. |
| relatedEvidence | Sources, derivatives, conflicts, replacements and package membership. |

## 12. Conditional metadata

- Test evidence: initial state, expected result, procedure, authorisation, abort criteria, instrumentation, anomalies and witnesses.

- Telemetry/log evidence: source clock, timezone, sampling interval, collection health, dropped data and query/filter.

- Configuration evidence: extraction command or interface, privilege used, configuration scope, redactions and target state.

- Human evidence: role, competence, interview protocol, date, corroboration and consent/recording status.

- External evidence: issuer, competence/accreditation where relevant, scope, validity, exclusions and permitted reliance.

- Derived evidence: source IDs, transformation code/query/version, assumptions, quality propagation and reviewer.

# Part VI - Provenance, integrity and chain of custody

## 13. Provenance model

The provenance terms below follow the W3C PROV data model (PROV-DM) at concept level.

| **Provenance object** | **Minimum content** |
|---|---|
| Entity | Evidence object or source record. |
| Activity | Collection, observation, transformation, review or custody event. |
| Agent | Person, system, provider or organisation responsible. |
| wasGeneratedBy | Activity that produced the object. |
| wasDerivedFrom | Source evidence and transformations. |
| wasAttributedTo | Responsible source or owner. |
| wasAssociatedWith | Collector, reviewer or tool involved. |
| used | Source objects consumed by a transformation. |
| invalidatedAtTime | When evidence became stale, superseded, withdrawn or destroyed. |

## 14. Integrity levels

| **Level** | **Name** | **Anchor** |
|---|---|---|
| I0 | Unknown | Integrity method absent or unverified. |
| I1 | Basic controlled | Repository permissions and version history. |
| I2 | Verified copy | Source comparison or controlled export metadata. |
| I3 | Hashed | Cryptographic digest recorded in manifest. |
| I4 | Signed / trusted timestamp | Digital signature or trusted timestamp validated. |
| I5 | Tamper-evident custody | End-to-end signed custody, immutable storage or equivalent control. |

The integrity level of an object and its I quality rating (§17) use the same anchors; the I rating records the level verified for the specific use.

## 15. Chain-of-custody events

- Creation or acquisition.

- Transfer between collectors, custodians or repositories.

- Read/access for review.

- Transformation, parsing, redaction or export.

- Integrity verification.

- Challenge, correction or supersession.

- Legal hold, restriction, retention extension or authorised destruction.

**EVM-REQ-014** Every material transformation shall produce a new Evidence Object linked to source evidence; original evidence shall not be silently overwritten.

**EVM-REQ-015** Redaction shall preserve an unredacted controlled source where lawful and shall record the basis, method and affected content.

# Part VII - Evidence quality dimensions and grading

## 16. Quality dimensions

| **Code** | **Dimension** | **Question** |
|---|---|---|
| P | Provenance | Can origin, authority and collection lineage be established? |
| F | Fitness (relevance) | Does the item address the precise subject, criterion, claim type, configuration and state of the assertion? |
| C | Coverage | Does it cover the required population, period, state and boundary? |
| R | Reliability | Is the method/source repeatable, controlled and corroborated? |
| T | Timeliness (currentness) | Is the item sufficiently current and representative of the state being asserted? |
| I | Integrity | Is it protected against undetected alteration and custody loss? |

Alignment note (v1.1): in v1.0, F denoted Freshness and T denoted Traceability. The canonical meanings are now F = Fitness/relevance and T = Timeliness/currentness; the former Freshness anchors are carried unchanged as the T anchors. Traceability is no longer rated per item because it is a property of the assessment record rather than of the evidence; it is enforced as a mandatory linkage requirement (§17A) and by validation rules EVM-VAL-002 and EVM-VAL-006.

## 17. Rating scale

### P rating anchors

| **Rating** | **Anchor** |
|---|---|
| P0 | Unknown origin |
| P1 | Identified but uncontrolled source |
| P2 | Accountable internal source |
| P3 | Controlled authoritative source |
| P4 | Corroborated authoritative source |
| P5 | Independently verified origin and lineage |

### F rating anchors

| **Rating** | **Anchor** |
|---|---|
| F0 | Relevance not established, or the item is not linked to the assertion |
| F1 | Indirect: concerns a related system, population or design generation, not the asserted subject |
| F2 | Partial: correct subject but a different claim type, configuration version or operating state |
| F3 | Relevant: addresses the asserted subject, claim type and period, and is linked to the assertion |
| F4 | Specific: addresses the precise assessment criterion, configuration version and declared operating states |
| F5 | Discriminating: designed for the criterion (e.g. a test with pre-declared acceptance criteria) so that a nonconforming condition would have been detected |

### C rating anchors

| **Rating** | **Anchor** |
|---|---|
| C0 | Unknown coverage |
| C1 | Anecdotal or isolated |
| C2 | Limited sample/state |
| C3 | Representative core scope |
| C4 | Broad scope and relevant states |
| C5 | Comprehensive declared population, period and states |

### R rating anchors

| **Rating** | **Anchor** |
|---|---|
| R0 | Unassessed |
| R1 | Weak/uncontrolled method |
| R2 | Plausible but lightly corroborated |
| R3 | Controlled repeatable method |
| R4 | Strong and independently corroborated |
| R5 | Validated method and independent verification |

### T rating anchors

| **Rating** | **Anchor** |
|---|---|
| T0 | Unknown age or state |
| T1 | Obsolete for represented state |
| T2 | Stale or change-sensitive |
| T3 | Acceptable for decision |
| T4 | Current and aligned to baseline |
| T5 | Near-real-time or event-current with healthy collection |

### I rating anchors

| **Rating** | **Anchor** |
|---|---|
| I0 | Unknown integrity |
| I1 | Basic repository controls |
| I2 | Verified source copy |
| I3 | Hash verified |
| I4 | Signature/timestamp verified |
| I5 | Tamper-evident end-to-end custody |

## 17A. Linkage requirement (formerly the T Traceability dimension)

**EVM-REQ-016** Every ACCEPTED Evidence Object used for a control result shall be linked to its subject, the assertion it supports, challenges or qualifies, and the period represented. An object without this linkage shall be rated F0 for that use.

**EVM-REQ-017** Evidence used for a Gate Result shall additionally be linked end to end to the Finding or UNKNOWN Record and to the Gate Result it informs; evidence used for an Assurance Decision shall be reachable from the decision through an immutable EvidenceManifest (EVM-VAL-015).

## 18. Evidence quality vector

Preferred expression: \[Class\]-P#-F#-C#-R#-T#-I#. Example: E4-P4-F4-C3-R4-T4-I3. The vector shall remain visible. A single averaged number may be used only as a secondary sorting aid and shall not replace the dimensions. The only sanctioned averaged number is the Evidence Quality Index (EQI) defined in AIDCF-010; it never changes a quality band, a sufficiency level, a control result, a Gate Result or a decision.

**EVM-REQ-018** Quality floors in Evidence Requirement Profiles shall be expressed per dimension (for example "P3 F3 C3 R3 T3 I2") and shall be tested per dimension; an item that misses any dimension of the floor does not meet the floor regardless of its EQI.

## 19. Evidence quality bands

Quality bands Q0–Q5 replace the "evidence grade E0–E5" used in AIDCF-005 §37 and AIDCF-006 §11.

| **Band** | **Rule** | **Permitted use** |
|---|---|---|
| Q0 Unusable | Any dimension P0, F0, R0, T0 or I0 without accepted limitation. | Context only; no positive assertion. |
| Q1 Weak | Multiple dimensions at 0–1 or unsupported source. | Candidate/UNKNOWN; remediation priority. |
| Q2 Limited | Core provenance established but limited coverage, timeliness or corroboration. | Descriptive or limited DESIGN claim. |
| Q3 Adequate | All claim-critical dimensions at least 3. | DESIGN or IMPLEMENTATION claim where appropriate. |
| Q4 Strong | Most dimensions 4+, with no claim-critical dimension below 3. | OPERATION or EFFECTIVENESS claim with sufficient package coverage. |
| Q5 Highly defensible | Independent/corroborated, representative, current and fit for the criterion, with strong integrity. | High-consequence gate or RESILIENCE claim, subject to method and sufficiency. |

# Part VIII - Timeliness, validity, retention and legal hold

## 20. Timeliness rule

Timeliness (dimension T) is risk- and change-based. The windows below are default review triggers, not universal expiry. A material change invalidates representativeness even when the nominal window has not elapsed.

| **Evidence category** | **Default currency basis** | **Immediate invalidation/review triggers** |
|---|---|---|
| Live telemetry and active alarms | Current collection health; decision-specific lookback | Collection outage, sensor/configuration change, incident. |
| Event and security logs | Usually current period and sufficient lookback for decision | Clock/source/query change, incident, retention gap. |
| Configuration snapshots | At assessment and after material change | Firmware, policy, topology, identity or setpoint change. |
| Capacity/performance metrics | Current demand cycle and peak/seasonal state | Expansion, workload shift, throttling or demand change. |
| Maintenance/calibration records | Current maintenance cycle | Overdue work, failure, deferral or scope change. |
| Commissioning and validation tests | Until material change, adverse event or review trigger | Architecture, load, firmware, procedure or provider change. |
| Recovery and continuity exercises | Risk-based periodic cycle and after material change | Failure, failed exercise, new dependency or recovery design change. |
| Architecture/design documents | Until superseded or material change | As-built discrepancy, expansion or reconfiguration. |
| Contracts/provider attestations | Until expiry, renewal or service change | Provider, SLA, subprocessor or jurisdiction change. |
| Interviews and walkthroughs | Point-in-time context | Role/process change or contradictory technical evidence. |

## 21. Retention classes

| **Class** | **Purpose** | **Rule** |
|---|---|---|
| R0 Transient | Temporary extraction or working copy. | Delete under controlled process after verified ingestion unless needed for decision traceability. |
| R1 Operational | Routine monitoring and work records. | Retain for operational, contractual and investigation needs. |
| R2 Assurance | Assessment evidence and workpapers. | Retain through decision validity plus defined challenge/reassessment period. |
| R3 Critical decision | Gate, resilience and high-consequence evidence. | Longer risk-based retention with immutable lineage. |
| R4 Legal/regulatory hold | Evidence subject to preservation obligation. | No alteration/destruction until authorised release. |
| R5 Canonical methodology | Schemas, mappings, approved examples and release artifacts. | Versioned permanent archive. |

Retention class codes R0–R5 are distinct from reliability ratings R0–R5 (§17); records shall qualify them (retentionClass versus quality.R).

**EVM-REQ-019** Retention periods shall be defined by applicable legal, contractual, regulatory, security, privacy and operational requirements; this standard does not prescribe universal years.

# Part IX - Coverage, sampling and representativeness

## 22. Coverage dimensions

| **Dimension** | **Coverage question** |
|---|---|
| Entity | Which assets, systems, providers and interfaces are included? |
| Population | What proportion and which strata of the population are represented? |
| Location | Which sites, halls, zones, racks and jurisdictions? |
| Time | Which period, season, demand cycle and incident window? |
| Operating state | Which of NORMAL, DEGRADED, MAINTENANCE, EMERGENCY, RECOVERY, TRANSITION, SHUTDOWN and FAILED are represented? |
| Scenario | Which threat, hazard, failure, common-mode and recovery paths? |
| Tenant/workload | Which tenancy, cluster, workload or Service Outcomes? |
| Control behaviour | Design, implementation, operation, monitoring, validation and recovery? |
| Dependency | Which upstream, downstream, shared and external dependencies? |

## 23. Sampling principles

- Sampling shall be risk-based, reproducible and documented.

- The population, strata, selection method, sample size rationale and exclusions shall be recorded.

- Judgmental sampling may target critical or anomalous items but shall not be represented as statistical coverage.

- Random or systematic sampling requires a trustworthy population frame.

- A sampled pass shall not be extrapolated beyond the represented population and conditions.

- Exceptions and failed samples shall influence expansion and conclusion.

## 24. Coverage rating

| **Level** | **Meaning** |
|---|---|
| C0 | Population or scope unknown. |
| C1 | Single example or anecdotal evidence. |
| C2 | Limited sample or one state. |
| C3 | Representative core population and expected state. |
| C4 | Broad population and material DEGRADED/MAINTENANCE states. |
| C5 | Comprehensive declared population, periods and applicable states, subject to practical limits. |

Evidence coverage (C, per item or package) is distinct from assessment coverage (the percentage of in-scope controls with a scored result), which is defined in AIDCF-010.

# Part X - Evidence sufficiency and confidence

## 25. Sufficiency model

Sufficiency is an assertion-specific judgment based on whether the combined evidence package meets required class diversity, quality floors, coverage, timeliness, independence, conflict resolution and state/scenario representation. It shall not be calculated only from evidence count.

| **Level** | **Name** | **Meaning** |
|---|---|---|
| S0 | None | No usable evidence. |
| S1 | Insufficient | Some evidence exists but cannot support the claim. |
| S2 | Minimum descriptive | Supports a bounded description or design intent. |
| S3 | Reasonable | Supports DESIGN or IMPLEMENTATION within declared scope. |
| S4 | Strong | Supports OPERATION or EFFECTIVENESS for representative conditions. |
| S5 | Highly defensible | Supports high-consequence gate or RESILIENCE claim with diverse, current, traceable and appropriately independent evidence. |

**EVM-REQ-020** Where the sufficiency of the evidence package for a claim is below the sufficiencyFloor of the applicable Evidence Requirement Profile, the control result for that claim shall be UNKNOWN (not PARTIAL or NONCONFORMING), except that a NONCONFORMING result may be recorded on evidence below the floor where that evidence affirmatively demonstrates that a criterion is not met; the rationale shall be recorded.

## 26. Sufficiency decision factors

| **Factor** | **Assessment** |
|---|---|
| Required class diversity | Are design, configuration, operation and validation classes present as required? |
| Quality floor | Does each mandatory item meet the per-dimension floor? |
| Complementarity | Do items address different weaknesses rather than duplicate one source? |
| Independence | Are critical claims corroborated by an appropriately separate source/method? |
| Coverage | Does the package represent population, state, time and scenario? |
| Conflict | Are material contradictions resolved or bounded? |
| UNKNOWN | Are missing elements identified with type, severity and decision effect? |
| Critical gate | Does the package meet the declared non-compensating gate floor (Part XIII)? |

## 27. Confidence

Confidence is a reviewer's recorded professional judgment of support for a bounded assertion. It has five levels and two flags.

| **Level** | **Meaning** |
|---|---|
| CONF-0 UNKNOWN | No defensible confidence state. |
| CONF-1 LOW | Weak/limited evidence; high sensitivity to assumptions. |
| CONF-2 MODERATE | Reasonable support with material limitations. |
| CONF-3 HIGH | Strong support with no unresolved material conflict within scope. |
| CONF-4 VERY_HIGH | Highly defensible, independently corroborated and representative support for the bounded claim. |

| **Flag** | **Meaning** | **Effect** |
|---|---|---|
| CONFLICTING | Material evidence supports incompatible propositions (U4). | Confidence for the affected assertion shall not exceed CONF-1 until the conflict is resolved or bounded under §34. |
| STALE | Previously supported but no longer sufficiently current (U3). | Confidence for current-state use reverts to CONF-0; historical use may retain its prior level with the period stated. |

Flags are recorded alongside a level (for example "CONF-1, CONFLICTING"); they are not levels.

| **Ceiling source** | **Maximum confidence** |
|---|---|
| Package sufficiency S0–S1 | CONF-0 |
| Package sufficiency S2 | CONF-1 |
| Package sufficiency S3 | CONF-2 |
| Package sufficiency S4 | CONF-3 |
| Package sufficiency S5 | CONF-4 |
| An attached US2 UNKNOWN (§35A) | CONF-2 |
| An attached US3, US4 or US5 UNKNOWN | CONF-1 for the affected assertion |

These are ceilings, not a formula: a reviewer may record lower confidence with rationale.

**EVM-REQ-021** Confidence shall be recorded with rationale and shall not be derived from a hidden formula.

**EVM-REQ-022** A confidence level shall not exceed the ceiling imposed by the weakest mandatory evidence requirement, an attached flag or an attached UNKNOWN Record.

# Part XI - Evidence-to-assertion and result model

## 28. Assertion structure

| **Field** | **Requirement** |
|---|---|
| assertionId | Stable versioned identity. |
| proposition | Subject-predicate-object or equivalent precise statement. |
| claimType | For control assessments, one of DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS or RESILIENCE. Other assertions may use the supplementary kinds in §29 (intent/governance, absence, independent assurance, derived decision). |
| scope/conditions | Capability Instance, boundary, operating state, configuration, load, period and assumptions. |
| evidenceRequirement | Required classes, quality floors, sufficiency floor, coverage and independence. |
| supportingEvidence | Evidence Objects supporting proposition. |
| challengingEvidence | Evidence Objects contradicting or weakening proposition. |
| qualifyingEvidence | Evidence limiting scope or interpretation. |
| assessment | Quality, sufficiency, conflict and UNKNOWN evaluation. |
| confidence/review | Confidence level and flags, reviewer and date. |
| decisionUse | Findings, gate or decision that relies upon the assertion. |

## 29. Claim-type evidence floors

| **Claim type** | **Minimum Assurance Level** | **Minimum pattern** |
|---|---|---|
| DESIGN | AL2 | E1 design evidence plus competent technical analysis; E5 where required by authority or consequence. |
| IMPLEMENTATION | AL3 | E2 configuration/as-built evidence plus E3 or E6 observation; reconciled to the approved design. |
| OPERATION | AL4 | E3 over a representative period and the declared operating states, plus current E2 and exception/incident review. |
| EFFECTIVENESS | AL5 | E4 representative validation under tested or observed adverse conditions, plus E2/E3 supporting state and operating evidence. |
| RESILIENCE | AL5 | E4 scenario/recovery evidence plus cross-domain E2/E3 and dependency coverage, demonstrating containment and recovery within tolerance. |

| **Supplementary assertion kind** | **Minimum pattern** |
|---|---|
| Intent/governance | E1 plus accountable approval and current applicability. |
| Negative/absence claim | Documented discovery coverage, method sensitivity and residual UNKNOWN. |
| Independent assurance | E5 scope and method plus access to underlying evidence where needed. |
| Derived decision | E7 with complete source lineage and human review. |

## 30. Control result and finding model

Control results use the canonical codes defined in AIDCF-010 (per control, per claim type, per scope). Their evidence rules are:

| **Result / record** | **Evidence rule** |
|---|---|
| CONFORMING | Affirmative evidence meets every assessment criterion for the claim type and the package meets the profile floors. |
| PARTIAL | Some criteria are met on evidence at or above floor; each unmet criterion is recorded as a Finding. |
| NONCONFORMING | Evidence demonstrates that criteria are materially not met, or that a safeguard is ineffective. |
| UNKNOWN | Evidence below floor, inaccessible, stale, conflicting or unresolved; an UNKNOWN Record with type and severity is mandatory. |
| NOT_APPLICABLE | Approved evidence-based non-applicability rationale and approver. |
| NOT_ASSESSED | In scope but not yet assessed; no evidence judgement made. |
| Observation (Finding type) | Evidence describes a condition without determining a control result. |
| Conflicting evidence | Not a result: recorded as UNKNOWN (U4) with the CONFLICTING confidence flag until resolved. |
| Suspended reliance | Not a result: the ControlAssessment lifecycle state becomes SUSPENDED and the result reverts to UNKNOWN (U3) until reassessed. |

# Part XII - Evidence-to-control mapping (Evidence Requirement Profiles)

## 31. Control Evidence Requirement Profile

Every AIDCF-007A control has an Evidence Requirement Profile. As of this version the profiles for all 360 controls are carried in the AIDCF-007A Canonical Master Control Registry as the evidenceProfile structure of each control record (one per control; per-domain machine files and CSV columns derived from it). This standard defines the meaning and rules of the fields; the registry holds the values. A profile is normative for evidence classes and floors but may be strengthened, never weakened, by a capability profile, criticality, scenario or decision need.

| **Field** | **Type / vocabulary** | **Meaning** |
|---|---|---|
| claimType | One of DESIGN, IMPLEMENTATION, OPERATION, EFFECTIVENESS, RESILIENCE | The highest claim type the control is designed to support; consistent with the control's requiredAssuranceLevel (DESIGN AL2, IMPLEMENTATION AL3, OPERATION AL4, EFFECTIVENESS and RESILIENCE AL5). Lower claim types are assessed with the patterns in §29. |
| profileTier | CP-1 to CP-5 | Control profile tier (§32). |
| requiredClasses | Array of E1–E7 | Classes that shall be present in the package for the claimType. |
| optionalClasses | Array of E1–E7 | Classes that may strengthen the package or serve as acceptable alternatives. |
| qualityFloor | String, e.g. "P3 F3 C3 R3 T3 I2" | Minimum rating per dimension for each mandatory item (§18). |
| sufficiencyFloor | S2 to S5 | Minimum package sufficiency for a CONFORMING or PARTIAL result (§25). |
| stateCoverage | Array of canonical operating states | Operating states the package shall represent. |
| periodCoverage | String | Required observation period or risk-based window (for example "≥ one full maintenance cycle including a MAINTENANCE state"). |
| independence | String | Required source/method separation (for example "test witnessed by a party independent of the installer"). |
| mandatoryItems | Array of strings | Non-substitutable evidence items. |
| acceptableAlternatives | Array of strings | Equivalent evidence with the rationale that makes it equivalent. |
| unknownEffect | String | UNKNOWN severity (US1–US5) to apply when the profile cannot be met, and its effect. |
| reassessmentTriggers | Array of strings | Conditions that invalidate the evidence and require reassessment. |

**EVM-REQ-023** The Evidence Requirement Profile applied in an assessment shall be the profile carried for that control in the version of the AIDCF-007A registry declared in the assessment plan; any strengthening shall be recorded with rationale in the Evidence Package, and any weakening shall not be permitted.

**EVM-REQ-024** A profile's unknownEffect shall state a severity determined with the test in §35A; where the control holds a CRITICAL gate mapping in the registry, the unknownEffect shall be at least US4 for any claim type mandatory for that gate.

## 32. Control profile tiers

| **Tier** | **Use** | **Minimum evidence pattern** |
|---|---|---|
| CP-1 Foundational | Governance, inventory, design intent. | E1 plus accountable source; S2/S3. |
| CP-2 Technical state | Configuration, topology and implementation. | E1+E2 with observation/reconciliation; S3. |
| CP-3 Operational | Operation, monitoring and maintenance. | E2+E3 across representative period; S3/S4. |
| CP-4 Effectiveness | Controls tested under defined conditions. | E2+E3+E4; S4. |
| CP-5 Critical/resilience | Critical gate, compound scenario or high-consequence outcome. | Diverse E1–E4 and appropriate E5; S5 or profile-defined strong floor. |

# Part XIII - Critical-gate evidence profiles

Gate names and scopes are canonical (AIDCF-010 Part VIII, which also defines the gate criteria, roll-up rule and decision ceilings). The machine-readable register is registries/gates/critical-gates.csv with criteria in registries/gates/critical-gate-criteria.csv.

| **Gate** | **Name** | **Mandatory evidence profile** | **Classes** | **Floor** | **Evidence effect (decision ceilings in AIDCF-010)** |
|---|---|---|---|---|---|
| CG-01 | Capability and outcome definition | Capability register; approved Service Outcomes and tolerances; criticality and tolerance analysis; architecture linkage; decision question | E1+E7 | S3 | An undefined or unapproved Capability Instance or outcome blocks any positive capability assurance. |
| CG-02 | Boundary and architecture integrity | Approved boundary; current architecture; as-built/configuration reconciliation; exclusions and external dependencies | E1+E2+E6 | S3 | An unclear material boundary or unreconciled architecture blocks a final conclusion for the affected area. |
| CG-03 | Critical dependency visibility | Dependency graph; source/route/provider evidence; common-mode and concentration analysis; ownership | E1+E2+E7 | S4 | A critical hidden dependency remains UNKNOWN, or FAIL if demonstrated unidentified or unowned. |
| CG-04 | Life safety and hazardous energy | Authorised engineering/safety records; arc-flash and hazard studies; inspection; permits; tests; unresolved hazard status | E1+E4+E5 | S4 | An unsafe unresolved condition blocks relevant assurance and any hazardous testing in the affected area. |
| CG-05 | Resilient electrical supply | SLD; protection/coordination and capacity study; UPS/BESS/generator tests; fuel; maintenance; EPMS/incident evidence | E1+E2+E3+E4 | S5 | Missing critical continuity evidence gives UNKNOWN; demonstrated inability gives FAIL. |
| CG-06 | Thermal continuity | Thermal design/model; P&ID; capacity/flow telemetry; leak/transfer/failover tests; maintenance | E1+E2+E3+E4 | S5 | An unverified critical heat-removal path gives UNKNOWN; demonstrated shortfall gives FAIL. |
| CG-07 | Critical control-system integrity | BMS/EPMS/CDU/PLC/SCADA architecture; configuration and logic; identity/authority; telemetry; fail-safe tests | E1+E2+E3+E4 | S4 | Uncontrolled or unverifiable critical automation limits or blocks assurance. |
| CG-08 | Compute, storage and network functional integrity | Current topology/configuration; capacity/performance telemetry; error data; failover/recovery tests | E2+E3+E4 | S4 | An unverified critical infrastructure function caps OPERATION/RESILIENCE assurance. |
| CG-09 | Failure containment | Fault-domain model; isolation design; scenario analysis; containment tests/incidents | E1+E2+E4+E7 | S4 | Absent or failed containment may be FAIL; an untested critical boundary is UNKNOWN. |
| CG-10 | Recovery readiness | Recovery plan; prerequisites; configuration/data sources; exercises/tests; defects and sign-off | E1+E2+E3+E4 | S5 | A plan without representative test supports DESIGN only, not recoverability. |
| CG-11 | Evidence sufficiency | Evidence requirements; manifest; quality/sufficiency assessments; conflicts and limitations | E1+E7 | S4 | Failure to meet the evidence floor blocks the dependent claim. |
| CG-12 | Critical UNKNOWN | UNKNOWN register with type and severity; consequence; resolution ownership; evidence requests; decision ceiling | E1+E7 | S3 | An undispositioned US4/US5 UNKNOWN caps or blocks assurance. |
| CG-13 | Responsibility and authority | RACI; delegations; owner/operator/provider clauses; escalation; decision authority | E1+E6 | S3 | An unowned critical function or dependency blocks accountable disposition. |
| CG-14 | Change control | Baseline; change request; impact analysis; test/rollback; approval; post-change validation | E1+E2+E3+E4 | S4 | Material uncontrolled change suspends affected evidence and decision. |
| CG-15 | Integrated digital authority over infrastructure | Identity and privilege records; reachability; control-plane interfaces; session logs; action/rollback tests | E2+E3+E4+E7 | S4 | Unverified consequential authority remains a US4 UNKNOWN. |

**EVM-REQ-025** Evidence for a critical gate shall not be substituted below its mandatory class or quality floor merely to produce a complete scorecard.

# Part XIV - Conflict, contradiction and UNKNOWN

## 33. Evidence relationship states

| **State** | **Meaning** |
|---|---|
| SUPPORTS | Evidence increases support for a precise assertion. |
| CHALLENGES | Evidence weakens or contradicts assertion. |
| QUALIFIES | Evidence narrows scope or conditions. |
| INCOMPLETE | Evidence covers only part of requirement. |
| STALE | Evidence no longer represents current state. |
| INACCESSIBLE | Evidence is believed to exist but cannot be reviewed. |
| UNVERIFIED | Origin, integrity or method is not sufficiently established. |
| SUPERSEDES | New object replaces current use while preserving history. |
| DUPLICATES | Same underlying source is represented more than once. |
| CONFLICTS_WITH | Two supported propositions are materially incompatible. |

SUPPORTS, CHALLENGES, QUALIFIES and SUPERSEDES are canonical graph relationships (AIDCF-014 §9). INCOMPLETE, STALE, INACCESSIBLE, UNVERIFIED, DUPLICATES and CONFLICTS_WITH are evidence-assessment states recorded on the EvidenceAssessment; in the graph, a conflict is expressed as CHALLENGES between the conflicting evidence and assertion plus an EvidenceConflict node.

## 34. Conflict workflow

Detect -\> register separate assertions -\> preserve both evidence lineages -\> assess scope/time/state differences -\> seek corroboration -\> competent review -\> resolve, bound or escalate -\> update decision while preserving history

## 35. UNKNOWN types

| **Code** | **Type** | **Definition** |
|---|---|---|
| U1 | Missing | Expected evidence not produced. |
| U2 | Inaccessible | Evidence exists but access is restricted or unavailable. |
| U3 | Stale | Evidence does not represent current state. |
| U4 | Conflicting | Material sources disagree. |
| U5 | Coverage gap | Required population, state, period or scenario not represented. |
| U6 | Source unverified | Origin/authority cannot be established. |
| U7 | Integrity uncertain | Alteration or custody cannot be ruled out. |
| U8 | Method uncertain | Collection/test method insufficiently defined. |
| U9 | Interpretation unresolved | Competent reviewers cannot yet determine meaning. |
| U10 | Dependency unknown | Evidence cannot establish a material external/shared dependency. |

**EVM-REQ-026** Each UNKNOWN Record shall identify subject, missing attribute, type (U1–U10), severity (US1–US5) with the test that determined it, reason, potential consequence, evidence needed, owner if known, status and decision/gate impact.

## 35A. UNKNOWN severity

Type explains why something is unknown; severity states what it could change. Severity is determined by applying the tests below top-down and assigning the first that applies. The same type can take any severity.

| **Code** | **Name** | **Test (first that applies, top-down)** | **Decision effect** |
|---|---|---|---|
| US5 | Systemic | Affects the assessment boundary, a Capability Instance or Service Outcome definition, or two or more gates. | Decision ≤ INCONCLUSIVE. |
| US4 | Critical | Affects a gate-critical control (a control with a CRITICAL mapping for an in-scope gate) or a gate criterion; triggers CG-12. | Gate → UNKNOWN; decision ≤ LIMITED or INCONCLUSIVE per that gate's UNKNOWN ceiling (AIDCF-010). |
| US3 | Material | Could change a control result or a decision condition, but affects no gate. | Decision ≤ CONDITIONALLY_ASSURED; a condition is recorded. |
| US2 | Moderate | Affects confidence but could not change any result. | Confidence ceiling CONF-2 for affected claims. |
| US1 | Low | No plausible effect on any result or condition. | Record only. |

How each UNKNOWN type is graded. The guidance below states what the assessor examines for each type when applying the test; it does not replace the test.

| **Type** | **Grading question** | **Typical outcome** |
|---|---|---|
| U1 Missing | What does the missing item support? If it is a mandatoryItem in the profile of a gate-critical control, or the evidence for a gate criterion, US4. If it is a mandatoryItem of a non-critical control, US3 (result becomes UNKNOWN). If an alternative item already meets the floor, US2 or US1. | US3; US4 for gate-critical controls; US5 if the missing item is the approved boundary or outcome definition. |
| U2 Inaccessible | Would access plausibly reveal a different result? Restricted provider evidence for a dependency on which a gate relies (for example a utility or colocation provider's maintenance records) is US4; where accessible corroborating evidence meets the floor, US2. | US3/US4; never downgraded on the assertion of the evidence holder alone. |
| U3 Stale | Has a material change occurred since observation (§20 triggers)? If yes and the claim concerns current state of a gate-critical control, US4; if no change is evidenced and only the nominal window has lapsed, US2. | US2–US4 depending on change evidence. |
| U4 Conflicting | Do the conflicting propositions lead to different results? If one proposition would make a gate-critical control NONCONFORMING, US4; if both lead to the same result, US2. | US3/US4 until resolved under §34. |
| U5 Coverage gap | Is the uncovered population, state or scenario one the Service Outcome tolerance depends on (for example the MAINTENANCE or DEGRADED state for a concurrently maintainable path)? If so and the control is gate-critical, US4; if the gap is the declared operating envelope itself, US5. | US3/US4; US5 where it spans the envelope or ≥ 2 gates. |
| U6 Source unverified | Is the item decisive? An unverified source for the only evidence of a gate criterion is US4; where corroborated by an independent verified source, US2. | US3/US4. |
| U7 Integrity uncertain | Could undetected alteration change the result? Integrity doubt over test or configuration evidence for a gate-critical control is US4; a suspected custody breach affecting evidence across several gates is US5 and is also treated as an evidence nonconformance (§47). | US4/US5 for decisive evidence. |
| U8 Method uncertain | Could the method have failed to detect a nonconforming condition (F below 4 for a test)? If so for a gate-critical claim, US4; otherwise US3. | US3/US4. |
| U9 Interpretation unresolved | Do the competing interpretations give different results? Grade in the same way as U4. | US2–US4. |
| U10 Dependency unknown | Does the unknown dependency affect a redundancy, independence or recovery claim? If it could create a common mode across paths relied on by one gate, US4 (CG-03); across two or more gates (for example a shared controller or shared utility path behind both power and cooling), US5. | US4/US5. |

**EVM-REQ-027** Severity shall be assigned by the assessor using the top-down test, recorded with the test that determined it, and reviewed by the independent reviewer for every US3, US4 and US5 UNKNOWN.

**EVM-REQ-028** An UNKNOWN Record's severity shall not be downgraded without new evidence or an approved boundary change, and the prior severity, rationale and approver shall be retained.

# Part XV - Derived, automated and AI-generated evidence

## 36. Derived evidence rules

- Retain every source Evidence ID and the transformation method.

- Record query, script, model, parameters, assumptions and version.

- Do not assign a quality dimension higher than source support without independent corroboration relevant to that dimension.

- Distinguish deterministic transformation from interpretive inference.

- Preserve failed, excluded and conflicting source records where material.

- Recalculate or invalidate derived evidence when a source changes or is withdrawn.

## 37. AI-assisted evidence

| **Use** | **Permitted status** | **Required safeguards** |
|---|---|---|
| Classification/extraction | Candidate | Source link, model/version, prompt/process record, review and sampling. |
| Summarisation | Candidate workpaper | Traceable citations to source passages and reviewer verification. |
| Anomaly detection | Signal/candidate | Baseline, sensitivity, false-positive/negative review and corroboration. |
| Path inference | Candidate graph assertion | Approved semantics, source evidence and accountable human review. |
| Quality scoring | Recommendation | Transparent inputs/rules and override rationale. |
| Final finding/decision | Not autonomous | Competent accountable human approval required. |

**EVM-REQ-029** AI-generated text or graph content shall not be treated as independent corroboration of the source data from which it was generated.

# Part XVI - Evidence lifecycle and review workflow

## 38. Lifecycle

Plan -\> Request -\> Collect -\> Identify -\> Validate -\> Classify -\> Protect -\> Assess Quality -\> Link to Assertion -\> Assess Sufficiency -\> Review Conflict/UNKNOWN (type and severity) -\> Accept or Reject -\> Use in Decision -\> Monitor Timeliness -\> Supersede/Retain/Destroy

## 39. Role model

| **Role** | **Responsibility** |
|---|---|
| Evidence owner | Accountable for source availability, quality and authorised use. |
| Collector | Acquires evidence under approved method and records provenance. |
| Custodian | Protects, versions, retains and controls access. |
| Technical specialist | Evaluates engineering or technical meaning. |
| Assessor | Links evidence to criteria and assertions; assigns UNKNOWN type and severity. |
| Independent reviewer | Challenges sufficiency, conflict, UNKNOWN severity and decision use. |
| Decision owner | Authorises bounded conclusion and conditions. |
| Privacy/security/legal reviewer | Determines handling, redaction, disclosure and hold obligations. |
| Tool/system owner | Maintains collection and transformation integrity. |

## 40. Evidence request record

| **Field** | **Content** |
|---|---|
| requestId | Stable identifier. |
| decision/assertion/control | Why evidence is required. |
| requested class/floor | Classes, metadata, quality, period, state and format. |
| source/owner | Expected provider and accountable owner. |
| authority/purpose | Permitted collection and use. |
| due/review trigger | Operational scheduling field. |
| received/status | Collected, partial, inaccessible, rejected or UNKNOWN. |
| handling | Classification, transfer and retention. |
| substitution | Alternative evidence and approval rationale. |
| escalation | Decision and gate effect of non-production, including the UNKNOWN severity that will apply. |

# Part XVII - Evidence security, privacy and disclosure

## 41. Classification levels

| **Level** | **Examples** | **Handling intent** |
|---|---|---|
| PUBLIC | Published methodology, synthetic examples. | Approved public release. |
| INTERNAL | General workpapers and non-sensitive procedures. | Authenticated organisational access. |
| CONFIDENTIAL | Client architecture, contracts, findings and operational records. | Need-to-know, encryption, restricted export. |
| RESTRICTED | Facility layouts, configurations, identities, routes and security evidence. | Strong access approval, logging and controlled sharing. |
| HIGHLY RESTRICTED | Combined physical/digital paths, secrets, live control authority. | Segregated storage, minimal access and sanitised reporting. |
| LEGAL HOLD | Any evidence under preservation obligation. | No deletion or unapproved alteration. |

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

| **Node** | **Purpose** |
|---|---|
| EvidenceObject | Addressable source item. |
| EvidenceSet | Assertion-specific collection. |
| EvidencePackage | Control/system/gate package. |
| EvidencePortfolio | Capability-level evidence collection. |
| EvidenceRequirement | Required class and threshold. |
| EvidenceAssessment | Quality and sufficiency judgment. |
| EvidenceSource | Originating system/person/provider. |
| CollectionActivity | Acquisition event. |
| TransformationActivity | Derived evidence process. |
| CustodyEvent | Access/transfer/change event. |
| Assertion | Proposition supported/challenged. |
| UnknownRecord | Missing or unresolved evidence condition with type and severity. |
| EvidenceConflict | Contradictory evidence relationship. |
| ReviewRecord | Human challenge/approval. |
| Decision | Bounded Assurance Decision. |

The canonical object classes for exchange are those of AIDCF-014 §7; the nodes above are the evidence-model view and map onto those classes.

## 44. Core graph relationships

| **Predicate** | **Meaning** | **Canonical AIDCF-014 §9 relationship** |
|---|---|---|
| SUPPORTS | Evidence supports a precise assertion. | SUPPORTS |
| CHALLENGES | Evidence weakens or contradicts assertion. | CHALLENGES |
| QUALIFIES | Evidence limits scope/conditions. | QUALIFIES |
| SATISFIES_REQUIREMENT | Evidence package meets requirement. | Evidence-model extension; exchanged as EVIDENCED_BY on the requirement with an assessment result. |
| COLLECTED_BY / GENERATED_BY / DERIVED_FROM | Provenance of an object. | Evidence-model extension (PROV-DM aligned). |
| OBSERVES / COVERS | Evidence records an entity/state, or covers scope, state, period or population. | Evidence-model extension. |
| VALIDATES | Test evidence evaluates a safeguard or claim. | SUPPORTS or CHALLENGES with claim type EFFECTIVENESS/RESILIENCE. |
| CONFLICTS_WITH | Objects/assertions materially disagree. | CHALLENGES plus EvidenceConflict. |
| SUPERSEDES | New object replaces current use. | SUPERSEDES |
| MEMBER_OF / CUSTODIAN_OF | Package membership; custody. | Evidence-model extension. |
| LIMITS | UNKNOWN/limitation constrains conclusion. | CONSTRAINS |
| EVIDENCES_GATE | Package contributes to Gate Result. | EVIDENCED_BY (Gate Result EVIDENCED_BY package) |

## 45. Publication package

| **File** | **Purpose** |
|---|---|
| aidcf-evm-v1.1.owl / .ttl | Formal evidence ontology and RDF/Turtle serialisation (namespace https://w3id.org/aidcf/ontology#; w3id registration pending). |
| aidcf-evm-context-v1.1.jsonld | JSON-LD context. |
| evidence-object-schema-v1.1.json | EvidenceObject exchange schema. |
| evidence-package-schema-v1.1.json | Package/portfolio schema. |
| aidcf-evm-shapes-v1.1.ttl | SHACL validation shapes. |
| evidence-types-v1.1.csv | Type registry (Appendix A). |
| quality-ratings-v1.1.csv | Quality dimension anchors (Appendix B). |
| AIDCF-007A registry evidenceProfile | Control Evidence Requirement Profiles for all 360 controls (Appendix C); no separate profile matrix is maintained in this artifact. |
| registries/gates/critical-gates.csv and critical-gate-criteria.csv | Gate evidence profile and criteria register (Appendix D). |
| retention-classes-v1.1.csv | Retention definitions. |
| conformance-tests/ | Positive, negative, migration and security fixtures. |
| CHANGELOG.md / MIGRATION.md | Version history and transition guidance, including the Annex G requirement mapping. |

# Part XIX - Conformance, validation and nonconformance

## 46. Validation rules

| **Rule** | **Validation statement** |
|---|---|
| EVM-VAL-001 | Every EvidenceObject has stable ID, class, source, scope, observation time, classification and review state. |
| EVM-VAL-002 | Every accepted material EvidenceObject links to at least one assertion or requirement, with subject and period. |
| EVM-VAL-003 | Every derived object links to sources and transformation activity. |
| EVM-VAL-004 | Every quality rating has rationale and reviewer. |
| EVM-VAL-005 | Every evidence package evaluates timeliness, coverage, conflict and sufficiency. |
| EVM-VAL-006 | Every Gate Result references its evidence requirement and package. |
| EVM-VAL-007 | Every missing mandatory item creates an UNKNOWN Record or an explicit adverse result. |
| EVM-VAL-008 | No UNKNOWN is encoded as favourable pass or numeric zero. |
| EVM-VAL-009 | No evidence item is treated as universal proof across unreviewed assertions. |
| EVM-VAL-010 | Every stale/superseded object remains historically traceable. |
| EVM-VAL-011 | Every restricted item has handling and access metadata. |
| EVM-VAL-012 | Every AI-generated assertion remains candidate until approved. |
| EVM-VAL-013 | Every evidence deletion has authorised destruction record unless prohibited by hold. |
| EVM-VAL-014 | Every test evidence object records initial state, method, conditions and anomalies. |
| EVM-VAL-015 | Every Assurance Decision links to an immutable evidence manifest or snapshot. |
| EVM-VAL-016 | Every UNKNOWN Record has a type U1–U10 and a severity US1–US5 with the determining test recorded. |
| EVM-VAL-017 | Every control Evidence Package cites the AIDCF-007A registry version of the Evidence Requirement Profile applied. |
| EVM-VAL-018 | Confidence records use CONF-0 to CONF-4 and do not exceed the ceilings in §27. |

## 47. Evidence nonconformance classes

| **Class** | **Examples** | **Decision treatment** |
|---|---|---|
| Critical | Fabricated/falsified evidence; concealed material conflict; unsafe unauthorised collection; custody breach affecting critical claim. | Stop use, preserve records, escalate, independently investigate and suspend affected decision (CG-11 FAIL in AIDCF-010). |
| Major | Missing provenance; unsupported effectiveness; stale critical evidence; incomplete gate package; hidden UNKNOWN. | Reject/limit evidence and reassess conclusion. |
| Minor | Non-material metadata defect or formatting inconsistency. | Correct and record. |
| Observation | Improvement opportunity without current decision impact. | Track through quality process. |

# Part XX - Worked evidence packages

## 48. Power continuity package

| **Component** | **Example** |
|---|---|
| Assertions | Required power continuity and resilient capacity exist for declared load and states (claim types OPERATION and RESILIENCE). |
| E1 | SLD, design basis, protection/coordination and capacity study, switching and fuel procedures. |
| E2 | Protection settings, UPS/generator/EPMS configuration, asset inventory. |
| E3 | Load, runtime, fuel, alarms, maintenance and incident evidence. |
| E4 | Generator start/transfer, UPS runtime, load-step and restoration tests. |
| E5 | Independent engineering/witness review where required. |
| Quality focus | Current load/configuration (T), representative states (C), shared dependencies, test safety. |
| Gate | CG-05; evidence floor S5. |
| UNKNOWN example | Unverified shared bus or fuel replenishment autonomy: U10/U1, graded US4 because fuel autonomy and replenishment is a CG-05 gate criterion (GC-05-5). |
| Decision limit | No resilience conclusion beyond tested load, duration and states. |

## 49. Liquid cooling package

| **Component** | **Example** |
|---|---|
| Assertions | Heat removal remains within envelope under NORMAL and defined DEGRADED states. |
| E1 | P&ID, thermal model, design limits, water/coolant specification. |
| E2 | CDU, controller, setpoint, sensor and loop configuration. |
| E3 | Flow, temperature, pressure, leak, quality and alarm telemetry. |
| E4 | Failover, isolation, leak response and thermal recovery test. |
| E5 | Specialist engineering review for high-consequence or novel architecture. |
| Quality focus | Sensor trust, seasonal condition, transient response and shared loop dependencies. |
| Gate | CG-06; evidence floor S5. |
| UNKNOWN example | Secondary-loop autonomy not verified at peak load: U5 coverage gap, graded US4 because it affects gate criterion GC-06-3 (secondary-loop envelope at peak load). |
| Decision limit | No generalisation from steady low load to full transient AI demand. |

## 50. Compute-storage-network package

| **Component** | **Example** |
|---|---|
| Assertions | Required usable performance, integrity and recovery are sustained for defined Service Outcomes. |
| E1 | Cluster/fabric/storage architecture and compatibility basis. |
| E2 | Firmware, driver, topology, scheduler and storage configurations. |
| E3 | Accelerator errors, fabric congestion, storage performance, capacity and incident records. |
| E4 | Benchmark, node/fabric failure, checkpoint and restore tests. |
| E5 | Independent validation where required. |
| Quality focus | Representative workload, topology version, error gaps and failure-domain coverage. |
| Gate | CG-08 and CG-10. |
| UNKNOWN example | Checkpoint recovery not tested after correlated metadata/fabric disruption: U5, graded US5 because it affects both CG-08 and CG-10. |
| Decision limit | Performance evidence does not prove recovery or integrity unless directly assessed. |

## 51. Digital authority over infrastructure

| **Component** | **Example** |
|---|---|
| Assertions | Only approved identities can cause consequential infrastructure actions within stated conditions. |
| E1 | Access policy, responsibility and remote-support process. |
| E2 | Identity, role, permission, gateway and controller configuration. |
| E3 | Authentication, session, command, change and revocation logs. |
| E4 | Authorised access-path, command restriction and revocation tests. |
| E7 | Integrated authority-path analysis using AIDCF-005 semantics. |
| Quality focus | Effective identity, inherited privilege, dormant routes, provider access and rollback. |
| Gate | CG-15. |
| UNKNOWN example | Remote OEM command scope cannot be independently verified: U2/U6, graded US4. |
| Decision limit | Reachability alone does not prove authority or realised physical effect. |

# Appendix A - Evidence type registry

Each subtype is a controlled narrower term of its class. A capability profile may add narrower terms beneath a subtype without redefining the parent class.

| **Subtype ID** | **Class** | **Preferred label** |
|---|---|---|
| E1-01 | E1 | Policy |
| E1-02 | E1 | Standard |
| E1-03 | E1 | Procedure |
| E1-04 | E1 | Runbook |
| E1-05 | E1 | Design Basis |
| E1-06 | E1 | Architecture Diagram |
| E1-07 | E1 | Single-Line Diagram |
| E1-08 | E1 | P&ID |
| E1-09 | E1 | As-Built Drawing |
| E1-10 | E1 | Contract |
| E1-11 | E1 | SLA |
| E1-12 | E1 | Attestation |
| E1-13 | E1 | Inventory |
| E1-14 | E1 | Risk Record |
| E2-01 | E2 | Device Configuration |
| E2-02 | E2 | Protection Setting |
| E2-03 | E2 | Firmware Baseline |
| E2-04 | E2 | Driver Matrix |
| E2-05 | E2 | Cluster Manifest |
| E2-06 | E2 | Scheduler Policy |
| E2-07 | E2 | Access Policy |
| E2-08 | E2 | Topology Export |
| E2-09 | E2 | Controller Logic |
| E2-10 | E2 | Configuration Snapshot |
| E2-11 | E2 | Golden Image |
| E3-01 | E3 | Telemetry Series |
| E3-02 | E3 | Event Log |
| E3-03 | E3 | Alarm Record |
| E3-04 | E3 | Capacity Metric |
| E3-05 | E3 | Performance Metric |
| E3-06 | E3 | Work Order |
| E3-07 | E3 | Maintenance Record |
| E3-08 | E3 | Incident Record |
| E3-09 | E3 | Change Record |
| E3-10 | E3 | Access Log |
| E3-11 | E3 | Video/Photo Observation |
| E3-12 | E3 | Inspection Record |
| E4-01 | E4 | Commissioning Test |
| E4-02 | E4 | Functional Test |
| E4-03 | E4 | Load Test |
| E4-04 | E4 | Failover Test |
| E4-05 | E4 | Recovery Test |
| E4-06 | E4 | Scenario Exercise |
| E4-07 | E4 | Simulation |
| E4-08 | E4 | Calibration Result |
| E4-09 | E4 | Witnessed Demonstration |
| E4-10 | E4 | Penetration/Control Test when authorised |
| E5-01 | E5 | Independent Engineering Review |
| E5-02 | E5 | Third-Party Assessment |
| E5-03 | E5 | Audit Report |
| E5-04 | E5 | Accredited Certificate |
| E5-05 | E5 | Laboratory Result |
| E5-06 | E5 | Provider Assurance Report |
| E5-07 | E5 | Regulatory Inspection |
| E5-08 | E5 | Independent Witness Record |
| E6-01 | E6 | Interview Record |
| E6-02 | E6 | Workshop Record |
| E6-03 | E6 | Walkthrough |
| E6-04 | E6 | Operator Demonstration |
| E6-05 | E6 | Expert Judgment |
| E6-06 | E6 | Shift Observation |
| E6-07 | E6 | Competency Record |
| E6-08 | E6 | Training Record |
| E7-01 | E7 | Trend Analysis |
| E7-02 | E7 | Correlation Analysis |
| E7-03 | E7 | Capacity Model |
| E7-04 | E7 | Failure Analysis |
| E7-05 | E7 | Dependency Graph |
| E7-06 | E7 | Reconciled Inventory |
| E7-07 | E7 | Evidence Quality Assessment |
| E7-08 | E7 | Score/Rating Output |
| E7-09 | E7 | AI-Assisted Extraction |
| E7-10 | E7 | Query Result |

# Appendix B - Quality rating matrix

Compact view of the anchors in §17 for tooling and rating sheets.

| **Rating** | **P Provenance** | **F Fitness** | **C Coverage** | **R Reliability** | **T Timeliness** | **I Integrity** |
|---|---|---|---|---|---|---|
| 0 | Unknown origin | Not established / unlinked | Unknown coverage | Unassessed | Unknown age or state | Unknown integrity |
| 1 | Identified, uncontrolled source | Indirect subject | Anecdotal or isolated | Weak/uncontrolled method | Obsolete for represented state | Basic repository controls |
| 2 | Accountable internal source | Partial: other claim type, version or state | Limited sample/state | Plausible, lightly corroborated | Stale or change-sensitive | Verified source copy |
| 3 | Controlled authoritative source | Relevant and linked to assertion | Representative core scope | Controlled repeatable method | Acceptable for decision | Hash verified |
| 4 | Corroborated authoritative source | Specific to criterion, version and states | Broad scope and relevant states | Strong, independently corroborated | Current and aligned to baseline | Signature/timestamp verified |
| 5 | Independently verified origin and lineage | Discriminating for the criterion | Comprehensive population, period and states | Validated method, independent verification | Near-real-time, healthy collection | Tamper-evident end-to-end custody |

# Appendix C - Control Evidence Requirement Profile register

The 360 Evidence Requirement Profiles are carried in the AIDCF-007A Canonical Master Control Registry (evidenceProfile of each control record; CSV exports flatten array fields with ";" separators). The register uses exactly the thirteen fields in §31: claimType, profileTier, requiredClasses, optionalClasses, qualityFloor, sufficiencyFloor, stateCoverage, periodCoverage, independence, mandatoryItems, acceptableAlternatives, unknownEffect, reassessmentTriggers.

Register validation rules:

- claimType is consistent with requiredAssuranceLevel (DESIGN–AL2, IMPLEMENTATION–AL3, OPERATION–AL4, EFFECTIVENESS/RESILIENCE–AL5).

- requiredClasses satisfy the claim-type minimum pattern in §29 and the tier pattern in §32.

- qualityFloor names all six dimensions; sufficiencyFloor is S2–S5 and is at least S4 for CP-4 and S5 (or a documented strong floor) for CP-5.

- stateCoverage uses canonical operating states only and includes every state in which the control is claimed to operate.

- unknownEffect states a US severity; it is at least US4 where the control has a CRITICAL gate mapping (§31).

- mandatoryItems are specific to the control; no profile reuses another's mandatoryItems verbatim unless the evidence is genuinely identical.

# Appendix D - Critical-gate evidence register

The normative gate evidence profiles are in Part XIII. The machine-readable register is registries/gates/critical-gates.csv (gateId, name, scope, evidenceFloor, requiredClasses, failCeiling, unknownCeiling, approvedNaConditions, ownerArtifact), and the gate criteria with their evidence and test methods are in registries/gates/critical-gate-criteria.csv. Gate criteria, roll-up and decision ceilings are owned by AIDCF-010.

# Appendix E - Record schemas

## E.1 EvidenceObject

| **Property** | **Cardinality** | **Type** |
|---|---|---|
| evidenceId | 1 | Identifier (immutable) |
| title | 1 | String |
| description | 0..1 | String |
| evidenceClass | 1 | Controlled value E1–E7 |
| subtype | 0..1 | Controlled value (Appendix A) |
| sourceId | 1 | Reference to EvidenceSource |
| owner | 1 | Reference to party/role |
| custodian | 0..1 | Reference to party/role |
| collector | 0..1 | Reference to agent |
| collectionMethod | 0..1 | Controlled value (assessment method code) |
| observationTime | 1 | Date-time or interval |
| collectionTime | 0..1 | Date-time |
| recordTime | 0..1 | Date-time |
| effectivePeriod | 0..1 | Interval |
| subjectRefs | 0..\* | References to subjects (assets, controls, gates, assertions) |
| scope | 0..1 | Structured scope (locations, population, operating states) |
| configurationVersion | 0..1 | Reference to baseline/version |
| integrityMethod | 0..1 | Controlled value |
| hash | 0..\* | Digest with algorithm |
| classification | 1 | Controlled value (§41) |
| retentionRule | 0..1 | Retention class (§21) with trigger |
| qualityAssessment | 0..\* | Quality vector per use (P/F/C/R/T/I with rationale) |
| reviewState | 1 | Controlled value (§9) |
| limitations | 0..\* | String |
| relatedEvidence | 0..\* | Typed reference (source, derivative, conflict, supersession, membership) |

## E.2 EvidenceAssessment

| **Property** | **Meaning** |
|---|---|
| assessmentId | Stable ID. |
| assertionOrRequirement | Precise evaluation target. |
| evidenceRefs | Items assessed. |
| qualityVector | P/F/C/R/T/I ratings and rationale. |
| sufficiency | S0–S5 and rationale. |
| confidence | CONF-0 to CONF-4, flags and rationale. |
| conflictsAndUnknowns | Unresolved conditions with UNKNOWN type and severity. |
| reviewer/competence | Accountable reviewer. |
| date/snapshot | Temporal and version context. |
| decisionEffect | Result, Finding, gate or claim ceiling. |

## E.3 EvidenceManifest

| **Property** | **Meaning** |
|---|---|
| manifestId/version | Immutable package identity. |
| package/portfolio | Parent scope. |
| evidenceItems | IDs, hashes, versions, locations and states. |
| missingItems | Expected but absent objects. |
| restrictedItems | Protected references and access rules. |
| supersession | Replaced objects and lineage. |
| signature/timestamp | Manifest integrity method. |
| review/approval | Release roles and date. |

## E.4 UnknownRecord

| **Property** | **Meaning** |
|---|---|
| unknownId | Stable ID. |
| subject | Control assessment, gate criterion, dependency, boundary element or outcome affected. |
| type | U1–U10. |
| severity | US1–US5, the determining test, assessor and reviewer. |
| missingAttribute/reason | What is unknown and why. |
| potentialConsequence | Which result, gate, condition or decision could change. |
| evidenceNeeded | Evidence request reference. |
| owner/status/dates | Resolution owner, status and target. |
| disposition | Resolved, bounded by approved boundary change, or carried with decision ceiling (AIDCF-010 CG-12). |
| severityHistory | Prior severities, rationale and approver. |

# Appendix F - Review and release gates

| **Review role** | **Status** | **Focus** |
|---|---|---|
| Methodology author | Draft completed | Evidence architecture coherence. |
| Assurance/evidence specialist | Pending | Quality, sufficiency, confidence and UNKNOWN severity model. |
| Electrical engineering | Pending | CG-05 evidence profile. |
| Mechanical/liquid cooling | Pending | CG-06 evidence profile. |
| Compute/storage/network | Pending | CG-08/CG-10 evidence profile. |
| Operations/reliability | Pending | Operational and recovery evidence. |
| OT/cybersecurity | Pending | Control-plane, identity and logging evidence. |
| Ontology/graph | Pending | Evidence classes/relationships and AIDCF-005/AIDCF-014 alignment. |
| Data/privacy/security | Pending | Classification, minimisation and handling. |
| Legal/records management | Pending | Retention, legal hold and disclosure. |
| Certification/accreditation | Pending | Evidence floors and scheme implications. |
| Independent practitioner | Pending | Usability and reproducibility. |
| Public release | Not approved | Mandatory review gates closed. |

## Acceptance criteria

- All AIDCF-007A controls carry a complete Evidence Requirement Profile in the registry that passes the Appendix C validation rules.

- Evidence quality dimensions remain visible and non-compensating where claim-critical.

- UNKNOWN, conflicts and stale evidence cannot be hidden by scoring; every UNKNOWN carries type and severity.

- Critical-gate evidence floors are enforceable.

- Human and machine-readable records preserve provenance and review.

- Security, privacy, retention and lawful handling are operationally usable.

- AIDCF-009 can directly consume the model for assessment procedures, and AIDCF-010 for results, gates and decisions.

## Change record

| **Version** | **Status** | **Summary** |
|---|---|---|
| 0.1 | Architecture draft | Evidence doctrine, hierarchy and taxonomy. |
| 0.5 | Integrated draft | Quality, sufficiency, gate, graph and lifecycle models. |
| 1.0 | Controlled-review draft | Full evidence standard and 360-control profile approach. |
| 1.1 | Draft for controlled review | Alignment to the canonical specification: AIDCF-007A, EC0–EC5, P/F/C/R/T/I meanings, confidence flags, UNKNOWN severity, registry-carried profiles, consecutive requirement IDs. |

# Annex G - Requirement identifier mapping (v1.0 to v1.1)

Requirement identifiers are numbered consecutively in v1.1. EVM-SEC and EVM-VAL identifiers are unchanged (EVM-VAL-016 to EVM-VAL-018 are new).

| **v1.0 ID** | **v1.1 ID** |
|---|---|
| EVM-REQ-001 | EVM-REQ-001 |
| EVM-REQ-002 | EVM-REQ-002 |
| EVM-REQ-003 | EVM-REQ-003 |
| EVM-REQ-004 | EVM-REQ-004 |
| EVM-REQ-005 | EVM-REQ-005 |
| EVM-REQ-006 | EVM-REQ-006 |
| EVM-REQ-007 | EVM-REQ-007 |
| EVM-REQ-008 | EVM-REQ-008 |
| EVM-REQ-009 | EVM-REQ-009 |
| EVM-REQ-010 | EVM-REQ-010 |
| EVM-REQ-011 | EVM-REQ-011 |
| EVM-REQ-012 | EVM-REQ-012 |
| — (new in v1.1) | EVM-REQ-013 |
| EVM-REQ-015 | EVM-REQ-014 |
| EVM-REQ-016 | EVM-REQ-015 |
| — (new in v1.1) | EVM-REQ-016 |
| — (new in v1.1) | EVM-REQ-017 |
| — (new in v1.1) | EVM-REQ-018 |
| EVM-REQ-021 | EVM-REQ-019 |
| — (new in v1.1) | EVM-REQ-020 |
| EVM-REQ-027 | EVM-REQ-021 |
| EVM-REQ-028 | EVM-REQ-022 |
| — (new in v1.1) | EVM-REQ-023 |
| — (new in v1.1) | EVM-REQ-024 |
| EVM-REQ-033 | EVM-REQ-025 |
| EVM-REQ-035 | EVM-REQ-026 |
| — (new in v1.1) | EVM-REQ-027 |
| — (new in v1.1) | EVM-REQ-028 |
| EVM-REQ-037 | EVM-REQ-029 |

## Final doctrine

Evidence is the currency of AIDCF assurance. An evidence item has no universal authority outside its provenance, fitness, scope, time, state, method and assertion. A strong-looking package cannot compensate for a missing mandatory class, critical coverage gap, unresolved conflict or failed gate. When evidence cannot support the requested conclusion, AIDCF preserves UNKNOWN, grades its severity, states the limitation and withholds stronger assurance rather than manufacturing certainty.
