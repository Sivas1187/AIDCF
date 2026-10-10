> Markdown edition (source of truth). PDF: [AIDCF-007A_Control_Universe_Constitutional_Amendment_v1.0.pdf](AIDCF-007A_Control_Universe_Constitutional_Amendment_v1.0.pdf)

# AIDCF-007A Control Universe Constitutional Amendment

**Approved 15 / 90 / 360 Baseline**

| **Field**                 | **Value**                                               |
|---------------------------|---------------------------------------------------------|
| Artifact ID               | AIDCF-007A-AMD-001                                      |
| Status                    | Approved baseline                                       |
| Author                    | Siva Sethumadhavan                                      |
| Applies to                | AIDCF-007 and all downstream AIDCF artifacts            |
| Approved control universe | 15 domains; 90 control families; 360 normative controls |
| Superseded statement      | 14 domains; 84 families; 336 controls                   |
| Registry                  | AIDCF-007A Canonical Master Control Registry v1.0       |

# 1. Constitutional decision

The authoritative AIDCF control universe consists of 15 control domains, 90 control families and 360 normative controls. Each domain contains six control families and 24 controls. Each family contains four controls. This decision is the sole cardinality baseline for AIDCF-007 and all dependent artifacts.

# 2. Supersession

Every statement declaring 14 domains, 84 families or 336 controls is deprecated and superseded. Such statements shall not be used for coverage, scoring, conformance, reporting, machine execution or assurance decisions after adoption of this amendment.

# 3. Canonical identifiers

The existing identifiers MCF-\<DOMAIN\>-001 through MCF-\<DOMAIN\>-024 remain stable. Family identifiers use \<DOMAIN\>-01 through \<DOMAIN\>-06. Identity is immutable; future meaning-changing replacements require a new identifier and an explicit supersession record.

# 4. Approved domain model

| **Code** | **Domain**                                                 | **Families** | **Controls** | **Primary gates**   |
|----------|------------------------------------------------------------|--------------|--------------|---------------------|
| GOV      | Governance, Accountability and Assurance Direction         | 6            | 24           | CG-13; CG-14        |
| CAP      | AI Capability, Service Outcome and Demand Management       | 6            | 24           | CG-01; CG-02        |
| DEP      | Dependency, Concentration and External Reliance Management | 6            | 24           | CG-03; CG-12        |
| PHY      | Physical Site, Building and Security Infrastructure        | 6            | 24           | CG-02; CG-04        |
| POW      | Electrical Power Infrastructure and Energy Continuity      | 6            | 24           | CG-05               |
| THM      | Cooling, Thermal and Fluid Infrastructure                  | 6            | 24           | CG-06               |
| ENV      | Environmental and Resource Performance                     | 6            | 24           | CG-02; CG-04        |
| CMP      | AI Compute Infrastructure                                  | 6            | 24           | CG-08               |
| STO      | AI Storage and Data Infrastructure                         | 6            | 24           | CG-08; CG-10        |
| NET      | AI Network and Interconnect Architecture                   | 6            | 24           | CG-08               |
| OPS      | Building Operations and Service Management                 | 6            | 24           | CG-07; CG-13; CG-14 |
| RES      | Resilience, Continuity and Recovery                        | 6            | 24           | CG-09; CG-10        |
| SUP      | Supply Chain, OEM and Ecosystem Assurance                  | 6            | 24           | CG-03; CG-13        |
| SEC      | Digital, OT and Control-Plane Security                     | 6            | 24           | CG-07; CG-15        |
| EVA      | Evidence, Assessment and Assurance Management              | 6            | 24           | CG-11; CG-12        |

# 5. Registry authority

The accompanying workbook is the canonical machine-readable registry. It contains the domain, family and control inventories plus APS, gate, ontology, failure, graph, evidence, assessment, assurance-level, lifecycle, UNKNOWN and reassessment mappings. Where narrative text and the registry conflict, the approved amendment and controlled registry govern cardinality and identifiers; substantive control changes still require controlled methodology review.

# 6. Normative governance rules

- No domain, family or control may be deleted from an approved baseline.

- Records may be ACTIVE, DEPRECATED or SUPERSEDED.

- Profiles may strengthen or add requirements but may not silently weaken the baseline.

- Not Applicable requires approved rationale; missing evidence is UNKNOWN.

- Critical-gate status remains separate from scores and maturity.

- All control changes require impact analysis across AIDCF-008 through AIDCF-015 and AITG mappings.

- Testing remains authorised, competent, proportionate and safe.

# 7. Downstream migration

| **Artifact** | **Required action**                                                                                  |
|--------------|------------------------------------------------------------------------------------------------------|
| AIDCF-008    | Reconcile control-to-evidence profiles to 360 controls.                                              |
| AIDCF-009    | Confirm 360 procedures and 90 family workbooks use canonical IDs.                                    |
| AIDCF-010    | Confirm scoring denominator, family/domain aggregation and gate overlays.                            |
| AIDCF-011    | Update program profiles and coverage reporting.                                                      |
| AIDCF-012    | Update report disclosures and control coverage registers.                                            |
| AIDCF-013    | Reconcile domain architecture control links.                                                         |
| AIDCF-014    | Publish corrected registries, schemas and migration record.                                          |
| AIDCF-015    | Replace PILOT-\* identifiers with canonical MCF identifiers and close BI-001/NC-01 after validation. |

# 8. Acceptance tests

- Exactly 15 unique domain codes.

- Exactly 90 unique family IDs, six per domain.

- Exactly 360 unique control IDs, 24 per domain and four per family.

- No duplicate or orphan control/family identifiers.

- Every control has APS, critical-gate, ontology, failure, graph, evidence, assessment, UNKNOWN and reassessment mappings.

- Every control has status and version.

# 9. Controlled-review caveat

The approved cardinality and identifiers are now fixed. The substantive adequacy of individual control wording and mappings remains subject to multidisciplinary controlled review, calibration and pilot evidence. This amendment does not create certification, engineering approval or assurance by itself.
