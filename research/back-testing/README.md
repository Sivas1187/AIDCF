# Incident back-testing kit (AIDCF-VAL-001)

**Status: frame built and screened; nothing selected or coded yet.** The incident register holds 221 real candidates (140 eligible, 81 excluded), found and screened on 2026-10-11 by an AI research assistant (screener code C90). Human second checks are still pending. See [`run-log/run-log.md`](run-log/run-log.md) for the flow, the shortfalls and the open items before selection. The only rows in the coding sheet are two fictional training examples (`INC-EXAMPLE-01`). Nothing in this folder reports a back-testing result.

## What this is

A kit for retrospective validation without a pilot. It tests whether AIDCF controls, AIDCF-004 failure scenarios and the critical gates CG-01 to CG-15 would have identified, before the event, the conditions behind publicly reported data-centre, AI-infrastructure and cloud incidents.

Each incident is coded by two coders, at least one of them independent of the framework author. The coders work from the incident's pre-event timeline before they read its root-cause analysis. For each causal factor they judge whether the assessment criteria and evidence profile of the relevant controls would have surfaced it (DETECTED, PARTIALLY_DETECTED, NOT_DETECTED, NOT_ADDRESSED, INSUFFICIENT_INFORMATION). For each relevant gate they judge whether it would have returned FAIL, UNKNOWN or PASS.

The result is evidence of **content validity and detection coverage** for README research questions RQ2, RQ4, RQ5 and RQ8. It is **not** proof of assurance value; only authorised pilots can provide that.

## Files

| File | Purpose |
|---|---|
| [`AIDCF-VAL-001_Incident_Back-Testing_Protocol_v1.0.md`](AIDCF-VAL-001_Incident_Back-Testing_Protocol_v1.0.md) | The protocol: eligibility, sampling, hindsight controls, coding procedure, judgement scales, gap handling, agreement, metrics, threats, ethics |
| [`coding-sheet.csv`](coding-sheet.csv) | Coding dataset: header plus two FICTIONAL example rows (one CONTROL row, one GATE row) |
| [`coding-sheet-dictionary.csv`](coding-sheet-dictionary.csv) | Definition, allowed values and source of values for every coding-sheet column |
| [`incident-register.csv`](incident-register.csv) | Sampling frame and selection log: 221 screened candidates |
| [`run-log/`](run-log/run-log.md) | Run log (frame flow, shortfalls, open items) and the search log of 115 queries |
| [`backtest_check.py`](backtest_check.py) | Standard-library validator (`--check`), agreement statistics (`--agreement`), metrics (`--metrics`) and the list of valid scenario-family codes (`--list-families`) |

## How to run it, in order

Section numbers refer to the protocol.

1. **Appoint roles** (section 5): study lead, extractor, Coder A, Coder B and adjudicator. At least one coder must be independent of the framework author. Collect independence and conflict declarations and assign pseudonymous coder codes (C01...).
2. **Freeze the baseline** (step 0): record the repository commit hash, frame-freeze date and protocol version in a run log.
3. **Build the frame** (section 7.1): search source families S1–S4 and log every candidate in `incident-register.csv` as CANDIDATE.
4. **Screen** (section 6): set `detail_level`, `eligibility_status` and `exclusion_code`. A second person checks every EX-02 and EX-04 exclusion.
5. **Select** (section 7.2): use the seeded random draw within strata, observing the sub-quotas and operator caps. Mark incidents SELECTED or RESERVE and archive every source.
6. **Calibrate** (step 3): each coder codes three non-sample calibration incidents and `INC-EXAMPLE-01`.
7. **Prepare dossiers** (step 2, section 8): the extractor produces each pre-event dossier containing only the PRE and EVENT segments.
8. **Coding pass 1** (step 4): each coder independently identifies factors, first PRE_REVEAL from the dossier and then POST_REVEAL from the full sources, and locks each version with a SHA-256 hash.
9. **Consolidate factors** (step 5): the adjudicator produces CF-01, CF-02, ... and records the crosswalk.
10. **Coding pass 2** (step 6): each coder independently maps controls, records detection judgements and judges the relevant gates and gaps, then locks.
11. **Check agreement**: run `python3 research/back-testing/backtest_check.py --check`, then `--agreement`. Apply the κ decision rules in section 13.2.
12. **Reconcile** (section 13.3): produce RECONCILED rows and run `--check` again.
13. **Analyse** (section 14): run `--metrics` and the required sensitivity analyses.
14. **Report and feed back** (sections 16–17): legal review, then the results report. Raise each distinct gap as a finding against AIDCF-007A through the CONTRIBUTING/GOVERNANCE process. After a release, recode the affected incidents.

