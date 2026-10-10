# AIDCF-018-EVA Evidence, Assessment and Assurance Management Domain Guide

## Document control

| Field | Value |
|---|---|
| Document ID | AIDCF-018-EVA |
| Title | Evidence, Assessment and Assurance Management Domain Guide |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Parent artifact | AIDCF-018 Domain Guides |
| Normative basis | AIDCF-007A (controls MCF-EVA-001 to MCF-EVA-024), AIDCF-006, AIDCF-008, AIDCF-009, AIDCF-010, AIDCF-011, AIDCF-012, AIDCF-014 |
| Requirement prefix | DG-EVA-REQ-NNN |

### Revision history

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-10 | Initial issue: domain guide aligned to the rewritten EVA controls, the AIDCF-008 evidence vocabularies and the control-level gate mappings of AIDCF-010. |

**Normative status.** This guide is informative except for the requirements labelled DG-EVA-REQ-NNN. The normative control requirements are those in the AIDCF-007A registry, and the evidence vocabularies are those of AIDCF-008; both prevail if this guide differs. Normative keywords follow ISO/IEC Directives Part 2 usage.

## 1 Purpose and scope

EVA assures the assurance. It covers the evidence system, the planning and execution of assessments, the treatment of Findings, UNKNOWN Records, conflicts and limitations, the evaluation of gates and decisions, and the mechanisms that keep a decision valid or withdraw it. It contains 24 controls in six families:

| Family | Name | Controls |
|---|---|---|
| EVA-01 | Evidence architecture | MCF-EVA-001 to 004 |
| EVA-02 | Evidence provenance and quality | MCF-EVA-005 to 008 |
| EVA-03 | Assessment planning and execution | MCF-EVA-009 to 012 |
| EVA-04 | Findings, UNKNOWN and limitations | MCF-EVA-013 to 016 |
| EVA-05 | Critical gates and decisions | MCF-EVA-017 to 020 |
| EVA-06 | Reassessment and continuing assurance | MCF-EVA-021 to 024 |

**In scope.** Evidence Requirement profiles; evidence ownership and requests; the evidence repository, manifests, retention, classification and recoverability; provenance, integrity and custody (including derived and AI-assisted evidence); quality ratings (P, F, C, R, T, I), currency and coverage; decision questions and scope; sampling and testing discipline; specialist involvement; Findings, UNKNOWN Records, conflicts and limitations; gate applicability, gate evidence, independent decision and claim language; evidence expiry, reassessment triggers, monitoring coverage and decision suspension or supersession.

**Out of scope.** The authority structures that appoint the decision authority, reviewers and assessors, and their independence and competence (GOV); the definition of the Capability Instance and Service Outcomes (CAP); the technical correctness of domain conclusions (each infrastructure domain); the security of the evidence platform as an IT system beyond evidence-specific protection (SEC).

**Boundary with other domains.** GOV governs (who may decide, who is independent); EVA computes and evidences (what was known, how well, and what follows). MCF-GOV-008 assigns evidence custody accountability; MCF-EVA-006 tests that integrity and custody mechanisms detect alteration. MCF-GOV-015 governs the gate register; MCF-EVA-017 and MCF-EVA-018 determine applicability and evidence for each gate.

## 2 Why this domain matters for AI capability

