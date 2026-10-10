> Markdown edition. Source: [AIDCF-012_Reporting_and_Assurance_Statement_Standard_v1.0.docx](AIDCF-012_Reporting_and_Assurance_Statement_Standard_v1.0.docx) · PDF: [AIDCF-012_Reporting_and_Assurance_Statement_Standard_v1.0.pdf](AIDCF-012_Reporting_and_Assurance_Statement_Standard_v1.0.pdf)

**AIDCF**

**AI Data Centre Facilities Assurance Framework**

**REPORTING & ASSURANCE STATEMENT STANDARD**

**Version 1.0**

**  
A normative standard for reports, bounded assurance statements, registers, dashboards, templates and machine-readable reporting schemas**

Artifact ID: AIDCF-RAS-001  
Status: Draft for controlled review  
Author: Siva Sethumadhavan  
Depends on: AIDCF-006 through AIDCF-011

**  
Reports communicate assurance. Reports do not create assurance.**

# Document control

**AIDCF-012 establishes a single reporting architecture for all AIDCF programs.**

| **Element**       | **Requirement**                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| Purpose           | Communicate scope, evidence, findings, gates, scores, UNKNOWN, decisions, limitations and validity consistently. |
| Inputs            | Approved AIDCF-009 assessment and AIDCF-010 decision snapshot under AIDCF-011 program governance.                |
| Outputs           | Executive, technical, domain, evidence, gate, customer, regulator, public and continuing-assurance packages.     |
| Non-certification | No report creates certification, accreditation, endorsement or guarantee.                                        |
| Security          | Sensitive infrastructure, identity, authority and dependency details require controlled disclosure.              |

# Part I - Reporting doctrine

**Reporting is a controlled transformation of an approved assurance record.**

| **Element**           | **Requirement**                                                     |
|-----------------------|---------------------------------------------------------------------|
| Evidence authority    | Presentation cannot strengthen evidence.                            |
| Single source         | All packages reference one authorised assessment/decision snapshot. |
| Audience tailoring    | Detail may change; meaning and limitations may not.                 |
| No silent omission    | Material gate FAIL/UNKNOWN and limitations remain visible.          |
| Score restraint       | Scores show coverage, confidence, gates and UNKNOWN.                |
| Management separation | Management response is separate from assessor conclusion.           |
| No certification      | No certificate, mark, accreditation or universal claim.             |
| Security              | Redaction protects detail but cannot hide decision limitations.     |
| Versioning            | Stable IDs, status, correction and supersession.                    |
| Human approval        | Automation drafts; accountable authorities approve.                 |

# Part II - Mandatory report content

**Every material report contains the same minimum assurance facts.**

| **Element**   | **Requirement**                                                      |
|---------------|----------------------------------------------------------------------|
| Capability    | Capability Instance and Service Outcomes.                            |
| Question      | Decision question and prohibited interpretations.                    |
| Scope         | Physical, logical, organisational, provider and temporal boundaries. |
| States/period | Assessed states and evidence period.                                 |
| Criteria      | AIDCF artifact/profile versions.                                     |
| Methods       | Assessment type, level and material procedures.                      |
| Evidence      | Coverage, quality, sufficiency, conflict and restrictions.           |
| Gates         | All applicable gate statuses and effects.                            |
| UNKNOWN       | Material unknowns, ceilings and evidence to resolve.                 |
| Scores        | Raw/adjusted, coverage, confidence and profile.                      |
| Decision      | Controlled AIDCF-010 state.                                          |
| Validity      | Conditions, expiry and reassessment triggers.                        |

# Part III - Report classes

**Each class serves a defined audience and intended use.**

| **Class** | **Report**                      | **Audience**                                    |
|-----------|---------------------------------|-------------------------------------------------|
| R1        | Executive Assurance Report      | Board, ExCo and accountable executives          |
| R2        | Technical Assessment Report     | Engineering, operations, security and assurance |
| R3        | Domain Report                   | Domain owner and specialist                     |
| R4        | Evidence Package                | Evidence custodians and reviewers               |
| R5        | Gate and Decision Package       | Independent reviewer and authority              |
| R6        | Customer/Second-Party Statement | Named relying party                             |
| R7        | Regulatory Support Package      | Authorised regulator engagement                 |
| R8        | Public Summary                  | Controlled external disclosure                  |
| R9        | Continuing-Assurance Report     | Monitored assertions and trigger state          |
| R10       | Remediation/Closure Report      | Action owners and reviewers                     |

# Part IV - Mandatory metadata

