# AIDCF-016 schema set (MDM 1.3)

Normative serialisation package of AIDCF-016 Machine-Executable Data Model Standard, release 1.3 (Draft for controlled review, 2026-10-10). Every file in this directory except `tools/` is generated from one model, `tools/aidcf_model.py`, by `tools/build_schemas.py`; do not edit generated files by hand.

| Path | Content |
|---|---|
| `json-schema/` | JSON Schema 2020-12. `definitions.schema.json` (IRI, date and code definitions, one enum per vocabulary, nested objects), `common-envelope.schema.json` (AIDCF-014 section 8 envelope) and one closed schema (`additionalProperties: false`) per class: the 48 AIDCF-014 section 7 classes, the reference classes Location, PartyEntity and Component, the supporting classes IACS, IACSZone, Conduit, SecurityLevel, FoundationalRequirement and Assertion (pending AIDCF-014 registration), and the auxiliary RelationshipRecord. Each schema carries `x-aidcf-class`, `x-aidcf-semantic-owner` and `x-aidcf-registration`. |
| `jsonld/aidcf-context-1.3.jsonld` | JSON-LD 1.1 context: `@protected`, `@vocab` set to the ontology namespace, references typed `@id`, ordered lists as `@list`, extension data as `@json`. |
| `owl/aidcf-core-1.3.ttl` | OWL 2 ontology (Turtle), version IRI `https://w3id.org/aidcf/ontology/1.3`. See `owl/README.md`. |
| `shacl/aidcf-shapes-1.3.ttl` | SHACL shapes: envelope, class profiles, nested objects, the domain, range and cardinality of all 41 relationships, inverse-property prohibition and SHACL-SPARQL rule shapes named by rule ID (AIDCF-014 BR-NNN, TR-NN; AIDCF-016 MDM-RNN). |
| `tools/aidcf_model.py` | The model: namespaces, vocabularies (hard-coded schemes plus the codes read from `registries/vocabularies/*.csv`), classes, relationships, properties, profiles and the gate-ceiling derivation rule. |
| `tools/build_schemas.py` | Generator. `python3 -B schemas/tools/build_schemas.py` writes the files; `--check` exits 1 if any generated file is out of date. |

Namespace `https://w3id.org/aidcf/ontology#` (prefix `aidcf:`). Schema `$id` base `https://w3id.org/aidcf/schema/1.3/`. Registration of the `w3id.org/aidcf` redirect is pending; until it is confirmed these IRIs are identifiers only and do not resolve.

The reference package `implementation/aidcf-015-v1.3/` carries an unmodified copy of this set (made by its `tools/build_registries.py`) and validates its dataset against it with `tools/run_all.py`. The v1.2 schema files formerly held here are superseded; the v1.2 package keeps its own copies under `implementation/aidcf-015-v1.2/`.
