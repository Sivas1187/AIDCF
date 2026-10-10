# AIDCF-018-GOV Governance, Accountability and Assurance Direction Domain Guide

## Document control

| Field | Value |
|---|---|
| Document ID | AIDCF-018-GOV |
| Title | Governance, Accountability and Assurance Direction Domain Guide |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Parent artifact | AIDCF-018 Domain Guides |
| Normative basis | AIDCF-007A (controls MCF-GOV-001 to MCF-GOV-024), AIDCF-006, AIDCF-008, AIDCF-010, AIDCF-011, AIDCF-012 |
| Requirement prefix | DG-GOV-REQ-NNN |

### Revision history

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-10-10 | Initial issue: domain guide aligned to the rewritten GOV controls and the control-level gate mappings of AIDCF-010. |

**Normative status.** This guide is informative except for the requirements labelled DG-GOV-REQ-NNN. The normative control requirements remain those in the AIDCF-007A registry; where this guide restates them it does so for explanation, and the registry prevails if they differ. Normative keywords follow ISO/IEC Directives Part 2 usage (shall, should, may, can).

## 1 Purpose and scope

The GOV domain answers one question for every assurance conclusion about an AI data centre capability: *who had the authority to direct the assurance, to own the risk, to decide, and to be held to account, and did that authority work as designed?* It contains 24 controls in six families:

| Family | Name | Controls |
|---|---|---|
| GOV-01 | Governance architecture | MCF-GOV-001 to 004 |
| GOV-02 | Accountability and responsibility | MCF-GOV-005 to 008 |
| GOV-03 | Policy and standards management | MCF-GOV-009 to 012 |
| GOV-04 | Risk and assurance governance | MCF-GOV-013 to 016 |
| GOV-05 | Stakeholder and regulatory interface | MCF-GOV-017 to 020 |
| GOV-06 | Ethics, impartiality and competence | MCF-GOV-021 to 024 |

**In scope.** The governance charter and decision rights of the assurance programme; accountability for Capability Instances, Required Functions and material Dependencies; risk-acceptance authority; custody accountability for evidence; the policy and technical-standards hierarchy; exception governance; assurance planning, risk-appetite linkage and gate governance; independent review; obligations to stakeholders, regulators and customers; external communication of conclusions; conflicts of interest, assessor independence, competence and appeals.

**Out of scope.** The engineering adequacy of power, cooling, compute, storage, network and control systems (POW, THM, CMP, STO, NET, SEC); the definition of Capability Instances and Service Outcomes themselves (CAP); the mechanics of evidence quality, sampling, UNKNOWN handling and gate computation (EVA); operational service management processes such as change execution and incident handling (OPS); provider-side governance, which is assessed through SUP controls.

**Boundary with other domains.** GOV owns *authority and accountability*; CAP owns *what is being assured*; EVA owns *how the assurance is evidenced and computed*. A useful test: if the failure is "the right person never decided", it is GOV; if it is "nobody defined what the capability must achieve", it is CAP; if it is "the evidence or the computation was wrong", it is EVA. Where two domains touch the same artefact (for example the gate register is governed in MCF-GOV-015 and populated in MCF-EVA-017 and MCF-EVA-018), the GOV control assesses that governance operates, and the EVA control assesses that the content is correct.

## 2 Why this domain matters for AI capability

Traditional data-centre governance was built around a relatively stable facility serving many heterogeneous IT loads, with facility management, IT operations and customers separated by long-standing contracts and service catalogues. AI capability changes the governance problem in five ways.

