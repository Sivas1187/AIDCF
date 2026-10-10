> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-VR-001_Full_Stack_Validation_Report_v1.1.pdf](AIDCF-VR-001_Full_Stack_Validation_Report_v1.1.pdf).

**AIDCF-VR-001**

**FULL-STACK VALIDATION REPORT**

**Against AIDCF-003 through AIDCF-014**

**Version 1.1**

**  
Validation subject: AIDCF-015 Reference Implementation, Synthetic Dataset and Conformance Pilot v1.0  
Conclusion: CONDITIONALLY VALIDATED AS A PILOT SPECIFICATION; NOT YET VALIDATED AS AN EXECUTABLE CONFORMANCE IMPLEMENTATION**

# Document control

| **Field** | **Value** |
|---|---|
| Public ID | AIDCF-VR-001 |
| Short code | VR |
| Former label | Filed as "AIDCF-016" in error. AIDCF-016 is the Machine-Executable Data Model Standard (`standards/aidcf-016-machine-executable-model/`). |
| Title | Full-Stack Validation Report |
| Version | 1.1 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Validation subject | AIDCF-015 pilot as at the date of version 1.0 (title page: v1.0). The AIDCF-015 v1.1, v1.2 and v1.3 packages respond to its findings. |
| Scope of version 1.1 | Relabelling, document control and the status table below. The validation content of version 1.0 (method, matrices, nonconformities, closure plan and release decision) is unchanged and records the position at the time of that validation. |

## Revision history

| **Version** | **Date** | **Summary** |
|---|---|---|
| 1.0 | Not stated | Full-stack validation of the AIDCF-015 pilot against AIDCF-003 to AIDCF-014; nonconformities NC-01 to NC-10. |
| 1.1 | 2026-10-10 | Relabelled AIDCF-VR-001 (formerly filed as AIDCF-016); document control added; status of findings as of 2026-10-10 added; original findings unchanged. |

## Status of findings as of 2026-10-10

This table records, for each nonconformity below, what the later AIDCF-015 packages provide. "Closed" means the remediation the finding asked for exists and was executed by `implementation/aidcf-015-v1.3/tools/run_all.py` on 2026-10-10 with every layer passing. All such execution is self-validation by the package author; independent execution is still required (NC-09), so none of these closures is independently verified.

| **ID** | **Status** | **Basis** |
|---|---|---|
| NC-01 | Closed | AIDCF-007A-AMD-001 adopted the 15/90/360 registry; AIDCF-015 v1.2 migrated the pilot controls to MCF identifiers (BI-001 resolved). v1.3 imports the registry unmodified and its REGISTRY layer checks 15 domains, 90 families and 360 unique controls. |
| NC-02 | Closed | v1.3 contains the machine package: JSON Schema 2020-12, JSON-LD 1.1 context, OWL 2 ontology and SHACL shapes (AIDCF-016 schema set), registry and vocabulary CSV files, a JSON-LD dataset, evidence fixtures, queries and conformance fixtures. |
| NC-03 | Closed (self-executed) | v1.3 SCHEMA and SHACL layers run over every record (closed schemas; pyshacl with the ontology graph), and positive and negative fixtures run with expected outcomes. Library versions are pinned in `requirements.txt` and inputs are hashed in `baseline/release-manifest.json`. Outputs are regenerated in `outputs/`. |
| NC-04 | Closed (self-executed) | v1.3 loads the dataset into an RDF graph and runs Q01 to Q12 (the AIDCF-014 section 19 questions) and two further queries, each compared with a hand-derived expected result. |
| NC-05 | Closed (self-executed) | v1.3 records pinned score inputs for all 360 controls, the method, a calculation hash and domain scores; the SCORE layer reperforms them. |
| NC-06 | Open | v1.3 has a programme charter, an AssuranceProgram record, assessor parties and ReviewRecords, but they are synthetic; there are no competence or independence records for real people. |
| NC-07 | Open | v1.3 has a technical report record (R2) and an assurance statement with identifiers, classification, distribution controls and validity, but the approval record is synthetic and no controlled issue has taken place. |
| NC-08 | Closed | v1.3 instantiates 34 synthetic evidence files, each with SHA-256, size and provenance on its EvidenceObject record; the INTEGRITY layer verifies them. |
| NC-09 | Open | No independent execution or signed conformance result exists. The v1.3 manifest is not signed (signatureStatus PENDING) and its approvals are PENDING. |
| NC-10 | Closed | Gate results use only PASS, FAIL, UNKNOWN, APPROVED_NA and NOT_ASSESSED, enforced by the JSON Schema enum and checked against `registries/vocabularies/gate-results.csv`; conditions are recorded only at decision level. |

# Executive conclusion

