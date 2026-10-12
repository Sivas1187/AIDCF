# AIDCF-VAL-001 run log: frame construction and screening

| Field | Value |
|---|---|
| Protocol | AIDCF-VAL-001 Incident Back-Testing Protocol v1.0 |
| Baseline commit | `25ed1f7` (release 3.1 plus validation kits) |
| Frame-freeze date | 2026-10-11 |
| Steps completed | 3 (build the frame) and 4 (screen), protocol section 7.1 and section 6 |
| Steps not started | Second check of EX-02 and EX-04 exclusions; selection draw (section 7.2); archiving; dossiers; coding |

## Screener

All candidates were found and screened by an AI research assistant (Claude), recorded as screener code `C90`. Each row cites a primary or regulator page that was retrieved during screening. Before selection, a human must confirm the screening (BT-REQ-006 requires a second person for every EX-02 and EX-04 call). C90 must not act as Coder A, Coder B or adjudicator.

## Search

The search was split into four non-overlapping source partitions:

| Partition | Sources |
|---|---|
| A | AWS post-event summaries; Google Cloud incident reports |
| B | Microsoft and Azure, GitHub, Cloudflare, Fastly, Meta, Oracle, IBM, Alibaba and other SaaS and infrastructure providers' post-incident reports |
| C | Regulator and public-body reports: FCC, CRTC, Australian Senate and government reviews, Ofcom, UK financial regulators, Singapore MAS, IMDA and MDDI, Japan MIC, and others |
| D | Colocation operators, HPC and supercomputing centres, AI providers and GPU clouds |

All 115 queries are in [`search-log.csv`](search-log.csv).

## Flow (protocol section 7.1, PRISMA style)

| Stage | Count |
|---|---|
| Candidates logged | 221 |
| Excluded | 81: EX-02 low detail 51, EX-01 no primary or regulator source 8, EX-04 out of scope 8, EX-06 source not retrievable 8, EX-05 duplicate 5, EX-03 outside date window 1 |
| Eligible | 140 (92 HIGH, 48 MEDIUM; 106 PRIMARY, 34 REGULATOR) |
| Selected | 0 (selection draw not yet run) |

## Eligible incidents against the section 7.2 targets

The capped capacity column applies the limit of 2 incidents per operator per stratum.

| Stratum | Eligible | Distinct operators | Capped capacity | Target / minimum | Position |
|---|---|---|---|---|---|
| CHANGE_HUMAN | 62 | 31 | 39 | 8 / 5 | Met |
| NETWORK_FABRIC | 22 | 19 | 21 | 8 / 5 | Met |
| CONTROL_PLANE_OT | 16 | 10 | 13 | 8 / 5 | Met |
| EXTERNAL_DEPENDENCY | 13 | 9 | 11 | 8 / 5 | Met |
| POWER | 12 | 7 | 9 | 8 / 5 | Met |
| COOLING | 10 | 7 | 9 | 8 / 5 | Met |
| STORAGE | 5 | 4 | 5 | 8 / 5 | Minimum only; shortfall of 3 against target |

Sub-quota tags among eligible incidents:

| Tag | Count |
|---|---|
| REGULATOR_REPORT | 34 |
| MULTI_SITE | 15 |
| AI_HPC | 14 (the whole-sample target is 14, so every one would have to be selected) |
| BATTERY | 4 |
| FIRE | 3 |
| HEAT_EVENT | 2 |
| WATER_INGRESS | 1 |
| LIQUID_COOLING | 1 (sub-quota is 2: shortfall) |

## Recorded shortfalls and observations (section 7.2, Shortfall)

1. **Liquid cooling.** Only one public incident report with enough detail was found: a coolant distribution unit failure at an HPC centre. Public reporting of liquid-cooling failures is very thin.
2. **Storage-initiated incidents.** Few public reports with enough detail exist outside hyperscale cloud.
3. **AI and GPU clouds and colocation operators.** These rarely publish root-cause reports. Most colocation incidents exist only in press coverage (EX-01). HPC centre status pages are mostly LOW detail.
4. **Operator concentration.** The eligible frame is dominated by providers that publish detailed reviews: Google Cloud 23, Microsoft Azure 17, Cloudflare 13, AWS 11, GitHub 11. The operator caps (6 per sample, 2 per stratum) will bind.
5. **Protocol gap.** Section 7.2 has no stratum for compute-hardware-initiated failures (GPU, node or server faults). Two such candidates were logged with a blank category. A COMPUTE stratum should be considered in protocol v1.1.

## Open items before selection

1. ~~Resolve the three undated rows.~~ Done 2026-10-12. INC-045 (ELIGIBLE) is recorded as DATE_APPROXIMATE, first week of May 2024: neither primary source states the day, and press accounts differ (30 April and about 2 May). The date does not affect its stratum. INC-124 and INC-125 are EXCLUDED, so their dates are not needed.
2. A human second check of every EX-02 and EX-04 exclusion (59 rows), recorded in `exclusion_checked_by`. Agreed procedure: an independent AI cross-check (KAI or DeepSeek) using [`cross-check/PROMPT.md`](cross-check/PROMPT.md) on four batches, then `cross-check/compare.py` lists the disagreements and Siva decides each of those. The run log will record it as "AI cross-check (model, date), human-confirmed".
3. Confirm the provisional categories flagged in `notes`. These are mainly change-initiated incidents filed as CHANGE_HUMAN rather than CONTROL_PLANE_OT, and utility-triggered incidents filed as POWER or COOLING rather than EXTERNAL_DEPENDENCY.
4. Archive every selected source. The Internet Archive could not be reached from the screening environment, so `archive_refs` is empty.
5. Retry these EX-06 sources:
   - Alibaba Cloud Hong Kong 2022;
   - Oracle London 2022;
   - Azure South Central US 2018;
   - the OVHcloud Strasbourg 2021 fire investigation report;
   - the AT&T February 2024 FCC report.
6. Record the selection seed and run the draw.

## Spot verification

Two eligible rows were picked at random and their primary sources fetched again. Both matched the register: INC-035 (Google Cloud, 2022-06-07, fibre cuts) and INC-126 (CenturyLink, 2018-12-27, FCC report).