1. **The unit of value is a capability, not a building.** A training cluster or inference pool is a tightly coupled system of accelerators, fabric, storage, liquid cooling and power that delivers value only as a whole. Accountability split along traditional facility/IT lines leaves the interfaces — facility water serving cold plates, power capping at rack level, the scheduler's response to thermal throttling — without an owner. MCF-GOV-006 therefore requires a single accountable owner for every Required Function and material Dependency, and MCF-CAP-002 requires a single capability owner with authority over both facility and platform resources.
2. **Decisions must be taken faster and under tighter margins.** Liquid-cooled racks at high density can have very short thermal ride-through on loss of facility water (validated per instance under MCF-CAP-019), and synchronous training produces load steps that interact with UPS and generation. Decisions such as curtailing AI load, aborting a test or entering a degraded state may need to be taken in minutes, often out of hours. MCF-GOV-002 requires emergency decision rights that are defined, delegated and usable.
3. **Multi-party control is the norm.** AI capacity is frequently delivered through colocation, GPU-as-a-service, sovereign or shared facilities, joint ventures and OEM-managed platforms. Responsibility clauses in contracts frequently diverge from what operators believe. MCF-GOV-005 reconciles the RACI to contractual responsibility clauses.
4. **Change is continuous.** Accelerator generations, rack densities and cooling technologies change on short cycles, so standards baselines, exceptions and assurance plans age quickly. MCF-GOV-010, MCF-GOV-011 and MCF-GOV-013 make the baseline, deviations and plan explicit and versioned.
5. **Assurance conclusions are increasingly relied upon externally** — by customers placing large training commitments, financiers, insurers and regulators of critical infrastructure. The governance of what is said externally (MCF-GOV-020), by whom (MCF-GOV-022) and after what challenge (MCF-GOV-016) determines whether reliance is defensible.

In short, GOV does not make the infrastructure more resilient by itself; it makes the assurance about the infrastructure *answerable*. Without it, CG-13 (Responsibility and authority) cannot pass and no Assurance Decision has an accountable issuer.

## 3 Reference patterns and variants

| Pattern | Description | Governance implications |
|---|---|---|
| G-P1 Single-owner enterprise | One organisation owns facility, platform and AI workloads | RACI is internal; the main risk is facility/IT split inside the organisation; emergency rights must cross that split |
| G-P2 Colocation tenant | Tenant owns accelerators, fabric and storage; provider owns building, power and often cooling plant | Capability owner sits in the tenant; provider contract defines who may curtail load, change setpoints, and notify of change; MCF-GOV-005 and MCF-GOV-006 depend on contract access |
| G-P3 Capacity-as-a-service | Provider owns and operates the full stack; customer consumes accelerators | Customer governance focuses on commitments (MCF-GOV-019) and reliance on provider assurance; provider internal governance assessed through SUP |
| G-P4 Shared or sovereign facility | Multiple tenants or public-interest users on shared infrastructure | Priority classification and conflicts between tenants become governance decisions; stakeholder obligations (MCF-GOV-017) are broad |
| G-P5 Joint venture or build-operate-transfer | Ownership and operation change over the lifecycle | Decision rights and charter must anticipate transfer; MCF-GOV-001 triggers on change of ownership |

Assurance programme variants (AIDCF-011): self-assessment, co-sourced, second-party and independent provider. The variant sets the independence level required by MCF-GOV-022 and the review arrangements in MCF-GOV-016.

## 4 Required functions and capability linkage

GOV controls do not implement physical Required Functions; they implement the governance functions on which every Required Function's assurance depends. In the 16-step chain (AIDCF-002), GOV acts at:

- **Step 1 Decision Question** — authority to pose and approve the question (MCF-GOV-001, MCF-GOV-002), linked to MCF-EVA-009.
- **Steps 2–4 Capability Instance, Service Outcome, Required Function** — accountable ownership (MCF-GOV-005, MCF-GOV-006, MCF-CAP-002) and the obligations that shape outcomes (MCF-GOV-017, MCF-GOV-019).
- **Step 6 Dependency and Fault Domain** — accountable owners for material dependencies (MCF-GOV-006), which supports CG-03.
- **Steps 12–14 Control Assessment, Finding/UNKNOWN Record, Gate Result** — gate governance (MCF-GOV-015), oversight (MCF-GOV-003), risk acceptance (MCF-GOV-007).
- **Step 16 Assurance Decision** — independence, review, external reporting and challenge (MCF-GOV-016, MCF-GOV-020 to MCF-GOV-024).

Governance functions every in-scope Capability Instance requires:

| Governance function | Delivered by |
|---|---|
| Direct the assurance programme | MCF-GOV-001, MCF-GOV-013 |
| Allocate and exercise decision rights, including in emergency | MCF-GOV-002 |
| Own capability, functions and dependencies | MCF-GOV-005, MCF-GOV-006 |
| Accept residual risk within appetite | MCF-GOV-007, MCF-GOV-014 |
| Control policy, standards, documents and deviations | MCF-GOV-009 to MCF-GOV-012 |
| Oversee gates and challenge conclusions | MCF-GOV-003, MCF-GOV-015, MCF-GOV-016, MCF-GOV-024 |
| Interface with stakeholders and regulators | MCF-GOV-017 to MCF-GOV-020 |
| Keep assessors impartial and competent | MCF-GOV-021 to MCF-GOV-023 |