**The pilot is internally coherent as a synthetic narrative demonstration, but it does not yet contain the actual schema, ontology, SHACL, registry, JSON-LD dataset, validation-runner output or query-execution evidence needed to substantiate machine-executable T3-T7 conformance.**

| **Dimension**               | **Result**            | **Reason**                                                                                                              |
|-----------------------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------|
| Conceptual alignment        | PASS                  | The capability-first, failure-informed, evidence-gated chain is preserved.                                              |
| Architectural instantiation | PASS WITH LIMITATIONS | Representative power, cooling, compute, storage, network, security and operations objects are instantiated narratively. |
| Control alignment           | BLOCKED               | AIDCF-007 has conflicting catalogue cardinalities; pilot uses local CTL identifiers.                                    |
| Evidence model              | PARTIAL               | Evidence objects and quality concepts are present, but source files, hashes and machine manifests are not delivered.    |
| Assessment execution        | PARTIAL               | Procedures and results are specified; no independently executed workpaper/test pack is provided.                        |
| Scoring/decision            | PASS WITH LIMITATIONS | Gate dominance, UNKNOWN and bounded decisions are coherent; numeric reproducibility evidence is absent.                 |
| Reporting                   | PARTIAL               | Executive and technical examples are present; full controlled statement/report packages are not delivered.              |
| Machine executability       | NOT DEMONSTRATED      | The document lists required files but does not include the machine package.                                             |
| Conformance                 | CONDITIONAL           | Suitable as a pilot design and worked example, not yet as a T7 executable conformance claim.                            |

# Validation method

**Validation compared AIDCF-015 claims and structures with the stated doctrines and required deliverables of the artifact stack. No real engineering or assurance conclusion is expressed.**

| **Test**               | **Method**                                                               |
|------------------------|--------------------------------------------------------------------------|
| V1 Semantic            | Check objects and terms against source-artifact ownership.               |
| V2 Traceability        | Check required forward and reverse chain.                                |
| V3 Completeness        | Check each source artifact has corresponding pilot records.              |
| V4 Decision integrity  | Check UNKNOWN, gates, scores and decisions.                              |
| V5 Reporting integrity | Check reports do not exceed decision.                                    |
| V6 Change integrity    | Check event, impact, reassessment and supersession.                      |
| V7 Machine proof       | Check whether required implementation files and execution outputs exist. |
| V8 Boundary            | Check synthetic, safety and non-certification limitations.               |

# Artifact-by-artifact validation

**The matrix distinguishes semantic alignment from executed conformance.**

| **Artifact** | **Status**            | **Validation basis**                                                                                                                       | **Required closure**                                                                                               |
|--------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| AIDCF-003    | PASS                  | Capability, outcomes, functions, systems, assets, interfaces, dependencies, fault domains, states and capacity assertions are represented. | Add formal IDs/IRIs and machine records.                                                                           |
| AIDCF-004    | PASS WITH LIMITATIONS | Five scenarios include initiating condition, propagation focus, safeguards, residual effect and evidence concept.                          | Add step-level propagation records and structured threat/hazard/mode typing.                                       |
| AIDCF-005    | PASS WITH LIMITATIONS | AITG handoff registry preserves mapping types, UNKNOWN and decision federation.                                                            | Deliver actual JSON-LD/RDF handoff records and mapping-review evidence.                                            |
| AIDCF-006    | PASS                  | Capability-first, evidence gating, visible UNKNOWN, gate dominance, bounded decision, safety and human authority are retained.             | No major doctrinal conflict found.                                                                                 |
| AIDCF-007    | BLOCKER               | Pilot explicitly uses local CTL-001 to CTL-012 because the master catalogue has conflicting 15/90/360 and 14/84/336 declarations.          | Resolve cardinality, freeze canonical registry and remap all pilot controls.                                       |
| AIDCF-008    | PARTIAL               | Twelve evidence objects, quality dimensions, restrictions and an intentional missing item are described.                                   | Provide evidence-object files, manifest, hashes, provenance, transformations and validation output.                |
| AIDCF-009    | PARTIAL               | Assessment procedures, findings, UNKNOWN and CG-01 to CG-15 workbooks are represented.                                                     | Provide executed workpapers, assessor/reviewer records, sampling/test records and procedure-level evidence links.  |
| AIDCF-010    | PASS WITH LIMITATIONS | LIMITED and superseding CONDITIONALLY_ASSURED decisions respect controlling gates and UNKNOWN.                                             | Provide actual scoring inputs, weights, formulas and deterministic re-performance output.                          |
| AIDCF-011    | PARTIAL               | Governance roles, decision authority, validity, trigger and pilot workflow are defined.                                                    | Issue formal charter, profile, plan, competence/independence and quality-review records.                           |
| AIDCF-012    | PARTIAL               | Executive and technical report examples match the LIMITED decision and retain limitations.                                                 | Generate complete R1/R2 packages and controlled assurance statement with IDs, approvals and distribution controls. |
| AIDCF-013    | PASS WITH LIMITATIONS | Synthetic architecture instantiates service outcomes, systems, interfaces, dependencies, states and fault domains.                         | Produce actual architecture views, structured link records and evidence attachments.                               |
| AIDCF-014    | NOT YET DEMONSTRATED  | AIDCF-015 lists schemas, semantic files, registries, events and tests but the DOCX is a specification, not the executable package.         | Build and run JSON Schema, JSON-LD, RDF/OWL, SHACL, registries, fixtures and conformance runner.                   |
| AIDCF-015    | CONDITIONAL           | Narrative pilot is coherent and transparent about synthetic status and baseline issue.                                                     | Downgrade self-declared T3-T7 results until machine artifacts and independent run evidence exist.                  |

