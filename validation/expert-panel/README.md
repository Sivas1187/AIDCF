# expert-panel

| Field | Value |
|---|---|
| Document ID | AIDCF-VAL-002-R |
| Title | Expert Panel Content Validation Kit README |
| Version | 1.0 |
| Date | 2026-10-11 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |

Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-11 | First issue. |

**Study status: kit ready; no panel convened.** No participant has been recruited, no ratings exist and no results have been produced. The only response data in this folder is the SYNTHETIC self-test fixture.

This folder holds the instruments for a modified Delphi expert panel that judges the content validity of a stratified sample of 48 AIDCF controls and all 15 Critical Gates. It addresses RQ3 (control-universe validity) and RQ8 (critical-gate effectiveness, at the level of expert judgement) in the repository [README](../../README.md#research-questions).

## Contents

| File | ID | Purpose | Generated |
|---|---|---|---|
| [`AIDCF-VAL-002_Expert_Panel_Content_Validation_Protocol_v1.0.md`](AIDCF-VAL-002_Expert_Panel_Content_Validation_Protocol_v1.0.md) | AIDCF-VAL-002 | Protocol: panel, method, analysis, consensus and stopping rules, dispositions, ethics, threats to validity | No |
| [`round-1-questionnaire.md`](round-1-questionnaire.md) | AIDCF-VAL-002-A | Panellist instructions, scales with anchors, item and response layout | No |
| [`round-1-item-booklet.md`](round-1-item-booklet.md) | AIDCF-VAL-002-B | Item text reproduced from the registries | Yes |
| [`participant-information-and-consent.md`](participant-information-and-consent.md) | AIDCF-VAL-002-C | Template: information sheet, consent form, eligibility and conflict declaration (requires sponsor legal and data-protection review) | No |
| [`control-sample.csv`](control-sample.csv) | | 48 sampled controls with gate roles and selection reason | Yes |
| [`gate-sample.csv`](gate-sample.csv) | | 15 gates with criteria counts and CRITICAL-control counts | Yes |
| [`round-1-response-template.csv`](round-1-response-template.csv) | | One row per item (48 controls, 15 gates); rating cells empty, non-applicable cells `NA` | Yes |
| [`tools/build_sample.py`](tools/build_sample.py) | | Deterministic sample, template and booklet generator | |
| [`tools/analyse_round.py`](tools/analyse_round.py) | | I-CVI, modified kappa, S-CVI/Ave and S-CVI/UA, median and IQR, consensus flags | |
| [`tools/test-fixtures/SYNTHETIC_round-1-responses.csv`](tools/test-fixtures/SYNTHETIC_round-1-responses.csv) | | SYNTHETIC data for `--self-test` only; panellist codes `SYN-P*`, item IDs `MCF-SYN-*` and `CG-SYN` do not exist in the registries | |

## Commands

Run from the repository root. Python 3.8 or later, standard library only.

```sh
# regenerate sample, template and booklet from the registries
python3 validation/expert-panel/tools/build_sample.py
# verify generated files are current and sampling rules hold (CI-friendly; exit 1 on failure)
python3 validation/expert-panel/tools/build_sample.py --check
# verify analysis arithmetic against hand-computed values
python3 validation/expert-panel/tools/analyse_round.py --self-test
# analyse a round (one CSV per panellist)
python3 validation/expert-panel/tools/analyse_round.py responses/R1_*.csv \
    --out r1-item-results.csv --scale-out r1-scale-results.csv --comments-out r1-comments.csv
```

## Sampling summary

Controls are ranked by SHA-256 of `AIDCF-VAL-002-2026-10-11:<controlId>` (no pseudo-random generator), then selected by four rules: at least 2 CRITICAL controls for each of CG-01 to CG-10 and CG-13 to CG-15; at least 4 controls per claim type; at least 3 per domain (maximum 4); fill to 48 preferring CRITICAL-mapped controls. CG-11 and CG-12 carry no control mappings and are rated as gate items only. At issue the sample holds 54% CRITICAL-mapped controls against 29% in the catalogue. Full rules: protocol section 6 and the `build_sample.py` docstring.

## Where results will go

Round response files are not committed. After the final round, the anonymised analysis report and item results are published here, and disposition records go to `validation/reviewer-dispositions/`.
