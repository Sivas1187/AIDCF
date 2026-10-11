**AIDCF**

# PILOT AUTHORISATION TEMPLATE

*AI Data Centre Facilities Assurance Framework: pilot pack*

Version 1.0

The authorisation record a host completes and signs before an AIDCF mini-pilot may start

Artifact ID: AIDCF-PIL-002
Artifact type: Pilot record template
Status: Draft for controlled review
Author: Siva Sethumadhavan

> **Pilot status: pack ready; no authorised pilot has taken place.** This is a blank template. A copy becomes an authorisation only when completed and signed by the named parties.

> **Legal review required.** This template is not legal advice and has not been reviewed for any jurisdiction. Before anyone signs it, the host's legal adviser must review it (and, where a separate organisation provides the assessment team or the facility, that organisation's legal adviser too), adapt it to the applicable law, contracts, data-protection and confidentiality obligations and insurance, and decide whether it is to be a contract, a memorandum of understanding or an internal authorisation. Nothing in it overrides the host's own policies, permits or statutory duties.

# Document control

| **Field** | **Value** |
|---|---|
| Document ID | AIDCF-PIL-002 |
| Title | AIDCF Pilot Authorisation Template |
| Version | 1.0 |
| Date | 2026-10-11 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Used with | AIDCF-PIL-001 Mini-Pilot Protocol (conditions C1–C10, PIL-REQ-001 to PIL-REQ-016); AIDCF-PIL-003 Evidence Request List; AIDCF-009 Part A WP-01, WP-03, WP-05 and B14; whitepaper §29.1 and §29.4 |

## Revision history

| **Version** | **Date** | **Summary** |
|---|---|---|
| 1.0 | 2026-10-11 | First issue. |

---

## How to complete this template

- Complete every field. A field that does not apply is marked "n/a" with a reason; a blank is not "not applicable" (AIDCF-009 §E).
- Square brackets show what to enter. Tick boxes are completed `[x]` or `[ ]` with a note where not ticked.
- The completed record is classified at least **Confidential** (AIDCF-012 Part XIII). It is held by the host and the lead assessor and is never committed to the public AIDCF repository.
- The completed record is the SG0 input. WP-01 (Assessment Charter) is prepared from it and must not contradict it.

---

# 1. Pilot identification

| **Field** | **Entry** |
|---|---|
| Pilot ID | PILOT-001 (or the next free identifier in the AIDCF pilot register) |
| Host pilot reference | [host reference] |
| Host organisation | [legal name; this field is never published without §12 approval] |
| Assessment team organisation(s) | [legal name(s)] |
| Programme model (AIDCF-011 Part III) | [first-party / co-sourced / second-party / independent provider] |
| Assessment type (AIDCF-011 Part V) | Implementation (AL3) or Operational (AL4) |
| Protocol version applied | AIDCF-PIL-001 v1.0 |
| AIDCF artifact versions (AMH-REQ-005) | AIDCF-007A registry [v1.1]; AIDCF-008 [v1.1]; AIDCF-009 Part A [v1.1]; AIDCF-010 [v1.1]; AIDCF-011 [v1.1]; AIDCF-012 [v1.1] |
| Starter Profile | `pilots/pilot-framework/starter-profile.csv` at repository commit [hash], verified with `--check` on [date] |
| Planned dates | SG0 [date]; fieldwork [from–to]; SG6 [date]; SG7 [date] |

# 2. Sponsor, capability owner and decision authority

## 2.1 Sponsor authorisation

| **Field** | **Entry** |
|---|---|
| Sponsor name and role | [name, post] |
| Authority | [delegation or instrument under which the sponsor authorises the decision question, scope, resources and access] |
| Resources committed | [host staff and time; facilities; budget, if any] |
| Sponsor statement | "I authorise the AIDCF mini-pilot described in this record, within the scope, rules of engagement and terms stated, and I commit the host resources listed. I understand that the maximum permissible decision under this scope is LIMITED (§4.3)." |

## 2.2 Capability owner

| **Field** | **Entry** |
|---|---|
| Capability owner name and role | [name, post] |
| Capability Instance owned | [identifier and name] |
| Variant B provider owners (if any) | [for each provided power or cooling service: provider, accountable person, agreement reference] |
| Same person as sponsor? | [yes/no; if yes, reason (PIL-REQ-003)] |
| Capability owner statement | "I confirm ownership of the Capability Instance and its Service Outcomes, approve the scope and evidence access in this record, and accept the stop right in §7." |