**A report without identity, lineage and intended use is non-conformant.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| reportId        | Required        |
| version         | Required        |
| status          | Required        |
| reportClass     | Required        |
| programId       | Required        |
| assessmentId    | Required        |
| decisionId      | Required        |
| issuer          | Required        |
| preparer        | Required        |
| reviewers       | Required        |
| intendedUsers   | Required        |
| intendedUse     | Required        |
| capabilityId    | Required        |
| serviceOutcomes | Required        |
| scope           | Required        |
| profile         | Required        |
| period          | Required        |
| classification  | Required        |
| validity        | Required        |
| supersedes      | Required        |

# Part V - Controlled decision language

**Only controlled, bounded decision wording is permitted.**

| **Element**            | **Requirement**                                                                      |
|------------------------|--------------------------------------------------------------------------------------|
| REASONABLY ASSURED     | Bounded evidence-supported confidence; no controlling gate FAIL or critical UNKNOWN. |
| CONDITIONALLY ASSURED  | Core claim supported subject to named, owned and time-bound conditions.              |
| LIMITED                | Material scope, evidence, coverage or UNKNOWN prevents stronger assurance.           |
| ADVERSE / NOT ASSURED  | Demonstrated material failure or controlling gate FAIL.                              |
| UNKNOWN / INCONCLUSIVE | Insufficient evidence, method or boundary for determination.                         |
| SUSPENDED              | Prior conclusion is not currently reliable.                                          |
| WITHDRAWN              | Issuer removes prior conclusion.                                                     |
| SUPERSEDED             | New authorised statement replaces prior.                                             |

# Part VI - Evidence reporting

**Normative reporting requirements.**

| **Element**      | **Requirement**                                                           |
|------------------|---------------------------------------------------------------------------|
| Manifest         | Stable evidence snapshot ID.                                              |
| Coverage         | Applicable, assessed, UNKNOWN, not assessed and N/A.                      |
| Quality          | Provenance, freshness, coverage, reliability, traceability and integrity. |
| Sufficiency      | Claim-specific S0-S5.                                                     |
| Conflict         | Supporting, challenging and qualifying evidence.                          |
| Restrictions     | Inaccessible, redacted, classified or third-party controlled.             |
| Derived evidence | Sources and transformation.                                               |
| Sampling/testing | Population, sample, conditions and limitations.                           |
| Disclosure       | No credentials/secrets/sensitive paths without authority.                 |

# Part VII - Critical-gate reporting

**Normative reporting requirements.**

| **Element**     | **Requirement**                                              |
|-----------------|--------------------------------------------------------------|
| Applicability   | Applicable, approved N/A or not assessed.                    |
| Status          | PASS, FAIL, UNKNOWN or approved N/A.                         |
| Basis           | Evidence and assessment references.                          |
| Decision effect | Ceiling, adverse, suspension or condition.                   |
| Related items   | Findings, UNKNOWN and scenarios.                             |
| Closure         | Owner, evidence, retest and trigger.                         |
| Prominence      | FAIL/critical UNKNOWN on executive first page and statement. |
| Visual rule     | No score colour may neutralise gate status.                  |

# Part VIII - Score reporting

**Normative reporting requirements.**

| **Element**         | **Requirement**                                       |
|---------------------|-------------------------------------------------------|
| Raw indicator       | Always present when numeric score is shown.           |
| Adjusted indicator  | Separately labelled.                                  |
| Coverage/confidence | Adjacent to every score.                              |
| Gate overlay        | Adjacent to domain/capability score.                  |
| UNKNOWN             | Count and materiality.                                |
| Profile/version     | Weights and scoring version.                          |
| Trend               | Separate condition from evidence/scope/method change. |
| Bands               | Descriptive, never certification tiers.               |
| Benchmark           | Cohort comparability and privacy disclosed.           |

# Part IX - Findings reporting

**Normative reporting requirements.**

| **Element**         | **Requirement**                                                             |
|---------------------|-----------------------------------------------------------------------------|
| Identity            | Stable ID and concise title.                                                |
| Criterion/condition | Requirement and evidenced state.                                            |
| Evidence            | Supporting and challenging references.                                      |
| Cause               | Only if evidenced or labelled analysis.                                     |
| Consequence         | Affected outcomes, dependencies and states.                                 |
| Classification      | Observation, improvement, weakness, significant weakness, critical finding. |
| Gate/score effect   | Explicit.                                                                   |
| Management response | Separate from assessor conclusion.                                          |
| Closure             | Evidence and reassessment criteria.                                         |
| Status              | Open through closed/superseded.                                             |

# Part X - UNKNOWN reporting

**Normative reporting requirements.**

| **Element**      | **Requirement**                                              |
|------------------|--------------------------------------------------------------|
| Identity/subject | Stable ID and affected object.                               |
| Missing item     | Attribute, evidence, state, provider or method.              |
| Reason           | Missing, inaccessible, stale, conflict, integrity or method. |
| Materiality      | Low, moderate, material, critical or systemic.               |
| Decision effect  | Condition, ceiling, adverse, suspension or withholding.      |
| Resolution       | Evidence/method required, owner and trigger.                 |
| No euphemism     | Critical UNKNOWN is not an improvement opportunity.          |

