# What AIDCF would have flagged: three public incidents

| Field | Value |
|---|---|
| Status | Illustrative, draft for the owner's review. **Not back-test results.** |
| Date | 2026-10-13 |
| Prepared by | AI research assistant (Claude), screener code C90, at the framework author's request |
| Framework version used | AIDCF-007A registry v1.1 (`registries/controls/`), gates in `registries/gates/`, AIDCF-004 v1.1 |
| Method | The AIDCF-VAL-001 coding logic (protocol sections 8 to 11), applied by one coder, without a second coder or adjudication |

## Read this first

These three write-ups show *how* AIDCF is applied to a real incident. They do not measure *how well* it works. They differ from a VAL-001 back-test in five ways, and each one weakens what they can show:

1. **One coder, not independent.** The coder works for the framework author and is the frame's screener (C90). The protocol bars C90 from coding. Nobody checked these judgements independently.
2. **Hindsight.** Each source was read in full before the factors were written down (coding phase POST_REVEAL). Prior familiarity is DETAILED for INC-040 and INC-068, both widely discussed, and GENERAL for INC-120.
3. **No comparison.** None of the conventional review methods (BL-ENG, BL-CX, BL-OT) was applied. A good result here does not mean AIDCF beats them.
4. **Scope stretch.** AIDCF assesses AI data-centre capabilities. These incidents happened in a cloud identity platform, a global backbone and a telecom voice network. AIDCF reaches them only through its network, dependency, security and operations controls.
5. **Three incidents are an anecdote, not a sample.** No rate or percentage below generalises.

The wording rule is fixed: **"AIDCF would have flagged"** means an assessment would have surfaced the condition before the event. It never means the incident would have been prevented. AIDCF-004 §7 separates detection from prevention.

## How the three were chosen

The incidents were drawn before any mapping, by a rule written down first:

- **Pool:** the 92 incidents in `incident-register.csv` that are ELIGIBLE, have detail HIGH and have a PRIMARY or REGULATOR source.
- **Draw:** the pool was sorted by ID and shuffled with `random.Random(20261013)`. The first three that repeat no failure category, no operator and no operator type were taken.
- **Recusal:** draw rank 2, INC-175, is an Anthropic incident. Anthropic makes the model that prepared this document, so that incident was recused and the draw continued.
- **Result:** INC-040 (rank 1), INC-068 (rank 3) and INC-120 (rank 7). Ranks 4 to 6 repeated a category or an operator type.

| Incident | Date | Operator | Type | Failure category |
|---|---|---|---|---|
| INC-040 | 2020-12-14 | Google Cloud | Hyperscale cloud | Control plane |
| INC-068 | 2021-10-04 | Meta | Enterprise | Change and human action |
| INC-120 | 2024-10-08 | Singtel | Telecom network | Network |

The draw and the recusal are recorded in `run-log/run-log.md`.

## Summary

| | INC-040 Google | INC-068 Meta | INC-120 Singtel |
|---|---|---|---|
| Pre-event causal factors | 4 | 5, plus 1 safeguard that worked | 3 |
| Flagged in full (DETECTED) | 1 | 1 | 0 |
| Flagged in part (PARTIALLY_DETECTED) | 2 | 4 | 2 |
| Missed although a control covers it (NOT_DETECTED) | 0 | 0 | 1 |
| Source too thin to judge | 1 | 0 | 0 |
| Projected gate FAIL | CG-15 | CG-10 | none |
| Projected false reassurance or no gate signal | none | CG-14 likely PASS | no gate engaged (gap G4) |
| Framework gaps found | 0 | 2 | 3 |

**The case for AIDCF.** In two of the three incidents, a specific critical gate would have failed on the condition that later caused the outage:
- **INC-040:** CG-15 fails because nothing limited how far an automation could cut a critical service's quota.
- **INC-068:** CG-10 fails because the out-of-band network depended on the network it was meant to recover.