# End-to-end traceability validation

**The narrative chain is materially complete, but machine-verifiable links have not yet been executed.**

| **Trace segment**                           | **Result**            | **Observation**                                                                            |
|---------------------------------------------|-----------------------|--------------------------------------------------------------------------------------------|
| Capability -\> Outcomes                     | PASS                  | One capability and five outcomes.                                                          |
| Outcomes -\> Functions                      | PASS                  | Ten required functions; explicit per-outcome link file absent.                             |
| Functions -\> Architecture                  | PARTIAL               | Systems are present; allocation matrix is absent.                                          |
| Architecture -\> Dependencies/Fault Domains | PASS                  | Nine dependencies and seven fault domains.                                                 |
| Dependencies -\> Scenarios                  | PARTIAL               | Scenario relationships are described, not delivered as structured edge records.            |
| Scenarios -\> Safeguards                    | PASS WITH LIMITATIONS | Safeguards are identified; activation/state/failure properties are incomplete.             |
| Safeguards -\> Controls                     | PARTIAL               | Representative local controls used; canonical MCF mapping blocked.                         |
| Controls -\> Evidence                       | PARTIAL               | Evidence register exists; assertion-specific mapping matrix absent.                        |
| Evidence -\> Assessment Results             | PARTIAL               | Results listed; executed lineage pack absent.                                              |
| Results -\> Findings/UNKNOWN                | PASS                  | Three findings and three UNKNOWN records.                                                  |
| Findings/UNKNOWN -\> Gates                  | PASS                  | CG-06/09 UNKNOWN and CG-10 conditional control decision.                                   |
| Gates -\> Score/Decision                    | PASS WITH LIMITATIONS | Decision effect is coherent; numerical score reproduction absent.                          |
| Decision -\> Reports                        | PASS                  | Examples preserve LIMITED state and limitations.                                           |
| Event -\> Impact -\> Reassessment           | PASS WITH LIMITATIONS | Affected objects and superseding decision are specified; engine execution evidence absent. |
| AIDCF -\> AITG handoff                      | PASS WITH LIMITATIONS | Mapping registry preserves ownership; machine handoff absent.                              |

# Material nonconformities

**These items prevent a claim that the pilot is a fully executed, machine-conformant reference implementation.**

| **ID** | **Severity** | **Nonconformity**                                                                               | **Required remediation**                                                                  |
|--------|--------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| NC-01  | BLOCKER      | Canonical AIDCF-007 control registry is unresolved.                                             | Approve authoritative catalogue version and mapping migration.                            |
| NC-02  | BLOCKER      | No actual machine-readable publication package accompanies the DOCX.                            | Deliver schemas, contexts, ontology, SHACL, registries and datasets.                      |
| NC-03  | MAJOR        | No validator/SHACL execution report proves T3/T4.                                               | Run fixtures and retain output, versions and hashes.                                      |
| NC-04  | MAJOR        | No graph-load/query output proves required Q01-Q08 answers.                                     | Load dataset into a supported graph projection and capture query results.                 |
| NC-05  | MAJOR        | No deterministic scoring workbook/configuration proves reproducibility.                         | Publish inputs, formula version, outputs and re-performance test.                         |
| NC-06  | MAJOR        | No formal AIDCF-011 charter, assessment plan, competence or independence records.               | Complete program governance package.                                                      |
| NC-07  | MAJOR        | No complete AIDCF-012 issued statement/report package.                                          | Generate controlled IDs, approvals, classification, validity and supersession.            |
| NC-08  | MODERATE     | Synthetic evidence objects are described but not instantiated as files with provenance/hash.    | Publish evidence fixtures and manifest.                                                   |
| NC-09  | MODERATE     | T7 claim is self-assessed and independent rerun is pending.                                     | Independent execution and signed conformance result.                                      |
| NC-10  | MODERATE     | Some pilot gate status uses CONDITIONAL although canonical gate vocabulary should be confirmed. | Align gate vocabulary exactly with AIDCF-010 and represent conditions in separate fields. |

