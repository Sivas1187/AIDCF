# AIDCF-019 Crosswalk: Singapore Baseline

Part of [AIDCF-019 Standards Crosswalks](../README.md). Mapping file: [singapore-mapping.csv](singapore-mapping.csv).

| **Field** | **Value** |
|---|---|
| Artifact ID | AIDCF-019 (crosswalk: Singapore baseline) |
| Version | 1.0 |
| Date | 2026-10-10 |
| Status | Draft for controlled review |
| Author | Siva Sethumadhavan |
| Basis | Singapore regulatory instruments, codes, guidelines, standards and schemes relevant to AI data centres, verified against public sources on 2026-10-10 (§2) |
| Mapping level | Instrument level; section level only for instruments whose structure was verified |
| Review status | Indicative; requires review by a person competent in Singapore digital-infrastructure regulation, and by holders of licensed Singapore Standards |

| **Version** | **Date** | **Summary** |
|---|---|---|
| 1.0 | 2026-10-10 | First issue. |

## 1. Why a Singapore baseline

Singapore is the original target market for AIDCF. It combines a constrained land and energy supply for data centres, a tropical climate, an active green data centre programme, and a regulatory framework for digital infrastructure that has moved within two years from voluntary guidance (2025) to a proposed licensing regime (Bill introduced 2026). An AI data centre operator in Singapore will typically hold or be subject to several of the instruments below at once; the crosswalk shows how each feeds AIDCF evidence and where AIDCF assessment remains necessary.

This crosswalk is not legal advice. Obligations depend on designation, licensing and contractual position, and on instruments whose commencement or final form is pending.

## 2. Instruments mapped (verified)

Each instrument below was verified for name, number, year and scope against the source listed, consulted on 2026-10-10. The `externalRef` column of the CSV uses the short names in the first column.