# Part XI - Management response

**Normative reporting requirements.**

| **Element**      | **Requirement**                             |
|------------------|---------------------------------------------|
| Position         | Agree, partly agree, disagree or reviewing. |
| Rationale        | Management view and evidence.               |
| Action/owner     | Specific action and accountable owner.      |
| Target/trigger   | Approved target or event.                   |
| Risk decision    | Management authority and rationale.         |
| Interim control  | Temporary safeguard and validity.           |
| Closure evidence | Required proof and independent validation.  |
| Separation       | Distinct styling and data object.           |

# Part XII - Validity and supersession

**Normative reporting requirements.**

| **Element**  | **Requirement**                                               |
|--------------|---------------------------------------------------------------|
| Validity     | Point/period and conditions.                                  |
| Triggers     | Change, incident, expiry, source outage, gate/finding change. |
| Correction   | Version, reason and approval.                                 |
| Suspension   | Affected claims and notice.                                   |
| Withdrawal   | Issuer, reason and effective date.                            |
| Supersession | New package references prior.                                 |
| Recall       | Known recipients notified for material change.                |
| Archive      | Authorised and superseded versions retained.                  |

# Part XIII - Classification

**Normative reporting requirements.**

| **Element**          | **Requirement**                                                  |
|----------------------|------------------------------------------------------------------|
| Public               | High-level decision and limitations only.                        |
| Client restricted    | Named users and contractual handling.                            |
| Confidential         | Detailed findings and technical content.                         |
| Highly restricted    | Sensitive paths, configurations, identities and vulnerabilities. |
| Redaction            | Reason recorded; controlled master retained.                     |
| Third-party evidence | Redistribution restrictions observed.                            |
| Privacy              | Personal data minimised.                                         |
| Export               | Controlled release record.                                       |

# Part XIV - Visual/accessibility

**Normative reporting requirements.**

| **Element**          | **Requirement**                                           |
|----------------------|-----------------------------------------------------------|
| Hierarchy            | Decision, gates, UNKNOWN and actions prominent.           |
| Colour               | Supplemental to text/icon/status.                         |
| Charts               | Denominator, coverage, version and units.                 |
| Tables               | Headers repeat; critical rows not split.                  |
| Language             | Plain executive language; precise technical meaning.      |
| Accessibility        | Structured headings, contrast, readable fonts and labels. |
| No misleading gauges | No false precision or certification cue.                  |
| Page control         | Classification, report ID, version and page number.       |

# Part XV - Quality review

**Normative reporting requirements.**

| **Element**        | **Requirement**                                    |
|--------------------|----------------------------------------------------|
| Reconciliation     | All claims trace to approved snapshot.             |
| Consistency        | All derivative reports agree.                      |
| Gate/UNKNOWN       | All material items visible.                        |
| Score              | Coverage, confidence and version correct.          |
| Claim              | No certification/guarantee/unsupported compliance. |
| Security           | Sensitive disclosure controlled.                   |
| Technical review   | Domain conclusions approved.                       |
| Independent review | Decision and statement challenged.                 |
| Authorisation      | Named issuer approves release.                     |

# Template - R1 Executive Assurance Report

**Standard structure for R1 Executive Assurance Report.**

| **Section** | **Required content**             |
|-------------|----------------------------------|
| 1           | Report control                   |
| 2           | Executive decision statement     |
| 3           | Capability/outcomes              |
| 4           | Scope/states/period              |
| 5           | Critical gates                   |
| 6           | Material findings and UNKNOWN    |
| 7           | CAI and supporting indicators    |
| 8           | Failure/dependency pathways      |
| 9           | Management actions/decision asks |
| 10          | Validity and non-certification   |

# Template - R2 Technical Assessment Report

**Standard structure for R2 Technical Assessment Report.**

| **Section** | **Required content**             |
|-------------|----------------------------------|
| 1           | Control and approval             |
| 2           | Question/criteria                |
| 3           | Capability architecture/boundary |
| 4           | Profile and methods              |
| 5           | Evidence/sampling/testing        |
| 6           | Control/family/domain results    |
| 7           | Failure scenarios                |
| 8           | Gates                            |
| 9           | Findings/UNKNOWN                 |
| 10          | Scores/coverage/confidence       |
| 11          | Technical conclusions            |
| 12          | Independent review               |
| 13          | Management response              |
| 14          | Validity/reassessment            |
| 15          | Appendices/schemas               |

# Template - R3 Domain Report

**Standard structure for R3 Domain Report.**

