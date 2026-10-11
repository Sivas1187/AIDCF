**AIDCF**

# LESSONS LEARNED TEMPLATE

*AI Data Centre Facilities Assurance Framework: pilot pack*

Version 1.0

The register in which a mini-pilot records usability problems, framework defects and interpretation questions, and turns them into dispositioned change proposals

Artifact ID: AIDCF-PIL-005
Artifact type: Pilot record template
Status: Draft for controlled review
Author: Siva Sethumadhavan

> **Pilot status: pack ready; no authorised pilot has taken place.** This is a blank template. No lesson has been recorded from a real pilot.

# Document control

| **Field** | **Value** |
|---|---|
| Document ID | AIDCF-PIL-005 |
| Title | AIDCF Lessons Learned Template |
| Version | 1.0 |
| Date | 2026-10-11 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Used with | AIDCF-PIL-001 §12 (PM-13, PM-14, PM-15, PM-20) and §14.3; AIDCF-PIL-004 §10; GOVERNANCE.md §8 (change classes) and §9 (change proposal requirements); whitepaper §29.3 "Learn" phase |

## Revision history

| **Version** | **Date** | **Summary** |
|---|---|---|
| 1.0 | 2026-10-11 | First issue. |

---

# 1. Purpose and rules

The pilot is worth running only if what it teaches reaches the framework. This register captures every lesson as it arises, in every phase, not only at the end.

1. Record lessons when they occur. Anyone on the pilot team, the independent reviewer, the decision authority and host staff may raise one through the lead assessor or research lead.
2. Record facts observed in the pilot, not opinions about the framework in general. Link each lesson to the record where it arose (workpaper, request row, control-claim log row).
3. A lesson never changes a result, Gate Result or decision of the pilot. If a defect means a result was wrong under the standard as written, it is corrected through the normal review process; the lesson records the defect.
4. Every lesson in a DEFECT_ category or INTERPRETATION is dispositioned as a change proposal, a deferral with reason, or a rejection with reason (PIL-REQ-014).
5. The full register is **Confidential**. A public version is produced only under AIDCF-PIL-002 §12, with host-specific detail removed. Lessons are written so that they make sense without identifying the host: describe the method problem, not the site.

# 2. Categories

| **Category** | **Use for** | **Feeds** |
|---|---|---|
| USABILITY | The method, a template or a tool was hard to apply, slow, confusing or error-prone, without the underlying requirement being wrong. | PM-13 |
| DEFECT_CONTROL | A control requirement or objective is ambiguous, untestable, duplicated, mis-scoped or missing a necessary element. | PM-14 |
| DEFECT_CRITERION | A control assessment criterion or a gate criterion (GC-nn-n) is ambiguous, unmeasurable or inconsistent with its gate or claim depth. | PM-14 |
| DEFECT_PROFILE | An evidence profile element (classes, floors, coverage, period, independence, mandatory items, alternatives, unknownEffect, triggers) is infeasible, inconsistent or insufficient. | PM-14 |
| DEFECT_MAPPING | A control-to-gate mapping or role (CRITICAL / SUPPORTING) appears wrong or missing. | PM-14 |
| DEFECT_VOCABULARY | A canonical term or code is ambiguous, missing, or conflicts between artifacts. | PM-14 |
| DEFECT_TEMPLATE | A workpaper, report or pilot template lacks a needed field or has a wrong one. | PM-14 |
| ORPHAN_FINDING | A material finding had no suitable control in the registry. | PM-15 |
| INTERPRETATION | Applying the standards needed an interpretation not stated in them. | PM-20 |
| METHOD | A procedure step, sequence or stage gate did not fit practice. | PM-14 or PM-13 |
| LOGISTICS | Access, scheduling, evidence transfer or staffing affected the pilot. | PM-19 |
| SAFETY_OR_SECURITY | A rule of engagement, classification or handling issue arose. Report immediately under AIDCF-PIL-002 §7.5 as well. | — |
| POSITIVE | Something worked notably well and should be kept. | — |

Severity:

| **Severity** | **Meaning** |
|---|---|
| High | Could change a control result, Gate Result or decision state if applied differently, or blocked the pilot. |
| Medium | Caused material rework, delay or disagreement, without changing a result. |
| Low | Minor friction or editorial. |

# 3. Pre-registered questions

The pilot is designed to answer these, in addition to whatever arises. Each is recorded as an INTERPRETATION or DEFECT_ item with what was observed, even if nothing went wrong.

