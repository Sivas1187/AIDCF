# AIDCF-015 changelog

## v1.4 (2026-10-13, AIDCF-REL-2026.10.2, Draft for controlled review)

- Seven failure scenarios, FS-06 to FS-12, instantiate AIDCF-004 Part XIV library scenarios X02 (CDU controller firmware fault), X03 (PFC storm), X04 (checkpoint storage saturation), X07 (coolant leak at a rack manifold), X08 (facility water contamination), X11 (concurrent maintenance) and X16 (alarm flood and operator mis-switching). They trace only through the case's existing systems, assets, functions and outcomes; no element, dependency or safeguard is added. Each scenario records its library source in `sourceRecord`.
- Initiators added for them: hazards HZ-03 (FLUID), HZ-04 (CHEMICAL) and HZ-05 (UTILITY_DISTURBANCE); failure modes FM-04 to FM-08.
- Scenarios may now start from a state other than NORMAL (FS-08 RECOVERY, FS-11 MAINTENANCE) and may affect more than one outcome (FS-07: SO-01 and SO-02).
- Q02 expected result updated: nine scenarios can defeat SO-01 (FS-01, FS-02, FS-05 to FS-07, FS-09 to FS-12). The old basis line named FS-01 to FS-05, although FS-03 and FS-04 never affected SO-01; it now states the rows.
- Erratum E-001 corrected: the decision question now says SO-01 to SO-03 are assessed as far as they apply in NORMAL and MAINTENANCE states, and that SO-02 (RECOVERY only) and the DEGRADED state of SO-03 are outside the assessed scope. FS-08 (pre-state RECOVERY) is a scenario model of SO-02, not an assessment of it.
- Gate results, score, coverage and the NOT_ASSURED decision are unchanged from v1.3.
- `implementation/aidcf-015-v1.3/` is unchanged as released.

## v1.3 (2026-10-10, AIDCF-REL-2026.10.1, Draft for controlled review)

- Rebuilt on the AIDCF-016 schema set (`schemas/`): common envelope, closed JSON Schemas for 58 classes (48 AIDCF-014 classes, 3 reference classes, 6 supporting classes pending registration, RelationshipRecord), JSON-LD 1.1 context with `@vocab` and protected terms, OWL 2 ontology, SHACL shapes. Replaces the v1.2 Turtle stub and `additionalProperties: true` schemas.
- Gate roles: per-control CRITICAL and SUPPORTING roles from `registries/controls/gate-mappings.csv`. The v1.2 synthetic gate-to-control lists and the baseline note about whole-domain gate lists are withdrawn.
- Gate results recomputed with the SPEC 6.2 roll-up over the 12 assessed controls, with every unassessed registry CRITICAL control carried as NOT_ASSESSED. Three gates FAIL on PARTIAL CRITICAL inputs (v1.2 recorded PASS for CG-03, CG-07 and CG-15); CG-02 is NOT_ASSESSED (v1.2 recorded PASS with one of 72 controls).
- Decision recomputed from gate ceilings and UNKNOWN severities: NOT_ASSURED (v1.2: LIMITED), controlled by the CG-07 FAIL ceiling. Decision ranks follow AIDCF-010 (REASONABLY_ASSURED > CONDITIONALLY_ASSURED > LIMITED > INCONCLUSIVE > NOT_ASSURED). An earlier v1.3 build ranked NOT_ASSURED and INCONCLUSIVE equal and broke the tie to INCONCLUSIVE, reporting INCONCLUSIVE; that tie-break is removed from `schemas/tools/aidcf_model.py` (DECISION_RANK, `derive_ceiling`), the SHACL rank expressions in `schemas/tools/build_schemas.py` and `tools/aidcf_rules.py` (`decision_ceiling`). The derived gate ceilings are unchanged. Dataset statement, prohibited claims, recommendation limitations, Q06/Q07 expected results and fixtures I-SHA-007, B-004 and B-012 updated; business fixture B-026 added (a FAIL with a NOT_ASSURED ceiling is not raised to INCONCLUSIVE by a US5 UNKNOWN).
- Coverage reported as scored / (in scope − NOT_APPLICABLE) = 11/360 = 3.0556% (12 assessed, 11 scored, 1 UNKNOWN).
- MCF-RES-017 re-evaluated as UNKNOWN: evidence below the S3 floor and no E4 evidence (v1.2: PARTIAL).
- Every edge carries a RelationshipRecord; inverse properties are never asserted.
- Full chain instantiated: capability, outcomes, functions, architecture snapshot, systems, assets, IACS zones and conduit, dependencies, fault domains, failure scenarios, safeguards, controls, evidence requirements, evidence objects with hashed fixtures, assessments, findings, UNKNOWN records, gates, score, recommendation, decision, statement, report, actions, trigger, event, handoff, migrations and baseline issues.
- `tools/run_all.py` executes 13 layers (REGISTRY, SYNTAX, SCHEMA, SHACL, BUSINESS_RULE, TRACEABILITY, GRAPH_QUERY, SCORE, INTEGRITY, MANIFEST, VOCABULARY, EXPORT, FIXTURE), counts checks and failures per layer, exits 1 on any failure and writes only to `outputs/`.
- Release manifest lists every package file except `outputs/` and itself, with an RFC 8785 digest; signature and approvals PENDING.
- Restored the v1.1 schemas and tests under `legacy/v1.1/` and run them as regression fixtures.
- Requirements pinned in `requirements.txt`.

## v1.2

- Adopted AIDCF-007A-AMD-001.
- Added full canonical domain, family and control registries.
- Migrated all live pilot-control references to canonical MCF identifiers.
- Added auditable PILOT-to-MCF migration matrix.
- Rebuilt evidence, assessments, gates, score, decision, reports and events.
- Added canonical-ID rejection tests, coverage anti-gaming test and deterministic score re-performance.
- Closed BI-001 and NC-01; retained independent T7 review as open.