| **Section** | **Required content**   |
|-------------|------------------------|
| 1           | Domain scope           |
| 2           | Functions/outcomes     |
| 3           | Control-family results |
| 4           | Evidence               |
| 5           | Inspection/testing     |
| 6           | Gates                  |
| 7           | Findings/UNKNOWN       |
| 8           | Domain indicators      |
| 9           | Conclusion             |
| 10          | Actions/triggers       |

# Template - R4 Evidence Package

**Standard structure for R4 Evidence Package.**

| **Section** | **Required content** |
|-------------|----------------------|
| 1           | Manifest             |
| 2           | Requirements matrix  |
| 3           | Evidence register    |
| 4           | Quality/sufficiency  |
| 5           | Conflict register    |
| 6           | Sampling             |
| 7           | Testing              |
| 8           | Restrictions         |
| 9           | Derived lineage      |
| 10          | Custody/retention    |

# Template - R5 Gate and Decision Package

**Standard structure for R5 Gate and Decision Package.**

| **Section** | **Required content**        |
|-------------|-----------------------------|
| 1           | Question/scope              |
| 2           | Gate matrix                 |
| 3           | Gate cards                  |
| 4           | Critical UNKNOWN            |
| 5           | Material findings/scenarios |
| 6           | Scores/coverage             |
| 7           | Recommendation              |
| 8           | Independent challenge       |
| 9           | Authority decision          |
| 10          | Conditions/validity         |

# Template - R6 Customer/Second-Party Statement

**Standard structure for R6 Customer/Second-Party Statement.**

| **Section** | **Required content** |
|-------------|----------------------|
| 1           | Issuer/user/use      |
| 2           | Capability/scope     |
| 3           | Criteria/level       |
| 4           | Responsibilities     |
| 5           | Methods/evidence     |
| 6           | Gates                |
| 7           | Conclusion           |
| 8           | Limitations          |
| 9           | Validity             |
| 10          | Restrictions         |
| 11          | Non-certification    |

# Template - R7 Regulatory Support Package

**Standard structure for R7 Regulatory Support Package.**

| **Section** | **Required content** |
|-------------|----------------------|
| 1           | Authority/cover      |
| 2           | Regulatory mapping   |
| 3           | Capability/scope     |
| 4           | Control mapping      |
| 5           | Evidence index       |
| 6           | Gate/decision trace  |
| 7           | Findings/response    |
| 8           | Scores if relevant   |
| 9           | Limitations          |
| 10          | Submission record    |

# Template - R8 Public Summary

**Standard structure for R8 Public Summary.**

| **Section** | **Required content**     |
|-------------|--------------------------|
| 1           | Issuer                   |
| 2           | High-level subject/scope |
| 3           | Assessment basis         |
| 4           | Decision                 |
| 5           | Limitations              |
| 6           | Validity                 |
| 7           | Contact/reference        |
| 8           | No certification         |

# Template - R9 Continuing-Assurance Report

**Standard structure for R9 Continuing-Assurance Report.**

| **Section** | **Required content** |
|-------------|----------------------|
| 1           | Baseline             |
| 2           | Monitored assertions |
| 3           | Source health        |
| 4           | Evidence refresh     |
| 5           | Gate changes         |
| 6           | Drift/triggers       |
| 7           | Findings/UNKNOWN     |
| 8           | Current decision     |
| 9           | Human review         |
| 10          | Validity             |

# Template - R10 Remediation/Closure Report

**Standard structure for R10 Remediation/Closure Report.**

| **Section** | **Required content** |
|-------------|----------------------|
| 1           | Original item        |
| 2           | Action               |
| 3           | Interim safeguards   |
| 4           | Closure evidence     |
| 5           | Retest/reassessment  |
| 6           | Gate/score impact    |
| 7           | Reviewer disposition |
| 8           | Decision update      |
| 9           | Supersession         |

# AS-01 Template - First-Party Conclusion

**A bounded AIDCF-aligned statement, never a certificate.**

| **Element**                              | **Requirement** |
|------------------------------------------|-----------------|
| statementId/version/status               | Required        |
| issuer/authority                         | Required        |
| intended users/use                       | Required        |
| responsibilities                         | Required        |
| capability/outcomes                      | Required        |
| scope/states/period                      | Required        |
| criteria/profile                         | Required        |
| assurance level/type                     | Required        |
| methods                                  | Required        |
| evidence coverage/sufficiency/confidence | Required        |
| critical gates                           | Required        |
| scores with context                      | Required        |
| controlled conclusion                    | Required        |
| conditions                               | Required        |
| UNKNOWN/limitations                      | Required        |
| validity/triggers                        | Required        |
| classification/distribution              | Required        |
| non-certification note                   | Required        |
| approvals                                | Required        |

