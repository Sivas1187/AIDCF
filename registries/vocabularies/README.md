# Controlled vocabularies

These CSV files are the **canonical machine-readable controlled vocabularies of AIDCF**. They encode Part VI of AIDCF-002 Core Conceptual Model (`foundations/conceptual-model/AIDCF-002_Core_Conceptual_Model_v1.0.md`). The CSV files and AIDCF-002 Part VI must stay identical in content; a change to one requires the same change to the other in the same release (CCM-REQ-023).

All artifacts, datasets and tools use these codes. Legacy codes are accepted on ingest only through the alias files, stored in canonical form, and the legacy value kept as provenance (CCM-REQ-003).

Format: UTF-8, comma-separated, one header row, RFC 4180 quoting. Where a cell holds several values they are separated by `|`. An empty cell means "no value" (for example, UNKNOWN has no score value).

## Files

| **File** | **Columns** | **Content** | **AIDCF-002 section** |
|---|---|---|---|
| `claim-types.csv` | code, name, meaning, minimumAssuranceLevel | The five claim types a Control Assessment can assert | 24 |
| `assurance-levels.csv` | code, name, permittedConclusion, highestClaimTypes, usableAsRequiredAssuranceLevel, legacyAlias | Programme depth AL0–AL6; only AL2–AL5 are valid as a control's Required Assurance Level; legacy A2–A5 map 1:1 | 25 |
| `control-results.csv` | code, meaning, scoreValue, countsInCoverage | Canonical control results and their score and coverage treatment | 26 |
| `control-result-aliases.csv` | legacyCode, canonicalCode, condition | Legacy control results (NOT_IMPLEMENTED, IMPLEMENTED, OPERATING_EFFECTIVELY, N/A, SUSPENDED and so on) and the condition under which each maps | 26 |
| `gate-results.csv` | code, meaning | Gate results; there is no conditional gate state | 27 |
| `decision-states.csv` | code, meaning | The five decision states | 28.1 |
| `decision-lifecycle.csv` | code, meaning, reliancePermitted | Decision record lifecycle; only ACTIVE permits reliance | 28.2 |
| `decision-aliases.csv` | legacyCode, canonicalCode, field, note | Legacy decision codes (ADVERSE, UNKNOWN_INCONCLUSIVE, CONDITIONAL and so on); `field` says whether the alias maps to the decision state or the lifecycle | 28.3 |
| `confidence.csv` | code, name, kind, meaning | CONF-0 to CONF-4 (kind `level`) and the flags CONFLICTING and STALE (kind `flag`) | 29 |
| `evidence-classes.csv` | code, name, primaryClaimSupported, representativeSubtypes | Evidence classes E1–E7 | 30.1 |
| `quality-dimensions.csv` | code, name, question, scale | The six evidence-quality dimensions P F C R T I, each rated 0–5 per assertion | 30.2 |
| `evidence-quality-bands.csv` | code, name, rule, permittedUse, legacyEvidenceGrade | Quality bands Q0–Q5; legacyEvidenceGrade gives the superseded AIDCF-005/006 evidence grade E0–E5 | 30.2 |
| `sufficiency-levels.csv` | code, name, meaning | Evidence-package sufficiency S0–S5 | 30.2 |
| `integrity-levels.csv` | code, name, anchor | Evidence integrity I0–I5 | 30.2 |
| `evidence-system-conformance-levels.csv` | code, name, minimumExpectation, legacyCode | Evidence-system conformance EC0–EC5 (formerly E0–E5 in AIDCF-008 §4) | 30.3 |
| `control-profile-tiers.csv` | code, name, use, minimumEvidencePattern | Control evidence profile tiers CP-1 to CP-5 | 30.3 |
| `unknown-types.csv` | code, name, definition | UNKNOWN types U1–U10 (why something is unknown) | 31.1 |
| `unknown-severity.csv` | code, name, testOrder, test, decisionEffect, legacyLabel | UNKNOWN severity US1–US5; apply tests in `testOrder` and take the first that applies | 31.2 |
| `operating-states.csv` | code, definition | Canonical operating states, including SHUTDOWN and FAILED | 32 |
| `assessment-methods.csv` | code, meaning | The ten assessment methods | 33.1 |
| `control-types.csv` | code, meaning | Control types; each control has one primary type | 33.2 |
| `lifecycle-stages.csv` | code, meaning, legacyStages | Lifecycle stages PLAN to DECOMMISSION, with the AIDCF-003 §17 stages they replace | 33.3 |
| `score-bands.csv` | code, name, lowerBoundInclusive, upperBoundExclusive, reportingCondition | Score bands B1–B5 (B5 has no upper bound and includes 100) and the presentation code WITHHELD, used for "Band withheld (coverage/UNKNOWN)" | 33.4 |
| `implementation-maturity.csv` | code, name, definition, typicalEvidence | Implementation Maturity IM0–IM5. Diagnostic only, never a control result, score input or gate input (AIDCF-017) | 26, AIDCF-017 §5 |
| `relationship-aliases.csv` | legacyType, canonicalType, directionRule, note | Legacy relationship types and how they map to the 41 canonical AIDCF-014 §9 relationship types | 34 |

## Related registries

- `registries/states/states.csv` lists the gate, control, decision-state and decision-lifecycle codes as `type,value` pairs, for tools that need a flat list. It carries the same codes as `gate-results.csv`, `control-results.csv`, `decision-states.csv` and `decision-lifecycle.csv`.
- `registries/gates/critical-gates.csv` holds the fifteen Critical Gates. Gate names, scopes and evidence floors are in AIDCF-002 Section 35.1. Criteria and ceilings are in AIDCF-010.
- The 41 canonical relationship types and 48 object classes are defined in AIDCF-014 §9 and §7.

## Ambiguous level codes

Some letters are used by more than one AIDCF scale (for example `I3` can be an integrity level or an AIDCF-005 integration conformance level). AIDCF-002 Part VIII gives the full ladders crosswalk. Where a code could be read either way, write it with the owning artifact's short code (CCM-REQ-031).
