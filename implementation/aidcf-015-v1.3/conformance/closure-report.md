# AIDCF-015 v1.3 closure report

| Field | Value |
|---|---|
| Release | AIDCF-REL-2026.10.1 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Evidence | `tools/run_all.py` output in `outputs/` (regenerated on every run; not covered by the manifest) |

All results below are self-validation by the package author's tooling. No independent execution has taken place.

## Defects in v1.2 and how v1.3 addresses them

| v1.2 defect | v1.3 position | Verified by |
|---|---|---|
| Turtle core was a stub; no OWL ontology | OWL 2 ontology with 58 classes, 41 object properties and their inverses, SKOS concept schemes for every vocabulary | SYNTAX, VOCABULARY |
| JSON-LD context had no `@vocab` | Protected context with `@vocab` and typed terms | SYNTAX (JSON-LD expansion of every dataset file) |
| `run_all` validated the ontology, not the data | SHACL runs over the dataset with the ontology as the ontology graph | SHACL |
| Tests were never executed | 58 fixtures (8 valid, 24 invalid, 26 business) and 2 legacy fixtures executed; each negative fixture must fail for its stated reason | FIXTURE |
| Static graph-query output | 14 SPARQL queries executed and compared with hand-derived expected results | GRAPH_QUERY |
| RDF parse failure not counted | Parse failures are counted failures; two negative syntax fixtures prove it | SYNTAX, FIXTURE |
| `additionalProperties: true`, no envelope | Closed schemas with the AIDCF-016 envelope | SCHEMA |
| Gates PASS on PARTIAL CRITICAL controls (CG-03, CG-06, CG-07, CG-13, CG-15); CG-02 PASS on 1 of 72 | Registry roles and the SPEC 6.2 roll-up: CG-03, CG-07 and CG-15 FAIL; CG-06 UNKNOWN; CG-02 and CG-13 NOT_ASSESSED | BUSINESS_RULE (MDM-R01, MDM-R02), SHACL, GRAPH_QUERY Q14 |
| `run_all` overwrote outputs and broke the manifest | `outputs/` is excluded from the manifest; the tool writes nowhere else | MANIFEST |
| Nothing signed | Still not signed: signatureStatus PENDING, approvals PENDING, stated in known issues | MANIFEST (MAN-06, MAN-07) |

## Open items

- Independent T7 execution and signed conformance result (AIDCF-VR-001 NC-09).
- Manifest signature and release approvals.
- Programme competence and independence records for real people (NC-06) and a controlled report issue (NC-07).
- Assessed: 12 of 360 controls (3.3333%). Coverage: 11 of 360 scored (3.0556%); MCF-RES-017 is UNKNOWN.