# AS-02 Template - Co-Sourced Statement

**A bounded AIDCF-aligned statement, never a certificate.**

| **Element**                              | **Requirement** |
|------------------------------------------|-----------------|
| statementId/version/status               | Required        |
| issuer/authority                         | Required        |
| intended users/use                       | Required        |
| responsibilities                         | Required        |
| capability/outcomes                      | Required        |
| scope/states/period                      | Required        |
| criteria/profile                         | Required        |
| assurance level/type                     | Required        |
| methods                                  | Required        |
| evidence coverage/sufficiency/confidence | Required        |
| critical gates                           | Required        |
| scores with context                      | Required        |
| controlled conclusion                    | Required        |
| conditions                               | Required        |
| UNKNOWN/limitations                      | Required        |
| validity/triggers                        | Required        |
| classification/distribution              | Required        |
| non-certification note                   | Required        |
| approvals                                | Required        |

# AS-03 Template - Second-Party Statement

**A bounded AIDCF-aligned statement, never a certificate.**

| **Element**                              | **Requirement** |
|------------------------------------------|-----------------|
| statementId/version/status               | Required        |
| issuer/authority                         | Required        |
| intended users/use                       | Required        |
| responsibilities                         | Required        |
| capability/outcomes                      | Required        |
| scope/states/period                      | Required        |
| criteria/profile                         | Required        |
| assurance level/type                     | Required        |
| methods                                  | Required        |
| evidence coverage/sufficiency/confidence | Required        |
| critical gates                           | Required        |
| scores with context                      | Required        |
| controlled conclusion                    | Required        |
| conditions                               | Required        |
| UNKNOWN/limitations                      | Required        |
| validity/triggers                        | Required        |
| classification/distribution              | Required        |
| non-certification note                   | Required        |
| approvals                                | Required        |

# AS-04 Template - Independent-Provider Statement

**A bounded AIDCF-aligned statement, never a certificate.**

| **Element**                              | **Requirement** |
|------------------------------------------|-----------------|
| statementId/version/status               | Required        |
| issuer/authority                         | Required        |
| intended users/use                       | Required        |
| responsibilities                         | Required        |
| capability/outcomes                      | Required        |
| scope/states/period                      | Required        |
| criteria/profile                         | Required        |
| assurance level/type                     | Required        |
| methods                                  | Required        |
| evidence coverage/sufficiency/confidence | Required        |
| critical gates                           | Required        |
| scores with context                      | Required        |
| controlled conclusion                    | Required        |
| conditions                               | Required        |
| UNKNOWN/limitations                      | Required        |
| validity/triggers                        | Required        |
| classification/distribution              | Required        |
| non-certification note                   | Required        |
| approvals                                | Required        |

# AS-05 Template - Continuing-Assurance Update

**A bounded AIDCF-aligned statement, never a certificate.**

| **Element**                              | **Requirement** |
|------------------------------------------|-----------------|
| statementId/version/status               | Required        |
| issuer/authority                         | Required        |
| intended users/use                       | Required        |
| responsibilities                         | Required        |
| capability/outcomes                      | Required        |
| scope/states/period                      | Required        |
| criteria/profile                         | Required        |
| assurance level/type                     | Required        |
| methods                                  | Required        |
| evidence coverage/sufficiency/confidence | Required        |
| critical gates                           | Required        |
| scores with context                      | Required        |
| controlled conclusion                    | Required        |
| conditions                               | Required        |
| UNKNOWN/limitations                      | Required        |
| validity/triggers                        | Required        |
| classification/distribution              | Required        |
| non-certification note                   | Required        |
| approvals                                | Required        |

# AS-06 Template - Suspension Notice

**A bounded AIDCF-aligned statement, never a certificate.**

| **Element**                              | **Requirement** |
|------------------------------------------|-----------------|
| statementId/version/status               | Required        |
| issuer/authority                         | Required        |
| intended users/use                       | Required        |
| responsibilities                         | Required        |
| capability/outcomes                      | Required        |
| scope/states/period                      | Required        |
| criteria/profile                         | Required        |
| assurance level/type                     | Required        |
| methods                                  | Required        |
| evidence coverage/sufficiency/confidence | Required        |
| critical gates                           | Required        |
| scores with context                      | Required        |
| controlled conclusion                    | Required        |
| conditions                               | Required        |
| UNKNOWN/limitations                      | Required        |
| validity/triggers                        | Required        |
| classification/distribution              | Required        |
| non-certification note                   | Required        |
| approvals                                | Required        |

# AS-07 Template - Withdrawal Notice

**A bounded AIDCF-aligned statement, never a certificate.**

