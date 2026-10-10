> Markdown edition (source of truth). PDF edition, generated from this file: [AIDCF-007A_Control_Universe_Constitutional_Amendment_v1.1.pdf](AIDCF-007A_Control_Universe_Constitutional_Amendment_v1.1.pdf).

# AIDCF-007A Control Universe Constitutional Amendment

**15 / 90 / 360 Baseline, with v1.1 amendment note AIDCF-007A-AMD-002**

## Document control

| **Field**                 | **Value**                                                                                                                                                     |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Public ID                 | AIDCF-007A (amendment instrument)                                                                                                                             |
| Amendment records         | AIDCF-007A-AMD-001 (v1.0, cardinality and identifiers); AIDCF-007A-AMD-002 (v1.1, control content, gate mapping and assurance levels)                         |
| Version                   | 1.1                                                                                                                                                           |
| Date                      | 2026-10-10                                                                                                                                                    |
| Status                    | Draft for controlled review. AMD-001 remains in force as the cardinality and identifier baseline (see §10); AMD-002 is proposed (see §11).                      |
| Author                    | Siva Sethumadhavan                                                                                                                                            |
| Amends and supersedes     | AIDCF-007 Master Control Framework and Control Catalogue v1.0 (archived at `archive/superseded/AIDCF-007_Control_Catalogue_v1.0.md` and `.xlsx`)              |
| Governs                   | AIDCF-007A Canonical Master Control Registry (v1.0 in force; v1.1 Proposed)                                                                                   |
| Downstream effect         | Binding on AIDCF-008 to AIDCF-019, AIDCF-VR-001 and AIDCF-WP-001 for control identity, cardinality and gate mapping                                           |
| Control universe          | 15 domains; 90 control families; 360 normative controls                                                                                                       |
| Deprecated statement      | 14 domains; 84 families; 336 controls (narrative statements only; see §2)                                                                                     |
| Registry                  | `standards/aidcf-007a/registry/AIDCF-007A_Canonical_Master_Control_Registry_15-90-360_v1.0.xlsx` (v1.0); registry v1.1 per §11                              |

### Revision history

| **Version** | **Date**   | **Summary**                                                                                                                                                                                                                                          |
|-------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.0         | Not stated | AIDCF-007A-AMD-001 issued: fixed 15/90/360 cardinality and MCF identifiers; deprecated 14/84/336 statements.                                                                                                                                         |
| 1.1         | 2026-10-10 | Clarified that the amendment supersedes the AIDCF-007 v1.0 catalogue and governs the AIDCF-007A registry; corrected the change history; added approval record, CG-01 to CG-15 names table and amendment note AIDCF-007A-AMD-002 (registry v1.1 proposals). |

# 1. Constitutional decision

The authoritative AIDCF control universe consists of 15 control domains, 90 control families and 360 normative controls. Each domain contains six control families and 24 controls. Each family contains four controls. This decision is the sole cardinality baseline for the AIDCF-007A registry and all dependent artifacts.

This amendment amends and supersedes the AIDCF-007 Master Control Framework and Control Catalogue v1.0. AIDCF-007 v1.0 is archived and retained for lineage only. All live references to the control universe shall use the public ID AIDCF-007A; "AIDCF-007" (without the suffix) denotes only the superseded v1.0 catalogue.

# 2. Supersession and corrected change history

The record of how the cardinality conflict arose is as follows.

1. The AIDCF-007 v1.0 workbook (`AIDCF-007_Control_Catalogue_v1.0.xlsx`, Summary sheet) already declared and contained 15 domains, 90 control families and 360 normative controls, using identifiers MCF-\<DOM\>-001 to MCF-\<DOM\>-024.
2. Separately, some narrative AIDCF documents stated a 14-domain / 84-family / 336-control universe. The conflict between these narrative statements and the workbook was recorded as a blocker in the full-stack validation (AIDCF-VR-001) and in the AIDCF-015 pilot, which used local pilot identifiers instead of MCF identifiers because of it.
3. AIDCF-007A-AMD-001 resolved the conflict in favour of the workbook. It did not add a domain or renumber any control; it confirmed the 15/90/360 universe that the workbook already held and deprecated the narrative 14/84/336 statements.

Every statement declaring 14 domains, 84 families or 336 controls is deprecated and superseded. Such statements shall not be used for coverage, scoring, conformance, reporting, machine execution or assurance decisions.

# 3. Canonical identifiers

