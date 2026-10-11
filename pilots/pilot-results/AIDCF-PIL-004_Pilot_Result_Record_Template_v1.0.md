**AIDCF**

# PILOT RESULT RECORD TEMPLATE

*AI Data Centre Facilities Assurance Framework: pilot pack*

Version 1.0

The record of what an authorised AIDCF mini-pilot did, decided and measured

Artifact ID: AIDCF-PIL-004
Artifact type: Pilot record template
Status: Draft for controlled review
Author: Siva Sethumadhavan

> **Pilot status: pack ready; no authorised pilot has taken place.** This is a blank template. No pilot result exists. Whitepaper §29 status PILOT-001: NOT AUTHORISED / NOT EXECUTED.

# Document control

| **Field** | **Value** |
|---|---|
| Document ID | AIDCF-PIL-004 |
| Title | AIDCF Pilot Result Record Template |
| Version | 1.0 |
| Date | 2026-10-11 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Aligned with | Whitepaper §29.2 (acceptance criteria), §29.3 (measures) and §29.4 (authorisation and result record); AIDCF-012 Part IV (metadata), Part V (controlled wording), Part VII (gate summary), Part X (UNKNOWN), Part XIII (classification); AIDCF-010 Part XII (derivation order) and Part XVII (Decision Recommendation record); AIDCF-009 Part A WP-14, WP-18, WP-19; AIDCF-PIL-001 §12 and §13 |
| Companion files | `pilot-metrics-template.csv`; `control-claim-log-template.csv` |

## Revision history

| **Version** | **Date** | **Summary** |
|---|---|---|
| 1.0 | 2026-10-11 | First issue. |

---

## How to use this record

- One record per pilot, completed at SG7 (or at an early stop) by the lead assessor and the research lead, and signed off by the sponsor and the decision authority.
- The full record is **Confidential**. A public version is produced only under AIDCF-PIL-002 §12: identifying fields are redacted to the agreed level, but redaction never removes the decision state, controlling Gate Results, US4/US5 UNKNOWN Records or material limitations (RAS-REQ-012).
- Every figure is a measured value from the pilot's own records. Planning assumptions from AIDCF-PIL-001 §8.2 appear only in §11, labelled as such.
- The decision content (§7) is copied from the approved decision record (WP-19) and the AIDCF-012 reports; it is not re-derived here (AMH-REQ-044).

---

# 1. Status (whitepaper §29.4)

| **Approval/result** | **Status** | **Required evidence** | **Reference** |
|---|---|---|---|
| Sponsor authorisation | [PENDING / SIGNED date] | Signed charter | AIDCF-PIL-002 §2.1, §15; WP-01 |
| Capability-owner authorisation | [PENDING / SIGNED date] | Scope and evidence-access approval | AIDCF-PIL-002 §2.2, §3, §6 |
| Safety/testing authorisation | [PENDING / SIGNED date] | Rules of engagement and stop criteria | AIDCF-PIL-002 §7, §8 |
| Data/privacy/security approval | [PENDING / SIGNED date] | Classification and disclosure decision | AIDCF-PIL-002 §9 to §12 |
| Independent reviewer acceptance | [PENDING / SIGNED date] | Review memorandum | AIDCF-PIL-002 §14; WP-18 |
| Execution | [NOT STARTED / IN PROGRESS / COMPLETED / STOPPED at SGn] | Workpapers and logs | §5 |
| Assurance Decision | [NOT ISSUED / ISSUED: decisionId, state, lifecycle state] | Signed decision record | §7; WP-19 |
| Public summary | [NOT AUTHORISED / AUTHORISED date / PUBLISHED reference] | Publication approval | §12 |

# 2. Record identification (AIDCF-012 Part IV)

| **Field** | **Entry** |
|---|---|
| Pilot ID | [PILOT-nnn] |
| Record version and status | [version]; [DRAFT / IN_REVIEW / ISSUED / CORRECTED / SUPERSEDED / WITHDRAWN] |
| Programme ID (AIDCF-011) | [entry] |
| Assessment ID (AIDCF-009) | [entry] |
| Decision ID | [entry, or "none issued"] |
| Issuer | [organisation and authority] |
| Preparers | [lead assessor; research lead] |
| Reviewers | [technical reviewers; independent reviewer] |
| Intended users and use | [named users; decision supported] |
| Classification | [Confidential (full record) / Public (approved version)] |
| Supersedes | [prior record or "none"] |

