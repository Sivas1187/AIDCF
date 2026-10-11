# AIDCF-VAL-001 Incident Back-Testing Protocol

Retrospective validation of AIDCF controls, failure scenarios and critical gates against publicly reported data-centre, AI-infrastructure and cloud incidents.

## Document control

| Field | Value |
|---|---|
| Document ID | AIDCF-VAL-001 |
| Title | Incident Back-Testing Protocol |
| Version | 1.0 |
| Date | 2026-10-11 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Instruments | [`coding-sheet.csv`](coding-sheet.csv), [`coding-sheet-dictionary.csv`](coding-sheet-dictionary.csv), [`incident-register.csv`](incident-register.csv), [`backtest_check.py`](backtest_check.py) |
| Execution status | Protocol ready. No incidents have been identified, screened or coded under this protocol. |

### Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-11 | First issue. |

---

## 1. Purpose and limits of the claim

Back-testing asks one question of each eligible public incident: **if an AIDCF assessment had been carried out shortly before the event, would the controls' assessment criteria and evidence profiles, and the critical gates, have surfaced the conditions that the incident's own report says led to it?**

The answer gives evidence of two properties:

- **Content validity.** Do the AIDCF-004 scenario families and failure modes, and the AIDCF-007A controls, cover the causal factors of real incidents?
- **Detection coverage.** For the factors they cover, would the assessment criteria, evidence requirements and gate logic as written have exposed the condition, or would the assessment have reported conformance?

Back-testing does **not** show that AIDCF assessments prevent incidents, that organisations using AIDCF would have acted on what was surfaced, or that AIDCF performs better than any other method. It assumes a competent assessor with full evidence access (section 4), so its results are an upper bound on what an assessment as specified could surface. They are not an estimate of what assessments achieve in practice. Only authorised pilots (README, *Pilot programme*) can provide evidence of assurance value in use.

**BT-REQ-001** Every output of this protocol shall state that back-testing gives evidence of content validity and detection coverage under the assumptions of section 4, and is not evidence of assurance value, incident prevention or predictive validity.

## 2. Research questions informed

| README research question | What back-testing measures | Primary metric (section 14) | What it cannot show |
|---|---|---|---|
| RQ2 Cross-domain completeness | Whether incident causal factors fall within the fifteen domains and 360 controls, and how many incidents need controls from several domains | Addressing coverage; NOT_ADDRESSED gap list; domains per incident | Whether there is excessive overlap between controls; padding of the catalogue (RQ3) |
| RQ4 Dependency discovery | Whether hidden, shared, external and recovery-only dependencies in incidents are covered by DEP controls and CG-03, and whether those controls would have surfaced them | Strict detection coverage for factors with cause family *Dependency* or a DEP scenario family; CG-03 projected results | Whether graph modelling beats domain-by-domain review (needs a comparison arm) |
| RQ5 Failure-path usefulness | Whether incident propagation maps onto AIDCF-004 scenario families, failure modes and the X01–X20 library paths | Scenario-family and failure-mode mapping rate; library-scenario match rate; G6 gaps | Whether explicit path modelling improves the quality of resilience conclusions in use |
| RQ8 Critical-gate effectiveness | Whether the gates relevant to each incident would have returned FAIL or UNKNOWN, or would have passed despite the condition | Gate-surfacing rate; false-reassurance cases (relevant gate projected PASS) | Effect of gates on real decisions; score-masking in live assessments |

Coder agreement (section 13) also tells RQ10 how clear the control criteria are, but it is not evidence of assessor reliability in a real assessment.

## 3. Terms

| Term | Meaning in this protocol |
|---|---|
| Incident | A publicly reported event in which data-centre, AI-infrastructure or cloud infrastructure failed to deliver a service outcome, with a published post-incident account. |
| Initiating event | AIDCF-004 §6: the event or condition that started the scenario. |
| Pre-event condition | A state that existed before the initiating event: design, configuration, capacity, maintenance state, dependency, procedure, staffing or safeguard condition. |
| Causal factor | A pre-event condition that the source identifies as causing or contributing to the incident or its escalation, or as delaying recovery. Recorded with a role: INITIATING, PREDISPOSING, ESCALATION or RECOVERY. |
| Reference date (T-ref) | The date of the hypothetical assessment: immediately before the initiating event. |
| Framework baseline | The frozen AIDCF version against which all incidents are coded (section 9, step 0). |
| Engaged control or criterion | A control or gate criterion that a coder maps to a causal factor of the incident. |
| Relevant gate | A critical gate whose scope (`registries/gates/critical-gates.csv`) covers the incident's consequence or a pre-event condition (section 11). |
| False reassurance | A relevant gate projected to PASS, or an engaged control projected CONFORMING (detection judgement NOT_DETECTED), despite the pre-event condition. |
| Pre-event dossier | An extract of the sources containing only the pre-event timeline and the observable outcome, prepared before coding (section 8). |

## 4. Counterfactual assessment model

Coders judge a hypothetical assessment with these fixed assumptions. The assumptions are deliberately favourable to the framework so that a NOT_DETECTED or PASS result cannot be explained away by poor execution.

