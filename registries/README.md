# Registries

Machine-readable AIDCF registries as CSV (and JSON for controls). They are generated from `controls/controls.json` (the full v1.1 control definitions) by [`tools/build_registry.py`](tools/build_registry.py), which also writes the v1.1 workbook; `tools/build_catalogue_md.py` renders the per-domain control catalogues and `tools/build_catalogue.py` the AIDCF-014 §17 registry catalogue in [`catalogue/`](catalogue/README.md).

| Folder | File | Rows | Content |
|---|---|---|---|
| `domains/` | `domains.csv` | 15 | Control domains, with the gates each domain contributes to |
| `families/` | `control-families.csv` | 90 | Control families, six per domain |
| `controls/` | `controls.csv`, `controls.json` | 360 | Controls: title, objective, testable requirement, claim type, required assurance level, control type, profile tier, sufficiency floor, CRITICAL and SUPPORTING gates |
| `controls/` | `evidence-profiles.csv` | 360 | One evidence requirement profile per control (AIDCF-008 §31): required and optional evidence classes, quality and sufficiency floors, state and period coverage, independence, mandatory items, acceptable alternatives, UNKNOWN effect, reassessment triggers |
| `controls/` | `gate-mappings.csv` | 589 | Per-control gate mappings: 106 CRITICAL and 483 SUPPORTING |
| `controls/` | `parameters.csv` | 508 | Parameters referenced by control requirements: name, unit, illustrative default and basis. The assessed organisation sets the actual value in its capability profile |
| `gates/` | `critical-gates.csv` | 15 | Critical gates CG-01 to CG-15: name, scope, evidence floor, required evidence classes, FAIL and UNKNOWN decision ceilings, APPROVED_NA conditions, owning artifact |
| `gates/` | `critical-gate-criteria.csv` | 101 | Pass criteria for each gate |
| `states/` | `states.csv` | 24 | Gate results, control results, decision states and decision lifecycle states |
| `vocabularies/` | 25 CSV files | | Canonical controlled vocabularies and legacy aliases (see [vocabularies/README.md](vocabularies/README.md)) |
| `catalogue/` | 15 CSV files and an index | | AIDCF-014 §17 registries not held elsewhere (artifacts, object types, relationship types, external mappings and others), and `registry-index.csv` showing which registries still lack the §17 common columns |

## Status

The control, evidence-profile, gate-mapping, parameter and gate-criteria registries are **proposed** under amendment AIDCF-007A-AMD-002 (registry v1.1); each row carries the AIDCF-014 record status `CANDIDATE`. They replace the v1.0 placeholder requirement text, which used one template for all 360 controls, and the v1.0 whole-domain gate mapping. They are not approved until AMD-002 is ratified under GOVERNANCE.md.

The approved baseline remains `standards/aidcf-007a/registry/AIDCF-007A_Canonical_Master_Control_Registry_15-90-360_v1.0.xlsx`. Control IDs, family IDs and the 15/90/360 cardinality are the same in both versions.

The authoritative registry is the workbook `standards/aidcf-007a/registry/AIDCF-007A_Canonical_Master_Control_Registry_15-90-360_v1.1.xlsx`. If a CSV and the workbook ever differ, the workbook governs.

`implementation/aidcf-015-v1.2/registries/` is the earlier package's copy and is left unchanged as released. `implementation/aidcf-015-v1.3/registries/` is generated from these files.