1. **Evidence volume and velocity are higher.** AI infrastructure produces telemetry at high rates from accelerators, fabrics, CDUs, EPMS and BMS; configuration changes through automated pipelines; and fleets of thousands of near-identical nodes. Without disciplined coverage and sampling (MCF-EVA-008, MCF-EVA-011), a handful of good examples is easily extrapolated to a fleet.
2. **Reality diverges from design faster.** Firmware, capping profiles, scheduler policies and setpoints change frequently. Evidence currency must be change-based, not calendar-based (MCF-EVA-008, MCF-EVA-021), and changes must trigger reassessment reliably (MCF-EVA-022).
3. **Evidence spans organisations.** Facility evidence often sits with a colocation provider, platform evidence with a cloud or OEM, and workload evidence with the tenant. Ownership of evidence requests and explicit UNKNOWN Records for refusals (MCF-EVA-002) prevent silent scope erosion.
4. **Derived and AI-assisted evidence is common.** Capacity analyses, dependency-path inference and AI-assisted extraction from commissioning dossiers are useful but can launder weak sources into confident outputs. MCF-EVA-005 requires lineage and human review, and prohibits AI-generated content from corroborating its own sources.
5. **Critical gates must not be averaged away.** High consequence and tight coupling mean one failed heat-removal path or one unowned dependency can defeat the outcome regardless of a strong average score. MCF-EVA-017 and MCF-EVA-018 make gate evaluation explicit and floor-bound, and MCF-EVA-014 keeps UNKNOWN visible.
6. **Reliance is external and consequential.** Decisions inform training commitments, financing and regulatory engagement. Bounded claim language (MCF-EVA-020), limitation disclosure (MCF-EVA-016) and prompt suspension (MCF-EVA-024) keep reliance proportionate.

## 3 Reference patterns and variants

| Pattern | Description | EVA emphasis |
|---|---|---|
| E-P1 Document-centric repository | Evidence held as files with a register | Manifest generation, immutability, metadata completeness (MCF-EVA-003); higher risk of untraced derived evidence |
| E-P2 Graph-native assurance record | Evidence, assertions, controls and gates held as AIDCF-014 objects and relationships | Graph queries for coverage and gate-control lists; tool configuration verification (with MCF-GOV-004) |
| E-P3 Federated evidence | Provider and tenant evidence exchanged across organisations | Custody of transfers, provider source owners, restricted evidence and U2 UNKNOWN handling |
| E-P4 Continuous evidence feeds | Telemetry and configuration feeds monitored for continuing assurance (AL6) | Monitoring coverage, feed health and blind-spot disclosure (MCF-EVA-023); trigger integration (MCF-EVA-022) |
| E-P5 AI-assisted evidence processing | Models extract, classify or summarise evidence | Candidate status, model/version records, human review, no self-corroboration (MCF-EVA-005) |

Assessment variants from AIDCF-011 (baseline, readiness, design, implementation, operational, resilience, major change, incident-triggered, periodic, continuous) change which claim types and gates are planned but use the same EVA controls.

## 4 Required functions and capability linkage

EVA implements steps 1 and 10 to 16 of the canonical chain, and the loop back to step 2:

| Chain step | EVA controls |
|---|---|
| 1 Decision Question | MCF-EVA-009 |
| (context) Boundary, criteria, exclusions | MCF-EVA-010 |
| 10 Evidence Requirement | MCF-EVA-001, MCF-EVA-002 |
| 11 Evidence Object | MCF-EVA-003 to MCF-EVA-008 |
| 12 Control Assessment | MCF-EVA-011, MCF-EVA-012 |
| 13 Finding / UNKNOWN Record | MCF-EVA-013 to MCF-EVA-016 |
| 14 Gate Result | MCF-EVA-017, MCF-EVA-018 |
| 15–16 Recommendation and Assurance Decision | MCF-EVA-019, MCF-EVA-020 |
| Report and Reassessment Trigger | MCF-EVA-021 to MCF-EVA-024 |

In ISO/IEC/IEEE 15026-2 terms, EVA supplies the Evidence elements, keeps Defeaters (Findings, UNKNOWN Records, CHALLENGES relationships) attached to the claims they challenge, and records Context (boundary, states, exclusions) so that the argument cannot silently broaden.

## 5 Dependencies, fault domains, common-mode concerns

- **Single repository.** Every decision depends on one evidence repository; loss or corruption affects every decision's reviewability. MCF-EVA-004 requires backups in a separate fault domain and tested restoration with hash verification.
- **Single telemetry pipeline.** Many E3 objects across domains may derive from one observability platform; a clock fault or ingestion gap affects them all at once and can masquerade as independent corroboration. MCF-EVA-007 rates reliability with this in mind, and MCF-EVA-023 monitors feed health.
- **Duplicated sources.** The same commissioning report, provider attestation or telemetry query may be cited by several controls; DUPLICATES relationships (AIDCF-008) must be recorded so it is not counted as diverse evidence.
- **Assessment tool configuration.** Gate-control lists, vocabularies and roll-up logic implemented in one tool are a common-mode dependency for all Gate Results (MCF-EVA-017, with MCF-GOV-004).
- **Shared people.** The same assessor rating evidence, resolving conflicts and drafting the recommendation reduces method diversity; re-rating (MCF-EVA-007) and independent decision (MCF-EVA-019) break the chain.
- **Provider access.** Evidence held by one provider for several domains (power, cooling, physical) makes all of them subject to one access decision; a refusal propagates as U2 UNKNOWN Records across domains.

