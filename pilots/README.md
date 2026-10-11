# pilots

AIDCF mini-pilot pack: what a host, an assessment team and a research lead need to run one small, authorised AIDCF assessment of a bounded AI Capability Instance and feed the results back into the framework.

**Status: pack ready; no authorised pilot has taken place.** Nothing in this folder records a pilot, a host, a sponsor, an approval or a result. Unsigned templates and generated lists are not evidence of an authorised pilot (README "Pilot programme"; GOVERNANCE.md §15). Whitepaper §29 status PILOT-001: NOT AUTHORISED / NOT EXECUTED.

## Contents

| Folder | Document or file | Purpose |
|---|---|---|
| [pilot-framework/](pilot-framework/) | [AIDCF-PIL-001 Mini-Pilot Protocol](pilot-framework/AIDCF-PIL-001_Mini-Pilot_Protocol_v1.0.md) | Objectives, eligible hosts, scope, AL3 target, Starter Profile, gates in scope and reachable decision, phases and effort assumptions, roles, evidence handling, research measures, exit criteria, publication and feedback. |
| | [starter-profile.csv](pilot-framework/starter-profile.csv) | 58 controls selected from the AIDCF-007A registry by a documented rule (generated). |
| | [tools/build_starter_profile.py](pilot-framework/tools/build_starter_profile.py) | Generator for the three generated CSV files; standard library only; `--check` mode. |
| [pilot-authorisation/](pilot-authorisation/) | [AIDCF-PIL-002 Pilot Authorisation Template](pilot-authorisation/AIDCF-PIL-002_Pilot_Authorisation_Template_v1.0.md) | Sponsor, scope, decision question, rules of engagement, safety sign-off, classification, retention, publication, conflicts, reviewer appointment, signatures. Must be reviewed by the host's legal adviser. |
| | [AIDCF-PIL-003 Evidence Request List Template](pilot-authorisation/AIDCF-PIL-003_Evidence_Request_List_Template_v1.0.md) and [evidence-request-list.csv](pilot-authorisation/evidence-request-list.csv) | 274 evidence request rows derived from the Starter Profile, registry evidence profiles and gate criteria (generated). |
| [pilot-results/](pilot-results/) | [AIDCF-PIL-004 Pilot Result Record Template](pilot-results/AIDCF-PIL-004_Pilot_Result_Record_Template_v1.0.md) | Result record aligned with whitepaper §29.4 and AIDCF-012. |
| | [pilot-metrics-template.csv](pilot-results/pilot-metrics-template.csv) | Research measures PM-01 to PM-20. |
| | [control-claim-log-template.csv](pilot-results/control-claim-log-template.csv) | One row per mandatory control-claim (107 at AL3) for effort, evidence, results and agreement (generated). |
| [lessons-learned/](lessons-learned/) | [AIDCF-PIL-005 Lessons Learned Template](lessons-learned/AIDCF-PIL-005_Lessons_Learned_Template_v1.0.md) | Lessons register and change proposals in the GOVERNANCE.md §9 form. |

## Order of use

1. Read AIDCF-PIL-001 and confirm the host meets conditions C1–C10.
2. Complete and sign AIDCF-PIL-002 after legal review (SG0).
3. Profile, scope and plan (SG1, SG2); issue AIDCF-PIL-003.
4. Collect, assess, review and decide (SG3 to SG6) under AIDCF-009 Part A, AIDCF-010 and AIDCF-012.
5. Complete AIDCF-PIL-004, the metrics files and AIDCF-PIL-005 (SG7).
6. Publish only anonymised material the host has approved in writing.

## Regenerating

```text
python3 pilots/pilot-framework/tools/build_starter_profile.py --check
```

## What may be added here

Only records classified PUBLIC under SECURITY.md after written host approval: an anonymised result record, anonymised metrics, an anonymised lessons register and change proposals. Evidence, workpapers and identifiable results are never committed.