| **ID** | **Question** | **Source** |
|---|---|---|
| Q1 | Did the S3 sufficiency target for claim types shallower than the profile claim type produce results that competent reviewers considered right? | AIDCF-PIL-001 §6.5 |
| Q2 | Is excluding controls outside an approved profile from the coverage denominator a legitimate tailoring, and how should it be recorded in WP-04? | AIDCF-PIL-001 §6.6 |
| Q3 | Should gate criteria that name a test be graded by claim depth, as gate floors are? | AIDCF-PIL-001 §7.2 |
| Q4 | Did the mapping between AIDCF-012 Part XIII and SECURITY.md classification classes work in practice? | AIDCF-PIL-001 §11.1 |
| Q5 | Were the registry mandatory items obtainable at a research host, and which acceptable alternatives were used? | PM-03, PM-04 |
| Q6 | Which Starter Profile controls produced the most assessor disagreement, and why? | PM-08, PM-10 |
| Q7 | Did the LIMITED-at-best decision still give the decision user something useful? | PM-18 |
| Q8 | Were the planning assumptions in AIDCF-PIL-001 §8.2 realistic? | PM-19 |

# 4. Lessons register

One row per lesson. Identifiers are LL-001, LL-002 and so on, never reused.

| **Field** | **Entry** |
|---|---|
| lessonId | LL-nnn |
| raisedBy / date | Role and date |
| phase / stage gate | Authorise, Profile, Plan, Collect, Assess, Review, Decide, Report, Learn / SG0–SG7 |
| category | §2 |
| severity | High, Medium, Low |
| artefact and clause | For example "AIDCF-007A registry v1.1, MCF-THM-010 evidence profile, mandatoryItems"; "AIDCF-009 Part A WP-04"; "AIDCF-PIL-003 §2" |
| controlIds / gateIds | Canonical IDs affected, if any |
| observation | What happened, factually, without host-identifying detail |
| evidence | Workpaper, request row, control-claim log row or meeting note (internal reference; not published) |
| effect in the pilot | Effort, delay, disagreement, result affected (and how it was handled under the standard as written) |
| proposed change | What should change, or "none: keep" for POSITIVE |
| change class (GOVERNANCE.md §8) | Editorial, Minor normative, Major normative, Constitutional, or n/a |
| route | AIDCF-007A amendment (registry); owner of AIDCF-008, -009, -010, -011, -012; pilot pack owner; n/a |
| disposition | CHANGE_PROPOSAL (with Change ID), DEFERRED (reason, revisit trigger), REJECTED (reason), NO_ACTION (POSITIVE, USABILITY with no change) |
| disposition by / date | Lead assessor and research lead; framework-owner response date when received |
| public version | Approved text for publication, or "not for publication" |

Register (copy rows as needed):

| **lessonId** | **Phase** | **Category** | **Severity** | **Artefact and clause** | **IDs** | **Observation** | **Proposed change** | **Change class** | **Disposition** |
|---|---|---|---|---|---|---|---|---|---|
| LL-001 | | | | | | | | | |

# 5. Change proposal (GOVERNANCE.md §9)

Each lesson dispositioned CHANGE_PROPOSAL is written up in the GOVERNANCE.md §9 form. The pilot team proposes; the framework owner and reviewers decide.

| **Field** | **Entry** |
|---|---|
| Change ID | [assigned by the framework owner on receipt; the lessonId until then] |
| Proposer | [pilot team role; organisation if agreed for publication] |
| Affected artifact and version | [entry] |
| Change class | [Editorial / Minor normative / Major normative / Constitutional] |
| Problem statement | [from the lesson, without host-identifying detail] |
| Evidence and rationale | [what the pilot observed; how often; with what effect; noting that one pilot is a single case] |
| Proposed text or machine delta | [exact proposed wording or CSV change] |
| Backward-compatibility impact | [entry] |
| Control and gate impact | [entry] |
| Evidence and assessment impact | [entry] |
| Scoring and decision impact | [entry] |
| Schema and graph impact | [entry] |
| Security and safety impact | [entry] |
| Migration plan | [entry] |
| Reviewer requirements | [disciplines needed to review] |

# 6. Close-out summary

Completed at SG7 and summarised in AIDCF-PIL-004 §10.

| **Item** | **Entry** |
|---|---|
| Lessons by category and severity | [table or counts] |
| Pre-registered questions Q1–Q8 | [one-line answer each, with lesson references] |
| Change proposals submitted | [Change IDs, artifacts, classes] |
| Deferred and rejected items | [count; reasons summarised] |
| Changes recommended to this pilot pack before the next pilot | [list] |
| Approved for publication | [yes / no; approval reference under AIDCF-PIL-002 §12] |
| Signed | Lead assessor [ ] Research lead [ ] Date [ ] |