# 3. Subject

| **Field** | **Entry** |
|---|---|
| Capability Instance | [identifier and description at the agreed disclosure level] |
| Boundary variant | [A / B]; APPROVED_NA gates if Variant B: [list with rationale and approver] |
| Service Outcomes and tolerances | [each outcome: metric, measurement point, tolerance, states] |
| Decision question | [as chartered] |
| Operating states | [in scope] |
| Evidence period and assessment date | [entry] |
| Exclusions | [each with rationale and decision effect, including the 302 controls outside the Starter Profile] |

# 4. Profile, level and coverage

| **Field** | **Entry** |
|---|---|
| AIDCF artifact versions | [AIDCF-007A, -008, -009, -010, -011, -012 versions] |
| Starter Profile | Commit [hash]; `--check` result [pass]; changes after SG1: [none / list with stage-gate approval] |
| Target Assurance Level | [AL3 / AL4]; claim types concluded: [entry] |
| Mandatory control-claims | [107 at AL3 / 138 at AL4] |
| Results by state | CONFORMING [n]; PARTIAL [n]; NONCONFORMING [n]; UNKNOWN [n]; NOT_APPLICABLE [n]; NOT_ASSESSED [n] |
| Coverage against approved profile (decision basis) | [Scored / (in-scope − NOT_APPLICABLE) × 100], per claim type |
| Coverage against all applicable registry controls (information only) | [value]; stated with the exclusion basis (AIDCF-PIL-001 §6.6) |
| UNKNOWN by severity | US1 [n]; US2 [n]; US3 [n]; US4 [n]; US5 [n] |
| UNKNOWN by type | U1 [n] … U10 [n] |
| Decision confidence | [CONF-0 to CONF-4, with flags] |

# 5. Execution

## 5.1 Stage gates (AIDCF-009 A6)

| **Stage gate** | **Date** | **Approver** | **Outcome (PROCEED / RETURN / STOP)** | **Items carried forward as UNKNOWN or NOT_ASSESSED** |
|---|---|---|---|---|
| SG0 Authorise | | | | |
| SG1 Scope | | | | |
| SG2 Plan | | | | |
| SG3 Fieldwork | | | | |
| SG4 Technical review | | | | |
| SG5 Independent review | | | | |
| SG6 Decide | | | | |
| SG7 Archive | | | | |

## 5.2 Rules of engagement

| **Item** | **Entry** |
|---|---|
| Stops exercised (AMH-REQ-031) | [none / each: date, by whom, reason, effect on results] |
| Deviations, incidents, near misses (B14 step 5) | [none / each with disposition] |
| Extractions not performed and why | [list; UNKNOWN Record references] |
| Close-out confirmed (B14 step 6) | [credentials revoked date; host confirmation] |

## 5.3 Acceptance criteria (whitepaper §29.2; AIDCF-PIL-001 §13)

| **Criterion** | **Met? (yes / no, with reason)** |
|---|---|
| Every assessed assertion has a stable identity and evidence reference | |
| All applicable gates have completed workbooks and independent review | |
| UNKNOWN, exclusions, conflicts and inaccessible scope remain visible | |
| Coverage is calculated against the approved applicable profile | |
| No test exceeded written authority or competent engineering governance | |
| The issued decision is bounded by scope, states, period, evidence and intended users | |
| Any public case material has explicit disclosure approval | |
| AIDCF-PIL-005 lessons register and both metrics files completed | |

# 6. Gate summary (AIDCF-012 VII.1)

All fifteen gates are listed. Results use only PASS, FAIL, UNKNOWN, APPROVED_NA or NOT_ASSESSED; there is no conditional gate result (RAS-REQ-007). Claim depth is stated for every evaluated gate (SDF-REQ-010).