**The case against.** In INC-120, AIDCF as written would give no gate-level warning: the controls it engages only support CG-08, and CG-08's critical controls are about AI fabrics. In INC-068, CG-14 would likely pass although one command could take out the backbone. That is false reassurance, the result the back-test is designed to catch. The five gaps below are concrete fixes to the framework. Finding and fixing such gaps is part of the value of back-testing, and only the full back-test can show how often they occur.

---

## INC-040: Google authentication outage, 14 December 2020

**Source:** Google Cloud incident report 20013, <https://status.cloud.google.com/incident/zall/20013> (PRIMARY).

**What happened.** For about 47 minutes, Google services that required Google OAuth sign-in failed. The User ID Service was being migrated to a new quota system. Parts of the old system were left in place and "incorrectly reported the usage for the User ID Service as 0". When a grace period expired, this triggered "automated quota systems to decrease the quota allowed for the User ID service". Its database could no longer accept writes, and authentication lookups failed. Google's existing safety checks "did not cover the scenario of zero reported load for a single service". Cloud Support's own tools were also affected, "which delayed our ability to share outage communications".

**Path.** This follows AIDCF-004 **X18** (a telemetry defect leads an automation to take a mass action) into **X15** (identity service failure).

| # | Pre-event condition | Role | Knowable? | AIDCF control and criterion | Judgement | Projected result |
|---|---|---|---|---|---|---|
| CF-01 | A migration left the old quota system reporting zero usage for a critical service, from October onwards | Predisposing | DISCOVERABLE | MCF-CAP-023 C3: post-change validation confirmed before closure | PARTIALLY_DETECTED: change records are sampled, so detection depends on this migration being picked (test D2 fails) | CONFORMING if not sampled |
| CF-02 | Automated quota enforcement could cut a critical service's quota below real use, across all data centres at once, with no check for an implausible zero reading | Escalation | DISCOVERABLE | **MCF-SEC-021 C3**: rate and magnitude limits enforced technically. C6: the link from telemetry to command is analysed for sensor trust. The authority register is mandatory evidence. | **DETECTED** | PARTIAL |
| CF-03 | Nearly every authenticated service depended on one identity service whose quota could change in a single global action | Dependency | DISCOVERABLE | MCF-RES-007 C3: blast-radius analysis covers common-mode cases, naming identity and automation | INSUFFICIENT_INFORMATION: the source does not say whether such an analysis existed or what it said | none |
| CF-04 | The tools used to tell customers about outages depended on the failing service | Recovery | DISCOVERABLE | MCF-DEP-004 C3: recovery dependencies are checked for a shared fault domain with the failure they recover from | PARTIALLY_DETECTED: the criterion covers recovery of Required Functions; customer communications sit at its edge | PARTIAL |

**Gates.**
- **CG-15 (integrated digital authority): FAIL.** MCF-SEC-021 is CRITICAL for CG-15, and a PARTIAL CRITICAL control fails the gate under the SPEC 6.2 roll-up. The evidence profile adds: "CG-15 cannot PASS while any automation … with consequential infrastructure authority is unregistered or unreconciled".
- **CG-14 (change control): INSUFFICIENT_INFORMATION.**

**What AIDCF would have flagged:** an automation with authority to remove a critical service's capacity everywhere at once, with no magnitude limit and no check that its input was plausible. **What it would not:** whether this particular migration was left half-finished. That depends on sampling.

---

## INC-068: Meta global outage, 4 October 2021

**Source:** Meta engineering, "More details about the October 4 outage", <https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/> (PRIMARY).

**What happened.**
- During routine maintenance, a command meant to assess global backbone capacity disconnected every backbone link. An audit tool should have stopped it, "but a bug in that audit tool prevented it from properly stopping the command."
- DNS servers withdraw their routes when they lose contact with the data centres. They therefore removed themselves from the internet while still running.
- "Our primary and out-of-band network access was down", so engineers had to travel to the sites, and deliberately strict physical security slowed them.
- Bringing load back carried its own risk: "suddenly reversing such a dip in power consumption could put everything from electrical systems to caches at risk." Meta staged the restart using practice from its "storm" drills. It noted that "we've never previously run a storm that simulated our global backbone being taken offline".

**Path.** No AIDCF-004 library scenario fits: see gap G6 below. The recovery phase follows the circular-recovery step of **X15**.