| Short name in CSV | Instrument | Issuer | Date and status | Scope summary (paraphrased) | Source consulted |
|---|---|---|---|---|---|
| IMDA Advisory Guidelines 2025 | Advisory Guidelines for Resilience and Security of Cloud Services and Data Centres | Infocomm Media Development Authority (IMDA) | Issued 25 February 2025; voluntary (providers encouraged to adopt) | Risk assessment, business impact analysis and continuity planning; cybersecurity measures, security testing and access control; cloud data governance and disaster recovery; for data centres, a business continuity management system and cybersecurity risks. Addresses misconfiguration, physical hazards such as fire and cooling failure, and cyber-attack. | IMDA press release, 25 Feb 2025 |
| Digital Infrastructure Bill (2026) | Digital Infrastructure Bill | Ministry of Digital Development and Information (MDDI); to be administered by IMDA | Public consultation 1–22 July 2026; First Reading announced 8 September 2026; **not enacted** as at 2026-10-10 | Two proposed licensing regimes. Resilience and security: co-location and cloud data centres of at least 10 MW critical IT load and major cloud service providers above a Singapore revenue threshold; security risk management measures, business continuity and disaster recovery plans, reporting of specified incidents. Energy efficiency: data centres of at least 3 MW critical IT load; facility PUE requirements, with IT-equipment and water-efficiency requirements possible later. | MDDI newsroom, 8 Sep 2026 |
| Cybersecurity Act 2018 as amended 2024 | Cybersecurity Act 2018, as amended by the Cybersecurity (Amendment) Act 2024 | Parliament of Singapore; administered by the Cyber Security Agency of Singapore (CSA) | Amendment Bill passed 7 May 2024; commencement of the foundational digital infrastructure provisions to be verified | Adds regulation of foundational digital infrastructure (FDI) service providers, which include cloud computing and data centre facility services, alongside CII, entities of special cybersecurity interest and systems of temporary cybersecurity concern. | Legal commentary (RPC, 2024); primary text to be consulted |
| CCoP-CII 2026 | Cybersecurity Code of Practice for Critical Information Infrastructure 2026 (Release 1) | Commissioner of Cybersecurity (CSA), under the Cybersecurity Act 2018 | Effective 29 July 2026; supersedes the Second Edition (2022, Revision One effective 12 December 2022); phased compliance into 2027 | Sections: 1 Preliminary; 2 Audit; 3 Governance (including Cyber Trust mark certification and outsourcing management); 4 Identification; 5 Protection; 6 Detection; 7 Response and Recovery; 8 Cyber Resiliency; 9 Training and Awareness; 10 Operational Technology Security; 11 Domain-Specific Practices; 12 Securing CII Interconnected Systems. Applies to designated CII owners. | CSA Codes of Practice page and published PDF |
| CSA Guidelines and Companion Guide on Securing AI Systems (2024) | Guidelines on Securing AI Systems; Companion Guide on Securing AI Systems | CSA | Published 15 October 2024; guidance; Companion Guide is a non-prescriptive, community-driven living resource | Security of AI systems throughout their lifecycle. | CSA publications page |
| BCA-IMDA Green Mark for Data Centres 2024 | Green Mark for Data Centre 2024 criteria (GMDC:2024) | Building and Construction Authority (BCA) and IMDA | Launched 18 October 2024; replaces GMDC:2019 | Criteria areas include energy efficiency in operation, intelligent systems, carbon reduction, health and well-being, resilience and maintainability. Ratings (Gold, GoldPLUS, Platinum) are time-limited and renewed. | Singapore Green Building Council article; IMDA scheme page |
| SS 564-1:2020; SS 564-2:2020 | Singapore Standard SS 564, Green data centres (Part 1 energy and environmental management systems; Part 2 guidance) | Singapore Standards Council (with IMDA) | 2020 editions current on the Singapore Standards eShop; series first published 2011, revised 2013 | Energy and environmental management system for data centres aligned with ISO 50001 (Plan-Do-Check-Act), with data-centre energy-efficiency metrics and practices. | IMDA green data centre standard page; Singapore Standards eShop listings |
| SS 697:2023 | Singapore Standard SS 697, Tropical Data Centre | Singapore Standards Council (with IMDA) | 2023 | Method and guidelines for safely and gradually raising data centre operating temperatures in tropical climates. | IMDA Tropical DC Standard page; eShop listing |
| SS 715:2025 | Singapore Standard SS 715, Energy Efficiency of Data Centre IT Equipment | Singapore Standards Council (with IMDA) | Launched 13 August 2025 | Selection of IT equipment meeting international energy-efficiency baselines; IT energy management practices (consolidation, virtualisation, utilisation); IT equipment able to operate at higher temperatures. | IMDA press release, 13 Aug 2025 |
| SS 726:2026 | Singapore Standard SS 726, Liquid Cooling in Tropical Data Centres | IMDA and Enterprise Singapore through the Singapore Standards Council | Launched 27 August 2026 | Guidance for implementing liquid cooling in tropical data centres, including alongside air cooling. Detailed technical scope not verified. | Enterprise Singapore media release, 27 Aug 2026 |
| MAS TRM 2021 | MAS Technology Risk Management Guidelines | Monetary Authority of Singapore (MAS) | Issued 18 January 2021 | Technology risk governance and oversight, risk management framework, third-party services, IT service management, IT resilience (including data centre resilience), access control, data and infrastructure security, cyber security operations and assessment, IT audit. Applies to MAS-regulated financial institutions, and so to financial-sector tenants and their providers by contract. Section numbers in the CSV were checked against a secondary source only. | Legal commentary (Linklaters, 2021); vendor compliance brief |
| MAS BCM 2022 | MAS Guidelines on Business Continuity Management | MAS | Issued 6 June 2022; expected to be met within 12 months | Identification of critical business services, service recovery time objectives, end-to-end dependency mapping, concentration risk, testing, independent audit, board and senior-management attestation. | Legal commentary (Allen & Gledhill, 2022) |

## 3. Instruments to be verified (not mapped)

These items were identified as relevant but could not be verified to the standard required for mapping on 2026-10-10. They shall not be relied upon until verified.