## 5 Dependencies, fault domains, common-mode concerns

Governance has fault domains just as infrastructure does. The common-mode concerns assessors should look for are:

- **Single-person dependency.** One individual holding the capability-owner role, the emergency decision right and the risk-acceptance authority. Absence of that person disables all three. MCF-GOV-002 and MCF-CAP-002 require named deputies for EMERGENCY and RECOVERY.
- **Shared reporting line.** The assessment team, the operations function and the decision authority reporting to the same executive whose objectives depend on a favourable conclusion. This is a common-mode threat to independence (MCF-GOV-022) and to review (MCF-GOV-016).
- **Shared tooling.** Change, exception, risk and decision workflows hosted on one platform with one administrator group. A misconfiguration of approver roles affects every decision class at once; MCF-GOV-002 tests the configuration directly.
- **Contract dependency.** Authority over facility resources held only through a provider contract the capability owner cannot see. MCF-GOV-005 records this as a U2 UNKNOWN rather than presuming the provider is responsible.
- **Methodology dependency.** All results depend on one methodology baseline and one tool configuration; if they diverge from the declared versions, every result is affected (MCF-GOV-004).

Governance dependencies on other domains: GOV relies on CAP for the capability register and outcome definitions that charters and RACIs reference, on EVA for the gate register content, and on OPS for change and incident records that feed exception and regulatory processes.

## 6 Threats, hazards and failure scenarios with propagation paths to Service Outcomes

| ID | Scenario | Propagation path | Service Outcome effect | Primary GOV safeguards |
|---|---|---|---|---|
| GOV-FS-01 | Out-of-hours facility water temperature excursion; no one present holds authority to curtail AI load | Excursion → accelerators throttle then trip → operator waits for authority → thermal limit exceeded across a pod | Performance and availability outcomes breached; potential hardware damage | MCF-GOV-002, MCF-GOV-006, MCF-CAP-002 |
| GOV-FS-02 | Provider changes facility water setpoint for efficiency; contract silent on notification | Setpoint change → reduced thermal margin → throttling under peak load | Performance outcome degraded; prior CG-06 evidence invalid | MCF-GOV-005, MCF-GOV-017, MCF-GOV-011 |
| GOV-FS-03 | Temporary bypass of a leak-detection interlock approved as an exception and never expired | Interlock bypassed → leak undetected → water reaches electrical equipment | Availability, integrity and safety outcomes | MCF-GOV-011, MCF-GOV-007 |
| GOV-FS-04 | Gate FAIL on CG-10 reported only as a domain score of 78 | Score presented → committee sees "substantial" → customer commitment made on unrecoverable capability | Recovery outcome commitment exceeds capability | MCF-GOV-015, MCF-GOV-003, MCF-GOV-019 |
| GOV-FS-05 | Assessor previously designed the CDU failover scheme assesses it | Self-review → design weakness not challenged → untested failover relied on | Recovery and availability outcomes | MCF-GOV-021, MCF-GOV-022, MCF-GOV-016 |
| GOV-FS-06 | Decision statement published as "AIDCF certified" | Prohibited claim → external reliance beyond scope → suspension not communicated | Reliance on outcomes not assured | MCF-GOV-020 |
| GOV-FS-07 | Risk accepted by an operations manager for a known single point of failure in the fabric spine | Unauthorised acceptance → no investment → spine failure partitions training job | Performance and availability outcomes | MCF-GOV-007, MCF-GOV-014 |

Each scenario is a defeater (AIDCF-002 step 7 at the governance level): it does not originate in the infrastructure, but it removes the safeguard that should have contained an infrastructure failure.

## 7 Safeguards

Safeguards in GOV are organisational mechanisms; each maps to the control that assesses it.

- **Approved charter and decision-rights matrix enforced in workflow tools** (MCF-GOV-001, MCF-GOV-002). Enforcement in the tool, not just in a document, is what turns a directive control into a preventive one.
- **Single accountable owner per Required Function and material Dependency, with counterparty contacts** (MCF-GOV-006).
- **Time-bound risk acceptance and exceptions with expiry and escalation** (MCF-GOV-007, MCF-GOV-011).
- **Gate register with reproducible roll-up and no edits outside reassessment** (MCF-GOV-015).
- **Independent review with authority to withhold concurrence, tested by seeded-defect exercises** (MCF-GOV-016).
- **Controlled external statements, approved by the decision authority, corrected on suspension** (MCF-GOV-020).
- **Declarations of interest, cooling-off periods and prohibition of outcome-contingent fees** (MCF-GOV-021).
- **Competence register matched to assignment, with specialist reliance recorded** (MCF-GOV-023).
- **Appeals that preserve the original record** (MCF-GOV-024).