| # | Pre-event condition | Role | Knowable? | AIDCF control and criterion | Judgement | Projected result |
|---|---|---|---|---|---|---|
| CF-01 | One maintenance command could take down every backbone link at once, and the guard meant to block it had a defect | Escalation | DISCOVERABLE that the command was possible; NOT_STATED whether the defect was known | MCF-NET-022: "no single change can be applied simultaneously … to all planes". C4 checks only changes already made. MCF-SEC-022 C4: tests confirm the approval guard cannot be bypassed. | PARTIALLY_DETECTED: NET-022 C4, read literally, passes because no such change had happened. SEC-022 would find the bug only if its tests included this command (D2 fails). | CONFORMING |
| CF-02 | The DNS health safeguard withdrew routes whenever its site lost the backbone, so a global network loss removed healthy DNS everywhere | Escalation | DISCOVERABLE | MCF-NET-024 C3: circular dependencies between DNS and the systems it supports are documented and broken. MCF-DEP-006 C5: automation with authority over more than one redundant member is recorded. | PARTIALLY_DETECTED: the dependency would surface, but neither criterion asks what the safeguard does when every site trips at once | PARTIAL |
| CF-03 | Out-of-band access depended on the same network it was meant to recover | Recovery | DISCOVERABLE | **MCF-NET-015 C2**: OOB does not depend on the production fabric or primary WAN. C4: a test with those unavailable. The OOB dependency analysis and isolation test record are mandatory evidence. | **DETECTED** | NONCONFORMING |
| CF-04 | On-site recovery depended on staff passing strict physical security | Recovery | STATED_KNOWN (a deliberate trade-off) | MCF-DEP-004 C1: the recovery dependency map includes specialist labour | PARTIALLY_DETECTED: the map records the dependency but does not time it against the recovery tolerance | PARTIAL |
| CF-05 | A global backbone loss had never been exercised | Predisposing | STATED_KNOWN | MCF-RES-003 C2 and C3: applicable X01 to X20 scenarios and compound scenarios are in the scenario library | PARTIALLY_DETECTED: C2 is met because no library scenario covers this case (gap G6) | PARTIAL |
| (safeguard) | Load was restored in stages to protect electrical systems, as practised in drills | Recovery | STATED_KNOWN | MCF-CAP-016 C2 and C3: restart inrush is modelled and a staging plan exists | AIDCF would credit this | CONFORMING |

**Gates.**
- **CG-10 (recovery readiness): FAIL.** MCF-NET-015 is CRITICAL for CG-10, and its profile states "CG-10 cannot PASS while OOB independence from the systems it recovers is unverified".
- **CG-14 (change control): likely PASS, which is false reassurance.** Its CRITICAL controls read on past change records, and none of them shows the single global command was possible.

**Gaps found.**
- **G2 (MCF-NET-022):** C4 checks history only. Proposed criterion: *"A test or configuration review shows that a single command or change cannot be applied to all planes, or both members of a redundant pair, without a second approval enforced outside the tool that issues it."*
- **G6 (AIDCF-004):** no library scenario covers a single management action that severs all inter-site connectivity, including out-of-band, and turns health safeguards into a global withdrawal. Proposed X21: *"Management-plane action isolates all sites."*

**What AIDCF would have flagged:** that recovery depended on the network being recovered, which fails CG-10. **What it would not, as written:** that one command could take out the whole backbone.

---

## INC-120: Singtel fixed-line voice outage, 8 October 2024

**Source:** IMDA press release on the S$1 million penalty, <https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2025/imda-fined-singtel-for-fixed-voice-disruption> (REGULATOR). The parliamentary answer at <https://mddi.gov.sg/media-centre/parliament/pqs-related-to-the-8-october-singtel-disruption> gives no further cause detail.