| Item | What is known | What must be verified before mapping |
|---|---|---|
| Cybersecurity Code of Practice for Cloud Services | Legal commentary reports that CSA planned to publish it in the second half of 2026, with companion guides | Publication, title, scope, applicability to data centre operators |
| Commencement of FDI provisions of the Cybersecurity (Amendment) Act 2024 | Amendment passed 7 May 2024 | Commencement date; any FDI designations or codes affecting data centres |
| Subsidiary legislation and licence conditions under the Digital Infrastructure Bill | Bill at First Reading; resilience, security and PUE obligations described at policy level | Enactment; licence conditions; incident thresholds; PUE values and measurement method |
| Detailed technical scope of SS 726:2026 | Title and high-level purpose verified | Cooling technologies covered (direct-to-chip, immersion, rear-door), CDU and secondary-loop requirements, water and safety provisions |
| Detailed criteria of GMDC:2024 | Criteria areas verified at headline level | Section structure, water criteria, IT-load criteria, resilience criteria content |
| SS 564-2:2020 exact title | Part 2 provides guidance on Part 1 | Exact title and relationship to ISO 50001:2018 |
| MAS TRM 2021 section numbering | Section topics confirmed from secondary sources | Section numbers and titles against the MAS original |
| Multi-Tier Cloud Security standard (SS 584) and other IMDA cloud standards | Candidate from earlier project research | Current edition and relevance to data centre infrastructure |
| Fire-safety and electrical-installation regulation applicable to data centres (SCDF fire code; Energy Market Authority electrical licensing) | Relevant to PHY-06 and POW families | Instrument names, current editions and data-centre-specific provisions |
| IMDA Green Data Centre Roadmap | Policy roadmap referenced in commentary | Status as policy (not a requirement) and any targets relevant to ENV families |

## 4. Where Singapore instruments overlap with AIDCF

- **Resilience and continuity (RES, CAP-03, DEP).** The IMDA Advisory Guidelines, the Digital Infrastructure Bill and the MAS BCM Guidelines converge on business impact analysis, continuity and disaster recovery planning, testing and incident reporting. MAS BCM's service recovery time objectives and end-to-end dependency mapping are close in intent to AIDCF Recovery Outcomes and DEP-01 for financial-sector tenants.
- **Energy and environment (ENV-02 to ENV-04, CAP-05).** SS 564, Green Mark for Data Centres, SS 715, SS 697 and the proposed PUE licensing requirement together give dense energy-performance coverage (ENV-02 is a HIGH-confidence PARTIAL, as it is for EN 50600).
- **Tropical thermal envelope (CAP-05, ENV-01, THM-03).** SS 697 and SS 715 encourage higher operating temperatures; SS 726 addresses liquid cooling in the tropics. These directly affect AIDCF thermal envelope parameters and the resilience-efficiency trade-off (ENV-02).
- **Cybersecurity and OT (SEC).** CCoP-CII 2026 sections 3 to 10 and 12 overlap SEC-01 to SEC-05 and DEP-05 where the data centre is CII or supports CII; section 10 covers OT security relevant to BMS and EPMS (SEC-02).
- **AI systems (SEC-06).** The CSA Guidelines on Securing AI Systems are the Singapore reference for AI-system security; their application to AI agents acting on infrastructure is by extension.

## 5. Where AIDCF goes beyond the Singapore baseline

- **Engineering depth.** The resilience instruments name power failure, cooling failure and fire as risks but, at the level verified, do not set engineering criteria for electrical supply, heat removal, liquid-cooling integrity or AI load transients. AIDCF POW, THM and CG-04 to CG-06 supply these.
- **AI infrastructure.** No verified Singapore instrument addresses accelerator clusters, scale-up domains, AI fabrics, checkpoint storage or their recovery (CMP, STO, NET).
- **Evidence and decisions.** The instruments require plans, audits and reports; AIDCF adds evidence quality and sufficiency, UNKNOWN Records and gate-based bounded decisions that can be reused across these regimes.
- **Supply chain.** Hardware provenance, firmware supply and spares (SUP-03 to SUP-05) are not addressed beyond outsourcing management and AI supply-chain guidance.

