# AIDCF-016 Machine-Executable Data Model Standard

| Field | Value |
|---|---|
| Public ID | AIDCF-016 (short code MDM) |
| Document | [AIDCF-016_Machine-Executable_Data_Model_Standard_v1.0.md](AIDCF-016_Machine-Executable_Data_Model_Standard_v1.0.md) |
| Version | 1.0 (schema set MDM 1.3) |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |

AIDCF-016 is the normative serialisation companion of AIDCF-014 (TDS-REQ-045). It defines how AIDCF records are serialised (JSON, JSON Schema 2020-12, JSON-LD 1.1, RDF/Turtle, OWL 2, SHACL, CSV registries), the namespace and identifier policy, the record envelope, the 48 canonical classes plus reference and supporting classes, the 41 relationships and relationship records, and the canonical decision rules every implementation must compute in the same way: gate roll-up, scope and NOT_ASSESSED, ceiling derivation, decision ceiling, score and change impact. It also defines the validation layers, the conformance classes MDM-C1 to MDM-C5 with their test catalogue, the release-manifest profile, and versioning and migration.

The identifier AIDCF-016 was previously used by mistake for the full-stack validation report. That report is now AIDCF-VR-001 and lives in `validation/validation-report/`.

## Related locations

| Path | Content |
|---|---|
| `schemas/` | The MDM 1.3 schema set, generated from `schemas/tools/aidcf_model.py` by `schemas/tools/build_schemas.py` |
| `implementation/aidcf-015-v1.3/` | AIDCF-015 v1.3 reference implementation. Its `tools/aidcf_rules.py` executes the rules of this standard. |
| `.github/workflows/ci.yml` | Regenerates and checks the schema set, then runs the v1.3 validation |

Conformance to AIDCF-016 is technical conformance of data. It is not engineering approval, assurance or certification. The AIDCF-015 v1.3 run is self-validation with an unsigned manifest.