**What happened.**
- For more than four hours, about 500,000 fixed-line users lost voice service, including access to emergency lines.
- A traffic surge hit a monitoring system's virtualised firewall, which "did not have adequate filters installed to protect the hardware against high intensity traffic". That firewall and the voice system's firewall "shared the same hardware memory resources", so the voice firewall began to malfunction intermittently.
- Failover to the second exchange did not complete: "Calls were dropped intermittently as voice traffic alternated between the affected and unaffected voice systems."
- IMDA found the incident "within Singtel's control to prevent". Singtel separated the hardware and added a mechanism to stop traffic alternating during failover.

**Path.** This follows the AIDCF-004 family *DEP: Hidden shared dependency*. The nearest library scenario, X11, is the electrical version of it.

| # | Pre-event condition | Role | Knowable? | AIDCF control and criterion | Judgement | Projected result |
|---|---|---|---|---|---|---|
| CF-01 | The voice firewall shared host memory with a non-critical monitoring firewall | Predisposing | DISCOVERABLE (configuration) | MCF-DEP-002 C1: the upstream dependency graph covers all dependency classes, including capacity. MCF-RES-005 C3: overlaps between fault domains are recorded. | PARTIALLY_DETECTED: shared virtualisation resources are not named by any criterion, so finding this depends on the assessor's reading | CONFORMING |
| CF-02 | The monitoring firewall had no filtering for high-intensity traffic | Predisposing | DISCOVERABLE | MCF-NET-011 C2: capacity thresholds are defined for in-path firewalls | PARTIALLY_DETECTED: the monitoring system is outside the assessed service unless CF-01 brings it in | CONFORMING |
| CF-03 | Failover had no protection against an intermittently failing primary, so traffic alternated between exchanges | Escalation | DISCOVERABLE (the guard was added afterwards) | MCF-NET-011 C3: failover behaviour is understood. C5: failover is tested within tolerance. | **NOT_DETECTED**: a clean failover test passes, and no criterion requires testing a partial or intermittent failure | CONFORMING |

**Gates.** **No gate would FAIL, and none gets a clear signal.** MCF-NET-011 is only SUPPORTING for CG-08. CG-08's CRITICAL controls (MCF-NET-001, -007, -008, -009 and the compute and storage controls) concern AI fabrics and are not engaged by this incident. CG-03 (dependency visibility) would depend on how the assessor read CF-01.

**Gaps found.**
- **G2 (MCF-DEP-002 or MCF-RES-005):** proposed criterion: *"Critical functions hosted on shared compute or virtualisation platforms are shown to be isolated (memory, CPU and I/O) from non-critical workloads, or the shared resource is recorded as a fault domain."*
- **G2 (MCF-NET-011, and by extension MCF-RES-017):** proposed criterion: *"Failover tests include a partial or intermittent failure of the active member, and show that failover completes without oscillation."*
- **G4 (gate mapping):** in-path gateways and their failover (MCF-NET-011) carry inference and service availability but are not CRITICAL for any gate. Proposed: make MCF-NET-011 CRITICAL for CG-08, or add an inference-path criterion to CG-08.

**What AIDCF would have flagged:** possibly the shared hardware, if the assessor traced dependencies down to the host. **What it would not, as written:** failover flapping under a partial failure, or any gate-level warning.

---

## What this shows, and what it does not

- **It shows the method end to end.** Conditions are taken from the operator's or regulator's own words. Each one is tied to a named control criterion and its mandatory evidence, then rolled up to a gate. Anyone can check every step against the cited source and registry row.
- **It shows that AIDCF can point at the specific gap,** not a general "resilience" concern, in two of three cases.
- **It shows that AIDCF misses things.** The five gaps above are framework fixes. They should go through CONTRIBUTING §5 as findings rather than be patched quietly.
- **It does not show a detection rate,** and it does not show that AIDCF beats existing practice. Only the VAL-001 back-test, with two independent coders, the seeded stratified draw and the BL-ANY-3 comparison, can support those claims.

## Effect on the back-test

INC-040, INC-068 and INC-120 are still ELIGIBLE in the frame. Because this mapping is now in the repository, any coder who reads it has DETAILED familiarity with them. The protocol already reports DETAILED codings separately. The owner should still decide one of two options before the selection draw:

1. Leave them in the frame and rely on that separate reporting.
2. Record them as a protocol deviation and exclude them from selection.