The identifiers MCF-\<DOMAIN\>-001 through MCF-\<DOMAIN\>-024 are stable. Family identifiers use \<DOMAIN\>-01 through \<DOMAIN\>-06; family *n* holds controls 4*n*−3 to 4*n*. Identity is immutable; a meaning-changing replacement requires a new identifier and an explicit supersession record. Title corrections that remove ambiguity without changing meaning (see §11.2) are recorded as amendments and do not change the identifier.

# 4. Domain model

| **Code** | **Domain**                                                 | **Families** | **Controls** | **v1.0 primary gates (superseded by §11.3)** |
|----------|------------------------------------------------------------|--------------|--------------|----------------------------------------------|
| GOV      | Governance, Accountability and Assurance Direction         | 6            | 24           | CG-13; CG-14                                 |
| CAP      | AI Capability, Service Outcome and Demand Management       | 6            | 24           | CG-01; CG-02                                 |
| DEP      | Dependency, Concentration and External Reliance Management | 6            | 24           | CG-03; CG-12                                 |
| PHY      | Physical Site, Building and Security Infrastructure        | 6            | 24           | CG-02; CG-04                                 |
| POW      | Electrical Power Infrastructure and Energy Continuity      | 6            | 24           | CG-05                                        |
| THM      | Cooling, Thermal and Fluid Infrastructure                  | 6            | 24           | CG-06                                        |
| ENV      | Environmental and Resource Performance                     | 6            | 24           | CG-02; CG-04                                 |
| CMP      | AI Compute Infrastructure                                  | 6            | 24           | CG-08                                        |
| STO      | AI Storage and Data Infrastructure                         | 6            | 24           | CG-08; CG-10                                 |
| NET      | AI Network and Interconnect Architecture                   | 6            | 24           | CG-08                                        |
| OPS      | Building Operations and Service Management                 | 6            | 24           | CG-07; CG-13; CG-14                          |
| RES      | Resilience, Continuity and Recovery                        | 6            | 24           | CG-09; CG-10                                 |
| SUP      | Supply Chain, OEM and Ecosystem Assurance                  | 6            | 24           | CG-03; CG-13                                 |
| SEC      | Digital, OT and Control-Plane Security                     | 6            | 24           | CG-07; CG-15                                 |
| EVA      | Evidence, Assessment and Assurance Management              | 6            | 24           | CG-11; CG-12                                 |

The right-hand column records the whole-domain gate association used in AIDCF-007 v1.0 and registry v1.0. It is retained for lineage. Under AMD-002 it is replaced by control-specific mapping (§11.3) and shall not be used to evaluate a gate.

# 5. Critical gates

The critical-gate names below are those defined in AIDCF-007 v1.0 (Critical Gates sheet) and are canonical. Gate criteria, roll-up and decision ceilings are defined in AIDCF-010; evidence floors in AIDCF-008.

| **Gate** | **Name**                                          | **What it protects**                                                                                                         |
|----------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| CG-01    | Capability and outcome definition                 | Capability Instance, Service Outcomes, tolerances, criticality and decision question are defined, owned and approved          |
| CG-02    | Boundary and architecture integrity               | Assessment boundary, current architecture, as-built reconciliation and exclusions                                             |
| CG-03    | Critical dependency visibility                    | Material internal and external dependencies, common modes and concentration are identified and owned                          |
| CG-04    | Life safety and hazardous energy                  | Fire, arc flash and shock, hazardous fluids and chemicals, confined space, refrigerants, battery thermal runaway, safe work    |
| CG-05    | Resilient electrical supply                       | Utility, distribution, UPS/BESS, generation, fuel, protection and power quality across operating states                       |
| CG-06    | Thermal continuity                                | Heat-removal path (air, liquid, facility water, heat rejection) across operating states, including transients                 |
| CG-07    | Critical control-system integrity                 | BMS, EPMS, CDU, PLC, SCADA and automation function safely, fail safe, and are configured and governed                         |
| CG-08    | Compute, storage and network functional integrity | Accelerators, storage and fabrics deliver required function, performance and integrity                                        |
| CG-09    | Failure containment                               | Fault domains, isolation and blast-radius limits prevent propagation beyond tolerance                                         |
| CG-10    | Recovery readiness                                | Restoration of outcome (power, cooling, compute, data and checkpoints, network, control plane) is planned and tested           |
| CG-11    | Evidence sufficiency                              | Evidence for decisive claims meets floors (meta-gate, evaluated across all controls)                                          |
| CG-12    | Critical UNKNOWN                                  | No unresolved US4/US5 UNKNOWN without disposition (meta-gate, evaluated across all controls)                                  |
| CG-13    | Responsibility and authority                      | Every critical function and dependency has an accountable owner and decision authority                                        |
| CG-14    | Change control                                    | Material changes are controlled, impact-assessed and validated                                                                |
| CG-15    | Integrated digital authority over infrastructure  | Identity, privilege, remote access and control-plane reach over facility and AI infrastructure are bounded, monitored, recoverable |

