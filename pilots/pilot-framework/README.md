# pilot-framework

**Status: pack ready; no authorised pilot has taken place.**

| File | Purpose |
|---|---|
| [AIDCF-PIL-001_Mini-Pilot_Protocol_v1.0.md](AIDCF-PIL-001_Mini-Pilot_Protocol_v1.0.md) | The mini-pilot protocol (PIL-REQ-001 to PIL-REQ-016). |
| [starter-profile.csv](starter-profile.csv) | Starter Profile: 58 controls, 107 mandatory control-claims at AL3. Generated; do not edit by hand. |
| [tools/build_starter_profile.py](tools/build_starter_profile.py) | Generator for `starter-profile.csv`, `../pilot-authorisation/evidence-request-list.csv` and `../pilot-results/control-claim-log-template.csv`. |

## Starter Profile rule (summary)

In-scope mapped gates: CG-01, CG-02, CG-03, CG-05, CG-06, CG-07, CG-10 (CG-11 and CG-12 are evaluated as meta-gates and select no controls).

- **R1**: every control with a CRITICAL mapping to an in-scope gate (50 controls), so each in-scope gate can be evaluated by the AIDCF-010 roll-up rule.
- **R2**: every CMP, STO or NET control not selected by R1 with a SUPPORTING mapping to CG-01, or SUPPORTING mappings to two or more in-scope gates (8 controls).

`mandatoryClaimTypesAtAL3` uses the AIDCF-010 Part IV rule L = min(T, r) with T = AL3. Columns and the reasoning, including why the profile is 58 controls rather than about 40 and why CG-02 is in scope, are in AIDCF-PIL-001 §6 and §7.

## Generator

```text
python3 pilots/pilot-framework/tools/build_starter_profile.py           # write
python3 pilots/pilot-framework/tools/build_starter_profile.py --check   # exit 1 if any output is stale
```

Standard library only; deterministic; reads `registries/controls/`, `registries/gates/`, `registries/domains/domains.csv` and `registries/vocabularies/claim-types.csv`; writes UTF-8 CSV with LF line endings. It fails if any CRITICAL control of an in-scope gate is not selected.