1. **Scope.** The assessment boundary includes the Capability Instance whose Service Outcome failed, plus the infrastructure the source names as involved. Where the operator was a tenant of another provider's facility, the coder records whether the gates would have been APPROVED_NA under their `approvedNaConditions` and carried by CG-03 instead.
2. **Level and profile.** Every engaged control is assessed at its registry `requiredAssuranceLevel` with the evidence profile in `registries/controls/evidence-profiles.csv` (required classes, mandatory items, state coverage, period coverage, independence).
3. **Competence and access.** The assessor is competent, follows the control's assessment procedure and criteria literally, and gets every evidence item that existed or could have been produced at T-ref.
4. **Timing.** The assessment takes place at T-ref. A condition that arose shortly before the event counts as visible only if it existed at T-ref, or if it arose through an event listed in the control's `reassessmentTriggers` (the framework would have required reassessment).
5. **No outcome knowledge.** The assessor does not know the event will happen. Coders judge whether the criteria and evidence would have surfaced the condition, not whether a perceptive assessor might have noticed it.

**BT-REQ-002** Coders shall apply the section 4 assumptions to every judgement and shall not credit detection to assessor insight that goes beyond the text of a control's assessment criteria, mandatory evidence items or assessment procedure.

## 5. Roles, competence and independence

| Role | Responsibilities | Independence requirement |
|---|---|---|
| Study lead | Freezes the baseline, runs the search, keeps the register and coder key, assigns incidents, produces outputs | May be the framework author; must disclose it |
| Extractor | Prepares pre-event dossiers (section 8) | Not Coder A or Coder B for the same incident |
| Coder A, Coder B | Code each incident independently | At least one of the two is independent of the framework author (`independent_of_author` = Y); preferably both |
| Adjudicator | Consolidates factor lists, chairs reconciliation, decides unresolved disagreements | Independent of the framework author whenever either coder is the author |

Coders need working knowledge of data-centre power, cooling and IT infrastructure, and must complete calibration (section 9, step 3). Coders and adjudicators declare in writing any prior design involvement in AIDCF, commercial interest, and any employment or contract with an operator in the sample during the incident period.

**BT-REQ-003** Each incident shall be coded by two coders working independently, at least one of whom is independent of the framework author. The framework author shall not act as adjudicator for an incident they have coded.

**BT-REQ-004** A coder who holds non-public knowledge of an incident (for example through employment, a contract or confidential briefing) shall be recused from that incident. The recusal is recorded in the register `notes` without recording the reason.

## 6. Incident eligibility and source quality

### 6.1 Inclusion criteria

An incident is eligible when all of the following hold:

1. It affected data-centre facility infrastructure (power, cooling, fire and physical systems), AI or HPC compute, storage or network fabric, cloud infrastructure services, or the control planes and OT systems that operate them.
2. The initiating event occurred between **2015-01-01** and the frame-freeze date (section 7.1).
3. At least one **PRIMARY** or **REGULATOR** source exists (section 6.2) and is publicly accessible without a confidentiality agreement.
4. The sources meet the minimum detail criteria (section 6.3).

### 6.2 Source hierarchy

| Source type | Definition | Permitted use |
|---|---|---|
| PRIMARY | Post-incident report, post-event summary or root-cause statement published by the operator or provider whose infrastructure failed, under its own name | Any coded fact, including causal factors and pre-event conditions |
| REGULATOR | Report by a regulator, statutory investigator, public inquiry or accident-investigation body | Any coded fact; takes precedence over PRIMARY where they conflict, with the conflict noted |
| SECONDARY_PRESS | Reputable technical or trade press: named author, editorial corrections policy, reporting that cites a primary or regulator source | Finding candidates, corroborating dates and scope; never the sole basis for a causal factor or pre-event condition |

Aggregated outage statistics, vendor marketing, social-media posts, forums and anonymous accounts are used only to find candidates.

**BT-REQ-005** Every causal factor and pre-event condition coded shall be traceable to a PRIMARY or REGULATOR source cited in `source_urls`. A factor supported only by SECONDARY_PRESS shall not be coded.

### 6.3 Minimum detail

The register's `detail_level` field records the screener's assessment:

| Level | Criteria | Eligible |
|---|---|---|
| HIGH | Timeline with timestamps or ordered steps; at least two causal or contributing factors; affected infrastructure layer and scope stated; at least one pre-event condition (configuration, design, maintenance state, capacity, procedure) stated explicitly | Yes |
| MEDIUM | Ordered description of events; at least one causal factor expressed as a pre-event condition; affected layer stated | Yes |
| LOW | Outcome and broad cause only (for example "a power issue"), no pre-event condition | No (EX-02) |

### 6.4 Exclusions

| Code | Exclusion |
|---|---|
| EX-01 | No PRIMARY or REGULATOR source; only secondary or anecdotal accounts |
| EX-02 | Detail level LOW |
| EX-03 | Initiating event outside the date window |
| EX-04 | Out of scope: application or software defect with no infrastructure, control-plane or capacity condition; data breach with no effect on infrastructure availability, integrity or control; consumer-device or end-user network issue |
| EX-05 | Duplicate of an incident already in the register (same event reported separately) |
| EX-06 | Source not retrievable or not archivable at screening |
| EX-07 | Source withdrawn, or the operator has publicly disputed the account in material respects and no regulator report settles it |
| EX-08 | Subject to active legal proceedings where the sponsor's legal adviser advises against coding |

**BT-REQ-006** Every candidate shall be logged in `incident-register.csv` with its eligibility outcome. A second person shall check every EX-02 and EX-04 exclusion, since these involve judgement, and record this in `exclusion_checked_by`.

## 7. Sampling frame and sample size

### 7.1 Frame construction