| **Element**                              | **Requirement** |
|------------------------------------------|-----------------|
| statementId/version/status               | Required        |
| issuer/authority                         | Required        |
| intended users/use                       | Required        |
| responsibilities                         | Required        |
| capability/outcomes                      | Required        |
| scope/states/period                      | Required        |
| criteria/profile                         | Required        |
| assurance level/type                     | Required        |
| methods                                  | Required        |
| evidence coverage/sufficiency/confidence | Required        |
| critical gates                           | Required        |
| scores with context                      | Required        |
| controlled conclusion                    | Required        |
| conditions                               | Required        |
| UNKNOWN/limitations                      | Required        |
| validity/triggers                        | Required        |
| classification/distribution              | Required        |
| non-certification note                   | Required        |
| approvals                                | Required        |

# AS-08 Template - Supersession Notice

**A bounded AIDCF-aligned statement, never a certificate.**

| **Element**                              | **Requirement** |
|------------------------------------------|-----------------|
| statementId/version/status               | Required        |
| issuer/authority                         | Required        |
| intended users/use                       | Required        |
| responsibilities                         | Required        |
| capability/outcomes                      | Required        |
| scope/states/period                      | Required        |
| criteria/profile                         | Required        |
| assurance level/type                     | Required        |
| methods                                  | Required        |
| evidence coverage/sufficiency/confidence | Required        |
| critical gates                           | Required        |
| scores with context                      | Required        |
| controlled conclusion                    | Required        |
| conditions                               | Required        |
| UNKNOWN/limitations                      | Required        |
| validity/triggers                        | Required        |
| classification/distribution              | Required        |
| non-certification note                   | Required        |
| approvals                                | Required        |

# Template - Evidence Register

**Machine and human-readable evidence register.**

| **Element**  | **Requirement** |
|--------------|-----------------|
| evidenceId   |                 |
| assertion    |                 |
| class        |                 |
| source       |                 |
| scope        |                 |
| period       |                 |
| state        |                 |
| integrity    |                 |
| quality      |                 |
| sufficiency  |                 |
| restrictions |                 |
| status       |                 |
| review       |                 |

# Template - Findings Register

**Machine and human-readable findings register.**

| **Element**    | **Requirement** |
|----------------|-----------------|
| findingId      |                 |
| criterion      |                 |
| condition      |                 |
| evidence       |                 |
| cause          |                 |
| consequence    |                 |
| classification |                 |
| gateEffect     |                 |
| scoreEffect    |                 |
| owner          |                 |
| action         |                 |
| target         |                 |
| closure        |                 |
| status         |                 |

# Template - UNKNOWN Register

**Machine and human-readable unknown register.**

| **Element**    | **Requirement** |
|----------------|-----------------|
| unknownId      |                 |
| subject        |                 |
| missingItem    |                 |
| reason         |                 |
| materiality    |                 |
| decisionEffect |                 |
| evidenceNeeded |                 |
| owner          |                 |
| trigger        |                 |
| status         |                 |

# Template - Gate Register

**Machine and human-readable gate register.**

| **Element**    | **Requirement** |
|----------------|-----------------|
| gateId         |                 |
| applicability  |                 |
| evidence       |                 |
| states         |                 |
| scenarios      |                 |
| status         |                 |
| findings       |                 |
| unknown        |                 |
| decisionEffect |                 |
| closure        |                 |
| review         |                 |

# Template - Decision Register

**Machine and human-readable decision register.**

| **Element**    | **Requirement** |
|----------------|-----------------|
| decisionId     |                 |
| question       |                 |
| subject        |                 |
| scope          |                 |
| recommendation |                 |
| gates          |                 |
| unknown        |                 |
| scores         |                 |
| conditions     |                 |
| decision       |                 |
| authority      |                 |
| validity       |                 |
| supersession   |                 |

# Template - Action Register

**Machine and human-readable action register.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| actionId        |                 |
| source          |                 |
| action          |                 |
| owner           |                 |
| priority        |                 |
| dependency      |                 |
| target          |                 |
| interimControl  |                 |
| closureEvidence |                 |
| validation      |                 |
| status          |                 |

# Template - Continuing Dashboard

**Machine and human-readable continuing dashboard.**

| **Element**     | **Requirement** |
|-----------------|-----------------|
| decision        |                 |
| gates           |                 |
| evidenceHealth  |                 |
| coverage        |                 |
| sourceOutage    |                 |
| controlDrift    |                 |
| dependencyDrift |                 |
| triggers        |                 |
| findings        |                 |
| criticalUnknown |                 |
| actions         |                 |
| validity        |                 |

# GOV Domain Reporting Annex - Governance

**Domain-specific reporting profile for governance.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# CAP Domain Reporting Annex - Capability

**Domain-specific reporting profile for capability.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# DEP Domain Reporting Annex - Dependencies