# 6. Registry authority

The registry workbook is the canonical machine-readable form of the control universe. It contains the domain, family and control inventories and the APS, gate, ontology, failure, graph, evidence, assessment, assurance-level, lifecycle, UNKNOWN and reassessment mappings. Where narrative text and the registry conflict, this amendment and the controlled registry govern cardinality and identifiers. Substantive control changes require controlled methodology review and are recorded as numbered amendments (AIDCF-007A-AMD-NNN).

# 7. Normative governance rules

- No domain, family or control may be deleted from an approved baseline.
- Records may be ACTIVE, DEPRECATED or SUPERSEDED.
- Profiles may strengthen or add requirements but may not silently weaken the baseline.
- NOT_APPLICABLE requires approved rationale; missing evidence is UNKNOWN.
- Critical-gate status remains separate from scores and maturity.
- All control changes require impact analysis across AIDCF-008 to AIDCF-019 and the AIDCF-005 AITG mappings.
- Testing remains authorised, competent, proportionate and safe.

# 8. Downstream migration

| **Artifact** | **Required action**                                                                                                         |
|--------------|-----------------------------------------------------------------------------------------------------------------------------|
| AIDCF-008    | Reconcile control-to-evidence profiles to 360 controls and the per-control evidence profiles of registry v1.1.               |
| AIDCF-009    | Confirm 360 procedures and 90 family workbooks use canonical IDs and the per-control procedures of registry v1.1.             |
| AIDCF-010    | Apply per-control CRITICAL/SUPPORTING gate mapping and the canonical gate roll-up rule.                                       |
| AIDCF-011    | Update programme profiles and coverage reporting; align required assurance levels to AL2–AL5.                                |
| AIDCF-012    | Update report disclosures and control coverage registers.                                                                    |
| AIDCF-013    | Reconcile domain architecture control links to AIDCF-007A family ranges.                                                     |
| AIDCF-014    | Publish corrected registries, vocabularies and migration record (serialisation per AIDCF-016).                               |
| AIDCF-015    | Replace pilot identifiers with canonical MCF identifiers and close the related baseline issue after validation.               |

# 9. Acceptance tests

- Exactly 15 unique domain codes.
- Exactly 90 unique family IDs, six per domain.
- Exactly 360 unique control IDs, 24 per domain and four per family.
- No duplicate or orphan control or family identifiers.
- No two controls share the same title (added by AMD-002).
- Every control has APS, critical-gate, ontology, failure, graph, evidence, assessment, UNKNOWN and reassessment mappings.
- Every control has status and version.
- Under registry v1.1: every gate CG-01 to CG-10 and CG-13 to CG-15 has at least three CRITICAL controls; CG-11 and CG-12 have no per-control mapping; every control's required assurance level is consistent with its claim type (§11.4).

# 10. Approval record

| **Item**                                   | **Record**                                                                                                                                                                                              |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Instrument                                 | AIDCF-007A-AMD-001 (cardinality 15/90/360 and canonical identifiers)                                                                                                                                    |
| Approved by                                | Siva Sethumadhavan, author, acting as baseline owner                                                                                                                                                    |
| Approval date                              | As stated on the v1.0 issue. The v1.0 document records the status "Approved baseline" but states no separate approval date.                                                                             |
| Scope of approval                          | Cardinality and identifiers only. It is not approval of control wording, mappings, evidence profiles or any engineering content.                                                                       |
| Independent multidisciplinary ratification | PENDING. No independent reviewer, committee or external body has ratified AMD-001.                                                                                                                      |
| Effect while ratification is pending       | AMD-001 is the working baseline for identity and cardinality across AIDCF artifacts. It creates no certification, engineering approval or assurance by itself.                                          |
| Instrument                                 | AIDCF-007A-AMD-002 (§11)                                                                                                                                                                               |
| Status                                     | Draft for controlled review. Not approved.                                                                                                                                                             |

# 11. Amendment note AIDCF-007A-AMD-002 (v1.1)

| **Field**        | **Value**                                                                                   |
|------------------|---------------------------------------------------------------------------------------------|
| Amendment ID     | AIDCF-007A-AMD-002                                                                          |
| Date             | 2026-10-10                                                                                  |
| Status           | Draft for controlled review                                                                 |
| Subject          | AIDCF-007A Canonical Master Control Registry v1.1                                           |
| Registry status  | Proposed — subject to controlled methodology review                                         |
| Identity effect  | None. All 15 domain codes, 90 family IDs and 360 control IDs are unchanged.                 |