Defence diversity (APS-024) applies: the committee (MCF-GOV-003), the independent reviewer (MCF-GOV-016) and the decision authority (MCF-EVA-019) should be different people, so that a single blind spot does not pass all three.

## 8 Critical-gate linkage

GOV is the principal contributor of CRITICAL controls to CG-13 (Responsibility and authority). Under the AIDCF-010 roll-up rule, CG-13 cannot PASS unless each in-scope CRITICAL control below is CONFORMING at its required claim type; a PARTIAL result on any of them yields FAIL.

| Gate | CRITICAL controls in this domain | SUPPORTING controls in this domain |
|---|---|---|
| CG-01 | — | MCF-GOV-017, MCF-GOV-019 |
| CG-03 | — | MCF-GOV-006 |
| CG-13 | MCF-GOV-002 Decision Rights (IMPLEMENTATION)<br>MCF-GOV-005 RACI and Role Ownership (IMPLEMENTATION)<br>MCF-GOV-006 Critical Function Accountability (IMPLEMENTATION)<br>MCF-GOV-007 Risk Acceptance Authority (OPERATION) | MCF-GOV-001, MCF-GOV-003, MCF-GOV-008, MCF-GOV-011, MCF-GOV-015, MCF-GOV-016, MCF-GOV-022 |
| CG-14 | — | MCF-GOV-010, MCF-GOV-011, MCF-GOV-012, MCF-GOV-018 |

Notes on the mapping:

- **Why these four GOV controls are CRITICAL for CG-13.** Decision rights (MCF-GOV-002), the RACI (MCF-GOV-005), function and dependency ownership (MCF-GOV-006) and risk-acceptance authority (MCF-GOV-007) together define and evidence that every critical function has an accountable owner with authority. If any one is not met, the CG-13 scope is directly defeated. MCF-CAP-002 (Capability Ownership) is the fifth CRITICAL control for CG-13, held in CAP.
- **Why the charter is SUPPORTING.** A missing charter weakens the programme but does not by itself leave a function unowned; its effect is evaluated at gate level.
- **CG-14.** GOV contributes SUPPORTING controls only (baseline, exceptions, documents, regulatory change). The CRITICAL change-control controls sit in CAP (MCF-CAP-023) and OPS.
- **CG-01.** Stakeholder obligations and customer commitments shape Service Outcomes and are SUPPORTING; the CRITICAL controls are in CAP and EVA.
- **CG-11 and CG-12** are meta-gates evaluated across all controls and are not mapped per control. GOV contributes to them indirectly through evidence custody (MCF-GOV-008) and oversight of UNKNOWN Records (MCF-GOV-003).

## 9 Capability-profile parameters

All defaults are illustrative and shall be replaced by values approved in the capability profile. They express programme cadence and governance tolerances; they are not engineering limits.

| Control | Parameter | Unit | Illustrative default | Basis |
|---|---|---|---|---|
| MCF-GOV-001 | Governance charter review interval | months | 12 | Capability-profile parameter set by the governing body; illustrative, shortened where the capability is changing rapidly |
| MCF-GOV-002 | Decision sample size per decision class | records | 10 or the full population if smaller | Judgemental sample per AIDCF-008 sampling principles; illustrative, increased if exceptions are found |
| MCF-GOV-003 | Oversight meeting interval | months | 3 | Capability-profile parameter; illustrative, shortened during build, major change or after a gate FAIL |
| MCF-GOV-003 | Out-of-cycle notification time for gate FAIL or US4/US5 UNKNOWN | working days | 5 | Capability-profile parameter; illustrative |
| MCF-GOV-005 | RACI reconciliation interval | months | 6 | Capability-profile parameter; illustrative |
| MCF-GOV-007 | Maximum risk-acceptance validity | months | 12 | Capability-profile parameter; illustrative, shorter for acceptances touching gate-critical controls |
| MCF-GOV-011 | Maximum exception duration | months | 6 | Capability-profile parameter; illustrative, renewable once by the approver |
| MCF-GOV-012 | Runbook review interval | months | 12 | Capability-profile parameter; illustrative, shorter for emergency runbooks after change |
| MCF-GOV-013 | Assurance planning period | months | 12 | Programme parameter; illustrative |
| MCF-GOV-016 | Review effectiveness test frequency | tests per year | 1 | Programme parameter; illustrative |
| MCF-GOV-018 | Regulatory escalation time for safety or reporting-duty changes | working days | 10 | Programme parameter; illustrative |
| MCF-GOV-020 | External correction time after decision suspension | working days | 10 | Programme parameter; illustrative |
| MCF-GOV-021 | Self-review cooling-off period | months | 12 | Programme parameter; illustrative |
| MCF-GOV-023 | Competence currency period | months | 24 | Programme parameter; illustrative, shorter for rapidly changing technologies |