## 2.3 Decision authority

| **Field** | **Entry** |
|---|---|
| Decision authority name and role | [name, post] |
| Authority for the decision question | [instrument or delegation] |
| Independence from the assessment team | [basis; must satisfy GC-13-6 and AIDCF-009 A4] |
| Decision authority statement | "I will issue the Assurance Decision after independent review, or record a decision not to issue one. I will not select a state above the maximum permissible state derived under AIDCF-010 (SDF-REQ-024)." |

# 3. Scope and boundary

| **Field** | **Entry** |
|---|---|
| Capability Instance | [identifier; one cluster or partition and its supporting systems] |
| Boundary variant (AIDCF-PIL-001 §3.1) | [A integrated / B tenant in a facility] |
| Physical boundary | [buildings, rooms, plant areas; described at a level that is itself Confidential] |
| Logical boundary | [cluster, scheduler, storage tiers, fabrics, management and out-of-band networks, control systems] |
| Organisational boundary | [owner, operator, estates or facilities function, providers and their responsibilities] |
| Temporal boundary | [assessment date; evidence period] |
| Operating states in scope | [as per profile stateCoverage; typically NORMAL, MAINTENANCE, DEGRADED, EMERGENCY, RECOVERY] |
| External dependencies to be recorded under CG-03 | [utility, telecom, cloud and service, OEM, sub-tier suppliers] |
| Exclusions | [each with rationale, Service Outcomes it can affect and decision effect (AMH-REQ-020); always including the 302 registry controls outside the Starter Profile] |
| Areas the pilot team will not enter | [list] |

# 4. Decision question, target Assurance Level and reachable decision

## 4.1 Decision question

| **Field** | **Entry** |
|---|---|
| Decision question | [the question the named decision user needs answered] |
| Top claim (AIDCF-009 §0.5) | "Capability Instance [X] can achieve Service Outcomes [Y] within tolerances [T] under declared operating states [S], for decision question [Q], as of date [D]." |
| Service Outcomes (preliminary) | [availability, performance, integrity, recovery outcomes with metric and tolerance, to be finalised in WP-02] |
| Named decision user(s) and intended use | [who will use the output, for what] |
| Prohibited interpretation | [for example: "The output is not a certification, an engineering or safety approval, or a statement about any system outside the boundary; it does not assess life safety, failure containment, change control, responsibility and authority, digital authority, or compute/storage/network functional integrity."] |

## 4.2 Target Assurance Level

| **Field** | **Entry** |
|---|---|
| Target AL | [AL3 (recommended) / AL4 (only where twelve months of operating records will be shared)] |
| Claim types concluded | [DESIGN, IMPLEMENTATION] or [DESIGN, IMPLEMENTATION, OPERATION] |
| Mandatory control-claims | [107 at AL3; 138 at AL4] |
| Freeze | The target AL is frozen at SG1 and is not changed after the first control result is recorded (PIL-REQ-004; SDF-REQ-008). |

## 4.3 Gates and the reachable decision (PIL-REQ-006)

| **Gate** | **Pilot scope** | **Ceiling if UNKNOWN or NOT_ASSESSED** |
|---|---|---|
| CG-01, CG-02, CG-03, CG-05, CG-06, CG-07, CG-10 | Evaluated | Per registries/gates/critical-gates.csv |
| CG-11, CG-12 | Evaluated (meta-gates over the profile) | Per registries/gates/critical-gates.csv |
| CG-04 | NOT_ASSESSED | LIMITED for outcomes depending on the affected area |
| CG-08 | NOT_ASSESSED | LIMITED for outcomes delivered by the cluster, fabric or storage tier |
| CG-09 | NOT_ASSESSED | LIMITED for the decision as a whole |
| CG-13 | NOT_ASSESSED | LIMITED |
| CG-14 | NOT_ASSESSED | LIMITED |
| CG-15 | NOT_ASSESSED | LIMITED; INCONCLUSIVE where an unverified authority reaches two or more other gates (US5) |
| Variant B only: CG-05 and/or CG-06 | [APPROVED_NA only if the registry conditions are met; rationale and approver] | none |