## 6 Threats, hazards and failure scenarios with propagation paths to Service Outcomes

EVA failures do not damage infrastructure directly; they cause wrong conclusions to be relied upon, which then fail to prevent or contain infrastructure failure.

| ID | Scenario | Propagation path | Outcome consequence | Primary EVA safeguards |
|---|---|---|---|---|
| EVA-FS-01 | CG-06 passed on an old CDU failover test that predates a cooling conversion | Stale E4 → gate PASS → capability expanded → CDU failover fails under new heat load | Availability and performance outcomes breached; decision relied upon was invalid | MCF-EVA-008, MCF-EVA-021, MCF-EVA-022 |
| EVA-FS-02 | Provider refuses access to UPS test reports; request closed as "not provided" | Missing evidence silently dropped → CG-05 assessed on design only → PASS | Recovery and availability outcomes unsupported | MCF-EVA-002, MCF-EVA-014, MCF-EVA-018 |
| EVA-FS-03 | AI summary of commissioning dossiers states "all failover tests passed"; one test was deferred | Candidate evidence treated as corroboration → deferred test unnoticed | Failover untested in service | MCF-EVA-005, MCF-EVA-007 |
| EVA-FS-04 | Design single-line diagram shows 2N; EPMS topology shows a shared upstream breaker; design accepted | Conflict resolved toward intent → common-mode path unreported | Uncontained failure across both paths | MCF-EVA-015 |
| EVA-FS-05 | Three healthy nodes sampled from a fleet with mixed firmware | Over-extrapolation → firmware defect in unsampled stratum | Performance or integrity outcome breached | MCF-EVA-011, MCF-EVA-008 |
| EVA-FS-06 | US4 UNKNOWN on recovery checkpoint integrity reworded as "improvement opportunity" in the executive report | UNKNOWN lost → decision REASONABLY_ASSURED → customer commitment | Integrity and recovery outcomes unsupported | MCF-EVA-014, MCF-EVA-016, MCF-EVA-020 |
| EVA-FS-07 | Incident affecting cooling not routed to the assurance team | No trigger → decision remains active | Continued reliance on invalid decision | MCF-EVA-022, MCF-EVA-024 |
| EVA-FS-08 | Test report edited after collection to remove an anomaly | Integrity failure → anomaly hidden | Weakness remains unaddressed | MCF-EVA-006 |

## 7 Safeguards

- **Evidence Requirement profiles never weaker than the registry**, with local subtypes mapped to AIDCF-008 classes (MCF-EVA-001).
- **Named source owners and explicit UNKNOWN Records for unfulfilled requests** (MCF-EVA-002).
- **Immutable identifiers, mandatory metadata and frozen manifests with hashes** per decision (MCF-EVA-003).
- **Retention classes, legal holds and tested restoration in a separate fault domain** (MCF-EVA-004).
- **Provenance and lineage for derived and AI-assisted evidence, with human review** (MCF-EVA-005).
- **Integrity values from collection, pre-decision re-verification and tamper exercises** (MCF-EVA-006).
- **Six-dimension quality vectors with independent re-rating** (MCF-EVA-007).
- **Change-based currency and explicit coverage across states and strata** (MCF-EVA-008).
- **Approved decision question and scope before fieldwork** (MCF-EVA-009, MCF-EVA-010).
- **Documented, reproducible sampling; authorised, safe tests with assessors observing** (MCF-EVA-011).
- **Specialist approval for technical conclusions** (MCF-EVA-012).
- **Traceable Findings closed only on re-assessed evidence** (MCF-EVA-013).
- **UNKNOWN preservation tested end to end** (MCF-EVA-014); **conflicts registered with both lineages** (MCF-EVA-015); **limitations disclosed in every report** (MCF-EVA-016).
- **Gate applicability and floor-bound gate evidence** (MCF-EVA-017, MCF-EVA-018); **independent decision with no automated approval** (MCF-EVA-019); **controlled claim language** (MCF-EVA-020).
- **Expiry detection, tested triggers, monitored feeds and rehearsed suspension** (MCF-EVA-021 to MCF-EVA-024).

