# Security Policy

## 1. Purpose

AIDCF models sensitive physical, digital and operational dependencies. Security concerns may involve the framework, repository, schemas, tooling, synthetic data, public documentation or unauthorised disclosure of real infrastructure information.

This policy defines what may be reported publicly and what requires private handling.

## 2. Supported materials

Security reports may cover:

- repository configuration;
- executable tools and validation scripts;
- JSON Schema, JSON-LD, RDF/OWL and SHACL artifacts;
- unsafe default behaviour;
- validation bypass;
- canonical identifier collision;
- manifest or integrity defects;
- malicious or misleading fixture behaviour;
- leakage of secrets or personal data;
- disclosure of sensitive infrastructure paths;
- unsafe testing language;
- misuse of AIDCF claims or marks.

Historical and superseded releases may receive limited maintenance, but material security or disclosure risks should still be reported.

## 3. Information-classification model

| Class | Description | Public repository treatment |
|---|---|---|
| `PUBLIC` | Framework concepts, synthetic examples, public references and aggregate status | Permitted after review |
| `CONTROLLED` | Detailed mappings, non-sensitive review comments and controlled implementation material | Publish only when specifically approved |
| `CONFIDENTIAL` | Real architecture, evidence, findings, remediation and provider details | Do not publish |
| `HIGHLY_RESTRICTED` | Credentials, privileged paths, physical routes, emergency actions, exploitable weaknesses and sensitive telemetry | Private, need-to-know handling only |

## 4. Do not report publicly

Do not open a public issue containing:

- passwords, keys, tokens or credentials;
- non-public IP addresses, hostnames or network paths;
- privileged-access routes;
- physical routes, access controls or emergency procedures;
- real single points of failure or exploitable vulnerabilities;
- sensitive utility, fuel, cooling or recovery dependencies;
- customer, provider or employee confidential information;
- personal data without lawful authority;
- unauthorised facility diagrams, logs, configurations or evidence;
- step-by-step instructions for hazardous or disruptive actions.

## 5. Private reporting channel

Report privately through GitHub private vulnerability reporting:

```text
https://github.com/Sivas1187/AIDCF/security/advisories/new
```

The report is visible only to the repository maintainers and the reporter. The repository owner enables this channel under **Settings → Code security → Private vulnerability reporting**. If the link does not open a report form, the channel is not yet enabled: do not publish the report anywhere in the repository, and wait until it is.

A private report should include:

```text
Report ID
Affected repository, artifact and version
Security classification
Issue summary
Technical details
Reproduction conditions
Potential impact
Evidence
Suggested mitigation
Disclosure constraints
Reporter contact and conflict disclosure
```

## 6. Expected maintainer handling

Maintainers should:

1. acknowledge receipt through the private channel;
2. classify the report;
3. restrict access to need-to-know participants;
4. preserve the original evidence and provenance;
5. determine whether the issue affects code, data, claims, safety or disclosure;
6. identify affected releases and downstream artifacts;
7. implement and test a remediation;
8. rotate compromised credentials or remove exposed data where applicable;
9. publish a security advisory only after disclosure review;
10. record version, migration and supersession impact.

No response deadline is promised by this document. The repository should define service expectations only when maintainers can support them.

## 7. Safe-harbour intent

This repository does not authorise testing against third-party systems, real facilities or infrastructure.

Any future safe-harbour statement must be reviewed legally and must define the repository-owned assets, authorised test boundaries and prohibited conduct.

## 8. Operational and physical safety

AIDCF does not authorise live operational testing.

Do not perform or recommend without explicit competent authorisation:

- electrical switching or protection changes;
- generator or UPS discharge tests;
- cooling or fluid interruption;
- load shedding or overload;
- emergency shutdown;
- production failover;
- destructive or intrusive cyber testing;
- changes to BMS, EPMS, OT or control systems;
- actions affecting life safety, availability or environmental compliance.

Potentially unsafe language in an AIDCF artifact should be reported as a `SAFE` issue.

## 9. Repository secrets and automation

Repository automation should use least privilege. Secrets must not be stored in source files, fixtures, examples, logs or manifests.

Workflows should:

- pin or review third-party actions;
- limit token permissions;
- avoid executing untrusted pull-request content with privileged secrets;
- preserve validation outputs;
- distinguish test data from production data;
- fail safely when required inputs are missing;
- avoid publishing restricted artifacts automatically.

## 10. Synthetic data boundary

Synthetic fixtures must not contain copied real-site identifiers, credentials, personal data or confidential architecture.

A synthetic label does not make real-derived confidential data safe for publication.

## 11. Security disclosure in reports

Public reports may withhold sensitive details but must not conceal:

- the existence of a material limitation;
- a controlling gate `FAIL` or material `UNKNOWN`;
- the scope and intended-use restrictions;
- the fact that details were redacted;
- the decision effect of the redacted issue.

Use controlled identifiers and a restricted annex where detailed evidence must be retained.

## 12. Vulnerability and issue status

Suggested states are:

```text
RECEIVED
TRIAGED
VALIDATED
MITIGATION_IN_PROGRESS
RESOLVED
DISCLOSED
REJECTED
DUPLICATE
```

Rejected reports should retain a rationale. Sensitive reports and evidence should not be exposed solely to demonstrate closure.

## 13. Claim and impersonation concerns

Report unauthorised claims such as:

- “AIDCF Certified”;
- “AIDCF Accredited”;
- false endorsement by the author, employer or reviewer;
- false claims of independent validation;
- use of an AIDCF result outside its scope, period or intended use;
- modification of control or gate results without disclosure.

## 14. Data retention and removal

Sensitive reports should be retained only as long as necessary for investigation, remediation, legal obligations and defensible version history.

If confidential content is committed publicly, deletion from the current branch alone may be insufficient because Git history, forks, caches and releases may retain it. Repository maintainers should follow the hosting platform's sensitive-data-removal procedures and rotate exposed secrets.

## 15. Publication gate

The repository should not be made public until:

- a private reporting channel is configured;
- responsible maintainers are named;
- repository secrets are scanned;
- public artifacts are classification-reviewed;
- real evidence is excluded or authorised and redacted;
- third-party and proprietary content is reviewed;
- automation permissions are reviewed;
- security contacts and governance are aligned.
