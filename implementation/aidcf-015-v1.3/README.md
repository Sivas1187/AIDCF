# AIDCF-015 v1.3 reference package

| Field | Value |
|---|---|
| Artifact | AIDCF-015 Reference Implementation, Synthetic Dataset and Conformance Pilot |
| Package version | 1.3 |
| Release identifier | AIDCF-REL-2026.10.1 |
| Data model | AIDCF-016 Machine-Executable Data Model Standard (MDM 1.3 schema set) |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Supersedes | `implementation/aidcf-015-v1.2/` (retained unchanged for comparison) |

This package is a synthetic, non-production reference implementation of AIDCF-014 and AIDCF-016. It describes no real facility, organisation or person. It is not an assurance conclusion, an engineering approval or a certification.

## What the package demonstrates

1. Every record uses the AIDCF-016 envelope and validates against closed JSON Schemas (2020-12) generated from one model (`schemas/tools/aidcf_model.py`).
2. The dataset expands as JSON-LD 1.1 and conforms to the AIDCF-016 SHACL shapes, with the OWL 2 ontology mixed in as the ontology graph.
3. Gate results follow the SPEC 6.2 roll-up using the per-control CRITICAL and SUPPORTING roles in `registries/controls/gate-mappings.csv`. They are not hand-entered: `tools/build_dataset.py` stops if its declared table differs from the rule engine (`tools/aidcf_rules.py`), and `tools/run_all.py` recomputes every gate independently.
4. Three gates FAIL because CRITICAL inputs are PARTIAL (PARTIAL never yields PASS). The CG-07 FAIL ceiling, NOT_ASSURED, controls the decision. Decision states are ranked as in AIDCF-010 (REASONABLY_ASSURED > CONDITIONALLY_ASSURED > LIMITED > INCONCLUSIVE > NOT_ASSURED), so the INCONCLUSIVE ceilings of the US5 UNKNOWN, the CG-01 UNKNOWN and the CG-05 UNKNOWN do not raise a demonstrated gate failure to INCONCLUSIVE. Fixture B-026 proves this.
5. The score is reperformed from pinned inputs; the band is WITHHELD.
6. Negative fixtures fail at the stated layer for the stated reason, and business fixtures are rejected by the stated rule.
7. The release manifest hashes every package file except `outputs/`. Running the validator never invalidates the manifest.

## Run

```
python3 -m pip install -r requirements.txt
python3 -B tools/run_all.py            # all layers, including fixtures (about 4 minutes)
python3 -B tools/run_all.py --skip-fixtures
```

`run_all.py` exits 1 if any check in any layer fails. It writes only to `outputs/`.

To rebuild after changing the model, registries or dataset design, run in this order:

```
python3 -B ../../schemas/tools/build_schemas.py      # repository schema set (AIDCF-016)
python3 -B tools/build_registries.py                  # copy registries and schemas into the package
python3 -B tools/build_dataset.py                     # dataset/*.jsonld and evidence-fixtures/
python3 -B tools/build_fixtures.py                    # tests/valid, tests/invalid, tests/business
python3 -B tools/build_manifest.py                    # baseline/release-manifest.json (last)
python3 -B tools/run_all.py
```

## Validation layers

| Layer | What is executed |
|---|---|
| REGISTRY | 15 domains, 90 families, 360 unique controls; one evidence profile per control with matching claim type; `gate-mappings.csv` agrees with the gate columns of `controls.csv`; copied registry files match their source hashes. |
| SYNTAX | Every JSON file parses; every Turtle file parses; every dataset file expands as JSON-LD. A parse failure is a counted failure. |
| SCHEMA | Every schema is checked against the 2020-12 metaschema; every record and the manifest validate against their class schema (`additionalProperties: false`). |
| SHACL | pyshacl over the full dataset with the OWL ontology mixed in (no inference): domain, range, cardinality, vocabulary and SHACL-SPARQL rule shapes. |
| BUSINESS_RULE | AIDCF-014 BR-001 to BR-015 and AIDCF-016 MDM-R01 to MDM-R20 in Python, including recomputation of every gate and of the decision ceiling. |
| TRACEABILITY | AIDCF-014 TR-01 to TR-18. |
| GRAPH_QUERY | SPARQL queries Q01 to Q12 (the AIDCF-014 section 19 questions) and Q13 to Q14, each compared with a hand-derived expected result in `queries/expected/`. |
| SCORE | SPEC 5.12 reperformance: coverage, mean, band, domain scores, UNKNOWN overlay and calculation hash. |
| INTEGRITY | SHA-256 and size of every evidence fixture; evidence-package digest; no orphan fixtures. |
| MANIFEST | Every listed file matches its hash and size; every package file is listed except `outputs/`; record `releaseRef` equals the manifest `releaseId`; RFC 8785 digest; no signature or approval is claimed. |
| VOCABULARY | OWL SKOS concepts and JSON Schema enums equal the `registries/vocabularies/*.csv` codes; alias tables map to canonical codes. |
| EXPORT | AIDCF-014 CT-09: an INTERNAL export withholds every record and edge above INTERNAL. |
| FIXTURE | Every fixture in `tests/` and the restored v1.1 fixtures in `legacy/v1.1/tests/`. |

Counts per layer from the latest run are in `outputs/validation-results.json`; failures and warnings are in `outputs/validation-failures.json`; ValidationResult records are in `outputs/validation-results.jsonld`.

## Dataset