## 11.1 Control content rewritten per control

Registry v1.0 (and AIDCF-007 v1.0) generated every control's objective, requirement, assessment criteria, evidence and procedure text from a single template ("Ensure … is defined, implemented, maintained and demonstrably supports …"), with only the title substituted. Registry v1.1 replaces that template text with content specific to each control:

- objective and one or more "shall" requirements naming the accountable role;
- three to seven independently testable assessment criteria;
- parameters, expressed as capability-profile parameters with illustrative defaults where values are site-specific;
- an evidence profile per control (claim type, profile tier CP-1 to CP-5, required evidence classes E1–E7, quality and sufficiency floors, operating-state coverage, independence, UNKNOWN effect and reassessment triggers) aligned to AIDCF-008;
- an ordered assessment procedure using the canonical assessment methods, aligned to AIDCF-009;
- control type, lifecycle stages, operating states, applicability, failure modes, ontology classes, testing-safety constraints, a control-specific UNKNOWN rule, informative references and related controls.

Control IDs, family IDs, family membership and family structure are unchanged.

## 11.2 Duplicate titles corrected

Two control titles duplicated titles elsewhere in the registry. They are disambiguated without change of meaning or identifier:

| **Control ID** | **v1.0 title**      | **v1.1 title**               | **Duplicated with**                 |
|----------------|---------------------|------------------------------|-------------------------------------|
| MCF-NET-004    | Fault-Domain Design | Fabric Fault-Domain Design   | MCF-CMP-008 Fault-Domain Design     |
| MCF-STO-019    | Recovery Sequencing | Storage Recovery Sequencing  | MCF-RES-014 Recovery Sequencing     |

## 11.3 Control-specific gate mapping

Registry v1.0 mapped every control in a domain to the domain's primary gates (§4), so that, for example, all 24 STO controls were mapped to CG-10. That mapping did not distinguish controls whose failure defeats a gate from controls that merely inform it. Registry v1.1 maps each control individually, 0..n gates per control, each with a role:

- **CRITICAL**: the gate cannot PASS unless this control is CONFORMING at its required claim type, when in scope.
- **SUPPORTING**: the control informs the gate evaluation; a NONCONFORMING result requires a documented gate-level evaluation but does not automatically fail the gate.

Mappings are made by meaning and across domains (for example, CG-04 draws on relevant PHY, POW, THM and ENV controls; CG-10 on POW, THM, CMP, STO, NET and RES recovery controls). CG-11 and CG-12 are meta-gates evaluated across all controls and are not mapped per control. Each of CG-01 to CG-10 and CG-13 to CG-15 has at least three CRITICAL controls. The gate roll-up rule is defined in AIDCF-010.

## 11.4 Assurance levels assigned per control

Registry v1.0 assigned required assurance levels A2 to A5 in rotation by position within each family. Registry v1.1 assigns each control a primary claim type and the minimum assurance level that claim type requires:

| **Claim type**   | **Minimum assurance level** |
|------------------|-----------------------------|
| DESIGN           | AL2                         |
| IMPLEMENTATION   | AL3                         |
| OPERATION        | AL4                         |
| EFFECTIVENESS    | AL5                         |
| RESILIENCE       | AL5                         |

Legacy codes A2 to A5 map one-to-one to AL2 to AL5.

## 11.5 Gate names restored

Some downstream documents had shortened or reworded critical-gate names (for example "Electrical continuity" for CG-05). Registry v1.1 and all dependent artifacts use the gate names from AIDCF-007 v1.0, as listed in §5.

## 11.6 Status and conditions

Registry v1.1 is Proposed — subject to controlled methodology review. Until AMD-002 is approved, registry v1.0 remains the identity and cardinality baseline; v1.1 content may be used for pilots, review and calibration, and any assessment that uses it shall disclose the registry version. Approval of AMD-002 requires the multidisciplinary review set out in §12.

# 12. Controlled-review caveat

The cardinality and identifiers are fixed by AMD-001. The adequacy of individual control wording, evidence profiles, gate mappings and assurance levels under AMD-002 remains subject to multidisciplinary controlled review (governance and assurance methodology, electrical, mechanical and liquid cooling, AI compute, storage and network architecture, operations, OT and security, evidence), calibration and pilot evidence. This amendment does not create certification, engineering approval or assurance by itself.