## 8 Critical-gate linkage

EVA contributes two CRITICAL controls to gates that protect the definition of the assurance subject: MCF-EVA-009 for CG-01 and MCF-EVA-010 for CG-02. Its remaining controls implement the doctrine of the meta-gates CG-11 (Evidence sufficiency) and CG-12 (Critical UNKNOWN).

| Gate | CRITICAL controls in this domain | SUPPORTING controls in this domain |
|---|---|---|
| CG-01 | MCF-EVA-009 Decision Question (DESIGN) | — |
| CG-02 | MCF-EVA-010 Scope and Criteria (DESIGN) | — |
| CG-04 | — | MCF-EVA-011 |
| CG-13 | — | MCF-EVA-002, MCF-EVA-019 |
| CG-14 | — | MCF-EVA-022 |

Notes on the mapping:

- **CG-01 and CG-02.** Without an approved decision question (MCF-EVA-009) the top claim has no Q; without an approved, reconciled scope (MCF-EVA-010) the boundary has no integrity. Either failure directly defeats its gate, so both are CRITICAL. An UNKNOWN on either is US5 Systemic and caps the decision at INCONCLUSIVE.
- **CG-11 and CG-12 are not mapped per control.** Under AIDCF-010 they are evaluated across all controls: CG-11 asks whether evidence for decisive claims meets floors; CG-12 asks whether any US4/US5 UNKNOWN Record lacks disposition. EVA-01, EVA-02 and EVA-04 controls are the mechanisms those evaluations depend on. A NONCONFORMING result on, for example, MCF-EVA-007 or MCF-EVA-014 is therefore not a CG-11 or CG-12 result in itself; it is a reason the CG-11 or CG-12 evaluation may be unable to conclude, recorded through the control's unknownEffect.
- **Gate mechanics controls (MCF-EVA-017, MCF-EVA-018)** have no per-gate mapping because they operate on every gate equally; a failure of either makes affected Gate Results unreliable, which is why their UNKNOWN effect is US4.
- **CG-13** receives SUPPORTING inputs from evidence ownership (MCF-EVA-002) and independent decision (MCF-EVA-019). **CG-14** receives a SUPPORTING input from change triggers (MCF-EVA-022). **CG-04** receives a SUPPORTING input from sampling and testing discipline (MCF-EVA-011), which governs test authorisation and safety.

**DG-EVA-REQ-001** Every gate evaluation report shall state, for CG-11 and CG-12, which EVA control results (if any) limited the evaluation and how.

## 9 Capability-profile parameters

All defaults are illustrative and shall be replaced by programme or engagement values approved in the capability profile or assurance plan.

| Control | Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|---|
| MCF-EVA-002 | Evidence request response time | working days | 10 | Engagement parameter; illustrative |
| MCF-EVA-004 | Evidence repository restoration test interval | months | 12 | Programme parameter; illustrative |
| MCF-EVA-006 | Integrity detection test interval | months | 12 | Programme parameter; illustrative |
| MCF-EVA-007 | Independent re-rating sample | % of supporting Evidence Objects | 10 | Programme parameter; illustrative, minimum of 10 objects |
| MCF-EVA-014 | UNKNOWN traceability test set size | UNKNOWN Records | 10 | Programme parameter; illustrative |
| MCF-EVA-021 | Expiry response time | working days | 20 | Programme parameter; illustrative |
| MCF-EVA-022 | Trigger test interval | months | 6 | Programme parameter; illustrative |
| MCF-EVA-023 | Maximum tolerated feed gap | % of period | 5 | Programme parameter; illustrative |
| MCF-EVA-024 | Suspension time after qualifying trigger | working days | 5 | Programme parameter; illustrative |
| MCF-EVA-024 | Suspension rehearsal interval | months | 12 | Programme parameter; illustrative |

