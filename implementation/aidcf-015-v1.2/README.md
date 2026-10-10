# AIDCF-015 v1.2 Canonical Baseline Migration Package

Synthetic, non-production executable reference implementation migrated to the approved AIDCF-007A baseline of 15 domains, 90 families and 360 controls.

## Release status
CANONICAL_BASELINE_COMPLIANT_SYNTHETIC_REFERENCE_IMPLEMENTATION, subject to independent T7 review and the stated limitations.

## Key changes
- Replaced 12 live `PILOT-*` assessment references with canonical `MCF-*` identifiers.
- Included complete 15/90/360 CSV registries.
- Preserved each legacy ID in `migratedFrom` and in the migration matrix.
- Re-generated evidence mappings, gate results, score snapshot, decision and reports.
- Closed BI-001 and NC-01.
- Preserved limited, synthetic, non-certification scope.

## Run
`python tools/run_all.py`

## Important boundary
Only 12 representative controls are assessed. Coverage is 3.3333% of the canonical 360-control universe. This package does not claim full control coverage or assurance of a real facility.