## 6. Using Singapore outputs as AIDCF evidence

| Output | AIDCF evidence class | Useful for | Limits |
|---|---|---|---|
| Green Mark for Data Centres rating and assessment report | E5 | ENV-02, ENV-04, OPS-03 context; EVA-06 validity | Rating period; facility scope; not an energy-allocation per Capability Instance |
| SS 564 EnMS certification (where held) | E5 | ENV-02 management-system evidence | Management-system conformity; measurement boundary must be confirmed |
| PUE submissions to IMDA (once licensed) | E3/E7 | ENV-02 PUE Measurement | Regulatory measurement method may differ from EN 50600-4-2; reconcile |
| CCoP-CII audit reports; Cyber Trust mark certificate | E5 | SEC-01 to SEC-05, GOV-04, EVA-03 | Applies only to designated CII; scope may exclude facility OT |
| Incident reports to IMDA or CSA | E3 | OPS-04, RES-06, EVA-04 | Reportable threshold differs from AIDCF Finding threshold |
| BCM/BCP and DR test records (IMDA guidelines, MAS BCM) | E4 | RES-03 to RES-05 | Often scoped to business services rather than infrastructure state transitions |

## 7. Coverage summary

| Relationship | Families | Share of 90 |
|---|---:|---:|
| EQUIVALENT | 0 | 0% |
| PARTIAL | 29 | 32% |
| SUPPORTS_EVIDENCE | 1 | 1% |
| CONTEXT | 12 | 13% |
| NO_MATCH | 48 | 53% |
| **Total** | **90** | **100%** |

Coverage by AIDCF domain (count of families with EQUIVALENT or PARTIAL / SUPPORTS_EVIDENCE / CONTEXT / NO_MATCH, out of 6):

| Domain | EQ or PARTIAL | SUPPORTS_EVIDENCE | CONTEXT | NO_MATCH |
|---|---:|---:|---:|---:|
| GOV | 5 | 0 | 0 | 1 |
| CAP | 2 | 0 | 1 | 3 |
| DEP | 4 | 0 | 0 | 2 |
| PHY | 0 | 0 | 2 | 4 |
| POW | 0 | 0 | 1 | 5 |
| THM | 1 | 0 | 1 | 4 |
| ENV | 3 | 0 | 2 | 1 |
| CMP | 0 | 0 | 2 | 4 |
| STO | 0 | 0 | 0 | 6 |
| NET | 0 | 0 | 0 | 6 |
| OPS | 1 | 0 | 1 | 4 |
| RES | 5 | 0 | 0 | 1 |
| SUP | 2 | 0 | 1 | 3 |
| SEC | 6 | 0 | 0 | 0 |
| EVA | 0 | 1 | 1 | 4 |

### AIDCF differentiation

48 AIDCF families have no corresponding provision in this framework (NO_MATCH). These are where AIDCF assurance goes beyond it; evidence for them must come from AIDCF-specific assessment or another crosswalked framework.