## 10 Evidence expectations by claim type

| Claim type | Controls | Profile tiers | Required classes (union) | Sufficiency floors |
|---|---|---|---|---|
| DESIGN | MCF-GOV-001, MCF-GOV-009, MCF-GOV-013, MCF-GOV-014, MCF-GOV-017 | CP-1 | E1+E6+E7 | S3 |
| IMPLEMENTATION | MCF-GOV-002, MCF-GOV-004, MCF-GOV-005, MCF-GOV-006, MCF-GOV-010, MCF-GOV-012, MCF-GOV-019, MCF-GOV-022 | CP-2 | E1+E2+E3+E6+E7 | S3 |
| OPERATION | MCF-GOV-003, MCF-GOV-007, MCF-GOV-008, MCF-GOV-011, MCF-GOV-015, MCF-GOV-018, MCF-GOV-020, MCF-GOV-021, MCF-GOV-023, MCF-GOV-024 | CP-3 | E1+E2+E3+E6+E7 | S4 |
| EFFECTIVENESS | MCF-GOV-016 | CP-4 | E1+E3+E4 | S4 |

Expectations by claim type for governance controls:

- **DESIGN (AL2).** Approved documents (E1) with an accountable approval from a source separate from the author, and current applicability. Examples: the charter and its governing-body resolution; the risk appetite statement. Interviews (E6) explain intent but do not substitute for approval evidence.
- **IMPLEMENTATION (AL3).** Evidence that the design is actually in force: workflow configuration exports showing approver roles (E2), reconciliations of named roles to appointments and contracts (E7), and interviews with role holders (E6). The characteristic weakness is a RACI that is approved but not reconciled to contracts; that yields PARTIAL, not CONFORMING.
- **OPERATION (AL4).** Records over a representative period (E3): minutes across at least four meeting cycles, risk acceptances active over twelve months, exceptions and their expiries, declarations dated before assignment. Samples shall be drawn by the assessor from full registers.
- **EFFECTIVENESS (AL5).** Only MCF-GOV-016 (Independent Review) is assessed at EFFECTIVENESS: evidence that review *detects* defects, from seeded-defect tests or reperformance (E4), not merely that review records exist.

Governance evidence is often confidential (board papers, contracts, personal declarations). Restriction is handled under AIDCF-008: the evidence lead records what was restricted, and restricted evidence that cannot be inspected becomes a U2 UNKNOWN rather than an assumed pass.

## 11 Assessment guidance

**Sequence.** Assess GOV early, because its results gate the reliability of everything else.

1. Charter, decision question authority and programme model (MCF-GOV-001, with MCF-EVA-009).
2. Ownership chain: capability owner (MCF-CAP-002), RACI (MCF-GOV-005), function and dependency ownership (MCF-GOV-006), decision rights (MCF-GOV-002).
3. Independence, conflicts and competence of the assessment team itself (MCF-GOV-021 to MCF-GOV-023) — before fieldwork relies on that team.
4. Policy, baseline and exceptions (MCF-GOV-009 to MCF-GOV-012), feeding the domain assessments.
5. Risk appetite, risk acceptance and plan (MCF-GOV-013, MCF-GOV-014, MCF-GOV-007).
6. After domain fieldwork: gate governance, oversight, review, external reporting and appeals (MCF-GOV-015, MCF-GOV-003, MCF-GOV-016, MCF-GOV-020, MCF-GOV-024).