- [ ] The sponsor and decision user understand that the **maximum permissible decision is LIMITED**, and that NOT_ASSURED and INCONCLUSIVE are possible.
- [ ] The sponsor and decision user understand that gate criteria naming tests (GC-05-4, GC-05-6, GC-05-7, GC-06-4, GC-06-6, GC-07-3, GC-07-7, GC-10-3, GC-10-4, GC-10-5) can be met only from existing records, because the pilot performs no tests.

# 5. Research purpose

| **Field** | **Entry** |
|---|---|
| Research lead | [name, organisation] |
| Research questions informed | [from AIDCF-PIL-001 §2.2] |
| Measures collected | PM-01 to PM-20 (AIDCF-PIL-001 §12.2) |
| Double assessment | About 20% of control-claims by a second assessor, blind; all evaluated Gate Results re-derived independently |
| Interviews and ratings used for research | [yes/no; scope] |
| Research ethics | [where the host or the research lead's institution requires ethics review for research involving people (interviews, usability and usefulness ratings): committee, reference and approval date; otherwise "not required" with the basis] |
| Participant information and consent | [how interviewees and raters are informed of research use and can decline, as determined by the host and ethics review] |
| Separation | Research measures never change a result, Gate Result or decision (AIDCF-PIL-001 §12.1). |

# 6. Evidence access

| **Field** | **Entry** |
|---|---|
| Evidence request list | AIDCF-PIL-003 and `evidence-request-list.csv` at the commit in §1 |
| Host evidence coordinator | [name, role] |
| Controlled repository | [host-provided or host-approved system; location; access list] |
| Configuration extraction | [systems; executed by host operator and witnessed / executed by assessor with read-only credentials; change-process reference] |
| Systems excluded from extraction | [systems whose owner judges extraction could affect a controller or production workload; recorded as UNKNOWN (U2) or met by a listed acceptable alternative] |
| Third-party evidence | [provider and OEM documents; redistribution restrictions; provider consent where needed] |
| Interview access | [roles available for interview; time per role] |
| Site access | [dates, escort, induction, areas] |
| Refusal handling | A refused or unavailable item is recorded as an UNKNOWN Record with type and severity, never treated as favourable (AMH-REQ-007). |

# 7. Rules of engagement checklist

Built from AIDCF-009 B14 steps 1–6, B10, B13, AMH-REQ-026, AMH-REQ-029 and AMH-REQ-031. Each line is ticked and, where needed, completed.

## 7.1 Method risk and permits (B14 step 1)

- [ ] Every planned method is listed with its risk class: DOCUMENT_REVIEW, INQUIRY, ANALYSIS (none); OBSERVATION of walkthroughs, INSPECTION without contact (low); read-only configuration extraction (low to medium, system owner to classify per system).
- [ ] Permits, inductions and escorts required for each area visited are listed: [list].
- [ ] No method classed above the agreed level is planned.

## 7.2 Authorities (B14 step 2)

| **Authority** | **Name, role, contact** |
|---|---|
| Safety authority (approves access and work; can stop any activity) | [entry] |
| Change authority (approves configuration extraction on production management interfaces) | [entry] |
| Stop authorities (anyone listed may stop pilot activity at any time) | Safety authority; capability owner; [others] |
| Host duty contact during fieldwork | [entry] |

- [ ] The safety authority and capability owner have the right to stop any assessment activity at any time; a stop is recorded with its effect on results (AMH-REQ-031).

## 7.3 Communications, monitoring and rollback (B14 step 3)

- [ ] Fieldwork schedule shared with the host operations team in advance.
- [ ] Each configuration extraction is booked in the host's change or work-control process where required, with the system owner present or consulted.
- [ ] A rollback is defined for each extraction where the system owner requires one (normally: terminate session, revoke credential).
- [ ] Escalation route for any unexpected system behaviour during extraction: [entry].

## 7.4 Credentials and sensitive paths (B14 step 4)

- [ ] Pilot credentials are named, read-only, time-limited and listed: [list].
- [ ] No credential, key, network address, hostname or privileged route is written into workpapers, reports or messages; evidence is cited by evidence ID.
- [ ] HIGHLY_RESTRICTED evidence is reviewed only on host-controlled systems.

## 7.5 Deviations, incidents and near misses (B14 step 5)

- [ ] Any deviation from these rules, incident or near miss is reported to the safety authority immediately and recorded in the pilot log with its effect on results.

## 7.6 Close-out (B14 step 6)

- [ ] At SG7: credentials revoked, temporary access removed, any loaned equipment returned, and the host confirms the environment is as found.

## 7.7 Prohibited activities

The pilot team shall not:

1. operate, switch, isolate, open, adjust, reset or acknowledge alarms on any equipment (AMH-REQ-026);
2. perform or direct any test, failover, load bank, transfer, restoration, black-start or exercise on power, cooling, fire and life-safety systems, control systems or production AI workloads (AMH-REQ-029 is not engaged because no test is authorised);
3. run active network scanning, vulnerability scanning or penetration testing, or deploy taps, sensors or agents;
4. write to, change or upload to any controller, BMS, EPMS, CDU, PLC/SCADA system, network device, scheduler or storage system;
5. use credentials other than those issued for the pilot, or retain them after SG7;
6. remove evidence from the controlled repository, photograph areas where the host prohibits it, or copy HIGHLY_RESTRICTED material to any non-host system;
7. enter areas outside the approved route or without escort where escort is required;
8. operate controls, accept risk or make management decisions for the host (AMH-REQ-013);
9. present any pilot output as certification, accreditation, engineering approval or framework-owner endorsement (AIDCF-011 Part XIV);
10. carry out any activity not listed as permitted in this record (PIL-REQ-009).

# 8. Safety authority sign-off

| **Field** | **Entry** |
|---|---|
| Safety authority | [name, role, authority] |
| Activities approved | [walkthrough routes; inspection areas; extraction systems and methods] |
| Conditions | [induction, PPE, escort, time windows, areas excluded] |
| Hazards briefed to the pilot team | [list or reference to host induction] |
| Statement | "I approve the activities listed, on the conditions stated, and I retain the right to stop any activity at any time." |
| Signature and date | [signature] [date] |

# 9. Information classification and handling

| **Class (AIDCF-012 Part XIII)** | **SECURITY.md class** | **Pilot content** | **Handling agreed** |
|---|---|---|---|
| Highly restricted | HIGHLY_RESTRICTED | Credentials, network addresses and paths, control-system configurations, privileged routes, physical routes, emergency procedures, exploitable weaknesses | Host systems only; need-to-know list: [names] |
| Confidential | CONFIDENTIAL | Architecture, evidence, workpapers, findings, remediation, provider details | Controlled repository; access list: [names] |
| Client restricted | CONTROLLED (nearest equivalent) | R2, R4, R5 reports and identifiable metrics | Named distribution: [names] |
| Public | PUBLIC | Anonymised research outputs; R8 Public Summary | Only after §12 approval |

- [ ] AIDCF-PIL-003 default classifications accepted; the evidence lead may raise, never lower, a default.
- [ ] Redaction keeps a controlled master and never removes the decision state, controlling Gate Results, US4/US5 UNKNOWN Records or material limitations (RAS-REQ-012).
- [ ] AI-assisted tools: [not used / used only on host-approved systems: list]; outputs treated as derived evidence (E7) with lineage.
- [ ] No pilot evidence, workpaper or identifiable result is committed to the public AIDCF repository (PIL-REQ-011).

# 10. Data retention and destruction

| **Record** | **Holder** | **Retention period** | **At end of retention** |
|---|---|---|---|
| Evidence copies | [host] | [period set by host policy] | [destroy / return]; certificate: [yes/no] |
| Workpapers WP-01 to WP-20 and the decision package | [host and assessment organisation] | [period] | [archive / destroy] |
| Pilot credentials and access logs | [host] | Revoked at SG7; logs per host policy | — |
| Research data (control-claim log, metrics) identifiable form | [research lead] | [period] | Destroyed or anonymised |
| Anonymised research data | [research lead; public repository if approved] | Indefinite | — |
| Personal data (interview notes, names) | [holder] | [minimum needed; period] | Destroyed |

- [ ] Workpapers are version-controlled and superseded versions retained for the retention period (AMH-REQ-004).
- [ ] Destruction of evidence copies held outside the host is certified to the host in writing.

# 11. Confidentiality, personal data and third-party material

| **Field** | **Entry** |
|---|---|
| Confidentiality terms | [reference to agreement, or terms here, as drafted by legal adviser] |
| Personal data | [categories (for example names and roles of interviewees); purpose; lawful basis as determined by the host's data-protection adviser; minimisation] |
| Third-party material | [provider and OEM documents; restrictions; consents] |
| Export or cross-border transfer | [none / conditions] |

# 12. Publication and anonymisation terms

| **Term** | **Agreed entry** |
|---|---|
| Host named in publications? | [no (default) / yes, in the following form: ...] |
| Outputs that may be published after approval | [anonymised metrics; anonymised lessons and change proposals; aggregated research results; R8 Public Summary] |
| Outputs that are never published | Evidence, workpapers, R2, R4, R5, topology, configurations, supplier and product names, any single point of failure or weakness |
| Anonymisation rules | No site, location, supplier, product, network, topology or personal details; counts small enough to identify a condition are suppressed or banded; free text reviewed for identifying detail |
| Approval process | Host approver [name, role] sees the exact text; approval in writing; approval may be withheld |
| Negative and null results | Published on the same terms as positive results, subject to the same approval |
| Decision publication | Only as an R8 Public Summary in AIDCF-012 controlled wording with all mandatory disclosures and the non-certification note |
| Repository status updates | The framework owner updates whitepaper §29.4 and README pilot status only on the basis of the signed records |
| Withdrawal | [host's right to withdraw approval before publication; effect after publication] |

# 13. Conflict of interest declarations

Every assessor, technical reviewer, independent reviewer, research lead and second assessor completes one row before appointment (AMH-REQ-012; APF-REQ-006).

| **Name** | **Role** | **Prior design, operation or advisory work on the subject in the previous assessment period** | **Financial or employment relationship with host or providers** | **Other interest** | **Safeguard or exclusion** | **Signature, date** |
|---|---|---|---|---|---|---|
| [ ] | [ ] | [none / describe] | [none / describe] | [none / describe] | [ ] | [ ] |

- [ ] No fee or reward is contingent on the decision state (APF-REQ-005).
- [ ] Where an assessor is a host employee, the self-review threat and its safeguard are recorded and will be disclosed in the statement.

# 14. Independent reviewer and decision authority appointment

| **Field** | **Entry** |
|---|---|
| Independent reviewer | [name, organisation] |
| Competence | [AC-5 basis: senior assurance competence; gate and decision challenge experience] |
| Independence basis | [no preparation role; no self-review threat; relationship to host and team] |
| Scope of review | At minimum every gate that is FAIL or UNKNOWN, every US3–US5 UNKNOWN severity, every US4/US5 UNKNOWN Record and the proposed decision wording (AMH-REQ-041; SDF-REQ-020) |
| Access | Full access to the decision package and evidence needed to sample assertions |
| Acceptance statement | "I accept appointment as independent reviewer for PILOT-[nnn] and confirm the independence basis stated." |
| Decision authority confirmation | As §2.3; confirms independence from the assessment team and from the independent reviewer |

# 15. Signatures

By signing, each party confirms that the host's legal adviser has reviewed this record and that the party has authority to sign.

| **Party** | **Name** | **Role** | **Signature** | **Date** |
|---|---|---|---|---|
| Sponsor | | | | |
| Capability owner | | | | |
| Variant B provider owner(s), if any | | | | |
| Decision authority | | | | |
| Safety authority | | | | |
| Data protection / information governance approver | | | | |
| Independent reviewer | | | | |
| Lead assessor | | | | |
| Research lead | | | | |
| Host legal adviser (review confirmed) | | | | |

# 16. Authorisation status (whitepaper §29.4)

Completed by the lead assessor and kept current.

| **Approval/result** | **Status** | **Required evidence** | **Reference** |
|---|---|---|---|
| Sponsor authorisation | [PENDING / SIGNED] | Signed charter | §2.1, §15 |
| Capability-owner authorisation | [PENDING / SIGNED] | Scope and evidence-access approval | §2.2, §3, §6 |
| Safety/testing authorisation | [PENDING / SIGNED] | Rules of engagement and stop criteria | §7, §8 |
| Data/privacy/security approval | [PENDING / SIGNED] | Classification and disclosure decision | §9 to §12 |
| Independent reviewer acceptance | [PENDING / SIGNED] | Review memorandum | §14 |
| Execution | NOT STARTED | Workpapers and logs | AIDCF-PIL-004 |
| Assurance Decision | NOT ISSUED | Signed decision record | AIDCF-PIL-004 |
| Public summary | NOT AUTHORISED | Publication approval | §12 |