## 10 Evidence expectations by claim type

| Claim type | Controls | Profile tiers | Required classes (union) | Sufficiency floors |
|---|---|---|---|---|
| DESIGN | MCF-EVA-001, MCF-EVA-009, MCF-EVA-010, MCF-EVA-017 | CP-1, CP-2 | E1+E7 | S3 |
| IMPLEMENTATION | MCF-EVA-002, MCF-EVA-003, MCF-EVA-011, MCF-EVA-012, MCF-EVA-019 | CP-2 | E1+E2+E3+E4 | S3 |
| OPERATION | MCF-EVA-005, MCF-EVA-007, MCF-EVA-008, MCF-EVA-013, MCF-EVA-015, MCF-EVA-016, MCF-EVA-018, MCF-EVA-020, MCF-EVA-021, MCF-EVA-023 | CP-3 | E1+E2+E3+E7 | S4 |
| EFFECTIVENESS | MCF-EVA-006, MCF-EVA-014, MCF-EVA-022 | CP-4 | E2+E3+E4+E7 | S4 |
| RESILIENCE | MCF-EVA-004, MCF-EVA-024 | CP-5 | E1+E2+E3+E4+E7 | S4 |

- **DESIGN (AL2).** Approved records (E1) and derivations (E7): the decision question, scope record, evidence profiles and gate applicability. Approval shall come from the decision authority, separate from the author.
- **IMPLEMENTATION (AL3).** The evidence system as configured: repository configuration exports and manifests (E2), request records, sampling plans and test authorisations, specialist approvals and decision workflow configuration (E1, E2, E3).
- **OPERATION (AL4).** The evidence system in use over a period: provenance and quality records across completed assessments, conflicts handled, limitations disclosed, gate packages assembled, claim language screened, expiry monitored (E1, E3, E7).
- **EFFECTIVENESS (AL5).** Demonstrations that detection mechanisms work: tamper exercises (MCF-EVA-006), UNKNOWN traceability or seeded-UNKNOWN tests (MCF-EVA-014), injected trigger events (MCF-EVA-022) (E4 with E3).
- **RESILIENCE (AL5).** Recovery of the evidence system and of reliance: tested repository restoration with hash verification (MCF-EVA-004) and rehearsed suspension and notification (MCF-EVA-024).

Self-reference caution: EVA controls are assessed with evidence produced by the evidence system they assess. To avoid circularity, the assessor should extract records directly from systems of record, recompute hashes with an independent tool, and have the independent reviewer reperform at least one roll-up and one severity assignment.

## 11 Assessment guidance

**Sequence.**

1. Before fieldwork: MCF-EVA-009 and MCF-EVA-010 (stop if either is not approved), MCF-EVA-017 (gate applicability), MCF-EVA-001 (profiles).
2. During fieldwork: MCF-EVA-002, MCF-EVA-005 to MCF-EVA-008, MCF-EVA-011, MCF-EVA-012 — evaluated continuously as evidence arrives, not only at the end.
3. At evaluation: MCF-EVA-013 to MCF-EVA-016, MCF-EVA-018.
4. At decision: MCF-EVA-019, MCF-EVA-020.
5. Programme-level, periodically: MCF-EVA-003, MCF-EVA-004, MCF-EVA-021 to MCF-EVA-024.

**Interviews.** Evidence lead; lead assessor; domain specialists; independent reviewer; decision authority; tool owner (repository, workflow, monitoring); provider evidence contacts.

**Inspections.** Repository configuration and access roles; manifest generation and freeze; hash values; workflow audit logs for decision approval; integration configuration between change, incident and evidence systems; monitoring feed-health dashboards.

**Sampling.** Draw Evidence Objects for provenance, quality and currency tests weighted toward those supporting gate-CRITICAL controls; draw Findings and UNKNOWN Records from full registers including closed and superseded items; draw reports and statements from the full set issued, not a management selection.