**Interviews.** Accountable executive; capability owner and deputy; facility operator duty manager (for emergency rights); provider account or service manager (for contractual responsibility); oversight committee chair and independent member; methodology owner; evidence lead; a sample of assessors (for declarations and competence). Interview the emergency alternate separately from the primary holder.

**Inspections.** Workflow-tool approver configuration (change, exception, risk, decision); document management system status for points of use; assurance graph owner attributes. Extract configuration by query executed or witnessed by the assessor.

**Sampling.** Draw from full registers: decisions per decision class, risk acceptances weighted to gate-critical controls, exceptions, committee meetings, external communications, engagement assignments. The illustrative sample size for decisions is in §9; expand on any nonconformity (MCF-GOV-002 procedure step 6). Judgemental sampling toward high-consequence items is expected and shall not be described as statistical coverage.

**Safe tests.** Governance tests are non-intrusive: reperformance of gate roll-ups (MCF-GOV-015), seeded-defect review tests on copies of closed engagements (MCF-GOV-016), tabletop walkthroughs of emergency decision rights (MCF-GOV-002), verification of counterparty contact routes using agreed non-operational messages (MCF-GOV-006).

**DG-GOV-REQ-001** The assessor shall extract workflow-tool approver configuration, or witness its extraction, for any decision class relied upon for CG-13; screenshots supplied by the approver population shall not be accepted as the sole evidence.

**DG-GOV-REQ-002** The assessment of MCF-GOV-021, MCF-GOV-022 and MCF-GOV-023 shall be performed by a person outside the assessment team whose independence and competence are being assessed.

## 12 Testing safety

GOV assessment involves no hazardous testing. The safety considerations are informational and organisational:

- Emergency decision rights are examined by walkthrough or tabletop; no real emergency is declared and no load is curtailed to test authority.
- Contact-route tests to providers use pre-agreed, clearly labelled non-operational messages; they shall not simulate an incident.
- Seeded-defect review tests use copies of closed engagements with synthetic defects clearly labelled, and are never introduced into live engagements or reports.
- Site visits to control rooms for point-of-use document inspection follow induction and escort rules and do not involve touching operational consoles.
- Board papers, contracts and personal declarations are handled under classification and minimisation rules.

**DG-GOV-REQ-003** No governance test shall cause an operational action (load curtailment, setpoint change, switching, workload pre-emption) or an external notification that could be mistaken for a real event.

## 13 UNKNOWN hot-spots and how to resolve them

| Hot-spot | Typical UNKNOWN type | Severity test outcome | Resolution route |
|---|---|---|---|
| Provider contract responsibility clauses not accessible | U2 Inaccessible | US4 where it concerns a gate-critical function (CG-13) | Negotiate clause-only disclosure under restriction; obtain provider attestation plus counterparty interview; otherwise keep UNKNOWN |
| Approver role configuration not extractable from a SaaS workflow tool | U2 | US4 for CG-13 decision classes | Vendor admin export, audit-log export, or reconciliation of complete approval log to role records |
| Governing-body approval of charter cannot be produced | U1 / U6 | US3 | Secretariat certified extract of the resolution |
| De facto ownership of a shared facility water loop | U9 Interpretation unresolved | US4 | Capability owner and facility operator agree and record a single owner; until then CG-13 UNKNOWN |
| Assessor declarations missing for part of the team | U1 | US3 | Retrospective declaration evaluated by the programme lead; affected results flagged |
| Completeness of external communications register | U5 Coverage gap | US3 | Search of published and submitted material over the period |

Absence of evidence for a governance mechanism is never resolved by interview alone where a record should exist (APS-033 No assumed favourable state).

## 14 Interfaces with other domains

| Domain | Interface | Direction |
|---|---|---|
| CAP | Capability register, capability owner, Service Outcomes, impact tolerances, criticality used by charter, RACI, appetite and plan | CAP → GOV (inputs); GOV → CAP (authority) |
| EVA | Decision question, scope, gate applicability and evidence, UNKNOWN register, decision issue; GOV governs, EVA computes | Bidirectional |
| DEP | Material dependencies requiring owners (MCF-GOV-006) | DEP → GOV |
| OPS | Change, incident and maintenance records feeding exceptions, document lifecycle and regulatory processes | OPS → GOV |
| SUP | Provider governance, contractual responsibilities, provider assurance reliance | SUP ↔ GOV |
| SEC | Authority over identity and privileged access (CG-15) depends on decision rights and RACI | GOV → SEC |
| POW, THM, CMP, STO, NET | Technical standards baseline (MCF-GOV-010); emergency decision rights for load curtailment | GOV → technical domains |
| RES | Emergency and recovery decision rights and deputies | GOV → RES |
| PHY, ENV | Regulatory and permit obligations (planning, water, emissions, safety) | PHY/ENV ↔ GOV |