1. **Freeze the frame window.** Record the frame-freeze date. Incidents after it are not added during the run.
2. **Systematic search.** Search each source family below. Record date, source, query and result count in the run log (section 18) so the search can be repeated.
   - **S1** Provider-published post-incident review channels: public post-event summary and incident-history pages of cloud providers; incident statements of colocation, network and HPC facility operators.
   - **S2** Regulator and public-body publications: telecommunications outage investigations, financial-sector operational-resilience incident reports, public inquiry reports, fire and accident investigation reports involving data centres.
   - **S3** Technical and trade press archives and public outage trackers: for finding candidates only.
   - **S4** Published compilations of post-incident reviews (practitioner or academic): for finding candidates only. Each incident is then traced to its primary source.
3. **Log, then screen.** Log every candidate before screening (`eligibility_status` = CANDIDATE), screen against section 6, and record the counts of identified, screened, excluded (by code), eligible, selected and coded incidents. Report the flow in the style of a PRISMA 2020 flow diagram (Page et al., 2021).

### 7.2 Strata and target sample

The primary stratum is `failure_category`: the layer where the initiating failure occurred.

| Stratum | Covers | Target | Minimum | Sub-quotas (where eligible incidents exist) |
|---|---|---|---|---|
| POWER | Utility, UPS and BESS, generation, fuel, distribution, protection, power quality | 8 | 5 | At least 1 involving battery failure or thermal runaway (tag BATTERY) |
| COOLING | Heat rejection, chilled water, air side, CDUs and liquid cooling, water supply, heat events | 8 | 5 | At least 2 heat/ambient events (HEAT_EVENT); at least 2 liquid-cooling incidents (LIQUID_COOLING) |
| NETWORK_FABRIC | Data-centre and AI fabrics, backbone, interconnect, core network services (DNS, time) | 8 | 5 | At least 1 AI/HPC fabric incident (AI_HPC) |
| STORAGE | Block, object and file storage, metadata services, checkpoint and backup tiers | 8 | 5 | — |
| CONTROL_PLANE_OT | BMS, EPMS, CDU and PLC controllers, cloud control planes, cluster managers, automation | 8 | 5 | At least 2 facility OT incidents |
| CHANGE_HUMAN | Change, maintenance, procedure and operator-action initiated incidents | 8 | 5 | — |
| EXTERNAL_DEPENDENCY | Utility, carrier, water, fuel, third-party service and regional events | 8 | 5 | At least 1 compound regional event (MULTI_SITE) |
| **Total** | | **56** | **35** | Across the whole sample: target at least 14 incidents tagged AI_HPC |

**Secondary balancing.** No single operator may account for more than 6 incidents in the sample or more than 2 in any stratum. Within these limits, aim for at least three operator types (`operator_type`) per stratum.

**Selection.** Where eligible incidents in a stratum exceed the target, select by seeded random draw, not by prominence. Sort eligible IDs ascending, shuffle with a recorded integer seed using Python's `random.Random(seed).shuffle`, take incidents in order while respecting the sub-quotas and operator caps, and record the draw rank in `stratum_draw_rank`. Undrawn eligible incidents are marked RESERVE and replace withdrawn incidents in draw order.

**Shortfall.** If a stratum or sub-quota cannot be filled, do not relax the eligibility rules. Record the shortfall as a result: it is itself evidence about what public reporting reveals, and especially about AI-specific and liquid-cooling incidents.

### 7.3 Sample-size rationale

The sample is sized for three purposes. The figures below are planning estimates, not power calculations.

1. **Agreement precision.** Assume about 3 judged causal factors per incident and about 2 engaged controls per factor. 56 incidents then give roughly 300 control-level judgement pairs. Using Cohen's (1960) large-sample approximation SE(κ) ≈ √(p_o(1−p_o) / (n(1−p_e)²)) with p_o = 0.80 and p_e = 0.30, SE ≈ 0.04, a 95% interval of about ±0.08. At the minimum of 35 incidents (about 190 pairs) the interval widens to about ±0.10. Gate judgements, at about 2.5 relevant gates per incident with p_e ≈ 0.5, give about ±0.13 at 56 incidents and ±0.17 at 35.
2. **Overall coverage precision.** About 170 judged factors give a 95% Wilson interval half-width (Wilson, 1927) of about 0.075 at a proportion of 0.5. 35 incidents (about 105 factors) give about 0.095.
3. **Stratum description.** Eight incidents per stratum (about 24 factors) gives a half-width near 0.19: enough to describe and compare strata, not to estimate stratum rates precisely. Stratum results are therefore reported descriptively.

Factors within an incident are not independent, so factor-level intervals understate the uncertainty. Section 14 requires incident-level metrics alongside them.

**BT-REQ-007** Selection within strata shall use the recorded seeded draw. The seed, the sorted eligible list and the resulting order shall be retained so the selection can be reproduced.

## 8. Hindsight-bias controls

Knowing the outcome makes it look more foreseeable than it was (Fischhoff, 1975). The controls below separate what was knowable before the event from what the post-incident analysis concluded.