**Reperformance.** Re-rate a sample of evidence (MCF-EVA-007); reperform severity assignment (MCF-EVA-014); reapply the gate roll-up (MCF-EVA-018); re-run one derived-evidence transformation (MCF-EVA-005); reperform one sampling selection from its population frame (MCF-EVA-011).

**DG-EVA-REQ-002** Hash verification of decision manifests for this domain shall be performed with a tool independent of the repository being assessed.

**DG-EVA-REQ-003** Where an EVA control is assessed by the team that operates the evidence system, the result shall carry a confidence ceiling of CONF-2 unless reperformed by the independent reviewer.

## 12 Testing safety

EVA tests are information-system tests, and the principal risks are to evidence integrity, operational alerting and external communication:

- **Tamper exercises (MCF-EVA-006)** use dedicated test objects in a non-production area with the evidence lead's written approval; real evidence is never altered.
- **Restoration tests (MCF-EVA-004)** restore to an isolated target; the production repository is never overwritten.
- **Injected trigger events (MCF-EVA-022)** use test categories or non-production queues agreed with the tool owner; they shall not page on-call operations staff or alter real change records.
- **Seeded-UNKNOWN tests (MCF-EVA-014)** use labelled copies of completed assessments.
- **Suspension rehearsals (MCF-EVA-024)** use test decision records and test distribution lists; no notice reaches real external recipients.
- **MCF-EVA-011 governs the safety of all assessment testing in every domain.** Hazardous-energy, pressurised-fluid, refrigerant, battery and service-affecting tests require written authorisation from the system owner and the safety authority, a method statement, initial-state verification, abort criteria, permits and restoration steps; assessors observe and do not operate equipment; the safety authority may stop any test, and a stopped test is recorded with its partial result and does not count as passed.

**DG-EVA-REQ-004** No EVA test shall modify, delete or re-classify a production Evidence Object, Finding, UNKNOWN Record, Gate Result or Assurance Decision.

## 13 UNKNOWN hot-spots and how to resolve them

| Hot-spot | Typical UNKNOWN type | Severity | Resolution route |
|---|---|---|---|
| No approved decision question or scope | U1 | US5 | Decision authority approves before fieldwork; otherwise decision ≤ INCONCLUSIVE |
| Provider refuses access to evidence | U2 | US4 where it concerns a gate-critical control | Clause-limited disclosure, witnessed viewing, provider attestation with sampled underlying evidence; otherwise retain UNKNOWN |
| Telemetry clock or ingestion gaps | U5 / U7 | US3, US4 if the evidence is gate-decisive | Re-extract from source with clock verification; bound the period |
| Design/observed conflict on redundancy | U4 | US4 (CG-05 or CG-09 criterion) | Corroborate by inspection or protection-setting export; specialist review; observed evidence prevails unless shown unrepresentative |
| AI-extracted evidence with no source passage links | U6 | US3 | Re-extract with citations; human verification of a sample |
| Decision manifest not retrievable | U1 | US3, escalated to MCF-EVA-024 review | Rebuild manifest from repository history; if impossible, suspend reliance |
| Evidence predates material change | U3 | US3, US4 for gate-decisive tests | Re-test or re-collect post-change |
| UNKNOWN register completeness doubtful | U5 | US4 | Workpaper search; reviewer reperformance |

## 14 Interfaces with other domains

| Domain | Interface |
|---|---|
| GOV | Custody accountability (MCF-GOV-008), gate governance (MCF-GOV-015), independent review (MCF-GOV-016), external reporting (MCF-GOV-020), independence and competence of evidence roles |
| CAP | Decision question and scope reference Capability Instances, Service Outcomes and the ArchitectureSnapshot; change impact feeds reassessment triggers |
| All infrastructure domains (PHY, POW, THM, ENV, CMP, STO, NET) | Evidence profiles, sampling and test discipline, specialist approval, gate evidence packages |
| OPS | Change and incident records as trigger sources; document control of procedures used as evidence |
| SEC | Protection of the evidence repository and workflow tools; privileged access used for configuration extraction |
| SUP | Provider evidence transfer, provider assurance reliance and non-inheritance |
| RES | Recovery test evidence and exercise records; recovery of the evidence system itself |
| DEP | U10 dependency-unknown records; evidence of external dependencies |

## 15 Informative references