## 15 Informative references

Document-level references only; no clause-level citation is implied.

- ISO 37000 — Governance of organizations.
- ISO/IEC 38500 — Governance of IT for the organization.
- ISO 31000 — Risk management guidelines; COSO Enterprise Risk Management framework.
- COSO Internal Control — Integrated Framework.
- ISO 37301 — Compliance management systems.
- ISO 9001 — Quality management systems (control of documented information).
- ISO 15489-1 — Records management.
- ISO 19011 — Guidelines for auditing management systems.
- ISAE 3000 — Assurance engagements other than audits or reviews of historical financial information.
- ISO/IEC 17020, ISO/IEC 17021-1, ISO/IEC 17024 — Conformity assessment bodies (impartiality, appeals, competence of persons).
- ISO/IEC 17000 — Conformity assessment vocabulary and general principles.
- Institute of Internal Auditors — Three Lines Model; Global Internal Audit Standards.
- ISO/IEC/IEEE 15026-2 — Assurance case.
- ISO/IEC 20000-1 — Service management system; ISO/IEC 19086 series — Cloud SLA framework.
- ISO/IEC 22237 series and EN 50600 series — Data centre facilities and infrastructures.
- AIDCF-006, AIDCF-008, AIDCF-010, AIDCF-011, AIDCF-012, AIDCF-014.

## 16 Control summary table

| Control ID | Title | Control type | AL | Claim type | Gate mappings |
|---|---|---|---|---|---|
| MCF-GOV-001 | Governance Charter | DIRECTIVE | AL2 | DESIGN | CG-13 SUPPORTING |
| MCF-GOV-002 | Decision Rights | PREVENTIVE | AL3 | IMPLEMENTATION | CG-13 CRITICAL |
| MCF-GOV-003 | Committee Oversight | DETECTIVE | AL4 | OPERATION | CG-13 SUPPORTING |
| MCF-GOV-004 | Methodology Ownership | DIRECTIVE | AL3 | IMPLEMENTATION | — |
| MCF-GOV-005 | RACI and Role Ownership | DIRECTIVE | AL3 | IMPLEMENTATION | CG-13 CRITICAL |
| MCF-GOV-006 | Critical Function Accountability | DIRECTIVE | AL3 | IMPLEMENTATION | CG-13 CRITICAL; CG-03 SUPPORTING |
| MCF-GOV-007 | Risk Acceptance Authority | PREVENTIVE | AL4 | OPERATION | CG-13 CRITICAL |
| MCF-GOV-008 | Evidence Custody | PREVENTIVE | AL4 | OPERATION | CG-13 SUPPORTING |
| MCF-GOV-009 | Policy Hierarchy | DIRECTIVE | AL2 | DESIGN | — |
| MCF-GOV-010 | Technical Standard Baselines | DIRECTIVE | AL3 | IMPLEMENTATION | CG-14 SUPPORTING |
| MCF-GOV-011 | Exception Governance | PREVENTIVE | AL4 | OPERATION | CG-14 SUPPORTING; CG-13 SUPPORTING |
| MCF-GOV-012 | Document Lifecycle | PREVENTIVE | AL3 | IMPLEMENTATION | CG-14 SUPPORTING |
| MCF-GOV-013 | Assurance Plan | DIRECTIVE | AL2 | DESIGN | — |
| MCF-GOV-014 | Risk Appetite Linkage | DIRECTIVE | AL2 | DESIGN | — |
| MCF-GOV-015 | Critical Gate Governance | PREVENTIVE | AL4 | OPERATION | CG-13 SUPPORTING |
| MCF-GOV-016 | Independent Review | DETECTIVE | AL5 | EFFECTIVENESS | CG-13 SUPPORTING |
| MCF-GOV-017 | Stakeholder Obligations | DIRECTIVE | AL2 | DESIGN | CG-01 SUPPORTING |
| MCF-GOV-018 | Regulatory Monitoring | DETECTIVE | AL4 | OPERATION | CG-14 SUPPORTING |
| MCF-GOV-019 | Customer Commitments | PREVENTIVE | AL3 | IMPLEMENTATION | CG-01 SUPPORTING |
| MCF-GOV-020 | External Reporting | PREVENTIVE | AL4 | OPERATION | — |
| MCF-GOV-021 | Conflict Management | PREVENTIVE | AL4 | OPERATION | — |
| MCF-GOV-022 | Assessor Independence | PREVENTIVE | AL3 | IMPLEMENTATION | CG-13 SUPPORTING |
| MCF-GOV-023 | Competence Management | PREVENTIVE | AL4 | OPERATION | — |
| MCF-GOV-024 | Appeal and Challenge | CORRECTIVE | AL4 | OPERATION | — |