| **Gate** | **Name** | **Result** | **Claim depth** | **Controlling items** | **Decision ceiling (AIDCF-010)** | **Closure required** |
|---|---|---|---|---|---|---|
| CG-01 | Capability and outcome definition | | | | | |
| CG-02 | Boundary and architecture integrity | | | | | |
| CG-03 | Critical dependency visibility | | | | | |
| CG-04 | Life safety and hazardous energy | NOT_ASSESSED | — | Out of pilot scope | LIMITED for outcomes depending on the affected area | Assess CG-04 in a later engagement |
| CG-05 | Resilient electrical supply | | | | | |
| CG-06 | Thermal continuity | | | | | |
| CG-07 | Critical control-system integrity | | | | | |
| CG-08 | Compute, storage and network functional integrity | NOT_ASSESSED | — | Out of pilot scope | LIMITED for outcomes delivered by the cluster, fabric or storage tier | |
| CG-09 | Failure containment | NOT_ASSESSED | — | Out of pilot scope | LIMITED for the decision as a whole | |
| CG-10 | Recovery readiness | | | | | |
| CG-11 | Evidence sufficiency | | | | | |
| CG-12 | Critical UNKNOWN | | | | | |
| CG-13 | Responsibility and authority | NOT_ASSESSED | — | Out of pilot scope | LIMITED | |
| CG-14 | Change control | NOT_ASSESSED | — | Out of pilot scope | LIMITED | |
| CG-15 | Integrated digital authority over infrastructure | NOT_ASSESSED | — | Out of pilot scope; US5 test applied: [result] | [LIMITED / INCONCLUSIVE if US5] | |

Gate criteria met only from existing test records (AIDCF-PIL-001 §7.2):

| **Criterion** | **Existing record found?** | **Status** | **UNKNOWN Record** |
|---|---|---|---|
| GC-05-4, GC-05-6, GC-05-7, GC-06-4, GC-06-6, GC-07-3, GC-07-7, GC-10-3, GC-10-4, GC-10-5 (one row each) | | | |

# 7. Decision

## 7.1 Derivation (AIDCF-010 Part XII; copied from the Decision Recommendation)

Per Service Outcome, in the fixed order; each step can only lower the ceiling.

| **Step** | **Input** | **Ceiling after step** | **Controlling reasons** |
|---|---|---|---|
| 0 Preconditions | Target AL; CG-01 evaluated; gate set fixed | — | |
| 1 Gates | Gate Results including NOT_ASSESSED gates | | |
| 2 UNKNOWN severity | UNKNOWN register | | |
| 3 Coverage | Profile coverage of mandatory control-claims | | |
| 4 Bands | Lowest reported band | | |
| 5 Conditions and confidence | Findings; decision confidence | | |
| 6 Recommendation | Maximum permissible state per outcome and for the question | | Prohibited higher states: [list] |

## 7.2 Decision