Document-level references only.

- ISO/IEC/IEEE 15026-2 — Assurance case.
- ISO 19011 — Guidelines for auditing management systems.
- ISAE 3000 — Assurance engagements other than audits or reviews of historical financial information.
- ISO/IEC 17020 — Requirements for bodies performing inspection; ISO/IEC 17000 — Conformity assessment vocabulary.
- ISO/IEC 27037 — Identification, collection, acquisition and preservation of digital evidence; ISO/IEC 27042 — Analysis and interpretation of digital evidence; ISO/IEC 27050 series — Electronic discovery.
- ISO 15489-1 — Records management; ISO 14721 — Open archival information system (OAIS) reference model.
- ISO/IEC 27001 — Information security management systems; ISO/IEC 27040 — Storage security.
- W3C PROV-DM — Provenance data model.
- ISO 2859-1 — Sampling procedures for inspection by attributes.
- NIST SP 800-92 — Computer security log management; NIST SP 800-137 — Information security continuous monitoring.
- ISO/IEC 20000-1 — Service management system (change and incident management).
- ISO 22301 — Business continuity management systems (exercising).
- AIDCF-006, AIDCF-008, AIDCF-009, AIDCF-010, AIDCF-011, AIDCF-012, AIDCF-014.

## 16 Control summary table

| Control ID | Title | Control type | AL | Claim type | Gate mappings |
|---|---|---|---|---|---|
| MCF-EVA-001 | Evidence Taxonomy | DIRECTIVE | AL2 | DESIGN | — |
| MCF-EVA-002 | Evidence Ownership | DIRECTIVE | AL3 | IMPLEMENTATION | CG-13 SUPPORTING |
| MCF-EVA-003 | Evidence Repository | PREVENTIVE | AL3 | IMPLEMENTATION | — |
| MCF-EVA-004 | Retention and Protection | RECOVERY | AL5 | RESILIENCE | — |
| MCF-EVA-005 | Source Provenance | PREVENTIVE | AL4 | OPERATION | — |
| MCF-EVA-006 | Integrity and Custody | DETECTIVE | AL5 | EFFECTIVENESS | — |
| MCF-EVA-007 | Relevance and Reliability | PREVENTIVE | AL4 | OPERATION | — |
| MCF-EVA-008 | Currency and Coverage | PREVENTIVE | AL4 | OPERATION | — |
| MCF-EVA-009 | Decision Question | DIRECTIVE | AL2 | DESIGN | CG-01 CRITICAL |
| MCF-EVA-010 | Scope and Criteria | DIRECTIVE | AL2 | DESIGN | CG-02 CRITICAL |
| MCF-EVA-011 | Sampling and Testing | PREVENTIVE | AL3 | IMPLEMENTATION | CG-04 SUPPORTING |
| MCF-EVA-012 | Specialist Involvement | PREVENTIVE | AL3 | IMPLEMENTATION | — |
| MCF-EVA-013 | Finding Traceability | DETECTIVE | AL4 | OPERATION | — |
| MCF-EVA-014 | UNKNOWN Preservation | DETECTIVE | AL5 | EFFECTIVENESS | — |
| MCF-EVA-015 | Conflict Handling | CORRECTIVE | AL4 | OPERATION | — |
| MCF-EVA-016 | Limitation Disclosure | DETECTIVE | AL4 | OPERATION | — |
| MCF-EVA-017 | Gate Applicability | DIRECTIVE | AL2 | DESIGN | — |
| MCF-EVA-018 | Gate Evidence | PREVENTIVE | AL4 | OPERATION | — |
| MCF-EVA-019 | Independent Decision | PREVENTIVE | AL3 | IMPLEMENTATION | CG-13 SUPPORTING |
| MCF-EVA-020 | Claim Language | PREVENTIVE | AL4 | OPERATION | — |
| MCF-EVA-021 | Evidence Expiry | DETECTIVE | AL4 | OPERATION | — |
| MCF-EVA-022 | Change Triggers | DETECTIVE | AL5 | EFFECTIVENESS | CG-14 SUPPORTING |
| MCF-EVA-023 | Monitoring Coverage | DETECTIVE | AL4 | OPERATION | — |
| MCF-EVA-024 | Decision Suspension and Supersession | RECOVERY | AL5 | RESILIENCE | — |