| Area | Content |
|---|---|
| Control framework | 15 ControlDomain, 90 ControlFamily, 360 Control, 15 CriticalGate and 375 EvidenceRequirement records imported from the AIDCF-007A v1.1 registry copy, with every Control-to-gate edge carrying its registry role. |
| Capability | CI-001, three Service Outcomes and six Required Functions (all values illustrative). |
| Architecture | Snapshot SNAP-001; seven systems (including an IACS with two IACS zones and a conduit); twelve assets; seventeen Dependency records; two fault domains; capacity assertions with supersession; SL-T and SL-C security levels. |
| Failure | One threat, two hazards, three failure modes, five failure scenarios with ordered propagation steps, seven safeguards governed by registry controls. |
| Assessment | Twelve Control Assessments (6 CONFORMING, 5 PARTIAL, 1 UNKNOWN), each with its procedure, evidence and review; six Findings; five UNKNOWN Records (US2, US3, US4, US4, US5). |
| Decision | Fifteen Gate Results, one Score Snapshot, one Decision Recommendation, one Assurance Decision (NOT_ASSURED), one statement and one report. |
| Continuing assurance | One pending CONFIGURATION_CHANGED event with candidate reassessment edges computed by the AIDCF-014 section 22 impact rule, two migration records and three baseline issues. |
| Relationships | Every asserted edge has a RelationshipRecord carrying the AIDCF-014 section 10 envelope and qualifiers; all 41 AIDCF-014 relationship types occur. |

### Gate results

| Gate | State | Reason |
|---|---|---|
| CG-01 | UNKNOWN | MCF-CAP-001 CONFORMING; 6 of 7 registry CRITICAL controls NOT_ASSESSED |
| CG-02 | NOT_ASSESSED | No CRITICAL control assessed, no criterion evaluated |
| CG-03 | FAIL | CRITICAL MCF-DEP-001 PARTIAL; GC-03-1 NOT_MET; U-003 (US5) attached |
| CG-04 | NOT_ASSESSED | As CG-02 |
| CG-05 | UNKNOWN | MCF-POW-001 CONFORMING; 7 of 8 CRITICAL controls NOT_ASSESSED |
| CG-06 | UNKNOWN | U-003 (US5) attached; no CRITICAL control assessed |
| CG-07 | FAIL | CRITICAL MCF-OPS-013 and MCF-SEC-005 PARTIAL; GC-07-6 NOT_MET; U-005 (US4) attached |
| CG-08 | UNKNOWN | MCF-STO-017 and MCF-NET-001 CONFORMING; 10 of 12 CRITICAL controls NOT_ASSESSED |
| CG-09 | NOT_ASSESSED | As CG-02 |
| CG-10 | UNKNOWN | U-004 (US4) on GC-10-5 |
| CG-11 | NOT_ASSESSED | Meta-gate; no criterion evaluated |
| CG-12 | NOT_ASSESSED | Meta-gate; no criterion evaluated |
| CG-13 | NOT_ASSESSED | Only a SUPPORTING input (MCF-SUP-021) was assessed |
| CG-14 | NOT_ASSESSED | As CG-02 |
| CG-15 | FAIL | CRITICAL MCF-SUP-021 PARTIAL; GC-15-4 NOT_MET |

Decision ceiling: NOT_ASSURED, controlled by the CG-07 FAIL (failCeiling NOT_ASSURED). Ceilings above it, which do not control: CG-01 UNKNOWN, CG-05 UNKNOWN and U-003 (US5), each INCONCLUSIVE; CG-03 FAIL and CG-15 FAIL, each LIMITED for the decision as a whole (their registry text also sets NOT_ASSURED for the outcomes reached by the defeated dependency or authority path); the remaining UNKNOWN and NOT_ASSESSED gates and U-004 and U-005 (US4), LIMITED; U-001 (US3), CONDITIONALLY_ASSURED. The decision question is not partitioned by outcome, so the ceiling applies to SO-01 to SO-03.

Score: 12 of 360 controls assessed (3.3333%), 11 scored and 1 UNKNOWN; coverage = scored / (in scope − NOT_APPLICABLE) = 11/360 = 3.0556%; mean 77.2727; band WITHHELD.

## Layout

| Path | Content |
|---|---|
| `registries/` | Unmodified copies of the repository registries and vocabularies (`registry-sources.json` records the hashes). |
| `schemas/` | Copy of the repository AIDCF-016 schema set (JSON Schema, JSON-LD context, OWL, SHACL). |
| `dataset/` | Synthetic records (JSON-LD, one `@graph` per file). |
| `evidence-fixtures/` | Synthetic evidence files hashed by the EvidenceObject records. |
| `queries/` | SPARQL queries and expected results. |
| `tests/` | `valid/`, `invalid/` and `business/` fixtures. |
| `legacy/v1.1/` | The v1.1 schemas and tests restored from `archive/historical-releases/AIDCF-015_v1.1_Executable_Reference_Implementation.zip`, executed as regression fixtures. |
| `migration/` | v1.1 to v1.2 migration matrix and plan (inputs to MIG-001). |
| `governance/` | Programme charter. |
| `baseline/` | Release manifest, known issues, baseline declaration. |
| `conformance/` | Closure report against the AIDCF-VR-001 findings. |
| `outputs/` | Validation outputs (excluded from the manifest; regenerated on every run). |
| `tools/` | Builders, rule engine and validator. |

## Limitations

See `baseline/known-issues.json`. In brief: self-validation only, with no independent execution; the manifest is not signed and no approval is recorded; synthetic data only; 12 of 360 controls assessed, coverage 11/360 (3.0556%); the review and approval records in the dataset are synthetic and record no human act.
