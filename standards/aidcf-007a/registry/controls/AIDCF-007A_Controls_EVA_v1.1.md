# AIDCF-007A Control Catalogue — EVA Evidence, Assessment and Assurance Management

Registry v1.1 (AIDCF-007A-AMD-002), 2026-10-10 — **PROPOSED, Draft for controlled review**. Generated from `registries/controls/controls.json`; the registry workbook governs. Domain guide: [AIDCF-018-EVA](../../../aidcf-018-domain-guides/AIDCF-018-EVA_Evidence_Assessment_and_Assurance_Domain_Guide_v1.0.md).

## Summary

| Control | Title | Type | Claim type | AL | CRITICAL gates | SUPPORTING gates |
|---|---|---|---|---|---|---|
| [MCF-EVA-001](#mcf-eva-001) | Evidence Taxonomy | DIRECTIVE | DESIGN | AL2 | — | — |
| [MCF-EVA-002](#mcf-eva-002) | Evidence Ownership | DIRECTIVE | IMPLEMENTATION | AL3 | — | CG-13 |
| [MCF-EVA-003](#mcf-eva-003) | Evidence Repository | PREVENTIVE | IMPLEMENTATION | AL3 | — | — |
| [MCF-EVA-004](#mcf-eva-004) | Retention and Protection | RECOVERY | RESILIENCE | AL5 | — | — |
| [MCF-EVA-005](#mcf-eva-005) | Source Provenance | PREVENTIVE | OPERATION | AL4 | — | — |
| [MCF-EVA-006](#mcf-eva-006) | Integrity and Custody | DETECTIVE | EFFECTIVENESS | AL5 | — | — |
| [MCF-EVA-007](#mcf-eva-007) | Relevance and Reliability | PREVENTIVE | OPERATION | AL4 | — | — |
| [MCF-EVA-008](#mcf-eva-008) | Currency and Coverage | PREVENTIVE | OPERATION | AL4 | — | — |
| [MCF-EVA-009](#mcf-eva-009) | Decision Question | DIRECTIVE | DESIGN | AL2 | CG-01 | — |
| [MCF-EVA-010](#mcf-eva-010) | Scope and Criteria | DIRECTIVE | DESIGN | AL2 | CG-02 | — |
| [MCF-EVA-011](#mcf-eva-011) | Sampling and Testing | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-04 |
| [MCF-EVA-012](#mcf-eva-012) | Specialist Involvement | PREVENTIVE | IMPLEMENTATION | AL3 | — | — |
| [MCF-EVA-013](#mcf-eva-013) | Finding Traceability | DETECTIVE | OPERATION | AL4 | — | — |
| [MCF-EVA-014](#mcf-eva-014) | UNKNOWN Preservation | DETECTIVE | EFFECTIVENESS | AL5 | — | — |
| [MCF-EVA-015](#mcf-eva-015) | Conflict Handling | CORRECTIVE | OPERATION | AL4 | — | — |
| [MCF-EVA-016](#mcf-eva-016) | Limitation Disclosure | DETECTIVE | OPERATION | AL4 | — | — |
| [MCF-EVA-017](#mcf-eva-017) | Gate Applicability | DIRECTIVE | DESIGN | AL2 | — | — |
| [MCF-EVA-018](#mcf-eva-018) | Gate Evidence | PREVENTIVE | OPERATION | AL4 | — | — |
| [MCF-EVA-019](#mcf-eva-019) | Independent Decision | PREVENTIVE | IMPLEMENTATION | AL3 | — | CG-13 |
| [MCF-EVA-020](#mcf-eva-020) | Claim Language | PREVENTIVE | OPERATION | AL4 | — | — |
| [MCF-EVA-021](#mcf-eva-021) | Evidence Expiry | DETECTIVE | OPERATION | AL4 | — | — |
| [MCF-EVA-022](#mcf-eva-022) | Change Triggers | DETECTIVE | EFFECTIVENESS | AL5 | — | CG-14 |
| [MCF-EVA-023](#mcf-eva-023) | Monitoring Coverage | DETECTIVE | OPERATION | AL4 | — | — |
| [MCF-EVA-024](#mcf-eva-024) | Decision Suspension and Supersession | RECOVERY | RESILIENCE | AL5 | — | — |

## EVA-01 Evidence architecture

### MCF-EVA-001

**Evidence Taxonomy** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure that every in-scope control has an Evidence Requirement profile expressed in the AIDCF-008 vocabulary (classes E1-E7, quality floor, sufficiency floor, state and period coverage, independence), and that any local evidence subtypes map unambiguously to those classes.

**Requirement.** The evidence lead shall maintain, for every in-scope control, an Evidence Requirement profile using the AIDCF-008 classes, quality dimensions (P, F, C, R, T, I), sufficiency levels and control profile tiers, strengthened where the capability profile or criticality requires and never weakened below the registry profile. The evidence lead shall maintain a mapping of every local evidence subtype (for example 'EPMS waveform capture', 'CDU trend export', 'fabric link error report') to exactly one AIDCF-008 class.

**Assessment criteria**

1. Every in-scope control has an Evidence Requirement profile with claim type, profile tier, required classes, quality floor, sufficiency floor, state and period coverage and independence.
2. No profile is weaker than the AIDCF-007A registry profile for the same control and claim type.
3. Every local evidence subtype in use maps to exactly one AIDCF-008 class.
4. Profiles for gate-CRITICAL controls meet or exceed the evidence floor of each gate they map to.
5. The taxonomy uses the canonical vocabularies only (E1-E7 classes, Q0-Q5 bands, S0-S5 sufficiency, EC0-EC5 conformance levels) with no legacy grade codes.

**Minimum evidence**

- Evidence Requirement profiles for in-scope controls
- Local subtype-to-class mapping
- Comparison of local profiles to registry profiles
- Gate floor comparison for CRITICAL controls

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses | E2 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Profiles in force at the assessment date |
| independence | Comparison to registry profiles performed by the assessor using the published registry release |
| mandatoryItems | Evidence Requirement profiles for in-scope controls; Local subtype-to-class mapping |
| acceptableAlternatives | Profiles held as machine-readable records in the assessment tool, exported with version |
| unknownEffect | US3 Material: evidence sufficiency judgements for affected controls lack a stated basis; CG-11 evaluation records the gap |
| reassessmentTriggers | New AIDCF-008 or AIDCF-007A release adopted; New local evidence subtype introduced; Change in capability profile strengthening requirements |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Obtain profiles and check field completeness for every in-scope control.
2. Compare each profile with the registry profile and list weakenings.
3. Check the subtype-to-class mapping for unmapped or multiply mapped subtypes.
4. Compare profiles of gate-CRITICAL controls with gate evidence floors.
5. Screen for legacy vocabulary.

**Gate mappings.** None

**Applicability.** Applies to every programme that produces Control Assessments.

**Lifecycle stages.** PLAN, DESIGN, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Evidence requested ad hoc with no stated requirement; Local profile weaker than the registry; Subtype counted as E4 test evidence when it is E3 observation; Legacy grade codes cause inconsistent sufficiency judgements

**Testing safety.** Desk review of profiles and mappings; no evidence collection is involved.

**UNKNOWN rule.** If a control has no profile, its result is UNKNOWN (U8 method uncertain) until a profile is approved; the assessor shall not improvise a floor.

**Ontology classes.** EvidenceRequirement, Control, EvidenceObject · **Related controls.** MCF-EVA-003, MCF-EVA-007, MCF-EVA-018, MCF-GOV-004

**Informative references.** AIDCF-008 Evidence Model; ISO/IEC/IEEE 15026-2 (assurance case) - evidence; W3C PROV-DM (provenance data model)

### MCF-EVA-002

**Evidence Ownership** · DIRECTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that for every Evidence Requirement there is a named source owner responsible for producing the evidence, so that requests reach someone with access and authority, and missing evidence is attributable.

**Requirement.** The evidence lead shall assign, for each Evidence Requirement in an assessment, a source owner (person or role in the owner, operator or provider organisation) responsible for producing the evidence by the requested date, and shall record each request, response, delay and refusal in the evidence request record. Unfulfilled requests at the response deadline shall be escalated to the capability owner and recorded as UNKNOWN where unresolved.

**Assessment criteria**

1. Every Evidence Requirement in the sample has an assigned source owner.
2. Every request has an evidence request record with request date, due date, response and status.
3. Overdue requests were escalated to the capability owner.
4. Unfulfilled requests at assessment close are recorded as UNKNOWN Records with type U1 or U2.
5. Provider-held evidence has a source owner in the provider organisation and an internal owner who manages the request.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Evidence request response time | working days | 10 | Engagement parameter; illustrative |

**Minimum evidence**

- Evidence request records for the assessment
- Source owner assignments
- Escalation records
- UNKNOWN Records for unfulfilled requests

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | The current or most recent completed assessment |
| independence | Assessor reconciles evidence request records to the UNKNOWN register |
| mandatoryItems | Evidence request records for the assessment; UNKNOWN Records for unfulfilled requests |
| acceptableAlternatives | Ticketing system records used for evidence requests, exported with full history |
| unknownEffect | US2 Moderate: attribution of missing evidence uncertain; confidence ceiling CONF-2 for affected controls |
| reassessmentTriggers | Change of provider; Repeated refusal of requests by a source; Change of evidence lead |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, SAMPLING

**Assessment procedure**

1. Obtain evidence request records and check source owner assignment.
2. Test timeliness and escalation for overdue requests.
3. Reconcile unfulfilled requests to UNKNOWN Records.
4. Check provider-held evidence ownership on both sides.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to every assessment that requests evidence from others.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Evidence request sent to a general mailbox and never answered; Missing evidence silently dropped from scope; Provider refuses access and no UNKNOWN is raised; Nobody knows who holds commissioning records

**Testing safety.** Review of evidence request records only; the assessor does not contact provider source owners directly without the internal owner's agreement.

**UNKNOWN rule.** Every request unfulfilled at assessment close becomes an UNKNOWN Record; it shall never be closed as 'not provided' without an UNKNOWN Record.

**Ontology classes.** EvidenceRequirement, EvidenceObject, UnknownRecord, Action · **Related controls.** MCF-GOV-008, MCF-EVA-014, MCF-EVA-001

**Informative references.** AIDCF-008 Evidence Model; ISO 19011 (guidelines for auditing management systems)

### MCF-EVA-003

**Evidence Repository** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that accepted evidence is held in a repository that assigns immutable identifiers, records the mandatory AIDCF-008 metadata, produces an EvidenceManifest with hashes for each Evidence Package, and supports retrieval of exactly the evidence a decision relied on.

**Requirement.** The evidence lead shall operate an evidence repository in which every Evidence Object has an immutable identifier, the mandatory metadata defined in AIDCF-008 (including source, collector, custodian, observation time, collection time, scope, state, classification, integrity value and lifecycle state), and conditional metadata for test, telemetry, configuration, human, external and derived evidence. The tool owner shall configure the repository to generate an EvidenceManifest with content hashes for each Evidence Package and to freeze the manifest referenced by each Assurance Decision.

**Assessment criteria**

1. Every Evidence Object in a sample has an immutable identifier and complete mandatory metadata.
2. Conditional metadata are present for test, telemetry, configuration, human, external and derived evidence in the sample.
3. Each Evidence Package supporting a decision has an EvidenceManifest with content hashes.
4. The manifest referenced by each decision is frozen and retrievable, and its hashes verify against stored objects.
5. Repository configuration prevents in-place overwrite of accepted Evidence Objects.

**Minimum evidence**

- Repository configuration export
- Sample of Evidence Object metadata records
- EvidenceManifests for decisions in the period
- Hash verification output

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2 |
| optionalClasses | E7 |
| qualityFloor | P4 F3 C4 R4 T3 I4 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Repository configuration at the assessment date and manifests for decisions issued in the last twelve months |
| independence | Hash verification run by the assessor with an independent tool |
| mandatoryItems | Repository configuration export; EvidenceManifests for decisions in the period; Hash verification output |
| acceptableAlternatives | Write-once storage with an external manifest generated per decision |
| unknownEffect | US3 Material: reproducibility of decisions uncertain; affected decisions treated as integrity-uncertain for CG-11 |
| reassessmentTriggers | Repository platform change or migration; Schema change; Failed hash verification |

**Assessment methods.** INSPECTION, SAMPLING, TEST, RECONCILIATION

**Assessment procedure**

1. Export repository configuration and verify identifier immutability and overwrite protection.
2. Sample Evidence Objects and check mandatory and conditional metadata.
3. Retrieve manifests for decisions in the period.
4. Recompute hashes with an independent tool and compare.

**Gate mappings.** None

**Applicability.** Applies to every programme issuing Assurance Decisions.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Evidence overwritten with a newer version under the same ID; Decision cannot be reproduced because its evidence set is unknown; Telemetry evidence without source clock or query; Missing collector identity

**Testing safety.** Hash recomputation uses read-only access to stored objects; no object is modified.

**UNKNOWN rule.** If a decision's manifest cannot be retrieved, record a U1 UNKNOWN against that decision's evidence basis and refer it to MCF-EVA-024 for suspension review.

**Ontology classes.** EvidenceObject, EvidencePackage, ReleaseManifest, AssuranceDecision · **Related controls.** MCF-EVA-004, MCF-EVA-006, MCF-GOV-008

**Informative references.** AIDCF-008 Evidence Model; AIDCF-014 End-to-End Traceability and Machine-Executable Data Standard; ISO 14721 (open archival information system reference model)

### MCF-EVA-004

**Retention and Protection** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure that assurance evidence is retained according to its retention class, protected according to its classification, preserved under legal hold, and recoverable after loss of the repository, so that decisions remain reviewable and challengeable throughout their validity.

**Requirement.** The evidence lead shall assign each Evidence Object a retention class (R0-R5) and a classification level, define retention periods by legal, contractual and decision-validity requirements, apply legal holds when instructed, and record authorised destruction. The tool owner shall back up the repository, including manifests and custody logs, to a separate fault domain and shall test restoration at the restoration test interval, verifying hashes and custody logs after restore.

**Assessment criteria**

1. Every Evidence Object in the sample has a retention class and classification.
2. Retention periods are defined and no Evidence Object supporting a decision still within its validity or challenge period was destroyed.
3. Legal holds in the period were applied to all relevant objects and destruction was blocked.
4. Backups of objects, manifests and custody logs are held in a fault domain separate from the primary repository.
5. A restoration test within the interval restored a representative sample and hashes and custody logs verified after restore.
6. Access controls enforce classification, and restricted evidence access is logged.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Evidence repository restoration test interval | months | 12 | Programme parameter; illustrative |

**Minimum evidence**

- Retention schedule and classification policy
- Sample of object retention and classification attributes
- Legal hold records
- Backup configuration showing separate fault domain
- Restoration test record with hash verification
- Destruction records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E2; E3; E4 |
| optionalClasses | E5 |
| qualityFloor | P4 F4 C3 R4 T3 I4 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; RECOVERY |
| periodCoverage | Retention events over twelve months and the latest restoration test |
| independence | Restoration test observed or verified by the assessor; hash comparison performed independently |
| mandatoryItems | Retention schedule and classification policy; Backup configuration showing separate fault domain; Restoration test record with hash verification |
| acceptableAlternatives | Restoration from an actual repository incident, with verification records, in place of a test |
| unknownEffect | US3 Material: future challenge and reassessment of decisions may be impossible; decision condition recorded |
| reassessmentTriggers | Repository platform change; Legal hold instruction; Failed restoration; Change of retention law or contract |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, TEST, SAMPLING

**Assessment procedure**

1. Review retention schedule and classification policy.
2. Sample objects and verify attributes and that none supporting a valid decision was destroyed.
3. Review legal hold application.
4. Inspect backup configuration for fault-domain separation.
5. Examine or observe a restoration test and recompute hashes on restored objects.

**Gate mappings.** None

**Applicability.** Applies to every programme retaining evidence beyond a single engagement.

**Lifecycle stages.** OPERATE, DECOMMISSION · **Operating states.** NORMAL, RECOVERY

**Failure modes addressed.** Evidence destroyed before challenge period ends; Backups in the same storage system as the primary; Restored evidence fails hash verification unnoticed; Classified evidence accessible to all assessors

**Testing safety.** Restoration tests use an isolated restore target; production repository content is never overwritten by a restore test.

**UNKNOWN rule.** If restoration has never been tested, the RESILIENCE claim is UNKNOWN (U1); backup existence alone supports only IMPLEMENTATION.

**Ontology classes.** EvidenceObject, EvidencePackage, DistributionControl · **Related controls.** MCF-EVA-003, MCF-GOV-008, MCF-EVA-006

**Informative references.** ISO 15489-1 (records management); ISO/IEC 27001 (information security management systems); ISO/IEC 27040 (storage security); ISO/IEC 27050 series (electronic discovery)

## EVA-02 Evidence provenance and quality

### MCF-EVA-005

**Source Provenance** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that every accepted Evidence Object has an established origin, authority and collection lineage, including derived and AI-assisted evidence whose sources, transformation and human review are recorded, so that no conclusion rests on evidence of unknown origin.

**Requirement.** The lead assessor shall ensure that, before an Evidence Object is accepted, its source, collector, collection activity and authority are recorded and verified; that derived evidence records source Evidence IDs, query or script and version, assumptions and reviewer; and that AI-assisted extraction, summarisation or classification is recorded with model and version, process record and the accountable human review, and is treated as candidate evidence that does not corroborate its own sources.

**Assessment criteria**

1. Every accepted Evidence Object in the sample has recorded source, collector, collection activity and authority.
2. Provenance was verified (for example extraction witnessed, issuer confirmed) for evidence supporting gate-CRITICAL controls.
3. Derived evidence records source IDs, transformation method and version, assumptions and reviewer.
4. AI-assisted evidence records model and version, process record and human reviewer, and is not used as independent corroboration of its sources.
5. No Evidence Object with P rating below the profile floor supports a CONFORMING result.

**Minimum evidence**

- Sample of accepted Evidence Object provenance records
- Collection activity records for gate-supporting evidence
- Derived evidence lineage records
- AI-assisted processing records with review

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3; E7 |
| optionalClasses | E2 |
| qualityFloor | P4 F3 C4 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Evidence accepted for assessments completed in the last twelve months |
| independence | Assessor reperforms provenance verification for a sub-sample at source |
| mandatoryItems | Sample of accepted Evidence Object provenance records; Derived evidence lineage records; AI-assisted processing records with review |
| acceptableAlternatives | W3C PROV-compatible provenance graph export in place of per-object records |
| unknownEffect | US3 Material: affected results may become UNKNOWN (U6); CG-11 evaluation records the gap |
| reassessmentTriggers | Introduction of AI-assisted evidence processing; New derived analytics; Provenance failure found |

**Assessment methods.** SAMPLING, REPERFORMANCE, DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Sample accepted Evidence Objects, weighted to those supporting CRITICAL controls.
2. Check provenance fields and verification records.
3. Trace derived evidence to sources and re-run one transformation.
4. Inspect AI-assisted processing records and confirm human review and non-use as corroboration.
5. Reperform provenance verification at source for a sub-sample.

**Gate mappings.** None

**Applicability.** Applies to every programme accepting evidence; AI-assisted criteria apply only where AI-assisted processing is used.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Screenshot of a configuration accepted with no record of who captured it or from where; Derived capacity analysis whose source telemetry cannot be identified; AI summary of commissioning reports treated as corroboration; Provider attestation with unverified issuer

**Testing safety.** Reperformance of extraction at source is read-only and performed by the system owner under observation.

**UNKNOWN rule.** Evidence whose origin cannot be established is recorded as U6 and is excluded from support of any CONFORMING result.

**Ontology classes.** EvidenceObject, EvidenceRequirement, ValidationResult · **Related controls.** MCF-EVA-006, MCF-EVA-007, MCF-EVA-003

**Informative references.** W3C PROV-DM (provenance data model); ISO/IEC 27037 (identification, collection, acquisition and preservation of digital evidence); AIDCF-008 Evidence Model

### MCF-EVA-006

**Integrity and Custody** · DETECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure that alteration of evidence or loss of custody is detected, so that evidence supporting gates and decisions can be shown to be the evidence originally collected.

**Requirement.** The evidence lead shall ensure that every Evidence Object supporting a gate result or Assurance Decision has an integrity value computed at collection, an integrity level (I0-I5) assigned, and a custody log; that integrity values are re-verified before decision issue and on retrieval for challenge or reassessment; and that integrity failures are recorded, investigated and the affected evidence withdrawn from support. The evidence lead shall test detection at least once per integrity test interval by a controlled tamper exercise on test objects.

**Assessment criteria**

1. Every gate-supporting Evidence Object in the sample has an integrity value from collection, an integrity level and a custody log.
2. Integrity values were re-verified before each decision issue in the period.
3. Integrity failures in the period were recorded, investigated and the affected evidence withdrawn from support.
4. A controlled tamper exercise within the interval was detected by the integrity mechanism.
5. Redactions preserved a controlled unredacted source and recorded basis and method.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Integrity detection test interval | months | 12 | Programme parameter; illustrative |

**Minimum evidence**

- Integrity values and custody logs for sampled evidence
- Pre-decision integrity verification records
- Integrity failure records
- Tamper exercise record
- Redaction records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E1; E5 |
| qualityFloor | P4 F4 C3 R4 T3 I4 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Decisions issued in the last twelve months and the latest tamper exercise |
| independence | Tamper exercise designed by a party other than the repository administrators |
| mandatoryItems | Integrity values and custody logs for sampled evidence; Pre-decision integrity verification records; Tamper exercise record |
| acceptableAlternatives | Detection of a real integrity event, with investigation record, in place of a tamper exercise |
| unknownEffect | US3 Material: affected evidence treated as U7; dependent gate results may become UNKNOWN under CG-11 |
| reassessmentTriggers | Integrity failure; Repository change; Custody gap discovered |

**Assessment methods.** TEST, SAMPLING, INSPECTION, REPERFORMANCE

**Assessment procedure**

1. Sample gate-supporting evidence and check integrity values, levels and custody logs.
2. Verify pre-decision re-verification records.
3. Review integrity failure handling.
4. Examine the tamper exercise design and result; reperform verification on a sub-sample.
5. Review redaction records.

**Gate mappings.** None

**Applicability.** Applies to all evidence supporting gate results or Assurance Decisions.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Test report edited after collection to remove an anomaly; Custody gap during provider transfer; Integrity values computed only after editing; Redaction removes content without a controlled original

**Testing safety.** Tamper exercises use dedicated test objects in a non-production area of the repository, with the evidence lead's written approval; real evidence is never altered.

**UNKNOWN rule.** Any Evidence Object whose integrity cannot be re-verified is recorded as U7 and withdrawn from support until re-collected or independently corroborated.

**Ontology classes.** EvidenceObject, EvidencePackage, ValidationResult · **Related controls.** MCF-GOV-008, MCF-EVA-005, MCF-EVA-004

**Informative references.** ISO/IEC 27037 (identification, collection, acquisition and preservation of digital evidence); ISO/IEC 27042 (analysis and interpretation of digital evidence); AIDCF-008 Evidence Model

### MCF-EVA-007

**Relevance and Reliability** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that each Evidence Object is rated for fitness to the precise assertion and for reliability of its method and source, with rationale, so that reliable but irrelevant evidence (for example a design document cited for an operation claim) does not support a result.

**Requirement.** The lead assessor shall ensure that every Evidence Object used to support a Control Assessment is rated on all six AIDCF-008 quality dimensions with rationale, that the fitness (F) rating considers subject, criterion, claim type, configuration and operating state, that the reliability (R) rating considers method repeatability and corroboration, and that a second assessor independently re-rates a sample with differences resolved and recorded.

**Assessment criteria**

1. Every supporting Evidence Object in the sample has P, F, C, R, T and I ratings with rationale.
2. F ratings reflect claim type and operating state; no E1 design evidence alone supports an OPERATION, EFFECTIVENESS or RESILIENCE claim.
3. Independent re-rating of a sample agrees within one point on each dimension, or differences were resolved and recorded.
4. No Evidence Object below the profile quality floor supports a CONFORMING result.
5. Quality vectors are retained and not collapsed to a single averaged number.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Independent re-rating sample | % of supporting Evidence Objects | 10 | Programme parameter; illustrative, minimum of 10 objects |

**Minimum evidence**

- Quality ratings with rationale for sampled evidence
- Independent re-rating records
- Control Assessments with supporting evidence lists

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E7 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C4 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Assessments completed in the last twelve months |
| independence | Re-rating by an assessor who did not perform the original rating |
| mandatoryItems | Quality ratings with rationale for sampled evidence; Independent re-rating records |
| acceptableAlternatives | Assessor re-rates a sample during this assessment if no re-rating records exist, with a Finding raised |
| unknownEffect | US3 Material: result support uncertain; CG-11 evaluation records the gap |
| reassessmentTriggers | New assessor team; Change in quality anchors; Systematic rating disagreement found |

**Assessment methods.** SAMPLING, REPERFORMANCE, ANALYSIS

**Assessment procedure**

1. Sample Control Assessments and their supporting evidence.
2. Check quality ratings and rationale.
3. Test claim-type fitness, especially E1-only support for higher claims.
4. Reperform ratings for a sub-sample and compare.
5. Compare ratings with profile floors for CONFORMING results.

**Gate mappings.** None

**Applicability.** Applies to every Control Assessment that relies on evidence, which is every Control Assessment other than NOT_APPLICABLE dispositions.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Design drawing accepted as proof of operation; Vendor datasheet accepted as proof of installed configuration; Ratings inflated to meet floors; Single averaged quality score hides a weak integrity rating

**Testing safety.** Desk re-rating of evidence records only; source systems are not accessed for this control.

**UNKNOWN rule.** Where reviewers cannot agree on a rating after discussion, record a U9 UNKNOWN on the evidence and apply the lower rating until resolved.

**Ontology classes.** EvidenceObject, ControlAssessment, EvidenceRequirement · **Related controls.** MCF-EVA-005, MCF-EVA-008, MCF-EVA-018

**Informative references.** AIDCF-008 Evidence Model; ISO 19011 (guidelines for auditing management systems) - audit evidence; ISAE 3000 (assurance engagements other than audits or reviews of historical financial information)

### MCF-EVA-008

**Currency and Coverage** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that evidence is current for the state asserted and covers the required population, locations, period, operating states and scenarios, so that a result is not extrapolated beyond what the evidence represents.

**Requirement.** The lead assessor shall ensure that each Evidence Object used to support a result is checked against the AIDCF-008 freshness basis for its category and against any material change since collection, and that each Control Assessment records coverage across entity, population, location, time, operating state, scenario, tenant or workload, and dependency dimensions, with gaps recorded as U3 or U5 UNKNOWN Records.

**Assessment criteria**

1. Every supporting Evidence Object in the sample was checked for currency against its category basis and for intervening material change.
2. Each sampled Control Assessment records coverage across the AIDCF-008 coverage dimensions relevant to its claim type.
3. Evidence predating a material change to its subject is not used without re-validation.
4. Coverage gaps (for example no evidence from DEGRADED or MAINTENANCE states) are recorded as U5 UNKNOWN Records.
5. No result is stated for a population, state or period broader than the evidence covers.

**Minimum evidence**

- Currency checks for sampled evidence
- Coverage records in sampled Control Assessments
- Change log for subjects of sampled evidence
- UNKNOWN Records for currency and coverage gaps

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3; E7 |
| optionalClasses | E2 |
| qualityFloor | P3 F4 C4 R3 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Assessments completed in the last twelve months |
| independence | Assessor compares evidence dates with the change log independently |
| mandatoryItems | Currency checks for sampled evidence; Coverage records in sampled Control Assessments; Change log for subjects of sampled evidence |
| acceptableAlternatives | Machine-generated freshness flags from the assessment tool, if the rules are verified |
| unknownEffect | US3 Material: affected results may be STALE; CG-11 evaluation records the gap |
| reassessmentTriggers | Material change to assessed subjects; Expiry of evidence currency windows; New operating state introduced |

**Assessment methods.** SAMPLING, RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Sample Control Assessments and their evidence.
2. Compare evidence dates with the freshness basis and change log.
3. Check coverage records against the relevant dimensions.
4. Confirm coverage gaps are recorded as UNKNOWN Records.
5. Compare stated result scope with evidence coverage.

**Gate mappings.** None

**Applicability.** Applies to every Control Assessment at OPERATION claim type or above, and to DESIGN and IMPLEMENTATION assessments where evidence predates a material change.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Commissioning test from before a cooling conversion used for current effectiveness; UPS test on one of four modules extrapolated to all; No maintenance-state evidence yet maintenance-state claim made; Telemetry from one hall used for a multi-hall instance

**Testing safety.** Desk analysis only.

**UNKNOWN rule.** Evidence that predates a material change is recorded as U3 for the changed subject; coverage gaps are recorded as U5 with the missing dimension named.

**Ontology classes.** EvidenceObject, ControlAssessment, UnknownRecord, Sample · **Related controls.** MCF-EVA-007, MCF-EVA-011, MCF-EVA-021

**Informative references.** AIDCF-008 Evidence Model; ISO 2859-1 (sampling procedures for inspection by attributes); ISO 19011 (guidelines for auditing management systems)

## EVA-03 Assessment planning and execution

### MCF-EVA-009

**Decision Question** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure that each assessment answers a precisely stated decision question (for example 'Can Capability Instance X sustain training goodput within tolerance through loss of one CDU per pod, as of date D?') that names the Capability Instance, Service Outcomes, tolerances, operating states, intended users and prohibited interpretations.

**Requirement.** The decision authority shall approve, before fieldwork begins, a decision question for each assessment that states the Capability Instance, the Service Outcomes and tolerances in question, the operating states, the as-of date or period, the intended users and use, and the interpretations the conclusion shall not support. The lead assessor shall frame the assurance case top claim from the approved decision question and shall obtain re-approval if the question changes during the assessment.

**Assessment criteria**

1. An approved decision question exists for each assessment, dated before fieldwork.
2. The question names Capability Instance, Service Outcomes, tolerances, operating states, as-of date or period, intended users and use, and prohibited interpretations.
3. The assurance case top claim is derived from the decision question without broadening it.
4. Changes to the question during the assessment were re-approved by the decision authority.
5. The report and Assurance Statement restate the same decision question.

**Minimum evidence**

- Approved decision question record
- Assurance case top claim
- Change records for the question
- Report and Assurance Statement extracts

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C3 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | The assessment under review |
| independence | Approval by the decision authority, separate from the lead assessor |
| mandatoryItems | Approved decision question record; Assurance case top claim |
| acceptableAlternatives | Engagement letter containing all required elements, approved by the decision authority |
| unknownEffect | US5 Systemic: decision question undefined; CG-01 Gate Result UNKNOWN and decision capped at INCONCLUSIVE |
| reassessmentTriggers | Change in intended users or use; Change of Capability Instance or Service Outcome in scope; Change of as-of date |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Obtain the approved decision question and check required elements and approval date.
2. Compare the top claim with the question.
3. Review change records for the question.
4. Compare the question restated in the report and statement.

**Gate mappings.** CG-01 Capability and outcome definition (CRITICAL)

**Applicability.** Applies to every assessment that produces an Assurance Decision.

**Lifecycle stages.** PLAN · **Operating states.** NORMAL

**Failure modes addressed.** Assessment asks 'is the data centre resilient?' with no instance, outcome or state; Conclusion used for a purchase decision it was not designed for; Top claim broader than the approved question; Question changed mid-assessment without approval

**Testing safety.** Desk review of engagement records only; draft decision questions are treated as confidential to the commissioning party.

**UNKNOWN rule.** If no approved decision question exists, record a US5 UNKNOWN Record; no Assurance Decision above INCONCLUSIVE may be issued.

**Ontology classes.** AssuranceProgram, Assessment, CapabilityInstance, ServiceOutcome · **Related controls.** MCF-EVA-010, MCF-GOV-001, MCF-CAP-001, MCF-CAP-010

**Informative references.** ISO/IEC/IEEE 15026-2 (assurance case); ISAE 3000 (assurance engagements other than audits or reviews of historical financial information) - engagement acceptance; AIDCF-009 Assessment Methodology Practitioner Handbook

### MCF-EVA-010

**Scope and Criteria** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure that each assessment has an approved boundary (physical, logical, organisational, provider and temporal), applicable criteria (AIDCF artifact and capability-profile versions, applicable controls, claim types, gates), and visible exclusions with their residual effect.

**Requirement.** The lead assessor shall prepare, and the decision authority shall approve before fieldwork, a scope record for each assessment stating the boundary across physical, logical, organisational, provider and temporal dimensions; the operating states assessed; the applicable AIDCF artifact and capability-profile versions; the applicable controls with claim types; the applicable gates; and every exclusion with rationale and residual effect on the decision. The lead assessor shall reconcile the boundary to the ArchitectureSnapshot (MCF-CAP-004) and record any element of the snapshot that is neither in scope nor excluded.

**Assessment criteria**

1. An approved scope record exists, dated before fieldwork, covering all five boundary dimensions and the operating states.
2. Applicable criteria are identified by version, including the control set with claim types and the gate set.
3. Every exclusion has rationale and residual effect on the decision.
4. Reconciliation to the ArchitectureSnapshot leaves no element neither in scope nor excluded.
5. Shared and external dependencies crossing the boundary are listed with how they are assessed (directly, by provider evidence, or as UNKNOWN).

**Minimum evidence**

- Approved scope record
- Applicable control and gate list with claim types
- Exclusion register with residual effect
- Boundary-to-ArchitectureSnapshot reconciliation

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E7 |
| optionalClasses | E2 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | The assessment under review |
| independence | Reconciliation reperformed by the independent reviewer for a sample of snapshot elements |
| mandatoryItems | Approved scope record; Exclusion register with residual effect; Boundary-to-ArchitectureSnapshot reconciliation |
| acceptableAlternatives | Machine-readable scope object in the assessment tool, exported with approval history |
| unknownEffect | US5 Systemic: assessment boundary unresolved; CG-02 Gate Result UNKNOWN and decision capped at INCONCLUSIVE |
| reassessmentTriggers | Change of boundary during assessment; New ArchitectureSnapshot version; Exclusion added or removed |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, ANALYSIS

**Assessment procedure**

1. Obtain the approved scope record and check dimensions, states and approval date.
2. Check criteria versions, control set and gate set.
3. Review exclusions for rationale and residual effect.
4. Reperform boundary reconciliation for a sample of snapshot elements.
5. Check treatment of cross-boundary dependencies.

**Gate mappings.** CG-02 Boundary and architecture integrity (CRITICAL)

**Applicability.** Applies to every assessment, including delta assessments after material change, which require their own scope record.

**Lifecycle stages.** PLAN · **Operating states.** NORMAL

**Failure modes addressed.** Utility supply excluded with no residual effect stated; Provider-operated cooling plant neither in scope nor excluded; Criteria version not stated, so results are unreproducible; Maintenance state silently omitted from scope

**Testing safety.** Desk review and graph reconciliation using read-only queries; no site access is required.

**UNKNOWN rule.** Any ArchitectureSnapshot element that is neither in scope nor excluded is recorded as a US5 UNKNOWN Record against the boundary.

**Ontology classes.** Assessment, ArchitectureSnapshot, Dependency, CriticalGate · **Related controls.** MCF-EVA-009, MCF-CAP-004, MCF-EVA-017, MCF-EVA-016

**Informative references.** ISO/IEC/IEEE 15026-2 (assurance case) - context and assumptions; ISO 19011 (guidelines for auditing management systems) - audit scope and criteria; AIDCF-011 Assurance Program Framework

### MCF-EVA-011

**Sampling and Testing** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that sampling is risk-based, reproducible and not over-extrapolated, and that tests are authorised, safe, defined in advance (initial state, method, expected result, abort criteria, restoration) and recorded with anomalies.

**Requirement.** The lead assessor shall document, for each sample, the population and its frame, strata, selection method, sample size rationale, exclusions and expansion rule, and shall record failed samples and their effect. For each test, the lead assessor shall obtain written authorisation from the system owner and, for hazardous or service-affecting tests, the safety authority, and shall record the initial state, method, expected result, abort criteria, instrumentation, restoration steps, result and anomalies. Tests shall be performed by authorised operators; assessors shall observe.

**Assessment criteria**

1. Each sample in the assessment has documented population frame, strata, method, size rationale, exclusions and expansion rule.
2. Judgemental samples are not represented as statistical coverage, and sampled results are not extrapolated beyond the represented population and conditions.
3. Failed samples triggered expansion or were reflected in the result.
4. Every test has prior written authorisation from the system owner and, where hazardous or service-affecting, the safety authority.
5. Every test record contains initial state, method, expected result, abort criteria, instrumentation, restoration, result and anomalies.
6. Tests were performed by authorised operators, with assessors observing.

**Minimum evidence**

- Sampling plans and records
- Test authorisations
- Test records with required conditional metadata
- Expansion records for failed samples

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E3; E4 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C4 R4 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL; MAINTENANCE; DEGRADED |
| periodCoverage | The assessment under review |
| independence | Independent reviewer reperforms selection from the population frame for one sample |
| mandatoryItems | Sampling plans and records; Test authorisations; Test records with required conditional metadata |
| acceptableAlternatives | Use of the operator's own test records as evidence, if they contain the required metadata and authorisation |
| unknownEffect | US3 Material: affected results may be over-extrapolated or unsafe to rely on; CG-11 evaluation records the gap |
| reassessmentTriggers | Test incident or abort; Change of sampling approach; Failed sample not expanded |

**Assessment methods.** DOCUMENT_REVIEW, REPERFORMANCE, SAMPLING

**Assessment procedure**

1. Review sampling plans for required elements.
2. Reperform selection for one sample from the population frame.
3. Check expansion after failed samples and absence of over-extrapolation.
4. Check test authorisations and safety authority sign-off for hazardous tests.
5. Check test records for required metadata and operator/observer roles.

**Gate mappings.** CG-04 Life safety and hazardous energy (SUPPORTING)

**Applicability.** Applies to every assessment that samples or tests.

**Lifecycle stages.** PLAN, OPERATE, COMMISSION · **Operating states.** NORMAL, MAINTENANCE, DEGRADED

**Failure modes addressed.** Assessor operates switchgear during a test; Test performed without abort criteria and fails to restore; Three good samples extrapolated to an entire fleet; Failed sample discarded

**Testing safety.** This control governs safety of all assessment testing: hazardous-energy, pressurised-fluid, refrigerant, battery and service-affecting tests require written authorisation from the system owner and the safety authority, a method statement, initial-state verification, abort criteria, permits under the site safe system of work and restoration steps. The safety authority may stop any test at any time; a stopped test is recorded with its partial result and does not count as passed.

**UNKNOWN rule.** If a test lacks authorisation records, its result is excluded from support and recorded as U8 (method uncertain); it is not re-run without authorisation.

**Ontology classes.** Sample, TestRecord, AssessmentProcedure · **Related controls.** MCF-EVA-008, MCF-EVA-012, MCF-CAP-019, MCF-CAP-022

**Informative references.** ISO 2859-1 (sampling procedures for inspection by attributes); ISO 19011 (guidelines for auditing management systems) - audit sampling; AIDCF-009 Assessment Methodology Practitioner Handbook

### MCF-EVA-012

**Specialist Involvement** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that domain specialists (electrical, mechanical, compute, storage and network, OT security, resilience, evidence and data) approve the technical methods and conclusions in their domains, and that reliance on specialists is recorded with scope, competence and responsibility.

**Requirement.** The lead assessor shall identify, for each assessment, the domains requiring specialist judgement, appoint a competent specialist for each (MCF-GOV-023), and record the specialist's scope, competence evidence and responsibility. Each specialist shall approve the methods and the Control Assessment results in their domain. Where a specialist is external, the lead assessor shall evaluate their independence and the transferability of their conclusions.

**Assessment criteria**

1. Domains requiring specialist judgement are identified for the assessment.
2. Each identified domain has an appointed specialist with recorded scope, competence evidence and responsibility.
3. Methods and Control Assessment results in each specialist domain carry the specialist's approval.
4. External specialists' independence and transferability of conclusions were evaluated.
5. No technical conclusion in a specialist domain was issued without specialist approval.

**Minimum evidence**

- Specialist domain identification
- Specialist appointment and reliance records
- Specialist approvals on methods and results
- External specialist evaluation records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F3 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | The assessment under review |
| independence | Independent reviewer confirms coverage of specialist domains |
| mandatoryItems | Specialist appointment and reliance records; Specialist approvals on methods and results |
| acceptableAlternatives | Specialist report with explicit scope and sign-off, incorporated by reference |
| unknownEffect | US3 Material: affected domain results carry CONF-2 ceiling and a decision condition |
| reassessmentTriggers | New domain in scope; Specialist change mid-assessment; Technical disagreement unresolved |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION, INQUIRY

**Assessment procedure**

1. Review domain identification against scope.
2. Check appointments and reliance records.
3. Reconcile results in each domain to specialist approvals.
4. Review external specialist evaluations.
5. Interview one specialist on scope and approval.

**Gate mappings.** None

**Applicability.** Applies to every assessment that includes technical infrastructure domains.

**Lifecycle stages.** PLAN, OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Generalist assessor concludes on protection coordination; OEM engineer acts as independent specialist for their own product; Specialist reviews methods but not results; Liquid-cooling domain not identified as needing a specialist

**Testing safety.** Record review and interview only.

**UNKNOWN rule.** If specialist approval is missing for a domain result, that result is UNKNOWN (U9 interpretation unresolved) until approved.

**Ontology classes.** Assessment, ReviewRecord, ControlAssessment · **Related controls.** MCF-GOV-023, MCF-EVA-011, MCF-EVA-015

**Informative references.** ISO 19011 (guidelines for auditing management systems) - technical experts; ISAE 3000 (assurance engagements other than audits or reviews of historical financial information) - use of experts; AIDCF-011 Assurance Program Framework

## EVA-04 Findings, UNKNOWN and limitations

### MCF-EVA-013

**Finding Traceability** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that every Finding is traceable to the criterion, the evidenced condition, the supporting and challenging evidence, the affected Service Outcomes, controls and gates, and to its action and closure evidence.

**Requirement.** The lead assessor shall record every Finding with a stable identifier, criterion (control and assessment criterion), condition, supporting and challenging Evidence Object references, cause where evidenced or labelled as analysis, consequence for Service Outcomes, dependencies and states, classification, and gate and score effect. The action owner shall record closure evidence, and the lead assessor shall close a Finding only after re-assessing that evidence.

**Assessment criteria**

1. Every Finding in the sample has identifier, criterion, condition, evidence references, consequence, classification and gate/score effect.
2. Cause is either evidenced or explicitly labelled as analysis.
3. Each Finding is linked in the graph to its control, Service Outcomes and gates.
4. Closed Findings have closure evidence re-assessed by an assessor, not closed on management assertion.
5. Findings are not deleted; superseded Findings retain history.

**Minimum evidence**

- Findings register extract
- Sampled Finding records with evidence links
- Graph links from Findings to controls, outcomes and gates
- Closure evidence and re-assessment records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3; E7 |
| optionalClasses |  |
| qualityFloor | P3 F4 C4 R3 T3 I4 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Findings raised or closed in the last twelve months |
| independence | Assessor selects Findings from the full register including closed and superseded items |
| mandatoryItems | Findings register extract; Sampled Finding records with evidence links; Closure evidence and re-assessment records |
| acceptableAlternatives | Findings exported from the assessment tool in AIDCF-014 format with history |
| unknownEffect | US3 Material: residual deficiency status uncertain; decision condition recorded |
| reassessmentTriggers | Register migration; Finding closed without evidence; Finding deleted |

**Assessment methods.** SAMPLING, RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Extract the full Findings register including closed and superseded items.
2. Sample Findings and check required fields and evidence references.
3. Check graph links to controls, outcomes and gates.
4. Verify closure evidence and re-assessment for closed Findings.
5. Compare register history for deletions.

**Gate mappings.** None

**Applicability.** Applies to every assessment that raises Findings.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Finding closed on an email saying 'fixed'; Finding with no link to the gate it affects; Cause speculated without evidence; Embarrassing Finding deleted

**Testing safety.** Review of Findings records only; closure evidence involving site changes is verified under the relevant domain control.

**UNKNOWN rule.** If a Finding's evidence references cannot be resolved to Evidence Objects, record a U1 UNKNOWN on the Finding and keep it open.

**Ontology classes.** Finding, EvidenceObject, Action, ControlAssessment · **Related controls.** MCF-EVA-014, MCF-EVA-016, MCF-GOV-024

**Informative references.** AIDCF-012 Reporting and Assurance Statement Standard; ISO 19011 (guidelines for auditing management systems) - audit findings

### MCF-EVA-014

**UNKNOWN Preservation** · DETECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure that missing, inaccessible, stale, conflicting or unverifiable knowledge is recorded as an UNKNOWN Record with type, severity and decision effect, carried unchanged into gates, scores, decisions and reports, and never silently resolved favourably.

**Requirement.** The lead assessor shall record every UNKNOWN as an UNKNOWN Record with subject, missing attribute, type (U1-U10), severity (US1-US5) with the test that determined it, reason, potential consequence, evidence needed, owner, status and gate and decision effect. The decision authority shall ensure that every US3, US4 and US5 UNKNOWN Record is reflected in the Gate Results, decision ceiling and report, and that UNKNOWN Records are closed only by new evidence or approved re-scoping, never by assumption.

**Assessment criteria**

1. Every UNKNOWN Record in the sample has all required fields including type and severity with the test applied.
2. Severity was assigned top-down by the US5-to-US1 tests; reperformance yields the same severity.
3. Every US4 UNKNOWN Record is reflected as a gate UNKNOWN and every US5 caps the decision at INCONCLUSIVE.
4. Every US3 and above UNKNOWN Record appears in the report with decision effect.
5. A seeded or traced set of UNKNOWNs survived unchanged from workpaper to report.
6. Closed UNKNOWN Records cite new evidence or approved re-scoping.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| UNKNOWN traceability test set size | UNKNOWN Records | 10 | Programme parameter; illustrative |

**Minimum evidence**

- UNKNOWN register extract
- Sampled UNKNOWN Records
- Gate Results and decision record
- Report extracts
- Traceability or seeded-UNKNOWN test record
- Closure records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E3; E4; E7 |
| optionalClasses | E1 |
| qualityFloor | P4 F4 C4 R4 T3 I4 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Assessments completed in the last twelve months |
| independence | Traceability test designed and scored by the independent reviewer |
| mandatoryItems | UNKNOWN register extract; Gate Results and decision record; Traceability or seeded-UNKNOWN test record |
| acceptableAlternatives | Reperformance by the assessor tracing every US3+ UNKNOWN Record of one completed assessment from workpaper to report |
| unknownEffect | US4 Critical: the reliability of every Gate Result is in doubt; CG-12 evaluation cannot conclude and decisions are capped at LIMITED |
| reassessmentTriggers | UNKNOWN missing from a report; Severity scheme change; Assessment tool change affecting UNKNOWN handling |

**Assessment methods.** REPERFORMANCE, TEST, SAMPLING, RECONCILIATION

**Assessment procedure**

1. Extract the UNKNOWN register and sample records.
2. Check required fields and reperform severity assignment.
3. Reconcile US4 and US5 records to Gate Results and decision ceiling.
4. Trace US3+ records into the report.
5. Examine or perform the traceability test from workpaper to report.
6. Review closure basis for closed records.

**Gate mappings.** None

**Applicability.** Applies to every assessment; an assessment with no UNKNOWN Records shall record that the UNKNOWN search was performed.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** UNKNOWN downgraded to an 'improvement opportunity' in the executive report; Missing evidence treated as conforming; US4 UNKNOWN not reflected in its gate; UNKNOWN closed because the deadline passed

**Testing safety.** Seeded-UNKNOWN tests use copies of completed assessments labelled as test material; they are never introduced into live workpapers.

**UNKNOWN rule.** If the register cannot be shown to be complete (for example UNKNOWNs held in personal notes), record a US4 UNKNOWN Record against UNKNOWN completeness for the assessment.

**Ontology classes.** UnknownRecord, GateResult, AssuranceDecision, AssuranceReport · **Related controls.** MCF-EVA-015, MCF-EVA-016, MCF-EVA-018, MCF-GOV-003

**Informative references.** AIDCF-008 Evidence Model; ISO/IEC/IEEE 15026-2 (assurance case) - defeaters; AIDCF-012 Reporting and Assurance Statement Standard

### MCF-EVA-015

**Conflict Handling** · CORRECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that when material evidence supports incompatible propositions (for example design shows 2N power, EPMS shows a shared upstream breaker), both lineages are preserved, the conflict is analysed and resolved, bounded or escalated, and the result reflects it.

**Requirement.** The lead assessor shall register each material evidence conflict as an EvidenceConflict with both assertions and their evidence lineages, analyse scope, time and state differences, seek corroboration, obtain competent review and record whether the conflict is resolved, bounded or escalated. Unresolved conflicts shall be recorded as U4 UNKNOWN Records; observed or tested evidence shall take precedence over design intent unless shown to be unrepresentative.

**Assessment criteria**

1. Every material conflict identified in the sample is registered with both assertions and lineages.
2. Each conflict record shows analysis of scope, time and state differences and corroboration sought.
3. Resolution, bounding or escalation is recorded with competent reviewer.
4. Unresolved conflicts are U4 UNKNOWN Records with severity assigned.
5. Where design intent conflicts with observed or tested evidence, the observed or tested evidence prevailed or the reason it was unrepresentative is recorded.
6. Neither lineage was deleted.

**Minimum evidence**

- Evidence conflict register
- Conflict analysis and review records
- UNKNOWN Records for unresolved conflicts

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E7 |
| optionalClasses | E2; E3 |
| qualityFloor | P3 F4 C4 R4 T3 I4 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Assessments completed in the last twelve months |
| independence | Assessor searches workpapers for contradictory evidence not registered as conflicts |
| mandatoryItems | Evidence conflict register; Conflict analysis and review records |
| acceptableAlternatives | Graph CHALLENGES relationships with linked EvidenceConflict nodes exported from the assessment tool |
| unknownEffect | US3 Material: results may rest on contested evidence; CG-11 evaluation records the gap |
| reassessmentTriggers | Conflict escalated; New contradictory evidence after decision; Conflict register not maintained |

**Assessment methods.** DOCUMENT_REVIEW, ANALYSIS, SAMPLING

**Assessment procedure**

1. Obtain the conflict register.
2. Search workpapers for unregistered contradictions.
3. Review analysis, corroboration and review for each sampled conflict.
4. Confirm unresolved conflicts are U4 UNKNOWN Records.
5. Check precedence of observed evidence over design intent.

**Gate mappings.** None

**Applicability.** Applies to every assessment in which two or more evidence sources address the same assertion.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Inconvenient telemetry ignored in favour of design documents; Conflicting provider attestation discarded; Conflict resolved by majority of documents rather than by evidence quality; Conflict unresolved but result CONFORMING

**Testing safety.** Desk analysis only; corroborating extraction, if needed, is read-only.

**UNKNOWN rule.** Unresolved material conflicts are U4 UNKNOWN Records and the affected result is UNKNOWN until resolved or bounded.

**Ontology classes.** EvidenceObject, UnknownRecord, ControlAssessment · **Related controls.** MCF-EVA-014, MCF-EVA-007, MCF-EVA-012

**Informative references.** AIDCF-008 Evidence Model; ISO/IEC/IEEE 15026-2 (assurance case)

### MCF-EVA-016

**Limitation Disclosure** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that every limitation on the conclusion (exclusions, restricted or inaccessible evidence, untested states, assumptions, sampling limits, provider reliance) is disclosed in every report and statement at a prominence matching its effect.

**Requirement.** The lead assessor shall compile a limitations register for each assessment covering exclusions, restricted or inaccessible evidence, unassessed operating states, assumptions, sampling and test limits and reliance on providers or specialists, each with its effect on the decision. The reporting owner shall ensure every report and Assurance Statement for the assessment discloses each limitation with an effect on the decision, and that redaction for security does not remove a limitation.

**Assessment criteria**

1. A limitations register exists covering the six limitation categories, each with decision effect.
2. Every limitation with a decision effect appears in each report and statement for the assessment.
3. Limitations affecting gates appear in the executive report alongside the Gate Results.
4. Redacted reports still state each limitation, even where its technical detail is withheld.
5. No report broadens scope beyond what the limitations allow.

**Minimum evidence**

- Limitations register
- All reports and statements for the assessment
- Redaction records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E7 |
| optionalClasses |  |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Assessments completed in the last twelve months |
| independence | Reconciliation by the independent reviewer |
| mandatoryItems | Limitations register; All reports and statements for the assessment |
| acceptableAlternatives | Limitations section in the technical report, if it is the single source for other reports |
| unknownEffect | US3 Material: intended users may over-rely; decision condition recorded |
| reassessmentTriggers | New audience-specific report; Redaction of a report; Change of scope after issue |

**Assessment methods.** RECONCILIATION, DOCUMENT_REVIEW

**Assessment procedure**

1. Obtain the limitations register.
2. Reconcile each limitation to every report and statement.
3. Check executive-report prominence for gate-affecting limitations.
4. Compare redacted and unredacted versions for limitation removal.
5. Check report scope against limitations.

**Gate mappings.** None

**Applicability.** Applies to every assessment that issues a report or statement.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Public summary omits that utility dependency was excluded; Redaction removes the statement that cooling failover was untested; Provider reliance not disclosed; Executive summary implies all states were assessed

**Testing safety.** Desk review; restricted report versions viewed under distribution controls.

**UNKNOWN rule.** If a report version cannot be obtained for reconciliation, record a U2 UNKNOWN for that report and treat its disclosure as unverified.

**Ontology classes.** AssuranceReport, AssuranceStatement, DistributionControl · **Related controls.** MCF-EVA-020, MCF-GOV-020, MCF-EVA-010, MCF-EVA-014

**Informative references.** AIDCF-012 Reporting and Assurance Statement Standard; ISAE 3000 (assurance engagements other than audits or reviews of historical financial information) - inherent limitations

## EVA-05 Critical gates and decisions

### MCF-EVA-017

**Gate Applicability** · DIRECTIVE · claim type DESIGN · required AL2

**Objective.** Ensure that, for each assessment, every critical gate CG-01 to CG-15 is determined as applicable or APPROVED_NA with boundary rationale, and that the CRITICAL and SUPPORTING control set for each applicable gate is identified from the registry for the scope.

**Requirement.** The lead assessor shall determine, for each assessment, the applicability of each gate CG-01 to CG-15 to the decision question and boundary, shall identify for each applicable gate the in-scope CRITICAL and SUPPORTING controls from the AIDCF-007A registry gate mappings and the gate criteria from AIDCF-010, and shall submit any proposed APPROVED_NA with boundary rationale to the decision authority. Meta-gates CG-11 and CG-12 shall always be applicable.

**Assessment criteria**

1. Each of the fifteen gates has an applicability determination for the assessment.
2. Every APPROVED_NA has boundary rationale and decision-authority approval.
3. CG-11 and CG-12 are applicable in every assessment.
4. For each applicable gate, the in-scope CRITICAL and SUPPORTING controls match the registry gate mappings filtered by scope.
5. Gate criteria and evidence floors applied are those of the declared AIDCF-010 version.

**Minimum evidence**

- Gate applicability record
- APPROVED_NA approvals
- Gate-to-control lists per applicable gate
- Registry gate mapping extract for the declared version

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-1 |
| requiredClasses | E1; E7 |
| optionalClasses |  |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | The assessment under review |
| independence | Reconciliation to registry mappings reperformed by the assessor using the published registry |
| mandatoryItems | Gate applicability record; Gate-to-control lists per applicable gate; Registry gate mapping extract for the declared version |
| acceptableAlternatives | Machine-generated gate-control lists from the assessment tool, if the tool configuration is verified under MCF-GOV-004 |
| unknownEffect | US4 Critical: affected Gate Results cannot be relied upon; decision capped at LIMITED |
| reassessmentTriggers | Registry gate mapping revision; Scope change; APPROVED_NA proposed |

**Assessment methods.** DOCUMENT_REVIEW, RECONCILIATION

**Assessment procedure**

1. Obtain the applicability record and check all fifteen gates.
2. Review APPROVED_NA rationale and approvals.
3. Reconcile gate-control lists to registry mappings filtered by scope.
4. Confirm gate criteria and floors match the declared AIDCF-010 version.

**Gate mappings.** None

**Applicability.** Applies to every assessment that issues Gate Results, including delta and incident-triggered assessments.

**Lifecycle stages.** PLAN · **Operating states.** NORMAL

**Failure modes addressed.** CG-04 marked not applicable for a site with battery rooms; CRITICAL control omitted from a gate's control list; Superseded gate criteria applied; APPROVED_NA granted by the lead assessor

**Testing safety.** Desk review against the published registry release; no system access is required.

**UNKNOWN rule.** If the registry version used for gate mappings cannot be identified, record a U8 UNKNOWN against every Gate Result of the assessment.

**Ontology classes.** CriticalGate, Control, Assessment · **Related controls.** MCF-EVA-018, MCF-GOV-015, MCF-EVA-010

**Informative references.** AIDCF-010 Scoring and Decision Framework; AIDCF-007A Canonical Master Control Registry

### MCF-EVA-018

**Gate Evidence** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that evidence for each applicable gate meets the gate's mandatory evidence classes and sufficiency floor from AIDCF-008, without substitution below the floor to complete a scorecard, and that Gate Results are computed by the AIDCF-010 roll-up rule.

**Requirement.** The lead assessor shall assemble, for each applicable gate, a gate Evidence Package containing the mandatory evidence classes for that gate, shall assess its sufficiency against the gate floor, and shall compute the Gate Result by the AIDCF-010 roll-up rule from CRITICAL control results, gate criteria and evidence sufficiency. The independent reviewer shall confirm, for each gate, that no evidence below the mandatory type or quality floor was substituted.

**Assessment criteria**

1. Each applicable gate has an Evidence Package containing its mandatory evidence classes.
2. Sufficiency of each gate package is assessed and recorded against the gate floor.
3. No gate PASS is supported by a package below its floor; such gates are UNKNOWN.
4. Each Gate Result reproduces when the roll-up rule is reapplied.
5. The independent reviewer confirmed absence of below-floor substitution for each gate.

**Minimum evidence**

- Gate Evidence Packages
- Gate sufficiency assessments
- Gate Result computation records
- Independent reviewer gate confirmation

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E7 |
| optionalClasses | E5 |
| qualityFloor | P4 F4 C4 R4 T3 I4 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Assessments completed in the last twelve months |
| independence | Reperformance by a party other than the lead assessor |
| mandatoryItems | Gate Evidence Packages; Gate sufficiency assessments; Gate Result computation records |
| acceptableAlternatives | Machine-readable gate packages and results in AIDCF-014 format |
| unknownEffect | US4 Critical: Gate Results unverified; decision capped at LIMITED |
| reassessmentTriggers | Gate floor revision; Gate PASS later contradicted; Evidence withdrawn from a gate package |

**Assessment methods.** REPERFORMANCE, DOCUMENT_REVIEW, ANALYSIS

**Assessment procedure**

1. Obtain gate packages and check mandatory classes per gate.
2. Review sufficiency assessments against floors.
3. Reapply the roll-up rule to recorded results.
4. Check independent reviewer confirmations.

**Gate mappings.** None

**Applicability.** Applies to every assessment that issues Gate Results.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** CG-05 passed on design documents and an old UPS test; Interview substituted for missing E4 recovery test under CG-10; Gate PASS with a CRITICAL control PARTIAL; Gate result computed by averaging

**Testing safety.** Desk reperformance of gate roll-up from recorded results; no evidence is re-collected under this control.

**UNKNOWN rule.** Any gate whose package is below floor is UNKNOWN; this shall be recorded as a US4 UNKNOWN Record against the gate.

**Ontology classes.** CriticalGate, GateResult, EvidencePackage · **Related controls.** MCF-EVA-017, MCF-EVA-019, MCF-GOV-015, MCF-EVA-007

**Informative references.** AIDCF-008 Evidence Model; AIDCF-010 Scoring and Decision Framework

### MCF-EVA-019

**Independent Decision** · PREVENTIVE · claim type IMPLEMENTATION · required AL3

**Objective.** Ensure that the Assurance Decision is issued by the accountable decision authority, separate from those who prepared and performed the assessment, on the basis of a recorded Decision Recommendation and review, and that automation only proposes.

**Requirement.** The decision authority shall issue each Assurance Decision personally or through documented delegation, on the basis of a Decision Recommendation from the lead assessor and the independent review record, and shall record the decision state, controlling reasons (including Gate Results and UNKNOWN ceilings), conditions with owners and dates, and validity. The tool owner shall ensure that no tool can transition a decision to APPROVED without the decision authority's authenticated action.

**Assessment criteria**

1. Every Assurance Decision in the period was issued by the decision authority or a documented delegate.
2. The decision authority was not the preparer or performer of the assessment.
3. Each decision references a Decision Recommendation and independent review record.
4. Each decision records state, controlling reasons, conditions with owners and dates, and validity.
5. Tool configuration requires an authenticated decision-authority action for APPROVED status; no automated approval occurred.

**Minimum evidence**

- Decision records
- Delegation instruments
- Decision Recommendations and review records
- Decision workflow configuration and audit log

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-2 |
| requiredClasses | E1; E2; E3 |
| optionalClasses | E6 |
| qualityFloor | P3 F4 C4 R3 T3 I4 |
| sufficiencyFloor | S3 |
| stateCoverage | NORMAL |
| periodCoverage | Decisions issued in the last twelve months |
| independence | Workflow configuration and audit log extracted by the assessor |
| mandatoryItems | Decision records; Decision workflow configuration and audit log |
| acceptableAlternatives | Signed paper decision records with a decision register, where no workflow tool is used |
| unknownEffect | US3 Material: decisions' authority uncertain; intended reliance restricted and condition recorded |
| reassessmentTriggers | Change of decision authority; Workflow tool change; Automated status change detected |

**Assessment methods.** DOCUMENT_REVIEW, INSPECTION, RECONCILIATION

**Assessment procedure**

1. List decisions in the period and verify issuer authority.
2. Compare issuer with preparer and performer records.
3. Check references to recommendation and review.
4. Check required decision content.
5. Inspect workflow configuration and audit log for automated approvals.

**Gate mappings.** CG-13 Responsibility and authority (SUPPORTING)

**Applicability.** Applies to every Assurance Decision.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Lead assessor issues the decision; Tool auto-approves when score exceeds a threshold; Decision issued without review; Conditions without owners or dates

**Testing safety.** Read-only inspection of workflow configuration and logs.

**UNKNOWN rule.** If the workflow audit log cannot show who approved a decision, record a U7 UNKNOWN against that decision's authority.

**Ontology classes.** AssuranceDecision, DecisionRecommendation, ReviewRecord · **Related controls.** MCF-GOV-002, MCF-GOV-016, MCF-GOV-022, MCF-EVA-018

**Informative references.** ISO/IEC 17020 (requirements for bodies performing inspection) - impartiality; AIDCF-010 Scoring and Decision Framework; AIDCF-006 Assurance Principles Standard

### MCF-EVA-020

**Claim Language** · PREVENTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that reports and statements use only the controlled decision, gate and result vocabulary, bound every conclusion by Capability Instance, Service Outcomes, scope, states and date, and contain no prohibited claims.

**Requirement.** The reporting owner shall ensure that every report and Assurance Statement uses the controlled decision states (REASONABLY_ASSURED, CONDITIONALLY_ASSURED, LIMITED, NOT_ASSURED, INCONCLUSIVE), Gate Results (PASS, FAIL, UNKNOWN, APPROVED_NA, NOT_ASSESSED) and control results of AIDCF-010 with the controlled wording of AIDCF-012; bounds each conclusion by Capability Instance, Service Outcomes, boundary, operating states and as-of date; and contains no prohibited claim (certified, accredited, universally safe, secure or resilient, compliant with all laws). The independent reviewer shall check claim language before issue.

**Assessment criteria**

1. Every report and statement in the sample uses only the controlled decision, gate and result vocabulary.
2. Each conclusion is bounded by Capability Instance, Service Outcomes, boundary, operating states and as-of date.
3. No prohibited claim appears.
4. No visual device (colour, badge, score) presents a stronger conclusion than the decision state.
5. Independent review of claim language is recorded before issue.

**Minimum evidence**

- Sampled reports and statements
- Independent review records for claim language

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E1; E3 |
| optionalClasses | E7 |
| qualityFloor | P3 F4 C4 R3 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Reports and statements issued in the last twelve months |
| independence | Assessor screens all issued documents, not a management-selected subset |
| mandatoryItems | Sampled reports and statements; Independent review records for claim language |
| acceptableAlternatives | Automated vocabulary screening output, verified by manual review of a sample |
| unknownEffect | US3 Material: external reliance may exceed decision; condition recorded |
| reassessmentTriggers | Change of AIDCF-012 controlled wording; Prohibited claim found; New report format |

**Assessment methods.** DOCUMENT_REVIEW, SAMPLING, ANALYSIS

**Assessment procedure**

1. Collect all issued reports and statements in the period.
2. Screen vocabulary and bounding elements.
3. Screen for prohibited claims and misleading visual devices.
4. Check independent review records.

**Gate mappings.** None

**Applicability.** Applies to every report or statement conveying an AIDCF conclusion.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Statement says 'fully resilient AI data centre'; Legacy term 'Adverse' or 'Conditional' used; Green badge shown for a LIMITED decision; Conclusion stated without as-of date

**Testing safety.** Desk review of issued documents only.

**UNKNOWN rule.** If an issued document cannot be retrieved, record a U2 UNKNOWN for that document's claim language.

**Ontology classes.** AssuranceReport, AssuranceStatement, AssuranceDecision · **Related controls.** MCF-GOV-020, MCF-EVA-016, MCF-EVA-019

**Informative references.** AIDCF-012 Reporting and Assurance Statement Standard; ISO/IEC 17000 (conformity assessment vocabulary and general principles)

## EVA-06 Reassessment and continuing assurance

### MCF-EVA-021

**Evidence Expiry** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that each Evidence Object relied on by a current decision has a currency basis and review date, that expiry is detected, and that expired mandatory evidence triggers review of the claims it supports.

**Requirement.** The evidence lead shall record, for each Evidence Object supporting a current Assurance Decision, its currency basis and review date per AIDCF-008, shall monitor for expiry, and on expiry of mandatory evidence shall notify the lead assessor and capability owner, mark the evidence STALE and initiate review of the dependent claims and Gate Results within the expiry response time.

**Assessment criteria**

1. Every Evidence Object supporting a current decision has a currency basis and review date.
2. Expiry monitoring operated throughout the period (for example scheduled reports or alerts).
3. Every expiry of mandatory evidence in the period was notified and the evidence marked STALE.
4. Dependent claims and Gate Results were reviewed within the expiry response time.
5. No current decision relies on expired mandatory evidence without a recorded review outcome.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Expiry response time | working days | 20 | Programme parameter; illustrative |

**Minimum evidence**

- Evidence currency records for current decisions
- Expiry monitoring outputs
- Expiry notifications and STALE markings
- Dependent claim review records

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL |
| periodCoverage | Twelve months preceding the assessment |
| independence | Assessor runs an independent expiry query against currency records |
| mandatoryItems | Evidence currency records for current decisions; Expiry monitoring outputs; Dependent claim review records |
| acceptableAlternatives | Manual quarterly expiry review records, if complete for the period |
| unknownEffect | US3 Material: current decisions may rely on stale evidence; condition recorded |
| reassessmentTriggers | Monitoring failure; Change in currency bases; Expired evidence found in use |

**Assessment methods.** ANALYSIS, RECONCILIATION, SAMPLING

**Assessment procedure**

1. Obtain currency records for evidence supporting current decisions.
2. Run an independent expiry query and compare with monitoring outputs.
3. Trace expiries to notifications, STALE markings and reviews.
4. Check current decisions for reliance on expired mandatory evidence.

**Gate mappings.** None

**Applicability.** Applies to every programme with decisions that remain valid over time.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL

**Failure modes addressed.** Annual UPS test expired but CG-05 PASS still reported; Provider certificate lapsed unnoticed; Evidence with no review date; Expiry alerts sent to a departed staff member

**Testing safety.** Read-only queries against currency records.

**UNKNOWN rule.** Evidence with no currency basis is treated as STALE (U3) for any OPERATION, EFFECTIVENESS or RESILIENCE claim.

**Ontology classes.** EvidenceObject, ReassessmentTrigger, AssuranceDecision · **Related controls.** MCF-EVA-008, MCF-EVA-022, MCF-EVA-024

**Informative references.** AIDCF-008 Evidence Model; ISO 15489-1 (records management)

### MCF-EVA-022

**Change Triggers** · DETECTIVE · claim type EFFECTIVENESS · required AL5

**Objective.** Ensure that material change, incidents, gate changes and evidence invalidation automatically or reliably trigger reassessment of the affected claims, gates and decisions, and that the trigger mechanism is shown to work.

**Requirement.** The assurance programme lead shall define reassessment triggers for each current Assurance Decision (material architecture, capacity, configuration, provider or ownership change; incidents affecting Service Outcomes; gate FAIL or critical UNKNOWN; evidence invalidation), shall connect the change, incident and evidence systems so that trigger events are routed to the lead assessor and capability owner, and shall verify at least once per trigger test interval, by injecting a test event, that triggers reach the responsible roles and initiate reassessment.

**Assessment criteria**

1. Each current decision has defined reassessment triggers covering change, incident, gate and evidence events.
2. Change, incident and evidence systems route trigger events to the lead assessor and capability owner.
3. Every material change and Service Outcome incident in the period was matched to a trigger response.
4. An injected test event within the interval reached the responsible roles and initiated the reassessment workflow.
5. Trigger responses record the affected claims, gates and decisions and the outcome.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Trigger test interval | months | 6 | Programme parameter; illustrative |

**Minimum evidence**

- Trigger definitions per decision
- Integration configuration between change, incident and evidence systems and the assurance workflow
- Trigger response records
- Injected test event record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-4 |
| requiredClasses | E2; E3; E4 |
| optionalClasses | E1; E7 |
| qualityFloor | P3 F4 C4 R4 T3 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; TRANSITION |
| periodCoverage | Twelve months preceding the assessment and the latest trigger test |
| independence | Assessor reconciles the full change and incident logs to trigger responses |
| mandatoryItems | Trigger definitions per decision; Trigger response records; Injected test event record |
| acceptableAlternatives | A genuine trigger event fully traced from source system to reassessment, in place of an injected test |
| unknownEffect | US3 Material: current decisions may persist after invalidating change; CG-14 evaluation records the gap |
| reassessmentTriggers | Integration change; Missed trigger found; New change or incident system |

**Assessment methods.** TEST, RECONCILIATION, INSPECTION, DOCUMENT_REVIEW

**Assessment procedure**

1. Review trigger definitions per current decision.
2. Inspect integration configuration.
3. Reconcile material changes and incidents to trigger responses.
4. Examine or perform an injected test event with the tool owner.

**Gate mappings.** CG-14 Change control (SUPPORTING)

**Applicability.** Applies to every programme with decisions remaining valid after issue.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, TRANSITION

**Failure modes addressed.** Cooling conversion completed but prior CG-06 PASS still relied upon; Incident ticket never reaches the assurance team; Trigger fires to a mailbox nobody monitors; Provider change outside the owner's change system

**Testing safety.** Injected test events are clearly marked as tests in non-production change or incident queues, or use a test category agreed with the tool owner; they shall not page operational on-call staff or alter real change records.

**UNKNOWN rule.** If provider-originated changes are not routed, record a U10 UNKNOWN for provider-dependent claims.

**Ontology classes.** ReassessmentTrigger, Event, AssuranceDecision, IntegrationHandoff · **Related controls.** MCF-CAP-023, MCF-EVA-021, MCF-EVA-024, MCF-EVA-023

**Informative references.** ISO/IEC 20000-1 (service management system) - change and incident management; AIDCF-014 End-to-End Traceability and Machine-Executable Data Standard; AIDCF-011 Assurance Program Framework

### MCF-EVA-023

**Monitoring Coverage** · DETECTIVE · claim type OPERATION · required AL4

**Objective.** Ensure that where continuing assurance is claimed, the specific claims monitored, the telemetry and evidence feeds used, their coverage and their blind spots are defined, and that feed health is itself monitored.

**Requirement.** The assurance programme lead shall, for each claim under continuing assurance, define the monitored indicators, their source feeds, coverage across assets, locations and operating states, thresholds that trigger review, and known blind spots. The tool owner shall monitor feed health (gaps, latency, clock integrity, dropped data) and alert the evidence lead on degradation; the programme lead shall state blind spots in each continuing-assurance report.

**Assessment criteria**

1. Each claim under continuing assurance has defined indicators, feeds, coverage, thresholds and blind spots.
2. Feed coverage reconciles to the in-scope asset and location population.
3. Feed health is monitored, and degradations in the period were alerted and actioned.
4. Threshold breaches in the period triggered review.
5. Continuing-assurance reports state blind spots and feed-health limitations.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Maximum tolerated feed gap | % of period | 5 | Programme parameter; illustrative |

**Minimum evidence**

- Continuing assurance claim definitions
- Feed coverage reconciliation
- Feed-health monitoring records
- Threshold breach review records
- Continuing-assurance reports

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-3 |
| requiredClasses | E2; E3; E7 |
| optionalClasses | E1 |
| qualityFloor | P4 F4 C4 R4 T4 I3 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; DEGRADED; MAINTENANCE |
| periodCoverage | Twelve months preceding the assessment |
| independence | Assessor reconciles feed coverage to asset registers independently |
| mandatoryItems | Continuing assurance claim definitions; Feed coverage reconciliation; Feed-health monitoring records |
| acceptableAlternatives | Observability platform coverage reports, if they map to assurance claims |
| unknownEffect | US3 Material: continuing-assurance claims unsupported; continuing claims reverted to point-in-time with condition |
| reassessmentTriggers | New assets not onboarded to monitoring; Feed outage beyond tolerance; Change of observability platform |

**Assessment methods.** RECONCILIATION, ANALYSIS, INSPECTION, DOCUMENT_REVIEW

**Assessment procedure**

1. Review continuing-assurance claim definitions.
2. Reconcile feed coverage to asset and location registers.
3. Analyse feed-health records for gaps and actions.
4. Trace threshold breaches to reviews.
5. Check blind-spot disclosure in reports.

**Gate mappings.** None

**Applicability.** Applies only where continuing assurance (AL6) is claimed; otherwise NOT_APPLICABLE.

**Lifecycle stages.** OPERATE · **Operating states.** NORMAL, DEGRADED, MAINTENANCE

**Failure modes addressed.** Continuous assurance claimed while half the CDUs report no telemetry; Clock drift corrupts event ordering; New hall never onboarded to monitoring; Blind spots omitted from report

**Testing safety.** Read-only access to observability and monitoring systems.

**UNKNOWN rule.** If feed coverage cannot be reconciled, record a U5 UNKNOWN and do not describe the claim as continuously assured.

**Ontology classes.** ReassessmentTrigger, EvidenceObject, AssuranceReport · **Related controls.** MCF-EVA-022, MCF-EVA-021, MCF-CAP-013

**Informative references.** AIDCF-011 Assurance Program Framework; NIST SP 800-137 (information security continuous monitoring); NIST SP 800-92 (guide to computer security log management)

### MCF-EVA-024

**Decision Suspension and Supersession** · RECOVERY · claim type RESILIENCE · required AL5

**Objective.** Ensure that when a decision can no longer be relied upon (material change, incident, gate FAIL, evidence invalidation, expiry), it is suspended, withdrawn or superseded promptly, intended users are notified, and history is preserved, so that failure of a prior conclusion is contained.

**Requirement.** The decision authority shall define criteria for suspension, withdrawal and supersession of Assurance Decisions, shall act on each trigger response that meets the criteria within the suspension time, shall notify all intended users and recipients of external communications, and shall preserve the prior decision, its evidence manifest and the reason for change. The programme lead shall rehearse the suspension and notification process at least once per rehearsal interval.

**Assessment criteria**

1. Suspension, withdrawal and supersession criteria are defined.
2. Each trigger response meeting the criteria in the period resulted in suspension, withdrawal or supersession within the suspension time.
3. All intended users and external recipients were notified.
4. Prior decisions, manifests and reasons are preserved and linked by SUPERSEDES relationships.
5. A rehearsal within the interval exercised suspension and notification end to end, or a real suspension did so.

**Capability-profile parameters**

| Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|
| Suspension time after qualifying trigger | working days | 5 | Programme parameter; illustrative |
| Suspension rehearsal interval | months | 12 | Programme parameter; illustrative |

**Minimum evidence**

- Suspension, withdrawal and supersession criteria
- Trigger response and decision lifecycle records
- Notification records
- Decision history with SUPERSEDES links
- Rehearsal or real-event record

**Evidence requirement profile**

| Field | Value |
|---|---|
| profileTier | CP-5 |
| requiredClasses | E1; E3; E4; E7 |
| optionalClasses | E6 |
| qualityFloor | P4 F4 C4 R4 T3 I4 |
| sufficiencyFloor | S4 |
| stateCoverage | NORMAL; RECOVERY |
| periodCoverage | Twelve months preceding the assessment and the latest rehearsal |
| independence | Rehearsal observed by the independent reviewer |
| mandatoryItems | Suspension, withdrawal and supersession criteria; Trigger response and decision lifecycle records; Rehearsal or real-event record |
| acceptableAlternatives | Real suspension event fully traced, in place of a rehearsal |
| unknownEffect | US3 Material: reliance on invalid decisions may continue; condition recorded and current decisions reviewed |
| reassessmentTriggers | Qualifying trigger not acted upon; Change of intended users; Change of decision authority |

**Assessment methods.** SCENARIO_EXERCISE, DOCUMENT_REVIEW, RECONCILIATION, SAMPLING

**Assessment procedure**

1. Review criteria.
2. Reconcile qualifying trigger responses to lifecycle actions and timing.
3. Check notifications to intended users and external recipients.
4. Inspect history preservation and SUPERSEDES links.
5. Examine or observe a rehearsal.

**Gate mappings.** None

**Applicability.** Applies to every programme with decisions relied upon after issue.

**Lifecycle stages.** OPERATE, CHANGE · **Operating states.** NORMAL, RECOVERY

**Failure modes addressed.** Customer still relying on a decision invalidated by a cooling incident; Superseded decision deleted; Suspension notice not sent to external recipients; Gate FAIL after incident not acted on

**Testing safety.** Rehearsals use test decision records and test distribution lists; no notice is sent to real external recipients during a rehearsal.

**UNKNOWN rule.** If decision history cannot be shown to be preserved, record a U7 UNKNOWN against prior decisions' traceability.

**Ontology classes.** AssuranceDecision, ReassessmentTrigger, AssuranceStatement, DistributionControl · **Related controls.** MCF-EVA-022, MCF-EVA-021, MCF-GOV-020, MCF-EVA-019

**Informative references.** AIDCF-012 Reporting and Assurance Statement Standard; AIDCF-011 Assurance Program Framework; ISO 22301 (business continuity management systems) - exercising