## Incident register guidance

`incident-register.csv` holds **real candidates only**: IDs `INC-001` upwards, assigned in the order candidates are logged. Never put fictional or example rows in it.

Do not add an incident unless a source has been retrieved and checked. The register must not be filled from memory, from secondary summaries or from lists of "famous outages": every entry is traced to the PRIMARY or REGULATOR source it cites. Log every candidate found by the search, including those later excluded, so the selection flow can be reported.

| Column | Content | Allowed values |
|---|---|---|
| `incident_id` | Register ID | `INC-NNN` |
| `neutral_descriptor` | Short factual label naming no cause, for example "Regional storage service disruption" | Free text |
| `operator_name_as_published` | Organisation name exactly as it appears in its own report or the regulator report | Free text |
| `operator_type` | As in the dictionary | `HYPERSCALE_CLOUD`, `COLOCATION`, `ENTERPRISE`, `AI_HPC_FACILITY`, `TELECOM_NETWORK`, `MANAGED_SERVICE`, `PUBLIC_SECTOR`, `OTHER` |
| `incident_date` | Date of the initiating event | `YYYY-MM-DD`; blank only with `DATE_UNRESOLVED` in `notes` (must be resolved before selection) |
| `failure_category` | Provisional sampling stratum, confirmed at coding | `POWER`, `COOLING`, `NETWORK_FABRIC`, `STORAGE`, `CONTROL_PLANE_OT`, `CHANGE_HUMAN`, `EXTERNAL_DEPENDENCY` |
| `tags` | Sub-quota tags, semicolon-separated | `HEAT_EVENT`, `LIQUID_COOLING`, `AI_HPC`, `FIRE`, `WATER_INGRESS`, `BATTERY`, `MULTI_SITE`, `REGULATOR_REPORT` |
| `primary_source_url` | Operator, provider or regulator report | URL |
| `primary_source_type` | Type of the primary source | `PRIMARY`, `REGULATOR` (`SECONDARY_PRESS` only on EXCLUDED rows) |
| `other_source_urls` | Further sources, semicolon-separated | URLs |
| `access_date` | Date the sources were last accessed | `YYYY-MM-DD` |
| `archive_refs` | Archive snapshot URL(s) of each source | URLs |
| `found_via` | Search source family and query reference from the run log | `S1`–`S4` plus query reference |
| `detail_level` | Protocol section 6.3 | `HIGH`, `MEDIUM`, `LOW` |
| `eligibility_status` | Screening and selection state | `CANDIDATE`, `ELIGIBLE`, `EXCLUDED`, `SELECTED`, `RESERVE`, `WITHDRAWN` |
| `exclusion_code` | Required if and only if EXCLUDED | `EX-01` to `EX-08` (protocol section 6.4) |
| `screened_by` | Screener coder code | `C01`... |
| `exclusion_checked_by` | Second checker for EX-02 and EX-04 | `C01`... |
| `stratum_draw_rank` | Position in the seeded within-stratum draw | Integer |
| `coder_a`, `coder_b`, `adjudicator` | Pseudonymous codes | `C01`... |
| `coding_status` | Progress | `NOT_STARTED`, `DOSSIER_READY`, `PASS1_LOCKED`, `FACTORS_CONSOLIDATED`, `PASS2_LOCKED`, `RECONCILED`, `QA_COMPLETE` |
| `notes` | Recusals (without reasons), conflicts between sources, withdrawal reasons | Free text |

## Validation

```text
python3 research/back-testing/backtest_check.py --check
```

The validator checks the column order of both CSV files and validates every code against the following files:

- AIDCF-004 v1.1: scenario families, X01–X20, FM-* failure modes, M-codes and cause families;
- `registries/controls/controls.csv`;
- the AIDCF-007A catalogue: assessment-criterion numbers;
- `registries/gates/`;
- the canonical vocabularies.

It also checks the consistency rules in protocol section 10, for example that DETECTED is never recorded with a CONFORMING result and that NOT_ADDRESSED carries a gap. It exits non-zero on any error. Only the Python standard library is used.