# Strengths confirmed

**The pilot demonstrates several important framework behaviors consistently.**

| **Strength**         | **Validation**                                                                                                                                       |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Synthetic boundary   | Repeatedly states that no real facility, engineering design or certification is represented.                                                         |
| UNKNOWN discipline   | Critical missing cooling-control independence remains explicit and constrains the initial decision.                                                  |
| Gate dominance       | CG-06 and CG-09 prevent a stronger initial decision.                                                                                                 |
| Decision progression | The initial LIMITED decision is not overwritten; the later conditional decision supersedes it.                                                       |
| Change impact        | The synthetic control-network change identifies affected dependencies, scenarios, safeguards, controls, findings, UNKNOWN, gates, score and reports. |
| Report restraint     | Executive and technical examples do not exceed the approved decision.                                                                                |
| Integration boundary | AIDCF and AITG decisions remain separate and federated.                                                                                              |
| Anti-gaming design   | Fixtures address UNKNOWN-to-N/A conversion, evidence duplication, gate averaging, dependency omission and unsupported closure.                       |

# Corrected conformance statement

**This wording replaces any stronger self-declared conformance status until executable evidence is available.**

| **Field**            | **Validated statement**                                                                                      |
|----------------------|--------------------------------------------------------------------------------------------------------------|
| Overall status       | CONDITIONALLY VALIDATED AS A SYNTHETIC PILOT SPECIFICATION.                                                  |
| Semantic conformance | Substantially aligned with AIDCF-003 through AIDCF-014, subject to listed gaps.                              |
| Machine conformance  | NOT YET DEMONSTRATED.                                                                                        |
| Decision conformance | The synthetic LIMITED decision is coherent with the stated UNKNOWN and gate results.                         |
| Change demonstration | Conceptually complete; engine execution not demonstrated.                                                    |
| Permitted claim      | AIDCF-015 provides a comprehensive synthetic worked example and implementation specification.                |
| Prohibited claim     | AIDCF-015 is not yet a functioning machine-executable conformance implementation and is not a certification. |

# Mandatory closure plan

**Complete these gates before declaring the pilot executable.**

| **Priority** | **Closure action**                                       | **Evidence of closure**                                        |
|--------------|----------------------------------------------------------|----------------------------------------------------------------|
| P0           | Resolve AIDCF-007 baseline and canonical IDs.            | Approved manifest, corrected artifact and migration record.    |
| P0           | Create the full machine package.                         | Schemas, JSON-LD, TTL/OWL, SHACL, CSV registries and dataset.  |
| P0           | Instantiate assertion-specific evidence and trace edges. | Evidence manifest, hashes and forward/reverse link validation. |
| P0           | Execute positive, negative and anti-gaming fixtures.     | Versioned validator output with pass/fail results.             |
| P0           | Execute graph load and canonical queries.                | Load report and query result pack.                             |
| P0           | Reperform scoring deterministically.                     | Configuration, inputs, calculation and result hash.            |
| P1           | Complete AIDCF-011 program governance records.           | Charter, plan, competence, independence and review.            |
| P1           | Issue AIDCF-012 controlled reports/statements.           | IDs, approvals, validity, classification and supersession.     |
| P1           | Run change event through implemented impact engine.      | Before/after snapshots and reviewed impact output.             |
| P1           | Independent rerun.                                       | Signed independent conformance report.                         |

# Release decision

**The pilot should remain in controlled review.**

| **Decision element**   | **Disposition**                                                                                   |
|------------------------|---------------------------------------------------------------------------------------------------|
| Release recommendation | Do not publish as a completed executable reference implementation yet.                            |
| Current permitted use  | Internal methodology review, schema design, implementation backlog and stakeholder demonstration. |
| Current restriction    | No external conformance, certification, facility assurance or full-control coverage claim.        |
| Next release candidate | AIDCF-015 v1.1 after P0 closure and independent runner evidence.                                  |
| Go/no-go gate          | Go only when NC-01 through NC-05 are closed and NC-06/07 have approved plans.                     |
| Final conclusion       | CONDITIONALLY VALIDATED; MATERIAL REMEDIATION REQUIRED FOR EXECUTABLE CONFORMANCE.                |

## Final validation doctrine

**The AIDCF-015 pilot is a strong narrative and methodological proof, but the distinction between a specification and an executed implementation is material. The pilot must not claim machine conformance merely because it defines the files, tests and queries that a conformant implementation should contain. Executable conformance requires the actual artifacts, successful validation runs, preserved outputs and independent review.**