**Domain-specific reporting profile for dependencies.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# PHY Domain Reporting Annex - Physical

**Domain-specific reporting profile for physical.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# POW Domain Reporting Annex - Power

**Domain-specific reporting profile for power.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# THM Domain Reporting Annex - Thermal

**Domain-specific reporting profile for thermal.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# ENV Domain Reporting Annex - Environment

**Domain-specific reporting profile for environment.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# CMP Domain Reporting Annex - Compute

**Domain-specific reporting profile for compute.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# STO Domain Reporting Annex - Storage

**Domain-specific reporting profile for storage.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# NET Domain Reporting Annex - Network

**Domain-specific reporting profile for network.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# OPS Domain Reporting Annex - Operations

**Domain-specific reporting profile for operations.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# RES Domain Reporting Annex - Resilience

**Domain-specific reporting profile for resilience.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# SUP Domain Reporting Annex - Supply Chain

**Domain-specific reporting profile for supply chain.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# SEC Domain Reporting Annex - Security

**Domain-specific reporting profile for security.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# EVA Domain Reporting Annex - Evidence/Assurance

**Domain-specific reporting profile for evidence/assurance.**

| **Element**                       | **Requirement** |
|-----------------------------------|-----------------|
| Purpose/outcomes                  | Required        |
| Scope/interfaces/providers/states | Required        |
| Control-family results            | Required        |
| Evidence quality/sufficiency      | Required        |
| Scenarios/dependencies            | Required        |
| Mapped gates                      | Required        |
| Domain score/coverage/confidence  | Required        |
| Findings/UNKNOWN                  | Required        |
| Bounded conclusion                | Required        |
| Sensitive disclosure controls     | Required        |
| Reassessment triggers             | Required        |

# Machine-Readable Reporting Package

**Schemas support AITG and reporting tools without delegating authority.**

| **Artifact**                     | **Purpose**                                                             |
|----------------------------------|-------------------------------------------------------------------------|
| report-metadata.schema.json      | Identity, issuer, users, subject, criteria, classification and lineage. |
| executive-report.schema.json     | R1 structure.                                                           |
| technical-report.schema.json     | R2 structure.                                                           |
| assurance-statement.schema.json  | AS-01 to AS-08.                                                         |
| evidence-register.schema.json    | Evidence disclosures.                                                   |
| finding-register.schema.json     | Findings and management response.                                       |
| unknown-register.schema.json     | UNKNOWN records.                                                        |
| gate-register.schema.json        | Gate results and effects.                                               |
| decision-register.schema.json    | Recommendation, decision and validity.                                  |
| continuing-dashboard.schema.json | Monitored claims, source health, drift and triggers.                    |
| public-summary.schema.json       | Permitted external disclosure.                                          |
| aidcf-report.owl / ttl           | Reporting ontology.                                                     |
| aidcf-report-shapes.ttl          | Validation shapes.                                                      |
| conformance-tests                | Consistency, non-certification, security and supersession.              |

# AITG Reporting Mappings

**Reporting objects preserve source lineage and native decisions.**

| **Element**         | **Requirement**                          |
|---------------------|------------------------------------------|
| Report              | AssuranceReport                          |
| Statement           | AssuranceStatement                       |
| Section             | ReportSection                            |
| Disclosure profile  | DisclosureProfile                        |
| Evidence register   | EvidenceManifest                         |
| Finding register    | FindingRegister                          |
| UNKNOWN register    | UnknownRegister                          |
| Gate register       | GateRegister                             |
| Decision            | AssuranceDecision                        |
| Management response | ManagementResponse                       |
| Validity            | ValidityCondition                        |
| Distribution        | DistributionControl                      |
| Correction          | CORRECTS                                 |
| Supersession        | SUPERSEDES                               |
| Reports             | REPORTS decision; never CREATES decision |

# Controlled Wording - REASONABLY ASSURED

**Model wording must be tailored to approved facts.**

| **Element**       | **Requirement**                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------|
| Decision state    | REASONABLY ASSURED                                                                                |
| Core meaning      | Bounded evidence-supported confidence; no controlling gate FAIL or critical UNKNOWN.              |
| Mandatory context | Capability, outcomes, scope, state, period, evidence, gates, limitations, validity and authority. |
| Prohibited use    | No certificate, guarantee or omitted controlling fact.                                            |

# Controlled Wording - CONDITIONALLY ASSURED

**Model wording must be tailored to approved facts.**

| **Element**       | **Requirement**                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------|
| Decision state    | CONDITIONALLY ASSURED                                                                             |
| Core meaning      | Core claim supported subject to named, owned and time-bound conditions.                           |
| Mandatory context | Capability, outcomes, scope, state, period, evidence, gates, limitations, validity and authority. |
| Prohibited use    | No certificate, guarantee or omitted controlling fact.                                            |