1. **Declared familiarity.** Before opening any material, each coder records `prior_familiarity` (NONE, GENERAL, DETAILED). Results are reported separately for DETAILED codings.
2. **Pre-event dossier.** The extractor splits each source into four segments: PRE (conditions, configuration, state and events before the initiating event), EVENT (initiating event and observable outcome: what failed, scope, duration), ANALYSIS (root cause, contributing-factor analysis, "why") and REMEDIATION (actions, lessons, commitments). The dossier contains PRE and EVENT only, paraphrased neutrally. Wording that attributes cause ("because", "due to", "the root cause was") is reduced to a statement of fact or removed, and the extractor logs each such change. The extractor does not add interpretation.
3. **Pre-reveal coding.** Coders read the dossier only. They list pre-event conditions and the AIDCF-004 scenario families an analyst would instantiate from them, reasoning forwards from conditions to possible paths. They record these factors (coding pass 1) with `coding_phase` = PRE_REVEAL and lock the file by recording its SHA-256 hash in the run log.
4. **Reveal.** Coders then read the full sources. They may add factors, flagged POST_REVEAL. Pre-reveal factors are not edited. If the analysis shows a pre-reveal factor was wrong, the coder adds a note; the row stays.
5. **Knowability.** For each factor, coders record what the source says was knowable before the event (`knowability`): STATED_KNOWN, DISCOVERABLE, NOT_KNOWABLE or NOT_STATED. A factor visible only through the post-event investigation (for example a defect found by teardown with no precursor in any record or test) is NOT_KNOWABLE. Coders must then check whether a knowable safeguard condition exists (for example a fleet-wide rollout without staging) and code that as a separate factor.
6. **Blind second coder.** Coder B never sees Coder A's codes before reconciliation, and coders are not told which of them, if either, is the framework author.
7. **Measurement.** The share of judged factors first identified POST_REVEAL is reported as a hindsight indicator. Detection metrics are reported for PRE_REVEAL factors alone as well as for all factors.

**BT-REQ-008** No coder shall read the ANALYSIS or REMEDIATION segments of an incident's sources before their pass 1 factor list for that incident is locked.

## 9. Coding procedure

### Step 0: Freeze the baseline

Record the framework baseline in the run log: repository commit hash; AIDCF-004 v1.1; control registry v1.1 (AIDCF-007A-AMD-002) as in `registries/controls/`; gate records and criteria as in `registries/gates/`; this protocol's version. The baseline does not change during the run. Changes proposed from findings are tested afterwards (section 16).

**BT-REQ-009** All incidents in a run shall be coded against one frozen framework baseline, recorded with its commit hash before coding begins.

### Step 1: Build the frame, screen and select

Follow sections 6 and 7. For each selected incident, archive every source (for example a public web-archive snapshot), list the archive references in `archive_refs` and record `access_date`.

### Step 2: Prepare the dossier

The extractor prepares the pre-event dossier (section 8). Status becomes DOSSIER_READY.

### Step 3: Calibrate (once per coder, before the first sample incident)

Coders independently code three calibration incidents that are eligible but not in the sample, plus the fictional example `INC-EXAMPLE-01`. They then compare results with the adjudicator and clarify their reading of section 10. Calibration codings are kept but excluded from all statistics. Repeat calibration if detection-judgement κ on the first 10 sample incidents is below 0.40 (section 13).

### Step 4: Independent factor identification (coding pass 1)

Each coder, working alone:

1. Records `prior_familiarity`, reads the dossier and writes `timeline_before_cause`.
2. Lists each causal factor as a **pre-event condition**: a state, not an event. Write "UPS maintenance bypass not returned to normal after work", not "UPS failed". Factor IDs are coder-local (CF-A01, CF-B01, ...).
3. For each factor records `factor_role`, `causal_factor`, `knowability`, `cause_family` (AIDCF-004 Part VI), `scenario_family` (Part XIII, `DOMAIN:Family name`), `library_scenario` (Part XIV X01–X20 or NONE), `failure_modes` (Appendix A FM-*) and `generic_modes` (Part VII M-codes). Control fields stay empty.
4. Locks the pre-reveal list, reads the full sources, adds POST_REVEAL factors and locks again. Status becomes PASS1_LOCKED once both coders have locked.

Analysis does not stop at "human error": coders record the systemic contributors the source describes, such as procedure, interface, alarm load, staffing and authority (AIDCF-004 THF-REQ-014).

### Step 5: Consolidate factors

The adjudicator merges both lists into consolidated factors CF-01, CF-02, ..., worded neutrally and without showing who proposed each. The crosswalk (for example "CF-03 from CF-A02; CF-B04") goes in the consolidated rows' `notes`. A consolidated factor takes PRE_REVEAL if either coder identified it before the reveal. The match rate (matched factors ÷ union of factors) is reported as factor-identification agreement. Status becomes FACTORS_CONSOLIDATED.

### Step 6: Independent mapping and judgement (coding pass 2)

Each coder, again working alone, takes every consolidated factor:

1. **Find candidate controls.**
   - Start from the AIDCF-007A families listed in the *Families* column of each coded Appendix A failure mode and in the *Relevant MCF control families* of any coded library scenario.
   - **Domain sweep:** scan the control titles and objectives of every domain the factor touches (at least the scenario family's domain, DEP and OPS). Engaged controls are often outside the obvious domain.
   - Keep a control when its **objective or requirement** covers the factor's subject. A shared keyword is not enough.
2. **Write one CONTROL row per kept control.**
   - Cite the assessment-criterion numbers relied on (`control_criteria`).
   - Check the control's evidence profile: mandatory items, required classes, `stateCoverage`, `periodCoverage`, `reassessmentTriggers`.
   - Record `projected_control_result` and `detection_judgement` using section 10, and note in `notes` the evidence item that would have revealed the condition.
3. **No control.** If no control's objective or requirement covers the factor after the sweep, write one row with `control_id` = NONE and `detection_judgement` = NOT_ADDRESSED, and record a gap (section 12).
4. **Gates.** Identify candidate and relevant gates and write one GATE row per relevant gate (section 11).
5. **Confidence and gaps.** Record `confidence` and any `gap_type` on each row.
6. **Lock.** Record the SHA-256 hash. Status becomes PASS2_LOCKED once both coders have locked.

### Step 7: Reconcile

See section 13.3. Produce RECONCILED rows. Status becomes RECONCILED.

### Step 8: Quality check

Run `python3 research/back-testing/backtest_check.py --check`. It must report zero errors; resolve or justify every warning. The study lead re-reads a 10% random sample of RECONCILED rows against the sources for traceability (BT-REQ-005). Status becomes QA_COMPLETE.

**BT-REQ-010** Every DETECTED, PARTIALLY_DETECTED or NOT_DETECTED judgement shall cite at least one assessment-criterion number of the engaged control, and its notes shall name the evidence item relied on.

**BT-REQ-011** Coders shall perform the domain sweep for every factor before recording NOT_ADDRESSED.

## 10. Detection judgement scale

The judgement is made for each pair of (consolidated factor, engaged control). Apply the steps in order and stop at the first that applies.

| Step | Condition | Judgement |
|---|---|---|
| 1 | `knowability` is NOT_KNOWABLE | No judgement: leave `detection_judgement` empty. The factor is counted in the unknowable tally and excluded from detection metrics. Check for a knowable safeguard condition (section 8, item 5). |
| 2 | `knowability` is NOT_STATED, or the source does not say enough to tell whether the cited criteria would apply | **INSUFFICIENT_INFORMATION** |
| 3 | After the domain sweep, no control's objective or requirement covers the factor | **NOT_ADDRESSED** (one row, `control_id` NONE; gap G1 or G6) |
| 4 | Tests D1–D4 below all hold | **DETECTED** |
| 5 | The control covers the condition and test D1 holds, but one or more of D2–D4 fails; or the criterion would surface a related weakness but understate its consequence | **PARTIALLY_DETECTED** |
| 6 | The control covers the condition, but its criteria, read literally with the profile's evidence, would be met despite it | **NOT_DETECTED** |

Detection tests:

- **D1 Criterion.** At least one cited assessment criterion, read literally, would be unmet, or could not be shown to be met, while the condition existed.
- **D2 Evidence.** A mandatory evidence item or required evidence class in the control's profile would contain or reveal the condition. Detection must not depend on optional evidence, on the affected item happening to fall in a sample, or on assessor judgement beyond the criterion text.
- **D3 State.** The operating state in which the condition existed or would show (for example MAINTENANCE, DEGRADED, EMERGENCY) is in the profile's `stateCoverage`.
- **D4 Timing.** The condition existed at T-ref, or arose through an event listed in the control's `reassessmentTriggers` (section 4, item 4).

Projected control result:

| Judgement | Permitted `projected_control_result` |
|---|---|
| DETECTED | PARTIAL, NONCONFORMING, or UNKNOWN (evidence absent or below floor, recorded as an UNKNOWN Record that names the condition) |
| PARTIALLY_DETECTED | Any of CONFORMING, PARTIAL, NONCONFORMING, UNKNOWN; record which test (D2, D3 or D4) failed |
| NOT_DETECTED | CONFORMING only. This is control-level false reassurance; record a gap (normally G2 or G3) |
| NOT_ADDRESSED, INSUFFICIENT_INFORMATION | Empty |

Factor-level judgement is the best judgement across the factor's engaged controls, ranked DETECTED > PARTIALLY_DETECTED > NOT_DETECTED. It is NOT_ADDRESSED if the factor's only row is NOT_ADDRESSED, and INSUFFICIENT_INFORMATION if every row is INSUFFICIENT_INFORMATION.

Boundary guidance:

- A projected UNKNOWN counts as DETECTED only when the UNKNOWN would itself point at the condition. Example: MCF-THM-010 says an untested CDU group is recorded as UNKNOWN, and the incident turns on that untested failover. A generic evidence gap unrelated to the condition is not detection.
- A test that exists and would pass because it does not reproduce the incident's conditions is NOT_DETECTED unless a criterion requires representative conditions. Example: a resistive load-bank test where the incident turned on dynamic load.
- If the source says the operator knew of the condition and accepted it, the judgement still concerns whether the assessment would have surfaced it. Surfacing is not the same as the condition being corrected; AIDCF-004 §7 separates detection from prevention.

**BT-REQ-012** Coders shall apply the section 10 decision order and tests D1–D4 exactly. A DETECTED judgement shall not be recorded with a projected result of CONFORMING.

## 11. Gate judgement

**Candidate gates** for an incident are the union of:

- the gates mapped (CRITICAL or SUPPORTING) to its engaged controls in `registries/controls/gate-mappings.csv`;
- the *Primary gates* of its coded scenario families (AIDCF-004 Part XIII);
- the *Relevant critical gates* of any coded library scenario.

A candidate gate is **relevant** if the incident's consequence, or a coded pre-event condition, falls within the gate's `scope` in `registries/gates/critical-gates.csv`. Coders write a GATE row for each relevant gate only, listing in `factor_id` the factors that engage it.

**Projected gate result.** Apply the canonical definitions in `registries/vocabularies/gate-results.csv` to the engaged controls and criteria:

| `gate_judgement` | Rule in this protocol |
|---|---|
| FAIL | An engaged CRITICAL-mapped control is projected NONCONFORMING or PARTIAL, or an engaged gate criterion (`critical-gate-criteria.csv`) would be shown not met. A NONCONFORMING SUPPORTING control whose deficiency is the causal factor also gives FAIL, because a competent gate-level evaluation would conclude the gate was defeated. |
| UNKNOWN | No FAIL condition, but an engaged CRITICAL control is projected UNKNOWN, gate evidence would fall below the gate's `evidenceFloor`, or a US4 UNKNOWN would be attached. |
| PASS | All engaged CRITICAL controls projected CONFORMING and all engaged gate criteria met. **This is a false-reassurance case** and must carry a gap (G4 or G5, or G2/G3 if the cause sits in a control). |
| APPROVED_NA | The gate would have been approved non-applicable under its `approvedNaConditions` (for example a colocation tenant boundary). Record which gate carries the dependency (normally CG-03) and judge that gate too. |
| INSUFFICIENT_INFORMATION | The sources do not allow a judgement. |

The judgement covers only the engaged controls and criteria; other gate content is assumed satisfied. A projected PASS therefore means "the gate would not have caught *this*", not that the gate would have passed overall.

**BT-REQ-013** A GATE row with `gate_judgement` PASS or FAIL shall cite the gate criteria relied on, and every PASS on a relevant gate shall be listed as a false-reassurance case in the results report.

## 12. Gap handling

Any incident factor that the framework does not address, or addresses in a way that would not surface it, is a gap. Each gap is coded on the row where it appears.

| `gap_type` | Meaning | Artefact affected | GOVERNANCE §8 change class |
|---|---|---|---|
| G1_NO_CONTROL | No control's objective or requirement covers the factor | AIDCF-007A control universe | A new control changes the 15/90/360 cardinality, which is a **constitutional** change. First test whether an existing control's objective can carry a new criterion (G2, minor normative). Propose a new control only where none can, and say why. |
| G2_NO_CRITERION | The control covers the subject but no assessment criterion tests the condition | AIDCF-007A control criteria (`registries/controls/`, catalogue) | Minor normative |
| G3_EVIDENCE_PROFILE | A criterion exists but the evidence profile (mandatory items, classes, state or period coverage, reassessment triggers) would not reveal the condition | `registries/controls/evidence-profiles.csv` | Minor normative; follows CONTRIBUTING §8 if the control is CRITICAL-mapped |
| G4_GATE_MAPPING | A control that would detect the condition is not mapped to the gate whose scope the consequence fell within | `registries/controls/gate-mappings.csv` | Minor normative (mapping), with critical-gate heightened review under CONTRIBUTING §8 |
| G5_GATE_CRITERION | Gate criteria or gate logic would give PASS despite the condition | `registries/gates/critical-gate-criteria.csv`, AIDCF-010 | Major normative (gate logic), CONTRIBUTING §8 |
| G6_THREAT_MODEL | No AIDCF-004 scenario family, Appendix A failure mode or library path fits the incident | AIDCF-004 | Minor normative (major if it changes the gate a scenario bears on) |

**Logging.** After reconciliation, every distinct gap becomes a finding raised as an issue against **AIDCF-007A** (the owner of control content), using the CONTRIBUTING §5 fields. G5 and G6 findings also name AIDCF-010 or AIDCF-004.

- **Category.** TECH for G1, G2 and G6; ASSUR for G3, G4 and G5.
- **Severity.**
  - BLOCKER if the gap makes CG-04 (life safety and hazardous energy) pass despite the condition.
  - MAJOR if it produces a false-reassurance PASS on any other relevant gate, or a NOT_ADDRESSED PREDISPOSING or ESCALATION factor.
  - MODERATE otherwise.
- **Content.** The issue cites the incident by register ID and URL, quotes no more than section 17 allows, states the proposed criterion, evidence item, mapping or scenario text, and gives the recurrence count across the sample.
- **Recurrence.** One incident is enough to raise a finding. Recurrence affects priority, not eligibility.

**BT-REQ-014** Every distinct reconciled gap shall be raised as a finding against AIDCF-007A, with category, severity and change class assigned by this section. Its disposition shall be recorded through the GOVERNANCE §9 change-proposal process.

## 13. Agreement measurement and disagreement resolution

### 13.1 Units and statistics

| Judgement | Unit | Statistic |
|---|---|---|
| Factor identification | Consolidated factor | Match rate = matched ÷ union (step 5) |
| Scenario-family assignment | Consolidated factor | Percentage exact agreement on the primary family |
| Control mapping | Consolidated factor | Mean Jaccard index of the two coders' control sets |
| Detection judgement | (incident, factor, control) pair coded by both | Percentage agreement and Cohen's κ (Cohen, 1960) over the five categories; marginal distributions reported |
| Gate relevance | Candidate gate | Count of gates judged relevant by one coder only |
| Gate judgement | (incident, gate) pair coded by both | Percentage agreement and Cohen's κ |

`backtest_check.py --agreement` computes these from rounds A and B. As a secondary analysis, report linearly weighted κ (Cohen, 1968) on the ordinal subset DETECTED > PARTIALLY_DETECTED > NOT_DETECTED. Also report Krippendorff's α (Krippendorff, 2004) if more than two coders are used.

### 13.2 Interpretation

Report κ with percentage agreement and the marginals together. When one category dominates, κ can be low even though agreement is high (Feinstein and Cicchetti, 1990). The Landis and Koch (1977) bands may be quoted only as descriptive labels. Decision rules:

- κ ≥ 0.60 on detection judgement: results reported as primary.
- 0.40 ≤ κ < 0.60: results reported with an explicit reliability caveat; the most frequent disagreement patterns are analysed and reported.
- κ < 0.40: results not reported as findings about the framework. Revise the scale wording or coder guidance, re-calibrate (step 3), and recode. The low agreement is itself reported as a finding about the clarity of the criteria involved (RQ10).

### 13.3 Disagreement resolution

1. **Consensus meeting.** Coders A and B meet with the adjudicator and discuss each disagreement against the source text and the control's criteria. Agreed codes become RECONCILED rows; the reason for any change goes in `notes`.
2. **Adjudication.** The adjudicator decides disagreements that remain and records the reasoning.
3. **Preserve originals.** Rounds A and B are never edited after locking.
4. **Systematic disagreements.** Where the same criterion is read differently across several incidents, record it as a G2 finding on criterion clarity.

**BT-REQ-015** Agreement statistics shall be computed only from locked independent rounds A and B, and shall be reported whatever their value.

## 14. Metrics and analysis

All metrics use RECONCILED rows, are produced by `backtest_check.py --metrics`, and carry 95% Wilson intervals.

| Metric | Definition |
|---|---|
| Addressing coverage | Judged factors (excluding NOT_KNOWABLE and INSUFFICIENT_INFORMATION) with at least one engaged control ÷ judged factors |
| Strict detection coverage | Judged factors whose factor-level judgement is DETECTED ÷ judged factors |
| Inclusive detection coverage | DETECTED or PARTIALLY_DETECTED ÷ judged factors (never reported without the strict figure) |
| Coverage by domain | Strict coverage grouped by the domain of the factor's primary scenario family, and by the domain of the engaged control |
| Coverage by stratum | Strict coverage grouped by `failure_category` (descriptive, section 7.3) |
| Coverage by gate | For each gate: count of relevant incidents and the distribution of projected FAIL / UNKNOWN / PASS / APPROVED_NA |
| Gate-surfacing rate | Incidents with at least one relevant gate projected FAIL or UNKNOWN ÷ incidents; FAIL-only rate reported separately |
| False-reassurance cases | List of (incident, gate) with projected PASS, and (incident, factor, control) with NOT_DETECTED |
| Threat-model fit | Factors with an Appendix A failure mode ÷ factors; incidents matching a library scenario ÷ incidents; G6 count |
| Gap list | Distinct reconciled gaps by type, artefact and recurrence |
| Hindsight indicator | Judged factors first identified POST_REVEAL ÷ judged factors; strict coverage for PRE_REVEAL factors alone |
| Unknowable tally | Factors coded NOT_KNOWABLE, by stratum |

Required sensitivity analyses:

- metrics at incident level: an incident counts as surfaced if any judged PREDISPOSING or ESCALATION factor is DETECTED;
- metrics excluding codings with `prior_familiarity` DETAILED;
- metrics from the independent coder's round alone (where only one coder is independent). If strict coverage differs from the reconciled figure by more than 10 percentage points, report both and discuss the difference;
- metrics excluding MEDIUM detail-level incidents.

No pass mark for the framework is set in advance. The results are descriptive evidence for RQ2, RQ4, RQ5 and RQ8, and null or negative results are reported on the same footing as positive ones (README, *Research Questions*).

## 15. Threats to validity

| Threat | Type | Mitigation in this protocol | Residual effect |
|---|---|---|---|
| Publication bias toward dramatic incidents; large providers publish more | External | Systematic search; seeded random selection within strata; operator caps; shortfall reported | Sample represents publicly reported incidents, not all incidents; facility-level and AI-specific failures are likely under-represented |
| Incomplete or self-serving public reports | Construct, internal | PRIMARY/REGULATOR only for facts; detail floor; INSUFFICIENT_INFORMATION and NOT_STATED codes; regulator takes precedence | Pre-event conditions not disclosed cannot be coded; coverage is conditional on disclosure |
| Hindsight bias | Internal | Dossier, pre-reveal locking, familiarity declaration, knowability coding, PRE_REVEAL-only metrics (section 8) | Familiar incidents cannot be fully blinded; reported separately |
| Framework author as coder; motivated generous mapping | Internal | At least one independent coder; independent adjudicator; criterion citation required; independent-coder sensitivity analysis | Disclosed in every output |
| Counterfactual optimism (competent assessor, full access) | Construct | Assumptions stated (section 4) and reported as an upper bound | Results do not estimate real-world detection |
| Mapping to "nearest" controls inflates coverage | Construct | Objective/requirement test, not keyword; D1–D4 tests; NOT_DETECTED requires CONFORMING | Some residual judgement; measured by κ |
| Small strata; clustered factors | Statistical conclusion | Wilson intervals; incident-level metrics; descriptive stratum reporting | Stratum differences are indicative only |
| Framework drift during the run | Internal | Frozen baseline (BT-REQ-009) | None if followed |
| Older incidents on superseded technology | External | 2015 window; AI_HPC and LIQUID_COOLING sub-quotas | Liquid-cooling and AI-fabric coverage depends on how many public reports exist |

## 16. Outputs and feedback into AIDCF

| Output | Content | Location |
|---|---|---|
| O1 Incident register | Full frame with eligibility decisions and flow counts | `incident-register.csv` |
| O2 Coded dataset | Rounds A, B and RECONCILED, locked hashes | `coding-sheet.csv` (or run-specific copies listed in the run log) |
| O3 Agreement report | Section 13 statistics and disagreement analysis | Results report annex |
| O4 Back-testing results report | Method summary, deviations from protocol, flow diagram, section 14 metrics and sensitivity analyses, false-reassurance cases, gap list, threats, RQ evidence statements | New controlled document; ID assigned at issue |
| O5 Findings | One issue per distinct gap (section 12) | Repository issue tracker |
| O6 Research-question evidence notes | Short evidence statements for RQ2, RQ4, RQ5, RQ8 | `research/research-questions/` |

**Feedback loop.**

1. **Raise.** Findings (O5) go into the issue tracker using the CONTRIBUTING §5 fields, with conflict-of-interest disclosure.
2. **Propose.** An accepted finding becomes a change proposal under GOVERNANCE §9 and is approved at the §10 threshold for its change class (section 12). Critical-gate changes follow CONTRIBUTING §8 and GOVERNANCE §11.
3. **Retest.** After a release that changes the baseline, recode the incidents behind each closed finding against the new baseline (same protocol, new run). Record whether the gap closed and whether any other judgement changed.
4. **Record.** Until an independent governance body exists, dispositions disclose that they are AIDCF-internal and author-controlled (GOVERNANCE §10).

**BT-REQ-016** The results report shall list every deviation from this protocol, with its reason and likely effect on the results.

## 17. Ethics, legal and publication

1. **Public information only.** Only publicly accessible sources are used. Non-public knowledge is not used even if a coder has it (BT-REQ-004).
2. **No speculation about named organisations.** Coded facts are limited to what the organisation's own report or a regulator report states. Where a source is silent, the code is NOT_STATED or INSUFFICIENT_INFORMATION; coders do not infer. Outputs use attributive wording ("the operator's report states that ...") and make no judgement of any organisation's competence, compliance, negligence or liability.
3. **Results are about AIDCF.** Every judgement concerns whether AIDCF's criteria would have surfaced a condition, not whether the operator should have found it. Outputs are worded accordingly.
4. **Minimal quotation.** Paraphrase. Published outputs use at most one short attributed quotation per incident, and only where the exact wording matters. Source reports are not redistributed; outputs link to the source and its archive copy.
5. **Citation.** Every source is cited with URL, access date and archive reference.
6. **Personal data.** Names of individuals in sources are not recorded. Coders are identified by pseudonymous codes; the key is held by the study lead.
7. **Security.** Outputs add no exploitable facility detail beyond what the source published, and aggregate where possible (SECURITY.md).
8. **Legal review.** Before publishing any incident-level output, the sponsor's legal adviser shall review this protocol, the results report and the incident appendix. That review covers, among other things, defamation, copyright and quotation, website terms of use for archiving, and active proceedings (EX-08). This protocol is not legal advice. With that advice, the study lead may decide to notify named operators before publication.

**BT-REQ-017** No incident-level output naming an organisation shall be published until it has been reviewed by the sponsor's legal adviser and the outcome recorded in the run log.

## 18. Records and data management

| Record | Content | Retention |
|---|---|---|
| Run log | Baseline commit hash; frame-freeze date; search log (date, source, query, result count); selection seed and draw; SHA-256 hashes of locked codings; deviations; legal-review outcome | With the results report |
| Coder key and declarations | Coder codes, names, independence and conflict declarations | Study lead only; not published |
| Dossiers | Pre-event dossiers with extractor change logs | With the run log; not published if they reproduce source text beyond fair quotation |
| Source archive references | Archive URLs and access dates | In the register |

Files are UTF-8 CSV with LF line endings. `backtest_check.py --check` validates column order, code values, cross-references and judgement consistency against the baseline files.

**BT-REQ-018** The run log, locked codings and register shall be retained so that an independent reviewer can recompute every published metric from the recorded data and baseline.

---

## Annex A: Method references

- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46.
- Cohen, J. (1968). Weighted kappa: Nominal scale agreement with provision for scaled disagreement or partial credit. *Psychological Bulletin*, 70(4), 213–220.
- Feinstein, A. R., and Cicchetti, D. V. (1990). High agreement but low kappa: I. The problems of two paradoxes. *Journal of Clinical Epidemiology*, 43(6), 543–549.
- Fischhoff, B. (1975). Hindsight ≠ foresight: The effect of outcome knowledge on judgment under uncertainty. *Journal of Experimental Psychology: Human Perception and Performance*, 1(3), 288–299.
- Krippendorff, K. (2004). *Content Analysis: An Introduction to Its Methodology* (2nd ed.). Sage.
- Landis, J. R., and Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174.
- Page, M. J., et al. (2021). The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*, 372, n71.
- Wilson, E. B. (1927). Probable inference, the law of succession, and statistical inference. *Journal of the American Statistical Association*, 22(158), 209–212.

## Annex B: Framework artefacts used

| Artefact | Used for |
|---|---|
| `foundations/threat-model/AIDCF-004_Threat_Hazard_and_Failure_Model_v1.1.md` | Cause families (Part VI), generic modes (Part VII), scenario families (Part XIII), library scenarios X01–X20 (Part XIV), failure modes (Appendix A) |
| `registries/controls/controls.csv`, `standards/aidcf-007a/registry/controls/` | Control IDs, objectives, requirements, assessment criteria |
| `registries/controls/evidence-profiles.csv` | Mandatory items, required classes, state and period coverage, reassessment triggers |
| `registries/controls/gate-mappings.csv` | Candidate gates and CRITICAL/SUPPORTING roles |
| `registries/gates/critical-gates.csv`, `critical-gate-criteria.csv` | Gate scope, evidence floors, approved-NA conditions, gate criteria |
| `registries/vocabularies/control-results.csv`, `gate-results.csv`, `confidence.csv` | Canonical result and confidence codes |
| CONTRIBUTING.md §5, §8; GOVERNANCE.md §8–§11 | Finding fields, change classes, approval thresholds |