| Domain | Families with NO_MATCH |
|---|---|
| GOV | GOV-06 Ethics, impartiality and competence |
| CAP | CAP-01 Capability inventory; CAP-04 Demand and growth modelling; CAP-06 Capability lifecycle and change |
| DEP | DEP-02 Shared and common-mode dependencies; DEP-06 Dependency monitoring and review |
| PHY | PHY-02 Building and structural integrity; PHY-03 Physical zoning and segregation; PHY-04 Access and surveillance; PHY-05 Asset movement and custody |
| POW | POW-02 Generation and fuel; POW-03 UPS and energy storage; POW-04 Distribution and protection; POW-05 Power quality and transient response; POW-06 Electrical monitoring, maintenance and recovery |
| THM | THM-02 Air cooling systems; THM-04 Heat rejection and water systems; THM-05 Fluid quality and leak management; THM-06 Thermal control, maintenance and recovery |
| ENV | ENV-05 Hazardous materials and waste |
| CMP | CMP-02 Cluster and scale-up domains; CMP-04 Firmware, driver and compatibility; CMP-05 Compute health and observability; CMP-06 Compute lifecycle and recovery |
| STO | STO-01 Storage architecture and tiering; STO-02 Performance and capacity; STO-03 Integrity and consistency; STO-04 Protection and replication; STO-05 Checkpoint and recovery services; STO-06 Storage monitoring and lifecycle |
| NET | NET-01 Scale-up and scale-out fabrics; NET-02 Performance and congestion control; NET-03 Storage and service networks; NET-04 Management and out-of-band networks; NET-05 Physical connectivity and optics; NET-06 Network control and observability |
| OPS | OPS-01 Operating model and staffing; OPS-02 Procedure and work control; OPS-05 Change and configuration management; OPS-06 Capacity and service operations |
| RES | RES-02 Fault-domain and containment design |
| SUP | SUP-03 Hardware and component provenance; SUP-05 Spares, logistics and obsolescence; SUP-06 Remote support and third-party access |
| EVA | EVA-01 Evidence architecture; EVA-02 Evidence provenance and quality; EVA-04 Findings, UNKNOWN and limitations; EVA-05 Critical gates and decisions |

## 8. Review status

Indicative. The regulatory position changes frequently (in 2026 alone: CCoP-CII 2026, SS 726:2026 and the Digital Infrastructure Bill). Re-verify every instrument in §2 and §3 before reliance, and require review by a person competent in Singapore digital-infrastructure regulation (AIDCF-019 §7, XW-REQ-006).

### Sources consulted (2026-10-10)

- IMDA, "IMDA introduces Advisory Guidelines to enhance the resilience and security of Cloud Services and Data Centres", press release, 25 February 2025: https://imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2025/advisory-guidelines-of-cloud-services-and-data-centres
- MDDI, "New Digital Infrastructure Bill to strengthen the foundations for Singapore's digital economy", 8 September 2026: https://www.mddi.gov.sg/newsroom/new-digital-infrastructure-bill-to-strengthen-the-foundations-for-singapore-s-digital-economy/
- CSA, Codes of Practice: https://www.csa.gov.sg/legislation/codes-of-practice/ ; CCoP Second Edition Revision One (PDF): https://www.csa.gov.sg/docs/default-source/legislation/ccop---second-edition_revision-one.pdf
- CSA, Guidelines and Companion Guide on Securing AI Systems: https://www.csa.gov.sg/resources/publications/guidelines-and-companion-guide-on-securing-ai-systems/
- IMDA, Green Data Centre Standard (SS 564): https://imda.gov.sg/industry-development/infrastructure/ict-standards-and-frameworks/green-data-centre-standard
- IMDA, Tropical DC Standard (SS 697): https://www.imda.gov.sg/how-we-can-help/green-dc-roadmap/tropical-dc-standard
- IMDA, SS 715 launch press release, 13 August 2025: https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2025/sg-it-energy-efficiency-standard-for-data-centres-launched
- Enterprise Singapore, SS 726 launch media release, 27 August 2026: https://www.enterprisesg.gov.sg/resources/media-centre/media-releases/2026/august/mr03826_singapore-launches-worlds-first-liquid-cooling-standard-for-data-centres-in-tropical-climates
- IMDA, BCA-IMDA Green Mark for Data Centres scheme: https://imda.gov.sg/how-we-can-help/bca-imda-green-mark-for-data-centres-scheme ; SGBC, GMDC:2024 launch: https://www.sgbc.sg/?p=7229
- Singapore Standards eShop listings for SS 564-1:2020, SS 564-2:2020 and SS 697:2023
- Secondary: Linklaters (MAS TRM, 2021); Allen & Gledhill (MAS BCM, 2022); RPC (Cybersecurity Act amendments, 2024); Rajah & Tann Asia (CCoP-CII 2026 and Cloud CCoP)