## 17 Worked synthetic example

> **SYNTHETIC EXAMPLE.** All names, organisations, values and results below are invented for illustration. They do not describe any real facility, organisation or assessment.

**Context.** Capability Instance SYN-CI-07 "Training Pod Group North" is a liquid-cooled training cluster owned by a synthetic tenant, Example AI Ltd, in a colocation hall operated by Example Colo plc (pattern G-P2). Decision question (approved under MCF-EVA-009): "Can SYN-CI-07 sustain its training availability and performance outcomes within tolerance through loss of one CDU per pod in NORMAL and MAINTENANCE states, as of 2026-09-30, for the tenant's board decision on a 12-month external training commitment?"

**Fieldwork summary (GOV only).**

| Control | Observation | Result |
|---|---|---|
| MCF-GOV-001 | Charter approved by tenant board; covers SYN-CI-07; states non-substitution | CONFORMING (DESIGN) |
| MCF-GOV-002 | Decision-rights matrix exists; emergency curtailment right assigned to tenant duty engineer; workflow tool enforces approver roles; but colocation contract reserves facility-side load-shed decisions to the provider with no defined trigger to call the tenant | PARTIAL (IMPLEMENTATION) |
| MCF-GOV-005 | RACI reconciled to contract in the period; one gap on facility water setpoint changes | PARTIAL (IMPLEMENTATION) |
| MCF-GOV-006 | Every Required Function owned except the shared secondary water loop, recorded as owned by "facilities" in tenant records and by "tenant" in provider records | UNKNOWN (U9), US4 Record raised |
| MCF-GOV-007 | 14 acceptances sampled; all within authority and unexpired | CONFORMING (OPERATION) |
| MCF-CAP-002 | Capability owner appointed with deputy | CONFORMING (IMPLEMENTATION) |

**Gate roll-up for CG-13.** CRITICAL controls: MCF-GOV-002 PARTIAL, MCF-GOV-005 PARTIAL, MCF-GOV-006 UNKNOWN, MCF-GOV-007 CONFORMING, MCF-CAP-002 CONFORMING. Under the AIDCF-010 rule, any CRITICAL control at PARTIAL produces FAIL, which takes precedence over UNKNOWN. **CG-13 = FAIL.**

**Effect on the decision.** CG-13 controls the decision question because the outcome under test (continuity through CDU loss) depends on timely load-shed and setpoint decisions across the tenant/provider boundary. Under AIDCF-012 controlled language a controlling gate FAIL supports NOT_ASSURED for the question as framed. The US4 UNKNOWN Record on the secondary loop is reported separately with its resolution route.

**Findings raised (abridged).**

- F-SYN-07-001 (MCF-GOV-002): no defined trigger or time for the provider to involve the tenant in facility-side load-shed decisions; consequence: AI load may be shed in an order inconsistent with tenant priority classes (MCF-CAP-012).
- F-SYN-07-002 (MCF-GOV-005): facility water setpoint changes have no Responsible party on the tenant side; consequence: changes can erode thermal margin without impact assessment (MCF-CAP-023).

**Management response (separate from assessor conclusion).** Tenant and provider agree a contract schedule naming a single owner for the secondary loop, a notification trigger for load-shed decisions, and a joint approval step for setpoint changes. Closure requires reassessment of MCF-GOV-002, MCF-GOV-005 and MCF-GOV-006 with the executed schedule and a tabletop walkthrough of the emergency route; until then the prior decision stands as NOT_ASSURED and the board is informed under MCF-GOV-020.

**What this example shows.** The infrastructure may be well engineered — CDU redundancy could pass its THM controls — yet the capability is not assured because nobody with authority is guaranteed to act at the boundary when it matters. That is the purpose of the GOV domain.