## 17 Worked synthetic example

> **SYNTHETIC EXAMPLE.** All names, organisations, values and results below are invented for illustration. They do not describe any real facility, organisation or assessment.

**Context.** A co-sourced operational assessment of Capability Instance SYN-CI-03 "Training Cluster East" in a colocation facility (evidence pattern E-P3, with AI-assisted extraction, E-P5). Decision question approved under MCF-EVA-009: "Can SYN-CI-03 sustain its training availability outcome within tolerance through loss of one UPS module and one CDU per pod, in NORMAL and MAINTENANCE states, as of 2026-09-30?" Scope approved under MCF-EVA-010; utility supply excluded with residual effect stated; provider-operated chilled-water plant in scope via provider evidence.

**Evidence handling events.**

1. *Request refused.* The provider declined to release generator load-test reports. Under MCF-EVA-002 the request was escalated and, unresolved at close, recorded as UNKNOWN Record U-SYN-03-004: type U2 Inaccessible; severity test top-down — not boundary or definition (not US5); affects the evidence for a CRITICAL control of CG-05 → **US4**.
2. *AI-assisted extraction.* A model extracted test outcomes from 140 commissioning PDFs. Under MCF-EVA-005 the output was recorded as candidate evidence with model version and process record; a reviewer verified 20 extractions against source passages and found one mis-read deferred CDU failover test. The extraction was corrected, and the full set re-verified for the "deferred" field.
3. *Conflict.* The design SLD showed independent A/B paths to each pod; the EPMS topology export showed both paths fed from one upstream board in Hall 2. Under MCF-EVA-015 both lineages were preserved; a site inspection by the electrical specialist confirmed the EPMS view. The design evidence was marked CHALLENGED, and the POW and DEP domains received a Finding of a common-mode path.
4. *Staleness.* The CDU failover test for pods 5–8 predated a rack-density increase. Under MCF-EVA-008 the test was marked STALE for the changed pods (U3), and a re-test was scheduled.

**Gate evaluation (EVA view).**

- **CG-05**: one CRITICAL control in POW is UNKNOWN because of U-SYN-03-004, and the conflict shows a demonstrated common-mode path in Hall 2. The POW specialist assessed the path as a gate criterion demonstrated not met → **CG-05 = FAIL** (FAIL takes precedence over UNKNOWN).
- **CG-06**: CDU failover CRITICAL control for pods 5–8 UNKNOWN (stale evidence; re-test pending) → **CG-06 = UNKNOWN**.
- **CG-11**: evaluated across all controls; the evidence for CG-06 is below floor for pods 5–8, and the evaluation records MCF-EVA-008 as the limiting control (DG-EVA-REQ-001).
- **CG-12**: one US4 UNKNOWN Record (U-SYN-03-004) has a disposition (owner, evidence needed, decision effect) and is carried into the report; CG-12 evaluation records it as dispositioned but unresolved.

**Decision and reporting.** The decision authority (not the lead assessor, per MCF-EVA-019) issued NOT_ASSURED for the decision question, because CG-05 FAIL controls it. The executive report (MCF-EVA-016, MCF-EVA-020) stated on its first page: CG-05 FAIL (common-mode upstream board in Hall 2), CG-06 UNKNOWN (stale CDU failover evidence, pods 5–8), and the US4 UNKNOWN on generator testing with its resolution route. No score was presented without its coverage and gate overlay.

**Reassessment.** Re-test of CDU failover for pods 5–8 and the provider's agreement to witnessed viewing of generator test reports were registered as reassessment triggers (MCF-EVA-022). A prior customer statement based on an earlier decision was withdrawn under MCF-EVA-024 within the suspension time, with history preserved and a SUPERSEDES link to the new decision.

**What this example shows.** The quality of the decision depended less on any single test than on four evidence disciplines working together: refused evidence became a visible UNKNOWN, AI-assisted extraction was checked rather than trusted, a design/observation conflict was resolved toward observed reality, and stale evidence was not allowed to support a current claim.
