# AIDCF errata

Errors found in a published release after it was issued. A released file is never edited in place, because its contents are fixed by the release manifest digest and the published file hashes. Each erratum is recorded here and is corrected in the next release.

| ID | Release | Found | Location | Erratum | Correction |
|---|---|---|---|---|---|
| E-001 | AIDCF-REL-2026.10.1 | 2026-10-13 | AIDCF-015 v1.3 synthetic case: the decision question in `dataset/decision.jsonld` and `dataset/assessment.jsonld` (built by `tools/build_dataset.py`); whitepaper v3.1 section on the synthetic case | The decision question asks whether CI-001 meets SO-01 to SO-03 in NORMAL and MAINTENANCE states. Those are the states the assessment covers, but they do not match the outcomes: SO-02 applies only in RECOVERY, and SO-03 applies in NORMAL and DEGRADED. Within the assessed scope, SO-02 is not assessed at all and SO-03 is assessed only in NORMAL. | The question should read: "Can the synthetic AI training and inference capability CI-001 be relied on to meet SO-01 to SO-03, as far as they apply in NORMAL and MAINTENANCE states, as at 2026-10-10? SO-02 (RECOVERY only) and the DEGRADED state of SO-03 are outside the assessed scope." The computed decision, gate results, score and coverage do not change. Corrected in the next release of AIDCF-015. |