# Controlled Wording - LIMITED

**Model wording must be tailored to approved facts.**

| **Element**       | **Requirement**                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------|
| Decision state    | LIMITED                                                                                           |
| Core meaning      | Material scope, evidence, coverage or UNKNOWN prevents stronger assurance.                        |
| Mandatory context | Capability, outcomes, scope, state, period, evidence, gates, limitations, validity and authority. |
| Prohibited use    | No certificate, guarantee or omitted controlling fact.                                            |

# Controlled Wording - ADVERSE / NOT ASSURED

**Model wording must be tailored to approved facts.**

| **Element**       | **Requirement**                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------|
| Decision state    | ADVERSE / NOT ASSURED                                                                             |
| Core meaning      | Demonstrated material failure or controlling gate FAIL.                                           |
| Mandatory context | Capability, outcomes, scope, state, period, evidence, gates, limitations, validity and authority. |
| Prohibited use    | No certificate, guarantee or omitted controlling fact.                                            |

# Controlled Wording - UNKNOWN / INCONCLUSIVE

**Model wording must be tailored to approved facts.**

| **Element**       | **Requirement**                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------|
| Decision state    | UNKNOWN / INCONCLUSIVE                                                                            |
| Core meaning      | Insufficient evidence, method or boundary for determination.                                      |
| Mandatory context | Capability, outcomes, scope, state, period, evidence, gates, limitations, validity and authority. |
| Prohibited use    | No certificate, guarantee or omitted controlling fact.                                            |

# Controlled Wording - SUSPENDED

**Model wording must be tailored to approved facts.**

| **Element**       | **Requirement**                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------|
| Decision state    | SUSPENDED                                                                                         |
| Core meaning      | Prior conclusion is not currently reliable.                                                       |
| Mandatory context | Capability, outcomes, scope, state, period, evidence, gates, limitations, validity and authority. |
| Prohibited use    | No certificate, guarantee or omitted controlling fact.                                            |

# Conformance Validation Catalogue

**A conformant package passes positive, negative, security and consistency tests.**

| **ID**      | **Validation**                                                 |
|-------------|----------------------------------------------------------------|
| RAS-VAL-001 | Approved assessment/program/decision snapshots referenced.     |
| RAS-VAL-002 | Capability, outcomes, scope, states and period explicit.       |
| RAS-VAL-003 | Criteria and versions identified.                              |
| RAS-VAL-004 | Users/use stated.                                              |
| RAS-VAL-005 | Gate FAIL/UNKNOWN prominent.                                   |
| RAS-VAL-006 | UNKNOWN/limitations not softened.                              |
| RAS-VAL-007 | Scores show coverage/confidence/gates/version.                 |
| RAS-VAL-008 | Management response separate.                                  |
| RAS-VAL-009 | No certification/accreditation/guarantee/universal compliance. |
| RAS-VAL-010 | Derivative reports not stronger than technical master.         |
| RAS-VAL-011 | Sensitive paths controlled.                                    |
| RAS-VAL-012 | Findings and decision claims traceable.                        |
| RAS-VAL-013 | Validity/conditions/triggers present.                          |
| RAS-VAL-014 | Correction/supersession preserve history.                      |
| RAS-VAL-015 | Continuing assurance names claims and blind spots.             |
| RAS-VAL-016 | Automation does not approve conclusions.                       |
| RAS-VAL-017 | Cross-report consistency completed.                            |
| RAS-VAL-018 | Technical/independent approvals recorded.                      |

# Review and Release Gates

**Draft pending multidisciplinary pilot and review.**

| **Reviewer/pilot**              | **Status** |
|---------------------------------|------------|
| Methodology author              | Pending    |
| Assurance/reporting specialist  | Pending    |
| Board reader                    | Pending    |
| Engineering reviewers           | Pending    |
| AI/HPC reviewer                 | Pending    |
| Evidence specialist             | Pending    |
| Legal/privacy/security reviewer | Pending    |
| Independent provider reviewer   | Pending    |
| Regulatory liaison              | Pending    |
| Customer/second-party reviewer  | Pending    |
| Accessibility/design reviewer   | Pending    |
| AITG/schema reviewer            | Pending    |
| Executive report pilot          | Pending    |
| Technical report pilot          | Pending    |
| Statement pilot                 | Pending    |
| Dashboard pilot                 | Pending    |
| Public release                  | Pending    |

## Final doctrine

**AIDCF reports and statements communicate an approved assurance record. They do not create evidence, improve a score, neutralise UNKNOWN, override a critical gate, transfer assurance or establish certification. Every package remains bounded, traceable, appropriately protected, consistent with the technical record and authorised by a competent issuer.**