| **Field** | **Entry** |
|---|---|
| Maximum permissible state | [from step 6] |
| Approved decision state | [REASONABLY_ASSURED / CONDITIONALLY_ASSURED / LIMITED / NOT_ASSURED / INCONCLUSIVE, or "no decision issued"] |
| Rationale if lower than maximum (SDF-REQ-025) | [entry] |
| Decision authority and date | [entry] |
| Decision lifecycle state | [DRAFT / RECOMMENDED / APPROVED / ACTIVE / SUSPENDED / WITHDRAWN / SUPERSEDED / EXPIRED] |
| Controlled wording (AIDCF-012 V.1, or V.3 if no decision issued) | [verbatim core sentence with bracketed items completed] |
| Supported claims (LIMITED only) | [each claim with its gate and claim depth] |
| Controlling Gate Results and UNKNOWN Records | [list] |
| US3–US5 UNKNOWN Records (AIDCF-012 Part X) | [id, subject, type, severity, effect, evidence needed, owner] |
| Limitations (WP-17) | [id, nature, affected items, disclosure] |
| Conditions (CONDITIONALLY_ASSURED only; not reachable under the AIDCF-PIL-001 scope) | n/a |
| Validity and Reassessment Triggers | [validity end; triggers from decisive controls' `reassessmentTriggers` (AMH-REQ-045)] |
| Independent review | [WP-18 reference; reviewer; challenges raised and disposed] |
| Non-certification note | "This statement is issued by [issuer] under its own authority using the AIDCF method. It is not a certificate, accreditation or endorsement by the AIDCF framework owner." |

# 8. Reports issued (AIDCF-012 Part III)

| **Class** | **Issued?** | **Report ID** | **Classification** | **Distribution** |
|---|---|---|---|---|
| R1 Executive Assurance Report | | | | |
| R2 Technical Assessment Report (required, RAS-REQ-003) | | | | |
| R3 Domain Report(s) | | | | |
| R4 Evidence Package | | | | |
| R5 Gate and Decision Package | | | | |
| R8 Public Summary | | | | |
| R10 Remediation/Closure Report | | | | |

# 9. Decision usefulness (PM-18)

Completed by each named decision user after receiving the reports, before seeing the research analysis. Rating: 1 strongly disagree, 2 disagree, 3 neither, 4 agree, 5 strongly agree, or "cannot say".

| **Statement** | **Rating** | **Reason** |
|---|---|---|
| U1 The output answered the decision question I set, within the limits stated. | | |
| U2 I could see why the decision state was what it was (gates, UNKNOWNs, limitations). | | |
| U3 The output told me what I would need to do or obtain to reach a stronger conclusion. | | |
| U4 The output told me something material I did not already know. | | |
| U5 I would rely on this output, within its stated scope, for the decision named. | | |
| U6 Compared with the reviews I normally receive for this infrastructure, this output was [more / equally / less] useful, because: | n/a | |

These statements are a structured prompt for one user's view; they are not a validated instrument and are not aggregated into a score.

# 10. Research measures summary

| **Measure** | **Value** | **Source** |
|---|---|---|
| PM-01 Time per control-claim (median, IQR) | | control-claim log |
| PM-02 Host effort per request | | evidence request tracking |
| PM-03 Evidence availability (fulfilled; on time) | | evidence request tracking |
| PM-04 Above-AL3 evidence availability | | evidence request tracking |
| PM-05 UNKNOWN rate, by type and severity | | control-claim log |
| PM-06 NOT_ASSESSED rate | | control-claim log |
| PM-07 Sufficiency achieved vs floor | | control-claim log |
| PM-08 Control-result agreement (raw, table, kappa, n) | | control-claim log |
| PM-09 Gate Result agreement (n = evaluated gates) | | WP-14 and re-derivation |
| PM-10 Disagreement causes | | control-claim log |
| PM-11 Scope agreement | | WP-02/WP-03 drafts |
| PM-12 Trace completeness | | AMH-REQ-017 trace |
| PM-13 Usability issues | | AIDCF-PIL-005 |
| PM-14 Framework defects | | AIDCF-PIL-005 |
| PM-15 Orphan findings | | WP-15 |
| PM-16 Dependencies newly identified | | WP-03; CG-03 workbook |
| PM-17 Gate–score divergence | | Score Snapshot; WP-14 |
| PM-18 Decision usefulness | | §9 |
| PM-19 Effort and elapsed time against plan | | §11 |
| PM-20 Interpretation questions | | AIDCF-PIL-005 |

Full definitions and values: `pilot-metrics-template.csv`. Results from one pilot are descriptive; they do not establish reliability, validity or generality.

# 11. Planning assumptions and actuals

The left-hand figures are the planning assumptions from AIDCF-PIL-001 §8.2, not facts.

| **Phase** | **Planned elapsed (weeks)** | **Actual elapsed** | **Planned team (person-days)** | **Actual team** | **Planned host (person-days)** | **Actual host** |
|---|---|---|---|---|---|---|
| Authorise (SG0) | 2–6 | | 3–6 | | 2–5 | |
| Profile (SG1) | 1–2 | | 5–10 | | 2–4 | |
| Plan (SG2) | 1–2 | | 3–6 | | 1–3 | |
| Collect (SG3) | 3–6 | | 8–15 | | 10–25 | |
| Assess, gate (SG4) | 3–5 | | 30–80 | | 2–5 | |
| Independent review (SG5) | 1–2 | | 3–8 | | 0–1 | |
| Decide, report (SG6) | 1–2 | | 4–8 | | 1–2 | |
| Archive, learn (SG7) | 1–2 | | 3–6 | | 1–2 | |
| **Total** | **13–27** | | **59–139** | | **19–47** | |

# 12. Publication

| **Field** | **Entry** |
|---|---|
| Host approver and date | [entry, or "not approved"] |
| Items approved for publication | [list] |
| Anonymisation applied | [summary of redactions and suppression] |
| Repository location of public items | [paths under pilots/ after approval] |
| Framework-owner update to whitepaper §29.4 and README | [requested date; reference to signed records] |

# 13. Sign-off

| **Party** | **Name** | **Statement** | **Signature** | **Date** |
|---|---|---|---|---|
| Lead assessor | | "This record is complete and consistent with the approved decision package." | | |
| Research lead | | "The research measures are reported from the pilot's records and did not influence any result." | | |
| Independent reviewer | | "The decision content reflects the package I reviewed." | | |
| Decision authority | | "The decision content reflects my decision." | | |
| Sponsor | | "I accept this record and the publication status stated." | | |
